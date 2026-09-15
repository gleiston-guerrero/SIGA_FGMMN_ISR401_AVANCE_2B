# -*- coding: utf-8 -*-
"""Pone al dia la declaracion de aporte individual y genera la version firmable.

    python 04_Trazabilidad/generar_aporte_individual.py

Produce dos artefactos que dicen lo mismo para publicos distintos:

  04_Trazabilidad/aporte_individual.csv   una fila por confirmacion
  10_Autoria/aporte_individual.md         elemento A10, para firmar

Sobre el recuento. Una declaracion de aporte no puede incluir el commit que la
deposita: ese identificador todavia no existe cuando se escribe el archivo. Por
eso el CSV llega hasta el commit inmediatamente anterior, y la diferencia con el
total del historial es siempre de una confirmacion. No es un descuadre.

Las descripciones ya escritas a mano se conservan. Para los commits nuevos se
toma el asunto del propio commit, que es lo que el autor escribio.

Solo biblioteca estandar.
"""
import collections
import csv
import io
import os
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
CSV = os.path.join(AQUI, "aporte_individual.csv")
MD = os.path.join(RAIZ, "10_Autoria", "aporte_individual.md")

REPO = "SIGA_FGMMN_ISR401_AVANCE_2B"
SEP = "\x1f"

ROLES = {
    "gsanchezc6@uteq.edu.ec":
        "Analista lider; especificacion, componente empirico e integracion",
    "ymunozq@uteq.edu.ec":
        "Documentacion, trazabilidad, auditoria de calidad y gestion de evidencias",
    "wcedenoa2@uteq.edu.ec":
        "Transcripcion y anonimizacion del corpus de entrevistas",
}
NOMBRES = {
    "gsanchezc6@uteq.edu.ec": "Gary Alberto Sanchez Cornejo",
    "ymunozq@uteq.edu.ec": "Yeranick Esther Munoz Quinonez",
    "wcedenoa2@uteq.edu.ec": "Winston Damian Cedeno Avila",
}
AREAS = [
    ("01_ERS", "Especificacion de requisitos"),
    ("02_Evidencias", "Evidencia de campo y etica"),
    ("03_Modelado", "Modelado UML e i*"),
    ("04_Trazabilidad", "Trazabilidad"),
    ("05_MVP", "Producto minimo viable"),
    ("06_Experimento", "Componente empirico"),
    ("07_Datos", "Paquete de datos"),
    ("07_Publicacion", "Manuscrito y deposito"),
    ("08_Defensa", "Defensa"),
    ("10_Autoria", "Evidencia de autoria"),
]


def git(*a):
    r = subprocess.run(["git"] + list(a), cwd=RAIZ, capture_output=True,
                       text=True, encoding="utf-8")
    if r.returncode:
        print("git fallo:", r.stderr.strip())
        sys.exit(1)
    return r.stdout


def area_de(ruta):
    for pre, nom in AREAS:
        if ruta.startswith(pre):
            return nom
    return "Documentos de raiz" if "/" not in ruta else "Otros"


def main():
    previas = {}
    campos = ["integrante", "rol", "repositorio", "commit", "fecha",
              "correo_de_la_firma", "aporte_descrito"]
    if os.path.isfile(CSV):
        with io.open(CSV, encoding="utf-8") as f:
            lector = csv.DictReader(f)
            campos = lector.fieldnames
            for r in lector:
                previas[r["commit"]] = r["aporte_descrito"]

    crudo = git("log", "--reverse", "--date=short",
                "--pretty=format:%h" + SEP + "%ae" + SEP + "%ad" + SEP + "%s")
    commits = [l.split(SEP) for l in crudo.split("\n") if l.strip()]

    # Se genera ANTES de crear el commit que deposita la declaracion firmada, asi
    # que se cuentan todos los commits existentes al imprimirla. El del deposito
    # no puede constar: todavia no existe cuando se firma.

    filas, nuevos = [], 0
    for h, correo, fecha, asunto in commits:
        if correo not in ROLES:
            print("AVISO: correo no declarado en el equipo: %s (%s)" % (correo, h))
        if h in previas:
            aporte = previas[h]
        else:
            aporte = asunto
            nuevos += 1
        filas.append({
            "integrante": NOMBRES.get(correo, "Autor no declarado"),
            "rol": ROLES.get(correo, "Rol no declarado"),
            "repositorio": REPO,
            "commit": h,
            "fecha": fecha,
            "correo_de_la_firma": correo,
            "aporte_descrito": aporte,
        })

    with io.open(CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=campos)
        w.writeheader()
        w.writerows(filas)

    # --- resumen por persona, para el documento firmable ---
    por_correo = collections.OrderedDict()
    for correo in ROLES:
        por_correo[correo] = []
    for fila in filas:
        por_correo.setdefault(fila["correo_de_la_firma"], []).append(fila)

    areas = {}
    for h, correo, _, _ in commits:
        for ruta in git("show", "--name-only", "--pretty=format:", h).split("\n"):
            ruta = ruta.strip()
            if ruta:
                areas.setdefault(correo, collections.Counter())[area_de(ruta)] += 1

    L = []
    L.append("# Declaracion de aporte individual")
    L.append("")
    L.append("**Proyecto SIGA · Equipo FGMMN · ISR-401 · Universidad Tecnica Estatal de Quevedo**")
    L.append("")
    L.append("Elemento **A10** de la evidencia de autoria. Declara que hizo cada integrante, "
             "sobre que")
    L.append("artefactos y con que confirmaciones del historial se acredita.")
    L.append("")
    L.append("Este documento **no se escribe a mano**: se genera con "
             "`04_Trazabilidad/generar_aporte_individual.py`")
    L.append("desde el propio historial. El detalle confirmacion por confirmacion esta en "
             "[`../04_Trazabilidad/aporte_individual.csv`](../04_Trazabilidad/aporte_individual.csv).")
    L.append("")
    L.append("---")
    L.append("")
    L.append("## Resumen")
    L.append("")
    L.append("| Integrante | Correo institucional | Commits | Primera | Ultima |")
    L.append("|---|---|---|---|---|")
    for correo in ROLES:
        g = por_correo.get(correo, [])
        if g:
            L.append("| %s | %s | **%d** | %s | %s |" %
                     (NOMBRES[correo], correo, len(g), g[0]["fecha"], g[-1]["fecha"]))
        else:
            L.append("| %s | %s | **0** | — | — |" % (NOMBRES[correo], correo))
    L.append("")
    L.append("Comprobable con `git shortlog -sne main`. El total de esta tabla es una "
             "confirmacion")
    L.append("menor que el historial completo, porque la declaracion no puede incluir el "
             "commit que la deposita.")
    L.append("")

    for correo in ROLES:
        g = por_correo.get(correo, [])
        L.append("---")
        L.append("")
        L.append("## %s" % NOMBRES[correo])
        L.append("")
        L.append("**Rol:** %s" % ROLES[correo])
        L.append("")
        if not g:
            L.append("**Confirmaciones a la fecha de esta declaracion: ninguna.**")
            L.append("")
            L.append("Se incorporo al equipo el 2026-09-02 y su trabajo comienza con la ronda "
                     "terminal de")
            L.append("campo. Se declara el cero en lugar de atribuirle una contribucion que el "
                     "historial")
            L.append("todavia no respalda; la declaracion se regenera en cuanto exista su "
                     "primera confirmacion.")
            L.append("")
            continue
        L.append("**Confirmaciones: %d**, de %s a %s." % (len(g), g[0]["fecha"], g[-1]["fecha"]))
        L.append("")
        L.append("### Areas sobre las que trabajo")
        L.append("")
        L.append("| Area | Archivos tocados |")
        L.append("|---|---|")
        for area, n in areas.get(correo, collections.Counter()).most_common():
            L.append("| %s | %d |" % (area, n))
        L.append("")
        L.append("### Confirmaciones")
        L.append("")
        L.append("| Commit | Fecha | Aporte |")
        L.append("|---|---|---|")
        for fila in g:
            L.append("| `%s` | %s | %s |" % (fila["commit"], fila["fecha"],
                                             fila["aporte_descrito"].replace("|", "/")))
        L.append("")

    L.append("---")
    L.append("")
    L.append("## Firmas")
    L.append("")
    L.append("Cada integrante firma declarando que el aporte que consta arriba a su nombre es "
             "suyo,")
    L.append("y que no reclama trabajo de otra persona.")
    L.append("")
    for correo in ROLES:
        L.append("")
        L.append("**%s**" % NOMBRES[correo])
        L.append("")
        L.append("Firma: ______________________________    Fecha: ______________")
        L.append("")
    L.append("---")
    L.append("")
    L.append("Generado el %s desde el historial del repositorio."
             % git("log", "-1", "--date=short", "--pretty=%ad").strip())

    os.makedirs(os.path.dirname(MD), exist_ok=True)
    io.open(MD, "w", encoding="utf-8").write("\n".join(L) + "\n")

    print("aporte_individual.csv")
    print("  %d filas (%d nuevas), sobre %d commits del historial"
          % (len(filas), nuevos, len(commits) + 1))
    for correo in ROLES:
        print("    %-32s %3d" % (NOMBRES[correo], len(por_correo.get(correo, []))))
    print("aporte_individual.md")
    print("  elemento A10, con bloque de firmas para los %d integrantes" % len(ROLES))
    return 0


if __name__ == "__main__":
    sys.exit(main())
