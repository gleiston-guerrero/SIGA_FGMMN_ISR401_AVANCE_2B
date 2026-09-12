# Banco de preguntas del tribunal

Proyecto SIGA · ISR-401 · Equipo FGMMN · Universidad Tecnica Estatal de Quevedo
Version 1.1 · 2026-09-04

Una respuesta por pregunta del temario. **Cada respuesta senala el artefacto que la
respalda**, porque la guia evalua que las respuestas se anclen en artefactos concretos y no
en opiniones.

---

## A. Sistema, dominio y partes interesadas

**A1. ¿Que problema real resuelve SIGA y para quien?**
Gestion de aulas en la Facultad de Ciencias de la Computacion de la UTEQ: hoy la deteccion
de un aire acondicionado danado o un proyector sin senal depende de que alguien pase por el
aula y avise. SIGA monitorea, alerta y gestiona el ticket.
→ `02_Evidencias/Transcripciones/`, EV-01 (CONS-01); `02_Evidencias/Documentos_Organizacion/`

**A2. ¿Como saben que el problema existe y no lo supusieron?**
De **dieciseis entrevistas** con tres perfiles distintos. **Diez estan codificadas**, en
36 fragmentos con su categoria y el requisito que derivan; las seis de la ronda terminal
del 2026-09-03 estan transcritas y su codificacion queda pendiente. Si insisten con la
cifra, la respuesta exacta es: dieciseis recogidas, diez analizadas.
→ `02_Evidencias/Codificacion_Tematica/codificacion_tematica.csv`

**A3. ¿Quienes son los usuarios y como se eligieron?**
Docencia (DOC), coordinacion academica (COORD) y conserjeria e infraestructura (CONS). Son
los tres perfiles que intervienen en el ciclo de vida de una falla de aula.
→ `03_Modelado/02_iStar_SD/`, `01_ERS/` seccion de actores

**A4. ¿Que documentos de la organizacion consultaron?**
Seis: estatuto de la UTEQ, codigo de etica, reglamento de vinculacion, horario academico,
horario de laboratorios --el artefacto con el que RNF-08 exige integrarse-- y la ficha de
registro de practicas de laboratorio, que acredita por escrito que el control de uso se
lleva en papel y con firma manuscrita.
→ `02_Evidencias/Documentos_Organizacion/`

---

## B. Especificacion

**B1. ¿Cuantos requisitos hay y como se garantiza que estan completos?**
25 funcionales con ocho atributos y 16 no funcionales cuantificados sobre ISO/IEC
25010:2023. Completitud medida: **100 %**, 25 de 25. Antes de la auditoria era 96 %; el requisito que faltaba se corrigio y la metrica esta recalculada.
→ `01_ERS/ERS_SRS_2B_v2.0.pdf`; `01_ERS/Auditoria_Calidad/auditoria_calidad_especificacion.md`

**B2. Deme un requisito no funcional y su forma de comprobarlo.**
RNF-01: las alertas de anomalia se entregan en ≤ 60 s desde la deteccion. Se comprueba con
prueba de carga sobre 50 aulas simuladas midiendo el tiempo real de entrega.
→ `01_ERS/`, tabla de requisitos no funcionales

**B3. ¿Algun requisito no es verificable?**
Si, uno: RF-14 pide recomendaciones «diferenciadas y **coherentes**». Diferenciadas es
observable; coherentes no tiene metrica. Esta identificado como defecto y tiene accion de
mejora.
→ `01_ERS/Auditoria_Calidad/auditoria_calidad_especificacion.md`, seccion 4

**B4. ¿Hay requisitos en conflicto?**
Uno abierto: RF-13 y RF-16 apagan ambos equipos de aulas desocupadas fuera de horario, los
dos con umbral ≤ 2 minutos. Se resuelve fusionandolos o delimitando su alcance.
→ misma auditoria, seccion 3

**B5. ¿Como mapearon los requisitos legales?**
Articulo por articulo en la matriz, columnas `Ley` y `Articulo`. RF-24 y RF-25 derivan de
los derechos de exportacion y rectificacion de la Ley Organica de Proteccion de Datos
Personales.
→ `04_Trazabilidad/matriz_trazabilidad.csv`

---

## C. Modelado y trazabilidad

**C1. ¿Que garantiza que los diagramas los hicieron ustedes?**
Cada diagrama se entrega con su archivo fuente nativo: `.vpp` de Visual Paradigm y
`.drawio` para los modelos iStar, junto a las exportaciones.
→ `03_Modelado/`

**C2. Tome un requisito y traceelo de punta a punta.**
RF-01 nace de EV-01, se realiza en CU-01 y CU-03, lo soporta el prototipo MU-01 y lo
implementan los componentes SensorIoT y LecturaSensor.
→ `04_Trazabilidad/matriz_trazabilidad.csv`, fila 1

**C3. ¿Su matriz esta completa?**
Completa en filas, no en cadenas, y conviene decirlo en ese orden. Son **75 filas** sobre
las **60** que pide el criterio, con **cero celdas vacias** y las cuatro columnas que
faltaban -clase, proceso, caso de prueba y estado de la traza- ya anadidas: la matriz paso
de 13 a 18 columnas. El **100 %** de los requisitos funcionales, 25 de 25, tiene la cadena hacia
adelante completa; antes era 12 de 25.

Ahora la parte incomoda, por si la preguntan: de las 75 filas, **59 cierran la cadena
entera**. Las otras 16 no se esconden, se clasifican: **nueve huerfanas** -el requisito nace
de la ley, no de una entrevista-, **una parcial** y **seis restricciones de diseno**
con algun eslabon que no aplica, porque se verifican por revision y no por caso de prueba.
Cada una con su causa y su accion, y la cifra se recalcula con
`python 04_Trazabilidad/verificar_matriz.py`.

Las ocho ultimas filas son los requisitos no funcionales del componente inteligente,
RNF-IA-01 a RNF-IA-08. Antes el componente de IA estaba descrito en el texto pero no
especificado como requisito: la palabra monitoreo aparecia 41 veces en el ERS y no habia
un solo umbral asociado. Ahora cada uno tiene metrica, unidad, umbral, metodo de
verificacion, responsable y frecuencia, y esta en la matriz con su elemento de diseno y su
caso de prueba.
→ auditoria de calidad, seccion 5

**C3b. Su matriz cita casos de prueba. ¿Donde estan?**
Definidos, y hasta el 3 de septiembre no lo estaban: la columna citaba cuarenta y nueve
identificadores que no correspondian a ningun documento. Lo encontramos nosotros al auditar
la matriz contra el arbol, y esta corregido en `04_Trazabilidad/casos_prueba.csv`.

Cada caso lleva objetivo, precondicion, procedimiento, resultado esperado y el criterio de
aceptacion Gherkin que decide si pasa. El catalogo se genera con un script que **falla** si
la correspondencia con la matriz se rompe en cualquiera de los dos sentidos, de modo que no
puede volver a desincronizarse sin que alguien lo note.

Y una precision que conviene decir antes de que la pregunten: **ninguno se presenta como
ejecutado**. Dieciocho son ejecutables hoy sobre el prototipo, porque el MVP implementa el
requisito; los otros treinta y uno exigen un sistema desplegado. Un catalogo de casos de
prueba es especificacion, no informe de ejecucion.
→ `04_Trazabilidad/README_casos_prueba.md`

**C4. ¿Que pasa si cambia un requisito?**
Afecta en promedio a 5 requisitos, medido sobre cinco casos representativos. El nodo mas
acoplado es RF-23, la bitacora, porque registra las acciones de siete requisitos.
→ auditoria de calidad, seccion 6

---

## D. Componente empirico

**D1. ¿Cual es la pregunta de investigacion?**
En que dimensiones de calidad difieren los requisitos funcionales elicitados por analistas
humanos frente a los generados por un modelo de lenguaje, a partir del mismo corpus de
entrevistas.
→ `06_Experimento/protocolo/protocolo.pdf`

**D2. ¿Como evitaron sesgar la evaluacion?**
Paquete ciego: los 51 items se presentan con identificador ciego y orden aleatorizado, sin
indicar origen. Los tres jueces son independientes y ninguno es participante del estudio.
→ `06_Experimento/instrumentos/Paquete_Evaluacion_Ciega_Jueces.md`

**D3. ¿Cual es el acuerdo entre evaluadores?**
Kappa de Fleiss entre 0,29 y 0,34 segun la dimension. En la escala de Landis y Koch es
acuerdo **justo**, y asi se reporta: no se presenta como bueno.
→ `06_Experimento/resultados/acuerdo_interevaluador.csv`

**D4. ¿Que resultados obtuvieron?**
Ninguno significativo tras la correccion de Holm-Bonferroni. La unica dimension con p por
debajo de 0,05 sin corregir, consistencia interna, sube a 0,059 al corregir.
→ `06_Experimento/resultados/hipotesis.csv`

**D5. ¿Y el tamano del efecto?**
Reportado con intervalo de confianza al 95 % por bootstrap de 10 000 replicas y semilla
fija. Los intervalos son muy anchos y cruzan el cero, que es lo esperable con esta potencia.
→ `06_Experimento/resultados/efectos.csv`

**D6. ¿Por que la muestra es tan pequena?**
El calculo de potencia lo cuantifica: para detectar d = 0,50 con alfa 0,05 y potencia 0,80
harian falta 34 unidades y hay 3. La potencia alcanzada es del **8,4 %** con el juez como
unidad de analisis. El analisis de sensibilidad por item, declarado como exploratorio y
posterior al registro, la sube a **41,7 %** con 25 y 26 observaciones. **Las dos
aproximaciones coinciden en el resultado**: ninguna dimension es significativa tras Holm.
Y 41,7 % sigue por debajo del 80 % convencional. Se declara como limitacion central, no se
disimula.
→ `06_Experimento/resultados/power_calculation.csv`

**D7. ¿Alcanzaron saturacion tematica?**
Si, con las dieciseis entrevistas codificadas: el promedio de codigos nuevos de las tres
ultimas es 1,333 frente a un umbral de 2,50. Con solo diez no saturaba, y la causa no era el
corpus sino el libro de codigos --- 36 codigos para 36 fragmentos, uno por uno, con lo que la
curva no puede aplanarse a ningun tamano. Al codificar las seis restantes contra el libro
existente pasa a 2,72 fragmentos por codigo.
Se comprobo que no depende del orden: las seis ultimas son del mismo dia, y el criterio
aguanta las 720 ordenaciones posibles (`robustez_saturacion.py`).
Las dos reservas se declaran: las instrucciones pedian reutilizar codigos, lo que empuja
hacia este resultado, y las seis nuevas son todas de docentes.
→ `07_Publicacion/tablas/saturacion_por_entrevista.csv`, `07_Publicacion/figuras/curva_saturacion.png`

**D8. ¿Como se que las cifras del reporte no estan escritas a mano?**
Porque se regeneran. `cd 06_Experimento && make all` reconstruye las cuatro figuras y las
cinco tablas desde los datos crudos, y la correspondencia entre cada salida y su script
esta declarada.
→ `07_Publicacion/dataset_zenodo/correspondencia_salidas.csv`

**D9. ¿Se desviaron del protocolo?**
Si, y estan documentadas con fecha, desviacion y motivo.
→ `06_Experimento/registro_previo/bitacora_desviaciones.pdf`

---

## E. Etica y datos

**E1. ¿Como protegieron a los participantes?**
Consentimiento informado firmado por cada uno, sustitucion de nombres por codigo, y
material audiovisual fuera de la zona publica. Un participante retiro su consentimiento y
su entrevista completa se elimino.
→ `02_Evidencias/Consentimientos/`, `07_Publicacion/dataset_zenodo/anonimizacion.md`

**E2. ¿Que hicieron con la entrevista retirada?**
EV-15 (DOC-03) se excluyo integramente. Ningun fragmento suyo consta en el corpus, ni en
la codificacion, ni en el material fuente del componente empirico.
→ purga registrada en el commit `639bea4`

**E3. ¿Cual es la base legal del tratamiento?**
Consentimiento informado para los datos de campo. Para los datos operativos del sistema,
mision de interes publico de la institucion educativa, conforme a la Ley Organica de
Proteccion de Datos Personales.
→ `02_Evidencias/Etica/`, `01_ERS/Componentes_IA/ficha_RF-09_analisis_predictivo_fallos.md` seccion 6

**E4. ¿Usaron inteligencia artificial? ¿Para que?**
En dos capacidades separadas: como **objeto de estudio**, generando el Conjunto A; y como
**apoyo de redaccion** sobre contenido del equipo. Las secciones evaluativas son produccion
propia. Declarado seccion por seccion.
→ `10_Autoria/declaracion_uso_ia.md`

---

## F. Componentes de inteligencia artificial

**F1. ¿Que partes de SIGA son inteligencia artificial?**
Una sola: RF-09, el analisis predictivo de fallos. RF-03 detecta ocupacion con un umbral
determinista sobre un sensor de presencia, y por definicion no es un sistema de IA.
→ `01_ERS/Componentes_IA/clasificacion_riesgo_ia.md`, seccion 1

**F2. ¿Que riesgo tiene ese componente?**
Riesgo minimo. El analisis descarta una a una las cuatro hipotesis educativas del Anexo III
del Reglamento (UE) 2024/1689: RF-09 no decide sobre admision, no evalua aprendizaje, no
determina nivel educativo y no vigila examenes. Predice el fallo de un equipo.
→ misma clasificacion, seccion 2

**F3. ¿Como se explica una prediccion a quien no es tecnico?**
Las tres variables que mas pesaron, en lenguaje llano, maximo 60 palabras, en menos de 2
segundos y sin que haya que pedirla. Se valida con una prueba de comprension: 4 de 5
participantes no tecnicos deben explicarla con sus palabras.
→ ficha RF-09, seccion 5

**F4. ¿Que pasa si el modelo trata peor a unas aulas que a otras?**
Tres requisitos de equidad lo miden: brecha de sensibilidad entre bloques edilicios, brecha
de falsos negativos por antiguedad del equipo y brecha de cobertura por ocupacion. Si
alguna supera su umbral, **el componente no se despliega**.
→ ficha RF-09, seccion 4

---

## G. Gestion, repositorio y aporte

**G1. ¿Como se verifica quien hizo que?**
Cada fila de la declaracion de aporte cita el identificador del commit que la respalda, con
el repositorio donde se resuelve.
→ `04_Trazabilidad/aporte_individual.csv`

**G2. Como se reparte el trabajo entre los integrantes?**
Entre los tres integrantes activos, y el historial lo muestra con correo institucional:
Sanchez Cornejo, Munoz Quinonez y Cedeno Avila son los unicos autores. El recuento vigente
esta en `04_Trazabilidad/composicion_equipo.md`.
La declaracion de aporte tiene una fila por commit, cada una con su identificador, y todas
resuelven.

El equipo son hoy **tres**: Cedeno Avila, Winston Damian se reincorporo el 2026-09-02 y
asume la transcripcion y anonimizacion del corpus de la ronda terminal. Sus confirmaciones
empiezan con ese trabajo, y hasta que existan la declaracion muestra su recuento en cero en
lugar de atribuirle una contribucion que el historial todavia no respalda. Mendoza Palma,
Allan Jeremy y Gilces Carranza, Jose Ignacio, que figuran en el grupo del SGA, estan
retirados del equipo: no produjeron artefactos ni commits y no se les atribuye trabajo.
-> `04_Trazabilidad/aporte_individual.csv` y `04_Trazabilidad/composicion_equipo.md`

**G2b. El registro previo en OSF declara mas personas de las que firman. Por que?**
Porque el protocolo se preregistro cuando el equipo era mayor. La lista de contribuyentes se
actualizo despues a la composicion vigente, y ambas cosas se declaran en lugar de ocultarse.
Lo que un registro OSF congela es el contenido registrado, que es lo que sostiene la marca
temporal frente al p-hacking, no la lista de personas.
-> `04_Trazabilidad/composicion_equipo.md`

**G3. ¿Como reproduzco su documento?**
Clonando el repositorio y ejecutando la secuencia de cuatro pasos del README: pdflatex,
bibtex, pdflatex, pdflatex.
→ `README.md`, apartado 4

**G4. ¿Como se que la evidencia no fue sustituida?**
`sha256sum -c checksums.sha256` comprueba sin error sobre un clon limpio, y cada archivo
multimedia tiene su hash en la ficha tecnica.
→ `checksums.sha256`, `02_Evidencias/00_Restringido/fichas_tecnicas.csv`

---

## H. Las preguntas incomodas

**H1. Si su estudio no encontro nada significativo, ¿de que sirve?**
De reportar un resultado nulo bien medido en lugar de uno significativo mal medido. El
estudio cuantifica su propia potencia, declara que es insuficiente y deja el pipeline
reproducible para que ampliar la muestra sea ejecutar una orden. Ocultarlo habria sido lo
facil.

**H2. ¿No es un problema que el mismo equipo elicitara los requisitos y evaluara la calidad?**
Si, y es una amenaza a la validez declarada. Se mitigo con evaluacion ciega por jueces
independientes que no participaron en la elicitacion. La limitacion remanente es que el
material fuente lo preparo el equipo.
→ reporte, seccion de amenazas a la validez

**H3. ¿Cuantas entrevistas deberian haber hecho?**
Mas. El cierre en 10 fue autorizado por el docente ante la restriccion de calendario, y la
consecuencia sobre la saturacion y la potencia esta cuantificada y declarada. No se
presenta como suficiente: se presenta como lo que fue.

**H4. ¿Que harian distinto si empezaran de nuevo?**
Tres cosas: llevar la unidad de analisis al item en lugar del juez, que multiplicaria la
potencia sin recolectar mas datos; registrar el protocolo antes de tocar ningun dato; y
documentar las dependencias entre requisitos desde la primera version, porque su ausencia
hizo que la especificacion aparentara un acoplamiento bajo que no tiene.

---

## I. La ronda terminal y lo que corrigio

Seccion anadida el 2026-09-04. Cubre lo que cambio entre la Entrega 2B y el examen final,
que es donde un tribunal suele preguntar: los cambios visibles entre una version y la
siguiente.

**I1. Corrigieron RNF-04 de dos a cinco minutos. ¿No es rebajar el requisito para poder
cumplirlo?**
Al reves: el umbral de dos minutos se habia fijado **sin preguntarle a ningun usuario**. En
la ronda terminal se le pregunto a un docente cuanto tardaria en entender la pantalla sin
capacitacion previa y respondio «maximo unos cinco minutos». Es la unica medicion de campo
que existe sobre ese umbral, y contradice la cifra escrita. Un umbral corregido con
evidencia vale mas que uno inventado que nadie comprobo. La cita esta en la transcripcion.
→ `02_Evidencias/Transcripciones/2026-09-03_Docente_DOC-09_EV-24_Transcripcion.md`

**I2. ¿Por que RNF-14 dejo de tener una sola cifra?**
Porque medir un tiempo medio sobre dos poblaciones distintas no mide el servicio, mide la
mezcla. La asistente de TIC describio que la falla menor --periferico, cable o conexion-- se
atiende en el acto, y que la mayor exige retirar el equipo y se resuelve en veinticuatro
horas. Un umbral unico de quince minutos no es medible sobre esas dos cosas juntas. Ahora se
mide por clase de falla. Quedo registrado como defecto **D-04** en el acta de la sesion.
→ `02_Evidencias/Validacion_Walkthrough/Sesiones_Validacion/2026-09-04_Tecnico_TIC-01_Walkthrough_Acta.pdf`

**I3. La guia pide tres sesiones de validacion con usuarios tecnicos. ¿Cuantas hicieron?**
**Las tres**, y estan depositadas: `TIC-01` el 2026-09-04 --asistente de Tecnologias TIC--,
`TIC-02` el 2026-09-05 --responsable de redes y soporte-- y `TIC-03` el 2026-09-07
--laboratorista de Ciencias de la Computacion, con dieciocho anios en el cargo--.

Costo tres dias y conviene decir por que: el area de Tecnologias de la Informacion y
Comunicacion estaba **en remodelacion el 4 de septiembre** y su personal no se encontraba en
la institucion. La institucion **si tiene** ese personal; la causa fue de calendario, no de
plantilla, y se declara asi para no atribuirle a la organizacion cliente una carencia que no
tiene.

Lo que si sigue corto es el **alcance**: quince minutos por sesion dejan seis de los ocho
requisitos dirigidos a Personal de TI sin consultar --`RNF-03`, `RNF-06`, `RNF-09`, `RNF-10`,
`RNF-12` y `RD-03`--, y esos siguen declarados huerfanos. Las tres sesiones respaldan `RD-10`,
`RD-11`, `RNF-01` y `RNF-14`.
→ `02_Evidencias/Validacion_Walkthrough/declaracion_perfil_tecnico.md`

**I4. ¿Por que los conserjes no cuentan como usuarios tecnicos, si manejan las camaras y los
proyectores?**
Porque ellos mismos se distinguen del tecnico, y esta grabado. `CONS-03` describe que
comunica la falla a la autoridad de la facultad y que «ella realiza el escrito y ella manda
para el tecnico»; `CONS-02`, que se avisa a los jefes «para que manden a los responsables a
dar un mantenimiento». Operan y reportan; no administran. El criterio aplicado fue lo que
cada persona declara que hace, no el nombre de su cargo ni la conveniencia del recuento.
→ `02_Evidencias/Transcripciones/`, EV-08 y EV-09

**I5. Tienen dieciseis entrevistas y analizan diez. ¿Por que no codificaron las seis nuevas?**
Porque la codificacion tematica es lectura interpretativa y se hace con el corpus completo
delante, no a ultima hora. Las seis estan transcritas, anonimizadas y depositadas; su
codificacion queda pendiente y **asi se declara en todos los documentos**, incluido el
manuscrito. Decir dieciseis sin esa precision haria pasar por analizado lo que solo esta
transcrito.
→ `07_Publicacion/manuscrito_final.pdf`, amenaza **T4**

**I6. ¿Que es RQ2 y por que aparece si el estudio comparaba humano contra LLM?**
El estudio siempre respondio dos preguntas y solo enunciaba una. RQ2 es **cuanta potencia
estadistica alcanza un panel ciego de tres jueces y que tamano necesitaria una replicacion**:
8,4 % frente al 80 % convencional, y harian falta 34 observaciones apareadas. La respuesta ya
estaba calculada por script antes de enunciarla.
→ `06_Experimento/resultados/power_calculation.csv`

**I7. La matriz tiene 59 filas con cadena completa de 75. ¿Y las otras 16?**
Las setenta y cinco tienen **todos sus eslabones declarados**: ninguna celda dice nada
ambiguo. Las que no cierran no estan a medio hacer, **no pueden** cerrar: nueve nacen del
analisis normativo de la Ley Organica de Proteccion de Datos y no de entrevista --inventarles
evidencia de campo seria fabricarla--, seis son restricciones de diseno que no tienen fuente o que se verifican por
revision y no por caso de prueba, `RNF-15` no tiene ninguna clase que la realice, y `RD-02`
se deja abierta a proposito: su fila de la matriz y su ficha del ERS dicen cosas distintas, y
escribirle una historia fijaria la contradiccion. Las demas se cerraron con historias
`HU-22` a `HU-38`: tenian fuente y solo les faltaba la historia. La columna se comprueba por script.
→ `04_Trazabilidad/huerfanos_y_cadenas_rotas.md`, `python 04_Trazabilidad/verificar_matriz.py`

**I8. Hay dieciseis entrevistas y quince videos. ¿Donde esta el que falta?**
Una sola ausencia: `EV-14` se registro **solo en audio por peticion expresa del
participante**. No es una omision, es un limite del consentimiento.

Hubo una segunda hasta el 2026-09-08. El video de `EV-16` estaba declarado como no
recuperable, y aparecio donde la propia declaracion decia que estaba: en el **Git LFS del
repositorio de la Entrega 2A**. La copia que maneja el equipo es un ZIP descargado, no un
clon, y por eso los punteros LFS figuraban como archivos de 134 bytes. Su SHA-256 coincide
con el `oid` del puntero y su duracion con la del audio ya inventariado. Ademas, el video y el audio de las seis de la
ronda terminal **no se publican**: su consentimiento dice literalmente que las grabaciones
originales no se publican, de modo que a la zona publica va solo la transcripcion anonimizada.
→ `02_Evidencias/00_Restringido/README_Restringido.md`, apartados 1 y 4

**I9. ¿Como sabemos que ese material restringido existe, si no lo podemos ver?**
Por la ficha tecnica: registra las treinta y cuatro piezas con su duracion, su codec, su tamano
y su **SHA-256**, de modo que cualquiera puede contrastar un archivo contra su hash sin
abrirlo. El contenedor esta cifrado con AES-256 y con los nombres de archivo ocultos, alojado
en el OneDrive institucional, y la contrasena se entrega al docente por el Sistema de Gestion
Academica y por ningun otro medio.
→ `02_Evidencias/00_Restringido/fichas_tecnicas.csv`

**I10. ¿Usaron inteligencia artificial? ¿En que exactamente?**
Si, y esta declarado seccion por seccion, incluidas aquellas en las que **no** se uso ninguna
herramienta. Hay dos usos separados: el Conjunto A de requisitos funcionales fue **generado
por un modelo de lenguaje a proposito**, como variable independiente del cuasi-experimento
--es el objeto de estudio, no asistencia--; y como apoyo de redaccion y de tooling, con el
metodo de validacion anotado en cada fila. La codificacion tematica del corpus y la curva de
saturacion las produjo el equipo sin herramienta, y asi consta.
→ `10_Autoria/declaracion_uso_ia.md`

**I11. ¿Que aprendieron que no esperaban?**
Que dos de los seis docentes respondieron que conocer el estado del aula antes de entrar les
resulta **indiferente**, lo que discute la premisa del sistema; y que la unica persona con
perfil tecnico localizada partio en dos una falla que la especificacion trataba como una
sola. Los dos hallazgos estan en el corpus y ninguno se omitio por incomodo.
→ `02_Evidencias/Transcripciones/`, EV-22 y EV-24

**I12. La tabla de la seccion 6 recomendaba el Enfoque 3, de explicabilidad, y ustedes
hicieron el Enfoque 1. ¿Por que?**
Conviene empezar por lo que dicen los dos instrumentos, porque **el enfoque se elegia**.

La rubrica de la Entrega 2A, la vigente cuando habia que elegir, dice: «se ofrecen tres
enfoques posibles; **cada equipo elige uno y solo uno**», y exige declararlo antes de la
semana 10 y registrarlo en OSF **antes de recolectar datos**. Elegimos el Enfoque 1 y lo
registramos el 2 de agosto, antes del primer dato. Las dos condiciones se cumplieron.

La tabla de la Entrega 2B **orienta**, no manda: su cabecera dice que «orienta la eleccion»,
que la pregunta es **sugerida** y el enfoque **recomendado**, y que «cada equipo **puede
modificar** la pregunta principal, pero debe declarar la modificacion por escrito y
justificar por que mantiene el compromiso con el minimo empirico». Eso es exactamente lo que
hicimos: la declaracion escrita es `06_Experimento/declaracion_enfoque.md` y la
justificacion del minimo empirico es su apartado 4.

Y aunque hubiera sido una asignacion, no habriamos vuelto atras, por el registro previo: el
protocolo esta en OSF con DOI `10.17605/OSF.IO/7PQ3H`, aceptado el 2 de agosto a las 20:25
UTC y archivado por el Center for Open Science en el Internet Archive. Esa marca temporal es
externa al equipo y anterior a la recoleccion. Un registro previo existe para impedir que la
pregunta se reescriba despues de ver los resultados; cambiarlo ahora lo convertiria en un
adorno.
→ `06_Experimento/declaracion_enfoque.md`
