---
title: Sin título
author: V.Santtiz
date: D:20240528153302+02'00'
language: es
type: report
pages: 43
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ANEXO 2
-->

# ANEXO 2

## ESTUDIOS BASICOS

#### 1.- HIDRÁULICA 2.- GASTO SOLIDO 3.- SOCAVACIONES 4.- SALIDAS HEC-RAS

### VERIFICACIÓN: DEFENSA RIBERA SUR REEMPLAZA: DEFENSA RIBERAS SUR Y NORTE

## RIO ELQUI - SECTOR RUTA 5 - DESEMBOCADURA

### TRAMO 570 METROS RIBERA SUR PUENTE RUTA 5 NORTE HACIA AGUAS ABAJO

#### COMUNA DE LA SERENA, IV REGION DE COQUIMBO MAYO 2024

**VICTOR SANTTIZ GARCIA - INGENIERO CIVIL**

[victor.santtiz@gmail.com - Whatsapp: +39 351 644 6334 +56 99 252 4610](mailto:victor.santtiz@gmail.com)

**PROYECTO DEFENSAS FLUVIALES RIO ELQUI. VERIFICACIÓN DEFENSA RIBERA SUR**

**SECTOR RUTA 5 - DESEMBOCADURA RIO ELQUI** ANEXO 2 - ESTUDIOS BASICOS

#### I N D I C E

**ANALISIS HIDRAULICO ..................................................................................................... 4**

1.1 Metodología ........................................................................................................................... 4

1.2 Parámetros Básicos Para El Cálculo ....................................................................................... 4

1.2.1. Caudales de Crecida ........................................................................................................ 4

1.2.2. Secciones Transversales del Cauce ................................................................................. 5

1.2.3. Coeficientes de Rugosidad .............................................................................................. 5

1.2.4. Condiciones de Borde ..................................................................................................... 5

1.3 Modelación ............................................................................................................................ 5

1.3.1. Tablas de Resultados de Parámetros Hidráulicos principales TR= 100 años .................. 6
1.3.2. Análisis del escurrimiento según TABLA 1-2 y TABLA 1-3 anteriores. ........................ 11
1.3.3. Parámetros escurrimiento. Compara SIN vs CON Proyecto ......................................... 11
1.3.4. Parámetros Hidráulicos principales en Puente Ruta 5 Norte. TR= 100 años. .............. 13
1.3.5. TR= 10 y 2 años. Parámetros Hidráulicos principales. ................................................. 14

**ANALISIS DE GASTO SÒLIDO ...........................................................................................18**

2.1 Datos para el cálculo ............................................................................................................ 18
2.2 Aplicación ............................................................................................................................. 18

2.3 Tablas de Resultados de GASTO SOLIDO ............................................................................ 19

**CÁLCULO DE SOCAVACIONES ..........................................................................................26**

3.1 Resultados de Socavación General ...................................................................................... 26

**SALIDAS HEC RAS - SECCIONES TRANSVERSALES SIN Y CON PROYECTO ..........................33**

4.1 SALIDAS HEC RAS - SECCIONES TRANSVERSALES SIN PROYECTO ....................................... 34

4.2 SALIDAS HEC RAS - SECCIONES TRANSVERSALES CON PROYECTO ..................................... 39

victor **.** santtiz@gmail.com - Whatsapp: +39 351 644 6334 +56 99 252 4610 Pág. 2 de 43

**PROYECTO DEFENSAS FLUVIALES RIO ELQUI. VERIFICACIÓN DEFENSA RIBERA SUR**

**SECTOR RUTA 5 - DESEMBOCADURA RIO ELQUI** **ANEXO 2**

#### - I N D I C E TABLAS

TABLA 1-1 Caudales máximos (m3/s) - Río ELQUI en puente Ruta 5 Norte. ............................... 4
TABLA 1-2 Parámetros Hidráulicos. SIN Proyecto T= 100 años (Q=1550 m3/s) ....................... 7
TABLA 1-3 Parámetros Hidráulicos. CON Proyecto T= 100 años (Q=1550 m3/s) .................... 9
TABLA 1-4 COMPARA Parámetros Hidráulicos. T= 100 años (Q=1550 m3/s) .......................... 12

TABLA 1-5 Parámetros Hidráulicos TR 100 años. Puente Ruta 5 Norte .................................... 13

TABLA 1-6 Parámetros Hidráulicos. SIN Proyecto - T= 10 y 2 años ......................................... 14
TABLA 1-7 Parámetros Hidráulicos. T= 10 y 2 años - CON Proyecto ......................................... 16
TABLA 2-1 GASTO SÓLIDO GS - TR= 100 años - SIN Proyecto ................................................... 20
TABLA 2-2 GASTO SÓLIDO GS - TR= 100 años - CON Proyecto ................................................. 21
TABLA 2-3 Gasto Sólido GS - TR= 10 años - SIN Proyecto ........................................................ 22
TABLA 2-4 Gasto Sólido GS - TR= 10 años - CON Proyecto ...................................................... 23
TABLA 2-5 Gasto Sólido GS - TR= 2 años - SIN Proyecto ........................................................... 24
TABLA 2-6 Gasto Sólido GS - TR= 2 años - CON Proyecto ......................................................... 25
TABLA 3-1 Socavación General; Tr=100 años - SIN Proyecto ..................................................... 27
TABLA 3-2 Socavación General; Tr=100 años - CON Proyecto .................................................. 28
TABLA 3-3 Socavación General; Tr= 10 años - SIN Proyecto ..................................................... 29
TABLA 3-4 Socavación General; Tr= 10 años - CON Proyecto .................................................. 30
TABLA 3-5 Socavación General; Tr= 2 años - SIN Proyecto ....................................................... 31
TABLA 3-6 Socavación General; Tr= 2 años- CON Proyecto ..................................................... 32

FIGURA 1-1 Sección Tipo. ............................................................................................................ 5

victor **.** santtiz@gmail.com - Whatsapp: +39 351 644 6334 +56 99 252 4610 Pág. 3 de 43

**PROYECTO DEFENSAS FLUVIALES RIO ELQUI. VERIFICACIÓN DEFENSA RIBERA SUR**

**SECTOR RUTA 5 - DESEMBOCADURA RIO ELQUI** ANEXO 2 - EST. BASICOS-HIDRAULICA

**ANALISIS HIDRAULICO**

Se determinan los parámetros hidráulicos que permitan verificar la cota de coronamiento del
pretil de encauzamiento en 570 m longitud, a partir del Puente Ruta 5 Norte hacia aguas abajo. Se
consideran crecidas de los períodos de retorno correspondientes a TR = 100, 10 y 2 años.

Se analizan 3 situaciones

i. Situación Actual: Longitud tramo = 2,550 Km.

En Plano: Km 0+150 al Km 2+700

ii. Situación Futura: Implementa Pretil en ribera SUR
Longitud = 570 m desde puente Ruta 5 Norte hacia aguas abajo.

En Plano: Km 1+750 al Km 1+180

Existen 3 puentes: Km 1+770. Puente Ruta 5 Norte

Km 1+980. Puente Ex Ruta 5 Norte

Km 2+095. Puente FFCC

**Observaciones:**

La línea de mar en desembocadura se ubica aproximadamente en Sección transversal Km

Km 0+150.

_La longitud del pretil es de 570 metros_, se inicia por _aguas arriba en sección Km 1+750_ en

estribo sur-poniente del puente Ruta 5 Norte y por _aguas abajo en Km 1+180_
**1.1** **Metodología**

Para la estimación de los ejes hidráulicos en las secciones del cauce, se utilizó el software de
modelación HEC-RAS, software elaborado por el “U.S, Army Corps Engineers”, cuyas relaciones se
presentan en el Informe Memoria del presente informe.

**1.2** **Parámetros Básicos Para El Cálculo**

1.2.1. Caudales de Crecida

Se utilizan los Caudales de tabla siguiente, extraídos de Tabla 4.10. de Anexo Hidrología.

**TABLA 1-1 Caudales máximos (m3/s) - Río ELQUI en puente Ruta 5 Norte.**

|Tr (años)|2|5|10|25|50|100|
|---|---|---|---|---|---|---|
|**Q (m3/s)**|85|215|350|600|860|**1550**|

victor **.** santtiz@gmail.com - Whatsapp: +39 351 644 6334 +56 99 252 4610 Pág. 4 de 43

**PROYECTO DEFENSAS FLUVIALES RIO ELQUI. VERIFICACIÓN DEFENSA RIBERA SUR**

**SECTOR RUTA 5 - DESEMBOCADURA RIO ELQUI** ANEXO 2 - EST. BASICOS-HIDRAULICA

1.2.2. Secciones Transversales del Cauce

En base a la información del levantamiento se Modeló una longitud de 2550 m medidos por el Eje
del cauce generándose 55 perfiles transversales cada 50 m. que abarcan el ancho de la caja del
río. En los tramos vecinos a puentes se consideran perfiles adicionales.

1.2.3. Coeficientes de Rugosidad

Se obtienen en base a la relación de COWAN (Hidráulica de los Canales Abiertos “, Ven Te Chow,
1982, tabla 5-5), Coef. Rugosidad N, con valores de 0.030 y 0.040 correspondientes al lecho de
cauce y planicie de inundación respectivamente, según se indica en Informe principal.

1.2.4. Condiciones de Borde

 - Aguas arriba: Las condiciones de Borde de aguas arriba, considera pend. media = 0,004.

 - Aguas abajo: La condición de borde de aguas abajo que corresponde a la desembocadura,

está condicionada por las mareas. No obstante, se utiliza la altura de partida es la normal,
con una pendiente 0.001, por resultar mayor a la altura de mareas.

**1.3** **Modelación**

Se realiza la modelación para las situaciones Sin y Con Proyecto. La situación Con proyecto
considera el Muro de Defensa como un Pretil por la ribera norte entre Km 1.180 al Km 1.740.

La sección tipo del Tramo Modificado, tiene la forma siguiente:

**FIGURA 1-1 Sección Tipo.**

victor **.** santtiz@gmail.com - Whatsapp: +39 351 644 6334 +56 99 252 4610 Pág. 5 de 43

**PROYECTO DEFENSAS FLUVIALES RIO ELQUI. VERIFICACIÓN DEFENSA RIBERA SUR**

**SECTOR RUTA 5 - DESEMBOCADURA RIO ELQUI** ANEXO 2 - EST. BASICOS-HIDRAULICA

1.3.1. Tablas de Resultados de Parámetros Hidráulicos principales TR= 100 años

Las características hidráulicas principales que arroja la modelación con la metodología utilizada,
se entregan en formato del software de modelación HEC-RAS en tablas siguientes, presentadas
desde aguas arriba hacia abajo.

TR= 100 años. Parámetros Hidráulicos principales tramo estudiado.
SIN Proyecto: TABLA 1-2 y CON Proyecto: TABLA 1-3
Se muestran en toda la longitud analizada.

Tramo L= 2.550 m. Km 2+700 hasta Km 0+150.

Corresponden a 57 secciones transversales.
Tramo Proyecto: L= 570 m. Km 1+750 al Km 1+180
Secciones con escurrimiento supercrítico: marcado con letra color rojo

Notas comunes:

Zona sombreada con color naranjo claro, es Tramo de Proyecto

victor **.** santtiz@gmail.com - Whatsapp: +39 351 644 6334 +56 99 252 4610 Pág. 6 de 43

**PROYECTO DEFENSAS FLUVIALES RIO ELQUI. VERIFICACIÓN DEFENSA RIBERA SUR**

**SECTOR RUTA 5 - DESEMBOCADURA RIO ELQUI** ANEXO 2 - EST. BASICOS-HIDRAULICA

|TABLA 1-2 Parámetros Hidráulicos. SIN Proyecto T= 100 años (Q=1550 m3/s)|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|River<br>Sta<br>|Min Ch<br>El|W.S.<br>Elev|Crit W.S.|E.G. Elev|E.G.<br>Slope|Vel Chnl|Flow<br>Area|Top W<br>Chnl|Froude<br># Chl|Hydr<br>Radius C|
||(m)|(m)|(m)|(m)|(m/m)|(m/s)|(m2)|(m)||(m)|
|HEC-RAS Plan: Plan 01 River: ACTUAL Reach: EJE_RIO_ELQUI<br># River Stations = 57|HEC-RAS Plan: Plan 01 River: ACTUAL Reach: EJE_RIO_ELQUI<br># River Stations = 57|HEC-RAS Plan: Plan 01 River: ACTUAL Reach: EJE_RIO_ELQUI<br># River Stations = 57|HEC-RAS Plan: Plan 01 River: ACTUAL Reach: EJE_RIO_ELQUI<br># River Stations = 57|HEC-RAS Plan: Plan 01 River: ACTUAL Reach: EJE_RIO_ELQUI<br># River Stations = 57|HEC-RAS Plan: Plan 01 River: ACTUAL Reach: EJE_RIO_ELQUI<br># River Stations = 57|HEC-RAS Plan: Plan 01 River: ACTUAL Reach: EJE_RIO_ELQUI<br># River Stations = 57|HEC-RAS Plan: Plan 01 River: ACTUAL Reach: EJE_RIO_ELQUI<br># River Stations = 57|HEC-RAS Plan: Plan 01 River: ACTUAL Reach: EJE_RIO_ELQUI<br># River Stations = 57|HEC-RAS Plan: Plan 01 River: ACTUAL Reach: EJE_RIO_ELQUI<br># River Stations = 57|HEC-RAS Plan: Plan 01 River: ACTUAL Reach: EJE_RIO_ELQUI<br># River Stations = 57|
|2,700|10.73|14.98|14.98|16.05|0.00486|4.80|288|97|0.89|2.97|
|2,650|10.62|13.89|14.35|15.62|0.01213|5.83|265|132|1.31|2.00|
|2,600|10.36|14.25|14.14|15.21|0.00518|4.38|346|140|0.89|2.46|
|2,550|10.09|14.11|13.89|14.91|0.00480|3.98|388|171|0.84|2.26|
|2,500|10.02|14.05|13.65|14.64|0.00348|3.45|442|190|0.72|2.32|
|2,450|9.91|13.68|13.54|14.42|0.00508|3.83|400|196|0.85|2.04|
|2,400|9.75|13.71|13.15|14.16|0.00254|3.10|452|180|0.62|2.51|
|2,350|9.58|13.79|12.59|14.02|0.00105|2.17|654|229|0.41|2.85|
|2,300|9.41|13.77|12.69|13.96|0.00085|2.02|691|230|0.37|3.00|
|2,250|9.21|13.77|12.27|13.91|0.00056|1.71|890|280|0.31|3.17|
|2,200|8.99|13.68|11.84|13.88|0.00063|1.98|751|207|0.33|3.62|
|2,160|8.57|13.49|11.94|13.83|0.00107|2.63|565|150|0.43|3.76|
|2,110|8.02|13.35|11.59|13.77|0.00108|2.91|521|120|0.45|4.32|
|**2,095**|||||||||||
|**2,080**|7.64|10.70|11.48|13.33|0.01761|7.24|210|99|1.59|2.09|
|**2,060**|7.33|10.21|11.02|12.96|0.01817|7.36|210|100|1.62|2.09|
|**2,035**|6.90|9.94|10.66|12.46|0.01611|7.05|219|102|1.53|2.15|
|1,990|6.49|11.26|10.50|12.06|0.00275|3.97|390|114|0.68|3.41|
|**1,980**|||||||||||
|**1,970**|6.28|10.00|10.51|11.98|0.01358|6.24|247|120|1.39|2.04|
|**1,900**|5.27|8.73|9.39|10.94|0.01561|6.65|227|112|1.49|2.02|
|1,850|4.95|9.60|8.70|10.23|0.00222|3.56|427|125|0.61|3.41|
|1,800|4.59|9.67|8.38|10.08|0.00149|2.82|546|167|0.50|3.25|
|**1770**|4.42|9.35|8.38|9.97|0.00290|3.49|449|130|0.55|2.72|
|1750|4.31|9.34|8.09|9.88|0.00198|3.30|470|126|0.53|3.47|
|1,740|4.25|9.33|7.95|9.84|0.00152|3.20|481|124|0.52|3.85|
|1,700|4.12|9.22|7.82|9.78|0.00151|3.36|446|106|0.52|4.19|
|1,650|4.00|7.98|7.95|9.55|0.00531|5.64|264|74|0.96|3.54|
|1,600|3.97|7.70|7.70|9.28|0.00562|5.65|263|77|0.98|3.40|
|**1,550**|3.57|7.04|7.60|8.89|0.00963|6.10|248|97|1.21|2.54|

victor **.** santtiz@gmail.com - Whatsapp: +39 351 644 6334 +56 99 252 4610 Pág. 7 de 43

**PROYECTO DEFENSAS FLUVIALES RIO ELQUI. VERIFICACIÓN DEFENSA RIBERA SUR**

**SECTOR RUTA 5 - DESEMBOCADURA RIO ELQUI** ANEXO 2 - EST. BASICOS-HIDRAULICA

|TABLA 1-2 Parámetros Hidráulicos. SIN Proyecto T= 100 años (Q=1550 m3/s)|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|River<br>Sta<br>|Min Ch<br>El|W.S.<br>Elev|Crit W.S.|E.G. Elev|E.G.<br>Slope|Vel Chnl|Flow<br>Area|Top W<br>Chnl|Froude<br># Chl|Hydr<br>Radius C|
||(m)|(m)|(m)|(m)|(m/m)|(m/s)|(m2)|(m)||(m)|
|1,500|3.35|7.87|7.33|8.39|0.00225|3.49|354|107|0.61|3.28|
|1,450|3.37|7.85|6.81|8.27|0.00155|3.11|405|111|0.52|3.65|
|1,400|2.99|7.64|6.93|8.16|0.00233|3.28|442|151|0.61|2.91|
|1,350|2.22|7.12|7.08|7.98|0.00407|4.28|331|115|0.81|2.86|
|**1,300**|2.37|7.21|6.80|7.71|0.00265|3.30|423|158|0.64|2.67|
|1,250|2.26|6.86|6.86|7.52|0.00520|3.77|364|185|0.86|1.96|
|**1,200 **|2.12|6.37|6.40|7.19|0.00776|4.04|371|230|1.01|1.61|
|1,180|1.95|6.27|6.35|7.08|0.0062|4.20|333|174|0.93|2.19|
|1,150|1.70|6.11|6.28|6.91|0.00399|4.43|276|90|0.81|3.05|
|1,100|1.46|5.45|5.74|6.63|0.00639|5.22|244|88|1.00|2.74|
|**1,050**|1.44|5.22|5.43|6.23|0.00750|4.75|280|133|1.04|2.11|
|1,000|1.42|5.45|4.99|5.80|0.00241|2.72|503|235|0.59|2.14|
|950|1.46|5.08|4.95|5.61|0.00469|3.35|425|239|0.80|1.78|
|900|1.31|5.12|4.67|5.30|0.00180|2.07|620|350|0.50|1.77|
|850|1.42|4.85|4.43|5.18|0.00263|2.93|362|161|0.62|2.24|
|800|1.26|4.66|4.39|5.04|0.00296|3.11|357|159|0.66|2.24|
|750|0.87|4.61|4.28|4.88|0.00208|2.57|458|208|0.55|2.19|
|700|0.77|4.54|4.12|4.78|0.00163|2.50|429|170|0.50|2.52|
|650|0.69|4.16|4.16|4.64|0.00354|3.39|365|162|0.72|2.24|
|600|0.64|4.07|3.80|4.42|0.00271|2.91|403|186|0.63|2.17|
|550|0.98|3.96|3.62|4.28|0.00250|2.83|413|186|0.61|2.22|
|500|1.00|3.89|3.38|4.15|0.00195|2.47|515|237|0.53|2.17|
|450|0.92|3.87|3.16|4.05|0.00132|2.04|597|273|0.44|2.19|
|400|0.70|3.83|3.06|3.98|0.00119|1.93|523|240|0.42|2.17|
|350|0.47|3.81|0.00|3.92|0.00083|1.62|664|304|0.35|2.19|
|300|0.49|3.77|0.00|3.88|0.00079|1.54|821|389|0.34|2.11|
|250|0.59|3.73|0.00|3.84|0.00077|1.50|911|440|0.33|2.07|
|200|0.68|3.66|0.00|3.79|0.00098|1.69|775|377|0.37|2.06|
|150|0.74|3.62|2.74|3.74|0.00100|1.62|854|449|0.37|1.90|

victor **.** santtiz@gmail.com - Whatsapp: +39 351 644 6334 +56 99 252 4610 Pág. 8 de 43

**PROYECTO DEFENSAS FLUVIALES RIO ELQUI. VERIFICACIÓN DEFENSA RIBERA SUR**

**SECTOR RUTA 5 - DESEMBOCADURA RIO ELQUI** ANEXO 2 - EST. BASICOS-HIDRAULICA

|TABLA 1-3 Parámetros Hidráulicos. CON Proyecto T= 100 años (Q=1550 m3/s)|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|River<br>Sta<br>|Min Ch<br>El|W.S.<br>Elev|Crit W.S.|E.G. Elev|E.G. Slope|Vel<br>Chnl|Flow<br>Area|Top W<br>Chnl|Froude<br># Chl|Hydr<br>Radius C|
||(m)|(m)|(m)|(m)|(m/m)|(m/s)|(m2)|(m)||(m)|
|HEC-RAS Plan: River: PROYECTO Reach: RIO ELQUI<br># River Stations = 57|HEC-RAS Plan: River: PROYECTO Reach: RIO ELQUI<br># River Stations = 57|HEC-RAS Plan: River: PROYECTO Reach: RIO ELQUI<br># River Stations = 57|HEC-RAS Plan: River: PROYECTO Reach: RIO ELQUI<br># River Stations = 57|HEC-RAS Plan: River: PROYECTO Reach: RIO ELQUI<br># River Stations = 57|HEC-RAS Plan: River: PROYECTO Reach: RIO ELQUI<br># River Stations = 57|HEC-RAS Plan: River: PROYECTO Reach: RIO ELQUI<br># River Stations = 57|HEC-RAS Plan: River: PROYECTO Reach: RIO ELQUI<br># River Stations = 57|HEC-RAS Plan: River: PROYECTO Reach: RIO ELQUI<br># River Stations = 57|HEC-RAS Plan: River: PROYECTO Reach: RIO ELQUI<br># River Stations = 57|HEC-RAS Plan: River: PROYECTO Reach: RIO ELQUI<br># River Stations = 57|
|2700|10.73|14.97|14.97|16.05|0.0049|4.80|288|97|0.89|2.97|
|2650|10.62|13.89|14.35|15.62|0.0121|5.83|265|132|1.31|2.00|
|2600|10.36|14.25|14.14|15.21|0.0052|4.38|346|140|0.89|2.46|
|2550|10.09|14.11|13.89|14.91|0.0048|3.98|388|171|0.84|2.26|
|2500|10.02|14.05|13.65|14.64|0.0035|3.45|443|190|0.72|2.33|
|2450|9.91|13.68|13.54|14.42|0.0051|3.83|400|196|0.85|2.04|
|2400|9.75|13.70|13.15|14.16|0.0026|3.11|451|180|0.63|2.51|
|2350|9.58|13.79|12.59|14.02|0.0010|2.17|654|229|0.41|2.85|
|2300|9.41|13.77|12.69|13.96|0.0008|2.01|691|230|0.37|3.00|
|2250|9.21|13.77|12.27|13.91|0.0006|1.71|890|280|0.31|3.17|
|2200|8.99|13.68|11.84|13.88|0.0006|1.98|751|207|0.33|3.62|
|2160|8.57|13.49|11.94|13.83|0.0011|2.63|565|150|0.43|3.76|
|2110|8.02|13.35|11.59|13.77|0.0011|2.91|521|120|0.45|4.32|
|2095|||||||||||
|2080|7.64|10.70|11.48|13.33|0.0176|7.24|210|99|1.59|2.09|
|2060|7.33|10.21|11.02|12.96|0.0182|7.36|210|100|1.62|2.10|
|2035|6.90|9.94|10.66|12.46|0.01611|7.05|219|102|1.53|2.15|
|1990|6.49|11.26|10.50|12.06|0.0028|3.97|390|114|0.68|3.41|
|1980|||||||||||
|1970|6.28|10.00|10.51|11.98|0.0136|6.24|247|120|1.39|2.04|
|1900|5.27|8.73|9.39|10.94|0.0156|6.65|227|112|1.49|2.02|
|1+850|4.95|9.30|8.70|10.08|0.0031|3.94|389|125|0.71|3.11|
|1+800|4.59|9.37|8.38|9.87|0.0021|3.11|496|168|0.58|2.94|
|**1+770**|4.42|8.96|8.24|9.66|0.00397|3.69|428|142|0.55|2.44|
|1+750|4.31|9.05|7.86|9.53|0.00217|3.06|517|153|0.50|3.16|
|1+740|4.25|9.09|7.67|9.47|0.0013|2.75|562|159|0.47|3.52|
|1+700|4.12|8.93|7.62|9.41|0.0015|3.08|492|132|0.51|3.73|
|1+650|4.00|8.16|7.72|9.24|0.0037|4.65|323|93|0.80|3.47|
|1+600|3.97|7.54|7.52|8.97|0.0059|5.37|281|92|0.98|3.04|
|1+550|3.57|7.57|7.46|8.60|0.0044|4.62|316|103|0.84|3.05|

victor **.** santtiz@gmail.com - Whatsapp: +39 351 644 6334 +56 99 252 4610 Pág. 9 de 43

**PROYECTO DEFENSAS FLUVIALES RIO ELQUI. VERIFICACIÓN DEFENSA RIBERA SUR**

**SECTOR RUTA 5 - DESEMBOCADURA RIO ELQUI** ANEXO 2 - EST. BASICOS-HIDRAULICA

|TABLA 1-3 Parámetros Hidráulicos. CON Proyecto T= 100 años (Q=1550 m3/s)|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|River<br>Sta<br>|Min Ch<br>El|W.S.<br>Elev|Crit W.S.|E.G. Elev|E.G. Slope|Vel<br>Chnl|Flow<br>Area|Top W<br>Chnl|Froude<br># Chl|Hydr<br>Radius C|
||(m)|(m)|(m)|(m)|(m/m)|(m/s)|(m2)|(m)||(m)|
|1+500|3.35|7.77|7.25|8.29|0.0023|3.45|371|117|0.62|3.14|
|1+450|3.37|7.79|6.71|8.15|0.0014|2.87|442|125|0.49|3.52|
|1+400|2.99|7.54|6.83|8.05|0.0023|3.22|463|164|0.61|2.82|
|1+350|2.22|7.10|6.93|7.88|0.0036|4.01|366|129|0.76|2.83|
|1+300|2.37|7.13|6.69|7.64|0.0027|3.28|435|166|0.65|2.61|
|1+250|2.26|6.78|6.78|7.44|0.0051|3.72|387|198|0.85|1.95|
|1+200|2.12|6.42|6.30|7.09|0.0057|3.63|423|245|0.88|1.73|
|1+180|1.95|6.35|6.28|7.00|0.0046|3.75|372|183|0.80|2.35|
|1+150|1.70|6.25|6.25|6.86|0.0029|3.94|296|90|0.69|3.27|
|1+100|1.46|5.47|5.72|6.61|0.0062|5.17|245|88|0.99|2.76|
|**1050**|1.44|5.23|5.44|6.23|0.0074|4.73|281|133|1.04|2.11|
|1000|1.42|5.47|4.99|5.81|0.0023|2.69|508|235|0.58|2.16|
|950|1.46|4.95|4.95|5.60|0.0062|3.66|395|239|0.91|1.65|
|900|1.31|5.11|4.67|5.30|0.0018|2.07|619|350|0.50|1.77|
|850|1.42|4.85|4.43|5.18|0.0026|2.92|362|161|0.62|2.24|
|800|1.26|4.66|4.39|5.04|0.0030|3.10|357|159|0.66|2.24|
|750|0.87|4.61|4.28|4.88|0.0021|2.57|458|208|0.55|2.19|
|700|0.77|4.54|4.12|4.78|0.0016|2.50|429|170|0.50|2.52|
|650|0.69|4.16|4.16|4.64|0.0035|3.39|365|162|0.72|2.24|
|600|0.64|4.07|3.85|4.42|0.0027|2.92|403|186|0.63|2.17|
|550|0.98|3.96|3.62|4.28|0.0024|2.81|414|186|0.60|2.22|
|500|1.00|3.89|3.38|4.16|0.0020|2.47|515|237|0.54|2.17|
|450|0.92|3.87|3.15|4.05|0.0014|2.07|596|273|0.45|2.18|
|400|0.70|3.83|3.06|3.98|0.0012|1.93|523|240|0.42|2.17|
|350|0.47|3.81|0.00|3.92|0.0008|1.62|664|304|0.35|2.19|
|300|0.49|3.77|0.00|3.88|0.0008|1.54|821|389|0.34|2.11|
|250|0.59|3.73|0.00|3.84|0.0008|1.50|911|440|0.33|2.07|
|200|0.68|3.66|0.00|3.79|0.0010|1.69|775|377|0.37|2.06|
|150|0.74|3.62|2.74|3.74|0.0010|1.6200|853.77|449|0.37|1.90|

victor **.** santtiz@gmail.com - Whatsapp: +39 351 644 6334 +56 99 252 4610 Pág. 10 de 43

**PROYECTO DEFENSAS FLUVIALES RIO ELQUI. VERIFICACIÓN DEFENSA RIBERA SUR**

**SECTOR RUTA 5 - DESEMBOCADURA RIO ELQUI** ANEXO 2 - EST. BASICOS-HIDRAULICA

1.3.2. Análisis del escurrimiento según TABLA 1-2 y TABLA 1-3 anteriores.

En toda la longitud analizada en las situaciones Sin y Con proyecto, se aprecian diferencias entre

las secciones transversales _**Km 1+850 al Km 0+900**_ .

En base al No de Froude, se aprecia escurrimiento muy similar en las situaciones SIN y CON
proyecto, caracterizados por presentar régimen sub-crítico o de río en la mayor parte de la
longitud analizada.

Excepcionalmente se verifica régimen de torrente solo en 8 secciones en situación Sin Proyecto y
en 6 secciones en situación Con Proyecto (Km marcados en color rojo), que se producen
preferentemente aguas abajo de los puentes FFCC y Ex Ruta 5 produciendo en general régimen
mixto. Se muestran estas secciones (en torrente) en color rojo en ambas tablas.

1.3.3. Parámetros escurrimiento. Compara SIN vs CON Proyecto

En TABLA 1-4 COMPARA Parámetros Hidráulicos. T= 100 años (Q=1550 m3/s) de algunas
características hidráulicas principales del escurrimiento que se producen en escurrimiento CON
Proyecto menos SIN Proyecto, dada por las diferencias de valores en dichos parámetros,
mostradas en las respectivas columnas “ **DIFERENCIA”** dentro de una misma sección y representan
en esa sección que el proyecto genera impacto.

Para análisis se considera un tramo mayor al influenciado, desde Km 1+970 a Km 0+800

victor **.** santtiz@gmail.com - Whatsapp: +39 351 644 6334 +56 99 252 4610 Pág. 11 de 43

**PROYECTO DEFENSAS FLUVIALES RIO ELQUI. VERIFICACIÓN DEFENSA RIBERA SUR**

**SECTOR RUTA 5 - DESEMBOCADURA RIO ELQUI** ANEXO 2 - EST. BASICOS-HIDRAULICA

**TABLA 1-4 COMPARA Parámetros Hidráulicos. T= 100 años (Q=1550 m3/s)**

|River<br>Sta|Eje Hidráulico (msnm)|Col3|Col4|Velocidad Canal Principal<br>(m/s)|Col6|Col7|Ancho Superficial Canal<br>principal (m)|Col9|Col10|No de Froude Canal<br>principa|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**River**<br>**Sta**|**SIN**<br>**Proy**|**CON**<br>**Proy**|**DIFERENCIA**|**SIN**<br>**Proy**|**CON**<br>**Proy**|**DIFERENCIA**|**SIN**<br>**Proy**|**CON**<br>**Proy**|**DIFERENCIA**|**SIN**<br>**Proy**|**CON**<br>**Proy**|**DIFERENCIA**|
|1,970|10.00|10.00|**0.00**|6.24|6.24|**0.00**|120|120|**0.00**|1.39|1.39|**0.00**|
|1,900|8.73|8.73|**0.00**|6.65|6.65|**0.00**|112|112|**0.00**|1.49|1.49|**0.00**|
|1,850|9.60|9.30|-0.30|3.56|3.94|0.38|125|125|0.00|0.61|0.71|0.10|
|1,800|9.67|9.37|-0.30|2.82|3.11|0.29|167|168|0.81|0.50|0.58|0.08|
|1,770|9.35|8.96|-0.40|3.49|3.69|0.20|130|142|11.94|0.55|0.55|0.01|
|1,750|9.34|9.05|-0.29|3.30|3.06|-0.24|126|153|27.42|0.53|0.50|-0.03|
|1,740|9.33|9.09|-0.24|3.20|2.75|-0.45|124|159|35.16|0.52|0.47|-0.05|
|1,700|9.22|8.93|-0.29|3.36|3.08|-0.28|106|132|25.56|0.52|0.51|-0.01|
|1,650|7.98|8.16|0.18|5.64|4.65|-0.99|74|93|18.45|0.96|0.80|-0.16|
|1,600|7.70|7.54|-0.16|5.65|5.37|-0.28|77|92|15.00|0.98|0.98|0.00|
|1,550|7.04|7.57|0.53|6.10|4.62|-1.48|97|103|6.10|1.21|0.84|-0.37|
|1,500|7.87|7.77|-0.10|3.49|3.45|-0.04|107|117|9.94|0.61|0.62|0.01|
|1,450|7.85|7.79|-0.06|3.11|2.87|-0.24|111|125|14.07|0.52|0.49|-0.03|
|1,400|7.64|7.54|-0.10|3.28|3.22|-0.06|151|164|12.36|0.61|0.61|0.00|
|1,350|7.12|7.10|-0.02|4.28|4.01|-0.27|115|129|13.49|0.81|0.76|-0.05|
|1,300|7.21|7.13|-0.08|3.30|3.28|-0.02|158|166|7.90|0.64|0.65|0.01|
|1,250|6.86|6.78|-0.08|3.77|3.72|-0.05|185|198|12.99|0.86|0.85|-0.01|
|1,200|6.37|6.42|0.05|4.04|3.63|-0.41|230|245|14.71|1.01|0.88|-0.13|
|1,180|6.27|6.35|0.09|4.20|3.75|-0.44|174|183|8.83|0.93|0.80|-0.13|
|1,150|6.11|6.25|0.14|4.43|3.94|-0.49|90|90|0.00|0.81|0.69|-0.12|
|1,100|5.45|5.47|0.02|5.22|5.17|-0.05|88|88|0.00|1.00|0.99|-0.01|
|1,050|5.22|5.23|0.01|4.75|4.73|0.01|133|133|0.00|1.04|1.04|0.00|
|1,000|5.45|5.47|0.02|2.72|2.69|0.02|235|235|0.00|0.59|0.58|-0.01|
|950|5.08|4.95|-0.13|3.35|3.66|-0.13|239|239|0.00|0.80|0.91|0.11|
|900|5.12|5.11|-0.01|2.07|2.07|-0.01|350|350|0.00|0.50|0.50|0.00|
|850|4.85|4.85|**0.00**|2.93|2.92|**0.00**|161|161|**0.00**|0.62|0.62|**0.00**|
|800|4.66|4.66|**0.00**|3.11|3.10|**0.00**|159|159|**0.00**|0.66|0.66|**0.00**|
||||||||||||||
|PROMEDIO EN TRAMO DEFENSA Km 1+750 al Km 1+180 = 570 metros|PROMEDIO EN TRAMO DEFENSA Km 1+750 al Km 1+180 = 570 metros|PROMEDIO EN TRAMO DEFENSA Km 1+750 al Km 1+180 = 570 metros|PROMEDIO EN TRAMO DEFENSA Km 1+750 al Km 1+180 = 570 metros|PROMEDIO EN TRAMO DEFENSA Km 1+750 al Km 1+180 = 570 metros|PROMEDIO EN TRAMO DEFENSA Km 1+750 al Km 1+180 = 570 metros|PROMEDIO EN TRAMO DEFENSA Km 1+750 al Km 1+180 = 570 metros|PROMEDIO EN TRAMO DEFENSA Km 1+750 al Km 1+180 = 570 metros|PROMEDIO EN TRAMO DEFENSA Km 1+750 al Km 1+180 = 570 metros|PROMEDIO EN TRAMO DEFENSA Km 1+750 al Km 1+180 = 570 metros|PROMEDIO EN TRAMO DEFENSA Km 1+750 al Km 1+180 = 570 metros|PROMEDIO EN TRAMO DEFENSA Km 1+750 al Km 1+180 = 570 metros|PROMEDIO EN TRAMO DEFENSA Km 1+750 al Km 1+180 = 570 metros|
|Prom|7.70|**7.66**|-0.04|4.05|**3.68 **|-0.37|131|**147**|15.86|0.76|**0.70**|-0.07|
||||**-0.5%**|||**-9.3%**|||**12.1%**|||**-8.8%**|
||||||||||||||
|PROMEDIO EN TRAMO AGUAS ARRIBA Km 1+850 a 1+750 = 100 metros|PROMEDIO EN TRAMO AGUAS ARRIBA Km 1+850 a 1+750 = 100 metros|PROMEDIO EN TRAMO AGUAS ARRIBA Km 1+850 a 1+750 = 100 metros|PROMEDIO EN TRAMO AGUAS ARRIBA Km 1+850 a 1+750 = 100 metros|PROMEDIO EN TRAMO AGUAS ARRIBA Km 1+850 a 1+750 = 100 metros|PROMEDIO EN TRAMO AGUAS ARRIBA Km 1+850 a 1+750 = 100 metros|PROMEDIO EN TRAMO AGUAS ARRIBA Km 1+850 a 1+750 = 100 metros|PROMEDIO EN TRAMO AGUAS ARRIBA Km 1+850 a 1+750 = 100 metros|PROMEDIO EN TRAMO AGUAS ARRIBA Km 1+850 a 1+750 = 100 metros|PROMEDIO EN TRAMO AGUAS ARRIBA Km 1+850 a 1+750 = 100 metros|PROMEDIO EN TRAMO AGUAS ARRIBA Km 1+850 a 1+750 = 100 metros|PROMEDIO EN TRAMO AGUAS ARRIBA Km 1+850 a 1+750 = 100 metros|PROMEDIO EN TRAMO AGUAS ARRIBA Km 1+850 a 1+750 = 100 metros|
|Prom|7.34|7.27|-0.07|3.87|3.67|-0.22|147|158|10.21|0.74|0.71|-0.03|
||||**-3.5%**|||**8.8%**|||**3.0%**|||**11.2%**|
||||||||||||||
|ROMEDIO EN TRAMO AGUAS ABAJO Km 1+180 a 0+900) = 280 metros|ROMEDIO EN TRAMO AGUAS ABAJO Km 1+180 a 0+900) = 280 metros|ROMEDIO EN TRAMO AGUAS ABAJO Km 1+180 a 0+900) = 280 metros|ROMEDIO EN TRAMO AGUAS ABAJO Km 1+180 a 0+900) = 280 metros|ROMEDIO EN TRAMO AGUAS ABAJO Km 1+180 a 0+900) = 280 metros|ROMEDIO EN TRAMO AGUAS ABAJO Km 1+180 a 0+900) = 280 metros|ROMEDIO EN TRAMO AGUAS ABAJO Km 1+180 a 0+900) = 280 metros|ROMEDIO EN TRAMO AGUAS ABAJO Km 1+180 a 0+900) = 280 metros|ROMEDIO EN TRAMO AGUAS ABAJO Km 1+180 a 0+900) = 280 metros|ROMEDIO EN TRAMO AGUAS ABAJO Km 1+180 a 0+900) = 280 metros|ROMEDIO EN TRAMO AGUAS ABAJO Km 1+180 a 0+900) = 280 metros|ROMEDIO EN TRAMO AGUAS ABAJO Km 1+180 a 0+900) = 280 metros|ROMEDIO EN TRAMO AGUAS ABAJO Km 1+180 a 0+900) = 280 metros|
|Prom|5.41|5.41|0.01|3.76|3.71|-0.11|189.18|189.18|0.00|0.79|0.79|-0.01|
||||**0.2%**|||**-2.9%**|||**0.0%**|||**-0.6%**|

**NOTA: Km 1+770 : Puente Ruta 5 Norte**

victor **.** santtiz@gmail.com - Whatsapp: +39 351 644 6334 +56 99 252 4610 Pág. 12 de 43

**PROYECTO DEFENSAS FLUVIALES RIO ELQUI. VERIFICACIÓN DEFENSA RIBERA SUR**

**SECTOR RUTA 5 - DESEMBOCADURA RIO ELQUI** ANEXO 2 - EST. BASICOS-HIDRAULICA

En tabla esta se verifica impacto hidráulico en las secciones donde el proyecto genera diferencias
respecto a la situación actual Sin Proyecto, ocurre entre las secciones transversales Km 1+850
hasta Km 0+900 (Longitud = 950 m), es decir desde tramo proyecto más 100 m aguas arriba y 280
m hacia aguas abajo.

Además muestra el promedio de las diferencias en tramo del Proyecto y del tramo influenciado.

1.3.4. Parámetros Hidráulicos principales en Puente Ruta 5 Norte. TR= 100 años.

En la sección del Puente Ruta 5 Norte (situado dentro del tramo influenciado), la modelación
efectuada arroja los parámetros hidráulicos principales que se muestran en tabla siguiente. Con
estos, para cálculos se complementan las TABLA 1-2 y TABLA 1-3 anteriores.

**TABLA 1-5 Parámetros Hidráulicos TR 100 años. Puente Ruta 5 Norte**

|River Sta|Min Ch<br>El<br>(m)|W.S.<br>Elev<br>(m)|Crit<br>W.S.<br>(m)|E.G.<br>Elev<br>(m)|E.G.<br>Slope<br>(m/m)|Vel<br>Chnl<br>(m/s)|Flow<br>Area<br>(m2)|Top W<br>Chnl<br>(m)|Froude<br># Chl|Hydr<br>Radius C<br>(m)|
|---|---|---|---|---|---|---|---|---|---|---|
|**SIN Proyecto **|**SIN Proyecto **|**SIN Proyecto **|**SIN Proyecto **|**SIN Proyecto **|**SIN Proyecto **|**SIN Proyecto **|**SIN Proyecto **|**SIN Proyecto **|**SIN Proyecto **|**SIN Proyecto **|
|1770 BR U|4.59|9.42|8.57|10.02|0.003036|3.42|456|144|0.5|2.54|
|1770 BR D|4.25|9.28|8.18|9.92|0.002768|3.56|442|116|0.59|2.89|
|**Prom 1**|**4.42**|**9.35**|**8.38**|**9.97**|**0.002902**|**3.49**|**449**|**130**|**0.55**|**2.72**|
|**CON Proyecto **|**CON Proyecto **|**CON Proyecto **|**CON Proyecto **|**CON Proyecto **|**CON Proyecto **|**CON Proyecto **|**CON Proyecto **|**CON Proyecto **|**CON Proyecto **|**CON Proyecto **|
|1770 BR U|4.59|8.9|8.57|9.76|0.005415|4.12|378|144|0.63|2.18|
|1770 BR D|4.25|9.02|7.9|9.55|0.002507|3.24|478|140|0.47|2.71|
|**Prom 2 **|**4.42**|**8.96**|**8.24**|**9.66**|**0.00397**|**3.69**|**428**|**142**|**0.55**|**2.44**|
|**DIFERENCIA DE VALORES MEDIOS. CON P - SIN P.**|**DIFERENCIA DE VALORES MEDIOS. CON P - SIN P.**|**DIFERENCIA DE VALORES MEDIOS. CON P - SIN P.**|**DIFERENCIA DE VALORES MEDIOS. CON P - SIN P.**|**DIFERENCIA DE VALORES MEDIOS. CON P - SIN P.**|**DIFERENCIA DE VALORES MEDIOS. CON P - SIN P.**|**DIFERENCIA DE VALORES MEDIOS. CON P - SIN P.**|**DIFERENCIA DE VALORES MEDIOS. CON P - SIN P.**|**DIFERENCIA DE VALORES MEDIOS. CON P - SIN P.**|**DIFERENCIA DE VALORES MEDIOS. CON P - SIN P.**|**DIFERENCIA DE VALORES MEDIOS. CON P - SIN P.**|
|**Dif= CP - SP **|0|-0.40|-0.14|-0.31|0.00107|0.20|-20.91|11.94|0.01|-0.27|
|**% =**<br>**Dif/Prom 1**||-4.2%|-1.7%|-3.2%|36.8%|5.6%|-4.7%|9.2%|0.9%|-10.1%|

 - Incidencia del Proyecto para TR=100 años, sobre los parámetros hidráulicos en Puente

Ruta 5 Norte:

Disminuye: Altura de aguas (4.2%); Altura crítica (1.7%); Bernoulli (3.2%); Área mojada

(4.7%); y Radio Hidráulico (10.1%).

Aumenta: Pendiente línea de Energía **j** (36.8%); Velocidad en canal principal (5.6%); Ancho

Superficial (9.2%) y No de Froude (0.9%)

victor **.** santtiz@gmail.com - Whatsapp: +39 351 644 6334 +56 99 252 4610 Pág. 13 de 43

**PROYECTO DEFENSAS FLUVIALES RIO ELQUI. VERIFICACIÓN DEFENSA RIBERA SUR**

**SECTOR RUTA 5 - DESEMBOCADURA RIO ELQUI** ANEXO 2 - EST. BASICOS-HIDRAULICA

1.3.5. TR= 10 y 2 años. Parámetros Hidráulicos principales.

Los Parámetros hidráulicos principales se muestran en el tramo de impacto, Km 1+970 al Km
1+100, por cuanto aguas arriba y abajo no se manifiestan alteraciones hidráulicas para el caudal
de diseño TR=100 años que es el de mayor exigencia. En TABLA 1-6 se muestran los valores en
situación Sin Proyecto y en TABLA 1-7 los equivalentes Con Proyecto.

|TABLA 1-6 Parámetros Hidráulicos. SIN Proyecto - T= 10 y 2 años|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|River<br>Sta|Profile|Q Total|Min Ch<br>El|W.S.<br>Elev|Crit<br>W.S.|E.G.<br>Elev|E.G.<br>Slope|Vel Chnl|Flow<br>Area|Top W<br>Chnl|Froude<br># Chl|Hydr<br>Radius C|
|River<br>Sta|Profile|(m3/s)|(m)|(m)|(m)|(m)|(m/m)|(m/s)|(m2)|(m)|(m)|(m)|
|1970|Tr=10|350|6.28|8.93|8.93|9.47|0.0069|3.46|118|60|0.93|1.41|
|1970|Tr= 2|85|6.28|8.05|8.05|8.32|0.0112|2.36|38|60|1.01|0.55|
||||||||||||||
|1900|Tr=10|350|5.27|7.53|7.09|8.51|0.0287|5.29|67|72|1.76|0.91|
|1900|Tr= 2|85|5.27|6.67|6.5|7.06|0.031|3.34|25|59|1.62|0.43|
||||||||||||||
|1850|Tr=10|350|4.95|6.99|7.34|7.69|0.003|2.77|150|59|0.64|1.87|
|1850|Tr= 2|85|4.95|5.98|6.27|6.43|0.0033|1.76|49|54|0.6|0.88|
||||||||||||||
|1800|Tr=10|350|4.59|6.8|7.28|7.53|0.0022|2.38|176|66|0.56|1.85|
|1800|Tr= 2|85|4.59|5.8|6.16|6.28|0.0024|1.56|59|55|0.51|0.93|
||||||||||||||
|1770|PUENTE RUTA 5 NORTE|PUENTE RUTA 5 NORTE|PUENTE RUTA 5 NORTE|PUENTE RUTA 5 NORTE|||||||||
||||||||||||||
|1740|Tr=10|350|4.25|6.19|6.53|6.84|0.0033|2.44|145|100|0.65|1.43|
|1740|Tr= 2|85|4.25|5.44|5.54|5.71|0.0062|1.79|48|85|0.76|0.56|
||||||||||||||
|1700|Tr=10|350|4.12|6.02|6.41|6.7|0.0033|2.37|148|106|0.64|1.39|
|1700|Tr= 2|85|4.12|5.17|5.32|5.48|0.005|1.78|48|72|0.7|0.66|
||||||||||||||
|1650|Tr=10|350|4|5.75|6.15|6.53|0.0032|2.72|131|74|0.66|1.72|
|1650|Tr= 2|85|4|4.87|5.17|5.29|0.0028|1.52|56|69|0.54|0.81|
||||||||||||||
|1600|Tr=10|350|3.97|5.59|6.01|6.37|0.003|2.69|137|70|0.64|1.79|
|1600|Tr= 2|85|3.97|4.72|5.05|5.16|0.0025|1.46|59|70|0.51|0.83|
||||||||||||||
|1550|Tr=10|350|3.57|5.43|5.88|6.21|0.0029|2.56|141|77|0.62|1.72|
|1550|Tr= 2|85|3.57|4.6|4.92|5.03|0.0026|1.43|60|77|0.52|0.76|
||||||||||||||
|1500|Tr=10|350|3.35|5.35|5.63|6.03|0.0041|2.81|126|82|0.73|1.51|
|1500|Tr= 2|85|3.35|4.47|4.63|4.83|0.0061|1.95|44|67|0.77|0.65|
||||||||||||||

victor **.** santtiz@gmail.com - Whatsapp: +39 351 644 6334 +56 99 252 4610 Pág. 14 de 43

**PROYECTO DEFENSAS FLUVIALES RIO ELQUI. VERIFICACIÓN DEFENSA RIBERA SUR**

**SECTOR RUTA 5 - DESEMBOCADURA RIO ELQUI** ANEXO 2 - EST. BASICOS-HIDRAULICA

|TABLA 1-6 Parámetros Hidráulicos. SIN Proyecto - T= 10 y 2 años|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|River<br>Sta|Profile|Q Total|Min Ch<br>El|W.S.<br>Elev|Crit<br>W.S.|E.G.<br>Elev|E.G.<br>Slope|Vel Chnl|Flow<br>Area|Top W<br>Chnl|Froude<br># Chl|Hydr<br>Radius C|
|River<br>Sta|Profile|(m3/s)|(m)|(m)|(m)|(m)|(m/m)|(m/s)|(m2)|(m)|(m)|(m)|
|1450|Tr=10|350|3.37|5.05|5.5|5.84|0.0029|2.61|138|75|0.63|1.75|
|1450|Tr= 2|85|3.37|4.23|4.48|4.6|0.003|1.52|56|73|0.56|0.76|
||||||||||||||
|1400|Tr=10|350|2.99|4.91|5.33|5.69|0.0032|2.68|133|75|0.65|1.71|
|1400|Tr= 2|85|2.99|4.1|4.2|4.38|0.0063|1.9|45|74|0.78|0.61|
||||||||||||||
|1350|Tr=10|350|2.22|4.64|5.22|5.54|0.0024|2.57|144|66|0.58|1.98|
|1350|Tr= 2|85|2.22|3.73|4|4.14|0.0034|1.65|52|66|0.59|0.77|
||||||||||||||
|1300|Tr=10|350|2.37|4.45|5.13|5.42|0.002|2.43|152|66|0.54|2.07|
|1300|Tr= 2|85|2.37|3.52|3.88|3.99|0.0023|1.5|58|61|0.5|0.91|
||||||||||||||
|1250|Tr=10|350|2.26|4.45|4.79|5.27|0.0039|3.09|117|60|0.73|1.83|
|1250|Tr= 2|85|2.26|3.46|3.64|3.83|0.0046|1.94|44|55|0.69|0.79|
||||||||||||||
|1200|Tr=10|350|2.12|4.21|4.59|5.08|0.0036|3.12|115|56|0.71|1.96|
|1200|Tr= 2|85|2.12|3.16|3.49|3.64|0.0027|1.7|50|52|0.55|0.96|
||||||||||||||
|1150|Tr=10|350|1.7|3.81|4.53|4.91|0.0022|2.8|140|49|0.57|2.42|
|1150|Tr= 2|85|1.7|2.77|3.47|3.55|0.0009|1.24|70|49|0.34|1.37|
||||||||||||||
|1100|Tr=10|350|1.46|3.56|4.54|4.79|0.0013|2.33|194|51|0.45|2.67|
|1100|Tr= 2|85|1.46|2.51|3.45|3.5|0.0005|1.05|83|51|0.26|1.59|

victor **.** santtiz@gmail.com - Whatsapp: +39 351 644 6334 +56 99 252 4610 Pág. 15 de 43

**PROYECTO DEFENSAS FLUVIALES RIO ELQUI. VERIFICACIÓN DEFENSA RIBERA SUR**

**SECTOR RUTA 5 - DESEMBOCADURA RIO ELQUI** ANEXO 2 - EST. BASICOS-HIDRAULICA

|TABLA 1-7 Parámetros Hidráulicos. T= 10 y 2 años - CON Proyecto|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|River<br>Sta<br>|Profile<br>|Q Total|Min Ch<br>El|W.S.<br>Elev|Crit W.S.|E.G.<br>Elev|E.G. Slope|Vel<br>Chnl|Flow<br>Area|Top W<br>Chnl|Froude #<br>Chl|Hydr<br>Radius C|
|||(m3/s)|(m)|(m)|(m)|(m)|(m/m)|(m/s)|(m2)|(m)||(m)|
|1970|Tr=10|350|6.28|8.88|8.88|9.37|0.00896|3.13|112|112|1|0.99|
|1970|Tr= 2|85|6.28|8.04|8.04|8.3|0.01124|2.27|37|72|1|0.51|
||||||||||||||
|1900|Tr=10|350|5.27|7.22|7.51|8.24|0.02029|4.48|78|84|1.49|0.92|
|1900|Tr= 2|85|5.27|6.5|6.67|7.06|0.03032|3.31|26|59|1.6|0.43|
||||||||||||||
|1850|Tr=10|350|4.95|7.37|6.95|7.64|0.00316|2.28|153|113|0.63|1.35|
|1850|Tr= 2|85|4.95|6.28|5.98|6.43|0.00409|1.71|50|69|0.64|0.72|
||||||||||||||
|1800|Tr=10|350|4.59|7.27|6.74|7.48|0.0025|2|175|132|0.56|1.32|
|1800|Tr= 2|85|4.59|6.14|5.79|6.25|0.00266|1.47|58|73|0.53|0.79|
||||||||||||||
|1770|PUENTE RUTA 5 NORTE|PUENTE RUTA 5 NORTE|PUENTE RUTA 5 NORTE|PUENTE RUTA 5 NORTE|PUENTE<br>RUTA 5<br>NORTE||||||||
||||||||||||||
|1740|Tr=10|<br>350|4.25|6.58|6.23|6.8|0.00349|2.08|168|155|0.64|1.08|
|1740|Tr= 2|85|4.25|5.54|5.44|5.71|0.00623|1.78|48|85|0.76|0.56|
||||||||||||||
|1700|Tr=10|<br>350|4.12|6.43|6.08|6.67|0.0032|2.16|162|132|0.62|1.23|
|1700|Tr= 2|85|4.12|5.32|5.17|5.48|0.00494|1.78|48|72|0.7|0.66|
||||||||||||||
|1650|Tr=10|<br>350|4|6.17|5.82|6.49|0.00341|2.52|138|93|0.66|1.48|
|1650|Tr= 2|85|4|5.17|4.87|5.29|0.00273|1.51|56|69|0.54|0.81|
||||||||||||||
|1600|Tr=10|<br>350|3.97|6.02|5.63|6.33|0.00307|2.45|141|92|0.63|1.53|
|1600|Tr= 2|85|3.97|5.05|4.72|5.16|0.0025|1.44|59|73|0.51|0.8|
||||||||||||||
|1550|Tr=10|<br>350|3.57|5.88|5.45|6.17|0.00293|2.37|148|98|0.62|1.5|
|1550|Tr= 2|85|3.57|4.93|4.6|5.03|0.00264|1.41|60|80|0.52|0.75|
||||||||||||||
|1500|Tr=10|<br>350|3.35|5.62|5.36|5.99|0.00428|2.69|130|95|0.73|1.37|
|1500|Tr= 2|85|3.35|4.64|4.47|4.83|0.00603|1.94|44|67|0.77|0.65|
||||||||||||||
|1450|Tr=10|<br>350|3.37|5.57|5.1|5.78|0.00239|2.05|167|118|0.55|1.41|
|1450|Tr= 2|85|3.37|4.48|4.23|4.6|0.00299|1.5|57|76|0.55|0.75|
||||||||||||||
|1400|Tr=10|<br>350|2.99|5.3|4.92|5.63|0.00334|2.53|138|91|0.66|1.51|

victor **.** santtiz@gmail.com - Whatsapp: +39 351 644 6334 +56 99 252 4610 Pág. 16 de 43

**PROYECTO DEFENSAS FLUVIALES RIO ELQUI. VERIFICACIÓN DEFENSA RIBERA SUR**

**SECTOR RUTA 5 - DESEMBOCADURA RIO ELQUI** ANEXO 2 - EST. BASICOS-HIDRAULICA

|TABLA 1-7 Parámetros Hidráulicos. T= 10 y 2 años - CON Proyecto|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|River<br>Sta<br>|Profile<br>|Q Total|Min Ch<br>El|W.S.<br>Elev|Crit W.S.|E.G.<br>Elev|E.G. Slope|Vel<br>Chnl|Flow<br>Area|Top W<br>Chnl|Froude #<br>Chl|Hydr<br>Radius C|
|||(m3/s)|(m)|(m)|(m)|(m)|(m/m)|(m/s)|(m2)|(m)||(m)|
|1400|Tr= 2|85|2.99|4.2|4.1|4.38|0.00624|1.89|45|74|0.77|0.61|
||||||||||||||
|1350|Tr=10|<br>350|2.22|5.19|4.65|5.47|0.0025|2.35|149|88|0.58|1.67|
|1350|Tr= 2|85|2.22|4.01|3.73|4.14|0.00338|1.6|53|70|0.59|0.75|
||||||||||||||
|1300|Tr=10|<br>350|2.37|5.09|4.46|5.35|0.00213|2.24|156|88|0.54|1.76|
|1300|Tr= 2|85|2.37|3.89|3.52|4|0.00233|1.46|58|67|0.5|0.86|
||||||||||||||
|1250|Tr=10|<br>350|2.26|4.81|4.46|5.2|0.00384|2.76|127|81|0.71|1.54|
|1250|Tr= 2|85|2.26|3.65|3.45|3.84|0.00435|1.88|45|56|0.67|0.79|
||||||||||||||
|1200|Tr=10|<br>350|2.12|4.63|4.22|5.02|0.00337|2.74|128|76|0.67|1.68|
|1200|Tr= 2|85|2.12|3.52|3.16|3.66|0.00254|1.64|52|53|0.53|0.97|
||||||||||||||
|1150|Tr=10|350|1.7|4.51|3.8|4.82|0.00309|2.47|139|90|0.63|1.54|
|1150|Tr= 2|85|1.7|3.48|2.76|3.56|0.00089|1.2|71|53|0.33|1.33|
||||||||||||||
|1100|Tr=10|350|1.46|4.44|3.56|4.67|0.00206|2.18|154|88|0.53|1.73|
|1100|Tr= 2|85|1.46|3.46|2.51|3.52|0.00053|1.03|82|53|0.26|1.55|
||||||||||||||

victor **.** santtiz@gmail.com - Whatsapp: +39 351 644 6334 +56 99 252 4610 Pág. 17 de 43

PROYECTO DEFENSAS FLUVIALES - COMUNA DE LA SERENA

SECTOR RUTA 5 - DESEMBOCADURA RIO ELQUI ANEXO 2 - EST. BASICOS-GASTO SOLIDO

**ANALISIS DE GASTO SÒLIDO**

El objetivo es verificar las tendencias de la capacidad de arrastre de sólidos (GS) del escurrimiento
en las situaciones Sin y Con Proyecto, a fin de estimar referencialmente su comportamiento en el

tramo de estudio.

Se considera el tramo de L= 950 m. influenciado por la Modificación del Cauce, esto es, entre las
secciones transversales Km 1+850 al Km 0+900, debido a que fuera de estos límites se presenta

influencia hidráulica nula.

Para el cálculo de la Tasa de Gasto Sólido de Fondo Se utilizan la de Relación de Meyer - PeterMüller para caudales períodos de retorno T= 100, 10 y 2 años, de acuerdo con la metodología
entregada en Informe Principal MEMORIA.

La relación de Meyer - Peter - Müller” se representa por medio de la siguiente expresión:

0.25 ( p/g ) [1/3] x ( (ps-p)/ps x gs ) [2/3] = T - Tc

Además se tienen:

gs = 0.792 x ps/(ps - 1) x (T - Tc ) 3/2

T = p x J x Rh x (QS/QT) x (K/KL) 3/2

Tc = 0.047 x ( p2 - p ) x d

**2.1** **Datos para el cálculo**

Resultados de Análisis Hidráulico

Se utilizan de los datos Granulométricos incluidos en estudio aprobado por D.G.A. (Res.

D.G.A. No180/2020, Región de Coquimbo), ANEXO 2 - GASTO SOLIDO siguiente:

Granulometría Integral de calicata excavada 100 m aguas abajo del actual Puente Ruta 5
Norte, cuyos diámetros característicos son:

**2.2** **Aplicación**

|Ps =|2.65|T / m3|
|---|---|---|
|Dm =|0.041|m|
|D50 =|0.020|m|
|D84 =|0.074|m|
|D90 =|0.096|m|
|D aparente|1.80|T / m3|

Para la aplicación de la relación **[(1)]** de gasto Sólido, se determinan previamente los coeficientes de
K de Strickler, la tensiones tangenciales **[(2)]** y la tensión crítica **[(3)]**, reemplazando los datos en las
respectivas relaciones.

Coeficientes K y KL

victor **.** santtiz@gmail.com - Whatsapp: +39 351 644 6334 +56 99 252 4610 Pág. 18 de 43

**PROYECTO DEFENSAS FLUVIALES RIO ELQUI. VERIFICACIÓN DEFENSA RIBERA SUR**

**SECTOR RUTA 5 - DESEMBOCADURA RIO ELQUI** ANEXO 2 EST. BASICOS - SALIDAS HEC RAS_CON PROYECTO

K = D 50 [(1/6)] / 26.3
Strickler =

KL = D 90 [(1/6) ] / 26.3

Tensión tangencial crítica: Tc = 0.047x (Ps-Pw) x Dm

**2.3** **Tablas de Resultados de GASTO SOLIDO**

A continuación, se presentan los resultados para las situaciones SIN Proyecto y CON Proyecto que
arroja la metodología utilizada. Se presenta sombreado el tramo del proyecto. Por motivos de
mejor visualización de gráficos, la longitud considerada en las figuras en Memoria (documento
principal), es mayor a 750 m. señalados, desde Sección Km 1+970 a Km 0+900.

victor **.** santtiz@gmail.com - Whatsapp: +39 351 644 6334 +56 99 252 4610 Pág. 19 de 43

**PROYECTO DEFENSAS FLUVIALES RIO ELQUI. VERIFICACIÓN DEFENSA RIBERA SUR**

**SECTOR RUTA 5 - DESEMBOCADURA RIO ELQUI** ANEXO 2 EST. BASICOS - SALIDAS HEC RAS_CON PROYECTO

**TABLA 2-1 GASTO SÓLIDO GS - TR= 100 años - SIN Proyecto**

|Dist. Plano (m)|J<br>x1000|R hid<br>( m )|Ancho B<br>( m )|T<br>K/m2|T-Tc<br>K/m2|gs<br>K/s/m|GS=Bx gs<br>K/s|
|---|---|---|---|---|---|---|---|
|1,970|13.58|2.04|120|18.90|17.28|90.35|10,865|
|1,900|15.61|2.02|112|21.51|19.90|111.59|12,482|
|1,850|2.22|3.41|125|5.16|3.55|8.39|1,046|
|1,800|1.49|3.25|167|3.31|1.69|2.77|464|
|1,770|2.90|2.72|130|5.38|3.76|9.17|1,191|
|1,750|1.98|3.47|126|4.70|3.08|6.79|855|
|1,740|1.52|3.85|124|4.00|2.38|4.62|572|
|1,700|1.51|4.19|106|4.31|2.70|5.56|592|
|1,650|5.31|3.54|74|12.82|11.20|47.13|3,510|
|1,600|5.62|3.40|77|13.04|11.42|48.55|3,745|
|1,550|9.63|2.54|97|16.69|15.07|73.58|7,127|
|1,500|2.25|3.28|107|5.04|3.42|7.95|854|
|1,450|1.55|3.65|111|3.85|2.23|4.20|465|
|1,400|2.33|2.91|151|4.63|3.01|6.57|994|
|1,350|4.07|2.86|115|7.94|6.32|19.98|2,302|
|1,300|2.65|2.67|158|4.83|3.22|7.26|1,147|
|1,250|5.20|1.96|185|6.95|5.34|15.50|2,862|
|1,200|7.76|1.61|230|8.52|6.90|22.81|5,243|
|1,180|6.25|2.19|174|9.32|7.70|26.89|4,675|
|1,150|3.99|3.05|90|8.30|6.68|21.73|1,952|
|1,100|6.39|2.74|88|11.95|10.34|41.80|3,693|
|1,050|7.50|2.11|133|10.80|9.18|34.99|4,636|
|1,000|2.41|2.14|235|3.53|1.91|3.32|780|
|950|4.69|1.78|239|5.70|4.08|10.37|2,481|
|900|1.80|1.77|350|2.17|0.56|0.52|184|
|850|2.63|2.24|161|4.02|2.41|4.70|758|
|800|2.96|2.24|159|4.53|2.91|6.25|993|

victor **.** santtiz@gmail.com - Whatsapp: +39 351 644 6334 +56 99 252 4610 Pág. 20 de 43

**PROYECTO DEFENSAS FLUVIALES RIO ELQUI. VERIFICACIÓN DEFENSA RIBERA SUR**

**SECTOR RUTA 5 - DESEMBOCADURA RIO ELQUI** ANEXO 2 EST. BASICOS - SALIDAS HEC RAS_CON PROYECTO

**TABLA 2-2 GASTO SÓLIDO GS - TR= 100 años - CON Proyecto**

|Dist. Plano (m)|J<br>x1000|R hid<br>( m )|Ancho B<br>( m )|T<br>K/m2|T-Tc<br>K/m2|gs<br>K/s/m|GS=Bx gs<br>K/s|
|---|---|---|---|---|---|---|---|
|1970|13.58|2.04|120|18.90|17.28|90.35|10,865|
|1900|15.61|2.02|112|21.51|19.90|111.59|12,482|
|1850|3.08|3.11|125|6.53|4.91|13.69|1,706|
|1800|2.07|2.94|168|4.14|2.53|5.05|850|
|1770|3.97|2.44|142|6.61|4.99|14.02|1,988|
|1750|2.17|3.16|153|4.68|3.06|6.73|1,032|
|1740|1.27|3.52|159|3.05|1.43|2.15|342|
|1700|1.48|3.73|132|3.76|2.15|3.96|522|
|1650|3.71|3.47|93|8.79|7.18|24.17|2,245|
|1600|5.88|3.04|92|12.19|10.58|43.25|3,984|
|1550|4.35|3.05|103|9.06|7.45|25.54|2,630|
|1500|2.32|3.14|117|4.98|3.36|7.75|909|
|1450|1.39|3.52|125|3.33|1.72|2.83|352|
|1400|2.35|2.82|164|4.52|2.90|6.22|1,016|
|1350|3.63|2.83|129|7.00|5.39|15.73|2,024|
|1300|2.68|2.61|166|4.78|3.16|7.08|1,175|
|1250|5.12|1.95|198|6.81|5.19|14.87|2,939|
|1200|5.72|1.73|245|6.75|5.13|14.63|3,577|
|1180|4.58|2.35|183|7.33|5.71|17.18|3,138|
|1150|2.87|3.27|90|6.41|4.79|13.18|1,184|
|1100|6.21|2.76|88|11.70|10.09|40.28|3,559|
|1050|7.43|2.11|133|10.70|9.08|34.42|4,561|
|1000|2.33|2.16|235|3.43|1.82|3.08|724|
|950|6.20|1.65|239|6.98|5.36|15.62|3,736|
|900|1.81|1.77|350|2.18|0.57|0.54|189|
|850|2.62|2.24|161|4.00|2.39|4.63|748|
|800|2.96|2.24|159|4.52|2.90|6.22|987|

victor **.** santtiz@gmail.com - Whatsapp: +39 351 644 6334 +56 99 252 4610 Pág. 21 de 43

**PROYECTO DEFENSAS FLUVIALES RIO ELQUI. VERIFICACIÓN DEFENSA RIBERA SUR**

**SECTOR RUTA 5 - DESEMBOCADURA RIO ELQUI** ANEXO 2 EST. BASICOS - SALIDAS HEC RAS_CON PROYECTO

**TABLA 2-3 Gasto Sólido GS - TR= 10 años - SIN Proyecto**

|Dist. Plano (m)|J<br>x1000|R hid<br>( m )|Ancho B<br>( m )|T<br>K/m2|T-Tc<br>K/m2|gs<br>K/s/m|GS=Bx gs<br>K/s|
|---|---|---|---|---|---|---|---|
|1,970|8.96|0.99|112|6.06|4.44|11.76|1,318|
|1,900|20.29|0.92|84|12.73|11.12|46.62|3,937|
|1,850|3.15|1.35|113|2.90|1.29|1.84|208|
|1,800|2.50|1.32|132|2.25|0.63|0.63|83|
|1,770||||||||
|1,750||||||||
|1,740|3.24|1.39|106|3.07|1.46|2.21|235|
|1,700|3.20|1.72|74|3.76|2.14|3.95|294|
|1,650|2.89|1.73|77|3.42|1.80|3.03|234|
|1,600|2.81|1.61|89|3.08|1.47|2.23|198|
|1,550|4.02|1.49|85|4.08|2.47|4.88|414|
|1,500|2.28|1.53|104|2.38|0.76|0.84|87|
|1,450|3.16|1.66|79|3.58|1.96|3.46|273|
|1,400|2.37|1.85|75|2.99|1.38|2.03|153|
|1,350|1.99|1.89|81|2.56|0.95|1.16|94|
|1,300|3.97|1.68|69|4.55|2.94|6.33|434|
|1,250|3.90|1.83|60|4.87|3.25|7.38|446|
|1,200|3.60|1.52|86|3.73|2.12|3.87|331|
|1,180|3.42|1.39|104|3.25|1.64|2.63|274|
|1,150|3.16|1.20|133|2.59|0.97|1.20|160|
|1,100|2.22|0.99|224|1.50|-0.12|0.00|0|
|1,050|3.38|0.93|201|2.14|0.53|0.48|96|
|1,000|5.55|0.67|277|2.54|0.92|1.11|307|
|950|2.93|1.05|161|2.10|0.48|0.42|68|
|900|3.83|1.05|154|2.74|1.13|1.51|232|
|850|3.16|1.03|178|2.22|0.60|0.59|105|
|800|2.13|1.22|162|1.77|0.16|0.08|13|

victor **.** santtiz@gmail.com - Whatsapp: +39 351 644 6334 +56 99 252 4610 Pág. 22 de 43

**PROYECTO DEFENSAS FLUVIALES RIO ELQUI. VERIFICACIÓN DEFENSA RIBERA SUR**

**SECTOR RUTA 5 - DESEMBOCADURA RIO ELQUI** ANEXO 2 EST. BASICOS - SALIDAS HEC RAS_CON PROYECTO

**TABLA 2-4 Gasto Sólido GS - TR= 10 años - CON Proyecto**

|Dist. Plano (m)|J<br>x1000|R hid<br>( m )|Ancho B<br>( m )|T<br>K/m2|T-Tc<br>K/m2|gs<br>K/s/m|GS=Bx gs<br>K/s|
|---|---|---|---|---|---|---|---|
|**CON PROYECTO TR= 10 años**|**CON PROYECTO TR= 10 años**|**CON PROYECTO TR= 10 años**|**CON PROYECTO TR= 10 años**|**CON PROYECTO TR= 10 años**|**CON PROYECTO TR= 10 años**|**CON PROYECTO TR= 10 años**|**CON PROYECTO TR= 10 años**|
|1,970|8.96|0.99|112|6.05|4.44|11.76|1,318|
|1,900|20.29|0.92|84|12.73|11.12|46.61|3,937|
|1,850|3.16|1.35|113|2.91|1.29|1.85|209|
|1,800|2.50|1.32|132|2.25|0.63|0.63|83|
|1,770|0.00|0.00|0.00|0.00|0.00|0.00|0.00|
|1,750|0.00|0.00|0|0.00|-1.62|0.00|0|
|1,740|3.20|1.23|132|2.69|1.07|1.39|184|
|1,700|3.41|1.48|93|3.44|1.82|3.09|287|
|1,650|3.07|1.53|92|3.21|1.59|2.52|233|
|1,600|2.93|1.50|98|3.00|1.39|2.05|201|
|1,550|4.28|1.37|95|4.00|2.39|4.64|439|
|1,500|2.39|1.41|118|2.30|0.69|0.72|84|
|1,450|3.34|1.51|91|3.44|1.82|3.10|282|
|1,400|2.50|1.67|88|2.85|1.23|1.72|152|
|1,350|2.13|1.76|88|2.56|0.94|1.15|101|
|1,300|3.84|1.54|81|4.03|2.42|4.73|385|
|1,250|3.37|1.68|76|3.86|2.24|4.23|319|
|1,200|3.09|1.54|90|3.25|1.63|2.62|236|
|1,180|3.12|1.40|107|2.99|1.37|2.02|216|
|1,150|3.16|1.20|133|2.59|0.97|1.20|160|
|1,100|2.22|0.99|224|1.50|-0.12|0.00|0|
|1,050|3.38|0.93|201|2.14|0.53|0.48|96|
|1,000|5.55|0.67|277|2.54|0.92|1.11|308|
|950|2.92|1.05|161|2.09|0.48|0.42|67|
|900|3.83|1.05|154|2.74|1.13|1.51|232|
|850|3.16|1.03|178|2.22|0.60|0.59|105|
|800|2.13|1.22|162|1.77|0.16|0.08|13|

victor **.** santtiz@gmail.com - Whatsapp: +39 351 644 6334 +56 99 252 4610 Pág. 23 de 43

**PROYECTO DEFENSAS FLUVIALES RIO ELQUI. VERIFICACIÓN DEFENSA RIBERA SUR**

**SECTOR RUTA 5 - DESEMBOCADURA RIO ELQUI** ANEXO 2 EST. BASICOS - SALIDAS HEC RAS_CON PROYECTO

**TABLA 2-5 Gasto Sólido GS - TR= 2 años - SIN Proyecto**

|Dist. Plano (m)|J<br>x1000|R hid<br>( m )|Ancho B<br>( m )|T<br>K/m2|T-Tc<br>K/m2|gs<br>K/s/m|GS=Bx gs<br>K/s|
|---|---|---|---|---|---|---|---|
|1,970|11.24|0.51|72|3.91|2.29|4.37|315|
|1,900|30.32|0.43|59|8.90|7.28|24.70|1,456|
|1,850|4.10|0.72|69|2.01|0.40|0.31|22|
|1,800|2.66|0.79|73|1.44|-0.18|0.00|0|
|1,770|0.00|0.00|0|0.00|-1.62|0.00|0|
|1,750|0.00|0.00|0.00|0.00|0.00|0.00|0.00|
|1,740|6.22|0.56|85|2.38|0.76|0.83|71|
|1,700|4.94|0.66|72|2.22|0.61|0.60|43|
|1,650|2.73|0.81|69|1.51|-0.11|0.00|0|
|1,600|2.51|0.80|73|1.37|-0.24|0.00|0|
|1,550|2.64|0.76|78|1.37|-0.25|0.00|0|
|1,500|6.09|0.65|67|2.70|1.09|1.42|95|
|1,450|2.97|0.77|72|1.56|-0.05|0.00|0|
|1,400|6.33|0.61|74|2.63|1.02|1.29|95|
|1,350|3.40|0.78|66|1.81|0.19|0.11|7|
|1,300|2.29|0.89|64|1.39|-0.23|0.00|0|
|1,250|4.51|0.80|55|2.46|0.85|0.98|53|
|1,200|2.61|0.98|52|1.75|0.13|0.06|3|
|1,180|1.92|1.12|52|1.47|-0.15|0.00|0|
|1,150|0.89|1.33|53|0.80|-0.81|0.00|0|
|1,100|0.53|1.55|53|0.56|-1.06|0.00|0|
|1,050|1.31|1.31|44|1.17|-0.44|0.00|0|
|1,000|1.22|1.31|46|1.09|-0.53|0.00|0|
|950|1.49|1.25|45|1.27|-0.34|0.00|0|
|900|4.06|0.88|49|2.44|0.82|0.94|46|
|850|7.99|0.72|49|3.93|2.31|4.42|218|
|800|3.94|0.83|55|2.23|0.61|0.61|33|

victor **.** santtiz@gmail.com - Whatsapp: +39 351 644 6334 +56 99 252 4610 Pág. 24 de 43

**PROYECTO DEFENSAS FLUVIALES RIO ELQUI. VERIFICACIÓN DEFENSA RIBERA SUR**

**SECTOR RUTA 5 - DESEMBOCADURA RIO ELQUI** ANEXO 2 EST. BASICOS - SALIDAS HEC RAS_CON PROYECTO

**TABLA 2-6 Gasto Sólido GS - TR= 2 años - CON Proyecto**

|Dist. Plano (m)|J<br>x1000|R hid<br>( m )|Ancho B<br>( m )|T<br>K/m2|T-Tc<br>K/m2|gs<br>K/s/m|GS=Bx gs<br>K/s|
|---|---|---|---|---|---|---|---|
|1,970|11.24|0.51|72|3.91|2.29|4.37|315|
|1,900|30.32|0.43|59|8.90|7.28|24.70|1,456|
|1,850|4.10|0.72|69|2.01|0.40|0.31|22|
|1,800|2.66|0.79|73|1.44|-0.18|0.00|0|
|1,770|0.00|0.00|0.00|0.00|0.00|0.00|0.00|
|1,750|0.00|0.00|0|0.00|-1.62|0.00|0|
|1,740|6.22|0.56|85|2.38|0.76|0.83|71|
|1,700|4.94|0.66|72|2.22|0.61|0.60|43|
|1,650|2.73|0.81|69|1.51|-0.11|0.00|0|
|1,600|2.51|0.80|73|1.37|-0.25|0.00|0|
|1,550|2.64|0.76|78|1.37|-0.25|0.00|0|
|1,500|6.06|0.65|67|2.69|1.07|1.40|93|
|1,450|2.99|0.76|73|1.55|-0.07|0.00|0|
|1,400|6.26|0.61|74|2.61|0.99|1.24|91|
|1,350|3.37|0.77|67|1.77|0.15|0.08|5|
|1,300|2.33|0.86|67|1.37|-0.25|0.00|0|
|1,250|4.34|0.79|56|2.34|0.73|0.78|44|
|1,200|2.53|0.97|53|1.68|0.06|0.02|1|
|1,180|1.88|1.11|53|1.43|-0.19|0.00|0|
|1,150|0.89|1.33|53|0.81|-0.81|0.00|0|
|1,100|0.53|1.55|53|0.56|-1.06|0.00|0|
|1,050|1.31|1.31|44|1.17|-0.44|0.00|0|
|1,000|1.22|1.30|46|1.08|-0.53|0.00|0|
|950|1.50|1.24|45|1.27|-0.35|0.00|0|
|900|4.09|0.88|49|2.46|0.84|0.97|48|
|850|7.97|0.71|51|3.86|2.25|4.23|214|
|800|3.94|0.83|55|2.23|0.61|0.61|33|

victor **.** santtiz@gmail.com - Whatsapp: +39 351 644 6334 +56 99 252 4610 Pág. 25 de 43

PROYECTO DEFENSAS FLUVIALES - COMUNA DE LA SERENA

SECTOR RUTA 5 - DESEMBOCADURA RIO ELQUI ANEXO 2 - EST. BASICOS-SOCAVACIONES

**CÁLCULO DE SOCAVACIONES**

Utilizando parámetros incluidos en análisis hidráulico y antecedentes granulométricos,

disponibles en el presente Informe y en _**ANEXO 2 Estudios Básicos- HIDRAULICA**_, se procedió a la

aplicación de los métodos descritos en _**documento principal MEMORIA (Cap. 5),**_ realizando los

cálculos de socavación general para estimación de la profundidad de Socavación y posteriormente

establecer cota de fundación del pretil y por otra parte, establecer si el Puente Ruta 5 requiere de

protección.

El tramo considerado en este análisis, va del Km 1+970 al Km 0+800 (31 secciones).

**3.1** **Resultados de Socavación General**

Los principales parámetros y resultados que arrojan los métodos descritos, se muestran en Tablas
siguientes:

victor **.** santtiz@gmail.com - Whatsapp: +39 351 644 6334 +56 99 252 4610 Pág. 26 de 43

**PROYECTO DEFENSAS FLUVIALES RIO ELQUI. VERIFICACIÓN DEFENSA RIBERA SUR**

**SECTOR RUTA 5 - DESEMBOCADURA RIO ELQUI** ANEXO 2 EST. BASICOS - SALIDAS HEC RAS_CON PROYECTO

**TABLA 3-1 Socavación General; Tr=100 años - SIN Proyecto**

|Dist.<br>Acum.|Parámetros|Col3|Col4|Col5|PROFUNDIDAD SOCAV. S= hs - h0 (m)|Col7|Col8|Col9|Cota (msnm)|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**Dist.**<br>**Acum.**|** A (m2)**|**B (m)**||**ho (m)**|**hs (m)**|**Lischtvan**|**Neill**|**Adop**|** Fondo**|**Socav**|
|1,970|247|120|3.88|3.72|7.72|4.00|2.53|3.26|6.28|3.02|
|1,900|227|112|4.25|3.46|7.54|4.08|2.96|3.52|5.27|1.75|
|1,850|427|125|1.60|4.65|5.20|0.55|0.83|0.69|4.95|4.26|
|1,800|546|167|1.29|5.08|4.94|0.00|0.00|0.00|4.59|4.59|
|1,770|449|130|1.51|4.93|5.36|0.43|0.59|0.51|4.42|3.91|
|1,750|470|126|1.37|5.03|5.10|0.07|0.43|0.25|4.31|4.06|
|1,740|481|124|1.30|5.08|4.97|0.00|0.34|0.17|4.25|4.08|
|1,700|446|106|1.34|5.10|5.10|0.00|0.73|0.37|4.12|3.75|
|1,650|264|74|2.53|3.98|5.45|1.47|2.52|2.00|4.00|2.00|
|1,600|263|77|2.61|3.73|5.14|1.41|2.53|1.97|3.97|2.00|
|1,550|248|97|3.33|3.47|5.66|2.19|2.23|2.21|3.57|1.36|
|1,500|354|107|1.97|4.52|5.89|1.37|1.66|1.51|3.35|1.84|
|1,450|405|111|1.61|4.48|4.98|0.50|1.15|0.83|3.37|2.54|
|1,400|442|151|1.71|4.65|5.48|0.83|0.58|0.71|2.99|2.28|
|1,350|331|115|2.32|4.9|7.38|2.48|1.69|2.09|2.22|0.13|
|1,300|423|158|1.90|4.84|6.25|1.41|0.66|1.03|2.37|1.34|
|1,250|364|185|2.71|4.6|7.68|3.08|0.90|1.99|2.26|0.27|
|1,200|371|230|3.03|4.25|7.57|3.32|0.72|2.02|2.12|0.10|
|1,180|333|174|3.02|4.314|7.69|3.37|1.17|2.27|1.95|-0.32|
|1,150|276|90|2.66|4.41|7.18|2.77|2.88|2.82|1.70|-1.12|
|1,100|244|88|3.23|3.99|7.32|3.33|3.39|3.36|1.46|-1.90|
|1,050|280|133|3.36|3.78|7.05|3.27|2.03|2.65|1.44|-1.21|
|1,000|503|235|1.86|4.03|4.85|0.82|0.17|0.50|1.42|0.92|
|950|425|239|2.48|3.62|5.29|1.67|0.54|1.10|1.46|0.36|
|900|620|350|1.71|3.81|4.24|0.43|0.00|0.21|1.31|1.10|
|850|362|161|2.50|3.43|4.97|1.54|1.23|1.38|1.42|0.04|
|800|357|159|2.53|3.4|4.95|1.55|1.28|1.42|1.26|-0.16|
||||||||||||
| =<br>1 <br>**X =** <br>0.305<br> = 1.27<br> = <br>0.99<br> <br> <br>| =<br>1 <br>**X =** <br>0.305<br> = 1.27<br> = <br>0.99<br> <br> <br>| =<br>1 <br>**X =** <br>0.305<br> = 1.27<br> = <br>0.99<br> <br> <br>| =<br>1 <br>**X =** <br>0.305<br> = 1.27<br> = <br>0.99<br> <br> <br>| =<br>1 <br>**X =** <br>0.305<br> = 1.27<br> = <br>0.99<br> <br> <br>| =<br>1 <br>**X =** <br>0.305<br> = 1.27<br> = <br>0.99<br> <br> <br>| =<br>1 <br>**X =** <br>0.305<br> = 1.27<br> = <br>0.99<br> <br> <br>| =<br>1 <br>**X =** <br>0.305<br> = 1.27<br> = <br>0.99<br> <br> <br>| =<br>1 <br>**X =** <br>0.305<br> = 1.27<br> = <br>0.99<br> <br> <br>| =<br>1 <br>**X =** <br>0.305<br> = 1.27<br> = <br>0.99<br> <br> <br>| =<br>1 <br>**X =** <br>0.305<br> = 1.27<br> = <br>0.99<br> <br> <br>|

victor **.** santtiz@gmail.com - Whatsapp: +39 351 644 6334 +56 99 252 4610 Pág. 27 de 43

**PROYECTO DEFENSAS FLUVIALES RIO ELQUI. VERIFICACIÓN DEFENSA RIBERA SUR**

**SECTOR RUTA 5 - DESEMBOCADURA RIO ELQUI** ANEXO 2 EST. BASICOS - SALIDAS HEC RAS_CON PROYECTO

**TABLA 3-2 Socavación General; Tr=100 años - CON Proyecto**

|Dist.<br>Acum.|Parámetros|Col3|Col4|Col5|PROFUNDIDAD SOCAV. S= hs - h0 (m)|Col7|Col8|Col9|Cota (msnm)|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**Dist.**<br>**Acum.**|** A (m2)**|**B (m)**||**ho (m)**|**hs (m)**|**Lischtvan**|**Neill**|**Adop**|** Fondo**|**Socav**|
|1,970|247|120|3.88|3.72|7.72|4.00|2.53|**3.26**|6.28|3.02|
|1,900|227|112|4.25|3.46|7.54|4.08|2.96|**3.52**|5.27|1.75|
|1,850|389|125|1.87|4.35|5.38|1.03|1.18|**1.10**|4.95|3.85|
|1,800|496|168|1.52|4.78|5.17|0.39|0.19|**0.29**|4.59|4.30|
|1,770|428|142|1.74|4.535|5.36|0.82|0.74|**0.78**|4.42|3.64|
|1,750|517|153|1.33|4.7383|4.62|0.00|0.07|**0.04**|4.31|4.27|
|1,740|562|159|1.19|4.84|4.35|0.00|0.00|**0.00**|4.25|4.25|
|1,700|492|132|1.31|4.81|4.66|0.00|0.27|**0.13**|4.12|3.99|
|1,650|323|93|2.10|4.16|4.99|0.83|1.35|**1.09**|4.00|2.91|
|1,600|281|92|2.63|3.57|4.89|1.32|1.97|**1.64**|3.97|2.33|
|1,550|316|103|2.33|4|5.15|1.15|1.32|**1.23**|3.57|2.34|
|1,500|371|117|1.94|4.42|5.65|1.23|1.39|**1.31**|3.35|2.04|
|1,450|442|125|1.51|4.42|4.67|0.25|0.74|**0.49**|3.37|2.88|
|1,400|463|164|1.67|4.55|5.23|0.68|0.42|**0.55**|2.99|2.44|
|1,350|366|129|2.11|4.88|6.84|1.96|1.25|**1.60**|2.22|0.62|
|1,300|435|166|1.87|4.76|6.05|1.29|0.56|**0.93**|2.37|1.44|
|1,250|387|198|2.56|4.52|7.19|2.67|0.74|**1.70**|2.26|0.56|
|1,200|423|245|2.54|4.3|6.71|2.41|0.46|**1.44**|2.12|0.68|
|1,180|372|183|2.59|4.4|7.01|2.61|0.89|**1.75**|1.95|0.20|
|1,150|296|90|2.36|4.55|6.82|2.27|2.62|**2.45**|1.70|-0.75|
|1,100|245|88|3.20|4.01|7.33|3.32|3.37|**3.34**|1.46|-1.88|
|1,050|281|133|3.35|3.79|7.05|3.26|2.02|**2.64**|1.44|-1.20|
|1,000|508|235|1.83|4.05|4.83|0.78|0.15|**0.46**|1.42|0.96|
|950|395|239|2.81|3.49|5.55|2.06|0.68|**1.37**|1.46|0.09|
|900|619|350|1.71|3.8|4.23|0.43|0.00|**0.22**|1.31|1.09|
|850|362|161|2.50|3.43|4.97|1.54|1.23|**1.38**|1.42|0.04|
|800|357|159|2.53|3.4|4.95|1.55|1.28|**1.42**|1.26|-0.16|
||||||||||||
| =<br>1 <br>**X =** <br>0.305<br> = 1.27<br> = <br>0.99<br> <br> <br>| =<br>1 <br>**X =** <br>0.305<br> = 1.27<br> = <br>0.99<br> <br> <br>| =<br>1 <br>**X =** <br>0.305<br> = 1.27<br> = <br>0.99<br> <br> <br>| =<br>1 <br>**X =** <br>0.305<br> = 1.27<br> = <br>0.99<br> <br> <br>| =<br>1 <br>**X =** <br>0.305<br> = 1.27<br> = <br>0.99<br> <br> <br>| =<br>1 <br>**X =** <br>0.305<br> = 1.27<br> = <br>0.99<br> <br> <br>| =<br>1 <br>**X =** <br>0.305<br> = 1.27<br> = <br>0.99<br> <br> <br>| =<br>1 <br>**X =** <br>0.305<br> = 1.27<br> = <br>0.99<br> <br> <br>| =<br>1 <br>**X =** <br>0.305<br> = 1.27<br> = <br>0.99<br> <br> <br>| =<br>1 <br>**X =** <br>0.305<br> = 1.27<br> = <br>0.99<br> <br> <br>| =<br>1 <br>**X =** <br>0.305<br> = 1.27<br> = <br>0.99<br> <br> <br>|

victor **.** santtiz@gmail.com - Whatsapp: +39 351 644 6334 +56 99 252 4610 Pág. 28 de 43

**PROYECTO DEFENSAS FLUVIALES RIO ELQUI. VERIFICACIÓN DEFENSA RIBERA SUR**

**SECTOR RUTA 5 - DESEMBOCADURA RIO ELQUI** ANEXO 2 EST. BASICOS - SALIDAS HEC RAS_CON PROYECTO

**TABLA 3-3 Socavación General; Tr= 10 años - SIN Proyecto**

|Dist.<br>Acum.|Parámetros|Col3|Col4|Col5|PROFUNDIDAD SOCAV. S= hs - h0 (m)|Col7|Col8|Col9|Cota (msnm)|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**Dist.**<br>**Acum.**|** A (m2)**|**B (m)**||**ho (m)**|**hs (m)**|**Lischtvan**|**Neill**|**Adop**|** Fondo**|**Socav**|
|1,970|112|112|3.15|2.6|4.50|1.90|0.11|1.01|6.28|5.27|
|1,900|78|84|4.72|1.95|4.25|2.30|0.57|1.44|5.27|3.83|
|1,850|153|113|1.87|2.42|2.75|0.33|0.00|0.17|4.95|4.78|
|1,800|175|132|1.66|2.68|2.87|0.19|0.00|0.09|4.59|4.50|
|1,770|0|0|||||||||
|1,750|0|0|||||||||
|1,740|148|106|1.90|2.29|2.60|0.31|0.00|0.15|4.12|3.97|
|1,700|128|74|1.90|2.16|2.41|0.25|0.00|0.13|4.00|3.87|
|1,650|134|77|1.82|2.06|1.95|0.00|0.00|0.00|3.97|3.97|
|1,600|144|89|1.76|2.34|2.24|0.00|0.00|0.00|3.57|3.57|
|1,550|127|85|2.11|2.3|2.53|0.23|0.00|0.11|3.35|3.24|
|1,500|161|104|1.64|2.25|2.27|0.02|0.00|0.01|3.37|3.36|
|1,450|132|79|1.88|2.35|2.66|0.31|0.00|0.16|2.99|2.83|
|1,400|141|75|1.63|3.02|3.30|0.28|0.00|0.14|2.22|2.08|
|1,350|154|81|1.48|2.79|2.76|0.00|0.00|0.00|2.37|2.37|
|1,300|116|69|2.12|2.57|3.27|0.70|0.04|0.37|2.26|1.89|
|1,250|111|60|2.10|2.46|3.08|0.62|0.15|0.38|2.12|1.74|
|1,200|131|86|2.02|2.79|3.51|0.72|0.00|0.36|1.70|1.34|
|1,180|142|104|1.98|2.83|3.51|0.69|0.00|0.34|1.60|1.25|
|1,150|160|133|1.93|2.88|3.52|0.64|0.00|0.32|1.44|1.12|
|1,100|222|224|1.59|2.84|2.98|0.14|0.00|0.07|1.42|1.35|
|1,050|188|201|1.94|2.61|3.13|0.52|0.00|0.26|1.46|1.20|
|1,000|185|277|2.48|2.53|3.62|1.09|0.00|0.55|1.31|0.76|
|950|170|161|1.99|2.24|2.61|0.37|0.00|0.19|1.42|1.23|
|900|162|154|2.09|2.16|2.60|0.44|0.00|0.22|1.26|1.04|
|850|183|178|1.87|2.41|2.74|0.33|0.00|0.17|0.87|0.70|
|800|199|162|1.54|2.4|2.35|0.00|0.00|0.00|0.77|0.77|
||||||||||||
| =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.89**<br> <br> <br>| =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.89**<br> <br> <br>| =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.89**<br> <br> <br>| =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.89**<br> <br> <br>| =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.89**<br> <br> <br>| =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.89**<br> <br> <br>| =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.89**<br> <br> <br>| =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.89**<br> <br> <br>| =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.89**<br> <br> <br>| =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.89**<br> <br> <br>| =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.89**<br> <br> <br>|

victor **.** santtiz@gmail.com - Whatsapp: +39 351 644 6334 +56 99 252 4610 Pág. 29 de 43

**PROYECTO DEFENSAS FLUVIALES RIO ELQUI. VERIFICACIÓN DEFENSA RIBERA SUR**

**SECTOR RUTA 5 - DESEMBOCADURA RIO ELQUI** ANEXO 2 EST. BASICOS - SALIDAS HEC RAS_CON PROYECTO

**TABLA 3-4 Socavación General; Tr= 10 años - CON Proyecto**

|Dist.<br>Acum.|Parámetros|Col3|Col4|Col5|PROFUNDIDAD SOCAV. S= hs - h0 (m)|Col7|Col8|Col9|Cota (msnm)|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**Dist.**<br>**Acum.**|** A (m2)**|**B (m)**||**ho (m)**|**hs (m)**|**Lischtvan**|**Neill**|**Adop**|** Fondo**|**Socav**|
|1970|112|112|3.15|2.6|4.50|1.90|0.11|1.01|6.28|5.27|
|1900|78|84|4.72|1.95|4.25|2.30|0.57|1.43|5.27|3.84|
|1850|153|113|1.87|2.42|2.75|0.33|0.00|0.17|4.95|4.78|
|1800|175|132|1.66|2.68|2.87|0.19|0.00|0.09|4.59|4.50|
|1770|||||||||||
|1750|||||||||||
|1740|162|132|1.89|2.31|2.61|0.30|0.00|0.15|4.12|3.97|
|1700|138|93|1.96|2.17|2.48|0.31|0.00|0.16|4.00|3.84|
|1650|141|92|1.87|2.05|1.98|0.00|0.00|0.00|3.97|3.97|
|1600|148|98|1.80|2.31|2.24|0.00|0.00|0.00|3.57|3.57|
|1550|130|95|2.18|2.27|2.54|0.27|0.00|0.14|3.35|3.21|
|1500|167|118|1.66|2.2|2.22|0.02|0.00|0.01|3.37|3.36|
|1450|138|91|1.92|2.31|2.65|0.34|0.00|0.17|2.99|2.82|
|1400|149|88|1.66|2.97|3.26|0.29|0.00|0.15|2.22|2.07|
|1350|156|88|1.53|2.72|2.75|0.03|0.00|0.01|2.37|2.36|
|1300|127|81|2.05|2.55|3.16|0.61|0.00|0.31|2.26|1.95|
|1250|128|76|1.93|2.51|2.96|0.45|0.00|0.22|2.12|1.90|
|1200|139|90|1.87|2.81|3.34|0.53|0.00|0.26|1.70|1.44|
|1,180|148|107|1.89|2.84|3.41|0.57|0.00|0.29|1.60|1.31|
|1150|160|133|1.93|2.88|3.52|0.64|0.00|0.32|1.44|1.12|
|1100|222|224|1.59|2.84|2.98|0.14|0.00|0.07|1.42|1.35|
|1050|188|201|1.94|2.61|3.13|0.52|0.00|0.26|1.46|1.20|
|1000|185|277|2.48|2.53|3.62|1.09|0.00|0.55|1.31|0.76|
|950|170|161|1.98|2.24|2.61|0.37|0.00|0.19|1.42|1.23|
|900|162|154|2.09|2.16|2.60|0.44|0.00|0.22|1.26|1.04|
|850|183|178|1.87|2.41|2.74|0.33|0.00|0.17|0.87|0.70|
|800|199|162|1.54|2.4|2.35|0.00|0.00|0.00|0.77|0.77|
||||||||||||
| =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.89**<br> <br> <br>| =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.89**<br> <br> <br>| =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.89**<br> <br> <br>| =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.89**<br> <br> <br>| =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.89**<br> <br> <br>| =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.89**<br> <br> <br>| =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.89**<br> <br> <br>| =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.89**<br> <br> <br>| =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.89**<br> <br> <br>| =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.89**<br> <br> <br>| =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.89**<br> <br> <br>|

victor **.** santtiz@gmail.com - Whatsapp: +39 351 644 6334 +56 99 252 4610 Pág. 30 de 43

**PROYECTO DEFENSAS FLUVIALES RIO ELQUI. VERIFICACIÓN DEFENSA RIBERA SUR**

**SECTOR RUTA 5 - DESEMBOCADURA RIO ELQUI** ANEXO 2 EST. BASICOS - SALIDAS HEC RAS_CON PROYECTO

**TABLA 3-5 Socavación General; Tr= 2 años - SIN Proyecto**

|Dist.<br>Acum.|Parámetros|Col3|Col4|Col5|PROFUNDIDAD SOCAV. S= hs - h0 (m)|Col7|Col8|Col9|Cota (msnm)|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**Dist.**<br>**Acum.**|** A (m2)**|**B (m)**||**ho (m)**|**hs (m)**|**Lischtvan**|**Neill**|**Adop**|** Fondo**|**Socav**|
|1,970|37.4|72.1|3.52|1.76|3.16|1.40|0.00|0.70|6.28|5.58|
|1,900|25.7|58.9|5.77|1.23|2.92|1.69|0.20|0.94|5.27|4.33|
|1,850|49.8|69.2|2.13|1.33|1.51|0.18|0.00|0.09|4.95|4.86|
|1,800|57.7|72.7|1.72|1.55|1.55|0.00|0.00|0.00|4.59|4.59|
|1,770|0.0|0.0|||||||||
|1,750|0.0|0.0|||||||||
|1,740|47.6|84.9|2.63|1.29|1.70|0.41|0.00|0.21|4.25|4.04|
|1,700|47.8|72.0|2.34|1.2|1.42|0.22|0.00|0.11|4.12|4.01|
|1,650|56.1|69.1|1.74|1.17|0.96|0.00|0.00|0.00|4.00|4.00|
|1,600|58.7|73.1|1.67|1.08|0.84|0.00|0.00|0.00|3.97|3.97|
|1,550|59.2|77.7|1.72|1.35|1.15|0.00|0.00|0.00|3.57|3.57|
|1,500|43.6|66.8|2.60|1.28|1.67|0.39|0.00|0.19|3.35|3.16|
|1,450|55.2|71.7|1.83|1.11|1.06|0.00|0.00|0.00|3.37|3.37|
|1,400|44.8|73.6|2.64|1.21|1.57|0.36|0.00|0.18|2.99|2.81|
|1,350|51.3|65.6|1.95|1.79|2.06|0.27|0.00|0.13|2.22|2.09|
|1,300|57.5|64.3|1.59|1.52|1.43|0.00|0.00|0.00|2.37|2.37|
|1,250|44.1|54.7|2.23|1.38|1.63|0.25|0.00|0.13|2.26|2.13|
|1,200|50.6|51.7|1.70|1.39|1.34|0.00|0.00|0.00|2.12|2.12|
|1,180|58.7|52.1|1.42|1.55|1.29|0.00|0.00|0.00|1.95|1.95|
|1,150|70.7|52.8|0.99|1.78|1.21|0.00|0.00|0.00|1.70|1.70|
|1,100|82.5|52.9|0.77|2|1.16|0.00|0.00|0.00|1.46|1.46|
|1,050|58.6|44.3|1.20|1.93|1.57|0.00|0.00|0.00|1.44|1.44|
|1,000|60.8|46.4|1.17|1.89|1.49|0.00|0.00|0.00|1.42|1.42|
|950|57.0|45.5|1.28|1.77|1.47|0.00|0.00|0.00|1.46|1.46|
|900|43.6|49.3|2.11|1.71|2.06|0.35|0.00|0.18|1.31|1.13|
|850|35.5|49.3|2.99|1.22|1.75|0.53|0.04|0.28|1.42|1.14|
|800|45.9|54.7|2.08|1.19|1.28|0.09|0.00|0.05|1.26|1.21|
|1,970|1,970|1,970|1,970|1,970|1,970|1,970|1,970|1,970|1,970|1,970|
| =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.822**<br> <br> <br>| =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.822**<br> <br> <br>| =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.822**<br> <br> <br>| =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.822**<br> <br> <br>| =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.822**<br> <br> <br>| =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.822**<br> <br> <br>| =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.822**<br> <br> <br>| =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.822**<br> <br> <br>| =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.822**<br> <br> <br>| =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.822**<br> <br> <br>| =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.822**<br> <br> <br>|

victor **.** santtiz@gmail.com - Whatsapp: +39 351 644 6334 +56 99 252 4610 Pág. 31 de 43

**PROYECTO DEFENSAS FLUVIALES RIO ELQUI. VERIFICACIÓN DEFENSA RIBERA SUR**

**SECTOR RUTA 5 - DESEMBOCADURA RIO ELQUI** ANEXO 2 EST. BASICOS - SALIDAS HEC RAS_CON PROYECTO

**TABLA 3-6 Socavación General; Tr= 2 años- CON Proyecto**

|Dist.<br>Acum.|Parámetros|Col3|Col4|Col5|PROFUNDIDAD SOCAV. S= hs - h0 (m)|Col7|Col8|Col9|Cota (msnm)|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**Dist.**<br>**Acum.**|** A (m2)**|**B (m)**||**ho (m)**|**hs (m)**|**Lischtvan**|**Neill**|**Adop**|** Fondo**|**Socav**|
|1970|37.4|72.1|3.52|1.76|3.16|1.40|0.00|0.70|6.28|5.58|
|1900|25.7|58.9|5.77|1.23|2.92|1.69|0.20|0.94|5.27|4.33|
|1850|49.8|69.2|2.13|1.33|1.51|0.18|0.00|0.09|4.95|4.86|
|1800|57.7|72.7|1.72|1.55|1.55|0.00|0.00|0.00|4.59|4.59|
|1770|||||||||||
|1750|||||||||||
|1740|47.6|84.9|2.63|1.29|1.70|0.41|0.00|0.21|4.25|4.04|
|1700|47.8|72.0|2.34|1.2|1.42|0.22|0.00|0.11|4.12|4.01|
|1650|56.1|69.1|1.74|1.17|0.96|0.00|0.00|0.00|4.00|4.00|
|1600|58.7|73.1|1.67|1.08|0.84|0.00|0.00|0.00|3.97|3.97|
|1550|59.3|77.7|1.72|1.35|1.15|0.00|0.00|0.00|3.57|3.57|
|1500|43.6|66.9|2.59|1.28|1.67|0.39|0.00|0.19|3.35|3.16|
|1450|55.5|72.7|1.83|1.11|1.07|0.00|0.00|0.00|3.37|3.37|
|1400|45.0|73.7|2.63|1.21|1.57|0.36|0.00|0.18|2.99|2.81|
|1350|51.9|66.8|1.94|1.79|2.05|0.26|0.00|0.13|2.22|2.09|
|1300|58.2|67.0|1.60|1.52|1.44|0.00|0.00|0.00|2.37|2.37|
|1250|45.1|56.1|2.18|1.39|1.62|0.23|0.00|0.12|2.26|2.14|
|1200|51.8|53.3|1.67|1.4|1.34|0.00|0.00|0.00|2.12|2.12|
|1180|59.4|53.1|1.40|1.55|1.29|0.00|0.00|0.00|1.95|1.95|
|1150|70.7|52.8|0.99|1.78|1.21|0.00|0.00|0.00|1.70|1.70|
|1100|82.5|52.9|0.77|2|1.16|0.00|0.00|0.00|1.46|1.46|
|1050|58.6|44.3|1.21|1.93|1.57|0.00|0.00|0.00|1.44|1.44|
|1000|60.8|46.4|1.17|1.89|1.49|0.00|0.00|0.00|1.42|1.42|
|950|57.0|45.5|1.28|1.76|1.46|0.00|0.00|0.00|1.46|1.46|
|900|43.5|49.2|2.12|1.71|2.07|0.36|0.00|0.18|1.31|1.13|
|850|36|51|2.98|1.22|1.74|0.52|0.03|0.27|1.42|1.15|
|800|46|55|2.08|1.19|1.28|0.09|0.00|0.05|1.26|1.21|
||||||||||||
| =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.822**<br> <br> <br>| =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.822**<br> <br> <br>| =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.822**<br> <br> <br>| =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.822**<br> <br> <br>| =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.822**<br> <br> <br>| =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.822**<br> <br> <br>| =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.822**<br> <br> <br>| =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.822**<br> <br> <br>| =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.822**<br> <br> <br>| =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.822**<br> <br> <br>| =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.822**<br> <br> <br>|

victor **.** santtiz@gmail.com - Whatsapp: +39 351 644 6334 +56 99 252 4610 Pág. 32 de 43

PROYECTO DEFENSAS FLUVIALES - COMUNA LA SERENA

SECTOR RUTA 5 - DESEMBOCADURA RIO ELQUI ANEXO 2 EST. BASICOS - SALIDAS HEC RAS_SIN PROYECTO

### - SALIDAS HEC RAS SECCIONES TRANSVERSALES SIN Y CON PROYECTO NOTA: Las secciones transversales se muestran desde aguas abajo hacia arriba. El lado SUR del río se ve a la derecha.

victor **.** santtiz@gmail.com - Whatsapp: +39 351 644 6334 +56 99 252 4610 Pág. 33 de 43

**PROYECTO DEFENSAS FLUVIALES RIO ELQUI. VERIFICACIÓN DEFENSA RIBERA SUR**

**SECTOR RUTA 5 - DESEMBOCADURA RIO ELQUI** ANEXO 2 EST. BASICOS - SALIDAS HEC RAS_CON PROYECTO

**4.1** **SALIDAS HEC RAS - SECCIONES TRANSVERSALES SIN PROYECTO**

victor **.** santtiz@gmail.com - Whatsapp: +39 351 644 6334 +56 99 252 4610 Pág. 34 de 43

**PROYECTO DEFENSAS FLUVIALES RIO ELQUI. VERIFICACIÓN DEFENSA RIBERA SUR**

**SECTOR RUTA 5 - DESEMBOCADURA RIO ELQUI** ANEXO 2 EST. BASICOS - SALIDAS HEC RAS_CON PROYECTO

victor **.** santtiz@gmail.com - Whatsapp: +39 351 644 6334 +56 99 252 4610 Pág. 35 de 43

**PROYECTO DEFENSAS FLUVIALES RIO ELQUI. VERIFICACIÓN DEFENSA RIBERA SUR**

**SECTOR RUTA 5 - DESEMBOCADURA RIO ELQUI** ANEXO 2 EST. BASICOS - SALIDAS HEC RAS_CON PROYECTO

victor **.** santtiz@gmail.com - Whatsapp: +39 351 644 6334 +56 99 252 4610 Pág. 36 de 43

**PROYECTO DEFENSAS FLUVIALES RIO ELQUI. VERIFICACIÓN DEFENSA RIBERA SUR**

**SECTOR RUTA 5 - DESEMBOCADURA RIO ELQUI** ANEXO 2 EST. BASICOS - SALIDAS HEC RAS_CON PROYECTO

victor **.** santtiz@gmail.com - Whatsapp: +39 351 644 6334 +56 99 252 4610 Pág. 37 de 43

**PROYECTO DEFENSAS FLUVIALES RIO ELQUI. VERIFICACIÓN DEFENSA RIBERA SUR**

**SECTOR RUTA 5 - DESEMBOCADURA RIO ELQUI** ANEXO 2 EST. BASICOS - SALIDAS HEC RAS_CON PROYECTO

victor **.** santtiz@gmail.com - Whatsapp: +39 351 644 6334 +56 99 252 4610 Pág. 38 de 43

PROYECTO DEFENSAS FLUVIALES - COMUNA LA SERENA

SECTOR RUTA 5 - DESEMBOCADURA RIO ELQUI ANEXO 2 EST. BASICOS - SALIDAS HEC RAS_CON PROYECTO

**4.2** **SALIDAS HEC RAS - SECCIONES TRANSVERSALES CON PROYECTO**

victor **.** santtiz@gmail.com - Whatsapp: +39 351 644 6334 +56 99 252 4610 Pág. 39 de 43

**PROYECTO DEFENSAS FLUVIALES RIO ELQUI. VERIFICACIÓN DEFENSA RIBERA SUR**

**SECTOR RUTA 5 - DESEMBOCADURA RIO ELQUI** ANEXO 2 EST. BASICOS - SALIDAS HEC RAS_CON PROYECTO

victor **.** santtiz@gmail.com - Whatsapp: +39 351 644 6334 +56 99 252 4610 Pág. 40 de 43

**PROYECTO DEFENSAS FLUVIALES RIO ELQUI. VERIFICACIÓN DEFENSA RIBERA SUR**

**SECTOR RUTA 5 - DESEMBOCADURA RIO ELQUI** ANEXO 2 EST. BASICOS - SALIDAS HEC RAS_CON PROYECTO

victor **.** santtiz@gmail.com - Whatsapp: +39 351 644 6334 +56 99 252 4610 Pág. 41 de 43

**PROYECTO DEFENSAS FLUVIALES RIO ELQUI. VERIFICACIÓN DEFENSA RIBERA SUR**

**SECTOR RUTA 5 - DESEMBOCADURA RIO ELQUI** ANEXO 2 EST. BASICOS - SALIDAS HEC RAS_CON PROYECTO

victor **.** santtiz@gmail.com - Whatsapp: +39 351 644 6334 +56 99 252 4610 Pág. 42 de 43

**PROYECTO DEFENSAS FLUVIALES RIO ELQUI. VERIFICACIÓN DEFENSA RIBERA SUR**

**SECTOR RUTA 5 - DESEMBOCADURA RIO ELQUI** ANEXO 2 EST. BASICOS - SALIDAS HEC RAS_CON PROYECTO

victor **.** santtiz@gmail.com - Whatsapp: +39 351 644 6334 +56 99 252 4610 Pág. 43 de 43

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1-1: Caudales máximos (m3/s) - Río ELQUI en puente Ruta 5 Norte.****

| Tr (años) | 2 | 5 | 10 | 25 | 50 | 100 |
| --- | --- | --- | --- | --- | --- | --- |
| **Q (m3/s)** | 85 | 215 | 350 | 600 | 860 | **1550** |

**Tabla 1-4: COMPARA Parámetros Hidráulicos. T= 100 años (Q=1550 m3/s)****

| River<br>Sta | Eje Hidráulico (msnm) | Col3 | Col4 | Velocidad Canal Principal<br>(m/s) | Col6 | Col7 | Ancho Superficial Canal<br>principal (m) | Col9 | Col10 | No de Froude Canal<br>principa | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **River**<br>**Sta** | **SIN**<br>**Proy** | **CON**<br>**Proy** | **DIFERENCIA** | **SIN**<br>**Proy** | **CON**<br>**Proy** | **DIFERENCIA** | **SIN**<br>**Proy** | **CON**<br>**Proy** | **DIFERENCIA** | **SIN**<br>**Proy** | **CON**<br>**Proy** | **DIFERENCIA** |
| 1,970 | 10.00 | 10.00 | **0.00** | 6.24 | 6.24 | **0.00** | 120 | 120 | **0.00** | 1.39 | 1.39 | **0.00** |
| 1,900 | 8.73 | 8.73 | **0.00** | 6.65 | 6.65 | **0.00** | 112 | 112 | **0.00** | 1.49 | 1.49 | **0.00** |
| 1,850 | 9.60 | 9.30 | -0.30 | 3.56 | 3.94 | 0.38 | 125 | 125 | 0.00 | 0.61 | 0.71 | 0.10 |
| 1,800 | 9.67 | 9.37 | -0.30 | 2.82 | 3.11 | 0.29 | 167 | 168 | 0.81 | 0.50 | 0.58 | 0.08 |
| 1,770 | 9.35 | 8.96 | -0.40 | 3.49 | 3.69 | 0.20 | 130 | 142 | 11.94 | 0.55 | 0.55 | 0.01 |
| 1,750 | 9.34 | 9.05 | -0.29 | 3.30 | 3.06 | -0.24 | 126 | 153 | 27.42 | 0.53 | 0.50 | -0.03 |
| 1,740 | 9.33 | 9.09 | -0.24 | 3.20 | 2.75 | -0.45 | 124 | 159 | 35.16 | 0.52 | 0.47 | -0.05 |
| 1,700 | 9.22 | 8.93 | -0.29 | 3.36 | 3.08 | -0.28 | 106 | 132 | 25.56 | 0.52 | 0.51 | -0.01 |
| 1,650 | 7.98 | 8.16 | 0.18 | 5.64 | 4.65 | -0.99 | 74 | 93 | 18.45 | 0.96 | 0.80 | -0.16 |
| 1,600 | 7.70 | 7.54 | -0.16 | 5.65 | 5.37 | -0.28 | 77 | 92 | 15.00 | 0.98 | 0.98 | 0.00 |
| 1,550 | 7.04 | 7.57 | 0.53 | 6.10 | 4.62 | -1.48 | 97 | 103 | 6.10 | 1.21 | 0.84 | -0.37 |
| 1,500 | 7.87 | 7.77 | -0.10 | 3.49 | 3.45 | -0.04 | 107 | 117 | 9.94 | 0.61 | 0.62 | 0.01 |
| 1,450 | 7.85 | 7.79 | -0.06 | 3.11 | 2.87 | -0.24 | 111 | 125 | 14.07 | 0.52 | 0.49 | -0.03 |
| 1,400 | 7.64 | 7.54 | -0.10 | 3.28 | 3.22 | -0.06 | 151 | 164 | 12.36 | 0.61 | 0.61 | 0.00 |
| 1,350 | 7.12 | 7.10 | -0.02 | 4.28 | 4.01 | -0.27 | 115 | 129 | 13.49 | 0.81 | 0.76 | -0.05 |
| 1,300 | 7.21 | 7.13 | -0.08 | 3.30 | 3.28 | -0.02 | 158 | 166 | 7.90 | 0.64 | 0.65 | 0.01 |
| 1,250 | 6.86 | 6.78 | -0.08 | 3.77 | 3.72 | -0.05 | 185 | 198 | 12.99 | 0.86 | 0.85 | -0.01 |
| 1,200 | 6.37 | 6.42 | 0.05 | 4.04 | 3.63 | -0.41 | 230 | 245 | 14.71 | 1.01 | 0.88 | -0.13 |
| 1,180 | 6.27 | 6.35 | 0.09 | 4.20 | 3.75 | -0.44 | 174 | 183 | 8.83 | 0.93 | 0.80 | -0.13 |
| 1,150 | 6.11 | 6.25 | 0.14 | 4.43 | 3.94 | -0.49 | 90 | 90 | 0.00 | 0.81 | 0.69 | -0.12 |
| 1,100 | 5.45 | 5.47 | 0.02 | 5.22 | 5.17 | -0.05 | 88 | 88 | 0.00 | 1.00 | 0.99 | -0.01 |
| 1,050 | 5.22 | 5.23 | 0.01 | 4.75 | 4.73 | 0.01 | 133 | 133 | 0.00 | 1.04 | 1.04 | 0.00 |
| 1,000 | 5.45 | 5.47 | 0.02 | 2.72 | 2.69 | 0.02 | 235 | 235 | 0.00 | 0.59 | 0.58 | -0.01 |
| 950 | 5.08 | 4.95 | -0.13 | 3.35 | 3.66 | -0.13 | 239 | 239 | 0.00 | 0.80 | 0.91 | 0.11 |
| 900 | 5.12 | 5.11 | -0.01 | 2.07 | 2.07 | -0.01 | 350 | 350 | 0.00 | 0.50 | 0.50 | 0.00 |
| 850 | 4.85 | 4.85 | **0.00** | 2.93 | 2.92 | **0.00** | 161 | 161 | **0.00** | 0.62 | 0.62 | **0.00** |
| 800 | 4.66 | 4.66 | **0.00** | 3.11 | 3.10 | **0.00** | 159 | 159 | **0.00** | 0.66 | 0.66 | **0.00** |
|  |  |  |  |  |  |  |  |  |  |  |  |  |
| PROMEDIO EN TRAMO DEFENSA Km 1+750 al Km 1+180 = 570 metros | PROMEDIO EN TRAMO DEFENSA Km 1+750 al Km 1+180 = 570 metros | PROMEDIO EN TRAMO DEFENSA Km 1+750 al Km 1+180 = 570 metros | PROMEDIO EN TRAMO DEFENSA Km 1+750 al Km 1+180 = 570 metros | PROMEDIO EN TRAMO DEFENSA Km 1+750 al Km 1+180 = 570 metros | PROMEDIO EN TRAMO DEFENSA Km 1+750 al Km 1+180 = 570 metros | PROMEDIO EN TRAMO DEFENSA Km 1+750 al Km 1+180 = 570 metros | PROMEDIO EN TRAMO DEFENSA Km 1+750 al Km 1+180 = 570 metros | PROMEDIO EN TRAMO DEFENSA Km 1+750 al Km 1+180 = 570 metros | PROMEDIO EN TRAMO DEFENSA Km 1+750 al Km 1+180 = 570 metros | PROMEDIO EN TRAMO DEFENSA Km 1+750 al Km 1+180 = 570 metros | PROMEDIO EN TRAMO DEFENSA Km 1+750 al Km 1+180 = 570 metros | PROMEDIO EN TRAMO DEFENSA Km 1+750 al Km 1+180 = 570 metros |
| Prom | 7.70 | **7.66** | -0.04 | 4.05 | **3.68 ** | -0.37 | 131 | **147** | 15.86 | 0.76 | **0.70** | -0.07 |
|  |  |  | **-0.5%** |  |  | **-9.3%** |  |  | **12.1%** |  |  | **-8.8%** |
|  |  |  |  |  |  |  |  |  |  |  |  |  |
| PROMEDIO EN TRAMO AGUAS ARRIBA Km 1+850 a 1+750 = 100 metros | PROMEDIO EN TRAMO AGUAS ARRIBA Km 1+850 a 1+750 = 100 metros | PROMEDIO EN TRAMO AGUAS ARRIBA Km 1+850 a 1+750 = 100 metros | PROMEDIO EN TRAMO AGUAS ARRIBA Km 1+850 a 1+750 = 100 metros | PROMEDIO EN TRAMO AGUAS ARRIBA Km 1+850 a 1+750 = 100 metros | PROMEDIO EN TRAMO AGUAS ARRIBA Km 1+850 a 1+750 = 100 metros | PROMEDIO EN TRAMO AGUAS ARRIBA Km 1+850 a 1+750 = 100 metros | PROMEDIO EN TRAMO AGUAS ARRIBA Km 1+850 a 1+750 = 100 metros | PROMEDIO EN TRAMO AGUAS ARRIBA Km 1+850 a 1+750 = 100 metros | PROMEDIO EN TRAMO AGUAS ARRIBA Km 1+850 a 1+750 = 100 metros | PROMEDIO EN TRAMO AGUAS ARRIBA Km 1+850 a 1+750 = 100 metros | PROMEDIO EN TRAMO AGUAS ARRIBA Km 1+850 a 1+750 = 100 metros | PROMEDIO EN TRAMO AGUAS ARRIBA Km 1+850 a 1+750 = 100 metros |
| Prom | 7.34 | 7.27 | -0.07 | 3.87 | 3.67 | -0.22 | 147 | 158 | 10.21 | 0.74 | 0.71 | -0.03 |
|  |  |  | **-3.5%** |  |  | **8.8%** |  |  | **3.0%** |  |  | **11.2%** |
|  |  |  |  |  |  |  |  |  |  |  |  |  |
| ROMEDIO EN TRAMO AGUAS ABAJO Km 1+180 a 0+900) = 280 metros | ROMEDIO EN TRAMO AGUAS ABAJO Km 1+180 a 0+900) = 280 metros | ROMEDIO EN TRAMO AGUAS ABAJO Km 1+180 a 0+900) = 280 metros | ROMEDIO EN TRAMO AGUAS ABAJO Km 1+180 a 0+900) = 280 metros | ROMEDIO EN TRAMO AGUAS ABAJO Km 1+180 a 0+900) = 280 metros | ROMEDIO EN TRAMO AGUAS ABAJO Km 1+180 a 0+900) = 280 metros | ROMEDIO EN TRAMO AGUAS ABAJO Km 1+180 a 0+900) = 280 metros | ROMEDIO EN TRAMO AGUAS ABAJO Km 1+180 a 0+900) = 280 metros | ROMEDIO EN TRAMO AGUAS ABAJO Km 1+180 a 0+900) = 280 metros | ROMEDIO EN TRAMO AGUAS ABAJO Km 1+180 a 0+900) = 280 metros | ROMEDIO EN TRAMO AGUAS ABAJO Km 1+180 a 0+900) = 280 metros | ROMEDIO EN TRAMO AGUAS ABAJO Km 1+180 a 0+900) = 280 metros | ROMEDIO EN TRAMO AGUAS ABAJO Km 1+180 a 0+900) = 280 metros |
| Prom | 5.41 | 5.41 | 0.01 | 3.76 | 3.71 | -0.11 | 189.18 | 189.18 | 0.00 | 0.79 | 0.79 | -0.01 |
|  |  |  | **0.2%** |  |  | **-2.9%** |  |  | **0.0%** |  |  | **-0.6%** |

**Tabla 1-5: Parámetros Hidráulicos TR 100 años. Puente Ruta 5 Norte****

| River Sta | Min Ch<br>El<br>(m) | W.S.<br>Elev<br>(m) | Crit<br>W.S.<br>(m) | E.G.<br>Elev<br>(m) | E.G.<br>Slope<br>(m/m) | Vel<br>Chnl<br>(m/s) | Flow<br>Area<br>(m2) | Top W<br>Chnl<br>(m) | Froude<br># Chl | Hydr<br>Radius C<br>(m) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **SIN Proyecto ** | **SIN Proyecto ** | **SIN Proyecto ** | **SIN Proyecto ** | **SIN Proyecto ** | **SIN Proyecto ** | **SIN Proyecto ** | **SIN Proyecto ** | **SIN Proyecto ** | **SIN Proyecto ** | **SIN Proyecto ** |
| 1770 BR U | 4.59 | 9.42 | 8.57 | 10.02 | 0.003036 | 3.42 | 456 | 144 | 0.5 | 2.54 |
| 1770 BR D | 4.25 | 9.28 | 8.18 | 9.92 | 0.002768 | 3.56 | 442 | 116 | 0.59 | 2.89 |
| **Prom 1** | **4.42** | **9.35** | **8.38** | **9.97** | **0.002902** | **3.49** | **449** | **130** | **0.55** | **2.72** |
| **CON Proyecto ** | **CON Proyecto ** | **CON Proyecto ** | **CON Proyecto ** | **CON Proyecto ** | **CON Proyecto ** | **CON Proyecto ** | **CON Proyecto ** | **CON Proyecto ** | **CON Proyecto ** | **CON Proyecto ** |
| 1770 BR U | 4.59 | 8.9 | 8.57 | 9.76 | 0.005415 | 4.12 | 378 | 144 | 0.63 | 2.18 |
| 1770 BR D | 4.25 | 9.02 | 7.9 | 9.55 | 0.002507 | 3.24 | 478 | 140 | 0.47 | 2.71 |
| **Prom 2 ** | **4.42** | **8.96** | **8.24** | **9.66** | **0.00397** | **3.69** | **428** | **142** | **0.55** | **2.44** |
| **DIFERENCIA DE VALORES MEDIOS. CON P - SIN P.** | **DIFERENCIA DE VALORES MEDIOS. CON P - SIN P.** | **DIFERENCIA DE VALORES MEDIOS. CON P - SIN P.** | **DIFERENCIA DE VALORES MEDIOS. CON P - SIN P.** | **DIFERENCIA DE VALORES MEDIOS. CON P - SIN P.** | **DIFERENCIA DE VALORES MEDIOS. CON P - SIN P.** | **DIFERENCIA DE VALORES MEDIOS. CON P - SIN P.** | **DIFERENCIA DE VALORES MEDIOS. CON P - SIN P.** | **DIFERENCIA DE VALORES MEDIOS. CON P - SIN P.** | **DIFERENCIA DE VALORES MEDIOS. CON P - SIN P.** | **DIFERENCIA DE VALORES MEDIOS. CON P - SIN P.** |
| **Dif= CP - SP ** | 0 | -0.40 | -0.14 | -0.31 | 0.00107 | 0.20 | -20.91 | 11.94 | 0.01 | -0.27 |
| **% =**<br>**Dif/Prom 1** |  | -4.2% | -1.7% | -3.2% | 36.8% | 5.6% | -4.7% | 9.2% | 0.9% | -10.1% |

**Tabla 2-1: GASTO SÓLIDO GS - TR= 100 años - SIN Proyecto****

| Dist. Plano (m) | J<br>x1000 | R hid<br>( m ) | Ancho B<br>( m ) | T<br>K/m2 | T-Tc<br>K/m2 | gs<br>K/s/m | GS=Bx gs<br>K/s |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1,970 | 13.58 | 2.04 | 120 | 18.90 | 17.28 | 90.35 | 10,865 |
| 1,900 | 15.61 | 2.02 | 112 | 21.51 | 19.90 | 111.59 | 12,482 |
| 1,850 | 2.22 | 3.41 | 125 | 5.16 | 3.55 | 8.39 | 1,046 |
| 1,800 | 1.49 | 3.25 | 167 | 3.31 | 1.69 | 2.77 | 464 |
| 1,770 | 2.90 | 2.72 | 130 | 5.38 | 3.76 | 9.17 | 1,191 |
| 1,750 | 1.98 | 3.47 | 126 | 4.70 | 3.08 | 6.79 | 855 |
| 1,740 | 1.52 | 3.85 | 124 | 4.00 | 2.38 | 4.62 | 572 |
| 1,700 | 1.51 | 4.19 | 106 | 4.31 | 2.70 | 5.56 | 592 |
| 1,650 | 5.31 | 3.54 | 74 | 12.82 | 11.20 | 47.13 | 3,510 |
| 1,600 | 5.62 | 3.40 | 77 | 13.04 | 11.42 | 48.55 | 3,745 |
| 1,550 | 9.63 | 2.54 | 97 | 16.69 | 15.07 | 73.58 | 7,127 |
| 1,500 | 2.25 | 3.28 | 107 | 5.04 | 3.42 | 7.95 | 854 |
| 1,450 | 1.55 | 3.65 | 111 | 3.85 | 2.23 | 4.20 | 465 |
| 1,400 | 2.33 | 2.91 | 151 | 4.63 | 3.01 | 6.57 | 994 |
| 1,350 | 4.07 | 2.86 | 115 | 7.94 | 6.32 | 19.98 | 2,302 |
| 1,300 | 2.65 | 2.67 | 158 | 4.83 | 3.22 | 7.26 | 1,147 |
| 1,250 | 5.20 | 1.96 | 185 | 6.95 | 5.34 | 15.50 | 2,862 |
| 1,200 | 7.76 | 1.61 | 230 | 8.52 | 6.90 | 22.81 | 5,243 |
| 1,180 | 6.25 | 2.19 | 174 | 9.32 | 7.70 | 26.89 | 4,675 |
| 1,150 | 3.99 | 3.05 | 90 | 8.30 | 6.68 | 21.73 | 1,952 |
| 1,100 | 6.39 | 2.74 | 88 | 11.95 | 10.34 | 41.80 | 3,693 |
| 1,050 | 7.50 | 2.11 | 133 | 10.80 | 9.18 | 34.99 | 4,636 |
| 1,000 | 2.41 | 2.14 | 235 | 3.53 | 1.91 | 3.32 | 780 |
| 950 | 4.69 | 1.78 | 239 | 5.70 | 4.08 | 10.37 | 2,481 |
| 900 | 1.80 | 1.77 | 350 | 2.17 | 0.56 | 0.52 | 184 |
| 850 | 2.63 | 2.24 | 161 | 4.02 | 2.41 | 4.70 | 758 |
| 800 | 2.96 | 2.24 | 159 | 4.53 | 2.91 | 6.25 | 993 |

**Tabla 2-2: GASTO SÓLIDO GS - TR= 100 años - CON Proyecto****

| Dist. Plano (m) | J<br>x1000 | R hid<br>( m ) | Ancho B<br>( m ) | T<br>K/m2 | T-Tc<br>K/m2 | gs<br>K/s/m | GS=Bx gs<br>K/s |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1970 | 13.58 | 2.04 | 120 | 18.90 | 17.28 | 90.35 | 10,865 |
| 1900 | 15.61 | 2.02 | 112 | 21.51 | 19.90 | 111.59 | 12,482 |
| 1850 | 3.08 | 3.11 | 125 | 6.53 | 4.91 | 13.69 | 1,706 |
| 1800 | 2.07 | 2.94 | 168 | 4.14 | 2.53 | 5.05 | 850 |
| 1770 | 3.97 | 2.44 | 142 | 6.61 | 4.99 | 14.02 | 1,988 |
| 1750 | 2.17 | 3.16 | 153 | 4.68 | 3.06 | 6.73 | 1,032 |
| 1740 | 1.27 | 3.52 | 159 | 3.05 | 1.43 | 2.15 | 342 |
| 1700 | 1.48 | 3.73 | 132 | 3.76 | 2.15 | 3.96 | 522 |
| 1650 | 3.71 | 3.47 | 93 | 8.79 | 7.18 | 24.17 | 2,245 |
| 1600 | 5.88 | 3.04 | 92 | 12.19 | 10.58 | 43.25 | 3,984 |
| 1550 | 4.35 | 3.05 | 103 | 9.06 | 7.45 | 25.54 | 2,630 |
| 1500 | 2.32 | 3.14 | 117 | 4.98 | 3.36 | 7.75 | 909 |
| 1450 | 1.39 | 3.52 | 125 | 3.33 | 1.72 | 2.83 | 352 |
| 1400 | 2.35 | 2.82 | 164 | 4.52 | 2.90 | 6.22 | 1,016 |
| 1350 | 3.63 | 2.83 | 129 | 7.00 | 5.39 | 15.73 | 2,024 |
| 1300 | 2.68 | 2.61 | 166 | 4.78 | 3.16 | 7.08 | 1,175 |
| 1250 | 5.12 | 1.95 | 198 | 6.81 | 5.19 | 14.87 | 2,939 |
| 1200 | 5.72 | 1.73 | 245 | 6.75 | 5.13 | 14.63 | 3,577 |
| 1180 | 4.58 | 2.35 | 183 | 7.33 | 5.71 | 17.18 | 3,138 |
| 1150 | 2.87 | 3.27 | 90 | 6.41 | 4.79 | 13.18 | 1,184 |
| 1100 | 6.21 | 2.76 | 88 | 11.70 | 10.09 | 40.28 | 3,559 |
| 1050 | 7.43 | 2.11 | 133 | 10.70 | 9.08 | 34.42 | 4,561 |
| 1000 | 2.33 | 2.16 | 235 | 3.43 | 1.82 | 3.08 | 724 |
| 950 | 6.20 | 1.65 | 239 | 6.98 | 5.36 | 15.62 | 3,736 |
| 900 | 1.81 | 1.77 | 350 | 2.18 | 0.57 | 0.54 | 189 |
| 850 | 2.62 | 2.24 | 161 | 4.00 | 2.39 | 4.63 | 748 |
| 800 | 2.96 | 2.24 | 159 | 4.52 | 2.90 | 6.22 | 987 |

**Tabla 2-3: Gasto Sólido GS - TR= 10 años - SIN Proyecto****

| Dist. Plano (m) | J<br>x1000 | R hid<br>( m ) | Ancho B<br>( m ) | T<br>K/m2 | T-Tc<br>K/m2 | gs<br>K/s/m | GS=Bx gs<br>K/s |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1,970 | 8.96 | 0.99 | 112 | 6.06 | 4.44 | 11.76 | 1,318 |
| 1,900 | 20.29 | 0.92 | 84 | 12.73 | 11.12 | 46.62 | 3,937 |
| 1,850 | 3.15 | 1.35 | 113 | 2.90 | 1.29 | 1.84 | 208 |
| 1,800 | 2.50 | 1.32 | 132 | 2.25 | 0.63 | 0.63 | 83 |
| 1,770 |  |  |  |  |  |  |  |
| 1,750 |  |  |  |  |  |  |  |
| 1,740 | 3.24 | 1.39 | 106 | 3.07 | 1.46 | 2.21 | 235 |
| 1,700 | 3.20 | 1.72 | 74 | 3.76 | 2.14 | 3.95 | 294 |
| 1,650 | 2.89 | 1.73 | 77 | 3.42 | 1.80 | 3.03 | 234 |
| 1,600 | 2.81 | 1.61 | 89 | 3.08 | 1.47 | 2.23 | 198 |
| 1,550 | 4.02 | 1.49 | 85 | 4.08 | 2.47 | 4.88 | 414 |
| 1,500 | 2.28 | 1.53 | 104 | 2.38 | 0.76 | 0.84 | 87 |
| 1,450 | 3.16 | 1.66 | 79 | 3.58 | 1.96 | 3.46 | 273 |
| 1,400 | 2.37 | 1.85 | 75 | 2.99 | 1.38 | 2.03 | 153 |
| 1,350 | 1.99 | 1.89 | 81 | 2.56 | 0.95 | 1.16 | 94 |
| 1,300 | 3.97 | 1.68 | 69 | 4.55 | 2.94 | 6.33 | 434 |
| 1,250 | 3.90 | 1.83 | 60 | 4.87 | 3.25 | 7.38 | 446 |
| 1,200 | 3.60 | 1.52 | 86 | 3.73 | 2.12 | 3.87 | 331 |
| 1,180 | 3.42 | 1.39 | 104 | 3.25 | 1.64 | 2.63 | 274 |
| 1,150 | 3.16 | 1.20 | 133 | 2.59 | 0.97 | 1.20 | 160 |
| 1,100 | 2.22 | 0.99 | 224 | 1.50 | -0.12 | 0.00 | 0 |
| 1,050 | 3.38 | 0.93 | 201 | 2.14 | 0.53 | 0.48 | 96 |
| 1,000 | 5.55 | 0.67 | 277 | 2.54 | 0.92 | 1.11 | 307 |
| 950 | 2.93 | 1.05 | 161 | 2.10 | 0.48 | 0.42 | 68 |
| 900 | 3.83 | 1.05 | 154 | 2.74 | 1.13 | 1.51 | 232 |
| 850 | 3.16 | 1.03 | 178 | 2.22 | 0.60 | 0.59 | 105 |
| 800 | 2.13 | 1.22 | 162 | 1.77 | 0.16 | 0.08 | 13 |

**Tabla 2-4: Gasto Sólido GS - TR= 10 años - CON Proyecto****

| Dist. Plano (m) | J<br>x1000 | R hid<br>( m ) | Ancho B<br>( m ) | T<br>K/m2 | T-Tc<br>K/m2 | gs<br>K/s/m | GS=Bx gs<br>K/s |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **CON PROYECTO TR= 10 años** | **CON PROYECTO TR= 10 años** | **CON PROYECTO TR= 10 años** | **CON PROYECTO TR= 10 años** | **CON PROYECTO TR= 10 años** | **CON PROYECTO TR= 10 años** | **CON PROYECTO TR= 10 años** | **CON PROYECTO TR= 10 años** |
| 1,970 | 8.96 | 0.99 | 112 | 6.05 | 4.44 | 11.76 | 1,318 |
| 1,900 | 20.29 | 0.92 | 84 | 12.73 | 11.12 | 46.61 | 3,937 |
| 1,850 | 3.16 | 1.35 | 113 | 2.91 | 1.29 | 1.85 | 209 |
| 1,800 | 2.50 | 1.32 | 132 | 2.25 | 0.63 | 0.63 | 83 |
| 1,770 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| 1,750 | 0.00 | 0.00 | 0 | 0.00 | -1.62 | 0.00 | 0 |
| 1,740 | 3.20 | 1.23 | 132 | 2.69 | 1.07 | 1.39 | 184 |
| 1,700 | 3.41 | 1.48 | 93 | 3.44 | 1.82 | 3.09 | 287 |
| 1,650 | 3.07 | 1.53 | 92 | 3.21 | 1.59 | 2.52 | 233 |
| 1,600 | 2.93 | 1.50 | 98 | 3.00 | 1.39 | 2.05 | 201 |
| 1,550 | 4.28 | 1.37 | 95 | 4.00 | 2.39 | 4.64 | 439 |
| 1,500 | 2.39 | 1.41 | 118 | 2.30 | 0.69 | 0.72 | 84 |
| 1,450 | 3.34 | 1.51 | 91 | 3.44 | 1.82 | 3.10 | 282 |
| 1,400 | 2.50 | 1.67 | 88 | 2.85 | 1.23 | 1.72 | 152 |
| 1,350 | 2.13 | 1.76 | 88 | 2.56 | 0.94 | 1.15 | 101 |
| 1,300 | 3.84 | 1.54 | 81 | 4.03 | 2.42 | 4.73 | 385 |
| 1,250 | 3.37 | 1.68 | 76 | 3.86 | 2.24 | 4.23 | 319 |
| 1,200 | 3.09 | 1.54 | 90 | 3.25 | 1.63 | 2.62 | 236 |
| 1,180 | 3.12 | 1.40 | 107 | 2.99 | 1.37 | 2.02 | 216 |
| 1,150 | 3.16 | 1.20 | 133 | 2.59 | 0.97 | 1.20 | 160 |
| 1,100 | 2.22 | 0.99 | 224 | 1.50 | -0.12 | 0.00 | 0 |
| 1,050 | 3.38 | 0.93 | 201 | 2.14 | 0.53 | 0.48 | 96 |
| 1,000 | 5.55 | 0.67 | 277 | 2.54 | 0.92 | 1.11 | 308 |
| 950 | 2.92 | 1.05 | 161 | 2.09 | 0.48 | 0.42 | 67 |
| 900 | 3.83 | 1.05 | 154 | 2.74 | 1.13 | 1.51 | 232 |
| 850 | 3.16 | 1.03 | 178 | 2.22 | 0.60 | 0.59 | 105 |
| 800 | 2.13 | 1.22 | 162 | 1.77 | 0.16 | 0.08 | 13 |

**Tabla 2-5: Gasto Sólido GS - TR= 2 años - SIN Proyecto****

| Dist. Plano (m) | J<br>x1000 | R hid<br>( m ) | Ancho B<br>( m ) | T<br>K/m2 | T-Tc<br>K/m2 | gs<br>K/s/m | GS=Bx gs<br>K/s |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1,970 | 11.24 | 0.51 | 72 | 3.91 | 2.29 | 4.37 | 315 |
| 1,900 | 30.32 | 0.43 | 59 | 8.90 | 7.28 | 24.70 | 1,456 |
| 1,850 | 4.10 | 0.72 | 69 | 2.01 | 0.40 | 0.31 | 22 |
| 1,800 | 2.66 | 0.79 | 73 | 1.44 | -0.18 | 0.00 | 0 |
| 1,770 | 0.00 | 0.00 | 0 | 0.00 | -1.62 | 0.00 | 0 |
| 1,750 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| 1,740 | 6.22 | 0.56 | 85 | 2.38 | 0.76 | 0.83 | 71 |
| 1,700 | 4.94 | 0.66 | 72 | 2.22 | 0.61 | 0.60 | 43 |
| 1,650 | 2.73 | 0.81 | 69 | 1.51 | -0.11 | 0.00 | 0 |
| 1,600 | 2.51 | 0.80 | 73 | 1.37 | -0.24 | 0.00 | 0 |
| 1,550 | 2.64 | 0.76 | 78 | 1.37 | -0.25 | 0.00 | 0 |
| 1,500 | 6.09 | 0.65 | 67 | 2.70 | 1.09 | 1.42 | 95 |
| 1,450 | 2.97 | 0.77 | 72 | 1.56 | -0.05 | 0.00 | 0 |
| 1,400 | 6.33 | 0.61 | 74 | 2.63 | 1.02 | 1.29 | 95 |
| 1,350 | 3.40 | 0.78 | 66 | 1.81 | 0.19 | 0.11 | 7 |
| 1,300 | 2.29 | 0.89 | 64 | 1.39 | -0.23 | 0.00 | 0 |
| 1,250 | 4.51 | 0.80 | 55 | 2.46 | 0.85 | 0.98 | 53 |
| 1,200 | 2.61 | 0.98 | 52 | 1.75 | 0.13 | 0.06 | 3 |
| 1,180 | 1.92 | 1.12 | 52 | 1.47 | -0.15 | 0.00 | 0 |
| 1,150 | 0.89 | 1.33 | 53 | 0.80 | -0.81 | 0.00 | 0 |
| 1,100 | 0.53 | 1.55 | 53 | 0.56 | -1.06 | 0.00 | 0 |
| 1,050 | 1.31 | 1.31 | 44 | 1.17 | -0.44 | 0.00 | 0 |
| 1,000 | 1.22 | 1.31 | 46 | 1.09 | -0.53 | 0.00 | 0 |
| 950 | 1.49 | 1.25 | 45 | 1.27 | -0.34 | 0.00 | 0 |
| 900 | 4.06 | 0.88 | 49 | 2.44 | 0.82 | 0.94 | 46 |
| 850 | 7.99 | 0.72 | 49 | 3.93 | 2.31 | 4.42 | 218 |
| 800 | 3.94 | 0.83 | 55 | 2.23 | 0.61 | 0.61 | 33 |

**Tabla 2-6: Gasto Sólido GS - TR= 2 años - CON Proyecto****

| Dist. Plano (m) | J<br>x1000 | R hid<br>( m ) | Ancho B<br>( m ) | T<br>K/m2 | T-Tc<br>K/m2 | gs<br>K/s/m | GS=Bx gs<br>K/s |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1,970 | 11.24 | 0.51 | 72 | 3.91 | 2.29 | 4.37 | 315 |
| 1,900 | 30.32 | 0.43 | 59 | 8.90 | 7.28 | 24.70 | 1,456 |
| 1,850 | 4.10 | 0.72 | 69 | 2.01 | 0.40 | 0.31 | 22 |
| 1,800 | 2.66 | 0.79 | 73 | 1.44 | -0.18 | 0.00 | 0 |
| 1,770 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| 1,750 | 0.00 | 0.00 | 0 | 0.00 | -1.62 | 0.00 | 0 |
| 1,740 | 6.22 | 0.56 | 85 | 2.38 | 0.76 | 0.83 | 71 |
| 1,700 | 4.94 | 0.66 | 72 | 2.22 | 0.61 | 0.60 | 43 |
| 1,650 | 2.73 | 0.81 | 69 | 1.51 | -0.11 | 0.00 | 0 |
| 1,600 | 2.51 | 0.80 | 73 | 1.37 | -0.25 | 0.00 | 0 |
| 1,550 | 2.64 | 0.76 | 78 | 1.37 | -0.25 | 0.00 | 0 |
| 1,500 | 6.06 | 0.65 | 67 | 2.69 | 1.07 | 1.40 | 93 |
| 1,450 | 2.99 | 0.76 | 73 | 1.55 | -0.07 | 0.00 | 0 |
| 1,400 | 6.26 | 0.61 | 74 | 2.61 | 0.99 | 1.24 | 91 |
| 1,350 | 3.37 | 0.77 | 67 | 1.77 | 0.15 | 0.08 | 5 |
| 1,300 | 2.33 | 0.86 | 67 | 1.37 | -0.25 | 0.00 | 0 |
| 1,250 | 4.34 | 0.79 | 56 | 2.34 | 0.73 | 0.78 | 44 |
| 1,200 | 2.53 | 0.97 | 53 | 1.68 | 0.06 | 0.02 | 1 |
| 1,180 | 1.88 | 1.11 | 53 | 1.43 | -0.19 | 0.00 | 0 |
| 1,150 | 0.89 | 1.33 | 53 | 0.81 | -0.81 | 0.00 | 0 |
| 1,100 | 0.53 | 1.55 | 53 | 0.56 | -1.06 | 0.00 | 0 |
| 1,050 | 1.31 | 1.31 | 44 | 1.17 | -0.44 | 0.00 | 0 |
| 1,000 | 1.22 | 1.30 | 46 | 1.08 | -0.53 | 0.00 | 0 |
| 950 | 1.50 | 1.24 | 45 | 1.27 | -0.35 | 0.00 | 0 |
| 900 | 4.09 | 0.88 | 49 | 2.46 | 0.84 | 0.97 | 48 |
| 850 | 7.97 | 0.71 | 51 | 3.86 | 2.25 | 4.23 | 214 |
| 800 | 3.94 | 0.83 | 55 | 2.23 | 0.61 | 0.61 | 33 |

**Tabla 3-1: Socavación General; Tr=100 años - SIN Proyecto****

| Dist.<br>Acum. | Parámetros | Col3 | Col4 | Col5 | PROFUNDIDAD SOCAV. S= hs - h0 (m) | Col7 | Col8 | Col9 | Cota (msnm) | Col11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Dist.**<br>**Acum.** | ** A (m2)** | **B (m)** |  | **ho (m)** | **hs (m)** | **Lischtvan** | **Neill** | **Adop** | ** Fondo** | **Socav** |
| 1,970 | 247 | 120 | 3.88 | 3.72 | 7.72 | 4.00 | 2.53 | 3.26 | 6.28 | 3.02 |
| 1,900 | 227 | 112 | 4.25 | 3.46 | 7.54 | 4.08 | 2.96 | 3.52 | 5.27 | 1.75 |
| 1,850 | 427 | 125 | 1.60 | 4.65 | 5.20 | 0.55 | 0.83 | 0.69 | 4.95 | 4.26 |
| 1,800 | 546 | 167 | 1.29 | 5.08 | 4.94 | 0.00 | 0.00 | 0.00 | 4.59 | 4.59 |
| 1,770 | 449 | 130 | 1.51 | 4.93 | 5.36 | 0.43 | 0.59 | 0.51 | 4.42 | 3.91 |
| 1,750 | 470 | 126 | 1.37 | 5.03 | 5.10 | 0.07 | 0.43 | 0.25 | 4.31 | 4.06 |
| 1,740 | 481 | 124 | 1.30 | 5.08 | 4.97 | 0.00 | 0.34 | 0.17 | 4.25 | 4.08 |
| 1,700 | 446 | 106 | 1.34 | 5.10 | 5.10 | 0.00 | 0.73 | 0.37 | 4.12 | 3.75 |
| 1,650 | 264 | 74 | 2.53 | 3.98 | 5.45 | 1.47 | 2.52 | 2.00 | 4.00 | 2.00 |
| 1,600 | 263 | 77 | 2.61 | 3.73 | 5.14 | 1.41 | 2.53 | 1.97 | 3.97 | 2.00 |
| 1,550 | 248 | 97 | 3.33 | 3.47 | 5.66 | 2.19 | 2.23 | 2.21 | 3.57 | 1.36 |
| 1,500 | 354 | 107 | 1.97 | 4.52 | 5.89 | 1.37 | 1.66 | 1.51 | 3.35 | 1.84 |
| 1,450 | 405 | 111 | 1.61 | 4.48 | 4.98 | 0.50 | 1.15 | 0.83 | 3.37 | 2.54 |
| 1,400 | 442 | 151 | 1.71 | 4.65 | 5.48 | 0.83 | 0.58 | 0.71 | 2.99 | 2.28 |
| 1,350 | 331 | 115 | 2.32 | 4.9 | 7.38 | 2.48 | 1.69 | 2.09 | 2.22 | 0.13 |
| 1,300 | 423 | 158 | 1.90 | 4.84 | 6.25 | 1.41 | 0.66 | 1.03 | 2.37 | 1.34 |
| 1,250 | 364 | 185 | 2.71 | 4.6 | 7.68 | 3.08 | 0.90 | 1.99 | 2.26 | 0.27 |
| 1,200 | 371 | 230 | 3.03 | 4.25 | 7.57 | 3.32 | 0.72 | 2.02 | 2.12 | 0.10 |
| 1,180 | 333 | 174 | 3.02 | 4.314 | 7.69 | 3.37 | 1.17 | 2.27 | 1.95 | -0.32 |
| 1,150 | 276 | 90 | 2.66 | 4.41 | 7.18 | 2.77 | 2.88 | 2.82 | 1.70 | -1.12 |
| 1,100 | 244 | 88 | 3.23 | 3.99 | 7.32 | 3.33 | 3.39 | 3.36 | 1.46 | -1.90 |
| 1,050 | 280 | 133 | 3.36 | 3.78 | 7.05 | 3.27 | 2.03 | 2.65 | 1.44 | -1.21 |
| 1,000 | 503 | 235 | 1.86 | 4.03 | 4.85 | 0.82 | 0.17 | 0.50 | 1.42 | 0.92 |
| 950 | 425 | 239 | 2.48 | 3.62 | 5.29 | 1.67 | 0.54 | 1.10 | 1.46 | 0.36 |
| 900 | 620 | 350 | 1.71 | 3.81 | 4.24 | 0.43 | 0.00 | 0.21 | 1.31 | 1.10 |
| 850 | 362 | 161 | 2.50 | 3.43 | 4.97 | 1.54 | 1.23 | 1.38 | 1.42 | 0.04 |
| 800 | 357 | 159 | 2.53 | 3.4 | 4.95 | 1.55 | 1.28 | 1.42 | 1.26 | -0.16 |
|  |  |  |  |  |  |  |  |  |  |  |
|  =<br>1 <br>**X =** <br>0.305<br> = 1.27<br> = <br>0.99<br> <br> <br> |  =<br>1 <br>**X =** <br>0.305<br> = 1.27<br> = <br>0.99<br> <br> <br> |  =<br>1 <br>**X =** <br>0.305<br> = 1.27<br> = <br>0.99<br> <br> <br> |  =<br>1 <br>**X =** <br>0.305<br> = 1.27<br> = <br>0.99<br> <br> <br> |  =<br>1 <br>**X =** <br>0.305<br> = 1.27<br> = <br>0.99<br> <br> <br> |  =<br>1 <br>**X =** <br>0.305<br> = 1.27<br> = <br>0.99<br> <br> <br> |  =<br>1 <br>**X =** <br>0.305<br> = 1.27<br> = <br>0.99<br> <br> <br> |  =<br>1 <br>**X =** <br>0.305<br> = 1.27<br> = <br>0.99<br> <br> <br> |  =<br>1 <br>**X =** <br>0.305<br> = 1.27<br> = <br>0.99<br> <br> <br> |  =<br>1 <br>**X =** <br>0.305<br> = 1.27<br> = <br>0.99<br> <br> <br> |  =<br>1 <br>**X =** <br>0.305<br> = 1.27<br> = <br>0.99<br> <br> <br> |

**Tabla 3-2: Socavación General; Tr=100 años - CON Proyecto****

| Dist.<br>Acum. | Parámetros | Col3 | Col4 | Col5 | PROFUNDIDAD SOCAV. S= hs - h0 (m) | Col7 | Col8 | Col9 | Cota (msnm) | Col11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Dist.**<br>**Acum.** | ** A (m2)** | **B (m)** |  | **ho (m)** | **hs (m)** | **Lischtvan** | **Neill** | **Adop** | ** Fondo** | **Socav** |
| 1,970 | 247 | 120 | 3.88 | 3.72 | 7.72 | 4.00 | 2.53 | **3.26** | 6.28 | 3.02 |
| 1,900 | 227 | 112 | 4.25 | 3.46 | 7.54 | 4.08 | 2.96 | **3.52** | 5.27 | 1.75 |
| 1,850 | 389 | 125 | 1.87 | 4.35 | 5.38 | 1.03 | 1.18 | **1.10** | 4.95 | 3.85 |
| 1,800 | 496 | 168 | 1.52 | 4.78 | 5.17 | 0.39 | 0.19 | **0.29** | 4.59 | 4.30 |
| 1,770 | 428 | 142 | 1.74 | 4.535 | 5.36 | 0.82 | 0.74 | **0.78** | 4.42 | 3.64 |
| 1,750 | 517 | 153 | 1.33 | 4.7383 | 4.62 | 0.00 | 0.07 | **0.04** | 4.31 | 4.27 |
| 1,740 | 562 | 159 | 1.19 | 4.84 | 4.35 | 0.00 | 0.00 | **0.00** | 4.25 | 4.25 |
| 1,700 | 492 | 132 | 1.31 | 4.81 | 4.66 | 0.00 | 0.27 | **0.13** | 4.12 | 3.99 |
| 1,650 | 323 | 93 | 2.10 | 4.16 | 4.99 | 0.83 | 1.35 | **1.09** | 4.00 | 2.91 |
| 1,600 | 281 | 92 | 2.63 | 3.57 | 4.89 | 1.32 | 1.97 | **1.64** | 3.97 | 2.33 |
| 1,550 | 316 | 103 | 2.33 | 4 | 5.15 | 1.15 | 1.32 | **1.23** | 3.57 | 2.34 |
| 1,500 | 371 | 117 | 1.94 | 4.42 | 5.65 | 1.23 | 1.39 | **1.31** | 3.35 | 2.04 |
| 1,450 | 442 | 125 | 1.51 | 4.42 | 4.67 | 0.25 | 0.74 | **0.49** | 3.37 | 2.88 |
| 1,400 | 463 | 164 | 1.67 | 4.55 | 5.23 | 0.68 | 0.42 | **0.55** | 2.99 | 2.44 |
| 1,350 | 366 | 129 | 2.11 | 4.88 | 6.84 | 1.96 | 1.25 | **1.60** | 2.22 | 0.62 |
| 1,300 | 435 | 166 | 1.87 | 4.76 | 6.05 | 1.29 | 0.56 | **0.93** | 2.37 | 1.44 |
| 1,250 | 387 | 198 | 2.56 | 4.52 | 7.19 | 2.67 | 0.74 | **1.70** | 2.26 | 0.56 |
| 1,200 | 423 | 245 | 2.54 | 4.3 | 6.71 | 2.41 | 0.46 | **1.44** | 2.12 | 0.68 |
| 1,180 | 372 | 183 | 2.59 | 4.4 | 7.01 | 2.61 | 0.89 | **1.75** | 1.95 | 0.20 |
| 1,150 | 296 | 90 | 2.36 | 4.55 | 6.82 | 2.27 | 2.62 | **2.45** | 1.70 | -0.75 |
| 1,100 | 245 | 88 | 3.20 | 4.01 | 7.33 | 3.32 | 3.37 | **3.34** | 1.46 | -1.88 |
| 1,050 | 281 | 133 | 3.35 | 3.79 | 7.05 | 3.26 | 2.02 | **2.64** | 1.44 | -1.20 |
| 1,000 | 508 | 235 | 1.83 | 4.05 | 4.83 | 0.78 | 0.15 | **0.46** | 1.42 | 0.96 |
| 950 | 395 | 239 | 2.81 | 3.49 | 5.55 | 2.06 | 0.68 | **1.37** | 1.46 | 0.09 |
| 900 | 619 | 350 | 1.71 | 3.8 | 4.23 | 0.43 | 0.00 | **0.22** | 1.31 | 1.09 |
| 850 | 362 | 161 | 2.50 | 3.43 | 4.97 | 1.54 | 1.23 | **1.38** | 1.42 | 0.04 |
| 800 | 357 | 159 | 2.53 | 3.4 | 4.95 | 1.55 | 1.28 | **1.42** | 1.26 | -0.16 |
|  |  |  |  |  |  |  |  |  |  |  |
|  =<br>1 <br>**X =** <br>0.305<br> = 1.27<br> = <br>0.99<br> <br> <br> |  =<br>1 <br>**X =** <br>0.305<br> = 1.27<br> = <br>0.99<br> <br> <br> |  =<br>1 <br>**X =** <br>0.305<br> = 1.27<br> = <br>0.99<br> <br> <br> |  =<br>1 <br>**X =** <br>0.305<br> = 1.27<br> = <br>0.99<br> <br> <br> |  =<br>1 <br>**X =** <br>0.305<br> = 1.27<br> = <br>0.99<br> <br> <br> |  =<br>1 <br>**X =** <br>0.305<br> = 1.27<br> = <br>0.99<br> <br> <br> |  =<br>1 <br>**X =** <br>0.305<br> = 1.27<br> = <br>0.99<br> <br> <br> |  =<br>1 <br>**X =** <br>0.305<br> = 1.27<br> = <br>0.99<br> <br> <br> |  =<br>1 <br>**X =** <br>0.305<br> = 1.27<br> = <br>0.99<br> <br> <br> |  =<br>1 <br>**X =** <br>0.305<br> = 1.27<br> = <br>0.99<br> <br> <br> |  =<br>1 <br>**X =** <br>0.305<br> = 1.27<br> = <br>0.99<br> <br> <br> |

**Tabla 3-3: Socavación General; Tr= 10 años - SIN Proyecto****

| Dist.<br>Acum. | Parámetros | Col3 | Col4 | Col5 | PROFUNDIDAD SOCAV. S= hs - h0 (m) | Col7 | Col8 | Col9 | Cota (msnm) | Col11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Dist.**<br>**Acum.** | ** A (m2)** | **B (m)** |  | **ho (m)** | **hs (m)** | **Lischtvan** | **Neill** | **Adop** | ** Fondo** | **Socav** |
| 1,970 | 112 | 112 | 3.15 | 2.6 | 4.50 | 1.90 | 0.11 | 1.01 | 6.28 | 5.27 |
| 1,900 | 78 | 84 | 4.72 | 1.95 | 4.25 | 2.30 | 0.57 | 1.44 | 5.27 | 3.83 |
| 1,850 | 153 | 113 | 1.87 | 2.42 | 2.75 | 0.33 | 0.00 | 0.17 | 4.95 | 4.78 |
| 1,800 | 175 | 132 | 1.66 | 2.68 | 2.87 | 0.19 | 0.00 | 0.09 | 4.59 | 4.50 |
| 1,770 | 0 | 0 |  |  |  |  |  |  |  |  |
| 1,750 | 0 | 0 |  |  |  |  |  |  |  |  |
| 1,740 | 148 | 106 | 1.90 | 2.29 | 2.60 | 0.31 | 0.00 | 0.15 | 4.12 | 3.97 |
| 1,700 | 128 | 74 | 1.90 | 2.16 | 2.41 | 0.25 | 0.00 | 0.13 | 4.00 | 3.87 |
| 1,650 | 134 | 77 | 1.82 | 2.06 | 1.95 | 0.00 | 0.00 | 0.00 | 3.97 | 3.97 |
| 1,600 | 144 | 89 | 1.76 | 2.34 | 2.24 | 0.00 | 0.00 | 0.00 | 3.57 | 3.57 |
| 1,550 | 127 | 85 | 2.11 | 2.3 | 2.53 | 0.23 | 0.00 | 0.11 | 3.35 | 3.24 |
| 1,500 | 161 | 104 | 1.64 | 2.25 | 2.27 | 0.02 | 0.00 | 0.01 | 3.37 | 3.36 |
| 1,450 | 132 | 79 | 1.88 | 2.35 | 2.66 | 0.31 | 0.00 | 0.16 | 2.99 | 2.83 |
| 1,400 | 141 | 75 | 1.63 | 3.02 | 3.30 | 0.28 | 0.00 | 0.14 | 2.22 | 2.08 |
| 1,350 | 154 | 81 | 1.48 | 2.79 | 2.76 | 0.00 | 0.00 | 0.00 | 2.37 | 2.37 |
| 1,300 | 116 | 69 | 2.12 | 2.57 | 3.27 | 0.70 | 0.04 | 0.37 | 2.26 | 1.89 |
| 1,250 | 111 | 60 | 2.10 | 2.46 | 3.08 | 0.62 | 0.15 | 0.38 | 2.12 | 1.74 |
| 1,200 | 131 | 86 | 2.02 | 2.79 | 3.51 | 0.72 | 0.00 | 0.36 | 1.70 | 1.34 |
| 1,180 | 142 | 104 | 1.98 | 2.83 | 3.51 | 0.69 | 0.00 | 0.34 | 1.60 | 1.25 |
| 1,150 | 160 | 133 | 1.93 | 2.88 | 3.52 | 0.64 | 0.00 | 0.32 | 1.44 | 1.12 |
| 1,100 | 222 | 224 | 1.59 | 2.84 | 2.98 | 0.14 | 0.00 | 0.07 | 1.42 | 1.35 |
| 1,050 | 188 | 201 | 1.94 | 2.61 | 3.13 | 0.52 | 0.00 | 0.26 | 1.46 | 1.20 |
| 1,000 | 185 | 277 | 2.48 | 2.53 | 3.62 | 1.09 | 0.00 | 0.55 | 1.31 | 0.76 |
| 950 | 170 | 161 | 1.99 | 2.24 | 2.61 | 0.37 | 0.00 | 0.19 | 1.42 | 1.23 |
| 900 | 162 | 154 | 2.09 | 2.16 | 2.60 | 0.44 | 0.00 | 0.22 | 1.26 | 1.04 |
| 850 | 183 | 178 | 1.87 | 2.41 | 2.74 | 0.33 | 0.00 | 0.17 | 0.87 | 0.70 |
| 800 | 199 | 162 | 1.54 | 2.4 | 2.35 | 0.00 | 0.00 | 0.00 | 0.77 | 0.77 |
|  |  |  |  |  |  |  |  |  |  |  |
|  =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.89**<br> <br> <br> |  =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.89**<br> <br> <br> |  =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.89**<br> <br> <br> |  =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.89**<br> <br> <br> |  =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.89**<br> <br> <br> |  =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.89**<br> <br> <br> |  =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.89**<br> <br> <br> |  =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.89**<br> <br> <br> |  =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.89**<br> <br> <br> |  =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.89**<br> <br> <br> |  =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.89**<br> <br> <br> |

**Tabla 3-4: Socavación General; Tr= 10 años - CON Proyecto****

| Dist.<br>Acum. | Parámetros | Col3 | Col4 | Col5 | PROFUNDIDAD SOCAV. S= hs - h0 (m) | Col7 | Col8 | Col9 | Cota (msnm) | Col11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Dist.**<br>**Acum.** | ** A (m2)** | **B (m)** |  | **ho (m)** | **hs (m)** | **Lischtvan** | **Neill** | **Adop** | ** Fondo** | **Socav** |
| 1970 | 112 | 112 | 3.15 | 2.6 | 4.50 | 1.90 | 0.11 | 1.01 | 6.28 | 5.27 |
| 1900 | 78 | 84 | 4.72 | 1.95 | 4.25 | 2.30 | 0.57 | 1.43 | 5.27 | 3.84 |
| 1850 | 153 | 113 | 1.87 | 2.42 | 2.75 | 0.33 | 0.00 | 0.17 | 4.95 | 4.78 |
| 1800 | 175 | 132 | 1.66 | 2.68 | 2.87 | 0.19 | 0.00 | 0.09 | 4.59 | 4.50 |
| 1770 |  |  |  |  |  |  |  |  |  |  |
| 1750 |  |  |  |  |  |  |  |  |  |  |
| 1740 | 162 | 132 | 1.89 | 2.31 | 2.61 | 0.30 | 0.00 | 0.15 | 4.12 | 3.97 |
| 1700 | 138 | 93 | 1.96 | 2.17 | 2.48 | 0.31 | 0.00 | 0.16 | 4.00 | 3.84 |
| 1650 | 141 | 92 | 1.87 | 2.05 | 1.98 | 0.00 | 0.00 | 0.00 | 3.97 | 3.97 |
| 1600 | 148 | 98 | 1.80 | 2.31 | 2.24 | 0.00 | 0.00 | 0.00 | 3.57 | 3.57 |
| 1550 | 130 | 95 | 2.18 | 2.27 | 2.54 | 0.27 | 0.00 | 0.14 | 3.35 | 3.21 |
| 1500 | 167 | 118 | 1.66 | 2.2 | 2.22 | 0.02 | 0.00 | 0.01 | 3.37 | 3.36 |
| 1450 | 138 | 91 | 1.92 | 2.31 | 2.65 | 0.34 | 0.00 | 0.17 | 2.99 | 2.82 |
| 1400 | 149 | 88 | 1.66 | 2.97 | 3.26 | 0.29 | 0.00 | 0.15 | 2.22 | 2.07 |
| 1350 | 156 | 88 | 1.53 | 2.72 | 2.75 | 0.03 | 0.00 | 0.01 | 2.37 | 2.36 |
| 1300 | 127 | 81 | 2.05 | 2.55 | 3.16 | 0.61 | 0.00 | 0.31 | 2.26 | 1.95 |
| 1250 | 128 | 76 | 1.93 | 2.51 | 2.96 | 0.45 | 0.00 | 0.22 | 2.12 | 1.90 |
| 1200 | 139 | 90 | 1.87 | 2.81 | 3.34 | 0.53 | 0.00 | 0.26 | 1.70 | 1.44 |
| 1,180 | 148 | 107 | 1.89 | 2.84 | 3.41 | 0.57 | 0.00 | 0.29 | 1.60 | 1.31 |
| 1150 | 160 | 133 | 1.93 | 2.88 | 3.52 | 0.64 | 0.00 | 0.32 | 1.44 | 1.12 |
| 1100 | 222 | 224 | 1.59 | 2.84 | 2.98 | 0.14 | 0.00 | 0.07 | 1.42 | 1.35 |
| 1050 | 188 | 201 | 1.94 | 2.61 | 3.13 | 0.52 | 0.00 | 0.26 | 1.46 | 1.20 |
| 1000 | 185 | 277 | 2.48 | 2.53 | 3.62 | 1.09 | 0.00 | 0.55 | 1.31 | 0.76 |
| 950 | 170 | 161 | 1.98 | 2.24 | 2.61 | 0.37 | 0.00 | 0.19 | 1.42 | 1.23 |
| 900 | 162 | 154 | 2.09 | 2.16 | 2.60 | 0.44 | 0.00 | 0.22 | 1.26 | 1.04 |
| 850 | 183 | 178 | 1.87 | 2.41 | 2.74 | 0.33 | 0.00 | 0.17 | 0.87 | 0.70 |
| 800 | 199 | 162 | 1.54 | 2.4 | 2.35 | 0.00 | 0.00 | 0.00 | 0.77 | 0.77 |
|  |  |  |  |  |  |  |  |  |  |  |
|  =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.89**<br> <br> <br> |  =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.89**<br> <br> <br> |  =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.89**<br> <br> <br> |  =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.89**<br> <br> <br> |  =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.89**<br> <br> <br> |  =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.89**<br> <br> <br> |  =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.89**<br> <br> <br> |  =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.89**<br> <br> <br> |  =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.89**<br> <br> <br> |  =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.89**<br> <br> <br> |  =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.89**<br> <br> <br> |

**Tabla 3-5: Socavación General; Tr= 2 años - SIN Proyecto****

| Dist.<br>Acum. | Parámetros | Col3 | Col4 | Col5 | PROFUNDIDAD SOCAV. S= hs - h0 (m) | Col7 | Col8 | Col9 | Cota (msnm) | Col11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Dist.**<br>**Acum.** | ** A (m2)** | **B (m)** |  | **ho (m)** | **hs (m)** | **Lischtvan** | **Neill** | **Adop** | ** Fondo** | **Socav** |
| 1,970 | 37.4 | 72.1 | 3.52 | 1.76 | 3.16 | 1.40 | 0.00 | 0.70 | 6.28 | 5.58 |
| 1,900 | 25.7 | 58.9 | 5.77 | 1.23 | 2.92 | 1.69 | 0.20 | 0.94 | 5.27 | 4.33 |
| 1,850 | 49.8 | 69.2 | 2.13 | 1.33 | 1.51 | 0.18 | 0.00 | 0.09 | 4.95 | 4.86 |
| 1,800 | 57.7 | 72.7 | 1.72 | 1.55 | 1.55 | 0.00 | 0.00 | 0.00 | 4.59 | 4.59 |
| 1,770 | 0.0 | 0.0 |  |  |  |  |  |  |  |  |
| 1,750 | 0.0 | 0.0 |  |  |  |  |  |  |  |  |
| 1,740 | 47.6 | 84.9 | 2.63 | 1.29 | 1.70 | 0.41 | 0.00 | 0.21 | 4.25 | 4.04 |
| 1,700 | 47.8 | 72.0 | 2.34 | 1.2 | 1.42 | 0.22 | 0.00 | 0.11 | 4.12 | 4.01 |
| 1,650 | 56.1 | 69.1 | 1.74 | 1.17 | 0.96 | 0.00 | 0.00 | 0.00 | 4.00 | 4.00 |
| 1,600 | 58.7 | 73.1 | 1.67 | 1.08 | 0.84 | 0.00 | 0.00 | 0.00 | 3.97 | 3.97 |
| 1,550 | 59.2 | 77.7 | 1.72 | 1.35 | 1.15 | 0.00 | 0.00 | 0.00 | 3.57 | 3.57 |
| 1,500 | 43.6 | 66.8 | 2.60 | 1.28 | 1.67 | 0.39 | 0.00 | 0.19 | 3.35 | 3.16 |
| 1,450 | 55.2 | 71.7 | 1.83 | 1.11 | 1.06 | 0.00 | 0.00 | 0.00 | 3.37 | 3.37 |
| 1,400 | 44.8 | 73.6 | 2.64 | 1.21 | 1.57 | 0.36 | 0.00 | 0.18 | 2.99 | 2.81 |
| 1,350 | 51.3 | 65.6 | 1.95 | 1.79 | 2.06 | 0.27 | 0.00 | 0.13 | 2.22 | 2.09 |
| 1,300 | 57.5 | 64.3 | 1.59 | 1.52 | 1.43 | 0.00 | 0.00 | 0.00 | 2.37 | 2.37 |
| 1,250 | 44.1 | 54.7 | 2.23 | 1.38 | 1.63 | 0.25 | 0.00 | 0.13 | 2.26 | 2.13 |
| 1,200 | 50.6 | 51.7 | 1.70 | 1.39 | 1.34 | 0.00 | 0.00 | 0.00 | 2.12 | 2.12 |
| 1,180 | 58.7 | 52.1 | 1.42 | 1.55 | 1.29 | 0.00 | 0.00 | 0.00 | 1.95 | 1.95 |
| 1,150 | 70.7 | 52.8 | 0.99 | 1.78 | 1.21 | 0.00 | 0.00 | 0.00 | 1.70 | 1.70 |
| 1,100 | 82.5 | 52.9 | 0.77 | 2 | 1.16 | 0.00 | 0.00 | 0.00 | 1.46 | 1.46 |
| 1,050 | 58.6 | 44.3 | 1.20 | 1.93 | 1.57 | 0.00 | 0.00 | 0.00 | 1.44 | 1.44 |
| 1,000 | 60.8 | 46.4 | 1.17 | 1.89 | 1.49 | 0.00 | 0.00 | 0.00 | 1.42 | 1.42 |
| 950 | 57.0 | 45.5 | 1.28 | 1.77 | 1.47 | 0.00 | 0.00 | 0.00 | 1.46 | 1.46 |
| 900 | 43.6 | 49.3 | 2.11 | 1.71 | 2.06 | 0.35 | 0.00 | 0.18 | 1.31 | 1.13 |
| 850 | 35.5 | 49.3 | 2.99 | 1.22 | 1.75 | 0.53 | 0.04 | 0.28 | 1.42 | 1.14 |
| 800 | 45.9 | 54.7 | 2.08 | 1.19 | 1.28 | 0.09 | 0.00 | 0.05 | 1.26 | 1.21 |
| 1,970 | 1,970 | 1,970 | 1,970 | 1,970 | 1,970 | 1,970 | 1,970 | 1,970 | 1,970 | 1,970 |
|  =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.822**<br> <br> <br> |  =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.822**<br> <br> <br> |  =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.822**<br> <br> <br> |  =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.822**<br> <br> <br> |  =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.822**<br> <br> <br> |  =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.822**<br> <br> <br> |  =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.822**<br> <br> <br> |  =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.822**<br> <br> <br> |  =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.822**<br> <br> <br> |  =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.822**<br> <br> <br> |  =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.822**<br> <br> <br> |

**Tabla 3-6: Socavación General; Tr= 2 años- CON Proyecto****

| Dist.<br>Acum. | Parámetros | Col3 | Col4 | Col5 | PROFUNDIDAD SOCAV. S= hs - h0 (m) | Col7 | Col8 | Col9 | Cota (msnm) | Col11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Dist.**<br>**Acum.** | ** A (m2)** | **B (m)** |  | **ho (m)** | **hs (m)** | **Lischtvan** | **Neill** | **Adop** | ** Fondo** | **Socav** |
| 1970 | 37.4 | 72.1 | 3.52 | 1.76 | 3.16 | 1.40 | 0.00 | 0.70 | 6.28 | 5.58 |
| 1900 | 25.7 | 58.9 | 5.77 | 1.23 | 2.92 | 1.69 | 0.20 | 0.94 | 5.27 | 4.33 |
| 1850 | 49.8 | 69.2 | 2.13 | 1.33 | 1.51 | 0.18 | 0.00 | 0.09 | 4.95 | 4.86 |
| 1800 | 57.7 | 72.7 | 1.72 | 1.55 | 1.55 | 0.00 | 0.00 | 0.00 | 4.59 | 4.59 |
| 1770 |  |  |  |  |  |  |  |  |  |  |
| 1750 |  |  |  |  |  |  |  |  |  |  |
| 1740 | 47.6 | 84.9 | 2.63 | 1.29 | 1.70 | 0.41 | 0.00 | 0.21 | 4.25 | 4.04 |
| 1700 | 47.8 | 72.0 | 2.34 | 1.2 | 1.42 | 0.22 | 0.00 | 0.11 | 4.12 | 4.01 |
| 1650 | 56.1 | 69.1 | 1.74 | 1.17 | 0.96 | 0.00 | 0.00 | 0.00 | 4.00 | 4.00 |
| 1600 | 58.7 | 73.1 | 1.67 | 1.08 | 0.84 | 0.00 | 0.00 | 0.00 | 3.97 | 3.97 |
| 1550 | 59.3 | 77.7 | 1.72 | 1.35 | 1.15 | 0.00 | 0.00 | 0.00 | 3.57 | 3.57 |
| 1500 | 43.6 | 66.9 | 2.59 | 1.28 | 1.67 | 0.39 | 0.00 | 0.19 | 3.35 | 3.16 |
| 1450 | 55.5 | 72.7 | 1.83 | 1.11 | 1.07 | 0.00 | 0.00 | 0.00 | 3.37 | 3.37 |
| 1400 | 45.0 | 73.7 | 2.63 | 1.21 | 1.57 | 0.36 | 0.00 | 0.18 | 2.99 | 2.81 |
| 1350 | 51.9 | 66.8 | 1.94 | 1.79 | 2.05 | 0.26 | 0.00 | 0.13 | 2.22 | 2.09 |
| 1300 | 58.2 | 67.0 | 1.60 | 1.52 | 1.44 | 0.00 | 0.00 | 0.00 | 2.37 | 2.37 |
| 1250 | 45.1 | 56.1 | 2.18 | 1.39 | 1.62 | 0.23 | 0.00 | 0.12 | 2.26 | 2.14 |
| 1200 | 51.8 | 53.3 | 1.67 | 1.4 | 1.34 | 0.00 | 0.00 | 0.00 | 2.12 | 2.12 |
| 1180 | 59.4 | 53.1 | 1.40 | 1.55 | 1.29 | 0.00 | 0.00 | 0.00 | 1.95 | 1.95 |
| 1150 | 70.7 | 52.8 | 0.99 | 1.78 | 1.21 | 0.00 | 0.00 | 0.00 | 1.70 | 1.70 |
| 1100 | 82.5 | 52.9 | 0.77 | 2 | 1.16 | 0.00 | 0.00 | 0.00 | 1.46 | 1.46 |
| 1050 | 58.6 | 44.3 | 1.21 | 1.93 | 1.57 | 0.00 | 0.00 | 0.00 | 1.44 | 1.44 |
| 1000 | 60.8 | 46.4 | 1.17 | 1.89 | 1.49 | 0.00 | 0.00 | 0.00 | 1.42 | 1.42 |
| 950 | 57.0 | 45.5 | 1.28 | 1.76 | 1.46 | 0.00 | 0.00 | 0.00 | 1.46 | 1.46 |
| 900 | 43.5 | 49.2 | 2.12 | 1.71 | 2.07 | 0.36 | 0.00 | 0.18 | 1.31 | 1.13 |
| 850 | 36 | 51 | 2.98 | 1.22 | 1.74 | 0.52 | 0.03 | 0.27 | 1.42 | 1.15 |
| 800 | 46 | 55 | 2.08 | 1.19 | 1.28 | 0.09 | 0.00 | 0.05 | 1.26 | 1.21 |
|  |  |  |  |  |  |  |  |  |  |  |
|  =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.822**<br> <br> <br> |  =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.822**<br> <br> <br> |  =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.822**<br> <br> <br> |  =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.822**<br> <br> <br> |  =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.822**<br> <br> <br> |  =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.822**<br> <br> <br> |  =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.822**<br> <br> <br> |  =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.822**<br> <br> <br> |  =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.822**<br> <br> <br> |  =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.822**<br> <br> <br> |  =<br>**1 **<br>**X =**<br>**0.305**<br> =** 1.27**<br> = <br>**0.822**<br> <br> <br> |
