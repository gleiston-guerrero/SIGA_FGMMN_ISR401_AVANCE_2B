# -*- coding: utf-8 -*-
"""Analisis de sensibilidad tomando el requisito como unidad de analisis.

POR QUE EXISTE ESTE SCRIPT
--------------------------
El plan preregistrado en OSF compara las medias por dimension tomando **al juez**
como unidad de analisis: promedia los items de cada origen dentro de cada juez y
aplica una prueba apareada sobre n = 3. Ese diseno es defendible --- controla la
severidad de cada juez --- pero deja el estudio con una potencia de 0,084 y con
intervalos de confianza del tamano del efecto que no se pueden interpretar.

Este script no sustituye a ese analisis: lo acompana. Toma el **requisito** como
unidad, promediando los tres jueces en cada item, con lo que la comparacion pasa
de n = 3 a n = 51 (25 requisitos humanos frente a 26 generados por el modelo).
Al no estar apareados los conjuntos --- son requisitos distintos, no el mismo
requisito medido dos veces --- la prueba es de muestras independientes.

Es un analisis **exploratorio y posterior al registro**. Se declara como tal en
la bitacora de desviaciones y en el manuscrito, y el analisis primario sigue
siendo el preregistrado.

Uso:
    python analisis_por_item.py --entrada ../datos_procesados \\
        --salida ../resultados --tabla ../../07_Publicacion/tablas
"""
import argparse
import csv
import io
import os
import sys

import numpy as np
from scipy import stats

SEMILLA = 20260802
N_BOOT = 10000
DIMENSIONES = ["Completitud(1-5)", "Ausencia_ambiguedad(1-5)", "Verificabilidad(1-5)",
               "Correccion_fuente(1-5)", "Consistencia_interna(1-5)"]


def cargar(ruta):
    """Devuelve {dimension: {'Humano': [medias por item], 'LLM': [...]}}."""
    por_item = {}
    with io.open(ruta, encoding="utf-8") as f:
        for fila in csv.DictReader(f):
            k = (fila["dimension"], fila["item_ciego"], fila["origen"])
            por_item.setdefault(k, []).append(float(fila["puntuacion"]))
    datos = {d: {"Humano": [], "LLM": []} for d in DIMENSIONES}
    for (dim, item, origen), vs in sorted(por_item.items()):
        if dim in datos:
            datos[dim][origen].append(sum(vs) / len(vs))
    return datos


def cliff(a, b):
    """Delta de Cliff: probabilidad de superioridad, sin supuestos de forma."""
    a, b = np.asarray(a), np.asarray(b)
    mayor = sum((x > b).sum() for x in a)
    menor = sum((x < b).sum() for x in a)
    return (mayor - menor) / float(len(a) * len(b))


def hedges(a, b):
    """g de Hedges: d de Cohen con la correccion de sesgo para muestras pequenas."""
    a, b = np.asarray(a), np.asarray(b)
    na, nb = len(a), len(b)
    s = np.sqrt(((na - 1) * a.var(ddof=1) + (nb - 1) * b.var(ddof=1)) / (na + nb - 2))
    if s == 0:
        return 0.0
    d = (a.mean() - b.mean()) / s
    J = 1 - 3.0 / (4 * (na + nb) - 9)
    return d * J


def ic_bootstrap(a, b, fn, rng):
    a, b = np.asarray(a), np.asarray(b)
    vals = np.empty(N_BOOT)
    for i in range(N_BOOT):
        vals[i] = fn(rng.choice(a, len(a), replace=True),
                     rng.choice(b, len(b), replace=True))
    return float(np.percentile(vals, 2.5)), float(np.percentile(vals, 97.5))


def holm(ps):
    """p ajustados por Holm-Bonferroni, devueltos en el orden original."""
    m = len(ps)
    orden = sorted(range(m), key=lambda i: ps[i])
    aj = [0.0] * m
    previo = 0.0
    for k, i in enumerate(orden):
        v = min(1.0, (m - k) * ps[i])
        previo = max(previo, v)
        aj[i] = previo
    return aj


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--entrada", required=True, help="carpeta con puntuaciones_consolidadas.csv")
    ap.add_argument("--salida", required=True, help="carpeta de resultados")
    ap.add_argument("--tabla", required=True, help="carpeta donde escribir la tabla LaTeX")
    a = ap.parse_args()

    rng = np.random.default_rng(SEMILLA)
    datos = cargar(os.path.join(a.entrada, "puntuaciones_consolidadas.csv"))

    filas, ps = [], []
    for dim in DIMENSIONES:
        h, l = datos[dim]["Humano"], datos[dim]["LLM"]
        # normalidad por grupo; decide la prueba, igual que el analisis primario
        sh_h = stats.shapiro(h).pvalue if len(h) >= 3 else float("nan")
        sh_l = stats.shapiro(l).pvalue if len(l) >= 3 else float("nan")
        normal = sh_h > 0.05 and sh_l > 0.05
        if normal:
            est, p = stats.ttest_ind(h, l, equal_var=False)
            nombre, efecto, ef_nom = "t de Welch", hedges(h, l), "g de Hedges"
            ic = ic_bootstrap(h, l, hedges, rng)
        else:
            est, p = stats.mannwhitneyu(h, l, alternative="two-sided")
            nombre, efecto, ef_nom = "U de Mann-Whitney", cliff(h, l), "delta de Cliff"
            ic = ic_bootstrap(h, l, cliff, rng)
        ps.append(float(p))
        filas.append({
            "Dimension": dim,
            "n_humano": len(h), "n_llm": len(l),
            "Media_Humano": round(float(np.mean(h)), 4),
            "Media_LLM": round(float(np.mean(l)), 4),
            "Prueba": nombre,
            "Estadistico": round(float(est), 4),
            "p_valor": round(float(p), 4),
            "Tipo_efecto": ef_nom,
            "Tamano_efecto": round(float(efecto), 4),
            "IC95_inferior": round(ic[0], 4),
            "IC95_superior": round(ic[1], 4),
        })

    for f, pa in zip(filas, holm(ps)):
        f["p_ajustado_holm"] = round(pa, 4)
        f["significativo_alpha_05"] = "Si" if pa < 0.05 else "No"

    os.makedirs(a.salida, exist_ok=True)
    campos = list(filas[0].keys())
    with io.open(os.path.join(a.salida, "analisis_por_item.csv"), "w",
                 encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=campos, lineterminator="\n")
        w.writeheader()
        w.writerows(filas)

    # potencia alcanzada con el tamano de efecto observado mas grande
    from statsmodels.stats.power import TTestIndPower
    mayor = max(abs(f["Tamano_efecto"]) for f in filas
                if f["Tipo_efecto"] == "g de Hedges") if any(
        f["Tipo_efecto"] == "g de Hedges" for f in filas) else 0.5
    pot = TTestIndPower().power(effect_size=0.5, nobs1=25, ratio=26 / 25.0,
                                alpha=0.05, alternative="two-sided")

    os.makedirs(a.tabla, exist_ok=True)
    tex = [r"\begin{table}[htbp]", r"\centering",
           r"\caption{Sensitivity analysis with the requirement as the unit of analysis "
           r"(exploratory, post-registration). Human $n=25$, LLM $n=26$; judge scores "
           r"averaged per item.}",
           r"\label{tab:por-item}", r"\small", r"\begin{tabular}{lccccc}", r"\toprule",
           r"Dimension & Human & LLM & Test statistic & $p$ (Holm) & Effect size [95\% CI] \\",
           r"\midrule"]
    corto = {"Completitud(1-5)": "Completeness", "Ausencia_ambiguedad(1-5)": "Non-ambiguity",
             "Verificabilidad(1-5)": "Verifiability", "Correccion_fuente(1-5)": "Source correctness",
             "Consistencia_interna(1-5)": "Internal consistency"}
    for f in filas:
        tex.append("%s & %.2f & %.2f & %.3f & %.4f & %.3f [%.3f, %.3f] \\\\" % (
            corto[f["Dimension"]], f["Media_Humano"], f["Media_LLM"],
            f["Estadistico"], f["p_ajustado_holm"], f["Tamano_efecto"],
            f["IC95_inferior"], f["IC95_superior"]))
    tex += [r"\bottomrule", r"\end{tabular}", r"\end{table}"]
    io.open(os.path.join(a.tabla, "tabla_por_item.tex"), "w",
            encoding="utf-8", newline="\n").write("\n".join(tex) + "\n")

    print("  analisis por item: n = %d humanos, %d del modelo" % (filas[0]["n_humano"], filas[0]["n_llm"]))
    print("  potencia para d = 0,5 con esos tamanos: %.3f  (era 0,084 con n = 3)" % pot)
    for f in filas:
        print("    %-28s %-18s p_holm=%.4f  %s=%.3f [%.3f, %.3f]" % (
            f["Dimension"], f["Prueba"], f["p_ajustado_holm"],
            f["Tipo_efecto"].split()[0], f["Tamano_efecto"],
            f["IC95_inferior"], f["IC95_superior"]))


if __name__ == "__main__":
    main()
