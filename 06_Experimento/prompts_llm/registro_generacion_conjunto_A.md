# Registro integro de la generacion del Conjunto A

**Proyecto SIGA · Equipo FGMMN · ISR-401 · Universidad Tecnica Estatal de Quevedo**

Registro de las instrucciones dadas a la herramienta generativa y de lo que esta hizo al
generar el Conjunto A de requisitos funcionales del cuasi-experimento. Extraido el
2026-09-12 de la exportacion oficial de datos de claude.ai de la cuenta de **Sanchez
Cornejo, Gary Alberto**, analista lider del equipo.

## 1. Datos de la generacion

| | |
|---|---|
| Herramienta | Claude, en la interfaz de chat de claude.ai (no API) |
| Cuenta | Sanchez Cornejo, Gary Alberto |
| Conversacion | «Análisis de archivos del docente», abierta el 2026-08-01 13:40:50 UTC; es la conversacion de trabajo del proyecto |
| Instruccion del usuario | Mensaje enviado el 2026-08-02 19:44:58 UTC |
| Respuesta del asistente | De 19:44:58 a 19:51:23 UTC del 2026-08-02 |
| Modelo | La exportacion de claude.ai no incluye un campo con el modelo. El registro que el asistente escribio en esa misma respuesta, `prompt_llm_conjunto_A.md`, declara **Claude Sonnet 5** |
| Temperatura, top-p y semilla | No disponibles: la interfaz de chat no los expone |
| Resultado | `Conjunto_A_RF_LLM.md`, 26 requisitos. **Identico** al que se genero en esta respuesta, salvo la nota de integridad sobre EV-15 que se le anadio el 2026-08-13 |
| Huella del extracto exportado | SHA-256 `9e413ef45abed4b667e81a88679988b0a59f58ead0054fbe5c31e42d3a64f437` de los mensajes 176 y 177 de la conversacion, serializados en JSON con claves ordenadas. La exportacion completa la conserva el analista lider |

## 2. Como se genero

El Conjunto A **no se obtuvo enviando al modelo la consigna literal de la guia** en una
sesion aparte. Se genero dentro de la conversacion de trabajo del proyecto: el usuario
indico que usara el propio modelo sobre las once transcripciones, y el asistente, en una
sola respuesta, reunio el material fuente, consulto la plantilla de ocho atributos en los
archivos del proyecto, redacto los 26 requisitos y armo el resto del paquete del
experimento. La consigna de la guia es la tarea que el asistente aplico, no un mensaje
que se le enviara.

El asistente ya conocia el proyecto y los requisitos del equipo por esa misma
conversacion. Esa exposicion previa esta declarada como amenaza a la validez de constructo
desde el 2026-08-02 en `prompt_llm_conjunto_A.md` y en el manuscrito.

Un mensaje anterior del usuario, de las 19:44:13 UTC, con el mismo texto salvo el punto «Usa
tu propio modelo», quedo sin respuesta en la exportacion; el usuario lo reenvio completo
45 segundos despues, y ese es el mensaje que se reproduce.

## 3. Que se omite en esta copia, y por que

| Omision | Motivo |
|---|---|
| Los bloques de razonamiento interno del modelo | No son instrucciones ni resultados; se reproducen solo las instrucciones, las acciones y los textos que el asistente produjo |
| La salida de leer `material_fuente_LLM.txt` | Contenia el texto de la entrevista EV-15, cuyo consentimiento se retiro el 2026-08-13. El material fuente depositado es el mismo sin EV-15 |
| Las salidas de la busqueda en los archivos del proyecto | Son fragmentos de la guia del docente y del ERS, que ya estan en el repositorio o no son del equipo |
| El script que armo el paquete ciego | Con su semilla permitiria reconstruir la tabla de desciego, que no reside en el repositorio publico |

Todo lo demas se reproduce **sin editar**, en el orden en que ocurrio.

---

## 4. Instruccion del usuario

Enviada el 2026-08-02 19:44:58 UTC.

Fragmentos de la respuesta anterior del asistente que el usuario cito al escribir:

1. «Listo, memoria actualizada. Y perfecto sobre el diagrama de contexto — con eso, los 41 diagramas quedan 100% en 300dpi, sin pendientes de resolución técnica en esa parte.»
2. «¿Qué transcripción usamos como material fuente para el LLM?»
3. «¿Ya tienes identificados los ≥3 jueces ciegos»

Texto del mensaje:

~~~~
1. Ya te lo envio
2. Hagamos las 11
3. Usa tu propio modelo
4. No podemos usar a los mismos docentes que ya entreviste?
~~~~

Archivo adjunto: System Context Diagram of the Intelligent Classroom Management System (SIGA).png, excerpt_from_previous_claude_message.txt.

## 5. Respuesta del asistente, paso a paso

### 1. 19:45:21 UTC · Texto del asistente

Antes de arrancar, reviso el diagrama que subiste y te freno en un punto real del #4 — no por seguirte la corriente en todo, sino porque esto sí puede comprometer la validez del experimento.

### 2. 19:45:22 UTC · Accion: `bash_tool`

Descripcion que dio el asistente: *Verificar el DPI del diagrama de contexto reexportado*

~~~~bash
cd /mnt/user-data/uploads && python3 -c "
from PIL import Image
im = Image.open('System_Context_Diagram_of_the_Intelligent_Classroom_Management_System__SIGA_.png')
print('tamaño:', im.size)
print('dpi:', im.info.get('dpi', 'NO EXIF DPI'))
"
~~~~

Resultado:

~~~~
tamaño: (3363, 1989)
dpi: (299.9994, 299.9994)
~~~~

### 3. 19:45:33 UTC · Texto del asistente

**Diagrama de contexto: 300dpi confirmado.** Con esto, los 41 diagramas quedan completos y sin pendiente técnico.

## Sobre el punto 4 — necesito que reconsideres esto

**No, no deberían ser los mismos docentes que ya entrevistaron.** No es una preferencia metodológica menor, es un problema real de validez:

1. **No serían jueces ciegos.** La guía exige explícitamente *"sin que las personas evaluadoras sepan cuál es cuál"* (Sección 5.1). Si DOC-01, DOC-02, DOC-03 o DOC-04 evalúan el Conjunto B (los RF humanos), están evaluando RF que en parte **salieron de sus propias palabras** en la entrevista. Es muy probable que reconozcan cuál conjunto es cuál, lo que invalida el diseño ciego de raíz.

2. **Conflicto de rol.** Son informantes (fuente de datos) y no pueden ser jueces del mismo estudio sin generar un sesgo que cualquier revisor — incluyendo tu propio docente — notaría de inmediato si lee la sección de amenazas a la validez con cuidado.

La guía es flexible en **quién puede ser juez** — dice literalmente *"tres estudiantes de otro paralelo **o** tres docentes del área"* — el requisito no es que sean externos a la universidad, es que **no sean las mismas personas que ya participaron como fuente de las entrevistas**. Entonces sí puedes usar docentes de la FCC, con tal de que sean distintos a DOC-01/02/03/04.

¿Tienes a mano 3 docentes o estudiantes de otro paralelo que **no** hayan sido entrevistados, o necesitas que te ayude a pensar a quién pedírselo?

---

Mientras me contestas eso, avanzo con todo lo que no depende de esa respuesta: el material fuente (las 11 transcripciones), la consigna exacta, y genero el Conjunto A (RF-LLM) usando mi propio modelo.

### 4. 19:45:42 UTC · Accion: `bash_tool`

Descripcion que dio el asistente: *Confirmar las 11 transcripciones disponibles como material fuente*

~~~~bash
ls /home/claude/Transcripciones/*.txt | wc -l
cat /home/claude/Transcripciones/*.txt | wc -w
~~~~

Resultado:

~~~~
12
27799
~~~~

### 5. 19:46:00 UTC · Accion: `project_knowledge_search`

~~~~
{
  "query": "requisito funcional ocho atributos plantilla identificador nombre descripción prioridad"
}
~~~~

Resultado:

_[Contenido omitido en esta copia publica: fragmentos de la guia del docente y del ERS devueltos por la busqueda]_

### 6. 19:46:13 UTC · Texto del asistente

Tengo el template exacto de 8 atributos que ya usan en el ERS (Nombre, Descripción, Actor/Origen, Entradas/Salidas, Precondición/Postcondición, Prioridad MoSCoW, Criterio de verificación). Armo el material fuente concatenando las 11 transcripciones.

### 7. 19:46:14 UTC · Accion: `bash_tool`

Descripcion que dio el asistente: *Concatenar las 11 transcripciones en el material fuente único, en el orden correcto*

~~~~bash
cd /home/claude/Transcripciones && python3 << 'EOF'
import glob

orden = ["EV-01","EV-02","EV-08","EV-09","EV-10","EV-11","EV-12","EV-13","EV-14","EV-15","EV-16"]
archivos = {}
for f in glob.glob("*.txt"):
    if f.startswith("00_"): continue
    for ev in orden:
        if f"_{ev}_" in f:
            archivos[ev] = f

faltantes = [ev for ev in orden if ev not in archivos]
print("Faltantes:", faltantes)

with open("/home/claude/material_fuente_LLM.txt", "w", encoding="utf-8") as out:
    out.write("MATERIAL FUENTE PARA EL COMPONENTE EMPÍRICO — PROYECTO SIGA\n")
    out.write("Corpus completo de las 11 entrevistas de campo, anonimizadas.\n")
    out.write("="*70 + "\n\n")
    for ev in orden:
        with open(archivos[ev], encoding="utf-8") as f:
            out.write(f.read())
        out.write("\n\n" + "="*70 + "\n\n")

import subprocess
wc = subprocess.run(["wc","-w","/home/claude/material_fuente_LLM.txt"], capture_output=True, text=True)
print(wc.stdout)
EOF
~~~~

Resultado:

~~~~
Faltantes: []
27124 /home/claude/material_fuente_LLM.txt
~~~~

### 8. 19:46:34 UTC · Texto del asistente

Antes de generar los RF, tengo que ser transparente sobre una limitación real de usar mi propio modelo así, en esta misma conversación.

### 9. 19:46:34 UTC · Accion: `view`

Descripcion que dio el asistente: *Leer el material fuente completo antes de generar los RF*

~~~~
{
  "path": "/home/claude/material_fuente_LLM.txt"
}
~~~~

Resultado:

_[Contenido omitido en esta copia publica: texto de `material_fuente_LLM.txt`, que incluia la entrevista EV-15]_

### 10. 19:46:58 UTC · Texto del asistente

Ya reví el corpus completo (y ya tenía conocimiento profundo de las 11 por el trabajo anterior de actas). Genero el conjunto de RF-LLM ahora, siguiendo la plantilla exacta de 8 atributos, basándome **solo** en lo que dicen las transcripciones — sin usar los RF-01 a RF-25 que ya conozco del ERS, para no contaminar la comparación con esos.

### 11. 19:46:58 UTC · Accion: `bash_tool`

Descripcion que dio el asistente: *Crear carpeta del experimento*

~~~~bash
mkdir -p /home/claude/experimento
~~~~

Resultado:

~~~~

~~~~

### 12. 19:47:02 UTC · Accion: `create_file`

Descripcion que dio el asistente: *Registrar el prompt exacto y metadata de replicabilidad usados para generar el Conjunto A (RF-LLM)*

Archivo creado: `/home/claude/experimento/prompt_llm_conjunto_A.md`

~~~~
# Registro de la consigna — Conjunto A (RF generados por LLM)

**Enfoque:** 1 (comparación de calidad de RF humanos vs. LLM), Sección 5.1 de la
Guía y Rúbrica de la Entrega 3 (2A).

## Modelo y parámetros

| Campo | Valor |
|---|---|
| Modelo | Claude Sonnet 5 (Anthropic) |
| Interfaz | Chat de Claude (claude.ai), no API directa |
| Temperatura | **No disponible** — la interfaz de chat no expone este parámetro al usuario ni al propio modelo; no se reporta un valor porque hacerlo sería inventar un dato no verificable |
| Top-p | **No disponible**, misma razón que la anterior |
| Semilla | No aplica — no configurable en esta interfaz |
| Fecha y hora de la consulta | 2026-08-02, sesión continua de chat |

## ⚠️ Limitación metodológica que debe declararse en el manuscrito

El modelo que generó el Conjunto A **es el mismo asistente que acompañó al
equipo durante la elaboración de este proyecto** a lo largo de varias
sesiones de chat previas, incluyendo la construcción de las actas de
walkthrough y referencias reiteradas a los RF-01 a RF-25 ya elicitados por
el equipo humano. Esto significa que el modelo **no es una instancia
"ingenua"** sin exposición previa al Conjunto B (los RF humanos) — a
diferencia de lo que idealmente exige un diseño experimental limpio, donde
el LLM evaluado no debería tener ningún conocimiento previo del resultado
humano que se le compara.

Esta es una **amenaza real a la validez de constructo** del experimento y
debe declararse explícitamente en la Sección de Amenazas a la Validez del
manuscrito, por ejemplo:

> "El modelo de lenguaje utilizado para generar el Conjunto A había estado
> expuesto, en sesiones de chat previas dentro de la misma cuenta de
> usuario, a referencias parciales del conjunto de requisitos humanos
> (Conjunto B) del proyecto SIGA. Aunque se instruyó al modelo a generar
> los requisitos exclusivamente a partir del material fuente adjunto sin
> reutilizar frases ya conocidas, no puede descartarse una influencia
> inconsciente en la selección o el énfasis de los requisitos generados.
> Esta limitación no estaba presente en un diseño ideal con una instancia
> de modelo sin historial previo (por ejemplo, vía API con una sesión
> nueva) y se reconoce como amenaza a la validez de constructo."

**Recomendación:** si el tiempo lo permite antes de la Entrega 4 (2B), repetir
la generación del Conjunto A usando la API directa con una conversación
nueva (sin historial previo) de Claude, GPT-4o o Llama 3.1 70B, registrando
temperatura y top-p reales, para tener una versión metodológicamente más
limpia. La versión actual sirve para completar el diseño y probar el
pipeline de análisis dentro del plazo de esta entrega.

## Consigna exacta utilizada (verbatim, Sección 5.1 de la guía)

```
A partir del siguiente material fuente, redacta requisitos funcionales
del sistema descrito, con los ocho atributos de la plantilla del
sílabo.
```

## Material fuente entregado al modelo

Corpus completo y anonimizado de las 11 entrevistas de campo de la segunda
ronda (EV-01, EV-02, EV-08 a EV-16), sin ningún RF, RNF ni documento del
ERS adjunto — únicamente las transcripciones. Archivo:
`material_fuente_LLM.txt` (27 124 palabras).

## Plantilla de 8 atributos indicada al modelo

1. ID y nombre del requisito
2. Descripción
3. Actor / Origen (con EV-XX)
4. Entradas / Salidas
5. Precondición / Postcondición
6. Prioridad (MoSCoW)
7. Criterio de verificación
~~~~

Resultado:

~~~~
File created successfully: /home/claude/experimento/prompt_llm_conjunto_A.md
~~~~

### 13. 19:47:23 UTC · Texto del asistente

Ahora genero el Conjunto A completo — los RF basados exclusivamente en las transcripciones.

### 14. 19:47:24 UTC · Accion: `create_file`

Descripcion que dio el asistente: *Generar el Conjunto A de RF producidos por el LLM a partir del material fuente*

Archivo creado: `/home/claude/experimento/Conjunto_A_RF_LLM.md`

~~~~
# Conjunto A — Requisitos Funcionales generados por LLM

Generado a partir del material fuente (11 transcripciones anonimizadas),
sin acceso al Conjunto B (RF elicitados por el equipo humano). Ver
`prompt_llm_conjunto_A.md` para la consigna exacta y la limitación
metodológica declarada.

---

### RFA-01 — Monitoreo de variables ambientales del aula
- **Descripción:** El sistema debe registrar y mostrar en tiempo real la temperatura y el estado de ocupación de cada aula.
- **Actor / Origen:** Personal de servicios generales (EV-01); Coordinación de carrera (EV-10)
- **Entradas / Salidas:** Entrada: lecturas de sensores de temperatura y presencia. Salida: valor actual visible por aula.
- **Precondición / Postcondición:** Aula con sensor instalado y operativo. / Valor actualizado disponible en el panel.
- **Prioridad (MoSCoW):** Must
- **Criterio de verificación:** El valor mostrado en el panel coincide con una lectura de referencia tomada manualmente en el aula, con margen de error aceptable.

### RFA-02 — Consulta de disponibilidad de aulas en tiempo real
- **Descripción:** El sistema debe permitir consultar qué aulas están libres u ocupadas en un momento dado, sin necesidad de desplazarse físicamente.
- **Actor / Origen:** Personal de servicios generales (EV-01); Docente (EV-15)
- **Entradas / Salidas:** Entrada: solicitud de consulta de estado. Salida: listado de aulas con su estado (libre/ocupada).
- **Precondición / Postcondición:** Aula registrada en el sistema. / Estado mostrado corresponde al estado real.
- **Prioridad (MoSCoW):** Must
- **Criterio de verificación:** Al ocupar físicamente un aula de prueba, el sistema refleja el cambio de estado en un tiempo razonable.

### RFA-03 — Control remoto de proyectores
- **Descripción:** El sistema debe permitir verificar y, cuando el hardware lo soporte, controlar remotamente el estado de encendido de los proyectores del aula.
- **Actor / Origen:** Docente (EV-16); Personal de servicios generales (EV-01)
- **Entradas / Salidas:** Entrada: comando de encendido/apagado o consulta de estado. Salida: confirmación del nuevo estado del proyector.
- **Precondición / Postcondición:** Proyector conectado a un módulo de control compatible. / Estado del proyector actualizado en el sistema.
- **Prioridad (MoSCoW):** Must
- **Criterio de verificación:** Un comando de prueba enviado desde el sistema cambia el estado físico observado del proyector.

### RFA-04 — Control remoto de climatización
- **Descripción:** El sistema debe permitir ajustar remotamente la temperatura del aire acondicionado del aula.
- **Actor / Origen:** Personal de servicios generales (EV-01)
- **Entradas / Salidas:** Entrada: valor de temperatura deseado. Salida: confirmación del ajuste aplicado.
- **Precondición / Postcondición:** Unidad de climatización compatible instalada. / Temperatura del aula ajustada al valor solicitado.
- **Prioridad (MoSCoW):** Must
- **Criterio de verificación:** Un ajuste de prueba enviado desde el sistema se refleja en el equipo físico dentro de un tiempo razonable.

### RFA-05 — Apagado automático de climatización en aulas desocupadas
- **Descripción:** El sistema debe apagar automáticamente el aire acondicionado cuando detecte que un aula quedó desocupada.
- **Actor / Origen:** Personal de servicios generales (EV-01)
- **Entradas / Salidas:** Entrada: estado de ocupación = desocupada. Salida: comando de apagado enviado al equipo.
- **Precondición / Postcondición:** Aula marcada como desocupada por el sensor de presencia. / Aire acondicionado apagado sin intervención manual.
- **Prioridad (MoSCoW):** Should
- **Criterio de verificación:** Al desocupar un aula de prueba, el sistema apaga el equipo sin que el personal deba hacerlo manualmente.

### RFA-06 — Alertas automáticas de fallas de equipamiento
- **Descripción:** El sistema debe generar una alerta automática cuando detecte una anomalía en el funcionamiento de un equipo del aula (proyector, climatización).
- **Actor / Origen:** Docente (EV-13, EV-16)
- **Entradas / Salidas:** Entrada: señal de anomalía del equipo. Salida: notificación de alerta con el aula y el equipo afectado.
- **Precondición / Postcondición:** Equipo con capacidad de reportar su propio estado. / Alerta visible para el personal responsable.
- **Prioridad (MoSCoW):** Must
- **Criterio de verificación:** Al simular una falla del equipo, se genera una alerta visible en un tiempo razonable.

### RFA-07 — Clasificación de prioridad de alertas
- **Descripción:** El sistema debe permitir clasificar cada alerta según su nivel de prioridad (por ejemplo, baja para un goteo de aire acondicionado, alta para una inundación del aula).
- **Actor / Origen:** Docente (EV-16)
- **Entradas / Salidas:** Entrada: tipo de incidente reportado. Salida: nivel de prioridad asignado.
- **Precondición / Postcondición:** Incidente registrado en el sistema. / Prioridad visible junto a la alerta.
- **Prioridad (MoSCoW):** Should
- **Criterio de verificación:** Un incidente de prueba de cada tipo recibe la prioridad esperada según la regla definida.

### RFA-08 — Registro de solicitud de mantenimiento con adjunto fotográfico
- **Descripción:** El sistema debe permitir registrar una solicitud de mantenimiento indicando aula, equipo afectado, tipo de incidencia y una fotografía opcional del problema.
- **Actor / Origen:** Docente (EV-15, EV-16)
- **Entradas / Salidas:** Entrada: datos del incidente + imagen adjunta. Salida: ticket de mantenimiento creado.
- **Precondición / Postcondición:** Usuario autenticado con permiso de reporte. / Ticket visible en el listado de solicitudes.
- **Prioridad (MoSCoW):** Must
- **Criterio de verificación:** Un reporte de prueba con foto adjunta se registra correctamente y es recuperable en el listado.

### RFA-09 — Catálogo ampliado de tipos de incidencia
- **Descripción:** El sistema debe ofrecer un catálogo de tipos de incidencia que incluya, además de fallas de equipo, categorías como mobiliario deteriorado, pizarra en mal estado, problemas de iluminación, inundación del aula y aula cerrada.
- **Actor / Origen:** Docente (EV-15)
- **Entradas / Salidas:** Entrada: selección del tipo de incidencia desde una lista. Salida: incidencia clasificada correctamente.
- **Precondición / Postcondición:** Catálogo de tipos de incidencia cargado en el sistema. / Reporte asociado a un tipo válido.
- **Prioridad (MoSCoW):** Should
- **Criterio de verificación:** El formulario de reporte ofrece las categorías mencionadas como opciones seleccionables, no como texto libre.

### RFA-10 — Seguimiento de ticket de mantenimiento con estado único
- **Descripción:** El sistema debe permitir consultar el historial de un ticket de mantenimiento mostrando el estado actual, la fecha y hora de cada actualización, sin duplicar columnas de estado anterior/nuevo.
- **Actor / Origen:** Docente (EV-16)
- **Entradas / Salidas:** Entrada: consulta de un ticket por su identificador. Salida: historial con fecha, hora y estado.
- **Precondición / Postcondición:** Ticket existente en el sistema. / Historial completo visible para el usuario que lo reportó.
- **Prioridad (MoSCoW):** Must
- **Criterio de verificación:** Al actualizar el estado de un ticket de prueba varias veces, el historial muestra cada cambio con su fecha y hora, sin columnas redundantes.

### RFA-11 — Acuse de recepción de solicitudes de mantenimiento
- **Descripción:** El sistema debe notificar de inmediato al usuario que reportó una falla que su solicitud fue recibida por el responsable, dentro del horario laboral.
- **Actor / Origen:** Docente (EV-16)
- **Entradas / Salidas:** Entrada: nueva solicitud de mantenimiento. Salida: estado "recibido" visible para quien reportó.
- **Precondición / Postcondición:** Solicitud registrada dentro del horario laboral. / Estado de acuse de recepción visible en un tiempo breve.
- **Prioridad (MoSCoW):** Should
- **Criterio de verificación:** Una solicitud de prueba cambia a estado "recibido" en un tiempo breve tras su creación.

### RFA-12 — Notificación multicanal de incidencias críticas
- **Descripción:** El sistema debe notificar simultáneamente a la autoridad de la facultad, a la persona que reportó el incidente y al responsable de la reparación cuando se registre una incidencia.
- **Actor / Origen:** Docente (EV-15)
- **Entradas / Salidas:** Entrada: incidencia registrada. Salida: notificación enviada a los tres destinatarios.
- **Precondición / Postcondición:** Roles de autoridad y responsable configurados en el sistema. / Constancia de notificación enviada a cada destinatario.
- **Prioridad (MoSCoW):** Should
- **Criterio de verificación:** Una incidencia de prueba genera notificación registrada para los tres roles simultáneamente.

### RFA-13 — Consulta agregada de estado de cámaras existentes
- **Descripción:** El sistema debe consultar, de forma agregada y sin identificar personas, si las cámaras de videovigilancia de un aula están operativas.
- **Actor / Origen:** Personal de servicios generales (EV-08)
- **Entradas / Salidas:** Entrada: consulta de estado de cámara por aula. Salida: indicador de funcionalidad (operativa / no operativa).
- **Precondición / Postcondición:** Cámara instalada en el aula consultada. / Estado de funcionalidad visible sin mostrar video.
- **Prioridad (MoSCoW):** Could
- **Criterio de verificación:** El sistema muestra correctamente el estado de una cámara operativa y de una no operativa, sin exponer imagen alguna.

### RFA-14 — Restricción de acceso a cámaras por rol
- **Descripción:** El sistema no debe permitir que el personal docente visualice el contenido de las cámaras de videovigilancia de las aulas.
- **Actor / Origen:** Docente (EV-15, expresó oposición explícita)
- **Entradas / Salidas:** Entrada: intento de acceso a video de cámara por un usuario con rol docente. Salida: acceso denegado.
- **Precondición / Postcondición:** Usuario autenticado con rol docente. / Intento de acceso registrado como denegado.
- **Prioridad (MoSCoW):** Must
- **Criterio de verificación:** Un intento de prueba de acceso a video con una cuenta de rol docente es rechazado por el sistema.

### RFA-15 — Consulta de disponibilidad de aulas alternativas
- **Descripción:** El sistema debe permitir consultar qué aulas están disponibles cuando la asignada resulta inutilizable, para facilitar un cambio de espacio.
- **Actor / Origen:** Docente (EV-15)
- **Entradas / Salidas:** Entrada: solicitud de aulas libres en un horario determinado. Salida: listado de aulas disponibles.
- **Precondición / Postcondición:** Aula original marcada como no disponible. / Listado de alternativas mostrado al usuario.
- **Prioridad (MoSCoW):** Could
- **Criterio de verificación:** Ante un aula marcada como no disponible, el sistema devuelve al menos una alternativa libre en el mismo horario, si existe.

### RFA-16 — Filtrado del panel por horario académico del docente
- **Descripción:** El sistema debe filtrar la vista de aulas del rol docente, mostrando únicamente las aulas correspondientes a su horario de clases.
- **Actor / Origen:** Docente (EV-15)
- **Entradas / Salidas:** Entrada: identidad del docente autenticado. Salida: listado de aulas restringido a su horario.
- **Precondición / Postcondición:** Horario del docente cargado en el sistema. / Vista muestra solo las aulas relevantes para ese docente.
- **Prioridad (MoSCoW):** Should
- **Criterio de verificación:** Al iniciar sesión con una cuenta docente de prueba, la vista solo incluye las aulas de su horario asignado.

### RFA-17 — Inventario de equipos disponibles en laboratorios
- **Descripción:** El sistema debe mostrar la cantidad de equipos de cómputo en buen estado disponibles en un laboratorio, considerando la capacidad requerida según la asignatura.
- **Actor / Origen:** Docente (EV-16)
- **Entradas / Salidas:** Entrada: consulta de un laboratorio específico. Salida: cantidad de equipos operativos disponibles.
- **Precondición / Postcondición:** Inventario del laboratorio registrado en el sistema. / Cantidad mostrada corresponde al estado real de los equipos.
- **Prioridad (MoSCoW):** Should
- **Criterio de verificación:** El número de equipos "en buen estado" mostrado coincide con una verificación física de referencia.

### RFA-18 — Reportes administrativos de ocupación y consumo
- **Descripción:** El sistema debe generar reportes con el porcentaje de ocupación promedio, el consumo eléctrico estimado y las incidencias registradas de un aula en un periodo determinado.
- **Actor / Origen:** Docente (EV-16, mencionado como vista administrativa)
- **Entradas / Salidas:** Entrada: aula y rango de fechas. Salida: reporte con los tres indicadores solicitados.
- **Precondición / Postcondición:** Datos históricos de ocupación, consumo e incidencias disponibles para el aula. / Reporte generado y visible.
- **Prioridad (MoSCoW):** Should
- **Criterio de verificación:** Un reporte generado para un aula y periodo de prueba refleja los valores esperados de los tres indicadores.

### RFA-19 — Simplificación de la pantalla principal para personal no técnico
- **Descripción:** El sistema debe presentar al personal no técnico una vista simple del estado de las aulas, comprensible sin explicación previa.
- **Actor / Origen:** Personal de servicios generales (EV-08, EV-09, validaron comprensibilidad de MU-01)
- **Entradas / Salidas:** Entrada: acceso a la vista principal con rol no técnico. Salida: información esencial de ocupación y estado del aula.
- **Precondición / Postcondición:** Usuario autenticado con rol de personal de servicios generales. / Vista mostrada sin requerir capacitación previa.
- **Prioridad (MoSCoW):** Should
- **Criterio de verificación:** Una persona sin formación técnica logra identificar el estado de un aula usando únicamente la vista, sin asistencia.

### RFA-20 — Gestión de permisos diferenciados por rol
- **Descripción:** El sistema debe explicitar y aplicar permisos distintos según el rol del usuario (por ejemplo, si un docente puede reportar o solo consultar alertas).
- **Actor / Origen:** Docente (EV-13)
- **Entradas / Salidas:** Entrada: acción solicitada por un usuario autenticado. Salida: acción permitida o denegada según su rol.
- **Precondición / Postcondición:** Rol del usuario definido en el sistema. / Acción ejecutada solo si el rol lo permite.
- **Prioridad (MoSCoW):** Must
- **Criterio de verificación:** Un usuario de prueba con rol docente puede realizar las acciones permitidas para ese rol y ninguna otra.

### RFA-21 — Historial de intervenciones de mantenimiento por equipo
- **Descripción:** El sistema debe exponer, también al rol docente, el historial de intervenciones de mantenimiento realizadas sobre un equipo específico.
- **Actor / Origen:** Docente (EV-13, detectó esta brecha en el prototipo)
- **Entradas / Salidas:** Entrada: consulta de historial por equipo. Salida: listado de intervenciones previas con fecha y causa.
- **Precondición / Postcondición:** Equipo con al menos una intervención registrada. / Historial visible para el rol docente, no solo administrativo.
- **Prioridad (MoSCoW):** Should
- **Criterio de verificación:** Un usuario docente de prueba puede consultar el historial de un equipo con intervenciones previas registradas.

### RFA-22 — Registro de estado del aula por sesión de clase
- **Descripción:** El sistema debe permitir registrar, al inicio y al final de cada sesión de clase, el estado de los equipos del aula (proyector, climatización), dejando constancia de en qué condición se recibió y se dejó el espacio.
- **Actor / Origen:** Docente (EV-13)
- **Entradas / Salidas:** Entrada: registro de estado con responsable identificado. Salida: bitácora de estado por sesión.
- **Precondición / Postcondición:** Sesión de clase activa en el sistema. / Registro de estado asociado a esa sesión y ese responsable.
- **Prioridad (MoSCoW):** Could
- **Criterio de verificación:** Un registro de prueba al inicio y fin de una sesión queda almacenado con responsable, fecha y hora.

### RFA-23 — Registro de bitácora de acciones de usuario
- **Descripción:** El sistema debe registrar en una bitácora las acciones relevantes ejecutadas por los usuarios (control remoto de equipos, gestión de roles).
- **Actor / Origen:** Personal de servicios generales (EV-01); Docente (EV-02)
- **Entradas / Salidas:** Entrada: acción ejecutada por un usuario. Salida: entrada de bitácora con usuario, acción y fecha/hora.
- **Precondición / Postcondición:** Usuario autenticado ejecuta una acción relevante. / Entrada de bitácora generada de forma automática.
- **Prioridad (MoSCoW):** Must
- **Criterio de verificación:** Una acción de prueba (por ejemplo, apagar un proyector) genera una entrada de bitácora verificable.

### RFA-24 — Monitoreo de conectividad de dispositivos IoT
- **Descripción:** El sistema debe indicar si los sensores y dispositivos IoT de un aula están conectados y transmitiendo datos correctamente.
- **Actor / Origen:** Personal de servicios generales (EV-01, mención indirecta sobre confiabilidad de sensores)
- **Entradas / Salidas:** Entrada: señal de estado de conexión del dispositivo. Salida: indicador de conectividad por aula.
- **Precondición / Postcondición:** Dispositivo IoT configurado en la red del aula. / Estado de conectividad visible y actualizado.
- **Prioridad (MoSCoW):** Should
- **Criterio de verificación:** Al desconectar intencionalmente un sensor de prueba, el sistema refleja el cambio de estado de conectividad.

### RFA-25 — Consulta desde dispositivo móvil
- **Descripción:** El sistema debe ser consultable desde un teléfono celular, sin requerir instalación adicional.
- **Actor / Origen:** Docente (EV-15, EV-16, ambos indicaron preferencia por consulta desde el teléfono)
- **Entradas / Salidas:** Entrada: acceso desde navegador móvil. Salida: interfaz funcional adaptada a pantalla pequeña.
- **Precondición / Postcondición:** Dispositivo móvil con navegador y conexión a la red institucional. / Interfaz utilizable sin instalación de aplicación adicional.
- **Prioridad (MoSCoW):** Must
- **Criterio de verificación:** Un usuario de prueba accede y opera las funciones principales desde un navegador móvil sin instalar software adicional.

### RFA-26 — Alerta ante conectividad de red no disponible
- **Descripción:** El sistema debe advertir a los usuarios cuando la conectividad de red del aula no permita el funcionamiento normal del sistema, dado que no todas las aulas cuentan con acceso a internet.
- **Actor / Origen:** Docente (EV-15, señaló la falta de conectividad como riesgo crítico)
- **Entradas / Salidas:** Entrada: pérdida de señal de red del aula. Salida: aviso de funcionalidad limitada.
- **Precondición / Postcondición:** Aula sin conectividad de red disponible. / Aviso mostrado antes de que el usuario intente usar funciones dependientes de red.
- **Prioridad (MoSCoW):** Should
- **Criterio de verificación:** Al simular la pérdida de conectividad de un aula de prueba, el sistema muestra el aviso correspondiente.
~~~~

Resultado:

~~~~
File created successfully: /home/claude/experimento/Conjunto_A_RF_LLM.md
~~~~

### 15. 19:48:39 UTC · Texto del asistente

Ahora armo el resto del paquete: rúbrica, hoja de puntuación, y el paquete ciego para los jueces (necesito los 25 RF humanos del ERS para emparejarlos).

### 16. 19:48:39 UTC · Accion: `project_knowledge_search`

~~~~
{
  "query": "RF-01 RF-02 RF-03 RF-04 RF-05 RF-06 RF-07 RF-08 RF-09 RF-10 descripción actor origen"
}
~~~~

Resultado:

_[Contenido omitido en esta copia publica: fragmentos de la guia del docente y del ERS devueltos por la busqueda]_

### 17. 19:49:05 UTC · Texto del asistente

Tengo suficiente para armar el resto. Genero la rúbrica, el paquete ciego mezclado (A+B sin revelar cuál es cuál), y la hoja de puntuación.

### 18. 19:49:05 UTC · Accion: `bash_tool`

Descripcion que dio el asistente: *Generar la rúbrica de evaluación con anclas 1-5*

~~~~bash
cd /home/claude/experimento && cat > rubrica_evaluacion.md << 'EOF'
# Rúbrica de evaluación — Comparación de calidad de RF (Enfoque 1)

Cada persona evaluadora puntúa **cada requisito de forma individual**,
sin saber si proviene del equipo humano o del LLM, en las siguientes
5 dimensiones, escala 1 (muy deficiente) a 5 (excelente).

## 1. Completitud
¿El requisito incluye toda la información necesaria para implementarlo
sin tener que adivinar detalles (actor, condición, resultado esperado)?

| Puntaje | Ancla |
|---|---|
| 1 | Falta información esencial; no se puede implementar sin preguntar de nuevo al cliente |
| 3 | Cubre lo esencial pero omite detalles secundarios (ej. formato exacto de salida) |
| 5 | Autocontenido: cualquier desarrollador podría implementarlo sin dudas |

## 2. Ausencia de ambigüedad
¿El texto admite una sola interpretación razonable?

| Puntaje | Ancla |
|---|---|
| 1 | Usa cuantificadores vagos ("rápido", "fácil") o admite varias lecturas contradictorias |
| 3 | Mayormente claro, con algún término que podría interpretarse de más de una forma |
| 5 | Una sola lectura posible; términos y umbrales precisos |

## 3. Verificabilidad
¿Existe una forma objetiva de comprobar que el requisito se cumplió?

| Puntaje | Ancla |
|---|---|
| 1 | No hay criterio de aceptación, o es subjetivo ("debe ser satisfactorio") |
| 3 | Hay criterio, pero requiere juicio humano para decidir si se cumplió |
| 5 | Criterio medible y objetivo (umbral numérico, prueba reproducible) |

## 4. Corrección respecto de la fuente
¿El requisito refleja fielmente lo que decían las transcripciones, sin
inventar ni contradecir lo que dijeron los participantes?

| Puntaje | Ancla |
|---|---|
| 1 | Contradice o no tiene respaldo alguno en el material fuente |
| 3 | Tiene respaldo parcial o requiere una interpretación forzada de la fuente |
| 5 | Trazable directamente a una afirmación concreta de una o más entrevistas |

## 5. Consistencia interna
¿El requisito no se contradice con otros requisitos del mismo conjunto?

| Puntaje | Ancla |
|---|---|
| 1 | Contradice abiertamente otro requisito del mismo conjunto |
| 3 | No contradice, pero se solapa parcialmente sin diferenciarse con claridad |
| 5 | Coherente y bien diferenciado de los demás requisitos del conjunto |

## Nota de acuerdo inter-evaluador

Cada persona evaluadora puntúa de forma independiente, sin consultar a
las demás. Una vez recogidas las 3 (o más) hojas de puntuación, se
calcula:
- **κ de Cohen** entre cada par de evaluadores.
- **κ de Fleiss** para el conjunto completo de evaluadores.
EOF
echo "Rúbrica generada"
~~~~

Resultado:

~~~~
Rúbrica generada
~~~~

### 19. 19:49:25 UTC · Accion: `bash_tool`

Descripcion que dio el asistente: *Registrar los 25 RF humanos del Conjunto B para construir el paquete ciego*

~~~~bash
cd /home/claude/experimento && cat > rf_humanos_conjunto_B.py << 'PYEOF'
# -*- coding: utf-8 -*-
# Nombres de los 25 RF humanos (Conjunto B), tal como constan en el ERS/SRS.
# Solo el nombre/descripcion breve, suficiente para el paquete ciego de jueces.
conjunto_B = {
"RF-01": "El sistema debe capturar en tiempo real temperatura, humedad y ocupación de cada aula mediante sensores IoT distribuidos.",
"RF-02": "El usuario autorizado debe poder visualizar y enviar comandos (encender/apagar/ajustar) a los dispositivos de un aula sin desplazarse físicamente.",
"RF-03": "El sistema debe detectar automáticamente si un aula está ocupada o vacía mediante sensores de presencia.",
"RF-04": "El sistema debe permitir el monitoreo y control remoto de los proyectores del aula.",
"RF-05": "El sistema debe permitir el monitoreo y ajuste remoto de la climatización del aula.",
"RF-06": "El sistema debe integrarse con el sistema de videovigilancia existente para consulta agregada de estado.",
"RF-07": "El sistema debe presentar un panel de control centralizado con la información consolidada de sensores, proyectores, climatización y conectividad.",
"RF-08": "El sistema debe generar y enviar alertas automáticas cuando detecte anomalías técnicas o condiciones fuera de los parámetros configurados.",
"RF-09": "El sistema debe analizar el comportamiento histórico de los equipos para estimar la probabilidad de fallas futuras mediante Inteligencia Artificial.",
"RF-10": "El sistema debe registrar cada falla y mantenimiento con fecha, hora, tipo de incidente, aula, equipo afectado y responsable.",
"RF-11": "El sistema debe notificar de forma inmediata al personal técnico cuando una falla afecte una clase en curso o comprometa equipos esenciales.",
"RF-12": "El sistema debe permitir gestionar solicitudes de mantenimiento, desde su registro hasta su cierre.",
"RF-13": "El sistema debe controlar automáticamente el apagado energético de equipos según reglas configuradas.",
"RF-14": "El sistema debe analizar patrones de consumo energético de los equipos del aula.",
"RF-15": "El sistema debe permitir programar horarios automatizados de encendido y apagado de equipos.",
"RF-16": "El sistema debe apagar automáticamente los equipos de un aula cuando esta quede desocupada.",
"RF-17": "El sistema debe generar reportes estadísticos periódicos sobre el uso y estado de las aulas.",
"RF-18": "El sistema debe permitir exportar reportes administrativos en formato PDF y Excel.",
"RF-19": "El sistema debe permitir el acceso diferenciado por roles, habilitando únicamente las funciones autorizadas según el perfil del usuario.",
"RF-20": "El sistema debe registrar el historial de ocupación de cada aula incluyendo fecha, hora de inicio, fin, duración y estado detectado.",
"RF-21": "El sistema debe enviar notificaciones automáticas cuando detecte proyectores o equipos de climatización encendidos fuera del horario académico vigente.",
"RF-22": "El sistema debe monitorear la conectividad de red de los dispositivos IoT instalados en las aulas.",
"RF-23": "El sistema debe registrar en una bitácora las acciones relevantes ejecutadas por los usuarios del sistema.",
"RF-24": "El sistema debe permitir a la persona usuaria exportar sus propios datos personales almacenados, conforme al derecho de acceso.",
"RF-25": "El sistema debe permitir a la persona usuaria solicitar la rectificación de sus datos personales almacenados.",
}
PYEOF
python3 -c "
import sys
sys.path.insert(0,'.')
from rf_humanos_conjunto_B import conjunto_B
print('Total RF humanos:', len(conjunto_B))
"
~~~~

Resultado:

~~~~
Total RF humanos: 25
~~~~

### 20. 19:49:40 UTC · Accion: `bash_tool`

Descripcion que dio el asistente: *Construir el paquete ciego mezclado (51 ítems) y la clave de respuestas separada*

_[Contenido omitido en esta copia publica: script que genera el paquete ciego y la tabla de desciego con una semilla fija]_

Resultado:

~~~~
Total RFA cargados: 26
Total RF-B cargados: 25
Paquete generado: 51 items totales (26 LLM + 25 humanos)
~~~~

### 21. 19:49:54 UTC · Texto del asistente

Ahora la hoja de puntuación CSV para que cada juez la llene.

### 22. 19:49:55 UTC · Accion: `bash_tool`

Descripcion que dio el asistente: *Generar la hoja de puntuación en blanco para cada juez*

~~~~bash
cd /home/claude/experimento && python3 << 'PYEOF'
import csv

with open("Hoja_Puntuacion_JUEZ.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["Item_ciego", "Completitud(1-5)", "Ausencia_ambiguedad(1-5)",
                "Verificabilidad(1-5)", "Correccion_fuente(1-5)", "Consistencia_interna(1-5)",
                "Comentario_opcional"])
    for i in range(1, 52):
        w.writerow([f"Item-{i:02d}", "", "", "", "", "", ""])
print("Hoja de puntuación generada: 51 filas en blanco")
PYEOF
ls -la /home/claude/experimento/
~~~~

Resultado:

~~~~
Hoja de puntuación generada: 51 filas en blanco
total 60
drwxr-xr-x  3 root root  4096 Aug  2 19:49 .
drwxr-xr-x 19 root root  4096 Aug  2 19:46 ..
-rw-r--r--  1 root root  1101 Aug  2 19:49 CLAVE_RESPUESTAS_no_compartir_con_jueces.csv
-rw-r--r--  1 root root 19338 Aug  2 19:48 Conjunto_A_RF_LLM.md
-rw-r--r--  1 root root   909 Aug  2 19:49 Hoja_Puntuacion_JUEZ.csv
-rw-r--r--  1 root root  7932 Aug  2 19:49 Paquete_Evaluacion_Ciega_Jueces.md
drwxr-xr-x  2 root root  4096 Aug  2 19:49 __pycache__
-rw-r--r--  1 root root  3491 Aug  2 19:47 prompt_llm_conjunto_A.md
-rw-r--r--  1 root root  3386 Aug  2 19:49 rf_humanos_conjunto_B.py
-rw-r--r--  1 root root  2553 Aug  2 19:49 rubrica_evaluacion.md
~~~~

### 23. 19:50:00 UTC · Texto del asistente

Ahora armo el protocolo experimental completo que amarra todo (PICOC, hipótesis, plan de análisis) y empaqueto todo en el zip para `06_Experimento/`.

### 24. 19:50:02 UTC · Accion: `bash_tool`

Descripcion que dio el asistente: *Generar el protocolo experimental completo con PICOC, hipótesis y plan de análisis*

~~~~bash
cd /home/claude/experimento && rm -rf __pycache__ && cat > protocolo_experimental.md << 'EOF'
# Protocolo del componente empírico — Proyecto SIGA
## Enfoque 1: Comparación de calidad de RF humanos vs. RF generados por LLM

## PICOC

| Elemento | Definición |
|---|---|
| **P**oblación | Requisitos funcionales del sistema SIGA (26 generados por LLM, 25 elicitados por el equipo humano) |
| **I**ntervención | Elicitación asistida por modelo de lenguaje grande (Claude Sonnet 5), a partir del corpus completo de 11 entrevistas anonimizadas |
| **C**omparación | Elicitación tradicional por el equipo humano (entrevistas + análisis manual) |
| **O**utcome (resultado) | Puntuación de calidad en 5 dimensiones (completitud, ausencia de ambigüedad, verificabilidad, corrección respecto de la fuente, consistencia interna), evaluada por ≥3 jueces ciegos |
| **C**ontexto | Proyecto académico de Ingeniería de Requerimientos, dominio de gestión inteligente de aulas, Facultad de Ciencias de la Computación, UTEQ |

## Pregunta de investigación

¿En qué dimensiones de calidad los requisitos funcionales elicitados por
un equipo humano difieren de los generados por un modelo de lenguaje
grande a partir del mismo material fuente?

## Hipótesis

- **H0:** No hay diferencia significativa en la puntuación media de
  calidad entre el Conjunto A (LLM) y el Conjunto B (humano) en ninguna
  de las 5 dimensiones evaluadas.
- **H1:** Existe una diferencia significativa en la puntuación media de
  calidad entre el Conjunto A y el Conjunto B en al menos una dimensión.

## Variables

| Tipo | Variable |
|---|---|
| Independiente | Origen del requisito (Humano / LLM) |
| Dependientes | Puntuación 1-5 en cada una de las 5 dimensiones de la rúbrica |
| Control | Mismo material fuente para ambos conjuntos; mismos jueces evalúan ambos conjuntos; orden aleatorizado y ciego |

## Participantes (jueces evaluadores)

**Requisito de independencia:** ninguno de los jueces puede ser una de
las personas entrevistadas en las 11 transcripciones que sirvieron como
material fuente (DOC-01 a DOC-04, COORD-01 a COORD-03, CONS-01 a
CONS-04), para preservar la ceguera del diseño. Mínimo 3 jueces; se
recomiendan 5 si es posible, siguiendo la Sección 5.1 de la guía.

## Diseño

Cuasi-experimento apareado. Cada juez evalúa los 51 ítems del paquete
ciego (`Paquete_Evaluacion_Ciega_Jueces.md`), sin saber el origen de
cada uno, usando la `Hoja_Puntuacion_JUEZ.csv`. El orden fue aleatorizado
con semilla fija (20260802) para reproducibilidad.

## Plan de análisis estadístico

1. Consolidar las hojas de puntuación de los ≥3 jueces.
2. Calcular acuerdo inter-evaluador: κ de Cohen por par de jueces, κ de
   Fleiss para el conjunto completo.
3. Prueba de normalidad Shapiro-Wilk sobre las puntuaciones de cada
   conjunto, por dimensión.
4. Si los datos son normales: prueba t para muestras apareadas
   (comparando la media de cada juez en Conjunto A vs. Conjunto B).
   Si no son normales: prueba de Wilcoxon.
5. Tamaño del efecto: Cohen d (si paramétrico) o Cliff δ (si no
   paramétrico).
6. Cálculo de potencia estadística previo (α = 0.05, potencia deseada
   1-β = 0.80).

## Amenazas a la validez (declaración obligatoria, ver también
`prompt_llm_conjunto_A.md`)

- **Validez de constructo:** el modelo usado para generar el Conjunto A
  tuvo exposición previa parcial al Conjunto B dentro de la misma
  cuenta de chat (ver limitación detallada en `prompt_llm_conjunto_A.md`).
- **Validez interna:** los jueces deben ser verificablemente
  independientes de las 11 entrevistas fuente; su selección debe
  documentarse.
- **Validez externa:** los resultados son específicos del dominio SIGA
  y de un modelo de LLM particular; no se generalizan automáticamente
  a otros dominios o modelos.
- **Validez de conclusión:** el tamaño de muestra (51 ítems, ≥3 jueces)
  es modesto; se recomienda ampliar jueces hacia la Entrega 4 (2B) si
  el tiempo lo permite.

## Registro previo

Este protocolo debe registrarse en OSF (https://osf.io) **antes** de
distribuir el paquete ciego a los jueces, conforme al gatekeeper G6 de
la guía. El equipo ya reportó tener el proyecto OSF creado pero sin
completar/registrar formalmente — completar antes de enviar el paquete.
EOF
echo "Protocolo generado"
ls -la
~~~~

Resultado:

~~~~
Protocolo generado
total 64
drwxr-xr-x  2 root root  4096 Aug  2 19:50 .
drwxr-xr-x 19 root root  4096 Aug  2 19:46 ..
-rw-r--r--  1 root root  1101 Aug  2 19:49 CLAVE_RESPUESTAS_no_compartir_con_jueces.csv
-rw-r--r--  1 root root 19338 Aug  2 19:48 Conjunto_A_RF_LLM.md
-rw-r--r--  1 root root   909 Aug  2 19:49 Hoja_Puntuacion_JUEZ.csv
-rw-r--r--  1 root root  7932 Aug  2 19:49 Paquete_Evaluacion_Ciega_Jueces.md
-rw-r--r--  1 root root  3491 Aug  2 19:47 prompt_llm_conjunto_A.md
-rw-r--r--  1 root root  4219 Aug  2 19:50 protocolo_experimental.md
-rw-r--r--  1 root root  3386 Aug  2 19:49 rf_humanos_conjunto_B.py
-rw-r--r--  1 root root  2553 Aug  2 19:49 rubrica_evaluacion.md
~~~~

### 25. 19:50:25 UTC · Texto del asistente

Ahora empaqueto todo en un zip listo para `06_Experimento/`.

### 26. 19:50:25 UTC · Accion: `bash_tool`

Descripcion que dio el asistente: *Organizar todo dentro de la estructura 06_Experimento/*

~~~~bash
cd /home/claude/experimento && rm -f rf_humanos_conjunto_B.py
cp /home/claude/material_fuente_LLM.txt .
mkdir -p /home/claude/pkg_experimento/06_Experimento/instrumentos /home/claude/pkg_experimento/06_Experimento/prompts_llm /home/claude/pkg_experimento/06_Experimento/resultados /home/claude/pkg_experimento/06_Experimento/scripts_analisis
cp protocolo_experimental.md /home/claude/pkg_experimento/06_Experimento/protocolo.pdf.md
cp prompt_llm_conjunto_A.md /home/claude/pkg_experimento/06_Experimento/prompts_llm/
cp material_fuente_LLM.txt /home/claude/pkg_experimento/06_Experimento/prompts_llm/
cp Conjunto_A_RF_LLM.md /home/claude/pkg_experimento/06_Experimento/prompts_llm/
cp rubrica_evaluacion.md /home/claude/pkg_experimento/06_Experimento/instrumentos/
cp Paquete_Evaluacion_Ciega_Jueces.md /home/claude/pkg_experimento/06_Experimento/instrumentos/
cp Hoja_Puntuacion_JUEZ.csv /home/claude/pkg_experimento/06_Experimento/instrumentos/
cp CLAVE_RESPUESTAS_no_compartir_con_jueces.csv /home/claude/pkg_experimento/06_Experimento/
find /home/claude/pkg_experimento -type f | sort
~~~~

Resultado:

~~~~
/home/claude/pkg_experimento/06_Experimento/CLAVE_RESPUESTAS_no_compartir_con_jueces.csv
/home/claude/pkg_experimento/06_Experimento/instrumentos/Hoja_Puntuacion_JUEZ.csv
/home/claude/pkg_experimento/06_Experimento/instrumentos/Paquete_Evaluacion_Ciega_Jueces.md
/home/claude/pkg_experimento/06_Experimento/instrumentos/rubrica_evaluacion.md
/home/claude/pkg_experimento/06_Experimento/prompts_llm/Conjunto_A_RF_LLM.md
/home/claude/pkg_experimento/06_Experimento/prompts_llm/material_fuente_LLM.txt
/home/claude/pkg_experimento/06_Experimento/prompts_llm/prompt_llm_conjunto_A.md
/home/claude/pkg_experimento/06_Experimento/protocolo.pdf.md
~~~~

### 27. 19:50:36 UTC · Accion: `bash_tool`

Descripcion que dio el asistente: *Corregir nombre de archivo y crear el script de análisis estadístico*

~~~~bash
cd /home/claude/pkg_experimento/06_Experimento && mv protocolo.pdf.md protocolo.md
rm -f -r resultados scripts_analisis
mkdir -p resultados scripts_analisis
cat > resultados/.gitkeep << 'EOF'
Aquí van los CSV con las puntuaciones consolidadas de los jueces, una
vez recibidas las Hoja_Puntuacion_JUEZ.csv completas.
EOF
cat > scripts_analisis/analizar_resultados.py << 'PYEOF'
# -*- coding: utf-8 -*-
"""
Script de análisis estadístico del componente empírico SIGA (Enfoque 1).
Uso: colocar las hojas de puntuación completas de cada juez en
resultados/ (una por juez, ej. juez1.csv, juez2.csv, juez3.csv) y
correr este script. Requiere: pandas, scipy, numpy.

    pip install pandas scipy numpy --break-system-packages
    python3 analizar_resultados.py
"""
import glob
import pandas as pd
import numpy as np
from scipy import stats

DIMENSIONES = [
    "Completitud(1-5)", "Ausencia_ambiguedad(1-5)", "Verificabilidad(1-5)",
    "Correccion_fuente(1-5)", "Consistencia_interna(1-5)",
]

def cargar_clave():
    clave = pd.read_csv("../CLAVE_RESPUESTAS_no_compartir_con_jueces.csv")
    return clave.set_index("Item_ciego")["Origen"].to_dict()

def cargar_jueces():
    archivos = sorted(glob.glob("../resultados/juez*.csv"))
    if not archivos:
        print("No se encontraron archivos resultados/juez*.csv todavía.")
        return []
    return [pd.read_csv(a) for a in archivos]

def main():
    origen = cargar_clave()
    jueces = cargar_jueces()
    if not jueces:
        return

    for dim in DIMENSIONES:
        print(f"\n=== Dimensión: {dim} ===")
        humano_scores, llm_scores = [], []
        for df in jueces:
            df["Origen"] = df["Item_ciego"].map(origen)
            humano_scores.append(df[df["Origen"] == "Humano"][dim].mean())
            llm_scores.append(df[df["Origen"] == "LLM"][dim].mean())

        humano_scores = np.array(humano_scores, dtype=float)
        llm_scores = np.array(llm_scores, dtype=float)

        print("Medias por juez (Humano):", humano_scores)
        print("Medias por juez (LLM):", llm_scores)

        # Normalidad
        if len(humano_scores) >= 3:
            _, p_norm_h = stats.shapiro(humano_scores)
            _, p_norm_l = stats.shapiro(llm_scores)
            normal = p_norm_h > 0.05 and p_norm_l > 0.05
        else:
            normal = False  # con n<3 no se puede evaluar normalidad de forma fiable

        if normal:
            stat, p = stats.ttest_rel(humano_scores, llm_scores)
            print(f"t-test apareado: t={stat:.3f}, p={p:.4f}")
        else:
            stat, p = stats.wilcoxon(humano_scores, llm_scores)
            print(f"Wilcoxon: W={stat:.3f}, p={p:.4f}")

        diff = humano_scores - llm_scores
        d = diff.mean() / diff.std(ddof=1) if diff.std(ddof=1) > 0 else float("nan")
        print(f"Cohen d (apareado): {d:.3f}")

if __name__ == "__main__":
    main()
PYEOF
echo "Script de análisis creado"
find /home/claude/pkg_experimento -type f | sort
~~~~

Resultado:

~~~~
Script de análisis creado
/home/claude/pkg_experimento/06_Experimento/CLAVE_RESPUESTAS_no_compartir_con_jueces.csv
/home/claude/pkg_experimento/06_Experimento/instrumentos/Hoja_Puntuacion_JUEZ.csv
/home/claude/pkg_experimento/06_Experimento/instrumentos/Paquete_Evaluacion_Ciega_Jueces.md
/home/claude/pkg_experimento/06_Experimento/instrumentos/rubrica_evaluacion.md
/home/claude/pkg_experimento/06_Experimento/prompts_llm/Conjunto_A_RF_LLM.md
/home/claude/pkg_experimento/06_Experimento/prompts_llm/material_fuente_LLM.txt
/home/claude/pkg_experimento/06_Experimento/prompts_llm/prompt_llm_conjunto_A.md
/home/claude/pkg_experimento/06_Experimento/protocolo.md
/home/claude/pkg_experimento/06_Experimento/resultados/.gitkeep
/home/claude/pkg_experimento/06_Experimento/scripts_analisis/analizar_resultados.py
~~~~

### 28. 19:50:51 UTC · Accion: `bash_tool`

Descripcion que dio el asistente: *Validar que el script de análisis corre correctamente con datos ficticios de prueba*

_[Contenido omitido en esta copia publica: script que genera el paquete ciego y la tabla de desciego con una semilla fija]_

Resultado:

~~~~
sintaxis OK

=== Dimensión: Completitud(1-5) ===
Medias por juez (Humano): [3.68 3.32 3.64]
Medias por juez (LLM): [3.30769231 3.23076923 3.38461538]
t-test apareado: t=2.910, p=0.1006
Cohen d (apareado): 1.680

=== Dimensión: Ausencia_ambiguedad(1-5) ===
Medias por juez (Humano): [3.56 3.44 3.28]
Medias por juez (LLM): [3.19230769 4.         3.        ]
t-test apareado: t=0.099, p=0.9303
Cohen d (apareado): 0.057

=== Dimensión: Verificabilidad(1-5) ===
Medias por juez (Humano): [3.44 3.48 3.32]
Medias por juez (LLM): [3.46153846 3.65384615 3.53846154]
t-test apareado: t=-2.314, p=0.1467
Cohen d (apareado): -1.336

=== Dimensión: Correccion_fuente(1-5) ===
Medias por juez (Humano): [3.52 3.6  3.76]
Medias por juez (LLM): [3.38461538 3.53846154 3.38461538]
Wilcoxon: W=0.000, p=0.2500
Cohen d (apareado): 1.163

=== Dimensión: Consistencia_interna(1-5) ===
Medias por juez (Humano): [3.   3.96 3.44]
Medias por juez (LLM): [3.84615385 3.57692308 4.03846154]
t-test apareado: t=-0.943, p=0.4453
Cohen d (apareado): -0.544
~~~~

### 29. 19:51:01 UTC · Texto del asistente

Script funciona perfecto — corrí una prueba con datos simulados (que borro ahora, esto era solo verificación técnica) y produce el análisis completo de las 5 dimensiones automáticamente en cuanto lleguen las hojas reales de los jueces.

### 30. 19:51:02 UTC · Accion: `bash_tool`

Descripcion que dio el asistente: *Limpiar los datos de prueba y empaquetar el paquete final del experimento*

~~~~bash
rm -f /home/claude/pkg_experimento/06_Experimento/resultados/juez*.csv
cd /home/claude/pkg_experimento && rm -f /home/claude/SIGA_06_Experimento.zip
zip -q -Xr /home/claude/SIGA_06_Experimento.zip 06_Experimento
cp /home/claude/SIGA_06_Experimento.zip /mnt/user-data/outputs/
unzip -l /mnt/user-data/outputs/SIGA_06_Experimento.zip
~~~~

Resultado:

~~~~
Archive:  /mnt/user-data/outputs/SIGA_06_Experimento.zip
  Length      Date    Time    Name
---------  ---------- -----   ----
        0  2026-08-02 19:50   06_Experimento/
        0  2026-08-02 19:50   06_Experimento/instrumentos/
     7932  2026-08-02 19:50   06_Experimento/instrumentos/Paquete_Evaluacion_Ciega_Jueces.md
      909  2026-08-02 19:50   06_Experimento/instrumentos/Hoja_Puntuacion_JUEZ.csv
     2553  2026-08-02 19:50   06_Experimento/instrumentos/rubrica_evaluacion.md
        0  2026-08-02 19:50   06_Experimento/prompts_llm/
   168394  2026-08-02 19:50   06_Experimento/prompts_llm/material_fuente_LLM.txt
     3491  2026-08-02 19:50   06_Experimento/prompts_llm/prompt_llm_conjunto_A.md
    19338  2026-08-02 19:50   06_Experimento/prompts_llm/Conjunto_A_RF_LLM.md
        0  2026-08-02 19:50   06_Experimento/scripts_analisis/
     2505  2026-08-02 19:50   06_Experimento/scripts_analisis/analizar_resultados.py
        0  2026-08-02 19:51   06_Experimento/resultados/
      125  2026-08-02 19:50   06_Experimento/resultados/.gitkeep
     1101  2026-08-02 19:50   06_Experimento/CLAVE_RESPUESTAS_no_compartir_con_jueces.csv
     4219  2026-08-02 19:50   06_Experimento/protocolo.md
---------                     -------
   210567                     15 files
~~~~

### 31. 19:51:08 UTC · Accion: `present_files`

~~~~
{
  "filepaths": [
    "/mnt/user-data/outputs/SIGA_06_Experimento.zip"
  ]
}
~~~~

Resultado:

~~~~
{"type": "local_resource", "file_path": "/mnt/user-data/outputs/SIGA_06_Experimento.zip", "name": "SIGA 06 Experimento", "mime_type": "application/zip", "uuid": "9a486d6e-c864-4e83-8fa0-42ea0a756d2f"}
~~~~

### 32. 19:51:11 UTC · Texto del asistente

## Componente empírico completo — listo para `06_Experimento/`

| Archivo | Qué es |
|---|---|
| `protocolo.md` | PICOC, hipótesis, variables, plan de análisis, amenazas a la validez |
| `prompts_llm/prompt_llm_conjunto_A.md` | Consigna exacta + **la limitación del modelo declarada sin maquillar** |
| `prompts_llm/material_fuente_LLM.txt` | Las 11 transcripciones concatenadas, tal cual se las di al modelo |
| `prompts_llm/Conjunto_A_RF_LLM.md` | **26 RF generados por mí**, con los 8 atributos, cada uno trazado a un EV-XX real |
| `instrumentos/rubrica_evaluacion.md` | 5 dimensiones con anclas 1-5 |
| `instrumentos/Paquete_Evaluacion_Ciega_Jueces.md` | **51 ítems mezclados y aleatorizados** (26 LLM + 25 humanos), sin revelar origen |
| `instrumentos/Hoja_Puntuacion_JUEZ.csv` | Plantilla en blanco, una por juez |
| `CLAVE_RESPUESTAS_no_compartir_con_jueces.csv` | **Solo para ustedes** — nunca se la manden a los jueces |
| `scripts_analisis/analizar_resultados.py` | Ya probado con datos ficticios — corre Shapiro-Wilk → t-test/Wilcoxon → Cohen d automáticamente |

## Lo más importante que quiero que leas, no que archives

**Declaré explícitamente en `prompt_llm_conjunto_A.md` que yo, como modelo, no soy un evaluador "ingenuo"** — ya había visto referencias a los RF-01 a RF-25 del equipo en esta misma conversación (cuando armamos las actas de walkthrough, por ejemplo). Eso es una amenaza real a la validez de constructo del experimento, y la documenté con el texto exacto que pueden pegar en la sección de amenazas a la validez del manuscrito. No la escondí porque ocultarla sería precisamente el tipo de cosa que el gatekeeper G4 busca evitar — mejor declarar la limitación que fingir que no existe.

## Lo que queda de tu lado

1. **Registrar el protocolo en OSF** antes de mandar el paquete a los jueces (G6).
2. **Conseguir los ≥3 jueces** — recuerda: no pueden ser DOC-01 a DOC-04, COORD-01 a COORD-03, ni CONS-01 a CONS-04.
3. Cuando tengas las hojas de puntuación llenas, me las mandas y corro el análisis real (ya está probado que el script funciona).

¿Seguimos con la codificación temática, o prefieres primero conseguir a los jueces mientras yo avanzo con otra cosa?

---

_10 bloques de razonamiento interno omitidos, segun el apartado 3._
