# -*- coding: utf-8 -*-
"""
SIGA - Pipeline de analisis reproducible del componente empirico.

Equivalente exacto de `make all`, para entornos sin make.

    python 06_Experimento/replicar.py

Ejecuta las nueve etapas en el mismo orden y con los mismos parametros que el
Makefile, de modo que ambas rutas producen byte a byte las mismas tablas y
figuras. La semilla del bootstrap esta fijada en 20260802.

Opciones:
    --etapas consolidar acuerdo ...   ejecuta solo las etapas indicadas
    --listar                          muestra las etapas y termina
    --verificar                       sondea codec y duracion del material y
                                      comprueba el manifiesto de sumas
"""
import argparse
import os
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)

SCRIPTS = os.path.join(RAIZ, "06_Experimento", "scripts_analisis")
CRUDOS = os.path.join(RAIZ, "06_Experimento", "datos_crudos")
PROC = os.path.join(RAIZ, "06_Experimento", "datos_procesados")
FIGS = os.path.join(RAIZ, "07_Publicacion", "figuras")
TABS = os.path.join(RAIZ, "07_Publicacion", "tablas")
RES = os.path.join(AQUI, "resultados")

ANALIZAR = os.path.join(SCRIPTS, "analizar_resultados.py")

# El n del calculo de potencia es el numero de jueces cuyas hojas estan en los
# datos crudos. Se cuenta, no se escribe: si se anade o se retira una hoja, la
# potencia se recalcula sola.
N_JUECES = len([f for f in os.listdir(CRUDOS)
                if f.startswith("juez") and f.endswith(".csv")])

ETAPAS = [
    ("consolidar", [ANALIZAR, "--etapa", "consolidar", "--entrada", CRUDOS, "--salida", PROC]),
    ("acuerdo", [ANALIZAR, "--etapa", "acuerdo", "--entrada", PROC, "--salida", RES]),
    ("supuestos", [ANALIZAR, "--etapa", "supuestos", "--entrada", PROC, "--salida", RES]),
    ("hipotesis", [ANALIZAR, "--etapa", "hipotesis", "--entrada", PROC, "--salida", RES,
                   "--correccion", "holm"]),
    ("efectos", [ANALIZAR, "--etapa", "efectos", "--entrada", PROC, "--salida", RES,
                 "--bootstrap", "10000", "--semilla", "20260802"]),
    ("saturacion", [os.path.join(SCRIPTS, "curva_saturacion.py"),
                    "--entrada", os.path.join(RAIZ, "02_Evidencias", "Codificacion_Tematica",
                                              "codificacion_tematica.csv"),
                    "--salida", os.path.join(FIGS, "curva_saturacion.png"),
                    "--tabla", os.path.join(TABS, "saturacion_por_entrevista.csv")]),
    ("por_item", [os.path.join(SCRIPTS, "analisis_por_item.py"),
                  "--entrada", PROC, "--salida", RES, "--tabla", TABS]),
    ("potencia", [os.path.join(SCRIPTS, "power_calculation.py"),
                  "--n-actual", str(N_JUECES),
                  "--salida-csv", os.path.join(RES, "power_calculation.csv"),
                  "--salida-tex", os.path.join(TABS, "tabla_power_calculation.tex")]),
    ("figuras", [os.path.join(SCRIPTS, "generar_figuras.py"),
                 "--entrada", RES, "--salida", FIGS, "--procesados", PROC]),
    ("tablas", [os.path.join(SCRIPTS, "generar_tablas.py"),
                "--entrada", RES, "--salida", TABS, "--procesados", PROC,
                "--acuerdo-ic", os.path.join(RAIZ, "07_Datos", "resultados",
                                             "acuerdo_interevaluador_ic.csv")]),
]


def entorno():
    """Crea los directorios de salida y deja constancia del entorno de Python."""
    for d in (PROC, RES, FIGS, TABS):
        os.makedirs(d, exist_ok=True)
    print("Python: " + sys.version.split()[0])
    congelado = subprocess.run([sys.executable, "-m", "pip", "freeze"],
                               capture_output=True, text=True)
    destino = os.path.join(RES, "entorno_python.txt")
    with open(destino, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(congelado.stdout)
    print("Entorno registrado en " + os.path.relpath(destino, RAIZ))


def correr(nombre, orden):
    print("")
    print("== etapa: " + nombre + " " + "=" * (58 - len(nombre)))
    r = subprocess.run([sys.executable] + orden, cwd=RAIZ)
    if r.returncode != 0:
        print("La etapa '" + nombre + "' termino con codigo " + str(r.returncode) + ".")
        sys.exit(r.returncode)


def verificar():
    """Sondeo de codec y duracion, y comprobacion del manifiesto de sumas."""
    import glob
    import hashlib

    import shutil

    print("== Sondeo de codec y duracion del material de entrevista ==")
    if shutil.which("ffprobe") is None:
        print("  ffprobe no esta en el PATH: el sondeo no se ejecuta.")
        print("  Instale FFmpeg y repita, o use `make verificar`.")
        return 2
    patrones = [os.path.join(RAIZ, "02_Evidencias", "Video", "*.mp4"),
                os.path.join(RAIZ, "02_Evidencias", "Audio", "*.mp3"),
                os.path.join(RAIZ, "02_Evidencias", "Audio", "*.wav")]
    medios = sorted(f for p in patrones for f in glob.glob(p))
    invalidos = 0
    for f in medios:
        r = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                            "format=duration,format_name", "-of", "csv=p=0", f],
                           capture_output=True, text=True)
        if r.returncode != 0 or not r.stdout.strip():
            print("  ARCHIVO INVALIDO  " + os.path.relpath(f, RAIZ))
            invalidos += 1
        else:
            print("  %-62s %s" % (os.path.relpath(f, RAIZ), r.stdout.strip()))
    print("  %d archivos sondeados, %d invalidos" % (len(medios), invalidos))

    print("")
    print("== Verificacion del manifiesto de sumas ==")
    manifiesto = os.path.join(RAIZ, "checksums.sha256")
    fallos = ausentes = comprobados = 0
    with open(manifiesto, encoding="utf-8") as fh:
        for linea in fh:
            linea = linea.rstrip("\n")
            if not linea.strip():
                continue
            suma, ruta = linea.split("  ", 1)
            destino = os.path.join(RAIZ, ruta)
            if not os.path.exists(destino):
                print("  AUSENTE   " + ruta)
                ausentes += 1
                continue
            h = hashlib.sha256()
            with open(destino, "rb") as bin_:
                for bloque in iter(lambda: bin_.read(1 << 20), b""):
                    h.update(bloque)
            comprobados += 1
            if h.hexdigest() != suma:
                print("  NO CUADRA " + ruta)
                fallos += 1
    print("  %d comprobados, %d no cuadran, %d ausentes" % (comprobados, fallos, ausentes))
    return 1 if (fallos or ausentes or invalidos) else 0


def main():
    ap = argparse.ArgumentParser(description="Pipeline reproducible de SIGA sin make.")
    ap.add_argument("--etapas", nargs="*", default=None,
                    help="Subconjunto de etapas a ejecutar, en el orden dado.")
    ap.add_argument("--listar", action="store_true", help="Lista las etapas y termina.")
    ap.add_argument("--verificar", action="store_true",
                    help="Sondea el material audiovisual y comprueba el manifiesto.")
    a = ap.parse_args()

    if a.listar:
        for n, _ in ETAPAS:
            print(n)
        return 0

    if a.verificar:
        return verificar()

    entorno()
    pedidas = a.etapas
    for nombre, orden in ETAPAS:
        if pedidas and nombre not in pedidas:
            continue
        correr(nombre, orden)

    print("")
    print("== Pipeline completo ==")
    print("Tablas en  " + os.path.relpath(TABS, RAIZ))
    print("Figuras en " + os.path.relpath(FIGS, RAIZ))
    return 0


if __name__ == "__main__":
    sys.exit(main())
