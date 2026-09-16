# -*- coding: utf-8 -*-
"""Empareja cada fuente editable de los diagramas con la imagen que produce — A3.

    python 10_Autoria/generar_fuentes_editables.py

Escribe 10_Autoria/fuentes_editables.md y actualiza, en 10_Autoria/README.md, la
tabla que va entre los marcadores

    <!-- inicio: tabla fuente-imagen -->
    <!-- fin: tabla fuente-imagen -->

La tabla no se escribe a mano. Se deriva de los archivos versionados de
03_Modelado/ (git ls-files) con esta regla:

- Una fuente .vpp o .drawio produce las imagenes de su misma carpeta que tienen
  su mismo nombre, con extension .png o .svg.
- Una fuente .fig produce las imagenes de su carpeta que no tienen fuente propia
  con su nombre: en este repositorio, los cuatro prototipos de Figma.

Si una fuente queda sin imagen, o una imagen sin fuente, el script lo dice y
termina con codigo 1.

Solo biblioteca estandar.
"""
import io
import os
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
CARPETA = "03_Modelado"
FUENTES = (".vpp", ".drawio", ".fig")
IMAGENES = (".png", ".svg")
HERRAMIENTA = {".vpp": "Visual Paradigm", ".drawio": "draw.io", ".fig": "Figma"}
INICIO = "<!-- inicio: tabla fuente-imagen -->"
FIN = "<!-- fin: tabla fuente-imagen -->"


def versionados():
    r = subprocess.run(["git", "ls-files", "--", CARPETA], cwd=RAIZ,
                       capture_output=True, text=True, check=True)
    return sorted(l.strip() for l in r.stdout.splitlines() if l.strip())


def emparejar(archivos):
    fuentes = [f for f in archivos if f.endswith(FUENTES)]
    imagenes = [f for f in archivos if f.endswith(IMAGENES)]
    raiz_fuente = {os.path.splitext(f)[0] for f in fuentes}
    pares = []
    usadas = set()
    for f in fuentes:
        carpeta = os.path.dirname(f)
        base, ext = os.path.splitext(f)
        if ext == ".fig":
            suyas = [i for i in imagenes if os.path.dirname(i) == carpeta
                     and os.path.splitext(i)[0] not in raiz_fuente]
        else:
            suyas = [i for i in imagenes if os.path.splitext(i)[0] == base]
        usadas.update(suyas)
        pares.append((f, sorted(suyas)))
    huerfanas = [i for i in imagenes if i not in usadas]
    return fuentes, imagenes, pares, huerfanas


def tabla(pares):
    filas = ["| Fuente editable | Imagen exportada | Carpeta |", "|---|---|---|"]
    for f, suyas in pares:
        nombres = ", ".join("`%s`" % os.path.basename(i) for i in suyas) or "**sin imagen**"
        filas.append("| `%s` | %s | `%s` |" % (os.path.basename(f), nombres, os.path.dirname(f)))
    return "\n".join(filas)


def main():
    archivos = versionados()
    fuentes, imagenes, pares, huerfanas = emparejar(archivos)
    sin_imagen = [f for f, suyas in pares if not suyas]

    cuenta_f = {e: sum(1 for f in fuentes if f.endswith(e)) for e in FUENTES}
    cuenta_i = {e: sum(1 for i in imagenes if i.endswith(e)) for e in IMAGENES}
    por_nombre = sum(1 for f, s in pares if not f.endswith(".fig") and s)
    fig = [(f, s) for f, s in pares if f.endswith(".fig")]

    md = io.StringIO()
    md.write("# Fuentes editables de los diagramas — elemento A3\n\n")
    md.write("**Proyecto SIGA · Equipo FGMMN · ISR-401 · UTEQ**\n\n")
    md.write("La guia exige el archivo fuente editable de todo diagrama junto a su imagen exportada:\n"
             "«sin el archivo fuente no hay prueba de que el diagrama se construyo y no se descargo».\n\n")
    md.write("Las fuentes **no se copian a esta carpeta**: residen junto a la imagen que producen, que\n"
             "es donde sirven para trabajar. La tabla de abajo empareja cada fuente con su imagen.\n\n")
    md.write("**Este archivo no se escribe a mano**: lo genera `generar_fuentes_editables.py` desde los\n"
             "archivos versionados de `03_Modelado/`, y la misma tabla se copia en `README.md`.\n\n")
    md.write("| Tipo de fuente | Cantidad | Herramienta |\n|---|---|---|\n")
    for e in FUENTES:
        md.write("| `%s` | %d | %s |\n" % (e, cuenta_f[e], HERRAMIENTA[e]))
    md.write("| **Total** | **%d** | |\n\n" % len(fuentes))
    md.write("| Imagen exportada | Cantidad |\n|---|---|\n")
    for e in IMAGENES:
        md.write("| `%s` | %d |\n" % (e, cuenta_i[e]))
    md.write("| **Total** | **%d** |\n\n" % len(imagenes))
    frases = ["**Como se empareja.** %d fuentes de Visual Paradigm y draw.io tienen su imagen en la "
              "misma carpeta y con el mismo nombre, exportada en `.png` y en `.svg`." % por_nombre]
    for f, s in fig:
        frases.append("El archivo de Figma `%s` produce las %d imagenes de `%s` que no tienen "
                      "fuente con su nombre." % (os.path.basename(f), len(s), os.path.dirname(f)))
    frases.append("Asi, las %d imagenes tienen su fuente y las %d fuentes tienen al menos una imagen."
                  % (len(imagenes) - len(huerfanas), len(fuentes) - len(sin_imagen)))
    md.write(" ".join(frases) + "\n\n")
    md.write("## Cada fuente con su imagen\n\n")
    md.write(tabla(pares) + "\n\n")
    md.write("## Comprobacion\n\n```\npython 10_Autoria/generar_fuentes_editables.py\n```\n\n"
             "Termina con codigo 0 solo si ninguna fuente queda sin imagen y ninguna imagen sin fuente.\n")
    io.open(os.path.join(AQUI, "fuentes_editables.md"), "w", encoding="utf-8", newline="\n").write(md.getvalue())

    readme = os.path.join(AQUI, "README.md")
    texto = io.open(readme, encoding="utf-8", newline="").read()
    if INICIO not in texto or FIN not in texto:
        print("README.md no tiene los marcadores de la tabla")
        return 1
    antes, resto = texto.split(INICIO, 1)
    _, despues = resto.split(FIN, 1)
    nl = "\r\n" if "\r\n" in texto else "\n"
    bloque = INICIO + nl + nl + tabla(pares).replace("\n", nl) + nl + nl + FIN
    io.open(readme, "w", encoding="utf-8", newline="").write(antes + bloque + despues)

    print("fuentes_editables.md y la tabla de README.md")
    print("  %d fuentes, %d imagenes" % (len(fuentes), len(imagenes)))
    for f in sin_imagen:
        print("  FUENTE SIN IMAGEN  %s" % f)
    for i in huerfanas:
        print("  IMAGEN SIN FUENTE  %s" % i)
    return 1 if (sin_imagen or huerfanas) else 0


if __name__ == "__main__":
    sys.exit(main())
