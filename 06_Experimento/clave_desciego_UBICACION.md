# Donde esta la tabla de desciego, y quien la custodia

**Proyecto SIGA · Equipo FGMMN · ISR-401 · Universidad Tecnica Estatal de Quevedo**
Nota depositada el 2026-09-03, en cumplimiento de la guia de desarrollo del 2026-09-02.

---

## 1. Que archivo se retiro

`06_Experimento/clave_desciego_items.csv` — la **tabla de desciego** del cuasi-experimento.
51 filas y tres columnas: `Item_ciego`, `Origen` y `Codigo_real`. Es lo que permite saber,
despues de puntuar, que requisito real habia detras de cada item ciego.

Estuvo publicado en este repositorio hasta el 2026-09-03.

## 2. Por que se retiro

La guia de desarrollo emitida por el docente el 2026-09-02, seccion 4, lo instruye
literalmente:

> «La clave de desciego sigue publicada en el repositorio publico. Retirela del repositorio
> publico y conservela en la zona restringida cifrada. Deje en su lugar una nota que explique
> donde esta y quien la custodia, y mantenga la anotacion de la desviacion.»

Esta nota es esa nota. La anotacion de la desviacion se mantiene, sin editar, en
[`registro_previo/desviacion_clave_desciego.md`](registro_previo/desviacion_clave_desciego.md).

## 3. Donde esta ahora

En el **contenedor cifrado con AES-256 y nombres de archivo ocultos** que es la zona
restringida del proyecto. Desde el 2026-09-06 ese contenedor esta **en este mismo
repositorio**, partido en 316 fragmentos desde su regeneracion del 2026-09-08 (272 hasta
entonces): se abre desde
[`../02_Evidencias/00_Restringido/contenedor/SIGA_zona_restringida.7z.001`](../02_Evidencias/00_Restringido/contenedor/SIGA_zona_restringida.7z.001)
y su descripcion completa esta en
[`../02_Evidencias/00_Restringido/README_Restringido.md`](../02_Evidencias/00_Restringido/README_Restringido.md).

Que este dentro del repositorio **no lo hace publico**: sigue cifrado y sin la contrasena no
se lee nada, ni siquiera los nombres de los archivos. Lo que cambia es que ya no depende de
que un enlace externo siga vivo el dia que alguien quiera comprobarlo.

La contrasena se entrega al docente responsable por el Sistema de Gestion Academica. No se
transmite por ningun otro medio y no consta en este repositorio.

| | |
|---|---|
| **Custodia** | Sanchez Cornejo, Gary Alberto — gsanchezc6@uteq.edu.ec |
| **Nombre en el contenedor** | `clave_desciego_items.csv` |
| **SHA-256 del archivo retirado** | `f5e2f13154d3446cb6f358c5783c5b0a6191af5cc6466d35612555b072e578c7` |
| **Fecha de retirada** | 2026-09-03 |

La suma se publica a proposito: permite comprobar que el archivo entregado al docente es
exactamente el que estuvo en el repositorio, sin ninguna alteracion posterior.

## 4. Como sigue corriendo el analisis sin ella

Retirar la tabla completa habria roto la cadena de replicacion, porque la etapa de
consolidacion necesita saber a que brazo pertenece cada item. Eso se resolvio separando las
dos cosas que la tabla mezclaba:

| | Contiene | Donde esta |
|---|---|---|
| **Brazo del experimento** | `Item_ciego` → `Humano` o `LLM` | Publicado, en [`../07_Datos/datos_crudos/asignacion_brazo_items.csv`](../07_Datos/datos_crudos/asignacion_brazo_items.csv) |
| **Desciego propiamente dicho** | `Item_ciego` → `RF-nn` o `RFA-nn` | Solo en el contenedor cifrado |

El brazo es la **condicion experimental**: sin el no hay analisis posible, y publicarlo no
desciega nada, porque no dice que requisito era. La correspondencia con el codigo real del
requisito es lo unico que permite reidentificar el item, y es lo que sale del repositorio.

Con esa separacion, `python 07_Datos/scripts/ejecutar.py` sigue reconstruyendo el paquete
completo desde los datos crudos en una sola orden, sobre un clon limpio.

## 5. Que hay que hacer con `06_Experimento/scripts_analisis`

El script `analizar_resultados.py` acepta la ruta de la tabla por el parametro `--clave` y
apunta por omision al archivo retirado. Quien tenga acceso al contenedor puede reproducir la
cadena original pasando la ruta local:

```
python 06_Experimento/scripts_analisis/analizar_resultados.py \
    --etapa consolidar --clave /ruta/local/clave_desciego_items.csv
```

Sin acceso al contenedor, la ruta reproducible es la del paquete de datos, que no necesita
la tabla.
