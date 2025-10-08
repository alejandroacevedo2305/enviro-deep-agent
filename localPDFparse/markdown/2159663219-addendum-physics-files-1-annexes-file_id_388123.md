---
title: Sin título
author: Desconocido
date: D:20231226133143-03'00'
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

26/12/2023

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

**Latitud** 39.7227 [o] S

**Longitud** 73.0727 [o] O
**Elevaci ́on** 16 _m_

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

% 38.92 45.83 50.08 55.04 60.66 62.5 62.5 56.41 52.22 46.67 41.67 38.48

(a) Porcentaje de tiempo con sombras cada mes en horario diurno.

**Hora** 00 01 02 03 04 05 06 07 08 09 10 11

% 100.0 100.0 100.0 100.0 100.0 100.0 75.91 50.78 23.23 0.0 0.0 0.0

**Hora** 12 13 14 15 16 17 18 19 20 21 22 23

% 0.0 0.0 0.0 0.0 0.0 0.0 29.74 57.74 85.29 100.0 100.0 100.0

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
|2|100|100|100|100|100|100|100|100|100|100|24|
|0|0|49|100|100|100|100|100|100|40|0|0|
|0|0|0|21|100|100|100|33|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|56|100|100|21|0|0|0|0|
|0|0|53|100|100|100|100|100|53|0|0|0|
|32|100|100|100|100|100|100|100|100|80|0|0|
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

**Configuraci ́on** Tracker 2 Ejes
**Montaje** open rack cell glassback
**Inclinaci ́on** 40 [o]

**Azimut** 0 [o]

**Coef. Temperatura** -0.45 % _/_ [o] _C_
**Ef. Inversor** 96.0 %

**P ́erdidas** 14 %

**Panel seleccionado** **Bifacial**

**Estacionalidad** Sin Estaciones

**Albedo** 0.24

**3.2** **Resultados de la generaci ́on el ́ectrica fotovoltaica**

Tabla 4: Resultados de la generaci ́on fotovoltaica

**Capacidad Instalada** 12.16 _kW_
**Total Diario** 69.0 _kWh_

**Total Anual** 25.02 _MWh_

**Factor de Planta** 23.0 %

Tabla 5: Ciclo anual de la generaci ́on fotovoltaica.

**Mes** Ene Feb Mar Abr May Jun Jul Ago Sep Oct Nov Dic

_MWh_ 3.76 2.96 2.42 1.51 1.01 0.84 0.83 1.17 1.9 2.29 2.87 3.48

(a) Promedio de la generaci ́on total en cada mes.

6

Reporte de
Generaci ́on Fotovoltaica

Tabla 6: Ciclo diario de la generaci ́on fotovoltaica.

**Hora** 00 01 02 03 04 05 06 07 08 09 10 11

_kWh_ 0.0 0.0 0.0 0.0 0.0 0.0 0.68 1.99 3.28 4.37 5.02 5.69

**Hora** 12 13 14 15 16 17 18 19 20 21 22 23

_kWh_ 6.17 6.57 6.67 6.97 6.78 6.49 4.59 2.8 0.48 0.0 0.0 0.0

(a) Promedio de la generaci ́on para cada hora.

4

3

_MWh_

2

1

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|A)|A)|A)|A)|A)|A)|A)|A)|A)|A)|A)|
||||||||||||
||||||||||||
||||||||||||

Ene Feb Mar Abr May Jun Jul Ago Sep Oct Nov Dic

_kWh_

6

4

2

0
00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23

Figura 4: A) Ciclo anual de generaci ́on, B) Ciclo diario de generaci ́on

Tabla 7: Total anual de la generaci ́on para cada a ̃no en la base de datos.

**A ̃no** 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016

_MWh_ 22.67 23.89 22.38 24.47 25.59 24.54 27.87 28.06 24.88 27.14 23.48 25.47 24.87

7

_MWh_

Reporte de
Generaci ́on Fotovoltaica

30

25

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

**Directa** 5.82 4.78 2.99 1.44 0.75 0.56 0.53 0.92 2.03 2.59 3.71 5.0

**Difusa** 1.92 1.67 1.48 1.09 0.66 0.5 0.6 0.87 1.38 2.0 2.44 2.42

**Global** 7.74 6.45 4.47 2.53 1.41 1.06 1.13 1.79 3.41 4.59 6.15 7.42

(a) Radiaci ́on incidente en el plano horizontal

**Mes** Ene Feb Mar Abr May Jun Jul Ago Sep Oct Nov Dic

**Directa** 5.01 4.78 3.76 2.34 1.56 1.35 1.19 1.64 2.77 2.8 3.28 4.09

**Difusa** 1.69 1.48 1.31 0.96 0.58 0.44 0.53 0.77 1.22 1.76 2.15 2.14

**Suelo** 0.22 0.18 0.13 0.07 0.04 0.03 0.03 0.05 0.1 0.13 0.17 0.21

**Global** 6.92 6.44 5.2 3.37 2.18 1.82 1.75 2.46 4.09 4.69 5.6 6.44

(b) Radiaci ́on incidente en un plano con inclinaci ́on igual a la latitud del sitio.

Difusa horizontal Directa horizontal

Reflejada del suelo en panel Difusa en panel Directa en panel

**10**

**5**

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

**Directa** 0.0 0.0 0.0 0.0 0.0 0.0 4.47 32.22 80.66 140.27 196.31 246.48

**Difusa** 0.0 0.0 0.0 0.0 0.0 0.0 3.62 18.29 47.6 91.25 134.91 178.15

**Global** 0.0 0.0 0.0 0.0 0.0 0.0 8.09 50.51 128.26 231.52 331.22 424.63

**Hora** 12 13 14 15 16 17 18 19 20 21 22 23

**Directa** 285.89 324.2 335.0 328.52 279.07 187.14 102.69 37.97 1.67 0.0 0.0 0.0

**Difusa** 206.9 201.6 177.15 142.53 100.38 68.6 31.94 12.2 1.61 0.0 0.0 0.0

**Global** 492.79 525.8 512.15 471.05 379.45 255.74 134.63 50.17 3.28 0.0 0.0 0.0

(a) Radiaci ́on incidente en el plano horizontal.

**Hora** 00 01 02 03 04 05 06 07 08 09 10 11

**Directa** 0.0 0.0 0.0 0.0 0.0 0.0 0.0 6.08 64.77 147.06 218.26 283.41

**Difusa** 0.0 0.0 0.0 0.0 0.0 0.0 3.19 16.15 42.03 80.58 119.13 157.31

**Suelo** 0.0 0.0 0.0 0.0 0.0 0.0 0.23 1.42 3.6 6.5 9.3 11.92

**Global** 0.0 0.0 0.0 0.0 0.0 0.0 3.42 23.65 110.4 234.14 346.69 452.64

**Hora** 12 13 14 15 16 17 18 19 20 21 22 23

**Directa** 332.88 383.3 397.85 397.51 332.22 226.0 79.83 1.81 0.0 0.0 0.0 0.0

**Difusa** 182.7 178.02 156.43 125.86 88.64 60.57 28.2 10.77 1.42 0.0 0.0 0.0

**Suelo** 13.83 14.76 14.38 13.22 10.65 7.18 3.78 1.41 0.09 0.0 0.0 0.0

**Global** 529.41 576.08 568.66 536.59 431.51 293.75 111.81 13.99 1.51 0.0 0.0 0.0

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

**Directa** 2.21 2.44 2.13 2.51 2.85 2.44 2.81 2.99 2.53 2.96 2.39 2.67 2.63

**Difusa** 1.59 1.45 1.58 1.45 1.3 1.42 1.36 1.29 1.44 1.27 1.46 1.39 1.41

**Global** 3.8 3.89 3.71 3.96 4.15 3.86 4.17 4.28 3.97 4.23 3.85 4.06 4.04

(a) Radiaci ́on incidente en el plano horizontal.

**A ̃no** 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016

**Directa** 2.42 2.64 2.33 2.66 3.01 2.77 3.41 3.46 2.84 3.31 2.58 2.92 2.96

**Difusa** 1.4 1.28 1.39 1.28 1.15 1.26 1.2 1.14 1.27 1.12 1.29 1.23 1.25

**Suelo** 0.11 0.11 0.1 0.11 0.12 0.11 0.12 0.12 0.11 0.12 0.11 0.11 0.11

**Global** 3.93 4.03 3.82 4.05 4.28 4.14 4.73 4.72 4.22 4.55 3.98 4.26 4.32

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
|23|0|0|0|0|0|0|0|0|0|0|16|
|178|128|18|0|0|0|0|0|0|18|105|159|
|365|283|158|36|0|0|0|16|89|146|222|309|
|541|459|303|155|78|46|78|125|195|263|365|472|
|722|630|456|272|150|121|127|205|318|405|525|640|
|849|736|558|343|216|185|176|271|410|514|645|767|
|914|786|617|389|229|167|174|267|455|574|728|864|
|918|817|624|391|231|171|179|267|486|607|756|884|
|881|771|569|338|194|150|160|241|464|587|731|848|
|777|664|491|272|156|115|125|183|399|511|654|767|
|642|528|350|188|100|70|77|124|302|421|537|650|
|474|376|225|116|52|30|32|72|198|299|425|491|
|305|212|100|33|4|0|0|19|88|172|279|333|
|141|63|6|0|0|0|0|0|8|68|143|178|
|15|0|0|0|0|0|0|0|0|2|32|48|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|

Ene Feb Mar Abr May Jun Jul Ago Sep Oct Nov Dic

Figura 9: Promedio de la radiaci ́on global horizontal para cada hora y mes.

12

900

800

700

600

500

400

300

200

100

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
|10|0|0|0|0|0|0|0|0|0|0|7|
|46|44|9|0|0|0|0|0|0|7|25|39|
|247|235|184|76|0|0|0|44|123|119|136|186|
|458|445|357|258|209|165|223|231|247|257|304|377|
|669|650|546|401|269|250|228|309|397|423|484|566|
|821|778|668|472|345|330|274|385|500|545|623|714|
|901|836|731|509|332|255|241|346|543|608|715|824|
|908|870|724|493|318|251|233|331|570|642|744|850|
|864|813|649|399|254|213|210|288|535|622|716|809|
|744|689|564|324|215|173|171|220|462|529|636|721|
|591|531|397|236|145|113|114|158|358|430|510|591|
|401|353|254|155|87|66|58|106|239|297|386|417|
|210|168|109|52|11|0|0|41|109|162|228|242|
|42|22|3|0|0|0|0|0|8|49|83|76|
|7|0|0|0|0|0|0|0|0|1|14|19|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|

Ene Feb Mar Abr May Jun Jul Ago Sep Oct Nov Dic

900

800

700

600

500

400

300

200

100

0

_W/m_ [2]

Figura 10: Promedio de la radiaci ́on global incidente en un plano con inclinacio ́on igual a la latitud del sitio,
para cada hora y mes.

13

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
|264|0|0|0|0|0|0|0|0|0|0|186|
|603|616|165|0|0|0|0|0|0|192|586|571|
|722|637|556|277|0|0|0|159|490|468|500|591|
|739|684|557|466|428|340|433|409|413|416|497|596|
|813|750|616|489|341|328|273|353|450|471|540|656|
|784|713|605|436|337|340|247|349|434|453|529|640|
|760|671|574|388|262|203|168|242|393|407|502|644|
|725|670|508|333|222|184|140|199|372|391|460|613|
|695|632|447|227|162|150|130|160|335|381|427|553|
|634|596|446|207|161|140|124|136|321|315|419|548|
|625|559|374|202|131|113|105|130|316|299|395|527|
|570|530|338|194|115|102|82|139|295|268|384|505|
|537|477|270|122|31|0|0|117|231|237|347|471|
|444|316|54|0|0|0|0|0|56|206|312|416|
|139|0|0|0|0|0|0|0|0|17|193|268|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|

Ene Feb Mar Abr May Jun Jul Ago Sep Oct Nov Dic

Figura 11: Promedio de la radiaci ́on directa normal para cada hora y mes.

14

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

**3.4** **Nubosidad**

La nubosidad es la componente atmosf ́erica que remueve mayor cantidad de radiaci ́on incidente. A
partir de im ́agenes del sat ́elite geostacionado GOES, se ha calculado la frecuencia de nubosidad para
cada hora y mes. Debido a que para la mayor parte del pa ́ıs se utilizan las im ́agenes del canal visible
en la detecci ́on de nubosidad, el dato solo est ́a disponible para las horas diurnas.

Tabla 11: Frecuencia de la nubosidad diurna.

**Mes** Ene Feb Mar Abr May Jun Jul Ago Sep Oct Nov Dic

% 19.69 19.07 24.17 27.78 28.29 26.44 28.14 30.9 28.28 32.09 30.69 26.1

(a) Porcentaje del mes con nubosidad diurna

**Hora** 00 01 02 03 04 05 06 07 08 09 10 11

% 0.0 0.0 0.0 0.0 0.0 0.0 14.08 28.94 50.1 68.23 68.82 67.88

**Hora** 12 13 14 15 16 17 18 19 20 21 22 23

% 66.63 62.4 58.56 51.29 46.48 36.26 18.87 4.34 1.41 0.0 0.0 0.0

(b) Porcentaje de la hora con nubosidad. Los ceros corresponden a horas donde no hay datos de nubosidad.

35

%

%

30

25

20

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

% 30.22 28.29 30.59 27.81 25.73 27.3 23.66 22.86 27.21 23.69 28.7 26.47 26.44

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
|8|0|0|0|0|0|0|0|0|0|0|8|
|21|4|5|0|0|0|0|0|0|0|0|22|
|21|27|22|11|0|0|0|19|15|36|41|35|
|26|29|38|38|23|24|22|42|51|54|48|40|
|22|26|36|45|57|56|66|60|52|52|47|37|
|27|32|40|54|62|60|72|63|56|56|50|41|
|31|38|45|61|72|78|82|75|62|62|54|42|
|34|38|52|67|77|80|86|80|64|64|59|46|
|37|41|57|78|83|84|87|84|68|65|62|52|
|42|43|56|79|83|85|87|86|68|71|62|50|
|40|45|62|79|85|86|88|86|68|71|63|51|
|43|45|63|77|84|83|87|82|67|73|63|51|
|42|44|64|78|52|0|0|64|69|74|64|51|
|42|45|40|0|0|0|0|0|39|70|62|50|
|36|0|0|0|0|0|0|0|0|23|60|50|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|
|0|0|0|0|0|0|0|0|0|0|0|0|

Ene Feb Mar Abr May Jun Jul Ago Sep Oct Nov Dic

Figura 14: Porcentaje de tiempo con nubes para cada hora y mes.

17

85

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

o C 16.57 16.56 14.46 11.68 9.59 8.2 7.62 8.23 9.27 10.85 12.74 14.79

(a) Temperatura promedio mensual.

**Hora** 00 01 02 03 04 05 06 07 08 09 10 11

o C 9.9 9.41 9.0 8.64 8.34 8.09 7.93 8.05 8.55 9.52 10.9 12.46

**Hora** 12 13 14 15 16 17 18 19 20 21 22 23

o C 13.95 15.23 16.21 16.71 16.69 15.98 14.97 13.81 12.73 11.86 11.14 10.49

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

|15|15|13|11|9|8|7|7|8|9|11|13|
|---|---|---|---|---|---|---|---|---|---|---|---|
|16|16|14|11|9|8|7|8|9|10|12|14|
|17|18|15|12|10|8|8|8|9|11|13|15|
|19|19|16|13|10|9|8|9|10|12|14|16|
|20|20|17|14|11|9|8|9|11|13|15|18|
|22|22|19|15|11|9|9|10|13|14|17|19|
|23|23|20|16|12|10|10|11|14|15|18|20|
|24|24|21|17|13|11|11|12|14|16|18|21|
|24|23|21|17|13|11|11|12|14|16|19|21|
|23|23|20|16|13|11|10|11|14|16|18|21|
|22|21|18|15|12|10|10|11|13|15|17|20|
|20|20|17|13|11|9|9|10|11|14|16|18|
|18|18|15|12|9|8|8|8|10|12|15|17|
|16|15|13|10|8|7|7|7|8|11|13|15|
|14|13|11|9|8|7|6|7|7|9|11|13|
|12|11|10|8|7|7|6|6|6|8|10|11|
|11|10|10|8|8|7|6|6|5|7|9|10|
|10|10|10|9|8|7|6|6|6|7|8|9|
|10|11|10|9|8|7|6|6|6|7|8|9|
|11|11|11|9|8|7|6|6|6|7|8|10|
|12|12|11|9|8|7|6|6|6|7|8|10|
|12|13|11|9|8|7|6|7|7|8|9|11|
|13|14|12|10|8|7|7|7|7|8|9|11|
|14|14|13|10|9|7|7|7|7|8|10|12|

Ene Feb Mar Abr May Jun Jul Ago Sep Oct Nov Dic

Figura 16: Promedio de la temperatura para cada mes y hora.

19

Reporte de
Generaci ́on Fotovoltaica

24

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

_m/s_ 1.58 1.51 1.17 1.23 1.49 2.04 2.12 2.13 1.55 1.54 1.66 1.75

(a) Promedio mensual de la magnitud del viento.

**Hora** 00 01 02 03 04 05 06 07 08 09 10 11

_m/s_ 1.29 1.26 1.25 1.21 1.2 1.18 1.18 1.2 1.27 1.38 1.51 1.69

**Hora** 12 13 14 15 16 17 18 19 20 21 22 23

_m/s_ 1.91 2.12 2.29 2.47 2.53 2.44 2.22 1.95 1.75 1.53 1.42 1.34

(b) Promedio de la magnitud del viento para cada hora.

_m/s_

_m/s_

2

1 _._ 5

Ene Feb Mar Abr May Jun Jul Ago Sep Oct Nov Dic

2

1 _._ 5

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

|1|1|1|1|1|2|2|2|1|1|1|1|
|---|---|---|---|---|---|---|---|---|---|---|---|
|1|1|1|1|1|2|2|2|1|1|1|1|
|2|2|1|1|1|2|2|2|1|1|1|2|
|2|2|1|1|2|2|2|2|2|2|2|2|
|2|2|1|1|2|2|2|2|2|2|2|3|
|3|2|2|2|2|2|2|2|2|2|3|3|
|3|3|2|2|2|2|2|2|2|3|3|3|
|3|3|2|2|2|2|2|2|2|3|3|3|
|3|3|2|2|2|2|2|3|2|2|3|3|
|3|2|2|2|2|2|2|3|2|2|3|3|
|2|2|2|2|2|2|2|2|2|2|2|3|
|2|2|1|1|2|2|2|2|2|2|2|2|
|2|2|1|1|2|2|2|2|2|2|2|2|
|1|1|1|1|1|2|2|2|2|1|1|1|
|1|1|1|1|1|2|2|2|1|1|1|1|
|1|1|1|1|1|2|2|2|1|1|1|1|
|1|1|1|1|1|2|2|2|1|1|1|1|
|1|1|1|1|1|2|2|2|1|1|1|1|
|1|1|1|1|1|2|2|2|1|1|1|1|
|1|1|1|1|1|2|2|2|1|1|1|1|
|1|1|1|1|1|2|2|2|1|1|1|1|
|1|1|1|1|1|2|2|2|1|1|1|1|
|1|1|1|1|1|2|2|2|1|1|1|1|
|1|1|1|1|1|2|2|2|1|1|1|1|

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