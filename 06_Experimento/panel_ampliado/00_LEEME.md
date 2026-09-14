# El panel ampliado: dos intentos y lo que ensenaron

**Proyecto SIGA --- Sistema Inteligente de Gestion de Aulas · Equipo FGMMN**
Universidad Tecnica Estatal de Quevedo · ISR-401 · Entrega Final (2B)

---

## 1. Que hay en esta carpeta y que no

Esta carpeta **no contiene el analisis del estudio**. El analisis del estudio es el de
los tres jueces que fija el registro previo de OSF `10.17605/OSF.IO/7PQ3H`, y esta en
`06_Experimento/resultados/`.

Aqui esta una **comprobacion de robustez que fallo**, hecha dos veces, con sus datos
crudos y su script. Se publica porque el resultado dice algo util, y porque un intento
que sale mal y se calla es la clase de cosa que hace irreproducible un estudio.

| | |
|---|---|
| `datos_crudos/primera_vuelta/` | 7 hojas, 2026-09-05, instrumento original de 51 enunciados y 5 dimensiones |
| `datos_crudos/segunda_vuelta/` | 7 hojas, 2026-09-06, instrumento corregido de 27 posiciones y 4 dimensiones |
| `datos_crudos/mapa_posiciones_segunda_vuelta.csv` | Posicion → item ciego, brazo y numero de aparicion |
| `analizar_panel_ampliado.py` | Reproduce las cuatro tablas desde los datos crudos |
| `resultados/` | Las cuatro tablas |

## 2. Que se intentaba

El registro previo fija tres jueces. Tres es poco, y la potencia calculada del contraste
--- **8,4 %** --- lo dice sin rodeos. Ampliar el panel a diez era la comprobacion obvia: si
la diferencia entre los requisitos del equipo y los del modelo es real, deberia
sobrevivir a mas evaluadores.

No sobrevivio. Y lo importante no es que no sobreviviera, sino **por que**.

## 3. Primera vuelta --- 2026-09-05

Siete evaluadores nuevos puntuaron los 51 enunciados en las 5 dimensiones: 255 juicios por
persona, en una sesion de unos 45 minutos.

| | |
|---|---|
| Fleiss kappa, media de las 4 dimensiones comunes | **--0,008** |
| Acuerdo crudo exacto entre parejas | 27,1 % |
| Acuerdo que daria el azar con ese mismo reparto | 27,7 % |

Con los diez jueces juntos, los cinco tamanos de efecto caian de d = --1,04…--5,27 a valores
en torno a cero y ninguna hipotesis quedaba significativa. **Nada de eso se deposito** como
analisis: se reviro el repositorio al estado publicado y se diagnostico el fallo.

> **Nota del 2026-09-14.** Esa d apareada sobre tres jueces se retiro como tamano del efecto
> porque su intervalo no es interpretable con n = 3 (desviacion 7,
> [`desviacion_tamano_efecto.md`](../registro_previo/desviacion_tamano_efecto.md)). Las cifras
> de este parrafo se conservan porque describen lo que se observo entonces; no son un
> resultado vigente. El efecto vigente se calcula con el requisito como unidad y es pequeno.

Tres causas, todas del procedimiento y ninguna del objeto de estudio:

1. **255 juicios en 45 minutos** son 10,6 segundos por juicio.
2. La dimension **«Correccion respecto de la fuente» no se podia responder**: pregunta si el
   enunciado es fiel a lo que dijeron los participantes, y el paquete entregado no incluia
   las transcripciones. Sin ellas la pregunta no tiene respuesta posible, solo una casilla
   que hay que rellenar igual.
3. **Cero calibracion.** Nadie vio un ejemplo puntuado antes de empezar.

## 4. Segunda vuelta --- 2026-09-06

El instrumento se rehizo para atacar las tres causas:

| | Primera | Segunda |
|---|---|---|
| Enunciados | 51 | **24**, 12 de cada brazo, seleccion aleatoria con semilla `20260906` |
| Dimensiones | 5 | **4** --- se retira «Correccion respecto de la fuente» |
| Juicios por persona | 255 | **108** |
| Anclas de la rubrica | En un archivo aparte | **Impresas en la hoja** |
| Calibracion previa | Ninguna | Tres ejemplos puntuados en grupo |
| Repetidos de control | Ninguno | **3**, ocultos en las posiciones 20, 24 y 26 |

Las 27 posiciones son los 24 enunciados mas los 3 repetidos. Los repetidos son la novedad
que mas rinde: el mismo enunciado aparece dos veces, separado 13, 14 y 16 posiciones de su
gemelo, y nadie sabe cuales son. Miden si una persona se puntua igual a si misma.

Sesion unica supervisada, **10:00 a 10:35**, los siete a la vez. 35 minutos para 108
juicios son **19,4 segundos por juicio** --- mejor que los 10,6 de la primera vuelta, pero
sigue siendo rapido y se declara como tal.

### El resultado

| Dimension | Fleiss kappa |
|---|---|
| Completitud | --0,028 |
| Ausencia de ambiguedad | +0,000 |
| Verificabilidad | --0,053 |
| Consistencia interna | --0,023 |
| **Media** | **--0,026** |

**Lo que estaba acordado por escrito antes de la sesion es la regla de decision, no una
cifra.** El protocolo de la segunda vuelta ---
[`protocolo_segunda_vuelta.md`](protocolo_segunda_vuelta.md), redactado el 2026-09-06 antes
de convocar a nadie --- dice literalmente:

> «**Si el acuerdo vuelve a salir cerca de cero**, la decision es mantener los tres jueces
> del registro previo como analisis primario y reportar las dos vueltas como lo que son: la
> prueba de que esta rubrica necesita evaluadores entrenados.»

Es lo que se ha aplicado, sin cambiar el criterio despues de ver el resultado.

**El 0,41 no procede de ese documento y no se presenta como umbral pactado.** Es la frontera
de Landis y Koch para acuerdo moderado, el convencionalismo con el que se lee cualquier kappa
en la literatura, y se usa aqui como referencia de lectura. La media obtenida, --0,026, no
queda por debajo de un liston que el equipo se hubiera fijado: queda por debajo de cualquier
lectura posible de la escala, porque es indistinguible del azar.

## 5. Por que no es un artefacto de kappa

Kappa castiga las escalas concentradas, y esta lo esta: el 81,5 % de las 756 puntuaciones
de la segunda vuelta son 4 o 5, y **el 1 no se uso ni una sola vez**. Con ese reparto, el
acuerdo esperado por azar sube y el techo de kappa baja. Es la objecion correcta y hay que
responderla con numeros, no descartarla.

Se responde comparando el acuerdo observado con el esperado:

| | Observado | Esperado por azar |
|---|---|---|
| Primera vuelta | 27,1 % | 27,7 % |
| Segunda vuelta | 37,5 % | 39,1 % |

**En las dos vueltas coinciden menos de lo que coincidirian tirando un dado cargado con sus
propias frecuencias.** No es que kappa exagere un acuerdo real; es que no hay acuerdo que
exagerar. El acuerdo dentro de un punto sube al 83,4 % en la segunda vuelta, pero con una
escala que solo usa tres valores eso es casi automatico y no prueba nada.

Tampoco lo salva quedarse con los mejores. Ordenando a los siete por su consistencia
interna y quedandose con los mas consistentes, kappa media no llega a positiva en ningun
corte: --0,027 con dos, --0,044 con tres, --0,056 con cuatro, --0,058 con cinco, --0,041 con
seis, --0,026 con los siete. No hay subconjunto que concuerde.

## 6. Lo que si midieron los repetidos

Aqui esta el hallazgo, y es el que justifica publicar todo esto.

| Juez | Puntuaciones identicas al reencontrar el mismo enunciado | Diferencia media | Maxima |
|---|---|---|---|
| JUEZ-06 | 7 de 12 | 0,42 | 1 |
| JUEZ-04 | 6 de 12 | 0,50 | 1 |
| JUEZ-05 | 6 de 12 | 0,50 | 1 |
| JUEZ-07 | 4 de 12 | 0,83 | 2 |
| JUEZ-08 | 2 de 12 | 1,25 | **3** |
| JUEZ-09 | **0 de 12** | 1,33 | **3** |
| JUEZ-10 | 1 de 12 | 1,33 | 2 |

Tres evaluadores se contradicen a si mismos **hasta en 3 puntos de una escala de 5**, sobre
el mismo enunciado, en la misma sesion, con veinte minutos de diferencia. JUEZ-09 no repite
ni una sola de sus doce puntuaciones.

Eso cambia la interpretacion por completo. Sin los repetidos, el resultado seria «siete
personas opinan cosas distintas», que es discutible y hasta legitimo. Con los repetidos, el
resultado es **«el ruido esta dentro de cada evaluador, no entre ellos»**: si alguien no
coincide consigo mismo, es imposible que coincida con otro, y la falta de acuerdo entre
jueces no mide desacuerdo, mide inestabilidad de la medicion.

## 7. Que se concluye

**El analisis primario del estudio sigue siendo el de los tres jueces del registro previo.**
No por conveniencia --- son los que dan efecto --- sino porque es lo que fija el registro
previo, porque son los unicos que concuerdan entre si, y porque la regla para sustituirlos
se escribio antes de mirar los datos y la condicion que la activaba no se cumplio, dos
veces.

El contraste es directo, y se mide sobre las mismas cuatro dimensiones en los tres casos:

| Panel | Fleiss kappa | Correlacion media entre parejas | Acuerdo crudo exacto |
|---|---|---|---|
| **Los 3 del registro previo** | **0,296--0,340** | **+0,731** | **53,3 %** |
| Los 7 de la primera vuelta | --0,029 a +0,006 | --0,002 | 27,1 % |
| Los 7 de la segunda vuelta | --0,053 a +0,000 | +0,085 | 37,5 % |

Los tres originales no son mejores por poco: coinciden exactamente en la mitad de sus
puntuaciones, y los siete en poco mas de un tercio, que es lo que da el azar.

El panel ampliado se reporta como lo que es: **una comprobacion de robustez que no se pudo
completar porque el instrumento no es utilizable por evaluadores sin entrenar.** Y esa es
una afirmacion con valor propio para quien quiera replicar el estudio:

> Una rubrica de calidad de requisitos de cinco dimensiones y cinco puntos, entregada a
> estudiantes de la propia carrera sin entrenamiento previo, no produce mediciones estables
> ni siquiera dentro de una misma persona. Dos intentos, dos instrumentos y dos
> procedimientos distintos dieron el mismo resultado. Un panel asi no amplia la potencia de
> un estudio: le anade ruido.

Lo que faltaria para hacerlo bien --- y no cabia en el plazo de esta entrega --- es una
sesion de entrenamiento con enunciados de practica corregidos en grupo hasta que el acuerdo
suba, antes de tocar los enunciados del estudio. Sin ese paso, mas evaluadores solo son mas
ruido.

## 8. Consentimiento de los evaluadores

Los siete firmaron un consentimiento especifico para el panel antes de puntuar. Sus datos
se manejan solo por el codigo `JUEZ-04` a `JUEZ-10`: **las hojas depositadas en esta carpeta
no llevan nombre, ni firma, ni ningun dato que permita llegar a la persona**, solo el codigo
y las puntuaciones.

Los consentimientos firmados, que si llevan nombre y firma manuscrita, **quedan fuera del
repositorio** y estan declarados como tales en
[`../../02_Evidencias/00_Restringido/README_Restringido.md`](../../02_Evidencias/00_Restringido/README_Restringido.md),
apartado 2, junto con el resto del material que el consentimiento no autoriza a publicar.

## 9. Como reproducirlo

```
python 06_Experimento/panel_ampliado/analizar_panel_ampliado.py
```

Solo biblioteca estandar. Escribe las cuatro tablas de `resultados/` desde los datos crudos
y no toca nada de `06_Experimento/resultados/`.
