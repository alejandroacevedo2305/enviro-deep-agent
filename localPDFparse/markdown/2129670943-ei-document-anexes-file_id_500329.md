---
title: ESTUDIO RIESGO DE INUNDACIÓN
author: Mónica Pinto
date: D:20140819103422-04'00'
language: es
type: report
pages: 17
has_toc: False
has_tables: True
extraction_quality: high
keywords: [CÓDIGO_REV]
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ANEXOS
-->

**STEEL PROJECT**

**LOTE 5, PARCELACION MIRAFLORES**

**ESTUDIO RIESGO DE INUNDACIÓN**

1

**INDICE**

2.1.RIESGO DE INUNDACIÓN .............................................................................................. 3

2.1.1. INTRODUCCIÓN .......................................................................................................... 3

2.1.2 METODOLOGÍA ............................................................................................................ 3

2.1.3 CONCLUSION ............................................................................................................. 11

2.1.4 BIBLIOGRAFÍA CONSULTADA ................................................................................... 12

**INDICE DE CUADROS**

Cuadro 1. Resumen datos geométricos Brazo Secundario Lampa ......................................... 4

Cuadro 2. Estaciones pluviométricas ...................................................................................... 4

Cuadro 3. Área influencia según método de Thiessen ............................................................ 5

Cuadro 4. Precipitación máxima en 24 horas para la cuenca del Estero Lampa ..................... 5

Cuadro 5. Ajustes para distintos períodos de retorno. ............................................................. 6

Cuadro 6. Precipitación efectiva para la Cuenca del Estero Lampa ........................................ 7

Cuadro 7. Estimación caudal para Brazo Secundario ............................................................. 8

**INDICE DE FIGURAS**

Figura 1. Vista parcial cauce seco aledaño a las instalaciones de Espumatex. Se aprecia
basura y vegetación en el mismo cauce. ................................................................................ 9

La Figura 2 ilustra el resultado de la modelización considerando un área aportante de 9,7 km2
............................................................................................................................................. 10

2

**2.1** **RIESGO DE INUNDACIÓN**

**2.1.1 INTRODUCCIÓN**

A continuación se presenta la estimación de crecidas e inundación para el Brazo Secundario
del estero Lampa, ubicado al norte de la confluencia de los esteros Lampa y Colina. La
modelación se realizó en HECGeoRAS® según a los datos entregados por DGA e información
tomada del Plan Maestro de Manejo de Cauce Cuenca estero Lampa.

La estimación del área de inundación en este informe, se realiza para ser presentada como
parte de la Declaración de Impacto Ambiental del proyecto “Industria Metalmecánica”,
propiedad de STEEL PROJECT.

_Objetivos_

_General_

Determinar si el emplazamiento del Proyecto Industria Metalmecánica, en el sector de
Miraflores se ve afectado a inundaciones por crecidas.

_Específicos_

Estimar el caudal y el área de inundación del Brazo Secundario del Estero Lampa.
Identificar el riesgo de inundación del proyecto de Steel Project (Lote 5).

**2.1.2 METODOLOGÍA**

La cartografía empleada en la modelación fue extraída del Plan Maestro, con curvas de nivel
cada 2 m. La base cartográfica está en SAD69.

La cartografía de salida se presenta en WGS84.

La información de las precipitaciones corresponde a la entregada por la DGA. Los datos de
precipitación abarcan desde 1970 hasta 2012.

**1. Variables y Condiciones de Borde Utilizados en la Simulación.**

El programa requiere para la simulación del cauce la caracterización de los perfiles
transversales, el coeficiente de rugosidad de Manning y los caudales a simular. HECGeoRAS® permite la simulación del caudal en el cauce deseado entregando resultados tales como
velocidades y alturas de escurrimiento, áreas de inundación, perfiles transversales y
longitudinales tanto para las diferentes secciones como para el cauce.

3

 - _Geometría del Cauce._

En el caso particular del brazo secundario del Estero Lampa, se generaron 97 perfiles
transversales espaciados cada 100 m, desde la junta con el Estero Lampa hacia aguas
arriba. La longitud del cauce considerado es de 9641,79 m.

 _Coeficiente de Manning._

Los datos de este coeficiente fueron tomados del Plan Maestro de Manejo de Cauces.

 - _Pendiente:_

Respecto de la pendiente, ésta se determinó mediante la siguiente fórmula:

S = h máx - h mín / longitud [m]

La longitud se determinó mediante software de aplicación.

El trazado de la geometría de los ríos, la medición de la longitud y estimación del desnivel se
realizó sobre la cartografía contenida los planos el Plan Maestro de Cauces.

Los datos obtenidos a partir de las distintas estimaciones se resumen en el Cuadro 1.

Cuadro 1. Resumen datos geométricos Brazo Secundario Lampa

|Tramo|n Manning|Col3|Col4|Desnivel<br>(m)|Longitud<br>(m)|Pendiente<br>(m/m)|
|---|---|---|---|---|---|---|
|Tramo<br>|~~Margen~~<br>izquierda<br>|cauce<br>|~~Margen~~<br>derecha<br>|~~Margen~~<br>derecha<br>|~~Margen~~<br>derecha<br>|~~Margen~~<br>derecha<br>|
|~~Estero~~|~~0,05~~|~~0,04~~|~~0,05~~|~~14~~|~~9641,79~~|~~0,001~~|

2. **Determinación de Precipitaciones.**

 - _Precipitaciones_

Las estaciones utilizadas en el presente estudio son las que se señalan en el Cuadro 2:

Cuadro 2. Estaciones pluviométricas

|Nombre Estación|Código DGA|Lat|Long|Altitud<br>msnm|
|---|---|---|---|---|
|~~Caleu~~<br>|~~05733007-4~~<br>|~~33° 00’ 00”~~<br>|~~70° 59’ 00”~~<br>|~~1120~~<br>|
|~~Embalse Huechún~~<br>|~~05732001-K~~<br>|~~33° 05’ 00”~~<br>|~~70° 48‘ 00”~~<br>|~~556~~<br>|
|~~Embalse Rungue~~<br>|~~05733008-2~~<br>|~~33° 01’ 00”~~<br>|~~70° 54’ 00”~~<br>|~~700~~<br>|
|~~Terrazas DGA~~|~~05730016-7~~|~~33° 26’ 00”~~|~~70° 38’ 00”~~|~~560~~|

Los datos considerados para la lluvia de diseño son las precipitaciones máximas en 24 horas,
abarcando una data entre 1970 y 2012.

Los datos de precipitaciones para cada estación se encuentran en el Anexo I.

4

Se aplicó la estimación de precipitaciones para la cuenca del Estero Lampa usando el método
Thiessen para distintos períodos de retorno. La cuenca del estero Lampa tiene una superficie
de 1356 km [2] . En el Cuadro 3 se indica el área de influencia de cada estación pluviométrica, de
acuerdo con el método anteriormente señalado, el que se aplicó mediante software de
aplicación.

Cuadro 3. Área influencia según método de Thiessen

|Nombre Estación|Área influencia<br>cuenca en km2|%|
|---|---|---|
|~~Caleu~~<br>|96,82|0,071|
|~~Embalse Huechún~~<br>|694,12|0,512|
|~~Embalse Rungue~~<br>|284,49|0,210|
|~~Terrazas DGA~~|280,57|0,207|

Las ponderaciones según el método de Thiessen para cada estación se encuentran en el
Anexo II.

El resultado obtenido de la ponderación de las precipitaciones máximas en 24 horas, según el
método aplicado es el que se muestra en el Cuadro 4:

Cuadro 4. Precipitación máxima en 24 horas para la cuenca del Estero Lampa

5

|Año|mm|
|---|---|
|1970|56,64|
|1971|61,80|
|1972|66,88|
|1973|58,92|
|1974|65,53|
|1975|36,97|
|1976|27,15|
|1977|49,29|
|1978|64,52|
|1979|68,88|
|1980|56,89|
|1981|87,50|
|1982|86,44|
|1983|51,94|
|1984|103,62|
|1985|24,54|
|1986|72,06|
|1987|98,41|
|1988|21,01|
|1989|45,47|
|1990|34,24|
|1991|51,64|

|Año|mm|
|---|---|
|1992|62,07|
|1993|33,42|
|1994|42,69|
|1995|34,64|
|1996|32,00|
|1997|75,47|
|1998|18,63|
|1999|36,46|
|2000|61,26|
|2001|56,58|
|2002|134,06|
|2003|54,73|
|2004|43,45|
|2005|51,02|
|2006|62,15|
|2007|25,26|
|2008|75,77|
|2009|26,94|
|2010|33,56|
|2011|18,17|
|2012|41,31|

En el Cuadro 5 se presentan los datos para cada período de retorno, los que fueron ajustados
usando el método de Gumbel, LogNorm y PearsonIII, evaluando el mejor ajuste o menor
discrepancia a través del test Kolmorogov-Smirnof. Estos cálculos se realizan en R, software de
código libre.

Cuadro 5. Ajustes para distintos períodos de retorno.

6

|Retorno|Gumbel|LogNorm|PearsonIII|
|---|---|---|---|
|2|49,66288|48,51093|47,60994|
|5|71,30945|71,5409|71,40604|
|10|86,64136|87,64853|89,21397|
|15|93,7273|96,99591|99,9783|
|20|99,38887|103,651|107,8319|
|25|103,7498|108,8402|114,0637|
|50|117,1836|125,1822|134,3015|
|100|130,5183|141,9674|156,0393|
|Discrepancia|0,0825|0,1016|0,1168|
|p-value|0,9084|0,7279|0,5604|

El ajuste que presenta menor discrepancia es Gumbel.

Para el cálculo de la precipitación efectiva se utilizó el método de la Curva Número (Manual de
cálculo de crecidas y caudales mínimos en cuencas sin información fluviométrica, 1995).

24500
CN =
254 + S

S es la retención máxima que se obtiene a base de la curva número seleccionada. La Curva
Número se estimó de acuerdo con el Manual de Estándares Técnicos y Económicos para obras
de riego y drenaje.

De tal manera que la fórmula queda como sigue:

24500
S = -254
CN

De acuerdo con el Manual de estándares técnicos, CN tiene un valor ponderado de 75,53 mm.
Para S se obtuvo 82,29 mm.

Para estimar la precipitación efectiva, finalmente, se utilizó la fórmula:

P ef = (P - 0,2 S) [2] / (P + 0,8 S)

Donde:

P ef : precipitación efectiva en mm.
S: retención máxima en mm
P: precipitación media que cae sobre la cuenca.

En este caso, la precipitación media corresponde a cada período de retorno, quedando la
información como sigue en el Cuadro 6:

Cuadro 6. Precipitación efectiva para la Cuenca del Estero Lampa

7

|Retorno|Gumbel|P<br>ef|
|---|---|---|
|2|49,66288|9,54643233|
|5|71,30945|21,9385282|
|10|86,64136|32,3053419|
|15|93,7273|37,4189704|
|20|99,38887|41,626274|
|25|103,7498|44,9332319|
|50|117,1836|55,4359655|
|100|130,5183|66,2578669|

**3. Caudal**

Si bien la cuenca del Estero Lampa tiene una superficie de 1.356 km2, el área considerada
para el presente estudio sólo abarca 9,74 km2, valor determinado mediante software de
aplicación y que corresponde a la microcuenca del Brazo Secundario del mencionado
Estero.

Este se encuentra aguas abajo de la localidad de Lampa y al poniente del mencionado
estero, entre las coordenadas WGS84 328500 E - 6313000 N por el norte y 329270 E6305067 N por el sur.

Para el cálculo del caudal se utilizó el Método Racional, cuya fórmula es la siguiente:

C x I x A
Q =

3,6

Donde:

Q: caudal máximo instantáneo de períodod e retorno T, expresado en m [3] /s.
C: Coeficiente de escorrentía asociado al período de retorno T.
I: intensidad de la lluvia asociada al período de retorno T y una duración igual al tiempo
de concentración de la cuenca pluvial, expresada en mm/h.
A: Área pluvial aportante expresada en km [2] .

Ahora bien, anteriormente se calculó la precipitación efectiva quedando por determinar sólo
la intensidad. El coeficiente de escorrentía está integrado en el cálculo de la precipitación,
quedando la fórmula anterior como sigue:

Q

I x A

= 3,6

Donde:
I = Pef /24

En el Cuadro 7 se indican los caudales obtenidos para cada período de retorno.

**Cuadro 7. Estimación caudal para Brazo** **Secundario**

|Retorno|E mm|mm/h|Área en<br>km2|Q m3/s|
|---|---|---|---|---|
|2|9,546|0,398|~~9,742~~<br>|1,076|
|5|21,939|0,914|~~9,742~~<br>|2,474|
|10|32,305|1,346|~~9,742~~<br>|3,643|
|15|37,419|1,559|~~9,742~~<br>|4,219|
|20|41,626|1,734|~~9,742~~<br>|4,694|
|25|44,933|1,872|~~9,742~~<br>|5,067|
|50|55,436|2,310|~~9,742~~<br>|6,251|
|100|66,258|2,761|~~9,742~~|7,471|

8

**4. Modelización**

Estimados los caudales, rugosidades y pendientes para cada tramo analizado, se procede a
modelar el caudal de crecida en HECGeoRAS®

Se estimó una superficie de inundación de 200 metros hacia cada lado desde el eje del
estero, considerando la presencia de cauces secos hacia ambos lados del Brazo
Secundario, como el que se aprecia en la Figura 1.

Figura 1. Vista parcial cauce seco aledaño a la Parcelación Miraflores. Se aprecia basura y

vegetación en el mismo cauce.

El resultado de la modelización se aprecia en la siguiente figura, para distintos períodos de
retorno: T5, T50 y T100, con un área de inundación de 200 m a cada lado del Brazo
Secundario del Estero Lampa, considerando los límites de esta microcuenca y que los drenes
que circundan la fábrica desaguan hacia el estero Cruces.

9

La Figura 2 ilustra el resultado de la modelización considerando un área aportante de 9,7 km [2]

Según la modelización, todos los períodos analizados (de los cuales en la imagen anterior sólo
se graficaron 3), presentan una distribución similar respecto de la superficie a abarcar.

10

De acuerdo con los datos ingresados al software, el área de inundación llegaría sólo hasta las
proximidades el cauce seco que se sitúa al oriente de la fábrica en los tres períodos de retorno
y a una distancia lineal de 800 m en dirección nor-nororiente.

A su vez, e inmediatamente al oriente de la fábrica y a una distancia sobre los 600 m, se sitúa
el otro límite de inundación para los tres períodos.

El cauce seco que se ubica al oriente de la fábrica sirve de drenaje y desagua en el estero
Cruces.

**2.1.3 CONCLUSION**

La distancia del área de inundación máxima proyectada abarca desde el lecho mayor episódico
hasta ± 400 m desde el eje hacia ambos lados en los distintos períodos de retorno solicitados
(T10, T50 y T100, descartándose la posibilidad de inundación por crecidas del Brazo
Secundario para el proyecto “Industria Metalmecánica” Steel Project.

El cauce que se presenta en la zona, entre el Brazo Secundario y el emplazamiento de la
Parcelación Miraflores, a la que pertenece el lote 5 en análisis, drena hacia el Estero Cruces;
serviría como drenaje natural para las aguas superficiales.

Carolina Muñoz L.

Geógrafa
Mg. Manejo de suelos y aguas

Julio de 2014

11

**2.1.4 BIBLIOGRAFÍA CONSULTADA**

DGA - MOP. 1987. Balance Hídrico.

DGA - MOP. 1995. Manual de cálculo de crecidas y caudales mínimos en cuencas sin
información fluviométrica.

SALGADO, L. 1999. Manual de estándares técnicos y económicos para obras de drenaje.

12

# ANEXOS

Terrazas DGA Huechun Caleu Rungue

**AÑO** **Máxima en 24 horas** **Máxima en 24 horas** **Máxima en 24 horas** **Máxima en 24 horas**

**Fecha** **Precipitación** **Fecha** **Precipitación** **Fecha** **Precipitación** **Fecha** **Precipitación**

**(mm)** **(mm)** **(mm)** **(mm)**

1970 14/07 51,9 28/07 72,0 14/07 59,0

1971 20/06 71,4 20/06 57,0 20/06 53,0

1972 06/05 66,9 30/05 66,0 13/06 67,0

1973 07/07 23,8 06/07 110,0 06/07 86,0

1974 29/06 81,5 30/11 49,0 27/06 52,2

1975 02/07 31,9 05/08 41,0 03/07 41,4

1976 04/06 26,8 04/06 27,5

1977 22/07 32,0 22/07 85,0 22/07 61,0

1978 16/11 49,8 14/07 140,5 14/07 67,5

1979 25/07 54,2 26/07 104,5 26/07 78,0

1980 18/07 34,8 10/04 82,0 18/07 75,0

1981 30/05 85,7 30/05 122,0 30/05 84,0

1982 26/06 58,3 26/06 138,0 15/07 106,5

1983 18/06 45,4 18/05 94,0 06/07 52,0

1984 04/07 69,7 03/07 184,0 03/07 125,0

1985 31/03 26,3 03/07 46,0 28/07 19,5

1986 15/06 44,5 21/08 120,0 27/05 92,1

1987 11/08 86,0 14/07 188,0 13/07 97,0

1988 18/08 20,3 13/08 12,6 13/08 59,0 12/08 29,3

1989 29/04 39,5 26/07 31,0 25/07 115,0 25/07 63,0

1990 30/08 53,0 30/08 28,0 06/08 47,0 18/09 26,6

1991 19/07 39,0 18/06 43,0 18/06 131,0 18/06 58,2

1992 05/06 46,9 25/05 57,0 25/05 101,5 05/06 76,0

1993 14/04 34,4 01/07 24,5 03/06 85,5 03/06 36,5

1994 22/05 27,0 22/05 40,0 22/05 86,0 22/05 50,0

1995 13/08 29,4 04/07 27,0 13/08 58,0 13/08 50,5

1996 02/04 40,1 06/07 20,0 13/06 52,0 06/07 46,5

1997 16/08 58,0 16/08 59,0 19/06 128,0 19/06 115,0

1998 26/04 19,3 26/02 11,7 05/06 53,0 05/06 23,2

1999 07/09 32,7 28/06 33,0 12/09 50,0 28/06 44,0

2000 13/06 67,6 13/06 47,0 13/06 115,0 13/06 71,5

2001 18/07 58,0 29/07 30,0 18/07 64,0 18/07 117,5

2002 03/06 109,4 03/06 139,0 03/06 110,0 03/06 154,5

2003 20/05 55,5 20/05 48,0 07/07 50,0 20/05 72,0

2004 12/11 46,2 12/11 38,0 02/08 55,3 02/08 50,0

2005 27/06 62,3 27/06 42,0 27/08 89,0 27/06 49,0

2006 07/06 62,5 13/10 53,0 13/10 64,0 13/10 83,5

2007 13/06 29,1 13/06 22,0 16/02 53,0 16/02 20,0

2008 15/08 77,7 15/08 54,5 15/08 150,0 15/08 100,5

2009 06/09 20,0 27/06 32,0 27/06 67,0 21/07 7,8

2010 07/11 44,0 17/06 30,0 06/07 37,0 06/07 30,8

2011 29/06 17,5 14/07 15,4 18/06 79,6 10/02 4,7

2012 26/05 21,8 26/05 30,5 26/05 110,7 26/05 63,3

Superficie

Estación m2 ha km2 %

Caleu 96817265,45 9681,73 96,82 0,071

Rungue 284491101,64 28449,11 284,49 0,210

Huechún 694122584,56 69412,26 694,12 0,512

Terrazas 280569103 28056,9103 280,57 0,207

1356000055 135600,0055 1356,00005 1

Ponderación

Año _**Terrazas**_ _**Huechun**_ _**Caleu**_ _**Rungue**_ _**Terrazas**_ _**Huechun**_ _**Caleu**_ _**Rungue**_ _**Suma**_

mm mm mm mm 0,207 0,512 0,071 0,210 mm

1988 20,3 12,6 59,0 29,3 4,20 6,45 4,21 6,15 21,01

1989 39,5 31,0 115,0 63,0 8,17 15,87 8,21 13,22 45,47

1990 53,0 28,0 47,0 26,6 10,97 14,33 3,36 5,58 34,24

1991 39,0 43,0 131,0 58,2 8,07 22,01 9,35 12,21 51,64

1992 46,9 57,0 101,5 76,0 9,70 29,18 7,25 15,94 62,07

1993 34,4 24,5 85,5 36,5 7,12 12,54 6,10 7,66 33,42

1994 27,0 40,0 86,0 50,0 5,59 20,48 6,14 10,49 42,69

1995 29,4 27,0 58,0 50,5 6,08 13,82 4,14 10,59 34,64

1996 40,1 20,0 52,0 46,5 8,30 10,24 3,71 9,76 32,00

1997 58,0 59,0 128,0 115,0 12,00 30,20 9,14 24,13 75,47

1998 19,3 11,7 53,0 23,2 3,99 5,99 3,78 4,87 18,63

1999 32,7 33,0 50,0 44,0 6,77 16,89 3,57 9,23 36,46

2000 67,6 47,0 115,0 71,5 13,99 24,06 8,21 15,00 61,26

2001 58,0 30,0 64,0 117,5 12,00 15,36 4,57 24,65 56,58

2002 109,4 139,0 110,0 154,5 22,64 71,15 7,85 32,41 134,06

2003 55,5 48,0 50,0 72,0 11,48 24,57 3,57 15,11 54,73

2004 46,2 38,0 55,3 50,0 9,56 19,45 3,95 10,49 43,45

2005 62,3 42,0 89,0 49,0 12,89 21,50 6,35 10,28 51,02

2006 62,5 53,0 64,0 83,5 12,93 27,13 4,57 17,52 62,15

2007 29,1 22,0 53,0 20,0 6,02 11,26 3,78 4,20 25,26

2008 77,7 54,5 150,0 100,5 16,08 27,90 10,71 21,09 75,77

2009 20,0 32,0 67,0 7,8 4,14 16,38 4,78 1,64 26,94

2010 44,0 30,0 37,0 30,8 9,10 15,36 2,64 6,46 33,56

2011 17,5 15,4 79,6 4,7 3,62 7,88 5,68 0,99 18,17

2012 21,8 30,5 110,7 63,3 4,51 15,61 7,90 13,28 41,31

Dato corregido según promedio estaciones para igual período

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Resumen datos geométricos Brazo Secundario Lampa**

| Tramo | n Manning | Col3 | Col4 | Desnivel<br>(m) | Longitud<br>(m) | Pendiente<br>(m/m) |
| --- | --- | --- | --- | --- | --- | --- |
| Tramo<br> | ~~Margen~~<br>izquierda<br> | cauce<br> | ~~Margen~~<br>derecha<br> | ~~Margen~~<br>derecha<br> | ~~Margen~~<br>derecha<br> | ~~Margen~~<br>derecha<br> |
| ~~Estero~~ | ~~0,05~~ | ~~0,04~~ | ~~0,05~~ | ~~14~~ | ~~9641,79~~ | ~~0,001~~ |

**Tabla 2.: Estaciones pluviométricas**

| Nombre Estación | Código DGA | Lat | Long | Altitud<br>msnm |
| --- | --- | --- | --- | --- |
| ~~Caleu~~<br> | ~~05733007-4~~<br> | ~~33° 00’ 00”~~<br> | ~~70° 59’ 00”~~<br> | ~~1120~~<br> |
| ~~Embalse Huechún~~<br> | ~~05732001-K~~<br> | ~~33° 05’ 00”~~<br> | ~~70° 48‘ 00”~~<br> | ~~556~~<br> |
| ~~Embalse Rungue~~<br> | ~~05733008-2~~<br> | ~~33° 01’ 00”~~<br> | ~~70° 54’ 00”~~<br> | ~~700~~<br> |
| ~~Terrazas DGA~~ | ~~05730016-7~~ | ~~33° 26’ 00”~~ | ~~70° 38’ 00”~~ | ~~560~~ |

**Tabla 3.: Área influencia según método de Thiessen**

| Nombre Estación | Área influencia<br>cuenca en km2 | % |
| --- | --- | --- |
| ~~Caleu~~<br> | 96,82 | 0,071 |
| ~~Embalse Huechún~~<br> | 694,12 | 0,512 |
| ~~Embalse Rungue~~<br> | 284,49 | 0,210 |
| ~~Terrazas DGA~~ | 280,57 | 0,207 |

**Tabla 4.: Precipitación máxima en 24 horas para la cuenca del Estero Lampa**

| Año | mm |
| --- | --- |
| 1970 | 56,64 |
| 1971 | 61,80 |
| 1972 | 66,88 |
| 1973 | 58,92 |
| 1974 | 65,53 |
| 1975 | 36,97 |
| 1976 | 27,15 |
| 1977 | 49,29 |
| 1978 | 64,52 |
| 1979 | 68,88 |
| 1980 | 56,89 |
| 1981 | 87,50 |
| 1982 | 86,44 |
| 1983 | 51,94 |
| 1984 | 103,62 |
| 1985 | 24,54 |
| 1986 | 72,06 |
| 1987 | 98,41 |
| 1988 | 21,01 |
| 1989 | 45,47 |
| 1990 | 34,24 |
| 1991 | 51,64 |

**Tabla 5.: Ajustes para distintos períodos de retorno.**

| Retorno | Gumbel | LogNorm | PearsonIII |
| --- | --- | --- | --- |
| 2 | 49,66288 | 48,51093 | 47,60994 |
| 5 | 71,30945 | 71,5409 | 71,40604 |
| 10 | 86,64136 | 87,64853 | 89,21397 |
| 15 | 93,7273 | 96,99591 | 99,9783 |
| 20 | 99,38887 | 103,651 | 107,8319 |
| 25 | 103,7498 | 108,8402 | 114,0637 |
| 50 | 117,1836 | 125,1822 | 134,3015 |
| 100 | 130,5183 | 141,9674 | 156,0393 |
| Discrepancia | 0,0825 | 0,1016 | 0,1168 |
| p-value | 0,9084 | 0,7279 | 0,5604 |

**Tabla 6.: Precipitación efectiva para la Cuenca del Estero Lampa**

| Retorno | Gumbel | P<br>ef |
| --- | --- | --- |
| 2 | 49,66288 | 9,54643233 |
| 5 | 71,30945 | 21,9385282 |
| 10 | 86,64136 | 32,3053419 |
| 15 | 93,7273 | 37,4189704 |
| 20 | 99,38887 | 41,626274 |
| 25 | 103,7498 | 44,9332319 |
| 50 | 117,1836 | 55,4359655 |
| 100 | 130,5183 | 66,2578669 |

**Tabla 7.: Estimación caudal para Brazo** **Secundario****

| Retorno | E mm | mm/h | Área en<br>km2 | Q m3/s |
| --- | --- | --- | --- | --- |
| 2 | 9,546 | 0,398 | ~~9,742~~<br> | 1,076 |
| 5 | 21,939 | 0,914 | ~~9,742~~<br> | 2,474 |
| 10 | 32,305 | 1,346 | ~~9,742~~<br> | 3,643 |
| 15 | 37,419 | 1,559 | ~~9,742~~<br> | 4,219 |
| 20 | 41,626 | 1,734 | ~~9,742~~<br> | 4,694 |
| 25 | 44,933 | 1,872 | ~~9,742~~<br> | 5,067 |
| 50 | 55,436 | 2,310 | ~~9,742~~<br> | 6,251 |
| 100 | 66,258 | 2,761 | ~~9,742~~ | 7,471 |
