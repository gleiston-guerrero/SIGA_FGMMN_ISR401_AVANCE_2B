# -*- coding: utf-8 -*-
"""
Cálculo de potencia estadística — vía alternativa al criterio C6 para el
Enfoque 1, cuando la curva de saturación temática no muestra inflexión
(ver 06_Experimento/README_OSF.md, desviación sobre el codebook sin
consolidar).

Calcula el tamaño muestral necesario (numero de pares apareados, p. ej.
jueces o respuestas de cuestionario) para detectar un tamaño de efecto de
Cohen d=0.5 con alpha=0.05 y potencia 1-beta=0.80 en una prueba t
apareada, y de paso reporta la potencia real ya alcanzada con el n actual
del componente empirico (n=3 jueces).

Requiere: statsmodels (pip install statsmodels)

Uso:
    python power_calculation.py
    python power_calculation.py --effect-size 0.5 --alpha 0.05 --power 0.80 --n-actual 3
"""
import argparse
import os

import pandas as pd
from statsmodels.stats.power import TTestPower


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--effect-size", type=float, default=0.5, help="Cohen d objetivo (default 0.5, convencion de la guia)")
    ap.add_argument("--alpha", type=float, default=0.05)
    ap.add_argument("--power", type=float, default=0.80)
    ap.add_argument("--n-actual", type=int, default=3, help="n real del diseño apareado (default 3 jueces)")
    ap.add_argument("--salida-csv", default="resultados/power_calculation.csv",
                     help="CSV con los resultados (default resultados/power_calculation.csv)")
    ap.add_argument("--salida-tex", default="../tablas/tabla_power_calculation.tex",
                     help="Tabla LaTeX lista para \\input (default ../tablas/tabla_power_calculation.tex)")
    args = ap.parse_args()

    analisis = TTestPower()

    n_necesario = analisis.solve_power(
        effect_size=args.effect_size, alpha=args.alpha, power=args.power, alternative="two-sided"
    )
    potencia_actual = analisis.solve_power(
        effect_size=args.effect_size, alpha=args.alpha, nobs=args.n_actual, alternative="two-sided"
    )

    print("=== Cálculo de potencia estadística (prueba t apareada) ===")
    print(f"Tamaño del efecto objetivo (Cohen d): {args.effect_size}")
    print(f"Nivel de significancia (alpha):        {args.alpha}")
    print(f"Potencia deseada (1-beta):             {args.power}")
    print(f"N necesario para alcanzar esa potencia: {n_necesario:.2f}  (redondear hacia arriba: {int(n_necesario) + 1})")
    print()
    print(f"N real del componente empírico:        {args.n_actual}")
    print(f"Potencia realmente alcanzada con N={args.n_actual}:  {potencia_actual:.4f}")
    print()
    print("Interpretación para el manuscrito (Amenazas a la validez — conclusion validity):")
    print(f"  Con N={args.n_actual}, el estudio solo alcanza una potencia de {potencia_actual:.1%} para detectar")
    print(f"  un efecto mediano (d=0.5) con alpha=0.05, muy por debajo del 80% convencional.")
    print(f"  Se necesitarían aproximadamente {int(n_necesario) + 1} pares para alcanzar la potencia deseada.")
    print("  Esta limitación se declara explícitamente en lugar de reportar saturación no alcanzada.")

    resultado = pd.DataFrame([{
        "Cohen_d_objetivo": args.effect_size,
        "alpha": args.alpha,
        "potencia_deseada": args.power,
        "n_necesario": round(n_necesario, 2),
        "n_necesario_redondeado": int(n_necesario) + 1,
        "n_actual": args.n_actual,
        "potencia_alcanzada_con_n_actual": round(potencia_actual, 4),
    }])

    os.makedirs(os.path.dirname(args.salida_csv) or ".", exist_ok=True)
    resultado.to_csv(args.salida_csv, index=False, encoding="utf-8")
    print(f"\nResultado escrito en: {args.salida_csv}")

    # Rotulos de la tabla impresa. El manuscrito esta en ingles, de modo que
    # las cabeceras tambien. Los nombres de columna del CSV no se tocan: son
    # los que leen los demas scripts.
    columnas_en = {
        "Cohen_d_objetivo": r"Target $d$", "alpha": r"$\alpha$",
        "potencia_deseada": "Target power",
        "n_necesario": r"$n$ needed", "n_necesario_redondeado": r"$n$ needed (int.)",
        "n_actual": r"$n$ actual",
        "potencia_alcanzada_con_n_actual": "Power achieved",
    }
    tabla = resultado.rename(columns=columnas_en)
    alineacion = "l" * len(tabla.columns)
    # Se formatea columna por columna segun el dtype ORIGINAL del DataFrame:
    # tabla.iloc[0] convertiria toda la fila a float si se mezclan int y
    # float (una Series solo admite un dtype), mostrando "34.0000" en vez
    # de "34" para las columnas enteras.
    valores_formateados = []
    for col in resultado.columns:
        v = resultado[col].iloc[0]
        if pd.api.types.is_integer_dtype(resultado[col]):
            valores_formateados.append(str(int(v)))
        elif pd.api.types.is_float_dtype(resultado[col]):
            valores_formateados.append(f"{v:.4f}")
        else:
            valores_formateados.append(str(v))

    lineas = [
        r"\begin{table}[htbp]", r"\centering", r"\footnotesize",
        r"\caption{Statistical power calculation for the paired t-test}",
        r"\label{tab:power_calculation}",
        f"\\begin{{tabular}}{{{alineacion}}}", r"\toprule",
        " & ".join(tabla.columns) + r" \\", r"\midrule",
        " & ".join(valores_formateados) + r" \\",
        r"\bottomrule", r"\end{tabular}", r"\end{table}", "",
    ]

    os.makedirs(os.path.dirname(args.salida_tex) or ".", exist_ok=True)
    with open(args.salida_tex, "w", encoding="utf-8") as f:
        f.write("\n".join(lineas))
    print(f"Tabla LaTeX escrita en: {args.salida_tex}")


if __name__ == "__main__":
    main()
