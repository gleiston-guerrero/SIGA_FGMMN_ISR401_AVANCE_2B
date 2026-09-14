# -*- coding: utf-8 -*-
"""
Genera las figuras del manuscrito (excepto la curva de saturación, que
produce curva_saturacion.py) a partir de los resultados del pipeline.

Uso (ver Makefile, objetivo `figuras`):
    python generar_figuras.py --entrada ../resultados --salida ../../figuras \
        [--procesados ../datos_procesados]

Genera:
    fig02_distribucion_por_dimension.png  — caja y puntos, Humano vs LLM, por dimension
    fig03_tamanos_efecto.png              — tamano del efecto con IC 95% por dimension
    fig04_acuerdo_interevaluador.png      — kappa de Cohen por par y kappa de Fleiss
"""
import argparse
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

DIMENSIONES = [
    "Completitud(1-5)", "Ausencia_ambiguedad(1-5)", "Verificabilidad(1-5)",
    "Correccion_fuente(1-5)", "Consistencia_interna(1-5)",
]


def fig_distribucion(procesados_dir, salida_dir):
    ruta = os.path.join(procesados_dir, "puntuaciones_consolidadas.csv")
    if not os.path.exists(ruta):
        print(f"AVISO: no existe {ruta}; se omite fig02 (distribucion por dimension).")
        return
    df = pd.read_csv(ruta, encoding="utf-8-sig")

    fig, axes = plt.subplots(1, len(DIMENSIONES), figsize=(4 * len(DIMENSIONES), 4.5), sharey=True)
    if len(DIMENSIONES) == 1:
        axes = [axes]
    for ax, dim in zip(axes, DIMENSIONES):
        sub = df[df["dimension"] == dim]
        datos = [sub[sub["origen"] == "Humano"]["puntuacion"].values,
                 sub[sub["origen"] == "LLM"]["puntuacion"].values]
        bp = ax.boxplot(datos, showmeans=True, widths=0.5)
        ax.set_xticks([1, 2])
        ax.set_xticklabels(["Humano", "LLM"])
        for i, d in enumerate(datos, start=1):
            jitter = np.random.default_rng(0).normal(0, 0.04, size=len(d))
            ax.scatter(np.full(len(d), i) + jitter, d, alpha=0.35, s=14, color="#2c6e49")
        ax.set_title(dim.replace("(1-5)", ""), fontsize=9)
        ax.set_ylim(0.5, 5.5)

    fig.suptitle("Distribución de puntuaciones por dimensión y origen (Humano vs. LLM)")
    fig.tight_layout()
    ruta_salida = os.path.join(salida_dir, "fig02_distribucion_por_dimension.png")
    fig.savefig(ruta_salida, dpi=200)
    plt.close(fig)
    print(f"Escrita: {ruta_salida}")


def fig_efectos(resultados_dir, salida_dir):
    ruta = os.path.join(resultados_dir, "efectos.csv")
    if not os.path.exists(ruta):
        print(f"AVISO: no existe {ruta}; se omite fig03 (tamanos de efecto).")
        return
    df = pd.read_csv(ruta, encoding="utf-8-sig")

    fig, ax = plt.subplots(figsize=(7, 4.5))
    y = np.arange(len(df))
    valores = df["Valor"].values
    err_inf = valores - df["IC95_inferior"].values
    err_sup = df["IC95_superior"].values - valores
    ax.errorbar(valores, y, xerr=[err_inf, err_sup], fmt="o", color="#2c6e49", capsize=4)
    ax.axvline(0, color="gray", linestyle="--", linewidth=1)
    ax.set_yticks(y)
    ax.set_yticklabels([d.replace("(1-5)", "") for d in df["Dimension"]])
    ax.invert_yaxis()
    ax.set_xlabel("g de Hedges o δ de Cliff, requisito como unidad (IC 95% bootstrap)")
    ax.set_title("Tamaños de efecto: Humano (n=25) vs. LLM (n=26)")
    fig.tight_layout()
    ruta_salida = os.path.join(salida_dir, "fig03_tamanos_efecto.png")
    fig.savefig(ruta_salida, dpi=200)
    plt.close(fig)
    print(f"Escrita: {ruta_salida}")


def fig_acuerdo(resultados_dir, salida_dir):
    ruta = os.path.join(resultados_dir, "acuerdo_interevaluador.csv")
    if not os.path.exists(ruta):
        print(f"AVISO: no existe {ruta}; se omite fig04 (acuerdo inter-evaluador).")
        return
    df = pd.read_csv(ruta, encoding="utf-8-sig")
    columnas_kappa = [c for c in df.columns if c != "Dimension"]

    fig, ax = plt.subplots(figsize=(8, 4.5))
    x = np.arange(len(df))
    ancho = 0.8 / max(len(columnas_kappa), 1)
    for i, col in enumerate(columnas_kappa):
        ax.bar(x + i * ancho, df[col], width=ancho, label=col)
    ax.set_xticks(x + ancho * (len(columnas_kappa) - 1) / 2)
    ax.set_xticklabels([d.replace("(1-5)", "") for d in df["Dimension"]], rotation=20, ha="right")
    ax.axhline(0, color="black", linewidth=0.8)
    ax.set_ylabel("Kappa")
    ax.set_title("Acuerdo inter-evaluador por dimensión")
    ax.legend(fontsize=7)
    fig.tight_layout()
    ruta_salida = os.path.join(salida_dir, "fig04_acuerdo_interevaluador.png")
    fig.savefig(ruta_salida, dpi=200)
    plt.close(fig)
    print(f"Escrita: {ruta_salida}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--entrada", required=True, help="Carpeta resultados/ (salida del pipeline de analizar_resultados.py)")
    ap.add_argument("--salida", required=True, help="Carpeta figuras/ del reporte")
    ap.add_argument("--procesados", default=None,
                     help="Carpeta datos_procesados/ (por defecto, ../datos_procesados relativo a --entrada)")
    args = ap.parse_args()

    procesados = args.procesados or os.path.join(args.entrada, "..", "datos_procesados")
    os.makedirs(args.salida, exist_ok=True)

    fig_distribucion(procesados, args.salida)
    fig_efectos(args.entrada, args.salida)
    fig_acuerdo(args.entrada, args.salida)


if __name__ == "__main__":
    main()
