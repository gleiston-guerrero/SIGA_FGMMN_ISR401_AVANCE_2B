# Evidencia de autoria y de trabajo propio

**Proyecto SIGA · Equipo FGMMN · ISR-401 · Universidad Tecnica Estatal de Quevedo**

Carpeta exigida por la seccion 6 de la guia de desarrollo emitida el 2026-09-02. Su
finalidad es que quede acreditado, de forma verificable, que los artefactos entregados
fueron producidos por las personas que los firman. La guia lo dice sin rodeos: **la ausencia
de esta evidencia no se suple con una declaracion.**

Este README declara el estado real de cada elemento. **Los doce estan depositados.**

---

## Estado de los doce elementos

| Cod. | Elemento | Estado | Que contiene |
|---|---|---|---|
| A1 | `bitacora_sesiones.csv` | **Depositado** | 24 filas, del 2026-08-30 al 2026-09-12. Derivado del historial por `generar_bitacora.py`: una por persona y dia con confirmaciones. Ningun campo se escribe a mano |
| A2 | `capturas/` | **Depositado. 3 de 3 por integrante** | Nueve capturas, tres por persona, cada una en su propia maquina. En todas se ven el archivo del proyecto abierto, el reloj del sistema y la sesion de usuario |
| A3 | Fuentes editables | **Depositado** | En el propio arbol, junto a cada imagen exportada. Inventario de 44 fuentes en `fuentes_editables.md` |
| A4 | `grabaciones/` | **Depositado** | Dos sesiones de trabajo de 15:18 y 15:43 con pantalla compartida y discusion audible, mas 18 capturas tomadas durante ellas |
| A5 | `notas_campo/` | **Depositado** | Las seis de la ronda terminal, manuscritas y escaneadas, con fecha, hora de inicio y fin, duracion y codigo de participante. Sin nombres propios |
| A6 | `fotos_equipo/` | **Depositado** | Dos fotografias en la facultad, con dos integrantes identificables. Se depositan tal como salieron del telefono: los metadatos son la evidencia y cualquier reedicion los altera |
| A7 | `doble_codificacion/` | **Depositado** | Las dos hojas de codificacion independientes sobre los mismos 39 fragmentos, el script del acuerdo y sus resultados. Kappa de Cohen **0,548** para el codigo y **0,911** para la categoria, con intervalo por bootstrap |
| A8 | `correspondencia/` | **Depositado** | Tres capturas de la coordinacion de la ronda terminal y la consulta al docente sobre las firmas de A10 con su respuesta. Datos de terceros censurados |
| A9 | `declaracion_uso_ia.md` | **Depositado** | Por seccion, incluidas aquellas en las que no se empleo ninguna herramienta |
| A10 | `aporte_individual.md` · `.pdf` | **Depositado y firmado** | Generado desde el historial por `04_Trazabilidad/generar_aporte_individual.py`. Regenerado el 2026-09-12 sobre el historial hasta `3530bb2` y **firmado por los tres integrantes acreditados ese mismo dia**; sustituye al firmado el 2026-09-04 |
| A11 | `exif_inventario.csv` | **Depositado** | Las dos fotografias de A6 con su fecha de captura leida de los metadatos, el dispositivo y el hash. Las dos conservan la fecha |
| A12 | `.mailmap` | **Depositado** | En la raiz del repositorio, que es donde Git lo lee |

## Sobre las firmas de A10

El elemento pide el documento **«firmado por los cinco»**. Este equipo son tres: de los cinco
nombres del grupo del SGA, **Mendoza Palma, Allan Jeremy** y **Gilces Carranza, Jose Ignacio**
estan retirados del equipo y no produjeron ningun artefacto. Se consulto por escrito al docente responsable, que respondio el 2026-09-04:
**«No debe aparecer nadie mas en el documento.»**

La consulta y la respuesta constan en
[`correspondencia/2026-09-04_Consulta_firmas_aporte_individual.png`](correspondencia/2026-09-04_Consulta_firmas_aporte_individual.png).
El documento lo firman los tres integrantes acreditados y no nombra a nadie mas.

## Sobre la lista de verificacion previa

[`verificacion_previa.pdf`](verificacion_previa.pdf) recoge las doce comprobaciones de la
seccion 11 de la guia, **ejecutadas sobre un clon limpio del remoto**, no marcadas a mano:
el detalle de cada una es la salida real de `verificacion_previa.py`.

Va firmada por **los tres integrantes** el 2026-09-12, sobre el clon limpio de `3530bb2`. La
guia exige que quien comprueba sea una persona distinta de quien produjo cada artefacto, y
con un solo firmante eso no se puede cumplir sobre el arbol entero. El reparto **lo calcula
el script desde el historial, archivo por archivo**: Cedeno Avila verifica lo que no toco,
Munoz Quinonez lo que toco el y ella no, y Sanchez Cornejo lo que tocaron los otros dos y el
no. Los dos archivos que tocaron los tres se declaran en el documento como sin verificador
distinto de su autor.

## Que no hay aqui

Ninguna carpeta se relleno con marcadores de posicion en ningun momento. El criterio de piso
P3 sanciona con cero cualquier archivo que anuncie una pieza de evidencia y no la contenga;
mientras un material no existia, la tabla de arriba lo declaraba faltante en lugar de crear
un archivo vacio con su nombre.

## Como comprobarlo

```bash
python 10_Autoria/verificacion_previa.py --clonar
```

Clona el remoto en una carpeta limpia y ejecuta las doce comprobaciones, incluida la de que
los doce elementos existen y tienen contenido.
