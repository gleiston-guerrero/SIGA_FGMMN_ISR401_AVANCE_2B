# -*- coding: utf-8 -*-
"""Etapa 3 - Integridad del paquete de datos.

Hace tres cosas y todas son comprobaciones, no transformaciones.

1. Correspondencia con el componente empirico. Los datos crudos de este paquete
   son los mismos que usa 06_Experimento, los scripts de scripts/analisis/ son
   los mismos que 06_Experimento/scripts_analisis/, y las salidas de la cadena de
   analisis son las mismas que produce 06_Experimento/replicar.py. Se comprueba
   que sean identicos byte a byte, no parecidos: si alguien edita una copia y no
   la otra, esto lo detecta.

2. Cobertura del diccionario. Todo archivo de datos delimitado del paquete debe
   tener descritas sus columnas en diccionario_datos.csv, y el diccionario no
   debe describir columnas que no existan.

3. Manifiesto de sumas. Regenera checksums_datos.sha256 sobre todo el paquete,
   excluyendose a si mismo.

Solo biblioteca estandar.
"""
import csv
import hashlib
import io
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
PAQUETE = os.path.dirname(AQUI)
RAIZ = os.path.dirname(PAQUETE)
MANIFIESTO = os.path.join(PAQUETE, "checksums_datos.sha256")

# Archivo del paquete -> archivo equivalente en el componente empirico.
ESPEJO = {
    "datos_crudos/juez1.csv": "06_Experimento/datos_crudos/juez1.csv",
    "datos_crudos/juez2.csv": "06_Experimento/datos_crudos/juez2.csv",
    "datos_crudos/juez3.csv": "06_Experimento/datos_crudos/juez3.csv",
    "datos_crudos/corpus_rf_rnf_etiquetado.json":
        "06_Experimento/datos_crudos/corpus_rf_rnf_etiquetado.json",
    "datos_crudos/respuestas_cuestionario.csv":
        "06_Experimento/datos_crudos/respuestas_cuestionario.csv",
    "datos_crudos/material_fuente_LLM.txt":
        "06_Experimento/prompts_llm/material_fuente_LLM.txt",
    "datos_crudos/paquete_evaluacion_ciega.md":
        "06_Experimento/instrumentos/Paquete_Evaluacion_Ciega_Jueces.md",
    "datos_crudos/codificacion_tematica.csv":
        "02_Evidencias/Codificacion_Tematica/codificacion_tematica.csv",
    "datos_crudos/transcripciones_anonimizadas.json":
        "06_Experimento/datos_crudos/transcripciones_anonimizadas.json",
}

# Cadena de analisis: la copia de este paquete y la de 06_Experimento.
for _script in ("analizar_resultados.py", "analisis_por_item.py", "curva_saturacion.py",
                "power_calculation.py", "generar_figuras.py", "generar_tablas.py"):
    ESPEJO["scripts/analisis/" + _script] = "06_Experimento/scripts_analisis/" + _script

# Salidas: las que produce la etapa analisis y las que produce replicar.py.
ESPEJO["datos_procesados/puntuaciones_consolidadas.csv"] =     "06_Experimento/datos_procesados/puntuaciones_consolidadas.csv"
for _carpeta, _origen in (("resultados/estadisticos/", "06_Experimento/resultados/"),
                          ("resultados/tablas/", "07_Publicacion/tablas/"),
                          ("resultados/figuras/", "07_Publicacion/figuras/")):
    _absoluta = os.path.join(PAQUETE, _carpeta)
    if os.path.isdir(_absoluta):
        for _nombre in sorted(os.listdir(_absoluta)):
            ESPEJO[_carpeta + _nombre] = _origen + _nombre


def sha256(ruta):
    h = hashlib.sha256()
    with open(ruta, "rb") as f:
        for bloque in iter(lambda: f.read(65536), b""):
            h.update(bloque)
    return h.hexdigest()


def archivos_del_paquete():
    salida = []
    for base, dirs, ficheros in os.walk(PAQUETE):
        dirs.sort()
        for nombre in sorted(ficheros):
            ruta = os.path.join(base, nombre)
            rel = os.path.relpath(ruta, PAQUETE).replace("\\", "/")
            if rel == "checksums_datos.sha256":
                continue
            if rel.endswith(".pyc") or "__pycache__" in rel:
                continue
            salida.append(rel)
    return salida


def comprobar_espejo():
    print("  Correspondencia con 06_Experimento")
    fallos = 0
    for rel, origen in sorted(ESPEJO.items()):
        a = os.path.join(PAQUETE, rel)
        b = os.path.join(RAIZ, origen)
        if not os.path.isfile(a) or not os.path.isfile(b):
            print("    FALTA  %s" % rel)
            fallos += 1
            continue
        if sha256(a) != sha256(b):
            print("    DIFIERE  %s" % rel)
            fallos += 1
    if not fallos:
        n_scripts = sum(1 for x in ESPEJO if x.startswith("scripts/"))
        n_salidas = sum(1 for x in ESPEJO if x.startswith(("resultados/", "datos_procesados/")))
        print("    %d archivos crudos, %d scripts de analisis y %d salidas identicos byte a byte"
              % (len(ESPEJO) - n_scripts - n_salidas, n_scripts, n_salidas))
    return fallos


def comprobar_diccionario():
    print("  Cobertura del diccionario de datos")
    ruta = os.path.join(PAQUETE, "diccionario_datos.csv")
    if not os.path.isfile(ruta):
        print("    FALTA diccionario_datos.csv")
        return 1
    descritas = {}
    with io.open(ruta, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            descritas.setdefault(r["archivo"], set()).add(r["columna"])

    fallos = 0
    for rel in archivos_del_paquete():
        if not rel.endswith(".csv") or rel == "diccionario_datos.csv":
            continue
        ruta_csv = os.path.join(PAQUETE, rel)
        with io.open(ruta_csv, encoding="utf-8") as f:
            cabecera = next(csv.reader(f), [])
        reales = set(c.strip() for c in cabecera if c.strip())
        if rel not in descritas:
            print("    SIN DESCRIBIR  %s" % rel)
            fallos += 1
            continue
        faltan = reales - descritas[rel]
        sobran = descritas[rel] - reales
        if faltan:
            print("    %s: columnas sin describir: %s" % (rel, ", ".join(sorted(faltan))))
            fallos += 1
        if sobran:
            print("    %s: el diccionario describe columnas inexistentes: %s"
                  % (rel, ", ".join(sorted(sobran))))
            fallos += 1
    if not fallos:
        print("    todas las columnas de todos los CSV estan descritas")
    return fallos


def escribir_manifiesto():
    lineas = []
    for rel in archivos_del_paquete():
        lineas.append("%s *./%s\n" % (sha256(os.path.join(PAQUETE, rel)), rel))
    with io.open(MANIFIESTO, "w", encoding="utf-8", newline="") as f:
        f.writelines(lineas)
    print("  Manifiesto de sumas")
    print("    checksums_datos.sha256 con %d entradas" % len(lineas))
    return 0


def main():
    fallos = comprobar_espejo()
    fallos += comprobar_diccionario()
    escribir_manifiesto()
    if fallos:
        print("\n  %d comprobacion(es) fallida(s)." % fallos)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
