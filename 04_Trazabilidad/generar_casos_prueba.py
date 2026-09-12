# -*- coding: utf-8 -*-
"""Genera 04_Trazabilidad/casos_prueba.csv, el catalogo de casos de prueba.

    python 04_Trazabilidad/generar_casos_prueba.py

Por que existe. La matriz de trazabilidad declara, para cada requisito, el caso
de prueba que lo verifica, y esos identificadores no correspondian a ningun
documento: la columna enlazaba con nada. Este catalogo los define, y la
comprobacion final del script exige correspondencia exacta en los dos sentidos:
ningun caso de prueba citado por la matriz puede faltar aqui, y ningun caso
definido aqui puede sobrar.

De donde sale cada campo. El objetivo y el resultado esperado se derivan del
enunciado del requisito tal como consta en la matriz, que es donde vive su
umbral. El elemento de diseno y el caso de uso salen de las columnas
correspondientes. Para los ocho requisitos del componente inteligente, el metodo
de verificacion se toma literalmente de su ficha, que ya lo especifica.

Lo que el catalogo NO afirma. No dice que las pruebas se hayan ejecutado. La
columna `ejecutable_hoy` distingue lo que el prototipo permite comprobar ahora
de lo que exige un sistema desplegado, y esa distincion se lee de
05_MVP/cobertura_requisitos.csv, no se supone.

Solo biblioteca estandar.
"""
import csv
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
MATRIZ = os.path.join(AQUI, "matriz_trazabilidad.csv")
COBERTURA = os.path.join(RAIZ, "05_MVP", "cobertura_requisitos.csv")
FICHA_IA = os.path.join(RAIZ, "01_ERS", "Componentes_IA",
                        "requisitos_no_funcionales_ia.csv")
SALIDA = os.path.join(AQUI, "casos_prueba.csv")

CAMPOS = ["ID", "Requisito", "Tipo_de_prueba", "Objetivo", "Precondicion",
          "Procedimiento", "Resultado_esperado", "Criterio_de_aceptacion",
          "Elemento_de_diseno", "Caso_de_uso", "Ejecutable_hoy", "Estado"]

# Umbral explicito dentro del enunciado: ">=95%", "<=2 s", "99%"...
RE_UMBRAL = re.compile(r"(>=|<=|>|<|maximo de|minimo de)?\s*"
                       r"(\d+[.,]?\d*)\s*(%|s\b|segundos|minutos|horas|dias|"
                       r"palabras|puntos porcentuales|MB)", re.I)


def cobertura_mvp():
    """RF -> True si el prototipo lo implementa."""
    d = {}
    with io.open(COBERTURA, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            d[r["ID-RF"].strip()] = r["Implementado"].strip().lower() == "si"
    return d


def fichas_ia():
    if not os.path.isfile(FICHA_IA):
        return {}
    with io.open(FICHA_IA, encoding="utf-8-sig") as f:
        return {r["Caso_de_prueba"]: r for r in csv.DictReader(f)}


def limpiar(t, n=None):
    t = " ".join(t.split())
    if n and len(t) > n:
        t = t[:n - 3].rsplit(" ", 1)[0] + "..."
    return t


def resultado(umbral, ca):
    """El resultado esperado se ancla en el criterio Gherkin cuando existe."""
    if umbral:
        base = "El sistema cumple el umbral declarado: %s" % umbral
    else:
        base = ("El comportamiento observado coincide con el enunciado del "
                "requisito, sin excepciones")
    if ca and not ca.startswith("Sin "):
        base += (". Se da por superada la prueba cuando se satisface el escenario "
                 "Gherkin de %s, definido en el ERS" % ca)
    return base


def procedimiento(tipo, objetivo, elemento, umbral):
    """Procedimiento acorde al tipo de requisito. No hay plantilla unica."""
    if tipo == "RF":
        return ("1) Autenticarse con un rol autorizado. "
                "2) Reproducir el escenario Gherkin del criterio de aceptacion "
                "asociado, sobre %s en el entorno de prueba. "
                "3) Observar la respuesta del sistema y su registro en bitacora. "
                "4) Repetir con datos limite y con un rol no autorizado, para "
                "comprobar que la funcion se deniega a quien no debe usarla."
                % (elemento or "el elemento correspondiente"))
    if tipo == "RD":
        return ("Revision documental. 1) Localizar en el diseno y en el codigo el "
                "punto donde la restriccion se materializa. 2) Comprobar que no "
                "existe ninguna ruta que la eluda. 3) Dejar constancia de la "
                "revision con fecha y revisor. No se verifica por ejecucion: una "
                "restriccion de diseno se comprueba mirando el diseno.")
    if umbral:
        return ("Medicion contra umbral. 1) Preparar el escenario descrito en la "
                "precondicion. 2) Tomar al menos 30 mediciones independientes de "
                "la magnitud del requisito. 3) Calcular el estadistico declarado y "
                "su intervalo de confianza del 95 %%. 4) Comparar con el umbral "
                "%s. Una medicion aislada no decide: el intervalo debe quedar del "
                "lado correcto." % umbral)
    return ("Medicion cualitativa. 1) Preparar el escenario de la precondicion. "
            "2) Ejecutar el escenario con participantes del perfil destinatario. "
            "3) Registrar el resultado y la evidencia que lo sostiene.")


def main():
    # utf-8-sig: la matriz lleva marca de orden de bytes, y con utf-8 a secas la
    # primera columna se lee como "﻿ID" y el script falla.
    with io.open(MATRIZ, encoding="utf-8-sig") as f:
        filas = list(csv.DictReader(f))
    mvp = cobertura_mvp()
    ia = fichas_ia()

    casos, vistos = [], set()
    for r in filas:
        for cp in [c.strip() for c in r["ID-CasoPrueba"].split(";") if c.strip()]:
            # Solo son identificadores de caso de prueba los que empiezan por
            # CP-. La matriz usa esta columna tambien para decir que no hay
            # caso de prueba: "Sin caso de prueba asociado", "No aplica
            # (restriccion de diseno)". Eso no es un identificador.
            if not cp.startswith("CP-") or cp in vistos:
                continue
            vistos.add(cp)

            req = cp.replace("CP-", "")
            tipo = r["Tipo"]
            elemento = limpiar(r["ID-Componente"], 120)
            if elemento.startswith("Sin "):
                elemento = "Sin componente asociado"
            objetivo = limpiar(r["Objetivo"], 200)
            cu = limpiar(r["ID-CU"], 60)
            ca = limpiar(r["ID-CA"], 80)
            if ca.startswith("Sin "):
                ca = "Sin criterio de aceptacion asociado"

            m = RE_UMBRAL.search(objetivo)
            umbral = limpiar(m.group(0)) if m else ""

            if cp in ia:
                d = ia[cp]
                casos.append({
                    "ID": cp,
                    "Requisito": d["ID"],
                    "Tipo_de_prueba": "Medicion contra umbral, componente inteligente",
                    "Objetivo": limpiar(d["Enunciado_verificable"], 300),
                    "Precondicion": ("Componente inteligente en operacion con datos "
                                     "suficientes; responsable designado: %s"
                                     % limpiar(d["Responsable"], 90)),
                    "Procedimiento": limpiar(d["Metodo_de_verificacion"], 420),
                    "Resultado_esperado": "%s, medido en %s" % (limpiar(d["Umbral"]),
                                                               limpiar(d["Unidad"])),
                    "Criterio_de_aceptacion": ca,
                    "Elemento_de_diseno": limpiar(d["Elemento_de_diseno"], 120),
                    "Caso_de_uso": cu,
                    "Ejecutable_hoy": "No: exige el sistema desplegado",
                    "Estado": limpiar(d["Estado_de_verificacion"], 200),
                })
                continue

            impl = mvp.get(req)
            if tipo == "RD":
                ejecutable = "No aplica: se verifica por revision documental"
            elif impl is True:
                ejecutable = "Si: el prototipo implementa el requisito"
            elif impl is False:
                ejecutable = "No: el prototipo no implementa el requisito"
            else:
                ejecutable = "No: requisito no funcional, exige medicion en operacion"

            casos.append({
                "ID": cp,
                "Requisito": req,
                "Tipo_de_prueba": {"RF": "Funcional",
                                   "RNF": "No funcional, medicion contra umbral",
                                   "RD": "Revision documental de restriccion de diseno"}[tipo],
                "Objetivo": "Comprobar que se cumple: %s" % objetivo,
                "Precondicion": ("Entorno de prueba desplegado con datos de ejemplo; "
                                 "elemento bajo prueba disponible: %s" % elemento),
                "Procedimiento": procedimiento(tipo, objetivo, elemento, umbral),
                "Resultado_esperado": resultado(umbral, ca),
                "Criterio_de_aceptacion": ca,
                "Elemento_de_diseno": elemento,
                "Caso_de_uso": cu,
                "Ejecutable_hoy": ejecutable,
                "Estado": "Especificado, no ejecutado",
            })

    casos.sort(key=lambda c: (c["ID"].count("-"), c["ID"]))
    with io.open(SALIDA, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS)
        w.writeheader()
        w.writerows(casos)

    # --- correspondencia exacta con la matriz, en los dos sentidos ---
    citados = set()
    for r in filas:
        for c in r["ID-CasoPrueba"].split(";"):
            c = c.strip()
            if c.startswith("CP-"):
                citados.add(c)
    definidos = {c["ID"] for c in casos}
    faltan = citados - definidos
    sobran = definidos - citados

    print("casos_prueba.csv")
    print("  %d casos definidos" % len(casos))
    print("  %d citados por la matriz" % len(citados))
    por_tipo = {}
    for c in casos:
        por_tipo[c["Tipo_de_prueba"]] = por_tipo.get(c["Tipo_de_prueba"], 0) + 1
    for k in sorted(por_tipo):
        print("    %-52s %d" % (k, por_tipo[k]))
    ejec = sum(1 for c in casos if c["Ejecutable_hoy"].startswith("Si"))
    print("  %d ejecutables hoy sobre el prototipo" % ejec)

    if faltan:
        print("\n  ERROR: citados por la matriz y no definidos: %s"
              % ", ".join(sorted(faltan)))
    if sobran:
        print("\n  ERROR: definidos y no citados: %s" % ", ".join(sorted(sobran)))
    if faltan or sobran:
        return 1
    print("  correspondencia exacta con la matriz en los dos sentidos")
    return 0


if __name__ == "__main__":
    sys.exit(main())
