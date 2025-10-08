---
title: Sin título
author: dss-mschulz
date: D:20200129221124-03'00'
language: es
type: report
pages: 72
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ANEXO 4.5.2 MODELACIÓN ATMOSFÉRICA DE EMISIONES
-->

# ANEXO 4.5.2 MODELACIÓN ATMOSFÉRICA DE EMISIONES

**NOVIEMBRE 2019**

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**INDICE**

**Página 2 de 72**

**1** **INTRODUCCIÓN ........................................................................................... 5**

1.1 O BJETIVOS ............................................................................................................................................ 6

**2** **DESCRIPCIÓN DEL PROYECTO ..................................................................... 7**

**3** **ANTECEDENTES ............................................................................................ 8**

3.1 M ARCO L EGAL R EGULATORIO ................................................................................................................... 8

3.1 E STADO DE LA C ALIDAD DEL A IRE EN LA CIUDAD DE C ONCEPCIÓN .................................................................... 9

_3.1.1_ _Línea de Base: Análisis del Cumplimiento Normativo ................................................................... 9_

_3.1.2_ _Concentración promedio Mensual de MP10 y MP2,5................................................................. 13_

_3.1.3_ _Ciclo de concentración diaria de MP10 y MP2,5 en la ciudad de Concepción ............................ 14_

**4** **JUSTIFICACIÓN DE LOS MODELOS UTILIZADOS EN LA MODELACIÓN ...... 16**

4.1 U SO DEL M ODELO CALPUFF ................................................................................................................ 16

4.2 U SO DEL M ODELO W EATHER R ESEARCH AND F ORECASTING M ODEL (WRF) ................................................... 18

**5** **METODOLOGÍA........................................................................................... 18**

5.1 M ODELACIÓN M ETEOROLÓGICA ............................................................................................................. 18

_5.1.1_ _Dominio de Modelación de Meteorológica ................................................................................ 18_

5.2 D OMINIO DE M ODELACIÓN CALPUFF .................................................................................................... 21

5.3 P OST P ROCESAMIENTO DE I NFORMACIÓN ................................................................................................. 23

5.4 E SCENARIO DE M ODELACIÓN ................................................................................................................. 27

**6** **RESULTADOS ............................................................................................. 30**

6.1 C ARACTERIZACIÓN G EOFÍSICA ................................................................................................................. 30

_6.1.1_ _Topografía .................................................................................................................................. 30_

_6.1.2_ _Caracterización Meteorológica ................................................................................................... 31_

6.2 R ESULTADOS DE LA M ODELACIÓN DE D ISPERSIÓN DE MP10 Y MP2,5 .......................................................... 46

_6.2.1_ _Material Particulado Respirable, MP10 ...................................................................................... 46_

_6.2.2_ _Material Particulado Fino Respirable, MP2,5 ............................................................................. 53_

_6.2.3_ _Concentración de Contaminantes en Puntos Discretos .............................................................. 59_

6.3 A PORTE A LA E STACIÓN DE M ONITOREO DE R EPRESENTATIVIDAD P OBLACIONAL (EMRP) .................................. 61

**7** **ANÁLISIS DE INCERTIDUMBRE DEL MODELO ........................................... 63**

7.1 A NÁLISIS DE AJUSTE SOBRE EL MODELO METEOROLÓGICO ............................................................................ 63

7.2 A JUSTE DE VARIABLES DEL MODELO ......................................................................................................... 64

_7.2.1_ _Correlación de temperaturas observada y modelada................................................................. 65_

_7.2.2_ _Correlación de velocidad del viento observada y modelada. ...................................................... 66_

_7.2.3_ _Correlación de dirección del viento observada y modelada ....................................................... 68_

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**Página 3 de 72**

**8** **CONCLUSIÓN ............................................................................................. 70**

**9** **REFERENCIAS ............................................................................................ 72**

**Índice de Tablas**

Tabla 1. Valores normados para MP10 y MP2,5 en Chile............................................................... 8

Tabla 2. Concentración promedio anual de MP10 Estación Kingston College ................................ 10

Tabla 3. Concentración promedio anual de MP2,5 Estación Kingston College ............................... 12

Tabla 4. Coordenadas de vértices del área de estudio. ............................................................... 19

Tabla 5. Coordenadas de la modelación CALPUFF ...................................................................... 21

Tabla 6. Características de Receptores discretos. ....................................................................... 24

Tabla 7. Polígonos de Modelación ............................................................................................. 29

Tabla 8. Frecuencia de los vientos anuales, WRF. ...................................................................... 31

Tabla 9. Frecuencia de los vientos verano, WRF. ....................................................................... 34

Tabla 10. Frecuencia de los vientos otoño, WRF. ....................................................................... 36

Tabla 11. Frecuencia de los vientos invierno, WRF. .................................................................... 38

Tabla 12. Frecuencia de los vientos en primavera, WRF. ............................................................ 40

Tabla 13. Concentración modelada de MP10 evaluada en puntos receptores ............................... 60

Tabla 14. Aumento de la concentración basal en la EMRP Kingston College ................................. 61

Tabla 15. Resumen de valores de ajuste de variables del modelo con la estación Coronel Norte. .. 64

**Índice de Figuras**

Figura 1. Ubicación del Proyecto ................................................................................................. 7

Figura 2. Concentración Promedio 24 horas de MP10 Estación Kingston College .......................... 10

Figura 3. Concentración Promedio Trianual de MP10 Estación Kingston College ........................... 11

Figura 4. Concentración Promedio 24 horas de MP2,5 Estación Kingston College ......................... 12

Figura 5. Concentración Promedio Trianual de MP2,5 Estación Kingston College .......................... 13

Figura 6. Concentración promedio mensual de MP10 Estación Kingston College ........................... 13

Figura 7. Concentración promedio mensual de MP2,5 Estación Kingston College .......................... 14

Figura 8. Ciclo horario de MP10 y MP2,5 promedio para el mes de julio, año 2018 ....................... 15

Figura 9. Dominio de la modelación de WRF .............................................................................. 20

Figura 10. Dominio de la Modelación de CALPUFF ...................................................................... 22

Figura 11. Ubicación de receptores ........................................................................................... 25

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**Página 4 de 72**

Figura 12. Estación de Monitoreo .............................................................................................. 26

Figura 13. Emisiones directas año 4 (operación) ........................................................................ 28

Figura 14. Elevación de terreno del área de estudio ................................................................... 30

Figura 15. Rosa de los Vientos Anual, WRF. .............................................................................. 32

Figura 16. Frecuencia de los vientos ......................................................................................... 33

Figura 17. Rosa de los Vientos Verano, WRF ............................................................................. 34

Figura 18. Frecuencia del viento en verano ............................................................................... 35

Figura 19. Rosa de los Vientos Otoño, WRF ............................................................................... 36

Figura 20. Frecuencia de los otoño ........................................................................................... 37

Figura 21. Rosa de los Vientos Invierno, WRF............................................................................ 38

Figura 22. Frecuencia de los invierno, año 2014 ........................................................................ 39

Figura 23. Rosa de los Vientos Primavera, WRF ......................................................................... 40

Figura 24. Frecuencia de los vientos en primavera ..................................................................... 41

Figura 25. Perfil diario de velocidad del viento, WRF año 2014 ................................................... 42

Figura 26. Temperatura Mensual en la WRF .............................................................................. 43

Figura 27. Perfil vertical de la temperatura ................................................................................ 44

Figura 28. Perfil diario de temperatura, WRF ............................................................................. 45

Figura 29. Precipitación mensual, WRF ...................................................................................... 45

Figura 30. Mapa de Dispersión Promedio Anual MP10 ................................................................ 48

Figura 31. Mapa de Isoconcentración Promedio Anual MP10 ....................................................... 49

Figura 32. Mapa de Dispersión Promedio 24 horas MP10 ............................................................ 51

Figura 33. Mapa de Isoconcentración Promedio 24 horas MP10 .................................................. 52

Figura 34. Mapa de Dispersión Promedio Anual MP2,5 ............................................................... 54

Figura 35. Mapa de Isoconcentración Promedio Anual MP2,5 ...................................................... 55

Figura 36. Mapa de Dispersión Promedio 24 horas MP2,5 ........................................................... 57

Figura 37. Mapa de Isoconcentración Promedio 24 horas MP2,5 ................................................. 58

Figura 38. Correlación entre temperaturas observadas y temperaturas modeladas ....................... 65

Figura 39. Comparación entre la frecuencia de temperatura de los datos modelados y observados 66

Figura 40. Correlación entre velocidad del viento observadas y temperaturas modeladas ............. 67

Figura 41. Comparación entre la frecuencia de velocidad del viento de los datos modelados y

observados.............................................................................................................................. 68

Figura 42. Correlación entre la dirección del viento observadas y temperaturas modeladas .......... 68

Figura 43. Comparación entre la frecuencia de dirección del viento de los datos modelados y

observados.............................................................................................................................. 69

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**Página 5 de 72**

**1** **Introducción**

En el siguiente informe se presenta la modelación de las emisiones atmosféricas del proyecto

inmobiliario **“Brisas II”** y su cuantificación en términos de concentración de MP10 y MP2,5,

además de la evaluación en los puntos receptores de interés y a la estación de calidad del

aire más cercana.

En el Informe de Estimación de Emisiones, se estimaron las tasas de emisiones que podrían

generarse en todas las fases del proyecto, es decir, construcción y operación, ya que como

es de esperar los proyectos inmobiliarios no contemplan etapas de abandono. Los resultados

permitieron concluir que es en el año 4, donde se desarrollará la operación de las 295

unidades habitacionales de la situación basal, junto con la operación de 100 viviendas y 80

departamentos que corresponden al proyecto “Brisas II”. Es por esto que durante el año 4

se alcanzan las tasas más altas de emisión de todo el proyecto y que además éstas precisan

ser evaluadas en término de la concentración en las que dichas emisiones se encontrarán

en el aire, a fin de evaluar una posible afectación a la salud de las personas mediante la

comparación con los límites establecidos en las normas de calidad primaria de calidad del

aire vigentes en el territorio nacional, cuyo bien jurídico protegido es la salud de las

personas.

La evaluación de la dispersión y concentración de las emisiones de material particulado se

realizó mediante el programa CALPUFF, el cual es un modelo de dispersión usado

ampliamente para simulaciones de concentraciones ambientales de las emisiones de

operaciones normales, con el objeto de establecer, desarrollar y analizar escenarios de

emisión y regulación. A su vez, CALPUFF es recomendado por el Ministerio de Medio

Ambiente en la “Guía para el Uso de Modelos de Calidad del Aire en el SEIA”, publicada el

año 2012. Los resultados y el análisis de estos se presentan en el siguiente informe.

Es importante señalar que el proyecto se encuentra emplazado en una zona declarada como

saturada y no latente por material particulado respirable MP10, mediante D.S. N° 41/2006

según el Ministerio Secretaría General de la Presidencia (MINSEGEPRES) y saturada por

Material Particulado Fino Respirable MP2,5 como concentración diaria, de acuerdo al D.S.

N°15/2015 del Ministerio del Medio Ambiente (MMA). Por lo que actualmente el ministerio

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**Página 6 de 72**

trabaja en el proceso de elaboración del Plan de Prevención y Descontaminación Atmosférica

para las comunas de Concepción Metropolitano, por tanto, actualmente, no existen límites

máximos de emisión permisible.

**1.1** **Objetivos**

Este informe tiene por objetivo presentar una descripción de las emisiones, específicamente

en relación a la dispersión de los contaminantes, además de la evaluación de la

concentración de contaminantes en puntos receptores de interés.

Para lo anterior se plantean los siguientes objetivos específicos:

 Evaluar el alcance de las emisiones de MP10, MP2,5 en la atmósfera, en términos de

la concentración que éstas podrían alcanzar en el aire.

 Evaluar las concentraciones obtenidas en función de la normativa nacional vigente,

a fin de predecir si la operación del proyecto generará efectos adversos a la calidad

de vida y salud de las personas y/o medio ambiente.

 Evaluar en puntos de interés de forma discreta [1] la concentración de los

contaminantes en estudio.

1 En términos de la modelación se entenderá como evaluación discreta aquella a la predicción de la concentración en un punto receptor

específico y a una altura determinada, es decir, puntualmente.

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**2** **Descripción del Proyecto**

**Página 7 de 72**

El proyecto inmobiliario “Brisas II” ubicado en el sector norponiente de la comuna de San

Pedro de la Paz, perteneciente a la provincia de Concepción, Región del Biobío (Figura 1),

consiste en la construcción de 100 viviendas y 4 edificios con un total de 80 departamentos

de uso residencial (180 unidades habitacionales), además de áreas verdes y equipamiento

en una superficie total de 2,40 hectáreas aproximadamente. A estas viviendas se les

sumaran las 295 unidades habitacionales existentes (Situación basal), las cuales

corresponden al proyecto inmobiliario “Brisas de San Pedro”, emplazadas en una superficie

de 3,87 hectáreas.

La construcción del proyecto “BRISAS II”, se llevará a cabo en un plazo de aproximadamente

3 años (36 meses), partiendo el primer semestre del año 2020 para finalizar el segundo

semestre del año 2022.

En la siguiente figura se muestra el proyecto que se somete a evaluación ambiental (blanco)

y la situación basal (rojo).

**Figura 1. Ubicación del Proyecto**

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**Página 8 de 72**

**3** **Antecedentes**

**3.1** **Marco Legal Regulatorio**

Los contaminantes MP10 y MP2,5 están regulados bajo normas de calidad primaria, cuyo

objetivo es proteger la salud de las personas de los efectos agudos y crónicos de la

exposición de estos contaminantes con un riesgo aceptable. Para esto, se fijan límites de

concentración permitidos, condiciones de superación de la norma y los niveles que dan paso

a situaciones de emergencia ambiental.

El material particulado respirable MP10 es regulado por el D.S. 59/1998 del Ministerio

Secretaría General de la Presidencia y el material particulado fino respirable MP2,5 es

regulado por el D.S. 12/2011 del Ministerio del Medio Ambiente.

En Tabla 1 se comparan para los contaminantes MP10 y MP2,5, los valores del límite anual,

límite diario y los rangos que dan origen a situaciones de alerta, preemergencia y

emergencia ambiental.

**Tabla 1. Valores normados para MP10 y MP2,5 en Chile.**

|Nivel|MP10 (μg/m3)|MP2.5 (μg/m3)|
|---|---|---|
|**Límite anual**|50|20|
|**Limite diario**|150|50|
|**Alerta**|195-239|80-109|
|**Preemergencia**|240-329|110-169|
|**Emergencia**|330 o mayor|170 o mayor|

Fuente: En base a D.S. 59/1998 MINSEGEPRES y D.S. 12/2011 MMA

La superación del límite normativo no es motivo de condiciones de superación de la norma,

sino que se considera que la norma es incumplida bajo las siguientes condiciones:

`o` Cuando el promedio de la concentración anual de tres años consecutivos iguale o

supere los 50 μg/m3.

`o` Si el percentil 98 (P98) de las concentraciones de 24 horas durante un año sea igual

o superior a 150 μg/m3.

`o` Si durante un año se registrasen siete o más días cuya concentración sea mayor a

150 μg/m3.

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**Página 9 de 72**

En el mismo contexto, las condiciones de superación de la norma de MP2,5 son las que se

describen a continuación:

`o` Cuando el promedio de la concentración anual de tres años consecutivos iguale o

supere los 20 μg/m3.

`o` Si el percentil 98 (P98) de las concentraciones de 24 horas durante un año sea igual

o superior a 50 μg/m3

Todo lo anterior, requiere del análisis exclusivo de estaciones de monitoreo con

representatividad poblacional (EMRP).

**3.1** **Estado de la Calidad del Aire en la ciudad de Concepción**

El proyecto se emplaza en la comuna de Concepción, que pertenece a la zona denominada

como Concepción Metropolitano, que fue declarada como zona saturada mediante

D.S. N° 15/2015 MMA que declara Zona Saturada por Material Particulado Fino Respirable

MP2,5 como concentración diaria, a las comunas de Lota, Coronel, San Pedro de la Paz,

Hualqui, Chiguayante, Concepción, Penco, Tomé, Hualpén y Talcahuano, debido a las altas

concentraciones de material particulado registrado en el área a partir de las Estaciones de

Monitoreo Kingston College, Punteras y Cerro Merquin.

**3.1.1** **Línea de Base: Análisis del Cumplimiento Normativo**

De las tres estaciones que dieron lugar a la declaración de saturación de la zona, para

efectos de este estudio, sólo se considera una, debido a su cercanía con el proyecto, lo que

la hace representativa. Esta estación corresponde a Kingston College, ubicada en la comuna

de Concepción, específicamente en las coordenadas UTM 673.817 E 5.927.247 N,

aproximadamente a 11,8 km del proyecto, cuyos datos para la caracterización fueron

extraídos desde el Sistema de Información Nacional de Calidad del Aire (SINCA) el día 25

de noviembre de 2019.

En la Figura 2, se presenta la concentración promedio de 24 horas registrada en dicha

estación, en donde se muestran los años que cumplen con la condición de tener más del

75% de los datos, y de donde es posible observar que existe superación en el límite

impuesto por el D.S. N° 59/1998 MINSEGPRES, que establece la norma de calidad primaria

para material particulado respirable (MP10) en los años 2015 y 2016.

**Página 10 de 72**

160

140

120

100

80

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

60

40

20

00

|Col1|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|||||||
|||||||
|||102|106|||
|71|75|||71||
||||||69|
|||||||
|||||||
|||||||

2013 2014 2015 2016 2017 2018

Concentracion 24 horas Límite Norma Lineal (Concentracion 24 horas)

**Figura 2. Concentración Promedio 24 horas de MP10 Estación Kingston College**

Fuente: Elaboración propia en base a los datos dispuestos en el Sistema Nacional de Calidad del

Aire (SINCA).

Respecto a la concentración promedio anual de MP10, se observa que ésta no excede la

norma para ningún año evaluado.

**Tabla 2. Concentración promedio anual de MP10 Estación Kingston College**

|Año|Porcentaje de<br>datos<br>disponibles<br>(%)|Concentración<br>Promedio Anual<br>(μg/m3)|Límite normativo<br>D.S. 59/1998<br>MINSEGEPRES<br>(μg/m3)|Porcentaje de<br>excedencia de la<br>norma (%)|
|---|---|---|---|---|
|2013|99|35,81|50|No excede|
|2014|99|32,32|32,32|No excede|
|2015|79|38,09|38,09|No excede|
|2016|89|40,42|40,42|No excede|
|2017|100|30,32|30,32|No Excede|
|2018|99|29,62|29,62|No Excede|

Fuente: Elaboración propia en base a los datos dispuestos en el Sistema Nacional de Calidad del

Aire (SINCA).

Con respecto a la concentración promedio trianual, se calculó para cuatro períodos

consecutivos correspondientes a los años 2013-2015, 2014-2016, 2015-2017, 2016-2018,

esto como resultado de la cantidad de datos existentes y necesarios para el análisis (>75%).

En la siguiente figura se presentan las concentraciones obtenidas, de donde se desprende

que no existe superación de la normativa en ninguno de los períodos analizados.

**Página 11 de 72**

60,00

50,00

40,00

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

30,00

20,00

10,00

0,00

|Col1|Col2|Col3|Col4|
|---|---|---|---|
||36,94|||
|35,41||36,28|33,45|
|||||
|||||
|||||

2013-2015 2014-2016 2015-2017 2016-2018

Concentración Trianual Límite Norma Lineal (Concentración Trianual)

**Figura 3. Concentración Promedio Trianual de MP10 Estación Kingston College**

Fuente: Elaboración propia en base a los datos dispuestos en el Sistema Nacional de Calidad del

Aire (SINCA).

Con respecto a los días de emergencia, preemergencia y/o emergencia para los años

analizados, en esta estación no se registró ninguno que presente tales características.

El D.S. N° 12/2011 del MMA establece la norma primaria de calidad ambiental para material

particulado fino respirable MP2,5 regulando la concentración promedio anual y diaria.

Es importante mencionar que respecto a las concentraciones para este contaminante en la

estación Kingston College, se observa que la estación solo presenta datos a partir del año

2015, por lo que de los cuatro años analizados (2015 al 2018) todos cumplen con el mínimo

de datos exigidos para realizar una caracterización de este contaminante.

En la Figura 4, se observan las concentraciones promedio de 24 horas de MP2,5 registradas

en la estación Kingston College, donde es posible analizar que de los cuatro años donde fue

posible caracterizar la concentración, ésta supera el límite establecido para todos los años.

**Página 12 de 72**

56,0

55,0

54,0

53,0

52,0

51,0

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

50,0

49,0

48,0

|Col1|55,8|Col3|55,8|
|---|---|---|---|
|||||
|||||
|||||
|52,2||||
|||||
|||50,1||
|||||
|||||

2015 2016 2017 2018

Concentración 24 horas Límite Norma Lineal (Concentración 24 horas)

**Figura 4. Concentración Promedio 24 horas de MP2,5 Estación Kingston College**

Fuente: Elaboración propia en base a los datos dispuestos en el Sistema Nacional de Calidad del

Aire (SINCA).

La concentración promedio anual de MP2,5 que establece el D.S. N° 12/2011 MMA, para los

años analizados, es superada en dos periodos, siendo el 2016 aquel que cuenta con un

mayor porcentaje de excedencia, con un 18,46%.

**Tabla 3. Concentración promedio anual de MP2,5 Estación Kingston College**

|Año|Porcentaje de<br>datos<br>disponibles (%)|Concentración<br>Promedio Anual<br>(μg/m3)|Límite normativo<br>D.S. 12/2011 MMA<br>(μg/m3)|Porcentaje de<br>excedencia de la<br>norma (%)|
|---|---|---|---|---|
|2013|0|-|20|-|
|2014|0|-|-|-|
|2015|76|20,71|20,71|3,57|
|2016|80|23,69|23,69|18,46|
|2017|95|16,47|16,47|No excede|
|2018|98|19,24|19,24|No excede|

Fuente: Elaboración propia en base a los datos dispuestos en el Sistema Nacional de Calidad del

Aire (SINCA).

Con respecto a las concentraciones de MP2,5 como promedio trianual, ésta se caracterizó

para el periodo 2015-2017 y 2016-2018, tal como se presenta en la siguiente figura.

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**Página 13 de 72**

|20,29|Col2|
|---|---|
|||
||19,80|
|||
|||

**Figura 5. Concentración Promedio Trianual de MP2,5 Estación Kingston College**

Para el período analizado, no existen días calificados como alerta, preemergencia y

emergencia ambiental por las altas concentraciones de MP2,5 en el aire.

**3.1.2** **Concentración promedio Mensual de MP10 y MP2,5**

A continuación, en la Figura 6 se muestra la concentración promedio mensual de MP10

registrada en la estación Kingston College, para el mismo período antes analizado.

**Figura 6. Concentración promedio mensual de MP10 Estación Kingston College**

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**Página 14 de 72**

**EMISIONES “BRISAS II”**

En la Figura 7, se observa la variación de la concentración promedio mensual de MP2,5 para

el período 2013-2018 dado que como se presentó en la Tabla 3, para los años 2013 y 2014

existe 0% de registros para ese contaminante, como se observa en la Tabla 3.

De esta información se desprende para el caso de material particulado fino que la

concentración promedio mensual tiene un comportamiento esperado, pues es menor en los

meses más cálidos y superior en los meses de otoño e invierno, exceptuando el año 2016,

el cual presenta altas concentraciones en la época estival.

**Figura 7. Concentración promedio mensual de MP2,5 Estación Kingston College**

**3.1.3** **Ciclo de concentración diaria de MP10 y MP2,5 en la ciudad de Concepción**

En la Figura 8, se observa la evolución de la concentración horaria durante el mes de Julio

del año 2018, la que fue calculada como el promedio de las concentraciones horarias de los

días para el mes indicado en la estación de monitoreo Kingston College.

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**Página 15 de 72**

**EMISIONES “BRISAS II”**

**Figura 8. Ciclo horario de MP10 y MP2,5 promedio para el mes de julio, año**

**2018**

En la figura se observa un cúmulo de concentración de MP10 y MP2,5, el cual se inicia a las

18 horas y tiene su peak entre las 20 y 21 horas, logrando una concentración promedio de

106,8 μ g/m [3] de MP10 y 95,5 μ g/m [3] de MP2,5. Desde ese momento, comienza a descender

paulatinamente hasta las 6 de la madrugada. Desde esa hora y hasta las 7 de la mañana la

concentración de MP se mantiene relativamente constante y desde entonces, hasta las 10

de la mañana la concentración de material particulado presenta un leve aumento,

influenciado probablemente por la capa residual. Luego de esto, la concentración comienza

a disminuir hasta las 15 horas, manteniéndose sin grandes fluctuaciones hasta las 16 horas.

Una hora más tarde la concentración de MP10 y MP2,5 comienza a aumentar

considerablemente, alcanzando máximas concentraciones en las horas de la tarde y la

noche.

El perfil de la concentración de MP10 y MP2,5 horaria, en un mes de invierno, está vinculado

a la fluctuación de la temperatura durante el día y el uso de calefactores en horarios donde

se reúne la familia. En conclusión, el comportamiento de la concentración de los

contaminantes es el típico de las ciudades cuyas altas concentraciones de material

particulado en el aire se deben al consumo intensivo de leña, como es el caso de Concepción.

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**4** **Justificación de los Modelos Utilizados en la Modelación**

**4.1** **Uso del Modelo CALPUFF**

**Página 16 de 72**

La modelación de dispersión atmosférica de las emisiones de MP10 y MP2,5 provenientes

del proyecto, se realizó con un modelo tipo “Puff”, específicamente el modelo CALPUFF.

Tal como lo define la Guía, los modelos tipo “Puff” son una combinación entre los modelos

Gaussianos y los modelos Lagrangeanos, en el sentido de que esencialmente calculan la

dispersión de contaminantes provenientes de una emisión instantánea, llamada “puff”, a lo

largo de una trayectoria. Su aproximación matemática consiste en estimar la dispersión en

forma Gaussiana en cada punto de una trayectoria, es decir, los modelos tipo “puff” sólo

requieren una trayectoria por “puff”, lo que hace su cálculo mucho más rápido. En el caso

de emisiones continuas, se simulan las trayectorias y la dispersión Gaussiana de muchos

“puffs”. El modelo tipo “puff” recomendado por la Guía es el modelo CALPUFF.

El CALPUFF, es un modelo completo que incorpora herramientas para procesar datos

meteorológicos y geofísicos, modelos de dispersión y pos-procesamiento. Dicho modelo es

recomendado por la Agencia de Protección Ambiental de los Estados Unidos (EPA) para

modelar transporte de contaminantes a larga distancia.

CALPUFF se compone de tres módulos:

- CALMET: Es un modelo meteorológico que desarrolla campos horarios de viento y

temperatura en una grilla de tres dimensiones. También asocia campos en dos dimensiones

de altura y usos de suelo.

Este módulo puede ser reemplazado por el modelo matemático WRF, cuyo uso es

recomendado por la guía citada.

- CALPUFF: Es un modelo de transporte y dispersión emitido desde fuentes

modeladas, simulando procesos de dispersión y transformación. CALPUFF utiliza los datos

generados por CALMET. Los archivos de salida de CALPUFF contienen las concentraciones

horarias o deposición por hora de flujos evaluados en receptores seleccionados.

- CALPOST: Es usado para procesar aquellos archivos generados por CALMET y

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**Página 17 de 72**

CALPUFF, produciendo tabulaciones que resumen los resultados de la simulación.

Ecuación del modelo CALPUFF

La ecuación básica que utiliza el modelo para realizar la modelaciones es la siguiente:

2

2σ
y [2][c] ~~[]]~~

2

Q
C=
2πσ x σ y

2
g=
(2π) [1 2] ⁄ σ z

2

g exp

~~[~~ [−d] 2σ x [2][a]

∑exp[ [−(H] [e] 2σ [+ 2nh)] z [2] [2]

2 2

[−d] 2σ x [2][a] [] exp[−d] 2σ y [2][c]

2

∞

n=−∞

[+ 2nh)] [2]

2σ z [2] ~~]~~

Dónde:

C, es concentración a nivel del suelo (g/m [3] ),

Q, es masa de contaminantes (g) en la nube.

σ x, es desviación estándar (m) de la distribución de Gauss en el viento a lo largo de la

dirección.

σ y, es desviación estándar (m) de la distribución de Gauss en el viento de costado

σ z, es desviación estándar (m) de la distribución de Gauss en la dirección vertical.

d a, es distancia (m) del centro de la nube al receptor en la dirección del viento a lo largo.

d c, es distancia (m) del centro de la nube al receptor en la dirección de viento cruzado.

g, es el término vertical (m) de la ecuación Gaussiana.

H, es la altura afectiva (m) desde el nivel del suelo del hojaldre.

h, es la altura de la capa de mezcla.

De acuerdo a las características del terreno, las distintas unidades geomorfológicas del área

de influencia del proyecto y el dominio de la modelación se consideraron utilizar el modelo

CALPUFF para simular la dispersión de los contaminantes.

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**Página 18 de 72**

**4.2** **Uso del Modelo Weather Research and Forecasting Model (WRF)**

El modelo Weather Research and Forecasting (WRF), es un modelo numérico recomendado

para la generación de datos meteorológicos y uno de los modelos de pronóstico

meteorológicos más avanzados.

Debido a la falta de una red robusta de estaciones meteorológicas, la Guía para el Uso de

Modelos de Calidad del Aire en el SEIA recomienda el uso de WRF por sobre el uso del

CALMET. Además, el mismo documento, sugiere el uso del WRF para la modelación de

dispersión de contaminantes con CALPUFF.

**5** **Metodología**

La modelación de la dispersión de contaminantes se realizó de acuerdo con los lineamientos

sugeridos en la “Guía para el Uso de Modelos de Calidad del Aire en el SEIA”, (SEA, 2012).

A continuación, se presentan las consideraciones para la evaluación del proyecto.

**5.1** **Modelación Meteorológica**

El modelo WRF es un modelo matemático que simula, a partir de variables influyentes en la

meteorología, las condiciones meteorológicas dentro de un dominio de modelación, para el

año 2014.

A continuación, se describen los criterios adoptados para la modelación meteorológica.

**5.1.1** **Dominio de Modelación de Meteorológica**

Se determinó un dominio de modelación WRF que incluyó el área circundante a la zona de

emplazamiento del proyecto y parte importante del Gran Concepción.

De este modo, el dominio de la modelación resultó ser 62 km x 62 km, con resolución

espacial de 1 km, tal como se muestra en la Figura 9 y cuyas coordenadas se pueden ver

en la siguiente tabla.

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**Página 19 de 72**

**Tabla 4. Coordenadas de vértices del área de estudio.**

|Vértice|Proyección: UTM, Huso 18 Sur; Datum: WGS-84|Col3|
|---|---|---|
|**Vértice**|**Este (km)**|**Norte (km)**|
|Suroeste|639,530|5.896,829|
|Sureste|701,530|5.896,829|
|Noroeste|639,530|5.958,829|
|Noreste|701,530|5.958,829|
|Centroide|670,530|5.927,829|

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**Figura 9. Dominio de la modelación de WRF**

**Página 20 de 72**

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**Página 21 de 72**

Por otro lado, la modelación fue realizada sobre 10 celdas de altura que van desde los 0 a

los 4.000 m. La altura de estas celdas considera un amplio rango para la variación diaria de

la capa de mezcla.

**5.2** **Dominio de Modelación CALPUFF**

La modelación de dispersión de MP10 y MP2,5 se realizó con el software CALPUFF, el cual

es capaz de simular el transporte de las partículas dentro de un área de estudio. Además,

permite modelar concentraciones en puntos discretos de interés.

Para esto el modelo tiene como datos de entrada dos in puts importantes: un modelo

meteorológico (WRF) y la tasa de emisión de las fuentes a modelar.

Para la simulación de dispersión de MP10 y MP2,5, se fijó un dominio de modelación acotado

en un área 20 km x 20 km, la cual abarca la totalidad del área del proyecto y otras áreas

cercanas. Es importante destacar que la extensión es menor al dominio del modelo

meteorológico WRF.

El dominio de modelación se escogió en consideración con las zonas circundantes al

proyecto inmobiliario, puntos receptores y la estación de calidad del aire más cercana

(Kingston College) que podría recibir algún aporte por la dinámica del transporte

atmosférico, tal como se presenta en la

**Tabla 5. Coordenadas de la modelación CALPUFF**

|Vértice|Proyección: UTM, Huso 19 S, Datum: WGS-84|Col3|
|---|---|---|
|**Vértice**|**Este (km)**|**Norte (km)**|
|Suroeste|655.551|5.908.888|
|Sureste|675.551|5.908.888|
|Noroeste|655.551|5.928.888|
|Noreste|675.551|5.928.888|

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**Página 22 de 72**

**Figura 10. Dominio de la Modelación de CALPUFF**

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**Página 23 de 72**

La modelación se realizó a través de la metodología de polígonos de emisión, los cuales

representan la calefacción y el tránsito dentro del área del proyecto. Desde ellos se simuló

las tasas de emisión de MP10 y MP2,5. Además, se consideró la transformación química de

los contaminantes en la atmósfera a través de MESOPUFF II, el que fue empleado con las

tasas de emisión directas NOx y SO 2 estimadas para la ejecución del proyecto en los distintos

escenarios y los valores por defecto del modelo para O 3 y NH 3 .

**5.3** **Post Procesamiento de Información**

La modelación de contaminantes fue evaluada en toda la grilla de modelación, con la que

se generaron los mapas de dispersión e isoconcentración de contaminantes. La modelación

ofrece un dato de concentración por cada vértice de la grilla, por lo que se usó el software

QGis para la digitalización de los resultados de la modelación.

Es importante señalar que estos mapas nacen de la modelación del dominio, representado

a través de una grilla de resolución 1km, la que entrega datos de concentración de cada

vértice. Dadas las características de la grilla, los mapas son el resultado de la interpolación

entre los datos de modelación en cada vértice. Además, los datos de concentración

generados por el modelo son el resultado de la concentración promedio de la primara capa

de modelación, la que tiene lugar desde 0 m nivel del suelo hasta los 20 m.

Por todo lo antes indicado, los mapas de dispersión e isoconcentración deben ser

considerados como una representación espacial de la pluma y no como referencia concreta

de la concentración, pues éstas suelen estar sobre dimensionadas.

Además, se realizó una evaluación de la concentración de los contaminantes estudiados en

cada uno de los puntos de interés, denominado punto receptor discreto. La modelación de

los puntos discretos tiene por objeto simular la concentración en el aire que una persona

pudiera captar, por lo tanto, fueron medidas a una altura 1,60 m sobre el nivel del suelo,

es decir, la media de la población chilena.

En la Tabla 6, se presentan las coordenadas UTM de los puntos receptores representativos

de viviendas habitación, alguno de ellos se encuentran dentro del proyecto y representan

viviendas que se encontrarán en operación en el año que se estima la máxima tasa de

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**Página 24 de 72**

máxima emisión para el proyecto. la distancia de cada punto receptor fue medida a un punto

representativo del proyecto (R1) ubicado en la coordenada UTM 665.589 m E 5.918.883 m

S.

**Tabla 6. Características de Receptores discretos.**

|Nombre|Coordenadas UTM, HUSO 19 S, WGS -84|Col3|Distancia al<br>emisor (m)|Dirección<br>desde<br>emisor|
|---|---|---|---|---|
|**Nombre**|**Este (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|
|R1|665.589|5.918.883|0|-|
|R2|665.505|5.918.901|0|-|
|R3|665.461|5.918.807|149|OSO|
|R4|665.719|5.918.763|177|SE|
|R5|665.530|5.918.741|153|SSO|
|R6|665.564|5.918.988|108|NNO|
|R7|665.698|5.918.932|120|ENE|
|R8|665.805|5.918.817|226|ESE|
|R9|665.841|5.918.977|270|ENE|
|R10|665.927|5.918.900|338|E|
|R11|665.651|5.919.404|524|N|
|R12|666.044|5.919.337|642|NE|
|R13|665.734|5.919.148|300|NNE|
|R14|665.621|5.919.235|355|N|
|R15|665.733|5.919.283|427|NNE|
|R16|665.788|5.918.997|229|ENE|
|R17|665.443|5.919.433|569|NNO|
|EMRP Kingston<br>College|673.817|5.927.247|11.740|NE|

En la Figura 11, se presenta la ubicación espacial de cada uno de los puntos receptores

evaluados. Cabe destacar que los receptores R6, R7, R16 se encuentran dentro del área de

la situación basal del proyecto, mientras que los receptores R1 y R2 se encuentran dentro

del área del proyecto. Además, a fin de poder predecir las concentraciones de contaminantes

en el área de influencia, se utilizó la información correspondiente a las estación de monitoreo

Kingston College, la cual fue caracterizadas dentro de la línea de base, tal como es sugerido

por la Guía para la Descripción de la Calidad del Aire en el Área de Influencia de Proyectos

que Ingresan al SEIA, cómo es posible apreciar en la figura antes mencionada, la estación

de monitoreo no se presenta por la distancia que tiene con el emisor, por tanto, la ubicación

espacial de está se observar en la Figura 12.

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**Figura 11. Ubicación de receptores**

**Página 25 de 72**

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**Figura 12. Estación de Monitoreo**

**Página 26 de 72**

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**5.4** **Escenario de Modelación**

**Página 27 de 72**

Según los resultados presentados en el Informe de Estimación de Emisiones, es en el año

cuatro donde se espera la mayor tasa de emisión de contaminante, esto por la operación

de las 295 unidades habitacionales de la situación basal (155 viviendas, 140 departamentos)

y de las unidades proyectadas por el proyecto “Brisas II” (100 viviendas, 80 departamentos),

es decir, 475 unidades habitacionales, sobre las cuales se supuso el peor escenario

existente. Respecto a las viviendas si bien estas no cuentan con ningun sistema de

calefacción, se consideró que el 100% de las viviendas se calefaccionaran en base a leña.

Las tasas de emision por concepto de calefacción, se modelaron durante los meses de marzo

a agosto, en base a la evolución de la concentración horaria presentada en la Figura 8 (ciclo

horario de MP10 y MP2,5 promedio para el mes de julio, año 2018), la que fue calculada

como el promedio de las concentraciones horarias en la estación de monitoreo Kingston

College.

Respecto a las tasas de emisión que corresponden al tránsito de vehículos por caminos

pavimentados dentro del área del proyecto, se modelaron en los períodos de 6 a 9 am y 18

a 22 pm.

En la Figura 13, se presentan las tasas de emisión que fueron modeladas. Es importante

mencionar que, para el escenario a evaluar, sólo fueron modeladas las fuentes directas en

ambas fases que corresponden a actividades de combustión por conceptos de calefacción y

transito interno dentro del area del proyecto.

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**Página 28 de 72**

**Figura 13. Emisiones directas año 4 (operación)**

A continuación, se presentan las fuentes emisoras que fueron modeladas con sus respectivas

coordenadas geográficas.

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**Tabla 7. Polígonos de Modelación**

**Página 29 de 72**

|Polígonos|Coordenadas UTM (m) WGS - 184 Huso 18 S|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Polígonos**|**A **|**A **|**B **|**B **|**C **|**C **|**D **|**D **|
|**Polígonos**|**x **|**y **|**x **|**Y **|**x **|**y **|**x **|**y **|
|P1|665.499|5.919.090|665.510|5.919.087|665.475|5.918.966|665.487|5.918.965|
|P2|665.511|5.919.083|665.636|5.919.062|665.507|5.919.055|665.632|5.919.035|
|P3|665.658|5.919.060|665.753|5.919.044|665.653|5.919.032|665.749|5.919.016|
|P4|665.532|5.919.039|665.618|5.919.024|665.529|5.919.013|665.613|5.918.999|
|P5|665.659|5.919.019|665.715|5.919.009|665.654|5.918.991|665.710|5.918.982|
|P6|665.504|5.919.006|665.709|5.918.971|665.497|5.918.963|665.701|5.918.931|
|P7|665.451|5.918.867|665.516|5.918.857|665.448|5.918.846|665.513|5.918.835|
|P8|665.574|5.918.848|665.629|5.918.839|665.571|5.918.826|665.626|5.918.817|
|P9|665.470|5.918.958|665.480|5.918.956|665.453|5.918.877|665.463|5.918.876|
|P10|665.630|5.918.912|665.638|5.918.911|665.621|5.918.852|665.629|5.918.851|
|P11|665.488|5.918.931|665.514|5.918.927|665.482|5.918.887|665.508|5.918.884|
|P12|665.590|5.918.909|665.614|5.918.905|665.582|5.918.860|665.607|5.918.856|
|P13|665.487|5.918.953|665.643|5.918.929|665.486|5.918.947|665.642|5.918.923|
|P14|665.560|5.918.857|665.563|5.918.857|665.553|5.918.812|665.556|5.918.811|
|P15|665.563|5.918.857|665.614|5.918.849|665.563|5.918.853|665.613|5.918.845|
|P16|665.622|5.918.920|665.625|5.918.920|665.610|5.918.850|665.614|5.918.849|
|P17|665.482|5.918.941|665.622|5.918.920|665.481|5.918.938|665.621|5.918.918|
|P18|665.481|5.918.938|665.485|5.918.938|665.477|5.918.914|665.480|5.918.913|

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**Página 30 de 72**

**6** **Resultados**

**6.1** **Caracterización Geofísica**

**6.1.1** **Topografía**

En la Figura 14, se puede observar la topografía dentro del dominio de modelación

meteorológica. En general, se observa que la mayoría del terreno varía entre los 0 y 400

m.s.n.m. El borde costero se caracteriza por tener una baja elevación que va aumentando

hacia el Este, lo que es característico de las unidades geomorfológicas que lo componen.

Específicamente la zona circundante al terreno tiene una elevación alrededor de los 0 a 20

m.s.n.m. y fluctúa en rangos pequeños de magnitud

**Figura 14. Elevación de terreno del área de estudio**

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**6.1.2** **Caracterización Meteorológica**

**Página 31 de 72**

**6.1.2.1** **Caracterización de la Velocidad y Dirección del Viento Anual y**

**Estacional**

**a.** **Dirección y velocidad de vientos predominantes anuales**

En la Figura 15 se presenta la rosa de vientos anual, construida en base a los datos

generados con el modelo WRF.

Los resultados indican que el modelo ha simulado frecuencias mayores para vientos cuyos

orígenes son la componente sur (S) y sursuroeste (SSO), representando el 17 y 31%,

respectivamente. Ambas componentes están regidas por vientos entre los 6,7 m/s y 12,9

m/s. También se observan frecuencias menores en otras componentes como suroeste (SO)

y norte (N), con un 9% en la frecuencia total sobre los vientos anuales simulados.

De esta forma, el vector resultante representa el 41% de los vientos simulados con origen

en los 217°, con lo que se espera que, en general durante el año, los vientos desplacen las

masas de aire en sentido noreste.

En la siguiente tabla se muestra la frecuencia de vientos por componente de origen

simulados por el modelo WRF.

**Tabla 8. Frecuencia de los vientos anuales, WRF.**

|Componente|Col2|Col3|Total|
|---|---|---|---|
|Norte|Norte|N|786|
|Nord noreste|Nord noreste|NNE|464|
|Noreste|Noreste|NE|128|
|Este noreste|Este noreste|ENE|48|
|Este|Este|E|36|
|Este Sureste|Este Sureste|ESE|89|
|Sureste|Sureste|SE|163|
|Sur sureste|Sur sureste|SSE|287|
|Sur|Sur|S|1513|
|Sur suroeste|Sur suroeste|SSO|2741|
|Suroeste|Suroeste|SO|746|
|Oeste suroeste|Oeste suroeste|OSO|257|
|Oeste|Oeste|O|264|
|Oeste noroeste|Oeste noroeste|ONO|290|
||~~**Concepción**~~<br>~~**Chile**~~<br>Los Pensamientos 197, San Pedro<br>de la Paz<br>(56.41)2287848<br>www.dss.cl|~~**Concepción**~~<br>~~**Chile**~~<br>Los Pensamientos 197, San Pedro<br>de la Paz<br>(56.41)2287848<br>www.dss.cl|~~**Santiago**~~<br>~~**Chile**~~<br>Av. Del Valle Sur 512, Of.304,<br>Huechuraba<br>(56.2)23494104|

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**Página 32 de 72**

|Col1|Componente|Col3|Total|Col5|
|---|---|---|---|---|
||Noroeste|NO|369|369|
||Norte noroeste|NNO|551|551|
||Sub total|Sub total|8732|8732|
||Calmas|Calmas|25|25|
||Total|Total|8757|8757|

Nota: Las filas sombreadas en celeste son las componentes que se simulan máximas frecuencias.

**Figura 15. Rosa de los Vientos Anual, WRF.**

Los resultados de la simulación meteorológica, sobre el área de estudio, han caracterizado

una zona en donde los vientos son de alta magnitud, propios de zonas costeras en donde

las condiciones de ventilación son favorables y en donde, además existiría un bajo

porcentaje de vientos calmos, es decir, aquellos inferiores a 0,5 m/s.

En este contexto, la Figura 16 muestra la frecuencia de los vientos en las distintas categorías

de velocidad, donde es evidente que son más frecuentes entre los 3,6 y 6,7 m/s,

representando el 31,5% de los vientos, siendo también son importantes los vientos entre

los 6,7 - 9,7 m/s y 9,1 - 12,9 m/s, constituyendo el 26,8 y 23,6% de los vientos simulados,

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**Página 33 de 72**

**EMISIONES “BRISAS II”**

respectivamente. Asimismo, se observa un bajo porcentaje de calmas de tan sólo el 0,3%

de los vientos y un 3,3% de vientos de magnitud mayor o igual a los 12,9 m/s.

**Figura 16. Frecuencia de los vientos**

**b.** **Dirección y velocidad de vientos predominantes en verano**

En la Figura 17, se ve la rosa de los vientos para los meses de verano, en donde se observa

que mayormente los vientos tienen origen entre las componentes sursuroeste

representando el 48% de los vientos simulados, aquellos que se originan en la componente

sur (S) y suroeste (SO) representan el 17 y 12% respectivamente. El resto de las

componentes tendría una ocurrencia menor. Como resultado, se espera que el vector

resultante tenga lugar en los 208° y que por consiguiente el desplazamiento de las masas

de aire sea hacia el nornordeste.

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**Figura 17. Rosa de los Vientos Verano, WRF**

**Página 34 de 72**

En la siguiente tabla se muestra la frecuencia de vientos por cada componente de origen,

de donde se observa la frecuencia de los vientos simulados por el modelo WRF.

**Tabla 9. Frecuencia de los vientos verano, WRF.**

|Componente|Col2|Col3|Total|
|---|---|---|---|
|Norte|Norte|N|63|
|Nord noreste|Nord noreste|NNE|51|
|Noreste|Noreste|NE|19|
|Este noreste|Este noreste|ENE|12|
|Este|Este|E|7|
|Este Sureste|Este Sureste|ESE|4|
|Sureste|Sureste|SE|9|
|Sur sureste|Sur sureste|SSE|34|
|Sur|Sur|S|374|
|Sur suroeste|Sur suroeste|SSO|1040|
|Suroeste|Suroeste|SO|261|
|Oeste suroeste|Oeste suroeste|OSO|69|
|Oeste|Oeste|O|44|
|Oeste noroeste|Oeste noroeste|ONO|36|
|Noroeste|Noroeste|NO|48|
|Norte noroeste|Norte noroeste|NNO|261|
||~~**Concepción**~~<br>~~**Chile**~~<br>Los Pensamientos 197, San Pedro<br>de la Paz<br>(56.41)2287848<br>www.dss.cl|~~**Concepción**~~<br>~~**Chile**~~<br>Los Pensamientos 197, San Pedro<br>de la Paz<br>(56.41)2287848<br>www.dss.cl|~~**Santiago**~~<br>~~**Chile**~~<br>Av. Del Valle Sur 512, Of.304,<br>Huechuraba<br>(56.2)23494104|

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**Página 35 de 72**

**EMISIONES “BRISAS II”**

|Col1|Componente|Total|Col4|
|---|---|---|---|
||Calmas|7|7|

Nota: Las filas sombreadas en celeste son las componentes que registran máximas frecuencias.

El modelo simuló vientos de magnitud superiores a los 3,6 m/s, lo cual presume condiciones

de ventilación favorable durante esta estación, sobre todo considerando que el porcentaje

de vientos calmos sólo constituye el 0,3% de los vientos simulados. Específicamente,

durante esta estación los vientos entre los 3,6-6,7; 6,7-9,1 y 9,1-12,9 m/s tendrían una

frecuencia cercana al 28%, tal como se puede ver en la siguiente figura.

**Figura 18. Frecuencia del viento en verano**

**c.** **Dirección y velocidad de vientos predominantes en otoño**

En Figura 19 se presenta la rosa de los vientos durante los meses de otoño. En ella se puede

observar que los vientos más frecuentemente simulados tendrían su origen en la

componente sursuroeste, sur y norte, con una representatividad del 22, 14 y 16%,

respectivamente. Como consecuencia de esto, el vector resultante tendría lugar en los 245°

y, por lo tanto, el desplazamiento de la masa de los vientos en esta estación sería hacia el

noreste.

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**Figura 19. Rosa de los Vientos Otoño, WRF**

**Página 36 de 72**

En la Tabla 10, se ve la frecuencia de los orígenes de los vientos en el mes de otoño simulada

por el modelo WRF.

**Tabla 10. Frecuencia de los vientos otoño, WRF.**

|Componente|Col2|Col3|Total|
|---|---|---|---|
|Norte|Norte|N|360|
|Nord noreste|Nord noreste|NNE|154|
|Noreste|Noreste|NE|45|
|Este noreste|Este noreste|ENE|14|
|Este|Este|E|13|
|Este Sureste|Este Sureste|ESE|38|
|Sureste|Sureste|SE|60|
|Sur sureste|Sur sureste|SSE|89|
|Sur|Sur|S|300|
|Sur suroeste|Sur suroeste|SSO|486|
|Suroeste|Suroeste|SO|137|
|Oeste suroeste|Oeste suroeste|OSO|49|
|Oeste|Oeste|O|80|
|Oeste noroeste|Oeste noroeste|ONO|87|
|Noroeste|Noroeste|NO|110|
||~~**Concepción**~~<br>~~**Chile**~~<br>Los Pensamientos 197, San Pedro<br>de la Paz<br>(56.41)2287848<br>www.dss.cl|~~**Concepción**~~<br>~~**Chile**~~<br>Los Pensamientos 197, San Pedro<br>de la Paz<br>(56.41)2287848<br>www.dss.cl|~~**Santiago**~~<br>~~**Chile**~~<br>Av. Del Valle Sur 512, Of.304,<br>Huechuraba<br>(56.2)23494104|

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**Página 37 de 72**

**EMISIONES “BRISAS II”**

|Col1|Componente|Col3|Total|Col5|
|---|---|---|---|---|
||Norte noroeste|NNO|178|178|
||Calmas|Calmas|8|8|

Nota: Las filas sombreadas en celeste son las componentes que registran máximas frecuencias.

En relación a la magnitud de los vientos, se observa que durante esta estación la frecuencia

de los vientos es menor para categorías superiores a los 6,7 m/s en comparación con la

estación anterior. No obstante ello, las condiciones de ventilación serían favorables ya que

el porcentaje de vientos calmos sería de apenas el 0,4% de los vientos totales, mientras

que aquellos entre los 3,6 y 6,7 m/s representarían el 33,3% de los vientos de la estación,

tal como se muestra a continuación.

**Figura 20. Frecuencia de los otoño**

**d.** **Dirección y velocidad de vientos predominantes en invierno**

En la Figura 21 se observa la rosa de los vientos simulada para el invierno por el modelo

WRF, la que en comparación con las otras estaciones tendría una participación mayor de

otras componentes de origen de viento. En efecto, se observa que los vientos provienen en

un 19% de la componente sur, un 16% del sursuroeste, 14% desde el norte y 11% desde

el nornoreste.

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**Figura 21. Rosa de los Vientos Invierno, WRF**

**Página 38 de 72**

En la siguiente tabla se muestra la frecuencia de los vientos simulados por el modelo WRF

durante los meses de invierno.

**Tabla 11. Frecuencia de los vientos invierno, WRF.**

|Componente|Col2|Total|
|---|---|---|
|Norte|N|306|
|Nord noreste|NNE|235|
|Noreste|NE|63|
|Este noreste|ENE|15|
|Este|E|14|
|Este Sureste|ESE|36|
|Sureste|SE|66|
|Sur sureste|SSE|106|
|Sur|S|419|
|Sur suroeste|SSO|362|
|Suroeste|SO|75|
|Oeste suroeste|OSO|41|
|Oeste|O|55|
|Oeste noroeste|ONO|81|
|Noroeste|NO|127|

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**Página 39 de 72**

**EMISIONES “BRISAS II”**

|Col1|Componente|Col3|Total|Col5|
|---|---|---|---|---|
||Norte noroeste|NNO|200|200|
||Calmas|Calmas|7|7|

Nota: Las filas sombreadas en celeste son las componentes que registran máximas frecuencias.

En la Figura 22, se observa la frecuencia de los vientos simulados por el modelo

meteorológico, con un bajo porcentaje de calmas, alcanzando sólo el 0,3% de los vientos

simulados en invierno. Respecto a las otras categorías de vientos, se observa que son más

frecuentes entre los 3,6 y 6,7 m/s, representando el 33,0% de los vientos totales de la

estación.

35

30

25

20

15

10

5

0

|Col1|Col2|33|Col4|Col5|Col6|
|---|---|---|---|---|---|
|||||||
||||26,5|||
|||||22,4||
||15|||||
|||||||
|||||||
|0,3|||||2,8|

Calmas 0.5-3.6 3.6-6.7 6.7-9.1 9.1-12.9 >=12.9

Frecuencia de Velocidad del Viento en Invierno

**Figura 22. Frecuencia de los invierno, año 2014**

**e.** **Dirección y velocidad de vientos predominantes en primavera**

En la Figura 23 se observa la rosa de los vientos durante la primavera simulados por el

modelo WRF. La máxima frecuencia de vientos tiene origen en la componente sursuroeste

(SSO) alcanzando los 39%, mientras que el 19% de los vientos tienen origen en el sur (S)

y el 13% de los vientos se originan en el suroeste (SO). Las otras componentes tendrían

una frecuencia considerablemente menor. Además, se puede apreciar que el componente

resultante tendría lugar en los 213°, con una representatividad del 70% de los vientos y por

consiguiente, el desplazamiento de las masas de aire sería hacia el noreste.

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**Figura 23. Rosa de los Vientos Primavera, WRF**

**Página 40 de 72**

En la siguiente tabla se muestra la frecuencia de vientos, por componente de origen,

simulados por el modelo WRF.

**Tabla 12. Frecuencia de los vientos en primavera, WRF.**

|Componente|Col2|Total|
|---|---|---|
|Norte|N|57|
|Nord noreste|NNE|24|
|Noreste|NE|1|
|Este noreste|ENE|7|
|Este|E|2|
|Este Sureste|ESE|11|
|Sureste|SE|28|
|Sur sureste|SSE|58|
|Sur|S|420|
|Sur suroeste|SSO|853|
|Suroeste|SO|273|
|Oeste suroeste|OSO|98|
|Oeste|O|85|
|Oeste noroeste|ONO|86|
|Noroeste|NO|84|

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**Página 41 de 72**

**EMISIONES “BRISAS II”**

|Col1|Componente|Col3|Total|Col5|
|---|---|---|---|---|
||Norte noroeste|NNO|94|94|
||Calmas|Calmas|3|3|

Nota: Las filas sombreadas en celeste son las componentes que registran máximas frecuencias.

Por otro lado, la rosa de los vientos demuestra que existe una prevalencia de la velocidad

de los vientos entre los 3,6 - 6,7 m/s, representando el 31,7% de la velocidad del viento

simulados por el WRF en primavera en el año 2014. También son frecuentes los vientos

entre los 6,7-9,1 m/s y los 9,1 - 12,9 m/s, con un 26,9 y 25,5% de los vientos totales

simulados para la estación. Además, tal como se ve en la Figura 24, el porcentaje de calmas

es de sólo el 0,1%.

**Figura 24. Frecuencia de los vientos en primavera**

**f.** **Perfil diario de velocidad del viento**

En la Figura 25, se observa el perfil de la velocidad del viento simulado por el modelo

meteorológico.

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**Página 42 de 72**

**EMISIONES “BRISAS II”**

**Figura 25. Perfil diario de velocidad del viento, WRF año 2014**

Los resultados evidencian que durante el verano es mayor la velocidad del viento, sobre

todo en las tardes, entre las 15 y 20 horas, en donde la velocidad es superior a 8 m/s. En

primavera la diferencia entre las velocidades mayores y menores es inferior a las simuladas

en verano, en donde las más altas son cercanas a los 8 m/s en el mismo rango de horas.

Durante los meses de otoño e invierno, la velocidad del viento es inferior a las estaciones

anteriores, de hecho, durante los meses de otoño la velocidad es incluso inferior a la media,

aunque con una tendencia similar, con velocidades mayores entre las 16 y 20 horas, donde

la velocidad excede los 6,5 m/s. Durante los meses de invierno la velocidad es más

fluctuante y no se observan momentos del día en donde el viento sea particularmente

mayor.

**6.1.2.2** **Caracterización de la Temperatura del Aire**

**g.** **Temperatura Diaria Mensual**

En la Figura 26, se presenta la temperatura media mensual simulada por el WRF para cada

mes del año modelado, además de las temperaturas máximas y mínimas.

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**Página 43 de 72**

**Figura 26. Temperatura Mensual modelo WRF 2014.**

Se observa que la temperatura promedio anual va disminuyendo paulatinamente en los

meses de otoño alcanzando las temperaturas más bajas en invierno y luego aumentar hacia

fin de año con la llegada de la primavera.

En este caso, la temperatura promedio mensual más alta fue simulada en febrero con

15,6°C, alcanzando máximas de 17,1°C y mínimas de 13,7°C. Por su parte, la temperatura

promedio mínima fue simulada en los meses agosto, julio y septiembre con temperaturas

de 11,6 y 11,8°C respectivamente. Entre estos meses la mayor amplitud térmica ocurriría

en el mes de julio, donde la mínima alcanzaría los 8,1°C y la máxima 14,3°C. No obstante,

entre todos los meses del año, la máxima amplitud térmica ocurre en el mes de junio, con

una temperatura mínima promedio de 7,7°C y máxima promedio de 15,1°C.

**h.** **Perfil Vertical de la Temperatura Mensual**

En la siguiente figura se observa el perfil vertical de la temperatura para cada mes del año.

Esta ofrece una visión de la variación de la temperatura respecto la altura, la gráfica de

estas variables entrega información sobre meses o momentos del año en donde pudieran

suscitarse episodios de inversión térmica.

La inversión térmica se relaciona estrechamente con contaminación atmosférica, pues

cuando se suscitan estos episodios, la dispersión de contaminantes disminuye y por

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**Página 44 de 72**

consiguiente, las concentraciones de contaminantes aumentan. En este caso, el modelo

WRF, no simuló episodios de inversión térmica, por lo cual se presumen condiciones

favorables para la dispersión de los contaminantes.

**Figura 27. Perfil vertical de la temperatura WRF 2014.**

**i.** **Perfil diario de la Temperatura**

La simulación del modelo meteorológico WRF, dentro del área de estudio, para temperaturas

horarias, demuestra un comportamiento similar en todas las estaciones del año. En efecto,

tal como se muestra en la Figura 28, la evolución de la temperatura diaria resulta tener una

leve disminución entre las 0 y 8 horas, a partir de entonces la temperatura aumenta hasta

alcanzar las temperaturas más altas entre los 16 y 18°C, para disminuir levemente hacia el

fin del día.

Además, se hace visible que en todas las estaciones la amplitud térmica es baja, llegando a

sólo una diferencia promedio de 0,5°C, siendo levemente mayor en primavera.

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**Página 45 de 72**

**EMISIONES “BRISAS II”**

**Figura 28. Perfil diario de temperatura, WRF 2014.**

**6.1.2.3** **Caracterización de la Precipitación**

La simulación meteorológica del modelo WRF, concluye que en el año modelado, la

precipitación en la zona de estudio alcanzó los 1.212 mm/año.

En la Figura 29, se muestra la precipitación mensual para el año, donde se observan eventos

de precipitación siendo menor en los meses de febrero y diciembre; y mayores en los meses

junio y julio, donde precipita el 51% del total anual simulado. En los meses de agosto y

septiembre precipita el 26%.

Para efectos de la modelación, la precipitación juega un rol importante en la remoción

natural de material particulado del aire, denominada deposición húmeda.

350

300

250

100

0

|Col1|Col2|Col3|Col4|Col5|327|Col7|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||293||||||
|||||||||||||
|||||||||||||
|||||123|||164|148||||
|||||||||||||
|||47|43||||||26|17||
|10|4||||||||||9|

Ene Feb Mar Abr May Jun Jul Ago Sep Oct Nov Dic

**Mes**
Precipitación

**Figura 29. Precipitación mensual, WRF 2014.**

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**Página 46 de 72**

**6.2** **Resultados de la Modelación de Dispersión de MP10 y MP2,5**

A continuación, se presentan los resultados de la modelación de las emisiones de MP10 y

MP2,5, tanto para la dispersión dentro del área de estudio, como para la evaluación de los

puntos discretos cercanos al proyecto.

**6.2.1** **Material Particulado Respirable, MP10**

En esta sección se exhibe el análisis de los resultados para el MP10 tanto como

concentración promedio anual y 24 horas.

**6.2.1.1** **Concentración Promedio Anual de MP10**

En la Figura 30, se observa la dispersión de la concentración promedio anual de MP10. Los

resultados de modelación sugieren que:

- La pluma de dispersión de MP10 simulada por el modelo abarca principalmente la zona de

emplazamiento del proyecto y parte de los terrenos contiguos a este.

- Las máximas concentraciones se encuentran cercanas al centro del proyecto,

específicamente donde se simularon los polígonos de operación del proyecto inmobiliario.

- Las concentraciones se distribuyen heterogéneamente dentro del área del proyecto, dado

que en el centro se encuentra la zona de máxima y mediana concentración, siendo la pluma

de magnitud más baja a medida que se aleja del centro.

- En todos los casos, cuando se refiere a zonas o puntos de máxima y mediana concentración

es en comparación a las obtenidas dentro de la zona de estudio, más no a que estas en sí

mismas sean altas.

- Las concentraciones modeladas van desde los 0,05 μg/m3 a los 0,74 μg/m3.

- En relación a los puntos receptores escogidos cercanos al área del proyecto, se observa

que cuatro de ellos se encuentran dentro de la pluma de dispersión.

En la Figura 31, se puede observar el mapa de isoconcentración, de donde se obtuvieron

los siguientes resultados:

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**Página 47 de 72**

- Las zonas de mayores concentraciones abarcan una superficie de 0,2 ha, con

concentraciones cercanas a los 0,63 μg/m3, ubicándose al centro del proyecto inmobiliario.

- La pluma se extiende desde la zona de máxima concentración hasta los 407 m por el norte

y 150 m por el sur, 180 m al este y 488 m al oeste, disminuyendo las concentraciones

simuladas en alrededor de un 71,43%.

- De los puntos receptores se observa que sólo uno (R1) se encuentran cercano a la zona

de mayor concentración la cual es cercana a los 0,74 μg/m3

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**Página 48 de 72**

**Figura 30. Mapa de Dispersión Promedio Anual MP10**

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**Página 49 de 72**

**Figura 31. Mapa de Isoconcentración Promedio Anual MP10**

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**6.2.1.2** **Concentración Promedio 24 horas de MP10**

**Página 50 de 72**

En la Figura 32, se presenta la dispersión de la concentración promedio 24 horas de MP10,

de donde se puede concluir que:

- Al igual que la pluma de dispersión simulada para las concentraciones promedio anual, la

pluma de dispersión como promedio de 24 horas presenta sus máximas concentraciones

dentro del área de emplazamiento del proyecto.

- La simulación de la pluma de dispersión de MP10 en su concentración promedio 24 horas

arroja resultados que van desde 0,6 a 2,9 μg/m3.

- Con base en los resultados obtenidos, existe 1 punto receptor (R1) ubicado en el intervalo

donde se registran concentraciones cuyos rango de concentración varían de 2,6 a 2,9

μg/m3.

En la Figura 33, se puede observar la dimensión de la pluma de isoconcentración, de la cual

se puede destacar lo siguiente:

- La pluma se extiende hasta los 326 m por el norte y 125 m al sur, 137 m al este y 313 m

al oeste desde la zona de mayor concentración. A estas distancias la concentración esperada

es de 0,8 μg/m3, lo que reducen en un 71,43% las concentraciones modeladas

- Se distinguen una zona de máxima concentración, cuyas superficie corresponde a 0,02 ha,

con una concentración cercana a los 2,9 μg/m3 ubicada al centro del proyecto.

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**Página 51 de 72**

**Figura 32. Mapa de Dispersión Promedio 24 horas MP10**

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**Página 52 de 72**

**Figura 33. Mapa de Isoconcentración Promedio 24 horas MP10**

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**6.2.2** **Material Particulado Fino Respirable, MP2,5**

**6.2.2.1** **Concentración Promedio Anual de MP2,5**

**Página 53 de 72**

En la Figura 34, se presenta la dispersión de la concentración promedio anual de MP2,5, de

donde, se encuentran los puntos receptores de interés, donde se puede destacar lo

siguiente:

- Al igual que la pluma de dispersión simulada para las concentraciones promedio anual

MP10, la pluma de dispersión como promedio anual de MP2,5 presenta sus máximas

concentraciones dentro del área de emplazamiento del proyecto.

- La simulación de la pluma de dispersión de MP2,5 en su concentración promedio anual

arroja resultados que van desde 0,15 a 0,68 μg/m3.

- Con base en los resultados obtenidos, existe 1 punto receptor (R1) ubicado en el intervalo

donde se registran concentraciones cuyos rango de concentración varían de 0,6 a 0,68

μg/m3.

En la Figura 35, se puede observar el mapa de isoconcentración como concentración

promedio anual de MP2,5, de donde se obtuvieron los siguientes resultados:

- Las isoconcentración modeladas abarca mayoritariamente la zona en donde se emplaza el

proyecto, extendiéndose por el norte 300 m, 115 m al sur, 121 m al este y 256 m al oeste

desde la zona de máximas concentración, lugares donde se modelaron concentraciones

cercanas 0,18 μg/m3.

- La isolínea de mayor magnitud es de 0,63 μg/m3, se ubica a dentro del área del proyecto

y comprende un área de 0,04 ha. Mientras que la isolínea de menor magnitud es de 0,18

μg/m3 la cual comprende un área de 13,32 ha.

- De los puntos receptores, sólo uno se encuentra próximo a la zona de máxima

concentración, con concentraciones cercanas a los 0,68 μg/m3.

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**Página 54 de 72**

**Figura 34. Mapa de Dispersión Promedio Anual MP2,5**

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**Página 55 de 72**

**Figura 35. Mapa de Isoconcentración Promedio Anual MP2,5**

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**6.2.2.2** **Concentración Promedio 24 horas de MP2,5**

**Página 56 de 72**

En la Figura 36, se presenta la dispersión de la concentración promedio 24 horas de MP2,5,

donde se puede concluir que:

- Al igual que la pluma de dispersión simulada para las concentraciones promedio anual, la

pluma de dispersión como promedio de 24 horas presenta sus máximas concentraciones

dentro del área de emplazamiento del proyecto.

- La simulación de la pluma de dispersión de MP2,5 en su concentración promedio 24 horas

arroja resultados que van desde 0,80 a 2,71 μg/m3.

- Con base en los resultados obtenidos, existe 1 punto receptor (R1) ubicado en el intervalo

donde se registran concentraciones cuyos rango de concentración varían de 2,28 a 2,71

μg/m3.

En la Figura 37, se puede observar la dimensión de la pluma de isoconcentración, de la cual

se puede destacar lo siguiente:

- La pluma se extiende hasta los 404 m por el norte y 146 m al sur, 175 m al este y 450 m

al oeste desde la zona de mayor concentración. A estas distancias la concentración esperada

es de 0,5 μg/m3, lo que reducen en un 80% las concentraciones modeladas. Esta zona de

mínima concentración abarca una superficie aproximada de 31,29 ha.

- Se distinguen una zona de máxima concentración, cuyas superficie corresponde a 0,06 ha,

con una concentración cercana a los 2,7 μg/m3 ubicada al centro del proyecto.

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**Página 57 de 72**

**Figura 36. Mapa de Dispersión Promedio 24 horas MP2,5**

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**Página 58 de 72**

**Figura 37. Mapa de Isoconcentración Promedio 24 horas MP2,5**

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**6.2.3** **Concentración de Contaminantes en Puntos Discretos**

**Página 59 de 72**

A continuación, se presentan las concentraciones modeladas para cada uno de los

contaminantes en los puntos receptores indicados en la Figura 11 y Figura 12, descritos en

la Tabla 6.

Los resultados de la modelación discreta de MP10 como concentración promedio anual

demostraron que en el receptor “R1” la concentración alcanzaría los 0,74 μg/m [3] seguido de

“R6” con 0,61 μg/m [3], ambos ubicados dentro del área del proyecto, siendo estas las

concentraciones más altas modeladas como promedio anual para el material particulado

respirable. En relación a los resultados obtenidos para la simulación de la concentración de

MP10 como promedio 24 horas se observa que el receptor “R1” alcanza la concentración

promedio 24 horas más alta y es de 2,96 μg/m [3], seguida por “R6” con 2,57 μg/m [3] .

Por su parte, los resultados de la modelación de MP2,5 en puntos discretos resultó ser

similar a la modelación de MP10 en términos de los puntos receptores en donde lo resultados

de la concentración fue mayor en comparación a otros puntos. Los resultados son los

esperados, puesto que se trata de la misma partícula sólo que en este caso se modela la

fracción más fina.

Así, al momento de evaluar los puntos discretos como concentración modelada promedio

anual MP2,5, el receptor “R1” resultó ser el punto discreto en donde la concentración es

mayor en comparación a los otros puntos receptores, alcanzando una magnitud de 0,68

μg/m [3], seguido de “R6” cuya concentración modelada fue de 0,56 μg/m [3] . Con respecto a la

concentración de MP2,5 como promedio 24 horas modelado, el receptor “R1”, es a aquel en

el que se espera la mayor concentración con 2,73 μg/m [3], seguido por el receptor “R6”, de

2,37 μg/m [3] respectivamente.

A continuación, en la siguiente tabla se presentan los resultados obtenidos de la modelación

discreta de la concentración promedio anual y 24 horas para MP10 y MP2,5

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFÉRICA

“DOÑA JOSEFA III”

Página 60 de 72

**Tabla 13. Concentración modelada de MP10 evaluada en puntos receptores**

|Punto<br>Receptor|Distancia al<br>Punto Emisor<br>(m)|Dirección de<br>Emplazamiento<br>respecto al punto<br>emisor|Concentración modelada de MP10<br>(μg/m3)|Col5|Concentración modelada de MP2,5<br>(μg/m3)|Col7|
|---|---|---|---|---|---|---|
|**Punto**<br>**Receptor**|**Distancia al**<br>**Punto Emisor**<br>**(m)**|**Dirección de**<br>**Emplazamiento**<br>**respecto al punto**<br>**emisor**|**Promedio Anual**|**Promedio 24**<br>**horas**|**Promedio Anual**|**Promedio 24**<br>**horas**|
|R1|0|-|0,74|2,96|0,68|2,73|
|R2|0|-|0,50|2,03|0,46|1,87|
|R3|149|OSO|0,13|0,86|0,12|0,80|
|R4|177|SE|0,03|0,35|0,03|0,33|
|R5|153|SSO|0,06|0,47|0,06|0,44|
|R6|108|NNO|0,61|2,57|0,56|2,37|
|R7|120|ENE|0,19|0,96|0,18|0,88|
|R8|226|ESE|0,03|0,29|0,02|0,27|
|R9|270|ENE|0,03|0,28|0,02|0,26|
|R10|338|E|0,02|0,21|0,02|0,20|
|R11|524|N|0,04|0,32|0,04|0,29|
|R12|642|NE|0,01|0,15|0,01|0,14|
|R13|300|NNE|0,09|0,59|0,08|0,54|
|R14|355|N|0,09|0,59|0,08|0,55|
|R15|427|NNE|0,05|0,33|0,04|0,31|
|R16|229|ENE|0,04|0,38|0,04|0,35|
|R17<br>|569<br>|NNO<br>|0,03<br>|0,26<br>|0,03<br>|0,24<br>|

Nota: Los valores sombreados en celeste son los valores más altos modelados entre los puntos receptores

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**Página 61 de 72**

**6.3** **Aporte a la Estación de Monitoreo de Representatividad Poblacional (EMRP)**

A continuación, se presentan los resultados de la concentración de MP10 y MP2,5 simuladas en

las EMRP y la proyección con la puesta en marcha del proyecto.

Para todos los efectos, se consideró como año base, las concentraciones registradas en las

EMRP para el año 2018.

**EMRP Kingston College**

En la Tabla 14, se observa el aumento de la concentración basal registrada en la EMRP Kingston

College entre enero y diciembre de 2018 para MP10 y MP2,5.

Los resultados evidencian un aumento de la condición basal de 0,05% para la concentración

promedio diario y 0,01% para la concentración promedio anual de MP10. Mientras que para

MP2,5 las concentraciones se incrementarían en 0,02% como concentración anual y en un

0,06% como concentración promedio 24 horas.

**Tabla 14. Aumento de la concentración basal en la EMRP Kingston College**

|Concentración<br>(μg/m3)|MP10|Col3|MP2,5|Col5|
|---|---|---|---|---|
|**Concentración**<br>**(μg/m3)**|**Promedio**<br>**Anual**|**Promedio 24 h**|**Promedio**<br>**Anual**|**Promedio 24 h**|
|**Registros EMRP,**<br>**Linea de base**<br>**2018**|29,62|69,00|19,24|55,80|
|**Modelada**|4,0E-05|3,7E-04|3,7E-05|3,4E-04|
|**Proyectada**|29,62|69,00|19,24|55,80|
|**Aumento**|0,01%|0,05%|0,02%|0,06%|

**Por lo cual, teniendo en cuenta que esta estación representa zonas urbanas pobladas**

**de la ciudad resulta importante destacar que se prevé un aumento no significativo**

**en la condición basal de la ciudad registrada en esta estación y, que la puesta en**

**marcha del proyecto no representa un empeoramiento sustancial de la calidad del**

**aire.**

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**Página 62 de 72**

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**7** **Análisis de Incertidumbre del Modelo**

**Página 63 de 72**

El análisis presentado a continuación corresponde a un análisis estadístico que describe la

covariación conjunta de dos variables (modeladas, observadas), con el objetivo de poder

establecer una comparación entre las distintas variables meteorológicas, tanto para la

meteorología simulada como por las observadas en las estación meteorológica. Para esto

se utiliza el coeficiente de correlación lineal de Pearson, dado que permite determinar la

dependencia o independencia entre las variables.

**7.1** **Análisis de ajuste sobre el modelo meteorológico**

La correlación de los datos se realizó entre datos observados y modelados. Los datos

observados corresponden a los registrados en la estación Coronel Norte, en línea con el

SINCA, única estación de monitoreo meteorológico con datos disponibles para el año 2014,

mismo año de simulación del modelo WRF, el cual es recomendado en la Guía para el Uso

de Modelos de Calidad del Aire que fue desarrollada por él SEA en 2012.

La correlación de los datos se determinó a través del ajuste por mínimos cuadrados, método

en el que existen dos parámetros de importancia: coeficiente de correlación de Pearson (r)

y el coeficiente de determinación (R2).

El coeficiente de correlación lineal es una medida de relación de Pearson entre dos variables

y se usa para medir el grado de relación entre ellas. El rango de valores va desde el -1 al 1

y está representado por la siguiente ecuación.

σ xy
r =
xy
σ x ∙σ y

Donde,

 - σ xy, es la covarianza entre x e y;

 - σ x, es la desviación estándar de x;

 - σ y, es la desviación estándar de y;

El coeficiente de determinación se utiliza como medida de eficiencia de la cobertura de datos

midiendo el porcentaje de variación entre las variables observadas y modeladas, es decir,

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**Página 64 de 72**

testea la capacidad predictiva del modelo e indica la proporción de la varianza de los

resultados que puede ser explicado por el modelo. Los valores del coeficiente de

determinación varían de 0 a 1, siendo este último el valor óptimo y está determinada por la

siguiente relación.

R [2] = r xy2 = σ xy
σ x ∙σ y

Donde,

 - σ xy, es la covarianza entre x e y;

 - σ x, es la desviación estándar de x;

 - σ y, es la desviación estándar de y;

Además, se presenta el análisis de tendencia de los valores modelados a estar

sobredimensionados o subdimensionados respecto de los observados, a través del percent

bias (PBIAS), el valor óptimo es 0 y su cálculo se realiza según la siguiente ecuación.

PBIAS=

~~[~~

∑ ni=1 (S i −O i )

∑ ni=1 O i

~~]~~

Donde,

 - S i, es el valor simulado;

 - O i, es el valor observado.

**7.2** **Ajuste de variables del modelo**

**Tabla 15. Resumen de valores de ajuste de variables del modelo con la estación**

**Coronel Norte.**

|Variable|Coeficiente de correlación<br>lineal (r)|Coeficiente de<br>determinación (R2)|
|---|---|---|
|Temperatura horaria|0,84|0,70|
|Velocidad del viento<br>horaria|0,45|0,20|
|Dirección del viento<br>horaria|0,02|0,0004|

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**7.2.1** **Correlación de temperaturas observada y modelada.**

**Página 65 de 72**

En la Figura 38, se observa la correlación entre la temperatura horaria observada en la

estación Coronel Norte y las simuladas por el modelo WRF.

30

25

20

15

10

5

|Col1|Col2|Col3|Col4|R2 = 0,7015|
|---|---|---|---|---|
||||||
||||||
||||||
||||||

5 10 15 20 25 30

**Temperatura (°C) WRF**
Temperatura Lineal (Temperatura)

**Figura 38. Correlación entre temperaturas observadas y temperaturas**

**modeladas**

A partir de la figura anterior se observa una correlación positiva entre las variables (r=0,84),

o sea que, existe una correlación directa entre las variables. Además, se observa que el

coeficiente de determinación es cercano a 1 (R [2] =0,70). En definitiva, el ajuste por mínimos

cuadrados de los datos observados y modelados concluye que 70% de los datos observados

en la Estación Coronel Norte para el año 2014 es simulado por el modelo WRF.

Además, se observa que el modelo simula más frecuencias de temperaturas entre los 11,8

y 14,6°C, mientras que los datos observados presentan una mayor variedad de registros de

temperatura en otras clases, tal como se muestra en la siguiente figura. Con lo anterior, se

concluye que el modelo subestima las temperaturas extremas.

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**Página 66 de 72**

33.9 ; 36.6

31.1 ; 33.9

28.4 ; 31.1

25.6 ; 28.4

22.8 ; 25.6

20.1 ; 22.8

17.3 ; 20.1

14.6 ; 17.3

11.8 ; 14.6

9 ; 11.8

6.3 ; 9

3.5 ; 6.3

0.8 ; 3.5

-2 ; 0.8

|0<br>1|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|0<br>0||||||
|4<br>0||||||
|43<br>0||||||
|161<br>0||||||
|574<br>0||||||
|8<br>0|44|||||
||162|0<br>1902||||
|||27|08||5295|
||168<br>1392|7||||
|652<br>22||||||
|253<br>0||||||
|61<br>0||||||
|1<br>0||||||

0 1000 2000 3000 4000 5000 6000

**Frecuencia**

Datos Modelados Datos Observados

**Figura 39. Comparación entre la frecuencia de temperatura de los datos**

**modelados y observados**

**7.2.2** **Correlación de velocidad del viento observada y modelada.**

En la siguiente figura se observa la velocidad del viento horaria observada en comparación

con las modeladas por el modelo WRF para el año 2014.

Es posible apreciar que existe una relación positiva entre las variables (r=0,45), y que el

coeficiente de correlación de los datos sugiere que no existe mucha correlación de los datos

(R [2] =0,2035). En este contexto, el análisis concluye que tan sólo el 20% de los datos

observados en la estación Coronel Norte se ajusta a las velocidades de viento simuladas por

el modelo WRF. En términos prácticos, se observa que existe una baja correlación entre los

datos modelados y los observados y que mientras el modelo simula condiciones en donde

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**Página 67 de 72**

**EMISIONES “BRISAS II”**

los vientos son de gran magnitud, la estación registró vientos de menor intensidad.

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|R2 = 0,2|035|
|---|---|---|---|---|---|---|---|---|---|
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||
|||||||||||

**Figura 40. Correlación entre velocidad del viento observadas y temperaturas**

**modeladas**

En efecto, tal como se muestra en la siguiente figura, el modelo tiende a sobre estimar

aquellos vientos de gran magnitud y a subestimar los vientos más calmos.

**Página 68 de 72**

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**Figura 41. Comparación entre la frecuencia de velocidad del viento de los datos**

**modelados y observados**

**7.2.3** **Correlación de dirección del viento observada y modelada**

En la siguiente figura se observa la correlación del viento entre los datos modelados y los

observados, de donde se puede concluir que no existe correlación entre ambos factores.

**Figura 42. Correlación entre la dirección del viento observadas y temperaturas**

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**Página 69 de 72**

**EMISIONES “BRISAS II”**

**modeladas**

No obstante, si bien se observa que casi no hay correlación entre la dirección de viento

horaria observada y modelada, el análisis de frecuencia demuestra que el modelo es capaz

de simular las frecuencias en las distintas componentes en un rango aceptable, pero que

aquellos en componente sur, son sobre estimados y los que nacen en el este y noreste este

son subestimadas.

NNW

WNW

W

SWW

SSW

S

SSE

SEE

E

NEE

NNE

N

|Col1|81<br>85|7<br>0|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
||585<br>478|||||||
|3|438<br>97|||||||
|31|551<br>9|||||||
|||1160<br>1089||||||
||||1741||||3585|
|3|82<br>642|||||||
|269<br>220||||||||
|91|503|||||||
|58||1020||||||
|179|609|||||||
||597<br>8|59||||||

0 500 1000 1500 2000 2500 3000 3500 4000

**Frecuencia**

Datos Modelados Datos Observados

**Figura 43. Comparación entre la frecuencia de dirección del viento de los datos**

**modelados y observados**

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**Página 70 de 72**

**8** **Conclusión**

Se estudiaron los alcances y magnitudes de las concentraciones de partículas que las

emisiones más altas generarán en el aire por el proyecto. De este modo, la simulación se

ajustó al cuarto año del proyecto inmobiliario en donde se proyecta la operación de 295

unidades habitacionales las cuales corresponden a la situación basal del proyecto “Brisas

II”, sumado a lo emitido por las unidades habitacionales del proyecto a evaluar (100 casas,

80 departamentos).

De esta forma, fueron modeladas las emisiones directas de MP10 y MP2,5 por concepto de

calefacción y transito interno, a fin de determinar las concentraciones que estos

contaminantes tendrán en la atmósfera y desde este punto de vista, evaluar el aporte a la

línea de base, además de prever posibles efectos negativos a la salud de las personas.

Tal como se abordó anteriormente en el informe, los puntos que recibirían un mayor aporte

en la concentración basal de todos los contaminantes estudiados serían los receptores “R1”

como concentración promedio anual, la cual alcanzaría los 0,74 μg/m [3] seguido de “R6” con

0,61 μg/m [3], ambos ubicados dentro del área del proyecto y siendo las más altas

concentraciones modeladas como promedio anual para el material particulado respirable.

En relación a los resultados obtenidos para la simulación de la concentración de MP10 como

promedio 24 horas se observa nuevamente que el receptor “R1” alcanza la concentración

promedio 24 horas más alta con 2,96 μg/m [3], mientras que “R6” tendría una concentración

proyectada de 2,57 μg/m [3] .

Por su parte, los resultados de la modelación de MP2,5 muestran que, como promedio anual,

el receptor “R1” alcanzaría la mayor concentración en comparación a los otros puntos

receptores, con una magnitud de 0,68 μg/m [3], seguido de “R6” cuya concentración modelada

fue de 0,56 μg/m [3] . Con respecto a la concentración de MP2,5 como promedio 24 horas

modelado, el receptor “R1”, es a aquel en que se espera la mayor concentración con 2,73

μg/m [3], seguido por el receptor “R6”, de 2,37 μg/m [3] .

El análisis de la variación de la concentración sobre la línea de base demuestra que la

ejecución del proyecto no representa un aumento significativo respecto a las

concentraciones que actualmente se registran en las estaciones de monitoreo. De hecho, se

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**Página 71 de 72**

prevé un aumento en la condición basal de 0,01% para la concentración promedio anual y

0,05% para la concentración promedio 24 horas de MP10 en la estación Kingston College.

En cuanto al incremento para el MP2,5 se predice un 0,02% como concentración anual y

0,06% como concentración promedio 24 horas.

Por otro lado, es importante considerar que la concentración en el aire de los contaminantes

puede ser influida por diversos factores, entre los cuales están la tasa de emisión, las

condiciones en que los contaminantes son liberados a la atmósfera, la topografía del

entorno, e indudablemente las condiciones meteorológicas; es decir, la dispersión y

concentración de las partículas y gases en el aire quedará determinado por las condiciones

ambientales en donde estos son liberados, como por ejemplo: gradiente de presión,

gradiente de temperatura, velocidad y dirección del vientos (los que a su vez están

influenciados por las características topográficas del lugar), entre otros. En este contexto,

la modelación de dispersión de contaminantes fue simulada usando el modelo meteorológico

WRF, el cual es recomendado por el SEIA en la Guía para el Uso de Modelos de Calidad del

Aire, y este caso en particular, entregado por el mismo organismo para este tipo de

modelaciones. El modelo meteorológico es de importancia, pues simula las condiciones que

conforman el proceso de dispersión de contaminantes, y por lo mismo es importante el

análisis de correlación entre las variables simuladas por el modelo y aquellas observadas

empíricamente.

**En conclusión, la modelación de las emisiones del proyecto tanto de material**

**particulado, MP10 y MP2,5 no representan un riesgo significativo a la salud ni**

**calidad de vida de la población según los criterios establecidos en la legislación**

**ambiental vigente. Así mismo, la proyección de la concentración en la EMRP**

**demuestra un aumento en las concentraciones basales despreciables y, por lo**

**tanto, es posible concluir que el proyecto no va en desmedro de la calidad del**

**aire de la ciudad y su área circundante.**

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES “BRISAS II”**

**Página 72 de 72**

**9** **Referencias**

Hernandez- Garces, A., J. Souto, A. Rodríguez, S. Saavera, J. Casares, 2015. Validation of

CALMET/CALPUFF models simulations around a large power plant stack, p. 51. Recuperado

el 27 de junio de 2016, desde

http://revistas.ucm.es/index.php/FITE/article/view/51192/47527.

Hernández-Garces, A., U. Jáuregui-Haga, J. González, J. Caseres-Long, S. Saavedra, F.

Guzmán-Martínez, A. Torres-Valle, 2016. Aplicaciones del modelo lagrangiano de dispersión

atmosférica CALPUFF, Ciencias de la Tierra y el Espacio, enero-junio, Vol. 17, No 1, p. 37.

ISSN 1729-3790. Recuperado el 29 de junio de 2016, desde

http://www.iga.cu/publicaciones/revista/assets/calpuffreview2.pdf.

Servicio de Evaluación Ambiental, 2012, Guía para el Uso de Modelos de Calidad del Aire en

el SEIA, p. 14-39. Recuperado el 01 de abril de 2016, desde

[http://www.sea.gob.cl/sites/default/files/migration_files/guias/Guia_uso_modelo_calidad_](http://www.sea.gob.cl/sites/default/files/migration_files/guias/Guia_uso_modelo_calidad_del_aire_seia.pdf)

del_aire_seia.pdf

Servicio de Evaluación Ambiental, 2015, Guía para la Descripción de la Calidad del Aire en

el Área de Influencia de Proyectos que Ingresan al SEIA. Recuperado el 22 de noviembre

de 2016, desde

[http://www.sea.gob.cl/sites/default/files/imce/archivos/2016/01/20/guia_calidad_del_aire.](http://www.sea.gob.cl/sites/default/files/imce/archivos/2016/01/20/guia_calidad_del_aire.pdf)

pdf.

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Valores normados para MP10 y MP2,5 en Chile.****

| Nivel | MP10 (μg/m3) | MP2.5 (μg/m3) |
| --- | --- | --- |
| **Límite anual** | 50 | 20 |
| **Limite diario** | 150 | 50 |
| **Alerta** | 195-239 | 80-109 |
| **Preemergencia** | 240-329 | 110-169 |
| **Emergencia** | 330 o mayor | 170 o mayor |

**Tabla 2.: Concentración promedio anual de MP10 Estación Kingston College****

| Año | Porcentaje de<br>datos<br>disponibles<br>(%) | Concentración<br>Promedio Anual<br>(μg/m3) | Límite normativo<br>D.S. 59/1998<br>MINSEGEPRES<br>(μg/m3) | Porcentaje de<br>excedencia de la<br>norma (%) |
| --- | --- | --- | --- | --- |
| 2013 | 99 | 35,81 | 50 | No excede |
| 2014 | 99 | 32,32 | 32,32 | No excede |
| 2015 | 79 | 38,09 | 38,09 | No excede |
| 2016 | 89 | 40,42 | 40,42 | No excede |
| 2017 | 100 | 30,32 | 30,32 | No Excede |
| 2018 | 99 | 29,62 | 29,62 | No Excede |

**Tabla 3.: Concentración promedio anual de MP2,5 Estación Kingston College****

| Año | Porcentaje de<br>datos<br>disponibles (%) | Concentración<br>Promedio Anual<br>(μg/m3) | Límite normativo<br>D.S. 12/2011 MMA<br>(μg/m3) | Porcentaje de<br>excedencia de la<br>norma (%) |
| --- | --- | --- | --- | --- |
| 2013 | 0 | - | 20 | - |
| 2014 | 0 | - | - | - |
| 2015 | 76 | 20,71 | 20,71 | 3,57 |
| 2016 | 80 | 23,69 | 23,69 | 18,46 |
| 2017 | 95 | 16,47 | 16,47 | No excede |
| 2018 | 98 | 19,24 | 19,24 | No excede |

**Tabla 4.: Coordenadas de vértices del área de estudio.****

| Vértice | Proyección: UTM, Huso 18 Sur; Datum: WGS-84 | Col3 |
| --- | --- | --- |
| **Vértice** | **Este (km)** | **Norte (km)** |
| Suroeste | 639,530 | 5.896,829 |
| Sureste | 701,530 | 5.896,829 |
| Noroeste | 639,530 | 5.958,829 |
| Noreste | 701,530 | 5.958,829 |
| Centroide | 670,530 | 5.927,829 |

**Tabla 5.: Coordenadas de la modelación CALPUFF****

| Vértice | Proyección: UTM, Huso 19 S, Datum: WGS-84 | Col3 |
| --- | --- | --- |
| **Vértice** | **Este (km)** | **Norte (km)** |
| Suroeste | 655.551 | 5.908.888 |
| Sureste | 675.551 | 5.908.888 |
| Noroeste | 655.551 | 5.928.888 |
| Noreste | 675.551 | 5.928.888 |

**Tabla 6.: Características de Receptores discretos.****

| Nombre | Coordenadas UTM, HUSO 19 S, WGS -84 | Col3 | Distancia al<br>emisor (m) | Dirección<br>desde<br>emisor |
| --- | --- | --- | --- | --- |
| **Nombre** | **Este (m)** | **Norte (m)** | **Norte (m)** | **Norte (m)** |
| R1 | 665.589 | 5.918.883 | 0 | - |
| R2 | 665.505 | 5.918.901 | 0 | - |
| R3 | 665.461 | 5.918.807 | 149 | OSO |
| R4 | 665.719 | 5.918.763 | 177 | SE |
| R5 | 665.530 | 5.918.741 | 153 | SSO |
| R6 | 665.564 | 5.918.988 | 108 | NNO |
| R7 | 665.698 | 5.918.932 | 120 | ENE |
| R8 | 665.805 | 5.918.817 | 226 | ESE |
| R9 | 665.841 | 5.918.977 | 270 | ENE |
| R10 | 665.927 | 5.918.900 | 338 | E |
| R11 | 665.651 | 5.919.404 | 524 | N |
| R12 | 666.044 | 5.919.337 | 642 | NE |
| R13 | 665.734 | 5.919.148 | 300 | NNE |
| R14 | 665.621 | 5.919.235 | 355 | N |
| R15 | 665.733 | 5.919.283 | 427 | NNE |
| R16 | 665.788 | 5.918.997 | 229 | ENE |
| R17 | 665.443 | 5.919.433 | 569 | NNO |
| EMRP Kingston<br>College | 673.817 | 5.927.247 | 11.740 | NE |

**Tabla 7.: Polígonos de Modelación****

| Polígonos | Coordenadas UTM (m) WGS - 184 Huso 18 S | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Polígonos** | **A ** | **A ** | **B ** | **B ** | **C ** | **C ** | **D ** | **D ** |
| **Polígonos** | **x ** | **y ** | **x ** | **Y ** | **x ** | **y ** | **x ** | **y ** |
| P1 | 665.499 | 5.919.090 | 665.510 | 5.919.087 | 665.475 | 5.918.966 | 665.487 | 5.918.965 |
| P2 | 665.511 | 5.919.083 | 665.636 | 5.919.062 | 665.507 | 5.919.055 | 665.632 | 5.919.035 |
| P3 | 665.658 | 5.919.060 | 665.753 | 5.919.044 | 665.653 | 5.919.032 | 665.749 | 5.919.016 |
| P4 | 665.532 | 5.919.039 | 665.618 | 5.919.024 | 665.529 | 5.919.013 | 665.613 | 5.918.999 |
| P5 | 665.659 | 5.919.019 | 665.715 | 5.919.009 | 665.654 | 5.918.991 | 665.710 | 5.918.982 |
| P6 | 665.504 | 5.919.006 | 665.709 | 5.918.971 | 665.497 | 5.918.963 | 665.701 | 5.918.931 |
| P7 | 665.451 | 5.918.867 | 665.516 | 5.918.857 | 665.448 | 5.918.846 | 665.513 | 5.918.835 |
| P8 | 665.574 | 5.918.848 | 665.629 | 5.918.839 | 665.571 | 5.918.826 | 665.626 | 5.918.817 |
| P9 | 665.470 | 5.918.958 | 665.480 | 5.918.956 | 665.453 | 5.918.877 | 665.463 | 5.918.876 |
| P10 | 665.630 | 5.918.912 | 665.638 | 5.918.911 | 665.621 | 5.918.852 | 665.629 | 5.918.851 |
| P11 | 665.488 | 5.918.931 | 665.514 | 5.918.927 | 665.482 | 5.918.887 | 665.508 | 5.918.884 |
| P12 | 665.590 | 5.918.909 | 665.614 | 5.918.905 | 665.582 | 5.918.860 | 665.607 | 5.918.856 |
| P13 | 665.487 | 5.918.953 | 665.643 | 5.918.929 | 665.486 | 5.918.947 | 665.642 | 5.918.923 |
| P14 | 665.560 | 5.918.857 | 665.563 | 5.918.857 | 665.553 | 5.918.812 | 665.556 | 5.918.811 |
| P15 | 665.563 | 5.918.857 | 665.614 | 5.918.849 | 665.563 | 5.918.853 | 665.613 | 5.918.845 |
| P16 | 665.622 | 5.918.920 | 665.625 | 5.918.920 | 665.610 | 5.918.850 | 665.614 | 5.918.849 |
| P17 | 665.482 | 5.918.941 | 665.622 | 5.918.920 | 665.481 | 5.918.938 | 665.621 | 5.918.918 |
| P18 | 665.481 | 5.918.938 | 665.485 | 5.918.938 | 665.477 | 5.918.914 | 665.480 | 5.918.913 |

**Tabla 8.: Frecuencia de los vientos anuales, WRF.****

| Componente | Col2 | Col3 | Total |
| --- | --- | --- | --- |
| Norte | Norte | N | 786 |
| Nord noreste | Nord noreste | NNE | 464 |
| Noreste | Noreste | NE | 128 |
| Este noreste | Este noreste | ENE | 48 |
| Este | Este | E | 36 |
| Este Sureste | Este Sureste | ESE | 89 |
| Sureste | Sureste | SE | 163 |
| Sur sureste | Sur sureste | SSE | 287 |
| Sur | Sur | S | 1513 |
| Sur suroeste | Sur suroeste | SSO | 2741 |
| Suroeste | Suroeste | SO | 746 |
| Oeste suroeste | Oeste suroeste | OSO | 257 |
| Oeste | Oeste | O | 264 |
| Oeste noroeste | Oeste noroeste | ONO | 290 |
|  | ~~**Concepción**~~<br>~~**Chile**~~<br>Los Pensamientos 197, San Pedro<br>de la Paz<br>(56.41)2287848<br>www.dss.cl | ~~**Concepción**~~<br>~~**Chile**~~<br>Los Pensamientos 197, San Pedro<br>de la Paz<br>(56.41)2287848<br>www.dss.cl | ~~**Santiago**~~<br>~~**Chile**~~<br>Av. Del Valle Sur 512, Of.304,<br>Huechuraba<br>(56.2)23494104 |

**Tabla 9.: Frecuencia de los vientos verano, WRF.****

| Componente | Col2 | Col3 | Total |
| --- | --- | --- | --- |
| Norte | Norte | N | 63 |
| Nord noreste | Nord noreste | NNE | 51 |
| Noreste | Noreste | NE | 19 |
| Este noreste | Este noreste | ENE | 12 |
| Este | Este | E | 7 |
| Este Sureste | Este Sureste | ESE | 4 |
| Sureste | Sureste | SE | 9 |
| Sur sureste | Sur sureste | SSE | 34 |
| Sur | Sur | S | 374 |
| Sur suroeste | Sur suroeste | SSO | 1040 |
| Suroeste | Suroeste | SO | 261 |
| Oeste suroeste | Oeste suroeste | OSO | 69 |
| Oeste | Oeste | O | 44 |
| Oeste noroeste | Oeste noroeste | ONO | 36 |
| Noroeste | Noroeste | NO | 48 |
| Norte noroeste | Norte noroeste | NNO | 261 |
|  | ~~**Concepción**~~<br>~~**Chile**~~<br>Los Pensamientos 197, San Pedro<br>de la Paz<br>(56.41)2287848<br>www.dss.cl | ~~**Concepción**~~<br>~~**Chile**~~<br>Los Pensamientos 197, San Pedro<br>de la Paz<br>(56.41)2287848<br>www.dss.cl | ~~**Santiago**~~<br>~~**Chile**~~<br>Av. Del Valle Sur 512, Of.304,<br>Huechuraba<br>(56.2)23494104 |

**Tabla 10.: Frecuencia de los vientos otoño, WRF.****

| Componente | Col2 | Col3 | Total |
| --- | --- | --- | --- |
| Norte | Norte | N | 360 |
| Nord noreste | Nord noreste | NNE | 154 |
| Noreste | Noreste | NE | 45 |
| Este noreste | Este noreste | ENE | 14 |
| Este | Este | E | 13 |
| Este Sureste | Este Sureste | ESE | 38 |
| Sureste | Sureste | SE | 60 |
| Sur sureste | Sur sureste | SSE | 89 |
| Sur | Sur | S | 300 |
| Sur suroeste | Sur suroeste | SSO | 486 |
| Suroeste | Suroeste | SO | 137 |
| Oeste suroeste | Oeste suroeste | OSO | 49 |
| Oeste | Oeste | O | 80 |
| Oeste noroeste | Oeste noroeste | ONO | 87 |
| Noroeste | Noroeste | NO | 110 |
|  | ~~**Concepción**~~<br>~~**Chile**~~<br>Los Pensamientos 197, San Pedro<br>de la Paz<br>(56.41)2287848<br>www.dss.cl | ~~**Concepción**~~<br>~~**Chile**~~<br>Los Pensamientos 197, San Pedro<br>de la Paz<br>(56.41)2287848<br>www.dss.cl | ~~**Santiago**~~<br>~~**Chile**~~<br>Av. Del Valle Sur 512, Of.304,<br>Huechuraba<br>(56.2)23494104 |

**Tabla 11.: Frecuencia de los vientos invierno, WRF.****

| Componente | Col2 | Total |
| --- | --- | --- |
| Norte | N | 306 |
| Nord noreste | NNE | 235 |
| Noreste | NE | 63 |
| Este noreste | ENE | 15 |
| Este | E | 14 |
| Este Sureste | ESE | 36 |
| Sureste | SE | 66 |
| Sur sureste | SSE | 106 |
| Sur | S | 419 |
| Sur suroeste | SSO | 362 |
| Suroeste | SO | 75 |
| Oeste suroeste | OSO | 41 |
| Oeste | O | 55 |
| Oeste noroeste | ONO | 81 |
| Noroeste | NO | 127 |

**Tabla 12.: Frecuencia de los vientos en primavera, WRF.****

| Componente | Col2 | Total |
| --- | --- | --- |
| Norte | N | 57 |
| Nord noreste | NNE | 24 |
| Noreste | NE | 1 |
| Este noreste | ENE | 7 |
| Este | E | 2 |
| Este Sureste | ESE | 11 |
| Sureste | SE | 28 |
| Sur sureste | SSE | 58 |
| Sur | S | 420 |
| Sur suroeste | SSO | 853 |
| Suroeste | SO | 273 |
| Oeste suroeste | OSO | 98 |
| Oeste | O | 85 |
| Oeste noroeste | ONO | 86 |
| Noroeste | NO | 84 |

**Tabla 13.: Concentración modelada de MP10 evaluada en puntos receptores****

| Punto<br>Receptor | Distancia al<br>Punto Emisor<br>(m) | Dirección de<br>Emplazamiento<br>respecto al punto<br>emisor | Concentración modelada de MP10<br>(μg/m3) | Col5 | Concentración modelada de MP2,5<br>(μg/m3) | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Punto**<br>**Receptor** | **Distancia al**<br>**Punto Emisor**<br>**(m)** | **Dirección de**<br>**Emplazamiento**<br>**respecto al punto**<br>**emisor** | **Promedio Anual** | **Promedio 24**<br>**horas** | **Promedio Anual** | **Promedio 24**<br>**horas** |
| R1 | 0 | - | 0,74 | 2,96 | 0,68 | 2,73 |
| R2 | 0 | - | 0,50 | 2,03 | 0,46 | 1,87 |
| R3 | 149 | OSO | 0,13 | 0,86 | 0,12 | 0,80 |
| R4 | 177 | SE | 0,03 | 0,35 | 0,03 | 0,33 |
| R5 | 153 | SSO | 0,06 | 0,47 | 0,06 | 0,44 |
| R6 | 108 | NNO | 0,61 | 2,57 | 0,56 | 2,37 |
| R7 | 120 | ENE | 0,19 | 0,96 | 0,18 | 0,88 |
| R8 | 226 | ESE | 0,03 | 0,29 | 0,02 | 0,27 |
| R9 | 270 | ENE | 0,03 | 0,28 | 0,02 | 0,26 |
| R10 | 338 | E | 0,02 | 0,21 | 0,02 | 0,20 |
| R11 | 524 | N | 0,04 | 0,32 | 0,04 | 0,29 |
| R12 | 642 | NE | 0,01 | 0,15 | 0,01 | 0,14 |
| R13 | 300 | NNE | 0,09 | 0,59 | 0,08 | 0,54 |
| R14 | 355 | N | 0,09 | 0,59 | 0,08 | 0,55 |
| R15 | 427 | NNE | 0,05 | 0,33 | 0,04 | 0,31 |
| R16 | 229 | ENE | 0,04 | 0,38 | 0,04 | 0,35 |
| R17<br> | 569<br> | NNO<br> | 0,03<br> | 0,26<br> | 0,03<br> | 0,24<br> |

**Tabla 14.: Aumento de la concentración basal en la EMRP Kingston College****

| Concentración<br>(μg/m3) | MP10 | Col3 | MP2,5 | Col5 |
| --- | --- | --- | --- | --- |
| **Concentración**<br>**(μg/m3)** | **Promedio**<br>**Anual** | **Promedio 24 h** | **Promedio**<br>**Anual** | **Promedio 24 h** |
| **Registros EMRP,**<br>**Linea de base**<br>**2018** | 29,62 | 69,00 | 19,24 | 55,80 |
| **Modelada** | 4,0E-05 | 3,7E-04 | 3,7E-05 | 3,4E-04 |
| **Proyectada** | 29,62 | 69,00 | 19,24 | 55,80 |
| **Aumento** | 0,01% | 0,05% | 0,02% | 0,06% |

**Tabla 15.: Resumen de valores de ajuste de variables del modelo con la estación****

| Variable | Coeficiente de correlación<br>lineal (r) | Coeficiente de<br>determinación (R2) |
| --- | --- | --- |
| Temperatura horaria | 0,84 | 0,70 |
| Velocidad del viento<br>horaria | 0,45 | 0,20 |
| Dirección del viento<br>horaria | 0,02 | 0,0004 |
