# Registro OSF del protocolo — estado y pendientes

## Registro confirmado

| Campo | Valor |
|---|---|
| **DOI del registro** | [`10.17605/OSF.IO/7PQ3H`](https://doi.org/10.17605/OSF.IO/7PQ3H) |
| Enlace directo | <https://osf.io/7pq3h> |
| Estado | **Aceptado** |
| Protocolo registrado | [`protocolo.pdf`](../protocolo/protocolo.pdf) · fuente en [`protocolo.tex`](../protocolo/protocolo.tex) y [`protocolo.md`](../protocolo/protocolo.md) |

Este DOI es el que debe constar en `CITATION.cff`, en el `README.md` de la raíz, en la
sección *Data and materials availability* del manuscrito y en la descripción del depósito
de Zenodo.

## Estado de los archivos del registro previo

| Archivo | Qué contiene | Estado |
|---|---|---|
| `bitacora_desviaciones.pdf` | Cada desviación del análisis ejecutado respecto del plan pre-registrado. | Presente |
| `desviacion_clave_desciego.md` | Desviación por la publicación de la tabla de desciego. | Presente |
| `osf_registration_api.json` | Respuesta íntegra de la API pública de OSF para este registro, descargada el 2026-08-31. Contiene la marca temporal, el estado del registro y el formulario completo. | **Presente** |
| `osf_internet_archive_bag.zip` | Copia del registro depositada por el Center for Open Science en el Internet Archive, en formato BagIt con sus manifiestos SHA-256 y SHA-512. Incluye el protocolo, la rúbrica y el paquete de evaluación ciega tal como estaban al registrarse. | **Presente** |
| `osf_internet_archive_meta.xml` | Metadatos del ítem del Internet Archive, con su propia fecha de archivo. | **Presente** |
| `osf_contributors_api.json` | Lista de contribuyentes del registro tal como la devuelve la API pública, descargada el 2026-08-31. | **Presente** |
| `osf_registration.pdf` | Exportación en PDF de la página pública del registro, 15 páginas, generada el 2026-08-31. Incluye el DOI, la fecha de registro, los contribuyentes, el enlace al Internet Archive y el formulario completo con sus actualizaciones. | **Presente** |
| `osf_internet_archive.pdf` | Exportación en PDF de la ficha del ítem en el Internet Archive, 6 páginas, con su fecha de archivo. | **Presente** |

## Marca temporal externa — verificada el 2026-08-31

El docente observó en su revisión que no localizaba «comprobante de registro previo con
marca temporal externa». Ahora está en esta carpeta, y no depende de la palabra del equipo:

| Hecho | Fuente | Marca temporal |
|---|---|---|
| Proyecto creado en OSF | `logs.json` del paquete BagIt | 2026-07-27T21:27:28 UTC |
| Subida del protocolo, la rúbrica y el paquete de evaluación ciega | `logs.json`, tres eventos | 2026-08-02T19:59:21 a 19:59:54 UTC |
| **Registro creado y aceptado** | `date_registered` de la API de OSF | **2026-08-02T20:25:07 UTC** |
| **Copia archivada por un tercero** | Internet Archive, `addeddate` | **2026-08-06T13:00:29 UTC** |
| Actualización con las 9 desviaciones | Página pública del registro | 2026-08-27 |
| Re-archivado tras la actualización | Internet Archive, `modified` | 2026-08-28T04:13:35 UTC |

El Internet Archive es un tercero independiente y el depósito lo hizo
`ops-admin@cos.io`, no el equipo. Cualquiera puede comprobarlo en
<https://archive.org/details/osf-registrations-7pq3h-v1> sin credenciales.

**Cómo verificarlo sin fiarse de este documento:**

```bash
curl -s https://api.osf.io/v2/registrations/7pq3h/ | grep -o '"date_registered":"[^"]*"'
curl -s https://archive.org/metadata/osf-registrations-7pq3h-v1 | grep -o '"addeddate":"[^"]*"'
```

## Lo que la marca temporal acredita, y lo que no

**No cumple G9, y conviene decirlo antes que lo diga el tribunal.** El criterio exige que
el protocolo esté registrado con marca temporal **anterior al inicio de la recolección de
datos**. El trabajo de campo se ejecutó entre el **2026-05-14** y el **2026-07-30**, según
las fechas de los diez consentimientos, videos y transcripciones. El registro es del
**2026-08-02**. La recolección precedió al registro en dos meses y medio.

### El registro ya está declarado como retrospectivo en la propia OSF

Esto es lo más relevante del expediente y conviene no perderlo de vista.

El **registro original**, del 2026-08-02, marcó el campo de existencia de datos como

> «Data does not yet exist. No part of the data that will be used for this analysis plan
> exists, and no part will be generated until after this plan is registered.»

La **actualización del 2026-08-27**, anterior a la revisión docente, corrigió ese campo de
forma expresa. Consta en la página pública y en `osf_registration.pdf`, página 3:

> «**Foreknowledge of data or evidence** — *Updated*. Analyses in this plan have been
> conducted already. At least some of the analyses described in this analysis plan have
> been conducted by the authors **making this a retrospective registration**.»

Y añade su justificación:

> «Esta actualización del registro se presenta después de ejecutar el plan de análisis
> pre-registrado y de conocer los resultados, con el único propósito de declarar
> explícitamente las desviaciones detectadas durante esa ejecución. Ninguna de las
> desviaciones al plan de análisis fue decidida después de ver qué resultado produciría
> cada una: las tres hacen el análisis más conservador, no menos, y de hecho ninguna de las
> 5 dimensiones evaluadas resultó significativa una vez aplicadas.»

**Consecuencia.** El equipo no oculta la naturaleza retrospectiva del registro: la declaró
en la fuente, en el propio repositorio de registros, con fecha del 27 de agosto y antes de
entregar. G9 sigue incumplido —un registro retrospectivo no es un pre-registro—, pero la
diferencia entre incumplir y ocultar es exactamente lo que separa una limitación declarada
de una falta de integridad. Esta declaración es verificable por cualquiera sin credenciales
en <https://osf.io/7pq3h>.

**Comprobación realizada el 2026-08-31.** Se verificó en el historial del repositorio 2A
la fecha en que se commitearon las puntuaciones de los jueces, para contrastarla con las
20:25:07 UTC del registro:

| Hora UTC del 2026-08-02 | Hecho |
|---|---|
| 19:40 | Se commitean las puntuaciones de los tres jueces (`4d678bf`) |
| **20:25:07** | **Se crea el registro en OSF** |

Las puntuaciones son **anteriores** al registro, en 45 minutos. Por tanto el componente
empírico **tampoco está pre-registrado**: ni el trabajo de campo, que precede en dos meses
y medio, ni el análisis de los jueces, que precede en tres cuartos de hora.

Esto es coherente con lo que la propia OSF declara desde el 2026-08-27, y no lo contradice:
el registro es **retrospectivo**, y así consta en la fuente. La cronología completa de ese
día, con el detalle de la publicación de la clave de desciego, está en
[`desviacion_clave_desciego.md`](desviacion_clave_desciego.md).

## Lo que el paquete archivado sí demuestra

**El instrumento ciego, con fecha de tercero.** `archived_files.zip` dentro del BagIt
contiene `Paquete_Evaluacion_Ciega_Jueces.md` tal como estaba el 2026-08-02, archivado por
el Internet Archive el 2026-08-06. Ese documento presenta 51 ítems sin una sola mención de
`RF-`, `RFA-`, `Humano` ni `LLM`. Es evidencia externa y fechada de que **el material
entregado a los jueces estaba correctamente cegado**, y sostiene lo declarado en
`desviacion_clave_desciego.md`.

**Participación de integrantes que el docente sitúa en factor cero.** Hay que distinguir
dos fotografías, porque no tienen el mismo valor probatorio.

**Lo que consta en el registro vivo**, comprobado el 2026-09-01 y guardado literalmente en
`osf_contributors_api.json`:

| Contribuyente | Permiso | Bibliografico |
|---|---|---|
| Sanchez Gary | admin | si |
| Yeranick Esther Munoz Quinonez | write | si |

**Eran los dos integrantes del equipo cuando se registro el protocolo.** Desde el
2026-09-02 el equipo activo son tres: Cedeno Avila, Winston Damian se reincorporo, y Mendoza
Palma, Allan Jeremy y Gilces Carranza, Jose Ignacio estan retirados. El registro del protocolo **no se modifica** --alterar un
pre-registro despues de recoger datos es justamente lo que el pre-registro existe para
impedir--; la incorporacion posterior se documenta en `osf_deviations.pdf`.

La declaracion de composicion, con el recuento por autor que la respalda, esta en
`04_Trazabilidad/composicion_equipo.md`.

**Lo que hay que precisar sobre el historial de esta lista.** El protocolo se preregistro
cuando el equipo tenia mas integrantes, y la lista de contribuyentes se actualizo despues
para reflejar la composicion vigente. Lo que el registro congela es **el contenido
registrado** --- preguntas, hipotesis, variables y plan de analisis ---, que es lo que
sostiene la marca temporal frente al p-hacking y al HARKing. La lista de personas asociadas
al registro si admite mantenimiento, y mantenerla al dia es lo correcto.

La copia archivada por el Internet Archive el 2026-08-06, actualizada el 2026-08-28, refleja
la composicion anterior por ser anterior a esa actualizacion. Se conserva sin retocar: es un
deposito de un tercero y su valor esta justamente en que nadie del equipo puede modificarlo.

## Pendiente: el nodo del proyecto declara un solo contribuyente

El registro `7pq3h` deriva del proyecto `3nruf`, y **ese proyecto tiene a Sánchez como
único contribuyente**. Si el tribunal abre el proyecto en lugar del registro, ve a una
sola persona.

Conviene añadir a los otros tres también al proyecto, para que ambos nodos digan lo mismo:
<https://osf.io/3nruf> → *Contributors* → *Add*. Se comprueba después con:

```bash
curl -s "https://api.osf.io/v2/nodes/3nruf/contributors/?embed=users" | grep -o '"full_name":"[^"]*"'
```

## Cómo se generaron los PDF, y cómo rehacerlos

OSF no ofrece un botón de exportación a PDF, y `Ctrl+P` sobre la página produce una sola
página truncada: el maquetado de la aplicación encierra el contenido en un contenedor de
altura fija, de modo que la impresión solo captura lo visible.

Los dos PDF de esta carpeta se generaron con Chrome en modo sin ventana, hablando con el
navegador por el protocolo DevTools, liberando esas alturas antes de imprimir. Es el mismo
motor de impresión que `Ctrl+P`, con el maquetado desbloqueado.

Si hay que rehacerlos, basta con volver a abrir las dos direcciones y comprobar que el PDF
resultante contiene, como el actual:

| Comprobación | `osf_registration.pdf` |
|---|---|
| Páginas | 15 |
| DOI `10.17605/OSF.IO/7PQ3H` | sí |
| Sección *Date Registered* | sí |
| Sección *Contributors* | sí |
| Enlace al Internet Archive | sí |
| Declaración de registro retrospectivo | sí, página 3 |

Direcciones: <https://osf.io/7pq3h> y
<https://archive.org/details/osf-registrations-7pq3h-v1>.
