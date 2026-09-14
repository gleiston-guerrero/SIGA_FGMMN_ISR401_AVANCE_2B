# Declaración ética y proceso de consentimiento informado

**Paquete de replicación SIGA — Sistema Inteligente de Gestión de Aulas**
Equipo FGMMN · Universidad Técnica Estatal de Quevedo (UTEQ) · ISR-401 · 2026

Documento exigido por la Sección 7.2 de la Guía de Entrega 4 (2B). Describe el marco
ético del estudio, el proceso de consentimiento informado aplicado a cada participante
y el cumplimiento de la **Ley Orgánica de Protección de Datos Personales del Ecuador**
(Registro Oficial Suplemento 459, 26 de mayo de 2021, en adelante LOPDP).

---

## 1. Naturaleza y riesgo del estudio

Estudio empírico de **ingeniería de requerimientos** con componente cualitativo
(entrevistas semiestructuradas, observación y sesiones de validación) y componente
cuantitativo (cuestionario y cuasi-experimento apareado de evaluación ciega de calidad
de requisitos).

- **Población.** Personal docente, de coordinación académica y de conserjería e
  infraestructura de la Facultad de Ciencias de la Computación y Diseño Digital de la
  UTEQ, mayores de edad, en el ejercicio de sus funciones profesionales.
- **Riesgo evaluado.** **Mínimo.** No se administran intervenciones clínicas,
  farmacológicas ni psicológicas. No se recogen datos de categoría especial (salud,
  origen étnico, convicciones religiosas, afiliación política o sindical, datos
  biométricos con fines identificativos, orientación sexual).
- **Riesgo residual identificado.** Reidentificación por inferencia contextual, dada
  la población reducida. Se mitiga según el procedimiento de
  [`07_Publicacion/dataset_zenodo/anonimizacion.md`](../../07_Publicacion/dataset_zenodo/anonimizacion.md).
- **Menores de edad.** El estudio **no** incluye participantes menores de edad. La
  política aplicable en caso de contacto incidental está documentada en el anexo
  `CB5_Politica_Datos_Menores` del expediente ético de la Entrega 2A.

---

## 2. Proceso de consentimiento informado

### 2.1 Secuencia aplicada a cada participante

1. **Contacto inicial** por correo institucional o de forma presencial, explicando el
   propósito académico del estudio y solicitando una cita.
2. **Entrega del formulario de consentimiento** antes de iniciar cualquier grabación.
3. **Lectura conjunta y espacio para preguntas**, sin límite de tiempo.
4. **Firma manuscrita** del formulario, con número de cédula, fecha y hora.
5. **Autorización específica de grabación** de audio y video, como casilla
   independiente del consentimiento general: una persona puede consentir la entrevista
   y negar la grabación.
6. **Autorización específica para el uso de sus datos anonimizados en publicaciones
   científicas revisadas por pares**, como tercera casilla independiente. Este punto
   es obligatorio en la Entrega 2B para todo participante que se incorpore en la ronda
   terminal.
7. **Entrega de una copia** del formulario firmado a la persona participante.
8. **Archivo** del original en `02_Evidencias/Consentimientos/` con nomenclatura
   `AAAA-MM-DD_Perfil_CODIGO_Consentimiento.pdf`, donde `CODIGO` es el seudónimo
   (`DOC-nn`, `COORD-nn`, `CONS-nn`, `TIC-nn`): ningún nombre de archivo contiene el
   nombre de una persona.

### 2.2 Contenido mínimo del formulario

- Identificación del proyecto, de la asignatura, de la institución y del docente
  responsable.
- Propósito del estudio, en lenguaje no técnico.
- Descripción de lo que se pedirá a la persona y duración estimada.
- Declaración de que la participación es **voluntaria** y puede interrumpirse en
  cualquier momento **sin consecuencia académica ni laboral alguna**.
- Derecho a **retirar el consentimiento** con posterioridad y consecuencias del
  retiro (ver Sección 4).
- Descripción de los datos que se recogen y del uso previsto.
- Declaración explícita de que los datos anonimizados se depositarán en un repositorio
  público (Zenodo) bajo licencia CC BY 4.0 y podrán ser reutilizados por terceros.
- Declaración de que los materiales identificables (video, audio, consentimiento
  firmado) **no** se publican y permanecen bajo acceso restringido.
- Plazo de conservación de los datos y procedimiento de destrucción.
- Datos de contacto para el ejercicio de derechos.
- Espacio para firma manuscrita, número de cédula, fecha y hora.

### 2.3 Consentimiento en la ronda terminal (Entrega 2B)

Conforme a la Sección 2.3 de la guía, **cada participante que se incorpore en la ronda
terminal firma un consentimiento nuevo**, redactado en cumplimiento de la LOPDP, con
autorización explícita para el eventual uso de sus datos anonimizados en publicaciones
científicas revisadas por pares. Los participantes de rondas anteriores fueron
cubiertos por la adenda de segunda ronda del expediente ético de 2A.

---

## 3. Cumplimiento de la LOPDP

| Principio de la LOPDP | Aplicación concreta en este estudio |
|---|---|
| **Licitud y transparencia** | Consentimiento previo, libre, específico, informado e inequívoco, documentado por escrito y con firma manuscrita. |
| **Finalidad** | Los datos se recogen exclusivamente para la elicitación y validación de requisitos del sistema SIGA y para el estudio empírico asociado. No se emplean para ningún otro fin. |
| **Minimización** | Solo se recogen los datos estrictamente necesarios. No se solicitan datos de categoría especial. Las variables demográficas se publican agregadas. |
| **Seudonimización** | Toda persona se identifica por seudónimo estable (`DOC-nn`, `COORD-nn`, `CONS-nn`). La tabla de correspondencia no se publica. |
| **Confidencialidad y seguridad** | El material identificable permanece en repositorio de acceso restringido al equipo, al docente responsable y al tribunal. Se firmó compromiso de confidencialidad por cada integrante. |
| **Conservación limitada** | Los materiales identificables se conservan **hasta el 30 de septiembre de 2028** y en esa fecha se destruyen, conforme a la Sección 3.2. |
| **Responsabilidad proactiva** | El procedimiento de anonimización se verifica mediante doble revisión independiente y acta firmada antes de todo depósito público. |

### 3.1 Derechos de las personas participantes

Toda persona participante puede ejercer, en cualquier momento y sin necesidad de
justificar su decisión, los derechos de **acceso, rectificación, eliminación,
oposición, portabilidad** y a no ser objeto de decisiones automatizadas, dirigiéndose
al contacto de la Sección 6.

### 3.2 Declaración expresa del tratamiento

Declaración única de los cuatro elementos que la LOPDP exige conocer antes de tratar datos
personales. Rige para todo el material del estudio que identifica o puede identificar a una
persona participante.

| Elemento | Declaración |
|---|---|
| **Base de licitud** | **Consentimiento del titular** (LOPDP, art. 7, numeral 1), otorgado por escrito, con firma manuscrita y casillas independientes para la entrevista, la grabación y el uso de los datos anonimizados en publicaciones. Sin consentimiento firmado no se trata ningún dato, y su retiro detiene el tratamiento conforme a la Sección 4. |
| **Finalidad** | Elicitar y validar los requisitos del sistema SIGA y ejecutar el estudio empírico del Proyecto Fin de Curso de ISR-401. Ningún dato se cede a terceros ni se usa para otro fin. Lo único que se publica son datos **anonimizados**, bajo CC BY 4.0. |
| **Plazo de conservación** | El material identificable —vídeo, audio, consentimientos firmados y tabla de correspondencia entre código y persona— se conserva **hasta el 30 de septiembre de 2028**: los 24 meses desde la finalización del proyecto que fija la política de retención del plan de gestión de datos aprobado (`Anexos/A04_Plan_Gestion_Datos.pdf`, apartado 9), contados desde el cierre del Proyecto Fin de Curso. En esa fecha se destruye el contenedor cifrado, se retira del repositorio y se levanta el acta de destrucción que exige el apartado 10 del mismo plan. Los datos anonimizados ya publicados no caducan, porque no permiten identificar a nadie. |
| **Responsable del tratamiento** | **Sánchez Cornejo, Gary Alberto** — <gsanchezc6@uteq.edu.ec>, analista líder del equipo: custodia el contenedor cifrado y su contraseña, y responde por el tratamiento que hace el equipo. El plan de gestión de datos (A04, apartado 13) asigna la **gestión** de los datos al docente responsable, **Ing. Gleiston Guerrero Ulloa**, con el apoyo del analista líder; el docente es además el contacto para ejercer los derechos de la Sección 3.1 y quien firma el acta de destrucción. |

---

## 4. Retiro del consentimiento

Si una persona retira su consentimiento:

1. Se **detiene inmediatamente** todo tratamiento nuevo de sus datos.
2. Se **eliminan** sus grabaciones de audio y video, su transcripción y su
   consentimiento del repositorio de evidencia, dejando constancia del hueco en el
   registro de evidencias sin revelar su identidad.
3. Si el retiro ocurre **antes** del depósito en Zenodo, sus datos se excluyen del
   paquete.
4. Si ocurre **después** del depósito, se publica una nueva versión del paquete sin
   sus datos; la versión anterior queda marcada como obsoleta en Zenodo. Se advierte a
   la persona, en el propio formulario de consentimiento, que las copias ya
   descargadas por terceros no son recuperables.
5. El retiro se documenta como **desviación respecto del protocolo pre-registrado** en
   `06_Experimento/registro_previo/bitacora_desviaciones.pdf`, indicando el impacto sobre el tamaño muestral
   sin revelar la identidad de quien se retiró.

---

## 5. Aprobación institucional y expediente ético

El expediente ético completo fue presentado en la Entrega 3 (2A) y se conserva en el
repositorio histórico
<https://github.com/gleiston-guerrero/SIGA_FGMMN_ISR401_AVANCE_2A> bajo `08_Etica/`:

| Anexo | Contenido |
|---|---|
| A01 | Protocolo de investigación |
| A02 | Instrumentos de recolección |
| A03 | Formulario de consentimiento informado |
| A04 | Plan de gestión de datos |
| A05 | Aval institucional |
| A06 | Declaración de conflicto de intereses |
| A07 | Compromiso de confidencialidad del equipo |
| A08 | Hoja de vida del docente responsable |
| A09 | Nómina del equipo |
| A10 | Cronograma Gantt |
| A11 | Análisis de riesgos |
| Adenda | Adenda de segunda ronda de campo |
| CB1–CB5 | Anexos de Categoría B (aval específico, protección de datos de la comunidad, no correlación con el SGA, política de datos de menores) |

**Estado de la aprobación.** El oficio de solicitud de aprobación ética consta en
[`Oficio_Solicitud_Aprobacion_Etica.pdf`](Oficio_Solicitud_Aprobacion_Etica.pdf) y la
solicitud completa en [`Solicitud_Aprobacion_Etica_SIGA.pdf`](Solicitud_Aprobacion_Etica_SIGA.pdf).
El número de oficio y la fecha de la resolución se incorporan a este documento en cuanto
la autoridad institucional los emita.

---

## 6. Contacto para el ejercicio de derechos

**Ing. Gleiston Guerrero Ulloa** — docente responsable del proyecto
Facultad de Ciencias de la Computación
Universidad Técnica Estatal de Quevedo
Campus Central, Av. Quito km 1½ vía a Santo Domingo de los Tsáchilas
Quevedo, Los Ríos, Ecuador

**Corresponsal del equipo:** Gary Alberto Sánchez Cornejo — <gsanchezc6@uteq.edu.ec>

---

## 7. Declaración de conflicto de intereses

Las personas autoras declaran no tener conflictos de interés financieros ni personales
que pudieran haber influido en el trabajo reportado. El estudio se realizó sin
financiamiento externo, en el marco de la asignatura ISR-401 Ingeniería de
Requerimientos de la Universidad Técnica Estatal de Quevedo.

---

## 8. Declaración de uso de tecnologías asistidas por inteligencia artificial

Conforme a las políticas editoriales de Elsevier y de Springer Nature sobre el uso de
IA generativa en la escritura científica, se declara:

1. **Como objeto de estudio.** Un Modelo Grande de Lenguaje fue utilizado de forma
   deliberada y controlada para generar el Conjunto A de requisitos funcionales que
   constituye la intervención experimental. El modelo, la interfaz, la fecha de la
   consulta y la consigna literal están registrados en `06_Experimento/prompts_llm/`.
   La temperatura y los parámetros de muestreo **no están disponibles**: la interfaz de
   chat no los expone, y así se declara en ese registro en lugar de inventar un valor.
2. **Como asistencia en la elaboración del entregable.** Se empleó un LLM en redacción,
   en scripts de verificación y de integridad, y en tareas de organización del
   repositorio. El inventario completo, sección por sección y con el método de validación
   de cada una, está en
   [`10_Autoria/declaracion_uso_ia.md`](../../10_Autoria/declaracion_uso_ia.md). Las
   personas autoras revisaron y asumen la responsabilidad íntegra del resultado.
3. **Límite infranqueable.** Ningún resultado, cifra, tabla, figura, conclusión ni
   referencia bibliográfica fue producido por un LLM. Toda referencia se verificó
   individualmente y cada DOI se resolvió manualmente antes del envío.

Los LLM **no** figuran como personas autoras, conforme a las políticas editoriales
vigentes.
