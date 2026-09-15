# Guion de la defensa oral — Proyecto SIGA

**Sistema Inteligente de Gestion de Aulas · Equipo FGMMN**
Universidad Tecnica Estatal de Quevedo · ISR-401 Ingenieria de Requerimientos · Entrega Final (2B)

---

## Modalidad: defensa individual

**La defensa es individual.** Cada integrante expone el proyecto completo por separado ante
el tribunal, y responde por la totalidad del trabajo: la especificacion, el diseno del
estudio empirico, los resultados y sus amenazas a la validez.

En la fecha de la defensa el equipo lo integraban dos personas, y **ambas rindieron
la suya**:

| Integrante | Rol en el proyecto |
|---|---|
| Sanchez Cornejo, Gary Alberto | Analista lider; especificacion, componente empirico e integracion |
| Munoz Quinonez, Yeranick Esther | Documentacion, trazabilidad, auditoria de calidad y gestion de evidencias |

Por ser individual, **no hay reparto de tiempos entre personas**. La estructura de bloques
que sigue describe como se organiza la exposicion de cada integrante dentro de los 25
minutos, seguidos de 10 minutos de preguntas.

**Lo que el tribunal evalua en esta modalidad** no es que cada quien defienda su parte, sino
lo contrario: que cada integrante sostenga el proyecto entero, incluidas las decisiones que
no tomo. Quien preparo la trazabilidad tiene que poder explicar por que la prueba de
hipotesis es apareada, y quien corrio el analisis tiene que poder explicar como se cierra
una cadena de trazabilidad rota.

---

## Bloque 1 — Problema y contribuciones (3 min)

- SIGA es un sistema real, con cliente identificable: la Facultad de Ciencias de la
  Computación y Diseño Digital de la UTEQ. No es un ejercicio de curso sobre un
  dominio ficticio.
- El problema de investigación: ¿los Requisitos Funcionales que genera un LLM a partir
  del mismo material de entrevistas son comparables en calidad a los que elicita un
  analista humano?
- Tres contribuciones concretas:
  1. Comparación pareada y ciega usando el **mismo corpus de entrevistas** para ambos
     orígenes — no un corpus distinto por brazo, que es lo que hacen la mayoría de los
     estudios previos.
  2. Un pipeline de análisis 100% reproducible, publicado con el paquete de datos.
  3. Divulgación explícita de las complicaciones metodológicas reales del estudio ---
     el retiro de consentimiento de un participante, el cierre de campo en N=10 y su
     reapertura, y el fracaso de las dos vueltas del panel ampliado --- en vez de
     ocultarlas.
- Pregunta de investigación (RQ1): decirla textual, tal como aparece en el manuscrito.

## Bloque 2 — El sistema y sus stakeholders (3 min)

- Las 6 capacidades centrales de SIGA (monitoreo ambiental, control remoto,
  alertas, análisis predictivo, mantenimiento, reportes).
- Los tres perfiles de usuario reales entrevistados: docentes, coordinación
  académica, conserjería/infraestructura — con foto o diagrama de contexto en
  pantalla (`03_Modelado/01_Contexto/`).
- Mencionar brevemente el volumen real de campo: **16 entrevistas**, con tres perfiles
  bien representados, **las dieciseis codificadas**: 136 fragmentos bajo 50 codigos. Las
  seis de la ronda terminal del 2026-09-03 se codificaron el 2026-09-06. Si preguntan por el
  cuasi-experimento, sus dos conjuntos salen de las diez primeras: ver I5 del banco.

## Bloque 3 — Metodología del componente empírico (4 min)

- Diseño: cuasi-experimento apareado, ciego, con 3 jueces independientes de las
  personas entrevistadas.
- 51 ítems evaluados en 5 dimensiones de calidad (completitud, ausencia de
  ambigüedad, verificabilidad, corrección respecto de la fuente, consistencia
  interna), escala 1–5.
- Plan de análisis: Shapiro-Wilk para elegir prueba paramétrica o no paramétrica,
  corrección de Holm-Bonferroni por comparaciones múltiples, tamaño del efecto con
  intervalo de confianza al 95% por *bootstrap*.
- Mencionar el registro previo en OSF (DOI 10.17605/OSF.IO/7PQ3H) y que las
  desviaciones respecto de ese registro están documentadas explícitamente.

## Bloque 4 — Resultados (6 min)

- Mostrar la tabla de descriptivos: en las 5 dimensiones, la mediana/media del LLM
  es igual o mayor que la del humano.
- Mostrar la tabla de hipótesis: **antes** de corregir, Consistencia_interna daba
  p=0,012 (parecía significativo); **después** de Holm-Bonferroni, p=0,059 — ya no
  lo es. Ninguna dimensión sobrevive la corrección.
- Mostrar la figura de tamaños de efecto con sus intervalos de confianza: con el
  requisito como unidad (25 frente a 26) los efectos son pequeños, de −0,12 a −0,26,
  y todos los intervalos cruzan el cero — mostrar visualmente por qué eso importa.
- Mostrar el cálculo de potencia: con 3 jueces, potencia real = 8,4%; se necesitarían
  34 pares para el 80% convencional. Esto explica por qué los intervalos son tan
  anchos.
- Mencionar brevemente la curva de saturación temática: **alcanza inflexión en `EV-23`**
  y cierra en 1,333 frente a un umbral de 2,500. Con las diez primeras no saturaba; la
  ronda terminal del 3 de septiembre la cerró. Decir también que se comprobó sobre las
  720 ordenaciones del bloque del mismo día — un párrafo, no más de 30 segundos.

## Bloque 5 — Discusión y amenazas a la validez (4 min)

- Implicación principal: la tendencia favorable al LLM en las cifras crudas **no**
  se sostiene estadísticamente con este tamaño de muestra — es un ejemplo concreto de
  por qué la corrección por comparaciones múltiples y el cálculo de potencia importan,
  no un formalismo.
- Las 4 categorías de amenazas, una frase cada una:
  - Interna: panel de 3 jueces, muy baja potencia.
  - Externa: un solo dominio, un solo idioma, un solo modelo — no generaliza sola.
  - Constructo: el LLM tuvo exposición previa parcial al conjunto humano, y el corpus
    fuente del LLM (11 entrevistas) ya no coincide exactamente con el corpus que
    respalda al conjunto humano (10, tras excluir una entrevista por retiro de
    consentimiento).
  - Conclusión: intervalos de confianza muy anchos por el tamaño de muestra pequeño.

## Bloque 6 — Conclusiones y trabajo futuro (3 min)

- Respuesta a RQ1: no se puede confirmar ni descartar una diferencia de calidad con
  el tamaño de muestra actual; se declara así explícitamente, sin sobre-interpretar
  la tendencia numérica favorable al LLM.
- Trabajo futuro concreto (citar los 3 del manuscrito): ampliar el panel a 34 jueces,
  re-generar los dos conjuntos sobre el corpus completo de 16 entrevistas, y ampliar la
  ronda terminal más allá del perfil docente, que es la reserva que queda declarada sobre
  la saturación.
- Cerrar reafirmando las 3 contribuciones del bloque 1 con la evidencia ya mostrada.

## Bloque 7 — Demostración del prototipo (2 min)

- Ejecutar en vivo (idealmente `docker compose up`, o el entorno estable que se haya
  preparado) los **dos escenarios de la matriz de trazabilidad** ya identificados de
  antemano — decidir cuáles antes del simulacro, no improvisar el día de la defensa.
- Usar únicamente las credenciales de demostración documentadas en `05_MVP/README.md`.
  Nunca credenciales reales de personas del cliente.
- Si la demo falla por completo, es C13 = 0 — practicar el flujo exacto varias veces
  antes, con la red/entorno ya verificado.

---

## Preguntas del tribunal (10 min) — preparación sugerida

Al ser individual, **cada integrante responde por el proyecto entero**. No hay temas
asignados por persona. Los que el tribunal suele tocar, y que conviene poder responder
sin mirar las diapositivas, son:

- **Por que REFSQ y no el journal.** La plantilla del manuscrito es Springer LNCS, que es la
  de REFSQ; el envio no exige cargo por procesamiento y el calendario cabe en el semestre.
- **El registro previo y sus desviaciones.** Que se preregistro, cuando, y por que las diez
  desviaciones se declaran en lugar de disimularse.
- **La potencia del estudio.** Por que un panel de tres jueces da una potencia de 0,084, que
  significa eso, y por que se reporta en lugar de omitirlo.
- **La matriz de trazabilidad.** Como se cierra una cadena rota y por que las 75 filas no
  tienen ninguna celda vacia.
- **El cierre en diez entrevistas, y su reapertura.** Que se declaro entonces, y por que el
  corpus son ahora dieciseis, **las dieciseis codificadas**, con la saturacion alcanzada en
  `EV-23` y comprobada sobre las 720 ordenaciones del bloque del mismo dia.
- **Los dos umbrales corregidos.** `RNF-04` paso de dos a cinco minutos y `RNF-14` dejo de
  tener una cifra unica, los dos **contra evidencia de campo**. Es la respuesta mas fuerte que
  tienen: corrigieron la especificacion porque preguntaron, no porque les convenia.
- **Las tres sesiones tecnicas, y lo que costo reunirlas.** `TIC-01`, `TIC-02` y `TIC-03`,
  del 4, 5 y 7 de septiembre: el area de TICS estaba en remodelacion el primer dia. Lo que
  sigue corto es el alcance, quince minutos por sesion. Y por que los conserjes no cuentan
  como perfil tecnico, que lo dicen
  ellos mismos en sus transcripciones.

**El banco de preguntas cubre estas y ocho mas** en su seccion G, cada una con el artefacto
que la respalda: `08_Defensa/banco_preguntas.md`.

> **Advertencia de la guia.** La defensa se puede reprobar si el tribunal detecta que un
> integrante no puede explicar decisiones basicas del proyecto, o si aparecen en las
> diapositivas resultados que no estan en el manuscrito ni en los scripts de analisis, lo
> que activa el gatekeeper G4. **Todo numero que se proyecte tiene que poder senalarse en una
> tabla o figura ya generada por el pipeline.**
