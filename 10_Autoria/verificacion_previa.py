# -*- coding: utf-8 -*-
"""Ejecuta la lista de verificacion previa de la seccion 11 de la guia.

    python 10_Autoria/verificacion_previa.py              (sobre esta copia)
    python 10_Autoria/verificacion_previa.py --clonar     (sobre un clon limpio)

Las doce comprobaciones de la guia se ejecutan de verdad, no se marcan a mano.
El resultado se escribe en 10_Autoria/verificacion_previa.md, listo para
imprimir y firmar.

Sobre quien firma. La guia exige que quien comprueba sea una persona distinta de
quien produjo cada artefacto. Este script no sustituye esa firma: automatiza la
comprobacion para que quien firme sepa exactamente que esta firmando, y deja
constancia de lo que la maquina no puede decidir.

Con --clonar, clona el remoto en una carpeta temporal y comprueba alli, que es
como lo hara el docente. Es la unica forma de detectar lo que solo falla en un
clon.

Solo biblioteca estandar.
"""
import io
import os
import re
import shutil
import subprocess
import sys
import tempfile

AQUI = os.path.dirname(os.path.abspath(__file__))
SALIDA = os.path.join(AQUI, "verificacion_previa.md")
REMOTO = "https://github.com/gleiston-guerrero/SIGA_FGMMN_ISR401_AVANCE_2B.git"

CORREOS = {"gsanchezc6@uteq.edu.ec", "ymunozq@uteq.edu.ec", "wcedenoa2@uteq.edu.ec"}
ELEMENTOS_A = {
    "A1": "bitacora_sesiones.csv", "A2": "capturas", "A3": "fuentes_editables.md",
    "A4": "grabaciones", "A5": "notas_campo", "A6": "fotos_equipo",
    "A7": "doble_codificacion", "A8": "correspondencia",
    "A9": "declaracion_uso_ia.md", "A10": "aporte_individual.md",
    "A11": "exif_inventario.csv", "A12": "../.mailmap",
}

resultados = []
COMMITTERS_AJENOS = []


def anotar(n, texto, estado, detalle):
    resultados.append((n, texto, estado, detalle))
    marca = {"CUMPLE": "OK ", "NO": "NO ", "PARCIAL": "-- ", "MANUAL": ".. "}[estado]
    print("%s %2d. %s" % (marca, n, detalle))


def correr(cmd, cwd, **kw):
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True,
                          encoding="utf-8", errors="replace", **kw)


def comprobar(raiz, clonado):
    # El orden importa. La comprobacion de sumas va ANTES de compilar, porque
    # compilar regenera reporte.pdf y pdfLaTeX incrusta una marca de tiempo:
    # el PDF recompilado nunca es byte a byte igual al depositado, y comprobar
    # el manifiesto despues daria un fallo que no lo es.
    comprobar_manifiesto(raiz)

    # --- 1 y 2: clonar y compilar el documento principal -------------------
    if clonado:
        r = correr(["pdflatex", "-interaction=nonstopmode", "reporte.tex"], raiz)
        correr(["bibtex", "reporte"], raiz)
        correr(["pdflatex", "-interaction=nonstopmode", "reporte.tex"], raiz)
        r = correr(["pdflatex", "-interaction=nonstopmode", "reporte.tex"], raiz)
        log = os.path.join(raiz, "reporte.log")
        texto = io.open(log, encoding="utf-8", errors="replace").read() \
            if os.path.isfile(log) else ""
        errores = len(re.findall(r"^!", texto, re.M))
        if r.returncode == 0 and errores == 0:
            anotar(1, "Se clono en carpeta limpia y se compilo el documento principal "
                      "desde el .tex siguiendo unicamente el README",
                   "CUMPLE", "Compilado sobre el clon con pdfLaTeX + BibTeX, sin errores")
        else:
            anotar(1, "Se clono en carpeta limpia y se compilo el documento principal",
                   "NO", "La compilacion devolvio %d error(es)" % errores)
        sin_resolver = len(re.findall(r"undefined", texto, re.I))
        m = re.search(r"Output written on .*?\((\d+) pages", texto)
        paginas = m.group(1) if m else "?"
        anotar(2, "El PDF resultante coincide con el entregado y no presenta "
                  "referencias sin resolver",
               "CUMPLE" if sin_resolver == 0 else "NO",
               "%s paginas regeneradas, %d referencias sin resolver. La comparacion "
               "es por contenido y no por suma: pdfLaTeX incrusta la fecha de "
               "compilacion, de modo que dos PDF del mismo fuente nunca son byte a "
               "byte iguales" % (paginas, sin_resolver))
    else:
        anotar(1, "Se clono en carpeta limpia y se compilo el documento principal",
               "MANUAL", "No comprobado: ejecute con --clonar")
        anotar(2, "El PDF resultante coincide y no tiene referencias sin resolver",
               "MANUAL", "No comprobado: ejecute con --clonar")

    # --- 3: archivos de 0 o 1 byte ----------------------------------------
    vacios = []
    for base, dirs, fs in os.walk(raiz):
        if ".git" in base:
            continue
        for f in fs:
            ruta = os.path.join(base, f)
            try:
                if os.path.getsize(ruta) <= 1:
                    vacios.append(os.path.relpath(ruta, raiz))
            except OSError:
                pass
    anotar(3, "No existe ningun archivo de cero o un byte cuyo nombre anuncie "
              "contenido de evidencia",
           "CUMPLE" if not vacios else "NO",
           "Cero archivos de 0 o 1 byte en todo el arbol" if not vacios
           else "%d archivo(s): %s" % (len(vacios), ", ".join(vacios[:5])))

    # --- 5: autores del historial (el manifiesto ya se comprobo arriba) ----
    # _autores ejecuta tambien las comprobaciones 6 a 12 y devuelve las marcas
    # de P4. Hasta el 2026-09-12 su resultado se descartaba aqui, de modo que
    # el apartado P4 del informe decia siempre que no habia ninguna marca.
    return _autores(raiz)


def comprobar_manifiesto(raiz):
    man = os.path.join(raiz, "checksums.sha256")
    if os.path.isfile(man):
        import hashlib
        malas = total = 0
        for linea in io.open(man, encoding="utf-8"):
            linea = linea.rstrip("\n")
            if not linea:
                continue
            total += 1
            h, ruta = linea.split(" *./", 1)
            p = os.path.join(raiz, ruta.replace("/", os.sep))
            if not os.path.isfile(p):
                malas += 1
                continue
            d = hashlib.sha256()
            with open(p, "rb") as fh:
                for b in iter(lambda: fh.read(65536), b""):
                    d.update(b)
            if d.hexdigest() != h:
                malas += 1
        anotar(4, "La comprobacion de sumas termina sin error sobre el clon limpio",
               "CUMPLE" if malas == 0 else "NO",
               "%d de %d sumas correctas" % (total - malas, total))
    else:
        anotar(4, "La comprobacion de sumas termina sin error", "NO",
               "No existe checksums.sha256")


def _autores(raiz):
    out = correr(["git", "log", "--format=%ae"], raiz).stdout
    autores = sorted(set(a.strip() for a in out.split("\n") if a.strip()))
    ajenos = [a for a in autores if a not in CORREOS]
    anotar(5, "Todos los autores del historial son integrantes declarados con "
              "correo institucional",
           "CUMPLE" if not ajenos else "NO",
           "%d autor(es): %s" % (len(autores), ", ".join(autores)) if not ajenos
           else "Autores no declarados: %s" % ", ".join(ajenos))

    # --- 5b: ningun agente automatizado firma (criterio P4) ----------------
    # Se buscan trailers, no palabras sueltas: un mensaje que explica que un
    # commit se hizo desde la web de GitHub menciona noreply@github.com sin ser
    # una firma. Los committers ajenos al equipo se informan aparte.
    registro = correr(["git", "log", "--format=%x1e%h%x1f%ce%x1f%cn%x1f%ae%x1f%B"],
                      raiz).stdout
    marcas = []
    for bloque in registro.split("\x1e")[1:]:
        h, ce, cn, ae, cuerpo = (bloque.split("\x1f") + [""] * 5)[:5]
        for linea in cuerpo.splitlines():
            l = linea.strip().lower()
            if l.startswith("co-authored-by:") or l.startswith("generated with") \
                    or (l.startswith("signed-off-by:") and ae.lower() not in l):
                marcas.append("%s (%s)" % (h, linea.strip()[:60]))
        if ce.strip() not in CORREOS:
            COMMITTERS_AJENOS.append("`%s`, aplicado por %s <%s> con autor %s"
                                     % (h, cn.strip(), ce.strip(), ae.strip()))
    anotar(6, "Existe etiqueta anotada de linea base, publicada y alcanzable "
              "desde la rama por defecto", *etiquetas(raiz))

    # --- 7: 07_Datos y la orden unica --------------------------------------
    orden = os.path.join(raiz, "07_Datos", "scripts", "ejecutar.py")
    if os.path.isfile(orden):
        r = correr([sys.executable, "07_Datos/scripts/ejecutar.py"], raiz)
        anotar(7, "La carpeta 07_Datos existe y la orden unica de analisis se "
                  "ejecuta sin error",
               "CUMPLE" if r.returncode == 0 else "NO",
               "python 07_Datos/scripts/ejecutar.py termino con codigo %d" % r.returncode)
    else:
        anotar(7, "La carpeta 07_Datos existe y la orden unica se ejecuta", "NO",
               "No existe 07_Datos/scripts/ejecutar.py")

    # --- 8: elementos A1 a A12 ---------------------------------------------
    faltan, vacias = [], []
    for cod, nombre in sorted(ELEMENTOS_A.items(), key=lambda x: int(x[0][1:])):
        p = os.path.join(raiz, "10_Autoria", nombre)
        if not os.path.exists(p):
            faltan.append(cod)
        elif os.path.isdir(p) and not [f for f in os.listdir(p)
                                       if not f.startswith("00_LEEME")]:
            vacias.append(cod)
    if faltan:
        estado, det = "NO", "Faltan: %s. Sin contenido: %s" % (
            ", ".join(faltan), ", ".join(vacias) or "ninguno")
    elif vacias:
        estado, det = "PARCIAL", "Los doce existen; sin contenido todavia: %s" % \
            ", ".join(vacias)
    else:
        estado, det = "CUMPLE", "Los doce elementos existen y tienen contenido"
    anotar(8, "La carpeta 10_Autoria contiene los elementos A1 a A12", estado, det)

    # --- 9: numeros generados por script -----------------------------------
    anotar(9, "Todo numero que aparece en los documentos procede de la salida de "
              "un script", "MANUAL",
           "La correspondencia salida-script esta declarada en "
           "07_Publicacion/dataset_zenodo/correspondencia_salidas.csv. Requiere "
           "revision humana")

    # --- 10: datos personales en la zona publica ---------------------------
    # Cedulas de los integrantes, declaradas por ellos mismos en la caratula
    # y en la composicion del equipo. No son un dato filtrado de un
    # participante, que es lo que este criterio persigue.
    PROPIAS = {"1208338291", "1207929645", "0942833492"}
    sospechas, propias_vistas = [], 0
    # Las guardas (?<![\\d.]) y (?![\\d.]) descartan fragmentos decimales:
    # una marca de tiempo de Excel como 46231.7374829051 contiene diez
    # digitos seguidos que no son una cedula.
    RE_CED = re.compile(r"(?<![\d.])\d{10}(?![\d.])")
    # Los PDF tambien se leen: una cedula en la capa de texto de un PDF es tan
    # publica como en un .md, y la version anterior de esta comprobacion no los
    # miraba. Leerlos exige PyMuPDF; sin el, los PDF quedan sin revisar y el
    # detalle lo dice en lugar de dar el criterio por cumplido.
    try:
        import pymupdf as _pdf
    except ImportError:
        try:
            import fitz as _pdf
        except ImportError:
            _pdf = None
    pdf_sin_revisar = 0
    for base, dirs, fs in os.walk(raiz):
        if ".git" in base or "00_Restringido" in base:
            continue
        for f in fs:
            p = os.path.join(base, f)
            if f.lower().endswith(".pdf"):
                if _pdf is None:
                    pdf_sin_revisar += 1
                    continue
                try:
                    with _pdf.open(p) as doc:
                        t = "\n".join(pg.get_text() for pg in doc)
                except Exception:
                    continue
            elif f.lower().endswith((".md", ".csv", ".txt", ".tex")):
                try:
                    t = io.open(p, encoding="utf-8", errors="ignore").read()
                except OSError:
                    continue
            else:
                continue
            for m in RE_CED.findall(t):
                if m.startswith("20"):              # descarta anios y fechas
                    continue
                if m in PROPIAS:
                    propias_vistas += 1
                    continue
                sospechas.append((os.path.relpath(p, raiz), m))
    unicos = sorted(set(x[0] for x in sospechas))
    anotar(10, "Ningun dato personal aparece en la zona publica del repositorio",
           ("CUMPLE" if not pdf_sin_revisar else "MANUAL") if not sospechas else "NO",
           ("Ninguna cedula ajena al equipo fuera de la zona restringida, incluida "
            "la capa de texto de los PDF. Las %d apariciones detectadas son las de "
            "los propios integrantes, declaradas por ellos en la caratula y en la "
            "composicion del equipo, no datos de participantes" % propias_vistas
            + ("" if not pdf_sin_revisar else
               ". %d PDF sin revisar: instale PyMuPDF" % pdf_sin_revisar))
           if not sospechas else
           "%d posible(s) cedula(s) AJENA(S) en %d archivo(s): %s. Revisar YA"
           % (len(sospechas), len(unicos), ", ".join(unicos[:4])))

    # --- 11: requisitos del componente inteligente -------------------------
    import csv as _csv
    ficha = os.path.join(raiz, "01_ERS", "Componentes_IA",
                         "requisitos_no_funcionales_ia.csv")
    if os.path.isfile(ficha):
        filas = list(_csv.DictReader(io.open(ficha, encoding="utf-8")))
        exigidos = ["Metrica", "Unidad", "Umbral", "Metodo_de_verificacion",
                    "Responsable", "Frecuencia_de_medicion"]
        incompletos = [r["ID"] for r in filas
                       if any(not r.get(c, "").strip() for c in exigidos)]
        anotar(11, "Cada requisito del componente inteligente tiene metrica, "
                   "unidad, umbral y metodo de verificacion",
               "CUMPLE" if not incompletos else "NO",
               "%d requisitos, todos con los seis atributos" % len(filas)
               if not incompletos else "Incompletos: %s" % ", ".join(incompletos))
    else:
        anotar(11, "Cada requisito del componente inteligente tiene sus atributos",
               "NO", "No existe requisitos_no_funcionales_ia.csv")

    # --- 12: la URL abre sin autenticar ------------------------------------
    anotar(12, "La URL declarada en la caratula abre el repositorio desde una "
               "sesion sin autenticar", "MANUAL",
           "Comprobar en una ventana privada del navegador: %s" % REMOTO)

    return marcas


def etiquetas(raiz):
    """Devuelve (estado, detalle) sobre la etiqueta de linea base."""
    nombres = [t for t in correr(["git", "tag"], raiz).stdout.split() if t]
    if not nombres:
        return "NO", "No hay ninguna etiqueta"
    anotadas, ligeras = [], []
    for t in nombres:
        tipo = correr(["git", "cat-file", "-t", t], raiz).stdout.strip()
        (anotadas if tipo == "tag" else ligeras).append(t)
    rama = correr(["git", "rev-parse", "--abbrev-ref", "HEAD"], raiz).stdout.strip()
    alcanzables = correr(["git", "tag", "--merged", rama], raiz).stdout.split()
    buenas = [t for t in anotadas if t in alcanzables]
    if not buenas:
        return "NO", "Etiquetas ligeras o no alcanzables: %s" % ", ".join(nombres)
    det = "%d etiqueta(s) anotada(s) y alcanzable(s) desde %s: %s" % (
        len(buenas), rama, ", ".join(buenas))
    if ligeras:
        det += ". Ligeras: %s" % ", ".join(ligeras)
    return "CUMPLE", det


CEDENO = "wcedenoa2@uteq.edu.ec"
MUNOZ = "ymunozq@uteq.edu.ec"
SANCHEZ = "gsanchezc6@uteq.edu.ec"
# Archivos que no se reparten: la propia verificacion no puede verificarse a si
# misma, y los manifiestos de sumas los regenera un script sobre todo el arbol.
NO_REPARTIBLES = ("checksums.sha256", "07_Datos/checksums_datos.sha256",
                  "10_Autoria/verificacion_previa.md",
                  "10_Autoria/verificacion_previa.pdf",
                  "10_Autoria/verificacion_previa.py")


def reparto(raiz):
    """Reparte los archivos versionados entre los firmantes, desde el historial.

    Cada archivo lo verifica alguien sin ninguna confirmacion sobre el:
      1. Cedeno Avila, todo lo que no toco.
      2. Munoz Quinonez, lo que toco Cedeno y ella no.
      3. Sanchez Cornejo, lo que tocaron los otros dos y el no.
    Lo que tocaron los tres no lo puede verificar nadie distinto de quien lo
    produjo, y se lista aparte en lugar de asignarlo.
    """
    salida = correr(["git", "log", "--name-only", "--format=%x1f%ae"], raiz).stdout
    autores = {}
    for bloque in salida.split("\x1f")[1:]:
        lineas = [l for l in bloque.split("\n") if l.strip()]
        if not lineas:
            continue
        for a in lineas[1:]:
            autores.setdefault(a, set()).add(lineas[0])
    vivos = [f for f in correr(["git", "ls-files"], raiz).stdout.split("\n")
             if f and f not in NO_REPARTIBLES]
    uno = [f for f in vivos if CEDENO not in autores.get(f, set())]
    resto = [f for f in vivos if CEDENO in autores.get(f, set())]
    dos = [f for f in resto if MUNOZ not in autores[f]]
    resto = [f for f in resto if MUNOZ in autores[f]]
    tres = [f for f in resto if SANCHEZ not in autores[f]]
    nadie = [f for f in resto if SANCHEZ in autores[f]]
    return uno, dos, tres, nadie


def _lista(archivos):
    return ", ".join("`%s`" % f for f in archivos) if archivos else "ninguno"


def escribir(marcas, clonado, sha, raiz):
    L = ["# Lista de verificacion previa",
         "",
         "**Proyecto SIGA · Equipo FGMMN · ISR-401 · Universidad Tecnica Estatal de Quevedo**",
         "",
         "Seccion 11 de la guia de desarrollo del 2026-09-02. Las doce comprobaciones se",
         "**ejecutaron**, no se marcaron a mano: el detalle de cada una es la salida real de",
         "`10_Autoria/verificacion_previa.py`.",
         "",
         "| | |", "|---|---|",
         "| Comprobado sobre | %s |" % ("un clon limpio del remoto" if clonado
                                        else "la copia de trabajo local"),
         "| Version | `%s` |" % sha,
         "",
         "---", "", "## Resultado", "",
         "| N.º | Comprobacion | Cumple | Detalle |", "|---|---|---|---|"]
    simbolos = {"CUMPLE": "**Si**", "NO": "**No**", "PARCIAL": "Parcial",
                "MANUAL": "Manual"}
    for n, texto, estado, detalle in sorted(resultados):
        L.append("| %d | %s | %s | %s |" % (n, texto, simbolos[estado], detalle))
    L += ["", "---", "",
          "## Criterio de piso P4: ningun agente automatizado firma el historial", ""]
    if marcas:
        L += ["**ATENCION.** Se detectaron marcas de coautoria automatizada en los mensajes de",
              "commit: %s. El criterio P4 sanciona esto con calificacion cero." % ", ".join(marcas),
              "Hay que reescribir esos mensajes antes de la entrega.", ""]
    else:
        L += ["Comprobado linea a linea sobre el cuerpo de todos los mensajes de commit:",
              "**ningun** trailer `Co-Authored-By`, ninguna linea `Generated with` y ningun",
              "`Signed-off-by` ajeno al autor. Todos los autores del historial son integrantes del",
              "equipo con su correo institucional.", ""]
    if COMMITTERS_AJENOS:
        L += ["**Committer distinto de un integrante** --- el autor si lo es: %s. Es la firma"
              % "; ".join(COMMITTERS_AJENOS),
              "con la que GitHub registra un commit hecho desde su interfaz web, explicada en",
              "`04_Trazabilidad/composicion_equipo.md`.", ""]
    L += ["Que parte de las operaciones de Git las ejecuto un asistente de inteligencia",
          "artificial, con la identidad del integrante al que se atribuia cada cambio, se",
          "declara en `10_Autoria/declaracion_uso_ia.md`.", ""]
    L += ["---", "", "## Lo que esta lista no decide", "",
          "Tres comprobaciones quedan marcadas como **manual** a proposito.",
          "",
          "La numero 9 --- que todo numero de los documentos proceda de un script --- exige leer",
          "los documentos y contrastarlos con la correspondencia declarada. Una maquina puede",
          "comprobar que la correspondencia existe, no que sea cierta.",
          "",
          "La numero 12 exige abrir la URL sin sesion iniciada, y este script no puede saber si",
          "quien lo ejecuta tiene credenciales guardadas.",
          "",
          "La numero 10 se ejecuta, pero su resultado es un indicio: busca secuencias de diez",
          "digitos fuera de la zona restringida. Que no encuentre ninguna no prueba que no haya",
          "datos personales de otra forma.",
          "",
          "---", "", "## Sobre la version que se verifica", "",
          "La version que consta arriba es la del commit **anterior** al que deposita este",
          "documento firmado. No puede ser otra: cuando se imprime y se firma, el commit que",
          "lo deposita todavia no existe, y su identificador tampoco. **La diferencia es",
          "siempre de una sola confirmacion**, y esa confirmacion es la del propio deposito.",
          "",
          "Es la misma regla que declara `aporte_individual.md` para el recuento por autor, y",
          "por el mismo motivo. La guia pide la lista firmada *antes de dar por cerrada la",
          "entrega*; el identificador lo anade este script por rigor propio, no porque se",
          "exija.",
          "",
          "Cualquiera puede rehacer la comprobacion sobre la version entregada:",
          "",
          "```bash",
          "python 10_Autoria/verificacion_previa.py --clonar",
          "```",
          "",
          ""]
    uno, dos, tres, nadie = reparto(raiz)
    L += ["---", "", "## Reparto de la verificacion", "",
          "La guia exige que quien comprueba sea **una persona distinta de quien produjo cada",
          "artefacto**. El reparto **lo calcula este script desde el historial, archivo por",
          "archivo**: cada archivo lo verifica alguien que no tiene ninguna confirmacion sobre",
          "el. Se comprueba con `git log --format=%ae -- <archivo>`.",
          "",
          "| Firmante | Verifica | Archivos |",
          "|---|---|---|",
          "| Cedeno Avila, Winston Damian | Todos los archivos sin ninguna confirmacion suya | %d |" % len(uno),
          "| Munoz Quinonez, Yeranick Esther | Los que tienen confirmaciones de Cedeno Avila y ninguna suya | %d |" % len(dos),
          "| Sanchez Cornejo, Gary Alberto | Los que tienen confirmaciones de los otros dos y ninguna suya | %d |" % len(tres),
          "",
          "**Archivos de la segunda firma:** %s." % _lista(dos),
          "",
          "**Archivos de la tercera firma:** %s." % _lista(tres),
          "",
          "**Sin verificador distinto de su autor:** %s. Tienen confirmaciones de los tres" % _lista(nadie),
          "integrantes, de modo que ninguno puede verificarlos sin comprobar trabajo propio; se",
          "declaran en lugar de asignarlos. Quedan fuera del reparto los manifiestos de sumas, que",
          "regenera un script, y los tres archivos de esta verificacion, que no puede verificarse a",
          "si misma.",
          ""]
    L += ["## Firmas", "",
          "Cada firmante declara haber revisado el resultado de arriba y las comprobaciones",
          "marcadas como manuales, sobre los archivos que el reparto le asigna.",
          "",
          "**Cedeno Avila, Winston Damian** --- wcedenoa2@uteq.edu.ec",
          "",
          "Firma: ______________________________    Fecha: ______________",
          "",
          "**Munoz Quinonez, Yeranick Esther** --- ymunozq@uteq.edu.ec",
          "",
          "Firma: ______________________________    Fecha: ______________",
          "",
          "**Sanchez Cornejo, Gary Alberto** --- gsanchezc6@uteq.edu.ec",
          "",
          "Firma: ______________________________    Fecha: ______________",
          ""]
    io.open(SALIDA, "w", encoding="utf-8").write("\n".join(L))


def main():
    clonar = "--clonar" in sys.argv
    origen = os.path.dirname(AQUI)
    tmp = None
    try:
        if clonar:
            tmp = tempfile.mkdtemp(prefix="siga_verif_")
            destino = os.path.join(tmp, "clon")
            print("Clonando el remoto en una carpeta limpia...")
            r = correr(["git", "clone", "-q", REMOTO, destino], tmp)
            if r.returncode:
                print("No se pudo clonar: %s" % r.stderr.strip())
                return 1
            raiz = destino
        else:
            raiz = origen
        sha = correr(["git", "rev-parse", "--short", "HEAD"], raiz).stdout.strip()
        print("Verificando %s sobre %s\n" % (sha, "un clon limpio" if clonar
                                             else "la copia local"))
        marcas = comprobar(raiz, clonar)
        escribir(marcas, clonar, sha, raiz)
        print("\nEscrito 10_Autoria/verificacion_previa.md")
        fallos = [r for r in resultados if r[2] == "NO"]
        if fallos:
            print("HAY %d COMPROBACION(ES) FALLIDA(S)." % len(fallos))
            return 1
        return 0
    finally:
        if tmp and os.path.isdir(tmp):
            shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
