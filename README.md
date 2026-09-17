# SIGA — Sistema Inteligente de Gestion de Aulas

**Proyecto Fin de Curso — Entrega Final (2B)**
Ingenieria de Requerimientos (ISR-401) · 4.º nivel · Carrera de Software
Facultad de Ciencias de la Computacion · Universidad Tecnica Estatal de Quevedo (UTEQ)
Periodo Academico Ordinario 2026–2027

**URL del repositorio:** https://github.com/gleiston-guerrero/SIGA_FGMMN_ISR401_AVANCE_2B

---

## 1. El sistema

SIGA es un sistema de gestion inteligente de aulas universitarias basado en Internet de
las Cosas y aprendizaje automatico, especificado para la Facultad de Ciencias de la
Computacion de la UTEQ como organizacion cliente identificable.

Cubre seis capacidades: monitoreo ambiental en tiempo real de temperatura, humedad y
ocupacion; control remoto de proyectores y climatizacion; generacion automatica de
alertas ante condiciones anomalas; analisis predictivo de fallos de equipamiento;
gestion del ciclo de vida de solicitudes de mantenimiento; y reportes administrativos
exportables.

Los perfiles de usuario elicitados en campo son **docentes (DOC)**, **coordinacion
academica (COORD)** y **conserjeria e infraestructura (CONS)**. La especificacion se
rige por ISO/IEC/IEEE 29148:2018 y los requisitos no funcionales se cuantifican sobre
el modelo de calidad de ISO/IEC 25010:2023.

El componente empirico es un cuasi-experimento apareado que compara la calidad de los
Requisitos Funcionales elicitados por analistas humanos frente a los generados por un
Modelo Grande de Lenguaje a partir del mismo corpus de entrevistas anonimizadas,
evaluados a ciegas por tres jueces independientes en cinco dimensiones de calidad.

Ese es el **Enfoque 1** de la asignatura, y **no coincide con el que la rubrica asigna al
codigo de equipo bajo el que el docente registra este proyecto**. La desviacion, su causa y
la razon por la que no se revirtio estan declaradas en
[`06_Experimento/declaracion_enfoque.md`](06_Experimento/declaracion_enfoque.md).

---

## 2. Integrantes y roles

| Integrante | Rol | Correo institucional | ORCID |
|---|---|---|---|
| Sanchez Cornejo, Gary Alberto | Analista lider · componente empirico · integracion | gsanchezc6@uteq.edu.ec | [`0009-0009-9599-8806`](https://orcid.org/0009-0009-9599-8806) |
| Munoz Quinonez, Yeranick Esther | Documentacion, trazabilidad y gestion de evidencias | ymunozq@uteq.edu.ec | [`0009-0005-7711-8730`](https://orcid.org/0009-0005-7711-8730) |
| Cedeno Avila, Winston Damian | Transcripcion y anonimizacion del corpus de entrevistas | wcedenoa2@uteq.edu.ec | [`0009-0000-6086-6269`](https://orcid.org/0009-0000-6086-6269) |

> **Sobre la composicion.** El equipo activo son **tres integrantes**: los de la tabla. Cedeno
> Avila se reincorporo el 2026-09-02 para la ronda terminal de campo. Los otros dos nombres
> que figuran en el grupo `FGMMN` del SGA, **Mendoza Palma, Allan Jeremy** y **Gilces
> Carranza, Jose Ignacio**, estan **retirados del equipo**: no produjeron artefactos ni
> confirmaciones en este repositorio, no participan en la Entrega Final ni en el examen final
> y no se les atribuye ninguna parte del trabajo. Por eso no tienen commits, ni aporte
> individual, ni firma. Quien responde por que, y desde cuando, se declara en
> [`04_Trazabilidad/composicion_equipo.md`](04_Trazabilidad/composicion_equipo.md).

> **Sobre los ORCID.** El apartado 9.2 de la guia los exige. Los tres integrantes se
> registraron el 2026-09-03 y sus identificadores constan arriba, cada uno enlazado a su
> registro publico. Hasta esa fecha el repositorio declaraba el hueco en lugar de omitir la
> columna.

Docente responsable: Ing. Gleiston Guerrero Ulloa.

El aporte de cada integrante, con el identificador del commit que lo respalda, se
declara en [`04_Trazabilidad/aporte_individual.csv`](04_Trazabilidad/aporte_individual.csv).

### Entregas anteriores del proyecto

El historial de **este** repositorio comienza el 2026-08-30, cuando se reorganizo el arbol
para la Entrega Final. La trazabilidad acumulada del proyecto no vive aqui: se reparte entre
los repositorios de cada entrega, que se enlazan para que la cadena 1A a 2B pueda auditarse
sin depender de la memoria de nadie.

| Entrega | Repositorio |
|---|---|
| Entrega 3 (2A) --- Especificacion y modelado | <https://github.com/gleiston-guerrero/SIGA_FGMMN_ISR401_AVANCE_2A> |
| Entrega Final (2B) --- esta | <https://github.com/gleiston-guerrero/SIGA_FGMMN_ISR401_AVANCE_2B> |

Los artefactos de las entregas anteriores que siguen vigentes se incorporaron a este
repositorio y su evolucion consta en `CHANGELOG.md`. Los que quedaron superados permanecen
solo en el repositorio de su entrega.

> **Por que hay un repositorio nuevo.** La Entrega Final se rigio por una rubrica distinta
> de la que goberno la Entrega 2A, con otra estructura de carpetas y otro conjunto de
> entregables. El equipo abrio este repositorio el 2026-08-29 para que el arbol
> correspondiera exactamente a la estructura exigida, en lugar de reorganizar el anterior y
> arrastrar carpetas de una entrega ya evaluada. Por eso el historial de aqui empieza el
> 2026-08-30 aunque la evidencia de campo este fechada meses antes: el trabajo anterior
> consta en el repositorio de la 2A, enlazado arriba. El motivo, las fechas y lo que el
> equipo asume por esa decision estan en `CHANGELOG.md`, version `2B-1.7.0`.

---

## 3. Identificadores persistentes y como citar

| Que | Identificador |
|---|---|
| Paquete de datos en Zenodo | [`10.5281/zenodo.21774350`](https://doi.org/10.5281/zenodo.21774350) --- **DOI de concepto**, resuelve siempre a la version mas reciente |
| Version citada por el manuscrito | [`10.5281/zenodo.22663649`](https://doi.org/10.5281/zenodo.22663649) --- version `2B-1.12.0`, la que corresponde a este arbol |
| Registro previo del protocolo en OSF | [`10.17605/OSF.IO/7PQ3H`](https://doi.org/10.17605/OSF.IO/7PQ3H) |
| **Caratula de identificacion** | [`caratula_identificacion_SGA.pdf`](caratula_identificacion_SGA.pdf), con la URL del repositorio, el identificador del ultimo commit y la etiqueta de linea base. Se deposita aqui ademas de subirse al Sistema de Gestion Academica |
| **Linea base vigente** | Etiqueta anotada **`2B-final-v5.12`**, la **unica vigente**: la version entregada tras la evaluacion de la Entrega Final, la guia de cierre del 2026-09-14 y el informe del examen suspenso del 2026-09-16: tamanos del efecto con el requisito como unidad (desviacion 7) y con pares efectivos e interpretabilidad declarados, cadena de analisis ejecutandose dentro de `07_Datos` (tambien como `run_all.py`), de donde el reporte, el manuscrito y el ERS toman sus tablas y figuras, notas de campo y sesiones de elicitacion en la bitacora, observaciones del docente con su resolucion en el reporte, materiales de la defensa con los efectos vigentes, verificacion previa y aporte individual firmados, las cifras vigentes de trazabilidad en el reporte y la auditoria de calidad, la URL del nuevo propietario del repositorio, los kappa con su intervalo de confianza en las tablas y en el texto, la tabla que empareja cada fuente editable con su imagen la retrospectiva del cierre ([`10_Autoria/retrospectiva_equipo.md`](10_Autoria/retrospectiva_equipo.md)) y ningun kappa sin su intervalo en el texto. Esta sobre el ultimo commit de la rama `main`. **Quien revise este repositorio debe ir directamente a esa etiqueta** (`git checkout 2B-final-v5.12`). Sustituye a `2B-final-v5.11`. `2B-final`, `2B-final-v2.1`, `2B-final-v3.0`, `2B-final-v4.0` y `2B-final-v5.0` a `2B-final-v5.11` se conservan **solo como referencia historica** de lo que se califico o deposito en cada fecha; ninguna es linea base. La caratula nombra el commit anterior al que la deposita, porque un archivo no puede contener el identificador del commit que lo contiene |
| Desviaciones respecto del protocolo | `06_Experimento/registro_previo/bitacora_desviaciones.pdf` |
| Codigo archivado en Software Heritage | `swh:1:snp:861295fead33417e3efc2753fd4a34897014a891` |
| Autoevaluacion FAIR | [`fair_assessment.pdf`](fair_assessment.pdf) --- **22 de 26 indicadores, 84,62 %**, nivel *moderate*. Salida real de F-UJI 4.0.0; el volcado crudo esta en `fair_assessment.json` y el informe lo genera `generar_fair_assessment.py` |
| Manuscrito | `07_Publicacion/manuscrito_final.pdf` |
| Especificacion de requisitos | [`01_ERS/ERS_SRS_2B_v2.0.pdf`](01_ERS/ERS_SRS_2B_v2.0.pdf) --- 135 paginas en A4, regeneradas desde el `.tex` con el ciclo completo de `bibtex`: sin referencias sin resolver y **sin ningun desborde** horizontal ni vertical en el registro de compilacion |
| **Curva de saturacion tematica** | [`02_Evidencias/Codificacion_Tematica/curva_saturacion.png`](02_Evidencias/Codificacion_Tematica/curva_saturacion.png) · datos en `saturacion_por_entrevista.csv` · insertada en el manuscrito, Fig. 4 |
| **Calculo de potencia** | [`06_Experimento/resultados/power_calculation.csv`](06_Experimento/resultados/power_calculation.csv) · script `scripts_analisis/power_calculation.py` · tabla en el manuscrito, `tabla_power_calculation.tex` |

**Cita recomendada del paquete de datos:**

> Sanchez Cornejo, G. A., Munoz Quinonez, Y. E. y Cedeno Avila, W. D. (2026). *Conjunto de
> datos del proceso de Ingenieria de Requerimientos del proyecto SIGA*. Zenodo.
> https://doi.org/10.5281/zenodo.21774350

Los metadatos de citacion legibles por maquina estan en `CITATION.cff`, con los tres
identificadores anteriores.

## 4. Estructura del repositorio

Nombres ASCII, sin acentos, sin espacios, palabras separadas con guion bajo.
Los archivos multimedia siguen la convencion `AAAA-MM-DD_TipoParticipante_Codigo_Tecnica.ext`.

> **Sobre el tercer campo del nombre.** La convencion nombra ese campo
> `NombreApellido`. En este repositorio se sustituye por el **codigo de participante**
> (`DOC-nn`, `COORD-nn`, `CONS-nn`, `ENT-nn`) porque el protocolo de disociacion de
> datos personales exigido por la seccion 5.10 y por la Ley Organica de Proteccion de
> Datos Personales prohibe publicar nombres propios en la evidencia. La correspondencia
> codigo–participante existe unicamente en el registro de custodia que se entrega al
> docente por el sistema de gestion academica. Sustitucion declarada en
> [`07_Publicacion/dataset_zenodo/anonimizacion.md`](07_Publicacion/dataset_zenodo/anonimizacion.md).

```
SIGA_FGMMN_ISR401_AVANCE_2B/
├── README.md                     Este archivo
├── LICENSE                       Apache-2.0 (codigo) + CC BY 4.0 (datos y documentos)
├── CITATION.cff                  Metadatos de citacion
├── CHANGELOG.md                  Historial de versiones
├── checksums.sha256              Sumas SHA-256 de la evidencia binaria y de datos
├── reporte.tex                   Documento entregado (se compila a reporte.pdf)
├── referencias.bib               Bibliografia del reporte, formato IEEE
├── 01_ERS/                       Especificacion de Requisitos de Software
│   ├── ERS_SRS_2B_v2.0.tex       Documento maestro
│   ├── secciones_generadas.tex   Cuerpo de la especificacion
│   ├── referencias.bib
│   ├── Auditoria_Calidad/        Las seis metricas de la seccion 5.6, con conteos base
│   └── Componentes_IA/           Fichas de los componentes de aprendizaje automatico
│
├── 02_Evidencias/                Evidencia primaria de campo
│   ├── Consentimientos/          Consentimientos informados firmados
│   ├── Video/                    Entrevistas en video
│   ├── Audio/                    Entrevistas en audio, redundantes con el video
│   ├── Transcripciones/          Una por entrevista, con marca de tiempo
│   ├── Guiones_Entrevista/       Version final aplicada, con historial de cambios
│   ├── Cuestionario/
│   │   ├── Respuestas/           Exportacion directa con marca temporal
│   │   └── Fotos_Aplicacion/     Evidencia fotografica de la aplicacion
│   ├── Fotos_Entorno/            Fotografias del sitio del cliente
│   ├── Documentos_Organizacion/  Documentos originales de la organizacion
│   ├── Codificacion_Tematica/    Tabla de codificacion con cobertura declarada
│   └── Validacion/
│       └── Sesiones_Validacion/  Sesiones con partes interesadas: video mas acta
│
├── 03_Modelado/                  Cada diagrama con su archivo fuente nativo
│   ├── 01_Contexto/              Contexto y frontera del sistema
│   ├── 02_iStar_SD/              Dependencias estrategicas
│   ├── 03_iStar_SR/              Razones estrategicas
│   ├── 04_Casos_Uso/             Diagrama general de casos de uso
│   ├── 05_Clases/                Diagrama de clases refinado
│   ├── 06_Secuencia/             Uno por caso de uso obligatorio
│   ├── 07_Actividad/             Uno por flujo principal
│   ├── 08_Estados/               Uno por entidad con ciclo de vida no trivial
│   ├── 10_Componentes/           Diagrama de componentes
│   ├── 11_Despliegue/            Diagrama de despliegue
│   └── 12_Prototipos_Interfaz/   Uno por pantalla obligatoria
│
├── 04_Trazabilidad/              Matriz, priorizacion MoSCoW/Kano y aporte individual
├── 05_MVP/
│   ├── codigo_fuente/            Codigo organizado por modulos
│   ├── despliegue/               Instrucciones reproducibles desde cero
│   └── demostracion/             Video del recorrido funcional
│
├── 06_Experimento/               Componente empirico y paquete de replicacion
│   ├── Makefile                  Pipeline completo con una sola orden
│   ├── replicar.py               El mismo pipeline sin depender de make
│   ├── protocolo/                Preguntas, hipotesis, variables y plan de analisis
│   ├── registro_previo/          Comprobante OSF y bitacora de desviaciones
│   ├── declaracion_enfoque.md    Por que se ejecuto el Enfoque 1 y no el 3
│   ├── clave_desciego_UBICACION.md  Donde esta la tabla de desciego, retirada del
│   │                             repositorio el 2026-09-03, y quien la custodia
│   ├── instrumentos/             Guiones, cuestionarios y rubricas en version final
│   ├── prompts_llm/              Consignas literales usadas con el modelo de lenguaje
│   ├── datos_crudos/             Formato abierto, sin edicion manual posterior
│   ├── datos_procesados/         Generados exclusivamente por script
│   ├── scripts_analisis/         Analisis reproducible, con una sola orden
│   ├── resultados/               Salidas estadisticas del analisis de tres jueces
│   └── panel_ampliado/           Las dos vueltas del panel de siete, que no se pudo
│                                 usar, con sus datos crudos y su diagnostico
│
├── 07_Publicacion/               Manuscrito y deposito de datos
│   ├── manuscrito_final.tex      Manuscrito en plantilla Springer LNCS
│   ├── manuscrito_final.pdf      Compilado, 15 paginas
│   ├── referencias.bib           40 entradas, 35 con DOI verificado
│   ├── analisis_revistas.md      Eleccion de la conferencia objetivo
│   ├── figuras/  tablas/         Producidas por los scripts, no a mano
│   └── dataset_zenodo/           Paquete depositado en Zenodo con DOI
│
├── 07_Datos/                     Paquete de datos: una sola orden desde los datos crudos
│   ├── datos_crudos/  datos_procesados/
│   ├── resultados/               Acuerdo con IC, y las tablas/, figuras/ y estadisticos/
│   │                             que el reporte y el manuscrito incluyen desde aqui
│   ├── scripts/                  Orquestador ejecutar.py, sus cinco etapas y analisis/,
│   │                             la cadena que genera las tablas y figuras del documento
│   └── diccionario_datos.csv · README_datos.md · LICENSE-DATA.txt ·
│       checksums_datos.sha256 · desviaciones.md · registro_deposito.md
│
├── 08_Defensa/                   Presentacion, libreto, defensa grabada y banco de preguntas
│
└── 10_Autoria/                   Evidencia de autoria, elementos A1 a A12
```

La zona restringida cifrada esta en `02_Evidencias/00_Restringido/`, y su contenido y
custodia se describen en su `README_Restringido.md`.

La estructura sigue el arbol obligatorio de la seccion 9.1 de la guia. Las evidencias
de etica quedan en `02_Evidencias/Etica/`, junto al resto de la evidencia primaria, y el
resumen del proceso etico del paquete publicado esta en
`07_Publicacion/dataset_zenodo/ETHICS.md`.

---

### Elementos aun no depositados

Se declaran aqui, y no en el arbol de arriba, para que **nada de lo que este repositorio
nombra deje de existir**.

| Elemento | Estado |
|---|---|
| Autorizacion del cambio de composicion del equipo | La solicitud esta firmada por los tres y depositada en `04_Trazabilidad/`; **resolverla corresponde al docente** |

**Lo que estuvo en esta tabla y ya no.** Se retira lo que se cumplio, con la fecha, porque
una tabla de ausencias que no se actualiza acaba declarando huecos que no existen ---
justo lo contrario de lo que persigue:

| Elemento | Se cerro |
|---|---|
| Regrabacion de la defensa a tres voces | 2026-09-09. `08_Defensa/2026-09-09_Defensa_Grabada.mp4`, 24 min 49 s |
| Tercera sesion de validacion con usuario tecnico | 2026-09-07. `WT-08`, `WT-09` y `WT-10` estan depositadas |
| `02_Evidencias/Cuestionario/Instrumento/` | 2026-09-07. El formulario seguia publicado y se exporto de ahi; sus 30 preguntas coinciden una a una con las columnas del export de respuestas |
| `02_Evidencias/Notas_Campo/` | 2026-09-05. Las **doce** notas estan firmadas y depositadas: seis manuscritas de la ronda terminal y seis de observacion de entorno |
| `02_Evidencias/Validacion_Walkthrough/Inspeccion/` | 2026-09-05. La inspeccion `INS-01` y la re-inspeccion `REINS-01` se celebraron y estan firmadas |
| `02_Evidencias/Validacion_Walkthrough/Solicitudes_Cambio/` | 2026-09-05. El comite `CCB-01` se reunio; cuatro solicitudes, tres aprobadas y una diferida |
| `03_Modelado/09_DFD/` | 2026-09-04. Los diagramas de nivel 0 y 1 estan depositados con su fuente `.drawio` |
| `03_Modelado/12_Prototipos_Interfaz/` | 2026-09-06. El archivo de Figma se deposito y las doce carpetas de `03_Modelado/` tienen fuente nativa |

---

## 5. Compilacion del documento entregado

Compilador: **pdfLaTeX** con **BibTeX**, distribucion TeX Live 2024 o MiKTeX 24.
Paquetes requeridos, tal como los carga cada documento:

- `reporte.tex`: `inputenc`, `fontenc`, `babel`, `geometry`, `graphicx`, `float`, `longtable`,
  `booktabs`, `amsmath`, `amssymb`, `xcolor`, `enumitem`, `fancyhdr`, `lastpage`, `hyperref` y
  `csquotes`.
- `01_ERS/ERS_SRS_2B_v2.0.tex`: `inputenc`, `babel`, `geometry`, `graphicx`, `float`,
  `longtable`, `array`, `booktabs`, `amssymb`, `xcolor`, `hyperref`, `enumitem`, `fancyhdr`,
  `titlesec` y `lastpage`.

Archivo principal: `reporte.tex`. Orden exacto de comandos, desde la raiz de un clon
limpio:

```bash
pdflatex  -interaction=nonstopmode reporte.tex
bibtex    reporte
pdflatex  -interaction=nonstopmode reporte.tex
pdflatex  -interaction=nonstopmode reporte.tex
```

El resultado es `reporte.pdf`, identico en contenido al documento entregado.

La Especificacion de Requisitos se compila por separado, con la misma secuencia:

```bash
cd 01_ERS
pdflatex  -interaction=nonstopmode ERS_SRS_2B_v2.0.tex
bibtex    ERS_SRS_2B_v2.0
pdflatex  -interaction=nonstopmode ERS_SRS_2B_v2.0.tex
pdflatex  -interaction=nonstopmode ERS_SRS_2B_v2.0.tex
```

---

## 6. Reproduccion del analisis

### Dependencias

- Python >= 3.11
- Las seis dependencias del analisis, **con version fijada**, en
  [`06_Experimento/requirements.txt`](06_Experimento/requirements.txt)
- `sha256sum` (en Windows, disponible con Git Bash)
- GNU Make es **opcional**: `replicar.py` ejecuta el mismo pipeline sin el

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r 06_Experimento/requirements.txt
```

Las versiones estan fijadas a proposito: son las que generaron las tablas y figuras
depositadas, y proceden de `06_Experimento/resultados/entorno_python.txt`, el volcado
completo del entorno. **Los scripts de verificacion del repositorio ---`04_Trazabilidad/`,
`02_Evidencias/Codificacion_Tematica/` y `10_Autoria/`--- no necesitan ninguna de las seis**:
usan solo la biblioteca estandar, de modo que la cadena de comprobacion corre en un clon
limpio sin instalar nada.

### Ejecucion completa

Una sola orden, partiendo unicamente de los datos crudos, que reconstruye el paquete de
datos y **ejecuta dentro de el la cadena de analisis que genera todas las tablas y figuras
del documento**, con los scripts de `07_Datos/scripts/analisis/`. Las escribe en
`07_Datos/resultados/tablas/`, `07_Datos/resultados/figuras/` y
`07_Datos/resultados/estadisticos/`, que es de donde **el reporte y el manuscrito las
incluyen al compilarse**, y comprueba que salen identicas byte a byte al manifiesto:

```bash
python 07_Datos/scripts/ejecutar.py
```

La misma cadena, con copias identicas de los scripts, sigue disponible en el componente
empirico, que conserva sus salidas en `06_Experimento/resultados/` y `07_Publicacion/`. La
etapa `integridad` del paquete comprueba que scripts y salidas coinciden byte a byte en los
dos sitios. Se lanza por cualquiera de estas dos rutas equivalentes:

```bash
python 06_Experimento/replicar.py
```

```bash
cd 06_Experimento && make all
```

El pipeline consolida las hojas de puntuacion de los tres jueces, calcula el acuerdo
inter-evaluador (kappa de Cohen ponderado por par y kappa de Fleiss), ejecuta las
pruebas de supuestos (Shapiro-Wilk y Levene), aplica la prueba de hipotesis por
dimension con correccion de Holm-Bonferroni, calcula el tamano del efecto con el requisito
como unidad (25 frente a 26, desviacion 7) e intervalo de confianza al 95 % por bootstrap
de 10 000 replicas con semilla `20260802`, genera la
curva de saturacion tematica y el calculo de potencia, y escribe todas las tablas y
todas las figuras del reporte en `tablas/` y `figuras/`.

Ninguna cifra del reporte se escribe a mano. Cada tabla y cada figura se regenera con
esa orden; la correspondencia entre cada salida y el script que la produce esta en
[`07_Publicacion/dataset_zenodo/correspondencia_salidas.csv`](07_Publicacion/dataset_zenodo/correspondencia_salidas.csv).

### De la afirmacion al numero

Ese archivo responde «de donde sale esta salida». La pregunta contraria --- **«usted afirma
esto, donde esta el numero»** --- la responde:

```bash
python 07_Publicacion/verificar_afirmaciones.py
```

Recorre las quince afirmaciones con cifra que hacen el manuscrito, el reporte, las
diapositivas y el libreto de la defensa; **recalcula cada una desde su salida** y avisa si
alguna dejo de coincidir, nombrando los documentos que habria que corregir. Escribe
[`07_Publicacion/correspondencia_afirmacion_resultado.csv`](07_Publicacion/correspondencia_afirmacion_resultado.csv)
y termina con codigo distinto de cero si algo no cuadra, de modo que sirve en una
comprobacion automatica.

Cubre un fallo que ninguna otra verificacion del repositorio detecta: que una cifra escrita
en prosa se quede atras cuando el analisis se vuelve a correr. El manifiesto de sumas dice
que los archivos no cambiaron y el comprobador de enlaces dice que las rutas existen;
ninguno de los dos mira si el 0,338 del manuscrito sigue siendo el de
`acuerdo_interevaluador.csv`.

### Verificacion de integridad

```bash
sha256sum -c checksums.sha256
```

Debe terminar sin un solo error sobre un clon limpio.

Sin `sha256sum`, y anadiendo el sondeo de codec y duracion del material audiovisual:

```bash
python 06_Experimento/replicar.py --verificar
```

---

## 7. Cierre de campo en dieciseis entrevistas

El corpus son **N = 16 entrevistas validas**. El levantamiento se habia cerrado en diez el
2026-08-17, por autorizacion verbal del docente ante la restriccion de calendario; esa
decision y sus limites estan documentados en
[`02_Evidencias/Etica/declaracion_reduccion_muestra.md`](02_Evidencias/Etica/declaracion_reduccion_muestra.md).
La **ronda terminal del 2026-09-03** anadio seis entrevistas a docentes (`EV-20` a `EV-25`)
y llevo el corpus al minimo terminal aplicable, con lo que aquella reduccion queda superada.
El documento de etica se conserva sin reescribir, con una nota de estado al inicio: registra
lo que ocurrio y cuando, que es justamente lo que lo hace util.

**Las dieciseis estan transcritas y codificadas.** Las seis de la ronda terminal se
codificaron el 2026-09-06, repartidas entre los tres integrantes por entrevista completa: 136
fragmentos bajo 50 codigos. Las grabaciones de esas seis no se publican, por lo que dice su
consentimiento: su ficha tecnica y su ubicacion constan en
[`02_Evidencias/00_Restringido/`](02_Evidencias/00_Restringido/).

Un tamano menor al de referencia se sostiene con el calculo que lo justifica, conforme
a la seccion 6 de la guia. Ese calculo esta en
[`06_Experimento/resultados/power_calculation.csv`](06_Experimento/resultados/power_calculation.csv):
para detectar un efecto d = 0,50 con alfa = 0,05 y potencia 0,80 se requieren 34
unidades; con las disponibles la potencia alcanzada es del 8,4 %. La consecuencia sobre
la interpretacion de los resultados se declara en la seccion de amenazas a la validez
del reporte.

La curva de saturacion tematica **alcanza inflexion en `EV-23`**, la decimocuarta: a partir
de ahi el promedio de codigos nuevos de las tres ultimas entrevistas queda por debajo del 5 %
de los acumulados. Cierra en **1,333 frente a un umbral de 2,500**, sobre 50 codigos
([`tablas/saturacion_por_entrevista.csv`](07_Publicacion/tablas/saturacion_por_entrevista.csv)).

Como el resultado cambio justo cuando convenia, se probaron **las 720 ordenaciones posibles**
del bloque de seis entrevistas del mismo dia: satura en las 720, y el peor caso --- 2,333 ---
sigue por debajo del umbral. Se reproduce con
`python 02_Evidencias/Codificacion_Tematica/robustez_saturacion.py`. Las tres reservas que
matizan el resultado, incluida una que va en contra, estan en
[`00_LEEME_SATURACION.md`](02_Evidencias/Codificacion_Tematica/00_LEEME_SATURACION.md).

Una entrevista adicional (EV-15, participante DOC-03) fue excluida por retiro del
consentimiento informado del participante, y su material fue suprimido conforme a la
politica de conservacion y supresion declarada en `02_Evidencias/Etica/`.

---

## 8. Licenciamiento

| Alcance | Licencia |
|---|---|
| Codigo del prototipo y scripts de analisis | Apache-2.0 |
| Datos, documentos, figuras, transcripciones y reporte | CC BY 4.0 |

El alcance exacto de cada una se declara en [`LICENSE`](LICENSE).

---

## 9. Declaracion de uso de inteligencia artificial

La declaracion obligatoria, seccion por seccion, con herramienta empleada, tipo de
asistencia y metodo concreto de validacion aplicado, esta en
[`10_Autoria/declaracion_uso_ia.md`](10_Autoria/declaracion_uso_ia.md).

Los modelos de lenguaje intervienen en este trabajo en dos capacidades separadas: como
**objeto de estudio**, generando el Conjunto A de Requisitos Funcionales bajo condiciones
registradas en [`06_Experimento/prompts_llm/`](06_Experimento/prompts_llm/); y como
**asistencia en la elaboracion del entregable** —redaccion, scripts de verificacion,
organizacion del repositorio y operaciones de Git—, inventariada en esa declaracion. Las
secciones evaluativas —analisis, discusion, conclusiones y justificacion de decisiones de
ingenieria— son produccion propia verificada contra la evidencia primaria; las amenazas a
la validez del manuscrito se redactaron con asistencia y asi constan.

---

## 10. Estado de la entrega

El inventario de lo que existe y de lo que falta, contrastado item por item contra los
minimos de la seccion 5 de la guia, se lleva en el control de trabajo del equipo, **fuera
de este repositorio**, para que ninguna nota de proceso se cuele en la entrega.

---

<sub>Universidad Tecnica Estatal de Quevedo · Facultad de Ciencias de la Computacion ·
Ingenieria de Requerimientos ISR-401 · Equipo FGMMN · 2026</sub>
