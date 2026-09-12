# Huerfanos y cadenas rotas de la matriz de trazabilidad

**Proyecto SIGA - Equipo FGMMN - ISR-401 - Universidad Tecnica Estatal de Quevedo**
Generado el 2026-08-31 sobre `matriz_trazabilidad.csv`, y actualizado el 2026-09-03
al anadirse los ocho requisitos no funcionales del componente inteligente y, el 2026-09-06,
la restriccion `RD-01` y, el 2026-09-12, las historias `HU-22` a `HU-38`: **75 filas**
y 18 columnas. De ellas, **59 cierran la cadena de extremo a extremo** y las 75 tienen todos sus eslabones declarados.

La guia exige que los huerfanos y las cadenas rotas se listen **con su causa y su
accion**, no que no existan. Este documento los enumera uno a uno.

---

## 1. Estado de la traza, fila a fila

| Estado | Filas | Que significa |
|---|---|---|
| Completa | **53** | La fila enlaza fuente, caso de uso, clase, proceso, caso de prueba, historia y criterio |
| Huerfana | 9 | No procede de evidencia de campo: nace de analisis normativo o de decision tecnica |
| Parcial | **1** | Tiene fuente de campo, pero le falta algun eslabon hacia adelante |
| Restriccion de diseno | 12 | Restriccion RD: no se verifica por caso de prueba sino por revision de diseno |

**Cero celdas vacias.** Toda celda que antes estaba en blanco declara ahora si el
eslabon existe o por que no aplica.

## 1.1 Que significa aqui que una fila este cerrada

La rubrica pide una matriz **con las filas cerradas**. Conviene decir con precision que
cuenta como cerrada en esta matriz, porque hay dos lecturas y las dos cifras son publicas:

| Lectura | Cifra |
|---|---|
| Filas **sin ningun eslabon sin declarar** --- cada celda dice que enlace existe o por que no aplica | **75 de 75** |
| Filas con la cadena **completa**: fuente, caso de uso, clase, proceso, caso de prueba, historia y criterio | **59 de 75** --- 53 clasificadas «Completa» y 6 que la tienen entera pero son restricciones de diseno |
| Filas que **no cierran** | **16 de 75** --- 9 huerfanas, 1 parcial y 6 restricciones de diseno con algun eslabon que no aplica |

La diferencia no son filas a medio hacer: son filas que **no pueden** tener todos los
eslabones, y el motivo esta declarado fila a fila en los apartados que siguen.

- **Nueve huerfanas** no proceden de entrevista porque nacen del analisis normativo de la
  Ley Organica de Proteccion de Datos Personales o de decision tecnica. Inventarles una
  evidencia de campo seria fabricarla. Contando tambien las restricciones de diseno que
  nacen de la misma via, **catorce filas declaran «Sin evidencia de campo»** y tres mas
  declaran «No aplica».
- **Doce restricciones de diseno** no se verifican por caso de prueba sino por revision de
  diseno. Es lo que son. **La ERS define dieciocho, y seis no tienen fila en la matriz**:
  el motivo de cada una esta en el apartado 7.
- Varias filas **no las realiza ninguna pantalla**: «Evidencia fotografica del trabajo de
  campo», «Dependencia del horario academico vigente» o «Evidencia del sistema de camaras
  existente» son filas de evidencia y de restriccion, no requisitos que un mockup pueda
  realizar. Exigirles un mockup es un error de categoria, no un eslabon roto.
- **Dieciocho filas se cerraron el 2026-09-12** escribiendo diecisiete historias con su
  criterio de aceptacion, `HU-22` a `HU-38`, en el ERS (version 4.6). Tenian fuente --- de
  campo o un «No aplica» declarado ---, caso de uso y clase, y solo les faltaba la historia.
  El ERS escribia historias solo para los requisitos Must; desde la version 4.6 las escribe
  tambien para los Should, los no funcionales, los del componente inteligente y las
  restricciones de diseno **que tienen fuente**. A las que no la tienen no se les escribe:
  una historia atribuye una necesidad a alguien, y eso seria inventarlo.
- **`RD-02` no se cerro a proposito.** Su fila en la matriz dice «detectar ausencia de
  conectividad como riesgo critico», y la ficha de `RD-02` en el ERS dice que los dispositivos
  operaran solo dentro de la red institucional. Escribirle una historia fijaria esa
  contradiccion; primero hay que decidir cual de los dos textos es el correcto.
- **`RNF-15`** tiene fuente (`EV-20`) pero ninguna clase del diagrama la realiza, y asignarle
  una seria modelar por conveniencia.

**La metrica que mide lo que se puede exigir** es la del apartado 4: requisitos funcionales
con la cadena hacia adelante completa. Ahi la referencia es 90 % y el proyecto esta en 100 %.

El equipo prefiere declarar las dos cifras a elegir la que le favorece. La segunda es la
exigente, y es la que figura tambien en el README.

**La columna se comprueba por script.** Estaba escrita a mano, y una columna a mano sobre
setenta y cinco filas se desincroniza sin que nadie lo note: seis filas declaraban menos
eslabones de los que les faltaban y tres estaban marcadas como incompletas teniendolos todos.
Ahora se contrasta contra las celdas:

```bash
python 04_Trazabilidad/verificar_matriz.py
```

Avisa de cada discrepancia y no escribe nada salvo que se le pida con `--escribir`. La
familia «restriccion de diseno» se respeta tal como la declaro el equipo: que una fila lo sea
es un juicio sobre su naturaleza, no algo que se deduzca de las celdas.

## 2. Requisitos funcionales sin fuente de campo

Son requisitos reales del sistema, pero **no nacen de una entrevista**: proceden del
analisis normativo de la Ley Organica de Proteccion de Datos Personales. Se declaran
como derivados normativos y no se les inventa una evidencia que no tienen.

| Requisito | Causa | Accion |
|---|---|---|
| **RF-25** Rectificar los datos personales del usuario | Derivado normativo: Art. 14 | Mantener la trazabilidad a la ley; recoger evidencia de campo cuando un participante lo exprese |

`RF-24`, que figuraba aqui, tiene fuente de campo desde el 2026-09-04: `EV-21`.

## 3. Requisitos funcionales con la cadena incompleta

| Requisito | Eslabon que falta | Causa | Accion |
|---|---|---|---|
| Requisito | Estado |
|---|---|
| **RF-06**, **RF-09**, **RF-14**, **RF-17** y **RF-18** | **Cerrados el 2026-09-12** con `HU-22` a `HU-26` y sus criterios. Les faltaban la historia y el criterio porque eran Should |

Ningun requisito funcional queda hoy con la cadena hacia adelante incompleta.

## 4. Metricas resultantes

| Submetrica | Antes | Ahora | Referencia |
|---|---|---|---|
| Requisitos con fuente identificada | 23/25 = 92,0 % | **24/25 = 96,0 %** | 100 % |
| Requisitos con cadena adelante completa | 12/25 = 48,0 % | **25/25 = 100,0 %** | >= 90 % |
| Celdas vacias en la matriz | 308 | **0** | - |
| Columnas de la cadena | 13 | **18** | clase, proceso, caso de prueba y estado anadidos |

La submetrica de fuente **no llega al 100 %** y no se fuerza: el requisito de la
seccion 2 no procede de campo, y declararlo es lo correcto. La guia pide que los
huerfanos se listen con causa y accion, que es lo que hace este documento.

## 5. Enlaces que se corrigieron

Antes de completar la matriz habia un problema mas grave que las celdas vacias:
**identificadores declarados que no resolvian**.

| Identificador | Problema | Correccion |
|---|---|---|
| `HU-24`, `HU-25`, `HU-07b`, `HU-07e`, `HU-10b`, `HU-12b`, `HU-12c`, `HU-12d` | No existen en el ERS, que solo define HU-01 a HU-17 | Sustituidos por la historia real del requisito, leida del ERS |
| `CA-01` a `CA-25` | El ERS **no contenia ni una sola mencion** de `CA-`: los escenarios Gherkin estaban sin etiquetar | Se etiquetaron los 17 escenarios del ERS como `CA-01` a `CA-17`, y la matriz los referencia |
| Numeracion de historias | La matriz numeraba por requisito (`HU-16` para RF-16); el ERS numera de forma correlativa (`HU-13` para RF-16) | Realineadas contra el ERS, que es la fuente |
| Tres filas con una coma de mas | Rompian la lectura del CSV como tabla | Corregidas |

## 6. Inconsistencia detectada al completar la matriz, declarada y no resuelta

Al enlazar cada requisito con su historia aparecio una contradiccion entre dos artefactos
del propio repositorio:

| Requisito | Prioridad en la ficha del ERS | Prioridad en `priorizacion_moscow_kano.csv` |
|---|---|---|
| RF-20 Historial de ocupacion | Should | **Must** |
| RF-24 Exportacion de datos personales | Should | **Must** |
| RF-25 Rectificacion de datos personales | Should | **Must** |

Las dos fuentes no pueden tener razon a la vez. El equipo **no la resuelve por su cuenta**
en este documento, porque cambiar una prioridad es una decision de producto y no de
trazabilidad, y corresponde tramitarla como solicitud de cambio ante el comite.

Lo que si se hizo, porque no depende de esa decision: **escribir las tres historias de
usuario que faltaban**, HU-18, HU-19 y HU-20, con sus criterios CA-18, CA-19 y CA-20. La
cadena de trazabilidad queda completa con independencia de como se resuelva la prioridad.

Hay un argumento a favor de **Must** que conviene tener presente al decidirlo: RF-24 y
RF-25 no son funciones deseables sino **obligaciones legales** bajo los articulos 13 y 14
de la Ley Organica de Proteccion de Datos Personales. Una obligacion legal dificilmente es
opcional.

---

## 7. Las seis restricciones de diseno que no estan en la matriz

La ERS especifica **dieciocho** restricciones de diseno, `RD-01` a `RD-18`. La matriz y el
tablero de gestion recogen **doce**. Las otras seis no aparecen, y aqui se dice cuales son
y por que --- una ausencia que no se declara es indistinguible de un descuido.

| | Tipo | Por que no tiene fila |
|---|---|---|
| `RD-14` | Temporal | Fija que la Entrega 3 documentaria la ERS completa. Es un compromiso de calendario del proyecto, no una propiedad del sistema: no hay nada que construir ni que verificar en el producto |
| `RD-15` | Temporal | Igual, para la Entrega 4. Su cumplimiento se comprueba mirando este repositorio, no el sistema |
| `RD-16` | Alcance | Excluye del sistema la matricula, la asistencia y las calificaciones. Una exclusion de dominio no genera actividad: lo que declara es que no se hara nada |
| `RD-18` | Alcance | Excluye la red electrica del campus y los dispositivos sin integracion IoT. Mismo caso |
| `RD-07` | Economica | Ata la seleccion de hardware al presupuesto aprobado. Condiciona una compra, no una linea de codigo, y el proyecto no llego a la fase de adquisicion |
| `RD-12` | Operativa | La instalacion fisica depende del Departamento de Infraestructura. Obliga a un tercero, no al equipo |

Las dos temporales y las dos exclusiones de alcance **no pueden trazarse**: no hay actividad
posible para algo que por definicion no se hace. `RD-07` y `RD-12` vinculan a terceros y
tampoco generan trabajo del equipo.

### `RD-01`, que si faltaba, se anadio

Hasta el 2026-09-06 tambien faltaba `RD-01`, y esa ausencia **no tenia justificacion**: es
tecnologica igual que `RD-02` a `RD-06`, que si estaban las cinco, y condiciona el diseno
igual que ellas. Su efecto llegaba a la matriz solo de forma indirecta, a traves de `RF-01`,
`RF-02`, `RF-07` y `RF-22`.

Se cerro creando su actividad en Jira --- `SIGA-61` --- y anadiendo su fila a la matriz. Las
dos listas pasan de 60 a **61** y la sincronizacion sigue en el **100 %**. El export
`tablero_gestion/export_tablero_SIGA.csv` se regenero desde Jira, no se edito a mano: se
comprobo fila a fila contra el anterior y **`SIGA-61` es la unica diferencia**.

Queda dicho tambien que `RD-17` es de alcance como `RD-16` y `RD-18` y si tiene fila. La
diferencia esta en lo que excluyen: `RD-17` acota una responsabilidad dentro del dominio del
sistema --- no hacer mantenimiento fisico de los equipos que si gestiona --- mientras que
`RD-16` y `RD-18` sacan del alcance dominios enteros que el sistema no toca en absoluto.
