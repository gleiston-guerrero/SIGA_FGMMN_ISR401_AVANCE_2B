# El contenedor de la zona restringida, dentro del repositorio

**Proyecto SIGA --- Sistema Inteligente de Gestion de Aulas · Equipo FGMMN**
Universidad Tecnica Estatal de Quevedo · ISR-401 · Entrega Final (2B)

---

## 1. Que hay aqui

**316 fragmentos** de un unico archivo `SIGA_zona_restringida.7z`, cifrado con **AES-256** y
con los nombres de archivo tambien cifrados. Contiene el material que el consentimiento
firmado **no autoriza a publicar**, y que esta enumerado en
[`../README_Restringido.md`](../README_Restringido.md), apartado 2.

Los fragmentos **no se pueden abrir por separado**. Solo sirven los 316 juntos y en orden.

| | |
|---|---|
| Archivo original | `SIGA_zona_restringida.7z`, 7 935 839 986 bytes |
| SHA-256 del original | `76a78d6b6be140effff3f9e3d42cbe13e6da68fa36ae49dec4b8fbb089df4f00` |
| Fragmentos | 316, de 24 MiB cada uno salvo el ultimo |
| Cifrado | AES-256, con cabecera de nombres cifrada |
| Fecha del contenedor | 2026-09-08 |

> **Rehecho el 2026-09-08.** El contenedor anterior --- 6 822 192 770 bytes en 272
> fragmentos, SHA-256 `d225b192...49f05f8a` --- se regenero para incorporar los dos videos
> que faltaban: el de la sesion `WT-10` con `TIC-03`, del 2026-09-07, y el de `EV-16`, que
> estuvo declarado como no recuperable hasta que aparecio en el almacen Git LFS del
> repositorio de la Entrega 2A. Pasa de **49 a 51 archivos**.
>
> **Se cifro con una contrasena distinta de la anterior.** La previa habia dejado de ser
> secreta, y un contenedor que viaja dentro de un repositorio publico se puede descargar
> entero y atacar sin limite de intentos. Cambiarla no es una precaucion de mas: es lo unico
> que sigue protegiendo consentimientos con nombre y cedula, y entrevistas de diecinueve
> personas.

## 2. Por que esta partido, y por que esta aqui dentro

**Partido**, porque GitHub rechaza cualquier archivo de mas de 100 MB sin Git LFS, y este
repositorio no usa LFS a proposito --- consta en `.gitattributes`. Cortado en 24 MiB, cada
fragmento entra holgadamente y el conjunto viaja como objetos normales de Git.

**Aqui dentro**, y no en un servicio externo, porque un enlace es un punto unico de fallo.
Hasta el 2026-09-06 este contenedor vivia solo en el OneDrive institucional y el repositorio
publicaba su direccion. Eso significa que si el enlace caduca, si la cuenta institucional
cambia, o si quien evalua no puede abrirlo, **la evidencia restringida deja de existir a
efectos practicos**, aunque el archivo siga en alguna parte. Depositado aqui, viaja con el
repositorio, se clona con el y se archiva con el en Software Heritage.

**La copia de OneDrive ya no se mantiene.** El contenedor esta unicamente en el repositorio,
en estos fragmentos.

## 3. Como reconstruirlo y abrirlo

Con 7-Zip instalado basta **abrir el primer fragmento**; el programa reconoce la secuencia
y reune el resto solo:

```
02_Evidencias/00_Restringido/contenedor/SIGA_zona_restringida.7z.001
```

Pedira la contrasena, que **no consta en este repositorio** y se entrega al docente
responsable por el Sistema de Gestion Academica. Por linea de orden:

```bash
7z x SIGA_zona_restringida.7z.001
```

Sin 7-Zip, los fragmentos se reunen concatenandolos en orden:

```bash
cat SIGA_zona_restringida.7z.* > SIGA_zona_restringida.7z
```

## 4. Como comprobar que llegaron completos

Antes de pedir la contrasena a nadie, conviene comprobar que el clon trajo los 316
fragmentos intactos. Esto no necesita contrasena:

```bash
cat SIGA_zona_restringida.7z.* | sha256sum
```

Debe dar exactamente:

```
76a78d6b6be140effff3f9e3d42cbe13e6da68fa36ae49dec4b8fbb089df4f00
```

Si coincide, el contenedor esta completo y sin alterar. Si no coincide, falta algun
fragmento o el clon se trunco: repetir el `git clone` antes de sospechar del cifrado.

La suma de cada fragmento por separado esta ademas en el manifiesto general del
repositorio, `checksums.sha256`, de modo que `sha256sum -c` localiza **cual** de los 316
vino mal.

## 5. Lo que esta comprobado y lo que no

**Comprobado:** que los 316 fragmentos reconstruyen el archivo original byte a byte. Se
calculo la suma SHA-256 del original y la de la concatenacion de los fragmentos, y
coinciden. Tambien que 7-Zip reconoce el conjunto como archivo cifrado desde el primer
fragmento.

**Comprobado tambien, el 2026-09-07:** que el contenedor **descifra y se extrae**. Lo hizo
quien custodia la contrasena, no consta aqui como se hizo, y el resultado son **49 archivos,
6,4 GB**: las grabaciones de video y audio de la ronda terminal y de las sesiones tecnicas,
las fotografias de sesion y el acta firmada de `WT-08`.

Las dos comprobaciones juntas cerraron la cadena para aquel contenedor: sus 272 fragmentos
reconstruian el archivo **byte a byte** --- misma suma SHA-256 --- y ese archivo **se abria**.
Si la concatenacion es identica al original y el original descifra, la concatenacion
descifra; no hay hueco entre las dos afirmaciones.

**Sobre el contenedor vigente**, regenerado el 2026-09-08 con 316 fragmentos y 51 archivos:
consta la reconstruccion byte a byte de la seccion anterior. La prueba de extraccion que se
describe arriba, con su resultado de 49 archivos, es la del contenedor del 2026-09-07.

> **Despues de extraerlo, borre la carpeta descomprimida.** Contiene 6,4 GB de material
> identificable sin cifrar: nombres, caras y voces de participantes que consintieron
> justamente lo contrario. El contenedor existe para que ese material **no** quede suelto en
> un escritorio.
