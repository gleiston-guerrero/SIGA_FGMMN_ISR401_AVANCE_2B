# Desviaciones respecto del protocolo

**Paquete de datos del proyecto SIGA · Equipo FGMMN · ISR-401 · UTEQ**

Toda diferencia entre lo previsto en el protocolo registrado en OSF y lo efectivamente
ejecutado, con su fecha y su motivo. Ninguna se corrige en silencio.

---

| # | Fecha | Desviacion | Motivo | Documento |
|---|---|---|---|---|
| 1 | 2026-08-31 | La tabla de desciego estaba publicada en el repositorio publico, en `datos_crudos/` y con un nombre que afirmaba una restriccion que el repositorio no cumplia | Error de organizacion al reconstruir el arbol: un artefacto de diseno experimental quedo en una carpeta de datos crudos | [`desviacion_clave_desciego.md`](../06_Experimento/registro_previo/desviacion_clave_desciego.md) |
| 2 | 2026-09-03 | La tabla de desciego sale del repositorio publico al contenedor cifrado | Instruccion expresa del docente en la guia de desarrollo del 2026-09-02. Se publica en su lugar `asignacion_brazo_items.csv`, que conserva el brazo de cada item —lo que el analisis necesita— y retira la correspondencia con el codigo real del requisito | [`clave_desciego_UBICACION.md`](../06_Experimento/clave_desciego_UBICACION.md) |
| 3 | 2026-08-31 | El analisis por item no estaba previsto en el protocolo | Se anadio para poder examinar el comportamiento de items concretos. Se declara como analisis exploratorio, no confirmatorio | [`desviacion_analisis_por_item.md`](../06_Experimento/registro_previo/desviacion_analisis_por_item.md) |
| 4 | 2026-09-03 | Los coeficientes de acuerdo se publicaban sin intervalo de confianza | La guia de desarrollo exige que toda medida de acuerdo entre evaluadores lleve su intervalo. Se anade por bootstrap de items, sin alterar los coeficientes ya publicados | Esta carpeta, etapa `acuerdo_ic` |
| 5 | 2026-09-12 | El registro previo decia que la potencia se evaluaria **antes** de contrastar las hipotesis, y no consta que se hiciera en ese orden | En este repositorio el resultado del calculo de potencia aparece el 2026-08-30, en la misma confirmacion que los contrastes, y su script el 2026-09-01. No hay constancia de una ejecucion anterior, y no se afirma. El calculo no altera ningun contraste: solo informa de que la potencia alcanzada es 0,084 | Apartado siguiente y [`README_datos.md`](README_datos.md), seccion 6b |
| 6 | 2026-09-12 | La guía preveía ejecutar el modelo con una consigna literal sobre el material fuente. El Conjunto A se generó dentro de la conversación de trabajo del proyecto, a partir de la instrucción «usa tu propio modelo», aplicando esa tarea | Se documenta al localizarse la conversación en la exportación de claude.ai. No cambia ningún dato, puntuación ni resultado; su efecto sobre la validez es la exposición previa del modelo, declarada como amenaza de constructo desde el 2026-08-02 | [`registro_generacion_conjunto_A.md`](../06_Experimento/prompts_llm/registro_generacion_conjunto_A.md) |

---

## Sobre la desviacion 4

El intervalo se anade; el coeficiente no cambia. Los veinte valores calculados por
`scripts/etapa2_acuerdo_ic.py` reproducen, a la precision con la que se publicaron, los que
ya constaban en `06_Experimento/resultados/acuerdo_interevaluador.csv`.

Esa comprobacion es deliberada: el paquete de datos usa una implementacion independiente,
escrita solo con biblioteca estandar, y el hecho de que coincida con la de scikit-learn es
lo que permite afirmar que el intervalo se calculo sobre el mismo estimador y no sobre otro.

El estimador es kappa de Cohen **con ponderacion lineal**, porque los cinco criterios de la
rubrica son ordinales de 1 a 5 y discrepar en un punto no equivale a discrepar en cuatro.

## Lo que sigue sin resolverse

El calculo de potencia arroja **0,084 con los tres jueces disponibles**, muy por debajo de
lo deseable. El **numero** de evaluadores no es una desviacion —estaba fijado de antemano
en el registro previo, con su justificacion—, sino una limitacion del diseno, y se declara
como amenaza a la validez de conclusion estadistica en el manuscrito. Lo que si es una
desviacion es el **momento** del calculo, y es la numero 5 de la tabla. Los intervalos de confianza
que ahora acompanan a cada coeficiente de acuerdo hacen visible esa misma imprecision.
