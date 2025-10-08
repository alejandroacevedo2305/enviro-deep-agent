---
title: Sin título
author: Nicolas Sepulveda
date: D:20240129143231-03'00'
language: es
type: report
pages: 63
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Informe de Modelación Atmosférica “Proyecto Modificación PTAS Hualañé”
-->

# Informe de Modelación Atmosférica “Proyecto Modificación PTAS Hualañé”

**Enero, 2024**

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

**Contenidos**

Página 2 de 63

1 Introducción. ....................................................................................................... 3

2 Objetivos. ........................................................................................................... 5

3 Marco Legal Regulatorio. ...................................................................................... 6

3.1 Estado de la Calidad del Aire de Hualañé......................................................... 7

3.1.1 Línea de Base: Análisis de Cumplimiento Normativo .................................. 7

4 Justificación de los modelos utilizados en el estudio. .............................................. 13

4.1 Uso modelo WRF ......................................................................................... 13

4.2 Uso modelo CALPUFF ................................................................................... 13

5 Metodología ....................................................................................................... 16

5.1 Modelación de partículas............................................................................... 16

5.1.1 Modelación meteorológica ...................................................................... 16

5.1.2 Modelación de dispersión de contaminantes ............................................. 17

5.1.3 Criterios para la modelación de partículas ................................................ 19

6 Resultados ......................................................................................................... 24

6.1 Modelamiento meteorológico ........................................................................ 24

6.1.1 Caracterización geofísica de la zona de estudio ........................................ 24

6.1.2 Caracterización de la velocidad y dirección de los vientos Anual ................. 25

6.1.3 Caracterización de la velocidad y dirección de los vientos Estacional .......... 27

6.1.4 Caracterización de la Temperatura del Aire .............................................. 36

6.1.5 Caracterización de la Precipitación .......................................................... 37

6.1.6 Altura Capa de meza .............................................................................. 38

6.2 Concentraciones Modeladas .......................................................................... 39

6.2.1 Dispersión e Isoconcentración Material Particulado Respirable, MP10 ......... 39

6.2.2 Dispersión e Isoconcentración Material Particulado Fino Respirable, MP 2.5 44

6.2.3 Modelación discreta de las emisiones contaminantes ................................ 49

7 Análisis de incertidumbre .................................................................................... 53

7.1 Caracterización de la Temperatura Modelada. ................................................. 56

7.2 Caracterización de la Velocidad del viento Modelada y Observada .................... 58

8 Conclusión ......................................................................................................... 61

9 Bibliografía ......................................................................................................... 63

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 3 de 63

**1** **Introducción.**

El proyecto “ **Modificación PTAS Hualañé** ” consiste en el paso de una tecnología de

laguna aireadas a unas lagunas aireadas multicelulares, se contempla abarcar una superficie

aproximada 0,61 hectáreas a ocupar por las obras proyectadas. El proyecto se ubicará en

la comuna de Hualañé, provincia de Curicó, Región del Maule.

Figura 1: Ubicación Del proyecto

Con este estudio se busca predecir la concentración de material particulado grueso y fino

(MP10 Y MP 2,5), además de evaluar su contribución en puntos receptores de interés y en

las estaciones de calidad del aire más cercanas, esto último respecto a su situación basal.

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 4 de 63

La modelación de las emisiones se realizó en base a los resultados obtenido de la estimación

de emisiones atmosférica. Considerando como escenario de máxima emisión el primer año

de construcción y la operación de la PTAS sin proyecto.

La evaluación de la dispersión y concentración de las emisiones de material particulado se

realizó mediante el programa CALPUFF, el cual es un modelo de dispersión usado

ampliamente para simulaciones de concentraciones ambientales de las emisiones normales,

con el objeto de establecer, desarrollar y analizar escenarios de emisión y regulación. A su

vez, CALPUFF es recomendado por el Ministerio de Medio Ambiente en la “Guía para el Uso

de Modelos de Calidad del Aire en el SEIA”, publicada el año 2023. Los resultados y análisis

de esta evaluación se presentan en el siguiente informe.

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 5 de 63

**2** **Objetivos.**

El presente informe, tiene como objetivo general cuantificar y evaluar el efecto en la

atmósfera debido a las emisiones de contaminantes generadas por el proyecto

**“Modificación PTAS Hualañé”** y cuantificar sus concentraciones.

Para lo anterior se plantean los siguientes objetivos específicos:

 Evaluar en términos de concentración, el alcance de las emisiones de MP10 y MP2,5

en la atmósfera.

 Evaluar la concentración de MP10 y MP2,5 en receptores que actualmente se

encuentren cercanos al proyecto, así como en las estaciones de calidad del aire

emplazadas cercanos a éste.

 Determinar la afectación a la salud de las personas debido al aporte a la

concentración basal de MP10 y MP2,5 en la ciudad, dado el desarrollo del proyecto.

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

**3** **Marco Legal Regulatorio.**

Página 6 de 63

Actualmente, los contaminantes MP10 y MP2,5 están regulados bajo normas de calidad

primaria, cuyo objetivo es proteger la salud de las personas de los efectos agudos y crónicos

de la exposición de estos contaminantes con un riesgo aceptable. Para esto, se fijan límites

de concentración permitidos, condiciones de superación de la norma y los niveles que dan

paso a situaciones de emergencia ambiental.

El material particulado respirable MP10 es regulado por el D.S. 12/2022 del Ministerio del

Medio Ambiente, mientras el material particulado fino respirable MP2,5 es regulado por el

D.S. 12/2011 del Ministerio del Medio Ambiente.

En la siguiente tabla se aprecian los valores del límite anual y diario para los contaminante

MP10 y MP2,5, además de los rangos que dan origen a situaciones de alerta, preemergencia

y emergencia ambiental.

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

superación de la noma, sino que se considera que la norma es incumplida bajo las siguientes

condiciones:

 - Cuando el promedio de la concentración anual de tres años consecutivos iguale o

supere los 50 μg/m3.

 - Si el percentil 98 (P98) de las concentraciones de 24 horas durante un año sea igual

o superior a 130 μg/m3.

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 7 de 63

 - Si durante un año se registrasen siete o más días cuya concentración sea mayor a

130 μg/m3.

En el mismo contexto, las condiciones de superación de la norma de MP2,5 son las que se

describen a continuación:

 - Cuando el promedio de la concentración anual de tres años consecutivos iguale o

supere los 20 μg/m3.

 - Si el percentil 98 (P98) de las concentraciones de 24 horas durante un año sea igual

o superior a 50 μg/m3

**3.1** **Estado de la Calidad del Aire de Hualañé**

La comuna de Hualañé no cuenta con estaciones de Calidad del Aire de representatividad

poblacional, por lo cual, se escogió la estación más cercana ubicada en Curicó, llamada

estación Curicó, ubicada en la comuna de Curicó.

**3.1.1** **Línea de Base: Análisis de Cumplimiento Normativo**

**3.1.1.1** **Material particulado respirable (MP10)**

En la siguiente figura, se observan las concentraciones promedió de 24 horas registradas

para los años, entre el 2015 y 2022, que tengan más del 75% de sus datos disponibles.

Podemos observar cómo existe superación de la norma solo en el año 2015, siendo este el

año con mayores concentraciones, y que disminuye constantemente las concentraciones en

los siguientes años hasta el 2021, donde aumenta hasta 114,0 ug/m [3], para luego disminuir

el 2022 hasta 94,9 ug/m [3], siendo la menor concentración registrada.

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 8 de 63

**Figura 2: Concentración Promedio 24 horas de MP10 Estación Curicó.**

Respecto a la concentración promedio anual de MP 10 que establece el D.S 12/2022 MMA,

podemos observar de la Tabla3 que en todos los años analizados es superada la normativa,

siendo en particular el año 2015 aquel con mayor porcentaje de excedencia, con un 190,3%.

**Tabla 2 Concentración promedio anual de MP10 estación**

|Año|Porcentaje de<br>datos<br>disponibles (%)|Concentración<br>Promedio Anual<br>(μg/m3)|Límite normativo<br>D.S. 12/2011 MMA<br>(μg/m3)|Porcentaje de<br>excedencia de la<br>norma (%)|
|---|---|---|---|---|
|2015|99,6%|58,1|50,0|190,3%|
|2016|-|-|-|-|
|2017|99,8%|43,9|43,9|119,10%|
|2018|99,9%|41,0|41,0|105,10%|
|2019|99,8%|45,3|45,3|116,70%|
|2020|99,8%|42,6|42,6|113,00%|
|2021|100,0%|42,3|42,3|111,60%|
|2022|99,5%|40,0|40,0|100,80%|

Fuente: Elaboración propia en base a los datos dispuestos en el Sistema Nacional de Calidad del

Aire (SINCA).

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 9 de 63

Con respecto a las concentraciones de MP10 como promedio trianual, esta fue caracterizada

para cuatro periodos, y tal como se evidencia en la siguiente figura, no existe superación

normativa en todos los periodos analizado siendo el primer intervalo (2017-2019) el que

presenta mayor concentración con 43,5.

**Figura 3. Concentración promedio trianual MP10, EMRP Curicó**

Además, para el periodo analizado, se registraron 31 días declarados con alerta siendo el

año 2021, el que exhibe un mayor número de días en esta condición, presentado 9 días de

alerta. En cuanto a los estados de preemergencia y/o emergencia, se registraron 16 de

preemergencia y 0 días de emergencia, tal como muestra la siguiente tabla:

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 10 de 63

**Tabla 3. Días de alerta, preemergencia y emergencia ambiental en la EMRP**

**Curicó**

|Año|MP10|Col3|Col4|MP2,5|Col6|Col7|
|---|---|---|---|---|---|---|
|**Año**|**Días de**<br>**Alerta**|**Días de**<br>**Preemergen**<br>**cia**|**Días de**<br>**Emergencia**|**Días de**<br>**Alerta**|**Días de**<br>**Preemergen**<br>**cia**|**Días de**<br>**Emergencia**|
|2015|0|0|0|8|1|0|
|2017|8|1|0|7|9|0|
|2018|7|9|0|3|2|0|
|2019|3|2|0|2|0|0|
|2020|2|0|0|9|3|0|
|2021|9|3|0|2|1|0|
|2022|2|1|0|8|1|0|

3.1.1.2 Material particulado respirable (MP2.5)

En la siguiente figura, se observan las concentraciones promedió de 24 horas registradas

para los años, entre el 2015 y 2022, que tengan más del 75% de sus datos disponibles.

Podemos observar cómo existe superación de la norma en todos los años, siendo el 2018

el año con mayores concentraciones.

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 11 de 63

**Figura 4: Concentración Promedio 24 horas MP2,5 Estación Curicó.**

Respecto a la concentración promedio anual de MP2,5 que establece el D.S. 12/2011 MMA,

podemos observar de la Tabla 4 que en todos los años analizados es superada la normativa,

siendo en particular el año 2020 aquel que cuenta con un mayor porcentaje de excedencia,

con un 30,8%.

**Tabla 4. Concentración promedio anual MP2,5 estación Curicó**

|Año|Porcentaje de<br>datos<br>disponibles (%)|Concentración<br>Promedio Anual<br>(μg/m3)|Límite normativo<br>D.S. 12/2011 MMA<br>(μg/m3)|Porcentaje de<br>excedencia de la<br>norma (%)|
|---|---|---|---|---|
|2015|99,8 %|25,8|20,0|28,9 %|
|2016|-|-|-|-|
|2017|99,6 %|23,4|23,4|17,0 %|
|2018|99,8 %|24,7|24,7|23,5 %|
|2019|99,5 %|22,8|22,8|14,1 %|
|2020|99,7 %|26,2|26,2|30,8 %|
|2021|99,6 %|22,6|22,6|13,2 %|

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 12 de 63

|Año|Porcentaje de<br>datos<br>disponibles (%)|Concentración<br>Promedio Anual<br>(μg/m3)|Límite normativo<br>D.S. 12/2011 MMA<br>(μg/m3)|Porcentaje de<br>excedencia de la<br>norma (%)|
|---|---|---|---|---|
|2022|99,6 %|23,4||17,0 %|

Con respecto a las concentraciones de MP2,5 como promedio trianual, esta fue caracterizada

para cuatro periodos, y tal como se evidencia en la siguiente figura, existe superación

normativa en todos los periodos analizados, siendo el primer Interval (2017-2019) el que

presenta mayor concentración con un 24,5 μg/m [3] .

**Figura 5. Concentración promedio trianual MP2,5, EMRP Curicó**

Además, para el período analizado, se registraron 31 días declarados con alerta, siendo el

año 2021, el que exhibe un mayor número de días en esta condición, presentando 9 días

de alerta. En cuanto a los estados de preemergencia y/o emergencia, se registraron 10 días

de preemergencia y 0 días de emergencia, tal como muestra la siguiente tabla:

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

**4** **Justificación de los modelos utilizados en el estudio.**

Página 13 de 63

El Servicio de Evaluación Ambiental en la “Guía para el Uso de Modelos de Calidad del Aire

en el SEIA” (2023) hace una serie de recomendaciones para la modelación de contaminantes

primarios [1] y secundarios en el aire. En la actualidad, esta guía es el único documento

existente como parámetro para la modelación de calidad del aire y tiene como objetivo

uniformar los criterios, exigencias técnicas y antecedentes para la evaluación de los impactos

asociados a este componente de proyectos que ingresen al Servicio de Evaluación

Ambiental. Dentro de las recomendaciones de la guía está el uso del modelo de dispersión

CALPUFF y sugiere la utilizar el modelo meteorológico WRF, los cuales fueron utilizados en

la modelación de las partículas del proyecto.

A continuación, se presenta la justificación de los modelos utilizados en el proyecto para

ejecución de la modelación de dispersión y concentración de emisiones partículas en el aire.

**4.1** **Uso modelo WRF**

El modelo Weather Research and Forecasting (WRF), es un modelo numérico de cuatro

dimensiones, recomendado para la generación de datos meteorológicos y es uno de los

modelos de pronóstico meteorológicos más avanzados.

Debido a la falta de una red robusta de estaciones meteorológicas, la “Guía para el Uso de

Modelos de Calidad del Aire en el SEIA” recomienda el uso de WRF por sobre el uso del

CALMET. Además, el mismo documento, sugiere el uso del WRF para la modelación de

dispersión de contaminantes con CALPUFF.

**4.2** **Uso modelo CALPUFF**

La modelación de dispersión atmosférica de partículas provenientes del proyecto se realizó

con un modelo tipo “Puff”, específicamente el modelo CALPUFF. Tal como lo define la guía,

los modelos tipo “puff” son una combinación entre los modelos Gaussianos y los modelos

Lagrangeanos, en el sentido de que esencialmente calculan la dispersión de contaminantes

1 Los contaminantes primarios son los producidos directamente por la actividad humana o la naturaleza a la
atmósfera, dentro de los cuales caben las emisiones odorantes.

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 14 de 63

provenientes de una emisión instantánea, llamada “puff”, a lo largo de una trayectoria. Su

aproximación matemática consiste en estimar la dispersión en forma Gaussiana en cada

punto de una trayectoria; es decir, los modelos tipo “puff” sólo requieren una trayectoria

por “puff”, lo que hace su cálculo mucho más rápido. En el caso de emisiones continuas, se

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

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 15 de 63

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

[−d] 2σ x [2][a] ~~[]]~~ [ exp[−d] 2σ y [2][c]

2

∞

n=−∞

[+ 2nh)] [2]

2σ z [2] ~~]~~

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

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 16 de 63

**5** **Metodología**

**5.1** **Modelación de partículas**

La modelación de partículas depende en gran parte de las tasas de emisión. Estos son

acoplados a un modelo meteorológico, el que en sí mismo simula las condiciones

meteorológicas para la zona de estudio con una resolución temporal de 1 hora; con estos

factores como variable de entrada al modelo, es simulada la dispersión de las partículas en

un modelo, que determinará la trayectoria de las partículas dentro del área de estudio.

**5.1.1** **Modelación meteorológica**

Para la modelación meteorológica, se utilizó un modelo WRF, construido con datos del año

2022 y resolución de 1 km, de extensión 95 km x 53 km. El modelo WRF es capaz de simular

el comportamiento meteorológico, a través de datos meteorológicos para el año de estudio,

el que posteriormente es interpolado dentro del área de estudio del modelo de acuerdo con

la topografía del lugar. En la Tabla 5 se resumen las características del modelo.

**Tabla 5. Características del modelo**

|Año de modelación|Col2|2022|
|---|---|---|
|**Periodo de Modelación**|**Periodo de Modelación**|1 año calendario|
|**Resolución temporal**|**Resolución temporal**|1 hora|
|**Resolución espacial**|**Resolución espacial**|1 km|
|**Coordenadas del centroide**|**Latitud**|-34,99°|
|**Coordenadas del centroide**|**Longitud**|-71,59°|
|**DATUM**|**DATUM**|NWS - 84|
|**Coordenadas del modelo**|**Coordenadas del modelo**|LCC|
|**Dominio de modelación**|**X **|95|
|**Dominio de modelación**|**Y **|53|
|**Dominio de modelación**|**Z **|10|

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

**5.1.2** **Modelación de dispersión de contaminantes**

Página 17 de 63

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

valores sub dimensionados, por lo tanto, en ocasiones es necesario realizar una sub

grilla de modelación a través de la modelación de puntos discretos, aumentando la

densidad de puntos de modelación y mejorando la evaluación de la concentración

simulada dentro del espacio circundante. De este modo, se generó una subgrilla de

2,0 km x 2,0 km desde el centroide del proyecto con una resolución de 250 metros.

 **Modelación de puntos discretos.** Se consideraron 15 puntos discretos cercanos

al proyecto junto a la EMRP Curicó. A continuación, se presenta en la Tabla 6 las

coordenadas, y en la Figura 6 la distribución espacial de los receptores discretos.

2 Como es el caso del tránsito y de las obras asociadas al movimiento de tierra.

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

**Tabla 6. Descripción de los puntos receptores**

Página 18 de 63

|Recepto<br>r|Coordenada UTM WGS 84 HUSO 19<br>S|Col3|Distancia al centro del proyecto<br>(m)|Descripció<br>n|
|---|---|---|---|---|
|**Recepto**<br>**r **|**Este (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|
|R1|243.389,9|6.126.261,1|70,6|Casa<br>habitación<br>existente|
|R2|243.292,3|6.126.350,4|122,2|Casa<br>habitación<br>existente|
|R3|243.540,8|6.126.111,6|245,1|Casa<br>habitación<br>existente|
|R4|243.219,0|6.126.431,6|230,2|Casa<br>habitación<br>existente|
|R5|243.462,7|6.126.397,1|219,3|Casa<br>habitación<br>existente|
|R6|243.375,1|6.126.507,2|283,9|Casa<br>habitación<br>existente|
|R7|243.090,6|6.126.511,3|321,6|Casa<br>habitación<br>existente|
|R8|243.239,2|6.126.560,5|344,2|Casa<br>habitación<br>existente|
|R9|243.681,7|6.126.248,3|355,3|Casa<br>habitación<br>existente|
|R9|2436.98,5|6.126.089,1|398,9|Casa<br>habitación<br>existente|
|R10|243.796,5|6.126.411,2|501,1|Estadio<br>Municipal<br>Hualañé|
|R11|243.905,4|6.126.203,2|580,4|Liceo<br>Hualañé|

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 19 de 63

|Recepto<br>r|Coordenada UTM WGS 84 HUSO 19<br>S|Col3|Distancia al centro del proyecto<br>(m)|Descripció<br>n|
|---|---|---|---|---|
|**Recepto**<br>**r **|**Este (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|
|R12|243.877,7|6.125.975,9|605,6|Hospital<br>Municipal<br>Hualañé|
|R13|243.910,0|6.126.334,0|591,9|Escuela|
|R14|242.778,5|6.126.643,1|688,3|Casa<br>habitación<br>existente|
|R15|243.389,9|6.126.261,1|70,6|Casa<br>habitación<br>existente|

**Figura 6. Receptores discretos**

**5.1.3** **Criterios para la modelación de partículas**

El año 1 corresponde al año con mayor emisión del proyecto, donde se lleva a cabo la etapa

de construcción de las mejoras de la PTAS más la operación de la planta sin modificaciones.

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 20 de 63

Para la modelación se ingresaron los polígonos que representan el área de construcción en

el año 1, donde se ejecutan las actividades de escarpe, tala, excavación, compactación,

carga de material y uso de maquinaria, los polígonos donde se genera el tránsito en rutas

no pavimentadas al interior del proyecto, los polígonos representantes del tránsito no

pavimentado externo al proyecto, y en rutas pavimentadas externas más cercanas al

proyecto.

Adicionalmente, se modelaron las emisiones de gases precursores de MP10 y MP2,5 en el

aire a través del módulo MESOPUFF II.

De acuerdo con la metodología aplicable, se realizaron polígonos representativos de cada

unidad para la simulación de las áreas de emisiones de partículas las que, fueron modeladas

como fuentes de emisión discontinuas, es decir, dentro del ciclo diurno, se consideró la

generación de emisiones durante 9 horas (9:00 a 18:00 hrs), ya que ese es el horario laboral

establecido para el proyecto. Para las actividades de tránsito se consideraron factores de

escalamientos en base al número de viajes que se realizan en la ruta y la distancia de estas.

Las coordenadas y su representación se encuentran en la siguiente tabla, así como también,

en la se presenta la ubicación espacial de éstos.

**Tabla 7. Coordenadas de modelación de las fuentes areales Fase de**

**Construcción**

|Actividad para<br>modelar|Unidad del<br>proyecto|Área (m2)|Coordenada UTM, HUSO 19 S,<br>DATUM WGS 84|Col5|
|---|---|---|---|---|
|**Actividad para**<br>**modelar**|**Unidad del**<br>**proyecto**|**Área (m2) **|**Este (m)**|**Norte (m)**|
|Preparación<br>Terreno|P1|1000 <br>|243.256,62|6.126.242,89|
|Preparación<br>Terreno|P1|1000 <br>|243.263,34|6.126.262,37|
|Preparación<br>Terreno|P1|1000 <br>|243.304,28|6.126.228,15|
|Preparación<br>Terreno|P1|1000 <br>|243.310,01|6.126.247,13|
|Preparación<br>Terreno|P2|1200 <br>|243.226,01|6.126.242,01|
|Preparación<br>Terreno|P2|1200 <br>|243.250,79|6.126.232,52|
|Preparación<br>Terreno|P2|1200 <br>|243.208,95|6.126.200,39|
|Preparación<br>Terreno|P2|1200 <br>|243.233,48|6.126.190,37|
|Preparación<br>Terreno|P3|1600 <br>|243.233,24|6.126.115,61|
|Preparación<br>Terreno|P3|1600 <br>|243.241,85|6.126.140,52|
|Preparación<br>Terreno|P3|1600 <br>|243.293,59|6.126.097,55|
|Preparación<br>Terreno|P3|1600 <br>|243.300,54|6.126.121,46|

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 21 de 63

|Actividad para<br>modelar|Unidad del<br>proyecto|Área (m2)|Coordenada UTM, HUSO 19 S,<br>DATUM WGS 84|Col5|
|---|---|---|---|---|
|**Actividad para**<br>**modelar**|**Unidad del**<br>**proyecto**|**Área (m2) **|**Este (m)**|**Norte (m)**|
|**Actividad para**<br>**modelar**|P4|1600 <br>|243.225,07|6.126.090,09|
|**Actividad para**<br>**modelar**|P4|1600 <br>|243.232,87|6.126.114,29|
|**Actividad para**<br>**modelar**|P4|1600 <br>|243.285,92|6.126.071,96|
|**Actividad para**<br>**modelar**|P4|1600 <br>|243.293,03|6.126.096,05|
|**Actividad para**<br>**modelar**|P5|200 <br>|243.184,33|6.126.108,06|
|**Actividad para**<br>**modelar**|P5|200 <br>|243.197,77|6.126.103,84|
|**Actividad para**<br>**modelar**|P5|200 <br>|243.179,95|6.126.094,93|
|**Actividad para**<br>**modelar**|P5|200 <br>|243.193,02|6.126.090,22|
|Grupo<br>electrógeno|P6|3 <br>|243.223,87|6.126.188,43|
|Grupo<br>electrógeno|P6|3 <br>|243.225,65|6.126.187,82|
|Grupo<br>electrógeno|P6|3 <br>|243.223,38|6.126.187,02|
|Grupo<br>electrógeno|P6|3 <br>|243.224,95|6.126.186,36|
|Ruta Interna No<br>Pavimentada|P7|138 <br>|243.232,32|6.126.181,34|
|Ruta Interna No<br>Pavimentada|P7|138 <br>|243.234,98|6.126.180,51|
|Ruta Interna No<br>Pavimentada|P7|138 <br>|243.252,01|6.126.228,28|
|Ruta Interna No<br>Pavimentada|P7|138 <br>|243.254,14|6.126.226,51|
|Ruta Interna No<br>Pavimentada|P8|47.9 <br>|243.251,97|6.126.228,38|
|Ruta Interna No<br>Pavimentada|P8|47.9 <br>|243.254,17|6.126.226,51|
|Ruta Interna No<br>Pavimentada|P8|47.9 <br>|243.267,98|6.126.236,51|
|Ruta Interna No<br>Pavimentada|P8|47.9 <br>|243.268,52|6.126.233,51|
|Ruta Interna No<br>Pavimentada|P9|246 <br>|243.268,09|6.126.236,51|
|Ruta Interna No<br>Pavimentada|P9|246 <br>|243.268,56|6.126.233,44|
|Ruta Interna No<br>Pavimentada|P9|246 <br>|243.354,62|6.126.209,62|
|Ruta Interna No<br>Pavimentada|P9|246 <br>|243.353,85|6.126.207,03|
|Ruta Externa No<br>Pavimentada|P10|115 <br>|243.353,85|6.126.207,03|
|Ruta Externa No<br>Pavimentada|P10|115 <br>|243.354,66|6.126.209,65|
|Ruta Externa No<br>Pavimentada|P10|115 <br>|243.391,09|6.126.188,09|
|Ruta Externa No<br>Pavimentada|P10|115 <br>|243.392,58|6.126.190,38|
|Ruta Externa No<br>Pavimentada|P11|371 <br>|243.391,16|6.126.188,06|
|Ruta Externa No<br>Pavimentada|P11|371 <br>|243.392,58|6.126.190,31|
|Ruta Externa No<br>Pavimentada|P11|371 <br>|243.487,73|6.126.087,68|
|Ruta Externa No<br>Pavimentada|P11|371 <br>|243.489,48|6.126.089,59|
|Ruta Externa No<br>Pavimentada|P12|279 <br>|243.487,59|6.126.091,68|
|Ruta Externa No<br>Pavimentada|P12|279 <br>|243.489,51|6.126.089,73|
|Ruta Externa No<br>Pavimentada|P12|279 <br>|243.543,35|6.126.174,06|
|Ruta Externa No<br>Pavimentada|P12|279 <br>|243.545,48|6.126.172,37|
||P13|777|243.543,33|6.126.174,13|

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 22 de 63

|Actividad para<br>modelar|Unidad del<br>proyecto|Área (m2)|Coordenada UTM, HUSO 19 S,<br>DATUM WGS 84|Col5|
|---|---|---|---|---|
|**Actividad para**<br>**modelar**|**Unidad del**<br>**proyecto**|**Área (m2) **<br>|**Este (m)**|**Norte (m)**|
|**Actividad para**<br>**modelar**|**Unidad del**<br>**proyecto**|**Área (m2) **<br>|243.545,56|6.126.172,44|
|**Actividad para**<br>**modelar**|**Unidad del**<br>**proyecto**|**Área (m2) **<br>|243.685,01|6.126.413,55|
|**Actividad para**<br>**modelar**|**Unidad del**<br>**proyecto**|**Área (m2) **<br>|243.687,24|6.126.411,92|
|**Actividad para**<br>**modelar**|P14|2670 <br>|243.685,85|6.126.409,35|
|**Actividad para**<br>**modelar**|P14|2670 <br>|243.687,32|6.126.411,87|
|**Actividad para**<br>**modelar**|P14|2670 <br>|244.418,96|6.125.831,45|
|**Actividad para**<br>**modelar**|P14|2670 <br>|244.420,45|6.125.833,83|
|**Actividad para**<br>**modelar**|P15|313 <br>|244.418,96|6.125.831,37|
|**Actividad para**<br>**modelar**|P15|313 <br>|244.420,57|6.125.833,81|
|**Actividad para**<br>**modelar**|P15|313 <br>|244.517,33|6.125.785,76|
|**Actividad para**<br>**modelar**|P15|313 <br>|244.518,74|6.125.788,19|
|**Actividad para**<br>**modelar**|P16|81.8 <br>|244.517,35|6.125.785,73|
|**Actividad para**<br>**modelar**|P16|81.8 <br>|244.518,82|6.125.788,25|
|**Actividad para**<br>**modelar**|P16|81.8 <br>|244.540,45|6.125.769,98|
|**Actividad para**<br>**modelar**|P16|81.8 <br>|244.542,03|6.125.772,42|
|**Actividad para**<br>**modelar**|P17|572 <br>|244.540,45|6.125.769,95|
|**Actividad para**<br>**modelar**|P17|572 <br>|244.54,11|6.125.772,37|
|**Actividad para**<br>**modelar**|P17|572 <br>|244.697,61|6.125.648,23|
|**Actividad para**<br>**modelar**|P17|572 <br>|244.699,57|6.125.650,21|
|**Actividad para**<br>**modelar**|P18|79.6 <br>|244.697,64|6.125.648,18|
|**Actividad para**<br>**modelar**|P18|79.6 <br>|244.699,63|6.125.650,18|
|**Actividad para**<br>**modelar**|P18|79.6 <br>|244.722,33|6.125.633,45|
|**Actividad para**<br>**modelar**|P18|79.6 <br>|244.723,46|6.125.636,04|
|**Actividad para**<br>**modelar**|P19|339 <br>|244.722,33|6.125.633,42|
|**Actividad para**<br>**modelar**|P19|339 <br>|244.723,49|6.125.635,96|
|**Actividad para**<br>**modelar**|P19|339 <br>|244.832,33|6.125.588,58|
|**Actividad para**<br>**modelar**|P19|339 <br>|244.833,83|6.125.590,93|
|**Actividad para**<br>**modelar**|P20|1525 <br>|244.832,33|6.125.588,49|
|**Actividad para**<br>**modelar**|P20|1525 <br>|244.833,86|6.125.590,96|
|**Actividad para**<br>**modelar**|P20|1525 <br>|245.254,27|6.125.301,47|
|**Actividad para**<br>**modelar**|P20|1525 <br>|245.255,98|6.125.304,02|
|**Actividad para**<br>**modelar**|P21|1447 <br>|243.544,03|6.126.170,21|
|**Actividad para**<br>**modelar**|P21|1447 <br>|243.545,53|6.126.172,39|
|**Actividad para**<br>**modelar**|P21|1447 <br>|244.037,76|6.125.970,84|
|**Actividad para**<br>**modelar**|P21|1447 <br>|244.039,03|6.125.973,21|
|**Actividad para**<br>**modelar**|P22|679|244.037,81|6.125.970,81|
|**Actividad para**<br>**modelar**|P22|679|244.039,15|6.125.973,16|

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 23 de 63

|Actividad para<br>modelar|Unidad del<br>proyecto|Área (m2)|Coordenada UTM, HUSO 19 S,<br>DATUM WGS 84|Col5|
|---|---|---|---|---|
|**Actividad para**<br>**modelar**|**Unidad del**<br>**proyecto**|**Área (m2) **|**Este (m)**|**Norte (m)**|
|**Actividad para**<br>**modelar**|**Unidad del**<br>**proyecto**|**Área (m2) **|244.262,16|6.125.884,23|
|**Actividad para**<br>**modelar**|**Unidad del**<br>**proyecto**|**Área (m2) **|244.263,43|6.125.886,83|
|**Actividad para**<br>**modelar**|P23|145|244.260,94|6.125.887,87|
|**Actividad para**<br>**modelar**|P23|145|244.263,51|6.125.886,89|
|**Actividad para**<br>**modelar**|P23|145|244.290,53|6.125.932,55|
|**Actividad para**<br>**modelar**|P23|145|244.292,58|6.125.930,96|

**Figura 7. Polígonos de modelación representativos de cada unidad modelada**

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 24 de 63

**6** **Resultados**

**6.1** **Modelamiento meteorológico**

Se procederá a presentar los resultados de la modelación meteorológica para el año 2022,

los cuales extrajeron del punto de grilla más cercano a la ubicación del proyecto.

**6.1.1** **Caracterización geofísica de la zona de estudio**

En la Figura 7, se observa la elevación del terreno en el dominio de la modelación WRF, La

fuente de información topográfica del dominio de modelación corresponde a cartas

topográficas digitales adquiridos desde la base de “U.S.GeologicalSurvey (USGS)- Global

Multi-resolution Terrain Elevation Data 2010 (GMTED2010)” con curvas de nivel de

resolución 30 [arc-segundos], equivalente a 920 [m] aproximadamente.

Como podemos ver, el proyecto se ubica en la cota topográfica en torno a los 50 m.s.n.m,

en lo que se denomina cordillera de la costa.

**Figura 8:** Elevación del terreno en el área de la modelación meteorológica

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 25 de 63

**6.1.2** **Caracterización de la velocidad y dirección de los vientos Anual**

En la siguiente figura se muestra la rosa de los vientos construida con los datos modelados

para el año 2022.

**Figura 9** : Rosa de vientos para el año 2022

Podemos ver que la dirección del viento, en la zona de emplazamiento del proyecto, tiene

como origen predominante el oeste noroeste, sur y sureste, las cuales corresponden a un

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 26 de 63

45,2% de las direcciones modeladas. En particular, la frecuencia de vientos con un origen

del oeste noroeste es de un 17,6%, del sur de un 16,7% y del sur sureste de un 10,9%

En la siguiente figura, podemos observar la frecuencia de la magnitud del viento en el

periodo modelado. Podemos observar que hay las velocidades entre los rangos 3,6-5,7 m/s

representan el 32,2% de los datos modelados, las cuales son aquellos con mayor frecuencia

en la zona de emplazamiento del proyecto. Además, podemos ver que el 8,1% de los

vientos, son calmos.

**Figura 10:** Frecuencia de la velocidad de los vientos anual

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 27 de 63

**6.1.3** **Caracterización de la velocidad y dirección de los vientos Estacional**

**6.1.3.1** **Caracterización de la velocidad y dirección de los vientos en verano**

En la siguiente figura se muestra la rosa de los vientos construida con los datos modelados

para el verano del año 2022.

**Figura 11** : Rosa de vientos para el verano, año 2022

Podemos ver que la dirección del viento, en la zona de emplazamiento del proyecto, tiene

como origen predominante el oeste noroeste, oeste y sur, las cuales corresponden a un

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 28 de 63

64,1% de las direcciones modeladas. En particular, la frecuencia de vientos con un origen

del oeste noroeste es de un 32,1%, del oeste de un 16,5% y del sur sureste de un 15,6%

En la siguiente figura, podemos observar la frecuencia de la magnitud del viento en el

periodo modelado. Podemos observar que hay las velocidades entre los rangos 3,6-5,7 m/s

representan el 27,6% de los datos modelados, mientras que las velocidades entre 0,5-2,1

m/s tiene una frecuencia de 23,3% y aquellas entre 5,7-8,8% un 21,9%. Además, podemos

ver que el 8,6% de los vientos, son calmos.

**Figura 12:** Frecuencia de la velocidad de los vientos en verano

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 29 de 63

6.1.3.2 Caracterización de la velocidad y dirección de los vientos en otoño

En la siguiente figura se muestra la rosa de los vientos construida con los datos modelados

para el otoño del año 2022.

**Figura 13** : Rosa de vientos para el otoño, año 2022

Podemos ver que la dirección del viento, en la zona de emplazamiento del proyecto, tiene

como origen predominante el sur, sur sureste y oeste noroeste, las cuales corresponden a

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 30 de 63

un 54,4% de las direcciones modeladas. En particular, los vientos con origen sur tienen una

frecuencia de 24,0%, seguido por la dirección sur sureste con un 16,3% y finalmente el

oeste noroeste con un 14,4%.

En la siguiente figura, podemos observar la frecuencia de la magnitud del viento en el

periodo modelado. Podemos observar que las velocidades en el rango 0,5-2,1 representan

un 34,7% de las velocidades modeladas, seguido por el rango entre 3,6-5,7 m/s, con un

20,6% y las calmas con 19,4%.

**Figura 14:** Frecuencia de la velocidad de los vientos en otoño

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 31 de 63

6.1.3.3 Caracterización de la velocidad y dirección de los vientos en invierno

En la siguiente figura se muestra la rosa de los vientos construida con los datos modelados

para el otoño del año 2022.

**Figura 15** : Rosa de vientos para el invierno, año 2022

Podemos ver que la dirección del viento, en la zona de emplazamiento del proyecto, tiene

como origen predominante el noreste, nor noreste y sur sureste, las cuales corresponden a

un 41,0% de las direcciones modeladas. En particular, los vientos con origen noreste tienen

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 32 de 63

una frecuencia de 14,8%, seguido por la dirección sur sureste con un 13,9% y finalmente

el nor noreste con un 12,8%.

En la siguiente figura, podemos observar la frecuencia de la magnitud del viento en el

periodo modelado. Podemos observar que las velocidades en el rango 3,6-5,7 representan

un 33,8% de las velocidades modeladas, seguido por el rango entre 0,5-2,1 m/s y 2,1-3,6

m/s, con un 22% y 21,9%. Las calmas representan un 6,6% de los datos modelados.

**Figura 16:** Frecuencia de la velocidad de los vientos en invierno

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 33 de 63

6.1.3.4 Caracterización de la velocidad y dirección de los vientos en primavera

En la siguiente figura se muestra la rosa de los vientos construida con los datos modelados

para el otoño del año 2022.

**Figura 17** : Rosa de vientos para la primavera, año 2022

Podemos ver que la dirección del viento, en la zona de emplazamiento del proyecto, tiene

como origen predominante el oeste noroeste, sur y oeste, las cuales corresponden a un

46,6% de las direcciones modeladas. En particular, los vientos con origen oeste noroeste

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 34 de 63

tienen una frecuencia de 19,7%, seguido por la dirección sur con un 14,9% y finalmente el

oeste con un 12,7%.

En la siguiente figura, podemos observar la frecuencia de la magnitud del viento en el

periodo. Podemos observar que las velocidades en el rango 3,6-5,7 representan un 32,7%

de las velocidades modeladas, seguido por el rango entre 2,1-3,6 m/s y 0,5-2,1 m/s, con

un 23,5% y 20,5%. Las calmas representan un 6,5% de los datos modelados.

**Figura 18:** Frecuencia de la velocidad de los vientos en invierno

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

6.1.3.5 Caracterización del ciclo diario del viento.

Página 35 de 63

En la Figura 19 se presenta el perfil horario promedio de la magnitud y dirección del viento,

modeladas con WRF, para cada mes del año 2022.

**Figura 19:** Ciclo Diario del Viento

Podemos apreciar como la magnitud del viento, durante todo el año, tiende a tener

magnitudes menores entre las 00:00 UTC y las 10:00 UTC, para luego aumentar en las

horas en magnitud hasta sobrepasar los 6 m/s entre las 14:00 y 15:00 UCT, luego comienza

a disminuir hasta completar el ciclo. El patrón distrito se conserva prácticamente se conserva

durante todo el año, con variaciones en la magnitud del viento, exceptuando el mes de

mayo donde pareciera que la rapidez del viento se oscila entre 2 y 3 m/s.

Con respecto a la dirección del viento podemos observar en que durante las 00:00 UTC y

las 09:00 UTC, tenemos viento del sur durante todo el año, exceptuando el mes de junio,

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 36 de 63

donde se es principalmente del este. Entre las 12:00 Y 19:00 UTC tenemos una variación

del comportamiento de la dirección del viento, En los meses de verano, el viento es

principalmente del oeste, pero a partir de marzo comienza a haber viento del oeste sur oeste

y a medida que se desarrolla el invierno, vemos que el viento pasa a ser más del suroeste,

para luego ir retomando el ciclo hacia diciembre. En junio tenemos un casi particular, donde

el viento del suroeste pasa a ser del sur este o sur sureste. Luego de las 19:00 UTC, el

viento vuelve a comportarse de forma similar al visto entre las 00:00 UTC y 09:00 UTC.

**6.1.4** **Caracterización de la Temperatura del Aire**

En la Figura 20 se presenta el perfil horario promedio de la magnitud y dirección del viento,

modeladas con WRF, para cada mes del año 2022.

**Figura 20:** Ciclo Diario para la Temperatura

En la figura podemos ver 2 ciclos muy claros y marcados, el primero de ellos es ciclo diario,

donde la temperatura va aumentando paulatinamente a partir de las 06:00 UTC hasta las

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 37 de 63

14:00 UTC, para luego volver a disminuir. El segundo ciclo que observamos el estacional, el

cual va modificando el ciclo diario a medida que pasamos del verano al otoño e invierno,

con temperaturas menores y disminuyendo la cantidad de horas en que se alcanzan las

máximas temperaturas.

**6.1.5** **Caracterización de la Precipitación**

En la Figura 21 podemos observar la precipitación mensual modelada por WRF. Tenemos

que la precipitación anual es de 431,4 mm.

**Figura 21:** Precipitación Mensual

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 38 de 63

Con respecto a la distribución mensual, podemos apreciar claramente como en la zona de

emplazamiento del proyecto hay una temporada húmeda que va desde abril hasta

septiembre, en donde se concentra más del 80% de la precipitación anual.

**6.1.6** **Altura Capa de meza**

En la Figura 22 podemos ver el ciclo diario promedio, para cada mes del año, de la altura

de la capa limite modelada en la zona de emplazamiento del proyecto (medida en metros)

**Figura 22:** Ciclo diario de altura de la capa limite

Podemos observar como la capa limite tiene un claro ciclo diario, en donde las menores

alturas se alcanzan durante las 00:00 y las 06:00 UTC y entre las 18:00 y las 23:00 UTC,

mientras que entre las 07:00 y las 12:00 UTC aumenta paulatinamente hasta sus valores

máximos para luego disminuir.

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 39 de 63

Con respecto a la variación mensual de ciclo diario, vemos que en los meses de invierno se

alcanzan valores mínimos mayores que duran el resto de los meses, mientras que los

máximos de altura son menores.

**6.2** **Concentraciones Modeladas**

A continuación, se presentan los resultados de la modelación de material particulado

emitidos a la atmosfera. Cabe recordar que, el escenario modelado corresponde a las

emisiones de material particulado, tanto MP10 como MP2,5, las cuales se producen en la

fase de construcción del proyecto durante el año 1, las cuales consideran también las

emisiones producidas en un año por la operación de la planta sin modificar.

**6.2.1** **Dispersión e Isoconcentración Material Particulado Respirable,**

**MP10**

A continuación, se presenta el análisis de los resultados para el MP10 tanto para la

concentración promedio anual y 24 horas.

Es importante señalar que la pluma de dispersión de MP10 simulada por el modelo abarca

la zona de emplazamiento del proyecto, donde se produce la construcción de la planta,

extendiéndose en menor concentración por los alrededores del proyecto.

**6.2.1.1** **Concentración promedio anual de MP10**

En la Figura 23, se muestra la pluma de dispersión de la concentración promedio anual de

MP2,5, de donde se concluye que:

 El comportamiento del material particulado como concentración promedio anual,

concentra sus máximas concentraciones en el último tramo de las rutas externas no

pavimentadas, desde donde se desplazan principalmente hacia oeste.

 La concentración generada en la atmósfera por las emisiones de MP10 varían

desde los 0,10 a los 0,22 μg/m3.

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 40 de 63

De los puntos receptores modelados, dos se ubican dentro de la pluma de dispersión,

los receptores R1 y R3.

En la Figura 24, se muestra el mapa de isoconcentración, de donde se puede concluir

que:

En relación con la dimensión, la pluma se extiende hasta los 259,1 m por el norte y

145,2 m por el sur, 137,6 m al este y 345,8 m al oeste desde la zona de mayor

concentración. A estas distancias la concentración esperada es de 0,22 μg/m3. La

distribución de la pluma se presenta de forma alargada en la dirección oeste.

Se distingue una zona de máxima concentración de 0,02 ha en donde las

concentraciones superan los 0,21 μg/m3, principalmente en el polígono que

representa las rutas externas no pavimentadas.

El área total de la pluma de isoconcentración abarca una superficie de 13,40 ha.

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 41 de 63

**Figura 23. Dispersión de la pluma de MP10 como concentración anual.**

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 42 de 63

**Figura 24. isolíneas de concentración de MP10 como concentración promedio**

**Anual**

**6.2.1.2** **Concentración promedio 24 horas de MP10**

En la Figura 25, se muestra la pluma de dispersión de la concentración promedio anual de

MP2,5, de donde se concluye que:

 El comportamiento del material particulado como concentración promedio anual,

concentra sus máximas concentraciones en el último tramo de las rutas externas no

pavimentadas, desde donde se desplazan principalmente hacia oeste.

 La concentración generada en la atmósfera por las emisiones de MP10 varían

desde los 0,50 a los 1,20 μg/m3.

 De los puntos receptores modelados, uno se ubica dentro de la pluma de dispersión,

los receptores R1.

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 43 de 63

En la Figura 26, se muestra el mapa de isoconcentración, de donde se puede concluir

que:

 En relación con la dimensión, la pluma se extiende hasta los 259,1 m por el norte y

166,7 m por el sur, 325,7 m al este y 239,2 m al oeste desde la zona de mayor

concentración. A estas distancias la concentración esperada es de 0,50 μg/m3. La

distribución de la pluma se presenta de forma alargada en la dirección noreste.

 Se distingue una zona de máxima concentración de 1,71 ha en donde las

concentraciones superan los 1,20 μg/m3, principalmente en el polígono que

representa las rutas externas no pavimentadas, la preparación del terreno y las rutas

internas no pavimentadas.

 El área total de la pluma de isoconcentración abarca una superficie de 23,90 ha.

**Figura 25. Dispersión de la pluma de MP10 como concentración de 24 horas.**

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 44 de 63

**Figura 26. Isolíneas de concentración de MP10 como concentración de 24 horas**

**6.2.2** **Dispersión e Isoconcentración Material Particulado Fino Respirable,**

**MP 2.5**

A continuación, se presenta el análisis de los resultados para el MP2,5, tanto para la

concentración promedio anual y 24 horas.

**6.2.2.1** **Concentración promedio anual de MP2,5**

En la Figura 27, se muestra la pluma de dispersión de la concentración promedio anual de

MP2,5, de donde se concluye que:

 El comportamiento del material particulado como concentración promedio anual,

concentra sus máximas concentraciones en el tramo de las rutas externas no

pavimentadas, desde donde se desplazan principalmente hacia suroeste.

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 45 de 63

La concentración generada en la atmósfera por las emisiones de MP2,5 varían

desde los 0,13 a los 0,22 μg/m3.

De los puntos receptores modelados, dos se ubican dentro de la pluma de dispersión,

los receptores R1 y R3.

En la Figura 28, se muestra el mapa de isoconcentración, de donde se puede concluir

que:

En relación con la dimensión, la pluma se extiende hasta los 123,3 m por el norte y

150,2 m por el sur, 171,6 m al este y 227,3 m al oeste desde la zona de mayor

concentración. A estas distancias la concentración esperada es de 0,13 μg/m3. La

distribución de la pluma se presenta de forma alargada en la dirección suroeste.

Se distingue una zona de máxima concentración de 0,51 ha en donde las

concentraciones superan los 0,2 μg/m3, principalmente en el polígono que

representa las rutas externas no pavimentadas.

El área total de la pluma de isoconcentración abarca una superficie de 8,80 ha.

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 46 de 63

**Figura 27. Dispersión de la pluma de MP2,5 como concentración promedio**

**anual**

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 47 de 63

**Figura 28. isolíneas de concentración de MP2,5 como concentración promedio**

**anual.**

**6.2.2.2** **Concentración promedio 24 horas de MP2,5**

En la Figura 29, se muestra la pluma de dispersión de la concentración promedio 24 horas

de MP2,5, de donde se concluye que:

 El comportamiento del material particulado como concentración promedio 24 horas,

concentra sus máximas concentraciones en el centro del proyecto, desde donde se

desplazan principalmente hacia noreste.

 La concentración generada en la atmósfera por las emisiones de MP2,5 varían

desde los 0,09 a los 0,15 μg/m3.

 De los puntos receptores modelados, solo uno se ubica dentro de la pluma de

dispersión, los receptores R1.

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 48 de 63

En la Figura 30, se muestra el mapa de isoconcentración, de donde se puede concluir

que:

En relación con la dimensión, la pluma se extiende hasta los 153,6 m por el norte y

146,9 m por el sur, 263,0 m al este y 125,5 m al oeste desde la zona de mayor

concentración. A estas distancias la concentración esperada es de 0,09 μg/m3. La

distribución de la pluma se presenta de forma alargada en la dirección noreste.

Se distingue una zona de máxima concentración de 0,29 ha en donde las

concentraciones superan los 0,15 μg/m3, principalmente en la PTAS.

El área total de la pluma de isoconcentración abarca una superficie de 9,60 ha.

**Figura 29. dispersión de la pluma de MP2,5 como concentración 24 horas.**

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 49 de 63

**Figura 30. Isolíneas de concentración de MP2,5 como concentración 24 horas**

**6.2.3** **Modelación discreta de las emisiones contaminantes**

La modelación discreta de emisiones fue realizada para MP10 y MP2,5 cuyos valores de

concentración para los puntos receptores son presentados en la siguiente tabla. Tal como

se ha mencionado, estos puntos corresponden principalmente a lugares de encuentro de la

población cercana al proyecto y a los caminos.

De los resultados obtenidos se destaca:

 Todas las concentraciones simuladas son de baja magnitud.

 Respecto a las concentraciones modeladas de MP10, se puede apreciar que las

concentraciones máximas se simularon en el receptor R1, lo que se debe a su

cercanía con la zona de construcción de proyecto, recibiendo las emisiones de las

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 50 de 63

actividades de escarpe, tala, excavación, compactación, carga de material, uso de

maquinaria y tránsito en vías no pavimentadas interna.

 El receptor que recibe el mayor aporte de la concentración de MP2,5 es el mismo

obtenido de la simulación de MP10, dado que el MP2,5 es la fracción fina del material

particulado grueso.

 Las concentraciones modeladas en el receptor R1 de MP10 tanto en concentración

promedio anual y 24 horas, alcanzan valores de 0,207 μg/m [3] y 1,18 μg/m [3],

respectivamente. Para el mismo receptor se simuló una concentración de MP2,5 de

0,025 μg/m [3] como promedio anual y 0,134 μg/m [3] como concentración 24 horas.

 La concentración de menor magnitud es la obtenida en el receptor R15, el que se

encuentra más alejado de la zona del proyecto y también de los caminos externos

del proyecto.

 Respecto al resto de los receptores, las concentraciones oscilan entre los 0,021 y

0,181 μg/m [3] como concentración promedio anual de MP10, y entre los 0,211 y 0,021

μg/m [3] como concentración promedio 24 horas del mismo contaminante. Mientras

que las concentraciones de MP2,5 varían entre valores entre 0,003 y 0,021 μg/m [3]

como concentración promedio anual, y entre 0,032 y 0,084 μg/m [3] como

concentración promedio 24 horas.

|Punto|Concentración MP10 (μg/m3)|Col3|Concentración MP2,5(μg/m3)|Col5|
|---|---|---|---|---|
|**Punto**|**Anual**|**24 horas**|**Anual**|**24 horas**|
|R1|0,207|1,18|0,025|0,134|
|R2|0,057|0,590|0,007|0,073|
|R3|0,182|0,729|0,021|0,084|
|R4|0,047|0,507|0,006|0,064|
|R5|0,033|0,431|0,004|0,058|
|R6|0,031|0,447|0,004|0,056|
|R7|0,039|0,499|0,005|0,061|
|R8|0,032|0.466|0,004|0,058|
|R9|0,084|0,417|0,010|0,052|
|R10|0,053|0,364|0,007|0,045|
|R11|0,028|0,269|0,003|0,034|
|R12|0,040|0,236|0,005|0,028|
|R13|0,024|0,211|0,003|0,028|

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 51 de 63

|Punto|Concentración MP10 (μg/m3)|Col3|Concentración MP2,5(μg/m3)|Col5|
|---|---|---|---|---|
|**Punto**|**Anual**|**24 horas**|**Anual**|**24 horas**|
|R14|0,037|0,234|0,004|0,029|
|R15|0,021|0,249|0,003|0,032|

**6.2.3.1** **Series de tiempo de las concentraciones para cada contaminante**

En esta sección, se analizará las series de tiempo horarias de las concentraciones modeladas

en cada receptor.

**6.2.3.1.1** **Series de tiempo de las concentraciones horarias.**

En la Figura 31 podemos observar la serie de tiempo de las concentraciones horarias de

MP10 modeladas en los distintos receptores.

**Figura 31.** Serie de tiempo de las concentraciones de MP10 modeladas para el año 2022

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 52 de 63

Siguiendo la tónica de los resultados anteriores, podemos ver como los valores más alto se

encuentran en los receptores R1 y R3, mientras que en el resto de los receptores los valores

obtenidos son mucho menores. Con respecto a lo anterior, podemos ver como el percentil

98 (línea marrón) de las concentraciones horarias nos indican que el 98% de las

concentraciones horarias se encuentran bajo los 2,5 μg/m [3] para el receptor R1 y 1,8 μg/m [3]

para el receptor R3, para el resto estos valores son menores a 1.

En la Figura 32 podemos observar la serie de tiempo de las concentraciones horarias de

MP2,5 modeladas en los distintos receptores.

**Figura 32.** Serie de tiempo de las concentraciones de MP10 modeladas para el año 2022

Podemos ver que el comportamiento de las concentraciones de MP2,5 son similares al visto

en MP10, pero con concentraciones menores. En general, las concentraciones en los

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 53 de 63

receptores R1 y R3 las mal altas, así lo demuestran el cálculo de su percentil 98, que dan

valores de 0,29 μg/m [3] y 0,20 μg/m [3], respectivamente.

**7** **Análisis de incertidumbre**

Tal como se plantea en la “Guía para el Uso de Modelos de Calidad del Aire en el SEIA”

(2023) de manera textual “cualquier modelo (meteorológico o de calidad del aire) representa

una aproximación a la realidad y, en consecuencia, sus resultados tienen incertidumbres

asociadas”. Ante lo cual, para cuantificar esta incertidumbre, se realiza un análisis entre los

valores entregados por el modelo WRF (valores meteorológicos) y valores observados, en

este caso los datos son extraídos de la Estación Deuca propiedad de la Red

Agrometeorológica del INIA; estación meteorológica más cercana al proyecto y con datos

disponibles para el año 2022, mismo año de simulación del modelo WRF.

El modelo WRF simuló las condiciones meteorológicas dentro de un rango de 95 x 53 km

celdas de una dimensión de 1 x 1 km. Para efectos del análisis del ajuste de los datos

meteorológicos simulados se seleccionó una celda en donde se ubica la estación Deuca,

desde la cual se extrajeron los datos y se compararon con los valores observados de la

estación meteorológica antes mencionada.

La correlación de los datos se determinó a través del ajuste por mínimos cuadrados, método

en el que existen dos parámetros de importancia: coeficiente de correlación lineal de

Pearson (r) y el coeficiente de determinación ( R [2] ).

El coeficiente de correlación lineal es una medida de relación de Pearson entre dos variables

y se usa para medir el grado de relación entre ellas. El rango de valores va desde el -1 al 1

y está representado por la siguiente ecuación.

r = [σ] [x][y]
xy

σ x . σ y

Donde,

- σ xy, es la covarianza entre x e y;

- σx, es la desviación estándar de x;

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

- σy, es la desviación estándar de y;

Página 54 de 63

El coeficiente de determinación se utiliza como medida de eficiencia de la cobertura de datos

midiendo el porcentaje de variación entre las variables observadas y modeladas, es decir,

testea la capacidad predictiva del modelo e indica la proporción de la varianza de los

resultados que puede ser explicado por el modelo. Los valores del coeficiente de

determinación varían de 0 a 1, siendo este último el valor óptimo y está determinada por la

siguiente relación.

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

n

BIAS = [1]

n [+ ∑(S] [i] [−O] [i] [)]

i=1

Donde,

 - S i, es el valor simulado;

 - O i, es el valor observado.

 - n, es el número de mediciones, en este caso el número de horas en un año, es decir,

8760.

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 55 de 63

Se presenta el Mean Absolute Error (MAE), el cual es una medida del error promedio

absoluto del modelo con respecto a las observaciones. Este estadístico se calcula mediante

a la siguiente formula.

n

MAE = [1]

n [+ ∑|S] [i] [−O] [i] [|]

i=1

Donde,

 - S i, es el valor simulado;

 - O i, es el valor observado.

 - n, es el número de mediciones, en este caso el número de horas en un año, es decir,

8760.

El Root Mean Squeare Error (RMSE) es una medida del desempeño promedio del modelo,

el cual, según él SEA, es un “estimador de la frecuencia de las diferencias entre los valores

observados y modelados, siendo especialmente sensible a los valores atípicos, por lo tanto,

a mayor diferencia entre estos valores menor será el grado de ajuste de este estadístico”.

Esta estadística valores de 0 al infinito, donde 0 es el valor de una modelación sin errores y

va creciendo a medida que decrece la capacidad del modelo de representar la realidad.

n

RMSE = √ [1]

n

n [+ ∑(S] [i] [−O] [i] [)] [2]

i=1

Los resultados del ajuste del modelo meteorológico se presentan en la siguiente tabla. Luego

de ésta, se presenta el detalle de los valores entregados.

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 56 de 63

**Tabla 8.** Resultados estadísticos obtenidos por la modelación

|Variable|Coeficiente de<br>correlación lineal (r)|Coeficiente de<br>determinación (r2)|Bias|MAE|RMSE|
|---|---|---|---|---|---|
|Temperatura<br>horaria|0,85|0,73|-0,42|2,86|3,60|
|Rapidez del<br>viento horaria|0,41|0,17|2,19|2,24|2,92|

**7.1** **Caracterización de la Temperatura Modelada.**

En la **Figura 33** se observa la correlación entre la temperatura horaria observada en la

estación Deuca y las simuladas por el modelo WRF del año 2022.

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 57 de 63

**Figura 33:** Correlación entre temperatura observada y modelada

En la figura anterior se observa que existe una correlación positiva entre la temperatura

observada y la modelada cuyo valor es 0,85. Por otro lado, el coeficiente de determinación

sugiere que el modelo es capaz de representar el 73% de la variabilidad observada.

En la **Figura 34** se observa la frecuencia de las temperaturas en rangos de clases para los

datos modelados y los simulados, donde podemos observar en que en general el modelo

tiene pocas diferencias con las observaciones, en particular se destaca que el modelo no

pudo representar las temperaturas negativas y mayores 30°C que se observaron. Con todo

esto, el valor del Bias concluye, que, en promedio, los datos modelados subestiman las

observaciones en 0,48°C, mientras que la RMSE y el MAE nos muestra que, en promedio,

dicha diferencia está en orden de 3,6°C

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 58 de 63

**Figura 34:** Frecuencia de las temperaturas observadas y modeladas

**7.2** **Caracterización de la Velocidad del viento Modelada y Observada**

En la Figura 35 se observa la correlación entre la temperatura horaria observada en la

estación Deuca y las simuladas por el modelo WRF del año 2022.

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 59 de 63

Figura 35: Correlación entre la rapidez del viento observada y modelada

De la figura anterior se observa que existe una correlación positiva entre la rapidez del

viento observada y la modelada. El valor del coeficiente de correlación lineal es 0,41. Por

otro lado, el coeficiente de determinación sugiere que el modelo es capaz de representar el

17% del comportamiento observado.

En la Figura 26 se observa la frecuencia de magnitudes de rapidez del viento en distintas

categorías. Se ve claramente como el modelo subestima la frecuencia de los vientos calmos

(entre los 0,0 y 0,5 m/s) con respecto a las observaciones. Esto es relevante para la

determinación del área de influencia, dado que la rapidez del viento afecta la extensión

afecta de forma directa la dispersión de los contaminantes. Además, observamos que sobre

estima la frecuencia de los vientos mayores 2,6 m/s en gran media. El Bias mostrado en la

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 60 de 63

tabla anterior, nos indica que el modelo en promedio sobre estima la rapidez del viento, y

el MAE y RMSE nos indica el promedio de dichas diferencias está en el orden de 2-3 m/s.

**Figura 36:** Frecuencia de la rapidez del viento observadas y modeladas

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 61 de 63

**8** **Conclusión**

Se estudió la concentración de las emisiones producto de la construcción proyectada para

el año 1 del proyecto inmobiliario y la operación actual del proyecto “ **MODIFICACIÓN**

**PTAS HUALAÑÉ** ” ubicado en la comuna de Hualañé, Provincia de Curicó, Región de Maule.

De esta forma, fueron modeladas las emisiones MP10 y MP2,5 a fin de determinar las

concentraciones que éstos tendrán en la atmósfera, además de prever posibles efectos a la

salud de las personas.

Tal como se abordó anteriormente en el informe, el desplazamiento de los contaminantes

ocurre mayoritariamente al interior de la zona de emplazamiento del proyecto y en las

proximidades del proyecto. Al respecto se destaca que:

 La pluma de dispersión de MP10 como promedio 24 horas abarca un total de 23,90

ha, donde las concentraciones corresponden a 0,50 μg/m3. La zona de máxima

concentración corresponde a la zona de emplazamiento del proyecto y las rutas no

pavimentadas externas, donde se realizan las actividades de escarpe, tala,

excavación, compactación, carga de material, uso de maquinaria y tránsito en vías

no pavimentadas interna, alcanzando concentraciones de 1,02 μg/m3.

 La pluma de dispersión de MP2,5 se extiende en dirección noreste. La pluma de

MP2,5 abarca una superficie menor a la MP10 y solo alcanza el receptor R1

 Solo los receptores R1 y R3 se encuentra dentro de las plumas generadas,

alcanzando una concentración diaria para MP10 de 0,53 μg/m3.

 Las concentraciones modeladas son de baja magnitud, descartando así, efectos

significativos sobre los receptores cercanos al proyecto.

Es importante considerar que la concentración en el aire de los contaminantes puede ser

influida por diversos factores, entre los cuales están la tasa de emisión, las condiciones en

que los contaminantes son liberados a la atmósfera, la topografía del entorno, e

indudablemente las condiciones meteorológicas, es decir, la dispersión y concentración de

las partículas y gases en el aire quedará determinada por las condiciones ambientales en

donde éstos son liberados, como por ejemplo: gradiente de presión, gradiente de

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 62 de 63

temperatura, velocidad y dirección del viento (los que a su vez están influenciados por las

características topográficas del lugar), entre otros.

Ademas, tal como menciona la guia para el uso de modelos de calidad del aire en el SEIA

todo modelo meteorológico representa una aproximación a la realidad por lo que sus

resultados tienen incertidumbres asociadas (ver apartado 7). Estas incertidumbres se

producen debido a las diferencias entre lo simulado por el modelo meteorologico WRF y los

datos observados de la Estación Deuca, perteneciente al INIA.

Finalmente, la modelación de las emisiones del proyecto de material particulado (MP10 y

MP2,5) resultaron ser de baja magnitud concluyendo que, el funcionamiento del **proyecto**

**no representa un riesgo significativo a la salud ni calidad de vida de la población,**

**según los criterios establecidos en la legislación ambiental vigente** . Considerando

que en ningún caso la concentración proyectada respecto de la concentración basal presentó

un aumento significativo que generara una posible condición de riesgo para las componentes

evaluadas.

DECLARACIÓN DE IMPACTO AMBIENTAL

INFORME MODELACIÓN ATMOSFERICA
“Proyecto Modificación PTAS Hualañé”

Página 63 de 63

**9** **Bibliografía**

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

**Tabla 1.: Valores normados para MP10 y MP2,5 en Chile.****

| Nivel | MP10 (μg/m3N) | MP2,5 (μg/m3) |
| --- | --- | --- |
| **Concentración Anual** | 50 | 20 |
| **Concentración 24 horas** | 130 | 50 |
| **Alerta** | 180-229 | 80-109 |
| **Preemergencia** | 230-329 | 110-169 |
| **Emergencia** | 330 o superior | 170 o superior |

**Tabla 2: Concentración promedio anual de MP10 estación****

| Año | Porcentaje de<br>datos<br>disponibles (%) | Concentración<br>Promedio Anual<br>(μg/m3) | Límite normativo<br>D.S. 12/2011 MMA<br>(μg/m3) | Porcentaje de<br>excedencia de la<br>norma (%) |
| --- | --- | --- | --- | --- |
| 2015 | 99,6% | 58,1 | 50,0 | 190,3% |
| 2016 | - | - | - | - |
| 2017 | 99,8% | 43,9 | 43,9 | 119,10% |
| 2018 | 99,9% | 41,0 | 41,0 | 105,10% |
| 2019 | 99,8% | 45,3 | 45,3 | 116,70% |
| 2020 | 99,8% | 42,6 | 42,6 | 113,00% |
| 2021 | 100,0% | 42,3 | 42,3 | 111,60% |
| 2022 | 99,5% | 40,0 | 40,0 | 100,80% |

**Tabla 3.: Días de alerta, preemergencia y emergencia ambiental en la EMRP****

| Año | MP10 | Col3 | Col4 | MP2,5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Año** | **Días de**<br>**Alerta** | **Días de**<br>**Preemergen**<br>**cia** | **Días de**<br>**Emergencia** | **Días de**<br>**Alerta** | **Días de**<br>**Preemergen**<br>**cia** | **Días de**<br>**Emergencia** |
| 2015 | 0 | 0 | 0 | 8 | 1 | 0 |
| 2017 | 8 | 1 | 0 | 7 | 9 | 0 |
| 2018 | 7 | 9 | 0 | 3 | 2 | 0 |
| 2019 | 3 | 2 | 0 | 2 | 0 | 0 |
| 2020 | 2 | 0 | 0 | 9 | 3 | 0 |
| 2021 | 9 | 3 | 0 | 2 | 1 | 0 |
| 2022 | 2 | 1 | 0 | 8 | 1 | 0 |

**Tabla 4.: Concentración promedio anual MP2,5 estación Curicó****

| Año | Porcentaje de<br>datos<br>disponibles (%) | Concentración<br>Promedio Anual<br>(μg/m3) | Límite normativo<br>D.S. 12/2011 MMA<br>(μg/m3) | Porcentaje de<br>excedencia de la<br>norma (%) |
| --- | --- | --- | --- | --- |
| 2015 | 99,8 % | 25,8 | 20,0 | 28,9 % |
| 2016 | - | - | - | - |
| 2017 | 99,6 % | 23,4 | 23,4 | 17,0 % |
| 2018 | 99,8 % | 24,7 | 24,7 | 23,5 % |
| 2019 | 99,5 % | 22,8 | 22,8 | 14,1 % |
| 2020 | 99,7 % | 26,2 | 26,2 | 30,8 % |
| 2021 | 99,6 % | 22,6 | 22,6 | 13,2 % |

**Tabla 5.: Características del modelo****

| Año de modelación | Col2 | 2022 |
| --- | --- | --- |
| **Periodo de Modelación** | **Periodo de Modelación** | 1 año calendario |
| **Resolución temporal** | **Resolución temporal** | 1 hora |
| **Resolución espacial** | **Resolución espacial** | 1 km |
| **Coordenadas del centroide** | **Latitud** | -34,99° |
| **Coordenadas del centroide** | **Longitud** | -71,59° |
| **DATUM** | **DATUM** | NWS - 84 |
| **Coordenadas del modelo** | **Coordenadas del modelo** | LCC |
| **Dominio de modelación** | **X ** | 95 |
| **Dominio de modelación** | **Y ** | 53 |
| **Dominio de modelación** | **Z ** | 10 |

**Tabla 6.: Descripción de los puntos receptores****

| Recepto<br>r | Coordenada UTM WGS 84 HUSO 19<br>S | Col3 | Distancia al centro del proyecto<br>(m) | Descripció<br>n |
| --- | --- | --- | --- | --- |
| **Recepto**<br>**r ** | **Este (m)** | **Norte (m)** | **Norte (m)** | **Norte (m)** |
| R1 | 243.389,9 | 6.126.261,1 | 70,6 | Casa<br>habitación<br>existente |
| R2 | 243.292,3 | 6.126.350,4 | 122,2 | Casa<br>habitación<br>existente |
| R3 | 243.540,8 | 6.126.111,6 | 245,1 | Casa<br>habitación<br>existente |
| R4 | 243.219,0 | 6.126.431,6 | 230,2 | Casa<br>habitación<br>existente |
| R5 | 243.462,7 | 6.126.397,1 | 219,3 | Casa<br>habitación<br>existente |
| R6 | 243.375,1 | 6.126.507,2 | 283,9 | Casa<br>habitación<br>existente |
| R7 | 243.090,6 | 6.126.511,3 | 321,6 | Casa<br>habitación<br>existente |
| R8 | 243.239,2 | 6.126.560,5 | 344,2 | Casa<br>habitación<br>existente |
| R9 | 243.681,7 | 6.126.248,3 | 355,3 | Casa<br>habitación<br>existente |
| R9 | 2436.98,5 | 6.126.089,1 | 398,9 | Casa<br>habitación<br>existente |
| R10 | 243.796,5 | 6.126.411,2 | 501,1 | Estadio<br>Municipal<br>Hualañé |
| R11 | 243.905,4 | 6.126.203,2 | 580,4 | Liceo<br>Hualañé |

**Tabla 7.: Coordenadas de modelación de las fuentes areales Fase de****

| Actividad para<br>modelar | Unidad del<br>proyecto | Área (m2) | Coordenada UTM, HUSO 19 S,<br>DATUM WGS 84 | Col5 |
| --- | --- | --- | --- | --- |
| **Actividad para**<br>**modelar** | **Unidad del**<br>**proyecto** | **Área (m2) ** | **Este (m)** | **Norte (m)** |
| Preparación<br>Terreno | P1 | 1000 <br> | 243.256,62 | 6.126.242,89 |
| Preparación<br>Terreno | P1 | 1000 <br> | 243.263,34 | 6.126.262,37 |
| Preparación<br>Terreno | P1 | 1000 <br> | 243.304,28 | 6.126.228,15 |
| Preparación<br>Terreno | P1 | 1000 <br> | 243.310,01 | 6.126.247,13 |
| Preparación<br>Terreno | P2 | 1200 <br> | 243.226,01 | 6.126.242,01 |
| Preparación<br>Terreno | P2 | 1200 <br> | 243.250,79 | 6.126.232,52 |
| Preparación<br>Terreno | P2 | 1200 <br> | 243.208,95 | 6.126.200,39 |
| Preparación<br>Terreno | P2 | 1200 <br> | 243.233,48 | 6.126.190,37 |
| Preparación<br>Terreno | P3 | 1600 <br> | 243.233,24 | 6.126.115,61 |
| Preparación<br>Terreno | P3 | 1600 <br> | 243.241,85 | 6.126.140,52 |
| Preparación<br>Terreno | P3 | 1600 <br> | 243.293,59 | 6.126.097,55 |
| Preparación<br>Terreno | P3 | 1600 <br> | 243.300,54 | 6.126.121,46 |

**Tabla 8.: ** Resultados estadísticos obtenidos por la modelación**

| Variable | Coeficiente de<br>correlación lineal (r) | Coeficiente de<br>determinación (r2) | Bias | MAE | RMSE |
| --- | --- | --- | --- | --- | --- |
| Temperatura<br>horaria | 0,85 | 0,73 | -0,42 | 2,86 | 3,60 |
| Rapidez del<br>viento horaria | 0,41 | 0,17 | 2,19 | 2,24 | 2,92 |
