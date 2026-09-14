# Desviacion del protocolo — unidad de analisis del tamano del efecto

**Proyecto SIGA — Sistema Inteligente de Gestion de Aulas · Equipo FGMMN**
Universidad Tecnica Estatal de Quevedo · ISR-401 · Entrega Final (2B)

Registro previo: `10.17605/OSF.IO/7PQ3H` · Fecha de esta desviacion: **2026-09-14**

---

## 1. Que decia el plan preregistrado

El registro previo fija que los tamanos del efecto «se expresaran como la d de Cohen para los
analisis parametricos y como el delta de Cliff para los no parametricos», y que junto a los
valores p se indicaran «los tamanos del efecto y los intervalos de confianza del 95 % siempre
que sea aplicable». La actualizacion retrospectiva del mismo registro anade que esos
intervalos se calculan por bootstrap, con 10 000 replicas y semilla 20260802.

Hasta esta fecha, el tamano del efecto se calculaba con la misma unidad que el contraste
apareado: **el juez**. Para cada dimension se tomaban las tres medias por juez de cada origen
y se calculaba una d de Cohen apareada sobre esas **tres** diferencias, remuestreando las tres
para obtener el intervalo.

## 2. Por que no se puede sostener

Con tres observaciones, el bootstrap solo puede formar unas pocas muestras distintas, y
varias repiten la misma diferencia tres veces, con desviacion nula. El resultado era el
publicado hasta la version `2B-final-v5.7`:

| Dimension | d apareada | IC 95 % |
|---|---|---|
| Completitud | −1,04 | [−2,12 ; 0,00] |
| Ausencia de ambiguedad | −2,35 | [−18,38 ; 0,00] |
| Verificabilidad | −1,46 | [−12,96 ; 0,00] |
| Correccion respecto de la fuente | δ = −0,56 | [−1,00 ; 1,00] |
| Consistencia interna | −5,27 | [−42,72 ; 0,00] |

Un intervalo de amplitud cuarenta no es una estimacion: indica que el calculo se hizo sobre
muy pocas unidades y que el numero **no debe reportarse como efecto**. Asi lo observo el
docente en la evaluacion de la Entrega Final publicada el 2026-09-14. La observacion es
correcta y se atiende sin discutirla: sobre n = 3 un intervalo del tamano del efecto
**no es aplicable**, en los terminos del propio registro.

La desviacion de 2026-09-01 ([`desviacion_analisis_por_item.md`](desviacion_analisis_por_item.md))
ya habia identificado el problema y anadido el analisis con el requisito como unidad, pero
mantuvo publicados los efectos apareados como resultado primario. Esa decision es la que se
corrige aqui.

## 3. Que se hizo

**El contraste de hipotesis no cambia.** La prueba apareada sobre los tres jueces, con
Shapiro-Wilk, t de Student o Wilcoxon y correccion de Holm-Bonferroni, sigue siendo el
analisis preregistrado y se reporta integro. Ningun valor p cambia.

**El tamano del efecto cambia de unidad.** Se calcula promediando los tres jueces en cada
requisito y comparando los **25 requisitos del equipo con los 26 del modelo**:

- g de Hedges —la d de Cohen con la correccion de sesgo para muestras pequenas— cuando
  Shapiro-Wilk no rechaza la normalidad en ninguno de los dos grupos;
- delta de Cliff en caso contrario;
- intervalo de confianza del 95 % por bootstrap estratificado (cada grupo se remuestrea por
  separado), 10 000 replicas, semilla 20260802.

Es exactamente el calculo del analisis por requisito, que ya estaba publicado desde el
2026-09-01. Por eso `efectos.csv` y `analisis_por_item.csv` dan ahora los mismos valores.

| Dimension | Efecto | Valor | IC 95 % |
|---|---|---|---|
| Completitud | δ de Cliff | −0,117 | [−0,434 ; 0,200] |
| Ausencia de ambiguedad | g de Hedges | −0,257 | [−0,824 ; 0,298] |
| Verificabilidad | δ de Cliff | −0,143 | [−0,459 ; 0,177] |
| Correccion respecto de la fuente | δ de Cliff | −0,178 | [−0,477 ; 0,128] |
| Consistencia interna | δ de Cliff | −0,185 | [−0,478 ; 0,126] |

**Los efectos apareados sobre tres jueces se retiran** del reporte, del manuscrito, de la
tabla de contrastes y de la figura de tamanos del efecto. Se conservan solo en la tabla del
apartado 2 de este documento, como constancia de lo que se publico y por que se retiro.

## 4. Que cambia en la conclusion

Nada. Con cualquiera de las dos unidades, **todos los intervalos cruzan el cero** y ninguna
dimension es significativa tras la correccion de Holm. Lo que cambia es la lectura de la
magnitud: los efectos apareados sugerian efectos «grandes» que no eran estimables; con el
requisito como unidad los efectos son **pequenos** —entre −0,12 y −0,26— y todos apuntan,
sin significacion, a favor del conjunto generado por el modelo.

## 5. Por que no se eligio despues de ver el resultado

El analisis por requisito se implemento y se publico el 2026-09-01, con su resultado, antes de
esta desviacion. Aqui no se ejecuta ningun analisis nuevo: se cambia cual de los dos calculos
ya publicados se presenta como tamano del efecto, y el motivo es la imposibilidad de estimar
un intervalo sobre tres observaciones, no el valor que resulta.

## 6. Columnas `n_pares` e `interpretable`

La guia de cierre del docente, del 2026-09-14, pide anadir a `efectos.csv` el numero de pares
efectivos y si el intervalo es interpretable, y reflejarlo en la tabla del reporte y del ERS.

- **`n_pares`** vale `NA`: el efecto compara 25 requisitos con 26, que son grupos independientes
  y no pares. Las unidades efectivas constan en `n_humano` y `n_llm`.
- **`interpretable`** lo calcula la etapa `efectos`, no se escribe a mano. Vale `si` cuando el
  efecto descansa en al menos 10 unidades (pares si el calculo es apareado; si no, las del grupo
  menor), el intervalo es finito y no degenerado y, para el delta de Cliff, no cubre el
  recorrido entero [-1, 1]. Las cinco dimensiones dan `si`. Con la misma regla, la d apareada
  sobre tres jueces del apartado 2 habria dado `no` en las cinco.

Ningun valor, intervalo ni valor p cambia: solo se anaden las dos columnas, que tambien recogen
la tabla de contrastes del reporte, del manuscrito y del ERS.

## 7. El deposito de Zenodo es anterior a esta desviacion

`07_Publicacion/dataset_zenodo/` es copia de lo que se deposito en Zenodo y no se reescribe. Su
`resultados_jueces/efectos.csv` y su `scripts_analisis/analizar_resultados.py` conservan por
tanto la d apareada sobre tres jueces que esta desviacion retira. **Quien replique desde el
deposito obtendra esos intervalos; los vigentes son los de `07_Datos/resultados/estadisticos/efectos.csv`.**

## 8. Trazabilidad

| Elemento | Ruta |
|---|---|
| Script | `07_Datos/scripts/analisis/analizar_resultados.py`, etapa `efectos` (copia identica en `06_Experimento/scripts_analisis/`) |
| Salida | `07_Datos/resultados/estadisticos/efectos.csv` (y `06_Experimento/resultados/efectos.csv`) |
| Tabla de contrastes y efectos | `07_Datos/resultados/tablas/tabla_hipotesis.tex` |
| Figura | `07_Datos/resultados/figuras/fig03_tamanos_efecto.png` |
| Registro en el paquete de datos | `07_Datos/desviaciones.md`, desviacion 7 |
