# Registro de cambios — SIGA (Sistema Inteligente de Gestion de Aulas)

Formato basado en Keep a Changelog. Versionado segun las entregas del Proyecto Fin de
Curso ISR-401, Universidad Tecnica Estatal de Quevedo, periodo 2026–2027.

Cada version registra lo anadido, lo cambiado y lo corregido. Solo se listan artefactos
que existen en el arbol del repositorio en el commit correspondiente.

---

## [2B-1.18.0] - 2026-09-14

Atiende las dos observaciones de la evaluacion de la Entrega Final publicada el 2026-09-14
que quedaban abiertas en los items B4 y B1. No cambia ningun dato crudo, ninguna puntuacion,
ningun valor p ni ninguna conclusion.

### Corregido

- **Tamanos del efecto (B4).** Se calculaban como d de Cohen apareada sobre las tres medias
  por juez, y el bootstrap de tres observaciones daba intervalos sin sentido, como
  [−42,72 ; 0,00] en Consistencia interna. Ahora se calculan con el **requisito como unidad**,
  25 del equipo frente a 26 del modelo: g de Hedges o delta de Cliff con IC 95 % por bootstrap
  estratificado. Los efectos son pequenos, entre −0,117 y −0,257, y todos los intervalos
  cruzan el cero. El contraste apareado preregistrado no cambia. Declarado como desviacion 7
  en `07_Datos/desviaciones.md` y en
  `06_Experimento/registro_previo/desviacion_tamano_efecto.md`.
- `efectos.csv`, `tabla_hipotesis.tex` y `fig03_tamanos_efecto.png` regenerados; apartados de
  magnitud del efecto del reporte y del manuscrito reescritos, con la cuarta desviacion en el
  manuscrito, que sigue en 15 paginas; `AFI-04` y `AFI-05` de `verificar_afirmaciones.py` y
  pregunta D5 del banco de la defensa al dia.
- **`reporte.tex`** mostraba en el PDF «extbf» y «exttt» sueltos en dos parrafos, por un
  tabulador donde debia ir `\t`, y un `**recalculan desde su fuente**` con los asteriscos de
  Markdown; dos rutas se salian del margen.

### Cambiado

- **La cadena de analisis vive en `07_Datos` (B1).** Los seis scripts de analisis estan en
  `07_Datos/scripts/analisis/` y la nueva etapa `analisis` (`etapa5_analisis.py`, que
  sustituye a `etapa5_documento.py`) los ejecuta sobre `07_Datos/datos_crudos/`, sin llamar a
  `06_Experimento`. Se anaden a los datos crudos `codificacion_tematica.csv` y
  `transcripciones_anonimizadas.json`, entradas de la curva de saturacion.
- **El reporte y el manuscrito incluyen sus tablas y figuras desde `07_Datos/resultados/`.**
- `06_Experimento/replicar.py` y su `Makefile` siguen funcionando igual. La etapa
  `integridad` comprueba ahora que los datos crudos, los seis scripts y las 18 salidas son
  identicos byte a byte en los dos sitios.
- `diccionario_datos.csv`, `README_datos.md`, `README.md`, portada del ERS y declaracion de uso
  de IA al dia.

### Linea base

**Quien revise el repositorio debe ir directamente a la etiqueta vigente**:
`git checkout 2B-final-v5.8`. `2B-final-v5.7` (`6be559a`) y todas las anteriores son historicas.

---

## [2B-1.17.1] - 2026-09-13

Revision de consistencia de todo el arbol, carpeta por carpeta, sobre la etiqueta
`2B-final-v5.6`. Corrige textos que se habian quedado atras respecto de la evidencia ya
depositada. No cambia ningun dato, cifra de resultados, requisito ni archivo de evidencia.

### Corregido

- **Metrica de Correccion en `reporte.tex`.** La tabla de metricas de calidad y el parrafo
  del anexo la daban como «no medible, Pendiente», y la auditoria la mide desde el
  2026-09-05: **0,04** (1 defecto residual, `DEF-06`, sobre 25 RF), Cumple, tras `INS-01` y
  `REINS-01`. El reporte sigue en 27 paginas.
- **`01_ERS/Auditoria_Calidad/auditoria_calidad_especificacion.md`.** La cabecera decia
  «Version 1.0» y la version vigente es la 3.0; la seccion 7 conservaba sin aviso la medicion
  inicial. Lleva ahora una nota de estado que remite al resultado vigente de la seccion 8.
- **`02_Evidencias/00_Restringido/README_Restringido.md` y `contenedor/00_LEEME.md`.**
  Seguian anunciando el enlace de OneDrive como copia redundante, con la suma del contenedor
  anterior a su regeneracion del 2026-09-08 (`d225b192…`). El contenedor esta unicamente en
  el repositorio: se retira el enlace y se declara la suma del contenedor vigente
  (`76a78d6b…`). Pasa de 272 a 316 fragmentos, igual que
  `06_Experimento/clave_desciego_UBICACION.md` y la pregunta I9 del banco de la defensa, que
  ademas decia treinta y cuatro piezas donde la ficha tecnica registra treinta y seis.
  `contenedor/00_LEEME.md` precisa que la prueba de extraccion documentada es la del
  contenedor del 2026-09-07.
- **`02_Evidencias/2026-09-03_notas_entrevistas_docentes.md`.** Conservaba los avisos
  «Anonimizacion pendiente» y «consentimiento: pendiente de completar». Se anade el estado:
  el nombre esta censurado en la transcripcion publicada y en las dos de control de calidad, y
  el consentimiento de DOC-05 esta depositado. El texto original se conserva.
- **`08_Defensa/banco_preguntas.md` y `guion.md`.** Decian «diez codificadas, seis pendientes»;
  las dieciseis estan codificadas desde el 2026-09-06 (136 fragmentos, 50 codigos). La
  pregunta I5 se reescribe conforme a la amenaza T4 del manuscrito, y el guion cita la ruta
  real del diagrama de contexto, `03_Modelado/01_Contexto/`.
- `reporte.tex` citaba `09_Defensa/banco_preguntas.md`; la carpeta es `08_Defensa/`.
- **`10_Autoria/declaracion_uso_ia.md` no cuadraba con el registro de la generacion del
  Conjunto A**, depositado el mismo 2026-09-12. El apartado 1 seguia hablando de «la consigna
  literal y sus parametros», que no existieron. El apartado 4 atribuia «el diseno del
  cuasi-experimento y su protocolo» al equipo sin herramienta, y el registro muestra que el
  asistente redacto el primer texto del protocolo, la rubrica, el paquete ciego y el script
  de analisis el 2026-08-02. Se corrigen los dos apartados y se anade el trabajo del 1 y 2 de
  agosto de 2026.
- **La declaracion no nombraba el texto del ERS, `01_ERS/Componentes_IA/` ni el codigo del
  MVP** en ningun apartado, ni con herramienta ni sin ella. Los tres se elaboraron con
  asistencia de Claude y se declaran ahora, con el metodo de validacion que consta en el
  repositorio.

### Linea base

**Quien revise el repositorio debe ir directamente a la etiqueta vigente**:
`git checkout 2B-final-v5.7`. `2B-final-v5.6` (`b082104`) y todas las anteriores son historicas.

---

## [2B-1.17.0] - 2026-09-12

Las tablas y figuras del documento quedan dentro del paquete de datos. Atiende la unica
observacion que mantuvo la ultima revision del docente, sobre el item B1.

### Cambiado

- **La orden unica `python 07_Datos/scripts/ejecutar.py` deposita dentro de `07_Datos/` las 18
  salidas del documento.** Hasta ahora la etapa `documento` las regeneraba y las comparaba con
  el manifiesto, pero las dejaba en `07_Publicacion/` y `06_Experimento/`, y
  `07_Datos/resultados/` contenia un solo archivo. Ahora, si las 18 coinciden byte a byte con
  el manifiesto, las copia a:
  - `07_Datos/resultados/tablas/`: las siete tablas del documento, seis `.tex` y
    `saturacion_por_entrevista.csv`;
  - `07_Datos/resultados/figuras/`: las cuatro figuras;
  - `07_Datos/resultados/estadisticos/`: acuerdo, supuestos, hipotesis, efectos, analisis por
    item y potencia;
  - `07_Datos/datos_procesados/puntuaciones_consolidadas.csv`.
  
  Antes de copiar vacia las tres carpetas de resultados, para que lo que quede en ellas sea
  siempre lo que acaba de producir la orden. Si una sola salida difiere, no deposita nada.
- `diccionario_datos.csv` describe las columnas de los ocho CSV nuevos del paquete, y
  `checksums_datos.sha256` pasa de 23 a 41 entradas.
- `README_datos.md` y el `README.md` de la raiz dicen donde queda cada tabla y figura.

### Sin cambios

Ninguna cifra, tabla ni figura cambia: las 18 salidas depositadas en `07_Datos/` son identicas
byte a byte a las que ya constaban en `07_Publicacion/` y `06_Experimento/`, que se conservan
donde estaban porque el reporte y el manuscrito las incluyen desde ahi.

### Linea base

**Quien revise el repositorio debe ir directamente a la etiqueta vigente**:
`git checkout 2B-final-v5.6`. `2B-final-v5.5` (`d074c6b`) y todas las anteriores son historicas.

---

## [2B-1.16.0] - 2026-09-12

Registro integro de la generacion del Conjunto A.

### Anadido

- **`06_Experimento/prompts_llm/registro_generacion_conjunto_A.md`**: la instruccion que recibio
  el modelo y cada accion que ejecuto al generar el Conjunto A, el 2026-08-02 entre las 19:44 y
  las 19:51 UTC, extraidas de la exportacion oficial de datos de claude.ai de la cuenta de
  Sanchez Cornejo, Gary Alberto. Los 26 requisitos que se generaron en esa respuesta son los
  depositados. La copia publica omite, y dice por que, el razonamiento interno del modelo, el
  texto de la entrevista EV-15, las busquedas en archivos del proyecto y el script que armo la
  tabla de desciego; lleva el SHA-256 del extracto original.
- **Desviacion 6** en `07_Datos/desviaciones.md`: la guia preveia ejecutar el modelo con una
  consigna literal, y el Conjunto A se genero dentro de la conversacion de trabajo del
  proyecto, a partir de la instruccion «usa tu propio modelo». No cambia ningun dato ni
  resultado.

### Corregido

- `prompt_llm_conjunto_A.md` decia que la conversacion no existia y presentaba la consigna de
  la guia como el mensaje enviado; ahora remite al registro integro y la presenta como la
  tarea que el modelo aplico.
- El manuscrito describia la intervencion como «single query, controlled temperature»: ni fue
  una consulta aislada ni la temperatura se controlo. Se corrige, igual que la amenaza T5, que
  remite ahora al registro. Sigue en 15 paginas.
- El reporte citaba `06_Experimento/consignas/` y `08_Etica/declaracion_uso_ia.md`, rutas que
  no existen; pasan a `06_Experimento/prompts_llm/` y `10_Autoria/declaracion_uso_ia.md`.

### Linea base

**Quien revise el repositorio debe ir directamente a la etiqueta vigente**:
`git checkout 2B-final-v5.5`. `2B-final-v5.4` (`107433f`) y todas las anteriores son historicas.

---

## [2B-1.15.1] - 2026-09-12

Declaracion uniforme de la composicion del equipo.

### Cambiado

- **El equipo activo son tres integrantes** --- Sanchez Cornejo, Munoz Quinonez y Cedeno
  Avila --- y **Mendoza Palma, Allan Jeremy y Gilces Carranza, Jose Ignacio estan retirados del
  equipo**. Hasta ahora varios documentos solo nombraban a Mendoza Palma como retirado y a
  Gilces Carranza como alguien que «no participo». Se declara igual en `README.md`,
  `04_Trazabilidad/composicion_equipo.md`, el ERS, `registro_osf.md`, el banco de preguntas y
  el README de `10_Autoria`: no produjeron artefactos ni confirmaciones, no participan en la
  Entrega Final ni en el examen final y no se les atribuye ninguna parte del trabajo.
- **El folleto de la defensa** listaba a los cinco como autores; ahora lista a los tres.
- `composicion_equipo.md` pone al dia el recuento por autor.

### Sin cambios, a proposito

- Los documentos firmados en fechas anteriores --- el expediente etico, el registro OSF archivado
  y la solicitud de cambio de composicion --- conservan la composicion de su momento.

### Linea base

**Quien revise el repositorio debe ir directamente a la etiqueta vigente**:
`git checkout 2B-final-v5.4`. `2B-final-v5.3` (`13dd0af`) y todas las anteriores pasan a ser
historicas; la tabla completa esta en `[2B-1.15.0]`.

---

## [2B-1.15.0] - 2026-09-12

Cierre de las filas de la matriz de trazabilidad que se podian cerrar sin inventar evidencia.

### Anadido

- **Diecisiete historias de usuario con su criterio de aceptacion, `HU-22` a `HU-38`**, en el
  ERS (version 4.6), para `RF-06`, `RF-09`, `RF-14`, `RF-17`, `RF-18`, `RNF-01`, `RNF-04`,
  `RNF-08`, `RNF-11`, `RNF-13`, `RNF-14`, `RNF-16`, `RD-01`, `RD-10`, `RD-11`, `RNF-IA-07` y
  `RNF-IA-08`. Cada criterio reproduce el criterio de verificacion que el requisito ya tenia:
  ningun umbral, actor ni cifra es nuevo. El ERS escribia historias solo para los requisitos
  Must; desde la 4.6 las escribe tambien para los que tienen fuente declarada.

### Cambiado

- **La matriz pasa de 41 a 59 filas con la cadena completa**, de 75. Se cierran 18 filas,
  entre ellas `RNF-IA-07` y `RNF-IA-08`, las dos del componente inteligente que seguian
  parciales. El caso de uso de `RNF-IA-08` pasa a «No aplica»: es un requisito de gobernanza que
  se verifica por revision documental. Los requisitos funcionales con la cadena hacia adelante
  completa pasan de 23 a **25 de 25**. Se actualizan la copia de la matriz del paquete de
  Zenodo, los casos de prueba, `huerfanos_y_cadenas_rotas.md`, el reporte y el banco de
  preguntas de la defensa. El ERS pasa a 134 paginas, sin desbordes.
- **Quedan abiertas 16 filas, a proposito:** las 13 sin fuente de campo, porque escribirles
  historia seria atribuir a alguien una necesidad que nadie expreso; `RD-02`, porque su fila
  en la matriz y su ficha en el ERS describen restricciones distintas; y `RNF-15`, porque
  ninguna clase del modelo la realiza.

### Corregido

- `generar_casos_prueba.py` fallaba al leer la matriz y la ficha de IA por su marca de orden
  de bytes, y por eso `casos_prueba.csv` no se regeneraba desde el 2026-09-08: la fila de
  `RNF-IA-03` no reflejaba el respaldo de campo que se le dio ese dia. Regenerado, la recoge.

### Pendiente declarado

- La copia de la matriz en `07_Publicacion/dataset_zenodo/` ya no coincide con la depositada
  en Zenodo `2B-1.12.0`. El tablero de Jira sigue nombrando las historias anteriores; su export
  se regenera desde la herramienta y no se edita a mano.
- La verificacion previa firmada sigue siendo la del clon limpio de `3530bb2`.

### Linea base

**Quien revise el repositorio debe ir directamente a la etiqueta vigente**:
`git checkout 2B-final-v5.3`.

| Etiqueta | Estado | Que identifica |
|---|---|---|
| **`2B-final-v5.3`** | **VIGENTE** | La version entregada a la rubrica de cierre: el ultimo commit de `main` |
| `2B-final-v5.2` | Historica | La 2B-1.14.2, antes de cerrar las filas de la matriz, sobre `1f05c14` |
| `2B-final-v5.1` | Historica | La 2B-1.14.1, con los documentos firmados, sobre `09edc04` |
| `2B-final-v5.0` | Historica | La 2B-1.14.0, sobre `3530bb2` |
| `2B-final-v4.0` | Historica | La del examen final de la semana 19, sobre `6bb3b08` |
| `2B-final-v3.0` | Historica | La depositada en Zenodo el 2026-09-04 |
| `2B-final-v2.1` | Historica | La que el docente califico provisionalmente sobre `0e69071` |
| `2B-final` | Historica | Apunta al mismo commit que `2B-final-v2.1` |

---

## [2B-1.14.2] - 2026-09-12

Segunda auditoria contra la rubrica de cierre, sobre un checkout limpio de `2B-final-v5.1`.
Todos los criterios de piso y los once items cumplen; ningun residuo en el arbol ni en los
metadatos de los archivos. Se corrigen los tres defectos que encontro.

### Corregido

- **La declaracion de uso de IA no cubria el ultimo tramo del 2026-09-12** (criterio de piso
  P9): el reparto de firmas calculado por script, el armado de los PDF firmados, las etiquetas
  v5.0 a v5.2 y esta auditoria. Se anaden.
- **La comprobacion P4 de `verificacion_previa.py` no se ejecutaba.** La funcion que la calcula
  devolvia su resultado y quien la llamaba lo descartaba, de modo que el informe decia siempre
  que no habia ninguna marca de coautoria. Ademas buscaba palabras sueltas, y habria marcado un
  mensaje que solo explica un commit hecho desde la web de GitHub. Ahora busca trailers linea a
  linea e informa aparte de los committers ajenos al equipo. **Resultado real sobre el
  historial: ningun trailer `Co-Authored-By` ni `Generated with`; un unico committer ajeno,
  `GitHub <noreply@github.com>` en `d0a3138`, con autor Cedeno Avila**, explicado en
  `04_Trazabilidad/composicion_equipo.md`. El apartado P4 de la verificacion firmada el
  2026-09-12 salio de la version defectuosa; su conclusion coincide con el resultado real, salvo
  que no mencionaba ese committer. No se vuelve a firmar.
- **El README no listaba todos los paquetes de LaTeX.** Faltaban `array`, que usa el ERS desde
  la 2B-1.14.0, y `inputenc`, `fontenc`, `amsmath` y `csquotes`. Ahora se listan por documento.

### Linea base

Esta tabla sustituye a la de `[2B-1.14.1]`. **Quien revise el repositorio debe ir directamente
a la etiqueta vigente**: `git checkout 2B-final-v5.2`.

| Etiqueta | Estado | Que identifica |
|---|---|---|
| **`2B-final-v5.2`** | **VIGENTE** | La version entregada a la rubrica de cierre: el ultimo commit de `main` |
| `2B-final-v5.1` | Historica | La 2B-1.14.1, con los documentos firmados y antes de esta auditoria, sobre `09edc04` |
| `2B-final-v5.0` | Historica | La 2B-1.14.0 antes de depositar los documentos firmados, sobre `3530bb2` |
| `2B-final-v4.0` | Historica | La del examen final de la semana 19, sobre `6bb3b08` |
| `2B-final-v3.0` | Historica | La depositada en Zenodo el 2026-09-04 |
| `2B-final-v2.1` | Historica | La que el docente califico provisionalmente sobre `0e69071` |
| `2B-final` | Historica | Apunta al mismo commit que `2B-final-v2.1` |

---

## [2B-1.14.1] - 2026-09-12

Deposito de los dos documentos firmados que cerraban la version 2B-1.14.0.

### Cambiado

- **`10_Autoria/aporte_individual.pdf` (A10)**, regenerado sobre el historial hasta `3530bb2` y
  firmado por los tres integrantes el 2026-09-12. Sustituye al firmado el 2026-09-04, que no
  cubria el trabajo posterior.
- **`10_Autoria/verificacion_previa.pdf`**, sobre el clon limpio de `3530bb2`, firmado por los
  tres integrantes el 2026-09-12. El reparto de firmas que declaraba era falso --- decia que
  Cedeno Avila no tenia confirmaciones en `01_ERS`, `04_Trazabilidad` ni `08_Defensa`, y las
  tiene ---; ahora `verificacion_previa.py` lo calcula desde el historial, archivo por archivo,
  y declara aparte los dos archivos que tocaron los tres.

### Linea base

Esta tabla sustituye a la de `[2B-1.14.0]`. **Quien revise el repositorio debe ir directamente
a la etiqueta vigente**: `git checkout 2B-final-v5.1`.

| Etiqueta | Estado | Que identifica |
|---|---|---|
| **`2B-final-v5.1`** | **VIGENTE** | La version entregada a la rubrica de cierre, con los documentos firmados: el ultimo commit de `main` |
| `2B-final-v5.0` | Historica | La version 2B-1.14.0 antes de depositar los documentos firmados, sobre `3530bb2` |
| `2B-final-v4.0` | Historica | La del examen final de la semana 19, sobre `6bb3b08` |
| `2B-final-v3.0` | Historica | La depositada en Zenodo el 2026-09-04 |
| `2B-final-v2.1` | Historica | La que el docente califico provisionalmente sobre `0e69071` |
| `2B-final` | Historica | Apunta al mismo commit que `2B-final-v2.1` |

---

## [2B-1.14.0] - 2026-09-12

Auditoria del repositorio contra la rubrica de cierre del Proyecto Fin de Curso, sobre un
clon limpio de `b9783c7`, y correccion de lo que encontro. No cambia ningun requisito, ningun
dato crudo ni ninguna cifra de resultados.

### Linea base

Esta tabla sustituye a la de `[2B-1.13.0]` y es la fuente unica de verdad sobre cual es la
vigente:

| Etiqueta | Estado | Que identifica |
|---|---|---|
| **`2B-final-v5.0`** | **VIGENTE** | La version entregada a la rubrica de cierre: el ultimo commit de `main` de esta version |
| `2B-final-v4.0` | Historica | La del examen final de la semana 19, sobre `6bb3b08` |
| `2B-final-v3.0` | Historica | La depositada en Zenodo el 2026-09-04 |
| `2B-final-v2.1` | Historica | La que el docente califico provisionalmente sobre `0e69071` |
| `2B-final` | Historica | Apunta al mismo commit que `2B-final-v2.1` |

Ninguna etiqueta se mueve ni se borra: la nueva se crea sobre el commit entregado y las
anteriores quedan como registro de lo que existio en cada fecha.

### Corregido

- **El manifiesto de sumas fallaba sobre un clon limpio.** `sha256sum -c checksums.sha256`
  daba `FAILED` en `10_Autoria/verificacion_previa.md`: el commit `b9783c7` regenero el
  manifiesto antes de reescribir ese archivo. Se regenera al final de esta version.
- **El ERS tenia 80 desbordes horizontales** en A4 (item A4 de la rubrica de cierre). Las 68
  tablas conservaban anchos fijos en centimetros que sumaban mas que la caja de texto; pasan
  a anchos proporcionales a ella, y se corrigen los parrafos que se salian del margen. El
  registro de compilacion queda con cero desbordes horizontales y verticales. El PDF pasa de
  124 a 130 paginas y su historial de versiones gana la entrada 4.5.
- **Cedulas en la capa de texto de PDF publicos** (item B6). La solicitud de aprobacion
  etica, su oficio y los anexos A01, A03, A06, A07 y A09 conservaban en texto extraible las
  cedulas del docente y de los cinco estudiantes de la nomina original, y las matriculas. Se
  queman en el mapa de bits. `verificacion_previa.py` no las detectaba porque no leia PDF; su
  comprobacion 10 los lee ahora.
- **La declaracion de uso de IA no cuadraba con el repositorio** (criterio de piso P9).
  Afirmaba cero desbordes en el ERS, un umbral de 0,41 fijado por escrito que no existe, y a
  la vez que los requisitos derivados de la codificacion eran juicio del equipo y que 38 los
  completo el asistente. Se corrigen las tres, y se anade lo que faltaba: el trabajo del 7 al
  12 de septiembre y las operaciones de Git que ejecuto el asistente.
- **El manuscrito seguia presentando el 0,41 como umbral pactado**, pese a la correccion del
  CHANGELOG del 2026-09-08. Se retira y se recompila el PDF.
- **`resumen_proceso_etico.md` decia que la temperatura y los parametros del modelo estaban
  registrados**, y el registro de la consigna dice que no estan disponibles.

### Anadido

- **Declaracion expresa del tratamiento de datos personales**: base de licitud, finalidad,
  plazo de conservacion —hasta el 30 de septiembre de 2028, los 24 meses del plan de gestion
  de datos— y responsable, en la seccion 3.2 de `02_Evidencias/Etica/resumen_proceso_etico.md`
  y en `07_Datos/LICENSE-DATA.txt`, que antes fijaba otro plazo.
- **Dos etapas en la orden unica de `07_Datos`** (items B1 y B3). `conjuntos` escribe en texto
  plano los dos conjuntos de requisitos comparados, tal como los vieron los jueces;
  `documento` ejecuta la cadena de `06_Experimento` y comprueba byte a byte contra el
  manifiesto las 18 salidas del documento. El paquete incorpora el corpus fuente comun y el
  paquete de evaluacion ciega, como copias identicas que la etapa `integridad` vigila.
- **Desviacion 5** en `07_Datos/desviaciones.md`: no consta que la potencia se calculara antes
  de contrastar las hipotesis, como preveia el registro previo. Y la justificacion del tamano
  muestral y del numero de evaluadores, que si es anterior, citada del registro en
  `README_datos.md`.
- **Nota de estado en `prompt_llm_conjunto_A.md`**: que parte del registro de la consigna es
  integra y cual no existe.

### Cambiado

- El calculo de potencia recibe el numero de jueces **contado** en los datos crudos, no un 3
  escrito en `replicar.py` y en el `Makefile`. La salida no cambia.
- Se retira `06_Experimento/resultados/resumen_resultados.csv`: ningun script lo generaba y su
  tamano del efecto para `Correccion_fuente` no coincidia con el de `efectos.csv`.
- README: la tabla de pendientes ya no da por pendiente la defensa grabada, el arbol incluye
  `07_Datos/` y `10_Autoria/`, y el manuscrito tiene 15 paginas, no 12.

---

## [2B-1.13.0] - 2026-09-11

Cierre de la rubrica de cierre del PFC. Una sola entrada, deliberadamente pequena, para
resolver el unico item del Bloque A que el repositorio no dejaba cerrado: la declaracion
de la linea base vigente dentro del propio CHANGELOG.

### Cambiado

- **Linea base vigente, declarada.** El README ya declaraba `2B-final-v4.0` como la unica
  linea base vigente del examen final (commit `6bb3b08`). El CHANGELOG reproducia la
  declaracion de la entrada `[2B-1.7.0]`, que nombraba `2B-final-v2.1` y quedo atras al
  etiquetarse `2B-final-v3.0` y luego `2B-final-v4.0`. Se reescribe aqui, al tope del
  registro, para que la fuente unica de verdad sea esta:

  | Etiqueta | Estado | Que identifica |
  |---|---|---|
  | **`2B-final-v4.0`** | **VIGENTE** | La version entregada para el examen final de la semana 19, sobre el commit `6bb3b08` |
  | `2B-final-v3.0` | Historica | La que se deposito en Zenodo el 2026-09-04, cuando se cerro `2B-1.9.0` |
  | `2B-final-v2.1` | Historica | La que el docente califico provisionalmente con 7,80/10 sobre el commit `0e69071` |
  | `2B-final` | Historica | Apunta al mismo commit que `2B-final-v2.1`. Se conserva porque pudo citarse externamente |

  Las cuatro etiquetas siguen anotadas; el arbol no se reescribe. Lo que se reescribe es
  unicamente el texto que dice cual es la vigente, para que el repositorio no se lea como
  si declarara dos lineas base a la vez.

---

## [2B-1.12.0] - 2026-09-07

La tercera sesion de validacion con usuario tecnico, `WT-10`, que cierra el reparto de
perfiles que la guia exige.

### Anadido

- **Sesion `WT-10` con `TIC-03`**, evidencia `EV-28`, del 2026-09-07: laboratorista de
  Ciencias de la Computacion, responsable del control operativo de las aulas y los
  laboratorios de la carrera, con dieciocho anios en el cargo. Acta de siete paginas con su
  hoja de firmas y consentimiento, ambos censurados en el mapa de bits.
- **El video de la sesion en la ficha tecnica**, que pasa de 34 a **35 piezas**: dieciocho
  videos y diecisiete audios. 00:15:32, 1280x720, h264/aac a 192 kbps, con su SHA-256.

### Cambiado

- **`declaracion_perfil_tecnico.md` ya no declara un incumplimiento.** Declaraba dos sesiones
  tecnicas de las tres exigidas y asumia la consecuencia en la calificacion. Se reescribe: el
  reparto se cumple. Se conserva el documento porque lo que sostiene la clasificacion de un
  participante como tecnico es su criterio, no el recuento, y ese criterio hay que poder
  auditarlo.
- **`EV-28` refuerza cuatro requisitos** en la matriz: `RD-10` y `RD-11` pasan de una fuente a
  dos, y `RNF-01` y `RNF-14` de dos a tres. No cierra ninguna fila nueva --- 41 de 75, como
  antes ---; anade triangulacion donde el respaldo era de un solo testigo.
- Recuento de sesiones de validacion, de nueve a **diez**, en el libreto de grabacion, el
  banco de preguntas, el LEEME de prototipos y el README.
- Consentimientos: de 21 a **22**, de 18 a **19** personas.

### Pendiente declarado

- **El video de `WT-10` no esta dentro del contenedor cifrado.** Se inventaria con su
  duracion, su codec y su SHA-256, y la columna `zona` de su fila lo dice: regenerar el
  contenedor exige la contrasena, que custodia el equipo. Se declara en lugar de dejar que el
  inventario prometa un archivo que el clon no trae.

---

## [2B-1.11.0] - 2026-09-06

Cierre de las tres fuentes que faltaban --- el archivo de Figma, el consentimiento del
segundo usuario tecnico y el panel ampliado --- y el diagnostico de por que el panel
ampliado no se pudo usar.

### Anadido

- **Archivo fuente de Figma de los cuatro prototipos**, en
  `03_Modelado/12_Prototipos_Interfaz/`. Era la unica carpeta de `03_Modelado/` sin fuente
  nativa; el inventario del elemento **A3** pasa de 43 a **44 fuentes** y las doce carpetas
  quedan completas.
- **Consentimiento de `TIC-02`**. El acta de la sesion `WT-09` estaba depositada desde el
  2026-09-05 y su consentimiento no, y el participante no tenia fila en el registro. Marco
  la primera casilla: autoriza el uso de sus datos anonimizados en publicaciones revisadas
  por pares. El registro pasa de veinte a **veintiun participantes**, dieciocho citables.
- **`06_Experimento/panel_ampliado/`**: los datos crudos de las **dos vueltas** del panel de
  siete evaluadores, el mapa de posiciones de la segunda y el script que reproduce las
  cuatro tablas de analisis. No es el analisis del estudio y lo dice en su primera linea.

### Cambiado

- **Se cierra la decision sobre el panel de diez jueces**, pendiente desde el 2026-09-05.
  Se mantienen los **tres jueces del registro previo** como analisis primario. La regla de
  decision se escribio antes de convocar la segunda sesion y se obtuvo un Fleiss medio de
  **-0,026**. `06_Experimento/resultados/` no se toca.

  > **Corregido el 2026-09-08.** Esta entrada decia que el liston para sustituirlos era
  > «Fleiss kappa >= 0,41» y que se habia fijado por escrito. La cifra no consta en el
  > protocolo de la segunda vuelta ni en ninguna otra parte: es la frontera de Landis y Koch
  > para acuerdo moderado, un convencionalismo de lectura, no un umbral pactado. Lo que si
  > se escribio de antemano es la regla de decision, y ese documento se deposita ahora como
  > `06_Experimento/panel_ampliado/protocolo_segunda_vuelta.md`.
- **Amenaza `T2` del manuscrito, reescrita.** Decia que el acuerdo entre evaluadores «no se
  intento mejorar con entrenamiento ni con una ronda de reconciliacion». Se intento dos
  veces, con dos instrumentos distintos, y ahora se reporta con sus cifras: por que fallo,
  por que no es un artefacto de la escala, y donde esta el ruido.
- El generador del registro de consentimientos etiquetaba a `TIC-01` y `TIC-02` como
  entrevistas semiestructuradas y les dejaba la evidencia en blanco. Son sesiones de
  validacion sobre prototipo, y su evidencia es el codigo del acta: `WT-08` y `WT-09`.
- El libreto de la defensa incorpora la decision: se retira el aviso del bloque 4 y se anade
  al bloque 5 el parrafo que cuenta el intento fallido, con la respuesta preparada para la
  pregunta previsible.

### Corregido

- **La censura del consentimiento de `TIC-02` era reversible.** Los cuatro recuadros negros
  eran dibujos vectoriales superpuestos a la imagen: el nombre, la cedula y la firma seguian
  intactos debajo y bastaba con borrarlos en cualquier editor de PDF. Se rehizo quemando las
  bandas en el mapa de bits sobre la envolvente de la tinta, y el archivo depositado ya no
  tiene dibujos vectoriales ni texto extraible. **Se comprobaron los otros diecisiete
  consentimientos del repositorio: ninguno tenia este defecto.**

---

## [2B-1.10.0] - 2026-09-06

Sesiones formales de verificacion y control de cambios, segundo usuario tecnico y una
revision de consistencia de todo el arbol.

### Anadido

- **Inspeccion formal `INS-01` y re-inspeccion `REINS-01`**, celebradas el 2026-09-05 y
  firmadas por los tres integrantes. Los cinco roles de Fagan repartidos entre tres
  personas, con autor y moderador siempre en personas distintas.
- **Acta del comite de control de cambios `CCB-01`** y las cuatro solicitudes `SC-01` a
  `SC-04`. Tres aprobadas; `SC-03` queda diferida de forma expresa.
- **Retrospectiva del equipo**, con tres elementos en cada una de las tres categorias.
- **Sesion de validacion `WT-09`** con el segundo usuario tecnico, `TIC-02`: acta con la
  hoja de firmas censurada y el video registrado en la ficha de la zona restringida como
  `EV-27`. Las sesiones pasan de ocho a **nueve**, y los usuarios tecnicos de uno a **dos**.
- **Las doce notas de campo**: las seis manuscritas de la ronda terminal y las seis de
  observacion de entorno, `NC-01` a `NC-06`, firmadas el 2026-09-05.
- **Tablero de gestion en Jira** con sesenta actividades y su medicion de sincronizacion
  contra la matriz, reproducible por script: 60 de 60, **100 %**.
- **Declaracion del enfoque empirico**: la rubrica asignaba el Enfoque 3 al codigo de equipo
  con el que el docente registra el proyecto, y se ejecuto el Enfoque 1. Se declara la
  desviacion y por que no se revierte, con el registro previo de OSF como argumento.
- **Libreto de grabacion de la defensa**, con el texto literal, el reparto a tres y las
  rutas de lo que hay que abrir.
- Tres diapositivas nuevas en el mazo de la defensa: verificacion y control de cambios,
  trazabilidad y gestion, y evidencia de campo. De doce a **quince**, dentro del minimo.
- `00_LEEME.md` en `03_Modelado/12_Prototipos_Interfaz/`, que fija la correspondencia entre
  `MU-01` a `MU-04` y sus archivos: la matriz los referenciaba en veintidos filas y esa
  correspondencia no estaba escrita en ningun sitio.

### Cambiado

- **La metrica de Correccion deja de estar pendiente**: la re-inspeccion cierra quince de
  los dieciseis defectos y deja `DEF-06` como unico residual. Correccion = 1/25 = **0,04**,
  por debajo del 0,05 de referencia. Es la ultima de las seis metricas de la seccion 5.6 que
  quedaba sin medir.
- `DEF-09` pasa a cerrado: los diagramas de flujo de datos existen en el arbol desde el
  2026-09-04 y el registro seguia declarandolos ausentes.
- La declaracion de perfil tecnico pasa de una sesion a dos, con la tabla de las dos y el
  perfil que cada participante declaro.
- Los artefactos del registro previo de OSF se consolidan bajo `registro_previo/`.

### Corregido

- **Cuatro identificadores repetidos en el banco de preguntas**: la seccion anadida el
  2026-09-04 volvia a empezar en `G1` cuando ya existia una seccion G. Pasa a ser la
  seccion **I**, y las cincuenta preguntas quedan sin ningun identificador duplicado.
- **Nueve referencias a rutas que ya no existen**, casi todas a `08_Etica/`, que es el
  nombre que la carpeta tenia en el repositorio de la Entrega 2A.
- **Cinco archivos duplicados**: dos dentro de `Etica/Anexos/` que rompian la numeracion
  `A01` a `A13`, y tres copias en la raiz de `06_Experimento` que nadie citaba.
- **Una fotografia de entorno duplicada**: `ENT-05` y `ENT-07` eran el mismo archivo byte a
  byte. Se retira `ENT-07` y el inventario pasa de veintinueve a **veintiocho**.
- La doble codificacion estaba depositada dos veces, en `10_Autoria/doble_codificacion/`
  --el elemento A7-- y en `02_Evidencias`, con dos coeficientes distintos publicados sobre
  los mismos datos. Se conserva A7, que es la ubicacion del indice de autoria.
- Cifras desfasadas: «diecisiete entrevistas» donde son dieciseis, la ficha tecnica sin
  contar `EV-27` en su enumeracion, y el banco declarando una sola sesion tecnica.
- `presentacion.pdf` se habia quedado en doce paginas mientras el `.pptx` tenia quince.

---

## [2B-1.9.0] - 2026-09-04

Cierre del examen final. Etiqueta `2B-final-v3.0`.

### Anadido

- **A2 completo**: tres capturas por cada integrante, todas con la barra de tareas y el
  reloj visibles.
- **A6 y A11**: dos fotografias del equipo en la facultad, depositadas tal como salieron
  del telefono, y su inventario EXIF con fecha de captura, dispositivo y hash.
- **A7**: las dos codificaciones tematicas independientes y su acuerdo. Kappa de Cohen sin
  ponderar de 0,548 para el codigo y 0,911 para la categoria, con intervalo por bootstrap.
- **A10 firmado** por los tres integrantes acreditados, previa consulta escrita al docente.
- Sesion de validacion `WT-08` con usuario tecnico, y las dos actas que faltaban por
  depositar: las sesiones de walkthrough pasan de cinco a **ocho**.
- Dos documentos mas de la organizacion: el horario de laboratorios --el artefacto con el
  que `RNF-08` exige integrarse-- y la ficha de registro de practicas. De cuatro a **seis**.
- Declaracion del perfil tecnico en las sesiones de validacion: se realizo una de las tres
  que pide la guia, y se declara la causa en lugar de reclasificar a nadie para cuadrar.

### Cambiado

- **El corpus son dieciseis entrevistas.** La documentacion declaraba diez.
- Las doce grabaciones de la ronda terminal y las dos de `TIC-01` constan en la ficha
  tecnica como zona restringida, con duracion, codec y hash.
- **Lista de verificacion previa firmada por dos integrantes**, repartida de modo que
  ninguno comprueba lo que produjo. Diez de doce comprobaciones en OK sobre clon limpio.

### Corregido tras la revision del expediente

- **`10_Autoria/README.md` declaraba A6 y A7 como pendientes**, A2 como parcial y A10 sin
  firmar. Es el indice del criterio de piso P7: quien lo leyera concluiria que la evidencia
  de autoria esta incompleta.
- **Cinco enlaces relativos rotos**, dos de ellos en el README y en la declaracion de uso de
  IA. Los 74 enlaces del repositorio resuelven.
- **El reporte, el ERS y el manuscrito** decian que el campo se cerro en diez entrevistas.
  Ahora declaran dieciseis y precisan que el analisis va sobre las diez codificadas.
- **La Tabla 68 del ERS** marcaba como pendientes el modelado UML, el dataset con DOI y el
  manuscrito, que estan hechos.
- **El registro de anonimizacion** se detenia el 29 de agosto y no recogia la censura de los
  consentimientos de la ronda terminal ni del acta `WT-08`.
- **`RNF-04` y `RNF-14`**, corregidos contra evidencia de campo.
- **La columna `Estado-Traza`** estaba escrita a mano y se habia desincronizado de las celdas.
  Ahora se comprueba con `04_Trazabilidad/verificar_matriz.py`. La cadena completa pasa de 34
  a 41 filas de 74.
- **El manuscrito enuncia RQ2**, que ya respondia sin declararla, y retira del titulo de un
  apartado una referencia a un criterio de la rubrica de la asignatura.
- **El banco de preguntas de la defensa** no cubria nada de la ronda terminal. Seccion G, con
  once preguntas ancladas a su artefacto.

### Corregido

- La curva de saturacion no era reproducible: `sort_values` no es estable y las seis
  entrevistas de la ronda terminal comparten fecha.
- El manifiesto se regeneraba a mano, y un archivo nuevo sin anadir no lo delataba ninguna
  comprobacion. Ahora sale de `git ls-files`.
- El recuento por autor declaraba cero confirmaciones para el tercer integrante.

---

## [2B-1.8.0] - 2026-09-04

Cierre de la ronda terminal de campo: el corpus pasa de diez a dieciseis entrevistas, y la
documentacion deja de declarar una muestra que ya no es la que hay.

### Anadido

- `06_Experimento/scripts_analisis/extender_corpus_json.py` — incorpora al corpus JSON las
  transcripciones depositadas que aun no figuran en el. No reescribe ningun registro
  anterior y lo comprueba campo por campo antes de escribir. El corpus pasa de 10 a 16.
- `02_Evidencias/Codificacion_Tematica/incorporar_codificacion.py` — valida una hoja de
  codificacion rellenada y la incorpora. Rechaza el fragmento que no aparece literal en la
  transcripcion, el tomado del entrevistador en lugar del participante, el que no lleva
  categoria o requisito, y el duplicado.
- `10_Autoria/generar_manifiesto.py` — regenera `checksums.sha256` desde `git ls-files`.
- `10_Autoria/doble_codificacion/calcular_acuerdo.py` — acuerdo entre las dos
  codificaciones tematicas del elemento A7, con kappa sin ponderar e intervalo por bootstrap.
- Ficha tecnica de los doce registros de la ronda terminal en
  `02_Evidencias/00_Restringido/fichas_tecnicas.csv`, con duracion, codec y hash del
  original de camara. Pasa de 18 a 30 filas.

### Cambiado

- **El corpus son dieciseis entrevistas.** La ronda terminal del 2026-09-03 anadio `EV-20` a
  `EV-25`, todas a docentes. `README.md` y la declaracion de reduccion de muestra se
  actualizan: la reduccion a diez queda **superada**, no borrada. El documento de etica
  conserva su texto y lleva una nota de estado al inicio.
- `02_Evidencias/00_Restringido/README_Restringido.md` — declara los **dos regimenes de
  publicacion**. Las diez primeras entrevistas se consintieron con un formulario que
  autoriza publicar el registro anonimizado; las seis de la ronda terminal, con uno que dice
  que las grabaciones originales no se publican. De estas ultimas, a la zona publica va solo
  la transcripcion y el consentimiento enmascarado.
- `CITATION.cff` — la version declarada estaba en `2B-1.5.0`, dos por detras del CHANGELOG.

### Corregido

- **La curva de saturacion no era reproducible.** `sort_values` de pandas usa quicksort, que
  no es estable, y las seis entrevistas de la ronda terminal comparten fecha: el orden entre
  ellas podia variar entre ejecuciones. Se desempata por identificador de evidencia.
  Reejecutada sobre la codificacion vigente, la tabla sale identica byte a byte a la
  publicada.
- La copia de `curva_saturacion.py` del deposito Zenodo tomaba el corpus de una carpeta que
  no existe dentro del propio deposito.
- El manifiesto se regeneraba a mano, y la comprobacion no delataba el hueco: un archivo
  nuevo que nadie anadiera no aparecia en ninguna linea y por tanto no fallaba nada.
- `04_Trazabilidad/composicion_equipo.md` declaraba cero commits para el tercer integrante.

---

## [2B-1.7.0] - 2026-09-03

Restitucion del paquete de datos, retirada de la clave de desciego, composicion del equipo
al dia y declaracion del origen del historial. Atiende la guia de desarrollo individualizada
emitida por el docente el 2026-09-02 tras verificar el repositorio sobre un clon completo.

### Origen de este repositorio, y por que el historial empieza el 30/08

La guia observa que todo el historial se concentra entre el 30/08 y el 01/09 mientras la
evidencia de campo esta fechada meses antes, y pide documentar la migracion indicando
origen, fecha y motivo. Se documenta aqui.

| | |
|---|---|
| **Origen** | `https://github.com/gsanchezc6-beep/SIGA_FGMMN_ISR401_AVANCE_2A` |
| **Fecha de creacion de este repositorio** | 2026-08-29 |
| **Primer commit** | 2026-08-30, 01:16 |
| **Motivo** | **Cambio de rubrica.** La Entrega Final se rigio por una rubrica distinta de la que goberno la Entrega 2A, con una estructura de carpetas y un conjunto de entregables diferentes. El equipo decidio abrir un repositorio nuevo en lugar de reorganizar el anterior, para que el arbol correspondiera exactamente a la estructura exigida y no arrastrara carpetas de una entrega ya evaluada. |

**Donde consta el trabajo anterior al 30/08.** En el repositorio de la Entrega 2A, enlazado
arriba, cuyo historial cubre la elicitacion, las diez entrevistas, el cuasi-experimento y el
registro previo del protocolo. Las fechas de ese historial son las de los artefactos que este
repositorio hereda. La cronologia del dia del cuasi-experimento, reconstruida commit a
commit desde ese repositorio, esta en
`06_Experimento/registro_previo/desviacion_clave_desciego.md`, con la orden de git que la
reproduce.

**Lo que el equipo asume.** Abrir un repositorio nuevo tuvo un coste: la trazabilidad
acumulada del proyecto quedo repartida entre dos repositorios en lugar de leerse en uno solo.
Se enlazan mutuamente y se declara la relacion, pero no se presenta el historial de este
repositorio como si fuera el del proyecto entero.

### Linea base vigente

Existen dos etiquetas anotadas sobre el mismo commit `0e69071`, y la guia advierte con razon
que dos lineas base simultaneas equivalen a ninguna. Se declara:

| Etiqueta | Estado | Que identifica |
|---|---|---|
| **`2B-final-v2.1`** | **VIGENTE** | La version de la Entrega Final que el docente califico, sobre el commit `0e69071` |
| `2B-final` | Historica | Apunta al mismo commit. Se conserva porque pudo citarse externamente, pero no es la referencia |

El trabajo del examen final es posterior a esa linea base y se etiquetara por separado al
cierre.

### Anadido

- `07_Datos/` - paquete de datos restituido con la estructura exigida: datos crudos, datos
  procesados, scripts, resultados, diccionario de datos, licencia de datos, manifiesto de
  sumas, desviaciones y registro de deposito. Se reconstruye entero con una sola orden,
  `python 07_Datos/scripts/ejecutar.py`, sin instalar ninguna dependencia.
- `07_Datos/datos_procesados/evaluacion_ciega_formato_largo.csv` - la hoja de evaluacion a
  ciegas en formato largo, con evaluador, requisito, orden de presentacion, brazo, criterio
  y puntuacion. 765 filas.
- `07_Datos/resultados/acuerdo_interevaluador_ic.csv` - los veinte coeficientes de acuerdo,
  cada uno con su intervalo de confianza del 95 % por bootstrap de items, que hasta ahora se
  publicaban desnudos.
- `06_Experimento/clave_desciego_UBICACION.md` - donde esta la tabla de desciego, quien la
  custodia y su suma SHA-256.
- `07_Datos/datos_crudos/asignacion_brazo_items.csv` - el brazo de cada item, que es lo que
  el analisis necesita, sin la correspondencia con el codigo real del requisito.

### Cambiado

- **Composicion del equipo: pasa a tres.** Cedeno Avila, Winston Damian se reincorpora el
  2026-09-02 y asume la transcripcion y anonimizacion del corpus de la ronda terminal.
  Mendoza Palma, Allan Jeremy, que figuraba en la caratula del SGA, se retira sin producir
  artefactos ni confirmaciones. Actualizados `04_Trazabilidad/composicion_equipo.md`,
  `CITATION.cff`, `README.md`, `01_ERS/secciones_generadas.tex`,
  `07_Publicacion/manuscrito_final.tex`, `08_Defensa/guion.md` y
  `08_Defensa/banco_preguntas.md`. La declaracion muestra el recuento de commits de Cedeno
  Avila **en cero** mientras lo sea, en lugar de atribuirle trabajo que el historial no
  respalda.
- `06_Experimento/scripts_analisis/analizar_resultados.py` - su etapa de consolidacion
  apunta ahora a `asignacion_brazo_items.csv`. Solo leia `Item_ciego` y `Origen`, nunca
  `Codigo_real`, de modo que la cadena corre igual sin la tabla de desciego. Ejecutado
  `replicar.py` completo tras el cambio, las 16 salidas resultan identicas byte a byte.

### Retirado

- `06_Experimento/clave_desciego_items.csv` - la tabla de desciego sale del repositorio
  publico al contenedor cifrado AES-256, por instruccion expresa de la guia. La anotacion de
  la desviacion se mantiene sin editar en
  `06_Experimento/registro_previo/desviacion_clave_desciego.md`.

### Lo que no se reescribe

El acta de constancia del cierre de campo en N=10 y los consentimientos de la sesion de
validacion comunicativa estan firmados por dos personas porque en esa fecha el equipo eran
dos. Se declara que la composicion se amplio despues, con su fecha, en lugar de rehacer un
documento firmado.

---

## [2B-1.6.0] - 2026-09-01

Analisis de sensibilidad, despliegue en contenedor y cierre de la verificacion documental.

### Anadido

- `06_Experimento/scripts_analisis/analisis_por_item.py` - analisis de sensibilidad que toma
  el requisito como unidad en lugar del juez. La potencia para un efecto mediano sube de
  **0,084 a 0,417**, y los tamanos de efecto pasan a tener intervalos interpretables. Las dos
  aproximaciones coinciden: ninguna dimension resulta significativa tras Holm-Bonferroni.
- `06_Experimento/registro_previo/desviacion_analisis_por_item.md` - la desviacion declarada,
  con lo que decia el plan preregistrado, que problema aparecio y que se hizo.
- `07_Publicacion/verificacion_referencias.md` - registro de la verificacion de las 40
  referencias: 35 con DOI que resuelve al trabajo citado y 5 sin DOI por no tener uno
  asignado, cada una con su motivo.
- `05_MVP/docker-compose.yml` - despliegue del prototipo con una sola orden.
- `02_Evidencias/Fotos_Entorno/` - once fotografias nuevas (ENT-16 a ENT-26) con su
  inventario, entre ellas la camara Dahua identificable y un aula vacia con las luminarias
  encendidas a plena luz de dia.
- `02_Evidencias/Codificacion_Tematica/` - la curva de saturacion y la tabla por entrevista,
  que la guia situa en esta carpeta.
- `08_Defensa/README.md` - declara que la defensa fue individual y que no existe grabacion.

### Cambiado

- Las diez transcripciones pasan de texto plano a **Markdown estructurado**, con la cabecera
  como tabla y cada intervencion marcada. El contenido se conserva literal.
- `protocolo.pdf`, `osf_registration.pdf` y `osf_deviations.pdf` se ven ya al nivel de
  `06_Experimento/`, como fija el arbol de la seccion 9.1.
- `08_Defensa/guion.md` y `guion_reparto_exposicion.md` - reescritos para defensa individual.
- El manuscrito incorpora la subseccion del analisis de sensibilidad y pasa a 13 paginas.

### Corregido

- Cuatro referencias cruzadas del manuscrito apuntaban a etiquetas inexistentes
  (`tab:desc` y `tab:power`) e imprimian interrogantes en el PDF.
- La respuesta G2 del banco de preguntas afirmaba que el historial estaba concentrado en una
  persona; el recuento real es 47 y 40.

---

## [2B-1.5.0] - 2026-09-01

Cierre del deposito FAIR, incorporacion del manuscrito y reorganizacion del arbol segun
la seccion 9.1 de la guia.

### Anadido

- `07_Publicacion/manuscrito_final.tex` y su PDF - manuscrito en plantilla Springer LNCS
  (`llncs.cls`), 12 paginas, compilado sin errores y sin citas sin resolver.
- `07_Publicacion/referencias.bib` - 40 entradas, 35 con DOI verificado uno a uno
  resolviendo al trabajo citado. Las cinco restantes son una norma ISO, el SWEBOK, un
  libro, una ley y un informe tecnico: ninguno tiene DOI asignado.
- `07_Publicacion/analisis_revistas.md` - eleccion de REFSQ 2027, track Research, como
  objetivo primario, coherente con la plantilla empleada.
- `07_Publicacion/dataset_zenodo/` - paquete efectivamente depositado en Zenodo.
- `06_Experimento/osf_deviations.pdf` - desviaciones declaradas respecto del protocolo.
- `fair_assessment.pdf` - autoevaluacion FAIR con F-UJI: 21 de 26 indicadores, 80,8 %.
- `04_Trazabilidad/composicion_equipo.md` - integrantes del equipo con el recuento por
  autor del historial que lo respalda.
- `08_Defensa/folleto_una_hoja.pdf` y `presentacion.pdf`.

### Cambiado

- **Reorganizacion del arbol.** `07_Datos/` se disuelve: los datos crudos, los procesados
  y los scripts pasan a `06_Experimento/`, y las figuras y tablas a `07_Publicacion/`.
  `09_Defensa/` pasa a `08_Defensa/`, `08_Etica/` a `02_Evidencias/Etica/` y
  `02_Evidencias/Validacion/` a `02_Evidencias/Validacion_Walkthrough/`. Los traslados se
  hicieron con `git mv`, de modo que el historial sigue a cada archivo.
- `06_Experimento/replicar.py` y `Makefile` - rutas actualizadas. El pipeline se ejecuto
  completo despues del traslado y regenera todas las tablas y figuras.
- `CITATION.cff` - el DOI principal pasa a ser el del deposito de datos en Zenodo; se
  anaden el registro OSF y el identificador de Software Heritage como identificadores
  relacionados.
- `README.md` - nueva seccion con los identificadores persistentes y la cita recomendada;
  arbol actualizado.
- Equipo declarado en la caratula del ERS, el README, el reporte, el manuscrito y
  `CITATION.cff`: dos integrantes, que son los dos autores del historial.
- `04_Trazabilidad/aporte_individual.csv` - regenerado desde `git log`: 87 filas, una por
  commit, todas con identificador que resuelve.
- `checksums.sha256` - regenerado sobre el arbol reorganizado: 290 entradas, comprobadas
  sin error.

### Corregido

- El manuscrito ya no contiene marcadores de plantilla: se sustituyeron el correo de
  contacto, el DOI de Zenodo y el identificador de Software Heritage por sus valores
  reales.
- `07_Publicacion/tablas/tabla_power_calculation.tex` - un caracter griego sin escapar
  impedia la compilacion.
- Se retiro `04_Trazabilidad/acreditacion_aporte.md`, que acreditaba a personas ajenas al
  equipo actual.

---

## [2B-1.4.0] - 2026-08-31

Cierre de la trazabilidad y acreditacion del aporte individual.

### Anadido

- `04_Trazabilidad/huerfanos_y_cadenas_rotas.md` - huerfanos y cadenas rotas listados con
  causa y accion, como exige la guia.
- `04_Trazabilidad/acreditacion_aporte.md` - responde a las dos observaciones del docente
  sobre el historial: el trabajo anterior al 30 de agosto y el aporte de los integrantes
  sin commits en este repositorio.
- `01_ERS/` - historias HU-18, HU-19 y HU-20 para RF-20, RF-24 y RF-25, con sus criterios
  CA-18, CA-19 y CA-20. Los diecisiete escenarios Gherkin existentes quedan etiquetados
  como CA-01 a CA-17.
- `04_Trazabilidad/matriz_trazabilidad.csv` - columnas de clase, proceso, caso de prueba y
  estado de la traza.

### Corregido

- Ocho identificadores de historia de la matriz no resolvian contra el ERS, y ningun
  criterio de aceptacion resolvia porque el ERS no los etiquetaba. Corregido en ambos
  extremos.
- La declaracion de aporte individual subestimaba el trabajo de tres integrantes. Rehecha
  sobre el historial real de los dos repositorios: 183 commits, uno por fila.
- Tres filas de la matriz arrastraban una coma de mas.

### Medido

- Trazabilidad, cadena adelante completa: de **48,0 % a 92,0 %**, por encima del 90 % de
  referencia.
- Celdas vacias en la matriz: de **308 a 0**.
- `checksums.sha256`: 254 entradas, con los archivos xml ya cubiertos.

---

## [2B-1.3.0] - 2026-08-31

Comprobante del registro previo y ampliacion del manifiesto de integridad.

### Anadido

- `06_Experimento/registro_previo/osf_registration.pdf` - exportacion de 15 paginas de la
  pagina publica del registro, con DOI, fecha de registro, contribuyentes y formulario.
- `06_Experimento/registro_previo/osf_internet_archive.pdf` - ficha del item archivado por
  el Center for Open Science, con su fecha propia.
- `06_Experimento/registro_previo/osf_registration_api.json`,
  `osf_contributors_api.json`, `osf_internet_archive_bag.zip` y
  `osf_internet_archive_meta.xml` - la misma evidencia en formato verificable con dos
  ordenes `curl`, sin credenciales.

### Cambiado

- `06_Experimento/registro_previo/registro_osf.md` - se corrige el estado: el registro ya
  constaba como retrospectivo en la propia OSF desde el 2026-08-27. G9 sigue incumplido,
  pero la declaracion esta hecha en la fuente y con fecha.
- `checksums.sha256` - de 248 a 253 entradas; el manifiesto cubre ahora los archivos zip.
- `.gitattributes` - `*.zip binary`, para que el hash del paquete archivado cuadre sobre
  un clon limpio.

---

## [2B-1.2.0] — 2026-08-31

Correcciones derivadas de la revision docente de la Entrega Final.

### Anadido

- `06_Experimento/registro_previo/desviacion_clave_desciego.md` — desviacion del
  protocolo documentada: que es la tabla de desciego, por que debe ser publica para que el
  paquete de replicacion funcione, y que amenaza a la validez queda declarada y pendiente
  de verificar.
- `01_ERS/` — subseccion 3.3.2, requisitos del componente de inteligencia artificial:
  rendimiento, equidad con su regla de no despliegue, explicabilidad, datos de
  entrenamiento con sus sesgos declarados, plan de monitoreo y clasificacion de riesgo.
- `01_ERS/` — resumen bilingue, Resumen y Abstract con sus palabras clave.

### Cambiado

- La tabla de desciego pasa de `07_Datos/datos_crudos/CLAVE_RESPUESTAS_no_compartir_con_jueces.csv`
  a `06_Experimento/clave_desciego_items.csv`. Es artefacto de diseno experimental, no dato
  crudo de campo, y su nombre anterior afirmaba una restriccion que el repositorio no
  cumplia. El contenido es identico y las diez salidas del pipeline no cambian.
- `07_Datos/scripts/analizar_resultados.py` — ruta por defecto de la tabla de desciego.
- `checksums.sha256` — regenerado.

---

## [2B-1.1.0] — 2026-08-30

Consolidacion de la especificacion y cierre de las declaraciones del repositorio.

### Anadido

- `06_Experimento/replicar.py` — el pipeline completo en una sola orden, sin depender de
  GNU Make. Ejecuta las nueve etapas con los mismos parametros y la misma semilla que el
  Makefile, y produce las mismas tablas y figuras byte a byte. Incluye `--verificar`,
  que sondea el codec y la duracion del material audiovisual y comprueba el manifiesto
  de sumas sin necesidad de `sha256sum`.
- `06_Experimento/resultados/entorno_python.txt` — version de Python y de cada
  dependencia con la que se produjeron los resultados publicados.
- `CITATION.cff` — identificador persistente del deposito: DOI `10.17605/OSF.IO/7PQ3H`,
  con su bloque `identifiers`.
- `README.md` — apartado «Elementos aun no depositados», que declara de forma explicita
  los cinco elementos que el repositorio todavia no contiene y en que estado esta cada
  uno.
- `reporte.tex` — etiquetas de las tres tablas de anexo que no las tenian:
  `tab:metricas`, `tab:retrospectiva` y `tab:correspondencia`.

### Cambiado

- `01_ERS/` — la especificacion pasa a version 4.0 y se identifica como Entrega Final
  (2B) en la caratula, en el repositorio declarado y en el historial de versiones. Las
  referencias a la Entrega 3 (2A) que describen hechos pasados se conservan intactas:
  son historia del documento, no una identidad equivocada.
- `01_ERS/secciones_generadas.tex` — las conclusiones dejan de anunciar como pendiente
  lo que esta entrega ya cierra, y declaran lo que sigue abierto: los umbrales de RNF-07,
  RNF-09, RNF-10, RNF-12, RNF-13 y RNF-15 sin verificacion de campo, y la cadena de
  trazabilidad hacia clase, proceso y caso de prueba.
- `reporte.tex` — cada figura y cada tabla se referencia ahora desde el cuerpo del texto.
  Antes ninguna de las cinco tablas generadas por el pipeline se citaba en la prosa.
- `README.md` — la orden unica de reproduccion se documenta por las dos vias, con GNU
  Make declarado como opcional.
- `checksums.sha256` — regenerado sobre las 248 entradas del manifiesto. Comprueba sin
  error.

### Corregido

- **Identificadores de requisito no funcional duplicados.** El prefijo aparecia como
  `NFR-` en las tablas del ERS y como `RNF-` en la prosa y en la matriz de trazabilidad,
  lo que rompia la resolucion automatica de identificadores. Se unifica en `RNF-`, que
  es el que ya usaban la matriz y la columna de tipo. 49 sustituciones en siete
  archivos.
- **Solapamiento funcional entre RF-13 y RF-16**, unico conflicto abierto que arrojaba
  la auditoria de consistencia. Ambos se disparaban ante la misma condicion y con el
  mismo umbral. Se delimitan por causa conforme a la solicitud de cambio SC-01: RF-13
  actua por consumo sostenido sin actividad, con independencia del horario; RF-16 actua
  al concluir la ultima franja asignada, con independencia del consumo. Se anade regla
  de precedencia y registro en bitacora de que regla ordeno el apagado. Se alinean las
  historias HU-11 y HU-13 y sus escenarios.
- **Carpetas declaradas y vacias.** El arbol del README describia cinco carpetas sin
  contenido en el repositorio. Se retiran del arbol y su ausencia se declara en el
  apartado nuevo, de modo que el repositorio no nombra nada que no exista.
- `README.md` — la descripcion de `04_Trazabilidad/` prometia tablas de huerfanos y un
  tablero que la carpeta no contiene; se ajusta a lo que hay.

---

## [2B-1.0.0] — 2026-08-29

Reconstruccion del repositorio de la Entrega Final sobre la estructura de la seccion 9
de la guia vigente.

### Anadido

- Arbol de carpetas de la seccion 9: `01_ERS/`, `02_Evidencias/` con sus subcarpetas de
  consentimientos, video, audio, transcripciones, guiones, cuestionario, fotografias del
  entorno, documentos de la organizacion, notas de campo, codificacion tematica y
  validacion; `03_Modelado/`, `04_Trazabilidad/`, `05_MVP/`, `06_Experimento/` y
  `07_Datos/`.
- `04_Trazabilidad/aporte_individual.csv` — una fila por aporte, cada una con el
  identificador del commit que la respalda y el repositorio donde se puede verificar.
- `07_Datos/diccionario_datos.csv` — significado, tipo y rango de cada variable de los
  datos crudos, procesados y de resultados.
- `07_Datos/correspondencia_salidas.csv` — cada tabla y cada figura del reporte
  emparejada con el script que la produce y la etapa del Makefile que la invoca.
- `08_Etica/declaracion_uso_ia.md` — declaracion por seccion, con herramienta, tipo de
  asistencia y metodo de validacion aplicado.
- `reporte.tex` — documento entregado, con las secciones y el orden que fija la
  seccion 10 de la guia.
- Tres registros de audio de entrevista recuperados del historial del repositorio de la
  Entrega 2A: DOC-02, COORD-03 y DOC-04.

### Cambiado

- Nomenclatura de archivos normalizada a ASCII sin acentos ni espacios, con guion bajo
  como separador. Afecta a las quince fotografias del entorno, a los cuatro prototipos
  de interfaz, al diagrama de contexto, al libro de respuestas del cuestionario y al
  horario academico.
- Los diez consentimientos y las cinco actas de sesion de validacion pasan a la
  convencion `AAAA-MM-DD_TipoParticipante_Codigo_Tecnica.ext`.
- El paquete de replicacion se traslada a `07_Datos/`, que es la carpeta que nombra la
  seccion 9. Los datos crudos, los datos procesados y los scripts quedan bajo esa raiz.
- Los diagramas UML se reorganizan por tipo de modelo, cada uno con su archivo fuente
  nativo junto a las exportaciones.

### Corregido

- Se retiran las referencias a artefactos de la guia anterior que no forman parte de
  esta entrega: autoevaluacion FAIR, identificador de Software Heritage y deposito
  externo con identificador persistente.
- Se eliminan los marcadores de plantilla y las instrucciones dirigidas al equipo de
  los archivos raiz. Ningun campo queda escrito como pendiente: los valores que no se
  pueden afirmar se omiten.
- Se elimina de la documentacion toda mencion a archivos que no existen en el arbol.

---

## [2A-1.0.0] — 2026-08-02 (Entrega 3, repositorio `SIGA_FGMMN_ISR401_AVANCE_2A`)

Version de la que procede la evidencia de campo migrada: transcripciones, consentimientos,
fotografias, documentos de la organizacion, modelado UML e i*, prototipos de interfaz y
registros de audio.

---

## [1B] y [1A] — 2026

Entregas iniciales del Proyecto Fin de Curso: elicitacion preliminar, primera version de
la especificacion y modelado de contexto.
