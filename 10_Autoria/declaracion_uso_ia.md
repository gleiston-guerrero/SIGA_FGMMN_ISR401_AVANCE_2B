# Declaracion de uso de inteligencia artificial

Proyecto SIGA — Entrega Final (2B) — ISR-401 — Equipo FGMMN
Ultima actualizacion: 2026-09-14

Elemento **A9** de la evidencia de autoria. Cubre, seccion por seccion, la herramienta
empleada, el tipo de asistencia recibida y el metodo concreto con el que el equipo valido
el contenido resultante.

**Cubre todas las secciones del entregable, incluidas aquellas en las que no se empleo
ninguna herramienta**, que se enumeran en el apartado 4. Declarar solo donde hubo
asistencia dejaria al lector sin saber si el silencio significa ausencia de uso o ausencia
de declaracion.

---

## 1. Los modelos de lenguaje como objeto de estudio

El Conjunto A de Requisitos Funcionales del componente empirico fue **generado por un
modelo grande de lenguaje**, deliberadamente y como variable independiente del
cuasi-experimento. No es asistencia de redaccion: es el material que el estudio compara.

El registro integro de la generacion, el modelo declarado y el material fuente estan en
[`06_Experimento/prompts_llm/`](../06_Experimento/prompts_llm/). **No hubo una consigna
literal enviada en una sesion aparte ni parametros controlados**: el Conjunto A se genero el
2026-08-02 dentro de la conversacion de trabajo del proyecto, a partir de la instruccion «usa
tu propio modelo», y la interfaz de chat no expone temperatura, top-p ni semilla. Consta en
[`registro_generacion_conjunto_A.md`](../06_Experimento/prompts_llm/registro_generacion_conjunto_A.md)
y como desviacion 6 en `07_Datos/desviaciones.md`. Las limitaciones
metodologicas de esa generacion —incluida la exposicion previa parcial del modelo al
Conjunto B en la misma sesion de chat— se declaran en
`06_Experimento/prompts_llm/prompt_llm_conjunto_A.md` y se recogen como amenaza a la
validez de constructo en el reporte.

---

## 2. Asistencia recibida en la elaboracion del entregable

| Seccion o artefacto | Herramienta | Tipo de asistencia | Metodo de validacion aplicado |
|---|---|---|---|
| Estructura del repositorio | Claude (Anthropic) | Reorganizacion del arbol de carpetas contra la seccion 9 de la guia y normalizacion de nombres de archivo a ASCII sin espacios | El equipo recorrio el arbol resultante carpeta por carpeta contra el texto de la seccion 9 y verifico que cada archivo migrado abre y conserva su contenido |
| `README.md` | Claude (Anthropic) | Redaccion a partir de datos que el equipo proporciono: integrantes, roles, dependencias y secuencia de compilacion | Cada ruta citada se comprobo contra el arbol real; la secuencia de compilacion se ejecuto sobre un clon limpio |
| `CHANGELOG.md`, `CITATION.cff`, `LICENSE` | Claude (Anthropic) | Redaccion de los archivos raiz obligatorios | El equipo verifico que ningun campo quedara escrito como pendiente y que los alcances de licencia correspondan a las rutas reales |
| `04_Trazabilidad/aporte_individual.csv` | Claude (Anthropic) | Extraccion de los identificadores de commit desde el historial de Git de ambos repositorios | Cada identificador se resolvio con `git show` contra el repositorio que la fila declara |
| `07_Publicacion/dataset_zenodo/diccionario_datos.csv` | Claude (Anthropic) | Redaccion de las definiciones a partir de las cabeceras reales de cada archivo de datos | El equipo contrasto cada fila con la cabecera del archivo que describe |
| `07_Publicacion/dataset_zenodo/correspondencia_salidas.csv` | Claude (Anthropic) | Emparejamiento de cada salida con el script que la produce, leido del Makefile | Se ejecuto `make all` y se comprobo que cada salida listada aparece regenerada |
| Auditoria del repositorio contra la rubrica | Claude (Anthropic) | Contraste sistematico del arbol y del historial contra los criterios de piso y las evidencias exigibles | El equipo verifico a mano cada hallazgo antes de actuar sobre el: conteos de archivos, ausencia de etiquetas y presencia de marcadores de plantilla |

---

### Trabajo del 1 y 2 de agosto de 2026, en la Entrega 2A

Anadido el 2026-09-12, cuando la exportacion de la conversacion de trabajo del proyecto en
claude.ai permitio documentar lo que el asistente produjo ese dia. Estos artefactos se
crearon en la Entrega 2A y llegaron a este repositorio con la migracion del 2026-08-30.

| Seccion o artefacto | Herramienta | Tipo de asistencia | Metodo de validacion aplicado |
|---|---|---|---|
| Conjunto A de requisitos | Claude (Anthropic), interfaz de chat | Generacion de los 26 requisitos: es el objeto de estudio, apartado 1 | Registro integro en `06_Experimento/prompts_llm/registro_generacion_conjunto_A.md`, con la huella SHA-256 del extracto |
| Protocolo del cuasi-experimento: PICOC, hipotesis, variables y plan de analisis | Claude (Anthropic), interfaz de chat | Redaccion del primer texto del protocolo en la misma respuesta que genero el Conjunto A | El equipo lo registro en OSF el 2026-08-02 (`10.17605/OSF.IO/7PQ3H`). Toda diferencia posterior entre lo registrado y lo ejecutado consta en `07_Datos/desviaciones.md` |
| Rubrica de evaluacion, hoja de puntuacion, paquete de evaluacion ciega y tabla de desciego | Claude (Anthropic), interfaz de chat | Armado de los instrumentos y mezcla de los 51 items con semilla fija | La tabla de desciego se custodia fuera de la zona publica (`06_Experimento/clave_desciego_UBICACION.md`). Los tres jueces, externos a los entrevistados, los eligio el equipo |
| `06_Experimento/scripts_analisis/analizar_resultados.py`, primera version | Claude (Anthropic), interfaz de chat | Script de consolidacion y analisis, probado con datos simulados que se borraron antes de recibir las hojas reales | Las salidas actuales se regeneran identicas byte a byte con `python 07_Datos/scripts/ejecutar.py` |

### Artefactos de la Entrega 2A incorporados en la migracion del 2026-08-30

Declarados el 2026-09-13. Se elaboraron con asistencia en las entregas anteriores y llegaron
a este repositorio con la migracion; hasta esta fecha la declaracion no los nombraba en ningun
apartado.

| Seccion o artefacto | Herramienta | Tipo de asistencia | Metodo de validacion aplicado |
|---|---|---|---|
| Texto de la Especificacion de Requisitos, `01_ERS/secciones_generadas.tex` | Claude (Anthropic) | Asistencia en la redaccion de la especificacion | Auditoria de calidad con las seis metricas y sus conteos base (`01_ERS/Auditoria_Calidad/`); inspeccion formal `INS-01`, re-inspeccion `REINS-01` y comite de cambios `CCB-01` (`02_Evidencias/Validacion_Walkthrough/`); cada requisito con fuente trazado a su evidencia de campo en la matriz, comprobada con `verificar_matriz.py` |
| Componente inteligente, `01_ERS/Componentes_IA/` | Claude (Anthropic) | Asistencia en la redaccion de la clasificacion de riesgo, la ficha de `RF-09`, los requisitos `RNF-IA`, el plan de monitoreo y la evidencia de explicabilidad | Los ocho `RNF-IA` constan en la matriz con su caso de prueba; `evidencia_explicabilidad.csv` se regenera con su script; el respaldo de campo de `RNF-IA-03` procede del cuestionario depositado |
| Codigo del prototipo, `05_MVP/codigo_fuente/` | Claude (Anthropic) | Asistencia en la escritura del codigo | Cobertura contrastada requisito por requisito en `05_MVP/cobertura_requisitos.csv` (17 de 20 Must), recorrido funcional grabado en `05_MVP/demostracion/`. Comprobado de nuevo el 2026-09-12: instala, siembra la base, arranca, y el inicio de sesion y los seis modulos de la API responden |

---

### Trabajo del 1 y 2 de septiembre de 2026

Posterior a la primera version de esta declaracion, y anadido aqui para que la
declaracion cubra el entregable completo y no solo su estado a finales de agosto.

| Seccion o artefacto | Herramienta | Tipo de asistencia | Metodo de validacion aplicado |
|---|---|---|---|
| Modelado UML e i* --- 41 diagramas | Claude (Anthropic) | Reconstruccion de los diagramas en PlantUML a partir de los modelos existentes, leidos de los `.vpp` y los `.drawio` originales | El equipo comprobo por script que los 41 diagramas conservan los elementos y relaciones del modelo original, y a ojo cada figura renderizada. La numeracion de mensajes de las 16 secuencias se verifico sin repeticiones |
| `03_Modelado/09_DFD/` | Claude (Anthropic) | Alineacion de los DFD de nivel 0 y 1 con el diagrama de contexto: traduccion al idioma del modelo y correspondencia de entidades y flujos | Los dibujo el equipo en draw.io. Se comprobo por script que se cumplen las tres reglas de la notacion: ningun flujo sin nombre, ninguno entre dos entidades externas y ninguno entre dos almacenes |
| Amenazas a la validez del manuscrito | Claude (Anthropic) | Redaccion de las ocho amenazas, dos por categoria, con su mitigacion y la limitacion remanente, a partir de los resultados y las desviaciones ya declaradas | Cada cifra citada se contrasto contra la tabla o figura que la produce; el manuscrito compila sin referencias sin resolver |
| `02_Evidencias/Member_Checking/` | Claude (Anthropic) | Redaccion del acta de la sesion, del guion y del consentimiento; censura de los datos identificables de los consentimientos firmados | La sesion la condujo el equipo. El acta consigna lo que ocurrio, incluida su duracion real tomada de la cabecera del video. La censura se verifico pagina por pagina sobre el archivo depositado |
| `02_Evidencias/Etica/acta_constancia_N10.pdf` | Claude (Anthropic) | Composicion del documento y censura de las cedulas de los testigos | Las firmas las recogio el equipo. El documento declara de forma expresa que no es una autorizacion escrita del docente |
| Integridad del repositorio | Claude (Anthropic) | Deteccion de que el manifiesto de sumas verificaba en la maquina local pero habria fallado sobre un clon limpio, y correccion de la normalizacion de fin de linea | Se clono el repositorio desde el remoto y se ejecuto la comprobacion completa: 440 de 440 sumas correctas |
| Recodificacion de video | Claude (Anthropic) | Ajuste de los videos de la sesion de verificacion y de la exposicion al formato declarado del repositorio | Se comprobo que la duracion del archivo depositado coincide con la del original y que decodifica de principio a fin sin errores |

---

### Trabajo del 3 de septiembre de 2026

| Seccion o artefacto | Herramienta | Tipo de asistencia | Metodo de validacion aplicado |
|---|---|---|---|
| `07_Datos/` --- paquete de datos | Claude (Anthropic) | Redaccion de los tres scripts de etapa y del orquestador, del diccionario de datos, de la licencia de datos y de la documentacion del paquete | Se clono el repositorio en limpio, se borro todo lo generado y se ejecuto la orden unica: las salidas regeneradas resultan identicas byte a byte a las depositadas. Los veinte coeficientes de acuerdo reproducen los que ya calculaba scikit-learn |
| `07_Datos/resultados/acuerdo_interevaluador_ic.csv` | Claude (Anthropic) | Implementacion del kappa de Cohen ponderado y de Fleiss con su intervalo por bootstrap, en biblioteca estandar | Contraste obligado contra los valores ya publicados. La primera version usaba kappa sin ponderar y **no coincidia**; el contraste lo detecto y se corrigio al estimador ponderado que declara el protocolo |
| `04_Trazabilidad/composicion_equipo.md` | Claude (Anthropic) | Redaccion de la declaracion de composicion tras el alta de un integrante y la baja de otro | Los recuentos por autor se comprobaron con `git shortlog -sne main` contra el propio historial. El integrante recien incorporado figura con cero commits porque esa es su situacion real |
| `CHANGELOG.md` --- version 2B-1.7.0 | Claude (Anthropic) | Redaccion de la entrada, incluida la documentacion de la migracion de repositorio | El motivo y la fecha los aporto el equipo; las fechas del historial se leyeron del repositorio |
| `10_Autoria/bitacora_sesiones.csv` | Claude (Anthropic) | Script que deriva la bitacora del historial de versiones | Ningun campo se escribe a mano: se regenera con `python 10_Autoria/generar_bitacora.py` y se comprueba que exista al menos una fila por cada dia con commits |
| `.mailmap` | Claude (Anthropic) | Unificacion de identidades historicas de Git | Comprobado con `git shortlog -sne main`: dos autores, ninguna identidad duplicada, ningun autor ajeno al equipo |
| Recompilacion del ERS en A4 | Claude (Anthropic) | Cambio de geometria y recompilacion | Verificado sobre el registro de compilacion: cero referencias sin resolver y cero errores. **Corregido el 2026-09-12:** esta fila afirmaba ademas «cero desbordes horizontales, cero verticales», y no era cierto. Recompilado el ERS en limpio, el registro tenia **80 desbordes horizontales**: las tablas conservaban los anchos en centimetros de la maquetacion anterior y sumaban mas que la caja de texto de A4. Se corrigieron el 2026-09-12 y se declaran en ese apartado |

### Trabajo del 4 de septiembre de 2026

Herramienta de apoyo a la codificacion tematica de la ronda terminal. **La
codificacion en si no se automatizo y sigue declarada en el apartado 4**: lo que
estas filas cubren es la preparacion mecanica del material y la correccion de dos
defectos de los scripts de analisis.

| Seccion o artefacto | Herramienta | Tipo de asistencia | Metodo de validacion aplicado |
|---|---|---|---|
| `06_Experimento/scripts_analisis/extender_corpus_json.py` | Claude (Anthropic) | Script que incorpora al corpus JSON las transcripciones depositadas que aun no figuran en el | No reescribe ningun registro anterior: empalma los nuevos y comprueba campo por campo que los diez originales quedan identicos antes de escribir. Los recuentos de turnos de las seis --64, 89, 105, 43, 37 y 91-- coinciden con los verificados al depositarlas |
| `curva_saturacion.py` --- orden determinista | Claude (Anthropic) | Deteccion de que `sort_values` de pandas no es estable y de que las seis entrevistas de la ronda terminal comparten fecha, con lo que el orden entre ellas podia variar entre ejecuciones; desempate por identificador de evidencia | Se reejecuto sobre la codificacion vigente y la tabla resultante es **identica byte a byte** a `saturacion_por_entrevista.csv` ya publicada. La correccion no altera ningun resultado anterior |
| `curva_saturacion.py` del deposito Zenodo | Claude (Anthropic) | Correccion de la ruta por omision del corpus, que apuntaba a una carpeta inexistente dentro del propio deposito | Se comprobo contra el arbol real del deposito: el archivo esta en la raiz, un nivel por encima de `scripts_analisis/` |
| `02_Evidencias/Codificacion_Tematica/incorporar_codificacion.py` | Claude (Anthropic) | Script que valida una hoja de codificacion rellenada y la incorpora al archivo | Probado con filas deliberadamente invalidas: rechaza el fragmento tomado del entrevistador, el retocado al copiar, el que no lleva categoria y el duplicado, y en ninguno de esos casos escribe nada |
| Hoja de turnos y busqueda de umbrales (material de trabajo, fuera del repositorio) | Claude (Anthropic) | Separacion de los turnos del participante, descarte de los que no llegan a 18 palabras y de las formulas de cortesia, y busqueda por termino de los turnos que mencionan cada requisito huerfano | Van **todos** los turnos que superan el umbral, sin seleccion previa, para que la eleccion de que es codificable la haga quien codifica. Las columnas de codigo y de juicio se entregan vacias |

---

### Trabajo del 4 de septiembre de 2026, tarde

| Seccion o artefacto | Herramienta | Tipo de asistencia | Metodo de validacion aplicado |
|---|---|---|---|
| Consistencia entre documentos | Claude (Anthropic) | Contraste de lo que cada documento afirma contra lo que hay en el arbol: enlaces relativos, recuentos declarados y afirmaciones sobre el corpus | Los 74 enlaces relativos del repositorio resuelven; cada recuento corregido se comprobo contra el archivo o la carpeta que describe |
| `manuscrito_final.tex` --- enunciado de RQ2 | Claude (Anthropic) | **Reestructuracion, no produccion.** El manuscrito respondia dos preguntas y solo enunciaba una. Se nombra la segunda sobre analisis que el equipo ya habia ejecutado --el calculo de potencia y el analisis de sensibilidad--, y se retira del titulo del apartado 4.3 una referencia a un criterio de la rubrica de la asignatura, que no tiene sentido en un manuscrito dirigido a REFSQ | **Ninguna cifra es nueva.** El 8,4 % de potencia y las 34 observaciones necesarias proceden de `06_Experimento/resultados/power_calculation.csv`, generado por script antes de esta edicion. El equipo contrasto cada cifra del parrafo anadido contra esa salida |
| `04_Trazabilidad/vaciado_umbrales.csv` | Claude (Anthropic) | Localizacion de la frase, la cifra y la evidencia de cada umbral huerfano en las transcripciones | **No se deposita en el repositorio.** Queda como material de trabajo del equipo. Cada cita se comprobo literal contra su transcripcion antes de escribirla |
| `RNF-04` y `RNF-14` --- correccion de umbrales | Claude (Anthropic) | Redaccion del enunciado corregido y propagacion a la matriz, los casos de prueba y la copia del deposito | **La decision es del equipo**, que confirmo por separado los dos hechos de campo antes de autorizar el cambio. Las dos citas que los sostienen se comprobaron literales contra `EV-24` y contra el acta `WT-08` |

---

### Trabajo del 5 de septiembre de 2026

| Seccion o artefacto | Herramienta | Tipo de asistencia | Metodo de validacion aplicado |
|---|---|---|---|
| `06_Experimento/declaracion_enfoque.md` | Claude (Anthropic) | Redaccion de la declaracion de desviacion respecto del enfoque empirico asignado por la rubrica. **Documento de constancia, no de resultados**: no introduce ninguna cifra, tabla ni conclusion nueva | Cada dato citado se comprobo contra su fuente en el repositorio: la fecha de aceptacion del registro en OSF contra `registro_previo/osf_registration_api.json`, el enunciado del enfoque contra la cabecera de `protocolo/protocolo.md`, y las cifras de potencia contra `resultados/power_calculation.csv`. La decision de no cambiar el enfoque es del equipo |
| `04_Trazabilidad/sincronizacion_tablero.py` | Claude (Anthropic) | Script que compara los identificadores de requisito del tablero de gestion contra los de la matriz de trazabilidad y calcula el porcentaje de sincronizacion | Probado con un export al que se le retiraron dos requisitos y se le anadio uno inexistente: el script senala exactamente esos tres y ninguno mas. El tablero lo poblo el equipo desde su propia cuenta |
| Backlog del tablero de gestion | Claude (Anthropic) | Volcado de los 60 requisitos de la matriz al formato de importacion, y correccion del estado con el que entraron | **Las 60 actividades entraron con estado Listo**, lo que las ocultaba del backlog y ademas declaraba terminado lo que no lo esta; se corrigieron a Por hacer. Comprobado despues: el backlog muestra las 60 |


### Trabajo del 6 de septiembre de 2026

| Seccion o artefacto | Herramienta | Tipo de asistencia | Metodo de validacion aplicado |
|---|---|---|---|
| Codificacion tematica de `EV-20` a `EV-25` | Ninguna | **La codificacion la hicieron las tres personas**, una entrevista completa cada una, y la columna `Analista_codificador` registra quien codifico cada fragmento | La asistencia se limito a repartir los turnos, verificar cada cita contra su transcripcion e incorporarlas con `incorporar_codificacion.py`. **Los codigos y las categorias son juicio del equipo.** La columna `Requisito_derivado` no lo es en 38 filas: se declara en la fila siguiente |
| `Requisito_derivado` de 38 filas que quedaron vacias | Claude (Anthropic) | 21 se completaron **por consistencia**, copiando el requisito que ese mismo codigo ya tenia asignado en la codificacion depositada. Las 17 restantes fueron **ocho decisiones** sobre codigos nuevos sin precedente | Cada una de las ocho lleva su justificacion escrita en el script que las aplico, y el criterio se tomo de la convencion que los propios codificadores usaron en los otros codigos nuevos. El equipo puede revertir cualquiera |
| `02_Evidencias/Codificacion_Tematica/robustez_saturacion.py` | Claude (Anthropic) | Script que prueba las 720 ordenaciones posibles del bloque de entrevistas del mismo dia, para comprobar que la saturacion no depende del orden | Solo biblioteca estandar; se ejecuta y reproduce la cifra publicada. La saturacion se alcanza en las 720 |
| `06_Experimento/panel_ampliado/` | Claude (Anthropic) | Digitalizacion de las siete hojas de la segunda vuelta desde los PDF, y el script que calcula acuerdo, consistencia intrajuez y efecto | Las 189 puntuaciones se extrajeron del texto del PDF, no a mano. **La regla de decision —mantener los tres jueces del registro previo si el acuerdo volvia a salir cerca de cero— la fijo el equipo por escrito antes de la segunda sesion**, en `panel_ampliado/protocolo_segunda_vuelta.md`; aqui solo se aplico. **Corregido el 2026-09-12:** esta fila decia «con su umbral», y esa regla no fija ningun umbral numerico; el 0,41 que se llego a citar es la frontera de Landis y Koch, no un liston pactado, como aclara el CHANGELOG desde el 2026-09-08 |
| Actividad `SIGA-61` del tablero de Jira | Claude (Anthropic) | **Creacion de una actividad en la herramienta**, a peticion expresa del equipo: la restriccion `RD-01` estaba en la ERS y no tenia ni actividad ni fila en la matriz | Se creo desde la cuenta del equipo con el mismo formato que las demas actividades `RD`. El export se **regenero desde Jira**, no se edito el CSV: se comparo fila a fila contra el anterior y `SIGA-61` es la unica diferencia |
| Censura del consentimiento de `TIC-02` | Claude (Anthropic) | El PDF entregado traia la censura como rectangulos vectoriales superpuestos, con el nombre, la cedula y la firma intactos debajo. Se rehizo quemandola en el mapa de bits | Comprobado despues sobre el archivo resultante: cero dibujos vectoriales, cero texto extraible y cero tinta bajo las bandas. Se revisaron ademas los otros diecisiete consentimientos del repositorio, que no tenian el defecto |

---

### Trabajo del 7 al 10 de septiembre de 2026

Todo lo de este tramo se hizo en sesiones con el asistente; el unico trabajo de campo del
tramo —la sesion `WT-10` con `TIC-03`, su grabacion y su acta manuscrita— lo hizo el equipo
y se declara en el apartado 4.

| Seccion o artefacto | Herramienta | Tipo de asistencia | Metodo de validacion aplicado |
|---|---|---|---|
| `07_Publicacion/verificar_afirmaciones.py` | Claude (Anthropic) | Script que recalcula cada cifra afirmada en el manuscrito, el reporte, las diapositivas y el libreto desde la salida que la sostiene | Termina con codigo distinto de cero si una cifra no coincide; se ejecuto antes de cada confirmacion que tocaba esos documentos |
| Contenedor cifrado dentro del repositorio | Claude (Anthropic) | Particion del contenedor en volumenes, confirmacion por lotes para esquivar el limite de envio, y en su segunda version el guion `rehacer_contenedor.sh` que el equipo ejecuto en su maquina para incorporar dos videos que faltaban | Comprobado byte a byte que los volumenes reconstruyen un contenedor con la misma SHA-256 y que descifra. La contrasena la custodia el analista lider y se entrega al docente por el Sistema de Gestion Academica |
| `02_Evidencias/Cuestionario/Instrumento/` | Claude (Anthropic) | Deposito del PDF que el equipo exporto del formulario publicado, y contraste de sus preguntas con las columnas del export de respuestas | Las 30 preguntas coinciden una a una con las 30 columnas |
| `fair_assessment.*` y `generar_fair_assessment.py` | Claude (Anthropic) | Obtencion de la evaluacion de F-UJI 4.0.0 sobre el deposito de Zenodo y script que compone el informe a partir de su salida | El informe no se redacta: se genera del JSON crudo de F-UJI, depositado junto a el |
| Acta de `WT-10` | Claude (Anthropic) | Transcripcion a limpio del borrador en Word que redacto el equipo y censura de la hoja de firmas | Se detecto que un parrafo del borrador era copia literal del acta de `TIC-01` y el equipo lo reescribio. Las tres cifras del acta —18 anos, 3 segundos, de 15 a 30 minutos— se contrastaron con la transcripcion de la sesion |
| Transcripciones `EV-26`, `EV-27` y `EV-28` | Claude (Anthropic) | **Solo formato**: paso de los tres archivos de texto que entrego el equipo a la plantilla del corpus | El contenido se conservo palabra por palabra, con titubeos y repeticiones; los marcadores de hablante ya venian puestos |
| Solicitud de cambio de composicion y `composicion_equipo.md` | Claude (Anthropic) | Redaccion del escrito y de la actualizacion de la declaracion de composicion | **El escrito lo firmaron los tres integrantes** el 2026-09-08. Los recuentos por autor se leyeron del historial |
| `06_Experimento/declaracion_enfoque.md` y `panel_ampliado/00_LEEME.md` | Claude (Anthropic) | Correccion de dos afirmaciones que no se sostenian: que el enfoque se asigno sin eleccion y que el liston de 0,41 constaba por escrito | Contrastadas contra el protocolo de la segunda vuelta y contra la guia; la cifra sin fuente se retiro |
| Manuscrito, reporte y caratulas | Claude (Anthropic) | Actualizacion de `AFI-13`, del DOI de version y de las caratulas, y regeneracion de los PDF desde su fuente | Cada PDF se recompilo desde su `.tex`; ninguna cifra nueva, todas contrastadas con `verificar_afirmaciones.py` |
| Deposito `2B-1.12.0` en Zenodo | Claude (Anthropic) | Instrucciones paso a paso para la publicacion y preparacion del paquete | **La subida y la publicacion las hizo el equipo** desde su cuenta. El DOI se copio de Zenodo |
| `08_Defensa/`: diapositivas, notas del orador, libreto v2.0 y banco de preguntas | Claude (Anthropic) | Redaccion del libreto por diapositiva y del reparto por integrante, correccion de diapositivas que afirmaban cosas que el repositorio no sostiene —el kappa de la doble codificacion inflado, la saturacion negada, un despliegue con Docker nunca ejecutado— y sustitucion de la diapositiva 9 | Las cifras del libreto se comprobaron contra sus salidas. **La exposicion, la demostracion en vivo y las respuestas son del equipo**, que grabo la defensa |
| Deposito de la defensa grabada | Claude (Anthropic) | Recodificacion del video de 413 MB a 80 MB con VLC para respetar el limite de GitHub | Se comprobo que decodifica hasta el ultimo fotograma y que la duracion coincide con la del original, 24 min 49 s |
| `10_Autoria/verificacion_previa.*` | Claude (Anthropic) | Reejecucion sobre un clon limpio del remoto | La salida del script es la que consta; la firman dos integrantes |
| **Operaciones de Git** | Claude (Anthropic) | **Buena parte de las confirmaciones y etiquetas del historial, en este tramo y en los anteriores declarados en este documento, las ejecuto el asistente desde la maquina del analista lider**, con el nombre y el correo institucional del integrante al que el equipo atribuyo cada cambio: tambien varias a nombre de Munoz Quinonez y de Cedeno Avila. Por ejemplo, `3eda626`, `aed73c3` y `298e28f` se confirmaron a nombre de Cedeno Avila con las transcripciones y la grabacion que el entrego. La etiqueta `2B-final-v4.0` se borro y se volvio a crear varias veces sobre commits posteriores antes de quedar en `6bb3b08` | El campo *author* de cada confirmacion identifica a quien el equipo atribuye el contenido; no acredita quien tecleo la orden. **El aporte de cada integrante se acredita ademas por las grabaciones de las sesiones de trabajo, las capturas por integrante y el aporte individual firmado** (`10_Autoria/grabaciones/`, `capturas/`, `aporte_individual.pdf`) |

### Trabajo del 11 de septiembre de 2026

| Seccion o artefacto | Herramienta | Tipo de asistencia | Metodo de validacion aplicado |
|---|---|---|---|
| `CHANGELOG.md` --- version `2B-1.13.0` y regeneracion de los manifiestos (`32d4f49`, `b9783c7`) | Ninguna | Los hizo el analista lider a mano | Se declara en el apartado 4. El manifiesto que regenero no casaba con `verificacion_previa.md` y se corrige el 2026-09-12 |

### Trabajo del 12 de septiembre de 2026

Auditoria del repositorio contra la rubrica de cierre del Proyecto Fin de Curso y
correccion de lo que encontro.

| Seccion o artefacto | Herramienta | Tipo de asistencia | Metodo de validacion aplicado |
|---|---|---|---|
| Auditoria contra la rubrica de cierre | Claude (Anthropic) | Contraste de los once items y de los criterios de piso contra un clon limpio: recompilacion de los tres documentos, ejecucion de las dos cadenas de analisis, comprobacion del manifiesto y lectura de la capa de texto de los PDF | Cada hallazgo se reprodujo con la orden que lo muestra antes de corregirlo |
| ERS en A4 sin desbordes | Claude (Anthropic) | Las 68 tablas pasan de anchos fijos en centimetros a anchos proporcionales a la caja de texto, y se corrigen los parrafos que se salian del margen; entrada 4.5 del historial de versiones | Recompilado en limpio: **cero desbordes horizontales y verticales, cero errores, cero referencias sin resolver**, y ningun bloque de texto ni imagen pasa del margen derecho en ninguna pagina. No cambia el contenido de ningun requisito |
| Censura de cedulas y matriculas en los PDF de etica | Claude (Anthropic) | Localizacion de las cedulas y matriculas que seguian en la capa de texto de la solicitud de aprobacion etica, el oficio y los anexos A01, A03, A06, A07 y A09, y censura quemada en el mapa de bits | Comprobado despues: cero cedulas en la capa de texto de todo PDF de la zona publica, salvo las de los tres integrantes en la caratula, el ERS y la solicitud de composicion |
| Declaracion expresa del tratamiento de datos | Claude (Anthropic) | Redaccion de la seccion 3.2 de `resumen_proceso_etico.md` y de `LICENSE-DATA.txt` | **El plazo y el responsable los decidio el equipo**; el plazo coincide con los 24 meses del plan de gestion de datos aprobado |
| `07_Datos/`: etapas `conjuntos` y `documento` | Claude (Anthropic) | Dos etapas nuevas del orquestador: los conjuntos A y B en texto plano, y la regeneracion de las tablas y figuras del documento con comparacion byte a byte contra el manifiesto | Ejecutada la orden unica: las 18 salidas del documento salen identicas a las depositadas |
| Calculo de potencia sin numero escrito a mano | Claude (Anthropic) | `replicar.py` y el `Makefile` cuentan las hojas de jueces en vez de pasar un 3 fijo | La salida `power_calculation.csv` no cambia |
| Registro de la consigna del modelo y desviacion 5 | Claude (Anthropic) | Nota de estado en `prompt_llm_conjunto_A.md` sobre que parte del registro es integra y cual no existe, y desviacion por el momento del calculo de potencia | Las fechas se leyeron del historial y del registro de OSF |
| Correcciones de esta declaracion, del manuscrito y del proceso etico | Claude (Anthropic) | Retirada de la afirmacion de los cero desbordes, del umbral de 0,41 como pactado, de la temperatura como registrada y de la contradiccion sobre los requisitos derivados | Cada correccion se contrasto con la fuente que la desmentia |
| `verificacion_previa.py`, comprobacion 10 | Claude (Anthropic) | La comprobacion de datos personales lee ahora tambien la capa de texto de los PDF | Antes daba por cumplido el criterio con cedulas ajenas en PDF; ahora las detecta |
| `verificacion_previa.py`, reparto de firmas | Claude (Anthropic) | El reparto de la verificacion entre firmantes pasa a calcularse desde el historial, archivo por archivo, en lugar de escribirse a mano. El texto anterior afirmaba que Cedeno Avila no tenia confirmaciones en tres carpetas donde si las tiene | Contrastado con `git log --format=%ae -- <archivo>` sobre cada uno de los 973 archivos repartidos |
| Documentos para firmar de `aporte_individual` y `verificacion_previa` | Claude (Anthropic) | Composicion de los PDF desde su `.md`, con las firmas agrupadas en una sola hoja, y armado del PDF depositado: el documento generado mas la hoja firmada que escaneo el equipo | **Las firmas son manuscritas de los tres integrantes.** La hoja escaneada se inserta sin retoque como ultima pagina |
| Etiquetas `2B-final-v5.0` a `2B-final-v5.3`, y caratulas | Claude (Anthropic) | Creacion de las etiquetas anotadas sobre el commit entregado y regeneracion de la caratula con `generar_caratula.py` | Ninguna etiqueta publicada se movio ni se borro; cada una se comprobo en el remoto. **La decision de cual es la vigente es del equipo** |
| Registro integro de la generacion del Conjunto A | Claude (Anthropic) | Localizacion de la conversacion de la generacion en la exportacion de datos de claude.ai del analista lider, comprobacion de que los 26 requisitos generados son los depositados, y composicion de `registro_generacion_conjunto_A.md` con las omisiones que declara: razonamiento interno, texto de EV-15, busquedas en archivos del proyecto y el script de la tabla de desciego. Correccion de los documentos que describian la generacion como una consigna literal con temperatura controlada | **La exportacion la descargo el analista lider desde su cuenta.** Las demas conversaciones se buscaron por texto de forma automatica, y de ellas solo se mostraron el titulo y las fechas. El extracto lleva su SHA-256 para que el original pueda contrastarse |
| Declaracion de los integrantes retirados | Claude (Anthropic) | Redaccion uniforme, en README, `composicion_equipo.md`, el ERS, el registro OSF, el banco de preguntas y el README de `10_Autoria`, de que Mendoza Palma y Gilces Carranza estan retirados del equipo; y correccion de la linea de autores del folleto de la defensa, que aun nombraba a los cinco | **La situacion de cada integrante la declaro el analista lider.** Se comprobo contra el historial que ninguno de los dos tiene confirmaciones. No se tocaron los documentos firmados de fechas anteriores, que reflejan la composicion de su momento |
| Historias `HU-22` a `HU-38` y cierre de 18 filas de la matriz | Claude (Anthropic) | Redaccion de diecisiete historias de usuario con su criterio de aceptacion Gherkin, a partir del enunciado, el actor, la precondicion y el criterio de verificacion que cada requisito ya tenia en el ERS o en su ficha; actualizacion de la matriz, su copia del deposito, los casos de prueba regenerados, el documento de huerfanos, el reporte y el banco de preguntas. Correccion de `generar_casos_prueba.py`, que fallaba al leer la matriz por su marca de orden de bytes | **Ningun umbral, actor ni cifra es nuevo**: cada criterio reproduce el criterio de verificacion del propio requisito. Solo se cerraron filas con fuente declarada; las 13 sin fuente, `RD-02` ---cuya fila contradice su ficha--- y `RNF-15` ---sin clase--- se dejan abiertas. `verificar_matriz.py` confirma 59 de 75 y la coincidencia de la columna de estado en las 75 filas |
| Auditoria de `2B-final-v5.1` y sus correcciones | Claude (Anthropic) | Segunda auditoria contra la rubrica de cierre sobre un checkout limpio de la etiqueta, busqueda de residuos en archivos y metadatos, y correccion de lo encontrado: esta declaracion no cubria el tramo anterior de este mismo dia; la comprobacion P4 de `verificacion_previa.py` no se ejecutaba y el informe decia siempre que no habia marcas; y el README no listaba el paquete `array` que usa el ERS | La comprobacion P4 corregida se ejecuto sobre el historial: ningun trailer de coautoria, y un unico committer ajeno, el de la interfaz web de GitHub en `d0a3138`, con autor integrante |

### Trabajo del 12 y 13 de septiembre de 2026

| Seccion o artefacto | Herramienta | Tipo de asistencia | Metodo de validacion aplicado |
|---|---|---|---|
| `07_Datos/scripts/etapa5_documento.py` y documentacion del paquete | Claude (Anthropic) | La etapa `documento` deposita las 18 salidas del documento dentro de `07_Datos/`, tras comprobarlas contra el manifiesto; descripcion de las columnas de los ocho CSV nuevos en `diccionario_datos.csv`, y actualizacion de `README_datos.md`, `README.md`, `CHANGELOG.md`, la portada del ERS y la caratula para la etiqueta `2B-final-v5.6`. **La confirmacion, el envio al remoto y la etiqueta `2B-final-v5.6` los ejecuto el asistente desde la maquina de Sanchez Cornejo, Gary Alberto, a peticion expresa suya y con su identidad** |
| Revision de consistencia de todo el arbol sobre `2B-final-v5.6` | Claude (Anthropic) | Recorrido carpeta por carpeta sobre la etiqueta publicada: sumas, enlaces y rutas citadas, recompilacion del reporte, del ERS y del manuscrito, ejecucion de los verificadores de cada carpeta, arranque del prototipo y reconstruccion del contenedor cifrado. Correccion de los textos desactualizados que encontro, listados en `CHANGELOG.md` `[2B-1.17.1]`, y actualizacion de README, portada del ERS y caratula para `2B-final-v5.7` | Cada correccion se contrasto con la evidencia que la sostiene: la metrica de Correccion con `REINS-01` y la seccion 8 de la auditoria; la suma del contenedor, recalculada sobre la concatenacion de los 316 fragmentos; las cifras de codificacion, recontadas en `codificacion_tematica.csv`. **Ningun dato, cifra de resultados ni archivo de evidencia cambia.** Que corregir lo decidio Sanchez Cornejo, Gary Alberto | Ejecutada la orden unica sobre un clon limpio: las 18 salidas depositadas son identicas byte a byte a las del manifiesto, la etapa `integridad` confirma que todas las columnas estan descritas y ninguna cifra cambia. **La observacion la hizo el docente; la decision de atenderla asi es del equipo** |

### Trabajo del 14 de septiembre de 2026

Correcciones que pidio el docente en la evaluacion de la Entrega Final publicada ese dia:
los tamanos del efecto con intervalos sin sentido (B4) y la cadena de analisis que seguia
viviendo en `06_Experimento` (B1).

| Seccion o artefacto | Herramienta | Tipo de asistencia | Metodo de validacion aplicado |
|---|---|---|---|
| Etapa `efectos` de `analizar_resultados.py`, `generar_tablas.py`, `generar_figuras.py` y `desviacion_tamano_efecto.md` | Claude (Anthropic) | Propuesta y codigo del cambio de unidad del tamano del efecto, del juez (n = 3) al requisito (25 frente a 26), y redaccion de la desviacion 7 | Se comprobo que `efectos.csv` da exactamente los mismos valores que `analisis_por_item.csv`, ya publicado desde el 2026-09-01, y que ningun valor p cambia. **Revisaron el cambio y decidieron adoptarlo Munoz Quinonez, Yeranick Esther y Sanchez Cornejo, Gary Alberto** |
| Apartados de magnitud del efecto de `reporte.tex` y `manuscrito_final.tex`, `verificar_afirmaciones.py` y pregunta D5 del banco de la defensa | Claude (Anthropic) | Redaccion de los parrafos que sustituyen a los efectos apareados, de la cuarta desviacion del manuscrito y de las afirmaciones `AFI-04` y `AFI-05` | Cada cifra se contrasto con `efectos.csv`; `verificar_afirmaciones.py` confirma las quince afirmaciones. El manuscrito se recompilo y se mantiene en 15 paginas |
| `07_Datos/scripts/analisis/`, `etapa5_analisis.py`, `etapa3_integridad.py`, `ejecutar.py`, `diccionario_datos.csv`, `README_datos.md` y `README.md` | Claude (Anthropic) | La cadena de analisis se ejecuta dentro de `07_Datos` desde sus datos crudos, y el reporte y el manuscrito incluyen las tablas y figuras desde `07_Datos/resultados/` | Orden unica ejecutada tras borrar los resultados: las 18 salidas son identicas byte a byte al manifiesto y a las de `06_Experimento/replicar.py`, que sigue funcionando sin cambios en su forma de uso |
| Correcciones de `reporte.tex` | Claude (Anthropic) | Localizacion de dos negritas y una ruta que se veian rotas en el PDF por un tabulador en lugar de `\t`, de unos asteriscos de Markdown impresos tal cual y de dos rutas que se salian del margen | PDF recompilado y revisado: sin marcas de LaTeX sueltas y sin desbordes visibles |
| **Operaciones de Git de este tramo** | Ninguna | **Las confirmaciones y el envio al remoto los ejecuto Munoz Quinonez, Yeranick Esther, desde su propio equipo y su cuenta**, aplicando los cambios preparados en una carpeta por confirmacion. El asistente no ejecuto ninguna confirmacion con su identidad | Cada confirmacion se reviso con `git status` y `git diff` antes de hacerla |

---

## 4. Secciones en las que no se empleo ninguna herramienta

Se enumeran para que la declaracion sea completa y no solo positiva.

| Seccion o artefacto | Quien lo produjo |
|---|---|
| Las dieciseis entrevistas de campo y su conduccion | El equipo, en persona |
| Las puntuaciones de los tres jueces del cuasi-experimento | Tres evaluadores externos, de forma independiente y ciega |
| La eleccion del enfoque, la decision de usar jueces externos a los entrevistados y el registro del protocolo en OSF | El equipo. **El texto del protocolo no**: se declara en el apartado «Trabajo del 1 y 2 de agosto de 2026» |
| Las decisiones de priorizacion MoSCoW, Kano y WSJF | El equipo |
| Los diagramas originales en Visual Paradigm (`.vpp`) y en draw.io | El equipo |
| El analisis, la discusion y las conclusiones | El equipo. Las **amenazas a la validez** del manuscrito se redactaron con asistencia y se declaran en el apartado del 1 y 2 de septiembre |
| La codificacion tematica del corpus y la curva de saturacion | El equipo. Incluida la de las seis entrevistas de la ronda terminal: la asistencia recibida se limito a separar los turnos y a buscar terminos, y las columnas de codigo, categoria y juicio se entregaron vacias. **Excepcion:** la columna `Requisito_derivado` de 38 filas, declarada en el apartado del 6 de septiembre |
| La sesion de validacion comunicativa y su conduccion | El equipo |
| Las sesiones de validacion con usuario tecnico `WT-08` a `WT-10`, su grabacion, sus actas manuscritas y la transcripcion de su audio | El equipo |
| La defensa oral: la exposicion, la demostracion en vivo y las respuestas, y su grabacion | El equipo. El libreto y las diapositivas se declaran en el apartado del 7 al 10 de septiembre |
| `CHANGELOG.md` `2B-1.13.0` y la regeneracion de manifiestos del 2026-09-11 | El analista lider, a mano |
| La obtencion de los consentimientos informados y de las firmas de testigos | El equipo |

## 5. Limites que el equipo se impuso

Las secciones evaluativas del reporte —analisis, discusion, conclusiones y justificacion
de las decisiones de ingenieria— son **produccion propia del equipo**, escritas contra la
evidencia primaria del proyecto y sostenibles ante el tribunal por cualquiera de sus
integrantes. Las amenazas a la validez del manuscrito son la excepcion y estan declaradas
arriba: se redactaron con asistencia a partir de resultados y desviaciones que el equipo
ya habia establecido.

Ninguna cifra, tabla, figura, resultado estadistico ni referencia bibliografica de este
trabajo procede de un modelo de lenguaje. Las cifras se generan por script desde los
datos crudos, con la correspondencia declarada en
[`07_Publicacion/dataset_zenodo/correspondencia_salidas.csv`](../07_Publicacion/dataset_zenodo/correspondencia_salidas.csv). Las
referencias de `referencias.bib` se verificaron individualmente y cada identificador
digital se resolvio antes de citarlo.

Los resultados no se redactaron antes de existir: la secuencia fue registrar el
protocolo, ejecutar el estudio, analizar con los scripts versionados y solo entonces
redactar.
