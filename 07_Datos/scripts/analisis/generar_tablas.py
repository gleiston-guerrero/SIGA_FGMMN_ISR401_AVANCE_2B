# -*- coding: utf-8 -*-
"""
Genera las tablas del manuscrito en LaTeX a partir de los resultados del
pipeline. No se escribe ninguna cifra a mano: todo sale de los CSV que
produjo analizar_resultados.py.

Uso (ver Makefile, objetivo `tablas`):
    python generar_tablas.py --entrada ../resultados --salida ../../tablas \
        [--procesados ../datos_procesados]

Genera:
    tabla_descriptivos.tex   — mediana, media, sd, min, max, IQR por dimension y origen
    tabla_supuestos.tex      — Shapiro-Wilk y Levene por dimension
    tabla_hipotesis.tex      — prueba, estadistico, p, p ajustado Holm, tamano de efecto e IC 95%
    tabla_acuerdo.tex        — kappa de Cohen por par y kappa de Fleiss
"""
import argparse
import os

import numpy as np
import pandas as pd

DIMENSIONES = [
    "Completitud(1-5)", "Ausencia_ambiguedad(1-5)", "Verificabilidad(1-5)",
    "Correccion_fuente(1-5)", "Consistencia_interna(1-5)",
]


_ESCAPES_LATEX = {
    "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#", "_": r"\_",
    "{": r"\{", "}": r"\}", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}",
}


def _escapar_latex(texto):
    return "".join(_ESCAPES_LATEX.get(c, c) for c in str(texto))


def _formatear_celda(valor):
    if pd.isna(valor):
        return "--"
    if isinstance(valor, (bool, np.bool_)):
        return "Sí" if valor else "No"
    if isinstance(valor, (float, np.floating)):
        return f"{valor:.3f}"
    return _escapar_latex(valor)


# Cabeceras cortas para el manuscrito. Los nombres de columna de los CSV son
# descriptivos a proposito --- Shapiro_p_Humano, Varianzas_homogeneas --- pero
# nueve de ellos no caben en el ancho de pagina de LNCS. El CSV no se toca: solo
# cambia como se rotulan en la tabla impresa.
CABECERAS = {
    "Dimension": "Dimension",
    "n_jueces": "$n$",
    "Shapiro_p_Humano": "SW $p$ (Human)",
    "Shapiro_p_LLM": "SW $p$ (LLM)",
    "Normal_Humano": "Normal (H)",
    "Normal_LLM": "Normal (L)",
    "Levene_estadistico": "Levene $W$",
    "Levene_p": "Levene $p$",
    "Varianzas_homogeneas": "Equal var.",
    "Prueba": "Test",
    "Estadistico_nombre": "Stat.",
    "Estadistico_valor": "Value",
    "p_valor": "$p$",
    "p_valor_ajustado": "$p_{\\mathrm{holm}}$",
    "Significativo_holm": "Sig.",
    "Tamano_efecto_nombre": "Effect size",
    "Tamano_efecto_valor": "Value",
    "IC95_inferior": "CI low",
    "IC95_superior": "CI high",
    # tabla_hipotesis
    "p_valor_ajustado_holm": "$p_{\\mathrm{holm}}$",
    "Tipo_efecto": "Effect size (per requirement)",
    "Valor": "Value",
    "IC 95%": "95\\% CI",
    # tabla_descriptivos
    "Dimensión": "Dimension",
    "Origen": "Source",
    "Mediana": "Median",
    "Media": "Mean",
    "DE": "SD",
    "Mín": "Min",
    "Máx": "Max",
    "RIC": "IQR",
    # tabla_acuerdo
    "Cohen_kappa_juez1_juez2": "$\\kappa$ J1--J2",
    "Cohen_kappa_juez1_juez3": "$\\kappa$ J1--J3",
    "Cohen_kappa_juez2_juez3": "$\\kappa$ J2--J3",
    "Fleiss_kappa_3jueces": "Fleiss $\\kappa$",
    # tabla_power_calculation
    "Cohen d objetivo": "Target Cohen's $d$",
    "Potencia deseada": "Target power",
    "n necesario (exacto)": "$n$ needed",
    "n necesario (redondeado)": "$n$ needed (rounded)",
    "n actual": "$n$ actual",
    "Potencia alcanzada con n actual": "Power achieved",
}


def _rotulo(columna):
    return CABECERAS.get(columna, _escapar_latex(columna))


def _df_a_latex(df, caption, label):
    """
    Genera una tabla LaTeX equivalente a df.to_latex(), sin depender de
    jinja2 (pandas >= 2.1 enruta DataFrame.to_latex por el Styler, que
    exige jinja2 como dependencia opcional no listada en el README).

    La tabla se envuelve en \\resizebox para que quepa en el ancho de la caja
    de texto: varias tienen nueve columnas y se salian del margen derecho.
    """
    columnas = list(df.columns)
    alineacion = "l" * len(columnas)
    lineas = [
        r"\begin{table}[htbp]",
        r"\centering",
        r"\footnotesize",
        f"\\caption{{{_escapar_latex(caption)}}}",
        f"\\label{{{label}}}",
        r"\resizebox{\textwidth}{!}{%",
        f"\\begin{{tabular}}{{{alineacion}}}",
        r"\toprule",
        " & ".join(_rotulo(c) for c in columnas) + r" \\",
        r"\midrule",
    ]
    for _, fila in df.iterrows():
        lineas.append(" & ".join(_formatear_celda(fila[c]) for c in columnas) + r" \\")
    lineas += [r"\bottomrule", r"\end{tabular}%", r"}", r"\end{table}", ""]
    return "\n".join(lineas)


def _escribir_tex(df, ruta, caption, label):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    latex = _df_a_latex(df, caption, label)
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(latex)
    print(f"Escrita: {ruta}")


def tabla_descriptivos(procesados_dir, salida_dir):
    ruta = os.path.join(procesados_dir, "puntuaciones_consolidadas.csv")
    if not os.path.exists(ruta):
        print(f"AVISO: no existe {ruta}; se omite tabla_descriptivos.")
        return
    df = pd.read_csv(ruta, encoding="utf-8-sig")

    filas = []
    for dim in DIMENSIONES:
        for origen in ["Humano", "LLM"]:
            sub = df[(df["dimension"] == dim) & (df["origen"] == origen)]["puntuacion"]
            if sub.empty:
                continue
            q1, q3 = sub.quantile([0.25, 0.75])
            filas.append({
                "Dimensión": dim.replace("(1-5)", ""),
                "Origen": origen,
                "Mediana": sub.median(),
                "Media": sub.mean(),
                "DE": sub.std(ddof=1),
                "Mín": sub.min(),
                "Máx": sub.max(),
                "RIC": q3 - q1,
            })
    resultado = pd.DataFrame(filas)
    _escribir_tex(resultado, os.path.join(salida_dir, "tabla_descriptivos.tex"),
                  "Descriptive statistics by quality dimension and requirement source", "tab:descriptivos")


def tabla_supuestos(resultados_dir, salida_dir):
    ruta = os.path.join(resultados_dir, "supuestos.csv")
    if not os.path.exists(ruta):
        print(f"AVISO: no existe {ruta}; se omite tabla_supuestos.")
        return
    df = pd.read_csv(ruta, encoding="utf-8-sig")
    df["Dimension"] = df["Dimension"].str.replace(r"\(1-5\)", "", regex=True)
    _escribir_tex(df, os.path.join(salida_dir, "tabla_supuestos.tex"),
                  "Assumption checks: normality (Shapiro-Wilk) and homogeneity of variances (Levene)",
                  "tab:supuestos")


def tabla_hipotesis(resultados_dir, salida_dir):
    ruta_hip = os.path.join(resultados_dir, "hipotesis.csv")
    ruta_efe = os.path.join(resultados_dir, "efectos.csv")
    if not (os.path.exists(ruta_hip) and os.path.exists(ruta_efe)):
        print("AVISO: falta hipotesis.csv o efectos.csv; se omite tabla_hipotesis.")
        return
    hip = pd.read_csv(ruta_hip, encoding="utf-8-sig")
    efe = pd.read_csv(ruta_efe, encoding="utf-8-sig")
    fusion = hip.merge(efe, on="Dimension")
    fusion["Dimension"] = fusion["Dimension"].str.replace(r"\(1-5\)", "", regex=True)
    fusion["IC 95%"] = fusion.apply(
        lambda r: f"[{r['IC95_inferior']:.3f}, {r['IC95_superior']:.3f}]"
        if pd.notna(r["IC95_inferior"]) else "--", axis=1)
    # El contraste es el apareado sobre los tres jueces, preregistrado. El
    # tamano del efecto se calcula con el requisito como unidad (25 frente a
    # 26): con n = 3 un efecto estandarizado no tiene intervalo interpretable.
    columnas = ["Dimension", "Prueba", "Estadistico_nombre", "Estadistico_valor",
                "p_valor", "p_valor_ajustado_holm", "Tipo_efecto", "Valor", "IC 95%"]
    resultado = fusion[columnas]
    _escribir_tex(resultado, os.path.join(salida_dir, "tabla_hipotesis.tex"),
                  "Paired hypothesis tests by dimension (n = 3 judges) with Holm-Bonferroni correction, "
                  "and effect sizes with the requirement as the unit (25 human vs. 26 LLM)",
                  "tab:hipotesis")


def tabla_acuerdo(resultados_dir, salida_dir):
    ruta = os.path.join(resultados_dir, "acuerdo_interevaluador.csv")
    if not os.path.exists(ruta):
        print(f"AVISO: no existe {ruta}; se omite tabla_acuerdo.")
        return
    df = pd.read_csv(ruta, encoding="utf-8-sig")
    df["Dimension"] = df["Dimension"].str.replace(r"\(1-5\)", "", regex=True)
    _escribir_tex(df, os.path.join(salida_dir, "tabla_acuerdo.tex"),
                  "Inter-rater agreement: pairwise Cohen kappa and overall Fleiss kappa",
                  "tab:acuerdo")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--entrada", required=True, help="Carpeta resultados/")
    ap.add_argument("--salida", required=True, help="Carpeta tablas/ del reporte")
    ap.add_argument("--procesados", default=None,
                     help="Carpeta datos_procesados/ (por defecto, ../datos_procesados relativo a --entrada)")
    args = ap.parse_args()

    procesados = args.procesados or os.path.join(args.entrada, "..", "datos_procesados")

    tabla_descriptivos(procesados, args.salida)
    tabla_supuestos(args.entrada, args.salida)
    tabla_hipotesis(args.entrada, args.salida)
    tabla_acuerdo(args.entrada, args.salida)


if __name__ == "__main__":
    main()
