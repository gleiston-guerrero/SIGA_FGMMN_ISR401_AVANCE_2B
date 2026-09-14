# Desviacion del protocolo — publicacion de la clave de desciego

**Proyecto SIGA · Equipo FGMMN · ISR-401 · Universidad Tecnica Estatal de Quevedo**
Registrada el 2026-08-31, a raiz de la revision docente de la Entrega Final (2B).

---

## 1. Que archivo es

`06_Experimento/clave_desciego_items.csv` es la **tabla de desciego** del cuasi-experimento.
Contiene 51 filas y tres columnas:

| Columna | Contenido |
|---|---|
| `Item_ciego` | Identificador que vieron los jueces: `Item-01` a `Item-51` |
| `Origen` | Brazo del experimento: `Humano` o `LLM` |
| `Codigo_real` | Identificador real del requisito, `RF-nn` o `RFA-nn` |

Es lo que permite saber, despues de puntuar, a que brazo pertenecia cada item.

## 2. Que observo el docente

> «En `07_Datos/datos_crudos` publicaron el archivo
> `CLAVE_RESPUESTAS_no_compartir_con_jueces.csv`. El propio nombre dice que no debe
> compartirse con los jueces, y esta en un repositorio publico. Retirenlo y documenten la
> desviacion.»

La observacion es correcta y el equipo la asume. **El nombre del archivo afirmaba una
restriccion que el repositorio no cumplia.**

## 3. Por que el archivo no se puede simplemente retirar

El script `06_Experimento/scripts_analisis/analizar_resultados.py` lo lee en su etapa `consolidar`
(linea 94) para asignar el campo `origen` a cada puntuacion. **Sin esta tabla, el paquete
de replicacion no corre de principio a fin**, y eso incumple el contenido minimo exigible
del paquete de replicacion ejecutable y el criterio de piso sobre regeneracion de tablas y
figuras desde los datos crudos.

Un tercero que quiera reproducir el analisis necesita esta tabla. Es un artefacto de
replicacion, no un dato que deba permanecer oculto una vez concluida la recoleccion.

## 4. Lo que se corrigio

| | Antes | Ahora |
|---|---|---|
| Ruta | `07_Datos/datos_crudos/` | `06_Experimento/` |
| Nombre | `CLAVE_RESPUESTAS_no_compartir_con_jueces.csv` | `clave_desciego_items.csv` |

**Por que cambia de carpeta.** No es un dato crudo de campo: es un artefacto del **diseno
experimental**, y su sitio esta junto al protocolo, las consignas y los instrumentos. De
hecho es donde residia en el repositorio de la Entrega 3 (2A), en
`06_Experimento/CLAVE_RESPUESTAS_no_compartir_con_jueces.csv`; se desplazo a
`datos_crudos/` al reconstruir el arbol para la 2B, y ese desplazamiento fue el error.

**Por que cambia de nombre.** El nombre anterior describia una regla operativa del momento
de la puntuacion —no entregar la clave a los jueces— y la convertia, al publicarse, en una
afirmacion falsa sobre el estado del repositorio. El nombre nuevo dice lo que el archivo
es.

**Lo que no cambia.** El contenido es identico, byte a byte. No se ha alterado ninguna
asignacion de origen.

## 5. Amenaza a la validez, declarada

La pregunta que importa no es donde esta el archivo hoy, sino **si algun juez pudo verlo
antes de puntuar**. El diseno era de evaluacion ciega: los tres jueces recibieron
unicamente los items con su identificador ciego.

Lo que consta:

| Hecho | Fecha |
|---|---|
| Puntuaciones de los tres jueces registradas | 2026-08-02 |
| Creacion de este repositorio (2B) | 2026-08-29 |
| Primer commit que incluye la clave en este repositorio | `bc8426a`, 2026-08-30 |

En **este** repositorio la clave se publico veintiocho dias despues de que los jueces
puntuaran, de modo que su publicacion aqui no pudo afectar al cegado.

### Comprobacion realizada el 2026-08-31

El equipo se comprometio a verificar en el historial del repositorio 2A la fecha en que la
clave se publico alli, y a declarar el resultado fuera cual fuera. Hecha la comprobacion,
esta es la cronologia de ese dia, en UTC:

| Hora UTC | Commit | Que ocurrio |
|---|---|---|
| **19:20** | `dbba6b4` | Entran al repositorio, **en el mismo commit**, la clave de desciego, el paquete de evaluacion ciega y la rubrica |
| **19:40** | `4d678bf` | Se commitean las puntuaciones de los tres jueces |
| **20:00** | `59d1574` | Se arma el conjunto de datos anonimizado |
| **20:25:07** | — | Se crea el registro en OSF |
| **20:40** | `bb04d43` | Se completa el conjunto de datos anonimizado |

Se reproduce con:

```bash
git clone https://github.com/gleiston-guerrero/SIGA_FGMMN_ISR401_AVANCE_2A
cd SIGA_FGMMN_ISR401_AVANCE_2A
TZ=UTC git log --diff-filter=A --date=iso-local \
  --format='%ad  %h  %s' -- "*CLAVE*" "*juez*" "*Paquete_Evaluacion*"
```

### Lectura del resultado

**La clave se publico 20 minutos antes de que se subieran las puntuaciones.** Tomado
aisladamente, el dato es incomodo. Dos hechos lo resuelven.

**Primero: la evaluacion no cabe en veinte minutos.** Tres jueces puntuaron 51 items en 5
dimensiones cada uno, es decir **765 valoraciones**. Producirlas entre las 19:20 y las
19:40 es materialmente imposible. La evaluacion ocurrio necesariamente antes de que la
clave estuviera publicada.

**Segundo: el repositorio no fue el canal de los jueces.** El paquete de evaluacion ciega
entro al repositorio en ese mismo commit de las 19:20, es decir que hasta ese momento no
estaba publicado alli. Si los jueces ya habian puntuado, recibieron el instrumento por otra
via, y no por el repositorio. El commit que lo introduce se titula «restaurar carpetas
obligatorias con su contenido real»: es una reorganizacion del arbol, no la creacion del
material.

**Conclusion que el equipo sostiene.** El cegado del experimento **se mantuvo**. La
publicacion de la clave fue posterior a la evaluacion, y el repositorio no fue el medio por
el que los jueces accedieron al instrumento. La desviacion es de organizacion documental:
un artefacto de diseno quedo en una carpeta que no le correspondia, con un nombre que
afirmaba una restriccion que el repositorio no cumplia.

**Lo que sigue sin poder probarse.** No existe registro de la hora exacta en que cada juez
emitio sus puntuaciones, porque se recogieron fuera del repositorio. El argumento anterior
es de imposibilidad material y de canal, no un registro directo. Se declara asi.

## 6. Lo que si esta probado: el material que recibieron los jueces no filtra el origen

Esto es comprobable hoy, sobre el propio repositorio.
`06_Experimento/instrumentos/Paquete_Evaluacion_Ciega_Jueces.md` es el documento que se
entrego a los tres jueces, y contiene:

| Comprobacion | Resultado |
|---|---|
| Items presentados | **51** |
| Menciones de `RF-` o `RFA-` | **0** |
| Menciones de `Humano` o `LLM` | **0** |

Sus instrucciones dicen literalmente que no se indica el origen de cada item y que el orden
fue aleatorizado. La hoja de puntuacion,
`06_Experimento/instrumentos/Hoja_Puntuacion_JUEZ.csv`, tampoco lo incluye.

Es decir: **el instrumento entregado estaba correctamente cegado**. Lo que no esta probado
es que ningun juez consultara por su cuenta el repositorio 2A, y esa es la comprobacion
pendiente de la seccion anterior. Los tres jueces son personas externas al equipo y no
consta que se les entregara la URL del repositorio, pero eso reduce la probabilidad, no la
descarta, y no se presenta como prueba.

## 7. Efecto sobre el analisis

Ninguno sobre las cifras. El traslado y el renombrado no alteran el contenido de la tabla.
Tras el cambio se ejecuto el pipeline completo y las diez salidas —cinco tablas y cuatro
figuras mas la tabla de saturacion— resultaron identicas byte a byte a las anteriores.
