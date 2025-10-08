---
title: Sin título
author: dss_105
date: D:20210413110546-04'00'
language: es
type: report
pages: 65
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - MODELACIÓN DE CONTAMINANTES ATMOSFÉRICOS PROYECTO REFERENCIAL AMPLIACIÓN Y MEJORAMIENTO AEROPUERTO EL LOA DE CALAMA
-->

# MODELACIÓN DE CONTAMINANTES ATMOSFÉRICOS PROYECTO REFERENCIAL AMPLIACIÓN Y MEJORAMIENTO AEROPUERTO EL LOA DE CALAMA

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

## Tabla de contenido

Página 2 de 65

**1** **INTRODUCCIÓN ........................................................................................................... 6**

1.1 O BJETIVOS ................................................................................................................................................................... 6

**2** **ANTECEDENTES ............................................................................................................ 7**

2.1 M ARCO LEGAL REGULATORIO ........................................................................................................................................... 7

2.2 E STADO DE LA CALIDAD DEL AIRE, C ALAMA ......................................................................................................................... 8

_Análisis del cumplimiento normativo ................................................................................................................... 8_

_Concentración promedio mensual de MP_ _10_ _y MP_ _2,5_ _........................................................................................... 17_

_Ciclo de concentración diaria de MP_ _10_ _y MP_ _2,5_ _en Calama ................................................................................. 20_

**3** **METODOLOGÍA ........................................................................................................... 22**

3.1 M ODELACIÓN METEOROLÓGICA ..................................................................................................................................... 22

_Dominio de modelación meteorológica ............................................................................................................. 22_

3.2 C ARACTERIZACIÓN METEOROLÓGICA DEL MODELO WRF ..................................................................................................... 24

_Caracterización de la velocidad y dirección del viento anual y estacional ......................................................... 24_

_Caracterización de la temperatura del aire ....................................................................................................... 34_

_Caracterización de la precipitación .................................................................................................................... 36_

_Altura de capa de mezcla ................................................................................................................................... 37_

3.3 M ODELACIÓN CALPUFF .............................................................................................................................................. 38

3.4 E SCENARIOS DE MODELACIÓN ........................................................................................................................................ 40

**4** **RESULTADOS .............................................................................................................. 44**

4.1 Á REA DE I NFLUENCIA ................................................................................................................................................... 44

4.2 C ONCENTRACIONES MODELADAS .................................................................................................................................... 45

_Dispersión e isoconcentración de contaminantes .............................................................................................. 45_

_Concentración de contaminantes en puntos discretos ...................................................................................... 57_

_Aporte del Proyecto a la concentración en estaciones de cumplimiento normativo. ........................................ 58_

_Aporte sinérgico del Proyecto y Proyectos circundantes aprobados ambientalmente por el SEIA a la_

_concentración en estaciones de cumplimiento normativo. ............................................................................................. 59_

**5** **ANÁLISIS DE RESULTADOS ........................................................................................ 63**

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

**Índice de Tablas**

Página 3 de 65

Tabla 1. Valores normados para MP 10 y MP 2,5 en Chile. .................................................................................... 7

Tabla 2. Concentración promedio anual de MP 10 Estación Colegio Pedro Vergara Keller. .................................... 9

Tabla 3. Concentración promedio anual de MP 2,5 Estación Colegio Pedro Vergara Keller................................... 10

Tabla 4. Concentración promedio anual de MP 10 Estación Club Deportivo 23 de Marzo. ................................... 12

Tabla 5. Concentración promedio anual de MP 2,5 Estación Club Deportivo 23 de Marzo. ................................... 13

Tabla 6. Concentración promedio anual de MP 10 Estación Centro. .................................................................. 15

Tabla 7. Concentración promedio anual de MP 2,5 Estación Centro. .................................................................. 16

Tabla 8. Coordenadas de vértices del área de estudio. .................................................................................. 22

Tabla 9. Características de receptores discretos. ........................................................................................... 42

Tabla 10. Características de estaciones de monitoreo. ................................................................................... 42

Tabla 11. Concentraciones modeladas en puntos receptores. ......................................................................... 57

Tabla 12. Proyección de la concentración en la EMRP Colegio Pedro Vergara Keller. ........................................ 58

Tabla 13. Proyección de la concentración en la EMRP Club Deportivo 23 de Marzo. ......................................... 58

Tabla 14. Proyección de la concentración en la EMRP Centro. ........................................................................ 58

Tabla 15. Aporte a la concentración de MP Proyectos en la EMRP Colegio Pedro Vergara Keller ....................... 59

Tabla 16. Aporte a la concentración de MP Proyectos en la EMRP Club Deportivo 23 de Marzo. ....................... 60

Tabla 17. Aporte a la concentración de MP Proyectos en la EMRP Centro. ....................................................... 61

**Índice de Figuras**

Figura 1. Ubicación del Proyecto. ................................................................................................................... 6

Figura 2. Concentración promedio 24 horas de MP 10, Estación Colegio Pedro Vergara Keller. ............................. 8

Figura 3. Concentración trianual de MP 10 Estación Colegio Pedro Vergara Keller. ............................................... 9

Figura 4. Concentración promedio 24 horas de MP 2,5 Estación Colegio Pedro Vergara Keller. ............................ 10

Figura 5. Concentración promedio trianual de MP 2,5 Estación Colegio Pedro Vergara Keller. ............................. 11

Figura 6. Concentración promedio 24 horas de MP 10, Estación Club Deportivo 23 de Marzo. ............................. 11

Figura 7. Concentración trianual de MP 10 Estación Club Deportivo 23 de Marzo. .............................................. 12

Figura 8. Concentración promedio 24 horas de MP 2,5 Estación Club Deportivo 23 de Marzo. ............................. 13

Figura 9. Concentración promedio trianual de MP 2,5 Estación Club Deportivo 23 de Marzo. .............................. 14

Figura 10. Concentración promedio 24 horas de MP 10, Estación Centro. .......................................................... 14

Figura 11. Concentración trianual de MP 10 Estación Centro. ........................................................................... 15

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

Página 4 de 65

Figura 12. Concentración promedio 24 horas de MP 2,5 Estación Centro. .......................................................... 16

Figura 13. Concentración promedio trianual de MP 2,5 Estación Centro. ............................................................ 17

Figura 14. Concentración promedio mensual de MP 10 Estación Colegio Pedro Vergara Keller ............................ 18

Figura 15. Concentración promedio mensual de MP 2,5 Estación Colegio Pedro Vergara Keller ........................... 18

Figura 16. Concentración promedio mensual de MP 10 Estación Club Deportivo 23 de Marzo. ............................ 19

Figura 17. Concentración promedio mensual de MP 2,5 Estación Club Deportivo 23 de Marzo. ........................... 19

Figura 18. Concentración promedio mensual de MP 10 Estación Centro. ........................................................... 20

Figura 19. Concentración promedio mensual de MP 2,5 Estación Centro. ........................................................... 20

Figura 20. Ciclo de concentración promedio horaria de MP 10 y MP 2,5 para junio, año 2019 ................................ 21

Figura 21. Dominio del modelo meteorológico WRF. ...................................................................................... 23

Figura 22. Rosa de los vientos anual WRF, año 2018. .................................................................................... 24

Figura 23. Frecuencia de los vientos simulados para el año 2018. .................................................................. 25

Figura 24. Rosa de los vientos en verano simulado por el modelo WRF, 2018. ................................................ 26

Figura 25. Frecuencia de los vientos simulados en verano para el año 2018.................................................... 27

Figura 26. Rosa de los vientos en otoño simulado por el modelo WRF, 2018. .................................................. 28

Figura 27. Frecuencia de los vientos simulados en otoño para el año 2018. .................................................... 29

Figura 28. Rosa de los vientos en invierno simulado por el modelo WRF, 2018. .............................................. 30

Figura 29. Frecuencia de los vientos simulados en invierno para el año 2018. ................................................. 31

Figura 30. Rosa de los vientos en primavera simulado por el modelo WRF, 2018. ........................................... 32

Figura 31. Frecuencia de los vientos simulados en primavera para el año 2018. .............................................. 33

Figura 32. Perfil diario de velocidad del viento, WRF año 2018. ...................................................................... 33

Figura 33. Temperatura mensual en el WRF, año 2018. ................................................................................. 35

Figura 34. Perfil diario de temperatura WRF, año 2018. ................................................................................. 36

Figura 35. Precipitación mensual WRF, año 2018. ......................................................................................... 37

Figura 36. Evolución diaria de la altura de capa de mezcla WRF, año 2018. .................................................... 38

Figura 37. Dominio modelo CALPUFF ............................................................................................................ 40

Figura 38. Ubicación de receptores discretos................................................................................................. 41

Figura 39. Ubicación estaciones de monitoreo aledañas al Proyecto. .............................................................. 41

Figura 40. Polígonos de modelación. ............................................................................................................ 43

Figura 41. Área de influencia del Proyecto. ................................................................................................... 44

Figura 42. Mapa dispersión de MP 10 promedio anual. ..................................................................................... 46

Figura 43. Mapa de isoconcentración MP 10 concentración promedio anual. ...................................................... 47

Figura 44. Mapa dispersión de MP 10 promedio 24 horas. ................................................................................ 49

Figura 45. Mapa de isoconcentración MP 10 concentración promedio 24 horas. ................................................. 50

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

Página 5 de 65

Figura 46. Mapa dispersión MP 2,5 promedio anual. ......................................................................................... 52

Figura 47. Mapa de isoconcentración MP 2,5 promedio anual. ........................................................................... 53

Figura 48. Mapa dispersión de MP 2,5 concentración promedio 24 horas. .......................................................... 55

Figura 49. Mapa de isoconcentraciones MP 2,5 concentración promedio 24 horas. ............................................. 56

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

Página 6 de 65

**1** **Introducción**

El “Proyecto Referencial Ampliación y Mejoramiento Aeropuerto El Loa de Calama” consiste en la
remodelación y ampliación de las instalaciones que son necesarias para dar a los pasajeros, las líneas
aéreas y demás usuarios del Aeropuerto las condiciones de servicio, confort y seguridad acordes a las
de un Aeropuerto regional con carácter internacional, cumpliendo la normativa nacional e internacional
en la materia. Las obras serán ejecutadas por el Concesionario que se adjudique el tercer periodo de
Concesión. Entre las principales instalaciones a modificar o construir se encuentra el terminal de
pasajeros, las plataformas comercial y general, la pista 10/28, calles de rodaje, vialidad y
estacionamientos.

El Aeropuerto El Loa está ubicado a 5,8 km al sur este del centro de la ciudad de Calama, Comuna de
Calama, Provincia de El Loa, Región de Antofagasta, opera bajo la modalidad de concesión. El código
IATA es CJC, el código OACI es SCCF y la clave de referencia OACI es 4D. En la Figura 1 se muestra la
ubicación del Proyecto.

**Figura 1. Ubicación del Proyecto.**

Fuente: elaboración propia con base en imagen ArcGis 10.2.2.

En este informe se presenta la evaluación de la dispersión y concentración de los contaminantes
emitidos a la atmósfera dentro del área de estudio, mediante las herramientas de modelación sugeridas
por el Servicio de Evaluación Ambiental, fijados en los lineamientos establecidos en la Guía para el Uso
de Modelos de Calidad del Aire en el SEIA.

**1.1** **Objetivos**

El presente estudio, tiene como objetivo general evaluar el efecto en la atmósfera debido a las emisiones
de contaminantes por la construcción del Proyecto “Proyecto Referencial Ampliación y Mejoramiento

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

Página 7 de 65

Aeropuerto El Loa de Calama”, con el fin evaluar una posible afectación a la salud o calidad de vida de
las personas que desarrollen actividades cercanas al área del Proyecto.

Para lo anterior se plantean los siguientes objetivos específicos:

 - Evaluar el alcance de la dispersión de MP 10 y MP 2,5, con el fin de predecir zonas de máximo y bajo
impacto.

 - Evaluar la concentración de MP 10 y MP 2,5 en receptores que actualmente se encuentren cercanos
al Proyecto.

 - Evaluar la concentración de MP 10 y MP 2,5 en Estaciones de Monitoreo con Representatividad
Poblacional (EMRP) cercanas al lugar del Proyecto, por la incorporación del “Proyecto Referencial
Ampliación y Mejoramiento Aeropuerto El Loa de Calama”.

**2** **Antecedentes**

**2.1** **Marco legal regulatorio**

Actualmente, los contaminantes MP 10 y MP 2,5 están regulados bajo normas de calidad primaria, cuyo
objetivo es proteger la salud de las personas de los efectos agudos y crónicos de la exposición de estos
contaminantes con un riesgo aceptable. Para esto, se fijan límites de concentración permitidos,
condiciones de superación de la norma y los niveles que dan paso a situaciones de emergencia
ambiental.

El material particulado respirable MP 10 es regulado por el D.S. N°59/1998 del Ministerio Secretaría
General de la Presidencial y el material particulado fino respirable MP 2,5 es regulado por el D.S.
N°12/2011 del Ministerio del Medio Ambiente.

En Tabla 1 se ve una comparación entre los valores del límite anual y diario para los contaminante MP 10
y MP 2,5, además de los rangos que dan origen a situaciones de alerta, preemergencia y emergencia
ambiental.

**Tabla 1. Valores normados para MP** **10** **y MP** **2,5** **en Chile.**

|Nivel|MP (μg/m3)<br>10|MP (μg/m3)<br>2,5|
|---|---|---|
|**Límite anual**|50|20|
|**Limite diario**|150|50|
|**Alerta**|195-239|80-109|
|**Preemergencia**|240-329|110-169|
|**Emergencia**|330 o mayor|170 o mayor|

Fuente: En base a D.S. N°59/1998 MINSEGEPRES y D.S. N°12/2011 MMA.

No obstante, la superación del límite normativo no es motivo de condiciones de superación de la norma,
sino que se considera que la norma es incumplida bajo las siguientes condiciones:

 Cuando el promedio de la concentración anual de tres años consecutivos iguale o supere los 50
μg/m3.

 Si el percentil 98 (P98) de las concentraciones de 24 horas durante un año sea igual o superior
a 150 μg/m3

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

Página 8 de 65

 Si durante un año se registrasen siete o más días cuya concentración sea mayor a 150 μg/m3

En el mismo contexto, las condiciones de superación de la norma de MP 2,5 son las que se describen a
continuación:

 Cuando el promedio de la concentración anual de tres años consecutivos iguale o supere los 20
μg/m3.

 Si el percentil 98 (P98) de las de 24 horas durante un año sea igual o superior a 50 μg/m3.

**2.2** **Estado de la calidad del aire, Calama**

A continuación, se presenta el cumplimiento normativo evidenciado en las estaciones de monitoreo con
representatividad poblacional “Estación Colegio Pedro Vergara Keller”, “Estación Club Deportivo 23 de
Marzo” y “Estación Centro”, para el período 2013-2019, mediante datos rescatados del SINCA el día 4
de marzo de 2020.

**Análisis del cumplimiento normativo**

**Estación Colegio Pedro Vergara Keller:**

Tal como se puede observar en la Figura 2, la concentración promedio 24 horas evidenciada en la
estación centro no supera el límite señalado por el D.S. N°59/1998 MINSEGPRES que establece la norma
de calidad primaria para material particulado respirable MP 10, para todo el período analizado, además
se observa que de todo el período analizado aquel que presenta la mayor concentración corresponde
al 2014 cuya concentración registrada correspondió a 100 μg/m [3], siendo este valor un 33,3% inferior al
límite establecido en la normativa vigente (150 μg/m [3] ).

**Figura 2. Concentración promedio 24 horas de MP** **10** **, Estación Colegio Pedro Vergara Keller.**

160.0

140.0

120.0

100.0

80.0

60.0

40.0

20.0

0.0

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||||||||||
||||||||||||||||||||||
|99.6|99.6|99.6|100.0|100.0|100.0|90.9|90.9|90.9|||||||||||||
|||||||||||||83.1|83.1|83.1|81.0|81.0|81.0||||
||||||||||||||||||||||
||||||||||62.2|62.2|62.2|||||||67.7|67.7|67.7|
||||||||||62.2|62.2|62.2|||||||67.7|||
||||||||||||||||||||||
||||||||||||||||||||||
||||||||||||||||||||||

2013 2014 2015 2016 2017 2018 2019

Concentración 24 horas Límite Norma

Fuente: Elaboración propia en base a los datos dispuestos en el Sistema Nacional de Calidad del Aire (SINCA).

Respecto a la concentración promedio anual de MP 10, se puede observar que esta oscila entre los 40,8
y 60,1 ug/m [3], de donde se aprecia además que en los tres primeros años del periodo analizado existió
superación normativa, a continuación, en la Tabla 6 se presenta un desglose de las concentraciones
evidenciadas junto al porcentaje de disponibilidad de datos y la excedencia a la normativa vigente.

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

Página 9 de 65

**Tabla 2. Concentración promedio anual de MP** **10** **Estación Colegio Pedro Vergara Keller.**

|Año|Porcentaje de<br>datos<br>disponibles<br>(%)|Concentración<br>Promedio Anual<br>(μg/m3)|Límite normativo D.S.<br>N°59/1998<br>MINSEGPRES (μg/m3)|Porcentaje de<br>excedencia de la<br>norma (%)|
|---|---|---|---|---|
|2013|93|60,1|50|Supera|
|2014|89|59,9|59,9|Supera|
|2015|87|52,1|52,1|Supera|
|2016|90|45,9|45,9|No supera|
|2017|91|47,0|47,0|No supera|
|2018|96|49,7|49,7|No supera|
|2019|85|40,8|40,8|No supera|

Fuente: Elaboración propia en base a los datos dispuestos en el Sistema Nacional de Calidad del Aire (SINCA).

Con respecto a la concentración promedio trianual, este análisis se realizó en los períodos en donde fue
posible calcular, correspondientes a cinco períodos en donde como era de suponer no se evidencia la
superación al límite de la normativa vigente en los primeros períodos analizados.

**Figura 3. Concentración trianual de MP** **10** **Estación Colegio Pedro Vergara Keller.**

70.00

60.00

50.00

40.00

30.00

20.00

10.00

0.00

|57.34|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
||54.47|51.21|48.65|45.82|
||||||
||||||
||||||
||||||
||||||

2013-2015 2014-2016 2015-2017 2016-2018 2017-2019

Concentración Trianual Límite Norma

Fuente: Elaboración propia en base a los datos dispuestos en el Sistema Nacional de Calidad del Aire (SINCA).

Sumado a lo anterior, es importante señalar para la estación analizada y en los períodos que esta
presenta información, es decir, 2013-2019, se analizaron la existencia de situaciones de alerta,
preemergencia y emergencia ambiental de MP 10 en base a los límites establecidos en el D.S. N°59/1998
del MINSEGPRES, de dicho análisis se arrojó que para el período evaluado solo existió un día de alerta
evidenciado en el año 2017.

Con respecto a las concentraciones de MP 2,5 para la estación “Colegio Pedro Vergara Keller”, se observa
que según lo establecido en el D.S. N°12/2011 del MMA, no existe superación normativa como
concentración diaria (50 ug/m [3] ), para todo el período evaluado, tal como se puede observar en la Figura
4.

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

Página 10 de 65

**Figura 4. Concentración promedio 24 horas de MP** **2,5** **Estación Colegio Pedro Vergara Keller.**

60.0

50.0

40.0

30.0

20.0

10.0

0.0

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||31.8|25.5|||26.9||
|24.5|||16.3|23.4||22.2|
||||||||
||||||||

2013 2014 2015 2016 2017 2018 2019

Concentración Diaria Límite Norma

Fuente: Elaboración propia en base a los datos dispuestos en el Sistema Nacional de Calidad del Aire (SINCA).

Respecto a la concentración promedio anual de MP 2,5 en la estación, se puede observar que existe una
superación a la normativa actualmente vigente para todo el período caracterizado.

**Tabla 3. Concentración promedio anual de MP** **2,5** **Estación Colegio Pedro Vergara Keller.**

|Año|Porcentaje de<br>datos<br>disponibles<br>(%)|Concentración<br>Promedio Anual<br>(μg/m3)|Límite normativo D.S.<br>12/2011 MMA (μg/m3)|Porcentaje de<br>excedencia de la<br>norma (%)|
|---|---|---|---|---|
|2013|93|11,7|20|No supera|
|2014|89|11,8|11,8|No supera|
|2015|85|11,3|11,3|No supera|
|2016|90|10,4|10,4|No supera|
|2017|87|9,5|9,5|No supera|
|2018|96|12,4|12,4|No supera|
|2019|84|8,5|8,5|No supera|

Fuente: Elaboración propia en base a los datos dispuestos en el Sistema Nacional de Calidad del Aire (SINCA).

Con respecto a la concentración promedio trianual, el cálculo se realizó para 5 períodos
correspondientes a los años 2013-2015, 2014-2016, 2015-2017, 2016-2018 y 2017-2019 de los cuales
se observa que las concentraciones no superan el límite en todo el período analizado.

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

Página 11 de 65

**Figura 5. Concentración promedio trianual de MP** **2,5** **Estación Colegio Pedro Vergara Keller.**

25.0

20.0

15.0

10.0

5.0

0.0

|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
||||||
|11.6|11.2|10.4|10.8|10.1|
||||||
||||||

2013-2015 2014-2016 2015-2017 2016-2018 2017-2019

Concentracion Trianual Límite Norma

Fuente: Elaboración propia en base a los datos dispuestos en el Sistema Nacional de Calidad del Aire (SINCA).

Al igual a lo ocurrido con MP 10, se analizó el periodo revisando los días en que se presentaron episodios
de alerta, preemergencia y emergencia ambiental por concentración de MP 2,5 según lo establecido en
el D.S. N°12/20111 MMA, del cual no se obtuvieron días con tales características.

**Estación Club Deportivo 23 de marzo:**

Tal como se puede observar en la Figura 6, la concentración promedio 24 horas evidenciada en la
estación club deportivo 23 de marzo no supera el límite señalado por el D.S. N°59/1998 MINSEGPRES
que establece la norma de calidad primaria para material particulado respirable MP 10, para todo el
período analizado, además se observa que de todo el período analizado aquel que presenta la mayor
concentración corresponde al 2015 cuya concentración registrada correspondió a 72,6 μg/m [3], siendo
este valor un 52% inferior al límite establecido en la normativa vigente (150 μg/m [3] ).

**Figura 6. Concentración promedio 24 horas de MP** **10,** **Estación Club Deportivo 23 de Marzo.**

160.0

140.0

120.0

100.0

80.0

60.0

40.0

20.0

0.0

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||||||||||
||||||||||||||||||||||
||||||||||||||||||||||
|71.8|71.8|71.8|68.1|68.1|68.1|72.6|72.6|72.6|||||||||||||
||||||||||60.5|60.5|60.5|63.1|63.1|63.1|67.1|67.1|67.1|62.5|62.5|62.5|
||||||||||||||||||||||
||||||||||||||||||||||
||||||||||||||||||||||
||||||||||||||||||||||
||||||||||||||||||||||

2013 2014 2015 2016 2017 2018 2019

Concentración 24 horas Límite Norma

Fuente: Elaboración propia en base a los datos dispuestos en el Sistema Nacional de Calidad del Aire (SINCA).

Respecto a la concentración promedio anual de MP 10, se puede observar que esta oscila entre los 38,9

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

Página 12 de 65

y 47,0 ug/m [3], de donde se aprecia además que en ningún periodo analizado existió superación
normativa, a continuación, en la Tabla 4 se presenta un desglose de las concentraciones evidenciadas
junto al porcentaje de disponibilidad de datos y la excedencia a la normativa vigente.

**Tabla 4. Concentración promedio anual de MP** **10** **Estación Club Deportivo 23 de Marzo.**

|Año|Porcentaje de<br>datos<br>disponibles<br>(%)|Concentración<br>Promedio Anual<br>(μg/m3)|Límite normativo D.S.<br>N°59/1998<br>MINSEGPRES (μg/m3)|Porcentaje de<br>excedencia de la<br>norma (%)|
|---|---|---|---|---|
|2013|97|46,9|50|No supera|
|2014|97|43,3|43,3|No supera|
|2015|96|47,0|47,0|No supera|
|2016|98|42,1|42,1|No supera|
|2017|93|38,9|38,9|No supera|
|2018|90|44,4|44,4|No supera|
|2019|95|39,3|39,3|No supera|

Fuente: Elaboración propia en base a los datos dispuestos en el Sistema Nacional de Calidad del Aire (SINCA).

Con respecto a la concentración promedio trianual, este análisis se realizó en los períodos en donde fue
posible calcular, correspondientes a cinco períodos en donde como era de suponer no se evidencia la
superación al límite de la normativa vigente.

**Figura 7. Concentración trianual de MP** **10** **Estación Club Deportivo 23 de Marzo.**

60.0

50.0

40.0

30.0

20.0

10.0

0.0

|45.7|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
||44.8|42.8|43.1|41.2|
||||||
||||||
||||||
||||||

2013-2015 2014-2016 2015-2017 2016-2018 2017-2019

Concentración Trianual Límite Norma

Fuente: Elaboración propia en base a los datos dispuestos en el Sistema Nacional de Calidad del Aire (SINCA).

Sumado a lo anterior, es importante señalar para la estación, se analizaron la existencia de situaciones
de alerta, preemergencia y emergencia ambiental de MP 10 en base a los límites establecidos en el D.S.
N°59/1998 del MINSEGPRES, de dicho análisis se arrojó que para el período evaluado no existieron casos
con tales características.

Con respecto a las concentraciones de MP 2,5 para la estación “Club Deportivo 23 de Marzo”, se observa
que según lo establecido en el D.S. N°12/2011 del MMA, no existe superación normativa como
concentración diaria (50 ug/m [3] ), en todo el período evaluado, tal como se puede observar en la Figura

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

Página 13 de 65

8.

**Figura 8. Concentración promedio 24 horas de MP** **2,5** **Estación Club Deportivo 23 de Marzo.**

60.0

50.0

40.0

30.0

20.0

10.0

0.0

|45.7|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
||44.8|42.8|43.1|41.2|
||||||
||||||
||||||
||||||

2013-2015 2014-2016 2015-2017 2016-2018 2017-2019

Concentración Trianual Límite Norma

Fuente: Elaboración propia en base a los datos dispuestos en el Sistema Nacional de Calidad del Aire (SINCA).

Respecto a la concentración promedio anual de MP 2,5 en la estación, se puede observar no existe una
superación a la normativa actualmente vigente para todo el período caracterizado.

**Tabla 5. Concentración promedio anual de MP** **2,5** **Estación Club Deportivo 23 de Marzo.**

|Año|Porcentaje de<br>datos disponibles<br>(%)|Concentración<br>Promedio Anual<br>(μg/m3)|Límite normativo<br>D.S. N°12/2011 MMA<br>(μg/m3)|Porcentaje de<br>excedencia de la<br>norma (%)|
|---|---|---|---|---|
|2013|97|7,8|20|No supera|
|2014|98|8,4|8,4|No supera|
|2015|96|9,3|9,3|No supera|
|2016|99|6,8|6,8|No supera|
|2017|96|6,3|6,3|No supera|
|2018|88|10,3|10,3|No supera|
|2019|96|7,0|7,0|No supera|

Fuente: Elaboración propia en base a los datos dispuestos en el Sistema Nacional de Calidad del Aire (SINCA).

Con respecto a la concentración promedio trianual, el cálculo se realizó para 5 períodos
correspondientes a los años 2013-2015, 2014-2016, 2015-2017, 2016-2018 y 2017-2019 de los cuales
se observa que las concentraciones superan el límite en todo el período analizado.

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

Página 14 de 65

**Figura 9. Concentración promedio trianual de MP** **2,5** **Estación Club Deportivo 23 de Marzo.**

25.0

20.0

15.0

10.0

5.0

0.0

|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
||||||
|8.5|8.2||||
|||7.5|7.8|7.9|
||||||

2013-2015 2014-2016 2015-2017 2016-2018 2017-2019

Concentracion Trianual Límite Norma

Fuente: Elaboración propia en base a los datos dispuestos en el Sistema Nacional de Calidad del Aire (SINCA).

Al igual a lo ocurrido con MP 10, se analizó el periodo revisando los días en que se presentaron episodios
de alerta, preemergencia y emergencia ambiental por concentración de MP 2,5 según lo establecido en el
D.S. N°12/20111 MMA, del cual tampoco se obtuvieron días con tales características.

**Estación Centro:**

Tal como se puede observar en la Figura 10, la concentración promedio 24 horas evidenciada en la
estación centro no supera el límite señalado por el D.S. N°59/1998 MINSEGPRES que establece la norma
de calidad primaria para material particulado respirable MP 10, para todo el período analizado, además
se observa que de todo el período analizada aquel que presenta la mayor concentración corresponde
al 2013 cuya concentración registrada correspondió a 80,2 μg/m [3], siendo este valor un 47% inferior al
límite establecido en la normativa vigente (150 μg/m [3] ).

**Figura 10. Concentración promedio 24 horas de MP** **10,** **Estación Centro.**

160.0

140.0

120.0

100.0

80.0

60.0

40.0

20.0

0.0

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||||||||||
||||||||||||||||||||||
||||||||||||||||||||||
|80.2|80.2|80.2|69.5|69.5|69.5||||||||||||||||
|||||||60.0|60.0|60.0|58.7|58.7|58.7|49.0|49.0|49.0||||52.5|52.5|52.5|
||||||||||||||||||||||
||||||||||||||||47.2|47.2|47.2||||
||||||||||||||||||||||
||||||||||||||||||||||
||||||||||||||||||||||

2013 2014 2015 2016 2017 2018 2019

Concentración 24 horas Límite Norma

Fuente: Elaboración propia en base a los datos dispuestos en el Sistema Nacional de Calidad del Aire (SINCA).

Respecto a la concentración promedio anual de MP 10, se puede observar que esta oscila entre los 30,9

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

Página 15 de 65

y 47,0 ug/m [3], de donde se aprecia además que en ningún periodo analizado existió superación
normativa, a continuación, en la Tabla 6 se presenta un desglose de las concentraciones evidenciadas
junto al porcentaje de disponibilidad de datos y la excedencia a la normativa vigente.

**Tabla 6. Concentración promedio anual de MP** **10** **Estación Centro.**

|Año|Porcentaje de<br>datos<br>disponibles<br>(%)|Concentración<br>Promedio Anual<br>(μg/m3)|Límite normativo D.S.<br>N°59/1998<br>MINSEGPRES (μg/m3)|Porcentaje de<br>excedencia de la<br>norma (%)|
|---|---|---|---|---|
|2013|87|47,0|50|No supera|
|2014|93|42,0|42,0|No supera|
|2015|96|40,8|40,8|No supera|
|2016|96|38,0|38,0|No supera|
|2017|95|33,0|33,0|No supera|
|2018|91|30,9|30,9|No supera|
|2019|92|31,1|31,1|No supera|

Fuente: Elaboración propia en base a los datos dispuestos en el Sistema Nacional de Calidad del Aire (SINCA).

Con respecto a la concentración promedio trianual, este análisis se realizó en los períodos en donde fue
posible calcular, correspondientes a cinco períodos en donde como era de suponer no se evidencia la
superación al límite de la normativa vigente.

**Figura 11. Concentración trianual de MP** **10** **Estación Centro.**

60.00

50.00

40.00

30.00

20.00

10.00

0.00

|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|43.28|41.96|38.47|||
||||35.70|33.28|
||||||
||||||
||||||

2013-2015 2014-2016 2015-2017 2016-2018 2017-2019

Concentración Trianual Límite Norma

Fuente: Elaboración propia en base a los datos dispuestos en el Sistema Nacional de Calidad del Aire (SINCA).

Sumado a lo anterior, es importante señalar para la estación analizada y en los períodos que esta
presenta información, es decir, 2013-2019, se analizaron la existencia de situaciones de alerta,
preemergencia y emergencia ambiental de MP 10 en base a los límites establecidos en el D.S. N°59/1998
del MINSEGPRES, de dicho análisis se arrojó que para el período evaluado no existieron casos con tales
características.

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

Página 16 de 65

Con respecto a las concentraciones de MP 2,5 para la estación Centro, se observa que según lo establecido
en el D.S. N°12/2011 del MMA, no existe superación normativa como concentración diaria (50 ug/m [3] ),
para todo el período evaluado, tal como se puede observar en la Figura 12.

**Figura 12. Concentración promedio 24 horas de MP** **2,5** **Estación Centro.**

60.0

50.0

40.0

30.0

20.0

10.0

0.0

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|18.3|21.6||||||
|||14.7|14.5|12.7|13.9|10.1|
||||||||

2013 2014 2015 2016 2017 2018 2019

Concentración Diaria Límite Norma

Fuente: Elaboración propia en base a los datos dispuestos en el Sistema Nacional de Calidad del Aire (SINCA).

Respecto a la concentración promedio anual de MP 2,5 en estación Centro, se puede observar que existe
una superación a la normativa actualmente vigente para todo el período caracterizado.

**Tabla 7. Concentración promedio anual de MP** **2,5** **Estación Centro.**

|Año|Porcentaje de<br>datos<br>disponibles<br>(%)|Concentración<br>Promedio Anual<br>(μg/m3)|Límite normativo D.S.<br>N°12/2011 MMA<br>(μg/m3)|Porcentaje de<br>excedencia de la<br>norma (%)|
|---|---|---|---|---|
|2013|87|10,9|20|No supera|
|2014|93|9,6|9,6|No supera|
|2015|96|9,3|9,3|No supera|
|2016|98|9,2|9,2|No supera|
|2017|96|7,8|7,8|No supera|
|2018|82|7,2|7,2|No supera|
|2019|84|5,8|5,8|No supera|

Fuente: Elaboración propia en base a los datos dispuestos en el Sistema Nacional de Calidad del Aire (SINCA).

Con respecto a la concentración promedio trianual, el cálculo se realizó para 5 períodos
correspondientes a los años 2013-2015, 2014-2016, 2015-2017, 2016-2018 y 2017-2019 de los cuales
se observa que las concentraciones superan el límite en todo el período analizado.

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

Página 17 de 65

**Figura 13. Concentración promedio trianual de MP** **2,5** **Estación Centro.**

25.0

20.0

15.0

10.0

5.0

0.0

|Col1|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
||||||
|9.9|9.4|8.8|8.1||
|||||6.9|
||||||

2013-2015 2014-2016 2015-2017 2016-2018 2017-2019

Concentracion Trianual Límite Norma

Fuente: Elaboración propia en base a los datos dispuestos en el Sistema Nacional de Calidad del Aire (SINCA).

Al igual a lo ocurrido con MP 10, se analizó el periodo revisando los días en que se presentaron episodios
de alerta, preemergencia y emergencia ambiental por concentración de MP 2,5 según lo establecido en el
D.S. N°12/2011 MMA, del cual tampoco se obtuvieron días con tales características.

A través de los antecedentes anteriormente presentados, es posible afirmar que en la comuna de Calama
hay cumplimiento de las normas de calidad del aire para los contaminantes criterios MP 10 y MP 2,5 en la
estación Centro y estación Club Deportivo 23 de Marzo, ya que en el periodo estudiado (2013-2019)
esta no supera los límites normativos vigentes establecidos, en relación a la Estación Colegio Pedro
Vergara Keller este si bien evidencia superación normativa para MP 10 como concentración trianual, esta
al transcurrir los años ha disminuido manteniéndose dentro de los márgenes normativos, para el caso
de MP 2,5, la estación cumple en todo el período evaluado.

**Concentración promedio mensual de MP** **10** **y MP** **2,5**

A continuación, en la Figura 14, Figura 15, Figura 18, Figura 19, Figura 16 y Figura 17, se muestra la
concentración promedio mensual de MP 10 y MP 2,5 registrada en las estaciones

De estas figuras se observa que existe un comportamiento típico de ciudades del norte del país, es decir,
la concentración promedio mensual son similares independiente del período analizado.

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

Página 18 de 65

**Figura 14. Concentración promedio mensual de MP** **10** **Estación Colegio Pedro Vergara Keller**

Fuente: Elaboración propia en base a los datos dispuestos en el Sistema Nacional de Calidad del Aire (SINCA).

**Figura 15. Concentración promedio mensual de MP** **2,5** **Estación Colegio Pedro Vergara Keller**

Fuente: Elaboración propia en base a los datos dispuestos en el Sistema Nacional de Calidad del Aire (SINCA).

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

Página 19 de 65

**Figura 16. Concentración promedio mensual de MP** **10** **Estación Club Deportivo 23 de Marzo.**

Fuente: Elaboración propia en base a los datos dispuestos en el Sistema Nacional de Calidad del Aire (SINCA).

**Figura 17. Concentración promedio mensual de MP** **2,5** **Estación Club Deportivo 23 de Marzo.**

Fuente: Elaboración propia en base a los datos dispuestos en el Sistema Nacional de Calidad del Aire (SINCA).

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

Página 20 de 65

**Figura 18. Concentración promedio mensual de MP** **10** **Estación Centro.**

Fuente: Elaboración propia en base a los datos dispuestos en el Sistema Nacional de Calidad del Aire (SINCA).

**Figura 19. Concentración promedio mensual de MP** **2,5** **Estación Centro.**

Fuente: Elaboración propia en base a los datos dispuestos en el Sistema Nacional de Calidad del Aire (SINCA).

**Ciclo de concentración diaria de MP** **10** **y MP** **2,5** **en Calama**

En la Figura 20, se observa la evolución de la concentración horaria durante el mes de junio del año
2019, las que fueron calculadas como el promedio de las concentraciones horarias de los días para el

mes indicado en la estación analizada.

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

Página 21 de 65

**Figura 20. Ciclo de concentración promedio horaria de MP** **10** **y MP** **2,5** **para junio, año 2019**

Fuente: Elaboración propia en base a los datos dispuestos en el Sistema Nacional de Calidad del Aire (SINCA).

En la figura anterior, se observa que la máxima concentración de MP 10 y MP 2,5 se inicia a las 18:00 horas
y tiene su máximo a las 21:00 horas logrando una concentración promedio de 124,1 μg/m [3] de MP 10 y
28,5 μg/m [3] de MP 2,5 en la estación “Club Deportivo 23 de Marzo” y de 76,7 μg/m [3] de MP 10 y 20,4 μg/m [3]
de MP 2,5 en la “Estación Centro”; luego este evento, las concentraciones descienden paulatinamente
hasta las 01:00 horas. Desde esa hora y hasta las 05:00 horas la concentración de MP 10 se mantiene
relativamente constante y es desde entonces hasta las 11:00 horas en donde la concentración de
material particulado presenta un leve aumento, influenciado probablemente por la capa residual. Luego
de esto, la concentración baja y se mantiene relativamente constante hasta las 13:00 horas, hora donde
reduce su concentración hasta alrededor de las 17:00 horas, una hora más tarde la concentración de
MP 10 comienza a aumentar considerablemente, alcanzando máximas concentraciones en las horas antes
mencionadas.

Con relación a la concentración de MP 2,5, luego de que a las 1:00 horas desciende la concentración esta
se mantiene relativamente constante hasta alrededor de las 18:00 horas cuando vuelve a comenzar su

ciclo.

En relación a la estación “Colegio Pedro Vergara Keller”, tal como se observa en la Figura 20, esta
presenta un comportamiento diferente en relación a las otras estaciones, en la cual la fluctuación horaria
tiene tres peak de concentración a las 13:00, 15:00 y 19:00 horas en donde se evidencian concentraciones
horarias de 68, 65 y 58 μg/m [3] de MP 10 respectivamente, en relación al resto del tiempo la
concentraciones se mantiene relativamente constante. Respecto a las concentraciones de MP 2,5, se
evidencia que las concentraciones no presentan mayores fluctuaciones independiente de la hora en que
se analice.

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

Página 22 de 65

**3** **Metodología**

La modelación de la dispersión de material particulado se realizó de acuerdo con la siguiente
metodología.

**3.1** **Modelación meteorológica**

El modelo Weather Research and Forecasting (WRF), es un modelo numérico recomendado para la
generación de datos meteorológicos y uno de los modelos de pronóstico meteorológicos más
avanzados.

Debido a la falta de una red robusta de estaciones meteorológicas, la Guía para el Uso de Modelos de
Calidad del Aire en el SEIA recomienda el uso de WRF por sobre el uso del CALMET. Además, el mismo
documento, sugiere el uso del WRF para la modelación de dispersión de contaminantes con CALPUFF.

El modelo WRF utilizado, simula condiciones meteorológicas para el año 2018 a partir de variables que
influyen directamente sobre él.

**Dominio de modelación meteorológica**

El dominio de la modelación de WRF, se extiende por toda el área de la comuna de Calama y la zona
circundante, abarcando una vasta área de simulación meteorológica.

De esta forma el dominio de la modelación meteorológica quedó definido en una extensión de 62 x 62
km, con resolución de 1,0 km. En la Figura 21, se observa la ubicación espacial del dominio de la
modelación, cuyas coordenadas se presentan en la Tabla 8.

**Tabla 8. Coordenadas de vértices del área de estudio.**

|Vértice|Proyección: UTM, Huso 19 Sur; Datum: WGS-84|Col3|
|---|---|---|
|**Vértice**|**Este (km)**|**Norte (km)**|
|Noroeste|488560.70|7557205.96|
|Noreste|550560.70|7557205.96|
|Suroeste|488560.70|7495205.96|
|Sureste|550560.70|7495205.96|
|Centroide|519560.70|7526205.96|

Fuente: Elaboración propia con base a WRF, 2018.

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

**Figura 21. Dominio del modelo meteorológico WRF.**

Fuente: elaboración propia con base en imagen ArcGis 10.2.2.

Página 23 de 65

Por otro lado, la modelación fue realizada sobre 10 celdas de altura que van desde los 0 a los 4.000 m.
Las alturas de estas celdas consideran un amplio rango para la variación diaria de la capa de mezcla.

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

**3.2** **Caracterización meteorológica del modelo WRF**

Página 24 de 65

**Caracterización de la velocidad y dirección del viento anual y estacional**

**3.2.1.1** **Dirección y velocidad de vientos predominantes anuales**

En la Figura 22 se presenta la rosa de vientos anual, construida en base a los datos generados por el
modelo WRF para el año 2018.

**Figura 22. Rosa de los vientos anual WRF, año 2018.**

Fuente: elaboración propia con base a WRF, 2018.

La rosa de los vientos resultante da cuenta de los vientos simulados por el modelo meteorológico tienen
diversos orígenes. En efecto, el 16,62% de los vientos tienen origen en el noreste (NE), de los cuales el
13,32% corresponden a vientos de velocidad superiores a 3,6 e inferiores a 8,8 m/s.

La componente que representa el segundo origen con mayoría de vientos simulada corresponde a este
noreste (ENE) con un 12,68% del total, seguido del oeste (W), con un 12,27%.

También se observa que la pluma de dispersión no se desplazará hacia el norte ni hacia el sur
principalmente, está lo hará hacia el oriente y poniente del lugar del emplazamiento del Proyecto. El
vector resultante de la rosa de los vientos presenta su dispersión de contaminantes hacia el sur,

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

Página 25 de 65

específicamente grado 184.

**Figura 23. Frecuencia de los vientos simulados para el año 2018.**

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

Anual

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|38.2|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||
|||||||||||||||
|||||||||||**27.7**|**27.7**|**27.7**||
|||||||||||||||
|||||||||||||||
|||||**18.2**|**18.2**|**18.2**||||||||
||**12.4**|**12.4**|**12.4**|||||||||||
||**12.4**|**12.4**|**12.4**|||||||||||
|||||||||||||||
|||||||||||||||
||||||||||||||**2.8**|
|**0.8**||||||||||||||

Calmos 0,5-2,1 2,1-3,6 3,6-5,7 >=5,7 >=8,8

**Velocidad de viento (m/s)**

Fuente: elaboración propia con base a WRF, 2018.

Tal como se observa en la Figura 23, la mayor frecuencia de los vientos corresponde a aquellos que son
superiores a 3,6 m/s e inferiores a 5,7 m/s, representando el 38,2% de los vientos simulados por el
modelo. El 27,7% de los vientos son mayores o iguales a 5,7 m/s. Los vientos calmos, es decir, aquellos
inferiores a 0,5 m/s son los de menor proporción, representando sólo el 0,8% de los vientos simulados.

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

**3.2.1.2** **Dirección y velocidad de vientos predominantes verano**

Página 26 de 65

A continuación, se presenta la rosa de los vientos simulada para la estación de verano en el año 2018.

**Figura 24. Rosa de los vientos en verano simulado por el modelo WRF, 2018.**

Fuente: elaboración propia con base a WRF, 2018.

Tal como se ve en la Figura 24, la modelación meteorológica sugiere que en los meses de verano los
vientos tienen una predominancia en sus orígenes en la componente oeste (W) representando el 15,05%
de los vientos de la estación, de ellos el 8,29% corresponde a vientos mayores a 3,6 m/s y menores a
5,7 m/s. El 13,70% de los vientos simulados durante el verano tendrían origen en la componente oeste
suroeste (WSW), influenciados principalmente por vientos que no superan los 8,8 m/s, en efecto, el total
de los datos para esta componente son inferiores al valor mencionado. Seguido de los vientos de origen
en el noreste (NE) que representan el 10,69% de los vientos simulados por el modelo.

De la Figura 24, también es posible apreciar que la frecuencia de los vientos en sentido norte y sur es
muy baja y que por lo tanto se espera que la dispersión de contaminantes no tendrá lugar hacia esos
sectores. Por consiguiente, se puede predecir que durante los meses de verano el desplazamiento de
las masas de aire será principalmente hacia el oriente y su vector resultante se encontraría en el grado
114 correspondiente a la componente este sureste (ESE).

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

Página 27 de 65

**Figura 25. Frecuencia de los vientos simulados en verano para el año 2018.**

45

40

35

30

25

20

15

10

Verano

5

0

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|37.5|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
||**18.8**|**18.8**|**18.8**|**21.2**|**21.2**|**21.2**||||**20.4**|**20.4**|**20.4**||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|||||||||||||||
|**1.2**|||||||||||||**1**|

Calmos 0,5-2,1 2,1-3,6 3,6-5,7 5,7-8,8 >=8,8

**Velocidad de viento (m/s)**

Fuente: elaboración propia con base a WRF, 2018.

Tal como se observa en la Figura 25, la mayor frecuencia de los vientos corresponde a aquellos que son
superiores a 3,6 m/s e inferiores a 5,7 m/s, representando el 37,5% de los vientos simulados por el
modelo. El 21,2% de los vientos son mayores a 2,1 m/s y menores a 3,6 m/s. Los vientos calmos, es decir,
aquellos inferiores a 0,5 m/s son los de menor proporción, representando sólo el 1,2% de los vientos
simulados.

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

**3.2.1.3** **Dirección y velocidad de vientos predominantes otoño**

Página 28 de 65

A continuación, se presenta la rosa de los vientos simulada para la estación de otoño en el año 2018.

**Figura 26. Rosa de los vientos en otoño simulado por el modelo WRF, 2018.**

Fuente: elaboración propia con base a WRF, 2018.

En la Figura 26, se observa la rosa de los vientos simulados durante el otoño. Los resultados concluyen
que el 21,01% de los vientos tiene origen en el noreste (NE), siendo predominantes aquellos de
velocidades mayores a 3,6 m/s y menores a 5,7 m/s, representando el 9,34% de los vientos en esta
componente. Los vientos en la componente este noreste (ENE), representan el 14,01% de los vientos
totales simulados durante el otoño, siendo prevalentes los vientos entre los 3,6 m/s y 5,70 m/s.

En general, se observa que la velocidad promedio simulada para la velocidad de viento en otoño es de
4,57 m/s. Los vientos tienen múltiples orígenes prevaleciendo aquellos que tienen lugar entre las
componentes noreste (NE) y estenoreste (ENE). En consecuencia, se puede concluir que las masas de
aire serán desplazadas hacia el sur suroeste (SSW).

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

Página 29 de 65

**Figura 27. Frecuencia de los vientos simulados en otoño para el año 2018.**

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

Otoño

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|40.7|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||
|||||||||||||||
|||||||||||**26.5**|**26.5**|**26.5**||
|||||||||||**26.5**||||
|||||**19**|**19**|**19**||||||||
|||||||||||||||
||**10.3**|**10.3**|**10.3**|||||||||||
||||||||||||||**2.4**|
|**1.1**||||||||||||||

Calmos 0,5-2,1 2,1-3,6 3,6-5,7 5,7-8,8 >=8,8

**Velocidad de viento (m/s)**

Fuente: elaboración propia con base a WRF, 2018.

Tal como se observa en la Figura 27, la mayor frecuencia de los vientos durante el otoño corresponde a
aquellos que son superiores a 3,6 m/s e inferiores a 5,7 m/s, representando el 40,7% de los vientos
simulados por el modelo. El 26,5% de los vientos son mayores a 5,7 m/s y menores a 8,8 m/s. Los vientos
calmos, es decir, aquellos inferiores a 0,5 m/s son los de menor proporción, representando sólo el 1,1%
de los vientos simulados.

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

**3.2.1.4** **Dirección y velocidad de vientos predominantes invierno**

Página 30 de 65

A continuación, se presenta la rosa de los vientos simulada para la estación de invierno en el año 2018.

**Figura 28. Rosa de los vientos en invierno simulado por el modelo WRF, 2018.**

Fuente: elaboración propia con base a WRF, 2018.

La rosa de los vientos durante los meses de invierno, visible en la Figura 28, siguiere que los vientos
tendrán múltiples orígenes. En efecto, los resultados indican que la mayoría de los vientos provienen
desde el noreste (NE) con un 21,60% del total y del este noreste (ENE) representando un 13,26% del
total. De los vientos de origen en estas componentes, la mayoría de estos van desde los 5,70 m/s hasta
los 8,80 m/s. En consecuencia, de esto, la dispersión de contaminantes será desplazada hacia el sur
suroeste (SSW), ya que el vector resultante se encuentra ubicado en el grado 197.

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

Página 31 de 65

**Figura 29. Frecuencia de los vientos simulados en invierno para el año 2018.**

40

35

30

25

20

15

10

5

0

Invierno

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|35.6|Col9|Col10|34.1|Col12|Col13|Col14|Col15|Col16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||
|||||||||||||||||
|||||||||||||||||
|||||**14.3**|**14.3**|**14.3**||||||||||
||**8.9**|**8.9**|**8.9**|||||||||||||
||||||||||||||**6.7**|**6.7**|**6.7**|
|||||||||||||||||
|||||||||||||||||
|**0.3**||||||||||||||||

Calmos 0,5-2,1 2,1-3,6 3,6-5,7 5,7-8,8 >=8,8

**Velocidad de viento (m/s)**

Fuente: elaboración propia con base a WRF, 2018.

Tal como se observa en la Figura 29, la mayor frecuencia de los vientos durante el invierno corresponde
a aquellos que son superiores a 3,6 m/s e inferiores a 5,7 m/s, representando el 35,6% de los vientos
simulados por el modelo. El 34,1% de los vientos son mayores a 5,7 m/s y menores a 8,8 m/s. Los vientos
calmos, es decir, aquellos inferiores a 0,5 m/s son casi despreciables, representando sólo el 0,3% de los
vientos simulados.

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

**3.2.1.5** **Dirección y velocidad de vientos predominantes primavera**

Página 32 de 65

A continuación, se presenta la rosa de los vientos simulada para la estación de primavera en el año 2018.

**Figura 30. Rosa de los vientos en primavera simulado por el modelo WRF, 2018.**

Fuente: elaboración propia con base a WRF, 2018.

De la Figura 30, se puede observar la rosa de los vientos durante la primavera simulados por el modelo
WRF. Las máximas frecuencias de vientos tienen origen en el componente oeste (O) representando el
15,48% de los vientos en primavera, de ellos el 8,37% corresponde a aquellos de magnitud superior a
3,6 m/s e inferior a 5,7 m/s. En segundo lugar, se presenta un comportamiento de vientos provenientes
desde el este noreste (ENE) con un 13,85% del total y desde el noreste (NE) con una representatividad
del 13,08%, donde los vientos provenientes en estas direcciones abundan en velocidades que van desde
los 3,60 m/s a los 5,70 m/s. En consecuencia, de lo anterior los vientos propiciarán que los contaminantes
se desplacen en dirección sur (S), específicamente en el grado 171.

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

Página 33 de 65

**Figura 31. Frecuencia de los vientos simulados en primavera para el año 2018.**

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|38.9|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||
|||||||||||||||
|||||||||||**29.6**|**29.6**|**29.6**||
|||||||||||||||
|||||**18.4**|**18.4**|**18.4**||||||||
|||||||||||||||
|||||||||||||||
||**11.6**|**11.6**|**11.6**|||||||||||
||**11.6**|||||||||||||
|||||||||||||||
|**0.6**|||||||||||||**0.9**|

Fuente: elaboración propia con base a WRF, 2018.

Tal como se observa en la Figura 31, la mayor frecuencia de los vientos durante la primavera
corresponde a aquellos que son superiores a 3,6 m/s e inferiores a 5,7 m/s, representando el 38,9% de
los vientos simulados por el modelo. El 29,6% de los vientos son mayores a 5,7 m/s y menores a 8,8 m/s.
Los vientos calmos, es decir, aquellos inferiores a 0,5 m/s son casi despreciables, representando sólo el
0,6% de los vientos simulados.

**3.2.1.6** **Perfil diario de velocidad del viento**

En la Figura 32, se observa el perfil diario de la velocidad del viento simulado por el modelo
meteorológico.

**Figura 32. Perfil diario de velocidad del viento, WRF año 2018.**

Fuente: elaboración propia con base a WRF, 2018.

En general se observa que la velocidad del viento modelada desde las 0 horas hasta las 7 de la
madrugada presenta valores estables para cada estación, mientras que en las horas 8 y 9 desciende,

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

Página 34 de 65

alcanzando la velocidad mínima a eso de las 8 horas durante los meses de verano. Desde entonces la
velocidad del viento asciende rápidamente desde las 13 hasta las 16 horas aproximadamente.
Finalmente, a partir de las 17 horas la velocidad del viento disminuye hasta las 21 horas donde aumenta
levemente hacia el final del día.

En la Figura 32, se observa que los meses de invierno y primavera tienen un comportamiento similar,
sin embargo, en primavera la magnitud del viento es mayor que en los meses de verano durante las 10
a 18 horas, mientras que la velocidad del viento en invierno es mayor que en primavera para las 1 a 9
horas, y vuelve a presentar este comportamiento durante las 19 a 23 horas. En efecto, la velocidad
máxima en primavera alcanza los 6,1 m/s a las 14 horas, en tanto que, en invierno, la máxima velocidad
de viento ocurre a las 7 horas alcanzando una magnitud de 6,1 m/s, al igual que durante la primavera;
las velocidades mínimas en primavera ocurren a las 19 horas alcanzando una magnitud de 2,7 m/s en
promedio, mientras que en invierno la velocidad mínima alcanza los 3,2 m/s a las 19 horas del día.

Durante el invierno la velocidad promedio del viento es mayor a la velocidad promedio de las demás
estaciones. De hecho, la velocidad promedio para el invierno alcanza los 5,1 m/s, mientras que las
velocidades promedio de las otras estaciones llegan a los 4,1m/s 4,2m/s y 4,9 m/s para el verano, otoño
y primavera respectivamente. Es así como durante el invierno, logra su máximo (6,1 m/s) a las 7 horas,
mientras que la mínima ocurre a las 19 horas alcanzando los 3,2 m/s. Además, tal como se observa en
la Figura 32, la magnitud de la velocidad promedio del viento durante el invierno y la primavera se
mantienen sobre la media anual.

Por el contrario, en el verano la velocidad del viento es menor generalmente que en todas las otras
estaciones. En efecto, las máximas velocidades llegan a los 6,1 m/s a las entre las 14 y 16 horas, mientras
que la mínima alcanza los 2,1 m/s a las 20 horas.

**Caracterización de la temperatura del aire**

**3.2.2.1** **Temperatura diaria mensual**

Tal como se ve en la Figura 33, la simulación del modelo meteorológico (WRF) sugiere que la
temperatura promedio mensual disminuye en los meses de otoño e invierno y aumenta en los meses
más cálidos durante la época estival.

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

Página 35 de 65

**Figura 33. Temperatura mensual en el WRF, año 2018.**

30.0

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||
||Ene|Feb|Mar|Abr|May|Jun|Jul|Jul|Jul|Ago|Sept|Oct|Nov|Dic|
|Temp prom|14.7|14.1|14.2|14.5|14.1|12.1|12.6|12.6|12.6|13.6|14.5|14.6|15.3|15.9|
|Temp max|21.8|21.6|23.1|22.5|22.0|18.6|18.2|18.2|18.2|21.7|24.4|21.9|22.1|23.9|
|Temp min|7.8|8.6|7.8|7.3|6.4|6.3|5.7|5.7|5.7|3.6|6.6|7.5|8.5|7.3|

Temp prom Temp max Temp min

Fuente: elaboración propia con base a WRF, 2018.

Las mínimas temperaturas fueron simuladas durante el mes de junio, las que en promedio alcanzaban
magnitudes de 12,1°C en promedio. Durante este mes la amplitud térmica llega a los 12,3°C, siendo la
amplitud más baja del total, llegando a máximas de 18,6°C y mínimas de 6,3°C.

La temperatura media máxima en el año fue simulada en el mes de diciembre alcanzando los 15,9°C,
con una amplitud térmica de 16,6°C. Otros meses cálidos fueron noviembre y enero, cuya media
mensual se encuentra aproximada a los 15°C.

Cabe mencionar que las temperaturas promedio anuales simuladas registró para los meses de febrero
y mayo, valores iguales equivalentes a 14,1°C. A pesar de esto, sus amplitudes térmicas son distintas, las
cuales corresponden a 13,0°C y 15,6°C respectivamente, lo que indica que para el mes de mayo sus
temperaturas fluctúan un poco más.

**3.2.2.2** **Perfil diario de la Temperatura**

La simulación del modelo meteorológico WRF dentro del área de estudio de las temperaturas horarias,
demuestran un comportamiento similar en todas las estaciones del año. En efecto, tal como se muestra
en la Figura 34, la evolución de la temperatura diaria resulta tener una leve diminución entre las 0 y 7
horas, a partir de entonces la temperatura aumenta hasta alcanzar temperaturas máximas entre las 15 y
16 horas, luego la temperatura disminuye constantemente hasta las 23 horas.

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

Página 36 de 65

**Figura 34. Perfil diario de temperatura WRF, año 2018.**

Fuente: elaboración propia con base a WRF, 2018.

Además, se hace visible que en los meses de verano y primavera la amplitud térmica diaria es
equivalente, llegando a una diferencia de 6,8°C entre la mínima y máxima promedio horario para ambas
estaciones. Durante los meses de otoño e invierno la amplitud térmica es menor siendo de 5,2°C y 4,8°C,
respectivamente, en donde es posible observar que durante el mes de invierno se registra la menor
amplitud térmica del año simulado.

Cabe destacar que, durante los meses de otoño se observa un ajuste al perfil de la variación térmica
media anual. Contrariamente, durante los meses de verano el perfil es muy superior a la media anual,
en tanto que la temperatura en inverno es evidentemente inferior.

**Caracterización de la precipitación**

Según los resultados de la simulación meteorológica del modelo WRF, concluyen que, en el año 2018,
la precipitación en la zona de estudio alcanzó los 108,6 mm/año.

En la Figura 35, se muestra la precipitación mensual para el año 2018, de donde se concluye que los
meses de mayor precipitación corresponden a los meses de febrero, marzo y julio, en donde precipita
el 85,9% del total anual simulado para el año 2018. Además, la modelación meteorológica concluye que
la precipitación no es importante en los meses enero, abril, mayo, junio, septiembre, octubre, noviembre
y diciembre, de hecho, en los últimos cuatro meses y para el mes de abril la precipitación resultó ser
nula.

Página 37 de 65

70.0

60.0

50.0

40.0

30.0

20.0

10.0

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

**Figura 35. Precipitación mensual WRF, año 2018.**

0.0

|Col1|61.5|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||**61.5**|||||||||||||||||||
|||||||||||||||||||||
|||||||||||||||||||||
|||||||||||||||||||||
|||||**15.7**|**15.7**|**15.7**||||**16.1**|**16.1**|**16.1**||||||||
||||||||||||||**13.7**|**13.7**|**13.7**|||||
|||||||||||||||||||||
|||||||||||||||||||||
|**0.8**|||||||**0.0**|**0.5**|**0.3**|||||||**0.0**|**0.0**|**0.0**|**0.0**|

Ene Feb Mar Abr May Jun Jul Ago Sep Oct Nov Dic

Fuente: elaboración propia con base a WRF, 2018.

Para efectos de la modelación, la precipitación juega un rol importante en la remoción de material
particulado en el aire, representando un medio de remoción natural denominado deposición húmeda.

**Altura de capa de mezcla**

La altura de la capa mezcla es de importancia, pues es un parámetro básico de la modelación de
dispersión de contaminantes, ya que es ahí donde tiene lugar el transporte turbulento de masas y
energía, constituyendo un parámetro que caracteriza la troposfera baja.

El modelo WRF, es capaz de simular la altura de capa de mezcla, de hecho, tal como se observa en la
Figura 36, la evolución de la capa de mezcla diaria tiene un patrón similar en todas las estaciones del
año. En general, se pude observar que durante la noche y madrugada la altura de capa de mezcla es
menor a la simulada durante el día, esto significa que es durante el día, en donde se propician mejores
condiciones para la dispersión de contaminantes.

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

Página 38 de 65

**Figura 36. Evolución diaria de la altura de capa de mezcla WRF, año 2018.**

Fuente: elaboración propia con base a WRF, 2018.

Los resultados son los esperados, pues se espera que la capa de mezcla sea más estable durante las
noches, debido a la ausencia de aporte energético del sol, influyendo en el intercambio vertical entre
distintos niveles desfavorablemente, de este modo, la agitación turbulenta es muy reducida.

Con la salida del sol, el calentamiento de la superficie terrestre es transmitido a la atmósfera,
produciendo agitación en la capa de mezcla lo que provoca un incremento en el espesor del volumen
del aire afectado por el calentamiento del suelo, llegando al máximo entre las 15 y 17 horas del día, es
en este momento del día en donde se propician las condiciones de máxima inestabilidad atmosférica,
favoreciendo la dispersión de contaminantes.

**3.3** **Modelación CALPUFF**

La modelación de dispersión atmosférica de contaminantes provenientes del Proyecto se realizó con un
modelo tipo “Puff”, específicamente el modelo CALPUFF.

Tal como lo define la Guía, los modelos tipo “puff” son una combinación entre los modelos Gaussianos
y los modelos Lagrangeanos, en el sentido de que esencialmente calculan la dispersión de
contaminantes provenientes de una emisión instantánea, llamada “puff”, a lo largo de una trayectoria.
Su aproximación matemática consiste en estimar la dispersión en forma Gaussiana en cada punto de
una trayectoria; es decir, los modelos tipo “puff” sólo requieren una trayectoria por “puff”, lo que hace
su cálculo mucho más rápido. En el caso de emisiones continuas, se simulan las trayectorias y la
dispersión Gaussiana de muchos “puffs”. Al respecto, el modelo tipo “puff” recomendado por la Guía es
el modelo CALPUFF.

Así mismo, es un modelo completo que incorpora herramientas para procesar datos meteorológicos y
geofísicos, modelos de dispersión y pos procesamiento. Dicho modelo es recomendado por la Agencia
de Protección Ambiental de los Estados Unidos (EPA) para modelar transporte a larga distancia de
contaminantes.

CALPUFF se compone de tres módulos:

CALMET: Es un modelo meteorológico que desarrolla campos horarios de viento y temperatura
en una grilla de tres dimensiones. También asocia campos en dos dimensiones de altura y usos de suelo.

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

Este módulo puede ser reemplazado por un WRF.

**e** **[e]**

**e**

Página 39 de 65

**e** **[e]**

**e**

CALPUFF: Es un modelo de transporte y dispersión emitido desde fuentes modeladas, simulando
procesos de dispersión y transformación. CALPUFF utiliza los datos generados por CALMET. Los archivos
de salida de CALPUFF contienen las concentraciones horarias o deposición por hora de flujos evaluados
en receptores seleccionados.

CALPOST: Es usado para procesar aquellos archivos generados por CALMET y CALPUFF,
produciendo tabulaciones que resumen los resultados de la simulación.

Ecuación del modelo CALPUFF

La ecuación básica que utiliza el modelo para realizar la modelación es la siguiente:

**e** **[e]**

**e**

**e** **[e]**

[−dd] 2σσ yy [2][cc2] [቉]

**e**

QQ
CC= **e** **[e]**
2ππσσ xx σσ yy

2
gg= **e**
(2ππ) [1 2] ⁄ σσ zz

gg e **e** ee **[e]**
~~ቈ~~ [−dd] 2σσ xx [2][aa2]

**e**

**e** **[e]**

**e**

nn=−∞

**e**

[−dd] 2σσ xx [2][aa2] ~~[቉]~~ [e] **[e]** [ee] ~~[ቈ]~~ [−dd] 2σσ yy [2][cc2]

**e**

**e** **[e]**

∞

**e**

**e** **[e]**

**e**
෍e eeቈ [−] [(HH] [ee] 2σσ [+ 2nnh)] zz [2] [2]

**e** **[e]**

[+ 2nnh)] [2]
**e**

2σσ zz [2] ቉

**e** **[e]**

**e**

Dónde:

C, es concentración a nivel del suelo (g/m [3] ),

Q, es masa de contaminantes (g) en la nube.

σx, es desviación estándar (m) de la distribución de Gauss en el viento a lo largo de la dirección.

σy, es desviación estándar (m) de la distribución de Gauss en el viento de costado

σz, es desviación estándar (m) de la distribución de Gauss en la dirección vertical.

da, es distancia (m) del centro de la nube al receptor en la dirección del viento a lo largo.

dc, es distancia (m) del centro de la nube al receptor en la dirección de viento cruzado.

g, es el término vertical (m) de la ecuación Gaussiana.

H, es la altura afectiva (m) desde el nivel del suelo del hojaldre.

h, es la altura de la capa de mezcla.

Considerando las características del terreno, las distintas unidades geomorfológicas del área de
influencia del Proyecto y el dominio de la modelación se consideró utilizar el modelo CALPUFF para
simular la dispersión de los contaminantes.

El dominio de la modelación de CALPUFF se extiende en un área de 31 x 31 km, la cual abarca zonas
circundantes al área del Proyecto y la comuna de Calama. A continuación, se presenta en la siguiente
figura.

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

**Figura 37. Dominio modelo CALPUFF**

Fuente: elaboración propia con base en imagen ArcGis 10.2.2.

**3.4** **Escenarios de modelación**

Página 40 de 65

Para analizar los resultados de la modelación de dispersión de contaminantes, se realizaron mapas de
iso-concentración de las emisiones generadas por la construcción del Proyecto. Dichos mapas
permitieron evaluar los niveles de concentración, en toda el área de estudio.

Por otro lado, con el fin de analizar el impacto en la calidad del aire en receptores específicos, se realizó
una modelación discreta a los cuales se le sumaron diferentes estaciones de monitoreo con
representatividad poblacional, para obtener la concentración en el aire de puntos y alturas
seleccionadas del área de estudio.

A continuación, se presenta en las siguientes figuras la ubicación y coordenadas de los receptores
discretos y las estaciones de monitoreo utilizados en la modelación.

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

**Figura 38. Ubicación de receptores discretos.**

Página 41 de 65

Fuente: elaboración propia con base en imagen ArcGis 10.2.2.
**Figura 39. Ubicación estaciones de monitoreo aledañas al Proyecto.**

Fuente: elaboración propia con base en imagen ArcGis 10.2.2.

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

Página 42 de 65

En la siguiente tabla se presentan las coordenadas UTM de los puntos receptores.

**Tabla 9. Características de receptores discretos.**

|Receptor<br>N°|UTM, Huso 19 S, WGS-<br>84|Col3|Descripción|Distancia al<br>Proyecto<br>(m)|
|---|---|---|---|---|
|**Receptor**<br>**N°**|**Este (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|
|R1|508.810|7.513.502|Viviendas cercanas|1.278|
|R2|508.166|7.512.663|7.512.663|620|
|R3|508.122|7.512.862|7.512.862|800|
|R4|507.808|7.512.486|7.512.486|755|
|R5|509.146|7.513.850|7.513.850|1.415|
|R6|510.054|7.513.947|7.513.947|1.580|
|R7|507.250|7.511.557|7.511.557|1.210|
|R8|508.457|7.513.187|7.513.187|1.092|

Fuente: Elaboración propia.

**Tabla 10. Características de estaciones de monitoreo.**

|Receptor<br>N°|UTM, Huso 19 S, WGS-<br>84|Col3|Descripción|Distancia al<br>Proyecto<br>(m)|
|---|---|---|---|---|
|**Receptor**<br>**N°**|**Este (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|
|R9|507.371|7.516.056|Estación Centro|4.122|
|R10|506.403|7.516.233|Estación Club Deportivo 23 de Marzo|4.915|
|R11|506.895|7.518.221|Estación Colegio Pedro Vergara Keller|6.287|

Fuente: Elaboración propia.

Dado que la mayor cantidad de emisiones directas estimadas en el estudio de estimación de emisiones
atmosféricas, sugieren que ocurrirán en el año 1 del Proyecto, en el cual se desarrolla la construcción
de este, en consecuencia de esto se modelaron dichas emisiones, lo cual considera:

 Excavaciones

 Demoliciones

 Tránsito vehicular

 Operación de maquinaria y vehículos

 Carguío de material

Es importante señalar, que además de estas emisiones fueron modeladas aquellas producidas por el
tránsito de vehículos por caminos pavimentados, que dan acceso al Proyecto.

La estimación de emisiones para el año 1 resultó ser de 13,43 ton/año de MP 10 y 5,13 ton/año de MP 2,5,
las que consideran todas las emisiones que conlleva el Proyecto. Sin embargo, la modelación consideró
solo las emisiones que se generan dentro del área del Proyecto en este año además de las producidas

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

Página 43 de 65

por el tránsito de caminos pavimentados que dan acceso al Proyecto, tal como fue mencionado
anteriormente.

Además, se consideró en la modelación la transformación química en el aire de precursores de material
particulado, tal como NO x .

Por otro lado, la modelación de las emisiones atmosféricas se realizó teniendo en cuenta la escala
temporal de las construcciones en un horario desde las 8 am a 6 pm. Esto con objeto de ser más prolijos
en la modelación, sobre todo por la influencia que podría tener sobre el promedio horario, calculado
como el percentil 98. A continuación, se presenta en la siguiente figura los polígonos modelados del
Proyecto.

**Figura 40. Polígonos de modelación.**

Fuente: elaboración propia con base en imagen ArcGis 10.2.2.

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

Página 44 de 65

**4** **Resultados**

**4.1** **Área de Influencia**

En la Figura 41, se muestra el área de influencia simulada para el Proyecto, la cual fue evaluada
asumiendo el peor escenario, a partir de la concentración promedio 24 horas de MP 10, de la cual se tiene
lo siguiente:

 - Las concentraciones modeladas son de baja magnitud, estima un área de 1.393 ha.

 - El área llega a concentraciones de 0,169 μg/m [3] como promedio 24 horas.

**Figura 41. Área de influencia del Proyecto.**

Fuente: elaboración propia con base en imagen ArcGis 10.2.2.

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

**4.2** **Concentraciones modeladas**

**Dispersión e isoconcentración de contaminantes**

Página 45 de 65

A continuación, se presentan los resultados de la pluma de dispersión e isoconcentración obtenida para
cada contaminante estudiado. Adicionalmente, se muestran los puntos receptores, sin embargo, las
concentraciones evaluadas como puntos discretos se aborda en extenso en la sección 4.2.2 de este
informe.

**4.2.1.1** **Material particulado respirable, MP** **10**

A continuación, se presenta el análisis de los resultados para el MP 10 tanto para la concentración
promedio anual y 24 horas.

Respecto a la magnitud de las concentraciones simuladas, se observa que tanto la concentración
promedio anual como la concentración promedio 24 horas en las zonas pobladas son bajas.

 - **Concentración Promedio Anual de MP** **10**

En la Figura 42, se observa la dispersión de la concentración promedio anual de MP 10 . Los resultados de
la modelación sugieren que:

 La forma que presenta la pluma de dispersión es acorde a las actividades que ocurrirán por la
construcción del Proyecto (tránsito de vehículos, excavaciones, demoliciones, entre otros), de
acuerdo con los polígonos modelados. Por tanto en base a estos, se visualizan 2 focos emisores
ubicados en el lado este, con concentraciones que van desde 0,048 a 0,570 μg/m3, y otro hacia
el lado norte, con concentraciones que van desde 0,048 a 0,256 μg/m3.

 Las concentraciones modeladas son de baja magnitud y van desde los 0,048 μg/m3 a los 0,570
μg/m3.

 Con relación a los puntos receptores escogidos cercanos al área del Proyecto, se observa que
los resultados de la modelación señalan que la pluma de concentración de MP 10 abarca áreas
que incluye un poco más de la mitad de estos puntos discretos (el 75% del total), pese a lo
anterior, es importante señalar que las concentraciones simuladas en dichos puntos, que se
encuentran dentro del área de la pluma, son de baja magnitud. Cabe mencionar, que dentro del
área de mayor concentración no se encuentra ningún receptor.

En la Figura 43, se puede observar el mapa de isoconcentración, de donde se obtuvieron los siguientes
resultados:

 La isolínea de mayor concentración abarca una superficie aproximada de 15,72 ha y la
concentración sería cercana a los 0,523 μg/m3.

 Se obtuvieron 2 plumas de isoconcentración, de las cuales aquella que simula el mayor foco
emisor, se extiende hasta los 748 m por el norte y 672 m al sur desde la zona de mayor
concentración, en estos lugares las concentraciones modeladas son de 0,105 μg/m3 y
representan una reducción del 80% de la isoconcentración más alta modelada.

**MODELACIÓN DE CONTAMINANTES ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y Mejoramiento Aeropuerto El Loa

de Calama”

**Figura 42. Mapa dispersión de MP** **10** **promedio anual.**

Fuente: elaboración propia con base en imagen ArcGis 10.2.2.

Página 46 de 65

**MODELACIÓN DE CONTAMINANTES ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y Mejoramiento Aeropuerto El Loa

de Calama”

**Figura 43. Mapa de isoconcentración MP** **10** **concentración promedio anual.**

Fuente: elaboración propia con base en imagen ArcGis 10.2.2.

Página 47 de 65

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y Mejoramiento
Aeropuerto El Loa de Calama”

- **Concentración Promedio 24 horas de MP** **10**

Página 48 de 65

En la Figura 44, se presenta la dispersión de la concentración promedio 24 horas de MP 10 [1], de donde se
puede concluir que:

 La pluma de dispersión como promedio de 24 horas tendría lugar mayoritariamente, dentro del
área de emplazamiento del Proyecto. De lo cual, se observan 3 focos emisores, acorde a las
actividades que ocurrirán por la construcción del Proyecto (tránsito de vehículos, excavaciones,
demoliciones, entre otros), de acuerdo con los polígonos modelados.

 En la pluma de dispersión se observa un área de concentraciones mayores, cuyo rango de
concentración varía entre los 1,396 y 1,702 μg/m3, emplazándose en el Proyecto,
específicamente en la zona este del Proyecto.

 Cabe mencionar, que dentro del área de mayor concentración no se encuentra emplazado
ningún receptor.

En la Figura 45, se puede observar la dimensión de la pluma de isoconcentración, de la cual se puede
destacar lo siguiente:

 Se distingue una isolínea de 18,9 ha en donde las concentraciones son cercanas a 1,534 μg/m3.
Esta zona es en donde se simularon las mayores concentraciones para el MP 10 concentración
diaria.

 Existen 2 plumas de isoconcentración, de las cuales, aquella que presenta el mayor foco emisor,
se extiende hasta los 901 m por el norte, 642 m al sur, 647 m hacia el este y 785 m hacia el oeste,
desde la zona de mayor concentración. A estas distancias la concentración esperada es de 0,307
μg/m3. En relación con la otra de pluma de isoconcentración, las concentraciones varían de 0,614
a 0,307 μg/m3, la cual comprende un área de 589 hectáreas.

 Además, es importante destacar que se observan cinco receptores dentro de las isolíneas
simuladas, dentro del área del foco secundario, en el cual las concentraciones en estos puntos
son de baja magnitud.

1 Calculada como el percentil 98 de las concentraciones promedio 24 horas para el año de modelación.

**MODELACIÓN DE CONTAMINANTES ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y Mejoramiento Aeropuerto El Loa

de Calama”

**Figura 44. Mapa dispersión de MP** **10** **promedio 24 horas.**

Fuente: elaboración propia con base en imagen ArcGis 10.2.2.

Página 49 de 65

**MODELACIÓN DE CONTAMINANTES ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y Mejoramiento Aeropuerto El Loa

de Calama”

**Figura 45. Mapa de isoconcentración MP** **10** **concentración promedio 24 horas.**

Fuente: elaboración propia con base en imagen ArcGis 10.2.2.

Página 50 de 65

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y Mejoramiento
Aeropuerto El Loa de Calama”

**4.2.1.2** **Material particulado fino respirable, MP** **2,5**

 - **Concentración Promedio Anual de MP2,5**

Página 51 de 65

En la Figura 46, se observa la dispersión de la concentración promedio anual de MP 2,5, además, se
encuentran los puntos receptores de interés, de donde se puede destacar:

 - Al igual a lo ocurrido en la concentración simulada para el MP 10 anual, la forma que presenta la
pluma de dispersión es acorde a las actividades que ocurrirán por la construcción del Proyecto
(tránsito de vehículos, excavaciones, demoliciones, entre otros), de acuerdo con los polígonos
modelados. Por tanto en base a estos, se visualizan 2 focos emisores ubicados en el lado este,
con concentraciones que van desde 0,026 a 0,315 μg/m3, y otro hacia el lado norte, con
concentraciones que van desde 0,026 a 0,141 μg/m3.

 Las concentraciones modeladas son de baja magnitud y van desde los 0,026 μg/m3 a los 0,315
μg/m3.

 En relación a los puntos receptores escogidos cercanos al área del Proyecto, se observa que los
resultados de la modelación señalan que la pluma de concentración de MP 2,5 abarca áreas que
incluye un poco más de la mitad de estos puntos discretos (el 75% del total), pese a lo anterior,
es importante señalar que las concentraciones simuladas en dichos puntos, que se encuentran
dentro del área de la pluma, son de baja magnitud. Cabe mencionar, que dentro del área de
mayor concentración no se encuentra ningún receptor.

En la Figura 47, se puede observar el mapa de isoconcentración, de donde se obtuvieron los siguientes
resultados:

 La isolínea de mayor concentración abarca una superficie aproximada de 14,52 ha y la
concentración sería cercana a los 0,290 μg/m3.

 Se obtuvieron 2 plumas de isoconcentración, de las cuales aquella que simula el mayor foco
emisor, se extiende hasta los 641 m por el norte y 613 m al sur desde la zona de mayor
concentración, en estos lugares las concentraciones modeladas son de 0,058 μg/m3 y
representan una reducción del 80% de la isoconcentración más alta modelada.

 Además, es importante destacar que no se observan receptores dentro de las isolíneas
simuladas, dado que las concentraciones en estos puntos son de baja magnitud.

**MODELACIÓN DE CONTAMINANTES ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y Mejoramiento Aeropuerto El Loa

de Calama”

**Figura 46. Mapa dispersión MP** **2,5** **promedio anual.**

Fuente: elaboración propia con base en imagen ArcGis 10.2.2.

Página 52 de 65

**MODELACIÓN DE CONTAMINANTES ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y Mejoramiento Aeropuerto El Loa

de Calama”

**Figura 47. Mapa de isoconcentración MP** **2,5** **promedio anual.**

Fuente: elaboración propia con base en imagen ArcGis 10.2.2.

Página 53 de 65

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

- **Concentración Promedio 24 horas de MP** **2,5**

Página 54 de 65

En la Figura 48, se presenta la pluma de dispersión para este contaminante simulada por el modelo en
concentración promedio diaria, de donde es importante señalar:

 La pluma de dispersión como promedio de 24 horas tendría lugar mayoritariamente, dentro del
área de emplazamiento del Proyecto. De lo cual, se observan 3 focos emisores, acorde a las
actividades que ocurrirán por la construcción del Proyecto (tránsito de vehículos, excavaciones,
demoliciones, entre otros), de acuerdo con los polígonos modelados.

 De los 3 focos observados, aquel que presenta las mayores concentraciones modeladas, se ubica
al este del Proyecto. Dentro de este foco, las mayores concentraciones varían de 0,669 a 0,816
μg/m3.

 Cabe mencionar, que dentro del área de mayor concentración no se encuentra emplazado
ningún receptor.

En la Figura 49, se puede observar la dimensión de la pluma de isoconcentración promedio 24 horas
para MP 2,5, de la cual se puede destacar lo siguiente:

 La isolínea de mayor concentración abarca una superficie aproximada de 16,36 ha y la
concentración sería cercana a los 0,741 μg/m3.

 Existen 2 plumas de isoconcentración, de las cuales, aquella que presenta el mayor foco emisor,
se extiende hasta los 701 m por el norte, 636 m al sur, 658 m hacia el este y 702 m hacia el oeste,
desde la zona de mayor concentración. A estas distancias la concentración esperada es de 0,148
μg/m3. En relación con la otra de pluma de isoconcentración, las concentraciones varían de 0,148
a 0,444 μg/m3, la cual comprende un área de 535,82 hectáreas.

 Además, es importante destacar que se observan tres receptores dentro de las isolíneas
simuladas, dentro del área del foco secundario, en el cual las concentraciones en estos puntos
son de baja magnitud.

**MODELACIÓN DE CONTAMINANTES ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y Mejoramiento Aeropuerto El Loa

de Calama”

**Figura 48. Mapa dispersión de MP** **2,5** **concentración promedio 24 horas.**

Fuente: elaboración propia con base en imagen ArcGis 10.2.2.

Página 55 de 65

**MODELACIÓN DE CONTAMINANTES ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y Mejoramiento Aeropuerto El Loa

de Calama”

**Figura 49. Mapa de isoconcentraciones MP** **2,5** **concentración promedio 24 horas.**

Fuente: elaboración propia con base en imagen ArcGis 10.2.2.

Página 56 de 65

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

**Concentración de contaminantes en puntos discretos**

Página 57 de 65

A continuación, se presentan las concentraciones modeladas para cada uno de los contaminantes
en los puntos receptores indicados y las estaciones de monitoreo (Ver la Figura 38 y Figura 39).
Además, dichos receptores están descritos en la Tabla 9 y Tabla 10.

Estos corresponden a la simulación realizada a la altura de 1,6 m sobre el nivel del suelo.

Los resultados de la modelación discreta de MP 10 tanto concentración promedio anual como
concentración promedio 24 horas demostraron que en el receptor “R2”, el cual se encuentra
cercano a uno de los polígonos de modelación por tránsito en camino pavimentado, simula la
concentración más alta de todos los puntos receptores evaluados con 0,127 μg/m [3] como
concentración anual y 0,740 μg/m [3] como concentración diaria, seguidos de este receptor, se
encontraría “R4”, que para el caso de promedio anual simula 0,121 μg/m [3] y 0,406 μg/m [3] como
concentración 24 horas.

Con respecto a la simulación realizada para el contaminante criterio MP 2,5, tal como era de esperar,
dado que se trata de la misma partícula, pero en una proporción más fina, se observa que el
receptor “R2”, evidencia las mayores concentraciones, siendo de 0,055 y 0,198 μg/m [3] en
concentración anual y diaria respectivamente. Esto, seguido de los receptores “R4”, cuyas
concentraciones modeladas corresponden a 0,053 y 0,165 μg/m [3] en concentración anual y diaria
respectivamente.

En la Tabla 11, se presentan los resultados de la modelación discreta de cada punto receptor, de
la cual se observa que en general las concentraciones modeladas son de baja magnitud.

**Tabla 11. Concentraciones modeladas en puntos receptores.**

|Punto<br>Receptor|Concentración modelada de MP<br>10<br>(μg/m3)|Col3|Concentración modelada de MP<br>2,5<br>(μg/m3)|Col5|
|---|---|---|---|---|
|**Punto**<br>**Receptor**|**Promedio Anual**|**Promedio 24**<br>**horas**|**Promedio Anual**|**Promedio 24**<br>**horas**|
|R1|0,022|0,099|0,010|0,050|
|R2|0,127|0,740|0,055|0,198|
|R3|0,086|0,388|0,038|0,147|
|R4|0,121|0,406|0,053|0,165|
|R5|0,027|0,125|0,013|0,069|
|R6|0,021|0,126|0,010|0,067|
|R7|0,054|0,215|0,023|0,097|
|R8|0,054|0,250|0,024|0,115|
|R9|0,006|0,038|0,002|0,016|
|R10|0,004|0,031|0,002|0,015|
|R11|0,002|0,015|0,001|0,007|

Fuente: Elaboración propia.
(*) Las concentraciones sombreadas corresponden a las más altas.

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

Página 58 de 65

**Aporte del Proyecto a la concentración en estaciones de cumplimiento normativo.**

En la Tabla 12, se observa el aumento de la concentración basal registrada en la EMRP Colegio
Pedro Vergara Keller entre enero y diciembre de 2019 (último año analizado) para MP 10 y MP 2,5 .

**Tabla 12. Proyección de la concentración en la EMRP Colegio Pedro Vergara Keller.**

|Concentración<br>(μg/m3)|MP<br>10|Col3|MP<br>2,5|Col5|
|---|---|---|---|---|
|**Concentración**<br>**(μg/m3)**|**Promedio**<br>**anual**|**Promedio 24**<br>**horas**|**Promedio**<br>**anual**|**Promedio 24**<br>**horas**|
|Basal|40,80|67,70|8,50|22,20|
|Del Proyecto|0,002|0,015|0,001|0,007|
|Proyectada en el sector|40,802|67,715|8,501|22,207|

Fuente: Elaboración propia.

Para la Estación Colegio Pedro Vergara Keller, se proyecta un aumento de la condición basal de
0,02% para la concentración promedio diario y 0,01% para la concentración promedio anual de
MP 10 . Con relación al MP 2,5 se esperan incrementos correspondientes a 0,03% y 0,01% como
concentración diaria y anual respectivamente.

En la Tabla 13, se observa el aumento de la concentración basal registrada en la EMRP Club
Deportivo 23 de Marzo entre enero y diciembre de 2019 (último año analizado) para MP 10 y MP 2,5 .

**Tabla 13. Proyección de la concentración en la EMRP Club Deportivo 23 de Marzo.**

|Concentración<br>(μg/m3)|MP<br>10|Col3|MP<br>2,5|Col5|
|---|---|---|---|---|
|**Concentración**<br>**(μg/m3)**|**Promedio**<br>**anual**|**Promedio 24**<br>**horas**|**Promedio**<br>**anual**|**Promedio 24**<br>**horas**|
|Basal|39,30|62,50|7,00|41,20|
|Del Proyecto|0,004|0,031|0,002|0,015|
|Proyectada en el sector|39,304|62,531|7,002|41,215|

Fuente: Elaboración propia.

Los resultados proyectan para la estación Club Deportivo 23 de Marzo, un aumento de la condición
basal de 0,05% para la concentración promedio diario y 0,01% para la concentración promedio
anual de MP 10 . Mientras que para MP 2,5 se esperan incrementos correspondientes a 0,03% y 0,04%
como concentración anual y diaria respectivamente.

En la Tabla 14, se observa el aumento de la concentración basal registrada en la EMRP Centro
entre enero y diciembre de 2019 (último año analizado) para MP 10 y MP 2,5 .

**Tabla 14. Proyección de la concentración en la EMRP Centro.**

|Concentración<br>(μg/m3)|MP<br>10|Col3|MP<br>2,5|Col5|
|---|---|---|---|---|
|**Concentración**<br>**(μg/m3)**|**Promedio**<br>**anual**|**Promedio 24**<br>**horas**|**Promedio**<br>**anual**|**Promedio 24**<br>**horas**|
|Basal|31,10|52,50|5,80|10,10|
|Del Proyecto|0,006|0,038|0,002|0,016|

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

Página 59 de 65

|Concentración<br>(μg/m3)|MP<br>10|Col3|MP<br>2,5|Col5|
|---|---|---|---|---|
|**Concentración**<br>**(μg/m3)**|**Promedio**<br>**anual**|**Promedio 24**<br>**horas**|**Promedio**<br>**anual**|**Promedio 24**<br>**horas**|
|Proyectada en el sector|31,106|52,538|5,802|10,116|

Fuente: Elaboración propia.

Los resultados proyectan para la estación Centro, un aumento de la condición basal de 0,07% para
la concentración promedio diario y 0,02% para la concentración promedio anual de MP 10 . Mientras
que para MP 2,5 se esperan incrementos correspondientes a 0,04% y 0,16% como concentración
anual y diaria respectivamente.

En base a todo lo anterior y teniendo en cuenta que las estaciones representan zonas urbanas
pobladas en la ciudad, resulta importante destacar que se prevé un aumento no significativo en
la condición basal de la ciudad registrada en las estaciones consideradas y que la puesta en
marcha del Proyecto no representa un cambio sustancial de la calidad del aire.

Además, en relación a los valores presentados en la Tabla 12, Tabla 13 y Tabla 14, y de acuerdo a
la Tabla 1 (que incluye los valores normados límites para MP 10 y MP 2,5 en Chile), se observa que la
situación proyectada en el sector, en las 3 estaciones de calidad de aire evaluadas (Estación
Colegio Pedro Vergara Keller, Estación Club Deportivo 23 de Marzo y Estación Centro) para los
dos contaminantes evaluados, se encontrarían bajo los límites normativos.

**Aporte sinérgico del Proyecto y Proyectos circundantes aprobados ambientalmente**
**por el SEIA a la concentración en estaciones de cumplimiento normativo.**

En la Tabla 15, se observa el aporte a la concentración basal en la EMRP Colegio Pedro Vergara
Keller entre enero y diciembre de 2019 (último año analizado) para MP 10 y MP 2,5 por la sinergia
producida por los Proyectos que se pretenden emplazar aledaños a esta y que fueron evaluados
ambientalmente.

**Tabla 15. Aporte a la concentración de MP Proyectos en la EMRP Colegio Pedro Vergara**

**Keller**

|Efecto Sinérgico|Col2|Concentración (μg/m3)|Col4|Col5|Col6|
|---|---|---|---|---|---|
|**Efecto Sinérgico**|**Efecto Sinérgico**|**MP10 **|**MP10 **|**MP2,5 **|**MP2,5 **|
|**Efecto Sinérgico**|**Efecto Sinérgico**|**Promedio**<br>**anual**|**Promedio**<br>**24 horas**|**Promedio**<br>**anual**|**Promedio**<br>**24 horas**|
|**Proyectos aprobados**<br>**ambientalmente en**|Parque fotovoltaico Verano de<br>San Juan I|0,00112|0,00732|0,00050|0,00325|
|**Proyectos aprobados**<br>**ambientalmente en**|Parque Eólico Calama|0,00000|0,00000|0,00000|0,00000|
|**Proyectos aprobados**<br>**ambientalmente en**|Línea de Transmisión 1x110 kV,<br>Planta Usya A Parque Eólico<br>Valle de los Vientos|0,00700|0,04300|0,00600|0,00360|
|**Proyectos aprobados**<br>**ambientalmente en**|Proyecto Fotovoltaico<br>Azabache|0,01000|0,06000|0,00200|0,01000|

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

Página 60 de 65

|Efecto Sinérgico<br>Potenciamiento Planta<br>Tratamiento De Aguas Servidas<br>Calama, Tratacal S.A.<br>Circunvalación Oriente Calama2<br>Parque fotovoltaico Verano de<br>San Juan II|Col2|Concentración (μg/m3)|Col4|Col5|Col6|
|---|---|---|---|---|---|
|**Efecto Sinérgico**<br>Potenciamiento Planta<br>Tratamiento De Aguas Servidas<br>Calama, Tratacal S.A.<br>Circunvalación Oriente Calama2 <br>Parque fotovoltaico Verano de<br>San Juan II|**Efecto Sinérgico**<br>Potenciamiento Planta<br>Tratamiento De Aguas Servidas<br>Calama, Tratacal S.A.<br>Circunvalación Oriente Calama2 <br>Parque fotovoltaico Verano de<br>San Juan II|**MP10 **|**MP10 **|**MP2,5 **|**MP2,5 **|
|**Efecto Sinérgico**<br>Potenciamiento Planta<br>Tratamiento De Aguas Servidas<br>Calama, Tratacal S.A.<br>Circunvalación Oriente Calama2 <br>Parque fotovoltaico Verano de<br>San Juan II|**Efecto Sinérgico**<br>Potenciamiento Planta<br>Tratamiento De Aguas Servidas<br>Calama, Tratacal S.A.<br>Circunvalación Oriente Calama2 <br>Parque fotovoltaico Verano de<br>San Juan II|**Promedio**<br>**anual**|**Promedio**<br>**24 horas**|**Promedio**<br>**anual**|**Promedio**<br>**24 horas**|
|**Efecto Sinérgico**<br>Potenciamiento Planta<br>Tratamiento De Aguas Servidas<br>Calama, Tratacal S.A.<br>Circunvalación Oriente Calama2 <br>Parque fotovoltaico Verano de<br>San Juan II|Potenciamiento Planta<br>Tratamiento De Aguas Servidas<br>Calama, Tratacal S.A.|0,00000|0,00000|0,00000|0,00000|
|**Efecto Sinérgico**<br>Potenciamiento Planta<br>Tratamiento De Aguas Servidas<br>Calama, Tratacal S.A.<br>Circunvalación Oriente Calama2 <br>Parque fotovoltaico Verano de<br>San Juan II|Circunvalación Oriente Calama2|0,00090|0,00580|0,00050|0,00323|
|**Efecto Sinérgico**<br>Potenciamiento Planta<br>Tratamiento De Aguas Servidas<br>Calama, Tratacal S.A.<br>Circunvalación Oriente Calama2 <br>Parque fotovoltaico Verano de<br>San Juan II|Parque fotovoltaico Verano de<br>San Juan II|0,10000|0,10000|0,00000|0.00000|
|**Sumatoria Proyectos evaluados por**<br>**el SEIA**|**Sumatoria Proyectos evaluados por**<br>**el SEIA**|**0,1208**|**0,2278**|**0,0095**|**0,0228**|
|**Proyecto**|**Proyecto**|**0,002**|**0,015**|**0,001**|**0,007**|
|**Situación basal**|**Situación basal**|**40,80**|**67,70**|**8,50**|**22,20**|
|**Concentración proyectada**|**Concentración proyectada**|**40,9228**|**67,9428**|**8,5105**|**22,2298**|

Fuente: Elaboración propia con base a datos del SEIA.

Para la Estación Colegio Pedro Vergara Keller, se proyecta que el aporte producto de la sinergia a
la condición basal sea de un 0,357% para la concentración promedio diario y 0,300% para la
concentración promedio anual de MP 10 . Con relación al MP 2,5 se esperan incrementos
correspondientes a 0,134% y 0,123% como concentración diaria y anual respectivamente.

En la Tabla 16, se observa el aporte a la concentración basal en la EMRP Club Deportivo 23 de
Marzo entre enero y diciembre de 2019 (último año analizado) para MP 10 y MP 2,5 por la sinergia
producida por los Proyectos que se pretenden emplazar aledaños a esta y que fueron evaluados
ambientalmente.

**Tabla 16. Aporte a la concentración de MP Proyectos en la EMRP Club Deportivo 23 de**

**Marzo.**

|Efecto Sinérgico|Col2|Concentración (μg/m3)|Col4|Col5|Col6|
|---|---|---|---|---|---|
|**Efecto Sinérgico**|**Efecto Sinérgico**|**MP10 **|**MP10 **|**MP2,5 **|**MP2,5 **|
|**Efecto Sinérgico**|**Efecto Sinérgico**|**Promedio**<br>**anual**|**Promedio**<br>**24 horas**|**Promedio**<br>**anual**|**Promedio**<br>**24 horas**|
|**Proyectos**<br>**aprobados**|Parque fotovoltaico Verano de<br>San Juan I|0,00219|0,01350|0,00097|0,00593|
|**Proyectos**<br>**aprobados**|Parque Eólico Calama|0,00000|0,00000|0,00000|0,00000|
|**Proyectos**<br>**aprobados**|Línea de Transmisión 1x110 kV,<br>Planta Usya A Parque Eólico<br>Valle de los Vientos|0,02400|0,07600|0,00200|0,00680|

2 Proyecto en estado de evaluación.

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

Página 61 de 65

|Efecto Sinérgico<br>Proyecto Fotovoltaico<br>Azabache<br>Potenciamiento Planta<br>Tratamiento De Aguas Servidas<br>Calama, Tratacal S.A.<br>Circunvalación Oriente Calama2<br>Parque fotovoltaico Verano de<br>San Juan II|Col2|Concentración (μg/m3)|Col4|Col5|Col6|
|---|---|---|---|---|---|
|**Efecto Sinérgico**<br>Proyecto Fotovoltaico<br>Azabache<br>Potenciamiento Planta<br>Tratamiento De Aguas Servidas<br>Calama, Tratacal S.A.<br>Circunvalación Oriente Calama2 <br>Parque fotovoltaico Verano de<br>San Juan II|**Efecto Sinérgico**<br>Proyecto Fotovoltaico<br>Azabache<br>Potenciamiento Planta<br>Tratamiento De Aguas Servidas<br>Calama, Tratacal S.A.<br>Circunvalación Oriente Calama2 <br>Parque fotovoltaico Verano de<br>San Juan II|**MP10 **|**MP10 **|**MP2,5 **|**MP2,5 **|
|**Efecto Sinérgico**<br>Proyecto Fotovoltaico<br>Azabache<br>Potenciamiento Planta<br>Tratamiento De Aguas Servidas<br>Calama, Tratacal S.A.<br>Circunvalación Oriente Calama2 <br>Parque fotovoltaico Verano de<br>San Juan II|**Efecto Sinérgico**<br>Proyecto Fotovoltaico<br>Azabache<br>Potenciamiento Planta<br>Tratamiento De Aguas Servidas<br>Calama, Tratacal S.A.<br>Circunvalación Oriente Calama2 <br>Parque fotovoltaico Verano de<br>San Juan II|**Promedio**<br>**anual**|**Promedio**<br>**24 horas**|**Promedio**<br>**anual**|**Promedio**<br>**24 horas**|
|**Efecto Sinérgico**<br>Proyecto Fotovoltaico<br>Azabache<br>Potenciamiento Planta<br>Tratamiento De Aguas Servidas<br>Calama, Tratacal S.A.<br>Circunvalación Oriente Calama2 <br>Parque fotovoltaico Verano de<br>San Juan II|Proyecto Fotovoltaico<br>Azabache|0,03000|0,12000|0,00500|0,02000|
|**Efecto Sinérgico**<br>Proyecto Fotovoltaico<br>Azabache<br>Potenciamiento Planta<br>Tratamiento De Aguas Servidas<br>Calama, Tratacal S.A.<br>Circunvalación Oriente Calama2 <br>Parque fotovoltaico Verano de<br>San Juan II|Potenciamiento Planta<br>Tratamiento De Aguas Servidas<br>Calama, Tratacal S.A.|0,07000|0,23000|0,03000|0,09000|
|**Efecto Sinérgico**<br>Proyecto Fotovoltaico<br>Azabache<br>Potenciamiento Planta<br>Tratamiento De Aguas Servidas<br>Calama, Tratacal S.A.<br>Circunvalación Oriente Calama2 <br>Parque fotovoltaico Verano de<br>San Juan II|Circunvalación Oriente Calama2|0,00176|0,01010|0,00097|0,00556|
|**Efecto Sinérgico**<br>Proyecto Fotovoltaico<br>Azabache<br>Potenciamiento Planta<br>Tratamiento De Aguas Servidas<br>Calama, Tratacal S.A.<br>Circunvalación Oriente Calama2 <br>Parque fotovoltaico Verano de<br>San Juan II|Parque fotovoltaico Verano de<br>San Juan II|0,00000|0,10000|0,00000|0,00000|
|**Sumatoria Proyectos evaluados por**<br>**el SEIA**|**Sumatoria Proyectos evaluados por**<br>**el SEIA**|**0,1312**|**0,5722**|**0,0397**|**0,1345**|
|**Proyecto**|**Proyecto**|**0,0040**|**0,0310**|**0,0020**|**0,0150**|
|**Situación basal**|**Situación basal**|**39,3000**|**62,5000**|**7,0000**|**41,2000**|
|**Concentración proyectada en la**<br>**Estación**|**Concentración proyectada en la**<br>**Estación**|**39,4352**|**63,1032**|**7,0417**|**41,3495**|

Fuente: Elaboración propia con base a datos del SEIA.

Los resultados que se proyectan muestran que el aporte producto de la sinergia a la condición
basal sea para la estación Club Deportivo 23 de Marzo, un aumento de la condición basal de
0,956% para la concentración promedio diario y 0,343% para la concentración promedio anual de
MP 10 . Mientras que para MP 2,5 se esperan incrementos correspondientes a 0,593% y 0,362% como
concentración anual y diaria respectivamente.

En la Tabla 17, se observa el aporte a la concentración basal en la EMRP Centro entre enero y
diciembre de 2019 (último año analizado) para MP 10 y MP 2,5 por la sinergia producida por los
Proyectos que se pretenden emplazar aledaños a esta y que fueron evaluados ambientalmente.

**Tabla 17. Aporte a la concentración de MP Proyectos en la EMRP Centro.**

|Efecto Sinérgico|Col2|Concentración (μg/m3)|Col4|Col5|Col6|
|---|---|---|---|---|---|
|**Efecto Sinérgico**|**Efecto Sinérgico**|**MP10 **|**MP10 **|**MP2,5 **|**MP2,5 **|
|**Efecto Sinérgico**|**Efecto Sinérgico**|**Promedio**<br>**anual**|**Promedio**<br>**24 horas**|**Promedio**<br>**anual**|**Promedio**<br>**24 horas**|
|**Proyectos**<br>**aprobados**|Parque fotovoltaico Verano de<br>San Juan I|0,00167|0,00706|0,00074|0,00314|
|**Proyectos**<br>**aprobados**|Parque Eólico Calama|0,00000|0,00000|0,00000|0,00000|
|**Proyectos**<br>**aprobados**|Línea de Transmisión 1x110 kV,<br>Planta Usya A Parque Eólico<br>Valle de los Vientos|0,02800|0,09500|0,00240|0,00830|

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

Página 62 de 65

|Efecto Sinérgico<br>Proyecto Fotovoltaico<br>Azabache<br>Potenciamiento Planta<br>Tratamiento De Aguas Servidas<br>Calama, Tratacal S.A.<br>Circunvalación Oriente Calama2<br>Parque fotovoltaico Verano de<br>San Juan II|Col2|Concentración (μg/m3)|Col4|Col5|Col6|
|---|---|---|---|---|---|
|**Efecto Sinérgico**<br>Proyecto Fotovoltaico<br>Azabache<br>Potenciamiento Planta<br>Tratamiento De Aguas Servidas<br>Calama, Tratacal S.A.<br>Circunvalación Oriente Calama2 <br>Parque fotovoltaico Verano de<br>San Juan II|**Efecto Sinérgico**<br>Proyecto Fotovoltaico<br>Azabache<br>Potenciamiento Planta<br>Tratamiento De Aguas Servidas<br>Calama, Tratacal S.A.<br>Circunvalación Oriente Calama2 <br>Parque fotovoltaico Verano de<br>San Juan II|**MP10 **|**MP10 **|**MP2,5 **|**MP2,5 **|
|**Efecto Sinérgico**<br>Proyecto Fotovoltaico<br>Azabache<br>Potenciamiento Planta<br>Tratamiento De Aguas Servidas<br>Calama, Tratacal S.A.<br>Circunvalación Oriente Calama2 <br>Parque fotovoltaico Verano de<br>San Juan II|**Efecto Sinérgico**<br>Proyecto Fotovoltaico<br>Azabache<br>Potenciamiento Planta<br>Tratamiento De Aguas Servidas<br>Calama, Tratacal S.A.<br>Circunvalación Oriente Calama2 <br>Parque fotovoltaico Verano de<br>San Juan II|**Promedio**<br>**anual**|**Promedio**<br>**24 horas**|**Promedio**<br>**anual**|**Promedio**<br>**24 horas**|
|**Efecto Sinérgico**<br>Proyecto Fotovoltaico<br>Azabache<br>Potenciamiento Planta<br>Tratamiento De Aguas Servidas<br>Calama, Tratacal S.A.<br>Circunvalación Oriente Calama2 <br>Parque fotovoltaico Verano de<br>San Juan II|Proyecto Fotovoltaico<br>Azabache|0,04000|0,01300|0,01000|0,02000|
|**Efecto Sinérgico**<br>Proyecto Fotovoltaico<br>Azabache<br>Potenciamiento Planta<br>Tratamiento De Aguas Servidas<br>Calama, Tratacal S.A.<br>Circunvalación Oriente Calama2 <br>Parque fotovoltaico Verano de<br>San Juan II|Potenciamiento Planta<br>Tratamiento De Aguas Servidas<br>Calama, Tratacal S.A.|0,06000|0,21000|0,02000|0,05000|
|**Efecto Sinérgico**<br>Proyecto Fotovoltaico<br>Azabache<br>Potenciamiento Planta<br>Tratamiento De Aguas Servidas<br>Calama, Tratacal S.A.<br>Circunvalación Oriente Calama2 <br>Parque fotovoltaico Verano de<br>San Juan II|Circunvalación Oriente Calama2|0,00141|0,00686|0,00078|0,00381|
|**Efecto Sinérgico**<br>Proyecto Fotovoltaico<br>Azabache<br>Potenciamiento Planta<br>Tratamiento De Aguas Servidas<br>Calama, Tratacal S.A.<br>Circunvalación Oriente Calama2 <br>Parque fotovoltaico Verano de<br>San Juan II|Parque fotovoltaico Verano de<br>San Juan II|0,00000|0,10000|0,00000|0,00000|
|**Sumatoria Proyectos evaluados por**<br>**el SEIA**|**Sumatoria Proyectos evaluados por**<br>**el SEIA**|**0,1349**|**0,4610**|**0,0349**|**0,0927**|
|**Proyecto**|**Proyecto**|**0,0060**|**0,0380**|**0,0020**|**0,0160**|
|**Situación basal**|**Situación basal**|**31,1000**|**52,5000**|**5,8000**|**10,1000**|
|**Concentración proyectada en la**<br>**Estación**|**Concentración proyectada en la**<br>**Estación**|**31,2409**|**52,9990**|**5,8369**|**10,2087**|

Fuente: Elaboración propia con base a datos del SEIA.

Los resultados muestran que el aporte producto de la sinergia a la condición basal sea para la
Estación Centro, un aumento de la condición basal de 0,942% para la concentración promedio
diario y 0,451% para la concentración promedio anual de MP 10 . Mientras que para MP 2,5 se esperan
incrementos correspondientes a 0,632% y 1,064% como concentración anual y diaria
respectivamente.

Es importante mencionar que los valores presentados en la Tabla 15, Tabla 16 y Tabla 17, y de
acuerdo a la Tabla 1 (que incluye los valores normados límites para MP 10 y MP 2,5 en Chile), se
observa que el aporte sinérgico de los diferentes Proyectos en el sector, evaluados en las
estaciones de calidad de aire (Estación Colegio Pedro Vergara Keller, Estación Club Deportivo 23
de Marzo y Estación Centro) para MP 10 y MP 2,5, se encontrarían bajo los límites normativos.

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

**5** **Análisis de resultados**

Página 63 de 65

Se estudió la concentración de las emisiones producto de la construcción del primer año del
“Proyecto Referencial Ampliación y Mejoramiento Aeropuerto El Loa de Calama”. De esta forma,
fueron modeladas las emisiones MP 10, MP 2,5 junto a su precursor NOx, a fin de determinar las
concentraciones que éstos tendrán en la atmosfera y desde este punto de vista, evaluar el aporte
a la línea de base, además de prever posibles efectos negativos a la salud de las personas.

Tal como se abordó en la sección 4.2.2 de éste informe, el receptor que recibiría un mayor aporte
en la concentración basal de por los dos contaminantes estudiados sería el receptor “R2”, que se
encuentra cercano a uno de los polígonos de modelación por tránsito en camino pavimentado,
con una simulación de concentración anual y diaria en el aire correspondiente a 0,127 y 0,740
μg/m [3] de MP 10, ubicado a una distancia de 620 metros del Proyecto. Con relación al MP 2,5 tal como
era de esperar, dado que se trata de la misma partícula, pero en una proporción más fina, se
observa que el receptor que simula la mayor concentración corresponde nuevamente a “R2”, en
donde se evidencian concentraciones de 0,055 y 0,198 μg/m [3] en concentración anual y diaria
respectivamente. Valores que fueron modelados a una altura promedio de 1,6 metros. Por lo
anterior, el aporte a los receptores evaluados es de bajas magnitudes.

El análisis de la variación de la concentración sobre la línea de base demuestra que el
funcionamiento del Proyecto prevé un aumento de la condición basal, el cual se ve reflejado
mayoritariamente en la estación de monitoreo Estación Centro, ubicada al oeste del Proyecto, a
una distancia de 4.122 metros, en esta se simula un aumento de la condición basal de 0,07% para
la concentración promedio diario y 0,02% para la concentración promedio anual de MP 10 . Mientras
que para MP 2,5 se esperan incrementos correspondientes a 0,04% y 0,16% como concentración
anual y diaria respectivamente en esta Estación. Por lo cual, el aporte a la concentración basal en
la estación no representaría un aumento significativo respecto de la línea de base.

Con relación a la sinergia aportada por otros Proyectos evaluados ambientalmente cercanos al
área de estudio, los resultados muestran que el aporte en la Estación Centro prevé el mayor
incremento en sus concentraciones, evidenciando un aumento de la condición basal de 0,499
μg/m [3] para la concentración promedio diario y 0,141 μg/m [3] para la concentración promedio anual
de MP 10 . Mientras que para MP 2,5 se esperan incrementos correspondientes a 0,037 μg/m [3] y 0,109
μg/m [3] como concentración anual y diaria, respectivamente. De estos aportes, el Proyecto sería
responsable del 7,615% y 4,259% de las concentraciones de MP 10 como concentración diaria y
anual, respectivamente, así como también del 5,418% y 14,726% de la concentración anual y diaria
de MP 2,5, respectivamente.

En relación a las plumas de dispersión presentadas en el Acápite 4.2.1, la forma que presenta la
pluma de dispersión es acorde a las actividades que ocurrirán por la construcción del Proyecto
(tránsito de vehículos, excavaciones, demoliciones, entre otros), de acuerdo a los polígonos
modelados (es decir, rodeando principalmente el área del Proyecto). Dentro de este contexto, es
importante considerar que la concentración en el aire de los contaminantes puede ser influida por
diversos factores, entre los cuales están la tasa de emisión, las condiciones en que los
contaminantes son liberados a la atmósfera, la topografía del entorno, e indudablemente las
condiciones meteorológicas; es decir, la dispersión y concentración de las partículas y gases en el
aire quedará determinado por las condiciones ambientales en donde estos son liberados, como

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

Página 64 de 65

por ejemplo: gradiente de presión, gradiente de temperatura, velocidad y dirección del vientos
(los que a su vez están influenciados por las características topográficas del lugar), entre otros.

Cabe mencionar que la modelación de dispersión de contaminantes fue simulada usando el
modelo meteorológico WRF, el cual es recomendado por el SEIA en la Guía para el Uso de Modelos
de Calidad del Aire. El modelo meteorológico es de importancia, pues simula las condiciones que
conforman el proceso de dispersión de contaminantes.

Finalmente, la modelación de las emisiones del Proyecto producto del material particulado, MP 10
y MP 2,5, siendo analizadas según línea de base y debido al incremento que estos presentarían en
las EMRP y la sinergia junto con los demás Proyectos, no representan un riesgo significativo a la
salud ni calidad de vida de la población, puesto que en ningún caso la proyección de la
concentración en los puntos receptores evaluados, respecto de la concentración basal representó
un aumento significativo; así mismo, se presume que no habrá afectación a los recursos naturales
dado las bajas tasas de concentraciones obtenidas de dicha modelación. Además, es importante
mencionar que el aporte del Proyecto en las estaciones de monitoreo de calidad de aire, de
acuerdo a la Tabla 1 (que incluye los valores normados límites para MP 10 y MP 2,5 en Chile), para
MP 10 y MP 2,5, se encontrarían bajo los límites normativos vigentes.

**MODELACIÓN DE CONTAMINANTES**

**ATMOSFFÉRICOS**

“Proyecto Referencial Ampliación y
Mejoramiento Aeropuerto El Loa de Calama”

Página 65 de 65

**Referencias**

Servicio de Evaluación Ambiental, 2012, Guía para el Uso de Modelos de Calidad del Aire en el
SEIA, p. 14-39. Recuperado el 01 de abril de 2016, desde
http://www.sea.gob.cl/sites/default/files/migration_files/guias/Guia_uso_modelo_calidad_del_air
e_seia.pdf

Ministerio del Medio Ambiente, 2015, Análisis General del Impacto Económico y social del
Proyecto de Plan de Prevención y Descontaminación de la Región Metropolitana. Recuperado el
13 de octubre de 2020, desde

https://consultasciudadanas.mma.gob.cl/storage/epac/antecedentes/3817cd40-bea9-485f-a37f90ae30b10940.pdf

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Valores normados para MP** **10** **y MP** **2,5** **en Chile.****

| Nivel | MP (μg/m3)<br>10 | MP (μg/m3)<br>2,5 |
| --- | --- | --- |
| **Límite anual** | 50 | 20 |
| **Limite diario** | 150 | 50 |
| **Alerta** | 195-239 | 80-109 |
| **Preemergencia** | 240-329 | 110-169 |
| **Emergencia** | 330 o mayor | 170 o mayor |

**Tabla 2.: Concentración promedio anual de MP** **10** **Estación Colegio Pedro Vergara Keller.****

| Año | Porcentaje de<br>datos<br>disponibles<br>(%) | Concentración<br>Promedio Anual<br>(μg/m3) | Límite normativo D.S.<br>N°59/1998<br>MINSEGPRES (μg/m3) | Porcentaje de<br>excedencia de la<br>norma (%) |
| --- | --- | --- | --- | --- |
| 2013 | 93 | 60,1 | 50 | Supera |
| 2014 | 89 | 59,9 | 59,9 | Supera |
| 2015 | 87 | 52,1 | 52,1 | Supera |
| 2016 | 90 | 45,9 | 45,9 | No supera |
| 2017 | 91 | 47,0 | 47,0 | No supera |
| 2018 | 96 | 49,7 | 49,7 | No supera |
| 2019 | 85 | 40,8 | 40,8 | No supera |

**Tabla 3.: Concentración promedio anual de MP** **2,5** **Estación Colegio Pedro Vergara Keller.****

| Año | Porcentaje de<br>datos<br>disponibles<br>(%) | Concentración<br>Promedio Anual<br>(μg/m3) | Límite normativo D.S.<br>12/2011 MMA (μg/m3) | Porcentaje de<br>excedencia de la<br>norma (%) |
| --- | --- | --- | --- | --- |
| 2013 | 93 | 11,7 | 20 | No supera |
| 2014 | 89 | 11,8 | 11,8 | No supera |
| 2015 | 85 | 11,3 | 11,3 | No supera |
| 2016 | 90 | 10,4 | 10,4 | No supera |
| 2017 | 87 | 9,5 | 9,5 | No supera |
| 2018 | 96 | 12,4 | 12,4 | No supera |
| 2019 | 84 | 8,5 | 8,5 | No supera |

**Tabla 4.: Concentración promedio anual de MP** **10** **Estación Club Deportivo 23 de Marzo.****

| Año | Porcentaje de<br>datos<br>disponibles<br>(%) | Concentración<br>Promedio Anual<br>(μg/m3) | Límite normativo D.S.<br>N°59/1998<br>MINSEGPRES (μg/m3) | Porcentaje de<br>excedencia de la<br>norma (%) |
| --- | --- | --- | --- | --- |
| 2013 | 97 | 46,9 | 50 | No supera |
| 2014 | 97 | 43,3 | 43,3 | No supera |
| 2015 | 96 | 47,0 | 47,0 | No supera |
| 2016 | 98 | 42,1 | 42,1 | No supera |
| 2017 | 93 | 38,9 | 38,9 | No supera |
| 2018 | 90 | 44,4 | 44,4 | No supera |
| 2019 | 95 | 39,3 | 39,3 | No supera |

**Tabla 5.: Concentración promedio anual de MP** **2,5** **Estación Club Deportivo 23 de Marzo.****

| Año | Porcentaje de<br>datos disponibles<br>(%) | Concentración<br>Promedio Anual<br>(μg/m3) | Límite normativo<br>D.S. N°12/2011 MMA<br>(μg/m3) | Porcentaje de<br>excedencia de la<br>norma (%) |
| --- | --- | --- | --- | --- |
| 2013 | 97 | 7,8 | 20 | No supera |
| 2014 | 98 | 8,4 | 8,4 | No supera |
| 2015 | 96 | 9,3 | 9,3 | No supera |
| 2016 | 99 | 6,8 | 6,8 | No supera |
| 2017 | 96 | 6,3 | 6,3 | No supera |
| 2018 | 88 | 10,3 | 10,3 | No supera |
| 2019 | 96 | 7,0 | 7,0 | No supera |

**Tabla 6.: Concentración promedio anual de MP** **10** **Estación Centro.****

| Año | Porcentaje de<br>datos<br>disponibles<br>(%) | Concentración<br>Promedio Anual<br>(μg/m3) | Límite normativo D.S.<br>N°59/1998<br>MINSEGPRES (μg/m3) | Porcentaje de<br>excedencia de la<br>norma (%) |
| --- | --- | --- | --- | --- |
| 2013 | 87 | 47,0 | 50 | No supera |
| 2014 | 93 | 42,0 | 42,0 | No supera |
| 2015 | 96 | 40,8 | 40,8 | No supera |
| 2016 | 96 | 38,0 | 38,0 | No supera |
| 2017 | 95 | 33,0 | 33,0 | No supera |
| 2018 | 91 | 30,9 | 30,9 | No supera |
| 2019 | 92 | 31,1 | 31,1 | No supera |

**Tabla 7.: Concentración promedio anual de MP** **2,5** **Estación Centro.****

| Año | Porcentaje de<br>datos<br>disponibles<br>(%) | Concentración<br>Promedio Anual<br>(μg/m3) | Límite normativo D.S.<br>N°12/2011 MMA<br>(μg/m3) | Porcentaje de<br>excedencia de la<br>norma (%) |
| --- | --- | --- | --- | --- |
| 2013 | 87 | 10,9 | 20 | No supera |
| 2014 | 93 | 9,6 | 9,6 | No supera |
| 2015 | 96 | 9,3 | 9,3 | No supera |
| 2016 | 98 | 9,2 | 9,2 | No supera |
| 2017 | 96 | 7,8 | 7,8 | No supera |
| 2018 | 82 | 7,2 | 7,2 | No supera |
| 2019 | 84 | 5,8 | 5,8 | No supera |

**Tabla 8.: Coordenadas de vértices del área de estudio.****

| Vértice | Proyección: UTM, Huso 19 Sur; Datum: WGS-84 | Col3 |
| --- | --- | --- |
| **Vértice** | **Este (km)** | **Norte (km)** |
| Noroeste | 488560.70 | 7557205.96 |
| Noreste | 550560.70 | 7557205.96 |
| Suroeste | 488560.70 | 7495205.96 |
| Sureste | 550560.70 | 7495205.96 |
| Centroide | 519560.70 | 7526205.96 |

**Tabla 9.: Características de receptores discretos.****

| Receptor<br>N° | UTM, Huso 19 S, WGS-<br>84 | Col3 | Descripción | Distancia al<br>Proyecto<br>(m) |
| --- | --- | --- | --- | --- |
| **Receptor**<br>**N°** | **Este (m)** | **Norte (m)** | **Norte (m)** | **Norte (m)** |
| R1 | 508.810 | 7.513.502 | Viviendas cercanas | 1.278 |
| R2 | 508.166 | 7.512.663 | 7.512.663 | 620 |
| R3 | 508.122 | 7.512.862 | 7.512.862 | 800 |
| R4 | 507.808 | 7.512.486 | 7.512.486 | 755 |
| R5 | 509.146 | 7.513.850 | 7.513.850 | 1.415 |
| R6 | 510.054 | 7.513.947 | 7.513.947 | 1.580 |
| R7 | 507.250 | 7.511.557 | 7.511.557 | 1.210 |
| R8 | 508.457 | 7.513.187 | 7.513.187 | 1.092 |

**Tabla 10.: Características de estaciones de monitoreo.****

| Receptor<br>N° | UTM, Huso 19 S, WGS-<br>84 | Col3 | Descripción | Distancia al<br>Proyecto<br>(m) |
| --- | --- | --- | --- | --- |
| **Receptor**<br>**N°** | **Este (m)** | **Norte (m)** | **Norte (m)** | **Norte (m)** |
| R9 | 507.371 | 7.516.056 | Estación Centro | 4.122 |
| R10 | 506.403 | 7.516.233 | Estación Club Deportivo 23 de Marzo | 4.915 |
| R11 | 506.895 | 7.518.221 | Estación Colegio Pedro Vergara Keller | 6.287 |

**Tabla 11.: Concentraciones modeladas en puntos receptores.****

| Punto<br>Receptor | Concentración modelada de MP<br>10<br>(μg/m3) | Col3 | Concentración modelada de MP<br>2,5<br>(μg/m3) | Col5 |
| --- | --- | --- | --- | --- |
| **Punto**<br>**Receptor** | **Promedio Anual** | **Promedio 24**<br>**horas** | **Promedio Anual** | **Promedio 24**<br>**horas** |
| R1 | 0,022 | 0,099 | 0,010 | 0,050 |
| R2 | 0,127 | 0,740 | 0,055 | 0,198 |
| R3 | 0,086 | 0,388 | 0,038 | 0,147 |
| R4 | 0,121 | 0,406 | 0,053 | 0,165 |
| R5 | 0,027 | 0,125 | 0,013 | 0,069 |
| R6 | 0,021 | 0,126 | 0,010 | 0,067 |
| R7 | 0,054 | 0,215 | 0,023 | 0,097 |
| R8 | 0,054 | 0,250 | 0,024 | 0,115 |
| R9 | 0,006 | 0,038 | 0,002 | 0,016 |
| R10 | 0,004 | 0,031 | 0,002 | 0,015 |
| R11 | 0,002 | 0,015 | 0,001 | 0,007 |

**Tabla 12.: Proyección de la concentración en la EMRP Colegio Pedro Vergara Keller.****

| Concentración<br>(μg/m3) | MP<br>10 | Col3 | MP<br>2,5 | Col5 |
| --- | --- | --- | --- | --- |
| **Concentración**<br>**(μg/m3)** | **Promedio**<br>**anual** | **Promedio 24**<br>**horas** | **Promedio**<br>**anual** | **Promedio 24**<br>**horas** |
| Basal | 40,80 | 67,70 | 8,50 | 22,20 |
| Del Proyecto | 0,002 | 0,015 | 0,001 | 0,007 |
| Proyectada en el sector | 40,802 | 67,715 | 8,501 | 22,207 |

**Tabla 13.: Proyección de la concentración en la EMRP Club Deportivo 23 de Marzo.****

| Concentración<br>(μg/m3) | MP<br>10 | Col3 | MP<br>2,5 | Col5 |
| --- | --- | --- | --- | --- |
| **Concentración**<br>**(μg/m3)** | **Promedio**<br>**anual** | **Promedio 24**<br>**horas** | **Promedio**<br>**anual** | **Promedio 24**<br>**horas** |
| Basal | 39,30 | 62,50 | 7,00 | 41,20 |
| Del Proyecto | 0,004 | 0,031 | 0,002 | 0,015 |
| Proyectada en el sector | 39,304 | 62,531 | 7,002 | 41,215 |

**Tabla 14.: Proyección de la concentración en la EMRP Centro.****

| Concentración<br>(μg/m3) | MP<br>10 | Col3 | MP<br>2,5 | Col5 |
| --- | --- | --- | --- | --- |
| **Concentración**<br>**(μg/m3)** | **Promedio**<br>**anual** | **Promedio 24**<br>**horas** | **Promedio**<br>**anual** | **Promedio 24**<br>**horas** |
| Basal | 31,10 | 52,50 | 5,80 | 10,10 |
| Del Proyecto | 0,006 | 0,038 | 0,002 | 0,016 |

**Tabla 15.: Aporte a la concentración de MP Proyectos en la EMRP Colegio Pedro Vergara****

| Efecto Sinérgico | Col2 | Concentración (μg/m3) | Col4 | Col5 | Col6 |
| --- | --- | --- | --- | --- | --- |
| **Efecto Sinérgico** | **Efecto Sinérgico** | **MP10 ** | **MP10 ** | **MP2,5 ** | **MP2,5 ** |
| **Efecto Sinérgico** | **Efecto Sinérgico** | **Promedio**<br>**anual** | **Promedio**<br>**24 horas** | **Promedio**<br>**anual** | **Promedio**<br>**24 horas** |
| **Proyectos aprobados**<br>**ambientalmente en** | Parque fotovoltaico Verano de<br>San Juan I | 0,00112 | 0,00732 | 0,00050 | 0,00325 |
| **Proyectos aprobados**<br>**ambientalmente en** | Parque Eólico Calama | 0,00000 | 0,00000 | 0,00000 | 0,00000 |
| **Proyectos aprobados**<br>**ambientalmente en** | Línea de Transmisión 1x110 kV,<br>Planta Usya A Parque Eólico<br>Valle de los Vientos | 0,00700 | 0,04300 | 0,00600 | 0,00360 |
| **Proyectos aprobados**<br>**ambientalmente en** | Proyecto Fotovoltaico<br>Azabache | 0,01000 | 0,06000 | 0,00200 | 0,01000 |

**Tabla 16.: Aporte a la concentración de MP Proyectos en la EMRP Club Deportivo 23 de****

| Efecto Sinérgico | Col2 | Concentración (μg/m3) | Col4 | Col5 | Col6 |
| --- | --- | --- | --- | --- | --- |
| **Efecto Sinérgico** | **Efecto Sinérgico** | **MP10 ** | **MP10 ** | **MP2,5 ** | **MP2,5 ** |
| **Efecto Sinérgico** | **Efecto Sinérgico** | **Promedio**<br>**anual** | **Promedio**<br>**24 horas** | **Promedio**<br>**anual** | **Promedio**<br>**24 horas** |
| **Proyectos**<br>**aprobados** | Parque fotovoltaico Verano de<br>San Juan I | 0,00219 | 0,01350 | 0,00097 | 0,00593 |
| **Proyectos**<br>**aprobados** | Parque Eólico Calama | 0,00000 | 0,00000 | 0,00000 | 0,00000 |
| **Proyectos**<br>**aprobados** | Línea de Transmisión 1x110 kV,<br>Planta Usya A Parque Eólico<br>Valle de los Vientos | 0,02400 | 0,07600 | 0,00200 | 0,00680 |

**Tabla 17.: Aporte a la concentración de MP Proyectos en la EMRP Centro.****

| Efecto Sinérgico | Col2 | Concentración (μg/m3) | Col4 | Col5 | Col6 |
| --- | --- | --- | --- | --- | --- |
| **Efecto Sinérgico** | **Efecto Sinérgico** | **MP10 ** | **MP10 ** | **MP2,5 ** | **MP2,5 ** |
| **Efecto Sinérgico** | **Efecto Sinérgico** | **Promedio**<br>**anual** | **Promedio**<br>**24 horas** | **Promedio**<br>**anual** | **Promedio**<br>**24 horas** |
| **Proyectos**<br>**aprobados** | Parque fotovoltaico Verano de<br>San Juan I | 0,00167 | 0,00706 | 0,00074 | 0,00314 |
| **Proyectos**<br>**aprobados** | Parque Eólico Calama | 0,00000 | 0,00000 | 0,00000 | 0,00000 |
| **Proyectos**<br>**aprobados** | Línea de Transmisión 1x110 kV,<br>Planta Usya A Parque Eólico<br>Valle de los Vientos | 0,02800 | 0,09500 | 0,00240 | 0,00830 |
