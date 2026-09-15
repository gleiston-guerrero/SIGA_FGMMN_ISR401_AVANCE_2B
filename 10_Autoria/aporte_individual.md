# Declaracion de aporte individual

**Proyecto SIGA · Equipo FGMMN · ISR-401 · Universidad Tecnica Estatal de Quevedo**

Elemento **A10** de la evidencia de autoria. Declara que hizo cada integrante, sobre que
artefactos y con que confirmaciones del historial se acredita.

Este documento **no se escribe a mano**: se genera con `04_Trazabilidad/generar_aporte_individual.py`
desde el propio historial. El detalle confirmacion por confirmacion esta en [`../04_Trazabilidad/aporte_individual.csv`](../04_Trazabilidad/aporte_individual.csv).

---

## Resumen

| Integrante | Correo institucional | Commits | Primera | Ultima |
|---|---|---|---|---|
| Gary Alberto Sanchez Cornejo | gsanchezc6@uteq.edu.ec | **173** | 2026-08-30 | 2026-09-13 |
| Yeranick Esther Munoz Quinonez | ymunozq@uteq.edu.ec | **114** | 2026-08-30 | 2026-09-14 |
| Winston Damian Cedeno Avila | wcedenoa2@uteq.edu.ec | **12** | 2026-09-04 | 2026-09-09 |

Comprobable con `git shortlog -sne main`. El total de esta tabla es una confirmacion
menor que el historial completo, porque la declaracion no puede incluir el commit que la deposita.

---

## Gary Alberto Sanchez Cornejo

**Rol:** Analista lider; especificacion, componente empirico e integracion

**Confirmaciones: 173**, de 2026-08-30 a 2026-09-13.

### Areas sobre las que trabajo

| Area | Archivos tocados |
|---|---|
| Evidencia de campo y etica | 679 |
| Documentos de raiz | 218 |
| Modelado UML e i* | 136 |
| Manuscrito y deposito | 129 |
| Componente empirico | 108 |
| Paquete de datos | 98 |
| Especificacion de requisitos | 70 |
| Evidencia de autoria | 68 |
| Defensa | 66 |
| Producto minimo viable | 53 |
| Trazabilidad | 48 |
| Otros | 8 |

### Confirmaciones

| Commit | Fecha | Aporte |
|---|---|---|
| `a939f6d` | 2026-08-30 | docs: agrega los archivos raiz obligatorios y la licencia dual |
| `4f85748` | 2026-08-30 | docs: agrega el reporte del estudio con su estructura y bibliografia |
| `d713c55` | 2026-08-30 | docs: agrega la ERS/SRS v2.0 compilada con sus figuras |
| `f3fa45d` | 2026-08-30 | feat: agrega la auditoria de calidad de la especificacion con sus conteos base |
| `36cd4f3` | 2026-08-30 | feat: agrega la ficha del componente de IA y su clasificacion de riesgo |
| `aada199` | 2026-08-30 | feat: agrega el diagrama de contexto y el modelado organizacional iStar |
| `59a779c` | 2026-08-30 | feat: agrega el diagrama general de casos de uso y el de clases refinado |
| `c1b4201` | 2026-08-30 | feat: agrega los diagramas de secuencia de los casos de uso obligatorios |
| `60868be` | 2026-08-30 | feat: agrega los diagramas de actividad de los flujos principales |
| `d938f4c` | 2026-08-30 | feat: agrega las maquinas de estado y los diagramas de componentes y despliegue |
| `2c5e510` | 2026-08-30 | feat: agrega los prototipos de interfaz de las pantallas obligatorias |
| `eac1c93` | 2026-08-30 | feat: agrega la matriz de trazabilidad y la priorizacion MoSCoW y Kano |
| `6928f8a` | 2026-08-30 | docs: agrega el protocolo experimental y su registro previo con desviaciones |
| `c986ab8` | 2026-08-30 | feat: agrega los instrumentos de evaluacion ciega y las consignas del modelo |
| `7e63cab` | 2026-08-30 | feat: agrega el pipeline de analisis reproducible con una sola orden |
| `42b53db` | 2026-08-30 | feat: agrega las salidas estadisticas del componente empirico |
| `bc8426a` | 2026-08-30 | data: agrega los datos crudos y procesados del paquete de replicacion |
| `698366a` | 2026-08-30 | data: agrega el diccionario de datos y la correspondencia de salidas del reporte |
| `bb4b3fd` | 2026-08-30 | feat: agrega el codigo fuente del prototipo organizado por modulos |
| `ffe701b` | 2026-08-30 | docs: agrega el despliegue del prototipo y su cobertura de requisitos |
| `33732bb` | 2026-08-30 | feat: agrega el video de demostracion del recorrido funcional |
| `6803847` | 2026-08-30 | docs: agrega el guion de la defensa individual y el banco de preguntas |
| `8e0334e` | 2026-08-30 | docs: declara el aporte individual con los identificadores de commit que lo respaldan |
| `4ecc5b1` | 2026-08-30 | docs: completa la declaracion de aporte y regenera el manifiesto de integridad |
| `bb53c76` | 2026-08-30 | fix: evita que el manifiesto de sumas se normalice a CRLF en Windows |
| `d7962ac` | 2026-08-30 | fix: impide que los archivos del manifiesto se normalicen al clonar |
| `baa8fce` | 2026-08-30 | docs: redacta el cuerpo completo del reporte del estudio |
| `b9cc55d` | 2026-08-30 | fix: el script de potencia emitia un alfa literal que rompia la compilacion |
| `bd6f017` | 2026-08-30 | docs(ers): identifica la especificacion como Entrega Final 2B en su version 4.0 |
| `e2ff989` | 2026-08-30 | build(ers): recompila la especificacion consolidada |
| `9132cb1` | 2026-08-30 | docs(reporte): referencia en el texto cada figura y cada tabla del estudio |
| `982df1b` | 2026-08-30 | build(reporte): recompila el reporte con las referencias cruzadas resueltas |
| `8c03f2b` | 2026-08-30 | docs(ers): declara version, fecha y commit base en la caratula |
| `3edde5a` | 2026-08-30 | docs(reporte): sincroniza la tabla de metricas con la auditoria y explica los cambios |
| `282133d` | 2026-08-30 | build: recompila ambos documentos y regenera el manifiesto de sumas |
| `05c2a39` | 2026-08-31 | docs(ers): corrige el commit base declarado en la caratula |
| `1375eb2` | 2026-08-31 | docs(ers): incorpora los requisitos del componente de IA a la especificacion |
| `f86f54d` | 2026-08-31 | docs(ers): anade el resumen bilingue que exige el criterio C1 |
| `2174d54` | 2026-08-31 | build(ers): recompila la especificacion y regenera el manifiesto |
| `e383c23` | 2026-08-31 | docs(ers): eleva la especificacion a la version 4.1 |
| `065b9c5` | 2026-08-31 | build(ers): recompila la version 4.1 y regenera el manifiesto |
| `28ab805` | 2026-08-31 | fix(ers): etiqueta los criterios de aceptacion y anade las historias que faltaban |
| `cf362f9` | 2026-08-31 | docs(ers): eleva la especificacion a la version 4.2 |
| `db6c5fe` | 2026-08-31 | build(ers): recompila la version 4.2 |
| `0bc376d` | 2026-08-31 | docs(ers): aplica las decisiones del comite CCB-01 y declara las dependencias |
| `ae7f654` | 2026-08-31 | build(ers): recompila la especificacion en su version 4.3 |
| `d4e5c8d` | 2026-08-31 | docs(etica): declara la reduccion de la muestra a diez entrevistas |
| `e1489e2` | 2026-09-01 | feat(publicacion): incorpora el manuscrito final y su paquete de deposito |
| `cfbda80` | 2026-09-01 | feat(experimento): anade el analisis de sensibilidad por item y reubica el pipeline |
| `bcc3149` | 2026-09-01 | feat(mvp): anade el despliegue del prototipo en contenedor |
| `a2ce2c6` | 2026-09-01 | docs(defensa): corrige los materiales a la modalidad individual |
| `4bd0a30` | 2026-09-01 | build(ers): deja la caratula con los dos integrantes reales y recompila |
| `ea7c616` | 2026-09-01 | docs(readme): declara los identificadores persistentes y el arbol vigente |
| `ae2cd78` | 2026-09-01 | fix(ers): deja la tabla de roles del anexo A.1 con los dos integrantes |
| `268837f` | 2026-09-01 | fix(reporte): corrige el umbral de trazabilidad y declara el cierre de cadenas |
| `dd91d88` | 2026-09-01 | docs(protocolo): anade notas de actualizacion sin reescribir lo registrado |
| `91ad3ca` | 2026-09-01 | fix(publicacion): apunta al registro OSF y al deposito Zenodo vigentes |
| `2048ebc` | 2026-09-01 | feat(evidencias): deposita la sesion de member checking MC-01 |
| `7b058eb` | 2026-09-01 | feat(etica): deposita el acta de constancia N=10 y el comprobante del correo |
| `9d3fc7c` | 2026-09-01 | fix(defensa): corrige la presentacion y actualiza el banco de preguntas |
| `d86291d` | 2026-09-01 | fix(modelado): reconstruye el diagrama i* SR |
| `94f0c19` | 2026-09-01 | feat(defensa): deposita la exposicion grabada y declara que no es la defensa |
| `0e69071` | 2026-09-01 | docs(trazabilidad): pone al dia la declaracion de aporte |
| `b1a2b94` | 2026-09-02 | docs(entrega): atiende las observaciones del informe de la 2B |
| `042732e` | 2026-09-03 | feat(datos): restituye 07_Datos como paquete de datos verificable |
| `69b3008` | 2026-09-03 | docs(equipo): declara la composicion de tres y el origen del historial |
| `e7c7b7e` | 2026-09-03 | feat(autoria): crea 10_Autoria con la evidencia que no depende de terceros |
| `2f9ef3d` | 2026-09-03 | feat(ers): especifica el componente inteligente como requisitos verificables |
| `930b580` | 2026-09-03 | feat(trazabilidad): define los casos de prueba que la matriz citaba sin respaldo |
| `4ae79d4` | 2026-09-03 | docs(autoria): pone al dia el aporte individual y deposita el elemento A10 |
| `6fc1216` | 2026-09-03 | feat(autoria): ejecuta la lista de verificacion previa de la seccion 11 |
| `fdb1c2c` | 2026-09-03 | feat(etica): registra el alcance del consentimiento de cada participante |
| `4dd22aa` | 2026-09-03 | fix(etica): corrige la asignacion de la ronda terminal a seis docentes |
| `81cc69e` | 2026-09-03 | docs(autoria): incorpora los ORCID y precisa quien rindio la defensa |
| `adfc44f` | 2026-09-04 | fix(publicacion): las tablas del manuscrito caben y estan en ingles |
| `898c973` | 2026-09-04 | fix(experimento): orden determinista de la curva e incorporacion del corpus |
| `5a47632` | 2026-09-04 | docs: el corpus son dieciseis entrevistas, y la documentacion lo dice |
| `bc8f312` | 2026-09-04 | feat(autoria): A6 y A11 completos, y el perfil tecnico declarado |
| `d6c1615` | 2026-09-04 | fix(evidencias): la causa del perfil tecnico es de calendario, no de plantilla |
| `e630d8c` | 2026-09-04 | fix(evidencias): el cargo de TIC-01 se toma del consentimiento firmado |
| `d1a02a1` | 2026-09-04 | feat(evidencias): sesion de validacion WT-08 con usuario tecnico |
| `d9c0af7` | 2026-09-04 | feat(autoria): A10 firmado por los tres integrantes acreditados |
| `1d402fe` | 2026-09-04 | docs: cierre del examen final, version 2B-1.9.0 |
| `808b74f` | 2026-09-04 | feat(autoria): deposita la respuesta del docente sobre las firmas de A10 |
| `e1798b4` | 2026-09-04 | fix: corrige lo que los documentos afirmaban y ya no era cierto |
| `7924138` | 2026-09-04 | fix(publicacion): la amenaza T4 del manuscrito declaraba una carencia que ya no existe |
| `102f6aa` | 2026-09-04 | fix(ers): corrige RNF-04 y RNF-14 contra la evidencia de campo |
| `b115c5d` | 2026-09-04 | feat: deposita la caratula de identificacion y actualiza el enlace del contenedor |
| `883f3dc` | 2026-09-04 | feat(publicacion): enuncia RQ2, que el manuscrito ya respondia sin declararla |
| `6159a82` | 2026-09-04 | docs: la caratula cita el commit de la linea base |
| `1cf77f2` | 2026-09-04 | fix: la caratula cita la etiqueta y no un identificador de commit |
| `e19cab6` | 2026-09-04 | fix(ers): el cronograma declaraba pendiente lo que ya esta entregado |
| `0456ca4` | 2026-09-05 | docs(experimento): declara la desviacion del enfoque asignado y por que no se revierte |
| `24ca9a4` | 2026-09-05 | feat(evidencias): deposita las seis notas de campo manuscritas de la ronda terminal |
| `df6b687` | 2026-09-05 | feat(evidencias): deposita las seis notas de campo de entorno firmadas |
| `6ea0af3` | 2026-09-05 | feat(trazabilidad): mide la sincronizacion entre el tablero de gestion y la matriz |
| `216af76` | 2026-09-05 | docs(autoria): declara la asistencia recibida en el tablero de gestion |
| `4641739` | 2026-09-05 | feat(trazabilidad): deposita el tablero de gestion y su medicion de sincronizacion |
| `a5f9bad` | 2026-09-06 | feat(validacion): deposita la sesion WT-09 con el segundo usuario tecnico |
| `c1d4eab` | 2026-09-06 | feat(defensa): anade el bloque de verificacion, trazabilidad y campo, y pasa el mazo a tres integrantes |
| `0b6ff3f` | 2026-09-06 | docs(defensa): libreto de grabacion con el texto literal y el reparto a tres |
| `5ca9da4` | 2026-09-06 | feat(evidencias): registra el material de WT-09 y enlaza EV-27 con los requisitos que contrasto |
| `e52dfc2` | 2026-09-06 | fix(evidencias): retira la doble codificacion duplicada y sincroniza el PDF de la presentacion |
| `f302a61` | 2026-09-06 | docs(modelado): fija la correspondencia MU-01 a MU-04 y declara la fuente de Figma pendiente |
| `ff6c137` | 2026-09-06 | docs(evidencias): explicita el criterio de EXIF aplicado a las fotografias de entorno |
| `b52f462` | 2026-09-06 | feat(modelado): deposita el archivo fuente de Figma de los cuatro prototipos |
| `555b954` | 2026-09-06 | feat(etica): deposita el consentimiento de TIC-02 y corrige el tipo de sesion de los usuarios tecnicos |
| `a10787f` | 2026-09-06 | feat(experimento): deposita el panel ampliado y su diagnostico como hallazgo metodologico |
| `23d5354` | 2026-09-06 | docs(publicacion): reescribe la amenaza T2 con la evidencia de las dos vueltas del panel |
| `cb649b9` | 2026-09-06 | chore: actualiza el manifiesto de sumas de verificacion |
| `673a018` | 2026-09-06 | fix(etica): pone al dia las cifras del registro de consentimientos |
| `ec77bb8` | 2026-09-06 | feat(codificacion): codifica EV-20 y EV-21 de la ronda terminal |
| `75100d7` | 2026-09-06 | feat(saturacion): la curva satura con las dieciseis entrevistas, con su comprobacion de robustez |
| `fcb6b0f` | 2026-09-06 | docs: propaga la saturacion alcanzada al reporte, al manuscrito y al README |
| `d3b4fce` | 2026-09-06 | feat(datos): incorpora el panel ampliado al paquete de Zenodo y corrige el diccionario de datos |
| `0d12e89` | 2026-09-06 | chore(datos): apunta al DOI de la version publicada hoy en Zenodo |
| `b2fd799` | 2026-09-06 | fix(defensa): las diapositivas afirmaban lo que ya no es cierto |
| `17cf5a0` | 2026-09-06 | feat(trazabilidad): cierra el hueco de RD-01 en el tablero y en la matriz |
| `73df2c8` | 2026-09-06 | feat(publicacion): comprueba cada cifra afirmada contra la salida que la sostiene |
| `2223240` | 2026-09-07 | data(restringido): contenedor cifrado, fragmentos 1 a 55 de 272 |
| `c011d87` | 2026-09-07 | data(restringido): contenedor cifrado, fragmentos 56 a 110 de 272 |
| `b31d53b` | 2026-09-07 | data(restringido): contenedor cifrado, fragmentos 111 a 165 de 272 |
| `e612dbf` | 2026-09-07 | data(restringido): contenedor cifrado, fragmentos 166 a 220 de 272 |
| `5854089` | 2026-09-07 | data(restringido): contenedor cifrado, fragmentos 221 a 272 de 272 |
| `827f6f9` | 2026-09-07 | docs(datos): separa el DOI de concepto del DOI de version, y cierra la verificacion del contenedor |
| `eb74ac4` | 2026-09-07 | feat(evidencias): deposita el instrumento del cuestionario y pone al dia la tabla de ausencias |
| `4dc5f38` | 2026-09-07 | fix(ers): anade a Cedeno Avila a la caratula y regenera el PDF desde su fuente |
| `d927745` | 2026-09-07 | feat(fair): sustituye la autoevaluacion redactada a mano por la salida real de F-UJI |
| `b4b1375` | 2026-09-07 | chore(integridad): incorpora al manifiesto los tres archivos de la autoevaluacion FAIR |
| `66af0b2` | 2026-09-07 | feat(validacion): deposita la sesion WT-10 con el tercer usuario tecnico |
| `9ad7b68` | 2026-09-07 | fix(cifras): pone de acuerdo la matriz, el corpus y la censura con lo que dicen los scripts |
| `ef42d97` | 2026-09-07 | fix(publicacion): actualiza AFI-13 y regenera el manuscrito desde su fuente |
| `d0a8cda` | 2026-09-07 | docs(autoria): reejecuta la verificacion previa sobre un clon limpio de ef42d97 |
| `beec5b0` | 2026-09-07 | fix(raiz): retira un residuo y pone al dia las dos caratulas |
| `9e2dda3` | 2026-09-07 | chore(caratula): regenera la caratula sobre la linea base etiquetada |
| `d702848` | 2026-09-07 | fix(deposito): el DOI de version ya no dice corresponder al arbol actual |
| `a473f26` | 2026-09-07 | fix(experimento): el enfoque se elegia, y la declaracion confesaba una desviacion inexistente |
| `62f1dd8` | 2026-09-07 | fix(composicion): el SGA declara cinco integrantes, no cuatro |
| `b09f0d4` | 2026-09-07 | fix(defensa): la diapositiva 13 seguia contando nueve sesiones y dos tecnicas |
| `d651f7f` | 2026-09-07 | fix(panel): el liston de 0,41 no constaba en ningun sitio, y el paquete Zenodo iba desfasado |
| `b75e522` | 2026-09-08 | fix(defensa): el kappa de la doble codificacion estaba inflado, y el guion negaba la saturacion |
| `5ef9e8d` | 2026-09-08 | feat(evidencias): recupera el video de EV-16, deposita la solicitud firmada y da respaldo de campo a RNF-IA-03 |
| `e1c7fbe` | 2026-09-08 | feat(deposito): la version 2B-1.12.0 esta publicada en Zenodo |
| `2a26ce9` | 2026-09-08 | chore(contenedor): volumenes 055 a 108 del contenedor rehecho |
| `7c9625a` | 2026-09-08 | chore(contenedor): volumenes 109 a 162 del contenedor rehecho |
| `dc04e01` | 2026-09-08 | chore(contenedor): volumenes 163 a 216 del contenedor rehecho |
| `0426933` | 2026-09-08 | chore(contenedor): volumenes 217 a 270 del contenedor rehecho |
| `aa8a694` | 2026-09-08 | chore(contenedor): volumenes 271 a 316 del contenedor rehecho |
| `7df0eaa` | 2026-09-08 | chore(contenedor): volumenes 001 a 054 del contenedor rehecho |
| `81455e4` | 2026-09-08 | feat(restringido): el contenedor se rehace con los dos videos que faltaban |
| `c7c9a77` | 2026-09-08 | feat(defensa): libreto v2.0, una entrada por diapositiva, y la demo sobre la via verificada |
| `a194c26` | 2026-09-08 | fix(defensa): el grafico de participacion no seguia su escala y el libreto se elogiaba solo |
| `0f914b0` | 2026-09-08 | feat(defensa): la diapositiva 9 pasa a ser el paquete de replicacion y el deposito FAIR |
| `fc145fa` | 2026-09-09 | docs(defensa): las cifras del libreto pasan de letra a digito |
| `6bb3b08` | 2026-09-09 | docs(autoria): reejecuta la verificacion previa sobre el clon limpio de 298e28f |
| `32d4f49` | 2026-09-11 | docs(changelog): declara la linea base vigente 2B-final-v4.0 al tope del registro |
| `b9783c7` | 2026-09-11 | chore(integridad): regenera los manifiestos sobre la copia actualizada |
| `25ba498` | 2026-09-12 | fix(ers): el ERS en A4 ya no desborda la caja de texto |
| `db71b2a` | 2026-09-12 | fix(etica): quema las cedulas de los PDF de etica y declara el tratamiento de datos |
| `52713e9` | 2026-09-12 | feat(datos): la orden unica de 07_Datos regenera tambien las tablas y figuras del documento |
| `814d45d` | 2026-09-12 | fix(publicacion): el manuscrito ya no presenta el 0,41 como umbral pactado |
| `e13df21` | 2026-09-12 | fix(autoria): la declaracion de uso de IA cuadra con el repositorio |
| `3080481` | 2026-09-12 | docs: declara la linea base 2B-final-v5.0 y pone al dia README y CHANGELOG |
| `0578810` | 2026-09-12 | chore(autoria): regenera la bitacora, el aporte individual y el manifiesto sobre el historial al dia |
| `3530bb2` | 2026-09-12 | docs(autoria): verificacion previa sobre el clon limpio de 0578810 y caratula de la linea base v5.0 |
| `6ae4e9e` | 2026-09-12 | feat(autoria): deposita el aporte individual y la verificacion previa firmados el 2026-09-12 |
| `09edc04` | 2026-09-12 | chore(caratula): regenera la caratula sobre la linea base 2B-final-v5.1 |
| `1f05c14` | 2026-09-12 | fix(autoria): la comprobacion P4 se ejecuta, la declaracion de IA cubre todo el 12 de septiembre y el README lista todos los paquetes |
| `13dd0af` | 2026-09-12 | feat(trazabilidad): cierra 18 filas de la matriz con las historias HU-22 a HU-38 |
| `107433f` | 2026-09-12 | docs(composicion): declara retirados a Mendoza Palma y Gilces Carranza en todo el repositorio |
| `d074c6b` | 2026-09-12 | feat(experimento): deposita el registro integro de la generacion del Conjunto A |
| `b082104` | 2026-09-12 | fix(datos): la orden unica deposita las tablas y figuras del documento dentro de 07_Datos |
| `6be559a` | 2026-09-13 | fix(consistencia): textos al dia en reporte, zona restringida, defensa y declaracion de IA |

---

## Yeranick Esther Munoz Quinonez

**Rol:** Documentacion, trazabilidad, auditoria de calidad y gestion de evidencias

**Confirmaciones: 114**, de 2026-08-30 a 2026-09-14.

### Areas sobre las que trabajo

| Area | Archivos tocados |
|---|---|
| Evidencia de campo y etica | 202 |
| Documentos de raiz | 96 |
| Evidencia de autoria | 79 |
| Producto minimo viable | 43 |
| Componente empirico | 38 |
| Manuscrito y deposito | 36 |
| Paquete de datos | 30 |
| Otros | 25 |
| Trazabilidad | 22 |
| Especificacion de requisitos | 18 |
| Modelado UML e i* | 7 |
| Defensa | 5 |

### Confirmaciones

| Commit | Fecha | Aporte |
|---|---|---|
| `1499dd9` | 2026-08-30 | data: agrega las transcripciones anonimizadas de las diez entrevistas |
| `ef5cf3d` | 2026-08-30 | data: agrega los diez registros de audio de entrevista en MP3 a 128 kbps |
| `4d88a4d` | 2026-08-30 | data: agrega los videos de entrevista de la primera ronda de campo |
| `e99b1ab` | 2026-08-30 | data: agrega los videos de entrevista de la segunda ronda de campo |
| `0a2ccd3` | 2026-08-30 | data: agrega los diez consentimientos informados enmascarados |
| `507c475` | 2026-08-30 | data: agrega la ficha tecnica de la evidencia audiovisual con sus hashes |
| `0f1b8af` | 2026-08-30 | data: agrega el cuestionario aplicado con sus sesenta respuestas |
| `ab0a112` | 2026-08-30 | data: agrega las fotografias del entorno operativo del cliente |
| `4cf6593` | 2026-08-30 | data: agrega los documentos originales de la organizacion cliente |
| `cdf3346` | 2026-08-30 | data: agrega la codificacion tematica de las transcripciones |
| `cd15418` | 2026-08-30 | feat: agrega el guion de validacion para participante no tecnico |
| `6379b69` | 2026-08-30 | data: agrega las actas de las sesiones de validacion enmascaradas |
| `e440b67` | 2026-08-30 | docs: agrega el paquete de anexos eticos del proyecto |
| `e35c9fe` | 2026-08-30 | docs: agrega los anexos de categoria B y la declaracion de uso de IA |
| `6603e61` | 2026-08-30 | fix(ers): unifica los identificadores en RNF- y delimita RF-13 frente a RF-16 |
| `2d9c602` | 2026-08-30 | feat(replicacion): anade replicar.py, el pipeline en una orden sin GNU Make |
| `0fe13ae` | 2026-08-30 | docs(citacion): declara el identificador persistente del deposito en CITATION.cff |
| `7dae4d5` | 2026-08-30 | docs(readme): retira del arbol las carpetas sin contenido y declara su ausencia |
| `82b102d` | 2026-08-30 | chore(integridad): regenera el manifiesto de sumas sobre las 248 entradas |
| `4ffb70a` | 2026-08-30 | docs(changelog): registra la consolidacion 2B-1.1.0 |
| `5851996` | 2026-08-30 | fix(ers): hace comprobable el criterio de aceptacion de RF-14 |
| `d87bc43` | 2026-08-30 | docs(auditoria): recalcula completitud, verificabilidad y consistencia |
| `06ce54e` | 2026-08-31 | fix(experimento): traslada y renombra la tabla de desciego de items |
| `e6cea7e` | 2026-08-31 | docs(experimento): documenta la desviacion de la clave de desciego |
| `b33e130` | 2026-08-31 | docs(readme): declara la tabla de desciego en su nueva ubicacion |
| `012ba1e` | 2026-08-31 | chore(integridad): regenera el manifiesto tras el traslado de la clave |
| `a663650` | 2026-08-31 | docs(changelog): registra las correcciones 2B-1.2.0 |
| `5800f35` | 2026-08-31 | docs(experimento): deposita el comprobante del registro previo en PDF |
| `afc0930` | 2026-08-31 | data(experimento): deposita la evidencia verificable del registro previo |
| `2ef0e9b` | 2026-08-31 | docs(experimento): corrige el estado del registro previo |
| `d214866` | 2026-08-31 | chore(integridad): extiende el manifiesto de sumas a los archivos zip |
| `dc1978b` | 2026-08-31 | docs(changelog): registra la version 2B-1.3.0 |
| `b4faffe` | 2026-08-31 | chore(integridad): extiende el manifiesto de sumas a los archivos xml |
| `1e68dda` | 2026-08-31 | fix(trazabilidad): corrige los enlaces rotos de la matriz y completa su cadena |
| `5804479` | 2026-08-31 | docs(trazabilidad): lista los huerfanos y las cadenas rotas con causa y accion |
| `dd1d07e` | 2026-08-31 | docs(auditoria): recalcula la trazabilidad tras completar la matriz |
| `49fc9ad` | 2026-08-31 | docs(aporte): rehace la declaracion de aporte sobre el historial real |
| `b32ef2d` | 2026-08-31 | docs(experimento): cierra las dos comprobaciones sobre el repositorio 2A |
| `ab6977d` | 2026-08-31 | chore(integridad): regenera el manifiesto tras completar la trazabilidad |
| `dd4abe4` | 2026-08-31 | docs(changelog): registra la version 2B-1.4.0 |
| `d42ba84` | 2026-09-01 | feat(evidencias): deposita once fotografias de entorno con su inventario |
| `5a60692` | 2026-09-01 | refactor(evidencias): pasa las transcripciones a Markdown estructurado |
| `5ca4257` | 2026-09-01 | refactor(evidencias): reubica etica, validacion y codificacion tematica |
| `c1b217d` | 2026-09-01 | docs(trazabilidad): declara la composicion real del equipo y rehace el aporte |
| `1518546` | 2026-09-01 | docs(auditoria): publica el par de valores antes y despues de las seis metricas |
| `96999d9` | 2026-09-01 | chore(integridad): cierra el deposito FAIR y regenera el manifiesto |
| `572513f` | 2026-09-01 | docs(changelog): registra las versiones 2B-1.5.0 y 2B-1.6.0 |
| `27e8adf` | 2026-09-01 | docs(trazabilidad): actualiza la declaracion de aporte al historial completo |
| `3e3de2b` | 2026-09-01 | feat(modelado): deposita los diagramas de flujo de datos de nivel 0 y 1 |
| `9619d02` | 2026-09-01 | docs(evidencias): documenta las carpetas declaradas y su estado real |
| `f4e63e0` | 2026-09-01 | docs(readme): corrige la fila de los DFD, que ya estan depositados |
| `023f745` | 2026-09-01 | fix(integridad): entrega los archivos de texto sin normalizar el fin de linea |
| `c76db09` | 2026-09-01 | chore(integridad): regenera el manifiesto sobre el arbol completo |
| `bbe5c87` | 2026-09-01 | fix(integridad): extiende la regla de no normalizar a todo el arbol |
| `84921aa` | 2026-09-01 | docs(trazabilidad): actualiza la declaracion de aporte al historial vigente |
| `998ab45` | 2026-09-03 | feat(evidencias): sustituye las fotografias de entorno sin metadato verificable |
| `88bb1fd` | 2026-09-03 | feat(evidencias): deposita los seis consentimientos de la ronda terminal |
| `076b392` | 2026-09-03 | feat(autoria): deposita la correspondencia de coordinacion, elemento A8 |
| `f889afc` | 2026-09-04 | feat(autoria): deposita las dos grabaciones de sesion, elemento A4 |
| `328499a` | 2026-09-04 | feat(autoria): deposita las notas de campo y la primera tanda de capturas |
| `f3fa233` | 2026-09-04 | feat(autoria): manifiesto por script, acuerdo de A7 y declaracion al dia |
| `14436bc` | 2026-09-04 | docs(trazabilidad): el recuento por autor deja de declarar cero para el tercero |
| `b92bc5d` | 2026-09-04 | docs(evidencias): declara las doce grabaciones de la ronda terminal |
| `be0dc83` | 2026-09-04 | fix(autoria): el instructivo de A2 pedia usuarios de Git que no existen |
| `4010c12` | 2026-09-04 | feat(autoria): A7 completo, con las dos codificaciones y su acuerdo |
| `c4c695a` | 2026-09-04 | feat(autoria): A2 completo, tres capturas por cada integrante |
| `17ceb08` | 2026-09-04 | feat(evidencias): dos documentos mas de la organizacion; se pasa de cuatro a seis |
| `c13ac7f` | 2026-09-04 | feat(evidencias): las dos actas que faltaban, firmadas; ocho sesiones en total |
| `2fded58` | 2026-09-04 | docs(autoria): la lista de verificacion previa, reejecutada sobre clon limpio |
| `1e67a87` | 2026-09-04 | fix(evidencias): enmascara el nombre y la firma de TIC-01 en el acta WT-08 |
| `928dded` | 2026-09-04 | fix(evidencias): el registro de anonimizacion no recogia el trabajo del 3 y 4 de septiembre |
| `66d717f` | 2026-09-04 | fix(evidencias): el recuento de consentimientos iba uno por detras |
| `77c0916` | 2026-09-04 | docs(autoria): la lista de verificacion declara que version comprueba |
| `c5ac738` | 2026-09-04 | docs(trazabilidad): declara que cuenta como fila cerrada, y con que cifra |
| `707db7a` | 2026-09-04 | feat(trazabilidad): la columna de estado se comprueba por script, y sube a 41 |
| `ec057fc` | 2026-09-04 | docs(defensa): el banco de preguntas cubre la ronda terminal |
| `4e8d2c2` | 2026-09-04 | fix(evidencias): la ficha tecnica omitia el video de la sesion de member checking |
| `fd16b5e` | 2026-09-06 | fix(consistencia): corrige rutas movidas, identificadores repetidos y cifras desfasadas |
| `cea459e` | 2026-09-06 | fix(consistencia): retira duplicados, consolida el registro previo y pone al dia el CHANGELOG |
| `6e8ea63` | 2026-09-06 | feat(codificacion): codifica EV-22 y EV-23 de la ronda terminal |
| `0f8338f` | 2026-09-06 | fix(datos): traduce las rutas de correspondencia_salidas.csv a la estructura del paquete |
| `1bb3761` | 2026-09-06 | docs(trazabilidad): declara las siete restricciones de diseno que no estan en la matriz |
| `4650019` | 2026-09-07 | docs(trazabilidad): regenera el aporte individual y ata el anexo de correspondencia a su verificador |
| `fdf0eb8` | 2026-09-14 | fix(analisis): el tamano del efecto se calcula con el requisito como unidad y deja de remuestrear tres jueces |
| `71c0725` | 2026-09-14 | docs(desviaciones): declara la desviacion 7, el tamano del efecto con el requisito como unidad |
| `0ea6784` | 2026-09-14 | docs(reporte): la magnitud del efecto se presenta con el requisito como unidad y retira los intervalos sobre tres jueces |
| `159446d` | 2026-09-14 | docs(manuscrito): efectos con el requisito como unidad y cuarta desviacion declarada |
| `2136f2c` | 2026-09-14 | fix(afirmaciones): las cifras del tamano del efecto se comprueban contra el nuevo calculo |
| `3f3c4da` | 2026-09-14 | feat(datos): la cadena de analisis y sus entradas crudas se depositan dentro de 07_Datos |
| `05f4c56` | 2026-09-14 | refactor(datos): la etapa analisis ejecuta la cadena desde 07_Datos sin pasar por 06_Experimento |
| `d1429d8` | 2026-09-14 | docs(reporte): incluye tablas y figuras desde 07_Datos/resultados y corrige negritas y rutas que se veian rotas en el PDF |
| `d68cc27` | 2026-09-14 | docs(manuscrito): incluye tablas y figuras desde 07_Datos/resultados |
| `6aa6a44` | 2026-09-14 | docs(datos): README y README_datos describen la cadena de analisis dentro de 07_Datos |
| `cecdd45` | 2026-09-14 | docs(manuscrito): condensa la redaccion de los efectos para mantener el limite de 15 paginas de REFSQ |
| `402fab3` | 2026-09-14 | docs(autoria): declara la asistencia recibida en las correcciones del 14 de septiembre |
| `e72cb48` | 2026-09-14 | chore(cierre): CHANGELOG 2B-1.18.0, README y portada del ERS para 2B-final-v5.8, y manifiestos de sumas al dia |
| `119d5c2` | 2026-09-14 | docs(autoria): declara que el asistente ejecuto las confirmaciones de este tramo |
| `8b9e4e5` | 2026-09-14 | feat(efectos): efectos.csv declara n_pares e interpretable y la orden unica responde tambien como run_all.py |
| `8edb271` | 2026-09-14 | docs(identificacion): la URL del repositorio y la de la entrega 2A apuntan al nuevo propietario |
| `c508399` | 2026-09-14 | docs(documentos): reporte, ERS y manuscrito recogen la tabla de efectos con pares e interpretabilidad y se recompilan |
| `b67c38d` | 2026-09-14 | feat(autoria): notas de campo con el nombre de la guia y sesiones de elicitacion en la bitacora con su nota o su motivo |
| `44cc1f0` | 2026-09-14 | docs(autoria): declara la asistencia y las confirmaciones del trabajo de cierre |
| `f429a85` | 2026-09-14 | feat(autoria): la bitacora declara que TIC-01 a TIC-03 no tienen nota de campo y remite a su acta firmada |
| `fc93821` | 2026-09-14 | docs(reporte): la retrospectiva recoge las observaciones del docente de los informes del 5 y el 14 de septiembre y su resolucion |
| `0e36817` | 2026-09-14 | chore(cierre): CHANGELOG 2B-1.19.0 y README con la linea base 2B-final-v5.8 de la guia de cierre |
| `3d0f2b6` | 2026-09-14 | chore(cierre): caratula para 2B-final-v5.8, bitacora regenerada y manifiesto de sumas al dia |
| `5ec910f` | 2026-09-14 | fix(manuscrito): elimina los desbordes de linea en rutas, en la tabla de trabajos relacionados y en el resumen, sin cambiar el texto |
| `b9fd4db` | 2026-09-14 | fix(manuscrito): el apartado de uso de IA deja de afirmar parametros de generacion que el registro declara no disponibles |
| `18bb4eb` | 2026-09-14 | chore(cierre): caratula, bitacora y manifiesto de sumas sobre el manuscrito corregido |
| `1786a01` | 2026-09-14 | docs(changelog): registra en 2B-1.19.0 las correcciones del manuscrito |
| `01db1c4` | 2026-09-14 | chore(autoria): pone al dia el aporte individual con el historial del cierre, listo para firmar |
| `a0f85d3` | 2026-09-14 | docs(reporte): declara 2B-final-v5.8 como linea base vigente y deja de fijar a mano el numero de sumas del manifiesto |
| `0a01de1` | 2026-09-14 | docs(autoria): el indice de A5 remite al nombre de las notas y a los motivos declarados en la bitacora |
| `8d0a321` | 2026-09-14 | chore(cierre): bitacora, caratula y manifiesto de sumas sobre la version auditada contra la guia de cierre |

---

## Winston Damian Cedeno Avila

**Rol:** Transcripcion y anonimizacion del corpus de entrevistas

**Confirmaciones: 12**, de 2026-09-04 a 2026-09-09.

### Areas sobre las que trabajo

| Area | Archivos tocados |
|---|---|
| Evidencia de campo y etica | 33 |
| Documentos de raiz | 9 |
| Evidencia de autoria | 9 |
| Defensa | 2 |
| Especificacion de requisitos | 1 |
| Trazabilidad | 1 |

### Confirmaciones

| Commit | Fecha | Aporte |
|---|---|---|
| `ea08aba` | 2026-09-04 | feat(evidencias): transcribe y anonimiza EV-20 y EV-21 con control de calidad |
| `d79c879` | 2026-09-04 | feat(evidencias): completa las seis transcripciones de la ronda terminal |
| `d0a3138` | 2026-09-04 | feat(evidencias): validacion e incorporacion de la codificacion tematica |
| `cf79792` | 2026-09-04 | feat(autoria): cuatro capturas mas de A2; dos integrantes llegan al minimo |
| `dd6fa4d` | 2026-09-04 | docs(autoria): lista de verificacion previa firmada por dos integrantes |
| `8fcdc7f` | 2026-09-04 | docs(autoria): lista de verificacion firmada sobre la version entregada |
| `9e549a6` | 2026-09-05 | feat(evidencias): deposita la doble codificacion A7 y su coeficiente de acuerdo |
| `8a1429e` | 2026-09-06 | feat(validacion): deposita INS-01, REINS-01, el comite CCB-01 y la retrospectiva |
| `f3334b8` | 2026-09-06 | feat(codificacion): codifica EV-24 y EV-25 y cierra el corpus al 100 por ciento |
| `3eda626` | 2026-09-09 | feat(evidencias): transcribe y anonimiza las tres sesiones tecnicas, EV-26, EV-27 y EV-28 |
| `aed73c3` | 2026-09-09 | chore(integridad): incorpora al manifiesto las tres transcripciones tecnicas |
| `298e28f` | 2026-09-09 | feat(defensa): deposita la defensa grabada a tres voces |

---

## Firmas

Cada integrante firma declarando que el aporte que consta arriba a su nombre es suyo,
y que no reclama trabajo de otra persona.


**Gary Alberto Sanchez Cornejo**

Firma: ______________________________    Fecha: ______________


**Yeranick Esther Munoz Quinonez**

Firma: ______________________________    Fecha: ______________


**Winston Damian Cedeno Avila**

Firma: ______________________________    Fecha: ______________

---

Generado el 2026-09-14 desde el historial del repositorio.
