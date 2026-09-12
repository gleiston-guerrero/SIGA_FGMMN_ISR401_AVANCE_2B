# Composicion del equipo en la Entrega Final (2B) y en el examen final

**Proyecto SIGA — Sistema Inteligente de Gestion de Aulas · Equipo FGMMN**
Universidad Tecnica Estatal de Quevedo · ISR-401 Ingenieria de Requerimientos

Actualizado el 2026-09-03, tras la reincorporacion de un integrante, y el 2026-09-12, para declarar
retirados a los dos nombres del SGA que no forman parte del equipo.

---

## 1. Quienes integran el equipo

| Integrante | Rol | Cedula | Correo institucional | Desde |
|---|---|---|---|---|
| Sanchez Cornejo, Gary Alberto | Analista lider; especificacion, componente empirico e integracion | 1208338291 | gsanchezc6@uteq.edu.ec | Inicio del proyecto |
| Munoz Quinonez, Yeranick Esther | Documentacion, trazabilidad, auditoria de calidad y gestion de evidencias | 1207929645 | ymunozq@uteq.edu.ec | Inicio del proyecto |
| Cedeno Avila, Winston Damian | Transcripcion y anonimizacion del corpus de entrevistas | — | wcedenoa2@uteq.edu.ec | **2026-09-02** |

**Son tres personas.** Las dos primeras responden por la Entrega Final (2B) tal como se
califico; la tercera se reincorpora para la ronda terminal de campo y responde por el
trabajo que produzca a partir de su fecha de incorporacion.

### Integrantes retirados

| Integrante | Situacion |
|---|---|
| Mendoza Palma, Allan Jeremy | **Retirado del equipo** |
| Gilces Carranza, Jose Ignacio | **Retirado del equipo** |

Los dos figuran en el grupo `FGMMN` del Sistema de Gestion Academica y ninguno forma parte
del equipo activo. **No produjeron artefactos ni confirmaciones en este repositorio**, no
participan en la Entrega Final ni en el examen final, y no se les atribuye ninguna parte del
trabajo ni responsabilidad sobre lo entregado. Por eso no tienen commits, ni fila en el
aporte individual, ni firma en ningun documento del equipo. El apartado 3 da el detalle.

## 2. Que dice el historial, que es lo que se puede comprobar

Esta declaracion no pide que se le crea. El recuento por autor sobre la rama por defecto es
comprobable con `git shortlog -sne main`:

| Autor del historial | Commits | Correo de la firma | Situacion |
|---|---|---|---|
| Gary Alberto Sanchez Cornejo | 169 | gsanchezc6@uteq.edu.ec | Acreditado |
| Yeranick Esther Munoz Quinonez | 83 | ymunozq@uteq.edu.ec | Acreditada |
| Winston Damian Cedeno Avila | 12 | wcedenoa2@uteq.edu.ec | Acreditado. **Incorporado el 2026-09-02**; sus confirmaciones empiezan con la ronda terminal |

Recuento actualizado el 2026-09-12 sobre el commit `13dd0af`. Mendoza Palma y Gilces Carranza,
retirados, no tienen ninguna confirmacion.

Hasta el 2026-09-03 esta tabla declaraba **cero** confirmaciones para el tercer integrante, y
se dejaba el cero a la vista porque la alternativa habria sido afirmar una contribucion que el
historial no respaldaba. Ya la respalda. El detalle commit por commit esta en
[`aporte_individual.csv`](aporte_individual.csv), con una fila por confirmacion y su
identificador, comprobado uno a uno contra el repositorio.

**Sobre el committer de una de esas tres confirmaciones.** Una se creo desde la interfaz web
de GitHub, de modo que su *committer* figura como `GitHub <noreply@github.com>` mientras que
su *autor* es el integrante con su correo institucional. Git distingue las dos cosas: el autor
identifica a quien se atribuye el cambio; el committer registra por que medio se aplico. Los
tres correos de autor del historial son los tres institucionales, comprobable con
`git log --format=%ae | sort -u`, y ninguna confirmacion lleva un autor ni un coautor que no
sea integrante.

**Lo que el campo autor no dice.** Buena parte de las confirmaciones —tambien varias a nombre
de los otros dos integrantes— las ejecuto un asistente de inteligencia artificial desde la
maquina del analista lider, con el nombre del integrante al que el equipo atribuyo cada
cambio. Se declara, con ejemplos, en
[`10_Autoria/declaracion_uso_ia.md`](../10_Autoria/declaracion_uso_ia.md). Por eso el aporte
de cada persona no se acredita solo con el recuento de confirmaciones, sino tambien con las
grabaciones de las sesiones de trabajo, las capturas por integrante y el aporte individual
firmado de `10_Autoria/`.

**Una precision sobre el recuento.** Una declaracion de aporte no puede incluir el commit
que la deposita: el identificador todavia no existe cuando se escribe el archivo. Por eso el
recuento corresponde al historial hasta el commit inmediatamente anterior a este, y la
diferencia es siempre de una sola confirmacion.

## 3. Quien se retiro, y cuando

El grupo `FGMMN` del Sistema de Gestion Academica declara **cinco** integrantes. La guia
de desarrollo del 2026-09-02 los conto sobre la caratula entonces subida, que recogia
cuatro, y observo --correctamente-- que dos de ellos no tenian ninguna confirmacion en el
historial. Sobre el listado completo del SGA **son dos los que no aparecen en el historial**,
y este apartado resuelve a los dos:

| Integrante declarado en el SGA | Situacion a 2026-09-12 |
|---|---|
| Sanchez Cornejo, Gary Alberto | Activo. Analista lider |
| Munoz Quinonez, Yeranick Esther | Activa. Documentacion, trazabilidad y auditoria |
| Cedeno Avila, Winston Damian | **Reincorporado** el 2026-09-02. Asume la transcripcion y anonimizacion del corpus de entrevistas de la ronda terminal |
| Mendoza Palma, Allan Jeremy | **Retirado del equipo.** No produjo artefactos ni confirmaciones en este repositorio y no participa en la Entrega Final ni en el examen final |
| Gilces Carranza, Jose Ignacio | **Retirado del equipo.** No produjo artefactos ni confirmaciones en este repositorio, no participo en el trabajo en ningun momento y no participa en la Entrega Final ni en el examen final |

**Se declara de mas, no de menos.** El recuento anterior de este documento decia cuatro
porque seguia a la caratula; el listado del SGA dice cinco. Se corrige al alza aunque el
segundo nombre anada un integrante sin contribucion, porque el evaluador va a comparar
contra el SGA y no contra la caratula.

No se reclama trabajo de quien se retiro, ni se le atribuye responsabilidad sobre lo
entregado. La caratula del SGA se corrige para reflejar la composicion vigente.

**La solicitud esta presentada y firmada.**
[`2026-09-08_Solicitud_Cambio_Composicion.pdf`](2026-09-08_Solicitud_Cambio_Composicion.pdf),
tres paginas, suscrita por los tres integrantes el 2026-09-08. Expone el cambio con sus
fechas, resuelve por su nombre a los dos declarados que no tienen confirmaciones, y pide tres
cosas: que se autorice la composicion de tres, que se indique si debe corregirse la caratula
del Sistema de Gestion Academica, y que **se deje constancia de que la solicitud se presenta
fuera de plazo** y de la consecuencia que ello tenga sobre la calificacion.

**Lo que el escrito no puede darse a si mismo es la autorizacion.** Subsana la omision de no
haberla pedido antes; concederla o no es del docente, y hasta que resuelva se declara
pendiente. Se prefiere que conste a que se pase por alto.

## 4. Que no se reescribe

Hay evidencia firmada que no admite actualizacion retroactiva, y no se toca:

- El **acta de constancia del cierre de campo en N=10** y sus firmas de testigos.
- Los **consentimientos de la sesion de validacion comunicativa** del 2026-09-01.

Los tres documentos estan firmados por dos personas porque en esa fecha el equipo eran dos.
Se declara aqui que la composicion se amplio despues, con su fecha, en lugar de rehacer un
documento firmado.

## 5. Coherencia con el registro previo

El registro del protocolo en OSF --- `10.17605/OSF.IO/7PQ3H` --- declara **dos**
contribuyentes, comprobado el 2026-09-01 contra la API publica y guardado literalmente en
`06_Experimento/registro_previo/osf_contributors_api.json`.

Esa lista corresponde a la composicion vigente cuando se ejecuto el cuasi-experimento, que
es el trabajo que el registro cubre. La reincorporacion del 2026-09-02 es posterior al
componente empirico y no afecta a su autoria.

Conviene precisar que las listas describen momentos distintos y no siempre coincidieron: el
protocolo se preregistro cuando el equipo tenia mas integrantes, y la lista de contribuyentes
se actualizo despues. Lo que un registro OSF congela es **el contenido registrado**
--- preguntas, hipotesis, variables y plan de analisis, que es lo que da valor a la marca
temporal --- no la lista de personas asociadas, que si admite mantenimiento.

Queda una diferencia menor y se declara: el nodo de proyecto `3nruf` del que cuelga el
registro figura hoy con un solo contribuyente. Es el contenedor, no el registro evaluable.

## 6. Alcance de esta declaracion

Los artefactos de entregas anteriores que este repositorio hereda fueron evaluados en su
propia entrega. Este documento no reclama para el equipo actual autoria sobre trabajo de
terceros, ni retira credito a quien lo produjo en su momento: delimita **quien responde por
la Entrega Final (2B) y por el examen final**, que es lo que se evalua.

Los tres integrantes respondemos por la totalidad del contenido entregado a partir del
2026-09-02. Por lo entregado y calificado antes de esa fecha responden los dos primeros.
