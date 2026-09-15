# Libreto de grabación de la defensa

**Proyecto SIGA — Sistema Inteligente de Gestión de Aulas · Equipo FGMMN**
Universidad Técnica Estatal de Quevedo · ISR-401 · Entrega Final (2B)
Versión 2.0 · 2026-09-08 · **una entrada por diapositiva**

---

## Cómo se usa

Cada apartado es **una diapositiva**. Lo que va entre comillas se dice; lo que va en
*cursiva* es una acción y no se lee.

No hay que memorizarlo. Hay que **entenderlo y decirlo con sus palabras**, pero sin salirse
de lo que afirma: cada cifra de aquí está verificada contra el repositorio, y si se cambia
una al hablar deja de estar respaldada.

**Reglas de la grabación**

- Una toma por diapositiva. Si alguien se traba, se corta y se repite **esa**, no todo.
- Nadie habla del trabajo de otro en primera persona. Quien no lo hizo dice «el equipo» o
  nombra a quien lo hizo.
- **25 minutos.** Cronómetro a la vista. Los tiempos de cada apartado suman 25:15, así que
  hay quince segundos de margen y ni uno más.

## Reparto

| | Diapositivas | Minutos |
|---|---|---|
| **Gary** | 1, 2, 4, 5, 6, 7, 14, 15 | 10:15 |
| **Yeranick** | 3, 8, 10, 12 | 9:00 |
| **Cedeño** | 9, 11, 13 | 6:00 |

Cada uno lleva su propia área: Gary el componente empírico, Yeranick el sistema y la
trazabilidad, Cedeño la evidencia de campo y la verificación. **Si el tribunal pregunta,
pregunta a quien lo expuso**, así que nadie exponga algo que no pueda defender sin la
diapositiva delante.

---
---

# 1 · GARY — Portada · 0:30

*Comparte pantalla con la presentación en modo presentador. Diapositiva 1.*

> «Buenos días. Somos el equipo FGMMN y presentamos SIGA, Sistema Inteligente de Gestión de
> Aulas, el proyecto fin de curso de Ingeniería de Requerimientos.
>
> Soy Gary Sánchez, me acompañan Yeranick Muñoz y Winston Cedeño. Vamos a repartirnos
> 25 minutos: yo llevo el componente empírico, Yeranick el sistema y la
> trazabilidad, y Winston la evidencia de campo y la verificación de la especificación.
>
> El estudio que presentamos compara los requisitos funcionales que elicita un analista
> humano con los que genera un modelo de lenguaje a partir del mismo material.»

*Avanza.*

---

# 2 · GARY — Problema y contribuciones · 1:45

*Diapositiva 2.*

> «Lo primero que conviene decir es que **SIGA tiene un cliente real e identificable**: la
> Facultad de Ciencias de la Computación de esta universidad. No es un dominio inventado
> para el curso. Las aulas existen, los proyectores fallan y hay personas que se ocupan de
> arreglarlos, y con esas personas hablamos.
>
> La pregunta de investigación es esta, y la digo textual como aparece en el manuscrito:
> **¿los requisitos funcionales que genera un modelo de lenguaje a partir del mismo material
> de entrevistas son comparables en calidad a los que elicita un analista humano?**
>
> Traemos 3 contribuciones.
>
> La primera es que la **comparación es pareada y ciega sobre el mismo corpus**. Los 2
> conjuntos de requisitos salen exactamente del mismo material fuente, no de corpus
> distintos por brazo, que es lo que hace la mayoría de los estudios previos y lo que impide
> saber si la diferencia viene del método o de los datos.
>
> La segunda es que **el pipeline de análisis es reproducible de principio a fin** y está
> publicado junto con el paquete de datos: los scripts, los datos crudos y los resultados.
> Cualquiera puede regenerar nuestras tablas y nuestras figuras.
>
> Y la tercera es el **registro completo del proceso**, incluidas sus complicaciones: un
> participante retiró su consentimiento y su material se eliminó entero; el campo se cerró en
> 10 entrevistas y se reabrió hasta 16; y se intentó un panel ampliado de evaluadores
> que no alcanzó acuerdo. Las 3 constan en el manuscrito con sus cifras.»

*Avanza y cede a Yeranick.*

---

# 3 · YERANICK — El sistema y sus perfiles · 2:15

*Diapositiva 3. En pantalla, el diagrama de contexto.*

> «SIGA tiene **6 capacidades centrales**: monitoreo ambiental en tiempo real, control
> remoto de los equipos del aula, alertas de anomalías, análisis predictivo de fallas,
> gestión de mantenimiento y reportes administrativos.
>
> Los perfiles con los que trabajamos son 3, y son los que de verdad usan las aulas:
> **docentes**, **coordinación académica** y **personal de servicios generales e
> infraestructura**. A ellos se suma el **personal técnico de tecnologías de la
> información**, que aparece en las sesiones de validación sobre el prototipo.
>
> El volumen de campo son **16 entrevistas** transcritas y anonimizadas, **10
> sesiones de validación** sobre los prototipos —3 de ellas con usuario técnico— y **12
> notas de campo**. Los 3 perfiles están bien representados; no es que hayamos hablado
> 15 veces con docentes y una con conserjería.
>
> El perfil menos consultado es el técnico, y es el destinatario de los requisitos con los
> umbrales más exigentes. Consta como amenaza a la validez de constructo en el manuscrito.»

*Avanza y cede a Gary.*

---

# 4 · GARY — Metodología · 2:15

*Diapositiva 4.*

> «El diseño es un **cuasi-experimento apareado y ciego**. Apareado porque cada requisito
> humano se compara con su equivalente generado sobre el mismo material; ciego porque los
> jueces no sabían qué requisito venía de dónde.
>
> El instrumento son **51 ítems evaluados en 5 dimensiones de calidad**:
> completitud, ausencia de ambigüedad, verificabilidad, corrección respecto de la fuente y
> consistencia interna. Escala de 1 a 5, con las anclas impresas en la propia hoja de
> puntuación.
>
> Los evaluaron **3 jueces independientes** de las personas entrevistadas.
>
> El plan de análisis se fijó antes de ver los datos: **Shapiro-Wilk** para decidir si la
> prueba es paramétrica o no, **corrección de Holm-Bonferroni** porque son 5
> comparaciones y no una, y **tamaño del efecto con intervalo de confianza al noventa y
> 5 % por bootstrap**.
>
> Y esto es lo importante: **el protocolo está registrado en el Open Science Framework
> antes de recoger un solo dato**, con DOI propio y sello temporal externo, del 2 de
> agosto. Eso es lo que permite afirmar que no reescribimos la pregunta después de ver los
> resultados. Las desviaciones que hubo respecto de ese registro están documentadas una a
> una, no disimuladas.»

*Avanza.*

---

# 5 · GARY — Resultados 1 de 3 · 1:30

*Diapositiva 5. En pantalla, la tabla de descriptivos.*

> «Empecemos por lo que dicen las cifras crudas.
>
> **En las 5 dimensiones, la media y la mediana del modelo igualan o superan a las del
> analista humano.** Las 5. Si nos quedáramos aquí, el titular sería que el modelo
> escribe mejores requisitos.
>
> Pero una diferencia favorable en los datos crudos **no implica, por sí sola, significancia
> estadística**. Las dos diapositivas siguientes son exactamente sobre eso.»

*Avanza.*

---

# 6 · GARY — Resultados 2 de 3 · 1:45

*Diapositiva 6. En pantalla, la tabla de hipótesis.*

> «Aquí está la corrección por comparaciones múltiples, y conviene mirarla despacio.
>
> El caso más cercano a la significancia es **consistencia interna**. Antes de corregir daba
> un p de **0,012**: por debajo del 0,05 convencional, o sea,
> parecía significativo.
>
> Después de aplicar **Holm-Bonferroni**, ese mismo p pasa a **0,059**. Ya no lo es.
>
> Y ese era el mejor caso. **Ninguna de las 5 dimensiones sobrevive la corrección.**
>
> Es la diferencia entre un hallazgo y un artefacto. Cuando se hacen 5 comparaciones
> sobre los mismos datos, la probabilidad de que alguna salga significativa por azar deja de
> ser el 5 %. Corregir no es un formalismo: es lo que impide anunciar un
> resultado que no está.»

*Avanza.*

---

# 7 · GARY — Resultados 3 de 3 · 1:45

*Diapositiva 7. En pantalla, la figura de tamaños de efecto y el cálculo de potencia.*

> «La tercera parte explica **por qué** no sobrevive nada.
>
> Los tamaños del efecto, calculados con el requisito como unidad —veinticinco requisitos
> del equipo frente a veintiséis del modelo—, son **pequeños**, de menos cero coma doce a
> menos cero coma veintiséis, y sus intervalos de confianza al 95 % **cruzan el cero**. Un intervalo que cruza el cero significa que
> los datos son compatibles con que la diferencia sea a favor, en contra, o inexistente.
>
> Y la razón es el tamaño de muestra. Calculamos la potencia estadística real del estudio:
> con 3 jueces es del **8,4 %**, frente al 80 % que se
> considera convencional. Para alcanzar ese 80 % harían falta **34
> observaciones apareadas**.
>
> La potencia está calculada por script y versionada en el paquete de datos, y es la cifra
> que sostiene toda la discusión que viene a continuación.»

*Avanza y cede a Yeranick.*

---

# 8 · YERANICK — Discusión y amenazas a la validez · 2:15

*Diapositiva 8.*

> «La implicación principal es esta: **la tendencia favorable al modelo no se sostiene
> estadísticamente con este tamaño de muestra**. No decimos que el modelo sea peor; decimos
> que con estos datos no se puede afirmar que sea mejor.
>
> Las amenazas las agrupamos en las 4 categorías habituales.
>
> **Validez interna.** Un panel de solo 3 jueces y una potencia muy baja. Es la más
> grave y ya la han visto cuantificada.
>
> **Validez externa.** Un solo dominio, un solo idioma, un solo modelo. Esto no generaliza
> por sí solo, y no pretendemos que lo haga.
>
> **Validez de constructo.** El modelo tuvo exposición previa parcial al material del
> conjunto humano, así que su corpus fuente no coincide exactamente con el del otro brazo.
> Está declarado.
>
> **Validez de conclusión.** Intervalos muy anchos, consecuencia directa del tamaño de
> muestra.
>
> Sobre la primera hicimos algo más que declararla: **intentamos corregirla**. Ampliamos el
> panel de 3 a 7 evaluadores, en 2 rondas. En las 2, el acuerdo medido con kappa
> de Fleiss salió **negativo** —−0,008 y −0,026—, indistinguible del azar.
>
> Lo interesante es por qué. Habíamos escondido enunciados repetidos en la hoja de
> puntuación, sin decírselo a nadie. **3 de los 7 evaluadores se contradijeron a sí
> mismos** hasta en 3 puntos sobre el mismo enunciado, en la misma sesión. Uno no repitió
> ninguna de sus 12 puntuaciones. Si alguien no coincide consigo mismo, no puede coincidir
> con otro: el ruido está dentro de cada evaluador, y por eso ampliar el panel no lo corrige.
> Esta rúbrica necesita evaluadores entrenados, y esa es la conclusión que reportamos.»

*Avanza y cede a Cedeño.*

---

# 9 · CEDEÑO — Paquete de replicación · 2:00

*Diapositiva 9.*

> «Todo lo que acaban de ver se puede rehacer sin pedirnos nada.
>
> Publicamos un **paquete de replicación** con los datos crudos, los scripts de análisis y los
> resultados. **Una sola orden regenera las tablas y las figuras del manuscrito** a partir de
> los datos. No es un enlace a una carpeta: es el estudio entero, ejecutable.
>
> Y está depositado bajo **3 identificadores persistentes**, los 3 comprobados.
>
> El primero es **Zenodo**, con el DOI de la versión 2B-1.12.0 del paquete de datos, bajo
> licencia Creative Commons. Ese identificador fija el contenido exacto: quien lo siga dentro
> de 5 años encuentra lo mismo que citamos hoy.
>
> El segundo es **el Open Science Framework**, donde está el protocolo registrado el 2 de
> agosto, antes de recoger un solo dato, con sello temporal externo al equipo.
>
> Y el tercero es **Software Heritage**, el archivo universal de código fuente, que conserva
> nuestro código con su propio identificador permanente.
>
> Sobre ese depósito pasamos la autoevaluación **FAIR con la herramienta F-UJI**, que es
> externa y automatizada: **22 indicadores de 26, un 84,62 %**. En localizable sacamos **7 de 7**.
>
> Es la parte del trabajo que sobrevive al curso: dentro de un año el repositorio puede
> cambiar, pero esos 3 identificadores siguen resolviendo.»

*Avanza y cede a Yeranick.*

---

# 10 · YERANICK — Demostración del prototipo · 2:30

> ### Antes de grabar: preparación obligatoria
>
> *Esto se hace **antes** de empezar a grabar, no delante del tribunal.*
>
> **1. Comprobar la versión de Node.** Hace falta 22.5 o superior:
>
> ```bash
> node --version
> ```
>
> **2. Levantar el prototipo** desde `05_MVP/codigo_fuente/`:
>
> ```bash
> cd 05_MVP/codigo_fuente
> npm install
> npm start
> ```
>
> Al primer arranque crea la base SQLite y siembra los datos de ejemplo solo. Queda en
> **`http://localhost:3000`**.
>
> **3. Dejar el navegador abierto en la pantalla de login**, sin sesión iniciada.
>
> **No use `docker compose up`.** Está en el repositorio pero `05_MVP/README.md` declara que
> nunca se ejecutó, porque la máquina donde se preparó la entrega no tiene Docker. La vía
> verificada, con fecha del 29 de agosto, es la de Node. Si el tribunal pregunta por Docker,
> se dice exactamente eso.
>
> **Si algo falla y hay que empezar de cero:** `rm -f siga.sqlite` y `npm start` otra vez.

*Diapositiva 10. Comparte la ventana del navegador, no la presentación.*

> «Vamos a ejecutar el prototipo en vivo. Son 2 escenarios que elegimos de antemano y que
> están en la matriz de trazabilidad.
>
> **El primero es el acceso diferenciado por roles, el requisito RF-19.** Entro como técnico
> de infraestructura.»

*Escribe `tecnico` / `tecnico123`. Entra.*

> «Vean el menú: Aulas, Alertas, Mantenimiento y Configuración. **4 módulos.** No ve
> Reportes ni Bitácora.
>
> Ahora salgo y entro como administrador.»

*Cierra sesión. Escribe `admin` / `admin123`. Entra.*

> «**Los 6 módulos.** Aparecen Reportes y Bitácora.
>
> Esto no es un detalle de interfaz. Es lo que nos pidieron los 2 usuarios técnicos con
> los que validamos: que el control corresponda al docente asignado o a un administrador
> autorizado, y que los estudiantes no puedan manipular los equipos desde la plataforma. La
> restricción de diseño RD-10 recoge eso, y aquí está implementada.
>
> **El segundo escenario es la cadena completa: sensor, alerta, ticket.** Los requisitos
> RF-01, RF-08 y RF-11.»

*Va al panel. Activa el simulador de sensores.*

> «El simulador genera lecturas ambientales sin necesidad de hardware. Cuando una lectura
> supera el umbral, el sistema **levanta la alerta automáticamente**…»

*Espera a que aparezca la alerta. La abre.*

> «…aquí está, con el aula, la magnitud y la hora. Y desde la propia alerta se **abre el
> ticket de mantenimiento**.»

*Crea el ticket. Lo muestra en el módulo de mantenimiento.*

> «Eso cierra la cadena que hoy no existe en la facultad: ahora mismo las incidencias se
> comunican de palabra al terminar la clase, y no queda registro. Nos lo dijeron los 3
> usuarios técnicos, cada uno por su lado.
>
> El prototipo cubre **17 de los 20 requisitos obligatorios, un 85 %**, frente al 60 % que pide la guía. El detalle requisito por
> requisito está en `cobertura_requisitos.csv`.»

*Vuelve a la presentación. Avanza y cede a Cedeño.*

---

# 11 · CEDEÑO — Verificación y control de cambios · 2:00

*Diapositiva 11.*

> «La especificación no la leímos por encima: **la inspeccionamos con método**.
>
> Aplicamos una **inspección de Fagan**, la INS-01, con 5 roles repartidos entre 3
> personas y con una regla: **el autor y el moderador nunca coinciden**. Encontró
> **16 defectos**: 3 críticos, 9 mayores y 4 menores. Eso da una densidad
> de **0,64 defectos por requisito funcional**.
>
> Después hicimos la **re-inspección REINS-01**, y aquí la regla fue que **cada defecto lo
> verifica quien no lo corrigió**. Quedaron **15 cerrados y 1 residual**: el DEF-06, la
> apertura individual de cámara, que el comité de control de cambios difirió de forma
> expresa en la solicitud SC-03.
>
> El comité, el CCB-01, resolvió **4 solicitudes de cambio**: 3 aprobadas y esa
> diferida.
>
> De ahí sale la métrica de corrección: **1 residual sobre 25 requisitos
> funcionales, 0,04**, frente a la referencia de 0,05.
> Cumple. El margen es de 1 solo defecto: con 2 residuales el valor sería 0,08.»

*Avanza y cede a Yeranick.*

---

# 12 · YERANICK — Trazabilidad y gestión · 2:00

*Diapositiva 12.*

> «La matriz de trazabilidad tiene **75 filas**, por encima de las 60 que
> pide el criterio, y **ninguna celda vacía**.
>
> De esas 75, **41 cierran la cadena completa**: desde la fuente de
> campo hasta el criterio de aceptación, pasando por el caso de uso, la clase, el proceso y
> el caso de prueba.
>
> Las otras 34 **no están a medio hacer: no pueden cerrar**, y cada una dice
> por qué. 9 son huérfanas porque el requisito nace del análisis de la Ley Orgánica de
> Protección de Datos y no de una entrevista; inventarles una fuente de campo sería
> fabricarla. 16 son parciales. Y 9 son restricciones de diseño, que se verifican
> por revisión y no por caso de prueba. **La cifra se recalcula con un script**, no se cuenta
> a mano.
>
> El tablero de gestión tiene **61 actividades**: 25 requisitos
> funcionales, 24 no funcionales y 12 restricciones de diseño.
>
> Y la sincronización entre el tablero y la matriz es del **100 %**: 61 de
> 61. Ni un requisito sin actividad, ni una actividad sin requisito. También se
> recalcula por script sobre el export del tablero.
>
> Ese 100 % **mide correspondencia entre dos listas, no avance**: las 61
> actividades están en «Por hacer», que es su estado en el tablero.»

*Avanza y cede a Cedeño.*

---

# 13 · CEDEÑO — Evidencia de campo · 2:00

*Diapositiva 13.*

> «El corpus son **16 entrevistas** transcritas y anonimizadas, y **las 16
> están codificadas temáticamente**: 136 fragmentos bajo 50 códigos.
> Las 6 últimas las codificamos el 6 de septiembre, repartidas entre los 3 por
> entrevista completa, y cada cita se comprobó literal contra su transcripción antes de
> entrar.
>
> La **curva de saturación alcanza inflexión en la entrevista EV-23**, la 14.ª, y
> cierra en 1,333 frente a un umbral de 2,5. Como el
> resultado cambió justo cuando nos convenía, probamos **las 720 ordenaciones
> posibles** del bloque de entrevistas del mismo día: satura en las 720.
>
> La **doble codificación** la hicimos 2 personas por separado sobre el mismo subconjunto.
> El kappa de Cohen es de **0,548 a nivel de código**, que es
> acuerdo moderado, y de **0,911 a nivel de categoría**. Damos las dos
> porque la diferencia entre ellas es el hallazgo: **coincidimos casi siempre en de qué trata
> el fragmento y discrepamos en qué código exacto asignarle**.
>
> En validación, **10 walkthroughs sobre los prototipos, 3 con usuario técnico**.
>
> Y de las 12 notas de campo, **6 son manuscritas y contemporáneas**, escritas durante
> la sesión, y las otras 6 son reconstrucción documentada, con esa condición indicada en
> su propia cabecera.»

*Avanza y cede a Gary.*

---

# 14 · GARY — Participación · 0:25

*Diapositiva 14.*

> «El reparto de estos 25 minutos sigue la contribución real de cada uno, que está
> declarada confirmación por confirmación en la matriz de aporte individual: **10 minutos, 9 y 6**. Los 3 superamos el mínimo de 4 minutos por integrante.»

*Avanza.*

---

# 15 · GARY — Cierre · 0:20

*Diapositiva 15.*

> «Todo lo que hemos dicho es comprobable: el repositorio es público, el protocolo está
> registrado en OSF y el paquete de replicación tiene DOI de Zenodo.
>
> Gracias. Quedamos a sus preguntas.»

*Deja la diapositiva 15 en pantalla durante las preguntas.*

---
---

# Antes de grabar — lista de comprobación

- [ ] **Ensayo cronometrado completo.** Los tiempos suman 25:15. Si se pasan, lo primero que
      se recorta es la diapositiva 2; lo último que se toca es la 8, que es lo que distingue
      este trabajo.
- [ ] **El prototipo levantado y probado**, con los dos escenarios ejecutados de principio a
      fin. No se improvisa delante del tribunal.
- [ ] Navegador en `http://localhost:3000`, sin sesión iniciada, y la presentación en otra
      ventana.
- [ ] Micrófono probado en los tres equipos.
- [ ] Cada uno ha leído **el banco de preguntas** de su área.

**Aviso para el equipo, no se proyecta:** una falla total de la demostración anula el
criterio del prototipo. Practiquen el flujo exacto antes, con el servidor ya arrancado.

# Si el tribunal aprieta

**«Su resultado depende de haber elegido tres jueces.»**

> «Depende del registro previo, que fija 3 y es anterior a los datos. Y los 3
> concuerdan entre sí: coinciden exactamente en el 53 % de sus
> puntuaciones, frente al 37 % de los 7, que es justo lo que da el
> azar. El criterio para sustituirlos lo escribimos antes de mirar los datos y no se cumplió.
> Cambiarlo después habría sido elegir el resultado.»

**«¿No saturó porque les convenía?»**

> «Es la pregunta correcta. Por eso probamos las 720 ordenaciones posibles y
> satura en todas. Y por eso declaramos 3 reservas en el propio documento, incluida una
> que va en contra: las instrucciones de codificación pedían reutilizar códigos, y eso empuja
> hacia la saturación.»

**«¿Por qué no hicieron el enfoque de explicabilidad?»**

> «Porque el enfoque se elegía. La rúbrica de la entrega anterior dice que cada equipo elige
> uno y solo uno, y exige declararlo y registrarlo en OSF antes de recoger datos. Elegimos el
> enfoque uno y lo registramos el 2 de agosto, antes del primer dato. La tabla de la
> entrega final orienta y recomienda, y permite modificar declarándolo por escrito, que es lo
> que hicimos.»
