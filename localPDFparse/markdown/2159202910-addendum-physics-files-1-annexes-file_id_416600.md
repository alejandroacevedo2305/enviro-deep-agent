---
title: Sin título
author: Desconocido
date: D:20231102174242-03'00'
language: es
type: report
pages: 21
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - EXPLORADOR
-->

# EXPLORADOR
## SOLAR

#### Reporte
### Generación Eléctrica Fotovoltaica

##### Reporte
###### Generaci ́on fotovoltaica y datos meteorol ́ogicos

02/11/2023

###### 1 Introducci ́on

En este reporte se presenta informaci ́on sobre el recurso solar basada en la modelaci ́on num ́erica de la
transferencia de radiaci ́on solar en la atm ́osfera y en datos satelitales de alta resoluci ́on. El producto
obtenido ha sido validado con observaciones, sin embargo, no debe ser considerado como definitivo
antes de ser corroborado con mediciones in situ.

El modelo utilizado para la transferencia radiativa en cielo despejado es el modelo CLIRAD-SW, el
cual considera las interacciones de la radiaci ́on con la atm ́osfera por bandas espectrales de manera independiente. El modelo utiliza datos de temperatura, humedad y aerosoles de rean ́alisis meteorol ́ogicos
y datos climatol ́ogicos de CO 2, CH 4 y O 3 .

La informaci ́on para la nubosidad que se ha utilizado proviene de los sat ́elites GOES-EAST para
los a ̃nos 2004 a 2016. Con esta base de datos se ha identificado la nubosidad y sus caracter ́ısticas
radiativas, y a trav ́es de un modelo emp ́ırico se ha modificado el resultado obtenido para una atm ́osfera
con cielo despejado para adaptarlo a una condici ́on de cielo nublado.

A continuaci ́on encontrar ́a los resultados del c ́alculo de la generaci ́on del sistema fotovoltaico evaluado,
de acuerdo a los par ́ametros ingresados, el impacto de la radiaci ́on incidente y las condiciones meteorol ́ogicas en el sitio de inter ́es. Adem ́as se muestra informaci ́on sobre la radiaci ́on (global, directa y
difusa) incidente en el panel de acuerdo a las caracter ́ısticas del arreglo fotovoltaico escogido, la radiaci ́on incidente en un plano horizontal y los promedios de la nubosidad, temperatura y la velocidad
del viento en el sitio seleccionado.

###### 2 Sitio

En esta secci ́on se muestran las caracter ́ısticas topogr ́aficas del sitio escogido por el usuario.

Tabla 1: Ubicaci ́on del sitio seleccionado

**Nombre** Mi Sitio

**Latitud** 40.2663 [o] S

**Longitud** 73.1157 [o] O
**Elevaci ́on** 94 _m_

2

Reporte de
Generaci ́on Fotovoltaica

Figura 1: Mapas del sitio seleccionado

3

Reporte de
Generaci ́on Fotovoltaica

**2.1** **Sombras topogr ́aficas**

Se ha utilizado una base de datos de altura del terreno de 90 [ _m_ ] de resoluci ́on y se ha considerado
la topograf ́ıa dentro de un radio de 180 [ _km_ ] desde el sitio seleccionado para obtener las sombras
proyectadas por los obst ́aculos topogr ́aficos en el entorno del sitio. Este an ́alisis NO considera el
impacto de otro tipo de obst ́aculos como por ejemplo edificios, ́arboles, cables, etc.

Tabla 2: Frecuencia de sombras.

**Mes** Ene Feb Mar Abr May Jun Jul Ago Sep Oct Nov Dic

% 38.7 45.72 50.06 55.12 61.65 62.5 62.5 57.29 52.25 46.53 41.67 38.21

(a) Porcentaje de tiempo con sombras cada mes en horario diurno.

**Hora** 00 01 02 03 04 05 06 07 08 09 10 11

% 100.0 100.0 100.0 100.0 100.0 100.0 75.55 50.84 26.77 0.0 0.0 0.0

**Hora** 12 13 14 15 16 17 18 19 20 21 22 23

% 0.0 0.0 0.0 0.0 0.0 0.0 30.16 57.5 84.34 100.0 100.0 100.0

(b) Porcentaje del a ̃no con sombras en cada hora.

%

%

60

50

40

Ene Feb Mar Abr May Jun Jul Ago Sep Oct Nov Dic

50

0

00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23

Figura 2: A) Ciclo anual de frecuencia de sombras, B) Ciclo diario de frecuencia de sombras.

4

23

22

21

20

19

18

17

16

15

14

13

12

11

10

09

08

07

06

05

04

03

02

01

00

Reporte de
Generaci ́on Fotovoltaica

100

|100|100|100|100|100|100|100|100|100|100|100|100|
|---|---|---|---|---|---|---|---|---|---|---|---|
|100|100|100|100|100|100|100|100|100|100|100|100|
|100|100|100|100|100|100|100|100|100|100|100|100|
|0|97|100|100|100|100|100|100|100|100|100|17|
|0|0|49|100|100|100|100|100|100|38|0|0|
|0|0|0|23|100|100|100|36|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|80|100|100|39|0|0|0|0|
|0|0|53|100|100|100|100|100|54|0|0|0|
|29|100|100|100|100|100|100|100|100|79|0|0|
|100|100|100|100|100|100|100|100|100|100|100|100|
|100|100|100|100|100|100|100|100|100|100|100|100|
|100|100|100|100|100|100|100|100|100|100|100|100|
|100|100|100|100|100|100|100|100|100|100|100|100|
|100|100|100|100|100|100|100|100|100|100|100|100|
|100|100|100|100|100|100|100|100|100|100|100|100|

Ene Feb Mar Abr May Jun Jul Ago Sep Oct Nov Dic

Figura 3: Porcentaje de la hora con sombras durante cada mes.

5

90

80

70

60

50

40

30

20

10

0

%

Reporte de
Generaci ́on Fotovoltaica

###### 3 Generaci ́on Fotovoltaica

**3.1** **Caracter ́ısticas del arreglo fotovoltaico**

Las caracter ́ısticas del sistema ingresadas por el usuario para la simulaci ́on de la generaci ́on fotovoltaica
y los resultados se presentan en esta secci ́on.

Tabla 3: Caracter ́ısticas del sistema fotovoltaico

**Configuraci ́on** HSAT
**Montaje** open rack cell glassback
**Inclinaci ́on** 40 [o]

**Azimut** 0 [o]

**Coef. Temperatura** -0.35 % _/_ [o] _C_
**Ef. Inversor** 96.0 %

**P ́erdidas** 14 %

**Panel seleccionado** **Bifacial**

**Estacionalidad** Sin Estaciones

**Albedo** 0.3

**3.2** **Resultados de la generaci ́on el ́ectrica fotovoltaica**

Tabla 4: Resultados de la generaci ́on fotovoltaica

**Capacidad Instalada** 19379 _kW_
**Total Diario** 103.45 _MWh_

**Total Anual** 37.76 _GWh_

**Factor de Planta** 22.0 %

Tabla 5: Ciclo anual de la generaci ́on fotovoltaica.

**Mes** Ene Feb Mar Abr May Jun Jul Ago Sep Oct Nov Dic

_GWh_ 5.75 4.44 3.61 2.18 1.44 1.11 1.23 1.81 2.85 3.54 4.4 5.4

(a) Promedio de la generaci ́on total en cada mes.

6

Reporte de
Generaci ́on Fotovoltaica

Tabla 6: Ciclo diario de la generaci ́on fotovoltaica.

**Hora** 00 01 02 03 04 05 06 07 08 09 10 11

_MWh_ 0.0 0.0 0.0 0.0 0.0 0.0 0.87 2.79 5.09 7.06 8.12 8.85

**Hora** 12 13 14 15 16 17 18 19 20 21 22 23

_MWh_ 9.38 9.68 9.68 10.15 10.25 9.6 7.06 4.18 0.67 0.0 0.0 0.0

(a) Promedio de la generaci ́on para cada hora.

6

_GWh_

_MWh_

4

2

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|A)|A)|A)|A)|A)|A)|A)|A)|A)|A)|A)|
||||||||||||
||||||||||||

Ene Feb Mar Abr May Jun Jul Ago Sep Oct Nov Dic

5

0

00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23

Figura 4: A) Ciclo anual de generaci ́on, B) Ciclo diario de generaci ́on

Tabla 7: Total anual de la generaci ́on para cada a ̃no en la base de datos.

**A ̃no** 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016

_GWh_ 35.78 36.65 35.42 36.44 39.44 36.34 40.41 40.86 37.69 39.84 35.78 38.09 38.11

7

Reporte de
Generaci ́on Fotovoltaica

40

_GWh_

35

2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016

Figura 5: Variaci ́on interanual de la generaci ́on fotovoltaica.

8

Reporte de
Generaci ́on Fotovoltaica

**3.3** **Radiaci ́on**

Las siguientes tablas y gr ́aficos muestran los promedios de la radiaci ́on global, directa y difusa incidente
sobre un plano horizontal y sobre un plano orientado hacia el norte, con una inclinaci ́on igual a la
latitud del sitio.

**3.3.1** **Insolaci ́on mensual**

Tabla 8: Promedio mensual de la insolaci ́on diaria en unidades de [ _kWh/m_ [2] _/d_ ́ı _a_ ].

**Mes** Ene Feb Mar Abr May Jun Jul Ago Sep Oct Nov Dic

**Directa** 5.12 4.3 2.86 1.52 0.9 0.66 0.68 1.12 2.02 2.4 3.21 4.34

**Difusa** 2.27 1.83 1.48 1.01 0.65 0.5 0.59 0.84 1.37 2.08 2.71 2.75

**Global** 7.39 6.13 4.34 2.53 1.55 1.16 1.27 1.96 3.39 4.48 5.92 7.09

(a) Radiaci ́on incidente en el plano horizontal

**Mes** Ene Feb Mar Abr May Jun Jul Ago Sep Oct Nov Dic

**Directa** 4.41 4.32 3.62 2.5 1.89 1.62 1.56 2.02 2.78 2.6 2.84 3.54

**Difusa** 2.0 1.61 1.31 0.89 0.57 0.44 0.52 0.74 1.21 1.84 2.39 2.43

**Suelo** 0.21 0.17 0.12 0.07 0.04 0.03 0.04 0.05 0.1 0.13 0.17 0.2

**Global** 6.62 6.1 5.05 3.46 2.5 2.09 2.12 2.81 4.09 4.57 5.4 6.17

(b) Radiaci ́on incidente en un plano con inclinaci ́on igual a la latitud del sitio.

Difusa horizontal Directa horizontal

Reflejada del suelo en panel Difusa en panel Directa en panel

**10**

**8**

**6**

**4**

**2**

**0**
**Ene** **Feb** **Mar** **Abr** **May** **Jun** **Jul** **Ago** **Sep** **Oct** **Nov** **Dic**

Figura 6: Promedio mensual de la insolaci ́on diaria incidente en un plano horizontal y en un plano inclinado,
separada en sus componentes directa, difusa y reflejada del suelo.

9

Reporte de
Generaci ́on Fotovoltaica

**3.3.2** **Ciclo diario de radiaci ́on**

Tabla 9: Promedio horario de la radiaci ́on incidente en unidades de [ _W/m_ [2] ].

**Hora** 00 01 02 03 04 05 06 07 08 09 10 11

**Directa** 0.0 0.0 0.0 0.0 0.0 0.0 4.42 28.92 74.69 129.95 189.3 232.04

**Difusa** 0.0 0.0 0.0 0.0 0.0 0.0 3.68 18.99 48.96 96.42 139.91 190.81

**Global** 0.0 0.0 0.0 0.0 0.0 0.0 8.1 47.91 123.65 226.37 329.21 422.85

**Hora** 12 13 14 15 16 17 18 19 20 21 22 23

**Directa** 275.01 306.92 305.24 299.62 258.49 171.29 99.55 39.22 2.0 0.0 0.0 0.0

**Difusa** 213.19 209.52 192.36 158.01 109.02 74.88 32.97 12.11 1.8 0.0 0.0 0.0

**Global** 488.2 516.44 497.6 457.63 367.51 246.17 132.52 51.33 3.8 0.0 0.0 0.0

(a) Radiaci ́on incidente en el plano horizontal.

**Hora** 00 01 02 03 04 05 06 07 08 09 10 11

**Directa** 0.0 0.0 0.0 0.0 0.0 0.0 0.0 5.77 63.12 149.27 225.42 280.27

**Difusa** 0.0 0.0 0.0 0.0 0.0 0.0 3.25 16.77 43.24 85.14 123.54 168.49

**Suelo** 0.0 0.0 0.0 0.0 0.0 0.0 0.23 1.34 3.47 6.36 9.24 11.87

**Global** 0.0 0.0 0.0 0.0 0.0 0.0 3.48 23.88 109.83 240.77 358.2 460.63

**Hora** 12 13 14 15 16 17 18 19 20 21 22 23

**Directa** 331.85 374.79 373.56 377.13 322.6 216.43 78.79 2.13 0.0 0.0 0.0 0.0

**Difusa** 188.25 185.01 169.85 139.53 96.27 66.12 29.12 10.69 1.59 0.0 0.0 0.0

**Suelo** 13.71 14.5 13.97 12.85 10.32 6.91 3.72 1.44 0.11 0.0 0.0 0.0

**Global** 533.81 574.3 557.38 529.51 429.19 289.46 111.63 14.26 1.7 0.0 0.0 0.0

(b) Radiaci ́on incidente en un plano con inclinaci ́on igual a la latitud del sitio.

Difusa horizontal Directa horizontal

Reflejada del suelo en panel Difusa en panel Directa en panel

**600**

**400**

**200**

**0**
**00** **01** **02** **03** **04** **05** **06** **07** **08** **09** **10** **11** **12** **13** **14** **15** **16** **17** **18** **19** **20** **21** **22** **23**

Figura 7: Promedio horario de la radiaci ́on global instant ́anea incidente en un plano horizontal y en un plano
inclinado, separada en sus componentes directa, difusa y reflejada en el suelo.

10

Reporte de
Generaci ́on Fotovoltaica

**3.3.3** **Variabilidad a ̃no a a ̃no**

Tabla 10: Promedio anual de la insolaci ́on diaria en unidades de [ _kWh/m_ [2] _/d_ ́ı _a_ ].

**A ̃no** 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016

**Directa** 2.18 2.27 2.09 2.27 2.74 2.29 2.63 2.75 2.42 2.72 2.18 2.44 2.44

**Difusa** 1.61 1.59 1.62 1.53 1.35 1.44 1.48 1.41 1.48 1.38 1.59 1.5 1.56

**Global** 3.79 3.86 3.71 3.8 4.09 3.73 4.11 4.16 3.9 4.1 3.77 3.94 4.0

(a) Radiaci ́on incidente en el plano horizontal.

**A ̃no** 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016

**Directa** 2.52 2.56 2.41 2.53 2.99 2.71 3.3 3.29 2.84 3.12 2.48 2.78 2.88

**Difusa** 1.42 1.4 1.43 1.35 1.2 1.27 1.3 1.24 1.31 1.22 1.41 1.33 1.37

**Suelo** 0.11 0.11 0.1 0.11 0.11 0.1 0.12 0.12 0.11 0.11 0.11 0.11 0.11

**Global** 4.05 4.07 3.94 3.99 4.3 4.08 4.72 4.65 4.26 4.45 4.0 4.22 4.36

(b) Radiaci ́on incidente en un plano con inclinaci ́on igual a la latitud del sitio.

Difusa horizontal Directa horizontal

Reflejada del suelo en panel Difusa en panel Directa en panel

**4**

**2**

**0**
**2004** **2005** **2006** **2007** **2008** **2009** **2010** **2011** **2012** **2013** **2014** **2015** **2016**

Figura 8: Promedio anual de la insolaci ́on diaria incidente en un plano horizontal y en un plano inclinado para
cada a ̃no de simulaci ́on.

11

Reporte de
Generaci ́on Fotovoltaica

**3.3.4** **Ciclo diario-anual**

Los siguientes gr ́aficos muestran el ciclo diario y el ciclo anual de la radiaci ́on solar incidente. El eje
horizontal indica la hora del d ́ıa (UTC-4) y el eje vertical indica el mes del a ̃no. La escala de colores
indica el valor medio de la radiaci ́on instant ́anea incidente en el panel en [ _W/m_ [2] ] para cada hora y

mes.

23

22

21

20

19

18

17

16

15

14

13

12

11

10

09

08

07

06

05

04

03

02

01

00

|0|0|0|0|0|0|0|0|0|0|0|0|
|---|---|---|---|---|---|---|---|---|---|---|---|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|26|1|0|0|0|0|0|0|0|0|0|19|
|182|130|19|0|0|0|0|0|0|19|109|162|
|356|272|158|35|0|0|0|15|90|148|226|299|
|509|441|294|152|78|45|77|127|192|252|348|450|
|670|589|438|260|158|133|139|214|324|388|514|597|
|797|700|529|336|230|198|186|282|409|494|622|723|
|864|765|595|375|234|175|189|287|451|553|687|813|
|889|776|606|378|249|187|194|292|471|591|737|845|
|848|735|545|336|218|169|177|268|444|586|720|829|
|743|626|476|286|181|136|154|210|389|508|640|739|
|622|501|347|211|127|85|104|153|305|396|500|612|
|446|338|226|126|63|34|43|88|208|294|388|469|
|288|193|98|37|3|0|0|20|95|175|263|317|
|132|60|7|0|0|0|0|0|8|69|132|170|
|16|0|0|0|0|0|0|0|0|2|30|49|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|

Ene Feb Mar Abr May Jun Jul Ago Sep Oct Nov Dic

Figura 9: Promedio de la radiaci ́on global horizontal para cada hora y mes.

12

850

800

750

700

650

600

550

500

450

400

350

300

250

200

150

100

50

0

_W/m_ [2]

Reporte de
Generaci ́on Fotovoltaica

23

22

21

20

19

18

17

16

15

14

13

12

11

10

09

08

07

06

05

04

03

02

01

00

|0|0|0|0|0|0|0|0|0|0|0|0|
|---|---|---|---|---|---|---|---|---|---|---|---|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|11|1|0|0|0|0|0|0|0|0|0|9|
|47|46|10|0|0|0|0|0|0|8|26|38|
|245|228|186|75|0|0|0|43|124|121|141|185|
|436|429|349|254|217|173|229|241|246|247|294|366|
|623|607|529|384|298|295|270|336|409|403|476|533|
|771|737|628|469|384|370|309|409|498|520|598|675|
|851|813|699|495|348|278|271|386|535|584|672|775|
|877|825|710|484|360|284|273|378|560|619|726|811|
|831|773|627|419|303|253|242|343|517|616|705|791|
|713|648|548|361|261|213|236|275|451|525|615|695|
|575|505|398|284|203|150|181|216|361|406|472|558|
|382|319|255|180|124|86|100|144|254|295|355|403|
|202|155|106|65|9|0|0|45|122|166|218|234|
|44|22|4|0|0|0|0|0|8|50|81|77|
|7|0|0|0|0|0|0|0|0|1|14|19|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|

Ene Feb Mar Abr May Jun Jul Ago Sep Oct Nov Dic

850

800

750

700

650

600

550

500

450

400

350

300

250

200

150

100

50

0

_W/m_ [2]

Figura 10: Promedio de la radiaci ́on global incidente en un plano con inclinacio ́on igual a la latitud del sitio,
para cada hora y mes.

13

23

22

21

20

19

18

17

16

15

14

13

12

11

10

09

08

07

06

05

04

03

02

01

00

|0|0|0|0|0|0|0|0|0|0|0|0|
|---|---|---|---|---|---|---|---|---|---|---|---|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|283|4|0|0|0|0|0|0|0|0|0|214|
|610|619|172|0|0|0|0|0|0|204|599|578|
|680|597|565|275|0|0|0|156|497|478|505|552|
|634|639|539|456|449|361|450|435|416|382|433|514|
|671|659|596|465|393|406|343|403|474|422|503|560|
|664|633|545|439|393|397|300|380|422|406|442|534|
|662|623|519|381|282|232|201|286|376|375|421|529|
|635|608|510|335|272|217|189|251|377|347|431|527|
|612|576|436|276|216|193|163|228|332|352|394|499|
|569|527|431|262|211|183|204|206|306|300|324|475|
|575|519|383|276|212|163|205|212|314|279|301|457|
|500|436|340|244|189|143|171|217|319|263|307|433|
|488|401|265|168|23|0|0|135|279|250|297|427|
|386|289|62|0|0|0|0|0|65|212|259|376|
|139|0|0|0|0|0|0|0|0|21|171|266|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|

Ene Feb Mar Abr May Jun Jul Ago Sep Oct Nov Dic

Figura 11: Promedio de la radiaci ́on directa normal para cada hora y mes.

14

Reporte de
Generaci ́on Fotovoltaica

650

600

550

500

450

400

350

300

250

200

150

100

50

0

_W/m_ [2]

Reporte de
Generaci ́on Fotovoltaica

**3.4** **Nubosidad**

La nubosidad es la componente atmosf ́erica que remueve mayor cantidad de radiaci ́on incidente. A
partir de im ́agenes del sat ́elite geostacionado GOES, se ha calculado la frecuencia de nubosidad para
cada hora y mes. Debido a que para la mayor parte del pa ́ıs se utilizan las im ́agenes del canal visible
en la detecci ́on de nubosidad, el dato solo est ́a disponible para las horas diurnas.

Tabla 11: Frecuencia de la nubosidad diurna.

**Mes** Ene Feb Mar Abr May Jun Jul Ago Sep Oct Nov Dic

% 24.09 22.36 24.62 26.39 25.29 24.08 25.22 27.68 27.63 33.05 33.89 29.89

(a) Porcentaje del mes con nubosidad diurna

**Hora** 00 01 02 03 04 05 06 07 08 09 10 11

% 0.0 0.0 0.0 0.0 0.0 0.0 14.73 30.0 48.25 66.23 66.99 67.85

**Hora** 12 13 14 15 16 17 18 19 20 21 22 23

% 66.53 63.09 61.09 53.52 47.36 37.8 19.41 4.3 1.71 0.0 0.0 0.0

(b) Porcentaje de la hora con nubosidad. Los ceros corresponden a horas donde no hay datos de nubosidad.

%

%

30

25

Ene Feb Mar Abr May Jun Jul Ago Sep Oct Nov Dic

60

40

20

0

00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23

Figura 12: A) Ciclo anual de frecuencia de nubosidad diurna, B) Ciclo diario de frecuencia de nubosidad.

15

%

Reporte de
Generaci ́on Fotovoltaica

Tabla 12: Variaci ́on interanual del porcentaje de nubosidad.

**A ̃no** 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016

% 29.13 28.62 29.56 28.55 25.77 27.57 24.06 23.73 26.97 24.68 29.15 27.11 26.55

30

25

2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016

Figura 13: Variaci ́on interanual del porcentaje de nubes.

16

Reporte de
Generaci ́on Fotovoltaica

23

22

21

20

19

18

17

16

15

14

13

12

11

10

09

08

07

06

05

04

03

02

01

00

|0|0|0|0|0|0|0|0|0|0|0|0|
|---|---|---|---|---|---|---|---|---|---|---|---|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|11|0|0|0|0|0|0|0|0|0|0|9|
|21|4|3|0|0|0|0|0|0|0|0|22|
|26|32|21|9|0|0|0|15|14|35|41|40|
|37|34|40|39|18|17|18|39|51|58|55|48|
|36|36|39|48|50|45|56|54|49|57|51|46|
|39|40|46|54|56|53|66|59|57|61|59|51|
|40|42|50|62|70|74|79|71|63|65|62|53|
|43|44|51|67|71|76|80|75|64|68|62|54|
|45|47|58|73|77|79|83|77|68|68|65|57|
|48|50|58|73|77|79|77|79|70|72|72|58|
|45|49|61|70|75|80|75|76|68|73|72|58|
|50|55|63|70|72|75|71|71|65|73|70|58|
|47|53|64|68|39|0|0|48|62|72|69|56|
|50|50|36|0|0|0|0|0|33|68|69|56|
|39|0|0|0|0|0|0|0|0|21|65|52|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|

Ene Feb Mar Abr May Jun Jul Ago Sep Oct Nov Dic

Figura 14: Porcentaje de tiempo con nubes para cada hora y mes.

17

80

75

70

65

60

55

50

45

40

35

30

25

20

15

10

5

0

%

Reporte de
Generaci ́on Fotovoltaica

**3.5** **Temperatura**

La temperatura ambiental afecta la eficiencia de las celdas fotovoltaicas. Las estimaciones de temperatura que se muestran en este cap ́ıtulo est ́an basadas en los resultados del Explorador E ́olico, los
cuales se basan en las simulaciones hechas con el modelo meteorol ́ogico WRF a 1[km] de resoluci ́on
para el a ̃no 2010.

Tabla 13: Temperatura media.

**Mes** Ene Feb Mar Abr May Jun Jul Ago Sep Oct Nov Dic

o C 16.07 16.09 14.01 11.24 9.27 7.72 7.52 8.03 8.73 10.27 12.1 14.28

(a) Temperatura promedio mensual.

**Hora** 00 01 02 03 04 05 06 07 08 09 10 11

o C 9.46 8.98 8.58 8.21 7.89 7.58 7.47 7.69 8.33 9.38 10.71 12.22

**Hora** 12 13 14 15 16 17 18 19 20 21 22 23

o C 13.65 14.87 15.72 16.16 16.08 15.4 14.39 13.26 12.17 11.33 10.63 10.02

(b) Temperatura promedio para cada hora.

o C

o C

15

10

Ene Feb Mar Abr May Jun Jul Ago Sep Oct Nov Dic

15

10

00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23

Figura 15: A) Ciclo diario de la temperatura media, B) Ciclo anual de la temperatura media.

18

23

22

21

20

19

18

17

16

15

14

13

12

11

10

09

08

07

06

05

04

03

02

01

00

|14|15|13|10|9|7|7|7|8|9|10|12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|15|16|13|11|9|8|7|8|8|9|11|13|
|16|17|14|11|9|8|8|8|9|10|12|14|
|18|18|15|12|10|8|8|9|10|11|13|16|
|20|20|16|13|10|9|8|9|10|12|14|17|
|21|21|18|14|11|9|9|10|12|14|16|19|
|22|22|20|15|12|9|10|11|13|15|17|19|
|23|23|20|16|13|10|10|11|14|15|18|20|
|23|23|20|16|13|10|10|11|14|15|18|20|
|23|22|19|15|13|10|10|11|13|15|18|20|
|22|21|18|14|12|10|10|10|12|14|17|19|
|20|19|16|13|11|9|9|10|11|13|16|18|
|18|17|15|12|9|8|8|9|10|12|14|16|
|16|15|13|10|8|7|7|8|8|10|13|15|
|14|13|11|9|7|6|6|7|7|9|11|13|
|12|12|10|8|7|6|6|6|6|8|9|11|
|11|11|10|8|7|6|6|6|5|7|8|10|
|10|10|9|8|7|6|6|6|5|6|8|9|
|10|11|10|8|7|6|6|6|5|6|7|9|
|11|11|10|8|7|6|6|6|6|7|8|9|
|11|12|10|9|8|6|6|6|6|7|8|10|
|12|12|11|9|8|7|6|6|6|7|8|10|
|12|13|11|9|8|7|6|6|7|8|9|11|
|13|14|12|10|8|7|7|7|7|8|9|12|

Ene Feb Mar Abr May Jun Jul Ago Sep Oct Nov Dic

Figura 16: Promedio de la temperatura para cada mes y hora.

19

Reporte de
Generaci ́on Fotovoltaica

22

20

18

16

14

12

10

8

6

o C

Reporte de
Generaci ́on Fotovoltaica

**3.6** **Viento**

La velocidad del viento interviene en el enfriamiento de ls celdas fotovoltaicas, y por lo tanto en su
eficiencia, adem ́as puede afectar la integridad del montaje de los paneles. Las estimaciones de viento
aqu ́ı presentadas corresponden a los resultados del Explorador E ́olico para una altura de 5.5 metros,
calculados con el modelo WRF a 1 [km] de resoluci ́on para el a ̃no 2010.

Tabla 14: Velocidad del viento a 5 _,_ 5[ _m_ ].

**Mes** Ene Feb Mar Abr May Jun Jul Ago Sep Oct Nov Dic

_m/s_ 1.98 2.02 1.78 1.79 1.81 2.32 2.4 2.44 1.87 1.84 2.03 2.04

(a) Promedio mensual de la magnitud del viento.

**Hora** 00 01 02 03 04 05 06 07 08 09 10 11

_m/s_ 1.7 1.68 1.65 1.64 1.62 1.59 1.63 1.69 1.73 1.87 2.03 2.18

**Hora** 12 13 14 15 16 17 18 19 20 21 22 23

_m/s_ 2.34 2.5 2.61 2.69 2.67 2.58 2.42 2.21 2.03 1.93 1.86 1.77

(b) Promedio de la magnitud del viento para cada hora.

_m/s_

2

Ene Feb Mar Abr May Jun Jul Ago Sep Oct Nov Dic

2 _._ 5

_m/s_

2

1 _._ 5

|B)|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||||||||||||
||||||||||||||||||||||||
||||||||||||||||||||||||

00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23

Figura 17: A) Ciclo diario de la magnitud del viento, B) Ciclo anual de la magnitud del viento.

20

23

22

21

20

19

18

17

16

15

14

13

12

11

10

09

08

07

06

05

04

03

02

01

00

|2|2|1|2|2|2|2|2|2|2|2|2|
|---|---|---|---|---|---|---|---|---|---|---|---|
|2|2|2|2|2|2|2|2|2|2|2|2|
|2|2|2|2|2|2|2|2|2|2|2|2|
|2|2|2|2|2|2|2|2|2|2|2|2|
|3|2|2|2|2|2|2|3|2|2|2|3|
|3|3|2|2|2|2|2|3|2|2|3|3|
|3|3|2|2|2|2|2|3|2|2|3|3|
|3|3|3|2|2|2|3|3|2|3|3|3|
|3|3|3|2|2|3|3|3|2|3|3|3|
|3|3|2|2|2|3|3|3|2|2|3|3|
|3|3|2|2|2|3|3|3|2|2|3|3|
|2|2|2|2|2|3|3|3|2|2|2|2|
|2|2|2|2|2|2|3|3|2|2|2|2|
|2|2|2|2|2|2|2|2|2|2|2|2|
|2|2|2|2|2|2|2|2|2|2|2|2|
|2|2|1|2|2|2|2|2|2|2|2|2|
|1|1|1|2|2|2|2|2|2|1|2|2|
|1|1|1|2|2|2|2|2|1|1|1|1|
|1|1|1|1|2|2|2|2|2|1|1|1|
|1|1|1|2|2|2|2|2|2|1|1|1|
|1|1|1|2|2|2|2|2|2|1|1|1|
|1|1|1|1|2|2|2|2|2|1|2|1|
|1|1|1|2|2|2|2|2|2|1|1|1|
|1|2|1|2|2|2|2|2|2|1|2|1|

Ene Feb Mar Abr May Jun Jul Ago Sep Oct Nov Dic

Figura 18: Promedio de la magnitud del viento para cada mes y hora.

21

Reporte de
Generaci ́on Fotovoltaica

3

2 _._ 8

2 _._ 6

2 _._ 4

2 _._ 2

2

1 _._ 8

1 _._ 6

1 _._ 4

1 _._ 2

1

_m/s_