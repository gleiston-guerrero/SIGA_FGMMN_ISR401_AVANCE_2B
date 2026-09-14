# -*- coding: utf-8 -*-
"""Orquestador unico del paquete de datos SIGA.

Una sola orden, desde la raiz del repositorio clonado:

    python 07_Datos/scripts/ejecutar.py

Reconstruye todo el contenido de datos_procesados/ y resultados/ a partir
exclusivamente de datos_crudos/, regenera las tablas y figuras del documento
ejecutando aqui dentro la cadena de analisis estadistico, y termina
comprobando la integridad del paquete. No pide argumentos ni pregunta nada.

Las etapas formato_largo, acuerdo_ic, conjuntos e integridad usan solo la
biblioteca estandar de Python 3.8 o superior. La etapa analisis necesita las
dependencias fijadas en 06_Experimento/requirements.txt, y si faltan lo dice
antes de ejecutar nada.

Etapas:

    1. formato_largo  Hoja de evaluacion a ciegas en formato largo, con el
                      orden de presentacion.
    2. acuerdo_ic     Kappa de Cohen ponderado y de Fleiss, cada uno con su
                      intervalo de confianza del 95 % por bootstrap.
    3. conjuntos      Los dos conjuntos de requisitos comparados, cada uno en
                      su archivo de texto plano.
    4. analisis       Ejecuta la cadena de analisis de scripts/analisis/ sobre
                      datos_crudos/ y escribe en resultados/estadisticos/,
                      resultados/tablas/ y resultados/figuras/ las tablas y
                      figuras que el reporte y el manuscrito incluyen desde
                      aqui. Comprueba que salen identicas byte a byte a las
                      del manifiesto.
    5. integridad     Correspondencia con 06_Experimento (datos, scripts y
                      salidas), cobertura del diccionario de datos y
                      manifiesto de sumas.

Opciones:
    --listar    muestra las etapas y termina
    --etapas    ejecuta solo las indicadas, por nombre
"""
import argparse
import os
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))

ETAPAS = [
    ("formato_largo", "etapa1_formato_largo.py",
     "Hoja de evaluacion a ciegas en formato largo"),
    ("acuerdo_ic", "etapa2_acuerdo_ic.py",
     "Acuerdo entre evaluadores con intervalo de confianza"),
    ("conjuntos", "etapa4_conjuntos_texto.py",
     "Conjuntos A y B de requisitos en texto plano"),
    ("analisis", "etapa5_analisis.py",
     "Cadena de analisis: tablas y figuras del documento"),
    ("integridad", "etapa3_integridad.py",
     "Correspondencia, diccionario y manifiesto de sumas"),
]


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--listar", action="store_true")
    ap.add_argument("--etapas", nargs="+", metavar="NOMBRE")
    args = ap.parse_args()

    if args.listar:
        for nombre, _, desc in ETAPAS:
            print("  %-16s %s" % (nombre, desc))
        return 0

    pendientes = ETAPAS
    if args.etapas:
        conocidas = {e[0] for e in ETAPAS}
        malas = [e for e in args.etapas if e not in conocidas]
        if malas:
            print("Etapa desconocida: %s" % ", ".join(malas))
            print("Disponibles: %s" % ", ".join(e[0] for e in ETAPAS))
            return 2
        pendientes = [e for e in ETAPAS if e[0] in args.etapas]

    print("Paquete de datos SIGA - reconstruccion desde datos crudos")
    print("Python %s" % sys.version.split()[0])
    print("")

    for i, (nombre, script, desc) in enumerate(pendientes, 1):
        print("[%d/%d] %s" % (i, len(pendientes), desc))
        r = subprocess.run([sys.executable, os.path.join(AQUI, script)])
        if r.returncode != 0:
            print("\nLa etapa '%s' fallo. Se detiene aqui." % nombre)
            return r.returncode
        print("")

    print("Listo. Todo lo de datos_procesados/ y resultados/ procede de")
    print("datos_crudos/ y de los scripts de esta carpeta, incluidas las")
    print("tablas y figuras que el reporte y el manuscrito toman de aqui.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
