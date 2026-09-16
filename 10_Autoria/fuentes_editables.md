# Fuentes editables de los diagramas — elemento A3

**Proyecto SIGA · Equipo FGMMN · ISR-401 · UTEQ**

La guia exige el archivo fuente editable de todo diagrama junto a su imagen exportada:
«sin el archivo fuente no hay prueba de que el diagrama se construyo y no se descargo».

Las fuentes **no se copian a esta carpeta**: residen junto a la imagen que producen, que
es donde sirven para trabajar. La tabla de abajo empareja cada fuente con su imagen.

**Este archivo no se escribe a mano**: lo genera `generar_fuentes_editables.py` desde los
archivos versionados de `03_Modelado/`, y la misma tabla se copia en `README.md`.

| Tipo de fuente | Cantidad | Herramienta |
|---|---|---|
| `.vpp` | 39 | Visual Paradigm |
| `.drawio` | 4 | draw.io |
| `.fig` | 1 | Figma |
| **Total** | **44** | |

| Imagen exportada | Cantidad |
|---|---|
| `.png` | 47 |
| `.svg` | 43 |
| **Total** | **90** |

**Como se empareja.** 43 fuentes de Visual Paradigm y draw.io tienen su imagen en la misma carpeta y con el mismo nombre, exportada en `.png` y en `.svg`. El archivo de Figma `Mockups_SIGA_Entrega2.fig` produce las 4 imagenes de `03_Modelado/12_Prototipos_Interfaz` que no tienen fuente con su nombre. Asi, las 90 imagenes tienen su fuente y las 44 fuentes tienen al menos una imagen.

## Cada fuente con su imagen

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

## Comprobacion

```
python 10_Autoria/generar_fuentes_editables.py
```

Termina con codigo 0 solo si ninguna fuente queda sin imagen y ninguna imagen sin fuente.
