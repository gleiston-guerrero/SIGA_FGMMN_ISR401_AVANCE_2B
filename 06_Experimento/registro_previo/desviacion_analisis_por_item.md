# Desviacion del protocolo — analisis de sensibilidad por item

**Proyecto SIGA — Sistema Inteligente de Gestion de Aulas · Equipo FGMMN**
Universidad Tecnica Estatal de Quevedo · ISR-401 · Entrega Final (2B)

Registro previo: `10.17605/OSF.IO/7PQ3H` · Fecha de esta desviacion: **2026-09-01**

---

## 1. Que decia el plan preregistrado

El protocolo registrado en OSF fija como unidad de analisis **al juez**: para cada dimension
se promedian las puntuaciones que cada juez otorgo a los items de cada origen, y se comparan
las dos series resultantes con una prueba apareada sobre **n = 3**.

Ese diseno tiene una razon: controla la severidad de cada evaluador, porque cada juez actua
como su propio control. Es una eleccion defendible y se mantiene como **analisis primario**.

## 2. Que problema aparecio al ejecutarlo

Dos, y ambos se detectaron al mirar las salidas, no antes.

**La potencia es de 0,084.** El propio `power_calculation.csv` lo declara: para detectar un
efecto mediano harian falta 34 observaciones apareadas y hay 3. La probabilidad de detectar
una diferencia real, si existiera, es de menos del 9 %.

**Los intervalos de confianza del tamano del efecto no se pueden interpretar.** Con n = 3, la
d de Cohen apareada alcanza valores como −5,27 con un intervalo de [−42,72 , 0,00]. Un
intervalo de esa amplitud no informa de nada.

De fondo hay un desperdicio de informacion: el estudio recogio **765 calificaciones**
individuales —51 items por 5 dimensiones por 3 jueces— y el analisis primario las reduce a
tres medias apareadas por dimension.

## 3. Que se hizo, y que no

**Se anadio** un analisis de sensibilidad que toma **el requisito** como unidad: se promedian
los tres jueces dentro de cada item, con lo que la comparacion pasa a 25 requisitos humanos
frente a 26 generados por el modelo. Como los dos conjuntos contienen requisitos distintos y
no el mismo requisito medido dos veces, la prueba es de muestras independientes: t de Welch
cuando Shapiro-Wilk no rechaza la normalidad y U de Mann-Whitney cuando la rechaza, con
correccion de Holm-Bonferroni sobre las cinco dimensiones y tamanos de efecto con intervalo
por bootstrap de 10.000 replicas, semilla 20260802.

**No se sustituyo nada.** El analisis preregistrado sigue siendo el primario y se reporta
integro en la seccion de resultados del manuscrito. El de sensibilidad se reporta despues,
etiquetado como **exploratorio y posterior al registro**.

**No se eligio despues de ver cual daba un resultado mejor.** Se implemento una sola vez, se
ejecuto una sola vez, y su resultado se reporta tal como salio.

## 4. Que cambia y que no

| | Analisis primario (n = 3) | Sensibilidad por item (n = 51) |
|---|---|---|
| Potencia para d = 0,5 | 0,084 | **0,417** |
| Tamanos de efecto | d hasta −5,27 | delta de Cliff entre −0,117 y −0,185; g de Hedges −0,257 |
| Intervalos de confianza | hasta [−42,72 , 0,00] | todos estrechos y **todos cruzan cero** |
| Dimensiones significativas tras Holm | **ninguna** | **ninguna** |

**Las dos coinciden en la conclusion.** Ni el analisis preregistrado ni el de sensibilidad
encuentran diferencia estadisticamente significativa entre los requisitos elicitados por el
equipo humano y los generados por el modelo de lenguaje, en ninguna de las cinco dimensiones,
despues de corregir por comparaciones multiples.

Esa coincidencia es el motivo de hacer un analisis de sensibilidad: **muestra que la
conclusion no depende de la eleccion analitica**. Un resultado nulo obtenido de un panel de
tres jueces merece esa comprobacion antes de que nadie se lo crea.

> **Actualizacion 2026-09-14.** Los efectos apareados de la columna izquierda ya no se
> publican como tamano del efecto. Desde esa fecha el tamano del efecto se calcula con el
> requisito como unidad, que es el de la columna derecha. El contraste apareado de n = 3 se
> mantiene. Motivo y detalle en [`desviacion_tamano_efecto.md`](desviacion_tamano_efecto.md).

## 5. Lo que sigue sin resolverse

La potencia sube de 0,084 a 0,417, y **0,417 sigue estando por debajo del 0,80 convencional**.
El estudio continua sin potencia suficiente para descartar un efecto pequeno, y asi se
declara en las amenazas a la validez del manuscrito. Lo que la desviacion consigue no es
convertir el estudio en concluyente: es dejar de presentar como interpretables unas cifras
que no lo eran.

## 6. Trazabilidad

| Elemento | Ruta |
|---|---|
| Script | `06_Experimento/scripts_analisis/analisis_por_item.py` |
| Etapa del pipeline | `por_item`, en `replicar.py` |
| Salida | `06_Experimento/resultados/analisis_por_item.csv` |
| Tabla del manuscrito | `07_Publicacion/tablas/tabla_por_item.tex` |
| Seccion del manuscrito | *Sensitivity analysis: the requirement as the unit of analysis* |
