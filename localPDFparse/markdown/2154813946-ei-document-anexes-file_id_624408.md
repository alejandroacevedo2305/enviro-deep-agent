---
title: Sin título
author: pclado
date: D:20191219032447-03'00'
language: es
type: manual
pages: 2
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Estimación del nivel de potencia acústica L W de una hidrolavadora.
  - Referencias:
-->

# Estimación del nivel de potencia acústica L W de una hidrolavadora.

De acuerdo a la revisión bibliográfica realizada por Hutt [Hutt, 2004], existe una publicación

[Barker et al, 1982] en donde se exponen mediciones de ruido producto de la operación de
equipos manuales de limpieza con agua a diferentes presiones de trabajo. Se midió el nivel de
presión sonora a aproximadamente 1,1m de la boquilla de salida del chorro de agua, por bandas
de octava y para equipos con distinta presión de salida (entre 28 y 69 MPa). Los resultados de
esta medición se muestran en la siguiente tabla.

_Tabla 1: Niveles de presión sonora medidos a 1,1m de la salida de chorro de agua._

|Presión de salida<br>(MPa)|Lp @ 1.1m (dB) por bandas de frecuencia en octava (Hz)|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Lp @ 1.1m<br>(dB)|
|---|---|---|---|---|---|---|---|---|---|
|Presión de salida<br>(MPa)|63|125|250|500|1000|2000|4000|8000|8000|
|27.6|76.0|76.0|78.0|81.0|83.0|86.0|88.0|87.0|93.0|
|34.5|75.0|78.0|81.0|84.0|86.0|89.0|91.0|90.0|95.9|
|41.3|76.0|79.0|82.0|86.0|88.0|90.0|92.0|92.0|97.4|
|48.2|79.0|80.0|85.0|88.0|91.0|93.0|95.0|95.0|100.3|
|55.1|80.0|83.0|86.0|90.0|93.0|95.0|97.0|97.0|102.3|
|62|82.0|83.0|88.0|91.0|95.0|97.0|99.0|99.0|104.2|
|68.9|82.0|84.0|89.0<br>|93.0<br>|96.0<br>|99.0<br>|101.0|101.0|106.1|

_Fuente: Barker et al, 1982._

Para una hidrolavadora común, la presión de trabajo usualmente oscila en 13 MPa. En orden de
obtener una estimación del nivel de potencia acústica de una hidrolavadora común, se realizó
una regresión lineal por bandas de octava, obteniendo valores de R [2] - 0,9, lo que implica un buen
ajuste de las ecuaciones obtenidas por regresión respecto de los datos medidos. Las ecuaciones
obtenidas son las siguientes:

L p 63Hz = 0,224P+ 67,424 (1)

L p 125Hz = 0,1972P+ 70,918 (2)

L p 250Hz = 0,2646P+ 71,379 (3)

L p 500Hz = 0,2802P+ 74,058 (4)

L p 1kHz = 0,3127P+ 74,77 (5)

L p 2kHz = 0,3114P+ 77,697 (6)

L p 4kHz = 0,3114P+ 79,697 (7)

L p 8kHz = 0,3373P+ 78,161 (8)

donde P es la presión nominal de trabajo de la hidrolavadora.

Por tanto, para una hidrolavadora común de 13 MPa de presión nominal de trabajo, se obtienen
los siguientes niveles de presión sonora a 1,1m de la salida de agua de la hidrolavadora.

|Col1|Tabla 1: Niveles de presión sonora interior de grupo generador.|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|Presión nominal<br>de trabajo (MPa)|Lp @ 1.1m (dB) por bandas de frecuencia en octava (Hz)|Lp @ 1.1m (dB) por bandas de frecuencia en octava (Hz)|Lp @ 1.1m (dB) por bandas de frecuencia en octava (Hz)|Lp @ 1.1m (dB) por bandas de frecuencia en octava (Hz)|Lp @ 1.1m (dB) por bandas de frecuencia en octava (Hz)|Lp @ 1.1m (dB) por bandas de frecuencia en octava (Hz)|Lp @ 1.1m (dB) por bandas de frecuencia en octava (Hz)|Lp @ 1.1m (dB) por bandas de frecuencia en octava (Hz)|Lp @ 1.1m<br>(dB)|
|Presión nominal<br>de trabajo (MPa)|63|125|250|500|1000|2000|4000|8000|8000|
|13,0|70.3|73.5|74.8|77.7|79.0|81.7|83.7|82.5|88.8|

_Fuente: Elaboración propia._

Para obtener el nivel de potencia acústica de este elemento, se debe aplicar la siguiente

ecuación:

L Wi = L pi −DI+ 11 (9)

donde:

L Wi es el nivel de potencia acústica de la banda “i” de frecuencia en octava,

L pi es el nivel de presión sonora obtenido para la banda “i” de frecuencia en octava,

DI es la corrección por directividad, que es aproximadamente igual a 3.

Finalmente, el nivel de potencia acústica de una hidrolavadora común de 13 MPa de presión
nominal de trabajo, se muestra en la siguiente tabla.

_Tabla 1: Niveles de presión sonora interior de grupo generador._

|Presión nominal<br>de trabajo (MPa)|Lw (dBA) por bandas de frecuencia en octava (Hz)|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Lw (dBA)|
|---|---|---|---|---|---|---|---|---|---|
|Presión nominal<br>de trabajo (MPa)|63|125|250|500|1000|2000|4000|8000|8000|
|13,0|52.1|65.4|74.2|82.5|87.0|90.9|92.7|89.3|**96.7**|

_Fuente: Elaboración propia._

# Referencias:

## 

[Hutt, 2004] Hutt, Rebeca. Literature Review: Noise from High Pressure Water Jetting.

Health and Safety Laboratory, Harpur Hill, Buxton, Debyshire, United Kingdom.

## 

[Barker et al, 1982] Barker C.R. and Cummings A. (University of Missouri-Rolla, U.S.A.)

and Anderson M. (Partek Corporation, U.S.A.). Jet noise measurements on hand held
cleaning equipment. Proceedings of the 6th International Symposium on Cutting
Technology, BHRA Fluid Engineering, April 1982, Paper D1.