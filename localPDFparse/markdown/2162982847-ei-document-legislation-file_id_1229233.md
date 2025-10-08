---
title: PROYECTO PARQUE FOTOVOLTAICO SOLAR ORIENTE
author: enieto
date: D:20240807105931-04'00'
language: es
type: manual
pages: 41
has_toc: False
has_tables: False
extraction_quality: high
keywords: [Región de Antofagasta, Chile]
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Estudio Hidroló ico g
-->

## PROYECTO PARQUE FOTOVOLTAICO SOLAR ORIENTE

#### APÉNDICE 02 ESTUDIO HIDROLÓGICO _OBRAS HIDRÁULICAS - PAS_ _155_

Junio 2024

PROYECTO PARQUE FOTOVOLTAICO SOLAR ORIENTE Apéndice-02-Hidrología
OBRAS HIDRÁULICAS - PAS 155 Página 1 de 41

### Hoja de control de calidad

Documento OBRAS HIDRÁULICAS - PAS 155

**Proyecto** **PROYECTO PARQUE FOTOVOLTAICO SOLAR ORIENTE**

Código SP1150-ORIENTE-PAS-AN-02-SP-HIDROLOGIA

Autores: Firma: CRM CRM DMJ

Fecha: 22/04/2024 17/05/2024 27/06/2024

Verificado Firma: CNU CNU ENP

Fecha: 22/04/2024 17/05/2024 27/06/2024

Destinatario Solar Oriente SpA

Notas

Apéndice-02-Hidrología PROYECTO PARQUE FOTOVOLTAICO SOLAR ORIENTE
Página 2 de 41 OBRAS HIDRÁULICAS - PAS 155

### Índice

Estudio Hidrológico ............................................................................................................................................................................................. 6

1. Introducción ...................................................................................................................................................................................................... 6

2. Antecedentes.................................................................................................................................................................................................... 7

2.1. Clima ....................................................................................................................................................................................................... 7

3. Estudio Hidrológico....................................................................................................................................................................................... 9

3.1. Análisis de caudales medios ..................................................................................................................................................... 9

3.2. Precipitación máxima diaria ................................................................................................................................................... 10

3.3. Análisis de datos dudosos ....................................................................................................................................................... 11

3.4. Método de Weibull ....................................................................................................................................................................... 13

3.5. Análisis de frecuencia ................................................................................................................................................................. 14

3.6. Prueba de bondad del ajuste ................................................................................................................................................. 19

3.1. Precipitación de Diseño............................................................................................................................................................. 21

3.1. Intensidad de diseño ................................................................................................................................................................... 22

3.2. Cálculo de caudales de crecida ........................................................................................................................................... 26

4. Conclusiones y recomendaciones .................................................................................................................................................... 40

PROYECTO PARQUE FOTOVOLTAICO SOLAR ORIENTE Apéndice-02-Hidrología
OBRAS HIDRÁULICAS - PAS 155 Página 3 de 41

### Índice de Tablas

Tabla No 1. Estación Guatacondo DGA .................................................................................................................................................... 8

Tabla No 2. Precipitaciones máximas diarias, estación Guatacondo DGA. ....................................................................... 11

Tabla No 3. Resultado de análisis de datos dudosos. ................................................................................................................... 12

Tabla No 4. Verificación de datos dudosos. ........................................................................................................................................ 13

Tabla No 5. Resultados Método Weibull................................................................................................................................................ 14

Tabla No 6. Método de Gumbel, valores de Yn y Sn. ...................................................................................................................... 16

Tabla No 7. Resultados análisis de frecuencia. ................................................................................................................................. 18

Tabla No 8. Valores críticos de “d” para prueba Kolmogorov-Smirnov. ............................................................................... 20

Tabla No 9. Resultados prueba de bondad del ajuste. .................................................................................................................. 21

Tabla No 10. Precipitaciones máximas diarias de diseño para los distintos períodos de retorno (T). ............... 21

Tabla No 11. Coeficientes de duración para 10 años de período de retorno. .................................................................. 23

Tabla No 12. Coeficientes de frecuencia para distintos períodos de retorno. Fuente: MC. Vol. III. ....................... 24

Tabla No 13. Intensidades de Diseño Guatacondo DGA.............................................................................................................. 24

Tabla No 14. Intensidades de Diseño Solar Oriente. ...................................................................................................................... 25

Tabla No 15. Datos cuencas aportantes. .............................................................................................................................................. 27

Tabla No 16. Tiempo de concentración. ................................................................................................................................................ 29

Tabla No 17. Factores coeficiente de escorrentía. ........................................................................................................................... 30

Tabla No 18. Coeficiente de Escorrentía, MC. Vol. III. ..................................................................................................................... 31

Tabla No 19. Coeficientes de escorrentía de diseño. ..................................................................................................................... 31

Tabla No 20. Coeficientes de duración para 10 años de periodo de retorno. .................................................................. 32

Tabla No 21. Clasificación de condiciones antecedentes de humedad del suelo. ....................................................... 33

Tabla No 22. Valores sugeridos por S.C.S. para distintos tipos de suelo en condiciones de humedad

antecedente AMC II. ......................................................................................................................................................................................... 34

Tabla No 23. Precipitación efectiva para estación Guatacondo DGA y sector Solar Oriente. ................................. 35

Tabla No 24. Intensidades de diseño. ..................................................................................................................................................... 37

Tabla No 25. Caudales líquidos con el método HUS. .................................................................................................................... 37

Tabla No 26. Caudales líquidos con el método Racional. ........................................................................................................... 38

Tabla No 27. Caudales detríticos de cuencas. ................................................................................................................................... 40

Tabla No 28. Periodos de retorno para diseños de drenaje. ...................................................................................................... 40

Apéndice-02-Hidrología PROYECTO PARQUE FOTOVOLTAICO SOLAR ORIENTE
Página 4 de 41 OBRAS HIDRÁULICAS - PAS 155

### Índice de Figuras

Figura No 1. Emplazamiento del Proyecto Parque Fotovoltaico Solar Oriente. .................................................................. 6

Figura No 2. Distribución de tipos de clima en la región de Tarapacá. .................................................................................. 7

Figura No 3. Emplazamiento estación pluviométrica Guatacondo DGA. ............................................................................... 8

Figura No 4. Sector de emplazamiento de camino hacia Proyecto. ......................................................................................... 9

Figura No 5. Resultados obtenidos del análisis de frecuencia. ................................................................................................ 18

Figura No 6. Isoyetas en zona de estudio. ............................................................................................................................................ 22

Figura No 7. Curvas IDF duraciones entre 1 y 24 horas, Guatacondo DGA. ...................................................................... 25

Figura No 8. Curvas IDF duraciones entre 1 y 24 horas, Solar Oriente. ................................................................................ 26

Figura No 9. Cuencas aportantes y quebradas. ................................................................................................................................ 27

Figura No 10. Fotografía del ámbito del Proyecto. ........................................................................................................................... 29

Figura No 11. Modelo de Solar Oriente en HEC-HMS. .................................................................................................................. 35

PROYECTO PARQUE FOTOVOLTAICO SOLAR ORIENTE Apéndice-02-Hidrología
OBRAS HIDRÁULICAS - PAS 155 Página 5 de 41

# Estudio Hidroló ico g

**1.** **Introducción**

Solar Oriente SpA se encuentra desarrollando el Proyecto Parque Fotovoltaico Solar Oriente ubicado en la

región de Tarapacá, a unos 150 kilómetros al sureste de la ciudad de Iquique.

El Proyecto se emplaza en las coordenadas 449.542,76m. este y 7.688.851,38 m. sur, a una altura de 971

msnm.

Figura No 1. Emplazamiento del Proyecto Parque Fotovoltaico Solar Oriente.

Fuente: Elaboración Propia.

El presente estudio tiene por objetivo:

1. Caracterizar el clima y condiciones geomorfológicas de la zona de emplazamiento del Proyecto.

2. Caracterizar hidrológicamente la cuenca de emplazamiento del Proyecto.

3. Estimar los caudales afluentes al Proyecto, para eventos de extremos asociados a diferentes

periodos de retorno.

4. Proponer medidas de saneamiento de las aguas lluvias afluentes al Proyecto.

Apéndice-02-Hidrología PROYECTO PARQUE FOTOVOLTAICO SOLAR ORIENTE
Página 6 de 41 OBRAS HIDRÁULICAS - PAS 155

**2.** **Antecedentes**

**2.1.** **Clima**

El clima presente en la Región de Tarapacá es característicamente árido. El desierto se manifiesta de forma

plena hacia la zona intermedia. Donde la influencia marítima pierde importancia. El paisaje carece de

vegetación y presenta una extrema aridez conformando el Desierto de Atacama.

Se presentan cuatro subtipos climáticos desérticos que, desde el poniente al oriente, son los siguientes:

 - Clima desértico costero nuboso.

 - Desértico interior (pampa).

 - Desértico marginal de altura.

 - Tundra por efecto de altura.

Figura No 2. Distribución de tipos de clima en la región de Tarapacá.

Fuente: Cartografía interactiva de los Climas de Chile.

El Proyecto se emplaza en torno a los 1.000 msnm con clima desértico normal (BWk), el cual se localiza en

la pampa, sin influencia oceánica costera. Este subtipo se caracteriza por ser de extrema aridez, donde las

precipitaciones anuales son de 0 mm, y las temperaturas medias alcanzan a 18° C. Característicos de este

clima son los días con cielos despejados y mucha luminosidad, y más seco que el clima del desértico

costero, la humedad relativa en promedio es de 50%.

PROYECTO PARQUE FOTOVOLTAICO SOLAR ORIENTE Apéndice-02-Hidrología
OBRAS HIDRÁULICAS - PAS 155 Página 7 de 41

Entre los 2.000 y 3.000 metros sobre el nivel del mar se presenta mayor volumen de precipitaciones. Esta

zona se ve caracterizada por una masa de aire inestable que por efectos de la altura produce nubosidad de

desarrollo vertical que da origen a precipitaciones durante casi todos los veranos. Si bien no son tan

abundantes como para eliminar la característica desértica, crean condiciones para la existencia de una

incipiente vegetación estacional. Las temperaturas muestran un régimen relativamente frío, con un

promedio no superior a los 10o C (CIREN, 1979).

En la zona de estudio se encuentra la estación pluviométrica Guatacondo DGA, ubicada a 46 kilómetros del

emplazamiento del Proyecto, pero en diferente zona climática que éste, por lo que se utilizarán las isoyetas

extraídas del producto “Precipitaciones máximas diarias” del portal Infraestructura de Datos Geoespaciales

(IDE Chile), donde se muestra la precipitación máxima diaria para T=10 años, para trasponer la precipitación

máxima en el parque Solar Oriente.

La estación pertenece a la DGA (Dirección General de Aguas) y permaneció activa desde 1977 hasta 2022,

con un registro de 47 años. A continuación, se muestra su ubicación respecto al Proyecto:

Figura No 3. Emplazamiento estación pluviométrica Guatacondo DGA.

Fuente: Elaboración Propia.

Tabla No 1. Estación Guatacondo DGA

Fuente: Elaboración Propia.

Apéndice-02-Hidrología PROYECTO PARQUE FOTOVOLTAICO SOLAR ORIENTE
Página 8 de 41 OBRAS HIDRÁULICAS - PAS 155

**3.** **Estudio Hidrológico**

**3.1.** **Análisis de caudales medios**

En este sector se encuentran quebradas de tipo intermitente que se activan en el periodo de lluvias

altiplánicas. Dentro de la cuenca aportante a la zona de estudio no se encuentra registro fluviométrico, por

lo que los caudales medios no son analizados, siendo inexistentes en la mayoría de años de análisis.

Las quebradas identificadas se encuentran intervenidas por caminos en gran parte de su extensión. Esto se

puede evidenciar con el corte de la quebrada en Figura No 4.

Figura No 4. Sector de emplazamiento de camino hacia Proyecto.

Fuente: Elaboración Propia.

Se puede visualizar el sector de intervención por camino proyectado en el plano de planta general adjunto

en el **Apéndice 06 Planos** “SP1150-ORIENTE-PAS155-DR-02-SP-PLANTA_GENERAL”.

PROYECTO PARQUE FOTOVOLTAICO SOLAR ORIENTE Apéndice-02-Hidrología
OBRAS HIDRÁULICAS - PAS 155 Página 9 de 41

**3.2.** **Precipitación máxima diaria**

Para comenzar con el estudio hidrológico, se tomaron 47 años de datos de estadísticas de la estación

Guatacondo DGA, muestra que se considera representativa a efectos de este análisis. A pesar de estar activa

la estación, la estación no posee datos de precipitaciones más allá de 2022, por lo que finalmente se ha

acotado la muestra desde 1977 a 2022 (ambos incluidos).

**1977** 01/09 0,00 **2000** 22/01 10,00

**1978** 13/01 3,40 **2001** 27/02 6,00

**1979** 15/01 4,00 **2002** 01/07 16,00

**1980** 19/03 1,80 **2003** 18/03 2,50

**1981** 09/02 3,00 **2004** 11/02 12,70

**1982** 17/06 1,00 **2005** 11/01 36,00

**1983** 10/06 12,00 **2006** 15/01 6,00

**1984** 10/01 12,50 **2007** 13/01 1,50

**1985** 06/03 9,00 **2008** 14/01 6,00

**1986** 01/02 3,00 **2009** 15/01 2,50

**1987** 09/03 10,00 **2010** 18/01 8,00

**1988** 11/03 2,00 **2011** 05/02 10,00

**1989** 04/02 3,00 **2012** 25/01 10,00

**1990** 17/02 3,00 **2013** 08/02 3,00

**1991** 04/01 3,00 **2014** 01/01 0,00

**1992** 02/06 6,00 **2015** 25/03 12,00

**1993** 09/08 12,00 **2016** 01/01 0,00

**1994** 06/03 2,00 **2017** 28/02 15,00

**1995** 14/03 22,30 **2018** 02/02 3,40

**1996** 28/08 5,00 **2019** 09/02 3,50

1997 20/01 18,00 **2020** 01/08 0,00

Apéndice-02-Hidrología PROYECTO PARQUE FOTOVOLTAICO SOLAR ORIENTE
Página 10 de 41 OBRAS HIDRÁULICAS - PAS 155

1998 27/01 1,00 **2021** 22/12 22,80

1999 07/03 2,00 **2022** 15/03 5,80

Tabla No 2. Precipitaciones máximas diarias, estación Guatacondo DGA.

Fuente: Estación Guatacondo DGA, Dirección General de Aguas (MOP).

Debido a que algunos datos mostraban valores iguales a cero, se comprobó si dicha estación estuvo activa

durante el periodo de tiempo indicado y se comprobó la poca existencia de datos, concluyendo que

efectivamente se tiene registro de dichos años, pero no existió precipitación alguna en esos períodos. Se

eliminan de la estadística.

**3.3.** **Análisis de datos dudosos**

Se realiza el análisis de datos dudosos cuando se tienen datos que se alejan significativamente de la

información y que afectan de una manera considerable la magnitud de los parámetros estadísticos de la

serie. Para determinar el rango de comprobación se calculan umbrales máximos y mínimos de la serie de

datos de caudales máximos de las estaciones analizadas. De acuerdo con el Water Resources Council

(1981), si la asimetría de la estación es mayor que +0,4, se consideran primero las pruebas para detectar

datos dudosos altos; si la asimetría de la estación es menor a -0,4, primero se consideran pruebas para

detectar datos dudosos bajos. Cuando la asimetría de la estación está entre ±0,4, deben aplicarse pruebas

para detectar datos dudosos altos y bajos antes de eliminar cualquier dato dudoso del conjunto de datos.

La siguiente ecuación de frecuencia puede utilizarse para detectar datos dudosos altos (Ven Te Chow, 1994):

y H = ~~y~~ + K n s y

y L = ~~y~~ −K n s y

Donde, y H es el umbral de datos dudosos máximo en unidades logarítmicas e y L es el umbral de datos

dudosos mínimo en unidades logarítmicas definidos por ~~y~~ es la media de la muestra, K n factor para la prueba

de datos dudosos y s y la desviación estándar.

Luego, se define el valor máximo y mínimo de la muestra con la expresión siguiente:

Q H = 10 [y] [H]

Q L = 10 [y] [L]

Donde, Q H es el umbral de datos dudosos máximo en m [3] /s y Q L es el umbral de datos dudosos mínimo en

m [3] /s.

A continuación, se muestra el resultado de análisis de datos dudosos:

PROYECTO PARQUE FOTOVOLTAICO SOLAR ORIENTE Apéndice-02-Hidrología
OBRAS HIDRÁULICAS - PAS 155 Página 11 de 41

**TABLA RESUMEN**

Tabla No 3. Resultado de análisis de datos dudosos.

Fuente: Elaboración Propia.

A continuación, se muestran los resultados de la aplicación del método a los datos de la estación

Guatacondo DGA. Se observa que toda la estadística de la estación se encuentra dentro de los rangos

determinados a través del análisis, por lo que no es necesario excluir información del registro.

**1977** - - - - **2000** 22/01 10,00 1,00 NO

**1978** 13/01 3,40 0,53 NO **2001** 27/02 6,00 0,78 NO

**1979** 15/01 4,00 0,60 NO **2002** 01/07 16,00 1,20 NO

**1980** 19/03 1,80 0,26 NO **2003** 18/03 2,50 0,40 NO

**1981** 09/02 3,00 0,48 NO **2004** 11/02 12,70 1,10 NO

**1982** 17/06 1,00 0,00 NO **2005** 11/01 36,00 1,56 NO

**1983** 10/06 12,00 1,08 NO **2006** 15/01 6,00 0,78 NO

**1984** 10/01 12,50 1,10 NO **2007** 13/01 1,50 0,18 NO

**1985** 06/03 9,00 0,95 NO **2008** 14/01 6,00 0,78 NO

**1986** 01/02 3,00 0,48 NO **2009** 15/01 2,50 0,40 NO

**1987** 09/03 10,00 1,00 NO **2010** 18/01 8,00 0,90 NO

**1988** 11/03 2,00 0,30 NO **2011** 05/02 10,00 1,00 NO

**1989** 04/02 3,00 0,48 NO **2012** 25/01 10,00 1,00 NO

**1990** 17/02 3,00 0,48 NO **2013** 08/02 3,00 0,48 NO

**1991** 04/01 3,00 0,48 NO **2014** 01/01 0,10 -1,00 NO

**1992** 02/06 6,00 0,78 NO **2015** 25/03 12,00 1,08 NO

**1993** 09/08 12,00 1,08 NO **2016** - - -

**1994** 06/03 2,00 0,30 NO **2017** 28/02 15,00 1,18 NO

Apéndice-02-Hidrología PROYECTO PARQUE FOTOVOLTAICO SOLAR ORIENTE
Página 12 de 41 OBRAS HIDRÁULICAS - PAS 155

**1995** 14/03 22,30 1,35 NO **2018** 02/02 3,40 0,53 NO

**1996** 28/08 5,00 0,70 NO **2019** 09/02 3,50 0,54 NO

**1997** 20/01 18,00 1,26 NO **2020** - - -

**1998** 27/01 1,00 0,00 NO **2021** 22/12 22,80 1,36 NO

**1999** 07/03 2,00 0,30 NO **2022** 15/03 5,80 0,76 NO

Tabla No 4. Verificación de datos dudosos.

Fuente: Elaboración Propia.

**3.4.** **Método de Weibull**

Este método consiste en ordenar los valores de caudales de la estación en estudio, de mayor a menor y

designando con la letra “m” el número de orden asignado a cada valor y con la letra “N” el total de datos de

la estadística. Luego, la probabilidad de excedencia P de que este valor sea igualado o superado queda

definida, en porcentaje, por la expresión de Weibull:

P= (N+ 1m ~~[)]~~ [ ∙100]

Se define el periodo de retorno T como el valor inverso a la probabilidad de excedencia, y es igual a:

T= [1]

P

Se ha considerado un horizonte de 43 años, desde el año 1978 al 2022. Los resultados obtenidos de la

aplicación de este método se presentan en la Tabla No 5.

**1** 36,00 0,98 44,00 **23** 5,00 0,48 1,91

**2** 22,80 0,95 22,00 **24** 4,00 0,45 1,83

**3** 22,30 0,93 14,67 **25** 3,50 0,43 1,76

**4** 18,00 0,91 11,00 **26** 3,40 0,41 1,69

**5** 16,00 0,89 8,80 **27** 3,40 0,39 1,63

**6** 15,00 0,86 7,33 **28** 3,00 0,36 1,57

**7** 12,70 0,84 6,29 **29** 3,00 0,34 1,52

PROYECTO PARQUE FOTOVOLTAICO SOLAR ORIENTE Apéndice-02-Hidrología
OBRAS HIDRÁULICAS - PAS 155 Página 13 de 41

**8** 12,50 0,82 5,50 **30** 3,00 0,32 1,47

**9** 12,00 0,80 4,89 **31** 3,00 0,30 1,42

**10** 12,00 0,77 4,40 **32** 3,00 0,27 1,38

**11** 12,00 0,75 4,00 **33** 3,00 0,25 1,33

**12** 10,00 0,73 3,67 **34** 2,50 0,23 1,29

**13** 10,00 0,70 3,38 **35** 2,50 0,20 1,26

**14** 10,00 0,68 3,14 **36** 2,00 0,18 1,22

**15** 10,00 0,66 2,93 **37** 2,00 0,16 1,19

**16** 9,00 0,64 2,75 **38** 2,00 0,14 1,16

**17** 8,00 0,61 2,59 **39** 1,80 0,11 1,13

**18** 6,00 0,59 2,44 **40** 1,50 0,09 1,10

**19** 6,00 0,57 2,32 **41** 1,00 0,07 1,07

**20** 6,00 0,55 2,20 **42** 1,00 0,05 1,05

**21** 6,00 0,52 2,10 **43** 0,10 0,02 1,02

22 5,80 0,50 2,00

Tabla No 5. Resultados Método Weibull.

Fuente: Elaboración Propia.

**3.5.** **Análisis de frecuencia**

El objetivo del análisis de frecuencia de cualquier variable aleatoria es asociar a cada valor una probabilidad

de ocurrencia. Ello se logra representando la variable con un determinado modelo probabilístico y

estimando los parámetros de dicho modelo. Es por esta razón que se utilizan los valores externos anuales,

es decir, las precipitaciones máximas anuales en 24 horas con el objetivo de predecir eventos extremos

futuros y así determinar los valores de la precipitación de diseño.

A continuación, se presenta una breve descripción de la formulación teórica de los modelos utilizados.

**3.5.1.** **Distribución Normal**

La distribución normal tiene la siguiente ecuación:

Apéndice-02-Hidrología PROYECTO PARQUE FOTOVOLTAICO SOLAR ORIENTE
Página 14 de 41 OBRAS HIDRÁULICAS - PAS 155

P(T) = X [̅ ] + z∙S x

Donde:

P(T) : Precipitación para un periodo de retorno T.

X [̅] : Promedio de la serie de precipitaciones máximas.

z : Variable aleatoria estandarizada asociada a la probabilidad de ocurrencia.

S x : Desviación estándar de la serie de precipitaciones máximas.

**3.5.2.** **Distribución Log-Normal**

La distribución Log-Normal tiene la siguiente ecuación:

Ln(P(T)) = X [̅ ] + z∙S x

Donde:

P(T) : Precipitación para un periodo de retorno T.

X [̅] : Promedio de los logaritmos de la serie de precipitaciones máximas.

z : Variable aleatoria estandarizada asociada a la probabilidad de ocurrencia.

S x : Desviación estándar de los logaritmos la serie de precipitaciones máximas.

**3.5.3.** **Distribución Gumbel**

Esta función de distribución acumulada está dada por la siguiente expresión:

F(x) = e [−e−a(x−u)]

Donde:

F(x) : Función de distribución asociada a la variable aleatoria x.

a : Parámetro de dispersión.

u : Moda de la distribución.

Al despejar la variable x de la ecuación anterior, se obtiene la precipitación máxima para un periodo de

retorno T, se tiene entonces:

x(T) = u− [1]

[1]

a [∙ln (−ln(1 −1] T

T [))]

En que,

Donde:

u= x̅ −S x ∙ S [Y] [n] n

a= [S] [n]

S x

x̅ : Promedio de la serie de precipitaciones.

S x : Desviación estándar de la serie de precipitaciones.

Y n : Valor medio de la variable reducida.

S n : Desviación estándar de la variable reducida.

Los valores de los parámetros Y n y S n de la variable reducida dependen del número de años de registros de

la muestra n y se tabulan a continuación en la siguiente tabla:

PROYECTO PARQUE FOTOVOLTAICO SOLAR ORIENTE Apéndice-02-Hidrología
OBRAS HIDRÁULICAS - PAS 155 Página 15 de 41

n Y n S n n Y n S n n Y n S n n Y n S n

**20** 0,5236 1,0628 **34** 0,5396 1,1255 **48** 0,5477 1,1574 **64** 0,5533 1,1793

**21** 0,5252 1,0696 **35** 0,5403 1,1285 **49** 0,5481 1,1590 **66** 0,5538 1,1814

**22** 0,5268 1,0754 **36** 0,5410 1,1313 **50** 0,5485 1,1607 **68** 0,5543 1,1834

**23** 0,5283 1,0811 **37** 0,5418 1,1339 **51** 0,5489 1,1623 **70** 0,5548 1,1854

**24** 0,5296 1,0864 **38** 0,5424 1,1363 **52** 0,5493 1,1638 **72** 0,5552 1,1873

**25** 0,5309 1,0915 **39** 0,5430 1,1388 **53** 0,5497 1,1653 **74** 0,5557 1,1890

**26** 0,5320 1,0961 **40** 0,5436 1,1413 **54** 0,5501 1,1667 **76** 0,5561 1,1906

**27** 0,5332 1,1004 **41** 0,5442 1,1436 **55** 0,5504 1,1681 **78** 0,5565 1,1923

**28** 0,5343 1,1047 **42** 0,5448 1,1458 **56** 0,5508 1,1696 **80** 0,5569 1,1938

**29** 0,5353 1,1086 **43** 0,5453 1,1480 **57** 0,5511 1,1708 **82** 0,5572 1,1953

**30** 0,5362 1,1124 **44** 0,5458 1,1499 **58** 0,5515 1,1721 **84** 0,5576 1,1967

**31** 0,5371 1,1159 **45** 0,5463 1,1519 **59** 0,5518 1,1734 **86** 0,5580 1,1980

**32** 0,5380 1,1193 **46** 0,5468 1,1538 **60** 0,5521 1,1747 **88** 0,5583 1,1994

**33** 0,5388 1,1226 **47** 0,5473 1,1557 **62** 0,5527 1,1770 **90** 0,5586 1,2007

Tabla No 6. Método de Gumbel, valores de Y n y S n .

Fuente: Hidrología en la Ingeniería. Germán Monsalve Sáenz. Primera Edición, Julio de 1995.

**3.5.4.** **Distribución Pearson Tipo III**

Esta distribución tiene la siguiente ecuación:

P(T) = x̅ + k(T) ∙S x
Donde,

P(T) : Precipitación máxima para un periodo de retorno T.

x̅ : Promedio de la serie de precipitaciones.

k(T) : Factor de frecuencia.

S x : Desviación estándar de la serie de precipitaciones.

Cuando el coeficiente de asimetría C s = 0, el factor de frecuencia k es igual a la variable normal estándar z,

en el caso que C s ≠0 el valor de k(T) se determina según:

k(T) = z+ (z [2] −1)k+ [1]

[1]

3 [(z] [3] [ −6z)k] [2] [ −(z] [2] [ −1)k] [3] [ + zk] [4] [ + 1] 3

3 [k] [5]

Con:

k= [C] [s]

6

Apéndice-02-Hidrología PROYECTO PARQUE FOTOVOLTAICO SOLAR ORIENTE
Página 16 de 41 OBRAS HIDRÁULICAS - PAS 155

**3.5.5.** **Distribución Log-Pearson Tipo III**

Esta distribución tiene la siguiente ecuación:

Log(P(T)) = y̅ + k(T) ∙S y

Donde:

P(T) : Precipitación máxima para un periodo de retorno T.

y̅ : Promedio de los logaritmos en base 10 de la serie de precipitaciones.

k(T) : Factor de frecuencia.

S y : Desviación estándar de los logaritmos en base 10 de la serie de precipitaciones.

Cuando el coeficiente de asimetría C s = 0, el factor de frecuencia k es igual a la variable normal estándar z,

en el caso que C s ≠0 el valor de k(T) se determina según:

k(T) = z+ (z [2] −1)k+ [1]

[1]

3 [(z] [3] [ −6z)k] [2] [ −(z] [2] [ −1)k] [3] [ + zk] [4] [ + 1] 3

3 [k] [5]

Con:

**3.5.6.** **Distribución Gamma (2 parámetros)**

k= [C] [s]

6

Esta función de distribución está dada por la siguiente expresión:

F(x) = [a] [β] [x] [β−1] [e] [−ax]

Γ(β)

Donde,

F(x) : Función de distribución asociada a la variable aleatoria x.

a : Parámetro de dispersión.

β : número de eventos respecto a la variable aleatoria x.

En que,

a= [x̅]

S x

2 [ ; β=] [x̅] [2]

S x

2

Donde,

x̅ : Promedio de la serie de precipitaciones.

S x : Desviación estándar de la serie de precipitaciones.

**3.5.7.** **Resultados Análisis de Frecuencia**

A continuación, se muestran los resultados obtenidos del análisis de frecuencia para las distribuciones

descritas y periodos de retorno (T) de 2, 5, 10, 20, 25, 50, 100 y 200 años:

PROYECTO PARQUE FOTOVOLTAICO SOLAR ORIENTE Apéndice-02-Hidrología
OBRAS HIDRÁULICAS - PAS 155 Página 17 de 41

Tabla No 7. Resultados análisis de frecuencia.

Fuente: Elaboración Propia.

Estos resultados han sido representados de forma gráfica en la siguiente figura:

Figura No 5. Resultados obtenidos del análisis de frecuencia.

Fuente: Elaboración Propia.

Apéndice-02-Hidrología PROYECTO PARQUE FOTOVOLTAICO SOLAR ORIENTE
Página 18 de 41 OBRAS HIDRÁULICAS - PAS 155

**3.6.** **Prueba de bondad del ajuste**

Finalizado el análisis de frecuencia, el siguiente paso es elegir la función de distribución que mejor se ajusta

a los datos de precipitaciones para cada estación. A continuación, se presentan dos métodos analíticos, que

como resultado deben arrojar cual es la distribución que mejor se ajusta a la serie de datos, y de esta forma

determinar la precipitación de diseño en distintos periodos de retorno.

**3.6.1.** **Test Chi cuadrado**

La prueba Chi-Cuadrado es un método estadístico que permite determinar la distribución que mejor ajuste

tiene con la serie de datos registrados en cada estación.

El procedimiento aplicado al caso de una variable hidrológica y para cada distribución analizada es la

siguiente:

 - Se divide el rango de variación de la muestra de N valores en k intervalos de clase, con lo que se

define un histograma de la muestra. El número de intervalos de clase se define por medio de la

siguiente ecuación:

k= 1 + 3.3 log 10 (N)

Es recomendable que el número de intervalos de clase sea igual o superior a k= 5. La amplitud de

cada intervalo se determina según:

a= [l] [su][p] [−l] [in][f]

k

 - A partir de este histograma, se determina la frecuencia absoluta de los valores observados f i para

cada uno de los intervalos.

 - A continuación, se adopta la hipótesis que la muestra corresponde a una cierta distribución

conocida, con función de densidad de frecuencia f(x).

 - Si se designa con C i a las fronteras de clase del histograma, las frecuencias absolutas esperadas e i

para cada clase y para la distribución elegida, vienen dadas por:

C i

i

e i f(x)dx
= N∙∫

C i−1

- Si la hipótesis adoptada es la adecuada, se demuestra que:

k

2

χ m

= ∑

i=1

(f i −e i ) [2]

e i

Se aproxima a una distribución χ ν2 con ν= k−s−1 grados de libertad, donde s es el número de parámetros

de la función de densidad de frecuencia en análisis.

En consecuencia, la prueba es la siguiente: se compara el valor obtenido de la muestra χ m2 con el valor de

la variable χ ν2, tabulado para un cierto nivel de confianza elegido.

2

Finalmente, se escoge como más probable aquella distribución que arroje el menor valor para la variable χ m

PROYECTO PARQUE FOTOVOLTAICO SOLAR ORIENTE Apéndice-02-Hidrología
OBRAS HIDRÁULICAS - PAS 155 Página 19 de 41

**3.6.2.** **Prueba Kolmogorov-Smirnov**

Esta prueba consiste en comparar el máximo valor absoluto de la diferencia D entre la función de

distribución de probabilidad observada F 0 (x m ) y la estimada F(x m )

D= máx |F 0 (x m ) −F(x m )|

La función de distribución de probabilidad observada se calcula de acuerdo a la siguiente expresión:

m
F 0 (x m ) = 1 − n+ 1

Donde m es el número de orden del dato x m en una lista de mayor a menor y n es el número total de datos.

Se compara el valor de la variable D con el valor crítico d que depende del número de datos y el nivel de

significancia, aceptando la hipótesis siempre y cuando se cumpla con D < d. En la Tabla No 8 se muestran

los valores de d, de acuerdo al tamaño de la muestra y al nivel de significancia.

**5** 0,51 0,56 0,67

**10** 0,37 0,41 0,49

**15** 0,30 0,34 0,40

**20** 0,26 0,29 0,35

**25** 0,24 0,26 0,32

**30** 0,22 0,24 0,29

**40** 0,19 0,21 0,25

Tabla No 8. Valores críticos de “d” para prueba Kolmogorov-Smirnov.

Fuente: MC. Vol. III.

**3.6.3.** **Resultados Prueba de Bondad**

Las distancias máximas de las distribuciones analizadas se muestran a continuación:

**Gumbel** 0,44 0,14

**Log Normal** 0,41 0,08

**Normal** 0,42 0,18

**Pearson III** 0,47 0,09

**Log Pearson III** 0,46

**Gamma** 0,47 0,09

Apéndice-02-Hidrología PROYECTO PARQUE FOTOVOLTAICO SOLAR ORIENTE
Página 20 de 41 OBRAS HIDRÁULICAS - PAS 155

Weibull 0,45 0,13

**Mejor distribución** **Log. Normal** **Log. Normal**

Tabla No 9. Resultados prueba de bondad del ajuste.

Fuente: Elaboración Propia.

Se observa que las distribuciones Gumbel y Weibull se ajustan de buena forma a los Datos Históricos tal y

como se muestra en la Figura No 5. En ella se observa que la curva de la distribución Normal tiende a

aplanarse a medida que aumentamos el período de retorno (T), mientras que las curvas correspondientes

a las distribuciones Log. Normal y Log. Pearson III crece exponencialmente representando de mejor forma

los eventos de precipitación extremos que encontramos en nuestra base de datos de la estación

Guatacondo DGA, finalmente en base a los resultados obtenidos mediante la prueba de bondad de ajuste,

se opta por la distribución **Log Normal.**

**3.1.** **Precipitación de Diseño**

Una vez realizado todo el proceso de estudio y tratamiento de los datos históricos obtenidos de la estación

Guatacondo DGA de la DGA, se obtiene la precipitación máxima diaria anual asociada a los distintos

periodos de retorno.

Según el 3.702.404 del Manual de Carreteras Vol. III, estos resultados son amplificados en un 10 % dado que

normalmente las 24 horas de mayor precipitación no coinciden con el intervalo de tiempo de medición, entre

las 8:00 am y las 8:00 am del día siguiente.

A continuación, se muestra cuadro resumen:

Periodo de retorno (T=años)

**Estación** **T=2** **T=5** **T=10** **T=25** **T=50** **T=100** **T=150** **T=200**

Tabla No 10. Precipitaciones máximas diarias de diseño para los distintos períodos de retorno (T).

Fuente: Elaboración Propia.

Los datos pluviométricos obtenidos en las estaciones se comparan con las isoyetas representativas de la

zona de estudio extraídas del producto “Precipitaciones máximas diarias” del portal Infraestructura de Datos

Geoespaciales (IDE Chile), donde se muestra la precipitación máxima diaria para T=10 años. En la Figura No

6 se presentan las estaciones pluviométricas y las isoyetas consideradas.

PROYECTO PARQUE FOTOVOLTAICO SOLAR ORIENTE Apéndice-02-Hidrología
OBRAS HIDRÁULICAS - PAS 155 Página 21 de 41

Figura No 6. Isoyetas en zona de estudio.

Fuente: Elaboración Propia.

Los valores obtenidos en Guatacondo DGA coinciden en la isoyeta de 20 mm para periodo de retorno de 10

años. Dentro de los rangos de las isoyetas en que quedan las estaciones cercanas al parque Solar Oriente

y que se encuentran a altitudes parecidas, se estima un valor de 5,6 mm de isoyeta, lo que entrega un valor

de 5,42 mm para periodo de retorno de 10 años en el parque Solar Oriente.

**3.1.** **Intensidad de diseño**

La determinación de las curvas Intensidad-Duración-Frecuencia (IDF) es de importancia para la aplicación

de métodos Precipitación-Escorrentía que permiten el cálculo de caudales. Este método se describe en

detalle en el numeral 3.702.404 del Manual de Carreteras.

Las curvas IDF se pueden estimar a partir de datos pluviométricos para duraciones de lluvia mayores a 1

[hora] en base a la siguiente expresión:

T = CD t ∙CF T ∙P 2410

P t

10

Donde:

P tT : Precipitación con período de retorno “T” años y duración “t” horas

CD t : Coeficiente de duración para t horas.

CF T : Coeficiente de frecuencia para T años de período de retorno.

P 2410 : Lluvia máxima diaria (8AM a 8AM) de 10 años de período de retorno.

Apéndice-02-Hidrología PROYECTO PARQUE FOTOVOLTAICO SOLAR ORIENTE
Página 22 de 41 OBRAS HIDRÁULICAS - PAS 155

**3.1.1.** **Coeficientes de duración**

La Tabla 3.702.403.A del MC. Vol. N°3 resume los coeficientes de duración para 10 años de periodo de

retorno. En nuestro caso, la estación más cercana sería la de Lequena, se ubica en la zona cordillerana y

posee unas características climáticas muy distintas por lo que no se utilizará en la totalidad de la cuenca. En

estos casos, dicho coeficiente se calcula mediante el método de Grunsky:

t10 = i 2410

t

i t

10

24 t

~~√~~ [24]

Donde:

i t10 : Intensidad de precipitación de “t” horas y 10 años de período de retorno.

t : Tiempo de duración de la tormenta en horas.

De ello se obtiene la siguiente expresión:

10

10 = [P] [24]

i 24

24

Una vez obtenidas las intensidades de diseño para cada una de las duraciones, se obtienen las

precipitaciones de diseño y con ello, los coeficientes de duración asociados, obteniendo los siguientes

resultados:

**Duración (horas)**

1 2 4 6 8 10 12 14 18 24

**Lequena** 0,34 0,52 0,75 0,87 0,93 0,94 0,95 0,96 0,92 1,00

**Grunsky** 0,20 0,29 0,41 0,50 0,58 0,65 0,71 0,76 0,87 1,00

Tabla No 11. Coeficientes de duración para 10 años de período de retorno.

Fuente: MC. Vol. III.

**3.1.2.** **Coeficientes de frecuencia**

Por otro lado, se han obtenido los coeficientes de frecuencia mediante la siguiente expresión:

CF T = P [P] [10][T]

Donde:

CF T : Coeficiente de frecuencia para un período de retorno T.

P [T] : Precipitación para un período de retorno T.

P [10] : Precipitación para un período de retorno de 10 años.

Los parámetros obtenidos se identifican en la siguiente tabla:

PROYECTO PARQUE FOTOVOLTAICO SOLAR ORIENTE Apéndice-02-Hidrología
OBRAS HIDRÁULICAS - PAS 155 Página 23 de 41

Tabla No 12. Coeficientes de frecuencia para distintos períodos de retorno. Fuente: MC. Vol. III.

**3.1.3.** **Curvas IDF**

Una vez obtenidos los coeficientes de duración y frecuencia es posible obtener las curvas IDF. Finalmente,

la intensidad correspondiente a dicha precipitación queda dada por:

T

[ [mm]

T

t

I t

[mm] hrs ~~[]]~~ [ = P] t [t]

Los resultados de la aplicación de estas ecuaciones para la determinación de las intensidades de diseño

para distintos periodos de retorno se presentan en las siguientes tablas:

**1** 1,945 4,291 6,579 10,438 14,095 18,487 21,398 23,712

**2** 1,487 3,281 5,031 7,982 10,778 14,137 16,363 18,133

**4** 1,072 2,366 3,628 5,756 7,773 10,195 11,800 13,076

**6** 0,829 1,830 2,806 4,451 6,011 7,884 9,125 10,112

**8** 0,665 1,467 2,249 3,569 4,819 6,321 7,316 8,107

**10** 0,538 1,186 1,819 2,886 3,897 5,111 5,916 6,556

**12** 0,453 0,999 1,532 2,430 3,282 4,305 4,982 5,521

**14** 0,392 0,865 1,327 2,105 2,843 3,729 4,315 4,782

**18** 0,292 0,645 0,989 1,569 2,119 2,779 3,217 3,565

**24** 0,238 0,526 0,806 1,279 1,727 2,266 2,622 2,906

Tabla No 13. Intensidades de Diseño Guatacondo DGA.

Fuente: Elaboración propia.

Apéndice-02-Hidrología PROYECTO PARQUE FOTOVOLTAICO SOLAR ORIENTE
Página 24 de 41 OBRAS HIDRÁULICAS - PAS 155

**1** 0,327 0,721 1,106 1,755 2,369 3,108 3,597 3,986

**2** 0,231 0,510 0,782 1,241 1,675 2,198 2,543 2,819

**4** 0,163 0,361 0,553 0,877 1,185 1,554 1,798 1,993

**6** 0,133 0,294 0,451 0,716 0,967 1,269 1,468 1,627

**8** 0,116 0,255 0,391 0,620 0,838 1,099 1,272 1,409

**10** 0,103 0,228 0,350 0,555 0,749 0,983 1,137 1,260

**12** 0,094 0,208 0,319 0,507 0,684 0,897 1,038 1,151

**14** 0,087 0,193 0,296 0,469 0,633 0,831 0,961 1,065

**18** 0,077 0,170 0,261 0,414 0,558 0,733 0,848 0,940

**24** 0,067 0,147 0,226 0,358 0,484 0,634 0,734 0,814

Tabla No 14. Intensidades de Diseño Solar Oriente.

Fuente: Elaboración propia.

A continuación, se presentan las curvas IDF obtenidas, para duraciones mayores a 1 hora.

Figura No 7. Curvas IDF duraciones entre 1 y 24 horas, Guatacondo DGA.

Fuente: Elaboración propia.

PROYECTO PARQUE FOTOVOLTAICO SOLAR ORIENTE Apéndice-02-Hidrología
OBRAS HIDRÁULICAS - PAS 155 Página 25 de 41

Figura No 8. Curvas IDF duraciones entre 1 y 24 horas, Solar Oriente.

Fuente: Elaboración propia.

**3.2.** **Cálculo de caudales de crecida**

La metodología utilizada para la estimación de los caudales de crecida considerando el análisis de una

cuenca sin información fluviométrica es la sugerida por el “Manual de Carretera Volumen No3” (MOP, 2014)

y el “Manual de Cálculo de Crecidas y Caudales Mínimos en Cuencas Sin Información Fluviométrica”

(DGA,1995).

A continuación, se describe la metodología utilizada en el presente estudio para la obtención del caudal de

crecida. En cuencas de áreas mayores a 20 km [2] con el método del Hidrograma Unitario Sintético y para

cuencas de áreas menores a 20 Km [2 ] con el método Racional.

**3.2.1.** **Áreas aportantes**

Para la obtención de las quebradas y sus cuencas asociadas se trabajan modelos digitales de terreno de

libre acceso, utilizando un modelo de elevación digital (DEM) y las cartas IGM de la zona. De esta forma,

mediante el uso de sistemas GIS se obtiene de forma gráfica la definición de las cuencas aportantes y sus

quebradas.

Apéndice-02-Hidrología PROYECTO PARQUE FOTOVOLTAICO SOLAR ORIENTE
Página 26 de 41 OBRAS HIDRÁULICAS - PAS 155

Figura No 9. Cuencas aportantes y quebradas.

Fuente: Elaboración propia.

En el ámbito del Proyecto se identifican 5 cuencas aportantes al área del proyecto. A continuación, se

presentan los datos de las cuencas estudiadas.

**1** 638,66 89,30 4585,75 963,00 1899,14 16,55

**2** 93,33 49,24 1714,00 960,00 1161,96 5,59

**3** 12,34 13,94 1100,00 983,50 1020,38 4,94

**4** 17,15 16,02 1062,00 970,25 1017,88 7,01

**5** 35,27 25,12 1171,50 970,25 1051,75 6,00

Tabla No 15. Datos cuencas aportantes.

Fuente: Elaboración propia.

**3.2.2.** **Tiempo de concentración**

Tiempo de concentración se define como el tiempo mínimo necesario para que todos los puntos de una

cuenca estén aportando agua de escorrentía directa, de forma simultánea al punto de salida, punto de

desagüe o punto de cierre. Está determinado por el tiempo que tarda en llegar a la salida de la cuenca el

agua que procede del punto hidrológicamente más alejado, y representa el momento a partir del cual el

caudal de escorrentía es constante. El punto hidrológicamente más alejado es aquél desde el que el agua

de escorrentía emplea más tiempo en llegar a la salida.

El tiempo de concentración se puede determinar mediante varios métodos, cuyos resultados son sometidos

a juicio para seleccionar aquellos que expresen valores razonables en relación con lo observado en terreno.

PROYECTO PARQUE FOTOVOLTAICO SOLAR ORIENTE Apéndice-02-Hidrología
OBRAS HIDRÁULICAS - PAS 155 Página 27 de 41

**1.** **Ecuación Normas Españolas**

Donde:

T c : Tiempo de concentración [min]

L : Longitud del cauce principal [km]

Tc= 18 ∙ [L] [0.76]

S [0.19]

S : Pendiente media de la cuenca [m/m]

**2.** **Kirpich**

T c = 0,02 ~~(~~ S [L] [0,385][0,77] ~~[)]~~

Donde:

T c : Tiempo de concentración [min]

L : Longitud del cauce principal [km]

S : Pendiente media de la cuenca [m/m]

Esta ecuación fue desarrollada a partir de información del SCS en siete cuencas rurales de Tennessee con

canales bien definidos, pendientes empinadas (3% a 10%) y áreas mayores a 2 km [2] .

**3.** **Giandotti**

[60]

0,8 ~~[(]~~ [4√A+ 1,5L] √H m

~~)~~

T c = [60]

√H m

Donde:

T c : Tiempo de concentración [min]

A : Área de la cuenca [km [2] ]

L : Longitud del cauce principal [km]

H m : Diferencia de nivel entre la cota media de la cuenca y la cota de salida [m]

Este método es válido en cuencas con A< 2 [km [2] ] y si L/5,4 < T c < L/3,6.

Los resultados se muestran a continuación:

Tiempo de concentración (minutos)

**Cuenca/Método** Normas españolas Kirpich Giandotti Adoptado

**1** 769,75 458,31 NO APLICA 769,75

**2** 601,77 421,70 NO APLICA 601,77

**3** 236,05 201,42 NO APLICA 236,05

Apéndice-02-Hidrología PROYECTO PARQUE FOTOVOLTAICO SOLAR ORIENTE
Página 28 de 41 OBRAS HIDRÁULICAS - PAS 155

Tiempo de concentración (minutos)

**4** 245,59 259,45 NO APLICA 245,59

**5** 355,96 322,24 NO APLICA 355,96

Tabla No 16. Tiempo de concentración.

Fuente: Elaboración propia.

El tiempo de concentración adoptado es el calculado mediante el método de norma española.

**3.2.3.** **Coeficiente de escorrentía**

Este parámetro depende de las características geomorfológicas del sector a analizar, por ejemplo:

topografía, vegetación, capacidad de almacenamiento, etc. Por tal motivo, depende fundamentalmente de

la inspección del terreno.

Durante el mes de agosto de 2023, se realizó una visita a terreno con el objetivo de identificar cursos

preferentes de escurrimiento. La conclusión de dicha visita fue la de que el sector es de pendiente moderada

a baja, con algunos puntos altos locales de forma excepcional. El terreno no tiene vegetación, salvo sectores

puntuales en quebradas, presenta alto nivel de compactación y porosidad media, lo que hace suponer un

moderado coeficiente de infiltración del suelo. No se observan indicios de escurrimientos recientes, aunque

sí se identifican numerosos cauces preferentes secos que coinciden con la identificación de las cartas IGM.

Se incluye imagen de la zona:

Figura No 10. Fotografía del ámbito del Proyecto.

Fuente: Elaboración propia.

Una primera aproximación para la estimación del coeficiente de escorrentía fue la metodología indicada en

el Manual de Carreteras:

PROYECTO PARQUE FOTOVOLTAICO SOLAR ORIENTE Apéndice-02-Hidrología
OBRAS HIDRÁULICAS - PAS 155 Página 29 de 41

Tabla No 17. Factores coeficiente de escorrentía.

Fuente: MC. Vol. III

En relación al relieve, la pendiente general del terreno para las cuencas es del orden de un 5% a un 20%;

además de acuerdo a lo observado en terreno de forma superficial, se presume un suelo de textura media

con capa superficial de arena y presencia de finos, por consiguiente, con moderada capacidad de

infiltración. No se observa cobertura vegetal salvo sectores singulares de quebradas y el almacenamiento

superficial es inexistente. Considerando todo lo anterior, se estimó el siguiente coeficiente de escorrentía:

Apéndice-02-Hidrología PROYECTO PARQUE FOTOVOLTAICO SOLAR ORIENTE
Página 30 de 41 OBRAS HIDRÁULICAS - PAS 155

**Relieve** 0,22 0,15 0,14 0,15 0,15

**Infiltración** 0,06 0,06 0,06 0,06 0,06

**Cobertura** 0,16 0,16 0,16 0,16 0,16

**Total** **0,52** **0,45** **0,44** **0,45** **0,45**

Tabla No 18. Coeficiente de Escorrentía, MC. Vol. III.

Fuente: Elaboración propia.

Para determinar coeficientes de escorrentía de tormentas de periodos de retorno mayor, el manual de

carreteras establece factores de amplificación de 1,1, 1,2, y 1,25 para periodos de retorno de 25, 50 y 100

años respectivamente. En base a lo anterior, con el objetivo de calcular los coeficientes de escorrentía para

los distintos periodos de retorno, se realiza una regresión con los factores antes mencionados en base al

coeficiente de escorrentía para un periodo de retorno de 10 años.

En base a lo antes expuesto se obtuvieron los siguientes coeficientes de escorrentía para los distintos

periodos de retorno:

**Cuencas** **T=2** **T=5** **T=10** **T=25** **T=50** **T=100** **T=150** **T=200**

**1** 0,44 0,49 0,52 0,57 0,62 0,65 0,68 0,70

**2** 0,38 0,42 0,45 0,50 0,54 0,56 0,59 0,61

**3** 0,38 0,41 0,44 0,48 0,53 0,55 0,58 0,60

**4** 0,38 0,42 0,45 0,50 0,54 0,56 0,59 0,61

**5** 0,38 0,42 0,45 0,50 0,54 0,56 0,59 0,61

Tabla No 19. Coeficientes de escorrentía de diseño.

Fuente: Elaboración propia.

**3.2.4.** **Hidrograma Unitario Sintético**

Para la estimación de los caudales de crecidas en las cuencas con área mayor a 20 Km [2] y periodo de

retorno de 2, 5, 10, 25, 50, 100 y 200 años se utilizó el programa HEC-HMS, considerando un modelo de la

cuenca con los siguientes componentes y metodología.

◼ Se define la subcuenca del punto de control.

◼ Método de crecidas para subcuencas: HU adimensional del SCS.

◼ Cálculo de Infiltración: CN.

PROYECTO PARQUE FOTOVOLTAICO SOLAR ORIENTE Apéndice-02-Hidrología
OBRAS HIDRÁULICAS - PAS 155 Página 31 de 41

◼ Se consideraron escenario de uso de suelo actual.

A continuación, se presentan los distintos componentes necesarios para realizar el modelo hidrológico

mediante el uso del HEC-HMS.

Para el hietograma de precipitación se consideró 5 duraciones de tormenta 4, 6, 8, 12 y 24 horas para los

cuales se determinaron los hietogramas de precipitación. Para determinar la cantidad de precipitación para

cada duración de la tormenta se utilizó la curva de duración de Varas obtenida de “Influencia del hietograma

de una tormenta en la crecida resultante” (Varas, 1985) que se presenta a continuación.

Grunsky 0,408 0,500 0,577 0,707 1,000

Guatacondo DGA 0,750 0,870 0,930 0,950 1,000

Tabla No 20. Coeficientes de duración para 10 años de periodo de retorno.

Fuente: Tabla 3.702.403.A, Manual de Carreteras Vol. 3.

Para las lluvias con duración 4, 6 y 8 horas se utilizaron hietogramas con intervalos de 15 minutos, para la

lluvia de duración 10 horas se utilizaron intervalos de 30 min, mientras que para las tormentas con 24 horas

de duración se utilizaron hietogramas con intervalos de 1 hora.

Otro parámetro relevante que interviene en el método del HUS, es la precipitación efectiva. Para estimar

dicho valor, se ha considerado el método de la Curva Número (CN) desarrollado por el U.S. Soil Conservation

Service, el cual consiste en determinar su valor, de acuerdo al uso del suelo y sus características

geomorfológicas.

De acuerdo a esta metodología, el valor de la precipitación efectiva (Pe) se determina a través de la siguiente

relación.

P e = P−I [(P−I] a [a] + S [)] [2]

Donde,

P : Precipitación media que cae sobre la cuenca.

S : Retención potencial máxima.

I a : Abstracción inicial.

A base de mediciones realizadas en numerosas cuencas experimentales, se determinaron las siguientes

relaciones.

I a = 0,2 ∙S , P e =

(P−0,2 ∙S) [2]

P+ 0,8 ∙S

Donde el valor de S (en mm) se determina con la siguiente fórmula.

S= [25400] −254

CN

Apéndice-02-Hidrología PROYECTO PARQUE FOTOVOLTAICO SOLAR ORIENTE
Página 32 de 41 OBRAS HIDRÁULICAS - PAS 155

En que CN corresponde al valor de la curva número seleccionada. Este valor depende de las condiciones

de humedad antecedente, del tipo, condición y uso del suelo, y se encuentra tabulado para las diferentes

condiciones.

Para estimar el valor de la CN, se debe considerar las condiciones antecedentes de humedad, las que

dependen de las precipitaciones registradas en los cinco días precedentes al evento en análisis,

subdividiéndose en tres grupos (I, II y III), de acuerdo a lo indicado en la tabla siguiente.

I < 12,7 <35,6

Tabla No 21. Clasificación de condiciones antecedentes de humedad del suelo.

Fuente: Hidrología Aplicada, Ven Te Chow (1996).

En Tabla No 22, se muestran valores del coeficiente CN para condiciones de humedad antecedente AMC II,

considerando que el suelo se clasifica en cuatro grupos (A, B, C y D), de acuerdo con el siguiente detalle.

◼ Grupo A: Arena profunda, suelos profundos depositados por el viento, limos agregados.

◼ Grupo B: Suelos poco profundos depositados por el viento.

◼ Grupo C: Margas arcillosas, margas arenosas poco profundas, suelos con bajo contenido

orgánico y suelos con alto contenido de arcilla.

◼ Grupo D: Suelos que se expanden significativamente cuando se mojan, arcillas altamente

plásticas y ciertos suelos salinos.

Finalmente, los valores de CN para otras condiciones de humedad antecedentes se determinan aplicando

las siguientes ecuaciones de transformación:

4,2CN(II) 23CN(II)
CN(I) = 10 −0,058CN(II) [ , CN(III) =] 10 + 0,13CN(II)

Donde,

CN(I) : CN en condiciones de humedad antecedente AMC I.

CN(II) : CN en condiciones de humedad antecedente AMC II.

CN(III) : CN en condiciones de humedad antecedente AMC III.

Vegas de ríos Condiciones óptimas 30 58 71 78

PROYECTO PARQUE FOTOVOLTAICO SOLAR ORIENTE Apéndice-02-Hidrología
OBRAS HIDRÁULICAS - PAS 155 Página 33 de 41

Áreas Comerciales 85% impermeables 89 92 94 95

Distritos Industriales 75% impermeables 81 88 91 93

Pavimentados Estacionamientos pavimentados, techos, accesos, etc. 98 98 98 98

Tabla No 22. Valores sugeridos por S.C.S. para distintos tipos de suelo en condiciones de humedad antecedente AMC II.

Fuente: Hidrología Aplicada, Ven Te Chow (1996).

En la visita a terreno se determinó que en la zona del estudio predominan los suelos de arena suelta y en

los sectores donde se evidencia el paso de cauces en crecidas los suelos presentaban cierta presencia de

arcillas y limos con plasticidad, por lo que se adoptó como tipo de suelo el Grupo B, con condición de

humedad antecedente CN(I).

A pesar que los suelos desérticos no se encuentran mencionados en la Tabla No 22, Ponce realiza un estudio

de la curva número extendiendo a distintas coberturas de suelo. Según lo observado en el parque se puede

asimilar a un suelo barbecho con pendiente >3% (Ponce V.M., 1989) con una CN(II) de 93, siendo finalmente

utilizado un valor de CN(I) de 85.

En consecuencia, el valor de la precipitación efectiva Pef (mm), se calculó con la relación desarrollada por

el U.S. Soil Conservation Service, ver Tabla No 23.

**Periodo de Retorno (años)** **Guatacondo DGA** **Solar Oriente**

**2** 2,49 0,09

**5** 8,47 0,97

**10** 14,83 2,26

Apéndice-02-Hidrología PROYECTO PARQUE FOTOVOLTAICO SOLAR ORIENTE
Página 34 de 41 OBRAS HIDRÁULICAS - PAS 155

**Periodo de Retorno (años)** **Guatacondo DGA** **Solar Oriente**

**25** 25,89 4,86

**50** 36,51 7,54

**100** 49,32 10,90

**150** 57,84 13,18

**200** 64,62 15,00

Tabla No 23. Precipitación efectiva para estación Guatacondo DGA y sector Solar Oriente.

Fuente: Elaboración Propia TYPSA.

A partir del Hidrograma Unitario y de las precipitaciones efectivas asociadas a una duración y periodo de

retorno dado, es posible obtener los Hidrogramas de Escorrentía Directa, multiplicando el Hidrograma

Unitario por la precipitación efectiva y el área de la subcuenca asociada (método de convolución).

Considerando los parámetros morfológicos de las cuencas aportante al punto de control presentados en

Tabla No 15, se calcularon los tiempos de concentración de las cuencas estudiadas, ver Tabla No 16.

Una vez modeladas las crecidas en las cuencas, el cálculo de los caudales con el programa HEC-HMS, se

realizó superponiendo y rastreando los hidrogramas obtenidos en los puntos de interés definidos para este

estudio.

Esto se realizó empleando el método de Muskingum, el cual está implementado en el programa HEC-HMS.

Figura No 11. Modelo de Solar Oriente en HEC-HMS.

Fuente: Elaboración Propia TYPSA.

El método de Muskingum plantea el cálculo del caudal efluente de un tramo en el intervalo de tiempo t+ Δ t,

por medio de la siguiente ecuación:

##### O = C I + C I + C O

_j_ + 1 1 _j_ + 1 2 _j_ 3 _j_

Donde,

PROYECTO PARQUE FOTOVOLTAICO SOLAR ORIENTE Apéndice-02-Hidrología
OBRAS HIDRÁULICAS - PAS 155 Página 35 de 41

##### −  t 2 KX C =

##### −  t + 2 KX 2 K (1 X ) C =

3

##### − − 2 K 1 X +  t 2 K 1 X

##### − −  t + 2 KX 2 K (1 X )  t C =

3

##### − − K 1 X +  t 2 K 1 X +  t

##### − − + 2 KX 2 K (1 X )  t C =

3

##### − − X +  t 2 K 1 X +  t

##### −  t 2 KX  t + 2 KX C 2 = − − K 1 X +  t 2 K 1 X +

##### −  t 2 KX  t + 2 C 2 = − − 2 K 1 X +  t 2 K 1 X

##### −  t =

##### 2

##### − 2 KX  t + C 2 = − − X +  t 2 K 1

1 2 3

##### 2 K 1

2 3

##### − − − 1 X +  t 2 K 1 X +  t 2 K 1 X +  t
#### ( ) ( ) ( )

##### − X + 

I j e I j+1 : son los caudales de entrada al tramo en los tiempos t y t+ Δ t, respectivamente.

O j e O j+1 : son los caudales de salida del tramo en los tiempos t y t+ Δ t, respectivamente.

K y X : constantes.

Para evaluar los coeficientes C1, C2 y C3 se hicieron los siguientes supuestos:

◼ El parámetro K se encuentra definido por la expresión (Muskingüm -Cunge):

 _x_ 

= =

_x_
_K_ =

_x_ _x_

=

_c_ _dQ_

_k_

_dQ_

_dA_

Este se estima igual al tiempo de viaje de la onda a lo largo del tramo definido entre los puntos de

control (descargas).

◼ Por otro lado, el parámetro X toma valores entre 0,0 y 0,3; este parámetro tiene poco peso en los

resultados que arroja el método, de manera que al no disponerse de la información que permita

realizar una calibración, se adoptó un valor 0,15.

**3.2.5.** **Método Racional**

El método Racional, relaciona el coeficiente de escorrentía, la intensidad media de la lluvia para distintos

períodos de retorno, y el área aportante pluvial, mediante la siguiente relación:

_C_ - _I_ - _A_
_Q_ =

6.3

Donde,

Q : Caudal instantáneo máximo de periodo de retorno T en m [3 ] /s.

C : Coeficiente de escorrentía de período de retorno T años.

I : Intensidad media de lluvia para un período de retorno de T años y una duración igual al tiempo de

concentración de la cuenca pluvial, en mm/hr.

Ap : Área pluvial aportante en km [2] .

El coeficiente de escorrentía C se obtiene del acápite 3.2.3.

**3.2.6.** **Cálculo de intensidades**

Las intensidades de precipitación asociadas a diferentes periodos de retorno y el tiempo de concentración

calculado fueron obtenidas mediante las curvas IDF, a continuación, se presentan los resultados:

Apéndice-02-Hidrología PROYECTO PARQUE FOTOVOLTAICO SOLAR ORIENTE
Página 36 de 41 OBRAS HIDRÁULICAS - PAS 155

**1** 12,83 0,36 0,79 1,21 1,92 2,59 3,40 3,93 4,36

**2** 10,03 0,10 0,23 0,35 0,55 0,75 0,98 1,14 1,26

**3** 3,93 0,17 0,37 0,56 0,89 1,20 1,58 1,82 2,02

**4** 4,09 0,16 0,36 0,55 0,87 1,17 1,54 1,78 1,98

**5** 5,93 0,13 0,30 0,45 0,72 0,97 1,28 1,48 1,64

Tabla No 24. Intensidades de diseño.

Fuente: Elaboración propia.

**3.2.7.** **Caudales para distintos períodos de retorno**

Una vez obtenidos todos los parámetros necesarios para la aplicación de los métodos, se obtuvieron los

caudales de diseño para distintos periodos de diseño:

**2** 14,50 0,70 0,10 0,20 0,30

**5** 31,90 1,50 0,30 0,40 0,70

**10** 50,20 2,30 0,50 0,60 1,10

**25** 96,70 3,60 0,70 1,00 1,80

**50** 153,90 4,80 1,00 1,40 2,40

**100** 231,00 6,30 1,30 1,80 3,10

**150** 285,70 7,40 1,50 2,10 3,60

**200** 330,80 8,20 1,70 2,30 4,00

Tabla No 25. Caudales líquidos con el método HUS.

Fuente: Elaboración propia.

**2** 28,22 1,03 0,21 0,30 0,51

**5** 68,23 2,49 0,52 0,72 1,23

PROYECTO PARQUE FOTOVOLTAICO SOLAR ORIENTE Apéndice-02-Hidrología
OBRAS HIDRÁULICAS - PAS 155 Página 37 de 41

**10** 111,60 4,07 0,85 1,18 2,01

**25** 194,78 7,11 1,48 2,05 3,50

**50** 286,94 10,48 2,17 3,02 5,16

**100** 392,04 14,31 2,97 4,13 7,04

**150** 477,91 17,45 3,62 5,03 8,59

**200** 545,04 19,90 4,13 5,74 9,80

Tabla No 26. Caudales líquidos con el método Racional.

Fuente: Elaboración propia.

Respecto a la elección del método, el uso de la fórmula o método racional se recomienda para cuencas

pequeñas, pero dada la simpleza del método de aplicación se generaliza para cuencas mayores sin tener

en cuenta que el método incluye supuestos que para cuencas mayores no se cumplen, siendo la

propagación de errores mayor mientras más alejado se esté de los supuestos iniciales.

Para delimitar la aplicación de la metodología, se debe definir qué se entiende por cuenca pequeña. En

general en una cuenca pequeña, en el sentido hidrológico, se deben cumplir los siguientes supuestos:

◼ Distribución temporal de la lluvia uniforme en toda la cuenca (para todo tiempo t la lluvia es igual en

toda la cuenca).

◼ Distribución espacial de la lluvia uniforme en toda la cuenca (en toda la cuenca cae la misma

cantidad de agua).

◼ La duración de una tormenta generalmente es mayor que el tiempo de concentración de la cuenca.

◼ La escorrentía ocurre a través de flujo superficial.

◼ Las pendientes son suficientemente fuertes para evitar almacenamientos superficiales.

Como todas las cuencas poseen distintas características es imposible generalizar un área máxima para que

una cuenca sea considerada pequeña, pero en la actualidad se utilizan criterios como que el tiempo de

concentración sea menor a 1 hora, o que su superficie sea menor a 2,5 km2 (“Engineering hydrology,

principles and practices”, Víctor Ponce, 2014). Adicionalmente, se debe tener en cuenta que al aplicar el

método racional no se tiene en cuenta lo siguiente:

◼ Variaciones temporales de la lluvia en la cuenca (a mayor superficie de la cuenca mayores

variaciones).

◼ Variaciones espaciales de la lluvia en la cuenca (a mayor superficie de la cuenca mayores

variaciones).

◼ Condición de humedad del suelo al recibir la lluvia.

Apéndice-02-Hidrología PROYECTO PARQUE FOTOVOLTAICO SOLAR ORIENTE
Página 38 de 41 OBRAS HIDRÁULICAS - PAS 155

Los tres puntos anteriores restringen el uso del método racional exclusivamente a cuencas pequeñas, que

cumplen o tienen condiciones muy cercanas a las condiciones ideales de aplicación del método.

En el caso de las cuencas de este estudio, específicamente cuenca 3 y 4, estas no cumplen la mayoría de

los criterios para ser definidas como cuencas pequeñas:

◼ Las dos tienen tiempos de concentración mayores a 1 hora, a pesar de haber aplicado la

metodología con el tiempo de concentración menor.

◼ Las dos cuencas tienen áreas del orden de los 20 km2.

◼ Debido a la diferencia de altura entre la parte alta y la salida de la cuenca tampoco se cumple el

criterio de uniformidad espacial de las precipitaciones, por lo que el supuesto de una intensidad

constante en toda la cuenca se debería descartar.

Si bien los mayores caudales de diseño se obtendrían con la fórmula racional, no se cumplen los supuestos

básicos del método, ni se tienen las características de las cuencas para que este sea aplicable. Por esto no

se recomiendan su uso ya que los caudales no serían representativos y aparentemente están

sobredimensionados.

Sumado a esto existe una recomendación en la literatura [1] en la que se indica que no se utilice la fórmula

racional en cuencas que presentan varios cauces que se unen, como las del presente estudio. Para estos

casos se recomiendan métodos racionales que son modificados de forma particular para las cuencas

estudiadas.

En el caso de Chile existe un método racional modificado (DGA, 1995) que extiende el uso de la fórmula a

cuencas mayores, pero que posee datos solo hasta la región de Atacama por lo que no es extrapolable

hasta Tarapacá. Bajo la aplicación de ese método modificado, los caudales que se obtienen son menores

a los obtenidos por el método racional sin modificar, lo que está en línea con la sobreestimación de caudales

que introduce el método racional cuando se aplica sin modificaciones en cuencas que no son pequeñas.

Es por ello que, se calcularon los caudales mediante los 2 métodos solicitados y finalmente se optó por

considerar los resultados obtenidos mediante el **método del HUS** .

**3.2.1.** **Caudales detríticos para distintos periodos de retorno**

A priori se estima un caudal detrítico con la siguiente expresión de la “Guía Metodológica para Proyectos de

Modificación de Cauces” de la DGA (2016):

Q detr = 1 −CQ liq v

Donde:

Q detr : Caudal sólido más caudal líquido (m [3] /s).

Q liq : Caudal líquido (m [3] /s).

C v : Concentración en volumen de sólidos (%).

1 San Diego County Hydrology Manual, County of San Diego, Department of Public Works (Junio 2003)

PROYECTO PARQUE FOTOVOLTAICO SOLAR ORIENTE Apéndice-02-Hidrología
OBRAS HIDRÁULICAS - PAS 155 Página 39 de 41

Respecto a la concentración en volumen de sólidos, se supone un 40% según lo indicado en la Guía

metodológica para proyectos de Modificación de Cauces (DGA, 2016).

**2** 24,17 1,17 0,17 0,33 0,50

**5** 53,17 2,50 0,50 0,67 1,17

**10** 83,67 3,83 0,83 1,00 1,83

**25** 161,17 6,00 1,17 1,67 3,00

**50** 256,20 8,00 1,67 2,33 4,00

**100** 385,00 10,50 2,17 3,00 5,17

**150** 476,17 12,33 2,50 3,50 6,00

**200** 551,33 13,67 2,83 3,83 6,67

Tabla No 27. Caudales detríticos de cuencas.

Fuente: Elaboración propia.

**4.** **Conclusiones y recomendaciones**

En la actualidad no existen normas o criterios de diseño que establezca un periodo de retorno para estas

obras asociadas a parques fotovoltaicos. En el manual de carreteras se indica que las obras de saneamiento

y drenaje de caminos deben ser diseñadas con un caudal asociado a un periodo de retorno de 10 años,

obteniendo un riesgo hidrológico de falla de 65%.

Tabla No 28. Periodos de retorno para diseños de drenaje.

Fuente: MC. Vol. III.

De acuerdo a lo expuesto en el manual de carreteras, el riesgo hidrológico de falla de una obra se obtiene

de la siguiente manera:

R= 1 −(1 − T [1]

n

T ~~[)]~~

Apéndice-02-Hidrología PROYECTO PARQUE FOTOVOLTAICO SOLAR ORIENTE
Página 40 de 41 OBRAS HIDRÁULICAS - PAS 155

Donde:

T : Periodo de retorno [años]

n : Vida útil supuesta [años]

Considerando que el parque tendrá una vida útil supuesta de 35 años y un caudal de 100 años de periodo

de retorno para el diseño de drenaje, se obtiene un riesgo hidrológico de falla del 30%.

Todas las obras de drenaje deberán ser diseñadas para el caudal de diseño T = 100 años y verificadas para

un caudal de T = 150 años.

Respecto a la solución propuesta para la protección de las instalaciones del Proyecto frente a eventuales

crecidas que considera: i) la implementación de dos canales perimetrales en el sector este de las aristas del

perímetro del predio, en función al sentido de la pendiente existente en cada tramo; y ii) un badén en el

camino de acceso, resulta conveniente a la hora de ejecutar el proyecto constructivo, dado que no se

requerirán obras de cruce con el cableado de baja y media tensión.

PROYECTO PARQUE FOTOVOLTAICO SOLAR ORIENTE Apéndice-02-Hidrología
OBRAS HIDRÁULICAS - PAS 155 Página 41 de 41