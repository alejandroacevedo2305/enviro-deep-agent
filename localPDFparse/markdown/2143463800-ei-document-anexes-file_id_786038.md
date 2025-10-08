---
title: Sin título
author: Lorena Fernanda Morales Morales
date: D:20190604194712-04'00'
language: es
type: report
pages: 45
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Modelación de Emisiones Atmosféricas DIA “Loteo Valles de Maule IV, Comuna de Maule, Región del Maule”
-->

# Modelación de Emisiones Atmosféricas DIA “Loteo Valles de Maule IV, Comuna de Maule, Región del Maule”

## Elaborado por: Lorena Morales M. Asesorías Ambientales y Otros EIRL 16/05/2019

Modelación de Estimaciones Atmosféricas

DIA “Loteo Valles de Maule IV, Comuna de Maule, Región del Maule”

## Contenido

1. INTRODUCCIÓN .......................................................................................................................... 2

2. OBJETIVOS .................................................................................................................................. 3

3. MODELACIÓN DE DISPERSIÓN ATMOSFÉRICA ........................................................................... 4

3.1 Descripción y Justificación del Modelo ...............................................................................4

3.2 Base Teórica del Modelo utilizado ......................................................................................4

3.3 Caracterización Meteorológica ...........................................................................................6

3.3.1 Análisis Meteorología Observacional ......................................................................... 7

3.4 Modelo Meteorológico .....................................................................................................13

3.4.1 Justificación Modelo Meteorológico ........................................................................ 13

3.4.2 Descripción Modelo Meteorológico ......................................................................... 13

3.5 Análisis De Incertidumbre ................................................................................................20

3.6 Características Del Dominio De Modelación Y Su Entorno ...............................................23

3.6.1 Características de Dominio ....................................................................................... 23

3.7 Datos topográficos y uso de suelo ....................................................................................24

3.8 Análisis y Caracterización de Calidad de Aire de la zona del proyecto .............................25

3.9 Fuentes De Emisión ..........................................................................................................27

3.10 Receptores .......................................................................................................................28

4. RESULTADOS MODELACIÓN CALIDAD DEL AIRE ....................................................................... 30

4.1 Determinación Área de Influencia ....................................................................................30

4.1.1 Concentración MP10 .................................................................................................. 31

4.1.2 Concentración MP2.5 ............................................................................................... 34

4.1.3 Concentración CO ..................................................................................................... 37

4.1.4 Concentración NOx ................................................................................................... 40

5. CONCLUSIÓN ............................................................................................................................ 43

6. REFERENCIAS ............................................................................................................................ 44

1

Modelación de Estimaciones Atmosféricas

DIA “Loteo Valles de Maule IV, Comuna de Maule, Región del Maule”

## 1. INTRODUCCIÓN

El presente informe contiene los resultados de la modelación de calidad del aire **para material**

**particulado (MP10, MP2,5) y gases** emitidos por las actividades de construcción y operación del

Proyecto _**DIA “Loteo Valles de Maule IV, Comuna de Maule, Región del Maule”**_ considerando el
peor de los escenarios para cada una de las fases [1] .

Se contempla específicamente verificar que el proyecto no genere alguno de los efectos,

características o circunstancias indicadas en el artículo 5 del D.S. N° 40/2012 del MMA, en cuanto

a calcular el aporte en concentración anual y diario de material particulado MP10, MP2,5 y gases

emitidos por las actividades a realizar en el proyecto en su peor escenario para sus fases de

construcción y operación, sobre los receptores sensibles identificados por el Proponente,

adjuntando las isolíneas de concentración.

Para la línea de base meteorológica se realizó una caracterización general de la meteorología

imperante en la zona. Para ello, se utilizó meteorología modelada por el modelo meteorológico

WRF adquirida por medio de Lakes Environmental, adicionalmente se recurrió a la recopilación de

antecedentes meteorológicos de la estación superficial más cercana al proyecto, correspondiente

a la Estación U.C Maule de administración de propiedad Ministerio de Medio Ambiente .

1 Para la fase de construcción se considera la tasa de emisión correspondiente a la etapa constructiva N°2,
que corresponde aquella con mayor cantidad de casas a construir. Para el caso de la fase de operación se
considera como peor escenario posterior a la entrega de la etapa N°4 del conjunto habitacional, de manera
tal, se considera como tasa de emisión la totalidad del conjunto habitacional, es decir, el 100% de las casas
habitadas contemplando un vehiculo por domicilio como fuente de emisión.

2

Modelación de Estimaciones Atmosféricas

DIA “Loteo Valles de Maule IV, Comuna de Maule, Región del Maule”

## 2. OBJETIVOS

El objetivo general del estudio es modelar las emisiones atmosféricas generadas por el proyecto, a

fin de evaluar el impacto en la calidad del aire durante las Fases de Construcción y Fase de

Operación del mismo.

Para lograr el objetivo principal del presente informe, se plantean objetivos específicos que

apoyan la evaluación realizada. Así los objetivos específicos son:

 - Realizar una caracterización meteorológica, con el fin de tener un conocimiento de los

fenómenos meteorológicos y climáticos del área en la que tendrá influencia el Proyecto.

 - Realizar un análisis de la línea de base de calidad del aire, en el cual se busca conocer los

niveles basales de concentración de material particulado (MP10, MP2,5 y gases)

característicos del área del proyecto.

##  Evaluar el impacto sobre la calidad del aire mediante la implementación del modelo de

calidad del aire, en las fases construcción y de operación del proyecto.

3

Modelación de Estimaciones Atmosféricas

DIA “Loteo Valles de Maule IV, Comuna de Maule, Región del Maule”

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

marco de la Evaluación Ambiental del Proyecto _**“Loteo Valles de Maule IV, Comuna de Maule,**_

_**Región del Maule”,**_ se considera pertinente la presentación de la Modelación de emisiones

atmosféricas generadas durante la fase de construcción y operación del proyecto, como

herramienta para evaluar el impacto de dichas emisiones sobre el recurso aire, y el consecuente

impacto sobre otros recursos naturales renovables y la salud de las personas.

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

Group de TRC Solutions. Debido a su desempeño, CALPUFF fue catalogado por la USEPA como

modelo recomendado para la evaluación del impacto en la calidad del aire de distintos tipos de

proyectos, especialmente, de aquellos donde es necesario considerar la variación en el tiempo y

en el espacio de las condiciones meteorológicas y su incidencia en el transporte, transformación y

remoción de contaminantes.

El sistema de modelación está compuesto por los siguientes componentes principales:

4

Modelación de Estimaciones Atmosféricas

DIA “Loteo Valles de Maule IV, Comuna de Maule, Región del Maule”

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

DIA “Loteo Valles de Maule IV, Comuna de Maule, Región del Maule”

### 3.3 Caracterización Meteorológica

Lo que busca la caracterización meteorológica es realizar una descripción cualitativa de la situación

meteorológica y topográfica del lugar. De acuerdo a los lineamientos indicados en la Guía de Uso

de modelos, el estudio de los procesos desde la mesoescala hasta la escala sinóptica, y cómo éstos

influyen en los procesos de transporte, dispersión y transformación de contaminantes a distintas

escalas temporales es lo óptimo para poder incluir opciones con menor propagación de error en la

estimación de las concentraciones. Se utilizó meteorología modelada por el modelo

meteorológico WRF e ingresada en modelo CALPUFF.

Los datos Meteorológicos observados, fueron tomados desde Estación Meteorológica, Estación

Osorno, administrada por el Ministerio de Medio Ambiente

El análisis se realizó para el periodo comprendido entre enero de 2018 a diciembre de 2018, para

la estación U.C Maule. La siguiente imagen, muestra la ubicación de la estación meteorológica

considerada en el análisis:

**Imagen N°1: Localización Estación Meteorológica**

|Nombre Estación|U.C Maule|
|---|---|
|**Coordenada Este**|262216|
|**Coordenada Norte**|6075477|

**Fuente: Elaboración desde Google Earth a partir de**

[https://sinca.mma.gob.cl/index.php/estacion/index/id/63](https://sinca.mma.gob.cl/index.php/estacion/index/id/63)

6

Modelación de Estimaciones Atmosféricas

DIA “Loteo Valles de Maule IV, Comuna de Maule, Región del Maule”

**3.3.1** **Análisis Meteorología Observacional**

La información meteorológica de la Estación U.C.Maule incluye antecedentes del periodo 2018,

abarcando desde Enero a Diciembre 2018, en forma horaria.

_**3.3.1.1**_ _**Rosa de los Vientos**_

El análisis del comportamiento de los vientos observados en la Estación U.C Maule, se presenta a

continuación para los meses de Enero a Diciembre de 2018. Este análisis se realizó con el fin de

comprender la distribución de velocidades y la frecuencia de ocurrencia de las diferentes

direcciones de viento.

**Gráfico N°1.1:** Serie de tiempo Dirección de Viento (soplando desde)

observadas en las Estación U.C.Maule, año 2018

7

Modelación de Estimaciones Atmosféricas

DIA “Loteo Valles de Maule IV, Comuna de Maule, Región del Maule”

**Gráfico N°1.2:** Serie de tiempo Dirección de Viento (soplando desde) observadas en las Estación

U.C Maule, Enero-Marzo año 2018

**Gráfico N°1.3:** Serie de tiempo Dirección de Viento (soplando desde) observadas en las Estación

U.C Maule, Abril-Junio año 2018.

8

Modelación de Estimaciones Atmosféricas

DIA “Loteo Valles de Maule IV, Comuna de Maule, Región del Maule”

**Gráfico N°1.4:** Serie de tiempo Dirección de Viento (soplando desde) observadas en las Estación

U.C Maule, Julio-Septiembre año 2018.

**Gráfico N°1.5:** Serie de tiempo Dirección de Viento (soplando desde) observadas en las Estación

U.C Maule, Octubre-Diciembre año 2017.

9

Modelación de Estimaciones Atmosféricas

DIA “Loteo Valles de Maule IV, Comuna de Maule, Región del Maule”

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

**Gráfico N°2.1:** Serie de tiempo Velocidad de Viento observadas en las Estación U.C Maule Enero

Diciembre 2018.

10

Modelación de Estimaciones Atmosféricas

DIA “Loteo Valles de Maule IV, Comuna de Maule, Región del Maule”

**Gráfico N°2.2:** Serie de tiempo Velocidad de Viento observadas en las Estación U.C Maule,Enero

Marzo 2018.

**Gráfico N°2.3:** Serie de tiempo Velocidad de Viento observadas en las Estación U.C Maule,AbrilJunio 2018

11

Modelación de Estimaciones Atmosféricas

DIA “Loteo Valles de Maule IV, Comuna de Maule, Región del Maule”

**Gráfico N°2.4:** Serie de tiempo Velocidad de Viento observadas en las Estación U.C Maule,Julio

Septiembre 2018.

**Gráfico N°2.5:** Serie de tiempo Velocidad de Viento observadas en las Estación U.C Maule Octubre

 - Diciembre 2018.

12

Modelación de Estimaciones Atmosféricas

DIA “Loteo Valles de Maule IV, Comuna de Maule, Región del Maule”

### 3.4 Modelo Meteorológico

**3.4.1** **Justificación Modelo Meteorológico**

Según lo establecido por la Guía para el uso de Modelos de Calidad del Aire en el SEIA, la selección

del modelo meteorológico utilizado en el presente estudio se realizó fundamentándose en las

condiciones de topografía compleja del área entorno al proyecto. Para esto, la guía recomienda un

modelo que permita simular una meteorología heterogénea.

La meteorología considerada por el modelo WRF corresponde a los datos modelados

proporcionados Lakes Environmental en período de 1 enero 2015 a 31 diciembre 2015. Esta

información fue utilizada en el modelo de calidad de aire CALPUFF.

**3.4.2** **Descripción Modelo Meteorológico**

La configuración de corrida se hizo desde la hora 1 del mes de enero del año 2015 hasta la hora 23

del día 31 de diciembre de 2015. Se configuró para la modelación horaria la zona UTC-4, y el paso

de tiempo es horario con un total de 8760 horas.

El modelo de investigación y pronóstico del tiempo (Weather Research and Forecasting - WRF) es

un sistema de predicción numérico de mesoscala de nueva generación, diseñado para servir

pronósticos operacionales y para estudio de la atmósfera.

|Tabla 3.5: Características de los Datos del Modelo Meteorológico WRF Usados para la Evaluación del Proyecto|Col2|
|---|---|
|Característica de los Datos del Modelo WRF|Característica de los Datos del Modelo WRF|
|- Periodo<br>- Latitud<br>- Longitud<br>- Tamaño del Dominio<br>- Resolución<br>- Zona Horaria<br> - Localización|Jan 01, 2015 - Dec 31,<br>35.516743 S<br>71.694496 W<br>50x50 km<br>1 km<br>-19 - Site Time Zone: UTC - 4<br>- Chile|

13

Modelación de Estimaciones Atmosféricas

DIA “Loteo Valles de Maule IV, Comuna de Maule, Región del Maule”

Ejemplos de los campos de vientos generados por WRF se presentan en Figura 2, para el año 2017

Figura N°2: Ejemplo de Campos de Vientos generados por el Modelo WRF en el Dominio

Fuente: Elaboración propia a partir de CALMET

La información meteorológica de la meterología modelada para el periodo 2017, abarcando desde

Enero a Diciembre 2017, se presenta a continuación;

14

Modelación de Estimaciones Atmosféricas

DIA “Loteo Valles de Maule IV, Comuna de Maule, Región del Maule”

_**3.4.2.1**_ _**Rosa de los Vientos**_

La meterología anual se presenta en la siguiente rosa de vientos;

**Gráfico N°3.4.2.1** : Serie de tiempo Dirección de Viento (soplando desde) modelada (WRF)

año 2015.

**Gráfico N°3.4.2.2 :** Serie de tiempo Dirección de Viento (soplando desde) modelada (WRF)

Enero a Marzo del año 2015.

15

Modelación de Estimaciones Atmosféricas

DIA “Loteo Valles de Maule IV, Comuna de Maule, Región del Maule”

**Gráfico N°3.4.2.3 :** Serie de tiempo Dirección de Viento (soplando desde) modelada (WRF)

Abril a Junio del año 2015.

**Gráfico N°3.4.2.4 :** Serie de tiempo Dirección de Viento (soplando desde) modelada (WRF)

Julio a Septiembre del año 2015.

16

Modelación de Estimaciones Atmosféricas

DIA “Loteo Valles de Maule IV, Comuna de Maule, Región del Maule”

**Gráfico N°3.4.2.5 :** Serie de tiempo Dirección de Viento (soplando desde) modelada (WRF)

Octubre a Diciembre del año 2015.

**Gráfico N°3.4.2.6:** Serie de tiempo Velocidad de Viento modelada (WRF) Año 2015.

17

Modelación de Estimaciones Atmosféricas

DIA “Loteo Valles de Maule IV, Comuna de Maule, Región del Maule”

**Gráfico N°3.4.2.7:** Serie de tiempo Velocidad de Viento modelada (WRF) Enero a Marzo Año 2015.

**Gráfico N°3.4.2.6:** Serie de tiempo Velocidad de Viento modelada (WRF) Abril a Junio Año 2015.

18

Modelación de Estimaciones Atmosféricas

DIA “Loteo Valles de Maule IV, Comuna de Maule, Región del Maule”

**Gráfico N°3.4.2.6:** Serie de tiempo Velocidad de Viento modelada (WRF) Julio a Septiembre Año

2015.

Gráfico N°3.4.2.6: Serie de tiempo Velocidad de Viento modelada (WRF) Octubre a Diciembre Año

2015.

19

Modelación de Estimaciones Atmosféricas

DIA “Loteo Valles de Maule IV, Comuna de Maule, Región del Maule”

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

[∑ ]

[∑ ]

~~√~~

∑ ∑ ∑

∑
~~√~~

(∑

) ∑

∑

Donde corresponde a las observaciones; corresponde a los valores modelados; e i

corresponde a cada uno de los N valores horarios de las variables analizadas para la estación.

**Tabla N°3.5.1: Comparación vientos observados vs modelados (WRF)**

|Estación|Sesgo|RMSE|r|
|---|---|---|---|
|Escuela U.C<br>Maule|0,31|1,19|0,83|

Tanto el sesgo como RMSE indican diferencias entre el modelo y los datos observados de la

estación de monitoreo, en donde los datos modelados poseen una asimitría positiva, por cuanto

presentan un coeficiente de correlación cercano a 1, por lo que existe una correlación positiva

directamente proporcional.

La siguiente figura, presenta la distribución horaria de los registros de velocidad de la Estación de

Monitoreo Escuela U.C Maule, respecto a los datos obtenidos del modelo de pronóstico WRF

utilizado.

20

Modelación de Estimaciones Atmosféricas

DIA “Loteo Valles de Maule IV, Comuna de Maule, Región del Maule”

**Gráfico N°3.6.2:** Gráfico Comparativo Velocidad de Viento

Modelada (WRF) v/s Observada Año 2018.

**Gráfico N°3.6.3:** Gráfico Comparativo Dirección del Viento

Modelada (WRF) v/s Observada Año 2018.

**Gráfico N°3.6.4:** Gráfico Comparativo Temperatura

21

Modelación de Estimaciones Atmosféricas

DIA “Loteo Valles de Maule IV, Comuna de Maule, Región del Maule”

Modelada (WRF) v/s Observada Año 2018.

Del gráfico anterior, se observa que los registros de la estación U.C Maule meterológica presenta

un comportamiento similar a los registrados por el archivo WRF.

22

Modelación de Estimaciones Atmosféricas

DIA “Loteo Valles de Maule IV, Comuna de Maule, Región del Maule”

### 3.6 Características Del Dominio De Modelación Y Su Entorno

**3.6.1** **Características de Dominio**

El dominio de modelación considerado para el presente proyecto corresponde a una grilla

rectangular de 50 km por 50 km, compuesta por celdas de 1 km por lado. En la Tabla 17 se

presentan las características del área correspondiente al dominio de modelación. El dominio

elegido abarca el área de influencia del proyecto para los distintos componentes ambientales que

pueden verse afectados por las emisiones de éste.

El dominio de modelación está definido por la siguiente imagen:

**Imagen N°2: Dominio de Modelación**

Fuente: Elaboración propia a partir de CALPUFF

23

Modelación de Estimaciones Atmosféricas

DIA “Loteo Valles de Maule IV, Comuna de Maule, Región del Maule”

### 3.7 Datos topográficos y uso de suelo

La topografía de la zona en análisis se obtiene de la Misión de Radar Topográfico del

Transbordador Espacial de la NASA1 (SRTM en inglés), que consiste en un modelo digital de

elevación de alta resolución que describe la altimetría de una zona mediante un conjunto de cotas

para una ubicación dada con una aproximadamente de 90 metros.

En la siguiente imagen se muestran las elevaciones obtenidas del área de influencia.

**Imagen N°3:** Topografía del dominio de modelación

Fuente Elaboración propia a partir de CALPUFF

Los tipos de suelo presentes en el dominio son de gran importancia para fines de modelación, ya

que determinan los procesos de transferencia de calor, afectando los balances de energía

superficial, elemento fundamental para poder estimar la altura de mezclado en los distintos

períodos en evaluación. Además de esto, tienen efecto en el viento a nivel de superficie, ya que

según el tipo de cobertura que se tenga, la resistencia que se ejerce sobre las corrientes de aire.

24

Modelación de Estimaciones Atmosféricas

DIA “Loteo Valles de Maule IV, Comuna de Maule, Región del Maule”

### 3.8 Análisis y Caracterización de Calidad de Aire de la zona del proyecto

Para establecer la situación basal de la calidad de aire del área de influencia del Proyecto se

tomaron los datos de estación más cercana al proyecto, denominada estación de monitoreo de

calidad de aire “U.C Maule”, emplazada a 11 kilómetros al Noreste del proyecto, para el período

comprendido entre Enero de 2018 y Diciembre de 2018. Cabe señalar que dicha estación sólo

dispone de información actualizada para MP2.5 y MP10.

**Figura N°3:** Ubicación Estación de Monitoreo Calidad de Aire

Las comunas de Talca y Maule actualmente presentan elevados niveles de Material Particulado

Respirable MP10 y Material Particulado Fino MP2,5, de acuerdo al montireo realizado desde el

año 2004 por la Secretaría Regional Ministerial de Salud del Maule (SEREMI de Salud). En base a

dicho análisis, se declararón zona saturada por material particulado respirable MP10, en su

concentración anual y de 24 horas, mediante DS No 12, del 4 de febrero 2010, de MINSEGPRES.

Por su parte desde el 28 de marzo de 2016 se encuentran dentro del Plan de Descontaminación

Atmosférica (PDA) de Talca y Maule, documento que señala que en el caso específico de Talca y

Maule, que el MP2,5 representa aproximadamente el 92% del MP10.

|Tabla N°3.6: Concentración (ug/m3) promedio|de contaminantes en EMRP durante el año 2018|
|---|---|
|**MP2.5 (ug/m3)**<br>**concentración promedio 24 hrs**|**PM 10 (ug/m3)**<br>**concentración promedio 24 hrs**|
|19,9|33,2|

**Fuente: Registro Estación U.C Maule**

25

Modelación de Estimaciones Atmosféricas

DIA “Loteo Valles de Maule IV, Comuna de Maule, Región del Maule”

**Figura N°3.1:** Concentración promedio 24 Hrs de MP2.5 (ug/m3)

Fuente: Elaboración propia a partir de datos de Estación U.C Maule

**Figura N°3.2:** Concentración promedio 24 Hrs de MP10 (ug/m3)

Fuente: Elaboración propia a partir de datos de Estación U.C Maule

26

Modelación de Estimaciones Atmosféricas

DIA “Loteo Valles de Maule IV, Comuna de Maule, Región del Maule”

### 3.9 Fuentes De Emisión

Para evaluar la dispersión atmosférica de las emisiones generadas por el proyecto, se consideran 2

Escenarios de modelación, en el caso de la fase de construcción se utiliza la tasa de emisión

proyectada para la etapa N°2 por considerarse aquella con mayor cantidad de emisión en relación

a las otras etapas constructivas (peor escenario), mientras que para la fase de operación se utiliza

como peor escenario, el correspondiente a la habitabilidad del 100% de las viviendas, de acuerdo

a la siguiente información;

**Tabla N°3.7:** Tasa de Emisión según Escenario de Modelación Fase Construcción

|Fuente|MP10 (Ton/año)|Col3|Col4|Col5|MP2.5 (Ton/año)|Col7|Col8|Col9|NOx (Ton/año)|Col11|Col12|Col13|CO(Ton/año)|Col15|Col16|Col17|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Fuente**|**E1**|**E2**|**E3**|**E4**|**E1**|**E2**|**E3**|**E4**|**E1**|**E2**|**E3**|**E4**|**E1**|**E2**|**E3**|**E4**|
|Escarpe|||||||||||||||||
|Excavación|0,35|0,35|0,24|0,32|0,21|0,21|0,14|0,19|||||||||
|Carga y<br>Descarga|0,02|0,02|0,01|0,02|0,00|0,00|0,00|0,00|||||||||
|Erosión Eólica<br>en Botadero|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|||||||||
|Re suspensión<br>por Tránsito de<br>Camiones<br>pesados en<br>Caminos No<br>Pavimentados|0,08|0,08|0,08|0,08|0,01|0,01|0,01|0,01|||||||||
|Proceso de<br>Combustión<br>interna<br>camiones<br>pesados|0,00|0,00|0,00|0,00|||||0,01|0,01|0,01|0,01|0,00|0,00|0,00|0,00|
|Proceso de<br>combustión en<br>maquinaria<br>pesada total|0,08|0,08|0,08|0,08|||||0,90|0,90|0,90|0,90|0,22|0,22|0,22|0,22|
|Re suspensión<br>por tránsito en<br>caminos<br>pavimentados|0,36|0,36|0,36|0,36|0,02|0,02|0,02|0,02|||||||||
|**TOTAL**|**0,89**|**0,89**|**0,77**|**0,84**|**0,24**|**0,24**|**0,17**|**0,22**|**0,91**|**0,91**|**0,91**|**0,91**|**0,23**|**0,23**|**0,23**|**0,23**|

**Tabla N°3.7.1:** Tasa de Emisión según Escenario de Modelación Fase Operación

|Fuente|MP10 (Ton/año)|MP2.5 (Ton/año)|NOx (Ton/año)|CO(Ton/año)|
|---|---|---|---|---|
|Proceso de Combustión interna camiones pesados|0,15|0|1,17|0,33|
|Re suspensión por tránsito en caminos pavimentados|0,65|0,16|0|0|
|TOTAL|0,79|0,15|1,17|0,33|

27

Modelación de Estimaciones Atmosféricas

DIA “Loteo Valles de Maule IV, Comuna de Maule, Región del Maule”

### 3.10 Receptores

La ubicación de los receptores se considera una grilla de receptores de 50 km x 50 km con

equispaciado de 1 km entre celdas.

Figura N°3.6: Emplazamiento Grilla de Receptores

Fuente: Elaboración propia a partir de GoogleEarth

28

Modelación de Estimaciones Atmosféricas

DIA “Loteo Valles de Maule IV, Comuna de Maule, Región del Maule”

Asímismo se contempla la evaluación de receptores discretos, según se indica en las siguiente

tabla e imágenes a continuación;

|N°|Coordenadas<br>Receptor|Col3|Descripción|
|---|---|---|---|
|**_N°_**|**_x _**|**_y _**|**_y _**|
|1|**255.253**|**6066.362**|**Pasaje N°4 casa 668**|
|2|**255.305**|**6066.257**|**Calle N°1 casa 601**|
|3|**255.497**|**6066.200**|**Sector Fundo San Juan S/N**|
|4|**255.701**|**6066.217**|**Calle Los Avellanos S/N**|
|5|**255.853**|**6066.248**|**Calle Los Avellanos S/N**|
|6|**255.836**|**6066.522**|**Planta de Tratamiento S/N**|
|7|**255.573**|**6066.504**|**Referencial Etapa 1**|
|8|**255.646**|**6066.333**|**Referencial Etapa 3**|

Figura N°3.6.1: Emplazamiento Receptores Discretos

29

Modelación de Estimaciones Atmosféricas

DIA “Loteo Valles de Maule IV, Comuna de Maule, Región del Maule”

### 4. RESULTADOS MODELACIÓN CALIDAD DEL AIRE

En la siguiente sección se entregan las concentraciones obtenidas utilizando el modelo

meteorológico de meso escala Weather Research Forecasting Model (WRF), como insumo para

CALPUFF View. De esta forma fue posible obtener las concentraciones de los contaminantes en

cada receptor según Escenario evaluado (Fase Construcción, Fase de Operación situación actual y

proyectada). Estos resultados no superan las concentraciones máximas referidas a las normas de

calidad primaria para los contaminantes MP10, MP2.5, CO y NOx respectivamente.

### 4.1 Determinación Área de Influencia

En base a la dispersión de los contaminantes evaluados, se determina como Área de Influencia,

aquel espacio comprendido por la dispersión del contaminante mayormente desplazado,

correspondiente al MP2,5 en su concentración de diaria, en una extensión aproximada de 7 Km

para el eje sur y 3,33 Km en el eje este . Para mayor detalle se presenta gráfica del área de

Influencia, según lo recién indicado;

**Gráfica N°4.1: Área de Influencia Componente Calidad de Aire**

Elaboración propia

30

Modelación de Estimaciones Atmosféricas

DIA “Loteo Valles de Maule IV, Comuna de Maule, Región del Maule”

**4.1.1** **Concentración MP10**

De acuerdo a lo indicado en el Decreto Supremo No12, de 4 de febrero de 2010, del Ministerio

Secretaría General de la Presidencia, declara a las comunas de Maule y Talca como Zona Saturada

por Material Particulado Respirable MP10, en concentración anual y de 24 horas.

Por su parte las emisiones de MP10 generadas por el proyecto y de acuerdo a los resultados de la

modelación el flujo del compuesto se concentra en la zona inmediata al proyecto, observándose

un aporte máximo en concentración para el receptor N°8, con un valor de 12,11 ug/m3N para el
período diario, durante la fase de construcción, que sumado a la situación basal [2] alcanza una
concentración máxima final [3] en receptor N°8 de 44,31 ug/m3N para el periodo diario.

Las coordenadas y concentraciones en períodos de concentración anual y diaria de receptores

discretos se presenta en la siguiente tabla.

**Tabla N°4.1:** Concentración MP10 en Receptores Discretos

|DS 59 del MINSEGPRES, Norma primaria<br>de calidad del aire para MP10;|Col2|Col3|Valor normado Concentración Diaria|Col5|Valor normado Concentración<br>Anual|Col7|
|---|---|---|---|---|---|---|
|**_DS 59 del MINSEGPRES, Norma primaria_**<br>**_de calidad del aire para MP10;_**|**_DS 59 del MINSEGPRES, Norma primaria_**<br>**_de calidad del aire para MP10;_**|**_DS 59 del MINSEGPRES, Norma primaria_**<br>**_de calidad del aire para MP10;_**|**_150 ug/m3N_**|**_150 ug/m3N_**|**_50 ug/m3N_**|**_50 ug/m3N_**|
|**_N°_**|**_Coordenadas_**<br>**_Receptor_**|**_Coordenadas_**<br>**_Receptor_**|**_Aporte Proyecto Concentración Diaria_**|**_Aporte Proyecto Concentración Diaria_**|**_Aporte Proyecto Concentración_**<br>**_Anual_**|**_Aporte Proyecto Concentración_**<br>**_Anual_**|
|**_N°_**|**_Coordenadas_**<br>**_Receptor_**|**_Coordenadas_**<br>**_Receptor_**|**_Fase Construcción_**|**_Fase Operación_**|**_Fase_**<br>**_Construcción_**|**_Fase_**<br>**_Operación_**|
|**_N°_**|**_x _**|**_y _**|**_ug/m3_**|**_ug/m3_**|**_ug/m3_**|**_ug/m3_**|
|1|**255.253**|**6066.362**|**0,45**|**3,01**|**0,09**|**0,57**|
|2|**255.305**|**6066.257**|**0,57**|**3,58**|**0,15**|**0,76**|
|3|**255.497**|**6066.200**|**0,89**|**6,40**|**0,30**|**2,51**|
|4|**255.701**|**6066.217**|**2,43**|**10.3**|**0,63**|**4,94**|
|5|**255.853**|**6066.248**|**1,02**|**1,14**|**0,27**|**4,96**|
|6|**255.836**|**6066.522**|**1,02**|**7,02**|**0,38**|**2,73**|
|7|**255.573**|**6066.504**|**2,14**|**12.3**|**0,62**|**6,55**|
|8|**255.646**|**6066.333**|**12,11**|**1,10**|**2,57**|**5,90**|

2 De acuerdo al registro de Estación Calidad de Aire U.C Maule de 32,2 ug/m3N en concentración diaria.
3 Situación basal más aporte del proyecto.

31

Modelación de Estimaciones Atmosféricas

DIA “Loteo Valles de Maule IV, Comuna de Maule, Región del Maule”

**Gráfica N°4.1.1:** Concentración MP10 Concentración Diaria Fase Construcción

**Gráfica N°4.1.2:** Concentración MP10 Concentración Anual Fase Construcción

**Gráfica N°4.1.5:** Concentración MP10 Concentración Diaria Operación

32

Modelación de Estimaciones Atmosféricas

DIA “Loteo Valles de Maule IV, Comuna de Maule, Región del Maule”

**Gráfica N°4.1.6:** Concentración MP10 Concentración Anual Fase Operación

33

Modelación de Estimaciones Atmosféricas

DIA “Loteo Valles de Maule IV, Comuna de Maule, Región del Maule”

**4.1.2** **Concentración MP2.5**

En relación a la calidad de aire de la zona del proyecto en lo que respecta a este contaminante, el

Plan de Desctontaminación Atmosférica de Talca y Maule, señala que desde el año 2004 las

comunas presentan elevados niveles de Material Particulado Respirable MP10 y Material

Particulado Fino MP2,5, que a su vez, en el caso específico de Talca y Maule, el MP2,5 representa

aproximadamente el 92% del MP10. Por cuanto, dicho compuesto se presenta en altas

concentraciones basales en la zona del proyecto.

Por su parte el flujo de MP2,5 generado por el proyecto, se concentra en la zona inmediata,

observándose un aporte máximo en concentración para el receptor N°8, con un valor de 5,49
ug/m3N para el período diario, durante la fase de construcción, que sumado a la situación basal [4]
alcanza una concentración máxima final [5] en receptor N°8 de 25,39 ug/m3N para el periodo diario.

Cabe señalar que este receptor sólo registrará dicha concentración una vez durante el año

modelado, de acuerdo a las proyecciones arrojadas por el modelo utilizado.

Las coordenadas y concentraciones en períodos de concentración anual y diaria de receptores

discretos se presenta en la siguiente tabla.

**Tabla N°4.2:** Concentración MP2,5 en Receptores Discretos

|DS 12/11 del MMA, Norma primaria de<br>calidad del aire para MP2.5;|Col2|Col3|Valor normado Concentración Diaria|Col5|Valor normado Concentración Anual|Col7|
|---|---|---|---|---|---|---|
|**_DS 12/11 del MMA, Norma primaria de_**<br>**_calidad del aire para MP2.5;_**|**_DS 12/11 del MMA, Norma primaria de_**<br>**_calidad del aire para MP2.5;_**|**_DS 12/11 del MMA, Norma primaria de_**<br>**_calidad del aire para MP2.5;_**|**_50 ug/m3N_**|**_50 ug/m3N_**|**_20 ug/m3N_**|**_20 ug/m3N_**|
|**_N°_**|**_Coordenadas_**<br>**_Receptor_**|**_Coordenadas_**<br>**_Receptor_**|**_Aporte Proyecto Concentración Diaria_**|**_Aporte Proyecto Concentración Diaria_**|**_Aporte Proyecto Concentración Anual_**|**_Aporte Proyecto Concentración Anual_**|
|**_N°_**|**_Coordenadas_**<br>**_Receptor_**|**_Coordenadas_**<br>**_Receptor_**|**_Fase Construcción_**|**_Fase Operación_**<br>**_Proyectada_**|**_Fase Construcción_**|**_Fase Operación_**<br>**_Proyectada_**|
|**_N°_**|**x **|**y **|**_ug/m3_**|**_ug/m3_**|**_ug/m3_**|**_ug/m3_**|
|1|**255.253 **|**6066.362 **|**0,13**|**0,73**|**0,02**|**0,13**|
|2|**255.305 **|**6066.257 **|**0,15**|**0,87**|**0,03**|**0,18**|
|3|**255.497 **|**6066.200 **|**0,24**|**1,55**|**0,64**|**0,60**|
|4|**255.701 **|**6066.217 **|**0,99**|**2,50**|**0,21**|**1,19**|
|5|**255.853 **|**6066.248 **|**0,28**|**2,76**|**0,06**|**1,20**|
|6|**255.836 **|**6066.522 **|**0,37**|**1,70**|**0,08**|**0,63**|
|7|**255.573 **|**6066.504 **|**0,84**|**2,99**|**0,13**|**1,58**|
|8|**255.646**|**6066.333**|**5,49**|**2,66**|**1,09**|**1,42**|

**Gráfica N°4.2.1:** Concentración MP2.5 Concentración Diaria Fase Construcción

4 De acuerdo al registro de Estación Calidad de Aire U.C Maule de 19,9 ug/m3N en concentración diaria.
5 Situación basal más aporte del proyecto.

34

Modelación de Estimaciones Atmosféricas

DIA “Loteo Valles de Maule IV, Comuna de Maule, Región del Maule”

**Gráfica N°4.2.2:** Concentración MP2.5 Concentración Anual Fase Construcción

**Gráfica N°4.2.5:** Concentración MP2.5 Concentración Diaria FaseOperación

35

Modelación de Estimaciones Atmosféricas

DIA “Loteo Valles de Maule IV, Comuna de Maule, Región del Maule”

**Gráfica N°4.2.6:** Concentración MP2.5 Concentración Anual Fase Operación

36

Modelación de Estimaciones Atmosféricas

DIA “Loteo Valles de Maule IV, Comuna de Maule, Región del Maule”

**4.1.3** **Concentración CO**

Por su parte las emisiones de CO [6] generadas por el proyecto y de acuerdo a los resultados de la

modelación el flujo del compuesto se concentra en la zona inmediata al proyecto, observándose

un aporte máximo en concentración para el receptor N°5, con un valor de 2,49E-4mg/m3N para el

período horario, durante la fase de operación, muy inferior a lo estipulado en la norma de calidad

primaria de acuerdo a la siguiente tabla.

Las coordenadas y concentraciones en períodos de concentración anual y diaria de receptores

discretos se presenta en la siguiente tabla.

**Tabla N°4.3:** Concentración CO en Receptores Discretos

|DS 115 del MINSEGPRES,<br>Norma primaria de calidad del<br>aire para CO;|Col2|Col3|Valor normado Concentración Horaria<br>50mg/m3N|Col5|Valor normado Concentración 8 Horas<br>30 mg/m3N|Col7|
|---|---|---|---|---|---|---|
|**_N°_**|**_Coordenadas Receptor_**|**_Coordenadas Receptor_**|**_Aporte Proyecto Concentración Horaria_**|**_Aporte Proyecto Concentración Horaria_**|**_Aporte Proyecto Concentración 8 Horas_**|**_Aporte Proyecto Concentración 8 Horas_**|
|**_N°_**|**_Coordenadas Receptor_**|**_Coordenadas Receptor_**|**_Fase_**<br>**_Construcción_**<br>**_mg/m3_**|**_Fase Operación_**<br>**_mg/m3_**|**_Fase Construcción_** <br>**_mg/m3_**|**_Fase Operación_**<br>**_mg/m3_**|
|**_N°_**|**_x _**|**_y _**|**_y _**|**_y _**|**_y _**|**_y _**|
|1|**255.253**|**6066.362**|**1,03E-4**|**7,87E-4**|**5,27E-5**|**4,48E-4**|
|2|**255.305 **|**6066.257 **|**1,29E-4**|**9,45E-4**|**6,05E-5**|**4,89E-4**|
|3|**255.497 **|**6066.200 **|**1,82E-4**|**1,59E-3**|**1,07E-4**|**8,55E-4**|
|4|**255.701 **|**6066.217 **|**1,88E-4**|**1,94E-3**|**1,05E-4**|**1,31E-3**|
|5|**255.853 **|**6066.248 **|**1,66E-4**|**2,49E-3**|**8,70E-5**|**1,47E-3**|
|6|**255.836 **|**6066.522 **|**1,30E-4**|**1,24E-3**|**8,78E-5**|**8,50E-4**|
|7|**255.573 **|**6066.504 **|**1,67E-4**|**1,84E-3**|**1,22E-4**|**1,33E-3**|
|8|**255.646 **|**6066.333 **|**2,13E-4**|**1,63E-3**|**1,26E-4**|**1,23E-3**|

6 Para este compuesto la Estación de Calidad de Aire no registra monitoreo.

37

Modelación de Estimaciones Atmosféricas

DIA “Loteo Valles de Maule IV, Comuna de Maule, Región del Maule”

**Gráfica N°4.3.1** Concentración Horaria CO Fase Construcción

**Gráfica N°4.3.2** Concentración 8 Horas CO Fase Construcción

Gráfica N°4.3.5 Concentración Horaria CO Fase Operación

38

Modelación de Estimaciones Atmosféricas

DIA “Loteo Valles de Maule IV, Comuna de Maule, Región del Maule”

Gráfica N°4.3.6 Concentración 8 Horas CO Fase Operación

39

Modelación de Estimaciones Atmosféricas

DIA “Loteo Valles de Maule IV, Comuna de Maule, Región del Maule”

**4.1.4** **Concentración NOx**

Por su parte las emisiones de NOx [7] generadas por el proyecto y de acuerdo a los resultados de la

modelación el flujo del compuesto se concentra en la zona inmediata al proyecto, observándose

un aporte máximo en concentración para el receptor N°5, con un valor de 7 ug/m3N para el

período horario, durante la fase de operación, muy inferior a lo estipulado en la norma de calidad

primaria de acuerdo a la siguiente tabla.

Las coordenadas y concentraciones en períodos de concentración anual y diaria de receptores

discretos se presenta en la siguiente tabla.

**Tabla N°4.4:** Concentración NOx en Receptores Discretos

|DS 115 del MINSEGPRES, Norma<br>primaria de calidad del aire para NOx|Col2|Col3|Valor normado Concentración<br>Horaria<br>400 ug/m3N|Col5|Valor normado Concentración Anual<br>100 ug/m3N|Col7|
|---|---|---|---|---|---|---|
|**_N°_**|**_Coordenadas_**<br>**_Receptor_**|**_Coordenadas_**<br>**_Receptor_**|**_Aporte Proyecto Concentración_**<br>**_Horaria_**|**_Aporte Proyecto Concentración_**<br>**_Horaria_**|**_Aporte Proyecto Concentración Anual_**|**_Aporte Proyecto Concentración Anual_**|
|**_N°_**|**_Coordenadas_**<br>**_Receptor_**|**_Coordenadas_**<br>**_Receptor_**|**_Fase_**<br>**_Construcción_** <br>**_ug/m3_**|**_Fase Operación_**<br>**_Proyectada_** **_ug/m3_**|**_Fase_**<br>**_Construcción_** <br>**_ug/m3_**|**_Fase Operación_**<br>**_Proyectada_** **_ug/m3_**|
|**_N°_**|**_x _**|**_y _**|**_y _**|**_y _**|**_y _**|**_y _**|
|1|**255.253**|**6066.362**|**0,26**|**1,87**|**0,01**|**0,11**|
|2|**255.305**|**6066.257**|**0,35**|**2,26**|**0,02**|**0,14**|
|3|**255.497**|**6066.200**|**0,56**|**4,07**|**0,06**|**0,51**|
|4|**255.701**|**6066.217**|**0,60**|**5,68**|**0,06**|**1,05**|
|5|**255.853**|**6066.248**|**0,52**|**7,00**|**0,05**|**1,05**|
|6|**255.836**|**6066.522**|**0,42**|**3,49**|**0,08**|**0,58**|
|7|**255.573**|**6066.504**|**0,57**|**5,36**|**0,15**|**1,42**|
|8|**255.646**|**6066.333**|**0,67**|**4,84**|**0,08**|**1,26**|

7 Para este compuesto la Estación de Calidad de Aire no registra monitoreo.

40

Modelación de Estimaciones Atmosféricas

DIA “Loteo Valles de Maule IV, Comuna de Maule, Región del Maule”

**Gráfica N°4.4.1** Concentración Horaria NOx Fase Construcción

**Gráfica N°4.4.2** Concentración Anual NOX Fase Construcción

41

Modelación de Estimaciones Atmosféricas

DIA “Loteo Valles de Maule IV, Comuna de Maule, Región del Maule”

Gráfica N°4.4.4 Concentración Horaria NOX Fase Operación

Gráfica N°4.4.5 Concentración Anual NOX Fase Operación

42

Modelación de Estimaciones Atmosféricas

DIA “Loteo Valles de Maule IV, Comuna de Maule, Región del Maule”

## 5. CONCLUSIÓN

A partir de las modelaciones realizadas con respecto a las emisiones atmosféricas para las fases

de Construcción y Operación, se presentan las siguientes conclusiones:

Para la determinación de la situación basal de la calidad del aire de los receptores evaluados, se

consideró el registro existente en la Estación de Monitoreo U.C Maule ubicada en la comuna de

Talca, a una distancia aproximada de 11 kilómetro del área del proyecto, por considerarse aquella
más cercana al proyecto con registros actualizados [8] .

Por su parte y en relación al Decreto Supremo No12, de 4 de febrero de 2010, del Ministerio

Secretaría General de la Presidencia, que declara a las comunas de Maule y Talca como Zona

Saturada por Material Particulado Respirable MP10, en concentración anual y de 24 horas. El

proyecto generará un aporte máximo en concentración de MP10 para el receptor N°8, de 12,11

ug/m3N para el período diario, que sumado a la situación basal alcanza una concentración

máxima final en receptor N°8 de 44,31 ug/m3N para el periodo diario.

A su vez, y de acuerdo a lo indicado en el PDA de Talca y Maule, el compuesto MP2,5 representa

aproximadamente el 92% del MP10 en las comunas de Talca y Maule, por cuanto se observa

igualmente altas concentraciones de dicho compuesto como situación basal, lo que sin duda,

influye en la determinación de las concentraciones finales de dicho compuesto, que para el caso

del presente proyecto, generará un aporte máximo en concentración para el receptor N°8, con un

valor de 5,49 ug/m3N para el período diario, durante la fase de construcción, que sumado a la

situación basal alcanza una concentración máxima final en receptor N°8 de 25,39 ug/m3N para el

periodo diario.

De lo expuesto anteriormente se concluye que:

-Los aportes del proyecto a las concentraciones de los contaminantes (MP2.5, MP10, CO y NOx)

en los receptores evaluados, no presentan riesgos para la salud de la población, toda vez que las

concentraciones finales resultantes, no superan las normas de calidad primaria de los

contaminantes estudiados.

-Los resultados obtenidos de la Modelación de Emisiones Atmosféricas permiten concluir que el

proyecto DIA “Loteo Valles de Maule IV, Comuna de Maule, Región del Maule”” no aporta

significativamente a las concentraciones de calidad del aire de la zona modelada y no generaría

eventos de latencia ni saturación de los contaminantes estudiados.

8 La Estación sólo cuenta con registros actualizados de MP10 Y MP2,5.

43

Modelación de Estimaciones Atmosféricas

DIA “Loteo Valles de Maule IV, Comuna de Maule, Región del Maule”

## 6. REFERENCIAS

 - Registro de Monitoreo Calidad de Aire y Meteorológico Estación U.C Maule.

 - Pontificia Universidad Católica de Chile, Educación Continua UC, Escuela de Ingeniería.

(2014). Manual de Usuario CALPUFF View.

 - Scire, J. S., Strimaitis, D. G., y Yamartino, R. J., 2000a. A User’s Guide for the CALPUFF

Dispersion Model (Version 5). Earth Tech Inc., Concord, Massachusetts.

44