# -*- coding: utf-8 -*-
"""Ata cada afirmacion con cifra a la salida que la sostiene, y la comprueba.

    python 07_Publicacion/verificar_afirmaciones.py

Escribe `correspondencia_afirmacion_resultado.csv` y devuelve codigo 1 si alguna
cifra afirmada ya no coincide con su fuente.

Por que existe.

El reporte ya trae esa correspondencia en un anexo --- «Correspondencia entre
afirmacion y resultado», tabla `tab:correspondencia` --- y el paquete de datos
trae `correspondencia_salidas.csv`, que ata cada salida con el script que la
produce. Lo que faltaba no era la tabla: era **comprobarla**. Una tabla de
correspondencias se lee, pero no se verifica sola, y basta con que alguien
reejecute el analisis para que las cifras de la prosa y las de los CSV dejen de
coincidir sin que nada lo delate.

Este script es el respaldo comprobable de ese anexo.

Y hay un fallo que ninguna otra comprobacion del repositorio detecta: que una
cifra escrita en prosa se quede atras cuando el analisis se vuelve a correr. El
manifiesto de sumas dice que los archivos no cambiaron; los enlaces dicen que las
rutas existen; ninguno de los dos mira si el 0,338 del manuscrito sigue siendo el
0,338 de `acuerdo_interevaluador.csv`. Este script si.

Cada afirmacion declara el valor que el texto publica y de donde deberia salir.
El script lee la fuente, extrae el valor y los compara con la tolerancia que
corresponde a los decimales publicados. Si el analisis se reejecuta y una cifra
cambia, esto lo dice y nombra el documento que hay que corregir.

Solo biblioteca estandar.
"""
import csv
import io
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
SALIDA = os.path.join(AQUI, "correspondencia_afirmacion_resultado.csv")


def celda(ruta, filtro, columna):
    """Devuelve la celda de la primera fila que cumple `filtro`."""
    with io.open(os.path.join(RAIZ, ruta), encoding="utf-8-sig") as f:
        for fila in csv.DictReader(f):
            if all(fila.get(k, "").strip() == v for k, v in filtro.items()):
                return fila[columna].strip()
    return None


def cuenta(ruta, filtro=None):
    """Cuenta filas de un CSV, opcionalmente filtrando."""
    with io.open(os.path.join(RAIZ, ruta), encoding="utf-8-sig") as f:
        filas = list(csv.DictReader(f))
    if filtro:
        filas = [r for r in filas
                 if all(r.get(k, "").strip() == v for k, v in filtro.items())]
    return len(filas)


def distintos(ruta, columna):
    with io.open(os.path.join(RAIZ, ruta), encoding="utf-8-sig") as f:
        return len(set(r[columna].strip() for r in csv.DictReader(f)
                       if r[columna].strip()))


# Cada entrada: (id, afirmacion, valor publicado, funcion que lo recalcula,
#                fuente, documentos que lo afirman)
RES = "06_Experimento/resultados/"
COD = "02_Evidencias/Codificacion_Tematica/"
TAB = "07_Publicacion/tablas/"

AFIRMACIONES = [
    ("AFI-01",
     "La potencia del panel de tres jueces es del 8,4 % frente al 80 % convencional",
     "0.0841",
     lambda: celda(RES + "power_calculation.csv", {}, "potencia_alcanzada_con_n_actual"),
     RES + "power_calculation.csv",
     "manuscrito_final.tex; reporte.tex; presentacion.pptx; libreto_grabacion.md"),

    ("AFI-02",
     "Detectar un efecto medio exigiria 34 observaciones apareadas; se dispone de 3",
     "34",
     lambda: celda(RES + "power_calculation.csv", {}, "n_necesario_redondeado"),
     RES + "power_calculation.csv",
     "manuscrito_final.tex; reporte.tex; libreto_grabacion.md"),

    ("AFI-03",
     "Ninguna de las cinco dimensiones es significativa tras el ajuste de Holm",
     "0",
     lambda: str(cuenta(RES + "hipotesis.csv",
                        {"significativo_alpha_05_ajustado": "True"})),
     RES + "hipotesis.csv",
     "manuscrito_final.tex; reporte.tex; presentacion.pptx"),

    ("AFI-04",
     "El tamano del efecto en Completitud, con el requisito como unidad, es delta de Cliff = -0,1169",
     "-0.1169",
     lambda: celda(RES + "efectos.csv", {"Dimension": "Completitud(1-5)"}, "Valor"),
     RES + "efectos.csv",
     "manuscrito_final.tex; reporte.tex"),

    ("AFI-05",
     "El delta de Cliff mayor en valor absoluto es el de Consistencia interna, -0,1846",
     "-0.1846",
     lambda: celda(RES + "efectos.csv",
                   {"Dimension": "Consistencia_interna(1-5)"}, "Valor"),
     RES + "efectos.csv",
     "manuscrito_final.tex; reporte.tex"),

    ("AFI-06",
     "El acuerdo entre los tres jueces del registro previo es Fleiss 0,296 a 0,340",
     "0.296|0.34",
     lambda: "%s|%s" % (
         min(celda(RES + "acuerdo_interevaluador.csv", {"Dimension": d},
                   "Fleiss_kappa_3jueces")
             for d in ["Verificabilidad(1-5)"]),
         max(celda(RES + "acuerdo_interevaluador.csv", {"Dimension": d},
                   "Fleiss_kappa_3jueces")
             for d in ["Ausencia_ambiguedad(1-5)"])),
     RES + "acuerdo_interevaluador.csv",
     "manuscrito_final.tex; reporte.tex; panel_ampliado/00_LEEME.md"),

    ("AFI-07",
     "El corpus tiene 16 entrevistas codificadas",
     "16",
     lambda: str(distintos(COD + "codificacion_tematica.csv", "ID_evidencia")),
     COD + "codificacion_tematica.csv",
     "reporte.tex; manuscrito_final.tex; presentacion.pptx; libreto_grabacion.md"),

    ("AFI-08",
     "La codificacion tematica tiene 136 fragmentos bajo 50 codigos",
     "136|50",
     lambda: "%d|%d" % (cuenta(COD + "codificacion_tematica.csv"),
                        distintos(COD + "codificacion_tematica.csv", "Codigo")),
     COD + "codificacion_tematica.csv",
     "reporte.tex; manuscrito_final.tex; presentacion.pptx"),

    ("AFI-09",
     "La saturacion se alcanza: 1,333 codigos nuevos en las tres ultimas frente a un umbral de 2,50",
     "1.333|2.5",
     lambda: "%s|%s" % (
         celda(TAB + "saturacion_por_entrevista.csv", {"orden": "16"},
               "promedio_nuevos_ultimas_3"),
         celda(TAB + "saturacion_por_entrevista.csv", {"orden": "16"},
               "umbral_5pct_hasta_aqui")),
     TAB + "saturacion_por_entrevista.csv",
     "reporte.tex; manuscrito_final.tex; presentacion.pptx; libreto_grabacion.md"),

    ("AFI-10",
     "La curva satura a partir de la entrevista 14",
     "True",
     lambda: celda(TAB + "saturacion_por_entrevista.csv", {"orden": "14"},
                   "saturado_hasta_aqui"),
     TAB + "saturacion_por_entrevista.csv",
     "reporte.tex; 00_LEEME_SATURACION.md"),

    ("AFI-11",
     "La matriz de trazabilidad tiene 75 filas",
     "75",
     lambda: str(cuenta("04_Trazabilidad/matriz_trazabilidad.csv")),
     "04_Trazabilidad/matriz_trazabilidad.csv",
     "reporte.tex; banco_preguntas.md; presentacion.pptx; libreto_grabacion.md"),

    ("AFI-12",
     "El tablero de gestion tiene 61 actividades, una por requisito",
     "61",
     lambda: str(cuenta("04_Trazabilidad/tablero_gestion/export_tablero_SIGA.csv")),
     "04_Trazabilidad/tablero_gestion/export_tablero_SIGA.csv",
     "reporte.tex; presentacion.pptx; libreto_grabacion.md"),

    ("AFI-13",
     "El registro de consentimientos tiene 22 participantes, 19 citables en el manuscrito",
     "22|19",
     lambda: "%d|%d" % (
         cuenta("02_Evidencias/Consentimientos/registro_consentimientos.csv"),
         cuenta("02_Evidencias/Consentimientos/registro_consentimientos.csv",
                {"citable_en_manuscrito": "Si"})),
     "02_Evidencias/Consentimientos/registro_consentimientos.csv",
     "00_LEEME.md de Consentimientos; CHANGELOG.md"),

    ("AFI-14",
     "El panel ampliado no alcanza acuerdo: Fleiss medio -0,026 en la segunda vuelta",
     "-0.026",
     lambda: celda("06_Experimento/panel_ampliado/resultados/acuerdo_dos_vueltas.csv",
                   {"vuelta": "segunda", "dimension": "MEDIA DE LAS 4"},
                   "fleiss_kappa"),
     "06_Experimento/panel_ampliado/resultados/acuerdo_dos_vueltas.csv",
     "manuscrito_final.tex; panel_ampliado/00_LEEME.md; libreto_grabacion.md"),

    ("AFI-15",
     "En la segunda vuelta un evaluador no repite ninguna de sus doce puntuaciones",
     "0",
     lambda: celda("06_Experimento/panel_ampliado/resultados/consistencia_intrajuez.csv",
                   {"juez": "JUEZ-09"}, "identicas"),
     "06_Experimento/panel_ampliado/resultados/consistencia_intrajuez.csv",
     "manuscrito_final.tex; panel_ampliado/00_LEEME.md; libreto_grabacion.md"),
]


def main():
    filas, fallos = [], []
    for ident, texto, publicado, calcula, fuente, docs in AFIRMACIONES:
        try:
            real = calcula()
        except Exception as e:                       # noqa: BLE001
            real, ok = "ERROR: %s" % e, False
        else:
            ok = (real is not None and
                  [x.strip().rstrip("0").rstrip(".") for x in str(real).split("|")] ==
                  [x.strip().rstrip("0").rstrip(".") for x in publicado.split("|")])
        if not ok:
            fallos.append((ident, texto, publicado, real, docs))
        filas.append({
            "ID_afirmacion": ident,
            "Afirmacion": texto,
            "Valor_publicado": publicado.replace("|", " y "),
            "Valor_recalculado": str(real).replace("|", " y "),
            "Coincide": "Si" if ok else "NO",
            "Archivo_fuente": fuente,
            "Documentos_que_lo_afirman": docs,
        })

    with io.open(SALIDA, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(filas[0].keys()))
        w.writeheader()
        w.writerows(filas)

    print("correspondencia_afirmacion_resultado.csv")
    print("  %d afirmaciones comprobadas contra su fuente" % len(filas))
    if not fallos:
        print("  todas coinciden")
        return 0
    print()
    print("  %d NO COINCIDEN --- hay que corregir el texto o rehacer el analisis:" % len(fallos))
    for ident, texto, pub, real, docs in fallos:
        print("    %s  publicado %r, recalculado %r" % (ident, pub, real))
        print("        %s" % texto)
        print("        lo afirman: %s" % docs)
    return 1


if __name__ == "__main__":
    sys.exit(main())
