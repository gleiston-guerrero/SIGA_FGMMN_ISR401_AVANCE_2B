# Tablero de gestion y sincronizacion con la especificacion

**Proyecto SIGA — Sistema Inteligente de Gestion de Aulas · Equipo FGMMN**
Universidad Tecnica Estatal de Quevedo · ISR-401 · Entrega Final (2B)
Medicion: 2026-09-05

---

## 1. El tablero

| | |
|---|---|
| Herramienta | Jira Cloud (Atlassian), espacio de software gestionado por el equipo |
| Espacio | `SIGA` — SIGA - Sistema Inteligente de Gestion de Aulas |
| Actividades | **60**, `SIGA-1` a `SIGA-60` |
| Composicion | 25 requisitos funcionales, 24 no funcionales --- 16 `RNF` y 8 `RNF-IA` --- y 12 restricciones de diseno |
| | La ERS especifica **dieciocho** restricciones. Las seis que no tienen actividad aqui estan declaradas una a una en [`../huerfanos_y_cadenas_rotas.md`](../huerfanos_y_cadenas_rotas.md), apartado 7 |
| Estado | Las 60 en **Por hacer** |

Cada actividad lleva en su descripcion el objetivo del requisito, el stakeholder, la
evidencia de origen, la historia de usuario, el criterio de aceptacion, el caso de prueba,
el marco legal aplicable y el estado de traza, tal como los declara la matriz.

## 2. La medicion

```bash
python 04_Trazabilidad/sincronizacion_tablero.py \
       04_Trazabilidad/tablero_gestion/export_tablero_SIGA.csv
```

```
requisitos en la matriz ....... 60
actividades en el tablero ..... 60
coinciden ..................... 60

SINCRONIZACION = 60 / 60 = 100.0 %
```

Se comparan **conjuntos de identificadores de requisito**, no textos: el titulo de una
actividad puede reescribirse sin que eso signifique una desincronizacion, pero un
identificador que falta a un lado si lo significa.

Se informan las dos direcciones por separado porque no quieren decir lo mismo:

- **Requisito sin actividad** --- el equipo especifico algo que nadie planifico.
- **Actividad sin requisito** --- hay trabajo planificado que no responde a la
  especificacion.

Hoy no hay ninguno de los dos casos.

## 3. Que significa y que no significa este 100 %

**Significa** que todo lo especificado esta planificado y que nada planificado se salio de
la especificacion, medido el 2026-09-05.

**No significa que el trabajo este hecho**: las sesenta y una actividades estan en *Por hacer*,
que es su estado real. El porcentaje mide correspondencia entre dos listas, no avance.

Conviene decirlo porque el tablero **entro mal la primera vez**: la importacion asigno a las
sesenta el estado *Listo*, lo que las ocultaba del backlog y ademas declaraba terminado lo
que no lo esta. Se corrigieron las sesenta a *Por hacer* antes de esta medicion.

## 4. Como reproducirlo

1. En Jira, vista **Lista** del espacio SIGA, exportar a CSV.
2. Ejecutar el script contra ese archivo.

El script acepta cualquier CSV que tenga una columna de resumen o titulo, de modo que la
comprobacion no depende del formato exacto que exporte la herramienta ni de que se siga
usando Jira.

## 5. Archivos

| Archivo | Que es |
|---|---|
| `export_tablero_SIGA.csv` | Export del tablero del 2026-09-05, 61 filas desde que se anadio `RD-01` el 2026-09-06 |
| `../sincronizacion_tablero.py` | Calcula el porcentaje. Solo biblioteca estandar |

Del export se conservan las columnas con contenido util --clave, resumen, tipo, estado,
etiquetas, fecha de creacion y descripcion-- y se retiran las de identificadores internos de
cuenta de la plataforma, que no aportan nada y son datos de una persona.
