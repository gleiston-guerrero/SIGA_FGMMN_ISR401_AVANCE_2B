# -*- coding: utf-8 -*-
"""Etapa 5 - Las tablas y figuras del documento, regeneradas dentro del paquete.

Las etapas 1 a 4 reconstruyen el contenido de este paquete. Las tablas y las
figuras que aparecen en el manuscrito y en el reporte las produce la cadena de
analisis del componente empirico, 06_Experimento/replicar.py. Esta etapa la
ejecuta desde aqui, para que la misma orden unica

    python 07_Datos/scripts/ejecutar.py

deje regeneradas tambien las tablas y figuras del documento. Despues las
compara byte a byte con las sumas que constan en el manifiesto de la raiz,
checksums.sha256, y si todas coinciden las deposita DENTRO de este paquete:

    07_Publicacion/tablas/              ->  07_Datos/resultados/tablas/
    07_Publicacion/figuras/             ->  07_Datos/resultados/figuras/
    06_Experimento/resultados/          ->  07_Datos/resultados/estadisticos/
    06_Experimento/datos_procesados/    ->  07_Datos/datos_procesados/

Antes de depositarlas borra las copias anteriores de tablas/, figuras/ y
estadisticos/, de modo que lo que queda en esas carpetas es siempre lo que
acaba de producir esta ejecucion, nunca un resto de otra. Si una sola salida no
coincide con el manifiesto, la etapa falla, dice cual y no deposita nada.

Que se compara y se deposita: todo lo que el manifiesto registra bajo esas
cuatro carpetas de origen, salvo sus README, que no son salidas, y salvo
06_Experimento/resultados/entorno_python.txt, que es un volcado del entorno de
quien ejecuta y no un resultado.

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

REPLICAR = os.path.join(RAIZ, "06_Experimento", "replicar.py")
MANIFIESTO = os.path.join(RAIZ, "checksums.sha256")
REQUISITOS = os.path.join(RAIZ, "06_Experimento", "requirements.txt")

# Carpeta de origen en el repositorio -> carpeta de destino dentro del paquete.
DESTINOS = {
    "06_Experimento/datos_procesados/": "datos_procesados/",
    "06_Experimento/resultados/": "resultados/estadisticos/",
    "07_Publicacion/tablas/": "resultados/tablas/",
    "07_Publicacion/figuras/": "resultados/figuras/",
}
# Carpetas del paquete que contienen solo salidas de esta etapa y se vacian
# antes de depositar. datos_procesados/ no, porque tambien la escriben las
# etapas 1 y 4.
PROPIAS = ("resultados/estadisticos/", "resultados/tablas/", "resultados/figuras/")
CARPETAS = tuple(DESTINOS)
EXCLUIDOS = ("06_Experimento/resultados/entorno_python.txt",)

MODULOS = {"matplotlib": "matplotlib", "numpy": "numpy", "pandas": "pandas",
           "scikit-learn": "sklearn", "scipy": "scipy", "statsmodels": "statsmodels"}


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
            if (ruta.startswith(CARPETAS) and ruta not in EXCLUIDOS
                    and not os.path.basename(ruta).upper().startswith("README")):
                salida[ruta] = suma
    return salida


def destino(ruta):
    for origen, dest in DESTINOS.items():
        if ruta.startswith(origen):
            return dest + ruta[len(origen):]
    raise ValueError(ruta)


def depositar(objetivo):
    for carpeta in PROPIAS:
        absoluta = os.path.join(PAQUETE, carpeta)
        if os.path.isdir(absoluta):
            shutil.rmtree(absoluta)
    fallos = 0
    for ruta, suma in sorted(objetivo.items()):
        rel = destino(ruta)
        absoluta = os.path.join(PAQUETE, rel)
        os.makedirs(os.path.dirname(absoluta), exist_ok=True)
        shutil.copyfile(os.path.join(RAIZ, ruta), absoluta)
        if sha256(absoluta) != suma:
            print("    DIFIERE TRAS DEPOSITAR  07_Datos/%s" % rel)
            fallos += 1
    return fallos


def main():
    faltan = [p for p, m in MODULOS.items() if importlib.util.find_spec(m) is None]
    if faltan:
        print("  Faltan dependencias del analisis: %s" % ", ".join(faltan))
        print("  Instalelas con:  pip install -r %s" % os.path.relpath(REQUISITOS, os.getcwd()))
        return 3

    objetivo = esperadas()
    if not objetivo:
        print("  El manifiesto no registra ninguna salida del documento")
        return 1

    r = subprocess.run([sys.executable, REPLICAR], cwd=RAIZ,
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    if r.returncode != 0:
        print(r.stdout[-3000:])
        print("  06_Experimento/replicar.py termino con codigo %d" % r.returncode)
        return r.returncode

    distintas, ausentes = [], []
    for ruta, suma in sorted(objetivo.items()):
        absoluta = os.path.join(RAIZ, ruta)
        if not os.path.isfile(absoluta):
            ausentes.append(ruta)
        elif sha256(absoluta) != suma:
            distintas.append(ruta)

    for ruta in ausentes:
        print("    NO SE GENERO  %s" % ruta)
    for ruta in distintas:
        print("    DIFIERE       %s" % ruta)
    n_tab = sum(1 for x in objetivo if x.startswith("07_Publicacion/tablas/"))
    n_fig = sum(1 for x in objetivo if x.startswith("07_Publicacion/figuras/"))
    if ausentes or distintas:
        print("  %d de %d salidas no coinciden con el manifiesto; no se deposita nada"
              % (len(ausentes) + len(distintas), len(objetivo)))
        return 1
    print("  %d salidas identicas byte a byte al manifiesto: %d tablas, %d figuras "
          "y %d resultados intermedios" % (len(objetivo), n_tab, n_fig,
                                           len(objetivo) - n_tab - n_fig))

    if depositar(objetivo):
        return 1
    print("  Depositadas dentro del paquete:")
    for carpeta in ("resultados/tablas/", "resultados/figuras/",
                    "resultados/estadisticos/", "datos_procesados/"):
        n = sum(1 for x in objetivo if destino(x).startswith(carpeta))
        print("    07_Datos/%-26s %d" % (carpeta, n))
    return 0


if __name__ == "__main__":
    sys.exit(main())
