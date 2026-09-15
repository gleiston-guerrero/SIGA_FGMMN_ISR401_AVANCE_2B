# Lista de verificacion previa

**Proyecto SIGA · Equipo FGMMN · ISR-401 · Universidad Tecnica Estatal de Quevedo**

Seccion 11 de la guia de desarrollo del 2026-09-02. Las doce comprobaciones se
**ejecutaron**, no se marcaron a mano: el detalle de cada una es la salida real de
`10_Autoria/verificacion_previa.py`.

| | |
|---|---|
| Comprobado sobre | un clon limpio del remoto |
| Version | `12ffaa6` |

---

## Resultado

| N.º | Comprobacion | Cumple | Detalle |
|---|---|---|---|
| 1 | Se clono en carpeta limpia y se compilo el documento principal desde el .tex siguiendo unicamente el README | **Si** | Compilado sobre el clon con pdfLaTeX + BibTeX, sin errores |
| 2 | El PDF resultante coincide con el entregado y no presenta referencias sin resolver | **Si** | 28 paginas regeneradas, 0 referencias sin resolver. La comparacion es por contenido y no por suma: pdfLaTeX incrusta la fecha de compilacion, de modo que dos PDF del mismo fuente nunca son byte a byte iguales |
| 3 | No existe ningun archivo de cero o un byte cuyo nombre anuncie contenido de evidencia | **Si** | Cero archivos de 0 o 1 byte en todo el arbol |
| 4 | La comprobacion de sumas termina sin error sobre el clon limpio | **Si** | 1009 de 1009 sumas correctas |
| 5 | Todos los autores del historial son integrantes declarados con correo institucional | **Si** | 3 autor(es): gsanchezc6@uteq.edu.ec, wcedenoa2@uteq.edu.ec, ymunozq@uteq.edu.ec |
| 6 | Existe etiqueta anotada de linea base, publicada y alcanzable desde la rama por defecto | **Si** | 13 etiqueta(s) anotada(s) y alcanzable(s) desde main: 2B-final, 2B-final-v2.1, 2B-final-v3.0, 2B-final-v4.0, 2B-final-v5.0, 2B-final-v5.1, 2B-final-v5.2, 2B-final-v5.3, 2B-final-v5.4, 2B-final-v5.5, 2B-final-v5.6, 2B-final-v5.7, 2B-final-v5.8 |
| 7 | La carpeta 07_Datos existe y la orden unica de analisis se ejecuta sin error | **Si** | python 07_Datos/scripts/ejecutar.py termino con codigo 0 |
| 8 | La carpeta 10_Autoria contiene los elementos A1 a A12 | **Si** | Los doce elementos existen y tienen contenido |
| 9 | Todo numero que aparece en los documentos procede de la salida de un script | Manual | La correspondencia salida-script esta declarada en 07_Publicacion/dataset_zenodo/correspondencia_salidas.csv. Requiere revision humana |
| 10 | Ningun dato personal aparece en la zona publica del repositorio | **Si** | Ninguna cedula ajena al equipo fuera de la zona restringida, incluida la capa de texto de los PDF. Las 20 apariciones detectadas son las de los propios integrantes, declaradas por ellos en la caratula y en la composicion del equipo, no datos de participantes |
| 11 | Cada requisito del componente inteligente tiene metrica, unidad, umbral y metodo de verificacion | **Si** | 8 requisitos, todos con los seis atributos |
| 12 | La URL declarada en la caratula abre el repositorio desde una sesion sin autenticar | Manual | Comprobar en una ventana privada del navegador: https://github.com/gleiston-guerrero/SIGA_FGMMN_ISR401_AVANCE_2B.git |

---

## Criterio de piso P4: ningun agente automatizado firma el historial

Comprobado linea a linea sobre el cuerpo de todos los mensajes de commit:
**ningun** trailer `Co-Authored-By`, ninguna linea `Generated with` y ningun
`Signed-off-by` ajeno al autor. Todos los autores del historial son integrantes del
equipo con su correo institucional.

**Committer distinto de un integrante** --- el autor si lo es: `d0a3138`, aplicado por GitHub <noreply@github.com> con autor wcedenoa2@uteq.edu.ec. Es la firma
con la que GitHub registra un commit hecho desde su interfaz web, explicada en
`04_Trazabilidad/composicion_equipo.md`.

Que parte de las operaciones de Git las ejecuto un asistente de inteligencia
artificial, con la identidad del integrante al que se atribuia cada cambio, se
declara en `10_Autoria/declaracion_uso_ia.md`.

---

## Lo que esta lista no decide

Tres comprobaciones quedan marcadas como **manual** a proposito.

La numero 9 --- que todo numero de los documentos proceda de un script --- exige leer
los documentos y contrastarlos con la correspondencia declarada. Una maquina puede
comprobar que la correspondencia existe, no que sea cierta.

La numero 12 exige abrir la URL sin sesion iniciada, y este script no puede saber si
quien lo ejecuta tiene credenciales guardadas.

La numero 10 se ejecuta, pero su resultado es un indicio: busca secuencias de diez
digitos fuera de la zona restringida. Que no encuentre ninguna no prueba que no haya
datos personales de otra forma.

---

## Sobre la version que se verifica

La version que consta arriba es la del commit **anterior** al que deposita este
documento firmado. No puede ser otra: cuando se imprime y se firma, el commit que
lo deposita todavia no existe, y su identificador tampoco. **La diferencia es
siempre de una sola confirmacion**, y esa confirmacion es la del propio deposito.

Es la misma regla que declara `aporte_individual.md` para el recuento por autor, y
por el mismo motivo. La guia pide la lista firmada *antes de dar por cerrada la
entrega*; el identificador lo anade este script por rigor propio, no porque se
exija.

Cualquiera puede rehacer la comprobacion sobre la version entregada:

```bash
python 10_Autoria/verificacion_previa.py --clonar
```


---

## Reparto de la verificacion

La guia exige que quien comprueba sea **una persona distinta de quien produjo cada
artefacto**. El reparto **lo calcula este script desde el historial, archivo por
archivo**: cada archivo lo verifica alguien que no tiene ninguna confirmacion sobre
el. Se comprueba con `git log --format=%ae -- <archivo>`.

| Firmante | Verifica | Archivos |
|---|---|---|
| Cedeno Avila, Winston Damian | Todos los archivos sin ninguna confirmacion suya | 970 |
| Munoz Quinonez, Yeranick Esther | Los que tienen confirmaciones de Cedeno Avila y ninguna suya | 30 |
| Sanchez Cornejo, Gary Alberto | Los que tienen confirmaciones de los otros dos y ninguna suya | 2 |

**Archivos de la segunda firma:** `02_Evidencias/Codificacion_Tematica/incorporar_codificacion.py`, `02_Evidencias/Transcripciones/2026-09-03_Docente_DOC-05_EV-20_Transcripcion.md`, `02_Evidencias/Transcripciones/2026-09-03_Docente_DOC-06_EV-21_Transcripcion.md`, `02_Evidencias/Transcripciones/2026-09-03_Docente_DOC-07_EV-22_Transcripcion.md`, `02_Evidencias/Transcripciones/2026-09-03_Docente_DOC-08_EV-23_Transcripcion.md`, `02_Evidencias/Transcripciones/2026-09-03_Docente_DOC-09_EV-24_Transcripcion.md`, `02_Evidencias/Transcripciones/2026-09-03_Docente_DOC-10_EV-25_Transcripcion.md`, `02_Evidencias/Transcripciones/2026-09-04_Tecnico_TIC-01_EV-26_Transcripcion.md`, `02_Evidencias/Transcripciones/2026-09-05_Tecnico_TIC-02_EV-27_Transcripcion.md`, `02_Evidencias/Transcripciones/2026-09-07_Tecnico_TIC-03_EV-28_Transcripcion.md`, `02_Evidencias/Transcripciones/control_calidad/00_LEEME.md`, `02_Evidencias/Transcripciones/control_calidad/DOC-05_transcripcion_wcedenoa2.md`, `02_Evidencias/Transcripciones/control_calidad/DOC-05_transcripcion_ymunozq.md`, `02_Evidencias/Transcripciones/control_calidad/DOC-06_transcripcion_wcedenoa2.md`, `02_Evidencias/Transcripciones/control_calidad/DOC-06_transcripcion_ymunozq.md`, `02_Evidencias/Transcripciones/control_calidad/comparacion_transcripciones.csv`, `02_Evidencias/Validacion_Walkthrough/Inspeccion/2026-09-05_INS-01_Registro_Inspeccion.pdf`, `02_Evidencias/Validacion_Walkthrough/Inspeccion/2026-09-05_REINS-01_Registro_Reinspeccion.pdf`, `02_Evidencias/Validacion_Walkthrough/Inspeccion/registro_defectos.csv`, `02_Evidencias/Validacion_Walkthrough/Solicitudes_Cambio/2026-08-31_CCB-01_Acta_Comite.pdf`, `02_Evidencias/Validacion_Walkthrough/Solicitudes_Cambio/SC-01_Delimitar_RF-13_RF-16.pdf`, `02_Evidencias/Validacion_Walkthrough/Solicitudes_Cambio/SC-02_Plazos_y_estados_del_ticket.pdf`, `02_Evidencias/Validacion_Walkthrough/Solicitudes_Cambio/SC-03_Apertura_individual_de_camara.pdf`, `02_Evidencias/Validacion_Walkthrough/Solicitudes_Cambio/SC-04_Prioridad_MoSCoW_RF-20_RF-24_RF-25.pdf`, `04_Trazabilidad/2026-09-05_Retrospectiva_Equipo.pdf`, `08_Defensa/2026-09-09_Defensa_Grabada.mp4`, `10_Autoria/capturas/2026-09-04_WinstonCD_control_calidad_transcripciones.png`, `10_Autoria/capturas/2026-09-04_WinstonCD_transcripcion_EV-21.png`, `10_Autoria/capturas/2026-09-04_gsanchezc6-beep_paquete_datos_formato_largo.png`, `10_Autoria/capturas/2026-09-04_gsanchezc6-beep_paquete_datos_integridad.png`.

**Archivos de la tercera firma:** `02_Evidencias/Validacion_Walkthrough/Inspeccion/00_LEEME.md`, `02_Evidencias/Validacion_Walkthrough/Solicitudes_Cambio/00_LEEME.md`.

**Sin verificador distinto de su autor:** `01_ERS/Auditoria_Calidad/auditoria_calidad_especificacion.md`, `02_Evidencias/Codificacion_Tematica/codificacion_tematica.csv`, `08_Defensa/README.md`. Tienen confirmaciones de los tres
integrantes, de modo que ninguno puede verificarlos sin comprobar trabajo propio; se
declaran en lugar de asignarlos. Quedan fuera del reparto los manifiestos de sumas, que
regenera un script, y los tres archivos de esta verificacion, que no puede verificarse a
si misma.

## Firmas

Cada firmante declara haber revisado el resultado de arriba y las comprobaciones
marcadas como manuales, sobre los archivos que el reparto le asigna.

**Cedeno Avila, Winston Damian** --- wcedenoa2@uteq.edu.ec

Firma: ______________________________    Fecha: ______________

**Munoz Quinonez, Yeranick Esther** --- ymunozq@uteq.edu.ec

Firma: ______________________________    Fecha: ______________

**Sanchez Cornejo, Gary Alberto** --- gsanchezc6@uteq.edu.ec

Firma: ______________________________    Fecha: ______________
