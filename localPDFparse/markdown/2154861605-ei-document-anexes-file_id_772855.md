---
title: Sin título
author: Maryorie Schulz
date: D:20211130192549-03'00'
language: es
type: report
pages: 67
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - MODELACIÓN ATMOSFÉRICA DE EMISIONES
-->

# MODELACIÓN ATMOSFÉRICA DE EMISIONES

**DICIEMBRE 2021**

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

**ÍNDICE**

Página 2 de 67

**1** **INTRODUCCIÓN ..................................................................................................................... 5**

**2** **OBJETIVOS ............................................................................................................................... 7**

**3** **MARCO LEGAL REGULATORIO ......................................................................................... 8**

**3.1** **Estado de la Calidad del Aire en la comuna de Negrete ......................................... 9**

**3.2** **Análisis del Cumplimiento Normativo .................................................................... 9**

**4** **JUSTIFICACIÓN DE LOS MODELOS UTILIZADOS EN EL ESTUDIO ...................... 12**

**4.1** **Uso del modelo CALPUFF ...................................................................................... 13**

**4.2** **Uso del modelo WRF ............................................................................................. 15**

**5** **METODOLOGÍA ................................................................................................................... 16**

**5.1** **Modelación de partículas ...................................................................................... 16**
5.1.1 Modelación meteorológica ............................................................................................................. 16
5.1.2 Modelación de dispersión de contaminantes ................................................................................. 16
5.1.3 Criterios para la modelación de partículas ..................................................................................... 18

**6** **RESULTADOS ....................................................................................................................... 25**

**6.1** **Modelamiento meteorológico ............................................................................... 25**
6.1.1 Caracterización de la velocidad y dirección de los vientos Anual y Estacional ............................... 25
6.1.2 Caracterización de la Temperatura del Aire ................................................................................... 36
6.1.3 Altura de Capa de Mezcla ............................................................................................................... 38

**6.2** **Concentraciones Modeladas ................................................................................. 40**

6.2.1 Dispersión e Isoconcentración Material Particulado Respirable, MP10 ......................................... 40
6.2.2 Dispersión e Isoconcentración Material Particulado Fino Respirable, MP2,5 ................................ 47

6.2.3 Modelación discreta de las emisiones contaminantes ................................................................... 53

**6.3** **Aporte a la estación de Monitoreo de Representatividad Poblacional (EMRP) .... 54**

**7** **ANÁLISIS DE INCERTIDUMBRE ..................................................................................... 56**

**7.1** **Temperatura ......................................................................................................... 58**

**7.2** **Velocidad del viento ............................................................................................. 59**

**7.3** **Dirección del viento .............................................................................................. 61**

**7.4** **Test de Bondad de Ajuste sobre el Modelo Meteorológico ................................... 63**

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

Página 3 de 67

**8** **CONCLUSIÓN ........................................................................................................................ 64**

**9** **BIBLIOGRAFÍA .................................................................................................................... 66**

**ÍNDICE DE FIGURAS**

Figura 1 Ubicación del proyecto ................................................................................... 5

Figura 2. Concentración Promedio 24 horas de MP10 estación 21 de Mayo...................... 9

Figura 3. Concentración Promedio Trianual de MP10, estación 21 de Mayo .................... 10

Figura 4. Concentración Promedio 24 horas de MP2,5 estación 21 de Mayo .................... 11

Figura 5. Concentración Promedio Trianual de MP2,5 estación 21 de Mayo .................... 12

Figura 6. Receptores discretos .................................................................................... 18

Figura 7. Polígonos de modelación representativos de cada unidad modelada ................ 24

Figura 8. Rosa de los vientos anual, WRF 2019 ............................................................ 25

Figura 9. Frecuencia de los vientos, año 2019 .............................................................. 26

Figura 10. Rosa de los vientos verano, WRF 2019 ........................................................ 27

Figura 11. Frecuencia de los vientos en verano, año 2019 ............................................ 28

Figura 12. Rosa de los vientos otoño, WRF 2019 .......................................................... 29

Figura 13. Frecuencia de los vientos en otoño, año 2019 .............................................. 31

Figura 14. Rosa de los vientos invierno, WRF 2019 ...................................................... 32

Figura 15. Frecuencia de los vientos en invierno, año 2019 ........................................... 33

Figura 16. Rosa de los vientos en primavera, WRF 2019 ............................................... 34

Figura 17. Frecuencia de los vientos en primavera, año 2019 ........................................ 35

Figura 18. Perfil diario de velocidad del viento, WRF año 2019 ...................................... 36

Figura 19. Temperatura Mensual WRF, año 2019 ......................................................... 37

Figura 20. Perfil diario de Temperatura, WRF año 2019 ................................................ 38

Figura 21. Evolución diaria de la altura de capa de mezcla, WRF año 2019 ..................... 39

Figura 22. Dispersión de la pluma de MP10 como concentración promedio anual ............ 42

Figura 23. Isoconcentración MP10 como concentración promedio anual ......................... 43

Figura 24. Dispersión de la pluma de MP10 como concentración promedio 24 horas ....... 45

Figura 25. Isoconcentración MP10 como concentración promedio 24 horas .................... 46

Figura 26. Dispersión de la pluma de MP2,5 como concentración promedio anual ........... 48

Figura 27. Isoconcentración MP2,5 como concentración promedio anual. ....................... 49

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

Página 4 de 67

Figura 28. Dispersión de la pluma de MP2,5 como concentración promedio 24 horas ...... 51

Figura 29. Isoconcentración MP2,5 como concentración promedio 24 horas ................... 52

Figura 30. Correlación entre temperaturas observadas y modeladas .............................. 58

Figura 31. Frecuencia de temperaturas observadas y modeladas ................................... 59

Figura 32. Correlación entre velocidad del viento observada y modeladas ...................... 60

Figura 33. Frecuencia de velocidad del viento observadas y modeladas ......................... 61

Figura 34. Correlación entre dirección del viento observado y simulado ......................... 62

Figura 35. Frecuencia de velocidad del viento observadas y modeladas ......................... 63

**ÍNDICE DE TABLAS**

Tabla 1. Valores normados para MP10 y MP2,5 en Chile. ............................................... 8

Tabla 2. Concentración promedio anual de MP10 estación 21 de Mayo .......................... 10

Tabla 3. Concentración promedio anual de MP2,5 estación 21 de Mayo ......................... 11

Tabla 4. Características del modelo ............................................................................. 16

Tabla 5. Descripción de los puntos receptores ............................................................. 17

Tabla 6. Coordenadas de modelación de las fuentes areales ......................................... 19

Tabla 7. Frecuencia de los vientos verano, WRF. .......................................................... 27

Tabla 8. Frecuencia de los vientos otoño, WRF. ........................................................... 30

Tabla 9. Frecuencia de los vientos invierno, WRF. ........................................................ 32

Tabla 10. Frecuencia de los vientos en primavera, WRF. ............................................... 34

Tabla 11. Concentración modelada en puntos receptores con respecto a MP10 y MP2,5 .. 54

Tabla 12. Aumento de la concentración basal en la EMRP 21 de Mayo, año 2018............ 54

Tabla 13. Estadísticos de variables meteorológicas modeladas ...................................... 57

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

Página 5 de 67

**1** **INTRODUCCIÓN**

El proyecto **“Extracción de Áridos Pozo Gallegos”** (en adelante proyecto), se ubicará en

la comuna de Negrete, provincia de Biobío, Región del Biobío (ver Figura 1). El proyecto

consiste en la extracción, procesamiento de material pétreo y producción de mezcla asfáltica

con el objetivo de abastecer las obras de mejoramiento de rutas viales de la Región del

Biobío.

**Figura 1 Ubicación del proyecto**

Con este estudio se busca predecir la concentración de material particulado grueso y fino

(MP10 y MP2,5), además de evaluar su contribución en puntos receptores de interés y en

las estaciones de calidad del aire más cercanas, esto último respecto a su situación basal.

La modelación de las emisiones se realizó en base a los resultados obtenido de la estimación

de emisiones atmosférica se en el Anexo 5.1 de la DIA, cuyos resultados indican que la

máxima emisión del proyecto se alcanza en el año 2, donde se solapan las emisiones de la

fase de operación y abandono del proyecto.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

Página 6 de 67

La evaluación de la dispersión y concentración de las emisiones de material particulado se

realizó mediante el programa CALPUFF, el cual es un modelo de dispersión usado

ampliamente para simulaciones de concentraciones ambientales de las emisiones de

operaciones normales, con el objeto de establecer, desarrollar y analizar escenarios de

emisión y regulación. A su vez, CALPUFF es recomendado por el Ministerio de Medio

Ambiente en la “Guía para el Uso de Modelos de Calidad del Aire en el SEIA”, publicada el

año 2012. Los resultados y análisis de esta evaluación se presentan en el siguiente informe.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

Página 7 de 67

**2** **Objetivos**

El presente informe, tiene como objetivo general cuantificar y evaluar el efecto en la

atmósfera debido a las emisiones de contaminantes generadas por el proyecto **“Extracción**

**de Áridos Pozo Gallegos”** y cuantificar sus concentraciones.

Para lo anterior se plantean los siguientes objetivos específicos:

 Evaluar en términos de concentración, el alcance de las emisiones de MP10 y MP2,5

en la atmósfera.

 Evaluar la concentración de MP10 y MP2,5 en receptores que actualmente se

encuentren cercanos al proyecto, así como en las estaciones de calidad del aire

emplazadas cercanos a éste.

 Determinar la afectación a la salud de las personas debido al aporte a la

concentración basal de MP10 y MP2,5 en la ciudad, dado el desarrollo del proyecto.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

**3** **Marco Legal Regulatorio**

Página 8 de 67

Actualmente, los contaminantes MP10 y MP2,5 están regulados bajo normas de calidad

primaria, cuyo objetivo es proteger la salud de las personas de los efectos agudos y crónicos

de la exposición de estos contaminantes con un riesgo aceptable. Para esto, se fijan límites

de concentración permitidos, condiciones de superación de la norma y los niveles que dan

paso a situaciones de emergencia ambiental.

El material particulado respirable MP10 es regulado por el D.S. 59/1998 MINSEGEPRES y el

material particulado fino respirable MP2,5 es regulado por el D.S. 12/2011 MMA.

En Tabla 1 se aprecian los valores del límite anual y diario para los contaminante MP10 y

MP2,5, además de los rangos que dan origen a situaciones de alerta, preemergencia y

emergencia ambiental.

**Tabla 1. Valores normados para MP10 y MP2,5 en Chile.**

|Nivel|MP10 (μg/m3)|MP2,5 (μg/m3)|
|---|---|---|
|**Promedio Anual**|50|20|
|**Promedio 24 horas**|150|50|
|**Alerta**|195-239|80-109|
|**Preemergencia**|240-329|110-169|
|**Emergencia**|330 o mayor|170 o mayor|

Fuente: En base a D.S. 59/1998 MINSEGEPRES y D.S. 12/2011 MMA

No obstante, la superación del límite normativo de MP10 no es motivo de condiciones de

superación de la noma, sino que se considera que la norma es incumplida bajo las siguientes

condiciones:

 - Cuando el promedio de la concentración anual de tres años consecutivos iguale o

supere los 50 μg/m3.

 - Si el percentil 98 (P98) de las concentraciones de 24 horas durante un año sea igual

o superior a 150 μg/m3

 - Si durante un año se registrasen siete o más días cuya concentración sea mayor a

150 μg/m3

En el mismo contexto, las condiciones de superación de la norma de MP2,5 son las que se

describen a continuación:

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

Página 9 de 67

 - Cuando el promedio de la concentración anual de tres años consecutivos iguale o

supere los 20 μg/m3.

 - Si el percentil 98 (P98) de las concentraciones de 24 horas durante un año sea igual

o superior a 50 μg/m3

**3.1** **Estado de la Calidad del Aire en la comuna de Negrete**

La comuna de Negrete no cuenta con Estaciones de Calidad del Aire de representatividad

población, por lo cual, se escogió la estación más cercana ubicada en Los Ángeles, llamada

Estación 21 de Mayo [1] . Esta estación cuenta con datos a partir del 2012, los resultados se

presentan a continuación.

**3.2** **Análisis del Cumplimiento Normativo**

Como se puede ver en la siguiente figura, la concentración promedio 24 horas supera el

límite establecido por el D.S. 59/1998 MINSEGEPRES que establece la norma de calidad

primaria para material particulado respirable MP10 en todo el período analizado (2013

2019).

**Figura 2. Concentración Promedio 24 horas de MP10 estación 21 de Mayo**

Fuente: Elaboración propia en base a los datos dispuestos en el Sistema Nacional de Calidad del

Aire (SINCA).

1 [Fuente: https://sinca.mma.gob.cl/index.php/estacion/index/key/875](https://sinca.mma.gob.cl/index.php/estacion/index/key/875)

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

Página 10 de 67

Respecto a la concentración promedio anual de MP10, se puede observar que esta excede

la norma para todo el periodo analizado salvo en el año 2017 y 2019.

**Tabla 2. Concentración promedio anual de MP10 estación 21 de Mayo**

|Año|Porcentaje<br>de datos<br>disponibles<br>(%)|Concentración<br>Promedio Anual<br>(μg/m3)|Límite normativo<br>D.S. 59/1998<br>MINSEGEPRES<br>(μg/m3)|Porcentaje de<br>excedencia de la<br>norma (%)|
|---|---|---|---|---|
|2013|96|53,96|50|7,92|
|2014|98|55,18|55,18|10,36|
|2015|100|56,05|56,05|12,11|
|2016|99|56,84|56,84|13,67|
|2017|100|45,73|45,73|No excede|
|2018|99|54,54|54,54|9,08|
|2019|97|32,72|32,72|No excede|

Fuente: Elaboración propia en base a los datos dispuestos en el Sistema Nacional de Calidad del

Aire (SINCA).

Con respecto a la concentración promedio trianual, esta fue posible analizar para 4

temporadas, de la cual se observa superación normativa en todo el período analizado.

**Figura 3. Concentración Promedio Trianual de MP10, estación 21 de Mayo**

El D.S. 12/2011 MMA establece la norma primaria de calidad ambiental para material

particulado fino respirable MP2,5, regulando la concentración promedio anual y diaria.

Referente a las concentraciones para este contaminante en estación 21 de Mayo, se observa

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

Página 11 de 67

que para los seis años analizados, las concentraciones promedio 24 horas superan el límite

normativo, siendo el año 2018 aquel donde se evidencian los mayores registros.

**Figura 4. Concentración Promedio 24 horas de MP2,5 estación 21 de Mayo**

Fuente: Elaboración propia en base a los datos dispuestos en el Sistema Nacional de Calidad del

Aire (SINCA).

La concentración promedio anual de MP2,5 que establece el D.S. 12/2011 MMA para los

años analizados es superada en todo el período analizado siendo el 2018 aquel que cuenta

con un mayor porcentaje de excedencia, con un 73,11%.

**Tabla 3. Concentración promedio anual de MP2,5 estación 21 de Mayo**

|Año|Porcentaje de<br>datos<br>disponibles (%)|Concentración<br>Promedio Anual<br>(μg/m3)|Límite normativo<br>D.S. 12/2011 MMA<br>(μg/m3)|Porcentaje de<br>excedencia de la<br>norma (%)|
|---|---|---|---|---|
|2013|96|28,88|20,0|44,40|
|2014|97|27,48|27,48|37,42|
|2015|98|29,05|29,05|45,25|
|2016|100|32,49|32,49|62,46|
|2017|99|27,74|27,74|38,69|
|2018|99|34,62|34,62|73,11|
|2019|98|15,56|15,56|No excede|

Fuente: Elaboración propia en base a los datos dispuestos en el Sistema Nacional de Calidad del

Aire (SINCA).

Con respecto a las concentraciones de MP2,5 como promedio trianual, esta fue caracterizada

para cuatro períodos, y tal como se evidencia en la siguiente figura, existe superación

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

Página 12 de 67

normativa en todos estos.

**Figura 5. Concentración Promedio Trianual de MP2,5 estación 21 de Mayo**

Los antecedentes demuestran que actualmente, en la comuna de Los Ángeles existen

registros suficientes para afirmar que no hay cumplimiento de las normas de calidad del aire

para los contaminantes criterios MP10 y MP2,5 al caracterizar la estación 21 de Mayo, ya

que en el periodo estudiado (2013-2018) estas son ampliamente superadas.

**4** **Justificación de los modelos utilizados en el estudio**

El Servicio de Evaluación Ambiental en la “Guía para el Uso de Modelos de Calidad del Aire

en el SEIA” (2012) hace una serie de recomendaciones para la modelación de contaminantes

primarios [2] y secundarios en el aire. En la actualidad, esta guía es el único documento

existente como parámetro para la modelación de calidad del aire y tiene como objetivo

uniformar los criterios, exigencias técnicas y antecedentes para la evaluación de los impactos

asociados a este componente de proyectos que ingresen al Servicio de Evaluación

Ambiental. Dentro de las recomendaciones de la guía está el uso del modelo de dispersión

CALPUFF y sugiere la utilizar el modelo meteorológico WRF, los cuales fueron utilizados en

la modelación de las partículas del proyecto.

2 Los contaminantes primarios son los producidos directamente por la actividad humana o la
naturaleza a la atmósfera, dentro de los cuales caben las emisiones odorantes.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

Página 13 de 67

A continuación, se presenta la justificación de los modelos utilizados en el proyecto para

ejecución de la modelación de dispersión y concentración de emisiones partículas en el aire.

**4.1** **Uso del modelo CALPUFF**

La modelación de dispersión atmosférica de particulas provenientes del proyecto se realizó

con un modelo tipo “Puff”, específicamente el modelo CALPUFF. Tal como lo define la guía,

los modelos tipo “puff” son una combinación entre los modelos Gaussianos y los modelos

Lagrangeanos, en el sentido de que esencialmente calculan la dispersión de contaminantes

provenientes de una emisión instantánea, llamada “puff”, a lo largo de una trayectoria. Su

aproximación matemática consiste en estimar la dispersión en forma Gaussiana en cada

punto de una trayectoria; es decir, los modelos tipo “puff” sólo requieren una trayectoria

por “puff”, lo que hace su cálculo mucho más rápido. En el caso de emisiones continuas, se

simulan las trayectorias y la dispersión Gaussiana de muchos “puffs”, como es en el caso de

las emisiones de particulas generadas por el proyecto. Al respecto, el modelo tipo “puff”

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

 CALPUFF: Es un modelo de transporte y dispersión de partículas y gases emitidos

desde fuentes modeladas, simulando procesos de dispersión y transformación.

CALPUFF utiliza los datos generados por CALMET. Los archivos de salida de CALPUFF

contienen las concentraciones horarias o deposición por hora de flujos evaluados en

receptores seleccionados.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

Página 14 de 67

 CALPOST: Es usado para procesar aquellos archivos generados por CALMET y

CALPUFF, produciendo tabulaciones que resumen los resultados de la simulación.

Ecuación del modelo CALPUFF

La ecuación básica que utiliza el modelo para realizar la modelación es la siguiente:

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

**σ** **y** **,** es desviación estándar (m) de la distribución de Gauss en el viento de costado

**σ** **z**, es desviación estándar (m) de la distribución de Gauss en la dirección vertical.

**d** **a** **,** es distancia (m) del centro de la nube al receptor en la dirección del viento a lo largo.

**d** **c**, es distancia (m) del centro de la nube al receptor en la dirección de viento cruzado.

**g**, es el término vertical (m [-1] ) de la ecuación Gaussiana.

**H**, es la altura afectiva (m) desde el nivel del suelo del hojaldre.

**h**, es la altura de la capa de mezcla.

El terreno en el cual se realizará la modelación de las emisiones partículas se considera

heterogéneo, debido a las distintas unidades geomorfológicas. Por esta razón y en

consistencia con las recomendaciones del SEA para la modelación de partículas en sus guías,

se consideró utilizar el modelo CALPUFF para simular la dispersión y concentración de las

emisiones partículas generadas por la futura operación del proyecto.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

**4.2** **Uso del modelo WRF**

Página 15 de 67

El modelo Weather Research and Forecasting (WRF), es un modelo numérico de cuatro

dimensiones, recomendado para la generación de datos meteorológicos y es uno de los

modelos de pronóstico meteorológicos más avanzados.

Debido a la falta de una red robusta de estaciones meteorológicas, la “Guía para el Uso de

Modelos de Calidad del Aire en el SEIA” recomienda el uso de WRF por sobre el uso del

CALMET. Además, el mismo documento, sugiere el uso del WRF para la modelación de

dispersión de contaminantes con CALPUFF.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

Página 16 de 67

**5** **Metodología**

**5.1** **Modelación de partículas**

La modelación de partículas depende en gran parte de las tasas de emisión. Estos son

acoplados a un modelo meteorológico, el que en sí mismo simula las condiciones

meteorológicas para la zona de estudio con una resolución temporal de 1 hora; con estos

factores como variable de entrada al modelo, es simulada la dispersión de las partículas en

un modelo, que determinará la trayectoria de las partículas dentro del área de estudio.

**5.1.1** **Modelación meteorológica**

Para la modelación meteorológica, se utilizó un modelo WRF, construido con datos del año

2019 y resolución de 1 km, de extensión 59 km x 59 km. El modelo WRF es capaz de simular

el comportamiento meteorológico, a través de datos meteorológicos para el año de estudio,

el que posteriormente es interpolado dentro del área de estudio del modelo de acuerdo con

la topografía del lugar. En la siguiente tabla se resumen las características del modelo.

**Tabla 4. Características del modelo**

|Año de modelación|Col2|2019|
|---|---|---|
|**Periodo de Modelación**|**Periodo de Modelación**|1 año calendario|
|**Resolución temporal**|**Resolución temporal**|1 hora|
|**Resolución espacial**|**Resolución espacial**|1 km|
|**Coordenadas del**<br>**centroide**|**Latitud**|-37,580°|
|**Coordenadas del**<br>**centroide**|**Longitud**|-72,558°|
|**DATUM**|**DATUM**|NWS - 84|
|**Coordenadas del modelo**|**Coordenadas del modelo**|LCC|
|**Dominio de modelación**|**X **|59|
|**Dominio de modelación**|**Y **|59|
|**Dominio de modelación**|**Z **|10|

**5.1.2** **Modelación de dispersión de contaminantes**

El modelo CALPUFF permite la simulación de la dispersión de contaminantes bajo dos

modalidades:

 **Modelación de la grilla de modelación** . La grilla de modelación viene seteada

del modelo meteorológico, acotando la simulación en la zona circundante más

próxima al proyecto, incluyendo las zonas pobladas importantes de evaluar. Dicha

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

grilla de modelación tiene una resolución espacial de 1 km.

Página 17 de 67

Este es el método más usual para la interpolación de las concentraciones de los

puntos de grilla (1 km), interpolando entre cada punto la concentración, hasta

obtener la pluma de dispersión. Por defecto la modelación de los puntos de grilla

entrega el valor de la concentración como el promedio en la primera capa de

modelación, la que ocurre entre los 0 y 20 m sobre el nivel del suelo.

En virtud de la resolución espacial del modelo y de la altura de la primera capa de

modelación, y al tratarse de áreas de emisión que se generan a altura del suelo o a

baja altura [3], muchas veces la obtención de la pluma de dispersión se genera con

valores sub dimensionados, por lo tanto, en ocasiones es necesario realizar una sub

grilla de modelación a través de la modelación de puntos discretos, aumentando la

densidad de puntos de modelación y mejorando la evaluación de la concentración

simulada dentro del espacio circundante. De este modo, se generó una subgrilla de

27 km x 20 km.

 **Modelación de puntos discretos.** Se consideraron 10 puntos discretos cercanos,

cuyas coordenadas se presentan a continuación y se presenta espacial mente en la

figura adjunta.

**Tabla 5. Descripción de los puntos receptores**

|Receptor|Coordenada UTM WGS 84 HUSO 19 S|Col3|Descripción|Distancia al centro<br>del proyecto (m)|
|---|---|---|---|---|
|**Receptor**|**Este (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|
|1|716779|5837235|Casa habitación|1.359|
|2|716067|5837690|Casa habitación|564|
|3|716554|5837544|Casa habitación|1.058|
|4|715618|5837322|Casa habitación|385|
|5|715158|5837277|Casa habitación|541|
|6|714902|5837586|Casa habitación|612|
|7|714069|5838113|Casa habitación|1.497|
|8|716268|5838656|Casa habitación|1.244|
|9|715012|5837652|Casa habitación|491|
|10|714528|5837782|Casa habitación|973|
|11|714522|5837001|Casa habitación|1.889|
|12|715207|5837589|Casa habitación|350|
|13|715471|5837484|Casa habitación|279|

3 Como es el caso del tránsito y de las obras asociadas al movimiento de tierra.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

Página 18 de 67

|Receptor|Coordenada UTM WGS 84 HUSO 19 S|Col3|Descripción|Distancia al centro<br>del proyecto (m)|
|---|---|---|---|---|
|**Receptor**|**Este (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|
|14|715870|5837638|Casa Habitación|383|

Nota: la distancia de los receptores se midió al centro del proyecto, en la coordenada en UTM WGS

84 HUSO 18 S son x: 715494,57 m e y: 5837756,52 m.

**Figura 6. Receptores discretos**

**5.1.3** **Criterios para la modelación de partículas**

Como escenario de modelación se consideró el año de máxima emisión, es decir el segundo

año de proyecto, en donde ocurre la operación del proyecto y el abandono paulatino de las

zonas extraídas en los meses previos. Los detalles de la estimación de emisiones se

presentan en el Anexo 5.1. Estimación de Emisiones Atmosféricas.

Adicionalmente, se modelaron las emisiones de gases precursores de MP10 y MP2,5 en el

aire a través del módulo MESOPUFF II.

De acuerdo con la metodología aplicable, se realizaron polígonos representativos de cada

unidad para la simulación de las áreas de emisiones de partículas las que, fueron modeladas

como fuentes de emisión discontinuas, es decir, dentro del ciclo diurno, se consideró la

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

Página 19 de 67

generación de emisiones durante 10 horas (8:00 a 19:00 hrs), ya que ese es el horario

laboral establecido para el proyecto, con una hora de almuerzo (13:00-14:00 hrs). Las

coordenadas y su representación se encuentran en la siguiente tabla, así como también, en

la Figura 7 se presenta la ubicación espacial de éstos.

**Tabla 6. Coordenadas de modelación de las fuentes areales**

|Unidad del proyecto|Coordenada UTM, HUSO 18S, DATUM WGS 84|Col3|
|---|---|---|
|**Unidad del proyecto**|**Este (m)**|**Norte (m)**|
|Escarpe y Excavación|715436|5838103|
|Escarpe y Excavación|715856|5837903|
|Escarpe y Excavación|715377|5837921|
|Escarpe y Excavación|715795|5837721|
|Planta Chancadora|715326|5837706|
|Planta Chancadora|715360|5837677|
|Planta Chancadora|715324|5837702|
|Planta Chancadora|715358|5837673|
|Planta Asfalto|715281|5837564|
|Planta Asfalto|715328|5837545|
|Planta Asfalto|715280|5837559|
|Planta Asfalto|715327|5837540|
|Grupo Electrógeno 1|715298|5837556|
|Grupo Electrógeno 1|715301|5837554|
|Grupo Electrógeno 1|715297|5837553|
|Grupo Electrógeno 1|715300|5837552|
|Grupo Electrógeno 2|715257|5837520|
|Grupo Electrógeno 2|715258|5837519|
|Grupo Electrógeno 2|715256|5837518|
|Grupo Electrógeno 2|715258|5837517|
|Grupo Electrógeno 3|715328|5837703|
|Grupo Electrógeno 3|715329|5837702|
|Grupo Electrógeno 3|715326|5837701|
|Grupo Electrógeno 3|715328|5837700|
|Grupo Electrógeno 4|715356|5837678|
|Grupo Electrógeno 4|715358|5837677|
|Grupo Electrógeno 4|715355|5837676|
|Grupo Electrógeno 4|715357|5837675|
|Acopio Planta Asfalto|715286|5837694|
|Acopio Planta Asfalto|715322|5837659|
|Acopio Planta Asfalto|715271|5837673|

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

Página 20 de 67

|Unidad del proyecto|Coordenada UTM, HUSO 18S, DATUM WGS 84|Col3|
|---|---|---|
|**Unidad del proyecto**|**Este (m)**|**Norte (m)**|
|**Unidad del proyecto**|715307|5837638|
|Acopio Planta Chancadora|715396|5837610|
|Acopio Planta Chancadora|715441|5837608|
|Acopio Planta Chancadora|715395|5837581|
|Acopio Planta Chancadora|715441|5837580|
|Ruta interna no pavimentada 1|715842|5837862|
|Ruta interna no pavimentada 1|715841|5837859|
|Ruta interna no pavimentada 1|715954|5837833|
|Ruta interna no pavimentada 1|715954|5837830|
|Ruta interna no pavimentada 2|715448|5837887|
|Ruta interna no pavimentada 2|715451|5837885|
|Ruta interna no pavimentada 2|715499|5837785|
|Ruta interna no pavimentada 2|715503|5837785|
|Ruta interna no pavimentada 3|715499|5837785|
|Ruta interna no pavimentada 3|715503|5837785|
|Ruta interna no pavimentada 3|715490|5837762|
|Ruta interna no pavimentada 3|715494|5837761|
|Ruta interna no pavimentada 4|715490|5837762|
|Ruta interna no pavimentada 4|715494|5837761|
|Ruta interna no pavimentada 4|715508|5837722|
|Ruta interna no pavimentada 4|715512|5837722|
|Ruta interna no pavimentada 5|715508|5837722|
|Ruta interna no pavimentada 5|715512|5837722|
|Ruta interna no pavimentada 5|715512|5837639|
|Ruta interna no pavimentada 5|715515|5837639|
|Ruta interna no pavimentada 6|715512|5837639|
|Ruta interna no pavimentada 6|715515|5837639|
|Ruta interna no pavimentada 6|715497|5837582|
|Ruta interna no pavimentada 6|715500|5837581|
|Ruta interna no pavimentada 7|715360|5837677|
|Ruta interna no pavimentada 7|715358|5837674|
|Ruta interna no pavimentada 7|715498|5837586|
|Ruta interna no pavimentada 7|715497|5837582|
|Ruta interna no pavimentada 8|715443|5837601|
|Ruta interna no pavimentada 8|715441|5837598|
|Ruta interna no pavimentada 8|715454|5837595|
|Ruta interna no pavimentada 8|715453|5837592|

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

Página 21 de 67

|Unidad del proyecto|Coordenada UTM, HUSO 18S, DATUM WGS 84|Col3|
|---|---|---|
|**Unidad del proyecto**|**Este (m)**|**Norte (m)**|
|Ruta interna no pavimentada 9|715456|5837609|
|Ruta interna no pavimentada 9|715459|5837608|
|Ruta interna no pavimentada 9|715451|5837597|
|Ruta interna no pavimentada 9|715454|5837595|
|Ruta interna no pavimentada 10|715291|5837722|
|Ruta interna no pavimentada 10|715289|5837719|
|Ruta interna no pavimentada 10|715326|5837706|
|Ruta interna no pavimentada 10|715324|5837703|
|Ruta interna no pavimentada 11|715289|5837719|
|Ruta interna no pavimentada 11|715292|5837717|
|Ruta interna no pavimentada 11|715258|5837692|
|Ruta interna no pavimentada 11|715262|5837691|
|Ruta interna no pavimentada 12|715258|5837692|
|Ruta interna no pavimentada 12|715262|5837691|
|Ruta interna no pavimentada 12|715257|5837573|
|Ruta interna no pavimentada 12|715260|5837575|
|Ruta interna no pavimentada 13|715260|5837575|
|Ruta interna no pavimentada 13|715257|5837573|
|Ruta interna no pavimentada 13|715281|5837564|
|Ruta interna no pavimentada 13|715280|5837561|
|Ruta interna no pavimentada 14|715257|5837573|
|Ruta interna no pavimentada 14|715260|5837572|
|Ruta interna no pavimentada 14|715235|5837500|
|Ruta interna no pavimentada 14|715238|5837499|
|Ruta interna no pavimentada 15|715261|5837585|
|Ruta interna no pavimentada 15|715261|5837581|
|Ruta interna no pavimentada 15|715403|5837528|
|Ruta interna no pavimentada 15|715402|5837524|
|Ruta interna no pavimentada 16|715399|5837526|
|Ruta interna no pavimentada 16|715402|5837524|
|Ruta interna no pavimentada 16|715395|5837513|
|Ruta interna no pavimentada 16|715398|5837511|
|Ruta interna no pavimentada 17|715399|5837515|
|Ruta interna no pavimentada 17|715418|5837509|
|Ruta interna no pavimentada 17|715398|5837511|
|Ruta interna no pavimentada 17|715417|5837506|
|Ruta interna no pavimentada 18|715421|5837534|

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

Página 22 de 67

|Unidad del proyecto|Coordenada UTM, HUSO 18S, DATUM WGS 84|Col3|
|---|---|---|
|**Unidad del proyecto**|**Este (m)**|**Norte (m)**|
|**Unidad del proyecto**|715425|5837533|
|**Unidad del proyecto**|715414|5837510|
|**Unidad del proyecto**|715418|5837509|
|Ruta interna no pavimentada 18|715357|5837478|
|Ruta interna no pavimentada 18|715359|5837475|
|Ruta interna no pavimentada 18|715341|5837462|
|Ruta interna no pavimentada 18|715344|5837461|
|Ruta interna no pavimentada 20|715382|5837485|
|Ruta interna no pavimentada 20|715386|5837483|
|Ruta interna no pavimentada 20|715357|5837478|
|Ruta interna no pavimentada 20|715359|5837475|
|Ruta interna no pavimentada 21|715395|5837513|
|Ruta interna no pavimentada 21|715398|5837511|
|Ruta interna no pavimentada 21|715382|5837485|
|Ruta interna no pavimentada 21|715386|5837483|
|Ruta interna no pavimentada 22|715421|5837567|
|Ruta interna no pavimentada 22|715423|5837565|
|Ruta interna no pavimentada 22|715400|5837529|
|Ruta interna no pavimentada 22|715403|5837528|
|Ruta interna no pavimentada 23|715443|5837579|
|Ruta interna no pavimentada 23|715446|5837577|
|Ruta interna no pavimentada 23|715421|5837567|
|Ruta interna no pavimentada 23|715423|5837565|
|Ruta interna no pavimentada 24|715450|5837593|
|Ruta interna no pavimentada 24|715453|5837592|
|Ruta interna no pavimentada 24|715443|5837579|
|Ruta interna no pavimentada 24|715446|5837577|
|Ruta interna no pavimentada 25|715242|5837512|
|Ruta interna no pavimentada 25|715241|5837509|
|Ruta interna no pavimentada 25|715338|5837477|
|Ruta interna no pavimentada 25|715336|5837474|
|Ruta interna no pavimentada 26|715354|5837535|
|Ruta interna no pavimentada 26|715357|5837533|
|Ruta interna no pavimentada 26|715334|5837478|
|Ruta interna no pavimentada 26|715338|5837477|
|Ruta interna no pavimentada 27|715328|5837545|
|Ruta interna no pavimentada 27|715327|5837541|

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

Página 23 de 67

|Unidad del proyecto|Coordenada UTM, HUSO 18S, DATUM WGS 84|Col3|
|---|---|---|
|**Unidad del proyecto**|**Este (m)**|**Norte (m)**|
|**Unidad del proyecto**|715354|5837535|
|**Unidad del proyecto**|715353|5837531|
|Ruta interna no pavimentada 28|715338|5837477|
|Ruta interna no pavimentada 28|715350|5837471|
|Ruta interna no pavimentada 28|715336|5837474|
|Ruta interna no pavimentada 28|715347|5837469|

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

**Figura 7. Polígonos de modelación representativos de cada unidad modelada**

Página 24 de 67

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

Página 25 de 67

## 6 Resultados

**6.1** **Modelamiento meteorológico**

**6.1.1** **Caracterización de la velocidad y dirección de los vientos Anual y**

**Estacional**

En la Figura 8 se presenta la rosa de vientos anual, construida en base a los datos generados

con el modelo WRF con datos del año 2019 para la comuna de Negrete y sus alrededores.

**Figura 8. Rosa de los vientos anual, WRF 2019**

De la figura anterior, se observa que el origen de los vientos se produce mayoritariamente

desde la componente Sur suroeste (SSW), cuyo vector resultante está situado

específicamente en el grado 202, por lo cual se espera que la dispersión de contaminantes

en el año ocurra principalmente hacia la componente Nor Noreste (NNE), específicamente

en dirección al grado 22.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

Página 26 de 67

“Extracción de Áridos Pozo Gallegos”

A la vez, se observa que el modelo simula en mayor frecuencia vientos situados con origen

en el Sur suroeste (SSW), los cuales representan el 50% de los vientos totales, el resto de

las componentes se presentan en menor magnitud, siendo cercanas al 10% de los vientos

totales en las direcciones nor noreste (NNE), norte (N) y sur (S). Los vientos anuales se

caracterizan por presentar mayor frecuencia en el rango de velocidades 3,60 - 8,8 m/s.

**Figura 9. Frecuencia de los vientos, año 2019**

Con base a los resultados obtenidos, la zona de estudio se caracteriza por vientos que

predominan en la componente Sur suroeste. En cuanto a las velocidades de los vientos

anuales, el rango con mayor frecuencia corresponde a 3,60 - 5,70 m/s con un 34% de los

vientos totales, seguidos por el rango 5,70 - 8,80 m/s con un 32%. Respecto a los vientos

calmos estos representan el 1,9% de los vientos totales anuales.

**6.1.1.1** **Dirección y velocidad de vientos predominantes en verano**

En la Figura 10, se presenta la rosa de los vientos para los meses de verano donde se

observa que los vientos, al igual a lo simulado como escenario anual, son mayoritariamente

frecuentes en la componente Sur Suroeste (SSW), representando el 71% de los vientos

totales de la estación. El resto de las componentes tienen una incidencia mucho menor, por

lo tanto, se espera que en verano los vientos desplacen las masas de aire hacia el Nor

noreste (NNE) específicamente al grado 22 y que por consiguiente la dispersión de

contaminantes tenga lugar hacia esa componente en un 81%.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

**Figura 10. Rosa de los vientos verano, WRF 2019**

Página 27 de 67

En la Tabla 7, se presenta la frecuencia de vientos por cada componente de origen, de

donde se observa la frecuencia de los vientos simulados por el modelo WRF en la época

estival para la ciudad de Negrete y sus alrededores.

**Tabla 7. Frecuencia de los vientos verano, WRF.**

|Componente|Col2|Total|
|---|---|---|
|Norte|N|57|
|Nord noreste|NNE|40|
|Noreste|NE|19|
|Este noreste|ENE|4|
|Este|E|14|

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

Página 28 de 67

“Extracción de Áridos Pozo Gallegos”

|Componente|Col2|Total|
|---|---|---|
|Este Sureste|ESE|13|
|Sureste|SE|19|
|Sur sureste|SSE|22|
|Sur|S|196|
|Sur suroeste|SSO|1.525|
|Suroeste|SO|168|
|Oeste suroeste|OSO|14|
|Oeste|O|6|
|Oeste noroeste|ONO|7|
|Noroeste|NO|5|
|Norte noroeste|NNO|26|

Nota: Las filas sombreadas en púrpura son las componentes que registran máximas

frecuencias.

En la Figura 11, se observa la proporción de los vientos en la estación de verano para los

siete rangos de velocidades evaluados. En este sentido, los resultados obtenidos son

concluyentes en que el modelo simuló mayoritariamente vientos que varían su velocidad

entre 5,70 - 8,80 m/s con un 45,8% del total, seguido por el rango 3,60 - 5,70 m/s con un

34,4% del total.

**Figura 11. Frecuencia de los vientos en verano, año 2019**

**6.1.1.2** **Dirección y velocidad de vientos predominantes en otoño**

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

Página 29 de 67

En la Figura 12, se presenta la rosa de los vientos para el otoño en donde se observa que

estos tienen origen mayormente en la componente Sur suroeste (SSW), similar a lo ocurrido

en los vientos anuales y los simulados para la estación de verano; constituyendo el 44%,

además se observa que el vector resultante se encuentra ubicado específicamente en el

grado 191 correspondiente a la componente Sur suroeste (SSW), y por consiguiente el

desplazamiento de los vientos ocurrirá hacia la componente nor noreste (NNE).

**Figura 12. Rosa de los vientos otoño, WRF 2019**

En la Tabla 8, se ve la frecuencia del origen de los vientos en los meses de otoño simulada

por el modelo WRF.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

**Tabla 8. Frecuencia de los vientos otoño, WRF.**

Página 30 de 67

|Componente|Col2|Total|
|---|---|---|
|Norte|N|189|
|Nord noreste|NNE|276|
|Noreste|NE|176|
|Este noreste|ENE|45|
|Este|E|15|
|Este Sureste|ESE|19|
|Sureste|SE|29|
|Sur sureste|SSE|45|
|Sur|S|226|
|Sur suroeste|SSO|952|
|Suroeste|SO|97|
|Oeste suroeste|OSO|6|
|Oeste|O|4|
|Oeste noroeste|ONO|4|
|Noroeste|NO|13|
|Norte noroeste|NNO|50|

Nota: Las filas sombreadas en púrpura son las componentes que registran máximas

frecuencias.

En la Figura 13, presenta la frecuencia de los vientos para categoría de vientos simulados

en los meses de otoño, de donde se observa que los vientos en la categoría 3,60 - 5,70

m/s, constituyen el 38,9%, seguido de la categoría 2,1 - 3,6 m/s con un 25,9% de las

velocidades totales de los vientos en esta estación. Por otra parte, es posible apreciar que

los vientos extremos, específicamente los superiores e iguales a 8,8 m/s no superan el 1%

del total de vientos simulados.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

Página 31 de 67

**Figura 13. Frecuencia de los vientos en otoño, año 2019**

**6.1.1.3** **Dirección y velocidad de vientos predominantes en invierno**

En la Figura 14, se presenta la rosa de los vientos para el invierno simulada a través de

WRF. En ésta se observa que los vientos más frecuentes fueron modelados en la

componente Sur suroeste (SSW) y representan el 30,2% del total de la estación, seguido

por vientos simulados en la componente Nor noreste (NNE) y norte (N) con un 18,1% y

16,3% del total, respectivamente. Además, en la figura se muestra que el vector resultante

se encuentra situado en el grado 311, es decir, la componente oeste noroeste, por tanto,

se espera que la dispersión de contaminante se produzca hacia la componente este sureste,

específicamente en el grado 131. Cabe destacar, además, que el promedio de viento

modelado para la estación se encuentra en el rango 3,60 - 5,70 m/s.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

**Figura 14. Rosa de los vientos invierno, WRF 2019**

Página 32 de 67

En la Tabla 9, se muestra la frecuencia de los vientos simulados por el modelo WRF durante

los meses de invierno.

**Tabla 9. Frecuencia de los vientos invierno, WRF.**

|Componente|Col2|Total|
|---|---|---|
|Norte|N|359|
|Nord noreste|NNE|399|
|Noreste|NE|143|
|Este noreste|ENE|66|
|Este|E|29|
|Este Sureste|ESE|24|
|Sureste|SE|24|
|Sur sureste|SSE|37|
|Sur|S|136|
|Sur suroeste|SSO|667|
|Suroeste|SO|135|

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

Página 33 de 67

“Extracción de Áridos Pozo Gallegos”

|Componente|Col2|Total|
|---|---|---|
|Oeste suroeste|OSO|17|
|Oeste|O|16|
|Oeste noroeste|ONO|10|
|Noroeste|NO|23|
|Norte noroeste|NNO|72|

Nota: Las filas sombreadas en púrpura son las componentes que registran máximas

frecuencias.

En la Figura 15, se aprecia la frecuencia de los vientos simulados por el modelo

meteorológico, de donde se puede observar que para el rango de 3,6 - 5,70 m/s se modeló

la mayor frecuencia de vientos con un 31,4% del total, seguidos por vientos ubicados en el

rango de 5,70 - 8,80 m/s y 2,10 - 3,6 m/s con el 24,9 y 22,8% del total. Respecto a las

categorías extremas es decir vientos calmos o las categorías en donde los vientos son

superiores o iguales a 11,10 m/s, el aporte de vientos corresponde a 2,3% y 0,4%,

respectivamente.

**Figura 15. Frecuencia de los vientos en invierno, año 2019**

**6.1.1.4** **Dirección y velocidad de vientos predominantes en primavera**

En la Figura 16, se observa la rosa de los vientos durante la primavera simulados por el

modelo WRF para el año 2019. La máxima frecuencia de vientos tiene origen en la

componente Sur suroeste (SSW) con un 55% de los vientos totales simulados, cuyo vector

resultante para esta estación si sitúa en la componente Sur Suroeste (SSW), sin embargo,

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

Página 34 de 67

al igual que en las otras estaciones del año, existe una influencia de los vientos en otros

orígenes, aunque en proporciones inferiores. Es importante señalar además que la

predominancia de los vientos en esta esta estación se encuentra en el rango 5,70 - 8,80

m/s.

**Figura 16. Rosa de los vientos en primavera, WRF 2019**

En la Tabla 10, se muestra la frecuencia de vientos por componente de origen, de donde se

observa la frecuencia de los vientos simulados por el modelo WRF para la estación de

primavera.

**Tabla 10. Frecuencia de los vientos en primavera, WRF.**

|Componente|Col2|Total|
|---|---|---|
|Norte|N|187|
|Nord noreste|NNE|134|
|Noreste|NE|65|

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

Página 35 de 67

“Extracción de Áridos Pozo Gallegos”

|Componente|Col2|Total|
|---|---|---|
|Este noreste|ENE|21|
|Este|E|14|
|Este Sureste|ESE|20|
|Sureste|SE|18|
|Sur sureste|SSE|24|
|Sur|S|145|
|Sur suroeste|SSO|1.200|
|Suroeste|SO|169|
|Oeste suroeste|OSO|24|
|Oeste|O|14|
|Oeste noroeste|ONO|19|
|Noroeste|NO|24|
|Norte noroeste<br>|NNO<br>|80<br>|

Nota: Las filas sombreadas en púrpura son las componentes que registran máximas frecuencias.

Por otro lado, tal como se observa en la Figura 17, la rosa de los vientos demuestra que

existe una baja frecuencia de vientos extremos, constituyendo un 1,19% para los vientos

calmos y un 0,41% para los vientos iguales o superiores a 11,1 m/s en primavera. Así

mismo, se puede observar en la figura que los vientos que presentaron una mayor

frecuencia son los situados en el rango de 5,7 - 8,8 m/s con un 39,5%.

**Figura 17. Frecuencia de los vientos en primavera, año 2019**

**6.1.1.5** **Perfil diario de las velocidades del viento anuales**

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

Página 36 de 67

“Extracción de Áridos Pozo Gallegos”

En la Figura 18, se observa el perfil de la velocidad del viento simulado por el modelo

meteorológico.

**Figura 18. Perfil diario de velocidad del viento, WRF año 2019**

De la figura se deprende que la propensión anual es que la velocidad del viento se mantiene

con leves fluctuaciones de 4,0 a 4,5 m/s entre las 23 y 7 horas. Desde entonces y hasta las

15 horas la velocidad del viento aumenta paulatinamente hasta llegar a los 5,5 m/s; luego

la velocidad disminuye para para continuar con el ciclo diario.

El análisis del perfil de la velocidad del viento por estación, permite evidenciar aquellas

estaciones en donde se simularon magnitudes de velocidades extremas, estas corresponden

al periodo de primavera con los registros más altos horarios con 6,0 m/s entre las 15 y 16

horas y la época estival con el más alto promedio correspondiente a 5,6 m/s en el transcurso

del día, mientras que la estación en donde se modelaron las velocidades más bajas

correspondería al invierno, con un promedio de 4,2 m/s.

**6.1.2** **Caracterización de la Temperatura del Aire**

**6.1.2.1** **Temperatura Mensual**

Tal como se ve en la Figura 19, la simulación del modelo meteorológico (WRF) sugiere que

la temperatura promedio mensual disminuye en los meses de otoño e invierno y aumenta

en los meses más cálidos (primavera y verano).

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

Página 37 de 67

**Figura 19. Temperatura Mensual WRF, año 2019**

En este sentido la temperatura promedio más alta se simuló para el mes de febrero, donde

alcanzarían los 34,41°C, en tanto que la mínima temperatura promedio mensual se espera

en el mes de julio donde llegaría a los 2,32°C.

Con respecto a la amplitud térmica se observa que esta es mayor en el mes de febrero con

oscilaciones de 26,5oC, mientras que la más baja ocurre en el mes de julio con 12,5oC.

**6.1.2.2** **Perfil Diario de la Temperatura**

La simulación del modelo meteorológico WRF dentro del área de estudio de las temperaturas

horarias, demuestran un comportamiento similar en todas las estaciones del año. En efecto,

como se evidencia en la Figura 20, la evolución de la temperatura diaria resulta tener leves

fluctuaciones entre las 22 y 10 horas, a partir de entonces la temperatura aumenta hasta

alcanzar temperaturas máximas entre las 13 y 17 horas, luego la temperatura disminuye

constantemente hasta las 22 horas, para continuar el ciclo diario.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

Página 38 de 67

“Extracción de Áridos Pozo Gallegos”

**Figura 20. Perfil diario de Temperatura, WRF año 2019**

Con respecto a la amplitud térmica, se hace visible que ésta en los meses de verano es

mayor que en las otras estaciones del año, llegando a una diferencia de 12,8 °C entre la

mínima y máxima promedio horaria, seguido por la primavera y otoño, con diferencias de

9,4 y 9,2oC respectivamente. Con respecto a los meses de invierno la amplitud termina es

inferior a las anteriores, solo alcanzando diferencias de temperatura de 4,9°C.

**6.1.3** **Altura de Capa de Mezcla**

La altura de la capa mezcla es de importancia, pues es un parámetro básico de la modelación

de dispersión de contaminantes, ya que es ahí donde tiene lugar el transporte turbulento

de masas y energía, constituyendo un parámetro que caracteriza la troposfera baja.

El modelo WRF, es capaz de simular la altura de capa de mezcla, de hecho, tal como se

observa en la Figura 21, la evolución de la capa de mezcla diaria tiene un patrón

relativamente similar en todas las estaciones del año.

En el mismo contexto, se observa que, durante los meses de invierno, la altura de capa de

mezcla es más baja en comparación a los otros meses, y, por tanto, se espera que las

condiciones de dispersión de contaminantes sean más desfavorables que en las otras

estaciones.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

Página 39 de 67

“Extracción de Áridos Pozo Gallegos”

En general, se puede observar que durante la noche y madrugada la altura de capa de

mezcla es menor a la simulada durante el día, esto significa que es en ese momento del día

en donde se propician peores condiciones para la dispersión de contaminantes. Esto debido

a la ausencia de aporte energético del sol, influyendo en el intercambio vertical entre

distintos niveles desfavorablemente, de este modo, la agitación turbulenta es poco

significativo.

**Figura 21. Evolución diaria de la altura de capa de mezcla, WRF año 2019**

Con la salida del sol, el aumento de calor de la superficie terrestre, éste es transmitido a la

atmosfera, produciendo agitación en la capa de mezcla lo que provoca un incremento en el

espesor del volumen del aire afectado por el calentamiento del suelo, llegando al máximo

entre las 14 y 16 horas del día, es en este momento del día en donde se propician las

condiciones de máxima inestabilidad atmosférica, favoreciendo la dispersión de

contaminantes.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

**6.2** **Concentraciones Modeladas**

Página 40 de 67

A continuación, se presentan los resultados de la modelación de material particulado

emitidos a la atmosfera. Cabe recordar que, el escenario modelado corresponde a las

emisiones de material particulado, tanto MP10 como MP2,5, las cuales se producen por la

operación y parte de la fase de abandono del proyecto en el año 2.

**6.2.1** **Dispersión e Isoconcentración Material Particulado Respirable, MP10**

A continuación, se presenta el análisis de los resultados para el MP10 tanto para la

concentración promedio anual y 24 horas.

Es importante señalar que la pluma de dispersión de MP10 simulada por el modelo abarca

principalmente la zona de emplazamiento del proyecto y parte de terrenos contiguos a este;

mientras que las máximas concentraciones se encuentran al interior del proyecto.

**6.2.1.1** **Concentración Promedio Anual de MP10**

En la Figura 22, se muestra la pluma de dispersión de la concertación promedio anual de

MP10, de donde se observa lo siguiente:

 Las concentraciones se distribuyen alrededor del proyecto, emplazando su zona de

máxima concentración mayoritariamente en el centro de éste y abarcando el área

circundante al camino de acceso al proyecto. La forma de la pluma tiene sentido con

que es en el mismo predio donde se generan la mayor parte de las emisiones, en

donde ocurre:

1. El transito interno en el camino no pavimentado.

2. Procesamiento de roca chancada

3. Producción de mezcla asfáltica

4. Uso de maquinaria para el apoyo de las obras.

5. Actividades como carga de material y erosión de pilas de acopio.

 La pluma de dispersión se distribuye mayormente en dirección nornoreste

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

Página 41 de 67

desplazándose aproximadamente en 484 m desde la zona de máxima concentración

hacia el borde más alto de la pluma.

 La pluma de dispersión tiene una forma relativamente homogénea en las direcciones

de la rosa de los vientos, pronunciándose de las direcciones sur suroeste y nor

noreste, lo que se condice con el comportamiento de los vientos anuales modelados

por el software WRF para el área de estudio.

 Las concentraciones modeladas van desde los 0,15 μg/m3 a los 0,60 μg/m3, las que

pueden ser catalogadas como de baja magnitud.

 En relación con los puntos receptores elegidos se observa que, 5 de los 14 evaluados

se encuentran dentro de la pluma. Los receptores R12 y R13, se encuentran dentro

de la zona de emplazamiento del proyecto, correspondiendo a unidades

habitacionales de los propietarios del terreno y son los más próximo al área de

instalación de faenas de éste. En tanto, que los receptores R4, R5 y R9 se encuentran

próximos a la planta y muy cercanos al camino de acceso del proyecto, de donde

podría recibir los aportes de las obras relacionada con la operación de las plantas

procesadoras de material pétreo y producción de mezcla asfáltica.

En la Figura 23, se muestra el mapa de isoconcentración, de donde se puede concluir que:

 La pluma se extiende hasta los 548 m por el norte y 409 m por el sur, 367 m al este

y 539 m al oeste desde la zona de máxima concentración, disminuyendo las

concentraciones simuladas en un 73%.

 Las zonas de mayores concentraciones abarcan una superficie de 0,015 ha y la

concentración sería cercana a los 0,55 μg/m3, ubicándose dentro de la zona de

emplazamiento del proyecto y muy fuertemente influenciado por el receptor R13,

que se encuentra colindante al área de instalación de faenas.

 El área total del mapa de isoconcentración abarca una superficie de 72,38 ha.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

**Figura 22. Dispersión de la pluma de MP10 como concentración promedio anual**

Página 42 de 67

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

**Figura 23. Isoconcentración MP10 como concentración promedio anual**

Página 43 de 67

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

**6.2.1.2** **Concentración Promedio 24 horas de MP10**

Página 44 de 67

En la Figura 24, se muestra la pluma de dispersión de la concentración promedio 24 horas

de MP10, de donde se concluye lo siguiente:

 La forma de la pluma de dispersión tiene similitud respecto a la obtenida en la

simulación de la concentración promedio anual, aunque con orientación inclinada

hacia el sureste.

 En la pluma de dispersión se observa un área de concentraciones mayores, cuyo

rango varía entre los 1,03 a 4,11 μg/m3.

 Con base en los resultados obtenidos, existen 6 de 14 puntos receptores inmersos

dentro de la pluma de dispersión, siendo estos, los receptores R4, R5, R6, R9, R12,

R13 y R14.

En la Figura 25, se muestra el mapa de isoconcentración, de donde se puede concluir que:

 La pluma se extiende hasta los 624 m por el norte y 808 m al sur, 860 m al este y

454 m al oeste desde la zona de mayor concentración. A estas distancias la

concentración esperada es de 1,00 μg/m3.

 La pluma de dispersión se distribuye mayormente en dirección sureste

desplazándose aproximadamente en 898 m desde el centro del proyecto hacia el

borde más alto de la pluma.

 Se distingue una zona de máxima concentración de 0,06 ha en donde las

concentraciones son cercanas a 4,00 μg/m3 dentro de la zona de emplazamiento del

proyecto

 El área total del mapa de isoconcentración abarca una superficie de 159 ha.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

**Figura 24. Dispersión de la pluma de MP10 como concentración promedio 24 horas**

Página 45 de 67

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

**Figura 25. Isoconcentración MP10 como concentración promedio 24 horas**

Página 46 de 67

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

Página 47 de 67

**6.2.2** **Dispersión e Isoconcentración Material Particulado Fino Respirable,**

**MP2,5**

A continuación, se presenta el análisis de los resultados para el MP2,5, tanto para la

concentración promedio anual y 24 horas. Es importante señalar que, la pluma de dispersión

de MP2,5 simulada por el modelo abarca principalmente la zona de emplazamiento del

proyecto y los lugares aledaños a éste.

**6.2.2.1** **Concentración Promedio Anual MP2,5**

En la Figura 26, se muestra la pluma de dispersión de la concertación promedio anual de

MP2,5, de donde se concluye que:

 La pluma de dispersión al igual que lo ocurrido para MP10 presenta un

comportamiento en el interior de la zona de emplazamiento del proyecto,

extendiéndose hacia las direcciones sur suroeste y nor noreste.

 La concentración generada en la atmosfera de las emisiones de MP2,5 varía desde

los 0,05 a los 0,10 μg/m3.

 De los puntos receptores modelados, 3 de 14 se encuentran dentro de la pluma de

dispersión, siendo estos los receptores R5, R12 y R13.

En la Figura 27, se muestra el mapa de isoconcentración, de donde se puede concluir:

 La pluma se extiende hasta los 323 m por el norte y 396 m al sur, 404 m al este y

323 m al oeste desde la zona de mayor concentración. A estas distancias la

concentración esperada es de 0,05 μg/m3.

 La distribución de la pluma tiene un importante componente nornoreste,

extendiéndose aproximadamente 429 m.

 En total la pluma abarca un área de aproximada de 44,50 ha.

 La isoconcentración de mayor magnitud es de 0,10 μg/m3 y se ubica dentro del

área de instalación de faenas del proyecto y presenta una superficie de 1,72 ha.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

**Figura 26. Dispersión de la pluma de MP2,5** **como concentración promedio anual**

Página 48 de 67

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

**Figura 27. Isoconcentración MP2,5** **como concentración promedio anual.**

Página 49 de 67

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

**6.2.2.2** **Concentración promedio 24 horas de MP2,5**

Página 50 de 67

En la Figura 28, se muestra la pluma de dispersión de la concertación promedio 24 horas

de MP2,5, de donde se concluye que:

 El comportamiento del material particulado fino como concentración promedio diario,

concentra sus máximas concentraciones en el área del proyecto, donde la pluma

abarca zonas circundantes al área de instalación de faenas de éste.

 La concentración generada en la atmósfera de las emisiones de MP2,5 varían desde

los 0,52 a los 1,04 μg/m3.

 Dentro de la pluma de dispersión existen 6 de 14 receptores, siendo estos los

receptores R4, R5, R6, R9, R12 y R13; los últimos dos receptores son viviendas

ubicadas dentro del área de emplazamiento del proyecto. De todas maneras, las

concentraciones simuladas son de baja magnitud.

En la Figura 29, se muestra el mapa de isoconcentración, de donde se puede concluir que:

 En relación con la dimensión, la pluma se extiende hasta los 259 m por el norte y

439 m por el sur, 459 m al este y 336 m al oeste desde la zona de mayor

concentración. A estas distancias la concentración esperada es de 1,00 μg/m3. La

distribución de la pluma es relativamente homogénea en las direcciones de la rosa

de los vientos con una pequeña prevalencia hacia el desplazamiento en la dirección

suroeste, desplazándose casi 540 m en esa dirección.

 El área donde se ubica la zona de mayor concentración evidencia una superficie 0,12

ha. Es en esta zona donde se encuentra el punto de mayor magnitud, con una

concentración cercana a 1,00 μg/m3.

 El área total de la pluma de isoconcentración abarca una superficie de 46,12 ha.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

Página 51 de 67

**Figura 28. Dispersión de la pluma de MP2,5 como concentración promedio 24 horas**

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

**Figura 29. Isoconcentración MP2,5 como concentración promedio 24 horas**

Página 52 de 67

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

**6.2.3** **Modelación discreta de las emisiones contaminantes**

Página 53 de 67

La modelación discreta de emisiones fue realizada tanto para la concentración de MP10 y

MP2,5 y, los valores de concentración para los puntos receptores presentados en la Tabla

11. Tal como se ha mencionado, estos puntos corresponden a viviendas próximas al

proyecto.

De los resultados obtenidos se destaca:

 Todas las concentraciones simuladas son de baja magnitud.

 Respecto a las concentraciones modeladas de MP10, se puede apreciar que las

concentraciones máximas simularon en los receptores R12, R13, R4 y R5.

Los receptores R12 y R13 son los más cercanos al proyecto, los cuales reciben los

aportes de las emisiones tanto de las obras del proyecto, como de los procesos

productivos involucrados dentro del proyecto y el tránsito por las vías no

pavimentadas internas. Los receptores R4 y R5, las concentraciones simuladas

tienen aporte del tránsito en vías no pavimentadas y en menor medida de las obras

asociadas al movimiento de tierra del proyecto.

 Por su parte, los receptores que reciben mayor aporte de en la concentración de

MP2,5 son los mismos obtenidos de la simulación del MP10, lo que tiene sustento

dado que el M2,5 es la fracción fina del material particulado grueso.

 Las concentraciones modeladas en el receptor R12 de MP10 tanto en concentración

promedio anual y 24 horas, alcanza valores de 0,42 μg/m [3] y 4,14 μg/m [3],

respectivamente. Para el mismo receptor se simuló concentración de MP2,5 de 0,11

μg/m [3] como promedio anual y 1,05 μg/m [3] como concentración 24 horas, siendo el

receptor con las mayores concentraciones modeladas.

 Las concentraciones de menor magnitud son las obtenidas en los receptores R1, R7

y R8, los que se encuentran más alejados de las zonas de emisión.

 Respecto al resto de los receptores, las concentraciones oscilan entre los 0,01 y 0,26

μg/m [3] como concentración promedio anual de MP10, 0,17 y 2,45 μg/m [3] como

concentración promedio 24 horas del mismo contaminante. Mientras que las

concentraciones de MP2,5 varían entre 0,03 y 0,05 μg/m [3] como concentración

promedio anual, y 0,04 y 0,70 μg/m [3] como concentración promedio 24 horas.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

Página 54 de 67

En la Tabla 11, se presentan los resultados de la modelación discreta de cada punto

receptor, de donde es importante destacar que ninguno de los receptores evaluados

constituye una alteración sustancial respecto a la concentración basal que podría existir en

la zona de forma que genere una alteración a la salud y calidad de vida de las personas.

**Tabla 11. Concentración modelada en puntos receptores con respecto a MP10** **y**

**MP2,5**

|Punto|Concentración MP10 (μg/m3)|Col3|Concentración MP2,5(μg/m3)|Col5|
|---|---|---|---|---|
|**Punto**|**Anual**|**24 horas**|**Anual**|**24 horas**|
|R1|0,01|0,09|0,002|0,02|
|R2|0,06|0,80|0,01|0,17|
|R3|0,01|0,17|0,003|0,04|
|R4|0,21|2,49|0,05|0,59|
|R5|0,26|2,45|0,08|0,72|
|R6|0,13|1,86|0,04|0,53|
|R7|0,01|0,11|0,002|0,03|
|R8|0,01|0,13|0,002|0,03|
|R9|0,16|2,24|0,05|0,70|
|R10|0,04|0,64|0,01|0,18|
|R11|0,02|0,26|0,01|0,08|
|R12|0,42|4,14|0,11|1,05|
|R13|0,56|3,24|0,10|0,72|
|R14|0,13|1,49|0,03|0,33|

**6.3** **Aporte a la estación de Monitoreo de Representatividad Poblacional (EMRP)**

A continuación, se presentan los resultados de la concentración de MP10 y MP2,5 simuladas

en la EMRP 21 de Mayo y la proyección con el año de mayor emisión del proyecto.

En la Tabla 12, se observa el aumento de la concentración basal registrada en la EMRP entre

enero y diciembre de 2018 para MP10 y MP2,5.

Los resultados evidencian un aumento de la condición basal de 0,00002% para la

concentración promedio anual de MP10 y de 0,00005% para la concentración promedio 24

horas; mientras que para MP2,5 se simula un incremento de 0,000008% y 0,00002%para

la concentración anual y 24 horas respectivamente.

**Tabla 12. Aumento de la concentración basal en la EMRP 21 de Mayo, año 2018**

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

Página 55 de 67

|Concentración<br>(μg/m3)|MP10|Col3|MP2,5|Col5|
|---|---|---|---|---|
|**Concentración**<br>**(μg/m3)**|**Promedio**<br>**Anual**|**Promedio 24 h**|**Promedio**<br>**Anual**|**Promedio 24 h**|
|**Registros**<br>**EMRP**|54,54|206,7|34,62|185,0|
|**Modelada**|1,02 x 10-5|9,91 x 10-5|2,67 x 10-6|2,58 x 10-5|
|**Proyectada**|**54,54**|**206,7**|**34,62**|**185,0**|

Por lo cual, teniendo en cuenta que esta estación representa zonas urbanas pobladas de la

ciudad y es la estación más próxima al proyecto, resulta importante destacar que se prevé

un **aumento no significativo en la condición basal registrada en esta estación y**

**que la puesta en marcha del proyecto, no representa un empeoramiento**

**sustancial de la calidad del aire.**

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

## 7 Análisis de incertidumbre

Página 56 de 67

Tal como se plantea en la “Guía para el Uso de Modelos de Calidad del Aire en el SEIA”

(2012) de manera textual “cualquier modelo (meteorológico o de calidad del aire) representa

una aproximación a la realidad y, en consecuencia, sus resultados tienen incertidumbres

asociadas” [4] . Ante lo cual, para cuantificar esta incertidumbre, se realiza un análisis entre los

valores entregados por el modelo WRF (valores meteorológicos) y valores observados, en

este caso los datos son extraídos de la Estación El Tambo, propiedad de la Red

Agrometeorológica del Instituto de Investigaciones Agropecuarias (INIA); estación

meteorológica más cercana a la planta y con datos disponibles para el año 2019, mismo año

de simulación del modelo WRF.

El modelo WRF simuló las condiciones meteorológicas dentro de un rango de 59 x 59 celdas

de una dimensión de 1 x 1 km. Para efectos del análisis del ajuste de los datos

meteorológicos simulados se seleccionó una celda en donde se ubica la estación Manzanares

- Renaico, desde la cual se extrajeron los datos y se compararon con los valores observados

de la estación meteorológica antes mencionada.

La correlación de los datos se determinó a través del ajuste por mínimos cuadrados, método

en el que existen dos parámetros de importancia: coeficiente de correlación lineal de

Pearson (r) y el coeficiente de determinación (R [2] ).

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

4 Texto extraído del primer párrafo de la página 38, acápite 7 de la Guía para el Uso de Modelos de
Calidad del Aire en el SEIA (2012)

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

- σ y, es la desviación estándar de y;

Página 57 de 67

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

Los resultados del ajuste del modelo meteorológico se presentan en la siguiente tabla. Luego

de ésta, se presenta el detalle de los valores entregados.

**Tabla 13. Estadísticos de variables meteorológicas modeladas**

|Variable|Coeficiente de<br>correlación lineal<br>(r)|Coeficiente de<br>determinación (R2)|Percent bias<br>(PBIAS)|
|---|---|---|---|
|Temperatura horaria|0,91|0,82|-5,94|

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

Página 58 de 67

|Variable|Coeficiente de<br>correlación lineal<br>(r)|Coeficiente de<br>determinación (R2)|Percent bias<br>(PBIAS)|
|---|---|---|---|
|Velocidad del viento horaria|0,70|0,49|191|
|Dirección del viento horaria|0,38|0,15|19|

**7.1** **Temperatura**

En la

**35**

**30**

**25**

**20**

**15**

**10**

**5**

**0**

|y|= 0,6147x|+ 4,5151|Col4|Col5|Col6|
|---|---|---|---|---|---|
||**R2 = 0,8**|**216**||||
|||||||
|||||||
|||||||
|||||||
|||||||

**0** **5** **10** **15** **20** **25** **30**

**WRF**

Figura 30 se observa la correlación entre la temperatura horaria observada en la estación

Manzanares y las simuladas por el modelo WRF del año 2019.

**35**

**30**

**25**

**20**

**15**

**10**

**5**

**0**

|y|= 0,6147x|+ 4,5151|Col4|Col5|Col6|
|---|---|---|---|---|---|
||**R2 = 0,8**|**216**||||
|||||||
|||||||
|||||||
|||||||
|||||||

**0** **5** **10** **15** **20** **25** **30**

**WRF**

**Figura 30. Correlación entre temperaturas observadas y modeladas**

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

Página 59 de 67

De la figura anterior se observa que existe una correlación directa y positiva entre la variable

observada y la modelada. El valor del coeficiente de correlación lineal es 0,91. Por otro lado,

el coeficiente de determinación sugiere que el modelo es capaz de simular 82% las

temperaturas de forma óptima.

En la Figura 31 se observa la frecuencia de las temperaturas en rangos de clases para los

datos modelados y observados. A partir del gráfico se desprende que, si bien el modelo es

capaz de reproducir de buena manera la variabilidad temporal de la temperatura, su calidad

disminuye considerablemente frente a valores extremos, particularmente aquellos donde la

temperatura es menor 1,6°C y superior a 27,8°C. En términos generales, es posible señalar

que el modelo subestima los datos observados en un 5,94%, valor obtenido a partir del

estadístico percent bias.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

Página 60 de 67

**Figura 31. Frecuencia de temperaturas observadas y modeladas**

**7.2** **Velocidad del viento**

En la Figura 32 se observa la velocidad del viento horaria observada en la Estación

Manzanares - Renaico en comparación con las modeladas por el modelo WRF para el año

2019.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

Página 61 de 67

|Col1|Col2|Col3|Col4|R2 = 0,4857|
|---|---|---|---|---|
||||||
||||||
||||||
||||||
||||||
||||||
||||||

**0,00** **2,00** **4,00** **6,00** **8,00** **10,00**

**WRF**

**Figura 32. Correlación entre velocidad del viento observada y modeladas**

De la figura anterior se observa que existe una correlación positiva entre la variable

observada y la modelada. El valor del coeficiente de correlación lineal es 0,70. Por otro lado,

el coeficiente de determinación sugiere que el modelo es capaz de simular el 49% de los

valores de velocidad del viento horarios de forma óptima.

En la Figura 33 se observa la frecuencia de magnitudes de velocidad del viento en distintas

categorías, de donde se puede observar que el modelo claramente sobrestima los valores

de velocidad de viento sobre los 3,7 m/s. De igual manera, el modelo subestima la frecuencia

de los vientos calmos (entre los 0,0 y 1,2 m/s), es decir, de acuerdo a los datos observados,

en el área de estudio hay una fuerte influencia de vientos calmos. Esto es relevante para la

determinación del área de influencia, pues al distribuir en otras categorías de vientos

mayores, el área es mayor, por lo tanto, la evaluación es conservadora.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

Página 62 de 67

**Figura 33. Frecuencia de velocidad del viento observadas y modeladas**

**7.3** **Dirección del viento**

En la Figura 34 se observa la correlación entre los datos observados en la Estación

Manzanares - Renaico y la modelación para el mismo año de evaluación.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

Página 63 de 67

**400**

**y = 0,3806x + 116,12**

**350**

**300**

**250**

**200**

**150**

**100**

**50**

**0**

|Col1|Col2|Col3|Col4|Col5|Col6|R2 = 0,|1476|
|---|---|---|---|---|---|---|---|
|||||||||
|||||||||
|||||||||
|||||||||
|||||||||
|||||||||
|||||||||

**0** **50** **100** **150** **200** **250** **300** **350** **400**

**WRF**

**Figura 34. Correlación entre dirección del viento observado y simulado**

De la figura anterior se observa que existe una correlación positiva entre la variable

observada y la modelada. El valor del coeficiente de correlación lineal es 0,38. Por otro lado,

el coeficiente de determinación sugiere que el modelo es capaz de simular el 15% de los

valores de dirección del viento horarios de forma óptima.

En la Figura 33 se observa la frecuencia de magnitudes de dirección del viento en distintas

categorías, de donde se puede observar que el modelo claramente subestima los valores de

dirección de viento en todas las clases. De todas formas, esta subestimación corresponde a

un 19% del total de los valores.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

Página 64 de 67

**Figura 35. Frecuencia de velocidad del viento observadas y modeladas**

**7.4** **Test de Bondad de Ajuste sobre el Modelo Meteorológico**

Se prescindirá de la aplicación de test de bondad de ajuste entre los datos modelados y los

observados, debido a que los datos modelados no provienen de una muestra sobre la cual

se ha supuesto una distribución de probabilidad específica, como, por ejemplo: log normal,

binomial, Bernoulli, etc., sino que son el resultado de la simulación a través de la

implementación de un modelo matemático.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

Página 65 de 67

## 8 Conclusión

Se estudió la concentración de las emisiones producto de la operación y abandono paulatino,

proyectadas para el año 2 del proyecto **“Extracción de Áridos Pozo Gallegos”** ubicado

en la comuna de Negrete, región del Biobío. De esta forma, fueron modeladas las emisiones

MP10 y MP2,5 a fin de determinar las concentraciones que éstos tendrán en la atmósfera,

además de prever posibles efectos a la salud de las personas.

Tal como se abordó anteriormente en el informe, el desplazamiento de los contaminantes

ocurre mayoritariamente al interior de la zona de emplazamiento del proyecto y en

proximidades del proyecto. Al respecto se destaca que:

 La pluma de dispersión de MP10 como promedio 24 horas abarca un total de 159

ha, donde las concentraciones corresponden a 1,00 μg/m3. La zona de máxima

concentración se encuentra dentro del área del proyecto y las concentraciones

alcanzan los 4,11 μg/m3.

 Los receptores discretos inmersos dentro de la pluma de dispersión son 6 de los 14

analizados, estando dos de ellos dentro del límite predial del proyecto.

 La pluma de dispersión de MP2,5 tiene un comportamiento similar a la de MP10,

pero abarcando una superficie menor y, por tanto, alcanzando menos receptores

discretos.

 El comportamiento de la dispersión de los contaminantes atmosféricos es

relativamente homogéneo en las direcciones de la rosa de los vientos con una leve

inclinación hacia el nor noreste, lo que se ve justificado con el comportamiento de

los vientos anuales modelados en WRF en la zona del proyecto para el año 2019.

El análisis de la variación de la concentración demuestra que la ejecución del **proyecto no**

**representa una perturbación respecto a las concentraciones que actualmente se**

**registran en la estación de monitoreo analizada.** De hecho, se prevé un aumento de

la condición basal de 0,00002% para la concentración promedio anual de MP10 y de

0,00005% para la concentración promedio 24 horas; mientras que para MP2,5 se simula un

incremento de 0,000008% y 0,00002%para la concentración anual y 24 horas

respectivamente en la Estación 21 de Mayo de propiedad el SINCA.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

Página 66 de 67

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

datos observados de la Estación 21 de Mayo.

Finalmente, la modelación de las emisiones del proyecto de material particulado (MP10 y

MP2,5), resultaron ser de baja magnitud concluyendo que, el funcionamiento del **proyecto**

**no representa un riesgo significativo a la salud ni calidad de vida de la población,**

**según los criterios establecidos en la legislación ambiental vigente** . Considerando

que en ningún caso la concentración proyectada respecto de la concentración basal presentó

un aumento significativo que generara una posible condición de riesgo para las componentes

evaluadas.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones

“Extracción de Áridos Pozo Gallegos”

Página 67 de 67

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

**Tabla 1.: Valores normados para MP10 y MP2,5 en Chile.****

| Nivel | MP10 (μg/m3) | MP2,5 (μg/m3) |
| --- | --- | --- |
| **Promedio Anual** | 50 | 20 |
| **Promedio 24 horas** | 150 | 50 |
| **Alerta** | 195-239 | 80-109 |
| **Preemergencia** | 240-329 | 110-169 |
| **Emergencia** | 330 o mayor | 170 o mayor |

**Tabla 2.: Concentración promedio anual de MP10 estación 21 de Mayo****

| Año | Porcentaje<br>de datos<br>disponibles<br>(%) | Concentración<br>Promedio Anual<br>(μg/m3) | Límite normativo<br>D.S. 59/1998<br>MINSEGEPRES<br>(μg/m3) | Porcentaje de<br>excedencia de la<br>norma (%) |
| --- | --- | --- | --- | --- |
| 2013 | 96 | 53,96 | 50 | 7,92 |
| 2014 | 98 | 55,18 | 55,18 | 10,36 |
| 2015 | 100 | 56,05 | 56,05 | 12,11 |
| 2016 | 99 | 56,84 | 56,84 | 13,67 |
| 2017 | 100 | 45,73 | 45,73 | No excede |
| 2018 | 99 | 54,54 | 54,54 | 9,08 |
| 2019 | 97 | 32,72 | 32,72 | No excede |

**Tabla 3.: Concentración promedio anual de MP2,5 estación 21 de Mayo****

| Año | Porcentaje de<br>datos<br>disponibles (%) | Concentración<br>Promedio Anual<br>(μg/m3) | Límite normativo<br>D.S. 12/2011 MMA<br>(μg/m3) | Porcentaje de<br>excedencia de la<br>norma (%) |
| --- | --- | --- | --- | --- |
| 2013 | 96 | 28,88 | 20,0 | 44,40 |
| 2014 | 97 | 27,48 | 27,48 | 37,42 |
| 2015 | 98 | 29,05 | 29,05 | 45,25 |
| 2016 | 100 | 32,49 | 32,49 | 62,46 |
| 2017 | 99 | 27,74 | 27,74 | 38,69 |
| 2018 | 99 | 34,62 | 34,62 | 73,11 |
| 2019 | 98 | 15,56 | 15,56 | No excede |

**Tabla 4.: Características del modelo****

| Año de modelación | Col2 | 2019 |
| --- | --- | --- |
| **Periodo de Modelación** | **Periodo de Modelación** | 1 año calendario |
| **Resolución temporal** | **Resolución temporal** | 1 hora |
| **Resolución espacial** | **Resolución espacial** | 1 km |
| **Coordenadas del**<br>**centroide** | **Latitud** | -37,580° |
| **Coordenadas del**<br>**centroide** | **Longitud** | -72,558° |
| **DATUM** | **DATUM** | NWS - 84 |
| **Coordenadas del modelo** | **Coordenadas del modelo** | LCC |
| **Dominio de modelación** | **X ** | 59 |
| **Dominio de modelación** | **Y ** | 59 |
| **Dominio de modelación** | **Z ** | 10 |

**Tabla 5.: Descripción de los puntos receptores****

| Receptor | Coordenada UTM WGS 84 HUSO 19 S | Col3 | Descripción | Distancia al centro<br>del proyecto (m) |
| --- | --- | --- | --- | --- |
| **Receptor** | **Este (m)** | **Norte (m)** | **Norte (m)** | **Norte (m)** |
| 1 | 716779 | 5837235 | Casa habitación | 1.359 |
| 2 | 716067 | 5837690 | Casa habitación | 564 |
| 3 | 716554 | 5837544 | Casa habitación | 1.058 |
| 4 | 715618 | 5837322 | Casa habitación | 385 |
| 5 | 715158 | 5837277 | Casa habitación | 541 |
| 6 | 714902 | 5837586 | Casa habitación | 612 |
| 7 | 714069 | 5838113 | Casa habitación | 1.497 |
| 8 | 716268 | 5838656 | Casa habitación | 1.244 |
| 9 | 715012 | 5837652 | Casa habitación | 491 |
| 10 | 714528 | 5837782 | Casa habitación | 973 |
| 11 | 714522 | 5837001 | Casa habitación | 1.889 |
| 12 | 715207 | 5837589 | Casa habitación | 350 |
| 13 | 715471 | 5837484 | Casa habitación | 279 |

**Tabla 6.: Coordenadas de modelación de las fuentes areales****

| Unidad del proyecto | Coordenada UTM, HUSO 18S, DATUM WGS 84 | Col3 |
| --- | --- | --- |
| **Unidad del proyecto** | **Este (m)** | **Norte (m)** |
| Escarpe y Excavación | 715436 | 5838103 |
| Escarpe y Excavación | 715856 | 5837903 |
| Escarpe y Excavación | 715377 | 5837921 |
| Escarpe y Excavación | 715795 | 5837721 |
| Planta Chancadora | 715326 | 5837706 |
| Planta Chancadora | 715360 | 5837677 |
| Planta Chancadora | 715324 | 5837702 |
| Planta Chancadora | 715358 | 5837673 |
| Planta Asfalto | 715281 | 5837564 |
| Planta Asfalto | 715328 | 5837545 |
| Planta Asfalto | 715280 | 5837559 |
| Planta Asfalto | 715327 | 5837540 |
| Grupo Electrógeno 1 | 715298 | 5837556 |
| Grupo Electrógeno 1 | 715301 | 5837554 |
| Grupo Electrógeno 1 | 715297 | 5837553 |
| Grupo Electrógeno 1 | 715300 | 5837552 |
| Grupo Electrógeno 2 | 715257 | 5837520 |
| Grupo Electrógeno 2 | 715258 | 5837519 |
| Grupo Electrógeno 2 | 715256 | 5837518 |
| Grupo Electrógeno 2 | 715258 | 5837517 |
| Grupo Electrógeno 3 | 715328 | 5837703 |
| Grupo Electrógeno 3 | 715329 | 5837702 |
| Grupo Electrógeno 3 | 715326 | 5837701 |
| Grupo Electrógeno 3 | 715328 | 5837700 |
| Grupo Electrógeno 4 | 715356 | 5837678 |
| Grupo Electrógeno 4 | 715358 | 5837677 |
| Grupo Electrógeno 4 | 715355 | 5837676 |
| Grupo Electrógeno 4 | 715357 | 5837675 |
| Acopio Planta Asfalto | 715286 | 5837694 |
| Acopio Planta Asfalto | 715322 | 5837659 |
| Acopio Planta Asfalto | 715271 | 5837673 |

**Tabla 7.: Frecuencia de los vientos verano, WRF.****

| Componente | Col2 | Total |
| --- | --- | --- |
| Norte | N | 57 |
| Nord noreste | NNE | 40 |
| Noreste | NE | 19 |
| Este noreste | ENE | 4 |
| Este | E | 14 |

**Tabla 8.: Frecuencia de los vientos otoño, WRF.****

| Componente | Col2 | Total |
| --- | --- | --- |
| Norte | N | 189 |
| Nord noreste | NNE | 276 |
| Noreste | NE | 176 |
| Este noreste | ENE | 45 |
| Este | E | 15 |
| Este Sureste | ESE | 19 |
| Sureste | SE | 29 |
| Sur sureste | SSE | 45 |
| Sur | S | 226 |
| Sur suroeste | SSO | 952 |
| Suroeste | SO | 97 |
| Oeste suroeste | OSO | 6 |
| Oeste | O | 4 |
| Oeste noroeste | ONO | 4 |
| Noroeste | NO | 13 |
| Norte noroeste | NNO | 50 |

**Tabla 9.: Frecuencia de los vientos invierno, WRF.****

| Componente | Col2 | Total |
| --- | --- | --- |
| Norte | N | 359 |
| Nord noreste | NNE | 399 |
| Noreste | NE | 143 |
| Este noreste | ENE | 66 |
| Este | E | 29 |
| Este Sureste | ESE | 24 |
| Sureste | SE | 24 |
| Sur sureste | SSE | 37 |
| Sur | S | 136 |
| Sur suroeste | SSO | 667 |
| Suroeste | SO | 135 |

**Tabla 10.: Frecuencia de los vientos en primavera, WRF.****

| Componente | Col2 | Total |
| --- | --- | --- |
| Norte | N | 187 |
| Nord noreste | NNE | 134 |
| Noreste | NE | 65 |

**Tabla 11.: Concentración modelada en puntos receptores con respecto a MP10** **y****

| Punto | Concentración MP10 (μg/m3) | Col3 | Concentración MP2,5(μg/m3) | Col5 |
| --- | --- | --- | --- | --- |
| **Punto** | **Anual** | **24 horas** | **Anual** | **24 horas** |
| R1 | 0,01 | 0,09 | 0,002 | 0,02 |
| R2 | 0,06 | 0,80 | 0,01 | 0,17 |
| R3 | 0,01 | 0,17 | 0,003 | 0,04 |
| R4 | 0,21 | 2,49 | 0,05 | 0,59 |
| R5 | 0,26 | 2,45 | 0,08 | 0,72 |
| R6 | 0,13 | 1,86 | 0,04 | 0,53 |
| R7 | 0,01 | 0,11 | 0,002 | 0,03 |
| R8 | 0,01 | 0,13 | 0,002 | 0,03 |
| R9 | 0,16 | 2,24 | 0,05 | 0,70 |
| R10 | 0,04 | 0,64 | 0,01 | 0,18 |
| R11 | 0,02 | 0,26 | 0,01 | 0,08 |
| R12 | 0,42 | 4,14 | 0,11 | 1,05 |
| R13 | 0,56 | 3,24 | 0,10 | 0,72 |
| R14 | 0,13 | 1,49 | 0,03 | 0,33 |

**Tabla 13.: Estadísticos de variables meteorológicas modeladas****

| Variable | Coeficiente de<br>correlación lineal<br>(r) | Coeficiente de<br>determinación (R2) | Percent bias<br>(PBIAS) |
| --- | --- | --- | --- |
| Temperatura horaria | 0,91 | 0,82 | -5,94 |
