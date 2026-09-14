# -*- coding: utf-8 -*-
"""Genera 10_Autoria/bitacora_sesiones.csv a partir del historial de versiones.

La bitacora no se escribe a mano. Cada campo se deriva del propio historial, de
modo que cualquiera puede regenerarla y obtener lo mismo:

    python 10_Autoria/generar_bitacora.py

Que es una sesion. Una sesion es el trabajo de una persona en un dia. Se agrupa
asi porque es la unidad que el historial permite delimitar sin suponer nada: la
hora de inicio es la de su primer commit de ese dia, la de fin la del ultimo, y
los artefactos trabajados son las rutas que esos commits tocaron. Con este
criterio existe al menos una fila por cada dia en que el repositorio registra
commits, que es lo que exige el elemento A1 de la guia de desarrollo.

Lo que la bitacora NO puede reconstruir, y por eso no lo inventa: el tiempo de
trabajo anterior al primer commit del dia. La hora de inicio es la del primer
commit, no la del momento en que la persona se sento a trabajar. Se declara asi
en la propia columna.

Solo biblioteca estandar.
"""
import collections
import csv
import io
import os
import subprocess
import sys
import unicodedata

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
SALIDA = os.path.join(AQUI, "bitacora_sesiones.csv")

SEP = "\x1f"
FIN = "\x1e"

# Usuario de GitHub de cada integrante. El de Gary consta en la URL del
# repositorio y el de Winston lo confirmo el equipo el 2026-09-03.
USUARIO_GIT = {
    "gsanchezc6@uteq.edu.ec": "gsanchezc6-beep",
    "ymunozq@uteq.edu.ec": "ymunozq",
    "wcedenoa2@uteq.edu.ec": "WinstonCD",
}

# Prefijo de ruta -> area de trabajo, para describir que se toco.
AREAS = [
    ("01_ERS", "Especificacion de requisitos"),
    ("02_Evidencias", "Evidencia de campo"),
    ("03_Modelado", "Modelado UML e i*"),
    ("04_Trazabilidad", "Trazabilidad y aporte individual"),
    ("05_MVP", "Producto minimo viable"),
    ("06_Experimento", "Componente empirico"),
    ("07_Datos", "Paquete de datos"),
    ("07_Publicacion", "Manuscrito y deposito"),
    ("08_Defensa", "Defensa"),
    ("10_Autoria", "Evidencia de autoria"),
]


def git(*args):
    r = subprocess.run(["git"] + list(args), cwd=RAIZ,
                       capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        print("git fallo: %s" % r.stderr.strip())
        sys.exit(1)
    return r.stdout


def area_de(ruta):
    for prefijo, nombre in AREAS:
        if ruta.startswith(prefijo):
            return nombre
    if "/" not in ruta:
        return "Documentos de raiz"
    return "Otros"


# --------------------------------------------------------------------------
# Sesiones de elicitacion y notas de campo (guia de cierre del 2026-09-14, 15)
#
# Ademas de las sesiones de trabajo sobre el repositorio, la bitacora registra
# una fila por sesion de elicitacion con participante. Tampoco se escriben a
# mano: cada sesion sale de la tabla de metadatos de su transcripcion en
# 02_Evidencias/Transcripciones/, y la nota de campo, del archivo que exista en
# 10_Autoria/notas_campo/ con su fecha y su codigo de participante.
#
# Lo unico declarado es el motivo de las sesiones que no tienen nota, en
# notas_campo/sesiones_sin_nota.csv, que tambien recoge las sesiones sin
# transcripcion. Cada sesion debe tener nota o motivo, y solo una de las dos
# cosas: si falta o sobra, el script lo dice y termina con codigo 1.

TRANSCRIPCIONES = os.path.join(RAIZ, "02_Evidencias", "Transcripciones")
NOTAS = os.path.join(AQUI, "notas_campo")
SIN_NOTA = os.path.join(NOTAS, "sesiones_sin_nota.csv")


def _clave(texto):
    sin_tildes = unicodedata.normalize("NFKD", texto)
    return "".join(c for c in sin_tildes if not unicodedata.combining(c)).lower().strip()


def _metadatos(ruta):
    campos = {}
    with io.open(ruta, encoding="utf-8") as f:
        for linea in f:
            if linea.startswith("---"):
                break
            if linea.startswith("|") and linea.count("|") >= 3:
                partes = [p.strip() for p in linea.strip().strip("|").split("|")]
                campos[_clave(partes[0])] = partes[1]
    return campos


def sesiones_elicitacion():
    declaradas = collections.OrderedDict()
    with io.open(SIN_NOTA, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            declaradas[r["evidencia"]] = r

    notas = sorted(n for n in os.listdir(NOTAS) if n.endswith("_Notas.jpg"))
    filas, problemas, vistas = [], [], set()

    def fila(ev, fecha, tecnica, codigo, ruta):
        nota = [n for n in notas if n.startswith(fecha + "_") and ("_%s_Notas." % codigo) in n]
        motivo = declaradas.get(ev, {}).get("motivo", "").strip()
        if nota and motivo:
            problemas.append("%s tiene nota y motivo declarado a la vez" % ev)
        if not nota and not motivo:
            problemas.append("%s (%s, %s) no tiene nota de campo ni motivo declarado" % (ev, fecha, codigo))
        vistas.add(ev)
        return {
            "identificador": "E-" + ev, "fecha": fecha, "hora_inicio": "", "hora_fin": "",
            "modalidad": "Sesion de elicitacion: " + tecnica, "participante": codigo,
            "usuario_git": "", "correo_institucional": "",
            "areas_trabajadas": "Evidencia de campo", "rutas_tocadas": ruta,
            "decisiones": "", "commits": "", "n_commits": 0, "n_archivos": 0,
            "notas_campo": "; ".join("10_Autoria/notas_campo/" + n for n in nota),
            "motivo_sin_notas": motivo,
        }

    for nombre in sorted(os.listdir(TRANSCRIPCIONES)):
        if not nombre.endswith("_Transcripcion.md"):
            continue
        m = _metadatos(os.path.join(TRANSCRIPCIONES, nombre))
        filas.append(fila(m["identificador de evidencia"], m["fecha de la sesion"],
                          m["tecnica de elicitacion"], m["codigo de participante"],
                          "02_Evidencias/Transcripciones/" + nombre))

    for ev, r in declaradas.items():
        if ev not in vistas:
            filas.append(fila(ev, r["fecha"], r["tecnica"], r["codigo_participante"], r["fuente"]))

    usadas = set()
    for f_ in filas:
        for n in f_["notas_campo"].split("; "):
            if n:
                usadas.add(n.rsplit("/", 1)[-1])
    for n in notas:
        if n not in usadas:
            problemas.append("la nota %s no corresponde a ninguna sesion" % n)
    return filas, problemas


def main():
    formato = SEP.join(["%H", "%h", "%an", "%ae", "%ad", "%s"]) + FIN
    crudo = git("log", "--reverse", "--date=format:%Y-%m-%d %H:%M",
                "--pretty=format:" + formato)

    commits = []
    for bloque in crudo.split(FIN):
        bloque = bloque.strip("\n")
        if not bloque:
            continue
        h, corto, autor, correo, fecha, asunto = bloque.split(SEP)
        dia, hora = fecha.split(" ")
        archivos = git("show", "--name-only", "--pretty=format:", h)
        rutas = [l.strip() for l in archivos.split("\n") if l.strip()]
        commits.append({
            "h": corto, "autor": autor, "correo": correo,
            "dia": dia, "hora": hora, "asunto": asunto, "rutas": rutas,
        })

    sesiones = collections.OrderedDict()
    for c in commits:
        sesiones.setdefault((c["dia"], c["correo"]), []).append(c)

    campos = ["identificador", "fecha", "hora_inicio", "hora_fin", "modalidad",
              "participante", "usuario_git", "correo_institucional",
              "areas_trabajadas", "rutas_tocadas", "decisiones",
              "commits", "n_commits", "n_archivos", "notas_campo", "motivo_sin_notas"]
    filas = []
    contador = collections.Counter()

    for (dia, correo), grupo in sesiones.items():
        contador[dia] += 1
        ident = "S-%s-%d" % (dia.replace("-", ""), contador[dia])
        rutas = []
        for c in grupo:
            for r in c["rutas"]:
                if r not in rutas:
                    rutas.append(r)
        areas = []
        for r in rutas:
            a = area_de(r)
            if a not in areas:
                areas.append(a)
        decisiones = " | ".join(dict.fromkeys(c["asunto"] for c in grupo))
        filas.append({
            "identificador": ident,
            "fecha": dia,
            "hora_inicio": grupo[0]["hora"],
            "hora_fin": grupo[-1]["hora"],
            "modalidad": "Trabajo individual sobre el repositorio",
            "participante": grupo[0]["autor"],
            "usuario_git": USUARIO_GIT.get(correo, "no declarado"),
            "correo_institucional": correo,
            "areas_trabajadas": "; ".join(areas),
            "rutas_tocadas": "; ".join(rutas[:12]) + (" ; (+%d mas)" % (len(rutas) - 12)
                                                      if len(rutas) > 12 else ""),
            "decisiones": decisiones,
            "commits": " ".join(c["h"] for c in grupo),
            "n_commits": len(grupo),
            "n_archivos": len(rutas),
            "notas_campo": "",
            "motivo_sin_notas": "",
        })

    n_trabajo = len(filas)
    elicitacion, problemas = sesiones_elicitacion()
    if problemas:
        print("Sesiones de elicitacion sin resolver:")
        for x in problemas:
            print("  " + x)
        sys.exit(1)
    filas.extend(elicitacion)
    filas.sort(key=lambda f: (f["fecha"], f["hora_inicio"]))
    with io.open(SALIDA, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=campos)
        w.writeheader()
        w.writerows(filas)

    dias = sorted(set(f["fecha"] for f in filas if f["n_commits"]))
    print("bitacora_sesiones.csv")
    print("  %d sesiones de trabajo sobre %d dias con commits" % (n_trabajo, len(dias)))
    con_nota = sum(1 for f in elicitacion if f["notas_campo"])
    print("  %d sesiones de elicitacion: %d con nota de campo, %d sin nota y con motivo declarado"
          % (len(elicitacion), con_nota, len(elicitacion) - con_nota))
    print("  del %s al %s" % (dias[0], dias[-1]))
    print("  %d commits en total" % sum(f["n_commits"] for f in filas))
    faltan = [d for d in dias if not any(f["fecha"] == d for f in filas)]
    if faltan:
        print("  ERROR: dias con commits sin fila: %s" % ", ".join(faltan))
        return 1
    print("  todos los dias con commits tienen al menos una fila")
    return 0


if __name__ == "__main__":
    sys.exit(main())
