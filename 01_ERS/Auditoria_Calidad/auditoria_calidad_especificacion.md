# Auditoria de calidad de la especificacion

Proyecto SIGA · ISR-401 · Equipo FGMMN · Universidad Tecnica Estatal de Quevedo
Version 3.0 · Medicion inicial del 2026-08-29 sobre el ERS/SRS v2.0, remedida el 2026-08-31
y el 2026-09-05. Las secciones 1 a 7 conservan la medicion inicial; el estado vigente de las
seis metricas es el de la seccion 8

Las seis metricas de la seccion 5.6 de la guia, cada una con su formula aplicada, sus
conteos base publicados **antes** de calcular, la aritmetica visible, el veredicto y la
accion de mejora.

---

## 1. Conteos base

Publicados antes de calcular ninguna metrica. Obtenidos por recuento automatico sobre
`01_ERS/secciones_generadas.tex` y `04_Trazabilidad/matriz_trazabilidad.csv`.

| Conteo | Valor |
|---|---|
| Requisitos funcionales especificados | 25 |
| Requisitos no funcionales especificados | 16 |
| Casos de uso identificados | 16 |
| Casos de uso especificados textualmente | 16 |
| Historias de usuario | 17 |
| Restricciones de diseno | 18 |
| Fichas de requisito funcional analizadas | 25 |
| Filas de la matriz de trazabilidad | 66 |
| Pares de requisitos funcionales posibles | 300 |

---

## 2. Completitud

**Formula.** Requisitos con los ocho atributos obligatorios completos, dividido por el
total de requisitos. Se acompana de dos submetricas: casos de uso especificados sobre
identificados, y actores con al menos un requisito asociado.

| Submetrica | Aritmetica | Resultado | Referencia | Veredicto |
|---|---|---|---|---|
| Requisitos con atributos completos | 25 / 25 | **100 %** | ≥ 95 % | **Cumple** |
| Casos de uso especificados sobre identificados | 16 / 16 | **100 %** | 100 % | **Cumple** |
| Actores con al menos un requisito | 3 / 3 | **100 %** | 100 % | **Cumple** |

**Hallazgo.** El recuento automatico marca **RF-01** como ficha incompleta por el atributo
de descripcion.

**Resuelto el 2026-08-30: era un artefacto del analisis, no un defecto.** La ficha de
RF-01 se reviso a mano y sus ocho atributos estan presentes y completos. El recuento
fallaba porque la fila de encabezado de esa tabla lleva marcado de color
(`\cellcolor` y `\textcolor`) que las demas fichas no tienen, y el analizador no lo
atravesaba.

**Valor corregido de la metrica.** Completitud pasa de 24/25 a **25/25 = 100 %**, por
encima de la referencia de 95 %. El conteo base de `conteos_base.csv` se mantiene tal
como se publico; lo que cambia es la clasificacion de esa unica ficha, y queda registrado
aqui para que la proxima medicion no vuelva a levantarla.

**Accion sobre el instrumento.** El analizador debe ignorar el marcado de color antes de
contar atributos. Mientras no se corrija, toda ficha con encabezado coloreado dara un
falso negativo.

---

## 3. Consistencia

**Formula.** Uno menos el cociente entre pares de requisitos en conflicto y pares
analizados. Con 25 requisitos funcionales, los pares posibles son 25 × 24 / 2 = **300**.

El analisis se concentro en tres familias donde el conflicto es plausible: umbrales de
tiempo que compiten entre si, disparadores que se solapan, y requisitos que actuan sobre
el mismo equipo.

| Par analizado | Naturaleza | Resultado |
|---|---|---|
| RF-13 y RF-16 | Ambos apagan equipos de un aula desocupada fuera de horario, ambos con umbral ≤ 2 minutos | **Conflicto en la medicion inicial. Resuelto el 2026-08-30** |
| RF-03 con RF-13 y RF-16 | La deteccion de ocupacion (≤ 15 s) alimenta a los dos apagados (≤ 2 min) | Consistente: el presupuesto de tiempo encaja |
| RF-08 y RNF-01 | Alerta de anomalia ≤ 1 min frente a entrega de alertas ≤ 60 s | Consistente: es el mismo valor |
| RF-08 y RF-11 | Alerta general ≤ 1 min frente a notificacion critica ≤ 30 s | Consistente: la critica es mas estricta, como corresponde |
| RF-21 y RF-16 | Notificar equipo encendido fuera de horario (≤ 60 s) frente a apagarlo (≤ 2 min) | Consistente: avisa antes de actuar |
| RF-24 y RF-25 con RF-23 | Exportacion y rectificacion de datos personales, ambas con registro en bitacora | Consistente |

**Aritmetica de la medicion inicial.** 1 − (1 / 300) = **0,9967**, con un conflicto abierto.

**Correccion aplicada y nueva medicion.** El solapamiento se resolvio delimitando los dos
requisitos por causa —RF-13 por consumo sostenido sin actividad, RF-16 por fin de la ultima
franja asignada— con regla de precedencia a favor de RF-16 cuando ambas condiciones
concurran. Se tramito como **SC-01** y se aplico en el commit `6603e61`.

Se resolvio ademas una segunda incoherencia que no era un conflicto entre requisitos sino
entre fuentes: RF-20, RF-24 y RF-25 declaraban una prioridad MoSCoW en la ficha del ERS y
otra distinta en la tabla de priorizacion. Se tramito como **SC-04** y hoy las 25 fichas
coinciden con la tabla.

**Aritmetica tras la correccion.** 1 − (0 / 300) = **1,0000**

| Metrica | Antes (29/08) | Despues (31/08) | Referencia | Veredicto |
|---|---|---|---|---|
| Indice de consistencia | 0,9967 | **1,0000** | ≥ 0,98 | **Cumple** |
| Conflictos abiertos | 1 | **0** | 0 | **Cumple** |

---

## 4. Verificabilidad

**Formula.** Requisitos con criterio de aceptacion comprobable, dividido por el total.

Se aplico este criterio de clasificacion: un criterio es **comprobable** cuando define una
prueba cuyo resultado es un valor contrastable contra un umbral, o un hecho binario que se
observa sin juicio del evaluador. Un criterio que exige valorar una cualidad sin metrica
**no es comprobable**.

| Aritmetica | Resultado | Referencia | Veredicto |
|---|---|---|---|
| 25 / 25 | **100 %** | ≥ 90 % | **Cumple** |

De los 24 comprobables, 18 fijan un umbral numerico y 6 definen una prueba de resultado
binario, como que un ticket cambie de estado o que un rol no pueda acceder a una funcion
reservada.

**Hallazgo.** **RF-14** exigia que el sistema «genera recomendaciones diferenciadas y
**coherentes**». Diferenciadas es observable; **coherentes no lo era**: no habia metrica,
umbral ni procedimiento que permitiera a dos evaluadores independientes llegar al mismo
veredicto.

**Corregido el 2026-08-30.** El criterio se reescribio con una prueba objetiva: perfiles
de uso distintos verificados por una diferencia de al menos el 20 % en horas de ocupacion
mensual, recomendaciones que difieren en al menos un parametro accionable, y acuerdo del
100 % entre dos evaluadores independientes sobre si cada parametro se deriva de un dato de
su aula. Con esa correccion, los 25 requisitos funcionales tienen criterio comprobable.

---

## 5. Trazabilidad

**Formula.** Dos submetricas. Requisitos con fuente identificada sobre el total, y
requisitos con la cadena adelante completa sobre el total. La cadena adelante se considera
completa cuando el requisito enlaza a caso de uso, historia de usuario y criterio de
aceptacion.

| Submetrica | Aritmetica | Resultado | Referencia | Veredicto |
|---|---|---|---|---|
| Requisitos con fuente identificada | 23 / 25 | **92,0 %** | 100 % | **No cumple** |
| Requisitos con cadena adelante completa | 23 / 25 | **92,0 %** | ≥ 90 % | **Cumple** |

**Corregido el 2026-08-31.** La medicion del 29 de agosto daba 48,0 % en la cadena
adelante y contaba 308 celdas vacias. Al completar la matriz aparecio que el problema no
era solo de huecos:

- **Ocho identificadores de historia no resolvian.** La matriz declaraba `HU-24`, `HU-25`,
  `HU-07b`, `HU-07e`, `HU-10b`, `HU-12b`, `HU-12c` y `HU-12d`, que no existen en el ERS. Y
  numeraba las historias por el numero del requisito cuando el ERS las numera de forma
  correlativa. Se realinearon contra el ERS.
- **Ningun criterio de aceptacion resolvia.** El ERS no contenia **ni una sola mencion** de
  `CA-`: los escenarios Gherkin estaban sin etiquetar. Se etiquetaron los diecisiete
  existentes.
- **Faltaban tres historias.** RF-20, RF-24 y RF-25 no tenian ninguna. Se redactaron como
  HU-18, HU-19 y HU-20, con sus criterios CA-18, CA-19 y CA-20.
- **Faltaban las cuatro columnas** que exige la guia: clase, proceso, caso de prueba y
  estado de la traza. Anadidas; la matriz pasa de 13 a 18 columnas.
- **Cero celdas vacias.** Toda celda declara ahora si el eslabon existe o por que no
  aplica, porque una celda en blanco no distingue «no procede» de «falta por hacer».

**Lo que sigue sin cumplir, y no se fuerza.** La submetrica de fuente se queda en 92,0 %:
**RF-24 y RF-25 no proceden de campo**, sino del analisis normativo de los articulos 13 y
14 de la LOPDP. Inventarles una entrevista de origen seria falsear la traza. Se declaran
como derivados normativos en
[`04_Trazabilidad/huerfanos_y_cadenas_rotas.md`](../../04_Trazabilidad/huerfanos_y_cadenas_rotas.md),
con su causa y su accion, que es lo que la guia pide para los huerfanos.

Los dos requisitos que siguen sin cadena completa, **RF-09 y RF-18**, son de prioridad
Should: el ERS escribe una historia por requisito obligatorio, y estos no lo son.

---

## 6. Modificabilidad

**Formula.** Promedio de requisitos afectados por un cambio, sobre una muestra de al menos
cinco requisitos representativos con sus dependencias enumeradas una a una.

### 6.1 Lo que declara el documento

El recuento automatico sobre el atributo *Entradas / Salidas* encuentra **solo dos
dependencias declaradas** en toda la especificacion: RF-13 y RF-16 dependen ambos de
RF-03. El promedio resultante es de **0,08 requisitos afectados por cambio**.

Ese valor cumple la referencia de ≤ 3,0 con enorme holgura, y **precisamente por eso no es
creible**.

### 6.2 Lo que muestra el analisis manual

Enumerando a mano las dependencias reales de cinco requisitos representativos:

| Requisito | Dependencias reales enumeradas | Afectados |
|---|---|---|
| **RF-03** Deteccion de ocupacion | RF-13 y RF-16 la consumen para decidir el apagado; RF-20 registra su historial; RF-07 muestra su estado | 4 |
| **RF-07** Panel centralizado | Consume RF-01 (ambiental), RF-03 (ocupacion), RF-04 (proyector), RF-05 (climatizacion), RF-09 (riesgo) y RF-22 (conectividad) | 6 |
| **RF-08** Alertas por anomalia | Consume RF-01 y RF-22; alimenta a RF-10 (historial) y RF-11 (notificacion critica) | 4 |
| **RF-12** Solicitudes de mantenimiento | Consume RF-08 y RF-09; alimenta a RF-10 y RF-17 (reportes) | 4 |
| **RF-23** Bitacora de acciones | Registra las acciones de RF-02, RF-04, RF-05, RF-12, RF-18, RF-24 y RF-25 | 7 |

**Aritmetica.** (4 + 6 + 4 + 4 + 7) / 5 = **5,00**

| Metrica | Resultado | Referencia | Veredicto |
|---|---|---|---|
| Promedio de requisitos afectados por cambio | **5,00** | ≤ 3,0 | **No cumple** |

**Hallazgo.** La metrica automatica daba 0,08 y la manual da 5,00. La diferencia no es un
error de calculo: **es el defecto**. Las dependencias existen en el sistema pero no estan
escritas en la especificacion, de modo que el documento aparenta un acoplamiento bajo que
no tiene. Un requisito con dependencias no declaradas es un requisito cuyo cambio nadie
puede estimar.

Los dos nodos mas acoplados son **RF-07** y **RF-23**, y ambos por la misma razon: son
puntos de convergencia, uno de presentacion y otro de registro.

**Accion de mejora.** Declarar en el atributo *Entradas / Salidas* de cada ficha los
requisitos de los que depende y a los que alimenta, y despues volver a medir. Para bajar
de 3,0 conviene ademas desacoplar RF-23 introduciendo un evento de bitacora generico, de
modo que anadir una accion registrable no obligue a tocar el requisito de bitacora.

### 6.3 Medicion despues de declarar las dependencias

Las 25 fichas declaran ya de que requisitos dependen y a cuales alimentan. El grafo se
escribio en un solo sentido y el inverso se derivo, de modo que **ninguna dependencia puede
figurar en una ficha y faltar en la otra**. RF-19 no aparece como flujo de datos: condiciona
el acceso a toda operacion y esa relacion ya consta en la precondicion de cada ficha;
contarla dos veces inflaria la metrica sin describir nada nuevo.

El grafo resultante tiene **50 dependencias declaradas** entre 25 requisitos, y su simetria se comprueba de forma automatica.

| Requisito de la muestra | Afectados antes | Afectados ahora |
|---|---|---|
| RF-03 Deteccion de ocupacion | 4 | 6 |
| RF-07 Panel centralizado | 6 | 8 |
| RF-08 Alertas por anomalia | 4 | 5 |
| RF-12 Solicitudes de mantenimiento | 4 | 7 |
| RF-23 Bitacora de acciones | 7 | 10 |

| Medicion | Valor | Referencia | Veredicto |
|---|---|---|---|
| Sobre la misma muestra de cinco | **7,20** | ≤ 3,0 | **No cumple** |
| Sobre las 25 fichas | **4,00** | ≤ 3,0 | **No cumple** |
| Automatica sobre el atributo *Entradas / Salidas* | **4,00** | — | Coincide con la manual |

**La metrica empeora, y esa es la lectura correcta.** El valor automatico y el manual ya
coinciden, que era el objetivo de la accion: el documento dejo de aparentar un acoplamiento
que no tenia. Lo que antes daba 0,08 frente a 5,00 —la distancia entre lo declarado y lo
real— hoy es un unico numero comprobable.

Se publican **las dos mediciones** porque la muestra de la version 1.0 no era representativa:
se eligieron los cinco requisitos mas acoplados, que es el peor caso. Medir sobre las 25
fichas es una poblacion completa y no una seleccion, y por eso es la cifra que se propone
como oficial. Aun asi, **4,00 no cumple**.

**Por que no se fuerza el numero.** Bajar de 3,0 exige desacoplar de verdad, no declarar
menos: un evento de bitacora generico que libere a RF-23 de nombrar nueve requisitos, y una
vista de estado consolidado del aula que libere a RF-07 de nombrar ocho. Ambas medidas
llevarian la metrica a **2,80**, y ambas son cambios de diseno de la especificacion, no
correcciones de redaccion. Se tramitan como solicitud de cambio y no se improvisan al
cierre de la entrega. Los dos nodos que concentran el problema siguen siendo **RF-23** y
**RF-07**, por la misma razon que en la medicion inicial: son puntos de convergencia.

---

## 7. Correccion

> **Estado vigente, desde el 2026-09-05: medida, 0,04, Cumple.** Lo que sigue en esta seccion
> es la medicion inicial del 2026-08-29, cuando la inspeccion aun no se habia celebrado. Se
> conserva sin reescribir porque registra por que entonces no se declaro ningun valor. La
> inspeccion `INS-01` y la re-inspeccion `REINS-01` se celebraron despues y estan en
> `02_Evidencias/Validacion_Walkthrough/Inspeccion/`; el calculo esta en la seccion 8.

**Formula.** Defectos residuales tras la re-inspeccion, dividido por el numero de
requisitos.

| Metrica | Resultado | Referencia | Veredicto |
|---|---|---|---|
| Defectos residuales por requisito | **no medible todavia** | ≤ 0,05 | **Pendiente** |

**Por que no se mide.** La metrica se calcula sobre los defectos que sobreviven a una
re-inspeccion, y en este proyecto **la sesion de inspeccion formal aun no se ha
realizado**: no existen `02_Evidencias/Validacion/Inspeccion/` ni el registro de defectos
ni el de re-inspeccion.

No se declara un valor. La guia establece que una metrica sin sus conteos publicados se
considera no reportada, y **inventar un numero aqui seria evidencia fabricada**, que la
seccion 4 sanciona en S3 con el 100 % de descuento.

**Accion de mejora.** Ejecutar la sesion de inspeccion sobre el ERS v2.0 con roles y
tiempos registrados, levantar el registro de defectos con tipo y severidad, corregir, y
re-inspeccionar. Los tres defectos que esta auditoria ya identifico —RF-01 incompleto,
solapamiento RF-13/RF-16 y criterio no comprobable de RF-14— entran como entrada de esa
inspeccion.

---

## 8. Resumen

| Metrica | Antes (v1.0, 29/08) | Despues (v2.0, 31/08) | Referencia | Veredicto |
|---|---|---|---|---|
| Completitud | 96,0 % · 100 % · 100 % | **100 % · 100 % · 100 %** | ≥ 95 % y 100 % | **Cumple** |
| Consistencia | 0,9967 con 1 conflicto | **1,0000 con 0 conflictos** | ≥ 0,98 y cero conflictos | **Cumple** |
| Verificabilidad | 96,0 % | **100 %** | ≥ 90 % | **Cumple** |
| Trazabilidad | 92,0 % y 48,0 % | 92,0 % y **92,0 %** | 100 % y ≥ 90 % | **No cumple** |
| Modificabilidad | 5,00 declarado como 0,08 | **4,00**, declarada y comprobable | ≤ 3,0 | **No cumple** |
| Correccion | no medible | **0,04** (1 residual / 25 RF) | ≤ 0,05 | **Cumple** |

**Tres metricas pasan a cumplir**: consistencia cierra su unico conflicto, completitud sube
al 100 % al descartarse el falso positivo de RF-01, y verificabilidad al reescribirse el
criterio de RF-14.

**Dos siguen sin cumplir, y ninguna de las dos se maquilla.** Trazabilidad se queda en el
92 % de la submetrica de fuente porque dos requisitos —RF-24 y RF-25— derivan del analisis
normativo y no de evidencia de campo; inventarles una fuente seria peor que declararlo.
Modificabilidad queda en 4,00 medida sobre la poblacion completa, y la explicacion
es que el acoplamiento dejo de estar oculto: hoy el valor automatico y el manual coinciden.

**La sexta ya esta medida.** La re-inspeccion **REINS-01** se celebro el 2026-09-05 y
verifico los dieciseis defectos uno por uno: quince quedan cerrados y **uno residual**,
`DEF-06`, la apertura individual de camara, que el comite difiere de forma expresa en
`SC-03`. De ahi sale Correccion = 1 / 25 = **0,04**, por debajo del 0,05 de referencia.

El margen es de **un solo defecto**: con dos residuales el valor seria 0,08 y no cumpliria.
Se dice para que se lea con la prudencia que merece, no como una holgura que no existe.
→ `02_Evidencias/Validacion_Walkthrough/Inspeccion/2026-09-05_REINS-01_Registro_Reinspeccion.pdf`

La guia exige que **toda metrica por debajo de su valor de referencia se corrija en el
documento y se vuelva a medir**, y que el reporte muestre el par de valores antes y
despues. La tabla de arriba publica ese par para las seis metricas.

| Version | Fecha | Contenido |
|---|---|---|
| 1.0 | 2026-08-29 | Medicion inicial sobre el ERS/SRS v2.0, antes de correcciones |
| 2.0 | 2026-08-31 | Medicion posterior a las correcciones y a las decisiones de CCB-01. Recalculadas consistencia y modificabilidad; el resumen publica el par antes/despues |
| 3.0 | 2026-09-05 | Se cierra **Correccion** tras celebrarse INS-01 y REINS-01: 0,04 con un unico defecto residual. Es la ultima de las seis metricas que quedaba sin medir |
