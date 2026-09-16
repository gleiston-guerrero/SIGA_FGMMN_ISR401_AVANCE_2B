# Evidencia de autoria y de trabajo propio

**Proyecto SIGA · Equipo FGMMN · ISR-401 · Universidad Tecnica Estatal de Quevedo**

Carpeta exigida por la seccion 6 de la guia de desarrollo emitida el 2026-09-02. Su
finalidad es que quede acreditado, de forma verificable, que los artefactos entregados
fueron producidos por las personas que los firman. La guia lo dice sin rodeos: **la ausencia
de esta evidencia no se suple con una declaracion.**

Este README declara el estado real de cada elemento. **Los doce estan depositados.**

---

## Estado de los doce elementos

| Cod. | Elemento | Estado | Que contiene |
|---|---|---|---|
| A1 | `bitacora_sesiones.csv` | **Depositado** | Una fila por persona y dia con confirmaciones, desde el 2026-08-30 hasta el ultimo dia con commits del historial. Derivado del historial por `generar_bitacora.py`, que se ejecuta en cada cierre; el numero de filas y la ultima fecha son los del propio archivo. Ningun campo se escribe a mano |
| A2 | `capturas/` | **Depositado. 3 de 3 por integrante** | Nueve capturas, tres por persona, cada una en su propia maquina. En todas se ven el archivo del proyecto abierto, el reloj del sistema y la sesion de usuario |
| A3 | Fuentes editables | **Depositado** | En el propio arbol, junto a cada imagen exportada: 44 fuentes y 90 imagenes. Cada fuente con su imagen en la tabla del apartado siguiente y en `fuentes_editables.md`, generados por `generar_fuentes_editables.py` |
| A4 | `grabaciones/` | **Depositado** | Dos sesiones de trabajo de 15:18 y 15:43 con pantalla compartida y discusion audible, mas 18 capturas tomadas durante ellas |
| A5 | `notas_campo/` | **Depositado** | Las seis de la ronda terminal, manuscritas y escaneadas, con fecha, hora de inicio y fin, duracion y codigo de participante. Sin nombres propios. Nombradas `AAAA-MM-DD_TECNICA_CODIGO_Notas.jpg`; las catorce sesiones de elicitacion sin nota declaran su motivo en `bitacora_sesiones.csv` (columna `motivo_sin_notas`) |
| A6 | `fotos_equipo/` | **Depositado** | Dos fotografias en la facultad, con dos integrantes identificables. Se depositan tal como salieron del telefono: los metadatos son la evidencia y cualquier reedicion los altera |
| A7 | `doble_codificacion/` | **Depositado** | Las dos hojas de codificacion independientes sobre los mismos 39 fragmentos, el script del acuerdo y sus resultados. Kappa de Cohen **0,548** para el codigo y **0,911** para la categoria, con intervalo por bootstrap |
| A8 | `correspondencia/` | **Depositado** | Tres capturas de la coordinacion de la ronda terminal y la consulta al docente sobre las firmas de A10 con su respuesta. Datos de terceros censurados |
| A9 | `declaracion_uso_ia.md` | **Depositado** | Por seccion, incluidas aquellas en las que no se empleo ninguna herramienta |
| A10 | `aporte_individual.md` · `.pdf` | **Depositado y firmado** | Generado desde el historial por `04_Trazabilidad/generar_aporte_individual.py`. La version firmada vigente cubre el historial hasta `08878c5` y la **firmaron los tres integrantes acreditados el 2026-09-15**; sustituye a las firmadas el 2026-09-04, el 2026-09-12 y el 2026-09-14 |
| A11 | `exif_inventario.csv` | **Depositado** | Las dos fotografias de A6 con su fecha de captura leida de los metadatos, el dispositivo y el hash. Las dos conservan la fecha |
| A12 | `.mailmap` | **Depositado** | En la raiz del repositorio, que es donde Git lo lee |

## A3: cada fuente editable con su imagen

La tabla la genera `generar_fuentes_editables.py` desde los archivos versionados de
`03_Modelado/`; no se escribe a mano. Cada fuente de Visual Paradigm o draw.io produce la
imagen de su misma carpeta con su mismo nombre, en `.png` y en `.svg`; el archivo de Figma
produce los cuatro prototipos de su carpeta. El script falla si una fuente queda sin imagen o
una imagen sin fuente.

<!-- inicio: tabla fuente-imagen -->

| Fuente editable | Imagen exportada | Carpeta |
|---|---|---|
| `Diagrama_Contexto.vpp` | `Diagrama_Contexto.png`, `Diagrama_Contexto.svg` | `03_Modelado/01_Contexto` |
| `iStar_SD.drawio` | `iStar_SD.png`, `iStar_SD.svg` | `03_Modelado/02_iStar_SD` |
| `iStar_SR.drawio` | `iStar_SR.png`, `iStar_SR.svg` | `03_Modelado/03_iStar_SR` |
| `usecase_general.vpp` | `usecase_general.png`, `usecase_general.svg` | `03_Modelado/04_Casos_Uso` |
| `class_diagram_refined.vpp` | `class_diagram_refined.png`, `class_diagram_refined.svg` | `03_Modelado/05_Clases` |
| `seq_UC01_monitor_room_status.vpp` | `seq_UC01_monitor_room_status.png`, `seq_UC01_monitor_room_status.svg` | `03_Modelado/06_Secuencia` |
| `seq_UC02_remote_equipment_control.vpp` | `seq_UC02_remote_equipment_control.png`, `seq_UC02_remote_equipment_control.svg` | `03_Modelado/06_Secuencia` |
| `seq_UC03_detect_room_occupancy.vpp` | `seq_UC03_detect_room_occupancy.png`, `seq_UC03_detect_room_occupancy.svg` | `03_Modelado/06_Secuencia` |
| `seq_UC04_generate_anomaly_alerts.vpp` | `seq_UC04_generate_anomaly_alerts.png`, `seq_UC04_generate_anomaly_alerts.svg` | `03_Modelado/06_Secuencia` |
| `seq_UC05_attend_anomaly_alert.vpp` | `seq_UC05_attend_anomaly_alert.png`, `seq_UC05_attend_anomaly_alert.svg` | `03_Modelado/06_Secuencia` |
| `seq_UC06_register_maintenance_request.vpp` | `seq_UC06_register_maintenance_request.png`, `seq_UC06_register_maintenance_request.svg` | `03_Modelado/06_Secuencia` |
| `seq_UC07_track_maintenance_ticket.vpp` | `seq_UC07_track_maintenance_ticket.png`, `seq_UC07_track_maintenance_ticket.svg` | `03_Modelado/06_Secuencia` |
| `seq_UC08_view_failure_maintenance_history.vpp` | `seq_UC08_view_failure_maintenance_history.png`, `seq_UC08_view_failure_maintenance_history.svg` | `03_Modelado/06_Secuencia` |
| `seq_UC09_generate_administrative_reports.vpp` | `seq_UC09_generate_administrative_reports.png`, `seq_UC09_generate_administrative_reports.svg` | `03_Modelado/06_Secuencia` |
| `seq_UC10_export_reports.vpp` | `seq_UC10_export_reports.png`, `seq_UC10_export_reports.svg` | `03_Modelado/06_Secuencia` |
| `seq_UC11_manage_users_roles_permissions.vpp` | `seq_UC11_manage_users_roles_permissions.png`, `seq_UC11_manage_users_roles_permissions.svg` | `03_Modelado/06_Secuencia` |
| `seq_UC12_monitor_iot_connectivity.vpp` | `seq_UC12_monitor_iot_connectivity.png`, `seq_UC12_monitor_iot_connectivity.svg` | `03_Modelado/06_Secuencia` |
| `seq_UC13_schedule_automatic_onoff_rules.vpp` | `seq_UC13_schedule_automatic_onoff_rules.png`, `seq_UC13_schedule_automatic_onoff_rules.svg` | `03_Modelado/06_Secuencia` |
| `seq_UC14_log_user_actions.vpp` | `seq_UC14_log_user_actions.png`, `seq_UC14_log_user_actions.svg` | `03_Modelado/06_Secuencia` |
| `seq_UC15_view_room_cameras.vpp` | `seq_UC15_view_room_cameras.png`, `seq_UC15_view_room_cameras.svg` | `03_Modelado/06_Secuencia` |
| `seq_UC16_predict_equipment_failures.vpp` | `seq_UC16_predict_equipment_failures.png`, `seq_UC16_predict_equipment_failures.svg` | `03_Modelado/06_Secuencia` |
| `act_UC01_monitor_room_status.vpp` | `act_UC01_monitor_room_status.png`, `act_UC01_monitor_room_status.svg` | `03_Modelado/07_Actividad` |
| `act_UC02_remote_equipment_control.vpp` | `act_UC02_remote_equipment_control.png`, `act_UC02_remote_equipment_control.svg` | `03_Modelado/07_Actividad` |
| `act_UC03_detect_room_occupancy.vpp` | `act_UC03_detect_room_occupancy.png`, `act_UC03_detect_room_occupancy.svg` | `03_Modelado/07_Actividad` |
| `act_UC04_generate_anomaly_alerts.vpp` | `act_UC04_generate_anomaly_alerts.png`, `act_UC04_generate_anomaly_alerts.svg` | `03_Modelado/07_Actividad` |
| `act_UC05_attend_anomaly_alert.vpp` | `act_UC05_attend_anomaly_alert.png`, `act_UC05_attend_anomaly_alert.svg` | `03_Modelado/07_Actividad` |
| `act_UC06_register_maintenance_request.vpp` | `act_UC06_register_maintenance_request.png`, `act_UC06_register_maintenance_request.svg` | `03_Modelado/07_Actividad` |
| `act_UC07_track_maintenance_ticket.vpp` | `act_UC07_track_maintenance_ticket.png`, `act_UC07_track_maintenance_ticket.svg` | `03_Modelado/07_Actividad` |
| `act_UC08_view_failure_maintenance_history.vpp` | `act_UC08_view_failure_maintenance_history.png`, `act_UC08_view_failure_maintenance_history.svg` | `03_Modelado/07_Actividad` |
| `act_UC09_generate_administrative_reports.vpp` | `act_UC09_generate_administrative_reports.png`, `act_UC09_generate_administrative_reports.svg` | `03_Modelado/07_Actividad` |
| `act_UC10_export_reports.vpp` | `act_UC10_export_reports.png`, `act_UC10_export_reports.svg` | `03_Modelado/07_Actividad` |
| `act_UC11_manage_users_roles_permissions.vpp` | `act_UC11_manage_users_roles_permissions.png`, `act_UC11_manage_users_roles_permissions.svg` | `03_Modelado/07_Actividad` |
| `act_UC12_monitor_iot_connectivity.vpp` | `act_UC12_monitor_iot_connectivity.png`, `act_UC12_monitor_iot_connectivity.svg` | `03_Modelado/07_Actividad` |
| `act_UC13_schedule_automatic_onoff_rules.vpp` | `act_UC13_schedule_automatic_onoff_rules.png`, `act_UC13_schedule_automatic_onoff_rules.svg` | `03_Modelado/07_Actividad` |
| `act_UC14_log_user_actions.vpp` | `act_UC14_log_user_actions.png`, `act_UC14_log_user_actions.svg` | `03_Modelado/07_Actividad` |
| `act_UC15_view_room_cameras.vpp` | `act_UC15_view_room_cameras.png`, `act_UC15_view_room_cameras.svg` | `03_Modelado/07_Actividad` |
| `act_UC16_predict_equipment_failures.vpp` | `act_UC16_predict_equipment_failures.png`, `act_UC16_predict_equipment_failures.svg` | `03_Modelado/07_Actividad` |
| `state_alert.vpp` | `state_alert.png`, `state_alert.svg` | `03_Modelado/08_Estados` |
| `state_maintenance_request.vpp` | `state_maintenance_request.png`, `state_maintenance_request.svg` | `03_Modelado/08_Estados` |
| `dfd_nivel_0.drawio` | `dfd_nivel_0.png`, `dfd_nivel_0.svg` | `03_Modelado/09_DFD` |
| `dfd_nivel_1.drawio` | `dfd_nivel_1.png`, `dfd_nivel_1.svg` | `03_Modelado/09_DFD` |
| `component_diagram.vpp` | `component_diagram.png`, `component_diagram.svg` | `03_Modelado/10_Componentes` |
| `deployment_diagram.vpp` | `deployment_diagram.png`, `deployment_diagram.svg` | `03_Modelado/11_Despliegue` |
| `Mockups_SIGA_Entrega2.fig` | `Mockup_Alertas.png`, `Mockup_Mantenimiento.png`, `Mockup_Panel.png`, `Mockup_Reportes.png` | `03_Modelado/12_Prototipos_Interfaz` |

<!-- fin: tabla fuente-imagen -->

## Sobre las firmas de A10

El elemento pide el documento **«firmado por los cinco»**. Este equipo son tres: de los cinco
nombres del grupo del SGA, **Mendoza Palma, Allan Jeremy** y **Gilces Carranza, Jose Ignacio**
estan retirados del equipo y no produjeron ningun artefacto. Se consulto por escrito al docente responsable, que respondio el 2026-09-04:
**«No debe aparecer nadie mas en el documento.»**

La consulta y la respuesta constan en
[`correspondencia/2026-09-04_Consulta_firmas_aporte_individual.png`](correspondencia/2026-09-04_Consulta_firmas_aporte_individual.png).
El documento lo firman los tres integrantes acreditados y no nombra a nadie mas.

## Sobre la lista de verificacion previa

[`verificacion_previa.pdf`](verificacion_previa.pdf) recoge las doce comprobaciones de la
seccion 11 de la guia, **ejecutadas sobre un clon limpio del remoto**, no marcadas a mano:
el detalle de cada una es la salida real de `verificacion_previa.py`.

La version vigente va firmada por **los tres integrantes** el 2026-09-15, sobre el clon limpio
de `08878c5`, y sustituye a las firmadas el 2026-09-12 y el 2026-09-14. La
guia exige que quien comprueba sea una persona distinta de quien produjo cada artefacto, y
con un solo firmante eso no se puede cumplir sobre el arbol entero. El reparto **lo calcula
el script desde el historial, archivo por archivo**: Cedeno Avila verifica lo que no toco,
Munoz Quinonez lo que toco el y ella no, y Sanchez Cornejo lo que tocaron los otros dos y el
no. Los dos archivos que tocaron los tres se declaran en el documento como sin verificador
distinto de su autor.

## Que no hay aqui

Ninguna carpeta se relleno con marcadores de posicion en ningun momento. El criterio de piso
P3 sanciona con cero cualquier archivo que anuncie una pieza de evidencia y no la contenga;
mientras un material no existia, la tabla de arriba lo declaraba faltante en lugar de crear
un archivo vacio con su nombre.

## Como comprobarlo

```bash
python 10_Autoria/verificacion_previa.py --clonar
```

Clona el remoto en una carpeta limpia y ejecuta las doce comprobaciones, incluida la de que
los doce elementos existen y tienen contenido.
