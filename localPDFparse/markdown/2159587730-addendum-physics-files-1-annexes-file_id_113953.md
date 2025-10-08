---
title: Sin título
author: Javiera Manetti
date: D:20240412180819-04'00'
language: es
type: manual
pages: 14
has_toc: False
has_tables: True
extraction_quality: high
---

|ELABORÓ : DOS|EDICIÓN|
|---|---|
|**REVISÓ**<br>: JSI|A|
|**FECHA**<br>: Abril - 2024|**FECHA**<br>: Abril - 2024|

**Índice**

1. INTRODUCCIÓN .................................................................................................................................................................................. 3

1.1. UBICACIÓN DEL PROYECTO .................................................................................................................................................. 3

2. ANTECEDENTES ................................................................................................................................................................................. 4

2.1. HIDROLOGÍA LOCAL ................................................................................................................................................................ 4

2.2. ÁREA APORTANTE .................................................................................................................................................................. 5

2.3. CAUDALES MÁXIMOS DE CRECIDA ....................................................................................................................................... 6

3. MODELACIÓN HIDRÁULICA ............................................................................................................................................................... 7

3.1. ZONA DE ANÁLISIS .................................................................................................................................................................. 7

3.2. METODOLOGÍA MODELACIÓN 1D .......................................................................................................................................... 8

3.2.1. Características geométricas del modelo ............................................................................................................................... 8

3.2.2. Estimación del coeficiente de rugosidad ............................................................................................................................... 8

3.2.3. Características de la modelación .......................................................................................................................................... 9

4. RESULTADOS MODELACIÓN 1D ..................................................................................................................................................... 10

Contacto : contacto@emergeingenieria.cl
**1**
Teléfono : +56 9 5659 1903

**Índice de figuras**

Figura 1.1. Ubicación del Proyecto................................................................................................................................................................ 3

Figura 2.1. Hidrología local............................................................................................................................................................................ 4

Figura 2.2. Área aportante a cauce a modificar ............................................................................................................................................ 5

Figura 3.1. Topografía disponible .................................................................................................................................................................. 7

Figura 4.1. Ubicación perfiles transversales asignados para la modelación hidráulica .............................................................................. 10

Figura 4.2. Área de inundación cauce natural ............................................................................................................................................. 12

Figura 4.3. Área de inundación con canal proyectado ................................................................................................................................ 13

**Índice de tablas**

Tabla 2.1. Parámetros morfométricos de áreas aportantes .......................................................................................................................... 5

Tabla 2.2. Resultados de caudal máximo, Área Aportante C2 ...................................................................................................................... 6

Tabla 3.1. Definición y valores para parámetros de la ecuación de Cowan.................................................................................................. 8

Tabla 3.2. Valores de parámetros y Manning obtenido mediante método de Cowan ................................................................................... 9

Tabla 4.1. Resultados modelación .............................................................................................................................................................. 11

Contacto : contacto@emergeingenieria.cl
**2**
Teléfono : +56 9 5659 1903

**1.** **INTRODUCCIÓN**

El Proyecto “PMGD Coloane” (en adelante, el “Proyecto”) está ubicado en la Región de Los Lagos, provincia de Chiloé, específicamente

en la comuna de Ancud, a unos 10 km al este de la ciudad de Ancud.

La finalidad de este estudio es caracterizar la componente hidrológica del área de estudio, y posteriormente, con la modelación hidráulica,

definir las áreas de inundación de los cauces existentes cercanos al Proyecto. La modelación hidráulica se realiza utilizando el software

de libre acceso HEC-RAS (Hydraulic Engineering Center - River Analysis System), desarrollado por el US Corp Engineers, el cual es

aceptado en proyectos hidráulicos por la Dirección General de Aguas (DGA) y la Dirección de Obras Hidráulicas (DOH).

**1.1.** **UBICACIÓN DEL PROYECTO**

El Proyecto se encuentra emplazado en la comuna de Ancud, provincia de Chiloé, región de Los Lagos. El ingreso a la zona del Proyecto

se realiza desde la Ruta 5 Sur, proyectándose un nuevo camino de ingreso que conecte con la ruta. En la Figura 1.1 se muestra la

ubicación general y local del Proyecto.

**Figura 1.1. Ubicación del Proyecto**

Contacto : contacto@emergeingenieria.cl
**3**
Teléfono : +56 9 5659 1903

**2.** **ANTECEDENTES**

**2.1.** **HIDROLOGÍA LOCAL**

La red hídrica local se caracteriza por el Río Huicha y dos cauces efluentes de él. En la Figura 2.1 se muestra la ubicación del Proyecto

y los cauces identificados.

**Figura 2.1. Hidrología local**

Debido a que los cauces interactúan con la ubicación de las plataformas en la cual se ubican los aerogeneradores, se proyecta en el

cauce ubicado al sur la construcción de un canal que desvíe el flujo, por lo tanto, se solicita el permiso de modificación de cauce.

Contacto : contacto@emergeingenieria.cl
**4**
Teléfono : +56 9 5659 1903

**2.2.** **ÁREA APORTANTE**

La delimitación del área aportante se realizó considerando como base la información topográfica disponible y la red hidrográfica definida,

con la interacción de las partes que componen el Proyecto.

En la Figura 2.2 se muestra el área aportante definida para el cauce a modificar, y en la Tabla 2.1 se resumen sus principales

características.

**Figura 2.2. Área aportante a cauce a modificar**

**Tabla 2.1. Parámetros morfométricos de áreas aportantes**

|Cuenca aportante|A (km2)<br>t|L (km)|H (m)<br>min|H (m)<br>máx|
|---|---|---|---|---|
|Área aportante C2|0,04|1,10|28,50|43,50|

Contacto : contacto@emergeingenieria.cl
**5**
Teléfono : +56 9 5659 1903

Donde:

A t : Superficie total del área aportante (km [2] )

L : Longitud cauce principal (km)

H min : Cota menor del área aportante (m)

H máx : Cota mayor del área aportante (m)

**2.3.** **CAUDALES MÁXIMOS DE CRECIDA**

En la Tabla 2.2 se muestran los resultados obtenidos de caudales máximos, utilizando el Método Racional para cuencas pequeñas.

**Tabla 2.2. Resultados de caudal máximo, Área Aportante C2**

|Periodo de retorno, T (años)|C(T)|PT (mm)<br>tc|iT (mm/h)<br>tc|Q (m3/s)<br>máximo|
|---|---|---|---|---|
|2|0,29|5,22|14,40|0,04|
|5|0,29|6,72|18,57|0,05|
|10|0,29|7,86|21,72|0,06|
|25|0,32|9,37|25,88|0,08|
|50|0,35|10,51|29,03|0,10|
|100|0,36|11,65|32,18|0,12|
|150|0,36|12,32|34,02|0,13|

Contacto : contacto@emergeingenieria.cl
**6**
Teléfono : +56 9 5659 1903

**3.** **MODELACIÓN HIDRÁULICA**

En esta etapa se contempla la caracterización de las condiciones hidráulicas que posee la zona de estudio. Esto se realiza por medio de

la modelación hidrodinámica del sistema en HEC-RAS V5.0.7.

**3.1.** **ZONA DE ANÁLISIS**

Considerando el área del Proyecto, se analiza su interacción con la lámina de inundación de los cauces identificados. Determinar las

áreas de inundación consiste en verificar la interacción de los cauces con el área del Proyecto, lo que se analiza para un periodo de

retorno de 100 y 150 años. En la Figura 3.1 se muestra la topografía disponible (curvas de nivel) y la ubicación del proyecto (para mayor

detalle revisar el _Anexo - Planos_ ).

**Figura 3.1. Topografía disponible**

Contacto : contacto@emergeingenieria.cl
**7**
Teléfono : +56 9 5659 1903

**3.2.** **METODOLOGÍA MODELACIÓN 1D**

Para definir el eje hidráulico, primero se genera un levantamiento topográfico del cauce mediante el programa Autocad Civil 3D, sobre el

levantamiento topográfico se define el trazado del eje del cauce y de sus perfiles transversales, para luego exportar esta información al

software de libre acceso HEC-RAS (Hydraulic Engineering Center - River Analysis System), desarrollado por el US Corp Engineers, el

cual resuelve la ecuación unidimensional del balance de energía, y en situaciones donde la superficie del agua varía rápidamente utiliza

la ecuación de momento.

Los datos requeridos para la modelación son:

1. Geometría del tramo del cauce por medio de secciones transversales

2. Rugosidad relativa del tramo a modelar (n de Manning)

3. Pendiente media aguas arriba y aguas abajo de la zona de interés

**3.2.1.** **Características geométricas del modelo**

En cuanto a la caracterización geométrica se utiliza el levantamiento topográfico disponible, caracterizado por medio de perfiles

transversales en sentido del escurrimiento. Los perfiles transversales fueron extraídos cada 20 m, logrando obtener una representación

adecuada de la batimetría del tramo de cauce estudiado, cada perfil cuenta con un largo variable dependiendo de la característica de las

planicies de inundación adyacentes, siempre garantizando cubrir todo el tramo del cauce inundado producto del caudal de crecida.

**3.2.2.** **Estimación del coeficiente de rugosidad**

El coeficiente de rugosidad para los cauces se obtuvo mediante el método de Cowan (1956), el cual estima el número de Manning a partir

de la separación de diversos factores, dado por la siguiente ecuación:

n = (n 0 + n 1 + n 2 + n 3 + n 4 ) ∗m 5

En la Tabla 3.1 se definen los parámetros y valores de dicha relación.

**Tabla 3.1. Definición y valores para parámetros de la ecuación de Cowan**

|Condiciones del canal|Col2|Valor|Col4|
|---|---|---|---|
|Material del lecho|Tierra|n0|0,020|
|Material del lecho|Roca cortada|Roca cortada|0,025|
|Material del lecho|Grava fina|Grava fina|0,024|
|Material del lecho|Grava gruesa|Grava gruesa|0,028|
|Grado de irregularidad perímetro mojado|Despreciable|n1|0,000|
|Grado de irregularidad perímetro mojado|Leve|Leve|0,001-0,005|
|Grado de irregularidad perímetro mojado|Moderado|Moderado|0,006-0,010|
|Grado de irregularidad perímetro mojado|Alto|Alto|0,011-0,020|

Contacto : contacto@emergeingenieria.cl
**8**
Teléfono : +56 9 5659 1903

|Condiciones del canal|Col2|Valor|Col4|
|---|---|---|---|
|Variación de las secciones|Graduales|n2|0,000|
|Variación de las secciones|Alternándose ocasionalmente|Alternándose ocasionalmente|0,001-0,005|
|Variación de las secciones|Alternándose frecuentemente|Alternándose frecuentemente|0,010-0,015|
|Efecto relativo de las obstrucciones|Despreciable|n3|0,000-0,004|
|Efecto relativo de las obstrucciones|Leve|Leve|0,005-0,015|
|Efecto relativo de las obstrucciones|Apreciable|Apreciable|0,020-0,030|
|Efecto relativo de las obstrucciones|Alto|Alto|0,040-0,060|
|Densidad de vegetación|Baja|n4|0,005-0,010|
|Densidad de vegetación|Media|Media|0,010-0,025|
|Densidad de vegetación|Alta|Alta|0,025-0,050|
|Densidad de vegetación|Muy alta|Muy alta|0,050-0,100|
|Sinuosidad y frecuencia de meandros|Leve|m5|1,000|
|Sinuosidad y frecuencia de meandros|Apreciable|Apreciable|1,150|
|Sinuosidad y frecuencia de meandros|Alto|Alto|1,300|

Fuente: Tabla 3.707.104B del Manual de Carreteras Volumen 3 (MOP, 2022).

En la Tabla 3.2 se indican los valores de los parámetros y el coeficiente de rugosidad (n) determinado mediante el método de Cowan.

**Tabla 3.2. Valores de parámetros y Manning obtenido mediante método de Cowan**

|n<br>0|n<br>1|n<br>2|n<br>3|n<br>4|m<br>5|n|
|---|---|---|---|---|---|---|
|0,020|0,005|0,005|0,000|0,005|1,150|0,040|

**3.2.3.** **Características de la modelación**

En los tramos donde no se observa la presencia de grandes obstrucciones ni cambios bruscos en el eje del flujo, se consideran los

coeficientes de contracción y expansión C CON = 0,1 y C EXP = 0,3 sugeridos por defecto en el software HEC-RAS. Las condiciones de borde

ingresadas al modelo corresponden a la pendiente normal aguas arriba y aguas abajo, con régimen de flujo mixto.

Contacto : contacto@emergeingenieria.cl
**9**
Teléfono : +56 9 5659 1903

**4.** **RESULTADOS MODELACIÓN 1D**

En la Figura 4.1 se muestran los perfiles transversales realizados y su ubicación respecto al Proyecto.

**Perfil 0**

**Perfil 340**

**Figura 4.1. Ubicación perfiles transversales asignados para la modelación hidráulica**

En la Tabla 4.1 se muestran los resultados obtenidos en los perfiles analizados, con los caudales para un periodo de retorno de 100 años,

para la situación sin y con proyecto. La situación sin proyecto considera las condiciones naturales del cauce, y la situación con proyecto

considera la construcción del canal.

Contacto : contacto@emergeingenieria.cl
**10**
Teléfono : +56 9 5659 1903

**Tabla 4.1. Resultados modelación**

|Perfil|Sin proyecto|Col3|Col4|Col5|Col6|Con proyecto|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**Perfil**|**Cota de**<br>**fondo**<br>**(m.s.n.m.)**|**Cota de agua**<br>**(m.s.n.m.)**|**Pendiente de**<br>**energía (m/m)**|**Velocidad**<br>**(m/s)**|**Fr**|**Cota de**<br>**fondo**<br>**(m.s.n.m.)**|**Cota de agua**<br>**(m.s.n.m.)**|**Pendiente de**<br>**energía (m/m)**|**Velocidad**<br>**(m/s)**|**Fr**|
|0|26,90|26,94|0,007|0,21|0,38|26,90|26,94|0,007|0,21|0,38|
|10|26,96|27,00|0,005|0,16|0,32|26,96|27,00|0,005|0,16|0,32|
|20|26,99|27,04|0,004|0,18|0,29|26,99|27,04|0,004|0,18|0,29|
|30|27,14|27,18|0,053|0,51|1,00|27,14|27,18|0,053|0,51|1,00|
|40|27,40|27,44|0,014|0,29|0,53|27,40|27,44|0,014|0,29|0,53|
|50|27,44|27,51|0,004|0,16|0,28|27,44|27,51|0,004|0,16|0,28|
|60|27,46|27,53|0,001|0,12|0,18|27,46|27,53|0,001|0,12|0,18|
|70|27,48|27,54|0,002|0,13|0,19|27,48|27,54|0,002|0,13|0,19|
|80|27,50|27,57|0,039|0,69|0,96|27,50|27,57|0,039|0,69|0,96|
|90|27,50|27,63|0,001|0,21|0,19|27,50|27,63|0,001|0,21|0,19|
|100|27,50|27,64|0,000|0,12|0,11|27,50|27,64|0,000|0,12|0,11|
|110|27,50|27,64|0,000|0,09|0,08|27,50|27,64|0,000|0,09|0,08|
|120|27,50|27,64|0,000|0,07|0,06|27,50|27,64|0,000|0,07|0,06|
|130|27,50|27,64|0,000|0,10|0,09|27,50|27,64|0,000|0,10|0,09|
|140|27,50|27,64|0,001|0,17|0,15|27,50|27,64|0,001|0,17|0,15|
|150|27,50|27,65|0,000|0,07|0,06|27,50|27,65|0,000|0,07|0,06|
|160|27,50|27,65|0,000|0,09|0,08|27,50|27,65|0,000|0,09|0,08|
|170|27,59|27,65|0,046|0,62|1,00|27,59|27,65|0,046|0,62|1,00|
|180|27,97|28,02|0,028|0,41|0,75|27,97|28,02|0,028|0,41|0,75|
|190|27,99|28,08|0,002|0,23|0,25|27,99|28,08|0,002|0,23|0,25|
|200|27,99|28,10|0,002|0,22|0,23|27,99|28,10|0,002|0,22|0,23|
|210|28,00|28,11|0,000|0,10|0,10|27,99|28,11|0,000|0,10|0,10|
|220|28,00|28,12|0,001|0,18|0,17|28,03|28,11|0,006|0,48|0,55|
|230|28,00|28,13|0,002|0,23|0,22|28,10|28,18|0,007|0,49|0,56|
|240|28,00|28,14|0,001|0,19|0,17|28,17|28,25|0,007|0,50|0,57|
|250|28,38|28,45|0,047|0,59|1,00|28,24|28,32|0,007|0,49|0,57|
|260|28,45|28,55|0,003|0,24|0,29|28,31|28,39|0,007|0,50|0,58|
|270|28,48|28,58|0,003|0,26|0,30|28,38|28,46|0,007|0,52|0,59|
|280|28,49|28,61|0,002|0,21|0,21|28,45|28,53|0,007|0,49|0,56|
|290|28,50|28,62|0,001|0,19|0,19|28,52|28,60|0,007|0,50|0,58|
|300|28,50|28,64|0,008|0,40|0,47|28,59|28,67|0,007|0,51|0,58|
|310|28,93|28,97|0,058|0,46|1,01|28,66|28,74|0,007|0,50|0,58|
|320|28,73|28,99|0,000|0,06|0,05|28,73|28,81|0,007|0,50|0,58|
|330|28,39|28,99|0,000|0,04|0,02|28,50|28,84|0,003|0,33|0,35|
|340|29,15|29,21|0,046|0,62|1,00|28,79|28,89|0,004|0,25|0,32|
|344.63|29,39|29,42|0,039|0,36|0,82|29,39|29,42|0,039|0,36|0,82|

Contacto : contacto@emergeingenieria.cl
**11**
Teléfono : +56 9 5659 1903

Finalmente, en la Figura 4.2 y Figura 4.3 se muestra el área de inundación del cauce y su relación con el área del Proyecto, para la

situación sin y con proyecto, respectivamente.

**Figura 4.2. Área de inundación cauce natural**

Contacto : contacto@emergeingenieria.cl
**12**
Teléfono : +56 9 5659 1903

**Figura 4.3. Área de inundación con canal proyectado**

Con la modelación hidráulica realizada se verifica que la construcción del canal cumple con lo requerido, que es evitar que el flujo del

cauce afecte a la plataforma del Proyecto. Destacar que el canal solo realiza un desvío del flujo, devolviéndolo al mismo cauce desde el

cual fue obtenido, por lo que se mantiene la cantidad y calidad del recurso hídrico.

Contacto : contacto@emergeingenieria.cl
**13**
Teléfono : +56 9 5659 1903

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 2.1.: Parámetros morfométricos de áreas aportantes****

| Cuenca aportante | A (km2)<br>t | L (km) | H (m)<br>min | H (m)<br>máx |
| --- | --- | --- | --- | --- |
| Área aportante C2 | 0,04 | 1,10 | 28,50 | 43,50 |

**Tabla 2.2.: Resultados de caudal máximo, Área Aportante C2****

| Periodo de retorno, T (años) | C(T) | PT (mm)<br>tc | iT (mm/h)<br>tc | Q (m3/s)<br>máximo |
| --- | --- | --- | --- | --- |
| 2 | 0,29 | 5,22 | 14,40 | 0,04 |
| 5 | 0,29 | 6,72 | 18,57 | 0,05 |
| 10 | 0,29 | 7,86 | 21,72 | 0,06 |
| 25 | 0,32 | 9,37 | 25,88 | 0,08 |
| 50 | 0,35 | 10,51 | 29,03 | 0,10 |
| 100 | 0,36 | 11,65 | 32,18 | 0,12 |
| 150 | 0,36 | 12,32 | 34,02 | 0,13 |

**Tabla 3.1.: Definición y valores para parámetros de la ecuación de Cowan****

| Condiciones del canal | Col2 | Valor | Col4 |
| --- | --- | --- | --- |
| Material del lecho | Tierra | n0 | 0,020 |
| Material del lecho | Roca cortada | Roca cortada | 0,025 |
| Material del lecho | Grava fina | Grava fina | 0,024 |
| Material del lecho | Grava gruesa | Grava gruesa | 0,028 |
| Grado de irregularidad perímetro mojado | Despreciable | n1 | 0,000 |
| Grado de irregularidad perímetro mojado | Leve | Leve | 0,001-0,005 |
| Grado de irregularidad perímetro mojado | Moderado | Moderado | 0,006-0,010 |
| Grado de irregularidad perímetro mojado | Alto | Alto | 0,011-0,020 |

**Tabla 3.2.: Valores de parámetros y Manning obtenido mediante método de Cowan****

| n<br>0 | n<br>1 | n<br>2 | n<br>3 | n<br>4 | m<br>5 | n |
| --- | --- | --- | --- | --- | --- | --- |
| 0,020 | 0,005 | 0,005 | 0,000 | 0,005 | 1,150 | 0,040 |

**Tabla 4.1.: Resultados modelación****

| Perfil | Sin proyecto | Col3 | Col4 | Col5 | Col6 | Con proyecto | Col8 | Col9 | Col10 | Col11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Perfil** | **Cota de**<br>**fondo**<br>**(m.s.n.m.)** | **Cota de agua**<br>**(m.s.n.m.)** | **Pendiente de**<br>**energía (m/m)** | **Velocidad**<br>**(m/s)** | **Fr** | **Cota de**<br>**fondo**<br>**(m.s.n.m.)** | **Cota de agua**<br>**(m.s.n.m.)** | **Pendiente de**<br>**energía (m/m)** | **Velocidad**<br>**(m/s)** | **Fr** |
| 0 | 26,90 | 26,94 | 0,007 | 0,21 | 0,38 | 26,90 | 26,94 | 0,007 | 0,21 | 0,38 |
| 10 | 26,96 | 27,00 | 0,005 | 0,16 | 0,32 | 26,96 | 27,00 | 0,005 | 0,16 | 0,32 |
| 20 | 26,99 | 27,04 | 0,004 | 0,18 | 0,29 | 26,99 | 27,04 | 0,004 | 0,18 | 0,29 |
| 30 | 27,14 | 27,18 | 0,053 | 0,51 | 1,00 | 27,14 | 27,18 | 0,053 | 0,51 | 1,00 |
| 40 | 27,40 | 27,44 | 0,014 | 0,29 | 0,53 | 27,40 | 27,44 | 0,014 | 0,29 | 0,53 |
| 50 | 27,44 | 27,51 | 0,004 | 0,16 | 0,28 | 27,44 | 27,51 | 0,004 | 0,16 | 0,28 |
| 60 | 27,46 | 27,53 | 0,001 | 0,12 | 0,18 | 27,46 | 27,53 | 0,001 | 0,12 | 0,18 |
| 70 | 27,48 | 27,54 | 0,002 | 0,13 | 0,19 | 27,48 | 27,54 | 0,002 | 0,13 | 0,19 |
| 80 | 27,50 | 27,57 | 0,039 | 0,69 | 0,96 | 27,50 | 27,57 | 0,039 | 0,69 | 0,96 |
| 90 | 27,50 | 27,63 | 0,001 | 0,21 | 0,19 | 27,50 | 27,63 | 0,001 | 0,21 | 0,19 |
| 100 | 27,50 | 27,64 | 0,000 | 0,12 | 0,11 | 27,50 | 27,64 | 0,000 | 0,12 | 0,11 |
| 110 | 27,50 | 27,64 | 0,000 | 0,09 | 0,08 | 27,50 | 27,64 | 0,000 | 0,09 | 0,08 |
| 120 | 27,50 | 27,64 | 0,000 | 0,07 | 0,06 | 27,50 | 27,64 | 0,000 | 0,07 | 0,06 |
| 130 | 27,50 | 27,64 | 0,000 | 0,10 | 0,09 | 27,50 | 27,64 | 0,000 | 0,10 | 0,09 |
| 140 | 27,50 | 27,64 | 0,001 | 0,17 | 0,15 | 27,50 | 27,64 | 0,001 | 0,17 | 0,15 |
| 150 | 27,50 | 27,65 | 0,000 | 0,07 | 0,06 | 27,50 | 27,65 | 0,000 | 0,07 | 0,06 |
| 160 | 27,50 | 27,65 | 0,000 | 0,09 | 0,08 | 27,50 | 27,65 | 0,000 | 0,09 | 0,08 |
| 170 | 27,59 | 27,65 | 0,046 | 0,62 | 1,00 | 27,59 | 27,65 | 0,046 | 0,62 | 1,00 |
| 180 | 27,97 | 28,02 | 0,028 | 0,41 | 0,75 | 27,97 | 28,02 | 0,028 | 0,41 | 0,75 |
| 190 | 27,99 | 28,08 | 0,002 | 0,23 | 0,25 | 27,99 | 28,08 | 0,002 | 0,23 | 0,25 |
| 200 | 27,99 | 28,10 | 0,002 | 0,22 | 0,23 | 27,99 | 28,10 | 0,002 | 0,22 | 0,23 |
| 210 | 28,00 | 28,11 | 0,000 | 0,10 | 0,10 | 27,99 | 28,11 | 0,000 | 0,10 | 0,10 |
| 220 | 28,00 | 28,12 | 0,001 | 0,18 | 0,17 | 28,03 | 28,11 | 0,006 | 0,48 | 0,55 |
| 230 | 28,00 | 28,13 | 0,002 | 0,23 | 0,22 | 28,10 | 28,18 | 0,007 | 0,49 | 0,56 |
| 240 | 28,00 | 28,14 | 0,001 | 0,19 | 0,17 | 28,17 | 28,25 | 0,007 | 0,50 | 0,57 |
| 250 | 28,38 | 28,45 | 0,047 | 0,59 | 1,00 | 28,24 | 28,32 | 0,007 | 0,49 | 0,57 |
| 260 | 28,45 | 28,55 | 0,003 | 0,24 | 0,29 | 28,31 | 28,39 | 0,007 | 0,50 | 0,58 |
| 270 | 28,48 | 28,58 | 0,003 | 0,26 | 0,30 | 28,38 | 28,46 | 0,007 | 0,52 | 0,59 |
| 280 | 28,49 | 28,61 | 0,002 | 0,21 | 0,21 | 28,45 | 28,53 | 0,007 | 0,49 | 0,56 |
| 290 | 28,50 | 28,62 | 0,001 | 0,19 | 0,19 | 28,52 | 28,60 | 0,007 | 0,50 | 0,58 |
| 300 | 28,50 | 28,64 | 0,008 | 0,40 | 0,47 | 28,59 | 28,67 | 0,007 | 0,51 | 0,58 |
| 310 | 28,93 | 28,97 | 0,058 | 0,46 | 1,01 | 28,66 | 28,74 | 0,007 | 0,50 | 0,58 |
| 320 | 28,73 | 28,99 | 0,000 | 0,06 | 0,05 | 28,73 | 28,81 | 0,007 | 0,50 | 0,58 |
| 330 | 28,39 | 28,99 | 0,000 | 0,04 | 0,02 | 28,50 | 28,84 | 0,003 | 0,33 | 0,35 |
| 340 | 29,15 | 29,21 | 0,046 | 0,62 | 1,00 | 28,79 | 28,89 | 0,004 | 0,25 | 0,32 |
| 344.63 | 29,39 | 29,42 | 0,039 | 0,36 | 0,82 | 29,39 | 29,42 | 0,039 | 0,36 | 0,82 |
