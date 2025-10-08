---
title: Sin título
author: dss-mschulz
date: D:20170713164051-04'00'
language: es
type: report
pages: 75
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ANEXO 4.7 MODELACIÓN ATMOSFÉRICA DE EMISIONES DE MATERIAL PARTICULADO
-->

# ANEXO 4.7 MODELACIÓN ATMOSFÉRICA DE EMISIONES DE MATERIAL PARTICULADO

**JULIO 2017**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Nueva Providencia 1363, Of.1201,
(56.41)2287848 Providencia
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

**INDICE**

Página 2 de 75

**1** **INTRODUCCIÓN .................................................................................................... 5**

1.1 O BJETIVOS ...................................................................................................................................... 5

**2** **DESCRIPCIÓN DEL PROYECTO .............................................................................. 6**

**3** **ANTECEDENTES ..................................................................................................... 7**

3.1 G EOGRÁFICOS Y T OPOGRÁFICOS ......................................................................................................... 7

3.2 M ETEOROLOGÍA .............................................................................................................................. 8

3.3 M ARCO L EGAL R EGULATORIO ............................................................................................................. 9

_3.3.1_ _Contaminantes Atmosféricos .................................................................................................. 9_

3.4 E STADO DE LA C ALIDAD DEL A IRE EN LA CIUDAD DE C ORONEL ................................................................. 11

**4** **JUSTIFICACIÓN DE LOS MODELOS UTILIZADOS EN LA MODELACIÓN ............... 14**

4.1 U SO DEL M ODELO CALPUFF .......................................................................................................... 14

4.2 U SO DEL M ODELO W EATHER R ESEARCH AND F ORECASTING M ODEL (WRF) ............................................. 16

**5** **METODOLOGÍA.................................................................................................... 17**

5.1 M ODELACIÓN M ETEOROLÓGICA Y DE D ISPERSIÓN ................................................................................ 17

_5.1.1_ _Dominio de Modelación de Meteorológica .......................................................................... 17_

_5.1.2_ _Dominio de Modelación CALPUFF ......................................................................................... 18_

_5.1.3_ _Post Procesamiento de Información ..................................................................................... 19_

_5.1.4_ _Escenario de Modelación ...................................................................................................... 21_

**6** **RESULTADOS ...................................................................................................... 24**

6.1 C ARACTERIZACIÓN M ETEOROLÓGICA ................................................................................................. 24

_6.1.1_ _Caracterización de la velocidad y dirección de los vientos Anual y Estacional ..................... 24_

_6.1.2_ _Perfil diario de velocidad del viento ...................................................................................... 34_

_6.1.3_ _Caracterización de la Temperatura del Aire ......................................................................... 35_

_6.1.4_ _Caracterización de la Precipitación ....................................................................................... 38_

6.2 C ONCENTRACIONES M ODELADAS ...................................................................................................... 39

_6.2.1_ _Dispersión e Isoconcentración de Material Particulado, MP ................................................ 39_

_6.2.2_ _Dispersión e Isoconcentración de CO .................................................................................... 48_

_6.2.3_ _Dispersión e Isoconcentración de NO_ _2_ _.................................................................................. 56_

_6.2.4_ _Modelación discreta de las emisiones contaminantes ......................................................... 64_

_6.2.5_ _Aporte del proyecto a la concentración a la Estación de Monitoreo de Representatividad_

_Poblacional (ERMP)............................................................................................................................ 65_

_6.2.6_ _Análisis resultados meteorológicos ...................................................................................... 65_

_6.2.7_ _Análisis de los resultados de concentración de contaminantes en la atmósfera.................. 72_

**7** **CONCLUSIÓN ...................................................................................................... 74**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

**Índice de Tablas**

Página 3 de 75

Tabla 1. Valores normados para MP 10 y MP 2,5 en Chile ............................................................ 9

Tabla 2. Coordenadas del dominio de la modelación meteorológica ....................................... 17

Tabla 3. Coordenadas de los puntos receptores discretos del proyecto ................................... 19

Tabla 4. Coordenadas de las Estaciones de Monitoreo con Representatividad Poblacional ....... 20

Tabla 5. Emisiones generadas por la chimenea ..................................................................... 21

Tabla 6. Parámetros de salida de material particulado y gases de la Chimenea ....................... 22

Tabla 7. Coordenada Fuente Puntual - Chimenea.................................................................. 22

Tabla 8. Frecuencia de los vientos anuales, WRF. ................................................................. 24

Tabla 9. Frecuencia de los vientos verano, WRF. .................................................................. 27

Tabla 10. Frecuencia de los vientos otoño, WRF. .................................................................. 29

Tabla 11. Frecuencia de los vientos invierno, WRF. ............................................................... 31

Tabla 12. Frecuencia de los vientos en primavera, WRF. ....................................................... 33

Tabla 13. Concentración modelada en puntos receptores con respecto a MP, CO y NO x .......... 64

Tabla 14. Aumento de la concentración basal en la ERMP Coronel ......................................... 65

**Índice de Figuras**

Figura 1. Elevación del Terreno ............................................................................................. 7

Figura 2. Climograma comuna Coronel. .................................................................................. 8

Figura 3. Concentración promedio trianual de MP 10 en las Estaciones de Representatividad

Poblacional ......................................................................................................................... 11

Figura 4. Concentración promedio anual 24 horas de MP 10 en las Estaciones de Monitoreo de

Representatividad Poblacional ............................................................................................. 12

Figura 5. Concentración promedio trianual de MP 2,5 en la EMRP Nueva Libertad ...................... 13

Figura 6. Concentración promedio 24 horas de MP 2,5 en la EMRP Nueva Libertad .................... 13

Figura 7. Domino de la modelación de meteorológica, WRF ................................................... 18

Figura 8. Dominio de Modelación de CALPUFF ...................................................................... 19

Figura 9. Ubicación de receptores discretos en el área de estudio cercanos al proyecto ........... 20

Figura 10. Ubicación espacial de la fuente puntual - chimenea .............................................. 23

Figura 11. Rosa de los Vientos Anual, WRF. ......................................................................... 25

Figura 12. Frecuencia de los vientos, año 2014..................................................................... 26

Figura 13. Rosa de los Vientos Verano, WRF ........................................................................ 27

Figura 14. Frecuencia de los verano, año 2014 ..................................................................... 28

Figura 15. Rosa de los Vientos Otoño, WRF .......................................................................... 29

Figura 16. Frecuencia de los otoño, año 2014 ....................................................................... 30

Figura 17. Rosa de los Vientos Invierno, WRF....................................................................... 31

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

Página 4 de 75

Figura 18. Frecuencia de los invierno, año 2014 ................................................................... 32

Figura 19. Rosa de los Vientos Primavera, WRF .................................................................... 33

Figura 20. Frecuencia de los vientos en primavera, año 2014 ................................................ 34

Figura 21. Perfil diario de velocidad del viento, WRF año 2014 .............................................. 35

Figura 22. Temperatura Mensual en la WRF, año 2014 ......................................................... 36

Figura 23. Perfil vertical de la temperatura ........................................................................... 37

Figura 24. Perfil diario de temperatura, WRF, año 2014 ........................................................ 38

Figura 25. Precipitación mensual, WRF, año 2014 ................................................................. 39

Figura 26. Dispersión de la pluma de MP 10 como concentración promedio anual ..................... 41

Figura 27. Isoconcentración MP 10 como concentración promedio anual .................................. 43

Figura 28. Dispersión de la pluma de MP 10 como concentración promedio 24 horas ................ 46

Figura 29. Iso concentración MP 10 como concentración promedio 24 horas. ........................... 47

Figura 30. Dispersión de la pluma de CO como concentración promedio 8 horas ..................... 50

Figura 31. Iso concentración CO como concentración promedio 8 horas ................................. 51

Figura 32. Dispersión de la pluma de CO como concentración promedio horaria ..................... 54

Figura 33. Iso concentración CO como concentración promedio horaria ................................. 55

Figura 34. Dispersión de la pluma de NO 2 como concentración promedio anual ...................... 58

Figura 35. Iso concentración NO 2 como concentración promedio anual ................................... 59

Figura 36. Dispersión de la pluma de NO 2 como concentración promedio horario .................... 62

Figura 37. Iso concentración NO 2 como concentración promedio horario ................................ 63

Figura 38. Correlación entre temperaturas observadas y temperaturas modeladas .................. 67

Figura 39. Comparación entre la frecuencia de temperatura de los datos modelados y

observados......................................................................................................................... 68

Figura 40. Correlación entre velocidad del viento observadas y temperaturas modeladas ........ 69

Figura 41. Comparación entre la frecuencia de velocidad del viento de los datos modelados y

observados......................................................................................................................... 70

Figura 42. Correlación entre la dirección del viento observadas y temperaturas modeladas ..... 71

Figura 43. Comparación entre la frecuencia de velocidad del viento de los datos modelados y

observados......................................................................................................................... 72

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

**1** **Introducción**

Página 5 de 75

En el siguiente informe se presenta la modelación de las emisiones atmosféricas del

proyecto inmobiliario **“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”**, y su

cuantificación en términos de concentración, además de la presentación de los valores

de concentración con respecto a puntos receptores de interés y a la estación más

cercana de calidad del aire.

La modelación de las emisiones se realizó en base a la información presentada en el

Anexo 4.7 de Estimación de Emisiones, específicamente bajo las emisiones de la fase

de operación. Los resultados del informe de emisión permitió concluir que esta fase es

donde se alcanzan las más altas tasas de emisión de material particulado (MP) y gases

de combustión, debido al proceso de combustión de la chimenea, producto de los

gases de salida de la planta de producción de peróxido. A partir de esto además, se

considera que la modelación de emisiones se realizará a través de la modelación de la

fuente puntual (chimenea). Estás emisiones precisan de ser evaluadas en términos de

concentración, a fin de cuantificar su aporte a la línea base del territorio, ya que la

zona donde se emplaza el proyecto se define como zona latente de MP 10 y zona

saturada de MP 2,5 . La emisión total de la chimenea proyecta, para el año completo de

producción es de 0,11 ton/año de MP, 4,45 ton/año de NO x y 2,23 ton/año de CO.

La evaluación de la dispersión y concentración de las emisiones de material particulado

se realizó mediante el programa CALPUFF, el cual es un modelo de dispersión usado

ampliamente para simulaciones de concentraciones ambientales de las emisiones de

operaciones normales, con el objeto de establecer, desarrollar y analizar escenarios de

emisión y regulación. A su vez, el modelo utilizado para evaluar la meteorología y

terreno es el programa WRF. A su vez, CALPUFF y WRF son modelos recomendados

por el Ministerio de Medio Ambiente en la “Guía para el Uso de Modelos de Calidad del

Aire en el SEIA”, publicada el año 2012. Los resultados y el análisis de éstos se

presentan en el siguiente informe.

**1.1** **Objetivos**

El presente informe, tiene como objetivo general evaluar el efecto en la atmósfera

debido a las emisiones de contaminantes generadas por el proyecto Planta Peróxido de

Hidrógeno - Coronel, y cuantificar sus concentraciones.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

Para lo anterior se plantean los siguientes objetivos específicos:

Página 6 de 75

 Evaluar en términos de concentración, el alcance de las emisiones de MP, NO x y

CO en la atmósfera.

 Evaluar la concentración de MP, NO x y CO en receptores que actualmente se

encuentren cercanos al proyecto, así como en las estaciones cercanas de

calidad del aire.

**2** **Descripción del Proyecto**

El proyecto “Planta de Peróxido de Hidrógeno - Coronel”, consiste en la construcción y

operación de una planta de peróxido de hidrógeno cuya producción máxima equivale a

**66.000 toneladas por año**, lo que corresponde a una producción equivalente de

**186.916** kg/día en un año tipo, considerando un producto al 35%.

Esta planta constituye una modificación o complemento del proyecto “Terminal de

almacenamiento de peróxido de hidrógeno”, RCA No10/2008 del mismo titular,

actualmente en operación y emplazado en el sitio colindante al terreno donde se

proyecta la planta productora sometida a evaluación por la presente DIA.

La evaluación de la dispersión y concentración de las emisiones de material particulado

se realizó mediante el programa CALPUFF, el cual es un modelo de dispersión usado

ampliamente para simulaciones de concentraciones ambientales de las emisiones de

operaciones normales, con el objeto de establecer, desarrollar y analizar escenarios de

emisión y regulación. A su vez, es recomendado por el Ministerio de Medio Ambiente

en la “Guía para el Uso de Modelos de Calidad del Aire en el SEIA”, publicada el año

2012.

La estimación de emisiones, presentada en el Anexo 4.2 se realizó en base a la fase de

operación. Los resultados permitieron concluir que esta fase es donde se alcanzan las

más altas tasas de emisión, debido a la combustión de los calefactores, tanto a leña

como a pellets de madera. Estas emisiones precisan de ser evaluadas en términos de

concentraciones, a fin de evaluar su aporte a la línea base de concentraciones presente

en la zona saturada, en la cual se emplaza el proyecto.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

**3** **Antecedentes**

**3.1** **Geográficos y Topográficos**

Página 7 de 75

Coronel es una comuna y ciudad de Chile, perteneciente a la provincia de Concepción,

región del Biobío, ubicada a 30 km al sur del centro de la capital regional, teniendo

una superficie total de 279 km [2] . Coronel, junto con otras comunas, está enmarcada

dentro del área denominada como el Concepción Metropolitano. Los límites de esta

comuna se establecen de la siguiente manera:

 Limita al Norte con las comunas de San Pedro de la Paz, Chiguayante y

Hualqui;

 Al Sur, con las comunas de Lota y Santa Juana;

 Al Oriente, con la comuna de Hualqui;

 Al Poniente, con el océano Pacifico.

**Figura 1. Elevación del Terreno**

Fuente: Elaboración Propia en base a la información de elevación del terreno obtenida de las

base de la WebGIS - SRTM3 Shuttle Radar Topography Mission Global Coverage (~90m)

Version 2; S37W74

En la Figura 1 se muestra la elevación del terreno en Coronel, de donde se observa

que la superficie donde se emplaza el proyecto se encuentra prácticamente a nivel del

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

Página 8 de 75

mar, al igual que gran parte de las zonas contiguas, siendo considerado un terreno

llano. Al noreste se presentación una elevación prominente, producto de la aparición

de distintos cerros. En resumen, el sector de emplazamiento presenta una elevación

prácticamente constante y de baja altitud, además de pocas perturbaciones de relieve.

**3.2** **Meteorología**

El territorio de la comuna de Coronel se encuentra en el dominio del clima subtropical

o mediterráneo de costa occidental, con moderada amplitud térmica, actuando como

regulador térmico la proximidad con el Océano Pacífico. La temperatura media anual

alcanza los 13,1°C, variando desde los 16,9°C en promedio del mes con más oscilación

térmica (enero) y 9,6°C en promedio del mes con menos oscilación (julio). Ahora las

máximas y mínimas temperaturas promedios alcanzan los 23,5°C en marzo y 7,1°C en

el mes de junio, el mes más frío del año.

En Coronel, anualmente precipitan promedio 715,4 mm y se manifiesta que sus

mayores valores de precipitación se alcanzan los meses de junio y julio. En la Figura 2

se observa, la precipitación promedio estadística y las temperaturas medias, máximas y

mínimas para Coronel.

**Figura 2. Climograma comuna Coronel.**

Fuente: Elaboración propia en base a la climograma construido en base a la información

obtenida de los Anuarios Climatológicos de la Estación Carriel Sur de Concepción

correspondiente a la Dirección Meteorológica de Chile

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

**3.3** **Marco Legal Regulatorio**

**3.3.1** **Contaminantes Atmosféricos**

Página 9 de 75

Actualmente, los contaminantes MP 10 y MP 2,5 están regulados bajo normas de calidad

primaria, cuyo objetivo es proteger la salud de las personas de los efectos agudos y

crónicos de la exposición de estos contaminantes con un riesgo aceptable. Para esto,

se fijan límites de concentración permitidos, condiciones de superación de la norma y

los niveles que dan paso a situaciones de alerta, premergencia y emergencia

ambiental.

El material particulado grueso respirable MP 10 es regulado por el Decreto Supremo

(D.S.) 59/1998 del Ministerio Secretaría General de la Presidencia (MINSEGEPRES) y el

material particulado fino respirable MP 2,5 es regulado por del D.S. 12/2011 del

Ministerio del Medio Ambiente (MMA). En la siguiente tabla se ve una comparación

entre los valores del límite anual y diario para los contaminantes MP 10 y MP 2,5, además

de los rangos que dan origen a situaciones de alerta, preemergencia y emergencia

ambiental.

**Tabla 1. Valores normados para MP** **10** **y MP** **2,5** **en Chile**

|Nivel|MP (μg/m3)<br>10|MP (μg/m3)<br>2,5|
|---|---|---|
|Límite anual|50|20|
|Límite diario|150|50|
|Alerta|195 - 239|80 -109|
|Preemergencia|240 - 329|110 - 169|
|Emergencia|330 o mayor|170 o mayor|

Fuente: En base a D.S 59/1998 MINSEGEPRES y D.S. 12/2011 MMA

No obstante, la superación del límite normativo no es motivo de condiciones de

superación de la norma, sino que se considera que la norma es incumplida bajo ciertas

condiciones:

 Cuando el promedio de la concentración anual de tres años consecutivos sea

igual o supere los 50 μg/m [3] .

 Si el percentil 98 (P98) de las concentraciones de 24 horas durante un año sea

igual o superior a 150 μg/m [3] .

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

Página 10 de 75

 Si durante un año se registrasen siete o más días cuya concentración sea

mayor a 150 μg/m [3] .

En el mismo contexto, las condiciones de superación de la norma de MP 2,5 son las que

se describen a continuación:

 Cuando el promedio de la concentración anual de tres años consecutivos sea

igual o supere los 20 μg/m [3] .

 Si el percentil 98 (P98) de las 24 horas durante un año sea igual o superior a

50 μg/m [3] .

También, dentro de los contaminantes normados se encuentra el monóxido de carbono

(CO) mediante el D.S. 115/2002 del MINSEGEPRES, regulando la concentración

promedio de 1 a 8 horas. La norma establece como concentración promedio de 1 hora

26 ppmv, equivalente a 30 mg/m [3] N y como concentración promedio de 8 horas, un

límite de 9 ppmv, o sea 10 mg/m [3] N. No obstante, en ambos casos se considerará

sobrepasada la norma cuando el promedio de tres años sucesivos del percentil 99

(P99) de los máximos diarios registrados en un año calendario supere el límite de la

norma.

El óxido de nitrógeno (NO 2 ) es regulado por el D.S.114/2003 MINSEGEPRES

estableciendo la normativa de calidad primaria de calidad del aire en todo el territorio

nacional, estableciendo límites de concentración anual y horaria. Quedó establecido

como concentración anual de 53 ppbv, es decir, 100 μg/m [3] N y la concentración horaria

en 213 ppbv, o sea, 400 μg/m [3] N. No obstante, se considerará sobrepasada la norma

de calidad del aire para NO 2 anual cuando el promedio trianual supera el límite

establecido y/o cuando el promedio aritmético del percentil 99 de los máximos diarios

sobrepasa los 213 ppbv.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

**3.4** **Estado de la Calidad del Aire en la ciudad de Coronel**

Página 11 de 75

Bajo la figura legal del D.S. 41/2006 del MINSEGEPRES el Concepción Metropolitano,

compuesto por las comunas Lota, Coronel, San Pedro de la Paz, Hualqui, Chiguayante,

Concepción, Penco, Tomé, Talcahuano y Hualpen, fue declarado como zona latente por

las concentraciones 24 horas y anual de MP 10 .

En efecto, tal como se muestra en la Figura 3 la norma se encuentra por sobre el 80%

en las estaciones Consultorio San Vicente e Indura para el periodo 2012-2014; en el

siguiente periodo la concentración se encuentra sobre el 80% sólo en la estación

Consultorio San Vicente; la condición prevalece durante el periodo 2014-2016, además

se observa que la estación Inpesca también se encuentra sobre el 80% del límite

establecido como concentración promedio anual en la norma. En la figura, se hace

visible que la estación Nueva Libertad se encuentra sobre el límite normativo en todas

los periodos del año pero con una clara tendencia a la baja.

**Figura 3. Concentración promedio trianual de MP** **10** **en las Estaciones de**

**Representatividad Poblacional**

Nota: EC, Estación Consultorio San Vicente; EID, Estación Indura; EEP, Estación ENAP Price;

ENL, Estación Libertad; EJ, Estación JUNJI; EID, Estación Indura; EKC, Estación Kingston

College

Por su parte, la concentración 24 horas entre los años 2012 y 2016 no se encuentra

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

Página 12 de 75

superado el límite fijado para la concentración promedio de 24 horas en ninguna de las

estaciones, no obstante, ésta se encuentra sobre el 80% en el 2012 en la estación

Nueva Libertad situación que no se replica en los años siguientes, no obstante, en los

años 2015 y 2016 la concentración supera el 80% de la norma en las estaciones

Consultorio San Vicente e Inpesca. Esto se puede ver gráficamente en la siguiente

figura.

**Figura 4. Concentración promedio anual 24 horas de MP** **10** **en las Estaciones**

**de Monitoreo de Representatividad Poblacional**

NOTA: EC, Estación Consultorio San Vicente; EID, Estación Indura; EEP, Estación ENAP Price;

ENL, Estación Libertad; EJ, Estación JUNJI; EID, Estación Indura; EKC, Estación Kingston

College

En 2015, se declara Zona Saturada las comunas que conforman el Concepción

Metropolitano por la concentración promedio diaria de MP 2,5, según lo establecido en el

D.S. 15/2015 del MMA.

La disposición de datos de calidad del aire entre los años 2012 y 2016 es reducida, por

lo que el análisis de la concentración de MP 2,5 se realizó solo en base a los datos

existentes para la estación Nueva Libertad.

En la siguiente figura, se presenta la concentración promedio trianual entre el periodo

de análisis, en donde se observa que la concentración sólo supera el límite de la norma

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

Página 13 de 75

en el periodo 2012 - 2014 situación considerablemente inferior en los periodos

siguientes.

**Figura 5. Concentración promedio trianual de MP** **2,5** **en la EMRP Nueva**

**Libertad**

No obstante la situación es distinta para la concentración promedio 24 horas en la

misma estación, en donde se observa que para todos los años de estudio la

concentración registrada supera el límite establecido por la norma correspondiente.

**Figura 6. Concentración promedio 24 horas de MP** **2,5** **en la EMRP Nueva**

**Libertad**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

Página 14 de 75

**4** **Justificación de los Modelos Utilizados en la Modelación**

El Servicio de Evaluación Ambiental en la “Guía para el Uso de Modelos de Calidad del

Aire en el SEIA” (2012) establece una serie de **recomendaciones** para la modelación

de contaminantes primarios y secundarios en el aire.

En la actualidad, esta guía es el único documento existente como parámetro para la

modelación de calidad del aire y tiene como objetivo uniformar los criterios, exigencias

técnicas y antecedentes para la evaluación de los impactos asociados a este

componente de proyectos que ingresen al Servicio de Evaluación Ambiental. Dentro de

las **recomendaciones** de la guía está el uso del modelo de dispersión CALPUFF.

A continuación, se presenta una justificación de los modelos utilizados en la ejecución

de la modelación de dispersión y concentración de odorantes en el aire.

**4.1** **Uso del Modelo CALPUFF**

La modelación de la dispersión atmosférica de las emisiones de material particulado y

gases de combustión provenientes del proyecto, se realizó con un modelo tipo “Puff”,

específicamente el modelo CALPUFF.

Tal como lo define la Guía, los modelos tipo “puff” son una combinación entre los

modelos Gaussianos y los modelos Lagrangeanos, en el sentido de que esencialmente

calculan la dispersión de contaminantes provenientes de una emisión instantánea,

llamada “puff”, a lo largo de una trayectoria. Su aproximación matemática consiste en

estimar la dispersión en forma Gaussiana en cada punto de una trayectoria; es decir,

los modelos tipo “puff” sólo requieren una trayectoria por “puff”, lo que hace su cálculo

mucho más rápido. En el caso de emisiones continuas, se simulan las trayectorias y la

dispersión Gaussiana de muchos “puffs”, como es en el caso de las emisiones de

material particulado del proyecto. Al respecto, el modelo tipo “puff” recomendado por

la Guía es el modelo CALPUFF.

Así mismo, es un modelo completo que incorpora herramientas para procesar datos

meteorológicos y geofísicos, modelos de dispersión y pos procesamiento. Dicho modelo

es recomendado también por la Agencia de Protección Ambiental de los Estados

Unidos (EPA) para modelar transporte a larga distancia de contaminantes.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

CALPUFF se compone de tres módulos:

Página 15 de 75

 CALMET: Es un modelo meteorológico que desarrolla campos horarios de viento

y temperatura en una grilla de tres dimensiones. También asocia campos en

dos dimensiones de altura y usos de suelo. Este módulo puede ser reemplazado

por el **modelo matemático WRF, el cuál fue utilizado para este informe**,

además es recomendado por la guía antes citada.

 CALPUFF: Es un modelo de transporte y dispersión emitido desde fuentes

modeladas, simulando procesos de dispersión y transformación. CALPUFF utiliza

los datos generados por CALMET. Los archivos de salida de CALPUFF contienen

las concentraciones horarias o deposición por hora de flujos evaluados en

receptores seleccionados.

 CALPOST: Es usado para procesar aquellos archivos generados por CALMET y

CALPUFF, produciendo tabulaciones que resumen los resultados de la

simulación.

Ecuación del modelo CALPUFF

La ecuación básica que utiliza el modelo para realizar la modelación es la siguiente:

~~[~~

~~[]]~~ ~~[[]~~

[]]

]

⁄

∑

~~[~~

Dónde:

**C**, es concentración a nivel del suelo (g/m [3] ),

**Q**, es masa de contaminantes (g) en la nube.

**σ** **x** **,** es desviación estándar (m) de la distribución de Gauss en el viento a lo largo de la

dirección.

**σ** **y** **,** es desviación estándar (m) de la distribución de Gauss en el viento de costado

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

Página 16 de 75

**σ** **z**, es desviación estándar (m) de la distribución de Gauss en la dirección vertical.

**d** **a** **,** es distancia (m) del centro de la nube al receptor en la dirección del viento a lo

largo.

**d** **c**, es distancia (m) del centro de la nube al receptor en la dirección de viento cruzado.

**g**, es el término vertical (m) de la ecuación Gaussiana.

**H**, es la altura afectiva (m) desde el nivel del suelo del hojaldre.

**h**, es la altura (m) de la capa de mezcla.

Considerando las características del terreno, las distintas unidades geomorfológicas del

área de influencia del proyecto y el dominio de la modelación se consideró utilizar el

modelo CALPUFF para simular la dispersión de los contaminantes generados por la

operación futura del proyecto.

**4.2** **Uso del Modelo Weather Research and Forecasting Model (WRF)**

El modelo Weather Research and Forecasting (WRF), es un modelo numérico

recomendado para la generación de datos meteorológicos y uno de los modelos de

pronóstico meteorológicos más avanzados.

Debido a la falta de una red robusta de estaciones meteorológicas, la Guía para el Uso

de Modelos de Calidad del Aire en el SEIA recomienda el uso de WRF por sobre el uso

del CALMET. Además, el mismo documento, sugiere el uso del WRF para la modelación

de dispersión de contaminantes con CALPUFF.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

**5** **Metodología**

Página 17 de 75

La modelación de la dispersión del material particulado y los gases generados por la

combustión del proceso de generación del Hidrógeno, se realizó de acuerdo a la

siguiente metodología.

**5.1** **Modelación Meteorológica y de Dispersión**

Como se mencionó en el ítem 4 del presente informe, el modelo para simular la

meteorología y el de dispersión son WRF y CALPUFF respectivamente.

El modelo WRF es un simulador matemático temporal, que representa, a partir de

variables influyentes en la física de la atmósfera, las condiciones meteorológicas de un

dominio específico de modelación, que para el caso de este informe será presentado

en el ítem 5.1.1 el cual comprende el año 2014. A su vez, CALPUFF es un modelo

matemático que simula la dispersión de los contaminantes en relación a las variables

que influyen directamente sobre estos, como es el caso de la meteorología, aportada

por el modelo WRF. Estos modelos fueron utilizados para la modelación de la

meteorología y la dispersión de contaminantes del proyecto.

A continuación, se presenta la descripción de ambos, en términos de sus dominios.

**5.1.1** **Dominio de Modelación de Meteorológica**

El domino de la modelación meteorológica WRF, se extendió por toda la comuna de

Coronel (zona de emplazamiento del proyecto), además de abarcar una parte

importante del Concepción Metropolitano. De este modo, el dominio de la modelación

resulto ser de 62 km x 62 km de extensión, con una resolución de grilla de 1 km, tal

como se presenta en la Figura 7 y la Tabla 2.

**Tabla 2. Coordenadas del dominio de la modelación meteorológica**

|Vértice|Proyección UTM, Huso 18 Sur, Datum: WSG-84|Col3|
|---|---|---|
|**Vértice**|**Este (km)**|**Norte (km)**|
|Suroeste|639,530|5.896,829|
|Sureste|701,530|5.896,829|
|Noroeste|639,530|5.958,829|
|Noreste|701,530|5.958,829|
|Centroide|670,530|5.927,829|

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

Página 18 de 75

**Figura 7. Domino de la modelación de meteorológica, WRF**

Cabe destacar que la modelación fue realizada sobre 10 celdas de altura que van

desde los 0 a los 4.500 metros de altura. La altura de las celdas modeladas considera

un rango amplio para la variación diaria de la capa de mezcla.

**5.1.2** **Dominio de Modelación CALPUFF**

El dominio de la modelación de la dispersión de los contaminantes, CALPUFF, se

extiende en un área de 30 km x 30 km, la cual abarca la totalidad del área del

proyecto, la comuna de Coronel y parte del Concepción Metropolitano. Es importante

destacar que la extensión del dominio de modelación de la dispersión (pluma) es

menor al domino de la modelación meteorológica, e incluye zonas de poca o nula

densidad poblacional.

El dominio de CALPUFF se escogió en consideración de los potenciales puntos

receptores y las estaciones de monitoreo con representatividad poblacional (EMRP)

que se encuentran en las ciudades cercanas al proyecto y que podría recibir el aporte

del proyecto a la condiciones atmosféricas, en cuanto de cantidad y dispersión de

contaminantes. El dominio en cuestión se presenta en la Figura 8.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

**Figura 8. Dominio de Modelación de CALPUFF**

Página 19 de 75

Cabe destacar que el modelo CALPUFF es alimentado con las salidas del modelo

meteorológico WRF y los valores de emisión ingresados en base a lo estipulado en el

ítem 5.1.4.

**5.1.3** **Post Procesamiento de Información**

Para analizar el alcance de las concentraciones con respecto a la calidad del aire en

receptores específicos, se realizó una modelación discreta, con el fin de obtener la

concentración en el aire de puntos y alturas seleccionadas del área de estudio.

A continuación, se presenta la ubicación y coordenadas de los receptores discretos

utilizados en la modelación. Los receptores identificados corresponden a unidades

habitacionales y puntos de trabajo dentro del área de modelación; las cuales algunas

se encuentran en la cercanías del proyecto. La información antes mencionada se

presenta en la Tabla 3 y la Figura 9.

**Tabla 3. Coordenadas de los puntos receptores discretos del proyecto**

|Receptor|UTM, Huso 18 S, WGS-84|Col3|Distancia al<br>proyecto (m)|
|---|---|---|---|
|**Receptor**|**Este (km)**|**Norte (km)**|**Norte (km)**|
|P1|662,892|5.905,951|36,78|
|P2|663,025|5.905,944|170,00|

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

Página 20 de 75

|Receptor|UTM, Huso 18 S, WGS-84|Col3|Distancia al<br>proyecto (m)|
|---|---|---|---|
|**Receptor**|**Este (km)**|**Norte (km)**|**Norte (km)**|
|P3|662,587|5.905,938|126,62|
|P4|662,953|5.905,827|154,80|
|P5|663,193|5.905,830|362,00|
|P6|662,749|5.905,838|119,20|
|P7|662,714|5.906,212|121,20|
|P8|662,867|5.906,258|107,60|
|P9|663,185|5.906,063|271,80|
|P10|663,170|5.905,677|412,90|

**Figura 9. Ubicación de receptores discretos en el área de estudio cercanos al**

**proyecto**

Otro punto importante a considerar, es la medición -cuantitativa de la concentración en

las estaciones de monitoreo de Calidad del Aire. Para el presente análisis se utilizarán

los datos de la estación Coronel del Sistema de Información de Calidad del Aire

(SINCA), que se encuentra ubicada en las coordenadas presentes en la Tabla 4, a una

distancia no superior de 7 km del proyecto.

**Tabla 4. Coordenadas de las Estaciones de Monitoreo con Representatividad**

**Poblacional**

|Receptor|UTM, Huso 18 S, WGS-84|Col3|Col4|Col5|Distancia al<br>proyecto (m)|
|---|---|---|---|---|---|
|**Receptor**|**Este (km)**|**Este (km)**|**Norte (km)**|**Norte (km)**|**Norte (km)**|
|Coronel|665,556|665,556|5.899,980|5.899,980|6.490,0|
|||~~**Concepción**~~<br>~~**Chile**~~<br>Los Pensamientos 197, San Pedro de la Paz<br>(56.41)2287848<br>www.dss.cl|~~**Concepción**~~<br>~~**Chile**~~<br>Los Pensamientos 197, San Pedro de la Paz<br>(56.41)2287848<br>www.dss.cl|~~**Santiago**~~<br>~~**Chile**~~<br>Av. Del Valle Sur 512, Of.304,<br>Huechuraba<br>(56.2)23494104|~~**Santiago**~~<br>~~**Chile**~~<br>Av. Del Valle Sur 512, Of.304,<br>Huechuraba<br>(56.2)23494104|

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

**5.1.4** **Escenario de Modelación**

Página 21 de 75

El escenario de modelación de partículas se realizó en base a los resultados obtenidos

de la estimación de emisiones atmosféricas, cuyos detalles se encuentran en el Anexo

4.2. Estimación de Emisiones Atmosféricas de la presente Declaración de Impacto

Ambiental. El resultado de esta estimación de emisiones atmosféricas de material

particulado y gases de combustión (CO, NO x ), sugiere que el año de más alta tasa de

emisión directa, es el periodo en el cual la planta se encuentra operativa, en este caso

y por término de tiempo, corresponderá al tercer año de estimación de emisiones, ya

que este considera un año completo de operación. Las emisiones se presentan en la

siguiente tabla.

**Tabla 5. Emisiones generadas por la chimenea**

|Contaminantes|Emisión (ton/año)|
|---|---|
|MP|0,110|
|NOx|4,452|
|CO|2,226|

Tal como se mencionó en la Tabla 5 las emisiones son generadas por la Chimenea de

la planta productiva de peróxido de hidrógeno. En esta chimenea se combustionan los

gases generados en el horno de producción de Hidrógeno (unidad SMR) y que son

utilizados para la generar vapor en el proceso, siendo su última etapa la quema de

estos en la Chimenea, con el fin de minimizar los agentes contaminantes al ambiente,

oxidando los compuestos orgánicos a su ultima estado (CO 2 ). Cabe destacar que no se

consideran emisiones de compuestos sulfatados debido a que el gas natural, utilizado

tanto en el proceso como para la quema en el horno, es pretratado para eliminar el

azufre que contiene.

Por ende, tal como se presenta, las emisiones de material particulado (MP), CO y NO x

son emitidas por una fuente puntual, por lo cual se modelará la dispersión de los

contaminantes solo en referencia a una fuente puntual. En este sentido, en la Tabla 6

se presentan los detalles de la chimenea, como datos de entrada, para ser modelada

como fuente puntual en el programa CALPUFF.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

Página 22 de 75

**Tabla 6. Parámetros de salida de material particulado y gases de la**

**Chimenea** **[1]**

|Ítem|Valor|Unidad|
|---|---|---|
|Altura del punto de<br>descarga de los gases|23,8|m|
|Temperatura Salida Gases|195|°C|
|Diámetro de ducto de<br>salida de los gases|23,8|m|
|Velocidad Escape Gases|10,0|m/s|

Por otro lado, la estimación y modelación de las emisiones de contaminantes se realizó

teniendo en cuenta la escala temporal de la operación. Esta escala comprende los

meses de enero a diciembre, en un horario continuo desde las 00:00 a las 23:59, a lo

largo de 355 días al año. Esta inclusión se realiza con objeto de ser más prolijos en la

modelación, sobre todo por la influencia que podría tener sobre el promedio horario.

Esta fuente se ubicará en la zona de la unidad del SMR, encargada de la producción de

Hidrógeno para el proceso. Las coordenadas representativas de la chimenea se

presentan en la Tabla 7 y Figura 10.

**Tabla 7. Coordenada Fuente Puntual - Chimenea**

|Fuente de Emisión|UTM, Huso 18 S, WGS-84|Col3|
|---|---|---|
|**Fuente de Emisión**|**Este (km)**|**Norte (km)**|
|Chimenea|662,807|5.906,019|

1 SMR Memorial Técnico Peróxido de Hidrógeno Solvay, TC 15-06-16

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

Página 23 de 75

**Figura 10. Ubicación espacial de la fuente puntual - chimenea**

Si bien las emisiones directas de material particulado son menores a las generadas en

la fase de construcción (0,188 ton/año), contienen emisiones muchas veces más alta

de CO y NOx, siendo este un parámetro de determinación para modelar este

escenario. Además, se agrega el hecho que las emisiones máximas de construcción

solo se darán el primer año, en cambio la emisión de la chimenea será por toda la vida

útil de la planta, estimada en 30 años.

Por último, las concentraciones obtenidas a partir de las emisiones antes mencionadas,

serán analizadas en relación a puntos receptores de interés, tal es el caso de viviendas

cercanas o sitios laborales y con respecto a EMRP, con el objeto de poder cuantificar

su aporte de contaminantes sobre éstos.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

**6** **Resultados**

**6.1** **Caracterización Meteorológica**

Página 24 de 75

**6.1.1** **Caracterización de la velocidad y dirección de los vientos Anual y**

**Estacional**

En la Figura 11 se presenta la rosa de vientos anual, construida en base a los datos

generados con el modelo WRF para el año 2014. Los resultados indican que el modelo

a simulado frecuencias mayores para vientos cuyos origen se tienen lugar en la

componente sur (S) y sursuroeste (SSO), representando el 17 y 31%,

respectivamente; ambas componentes están regidas por vientos entre los superiores o

iguales a 6,7 m/s e inferiores a 12,9 m/s. También se observan frecuencias menores

en otras componentes como suroeste (SO) y norte (N) con un 9% en la frecuencia

total sobre los vientos anuales simulados. De ésta forma, el vector resultante

representa el 41% de los vientos simulados con origen en los 217° con lo que se

espera que, en general durante el año los vientos desplacen las masas de aire en

sentido noreste.

En la siguiente tabla se muestra la frecuencia de vientos por componente de origen, de

donde se observa la frecuencia de los vientos simulados por el modelo WRF.

**Tabla 8. Frecuencia de los vientos anuales, WRF.**

|Componente|Col2|Total|
|---|---|---|
|Norte|N|786|
|Nord noreste|NNE|464|
|Noreste|NE|128|
|Este noreste|ENE|48|
|Este|E|36|
|Este Sureste|ESE|89|
|Sureste|SE|163|
|Sur sureste|SSE|287|
|Sur|S|1513|
|Sur suroeste|SSO|2741|
|Suroeste|SO|746|
|Oeste suroeste|OSO|257|
|Oeste|O|264|
|Oeste noroeste|ONO|290|
|Noroeste|NO|369|

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

Página 25 de 75

|Componente|Col2|Total|
|---|---|---|
|Norte noroeste|NNO|551|
|Sub total|Sub total|8732|
|Calmas|Calmas|25|
|Total<br>|Total<br>|8757<br>|

Nota: Las filas sombreadas en celeste son las componentes que se simulan máximas

frecuencias.

**Figura 11. Rosa de los Vientos Anual, WRF.**

Los resultados de la simulación meteorológica sobre el área de estudio han

caracterizado una zona en donde los vientos son de alta magnitud, propios de las

zonas costeras en donde las condiciones de ventilación son favorables y en donde

además existiría un bajo porcentaje de vientos calmos, es decir aquellos inferiores a

0,5 m/s.

En este contexto, la Figura 12 muestra la frecuencia de los vientos en las distintas

categorías de velocidad del viento, donde es evidente que los vientos son más

frecuentes entre los 3.6 y 6,7 m/s representando el 31,5% de los vientos, siendo

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

Página 26 de 75

también importantes los vientos entre los 6,7 - 9,7 m/s y 9,1 - 12,9 m/s constituyendo

el 26,8 y 23,6% de los vientos simulados, respectivamente. Además, se observa un

bajo porcentaje de calmas, de tan sólo el 0,3% de los vientos y un 3,3% de vientos

cuya magnitud fuera mayor o igual a los 12,9 m/s.

**Figura 12. Frecuencia de los vientos, año 2014**

**6.1.1.1** **Dirección y velocidad de vientos predominantes en verano**

En la Figura 13, se ve la rosa de los vientos para los meses de verano, en donde se

observa que mayormente los vientos tienen origen entre las componentes sursuroeste

representando el 48% de los vientos simulados, además de aquellos que se originan

en la componente sur (S) y suroeste (SO) representando el 17 y 12%

respectivamente; mientras que el resto de las componentes tendría una ocurrencia

menor. Como resultado, es espera que el vector resultante tenga lugar en los 208° y

que por consiguiente el desplazamiento de las masas de aire sea hacia el nornordeste.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

**Figura 13. Rosa de los Vientos Verano, WRF**

Página 27 de 75

En la siguiente tabla se muestra la frecuencia de vientos por cada componente de

origen, de donde se observa la frecuencia de los vientos simulados por el modelo WRF.

**Tabla 9. Frecuencia de los vientos verano, WRF.**

|Componente|Col2|Total|
|---|---|---|
|Norte|N|63|
|Nord noreste|NNE|51|
|Noreste|NE|19|
|Este noreste|ENE|12|
|Este|E|7|
|Este Sureste|ESE|4|
|Sureste|SE|9|
|Sur sureste|SSE|34|
|Sur|S|374|
|Sur suroeste|SSO|1040|
|Suroeste|SO|261|
|Oeste suroeste|OSO|69|

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

Página 28 de 75

|Componente|Col2|Total|
|---|---|---|
|Oeste|O|44|
|Oeste noroeste|ONO|36|
|Noroeste|NO|48|
|Norte noroeste|NNO|261|
|Calmas|Calmas|7|

Nota: Las filas sombreadas en celeste son las componentes que registran máximas frecuencias.

El modelo simuló vientos de magnitud superiores a los 3,6 m/s, lo cual presume

condiciones de ventilación favorable durante ésta estación, sobre todo considerando

que el porcentaje de vientos calmos sólo constituye el 0,3% de los vientos simulados.

Específicamente, durante ésta estación los vientos entre los 3,6-6,7; 6,7-9,1 y 9,1-12,9

m/s tendría frecuencias cercanas al 28%, tal como se puede ver en la Figura 14.

**Figura 14. Frecuencia de los verano, año 2014**

**6.1.1.2** **Dirección y velocidad de vientos predominantes en otoño**

En la Figura 15 se presenta la rosa de los vientos durante los meses de otoño, en ella

se puede observar que los vientos más frecuentemente simulados tendrían su origen

en la componente sursuroeste, sur y norte, con una representatividad del 22, 14 y

16%, respectivamente. Como resultado de esto, el vector resultante tendría lugar en

los 245° y por lo tanto el desplazamiento de la masa de los vientos en ésta estación

sería hacia el noreste.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

**Figura 15. Rosa de los Vientos Otoño, WRF**

Página 29 de 75

En la Tabla 10, se ve la frecuencia de los origen de los vientos en el mes de otoño

simulada por el modelo WRF.

**Tabla 10. Frecuencia de los vientos otoño, WRF.**

|Componente|Col2|Total|
|---|---|---|
|Norte|N|360|
|Nord noreste|NNE|154|
|Noreste|NE|45|
|Este noreste|ENE|14|
|Este|E|13|
|Este Sureste|ESE|38|
|Sureste|SE|60|
|Sur sureste|SSE|89|
|Sur|S|300|

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

Página 30 de 75

|Componente|Col2|Total|
|---|---|---|
|Sur suroeste|SSO|486|
|Suroeste|SO|137|
|Oeste suroeste|OSO|49|
|Oeste|O|80|
|Oeste noroeste|ONO|87|
|Noroeste|NO|110|
|Norte noroeste|NNO|178|
|Calmas<br>|Calmas<br>|8 <br>|

Nota: Las filas sombreadas en celeste son las componentes que registran máximas frecuencias.

En relación a la magnitud de los vientos, se observa que durante ésta estación la

frecuencia de los vientos es menor para categorías superiores a los 6,7 m/s en

comparación con la estación anterior, no obstante, las condiciones de ventilación serían

favorables ya que el porcentaje de vientos calmos sería de apenas el 0,4% de los

vientos totales, mientras que aquellos entre los 3,6 y 6,7 m/s representarían el 33,3%

de los vientos de la estación, tal como se muestra en la Figura 16.

**Figura 16. Frecuencia de los otoño, año 2014**

**6.1.1.3** **Dirección y velocidad de vientos predominantes en invierno**

En Figura 17 se observa la rosa de los vientos simulada para el invierno por el modelo

WRF para el año 2014, la que en comparación con las otras estaciones tendría una

participación mayor de otras componentes de origen de viento. En efecto, se observa

que los vientos provienen en un 19% de la componente sur, un 16% del sursuroeste,

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

14% desde el norte y 11% desde el nornoreste.

**Figura 17. Rosa de los Vientos Invierno, WRF**

Página 31 de 75

En la Tabla 11 se muestra la frecuencia de los vientos simulados por el modelo WRF

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

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

Página 32 de 75

|Componente|Col2|Total|
|---|---|---|
|Sur suroeste|SSO|362|
|Suroeste|SO|75|
|Oeste suroeste|OSO|41|
|Oeste|O|55|
|Oeste noroeste|ONO|81|
|Noroeste|NO|127|
|Norte noroeste|NNO|200|
|Calmas|Calmas|7|

Nota: Las filas sombreadas en celeste son las componentes que registran máximas frecuencias.

En la Figura 18, se observa la frecuencia de los vientos simulados por el modelo

meteorológico, de donde se puede observar un bajo porcentaje de calmas, alcanzando

sólo el 0,3% de los vientos simulados en invierno. Respecto a las otras categorías de

vientos, se observa que son más frecuentes entre los 3,6 y 6,7 m/s, representando el

33,0% de los vientos totales en la estación.

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
||||||2,8|
|0,3||||||

Calmas 0.5-3.6 3.6-6.7 6.7-9.1 9.1-12.9 >=12.9

Frecuencia de Velocidad del Viento en Invierno

**Figura 18. Frecuencia de los invierno, año 2014**

**6.1.1.4** **Dirección y velocidad de vientos predominantes en primavera**

En la Figura 19 se observa la rosa de los vientos durante la primavera simulados por el

modelo WRF. La máxima frecuencia de vientos tienen origen en la componente

sursuroeste (SSO) alcanzando los 39%, mientras que el 19% de los vientos tienen

origen en el sur (S) y el 13% de los vientos se originan en el suroeste (SO); mientras

que las otras componentes tendrían una frecuencia considerablemente menor. Además

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

Página 33 de 75

se puede apreciar que el componente resultante tendría lugar en los 213° con una

representatividad del 70% de los vientos y por consiguiente el desplazamiento de las

masas de aire sería hacia el noreste.

**Figura 19. Rosa de los Vientos Primavera, WRF**

En la Tabla 12 se muestra la frecuencia de vientos por componente de origen, de

donde se observa la frecuencia de los vientos simulados por el modelo WRF.

**Tabla 12. Frecuencia de los vientos en primavera, WRF.**

|Componente|Col2|Total|
|---|---|---|
|Norte|N|57|
|Nord noreste|NNE|24|
|Noreste|NE|1|
|Este noreste|ENE|7|
|Este|E|2|
|Este Sureste|ESE|11|

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

Página 34 de 75

|Componente|Col2|Total|
|---|---|---|
|Sureste|SE|28|
|Sur sureste|SSE|58|
|Sur|S|420|
|Sur suroeste|SSO|853|
|Suroeste|SO|273|
|Oeste suroeste|OSO|98|
|Oeste|O|85|
|Oeste noroeste|ONO|86|
|Noroeste|NO|84|
|Norte noroeste|NNO|94|
|Calmas<br>|Calmas<br>|3 <br>|

Nota: Las filas sombreadas en celeste son las componentes que registran máximas frecuencias.

Por otro lado, la rosa de los vientos demuestra que existe una prevalencia de la

velocidad de los vientos entre los 3,6 - 6,7 m/s, representando el 31,7% de la

velocidad del viento simulados por el WRF en primavera en el año 2014, también son

frecuentes los vientos entre los 6,7-9,1 m/s y los 9,1 - 12,9 m/s con un 26,9 y 25,5%

de los vientos totales simulados para la estación. Además tal como se ve Figura 20 el

porcentaje de calmas es de sólo el 0,1%.

**Figura 20. Frecuencia de los vientos en primavera, año 2014**

**6.1.2** **Perfil diario de velocidad del viento**

En la Figura 21, se observa el perfil de la velocidad del viento simulado por el modelo

meteorológico.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

Página 35 de 75

**Figura 21. Perfil diario de velocidad del viento, WRF año 2014**

Los resultados evidencian que es durante el verano cuando la velocidad del viento es

mayor, sobre todo en las tardes entre las 15:00 y 20:00 horas en donde la velocidad

del viento es superior a 8 m/s; de forma similar, en primavera la diferencia entre las

velocidades mayores y menores es inferior a las simuladas en verano, en donde las

velocidades más altas son cercanas a los 8 m/s entre el mismo rango de hora. Durante

los meses de otoño e invierno, la velocidad del viento es inferior a las estaciones

anteriores; de hecho, durante los meses de otoño la velocidad del viento es incluso

inferior a la media aunque con una tendencia similar, en donde las velocidades son

mayores entre las 16:00 y 20:00 horas donde la velocidad excede los 6,5 m/s; durante

los meses de invierno la velocidad es más fluctuante, tanto que no se observan

momentos del día en donde el viento sea particularmente mayor.

**6.1.3** **Caracterización de la Temperatura del Aire**

**6.1.3.1** **Temperatura Diaria Mensual**

En la Figura 22, se presenta la temperatura media mensual simulada por el WRF para

cada mes del 2014, además de las temperaturas máximas y mínimas para cada mes.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

Página 36 de 75

**Figura 22. Temperatura Mensual en la WRF, año 2014**

Se observa que la temperatura promedio anual va disminuyendo paulatinamente en los

meses de otoño para alcanzar las temperaturas más bajas en invierno para

posteriormente aumentar hacia fin de año con la llegada de la primavera.

En éste caso la temperatura promedio mensual más alta fue simulada en febrero con

15,6°C, alcanzando máximas de 17,1°C y mínimas de 13,7°C. Por su parte, la

temperatura promedio mínima fue simulada en los meses agosto, julio y septiembre

con temperaturas de 11,6 y 11,8°C respectivamente, entre éstos meses la mayor

amplitud térmica ocurriría en el mes de julio donde la mínima alcanzaría los 8,1°C y la

máxima 14,3°C. No obstante, entre todos los meses del año, la máxima amplitud

térmica ocurre en el mes de junio con una temperatura mínima promedio de 7,7°C y

máxima promedio de 15,1°C.

**6.1.3.2** **Perfil Vertical de la Temperatura**

En la Figura 23 se observa el perfil vertical de la temperatura para cada mes del año.

Esta ofrece una visión de la variación de la temperatura respecto la altura, la gráfica de

éstas variables entrega información sobre meses o momentos del año en donde

pudieran suscitarse episodios de inversión térmica.

La inversión térmica se relaciona estrechamente con contaminación atmosférica, pues

cuando se suscitan esto episodios, la dispersión de contaminantes disminuye y por

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

Página 37 de 75

consiguiente las concentraciones de contaminantes aumentan. En éste caso, el modelo

WRF, no simuló episodios de inversión térmica, por lo cual se presumen condiciones

favorables para dispersión de contaminantes.

**Figura 23. Perfil vertical de la temperatura**

**6.1.3.3** **Perfil diario de la Temperatura**

La simulación del modelo meteorológico WRF dentro del área de estudio de las

temperaturas horarias, demuestran un comportamiento similar en todas las estaciones

del año. En efecto, tal como se muestra en la Figura 24, la evolución de la temperatura

diaria resulta tener una leve diminución entre las 00:00 y 08:00 horas, a partir de

entonces la temperatura aumenta hasta alcanzar las temperaturas más altas ente las

16 y 18°C para disminuir levemente hacia el fin del día.

Además, se hace visible que en todas las estaciones la amplitud térmica es baja

llegando a sólo una diferencia promedio de 0,5°C, siendo levemente mayor en

primavera.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

Página 38 de 75

**Figura 24. Perfil diario de temperatura, WRF, año 2014**

**6.1.4** **Caracterización de la Precipitación**

Según los resultados de la simulación meteorológica del modelo WRF, concluyen que

en el año 2014, la precipitación en la zona de estudio alcanzó los 1.212 mm/año. En la

Figura 25, se muestra la precipitación mensual para el año 2014 donde se observa que

durante todo el año se simularon eventos de precipitación siendo menor en los meses

de febrero y diciembre; y mayores en los meses junio y julio en donde precipita el 51%

del total anual simulado, además de los meses agosto y septiembre en donde precipita

el 26%.

Para efectos de la modelación, la precipitación juega un rol importante en la remoción

de material particulado en el aire, representando un medio de remoción de éste

natural denominado deposición húmeda.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

Página 39 de 75

350

300

250

200

150

100

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

0

50

|Col1|Col2|Col3|Col4|Col5|327|Col7|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||293||||||
|||||||||||||
|||||||||||||
|||||123|||164|148||||
|||||||||||||
|||47|43||||||26|||
|10|4|||||||||17|9|

Ene Feb Mar Abr May Jun Jul Ago Sep Oct Nov Dic

**Mes**

**Figura 25. Precipitación mensual, WRF, año 2014**

**6.2** **Concentraciones Modeladas**

A continuación, se presentan los resultados de la modelación de material particulado

(MP), monóxido de carbono (CO) y dióxido de nitrógeno (NO 2 ) emitidos a la atmósfera.

Como datos de ingreso para la modelación de los contaminantes fueron utilizadas las

emisiones extraídas de la fase de operación del proyecto, específicamente de la

Chimenea de salida de los gases de combustión; datos presentes en el Anexo 4.2.1 de

Estimación de Emisiones Atmosféricas.

**6.2.1** **Dispersión e Isoconcentración de Material Particulado, MP**

A continuación, se presenta el análisis de los resultados de las concentraciones de

material particulado tanto como promedio anual como 24 horas.

Cabe destacar que el análisis se realizará en términos de material particulado total, tal

como se presentó en el Anexo 4.2 de la Estimación de Emisiones, por ende este

análisis es la cota máxima para el Material Particulado Grueso (MP 10 ) y Material

Particulado Fino (MP 2,5 ), por ende, **para términos prácticos se considerará los**

**valores y análisis a continuación presentados como MP** **10** y por un factor menor

a la unidad para el MP 2,5, ya que este último se encuentra contenido en el MP 10 .

Es importante señalar que la pluma de dispersión del material particulado simulada por

el modelo abarca principalmente la zona de emplazamiento del proyecto y parte de las

unidades habitacionales cercanas e industrias contiguas al proyecto. Se observa que

las máximas concentraciones se alcanzan en la cercanía de la planta, comportamiento

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

habitual en la modelación de fuentes puntuales.

**6.2.1.1** **Concentración Promedio Anual de MP** **10**

Página 40 de 75

En Figura 26 se muestra la pluma de dispersión de la concertación promedio anual de

MP 10, de donde se concluye lo siguiente:

 Los vientos simulados por el modelo WRF influyen en la pluma de dispersión,

ya que tal como se presentó en el análisis de éstos (ítem 6.1.1) su componente

predominante es de sur o suroeste por ende, generarían un transporte hacia el

norte o noreste, comportamiento previsto por la simulación. A la vez, estos

vientos modelados, tiene una velocidad relativamente alta, con una frecuencia

predominante entre velocidad de 3 a 12 m/s, lo cual también se refleja en la

pluma y en su radio de dispersión.

 Tal como se mencionó en la ítem 5.1.4, las emisiones directas estimadas se

cuantifican en 0,110 ton/año, las que generarán una concentración máxima

promedio anual de 0,0032 μg/m [3] . Esta concentración, se genera fuera del área

del proyecto, comportamiento típico de las fuentes puntuales.

 Si bien, y tal como se presenta en la Figura 26, los puntos discretos se

encuentran inmersos dentro de la pluma de dispersión, los valores de

concentración son tan bajos que llegan a ser despreciables. Además, se

considera la alta dispersión del punto donde se emplaza la fuente puntual y la

altura a la cual son emitidas estas partículas, que es a más de 24 metros (ver

Tabla 7). Los puntos discretos 5 y 10 corresponden a los únicos puntos de

unidades habitacionales, y tal como muestra la figura, la pluma de dispersión

no tiene ese sentida, tal que casi es incidental su presencia en esos puntos.

 Cabe destacar que esta concentración corresponde al promedio aritmético entre

los 0 y 20 metros sobre la elevación del terreno, correspondiente a la primera

celda de modelación vertical; entre las celdas horizontales de 1 km x 1 km.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

**Figura 26. Dispersión de la pluma de MP** **10** **como concentración promedio anual**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Nueva Providencia 1363, Of.1201,
(56.41)2287848 Providencia
www.dss.cl (56.2)23494104

En la Figura 27, se muestra el mapa de isoconcentración, de donde se puede concluir

que:

 El área de estudio es acotada a 173,2 hectáreas, debido a que luego de esta

superficie los valores de concentración son prácticamente nulos. Esta área

cubre principalmente el emplazamiento del proyecto. De todas formas, las

concentraciones son bajas por las razones planteadas en el punto anterior.

 - Las máximas concentraciones fluctúan entre los 0,0026 y 0,0032 μg/m [3] y

abarcan un área de 15,2 hectáreas, la cual se encuentra a una distancia no

mayor de 100 metros hacia el norte de la zona de emplazamiento del proyecto.

 Al avanzar cerca 1.500 m desde la zona de mayores emisiones del proyecto, las

concentraciones alcanzan la mitad de la concentración máxima promedio anual.

 Tal como se ha presentado, el impacto es prácticamente nulo en las cercanías

del proyecto, debido a las condiciones de liberación del material particulado.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Nueva Providencia 1363, Of.1201,
(56.41)2287848 Providencia
www.dss.cl (56.2)23494104

**Figura 27. Isoconcentración MP** **10** **como concentración promedio anual**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Nueva Providencia 1363, Of.1201,
(56.41)2287848 Providencia
www.dss.cl (56.2)23494104

**6.2.1.2** **Concentración Promedio 24 horas de MP** **10**

En la Figura 28 se muestra la pluma de dispersión de la concentración promedio 24

horas de MP 10, de donde se concluye lo siguiente:

 Los vientos simulados por el modelo WRF influyen en la pluma de dispersión,

ya que tal como se presentó en el análisis de éstos (ítem 6.1.1) su componente

predominante es de sur o suroeste por ende, generarían un transporte hacia el

norte o noreste, comportamiento previsto por la simulación. A la vez, estos

vientos modelados, tiene una velocidad relativamente alta, con una frecuencia

predominante entre velocidad de 3 a 12 m/s, lo cual también se refleja en la

pluma y en su radio de dispersión.

 Tal como se mencionó en la ítem 5.1.4, las emisiones directas estimadas se

cuantifican en 0,110 ton/año, las que generarán una concentración máxima

promedio 24 horas de 0,0160 μg/m [3] . Esta concentración, se genera fuera del

área del proyecto, comportamiento típico de las fuentes puntuales.

 Si bien, y tal como se presenta en la Figura 28, los puntos discretos se

encuentran inmersos dentro de la pluma de dispersión, los valores de

concentración son tan bajos que no existe afectación probable. Además, se

considera la alta dispersión del punto donde se emplaza la fuente puntual y la

altura a la cual son emitidas estas partículas, que es a más de 24 metros (ver

Tabla 7). Los puntos discretos 5 y 10 corresponden a los únicos puntos de

unidades habitacionales, y tal como muestra la figura, la pluma de dispersión

no tiene ese sentido espacial, tal que casi es incidental su presencia en esos

puntos.

 Cabe destacar que esta concentración corresponde al promedio aritmético entre

los 0 y 20 metros sobre la elevación del terreno, correspondiente a la primera

celda de modelación vertical; entre las celdas horizontales de 1 km x 1 km.

En la Figura 29, se muestra el mapa de iso concentración, de donde se puede concluir

que:

 El área de estudio es acotada a 173,2 hectáreas, debido a que luego de esta

superficie los valores de concentración son prácticamente nulos. Esta área

cubre principalmente el emplazamiento del proyecto. De todas formas, las

concentraciones son bajas por las razones planteadas en el punto anterior.

 - Las máximas concentraciones fluctúan entre los 0,0139 y 0,0160 μg/m [3] y

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Nueva Providencia 1363, Of.1201,
(56.41)2287848 Providencia
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

Página 45 de 75

abarcan un área de 15,2 hectáreas, la cual se encuentra a una distancia no

mayor de 100 metros hacia el norte de la zona de emplazamiento del proyecto.

Al avanzar cerca 1.500 m desde la zona de mayores emisiones del proyecto, las

concentraciones alcanzan la mitad de la concentración máxima promedio anual.

Tal como se ha presentado, el impacto es prácticamente nulo en las cercanías

del proyecto, debido a las condiciones de liberación del material particulado.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

Página 46 de 75

**Figura 28. Dispersión de la pluma de MP** **10** **como concentración promedio 24 horas**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Nueva Providencia 1363, Of.1201,
(56.41)2287848 Providencia
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

Página 47 de 75

**Figura 29. Iso concentración MP** **10** **como concentración promedio 24 horas.**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

**6.2.2** **Dispersión e Isoconcentración de CO**

Página 48 de 75

A continuación, se presenta el análisis de los resultados de las concentraciones de

monóxido de carbono (CO) tanto como promedio horario como 8 horas. Las

concentraciones obtenidas para este análisis, y tal como se planteó en el ítem 5.1.4,

están en base a las emisiones generadas por la chimenea del proceso de producción

de Hidrógeno y por ende, solo dependerán de esta fuente puntual.

Es importante señalar que la pluma de dispersión del CO simulada por el modelo

abarca principalmente la zona de emplazamiento del proyecto y parte de las unidades

habitacionales cercanas e industrias contiguas al proyecto. Se observa que las

máximas concentraciones se alcanzan en la cercanía de la planta, comportamiento

habitual en la modelación de fuentes puntuales.

**6.2.2.1** **Concentración Promedio 8 Horas de CO**

En Figura 30 se muestra la pluma de dispersión de la concertación promedio 8 horas

de CO, de donde se concluye que:

 Los vientos simulados por el modelo WRF influyen en la pluma de dispersión,

ya que tal como se presentó en el análisis de éstos (ítem 6.1.1) su componente

predominante es de sur o suroeste por ende, generarían un transporte hacia el

norte o noreste, comportamiento previsto por la simulación. A la vez, estos

vientos modelados, tiene una velocidad relativamente alta, con una frecuencia

predominante entre velocidad de 3 a 12 m/s, lo cual también se refleja en la

pluma y en su radio de dispersión.

 Tal como se mencionó en la ítem 5.1.4, las emisiones directas estimadas se

cuantifican en 2,226 ton/año, las que generarán una concentración máxima

promedio 8 horas de 0,0017 mg/Nm [3] . Esta concentración, se genera en menor

medida en la zona del proyecto, pero primordialmente fuera de éste,

comportamiento típico de las fuentes puntuales.

 Si bien, y tal como se presenta en la Figura 30, los puntos discretos se

encuentran inmersos dentro de la pluma de dispersión, los valores de

concentración son tan bajos que no son considerados como afectación a als

personas. Cabe considerar que la norma de CO para 8 horas estipula una

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Nueva Providencia 1363, Of.1201,
(56.41)2287848 Providencia
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

Página 49 de 75

concentración de 10 mg/Nm [3], valor muy por encima de lo modelado. Además,

se considera la alta dispersión del punto donde se emplaza la fuente puntual y

la altura a la cual son emitidas este gas, que es a más de 24 metros (ver Tabla

7). Los puntos discretos 5 y 10 corresponden a los únicos puntos de unidades

habitacionales.

 Cabe destacar que esta concentración corresponde al promedio aritmético entre

los 0 y 20 metros sobre la elevación del terreno, correspondiente a la primera

celda de modelación vertical; entre las celdas horizontales de 1 km x 1 km.

En la Figura 31, se muestra el mapa de isoconcentración, de donde se puede concluir:

 El área de estudio es acotada a 200 hectáreas, debido a que luego de esta

superficie los valores de concentración son prácticamente nulos. Esta área

cubre principalmente el emplazamiento del proyecto e industrias cercanías, y

en menor medida las unidades habitacionales presentes al sureste del proyecto.

De todas formas, como se presentó en el análisis de la pluma de concentración

de CO para concentraciones promedio 8 horas, los valores de concentración

son bajos para ver una afectación real por éstos.

 - Las máximas concentraciones fluctúan entre los 0,0015 y 0,0017 μg/m [3] y

abarcan un área de 19,4 hectáreas, la cual se encuentra inmersa, una parte, al

proyecto y a una distancia no superior de 50 metros de la fuente puntual

(chimenea).

 Al avanzar cerca 1.500 m desde la zona de mayores emisiones del proyecto, las

concentraciones alcanzan valores de concentración tendientes a cero. Tal como

se ha presentado, el impacto es prácticamente nulo en las cercanías del

proyecto, debido a las condiciones de liberación del gas.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

Página 50 de 75

**Figura 30. Dispersión de la pluma de CO** **como concentración promedio 8 horas**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Nueva Providencia 1363, Of.1201,
(56.41)2287848 Providencia
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

Página 51 de 75

**Figura 31. Iso concentración CO** **como concentración promedio 8 horas**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

**6.2.2.2** **Concentración Promedio Horaria de CO**

Página 52 de 75

En Figura 32 se muestra la pluma de dispersión de la concertación promedio horaria de

CO, de donde se concluye que:

 Los vientos anuales simulados por el modelo WRF no influyen de la manera

esperada en la dirección de dispersión del contaminante, ya que tal como se

presentó en el análisis de éstos (ítem 6.1.1) su componente predominante es

de sur o suroeste por ende, se esperaría que el transporte fuese en dirección

norte o noreste, sin embargo, si bien no se aprecia este comportamiento en la

pluma, este comportamiento se debe a temas temporales, ya que los vientos

tienen distintas direcciones según la hora del día, lo que de alguna manera

presenta esta dispersión. De todas maneras se aprecia el alcance de esta

debido a la velocidad del viento, la cual tiene una predominancia en velocidades

de entre 3 a 12 m/s.

 Tal como se mencionó en la ítem 5.1.4, las emisiones directas estimadas se

cuantifican en 2,226 ton/año, las que generarán una concentración máxima

promedio anual de 0,0034 mg/Nm [3] . Esta concentración, se genera dentro del

área de emplazamiento del proyecto.

 Si bien, y tal como se presenta en la Figura 32, los puntos discretos se

encuentran inmersos dentro de la pluma de dispersión, los valores de

concentración son bajos, ya que las concentraciones por norma son 30 mg/m [3],

valores muy por encima de los modelados. Además, se considera la alta

dispersión del punto donde se emplaza la fuente puntual y la altura a la cual

son emitidas estas partículas, que es a más de 24 metros (ver Tabla 7). Los

puntos discretos 5 y 10 corresponden a los únicos puntos de unidades

habitacionales.

 Cabe destacar que esta concentración corresponde al promedio aritmético entre

los 0 y 20 metros sobre la elevación del terreno, correspondiente a la primera

celda de modelación vertical; entre las celdas horizontales de 1 km x 1 km.

En la Figura 33, se muestra el mapa de isoconcentración, de donde se puede concluir

que:

 El área de estudio es acotada a 200 hectáreas, debido a que luego de esta

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Nueva Providencia 1363, Of.1201,
(56.41)2287848 Providencia
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

Página 53 de 75

superficie los valores de concentración son prácticamente nulos. Esta área

cubre principalmente el emplazamiento del proyecto e industrias cercanías, y

en menor medida las unidades habitacionales presentes al sureste del proyecto.

De todas formas, como se presentó en el análisis de la pluma de concentración

de CO para concentraciones promedio horaria, los valores de concentración son

bajos para ver una afectación real por éstos.

- Las máximas concentraciones fluctúan entre los 0,0026 y 0,0030 μg/m [3] y

abarcan un área de 19,4 hectáreas, la cual se encuentra inmersa, una parte, al

proyecto y a una distancia no superior de 50 metros de la fuente puntual

(chimenea).

Al avanzar cerca 1.500 m desde la zona de mayores emisiones del proyecto, las

concentraciones alcanzan valores de concentración tendientes a cero. Tal como

se ha presentado, el impacto es prácticamente nulo en las cercanías del

proyecto, debido a las condiciones de liberación del gas.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

Página 54 de 75

**Figura 32. Dispersión de la pluma de CO como concentración promedio horaria**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Nueva Providencia 1363, Of.1201,
(56.41)2287848 Providencia
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

Página 55 de 75

**Figura 33. Iso concentración CO como concentración promedio horaria**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Nueva Providencia 1363, Of.1201,
(56.41)2287848 Providencia
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

**6.2.3** **Dispersión e Isoconcentración de NO** **2**

Página 56 de 75

A continuación, se presenta el análisis de los resultados de las concentraciones de

óxidos de nitrógeno (NO x ) tanto como promedio horario como 8 horas. Las

concentraciones obtenidas para este análisis, y tal como se planteó en el ítem 5.1.4,

están en base a las emisiones generadas por la chimenea del proceso de producción

de Hidrógeno y por ende, solo dependerán de esta fuente puntual. Cabe destacar para

términos prácticos de análisis, se considerará las concentraciones modeladas de NO x

como concentraciones de NO 2 .

Es importante señalar que la pluma de dispersión del NO 2 simulada por el modelo

abarca principalmente la zona de emplazamiento del proyecto y parte de las unidades

habitacionales cercanas e industrias contiguas al proyecto. Se observa que las

máximas concentraciones se alcanzan en la cercanía de la planta, comportamiento

habitual en la modelación de fuentes puntuales.

**6.2.3.1** **Concentración Promedio Anual NO** **2**

En Figura 34 se muestra la pluma de dispersión de la concertación promedio anual de

NO 2, de donde se concluye que:

 Los vientos simulados por el modelo WRF influyen en la pluma de dispersión,

ya que tal como se presentó en el análisis de éstos (ítem 6.1.1) su componente

predominante es de sur o suroeste por ende, generarían un transporte hacia el

norte o noreste, comportamiento previsto por la simulación. A la vez, estos

vientos modelados, tiene una velocidad relativamente alta, con una frecuencia

predominante entre velocidad de 3 a 12 m/s, lo cual también se refleja en la

pluma y en su radio de dispersión.

 Tal como se mencionó en la ítem 5.1.4, las emisiones directas estimadas se

cuantifican en 4,452 ton/año, las que generarán una concentración máxima

promedio anual de 0,1227 μg/m [3] . Esta concentración, se genera fuera del área

del proyecto, comportamiento típico de las fuentes puntuales.

 Si bien, y tal como se presenta en la Figura 34, los puntos discretos se

encuentran inmersos dentro de la pluma de dispersión, los valores de

concentración son tan bajos que llegan a ser despreciables. Además, se

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Nueva Providencia 1363, Of.1201,
(56.41)2287848 Providencia
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

Página 57 de 75

considera la alta dispersión del punto donde se emplaza la fuente puntual y la

altura a la cual son emitidas estas partículas, que es a más de 24 metros (ver

Tabla 7). Los puntos discretos 5 y 10 corresponden a los únicos puntos de

unidades habitacionales, y tal como muestra la figura, la pluma de dispersión

no tiene ese sentida, tal que casi es incidental su presencia en esos puntos.

 Cabe destacar que esta concentración corresponde al promedio aritmético entre

los 0 y 20 metros sobre la elevación del terreno, correspondiente a la primera

celda de modelación vertical; entre las celdas horizontales de 1 km x 1 km.

En la Figura 35, se muestra el mapa de isoconcentración, de donde se puede concluir:

 El área de estudio es acotada a 200 hectáreas, debido a que luego de esta

superficie los valores de concentración son prácticamente nulos. Esta área

cubre principalmente el emplazamiento del proyecto e industrias cercanías, y

en menor medida las unidades habitacionales presentes al sureste del proyecto.

De todas formas, como se presentó en el análisis de la pluma de concentración

de NO 2 para concentraciones promedio horaria, los valores de concentración

son bajos para ver una afectación real por éstos.

 - Las máximas concentraciones fluctúan entre los 0,1001 y 0,1200 μg/m [3] y

abarcan un área de 19,4 hectáreas, la cual se encuentra inmersa, una parte, al

proyecto y a una distancia no superior de 50 metros de la fuente puntual

(chimenea).

 Al avanzar cerca 1.500 m desde la zona de mayores emisiones del proyecto, las

concentraciones alcanzan valores de concentración tendientes a cero. Tal como

se ha presentado, el impacto es prácticamente nulo en las cercanías del

proyecto, debido a las condiciones de liberación del gas.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

Página 58 de 75

**Figura 34. Dispersión de la pluma de NO** **2** **como concentración promedio anual**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Nueva Providencia 1363, Of.1201,
(56.41)2287848 Providencia
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

Página 59 de 75

**Figura 35. Iso concentración NO** **2** **como concentración promedio anual**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

**6.2.3.2** **Concentración Promedio Horaria de NO** **2**

Página 60 de 75

En Figura 36 se muestra la pluma de dispersión de la concentración promedio horaria

de NO 2, de donde se concluye que:

 Los vientos simulados por el modelo WRF influyen en la pluma de dispersión,

ya que tal como se presentó en el análisis de éstos (ítem 6.1.1) su componente

predominante es de sur o suroeste por ende, generarían un transporte hacia el

norte o noreste, comportamiento previsto por la simulación. A la vez, estos

vientos modelados, tiene una velocidad relativamente alta, con una frecuencia

predominante entre velocidad de 3 a 12 m/s, lo cual también se refleja en la

pluma y en su radio de dispersión.

 Tal como se mencionó en la ítem 5.1.4, las emisiones directas estimadas se

cuantifican en 4,452 ton/año, las que generarán una concentración máxima

promedio anual de 4,100 μg/m [3] . Esta concentración, se genera fuera del área

del proyecto, comportamiento típico de las fuentes puntuales.

 Si bien, y tal como se presenta en la Figura 36, los puntos discretos se

encuentran inmersos dentro de la pluma de dispersión, los valores de

concentración son tan bajos que llegan a ser despreciables. Además, se

considera la alta dispersión del punto donde se emplaza la fuente puntual y la

altura a la cual son emitidas estas partículas, que es a más de 24 metros (ver

Tabla 7). Los puntos discretos 5 y 10 corresponden a los únicos puntos de

unidades habitacionales, y tal como muestra la figura, la pluma de dispersión

no tiene ese sentida, tal que casi es incidental su presencia en esos puntos.

 Cabe destacar que esta concentración corresponde al promedio aritmético entre

los 0 y 20 metros sobre la elevación del terreno, correspondiente a la primera

celda de modelación vertical; entre las celdas horizontales de 1 km x 1 km.

En la Figura 37, se muestra el mapa de isoconcentración, de donde se puede concluir

que:

 El área de estudio es acotada a 200 hectáreas, debido a que luego de esta

superficie los valores de concentración son prácticamente nulos. Esta área

cubre principalmente el emplazamiento del proyecto e industrias cercanías, y

en menor medida las unidades habitacionales presentes al sureste del proyecto.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Nueva Providencia 1363, Of.1201,
(56.41)2287848 Providencia
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

Página 61 de 75

De todas formas, como se presentó en el análisis de la pluma de concentración

de NO 2 para concentraciones promedio horaria, los valores de concentración

son bajos para ver una afectación real por éstos.

Las máximas concentraciones fluctúan entre los 3,501 y 4,100 μg/m [3] y abarcan

un área de 19,4 hectáreas, la cual se encuentra inmersa, una parte, al proyecto

y a una distancia no superior de 50 metros de la fuente puntual (chimenea).

Al avanzar cerca 1.500 m desde la zona de mayores emisiones del proyecto, las

concentraciones alcanzan valores de concentración tendientes a cero. Tal como

se ha presentado, el impacto es prácticamente nulo en las cercanías del

proyecto, debido a las condiciones de liberación del gas.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

Página 62 de 75

**Figura 36. Dispersión de la pluma de NO** **2** **como concentración promedio horario**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Nueva Providencia 1363, Of.1201,
(56.41)2287848 Providencia
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

Página 63 de 75

**Figura 37. Iso concentración NO** **2** **como concentración promedio horario**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Nueva Providencia 1363, Of.1201,
(56.41)2287848 Providencia
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

**6.2.4** **Modelación discreta de las emisiones contaminantes**

Página 64 de 75

La modelación discreta de emisiones fue realizada tanto para la concentración de

material particulado, como de los gases CO y NOx. Los valores de las concentraciones

modeladas para estos puntos discretos se presentan en la Tabla 13. Cabe destacar que

de esta tabla, solos os puntos P5 y P10 corresponden específicamente a unidades

habitacionales urbanas cercanas al proyecto, los demás puntos comprenden a puntos

industriales de trabajo cercanos a la planta.

De la Tabla 13 se puede apreciar que los puntos con mayores concentraciones son el

P3 y P7, puntos que están presentes en la tendencia de dispersión de pluma. Si bien,

se puede mencionar que contienen las mayores concentraciones, en términos

normativos, las concentraciones modeladas son bajas, siendo varias veces menores a

su norma, y siendo su impacto casi insignificante a la línea base de la zona, tal como

se presentará en el ítem 6.2.5.

**Tabla 13. Concentración modelada en puntos receptores con respecto a MP,**

**CO y NO** **x**

|Punto|Distancia al<br>proyecto (m)|Concentraciones Modeladas|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Punto**|**Distancia al**<br>**proyecto (m)**|**MP**<br>**(μg/m3) **|**MP**<br>**(μg/m3) **|**CO**<br>**(μg/m3) **|**CO**<br>**(μg/m3) **|**NO2 **<br>**(μg/m3) **|**NO2 **<br>**(μg/m3) **|
|**Punto**|**Distancia al**<br>**proyecto (m)**|**Anual**|**24 horas**|**8 horas**|**Horaria**|**Anual**|**Horaria**|
|P1|36,78|0,000|0,040|0,000|0,002|0,006|2,047|
|P2|170,00|0,001|0,050|0,001|0,002|0,023|2,273|
|P3|126,62|0,001|0,120|0,001|0,005|0,052|6,473|
|P4|154,80|0,000|0,050|0,001|0,002|0,018|2,603|
|P5|362,00|0,001|0,060|0,001|0,002|0,038|2,290|
|P6|119,20|0,000|0,040|0,000|0,001|0,016|2,071|
|P7|121,20|0,001|0,060|0,001|0,002|0,024|5,439|
|P8|107,60|0,002|0,060|0,001|0,003|0,066|4,255|
|P9|271,80|0,001|0,060|0,001|0,003|0,045|3,274|
|P10|412,90|0,001|0,060|0,001|0,002|0,038|2,742|

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Nueva Providencia 1363, Of.1201,
(56.41)2287848 Providencia
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

Página 65 de 75

**6.2.5** **Aporte del proyecto a la concentración a la Estación de Monitoreo de**

**Representatividad Poblacional (ERMP)**

Tal como se ha mostrado en la exposición de los resultados, las mayores

concentraciones de contaminantes se generan en las proximidades del proyecto,

haciendo que la cuantificación para todos los contaminantes sean prácticamente nulas

a distancias superiores a 1,5 km. La estación de monitoreo de representatividad

poblacional se encuentran a 6,5 km, siendo esta la estación Coronel del SINCA.

La cuantificación del aporte del proyecto a la condición basal de la concentraciones en

la ERMP pertinentes, información del año 2016 para la estación Coronel, expresado en

la Tabla 14, muestra que el aporte estimado del proyecto no supero el 0,01% para

ninguna de las contaminantes.

**Tabla 14. Aumento de la concentración basal en la ERMP Coronel**

|Concentración|MP (μg/m3)<br>10|Col3|CO (mg/m3)|Col5|NO (μg/m3)<br>2|Col7|
|---|---|---|---|---|---|---|
|**Concentración**|**Anual**|**24 h**|**8 h**|**1 h**|**Anual**|**1 h**|
|**Registro**|56,32|126,3|0,7325|0,9276|25,43|184,4|
|**Modelada**|0,0001|0,0700|0,0001|0,0003|0,0017|0,3301|
|**Proyectada**|56,32|126,3|0,7326|0,9279|25,43|184,7|

Nota: Elaboración Propia en base a la información obtenida del Sistema de Información de

Calidad del Aire (SINCA) y los datos obtenidos de la modelación.

**6.2.6** **Análisis resultados meteorológicos**

**6.2.6.1** **Análisis de ajuste sobre el modelo meteorológico**

La correlación de los datos se realizó entre datos observados y modelados. Los datos

observados corresponden a los registrados en la estación Coronel, en línea con el

SINCA, única estación de monitoreo meteorológico con datos disponibles para el año

2014, mismo año de simulación del modelo WRF.

La correlación de los datos se determinó a través del ajuste por mínimos cuadrados,

método en el que existen dos parámetros de importancia: coeficiente de correlación de

Pearson (r) y el coeficiente de determinación (R [2] ).

El coeficiente de correlación lineal es una medida de relación de Pearson entre dos

variables y se usa para medir el grado de relación entre ellas. El rango de valores va

desde el -1 al 1 y está representado por la siguiente ecuación.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

Página 66 de 75

Donde,

 - σ xy, es la covarianza entre x e y;

 - σ x, es la desviación estándar de x;

 - σ y, es la desviación estándar de y;

El coeficiente de determinación, se utiliza como medida de eficiencia de la cobertura de

datos midiendo el porcentaje de variación entre las variables observadas y modeladas,

es decir, testea la capacidad predictiva del modelo e indica la proporción de la varianza

de los resultados que puede ser explicado por el modelo. Los valores del coeficiente de

determinación varían de 0 a 1, siendo este último el valor óptimo y está determinada

por la siguiente relación.

Donde,

 - σ xy, es la covarianza entre x e y;

 - σ x, es la desviación estándar de x;

 - σ y, es la desviación estándar de y;

Con los indicadores antes mencionados, se analizarán a continuación las variables

meteorológicas.

**6.2.6.2** **Temperatura**

En la Figura 38, se observa la correlación entre la temperatura horaria observada en la

estación Coronel y las simuladas por el modelo WRF.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

Página 67 de 75

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

A partir de la figura anterior se observa una correlación positiva entre las variables

(r=0,84), o sea que, existe una correlación directa entre las variables, además se

observa que el coeficiente de determinación es cercano a 1 (R [2] =0,70). En definitiva, al

ajuste por mínimos cuadrados de los datos observados y modelados concluyen que

70% de los datos observados en la Estación Coronel para el año 2014 es simulado por

el modelo WRF.

Además, se observa que el modelo simula más frecuencias de temperaturas entre los

11,8 y 14,6°C mientras que los datos observados presenta una mayor variedad de

registros de temperatura en otras clases, tal como se muestra en la siguiente figura.

Con lo anterior, se concluye que el modelo subestima las temperaturas extremas.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

Página 68 de 75

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
|0 <br>0||||||
|4 <br>0||||||
|43<br>0||||||
|161<br>0||||||
|574<br>0||||||
|8<br>0|44|||||
||162|0<br>1902||||
|||27|08||5295|
||16<br>1392|87||||
|652<br>22||||||
|253<br>0||||||
|61<br>0||||||
|1 <br>0||||||

0 1000 2000 3000 4000 5000 6000

**Frecuencia**

Datos Modelados Datos Observados

**Figura 39. Comparación entre la frecuencia de temperatura de los datos**

**modelados y observados**

**6.2.6.3** **Velocidad del viento**

En la siguiente figura se observa la velocidad del viento horaria observada en

comparación con las modeladas por el modelo WRF para el año 2014.

De donde es posible apreciar que existe una relación positiva entre las variables

(r=0,45), y que el coeficiente de correlación de los datos, sugiere que no existe mucha

correlación de los datos (R [2] =0,2035); en éste contexto, el análisis concluye que tan

sólo el 20% de los datos observados en la estación Coronel se ajusta a las velocidades

de viento simuladas por el modelo WRF. En términos prácticos, se observa que existe

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

Página 69 de 75

una baja correlación entre los datos modelados y los observados y que mientras el

modelo simula condiciones en donde los vientos son de gran magnitud, la estación

registró vientos de menor intensidad.

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

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

9.4 ; 10.1

8.7 ; 9.4

8 ; 8.7

7.2 ; 8

6.5 ; 7.2

5.8 ; 6.5

5.1 ; 5.8

4.3 ; 5.1

3.6 ; 4.3

2.9 ; 3.6

2.2 ; 2.9

1.4 ; 2.2

0.7 ; 1.4

0 ; 0.7

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

Página 70 de 75

|0|549|Col3|Col4|Col5|
|---|---|---|---|---|
|1|582||||
|4|663||||
|20|7|33|||
|36||783|||
|92||790|||
|252|613||||
||585<br>378||||
||574<br>548||||
||465|809|||
||365||1267||
|30|0|||1584|
|166||||1768|
|62||||188|

0 400 800 1200 1600 2000

Datos Observados Datos Modelados

**Figura 41. Comparación entre la frecuencia de velocidad del viento de los**

**datos modelados y observados**

**6.2.6.4** **Dirección del viento**

En la siguiente figura se observa la correlación del viento entre los datos modelados y

los observados, de donde se puede concluir que no existe correlación entre ambos

factores.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

Página 71 de 75

**Figura 42. Correlación entre la dirección del viento observadas y**

**temperaturas modeladas**

No obstante, si bien se observa que casi no hay correlación entre la dirección de viento

horaria observada y modelada, el análisis de frecuencia demuestra que el modelo es

capaz de simular las frecuencias en las distintas componentes en un rango aceptable,

pero que aquellos en componente sur, son sobre estimados y los que nacen en el este

y noreste este son subestimadas.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

Página 72 de 75

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

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

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
||597<br>85|9||||||

0 500 1000 1500 2000 2500 3000 3500 4000

**Frecuencia**

Datos Modelados Datos Observados

**Figura 43. Comparación entre la frecuencia de velocidad del viento de los**

**datos modelados y observados**

**6.2.6.5** **Test de Bondad de Ajuste sobre el Modelo Meteorológico**

Se prescindirá de la aplicación de test de bondad de ajuste entre los datos modelados

y los observados, debido a que los datos modelados no provienen de una muestra

sobre la cual se ha supuesto una distribución de probabilidad específica, como, por

ejemplo: log normal, binomial, Bernoulli, etc., sino que son el resultado de la

simulación a través de la implementación de un modelo matemático.

**6.2.7** **Análisis de los resultados de concentración de contaminantes en la**

**atmósfera**

Los resultados de la modelación son los esperados en cuanto a su magnitud, sobre

todo en lo que respecta a las bajas concentraciones obtenidas como resultado de la

modelación de material particulado y gases (CO y NOx) fuera del área del proyecto,

estos producto de la acción de los vientos y la cantidad de emisiones asociadas,

además de la altura y velocidad de escape del material particulado y los gases de

combustión.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

Página 73 de 75

Es importante señalar, que las concentraciones modeladas de material particulado y

gases no deberían representar un impacto significativo en la comuna de Coronel y en

el Concepción Metropolitano, pues el proyecto, de acuerdo a lo valores de

concentración modelados, su dispersión, y los valores de la modelación discreta,

aportan menos de un 0,1% de concentración a la línea base, siendo casi incidental en

ésta.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

**7** **Conclusión**

Página 74 de 75

La concentración en el aire de contaminantes depende de múltiples factores, entre

ellos la tasa de emisión de la fuente emisora, las características topográficas y

meteorológicas de la zona, para acotar las variables. Bajo esta mirada, esta última

variable, la meteorología se hacen importantes a la hora de evaluar un modelo. La

modelación de la meteorológica fue realizada con el modelo WRF y el resultado de esta

modelación fue analizado en función al coeficiente de correlación lineal y el coeficiente

de determinación. De las variables meteorológicas se concluye que:

 Para el caso de la temperatura, los resultados fueron iguales a 0,84 y 0,70 para

el coeficiente de correlación y determinación respectivamente, evidenciando

una alta representación del perfil de temperatura.

 En el caso de la velocidad del viento, la comparativa con la estación Coronel

arrojo valores de 0,45 y 0,20 para el coeficiente de correlación y de

determinación respectivamente, evidencia un comportamiento similar y

aceptable para la modelación.

 Por último, para el caso de la dirección del viento, los valores fueron

prácticamente nulas para ambos coeficientes. Ahora bien, el análisis de

frecuencia demuestra que el modelo es capaz de simular las frecuencias en las

distintas componentes en un rango aceptable, pero que aquellos en

componente sur, son sobre estimados y los que nacen en el este y noreste este

son subestimadas.

Por consiguiente, se concluye el modelo WRF tiene una aceptable representación de la

meteorología, considerando que la atmosfera es definida como un fluido caótico

turbulento.

Las concentraciones modeladas, si bien fueron sobredimensionadas desde su origen en

el informe de emisiones considerando el peor escenario, éstas no generarían efectos

adversos sobre la población del proyecto y sobre las poblaciones cercanas al área de

emplazamiento del proyecto. Esta afirmación se basa en la cuantificación del aporte de

las concentraciones sobre las EMRP, presentadas en la Tabla 14, en la cual se

manifiesta que el aporte de las concentraciones no es superior al 0,01%, siendo

ínfimas en consideración a la línea base actual, además de la cuantificación de las

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

DECLARACIÓN DE IMPACTO AMBIENTAL
“PLANTA PERÓXIDO DE HIDRÓGENO - CORONEL”

Página 75 de 75

concentraciones de MP 10 y MP 2,5, como de CO y NO x (sección 6.2.1, 6.2.2 y 6.2.3), en

la cual se evidencia que las concentraciones son cercanas a cero una vez distanciados

aprox. 1.500 metros de la zona del proyecto.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro de la Paz Av. Del Valle Sur 512, Of.304,
(56.41)2287848 Huechuraba
www.dss.cl (56.2)23494104

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Valores normados para MP** **10** **y MP** **2,5** **en Chile****

| Nivel | MP (μg/m3)<br>10 | MP (μg/m3)<br>2,5 |
| --- | --- | --- |
| Límite anual | 50 | 20 |
| Límite diario | 150 | 50 |
| Alerta | 195 - 239 | 80 -109 |
| Preemergencia | 240 - 329 | 110 - 169 |
| Emergencia | 330 o mayor | 170 o mayor |

**Tabla 2.: Coordenadas del dominio de la modelación meteorológica****

| Vértice | Proyección UTM, Huso 18 Sur, Datum: WSG-84 | Col3 |
| --- | --- | --- |
| **Vértice** | **Este (km)** | **Norte (km)** |
| Suroeste | 639,530 | 5.896,829 |
| Sureste | 701,530 | 5.896,829 |
| Noroeste | 639,530 | 5.958,829 |
| Noreste | 701,530 | 5.958,829 |
| Centroide | 670,530 | 5.927,829 |

**Tabla 3.: Coordenadas de los puntos receptores discretos del proyecto****

| Receptor | UTM, Huso 18 S, WGS-84 | Col3 | Distancia al<br>proyecto (m) |
| --- | --- | --- | --- |
| **Receptor** | **Este (km)** | **Norte (km)** | **Norte (km)** |
| P1 | 662,892 | 5.905,951 | 36,78 |
| P2 | 663,025 | 5.905,944 | 170,00 |

**Tabla 4.: Coordenadas de las Estaciones de Monitoreo con Representatividad****

| Receptor | UTM, Huso 18 S, WGS-84 | Col3 | Col4 | Col5 | Distancia al<br>proyecto (m) |
| --- | --- | --- | --- | --- | --- |
| **Receptor** | **Este (km)** | **Este (km)** | **Norte (km)** | **Norte (km)** | **Norte (km)** |
| Coronel | 665,556 | 665,556 | 5.899,980 | 5.899,980 | 6.490,0 |
|  |  | ~~**Concepción**~~<br>~~**Chile**~~<br>Los Pensamientos 197, San Pedro de la Paz<br>(56.41)2287848<br>www.dss.cl | ~~**Concepción**~~<br>~~**Chile**~~<br>Los Pensamientos 197, San Pedro de la Paz<br>(56.41)2287848<br>www.dss.cl | ~~**Santiago**~~<br>~~**Chile**~~<br>Av. Del Valle Sur 512, Of.304,<br>Huechuraba<br>(56.2)23494104 | ~~**Santiago**~~<br>~~**Chile**~~<br>Av. Del Valle Sur 512, Of.304,<br>Huechuraba<br>(56.2)23494104 |

**Tabla 5.: Emisiones generadas por la chimenea****

| Contaminantes | Emisión (ton/año) |
| --- | --- |
| MP | 0,110 |
| NOx | 4,452 |
| CO | 2,226 |

**Tabla 6.: Parámetros de salida de material particulado y gases de la****

| Ítem | Valor | Unidad |
| --- | --- | --- |
| Altura del punto de<br>descarga de los gases | 23,8 | m |
| Temperatura Salida Gases | 195 | °C |
| Diámetro de ducto de<br>salida de los gases | 23,8 | m |
| Velocidad Escape Gases | 10,0 | m/s |

**Tabla 7.: Coordenada Fuente Puntual - Chimenea****

| Fuente de Emisión | UTM, Huso 18 S, WGS-84 | Col3 |
| --- | --- | --- |
| **Fuente de Emisión** | **Este (km)** | **Norte (km)** |
| Chimenea | 662,807 | 5.906,019 |

**Tabla 8.: Frecuencia de los vientos anuales, WRF.****

| Componente | Col2 | Total |
| --- | --- | --- |
| Norte | N | 786 |
| Nord noreste | NNE | 464 |
| Noreste | NE | 128 |
| Este noreste | ENE | 48 |
| Este | E | 36 |
| Este Sureste | ESE | 89 |
| Sureste | SE | 163 |
| Sur sureste | SSE | 287 |
| Sur | S | 1513 |
| Sur suroeste | SSO | 2741 |
| Suroeste | SO | 746 |
| Oeste suroeste | OSO | 257 |
| Oeste | O | 264 |
| Oeste noroeste | ONO | 290 |
| Noroeste | NO | 369 |

**Tabla 9.: Frecuencia de los vientos verano, WRF.****

| Componente | Col2 | Total |
| --- | --- | --- |
| Norte | N | 63 |
| Nord noreste | NNE | 51 |
| Noreste | NE | 19 |
| Este noreste | ENE | 12 |
| Este | E | 7 |
| Este Sureste | ESE | 4 |
| Sureste | SE | 9 |
| Sur sureste | SSE | 34 |
| Sur | S | 374 |
| Sur suroeste | SSO | 1040 |
| Suroeste | SO | 261 |
| Oeste suroeste | OSO | 69 |

**Tabla 10.: Frecuencia de los vientos otoño, WRF.****

| Componente | Col2 | Total |
| --- | --- | --- |
| Norte | N | 360 |
| Nord noreste | NNE | 154 |
| Noreste | NE | 45 |
| Este noreste | ENE | 14 |
| Este | E | 13 |
| Este Sureste | ESE | 38 |
| Sureste | SE | 60 |
| Sur sureste | SSE | 89 |
| Sur | S | 300 |

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

**Tabla 12.: Frecuencia de los vientos en primavera, WRF.****

| Componente | Col2 | Total |
| --- | --- | --- |
| Norte | N | 57 |
| Nord noreste | NNE | 24 |
| Noreste | NE | 1 |
| Este noreste | ENE | 7 |
| Este | E | 2 |
| Este Sureste | ESE | 11 |

**Tabla 13.: Concentración modelada en puntos receptores con respecto a MP,****

| Punto | Distancia al<br>proyecto (m) | Concentraciones Modeladas | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Punto** | **Distancia al**<br>**proyecto (m)** | **MP**<br>**(μg/m3) ** | **MP**<br>**(μg/m3) ** | **CO**<br>**(μg/m3) ** | **CO**<br>**(μg/m3) ** | **NO2 **<br>**(μg/m3) ** | **NO2 **<br>**(μg/m3) ** |
| **Punto** | **Distancia al**<br>**proyecto (m)** | **Anual** | **24 horas** | **8 horas** | **Horaria** | **Anual** | **Horaria** |
| P1 | 36,78 | 0,000 | 0,040 | 0,000 | 0,002 | 0,006 | 2,047 |
| P2 | 170,00 | 0,001 | 0,050 | 0,001 | 0,002 | 0,023 | 2,273 |
| P3 | 126,62 | 0,001 | 0,120 | 0,001 | 0,005 | 0,052 | 6,473 |
| P4 | 154,80 | 0,000 | 0,050 | 0,001 | 0,002 | 0,018 | 2,603 |
| P5 | 362,00 | 0,001 | 0,060 | 0,001 | 0,002 | 0,038 | 2,290 |
| P6 | 119,20 | 0,000 | 0,040 | 0,000 | 0,001 | 0,016 | 2,071 |
| P7 | 121,20 | 0,001 | 0,060 | 0,001 | 0,002 | 0,024 | 5,439 |
| P8 | 107,60 | 0,002 | 0,060 | 0,001 | 0,003 | 0,066 | 4,255 |
| P9 | 271,80 | 0,001 | 0,060 | 0,001 | 0,003 | 0,045 | 3,274 |
| P10 | 412,90 | 0,001 | 0,060 | 0,001 | 0,002 | 0,038 | 2,742 |

**Tabla 14.: Aumento de la concentración basal en la ERMP Coronel****

| Concentración | MP (μg/m3)<br>10 | Col3 | CO (mg/m3) | Col5 | NO (μg/m3)<br>2 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Concentración** | **Anual** | **24 h** | **8 h** | **1 h** | **Anual** | **1 h** |
| **Registro** | 56,32 | 126,3 | 0,7325 | 0,9276 | 25,43 | 184,4 |
| **Modelada** | 0,0001 | 0,0700 | 0,0001 | 0,0003 | 0,0017 | 0,3301 |
| **Proyectada** | 56,32 | 126,3 | 0,7326 | 0,9279 | 25,43 | 184,7 |
