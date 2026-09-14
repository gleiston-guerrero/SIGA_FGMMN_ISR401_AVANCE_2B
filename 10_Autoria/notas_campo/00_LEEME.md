# A5 — Notas manuscritas de las sesiones de elicitacion

Notas **escritas a mano** durante cada sesion, escaneadas, **con la fecha visible** en la
propia hoja.

No sirve una transcripcion mecanografiada: lo que se pide es la nota manuscrita.

## Como capturarlas

Lleve un cuaderno a cada entrevista y escriba la fecha grande y legible en la esquina
superior de cada hoja, antes de empezar. Escriba durante la sesion, no despues.

Escanee o fotografie cada hoja con luz suficiente para que la fecha se lea sin ampliar.

## Nombre del archivo

El que fija la guia de cierre del docente, del 2026-09-14:

```
AAAA-MM-DD_TECNICA_CODIGO_Notas.jpg
```

Ejemplo: `2026-09-03_Entrevista_DOC-05_Notas.jpg`

## Las sesiones que no tienen nota

La bitacora (`../bitacora_sesiones.csv`) registra una fila por sesion de elicitacion, derivada
de su transcripcion. Su columna `notas_campo` nombra la nota de la sesion, y su columna
`motivo_sin_notas` explica por que no la hay cuando falta. Los motivos los declara el equipo en
[`sesiones_sin_nota.csv`](sesiones_sin_nota.csv), y `generar_bitacora.py` no termina si una
sesion no tiene nota ni motivo.

**No se elaboran notas a posteriori.** Una nota escrita despues y fechada el dia de la sesion no
acreditaria lo que se registro durante ella: seria una reconstruccion presentada como registro.

## Cuidado con los datos personales

Si en la nota aparece el nombre del entrevistado, tapelo antes de escanear. La zona publica
del repositorio no admite datos identificables, y el criterio de piso es explicito: ningun
archivo cuyo nombre revele la identidad de un participante puede quedar en la zona publica.

## Por que estas seis estan tambien en `02_Evidencias/Notas_Campo/`

Figuran en dos sitios porque responden a dos exigencias distintas: aqui como **elemento A5
del indice de autoria**, y alli como **evidencia de campo de la seccion 5.1 de la guia**,
junto a las seis notas de observacion de entorno `NC-01` a `NC-06`, que completan las doce.

Alli se depositaron como PDF de una pagina. Aqui estan en JPG porque asi lo pide la guia de
cierre, y **no son una segunda digitalizacion**: cada JPG es, byte a byte, la imagen escaneada
que contiene el PDF correspondiente, extraida sin recomprimir. Se comprueba asi:

```
pdfimages -j 02_Evidencias/Notas_Campo/2026-09-03_Docente_DOC-05_EV-20_NotaCampo.pdf /tmp/doc05
cmp /tmp/doc05-000.jpg 10_Autoria/notas_campo/2026-09-03_Entrevista_DOC-05_Notas.jpg
```

`cmp` no imprime nada cuando los dos archivos son identicos.
