---
title: Sin título
author: Maryorie Schulz
date: D:20230809102621-04'00'
language: es
type: report
pages: 60
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ANEXO 3.2 MODELACIÓN ATMOSFÉRICA DE EMISIONES
-->

# ANEXO 3.2 MODELACIÓN ATMOSFÉRICA DE EMISIONES

**Julio 2023**

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

**ÍNDICE**

Página 2 de 60

**1** **INTRODUCCIÓN ..................................................................................................................... 5**

**2** **OBJETIVOS ............................................................................................................................... 7**

**3** **MARCO LEGAL REGULATORIO ......................................................................................... 8**

**3.1** **Estado de la Calidad del Aire en zonas circundantes al proyecto .......................... 9**

**3.2** **Análisis del Cumplimiento Normativo .................................................................... 9**

**4** **JUSTIFICACIÓN DE LOS MODELOS UTILIZADOS EN EL ESTUDIO ...................... 10**

**4.1** **Uso del modelo CALPUFF ...................................................................................... 11**

**4.2** **Uso del modelo WRF ............................................................................................. 13**

**5** **METODOLOGÍA ................................................................................................................... 14**

**5.1** **Modelación de partículas ...................................................................................... 14**
5.1.1 Modelación meteorológica ............................................................................................................. 14
5.1.2 Modelación de dispersión de contaminantes ................................................................................. 14
5.1.3 Criterios para la modelación de partículas ..................................................................................... 17

**6** **RESULTADOS ....................................................................................................................... 21**

**6.1** **Modelamiento meteorológico ............................................................................... 21**
6.1.2 Caracterización de la temperatura del aire .................................................................................... 31
6.1.3 Caracterización de la Precipitación ................................................................................................. 33
6.1.4 Altura de la capa de mezcla ............................................................................................................ 34

**6.2** **Concentraciones Modeladas ................................................................................. 36**

6.2.1 Dispersión e Isoconcentración Material Particulado Respirable, MP10 ......................................... 36
6.2.2 Dispersión e Isoconcentración Material Particulado Fino Respirable, MP2,5 ................................ 43

6.2.3 Modelación discreta de las emisiones contaminantes ................................................................... 49

6.2.4 Aporte a la estación de Monitoreo de Representatividad Poblacional (EMRP) ............................. 50

**7** **ANÁLISIS DE INCERTIDUMBRE ..................................................................................... 51**

**7.1** **Temperatura ......................................................................................................... 53**

**7.2** **Velocidad del viento ............................................................................................. 55**

**8** **CONCLUSIÓN ........................................................................................................................ 58**

**9** **BIBLIOGRAFÍA .................................................................................................................... 60**

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

Página 3 de 60

**ÍNDICE DE FIGURAS**

Figura 1. Ubicación del proyecto .................................................................................. 5
Figura 2. Ubicación EMRP. ......................................................................................... 10
Figura 3. Receptores discretos. ................................................................................... 16
Figura 4. Polígonos de modelación representativos de cada unidad modelada. ............... 20
Figura 5. Rosa de los vientos Anual ............................................................................ 21
Figura 6. Frecuencia de la velocidad de los vientos anual .............................................. 22
Figura 7. Rosa de los vientos verano ........................................................................... 23
Figura 8. Frecuencia de la velocidad de los vientos verano ............................................ 24
Figura 9. Rosa de los vientos otoño ............................................................................ 25
Figura 10. Frecuencia de la velocidad de los vientos otoño. .......................................... 26
Figura 11. Rosa de los vientos Invierno ....................................................................... 27
Figura 12. Frecuencia de la velocidad de los vientos invierno ........................................ 28
Figura 13. Rosa de los vientos primavera .................................................................... 29
Figura 14. Frecuencia de la velocidad de los vientos Primavera. .................................... 30
Figura 15. Perfil diario de velocidad del viento ............................................................. 31
Figura 16. Perfil diario de temperatura ........................................................................ 32
Figura 17. Perfil mensual de precipitación ................................................................... 33
Figura 18. Perfil diario de la altura de la capa de mezcla. .............................................. 34
Figura 19. Dispersión de la pluma de MP10 como concentración de 24 horas ................. 38
Figura 20. Isolíneas de concentración de MP10 como concentración de 24 horas ............ 39
Figura 21. Dispersión de la pluma de MP10 como concentración promedio anual ............ 41
Figura 22. Isolíneas de concentración de MP10 como concentración promedio anual ...... 42
Figura 23. Dispersión de la pluma de MP2,5 como concentración promedio 24 horas....... 44
Figura 24. Isolíneas de concentración de MP2,5 como concentración promedio 24 horas . 45
Figura 25. Dispersión de la pluma de MP2,5 como concentración promedio anual ........... 47
Figura 26. Isolíneas de concentración de MP2,5 como concentración promedio anual ..... 48
Figura 27. Correlación entre temperaturas observadas y modeladas. ............................. 54
Figura 28. Frecuencia de temperaturas observadas y modeladas. .................................. 55
Figura 29. Correlación entre velocidad del viento observada y modeladas. ..................... 56
Figura 30. Frecuencia de velocidad del viento observadas y modeladas. ........................ 57

**ÍNDICE DE TABLAS**

Tabla 1. Valores normados para MP10 y MP2,5 en Chile. ............................................... 8

Tabla 2. Estaciones conectadas a la red SINCA dentro la comuna de Calama. ................. 9

Tabla 3. Características del modelo ............................................................................. 14

Tabla 4. Descripción de los puntos receptores ............................................................. 15

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

Página 4 de 60

Tabla 5. Coordenadas de modelación de las fuentes areales ......................................... 17

Tabla 6. Concentración modelada en puntos receptores con respecto a MP10 y MP2,5. ... 49
Tabla 7. Estadísticos de variables meteorológicas modeladas. ....................................... 53

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

Página 5 de 60

**1** **INTRODUCCIÓN**

El **“Proyecto Ampliación de Zona de Extracción en Pozo Lastrero 2”** (en adelante

proyecto) se ubica en la zona no urbana de la comuna de Calama, Región de los Antofagasta

(Figura 1). El proyecto corresponde a una modificación de un proyecto existente con RCA

del año 2013, el nuevo proyecte consiste en un polígono de extracción de áridos de

aproximadamente 75 hectáreas, con un volumen de extracción cercano a los 2.100.000 m [3],

y manteniendo la zona de procesamiento e instalación de faena.

**Figura 1. Ubicación del proyecto**

En el contexto de la Declaración de Impacto Ambiental del proyecto, se presenta este

Informe de emisiones atmosféricos con el objetivo de predecir la concentración de material

particulado grueso y fino (MP10 y MP2,5), además de evaluar su contribución en puntos

receptores de interés y en las estaciones de calidad del aire más cercanas, esto último

respecto a su situación basal.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

Página 6 de 60

La modelación de las emisiones se realizó en base a los resultados obtenidos de la

estimación de emisiones atmosférica que se presenta junto con el ingreso del proyecto al

SEIA. Dado que el objetivo de la presente modelación es predecir las concentraciones de

MP10 y MP2,5 a las cuales estarán expuestos los receptores cercanos al área de proceso,

es por esto por lo que se considera como escenario de modelación los años donde se alcanza

el máximo de emisiones directas de MP10 y MP2,5. Según el informe de estimación, el año

de máxima emisión es el año 16 del proyecto, el cual considera las emisiones de

correspondiente a la extracciones de los áridos, además de las emisiones de la fase de

abandono, donde se considera las emisiones por atenuaciones de los taludes .

La evaluación de la dispersión y concentración de las emisiones de material particulado se

realizó mediante el programa CALPUFF, el cual es un modelo de dispersión usado

ampliamente para simulaciones de concentraciones ambientales de las emisiones de

operaciones normales, con el objeto de establecer, desarrollar y analizar escenarios de

emisión y regulación. A su vez, CALPUFF es recomendado por el Ministerio de Medio

Ambiente en la “Guía para el Uso de Modelos de Calidad del Aire en el SEIA”, publicada el

año 2023. Los resultados y análisis de esta evaluación se presentan en el siguiente informe.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

Página 7 de 60

**2** **Objetivos**

El presente informe, tiene como objetivo general cuantificar y evaluar el efecto en la

atmósfera debido a las emisiones de contaminantes generadas por el proyecto **“Proyecto**

**Ampliación de Zona de Extracción en Pozo Lastrero 2”** y cuantificar sus

concentraciones.

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
“Ampliación de zona de extracción en pozo lastrero 2”

**3** **Marco Legal Regulatorio**

Página 8 de 60

Actualmente, los contaminantes MP10 y MP2,5 están regulados bajo normas de calidad

primaria, cuyo objetivo es proteger la salud de las personas de los efectos agudos y crónicos

de la exposición de estos contaminantes con un riesgo aceptable. Para esto, se fijan límites

de concentración permitidos, condiciones de superación de la norma y los niveles que dan

paso a situaciones de emergencia ambiental.

El material particulado respirable MP10 es regulado por el D.S. 12/2022 del Ministerio de

Medio Ambiente y el material particulado fino respirable MP2,5 es regulado por el D.S.

12/2011 del Ministerio del Medio Ambiente.

En Tabla 1 se aprecian los valores del límite anual y diario para los contaminante MP10 y

MP2,5, además de los rangos que dan origen a situaciones de alerta, preemergencia y

emergencia ambiental.

**Tabla 1. Valores normados para MP10 y MP2,5 en Chile.**

|Nivel|MP10 (μg/m3)|MP2,5 (μg/m3)|
|---|---|---|
|**Promedio Anual**|50|20|
|**Promedio 24 horas**|130|50|
|**Alerta**|180-229|80-109|
|**Preemergencia**|230-329|110-169|
|**Emergencia**|330 o mayor|170 o mayor|

Fuente: En base a D.S. 12/2022 MMA y D.S. 12/2011 MMA

No obstante, la superación del límite normativo de MP10 no es motivo de condiciones de

superación de la norma, sino que se considera que la norma es incumplida bajo las

siguientes condiciones:

 - Cuando el promedio de la concentración anual de tres años consecutivos iguale o

supere los 50 μg/m3.

 - Si el percentil 98 (P98) de las concentraciones de 24 horas durante un año sea igual

o superior a 130 μg/m3

 - Si durante un año se registrasen siete o más días cuya concentración sea mayor a

130 μg/m3

En el mismo contexto, las condiciones de superación de la norma de MP2,5 son las que se

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

Página 9 de 60

describen a continuación:

 - Cuando el promedio de la concentración anual de tres años consecutivos iguale o

supere los 20 μg/m3.

 - Si el percentil 98 (P98) de las concentraciones de 24 horas durante un año sea igual

o superior a 50 μg/m3

**3.1** **Estado de la Calidad del Aire en zonas circundantes al proyecto**

Dentro de la región de Antofagasta se encuentran varias zonas consideradas como

saturadas y latentes, entre las cuales se la ciudad de Calama y zonas circundantes (D.S

N°57/2009 del MMA), pero en la zona de emplazamiento del proyecto este fuera de este

PDA. En el caso de la comuna donde se emplaza el proyecto (Calama), cuenta con 5

estaciones de monitoreo, las cuales están ubicadas en la ciudad de Calama.

**Tabla 2. Estaciones conectadas a la red SINCA dentro la comuna de Calama.**

|Estación|Contaminantes|Rango de datos|Distancia<br>al<br>proyecto<br>(km)|
|---|---|---|---|
|**Colegio Vergara Keller**|MP2,5, MP10|12/2012 - actualidad | 01/2013 - Actualidad|43,3|
|**Club Deportivo 23 de marzo**|MP2,5, MP10|03/2017 - Actualidad|42,8|
|**Estación Centro**|MP2,5, MP10|10/2012 - Actualidad | 07/2012 - Actualidad|<br>41,8|
|**Oasis**|-|-|41,1|
|**Hospital el Cobre**|MP2,5, MP10|01/2020 - Actualidad | 01/2002 - Actualidad|40,6|

Como se observa en la tabla, solo la estación oasis no tiene información disponible para

realizar un análisis normativo, para ambos contaminantes, pero debido a su distancia al

proyecto carecen de representatividad.

**3.2** **Análisis del Cumplimiento Normativo**

Como se ve en la Figura 2, las estaciones con representatividad poblacional presentes en

las cercanías del proyecto se encuentran en la ciudad de Calama, ubicada a más de 40 km

del proyecto. Debido a que todas las estaciones están a más de 10 km del proyecto, no se

consideran representativas para el sector, por lo tanto, no se tienen estaciones viables para

realizar un análisis normativo en las cercanías del proyecto.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

**Figura 2. Ubicación EMRP.**

**4** **Justificación de los modelos utilizados en el estudio**

Página 10 de 60

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

1 Los contaminantes primarios son los producidos directamente por la actividad humana o la
naturaleza a la atmósfera.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

Página 11 de 60

ejecución de la modelación de dispersión y concentración de emisiones partículas en el aire.

**4.1** **Uso del modelo CALPUFF**

La modelación de dispersión atmosférica de partículas provenientes del proyecto se realizó

con un modelo tipo “puff”, específicamente el modelo CALPUFF. Tal como lo define la guía,

los modelos tipo “puff” son una combinación entre los modelos Gaussianos y los modelos

Lagrangeanos, en el sentido de que esencialmente calculan la dispersión de contaminantes

provenientes de una emisión instantánea, llamada “puff”, a lo largo de una trayectoria. Su

aproximación matemática consiste en estimar la dispersión en forma Gaussiana en cada

punto de una trayectoria; es decir, los modelos tipo “puff” sólo requieren una trayectoria

por “puff”, lo que hace su cálculo mucho más rápido. En el caso de emisiones continuas, se

simulan las trayectorias y la dispersión Gaussiana de muchos “puff”, como es en el caso de

las emisiones de partículas

generadas por el proyecto. Al respecto, el modelo tipo “puff” recomendado por la Guía es

el modelo **CALPUFF** .

Así mismo, es un modelo completo que incorpora herramientas para procesar datos

meteorológicos y geofísicos, modelos de dispersión y post procesamiento. Dicho modelo es

recomendado por la Agencia de Protección Ambiental de los Estados Unidos (EPA) para

modelar transporte a larga distancia de contaminantes.

CALPUFF se compone de tres módulos:

 CALMET: Es un modelo meteorológico que desarrolla campos horarios de viento y

temperatura en una grilla de tres dimensiones. También asocia campos en dos

dimensiones de altura y usos de suelo. **Este modelo fue reemplazado por WRF,**

**tal como lo recomienda la guía antes citada.**

 CALPUFF: Es un modelo de transporte y dispersión de partículas y gases emitidos

desde fuentes modeladas, simulando procesos de dispersión y transformación.

CALPUFF utiliza los datos generados por CALMET. Los archivos de salida de CALPUFF

contienen las concentraciones horarias o deposición por hora de flujos evaluados en

receptores seleccionados.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

Página 12 de 60

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
“Ampliación de zona de extracción en pozo lastrero 2”

**4.2** **Uso del modelo WRF**

Página 13 de 60

El modelo Weather Research and Forecasting Model (WRF), es un modelo numérico de

cuatro dimensiones, recomendado para la generación de datos meteorológicos y es uno de

los modelos de pronóstico meteorológicos más avanzados.

Debido a la falta de una red robusta de estaciones meteorológicas, la “Guía para el Uso de

Modelos de Calidad del Aire en el SEIA” recomienda el uso de WRF por sobre el uso del

CALMET. Además, el mismo documento, sugiere el uso del WRF para la modelación de

dispersión de contaminantes con CALPUFF.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

Página 14 de 60

**5** **Metodología**

**5.1** **Modelación de partículas**

La modelación de partículas depende en gran parte de las tasas de emisión. Estos son

acoplados a un modelo meteorológico, el que en sí mismo simula las condiciones

meteorológicas para la zona de estudio con una resolución temporal de 1 hora; con estos

factores como variable de entrada al modelo, es simulada la dispersión de las partículas en

un modelo, que determinará la trayectoria de las partículas dentro del área de estudio.

**5.1.1** **Modelación meteorológica**

Para la modelación meteorológica, se utilizó un modelo WRF, construido con datos del año

2022 y resolución de 1 km, de extensión 66 km x 66 km. El modelo WRF es capaz de simular

el comportamiento meteorológico, a través de datos meteorológicos para el año de estudio,

el que posteriormente es interpolado dentro del área de estudio del modelo de acuerdo con

la topografía del lugar. En la siguiente tabla se resumen las características del modelo.

**Tabla 3. Características del modelo**

|Año de modelación|Col2|2022|
|---|---|---|
|**Periodo de Modelación**|**Periodo de Modelación**|1 año calendario|
|**Resolución temporal**|**Resolución temporal**|1 hora|
|**Resolución espacial**|**Resolución espacial**|1 km|
|**Coordenadas del**<br>**centroide**|**Latitud**|22,635°S|
|**Coordenadas del**<br>**centroide**|**Longitud**|68,751°W|
|**DATUM**|**DATUM**|NWS - 84|
|**Coordenadas del modelo**|**Coordenadas del modelo**|LCC|
|**Dominio de modelación**|**X **|66|
|**Dominio de modelación**|**Y **|66|
|**Dominio de modelación**|**Z **|10|

**5.1.2** **Modelación de dispersión de contaminantes**

El modelo CALPUFF permite la simulación de la dispersión de contaminantes bajo dos

modalidades:

 **Modelación de la grilla de modelación** . La grilla de modelación viene seteada

del modelo meteorológico, acotando la simulación en la zona circundante más

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

Página 15 de 60

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

5 km x 5 km desde el centroide del proyecto, con resolución variable entre 100 y

500 m.

**Modelación de puntos discretos.** Se consideraron 5 puntos discretos cercanos al

proyecto y 1 punto para representar una ubicación a 10 km del proyecto, como

referencia a un EMRP, como será explicado en el 6.2.3. Las coordenadas se

presentan a continuación y se presenta espacialmente en la figura adjunta.

**Tabla 4. Descripción de los puntos receptores**

|Receptor|Coordenada UTM WGS<br>84 HUSO 18 S|Col3|Descripción|
|---|---|---|---|
|**Receptor**|**Este (m)**|**Norte (m)**|**Norte (m)**|
|1|543.317|7.497.372|Industrial|
|2|542.503|7.497.827|Industrial|
|3|546.291|7.496.158|Industrial|
|4|546.018|7.495.729|Industrial|
|5|542.096|7.496.296|Ruta|
|6|534.286|7.499.667|Punto referencia a 10 km|

2 Como es el caso del tránsito y de las obras asociadas al movimiento de tierra.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

**Figura 3. Receptores discretos.**

Página 16 de 60

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

**5.1.3** **Criterios para la modelación de partículas**

Página 17 de 60

Como escenario de modelación se consideró el año de máxima emisión, como se indica en

la tabla “Emisiones totales generadas por el proyecto” del informe de estimación de

emisiones, lo que ocurre en el año 16 del proyecto. Durante este año ocurre la mayor

emisión de MP debido a que se realizan las actividades propias de la fase de operación,

como la erosión por pila de acopio y el área de proceso. Los detalles de la estimación de

emisiones se presentan en el informe de Estimación de Emisiones Atmosféricas.

Para la modelación se generaron polígonos representativos de las actividades de tránsito en

rutas no pavimentadas, principalmente dentro del proyecto junto con rutas aledañas al

mismo, rutas externas pavimentadas, erosión de pila de acopio, grupo electrógenos, y

actividades denominadas “área de proceso” y “zona de extracción” que involucraban

actividades de chancado, tamizado, correa transportadora, transferencia de materiales,

excavación y combustión de maquinaria fuera de ruta. Además, se incorporaron las

emisiones que se generan en la zona de relleno.

Adicionalmente, se modelaron las emisiones de gases precursores de MP10 y MP2,5 en el

aire a través del módulo MESOPUFF II.

De acuerdo con la metodología aplicable, se realizaron polígonos representativos de cada

unidad para la simulación de las áreas de emisiones de partículas las que, fueron modeladas

como fuentes de emisión discontinuas, es decir, dentro del ciclo diurno, se consideró la

generación de emisiones durante 10 horas (8:00 a 18:00 hrs), ya que ese es el horario

laboral establecido para el proyecto. Las coordenadas y su representación se encuentran en

la siguiente tabla, así como también, en la se presenta la ubicación espacial de éstos.

.

**Tabla 5. Coordenadas de modelación de las fuentes areales**

|Actividad Para<br>Modelar|Elevación<br>(msnm)|Coordenada UTM, HUSO 19S,<br>DATUM WGS 84|Col4|
|---|---|---|---|
|**Actividad Para**<br>**Modelar**|**Elevación**<br>**(msnm)**|**Este (m)**|**Norte (m)**|
|Zona de Extracción|2845|545.009,22|7.496.689,05|
|Zona de Extracción|2845|545.151,02|7.496.687,16|
|Zona de Extracción|2845|545.010,04|7.496.398,37|

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

Página 18 de 60

|Col1|Col2|545.150,60|7.496.397,95|
|---|---|---|---|
|Zona de Relleno|2843|545.011,52|7.496.968,08|
|Zona de Relleno|2843|545.147,38|7.496.966,20|
|Zona de Relleno|2843|545.009,22|7.496.689,05|
|Zona de Relleno|2843|545.151,02|7.496.687,16|
|Área de Proceso|2808|544.011,22|7.497.166,19|
|Área de Proceso|2808|544.029,99|7.497.165,04|
|Área de Proceso|2808|544.011,11|7.497.145,89|
|Área de Proceso|2808|544.028,82|7.497.145,83|
|Zona de Acopio|2807|543.911,39|7.497.195,85|
|Zona de Acopio|2807|544.014,13|7.497.193,27|
|Zona de Acopio|2807|543.899,34|7.497.102,18|
|Zona de Acopio|2807|544.006,33|7.497.097,64|
|Grupo electrógeno|2808|543.927,73|7.497.025,66|
|Grupo electrógeno|2808|543.929,45|7.497.025,42|
|Grupo electrógeno|2808|543.927,45|7.497.023,24|
|Grupo electrógeno|2808|543.928,94|7.497.023,24|
|Ruta Interna No<br>Pavimentada|2809|543.946,78|7.497.030,02|
|Ruta Interna No<br>Pavimentada|2809|543.993,75|7.497.027,92|
|Ruta Interna No<br>Pavimentada|2809|543.945,39|7.497.025,63|
|Ruta Interna No<br>Pavimentada|2809|543.993,58|7.497.023,37|
|Ruta Interna No<br>Pavimentada|2809|543.993,58|7.497.023,37|
|Ruta Interna No<br>Pavimentada|2809|543.996,48|7.497.023,36|
|Ruta Interna No<br>Pavimentada|2809|543.992,99|7.496.972,62|
|Ruta Interna No<br>Pavimentada|2809|543.995,85|7.496.972,76|
|Ruta Interna No<br>Pavimentada|2826|543.995,85|7.496.972,76|
|Ruta Interna No<br>Pavimentada|2826|545.151,90|7.496.972,40|
|Ruta Interna No<br>Pavimentada|2826|543.996,18|7.496.969,75|
|Ruta Interna No<br>Pavimentada|2826|545.151,97|7.496.968,38|
|Ruta Interna No<br>Pavimentada|2847|545.151,97|7.496.968,38|
|Ruta Interna No<br>Pavimentada|2847|545.156,36|7.496.968,37|
|Ruta Interna No<br>Pavimentada|2847|545.151,64|7.496.398,45|
|Ruta Interna No<br>Pavimentada|2847|545.155,78|7.496.398,43|
|Ruta Interna No<br>Pavimentada|2773|542.092,62|7.496.299,34|
|Ruta Interna No<br>Pavimentada|2773|542.211,13|7.496.377,57|
|Ruta Interna No<br>Pavimentada|2773|542.096,52|7.496.294,83|
|Ruta Interna No<br>Pavimentada|2773|542.216,07|7.496.368,71|
|Ruta Interna No<br>Pavimentada|2775|542.566,92|7.496.818,58|
|Ruta Interna No<br>Pavimentada|2775|542.571,62|7.496.813,17|
|Ruta Interna No<br>Pavimentada|2775|542.211,13|7.496.377,57|

|545.150,60 7.496.397,95<br>545.011,52 7.496.968,08<br>545.147,38 7.496.966,20<br>Zona de Relleno 2843<br>545.009,22 7.496.689,05<br>545.151,02 7.496.687,16<br>544.011,22 7.497.166,19<br>544.029,99 7.497.165,04<br>Área de Proceso 2808<br>544.011,11 7.497.145,89<br>544.028,82 7.497.145,83<br>543.911,39 7.497.195,85<br>544.014,13 7.497.193,27<br>Zona de Acopio 2807<br>543.899,34 7.497.102,18<br>544.006,33 7.497.097,64<br>543.927,73 7.497.025,66<br>543.929,45 7.497.025,42<br>Grupo electrógeno 2808<br>543.927,45 7.497.023,24<br>543.928,94 7.497.023,24<br>543.946,78 7.497.030,02<br>543.993,75 7.497.027,92<br>2809<br>543.945,39 7.497.025,63<br>543.993,58 7.497.023,37<br>543.993,58 7.497.023,37<br>543.996,48 7.497.023,36<br>2809<br>543.992,99 7.496.972,62<br>543.995,85 7.496.972,76<br>543.995,85 7.496.972,76<br>545.151,90 7.496.972,40<br>2826<br>543.996,18 7.496.969,75<br>Ruta Interna No<br>545.151,97 7.496.968,38<br>Pavimentada<br>545.151,97 7.496.968,38<br>545.156,36 7.496.968,37<br>2847<br>545.151,64 7.496.398,45<br>545.155,78 7.496.398,43<br>542.092,62 7.496.299,34<br>542.211,13 7.496.377,57<br>2773<br>542.096,52 7.496.294,83<br>542.216,07 7.496.368,71<br>542.566,92 7.496.818,58<br>2775 542.571,62 7.496.813,17<br>542.211,13 7.496.377,57|Col2|Col3|
|---|---|---|
||~~**Concepción**~~<br>~~**Chile**~~<br>Los Pensamientos 197, Huertos Familiares, San Pedro<br>de la Paz<br>(56.41)2287848<br>www.dss.cl|~~**Santiago**~~<br>~~**Chile**~~<br>Av. del Valle Sur 512 Oficina 304, Ciudad Empresaial,<br>Huechuraba<br>(56.2)23494104<br>www.dss.cl|

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

Página 19 de 60

|Col1|Col2|542.216,07|7.496.368,71|
|---|---|---|---|
||2778|542.566,92|7.496.818,58|
||2778|542.876,94|7.497.046,39|
||2778|542.571,62|7.496.813,17|
||2778|542.879,50|7.497.042,41|
||2790|542.879,50|7.497.042,41|
||2790|543.630,57|7.497.054,71|
||2790|542.882,81|7.497.038,18|
||2790|543.630,38|7.497.048,54|
||2804|543.630,57|7.497.054,71|
||2804|543.933,43|7.497.004,12|
||2804|543.630,38|7.497.048,54|
||2804|543.932,09|7.497.000,18|
||2808|543.968,46|7.497.123,69|
||2808|543.973,80|7.497.122,71|
||2808|543.933,43|7.497.004,12|
||2808|543.938,72|7.497.002,79|
|Ruta Externa<br>Pavimentada|2721|537.425,65|7.498.294,71|
|Ruta Externa<br>Pavimentada|2721|542.096,14|7.496.294,26|
|Ruta Externa<br>Pavimentada|2721|537.424,43|7.498.291,00|
|Ruta Externa<br>Pavimentada|2721|542.091,32|7.496.290,05|

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

**Figura 4. Polígonos de modelación representativos de cada unidad modelada.**

Página 20 de 60

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

Página 21 de 60

## 6 Resultados

**6.1** **Modelamiento meteorológico**

En la Figura 5 se presenta la rosa de los vientos anual, construida en base a los datos

generados con el modelo WRF, con datos del año 2022.

**Figura 5. Rosa de los vientos Anual**

La rosa de vientos resultante da cuenta que los vientos simulados tienen su origen desde la

componente sur oeste, noreste y oeste noroeste. Los vientos entre estas coordenadas

abarcan un 35,8% del total de las direcciones de origen de los vientos en la zona. El origen

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

Página 22 de 60

de los vientos con mayor frecuencia es la componente sur oeste, con un 12,8% del origen

de los vientos totales, seguida por la componente noreste, con un 12,4%.

En la Figura 6 podemos ver la frecuencia de la velocidad de viento. Se observa una mayor

tendencia a vientos entre 0,5-2,1 m/s los cuales representan un 35,4% del total de

velocidades simuladas, seguido por las velocidades entre 2,1-3,6 m/s y 3,6-5,7 m/s con un

20,0% y 15,2%, respectivamente.

**Figura 6. Frecuencia de la velocidad de los vientos anual**

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

Página 23 de 60

**6.1.1.1** **Caracterización de la velocidad y dirección del viento, verano**

En la Figura 7 se presenta la rosa de los vientos para los meses de verano, construida en

base a las salidas generadas por el modelo WRF, para el año 2022.

**Figura 7. Rosa de los vientos verano**

La rosa de vientos resultante da cuenta que los vientos simulados tienen su origen desde

las componentes sur oeste, oeste suroeste y oeste. Los vientos entre estas coordenadas

abarcan un 39,5% del total de las direcciones de origen de los vientos en la zona. El origen

de los vientos con mayor frecuencia es la componente sur oeste, con un 24,8% del origen

de los vientos totales, seguida por la componente oeste suroeste, con un 7,4%.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

Página 24 de 60

En la Figura 8 podemos ver la frecuencia de la velocidad de viento para los meses de verano.

Se observa una mayor tendencia a vientos entre 0,5-2,1 m/s, los cuales representan un

35,9% del total de velocidades simuladas., seguidos por los vientos entre 5,7-8,8 m/s 2,1

3,6 m/s, con un 19,3% y un 18,3%, respectivamente.

**Figura 8. Frecuencia de la velocidad de los vientos verano**

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

Página 25 de 60

**6.1.1.2** **Caracterización de la velocidad y dirección del viento, otoño**

En la Figura 9 se presenta la rosa de los vientos para los meses de otoño, construida en

base a los datos generados con el modelo WRF, Para el 2022.

**Figura 9. Rosa de los vientos otoño**

La rosa de vientos resultante da cuenta que los vientos simulados tienen su origen desde

las componentes noreste, sur oeste y oeste noroeste. Los vientos entre estas coordenadas

abarcan un 34,9% del total de las direcciones de origen de los vientos en la zona. El origen

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

Página 26 de 60

de los vientos con mayor frecuencia es la componente noreste, con un 13,7% del origen de

los vientos totales, seguido por los vientos con origen del sur oeste, con un sur 11,0%.

En la Figura 10 podemos ver la frecuencia de la velocidad de viento para los meses de

otoño. Podemos observar que hay tendencia a modelar vientos entre 0,5-2,1 m/s, los cuales

representan un 37% del total de velocidades simuladas., seguido por los vientos entre 2,1

3,6 m/s y 3,6-5,7 m/s con un 20,8% y un 16,8%, respectivamente.

**Figura 10. Frecuencia de la velocidad de los vientos otoño.**

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

Página 27 de 60

**6.1.1.3** **Caracterización de la velocidad y dirección del viento, invierno**

En la Figura 11 se presenta la rosa de los vientos para los meses de invierno, construida en

base a las salidas generadas por el modelo WRF, para el año 2022.

**Figura 11. Rosa de los vientos Invierno**

La rosa de vientos resultante da cuenta que los vientos simulados tienen su origen desde

las componentes noreste, nornoreste y oeste noroeste. Los vientos entre estas coordenadas

abarcan un 41,6% del total de las direcciones de origen de los vientos en la zona. El origen

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

Página 28 de 60

de los vientos con mayor frecuencia es la componente noreste, con un 18,6% del origen de

los vientos totales, seguido por los vientos con origen del nornoreste, con un 12,1%.

En la Figura 12 podemos ver la frecuencia de la velocidad de viento para los meses de

invierno. Podemos observar que hay tendencia a modelar vientos entre 0,5-2,1, los cuales

representan un 35,5% del total de velocidades simuladas, seguido por los vientos entre 2,1

3,6 m/s y 3,6-5,7 m/s, con un 21,3% y 19,8% de las velocidades simuladas.

**Figura 12. Frecuencia de la velocidad de los vientos invierno**

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

Página 29 de 60

**6.1.1.4** **Caracterización de la velocidad y dirección del viento, primavera**

En la Figura 13 se presenta la rosa de los vientos para los meses de primavera, construida

en base a las salidas generadas por el modelo WRF, para el año 2022.

**Figura 13. Rosa de los vientos primavera**

La rosa de vientos resultante da cuenta que los vientos simulados tienen su origen desde

las componentes oeste noroeste, noreste y sur oeste. Los vientos entre estas coordenadas

abarcan un 38,3% del total de las direcciones de origen de los vientos en la zona. El origen

de los vientos con mayor frecuencia es la componente oeste noroeste, con un 15,7% del

origen de los vientos totales, seguido por los vientos con origen del noreste, con un 12,0%.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

Página 30 de 60

En la Figura 14 podemos ver la frecuencia de la velocidad de viento para los meses de

primavera. Podemos observar que hay tendencia a modelar vientos entre 0,5-2,1 m/s, los

cuales representan un 33,2 del total de velocidades simuladas, seguido por los vientos entre

2,1 - 3,6 m/s y 5,7 - 8,8 m/s, con un 19,6% y 18,9% respetivamente.

**Figura 14. Frecuencia de la velocidad de los vientos Primavera.**

**6.1.1.5** **Perfil Diario de las velocidades del viento anuales.**

En la Figura 15 se presenta el perfil horario promedio de las velocidades del viento para

cada estación del año, además de su evolución con respecto a las velocidades anuales. La

figura fue construida de los resultados del modelo WRF, para el año 2022.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

Figura 15. Perfil diario de velocidad del viento

Página 31 de 60

Se aprecia de la figura anterior, que el comportamiento de la velocidad de los vientos para

las distintas estaciones del año, en relación con la variación anual, es muy similar, y solo

presenta una variación en la rapidez del viento obtenida.

Vemos que la velocidad del viento tiende a disminuir constantemente entre las 00:00 a

09:00 horas, luego comienzan a aumentar alcanzando su máximo entre las 12 y 15 UTC,

para luego volver a disminuir hasta completar ciclo. Una diferencia que podemos observar

es como los valores extremos obtenidos en verano, son mayores que a los del resto de la

estaciones.

**6.1.2** **Caracterización de la temperatura del aire**

**6.1.2.1** **Perfil diario de Temperatura**

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

Página 32 de 60

En la Figura 16 podemos ver la temperatura promedio para cada mes del año, construida

con los resultados del modelo WRF, para el año 2022.

**Figura 16. Perfil diario de temperatura**

Podemos observar como el rango de temperaturas observados va entre los 2,5°C y 22,5°C.

Las temperaturas más altas se concentran en los meses de enero, febrero y marzo. En estos

meses podemos ver como la temperatura entre las 00:00 UTC y las 06:00 UTC varía entre

los 7,5°C y 12,5°C, para luego aumentar constantemente hasta alcanzar un máximo entre

las 11:00 UTC y 16:00 UTC, para luego disminuir constantemente hasta completar el ciclo.

En los restos de los meses se da un patrón similar al descrito en los meses de verano, pero

los rangos de temperaturas modeladas van disminuyendo hasta alcanzar un mínimo en los

meses de invierno, donde se encuentran entre los 4°C y 15°C.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

**6.1.3** **Caracterización de la Precipitación**

Página 33 de 60

A partir de la modelación meteorológica del modelo WRF se obtienen las precipitaciones del

lugar, que es un parámetro importante en cuanto a la potencial deposición húmeda de

algunos contaminantes. Según los resultados presentados por el modelo WRF, se concluye

que, para la zona de interés, el total de precipitación para el año 2022 es de 5.3 mm.

**Figura 17. Perfil mensual de precipitación**

En la Figura 17, se muestra la precipitación mensual para el año de estudio, de donde se

concluye que la precipitación en la zona de emplazamiento del proyecto es prácticamente

nula, siendo los meses de enero y junio aquellos con los mayores montos, los cuales

corresponden a 2,9 mm y 2,3 mm, respectivamente.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

**6.1.4** **Altura de la capa de mezcla**

Página 34 de 60

La altura de la capa de mezcla se define como la capa de la atmosfera (troposfera) que está

influenciada de manera directa con las condiciones de la superficie del suelo, y es donde se

da lugar la turbulencia mecánica y térmica (transferencia de calor y materia) de los gases y

partículas presentes en ella (contaminantes), proceso característico de la troposfera baja.

En términos generales, la altura de la capa de mezcla varía de unos cuantos kilómetros en

el día a unos cientos de metros en la noche.

**Figura 18. Perfil diario de la altura de la capa de mezcla.**

Como podemos observar en la figura, se observa que las mayores alturas de la cámara

limite se dan entre las 10:00 UTC y 15 UTC, con la diferencia de que en los meses de

invierno la altura de la capa limite alcanza valores entre 0 m y los 1250 m, mientras que,

en primavera, los alcanzan los 2250 m.

Lo anterior se explica debido a que la capa de mezcla se hace más estable durante las

noches, debido a la ausencia de aporte energético del sol, influyendo negativamente en el

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

Página 35 de 60

intercambio vertical, de este modo, la turbulenta térmica es prácticamente nula. Con la

salida del sol, el calentamiento de la superficie terrestre es transmitido a la atmosfera,

produciendo agitación en la capa de mezcla lo que provoca un incremento en el espesor del

volumen del aire afectado por el suelo, llegando al máximo entre las 12:00 y 15:00 horas

del día, es en este momento del día en donde se propician las condiciones de máxima

inestabilidad atmosférica, favoreciendo la turbulencia térmica y la dispersión de

contaminantes.

Por ende, y a modo de conclusión, se puede mencionar que este parámetro es importante

para la concentración de un contaminante, ya que a medida que disminuye la altura de capa

de mezcla, el contaminante tiende a concentrarse, y, por el contrario, a medida que se aleja

de la superficie, el contaminante tiene a dispersarse.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

**6.2** **Concentraciones Modeladas**

Página 36 de 60

A continuación, se presentan los resultados de la modelación de material particulado

emitidos a la atmosfera. Cabe recordar que, el escenario modelado, corresponde a las

emisiones de material particulado, tanto MP10 como MP2,5, producidas durante el año 16,

donde se superponen las actividades de operación y abandono.

**6.2.1** **Dispersión e Isoconcentración Material Particulado Respirable, MP10**

A continuación, se presenta el análisis de los resultados para el MP10 tanto para la

concentración promedio anual y 24 horas.

**6.2.1.1** **Concentración Promedio 24 horas de MP10**

En la Figura 19, se muestra la pluma de dispersión de la concentración promedio diaria de

MP10, de donde se observa lo siguiente:

 La pluma muestra una dispersión principalmente hacia el Norte y el Sur, siendo más

acotada hacia el Este y el Oeste.

 Las mayores concentraciones se registran en la zona del polígono de modelación de

Zona de acopio y Área de proceso, lo cual es coherente dado que en conjunto estas

actividades concentran el 85% de las emisiones del proyecto para el año 16. En el

punto de máxima concentración se alcanzan entre 120-150 ug/m3.

 Las concentraciones modeladas van desde los 2,00 μg/m3 a los 150,0 μg/m3,

principalmente contenidas dentro de los límites del proyecto, pero desplazándose en

dirección SSO-NNE. Las concentraciones disminuyen rápidamente en la medida que

se alejan del máximo. A 300 m hacia el oeste, la concentración baja drásticamente

un 93,3%, alcanzando los 10 μg/m3.

 De los receptores definidos, solo el receptor R1 se encuentra dentro de la pluma de

dispersión, registrando concentraciones de 2,89 μg/m3. En tanto, el receptor R2

presenta las menores concentraciones de MP10, con 0,39 μg/m3.

En la Figura 20, se muestra el mapa de isoconcentración, de donde se puede concluir que:

 La pluma se extiende hasta los 1470 m por el Norte y 2000 m por el Sur, 1727 m al

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

Página 37 de 60

Este y 885 m al Oeste desde la zona de máxima concentración. Las concentraciones

disminuyen hasta un 98,6% entre el punto de máxima concentración, y la

isoconcentración de 2,0 μg/m3.

El área donde se ubica la zona de mayor concentración abarca una superficie de 0,1

ha, con una concentración equivalente a 150,0 μg/m3. Esta área de cobertura

corresponde principalmente a las actividades de acopio y área de proceso.

El área total del mapa de isoconcentración abarca una superficie de 668 ha.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

**Figura 19. Dispersión de la pluma de MP10 como concentración de 24 horas**

Página 38 de 60

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

**Figura 20. Isolíneas de concentración de MP10 como concentración de 24 horas**

Página 39 de 60

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

**6.2.1.2** **Concentración Promedio Anual de MP10**

Página 40 de 60

En la Figura 21, se muestra la pluma de dispersión de la concentración promedio anual de

MP10, de donde se concluye lo siguiente:

 La pluma de concentración promedio anual de MP10 muestra una zona de máxima

concentración, de forma congruente al caso de promedio de 24 horas. Las

concentraciones descienden rápidamente al alejarse de este punto, particularmente

hacia el oeste.

 La extensión de la pluma de MP10 promedio anual no alcanza a cubrir a ninguno de

los receptores definidos. En particular, el receptor R1 presenta una concentración de

0,59 μg/m3.

En la Figura 22, se muestra el mapa de isoconcentración, de donde se puede concluir que:

 La pluma se extiende hasta los 860 m por el Norte y 1095 m al Sur, 530 m al Oeste

y 993 m al Este desde la zona de mayor concentración. A estas distancias la

concentración modelada es de 2,00 μg/m3.

 La pluma de dispersión crece radialmente, salvo hacia el Oeste.

 Se distingue una zona de máxima concentración de 0,10 ha en donde las

concentraciones son del orden de 90,0 μg/m3, correspondiente a la zona de acopio

y el área de operación.

 El área total del mapa de isoconcentración abarca una superficie de 221,0 ha.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

**Figura 21. Dispersión de la pluma de MP10 como concentración promedio anual**

Página 41 de 60

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

**Figura 22. Isolíneas de concentración de MP10 como concentración promedio anual**

Página 42 de 60

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

Página 43 de 60

**6.2.2** **Dispersión e Isoconcentración Material Particulado Fino Respirable,**

**MP2,5**

A continuación, se presenta el análisis de los resultados para el MP2,5, tanto para la

concentración promedio anual y 24 horas.

**6.2.2.1** **Concentración Promedio 24 horas de MP2,5**

En la Figura 23, se muestra la pluma de dispersión de la concentración promedio diario de

MP2,5, de donde se concluye que:

 La pluma de dispersión presenta sus mayores concentraciones en la zona de acopio

y el área de proceso. El desplazamiento de la pluma es en dirección SSO-NNE, y

extendiéndose hacia el Este.

 La concentración generada en la atmosfera de las emisiones de MP2,5 varía desde

los 2,00 a los 24,00 μg/m3.

 No se registra ningún receptor bajo la pluma de MP2,5 en promedio 24 horas. El

receptor más cercano, R1, registra una concentración de 0,45 μg/m3.

En la Figura 24, se muestra el mapa de isoconcentración, de donde se puede concluir:

 La pluma se extiende hasta los 748 m por el Norte y 1013 m al Sur, 888 m al Este y

340 m al Oeste desde la zona de mayor concentración. A estas distancias la

concentración esperada es de 2,0 μg/m3, reduciéndose un 92% del punto de

máxima concentración.

 El área donde se ubica la zona de mayor concentración abarca una superficie de

0,04 ha, donde se encuentra el punto de mayor magnitud, con concentraciones entre

24,0 μg/m [3] .

 En total la pluma abarca un área aproximada de 160,0 ha.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

**Figura 23. Dispersión de la pluma de MP2,5** **como concentración promedio 24 horas**

Página 44 de 60

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

Página 45 de 60

**Figura 24. Isolíneas de concentración de MP2,5 como concentración promedio 24 horas**

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

**6.2.2.2** **Concentración Promedio Anual de MP2,5**

Página 46 de 60

En la Figura 25, se muestra la pluma de dispersión de la concentración promedio anual de

MP2,5, de donde se concluye que:

 La pluma de concentración de MP2,5 promedio anual, es considerablemente menor

al resto de plumas presentadas. Se extiende principalmente al Sur y al Este, y

presenta valores que van entre los 2,0 μg/m3 a los 15,0 μg/m3.

 Ningún receptor se encuentra dentro de la pluma de dispersión de MP2,5 en

promedio anual. El receptor más cercano, R1, presenta concentraciones de 0,09

μg/m3.

En la Figura 26, se muestra el mapa de isoconcentración, de donde se puede concluir

que:

 En relación con la dimensión, la pluma se extiende hasta los 228 m por el Norte y

470 m por el Sur, 364 m al este y 230 m al oeste desde la zona de mayor

concentración. A estas distancias la concentración esperada es de 2,0 μg/m3.

 El área total de la pluma de isoconcentración abarca una superficie de 31,2 ha.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

**Figura 25. Dispersión de la pluma de MP2,5 como concentración promedio anual**

Página 47 de 60

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

**Figura 26. Isolíneas de concentración de MP2,5 como concentración promedio anual**

Página 48 de 60

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

**6.2.3** **Modelación discreta de las emisiones contaminantes**

Página 49 de 60

La modelación discreta de emisiones fue realizada tanto para la concentración de MP10 y

MP2,5, los valores de concentración para los puntos receptores son presentados en la Tabla

6. Estos puntos están compuestos solo por receptores de carácter industrial, al no

registrarse de otro tipo en las cercanías. También se incluye como receptor un punto a 10

km de distancia del punto de máxima concentración, el que se usará como referencia en el

acápite **¡Error! No se encuentra el origen de la referencia.** para evaluar su aporte a

una EMRP.

De los resultados obtenidos se destaca:

 Todas las concentraciones simuladas son de baja magnitud.

 Respecto a las concentraciones modeladas de MP10, se puede apreciar que las

concentraciones máximas se simularon en los receptores R1, R3 y R4, todos de

carácter industrial. Estos receptores registran 2,89, 1,14 y 1,21 μg/m [3 ] para MP10

promedio 24 horas, y 0,59, 0,23 y 0,23 μg/m [3], respectivamente.

 Los receptores que reciben mayor aporte de la concentración de MP2,5 son los

mismos obtenidos de la simulación del MP10, dado que el MP2,5 es la fracción fina

del material particulado grueso.

 Las concentraciones de menor magnitud son las obtenidas en el receptor R2, con

valores modelados de 0,30 y 0,06 μg/m [3 ] para MP10 y MP2,5 promedio de 24 horas,

y 0,09 y 0,02 μg/m [3 ] para MP10 y MP2,5 promedio anual.

**Tabla 6. Concentración modelada en puntos receptores con respecto a MP10** **y**

**MP2,5.**

|Punto|Concentración MP10 (μg/m3)|Col3|Concentración MP2,5(μg/m3)|Col5|
|---|---|---|---|---|
|**Punto**|**Anual**|**24 horas**|**Anual**|**24 horas**|
|R1|0,59|2,89|0,09|0,45|
|R2|0,09|0,39|0,02|0,06|
|R3|0,23|1,14|0,04|0,18|
|R4|0,23|1,21|0,04|0,19|
|R5|0,15|0,47|0,02|0,07|
|R6|0,0061|0,0230|0,0010|0,0038|

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

Página 50 de 60

**6.2.4** **Aporte a la estación de Monitoreo de Representatividad Poblacional**

**(EMRP)**

Tal como se mencionó en el acápite 3.2 de Análisis del Cumplimiento Normativo, ninguna

EMRP se encuentra lo suficientemente cercana al proyecto para evaluar el aporte del

proyecto a las mismas. De hecho, tal como se muestra en la Figura 2, las estaciones se

encuentran a más de 40 km del proyecto. Sin embargo, se calculó el eventual aporte de una

estación que cumpla con los criterios de representatividad a una distancia de 10 km del

proyecto. Este punto simulado corresponde al receptor R6 de la Tabla 6.

De esta manera, la concentración simulada para el receptor R6 es de 0,0061 para MP10

promedio anual, 0,0230 para MP10 promedio 24 horas, 0,0010 para MP2,5 promedio anual

y 0,0038 para MP2,5 promedio 24 horas. Estas concentraciones son de baja magnitud, por

lo que se desprende que la concentración en las EMRP de Calama sería varias órdenes de

magnitud menor. Al respecto, se prevé un **aumento no significativo en la condición**

**basal registrada en las estaciones meteorológicas con representatividad**

**poblacional y, que la puesta en marcha del proyecto no representa un**

**empeoramiento de la calidad del aire.**

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

## 7 Análisis de incertidumbre

Página 51 de 60

Tal como se plantea en la “Guía para el Uso de Modelos de Calidad del Aire en el SEIA”

(2023) de manera textual “cualquier modelo (meteorológico o de calidad del aire) representa

una aproximación a la realidad y, en consecuencia, sus resultados tienen incertidumbres

asociadas” [3] . Ante lo cual, para cuantificar esta incertidumbre, se realiza un análisis entre los

valores entregados por el modelo WRF (valores meteorológicos) y valores observados, en

este caso los datos son extraídos de la estación Aeródromo Loa - Calama, propiedad de la

Dirección Meteorológica de Chile (DMC); estación meteorológica más cercana al proyecto y

con datos disponibles para el año 2022, mismo año de simulación del modelo WRF.

El modelo WRF simuló las condiciones meteorológicas dentro de un rango de 66 x 66 celdas

de una dimensión de 1 x 1 km. Para efectos del análisis del ajuste de los datos

meteorológicos simulados se seleccionó una celda en donde se ubica la estación Aeródromo

Loa - Calama, desde la cual se extrajeron los datos y se compararon con los valores

observados de la estación meteorológica antes mencionada.

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

 - σ y, es la desviación estándar de y;

3 Texto extraído del primer párrafo de la página 38, acápite 7 de la Guía para el Uso de Modelos de
Calidad del Aire en el SEIA (2012)

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

Página 52 de 60

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

Se presenta el Mean Absolute Error (MAE), el cual es una medida del error promedio

absoluto del modelo con respecto a las observaciones. Este estadístico se calcula mediante

a la siguiente formula.

n

MAE = [1]

n [+ ∑|S] [i] [−O] [i] [|]

i=1

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

Página 53 de 60

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

**Tabla 7. Estadísticos de variables meteorológicas modeladas.**

|Variable|Coeficiente<br>de<br>correlación<br>lineal (r)|Coeficiente de<br>determinación<br>(R2)|RMSE|MAE|BIAS|
|---|---|---|---|---|---|
|Temperatura horaria|0,77|0,61|4,5|3,6|-0,43|
|Velocidad del viento<br>horaria|0,49|25|4,4|3,7|-3.5|

**7.1** **Temperatura**

En la Figura 27 se observa la correlación entre la temperatura horaria observada desde la

estación Aeródromo Loa - Calama respecto a la modelada por el modelo WRF del año 2022.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

Página 54 de 60

**Figura 27. Correlación entre temperaturas observadas y modeladas.**

Respecto a la figura anterior se observa que la correlación entre la temperatura horaria

observada en la estación Aeropuerto el Aeródromo Loa - Calama y la temperatura horaria

modelada por el modelo WRF en el año 2022, es directa y positiva con un coeficiente de

correlación lineal de 0,61. Por otro lado, el coeficiente de determinación sugiere que el

modelo es capaz de simular el 61% de las temperaturas horarias observadas de forma

óptima.

En la Figura 28, se observa la frecuencia de las temperaturas horarias en rangos de clases

tanto para los datos observados como modelados. Es visible que el modelo subestima las

temperaturas en el rango 0°C - 10°C en un 13,5%, mientras que sobrestima las

temperaturas entre los 10°C - 20°C en un 35,8%. Además, vemos que WRF no fue capaz

de modelar los eventos de temperaturas bajo los 0°C presentes en los datos observado y

que subestimo la ocurrencia de evento entre los 20°C - 30°C en un 22,3%.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

Página 55 de 60

**Figura 28. Frecuencia de temperaturas observadas y modeladas.**

**7.2** **Velocidad del viento**

En la Figura 29 se observa la correlación entre la velocidad del viento horaria observada

desde la estación Aeropuerto el Aeródromo Loa - Calama, respecto a la modelada por el

modelo WRF del año 2022.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

Página 56 de 60

**Figura 29. Correlación entre velocidad del viento observada y modeladas.**

Respecto a la figura anterior se observa que la correlación entre la velocidad del viento

horaria observada y la modelada por el modelo WRF en el año 2021, es positiva con un

coeficiente de correlación lineal correspondiente a 0,49. Por otro lado, el coeficiente de

determinación sugiere que el modelo es capaz de simular el 25% de las velocidades del

viento horarias de forma óptima en la estación, en consecuencia, el modelo se ajusta

parcialmente a los datos observados.

En la Figura 30 se observa la frecuencia de la velocidad del viento horaria en rangos de

clases tanto para los datos observados como modelados. En efecto, el modelo claramente

sobreestima los eventos de Calma, viento entre 0,5 - 2,1 m/s, tanto que, en el caso de los

primeros, la estación no registro ninguna calma, mientras que el modelo registro 14,6%.

Además, podemos ver como el modelo subestimo ocurrencia de eventos de viento mayores

a 5,7 m/s en una gran medida.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

Página 57 de 60

**Figura 30. Frecuencia de velocidad del viento observadas y modeladas.**

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

Página 58 de 60

## 8 Conclusión

Se estudió la concentración de las emisiones producto de la construcción y operación

proyectada para el año 16 del proyecto **“Ampliación de zona de extracción en pozo**

**lastrero 2”** ubicado en la comuna de Calama, región de Antofagasta. De esta forma, fueron

modeladas las emisiones MP10 y MP2,5 a fin de determinar las concentraciones que éstos

tendrán en la atmósfera, además de prever posibles efectos a la salud de las personas.

Tal como se abordó anteriormente en el informe, el desplazamiento de los contaminantes

ocurre mayoritariamente en la zona destinada a la operación del proyecto y en sus

alrededores. Al respecto se destaca que:

 La pluma de dispersión de MP10 como promedio 24 horas abarca un total de 668

ha, luego de lo cual las concentraciones son menores a 2,0 μg/m3. La zona de

máxima concentración se genera principalmente por el por el acopio de material y

área de proceso en donde las concentraciones alcanzan has 150 μg/m3. El

desplazamiento de la pluma se principalmente en dirección SSO-NNE, y hacia el Este.

Las concentraciones decaen rápidamente hacia el Oeste, en dirección al receptor R1,

disminuyendo un 93,3% en los primeros 300 m.

 Solo un receptor se encuentra dentro de las plumas generadas, R1. En este punto

las concentraciones alcanzan 2,89 μg/m3 para MP10 promedio 24 horas. Cabe

señalar que todos los receptores considerados son de tipo industrial.

 La pluma de dispersión de MP2,5 tiene un comportamiento similar a la de MP10,

extendiéndose similarmente, pero con concentraciones de menor magnitud y no

cubre ninguno de los receptores propuestos.

Dada la ubicación del proyecto, no existe ninguna estación de monitoreo con

representatividad poblacional que pueda considerarse para evaluar el impacto sobre estas.

Sin embargo, se consideró un receptor de referencia a 10 km de distancia, el cual registró

concentraciones de 0,023 y 0,0038 para MP10 y MP2,5 en promedio 24 horas, lo que permite

prever que el **proyecto no representa una perturbación respecto a las**

**concentraciones que actualmente se registran en las estaciones de monitoreo.**

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

Página 59 de 60

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

datos observados de la Estación Carriel Sur - Concepción propiedad del INIA.

Finalmente, la modelación de las emisiones de material particulado (MP10 y MP2,5) del

proyecto, resultaron ser de baja magnitud concluyendo que, el funcionamiento del

**proyecto no representa un riesgo significativo a la salud ni calidad de vida de la**

**población, según los criterios establecidos en la legislación ambiental vigente** .

Considerando que en ningún caso la concentración proyectada respecto de la concentración

basal presentó un aumento significativo que generara una posible condición de riesgo para

las componentes evaluadas.

DECLARACIÓN DE IMPACTO AMBIENTAL

Informe de Modelación Atmosférica de Emisiones
“Ampliación de zona de extracción en pozo lastrero 2”

Página 60 de 60

## 9 Bibliografía

Hernandez- Garces, A., J. Souto, A. Rodríguez, S. Saavera, J. Casares, 2015.

Recuperado

el 27 de junio de 2016, desde

http://revistas.ucm.es/index.php/FITE/article/view/51192/47527

Hernández-Garces, A., U. Jáuregui-Haga, J. González, J. Caseres-Long, S. Saavedra, F.

Guzmán-Martínez, A. Torres-Valle, 2016. Aplicaciones del modelo lagrangiano de dispersión

atmosférica CALPUFF, Ciencias de la Tierra y el Espacio, enero-junio, Vol. 17, No 1, p. 37.

ISSN 1729-3790. Recuperado el 29 de junio de 2016, desde

http://www.iga.cu/publicaciones/revista/assets/calpuffreview2.pdf.

Servicio de Evaluación Ambiental, 2023, Guía para el Uso de Modelos de Calidad del Aire en

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
| **Promedio 24 horas** | 130 | 50 |
| **Alerta** | 180-229 | 80-109 |
| **Preemergencia** | 230-329 | 110-169 |
| **Emergencia** | 330 o mayor | 170 o mayor |

**Tabla 2.: Estaciones conectadas a la red SINCA dentro la comuna de Calama.****

| Estación | Contaminantes | Rango de datos | Distancia<br>al<br>proyecto<br>(km) |
| --- | --- | --- | --- |
| **Colegio Vergara Keller** | MP2,5, MP10 | 12/2012 - actualidad | 01/2013 - Actualidad |
| **Club Deportivo 23 de marzo** | MP2,5, MP10 | 03/2017 - Actualidad | 42,8 |
| **Estación Centro** | MP2,5, MP10 | 10/2012 - Actualidad | 07/2012 - Actualidad |
| **Oasis** | - | - | 41,1 |
| **Hospital el Cobre** | MP2,5, MP10 | 01/2020 - Actualidad | 01/2002 - Actualidad |

> ⚠️ Confianza de extracción: 0.73

**Tabla 3.: Características del modelo****

| Año de modelación | Col2 | 2022 |
| --- | --- | --- |
| **Periodo de Modelación** | **Periodo de Modelación** | 1 año calendario |
| **Resolución temporal** | **Resolución temporal** | 1 hora |
| **Resolución espacial** | **Resolución espacial** | 1 km |
| **Coordenadas del**<br>**centroide** | **Latitud** | 22,635°S |
| **Coordenadas del**<br>**centroide** | **Longitud** | 68,751°W |
| **DATUM** | **DATUM** | NWS - 84 |
| **Coordenadas del modelo** | **Coordenadas del modelo** | LCC |
| **Dominio de modelación** | **X ** | 66 |
| **Dominio de modelación** | **Y ** | 66 |
| **Dominio de modelación** | **Z ** | 10 |

**Tabla 4.: Descripción de los puntos receptores****

| Receptor | Coordenada UTM WGS<br>84 HUSO 18 S | Col3 | Descripción |
| --- | --- | --- | --- |
| **Receptor** | **Este (m)** | **Norte (m)** | **Norte (m)** |
| 1 | 543.317 | 7.497.372 | Industrial |
| 2 | 542.503 | 7.497.827 | Industrial |
| 3 | 546.291 | 7.496.158 | Industrial |
| 4 | 546.018 | 7.495.729 | Industrial |
| 5 | 542.096 | 7.496.296 | Ruta |
| 6 | 534.286 | 7.499.667 | Punto referencia a 10 km |

**Tabla 5.: Coordenadas de modelación de las fuentes areales****

| Actividad Para<br>Modelar | Elevación<br>(msnm) | Coordenada UTM, HUSO 19S,<br>DATUM WGS 84 | Col4 |
| --- | --- | --- | --- |
| **Actividad Para**<br>**Modelar** | **Elevación**<br>**(msnm)** | **Este (m)** | **Norte (m)** |
| Zona de Extracción | 2845 | 545.009,22 | 7.496.689,05 |
| Zona de Extracción | 2845 | 545.151,02 | 7.496.687,16 |
| Zona de Extracción | 2845 | 545.010,04 | 7.496.398,37 |

**Tabla 6.: Concentración modelada en puntos receptores con respecto a MP10** **y****

| Punto | Concentración MP10 (μg/m3) | Col3 | Concentración MP2,5(μg/m3) | Col5 |
| --- | --- | --- | --- | --- |
| **Punto** | **Anual** | **24 horas** | **Anual** | **24 horas** |
| R1 | 0,59 | 2,89 | 0,09 | 0,45 |
| R2 | 0,09 | 0,39 | 0,02 | 0,06 |
| R3 | 0,23 | 1,14 | 0,04 | 0,18 |
| R4 | 0,23 | 1,21 | 0,04 | 0,19 |
| R5 | 0,15 | 0,47 | 0,02 | 0,07 |
| R6 | 0,0061 | 0,0230 | 0,0010 | 0,0038 |

**Tabla 7.: Estadísticos de variables meteorológicas modeladas.****

| Variable | Coeficiente<br>de<br>correlación<br>lineal (r) | Coeficiente de<br>determinación<br>(R2) | RMSE | MAE | BIAS |
| --- | --- | --- | --- | --- | --- |
| Temperatura horaria | 0,77 | 0,61 | 4,5 | 3,6 | -0,43 |
| Velocidad del viento<br>horaria | 0,49 | 25 | 4,4 | 3,7 | -3.5 |
