---
title: Sin título
author: Maryorie Schulz
date: D:20230228214218-03'00'
language: es
type: report
pages: 132
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - MODELACIÓN ATMOSFÉRICA DE EMISIONES
-->

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 1 de 132**

# MODELACIÓN ATMOSFÉRICA DE EMISIONES

**FEBRERO 2023**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**ÍNDICE**

**Página 2 de 132**

**1** **INTRODUCCIÓN ................................................................................................................ 6**

**2** **OBJETIVOS ......................................................................................................................... 8**

**3** **MARCO LEGAL REGULATORIO ..................................................................................... 9**

**3.1** **Estado de la Calidad del Aire en zonas circundantes al proyecto ........................ 12**

**3.2** **Análisis del Cumplimiento Normativo .................................................................. 12**
**4** **JUSTIFICACIÓN DE LOS MODELOS UTILIZADOS EN EL ESTUDIO ..................... 24**

**4.1** **Uso del modelo CALPUFF ...................................................................................... 24**

**4.2** **Uso del modelo WRF ............................................................................................. 26**
**5** **METODOLOGÍA .............................................................................................................. 27**

**5.1** **Modelación de partículas ...................................................................................... 27**
5.1.1 Modelación meteorológica ........................................................................................................ 27
5.1.2 Modelación de dispersión de contaminantes ............................................................................. 27
5.1.3 Criterios para la modelación de partículas .................................................................................. 33

**6** **RESULTADOS.................................................................................................................. 41**

**6.1** **Modelamiento meteorológico ............................................................................... 41**
6.1.2 Caracterización de la velocidad y dirección de los vientos Anual y Estacional. ............................. 42
6.1.3 Caracterización de la Temperatura del Aire ................................................................................ 57
6.1.4 Altura de Capa de Mezcla........................................................................................................... 60
6.1.5 Caracterización de la precipitación ............................................................................................. 62

**6.2** **Concentraciones Modeladas ................................................................................. 63**

6.2.1 Dispersión e Isoconcentración Material Particulado Respirable, MP10 ....................................... 63
6.2.2 Dispersión e Isoconcentración Material Particulado Fino Respirable, MP2,5 ............................... 73
6.2.3 Dispersión Dióxido de Nitrógeno, NO 2 ........................................................................................ 81
6.2.4 Dispersión Dióxido de Azufre (SO 2 ) ............................................................................................. 89
6.2.5 Dispersión Monóxido de Carbono (CO)..................................................................................... 102

6.2.6 Modelación discreta de las emisiones contaminantes .............................................................. 111

6.2.7 Aporte a la estación de Monitoreo de Representatividad Poblacional (EMRP) .......................... 118
**7** **ANÁLISIS DE INCERTIDUMBRE ............................................................................... 120**

**7.1** **Temperatura ....................................................................................................... 122**

**7.2** **Velocidad del viento ........................................................................................... 123**

**7.3** **Componente zonal del viento ............................................................................. 125**

**7.4** **Test de Bondad de Ajuste sobre el Modelo Meteorológico................................. 126**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 3 de 132**

**8** **CONCLUSIÓN ................................................................................................................ 127**

**9** **BIBLIOGRAFÍA ............................................................................................................. 130**

**ÍNDICE DE FIGURAS**

Figura 1. Ubicación del proyecto .................................................................................. 6
Figura 2. Ubicación EMRP Rancagua I ......................................................................... 13
Figura 3. Concentración promedio 24 horas de MP10, EMRP Rancagua I ........................ 14
Figura 4. Concentración promedio trianual MP10, EMRP Rancagua I .............................. 15
Figura 5. Concentración promedio 24 horas de MP2,5, EMRP Rancagua I ....................... 16
Figura 6. Concentración promedio trianual MP2,5, EMRP Rancagua I ............................. 17
Figura 7. Concentración promedio trianual horaria de SO 2, EMRP Rancagua I ................. 19
Figura 8. Concentración promedio trianual 24 horas de SO 2, EMRP Rancagua I .............. 20
Figura 9. Concentración promedio trianual de SO 2, EMRP Rancagua I ............................ 21
Figura 10. Concentración promedio trianual horaria de CO, EMRP Rancagua I ................ 22
Figura 11. Concentración promedio trianual 8 horas de CO, EMRP Rancagua I ............... 24
Figura 12. Receptores discretos dentro del proyecto..................................................... 31
Figura 13. Receptores discretos fuera del polígono del proyecto .................................... 32
Figura 14. Polígonos de modelación representativos de cada unidad modelada ............... 39
Figura 15. Elevación del terreno en el área de la modelación meteorológica ................... 41
Figura 16. Rosa de los vientos anual, WRF 2021. ......................................................... 42
Figura 17. Frecuencia de los vientos, año 2021. ........................................................... 44
Figura 18. Rosa de los vientos verano, WRF 2021. ....................................................... 45
Figura 19. Frecuencia de los vientos en verano, año 2021. ........................................... 47
Figura 20. Rosa de los vientos otoño, WRF 2021. ......................................................... 48
Figura 21. Frecuencia de los vientos en otoño, año 2021. ............................................. 50
Figura 22. Rosa de los vientos invierno, WRF 2021. ..................................................... 51
Figura 23. Frecuencia de los vientos en invierno, año 2021. .......................................... 53
Figura 24. Rosa de los vientos en primavera, WRF 2021. .............................................. 54
Figura 25. Frecuencia de los vientos en primavera, año 2021. ....................................... 56
Figura 26. Perfil diario de velocidad del viento, WRF año 2021. ..................................... 57
Figura 27. Temperatura Mensual WRF, año 2021. ........................................................ 58
Figura 28. Perfil diario de Temperatura, WRF año 2021. ............................................... 59
Figura 29. Evolución diaria de la altura de capa de mezcla, WRF año 2021. .................... 61
Figura 30. Precipitación Anual, WRF 2021. .................................................................. 62
Figura 31. Dispersión de la pluma de MP10 como concentración de 24 horas ................. 66
Figura 32. Dispersión de la pluma de MP10 como concentración de 24 horas, receptores

internos .................................................................................................................... 67

Figura 33. Isolíneas de concentración de MP10 como concentración de 24 horas. ........... 68

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 4 de 132**

Figura 34. Dispersión de la pluma de MP10 como concentración promedio anual. ........... 70
Figura 35. Dispersión de la pluma de MP10 como concentración promedio anual,
receptores internos ................................................................................................... 71
Figura 36. Isolíneas de concentración de MP10 como concentración promedio anual. ...... 72
Figura 37. Dispersión de la pluma de MP2,5 como concentración promedio diario ........... 74
Figura 38. Dispersión de la pluma de MP2,5 como concentración promedio diaria,
receptores internos ................................................................................................... 75
Figura 39. Isolíneas de concentración de MP2,5 como concentración promedio diaria...... 76
Figura 40. Dispersión de la pluma de MP2,5 como concentración promedio anual ........... 78
Figura 41. Dispersión de la pluma de MP2,5 como concentración promedio anual,
receptores internos ................................................................................................... 79
Figura 42. Isolíneas de concentración de MP2,5 como concentración promedio anual. ..... 80
Figura 43. Dispersión de la pluma de NO 2 como concentración máxima horaria .............. 82
Figura 44. Dispersión de la pluma de NO 2 como concentración máxima horaria, receptores

internos .................................................................................................................... 83

Figura 45. Isolíneas de concentración de NO 2 como concentración máxima horaria. ........ 84
Figura 46. Dispersión de la pluma de NO 2 como concentración anual. ............................ 86
Figura 47. Dispersión de la pluma de NO 2 como concentración anual, receptores internos

............................................................................................................................... 87

Figura 48. Isolíneas de concentración de NO 2 como concentración anual. ...................... 88
Figura 49. Dispersión de la pluma de SO 2 como concentración horaria ........................... 91
Figura 50. Dispersión de la pluma de SO 2 como concentración horaria, receptores internos

............................................................................................................................... 92

Figura 51. Isolíneas de concentración de SO 2 como concentración horaria ..................... 93
Figura 52. Dispersión de la pluma de SO 2 como concentración 24 horas ......................... 95
Figura 53. Dispersión de la pluma de SO 2 como concentración 24 horas, receptores

internos .................................................................................................................... 96

Figura 54. Isolíneas de concentración de SO 2 como concentración 24 horas ................... 97
Figura 55. Dispersión de la pluma de SO 2 como concentración anual ............................. 99
Figura 56. Dispersión de la pluma de SO 2 como concentración anual, receptores internos

............................................................................................................................. 100

Figura 57. Isolíneas de concentración de SO 2 como concentración anual ...................... 101
Figura 58. Dispersión de la pluma de CO como concentración horaria .......................... 104
Figura 59. Dispersión de la pluma de CO como concentración horaria, receptores internos

............................................................................................................................. 105

Figura 60. Isolíneas de concentración de CO como concentración horaria .................... 106
Figura 61. Dispersión de la pluma de CO como concentración 8 horas ......................... 108
Figura 62. Dispersión de la pluma de CO como concentración 8 horas, receptores internos

............................................................................................................................. 109

Figura 63. Isolíneas de concentración de CO como concentración 8 horas .................... 110
Figura 64. Correlación entre temperaturas observadas y modeladas. ........................... 122
Figura 65. Frecuencia de temperaturas observadas y modeladas. ................................ 123

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 5 de 132**

Figura 66. Correlación entre velocidad del viento observada y modeladas. ................... 124
Figura 67. Frecuencia de velocidad del viento observadas y modeladas. ...................... 125
Figura 68. Frecuencia de velocidad del viento observadas y modeladas. ...................... 126

**ÍNDICE DE TABLAS**

Tabla 1. Valores normados para MP10 y MP2,5 en Chile ................................................ 9
Tabla 2. Valores normados para NO 2 y SO 2 en Chile ..................................................... 10
Tabla 3. Valores normados para CO en Chile ............................................................... 10
Tabla 4. Porcentaje de superación concentración promedio anual de MP10, EMRP
Rancagua I. .............................................................................................................. 14
Tabla 5. Registro de días declarados en alerta, preemergencia y emergencia para MP10 en
la EMRP Rancagua I .................................................................................................. 15
Tabla 6. Porcentaje de superación concentración promedio anual de MP2,5, EMRP
Rancagua I. .............................................................................................................. 16
Tabla 7. Registro de días declarados en alerta, preemergencia y emergencia para MP2,5
en la EMRP Rancagua I .............................................................................................. 17
Tabla 8. Porcentaje de superación concentración horaria de SO 2, EMRP Rancagua I. ...... 18
Tabla 9. Porcentaje de superación concentración 24 horas de SO 2, EMRP Rancagua I. .... 19
Tabla 10. Porcentaje de superación concentración promedio anual de SO 2, EMRP
Rancagua I. .............................................................................................................. 20
Tabla 11. Registro de días declarados en alerta, preemergencia y emergencia para SO 2 en
la EMRP Rancagua I .................................................................................................. 21
Tabla 12. Porcentaje de superación concentración máxima horaria CO, EMRP Rancagua I.

............................................................................................................................... 22

Tabla 13. Porcentaje de superación concentración máxima 8 horas CO, EMRP Rancagua I.

............................................................................................................................... 23

Tabla 14. Características del modelo ........................................................................... 27

Tabla 15. Descripción de los puntos receptores ............................................................ 28
Tabla 16. Coordenadas de modelación de las fuentes areales Fase de Operación ............ 33
Tabla 17. Frecuencia de la dirección de los vientos anual, WRF 2021. ............................ 43
Tabla 18. Frecuencia de los vientos verano, WRF. ........................................................ 45
Tabla 19. Frecuencia de los vientos otoño, WRF. ......................................................... 49
Tabla 20. Frecuencia de los vientos invierno, WRF. ...................................................... 51
Tabla 21. Frecuencia de los vientos en primavera, WRF. ............................................... 54
Tabla 22. Concentración modelada en puntos receptores con respecto a MP10 y MP2,5.112
Tabla 23. Concentración modelada en puntos receptores con respecto a NO 2 ............... 114
Tabla 24. Concentración modelada en puntos receptores con respecto a SO 2 . .............. 115
Tabla 25. Concentraciones de CO en puntos receptores .............................................. 117
Tabla 26. Aumento de la concentración basal en la EMRP Rancagua I, año 2021 .......... 118
Tabla 27. Estadísticos de variables meteorológicas modeladas. ................................... 122

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**1** **INTRODUCCIÓN**

**Página 6 de 132**

El proyecto inmobiliario **“Brisas de Machalí II”** ubicado en la comuna de Machalí,

perteneciente a la provincia de Cachapoal, región del Libertador Bernardo O’Higgins (ver

Figura 1). Consiste en la construcción de 251 unidades habitacionales del tipo casas, en una

superficie total de 11,8 hectáreas aproximadamente. A estas viviendas se les sumaran las

102 unidades habitacionales actualmente en construcción, que constituyen la situación basal

del proyecto, emplazados en una superficie aproximada de 4,8 hectáreas. La construcción

del proyecto inmobiliario **“Brisas de Machalí II”**, se llevará a cabo en un plazo de

aproximadamente 36 meses, partiendo el primer semestre del año 2023 para finalizar el

primer semestre del año 2026.

**Figura 1. Ubicación del proyecto**

Con este estudio se busca predecir la concentración de material particulado grueso (MP10),

material particulado fino (MP2,5), y de los gases óxido de nitrógeno (NOx), óxido de azufre

(SOx), y monóxido de carbono (CO). Además, se busca evaluar su contribución en puntos

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 7 de 132**

receptores de interés y en las estaciones de calidad del aire más cercanas, esto último

respecto a su situación basal.

La modelación de las emisiones se realizó en base a los resultados obtenidos de la

actualización del informe de estimación de emisiones atmosféricas que se presenta en la

ADENDA II. Dado que el objetivo de la presente modelación es predecir las concentraciones

de MP10, MP2,5, NOx, SOx y CO a las cuales estarán expuestos los receptores cercanos al

área de proceso, es que se considera como escenario de modelación el año donde se alcanza

el máximo de emisiones directas de MP. En la tabla 88 del informe de estimación de

emisiones se muestra que el año donde se alcanza la máxima emisión de MP10 dentro del

proyecto es el año 4, donde se efectúa la plena operación del proyecto.

La evaluación de la dispersión y concentración de las emisiones de material particulado y

gases se realizó mediante el programa CALPUFF, el cual es un modelo de dispersión usado

ampliamente para la simulación de las concentraciones en el ambiente, producto de

emisiones por operaciones normales, con el objeto de establecer, desarrollar y analizar

escenarios de emisión y regulación. A su vez, CALPUFF es recomendado por el Ministerio de

Medio Ambiente en la “Guía para el Uso de Modelos de Calidad del Aire en el SEIA”,

publicada el año 2012. Los resultados y análisis de esta evaluación se presentan en el

siguiente informe.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 8 de 132**

**2** **Objetivos**

El presente informe, tiene como objetivo general cuantificar y evaluar el efecto en la

atmósfera debido a las emisiones de contaminantes generadas por el proyecto inmobiliario

**“Brisas de Machalí II”** y cuantificar sus concentraciones.

Para lo anterior se plantean los siguientes objetivos específicos:

 Evaluar en términos de concentración, el alcance de las emisiones de MP10, MP2,5,

NOx, SOx y CO en la atmósfera.

 Evaluar la concentración de MP10, MP2,5, NOx, SOx y CO en los receptores que

actualmente se encuentren cercanos al proyecto, así como en las estaciones de

calidad del aire emplazadas cercanos a éste.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**3** **Marco Legal Regulatorio**

**Página 9 de 132**

Actualmente, los contaminantes MP10, MP2,5, NO 2, SO 2 y CO están regulados bajo normas

de calidad primaria, cuyo objetivo es proteger la salud de las personas de los efectos agudos

y crónicos de la exposición de estos contaminantes con un riesgo aceptable. Para esto, se

fijan límites de concentración permitidos, condiciones de superación de la norma y los

niveles que dan paso a situaciones de emergencia ambiental.

El material particulado respirable MP10 es regulado por el D.S. 12/2022 del Ministerio del

Medio Ambiente, mientras el material particulado fino respirable MP2,5 es regulado por el

D.S. 12/2011 del Ministerio del Medio Ambiente.

En la Tabla 1 se aprecian los valores del límite anual y diario para los contaminante MP10 y

MP2,5, además de los rangos que dan origen a situaciones de alerta, preemergencia y

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

 - Si el percentil 98 (P98) de las concentraciones de 24 horas durante un año sea igual

o superior a 130 μg/m3N.

 - Si durante un año se registrasen siete o más días cuya concentración sea mayor a

130 μg/m3N.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 10 de 132**

En el mismo contexto, las condiciones de superación de la norma de MP2,5 son las que se

describen a continuación:

 - Cuando el promedio de la concentración anual de tres años consecutivos iguale o

supere los 20 μg/m3.

 - Si el percentil 98 (P98) de las concentraciones de 24 horas durante un año sea igual

o superior a 50 μg/m3.

En la misma línea, el Dióxido De Nitrógeno (NO 2 ) es regulado por el D.S. 114/2003 del

Ministerio Secretaría General De La Presidencia, el Dióxido De Azufre (SO 2 ) es regulado por

el D.S. 104/2019 del Ministerio del Medio Ambiente, y el Monóxido De Carbono (CO) es

regulado por el D.S. 115/2002 del Ministerio Secretaría General De La Presidencia.

En la Tabla 2 y Tabla 3 se aprecian los valores del límite anual, diario, de 8 horas y horario

para los contaminantes NO 2, SO 2 y CO, además de los rangos que dan origen a situaciones

de alerta, preemergencia y emergencia ambiental.

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

Fuente: En base a D.S. 114/2003 MINSEGEPRES y D.S. 104/2019 MMA

**Tabla 3. Valores normados para CO en Chile**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 11 de 132**

|Nivel|Unidad|CO|
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

Las condiciones de superación de la norma de NO 2 son las que se describen a continuación:

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

 Cuando el promedio trianual del percentil 99 (P99) de los máximos diarios de

concentración de 8 horas durante un año iguale o supere los 10 mg/m3N.

 Cuando el promedio trianual del percentil 99 (P99) de los máximos diarios de

concentración de 1 hora durante un año iguale o supere los 30 mg/m3N.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 12 de 132**

**3.1** **Estado de la Calidad del Aire en zonas circundantes al proyecto**

El valle central de la Región del Libertador General Bernardo O'Higgins fue declarado zona

saturada por material particulado respirable MP10, como concentración anual y de 24 horas,

por medio del D.S N°7/2009 (MMA), y como zona saturada por material particulado fino

respirable MP2,5, como concentración anual y de 24 horas, por el D.S N°42/2018 (MMA),

contando con un Plan De Descontaminación Atmosférica vigente, establecido en el D.S

N°15/2013 del MMA, en los cuales se incluye la comuna de Machalí, lugar de emplazamiento

del proyecto.

**3.2** **Análisis del Cumplimiento Normativo**

Para llevar a cabo el siguiente análisis, se utilizó la Estación Rancagua I, ubicada a

aproximadamente 4,2 km de distancia del proyecto (Ver Figura 2). Dicha estación

corresponde a la más cercana al proyecto, y que cuenta con la mayor cantidad de

información disponible para efectos del levantamiento de información de la línea de base

del proyecto, sin embargo, no posee datos actualizados del contaminante NO 2 . La

información extraída de la Estación Rancagua I comprende el periodo 2014 - 2021.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Figura 2. Ubicación EMRP Rancagua I**

**Página 13 de 132**

El D.S. 12/2022 MMA establece la norma primaria de calidad ambiental para material

particulado respirable MP10, regulando la concentración promedio anual y diaria.

En la Figura 3 se observa que el percentil 98 de la concentración promedio 24 horas supera

los límites establecidos por la norma primaria de calidad del aire para MP10 entre los años

2014 y 2017, disminuyendo su concentración el año 2018, para luego aumentar el año 2019

y disminuir nuevamente los años 2020 y 2021, manteniéndose por debajo de los 130

μg/m3N establecidos.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 14 de 132**

**Figura 3. Concentración promedio 24 horas de MP10, EMRP Rancagua I**

La concentración promedio anual de MP10 es superada en todo el período analizado, siendo

el año 2015 aquel que posee el mayor porcentaje de excedencia, con un 61%.

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

**Página 15 de 132**

80

70

60

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

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

se registraron un total de 10 días de alerta y 1 día de preemergencia en la estación Rancagua

I en la secuencia temporal analizada, siendo el año 2015 el que concentra las peores

condiciones, como se muestra en la Tabla 5.

<!-- INICIO TABLA 5. -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- I en la secuencia temporal analizada, siendo el año 2015 el que concentra las peores condiciones, como se muestra en la Tabla 5. -->

**Tabla 5.: Registro de días declarados en alerta, preemergencia y emergencia****

| Año | Días de alerta | Días de<br>preemergencia | Días de emergencia |
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

**para MP10 en la EMRP Rancagua I**

|Año|Días de alerta|Días de<br>preemergencia|Días de emergencia|
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

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 16 de 132**

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

La concentración promedio anual de MP2,5 que establece el D.S. 12/2011 MMA es superada

en todo el período analizado, siendo el año 2014 el que cuenta con el mayor porcentaje de

excedencia, con un 40%.

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

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 17 de 132**

|Año|Porcentaje de<br>datos disponibles<br>(%)|Concentración<br>Promedio Anual<br>(μg/m3)|Límite normativo<br>D.S. 12/2011 MMA<br>(μg/m3)|Porcentaje de<br>excedencia de la<br>norma (%)|
|---|---|---|---|---|
|2021|98%|26,0||30%|

Con respecto a las concentraciones de MP2,5 como promedio trianual, existe superación

normativa en los seis periodos analizados, siendo el periodo de 2014 - 2016 el que presenta

la mayor concentración con 25,4 μg/m [3] .

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

con preemergencia ambiental por MP2,5, siendo el año 2014 el que exhibe un mayor número

de días en condiciones de superación, tal como muestra la Tabla 7:

**Tabla 7. Registro de días declarados en alerta, preemergencia y emergencia**

**para MP2,5 en la EMRP Rancagua I**

|Año|Días de alerta|Días de<br>preemergencia|Días de emergencia|
|---|---|---|---|
|2014|16|3|0|
|2015|7|0|0|
|2016|10|2|0|
|2017|3|0|0|
|2018|4|1|0|

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 18 de 132**

|Año|Días de alerta|Días de<br>preemergencia|Días de emergencia|
|---|---|---|---|
|2019|7|1|0|
|2020|5|1|0|
|2021|14|1|0|

El D.S. 104/2019 MMA establece la norma primaria de calidad de aire para dióxido de azufre

(SO 2 ), regulando la concentración promedio anual, diaria y horaria.

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

superación normativa en los seis periodos analizados, presentando su mayor concentración

el periodo de 2014 - 2016 con 7,4 ppbv, como se observa en la Figura 7.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 19 de 132**

**Figura 7. Concentración promedio trianual horaria de SO** **2** **, EMRP Rancagua I**

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

Estación Rancagua I, de donde se observa que durante todos los periodos la concentración

no excede la normativa vigente de 57 ppbv, presentando una tendencia decreciente.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 20 de 132**

**Figura 8. Concentración promedio trianual 24 horas de SO** **2** **, EMRP Rancagua I**

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

normativa en los seis periodos analizados, siendo los periodos de 2016 - 2018 y 2017 - 2019

los que presentan la mayor concentración con 2,7 ppbv.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 21 de 132**

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

se registraron un total de 6 días de alerta y 8 días de preemergencia en la estación Rancagua

I en la secuencia temporal analizada, siendo el año 2015 el que concentra la mayor cantidad

de días en dichas condiciones, como se muestra en la Tabla 11.

<!-- INICIO TABLA 11. -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- I en la secuencia temporal analizada, siendo el año 2015 el que concentra la mayor cantidad de días en dichas condiciones, como se muestra en la Tabla 11. -->

**Tabla 11.: Registro de días declarados en alerta, preemergencia y emergencia****

| Año | Días de alerta | Días de<br>preemergencia | Días de emergencia |
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

|Año|Días de alerta|Días de<br>preemergencia|Días de emergencia|
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

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 22 de 132**

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

En la Figura 10 se presenta la concentración máxima horaria como promedio trianual de CO

de la Estación Rancagua I, donde se observa que durante todos los periodos la

concentración no excede la normativa vigente de 26 ppmv.

**Figura 10. Concentración promedio trianual horaria de CO, EMRP Rancagua I**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 23 de 132**

El percentil 99 de los máximos diarios de concentración de 8 horas para CO que establece

el D.S. 115/2002 MINSEGEPRES no es superada en todo el período analizado, siendo el año

2018 el que cuenta con la mayor concentración, con 4,2 ppmv.

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

La concentración máxima de 8 horas como promedio trianual para CO, no muestra

superación normativa en los seis periodos analizados, siendo los periodos de 2016 - 2018 y

2017 - 2019 los que presentan la mayor concentración con 3,8 ppmv, como se puede

observar en la Figura 11.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 24 de 132**

**Figura 11. Concentración promedio trianual 8 horas de CO, EMRP Rancagua I**

En relación con los días de alerta, preemergencia y/o emergencia en los años analizados

para el CO, no se registró ninguna de las condiciones de superación en la estación Rancagua

I.

**4** **Justificación de los modelos utilizados en el estudio**

El Servicio de Evaluación Ambiental en la “Guía para el Uso de Modelos de Calidad del Aire

en el SEIA” (2012) hace una serie de recomendaciones para la modelación de contaminantes

primarios [1] y secundarios en el aire. En la actualidad, esta guía es el único documento

existente como parámetro para la modelación de calidad del aire y tiene como objetivo

uniformar los criterios, exigencias técnicas y antecedentes para la evaluación de los impactos

asociados a este componente de proyectos que ingresen al Servicio de Evaluación

Ambiental. Dentro de las recomendaciones de la guía está el uso del modelo de dispersión

CALPUFF y sugiere a utilizar el modelo meteorológico WRF, los cuales fueron utilizados en

la modelación de las partículas del proyecto.

A continuación, se presenta la justificación de los modelos utilizados en el proyecto para

ejecución de la modelación de dispersión y concentración de emisiones de partículas en el

aire.

**4.1** **Uso del modelo CALPUFF**

La modelación de dispersión atmosférica de partículas provenientes del proyecto se realizó

con un modelo tipo “Puff”, específicamente el modelo CALPUFF. Tal como lo define la guía,

los modelos tipo “puff” son una combinación entre los modelos Gaussianos y los modelos

Lagrangeanos, en el sentido de que esencialmente calculan la dispersión de contaminantes

provenientes de una emisión instantánea, llamada “puff”, a lo largo de una trayectoria. Su

aproximación matemática consiste en estimar la dispersión en forma Gaussiana en cada

punto de una trayectoria; es decir, los modelos tipo “puff” sólo requieren una trayectoria

por “puff”, lo que hace su cálculo mucho más rápido. En el caso de emisiones continuas, se

1 Los contaminantes primarios son los producidos directamente por la actividad humana o la
naturaleza a la atmósfera, dentro de los cuales caben las emisiones odorantes.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 25 de 132**

simulan las trayectorias y la dispersión Gaussiana de muchos “puffs”, como es en el caso de

las emisiones de partículas generadas por el proyecto. Al respecto, el modelo tipo “puff”

recomendado por la Guía es el modelo **CALPUFF** .

Así mismo, es un modelo completo que incorpora herramientas para procesar datos

meteorológicos y geofísicos, modelos de dispersión y post procesamiento. Dicho modelo es

recomendado por la Agencia de Protección Ambiental de los Estados Unidos (EPA) para

modelar transporte a larga distancia de contaminantes.

CALPUFF se compone de tres módulos:

 CALMET: Es un modelo meteorológico que desarrolla campos horarios de viento y

temperatura en una grilla de tres dimensiones. También asocia campos en dos

dimensiones de altura y usos de suelo. **Este modelo fue reemplazado por el**

**WRF, tal como lo recomienda la guía antes citada.**

 CALPUFF: Es un modelo de transporte y dispersión de partículas emitidas desde

fuentes modeladas, simulando procesos de dispersión y transformación. CALPUFF

utiliza los datos generados por CALMET. Los archivos de salida de CALPUFF

contienen las concentraciones horarias o deposición por hora de flujos evaluados en

receptores seleccionados.

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

g exp

~~[~~ [−d] 2σ x [2][a]

∑exp ~~[~~ [−(H] [e] 2σ [+ 2nh)] z [2] [2]

2 2

[−d] 2σ x [2][a] [] exp] ~~[[]~~ [−d] 2σ y [2][c]

2

∞

n=−∞

[+ 2nh)] [2]

2σ z [2] ]

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 26 de 132**

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

consistencia con las recomendaciones del SEA para la modelación de partículas en sus guías,

se consideró utilizar el modelo CALPUFF para simular la dispersión y concentración de las

emisiones de partículas generadas por la futura operación del proyecto.

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
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 27 de 132**

**5** **Metodología**

**5.1** **Modelación de partículas**

La modelación de partículas depende en gran parte de las tasas de emisión. Estos son

acoplados a un modelo meteorológico, el que en sí mismo simula las condiciones

meteorológicas para la zona de estudio con una resolución temporal de 1 hora; con estos

factores como variable de entrada al modelo, es simulada la dispersión de las partículas en

un modelo, que determinará la trayectoria de las partículas dentro del área de estudio.

**5.1.1** **Modelación meteorológica**

Para la modelación meteorológica, se utilizó un modelo WRF, construido con datos del año

2021 y resolución de 1 km, de extensión 57 km x 57 km. El modelo WRF es capaz de simular

el comportamiento meteorológico, a través de datos meteorológicos para el año de estudio,

el que posteriormente es interpolado dentro del área de estudio del modelo de acuerdo con

la topografía del lugar. En la Tabla 14 se resumen las características del modelo.

**Tabla 14. Características del modelo**

|Año de modelación|Col2|2021|
|---|---|---|
|**Periodo de Modelación**|**Periodo de Modelación**|1 año calendario|
|**Resolución temporal**|**Resolución temporal**|1 hora|
|**Resolución espacial**|**Resolución espacial**|1 km|
|**Coordenadas del centroide**|**Latitud**|-34,19°|
|**Coordenadas del centroide**|**Longitud**|-70,73°|
|**DATUM**|**DATUM**|NWS - 84|
|**Coordenadas del modelo**|**Coordenadas del modelo**|LCC|
|**Dominio de modelación**|**X **|57|
|**Dominio de modelación**|**Y **|57|
|**Dominio de modelación**|**Z **|10|

**5.1.2** **Modelación de dispersión de contaminantes**

El modelo CALPUFF permite la simulación de la dispersión de contaminantes bajo dos

modalidades:

 **Modelación de la grilla de modelación** . La grilla de modelación viene seteada

del modelo meteorológico, acotando la simulación en la zona circundante más

próxima al proyecto, incluyendo las zonas pobladas importantes de evaluar. Dicha

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

grilla de modelación tiene una resolución espacial de 1 km.

**Página 28 de 132**

Este es el método más usual para la interpolación de las concentraciones de los

puntos de grilla (1 km), interpolando entre cada punto la concentración, hasta

obtener la pluma de dispersión. Por defecto la modelación de los puntos de grilla

entrega el valor de la concentración como el promedio en la primera capa de

modelación, la que ocurre entre los 0 y 20 m sobre el nivel del suelo.

En virtud de la resolución espacial del modelo y de la altura de la primera capa de

modelación, y al tratarse de áreas de emisión que se generan a altura del suelo o a

baja altura [2], muchas veces la obtención de la pluma de dispersión se genera con

valores sub dimensionados, por lo tanto, en ocasiones es necesario realizar una sub

grilla de modelación a través de la modelación de puntos discretos, aumentando la

densidad de puntos de modelación y mejorando la evaluación de la concentración

simulada dentro del espacio circundante. De este modo, se generó una subgrilla de

6 km x 6 km desde el centroide del proyecto.

 **Modelación de puntos discretos.** Inicialmente se consideraron 20 puntos

receptores discretos cercanos al proyecto, estos comprenden desde el R18 al R37,

luego a solicitud de la autoridad se consideraron puntos discretos, tanto dentro del

proyecto, estos corresponden a aquellos del R1 al R17; cabe destacar que de los

receptores R1 al R8, aparte de ser receptores son fuentes de emisión, ya que son

representativos de la situación base del proyecto, sobre la cual se simula en el

modelamiento el uso de calefacción a leña durante el invierno. También se discretizó

la EMRP Rancagua I, correspondiendo al R38.

**Tabla 15. Descripción de los puntos receptores**

2 Como es el caso del tránsito y de las obras asociadas al movimiento de tierra.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**Página 29 de 132**

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

|Receptor|Coordenada UTM WGS 84 HUSO 19 S|Col3|Descripción|Distancia<br>al centro<br>del<br>proyecto<br>(m)|
|---|---|---|---|---|
|**Receptor**|**Este (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|
|R1|345.981|6.217.069|Vivienda dentro del proyecto|26|
|R2|345.922|6.216.924|Vivienda dentro del proyecto|131|
|R3|346.011|6.216.981|Vivienda dentro del proyecto|81|
|R4|345.983|6.216.874|Vivienda dentro del proyecto|174|
|R5|346.058|6.216.870|Vivienda dentro del proyecto|201|
|R6|346.108|6.216.839|Vivienda dentro del proyecto|253|
|R7|346.022|6.216.768|Vivienda dentro del proyecto|286|
|R8|345.960|6.216.836|Vivienda dentro del proyecto|212|
|R9|346.057|6.217.027|Vivienda dentro del proyecto|94|
|R10|346.196|6.216.987|Vivienda dentro del proyecto|239|
|R11|346.150|6.216.875|Vivienda dentro del proyecto|253|
|R12|346.016|6.217.157|Vivienda dentro del proyecto|120|
|R13|345.850|6.217.035|Vivienda dentro del proyecto|116|
|R14|345.750|6.217.200|Vivienda dentro del proyecto|263|
|R15|345.852|6.217.180|Vivienda dentro del proyecto|174|
|R16|345.932|6.217.262|Vivienda dentro del proyecto|217|
|R17|345.805|6.217.116|Vivienda dentro del proyecto|174|
|R18|345.721|6.216.943|Vivienda|266|
|R19|345.617|6.217.389|Vivienda|487|
|R20|345.806|6.217.513|Vivienda|491|
|R21|345.472|6.216.974|Vivienda|499|
|R22|346.077|6.216.507|Vivienda|552|
|R23|346.591|6.217.215|Vivienda|648|
|R24|345.344|6.217.342|Vivienda|687|
|R25|346.428|6.217.596|Vivienda|717|
|R26|345.393|6.217.607|Vivienda|800|
|R27|346.070|6.216.198|Vivienda|856|
|R28|345.850|6.217.995|Vivienda|954|
|R29|345.010|6.217.262|Vivienda|979|
|R30|346.513|6.216.236|Vivienda|980|
|R31|346.993|6.217.180|Liceo Machalí|1.036|
|R32|345.035|6.217.591|Vivienda|1.077|
|R33|347.841|6.216.377|Plaza Machalí|1.992|
|R34|344.268|6.217.322|Colegio San Alberto|1.719|
|R35|343.600|6.217.039|Colegio San Ignacio|2.365|
|R36|342.515|6.217.146|Colegio Manuel Rodríguez|3.451|

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**Página 30 de 132**

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

|Receptor|Coordenada UTM WGS 84 HUSO 19 S|Col3|Descripción|Distancia<br>al centro<br>del<br>proyecto<br>(m)|
|---|---|---|---|---|
|**Receptor**|**Este (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|
|R37|339.886|6.217.497|Liceo Bicentenario Oscar Castro Zúñiga|6.096|
|R38|342.015|6.218.523|Estación Rancagua I|4.216|

Nota: La distancia de los receptores se midió al centro del proyecto, en la coordenada

UTM WGS 84 HUSO 19 S x: 345.965 m e y: 6.217.048 m.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 31 de 132**

**Figura 12. Receptores discretos dentro del proyecto**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 32 de 132**

**Figura 13. Receptores discretos fuera del polígono del proyecto**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**5.1.3** **Criterios para la modelación de partículas**

**Página 33 de 132**

Como escenario de modelación se consideró el año de máxima emisión, como se indica en

la tabla 88 de la actualización del informe de estimación de emisiones, lo que ocurre durante

el año 4 del proyecto. Durante este año se presenta la mayor emisión de MP debido a que

entra en operación la totalidad de las unidades habitacionales del proyecto, lo que conlleva

un mayor tránsito por caminos internos pavimentados, efectuado por los habitantes de las

353 viviendas entregadas, aumentando así, la emisión de MP. Los detalles de la estimación

de emisiones se presentan en el informe de Estimación de Emisiones Atmosféricas. Para la

fase de operación se incorporó los polígonos donde se generan el tránsito en rutas

pavimentadas internas, el área representante de la calefacción domiciliaria y el tránsito en

rutas pavimentadas externo más cercano al proyecto.

Adicionalmente, se modelaron las emisiones de gases precursores de MP10 y MP2,5 en el

aire a través del módulo MESOPUFF II.

**De acuerdo con la metodología aplicable, se realizaron polígonos representativos de cada**
**unidad para la simulación de las áreas de emisiones de partículas, las que fueron modeladas**
**como fuentes de emisión discontinuas, es decir, dentro del ciclo diurno, simulando dicho**
**periodo como el de uso de los vehículos por parte de los residentes. Además, se consideró**
**para la fase de operación un ciclo estacional para la calefacción domiciliaria, donde la**
**generación de dichas emisiones se situó en las estaciones de otoño e invierno, durante las**

**24 horas del día. Las coordenadas de los polígonos utilizados se encuentran en**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**la Tabla 16, así como también, en la**

**Página 34 de 132**

**Figura 14. Polígonos de Modelación representativos de cada unidad modelada,**

**vista general**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

Figura 15 se presenta la ubicación espacial de éstos.

**Página 35 de 132**

**Tabla 16. Coordenadas de modelación de las fuentes areales Fase de Operación**

|Actividad para<br>modelar|Unidad del<br>proyecto|Área (m2)|Coordenada UTM, HUSO 19 S,<br>DATUM WGS 84|Col5|
|---|---|---|---|---|
|**Actividad para**<br>**modelar**|**Unidad del**<br>**proyecto**|**Área (m2) **|**Este (m)**|**Norte (m)**|
|Ruta Pavimentada<br>Interna|P1|209|345.930|6.216.976|
|Ruta Pavimentada<br>Interna|P1|209|345.933|6.216.978|
|Ruta Pavimentada<br>Interna|P1|209|345.967|6.216.927|
|Ruta Pavimentada<br>Interna|P1|209|345.969|6.216.929|
|Ruta Pavimentada<br>Interna|P2|103|345.965|6.216.930|
|Ruta Pavimentada<br>Interna|P2|103|345.967|6.216.927|

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 36 de 132**

|Actividad para<br>modelar|Unidad del<br>proyecto|Área (m2)|Coordenada UTM, HUSO 19 S,<br>DATUM WGS 84|Col5|
|---|---|---|---|---|
|**Actividad para**<br>**modelar**|**Unidad del**<br>**proyecto**|**Área (m2) **|**Este (m)**|**Norte (m)**|
|**Actividad para**<br>**modelar**|**Unidad del**<br>**proyecto**|**Área (m2) **|345.940|6.216.908|
|**Actividad para**<br>**modelar**|**Unidad del**<br>**proyecto**|**Área (m2) **|345.944|6.216.907|
|**Actividad para**<br>**modelar**|P3|29|345.94|6.216.908|
|**Actividad para**<br>**modelar**|P3|29|345.944|6.216.907|
|**Actividad para**<br>**modelar**|P3|29|345.942|6.216.898|
|**Actividad para**<br>**modelar**|P3|29|345.945|6.216.900|
|**Actividad para**<br>**modelar**|P4|454|345.942|6.216.897|
|**Actividad para**<br>**modelar**|P4|454|345.945|6.216.900|
|**Actividad para**<br>**modelar**|P4|454|346.021|6.216.795|
|**Actividad para**<br>**modelar**|P4|454|346.023|6.216.798|
|**Actividad para**<br>**modelar**|P5|25|346.023|6.216.798|
|**Actividad para**<br>**modelar**|P5|25|346.029|6.216.799|
|**Actividad para**<br>**modelar**|P5|25|346.021|6.216.795|
|**Actividad para**<br>**modelar**|P5|25|346.031|6.216.796|
|**Actividad para**<br>**modelar**|P6|268|346.029|6.216.799|
|**Actividad para**<br>**modelar**|P6|268|346.087|6.216.847|
|**Actividad para**<br>**modelar**|P6|268|346.031|6.216.796|
|**Actividad para**<br>**modelar**|P6|268|346.089|6.216.844|
|**Actividad para**<br>**modelar**|P7|862|345.871|6.216.933|
|**Actividad para**<br>**modelar**|P7|862|346.053|6.217.081|
|**Actividad para**<br>**modelar**|P7|862|345.873|6.216.930|
|**Actividad para**<br>**modelar**|P7|862|346.055|6.217.079|
|**Actividad para**<br>**modelar**|P8|243|346.052|6.217.076|
|**Actividad para**<br>**modelar**|P8|243|346.055|6.217.079|
|**Actividad para**<br>**modelar**|P8|243|346.090|6.217.027|
|**Actividad para**<br>**modelar**|P8|243|346.093|6.217.029|
|**Actividad para**<br>**modelar**|P9|122|346.091|6.217.032|
|**Actividad para**<br>**modelar**|P9|122|346.117|6.217.052|
|**Actividad para**<br>**modelar**|P9|122|346.094|6.217.029|
|**Actividad para**<br>**modelar**|P9|122|346.119|6.217.049|
|**Actividad para**<br>**modelar**|P10|29|346.117|6.217.053|
|**Actividad para**<br>**modelar**|P10|29|346.128|6.217.051|
|**Actividad para**<br>**modelar**|P10|29|346.119|6.217.049|
|**Actividad para**<br>**modelar**|P10|29|346.125|6.217.048|

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 37 de 132**

|Actividad para<br>modelar|Unidad del<br>proyecto|Área (m2)|Coordenada UTM, HUSO 19 S,<br>DATUM WGS 84|Col5|
|---|---|---|---|---|
|**Actividad para**<br>**modelar**|**Unidad del**<br>**proyecto**|**Área (m2) **|**Este (m)**|**Norte (m)**|
|**Actividad para**<br>**modelar**|P11|457|346.125|6.217.048|
|**Actividad para**<br>**modelar**|P11|457|346.128|6.217.050|
|**Actividad para**<br>**modelar**|P11|457|346.202|6.216.948|
|**Actividad para**<br>**modelar**|P11|457|346.205|6.216.950|
|**Actividad para**<br>**modelar**|P12|25|346.202|6.216.948|
|**Actividad para**<br>**modelar**|P12|25|346.205|6.216.949|
|**Actividad para**<br>**modelar**|P12|25|346.200|6.216.942|
|**Actividad para**<br>**modelar**|P12|25|346.202|6.216.939|
|**Actividad para**<br>**modelar**|P13|300|346.200|6.216.942|
|**Actividad para**<br>**modelar**|P13|300|346.202|6.216.939|
|**Actividad para**<br>**modelar**|P13|300|346.137|6.216.890|
|**Actividad para**<br>**modelar**|P13|300|346.140|6.216.887|
|**Actividad para**<br>**modelar**|P14|266|345.862|6.216.942|
|**Actividad para**<br>**modelar**|P14|266|345.923|6.216.992|
|**Actividad para**<br>**modelar**|P14|266|345.864|6.216.940|
|**Actividad para**<br>**modelar**|P14|266|345.925|6.216.990|
|**Actividad para**<br>**modelar**|P15|114|345.900|6.217.016|
|**Actividad para**<br>**modelar**|P15|114|345.903|6.217.019|
|**Actividad para**<br>**modelar**|P15|114|345.921|6.216.990|
|**Actividad para**<br>**modelar**|P15|114|345.923|6.216.992|
|**Actividad para**<br>**modelar**|P16|72|345.888|6.217.033|
|**Actividad para**<br>**modelar**|P16|72|345.891|6.217.035|
|**Actividad para**<br>**modelar**|P16|72|345.900|6.217.017|
|**Actividad para**<br>**modelar**|P16|72|345.903|6.217.019|
|**Actividad para**<br>**modelar**|P17|73|345.883|6.217.053|
|**Actividad para**<br>**modelar**|P17|73|345.887|6.217.054|
|**Actividad para**<br>**modelar**|P17|73|345.889|6.217.033|
|**Actividad para**<br>**modelar**|P17|73|345.891|6.217.035|
|**Actividad para**<br>**modelar**|P18|63|345.877|6.217.069|
|**Actividad para**<br>**modelar**|P18|63|345.880|6.217.070|
|**Actividad para**<br>**modelar**|P18|63|345.883|6.217.053|
|**Actividad para**<br>**modelar**|P18|63|345.886|6.217.054|
|**Actividad para**<br>**modelar**|P19|709|345.753|6.217.224|
|**Actividad para**<br>**modelar**|P19|709|345.755|6.217.226|

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 38 de 132**

|Actividad para<br>modelar|Unidad del<br>proyecto|Área (m2)|Coordenada UTM, HUSO 19 S,<br>DATUM WGS 84|Col5|
|---|---|---|---|---|
|**Actividad para**<br>**modelar**|**Unidad del**<br>**proyecto**|**Área (m2) **|**Este (m)**|**Norte (m)**|
|**Actividad para**<br>**modelar**|**Unidad del**<br>**proyecto**|**Área (m2) **|345.877|6.217.069|
|**Actividad para**<br>**modelar**|**Unidad del**<br>**proyecto**|**Área (m2) **|345.880|6.217.070|
|**Actividad para**<br>**modelar**|P20|436|345.755|6.217.226|
|**Actividad para**<br>**modelar**|P20|436|345.840|6.217.310|
|**Actividad para**<br>**modelar**|P20|436|345.758|6.217.223|
|**Actividad para**<br>**modelar**|P20|436|345.842|6.217.307|
|**Actividad para**<br>**modelar**|P21|257|345.840|6.217.310|
|**Actividad para**<br>**modelar**|P21|257|345.843|6.217.307|
|**Actividad para**<br>**modelar**|P21|257|345.893|6.217.361|
|**Actividad para**<br>**modelar**|P21|257|345.895|6.217.359|
|Ruta Pavimentada<br>Externa|P22|40|345.861|6.216.927|
|Ruta Pavimentada<br>Externa|P22|40|345.871|6.216.933|
|Ruta Pavimentada<br>Externa|P22|40|345.863|6.216.925|
|Ruta Pavimentada<br>Externa|P22|40|345.873|6.216.930|
|Ruta Pavimentada<br>Externa|P23|1.092|345.861|6.216.927|
|Ruta Pavimentada<br>Externa|P23|1.092|345.863|6.216.925|
|Ruta Pavimentada<br>Externa|P23|1.092|345.625|6.216.748|
|Ruta Pavimentada<br>Externa|P23|1.092|345.627|6.216.745|
|Ruta Pavimentada<br>Externa|P24|4.038|344.965|6.217.605|
|Ruta Pavimentada<br>Externa|P24|4.038|344.962|6.217.603|
|Ruta Pavimentada<br>Externa|P24|4.038|345.625|6.216.743|
|Ruta Pavimentada<br>Externa|P24|4.038|345.627|6.216.745|
|Ruta Pavimentada<br>Externa|P25|7.471|344.964|6.217.600|
|Ruta Pavimentada<br>Externa|P25|7.471|344.962|6.217.603|
|Ruta Pavimentada<br>Externa|P25|7.471|343.737|6.217.010|
|Ruta Pavimentada<br>Externa|P25|7.471|343.731|6.217.014|
|Ruta Pavimentada<br>Externa|P26|499|343.737|6.217.010|
|Ruta Pavimentada<br>Externa|P26|499|343.731|6.217.014|
|Ruta Pavimentada<br>Externa|P26|499|343.641|6.216.989|
|Ruta Pavimentada<br>Externa|P26|499|343.641|6.216.994|
|Ruta Pavimentada<br>Externa|P27|3.239|343.641|6.216.989|
|Ruta Pavimentada<br>Externa|P27|3.239|343.641|6.216.994|
|Ruta Pavimentada<br>Externa|P27|3.239|343.089|6.217.069|
|Ruta Pavimentada<br>Externa|P27|3.239|343.090|6.217.075|
|Ruta Pavimentada<br>Externa|P28|8.068|343.089|6.217.069|
|Ruta Pavimentada<br>Externa|P28|8.068|343.090|6.217.075|

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 39 de 132**

|Actividad para<br>modelar|Unidad del<br>proyecto|Área (m2)|Coordenada UTM, HUSO 19 S,<br>DATUM WGS 84|Col5|
|---|---|---|---|---|
|**Actividad para**<br>**modelar**|**Unidad del**<br>**proyecto**|**Área (m2) **|**Este (m)**|**Norte (m)**|
|**Actividad para**<br>**modelar**|**Unidad del**<br>**proyecto**|**Área (m2) **|341.971|6.217.179|
|**Actividad para**<br>**modelar**|**Unidad del**<br>**proyecto**|**Área (m2) **|341.973|6.217.188|
|**Actividad para**<br>**modelar**|P29|11.390|341.971|6.217.179|
|**Actividad para**<br>**modelar**|P29|11.390|341.973|6.217.188|
|**Actividad para**<br>**modelar**|P29|11.390|340.897|6.217.387|
|**Actividad para**<br>**modelar**|P29|11.390|340.898|6.217.397|
|**Actividad para**<br>**modelar**|P30|9.248|340.897|6.217.387|
|**Actividad para**<br>**modelar**|P30|9.248|340.898|6.217.397|
|**Actividad para**<br>**modelar**|P30|9.248|339.609|6.217.583|
|**Actividad para**<br>**modelar**|P30|9.248|339.611|6.217.589|
|Calefacción|P31|3.794|346.009|6.216.972|
|Calefacción|P31|3.794|346.025|6.216.982|
|Calefacción|P31|3.794|346.116|6.216.828|
|Calefacción|P31|3.794|346.132|6.216.842|
|Calefacción|P32|2.571|346.009|6.216.765|
|Calefacción|P32|2.571|346.103|6.216.843|
|Calefacción|P32|2.571|346.021|6.216.750|
|Calefacción|P32|2.571|346.115|6.216.827|
|Calefacción|P33|3.106|346.001|6.216.836|
|Calefacción|P33|3.106|346.056|6.216.880|
|Calefacción|P33|3.106|346.029|6.216.802|
|Calefacción|P33|3.106|346.082|6.216.846|
|Calefacción|P34|3.230|345.966|6.216.880|
|Calefacción|P34|3.230|346.026|6.216.926|
|Calefacción|P34|3.230|345.995|6.216.846|
|Calefacción|P34|3.230|346.050|6.216.891|
|Calefacción|P35|3.015|345.916|6.216.885|
|Calefacción|P35|3.015|345.934|6.216.898|
|Calefacción|P35|3.015|346.002|6.216.774|
|Calefacción|P35|3.015|346.018|6.216.785|
|Calefacción|P36|2.401|345.951|6.216.977|
|Calefacción|P36|2.401|345.999|6.217.015|
|Calefacción|P36|2.401|345.975|6.216.947|
|Calefacción|P36|2.401|346.023|6.216.984|
|Calefacción|P37|2.655|345.884|6.216.925|
|Calefacción|P37|2.655|345.932|6.216.962|
|Calefacción|P37|2.655|345.912|6.216.890|
|Calefacción|P37|2.655|345.958|6.216.928|

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 40 de 132**

|Actividad para<br>modelar|Unidad del<br>proyecto|Área (m2)|Coordenada UTM, HUSO 19 S,<br>DATUM WGS 84|Col5|
|---|---|---|---|---|
|**Actividad para**<br>**modelar**|**Unidad del**<br>**proyecto**|**Área (m2) **|**Este (m)**|**Norte (m)**|
|**Actividad para**<br>**modelar**|P38|2.921|345.917|6.217.022|
|**Actividad para**<br>**modelar**|P38|2.921|346.059|6.217.140|
|**Actividad para**<br>**modelar**|P38|2.921|345.927|6.217.011|
|**Actividad para**<br>**modelar**|P38|2.921|346.070|6.217.128|

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 41 de 132**

**Figura 14. Polígonos de Modelación representativos de cada unidad modelada, vista general**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 42 de 132**

**Figura 15. Polígonos de modelación representativos de cada unidad modelada, ampliado**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 43 de 132**

## 6 Resultados

**6.1** **Modelamiento meteorológico**

En la Figura 16, se observa la topografía utilizada por el modelo WRF para realizar la

modelación meteorológica. En esta se observa que el terreno corresponde a una zona

cordillerana, con alturas entre los 500 m.s.n.m y los 2250 m.s.n.m.

El proyecto se encuentra particularmente en la cota 500 m.s.n.m.

**Figura 16. Elevación del terreno en el área de la modelación meteorológica**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 44 de 132**

**6.1.2** **Caracterización de la velocidad y dirección de los vientos Anual y**

**Estacional.**

En la Figura 17 se presenta la rosa de vientos anual, construida en base a los datos

generados con el modelo WRF con información del año 2021 para la comuna de Machalí y

sus alrededores.

**Figura 17. Rosa de los vientos anual, WRF 2021.**

De la figura anterior, se observa que los vientos simulados tienen su origen desde la

componente Sursuroeste (SSO) principalmente, mientras que en menor magnitud la

componente Suroeste (SO) y Sur (S). En efecto, el origen de los vientos con mayor

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 45 de 132**

frecuencia es en la componente Sursuroeste (SSO) con un 25,0% del origen de los vientos

totales. Estos vientos se caracterizan por estar concentrados principalmente en el rango de

2,1 - 3,6 m/s. La segunda dirección prioritaria es la Suroeste (SO), con un 16,7% del origen

de vientos locales.

En la Tabla 17 se muestra la frecuencia de vientos por componente de origen, de los datos

simulados por el modelo WRF para el año 2021.

**Tabla 17. Frecuencia de la dirección de los vientos anual, WRF 2021.**

|Componente|Calmas|0,5-2,1|2,1-3,6|3,6-5,7|5,7-8,8|8,8-11,0|>11,0|Porcentaje|
|---|---|---|---|---|---|---|---|---|
|N|67|79|29|29|20|0|2|2,6%|
|NNE|77|115|66|44|33|4|2|3,9%|
|NE|91|155|126|127|48|7|3|6,4%|
|ENE|55|72|71|145|52|0|2|4,5%|
|E|25|32|20|43|19|3|2|1,6%|
|ESE|38|10|8|6|1|0|0|0,7%|
|SE|42|27|8|5|1|0|0|0,9%|
|SSE|72|121|141|156|1|0|0|5,6%|
|S|124|442|466|220|7|0|0|14,4%|
|SSO|136|592|906|515|37|0|0|25,0%|
|SO|92|362|469|471|73|0|0|16,7%|
|OSO|40|144|239|371|191|1|0|11,3%|
|O|41|33|52|158|30|1|0|3,6%|
|ONO|32|30|6|4|2|0|0|0,8%|
|NO|37|20|2|0|0|0|2|0,7%|
|NNO|48|25|5|16|14|0|4|1,3%|

Nota: Las filas sombreadas en azul son las componentes que registran máximas

frecuencias.

En el gráfico de frecuencia de velocidad del viento de la Figura 18, se observa que el modelo

simuló una mayor tendencia de vientos entre los 2,1 - 3,6 m/s, representando estos un

29,8% del total de velocidades simuladas. Luego vientos con velocidades entre los rangos

0,5 - 2,1 m/s y 3,6 - 5,7 m/s siguen, con frecuencias de 25,8% y 26,4% respectivamente.

Por el contrario, las categorías extremas, es decir, los vientos mayores a 11 m/s, entre el

rango 8,8 - 11 m/s, entre 5,7 - 8,8 m/s y calmas (menores a 0,5 m/s) ocurren en menor

proporción, representando solo el 0,2%, 0,2%, 6,0% y 11,6% respectivamente de los

vientos totales.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 46 de 132**

**Figura 18. Frecuencia de los vientos, año 2021.**

**6.1.2.1** **Dirección y velocidad de vientos predominantes en verano.**

Como se observa en la siguiente figura, la simulación meteorológica muestra que en los

meses de verano del 2021 los vientos tienen un origen mayoritario en la componente

Suroeste (SO), Sursuroeste (SSO), Sur (S), y Oeste suroeste (OSO), las que en conjunto

constituyen el 75,9% del total de las direcciones de origen de los vientos. El rango de

velocidades que prevalece en estas direcciones varía entre los 3,6 - 5,7 m/s. El resto de los

vientos tienen frecuencias similares inferiores en distintas componentes.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 47 de 132**

**Figura 19. Rosa de los vientos verano, WRF 2021.**

En la siguiente tabla, se presenta la frecuencia de vientos por cada componente de origen,

de donde se observa la frecuencia de los vientos simulados por el modelo WRF en la época

estival para la ciudad de Machalí y sus alrededores.

**Tabla 18. Frecuencia de los vientos verano, WRF.**

|Componente|Calmas|0,5-2,1|2,1-3,6|3,6-5,7|5,7-8,8|8,8-11,0|>11,0|Porcentaje|
|---|---|---|---|---|---|---|---|---|
|N|10|19|4|1|1|0|0|1,6%|
|NNE|10|27|2|1|1|0|0|1,9%|
|NE|20|32|17|3|0|0|0|3,3%|

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 48 de 132**

|Componente|Calmas|0,5-2,1|2,1-3,6|3,6-5,7|5,7-8,8|8,8-11,0|>11,0|Porcentaje|
|---|---|---|---|---|---|---|---|---|
|ENE|10|11|13|10|0|0|0|2,0%|
|E|8|11|0|1|0|0|0|0,9%|
|ESE|7|5|0|0|0|0|0|0,6%|
|SE|16|4|0|0|0|0|0|0,9%|
|SSE|31|39|37|55|0|0|0|7,5%|
|S|27|97|144|66|3|0|0|15,6%|
|SSO|21|137|171|135|14|0|0|22,1%|
|SO|20|93|126|218|52|0|0|23,6%|
|OSO|7|33|49|99|127|1|0|14,6%|
|O|6|9|10|24|12|0|0|2,8%|
|ONO|11|4|3|0|0|0|0|0,8%|
|NO|12|3|0|0|0|0|0|0,7%|
|NNO|14|6|0|1|1|0|0|1,0%|

Nota: Las filas sombreadas en azul son las componentes que registran máximas

frecuencias.

La Figura 20 muestra el gráfico de frecuencia de velocidad del viento en la estación de

verano para los siete rangos de velocidades evaluados. En ella es posible observar una alta

frecuencia de los vientos entre 3,6 - 5,7 m/s, 2,1 - 3,6 m/s y 0,5 - 2,1 m/s, los que

representan un 28,4%, 26,7% y 24,5% respectivamente de los vientos totales simulados.

En menor proporción se presentan vientos entre los 5,7 - 8,8 m/s y calmos (menores a 0,5

m/s), representando el 9,8%, y 10,6% respectivamente de los vientos totales. Por otra

parte, es posible apreciar que no se presentan velocidades superiores a 8,8 m/s.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 49 de 132**

**Figura 20. Frecuencia de los vientos en verano, año 2021.**

**6.1.2.2** **Dirección y velocidad de vientos predominantes en otoño.**

En la Figura 21, se presenta la rosa de los vientos para los meses de otoño en donde se

observa que estos tienen su origen mayormente en la componente Sursuroeste (SSO),

representando el 26,5% del total de las direcciones de los vientos en otoño, seguido por

vientos simulados en la componente Suroeste (SO) y Sur (S), con un 16,8% y 14,4%

respectivamente del total. Los vientos entre estas coordenadas representan en su conjunto

el 57,7% del total de los vientos simulados. El rango de velocidades que prevalece en estas

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 50 de 132**

direcciones varía entre los 2,1 - 3,6 m/s. El resto de las componentes, por su parte, se

presentan en menor frecuencia.

**Figura 21. Rosa de los vientos otoño, WRF 2021.**

En la Tabla 19, se ve la frecuencia del origen de los vientos en los meses de otoño simulada

por el modelo WRF.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 51 de 132**

**Tabla 19. Frecuencia de los vientos otoño, WRF.**

|Componente|Calmas|0,5-2,1|2,1-3,6|3,6-5,7|5,7-8,8|8,8-11,0|>11,0|Porcentaje|
|---|---|---|---|---|---|---|---|---|
|N|22|16|6|5|3|0|0|2,4%|
|NNE|32|32|19|10|5|0|0|4,4%|
|NE|31|52|31|33|5|1|0|6,9%|
|ENE|20|25|19|27|12|0|0|4,7%|
|E|9|8|3|4|3|1|0|1,3%|
|ESE|14|1|2|3|0|0|0|0,9%|
|SE|10|10|0|0|0|0|0|0,9%|
|SSE|19|33|21|52|1|0|0|5,7%|
|S|40|131|94|52|1|0|0|14,4%|
|SSO|53|168|258|102|5|0|0|26,5%|
|SO|36|118|140|73|3|0|0|16,8%|
|OSO|12|40|62|92|11|0|0|9,8%|
|O|12|7|14|27|1|0|0|2,8%|
|ONO|7|5|0|1|0|0|0|0,6%|
|NO|9|4|0|0|0|0|0|0,6%|
|NNO|14|5|1|4|5|0|0|1,3%|

Nota: Las filas sombreadas en azul son las componentes que registran máximas

frecuencias.

En la Figura 22, se presenta la frecuencia de los vientos para categoría de vientos simulados

en los meses de otoño, de donde se observa que los vientos de mayor frecuencia se

encuentran en las categorías 2,1 - 3,6 m/s, 0,5 - 2,1 m/s y 3,6 - 5,7 m/s representando un

30,3%, 29,7% y 22,0% respectivamente de los vientos totales simulados en esta estación.

Vientos calmos (menores a 0,5 m/s) le siguen con un 15,4% del total. Se observa además

que los vientos entre el rango 8,8 - 11 m/s y 5,7 - 8,8 m/s constituyen una baja frecuencia

con solo 0,2% y 2,5% respectivamente del total de datos medidos, mientras que vientos

intensos, superiores a 11 m/s no presentan mediciones.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 52 de 132**

**Figura 22. Frecuencia de los vientos en otoño, año 2021.**

**6.1.2.3** **Dirección y velocidad de vientos predominantes en invierno.**

En la Figura 23, se presenta la rosa de los vientos para el invierno simulada a través de

WRF. En ésta se observa que los vientos más frecuentes fueron modelados en la

componente Sursuroeste (SSO) representando el 24,2% del total de los vientos simulados

para la estación. La velocidad predominante en esta dirección varía entre el rango 2,1 - 3,6

m/s. A continuación, le siguen los vientos simulados en la componente Sur (S) y Noreste

(NE) con un 13,5% y 12,3% del total, respectivamente.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 53 de 132**

**Figura 23. Rosa de los vientos invierno, WRF 2021.**

En la Tabla 20, se muestra la frecuencia de los vientos simulados por el modelo WRF durante

los meses de invierno.

**Tabla 20. Frecuencia de los vientos invierno, WRF.**

|Componente|Calmas|0,5-2,1|2,1-3,6|3,6-5,7|5,7-8,8|8,8-11,0|>11,0|Porcentaje|
|---|---|---|---|---|---|---|---|---|
|N|21|29|16|14|11|0|1|4,2%|
|NNE|26|38|38|29|24|3|2|7,2%|
|NE|32|57|63|72|40|6|2|12,3%|
|ENE|20|24|30|85|33|0|1|8,7%|

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 54 de 132**

|Componente|Calmas|0,5-2,1|2,1-3,6|3,6-5,7|5,7-8,8|8,8-11,0|>11,0|Porcentaje|
|---|---|---|---|---|---|---|---|---|
|E|6|6|10|31|15|2|1|3,2%|
|ESE|12|3|5|1|0|0|0|1,0%|
|SE|12|4|4|1|1|0|0|1,0%|
|SSE|15|24|31|10|0|0|0|3,6%|
|S|39|115|99|46|0|0|0|13,5%|
|SSO|45|164|221|105|0|0|0|24,2%|
|SO|24|74|56|12|3|0|0|7,7%|
|OSO|16|37|53|34|0|0|0|6,3%|
|O|16|8|9|35|4|0|0|3,3%|
|ONO|8|15|2|1|2|0|0|1,3%|
|NO|11|8|1|0|0|0|0|0,9%|
|NNO|13|8|4|6|5|0|0|1,6%|

Nota: Las filas sombreadas en azul son las componentes que registran máximas

frecuencias.

En la Figura 24, se muestra la frecuencia de los vientos simulados para cada categoría de

velocidad por el modelo meteorológico, de donde se puede observar que para los rangos de

2,1 - 3,6 m/s, 0,5 - 2,1 m/s y 3,6 - 5,7 m/s se modeló las mayores frecuencias de vientos

con un 29,1%, 27,8% y 21,8% del total, seguidos por vientos calmos (menores a 0,5 m/s)

y en el rango de 5,7 - 8,8 m/s, con un 14,3% y 6,2% respectivamente del total de los datos

simulados. Respecto a las categorías extremas, los vientos superiores o iguales a 8,8 m/s

solo aportan el 0,8% de las velocidades totales para esta estación.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 55 de 132**

**Figura 24. Frecuencia de los vientos en invierno, año 2021.**

**6.1.2.4** **Dirección y velocidad de vientos predominantes en primavera.**

La simulación meteorológica presentada en la Figura 25, muestra que en los meses de

primavera los vientos tienen su origen principal en la componente Sursuroeste (SSO),

seguida de las componentes Suroeste (SO), Oeste suroeste (OSO) y Sur (S), constituyendo

en conjunto estas cuatro componentes el 74,4% del total de los orígenes de los vientos de

la estación. El rango de velocidades que prevalece en estas direcciones dominantes varía en

promedio en el rango de 2,1 - 5,7 m/s. De manera similar a las otras estaciones, el resto

de las componentes ejercen su influencia en menor frecuencia.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 56 de 132**

**Figura 25. Rosa de los vientos en primavera, WRF 2021.**

En la Tabla 21, se muestra la frecuencia de vientos por componente de origen, de donde se

observa la frecuencia de los vientos simulados por el modelo WRF para la estación de

primavera.

**Tabla 21. Frecuencia de los vientos en primavera, WRF.**

|Componente|Calmas|0,5-2,1|2,1-3,6|3,6-5,7|5,7-8,8|8,8-11,0|>11,0|Porcentaje|
|---|---|---|---|---|---|---|---|---|
|N|14|15|3|9|5|0|1|2,2%|
|NNE|9|18|7|4|3|1|0|1,9%|
|NE|8|14|15|19|3|0|1|2,7%|

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 57 de 132**

|Componente|Calmas|0,5-2,1|2,1-3,6|3,6-5,7|5,7-8,8|8,8-11,0|>11,0|Porcentaje|
|---|---|---|---|---|---|---|---|---|
|ENE|5|12|9|23|7|0|1|2,6%|
|E|2|7|7|7|1|0|1|1,1%|
|ESE|5|1|1|2|1|0|0|0,5%|
|SE|4|9|4|4|0|0|0|1,0%|
|SSE|7|25|52|39|0|0|0|5,6%|
|S|18|99|129|56|3|0|0|14,0%|
|SSO|17|123|256|173|18|0|0|26,9%|
|SO|12|77|147|168|15|0|0|19,2%|
|OSO|5|34|75|146|53|0|0|14,3%|
|O|7|9|19|72|13|1|0|5,5%|
|ONO|6|6|1|2|0|0|0|0,7%|
|NO|5|5|1|0|0|0|2|0,6%|
|NNO|7|6|0|5|3|0|4|1,1%|

Nota: Las filas sombreadas en azul son las componentes que registran máximas

frecuencias.

En el gráfico de frecuencia de velocidad del viento de la Figura 26, se observa una mayor

frecuencia en las categorías de velocidades en el rango 0,5 - 5,7 m/s, lo que representa en

su conjunto el 87,7% de los vientos totales simulados para esta estación. En menor

frecuencia se presentan los vientos intensos, superiores a 8,8 m/s, y los vientos calmos

(menores a 0,5 m/s), con un 0,6% y 6,0% respectivamente del total de los datos simulados.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 58 de 132**

**Figura 26. Frecuencia de los vientos en primavera, año 2021.**

**6.1.2.5** **Perfil diario de las velocidades del viento anuales.**

En la Figura 27 se presenta el perfil horario promedio de las velocidades del viento para

cada estación del año, además de su evolución con respecto a las velocidades anuales, con

los datos extraídos del modelo WRF del 2021. De la figura se desprende que la velocidad

del viento anual se mantiene con fluctuaciones entre 1,50 - 2,25 m/s entre las 23:00 y 08:00

horas. Desde entonces y hasta las 17:00 horas la velocidad del viento aumenta fuertemente

hasta llegar a los 4,75 m/s; luego la velocidad disminuye para continuar con el ciclo diario.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 59 de 132**

**Figura 27. Perfil diario de velocidad del viento, WRF año 2021.**

El análisis del perfil de la velocidad del viento horario por estación nos permite evidenciar el

comportamiento del viento esperado para cada estación. Vemos que las velocidades

promedio máximas se alcanzaron en las estaciones de verano y primavera con velocidades

promedio de 6,5 m/s y 5,3 m/s respectivamente, por el contrario, los vientos promedios

menos intensos se registraron en verano y otoño donde las velocidades del viento promedio

corresponden a 0,9 m/s y 1,2 m/s respectivamente. Finalmente, como se observa en la

figura los vientos promedio más intensos se alcanzaron durante el verano, siendo

particularmente evidente el incremento durante las 15:00 y 18:00 horas del día.

**6.1.3** **Caracterización de la Temperatura del Aire**

**6.1.3.1** **Temperatura Mensual**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 60 de 132**

En la Figura 28 se aprecia la variabilidad anual de la temperatura promedio mensual mínima,

máxima y promedio, simulada con el modelo meteorológico WRF. La simulación indica que

la temperatura promedio mensual disminuye durante los meses de otoño e invierno y

aumentan durante los meses más cálidos (primavera y verano).

**Figura 28. Temperatura Mensual WRF, año 2021.**

Se observa que la temperatura máxima mensual modelada se alcanza en los meses de

enero, febrero, marzo y diciembre, donde se superarían los 33,0°C. Por el contrario, el mes

más frío es mayo, donde se alcanzó una temperatura de 3,0°C. Además, son junio y julio

los meses con menor amplitud térmica, alcanzando en promedio los 20,5°C.

La mayor amplitud térmica simulada durante el año se logra en enero y marzo, donde se

alcanzan los 27,9°C y 27,7°C, respectivamente. Los resultados sugieren a su vez que en la

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 61 de 132**

zona existe una importante variación térmica, la que en promedio alcanza durante el año

los 24,7°C.

**6.1.3.2** **Perfil Diario de la Temperatura**

La Figura 29 muestra el perfil promedio diario de temperaturas para el punto de análisis,

simulado con WRF. En efecto es posible apreciar que todas las estaciones del año presentan

un comportamiento similar, alcanzando una temperatura mínima entre las 23:00 y 06:00

horas, posteriormente a medida se calienta la superficie por acción de la radiación solar, la

temperatura comienza a aumentar alcanzando nuevamente para todas las estaciones su

máximo entre las 12:00 y 16:00 horas, para luego disminuir constantemente hacia las

últimas horas de la noche.

**Figura 29. Perfil diario de Temperatura, WRF año 2021.**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 62 de 132**

Además, es posible apreciar que la mayor amplitud térmica se simula para los meses más

cálidos, alcanzando en verano una diferencia de 16,4°C entre el promedio horario máximo

y mínimo, seguidos de los meses de primavera y otoño donde la amplitud térmica es de

12,5°C y 12,2°C, respectivamente. Por el contrario, en invierno se alcanza la menor amplitud

térmica respecto a las otras estaciones con una diferencia de solo 7,7°C.

**6.1.4** **Altura de Capa de Mezcla**

La altura de la capa mezcla es de importancia, pues es un parámetro básico de la modelación

de dispersión de contaminantes, ya que es ahí donde tiene lugar el transporte turbulento

de masas y energía, constituyendo un parámetro que caracteriza la troposfera baja.

El modelo WRF, es capaz de simular la altura de capa de mezcla, de hecho, tal como se

observa en la Figura 30, la evolución de la capa de mezcla diaria tiene un patrón

relativamente similar en todas las estaciones del año.

En el mismo contexto, se observa que, durante los meses de invierno, la altura de capa de

mezcla es la más estable en comparación a los otros meses, y, por tanto, se espera que las

condiciones de dispersión de contaminantes sean más desfavorables comparada con las

otras estaciones.

En general, se puede observar que durante la noche y madrugada la altura de capa de

mezcla es menor a la simulada durante el día, esto significa que es en ese momento del día

en donde se propician peores condiciones para la dispersión de contaminantes. Esto debido

a la ausencia de aporte energético del sol, influyendo en el intercambio vertical entre

distintos niveles desfavorablemente, de este modo, la agitación turbulenta es poco

significativo.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 63 de 132**

**Figura 30. Evolución diaria de la altura de capa de mezcla, WRF año 2021.**

Con la salida del sol, el aumento de calor de la superficie terrestre, éste es transmitido a la

atmosfera, produciendo agitación en la capa de mezcla lo que provoca un incremento en el

espesor del volumen del aire afectado por el calentamiento del suelo, llegando al máximo

entre las 13:00 y 15:00 horas del día, es en este momento del día en donde se propician

las condiciones de máxima inestabilidad atmosférica, favoreciendo la dispersión de

contaminantes.

Por ende, y a modo de conclusión, se puede mencionar que este parámetro es importante

para la concentración de un contaminante, ya que a medida que disminuye la altura de capa

de mezcla, el contaminante tiende a concentrarse, y, por el contrario, a medida que se aleja

de la superficie, el contaminante tiene a dispersarse.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**6.1.5** **Caracterización de la precipitación**

**Página 64 de 132**

La simulación meteorológica del modelo WRF presentada en la Figura 31, determinó que

para el año 2021 la precipitación en la zona de estudio alcanzó los 260,5 mm.

Es posible observar, además que los meses con la mayor precipitación simulada son agosto

y septiembre, los que en su conjunto representan el 68% de la precipitación anual simulada.

En efecto agosto es el mes donde se presenta la máxima precipitación con 122 mm, que

representa el 47% de la precipitación anual. Por su parte los meses más cálidos, a excepción

de enero, presentan escaso aporte a la precipitación anual en la zona.

**Figura 31. Precipitación Anual, WRF 2021.**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**6.2** **Concentraciones Modeladas**

**Página 65 de 132**

A continuación, se presentan los resultados de la modelación de material particulado y gases

emitidos a la atmosfera. Cabe recordar que, el escenario modelado corresponde a las

emisiones de material particulado, tanto MP10 como MP2,5, y gases (NO 2, SO 2 y CO), las

cuales se producen en la fase de operación del proyecto durante el año 4.

**6.2.1** **Dispersión e Isoconcentración Material Particulado Respirable, MP10**

A continuación, se presenta el análisis de los resultados para el MP10 tanto para la

concentración promedio anual y 24 horas.

Es importante señalar que la pluma de dispersión de MP10 simulada por el modelo abarca

la zona de emplazamiento del proyecto, donde se produce operación de las 357 unidades

habitacionales contempladas en el proyecto.

**6.2.1.1** **Concentración Promedio 24 horas de MP10**

En la Figura 32, se muestra la pluma de dispersión de la concentración promedio diaria de

MP10, de donde se observa lo siguiente:

 Las concentraciones se distribuyen alrededor del proyecto, situando su máxima

concentración en la zona centro del proyecto, específicamente en el lugar donde se

realiza la combustión a leña para calefacción de las viviendas de la situación basal.

Además, se observa una concentración de las emisiones en la zona donde se ubican

las rutas de tránsito interno y las rutas externas adyacentes al polígono del proyecto.

La forma de la pluma demuestra que es en el mismo predio del proyecto donde se

genera la mayor parte de las emisiones, principalmente en la zona donde se ubican

las actividades ejecutadas en la fase de operación. Las actividades ejecutadas en la

zona de mayor concentración corresponden a:

1. Calefacción domiciliaria.

2. Transito interno por vías pavimentadas.

3. Transito externo por vías pavimentadas.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 66 de 132**

 La pluma de dispersión se distribuye mayormente en las direcciones norte y este

desplazándose aproximadamente en 912 m desde la zona de máxima concentración

hacia el borde más alejado de la pluma.

 La pluma de dispersión tiene una forma relativamente homogénea en las direcciones

de la rosa de los vientos, pronunciándose en las direcciones norte y oeste noroeste.

Esto se condice con fuentes de emisión que liberan emisiones a baja altura, con lo

cual, las emisiones tienden a dispersarse dentro del medio circundante.

 Las concentraciones modeladas van desde los 1,0 μg/m3 a los 4,58 μg/m3 en la zona

central del proyecto, donde se realizar gran parte del tránsito en vías pavimentadas,

con una inclinación hacia la zona donde se llevan a cabo las actividades de

calefacción domiciliaria y circulación de vehículos por caminos pavimentados, las que

pueden ser catalogadas como de baja magnitud.

 En relación con los puntos receptores externos elegidos se observa que, 7 de los 20

evaluados se encuentran dentro de la pluma principal. Los receptores R22, R19 y

R21 son los más próximo al área de mayor concentración, alcanzando los 2,62

μg/m3, 1,79 μg/m3 y 2,09 μg/m3 respectivamente. En tanto, que los receptores R36

y R37 se encuentran más alejados del proyecto, alcanzando concentraciones de

MP10 de 0,02 μg/m3 y 0,01 μg/m3 respectivamente. Por otra parte, la totalidad de

los receptores internos se encuentran dentro de la pluma de dispersión, siendo los

receptores ubicados en la situación basal los que presentan las mayores

concentraciones.

En la Figura 34, se muestra el mapa de isoconcentración, de donde se puede concluir que:

 La pluma se extiende hasta los 908 m por el norte y 403 m por el sur, 749 m al este

y 754 m al oeste desde la zona de máxima concentración, disminuyendo las

concentraciones simuladas en un 71% respecto al punto de máxima concentración.

 La zona de mayor concentración abarca una superficie de 3,36 ha. Esta superficie

abarca la zona donde se realiza la calefacción domiciliaria junto con la circulación de

vehículos por caminos pavimentados, alcanzando concentraciones entre los 3,72 -

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 67 de 132**

4,40 μg/m [3] .

El área total del mapa de isoconcentración abarca una superficie de 150,89 ha.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 68 de 132**

**Figura 32. Dispersión de la pluma de MP10 como concentración de 24 horas**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 69 de 132**

**Figura 33. Dispersión de la pluma de MP10 como concentración de 24 horas, receptores internos**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 70 de 132**

**Figura 34. Isolíneas de concentración de MP10 como concentración de 24 horas.**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**6.2.1.2** **Concentración Promedio Anual de MP10**

**Página 71 de 132**

En la Figura 35, se muestra la pluma de dispersión de la concentración promedio anual de

MP10, de donde se concluye lo siguiente:

 La forma de la pluma de dispersión es completamente homogénea, con una marcada

inclinación hacia el nor noreste.

 En la pluma de dispersión se observa un área de mayores concentraciones donde se

realizan las actividades de tránsito en caminos pavimentados, la ubicación de la

situación basal donde se realiza la calefacción domiciliaria, cuyo rango varía entre

los 0,50 a 1,52 μg/m3.

 Con base en los resultados obtenidos, de los receptores externos solo el receptor 18

se encuentra inmerso dentro de la pluma de dispersión. Respecto a los receptores

internos, es casi la totalidad de estos se encuentran dentro de la pluma de dispersión

a excepción del receptor R14.

En la Figura 37, se muestra el mapa de isoconcentración, de donde se puede concluir que:

 La pluma se extiende hasta los 428 m por el norte y 344 m al sur, 322 m al oeste y

353 m al este desde la zona de mayor concentración. A estas distancias la

concentración esperada es de 0,50 μg/m3.

 La pluma de dispersión se distribuye de manera relativamente uniforme con una

extensión en dirección nor noreste, desplazándose aproximadamente 479 m desde

el centro del proyecto hacia el borde más largo de la pluma.

 Se distingue una zona de máxima concentración de 0,05 ha en donde las

concentraciones varían en los 1,22 a 1,40 μg/m3 dentro de la zona de emplazamiento

del proyecto.

 El área total del mapa de isoconcentración abarca una superficie de 43,82 ha.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 72 de 132**

**Figura 35. Dispersión de la pluma de MP10 como concentración promedio anual.**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 73 de 132**

**Figura 36. Dispersión de la pluma de MP10 como concentración promedio anual, receptores internos**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 74 de 132**

**Figura 37. Isolíneas de concentración de MP10 como concentración promedio anual.**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 75 de 132**

**6.2.2** **Dispersión e Isoconcentración Material Particulado Fino Respirable, MP2,5**

A continuación, se presenta el análisis de los resultados para el MP2,5, tanto para la

concentración promedio anual y 24 horas.

**6.2.2.1** **Concentración Promedio diaria MP2,5**

En la Figura 38, se muestra la pluma de dispersión de la concentración promedio diario de

MP2,5, de donde se concluye que:

 La pluma de dispersión al igual que lo ocurrido para MP10 presenta sus mayores

concentraciones en la zona central del proyecto, donde existe un gran tránsito en

vías pavimentadas y también en la zona donde se realiza la calefacción domiciliaria

en los meses de invierno y otoño, cuyas emisiones constituyen el principal aporte a

las concentraciones modeladas.

 La concentración generada en la atmosfera de las emisiones de MP2,5 varía desde

los 1,00 a los 3,61 μg/m3.

 De los puntos receptores externos modelados, solo 4 de los 20 se encuentran dentro

de la pluma de dispersión, siendo el receptor R18 el cual alcanza la mayor

concentración, la que equivalente a 1,25 μg/m3. Respecto a los receptores internos,

la totalidad de estos se encuentra dentro de la pluma de dispersión.

En la Figura 40, se muestra el mapa de isoconcentración, de donde se puede concluir:

 La pluma se extiende hasta los 635 m por el norte y 316 m al sur, 429 m al este y

562 m al oeste desde la zona de mayor concentración. A estas distancias la

concentración esperada es de 1,0 μg/m3.

 En total la pluma abarca un área de aproximada de 87,66 ha.

 Las zonas de mayores concentraciones abarcan una superficie de 2,41 ha. Esta

superficie se ubica abarcando el área de circulación de vehículos en camino

pavimentado, y el área de la situación basal del proyecto, donde se alcanzan

concentraciones que varían entre los 3,04 - 3,55 μg/m [3] .

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 76 de 132**

**Figura 38. Dispersión de la pluma de MP2,5** **como concentración promedio diario**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 77 de 132**

**Figura 39. Dispersión de la pluma de MP2,5** **como concentración promedio diaria, receptores internos**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 78 de 132**

**Figura 40. Isolíneas de concentración de MP2,5 como concentración promedio diaria.**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**6.2.2.2** **Concentración promedio anual de MP2,5**

**Página 79 de 132**

En la Figura 41, se muestra la pluma de dispersión de la concentración promedio anual de

MP2,5, de donde se concluye que:

 El comportamiento del material particulado fino como concentración promedio anual,

concentra sus máximas concentraciones en la zona centro del proyecto,

desplazándose en las direcciones Norte y Sur, viéndose influenciado principalmente

por la zona donde se realiza calefacción a leña de la situación basal.

 La concentración generada en la atmósfera por las emisiones de MP2,5 varían desde

los 0,50 a los 1,10 μg/m3.

 Ninguno de los puntos receptores externos se encuentra dentro de la pluma de

dispersión, siendo el receptor R18 el más cercano con una concentración de 0,26

μg/m3. Respecto a los receptores internos, los receptores R14 al R17 se encuentran

fuera de la pluma de dispersión, siendo estos receptores los más alejados de la

situación basal del proyecto, la principal fuente de MP dentro del proyecto.

En la Figura 43, se muestra el mapa de isoconcentración, de donde se puede concluir

que:

 En relación con la dimensión, la pluma se extiende hasta los 305 m por el norte y

208 m por el sur, 178 m al este y 255 m al oeste desde la zona de mayor

concentración. A estas distancias la concentración esperada es de 0,50 μg/m3. La

distribución de la pluma se presenta de manera relativamente uniforme en todas las

direcciones.

 El área donde se ubica la zona de mayor concentración evidencia una superficie 1,64

ha. Es en esta zona donde se encuentra el punto de mayor magnitud, con una

concentración equivalente a 0,98 μg/m3.

 El área total de la pluma de isoconcentración abarca una superficie de 17,96 ha.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 80 de 132**

**Figura 41. Dispersión de la pluma de MP2,5 como concentración promedio anual**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 81 de 132**

**Figura 42. Dispersión de la pluma de MP2,5 como concentración promedio anual, receptores internos**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 82 de 132**

**Figura 43. Isolíneas de concentración de MP2,5 como concentración promedio anual.**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**6.2.3** **Dispersión Dióxido de Nitrógeno, NO** **2**

**Página 83 de 132**

A continuación, se presenta el análisis de los resultados para el NO 2, tanto para la

concentración anual y horaria.

**6.2.3.1** **Concentración horaria NO** **2**

En la Figura 44, se muestra la pluma de dispersión de la concentración horaria de NO 2 de

donde se concluye que:

 La pluma de dispersión presenta una forma irregular, centrándose en medio del

proyecto, donde se llevan a cabo principalmente las actividades transito interno en

vías pavimentadas y calefacción por combustión a leña, demostrando que su

principal aporte corresponde a la calefacción de las viviendas, seguido de la

combustión interna de los vehículos livianos.

 La concentración generada en la atmosfera de las emisiones de NO 2 varía desde los

3,30 a los 10,00 μg/m3.

 De los puntos receptores externos modelados, cuatro se encuentran dentro de la

pluma de dispersión, siendo el más alto el receptor R22 con una concentración de

5,62 μg/m3. Respecto a los internos, la totalidad de estos se encuentra dentro de la

pluma de dispersión.

 La pluma se extiende hasta los 737 m por el norte y 459 m al sur, 254 m al este y

451 m al oeste desde la zona de mayor concentración. A estas distancias la

concentración esperada es de 3,30 μg/m3.

 En total la pluma abarca un área de aproximada de 97,86 ha.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 84 de 132**

**Figura 44. Dispersión de la pluma de NO** **2** **como concentración máxima horaria**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 85 de 132**

**Figura 45. Dispersión de la pluma de NO** **2** **como concentración máxima horaria, receptores internos**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 86 de 132**

**Figura 46. Isolíneas de concentración de NO** **2** **como concentración máxima horaria.**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**6.2.3.2** **Concentración Anual NO** **2**

**Página 87 de 132**

En la Figura 47, se muestra la pluma de dispersión de la concentración anual de NO 2, de

donde se concluye que:

 La pluma de dispersión se distribuye principalmente en la situación basal del

proyecto y en parte de las rutas internas pavimentadas.

 - La concentración de emisiones generadas de NO 2 en un año, varía desde los 0,40 a

los 1,11 μg/m3.

 De los puntos receptores externos modelados, ninguno de los 20 se encuentra

dentro de la pluma de dispersión, siendo el receptor R22 el más cercano, con una

concentración de 0,37 μg/m3. Respecto a los internos, solo 2 de los 17 receptores

se encuentran fuera de la pluma de dispersión, siendo estos los más alejados de la

situación basal.

 La pluma se extiende hasta los 348 m por el norte y 263 m al sur, 263 m al este y

261 m al oeste desde la zona de mayor concentración. A estas distancias la

concentración esperada es de 0,40 μg/m3.

 En total la pluma abarca un área de aproximada de 28,26 ha.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 88 de 132**

**Figura 47. Dispersión de la pluma de NO** **2** **como concentración anual.**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 89 de 132**

**Figura 48. Dispersión de la pluma de NO** **2** **como concentración anual, receptores internos**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 90 de 132**

**Figura 49. Isolíneas de concentración de NO** **2** **como concentración anual.**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**6.2.4** **Dispersión Dióxido de Azufre (SO** **2** **)**

**Página 91 de 132**

A continuación, se presenta el análisis de los resultados para el SO2, tanto para la

concentración horaria, diaria y anual.

**6.2.4.1** **Concentración horaria SO** **2**

En la Figura 50, se muestra la pluma de dispersión de la concentración horaria de SO 2, de

donde se concluye lo siguiente:

 La forma de la pluma de dispersión es relativamente homogénea, presentando un

leve pronunciamiento en dirección este noreste.

 En la pluma de dispersión se observa un área de mayores concentraciones donde se

realizan las actividades de tránsito en caminos pavimentados interno junto a la

ubicación de la situación basal donde se realiza la calefacción domiciliaria, cuyo rango

varía entre los 0,13 a 0,33 μg/m3.

 Con base en los resultados obtenidos, solo 1 de los 17 receptores externos se

encuentra inmerso dentro de la pluma de dispersión, siendo el R18 el que posee la

mayor concentración con 0,114 μg/m3. Respecto a los internos, solo 2 de los 17

receptores se encuentran fuera de la pluma de dispersión, siendo estos los más

alejados de la situación basal.

En la Figura 52, se muestra el mapa de isoconcentración, de donde se puede concluir que:

 La pluma se extiende hasta los 308 m por el norte y 306 m al sur, 332 m al oeste y

362 m al este desde la zona de mayor concentración. A estas distancias la

concentración esperada es de 0,13 μg/m3.

 La pluma de dispersión se distribuye de manera relativamente uniforme con una

extensión en dirección este, desplazándose aproximadamente 439 m desde el centro

del proyecto hacia el borde más largo de la pluma.

 Se distingue una zona de máxima concentración de 1,51 ha en donde las

concentraciones varían en los 0,25 a 0,28 μg/m3 dentro de la zona de emplazamiento

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 92 de 132**

del proyecto.

El área total del mapa de isoconcentración abarca una superficie de 35,3 ha.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 93 de 132**

**Figura 50. Dispersión de la pluma de SO** **2** **como concentración horaria**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 94 de 132**

**Figura 51. Dispersión de la pluma de SO** **2** **como concentración horaria, receptores internos**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 95 de 132**

**Figura 52. Isolíneas de concentración de SO** **2** **como concentración horaria**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**6.2.4.2** **Concentración 24 horas SO** **2**

**Página 96 de 132**

En la Figura 53, se muestra la pluma de dispersión de la concentración 24 horas de SO 2, de

donde se concluye que:

 La pluma de dispersión presenta sus mayores concentraciones en la situación basal

del proyecto, donde se realiza la actividad de calefacción de las viviendas mediante

la combustión de leña. Adicionalmente, la pluma cubre la mayoría de las rutas

pavimentadas internas del proyecto junto con las vías pavimentadas externas

adyacentes al polígono del proyecto.

 La concentración generada en la atmosfera de las emisiones de SO 2 varía desde los

0,08 a los 0,16 μg/m3.

 Ninguno de los 20 puntos receptores externos modelados se encuentra dentro de la

pluma de dispersión, siendo el receptor R22 el que presenta concentraciones de

0,079 μg/m3. Respecto a los internos, 4 de los 17 receptores se encuentran fuera

de la pluma de dispersión, siendo estos los más alejados de la situación basal.

En la Figura 55, se muestra el mapa de isoconcentración, de donde se puede concluir:

 La pluma se extiende hasta los 288 m por el norte y 230 m al sur, 275 m al este y

275 m al oeste desde la zona de mayor concentración. A estas distancias la

concentración esperada es de 0,08 μg/m3.

 En total la pluma abarca un área de aproximada de 23,3 ha.

 Las zonas de mayores concentraciones abarcan una superficie de 0,52 ha, donde se

alcanzan concentraciones que varían entre los 0,14 - 0,16 μg/m [3] .

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 97 de 132**

**Figura 53. Dispersión de la pluma de SO** **2** **como concentración 24 horas**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 98 de 132**

**Figura 54. Dispersión de la pluma de SO** **2** **como concentración 24 horas, receptores internos**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 99 de 132**

**Figura 55. Isolíneas de concentración de SO** **2** **como concentración 24 horas**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**6.2.4.3** **Concentración Anual SO** **2**

**Página 100 de**

**132**

En la Figura 56, se muestra la pluma de dispersión de la concentración anual de SO 2, de

donde se concluye que:

 El comportamiento del dióxido de azufre como concentración promedio anual, al

igual que el SO 2 como norma diaria, concentra sus máximas concentraciones en la

zona de situación basal del proyecto.

 La concentración generada en la atmósfera por las emisiones de MP2,5 varían desde

los 0,020 a los 0,049 μg/m3.

 De los puntos receptores externos modelados, ninguno se encuentra dentro de la

pluma de dispersión. Respecto a los internos, 5 de los 17 receptores se encuentran

fuera de la pluma de dispersión, siendo estos los más alejados de la situación basal.

En la Figura 58, se muestra el mapa de isoconcentración, de donde se puede concluir

que:

 En relación con la dimensión, la pluma se extiende hasta los 220 m por el norte y

256 m por el sur, 180 m al este y 234 m al oeste desde la zona de mayor

concentración. A estas distancias la concentración esperada es de 0,02 μg/m3.

 El área donde se ubica la zona de mayor concentración evidencia una superficie 1,2

ha. Es en esta zona donde se encuentra el punto de mayor magnitud, con una

concentración equivalente a 0,040 μg/m3.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 101 de**

**132**

**Figura 56. Dispersión de la pluma de SO** **2** **como concentración anual**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 102 de**

**132**

**Figura 57. Dispersión de la pluma de SO** **2** **como concentración anual, receptores internos**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 103 de**

**132**

**Figura 58. Isolíneas de concentración de SO** **2** **como concentración anual**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**6.2.5** **Dispersión Monóxido de Carbono (CO)**

**Página 104 de**

**132**

A continuación, se presenta el análisis de los resultados para el CO, tanto para la

concentración en 8 horas y horaria.

**6.2.5.1** **Concentración horaria CO**

En la Figura 59, se muestra la pluma de dispersión de la concentración horaria de CO, de

donde se concluye lo siguiente:

 La forma de la pluma de dispersión es relativamente homogénea, con una inclinación

en dirección nor noreste.

 En la pluma de dispersión se observa un área de mayores concentraciones donde se

realizan las actividades calefacción domiciliaria junto con el tránsito en vías

pavimentadas internas, siendo la primera actividad la principal aportante de este

contaminante.

 Con base en los resultados obtenidos, solo 1 de los 17 receptores externos definidos

se encuentra inmerso dentro de la pluma de dispersión, siendo el R18 el que posee

la mayor concentración con 0,164 mg/m3. Respecto a los internos, solo 2 de los 17

receptores se encuentran fuera de la pluma de dispersión, siendo estos los más

alejados de la situación basal.

En la Figura 59, se muestra el mapa de isoconcentración, de donde se puede concluir que:

 La pluma se extiende hasta los 315 m por el norte y 259 m al sur, 257 m al oeste y

392 m al este desde la zona de mayor concentración. A estas distancias la

concentración esperada es de 0,15 mg/m3.

 La pluma de dispersión se distribuye de manera relativamente uniforme con una

extensión en dirección nor noreste, desplazándose aproximadamente 447 m desde

el centro del proyecto hacia el borde más largo de la pluma.

 Se distingue una zona de máxima concentración de 0,24 ha en donde las

concentraciones varían en los 0,27 a 0,30 mg/m3 dentro de la zona de

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

emplazamiento del proyecto.

**Página 105 de**

**132**

El área total del mapa de isoconcentración abarca una superficie de 34,71 ha.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 106 de**

**132**

**Figura 59. Dispersión de la pluma de CO como concentración horaria**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 107 de**

**132**

**Figura 60. Dispersión de la pluma de CO como concentración horaria, receptores internos**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 108 de**

**132**

**Figura 61. Isolíneas de concentración de CO como concentración horaria**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**6.2.5.2** **Concentración 8 horas CO**

**Página 109 de**

**132**

En la Figura 62, se muestra la pluma de dispersión de la concentración 8 horas para CO, de

donde se concluye que:

 En la pluma de dispersión, al igual que la pluma horaria de CO, se distribuye

principalmente alrededor de la zona de situación basal del proyecto, donde se

desarrolla la actividad de combustión de leña para calefacción de las viviendas

 La concentración generada en la atmosfera de las emisiones de CO varía desde los

0,10 a los 0,21 mg/m3.

 De los puntos receptores externos modelados, solo 1 de los 20 se encuentran dentro

de la pluma de dispersión, siendo el receptor R1 el cual alcanza la mayor

concentración, la que equivalente a 0,11 mg/m3. Respecto a los internos, 4 de los

17 receptores se encuentran fuera de la pluma de dispersión, siendo estos los más

alejados de la situación basal.

En la Figura 64, se muestra el mapa de isoconcentración, de donde se puede concluir:

 La pluma se extiende hasta los 258 m por el norte y 254 m al sur, 342 m al este y

234 m al oeste desde la zona de mayor concentración. A estas distancias la

concentración esperada es de 0,10 mg/m3.

 En total la pluma abarca un área de aproximada de 26,1 ha.

 Las zonas de mayores concentraciones abarcan una superficie de 0,89 ha, donde se

alcanzan concentraciones que varían entre los 0,17 - 0,19 mg/m [3] .

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 110 de**

**132**

**Figura 62. Dispersión de la pluma de CO como concentración 8 horas**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 111 de**

**132**

**Figura 63. Dispersión de la pluma de CO como concentración 8 horas, receptores internos**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 112 de**

**132**

**Figura 64. Isolíneas de concentración de CO como concentración 8 horas**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**6.2.6** **Modelación discreta de las emisiones contaminantes**

**Página 113 de**

**132**

La modelación discreta de emisiones fue realizada para MP10, MP2,5, NO 2, SO 2, CO, cuyos

valores de concentración para los puntos receptores son presentados en las siguientes

tablas. Tal como se ha mencionado, estos puntos corresponden a viviendas y lugares de

encuentro de la población cercana al proyecto y a los caminos.

**6.2.6.1** **Material Particulado Grueso y Fino**

A continuación, se presentan los resultados de la modelación para MP10 y MP2,5 para todos

los receptores incluidos en la modelación.

A grandes rasgos se puede observar que la concentración modelada como MP - 24 horas,

independientemente de su fracción, es considerablemente mayor que el promedio anual.

esto se debe a que las concentraciones se encuentran altamente influenciados por el uso

de leña para calefacción residencial, en este aspecto, es importante tener presente que el

cálculo la concentración 24 horas se obtiene determinando el percentil 98 de las

concentraciones diarias modeladas representando una concentración en particular de uno

de los días modelados, el que coincide con el periodo de invierno en donde se usa calefacción

y en donde las condiciones de dispersión son más complejas (inversión térmica, vientos

calmos, etc.). De los resultados obtenidos se observa que en percentiles más bajos al 98 las

concentraciones de MP disminuyen considerablemente, lo que reafirma que las

concentraciones anuales sean de magnitud considerablemente más bajas a las 24 h.

De los resultados obtenidos se destaca:

 Todas las concentraciones modeladas en los 37 receptores discretos son de baja

magnitud.

 Los receptores en los que se simularon concentraciones de mayor magnitud en

comparación al resto son los que se encuentran en la situación base del proyecto,

los que a la vez son fuentes emisoras, a representar el uso de calefacción residencial.

Cabe hacer la mención que, para el resto de las viviendas, el proyecto contempla

sistema de calefacción integrado a la vivienda, por lo que no se genera el mismo

efecto.

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 114 de**

**132**

 Respecto al MP10 como norma diaria, las concentraciones en los receptores dentro

del polígono del proyecto fluctuaron entre los 1,70 μg/m [3] a los 4,59 μg/m [3], en

cambio, para los receptores fuera del polígono del proyecto las concentraciones

modeladas variaron entre los 0,01 μg/m [3] a los 2,63 μg/m [3] .

 Por otra parte, respecto al mismo contaminante como promedio anual las

concentraciones en los receptores discretos dentro del polígono del proyecto se

movieron entre los 0,63 μg/m [3] a los 1,52 μg/m [3], en cambio, los receptores externos

presentaron concentraciones entre los 0,00 μg/m [3] a los 0,57 μg/m [3] .

 Respecto al material particulado fino como norma diaria las concentraciones

modeladas en los receptores internos variaron entre los 1,39 μg/m [3] a los 3,61 μg/m [3],

en cambio, para los receptores externos se presentaron concentraciones que

variaban entre los 0,01 μg/m [3] a los 1,71 μg/m [3] .

 Por último, las concentraciones de MP2,5 como promedio anual variaron entre los

0,30 μg/m [3] a los 1,18 μg/m [3] para los receptores internos y entre 0,00 μg/m [3] a los

0,38 μg/m [3] .

**Tabla 22. Concentración modelada en puntos receptores con respecto a MP10** **y**

**MP2,5.**

|Punto|Concentración MP10 (μg/m3)|Col3|Concentración MP2,5(μg/m3)|Col5|
|---|---|---|---|---|
|**Punto**|**Anual**|**24 horas**|**Anual**|**24 horas**|
|R1|1,11|3,89|0,70|2,57|
|**R2**|**1,52**|**4,36**|**1,18**|**3,61**|
|R3|1,31|4,03|0,88|2,79|
|R4|1,37|4,04|1,03|3,35|
|R5|1,29|4,16|0,94|3,01|
|**R6**|**1,16**|**4,31**|**0,74**|**2,43**|
|**R7**|**1,15**|**4,58**|**0,71**|**2,78**|
|R8|1,10|3,64|0,78|2,80|
|R9|0,63|1,70|0,46|1,42|
|R10|0,96|3,51|0,56|2,08|
|R11|1,08|4,22|0,56|2,09|
|R12|0,75|3,10|0,46|1,85|
|R13|0,83|3,75|0,37|1,77|
|R14|0,14|0,31|0,06|0,17|
|R15|0,90|3,59|0,36|1,49|

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 115 de**

**132**

|Punto|Concentración MP10 (μg/m3)|Col3|Concentración MP2,5(μg/m3)|Col5|
|---|---|---|---|---|
|**Punto**|**Anual**|**24 horas**|**Anual**|**24 horas**|
|R16|0,65|3,03|0,30|1,39|
|R17|0,21|0,45|0,11|0,35|
|R18|0,33|1,49|0,26|1,25|
|**R19**|**0,35**|**1,79**|**0,15**|**0,73**|
|R20|0,04|0,16|0,02|0,10|
|R21|0,37|2,09|0,17|0,89|
|**R22**|**0,57**|**2,62**|**0,38**|**1,71**|
|**R23**|**0,31**|**1,63**|**0,18**|**0,89**|
|R24|0,16|0,88|0,09|0,47|
|R25|0,24|1,29|0,11|0,55|
|R26|0,15|0,88|0,06|0,33|
|R27|0,29|1,51|0,18|0,83|
|R28|0,11|0,59|0,05|0,25|
|R29|0,09|0,55|0,04|0,25|
|R30|0,21|1,13|0,12|0,65|
|R31|0,12|0,69|0,06|0,34|
|R32|0,07|0,41|0,03|0,19|
|R33|0,03|0,17|0,02|0,10|
|R34|0,02|0,13|0,01|0,07|
|R35|0,01|0,06|0,01|0,04|
|R36|0,00|0,02|0,00|0,02|
|R37|0,00|0,01|0,00|0,01|

 - Los receptores marcados en azul presentan las mayores concentraciones modeladas

**6.2.6.2** **Dióxido de Nitrógeno (NO** **2** **)**

De los resultados obtenidos se destaca:

 Todas las concentraciones modeladas en los 37 receptores discretos son de baja

magnitud.

 - Respecto al NO 2 como norma horaria, las concentraciones en los receptores dentro

del polígono del proyecto fluctuaron entre los 2,83 μg/m [3] a los 10,05 μg/m [3], en

cambio, para los receptores fuera del polígono del proyecto las concentraciones

modeladas variaron entre los 0,01 μg/m [3] a los 5,69 μg/m [3] .

 Por otra parte, respecto al mismo contaminante como promedio anual las

concentraciones en los receptores discretos dentro del polígono del proyecto se

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 116 de**

**132**

movieron entre los 0,42 μg/m [3] a los 1,11 μg/m [3], en cambio, los receptores externos

presentaron concentraciones entre los 0,00 μg/m [3] a los 0,37 μg/m [3] .

**Tabla 23. Concentración modelada en puntos receptores con respecto a NO** **2**

|Punto|Concentración NO (μg/m3)<br>2|Col3|
|---|---|---|
|**Punto**|**Horario**|**Anual**|
|R1|8,47|0,78|
|**R2**|**8,37 **|**1,11 **|
|R3|7,85|0,92|
|R4|6,55|0,99|
|R5|7,34|0,91|
|**R6**|**9,02 **|**0,79 **|
|**R7**|**9,94 **|**0,78 **|
|R8|7,10|0,78|
|R9|2,83|0,45|
|R10|7,14|0,66|
|R11|9,98|0,72|
|R12|7,11|0,50|
|**R13**|**10,05 **|**0,54 **|
|R14|1,10|0,10|
|R15|9,24|0,60|
|R16|8,33|0,42|
|R17|1,31|0,15|
|R18|2,57|0,22|
|**R19**|**5,49 **|**0,21 **|
|R20|0,50|0,03|
|**R21**|**5,69 **|**0,22 **|
|**R22**|**5,62 **|**0,37 **|
|R23|3,24|0,19|
|R24|2,10|0,09|
|R25|2,90|0,14|
|R26|2,21|0,08|
|R27|3,08|0,18|
|R28|1,12|0,06|
|R29|1,09|0,05|
|R30|2,10|0,12|

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 117 de**

**132**

|Punto|Concentración NO (μg/m3)<br>2|Col3|
|---|---|---|
|**Punto**|**Horario**|**Anual**|
|R31|1,10|0,06|
|R32|0,75|0,03|
|R33|0,20|0,01|
|R34|0,16|0,01|
|R35|0,07|0,00|
|R36|0,02|0,00|
|R37|0,01|0,00|

 - Los receptores marcados en azul presentan las mayores concentraciones modeladas

**6.2.6.3** **Dióxido de Azufre (SO** **2** **)**

De los resultados obtenidos se destaca:

 Todas las concentraciones modeladas en los 37 receptores discretos son de baja

magnitud.

 - Respecto al SO 2 como norma horaria, las concentraciones en los receptores dentro

del polígono del proyecto fluctuaron entre los 0,120 μg/m [3] a los 0,332 μg/m [3], en

cambio, para los receptores fuera del polígono del proyecto las concentraciones

modeladas variaron entre los 0,000 μg/m [3] a los 0,179 μg/m [3] .

 Por otra parte, respecto al mismo contaminante como promedio diario las

concentraciones en los receptores discretos dentro del polígono del proyecto se

movieron entre los 0,050 μg/m [3] a los 0,164 μg/m [3], en cambio, los receptores

externos presentaron concentraciones entre los 0,000 μg/m [3] a los 0,079 μg/m [3] .

 Por último, respecto a las concentraciones como promedio anual en los receptores

internos, estas variaron entre los 0,010 μg/m [3] a los 0,049 μg/m [3], en cambio, los

receptores externos presentaron concentraciones entre los 0,000 μg/m [3] a los 0,016

μg/m [3] .

**Tabla 24. Concentración modelada en puntos receptores con respecto a SO** **2** **.**

|Punto|Concentración SO (μg/m3)<br>2|Col3|Col4|
|---|---|---|---|
|**Punto**|**Horario**|**Diaria**|**Anual**|
|R1|0,012|0,004|0,001|

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 118 de**

**132**

|Punto|Concentración SO (μg/m3)<br>2|Col3|Col4|
|---|---|---|---|
|**Punto**|**Horario**|**Diaria**|**Anual**|
|**R2**|**0,084**|**0,033**|**0,006**|
|**R3**|**0,179**|**0,079**|**0,016**|
|**R4**|**0,076**|**0,033**|**0,007**|
|R5|0,041|0,018|0,003|
|R6|0,044|0,018|0,004|
|R7|0,028|0,012|0,002|
|R8|0,095|0,038|0,007|
|R9|0,017|0,007|0,002|
|R10|0,023|0,010|0,002|
|R11|0,069|0,027|0,005|
|R12|0,026|0,013|0,002|
|R13|0,016|0,007|0,001|
|R14|0,007|0,004|0,001|
|R15|0,006|0,003|0,000|
|R16|0,003|0,002|0,000|
|R17|0,001|0,001|0,000|
|R18|0,000|0,000|0,000|
|R19|0,001|0,000|0,000|
|R20|0,012|0,004|0,001|
|**R21**|**0,084**|**0,033**|**0,006**|
|**R22**|**0,179**|**0,079**|**0,016**|
|R23|0,076|0,033|0,007|
|R24|0,041|0,018|0,003|
|R25|0,044|0,018|0,004|
|R26|0,028|0,012|0,002|
|**R27**|**0,095**|**0,038**|**0,007**|
|R28|0,017|0,007|0,002|
|R29|0,023|0,010|0,002|
|R30|0,069|0,027|0,005|
|R31|0,026|0,013|0,002|
|R32|0,016|0,007|0,001|
|R33|0,007|0,004|0,001|
|R34|0,006|0,003|0,000|
|R35|0,003|0,002|0,000|
|R36|0,001|0,001|0,000|
|R37|0,000|0,000|0,000|

- Los receptores marcados en azul presentan las mayores concentraciones modeladas

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**6.2.6.4** **Monóxido de Carbono (CO)**

De los resultados obtenidos se destaca:

**Página 119 de**

**132**

Todas las concentraciones modeladas en los 37 receptores discretos son de baja

magnitud.

Respecto al CO como norma horaria, las concentraciones en los receptores dentro

del polígono del proyecto fluctuaron entre los 0,12 mg/m [3] a los 0,34 mg/m [3], en

cambio, para los receptores fuera del polígono del proyecto las concentraciones

modeladas variaron entre los 0,00 mg/m [3] a los 0,18 mg/m [3] .

Por otra parte, respecto al mismo contaminante como promedio de 8 horas las

concentraciones en los receptores discretos dentro del polígono del proyecto se

movieron entre los 0,07 mg/m [3] a los 0,21 mg/m [3], en cambio, los receptores externos

presentaron concentraciones entre los 0,00 mg/m [3] a los 0,11 mg/m [3] .

**Tabla 25. Concentraciones de CO en puntos receptores**

|Punto|Concentración CO (mg/m3)|Col3|
|---|---|---|
|**Punto**|**Horario**|** 8 horas**|
|R1|0,22|0,14|
|**R2**|**0,34**|**0,21**|
|R3|0,22|0,14|
|**R4**|**0,25**|**0,17**|
|R5|0,24|0,15|
|R6|0,21|0,13|
|**R7**|**0,27**|**0,14**|
|R8|0,23|0,15|
|R9|0,12|0,08|
|R10|0,19|0,12|
|R11|0,18|0,11|
|R12|0,18|0,10|
|R13|0,17|0,09|
|R14|0,02|0,01|
|R15|0,14|0,07|
|R16|0,13|0,07|
|R17|0,04|0,02|

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 120 de**

**132**

|Punto|Concentración CO (mg/m3)|Col3|
|---|---|---|
|**Punto**|**Horario**|** 8 horas**|
|**R18**|**0,11**|**0,07**|
|R19|0,08|0,04|
|R20|0,01|0,01|
|**R21**|**0,10**|**0,04**|
|**R22**|**0,18**|**0,11**|
|R23|0,08|0,04|
|R24|0,05|0,03|
|R25|0,05|0,03|
|R26|0,03|0,02|
|R27|0,10|0,05|
|R28|0,02|0,01|
|R29|0,02|0,01|
|R30|0,08|0,04|
|R31|0,03|0,02|
|R32|0,02|0,01|
|R33|0,01|0,01|
|R34|0,01|0,00|
|R35|0,00|0,00|
|R36|0,00|0,00|
|R37|0,00|0,00|

 - Los receptores marcados en azul presentan las mayores concentraciones modeladas

**6.2.7** **Aporte a la estación de Monitoreo de Representatividad Poblacional**

**(EMRP)**

A continuación, se presentan los resultados de la concentración de MP2,5 simuladas en la

EMRP Rancagua I y la proyección con el año de mayor emisión del proyecto.

En la Tabla 26, se observa el aumento de la concentración basal registrada en la EMRP entre

enero y diciembre de 2021 para MP10, MP2,5, SO 2 y CO.

Los resultados evidencian un aumento de la condición basal menor al 0,1% para la

concentración de todos los contaminantes.

**Tabla 26. Aumento de la concentración basal en la EMRP Rancagua I, año 2021**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 121 de**

**132**

|Col1|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|MP10<br>(μg/m3)|Anual|51,15|0,002|51,152|0,00%|
|MP10<br>(μg/m3)|24 horas|129,22|0,012|129,232|0,01%|
|MP2,5<br>(μg/m3)|Anual|26,03|0,002|26,032|0,01%|
|MP2,5<br>(μg/m3)|24 horas|91,71|0,009|91,719|0,01%|
|SO2<br>(μg/m3)|Anual|1,02|0,00004|1,020|0,00%|
|SO2<br>(μg/m3)|24 horas|1,32|0,00028|1,320|0,02%|
|SO2<br>(μg/m3)|1 hora|1,37|0,00055|1,371|0,04%|
|CO<br>(mg/m3)|8 horas|3,12|0,0005|3,120|0,01%|
|CO<br>(mg/m3)|1 hora|4,30|0,0006|4,301|0,01%|

Por lo cual, teniendo en cuenta que esta estación representa zonas urbanas pobladas de la

ciudad y es la estación más próxima al proyecto, resulta importante destacar que se prevé

un **aumento no significativo en la condición basal registrada en esta estación y**

**que la puesta en marcha del proyecto, no representa un empeoramiento**

**sustancial de la calidad del aire.**

**Concepción** **Chile** **Santiago** **Chile**
Los Pensamientos 197, San Pedro Av. del Valle Sur 512 Oficina 304
de la Paz Ciudad Empresarial, Huechuraba
(56-41)2287848 (56-2)23494104
www.dss.cl

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

## 7 Análisis de incertidumbre

**Página 122 de**

**132**

Tal como se plantea en la “Guía para el Uso de Modelos de Calidad del Aire en el SEIA”

(2012) de manera textual “cualquier modelo (meteorológico o de calidad del aire) representa

una aproximación a la realidad y, en consecuencia, sus resultados tienen incertidumbres

asociadas” [3] . Ante lo cual, para cuantificar esta incertidumbre, se realiza un análisis entre los

valores entregados por el modelo WRF (valores meteorológicos) y valores observados, en

este caso los datos son extraídos de la Estación Codelco - Machalí, propiedad de la Red

Agrometeorológica del Instituto de Investigaciones Agropecuarias (INIA); estación

meteorológica más cercana al proyecto y con datos disponibles para el año 2021, mismo

año de simulación del modelo WRF.

El modelo WRF simuló las condiciones meteorológicas dentro de un rango de 57 x 57 celdas

de una dimensión de 1 x 1 km. Para efectos del análisis del ajuste de los datos

meteorológicos simulados se seleccionó una celda en donde se ubica la estación Codelco

Machalí desde la cual se extrajeron los datos y se compararon con los valores observados

de la estación meteorológica antes mencionada.

La correlación de los datos se determinó a través del ajuste por mínimos cuadrados, método

en el que existen dos parámetros de importancia: coeficiente de correlación lineal de

Pearson (r) y el coeficiente de determinación (R [2] ).

El coeficiente de correlación lineal es una medida de relación de Pearson entre dos variables

y se usa para medir el grado de relación entre ellas. El rango de valores va desde el -1 al 1

y está representado por la siguiente ecuación.

r =
xy

σ xy

σ x ∙σ y

Donde,

 - σ xy, es la covarianza entre x e y;

 - σ x, es la desviación estándar de x;

3 Texto extraído del primer párrafo de la página 38, acápite 7 de la Guía para el Uso de Modelos de
Calidad del Aire en el SEIA (2012)

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

- σ y, es la desviación estándar de y;

**Página 123 de**

**132**

El coeficiente de determinación se utiliza como medida de eficiencia de la cobertura de datos

midiendo el porcentaje de variación entre las variables observadas y modeladas, es decir,

testea la capacidad predictiva del modelo e indica la proporción de la varianza de los

resultados que puede ser explicado por el modelo. Los valores del coeficiente de

determinación varían de 0 a 1, siendo este último el valor óptimo y está determinada por la

siguiente relación.

R [2] = r xy2 = σ xy
~~(~~ σ x ∙σ y

) 2

Donde,

 - σ xy, es la covarianza entre x e y;

 - σ x, es la desviación estándar de x;

 - σ y, es la desviación estándar de y;

Además, se presenta el análisis de tendencia de los valores modelados a estar

sobredimensionados o subdimensionados respecto de los observados, a través del percent

bias (PBIAS), el valor óptimo es 1 y su cálculo se realiza según la siguiente ecuación.

PBIAS= [

∑ ni=1 O i

∑ ni=1 (S i −O i )

~~]~~

Donde,

 - S i, es el valor simulado;

 - O i, es el valor observado.

Los resultados del ajuste del modelo meteorológico se presentan en la siguiente tabla. Luego

de ésta, se presenta el detalle de los valores entregados.

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 124 de**

**132**

**Tabla 27. Estadísticos de variables meteorológicas modeladas.**

|Variable|Coeficiente de<br>correlación lineal<br>(r)|Coeficiente de<br>determinación (R2)|Percent bias<br>(PBIAS)|
|---|---|---|---|
|Temperatura horaria|0,91|0,82|-0,32|
|Velocidad del viento horaria|0,45|0,20|-1,03|
|Componente zonal del viento|0,69|0,48|-|

**7.1** **Temperatura**

En la Figura 65 se observa la correlación entre la temperatura horaria observada desde la

estación Codelco - Machalí respecto a la modelada por el modelo WRF del año 2021.

**Figura 65. Correlación entre temperaturas observadas y modeladas.**

Respecto a la figura anterior se observa que la correlación entre la temperatura horaria

observada en la estación Codelco y la temperatura horaria modelada por el modelo WRF en

el año 2021, es directa y positiva con un coeficiente de correlación lineal de 0,91. Por otro

lado, el coeficiente de determinación sugiere que el modelo es capaz de simular el 82% de

las temperaturas horarias observadas de forma óptima.

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 125 de**

**132**

En la Figura 66, se observa la frecuencia de las temperaturas horarias en rangos de clases

tanto para los datos observados como modelados. A partir del grafico se desprende que, si

bien el modelo es capaz de reproducir de buena manera la variabilidad temporal de la

temperatura, su calidad disminuye frente a valores extremos. Es visible además que el

modelo sobreestima las temperaturas en el rango 0 - 20°C, mientras que subestima las

temperaturas entre los 20 - 30°C. Con todo esto, el valor del percent bias concluye, que en

general, los datos modelados se encuentran un 1% sobreestimados en relación con los

observados.

**Figura 66. Frecuencia de temperaturas observadas y modeladas.**

**7.2** **Velocidad del viento**

En la Figura 67 se observa la correlación entre la velocidad del viento horaria observada

desde la estación Codelco - Machalí, respecto a la modelada por el modelo WRF del año

2021.

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 126 de**

**132**

**Figura 67. Correlación entre velocidad del viento observada y modeladas.**

Respecto a la figura anterior se observa que la correlación entre la velocidad del viento

horaria observada y la modelada por el modelo WRF en el año 2021, es positiva con un

coeficiente de correlación lineal correspondiente a 0,45. Por otro lado, el coeficiente de

determinación sugiere que el modelo es capaz de simular el 20% de las velocidades del

viento horarias de forma óptima en la estación, en consecuencia, el modelo no se ajusta

fielmente a los datos observados.

En la Figura 68 se observa la frecuencia de la velocidad del viento horaria en rangos de

clases tanto para los datos observados como modelados. En efecto, el modelo claramente

sobreestima los valores de velocidad del viento menores a los 2,1 m/s y subestima la

frecuencia de vientos de mayor intensidad, siendo particularmente notorio entre los 5,7 y

8,8 m/s. Esto demuestra que, de acuerdo con los datos observados, el área de estudio existe

una fuerte influencia de vientos de alta intensidad. Esto es relevante para las

concentraciones de contaminantes que se modelan, ya que, al presentarse menores

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 127 de**

**132**

velocidades de viento, ocurre menor dispersión de estos contaminantes. Esto genera que

las concentraciones modeladas sean mayores a las que se podrían presentar en la realidad,

evaluando así, un escenario conservador.

**Figura 68. Frecuencia de velocidad del viento observadas y modeladas.**

**7.3** **Componente zonal del viento**

La componente zonal, a la que se denomina u, es la componente de la velocidad horizontal

a lo largo de un círculo de latitud, en dirección Oeste a Este. Es decir, u es positiva cuando

apunta hacia el Este, que sería el sentido positivo de nuestro eje x si dibujamos en un

sistema de coordenadas cartesianas.

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 128 de**

**132**

**Figura 69. Frecuencia de velocidad del viento observadas y modeladas.**

En la Figura 69 podemos observar cómo se relacionan la componente zonal observada con

la modelada. En concreto, se obtuvo que la correlación entre ambas fue de un 0,69 lo que

implica que el modelo es capaz de representar un 48% del comportamiento observado.

**7.4** **Test de Bondad de Ajuste sobre el Modelo Meteorológico**

Se prescindirá de la aplicación de test de bondad de ajuste entre los datos modelados y los

observados, debido a que los datos modelados no provienen de una muestra sobre la cual

se ha supuesto una distribución de probabilidad específica, como, por ejemplo: log normal,

binomial, Bernoulli, etc., sino que son el resultado de la simulación a través de la

implementación de un modelo matemático.

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 129 de**

**132**

## 8 Conclusión

Se estudió la concentración de las emisiones producto de la operación, proyectadas para el

año 4 del proyecto **“Brisas de Machalí II”** ubicado en la comuna de Machalí, región del

Libertador Bernardo O’Higgins. De esta forma, fueron modeladas las emisiones MP10,

MP2,5, NO 2, SO 2 y CO a fin de determinar las concentraciones que éstos tendrán en la

atmósfera, además de prever posibles efectos a la salud de las personas.

Tal como se abordó anteriormente en el informe, el desplazamiento de los contaminantes

ocurre mayoritariamente al interior de la zona de emplazamiento del proyecto y en las

proximidades del proyecto. Al respecto se destaca que:

 Las plumas de material particulado MP10 Y MP2,5 poseen su mayor concentración

en la situación basal del proyecto, donde se generan emisiones por calefacción

domiciliaria durante los meses fríos del año. También presenta una dispersión de las

emisiones en la zona de emplazamiento de las rutas internas del proyecto, donde se

encuentra el camino pavimentado por el cual transitan los vehículos livianos.

 En cuanto a los gases modelados, casi todos presentan un comportamiento similar

al material particulado, presentando las mayores concentraciones en la zona de la

situación basal del proyecto, influenciado principalmente por la combustión a leña

que allí se realiza. Por el contrario, la pluma de emisión del dióxido de nitrógeno

como norma horaria se concentra en el centro del proyecto, donde se realiza en

tránsito interno de los vehículos, demostrando la predominancia de esta actividad

por sobre la combustión a leña, la cual solamente se realiza durante un semestre al

año.

 Los receptores dentro del polígono del proyecto son los que presentaron las

concentraciones más altas, lo cual se condice con que es en esta misma zona donde

se emiten los contaminantes estudiados.

 Por otra parte, respecto a los receptores externos un total de 7 receptores se

encuentran dentro de las plumas generadas, siendo el R18 el que se encuentra

expuesto a las mayores concentraciones de los distintos contaminantes. De todas

maneras, las concentraciones no representan un peligro para la salud del receptor.

El análisis de la variación de la concentración demuestra que la ejecución del **proyecto no**

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 130 de**

**132**

**representa una perturbación respecto a las concentraciones que actualmente se**

**registran en la estación de monitoreo analizada.** De hecho, se prevé un aumento

máximo de la condición basal de 0,07% correspondiente a las concentraciones horarias de

SO 2 en comparación al resto de los contaminantes para la Estación Rancagua I de propiedad

el SINCA.

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

producen debido a las diferencias entre lo simulado por el modelo meteorologico WRF y los

datos observados de la Estación Codelco - Machalí propiedad del INIA.

Finalmente, la modelación de las emisiones del proyecto de material particulado (MP10 y

MP2,5) y gases (NO 2, SO 2 y CO) resultaron ser de baja magnitud concluyendo que, el

funcionamiento del **proyecto no representa un riesgo significativo a la salud ni**

**calidad de vida de la población, según los criterios establecidos en la legislación**

**ambiental vigente**, toda vez que no trasgrede los criterios para la evaluación de la

generación o presencia del efecto, característica o circunstancia de la letra a) del Art. 11 de

la Ley 19.300, los cuales son:

A. **Superación de valores de exposición establecidos en normas de calidad**

**primaria.** Como se pudo observar, todas las concentraciones se encuentran bajo la

normativa vigente y que el aporte a la EMRP en donde se analiza el cumplimiento

normativo es mínimo.

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 131 de**

**132**

B. **Superación de valores de exposición establecidos en normas primarias de**

**calidad del ambiental de los Estados que señala el RSEIA.** No aplica su

análisis, ya que para todos los contaminantes analizados Chile tiene normas vigentes.

C. **Aumento del riesgo pre-existente.** Este análisis solo es aplicable al MP10 y

MP2,5 por cuyas concentraciones se encuentra declarado como saturado; si bien

existe un aporte a la concentración, se observa que no es alta magnitud y que no

supera los rangos de exposición sugeridos por la OMS. Adicionalmente el Titular del

proyecto tendrá la obligación de compensar sus emisiones de acuerdo al PDA

vigente, con lo que estará compensando el total de sus emisiones más un 20%

aportando en ésta misma proporción a disminuir el riesgo a la concentración pre

existente; en virtud de ellos el titular, propenderá en la medida de lo posible que la

compensación de las emisiones tengan lugar en las cercanías del proyecto, para

generar un efecto positivo en la misma zona.

D. **Superación del nivel de riesgo incremental aceptado para el caso de**

**contaminantes cancerígenos, considerando los niveles, frecuencia y**

**duración de la exposición.** No es aplicable al proyecto, pues éste no genera

emisiones de este tipo.

E. **Superación de valores referenciales para el caso de contaminantes no**

**cancerígenos, considerando los niveles, frecuencia y duración de la**

**exposición.** Como se mencionó anteriormente, el proyecto no genera

concentraciones en frecuencias de acuerdo a la exposición de cada contaminante

que sea peligroso para la salud de la población, estado todos dentro de los márgenes

del riesgo aceptable por la legislación chilena y la OMS.

**INFORME DE MODELACIÓN ATMOSFÉRICA DE**

**EMISIONES**
“PROYECTO INMOBILIARIO BRISAS DE MACHALÍ II”

**Página 132 de**

**132**

## 9 Bibliografía

Hernandez- Garces, A., J. Souto, A. Rodríguez, S. Saavera, J. Casares, 2015. Validation of

CALMET/CALPUFF models simulations around a large power plant stack, p. 51. Recuperado

el 27 de junio de 2016, desde

http://revistas.ucm.es/index.php/FITE/article/view/51192/47527

Hernández-Garces, A., U. Jáuregui-Haga, J. González, J. Caseres-Long, S. Saavedra, F.

Guzmán-Martínez, A. Torres-Valle, 2016. Aplicaciones del modelo lagrangiano de dispersión

atmosférica CALPUFF, Ciencias de la Tierra y el Espacio, enero-junio, Vol. 17, No 1, p. 37.

ISSN 1729-3790. Recuperado el 29 de junio de 2016, desde

http://www.iga.cu/publicaciones/revista/assets/calpuffreview2.pdf.

Servicio de Evaluación Ambiental, 2012, Guía para el Uso de Modelos de Calidad del Aire en

el SEIA, p. 14-39. Recuperado el 01 de abril de 2016, desde

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

**Tabla 2.: Valores normados para NO** **2** **y SO** **2** **en Chile****

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

**Tabla 7.: Registro de días declarados en alerta, preemergencia y emergencia****

| Año | Días de alerta | Días de<br>preemergencia | Días de emergencia |
| --- | --- | --- | --- |
| 2014 | 16 | 3 | 0 |
| 2015 | 7 | 0 | 0 |
| 2016 | 10 | 2 | 0 |
| 2017 | 3 | 0 | 0 |
| 2018 | 4 | 1 | 0 |

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
| **Coordenadas del centroide** | **Latitud** | -34,19° |
| **Coordenadas del centroide** | **Longitud** | -70,73° |
| **DATUM** | **DATUM** | NWS - 84 |
| **Coordenadas del modelo** | **Coordenadas del modelo** | LCC |
| **Dominio de modelación** | **X ** | 57 |
| **Dominio de modelación** | **Y ** | 57 |
| **Dominio de modelación** | **Z ** | 10 |

**Tabla 16.: Coordenadas de modelación de las fuentes areales Fase de Operación****

| Actividad para<br>modelar | Unidad del<br>proyecto | Área (m2) | Coordenada UTM, HUSO 19 S,<br>DATUM WGS 84 | Col5 |
| --- | --- | --- | --- | --- |
| **Actividad para**<br>**modelar** | **Unidad del**<br>**proyecto** | **Área (m2) ** | **Este (m)** | **Norte (m)** |
| Ruta Pavimentada<br>Interna | P1 | 209 | 345.930 | 6.216.976 |
| Ruta Pavimentada<br>Interna | P1 | 209 | 345.933 | 6.216.978 |
| Ruta Pavimentada<br>Interna | P1 | 209 | 345.967 | 6.216.927 |
| Ruta Pavimentada<br>Interna | P1 | 209 | 345.969 | 6.216.929 |
| Ruta Pavimentada<br>Interna | P2 | 103 | 345.965 | 6.216.930 |
| Ruta Pavimentada<br>Interna | P2 | 103 | 345.967 | 6.216.927 |

**Tabla 17.: Frecuencia de la dirección de los vientos anual, WRF 2021.****

| Componente | Calmas | 0,5-2,1 | 2,1-3,6 | 3,6-5,7 | 5,7-8,8 | 8,8-11,0 | >11,0 | Porcentaje |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| N | 67 | 79 | 29 | 29 | 20 | 0 | 2 | 2,6% |
| NNE | 77 | 115 | 66 | 44 | 33 | 4 | 2 | 3,9% |
| NE | 91 | 155 | 126 | 127 | 48 | 7 | 3 | 6,4% |
| ENE | 55 | 72 | 71 | 145 | 52 | 0 | 2 | 4,5% |
| E | 25 | 32 | 20 | 43 | 19 | 3 | 2 | 1,6% |
| ESE | 38 | 10 | 8 | 6 | 1 | 0 | 0 | 0,7% |
| SE | 42 | 27 | 8 | 5 | 1 | 0 | 0 | 0,9% |
| SSE | 72 | 121 | 141 | 156 | 1 | 0 | 0 | 5,6% |
| S | 124 | 442 | 466 | 220 | 7 | 0 | 0 | 14,4% |
| SSO | 136 | 592 | 906 | 515 | 37 | 0 | 0 | 25,0% |
| SO | 92 | 362 | 469 | 471 | 73 | 0 | 0 | 16,7% |
| OSO | 40 | 144 | 239 | 371 | 191 | 1 | 0 | 11,3% |
| O | 41 | 33 | 52 | 158 | 30 | 1 | 0 | 3,6% |
| ONO | 32 | 30 | 6 | 4 | 2 | 0 | 0 | 0,8% |
| NO | 37 | 20 | 2 | 0 | 0 | 0 | 2 | 0,7% |
| NNO | 48 | 25 | 5 | 16 | 14 | 0 | 4 | 1,3% |

**Tabla 18.: Frecuencia de los vientos verano, WRF.****

| Componente | Calmas | 0,5-2,1 | 2,1-3,6 | 3,6-5,7 | 5,7-8,8 | 8,8-11,0 | >11,0 | Porcentaje |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| N | 10 | 19 | 4 | 1 | 1 | 0 | 0 | 1,6% |
| NNE | 10 | 27 | 2 | 1 | 1 | 0 | 0 | 1,9% |
| NE | 20 | 32 | 17 | 3 | 0 | 0 | 0 | 3,3% |

**Tabla 19.: Frecuencia de los vientos otoño, WRF.****

| Componente | Calmas | 0,5-2,1 | 2,1-3,6 | 3,6-5,7 | 5,7-8,8 | 8,8-11,0 | >11,0 | Porcentaje |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| N | 22 | 16 | 6 | 5 | 3 | 0 | 0 | 2,4% |
| NNE | 32 | 32 | 19 | 10 | 5 | 0 | 0 | 4,4% |
| NE | 31 | 52 | 31 | 33 | 5 | 1 | 0 | 6,9% |
| ENE | 20 | 25 | 19 | 27 | 12 | 0 | 0 | 4,7% |
| E | 9 | 8 | 3 | 4 | 3 | 1 | 0 | 1,3% |
| ESE | 14 | 1 | 2 | 3 | 0 | 0 | 0 | 0,9% |
| SE | 10 | 10 | 0 | 0 | 0 | 0 | 0 | 0,9% |
| SSE | 19 | 33 | 21 | 52 | 1 | 0 | 0 | 5,7% |
| S | 40 | 131 | 94 | 52 | 1 | 0 | 0 | 14,4% |
| SSO | 53 | 168 | 258 | 102 | 5 | 0 | 0 | 26,5% |
| SO | 36 | 118 | 140 | 73 | 3 | 0 | 0 | 16,8% |
| OSO | 12 | 40 | 62 | 92 | 11 | 0 | 0 | 9,8% |
| O | 12 | 7 | 14 | 27 | 1 | 0 | 0 | 2,8% |
| ONO | 7 | 5 | 0 | 1 | 0 | 0 | 0 | 0,6% |
| NO | 9 | 4 | 0 | 0 | 0 | 0 | 0 | 0,6% |
| NNO | 14 | 5 | 1 | 4 | 5 | 0 | 0 | 1,3% |

**Tabla 20.: Frecuencia de los vientos invierno, WRF.****

| Componente | Calmas | 0,5-2,1 | 2,1-3,6 | 3,6-5,7 | 5,7-8,8 | 8,8-11,0 | >11,0 | Porcentaje |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| N | 21 | 29 | 16 | 14 | 11 | 0 | 1 | 4,2% |
| NNE | 26 | 38 | 38 | 29 | 24 | 3 | 2 | 7,2% |
| NE | 32 | 57 | 63 | 72 | 40 | 6 | 2 | 12,3% |
| ENE | 20 | 24 | 30 | 85 | 33 | 0 | 1 | 8,7% |

**Tabla 21.: Frecuencia de los vientos en primavera, WRF.****

| Componente | Calmas | 0,5-2,1 | 2,1-3,6 | 3,6-5,7 | 5,7-8,8 | 8,8-11,0 | >11,0 | Porcentaje |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| N | 14 | 15 | 3 | 9 | 5 | 0 | 1 | 2,2% |
| NNE | 9 | 18 | 7 | 4 | 3 | 1 | 0 | 1,9% |
| NE | 8 | 14 | 15 | 19 | 3 | 0 | 1 | 2,7% |

**Tabla 22.: Concentración modelada en puntos receptores con respecto a MP10** **y****

| Punto | Concentración MP10 (μg/m3) | Col3 | Concentración MP2,5(μg/m3) | Col5 |
| --- | --- | --- | --- | --- |
| **Punto** | **Anual** | **24 horas** | **Anual** | **24 horas** |
| R1 | 1,11 | 3,89 | 0,70 | 2,57 |
| **R2** | **1,52** | **4,36** | **1,18** | **3,61** |
| R3 | 1,31 | 4,03 | 0,88 | 2,79 |
| R4 | 1,37 | 4,04 | 1,03 | 3,35 |
| R5 | 1,29 | 4,16 | 0,94 | 3,01 |
| **R6** | **1,16** | **4,31** | **0,74** | **2,43** |
| **R7** | **1,15** | **4,58** | **0,71** | **2,78** |
| R8 | 1,10 | 3,64 | 0,78 | 2,80 |
| R9 | 0,63 | 1,70 | 0,46 | 1,42 |
| R10 | 0,96 | 3,51 | 0,56 | 2,08 |
| R11 | 1,08 | 4,22 | 0,56 | 2,09 |
| R12 | 0,75 | 3,10 | 0,46 | 1,85 |
| R13 | 0,83 | 3,75 | 0,37 | 1,77 |
| R14 | 0,14 | 0,31 | 0,06 | 0,17 |
| R15 | 0,90 | 3,59 | 0,36 | 1,49 |

**Tabla 23.: Concentración modelada en puntos receptores con respecto a NO** **2****

| Punto | Concentración NO (μg/m3)<br>2 | Col3 |
| --- | --- | --- |
| **Punto** | **Horario** | **Anual** |
| R1 | 8,47 | 0,78 |
| **R2** | **8,37 ** | **1,11 ** |
| R3 | 7,85 | 0,92 |
| R4 | 6,55 | 0,99 |
| R5 | 7,34 | 0,91 |
| **R6** | **9,02 ** | **0,79 ** |
| **R7** | **9,94 ** | **0,78 ** |
| R8 | 7,10 | 0,78 |
| R9 | 2,83 | 0,45 |
| R10 | 7,14 | 0,66 |
| R11 | 9,98 | 0,72 |
| R12 | 7,11 | 0,50 |
| **R13** | **10,05 ** | **0,54 ** |
| R14 | 1,10 | 0,10 |
| R15 | 9,24 | 0,60 |
| R16 | 8,33 | 0,42 |
| R17 | 1,31 | 0,15 |
| R18 | 2,57 | 0,22 |
| **R19** | **5,49 ** | **0,21 ** |
| R20 | 0,50 | 0,03 |
| **R21** | **5,69 ** | **0,22 ** |
| **R22** | **5,62 ** | **0,37 ** |
| R23 | 3,24 | 0,19 |
| R24 | 2,10 | 0,09 |
| R25 | 2,90 | 0,14 |
| R26 | 2,21 | 0,08 |
| R27 | 3,08 | 0,18 |
| R28 | 1,12 | 0,06 |
| R29 | 1,09 | 0,05 |
| R30 | 2,10 | 0,12 |

**Tabla 24.: Concentración modelada en puntos receptores con respecto a SO** **2** **.****

| Punto | Concentración SO (μg/m3)<br>2 | Col3 | Col4 |
| --- | --- | --- | --- |
| **Punto** | **Horario** | **Diaria** | **Anual** |
| R1 | 0,012 | 0,004 | 0,001 |

**Tabla 25.: Concentraciones de CO en puntos receptores****

| Punto | Concentración CO (mg/m3) | Col3 |
| --- | --- | --- |
| **Punto** | **Horario** | ** 8 horas** |
| R1 | 0,22 | 0,14 |
| **R2** | **0,34** | **0,21** |
| R3 | 0,22 | 0,14 |
| **R4** | **0,25** | **0,17** |
| R5 | 0,24 | 0,15 |
| R6 | 0,21 | 0,13 |
| **R7** | **0,27** | **0,14** |
| R8 | 0,23 | 0,15 |
| R9 | 0,12 | 0,08 |
| R10 | 0,19 | 0,12 |
| R11 | 0,18 | 0,11 |
| R12 | 0,18 | 0,10 |
| R13 | 0,17 | 0,09 |
| R14 | 0,02 | 0,01 |
| R15 | 0,14 | 0,07 |
| R16 | 0,13 | 0,07 |
| R17 | 0,04 | 0,02 |

**Tabla 27.: Estadísticos de variables meteorológicas modeladas.****

| Variable | Coeficiente de<br>correlación lineal<br>(r) | Coeficiente de<br>determinación (R2) | Percent bias<br>(PBIAS) |
| --- | --- | --- | --- |
| Temperatura horaria | 0,91 | 0,82 | -0,32 |
| Velocidad del viento horaria | 0,45 | 0,20 | -1,03 |
| Componente zonal del viento | 0,69 | 0,48 | - |
