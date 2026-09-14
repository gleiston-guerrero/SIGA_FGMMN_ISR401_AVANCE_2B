# -*- coding: utf-8 -*-
"""Etapa 5 - La cadena de analisis, completa y dentro del paquete.

Las etapas 1 a 4 reconstruyen la hoja en formato largo, el acuerdo con su
intervalo y los conjuntos en texto plano. Esta etapa ejecuta el analisis
estadistico del que salen TODAS las tablas y figuras del reporte y del
manuscrito, y lo hace aqui dentro:

    lee de      07_Datos/datos_crudos/
    ejecuta     07_Datos/scripts/analisis/*.py
    escribe en  07_Datos/datos_procesados/puntuaciones_consolidadas.csv
                07_Datos/resultados/estadisticos/   6 resultados
                07_Datos/resultados/tablas/         7 tablas
                07_Datos/resultados/figuras/        4 figuras

No llama a nada de 06_Experimento ni de 07_Publicacion. El reporte (reporte.tex)
y el manuscrito (07_Publicacion/manuscrito_final.tex) incluyen las tablas y
figuras directamente desde 07_Datos/resultados/, de modo que lo que produce
esta etapa es, literalmente, lo que aparece en los documentos.

Antes de escribir vacia resultados/estadisticos/, resultados/tablas/ y
resultados/figuras/, para que lo que quede en ellas sea siempre lo que acaba de
producir esta ejecucion. Despues compara cada salida, byte a byte, con la suma
que consta en el manifiesto de la raiz, checksums.sha256: si una sola difiere,
lo dice y termina con codigo 1.

Los scripts de analisis/ son copia identica de los de
06_Experimento/scripts_analisis/, que siguen ejecutandose con
06_Experimento/replicar.py y con su Makefile. La etapa integridad comprueba que
ambas copias sean identicas byte a byte y que las dos cadenas den las mismas
salidas.

Dependencias. A diferencia de las etapas 1 a 4, esta necesita las seis
bibliotecas del analisis estadistico, con version fijada en
06_Experimento/requirements.txt:

    pip install -r 06_Experimento/requirements.txt

Si falta alguna, la etapa lo dice y termina con codigo 3, sin ejecutar nada.
"""
import hashlib
import importlib.util
import os
import shutil
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
PAQUETE = os.path.dirname(AQUI)
RAIZ = os.path.dirname(PAQUETE)

ANALISIS = os.path.join(AQUI, "analisis")
CRUDOS = os.path.join(PAQUETE, "datos_crudos")
PROC = os.path.join(PAQUETE, "datos_procesados")
EST = os.path.join(PAQUETE, "resultados", "estadisticos")
TAB = os.path.join(PAQUETE, "resultados", "tablas")
FIG = os.path.join(PAQUETE, "resultados", "figuras")

MANIFIESTO = os.path.join(RAIZ, "checksums.sha256")
REQUISITOS = os.path.join(RAIZ, "06_Experimento", "requirements.txt")

MODULOS = {"matplotlib": "matplotlib", "numpy": "numpy", "pandas": "pandas",
           "scikit-learn": "sklearn", "scipy": "scipy", "statsmodels": "statsmodels"}

# Lo que esta etapa produce y el manifiesto de la raiz registra.
PREFIJOS = ("07_Datos/resultados/estadisticos/", "07_Datos/resultados/tablas/",
            "07_Datos/resultados/figuras/")
PROCESADO = "07_Datos/datos_procesados/puntuaciones_consolidadas.csv"


def script(nombre):
    return os.path.join(ANALISIS, nombre)


def etapas():
    # El n del calculo de potencia es el numero de hojas de juez que hay en los
    # datos crudos. Se cuenta, no se escribe.
    n_jueces = len([f for f in os.listdir(CRUDOS)
                    if f.startswith("juez") and f.endswith(".csv")])
    analizar = script("analizar_resultados.py")
    clave = os.path.join(CRUDOS, "asignacion_brazo_items.csv")
    return [
        ("consolidar", [analizar, "--etapa", "consolidar", "--entrada", CRUDOS,
                        "--salida", PROC, "--clave", clave]),
        ("acuerdo", [analizar, "--etapa", "acuerdo", "--entrada", PROC, "--salida", EST]),
        ("supuestos", [analizar, "--etapa", "supuestos", "--entrada", PROC, "--salida", EST]),
        ("hipotesis", [analizar, "--etapa", "hipotesis", "--entrada", PROC, "--salida", EST,
                       "--correccion", "holm"]),
        ("efectos", [analizar, "--etapa", "efectos", "--entrada", PROC, "--salida", EST,
                     "--bootstrap", "10000", "--semilla", "20260802"]),
        ("saturacion", [script("curva_saturacion.py"),
                        "--entrada", os.path.join(CRUDOS, "codificacion_tematica.csv"),
                        "--fechas", os.path.join(CRUDOS, "transcripciones_anonimizadas.json"),
                        "--salida", os.path.join(FIG, "curva_saturacion.png"),
                        "--tabla", os.path.join(TAB, "saturacion_por_entrevista.csv")]),
        ("por_item", [script("analisis_por_item.py"), "--entrada", PROC, "--salida", EST,
                      "--tabla", TAB]),
        ("potencia", [script("power_calculation.py"), "--n-actual", str(n_jueces),
                      "--salida-csv", os.path.join(EST, "power_calculation.csv"),
                      "--salida-tex", os.path.join(TAB, "tabla_power_calculation.tex")]),
        ("figuras", [script("generar_figuras.py"), "--entrada", EST, "--salida", FIG,
                     "--procesados", PROC]),
        ("tablas", [script("generar_tablas.py"), "--entrada", EST, "--salida", TAB,
                    "--procesados", PROC]),
    ]


def sha256(ruta):
    h = hashlib.sha256()
    with open(ruta, "rb") as f:
        for bloque in iter(lambda: f.read(65536), b""):
            h.update(bloque)
    return h.hexdigest()


def esperadas():
    salida = {}
    with open(MANIFIESTO, encoding="utf-8") as f:
        for linea in f:
            linea = linea.rstrip("\r\n")
            if not linea.strip():
                continue
            suma, ruta = linea.split(" ", 1)
            ruta = ruta.lstrip("*").lstrip()
            if ruta.startswith("./"):
                ruta = ruta[2:]
            if ruta.startswith(PREFIJOS) or ruta == PROCESADO:
                salida[ruta] = suma
    return salida


def generadas():
    salida = [PROCESADO]
    for carpeta in (EST, TAB, FIG):
        for nombre in sorted(os.listdir(carpeta)):
            ruta = os.path.join(carpeta, nombre)
            if os.path.isfile(ruta):
                salida.append(os.path.relpath(ruta, RAIZ).replace("\\", "/"))
    return salida


def main():
    faltan = [p for p, m in MODULOS.items() if importlib.util.find_spec(m) is None]
    if faltan:
        print("  Faltan dependencias del analisis: %s" % ", ".join(faltan))
        print("  Instalelas con:  pip install -r %s" % os.path.relpath(REQUISITOS, os.getcwd()))
        return 3

    objetivo = esperadas()
    if not objetivo:
        print("  El manifiesto no registra ninguna salida del analisis")
        return 1

    for carpeta in (EST, TAB, FIG):
        if os.path.isdir(carpeta):
            shutil.rmtree(carpeta)
        os.makedirs(carpeta)
    os.makedirs(PROC, exist_ok=True)

    for nombre, orden in etapas():
        r = subprocess.run([sys.executable] + orden, cwd=RAIZ,
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        if r.returncode != 0:
            print(r.stdout[-3000:])
            print("  La etapa de analisis '%s' termino con codigo %d" % (nombre, r.returncode))
            return r.returncode

    producidas = generadas()
    ausentes = sorted(set(objetivo) - set(producidas))
    sobrantes = sorted(set(producidas) - set(objetivo))
    distintas = sorted(x for x in producidas
                       if x in objetivo and sha256(os.path.join(RAIZ, x)) != objetivo[x])
    for ruta in ausentes:
        print("    NO SE GENERO  %s" % ruta)
    for ruta in sobrantes:
        print("    NO CONSTA EN EL MANIFIESTO  %s" % ruta)
    for ruta in distintas:
        print("    DIFIERE       %s" % ruta)
    if ausentes or sobrantes or distintas:
        print("  %d salida(s) no coinciden con el manifiesto"
              % (len(ausentes) + len(sobrantes) + len(distintas)))
        return 1

    print("  Cadena de analisis ejecutada desde 07_Datos/scripts/analisis/")
    print("  %d salidas identicas byte a byte al manifiesto:" % len(producidas))
    for etiqueta, prefijo in (("resultados/tablas/", PREFIJOS[1]),
                              ("resultados/figuras/", PREFIJOS[2]),
                              ("resultados/estadisticos/", PREFIJOS[0])):
        print("    07_Datos/%-26s %d" % (etiqueta, sum(1 for x in producidas if x.startswith(prefijo))))
    print("    07_Datos/%-26s %d" % ("datos_procesados/", 1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
