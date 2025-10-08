---
title: Sin título
author: Lorena Fernanda Morales Morales
date: D:20190522173920-04'00'
language: es
type: report
pages: 53
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Modelación de Emisiones Atmosféricas DIA “Planta Caleta Bay II.”
-->

# Modelación de Emisiones Atmosféricas DIA “Planta Caleta Bay II.”

## Elaborado por: Lorena Morales M. Asesorías Ambientales y Otros EIRL 22/05/2019

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

## Contenido

1. INTRODUCCIÓN ..........................................................................................................................2

2. OBJETIVOS ..................................................................................................................................3

3. MODELACIÓN DE DISPERSIÓN ATMOSFÉRICA............................................................................4

3.1 Descripción y Justificación del Modelo .............................................................................. 4

3.2 Base Teórica del Modelo utilizado ..................................................................................... 4

3.3 Caracterización Meteorológica .......................................................................................... 6

3.3.1 Análisis Meteorología Observacional..........................................................................7

3.4 Modelo Meteorológico .................................................................................................... 13

3.4.1 Justificación Modelo Meteorológico.........................................................................13

3.4.2 Descripción Modelo Meteorológico .........................................................................13

3.5 Análisis De Incertidumbre................................................................................................ 21

3.6 Características Del Dominio De Modelación Y Su Entorno .............................................. 22

3.6.1 Características de Dominio .......................................................................................22

3.7 Datos topográficos y uso de suelo ................................................................................... 23

3.8 Análisis y Caracterización de Calidad de Aire de la zona del proyecto............................. 24

3.9 Fuentes De Emisión ......................................................................................................... 25

3.10 Receptores....................................................................................................................... 27

4.RESULTADOS MODELACIÓN CALIDAD DEL AIRE ............................................................................28

4.1 Determinación Área de Influencia ................................................................................... 28

4.1.1 Concentración MP10 ..................................................................................................29

4.1.2 Concentración MP2.5 ...............................................................................................34

4.1.3 Concentración CO .....................................................................................................39

4.1.4 Concentración NOx ...................................................................................................44

4. CONCLUSIÓN ............................................................................................................................49

5. REFERENCIAS ............................................................................................................................51

1

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

## 1. INTRODUCCIÓN

El presente informe contiene los resultados de la modelación de calidad del aire **para material**

**particulado (MP10, MP2.5) y gases** emitidos por las actividades de construcción y operación del

Proyecto _**DIA “Planta Caleta Bay II”**_ .

Se contempla específicamente verificar que el proyecto no genere alguno de los efectos,

características o circunstancias indicadas en el artículo 5 del D.S. N° 40/2012 del MMA, en cuanto

a calcular el aporte en concentración anual y diario de material particulado MP10, MP2.5 y gases

emitidos por las actividades a realizar en el proyecto, sobre los receptores sensibles identificados

por el Proponente, adjuntando las isolíneas de concentración que permiten observar la zona de

máximo impacto del proyecto.

Para la línea de base meteorológica se realizó una caracterización general del clima y la

meteorología imperante en la zona. Para ello, se utilizó meteorología modelada por el modelo

meteorológico WRF adquirida por medio de Lakes Environmental, adicionalmente se recurrió a la

recopilación de antecedentes bibliográficos tanto de organismos públicos como privados.

2

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

## 2. OBJETIVOS

El objetivo general del estudio es modelar las emisiones atmosféricas para evaluar el impacto en

la calidad del aire, para la Fase de Construcción y Fase de Operación del Proyecto.

Para lograr el objetivo principal del presente informe, se plantean objetivos específicos que

apoyan la evaluación que se realizó. Así los objetivos específicos son:

 - Realizar una caracterización meteorológica, con el fin de tener un conocimiento de los

fenómenos meteorológicos y climáticos del área en la que tendrá influencia el Proyecto.

 - Realizar un análisis de la línea de base de calidad del aire, en el cual se busca conocer los

niveles basales de concentración de material particulado (MP10, MP2.5 y gases)

característicos del área del proyecto.

 - Evaluar el impacto sobre la calidad del aire mediante la implementación del modelo de

calidad del aire, en las fases construcción y de operación del proyecto.

3

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

## 3. MODELACIÓN DE DISPERSIÓN ATMOSFÉRICA

Por medio de la ejecución de una serie de etapas, se logró determinar la estimación de las

concentraciones en los escenarios definidos, para un dominio determinado de receptores de

interés y que permitió, además, la generación de curvas de isoconcentración generadas a través

de una malla con equiespaciado cada 1 kilómetro.

La metodología se basa en las recomendaciones definidas en la Guía de Uso de Modelos de

Calidad de Aire en el SEIA, año 2014. En este caso en particular, se utiliza el modelo CALPUFF

siguiendo la recomendación de la misma Guía de Uso de Modelos de Calidad del Aire, utilizando

como criterio principal la mayoría de los receptores de interés, que se ubican dentro del área de

modelación y que constituye el área de influencia de la componente.

### 3.1 Descripción y Justificación del Modelo

Considerando lo indicado en la Guía para el uso de Modelos de Calidad de Aire en el SEIA y en el

marco de la Evaluación Ambiental del Proyecto _**“Planta Caleta Bay II”,**_ se considera pertinente la

presentación de la Modelación de emisiones atmosféricas generadas durante la fase de

construcción y operación del proyecto, como herramienta para evaluar el impacto de dichas

emisiones sobre el recurso aire, y el consecuente impacto sobre otros recursos naturales

renovables y la salud de las personas.

Según lo establecido por la Guía para el uso de Modelos de Calidad del Aire en el SEIA, la selección

del modelo de Calidad del Aire utilizado en el presente estudio se realizó debido a la topografía

compleja del área donde se emplaza el proyecto y al alcance de las emisiones de este. Por esta

razón, fue usado el modelo CALPUFF explicado a continuación.

### 3.2 Base Teórica del Modelo utilizado

La simulación del aporte del proyecto a las concentraciones de contaminantes se realizará

mediante el modelo CALPUFF, recomendado por la U. S. EPA para la evaluación de dispersión de

contaminantes desde fuentes continuas.

CALPUFF es un sistema de modelación avanzado para calidad del aire que considera además, la

meteorología de carácter no permanente. Su desarrollo estuvo a cargo del Sigma Research

Corporation mientras que su actual mantenimiento es responsabilidad del Atmospheric Studies

4

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

Group de TRC Solutions. Debido a su desempeño, CALPUFF fue catalogado por la USEPA como

modelo recomendado para la evaluación del impacto en la calidad del aire de distintos tipos de

proyectos, especialmente, de aquellos donde es necesario considerar la variación en el tiempo y

en el espacio de las condiciones meteorológicas y su incidencia en el transporte, transformación y

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

 - Modela contaminantes de forma simultánea fuentes de diverso tipo y que modifican su

nivel de actividad a lo largo del tiempo.

Permite diferenciar entre contaminantes inertes y aquellos que experimentan transformaciones

de primer orden.

5

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

### 3.3 Caracterización Meteorológica

Lo que busca la caracterización meteorológica es realizar una descripción cualitativa de la situación

meteorológica y topográfica del lugar. De acuerdo a los lineamientos indicados en la Guía de Uso

de modelos, el estudio de los procesos desde la mesoescala hasta la escala sinóptica, y cómo éstos

influyen en los procesos de transporte, dispersión y transformación de contaminantes a distintas

escalas temporales es lo óptimo para poder incluir opciones con menor propagación de error en la

estimación de las concentraciones. Se utilizó meteorología modelada por el modelo

meteorológico WRF e ingresada en modelo CALPUFF.

Los datos Meteorológicos observados, fueron tomados desde Estación Meteorológica, Estación

Mirasol, administrada por el Ministerio de Medio Ambiente

El análisis se realizó para el periodo comprendido entre enero de 2017 a diciembre de 2017, para

la estación Mirasol. La siguiente imagen, muestra la ubicación de la estación meteorológica

considerada en el análisis:

**Imagen N°1: Localización Estación Meteorológica**

|Nombre Estación|Escuela Mirasol|
|---|---|
|~~**Coordenada Este** ~~<br>|~~41,47944~~<br>|
|~~**Coordenada Norte**~~|~~72,96889~~|

Fuente: Elaboración desde Google Earth a partirde

[https://sinca.mma.gob.cl/index.php/estacion/index/id/63](https://sinca.mma.gob.cl/index.php/estacion/index/id/63)

6

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

**3.3.1** **Análisis Meteorología Observacional**

La información meteorológica de la Estación Mirasol, incluye antecedentes del periodo 2017,

abarcando desde Enero a Diciembre 2017, en forma horaria.

_**3.3.1.1**_ _**Rosa de los Vientos**_

El análisis del comportamiento de los vientos observados en la Estación Mirasol, se presenta a

continuación para los meses de Enero a Diciembre de 2017. Este análisis se realizó con el fin de

comprender la distribución de velocidades y la frecuencia de ocurrencia de las diferentes

direcciones de viento.

Gráfico N°1.1: Serie de tiempo Dirección de Viento (soplando desde) observadas en las Estación

Escuela Mirasol, año 2017.

7

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

Gráfico N°1.2: Serie de tiempo Dirección de Viento (soplando desde) observadas en las Estación

Escuela Mirasol, Enero-Marzo año 2017.

Gráfico N°1.3: Serie de tiempo Dirección de Viento (soplando desde) observadas en las Estación

Escuela Mirasol, Abril-Junio año 2017.

8

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

Gráfico N°1.4: Serie de tiempo Dirección de Viento (soplando desde) observadas en las Estación

Escuela Mirasol, Julio-Septiembre año 2017.

Gráfico N°1.5: Serie de tiempo Dirección de Viento (soplando desde) observadas en las Estación

Escuela Mirasol, Octubre-Diciembre año 2017.

9

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

_**3.3.1.2**_ _**Velocidad de Vientos**_

**Series de Tiempo - Velocidad del Viento**

En esta sección se presentan series de tiempo de Velocidad de Viento observados durante los

meses de Enero a Diciembre del año 2017 en la estación en estudio. Estos gráficos permiten

realizar un análisis cualitativo de los datos en términos de completitud de la serie y periodos

faltantes, valores fuera de rango o fallas técnicas de los equipos.

Como se aprecia en estas figuras, la trayectoria de la serie de velocidad de viento observada

durante los meses analizados no presenta ausencia de registros para los periodos seleccionados

para análisis. En estas figuras es posible observar también, que en la estación de monitoreo se

presenta un comportamiento estacional, con velocidades de viento promedios de 0,6 m/s

aproximadamente, observándose un valor máximo de 2,1 m/s.

Gráfico N°2.1: Serie de tiempo Velocidad de Viento observadas en las Estación Mirasol, Enero

Diciembre 2017.

10

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

Gráfico N°2.2: Serie de tiempo Velocidad de Viento observadas en las Estación Mirasol, Enero

Marzo 2017.

Gráfico N°2.3: Serie de tiempo Velocidad de Viento observadas en las Estación Mirasol, AbrilJunio 2017.

11

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

Gráfico N°2.4: Serie de tiempo Velocidad de Viento observadas en las Estación Mirasol, Julio

Septiembre 2017.

Gráfico N°2.5: Serie de tiempo Velocidad de Viento observadas en las Estación Mirasol, Octubre

Diciembre 2017.

12

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

### 3.4 Modelo Meteorológico

**3.4.1** **Justificación Modelo Meteorológico**

Según lo establecido por la Guía para el uso de Modelos de Calidad del Aire en el SEIA, la selección

del modelo meteorológico utilizado en el presente estudio se realizó fundamentándose en las

condiciones de topografía compleja del área entorno al proyecto. Para esto, la guía recomienda un

modelo que permita simular una meteorología heterogénea.

La meteorología considerada por el modelo WRF corresponde a los datos modelados

proporcionados Lakes Environmental en período de 1 enero 2017 a 31 diciembre 2017. Esta

información fue utilizada en el modelo de calidad de aire CALPUFF.

**3.4.2** **Descripción Modelo Meteorológico**

La configuración de corrida se hizo desde la hora 1 del mes de enero del año 2017 hasta la hora 23

del día 31 de diciembre de 2017. Se configuró para la modelación horaria la zona UTC-4, y el paso

de tiempo es horario con un total de 8760 horas.

El modelo de investigación y pronóstico del tiempo (Weather Research and Forecasting - WRF) es

un sistema de predicción numérico de mesoscala de nueva generación, diseñado para servir

pronósticos operacionales y para estudio de la atmósfera.

|Tabla 3.5: Características de los Datos del Modelo Meteorológico WRF Usados para la Evaluación del Proyecto|Col2|
|---|---|
|Característica de los Datos del Modelo WRF|Característica de los Datos del Modelo WRF|
|- Periodo<br>- Latitud<br>- Longitud<br>- Tamaño del Dominio<br>- Resolución<br>- Zona Horaria<br> - Localización|Jan 01, 2017 - Dec 31,<br>41.495464 S<br>73.034447 W<br>50x50 km<br>1 km<br>-18 - Site Time Zone: UTC - 4<br>- Chile|

13

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

Ejemplos de los campos de vientos generados por WRF se presentan en Figura 2, para el año 2017

Figura N°2: Ejemplo de Campos de Vientos generados por el Modelo WRF en el Dominio

Fuente: Elaboración propia a partir de CALMET

La información meteorológica de la meterología modelada para el periodo 2017, abarcando desde

Enero a Diciembre 2017, se presenta a continuación;

14

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

_**3.4.2.1**_ _**Rosa de los Vientos**_

La meterología anual se presenta en la siguiente rosa de vientos;

Gráfico N°3.4.2.1 : Serie de tiempo Dirección de Viento (soplando desde) modelada (WRF)

año 2017.

15

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

Gráfico N°3.4.2.2 : Serie de tiempo Dirección de Viento (soplando desde) modelada (WRF)

Enero a Marzo del año 2017.

Gráfico N°3.4.2.3 : Serie de tiempo Dirección de Viento (soplando desde) modelada (WRF)

Abril a Junio del año 2017.

16

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

Gráfico N°3.4.2.4 : Serie de tiempo Dirección de Viento (soplando desde) modelada (WRF)

Julio a Septiembre del año 2017.

Gráfico N°3.4.2.5 : Serie de tiempo Dirección de Viento (soplando desde) modelada (WRF)

Octubre a Diciembre del año 2017.

17

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

Gráfico N°3.4.2.6: Serie de tiempo Velocidad de Viento modelada (WRF) Año 2017.

Gráfico N°3.4.2.7: Serie de tiempo Velocidad de Viento modelada (WRF) Enero a Marzo Año 2017.

18

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

Gráfico N°3.4.2.6: Serie de tiempo Velocidad de Viento modelada (WRF) Abril a Junio Año 2017.

Gráfico N°3.4.2.6: Serie de tiempo Velocidad de Viento modelada (WRF) Julio a Septiembre Año

2017.

19

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

Gráfico N°3.4.2.6: Serie de tiempo Velocidad de Viento modelada (WRF) Octubre a Diciembre Año

2017.

20

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

### 3.5 Análisis De Incertidumbre

Para realizar el análisis de incertidumbre se siguieron las recomendaciones que señaladas en la

“Guía para el uso de modelos de calidad del aire en el SEIA” (SEA, 2012). Esta guía, en el acápite 7,

menciona que cualquier modelo representa una aproximación a la realidad y sus resultados tienen

incertidumbres asociadas, las cuales se expresan a través de diferencias entre lo estimado y lo

observado.

La meteorología observada y modelada se evalúa comparando la velocidad de los vientos

generados por el modelo con las observaciones locales, miente la determinación del sesgo,

coeficiente de correlación y el error medio cuadrático.

Las definiciones matemáticas de cada uno de los estadísticos utilizados se presentan a

continuación:

N

Sesgo= [1]

N [∑(M] [i] [−O] [i] [)]

i

N

RMSE= √ [1]

N

N [∑(M] [i] [−O] [i] [)] [2]

i

N ∑ Ni=1 O i M i −∑ Ni=1 O i ∑ Ni=1 M i
r=

Ni=1 O i

√(N ∑

2 −(∑ Ni=1 O i )

2 N M
)(N∑ i=1 i

Ni=1 O i2 −(∑ Ni=1 O i ) 2 )(N∑ Ni=1 M i2 −(∑ Ni=1 M i ) 2 )

2 −(∑ Ni=1 M i )

Donde O i corresponde a las observaciones; M i corresponde a los valores modelados; e i

corresponde a cada uno de los N valores horarios de las variables analizadas para la estación.

**Tabla N°3.5.1: Comparación vientos observados vs modelados (WRF)**

|Estación|Sesgo|RMSE|r|
|---|---|---|---|
|Escuela Mirasol|2,47|9,62|0,67|

Tanto el sesgo como RMSE indican diferencias entre el modelo y los datos observados de la

estación de monitoreo, en donde los datos modelados poseen una asimitría positiva, por cuanto

presentan un coeficiente de correlación cercano a 1, por lo que existe una correlación positiva

directamente proporcional.

Del gráfico anterior, se observa que los registros de la estación meterológica Escuela Mirasol

presenta un comportamiento similar a los registrados por el archivo WRF.

21

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

### 3.6 Características Del Dominio De Modelación Y Su Entorno

**3.6.1** **Características de Dominio**

El dominio de modelación considerado para el presente proyecto corresponde a una grilla

rectangular de 60 km por 60 km, compuesta por celdas de 1 km por lado. En la Tabla 17 se

presentan las características del área correspondiente al dominio de modelación. El dominio

elegido abarca el área de influencia del proyecto para los distintos componentes ambientales que

pueden verse afectados por las emisiones de éste.

El dominio de modelación está definido por la siguiente imagen:

**Imagen N°2: Dominio de Modelación**

Fuente: Elaboración propia a partir de CALPUFF

22

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

### 3.7 Datos topográficos y uso de suelo

La topografía de la zona en análisis se obtiene de la Misión de Radar Topográfico del

Transbordador Espacial de la NASA1 (SRTM en inglés), que consiste en un modelo digital de

elevación de alta resolución que describe la altimetría de una zona mediante un conjunto de cotas

para una ubicación dada con una aproximadamente de 90 metros.

En la siguiente imagen se muestran las elevaciones obtenidas del área de influencia.

Imagen N°3: Topografía del dominio de modelación

Fuente Elaboración propia a partir de CALPUFF

Los tipos de suelo presentes en el dominio son de gran importancia para fines de modelación, ya

que determinan los procesos de transferencia de calor, afectando los balances de energía

superficial, elemento fundamental para poder estimar la altura de mezclado en los distintos

períodos en evaluación. Además de esto, tienen efecto en el viento a nivel de superficie, ya que

según el tipo de cobertura que se tenga, la resistencia que se ejerce sobre las corrientes de aire.

23

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

### 3.8 Análisis y Caracterización de Calidad de Aire de la zona del proyecto

Para establecer la situación basal de la calidad de aire del área de influencia del Proyecto se

tomaron los datos de estación más cercana al proyecto, denominada estación de monitoreo de

calidad de aire “Mirasol”, emplazada a 6 kilómetros al noroeste del proyecto, para el período

comprendido entre Enero de 2017 y Diciembre de 2017. Cabe señalar que dicha estación sólo

dispone de información actualizada para MP2.5.

Figura N°3: Ubicación Estación de Monitoreo Calidad de Aire

Tabla N°3.6: Concentración (ug/m3) promedio de contaminantes en EMRP durante el año 2017

MP2.5 (ug/m3)

concentración

promedio 24

hrs

PM 10 (ug/m3)

concentración

promedio 24

hrs

SO2(ug/m3)

concentración

promedio 24 hrs

CO(ug/m3)

concentración

promedio 24 hrs

NOX(ug/m3)

concentración

promedio 24 hrs

Fuente: Registro Estación Mirasol

24

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

Figura N°3.1: Concentración promedio 24 Hrs de MP2.5 (ug/m3)

Fuente: Elaboración propia a partir de datos de Estación Mirasol

### 3.9 Fuentes De Emisión

Para evaluar la dispersión atmosférica de las emisiones provenientes de la planta, se consideran 2

Escenarios de modelación, de acuerdo a la siguiente información;

Tabla N°3.7: Tasa de Emisión según Escenario de Modelación Fase Construcción

|Fuente emisora|MP10<br>(Ton/año)|MP2,5<br>(Ton/año)|NOx<br>(Ton/año)|CO (Ton/año)|SOx<br>(Ton/año)|
|---|---|---|---|---|---|
|Escarpe + Transferencia de<br>Materiales|0,0071|0,0032|-|-|-|
|Gases Circulación de<br>Vehículos en Ruta|0,0120|0,0025|-|-|-|
|Maquinaria utilizada en la<br>Construcción|0,0081|-|0,1836|0,0233|-|
|Re suspendido en Caminos<br>Pavimentados|0,0121|0,0025|-|-|-|
|Combustión Vehículos|0,0000|-|0,0003|0,0001|0,0000|
|Total Emisiones (T/año)|0,0393|0,0083|0,1838|0,0233|0,0000|

25

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

Tabla N°3.7.1: Tasa de Emisión según Escenario de Modelación Fase Operación

|Fuente emisora|MP10<br>(Ton/año)|MP2,5<br>(Ton/año)|NOx<br>(ton/año|CO<br>(Ton/año)|SOx<br>(Ton/año)|
|---|---|---|---|---|---|
|Gases Circulación de<br>Vehículos en Ruta|15,3860|13,7700|-|-|-|
|Equipos electrógenos|0,5900|-|20,2360|4,6260|0,0010|
|Re suspendido en Caminos<br>Pavimentados|0,4340|0,0915|-|-|-|
|Combustión Vehículos|0,0003||0,0161|0,0039|0,0004|
|Total Emisiones (T/año)|16,4103|13,8615|20,2521|4,6299|0,0014|

26

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

### 3.10 Receptores

La ubicación de los receptores se considera una grilla de receptores de 60 km x 60 km con

equispaciado de 1 km entre celdas.

Figura N°3.6: Emplazamiento Grilla de Receptores

Fuente: Elaboración propia a partir de GoogleEarth

Figura N°3.6: Emplazamiento Receptores Discretos

Fuente: Elaboración propia a partir de GoogleEarth

27

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

### 4.RESULTADOS MODELACIÓN CALIDAD DEL AIRE

En la siguiente sección se entregan las concentraciones obtenidas utilizando el modelo

meteorológico de meso escala Weather Research Forecasting Model (WRF), como insumo para

CALPUFF View. De esta forma fue posible obtener las concentraciones de los contaminantes en

cada receptor según Escenario evaluado (Fase Construcción y Fase de Operación). Estos resultados

no superan las concentraciones máximas referidas a las normas de calidad primaria para los

contaminantes MP10, MP2.5, CO y NOx respectivamente.

### 4.1 Determinación Área de Influencia

En base a la dispersión de los contaminantes evaluados, se determina como Área de Influencia,

aquel espacio comprendido por la dispersión del contaminante mayormente desplazado,

correspondiente a MP2,5 en su Concentración Anual, precisamente aquella área en la cual se

registra mayor concentración, en una extensión aproximada de 2,3 Km para el eje Este-Oeste y
2,9 Km en el eje Norte-Sur, equivalente a 4,9 Km2. Para mayor detalle se presenta gráfica del área

de Influencia, según lo recién indicado;

**Gráfica N°4.1: Área de Influencia Componente Calidad de Aire**

Elaboración propia

28

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

**4.1.1** **Concentración MP10**

El flujo de contaminantes se concentra en la zona inmediata al proyecto, desplazándose la pluma

de dispersión hacia el sector sureste observándose una concentración máxima en los receptores

N°3 y N°4 para la fase de Operación, y en menor concentración para el receptor N°1 en la fase de

Operación concentración anual. La concentraciones máximas no superan la norma primaria de

calidad del aire para MP2.5.

Las coordenadas y concentraciones en períodos de concentración anual y diaria de receptores

discretos se presenta en la siguiente tabla.

**Tabla N°4.1: Concentración MP10** **en Receptores Discretos**

|DS 59 del MINSEGPRES, Norma primaria de<br>calidad del aire para MP10;|Col2|Col3|Valor normado<br>Concentración Diaria|Col5|Valor normado Concentración|Col7|
|---|---|---|---|---|---|---|
|**_DS 59 del MINSEGPRES, Norma primaria de_**<br>**_calidad del aire para MP10;_**|**_DS 59 del MINSEGPRES, Norma primaria de_**<br>**_calidad del aire para MP10;_**|**_DS 59 del MINSEGPRES, Norma primaria de_**<br>**_calidad del aire para MP10;_**|<br>**_Valor normado_**<br>**_Concentración Diaria_**|<br>**_Valor normado_**<br>**_Concentración Diaria_**|**_ Anual_**|**_ Anual_**|
|**_DS 59 del MINSEGPRES, Norma primaria de_**<br>**_calidad del aire para MP10;_**|**_DS 59 del MINSEGPRES, Norma primaria de_**<br>**_calidad del aire para MP10;_**|**_DS 59 del MINSEGPRES, Norma primaria de_**<br>**_calidad del aire para MP10;_**|<br>**_150 ug/m3N_**|<br>**_150 ug/m3N_**|**_50 ug/m3N_**|**_50 ug/m3N_**|
|**_N°_**|**_Coordenadas_**<br>**_Receptor_**|**_Coordenadas_**<br>**_Receptor_**|<br>**_Aporte Proyecto_**<br>**_Concentración Diaria_**|<br>**_Aporte Proyecto_**<br>**_Concentración Diaria_**|**_Aporte Proyecto_**<br>**_Concentración Anual_**|**_Aporte Proyecto_**<br>**_Concentración Anual_**|
|**_N°_**|**_Coordenadas_**<br>**_Receptor_**|**_Coordenadas_**<br>**_Receptor_**|<br>**_Fase_**<br>**_Operación_**|**_Fase_**<br>**_Construcción_**|**_Fase_**<br>**_Operación_**|**_Fase_**<br>**_Construcción_**|
|**_N°_**|**_ x_**|**_ y_**|<br>**_ug/m3_**|**_ug/m3_**|**_ug/m3_**|**_ug/m3_**|
|1|**664202**|**5404429**|**6,99**|**1,19E-06**|**3,16**|**1,64E-07**|
|2|**663895**|**5404389**|**9,87**|**3,96E-06**|**1,84**|**5,60E-07**|
|3|**663797**|**5404327**|**10.2**|**4,74E-06**|**1,96**|**7,60E-07**|
|4|**663698**|**5404275**|**10,2**|**4,27E-06**|**1,89**|**5,46E-07**|
|5|**663747**|**5404058**|**6,48**|**4,00E-06**|**2,82**|**3,59E-07**|
|6|**663879**|**5403922**|**4,35**|**3,90E-06**|**1,66**|**9,50E-07**|

Para mayor comprensión a continuación se presentan imágenes según los receptores evaluados

en sus diversos períodos, junto a su pluma de dispersión representada por isoconcentraciones

que reflejan el resultado de la modelación.

29

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

Gráfica N°4.1: Concentración MP10 Concentración Diaria Fase Operación

30

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

Gráfica N°4.2: Concentración MP10 Concentración Anual Fase Operación

31

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

Gráfica N°4.3: Concentración MP10 Concentración Diaria Fase Construcción

32

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

Gráfica N°4.1: Concentración MP10 Concentración Anual Fase Construcción

33

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

**4.1.2** **Concentración MP2.5**

El flujo de contaminantes se concentra en la zona inmediata al proyecto, desplazándose la pluma

de dispersión hacia el sector sureste observándose una concentración máxima en el receptor N°3

para la fase de Operación, y en menor concentración para el receptor N°1 en la fase de Operación

concentración anual. La concentraciones máximas no superan la norma primaria de calidad del

aire para MP2.5.

Para este contaminante se considera una situación basal en concentración diaria de 30.2 (ug/m3) [1],

que sumado a la concentración máxima arrojada por el modelo, correspondiente al receptor N°3,
la concentración final [2] sobre éste alcanzaría los 39,2 (ug/m3). Cabe señalar que dicho valor se

encuentra bajo el límite establecido en DS 12/11 del MMA, Norma primaria de calidad del aire

para MP2.5, por cuanto, el proyecto no generaría eventos de latencia ni saturación sobre la zona

modelada, toda vez, que a nivel porcentual equivale al 78% del valor normado, ello durante el

peor escenario evaluado (Fase de Operación y Construcción).

Las coordenadas y concentraciones en períodos de concentración anual y diaria de receptores

discretos se presenta en la siguiente tabla.

**Tabla N°4.2: Concentración MP2,5** **en Receptores Discretos**

|DS 12/11 del MMA, Norma primaria de<br>calidad del aire para MP2.5;|Col2|Col3|Valor normado Concentración<br>Diaria|Col5|Valor normado Concentración<br>Anual|Col7|
|---|---|---|---|---|---|---|
|**_DS 12/11 del MMA, Norma primaria de_**<br>**_calidad del aire para MP2.5;_**|**_DS 12/11 del MMA, Norma primaria de_**<br>**_calidad del aire para MP2.5;_**|**_DS 12/11 del MMA, Norma primaria de_**<br>**_calidad del aire para MP2.5;_**|**_50 ug/m3N_**|**_50 ug/m3N_**|**_20 ug/m3N_**|**_20 ug/m3N_**|
|**_N°_**|**_Coordenadas_**<br>**_ Receptor_**|**_Coordenadas_**<br>**_ Receptor_**|**_Aporte Proyecto_**<br>**_Concentración Diaria_**|**_Aporte Proyecto_**<br>**_Concentración Diaria_**|**_Aporte Proyecto_**<br>**_Concentración Anual_**|**_Aporte Proyecto_**<br>**_Concentración Anual_**|
|**_N°_**|**_Coordenadas_**<br>**_ Receptor_**|**_Coordenadas_**<br>**_ Receptor_**|**_Fase_**<br>**_Operación_**|**_Fase_**<br>**_Construcción_**|**_Fase_**<br>**_Operación_**|**_Fase_**<br>**_Construcción_**|
|**_N°_**|** x**|** y**|**_ug/m3_**|**_ug/m3_**|**_ug/m3_**|**_ug/m3_**|
|1|**664202**|**5404429**|**6,12**|**2,52E-07**|**2,77**|**3,47E-08**|
|2|**663895**|**5404389**|**8,64**|**8,37E-07**|**1,61**|**1,18E-07**|
|3|**663.797**|**5404327**|**8,94**|**1,00E-06**|**1,71**|**1,60E-07**|
|4|**663698**|**5404275**|**9,00**|**9,02E-07**|**1,66**|**1,15E-07**|
|5|**663747**|**5404058**|**5,68**|**8,45E-07**|**2,48**|**7,59E-08**|
|6|**663879**|**5404922**|**3,82**|**8,25E-07**|**1,45**|**2,00E-07**|

Para mayor comprensión a continuación se presentan imágenes según los receptores evaluados

en sus diversos períodos, junto a su pluma de dispersión representada por isoconcentraciones

que reflejan el resultado de la modelación.

1 Según registros de SINCA. MMA Estación Mirasol. Puerto Montt.
2 Concentración final (concentración estimada por el modelo más la situación basal)

34

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

Gráfica N°4.2.1: Concentración MP2.5 Concentración Diaria Fase Operación

35

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

Gráfica N°4.2.2: Concentración MP2.5 Concentración Anual Fase Operación

36

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

Gráfica N°4.2.3: Concentración MP2.5 Concentración Diaria Fase Construcción

37

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

Gráfica N°4.2.4: Concentración MP2.5 Concentración Anual Fase Construcción

38

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

**4.1.3** **Concentración CO**

El flujo de contaminantes se concentra en la zona inmediata al proyecto, desplazándose la pluma

de dispersión hacia el sector sureste observándose una concentración máxima en el receptor N°4

para la fase de Operación en concentración diaria, y en menor concentración para el receptor N°3

y N°4 de la fase de Operación concentración anual. La concentraciones máximas no superan la

norma primaria de calidad del aire para CO.

Las coordenadas y concentraciones en períodos de concentración anual y diaria de receptores

discretos se presenta en la siguiente tabla.

**Tabla N°4.3: Concentración CO en Receptores Discretos**

|DS 115 del MINSEGPRES,<br>Norma primaria de calidad<br>del aire para CO;|Col2|Col3|Valor normado Concentración Horaria<br>30 mg/m3N|Col5|Valor normado Concentración 8 Horas<br>10 mg/m3N|Col7|
|---|---|---|---|---|---|---|
|**_N°_**|**_Coordenadas_**<br>**_Receptor_**|**_Coordenadas_**<br>**_Receptor_**|**_Aporte Proyecto Concentración Horaria_**|**_Aporte Proyecto Concentración Horaria_**|**_Aporte Proyecto Concentración 8 Horas_**|**_Aporte Proyecto Concentración 8 Horas_**|
|**_N°_**|**_Coordenadas_**<br>**_Receptor_**|**_Coordenadas_**<br>**_Receptor_**|**_Fase Operación_**<br>**_mg/m3_**|**_Fase Construcción_**<br>**_mg/m3_**|**_Fase Operación_**<br>**_mg/m3_**|**_Fase Construcción_**<br>**_mg/m3_**|
|**_N°_**|**_x _**|**_y _**|**_y _**|**_y _**|**_y _**|**_y _**|
|1|**664202**|**5404429**|**5,04E-05**|**4,36E-09**|**2,82E-05**|** 1,69E-09**|
|2|**663895**|**5404389**|**6,91E-05**|**9,21E-09**|**3,96E-05**|**4,51E-09**|
|3|**663.797**|**5404327**|**7,69E-05**|**8,79E-09**|**4,42E-05**|**4,19E-09**|
|4|**663698**|**5404275**|**8,00E-05**|**7,66E-09**|**4,46E-05**|**4,41E-09**|
|5|**663747**|**5404058**|**5,81E-05**|**4,74E-09**|**3,11E-05**|**3,96E-09**|
|6|**663879**|**5404922**|**3,52E-05**|**1,05E-08**|** 2,23E-05**|**5,21E-09**|

Para mayor comprensión a continuación se presentan imágenes según los receptores evaluados

en sus diversos períodos, junto a su pluma de dispersión representada por isoconcentraciones

que reflejan el resultado de la modelación.

39

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

Gráfica N°4.3.1 Concentración Horaria CO Fase Operación

40

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

Gráfica N°4.3.2 Concentración 8 Horas CO Fase Operación

41

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

Gráfica N°4.3.3 Concentración Horaria CO Fase Construcción

42

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

Gráfica N°4.3.4 Concentración 8 Horas CO Fase Construcción

43

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

**4.1.4** **Concentración NOx**

El flujo de contaminantes se concentra en la zona inmediata al proyecto, desplazándose la pluma

de dispersión hacia el sector sureste observándose una concentración máxima en el receptor N°4

para la fase de Operación concentración diaria, y en menor concentración para el receptor N°1 en

la fase de Operación concentración anual. La concentraciones máximas no superan la norma

primaria de calidad del aire para NOx.

Las coordenadas y concentraciones en períodos de concentración anual y diaria de receptores

discretos se presenta en la siguiente tabla.

**Tabla N°4.4: Concentración NOx en Receptores Discretos**

|DS 115 del MINSEGPRES, Norma primaria<br>de calidad del aire para NOx|Col2|Col3|Valor normado Concentración<br>Horaria<br>400 ug/m3N|Col5|Valor normado Concentración<br>Anual<br>100 ug/m3N|Col7|
|---|---|---|---|---|---|---|
|**_N°_**|**_Coordenadas_**<br>**_Receptor_**|**_Coordenadas_**<br>**_Receptor_**|**_Aporte Proyecto Concentración_**<br>**_Horaria_**|**_Aporte Proyecto Concentración_**<br>**_Horaria_**|**_Aporte Proyecto Concentración_**<br>**_Anual_**|**_Aporte Proyecto Concentración_**<br>**_Anual_**|
|**_N°_**|**_Coordenadas_**<br>**_Receptor_**|**_Coordenadas_**<br>**_Receptor_**|**_Fase Operación_** <br>**_ug/m3_**|**_Fase Construcción_** <br>**_ug/m3_**|**_Fase Operación_**<br>**_ug/m3_**|**_Fase Construcción_**<br>**_ug/m3_**|
|**_N°_**|**_x _**|**_y _**|**_y _**|**_y _**|**_y _**|**_y _**|
|1|**664202**|**5404429**|**0,20**|**3,44E-05**|**0,032**|**7,70E-07**|
|2|**663895**|**5404389**|**0,28**|**7,26E-05**|**0,018**|**2,62E-06**|
|3|**663.797**|**5404327**|**0,31**|**6,93E-05**|**0,019**|**3,55E-06**|
|4|**663698**|**5404275**|**0,33**|**6,04E-05**|**0,019**|**2,55E-06**|
|5|**663747**|**5404058**|**0,23**|**3,74E-05**|**0,028**|**1,68E-06**|
|6|**663879**|**5404922**|**0,14**|**8,34E-05**|**0,016**|**4,44E-06**|

Para mayor comprensión a continuación se presentan imágenes según los receptores evaluados

en sus diversos períodos, junto a su pluma de dispersión representada por isoconcentraciones

que reflejan el resultado de la modelación.

44

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

Gráfica N°4.4.1 Concentración Horaria NOx Fase Operación

45

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

Gráfica N°4.4.2 Concentración Anual NOX Fase Operación

46

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

Gráfica N°4.4.3 Concentración Horaria NOX Fase Construcción

47

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

Gráfica N°4.4.4 Concentración Anual NOx Fase Construcción

48

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

## 4. CONCLUSIÓN

A partir de las modelaciones realizadas con respecto a las emisiones atmosféricas para las fases de
Construcción y Operación, se presentan las siguientes conclusiones:

- Para la determinación de la situación basal de la calidad del aire de los receptores evaluados, se
consideró el registro existente en la Estación de Monitoreo Mirasol ubicada en la comuna de
Puerto Montt, por considerarse aquella más cercana al proyecto con registros actualizados [3] .

- El flujo de contaminantes se concentra en la zona inmediata dispersándose hacia el sector
sureste. Las concentraciones obtenidas del modelo corresponden a;

 - Para el caso del contaminante MP10, se observa una concentración diaria máxima de 10,2
ug/m 3 de MP10 en los receptores N°3 y 41 para la fase de Operación. En menor
concentración para el receptor N°1 en la fase de Operación en concentración anual (3,16
ug/m 3 ).

 - En relación al MP2.5 se registra una concentración máxima diaria de 9 ug/m 3 en el
receptor N°4 para la fase de Operación, mientras que para la concentración anual de 2,77
ug/m3. Cabe señalar que, para este compuesto se considera una situación basal en
concentración diaria de 30.2 ug/m3 que sumado a la concentración máxima en el receptor
N°1, alcanzaría una concentración final de 39 ug/m 3 . Dicho valor se encuentra bajo el
límite establecido en DS 12/11 del MMA, Norma primaria de calidad del aire para MP2.5,
por cuanto, el proyecto no generaría eventos de latencia ni saturación sobre la zona
modelada, toda vez, que a nivel porcentual equivale al 78% del valor normado, ello
durante el peor escenario evaluado (Fase de Operación).

 - Para el contaminate CO el resultado de la modelación arroja una concentración máxima
horaria 8,0E-5 mg/m 3 durante la fase Operación en su receptor N°4. Mientras que
durante la misma fase de Operación se estima una concentración máxima de 5,21E-09
mg/m 3 en el receptor N°6.

 - Para el contaminate NOx el resultado de la modelación arroja una concentración máxima
horaria 0,33 ug/m3 durante la fase Operación en su receptor N°4. Mientras que durante

la misma fase de Operación se estima una concentración máxima de 0,28 ug/m3 en el

receptor N°6.

Los aportes del proyecto a las concentraciones de los contaminantes en estudio (MP 2.5,

MP10,, CO y NOx), en los receptores evaluados no presentan valores que superen las normas

de calidad primaria de los contaminantes estudiados.

3 La Estación sólo cuenta con registros actualizados de MP2.5.

49

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

Los resultados obtenidos de la Modelación de Emisiones Atmosféricas, permiten concluir que

el proyecto _**DIA**_ _**“Planta Caleta Bay II”**_ no aporta significativamente a las concentraciones de

calidad del aire de la zona modelada y no generaría eventos de latencia ni saturación de los

contaminantes estudiados.

50

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

## 5. REFERENCIAS

 - Registro de Monitoreo Calidad de Aire y Meteorológico Estación Mirasol.

 - Pontificia Universidad Católica de Chile, Educación Continua UC, Escuela de Ingeniería.

(2014). Manual de Usuario CALPUFF View.

 - Scire, J. S., Strimaitis, D. G., y Yamartino, R. J., 2000a. A User’s Guide for the CALPUFF

Dispersion Model (Version 5). Earth Tech Inc., Concord, Massachusetts.

51

Modelación de Estimaciones Atmosféricas

DIA “Planta Caleta Bay II”

52