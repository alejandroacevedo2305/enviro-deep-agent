---
title: Sin título
author: Maryorie Schulz
date: D:20230126202221-03'00'
language: es
type: report
pages: 106
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - MODELACIÓN ATMOSFÉRICA DE EMISIONES PROYECTO HABITACIONAL LA GAMBOINA
-->

# MODELACIÓN ATMOSFÉRICA DE EMISIONES PROYECTO HABITACIONAL LA GAMBOINA

**ENERO 2023**

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO HABITACIONAL DOÑA LA GAMBOINA”

**ÍNDICE**

**Página 2 de 106**

**1** **INTRODUCCIÓN ............................................................................................ 7**

**2** **OBJETIVOS.................................................................................................... 9**

**3** **MARCO LEGAL REGULATORIO .................................................................... 10**

**3.1** **Estado de la Calidad del Aire en zonas circundantes al proyecto ............. 13**

**3.2** **Análisis del Cumplimiento Normativo ...................................................... 13**

**4** **JUSTIFICACIÓN DE LOS MODELOS UTILIZADOS EN EL ESTUDIO .............. 24**

**4.1** **Uso del modelo CALPUFF ......................................................................... 25**

**4.2** **Uso del modelo WRF ................................................................................ 27**

**5** **METODOLOGÍA ........................................................................................... 28**

**5.1** **Modelación de partículas ......................................................................... 28**

5.1.1 Modelación meteorológica ............................................................................. 28

5.1.2 Modelación de dispersión de contaminantes ................................................... 29

5.1.3 Criterios para la modelación de partículas ...................................................... 31

**6** **RESULTADOS .............................................................................................. 36**

**6.1** **Modelamiento meteorológico .................................................................. 36**

6.1.1. Caracterización Geofísica de la zona de estudio ........................................... 36

6.1.2 Caracterización de la velocidad y dirección de los vientos Anual y Estacional. .... 37

6.1.3 Caracterización de la Temperatura del Aire ..................................................... 48

6.1.4 Altura de Capa de Mezcla.............................................................................. 50

6.1.5 Caracterización de la precipitación ................................................................. 52

**6.2** **Concentraciones Modeladas .................................................................... 54**

6.2.1 Dispersión e Isoconcentración Material Particulado Respirable, MP10................ 54

6.2.2 Dispersión e Isoconcentración Material Particulado Fino Respirable, MP2,5 ....... 61

6.2.3 Dispersión Dióxido de Nitrógeno, NO 2 ............................................................ 67

6.2.4 Dispersión Dióxido de Azufre (SO 2 ) ................................................................ 73

6.2.5 Dispersión Monóxido de Carbono (CO) ........................................................... 82

6.2.6 Modelación discreta de las emisiones contaminantes ....................................... 88

6.2.7 Aporte a la estación de Monitoreo de Representatividad Poblacional (EMRP) ..... 92

**7** **ANÁLISIS DE INCERTIDUMBRE .................................................................. 95**

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO HABITACIONAL DOÑA LA GAMBOINA”

**Página 3 de 106**

**7.1** **Temperatura ............................................................................................ 97**

**7.2** **Velocidad del viento ................................................................................. 99**

**7.3** **Dirección del viento ............................................................................... 100**

7.3.1 Componente zonal del viento ...................................................................... 101

7.3.2 Componente meridional del viento ............................................................... 102

**7.4** **Test de Bondad de Ajuste sobre el Modelo Meteorológico ..................... 103**

**8** **CONCLUSIÓN ............................................................................................ 104**

**9** **BIBLIOGRAFÍA .......................................................................................... 106**

**ÍNDICE DE FIGURAS**

Figura 1. Ubicación del proyecto .................................................................................. 7

Figura 2. Ubicación EMRP Rancagua I ......................................................................... 14

Figura 3. Concentración promedio 24 horas de MP10, EMRP Rancagua I ........................ 15

Figura 4. Concentración promedio trianual MP10, EMRP Rancagua I .............................. 16

Figura 5. Concentración promedio 24 horas de MP2,5, EMRP Rancagua I ....................... 17

Figura 6. Concentración promedio trianual MP2,5, EMRP Rancagua I ............................. 18

Figura 7. Concentración promedio trianual horaria de SO 2, EMRP Rancagua I ................. 19

Figura 8. Concentración promedio trianual 24 horas de SO 2, EMRP Rancagua I .............. 20

Figura 9. Concentración promedio trianual de SO 2, EMRP Rancagua I ............................ 21

Figura 10. Concentración promedio trianual horaria de CO, EMRP Rancagua I ................ 23

Figura 11. Concentración promedio trianual 8 horas de CO, EMRP Rancagua I ............... 24

Figura 12. Receptores discretos .................................................................................. 31

Figura 13. Polígonos de modelación representativos de cada unidad modelada............... 35

Figura 14. Elevación del terreno en el área de la modelación meteorológica ................... 36

Figura 15. Rosa de los vientos anual, WRF 2021. ......................................................... 37

Figura 16. Frecuencia de los vientos, año 2021. ........................................................... 38

Figura 17. Rosa de los vientos verano, WRF 2021. ....................................................... 39

Figura 18. Frecuencia de los vientos en verano, año 2021. ........................................... 40

Figura 19. Rosa de los vientos otoño, WRF 2021. ......................................................... 41

Figura 20. Frecuencia de los vientos en otoño, año 2021. ............................................. 42

Figura 21. Rosa de los vientos invierno, WRF 2021. ..................................................... 43

Figura 22. Frecuencia de los vientos en invierno, año 2021. .......................................... 44

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO HABITACIONAL DOÑA LA GAMBOINA”

**Página 4 de 106**

Figura 23. Rosa de los vientos en primavera, WRF 2021. .............................................. 45

Figura 24. Frecuencia de los vientos en primavera, año 2021. ....................................... 46

Figura 25. Perfil diario de velocidad del viento, WRF año 2021. ..................................... 47

Figura 26. Temperatura Mensual WRF, año 2021. ........................................................ 48

Figura 27. Perfil diario de Temperatura, WRF año 2021. ............................................... 49

Figura 28. Evolución diaria de la altura de capa de mezcla, WRF año 2021. .................... 51

Figura 29. Precipitación Anual, WRF 2021. .................................................................. 53

Figura 30. Dispersión de la pluma de MP10 como concentración de 24 horas ................. 56

Figura 31. Isolíneas de concentración de MP10 como concentración de 24 horas. ........... 57

Figura 32. Dispersión de la pluma de MP10 como concentración promedio anual. ........... 59

Figura 33. Isolíneas de concentración de MP10 como concentración promedio anual. ..... 60

Figura 34. Dispersión de la pluma de MP2,5 como concentración promedio diaria. .......... 62

Figura 35. Isolíneas de concentración de MP2,5 como concentración promedio diaria. .... 63

Figura 36. Dispersión de la pluma de MP2,5 como concentración promedio anual. .......... 65

Figura 37. Isolíneas de concentración de MP2,5 como concentración promedio anual. .... 66

Figura 38. Dispersión de la pluma de NO 2 como concentración máxima horaria. ............. 68

Figura 39. Isolíneas de concentración de NO 2 como concentración máxima horaria. ........ 69

Figura 40. Dispersión de la pluma de NO 2 como concentración anual. ............................ 71

Figura 41. Isolíneas de concentración de NO 2 como promedio anual. ............................. 72

Figura 42. Dispersión de la pluma de SO 2 como concentración horaria ........................... 74

Figura 43. Isolíneas de concentración de SO 2 como concentración horaria ..................... 75

Figura 44. Dispersión de la pluma de SO 2 como concentración 24 horas ......................... 77

Figura 45. Isolíneas de concentración de SO 2 como concentración 24 horas ................... 78

Figura 46. Dispersión de la pluma de SO 2 como concentración anual ............................. 80

Figura 47. Isolíneas de concentración de SO 2 como concentración anual ........................ 81

Figura 48. Dispersión de la pluma de CO como concentración horaria ............................ 83

Figura 49. Isolíneas de concentración de CO como concentración horaria ...................... 84

Figura 50. Dispersión de la pluma de CO como concentración 8 horas ........................... 86

Figura 51. Isolíneas de concentración de CO como concentración 8 horas ...................... 87

Figura 52. Correlación entre temperaturas observadas y modeladas. ............................. 97

Figura 53. Frecuencia de temperaturas observadas y modeladas. .................................. 98

Figura 54. Correlación entre velocidad del viento observada y modeladas. ..................... 99

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO HABITACIONAL DOÑA LA GAMBOINA”

**Página 5 de 106**

Figura 55. Frecuencia de velocidad del viento observadas y modeladas. ...................... 100

Figura 56. Frecuencia de velocidad del viento observadas y modeladas. ...................... 102

Figura 57. Correlación componente meridional del viento. .......................................... 103

**ÍNDICE DE TABLAS**

Tabla 1. Valores normados para MP10 y MP2,5 en Chile ............................................... 10

Tabla 2. Valores normados para NO 2 y SO 2 en Chile ..................................................... 11

Tabla 3. Valores normados para CO en Chile ............................................................... 12

<!-- INICIO TABLA 3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- es regulado por el D.S. 115/2002 del Ministerio Secretaría General De La Presidencia. En la Tabla 2 y -->

**Tabla 3: se aprecian los valores del límite anual, diario, de 8 horas y horario para los**

| Nivel | Unidad | NO<br>2 | SO<br>2 |
| --- | --- | --- | --- |
| **Concentración Anual** | μg/m3N | 100 | 60 |
| **Concentración Anual** | ppbv | 53 | 23 |
| **Concentración 24 horas** | μg/m3N | - | 150 |
| **Concentración 24 horas** | ppbv | - | 57 |
| **Concentración 1 hora** | μg/m3N | 400 | 350 |
| **Concentración 1 hora** | ppbv | 213 | 134 |
| **Alerta** | μg/m3N | 1.130-2.259 | 500-649 |
| **Alerta** | ppbv | 601-1.201 | 191-247 |
| **Preemergencia** | μg/m3N | 2.260-2.999 | 650-949 |
| **Preemergencia** | ppbv | 1.202-1.595 | 248-362 |
| **Emergencia** | μg/m3N | 3.000 o superior | 950 o superior |
| **Emergencia** | ppbv | 1.596 o superior | 363 o superior |

<!-- Estadísticas: 12 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- **Concepción** **Chile** **Santiago** **Chile** Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304 de la Paz Ciudad Empresarial, Huechuraba (56-41)2287848 (56-2)23494104 -->
<!-- FIN TABLA 3 -->


Tabla 4. Porcentaje de superación concentración promedio anual de MP10, EMRP

Rancagua I. .............................................................................................................. 15

Tabla 5. Registro de días declarados en alerta, preemergencia y emergencia para MP10 en

la EMRP Rancagua I. ................................................................................................. 16

Tabla 6. Porcentaje de superación concentración promedio anual de MP2,5, EMRP

Rancagua I. .............................................................................................................. 17

Tabla 7. Registro de días declarados en alerta, preemergencia y emergencia para MP2,5

en la EMRP Rancagua I.............................................................................................. 18

Tabla 8. Porcentaje de superación concentración horaria de SO 2, EMRP Rancagua I. ...... 19

Tabla 9. Porcentaje de superación concentración 24 horas de SO 2, EMRP Rancagua I. .... 20

Tabla 10. Porcentaje de superación concentración promedio anual de SO 2, EMRP

Rancagua I. .............................................................................................................. 21

Tabla 11. Registro de días declarados en alerta, preemergencia y emergencia para SO 2 en

la EMRP Rancagua I .................................................................................................. 22

Tabla 12. Porcentaje de superación concentración máxima horaria CO, EMRP Rancagua I.

............................................................................................................................... 22

Tabla 13. Porcentaje de superación concentración máxima 8 horas CO, EMRP Rancagua I.

............................................................................................................................... 23

Tabla 14. Características del modelo ........................................................................... 28

Tabla 15. Descripción de los puntos receptores ............................................................ 30

Tabla 16. Coordenadas de modelación de las fuentes areales ....................................... 32

Tabla 17. Concentración modelada en puntos receptores con respecto a MP10 y MP2,5. . 89

Tabla 18. Concentración modelada en puntos receptores con respecto a SO 2 . ................ 90

Tabla 19. Concentración modelada en puntos receptores con respecto a NO 2 ................. 90

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO HABITACIONAL DOÑA LA GAMBOINA”

**Página 6 de 106**

Tabla 20. Concentración modelada en puntos receptores con respecto a CO .................. 92

Tabla 21. Aumento de la concentración basal en la EMRP Rancagua I, año 2021 ............ 93

Tabla 22. Concentraciones basales de SO 2 y aporte del proyecto ................................... 93

Tabla 23. Estadísticos de variables meteorológicas modeladas. ..................................... 97

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 7 de 106**

**1** **INTRODUCCIÓN**

El proyecto “ **Proyecto habitacional La Gamboina”** ubicado en la comuna de

Rancagua, perteneciente a la provincia de Cachapoal, región del Libertador Bernardo

O’Higgins (ver Figura 1). Consiste en la construcción de 408 unidades habitacionales de

carácter social, que corresponden a viviendas del tipo departamento, en una superficie

total de 3,2 hectáreas aproximadamente. A estas viviendas se les sumaran las 264

unidades habitacionales de tipo departamento existentes del proyecto denominado “Doña

Emilia” (situación basal) emplazadas en una superficie de 2,2 hectáreas.

En la siguiente figura se muestra el proyecto que se somete a evaluación ambiental y la

situación basal.

**Figura 1. Ubicación del proyecto**

Con este estudio se busca predecir la concentración de material particulado grueso

(MP10), material particulado fino (MP2,5), y de los gases óxido de nitrógeno (NOx), óxido

de azufre (SOx), y monóxido de carbono (CO). Además, se busca evaluar su contribución

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 8 de 106**

en puntos receptores de interés y en las estaciones de calidad del aire más cercanas, esto

último respecto a su situación basal.

La modelación de las emisiones se realizó en base a los resultados obtenidos de la

actualización del informe de estimación de emisiones atmosféricas que se presenta en la

Adenda I. Dado que el objetivo de la presente modelación es predecir las concentraciones

de MP10, MP2,5, NOx, SOx y CO a las cuales estarán expuestos los receptores cercanos al

área de proceso, es que se considera como escenario de modelación el año donde se

alcanza el máximo de emisiones de MP dentro del polígono del proyecto. Esto sucede en el

año 1 del proyecto, donde se construyen las nuevas viviendas junto con la entrada en

operación de la situación basal.

La evaluación de la dispersión y concentración de las emisiones de material particulado y

gases se realizó mediante el programa CALPUFF, el cual es un modelo de dispersión usado

ampliamente para la simulación de estas concentraciones en el ambiente, producto de

emisiones por operaciones normales, con el objeto de establecer, desarrollar y analizar

escenarios de emisión y regulación. A su vez, CALPUFF es recomendado por el Ministerio

de Medio Ambiente en la “Guía para el Uso de Modelos de Calidad del Aire en el SEIA”,

publicada el año 2012. Los resultados y análisis de esta evaluación se presentan en el

siguiente informe.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 9 de 106**

**2** **Objetivos**

El presente informe, tiene como objetivo general cuantificar y evaluar el efecto en la

atmósfera debido a las emisiones de contaminantes generadas por el proyecto

habitacional **“La Gamboina”** y cuantificar sus concentraciones.

Para lo anterior se plantean los siguientes objetivos específicos:

 Evaluar en términos de concentración, el alcance de las emisiones de MP10,

MP2,5, NOx, SOx y CO en la atmósfera.

 Evaluar la concentración de MP10, MP2,5, NOx, SOx y CO en los receptores que

actualmente se encuentren cercanos al proyecto, así como en las estaciones de

calidad del aire emplazadas cercanos a éste.

 Determinar la afectación a la salud de las personas debido al aporte a la

concentración basal de MP10, MP2,5, SO 2 y CO en la ciudad, dado el desarrollo del

proyecto.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**3** **Marco Legal Regulatorio**

**Página 10 de 106**

Actualmente, los contaminantes MP10, MP2,5, NO 2, SO 2 y CO están regulados bajo

normas de calidad primaria, cuyo objetivo es proteger la salud de las personas de los

efectos agudos y crónicos de la exposición de estos contaminantes con un riesgo

aceptable. Para esto, se fijan límites de concentración permitidos, condiciones de

superación de la norma y los niveles que dan paso a situaciones de emergencia ambiental.

El material particulado respirable MP10 es regulado por el D.S. 12/2022 del Ministerio del

Medio Ambiente, mientras el material particulado fino respirable MP2,5 es regulado por el

D.S. 12/2011 del Ministerio del Medio Ambiente.

En la Tabla 1 se aprecian los valores del límite anual y diario para los contaminante MP10

y MP2,5, además de los rangos que dan origen a situaciones de alerta, preemergencia y

emergencia ambiental.

**Tabla 1. Valores normados para MP10 y MP2,5 en Chile**

|Nivel|MP10 (μg/m3N)|MP2,5 (μg/m3)|
|---|---|---|
|**Concentración Anual**|50|20|
|**Concentración 24 horas**|130|50|
|**Alerta**|180-229|80-109|
|**Preemergencia**|230-329|110-169|
|**Emergencia**|330 o superior|170 o superior|

Fuente: En base a D.S. 12/2022 MMA y D.S. 12/2011 MMA

No obstante, la superación del límite normativo de MP10 no es motivo de condiciones de

superación de la norma, sino que se considera que la norma es incumplida bajo las

siguientes condiciones:

 - Cuando el promedio de la concentración anual de tres años consecutivos iguale o

supere los 50 μg/m3N.

 - Si el percentil 98 (P98) de las concentraciones de 24 horas durante un año sea

igual o superior a 130 μg/m3N.

 - Si durante un año se registrasen siete o más días cuya concentración sea mayor a

130 μg/m3N.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 11 de 106**

En el mismo contexto, las condiciones de superación de la norma de MP2,5 son las que se

describen a continuación:

 - Cuando el promedio de la concentración anual de tres años consecutivos iguale o

supere los 20 μg/m3.

 - Si el percentil 98 (P98) de las concentraciones de 24 horas durante un año sea

igual o superior a 50 μg/m3.

En la misma línea, el Dióxido De Nitrógeno (NO 2 ) es regulado por el D.S. 114/2003 del

Ministerio Secretaría General De La Presidencia, el Dióxido De Azufre (SO 2 ) es regulado

por el D.S. 104/2019 del Ministerio del Medio Ambiente, y el Monóxido De Carbono (CO)

es regulado por el D.S. 115/2002 del Ministerio Secretaría General De La Presidencia.

En la Tabla 2 y

Tabla 3 se aprecian los valores del límite anual, diario, de 8 horas y horario para los

contaminantes NO 2, SO 2 y CO, además de los rangos que dan origen a situaciones de

alerta, preemergencia y emergencia ambiental.

**Tabla 2. Valores normados para NO** **2** **y SO** **2** **en Chile**

|Nivel|Unidad|NO<br>2|SO<br>2|
|---|---|---|---|
|**Concentración Anual**|μg/m3N|100|60|
|**Concentración Anual**|ppbv|53|23|
|**Concentración 24 horas**|μg/m3N|-|150|
|**Concentración 24 horas**|ppbv|-|57|
|**Concentración 1 hora**|μg/m3N|400|350|
|**Concentración 1 hora**|ppbv|213|134|
|**Alerta**|μg/m3N|1.130-2.259|500-649|
|**Alerta**|ppbv|601-1.201|191-247|
|**Preemergencia**|μg/m3N|2.260-2.999|650-949|
|**Preemergencia**|ppbv|1.202-1.595|248-362|
|**Emergencia**|μg/m3N|3.000 o superior|950 o superior|
|**Emergencia**|ppbv|1.596 o superior|363 o superior|

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 12 de 106**

Fuente: En base a D.S. 114/2003 MINSEGEPRES y D.S. 104/2019 MMA

**Tabla 3. Valores normados para CO en Chile**

|Nivel|Unidad|Valor|
|---|---|---|
|**Concentración 8 horas**|mg/m3N|10|
|**Concentración 8 horas**|ppmv|9|
|**Concentración 1 hora**|mg/m3N|30|
|**Concentración 1 hora**|ppmv|26|
|**Alerta**|mg/m3N|17-33|
|**Alerta**|ppmv|15-29|
|**Preemergencia**|mg/m3N|34-39|
|**Preemergencia**|ppmv|30-34|
|**Emergencia**|mg/m3N|40 o superior|
|**Emergencia**|ppmv|35 o superior|

Fuente: En base a D.S. 115/2002 MINSEGEPRES

Las condiciones de superación de la norma de NO 2 son las que se describen a

continuación:

 Cuando el promedio de la concentración anual de tres años consecutivos iguale o

supere los 100 μg/m3N.

 Cuando el promedio trianual del percentil 99 (P99) de los máximos diarios de

concentración de 1 hora durante un año iguale o supere los 400 μg/m3N.

Las situaciones que dan origen a la superación de la norma de SO 2 son:

 Cuando el promedio de la concentración anual de tres años consecutivos iguale o

supere los 60 μg/m3N.

 Cuando el promedio trianual del percentil 99 (P99) de las concentraciones de 24

horas durante un año iguale o supere los 150 μg/m3N.

 Cuando el promedio trianual del percentil 98,5 (P98,5) de las concentraciones de 1

hora durante un año iguale o supere los 350 μg/m3N.

Se considera que la norma de CO es incumplida bajo las siguientes condiciones:

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 13 de 106**

 Cuando el promedio trianual del percentil 99 (P99) de los máximos diarios de

concentración de 8 horas durante un año iguale o supere los 10 mg/m3N.

 Cuando el promedio trianual del percentil 99 (P99) de los máximos diarios de

concentración de 1 hora durante un año iguale o supere los 30 mg/m3N.

**3.1** **Estado de la Calidad del Aire en zonas circundantes al proyecto**

El valle central de la Región del Libertador General Bernardo O'Higgins fue declarado zona

saturada por material particulado respirable MP10, como concentración anual y de 24

horas, por medio del D.S N°7/2009 (MMA), y como zona saturada por material particulado

fino respirable MP2,5, como concentración anual y de 24 horas, por el D.S N°42/2018

(MMA), contando con un Plan De Descontaminación Atmosférica vigente, establecido en el

D.S N°15/2013 del MMA, en los cuales se incluye la comuna de Rancagua, lugar de

emplazamiento del proyecto.

**3.2** **Análisis del Cumplimiento Normativo**

Para llevar a cabo el siguiente análisis, se utilizó la Estación de Monitoreo de

Representatividad Poblacional (EMRP) de Rancagua I, la cual se ubica a aproximadamente

a 1.200 m de distancia del proyecto (Ver Figura 2). Dicha estación corresponde a la más

cercana al proyecto, y que cuenta con la mayor cantidad de información disponible para

efectos del levantamiento de información de la línea de base del proyecto, sin embargo,

no posee datos actualizados del contaminante NO 2 . La información extraída de la Estación

Rancagua I comprende el periodo 2014 - 2021.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Figura 2. Ubicación EMRP Rancagua I**

**Página 14 de 106**

El D.S. 12/2022 MMA establece la norma primaria de calidad ambiental para material

particulado respirable MP10, regulando la concentración promedio anual y diaria.

En la Figura 3 se observa que el percentil 98 de la concentración promedio 24 horas

supera los límites establecidos por la norma primaria de calidad del aire para MP10 entre

los años 2014 al 2017 junto con el año 2019. Para los restantes tres años se presentan

concentraciones menores al límite normativo. Esta estación alcanza su valor más alto para

este contaminante durante el año 2015 donde presenta un percentil 98 de 181,8 μg/m [3] .

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 15 de 106**

**Figura 3. Concentración promedio 24 horas de MP10, EMRP Rancagua I**

La concentración promedio anual de MP10 es superada en los 8 años analizados, siendo el

año 2015 aquel que posee el mayor porcentaje de excedencia, con un 61%.

**Tabla 4. Porcentaje de superación concentración promedio anual de MP10,**

**EMRP Rancagua I.**

|Año|Porcentaje de<br>datos disponibles<br>(%)|Concentración<br>Promedio Anual<br>(μg/m3N)|Límite normativo<br>D.S. 12/2022 MMA<br>(μg/m3N)|Porcentaje de<br>excedencia de la<br>norma (%)|
|---|---|---|---|---|
|2014|99%|71,9|50,0|44%|
|2015|95%|80,7|80,7|61%|
|2016|100%|72,5|72,5|45%|
|2017|98%|63,9|63,9|28%|
|2018|98%|55,1|55,1|10%|
|2019|98%|59,8|59,8|20%|
|2020|99%|55,7|55,7|11%|
|2021|97%|51,2|51,2|2%|

En la Figura 4 se presenta la concentración promedio trianual de MP10 de la Estación

Rancagua I, de donde se observa que durante todos los periodos la concentración excede

la normativa vigente de 50 μg/m3N, destacando el periodo 2014 - 2016 como el de mayor

concentración con 75 μg/m3N.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**Página 16 de 106**

80

70

60

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

50

40

30

20

10

0

|75,0|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|**75,0**|**72,4**|||||
|||**63,8**|**59,6**|**56,9**|**55,6**|
|||||||
|||||||
|||||||
|||||||
|||||||
|||||||

2014-2016 2015-2017 2016-2018 2017-2019 2018-2020 2019-2021

Concentración Trianual Límite Norma Lineal (Concentración Trianual)

**Figura 4. Concentración promedio trianual MP10, EMRP Rancagua I**

En relación con los días de alerta, preemergencia y/o emergencia de los años analizados,

se registraron un total de 10 días de alerta y 1 día de preemergencia en la estación

Rancagua I en la secuencia temporal analizada, siendo el año 2015 el que concentra las

peores condiciones, como se muestra en la Tabla 5.

<!-- INICIO TABLA 5. -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Rancagua I en la secuencia temporal analizada, siendo el año 2015 el que concentra las peores condiciones, como se muestra en la Tabla 5. -->

**Tabla 5.: Registro de días declarados en alerta, preemergencia y emergencia****

| Año | Días de alerta | Días de preemergencia | Días de emergencia |
| --- | --- | --- | --- |
| 2014 | 1 | 0 | 0 |
| 2015 | 7 | 1 | 0 |
| 2016 | 2 | 0 | 0 |
| 2017 | 0 | 0 | 0 |
| 2018 | 0 | 0 | 0 |
| 2019 | 0 | 0 | 0 |
| 2020 | 0 | 0 | 0 |
| 2021 | 0 | 0 | 0 |

<!-- Estadísticas: 8 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- El D.S. 12/2011 MMA establece la norma primaria de calidad ambiental para material particulado fino respirable MP2,5, regulando la concentración promedio anual y diaria. -->
<!-- FIN TABLA 5. -->


**Tabla 5. Registro de días declarados en alerta, preemergencia y emergencia**

**para MP10 en la EMRP Rancagua I.**

|Año|Días de alerta|Días de preemergencia|Días de emergencia|
|---|---|---|---|
|2014|1|0|0|
|2015|7|1|0|
|2016|2|0|0|
|2017|0|0|0|
|2018|0|0|0|
|2019|0|0|0|
|2020|0|0|0|
|2021|0|0|0|

El D.S. 12/2011 MMA establece la norma primaria de calidad ambiental para material

particulado fino respirable MP2,5, regulando la concentración promedio anual y diaria.

Respecto a este contaminante, la EMRP solo cuenta con datos desde del año 2017, los

cuales se presentan en el siguiente análisis.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 17 de 106**

En la Figura 5, se observa el percentil 98 de la concentración promedio 24 horas

registrado entre los años 2014 - 2021, donde se visualiza que existe superación de la

normativa durante todo el periodo analizado, siendo el año 2014 el que presenta la

mayor concentración en 24 horas con una superación de la norma en 96,6 μg/m [3], seguido

por el año 2021 con 91,7 μg/m [3] .

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||
|||||||||||||||||
|||||||**73,0**<br>|**73,0**<br>|**73,0**<br>|**73,0**<br>|**73,0**<br>||||||
|||||||||||||||||
|||||||||||||||||
|||||||||||||||||
|||||||||||||||||
|||||||||||||||||

**Figura 5. Concentración promedio 24 horas de MP2,5, EMRP Rancagua I**

La concentración promedio anual de MP2,5 que establece el D.S. 12/2011 MMA es

superada en todo el período analizado. El año 2014 es el que cuenta con el mayor

porcentaje de excedencia, con un 40%.

**Tabla 6. Porcentaje de superación concentración promedio anual de MP2,5,**

**EMRP Rancagua I.**

|Año|Porcentaje de<br>datos disponibles<br>(%)|Concentración<br>Promedio Anual<br>(μg/m3)|Límite normativo<br>D.S. 12/2011 MMA<br>(μg/m3)|Porcentaje de<br>excedencia de la<br>norma (%)|
|---|---|---|---|---|
|2014|100%|28,0|20,0|40%|
|2015|99%|24,1|24,1|20%|
|2016|100%|24,1|24,1|20%|
|2017|98%|23,4|23,4|17%|
|2018|98%|21,5|21,5|8%|
|2019|97%|24,5|24,5|23%|
|2020|98%|23,0|23,0|15%|
|2021|98%|26,0|26,0|30%|

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 18 de 106**

Con respecto a las concentraciones de MP2,5 como promedio trianual, existe superación

normativa en los tres periodos analizados, siendo el periodo de 2014 - 2016 el que

presenta la mayor concentración con 25,4 μg/m [3] .

30

25

20

15

10

5

0

|25,4|Col2|Col3|23,8|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|24,5|Col17|Col18|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||**23,0**|**23,0**|**23,0**|**23,2**|**23,2**|**23,2**|**23,0**|**23,0**|**23,0**||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||
|||||||||||||||||||

2014-2016 2015-2017 2016-2018 2017-2019 2018-2020 2019-2021

Concentración Trianual Límite Norma Lineal (Concentración Trianual)

**Figura 6. Concentración promedio trianual MP2,5, EMRP Rancagua I**

Para el período analizado se registraron 66 días declarados con alerta y 9 días declarados

con preemergencia ambiental por MP2,5, siendo el año 2014 el que exhibe un mayor

número de días en condiciones de superación, tal como muestra la Tabla 7:

**Tabla 7. Registro de días declarados en alerta, preemergencia y emergencia**

**para MP2,5 en la EMRP Rancagua I**

|Año|Días de alerta|Días de preemergencia|Días de emergencia|
|---|---|---|---|
|2014|16|3|0|
|2015|7|0|0|
|2016|10|2|0|
|2017|3|0|0|
|2018|4|1|0|
|2019|7|1|0|
|2020|5|1|0|
|2021|14|1|0|

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 19 de 106**

El D.S. 104/2019 MMA establece la norma primaria de calidad de aire para dióxido de

azufre (SO 2 ), regulando la concentración promedio anual, diaria y horaria.

El percentil 98,5 de la concentración promedio horaria de SO 2 no supera la norma en todo

el período analizado, como se observa en la Tabla 8.

**Tabla 8. Porcentaje de superación concentración horaria de SO** **2** **, EMRP**

**Rancagua I.**

|Año|Porcentaje de<br>datos disponibles<br>(%)|Concentración<br>Horaria (ppbv)|Límite normativo<br>D.S. 104/2019<br>MMA (ppbv)|Porcentaje de<br>excedencia de la<br>norma (%)|
|---|---|---|---|---|
|2014|92%|9,1|134|No excede la norma|
|2015|97%|6,2|6,2|No excede la norma|
|2016|100%|6,9|6,9|No excede la norma|
|2017|98%|5,3|5,3|No excede la norma|
|2018|98%|7,6|7,6|No excede la norma|
|2019|97%|5,6|5,6|No excede la norma|
|2020|98%|1,9|1,9|No excede la norma|
|2021|99%|1,4|1,4|No excede la norma|

Con respecto a las concentraciones horarias de SO 2 como promedio trianual, no existe

superación normativa en los seis periodos analizados, presentando su mayor

concentración el periodo de 2014 - 2016 con 7,4 ppbv, como se observa en la Figura 7.

**Figura 7. Concentración promedio trianual horaria de SO** **2** **, EMRP Rancagua I**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 20 de 106**

El percentil 99 de la concentración promedio en 24 horas de SO 2 tampoco supera la norma

en todo el período analizado, siendo su mayor concentración 11,8 ppbv el año 2015, como

se observa en la Tabla 9.

**Tabla 9. Porcentaje de superación concentración 24 horas de SO** **2** **, EMRP**

**Rancagua I.**

|Año|Porcentaje de<br>datos disponibles<br>(%)|Concentración<br>24 Horas (ppbv)|Límite normativo<br>D.S. 104/2019<br>MMA (ppbv)|Porcentaje de<br>excedencia de la<br>norma (%)|
|---|---|---|---|---|
|2014|92%|7,7|57|No excede la norma|
|2015|97%|11,8|11,8|No excede la norma|
|2016|100%|8,5|8,5|No excede la norma|
|2017|98%|8,4|8,4|No excede la norma|
|2018|98%|9,0|9,0|No excede la norma|
|2019|97%|5,5|5,5|No excede la norma|
|2020|98%|1,8|1,8|No excede la norma|
|2021|99%|1,3|1,3|No excede la norma|

En la Figura 8 se presenta la concentración 24 horas como promedio trianual de SO 2 de la

Estación Rancagua I, de donde se observa que durante todos los periodos la

concentración no excede la normativa vigente de 57 ppbv, presentando una tendencia

decreciente.

**Figura 8. Concentración promedio trianual 24 horas de SO** **2** **, EMRP Rancagua I**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 21 de 106**

La concentración promedio anual de SO 2 no es superada en todo el período analizado,

siendo el año 2018 aquel que posee la mayor concentración con 3,9 ppbv.

**Tabla 10. Porcentaje de superación concentración promedio anual de SO** **2** **,**

**EMRP Rancagua I.**

|Año|Porcentaje de<br>datos disponibles<br>(%)|Concentración<br>Anual (ppbv)|Límite normativo<br>D.S. 104/2019<br>MMA (ppbv)|Porcentaje de<br>excedencia de la<br>norma (%)|
|---|---|---|---|---|
|2014|92%|2,1|23|No excede la norma|
|2015|97%|2,0|2,0|No excede la norma|
|2016|100%|2,0|2,0|No excede la norma|
|2017|98%|2,3|2,3|No excede la norma|
|2018|98%|3,9|3,9|No excede la norma|
|2019|97%|1,8|1,8|No excede la norma|
|2020|98%|1,1|1,1|No excede la norma|
|2021|99%|1,0|1,0|No excede la norma|

Con respecto a las concentraciones de SO 2 como promedio trianual, no existe superación

normativa en los seis periodos analizados, siendo los periodos de 2016 - 2018 y 2017

2019 los que presentan la mayor concentración con 2,7 ppbv.

25

20

15

10

5

0

|Col1|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|||||||
|||||||
|||||||
|||||||
|**2,0**|**2,1**|**2,7**|**2,7**|**2,2**|**1,3**|

2014-2016 2015-2017 2016-2018 2017-2019 2018-2020 2019-2021

Concentración Trianual Límite Norma Lineal (Concentración Trianual)

**Figura 9. Concentración promedio trianual de SO** **2** **, EMRP Rancagua I**

En relación con los días de alerta, preemergencia y/o emergencia de los años analizados,

se registraron un total de 6 días de alerta y 8 días de preemergencia en la estación

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 22 de 106**

Rancagua I en la secuencia temporal analizada, siendo el año 2015 el que concentra la

mayor cantidad de días en dichas condiciones, como se muestra en la Tabla 11.

<!-- INICIO TABLA 11. -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Rancagua I en la secuencia temporal analizada, siendo el año 2015 el que concentra la mayor cantidad de días en dichas condiciones, como se muestra en la Tabla 11. -->

**Tabla 11.: Registro de días declarados en alerta, preemergencia y emergencia****

| Año | Días de alerta | Días de preemergencia | Días de emergencia |
| --- | --- | --- | --- |
| 2014 | 0 | 0 | 0 |
| 2015 | 4 | 7 | 0 |
| 2016 | 1 | 1 | 0 |
| 2017 | 1 | 0 | 0 |
| 2018 | 0 | 0 | 0 |
| 2019 | 0 | 0 | 0 |
| 2020 | 0 | 0 | 0 |
| 2021 | 0 | 0 | 0 |

<!-- Estadísticas: 8 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- El D.S. 115/2002 MINSEGEPRES establece la norma primaria de calidad de aire para monóxido de carbono (CO), regulando la concentración en 8 horas y horaria. -->
<!-- FIN TABLA 11. -->


**Tabla 11. Registro de días declarados en alerta, preemergencia y emergencia**

**para SO** **2** **en la EMRP Rancagua I**

|Año|Días de alerta|Días de preemergencia|Días de emergencia|
|---|---|---|---|
|2014|0|0|0|
|2015|4|7|0|
|2016|1|1|0|
|2017|1|0|0|
|2018|0|0|0|
|2019|0|0|0|
|2020|0|0|0|
|2021|0|0|0|

El D.S. 115/2002 MINSEGEPRES establece la norma primaria de calidad de aire para

monóxido de carbono (CO), regulando la concentración en 8 horas y horaria.

El percentil 99 de los máximos diarios de concentración de 1 hora para CO no supera la

norma en todo el período analizado, llegando a su máximo el año 2018 con 10,6 ppmv,

como se observa en la Tabla 12.

**Tabla 12. Porcentaje de superación concentración máxima horaria CO, EMRP**

**Rancagua I.**

|Año|Porcentaje de<br>datos disponibles<br>(%)|Concentración<br>Horaria (ppmv)|Límite normativo<br>D.S. 115/2002<br>MINSEGEPRES<br>(ppmv)|Porcentaje de<br>excedencia de la<br>norma (%)|
|---|---|---|---|---|
|2014|94%|4,5|26|No excede la norma|
|2015|99%|9,3|9,3|No excede la norma|
|2016|100%|8,8|8,8|No excede la norma|
|2017|98%|7,5|7,5|No excede la norma|
|2018|96%|10,6|10,6|No excede la norma|
|2019|98%|4,6|4,6|No excede la norma|
|2020|98%|3,8|3,8|No excede la norma|
|2021|99%|4,3|4,3|No excede la norma|

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 23 de 106**

En la Figura 10 se presenta la concentración máxima horaria como promedio trianual de

CO de la Estación Rancagua I, donde se observa que durante todos los periodos la

concentración no excede la normativa vigente de 26 ppmv.

**Figura 10. Concentración promedio trianual horaria de CO, EMRP Rancagua I**

El percentil 99 de los máximos diarios de concentración de 8 horas para CO que establece

el D.S. 115/2002 MINSEGEPRES no es superada en todo el período analizado, siendo el

año 2018 el que cuenta con la mayor concentración, con 4,2 ppmv.

**Tabla 13. Porcentaje de superación concentración máxima 8 horas CO, EMRP**

**Rancagua I.**

|Año|Porcentaje de<br>datos disponibles<br>(%)|Concentración 8<br>Horas (ppmv)|Límite normativo<br>D.S. 115/2002<br>MINSEGEPRES<br>(ppmv)|Porcentaje de<br>excedencia de la<br>norma (%)|
|---|---|---|---|---|
|2014|94%|2,9|9|No excede la norma|
|2015|99%|3,2|3,2|No excede la norma|
|2016|100%|3,1|3,1|No excede la norma|
|2017|98%|4,1|4,1|No excede la norma|
|2018|96%|4,2|4,2|No excede la norma|
|2019|98%|3,1|3,1|No excede la norma|
|2020|98%|2,8|2,8|No excede la norma|
|2021|99%|3,1|3,1|No excede la norma|

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 24 de 106**

La concentración máxima de 8 horas como promedio trianual para CO, no muestra

superación normativa en los seis periodos analizados, siendo los periodos de 2016 - 2018

y 2017 - 2019 los que presentan la mayor concentración con 3,8 ppmv, como se puede

observar en la Figura 11.

**Figura 11. Concentración promedio trianual 8 horas de CO, EMRP Rancagua I**

En relación con los días de alerta, preemergencia y/o emergencia en los años analizados

para el CO, no se registró ninguna de las condiciones de superación en la estación

Rancagua I.

**4** **Justificación de los modelos utilizados en el estudio**

El Servicio de Evaluación Ambiental en la “Guía para el Uso de Modelos de Calidad del Aire

en el SEIA” (2012) hace una serie de recomendaciones para la modelación de

contaminantes primarios [1] y secundarios en el aire. En la actualidad, esta guía es el único

documento existente como parámetro para la modelación de calidad del aire y tiene como

objetivo uniformar los criterios, exigencias técnicas y antecedentes para la evaluación de

los impactos asociados a este componente de proyectos que ingresen al Servicio de

Evaluación Ambiental. Dentro de las recomendaciones de la guía está el uso del modelo de

1 Los contaminantes primarios son los producidos directamente por la actividad humana o la
naturaleza a la atmósfera.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 25 de 106**

dispersión CALPUFF y sugiere a utilizar el modelo meteorológico WRF, los cuales fueron

utilizados en la modelación de las partículas del proyecto.

A continuación, se presenta la justificación de los modelos utilizados en el proyecto para

ejecución de la modelación de dispersión y concentración de emisiones de partículas en el

aire.

**4.1** **Uso del modelo CALPUFF**

La modelación de dispersión atmosférica de partículas provenientes del proyecto se realizó

con un modelo tipo “Puff”, específicamente el modelo CALPUFF. Tal como lo define la

guía, los modelos tipo “puff” son una combinación entre los modelos Gaussianos y los

modelos Lagrangeanos, en el sentido de que esencialmente calculan la dispersión de

contaminantes provenientes de una emisión instantánea, llamada “puff”, a lo largo de una

trayectoria. Su aproximación matemática consiste en estimar la dispersión en forma

Gaussiana en cada punto de una trayectoria; es decir, los modelos tipo “puff” sólo

requieren una trayectoria por “puff”, lo que hace su cálculo mucho más rápido. En el caso

de emisiones continuas, se simulan las trayectorias y la dispersión Gaussiana de muchos

“puffs”, como es en el caso de las emisiones de partículas generadas por el proyecto. Al

respecto, el modelo tipo “puff” recomendado por la Guía es el modelo **CALPUFF** .

Así mismo, es un modelo completo que incorpora herramientas para procesar datos

meteorológicos y geofísicos, modelos de dispersión y post procesamiento. Dicho modelo

es recomendado por la Agencia de Protección Ambiental de los Estados Unidos (EPA) para

modelar transporte a larga distancia de contaminantes.

CALPUFF se compone de tres módulos:

 CALMET: Es un modelo meteorológico que desarrolla campos horarios de viento y

temperatura en una grilla de tres dimensiones. También asocia campos en dos

dimensiones de altura y usos de suelo. **Este modelo fue reemplazado por el**

**WRF, tal como lo recomienda la guía antes citada.**

 CALPUFF: Es un modelo de transporte y dispersión de partículas emitidas desde

fuentes modeladas, simulando procesos de dispersión y transformación. CALPUFF

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 26 de 106**

utiliza los datos generados por CALMET. Los archivos de salida de CALPUFF

contienen las concentraciones horarias o deposición por hora de flujos evaluados

en receptores seleccionados.

 CALPOST: Es usado para procesar aquellos archivos generados por CALMET y

CALPUFF, produciendo tabulaciones que resumen los resultados de la simulación.

Ecuación del modelo CALPUFF

La ecuación básica que utiliza el modelo para realizar la modelación es la siguiente:

2

2σ

[−d] y [2][c] ~~[]]~~

2

Q
C=
2πσ x σ y

2
g=
(2π) [1 2] ⁄ σ z

2

g exp[ [−d] 2σ x [2][a]

∑exp[ [−(H] [e] 2σ [+ 2nh)] z [2] [2]

2 2

[−d] 2σ x [2][a] ~~[]]~~ [ exp] ~~[[]~~ [−d] 2σ y [2][c]

2

∞

n=−∞

[+ 2nh)] [2]

2σ z [2] ]

Dónde:

**C**, es concentración a nivel del suelo (g/m [3] ),

**Q**, es masa de contaminantes (g) en la nube.

**σ** **x** **,** es desviación estándar (m) de la distribución de Gauss en el viento a lo largo de la

dirección.

**σ** **y** **,** es desviación estándar (m) de la distribución de Gauss en el viento de costado.

**σ** **z**, es desviación estándar (m) de la distribución de Gauss en la dirección vertical.

**d** **a** **,** es distancia (m) del centro de la nube al receptor en la dirección del viento a lo largo.

**d** **c**, es distancia (m) del centro de la nube al receptor en la dirección de viento cruzado.

**g**, es el término vertical (m [-1] ) de la ecuación Gaussiana.

**H**, es la altura afectiva (m) desde el nivel del suelo del hojaldre.

**h**, es la altura de la capa de mezcla.

El terreno en el cual se realizará la modelación de las emisiones de partículas se considera

heterogéneo, debido a las distintas unidades geomorfológicas. Por esta razón y en

consistencia con las recomendaciones del SEA para la modelación de partículas en sus

guías, se consideró utilizar el modelo CALPUFF para simular la dispersión y concentración

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 27 de 106**

de las emisiones de partículas generadas por la futura operación del proyecto.

**4.2** **Uso del modelo WRF**

El modelo Weather Research and Forecasting (WRF), es un modelo numérico de cuatro

dimensiones, recomendado para la generación de datos meteorológicos y es uno de los

modelos de pronóstico meteorológicos más avanzados.

Debido a la falta de una red robusta de estaciones meteorológicas, la “Guía para el Uso de

Modelos de Calidad del Aire en el SEIA” recomienda el uso de WRF por sobre el uso del

CALMET. Además, el mismo documento, sugiere el uso del WRF para la modelación de

dispersión de contaminantes con CALPUFF.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 28 de 106**

**5** **Metodología**

**5.1** **Modelación de partículas**

La modelación de partículas depende en gran parte de las tasas de emisión. Estos son

acoplados a un modelo meteorológico, el que en sí mismo simula las condiciones

meteorológicas para la zona de estudio con una resolución temporal de 1 hora; con estos

factores como variable de entrada al modelo, es simulada la dispersión de las partículas en

un modelo, que determinará la trayectoria de las partículas dentro del área de estudio.

**5.1.1** **Modelación meteorológica**

Para la modelación meteorológica, se utilizó un modelo WRF, construido con datos del año

2021 y resolución de 1 km, de extensión 57 km x 57 km. El modelo WRF es capaz de

simular el comportamiento meteorológico, a través de datos meteorológicos para el año

de estudio, el que posteriormente es interpolado dentro del área de estudio del modelo de

acuerdo con la topografía del lugar. En la Tabla 14 se resumen las características del

modelo.

**Tabla 14. Características del modelo**

|Año de modelación|Col2|2021|
|---|---|---|
|**Periodo de Modelación**|**Periodo de Modelación**|1 año calendario|
|**Resolución temporal**|**Resolución temporal**|1 hora|
|**Resolución espacial**|**Resolución espacial**|1 km|
|**Coordenadas del centroide**|**Latitud**|-34,193°|
|**Coordenadas del centroide**|**Longitud**|-70,731°|
|**DATUM**|**DATUM**|NWS - 84|
|**Coordenadas del modelo**|**Coordenadas del modelo**|LCC|
|**Dominio de modelación**|**X **|57|
|**Dominio de modelación**|**Y **|57|
|**Dominio de modelación**|**Z **|10|

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**5.1.2** **Modelación de dispersión de contaminantes**

**Página 29 de 106**

El modelo CALPUFF permite la simulación de la dispersión de contaminantes bajo dos

modalidades:

 **Modelación de la grilla de modelación** . La grilla de modelación viene seteada

del modelo meteorológico, acotando la simulación en la zona circundante más

próxima al proyecto, incluyendo las zonas pobladas importantes de evaluar. Dicha

grilla de modelación tiene una resolución espacial de 1 km.

Este es el método más usual para la interpolación de las concentraciones de los

puntos de grilla (1 km), interpolando entre cada punto la concentración, hasta

obtener la pluma de dispersión. Por defecto la modelación de los puntos de grilla

entrega el valor de la concentración como el promedio en la primera capa de

modelación, la que ocurre entre los 0 y 20 m sobre el nivel del suelo.

En virtud de la resolución espacial del modelo y de la altura de la primera capa de

modelación, y al tratarse de áreas de emisión que se generan a altura del suelo o a

baja altura [2], muchas veces la obtención de la pluma de dispersión se genera con

valores sub dimensionados, por lo tanto, en ocasiones es necesario realizar una

sub grilla de modelación a través de la modelación de puntos discretos,

aumentando la densidad de puntos de modelación y mejorando la evaluación de la

concentración simulada dentro del espacio circundante. De este modo, se generó

una subgrilla de 1,5 km x 1,5 km desde el centroide del proyecto con una

separación de 100 metros entre cada punto.

 **Modelación de puntos discretos.** Se consideraron 19 puntos discretos cercanos

al proyecto. Las coordenadas se presentan a continuación y se presenta

espacialmente en la figura adjunta.

2 Como es el caso del tránsito y de las obras asociadas al movimiento de tierra.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 30 de 106**

**Tabla 15. Descripción de los puntos receptores**

|Receptor|Coordenada UTM WGS 84 HUSO 19 S|Col3|Descripción|Distancia al<br>centro del<br>proyecto (m)|
|---|---|---|---|---|
|**Receptor**|**Este (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|
|1|343.218|6.219.033|Vivienda I|200|
|2|343.411|6.218.900|Vivienda II|242|
|3|343.380|6.218.678|Vivienda III|258|
|4|343.193|6.218.692|Situación basal|146|
|5|343.094|6.218.644|Vivienda IV|210|
|6|342.930|6.218.700|Colegio San Sebastián School|282|
|7|342.875|6.218.841|Vivienda V|302|
|8|343.030|6.219.047|Vivienda VI|256|
|9|343.197|6.219.156|Vivienda VII|320|
|10|343.335|6.219.105|Plaza|311|
|11|343.708|6.218.847|Vivienda VIII|531|
|12|343.616|6.218.437|Vivienda IX|594|
|13|343.345|6.218.091|Vivienda X|765|
|14|343.100|6.218.361|Vivienda XI|482|
|15|342.845|6.218.290|Parque Villa Nueva Cordillera|640|
|16|342.453|6.218.756|Vivienda XII|729|
|17|342.946|6.219.279|Cancha Club Unión Gamboina|499|
|18|342.443|6.219.920|CESFAM Ignacio Caroca|1.308|
|19|342.015|6.218.518|EMRP Rancagua I|1.205|

Nota: La distancia de los receptores se midió al centro del proyecto, en la coordenada

UTM WGS 84 HUSO 19 S x: 343.177 m e y: 6.218.837 m.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Figura 12. Receptores discretos**

**5.1.3** **Criterios para la modelación de partículas**

**Página 31 de 106**

Como escenario de modelación se consideró el año de máxima emisión de MP dentro del

polígono del proyecto, como se indica en la tabla 68 de la actualización del informe de

estimación de emisiones, lo que ocurre durante el año 1 del proyecto. Durante este año se

presenta la mayor emisión de MP directo debido a que se construyen 120 viviendas en

paralelo con la entrada en operación de 264 unidades habitacionales de la situación basal

durante el segundo semestre. Esto conlleva la realización de actividades propias a la

construcción de las viviendas, junto a un mayor tránsito por caminos internos

pavimentados y combustión de kerosene para calefacción, aumentando así, la emisión de

MP. Los detalles de la estimación de emisiones se presentan en el informe de Estimación

de Emisiones Atmosféricas. Para la fase de construcción se ingresaron los polígonos donde

se generan el tránsito en rutas pavimentadas y tránsito en rutas no pavimentadas al

interior del proyecto, junto a los polígonos que representan el área de construcción en el

año 1, donde se ejecutan las actividades de escarpe, excavaciones, transferencias de

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 32 de 106**

material, compactación y uso de maquinaria, además del tránsito en rutas pavimentadas

externo más cercanas al proyecto. Para la fase de operación se incorporó los polígonos

donde se generan el tránsito en rutas pavimentadas internas, el área representante de la

calefacción domiciliaria y el tránsito en rutas pavimentadas externo más cercano al

proyecto.

Adicionalmente, se modelaron las emisiones de gases precursores de MP10 y MP2,5 en el

aire a través del módulo MESOPUFF II.

De acuerdo con la metodología aplicable, se realizaron polígonos representativos de cada

unidad para la simulación de las áreas de emisiones de partículas, las que fueron

modeladas como fuentes de emisión discontinuas, es decir, dentro del ciclo diurno, se

consideró para la fase de construcción la generación de emisiones durante 9 horas (8:00 a

18:00 hrs), correspondiente al horario laboral establecido para el proyecto, y se consideró

para la fase de operación la generación de emisiones durante 16 horas (6:00 a 20:00 hrs),

simulando dicho periodo como el de uso de los vehículos por parte de los residentes.

Además, se consideró para la fase de operación un ciclo estacional para la calefacción

domiciliaria, donde la generación de dichas emisiones se situó en las estaciones de otoño

e invierno durante 15 horas del día. Las coordenadas de los polígonos utilizados se

encuentran en la Tabla 16, así como también, en la Figura 13 se presenta la ubicación

espacial de éstos.

**Tabla 16. Coordenadas de modelación de las fuentes areales**

|Actividad para<br>modelar|Unidad del<br>proyecto|Área (m2)|Coordenada UTM. HUSO 19 S.<br>DATUM WGS 84|Col5|
|---|---|---|---|---|
|**Actividad para**<br>**modelar**|**Unidad del**<br>**proyecto**|**Área (m2) **|**Este (m)**|**Norte (m)**|
|Polígono<br>Construcción|P1|11.596|343.262|6.218.682|
|Polígono<br>Construcción|P1|11.596|343.285|6.218.850|
|Polígono<br>Construcción|P1|11.596|343.168|6.218.765|
|Polígono<br>Construcción|P1|11.596|343.256|6.218.874|
|Polígono<br>Construcción|P2|9.886|343.256|6.218.874|
|Polígono<br>Construcción|P2|9.886|343.184|6.218.787|
|Polígono<br>Construcción|P2|9.886|343.176|6.218.942|
|Polígono<br>Construcción|P2|9.886|343.132|6.218.833|
|Polígono<br>Construcción|P3|4.891|343.176|6.218.942|
|Polígono<br>Construcción|P3|4.891|343.249|6.218.881|
|Polígono<br>Construcción|P3|4.891|343.214|6.218.988|
|Polígono<br>Construcción|P3|4.891|343.264|6.218.950|

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 33 de 106**

|Actividad para<br>modelar|Unidad del<br>proyecto|Área (m2)|Coordenada UTM. HUSO 19 S.<br>DATUM WGS 84|Col5|
|---|---|---|---|---|
|**Actividad para**<br>**modelar**|**Unidad del**<br>**proyecto**|**Área (m2) **|**Este (m)**|**Norte (m)**|
|**Actividad para**<br>**modelar**|P4|2.359|343.176|6.218.942|
|**Actividad para**<br>**modelar**|P4|2.359|343.132|6.218.833|
|**Actividad para**<br>**modelar**|P4|2.359|343.134|6.218.889|
|**Actividad para**<br>**modelar**|P4|2.359|343.093|6.218.921|
|**Actividad para**<br>**modelar**|P5|3.965|343.132|6.218.833|
|**Actividad para**<br>**modelar**|P5|3.965|343.093|6.218.921|
|**Actividad para**<br>**modelar**|P5|3.965|343.114|6.218.815|
|**Actividad para**<br>**modelar**|P5|3.965|343.051|6.218.870|
|Ruta Interna NPAV<br>Construcción|P6|881|343.216|6.218.991|
|Ruta Interna NPAV<br>Construcción|P6|881|343.219|6.218.988|
|Ruta Interna NPAV<br>Construcción|P6|881|343.089|6.218.837|
|Ruta Interna NPAV<br>Construcción|P6|881|343.092|6.218.834|
|Ruta Interna NPAV<br>Construcción|P7|649|343.112|6.218.859|
|Ruta Interna NPAV<br>Construcción|P7|649|343.110|6.218.856|
|Ruta Interna NPAV<br>Construcción|P7|649|343.245|6.218.744|
|Ruta Interna NPAV<br>Construcción|P7|649|343.243|6.218.741|
|Ruta Interna PAV<br>Construcción|P8|24|343.088|6.218.837|
|Ruta Interna PAV<br>Construcción|P8|24|343.091|6.218.835|
|Ruta Interna PAV<br>Construcción|P8|24|343.084|6.218.831|
|Ruta Interna PAV<br>Construcción|P8|24|343.089|6.218.831|
|Ruta Interna PAV<br>Construcción|P9|629|343.084|6.218.831|
|Ruta Interna PAV<br>Construcción|P9|629|343.089|6.218.831|
|Ruta Interna PAV<br>Construcción|P9|629|343.232|6.218.701|
|Ruta Interna PAV<br>Construcción|P9|629|343.234|6.218.703|
|Ruta Interna PAV<br>Operación|P10|80|343.221|6.218.671|
|Ruta Interna PAV<br>Operación|P10|80|343.224|6.218.669|
|Ruta Interna PAV<br>Operación|P10|80|343.239|6.218.694|
|Ruta Interna PAV<br>Operación|P10|80|343.243|6.218.696|
|Ruta Interna PAV<br>Operación|P11|1.080|343.239|6.218.694|
|Ruta Interna PAV<br>Operación|P11|1.080|343.243|6.218.696|
|Ruta Interna PAV<br>Operación|P11|1.080|343.048|6.218.863|
|Ruta Interna PAV<br>Operación|P11|1.080|343.051|6.218.866|
|Ruta Externa PAV|P12|286|343.217|6.218.994|
|Ruta Externa PAV|P12|286|343.214|6.218.991|
|Ruta Externa PAV|P12|286|343.163|6.219.031|
|Ruta Externa PAV|P12|286|343.165|6.219.024|
|Ruta Externa PAV|P13|3.734|343.163|6.219.031|
|Ruta Externa PAV|P13|3.734|343.165|6.219.024|
|Ruta Externa PAV|P13|3.734|342.782|6.218.544|
|Ruta Externa PAV|P13|3.734|342.778|6.218.547|
|Ruta Externa PAV|P14|348|342.782|6.218.544|
|Ruta Externa PAV|P14|348|342.778|6.218.547|
|Ruta Externa PAV|P14|348|342.725|6.218.497|

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 34 de 106**

|Actividad para<br>modelar|Unidad del<br>proyecto|Área (m2)|Coordenada UTM. HUSO 19 S.<br>DATUM WGS 84|Col5|
|---|---|---|---|---|
|**Actividad para**<br>**modelar**|**Unidad del**<br>**proyecto**|**Área (m2) **|**Este (m)**|**Norte (m)**|
|**Actividad para**<br>**modelar**|**Unidad del**<br>**proyecto**|**Área (m2) **|342.724|6.218.502|
|**Actividad para**<br>**modelar**|P15|374|342.725|6.218.497|
|**Actividad para**<br>**modelar**|P15|374|342.724|6.218.502|
|**Actividad para**<br>**modelar**|P15|374|342.640|6.218.497|
|**Actividad para**<br>**modelar**|P15|374|342.638|6.218.500|
|**Actividad para**<br>**modelar**|P16|1.680|342.640|6.218.497|
|**Actividad para**<br>**modelar**|P16|1.680|342.638|6.218.500|
|**Actividad para**<br>**modelar**|P16|1.680|342.417|6.218.205|
|**Actividad para**<br>**modelar**|P16|1.680|342.413|6.218.208|
|**Actividad para**<br>**modelar**|P17|767|342.607|6.218.460|
|**Actividad para**<br>**modelar**|P17|767|342.603|6.218.456|
|**Actividad para**<br>**modelar**|P17|767|342.492|6.218.529|
|**Actividad para**<br>**modelar**|P17|767|342.490|6.218.524|
|**Actividad para**<br>**modelar**|P18|1.438|342.492|6.218.529|
|**Actividad para**<br>**modelar**|P18|1.438|342.490|6.218.524|
|**Actividad para**<br>**modelar**|P18|1.438|342.276|6.218.573|
|**Actividad para**<br>**modelar**|P18|1.438|342.274|6.218.566|
|**Actividad para**<br>**modelar**|P19|3.288|342.276|6.218.573|
|**Actividad para**<br>**modelar**|P19|3.288|342.274|6.218.566|
|**Actividad para**<br>**modelar**|P19|3.288|341.802|6.218.770|
|**Actividad para**<br>**modelar**|P19|3.288|341.801|6.218.765|
|Operación Año 1|P20|22.880|343.262|6.218.683|
|Operación Año 1|P20|22.880|343.252|6.218.605|
|Operación Año 1|P20|22.880|343.051|6.218.869|
|Operación Año 1|P20|22.880|343.000|6.218.804|
|Operación Año 1|P21|1.849|343.132|6.218.834|
|Operación Año 1|P21|1.849|343.114|6.218.814|
|Operación Año 1|P21|1.849|343.184|6.218.787|
|Operación Año 1|P21|1.849|343.167|6.218.767|

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 35 de 106**

**Figura 13. Polígonos de modelación representativos de cada unidad modelada.**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 36 de 106**

## 6 Resultados

**6.1** **Modelamiento meteorológico**

**6.1.1** **Caracterización Geofísica de la zona de estudio**

En la Figura 14, se observa la topografía de la zona de emplazamiento del proyecto, de

donde se puede ver que el proyecto se emplaza en un valle, caracterizado por amplias

zonas planas de elevación cercana a los 250 m.s.n.m. y formaciones de elevaciones más

grandes llegando a los 2750 m.s.n.m.

El proyecto se encuentra particularmente en la cota 500 m.s.n.m.

**Figura 14. Elevación del terreno en el área de la modelación meteorológica**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 37 de 106**

**6.1.2** **Caracterización de la velocidad y dirección de los vientos Anual y**

**Estacional.**

En la Figura 15 se presenta la rosa de vientos anual, construida en base a los datos

generados con el modelo WRF con información del año 2021 para la comuna de Rancagua

y sus alrededores.

**Figura 15. Rosa de los vientos anual, WRF 2021.**

La rosa de vientos resultante da cuenta que los vientos simulados tienen su origen desde

las componentes suroeste, oeste suroeste y nor noreste. Los vientos entre estas

coordenadas abarcan un 53 % del total de las direcciones de origen de los vientos en la

zona. El origen de los vientos con mayor frecuencia es la componente suroeste, con un

33,65% del origen de los vientos totales, seguida por la componente oeste suroeste, con

un 12,10%.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 38 de 106**

En el gráfico de la Figura 16 podemos ver la frecuencia de la velocidad de viento. Se

observa una mayor tendencia a vientos entre 0,5-2,1 m/s los cuales representan un

39,0% del total de velocidades simuladas.

**Figura 16. Frecuencia de los vientos, año 2021.**

**6.1.2.1** **Dirección y velocidad de vientos predominantes en verano.**

Como se observa en la siguiente figura, la simulación meteorológica da cuenta que los

vientos simulados tienen su origen desde las componentes suroeste, oeste suroeste y

oeste. Los vientos entre estas coordenadas abarcan un 56,6% del total de las direcciones

de origen de los vientos en la zona. El origen de los vientos con mayor frecuencia es la

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 39 de 106**

componente suroeste, con un 33,8% del origen de los vientos totales, seguida por la

componente oeste suroeste, con un 16,15%.

**Figura 17. Rosa de los vientos verano, WRF 2021.**

En la Figura 18 podemos ver la frecuencia de la velocidad de viento para los meses de

verano. Se observa una mayor tendencia a vientos entre 0,5-2,1 m/s, los cuales

representan un 45,1% del total de velocidades simuladas.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 40 de 106**

**Figura 18. Frecuencia de los vientos en verano, año 2021.**

**6.1.2.2** **Dirección y velocidad de vientos predominantes en otoño.**

En la Figura 19 se presenta la rosa de los vientos la cual da cuenta que los vientos

simulados tienen su origen desde las componentes suroeste, oeste suroeste y nor noreste.

Los vientos entre estas coordenadas abarcan un 50,8% del total de las direcciones de

origen de los vientos en la zona. El origen de los vientos con mayor frecuencia es la

componente suroeste, con un 33,5% del origen de los vientos totales, seguido por los

vientos con origen del oeste suroeste, con un 10,4%.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 41 de 106**

**Figura 19. Rosa de los vientos otoño, WRF 2021.**

En la siguiente figura se presenta la frecuencia de los vientos para categoría de vientos

simulados en los meses de otoño, en ella podemos ver que hay tendencia a modelar

vientos entre 0,5-2,1, los cuales representan un 41,5% del total de velocidades simuladas.

Seguido por las velocidades entre 2,1-3,6 y velocidades entre 3,6-5,7 con un 28,7% y

14,6% respectivamente.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 42 de 106**

**Figura 20. Frecuencia de los vientos en otoño, año 2021.**

**6.1.2.3** **Dirección y velocidad de vientos predominantes en invierno.**

En la Figura 21, se presenta la rosa de los vientos para el invierno simulada a través de

WRF. La rosa de vientos resultante da cuenta que los vientos simulados tienen su origen

desde las componentes suroeste, noreste y nor noreste. Los vientos entre estas

coordenadas abarcan un 45,9% del total de las direcciones de origen de los vientos en la

zona. El origen de los vientos con mayor frecuencia es la componente suroeste, con un

24,8% del origen de los vientos totales, seguido por los vientos con origen del noreste,

con un 11,1%.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 43 de 106**

**Figura 21. Rosa de los vientos invierno, WRF 2021.**

En la siguiente figura se muestra la frecuencia de los vientos simulados para cada

categoría de velocidad por el modelo meteorológico, de donde podemos ver la frecuencia

de la velocidad de viento para los meses de invierno. Podemos observar que hay

tendencia a modelar vientos entre 0,5-2,1, los cuales representan un 32,9% del total de

velocidades simuladas.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 44 de 106**

**Figura 22. Frecuencia de los vientos en invierno, año 2021.**

**6.1.2.4** **Dirección y velocidad de vientos predominantes en primavera.**

La simulación meteorológica presentada en la Figura 23, da cuenta que los vientos

simulados tienen su origen desde las componentes sur suroeste, oeste y sur. Los vientos

entre estas coordenadas abarcan un 62,7% del total de las direcciones de origen de los

vientos en la zona. El origen de los vientos con mayor frecuencia es la componente

suroeste, con un 43,5% del origen de los vientos totales, seguido por los vientos con

origen del oeste suroeste, con un 13,6%.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 45 de 106**

**Figura 23. Rosa de los vientos en primavera, WRF 2021.**

En el gráfico de frecuencia de velocidad del viento de la Figura 24 se observa que hay

tendencia a modelar vientos entre 0,5-2,1, los cuales representan un 36,8% del total de

velocidades simuladas. En segundo y tercer lugar encontramos los rangos de velocidades

de 2,1 - 3,6 y 3,6 -5,7 con un 34,6% y 20,7% respectivamente.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 46 de 106**

**Figura 24. Frecuencia de los vientos en primavera, año 2021.**

**6.1.2.5** **Perfil diario de las velocidades del viento anuales.**

En la Figura 25 se presenta el perfil horario promedio de las velocidades del viento para

cada estación del año, además de su evolución con respecto a las velocidades anuales,

con los datos extraídos del modelo WRF del 2021.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 47 de 106**

**Figura 25. Perfil diario de velocidad del viento, WRF año 2021.**

Se aprecia de la figura anterior, que el comportamiento de la velocidad de los vientos para

las distintas estaciones del año, en relación con la variación anual, es muy similar. Se

aprecia que la velocidad de los vientos en las distintas estaciones del año sigue la misma

tendencia que las velocidades anuales.

Vemos que la velocidad del viento tiende a disminuir constantemente entre las 00:00 a

06:00 horas, luego comienzan a aumentar alcanzando su máximo entre las 14 y 17 UTC,

alcanzando variación mayor a 2,86 m/s. Esta diferencia aumenta a 4,38 m/s en verano y

disminuye a 1,52 m/s en invierno. Estas variaciones se deben a las diferencias en las

temperaturas alcanzadas en dichas estaciones.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**6.1.3** **Caracterización de la Temperatura del Aire**

**6.1.3.1** **Temperatura Mensual**

**Página 48 de 106**

En la Figura 26 se aprecia la variabilidad anual de la temperatura promedio mensual

mínima, máxima y promedio, simulada con el modelo meteorológico WRF. La simulación

indica que la temperatura promedio mensual disminuye durante los meses de otoño e

invierno y aumentan durante los meses más cálidos (primavera y verano).

**Figura 26. Temperatura Mensual WRF, año 2021.**

En este sentido la temperatura promedio más alta se simuló para el mes de febrero,

donde alcanzarían los 22,6°C, en tanto que la mínima temperatura promedio mensual se

espera en el mes de julio donde llegaría a los 12,7°C.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 49 de 106**

Con respecto a la amplitud térmica se observa que esta es mayor en el mes de diciembre

con un valor de 25,52°C, mientras que la más baja ocurre en el mes de julio, alcanzado

los 18,53°C.

**6.1.3.2** **Perfil Diario de la Temperatura**

La Figura 27 muestra el perfil promedio diario de temperaturas para el punto de análisis,

simulado con WRF. La simulación del modelo meteorológico WRF dentro del área de

estudio, demuestra que las temperaturas horarias simuladas tienen una misma tendencia

en todas las estaciones del año. En efecto, tal como se muestra en la Figura 27, la

evolución de la temperatura diaria resulta tener una leve diminución entre las 00:00 y

09:00 horas, a partir de entonces la temperatura aumenta hasta alcanzar temperaturas

máximas entre las 12:00 y 16:00 horas, luego la temperatura disminuye constantemente

hasta las 23:00 horas.

**Figura 27. Perfil diario de Temperatura, WRF año 2021.**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 50 de 106**

Además, se hace visible que en los meses de verano la amplitud térmica diaria es mayor

que en las otras estaciones del año, llegando a una diferencia de 12,90°C entre la mínima

y máxima promedio horario. Durante los meses de primavera la amplitud térmica es

menor bordeando los 10,25°C. Durante los meses de otoño la amplitud térmica es menor

bordeando los 9,58°C. Por último, en los meses de invierno la amplitud termina es inferior

a la alcanzada en las otras estaciones llegando los 6,30°C.

**6.1.4** **Altura de Capa de Mezcla**

La altura de la capa de mezcla se define como la capa de la atmosfera (troposfera) que

está influenciada de manera directa con las condiciones de la superficie del suelo, y es

donde se da lugar la turbulencia mecánica y térmica (transferencia de calor y materia) de

los gases y partículas presentes en ella (contaminantes), proceso característico de la

troposfera baja. En términos generales, la altura de la capa de mezcla varía de unos

cuantos kilómetros en el día a unos cientos de metros en la noche.

El modelo WRF, es capaz de simular la altura de capa de mezcla, de hecho, tal como se

observa en la Figura 28, la evolución de la capa de mezcla diaria tiene un patrón

relativamente similar en todas las estaciones del año.

En el mismo contexto, el comportamiento de la capa de mezcla muestra un aumento de su

altura desde el horario de salida del sol (entre 06:00 a 08:00 am) teniendo su mayor valor

entre las 12:00 a las 15:00 horas, la cual tiene una altura de máxima cercana a los 2000

metros para el verano, cercana a los 1600 metros en primavera, a los 1100 metros en

otoño y a los 500 metros en invierno. Luego de este periodo del día, la altura de la capa

disminuye debido a la menor influencia de la radiación reflejada (albedo) de la superficie.

Por último, durante la noche y madrugada, la altura de capa de mezcla alcanza sus

menores valores, debido a una menor influencia del albedo. Este comportamiento es el

esperado, resaltando el hecho que, en verano y primavera, las alturas máximas de la capa

sean mayores que en invierno debido a la influencia de la radiación solar.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 51 de 106**

**Figura 28. Evolución diaria de la altura de capa de mezcla, WRF año 2021.**

Lo anterior se explica debido a que la capa de mezcla se hace más estable durante las

noches, debido a la ausencia de aporte energético del sol, influyendo negativamente en el

intercambio vertical, de este modo, la turbulenta térmica es prácticamente nula. Con la

salida del sol, el calentamiento de la superficie terrestre es transmitido a la atmosfera,

produciendo agitación en la capa de mezcla lo que provoca un incremento en el espesor

del volumen del aire afectado por el suelo, llegando al máximo entre las 12:00 y 15:00

horas del día, es en este momento del día en donde se propician las condiciones de

máxima inestabilidad atmosférica, favoreciendo la turbulencia térmica y la dispersión de

contaminantes.

Por ende, y a modo de conclusión, se puede mencionar que este parámetro es importante

para la concentración de un contaminante, ya que a medida que disminuye la altura de

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 52 de 106**

capa de mezcla, el contaminante tiende a concentrarse, y, por el contrario, a medida que

se aleja de la superficie, el contaminante tiene a dispersarse.

**6.1.5** **Caracterización de la precipitación**

La simulación meteorológica del modelo WRF presentada en la Figura 29, determinó que

para el año 2021 la precipitación en la zona de estudio alcanzó los 309 mm.

Es posible observar, además que los meses con la mayor precipitación simulada son

agosto y septiembre, los que en su conjunto representan el 73,14% de la precipitación

anual simulada. En efecto agosto es el mes donde se presenta la máxima precipitación con

156 mm, que representa más del 50% de la precipitación anual. Por su parte los meses

más cálidos, a excepción de enero, presentan escaso aporte a la precipitación anual en la

zona.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Figura 29. Precipitación Anual, WRF 2021.**

**Página 53 de 106**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**6.2** **Concentraciones Modeladas**

**Página 54 de 106**

A continuación, se presentan los resultados de la modelación de material particulado y

gases emitidos a la atmosfera. Cabe recordar que, el escenario modelado corresponde a

las emisiones de material particulado, tanto MP10 como MP2,5, y gases (NO 2, SO 2 y CO),

las cuales se producen en las fases de construcción y operación del proyecto durante el

año 1.

**6.2.1** **Dispersión e Isoconcentración Material Particulado Respirable, MP10**

A continuación, se presenta el análisis de los resultados para el MP10 tanto para la

concentración promedio anual y 24 horas.

Es importante señalar que la pluma de dispersión de MP10 simulada por el modelo abarca

la zona de emplazamiento del proyecto y alrededores, donde se construyen 120 viviendas

en paralelo con la entrada en operación de 264 unidades habitacionales durante el

segundo semestre de ese año.

**6.2.1.1** **Concentración Promedio 24 horas de MP10**

En la Figura 30, se muestra la pluma de dispersión de la concentración promedio diaria de

MP10, de donde se observa lo siguiente:

 Las concentraciones se distribuyen alrededor del proyecto, situando su máxima

concentración en la zona centro del proyecto, lugar donde se realiza gran parte del

tránsito en vías pavimentadas y no pavimentadas. Además, se observa una

concentración de las emisiones en la zona donde se ubica el polígono que se

construye durante el año 1, lugar de ejecución de las actividades de propias de la

fase de construcción como escarpe, compactación, excavación, entre otras. La

forma de la pluma demuestra que es en el mismo predio del proyecto donde se

genera la mayor parte de las emisiones, principalmente en la zona donde se ubican

las actividades ejecutadas en la fase de operación y fase de construcción. Las

actividades ejecutadas en la zona de mayor concentración corresponden a:

1. Calefacción domiciliaria de la situación basal.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

2. Transito interno por vías pavimentadas.

3. Transito externo por vías pavimentadas.

**Página 55 de 106**

4. Actividades de construcción como escarpe, excavación, compactación, carga y

descarga de material y uso de maquinaria.

 La pluma de dispersión tiene una forma relativamente circular con un ligero

pronunciamiento hacía el oeste y sur del proyecto.

 Las concentraciones modeladas van desde los 2,80 μg/m3 a los 6,00 μg/m3 en la

zona central del proyecto, donde se realiza tránsito en vías no pavimentadas junto

con otras actividades propias de la construcción como excavaciones, escarpe,

compactación, entre otros. El polígono de la situación basal donde se realizan

actividades de operación del proyecto como transito en vías pavimentadas y

calefacción domiciliaria presenta concentraciones similares a las del polígono de

construcción, las que de todas maneras pueden ser catalogadas como de baja

magnitud.

 En relación con los puntos receptores elegidos se observa que, 7 de los 18

evaluados se encuentran dentro de la pluma principal. Los receptores R4, R7 y R2

son los que presentan las concentraciones más altas, alcanzando los 2,73 μg/m3,

2,61 μg/m3 y 2,48 μg/m3 respectivamente. En tanto, que los receptores R13 y R18

se encuentran más alejados del proyecto, alcanzando concentraciones de MP10 de

0,55 μg/m3 y 0,03 μg/m3 respectivamente.

En la Figura 31, se muestra el mapa de Isoconcentración, de donde se puede concluir

que:

 La pluma se extiende hasta los 250 m por el norte y 350 m por el sur, 442 m al

oeste y 345 m al este desde la zona de máxima concentración, disminuyendo las

concentraciones simuladas en un 67% respecto al punto de máxima concentración.

 La zona de mayor concentración abarca una superficie de 0,629 ha y la

concentración sería cercana a los 5,2 μg/m3, ubicándose dentro de la zona de

emplazamiento del proyecto.

 El área total del mapa de Isoconcentración abarca una superficie de 36,292 ha.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 56 de 106**

**Figura 30. Dispersión de la pluma de MP10 como concentración de 24 horas**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 57 de 106**

**Figura 31. Isolíneas de concentración de MP10 como concentración de 24 horas.**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**6.2.1.2** **Concentración Promedio Anual de MP10**

**Página 58 de 106**

En la Figura 32, se muestra la pluma de dispersión de la concentración promedio anual de

MP10, de donde se concluye lo siguiente:

 La forma de la pluma de dispersión tiene similitud respecto a la obtenida en la

simulación de la concentración promedio diario, aunque con una extensión menor

y concentrándose en la zona de emplazamiento del proyecto, específicamente en la

zona de construcción.

 En la pluma de dispersión se observa un área de concentraciones menores en

magnitud, cuyo rango varía entre los 1,0 μg/m3 a los 3,1 μg/m3.

 Con base en los resultados obtenidos, ninguno de los receptores evaluados se

emplazada dentro de la pluma de influencia dado que estos presentan

concentraciones más bajas que 1,0 μg/m3.

En la Figura 33, se muestra el mapa de isoconcentración, de donde se puede concluir que:

 La pluma se extiende hasta los 107 m por el norte y 137 m al sur, 117 m al oeste y

134 m al este desde la zona de mayor concentración. A estas distancias la

concentración esperada es de 1,00 μg/m3.

 La pluma de dispersión se distribuye de forma similar a la pluma de dispersión de

MP10 como norma diaria ya que presenta una forma circular relativamente

uniforme con una extensión en dirección sureste desplazándose aproximadamente

en 215 m desde el centro del proyecto hacia el borde más largo de la pluma.

 Se distingue una zona de máxima concentración de 0,164 ha en donde las

concentraciones son cercanas a 2,68 μg/m3 dentro de la zona de emplazamiento

del proyecto.

 El área total del mapa de isoconcentración abarca una superficie de 5,431 ha.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 59 de 106**

**Figura 32. Dispersión de la pluma de MP10 como concentración promedio anual.**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 60 de 106**

**Figura 33. Isolíneas de concentración de MP10 como concentración promedio anual.**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 61 de 106**

**6.2.2** **Dispersión e Isoconcentración Material Particulado Fino Respirable,**

**MP2,5**

A continuación, se presenta el análisis de los resultados para el MP2,5, tanto para la

concentración promedio anual y 24 horas.

**6.2.2.1** **Concentración Promedio diaria MP2,5**

En la Figura 34, se muestra la pluma de dispersión de la concentración promedio diario de

MP2,5, de donde se concluye que:

 La pluma de dispersión al igual que lo ocurrido para MP10 presenta sus mayores

concentraciones en la zona central del proyecto, donde existe un gran tránsito

tanto por las actividades de la fase de construcción como la de operación junto con

las actividades propias de la construcción como excavación, compactación,

escarpe, entre otras. En contraste de lo que ocurre con la pluma de dispersión de

MP10 como norma diaria, la pluma de MP2,5 como norma diaria se distribuye

principalmente dentro del polígono del proyecto, cubriendo levemente algunas

viviendas contiguas al polígono ya mencionado.

 La concentración generada en la atmosfera de las emisiones de MP2,5 varía desde

los 1,0 μg/m3 a los 2,0 μg/m3.

 De los 18 puntos receptores modelados, ninguno se encuentra dentro de la pluma

de dispersión de MP2,5 como norma diaria.

En la Figura 35, se muestra el mapa de isoconcentración, de donde se puede concluir:

 La pluma se extiende hasta los 104 m por el norte y 185 m al sur, 156 m al oeste y

162 m al oeste desde la zona de mayor concentración. A estas distancias la

concentración esperada es de 1,0 μg/m3.

 En total la pluma abarca un área de aproximada de 7,768 ha.

 Las zonas de mayores concentraciones abarcan una superficie de 0,335 ha. Esta

superficie se ubica abarcando el área de circulación de vehículos en camino no

pavimentados y actividades de construcción, donde se alcanzan concentraciones

de 1,80 μg/m [3] .

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 62 de 106**

**Figura 34. Dispersión de la pluma de MP2,5** **como concentración promedio diaria.**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 63 de 106**

**Figura 35. Isolíneas de concentración de MP2,5 como concentración promedio diaria.**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**6.2.2.2** **Concentración promedio anual de MP2,5**

**Página 64 de 106**

En la Figura 36, se muestra la pluma de dispersión de la concentración promedio anual de

MP2,5, de donde se concluye que:

 El comportamiento del material particulado fino como concentración promedio

anual, concentra sus máximas concentraciones en la zona centro del proyecto,

pronunciándose en dirección sureste.

 La concentración generada en la atmósfera por las emisiones de MP2,5 varían

desde los 0,5 a los 1,0 μg/m3.

 Ninguno de los 18 puntos receptores modelados se encuentra dentro de la pluma

de MP2,5 como promedio anual.

En la Figura 37, se muestra el mapa de isoconcentración, de donde se puede concluir

que:

 La pluma se extiende hasta los 43 m por el norte y 123 m al sur, 81 m al oeste y

96 m al este desde la zona de mayor concentración. A estas distancias la

concentración esperada es de 0,50 μg/m3.

 El área donde se ubica la zona de mayor concentración evidencia una superficie

0,105 ha. Es en esta zona donde se encuentra el punto de mayor magnitud, con

una concentración equivalente a 0,9 μg/m3.

 El área total de la pluma de isoconcentración abarca una superficie de 3,087 ha.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 65 de 106**

**Figura 36. Dispersión de la pluma de MP2,5 como concentración promedio anual.**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 66 de 106**

**Figura 37. Isolíneas de concentración de MP2,5 como concentración promedio anual.**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**6.2.3** **Dispersión Dióxido de Nitrógeno, NO** **2**

**Página 67 de 106**

A continuación, se presenta el análisis de los resultados para el NO 2, tanto para la

concentración anual y horaria.

**6.2.3.1** **Concentración horaria NO** **2**

En la Figura 38, se muestra la pluma de dispersión de la concentración horaria de NO 2 de

donde se concluye que:

 La pluma de dispersión se centra en el proyecto y sus alrededores, donde se llevan

a cabo principalmente las actividades de construcción y transito interno en vías

pavimentadas y no pavimentadas, demostrando que su principal aporte

corresponde a la combustión de maquinaria, seguido de la combustión interna de

los vehículos tanto pesados como livianos.

 La concentración generada en la atmosfera de las emisiones de NO 2 varía desde

los 8,0 μg/m3N a los 15,3 μg/m3N.

 De los puntos receptores modelados, solo 1 de 18 se encuentra dentro de la pluma

de dispersión, siendo el receptor R4 el que presenta la concentración más alta con

9,44 μg/m3N.

 La pluma se extiende hasta los 165 m por el norte y 177 m al sur, 185 m al oeste y

167 m al oeste desde la zona de mayor concentración. A estas distancias la

concentración esperada es de 8,0 μg/m3N.

 En total la pluma abarca un área de aproximada de 9,452 ha.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 68 de 106**

**Figura 38. Dispersión de la pluma de NO** **2** **como concentración máxima horaria.**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 69 de 106**

**Figura 39. Isolíneas de concentración de NO** **2** **como concentración máxima horaria.**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**6.2.3.2** **Concentración anual NO** **2**

**Página 70 de 106**

En la Figura 40, se muestra la pluma de dispersión de la concentración anual de NO 2, de

donde se concluye que:

 La pluma de dispersión se distribuye por casi toda el área de construcción del

proyecto, presentando las mayores concentraciones en el área donde se realizan

las actividades propias de la fase constructiva.

 - La concentración de emisiones generadas de NO 2 en un año, varía desde los 1,0 a

los 2,1 μg/m3N.

 De los puntos receptores modelados, ninguno de los 18 se encuentra dentro de la

pluma de dispersión, siendo el receptor R4 el más cercano, con una concentración

de 0,696 μg/m3.

 La pluma se extiende hasta los 42 m por el norte y 158 m al sur, 85 m al oeste y

100 m al este desde la zona de mayor concentración. A estas distancias la

concentración esperada es de 1,0 μg/m3.

 Las zonas de mayores concentraciones abarcan una superficie de 0,119 ha donde

la concentración sería superior a los 1,88 μg/m3 ubicándose en el centro del

proyecto.

 En total la pluma abarca un área de aproximada de 4,050 ha.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 71 de 106**

**Figura 40. Dispersión de la pluma de NO** **2** **como concentración anual.**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 72 de 106**

**Figura 41. Isolíneas de concentración de NO** **2** **como promedio anual.**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**6.2.4** **Dispersión Dióxido de Azufre (SO** **2** **)**

**Página 73 de 106**

A continuación, se presenta el análisis de los resultados para el SO2, tanto para la

concentración anual, diaria y horaria.

**6.2.4.1** **Concentración horaria SO** **2**

En la Figura 42 se muestra la pluma de dispersión de la concentración horaria de SO 2, de

donde se concluye lo siguiente:

 La forma de la pluma de dispersión es relativamente circular pronunciándose en

direcciones oeste y sur.

 En la pluma de dispersión se observa un área de mayores concentraciones donde

se realizan propias de la operación de la situación basal dado que la calefacción

domiciliaria es el principal aportante de este contaminante, presentando un rango

de concentraciones que varían entre los 9,0 μg/m3N a 17,5 μg/m3N.

 Con base en los resultados obtenidos, 4 de los 18 receptores se encuentran

inmersos dentro de la pluma de dispersión, siendo el R4 el que posee la mayor

concentración con 10,827 μg/m3N.

En la Figura 43, se muestra el mapa de isoconcentración, de donde se puede concluir que:

 La pluma se extiende hasta los 262 m por el norte y 222 m al sur, 319 m al oeste y

216 m al este desde la zona de mayor concentración. A estas distancias la

concentración esperada es de 9,0 μg/m3N.

 La pluma de dispersión se distribuye de manera relativamente uniforme con una

extensión en las direcciones oeste y suroeste.

 Se distingue una zona de máxima concentración de 0,057 ha en donde las

concentraciones son cercanas a los 15,8 μg/m3N.

 El área total del mapa de isoconcentración abarca una superficie de 20,172 ha

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 74 de 106**

**Figura 42. Dispersión de la pluma de SO** **2** **como concentración horaria**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 75 de 106**

**Figura 43. Isolíneas de concentración de SO** **2** **como concentración horaria**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**6.2.4.2** **Concentración 24 horas SO** **2**

**Página 76 de 106**

En la Figura 44, se muestra la pluma de dispersión de la concentración 24 horas de SO 2,

de donde se concluye que:

 La pluma de dispersión presenta sus mayores concentraciones al interior del

polígono del proyecto, específicamente en la zona de operación de la situación

basal donde se encuentran las viviendas ya entregadas.

 - La concentración generada en la atmosfera de las emisiones de SO 2 como norma

diaria varía desde los 3,5 a los 7,1 μg/m3N.

 De los puntos receptores modelados, solo 2 de los 18 se encuentran dentro de la

pluma de dispersión, siendo el receptor R4 el cual alcanza la mayor concentración,

la que equivalente a 3,869 μg/m3N.

En la Figura 45, se muestra el mapa de isoconcentración, de donde se puede concluir:

 La pluma se extiende hasta los 141 m por el norte y 108 m al sur, 172 m al oeste y

107 m al este desde la zona de mayor concentración. A estas distancias la

concentración esperada es de 3,5 μg/m3N.

 En total la pluma abarca un área de aproximada de 5,737 ha.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 77 de 106**

**Figura 44. Dispersión de la pluma de SO** **2** **como concentración 24 horas**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 78 de 106**

**Figura 45. Isolíneas de concentración de SO** **2** **como concentración 24 horas**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**6.2.4.3** **Concentración Anual SO** **2**

**Página 79 de 106**

En la Figura 46, se muestra la pluma de dispersión de la concentración anual de SO 2, de

donde se concluye que:

 El comportamiento del dióxido de azufre como concentración promedio anual,

concentra sus máximas concentraciones en la zona de operación del proyecto y

área externa contigua a este polígono, al igual que el comportamiento del dióxido

de azufre en concentración diaria. Esta distribución se debe a que la calefacción

domiciliaria con kerosene que se presenta en la operación de la situación basal es

la principal aportante de SO 2 del proyecto.

 - La concentración generada en la atmósfera por las emisiones de SO 2 como norma

anual varían desde los 0,80 a los 1,75 μg/m3N.

 De los 18 puntos receptores modelados, solo dos se encuentra dentro de la pluma

de dispersión del contaminante, siendo el receptor R4 el que presenta las

concentraciones más altas con 1,129 μg/m3N.

En la Figura 47, se muestra el mapa de isoconcentración, de donde se puede concluir

que:

 En relación con la dimensión, la pluma se extiende hasta los 128 m por el norte y

105 m por el sur, 114 m al oeste y 114 m al este desde la zona de mayor

concentración. A estas distancias la concentración esperada es de 0,8 μg/m3N.

 El área donde se ubica la zona de mayor concentración evidencia una superficie

0,20 ha. Es en esta zona donde se encuentra el punto de mayor magnitud, con

una concentración equivalente a 0,05 μg/m3N.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 80 de 106**

**Figura 46. Dispersión de la pluma de SO** **2** **como concentración anual**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 81 de 106**

**Figura 47. Isolíneas de concentración de SO** **2** **como concentración anual**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**6.2.5** **Dispersión Monóxido de Carbono (CO)**

**Página 82 de 106**

A continuación, se presenta el análisis de los resultados para el CO, tanto para la

concentración en 8 horas y horaria.

**6.2.5.1** **Concentración horaria CO**

En la Figura 48, se muestra la pluma de dispersión de la concentración horaria de CO, de

donde se concluye lo siguiente:

 La forma de la pluma de dispersión es relativamente circular con una forma

irregular.

 En la pluma de dispersión se observa un área de mayores concentraciones donde

se realizan las actividades de tránsito en caminos no pavimentados interno junto

con las actividades de construcción del proyecto.

 Las concentraciones simuladas fluctúan entre los 0,007 mg/m [3] N a los 0,0122

mg/m [3] N.

 Con base en los resultados obtenidos, solo 1 de los 18 receptores se encuentran

inmersos dentro de la pluma de dispersión, siendo el R4 el que posee la mayor

concentración con 0,0075 mg/m3N.

En la Figura 48, se muestra el mapa de isoconcentración, de donde se puede concluir que:

 La pluma se extiende hasta los 169 m por el norte y 144 m al sur, 167 m al oeste y

156 m al este desde la zona de mayor concentración. A estas distancias la

concentración esperada es de 0,007 mg/m3N.

 La pluma de dispersión se distribuye de manera relativamente uniforme en todas

las direcciones de la rosa de los vientos, desplazándose aproximadamente 152 m

desde el centro del proyecto hacia el borde más largo de la pluma.

 Se distingue una zona de máxima concentración de 0,192 ha en donde las

concentraciones cercanas a los 0,0122 mg/m [3] N.

 El área total del mapa de isoconcentración abarca una superficie de 7,376 ha.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 83 de 106**

**Figura 48. Dispersión de la pluma de CO como concentración horaria**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 84 de 106**

**Figura 49. Isolíneas de concentración de CO como concentración horaria**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**6.2.5.2** **Concentración 8 horas CO**

**Página 85 de 106**

En la Figura 50, se muestra la pluma de dispersión de la concentración 8 horas para CO,

de donde se concluye que:

 En la pluma de dispersión se observa un área de mayores concentraciones donde

se realizan las actividades de tránsito en caminos no pavimentados junto con la

zona que se construye el año 1.

 La concentración generada en la atmosfera de las emisiones de CO varía desde los

0,0045 a los 0,0075 mg/m3N.

 De los 18 puntos receptores modelados, ninguno se encuentra dentro de la pluma

de dispersión de CO como norma de 8 horas.

En la Figura 51, se muestra el mapa de isoconcentración, de donde se puede concluir:

 La pluma se extiende hasta los 87 m por el norte y 125 m al sur, 150 m al oeste y

116 m al este desde la zona de mayor concentración. A estas distancias la

concentración esperada es de 0,0045 mg/m3N.

 En total la pluma abarca un área de aproximada de 4,743 ha.

 Las zonas de mayores concentraciones abarcan una superficie de 0,253 ha donde

se alcanzan concentraciones similares a 0,0065 mg/m [3] N.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 86 de 106**

**Figura 50. Dispersión de la pluma de CO como concentración 8 horas**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 87 de 106**

**Figura 51. Isolíneas de concentración de CO como concentración 8 horas**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**6.2.6** **Modelación discreta de las emisiones contaminantes**

**Página 88 de 106**

La modelación discreta de emisiones fue realizada para MP10, MP2,5, NO 2, SO 2, CO, cuyos

valores de concentración para los puntos receptores son presentados en las siguientes

tablas. Tal como se ha mencionado, estos puntos corresponden a viviendas y lugares de

encuentro de la población cercana al proyecto y a los principales caminos externos por los

cuales se transitará durante el desarrollo del proyecto.

**6.2.6.1** **Material Particulado Grueso y Fino**

De los resultados discretos obtenidos para estos contaminantes se destaca:

 Todas las concentraciones modeladas en los 18 receptores discretos son de baja

magnitud.

 - Respecto al MP10, las concentraciones en los receptores van entre 0,003 ug/m [3] -

0,489 ug/m [3] y 0,025 ug/m [3] - 2,734 ug/m [3] para la norma anual y diaria

respectivamente, alcanzando 0,98% y 2,10% de los límites normativos respectivos.

 Respecto al material particulado fino, las concentraciones en los receptores van

entre 0,001 ug/m [3] - 0,171 ug/m [3] y 0,008 - 0,941 ug/m [3] para la norma anual y

diaria respectivamente, alcanzando 0,86% y 1,88% de los límites normativos

respectivos.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 89 de 106**

**Tabla 17. Concentración modelada en puntos receptores con respecto a MP10** **y**

**MP2,5.**

|Punto|Concentración MP10 (μg/m3)|Col3|Col4|Col5|Concentración MP2,5 (μg/m3)|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Punto**|**Anual**|**%respecto**<br>**a la norma**|**Diario**|**%respecto**<br>**a la norma**|**Anual**|**%respecto**<br>**a la norma**|**Diario**|**%respecto**<br>**a la norma**|
|**R1**|**0,405**|**0,81%**|**2,451**|**1,89%**|**0,133**|**0,67%**|**0,821**|**1,64%**|
|**R2**|**0,419**|**0,84%**|**2,475**|**1,90%**|**0,141**|**0,71%**|**0,832**|**1,66%**|
|R3|0,269|0,54%|2,050|1,58%|0,091|0,46%|0,692|1,38%|
|**R4**|**0,489**|**0,98%**|**2,734**|**2,10%**|**0,171**|**0,86%**|**0,941**|**1,88%**|
|**R5**|**0,331**|**0,66%**|**2,423**|**1,86%**|**0,118**|**0,59%**|**0,823**|**1,65%**|
|R6|0,270|0,54%|2,453|1,89%|0,092|0,46%|0,824|1,65%|
|**R7**|**0,240**|**0,48%**|**2,606**|**2,00%**|**0,082**|**0,41%**|**0,872**|**1,74%**|
|R8|0,228|0,46%|2,223|1,71%|0,077|0,39%|0,752|1,50%|
|R9|0,205|0,41%|1,721|1,32%|0,069|0,35%|0,579|1,16%|
|R10|0,319|0,64%|1,871|1,44%|0,106|0,53%|0,631|1,26%|
|R11|0,148|0,30%|1,333|1,03%|0,050|0,25%|0,454|0,91%|
|R12|0,102|0,20%|1,030|0,79%|0,035|0,18%|0,351|0,70%|
|R13|0,056|0,11%|0,552|0,42%|0,019|0,10%|0,189|0,38%|
|R14|0,148|0,30%|1,417|1,09%|0,051|0,26%|0,483|0,97%|
|R15|0,106|0,21%|1,000|0,77%|0,037|0,19%|0,343|0,69%|
|R16|0,082|0,16%|0,863|0,66%|0,028|0,14%|0,292|0,58%|
|R17|0,074|0,15%|0,708|0,54%|0,025|0,13%|0,237|0,47%|
|R18|0,003|0,01%|0,025|0,02%|0,001|0,01%|0,008|0,02%|

*los receptores marcados en negrita corresponden a los que presentan las mayores

concentraciones

**6.2.6.2** **Dióxido de azufre (SO** **2** **)**

De los resultados discretos obtenidos para este contaminante se destaca:

 Todas las concentraciones modeladas en los 18 receptores discretos son de baja

magnitud.

 - Respecto al SO 2 como norma horaria, las concentraciones en los receptores van

entre 0,034 - 10,827 ug/m [3] N, alcanzando un 3,09% del límite normativo

respectivo.

 - En tanto, las concentraciones de SO 2 como norma diaria en los receptores van

entre 0,016 - 3,869 ug/m [3] N, alcanzando un 2,58% del límite normativo.

 - Por último, las concentraciones de SO 2 como promedio anual en los receptores van

entre 0,001 - 1,129 ug/m [3] N alcanzando un 1,88% del valor normativo.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 90 de 106**

**Tabla 18. Concentración modelada en puntos receptores con respecto a SO** **2** **.**

|Punto|Concentración SO (μg/m3N)<br>2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**Punto**|**Horario**|**%respecto**<br>**a la norma**|**Diario**|**%respecto**<br>**a la norma**|**Anual**|**%respecto**<br>**a la norma**|
|**R1**|**8,345**|**2,38%**|**2,183**|**1,46%**|**0,247**|**0,41%**|
|R2|8,044|2,30%|2,192|1,46%|0,235|0,39%|
|R3|8,413|2,40%|2,048|1,37%|0,225|0,38%|
|**R4**|**10,827**|**3,09%**|**3,869**|**2,58%**|**1,129**|**1,88%**|
|**R5**|**10,628**|**3,04%**|**3,675**|**2,45%**|**0,800**|**1,33%**|
|**R6**|**10,066**|**2,88%**|**3,351**|**2,23%**|**0,298**|**0,50%**|
|**R7**|**9,374**|**2,68%**|**2,608**|**1,74%**|**0,241**|**0,40%**|
|R8|7,673|2,19%|2,198|1,47%|0,198|0,33%|
|R9|5,730|1,64%|1,495|1,00%|0,151|0,25%|
|R10|5,814|1,66%|1,447|0,96%|0,171|0,29%|
|R11|3,947|1,13%|1,223|0,82%|0,097|0,16%|
|R12|3,803|1,09%|0,967|0,64%|0,090|0,15%|
|R13|2,645|0,76%|0,625|0,42%|0,063|0,11%|
|R14|7,246|2,07%|1,947|1,30%|0,176|0,29%|
|R15|4,984|1,42%|1,639|1,09%|0,137|0,23%|
|R16|3,236|0,92%|1,027|0,68%|0,086|0,14%|
|R17|1,832|0,52%|0,509|0,34%|0,049|0,08%|
|R18|0,034|0,01%|0,016|0,01%|0,001|0,00%|

*los receptores marcados en negrita corresponden a los que presentan las mayores

concentraciones

**6.2.6.3** **Dióxido de Nitrógeno (NO** **2** **)**

De los resultados discretos obtenidos para este contaminante se destaca:

 Todas las concentraciones modeladas en los 18 receptores discretos son de baja

magnitud.

 - Respecto al NO 2 como norma horaria, las concentraciones en los receptores van

entre 0,024 ug/m [3] N - 9,442 ug/m [3] N, alcanzando un 2,36% del límite normativo

respectivo.

 - En tanto, las concentraciones de NO 2 como norma anual en los receptores van

entre 0,001 ug/m [3] N - 0,696 ug/m [3] N, alcanzando un 0,70% del límite normativos

respectivo.

**Tabla 19. Concentración modelada en puntos receptores con respecto a NO** **2**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 91 de 106**

|Punto|Concentración NO (μg/m3N)<br>2|Col3|Col4|Col5|
|---|---|---|---|---|
|**Punto**|**Horario**|**%respecto a la**<br>**norma**|**Anual**|**%respecto a la**<br>**norma**|
|**R1**|**7,089**|**1,77%**|**0,311**|**0,31%**|
|R2|5,391|1,35%|0,302|0,30%|
|R3|4,912|1,23%|0,213|0,21%|
|**R4**|**9,442**|**2,36%**|**0,696**|**0,70%**|
|**R5**|**6,867**|**1,72%**|**0,484**|**0,48%**|
|**R6**|**6,297**|**1,57%**|**0,270**|**0,27%**|
|**R7**|**6,888**|**1,72%**|**0,225**|**0,23%**|
|R8|5,767|1,44%|0,188|0,19%|
|R9|4,137|1,03%|0,156|0,16%|
|R10|3,978|0,99%|0,225|0,23%|
|R11|2,225|0,56%|0,098|0,10%|
|R12|2,128|0,53%|0,075|0,08%|
|R13|1,393|0,35%|0,045|0,05%|
|R14|3,740|0,94%|0,135|0,14%|
|R15|3,120|0,78%|0,102|0,10%|
|R16|2,464|0,62%|0,077|0,08%|
|R17|1,443|0,36%|0,051|0,05%|
|R18|0,024|0,01%|0,001|0,00%|

*los receptores marcados en negrita corresponden a los que presentan las mayores

concentraciones

**6.2.6.4** **Monóxido de Carbono (CO)**

De los resultados discretos obtenidos para este contaminante se destaca:

 Todas las concentraciones modeladas en los 18 receptores discretos son de muy

baja magnitud.

 Respecto al CO como norma horaria, las concentraciones en los receptores van

entre 0,0000 - 0,0075 mg/m [3], alcanzando un 0,03% del límite normativo

respectivo.

 En tanto, las concentraciones de CO como promedio móvil de 8 horas en los

receptores van entre 0,0000 - 0,0041 mg/m [3], alcanzando un 0,04% del límite

normativos respectivo.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 92 de 106**

**Tabla 20. Concentración modelada en puntos receptores con respecto a CO**

|Punto|Concentración CO (mg/m3N)|Col3|Col4|Col5|
|---|---|---|---|---|
|**Punto**|**Horario**|**%respecto a la**<br>**norma**|**8 horas**|**%respecto a la**<br>**norma**|
|**R1**|**0,0060**|**0,020%**|**0,0033**|**0,033%**|
|R2|0,0041|0,014%|0,0029|0,029%|
|R3|0,0035|0,012%|0,0030|0,030%|
|**R4**|**0,0075**|**0,025%**|**0,0041**|**0,041%**|
|**R5**|**0,0051**|**0,017%**|**0,0037**|**0,037%**|
|**R6**|**0,0043**|**0,014%**|**0,0035**|**0,035%**|
|R7|0,0034|0,011%|0,0032|0,032%|
|**R8**|**0,0041**|**0,014%**|**0,0030**|**0,030%**|
|R9|0,0032|0,011%|0,0025|0,025%|
|R10|0,0029|0,010%|0,0025|0,025%|
|R11|0,0009|0,003%|0,0017|0,017%|
|R12|0,0009|0,003%|0,0014|0,014%|
|R13|0,0007|0,002%|0,0008|0,008%|
|R14|0,0015|0,005%|0,0021|0,021%|
|R15|0,0014|0,005%|0,0014|0,014%|
|R16|0,0011|0,004%|0,0012|0,012%|
|R17|0,0009|0,003%|0,0009|0,009%|
|R18|0,0000|0,000%|0,0000|0,000%|

*los receptores marcados en negrita corresponden a los que presentan las mayores

concentraciones

De esta manera, se concluye que las concentraciones de los cinco contaminantes

modelados en los 18 receptores discretos **son de baja magnitud, lo que significa que**

**la ejecución proyecto en evaluación no tiene impactos significativos sobre la**

**calidad del aire de los receptores evaluados.**

**6.2.7** **Aporte a la estación de Monitoreo de Representatividad Poblacional**

**(EMRP)**

A continuación, se presentan los resultados de la concentración de MP10 y MP2,5

simuladas en la EMRP Rancagua I y la proyección con el año de mayor emisión del

proyecto.

En la Tabla 21, se observa el aumento de la concentración basal registrada en la EMRP

entre enero y diciembre de 2021 para MP10, MP2,5, SO 2 y CO.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 93 de 106**

Los resultados evidencian un aumento de la condición basal menor al 0,13% para la

concentración de MP10 y MP2,5. En el caso del SO 2 el máximo aumento respecto a la

condición basal es de un 14,29% y en el CO es solamente de un 0,01%.

**Tabla 21. Aumento de la concentración basal en la EMRP Rancagua I, año 2021**

|Contaminante|Col2|Registro EMRP|Modelado<br>(ug/m3)|Proyectado<br>(ug/m3)|Porcentaje<br>de aumento|
|---|---|---|---|---|---|
|**Contaminante**|**Contaminante**|**(ug/m3) **|**(ug/m3) **|**(ug/m3) **|**(ug/m3) **|
|MP10|Anual|51,15|0,025|51,18|**0,05%**|
|MP10|24 horas|129,22|0,173|129,39|**0,13%**|
|MP2,5|Anual|26,03|0,009|26,04|**0,03%**|
|MP2,5|24 horas|91,71|0,060|91,77|**0,07%**|
|SO2|Anual|2,61|0,015|2,625|**0,57%**|
|SO2|24 horas|3,39|0,153|3,543|**4,51%**|
|SO2|1 hora|3,66|0,373|4,033|**10,19%**|
|CO|8 horas|4,78|0,0003|4,780|**0,01%**|
|CO|1 hora|3,44|0,0002|3,440|**0,01%**|

De los cuatro contaminantes de los cuales se tiene información disponible en la EMRP

Rancagua I, tres presentaron aumentos en su concentración basal menor al 0,2%. En

cambio, el SO 2 emitido en el proyecto presenta un aumento en la concentración basal de

0,57%, 4,51% y 10,19% de SO 2 como norma anual, de 24 horas y horaria

respectivamente. Se observa que es un porcentaje de aumento considerable respecto a la

situación basal, esto se da principalmente debido a que las concentraciones basales de

SO 2 **medidas en la estación son muy bajas** . Esto se observa ya que las

concentraciones basales de SO 2 como norma anual, diaria y horaria representan un

4,35%, 2,26% y 1,05% de sus respectivos límites normativos, tal como se observa en la

siguiente tabla

**Tabla 22. Concentraciones basales de SO** **2** **y aporte del proyecto**

|Contaminante|Col2|Registro EMRP|Límite normativo|Porcentaje<br>respecto a<br>la norma|Proyectado|Porcentaje<br>respecto a<br>la norma|
|---|---|---|---|---|---|---|
|**Contaminante**|**Contaminante**|**(ug/m3N)**|**(ug/m3N)**|**(ug/m3N)**|**(ug/m3N)**|**(ug/m3N)**|
|SO2|Anual|2,61|60|4,35%|2,63|**4,38%**|
|SO2|24 horas|3,39|150|2,26%|3,54|**2,36%**|
|SO2|1 hora|3,66|350|1,05%|4,03|**1,15%**|

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 94 de 106**

Estas bajas concentraciones basales causan que pequeños aportes como los del proyecto

(no mayores a 0,4 ug/m [3] N) representen porcentajes importantes en el aumento de las

concentraciones basales. Sin embargo, se observa que, a pesar de estos aumentos

importantes, las concentraciones de SO 2 siguen estando muy por bajo los límites

normativos, lo que no representaría un riesgo a la población. Esto queda en evidencia

cuando se comparan las concentraciones proyectadas respecto a los límites normativos,

alcanzando menos del 5% del límite normado y presentando un aumento no mayor al

0,1% respecto a la situación sin proyecto.

Por lo cual, teniendo en cuenta que esta estación representa zonas urbanas pobladas de la

ciudad y es la estación más próxima al proyecto, resulta importante destacar que se prevé

un **aumento no significativo para tres de los cuatro contaminantes medidos en**

**la condición basal registrada en esta estación. En el caso del SO** **2** **, las**

**concentraciones proyectadas se encuentran muy por bajo del límite normativo,**

**lo que no representa un empeoramiento sustancial de la calidad del aire.**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

## 7 Análisis de incertidumbre

**Página 95 de 106**

Tal como se plantea en la “Guía para el Uso de Modelos de Calidad del Aire en el SEIA”

(2012) de manera textual “cualquier modelo (meteorológico o de calidad del aire)

representa una aproximación a la realidad y, en consecuencia, sus resultados tienen

incertidumbres asociadas” [3] . Ante lo cual, para cuantificar esta incertidumbre, se realiza un

análisis entre los valores entregados por el modelo WRF (valores meteorológicos) y

valores observados, en este caso los datos son extraídos de la Estación Aeródromo La

Indepedencia, propiedad de la Red Agrometeorológica del Instituto de Investigaciones

Agropecuarias (INIA); estación meteorológica más cercana al proyecto y con datos

disponibles para el año 2021, mismo año de simulación del modelo WRF.

El modelo WRF simuló las condiciones meteorológicas dentro de un rango de 57 x 57

celdas de una dimensión de 1 x 1 km. Para efectos del análisis del ajuste de los datos

meteorológicos simulados se seleccionó una celda en donde se ubica la estación

Aeródromo La Independencia, desde la cual se extrajeron los datos y se compararon con

los valores observados de la estación meteorológica antes mencionada.

La correlación de los datos se determinó a través del ajuste por mínimos cuadrados,

método en el que existen dos parámetros de importancia: coeficiente de correlación lineal

de Pearson (r) y el coeficiente de determinación (R [2] ).

El coeficiente de correlación lineal es una medida de relación de Pearson entre dos

variables y se usa para medir el grado de relación entre ellas. El rango de valores va

desde el -1 al 1 y está representado por la siguiente ecuación.

σ xy
r =
xy
σ x ∙σ y

Donde,

 - σ xy, es la covarianza entre x e y;

 - σ x, es la desviación estándar de x;

3 Texto extraído del primer párrafo de la página 38, acápite 7 de la Guía para el Uso de Modelos de
Calidad del Aire en el SEIA (2012)

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

- σ y, es la desviación estándar de y;

**Página 96 de 106**

El coeficiente de determinación se utiliza como medida de eficiencia de la cobertura de

datos midiendo el porcentaje de variación entre las variables observadas y modeladas, es

decir, testea la capacidad predictiva del modelo e indica la proporción de la varianza de los

resultados que puede ser explicado por el modelo. Los valores del coeficiente de

determinación varían de 0 a 1, siendo este último el valor óptimo y está determinada por

la siguiente relación.

R [2] = r 2
xy
= (

σ xy

σ x ∙σ y

2

~~)~~

Donde,

 - σ xy, es la covarianza entre x e y;

 - σ x, es la desviación estándar de x;

 - σ y, es la desviación estándar de y;

Además, se presenta el análisis de tendencia de los valores modelados a estar

sobredimensionados o subdimensionados respecto de los observados, a través del percent

bias (PBIAS), el valor óptimo es 1 y su cálculo se realiza según la siguiente ecuación.

PBIAS=

~~[~~

∑ ni=1 (S i −O i )

∑ ni=1 O i

~~]~~

Donde,

 - S i, es el valor simulado;

 - O i, es el valor observado.

Los resultados del ajuste del modelo meteorológico se presentan en la siguiente tabla.

Luego de ésta, se presenta el detalle de los valores entregados.

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 97 de 106**

**Tabla 23. Estadísticos de variables meteorológicas modeladas.**

|Variable|Coeficiente de<br>correlación lineal<br>(r)|Coeficiente de<br>determinación (R2)|Percent bias<br>(PBIAS)|
|---|---|---|---|
|Temperatura horaria|0,89|0,79|-0,15|
|Velocidad del viento horaria|0,47|0,22|0,90|
|Componente zonal del viento|0,1|0,01|-|
|Componente meridional del<br>viento|0,49|0,24|-|

**7.1** **Temperatura**

En la Figura 52 se observa la correlación entre la temperatura horaria observada desde la

estación Aeródromo - La independencia respecto a la modelada por el modelo WRF del

año 2021.

**Figura 52. Correlación entre temperaturas observadas y modeladas.**

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 98 de 106**

Respecto a la figura anterior se observa que la correlación entre la temperatura horaria

observada en la estación Palermo y la temperatura horaria modelada por el modelo WRF

en el año 2021, es directa y positiva con un coeficiente de correlación lineal de 0,89. Por

otro lado, el coeficiente de determinación sugiere que el modelo es capaz de simular el

79% de las temperaturas horarias observadas de forma óptima.

En la Figura 53, se observa la frecuencia de las temperaturas horarias en rangos de clases

tanto para los datos observados como modelados. A partir del grafico se desprende que, si

bien el modelo es capaz de reproducir de buena manera la variabilidad temporal de la

temperatura, su calidad disminuye frente a valores extremos. Es visible además que el

modelo sobreestima las temperaturas en el rango 0 - 10°C, mientras que subestima las

temperaturas entre los 10 - 30°C. Con todo esto, el valor del percent bias concluye, que

en general, los datos modelados se encuentran un 15% subestimados en relación con los

observados.

**Figura 53. Frecuencia de temperaturas observadas y modeladas.**

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**7.2** **Velocidad del viento**

**Página 99 de 106**

En la Figura 54 se observa la correlación entre la velocidad del viento horaria observada

desde la estación Aeródromo - La independencia, respecto a la modelada por el modelo

WRF del año 2021.

**Figura 54. Correlación entre velocidad del viento observada y modeladas.**

Respecto a la figura anterior se observa que la correlación entre la velocidad del viento

horaria observada y la modelada por el modelo WRF en el año 2021, es positiva con un

coeficiente de correlación lineal correspondiente a 0,47. Por otro lado, el coeficiente de

determinación sugiere que el modelo es capaz de simular el 22% de las velocidades del

viento horarias de forma óptima en la estación, en consecuencia, el modelo no se ajusta

fielmente a los datos observados.

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 100 de**

**106**

En la Figura 55 se observa la frecuencia de la velocidad del viento horaria en rangos de

clases tanto para los datos observados como modelados. En efecto, el modelo claramente

sobreestima los valores de velocidad del viento sobre los 2.1 m/s y subestima la

frecuencia de vientos de menor intensidad, siendo particularmente notorio entre los 0,0 y

0,5 m/s. Esto demuestra de acuerdo con los datos observados que en el área de estudio

existe una fuerte influencia de vientos de baja intensidad. Esto es relevante para la

determinación del área de influencia, pues al distribuir en otras categorías de viento

mayores, el área es mayor, por lo tanto, la evaluación es conservadora.

**Figura 55. Frecuencia de velocidad del viento observadas y modeladas.**

**7.3** **Dirección del viento**

Debido a que la dirección del viento es una variable circular, el coeficiente de Pearson no

nos da una buena representación para determinar cómo se comporta el modelo con

respecto a las observaciones.

Como la velocidad es una magnitud vectorial, es decir, que tiene módulo (su valor

expresado por ejemplo en m/s, o en km/h), dirección y sentido. El vector velocidad

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 101 de**

**106**

horizontal del viento podemos dividirlo en dos componentes, denominadas componente

zonal (u) y componente meridional del viento(v).

Las componentes del viento se calculan de la siguiente forma:

u= |V| ∗cos(φ)

v= |V| ∗sin(φ)

Donde:

|V|, es la magnitud del viento. φ, es la dirección del viento (angulo medido desde el
norte).

**7.3.1** **Componente zonal del viento**

La componente zonal, a la que se denomina u, es la componente de la velocidad

horizontal a lo largo de un círculo de latitud, en dirección Oeste a Este. Es decir, u es

positiva cuando apunta hacia el Este, que sería el sentido positivo de nuestro eje x si

dibujamos en un sistema de coordenadas cartesianas.

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 102 de**

**106**

**Figura 56. Frecuencia de velocidad del viento observadas y modeladas.**

En la Figura 56 podemos observar cómo se relacionan la componente zonal observada con

la modelada. En concreto, se obtuvo que la correlación entre ambas fue de un 0,10 lo que

implica que el modelo es capaz de representar un 1% del comportamiento observado.

**7.3.2** **Componente meridional del viento**

La componente meridional, a la que se denomina v, es la componente de la velocidad

horizontal a lo largo de un meridiano, de Sur a Norte. Es decir, que en nuestro sistema de

coordenadas cartesianas sería la proyección en el eje y, positivo hacia arriba.

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 103 de**

**106**

**Figura 57. Correlación componente meridional del viento.**

En la Figura 57 podemos observar cómo se relacionan la componente meridional

observada con la modelada. En concreto, se obtuvo que la correlación entre ambas fue de

un 0,49, lo que implica que el modelo es capaz de representar un 24% del

comportamiento observado.

**7.4** **Test de Bondad de Ajuste sobre el Modelo Meteorológico**

Se prescindirá de la aplicación de test de bondad de ajuste entre los datos modelados y

los observados, debido a que los datos modelados no provienen de una muestra sobre la

cual se ha supuesto una distribución de probabilidad específica, como, por ejemplo: log

normal, binomial, Bernoulli, etc., sino que son el resultado de la simulación a través de la

implementación de un modelo matemático.

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 104 de**

**106**

## 8 Conclusión

Se estudió la concentración de las emisiones producto de la construcción y operación,

proyectadas para el año 1 del proyecto **“Proyecto Habitacional La Gamboina”** ubicado

en la comuna de Rancagua, región del Libertador Bernardo O’Higgins. De esta forma,

fueron modeladas las emisiones MP10, MP2,5, NO 2, SO 2 y CO a fin de determinar las

concentraciones que éstos tendrán en la atmósfera, además de prever posibles efectos a

la salud de las personas.

Tal como se abordó anteriormente en el informe, el desplazamiento de los contaminantes

ocurre mayoritariamente al interior de la zona de emplazamiento del proyecto y en las

proximidades del proyecto. Al respecto se destaca que:

 Las plumas de material particulado MP10 Y MP2,5 poseen su mayor concentración

en el centro del proyecto, donde se encuentra el polígono de construcción del

proyecto durante el año 1. También presenta una concentración importante de las

emisiones en la zona de operación de la situación basal, donde se realizan las

actividades de tránsito por caminos pavimentados y emisiones por calefacción

domiciliaria en las temporadas de otoño e invierno.

 En cuanto a los gases modelados, el dióxido de nitrógeno y el monóxido de

carbono al igual que el material particulado, presentan sus máximas

concentraciones dentro del mismo polígono de construcción. Por otra parte, las

plumas de emisión del dióxido de azufre se centran en el área de operación de la

primera subfase donde se llevan a cabo las actividades de calefacción domiciliaria y

tránsito en vías pavimentadas, siendo la calefacción la principal actividad emisora

de este contaminante.

 De los 18 receptores discretos evaluados, 8 se encuentran dentro de las plumas de

dispersión generadas, siendo el R4 el que se encuentra expuesto a las mayores

concentraciones de los distintos contaminantes dado que este se ubica en la

situación basal del proyecto. De todas maneras, las concentraciones no

representan un peligro para la salud del receptor. Adicionalmente, se espera que

estas concentraciones disminuyan cuando el proyecto entre en plena operación

dada la menor emisión de MP.

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 105 de**

**106**

El análisis de la variación de la concentración demuestra que la ejecución del **proyecto**

**no representa una perturbación respecto a las concentraciones que**

**actualmente se registran en la estación de monitoreo analizada para tres de los**

**cuatro contaminantes analizados para los cuales hay información de línea de**

**base (MP10, MP2,5 y CO).** En el caso del SO 2, en el escenario modelado se prevé un

aumento de la condición basal de un 10,19%. Sin embargo, este aumento esta dado a

que las concentraciones basales de SO 2 son demasiado bajas respecto a los límites

normativos. **Esto se refleja en que las concentraciones basales más el aporte**

**modelado no superan un 4,68% del límite normativo, lo que indica la no**

**afectación a la calidad del aire basal.**

Es importante considerar que la concentración en el aire de los contaminantes puede ser

influida por diversos factores, entre los cuales están la tasa de emisión, las condiciones en

que los contaminantes son liberados a la atmósfera, la topografía del entorno, e

indudablemente las condiciones meteorológicas, es decir, la dispersión y concentración de

las partículas y gases en el aire quedará determinada por las condiciones ambientales en

donde éstos son liberados, como por ejemplo: gradiente de presión, gradiente de

temperatura, velocidad y dirección del vientos (los que a su vez están influenciados por las

características topográficas del lugar), entre otros.

Ademas, tal como menciona la guia para el uso de modelos de calidad del aire en el SEIA

todo modelo meteorológico representa una aproximación a la realidad por lo que sus

resultados tienen incertidumbres asociadas (ver apartado 7). Estas incertidumbres se

producen debido a las diferencias entre lo simulado por el modelo meteorologico WRF y

los datos observados de la estación Aeródromo La Independencia, propiedad del INIA.

Finalmente, la modelación de las emisiones del proyecto de material particulado (MP10 y

MP2,5) y gases (NO 2, SO 2 y CO) resultaron ser de baja magnitud concluyendo que, el

funcionamiento del **proyecto no representa un riesgo significativo a la salud ni**

**calidad de vida de la población, según los criterios establecidos en la legislación**

**ambiental vigente** . Considerando que en ningún caso la concentración proyectada

respecto de la concentración basal presentó un aumento significativo que generaría una

posible condición de riesgo para las componentes evaluadas.

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**

“PROYECTO HABITACIONAL LA GAMBOINA”

**Página 106 de**

**106**

## 9 Bibliografía

Hernandez- Garces, A., J. Souto, A. Rodríguez, S. Saavera, J. Casares, 2015. Validation of

CALMET/CALPUFF models simulations around a large power plant stack, p. 51.

Recuperado el 27 de junio de 2016, desde

http://revistas.ucm.es/index.php/FITE/article/view/51192/47527

Hernández-Garces, A., U. Jáuregui-Haga, J. González, J. Caseres-Long, S. Saavedra, F.

Guzmán-Martínez, A. Torres-Valle, 2016. Aplicaciones del modelo lagrangiano de

dispersión atmosférica CALPUFF, Ciencias de la Tierra y el Espacio, enero-junio, Vol. 17,

No 1, p. 37. ISSN 1729-3790. Recuperado el 29 de junio de 2016, desde

http://www.iga.cu/publicaciones/revista/assets/calpuffreview2.pdf.

Servicio de Evaluación Ambiental, 2012, Guía para el Uso de Modelos de Calidad del Aire

en el SEIA, p. 14-39. Recuperado el 01 de abril de 2016, desde

[http://www.sea.gob.cl/sites/default/files/migration_files/guias/Guia_uso_modelo_calidad_](http://www.sea.gob.cl/sites/default/files/migration_files/guias/Guia_uso_modelo_calidad_del_aire_seia.pdf)

del_aire_seia.pdf.

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Valores normados para MP10 y MP2,5 en Chile****

| Nivel | MP10 (μg/m3N) | MP2,5 (μg/m3) |
| --- | --- | --- |
| **Concentración Anual** | 50 | 20 |
| **Concentración 24 horas** | 130 | 50 |
| **Alerta** | 180-229 | 80-109 |
| **Preemergencia** | 230-329 | 110-169 |
| **Emergencia** | 330 o superior | 170 o superior |

**Tabla 3.: Valores normados para CO en Chile****

| Nivel | Unidad | Valor |
| --- | --- | --- |
| **Concentración 8 horas** | mg/m3N | 10 |
| **Concentración 8 horas** | ppmv | 9 |
| **Concentración 1 hora** | mg/m3N | 30 |
| **Concentración 1 hora** | ppmv | 26 |
| **Alerta** | mg/m3N | 17-33 |
| **Alerta** | ppmv | 15-29 |
| **Preemergencia** | mg/m3N | 34-39 |
| **Preemergencia** | ppmv | 30-34 |
| **Emergencia** | mg/m3N | 40 o superior |
| **Emergencia** | ppmv | 35 o superior |

**Tabla 4.: Porcentaje de superación concentración promedio anual de MP10,****

| Año | Porcentaje de<br>datos disponibles<br>(%) | Concentración<br>Promedio Anual<br>(μg/m3N) | Límite normativo<br>D.S. 12/2022 MMA<br>(μg/m3N) | Porcentaje de<br>excedencia de la<br>norma (%) |
| --- | --- | --- | --- | --- |
| 2014 | 99% | 71,9 | 50,0 | 44% |
| 2015 | 95% | 80,7 | 80,7 | 61% |
| 2016 | 100% | 72,5 | 72,5 | 45% |
| 2017 | 98% | 63,9 | 63,9 | 28% |
| 2018 | 98% | 55,1 | 55,1 | 10% |
| 2019 | 98% | 59,8 | 59,8 | 20% |
| 2020 | 99% | 55,7 | 55,7 | 11% |
| 2021 | 97% | 51,2 | 51,2 | 2% |

**Tabla 6.: Porcentaje de superación concentración promedio anual de MP2,5,****

| Año | Porcentaje de<br>datos disponibles<br>(%) | Concentración<br>Promedio Anual<br>(μg/m3) | Límite normativo<br>D.S. 12/2011 MMA<br>(μg/m3) | Porcentaje de<br>excedencia de la<br>norma (%) |
| --- | --- | --- | --- | --- |
| 2014 | 100% | 28,0 | 20,0 | 40% |
| 2015 | 99% | 24,1 | 24,1 | 20% |
| 2016 | 100% | 24,1 | 24,1 | 20% |
| 2017 | 98% | 23,4 | 23,4 | 17% |
| 2018 | 98% | 21,5 | 21,5 | 8% |
| 2019 | 97% | 24,5 | 24,5 | 23% |
| 2020 | 98% | 23,0 | 23,0 | 15% |
| 2021 | 98% | 26,0 | 26,0 | 30% |

**Tabla 7.: Registro de días declarados en alerta, preemergencia y emergencia****

| Año | Días de alerta | Días de preemergencia | Días de emergencia |
| --- | --- | --- | --- |
| 2014 | 16 | 3 | 0 |
| 2015 | 7 | 0 | 0 |
| 2016 | 10 | 2 | 0 |
| 2017 | 3 | 0 | 0 |
| 2018 | 4 | 1 | 0 |
| 2019 | 7 | 1 | 0 |
| 2020 | 5 | 1 | 0 |
| 2021 | 14 | 1 | 0 |

**Tabla 8.: Porcentaje de superación concentración horaria de SO** **2** **, EMRP****

| Año | Porcentaje de<br>datos disponibles<br>(%) | Concentración<br>Horaria (ppbv) | Límite normativo<br>D.S. 104/2019<br>MMA (ppbv) | Porcentaje de<br>excedencia de la<br>norma (%) |
| --- | --- | --- | --- | --- |
| 2014 | 92% | 9,1 | 134 | No excede la norma |
| 2015 | 97% | 6,2 | 6,2 | No excede la norma |
| 2016 | 100% | 6,9 | 6,9 | No excede la norma |
| 2017 | 98% | 5,3 | 5,3 | No excede la norma |
| 2018 | 98% | 7,6 | 7,6 | No excede la norma |
| 2019 | 97% | 5,6 | 5,6 | No excede la norma |
| 2020 | 98% | 1,9 | 1,9 | No excede la norma |
| 2021 | 99% | 1,4 | 1,4 | No excede la norma |

**Tabla 9.: Porcentaje de superación concentración 24 horas de SO** **2** **, EMRP****

| Año | Porcentaje de<br>datos disponibles<br>(%) | Concentración<br>24 Horas (ppbv) | Límite normativo<br>D.S. 104/2019<br>MMA (ppbv) | Porcentaje de<br>excedencia de la<br>norma (%) |
| --- | --- | --- | --- | --- |
| 2014 | 92% | 7,7 | 57 | No excede la norma |
| 2015 | 97% | 11,8 | 11,8 | No excede la norma |
| 2016 | 100% | 8,5 | 8,5 | No excede la norma |
| 2017 | 98% | 8,4 | 8,4 | No excede la norma |
| 2018 | 98% | 9,0 | 9,0 | No excede la norma |
| 2019 | 97% | 5,5 | 5,5 | No excede la norma |
| 2020 | 98% | 1,8 | 1,8 | No excede la norma |
| 2021 | 99% | 1,3 | 1,3 | No excede la norma |

**Tabla 10.: Porcentaje de superación concentración promedio anual de SO** **2** **,****

| Año | Porcentaje de<br>datos disponibles<br>(%) | Concentración<br>Anual (ppbv) | Límite normativo<br>D.S. 104/2019<br>MMA (ppbv) | Porcentaje de<br>excedencia de la<br>norma (%) |
| --- | --- | --- | --- | --- |
| 2014 | 92% | 2,1 | 23 | No excede la norma |
| 2015 | 97% | 2,0 | 2,0 | No excede la norma |
| 2016 | 100% | 2,0 | 2,0 | No excede la norma |
| 2017 | 98% | 2,3 | 2,3 | No excede la norma |
| 2018 | 98% | 3,9 | 3,9 | No excede la norma |
| 2019 | 97% | 1,8 | 1,8 | No excede la norma |
| 2020 | 98% | 1,1 | 1,1 | No excede la norma |
| 2021 | 99% | 1,0 | 1,0 | No excede la norma |

**Tabla 12.: Porcentaje de superación concentración máxima horaria CO, EMRP****

| Año | Porcentaje de<br>datos disponibles<br>(%) | Concentración<br>Horaria (ppmv) | Límite normativo<br>D.S. 115/2002<br>MINSEGEPRES<br>(ppmv) | Porcentaje de<br>excedencia de la<br>norma (%) |
| --- | --- | --- | --- | --- |
| 2014 | 94% | 4,5 | 26 | No excede la norma |
| 2015 | 99% | 9,3 | 9,3 | No excede la norma |
| 2016 | 100% | 8,8 | 8,8 | No excede la norma |
| 2017 | 98% | 7,5 | 7,5 | No excede la norma |
| 2018 | 96% | 10,6 | 10,6 | No excede la norma |
| 2019 | 98% | 4,6 | 4,6 | No excede la norma |
| 2020 | 98% | 3,8 | 3,8 | No excede la norma |
| 2021 | 99% | 4,3 | 4,3 | No excede la norma |

**Tabla 13.: Porcentaje de superación concentración máxima 8 horas CO, EMRP****

| Año | Porcentaje de<br>datos disponibles<br>(%) | Concentración 8<br>Horas (ppmv) | Límite normativo<br>D.S. 115/2002<br>MINSEGEPRES<br>(ppmv) | Porcentaje de<br>excedencia de la<br>norma (%) |
| --- | --- | --- | --- | --- |
| 2014 | 94% | 2,9 | 9 | No excede la norma |
| 2015 | 99% | 3,2 | 3,2 | No excede la norma |
| 2016 | 100% | 3,1 | 3,1 | No excede la norma |
| 2017 | 98% | 4,1 | 4,1 | No excede la norma |
| 2018 | 96% | 4,2 | 4,2 | No excede la norma |
| 2019 | 98% | 3,1 | 3,1 | No excede la norma |
| 2020 | 98% | 2,8 | 2,8 | No excede la norma |
| 2021 | 99% | 3,1 | 3,1 | No excede la norma |

**Tabla 14.: Características del modelo****

| Año de modelación | Col2 | 2021 |
| --- | --- | --- |
| **Periodo de Modelación** | **Periodo de Modelación** | 1 año calendario |
| **Resolución temporal** | **Resolución temporal** | 1 hora |
| **Resolución espacial** | **Resolución espacial** | 1 km |
| **Coordenadas del centroide** | **Latitud** | -34,193° |
| **Coordenadas del centroide** | **Longitud** | -70,731° |
| **DATUM** | **DATUM** | NWS - 84 |
| **Coordenadas del modelo** | **Coordenadas del modelo** | LCC |
| **Dominio de modelación** | **X ** | 57 |
| **Dominio de modelación** | **Y ** | 57 |
| **Dominio de modelación** | **Z ** | 10 |

**Tabla 15.: Descripción de los puntos receptores****

| Receptor | Coordenada UTM WGS 84 HUSO 19 S | Col3 | Descripción | Distancia al<br>centro del<br>proyecto (m) |
| --- | --- | --- | --- | --- |
| **Receptor** | **Este (m)** | **Norte (m)** | **Norte (m)** | **Norte (m)** |
| 1 | 343.218 | 6.219.033 | Vivienda I | 200 |
| 2 | 343.411 | 6.218.900 | Vivienda II | 242 |
| 3 | 343.380 | 6.218.678 | Vivienda III | 258 |
| 4 | 343.193 | 6.218.692 | Situación basal | 146 |
| 5 | 343.094 | 6.218.644 | Vivienda IV | 210 |
| 6 | 342.930 | 6.218.700 | Colegio San Sebastián School | 282 |
| 7 | 342.875 | 6.218.841 | Vivienda V | 302 |
| 8 | 343.030 | 6.219.047 | Vivienda VI | 256 |
| 9 | 343.197 | 6.219.156 | Vivienda VII | 320 |
| 10 | 343.335 | 6.219.105 | Plaza | 311 |
| 11 | 343.708 | 6.218.847 | Vivienda VIII | 531 |
| 12 | 343.616 | 6.218.437 | Vivienda IX | 594 |
| 13 | 343.345 | 6.218.091 | Vivienda X | 765 |
| 14 | 343.100 | 6.218.361 | Vivienda XI | 482 |
| 15 | 342.845 | 6.218.290 | Parque Villa Nueva Cordillera | 640 |
| 16 | 342.453 | 6.218.756 | Vivienda XII | 729 |
| 17 | 342.946 | 6.219.279 | Cancha Club Unión Gamboina | 499 |
| 18 | 342.443 | 6.219.920 | CESFAM Ignacio Caroca | 1.308 |
| 19 | 342.015 | 6.218.518 | EMRP Rancagua I | 1.205 |

**Tabla 16.: Coordenadas de modelación de las fuentes areales****

| Actividad para<br>modelar | Unidad del<br>proyecto | Área (m2) | Coordenada UTM. HUSO 19 S.<br>DATUM WGS 84 | Col5 |
| --- | --- | --- | --- | --- |
| **Actividad para**<br>**modelar** | **Unidad del**<br>**proyecto** | **Área (m2) ** | **Este (m)** | **Norte (m)** |
| Polígono<br>Construcción | P1 | 11.596 | 343.262 | 6.218.682 |
| Polígono<br>Construcción | P1 | 11.596 | 343.285 | 6.218.850 |
| Polígono<br>Construcción | P1 | 11.596 | 343.168 | 6.218.765 |
| Polígono<br>Construcción | P1 | 11.596 | 343.256 | 6.218.874 |
| Polígono<br>Construcción | P2 | 9.886 | 343.256 | 6.218.874 |
| Polígono<br>Construcción | P2 | 9.886 | 343.184 | 6.218.787 |
| Polígono<br>Construcción | P2 | 9.886 | 343.176 | 6.218.942 |
| Polígono<br>Construcción | P2 | 9.886 | 343.132 | 6.218.833 |
| Polígono<br>Construcción | P3 | 4.891 | 343.176 | 6.218.942 |
| Polígono<br>Construcción | P3 | 4.891 | 343.249 | 6.218.881 |
| Polígono<br>Construcción | P3 | 4.891 | 343.214 | 6.218.988 |
| Polígono<br>Construcción | P3 | 4.891 | 343.264 | 6.218.950 |

**Tabla 17.: Concentración modelada en puntos receptores con respecto a MP10** **y****

| Punto | Concentración MP10 (μg/m3) | Col3 | Col4 | Col5 | Concentración MP2,5 (μg/m3) | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Punto** | **Anual** | **%respecto**<br>**a la norma** | **Diario** | **%respecto**<br>**a la norma** | **Anual** | **%respecto**<br>**a la norma** | **Diario** | **%respecto**<br>**a la norma** |
| **R1** | **0,405** | **0,81%** | **2,451** | **1,89%** | **0,133** | **0,67%** | **0,821** | **1,64%** |
| **R2** | **0,419** | **0,84%** | **2,475** | **1,90%** | **0,141** | **0,71%** | **0,832** | **1,66%** |
| R3 | 0,269 | 0,54% | 2,050 | 1,58% | 0,091 | 0,46% | 0,692 | 1,38% |
| **R4** | **0,489** | **0,98%** | **2,734** | **2,10%** | **0,171** | **0,86%** | **0,941** | **1,88%** |
| **R5** | **0,331** | **0,66%** | **2,423** | **1,86%** | **0,118** | **0,59%** | **0,823** | **1,65%** |
| R6 | 0,270 | 0,54% | 2,453 | 1,89% | 0,092 | 0,46% | 0,824 | 1,65% |
| **R7** | **0,240** | **0,48%** | **2,606** | **2,00%** | **0,082** | **0,41%** | **0,872** | **1,74%** |
| R8 | 0,228 | 0,46% | 2,223 | 1,71% | 0,077 | 0,39% | 0,752 | 1,50% |
| R9 | 0,205 | 0,41% | 1,721 | 1,32% | 0,069 | 0,35% | 0,579 | 1,16% |
| R10 | 0,319 | 0,64% | 1,871 | 1,44% | 0,106 | 0,53% | 0,631 | 1,26% |
| R11 | 0,148 | 0,30% | 1,333 | 1,03% | 0,050 | 0,25% | 0,454 | 0,91% |
| R12 | 0,102 | 0,20% | 1,030 | 0,79% | 0,035 | 0,18% | 0,351 | 0,70% |
| R13 | 0,056 | 0,11% | 0,552 | 0,42% | 0,019 | 0,10% | 0,189 | 0,38% |
| R14 | 0,148 | 0,30% | 1,417 | 1,09% | 0,051 | 0,26% | 0,483 | 0,97% |
| R15 | 0,106 | 0,21% | 1,000 | 0,77% | 0,037 | 0,19% | 0,343 | 0,69% |
| R16 | 0,082 | 0,16% | 0,863 | 0,66% | 0,028 | 0,14% | 0,292 | 0,58% |
| R17 | 0,074 | 0,15% | 0,708 | 0,54% | 0,025 | 0,13% | 0,237 | 0,47% |
| R18 | 0,003 | 0,01% | 0,025 | 0,02% | 0,001 | 0,01% | 0,008 | 0,02% |

**Tabla 18.: Concentración modelada en puntos receptores con respecto a SO** **2** **.****

| Punto | Concentración SO (μg/m3N)<br>2 | Col3 | Col4 | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Punto** | **Horario** | **%respecto**<br>**a la norma** | **Diario** | **%respecto**<br>**a la norma** | **Anual** | **%respecto**<br>**a la norma** |
| **R1** | **8,345** | **2,38%** | **2,183** | **1,46%** | **0,247** | **0,41%** |
| R2 | 8,044 | 2,30% | 2,192 | 1,46% | 0,235 | 0,39% |
| R3 | 8,413 | 2,40% | 2,048 | 1,37% | 0,225 | 0,38% |
| **R4** | **10,827** | **3,09%** | **3,869** | **2,58%** | **1,129** | **1,88%** |
| **R5** | **10,628** | **3,04%** | **3,675** | **2,45%** | **0,800** | **1,33%** |
| **R6** | **10,066** | **2,88%** | **3,351** | **2,23%** | **0,298** | **0,50%** |
| **R7** | **9,374** | **2,68%** | **2,608** | **1,74%** | **0,241** | **0,40%** |
| R8 | 7,673 | 2,19% | 2,198 | 1,47% | 0,198 | 0,33% |
| R9 | 5,730 | 1,64% | 1,495 | 1,00% | 0,151 | 0,25% |
| R10 | 5,814 | 1,66% | 1,447 | 0,96% | 0,171 | 0,29% |
| R11 | 3,947 | 1,13% | 1,223 | 0,82% | 0,097 | 0,16% |
| R12 | 3,803 | 1,09% | 0,967 | 0,64% | 0,090 | 0,15% |
| R13 | 2,645 | 0,76% | 0,625 | 0,42% | 0,063 | 0,11% |
| R14 | 7,246 | 2,07% | 1,947 | 1,30% | 0,176 | 0,29% |
| R15 | 4,984 | 1,42% | 1,639 | 1,09% | 0,137 | 0,23% |
| R16 | 3,236 | 0,92% | 1,027 | 0,68% | 0,086 | 0,14% |
| R17 | 1,832 | 0,52% | 0,509 | 0,34% | 0,049 | 0,08% |
| R18 | 0,034 | 0,01% | 0,016 | 0,01% | 0,001 | 0,00% |

**Tabla 20.: Concentración modelada en puntos receptores con respecto a CO****

| Punto | Concentración CO (mg/m3N) | Col3 | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Punto** | **Horario** | **%respecto a la**<br>**norma** | **8 horas** | **%respecto a la**<br>**norma** |
| **R1** | **0,0060** | **0,020%** | **0,0033** | **0,033%** |
| R2 | 0,0041 | 0,014% | 0,0029 | 0,029% |
| R3 | 0,0035 | 0,012% | 0,0030 | 0,030% |
| **R4** | **0,0075** | **0,025%** | **0,0041** | **0,041%** |
| **R5** | **0,0051** | **0,017%** | **0,0037** | **0,037%** |
| **R6** | **0,0043** | **0,014%** | **0,0035** | **0,035%** |
| R7 | 0,0034 | 0,011% | 0,0032 | 0,032% |
| **R8** | **0,0041** | **0,014%** | **0,0030** | **0,030%** |
| R9 | 0,0032 | 0,011% | 0,0025 | 0,025% |
| R10 | 0,0029 | 0,010% | 0,0025 | 0,025% |
| R11 | 0,0009 | 0,003% | 0,0017 | 0,017% |
| R12 | 0,0009 | 0,003% | 0,0014 | 0,014% |
| R13 | 0,0007 | 0,002% | 0,0008 | 0,008% |
| R14 | 0,0015 | 0,005% | 0,0021 | 0,021% |
| R15 | 0,0014 | 0,005% | 0,0014 | 0,014% |
| R16 | 0,0011 | 0,004% | 0,0012 | 0,012% |
| R17 | 0,0009 | 0,003% | 0,0009 | 0,009% |
| R18 | 0,0000 | 0,000% | 0,0000 | 0,000% |

**Tabla 21.: Aumento de la concentración basal en la EMRP Rancagua I, año 2021****

| Contaminante | Col2 | Registro EMRP | Modelado<br>(ug/m3) | Proyectado<br>(ug/m3) | Porcentaje<br>de aumento |
| --- | --- | --- | --- | --- | --- |
| **Contaminante** | **Contaminante** | **(ug/m3) ** | **(ug/m3) ** | **(ug/m3) ** | **(ug/m3) ** |
| MP10 | Anual | 51,15 | 0,025 | 51,18 | **0,05%** |
| MP10 | 24 horas | 129,22 | 0,173 | 129,39 | **0,13%** |
| MP2,5 | Anual | 26,03 | 0,009 | 26,04 | **0,03%** |
| MP2,5 | 24 horas | 91,71 | 0,060 | 91,77 | **0,07%** |
| SO2 | Anual | 2,61 | 0,015 | 2,625 | **0,57%** |
| SO2 | 24 horas | 3,39 | 0,153 | 3,543 | **4,51%** |
| SO2 | 1 hora | 3,66 | 0,373 | 4,033 | **10,19%** |
| CO | 8 horas | 4,78 | 0,0003 | 4,780 | **0,01%** |
| CO | 1 hora | 3,44 | 0,0002 | 3,440 | **0,01%** |

**Tabla 22.: Concentraciones basales de SO** **2** **y aporte del proyecto****

| Contaminante | Col2 | Registro EMRP | Límite normativo | Porcentaje<br>respecto a<br>la norma | Proyectado | Porcentaje<br>respecto a<br>la norma |
| --- | --- | --- | --- | --- | --- | --- |
| **Contaminante** | **Contaminante** | **(ug/m3N)** | **(ug/m3N)** | **(ug/m3N)** | **(ug/m3N)** | **(ug/m3N)** |
| SO2 | Anual | 2,61 | 60 | 4,35% | 2,63 | **4,38%** |
| SO2 | 24 horas | 3,39 | 150 | 2,26% | 3,54 | **2,36%** |
| SO2 | 1 hora | 3,66 | 350 | 1,05% | 4,03 | **1,15%** |

**Tabla 23.: Estadísticos de variables meteorológicas modeladas.****

| Variable | Coeficiente de<br>correlación lineal<br>(r) | Coeficiente de<br>determinación (R2) | Percent bias<br>(PBIAS) |
| --- | --- | --- | --- |
| Temperatura horaria | 0,89 | 0,79 | -0,15 |
| Velocidad del viento horaria | 0,47 | 0,22 | 0,90 |
| Componente zonal del viento | 0,1 | 0,01 | - |
| Componente meridional del<br>viento | 0,49 | 0,24 | - |
