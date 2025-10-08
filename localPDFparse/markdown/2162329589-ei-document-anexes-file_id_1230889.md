---
title: Sin título
author: Nicolas Sepulveda
date: D:20240506102000-04'00'
language: es
type: report
pages: 75
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - MODELACIÓN DE CONTAMINANTES ATMOSFÉRICOS “PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS LO AGUIRRE”
  - Contenidos
  - 1 Introducción
  - 2 Objetivos
  - 3 Marco Legal Regulatorio
  - 4 Justificación de los modelos utilizados en el estudio
  - 5 Metodología
  - 6 Resultados
  - 7 Análisis de incertidumbre
  - 8 Conclusión
  ... y 1 secciones más
-->

# MODELACIÓN DE CONTAMINANTES ATMOSFÉRICOS “PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS LO AGUIRRE”

**ABRIL 2024**

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

# Contenidos

Página 2 de 75

1 Introducción ...................................................................................................................... 3

2 Objetivos ........................................................................................................................... 5
3 Marco Legal Regulatorio ..................................................................................................... 6
3.1 Estado de la Calidad del Aire de Pudahuel, Región Metropolitana de Santiago ................. 7
3.2 Análisis Estado de Calidad del Aire ............................................................................... 7

4 Justificación de los modelos utilizados en el estudio............................................................ 17

4.1 Uso modelo WRF ...................................................................................................... 17

4.2 Uso modelo CALPUFF ................................................................................................ 17

5 Metodología ..................................................................................................................... 20
5.1 Modelación de partículas ........................................................................................... 20
5.1.1 Modelación meteorológica .................................................................................. 20
5.1.2 Modelación de dispersión de contaminantes ........................................................ 21
5.1.3 Criterios para la modelación de partículas ........................................................... 23

6 Resultados ....................................................................................................................... 25

6.1 Estaciones meteorológicas cercanas ........................................................................... 25
6.2 Modelamiento meteorológico ..................................................................................... 26
6.2.1 Caracterización geofísica de la zona de estudio .................................................... 26
6.2.2 Caracterización de la rapidez y dirección de lo viento anual y estacional ................ 27
6.2.3 Caracterización de la temperatura del aire ........................................................... 35
6.2.4 Caracterización de la precipitación ...................................................................... 36
6.2.5 Altura capa de mezcla ........................................................................................ 37

6.3 Concentraciones Modeladas ....................................................................................... 39
6.3.1 Área de influencia del proyecto ........................................................................... 39
6.3.2 Dispersión de Material Particulado Respirable, MP10 ............................................ 40
6.3.3 Dispersión Material Particulado Fino Respirable, MP2,5 ........................................ 44
6.3.4 Modelación discreta de las emisiones contaminantes............................................ 48

7 Análisis de incertidumbre .................................................................................................. 53

7.1 Estación San Pablo-DASA .......................................................................................... 56

7.1.1 Caracterización de la temperatura modelada y observada. ................................... 56
7.1.2 Caracterización de la rapidez del viento modelada y observada. ........................... 60
7.2 Estación Pudahuel ..................................................................................................... 65

7.2.1 Caracterización de la temperatura modelada y observada. ................................... 65
7.2.2 Caracterización de la rapidez del viento modelada y observada. ........................... 68
8 Conclusión ....................................................................................................................... 73

9 Bibliografía ....................................................................................................................... 75

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 3 de 75

# 1 Introducción

El proyecto **“Planta de Tratamiento de Aguas Servidas Aguas Lo Aguirre”**, se ubica

en el sector Valle lo Aguirre en la comuna de Pudahuel, Región Metropolitana, como

podemos observar en la Figura 1.

**Figura 1. Ubicación del proyecto**

El presente proyecto denominado **“Planta de Tratamiento de Aguas Servidas Aguas**

**Lo Aguirre”**, consiste en la construcción de una Planta de Tratamiento de Aguas Servidas

(PTAS) que contempla la tecnología de lodos activados con un reactor de aireación

convencional y surge de la necesidad de brindar servicio de saneamiento al sector Valle Lo

Aguirre, ubicado en la comuna de Pudahuel, Región Metropolitana específicamente a un

costado de la Ruta 68. El objetivo de la planta es disponer las aguas servidas para el área

de concesión en conformidad al Plan de Desarrollo aprobado en la Superintendencia de

Servicios sanitarios (SISS) al año 2034.

La planta contempla las siguientes unidades

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 4 de 75

I. **Línea de Agua**

 - Planta elevadora de cabecera.

 Planta de pretratamiento compacto con el objetivo de separar los sólidos,

desarenado y desengrasado.

 - Cámara distribución de caudal de entrada.

 Cuatro reactores de aireación convencional (una zona anóxica y una zona

aireada).

 - Cámara distribución de caudal de salida.

 Dos sedimentadores con un tratamiento anóxico agitado y una segunda

recirculación.

 Sistema de desinfección compuesto de una cámara de contacto en la cual se

realizará la desinfección a través de la adición de cloro gas.

II. **Línea de Lodos**

 - Sistema de bombas RAS/WAS

 - Sala de deshidratado de lodos

 Encaladora (opcional)

Con este estudio se busca predecir la concentración de material particulado grueso y fino

(MP10 Y MP2,5), además de evaluar su contribución en puntos receptores de interés.

La modelación de las emisiones se realizó en base a los resultados obtenido de la

estimación de emisiones atmosférica. Considerando como escenario de máxima emisión el

primer año de construcción de la PTAS.

La evaluación de la dispersión y concentración de las emisiones de material particulado se

realizó mediante el programa CALPUFF, el cual es un modelo de dispersión usado

ampliamente para simulaciones de concentraciones ambientales de las emisiones

normales, con el objeto de establecer, desarrollar y analizar escenarios de emisión y

regulación. A su vez, CALPUFF es recomendado por el Ministerio de Medio Ambiente en la

“Guía para el Uso de Modelos de Calidad del Aire en el SEIA”, publicada el año 2023. Los

resultados y análisis de esta evaluación se presentan en el siguiente informe.

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 5 de 75

# 2 Objetivos

El presente informe, tiene como objetivo general cuantificar y evaluar el efecto en la

atmósfera debido a las emisiones de contaminantes generadas por el proyecto **“Planta**

**de Tratamiento de Aguas Servidas Aguas Lo Aguirre”** y cuantificar sus

concentraciones.

Para lo anterior se plantean los siguientes objetivos específicos:

 Evaluar en términos de concentración, el alcance de las emisiones de MP10 y

MP2,5 en la atmósfera.

 Evaluar la concentración de MP10 y MP2,5 en receptores que actualmente se

encuentren cercanos al proyecto y compararlo con los límites establecidos en el

Documento Técnico del SEA.

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

# 3 Marco Legal Regulatorio

Página 6 de 75

Actualmente, los contaminantes MP10 y MP2,5 están regulados bajo normas de calidad

primaria, cuyo objetivo es proteger la salud de las personas de los efectos agudos y

crónicos de la exposición de estos contaminantes con un riesgo aceptable. Para esto, se

fijan límites de concentración permitidos, condiciones de superación de la norma y los

niveles que dan paso a situaciones de emergencia ambiental.

El material particulado respirable MP10 es regulado por el D.S. 12/2022 del Ministerio del

Medio Ambiente, mientras el material particulado fino respirable MP2,5 es regulado por el

D.S. 12/2011 del Ministerio del Medio Ambiente.

En la Tabla 1 se aprecian los valores del límite anual y diario para los contaminante MP10

y MP2,5, además de los rangos que dan origen a situaciones de alerta, preemergencia y

emergencia ambiental.

**Tabla 1. Valores normados para MP10 y MP2,5 en Chile.**

|Nivel|MP10 (μg/m3N)|MP2,5 (μg/m3)|
|---|---|---|
|**Concentración Anual**|50|20|
|**Concentración 24 horas**|130|50|
|**Alerta**|180-229|80-109|
|**Preemergencia**|230-329|110-169|
|**Emergencia**|330 o superior|170 o superior|

Fuente: En base a D.S. 12/2022 MMA y D.S. 12/2011 MMA

No obstante, la superación del límite normativo de MP10 no es motivo de condiciones de

superación de la noma, sino que se considera que la norma es incumplida bajo las

siguientes condiciones:

 - Cuando el promedio de la concentración anual de tres años consecutivos iguale o

supere los 50 μg/m3.

 - Si el percentil 98 (P98) de las concentraciones de 24 horas durante un año sea

igual o superior a 130 μg/m3.

 - Si durante un año se registrasen siete o más días cuya concentración sea mayor a

130 μg/m3.

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 7 de 75

En el mismo contexto, las condiciones de superación de la norma de MP2,5 son las que se

describen a continuación:

 - Cuando el promedio de la concentración anual de tres años consecutivos iguale o

supere los 20 μg/m3.

 - Si el percentil 98 (P98) de las concentraciones de 24 horas durante un año sea

igual o superior a 50 μg/m3.

## 3.1 Estado de la Calidad del Aire de Pudahuel, Región Metropolitana de Santiago

El proyecto se emplaza dentro de la Región Metropolitana la cual a partir del D.S 131 de

1996 se encuentra saturada por MP10 y PTS como concentración diaria, monóxido de

carbono como concentración 8 horas y latente por dióxido de nitrógeno como

concentración anual. Además, que mediante el D.S. 67 de 2014, esta se encuentra

saturada como concentración 24 horas por MP2,5, lo anterior debido a la superación de

diversas estaciones de la red de monitoreo pertenecientes a la Región Metropolitana de

Santiago.

En la siguiente tabla se presentan las estaciones que se encuentran más próximas al

proyecto con la cual se caracterizará la situación basal para los contaminantes criterios

analizados en el presente informe correspondientes a MP10 y MP2,5.

**Tabla 2. Estaciones conectadas a la red SINCA cercanas al emplazamiento del**

**proyecto.**

|Estación|Contaminantes|Rango de datos|Distancia al<br>proyecto (km)|
|---|---|---|---|
|**Pudahuel**|MP10 y MP2,5|2014 a la actualidad|7,4|
|**Cerrillos II**|MP10 y MP2,5|Abril 2022 a la actualidad|8,5|

Fuente: Elaboración propia en base a los datos dispuestos en el Sistema Nacional de Calidad del

Aire (SINCA).

## 3.2 Análisis Estado de Calidad del Aire

Para llevar a cabo el siguiente análisis, se utilizaron las estaciones Pudahuel y Cerrillos, las

cuales se visualizan en la siguiente imagen.

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

**Figura 2. Ubicación EMRP**

Página 8 de 75

El D.S. 12/2022 MMA establece la norma primaria de calidad ambiental para material

particulado respirable MP10, regulando la concentración promedio anual y diaria.

En la Figura 3 se observa que el percentil 98 de la concentración promedio 24 horas

supera el límite establecido por la norma primaria de calidad del aire para MP10 en todo el

periodo analizado en la estación Pudahuel. Mientras que en Figura 4 se observa las

concentraciones medidas en la estación Cerrillos II donde también se evidencia superación

en el año de análisis.

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 9 de 75

**Figura 3. Concentración promedio 24 horas de MP10, EMRP Pudahuel.**

**Figura 4. Concentración promedio 24 horas de MP10, EMRP Cerrillo II.**

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 10 de 75

Con relación a la concentración promedio anual de MP10 también se observa que esta es

superada en todo el periodo analizado para la estación Pudahuel, lo mismo ocurre para el

año con data disponible para la estación Cerrillos II.

**Tabla 3. Porcentaje de superación concentración promedio anual de MP10,**

**EMRP Pudahuel.**

|Año|Concentración<br>Promedio Anual<br>(μg/m3)|Límite normativo D.S.<br>12/2022 MMA (μg/m3N)|Porcentaje de excedencia<br>de la norma (%)|
|---|---|---|---|
|2014|63,63|50,0|27|
|2015|73,67|73,67|47|
|2016|69,52|69,52|39|
|2017|65,21|65,21|30|
|2018|58,64|58,64|17|
|2019|72,56|72,56|45|
|2020|62,98|62,98|26|
|2021|63,26|63,26|27|
|2022|64,71|64,71|29|
|2023|65,59|65,59|31|

**Tabla 4. Porcentaje de superación concentración promedio anual de MP10,**

**EMRP Cerrillos II.**

|Año|Concentración<br>Promedio Anual<br>(μg/m3)|Límite normativo D.S.<br>12/2022 MMA (μg/m3N)|Porcentaje de excedencia<br>de la norma (%)|
|---|---|---|---|
|2023|68,91|50,0|38|

En la Figura 5 se presenta la concentración promedio trianual de MP10 de la Estación

Pudahuel, donde se evaluó la concentración para ocho periodos comprendidos entre 2014

a 2023. De esta se observa que la estación excede el límite normativo durante todos los

periodos, además se destaca que las concentraciones se mantienen relativamente

constantes, con valores en torno a 64 μg/m3. Cabe señalar que dada la cantidad de data

disponible no es posible realizar esta caracterización para la estación Cerrillos II.

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 11 de 75

**Figura 5. Concentración Promedio Trianual de MP10, EMRP Pudahuel.**

En relación con los días de alerta, preemergencia y/o emergencia en el año analizado, se

registraron 30 días de alerta, 5 de premergencia y 0 de emergencia ambiental en la

estación Pudahuel, siendo aquel que presenta mayor cantidad de días con este tipo de

declaraciones el 2015 tal como se muestra en la Tabla 4. Con relación a la estación

<!-- INICIO TABLA 4. -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |2020|62,98|62,98|26| |2021|63,26|63,26|27| |2022|64,71|64,71|29| |2023|65,59|65,59|31| -->

**Tabla 4.: Porcentaje de superación concentración promedio anual de MP10,****

| Año | Concentración<br>Promedio Anual<br>(μg/m3) | Límite normativo D.S.<br>12/2022 MMA (μg/m3N) | Porcentaje de excedencia<br>de la norma (%) |
| --- | --- | --- | --- |
| 2023 | 68,91 | 50,0 | 38 |

<!-- Estadísticas: 1 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- En la Figura 5 se presenta la concentración promedio trianual de MP10 de la Estación Pudahuel, donde se evaluó la concentración para ocho periodos comprendidos entre 2014 -->
<!-- FIN TABLA 4. -->


Cerrillos estos días corresponden a 3 días de alerta evidenciados en año 2023, único con

data disponible.

**Tabla 5. Registro de días declarados en alerta, preemergencia y emergencia**

**para MP10, EMRP Pudahuel**

|Año|Días de alerta|Días de preemergencia|Días de emergencia|
|---|---|---|---|
|2014|4|0|0|
|2015|6|3|0|
|2016|0|0|0|
|2017|2|0|0|
|2018|1|0|0|
|2019|6|2|0|

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 12 de 75

|Año|Días de alerta|Días de preemergencia|Días de emergencia|
|---|---|---|---|
|2020|1|0|0|
|2021|5|0|0|
|2022|1|0|0|
|2023|4|0|0|

**Tabla 6. Registro de días declarados en alerta, preemergencia y emergencia**

**para MP10, EMRP Cerrillos II**

|Año|Días de alerta|Días de preemergencia|Días de emergencia|
|---|---|---|---|
|2023|3|0|0|

Fuente: Elaboración propia en base a los datos dispuestos en el Sistema Nacional de Calidad del

Aire (SINCA).

El D.S. 12/2011 MMA establece la norma primaria de calidad ambiental para material

particulado fino respirable MP2,5, regulando la concentración promedio anual y diaria.

En la siguiente figura, se observa el percentil 98 de las concentraciones promedio de 24

horas registradas entre los años 2014 - 2023 para la estación Pudahuel, donde se

visualiza que existe superación de la normativa durante todo el periodo analizado, siendo

el año 2015 el que presenta la mayor concentración en 24 horas con una superación de la

norma en 105,9 μg/m [3] . Por su parte, la estación Cerrillos II para el año 2023 presenta una

concentración 70,6 μg/m [3] de superando también el límite normativo vigente.

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 13 de 75

**Figura 6. Concentración Promedio 24 horas de MP2,5, EMRP Pudahuel**

**Figura 7. Concentración Promedio 24 horas de MP2,5, EMRP Cerillos II**

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 14 de 75

La concentración promedio anual de MP2,5 que establece el D.S. 12/2011 MMA para los

años analizados es superada durante el período 2014 - 2022, siendo el año 2015

nuevamente el de mayor superación con un 68%.

**Tabla 7. Concentración promedio anual de MP2,5, EMRP Pudahuel**

|Año|Concentración<br>promedio anual<br>(μg/m3)|Límite normativo D.S.<br>12/2011 MMA (μg/m3)|Porcentaje de excedencia<br>de la norma (%)|
|---|---|---|---|
|2014|28,80|20|44|
|2015|33,56|33,56|68|
|2016|32,39|32,39|62|
|2017|28,45|28,45|42|
|2018|26,87|26,87|34|
|2019|26,84|26,84|34|
|2020|24,07|24,07|20|
|2021|26,27|26,27|31|
|2022|24,84|24,84|24|
|2023|28,80|28,80|44|

De la Tabla 8 se observa que en la estación Cerrillos II la concentración promedio anual

de MP2,5 para el año 2023.

**Tabla 8. Porcentaje de superación concentración promedio anual de MP2,5,**

**EMRP Cerrillos II**

|Año|Concentración<br>promedio anual<br>(μg/m3)|Límite normativo D.S.<br>12/2022 MMA (μg/m3N)|Porcentaje de excedencia<br>de la norma (%)|
|---|---|---|---|
|2023|25,26|20|11|

En la Figura 8 se presenta la concentración promedio trianual de MP2,5 de la Estación

Pudahuel, donde se evaluó la concentración promedio trianual de MP2,5 para el periodo

comprendido entre 2014 a 2023, de esta se observa que durante todos los periodos la

concentración excede la normativa vigente de 20 μg/m3. Con relación a la estación

Cerrillos II y al igual que lo ocurrido para MP10, esto no fue posible de caracterizar, dado

que únicamente existe un año de data.

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 15 de 75

**Figura 8. Concentración Promedio Trianual de MP2,5, EMRP Pudahuel**

En relación con los días de alerta, preemergencia y/o emergencia de los años analizados,

en la Tabla 9 se observa que en la estación Pudahuel se registraron un total de 57 días de

alerta, 17 días de preemergencia y 1 día de emergencia en la secuencia temporal

analizada, siendo el año 2015 el que concentra las peores condiciones, por su parte en la

estación Cerrillos II para el año 2023 se registró 1 día de alerta tal como se ve en la Tabla

10.

**Tabla 9. Registro de días declarados en alerta, preemergencia y emergencia**

**para MP2,5, EMRP Pudahuel**

|Año|Días de alerta|Días de preemergencia|Días de emergencia|
|---|---|---|---|
|2014|7|3|0|
|2015|16|4|1|
|2016|4|4|0|
|2017|1|0|0|
|2018|1|2|0|
|2019|8|0|0|

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 16 de 75

|Año|Días de alerta|Días de preemergencia|Días de emergencia|
|---|---|---|---|
|2020|0|1|0|
|2021|9|2|0|
|2022|4|0|0|
|2023|2|1|0|

**Tabla 10. Registro de días declarados en alerta, preemergencia y emergencia**

**para MP2,5, EMRP Cerrillos II**

|Año|Días de alerta|Días de preemergencia|Días de emergencia|
|---|---|---|---|
|2023|1|0|0|

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 17 de 75

# 4 Justificación de los modelos utilizados en el estudio

El Servicio de Evaluación Ambiental en la “Guía para el Uso de Modelos de Calidad del Aire

en el SEIA” (2023) hace una serie de recomendaciones para la modelación de

contaminantes primarios y secundarios en el aire. En la actualidad, esta guía es el único

documento existente como parámetro para la modelación de calidad del aire y tiene como

objetivo uniformar los criterios, exigencias técnicas y antecedentes para la evaluación de

los impactos asociados a este componente de proyectos que ingresen al Servicio de

Evaluación Ambiental. Dentro de las recomendaciones de la guía está el uso del modelo de

dispersión CALPUFF y sugiere la utilizar el modelo meteorológico WRF, los cuales fueron

utilizados en la modelación de las partículas del proyecto.

A continuación, se presenta la justificación de los modelos utilizados en el proyecto para

ejecución de la modelación de dispersión y concentración de emisiones partículas en el

aire.

## 4.1 Uso modelo WRF

El modelo Weather Research and Forecasting (WRF), es un modelo numérico de cuatro

dimensiones, recomendado para la generación de datos meteorológicos y es uno de los

modelos de pronóstico meteorológicos más avanzados.

Debido a la falta de una red robusta de estaciones meteorológicas, la “Guía para el Uso de

Modelos de Calidad del Aire en el SEIA” recomienda el uso de WRF por sobre el uso del

CALMET. Además, el mismo documento, sugiere el uso del WRF para la modelación de

dispersión de contaminantes con CALPUFF.

## 4.2 Uso modelo CALPUFF

La modelación de dispersión atmosférica de partículas provenientes del proyecto se realizó

con un modelo tipo “Puff”, específicamente el modelo CALPUFF. Tal como lo define la

guía, los modelos tipo “puff” son una combinación entre los modelos Gaussianos y los

modelos Lagrangeanos, en el sentido de que esencialmente calculan la dispersión de

contaminantes provenientes de una emisión instantánea, llamada “puff”, a lo largo de una

trayectoria. Su aproximación matemática consiste en estimar la dispersión en forma

Gaussiana en cada punto de una trayectoria; es decir, los modelos tipo “puff” sólo

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 18 de 75

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

g exp

~~[~~ [−d] 2σ x [2][a]

∑exp ~~[~~ [−(H] [e] 2σ [+ 2nh)] z [2] [2]

2 2

[−d] 2σ x [2][a] ~~[]]~~ [ exp] ~~[[]~~ [−d] 2σ y [2][c]

2

∞

n=−∞

[+ 2nh)] [2]

2σ z [2] ~~]~~

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 19 de 75

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

de las emisiones de partículas generadas por la futura construcción del proyecto.

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 20 de 75

# 5 Metodología

## 5.1 Modelación de partículas

La modelación de partículas depende en gran parte de las tasas de emisión. Estos son

acoplados a un modelo meteorológico, el que en sí mismo simula las condiciones

meteorológicas para la zona de estudio con una resolución temporal de 1 hora; con estos

factores como variable de entrada al modelo, es simulada la dispersión de las partículas en

un modelo, que determinará la trayectoria de las partículas dentro del área de estudio.

5.1.1 Modelación meteorológica

Para la modelación meteorológica, se utilizó un modelo WRF, construido con datos del año

2022 y resolución de 1 km, de extensión 72 km x 60 km. El modelo WRF es capaz de

simular el comportamiento meteorológico, a través de datos meteorológicos para el año

de estudio, el que posteriormente es interpolado dentro del área de estudio del modelo de

acuerdo con la topografía del lugar; en la siguiente tabla se presentan las coordenadas del

WRF en cada vértice y su centroide. En la Figura 9, se observa el dominio de la

modelación del WRF.

**Tabla 11. Características del modelo WRF**

|Vértice|Latitud|Longitud|
|---|---|---|
|Noroeste|33,31°S|71,17°O|
|Suroeste|33,97°S|71,17°O|
|Noreste|33,31°S|70,37°O|
|Sureste|33,97°S|70,37°O|
|Centroide|33,64°S|70,77°O|

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

**Figura 9. Dominio de Modelo WRF**

5.1.2 Modelación de dispersión de contaminantes

Página 21 de 75

El modelo CALPUFF permite la simulación de la dispersión de contaminantes bajo dos

modalidades:

 **Modelación de la grilla de modelación** . La grilla de modelación viene seteada

del modelo meteorológico, acotando la simulación en la zona circundante más

próxima al proyecto, incluyendo las zonas pobladas importantes de evaluar. Dicha

grilla de modelación tiene una resolución espacial de 1 km

Este es el método más usual para la interpolación de las concentraciones de los

puntos de grilla (1 km), interpolando entre cada punto la concentración, hasta

obtener la pluma de dispersión.

En virtud de la resolución espacial del modelo y de la altura de la primera capa de

modelación, y al tratarse de áreas de emisión que se generan a altura del suelo o a baja

altura, muchas veces la obtención de la pluma de dispersión se genera con valores sub

dimensionados, por lo tanto, en ocasiones es necesario realizar una sub grilla de

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 22 de 75

modelación a través de la modelación de puntos discretos, aumentando la densidad de

puntos de modelación y mejorando la evaluación de la concentración simulada dentro del

espacio circundante. De este modo, se generó una subgrilla de 20 m x 20 m en el área de

emplazamiento del proyecto, una grilla de resolución de 50 m x 50 m en un área de 500 m

alrededor de la planta y finalmente una grilla de 250 m x 250 m en un área de 2000

metros alrededor de la grilla de 50 m.

**Figura 10. Subgrilla utilizada para crear las plumas de dispersión**

 **Modelación de puntos discretos.** Se consideraron 16 puntos discretos cercanos

al proyecto. A continuación, se presenta en la Tabla 12 las coordenadas, y en la

Figura 11 la distribución espacial de los receptores discretos.

**Tabla 12. Receptores cercanos al proyecto**

|Receptor|Coordenada UTM HUSO 18 S (m)|Col3|Distancia desde la planta<br>(m)|
|---|---|---|---|
|**Receptor**|**Este**|**Norte**|**Norte**|
|R1|328.746,00|6.298.440,00|95,6|
|R2|328.793,00|6.298.395,00|124,5|
|R3|328.913,00|6.298.375,00|243,9|

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 23 de 75

|Receptor|Coordenada UTM HUSO 18 S (m)|Col3|Distancia desde la planta<br>(m)|
|---|---|---|---|
|**Receptor**|**Este**|**Norte**|**Norte**|
|R4|328.884,00|6.298.120,00|339,2|
|R5|329.093,00|6.298.276,00|437,6|
|R6|328.582,00|6.298.696,00|322,7|
|R7|328.310,00|6.298.706,00|480,3|
|R8|329.006,00|6.298.763,00|510,6|
|R9|329.283,00|6.298.506,00|623,9|
|R10|328.581,00|6.297.854,00|537,6|
|R11|329.348,00|6.298.690,00|746,1|
|R12|328.065,00|6.297.911,00|766,1|
|R13|328.965,00|6.299.236,00|869,0|
|R14|328.933,00|6.299.302,00|915,1|
|R15|329.032,00|6.299.690,00|1.335,7|
|R16|328.912,00|6.299.430,00|1.045,9|

**Figura 11. Receptores discretos**

5.1.3 Criterios para la modelación de partículas

El año 1 corresponde al año con mayor emisión del proyecto, donde se lleva a cabo la

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

etapa de construcción de la PTAS en su subfase I.

Página 24 de 75

Para la modelación se ingresaron los polígonos que representan el área de construcción en

el año 1, donde se ejecutan las actividades de demolición, excavación, erosión en pila de

acopio, carga de material y uso de maquinaria los polígonos donde se genera el tránsito

en rutas no pavimentadas al interior del proyecto y los polígonos representantes del

tránsito pavimentado que dan acceso al proyecto.

Adicionalmente, se modelaron las emisiones de gases precursores de MP10 y MP2,5 en el

aire a través del módulo MESOPUFF II.

De acuerdo con la metodología aplicable, se realizaron polígonos representativos de cada

unidad para la simulación de las áreas de emisiones de partículas las que, fueron

modeladas como fuentes de emisión discontinuas, es decir, dentro del ciclo diurno, se

consideró la generación de emisiones durante 10 horas (8:00 a 17:00 hrs), ya que ese es

el horario laboral establecido para el proyecto.

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 25 de 75

# 6 Resultados

## 6.1 Estaciones meteorológicas cercanas

En la Figura 12 se observan las estaciones meteorológicas cercanas al proyecto. Podemos

notar que existen cuatro estaciones meteorológicas, pertenecientes a

AGROMETEOROLOGIA, cuyos nombres son: estación Chorrillo, estación Pudahuel, estación

Rinconada y estación San Pablo-Dasa.

**Figura 12. Ubicación estaciones meteorológicas cercanas al proyecto**

En la Tabla 13 se observan las distancias al proyecto y porcentajes de datos disponibles

para las variables de temperatura, precipitación, dirección del viento y magnitud del

viento, disponible para las estaciones Pudahuel, San Pablo-DASA y Rinconada. Se observa

que, a pesar de que la estación Rinconada es la más cercana (5,39 km), esta se encuentra

detrás de un cerro por lo que sus observaciones estarán influenciadas por el mismo, por

esta razón la estación rinconada no será considerada para realizar el análisis de

incertidumbre y en cambio se realizaran con las estaciones Pudahuel y San Pablo-DASA.

Se descarta la estación Chorrillo por ser la más lejana al proyecto.

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 26 de 75

**Tabla 13. Características de las estaciones meteorológicas cercanas al proyecto**

|Estación|Distancia<br>al<br>Proyecto<br>(km)|Año|Porcentaje de datos por Variable (%)|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**Estación**|**Distancia**<br>**al**<br>**Proyecto**<br>**(km) **|**Año**|**Temperatura**|**Precipitación**|**Dirección del viento**|**Magnitud del viento**|
|Pudahuel|7,67|2021|99,89|99,89|99,89|99,89|
|Pudahuel|7,67|2022|99,98|99,98|99,98|99,98|
|Pudahuel|7,67|2023|99,94|99,94|99,94|99,94|
|San<br>Pablo-<br>DASA|9,58|2021|96,32|96,51|96,51|96,51|
|San<br>Pablo-<br>DASA|9,58|2022|99,68|99,68|99,68|99,68|
|San<br>Pablo-<br>DASA|9,58|2023|96,32|96,51|96,51|96,51|
|Rinconada|5,39|2021|99,99|99,99|99,99|99,99|
|Rinconada|5,39|2022|100|100|100|100|
|Rinconada|5,39|2023|99,67|99,67|99,67|99,67|

Como no existe una estación meteorológica a una distancia menor a 5 km del proyecto, y

por lo tanto no se cuenta con una estación meteorológica representativa, se realizó la

caracterización meteorológica utilizando las salidas del modelo WRF.

## 6.2 Modelamiento meteorológico

A continuación, se presentan los resultados de la modelación meteorológica para el año

2022, los cuales se extrajeron del punto de grilla más cercano a la ubicación del proyecto.

6.2.1 Caracterización geofísica de la zona de estudio

En la Figura 13, se observa la elevación del terreno en el dominio de la modelación WRF,

La fuente de información topográfica del dominio de modelación corresponde a cartas

topográficas digitales adquiridos desde la base de “U.S.GeologicalSurvey (USGS)- Global

Multi-resolution Terrain Elevation Data 2010 (GMTED2010)” con curvas de nivel de

resolución 30 [arc-segundos], equivalente a 920 [m] aproximadamente. Se observa que,

el proyecto se ubica en la cota topográfica en torno a los 350 y 500 m s.n.m, lo cual es

concordante con la Figura 13.

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 27 de 75

**Figura 13. Elevación del terreno en el área de la modelación meteorológica**

6.2.2 Caracterización de la rapidez y dirección de lo viento anual y estacional

En esta parte de informe podemos ver distintas imágenes que representan la rosa de los

vientos y las frecuencias de la rapidez del viento construidas con las salidas del modelo

WRF, para el año 2022. En la Figura 14 y Figura 15 se observa la rosa de los vientos anual

y la frecuencia de la rapidez de los vientos anual, respectivamente. Además, en las Figura

16, Figura 17, Figura 18 y Figura 19 se presentan las rosas de los vientos construidas con

los datos para verano, otoño, invierno y primavera, respectivamente. Finalmente, en la

Figura 20, se presentan las imágenes A, B, C y D, las cuales corresponden a las

frecuencias de la rapidez del viento construida con los datos de verano, otoño, invierno y

primavera.

Podemos observar en la Figura 14 la rosa de los vientos anual, para el año 2022,

construida con las salidas del modelo WRF, utilizando el punto de grilla más cercano al

proyecto. En esta figura es posible notar como el viento predominante en el año es del sur

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 28 de 75

suroeste, del este sureste y oeste suroeste, los cuales abarcan el 34,3% de los orígenes

de los vientos totales. En particular, los vientos del suroeste corresponden a un 13,8% del

total, mientras que los vientos del este sureste representan un 10,64% y los vientos del

oeste suroeste un 9,82%. Además, podemos observar que otras direcciones son

ligeramente menos predominantes, como los vientos del nor noreste con 8,72% o los

vientos del noreste con un 7,83%.

**Figura 14. Rosa de vientos construida con las salidas del modelo WRF, para el**

**año 2022**

Con respecto a la frecuencia de la rapidez del viento anual, la cual se puede ver en la

Figura 15, podemos ver como predominan las calmas con un 37,7%, seguido con los

vientos entre 0,5-2,1 m/s y 3,6-5,7 m/s con un 34,2% y un 13,2% del total,

respectivamente. Cabe destacar que los vientos en el rango de 2,1-3,6 m/s poseen un

8.5% del total y los vientos que superan los 5,7 m/s representan el 6,4%.

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 29 de 75

**Figura 15. Frecuencia de la velocidad de los vientos anual construida con las**

**salidas del modelo WRF, para el año 2022**

Con respecto al análisis estacional de las rosas de viento, se observa que en verano

(Figura 16) los vientos predominantes son del suroeste, con un 24,4% de los orígenes de

los vientos totales, mientras que los vientos del oeste suroeste y este sureste con un

14,6% y 10,3, respectivamente. En otoño (Figura 17) se observa que los vientos de

distribuyen en mayores direcciones, las 5 direcciones más frecuentes son suroeste con un

13,58%, este sureste con un 11,54, nor noreste con un 9,6% y noreste con un 7,84%.

46%, este-sureste con un 9,65%, norte con un 9,56% y nor noroeste con un 8,61%.

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 30 de 75

**Figura 16.** **Rosa de vientos para el verano, construida con las salidas del modelo**

**WRF, para el año 2022**

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 31 de 75

**Figura 17. Rosa de vientos para el otoño, construida con las salidas del modelo**

**WRF, para el año 2022**

Se observa que en invierno (Figura 18) vemos que los vientos con una componente norte

se vuelven más predominantes, esto se traduce a que los origines de los vientos más

frecuentes sean nor noreste con un 10,46%, este-sureste con un 9,65%, norte con un

9,56% y nor noroeste con un 8,61%. Finalmente, en primavera (Figura 19) los orígenes

de los vientos predominantes son suroeste con un 13,87%, oeste suroeste con un 12,45%

y seste sureste con un 11,04%.

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 32 de 75

**Figura 18** . **Rosa de vientos para el invierno, construida con las salidas del**

**modelo WRF, para el año 2022**

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 33 de 75

**Figura 19. Rosa de vientos para la primavera, construida con las salidas del**

**modelo WRF, para el año 2022**

En la Figura 20 se observa la frecuencia de la rapidez del viento para cada los meses de

verano (A), otoño(B), invierno (C) y primavera (D). Podemos ver que en verano la

frecuencia predominante de vientos son las calmas, con un 32%, seguido por los vientos

entre 0,5 - 2,1 m/s y 3,6 - 5,7 m/s con un 28% y 19,3%. En otoño la rapidez del viento

predominantes se da en el rango entre 0,5 - 2,1 m/s con un 39,4%, seguido por las

calmas y los vientos en el rango de 12,2 - 5,7 m/s se observan un 38,5% y 12,2%,

respectivamente. En invierno se ve que predominan las calmas con un 37%, seguido por

los vientos entre 0,5 - 2,1 m/s y 3,6 - 5,7 m/s con un 30,9% y un 14,7, respectivamente.

Finalmente, en primavera, se observa que las calmas predominan con un 43,2%, seguido

de los vientos entre 0,5 - 2,1 m/s y 2,1 - 3,6 m/s con un 38,2 % y 8 %, respectivamente.

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 34 de 75

**Figura 20. Frecuencia de la rapidez del viento construida con los resultados del**

**modelo WRF, para el año 2022. Se calculo para el verano (A), otoño (B),**

**invierno (C) y primavera (D)**

6.2.2.1 Caracterización del ciclo diario del viento.

En la Figura 21 se presenta el perfil horario promedio de la magnitud y dirección del

viento, modeladas con WRF, para cada mes del año 2022.

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 35 de 75

**Figura 21. Ciclo Diario del Viento construido con la modelación WRF, para el**

**año 2022**

Se puede observar que, a lo largo del año, la intensidad del viento tiende a ser menor

entre las 00:00 y las 09:00 UTC. Posteriormente, esta intensidad aumenta gradualmente,

alcanzando velocidades superiores a los 5,0 m/s entre las 15:00 y 17:00 UTC, antes de

comenzar a disminuir y cerrar el ciclo diario. Este patrón se mantiene con consistencia a lo

largo de la mayoría del año, aunque presenta variaciones en la magnitud del viento. Cabe

destacar que, en los meses de invierno, las velocidades del viento suelen oscilar entre 0

m/s y 3,0 m/s.

6.2.3 Caracterización de la temperatura del aire

En la Figura 22 se presenta el perfil horario promedio de la temperatura modelada con

WRF, para cada mes del año 2022.

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 36 de 75

**Figura 22. Ciclo diario para la temperatura modelada usando WRF, para el año**

**2022**

En la Figura 22 podemos ver 2 ciclos muy claros y definidos. El primero de ellos

corresponde al ciclo diario, donde la temperatura experimenta un aumento gradual desde

las 06:00 UTC hasta las 13:00 UTC, para luego descender nuevamente. El segundo ciclo

observado es el ciclo estacional. Este ciclo modifica la pauta del ciclo diario a medida que

transitamos del verano al otoño e invierno, caracterizado por temperaturas más bajas y

una reducción en la duración de las horas en las que se alcanzan las temperaturas

máximas.

6.2.4 Caracterización de la precipitación

En la Figura 23 podemos observar la precipitación mensual modelada por WRF. Tenemos

que la precipitación anual es de 483,03 mm.

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 37 de 75

**Figura 23. Precipitación Mensual modelada usando WRF, para el año 2022**

Con respecto a la distribución mensual, se puede identificar claramente como en la zona

de emplazamiento del proyecto invierno (junio, julio y agosto) presenta los valores

máximos de precipitación donde junio posee 198,1 mm, mientras que abril y septiembre

muestran valores similares de precipitación con 33,5 mm y 33,1 mm respectivamente.

6.2.5 Altura capa de mezcla

En la Figura 24 se presenta el ciclo diario promedio, para cada mes del año, de la altura

de la capa limite modelada en la zona de emplazamiento del proyecto (medida en metros).

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 38 de 75

**Figura 24. Ciclo diario de altura de la capa limite modelada usando WRF, para el**

**año 2022**

Se observa como la capa limite tiene un claro ciclo diario, en donde las menores alturas se

alcanzan durante las 00:00 y las 07:00 UTC y entre las 17:00 y las 23:00 UTC, mientras

que entre las 08:00 y las 12:00 UTC aumenta paulatinamente hasta sus valores máximos

para luego disminuir hasta completar el ciclo.

En cuanto a la variación mensual del ciclo diario, se observa que durante los meses de

invierno se registran valores mínimos más elevados que perduran a lo largo del resto de

los meses. Además, se aprecia que las alturas de los máximos son inferiores durante este

periodo.

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

6.3 Concentraciones Modeladas

Página 39 de 75

A continuación, se presentan los resultados de la modelación de material particulado

emitidos a la atmosfera. Cabe recordar que, el escenario modelado corresponde a las

emisiones de material particulado, tanto MP10 como MP2,5, las cuales se producen en la

fase de construcción del proyecto durante el año 1.

6.3.1 Área de influencia del proyecto

En la siguiente figura se muestra el área de influencia simulada para el proyecto, la cual

fue evaluada asumiendo el peor escenario, a partir de la concentración promedio 24 horas

de MP10, de la cual se tiene lo siguiente:

- Las concentraciones modeladas, de acuerdo con la Guía de Calidad del Aire de la

OMS (2021) y el Criterio de Evaluación del SEIA 2023 son de baja magnitud y estima un

área de 1,72 ha.

- El área llega a concentraciones de 0,106 μg/m [3] como promedio 24 horas, valor

correspondiente al 0,08% de la norma (130 μg/m [3] ).

**Figura 25. Área de influencia**

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

6.3.2 Dispersión de Material Particulado Respirable, MP10

Página 40 de 75

A continuación, se presenta el análisis de los resultados para el MP10 tanto para la

concentración promedio anual como de 24 horas.

Es importante señalar que la pluma de dispersión de MP10 simulada por el modelo abarca

la zona de emplazamiento del proyecto, donde se produce la construcción del proyecto en

evaluación.

6.3.2.1 Concentración Promedio 24 horas de MP10

En la Figura 26, se muestra la pluma de dispersión de la concentración promedio diaria de

MP10 de donde se observa lo siguiente:

 La pluma de dispersión se distribuye tanto dentro como fuera del polígono del

proyecto, situando su máxima concentración en la zona donde se construirán las

obras, cabe señalar que, si bien se modelaron las obras asociadas a la construcción

de la impulsión, la temporalidad de las obras caracterizadas, simularon

concentraciones no significativas en esas zonas.

 La pluma de dispersión tiene una forma homogénea, distribuyéndose en las cuatro

direcciones de la rosa de los vientos.

 Las concentraciones modeladas van desde los 0,107 μg/m3 a 0,249 μg/m3 en la

zona circundante al proyecto.

 En relación con los puntos receptores elegidos se observa que ninguno se

encuentra dentro de la pluma de dispersión.

 La pluma se extiende 73,5 m al norte, 66,7 m al sur, 86,5 m al este y 80,9 m al

oeste desde la zona de máxima concentración, a estas distancias, las

concentraciones se reducen en un 57%.

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS LO AGUIRRE”

Página 41 de 75

**Figura 26. Dispersión de la pluma de MP10 como concentración de 24 horas**

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

6.3.2.2 Concentración Promedio Anual de MP10

Página 42 de 75

En la Figura 27, se muestra la pluma de dispersión de la concentración promedio anual de

MP10 de donde se concluye lo siguiente:

 La pluma de dispersión se distribuye de manera similar a la obtenida en la

simulación de la concentración promedio diario, situando su máxima concentración

en la zona donde se construirán las obras, cabe señalar que, si bien se modelaron

las obras asociadas a la construcción de la impulsión, la temporalidad de las obras

caracterizadas, simularon concentraciones no significativas en esas zonas.

 En la pluma de dispersión se observa un área de concentración mayor, cuyo rango

varía entre los 0,056 a 0,129 μg/m3.

 La pluma se extiende hasta los 59,4 m por el norte y 56 m al sur, 67,3 m al este y

68,9 m al oeste desde la zona de mayor concentración, en la cual se modelaron

aproximadamente 0,056 μg/m3.

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS LO AGUIRRE”

Página 43 de 75

**Figura 27. Dispersión de la pluma de MP10 como concentración promedio anual**

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

6.3.3 Dispersión Material Particulado Fino Respirable, MP2,5

Página 44 de 75

A continuación, se presenta el análisis de los resultados para el MP2,5, tanto para la

concentración promedio anual y 24 horas.

6.3.3.1 Concentración Promedio diaria MP2,5

En la Figura 28, se muestra la pluma de dispersión de la concentración promedio diaria de

MP2,5 de donde se concluye que:

 La pluma de dispersión de MP2,5 como norma diaria, al igual que lo ocurrido para

MP10, presenta sus mayores concentraciones en la zona donde se modela el

proyecto. Es importante mencionar que, si bien se modelaron las obras asociadas a

la construcción de la impulsión, la temporalidad de las obras caracterizadas,

simularon concentraciones no significativas en esas zonas.

 La concentración generada en la atmosfera de las emisiones de MP2,5 varía desde

los 0,101 a los 0,235 μg/m3.

 La pluma se extiende hasta los 72,9 m por el norte y 68,2 m al sur, 78 m al este y

86 m al oeste desde la zona de mayor concentración. A estas distancias la

concentración esperada es de 0,101 μg/m3.

 La zona de máxima concentración abarca una superficie de 0,19 hectáreas

 De los receptores identificados ninguno se emplaza dentro de la pluma.

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS LO AGUIRRE”

Página 45 de 75

**Figura 28. Dispersión de la pluma de MP2,5** **como concentración promedio diaria**

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

6.3.3.2 Concentración promedio anual de MP2,5

Página 46 de 75

En la Figura 29, se muestra la pluma de dispersión de la concentración promedio anual de

MP2,5 de donde se concluye que:

 El comportamiento del material particulado fino como concentración promedio

anual, concentra sus máximas concentraciones en el sector donde donde se

construirán las obras, cabe señalar que, si bien se modelaron las obras asociadas a

la construcción de la impulsión, la temporalidad de las obras caracterizadas,

simularon concentraciones no significativas en esas zonas.

 La concentración generada en la atmósfera por las emisiones de MP2,5 varían

desde los 0,053 a los 0,122 μg/m3.

 La pluma se extiende hasta los 57 m por el norte y 57 m al sur, 71 m al este y 70

m al oeste desde la zona de mayor concentración. A estas distancias la

concentración se reduce en un 56,5%.

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS LO AGUIRRE”

Página 47 de 75

**Figura 29. Dispersión de la pluma de MP2,5 como concentración promedio anual**

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

6.3.4 Modelación discreta de las emisiones contaminantes

Página 48 de 75

La modelación discreta de emisiones fue realizada tanto para la concentración de MP10 y

MP2,5, los valores de concentración para los puntos receptores son presentados a

continuación. Estos puntos están compuestos por receptores cercanos al proyecto.

Como el proyecto se emplaza en una zona que en la actualidad se encuentra con

declaratoria de saturación por MP10 y MP2,5 ambas como concentración diaria (D.S

N°131/1996 MINSEGPRES y D.S. N°67/2014 del MMA respectivamente) y además de

acuerdo a las concentraciones medidas en las estaciones cercanas al emplazamiento del

proyecto, se superan los límites normativos de material particulado fino y grueso en

ambos en su métrica anual (ver acápite 3.2), se prevé un riesgo pre-existe para la salud

de la población producidas en todas las concentraciones tal como lo señala el documento

técnico, “CRITERIO DE EVALUACIÓN EN EL SEIA: Impacto de emisiones en zonas

saturadas por material particulado respirable MP10 y material particulado fino respirable

MP2,5” (SEA, 2023). En virtud de lo anterior, se analizan las concentraciones modeladas a

partir del documento técnico antes mencionado, considerando como límite máximo de

concentración a emitir por el proyecto aquellas que aparecen en la Tabla 14, las cuales se

extrajeron de la Tabla 1 del documento técnico.

**Tabla 14. Criterio de valores de significancia sobre receptores humanos**

**aplicables para el proyecto, considerando 1 año.**

|Contaminante|Periodo|Incremento en la<br>concentración (μg/m3)|
|---|---|---|
|MP2,5|24 horas|1,71|
|MP2,5|Anual|0,33|
|MP10|24 horas|5,00|
|MP10|Anual|1,00|

Fuente: Tabla 2, del documento: “CRITERIO DE EVALUACIÓN EN EL SEIA: Impacto de emisiones

en zonas saturadas por material particulado respirable MP10 y material particulado fino respirable

MP2,5” (SEA, 2023).

A continuación, se presenta el análisis realizado para cada una de las métricas simuladas.

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 49 de 75

**Tabla 15. Análisis receptor y concentración MP2,5 24 horas (evaluación riesgo**

**pre-existente).**

|Receptor|Aporte proyecto<br>(μg/m3)|Límite establecido<br>Tabla 1 DT:Criterio<br>de Evaluación<br>(μg/m3)|¿Genera impacto?|
|---|---|---|---|
|R1|0,073|1,71|No|
|R2|0,070|0,070|No|
|R3|0,054|0,054|No|
|R4|0,044|0,044|No|
|R5|0,042|0,042|No|
|R6|0,048|0,048|No|
|R7|0,007|0,007|No|
|R8|0,043|0,043|No|
|R9|0,031|0,031|No|
|R10|0,030|0,030|No|
|R11|0,023|0,023|No|
|R12|0,022|0,022|No|
|R13|0,005|0,005|No|
|R14|0,007|0,007|No|
|R15|0,005|0,005|No|
|R16|0,002|0,002|No|
|PMI|0,246|0,246|No|

**Tabla 16. Análisis receptor y concentración MP2,5 Anual (evaluación riesgo pre-**

**existente).**

|Receptor|Aporte proyecto<br>(μg/m3)|Límite establecido<br>Tabla 1 DT:Criterio<br>de Evaluación<br>(μg/m3)|¿Genera impacto?|
|---|---|---|---|
|R1|0,025|0,33|No|
|R2|0,018|0,018|No|
|R3|0,010|0,010|No|
|R4|0,007|0,007|No|
|R5|0,006|0,006|No|
|R6|0,008|0,008|No|

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 50 de 75

|Receptor|Aporte proyecto<br>(μg/m3)|Límite establecido<br>Tabla 1 DT:Criterio<br>de Evaluación<br>(μg/m3)|¿Genera impacto?|
|---|---|---|---|
|R7|0,001||No|
|R8|0,006|0,006|No|
|R9|0,005|0,005|No|
|R10|0,005|0,005|No|
|R11|0,004|0,004|No|
|R12|0,004|0,004|No|
|R13|0,001|0,001|No|
|R14|0,001|0,001|No|
|R15|0,001|0,001|No|
|R16|0,001|0,001|No|
|PMI|0,128|0,128|No|

**Tabla 17. Análisis receptor y concentración MP10 24 horas (evaluación riesgo**

**pre-existente).**

|Receptor|Aporte proyecto<br>(μg/m3)|Límite establecido<br>Tabla 1 DT:Criterio<br>de Evaluación<br>(μg/m3)|¿Genera impacto?|
|---|---|---|---|
|R1|0,080|5,00|No|
|R2|0,076|0,076|No|
|R3|0,059|0,059|No|
|R4|0,048|0,048|No|
|R5|0,046|0,046|No|
|R6|0,055|0,055|No|
|R7|0,009|0,009|No|
|R8|0,047|0,047|No|
|R9|0,034|0,034|No|
|R10|0,033|0,033|No|
|R11|0,025|0,025|No|
|R12|0,024|0,024|No|
|R13|0,008|0,008|No|
|R14|0,009|0,009|No|
|R15|0,009|0,009|No|

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 51 de 75

|Receptor|Aporte proyecto<br>(μg/m3)|Límite establecido<br>Tabla 1 DT:Criterio<br>de Evaluación<br>(μg/m3)|¿Genera impacto?|
|---|---|---|---|
|R16|0,003||No|
|PMI|0,260|0,260|No|

**Tabla 18. Análisis receptor y concentración MP10 Anual (evaluación riesgo pre-**

**existente).**

|Receptor|Aporte proyecto<br>(μg/m3)|Límite establecido<br>Tabla 1 DT:Criterio<br>de Evaluación<br>(μg/m3)|¿Genera impacto?|
|---|---|---|---|
|R1|0,028|1,00|No|
|R2|0,020|0,020|No|
|R3|0,011|0,011|No|
|R4|0,007|0,007|No|
|R5|0,007|0,007|No|
|R6|0,010|0,010|No|
|R7|0,002|0,002|No|
|R8|0,007|0,007|No|
|R9|0,005|0,005|No|
|R10|0,006|0,006|No|
|R11|0,004|0,004|No|
|R12|0,004|0,004|No|
|R13|0,002|0,002|No|
|R14|0,002|0,002|No|
|R15|0,002|0,002|No|
|R16|0,001|0,001|No|
|PMI|0,135|0,135|No|

De esta manera, se concluye que las concentraciones simuladas para los contaminante

MP10 y MP2,5 en ambas métricas, no generarán impacto en ninguno de los receptores

identificados, tal como se puede observar en las tablas precedentes, simulando en el

Punto de Máximo Impacto (PMI) concentraciones de 0,260 μg/m [3] y 0,135 μg/m [3] para

MP10 en sus métricas diarias y anual respectivamente y 0,246 μg/m [3] como concentración

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 52 de 75

diaria y 0,128 μg/m [3] como concentración anual para MP2,5, cuanto el proyecto en

evaluación **no genera impactos significativos sobre la calidad del aire de los**

**receptores evaluados ni las zonas circundantes al proyecto.**

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

# 7 Análisis de incertidumbre

Página 53 de 75

Tal como se plantea en la “Guía para el Uso de Modelos de Calidad del Aire en el SEIA”

(2023) de manera textual “cualquier modelo (meteorológico o de calidad del aire)

representa una aproximación a la realidad y, en consecuencia, sus resultados tienen

incertidumbres asociadas”. Ante lo cual, para cuantificar esta incertidumbre, se realiza un

análisis entre los valores entregados por el modelo WRF (valores meteorológicos) y

valores observados. En este caso los datos son extraídos de la **Estación San Pablo-**

**DASA** y **Pudahuel** de la Red Agrometeorológica del INIA; estación meteorológica más

cercana al proyecto y con datos disponibles para el año 2022, mismo año de simulación

del modelo WRF.

El modelo WRF simuló las condiciones meteorológicas dentro de un rango de 72 x 60 km

celdas de una dimensión de 1 x 1 km. Para efectos del análisis del ajuste de los datos

meteorológicos simulados se seleccionó una celda en donde se ubica la estación San

Pablo-DASA, desde la cual se extrajeron los datos y se compararon con los valores

observados de la estación meteorológica antes mencionada.

La correlación de los datos se determinó a través del ajuste por mínimos cuadrados,

método en el que existen dos parámetros principales: el coeficiente de correlación lineal

de Pearson (r) y el coeficiente de determinación ( R [2] ).

El coeficiente de correlación lineal es una medida de relación de Pearson entre dos

variables y se usa para medir el grado de relación entre ellas. El rango de valores va

desde el -1 al 1 y está representado por la siguiente ecuación.

r = [σ] [x][y]
xy

σ x . σ y

Donde,

- σ xy, es la covarianza entre x e y;

- σx, es la desviación estándar de x;

- σy, es la desviación estándar de y;

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 54 de 75

El coeficiente de determinación se utiliza como medida de eficiencia de la cobertura de

datos midiendo el porcentaje de variación entre las variables observadas y modeladas, es

decir, testea la capacidad predictiva del modelo e indica la proporción de la varianza de los

resultados que puede ser explicado por el modelo. Los valores del coeficiente de

determinación varían de 0 a 1, siendo este último el valor óptimo y está determinada por

la siguiente relación.

**Ecuación 7.1**

R [2] = r 2
xy
= (

σ xy

σ x . σ y

) 2

Donde,

- σ xy, es la covarianza entre x e y;

- σ x, es la desviación estándar de x;

- σ y, es la desviación estándar de y;

Se presenta el análisis de tendencia de los valores modelados a estar sobredimensionados

o subdimensionados respecto de los observados, a través del BIAS, el valor óptimo es 0 y

su cálculo se realiza según la siguiente ecuación.

**Ecuación 7.2**

n

BIAS = [1]

n [+ ∑(S] [i] [−O] [i] [)]

i=1

Donde,

 - S i, es el valor simulado;

 - O i, es el valor observado.

 - n, es el número de mediciones, en este caso el número de horas en un año, es

decir, 8760.

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 55 de 75

Se presenta el Mean Absolute Error (MAE), el cual es una medida del error promedio

absoluto del modelo con respecto a las observaciones. Este estadístico se calcula mediante

a la siguiente formula.

**Ecuación 7.3**

n

MAE = [1]

n [+ ∑|S] [i] [−O] [i] [|]

i=1

Donde,

 - S i, es el valor simulado;

 - O i, es el valor observado.

 - n, es el número de mediciones, en este caso el número de horas en un año, es

decir, 8760.

El Root Mean Squeare Error (RMSE) es una medida del desempeño promedio del modelo,

el cual, según él SEA, es un “estimador de la frecuencia de las diferencias entre los valores

observados y modelados, siendo especialmente sensible a los valores atípicos, por lo

tanto, a mayor diferencia entre estos valores menor será el grado de ajuste de este

estadístico”. Esta estadística valores de 0 al infinito, donde 0 es el valor de una

modelación sin errores y va creciendo a medida que decrece la capacidad del modelo de

representar la realidad.

**Ecuación 7.4**

n

RMSE = √ [1]

n

n [+ ∑(S] [i] [−O] [i] [)] [2]

i=1

Los resultados del ajuste del modelo meteorológico se presentan en la Tabla 19, en donde

se ve claramente como el modelo cumple con todos los criterios para los estadísticos

solicitados al realizar el análisis de incertidumbre con la estación Pablo-Dasa, pero al

realizar en la estación Pudahuel notamos que la correlación de la rapidez del viento es

menor a lo solicitado.

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 56 de 75

**Tabla 19. Resultados estadísticos obtenidos por la modelación**

|Variable|Correlación<br>lineal (r)|Coeficiente de<br>determinación (r2)|Bias|MAE|RMSE|
|---|---|---|---|---|---|
|**Estación San Pablo-DASA**|**Estación San Pablo-DASA**|**Estación San Pablo-DASA**|**Estación San Pablo-DASA**|**Estación San Pablo-DASA**|**Estación San Pablo-DASA**|
|Temperatura (°C)|0,93|0,86|0,86|2,22|2,9|
|Rapidez del Viento|0,63|0,39|0,09|1,13|1,6|
|**Estación San Pablo-DASA**|**Estación San Pablo-DASA**|**Estación San Pablo-DASA**|**Estación San Pablo-DASA**|**Estación San Pablo-DASA**|**Estación San Pablo-DASA**|
|Temperatura (°C)|0,88|0,77|0,56|2,72|3,53|
|Rapidez del viento<br>(m/s)|0,30|0,09|-0,75|1,96|2,55|
|**Criterio guía modelación SEA**|**Criterio guía modelación SEA**|**Criterio guía modelación SEA**|**Criterio guía modelación SEA**|**Criterio guía modelación SEA**|**Criterio guía modelación SEA**|
|Temperatura (°C)|>0,8|-|-4 - 4|≤ 4|≤ 4,5|
|Rapidez del viento<br>(m/s)|>0,6|-|-2,5 - 2,5|≤ 3|≤3,5|

## 7.1 Estación San Pablo-DASA

7.1.1 Caracterización de la temperatura modelada y observada.

En la Figura 30 se observa la correlación entre la temperatura horaria observada en la

estación San Pablo-DASA y las simuladas por el modelo WRF del año 2022.

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 57 de 75

**Figura 30. Correlación entre temperatura observada y modelada**

En la figura anterior se puede notar que existe una correlación positiva entre la

temperatura observada y la modelada cuyo valor es 0,93. A su vez, el coeficiente de

determinación sugiere que el modelo es capaz de representar el 86% de la variabilidad

observada.

En la Figura 31 se observa la frecuencia de las temperaturas en rangos de clases para los

datos modelados y los simulados, donde se observa en que en general el modelo tiene

pocas diferencias con las observaciones. El valor del BIAS nos indica que la temperatura

promedio modelada es 0,86°C mayor a la observada.

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 58 de 75

**Figura 31. Frecuencia de las temperaturas observadas y modeladas**

En la Figura 32 se presenta el ciclo diario mensual promedio de la temperatura observada

(izquierda) y modelada por el modelo WRF (derecha), para el año 2022. Se destacan

diferencias, ya que los valores de temperatura observada tienden a ser ligeramente más

fríos entre las 00:00 UTC y las 08:00 UTC en invierno y en el mismo rango horarios, pero

en verano la temperatura modelada es menor en lo observado, mientras que las

temperaturas modeladas s entre las 12:00 UTC y las 18:00 UTC en verano, otoño y

primavera presentan valores muy cercanos a lo observado, mientras que en invierno

posee temperaturas ligeramente menores. En general el mayor cambio que hay es un

aumento de la temperatura en los rangos fríos que se ve reflejado en un aumento

promedio de 0.86°C.

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 59 de 75

**Figura 32. Ciclo diario mensual de la temperatura observada (izquierda) y**

**modelada por WRF (derecha), para el año 2022**

En la Figura 33, se presenta el ciclo diario promedio de la temperatura para el período

completo, tanto en la representación del modelo WRF (línea azul) como en la observada

(línea roja). En términos generales, el modelo WRF logra una sólida representación de la

variabilidad diaria, evidenciada por una correlación de 0,97. Se observa un leve desfase de

aproximadamente 1 hora entre ambas representaciones. Se destaca que, la temperatura

observada es menor a la modelada entre las 00:00 UTC y las 14:00 UTC y a partir de las

19:00 UTC.

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 60 de 75

**Figura 33. Ciclo diario promedio modelado (azul) y observado (rojo)**

7.1.2 Caracterización de la rapidez del viento modelada y observada.

En la Figura 34 se presenta la correlación entre la temperatura horaria observada en la

estación San Pablo-DASA las simuladas por el modelo WRF del año 2022.

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 61 de 75

**Figura 34. Correlación entre la rapidez del viento observada y modelada**

De la figura anterior se nota que existe una correlación positiva entre la rapidez del viento

observada y la modelada, siendo el valor del coeficiente de correlación lineal de 0,63. Por

otro lado, el coeficiente de determinación sugiere que el modelo es capaz de representar

el 39% del comportamiento observado.

En la Figura 35 se observa la frecuencia de magnitudes de rapidez del viento en distintas

categorías. Se identifica claramente como el modelo sobreestima la frecuencia de los

vientos calmos (entre los 0,0 y 0,5 m/s) y subestima aquellos entre 0,5 - 2,1 m/s con,

respecto a las observaciones. El resto de rangos presentan pequeñas sub y sobre

estimaciones, pero no tan relevantes como las mencionadas anteriormente.

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 62 de 75

**Figura 35. Frecuencia de la rapidez del viento observadas y modeladas**

En la Figura 36 se presenta el ciclo diario de la rapidez del viento observado en la estación

San Pablo-DASA (izquierda) y modelado por WRF (derecha). Se ve claramente que la

rapidez del viento observada es menor a la modelada entre las 14:00 y 18:00 UTC. En las

observaciones (izquierda), se ve claramente como la rapidez del viento es menor 1 m/s

entre las 00:00 UTC y 08:00 UTC, para luego aumentar paulatinamente hasta

aproximadamente las 16:00 UTC, llegando hasta los 4,5 m/s aproximadamente, para

luego comenzar a disminuir hasta completar el ciclo. Por otro lado, el ciclo diario modelado

toma velocidades entre 0 m/s hasta aproximadamente 6,5 m/s, en general vemos que la

rapidez del viento toma valores entre 0 m/s y 3,0 m/s entre las 00:00 UTC y las 12:00

UTC, para luego aumentar paulatinamente y tomar valores sobre los 6,0 m/s hasta las

16:00 UTC, para luego comenzar a disminuir hasta completar el ciclo.

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 63 de 75

**Figura 36. Ciclo diario mensual de la rapidez del viento observada (izquierda) y**

**modelada por WRF (derecha), para el año 2022**

En la Figura 37, se presenta el ciclo diario promedio de la rapidez del viento para todo el

periodo modelado (línea azul) y observado (línea roja). Podemos ver que, en promedio,

WRF logra una buena representación del ciclo diario de la rapidez del viento, representado

por una correlación 0,96. Se destaca que la rapidez del viento modelada es mayor a la

observada entre las 14:00 y 23:00 UTC.

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 64 de 75

**Figura 37. Ciclo diario promedio modelado (azul) y observado (rojo)**

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

## 7.2 Estación Pudahuel

7.2.1 Caracterización de la temperatura modelada y observada.

Página 65 de 75

En la Figura 38 se observa la correlación entre la temperatura horaria observada en la

estación Pudahuel y las simuladas por el modelo WRF del año 2022.

**Figura 38. Correlación entre temperatura observada y modelada**

En la figura anterior se puede notar que existe una correlación positiva entre la

temperatura observada y la modelada cuyo valor es 0,88. A su vez, el coeficiente de

determinación sugiere que el modelo es capaz de representar el 78% de la variabilidad

observada.

En la Figura 39 se observa la frecuencia de las temperaturas en rangos de clases para los

datos modelados y los simulados, donde se observa en que en general el modelo tiene

pocas diferencias con las observaciones. El valor del BIAS nos indica que la temperatura

promedio modelada es 0,56°C mayor a la observada.

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 66 de 75

**Figura 39. Frecuencia de las temperaturas observadas y modeladas**

En la Figura 40 se presenta el ciclo diario mensual promedio de la temperatura observada

(izquierda) y modelada por el modelo WRF (derecha), para el año 2022. Se destacan

diferencias, ya que los valores de temperatura observada tienden a ser más fríos entre las

00:00 UTC y las 08:00 UTC en invierno y en el mismo rango horario, pero en verano la

temperatura modelada es mayor a lo observado, mientras que las temperaturas

modeladas son entre las 12:00 UTC y las 18:00 UTC en todas las estaciones existe menor

temperatura. En general el mayor cambio que hay es un aumento de la temperatura en

los rangos fríos que se ve reflejado en un aumento promedio de 0.56°C.

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 67 de 75

**Figura 40. Ciclo diario mensual de la temperatura observada (izquierda) y**

**modelada por WRF (derecha), para el año 2022**

En la Figura 41, se presenta el ciclo diario promedio de la temperatura para el período

completo, tanto en la representación del modelo WRF (línea azul) como en la observada

(línea roja). En términos generales, el modelo WRF logra una sólida representación de la

variabilidad diaria, evidenciada por una correlación de 0,95. Se observa un leve desfase de

aproximadamente 1 hora entre ambas representaciones. Se destaca que, la temperatura

observada es menor a la modelada entre las 00:00 UTC y las 11:00 UTC y a partir de las

12:00 UTC los valores observados presentan magnitudes mayores que lo modelado.

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 68 de 75

**Figura 41. Ciclo diario promedio modelado (azul) y observado (rojo)**

7.2.2 Caracterización de la rapidez del viento modelada y observada.

En la Figura 42 se presenta la correlación entre la temperatura horaria observada en la

estación Pudahuel las simuladas por el modelo WRF del año 2022.

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 69 de 75

**Figura 42. Correlación entre la rapidez del viento observada y modelada**

De la figura anterior se nota que existe una correlación positiva entre la rapidez del viento

observada y la modelada, siendo el valor del coeficiente de correlación lineal de 0,3. Por

otro lado, el coeficiente de determinación sugiere que el modelo es capaz de representar

el 9% del comportamiento observado.

En la Figura 43 se observa la frecuencia de magnitudes de rapidez del viento en distintas

categorías. Se identifica claramente como el modelo sobreestima la frecuencia de los

vientos calmos (entre los 0,0 y 0,5 m/s) y subestima aquellos entre 0,5 - 2,1 m/s y 5.7

8.8 con respecto a las observaciones. El resto de rangos presentan pequeñas sub y sobre

estimaciones, pero no tan relevantes como las mencionadas anteriormente.

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 70 de 75

**Figura 43. Frecuencia de la rapidez del viento observadas y modeladas**

En la Figura 44 se presenta el ciclo diario de la rapidez del viento observado en la estación

Pudahuel (izquierda) y modelado por WRF (derecha). Se ve claramente que la rapidez del

viento observada es mayor a la modelada en todas las horas y estaciones del año. En las

observaciones (izquierda), se ve claramente como la rapidez del viento es mayor a 1 m/s

entre las 00:00 UTC y 10:00 UTC, para luego aumentar paulatinamente hasta

aproximadamente las 16:00 UTC, llegando hasta los 6,5 m/s aproximadamente, para

luego comenzar a disminuir hasta completar el ciclo. Por otro lado, el ciclo diario modelado

toma velocidades entre 0 m/s hasta aproximadamente 6,5 m/s, en general vemos que la

rapidez del viento toma valores entre 0 m/s y 2,0 m/s entre las 00:00 UTC y las 8:00 UTC,

para luego aumentar paulatinamente y tomar valores máximos de los 4,5 m/s

aproximadamente hasta las 16:00 UTC, para luego comenzar a disminuir hasta completar

el ciclo.

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 71 de 75

**Figura 44. Ciclo diario mensual de la rapidez del viento observada (izquierda) y**

**modelada por WRF (derecha), para el año 2022**

En la Figura 45, se presenta el ciclo diario promedio de la rapidez del viento para todo el

periodo modelado (línea azul) y observado (línea roja). Podemos ver que, en promedio,

WRF logra una representación regular del ciclo diario de la rapidez del viento,

representado por una correlación 0,75. Se destaca que la rapidez del viento modelada es

menor a la observada en la mayoría de los rangos horarios.

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 72 de 75

**Figura 45. Ciclo diario promedio modelado (azul) y observado (rojo)**

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 73 de 75

# 8 Conclusión

Se estudió la concentración de las emisiones producto de la construcción proyectada para

el año 1 del proyecto “ **Planta de Tratamiento de Aguas Servidas Aguas Lo Aguirre** ”

a ubicarse en la comuna de Pudahuel, Región Metropolitana. De esta forma, fueron

modeladas las emisiones de MP10 y MP2,5 a fin de determinar las concentraciones que

éstos tendrán en la atmósfera, además de prever posibles efectos a la salud de las

personas y recursos naturales.

Tal como se abordó anteriormente en el informe, el desplazamiento de los contaminantes

ocurre mayoritariamente al interior de la zona de emplazamiento del proyecto y en las

proximidades del proyecto. Al respecto se destaca que:

 Todas las plumas de dispersión se distribuyen tanto dentro como fuera del

polígono del proyecto, situando su máxima concentración en la zona donde se

construirán las obras, cabe señalar que, si bien se modelaron las obras asociadas a

la construcción de la impulsión, la temporalidad de las obras caracterizadas,

simularon concentraciones no significativas en esas zonas.

 El receptor R1 es aquel que presenta las mayores concentraciones modelas, sin

embargo, los valores evidenciados son de baja magnitud y en ningún caso

generarán un impacto significativo en la salud de la población.

 El punto de máximo impacto para todas las métricas analizadas se emplaza dentro

del proyecto y las concentraciones modeladas son de baja magnitud.

Es importante considerar que la concentración en el aire de los contaminantes puede ser

influida por diversos factores, entre los cuales están la tasa de emisión, las condiciones en

que los contaminantes son liberados a la atmósfera, la topografía del entorno, e

indudablemente las condiciones meteorológicas, es decir, la dispersión y concentración de

las partículas y gases en el aire quedará determinada por las condiciones ambientales en

donde éstos son liberados, como por ejemplo: gradiente de presión, gradiente de

temperatura, velocidad y dirección del viento (los que a su vez están influenciados por las

características topográficas del lugar), entre otros.

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 74 de 75

Ademas, tal como menciona la guia para el uso de modelos de calidad del aire en el SEIA

todo modelo meteorológico representa una aproximación a la realidad por lo que sus

resultados tienen incertidumbres asociadas (ver apartado 7). Estas incertidumbres se

producen debido a las diferencias entre lo simulado por el modelo meteorologico WRF y

los datos observados en ambas estaciones pertenencientes al INIA analizadas.

Finalmente, la modelación de las emisiones del proyecto de material particulado (MP10 y

MP2,5) resultaron ser de baja magnitud concluyendo que, el funcionamiento del **proyecto**

**no representa un riesgo significativo a la salud ni calidad de vida de la**

**población, según los criterios de evaluación establecidos en el documento**

**técnico publicado por el SEA** . Considerando que en ningún caso las concentraciones

proyectadas inclusive en el punto de máximo impacto alcanzan siquiera los valores más

restrictivos presentes en el documento técnico para zonas saturadas.

DECLARACIÓN DE IMPACTO AMBIENTAL
INFORME MODELACIÓN DE EMISIONES ATMOSFÉRICAS

“PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS AGUAS

LO AGUIRRE”

Página 75 de 75

# 9 Bibliografía

Hernandez- Garces, A., J. Souto, A. Rodríguez, S. Saavera, J. Casares, 2015. Validation of

CALMET/CALPUFF models simulations around a large power plant stack, p. 51.

Recuperado el 27 de junio de 2016, desde

http://revistas.ucm.es/index.php/FITE/article/view/51192/47527

Hernández-Garces, A., U. Jáuregui-Haga, J. González, J. Caseres-Long, S. Saavedra, F.

Guzmán-Martínez, A. Torres-Valle, 2016. Aplicaciones del modelo lagrangiano de

dispersión atmosférica CALPUFF, Ciencias de la Tierra y el Espacio, enero-junio, Vol. 17,

No 1, p. 37. ISSN 1729-3790. Recuperado el 29 de junio de 2016, desde

http://www.iga.cu/publicaciones/revista/assets/calpuffreview2.pdf.

Servicio de Evaluación Ambiental, 2023, Guía para el Uso de Modelos de Calidad del Aire

en el SEIA. Recuperado el 11 de agosto de 2023, desde:

 - - [https://sea.gob.cl/sites/default/files/imce/archivos/2023/02.FEB/28/Guia](https://sea.gob.cl/sites/default/files/imce/archivos/2023/02.FEB/28/Guia-Calidad-del-aire_V.4-final.pdf) Calidad del

 aire_V.4 final.pdf

Servicio de Evaluación Ambiental, 2023, Guía para la evaluación ambiental del riesgo para

la salud de la población (segunda edición). Recuperado el 11 de agosto de 2023, desde:

https://sea.gob.cl/sites/default/files/imce/archivos/2023/03/08/Guia.pdf

DICTUC 2022, EVALUACIÓN SIGNIFICANCIA DEL IMPACTO DE LAS EMISIONES DE UN

PROYECTO O ACTIVIDAD EN ZONAS SATURADAS EN EL MARCO DEL SEIA. Recuperado el

11 de agosto de 2023, desde:

 - [https://www.sea.gob.cl/sites/default/files/imce/archivos/2022/03/21/18fa27dd74](https://www.sea.gob.cl/sites/default/files/imce/archivos/2022/03/21/18fa27dd74-6bc2-4b96-9960-1ee4f178c967.pdf) 6bc2

 - 4b96 9960 1ee4f178c967.pdf

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Valores normados para MP10 y MP2,5 en Chile.****

| Nivel | MP10 (μg/m3N) | MP2,5 (μg/m3) |
| --- | --- | --- |
| **Concentración Anual** | 50 | 20 |
| **Concentración 24 horas** | 130 | 50 |
| **Alerta** | 180-229 | 80-109 |
| **Preemergencia** | 230-329 | 110-169 |
| **Emergencia** | 330 o superior | 170 o superior |

**Tabla 2.: Estaciones conectadas a la red SINCA cercanas al emplazamiento del****

| Estación | Contaminantes | Rango de datos | Distancia al<br>proyecto (km) |
| --- | --- | --- | --- |
| **Pudahuel** | MP10 y MP2,5 | 2014 a la actualidad | 7,4 |
| **Cerrillos II** | MP10 y MP2,5 | Abril 2022 a la actualidad | 8,5 |

**Tabla 3.: Porcentaje de superación concentración promedio anual de MP10,****

| Año | Concentración<br>Promedio Anual<br>(μg/m3) | Límite normativo D.S.<br>12/2022 MMA (μg/m3N) | Porcentaje de excedencia<br>de la norma (%) |
| --- | --- | --- | --- |
| 2014 | 63,63 | 50,0 | 27 |
| 2015 | 73,67 | 73,67 | 47 |
| 2016 | 69,52 | 69,52 | 39 |
| 2017 | 65,21 | 65,21 | 30 |
| 2018 | 58,64 | 58,64 | 17 |
| 2019 | 72,56 | 72,56 | 45 |
| 2020 | 62,98 | 62,98 | 26 |
| 2021 | 63,26 | 63,26 | 27 |
| 2022 | 64,71 | 64,71 | 29 |
| 2023 | 65,59 | 65,59 | 31 |

**Tabla 5.: Registro de días declarados en alerta, preemergencia y emergencia****

| Año | Días de alerta | Días de preemergencia | Días de emergencia |
| --- | --- | --- | --- |
| 2014 | 4 | 0 | 0 |
| 2015 | 6 | 3 | 0 |
| 2016 | 0 | 0 | 0 |
| 2017 | 2 | 0 | 0 |
| 2018 | 1 | 0 | 0 |
| 2019 | 6 | 2 | 0 |

**Tabla 6.: Registro de días declarados en alerta, preemergencia y emergencia****

| Año | Días de alerta | Días de preemergencia | Días de emergencia |
| --- | --- | --- | --- |
| 2023 | 3 | 0 | 0 |

**Tabla 7.: Concentración promedio anual de MP2,5, EMRP Pudahuel****

| Año | Concentración<br>promedio anual<br>(μg/m3) | Límite normativo D.S.<br>12/2011 MMA (μg/m3) | Porcentaje de excedencia<br>de la norma (%) |
| --- | --- | --- | --- |
| 2014 | 28,80 | 20 | 44 |
| 2015 | 33,56 | 33,56 | 68 |
| 2016 | 32,39 | 32,39 | 62 |
| 2017 | 28,45 | 28,45 | 42 |
| 2018 | 26,87 | 26,87 | 34 |
| 2019 | 26,84 | 26,84 | 34 |
| 2020 | 24,07 | 24,07 | 20 |
| 2021 | 26,27 | 26,27 | 31 |
| 2022 | 24,84 | 24,84 | 24 |
| 2023 | 28,80 | 28,80 | 44 |

**Tabla 8.: Porcentaje de superación concentración promedio anual de MP2,5,****

| Año | Concentración<br>promedio anual<br>(μg/m3) | Límite normativo D.S.<br>12/2022 MMA (μg/m3N) | Porcentaje de excedencia<br>de la norma (%) |
| --- | --- | --- | --- |
| 2023 | 25,26 | 20 | 11 |

**Tabla 9.: Registro de días declarados en alerta, preemergencia y emergencia****

| Año | Días de alerta | Días de preemergencia | Días de emergencia |
| --- | --- | --- | --- |
| 2014 | 7 | 3 | 0 |
| 2015 | 16 | 4 | 1 |
| 2016 | 4 | 4 | 0 |
| 2017 | 1 | 0 | 0 |
| 2018 | 1 | 2 | 0 |
| 2019 | 8 | 0 | 0 |

**Tabla 10.: Registro de días declarados en alerta, preemergencia y emergencia****

| Año | Días de alerta | Días de preemergencia | Días de emergencia |
| --- | --- | --- | --- |
| 2023 | 1 | 0 | 0 |

**Tabla 11.: Características del modelo WRF****

| Vértice | Latitud | Longitud |
| --- | --- | --- |
| Noroeste | 33,31°S | 71,17°O |
| Suroeste | 33,97°S | 71,17°O |
| Noreste | 33,31°S | 70,37°O |
| Sureste | 33,97°S | 70,37°O |
| Centroide | 33,64°S | 70,77°O |

**Tabla 12.: Receptores cercanos al proyecto****

| Receptor | Coordenada UTM HUSO 18 S (m) | Col3 | Distancia desde la planta<br>(m) |
| --- | --- | --- | --- |
| **Receptor** | **Este** | **Norte** | **Norte** |
| R1 | 328.746,00 | 6.298.440,00 | 95,6 |
| R2 | 328.793,00 | 6.298.395,00 | 124,5 |
| R3 | 328.913,00 | 6.298.375,00 | 243,9 |

**Tabla 13.: Características de las estaciones meteorológicas cercanas al proyecto****

| Estación | Distancia<br>al<br>Proyecto<br>(km) | Año | Porcentaje de datos por Variable (%) | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Estación** | **Distancia**<br>**al**<br>**Proyecto**<br>**(km) ** | **Año** | **Temperatura** | **Precipitación** | **Dirección del viento** | **Magnitud del viento** |
| Pudahuel | 7,67 | 2021 | 99,89 | 99,89 | 99,89 | 99,89 |
| Pudahuel | 7,67 | 2022 | 99,98 | 99,98 | 99,98 | 99,98 |
| Pudahuel | 7,67 | 2023 | 99,94 | 99,94 | 99,94 | 99,94 |
| San<br>Pablo-<br>DASA | 9,58 | 2021 | 96,32 | 96,51 | 96,51 | 96,51 |
| San<br>Pablo-<br>DASA | 9,58 | 2022 | 99,68 | 99,68 | 99,68 | 99,68 |
| San<br>Pablo-<br>DASA | 9,58 | 2023 | 96,32 | 96,51 | 96,51 | 96,51 |
| Rinconada | 5,39 | 2021 | 99,99 | 99,99 | 99,99 | 99,99 |
| Rinconada | 5,39 | 2022 | 100 | 100 | 100 | 100 |
| Rinconada | 5,39 | 2023 | 99,67 | 99,67 | 99,67 | 99,67 |

**Tabla 14.: Criterio de valores de significancia sobre receptores humanos****

| Contaminante | Periodo | Incremento en la<br>concentración (μg/m3) |
| --- | --- | --- |
| MP2,5 | 24 horas | 1,71 |
| MP2,5 | Anual | 0,33 |
| MP10 | 24 horas | 5,00 |
| MP10 | Anual | 1,00 |

**Tabla 15.: Análisis receptor y concentración MP2,5 24 horas (evaluación riesgo****

| Receptor | Aporte proyecto<br>(μg/m3) | Límite establecido<br>Tabla 1 DT:Criterio<br>de Evaluación<br>(μg/m3) | ¿Genera impacto? |
| --- | --- | --- | --- |
| R1 | 0,073 | 1,71 | No |
| R2 | 0,070 | 0,070 | No |
| R3 | 0,054 | 0,054 | No |
| R4 | 0,044 | 0,044 | No |
| R5 | 0,042 | 0,042 | No |
| R6 | 0,048 | 0,048 | No |
| R7 | 0,007 | 0,007 | No |
| R8 | 0,043 | 0,043 | No |
| R9 | 0,031 | 0,031 | No |
| R10 | 0,030 | 0,030 | No |
| R11 | 0,023 | 0,023 | No |
| R12 | 0,022 | 0,022 | No |
| R13 | 0,005 | 0,005 | No |
| R14 | 0,007 | 0,007 | No |
| R15 | 0,005 | 0,005 | No |
| R16 | 0,002 | 0,002 | No |
| PMI | 0,246 | 0,246 | No |

**Tabla 16.: Análisis receptor y concentración MP2,5 Anual (evaluación riesgo pre-****

| Receptor | Aporte proyecto<br>(μg/m3) | Límite establecido<br>Tabla 1 DT:Criterio<br>de Evaluación<br>(μg/m3) | ¿Genera impacto? |
| --- | --- | --- | --- |
| R1 | 0,025 | 0,33 | No |
| R2 | 0,018 | 0,018 | No |
| R3 | 0,010 | 0,010 | No |
| R4 | 0,007 | 0,007 | No |
| R5 | 0,006 | 0,006 | No |
| R6 | 0,008 | 0,008 | No |

**Tabla 17.: Análisis receptor y concentración MP10 24 horas (evaluación riesgo****

| Receptor | Aporte proyecto<br>(μg/m3) | Límite establecido<br>Tabla 1 DT:Criterio<br>de Evaluación<br>(μg/m3) | ¿Genera impacto? |
| --- | --- | --- | --- |
| R1 | 0,080 | 5,00 | No |
| R2 | 0,076 | 0,076 | No |
| R3 | 0,059 | 0,059 | No |
| R4 | 0,048 | 0,048 | No |
| R5 | 0,046 | 0,046 | No |
| R6 | 0,055 | 0,055 | No |
| R7 | 0,009 | 0,009 | No |
| R8 | 0,047 | 0,047 | No |
| R9 | 0,034 | 0,034 | No |
| R10 | 0,033 | 0,033 | No |
| R11 | 0,025 | 0,025 | No |
| R12 | 0,024 | 0,024 | No |
| R13 | 0,008 | 0,008 | No |
| R14 | 0,009 | 0,009 | No |
| R15 | 0,009 | 0,009 | No |

**Tabla 18.: Análisis receptor y concentración MP10 Anual (evaluación riesgo pre-****

| Receptor | Aporte proyecto<br>(μg/m3) | Límite establecido<br>Tabla 1 DT:Criterio<br>de Evaluación<br>(μg/m3) | ¿Genera impacto? |
| --- | --- | --- | --- |
| R1 | 0,028 | 1,00 | No |
| R2 | 0,020 | 0,020 | No |
| R3 | 0,011 | 0,011 | No |
| R4 | 0,007 | 0,007 | No |
| R5 | 0,007 | 0,007 | No |
| R6 | 0,010 | 0,010 | No |
| R7 | 0,002 | 0,002 | No |
| R8 | 0,007 | 0,007 | No |
| R9 | 0,005 | 0,005 | No |
| R10 | 0,006 | 0,006 | No |
| R11 | 0,004 | 0,004 | No |
| R12 | 0,004 | 0,004 | No |
| R13 | 0,002 | 0,002 | No |
| R14 | 0,002 | 0,002 | No |
| R15 | 0,002 | 0,002 | No |
| R16 | 0,001 | 0,001 | No |
| PMI | 0,135 | 0,135 | No |

**Tabla 19.: Resultados estadísticos obtenidos por la modelación****

| Variable | Correlación<br>lineal (r) | Coeficiente de<br>determinación (r2) | Bias | MAE | RMSE |
| --- | --- | --- | --- | --- | --- |
| **Estación San Pablo-DASA** | **Estación San Pablo-DASA** | **Estación San Pablo-DASA** | **Estación San Pablo-DASA** | **Estación San Pablo-DASA** | **Estación San Pablo-DASA** |
| Temperatura (°C) | 0,93 | 0,86 | 0,86 | 2,22 | 2,9 |
| Rapidez del Viento | 0,63 | 0,39 | 0,09 | 1,13 | 1,6 |
| **Estación San Pablo-DASA** | **Estación San Pablo-DASA** | **Estación San Pablo-DASA** | **Estación San Pablo-DASA** | **Estación San Pablo-DASA** | **Estación San Pablo-DASA** |
| Temperatura (°C) | 0,88 | 0,77 | 0,56 | 2,72 | 3,53 |
| Rapidez del viento<br>(m/s) | 0,30 | 0,09 | -0,75 | 1,96 | 2,55 |
| **Criterio guía modelación SEA** | **Criterio guía modelación SEA** | **Criterio guía modelación SEA** | **Criterio guía modelación SEA** | **Criterio guía modelación SEA** | **Criterio guía modelación SEA** |
| Temperatura (°C) | >0,8 | - | -4 - 4 | ≤ 4 | ≤ 4,5 |
| Rapidez del viento<br>(m/s) | >0,6 | - | -2,5 - 2,5 | ≤ 3 | ≤3,5 |
