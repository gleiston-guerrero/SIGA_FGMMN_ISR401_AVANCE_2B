# Registro de la consigna — Conjunto A (RF generados por LLM)

**Enfoque:** 1 (comparación de calidad de RF humanos vs. LLM), Sección 5.1 de la
Guía y Rúbrica de la Entrega 3 (2A).

## Estado de este registro (actualizado el 2026-09-12)

> **El registro íntegro de la generación existe y está depositado** en
> [`registro_generacion_conjunto_A.md`](registro_generacion_conjunto_A.md), extraído de la
> exportación oficial de claude.ai de la cuenta del analista líder: la instrucción que se dio
> al modelo, cada acción que ejecutó y el Conjunto A que escribió, con su hora. Precisa cómo
> se generó: **dentro de la conversación de trabajo del proyecto, a partir de la instrucción
> «usa tu propio modelo»**, aplicando la tarea de la guía, y no enviando la consigna literal
> en una sesión aparte. Lo que sigue en este archivo se conserva como se escribió el
> 2026-08-02.

Este archivo se redactó el 2026-08-02, el mismo día de la consulta, y se conserva tal cual
a partir del apartado siguiente. Esta nota solo precisa **qué es íntegro y qué no**, porque
la rúbrica de cierre pide el registro íntegro de las instrucciones dadas a la herramienta.

| | Estado |
|---|---|
| Instrucción que produjo el Conjunto A | **Íntegra** en `registro_generacion_conjunto_A.md`: «Hagamos las 11 · Usa tu propio modelo». La consigna de la guía que se cita más abajo es la tarea que el modelo aplicó; no se le envió como mensaje |
| Plantilla de ocho atributos indicada al modelo | **Íntegra**: apartado final |
| Material fuente entregado | **Íntegro salvo EV-15**: `material_fuente_LLM.txt`. El texto de EV-15 se entregó al modelo el 2026-08-02 y se suprimió del archivo después, cuando el participante retiró su consentimiento (confirmado el 2026-08-13); en su lugar queda una nota. Por eso el archivo tiene hoy 23 934 palabras y no las 27 124 que se citan más abajo |
| Modelo, interfaz y fecha | **Íntegros**: tabla siguiente |
| Temperatura, top-p y semilla | **No disponibles**: la interfaz de chat no los expone |
| Exportación completa de la conversación | **Existe.** Se localizó el 2026-09-12 en la exportación de datos de claude.ai de la cuenta del analista líder, que la conserva. La copia pública, con las omisiones que declara, es `registro_generacion_conjunto_A.md` |
| Conjunto A resultante | `Conjunto_A_RF_LLM.md`, y en texto plano, tal como lo vieron los jueces, en `07_Datos/datos_procesados/conjunto_A_llm.txt` |
| Conjunto B con el que se compara | En texto plano en `07_Datos/datos_procesados/conjunto_B_humano.txt` |

La recomendación del final de la sección de limitaciones —repetir la generación por API
con una sesión nueva antes de la Entrega 2B— **no se ejecutó**. El estudio se hizo con el
Conjunto A tal como se generó el 2026-08-02 y la exposición previa se declara como amenaza
a la validez de constructo en el manuscrito.

---

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

## Consigna exacta de la guía (Sección 5.1)

> Nota del 2026-09-12: es la consigna que prescribe la guía y la tarea que el modelo aplicó.
> El mensaje que efectivamente recibió está en `registro_generacion_conjunto_A.md`.

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
