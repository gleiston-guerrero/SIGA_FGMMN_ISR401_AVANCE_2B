# -*- coding: utf-8 -*-
"""Genera la caratula de identificacion para el Sistema de Gestion Academica.

    python generar_caratula.py

Escribe caratula_identificacion_SGA.tex y lo compila a PDF.

Por que se genera y no se escribe a mano. La caratula declara el ultimo commit
y la etiqueta de linea base, y las dos cosas cambian cada vez que se toca el
repositorio. La version anterior era un PDF de Word sin fuente versionada, con
el hueco de ULTIMO COMMIT en blanco y la etiqueta apuntando a 2B-final-v3.0
cuando la vigente ya era otra. Un dato que hay que teclear a mano acaba
caducando; uno que se lee del repositorio, no.

El contenido y su orden son los mismos que tenia el documento de Word. Lo unico
que cambia es de donde salen el commit, su fecha y la etiqueta.

Solo biblioteca estandar y pdflatex.
"""
import io
import os
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
BASE = "caratula_identificacion_SGA"
TEX = os.path.join(AQUI, BASE + ".tex")
PDF = os.path.join(AQUI, BASE + ".pdf")

PLANTILLA = r"""\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[spanish,es-noquoting]{babel}
\usepackage[margin=2.5cm]{geometry}
\usepackage{url}
\pagestyle{empty}
\setlength{\parindent}{0pt}

\begin{document}

\textbf{TEMA:}\\
Proyecto Fin de Curso: Entrega 2B -- Proyecto Integrador Final.

\bigskip
\textbf{ESTUDIANTES:}\\
Cede\~no Avila Winston Damian | CI: 0942833492 | wcedenoa2@uteq.edu.ec\\
Mu\~noz Qui\~nonez Yeranick Esther | CI: 1207929645 | ymunozq@uteq.edu.ec\\
Sanchez Cornejo Gary Alberto | CI: 1208338291 | gsanchezc6@uteq.edu.ec

\bigskip
\textbf{CURSO:}\\
4TO ``B''

\bigskip
\textbf{DOCENTE:}\\
Ing. Guerrero Ulloa Gleiston Ciceron

\bigskip
\textbf{MATERIA:}\\
Ingenier\'ia de Requerimientos

\bigskip
\textbf{REPOSITORIO GITHUB:}\\
\url{https://github.com/gleiston-guerrero/SIGA_FGMMN_ISR401_AVANCE_2B.git}

\bigskip
\textbf{ULTIMO COMMIT:}\\
\texttt{%(commit)s} --- %(fecha)s

\vspace{2cm}
\begin{center}
QUEVEDO -- LOS R\'IOS -- ECUADOR\\
2026 -- 2027 PPA
\end{center}

\vspace{1cm}
Etiqueta de linea base: \texttt{%(etiqueta)s}

\end{document}
"""


def git(*a):
    r = subprocess.run(["git"] + list(a), cwd=AQUI, capture_output=True, text=True)
    return r.stdout.strip()


def main():
    datos = {
        "commit": git("rev-parse", "--short=7", "HEAD"),
        "fecha": git("log", "-1", "--date=format:%d/%m/%Y %H:%M", "--pretty=%ad"),
        "etiqueta": git("describe", "--tags", "--abbrev=0") or "sin etiqueta",
    }
    io.open(TEX, "w", encoding="utf-8", newline="\n").write(PLANTILLA % datos)

    subprocess.run(["pdflatex", "-interaction=batchmode", BASE + ".tex"],
                   cwd=AQUI, capture_output=True, text=True)
    if not os.path.isfile(PDF):
        print("pdflatex no produjo el PDF")
        return 1
    for ext in (".aux", ".log", ".out"):
        f = os.path.join(AQUI, BASE + ext)
        if os.path.isfile(f):
            os.remove(f)
    print(BASE + ".pdf")
    print("  ultimo commit: %(commit)s --- %(fecha)s" % datos)
    print("  etiqueta:      %(etiqueta)s" % datos)
    return 0


if __name__ == "__main__":
    sys.exit(main())
