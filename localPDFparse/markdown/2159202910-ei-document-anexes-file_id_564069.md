---
title: Microsoft Word - Informe Modelación Emisiones PS_Burgos Vcorregida_ ObsLM.docx
author: Desconocido
date: D:20230512213130Z00'00'
language: es
type: report
pages: 46
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Modelación de Emisiones Atmosféricas “DIA PARQUE SOLAR BURGOS” Región del Biobío
  - −6∑ "!%& O ! )
  - " M
  - −(∑ "!%& M ! )
-->

# Modelación de Emisiones Atmosféricas “DIA PARQUE SOLAR BURGOS” Región del Biobío

## Elaborado por: Lorena Morales M. Asesorías Ambientales y Otros EIRL 12-05-2023

**Modelación de Estimaciones Atmosféricas**

**“DIA PARQUE SOLAR BURGOS”**

## Contenido

1. INTRODUCCIÓN ........................................................................................................................... 4

2. OBJETIVOS ................................................................................................................................... 5

3. MODELACIÓN DE DISPERSIÓN ATMOSFÉRICA ............................................................................ 6

3.1 Descripción y Justificación del Modelo ............................................................................... 6

3.2 Base Teórica del Modelo utilizado ...................................................................................... 7

3.3 Caracterización Meteorológica ........................................................................................... 8

3.3.1 Análisis Meteorología Observacional ............................................................................ 9

3.4 Modelo Meteorológico ..................................................................................................... 15

3.4.1 Justificación Modelo Meteorológico ........................................................................... 15

3.4.2 Descripción Modelo Meteorológico ............................................................................ 15

3.5 Análisis De Incertidumbre ................................................................................................. 22

3.6 Características Del Dominio De Modelación Y Su Entorno ................................................ 23

3.6.1 Características de Dominio .......................................................................................... 23

3.7 Datos topográficos y uso de suelo .................................................................................... 24

3.8 Fuentes De Emisión ........................................................................................................... 25

3.9 Receptores ........................................................................................................................ 25

3.10 Análisis y Caracterización de Calidad de Aire de la zona del proyecto .............................. 27

4. RESULTADOS MODELACIÓN CALIDAD DEL AIRE ....................................................................... 28

4.1 Determinación Área de Influencia ..................................................................................... 29

4.1.1 Concentración Material Particulado 10 ....................................................................... 30

4.1.2 Concentración Material Particulado 2.5 ...................................................................... 32

4.1.3 Concentración NOx ..................................................................................................... 35

4.1.4 Concentración CO ....................................................................................................... 37

4.1.1 Concentración SO2 ...................................................................................................... 40

5. CONCLUSIÓN ............................................................................................................................. 44

6. REFERENCIAS ............................................................................................................................. 45

_**www.modelacionesatmosfericas.cl**_
1

**Modelación de Estimaciones Atmosféricas**

**“DIA PARQUE SOLAR BURGOS”**

**ÍNDICE DE TABLAS**

Tabla 1 Tabla 3.5: Características de los Datos del Modelo Meteorológico WRF Usados para la

Evaluación del Proyecto .................................................................................................................... 15

Tabla 2 : Comparación vientos observados vs modelados (WRF) ..................................................... 22

Tabla 3 Total emisiones por fase del Proyecto .................................................................................. 25

Tabla 4 Concentración (ug/m3) promedio de contaminantes en EMRP durante el año 2020 ........ 27

Tabla 5 Normativa aplicable .............................................................................................................. 28

Tabla 6 Concentración MP10 en Receptores Discretos ................................................................... 30

Tabla 7 Concentración MP2.5 en Receptores Discretos .................................................................. 32

Tabla 8 Concentración NOx en Receptores Discretos ...................................................................... 35

Tabla 9 Concentración CO en Receptores Discretos ........................................................................ 37

Tabla 10 Concentración SO2 en Receptores Discretos .................................................................... 40

**ÍNDICE DE IMÁGENES**

Imagen 1 Localización Estación Meteorológica Superficial ................................................................. 8

Imagen 2 Serie de tiempo Dirección de Viento (soplando desde) observadas en las Estación La Unión,

año 2022 ............................................................................................................................................. 9

Imagen 3 Serie de tiempo Dirección de Viento (soplando desde) observadas en las Estación La Unión,

Enero-Marzo 2022 ............................................................................................................................ 10

Imagen 4 Serie de tiempo Dirección de Viento (soplando desde) observadas en las Estación La

Unión, Abril-Junio 2022 ..................................................................................................................... 10

Imagen 5 Serie de tiempo Dirección de Viento (soplando desde) observadas en las Estación La Unión,

Julio-Septiembre 2022 ...................................................................................................................... 11

Imagen 6 Serie de tiempo Dirección de Viento (soplando desde) observadas en las Estación La Unión,

Octubre-Diciembre 2022 ................................................................................................................... 11

Imagen 7 Serie de tiempo Velocidad de Viento observadas en las Estación La Unión, Enero
Diciembre 2022. ................................................................................................................................ 12

Imagen 8 Serie de tiempo Velocidad de Viento observadas en las Estación La Unión, Enero-Marzo

2022. ................................................................................................................................................. 13

Imagen 9 Serie de tiempo Velocidad de Viento observadas en las Estación La Unión, Abril - Junio

2022 .................................................................................................................................................. 13

Imagen 10 Serie de tiempo Velocidad de Viento observadas en las Estación La Unión Julio
Septiembre 2022 ............................................................................................................................... 14

Imagen 11 Serie de tiempo Velocidad de Viento observadas en las Estación La Unión, Octubre
Diciembre 2022. ................................................................................................................................ 14

Imagen 12 Ejemplo de Campos de Vientos generados por el Modelo WRF en el Dominio .............. 16

Imagen 13 Serie de tiempo Dirección de Viento (soplando desde) modelada (WRF) año

2022. ................................................................................................................................................. 17

_**www.modelacionesatmosfericas.cl**_
2

**Modelación de Estimaciones Atmosféricas**

**“DIA PARQUE SOLAR BURGOS”**

Imagen 14 Serie de tiempo Dirección de Viento (soplando desde) modelada (WRF) Enero

a Marzo del año 2022. ....................................................................................................................... 17

Imagen 15 Serie de tiempo Dirección de Viento (soplando desde) modelada (WRF) Abril

a Junio del año 2022. ........................................................................................................................ 18

Imagen 16 Serie de tiempo Dirección de Viento (soplando desde) modelada (WRF) Octubre

a Diciembre del año 2022. ................................................................................................................ 19

Imagen 17 Serie de tiempo Velocidad de Viento modelada (WRF) Año 2022. ................................ 19

Imagen 18 Serie de tiempo Velocidad de Viento modelada (WRF) Enero a Marzo Año 2022. ........ 20

Imagen 19 Serie de tiempo Velocidad de Viento modelada (WRF) Abril a Junio Año 2022. ........... 20

Imagen 20 Serie de tiempo Velocidad de Viento modelada (WRF) Julio a Septiembre Año 2022. . 21

Imagen 21 Serie de tiempo Velocidad de Viento modelada (WRF) Octubre a Diciembre Año 2022.

.......................................................................................................................................................... 21

Imagen 22 Dominio de Modelación .................................................................................................. 23

Imagen 23 Topografía del dominio de modelación .......................................................................... 24

Imagen 24 Emplazamiento Grilla de Receptores .............................................................................. 25

Imagen 25 Emplazamiento Receptores Discretos ............................................................................. 26

Imagen 26 Ubicación Estación de Monitoreo Calidad de Aire .......................................................... 27
Imagen 27 Área de Influencia Componente Aire y Salud de la Población ........................................ 29

_**www.modelacionesatmosfericas.cl**_
3

**Modelación de Estimaciones Atmosféricas**

**“DIA PARQUE SOLAR BURGOS”**

## 1. INTRODUCCIÓN

El presente informe contiene los resultados de la modelación de calidad del aire para material

particulado y gases de combustión emitidos durante las fases de construcción, operación y cierre

de la DIA “Parque Solar Burgos”, comuna de la Unión.

Se contempla específicamente verificar que el proyecto no genere alguno de los efectos,

características o circunstancias indicadas en el artículo 5 del D.S. N° 40/2012 del MMA, sobre los

receptores sensibles identificados, adjuntando las isolíneas de concentración que permiten

observar la zona de máximo impacto del proyecto.

Para la línea de base meteorológica se realizó una caracterización general del clima y la

meteorología imperante en la zona. Para ello, se utilizó meteorología determinada por el modelo

meteorológico WRF, adicionalmente se recurrió a la recopilación de antecedentes en organismos

públicos.

_**www.modelacionesatmosfericas.cl**_
4

**Modelación de Estimaciones Atmosféricas**

**“DIA PARQUE SOLAR BURGOS”**

## 2. OBJETIVOS

El objetivo general del estudio es modelar las emisiones atmosféricas generadas por las fases de

construcción, operación y cierre de la “DIA Parque Solar Burgos” a fin de evaluar el impacto en la

calidad del aire en las distintas fases del proyecto.

Para lograr el objetivo principal del presente informe, se plantean objetivos específicos que apoyan

la evaluación que se realizó. Así los objetivos específicos son:

 - Realizar una caracterización meteorológica, con el fin de tener un conocimiento de los

fenómenos meteorológicos y climáticos del área en la que tendrá influencia el Proyecto.

 - Realizar un análisis de la línea de base de calidad del aire, en el cual se busca conocer los

niveles basales de concentración de material particulado característicos del área del

proyecto.

 - Evaluar el impacto sobre la calidad del aire mediante la implementación del modelo de

calidad del aire, en las fases de construcción, operación y cierre del proyecto.

_**www.modelacionesatmosfericas.cl**_
5

**Modelación de Estimaciones Atmosféricas**

**“DIA PARQUE SOLAR BURGOS”**

## 3. MODELACIÓN DE DISPERSIÓN ATMOSFÉRICA

Por medio de la ejecución de una serie de etapas, se logró determinar la estimación de las

concentraciones en los escenarios definidos, para un dominio determinado de receptores de interés

y que permitió, además, la generación de curvas de isoconcentración generadas a través de una

malla con equiespaciado cada 1 kilómetro.

La metodología se basa en las recomendaciones definidas en la Guía de Uso de Modelos de Calidad

de Aire en el SEIA, año 2014. En este caso en particular, se utiliza el modelo CALPUFF siguiendo la

recomendación de la misma Guía de Uso de Modelos de Calidad del Aire, utilizando como criterio

principal la mayoría de los receptores de interés, que se ubican dentro del área de modelación y que

constituye el área de influencia de la componente.

### 3.1 Descripción y Justificación del Modelo

Considerando lo indicado en la Guía para el uso de Modelos de Calidad de Aire en el SEIA y en el

marco de la Evaluación Ambiental del Proyecto _**“Parque Solar Burgos”,**_ se considera pertinente la

presentación de la Modelación de emisiones atmosféricas generadas durante todas las fases del

proyecto, como herramienta para evaluar el impacto de dichas emisiones sobre el recurso aire, y el

consecuente impacto sobre otros recursos naturales renovables y la salud de las personas.

Según lo establecido por la Guía para el uso de Modelos de Calidad del Aire en el SEIA, la selección

del modelo de Calidad del Aire utilizado en el presente estudio se realizó debido a la topografía

compleja del área donde se emplaza el proyecto y al alcance de las emisiones de este. Por esta

razón, fue usado el modelo CALPUFF explicado a continuación.

_**www.modelacionesatmosfericas.cl**_
6

**Modelación de Estimaciones Atmosféricas**

**“DIA PARQUE SOLAR BURGOS”**

### 3.2 Base Teórica del Modelo utilizado

La simulación del aporte del proyecto a las concentraciones de contaminantes se realizará mediante

el modelo CALPUFF, recomendado por la U. S. EPA para la evaluación de dispersión de

contaminantes desde fuentes continuas.

CALPUFF es un sistema de modelación avanzado para calidad del aire que considera además, la

meteorología de carácter no permanente. Su desarrollo estuvo a cargo del Sigma Research

Corporation mientras que su actual mantenimiento es responsabilidad del Atmospheric Studies

Group de TRC Solutions. Debido a su desempeño, CALPUFF fue catalogado por la USEPA como

modelo recomendado para la evaluación del impacto en la calidad del aire de distintos tipos de

proyectos, especialmente, de aquellos donde es necesario considerar la variación en el tiempo y en

el espacio de las condiciones meteorológicas y su incidencia en el transporte, transformación y

remoción de contaminantes.

El sistema de modelación está compuesto por los siguientes componentes principales:

**CALMET:** es un modelo meteorológico que genera campos de viento tridimensionales horarios, en

base a registros superficiales y del perfil de altura. Además, las salidas de este modelo entregan

información en el dominio de la modelación sobre alturas de la capa de mezcla, características

superficiales y propiedades de dispersión.

**CALPUFF:** corresponde a un modelo Lagrangiano-Gaussiano de transporte y dispersión de soplos o

“puff” emitidos por las fuentes consideradas por el proyecto. De esta forma, a partir de la

información de emisiones y meteorología proporcionada, el programa simula el proceso de

dispersión y transformación de los contaminantes, en un rango de validez desde metros hasta

cientos de kilómetros.

**CALPOST:** es un programa utilizado para el post-procesamiento de los resultados obtenidos en la

modelación de CALPUFF, y que permite calcular las concentraciones en los receptores según los

promedios requeridos por cada norma. Además, es capaz de gestionar los datos de cada

contaminante según el período de tiempo requerido, ordenando las máximas concentraciones

obtenidas e identificando el momento en que cada una de éstas suceden (hora, día, mes y año).

Dentro de las capacidades del sistema de modelación se destacan los siguientes puntos:

 - Permite modelar transporte de largo alcance (hasta 200 km).

 - Simula procesos meteorológicos complejos tales como: velocidades de vientos muy bajas,

estancamiento, fumigación y recirculación.

 - Es capaz de incorporar efectos debidos a la proximidad al borde costero o a causa de

topografía compleja.

_**www.modelacionesatmosfericas.cl**_
7

**Modelación de Estimaciones Atmosféricas**

**“DIA PARQUE SOLAR BURGOS”**

 - Modela contaminantes de forma simultánea fuentes de diverso tipo y que modifican su

nivel de actividad a lo largo del tiempo.

Permite diferenciar entre contaminantes inertes y aquellos que experimentan transformaciones de

primer orden.

### 3.3 Caracterización Meteorológica

Lo que busca la caracterización meteorológica es realizar una descripción cualitativa de la situación

meteorológica y topográfica del lugar. De acuerdo a los lineamientos indicados en la Guía de Uso de

modelos, el estudio de los procesos desde la mesoescala hasta la escala sinóptica, y cómo éstos

influyen en los procesos de transporte, dispersión y transformación de contaminantes a distintas

escalas temporales es lo óptimo para poder incluir opciones con menor propagación de error en la

estimación de las concentraciones. Se utilizó meteorología modelada por el modelo meteorológico

WRF e ingresada en modelo CALPUFF.

Los datos Meteorológicos observados, fueron tomados desde Estación Meteorológica, Estación La

Unión, administrada por el Ministerio de Medio Ambiente

El análisis se realizó para el periodo comprendido entre enero de 2022 a diciembre de 2022, para

la Estación La Unión. La siguiente imagen, muestra la ubicación de la estación meteorológica

considerada en el análisis:

Imagen 1 **Localización Estación Meteorológica Superficial**

|Nombre Estación|La Unión|
|---|---|
|**Coordenada Este**|663446.00 E|
|**Coordenada Norte**|5538659.00 N|

Fuente: Elaboración desde Google Earth a partir de SINCA.

_**www.modelacionesatmosfericas.cl**_
8

**Modelación de Estimaciones Atmosféricas**

**“DIA PARQUE SOLAR BURGOS”**

**3.3.1** **Análisis Meteorología Observacional**

La información meteorológica de la Estación La Unión, incluye antecedentes del periodo 2022,

abarcando desde Enero a Diciembre 2022, en forma horaria.

_**3.3.1.1**_ _**Rosa de los Vientos**_

El análisis del comportamiento de los vientos observados en la Estación La Unión, se presenta a

continuación para los meses de Enero a Diciembre de 2022. Este análisis se realizó con el fin de

comprender la distribución de velocidades y la frecuencia de ocurrencia de las diferentes

direcciones de viento. De la rosa anual es posible observar que el viento sopla desde el norte,

Imagen 2 Serie de tiempo Dirección de Viento (soplando desde) observadas en las Estación La

Unión, año 2022

_**www.modelacionesatmosfericas.cl**_
9

**Modelación de Estimaciones Atmosféricas**

**“DIA PARQUE SOLAR BURGOS”**

Imagen 3 Serie de tiempo Dirección de Viento (soplando desde) observadas en las Estación La

Unión, Enero-Marzo 2022

Imagen 4 Serie de tiempo Dirección de Viento (soplando desde) observadas en las Estación La

Unión, Abril-Junio 2022

_**www.modelacionesatmosfericas.cl**_
10

**Modelación de Estimaciones Atmosféricas**

**“DIA PARQUE SOLAR BURGOS”**

Imagen 5 Serie de tiempo Dirección de Viento (soplando desde) observadas en las Estación La

Unión, Julio-Septiembre 2022

Imagen 6 Serie de tiempo Dirección de Viento (soplando desde) observadas en las Estación La

Unión, Octubre-Diciembre 2022

.

_**www.modelacionesatmosfericas.cl**_
11

**Modelación de Estimaciones Atmosféricas**

**“DIA PARQUE SOLAR BURGOS”**

_**3.3.1.2**_ _**Velocidad de Vientos**_

**Series de Tiempo - Velocidad del Viento**

En esta sección se presentan series de tiempo de Velocidad de Viento observados durante los meses

de Enero a Diciembre del año 2022 en la estación en estudio. Estos gráficos permiten realizar un

análisis cualitativo de los datos en términos de completitud de la serie y periodos faltantes, valores

fuera de rango o fallas técnicas de los equipos.

Como se aprecia en estas figuras, la trayectoria de la serie de velocidad de viento observada durante

los meses analizados no presenta ausencia de registros para los periodos seleccionados para

análisis. En estas figuras es posible observar también, que en la estación de monitoreo se presenta

un comportamiento estacional, con velocidades de viento promedios entre 0,5 m/s y 2,1 m/s en el

registro anual con un casi 90% de los datos observados.

Imagen 7 Serie de tiempo Velocidad de Viento observadas en las Estación La Unión, Enero

Diciembre 2022.

_**www.modelacionesatmosfericas.cl**_
12

**Modelación de Estimaciones Atmosféricas**

**“DIA PARQUE SOLAR BURGOS”**

Imagen 8 Serie de tiempo Velocidad de Viento observadas en las Estación La Unión, Enero-Marzo

2022.

Imagen 9 Serie de tiempo Velocidad de Viento observadas en las Estación La Unión, Abril - Junio

2022

_**www.modelacionesatmosfericas.cl**_
13

**Modelación de Estimaciones Atmosféricas**

**“DIA PARQUE SOLAR BURGOS”**

Imagen 10 Serie de tiempo Velocidad de Viento observadas en las Estación La Unión Julio

Septiembre 2022

Imagen 11 Serie de tiempo Velocidad de Viento observadas en las Estación La Unión, Octubre

Diciembre 2022.

_**www.modelacionesatmosfericas.cl**_
14

**Modelación de Estimaciones Atmosféricas**

**“DIA PARQUE SOLAR BURGOS”**

### 3.4 Modelo Meteorológico

**3.4.1** **Justificación Modelo Meteorológico**

Según lo establecido por la Guía para el uso de Modelos de Calidad del Aire en el SEIA, la selección

del modelo meteorológico utilizado en el presente estudio se realizó fundamentándose en las

condiciones de topografía compleja del área entorno al proyecto. Para esto, la guía recomienda un

modelo que permita simular una meteorología heterogénea.

La meteorología considerada por el modelo WRF correspondiente al período d 1 enero 2022 a 31

diciembre 2022. Esta información fue utilizada en el modelo de calidad de aire CALPUFF.

**3.4.2** **Descripción Modelo Meteorológico**

La configuración de corrida se hizo desde la hora 1 del mes de enero del año 2022 hasta la hora 23

del día 31 de diciembre de 2022. Se configuró para la modelación horaria la zona UTC-4, y el paso

de tiempo es horario con un total de 8760 horas.

El modelo de investigación y pronóstico del tiempo (Weather Research and Forecasting - WRF) es

un sistema de predicción numérico de mesoscala de nueva generación, diseñado para servir

pronósticos operacionales y para estudio de la atmósfera.

|Tabla 1 Características de los Datos del Modelo Meteorológico WRF Usados para la Evaluación del Proyecto|Col2|
|---|---|
|Característica de los Datos del Modelo WRF|Característica de los Datos del Modelo WRF|
|- Periodo<br>- Coordenada Este<br>- Coordenada Norte<br>- Tamaño del Dominio<br>- Resolución<br>- Zona Horaria<br>- Localización|Jan 01, 2022 - Dec 31,<br>660199.00 E<br>5540863.00 S<br>50x50 km<br>1 km<br>-18 - Site Time Zone: UTC - 4<br>- Chile|

Ejemplos de los campos de vientos generados por WRF se presentan en Figura 2, para el año 2022

_**www.modelacionesatmosfericas.cl**_
15

**Modelación de Estimaciones Atmosféricas**

**“DIA PARQUE SOLAR BURGOS”**

Imagen 12 Ejemplo de Campos de Vientos generados por el Modelo WRF en el Dominio

Fuente: Elaboración propia a partir de CALMET

La información meteorológica de la meterología modelada para el periodo 2022, abarcando desde

Enero a Diciembre 2022, se presenta a continuación;

_**www.modelacionesatmosfericas.cl**_
16

**Modelación de Estimaciones Atmosféricas**

**“DIA PARQUE SOLAR BURGOS”**

_**3.4.2.1**_ _**Rosa de los Vientos**_

La meterología anual se presenta en la siguiente rosa de vientos;

Imagen 13 Serie de tiempo Dirección de Viento (soplando desde) modelada (WRF) año

2022.

Imagen 14 Serie de tiempo Dirección de Viento (soplando desde) modelada (WRF)

Enero a Marzo del año 2022.

_**www.modelacionesatmosfericas.cl**_
17

**Modelación de Estimaciones Atmosféricas**

**“DIA PARQUE SOLAR BURGOS”**

Imagen 15 Serie de tiempo Dirección de Viento (soplando desde) modelada (WRF)

Abril a Junio del año 2022.

Imagen Serie de tiempo Dirección de Viento (soplando desde) modelada (WRF)

Julio a Septiembre del año 2022.

_**www.modelacionesatmosfericas.cl**_
18

**Modelación de Estimaciones Atmosféricas**

**“DIA PARQUE SOLAR BURGOS”**

Imagen 16 Serie de tiempo Dirección de Viento (soplando desde) modelada (WRF)

Octubre a Diciembre del año 2022.

Imagen 17 Serie de tiempo Velocidad de Viento modelada (WRF) Año 2022.

_**www.modelacionesatmosfericas.cl**_
19

**Modelación de Estimaciones Atmosféricas**

**“DIA PARQUE SOLAR BURGOS”**

Imagen 18 Serie de tiempo Velocidad de Viento modelada (WRF) Enero a Marzo Año 2022.

Imagen 19 Serie de tiempo Velocidad de Viento modelada (WRF) Abril a Junio Año 2022.

_**www.modelacionesatmosfericas.cl**_
20

**Modelación de Estimaciones Atmosféricas**

**“DIA PARQUE SOLAR BURGOS”**

Imagen 20 Serie de tiempo Velocidad de Viento modelada (WRF) Julio a Septiembre Año 2022.

Imagen 21 Serie de tiempo Velocidad de Viento modelada (WRF) Octubre a Diciembre Año 2022.

_**www.modelacionesatmosfericas.cl**_
21

**Modelación de Estimaciones Atmosféricas**

**“DIA PARQUE SOLAR BURGOS”**

### 3.5 Análisis De Incertidumbre

Para realizar el análisis de incertidumbre se siguieron las recomendaciones que señaladas en la

“Guía para el uso de modelos de calidad del aire en el SEIA” (SEA, 2012). Esta guía, en el acápite 7,

menciona que cualquier modelo representa una aproximación a la realidad y sus resultados tienen

incertidumbres asociadas, las cuales se expresan a través de diferencias entre lo estimado y lo

observado.

La meteorología observada y modelada se evalúa comparando la velocidad de los vientos generados

por el modelo con las observaciones locales, miente la determinación del sesgo, coeficiente de

correlación y el error medio cuadrático.

Las definiciones matemáticas de cada uno de los estadísticos utilizados se presentan a continuación:

"

Sesgo= [1]

N [*(M] [!] [ −O] [!] [)]

!

RMSE=

N

~~2~~ [1]

"

N [*(M] [!] [ −O] [!] [)] [#]

!

N ∑ "!%& O ! M ! −∑ "!%& O ! ∑ "!%& M !
r=

"!%& O !

5(N ∑

# −6∑ "!%& O ! )

# " M
7 (N∑ !%& !

"!%& O !# −6∑ "!%& O ! ) # 7 (N∑ "!%& M !# −(∑ "!%& M ! ) # )

# −(∑ "!%& M ! )

Donde O ! corresponde a las observaciones; M ! corresponde a los valores modelados; e i

corresponde a cada uno de los N valores horarios de las variables analizadas para la estación.

Tabla 2 **: Comparación vientos observados vs modelados (WRF)**

|Estación|Sesgo|RMSE|r|
|---|---|---|---|
|La Unión|1.11|1.95|0.25|

Tanto el sesgo como RMSE indican diferencias entre el modelo y los datos observados de la estación

de monitoreo y un coeficiente de correlación 0 < r < 1, que indica una correlación positiva

directamente proporcional.

Del gráfico anterior, se observa que los registros de la estación meterológica Calabozo de la comuna

de Coronel, presenta un comportamiento similar a los registrados por el archivo WRF.

_**www.modelacionesatmosfericas.cl**_
22

**Modelación de Estimaciones Atmosféricas**

**“DIA PARQUE SOLAR BURGOS”**

### 3.6 Características Del Dominio De Modelación Y Su Entorno

**3.6.1** **Características de Dominio**

El dominio de modelación considerado para el presente proyecto corresponde a una grilla

rectangular de 50 km por 50 km, compuesta por celdas de 1 km por lado. En la imagen 2 se presentan

las características del área correspondiente al dominio de modelación. El dominio elegido abarca el

área de influencia del proyecto para los distintos componentes ambientales que pueden verse

afectados por las emisiones de éste.

El dominio de modelación está definido por la siguiente imagen:

Imagen 22 **Dominio de Modelación**

Fuente: Elaboración propia a partir de CALPUFF

_**www.modelacionesatmosfericas.cl**_
23

**Modelación de Estimaciones Atmosféricas**

**“DIA PARQUE SOLAR BURGOS”**

### 3.7 Datos topográficos y uso de suelo

La topografía de la zona en análisis se obtiene de la Misión de Radar Topográfico del Transbordador

Espacial de la NASA1 (SRTM en inglés), que consiste en un modelo digital de elevación de alta

resolución que describe la altimetría de una zona mediante un conjunto de cotas para una ubicación

dada con una aproximadamente de 90 metros.

En la siguiente imagen se muestran las elevaciones obtenidas del área de influencia.

Imagen 23 Topografía del dominio de modelación

Fuente Elaboración propia a partir de CALPUFF

Los tipos de suelo presentes en el dominio son de gran importancia para fines de modelación, ya

que determinan los procesos de transferencia de calor, afectando los balances de energía

superficial, elemento fundamental para poder estimar la altura de mezclado en los distintos

períodos en evaluación. Además de esto, tienen efecto en el viento a nivel de superficie, ya que

según el tipo de cobertura que se tenga, la resistencia que se ejerce sobre las corrientes de aire.

_**www.modelacionesatmosfericas.cl**_
24

**Modelación de Estimaciones Atmosféricas**

**“DIA PARQUE SOLAR BURGOS”**

### 3.8 Fuentes De Emisión

En la Tabla a continuación se presentan los resultados de las emisiones para las distintas Fases de

del proyecto.

Tabla 3 Total emisiones por fase del Proyecto

|Fase|MP (Ton/año|MP10<br>(Ton/año)|MP2.5<br>(Ton/año)|NOx<br>(Ton/año)|CO<br>(Ton/año)|Sox<br>(Ton/año)|
|---|---|---|---|---|---|---|
|**Construcción**|1.17|0.33|0.11|0.58|0.00442|3.63E-04|
|**Operación**|0.03|0.01|0.0009|0.0003|0.00036|4.29E-07|
|**Cierre**|1.32|0.35|0.12|0.62|0.00534|3.87E-04|

### 3.9 Receptores

La ubicación de los receptores se considera una grilla de receptores de 50 km x 50 km con

equispaciado de 1 km entre celdas.

Imagen 24 Emplazamiento Grilla de Receptores

Fuente: Elaboración propia a partir de GoogleEarth

_**www.modelacionesatmosfericas.cl**_
25

**Modelación de Estimaciones Atmosféricas**

**“DIA PARQUE SOLAR BURGOS”**

Imagen 25 Emplazamiento Receptores Discretos

Fuente: Elaboración propia a partir de GoogleEarth

_**www.modelacionesatmosfericas.cl**_
26

**Modelación de Estimaciones Atmosféricas**

**“DIA PARQUE SOLAR BURGOS”**

### 3.10 Análisis y Caracterización de Calidad de Aire de la zona del proyecto

Para establecer la situación basal de la calidad de aire del área de influencia del Proyecto se procede

a la toma de datos correspondiente a la estación más cercana al proyecto, denominada estación de

monitoreo de calidad de aire “Estación La Unión”, emplazada a 5 kilómetros al sureste del proyecto,

para el período comprendido entre Enero de 2022 y Diciembre de 2022.

Imagen 26 Ubicación Estación de Monitoreo Calidad de Aire

Tabla 4 Concentración (ug/m3) promedio de contaminantes en EMRP durante el año 2020

|MP10 (ug/m3)<br>concentración<br>promedio 24 hrs|MP2.5 (ug/m3)<br>concentración<br>promedio 24 hrs|NOx (ug/m3)<br>concentración<br>promedio 24 hrs|CO(ug/m3)<br>concentración<br>promedio 1 hr|
|---|---|---|---|
|**s.i**|**27,04**|**si**|**si**|

Fuente: Registro Estación La Unión

_**www.modelacionesatmosfericas.cl**_
27

**Modelación de Estimaciones Atmosféricas**

**“DIA PARQUE SOLAR BURGOS”**

## 4. RESULTADOS MODELACIÓN CALIDAD DEL AIRE

En la siguiente sección se entregan las concentraciones obtenidas utilizando el modelo

meteorológico de meso escala Weather Research Forecasting Model (WRF), como insumo para

CALPUFF View. De esta forma fue posible obtener las concentraciones de Material Particulado y

gases de combustión en cada receptor según Escenario evaluado (Fase de Construcción, Operación

y Abandono).

En base a los resultados de la modelación a continuación se presentan las concentraciones de los

contaminantes de MP10, MP2.5, CO, NOx y Sox por receptores evaluados, según periodos versus el

valor norma de calidad primaria. Junto a ello, el valor de la línea base de calidad de aire en área de

influencia.

De los resultados presentados más adelante, se indica que el proyecto no genera riesgo a la salud

de la población, toda vez que las concentraciones MP10, MP2.5, NOx, SOx y CO proyectadas por el

modelo no generarían eventos de latencia y/o saturación para los compuestos estudiados.

Preliminarmente presentamos la Normativa aplicable al proyecto, relativa a las Normas de Calidad

Primaria consideradas para la evaluación del riesgo sobre la salud de la población identificada.

Las concentraciones modeladas, se comparan con los valores entregados por las normas primarias

de calidad del aire vigentes para los contaminantes estudiados. Los umbrales de las normas citadas

se presentan en la siguiente tabla.

Tabla 5 **Normativa aplicable**

|Normativa|Límite Norma|Concentración|
|---|---|---|
|- DS 104/2018 del MMA, norma primaria de calidad del aire para SO2,; <br>|60 ug/m3N <br>|Anual <br>|
|- DS 104/2018 del MMA, norma primaria de calidad del aire para SO2,; <br>|150 ug/m3N <br>|Diaria <br>|
|- DS 104/2018 del MMA, norma primaria de calidad del aire para SO2,; <br>|350 ug/m3N <br>|Horaria <br>|
|- DS 104/2018 del MMA, norma secundaria de calidad del aire para SO2,; <br>|60 ug/m3N <br>|Anual <br>|
|- DS 104/2018 del MMA, norma secundaria de calidad del aire para SO2,; <br>|260 ug/m3N <br>|Diaria <br>|
|- DS 104/2018 del MMA, norma secundaria de calidad del aire para SO2,; <br>|700 ug/m3N <br>|Horaria <br>|
|- DS 114/2002 del MINSEGPRES, norma primaria de calidad del aire para NO2; <br>|~~400 ug/m3N ~~<br>|~~1 hora ~~<br>|
|- DS 114/2002 del MINSEGPRES, norma primaria de calidad del aire para NO2; <br>|100 ug/m3N <br>|Anual <br>|
|- DS 115/2002 del MINSEGPRES, norma primaria de calidad del aire para CO; <br>|10 mg/m3N <br>|8 horas <br>|
|- DS 115/2002 del MINSEGPRES, norma primaria de calidad del aire para CO; <br>|30 mg/m3N <br>|1 hora <br>|
|- DS 12/2010 del MMA, norma primaria de calidad del aire paraMP2,5 <br>|50 ug/m3N <br>|Diaria <br>|
|- DS 12/2010 del MMA, norma primaria de calidad del aire paraMP2,5 <br>|20 ug/m3N <br>|Anual <br>|
|- DS 59/1998 del MINSEGPRES, norma primaria de calidad del aire para MP10;|150 ug/m3N <br>|Diaria <br>|
|- DS 59/1998 del MINSEGPRES, norma primaria de calidad del aire para MP10;|50 ug/m3N|Anual|

Fuente: Elaboración propia

Del análisis presentado en los siguientes ítems, como se señala anteriormente, se descarta en todos

los receptores evaluados el riesgo sobre la salud de la población, esto considerando las

concentraciones finales proyectadas.

_**www.modelacionesatmosfericas.cl**_
28

**Modelación de Estimaciones Atmosféricas**

**“DIA PARQUE SOLAR BURGOS”**

### 4.1 Determinación Área de Influencia

De acuerdo a los resultados obtenidos, **el proyecto no genera riesgo a la salud de la población para**

**las fases de construcción, operación y cierre del proyecto**, toda vez que **las concentraciones MP10,**

**MP2.5, NOx, SOx y CO proyectadas por el modelo no generarían eventos de latencia y/o**

**saturación** para los compuestos estudiados.

En base a lo antes indicado, y según lo establecido en la Guía "Determinación Y Descripción General
Del Área De Influencia" [1], y a lo definido en su criterio 15, el área de influencia para el elemento Aire

comprende el espacio desde donde se generan dichas emisiones (fuente de la emisión) más el

comprendido por la dispersión de contaminantes emitidos.

De acuerdo a lo antes señalado, el área de influencia para el elemento aire, corresponde a la

dispersión del Material Particulado 10, según la siguiente gráfica;

Imagen 27 **Área de Influencia Componente Aire y Salud de la Población**

Elaboración propia

1

https://www.sea.gob.cl/sites/default/files/imce/archivos/2017/05/03/guia_area_de_influencia_ajuste_10.p

df

_**www.modelacionesatmosfericas.cl**_
29

**Modelación de Estimaciones Atmosféricas**

**“DIA PARQUE SOLAR BURGOS”**

**4.1.1** **Concentración Material Particulado 10**

El flujo de emisiones se concentra en la zona inmediata al proyecto, desplazándose la pluma de

dispersión hacia el sector noreste, observándose una concentración máxima diaria en el receptor

N°7 con un valor de 1.41ug/m3 en la fase de construcción y cierre, que no supera el valor límite

establecido.

Las coordenadas y concentraciones en períodos de concentración anual y diaria de receptores

discretos se presenta en la siguiente tabla.

Tabla 6 **Concentración MP10** **en Receptores Discretos**

|Fase Construcción Concentración Diaria|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|PM10|**N°**|**Coordenadas Receptor**|**Coordenadas Receptor**|**Valor**<br>**Fondo**|**Aporte**<br>**Proyecto**<br>**24 hrs**|**Total**<br>**(Concentración**<br>**final (situación**<br>**basal más**<br>**aporte**<br>**proyecto)**|**Normativa**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**final**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**aporte del**<br>**proyecto**|
|PM10|**N°**|**NLAT_WGS84**|**ELON_WGS84**|**ug/m3**|**ug/m3**|**ug/m3**|**ug/m3**|**% **|**% **|
|PM10|1|-40.27159|-73.118011||0.68|0.68|150|0.45|0.45|
|PM10|2|-40.269632|-73.115445||0.76|0.76|150|0.50|0.50|
|PM10|3|-40.269632|-73.11445||0.67|0.67|150|0.44|0.44|
|PM10|4|-40.262679|-73.111779||0.58|0.58|150|0.39|0.39|
|PM10|5|-40.264237|-73.124765||0.23|0.23|150|0.15|0.15|
|PM10|6|-40.260482|-73.1078||0.31|0.31|150|0.20|0.20|
|PM10|7|-40.265796|-73.114816||1.41|1.41|150|0.94|0.94|
|PM10|8|-40.272394|-73.112981||0.42|0.42|150|0.28|0.28|
|PM10|9|-40.2724|-73.112407||0.32|0.32|150|0.21|0.21|
|**Fase Operación Concentración Diaria**|**Fase Operación Concentración Diaria**|**Fase Operación Concentración Diaria**|**Fase Operación Concentración Diaria**|**Fase Operación Concentración Diaria**|**Fase Operación Concentración Diaria**|**Fase Operación Concentración Diaria**|**Fase Operación Concentración Diaria**|**Fase Operación Concentración Diaria**|**Fase Operación Concentración Diaria**|
|PM10|**N°**|**Coordenadas Receptor**|**Coordenadas Receptor**|**Valor**<br>**Fondo**|**Aporte**<br>**Proyecto**<br>**24 hrs**|**Total**<br>**(Concentración**<br>**final (situación**<br>**basal más**<br>**aporte**<br>**proyecto)**|**Normativa**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**final**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**aporte del**<br>**proyecto**|
|PM10|**N°**|**NLAT_WGS84**|**ELON_WGS84**|**ug/m3**|**ug/m3**|**ug/m3**|**ug/m3**|**% **|**% **|
|PM10|**1 **|-40.27159|-73.118011||2.03E-02|2.03E-02|150|0.01|0.01|
|PM10|2|-40.269632|-73.115445||2.27E-02|2.27E-02|150|0.02|0.02|
|PM10|3|-40.269632|-73.11445||2.00E-02|2.00E-02|150|0.01|0.01|
|PM10|4|-40.262679|-73.111779||1.75E-02|1.75E-02|150|0.01|0.01|
|PM10|5|-40.264237|-73.124765||6.95E-03|6.95E-03|150|0.00|0.00|
|PM10|6|-40.260482|-73.1078||9.22E-03<br>|9.22E-03<br>|150|0.01<br>|0.01<br>|
|PM10|7|-40.265796|-73.114816||~~4.24E-02~~|~~4.24E-02~~|150|~~0.03~~|~~0.03~~|
|PM10|8|-40.272394|-73.112981||1.27E-02|1.27E-02|150|0.01|0.01|
|PM10|9|-40.2724|-73.112407||9.58E-03|9.58E-03|150|0.01|0.01|
|**Fase Abandono Concentración Diaria**|**Fase Abandono Concentración Diaria**|**Fase Abandono Concentración Diaria**|**Fase Abandono Concentración Diaria**|**Fase Abandono Concentración Diaria**|**Fase Abandono Concentración Diaria**|**Fase Abandono Concentración Diaria**|**Fase Abandono Concentración Diaria**|**Fase Abandono Concentración Diaria**|**Fase Abandono Concentración Diaria**|
|PM10|**N°**|**Coordenadas Receptor**|**Coordenadas Receptor**|**Valor**<br>**Fondo**|**Aporte**<br>**Proyecto**<br>**24 hrs**|**Total**<br>**(Concentración**<br>**final (situación**<br>**basal más**<br>**aporte**<br>**proyecto)**|**Normativa**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**final**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**aporte del**<br>**proyecto**|
|PM10|**N°**|**NLAT_WGS84**|**ELON_WGS84**|ug/m3|ug/m3|ug/m3|ug/m3|**% **|**% **|
|PM10|1|-40.27159|-73.118011||6.76E-01|6.76E-01|150|0.45|0.45|
|PM10|2|-40.269632|-73.115445||7.57E-01|7.57E-01<br>|150|0.50<br>|0.50<br>|
|PM10|3|-40.269632|-73.11445||6.66E-01|~~6.66E-01~~|150|~~0.44~~|~~0.44~~|

_**www.modelacionesatmosfericas.cl**_
30

**Modelación de Estimaciones Atmosféricas**

**“DIA PARQUE SOLAR BURGOS”**

|Col1|4|-40.262679|-73.111779|Col5|5.84E-01|5.84E-01|150|0.39|0.39|
|---|---|---|---|---|---|---|---|---|---|
||5|-40.264237|-73.124765||2.32E-01|2.32E-01<br>|150|0.15<br>|0.15<br>|
||6|-40.260482|-73.1078||3.07E-01|~~3.07E-01~~|150|~~0.20~~|~~0.20~~|
||7|-40.265796|-73.114816||1.41E+00|1.41E+00|150|0.94|0.94|
||8|-40.272394|-73.112981||0.42193|4.22E-01|150|0.28|0.28|
||9|-40.2724|-73.112407||0.31931|3.19E-01|150|0.21|0.21|

|Fase Construcción Concentración Anual|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|PM10|**N°**|**Coordenadas Receptor**|**Coordenadas Receptor**|**Valor**<br>**Fondo**|**Aporte**<br>**Proyecto**<br>**Anual**|**Total**<br>**(Concentración**<br>**final (situación**<br>**basal más**<br>**aporte**<br>**proyecto)**|**Normativa**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**final**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**aporte del**<br>**proyecto**|
|PM10|**N°**|**NLAT_WGS84**|**ELON_WGS84**|** ug/m3**|**ug/m3**|**ug/m3**|**ug/m3**|**% **|**% **|
|PM10|1|-40.27159|-73.118011||0.09|0.09|50|0.18|0.18|
|PM10|2|-40.269632|-73.115445||0.13|0.13|50|0.26|0.26|
|PM10|3|-40.269632|-73.11445||0.11|0.11|50|0.21|0.21|
|PM10|4|-40.262679|-73.111779||0.12|0.12|50|0.23|0.23|
|PM10|5|-40.264237|-73.124765||0.03|0.03|50|0.05|0.05|
|PM10|6|-40.260482|-73.1078||0.06|0.06|50|0.11|0.11|
|PM10|7|-40.265796|-73.114816||0.37|0.37|50|0.73|0.73|
|PM10|8|-40.272394|-73.112981||0.05|0.05|50|0.11|0.11|
|PM10|9|-40.2724|-73.112407||0.05|0.05|50|0.09|0.09|
|**Fase Operación Concentración Anual**|**Fase Operación Concentración Anual**|**Fase Operación Concentración Anual**|**Fase Operación Concentración Anual**|**Fase Operación Concentración Anual**|**Fase Operación Concentración Anual**|**Fase Operación Concentración Anual**|**Fase Operación Concentración Anual**|**Fase Operación Concentración Anual**|**Fase Operación Concentración Anual**|
|PM10|**N°**|**Coordenadas Receptor**|**Coordenadas Receptor**|**Valor**<br>**Fondo**|**Aporte**<br>**Proyecto**<br>**Anual**|**Total**<br>**(Concentración**<br>**final (situación**<br>**basal más**<br>**aporte**<br>**proyecto)**|**Normativa**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**final**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**aporte del**<br>**proyecto**|
|PM10|**N°**|**NLAT_WGS84**|**ELON_WGS84**|** ug/m3**|**ug/m3**|**ug/m3**|**ug/m3**|**% **|**% **|
|PM10|**1 **|-40.27159|-73.118011||0.003|0.003|50|**0.01**|0.01|
|PM10|2|-40.269632|-73.115445||0.004|0.004|50|**0.01**|0.01|
|PM10|3|-40.269632|-73.11445||0.003|0.003|50|**0.01**|0.01|
|PM10|4|-40.262679|-73.111779||0.003|0.003|50|**0.01**|0.01|
|PM10|5|-40.264237|-73.124765||0.001|0.001|50|**0.00**|0.00|
|PM10|6|-40.260482|-73.1078||0.002|0.002<br>|50|**0.00**<br>|0.00|
|PM10|7|-40.265796|-73.114816||0.011|~~0.011~~|50|~~**0.02**~~|0.02|
|PM10|8|-40.272394|-73.112981||0.002|0.002|50|**0.00**|0.00|
|PM10|9|-40.2724|-73.112407||0.001|0.001|50|**0.00**|0.00|
|**Fase Abandono Concentración Anual**|**Fase Abandono Concentración Anual**|**Fase Abandono Concentración Anual**|**Fase Abandono Concentración Anual**|**Fase Abandono Concentración Anual**|**Fase Abandono Concentración Anual**|**Fase Abandono Concentración Anual**|**Fase Abandono Concentración Anual**|**Fase Abandono Concentración Anual**|**Fase Abandono Concentración Anual**|
|PM10|**N°**|**Coordenadas Receptor**|**Coordenadas Receptor**|**Valor**<br>**Fondo**|**Aporte**<br>**Proyecto**<br>**Anual**|**Total**<br>**(Concentración**<br>**final (situación**<br>**basal más**<br>**aporte**<br>**proyecto)**|**Normativa**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**final**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**aporte del**<br>**proyecto**|
|PM10|**N°**|**NLAT_WGS84**|**ELON_WGS84**|** ug/m3**|**ug/m3**|**ug/m3**|**ug/m3**|**% **|**% **|
|PM10|1|-40.27159|-73.118011||0.09|0.09|50.00|0.18|0.18|
|PM10|2|-40.269632|-73.115445||0.13|0.13|50.00|0.26|0.26|
|PM10|3|-40.269632|-73.11445||0.11|0.11|50.00|0.21|0.21|
|PM10|4|-40.262679|-73.111779||0.12|0.12|50.00|0.23|0.23|
|PM10|5|-40.264237|-73.124765||0.03|0.03|50.00|0.05|0.05|
|PM10|6|-40.260482|-73.1078||0.06|0.06|50.00|0.11|0.11|
|PM10|7|-40.265796|-73.114816||0.37|0.37|50.00|0.73|0.73|
|PM10|8|-40.272394|-73.112981||0.05|0.05|50.00|0.11|0.11|
|PM10|9|-40.2724|-73.112407||0.05|0.05|50.00|0.09|0.09|

_**www.modelacionesatmosfericas.cl**_
31

**Modelación de Estimaciones Atmosféricas**

**“DIA PARQUE SOLAR BURGOS”**

Como se observa en la tabla aquí indicada, los receptores evaluados, poseen concentraciones muy

por debajo del límite establecido en la norma de calidad primaria; 150 ug/m3N para la concentración

diaria y 50 ug/m3N para la concentración anual, respectivamente, por tanto, es posible señalar que

el proyecto no aporta significativamente sobre la calidad de aire del área de influencia toda vez que

sus concentraciones son despreciables.

Para mayor comprensión a continuación en Anexo N°1 se presentan imágenes de pluma de

dispersión representada por isoconcentraciones que reflejan el resultado de la modelación.

**4.1.2** **Concentración Material Particulado 2.5**

El flujo de emisiones se concentra en la zona inmediata al proyecto, desplazándose la pluma de

dispersión hacia el sector noreste, observándose una concentración máxima diaria en el receptor

N°7 con un valor de 0.56 ug/m3 en la fase de Cierre en concentración diaria, que sumado la situación

basal alcanza los 55.21 ug/m3. No superando el valor límite establecido en normativa.

Las coordenadas y concentraciones en períodos de concentración anual y diaria de receptores

discretos se presenta en la siguiente tabla.

Tabla 7 **Concentración MP2.5** **en Receptores Discretos**

|Fase Construcción Concentración Diaria|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|PM2.5|**N°**|**Coordenadas Receptor**|**Coordenadas Receptor**|**Valor**<br>**Fondo**|**Aporte**<br>**Proyecto**<br>**24 hrs**|**Total**<br>**(Concentración**<br>**final (situación**<br>**basal más**<br>**aporte**<br>**proyecto)**|**Normativa**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**final**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**aporte del**<br>**proyecto**|
|PM2.5|**N°**|**NLAT_WGS84**|**ELON_WGS84**|** ug/m3**|**ug/m3**|**ug/m3**|**ug/m3**|**% **|**% **|
|PM2.5|1|-40.27159|-73.118011|27.04|0.20|27.24|50|54.49|0.41|
|PM2.5|2|-40.269632|-73.115445|27.04|0.23|27.27|50|54.53|0.45|
|PM2.5|3|-40.269632|-73.11445|27.04|0.20|27.24|50|54.48|0.40|
|PM2.5|4|-40.262679|-73.111779|27.04|0.18|27.22|50|54.43|0.35|
|PM2.5|5|-40.264237|-73.124765|27.04|0.07|27.11|50|54.22|0.14|
|PM2.5|6|-40.260482|-73.1078|27.04|0.09|27.13|50|54.26|0.18|
|PM2.5|7|-40.265796|-73.114816|27.04|0.42|27.46|50|54.93|0.85|
|PM2.5|8|-40.272394|-73.112981|27.04|0.13|27.17|50|54.33|0.25|
|PM2.5|9|-40.2724|-73.112407|27.04|0.10|27.14|50|54.27|0.19|
|**Fase Operación Concentración Diaria**|**Fase Operación Concentración Diaria**|**Fase Operación Concentración Diaria**|**Fase Operación Concentración Diaria**|**Fase Operación Concentración Diaria**|**Fase Operación Concentración Diaria**|**Fase Operación Concentración Diaria**|**Fase Operación Concentración Diaria**|**Fase Operación Concentración Diaria**|**Fase Operación Concentración Diaria**|
|PM2.5|**N°**|**Coordenadas Receptor**|**Coordenadas Receptor**|**Valor**<br>**Fondo**|**Aporte**<br>**Proyecto**<br>**24 hrs**|**Total**<br>**(Concentración**<br>**final (situación**<br>**basal más**<br>**aporte**<br>**proyecto)**|**Normativa**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**final**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**aporte del**<br>**proyecto**|
|PM2.5|**N°**|**NLAT_WGS84**|**ELON_WGS84**|** ug/m3**|**ug/m3**|**ug/m3**|**ug/m3**|**% **|**% **|
|PM2.5|**1 **|-40.27159|-73.118011|27.04|0.002|27.04<br>|50<br>|54.08<br>|0.00|
|PM2.5|2|-40.269632|-73.115445|27.04|0.002|~~27.04~~|~~50~~|~~54.08~~|0.00|
|PM2.5|3|-40.269632|-73.11445|27.04|0.002|27.04|50|54.08|0.00|
|PM2.5|4|-40.262679|-73.111779|27.04|0.002|27.04|50|54.08|0.00|
|PM2.5|5|-40.264237|-73.124765|27.04|0.001|27.04|50|54.08|0.00|
|PM2.5|6|-40.260482|-73.1078|27.04|0.001|27.04|50|54.08|0.00|

_**www.modelacionesatmosfericas.cl**_
32

**Modelación de Estimaciones Atmosféricas**

**“DIA PARQUE SOLAR BURGOS”**

|Col1|7|-40.265796|-73.114816|27.04|0.004|27.04|50|54.09|0.01|
|---|---|---|---|---|---|---|---|---|---|
||8|-40.272394|-73.112981|27.04|0.001|27.04<br>|50<br>|54.08<br>|0.00|
||9|-40.2724|-73.112407|27.04|0.001|~~27.04~~|~~50~~|~~54.08~~|0.00|
|**Fase Abandono Concentración Diaria**|**Fase Abandono Concentración Diaria**|**Fase Abandono Concentración Diaria**|**Fase Abandono Concentración Diaria**|**Fase Abandono Concentración Diaria**|**Fase Abandono Concentración Diaria**|**Fase Abandono Concentración Diaria**|**Fase Abandono Concentración Diaria**|**Fase Abandono Concentración Diaria**|**Fase Abandono Concentración Diaria**|
|PM2.5|**N°**|**Coordenadas Receptor**|**Coordenadas Receptor**|**Valor**<br>**Fondo**|**Aporte**<br>**Proyecto**<br>**24 hrs**|**Total**<br>**(Concentración**<br>**final (situación**<br>**basal más**<br>**aporte**<br>**proyecto)**|**Normativa**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**final**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**aporte del**<br>**proyecto**|
|PM2.5|**N°**|**NLAT_WGS84**|**ELON_WGS84**|** ug/m3**|**ug/m3**|**ug/m3**|**ug/m3**|**% **|**% **|
|PM2.5|1|-40.27159|-73.118011|27.04|0.27|27.31|50|54.62|0.54|
|PM2.5|2|-40.269632|-73.115445|27.04|0.30|27.34|50|54.69|0.61|
|PM2.5|3|-40.269632|-73.11445|27.04|0.27|27.31|50|54.61|0.53|
|PM2.5|4|-40.262679|-73.111779|27.04|0.23|27.27|50|54.55|0.47|
|PM2.5|5|-40.264237|-73.124765|27.04|0.09|27.13|50|54.27|0.19|
|PM2.5|6|-40.260482|-73.1078|27.04|0.12|27.16|50|54.33|0.25|
|PM2.5|7|-40.265796|-73.114816|27.04|0.56|27.60|50|55.21|1.13|
|PM2.5|8|-40.272394|-73.112981|27.04|0.17|27.21|50|54.42|0.34|
|PM2.5|9|-40.2724|-73.112407|27.04|0.13|27.17|50|54.34|0.26|

|Fase Construcción Concentración Anual|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|PM2.5|**N°**|**Coordenadas Receptor**|**Coordenadas Receptor**|**Valor**<br>**Fondo**|**Aporte**<br>**Proyecto**<br>**Anual**|**Total**<br>**(Concentración**<br>**final (situación**<br>**basal más**<br>**aporte**<br>**proyecto)**|**Normativa**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**final**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**aporte del**<br>**proyecto**|
|PM2.5|**N°**|**NLAT_WGS84**|**ELON_WGS84**|** ug/m3**|**ug/m3**|**ug/m3**|**ug/m3**|**% **|**% **|
|PM2.5|1|-40.27159|-73.118011||0.03|0.03|20|0.14|0.14|
|PM2.5|2|-40.269632|-73.115445||0.04|0.04|20|0.19|0.19|
|PM2.5|3|-40.269632|-73.11445||0.03|0.03|20|0.16|0.16|
|PM2.5|4|-40.262679|-73.111779||0.03|0.03|20|0.17|0.17|
|PM2.5|5|-40.264237|-73.124765||0.01|0.01|20|0.04|0.04|
|PM2.5|6|-40.260482|-73.1078||0.02|0.02|20|0.08|0.08|
|PM2.5|7|-40.265796|-73.114816||0.11|0.11|20|0.55|0.55|
|PM2.5|8|-40.272394|-73.112981||0.02|0.02|20|0.08|0.08|
|PM2.5|9|-40.2724|-73.112407||0.01|0.01|20|0.07|0.07|
|**Fase Operación Concentración Anual**|**Fase Operación Concentración Anual**|**Fase Operación Concentración Anual**|**Fase Operación Concentración Anual**|**Fase Operación Concentración Anual**|**Fase Operación Concentración Anual**|**Fase Operación Concentración Anual**|**Fase Operación Concentración Anual**|**Fase Operación Concentración Anual**|**Fase Operación Concentración Anual**|
|PM2.5|**N°**|**Coordenadas Receptor**|**Coordenadas Receptor**|**Valor**<br>**Fondo**|**Aporte**<br>**Proyecto**<br>**Anual**|**Total**<br>**(Concentración**<br>**final (situación**<br>**basal más**<br>**aporte**<br>**proyecto)**|**Normativa**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**final**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**aporte del**<br>**proyecto**|
|PM2.5|**N°**|**NLAT_WGS84**|**ELON_WGS84**|** ug/m3**|**ug/m3**|**ug/m3**|**ug/m3**|**% **|**% **|
|PM2.5|**1 **|-40.27159|-73.118011||3.E-04|3.E-04|20|0.01|0.00|
|PM2.5|2|-40.269632|-73.115445||4.E-04|4.E-04|20|0.02|0.00|
|PM2.5|3|-40.269632|-73.11445||3.E-04|3.E-04|20|0.02|0.00|
|PM2.5|4|-40.262679|-73.111779||3.E-04|3.E-04<br>|20<br>|0.02|0.00|
|PM2.5|5|-40.264237|-73.124765||8.E-05|~~8.E-05~~|~~20~~|0.00|0.00|
|PM2.5|6|-40.260482|-73.1078||2.E-04|2.E-04|20|0.01|0.00|
|PM2.5|7|-40.265796|-73.114816||1.E-03|1.E-03|20|0.05|0.01|
|PM2.5|8|-40.272394|-73.112981||2.E-04|2.E-04|20|0.01|0.00|
|PM2.5|9|-40.2724|-73.112407||1.E-04|1.E-04|20|0.01|0.00|
|**Fase Abandono Concentración Anual**|**Fase Abandono Concentración Anual**|**Fase Abandono Concentración Anual**|**Fase Abandono Concentración Anual**|**Fase Abandono Concentración Anual**|**Fase Abandono Concentración Anual**|**Fase Abandono Concentración Anual**|**Fase Abandono Concentración Anual**|**Fase Abandono Concentración Anual**|**Fase Abandono Concentración Anual**|
|PM2.5|**N°**|**Coordenadas Receptor**|**Coordenadas Receptor**|**Valor**<br>**Fondo**|**Aporte**<br>**Proyecto**<br>**Anual**|**Total**<br>**(Concentración**<br>**final (situación**<br>**basal más**|**Normativa**|**Porcentaje de**<br>**la Norma en**<br>**base a**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**|

_**www.modelacionesatmosfericas.cl**_
33

**Modelación de Estimaciones Atmosféricas**

**“DIA PARQUE SOLAR BURGOS”**

|Col1|Col2|Col3|Col4|Col5|Col6|aporte<br>proyecto)|Col8|concentración<br>final|aporte del<br>proyecto|
|---|---|---|---|---|---|---|---|---|---|
|||**NLAT_WGS84**|**ELON_WGS84**|** ug/m3**|**ug/m3**|**ug/m3**|**ug/m3**|**% **|**% **|
||1|-40.27159|-73.118011||3.69E-02|3.69E-02|20|0.18|0.18|
||2|-40.269632|-73.115445||5.16E-02|5.16E-02|20|0.26|0.26|
||3|-40.269632|-73.11445||4.28E-02|4.28E-02|20|0.21|0.21|
||4|-40.262679|-73.111779||4.66E-02|4.66E-02|20|0.23|0.23|
||5|-40.264237|-73.124765||1.07E-02|1.07E-02|20|0.05|0.05|
||6|-40.260482|-73.1078||2.24E-02|2.24E-02|20|0.11|0.11|
||7|-40.265796|-73.114816||1.46E-01|1.46E-01|20|0.73|0.73|
||8|-40.272394|-73.112981||2.18E-02|2.18E-02|20|0.11|0.11|
||9|-40.2724|-73.112407||1.89E-02|1.89E-02|20|0.09|0.09|

Como se observa en la tabla aquí indicada, los receptores evaluados, poseen concentraciones muy

por debajo del límite establecido en la norma de calidad primaria; 50 ug/m3N para la concentración

diaria y 20 ug/m3N para la concentración anual, respectivamente, por tanto, es posible señalar que

el proyecto no aporta significativamente sobre la calidad de aire del área de influencia toda vez que

sus concentraciones son despreciables.

Para mayor comprensión en Anexo N°1 se presentan imágenes de la pluma de dispersión

representada por isoconcentraciones que reflejan el resultado de la modelación.

_**www.modelacionesatmosfericas.cl**_
34

**Modelación de Estimaciones Atmosféricas**

**“DIA PARQUE SOLAR BURGOS”**

**4.1.3** **Concentración NOx**

El flujo de emisiones se concentra en la zona inmediata al proyecto, desplazándose la pluma de

dispersión hacia el sector noreste, observándose una concentración máxima horaria en el receptor

N°7 con un valor de 11.3 ug/m3 en la fase de Construcción y Cierre en concentración horaria. No

superando el valor límite establecido en normativa.

Las coordenadas y concentraciones en períodos de concentración horaria y anual de receptores

discretos se presenta en la siguiente tabla.

Tabla 8 **Concentración NOx** **en Receptores Discretos**

|Fase Construcción Concentración Horaria|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|NOx|**N°**|**Coordenadas Receptor**|**Coordenadas Receptor**|**Valor**<br>**Fondo**|**Aporte**<br>**Proyecto**<br>**24 hrs**|**Total**<br>**(Concentración**<br>**final (situación**<br>**basal más**<br>**aporte**<br>**proyecto)**|**Normativa**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**final**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**aporte del**<br>**proyecto**|
|NOx|**N°**|**NLAT_WGS84**|**ELON_WGS84**|** ug/m3**|**ug/m3**|**ug/m3**|**ug/m3**|**% **|**% **|
|NOx|1|-40.27159|-73.118011||4.05|4.05|400|1.01|1.01|
|NOx|2|-40.269632|-73.115445||4.92|4.92|400|1.23|1.23|
|NOx|3|-40.269632|-73.11445||3.61|3.61|400|0.90|0.90|
|NOx|4|-40.262679|-73.111779||4.65|4.65|400|1.16|1.16|
|NOx|5|-40.264237|-73.124765||0.69|0.69|400|0.17|0.17|
|NOx|6|-40.260482|-73.1078||2.25|2.25|400|0.56|0.56|
|NOx|7|-40.265796|-73.114816||11.30|11.30|400|2.82|2.82|
|NOx|8|-40.272394|-73.112981||1.55|1.55|400|0.39|0.39|
|NOx|9|-40.2724|-73.112407||1.37|1.37|400|0.34|0.34|
|**Fase Operación Concentración Horaria**|**Fase Operación Concentración Horaria**|**Fase Operación Concentración Horaria**|**Fase Operación Concentración Horaria**|**Fase Operación Concentración Horaria**|**Fase Operación Concentración Horaria**|**Fase Operación Concentración Horaria**|**Fase Operación Concentración Horaria**|**Fase Operación Concentración Horaria**|**Fase Operación Concentración Horaria**|
|NOx|**N°**|**Coordenadas Receptor**|**Coordenadas Receptor**|**Valor**<br>**Fondo**|**Aporte**<br>**Proyecto**<br>**24 hrs**|**Total**<br>**(Concentración**<br>**final (situación**<br>**basal más**<br>**aporte**<br>**proyecto)**|**Normativa**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**final**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**aporte del**<br>**proyecto**|
|NOx|**N°**|**NLAT_WGS84**|**ELON_WGS84**|** ug/m3**|**ug/m3**|**ug/m3**|**ug/m3**|**% **|**% **|
|NOx|**1 **|-40.27159|-73.118011||2.E-03|2.E-03|400|0.000|0.000|
|NOx|2|-40.269632|-73.115445||2.E-03|2.E-03|400|0.001|0.001|
|NOx|3|-40.269632|-73.11445||2.E-03|2.E-03<br>|400|0.000<br>|0.000|
|NOx|4|-40.262679|-73.111779||2.E-03|~~2.E-03~~|400|~~0.001~~|0.001|
|NOx|5|-40.264237|-73.124765||3.E-04|3.E-04|400|0.000|0.000|
|NOx|6|-40.260482|-73.1078||1.E-03|1.E-03|400|0.000|0.000|
|NOx|7|-40.265796|-73.114816||5.E-03|5.E-03|400|0.001|0.001|
|NOx|8|-40.272394|-73.112981||7.E-04|7.E-04|400|0.000|0.000|
|NOx|9|-40.2724|-73.112407||6.E-04|6.E-04|400|0.000|0.000|
|**Fase Abandono Concentración Horaria**|**Fase Abandono Concentración Horaria**|**Fase Abandono Concentración Horaria**|**Fase Abandono Concentración Horaria**|**Fase Abandono Concentración Horaria**|**Fase Abandono Concentración Horaria**|**Fase Abandono Concentración Horaria**|**Fase Abandono Concentración Horaria**|**Fase Abandono Concentración Horaria**|**Fase Abandono Concentración Horaria**|
|NOx|**N°**|**Coordenadas Receptor**|**Coordenadas Receptor**|**Valor**<br>**Fondo**|**Aporte**<br>**Proyecto**<br>**24 hrs**|**Total**<br>**(Concentración**<br>**final (situación**<br>**basal más**<br>**aporte**<br>**proyecto)**|**Normativa**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**final**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**aporte del**<br>**proyecto**|
|NOx|**N°**|**NLAT_WGS84**|**ELON_WGS84**|** ug/m3**|**ug/m3**|**ug/m3**|**ug/m3**|**% **<br>|**% **<br>|
|NOx|1|-40.27159|-73.118011||4.05|4.046|400|~~1.0~~|~~1.0~~|
|NOx|2|-40.269632|-73.115445||4.92|4.9223|400|1.2|1.2|
|NOx|3|-40.269632|-73.11445||3.61|3.6084|400|0.9|0.9|
|NOx|4|-40.262679|-73.111779||4.65|4.6502|400|1.2|1.2|
|NOx|5|-40.264237|-73.124765||0.69|0.6903|400|0.2|0.2|

_**www.modelacionesatmosfericas.cl**_
35

**Modelación de Estimaciones Atmosféricas**

**“DIA PARQUE SOLAR BURGOS”**

|Col1|6|-40.260482|-73.1078|Col5|2.25|2.2513|400|0.6|0.6|
|---|---|---|---|---|---|---|---|---|---|
||7|-40.265796|-73.114816||11.30|11.299|400|2.8|2.8|
||8|-40.272394|-73.112981||1.55|1.5514|400|0.4|0.4|
||9|-40.2724|-73.112407||1.37|1.3729|400|0.3|0.0|

|Fase Construcción Concentración Anual|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|NOx|**N°**|**Coordenadas Receptor**|**Coordenadas Receptor**|**Valor**<br>**Fondo**|**Aporte**<br>**Proyecto**<br>**Anual**|**Total**<br>**(Concentración**<br>**final (situación**<br>**basal más**<br>**aporte**<br>**proyecto)**|**Normativa**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**final**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**aporte del**<br>**proyecto**|
|NOx|**N°**|**NLAT_WGS84**|**ELON_WGS84**|** ug/m3**|**ug/m3**|**ug/m3**|**ug/m3**|**% **|**% **|
|NOx|1|-40.27159|-73.118011||0.18|0.18|100|0.18|0.18|
|NOx|2|-40.269632|-73.115445||0.26|0.18|100|0.18|0.26|
|NOx|3|-40.269632|-73.11445||0.21|0.18|100|0.18|0.21|
|NOx|4|-40.262679|-73.111779||0.23|0.18|100|0.18|0.23|
|NOx|5|-40.264237|-73.124765||0.05|0.18|100|0.18|0.05|
|NOx|6|-40.260482|-73.1078||0.11|0.18|100|0.18|0.11|
|NOx|7|-40.265796|-73.114816||0.73|0.18|100|0.18|0.73|
|NOx|8|-40.272394|-73.112981||0.11|0.18|100|0.18|0.11|
|NOx|9|-40.2724|-73.112407||0.09|0.18|100|0.18|0.09|
|**Fase Operación Concentración Anual**|**Fase Operación Concentración Anual**|**Fase Operación Concentración Anual**|**Fase Operación Concentración Anual**|**Fase Operación Concentración Anual**|**Fase Operación Concentración Anual**|**Fase Operación Concentración Anual**|**Fase Operación Concentración Anual**|**Fase Operación Concentración Anual**|**Fase Operación Concentración Anual**|
|NOx|**N°**|**Coordenadas Receptor**|**Coordenadas Receptor**|**Valor**<br>**Fondo**|**Aporte**<br>**Proyecto**<br>**Anual**|**Total**<br>**(Concentración**<br>**final (situación**<br>**basal más**<br>**aporte**<br>**proyecto)**|**Normativa**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**final**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**aporte del**<br>**proyecto**|
|NOx|**N°**|**NLAT_WGS84**|**ELON_WGS84**|** ug/m3**|**ug/m3**|**ug/m3**|**ug/m3**|**% **|**% **|
|NOx|**1 **|-40.27159|-73.118011||8.E-05|8.E-05|100|0.0001|0.0001|
|NOx|2|-40.269632|-73.115445||1.E-04|1.E-04|100|0.0001|0.0001|
|NOx|3|-40.269632|-73.11445||1.E-04|1.E-04|100|0.0001|0.0001|
|NOx|4|-40.262679|-73.111779||1.E-04|1.E-04|100|0.0001|0.0001|
|NOx|5|-40.264237|-73.124765||2.E-05|2.E-05|100|0.0000|0.0000|
|NOx|6|-40.260482|-73.1078||5.E-05|5.E-05|100|0.0001<br>|0.0001|
|NOx|7|-40.265796|-73.114816||3.E-04|3.E-04|100|~~0.0003~~|0.0003|
|NOx||-40.272394|-73.112981||5.E-05|5.E-05|101|0.0000|0.0000|
|NOx||-40.2724|-73.112407||4.E-05|4.E-05|102|0.0000|0.0000|
|**Fase Abandono Concentración Anual**|**Fase Abandono Concentración Anual**|**Fase Abandono Concentración Anual**|**Fase Abandono Concentración Anual**|**Fase Abandono Concentración Anual**|**Fase Abandono Concentración Anual**|**Fase Abandono Concentración Anual**|**Fase Abandono Concentración Anual**|**Fase Abandono Concentración Anual**|**Fase Abandono Concentración Anual**|
|NOx|**N°**|**Coordenadas Receptor**|**Coordenadas Receptor**|**Valor**<br>**Fondo**|**Aporte**<br>**Proyecto**<br>**Anual**|**Total**<br>**(Concentración**<br>**final (situación**<br>**basal más**<br>**aporte**<br>**proyecto)**|**Normativa**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**final**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**aporte del**<br>**proyecto**|
|NOx|**N°**|**NLAT_WGS84**|**ELON_WGS84**|** ug/m3**|**ug/m3**|**ug/m3**|**ug/m3**|**% **|**% **|
|NOx|1|-40.27159|-73.118011||0.18|0.18|100|0.18|0.18|
|NOx|2|-40.269632|-73.115445||0.26|0.26|100|0.26|0.26|
|NOx|3|-40.269632|-73.11445||0.21|0.21|100|0.21<br>|0.21<br>|
|NOx|4|-40.262679|-73.111779||0.23|0.23|100|~~0.23~~|~~0.23~~|
|NOx|5|-40.264237|-73.124765||0.05|0.05|100|0.05|0.05|
|NOx|6|-40.260482|-73.1078||0.11|0.11|100|0.11|0.11|
|NOx|7|-40.265796|-73.114816||0.73|0.73|100|0.73|0.73|
|NOx|8|-40.272394|-73.112981||0.11|1.35|100|1.35|0.11|
|NOx|9|-40.2724|-73.112407||0.09|1.97|100|1.97|0.09|

_**www.modelacionesatmosfericas.cl**_
36

**Modelación de Estimaciones Atmosféricas**

**“DIA PARQUE SOLAR BURGOS”**

Como se observa en la tabla aquí indicada, los receptores evaluados, poseen concentraciones muy

por debajo del límite establecido en la norma de calidad primaria; 400 ug/m3N para la concentración

horaria y 100 ug/m3N para la concentración anual, respectivamente, por tanto, es posible señalar

que el proyecto no aporta significativamente sobre la calidad de aire del área de influencia toda vez

que sus concentraciones son despreciables.

Para mayor comprensión a continuación en Anexo N°1 se presentan imágenes según los receptores

evaluados en sus diversos períodos, junto a su pluma de dispersión representada por

isoconcentraciones que reflejan el resultado de la modelación.

**4.1.4** **Concentración CO**

El flujo de emisiones se concentra en la zona inmediata al proyecto, desplazándose la pluma de

dispersión hacia el sector noreste, observándose una concentración máxima diaria en el receptor

N°7 con un valor de 8E-02 ug/m3 en la fase de Construcción en concentración horaria.

Las coordenadas y concentraciones en períodos de concentración horaria y 8 horas de receptores

discretos se presenta en la siguiente tabla.

Tabla 9 **Concentración CO** **en Receptores Discretos**

|Fase Construcción Concentración Horaria|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|CO|**N°**|**Coordenadas Receptor**|**Coordenadas Receptor**|**Valor**<br>**Fondo**|**Aporte**<br>**Proyecto**<br>**Horario**|**Total**<br>**(Concentración**<br>**final (situación**<br>**basal más**<br>**aporte**<br>**proyecto)**|**Normativa**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**final**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**aporte del**<br>**proyecto**|
|CO|**N°**|**NLAT_WGS84**|**ELON_WGS84**|** ug/m3**|**ug/m3**|**ug/m3**|**ug/m3**|**% **|**% **|
|CO|1|-40.27159|-73.118011||3.E-02|3.E-02|30|0.09|0.09|
|CO|2|-40.269632|-73.115445||3.E-02|3.E-02|30|0.11|0.11|
|CO|3|-40.269632|-73.11445||3.E-02|3.E-02|30|0.08|0.08|
|CO|4|-40.262679|-73.111779||3.E-02|3.E-02|30|0.11|0.11|
|CO|5|-40.264237|-73.124765||5.E-03|5.E-03|30|0.02|0.02|
|CO|6|-40.260482|-73.1078||2.E-02|2.E-02|30|0.05|0.05|
|CO|7|-40.265796|-73.114816||8.E-02|8.E-02|30|0.26|0.26|
|CO|8|-40.272394|-73.112981||1.E-02|1.E-02|30|0.04|0.04|
|CO|9|-40.2724|-73.112407||1.E-02|1.E-02|30|0.03|0.03|
|**Fase Operación Concentración Horaria**|**Fase Operación Concentración Horaria**|**Fase Operación Concentración Horaria**|**Fase Operación Concentración Horaria**|**Fase Operación Concentración Horaria**|**Fase Operación Concentración Horaria**|**Fase Operación Concentración Horaria**|**Fase Operación Concentración Horaria**|**Fase Operación Concentración Horaria**|**Fase Operación Concentración Horaria**|
|CO|**N°**|**Coordenadas Receptor**|**Coordenadas Receptor**|**Valor**<br>**Fondo**|**Aporte**<br>**Proyecto**<br>**Horario**|**Total**<br>**(Concentración**<br>**final (situación**<br>**basal más**<br>**aporte**<br>**proyecto)**|**Normativa**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**final**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**aporte del**<br>**proyecto**|
|CO|**N°**|**NLAT_WGS84**|**ELON_WGS84**|** ug/m3**|**ug/m3**|**ug/m3**|**ug/m3**|**% **|**% **|
|CO|**1 **|-40.27159|-73.118011||2.E-03|2.E-03|30|0.01|0.01|
|CO|2|-40.269632|-73.115445||2.E-03|2.E-03|30|0.01|0.01|
|CO|3|-40.269632|-73.11445||2.E-03|2.E-03|30|0.01|0.01|
|CO|4|-40.262679|-73.111779||2.E-03|2.E-03|30|0.01|0.01|
|CO|5|-40.264237|-73.124765||3.E-04|3.E-04|30|0.00|0.00|
|CO|6|-40.260482|-73.1078||1.E-03|1.E-03<br>|30|0.00<br>|0.00|
|CO|7|-40.265796|-73.114816||6.E-03|~~6.E-03~~|30|~~0.02~~|0.02|
|CO|8|-40.272394|-73.112981||8.E-04|8.E-04|30|0.00|0.00|

_**www.modelacionesatmosfericas.cl**_
37

**Modelación de Estimaciones Atmosféricas**

**“DIA PARQUE SOLAR BURGOS”**

|Col1|9|-40.2724|-73.112407|Col5|7.E-04|7.E-04|30|0.00|0.00|
|---|---|---|---|---|---|---|---|---|---|
|**Fase Abandono Concentración Horaria**|**Fase Abandono Concentración Horaria**|**Fase Abandono Concentración Horaria**|**Fase Abandono Concentración Horaria**|**Fase Abandono Concentración Horaria**|**Fase Abandono Concentración Horaria**|**Fase Abandono Concentración Horaria**|**Fase Abandono Concentración Horaria**|**Fase Abandono Concentración Horaria**|**Fase Abandono Concentración Horaria**|
|CO|**N°**|**Coordenadas Receptor**|**Coordenadas Receptor**|**Valor**<br>**Fondo**|**Aporte**<br>**Proyecto**<br>**Horario**|**Total**<br>**(Concentración**<br>**final (situación**<br>**basal más**<br>**aporte**<br>**proyecto)**|**Normativa**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**final**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**aporte del**<br>**proyecto**|
|CO|**N°**|**NLAT_WGS84**|**ELON_WGS84**|** ug/m3**|**ug/m3**|**ug/m3**|**ug/m3**|**% **|**% **|
|CO|1|-40.27159|-73.118011||3.E-02|3.E-02|30|0.11|0.11|
|CO|2|-40.269632|-73.115445||4.E-02|4.E-02|30|0.14|0.14|
|CO|3|-40.269632|-73.11445||3.E-02|3.E-02|30|0.10|0.10|
|CO|4|-40.262679|-73.111779||4.E-02|4.E-02|30|0.13|0.13|
|CO|5|-40.264237|-73.124765||6.E-03|6.E-03|30|0.02|0.02|
|CO|6|-40.260482|-73.1078||2.E-02|2.E-02|30|0.06|0.06|
|CO|7|-40.265796|-73.114816||1.E-01|1.E-01|30|0.32|0.32|
|CO|8|-40.272394|-73.112981||1.E-02|1.E-02|30|0.04|0.04|
|CO|9|-40.2724|-73.112407||1.E-02|1.E-02|30|0.04|0.04|

|Fase Construcción Concentración 8 Horas|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|CO|**N°**|**Coordenadas Receptor**|**Coordenadas Receptor**|**Valor**<br>**Fondo**|**Aporte**<br>**Proyecto**<br>**8 Hrs**|**Total**<br>**(Concentración**<br>**final (situación**<br>**basal más**<br>**aporte**<br>**proyecto)**|**Normativa**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**final**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**aporte del**<br>**proyecto**|
|CO|**N°**|**NLAT_WGS84**|**ELON_WGS84**|**ug/m3**|**ug/m3**|**ug/m3**|**ug/m3**|**% **|**% **|
|CO|1|-40.27159|-73.118011||2.05E-02|2.05E-02|10|0.20|0.20|
|CO|2|-40.269632|-73.115445||2.39E-02|2.39E-02|10|0.24|0.24|
|CO|3|-40.269632|-73.11445||2.15E-02|2.15E-02|10|0.21|0.21|
|CO|4|-40.262679|-73.111779||1.76E-02|1.76E-02|10|0.18|0.18|
|CO|5|-40.264237|-73.124765||6.08E-03|6.08E-03|10|0.06|0.06|
|CO|6|-40.260482|-73.1078||9.38E-03|9.38E-03|10|0.09|0.09|
|CO|7|-40.265796|-73.114816||3.67E-02|3.67E-02|10|0.37|0.37|
|CO|8|-40.272394|-73.112981||1.23E-02|1.23E-02|11|0.11|0.11|
|CO|9|-40.2724|-73.112407||1.07E-02|1.07E-02|12|0.09|0.09|
|**Fase Operación Concentración 8 Horas**|**Fase Operación Concentración 8 Horas**|**Fase Operación Concentración 8 Horas**|**Fase Operación Concentración 8 Horas**|**Fase Operación Concentración 8 Horas**|**Fase Operación Concentración 8 Horas**|**Fase Operación Concentración 8 Horas**|**Fase Operación Concentración 8 Horas**|**Fase Operación Concentración 8 Horas**|**Fase Operación Concentración 8 Horas**|
|CO|**N°**|**Coordenadas Receptor**|**Coordenadas Receptor**|**Valor**<br>**Fondo**|**Aporte**<br>**Proyecto**<br>**8 Hrs**|**Total**<br>**(Concentración**<br>**final (situación**<br>**basal más**<br>**aporte**<br>**proyecto)**|**Normativa**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**final**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**aporte del**<br>**proyecto**|
|CO|**N°**|**NLAT_WGS84**|**ELON_WGS84**|**ug/m3**|**ug/m3**|**ug/m3**|**ug/m3**|**% **|**% **|
|CO|**1 **|-40.27159|-73.118011||1.46E-03|1.46E-03|10|1.46E-02|1.46E-02|
|CO|2|-40.269632|-73.115445||1.71E-03|1.71E-03|10|1.71E-02|1.71E-02|
|CO|3|-40.269632|-73.11445||1.53E-03|1.53E-03|10|1.53E-02|1.53E-02|
|CO|4|-40.262679|-73.111779||1.26E-03|1.26E-03|10|1.26E-02|1.26E-02|
|CO|5|-40.264237|-73.124765||4.35E-04|4.35E-04<br>|10|4.35E-03<br>|4.35E-03|
|CO|6|-40.260482|-73.1078||6.70E-04|~~6.70E-04~~|10|~~6.70E-03~~|6.70E-03|
|CO|7|-40.265796|-73.114816||2.62E-03|2.62E-03|10|2.62E-02|2.62E-02|
|CO|8|-40.272394|-73.112981||8.77E-04|8.77E-04|10|8.77E-03|8.77E-03|
|CO|9|-40.2724|-73.112407||7.65E-04|7.65E-04|10|7.65E-03|7.65E-03|
|**Fase Abandono Concentración 8 Horas**|**Fase Abandono Concentración 8 Horas**|**Fase Abandono Concentración 8 Horas**|**Fase Abandono Concentración 8 Horas**|**Fase Abandono Concentración 8 Horas**|**Fase Abandono Concentración 8 Horas**|**Fase Abandono Concentración 8 Horas**|**Fase Abandono Concentración 8 Horas**|**Fase Abandono Concentración 8 Horas**|**Fase Abandono Concentración 8 Horas**|
|CO|**N°**|**Coordenadas Receptor**|**Coordenadas Receptor**|**Valor**<br>**Fondo**|**Aporte**<br>**Proyecto**<br>**8 Hrs**|**Total**<br>**(Concentración**<br>**final (situación**<br>**basal más**|**Normativa**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**final**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**|

_**www.modelacionesatmosfericas.cl**_
38

**Modelación de Estimaciones Atmosféricas**

**“DIA PARQUE SOLAR BURGOS”**

|Col1|Col2|Col3|Col4|Col5|Col6|aporte<br>proyecto)|Col8|Col9|aporte del<br>proyecto|
|---|---|---|---|---|---|---|---|---|---|
|||**NLAT_WGS84**|**ELON_WGS84**|**ug/m3**|**ug/m3**|**ug/m3**|**ug/m3**|**% **|**% **|
||1|-40.27159|-73.118011||2.48E-02|2.48E-02|10|2.48E-01|0.24845|
||2|-40.269632|-73.115445||2.90E-02|2.90E-02|10|2.90E-01|0.29035|
||3|-40.269632|-73.11445||2.61E-02|2.61E-02|10|2.61E-01|0.2608|
||4|-40.262679|-73.111779||2.14E-02|2.14E-02|10|2.14E-01|0.2141|
||5|-40.264237|-73.124765||7.39E-03|7.39E-03|10|7.39E-02|0.073883|
||6|-40.260482|-73.1078||1.14E-02|1.14E-02|10|1.14E-01|0.11388|
||7|-40.265796|-73.114816||4.46E-02|4.46E-02|10|4.46E-01|0.44586|
||8|-4.03E+01|-7.31E+01||1.49E-02|1.49E-02|10|1.49E-01|0.14906|
||9|-4.03E+01|-7.31E+01||1.30E-02|1.30E-02|10|1.30E-01|0.13011|

Como se observa en la tabla aquí indicada, los receptores evaluados, poseen concentraciones muy

por debajo del límite establecido en la norma de calidad primaria; 30 ug/m3N para la concentración

horaria, y 10 ug/m3N para la concentración 8 horas, respectivamente, por tanto, es posible señalar

que el proyecto no aporta significativamente sobre la calidad de aire del área de influencia toda vez

que sus concentraciones son despreciables.

Para mayor comprensión en Anexo N°1 se presentan imágenes de pluma de dispersión

representada por isoconcentraciones que reflejan el resultado de la modelación.

_**www.modelacionesatmosfericas.cl**_
39

**Modelación de Estimaciones Atmosféricas**

**“DIA PARQUE SOLAR BURGOS”**

**4.1.1** **Concentración SO2**

El flujo de emisiones se concentra en la zona inmediata al proyecto, desplazándose la pluma de

dispersión hacia el sector noreste, observándose una concentración máxima diaria en el receptor

N°7 con un valor de 5E-02 ug/m3 en la fase de Construcción concentración horaria.

Las coordenadas y concentraciones en períodos de concentración horaria, diaria y anual de

receptores discretos se presenta en la siguiente tabla.

Tabla 10 **Concentración SO2** **en Receptores Discretos**

|Fase Construcción Concentración Horaria|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|SO2|**N°**|**Coordenadas Receptor**|**Coordenadas Receptor**|**Valor**<br>**Fondo**|**Aporte**<br>**Proyecto**<br>**Horaria**|**Total**<br>**(Concentración**<br>**final (situación**<br>**basal más**<br>**aporte**<br>**proyecto)**|**Normativa**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**final**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**aporte del**<br>**proyecto**|
|SO2|**N°**|**NLAT_WGS84**|**ELON_WGS84**|** ug/m3**|**ug/m3**|**ug/m3**|**ug/m3**|**% **|**% **|
|SO2|1|-40.27159|-73.118011||8.E-03|8.E-03|350|2.E-03|2.E-03|
|SO2|2|-40.269632|-73.115445||1.E-02|1.E-02|350|4.E-03|4.E-03|
|SO2|3|-40.269632|-73.11445||1.E-02|1.E-02|350|3.E-03|3.E-03|
|SO2|4|-40.262679|-73.111779||1.E-02|1.E-02|350|3.E-03|3.E-03|
|SO2|5|-40.264237|-73.124765||2.E-03|2.E-03|350|7.E-04|7.E-04|
|SO2|6|-40.260482|-73.1078||6.E-03|6.E-03|350|2.E-03|2.E-03|
|SO2|7|-40.265796|-73.114816||5.E-02|5.E-02|350|1.E-02|1.E-02|
|SO2|8|-40.272394|-73.112981||4.E-03|4.E-03|351|1.E-03|1.E-03|
|SO2|9|-40.2724|-73.112407||4.E-03|4.E-03|352|1.E-03|1.E-03|
|**Fase Operación Concentración Horaria**|**Fase Operación Concentración Horaria**|**Fase Operación Concentración Horaria**|**Fase Operación Concentración Horaria**|**Fase Operación Concentración Horaria**|**Fase Operación Concentración Horaria**|**Fase Operación Concentración Horaria**|**Fase Operación Concentración Horaria**|**Fase Operación Concentración Horaria**|**Fase Operación Concentración Horaria**|
|SO2|**N°**|**Coordenadas Receptor**|**Coordenadas Receptor**|**Valor**<br>**Fondo**|**Aporte**<br>**Proyecto**<br>**Horaria**|**Total**<br>**(Concentración**<br>**final (situación**<br>**basal más**<br>**aporte**<br>**proyecto)**|**Normativa**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**final**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**aporte del**<br>**proyecto**|
|SO2|**N°**|**NLAT_WGS84**|**ELON_WGS84**|** ug/m3**|**ug/m3**|**ug/m3**|**ug/m3**|**% **|**% **|
|SO2|**1 **|-40.27159|-73.118011||8.46E-07|8.46E-07|350|2.42E-07|2.42E-07|
|SO2|2|-40.269632|-73.115445||1.50E-06|1.50E-06|350|4.28E-07|4.28E-07|
|SO2|3|-40.269632|-73.11445||1.12E-06|1.12E-06<br>|350|3.19E-07<br>|3.19E-07|
|SO2|4|-40.262679|-73.111779||9.98E-07|~~9.98E-07~~|350|~~2.85E-07~~|2.85E-07|
|SO2|5|-40.264237|-73.124765||2.34E-07|2.34E-07|350|6.68E-08|6.68E-08|
|SO2|6|-40.260482|-73.1078||6.30E-07|6.30E-07|350|1.80E-07|1.80E-07|
|SO2|7|-40.265796|-73.114816||4.53E-06|4.53E-06|350|1.30E-06|1.30E-06|
|SO2|8|-40.272394|-73.112981||4.41E-07|4.41E-07|350|1.26E-07|1.26E-07|
||9|-40.2724|-73.112407||4.17E-07|4.17E-07|350|1.19E-07|1.19E-07|
|**Fase Abandono ConcentraciónHoraria**|**Fase Abandono ConcentraciónHoraria**|**Fase Abandono ConcentraciónHoraria**|**Fase Abandono ConcentraciónHoraria**|**Fase Abandono ConcentraciónHoraria**|**Fase Abandono ConcentraciónHoraria**|**Fase Abandono ConcentraciónHoraria**|**Fase Abandono ConcentraciónHoraria**|**Fase Abandono ConcentraciónHoraria**|**Fase Abandono ConcentraciónHoraria**|
|SO2|**N°**|**Coordenadas Receptor**|**Coordenadas Receptor**|**Valor**<br>**Fondo**|**Aporte**<br>**Proyecto**<br>**Horaria**|**Total**<br>**(Concentración**<br>**final (situación**<br>**basal más**<br>**aporte**<br>**proyecto)**|**Normativa**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**final**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**aporte del**<br>**proyecto**|
|SO2|**N°**|**NLAT_WGS84**|**ELON_WGS84**|** ug/m3**|**ug/m3**|**ug/m3**|**ug/m3**|**% **|**% **|
|SO2|1|-40.27159|-73.118011||8.46E-04|8.46E-04|350|0.000|0.000|
|SO2|2|-40.269632|-73.115445||1.50E-03|1.50E-03|350|0.000|0.000|
|SO2|3|-40.269632|-73.11445||1.12E-03|1.12E-03|350|0.000|0.000|
|SO2|4|-40.262679|-73.111779||9.98E-04|9.98E-04|350|0.000|0.000|
|SO2|5|-40.264237|-73.124765||2.34E-04|2.34E-04|350|0.000|0.000|

_**www.modelacionesatmosfericas.cl**_
40

**Modelación de Estimaciones Atmosféricas**

**“DIA PARQUE SOLAR BURGOS”**

|Col1|6|-40.260482|-73.1078|Col5|6.30E-04|6.30E-04|350|0.000|0.000|
|---|---|---|---|---|---|---|---|---|---|
||7|-40.265796|-73.114816||4.53E-03|4.53E-03|350|0.001|0.001|
||8|-4.03E+01|-7.31E+01||4.41E-04|4.41E-04|350|0.000|0.000|
||9|-4.03E+01|-7.31E+01||4.17E-04|4.17E-04|350|0.000|0.000|

|Fase Construcción Diaria|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|SO2|**N°**|**Coordenadas Receptor**|**Coordenadas Receptor**|**Valor**<br>**Fondo**|**Aporte**<br>**Proyecto**<br>**Anual**|**Total**<br>**(Concentración**<br>**final (situación**<br>**basal más**<br>**aporte**<br>**proyecto)**|**Normativa**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**final**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**aporte del**<br>**proyecto**|
|SO2|**N°**|**NLAT_WGS84**|**ELON_WGS84**|** ug/m3**|**ug/m3**|**ug/m3**|**ug/m3**|**% **|**% **|
|SO2|1|-40.27159|-73.118011||7.E-03|7.E-03|150|5.E-03|5.E-03|
|SO2|2|-40.269632|-73.115445||8.E-03|8.E-03|150|5.E-03|5.E-03|
|SO2|3|-40.269632|-73.11445||7.E-03|7.E-03|150|4.E-03|4.E-03|
|SO2|4|-40.262679|-73.111779||6.E-03|6.E-03|150|4.E-03|4.E-03|
|SO2|5|-40.264237|-73.124765||2.E-03|2.E-03|150|2.E-03|2.E-03|
|SO2|6|-40.260482|-73.1078||3.E-03|3.E-03|150|2.E-03|2.E-03|
|SO2|7|-40.265796|-73.114816||1.E-02|1.E-02|150|9.E-03|9.E-03|
|SO2|8|-40.272394|-73.112981||4.E-03|4.E-03|150|3.E-03|3.E-03|
|SO2|9|-40.2724|-73.112407||3.E-03|3.E-03|150|2.E-03|2.E-03|
|**Fase Operación Concentración Diaria**|**Fase Operación Concentración Diaria**|**Fase Operación Concentración Diaria**|**Fase Operación Concentración Diaria**|**Fase Operación Concentración Diaria**|**Fase Operación Concentración Diaria**|**Fase Operación Concentración Diaria**|**Fase Operación Concentración Diaria**|**Fase Operación Concentración Diaria**|**Fase Operación Concentración Diaria**|
|SO2|**N°**|**Coordenadas Receptor**|**Coordenadas Receptor**|**Valor**<br>**Fondo**|**Aporte**<br>**Proyecto**<br>**Anual**|**Total**<br>**(Concentración**<br>**final (situación**<br>**basal más**<br>**aporte**<br>**proyecto)**|**Normativa**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**final**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**aporte del**<br>**proyecto**|
|SO2|**N°**|**NLAT_WGS84**|**ELON_WGS84**|** ug/m3**|**ug/m3**|**ug/m3**|**ug/m3**|**% **|**% **|
|SO2|**1 **|-40.27159|-73.118011||6.76E-07|6.76E-07|150|4.51E-07|4.51E-07|
|SO2|2|-40.269632|-73.115445||7.57E-07|7.57E-07|150|5.05E-07|5.05E-07|
|SO2|3|-40.269632|-73.11445||6.66E-07|6.66E-07|150|4.44E-07|4.44E-07|
|SO2|4|-40.262679|-73.111779||5.84E-07|5.84E-07<br>|150|3.89E-07<br>|3.89E-07|
|SO2|5|-40.264237|-73.124765||2.32E-07|~~2.32E-07~~|150|~~1.54E-07~~|1.54E-07|
|SO2|6|-40.260482|-73.1078||3.07E-07|3.07E-07|150|2.05E-07|2.05E-07|
|SO2|7|-40.265796|-73.114816||1.41E-06|1.41E-06|150|9.41E-07|9.41E-07|
|SO2|8|-40.272394|-73.112981||4.22E-07|4.22E-07|150|2.81E-07|2.81E-07|
|SO2|9|-40.2724|-73.112407||3.19E-07|3.19E-07|150|2.13E-07|2.13E-07|
|**Fase Abandono Concentración Diaria**|**Fase Abandono Concentración Diaria**|**Fase Abandono Concentración Diaria**|**Fase Abandono Concentración Diaria**|**Fase Abandono Concentración Diaria**|**Fase Abandono Concentración Diaria**|**Fase Abandono Concentración Diaria**|**Fase Abandono Concentración Diaria**|**Fase Abandono Concentración Diaria**|**Fase Abandono Concentración Diaria**|
|SO2|**N°**|**Coordenadas Receptor**|**Coordenadas Receptor**|**Valor**<br>**Fondo**|**Aporte**<br>**Proyecto**<br>**Anual**|**Total**<br>**(Concentración**<br>**final (situación**<br>**basal más**<br>**aporte**<br>**proyecto)**|**Normativa**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**final**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**aporte del**<br>**proyecto**|
|SO2|**N°**|**NLAT_WGS84**|**ELON_WGS84**|** ug/m3**|**ug/m3**|**ug/m3**|**ug/m3**|**% **|**% **|
|SO2|1|-40.27159|-73.118011||7.E-04|2.E-03|150|0.0014|0.0005|
|SO2|2|-40.269632|-73.115445||8.E-04|2.E-03|150|0.0015|0.0005|
|SO2|3|-40.269632|-73.11445||7.E-04|2.E-03|150|0.0013|0.0004|
|SO2|4|-40.262679|-73.111779||6.E-04|2.E-03|150|0.0012|0.0004|
|SO2|5|-40.264237|-73.124765||2.E-04|7.E-04|150|0.0005|0.0002|
|SO2|6|-40.260482|-73.1078||3.E-04|9.E-04|150|0.0006|0.0002|
|SO2|7|-40.265796|-73.114816||1.E-03|4.E-03|150|0.0028|0.0009|
|SO2|8|-4.E+01|-7.E+01||4.E-04|8.E-03|150|0.0050|0.0003|
|SO2|9|-4.E+01|-7.E+01||3.E-04|1.E-02|150|0.0072|0.0002|

_**www.modelacionesatmosfericas.cl**_
41

**Modelación de Estimaciones Atmosféricas**

**“DIA PARQUE SOLAR BURGOS”**

|Fase Construcción Anual|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|SO2|**N°**|**Coordenadas Receptor**|**Coordenadas Receptor**|**Valor**<br>**Fondo**|**Aporte**<br>**Proyecto**<br>**Anual**|**Total**<br>**(Concentración**<br>**final (situación**<br>**basal más**<br>**aporte**<br>**proyecto)**|**Normativa**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**final**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**aporte del**<br>**proyecto**|
|SO2|**N°**|**NLAT_WGS84**|**ELON_WGS84**|** ug/m3**|**ug/m3**|**ug/m3**|**ug/m3**|**% **|**% **|
|SO2|1|-40.27159|-73.118011||9.E-04|9.E-04|60|0.0015|0.0015|
|SO2|2|-40.269632|-73.115445||1.E-03|1.E-03|60|0.0021|0.0021|
|SO2|3|-40.269632|-73.11445||1.E-03|1.E-03|60|0.0018|0.0018|
|SO2|4|-40.262679|-73.111779||1.E-03|1.E-03|60|0.0019|0.0019|
|SO2|5|-40.264237|-73.124765||3.E-04|3.E-04|60|0.0004|0.0004|
|SO2|6|-40.260482|-73.1078||6.E-04|6.E-04|60|0.0009|0.0009|
|SO2|7|-40.265796|-73.114816||4.E-03|4.E-03|60|0.0061|0.0061|
|SO2|8|-40.272394|-73.112981||5.E-04|5.E-04|60|0.0009|0.0009|
|SO2|9|-40.2724|-73.112407||5.E-04|5.E-04|60|0.0008|0.0008|
|**Fase Operación Concentración Anual**|**Fase Operación Concentración Anual**|**Fase Operación Concentración Anual**|**Fase Operación Concentración Anual**|**Fase Operación Concentración Anual**|**Fase Operación Concentración Anual**|**Fase Operación Concentración Anual**|**Fase Operación Concentración Anual**|**Fase Operación Concentración Anual**|**Fase Operación Concentración Anual**|
|SO2|**N°**|**Coordenadas Receptor**|**Coordenadas Receptor**|**Valor**<br>**Fondo**|**Aporte**<br>**Proyecto**<br>**Anual**|**Total**<br>**(Concentración**<br>**final (situación**<br>**basal más**<br>**aporte**<br>**proyecto)**|**Normativa**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**final**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**aporte del**<br>**proyecto**|
|SO2|**N°**|**NLAT_WGS84**|**ELON_WGS84**|** ug/m3**|**ug/m3**|**ug/m3**|**ug/m3**|**% **|**% **|
|SO2|**1 **|-40.27159|-73.118011||9.23E-08|9.23E-08|60|1.54E-07|1.54E-07|
|SO2|2|-40.269632|-73.115445||1.29E-07|1.29E-07|60|2.15E-07|2.15E-07|
|SO2|3|-40.269632|-73.11445||1.07E-07|1.07E-07|60|1.78E-07|1.78E-07|
|SO2|4|-40.262679|-73.111779||1.16E-07|1.16E-07|60|1.94E-07|1.94E-07|
|SO2|5|-40.264237|-73.124765||2.67E-08|2.67E-08|60|4.45E-08|4.45E-08|
|SO2|6|-40.260482|-73.1078||5.61E-08<br>|5.61E-08<br>|60|9.34E-08<br>|9.34E-08|
|SO2|7|-40.265796|-73.114816||~~3.66E-07~~|~~3.66E-07~~|60|~~6.10E-07~~|6.10E-07|
|SO2|8|-40.272394|-73.112981||5.45E-08|5.45E-08|60|9.08E-08|9.08E-08|
|SO2|9|-40.2724|-73.112407||4.72E-08|4.72E-08|60|7.87E-08|7.87E-08|
|**Fase Abandono Concentración Anual**|**Fase Abandono Concentración Anual**|**Fase Abandono Concentración Anual**|**Fase Abandono Concentración Anual**|**Fase Abandono Concentración Anual**|**Fase Abandono Concentración Anual**|**Fase Abandono Concentración Anual**|**Fase Abandono Concentración Anual**|**Fase Abandono Concentración Anual**|**Fase Abandono Concentración Anual**|
|SO2|**N°**|**Coordenadas Receptor**|**Coordenadas Receptor**|**Valor**<br>**Fondo**|**Aporte**<br>**Proyecto**<br>**Anual**|**Total**<br>**(Concentración**<br>**final (situación**<br>**basal más**<br>**aporte**<br>**proyecto)**|**Normativa**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**final**|**Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**aporte del**<br>**proyecto**|
|SO2|**N°**|**NLAT_WGS84**|**ELON_WGS84**|** ug/m3**|**ug/m3**|**ug/m3**|**ug/m3**|**% **|**% **|
|SO2|1|-40.27159|-73.118011||9.23E-05|9.23E-05|60|0.0002|0.0002|
|SO2|2|-40.269632|-73.115445||1.29E-04|1.29E-04|60|0.0002|0.0002|
|SO2|3|-40.269632|-73.11445||1.07E-04<br>|1.07E-04<br>|60|0.0002|0.0002|
|SO2|4|-40.262679|-73.111779||~~1.16E-04~~|~~1.16E-04~~|60|0.0002|0.0002|
|SO2|5|-40.264237|-73.124765||2.67E-05|2.67E-05|60|0.0000|0.0000|
|SO2|6|-40.260482|-73.1078||5.61E-05|5.61E-05|60|0.0001|0.0001|
|SO2|7|-40.265796|-73.114816||3.66E-04|3.66E-04|60|0.0006|0.0006|
|SO2|8|-40.272394|-73.112981||5.45E-05|5.45E-05|60|0.0001|0.0001|
|SO2|9|-40.2724|-73.112407||4.72E-05|4.72E-05|60|0.0001|0.0001|

_**www.modelacionesatmosfericas.cl**_
42

**Modelación de Estimaciones Atmosféricas**

**“DIA PARQUE SOLAR BURGOS”**

Como se observa en la tabla aquí indicada, los receptores evaluados, poseen concentraciones muy

por debajo del límite establecido en la norma de calidad primaria, por tanto, es posible señalar que

el proyecto no aporta significativamente sobre la calidad de aire del área de influencia toda vez que

sus concentraciones son despreciables

Para mayor comprensión en Anexo N°1 se presentan imágenes de pluma de dispersión

representada por isoconcentraciones que reflejan el resultado de la modelación.

_**www.modelacionesatmosfericas.cl**_
43

**Modelación de Estimaciones Atmosféricas**

**“DIA PARQUE SOLAR BURGOS”**

## 5. CONCLUSIÓN

A partir de las modelaciones realizadas con respecto a las emisiones atmosféricas generadas
durante las fases de Construcción, Operación y Cierre del Parque Solar Burgos, se presentan las
siguientes conclusiones:

El flujo de emisiones se concentra en la zona inmediata al proyecto, desplazándose la pluma de

dispersión hacia el sector noreste en una distancia de 5.44 kilómetros apróximadamente desde la

fuente de emisión.

De acuerdo a los resultados obtenidos es posible señalar que en todas las fases evaluadas

(Construcción, Operación y Cierre) del proyecto, las emisiones atmosféricas no generará eventos

de latencia y saturación para los compuestos evaluados (MP10, MP2.5, NOx, CO y SO2), por cuanto,

no se superan los límites establecidos en las normas de calidad primaria para los compuestos antes

indicados.

_**www.modelacionesatmosfericas.cl**_
44

**Modelación de Estimaciones Atmosféricas**

**“DIA PARQUE SOLAR BURGOS”**

## 6. REFERENCIAS

 - Registro de Monitoreo Calidad de Aire y Meteorológico Estación La Unión.

 - Pontificia Universidad Católica de Chile, Educación Continua UC, Escuela de Ingeniería.

(2014). Manual de Usuario CALPUFF View.

 - Scire, J. S., Strimaitis, D. G., y Yamartino, R. J., 2000a. A User’s Guide for the CALPUFF

Dispersion Model (Version 5). Earth Tech Inc., Concord, Massachusetts.

_**www.modelacionesatmosfericas.cl**_
45

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 2: **: Comparación vientos observados vs modelados (WRF)****

| Estación | Sesgo | RMSE | r |
| --- | --- | --- | --- |
| La Unión | 1.11 | 1.95 | 0.25 |

**Tabla 3: Total emisiones por fase del Proyecto**

| Fase | MP (Ton/año | MP10<br>(Ton/año) | MP2.5<br>(Ton/año) | NOx<br>(Ton/año) | CO<br>(Ton/año) | Sox<br>(Ton/año) |
| --- | --- | --- | --- | --- | --- | --- |
| **Construcción** | 1.17 | 0.33 | 0.11 | 0.58 | 0.00442 | 3.63E-04 |
| **Operación** | 0.03 | 0.01 | 0.0009 | 0.0003 | 0.00036 | 4.29E-07 |
| **Cierre** | 1.32 | 0.35 | 0.12 | 0.62 | 0.00534 | 3.87E-04 |

**Tabla 4: Concentración (ug/m3) promedio de contaminantes en EMRP durante el año 2020**

| MP10 (ug/m3)<br>concentración<br>promedio 24 hrs | MP2.5 (ug/m3)<br>concentración<br>promedio 24 hrs | NOx (ug/m3)<br>concentración<br>promedio 24 hrs | CO(ug/m3)<br>concentración<br>promedio 1 hr |
| --- | --- | --- | --- |
| **s.i** | **27,04** | **si** | **si** |

**Tabla 5: **Normativa aplicable****

| Normativa | Límite Norma | Concentración |
| --- | --- | --- |
| - DS 104/2018 del MMA, norma primaria de calidad del aire para SO2,; <br> | 60 ug/m3N <br> | Anual <br> |
| - DS 104/2018 del MMA, norma primaria de calidad del aire para SO2,; <br> | 150 ug/m3N <br> | Diaria <br> |
| - DS 104/2018 del MMA, norma primaria de calidad del aire para SO2,; <br> | 350 ug/m3N <br> | Horaria <br> |
| - DS 104/2018 del MMA, norma secundaria de calidad del aire para SO2,; <br> | 60 ug/m3N <br> | Anual <br> |
| - DS 104/2018 del MMA, norma secundaria de calidad del aire para SO2,; <br> | 260 ug/m3N <br> | Diaria <br> |
| - DS 104/2018 del MMA, norma secundaria de calidad del aire para SO2,; <br> | 700 ug/m3N <br> | Horaria <br> |
| - DS 114/2002 del MINSEGPRES, norma primaria de calidad del aire para NO2; <br> | ~~400 ug/m3N ~~<br> | ~~1 hora ~~<br> |
| - DS 114/2002 del MINSEGPRES, norma primaria de calidad del aire para NO2; <br> | 100 ug/m3N <br> | Anual <br> |
| - DS 115/2002 del MINSEGPRES, norma primaria de calidad del aire para CO; <br> | 10 mg/m3N <br> | 8 horas <br> |
| - DS 115/2002 del MINSEGPRES, norma primaria de calidad del aire para CO; <br> | 30 mg/m3N <br> | 1 hora <br> |
| - DS 12/2010 del MMA, norma primaria de calidad del aire paraMP2,5 <br> | 50 ug/m3N <br> | Diaria <br> |
| - DS 12/2010 del MMA, norma primaria de calidad del aire paraMP2,5 <br> | 20 ug/m3N <br> | Anual <br> |
| - DS 59/1998 del MINSEGPRES, norma primaria de calidad del aire para MP10; | 150 ug/m3N <br> | Diaria <br> |
| - DS 59/1998 del MINSEGPRES, norma primaria de calidad del aire para MP10; | 50 ug/m3N | Anual |

**Tabla 6: **Concentración MP10** **en Receptores Discretos****

| Fase Construcción Concentración Diaria | Col2 | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PM10 | **N°** | **Coordenadas Receptor** | **Coordenadas Receptor** | **Valor**<br>**Fondo** | **Aporte**<br>**Proyecto**<br>**24 hrs** | **Total**<br>**(Concentración**<br>**final (situación**<br>**basal más**<br>**aporte**<br>**proyecto)** | **Normativa** | **Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**final** | **Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**aporte del**<br>**proyecto** |
| PM10 | **N°** | **NLAT_WGS84** | **ELON_WGS84** | **ug/m3** | **ug/m3** | **ug/m3** | **ug/m3** | **% ** | **% ** |
| PM10 | 1 | -40.27159 | -73.118011 |  | 0.68 | 0.68 | 150 | 0.45 | 0.45 |
| PM10 | 2 | -40.269632 | -73.115445 |  | 0.76 | 0.76 | 150 | 0.50 | 0.50 |
| PM10 | 3 | -40.269632 | -73.11445 |  | 0.67 | 0.67 | 150 | 0.44 | 0.44 |
| PM10 | 4 | -40.262679 | -73.111779 |  | 0.58 | 0.58 | 150 | 0.39 | 0.39 |
| PM10 | 5 | -40.264237 | -73.124765 |  | 0.23 | 0.23 | 150 | 0.15 | 0.15 |
| PM10 | 6 | -40.260482 | -73.1078 |  | 0.31 | 0.31 | 150 | 0.20 | 0.20 |
| PM10 | 7 | -40.265796 | -73.114816 |  | 1.41 | 1.41 | 150 | 0.94 | 0.94 |
| PM10 | 8 | -40.272394 | -73.112981 |  | 0.42 | 0.42 | 150 | 0.28 | 0.28 |
| PM10 | 9 | -40.2724 | -73.112407 |  | 0.32 | 0.32 | 150 | 0.21 | 0.21 |
| **Fase Operación Concentración Diaria** | **Fase Operación Concentración Diaria** | **Fase Operación Concentración Diaria** | **Fase Operación Concentración Diaria** | **Fase Operación Concentración Diaria** | **Fase Operación Concentración Diaria** | **Fase Operación Concentración Diaria** | **Fase Operación Concentración Diaria** | **Fase Operación Concentración Diaria** | **Fase Operación Concentración Diaria** |
| PM10 | **N°** | **Coordenadas Receptor** | **Coordenadas Receptor** | **Valor**<br>**Fondo** | **Aporte**<br>**Proyecto**<br>**24 hrs** | **Total**<br>**(Concentración**<br>**final (situación**<br>**basal más**<br>**aporte**<br>**proyecto)** | **Normativa** | **Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**final** | **Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**aporte del**<br>**proyecto** |
| PM10 | **N°** | **NLAT_WGS84** | **ELON_WGS84** | **ug/m3** | **ug/m3** | **ug/m3** | **ug/m3** | **% ** | **% ** |
| PM10 | **1 ** | -40.27159 | -73.118011 |  | 2.03E-02 | 2.03E-02 | 150 | 0.01 | 0.01 |
| PM10 | 2 | -40.269632 | -73.115445 |  | 2.27E-02 | 2.27E-02 | 150 | 0.02 | 0.02 |
| PM10 | 3 | -40.269632 | -73.11445 |  | 2.00E-02 | 2.00E-02 | 150 | 0.01 | 0.01 |
| PM10 | 4 | -40.262679 | -73.111779 |  | 1.75E-02 | 1.75E-02 | 150 | 0.01 | 0.01 |
| PM10 | 5 | -40.264237 | -73.124765 |  | 6.95E-03 | 6.95E-03 | 150 | 0.00 | 0.00 |
| PM10 | 6 | -40.260482 | -73.1078 |  | 9.22E-03<br> | 9.22E-03<br> | 150 | 0.01<br> | 0.01<br> |
| PM10 | 7 | -40.265796 | -73.114816 |  | ~~4.24E-02~~ | ~~4.24E-02~~ | 150 | ~~0.03~~ | ~~0.03~~ |
| PM10 | 8 | -40.272394 | -73.112981 |  | 1.27E-02 | 1.27E-02 | 150 | 0.01 | 0.01 |
| PM10 | 9 | -40.2724 | -73.112407 |  | 9.58E-03 | 9.58E-03 | 150 | 0.01 | 0.01 |
| **Fase Abandono Concentración Diaria** | **Fase Abandono Concentración Diaria** | **Fase Abandono Concentración Diaria** | **Fase Abandono Concentración Diaria** | **Fase Abandono Concentración Diaria** | **Fase Abandono Concentración Diaria** | **Fase Abandono Concentración Diaria** | **Fase Abandono Concentración Diaria** | **Fase Abandono Concentración Diaria** | **Fase Abandono Concentración Diaria** |
| PM10 | **N°** | **Coordenadas Receptor** | **Coordenadas Receptor** | **Valor**<br>**Fondo** | **Aporte**<br>**Proyecto**<br>**24 hrs** | **Total**<br>**(Concentración**<br>**final (situación**<br>**basal más**<br>**aporte**<br>**proyecto)** | **Normativa** | **Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**final** | **Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**aporte del**<br>**proyecto** |
| PM10 | **N°** | **NLAT_WGS84** | **ELON_WGS84** | ug/m3 | ug/m3 | ug/m3 | ug/m3 | **% ** | **% ** |
| PM10 | 1 | -40.27159 | -73.118011 |  | 6.76E-01 | 6.76E-01 | 150 | 0.45 | 0.45 |
| PM10 | 2 | -40.269632 | -73.115445 |  | 7.57E-01 | 7.57E-01<br> | 150 | 0.50<br> | 0.50<br> |
| PM10 | 3 | -40.269632 | -73.11445 |  | 6.66E-01 | ~~6.66E-01~~ | 150 | ~~0.44~~ | ~~0.44~~ |

**Tabla 7: **Concentración MP2.5** **en Receptores Discretos****

| Fase Construcción Concentración Diaria | Col2 | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PM2.5 | **N°** | **Coordenadas Receptor** | **Coordenadas Receptor** | **Valor**<br>**Fondo** | **Aporte**<br>**Proyecto**<br>**24 hrs** | **Total**<br>**(Concentración**<br>**final (situación**<br>**basal más**<br>**aporte**<br>**proyecto)** | **Normativa** | **Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**final** | **Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**aporte del**<br>**proyecto** |
| PM2.5 | **N°** | **NLAT_WGS84** | **ELON_WGS84** | ** ug/m3** | **ug/m3** | **ug/m3** | **ug/m3** | **% ** | **% ** |
| PM2.5 | 1 | -40.27159 | -73.118011 | 27.04 | 0.20 | 27.24 | 50 | 54.49 | 0.41 |
| PM2.5 | 2 | -40.269632 | -73.115445 | 27.04 | 0.23 | 27.27 | 50 | 54.53 | 0.45 |
| PM2.5 | 3 | -40.269632 | -73.11445 | 27.04 | 0.20 | 27.24 | 50 | 54.48 | 0.40 |
| PM2.5 | 4 | -40.262679 | -73.111779 | 27.04 | 0.18 | 27.22 | 50 | 54.43 | 0.35 |
| PM2.5 | 5 | -40.264237 | -73.124765 | 27.04 | 0.07 | 27.11 | 50 | 54.22 | 0.14 |
| PM2.5 | 6 | -40.260482 | -73.1078 | 27.04 | 0.09 | 27.13 | 50 | 54.26 | 0.18 |
| PM2.5 | 7 | -40.265796 | -73.114816 | 27.04 | 0.42 | 27.46 | 50 | 54.93 | 0.85 |
| PM2.5 | 8 | -40.272394 | -73.112981 | 27.04 | 0.13 | 27.17 | 50 | 54.33 | 0.25 |
| PM2.5 | 9 | -40.2724 | -73.112407 | 27.04 | 0.10 | 27.14 | 50 | 54.27 | 0.19 |
| **Fase Operación Concentración Diaria** | **Fase Operación Concentración Diaria** | **Fase Operación Concentración Diaria** | **Fase Operación Concentración Diaria** | **Fase Operación Concentración Diaria** | **Fase Operación Concentración Diaria** | **Fase Operación Concentración Diaria** | **Fase Operación Concentración Diaria** | **Fase Operación Concentración Diaria** | **Fase Operación Concentración Diaria** |
| PM2.5 | **N°** | **Coordenadas Receptor** | **Coordenadas Receptor** | **Valor**<br>**Fondo** | **Aporte**<br>**Proyecto**<br>**24 hrs** | **Total**<br>**(Concentración**<br>**final (situación**<br>**basal más**<br>**aporte**<br>**proyecto)** | **Normativa** | **Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**final** | **Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**aporte del**<br>**proyecto** |
| PM2.5 | **N°** | **NLAT_WGS84** | **ELON_WGS84** | ** ug/m3** | **ug/m3** | **ug/m3** | **ug/m3** | **% ** | **% ** |
| PM2.5 | **1 ** | -40.27159 | -73.118011 | 27.04 | 0.002 | 27.04<br> | 50<br> | 54.08<br> | 0.00 |
| PM2.5 | 2 | -40.269632 | -73.115445 | 27.04 | 0.002 | ~~27.04~~ | ~~50~~ | ~~54.08~~ | 0.00 |
| PM2.5 | 3 | -40.269632 | -73.11445 | 27.04 | 0.002 | 27.04 | 50 | 54.08 | 0.00 |
| PM2.5 | 4 | -40.262679 | -73.111779 | 27.04 | 0.002 | 27.04 | 50 | 54.08 | 0.00 |
| PM2.5 | 5 | -40.264237 | -73.124765 | 27.04 | 0.001 | 27.04 | 50 | 54.08 | 0.00 |
| PM2.5 | 6 | -40.260482 | -73.1078 | 27.04 | 0.001 | 27.04 | 50 | 54.08 | 0.00 |

**Tabla 8: **Concentración NOx** **en Receptores Discretos****

| Fase Construcción Concentración Horaria | Col2 | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NOx | **N°** | **Coordenadas Receptor** | **Coordenadas Receptor** | **Valor**<br>**Fondo** | **Aporte**<br>**Proyecto**<br>**24 hrs** | **Total**<br>**(Concentración**<br>**final (situación**<br>**basal más**<br>**aporte**<br>**proyecto)** | **Normativa** | **Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**final** | **Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**aporte del**<br>**proyecto** |
| NOx | **N°** | **NLAT_WGS84** | **ELON_WGS84** | ** ug/m3** | **ug/m3** | **ug/m3** | **ug/m3** | **% ** | **% ** |
| NOx | 1 | -40.27159 | -73.118011 |  | 4.05 | 4.05 | 400 | 1.01 | 1.01 |
| NOx | 2 | -40.269632 | -73.115445 |  | 4.92 | 4.92 | 400 | 1.23 | 1.23 |
| NOx | 3 | -40.269632 | -73.11445 |  | 3.61 | 3.61 | 400 | 0.90 | 0.90 |
| NOx | 4 | -40.262679 | -73.111779 |  | 4.65 | 4.65 | 400 | 1.16 | 1.16 |
| NOx | 5 | -40.264237 | -73.124765 |  | 0.69 | 0.69 | 400 | 0.17 | 0.17 |
| NOx | 6 | -40.260482 | -73.1078 |  | 2.25 | 2.25 | 400 | 0.56 | 0.56 |
| NOx | 7 | -40.265796 | -73.114816 |  | 11.30 | 11.30 | 400 | 2.82 | 2.82 |
| NOx | 8 | -40.272394 | -73.112981 |  | 1.55 | 1.55 | 400 | 0.39 | 0.39 |
| NOx | 9 | -40.2724 | -73.112407 |  | 1.37 | 1.37 | 400 | 0.34 | 0.34 |
| **Fase Operación Concentración Horaria** | **Fase Operación Concentración Horaria** | **Fase Operación Concentración Horaria** | **Fase Operación Concentración Horaria** | **Fase Operación Concentración Horaria** | **Fase Operación Concentración Horaria** | **Fase Operación Concentración Horaria** | **Fase Operación Concentración Horaria** | **Fase Operación Concentración Horaria** | **Fase Operación Concentración Horaria** |
| NOx | **N°** | **Coordenadas Receptor** | **Coordenadas Receptor** | **Valor**<br>**Fondo** | **Aporte**<br>**Proyecto**<br>**24 hrs** | **Total**<br>**(Concentración**<br>**final (situación**<br>**basal más**<br>**aporte**<br>**proyecto)** | **Normativa** | **Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**final** | **Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**aporte del**<br>**proyecto** |
| NOx | **N°** | **NLAT_WGS84** | **ELON_WGS84** | ** ug/m3** | **ug/m3** | **ug/m3** | **ug/m3** | **% ** | **% ** |
| NOx | **1 ** | -40.27159 | -73.118011 |  | 2.E-03 | 2.E-03 | 400 | 0.000 | 0.000 |
| NOx | 2 | -40.269632 | -73.115445 |  | 2.E-03 | 2.E-03 | 400 | 0.001 | 0.001 |
| NOx | 3 | -40.269632 | -73.11445 |  | 2.E-03 | 2.E-03<br> | 400 | 0.000<br> | 0.000 |
| NOx | 4 | -40.262679 | -73.111779 |  | 2.E-03 | ~~2.E-03~~ | 400 | ~~0.001~~ | 0.001 |
| NOx | 5 | -40.264237 | -73.124765 |  | 3.E-04 | 3.E-04 | 400 | 0.000 | 0.000 |
| NOx | 6 | -40.260482 | -73.1078 |  | 1.E-03 | 1.E-03 | 400 | 0.000 | 0.000 |
| NOx | 7 | -40.265796 | -73.114816 |  | 5.E-03 | 5.E-03 | 400 | 0.001 | 0.001 |
| NOx | 8 | -40.272394 | -73.112981 |  | 7.E-04 | 7.E-04 | 400 | 0.000 | 0.000 |
| NOx | 9 | -40.2724 | -73.112407 |  | 6.E-04 | 6.E-04 | 400 | 0.000 | 0.000 |
| **Fase Abandono Concentración Horaria** | **Fase Abandono Concentración Horaria** | **Fase Abandono Concentración Horaria** | **Fase Abandono Concentración Horaria** | **Fase Abandono Concentración Horaria** | **Fase Abandono Concentración Horaria** | **Fase Abandono Concentración Horaria** | **Fase Abandono Concentración Horaria** | **Fase Abandono Concentración Horaria** | **Fase Abandono Concentración Horaria** |
| NOx | **N°** | **Coordenadas Receptor** | **Coordenadas Receptor** | **Valor**<br>**Fondo** | **Aporte**<br>**Proyecto**<br>**24 hrs** | **Total**<br>**(Concentración**<br>**final (situación**<br>**basal más**<br>**aporte**<br>**proyecto)** | **Normativa** | **Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**final** | **Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**aporte del**<br>**proyecto** |
| NOx | **N°** | **NLAT_WGS84** | **ELON_WGS84** | ** ug/m3** | **ug/m3** | **ug/m3** | **ug/m3** | **% **<br> | **% **<br> |
| NOx | 1 | -40.27159 | -73.118011 |  | 4.05 | 4.046 | 400 | ~~1.0~~ | ~~1.0~~ |
| NOx | 2 | -40.269632 | -73.115445 |  | 4.92 | 4.9223 | 400 | 1.2 | 1.2 |
| NOx | 3 | -40.269632 | -73.11445 |  | 3.61 | 3.6084 | 400 | 0.9 | 0.9 |
| NOx | 4 | -40.262679 | -73.111779 |  | 4.65 | 4.6502 | 400 | 1.2 | 1.2 |
| NOx | 5 | -40.264237 | -73.124765 |  | 0.69 | 0.6903 | 400 | 0.2 | 0.2 |

**Tabla 9: **Concentración CO** **en Receptores Discretos****

| Fase Construcción Concentración Horaria | Col2 | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CO | **N°** | **Coordenadas Receptor** | **Coordenadas Receptor** | **Valor**<br>**Fondo** | **Aporte**<br>**Proyecto**<br>**Horario** | **Total**<br>**(Concentración**<br>**final (situación**<br>**basal más**<br>**aporte**<br>**proyecto)** | **Normativa** | **Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**final** | **Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**aporte del**<br>**proyecto** |
| CO | **N°** | **NLAT_WGS84** | **ELON_WGS84** | ** ug/m3** | **ug/m3** | **ug/m3** | **ug/m3** | **% ** | **% ** |
| CO | 1 | -40.27159 | -73.118011 |  | 3.E-02 | 3.E-02 | 30 | 0.09 | 0.09 |
| CO | 2 | -40.269632 | -73.115445 |  | 3.E-02 | 3.E-02 | 30 | 0.11 | 0.11 |
| CO | 3 | -40.269632 | -73.11445 |  | 3.E-02 | 3.E-02 | 30 | 0.08 | 0.08 |
| CO | 4 | -40.262679 | -73.111779 |  | 3.E-02 | 3.E-02 | 30 | 0.11 | 0.11 |
| CO | 5 | -40.264237 | -73.124765 |  | 5.E-03 | 5.E-03 | 30 | 0.02 | 0.02 |
| CO | 6 | -40.260482 | -73.1078 |  | 2.E-02 | 2.E-02 | 30 | 0.05 | 0.05 |
| CO | 7 | -40.265796 | -73.114816 |  | 8.E-02 | 8.E-02 | 30 | 0.26 | 0.26 |
| CO | 8 | -40.272394 | -73.112981 |  | 1.E-02 | 1.E-02 | 30 | 0.04 | 0.04 |
| CO | 9 | -40.2724 | -73.112407 |  | 1.E-02 | 1.E-02 | 30 | 0.03 | 0.03 |
| **Fase Operación Concentración Horaria** | **Fase Operación Concentración Horaria** | **Fase Operación Concentración Horaria** | **Fase Operación Concentración Horaria** | **Fase Operación Concentración Horaria** | **Fase Operación Concentración Horaria** | **Fase Operación Concentración Horaria** | **Fase Operación Concentración Horaria** | **Fase Operación Concentración Horaria** | **Fase Operación Concentración Horaria** |
| CO | **N°** | **Coordenadas Receptor** | **Coordenadas Receptor** | **Valor**<br>**Fondo** | **Aporte**<br>**Proyecto**<br>**Horario** | **Total**<br>**(Concentración**<br>**final (situación**<br>**basal más**<br>**aporte**<br>**proyecto)** | **Normativa** | **Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**final** | **Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**aporte del**<br>**proyecto** |
| CO | **N°** | **NLAT_WGS84** | **ELON_WGS84** | ** ug/m3** | **ug/m3** | **ug/m3** | **ug/m3** | **% ** | **% ** |
| CO | **1 ** | -40.27159 | -73.118011 |  | 2.E-03 | 2.E-03 | 30 | 0.01 | 0.01 |
| CO | 2 | -40.269632 | -73.115445 |  | 2.E-03 | 2.E-03 | 30 | 0.01 | 0.01 |
| CO | 3 | -40.269632 | -73.11445 |  | 2.E-03 | 2.E-03 | 30 | 0.01 | 0.01 |
| CO | 4 | -40.262679 | -73.111779 |  | 2.E-03 | 2.E-03 | 30 | 0.01 | 0.01 |
| CO | 5 | -40.264237 | -73.124765 |  | 3.E-04 | 3.E-04 | 30 | 0.00 | 0.00 |
| CO | 6 | -40.260482 | -73.1078 |  | 1.E-03 | 1.E-03<br> | 30 | 0.00<br> | 0.00 |
| CO | 7 | -40.265796 | -73.114816 |  | 6.E-03 | ~~6.E-03~~ | 30 | ~~0.02~~ | 0.02 |
| CO | 8 | -40.272394 | -73.112981 |  | 8.E-04 | 8.E-04 | 30 | 0.00 | 0.00 |

**Tabla 10: **Concentración SO2** **en Receptores Discretos****

| Fase Construcción Concentración Horaria | Col2 | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SO2 | **N°** | **Coordenadas Receptor** | **Coordenadas Receptor** | **Valor**<br>**Fondo** | **Aporte**<br>**Proyecto**<br>**Horaria** | **Total**<br>**(Concentración**<br>**final (situación**<br>**basal más**<br>**aporte**<br>**proyecto)** | **Normativa** | **Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**final** | **Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**aporte del**<br>**proyecto** |
| SO2 | **N°** | **NLAT_WGS84** | **ELON_WGS84** | ** ug/m3** | **ug/m3** | **ug/m3** | **ug/m3** | **% ** | **% ** |
| SO2 | 1 | -40.27159 | -73.118011 |  | 8.E-03 | 8.E-03 | 350 | 2.E-03 | 2.E-03 |
| SO2 | 2 | -40.269632 | -73.115445 |  | 1.E-02 | 1.E-02 | 350 | 4.E-03 | 4.E-03 |
| SO2 | 3 | -40.269632 | -73.11445 |  | 1.E-02 | 1.E-02 | 350 | 3.E-03 | 3.E-03 |
| SO2 | 4 | -40.262679 | -73.111779 |  | 1.E-02 | 1.E-02 | 350 | 3.E-03 | 3.E-03 |
| SO2 | 5 | -40.264237 | -73.124765 |  | 2.E-03 | 2.E-03 | 350 | 7.E-04 | 7.E-04 |
| SO2 | 6 | -40.260482 | -73.1078 |  | 6.E-03 | 6.E-03 | 350 | 2.E-03 | 2.E-03 |
| SO2 | 7 | -40.265796 | -73.114816 |  | 5.E-02 | 5.E-02 | 350 | 1.E-02 | 1.E-02 |
| SO2 | 8 | -40.272394 | -73.112981 |  | 4.E-03 | 4.E-03 | 351 | 1.E-03 | 1.E-03 |
| SO2 | 9 | -40.2724 | -73.112407 |  | 4.E-03 | 4.E-03 | 352 | 1.E-03 | 1.E-03 |
| **Fase Operación Concentración Horaria** | **Fase Operación Concentración Horaria** | **Fase Operación Concentración Horaria** | **Fase Operación Concentración Horaria** | **Fase Operación Concentración Horaria** | **Fase Operación Concentración Horaria** | **Fase Operación Concentración Horaria** | **Fase Operación Concentración Horaria** | **Fase Operación Concentración Horaria** | **Fase Operación Concentración Horaria** |
| SO2 | **N°** | **Coordenadas Receptor** | **Coordenadas Receptor** | **Valor**<br>**Fondo** | **Aporte**<br>**Proyecto**<br>**Horaria** | **Total**<br>**(Concentración**<br>**final (situación**<br>**basal más**<br>**aporte**<br>**proyecto)** | **Normativa** | **Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**final** | **Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**aporte del**<br>**proyecto** |
| SO2 | **N°** | **NLAT_WGS84** | **ELON_WGS84** | ** ug/m3** | **ug/m3** | **ug/m3** | **ug/m3** | **% ** | **% ** |
| SO2 | **1 ** | -40.27159 | -73.118011 |  | 8.46E-07 | 8.46E-07 | 350 | 2.42E-07 | 2.42E-07 |
| SO2 | 2 | -40.269632 | -73.115445 |  | 1.50E-06 | 1.50E-06 | 350 | 4.28E-07 | 4.28E-07 |
| SO2 | 3 | -40.269632 | -73.11445 |  | 1.12E-06 | 1.12E-06<br> | 350 | 3.19E-07<br> | 3.19E-07 |
| SO2 | 4 | -40.262679 | -73.111779 |  | 9.98E-07 | ~~9.98E-07~~ | 350 | ~~2.85E-07~~ | 2.85E-07 |
| SO2 | 5 | -40.264237 | -73.124765 |  | 2.34E-07 | 2.34E-07 | 350 | 6.68E-08 | 6.68E-08 |
| SO2 | 6 | -40.260482 | -73.1078 |  | 6.30E-07 | 6.30E-07 | 350 | 1.80E-07 | 1.80E-07 |
| SO2 | 7 | -40.265796 | -73.114816 |  | 4.53E-06 | 4.53E-06 | 350 | 1.30E-06 | 1.30E-06 |
| SO2 | 8 | -40.272394 | -73.112981 |  | 4.41E-07 | 4.41E-07 | 350 | 1.26E-07 | 1.26E-07 |
|  | 9 | -40.2724 | -73.112407 |  | 4.17E-07 | 4.17E-07 | 350 | 1.19E-07 | 1.19E-07 |
| **Fase Abandono ConcentraciónHoraria** | **Fase Abandono ConcentraciónHoraria** | **Fase Abandono ConcentraciónHoraria** | **Fase Abandono ConcentraciónHoraria** | **Fase Abandono ConcentraciónHoraria** | **Fase Abandono ConcentraciónHoraria** | **Fase Abandono ConcentraciónHoraria** | **Fase Abandono ConcentraciónHoraria** | **Fase Abandono ConcentraciónHoraria** | **Fase Abandono ConcentraciónHoraria** |
| SO2 | **N°** | **Coordenadas Receptor** | **Coordenadas Receptor** | **Valor**<br>**Fondo** | **Aporte**<br>**Proyecto**<br>**Horaria** | **Total**<br>**(Concentración**<br>**final (situación**<br>**basal más**<br>**aporte**<br>**proyecto)** | **Normativa** | **Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**final** | **Porcentaje de**<br>**la Norma en**<br>**base a**<br>**concentración**<br>**aporte del**<br>**proyecto** |
| SO2 | **N°** | **NLAT_WGS84** | **ELON_WGS84** | ** ug/m3** | **ug/m3** | **ug/m3** | **ug/m3** | **% ** | **% ** |
| SO2 | 1 | -40.27159 | -73.118011 |  | 8.46E-04 | 8.46E-04 | 350 | 0.000 | 0.000 |
| SO2 | 2 | -40.269632 | -73.115445 |  | 1.50E-03 | 1.50E-03 | 350 | 0.000 | 0.000 |
| SO2 | 3 | -40.269632 | -73.11445 |  | 1.12E-03 | 1.12E-03 | 350 | 0.000 | 0.000 |
| SO2 | 4 | -40.262679 | -73.111779 |  | 9.98E-04 | 9.98E-04 | 350 | 0.000 | 0.000 |
| SO2 | 5 | -40.264237 | -73.124765 |  | 2.34E-04 | 2.34E-04 | 350 | 0.000 | 0.000 |
