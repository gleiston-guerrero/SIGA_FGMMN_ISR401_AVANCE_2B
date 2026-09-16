# Retrospectiva del equipo — cierre del Proyecto Fin de Curso

**Proyecto SIGA · Equipo FGMMN · ISR-401 · Universidad Tecnica Estatal de Quevedo**

Fecha: 2026-09-16
Redactada por: Munoz Quinonez, Yeranick Esther

Complementa la retrospectiva del 2026-09-05, que esta en el anexo «Retrospectiva del equipo»
de `reporte.tex`. Esta recoge lo que paso despues: las evaluaciones del cierre, los reclamos
que presentamos, como se resolvieron, que hizo cada integrante y que aprendimos.

---

## 1. Cronologia del cierre

| Fecha | Que paso | Donde consta |
|---|---|---|
| 2026-09-02 | El docente emite la guia de desarrollo y consolidacion sobre el clon de ese dia | `CHANGELOG.md` |
| 2026-09-12 | Rubrica de cierre del PFC. Presentamos cuatro objeciones: A3 (trabajo anterior al 30/08), fuentes editables, capturas e inventario EXIF, y composicion del equipo | Etiquetas `2B-final-v5.0` a `v5.5` |
| 2026-09-13 | El docente acepta las cuatro objeciones y califica 8,42. Queda a medias solo B1: las tablas debian generarse dentro de `07_Datos` | Etiquetas `2B-final-v5.6` y `v5.7` |
| 2026-09-14 | Nueva evaluacion: 2,99. B4 (tamanos del efecto con intervalos sin sentido) y un factor individual proporcional a los commits | Informe del docente |
| 2026-09-14 | Presento un reclamo sobre la escala de factores y el factor individual | Enviado por WhatsApp |
| 2026-09-14 | Guia de cierre del examen suspenso. Corrijo B4 (el efecto se calcula con el requisito como unidad, desviacion 7) y B1 (la cadena de analisis se ejecuta dentro de `07_Datos`) | Etiqueta `2B-final-v5.8` |
| 2026-09-14 y 15 | Correcciones de la guia de cierre: columnas `n_pares` e `interpretable`, notas de campo y motivos en la bitacora, URL del nuevo propietario, cifras y rutas del reporte | Etiquetas `2B-final-v5.9` y `v5.10` |
| 2026-09-16 | Llega un informe que no corresponde a SIGA: cita el commit `cc6d886` y la etiqueta `cierre-v1.0-final`, que no existen en nuestro repositorio. Se lo indico al docente, que reconoce el error y recalifica | Comunicado por WhatsApp |
| 2026-09-16 | Informe del examen suspenso sobre `98f1a6b`: 4,00, con §3, §15 y §16 por modificar | Informe del docente |
| 2026-09-16 | Correcciones de §15 y §16: kappa con intervalo, tabla por requisito con pares e interpretabilidad, cifra retirada del manuscrito, tabla fuente-imagen y esta retrospectiva | Commits `900b9f7` a `7716773`, este archivo y la etiqueta `2B-final-v5.11` |

## 2. Reclamos presentados y como se resolvieron

| Reclamo | Que pedimos | Resolucion |
|---|---|---|
| Objeciones a la rubrica de cierre (2026-09-12) | Que se verificaran A3, las fuentes editables, las capturas y el EXIF abriendo los archivos, y que se aceptara la composicion de tres integrantes | Aceptadas las cuatro el 2026-09-13. La composicion se autorizo a posteriori, sin sentar precedente, con factor individual cero para los dos nombres retirados |
| Calificacion del 2026-09-14 | Aplicar la escala de factores de la rubrica (1,00 / 0,90 / 0,75 / 0,60), revisar B2, B5 y B6, reconocer B1 resuelto y aplicar el criterio P8 en lugar de un factor proporcional a los commits | El docente respondio con la guia de cierre del examen suspenso, que calcula la nota de otra forma; la nota individual se asigna a quien trabajo en la fase de cierre |
| Informe equivocado (2026-09-16) | Que se revisara SIGA sobre `98f1a6b`, porque el informe citaba un commit, una etiqueta y archivos de otro repositorio | El docente reconocio el error y recalifico el mismo dia: 4,00 sobre `98f1a6b` |

## 3. Quien hizo que

| Integrante | Rol declarado | Trabajo en el repositorio |
|---|---|---|
| Sanchez Cornejo, Gary Alberto | Analista lider; especificacion, componente empirico e integracion | 173 commits del 2026-08-30 al 2026-09-13: ERS, modelado, componente empirico, paquete de datos hasta `2B-final-v5.7` |
| Munoz Quinonez, Yeranick Esther | Documentacion, trazabilidad, auditoria de calidad y gestion de evidencias | Commits desde el 2026-08-30. Desde el 2026-09-14, todos los commits de la fase de cierre: correcciones de B4 y B1, guia de cierre, etiquetas `2B-final-v5.8` a `v5.10`, las correcciones de §15 y §16 y la etiqueta `2B-final-v5.11` |
| Cedeno Avila, Winston Damian | Transcripcion y anonimizacion del corpus | 12 commits del 2026-09-04 al 2026-09-09: transcripciones EV-20 a EV-28, codificacion tematica, doble codificacion, inspecciones INS-01 y REINS-01 y defensa grabada |

Mendoza Palma, Allan Jeremy y Gilces Carranza, Jose Ignacio estan retirados del equipo y no
produjeron ningun artefacto.

En la fase de cierre me ayudo, fuera del repositorio, el analista lider de SIGA, Sanchez
Cornejo, Gary Alberto: reviso conmigo los informes y la guia y me aconsejo; preparo con un
asistente de IA, en su computadora, los paquetes de correccion que yo revise y aplique; y
firmo, junto con Cedeno Avila, la verificacion previa y el aporte individual del 2026-09-14 y
del 2026-09-15. Nadie mas me ayudo.

Los commits de la fase de cierre los ejecuto un asistente de IA en mi equipo, con mi identidad,
bajo mi supervision y controlando yo cada decision. Las herramientas de IA usadas en cada
correccion constan en `10_Autoria/declaracion_uso_ia.md`.

## 4. Que aprendimos

1. Con una muestra tan pequena, el estimador puntual carece de valor inferencial, pues el
   intervalo de confianza (amplitud 40) es compatible tanto con ausencia de efecto como con un
   efecto sustancial. La leccion es reportar siempre el intervalo junto al estimador y
   reconocer cuando el tamano muestral no permite conclusion alguna.
2. Todo reclamo academico debe fundamentarse en una auditoria previa del propio trabajo frente
   al criterio textual de la rubrica y la evidencia efectivamente disponible en el
   repositorio. Impugnar una calificacion sin esa verificacion previa debilita el argumento,
   incluso cuando existe una causa legitima de fondo.
3. Se procuraria, desde el inicio, dejar constancia formal de las condiciones de conformacion
   del equipo y mantener la totalidad del trabajo consolidado en un repositorio unico y
   evaluable, evitando su dispersion en repositorios de terceros o en archivos delta que
   impidan reconstruir el avance real del proyecto.
4. La reproducibilidad —mediante checksums, orden determinista de datos y documentos
   autocompilables— constituye la garantia ultima de la integridad de una entrega, al permitir
   su verificacion independiente sin depender del testimonio de quien la produjo.

## 5. Que haremos distinto

| Que | Accion concreta | Responsable |
|---|---|---|
| Sobrecarga de trabajo | Dividir el trabajo equitativamente | Sanchez Cornejo, Gary Alberto |
| Temor a pedir ayuda | Confiar en mi equipo de trabajo | Munoz Quinonez, Yeranick Esther |
| Baja participacion en la fase de cierre | Involucrarse en mayor medida con el equipo | Cedeno Avila, Winston Damian |
