---
title: Sin título
author: Lorena Fernanda Morales Morales
date: D:20181018171138-03'00'
language: es
type: report
pages: 40
has_toc: False
has_tables: True
extraction_quality: high
---

|Col1|Col2|Col3|
|---|---|---|
|Modelación de Emisiones<br>Atmosféricas<br>DIA “Modificación y Modelación<br>Planta Elaboradora de Harina y<br>Aceite de Pescado,Salmonoil S.A.”<br>|||

### Elaborado por: Lorena Morales M. Asesorías Ambientales y Otros EIRL 18/10/2018

Modelación de Estimaciones Atmosféricas

DIA “Modificación y Modelación Planta Elaboradora de Harina y Aceite de Pescado, Salmonoil S.A.”

### Contenido

1. INTRODUCCIÓN ........................................................................................................................... 2

2. OBJETIVOS ................................................................................................................................... 3

3. MODELACIÓN DE DISPERSIÓN ATMOSFÉRICA ............................................................................ 4

3.1 Descripción y Justificación del Modelo ............................................................................... 4

3.2 Base Teórica del Modelo utilizado ...................................................................................... 4

3.3 Caracterización Meteorológica ........................................................................................... 6

3.3.1 Análisis Meteorología Observacional .......................................................................... 7

3.4 Modelo Meteorológico ..................................................................................................... 13

3.4.1 Justificación Modelo Meteorológico ......................................................................... 13

3.4.2 Descripción Modelo Meteorológico .......................................................................... 13

3.5 Análisis De Incertidumbre ................................................................................................. 20

3.6 Características Del Dominio De Modelación Y Su Entorno ............................................... 23

3.6.1 Características de Dominio ........................................................................................ 23

3.7 Datos topográficos y uso de suelo .................................................................................... 24

3.8 Análisis y Caracterización de Calidad de Aire de la zona del proyecto ............................. 25

3.9 Fuentes De Emisión ........................................................................................................... 26

3.10 Receptores......................................................................................................................... 27

4. RESULTADOS MODELACIÓN CALIDAD DEL AIRE ....................................................................... 29

4.1 Determinación Área de Influencia .................................................................................... 29

4.1.1 Concentración MP10 .................................................................................................. 30

4.1.2 Concentración MP2.5 ................................................................................................ 31

4.1.3 Concentración CO ...................................................................................................... 32

4.1.4 Concentración NOx ................................................................................................... 34

4.1.5 Concentración SO2 .................................................................................................... 35

5. CONCLUSIÓN ............................................................................................................................. 37

6. REFERENCIAS ............................................................................................................................. 39

1

Modelación de Estimaciones Atmosféricas

DIA “Modificación y Modelación Planta Elaboradora de Harina y Aceite de Pescado, Salmonoil S.A.”

### 1. INTRODUCCIÓN

El presente informe contiene los resultados de la modelación de calidad del aire **para material**

**particulado (MP10, MP2,5) y gases** emitidos por las actividades de construcción y operación del
Proyecto _**DIA “MODIFICACIÓN Y MODERNIZACIÓN PLANTA ELABORADA DE HARINA Y ACEITE DE**_

_**PESCADO,SALMONOIL S.A.”**_ en el Escenario Situación Proyectada y actual.

Se contempla específicamente verificar que el proyecto no genere alguno de los efectos,

características o circunstancias indicadas en el artículo 5 del D.S. N° 40/2012 del MMA, en cuanto

a calcular el aporte en concentración anual y diario de material particulado MP10, MP2,5, MPS y

gases emitidos por las actividades a realizar en el proyecto en su peor escenario, sobre los

receptores sensibles identificados por el Proponente,, adjuntando las isolíneas de concentración y

señalar la zona de máximo impacto del proyecto.

Para la línea de base meteorológica se realizó una caracterización general del clima y la

meteorología imperante en la zona. Para ello, se utilizó meteorología modelada por el modelo

meteorológico WRF adquirida por medio de Lakes Environmental, adicionalmente se recurrió a la

recopilación de antecedentes bibliográficos tanto de organismos públicos como privados.

2

Modelación de Estimaciones Atmosféricas

DIA “Modificación y Modelación Planta Elaboradora de Harina y Aceite de Pescado, Salmonoil S.A.”

### 2. OBJETIVOS

El objetivo general del estudio es modelar las emisiones atmosféricas para evaluar el impacto en

la calidad del aire, para la Fase de Construcción, Fase de Operación Actual, y Fase de Operación

Situación Proyectada (etapa de operación del Proyecto).

Para lograr el objetivo principal del presente informe, se plantean objetivos específicos que

apoyan la evaluación que se realizó. Así los objetivos específicos son:

 - Realizar una caracterización meteorológica, con el fin de tener un conocimiento de los

fenómenos meteorológicos y climáticos del área en la que tendrá influencia el Proyecto.

 - Realizar un análisis de la línea de base de calidad del aire, en el cual se busca conocer los

niveles basales de concentración de material particulado (MP10, MP2,5 y gases)

característicos del área del proyecto.

 - Evaluar el impacto sobre la calidad del aire mediante la implementación del modelo de

calidad del aire, en las fases construcción y de operación del proyecto (actual y

proyectada).

3

Modelación de Estimaciones Atmosféricas

DIA “Modificación y Modelación Planta Elaboradora de Harina y Aceite de Pescado, Salmonoil S.A.”

### 3. MODELACIÓN DE DISPERSIÓN ATMOSFÉRICA

Por medio de la ejecución de una serie de etapas, se logró determinar la estimación de las

concentraciones en un escenario definido, para un dominio determinado de receptores de interés

y que permitió, además, la generación de curvas de isoconcentración generadas a través de una

malla con equiespaciado cada 1 kilómetro.

La metodología se basa en las recomendaciones definidas en la Guía de Uso de Modelos de

Calidad de Aire en el SEIA, año 2014. En este caso en particular, se utiliza el modelo CALPUFF

siguiendo la recomendación de la misma Guía de Uso de Modelos de Calidad del Aire, utilizando

como criterio principal la mayoría de los receptores de interés, que se ubican dentro del área de

modelación y que constituye el área de influencia de la componente.

#### 3.1 Descripción y Justificación del Modelo

Considerando lo indicado en la Guía para el uso de Modelos de Calidad de Aire en el SEIA y en el
marco de la Evaluación Ambiental del Proyecto _**“MODIFICACIÓN Y MODERNIZACIÓN PLANTA**_

_**ELABORADA DE HARINA Y ACEITE DE PESCADO,SALMONOIL S.A.”,**_ se considera pertinente la

presentación de la Modelación de emisiones atmosféricas generadas durante la fase

deconstrucción y operación del proyecto, como herramienta para evaluar el impacto de dichas

emisiones sobre el recurso aire, y el consecuente impacto sobre otros recursos naturales

renovables y la salud de las personas.

Según lo establecido por la Guía para el uso de Modelos de Calidad del Aire en el SEIA, la selección

del modelo de Calidad del Aire utilizado en el presente estudio se realizó debido a la topografía

compleja del área donde se emplaza el proyecto y al alcance de las emisiones de este. Por esta

razón, fue usado el modelo CALPUFF explicado a continuación.

#### 3.2 Base Teórica del Modelo utilizado

La simulación del aporte del proyecto a las concentraciones de contaminantes se realizará

mediante el modelo CALPUFF, recomendado por la U. S. EPA para la evaluación de dispersión de

contaminantes desde fuentes continuas.

CALPUFF es un sistema de modelación avanzado para calidad del aire que considera además, la

meteorología de carácter no permanente. Su desarrollo estuvo a cargo del Sigma Research

4

Modelación de Estimaciones Atmosféricas

DIA “Modificación y Modelación Planta Elaboradora de Harina y Aceite de Pescado, Salmonoil S.A.”

Corporation mientras que su actual mantenimiento es responsabilidad del Atmospheric Studies

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

DIA “Modificación y Modelación Planta Elaboradora de Harina y Aceite de Pescado, Salmonoil S.A.”

#### 3.3 Caracterización Meteorológica

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
|**Coordenada Este**|41,47944|
|**Coordenada Norte**|72,96889|

Fuente: Elaboración desde Google Earth a partir de

[https://sinca.mma.gob.cl/index.php/estacion/index/id/63](https://sinca.mma.gob.cl/index.php/estacion/index/id/63)

6

Modelación de Estimaciones Atmosféricas

DIA “Modificación y Modelación Planta Elaboradora de Harina y Aceite de Pescado, Salmonoil S.A.”

**3.3.1** **Análisis Meteorología Observacional**

La información meteorológica de la Estación Mirsasol, incluye antecedentes del periodo 2017,

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

DIA “Modificación y Modelación Planta Elaboradora de Harina y Aceite de Pescado, Salmonoil S.A.”

Gráfico N°1.2: Serie de tiempo Dirección de Viento (soplando desde) observadas en las Estación

Escuela Mirasol, Enero-Marzo año 2017.

Gráfico N°1.3: Serie de tiempo Dirección de Viento (soplando desde) observadas en las Estación

Escuela Mirasol, Abril-Junio año 2017.

8

Modelación de Estimaciones Atmosféricas

DIA “Modificación y Modelación Planta Elaboradora de Harina y Aceite de Pescado, Salmonoil S.A.”

Gráfico N°1.4: Serie de tiempo Dirección de Viento (soplando desde) observadas en las Estación

Escuela Mirasol, Julio-Septiembre año 2017.

Gráfico N°1.5: Serie de tiempo Dirección de Viento (soplando desde) observadas en las Estación

Escuela Mirasol, Octubre-Diciembre año 2017.

9

Modelación de Estimaciones Atmosféricas

DIA “Modificación y Modelación Planta Elaboradora de Harina y Aceite de Pescado, Salmonoil S.A.”

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

DIA “Modificación y Modelación Planta Elaboradora de Harina y Aceite de Pescado, Salmonoil S.A.”

Gráfico N°2.2: Serie de tiempo Velocidad de Viento observadas en las Estación Mirasol, Enero

Marzo 2017.

Gráfico N°2.3: Serie de tiempo Velocidad de Viento observadas en las Estación Mirasol, AbrilJunio 2017.

11

Modelación de Estimaciones Atmosféricas

DIA “Modificación y Modelación Planta Elaboradora de Harina y Aceite de Pescado, Salmonoil S.A.”

Gráfico N°2.4: Serie de tiempo Velocidad de Viento observadas en las Estación Mirasol, Julio

Septiembre 2017.

Gráfico N°2.5: Serie de tiempo Velocidad de Viento observadas en las Estación Mirasol, Octubre

Diciembre 2017.

12

Modelación de Estimaciones Atmosféricas

DIA “Modificación y Modelación Planta Elaboradora de Harina y Aceite de Pescado, Salmonoil S.A.”

#### 3.4 Modelo Meteorológico

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
|- Periodo<br>- Latitud<br>- Longitud<br>- Tamaño del Dominio<br>- Resolución<br>- Zona Horaria<br> - Localización|Jan 01, 2017 - Dec 31,<br>41.666028 S<br>73.196381 W<br>100x100 km<br>1 km<br>-18 - Site Time Zone: UTC - 4<br>- Chile|

13

Modelación de Estimaciones Atmosféricas

DIA “Modificación y Modelación Planta Elaboradora de Harina y Aceite de Pescado, Salmonoil S.A.”

Ejemplos de los campos de vientos generados por WRF se presentan en Figura 2, para el año 2017

Figura N°2: Ejemplo de Campos de Vientos generados por el Modelo WRF en el Dominio

Fuente: Elaboración propia a partir de CALMET

La información meteorológica de la meterología modelada para el periodo 2017, abarcando desde

Enero a Diciembre 2017, se presenta a continuación;

14

Modelación de Estimaciones Atmosféricas

DIA “Modificación y Modelación Planta Elaboradora de Harina y Aceite de Pescado, Salmonoil S.A.”

_**3.4.2.1**_ _**Rosa de los Vientos**_

La meterología anual se presenta en la siguiente rosa de vientos;

Gráfico N°3.4.2.1 : Serie de tiempo Dirección de Viento (soplando desde) modelada (WRF)

año 2017.

15

Modelación de Estimaciones Atmosféricas

DIA “Modificación y Modelación Planta Elaboradora de Harina y Aceite de Pescado, Salmonoil S.A.”

Gráfico N°3.4.2.2 : Serie de tiempo Dirección de Viento (soplando desde) modelada (WRF)

Enero a Marzo del año 2017.

Gráfico N°3.4.2.3 : Serie de tiempo Dirección de Viento (soplando desde) modelada (WRF)

Abril a Junio del año 2017.

16

Modelación de Estimaciones Atmosféricas

DIA “Modificación y Modelación Planta Elaboradora de Harina y Aceite de Pescado, Salmonoil S.A.”

Gráfico N°3.4.2.4 : Serie de tiempo Dirección de Viento (soplando desde) modelada (WRF)

Julio a Septiembre del año 2017.

Gráfico N°3.4.2.5 : Serie de tiempo Dirección de Viento (soplando desde) modelada (WRF)

Octubre a Diciembre del año 2017.

17

Modelación de Estimaciones Atmosféricas

DIA “Modificación y Modelación Planta Elaboradora de Harina y Aceite de Pescado, Salmonoil S.A.”

Gráfico N°3.4.2.6: Serie de tiempo Velocidad de Viento modelada (WRF) Año 2017.

Gráfico N°3.4.2.7: Serie de tiempo Velocidad de Viento modelada (WRF) Enero a Marzo Año 2017.

18

Modelación de Estimaciones Atmosféricas

DIA “Modificación y Modelación Planta Elaboradora de Harina y Aceite de Pescado, Salmonoil S.A.”

Gráfico N°3.4.2.6: Serie de tiempo Velocidad de Viento modelada (WRF) Abril a Junio Año 2017.

Gráfico N°3.4.2.6: Serie de tiempo Velocidad de Viento modelada (WRF) Julio a Septiembre Año

2017.

19

Modelación de Estimaciones Atmosféricas

DIA “Modificación y Modelación Planta Elaboradora de Harina y Aceite de Pescado, Salmonoil S.A.”

Gráfico N°3.4.2.6: Serie de tiempo Velocidad de Viento modelada (WRF) Octubre a Diciembre Año

2017.

#### 3.5 Análisis De Incertidumbre

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

20

Modelación de Estimaciones Atmosféricas

DIA “Modificación y Modelación Planta Elaboradora de Harina y Aceite de Pescado, Salmonoil S.A.”

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
) (N∑ i=1 i

Ni=1 O i2 −(∑ Ni=1 O i ) 2 ) (N∑ Ni=1 M i2 −(∑ Ni=1 M i ) 2 )

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

En la siguiente figura se observa el punto que representa los datos del modelo, atendiendo a los

estadísticos calculados, observándose el coeficiente de correlación de 0,6 (punto rojo).

Gráfico N°3.6.1: Diagrama de Taylor Velocidad de Viento

Modelada (WRF) v/s Observada Año 2017.

21

Modelación de Estimaciones Atmosféricas

DIA “Modificación y Modelación Planta Elaboradora de Harina y Aceite de Pescado, Salmonoil S.A.”

La siguiente figura, presenta la distribución horaria de los registros de velocidad de la Estación de

Monitoreo Escuela Mirasol, respecto a los datos obtenidos del modelo de pronóstico WRF

utilizado.

Gráfico N°3.6.2: Gráfico Comparativo Velocidad de Viento

Modelada (WRF) v/s Observada Año 2017.

Del gráfico anterior, se observa que los registros de la estación meterológica Escuela Mirasol

presenta un comportamiento similar a los registrados por el archivo WRF.

22

Modelación de Estimaciones Atmosféricas

DIA “Modificación y Modelación Planta Elaboradora de Harina y Aceite de Pescado, Salmonoil S.A.”

#### 3.6 Características Del Dominio De Modelación Y Su Entorno

**3.6.1** **Características de Dominio**

El dominio de modelación considerado para el presente proyecto corresponde a una grilla

rectangular de 100 km por 100 km, compuesta por celdas de 1 km por lado. En la Tabla 17 se

presentan las características del área correspondiente al dominio de modelación. El dominio

elegido abarca el área de influencia del proyecto para los distintos componentes ambientales que

pueden verse afectados por las emisiones de éste.

El dominio de modelación está definido por la siguiente imagen:

**Imagen N°2: Dominio de Modelación**

Fuente: Elaboración propia a partir de CALPUFF

23

Modelación de Estimaciones Atmosféricas

DIA “Modificación y Modelación Planta Elaboradora de Harina y Aceite de Pescado, Salmonoil S.A.”

#### 3.7 Datos topográficos y uso de suelo

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

24

Modelación de Estimaciones Atmosféricas

DIA “Modificación y Modelación Planta Elaboradora de Harina y Aceite de Pescado, Salmonoil S.A.”

#### 3.8 Análisis y Caracterización de Calidad de Aire de la zona del proyecto

Para establecer la situación basal de la calidad de aire del área de influencia del Proyecto se

tomaron los datos de estación más cercana al proyecto, denominada estación de monitoreo de

calidad de aire “Mirasol”, emplazada a 28 kilómetros al noroeste del proyecto y a 33 kilómetros

del receptor [1] más lejano,

para el período comprendido

entre Enero de 2017 y

Diciembre de 2017. Cabe

señalar que dicha estación

sólo dispone de información

actualizada para MP2.5.

Figura N°3: Ubicación

Estación de Monitoreo

Calidad de Aire

Tabla N°3.6: Concentración (ug/m3) promedio de contaminantes en EMRP durante el año 2017

|MP2.5 (ug/m3)<br>concentración<br>promedio 24 hrs|PM 10 (ug/m3)<br>concentración<br>promedio 24 hrs|SO2(ug/m3)<br>concentración<br>promedio 24 hrs|CO(ug/m3)<br>concentración<br>promedio 24 hrs|NOX(ug/m3)<br>concentración<br>promedio 24 hrs|
|---|---|---|---|---|
|**30,2**|Sin información|Sin información|Sin información|Sin información|

Fuente: Registro Estación Mirasol

Figura N°3.1: Concentración promedio 24 Hrs de MP2.5 (ug/m3)

Fuente: Elaboración propia a partir de datos de Estación Mirasol

1 Receptor N°5

25

Modelación de Estimaciones Atmosféricas

DIA “Modificación y Modelación Planta Elaboradora de Harina y Aceite de Pescado, Salmonoil S.A.”

#### 3.9 Fuentes De Emisión

Para evaluar la dispersión atmosférica de las emisiones provenientes de la planta, se consideran 3

Escenarios de modelación, de acuerdo a la siguiente información;

Tabla N°3.7: Tasa de Emisión según Escenario de Modelación

|Escenario Fase Construcción|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|**Fuente de Emisión**|**MP 10**<br>**(ton/año)**|**MP 2,5**<br>**(ton/año)**|**NOx**<br>**(ton/año)**|**CO**<br>**(ton/año)**|**SOx**<br>**(ton/año)**|
|**Escarpe+Excavación+Transferencia de Material**|0,2559|0,116||||
|**Circulación por Caminos NO Pavimentados**|0,034|||||
|**Circulación por Caminos Pavimentados**|0,434|0,0915||||
|**Combustión Vehiculos**|0,000179||0,010444|0,00261|0,000272|
|**Combustón Maquinaria**|0,292||3,608|0,837||

|Escenario Fase Operación Situación Actual|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|**Fuente**|**MP 10**<br>**(ton/año)**|**MP 2,5**<br>**(ton/año)**|**NOx**<br>**(ton/año)**|**CO**<br>**(ton/año)**|**SOx**<br>**(ton/año)**|
|**Circulación por Caminos Pavimentados**|58,69|13,777||||
|**Combustión Vehiculos**|0,000277||0,016118|0,003891|0,000418|
|**Equipos Electrógenos**|0,232||7,95|1,819|0,013|
|**Calderas existentes**|16,39629|22,978|76,935|61,548|1130,426|

|Escenario Fase Operación Situación Proyectada|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|**Fuente**|**MP 10**<br>**(ton/año)**|**MP 2,5**<br>**(ton/año)**|**NOx**<br>**(ton/año)**|**CO**<br>**(ton/año)**|**SOx**<br>**(ton/año)**|
|**Circulación por Caminos Pavimentados**|58,727|13,777||||
|**Combustión Vehiculos**|0,000277||0,016118|0,003891|0,000418|
|**Equipos Electrógenos**|0,59||20,236|4,629|0,00102|
|**Calderas nuevas**|4,14|1,57|105|84|1543|

26

Modelación de Estimaciones Atmosféricas

DIA “Modificación y Modelación Planta Elaboradora de Harina y Aceite de Pescado, Salmonoil S.A.”

#### 3.10 Receptores

La ubicación de los receptores en estudio se indican en las siguientes tablas y la imagen a

continuación:

Tabla N°3.8: Emplazamiento Receptores

|N°|Receptor|Col3|Descripción|
|---|---|---|---|
|**Receptor**|**Coordenada E**|**Coordenada N**|Vivienda habitacional de 1 piso|
|R1|650.152|5.386.326|Vivienda habitacional de 1 piso|
|R2|649.882|5.385.500|Vivienda habitacional de 1 piso|
|R3|649.950|5.385.312|Vivienda habitacional de 1 piso|
|R4|650.456|5.382.131|Vivienda habitacional de 1 piso|
|R5|650.186|5.382.855|Vivienda habitacional de 1 piso|
|R6|646.767|5.382.968|Vivienda habitacional de 1 piso|
|R7|648.917|5.382.932|Vivienda habitacional de 1 piso|
|R8|654.055|5.382.778|Vivienda habitacional de 1 piso|
|R9|649.617|5.384.217|Vivienda habitacional de 1 piso|
|R10|650.151|5.388.119|Vivienda habitacional de 1 piso|
|R11|652.145|5.386.749|Vivienda habitacional de 1 piso|
|R12|662.248|5.398.696|Vivienda habitacional de 1 piso|
|R13|649.988|5.388.192|Vivienda habitacional de 1 piso|
|R14|649.976|5.385.715|Vivienda habitacional de 1 piso|
|R15|649.928|5.382.970|Planta Salmonoil|

Adicionalmente, se considera un grilla de receptores de de 100 km x 100 km con equispaciado de

1 km entre celdas.

27

Modelación de Estimaciones Atmosféricas

DIA “Modificación y Modelación Planta Elaboradora de Harina y Aceite de Pescado, Salmonoil S.A.”

Figura N°3.6: Emplazamiento Receptores Discretos

Fuente: Elaboración propia a partir de GoogleEarth

28

Modelación de Estimaciones Atmosféricas

DIA “Modificación y Modelación Planta Elaboradora de Harina y Aceite de Pescado, Salmonoil S.A.”

#### 4. RESULTADOS MODELACIÓN CALIDAD DEL AIRE

En la siguiente sección se entregan las concentraciones obtenidas utilizando el modelo

meteorológico de meso escala Weather Research Forecasting Model (WRF), como insumo para

CALPUFF View. De esta forma fue posible obtener las concentraciones de los contaminantes en

cada receptor según Escenario evaluado (Fase Construcción, Fase de Operación situación actual y

proyectada). Estos resultados no superan las concentraciones máximas referidas a las normas de

calidad primaria para los contaminantes MP10, MP2.5, CO, NOx y SO2 respectivamente.

#### 4.1 Determinación Área de Influencia

En base a la dispersión de los contaminantes evaluados, se determina como Área de Influencia,

aquel espacio comprendido por la dispersión del contaminante mayormente desplazado,

correspondiente al Monóxido de Carbono (CO) en su concentración de 8 horas, precisamente
aquella área en la cual se registra mayor concentración [2], en una extensión aproximada de 4,4 Km

para el eje Este-Oeste y 5,4 Km en el eje Norte-Sur, equivalente a 27,4 Km2. Para mayor detalle se

presenta gráfica del área de Influencia, según lo recién indicado;

**Gráfica N°4.1: Área de Influencia Componente Calidad de Aire**

Elaboración propia

2 Concentración entre los 5 y 18,4 ug/m 3

29

Modelación de Estimaciones Atmosféricas

DIA “Modificación y Modelación Planta Elaboradora de Harina y Aceite de Pescado, Salmonoil S.A.”

**4.1.1** **Concentración MP10**

El flujo de contaminantes se concentra en la zona inmediata al proyecto, desplazándose la pluma

de dispersión hacia el noreste, observándose una concentración máxima en el receptor N°1 para

la fase de Operación Actual como para la Situación Proyectada y en el receptor N°16 para la fase

de Construcción. Las concentraciones máximas no superan la norma primaria de calidad del aire

para MP10

Las coordenadas y concentraciones en períodos de concentración anual y diaria de receptores

discretos se presenta en la siguiente tabla.

**Tabla N°4.1: Concentración MP10** **en Receptores Discretos**

|DS 59 del MINSEGPRES,<br>Norma primaria de calidad<br>del aire para MP10;|Col2|Col3|Valor normado Concentración Diaria|Col5|Col6|Col7|Valor normado Concentración Anual|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**_DS 59 del MINSEGPRES,_**<br>**_Norma primaria de calidad_**<br>**_del aire para MP10;_**|**_DS 59 del MINSEGPRES,_**<br>**_Norma primaria de calidad_**<br>**_del aire para MP10;_**|**_DS 59 del MINSEGPRES,_**<br>**_Norma primaria de calidad_**<br>**_del aire para MP10;_**|**_150 ug/m3N_**|**_150 ug/m3N_**|**_150 ug/m3N_**|<br>**_50 ug/m3N_**|<br>**_50 ug/m3N_**|<br>**_50 ug/m3N_**|<br>**_50 ug/m3N_**|
|**_N°_**|**_Coordenadas_**<br>**_Receptor_**|**_Coordenadas_**<br>**_Receptor_**|**_Aporte Proyecto Concentración Diaria_**|**_Aporte Proyecto Concentración Diaria_**|**_Aporte Proyecto Concentración Diaria_**||<br>**_Aporte Proyecto Concentración Anual_**|<br>**_Aporte Proyecto Concentración Anual_**|<br>**_Aporte Proyecto Concentración Anual_**|
|**_N°_**|**_Coordenadas_**<br>**_Receptor_**|**_Coordenadas_**<br>**_Receptor_**|**_Fase_**<br>**_Construcción_**|**_Fase_**<br>**_Operación_**<br>**_Actual_**|**_Fase_**<br>**_Operación_**<br>**_Proyectada_**|<br>**_Fase_**<br>**_Construcción_**|<br>**_Fase_**<br>**_Construcción_**|**_Fase_**<br>**_Operación_**<br>**_Actual_**|**_Fase_**<br>**_Operación_**<br>**_Proyectada_**|
|**_N°_**|**_ x_**|**_ y_**|**_ug/m3_**|**_ug/m3_**|**_ug/m3_**||<br>**_ug/m3_**|**_ug/m3_**|**_ug/m3_**|
|1|650.152|5.386.326|1,641|**14,037**|**14,046**||<br>0,305|**3,903**|**3,865**|
|2|649.882|5.385.500|1,304|2,335|2,337||<br>0,224|0,546|0,554|
|3|649.950|5.385.312|1,684|1,778|1,875||<br>0,416|0,426|0,458|
|4|650.456|5.382.131|0,028|0,281|0,196||<br>0,005|0,091|0,069|
|5|650.186|5.382.855|0,052|0,421|0,269||<br>0,010|0,120|0,089|
|6|646.767|5.382.968|0,046|0,269|0,233||<br>0,007|0,095|0,090|
|7|648.917|5.382.932|0,023|0,541|0,229||<br>0,006|0,154|0,095|
|8|654.055|5.382.778|0,006|0,155|0,107||<br>0,001|0,049|0,041|
|9|649.617|5.384.217|0,310|1,119|0,496||<br>0,047|0,309|0,179|
|10|650.151|5.388.119|0,133|11,933|11,941||<br>0,035|3,682|3,651|
|11|652.145|5.386.749|0,033|0,436|0,434||<br>0,005|0,142|0,127|
|12|662.248|5.398.696|0,003|0,609|0,609||<br>0,001|0,220|0,219|
|13|649.988|5.388.192|0,129|10,786|10,795||<br>0,034|3,612|3,586|
|14|649.976|5.385.715|1,864|4,218|4,216||<br>0,324|1,032|1,031|
|15|649.928|5.382.970|0,047|0,442|0,271||<br>0,009|0,121|0,088|
|16|650.210|5.385.752|**12,084**|4,614|4,617||<br>**4,739**|1,185|1,184|

Para mayor comprensión en Apéndice N°1 se presentan imágenes según los receptores evaluados

en sus diversos períodos. Para luego presentar la pluma de dispersión representada por

isoconcentraciones que reflejan el resultado de la modelación.

30

Modelación de Estimaciones Atmosféricas

DIA “Modificación y Modelación Planta Elaboradora de Harina y Aceite de Pescado, Salmonoil S.A.”

**4.1.2** **Concentración MP2.5**

El flujo de contaminantes se concentra en la zona inmediata al proyecto, desplazándose la pluma

de dispersión hacia el sector noreste observándose una concentración máxima en el receptor N°1

para la fase de Operación Actual así como en Situación Proyectada, y en menor concentración

para el receptor N°16 en la fase de Construcción. La concentraciones máximas no superan la

norma primaria de calidad del aire para MP2.5.

Para este contaminante se considera una situación basal en concentración diaria de 30.2 (ug/m 3) [3],

que sumado a la concentración máxima arrojada por el modelo, correspondiente al receptor N°1,
la concentración final [4] sobre éste alcanzaría los 33,5 (ug/m3). Cabe señalar que dicho valor se

encuentra bajo el límite establecido en DS 12/11 del MMA, Norma primaria de calidad del aire

para MP2.5, por cuanto, el proyecto no generaría eventos de latencia ni saturación sobre la zona

modelada, toda vez, que a nivel porcentual equivale al 67% del valor normado, ello durante el

peor escenario evaluado (Fase de Operación Actual y Proyectada).

Las coordenadas y concentraciones en períodos de concentración anual y diaria de receptores

discretos se presenta en la siguiente tabla.

**Tabla N°4.2: Concentración MP2,5** **en Receptores Discretos**

|DS 12/11 del MMA, Norma<br>primaria de calidad del aire<br>para MP2.5;|Col2|Col3|Valor normado Concentración Diaria|Col5|Col6|Valor normado Concentración Anual|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**_DS 12/11 del MMA, Norma_**<br>**_primaria de calidad del aire_**<br>**_para MP2.5;_**|**_DS 12/11 del MMA, Norma_**<br>**_primaria de calidad del aire_**<br>**_para MP2.5;_**|**_DS 12/11 del MMA, Norma_**<br>**_primaria de calidad del aire_**<br>**_para MP2.5;_**|**_50 ug/m3N_**|**_50 ug/m3N_**|**_50 ug/m3N_**|**_20 ug/m3N_**|**_20 ug/m3N_**|**_20 ug/m3N_**|
|**_N°_**|**_Coordenadas_**<br>**_ Receptor_**|**_Coordenadas_**<br>**_ Receptor_**|**_Aporte Proyecto Concentración Diaria_**|**_Aporte Proyecto Concentración Diaria_**|**_Aporte Proyecto Concentración Diaria_**|**_Aporte Proyecto Concentración Anual_**|**_Aporte Proyecto Concentración Anual_**|**_Aporte Proyecto Concentración Anual_**|
|**_N°_**|**_Coordenadas_**<br>**_ Receptor_**|**_Coordenadas_**<br>**_ Receptor_**|**_Fase_**<br>**_Construcción_**|**_Fase_**<br>**_Operación_**<br>**_Actual_**|**_Fase Operación_**<br>**_Proyectada_**|**_Fase_**<br>**_Construcción_**|**_Fase_**<br>**_Operación_**<br>**_Actual_**|**_Fase Operación_**<br>**_Proyectada_**|
|**_N°_**|** x**|** y**|**_ug/m3_**|**_ug/m3_**|**_ug/m3_**|**_ug/m3_**|**_ug/m3_**|**_ug/m3_**|
|1|650.152|5.386.326|0,215|**3,30**|**3,29**|0,04|**1,02**|**0,90**|
|2|649.882|5.385.500|0,169|0,58|0,55|0,02|0,14|0,13|
|3|649.950|5.385.312|0,306|0,52|0,42|0,06|0,12|0,10|
|4|650.456|5.382.131|0,003|0,26|0,05|0,00|0,06|0,02|
|5|650.186|5.382.855|0,007|0,45|0,07|0,00|0,08|0,02|
|6|646.767|5.382.968|0,007|0,15|0,06|0,00|0,03|0,02|
|7|648.917|5.382.932|0,003|0,65|0,07|0,00|0,13|0,02|
|8|654.055|5.382.778|0,001|0,12|0,03|0,00|0,02|0,01|
|9|649.617|5.384.217|0,054|1,42|0,14|0,01|0,29|0,05|
|10|650.151|5.388.119|0,019|2,91|0,28|0,01|0,92|0,86|
|11|652.145|5.386.749|0,005|0,26|0,10|0,00|0,06|0,03|

3 Según registros de SINCA. MMA Estación Mirasol. Puerto Montt.
4 Concentración final (concentración estimada por el modelo más la situación basal)

31

Modelación de Estimaciones Atmosféricas

DIA “Modificación y Modelación Planta Elaboradora de Harina y Aceite de Pescado, Salmonoil S.A.”

|12|662.248|5.398.696|0,001|0,15|0,14|0,00|0,06|0,05|
|---|---|---|---|---|---|---|---|---|
|13|649.988|5.388.192|0,018|2,57|2,53|0,01|0,89|0,84|
|14|649.976|5.385.715|0,191|0,98|0,99|0,03|0,26|0,24|
|15|649.928|5.382.970|0,006|0,47|0,07|0,00|0,08|0,02|
|16|650.210|5.385.752|**1,629**|1,08|1,08|**0,44**|0,28|0,28|

Para mayor comprensión en Apéndice N°1 se presentan imágenes de la pluma de dispersión

representada por isoconcentraciones que reflejan el resultado de la modelación.

**4.1.3** **Concentración CO**

El flujo de contaminantes se concentra en la zona inmediata al proyecto, desplazándose la pluma

de dispersión hacia el noreste observándose una concentración máxima en el receptor N°1 para

la fase de Operación Actual y Situación Proyectada. Mientras que para la fase de construcción se

observa mayor concentración en el receptor N°16. Para lo que respecta en la fase de Operación
Actual en concentración 8 Horas se registra mayor concentración en el receptor N°9 [5] . Las

concentraciones máximas no superan la norma primaria de calidad del aire para CO.

Las coordenadas y concentraciones en períodos de concentración horarial y 8 horas de receptores

discretos se presenta en la siguiente tabla.

**Tabla N°4.3: Concentración CO en Receptores Discretos**

|DS 115 del MINSEGPRES,<br>Norma primaria de calidad<br>del aire para CO;|Col2|Col3|Valor normado Concentración Horaria<br>50 ug/m3N|Col5|Col6|Valor normado Concentración 8 Horas<br>30 mg/m3N|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**_N°_**|**_Coordenadas_**<br>**_Receptor_**|**_Coordenadas_**<br>**_Receptor_**|**_Aporte Proyecto Concentración Horaria_**|**_Aporte Proyecto Concentración Horaria_**|**_Aporte Proyecto Concentración Horaria_**|**_Aporte Proyecto Concentración 8 Horas_**|**_Aporte Proyecto Concentración 8 Horas_**|**_Aporte Proyecto Concentración 8 Horas_**|
|**_N°_**|**_Coordenadas_**<br>**_Receptor_**|**_Coordenadas_**<br>**_Receptor_**|**_Fase_**<br>**_Construcción_**<br>**_mg/m3_**|**_Fase_**<br>**_Operación_**<br>**_Actual_** <br>**_mg/m3_**|**_Fase_**<br>**_Operación_**<br>**_Proyectada_** <br>**_mg/m3_**|**_Fase_**<br>**_Construcción_** <br>**_mg/m3_**|**_Fase_**<br>**_Operación_**<br>**_Actual_** **_mg/m3_**|**_Fase_**<br>**_Operación_**<br>**_Proyectada_** <br>**_mg/m3_**|
|**_N°_**|**_x _**|**_y _**|**_y _**|**_y _**|**_y _**|**_y _**|**_y _**|**_y _**|
|1|650.152|5.386.326|7,091*10E-3|**1,037*10E-2**|**15,703*10E-3**|4,331*10E-3|5,595*10E-3|**9,399*10E-3**|
|2|649.882|5.385.500|5,223*10E-3|5,128*10E-4|5,945*10E-3|2,932*10E-3|1,174*10E-3|3,177*10E-3|
|3|649.950|5.385.312|7,889*10E-3|1,181*10-E-3|7,966*10E-3|4,748*10E-3|1,261*10E-3|4,497*10E-3|
|4|650.456|5.382.131|0,136*10E-3|3,058*10E-3|4,239*10E-3|0,078*10E-3|1,191*10E-3|1,729*10E-3|
|5|650.186|5.382.855|0,267*10E-3|4,021*10E-3|5,589*10E-3|0,014*10E-3|1,855*10E-3|2,630*10E-3|
|6|646.767|5.382.968|0,245*10E-3|5,836*10E-4|9,613*10E-3|0,138*10E-3|7,241*10E-4|1,146*10E-3|
|7|648.917|5.382.932|0,139*10E-3|4,959*10E-3|6,815*10E-3|0,071*10E-3|3,073*10E-3|4,281*10E-3|
|8|654.055|5.382.778|0,027*10E-3|1,247*10E-3|1,780*10E-3|0,012*10E-3|6,119*10E-4|8,662*10E-4|
|9|649.617|5.384.217|1,190*10E-3|1,009*10E-2|13,838*10E-3|0,863*10E-3|**6,452*10E-3**|8,828*10E-3|

5 En su Concentración 8 Horas

32

Modelación de Estimaciones Atmosféricas

DIA “Modificación y Modelación Planta Elaboradora de Harina y Aceite de Pescado, Salmonoil S.A.”

|10|650.151|5.388.119|0,417*10E-3|3,745*10E-3|5,603*10E-3|0,302*10E-3|2,231*10E-3|3,249*10E-3|
|---|---|---|---|---|---|---|---|---|
|11|652.145|5.386.749|0,139*10E-3|2,278*10E-3|3,320*10E-3|0,090*10E-3|1,220*10E-3|1,820*10E-3|
|12|662.248|5.398.696|0,004*10E-3|1,750*10E-4|0,2514*10E-3|0,0023*10E-3|1,053*10E-4|0,151*10E-3|
|13|649.988|5.388.192|0,471*10E-3|3,736*10E-3|5,6021*10E-3|0,3237*10E-3|2,045*10E-3|3,021*10E-3|
|14|649.976|5.385.715|7,700*10E-3|5,853*10E-4|3,716*10E-3|4,216*10E-3|1,336*10E-3|3,243*10E-3|
|15|649.928|5.382.970|0,2632*10E-3|4,154*10E-3|5,848*10E-3|0,124*10E-3|2,056*10E-3|3,929*10E-3|
|16|650.210|5.385.752|**50,447*10E-3**|2,533*10E-4|0,454*10E-3|**33,077*10E-3**|6,504*10E-4|1,320*10E-3|

Para mayor comprensión en Apéndice N°1 se presentan imágenes de la pluma de contaminación

representada por isoconcentraciones que reflejan el resultado de la modelación.

33

Modelación de Estimaciones Atmosféricas

DIA “Modificación y Modelación Planta Elaboradora de Harina y Aceite de Pescado, Salmonoil S.A.”

**4.1.4** **Concentración NOx**

El flujo de contaminantes se concentra en la zona inmediata al proyecto, desplazándose la pluma

de dispersión hacia el sector noreste, observándose una concentración máxima en el receptor N°

3, tanto para la fase Construcción como para la fase de Operación Situación Proyectada.

Mientras que para la fase de Operación Actual, se registra mayor concentración en los receptores
N°1 [6] y N°9 [7] . Las concentraciones máximas no supera la norma primaria de calidad del aire para

NOx.

Las coordenadas y concentraciones en períodos de concentración horaria y anual de receptores

discretos se presenta en la siguiente tabla.

**Tabla N°4.4: Concentración NOx en Receptores Discretos**

|DS 115 del MINSEGPRES,<br>Norma primaria de calidad<br>del aire para NOx|Col2|Col3|Valor normado Concentración Horaria<br>400 ug/m3N|Col5|Col6|Valor normado Concentración Anual<br>100 ug/m3N|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**_N°_**|**_Coordenadas_**<br>**_Receptor_**|**_Coordenadas_**<br>**_Receptor_**|**_Aporte Proyecto Concentración Horaria_**|**_Aporte Proyecto Concentración Horaria_**|**_Aporte Proyecto Concentración Horaria_**|**_Aporte Proyecto Concentración Anual_**|**_Aporte Proyecto Concentración Anual_**|**_Aporte Proyecto Concentración Anual_**|
|**_N°_**|**_Coordenadas_**<br>**_Receptor_**|**_Coordenadas_**<br>**_Receptor_**|**_Fase_**<br>**_Construcción_** <br>**_ug/m3_**|**_Fase_**<br>**_Operación_**<br>**_Actual_** <br>**_ug/m3_**|**_Fase_**<br>**_Operación_**<br>**_Proyectada_** <br>**_ug/m3_**|**_Fase_**<br>**_Construcción_** <br>**_ug/m3_**|**_Fase_**<br>**_Operación_**<br>**_Actual_** <br>**_ug/m3_**|**_Fase_**<br>**_Operación_**<br>**_Proyectada_** <br>**_ug/m3_**|
|**_N°_**|**_x _**|**_y _**|**_y _**|**_y _**|**_y _**|**_y _**|**_y _**|**_y _**|
|1|650.152|5.386.326|30,570|**12,965**|29,092|1,3223|0,4208|1,4634|
|2|649.882|5.385.500|22,518|0,641|23,121|1,3223|0,0479|0,5877|
|3|649.950|5.385.312|**34,437**|1,476|**32,616**|**2,2140**|0,0653|**1,5317**|
|4|650.456|5.382.131|0,587|3,823|5,695|0,0508|0,1488|0,2572|
|5|650.186|5.382.855|1,153|5,027|7,529|0,0365|0,2100|0,3629|
|6|646.767|5.382.968|1,057|0,729|2,221|0,0044|0,0340|0,0773|
|7|648.917|5.382.932|0,602|6,199|8,700|0,2703|0,3876|0,6188|
|8|654.055|5.382.778|0,119|1,558|2,403|0,0864|0,0503|0,0841|
|9|649.617|5.384.217|5,141|12,608|17,893|0,0230|** 0,8547**|1,3541|
|10|650.151|5.388.119|1,802|4.681|8,416|0,0009|0,2292|0,4442|
|11|652.145|5.386.749|0,599|2,847|4,927|0,0230|0,1011|0,1809|
|12|662.248|5.398.696|0,017|0,219|0,353|0,0009|0,0112|0,0187|
|13|649.988|5.388.192|2,033|4,670|8,518|0,0859|0,2022|0,4048|
|14|649.976|5.385.715|33,195|0,732|9,490|1,1204|0,0528|0,3082|
|15|649.928|5.382.970|1,135|5,192|7,787|0,0478|0,2183|0,3605|
|16|650.210|5.385.752|217,460|0,312|0,814|25,8870|0,0264|0,0928|

6 En su Concentración Horaria
7 En su Concentración Anual

34

Modelación de Estimaciones Atmosféricas

DIA “Modificación y Modelación Planta Elaboradora de Harina y Aceite de Pescado, Salmonoil S.A.”

Para mayor comprensión en Apéndice N°1 se presentan imágenes de la pluma de dispersión

representada por isoconcentraciones que reflejan el resultado de la modelación.

**4.1.5** **Concentración SO2**

El flujo de contaminantes se concentra en la zona inmediata al proyecto, desplazándose la pluma

de dispersión hacia el sector noreste, observándose una concentración máxima en el receptor

N°9 durante la fase de Operación Actual y Situación Proyectada.

Las coordenadas y concentraciones en períodos de concentración anual y diaria de receptores

discretos se presenta en la siguiente tabla.

**Tabla N°4.5: Concentración SO2 en Receptores Discretos**

|DS 113 del MINSEGPRES,<br>Norma primaria de calidad<br>del aire para SO2|Col2|Col3|Valor normado Concentración Diaria<br>250 ug/m3N|Col5|Col6|Valor normado Concentración Anual<br>80 ug/m3N|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**_N°_**|**_Coordenadas_**<br>**_Receptor_**|**_Coordenadas_**<br>**_Receptor_**|**_Aporte Proyecto Concentración Diaria_**|**_Aporte Proyecto Concentración Diaria_**|**_Aporte Proyecto Concentración Diaria_**|**_Aporte Proyecto Concentración Anual_**|**_Aporte Proyecto Concentración Anual_**|**_Aporte Proyecto Concentración Anual_**|
|**_N°_**|**_Coordenadas_**<br>**_Receptor_**|**_Coordenadas_**<br>**_Receptor_**|**_Fase_**<br>**_Construcción_**|**_Fase_**<br>**_Operación_**<br>**_Actual_**|**_Fase_**<br>**_Operación_**<br>**_Proyectada_**|**_Fase_**<br>**_Construcción_**|**_Fase_**<br>**_Operación_**<br>**_Actual_**|**_Fase_**<br>**_Operación_**<br>**_Proyectada_**|
|**_N°_**|**_x _**|**_y _**|**_ug/m3_**|**_ug/m3_**|**_ug/m3_**|**_ug/m3_**|**_ug/m3_**|**_ug/m3_**|
|1|650.152|5.386.326|**0,0001**|63,638|86,876|0,0000|6,1824|8,4403|
|2|649.882|5.385.500|0,0000|19,765|26,986|0,0000|0,7041|0,9619|
|3|649.950|5.385.312|0,0000|22,923|31,290|0,0000|0,9589|1,3114|
|4|650.456|5.382.131|0,0000|15,105|20,618|0,0000|2,1867|2,9849|
|5|650.186|5.382.855|0,0000|22,077|30,136|0,0000|3,0861|4,2125|
|6|646.767|5.382.968|0,0000|11,300|15,424|0,0000|0,4995|0,6820|
|7|648.917|5.382.932|0,0000|35,860|48,949|0,0000|5,6962|7,7753|
|8|654.055|5.382.778|0,0000|6,779|9,254|0,0000|0,7393|1,0092|
|9|649.617|5.384.217|0,0000|** 75,191**|**102,640**|0,0000|** 12,558**|**17,1410**|
|10|650.151|5.388.119|0,0000|30,012|40,967|0,0000|3,3679|4,5973|
|11|652.145|5.386.749|0,0000|12,720|17,363|0,0000|1,4855|2,0277|
|12|662.248|5.398.696|0,0000|1,1715|1,599|0,0000|0,1642|0,2241|
|13|649.988|5.388.192|0,0000|31,692|43,260|0,0000|2,9708|4,0553|
|14|649.976|5.385.715|0,0000|22,128|30,204|0,0000|0,7759|1,0596|
|15|649.928|5.382.970|0,0000|26,047|35,554|0,0000|3,2074|4,3781|
|16|650.210|5.385.752|0,0000|10,568|14,425|0,0000|0,3874|0,5289|

35

Modelación de Estimaciones Atmosféricas

DIA “Modificación y Modelación Planta Elaboradora de Harina y Aceite de Pescado, Salmonoil S.A.”

Para mayor comprensión en Apéndice N°1 se presentan imágenes de la pluma de dispersión

representada por isoconcentraciones que reflejan el resultado de la modelación.

36

Modelación de Estimaciones Atmosféricas

DIA “Modificación y Modelación Planta Elaboradora de Harina y Aceite de Pescado, Salmonoil S.A.”

### 5. CONCLUSIÓN

A partir de las modelaciones realizadas con respecto a las emisiones atmosféricas para las fases

de Construcción, Operación Actual y Situación Proyectada, se presentan las siguientes

conclusiones:

Para la determinación de la situación basal de la calidad del aire de los receptores evaluados,

se consideró el registro existente en la Estación de Monitoreo Mirasol ubicada en la comuna

de Puerto Montt, por considerarse aquella más cercana al proyecto con registros
actualizados [8] .

El flujo de contaminantes se concentra en la zona inmediata dispersándose hacia el sector

noreste. Las concentraciones obtenidas del modelo corresponden a;

`o` Para el caso del contaminante MP10, se observa una concentración diaria máxima de

14 ug/m 3 de MP10 en el receptor N°1 para la fase de Operación Actual y Situación

Proyectada. En menor concentración para el receptor N°16 en la fase de Construcción

(12 ug/m 3 ).

`o` En relación al MP2.5 se registra una concentración máxima diaria de 3,3 ug/m 3 en el

receptor N°1 para la fase de Operación tanto actual como proyectada. Para la fase de

Construcción presentaría un valor máximo de 1,6 ug/m 3 en el receptor N°16. Cabe

señalar que, para este compuesto se considera una situación basal en concentración

diaria de 30.2 ug/m3 que sumado a la concentración máxima en el receptor N°1,

alcanzaría una concentración final de 33,5 ug/m 3 . Dicho valor se encuentra bajo el

límite establecido en DS 12/11 del MMA, Norma primaria de calidad del aire para

MP2.5, por cuanto, el proyecto no generaría eventos de latencia ni saturación sobre la

zona modelada, toda vez, que a nivel porcentual equivale al 67% del valor normado,

ello durante el peor escenario evaluado (Fase de Operación Actual y Proyectada).

`o` Para el contaminate CO el resultado de la modelación arroja una concentración

máxima horaria de 0,01 mg/m 3 durante la fase Operación Actual, 0,015 mg/m 3 en la

Situación Proyectada, ambos casos para el receptor N°1. Mientras que durante la fase

de Construcción se estima una concentración máxima de 0,05 mg/m 3 en el receptor

N°16.

8 La Estación sólo cuenta con registros actualizados de MP2.5.

37

Modelación de Estimaciones Atmosféricas

DIA “Modificación y Modelación Planta Elaboradora de Harina y Aceite de Pescado, Salmonoil S.A.”

`o` En tanto, para el NOx durante la fase de Operación Actual el modelo arroja una

concentración máxima de 12,9 ug/m 3 en receptor N°1. En la fase de Construcción y

Operación Proyectada el valor máximo observado corresponde a 34 ug/m 3 en el

receptor N°3.

`o` Y por último para el contaminante SO2 la concentración máxima diaria corresponde a

75 ug/m3 para la fase Operación Actual y 102 ug/m 3 para la Fase Operación Situación

Proyectada, ambos en el receptor N°9. Mientras que para la fase de Construcción sólo

se observa una concentración máxima de 0,0001 ug/m 3 para el receptor N°1.

De los parámetros en estudio posible señalar que el aporte del proyecto en los receptores

discretos y en la grilla de receptores evaluados no supera la Normativa de Calidad Primaria en

las concentraciones horarias, diarias, y anuales.

De lo expuesto anteriormente se concluye que:

Los aportes del proyecto a las concentraciones de los contaminantes en estudio (MP 2.5, MP10,

MPS, CO, NOx y SO2), no presentan riesgos para la salud de la población, toda vez que los

resultados no superan las normas de calidad primaria de los contaminantes estudiados.

Los resultados obtenidos de la Modelación de Emisiones Atmosféricas, permiten concluir que
el proyecto _**“DÍA Modificación y Modernización Planta Elaborada de Harina y Aceite de**_

_**Pescado,Salmonoil S.A.”**_ no aporta significativamente a las concentraciones de calidad del aire

de la zona modelada y no generaría eventos de latencia ni saturación de los contaminantes

estudiados.

38

Modelación de Estimaciones Atmosféricas

DIA “Modificación y Modelación Planta Elaboradora de Harina y Aceite de Pescado, Salmonoil S.A.”

### 6. REFERENCIAS

 - Registro de Monitoreo Calidad de Aire y Meteorológico Estación Mirasol.

 - Pontificia Universidad Católica de Chile, Educación Continua UC, Escuela de Ingeniería.

(2014). Manual de Usuario CALPUFF View.

 - Scire, J. S., Strimaitis, D. G., y Yamartino, R. J., 2000a. A User’s Guide for the CALPUFF

Dispersion Model (Version 5). Earth Tech Inc., Concord, Massachusetts.

39