# -*- coding: utf-8 -*-
"""
Curva de saturación temática — Proyecto SIGA (Entrega 4, 2B).

Cuenta, en orden cronológico de entrevista, cuántos códigos temáticos
NUEVOS (nunca vistos en una entrevista anterior) aparecen en cada
entrevista, y evalúa el criterio de saturación de la Sección 3 de la
guía: "saturado cuando, en las últimas tres entrevistas, el promedio de
códigos nuevos por entrevista es <= 5% del total acumulado".

La fecha de cada entrevista se toma de transcripciones_anonimizadas.json
(no se hardcodea), para que la curva se pueda regenerar automáticamente
si cambia el corpus de transcripciones.

Uso:
    python curva_saturacion.py --entrada ../../02_Evidencias/Codificacion_Tematica/codificacion_tematica.csv \
        --salida ../../figuras/curva_saturacion.png \
        --tabla ../../tablas/saturacion_por_entrevista.csv
"""
import argparse
import json
import os
import re

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

FECHAS_JSON_DEFAULT = os.path.join(
    os.path.dirname(__file__), "..", "datos_crudos",
    "transcripciones_anonimizadas.json",
)


def cargar_fechas(ruta_json):
    # utf-8-sig: tolera un BOM inicial si el archivo se genero o se edito
    # con herramientas de Windows (p. ej. PowerShell Set-Content -Encoding utf8).
    with open(ruta_json, "r", encoding="utf-8-sig") as f:
        datos = json.load(f)
    return {t["id_evidencia"]: t["fecha"] for t in datos["transcripciones"]}


def cargar_codificacion(ruta_csv):
    df = pd.read_csv(ruta_csv, engine="python", on_bad_lines="warn", encoding="utf-8-sig")
    df.columns = [c.strip().rstrip(";") for c in df.columns]
    df["ID_evidencia"] = df["ID_evidencia"].astype(str).str.strip()
    df["Codigo"] = df["Codigo"].astype(str).str.strip()
    # Una fila puede citar mas de un ID_evidencia separado por ';' (no
    # ocurre hoy en el archivo, pero se soporta por si acaso).
    filas = []
    for _, fila in df.iterrows():
        for ev in re.split(r"[;,]", fila["ID_evidencia"]):
            ev = ev.strip()
            if ev:
                filas.append({"ID_evidencia": ev, "Codigo": fila["Codigo"]})
    return pd.DataFrame(filas)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--entrada", required=True, help="codificacion_tematica.csv")
    ap.add_argument("--salida", required=True, help="PNG de salida de la curva")
    ap.add_argument("--tabla", required=True, help="CSV de salida con el detalle por entrevista")
    ap.add_argument("--fechas", default=FECHAS_JSON_DEFAULT,
                    help="JSON con la fecha de cada id_evidencia (transcripciones_anonimizadas.json)")
    args = ap.parse_args()

    fechas = cargar_fechas(args.fechas)
    df = cargar_codificacion(args.entrada)

    evs_sin_fecha = sorted(set(df["ID_evidencia"]) - set(fechas))
    if evs_sin_fecha:
        print(f"AVISO: sin fecha registrada para {evs_sin_fecha}; se excluyen del orden cronologico.")
        df = df[~df["ID_evidencia"].isin(evs_sin_fecha)]

    df["fecha"] = df["ID_evidencia"].map(fechas)
    # Orden cronologico, desempatando por identificador de evidencia. El
    # desempate no es cosmetico: las seis entrevistas de la ronda terminal
    # comparten fecha, y `sort_values` usa quicksort, que no es estable. Sin
    # segunda clave el orden de esas seis --y con el, cuantos codigos nuevos
    # se le atribuyen a cada una-- podria variar entre ejecuciones. Los
    # identificadores se asignaron en el orden en que se condujeron.
    orden_evs = (
        df[["ID_evidencia", "fecha"]]
        .drop_duplicates()
        .sort_values(["fecha", "ID_evidencia"], kind="mergesort")
        .reset_index(drop=True)
    )

    vistos = set()
    filas_tabla = []
    for i, row in orden_evs.iterrows():
        ev = row["ID_evidencia"]
        codigos_ev = set(df.loc[df["ID_evidencia"] == ev, "Codigo"])
        nuevos = codigos_ev - vistos
        vistos |= codigos_ev
        filas_tabla.append({
            "orden": i + 1,
            "id_evidencia": ev,
            "fecha": row["fecha"],
            "codigos_en_entrevista": len(codigos_ev),
            "codigos_nuevos": len(nuevos),
            "codigos_acumulados": len(vistos),
        })

    tabla = pd.DataFrame(filas_tabla)
    total_final = tabla["codigos_acumulados"].iloc[-1] if len(tabla) else 0

    # Criterio de saturacion: promedio de codigos nuevos en las ultimas 3
    # entrevistas <= 5% del total acumulado final.
    ultimas3 = tabla.tail(3)
    promedio_ultimas3 = ultimas3["codigos_nuevos"].mean() if len(ultimas3) else float("nan")
    umbral_5pct = 0.05 * total_final if total_final else float("nan")
    saturado = bool(promedio_ultimas3 <= umbral_5pct) if total_final else False

    # Las tres columnas se calculan **entrevista por entrevista**, no como el
    # valor final repetido en todas las filas. Un veredicto global copiado en la
    # primera fila diria que el corpus estaba saturado con una sola entrevista,
    # que es imposible; asi la tabla muestra cuando se alcanza y la ultima fila
    # coincide con el veredicto global que se imprime abajo.
    tabla["promedio_nuevos_ultimas_3"] = (
        tabla["codigos_nuevos"].rolling(3, min_periods=3).mean().round(3))
    tabla["umbral_5pct_hasta_aqui"] = (0.05 * tabla["codigos_acumulados"]).round(3)
    tabla["saturado_hasta_aqui"] = [
        "" if pd.isna(m) else str(bool(m <= u))
        for m, u in zip(tabla["promedio_nuevos_ultimas_3"],
                        tabla["umbral_5pct_hasta_aqui"])]

    os.makedirs(os.path.dirname(args.tabla), exist_ok=True)
    tabla.to_csv(args.tabla, index=False, encoding="utf-8")

    os.makedirs(os.path.dirname(args.salida), exist_ok=True)
    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.plot(tabla["orden"], tabla["codigos_acumulados"], marker="o", color="#2c6e49", label="Códigos acumulados")
    ax2 = ax.twinx()
    ax2.bar(tabla["orden"], tabla["codigos_nuevos"], alpha=0.25, color="#4c956c", label="Códigos nuevos por entrevista")
    ax.set_xlabel("Entrevista (orden cronológico)")
    ax.set_ylabel("Códigos acumulados")
    ax2.set_ylabel("Códigos nuevos en esta entrevista")
    ax.set_xticks(tabla["orden"])
    ax.set_xticklabels(tabla["id_evidencia"], rotation=45, ha="right")
    titulo_estado = "saturación alcanzada" if saturado else "sin inflexión clara todavía"
    ax.set_title(f"Curva de saturación temática — SIGA ({titulo_estado})")
    fig.tight_layout()
    fig.savefig(args.salida, dpi=200)

    print(f"Entrevistas analizadas: {len(tabla)}")
    print(f"Total de códigos distintos: {total_final}")
    print(f"Promedio de códigos nuevos en las últimas 3 entrevistas: {promedio_ultimas3:.3f}")
    print(f"Umbral (5% del total acumulado): {umbral_5pct:.3f}")
    print(f"¿Saturado según el criterio de la guía?: {saturado}")
    print(f"Tabla escrita en: {args.tabla}")
    print(f"Figura escrita en: {args.salida}")


if __name__ == "__main__":
    main()
