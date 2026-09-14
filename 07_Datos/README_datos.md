# Paquete de datos — Proyecto SIGA

**Equipo FGMMN · Ingenieria de Requisitos (ISR-401) · Universidad Tecnica Estatal de Quevedo**

Este es el paquete de datos del componente empirico: el cuasi-experimento de evaluacion
ciega en el que tres jueces independientes puntuaron 51 requisitos —unos redactados por el
equipo, otros generados por un modelo de lenguaje— en cinco dimensiones de calidad.

---

## 1. Como se reproduce, en una sola orden

Desde la raiz del repositorio recien clonado:

```
python 07_Datos/scripts/ejecutar.py
```

Eso reconstruye **todo** el contenido de `datos_procesados/` y de `resultados/` a partir
unicamente de `datos_crudos/`. **La cadena de analisis estadistico se ejecuta aqui dentro**,
con los scripts de `scripts/analisis/`, y escribe en `resultados/tablas/`,
`resultados/figuras/` y `resultados/estadisticos/` las tablas y figuras del documento.
Comprueba que salen identicas byte a byte a las del manifiesto y termina comprobando la
integridad del paquete.

**El reporte y el manuscrito incluyen sus tablas y figuras directamente desde
`07_Datos/resultados/`.** Lo que produce esta orden no es una copia de lo que aparece en los
documentos: es lo mismo que los documentos cargan al compilarse.

**Una sola dependencia previa.** Las etapas propias del paquete usan solo la biblioteca
estandar de Python. La etapa `analisis` ejecuta la cadena de analisis estadistico, que
necesita seis bibliotecas con version fijada. Se instalan una vez, antes de la orden:

```
pip install -r 06_Experimento/requirements.txt
```

Si faltan, la etapa `analisis` lo dice y se detiene sin tocar nada; no hay que editar
ningun archivo ni ejecutar nada a mano.

Para ver las etapas sin ejecutarlas:

```
python 07_Datos/scripts/ejecutar.py --listar
```

---

## 2. Que contiene cada carpeta

| Ruta | Contenido |
|---|---|
| `datos_crudos/` | Los datos **tal como salieron del instrumento**, sin ninguna edicion manual |
| `datos_procesados/` | Derivados, generados solo por los scripts. Se pueden borrar y regenerar |
| `scripts/` | El orquestador y las cinco etapas |
| `scripts/analisis/` | **La cadena de analisis estadistico**: consolidacion, acuerdo, supuestos, contrastes, tamanos del efecto, analisis por requisito, saturacion, potencia, tablas y figuras |
| `resultados/` | Acuerdo entre evaluadores con su intervalo, generado por la etapa `acuerdo_ic`. Nunca escrito a mano |
| `resultados/tablas/` | **Las siete tablas del documento**: seis `.tex` que el reporte y el manuscrito incluyen desde aqui, y la tabla de saturacion en CSV |
| `resultados/figuras/` | **Las cuatro figuras del documento**, en PNG, incluidas desde aqui por el reporte y el manuscrito |
| `resultados/estadisticos/` | Los seis resultados estadisticos de los que salen esas tablas y figuras: acuerdo, supuestos, hipotesis, tamanos del efecto, analisis por item y potencia |
| `diccionario_datos.csv` | Cada columna de cada CSV: tipo, unidad, rango, faltantes y procedencia |
| `desviaciones.md` | Toda diferencia respecto de lo previsto en el protocolo, con fecha y motivo |
| `registro_deposito.md` | Identificadores persistentes del deposito y sus fechas |
| `checksums_datos.sha256` | Manifiesto de sumas de todo el paquete |
| `LICENSE-DATA.txt` | Licencia de los datos, distinta de la del codigo |

### Los datos crudos

| Archivo | Que es |
|---|---|
| `juez1.csv`, `juez2.csv`, `juez3.csv` | Las hojas de puntuacion devueltas por cada juez. 51 items x 5 dimensiones |
| `asignacion_brazo_items.csv` | A que brazo del experimento pertenece cada item ciego: `Humano` o `LLM` |
| `material_fuente_LLM.txt` | **El corpus fuente comun** del que salieron ambos conjuntos de requisitos: las transcripciones anonimizadas de la segunda ronda de campo, tal como se entregaron al modelo. EV-15 esta suprimida por retiro del consentimiento |
| `paquete_evaluacion_ciega.md` | El instrumento entregado a los jueces: los 51 enunciados con su identificador ciego, en el orden en que se presentaron |
| `corpus_rf_rnf_etiquetado.json` | Los requisitos elicitados por el equipo con su trazabilidad: casos de uso, evidencias, componentes y priorizacion |
| `respuestas_cuestionario.csv` | Las 31 respuestas del cuestionario digital v2.0 (EV-17), anonimas |

Las dos primeras son copias identicas byte a byte de
`06_Experimento/prompts_llm/material_fuente_LLM.txt` y
`06_Experimento/instrumentos/Paquete_Evaluacion_Ciega_Jueces.md`; la etapa `integridad` lo
comprueba. El registro integro de la generacion —la instruccion que recibio el modelo, cada accion que
ejecuto y su hora— esta en
[`06_Experimento/prompts_llm/registro_generacion_conjunto_A.md`](../06_Experimento/prompts_llm/registro_generacion_conjunto_A.md),
y el modelo, la interfaz y los parametros en
[`prompt_llm_conjunto_A.md`](../06_Experimento/prompts_llm/prompt_llm_conjunto_A.md).

### Las etapas

| Etapa | Que produce |
|---|---|
| `formato_largo` | `evaluacion_ciega_formato_largo.csv` — evaluador, requisito, orden de presentacion, brazo, criterio y puntuacion. 765 filas |
| `acuerdo_ic` | `acuerdo_interevaluador_ic.csv` — kappa de Cohen ponderado y de Fleiss, cada uno con su intervalo de confianza del 95 % |
| `conjuntos` | `conjunto_A_llm.txt` (26 requisitos) y `conjunto_B_humano.txt` (25), en texto plano y con el enunciado literal que vieron los jueces. No contienen la tabla de desciego |
| `analisis` | Ejecuta la cadena de `scripts/analisis/` sobre `datos_crudos/` y escribe 7 tablas en `resultados/tablas/`, 4 figuras en `resultados/figuras/`, 6 resultados en `resultados/estadisticos/` y `puntuaciones_consolidadas.csv` en `datos_procesados/`. Antes vacia esas tres carpetas de resultados, para que lo que quede sea lo que acaba de producir la orden. No llama a nada de `06_Experimento` ni de `07_Publicacion`. Falla si una sola de las 18 salidas difiere del manifiesto `checksums.sha256` |
| `integridad` | Comprueba que los datos crudos, los seis scripts de analisis y las 18 salidas son identicos byte a byte a sus equivalentes de `06_Experimento` y `07_Publicacion`, la cobertura del diccionario, y regenera el manifiesto de sumas |

---

## 3. Sobre el orden de presentacion

La hoja en formato largo incluye la columna `orden_presentacion`, y conviene decir de donde
sale porque no es un dato que se haya medido despues.

El paquete de evaluacion ciega se armo **una sola vez, con los items en orden aleatorizado**,
y ese mismo orden se entrego a los tres jueces. Asi lo declara
`06_Experimento/instrumentos/Paquete_Evaluacion_Ciega_Jueces.md` en sus instrucciones. Por
tanto el orden de presentacion de un item es su posicion en el paquete: `Item-01` se
presento en primer lugar, `Item-51` en ultimo.

**No hubo un orden distinto por juez.** Quien quiera comprobarlo tiene el instrumento
completo en esa ruta.

---

## 4. Sobre la tabla de desciego

`asignacion_brazo_items.csv` dice a que brazo pertenece cada item, que es lo que el analisis
necesita. **No** dice a que requisito real corresponde cada item ciego.

Esa correspondencia —la tabla de desciego propiamente dicha— no reside en el repositorio
publico. Donde esta y quien la custodia consta en
[`06_Experimento/clave_desciego_UBICACION.md`](../06_Experimento/clave_desciego_UBICACION.md),
y la desviacion que la motivo sigue anotada en
[`06_Experimento/registro_previo/desviacion_clave_desciego.md`](../06_Experimento/registro_previo/desviacion_clave_desciego.md).

---

## 5. Relacion con 06_Experimento

Las dos carpetas no se solapan por descuido, y conviene entender el reparto:

- **`06_Experimento/`** es el componente empirico: el protocolo, el registro previo en OSF,
  los instrumentos, las consignas dadas al modelo de lenguaje, los scripts de analisis
  estadistico y sus salidas. Es la cadena del estudio.
- **`07_Datos/`** es el paquete de datos: la unidad depositable, autocontenida y verificable
  por un tercero sin conocer el resto del repositorio. **La cadena que genera las tablas y
  figuras del documento vive aqui**, en `scripts/analisis/`, y el reporte y el manuscrito
  las toman de `resultados/`.

`06_Experimento/replicar.py` y su `Makefile` siguen funcionando igual que antes, con los
mismos scripts en `06_Experimento/scripts_analisis/`, porque forman parte del componente
empirico ya verificado. Los datos crudos, los seis scripts de analisis y las 18 salidas son
**los mismos** en los dos sitios, no una version parecida: la etapa `integridad` lo comprueba
con sumas SHA-256 y falla si alguien edita una sola de las copias. Esa comprobacion es la
razon por la que la duplicacion es segura.

---

## 6. Que numeros salen de aqui

Ningun numero de los documentos del proyecto esta escrito a mano. Los que proceden de este
paquete son:

| Numero | Donde aparece | Se regenera con |
|---|---|---|
| Kappa de Cohen y de Fleiss por dimension | Reporte del estudio y manuscrito | `acuerdo_ic` |
| Intervalos de confianza del acuerdo | Reporte del estudio | `acuerdo_ic` |
| 765 valoraciones, 51 items, 3 jueces | Reporte, manuscrito y ERS | `formato_largo` |

Los tamanos del efecto, los contrastes de hipotesis y el calculo de potencia los calcula la
etapa `analisis`, con los scripts de `scripts/analisis/`, de modo que tambien esos numeros,
y las tablas y figuras que los muestran, salen de la misma orden unica y quedan dentro de
`07_Datos/`.

| Numero | Donde aparece | Se regenera con |
|---|---|---|
| Tamano del efecto por dimension con IC del 95 %, con el requisito como unidad (25 frente a 26; desviacion 7) | Reporte y manuscrito | `analisis` → `resultados/estadisticos/efectos.csv`, `resultados/tablas/tabla_hipotesis.tex` y `resultados/figuras/fig03_tamanos_efecto.png` |
| Analisis de sensibilidad con el requisito como unidad: contrastes independientes | Manuscrito, tabla por item | `analisis` → `resultados/estadisticos/analisis_por_item.csv` y `resultados/tablas/tabla_por_item.tex` |
| Contrastes de hipotesis y supuestos | Reporte y manuscrito | `analisis` → `resultados/estadisticos/hipotesis.csv`, `supuestos.csv` y sus tablas `.tex` |
| Potencia alcanzada | Manuscrito y reporte | `analisis` → `resultados/estadisticos/power_calculation.csv` y `resultados/tablas/tabla_power_calculation.tex`, con el numero de jueces **contado** en `datos_crudos/`, no escrito a mano |
| Curva de saturacion tematica | Reporte y manuscrito | `analisis` → `resultados/tablas/saturacion_por_entrevista.csv` y `resultados/figuras/curva_saturacion.png` |

---

## 6b. Justificacion del tamano muestral y del numero de evaluadores

Consta **antes del analisis**, en el registro previo del protocolo en OSF
(`10.17605/OSF.IO/7PQ3H`, aceptado el 2026-08-02), cuyo texto integro se conserva en
`06_Experimento/registro_previo/osf_registration_api.json`:

- **Tamano de la muestra.** No hay muestreo: se analiza la **poblacion completa** de
  requisitos funcionales elegibles generados por los dos enfoques en el estudio de caso,
  que resultaron ser 25 del equipo y 26 del modelo.
- **Numero de evaluadores.** Un **minimo de tres** evaluadores independientes, fijado para
  poder estimar el acuerdo entre pares (kappa de Cohen) y entre todos (kappa de Fleiss) y
  para reducir el sesgo de un evaluador individual.

Lo que el registro preveia y **no** se hizo en el orden previsto es el calculo de potencia:
el registro dice que se evaluaria antes de contrastar las hipotesis, y se ejecuto despues.
Esta declarado como desviacion 5 en [`desviaciones.md`](desviaciones.md).

---

## 7. Politica de datos personales

En este paquete **no hay ningun dato personal**. Las hojas de los jueces se identifican como
`juez1`, `juez2` y `juez3`; el cuestionario se recogio de forma anonima y sin campos
identificables. El material que si contiene datos personales —consentimientos firmados,
originales de camara, registro de custodia codigo-participante— se conserva en el contenedor
cifrado AES-256 descrito en
[`02_Evidencias/00_Restringido/README_Restringido.md`](../02_Evidencias/00_Restringido/README_Restringido.md)
y no se publica.
