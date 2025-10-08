---
title: Sin título
author: Anexo 1.5 Estudio de emisiones atmosféricas, DIA “Data Center Chile 2”
date: D:20250416202301-04'00'
language: es
type: report
pages: 70
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Proyecto DIA “Conjunto Habitacional Don Vicente Bosquemar”
-->

# Proyecto DIA “Conjunto Habitacional Don Vicente Bosquemar”

### Informe de modelación de dispersión de emisiones atmosféricas

Elaborado por:

GIZA Ingeniería SpA
[https://gizaingenieria.com/](https://gizaingenieria.com/)

Región Metropolitana, abril de 2025

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente_
_1_
_Bosquemar”_

**ÍNDICE**

**1. INTRODUCCIÓN ............................................................................................................................................ 5**

**2. OBJETIVOS .................................................................................................................................................... 5**

2.1. O BJETIVO G ENERAL ............................................................................................................................................ 5

2.2. O BJETIVOS E SPECÍFICOS ....................................................................................................................................... 5

**3. ÁREA DE ESTUDIO ......................................................................................................................................... 5**
**3. METODOLOGÍA ............................................................................................................................................. 8**

3.1. WRF ............................................................................................................................................................... 8

3.2. CALPUFF ........................................................................................................................................................ 8

**4. NORMATIVA ................................................................................................................................................. 8**

4.1. M ARCO L EGAL ................................................................................................................................................... 8

4.2. L ÍNEA DE B ASE ................................................................................................................................................... 9

**5. ANÁLISIS METEOROLÓGICO ........................................................................................................................ 10**

5.1. R ECOPILACIÓN DE LA I NFORMACIÓN ..................................................................................................................... 10

5.2. S ERIES DE T IEMPO DE LA VELOCIDAD DEL VIENTO .................................................................................................... 11

5.3. R OSAS DE V IENTO DE LA V ELOCIDAD DEL V IENTO .................................................................................................... 14

5.4. C ICLO E STACIONAL DE LA V ELOCIDAD DEL V IENTO .................................................................................................. 16

5.5. C ICLO D IARIO V ELOCIDAD DEL V IENTO ................................................................................................................. 16

5.5. S ERIE DE TIEMPO DE LA TEMPERATURA ................................................................................................................. 18

5.7. C ICLO ESTACIONAL DE LA TEMPERATURA ............................................................................................................... 19

5.5. C ICLO DIARIO DE LA TEMPERATURA ...................................................................................................................... 19

**6. ANÁLISIS DE LA INCERTIDUMBRE ................................................................................................................ 21**

6.1. R AÍZ DEL E RROR C UADRÁTICO M EDIO .................................................................................................................. 21

6.2. S ESGO ............................................................................................................................................................ 21

6.3. C OEFICIENTE DE C ORRELACIÓN ........................................................................................................................... 21

**7. DATOS DE ENTRADA AL MODELO ............................................................................................................... 23**

7.1. E MISIONES ...................................................................................................................................................... 23

7.2. R ECEPTORES .................................................................................................................................................... 26

7.3. T OPOGRAFÍA ................................................................................................................................................... 28

7.4. M ETEOROLOGÍA ............................................................................................................................................... 28

**8. RESULTADOS DE LA MODELACIÓN .............................................................................................................. 29**

8.1. R ESULTADOS ................................................................................................................................................... 29

8.2. A NÁLISIS N ORMATIVO ....................................................................................................................................... 33

8.3. A NÁLISIS DEL I MPACTO S IGNIFICATIVO .................................................................................................................. 38

8.4. P UNTOS DE M ÁXIMO I MPACTO ........................................................................................................................... 40

8.5. I SOCONCENTRACIONES ...................................................................................................................................... 42

**9. ÁREA DE INFLUENCIA .................................................................................................................................. 67**

**10. CONCLUSIONES ......................................................................................................................................... 70**

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente_
_2_
_Bosquemar”_

**ÍNDICE DE TABLAS**

Tabla 1 Normativa Ambiental Vigente ..................................................................................................................... 8

Tabla 2 Estación de Monitoreo................................................................................................................................. 9

Tabla 3 Línea de Base Estación Mirasol .................................................................................................................... 9

Tabla 4 Ubicación Estación y Variables Meteorológica Analizada.......................................................................... 11
Tabla 5 Estadísticas de Datos Meteorológicos Analizados ..................................................................................... 11
Tabla 6 Estadísticas de Datos Meteorológicos Analizados de Temperatura .......................................................... 18
Tabla 7 Estadígrafos de evaluación de desempeño del modelo para la velocidad del viento ............................... 22
Tabla 8 Emisiones Atmosféricas Fase de Construcción más Operación ................................................................. 23
Tabla 9 Parámetros Ingresados a Cada Fuente ...................................................................................................... 23
Tabla 10 Emisiones Ingresadas al Modelo Construcción y Operación Año 7 ......................................................... 24
Tabla 11 Emisiones Ingresadas Operación Año 9 ................................................................................................... 24
Tabla 12 Receptores Considerados en el Proyecto ................................................................................................ 26
Tabla 13 Concentraciones obtenidas en los Receptores Norma Primaria Escenario Construcción más Operación

Año 7 .............................................................................................................................................................. 29

Tabla 14 Concentraciones obtenidas en los Receptores Norma Primaria Escenario Operación año 9 ................. 31
Tabla 15 Concentraciones del Proyecto Comparados con la Normativa Primaria, Escenario Construcción más

Operación Año 7 ............................................................................................................................................ 34
Tabla 16 Concentraciones del Proyecto Comparados con la Normativa Primaria, Escenario Operación Año 9 .... 36
Tabla 17 Análisis de Impacto Significativo MP2,5 μg/m3, Escenario Construcción más Operación del año 7 ...... 38
Tabla 18 Análisis de Impacto Significativo MP2,5 μg/m3, Escenario Operación del año 9 .................................... 39
Tabla 19 Punto Máximo Impacto, Escenario Construcción más Operación del año 7 ........................................... 40
Tabla 20 Punto Máximo Impacto, Escenario Operación del año 9 ......................................................................... 40

**ÍNDICE DE FIGURAS**

Figura 1 Ubicación del Proyecto ............................................................................................................................... 6
Figura 2 Dominio de Modelación ............................................................................................................................. 7
Figura 3 Serie observada y modelada de la velocidad del viento - Estación Alerce Periodo 01 enero 2022 - 31

diciembre 2022 .............................................................................................................................................. 12

Figura 4 Serie observada y modelada de la dirección del viento - Estación Alerce Periodo 01 enero 2022 - 31

diciembre 2022 .............................................................................................................................................. 13

Figura 5 Rosa de Viento Ciclo Completo - Estación Alerce Periodo 01 enero 2022 - 31 diciembre 2022 ............. 14
Figura 6 Variabilidad temporal del viento - Estación Alerce .................................................................................. 15
Figura 7 Ciclo estacional del viento - Estación Alerce Periodo 01 enero 2022 - 31 diciembre 2022 .................... 16
Figura 8 Ciclo diario de la velocidad del viento observada y modelada- Estación Alerce Periodo 01 enero 202231 diciembre 2022 ......................................................................................................................................... 17

Figura 9 Ciclo diario de la dirección del viento observada y modelada- Estación Alerce Periodo 01 enero 202231 diciembre 2022 ......................................................................................................................................... 18

Figura 10 Serie de tiempo de la temperatura observada y modelada- Estación Alerce Periodo 01 enero 202231 diciembre 2022 ......................................................................................................................................... 19

Figura 11 Ciclo estacional de la temperatura - Estación Alerce Periodo 01 enero 2022 - 31 diciembre 2022 .... 19
Figura 12 Serie de tiempo de la temperatura observada y modelada- Estación Alerce Periodo 01 enero 202231 diciembre 2022 ......................................................................................................................................... 20

Figura 13 Ubicación Geográfica de los Receptores ................................................................................................ 27
Figura 14 Curvas de Nivel del Área de Estudio ....................................................................................................... 28
Figura 15 Ubicación de los PMI, Escenario Construcción Más Operación Año 7 ................................................... 41
Figura 16 Ubicación de los PMI, Escenario Operación Año 9 ................................................................................. 42
Figura 17 Isolíneas de Concentración MP-10 Promedio Anual, Escenario Construcción más Operación Año 7 ... 43

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente_
_3_
_Bosquemar”_

Figura 18 Isolíneas de Concentración MP-10 Percentil 98, Escenario Construcción más Operación Año 7 .......... 44
Figura 19 Isolíneas Concentración MP-2,5 Media Anual, Escenario Construcción más Operación Año 7 ............. 45
Figura 20 Isolíneas Concentración MP-2,5 Percentil 98, Escenario Construcción más Operación Año 7 .............. 46
Figura 21 Isolíneas de Concentración NO2 Media Anual, Escenario Construcción más Operación Año 7 ............ 47
Figura 22 Isolíneas de Concentración NO2, Percentil 99 1 Hora, Escenario Construcción más Operación Año 7 . 48
Figura 23 Isolíneas de Concentración NO2, Percentil 99 24 Horas, Escenario Construcción más Operación Año 7

....................................................................................................................................................................... 49

Figura 24 Isolíneas de Concentración CO Percentil 99 1 Hora, Escenario Construcción más Operación Año 7 .... 50
Figura 25 Isolíneas de Concentración CO Percentil 99 8 Horas, Escenario Construcción más Operación Año 7 ... 51
Figura 26 Isolíneas de Concentración SO2 Media Anual, Escenario Construcción más Operación Año 7 ............. 52
Figura 27 Isolíneas de Concentración SO2, Percentil 99 24 Horas, Escenario Construcción más Operación Año 7

....................................................................................................................................................................... 53

Figura 28 Isolíneas de Concentración SO2, Percentil 99 1 Hora, Escenario Construcción más Operación Año 7 .. 54
Figura 29 Isolíneas de Concentración MP-10 Promedio Anual, Escenario Operación Año 9 ................................. 55
Figura 30 Isolíneas de Concentración MP-10 Percentil 98, Escenario Operación Año 9 ........................................ 56
Figura 31 Isolíneas Concentración MP-2,5 Media Anual, Escenario Operación Año 9 .......................................... 57
Figura 32 Isolíneas Concentración MP-2,5 Percentil 98, Escenario Operación Año 9 ............................................ 58
Figura 33 Isolíneas de Concentración NO2 Media Anual, Escenario Operación Año 9 .......................................... 59
Figura 34 Isolíneas de Concentración NO2 Percentil 99, 1 Hora, Escenario Operación Año 9 ............................... 60
Figura 35 Isolíneas de Concentración NO2 Percentil 99, 24 Horas, Escenario Operación Año 9 ........................... 61
Figura 36 Isolíneas de Concentración CO Percentil 99 1 Hora, Escenario Operación Año 9 .................................. 62
Figura 37 Isolíneas de Concentración CO Percentil 99 8 Horas, Escenario Operación Año 9 ................................ 63
Figura 38 Isolíneas de Concentración SO2 Media Anual, Escenario Operación Año 9 ........................................... 64
Figura 39 Isolíneas de Concentración SO2 Percentil 99 24 Horas, Escenario Operación Año 9 ............................. 65
Figura 40 Isolíneas de Concentración SO2, Percentil 99 1 Hora, Escenario Operación.......................................... 66
Figura 41 Área de Influencia del Proyecto Fase de Construcción más Operación Año 7 ....................................... 68
Figura 42 Área de Influencia del Proyecto Fase Operación Año 9.......................................................................... 69

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente_
_4_
_Bosquemar”_

**1. INTRODUCCIÓN**

El proyecto denominado _DIA “Conjunto Habitacional Don Vicente Bosquemar”_, consiste en un conjunto habitacional
acogido al D.F.L N°2 de 1959 y al D.L. N°1552 de 1979, con un total de 865 viviendas, 946 estacionamientos
vehiculares, 6 salas múltiples y 4 locales comerciales, que se desarrolla en 3 lotes.

El desarrollo habitacional de las etapas A y B emplazadas en el Lote W2 se encuentran ejecutadas y recibidas por
la Dirección de Obras Municipales de Puerto Montt. Considera un total de 232 viviendas, 237 estacionamientos y

4 locales comerciales.

El segundo desarrollo inmobiliario corresponde a la construcción y operación de la etapa C (casas) en el Lote W3A, y las etapas D, E, F y G (departamentos) en el Lote W3-B, que ambos vienen a sumar 633 viviendas y 711
estacionamientos vehiculares a las etapas ejecutadas y recepcionadas del Lote W2. La fase de construcción de las
etapas del Lote W3-A y Lote W3-B tendrá una duración total de 93 meses, es decir, 7 años y nueve meses
aproximadamente. Se aclara que, habrá meses sin actividad en obra.

El siguiente informe da cuenta de la modelación de la dispersión de los contaminantes material particulado
respirable MP10, material particulado respirable fino MP2,5, dióxido de nitrógeno NO2, dióxido de azufre SO2 y
monóxido de carbono CO del proyecto para el escenario de construcción y operación del proyecto.

Para la modelación de la dispersión, la meteorología fue realizada con el software WRF-ARW para el año 2022,
peor año de concentraciones definido a través de la línea de base de la Estación Mirasol. La dispersión de los
contaminantes se ejecutó con el modelo CALPUFF, ambos modelos se realizaron bajo la metodología de la “Guía
para el Uso de Modelos de Calidad del Aire en el SEIA” del año 2023.

**2. OBJETIVOS**

**2.1. Objetivo General**

Modelar la dispersión de contaminantes del Proyecto

**2.2. Objetivos Específicos**

 - Obtener la línea de base del proyecto

 - Realizar el análisis meteorológico de la zona de estudio del proyecto

 - Obtener resultados de la modelación de la dispersión del proyecto

 - Análisis del cumplimiento normativo

**3. ÁREA DE ESTUDIO**

El área de estudio comprende un dominio de modelación que corresponde a una grilla de 20 x 16 km con una
resolución de 1 km. La Figura 1 muestra la ubicación del proyecto y la Figura 2 muestra el dominio de modelación.

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente_
_5_
_Bosquemar”_

Figura 1 Ubicación del Proyecto

Fuente: Elaboración propia, 2025

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente_
_6_
_Bosquemar”_

Figura 2 Dominio de Modelación

Fuente: Elaboración propia, 2025

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente_
_7_
_Bosquemar”_

**3. METODOLOGÍA**

La metodología utilizada en el presente informe corresponde a la ejecución del modelo meteorológico WRF y la
ejecución del modelo de dispersión CALPUFF siguiendo las directrices de la “Guía para el Uso de Modelos de
Calidad del Aire en el SEIA”, a continuación, se describen los modelos utilizados.

**3.1. WRF**

El Modelo de Investigación y Pronóstico del Tiempo (WRF) es un sistema numérico de predicción del tiempo de
mesoescala de última generación diseñado para aplicaciones de investigación atmosférica y pronóstico operativo.
Cuenta con dos núcleos dinámicos, un sistema de asimilación de datos y una arquitectura de software que admite
computación paralela y extensibilidad del sistema. El modelo sirve para una amplia gama de aplicaciones
meteorológicas en escalas que van desde decenas de metros hasta miles de kilómetros.

**3.2. CALPUFF**

CALPUFF es un sistema avanzado de modelado meteorológico y de la calidad del aire en estado no estacionario.
El sistema de modelado consta de tres componentes principales y un conjunto de programas de
preprocesamiento y posprocesamiento. Los componentes principales del sistema de modelado son CALMET (un
modelo meteorológico tridimensional de diagnóstico), CALPUFF (un modelo de dispersión de la calidad del aire)
y CALPOST (un paquete de procesamiento posterior). Además de estos componentes, hay muchos otros
procesadores que se pueden usar para preparar datos geofísicos (uso de la tierra y terreno) en muchos formatos
estándar; datos meteorológicos (superficie, aire superior, precipitación y datos de boyas); e interfaces a otros
modelos como el Penn State/NCAR Mesoscale Model (MM5), los modelos Eta/NAM y RUC de los Centros
Nacionales de Predicción Ambiental (NCEP), el modelo Weather Research and Forecasting (WRF) y el modelo

RAMS.

**4. NORMATIVA**

**4.1. Marco Legal**

El marco legal está dado por la normativa ambiental aplicable, la cual establece los valores límites para cada
contaminante normado, con el fin de evitar poner en riesgo la salud de la población por temas de calidad de aire.

Tabla 1 Normativa Ambiental Vigente

|Norma|Contaminante|Estadístico|Límite Noma|Referencia|
|---|---|---|---|---|
|Primaria|MP10|Media Anual|50 μg/m3N|D.S. 12/21 MMA|
|Primaria|MP10|Percentil 98 Diario|130 μg/m3N|D.S. 12/21 MMA|
|Primaria|MP2,5|Media Anual|20 μg/m3|D.S. 12/11 MMA|
|Primaria|MP2,5|Percentil 98 Diario|50 μg/m3|D.S. 12/11 MMA|
|Primaria|SO2|Media Anual|60 μg/m3N|D.S. 104/19 MMA|
|Primaria|SO2|Percentil 99 Diario|150 μg/m3N|D.S. 104/19 MMA|
|Primaria|SO2|Percentil 99 Horario|350 μg/m3N|D.S. 104/19 MMA|
|Primaria|NO2|Media Anual|60 μg/m3N|D.S. 40/23 MMA|
|Primaria|NO2|Percentil 99 Diario|150 μg/m3N|D.S. 40/23 MMA|
|Primaria|NO2|Percentil 99 Horario|350 μg/m3N|D.S. 40/23 MMA|
|Primaria|CO|Percentil 8 Horas|10.000 μg/m3N|D.S. 115/02 MINSEGPRES|
|Primaria|CO|Percentil 99 Horario|30.000 μg/m3N|D.S. 115/02 MINSEGPRES|

Fuente: Biblioteca del Congreso Nacional de Chile

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente_
_8_
_Bosquemar”_

**4.2. Línea de Base**

A continuación, en la Tabla 2 se muestra la estación considerada para la línea de base y en la Tabla 3 se muestran
los estadísticos obtenidos de la estación comparados con la norma.

Tabla 2 Estación de Monitoreo

|Estación|Coordenadas UTMa|Col3|Contaminante|Fecha de Monitoreo|
|---|---|---|---|---|
|Estación|Este (m)|Norte (m)|Norte (m)|Norte (m)|
|Mirasol|669.585|5.406.017|MP2,5|Enero 2021 a diciembre<br>2023|

Fuente: SINCA, 2025

Tabla 3 Línea de Base Estación Mirasol

|Contaminante|Estadístico|Año|ug/m3|Norma|% Norma|
|---|---|---|---|---|---|
|MP2,5 ug/m3|Media Anual|2021|24|20|120|
|MP2,5 ug/m3|Percentil 98 24 horas|Percentil 98 24 horas|112|50|224|
|MP2,5 ug/m3|Media Anual|2022|29|20|144|
|MP2,5 ug/m3|Percentil 98 24 horas|Percentil 98 24 horas|141|50|282|
|MP2,5 ug/m3|Media Anual|2023|20|20|101|
|MP2,5 ug/m3|Percentil 98 24 horas|Percentil 98 24 horas|110|50|220|
|MP2,5 ug/m3|Media Anual|2024|20|20|100|
|MP2,5 ug/m3|Percentil 98 24 horas|Percentil 98 24 horas|88|50|177|

Fuente: SINCA, 2025

Como se observa en la Tabla 3 el año de mayores concentraciones para los estadísticos normados de la línea de
base de la estación Mirasol, corresponde al 2022. En base a esta información es que se procede a generar la
información meteorológica con el modelo WRF para el año 2022.

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente_
_9_
_Bosquemar”_

**5. ANÁLISIS METEOROLÓGICO**

Dado que la meteorología es la que media entre las emisiones y su impacto en los puntos de interés, es

importante realizar una evaluación cualitativa y cuantitativa de la temperatura, velocidad y dirección del viento

modelado, con el fin de conocer y corregir esta diferencia en los resultados obtenidos para la dispersión de

contaminantes.

Esta meteorología se realiza mediante el modelo WRF el cual corresponde a un modelo de predicción numérica

del tiempo diseñado para la investigación y para aplicaciones operativas. Diversas instituciones han contribuido

y siguen contribuyendo a su desarrollo, con el firme objetivo de construir el modelo de pronóstico numérico de

mesoescala de la siguiente generación, para lograr un avance en el entendimiento de los procesos atmosféricos

y en la predicción de tiempo. Los principales componentes de este modelo son las fuentes externas de datos,

como son los datos de entrada y la información geográfica, el sistema de pre-procesamiento, el modelo WRF
ARW y los sistemas de post-procesamiento.

Este modelo se encuentra recomendado por la “Guía para el uso de modelos de calidad del aire en el SEIA”, para

la generación de datos meteorológicos, ya que, según indica, es uno de los modelos meteorológicos de pronóstico

más avanzados y completos, siendo empleado en la mayoría de los proyectos relacionados con modelación

atmosférica encargados por organismos estatales como el Ministerio del Medio Ambiente (MMA) y la ex Comisión

Nacional de Energía (CNE) (ahora Ministerio de Energía).

Para generar la modelación meteorológica, se utilizan tres dominios anidados, donde cada celda es de 9, 3 y 1

kilómetros respectivamente para un año calendario.

Es importante mencionar que la modelación meteorológica se realiza bajo las directrices establecidas en la “Guía

para el Uso de Modelos de Calidad del Aire en el SEIA, segunda edición 2023” del Servicio de Evaluación

Ambiental, que indica que se debe analizar al menos los tres años anteriores de datos observados en el dominio

de modelación, escogiendo el período en el cual se registren las mayores concentraciones del contaminante en

la zona de modelación, ya que, este parámetro tiene relación directa con el comportamiento de la atmósfera.

Dado lo anterior, se analizan los valores correspondientes a la calidad del aire de MP2,5 medidos por la estación

Mirasol, ubicada en el área de interés, presentando sus concentraciones anuales para el año 2021, 2022, 2023 y

2024, determinando cómo peor escenario para la dispersión de contaminantes al año 2022, ya que presenta el

mayor valor para la concentración de material particulado MP2,5, tanto para su norma anual como diaria (Ver

4.2. Línea de Base)

**5.1. Recopilación de la Información**

La metodología utilizada para el desarrollo del capítulo de meteorología y validación del modelo WRF consiste,

por una parte, en el análisis cualitativo de la temperatura, velocidad y dirección del viento entre los datos

observados por una estación de monitoreo cercana al Proyecto y los datos modelados en dicho punto. Estos

registros corresponden a valores con resolución temporal horaria, para el período correspondiente entre enero

a diciembre de 2022, en la estación de monitoreo Alerce, proporcionada por el sistema de Información Nacional

de Calidad del Aire (SINCA).

Por otro lado, se realiza un análisis cuantitativo con el fin de obtener un valor representativo del error del modelo

e incluir este en los resultados obtenidos del modelo de dispersión con el fin de obtener un ajuste más

representativo de la realidad.

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente_
_10_
_Bosquemar”_

A continuación, se presentan las coordenadas y variables analizadas.

Tabla 4 Ubicación Estación y Variables Meteorológica Analizada

|Estación|Coordenadas UTM - WGS 84|Col3|Variables|Periodo|
|---|---|---|---|---|
|Estación|Este (m)|Norte (m)|Norte (m)|Norte (m)|
|Alerce|669.585|5.406.016|Velocidad del viento<br>Dirección del viento<br>Temperatura|01 de enero al 31 de<br>diciembre 2022|

Fuente: Elaboración propia, 2025

Tanto la velocidad como la temperatura como la velocidad y dirección del viento son variables meteorológicas

relevantes para el análisis de los datos de entrada del modelo de dispersión al objeto de observar la dirección de

las masas de aire. Debido a lo anterior, a continuación, se presenta un resumen de la información registrada para

ambas variables, con sus respectivas series de tiempo y ciclos diarios.

**5.2. Series de Tiempo de la velocidad del viento**

Para un análisis adecuado de las variables meteorológicas, de acuerdo con lo señalado en la “guía para el uso de
modelos de calidad del aire en el SEIA”, la serie de datos debe contener al menos un 75% de datos válidos, para
garantizar la calidad de un análisis de datos meteorológicos, lo que en este caso de estudio se cumple para el
periodo de estudio, ya que el registro con el que se cuenta en la estación Alerce es de 99% de datos válidos.

A modo de verificación, se presenta en las siguientes figuras las series de tiempo para las variables de velocidad

y dirección de viento observadas y modeladas.

Tabla 5 Estadísticas de Datos Meteorológicos Analizados

|Estación|Datos Totales|Porcentaje de Datos Válidos|Porcentaje De Calma (%)|Col5|
|---|---|---|---|---|
|Estación|Datos Totales|Porcentaje de Datos Válidos|Periodo Diurno|Periodo Nocturno|
|Alerce|8.698|99%|5,84%|25,41%|

Fuente: Elaboración propia, 2025

La serie temporal de la velocidad del viento observada no muestra una variación en el ciclo anual, ya que las
velocidades se comportan de manera constante a lo largo del año, con velocidades que varían entre 6 y 8 m/s,
observando algunos eventos extremos entre abril y agosto, registrando las máximas magnitudes. principalmente

en los eventos extremos.

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente_
_11_
_Bosquemar”_

Figura 3 Serie observada y modelada de la velocidad del viento - Estación Alerce Periodo 01 enero 2022 - 31

|Col1|diciembre 2022|
|---|---|
|Observado||
|Modelado|<br> <br>|

Fuente: Elaboración propia, 2025

Con respecto a la dirección del viento se observan dos patrones dominantes, tanto en los datos observados como
modelados. El primero de ellos corresponde a vientos desde el Norte (N), correspondiendo a la línea centrada en
0° y 360°. Por otro lado, se observa un segundo patrón dominante con vientos preferentemente desde el Sur (S)
a lo largo de todo el año.

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente_
_12_
_Bosquemar”_

Figura 4 Serie observada y modelada de la dirección del viento - Estación Alerce Periodo 01 enero 2022 - 31

|Col1|diciembre 2022|
|---|---|
|Observado||
|Modelado||

Fuente: Elaboración propia, 2025

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente_
_13_
_Bosquemar”_

**5.3. Rosas de Viento de la Velocidad del Viento**

A continuación, se muestran las rosas de vientos tanto para el ciclo anual como para diferentes periodos del día,
con el fin de caracterizar la variabilidad temporal del viento modelado durante el periodo enero a diciembre de

2022 en la estación Alerce.

Observando el comportamiento desde las 00:00 a 23:00 horas, los registros muestran que la dirección de máxima

frecuencia en los datos observados corresponde a vientos procedentes desde el Norte (N), Norte Noreste (NNE)

y Norte Noroeste (NNO), explicando en conjunto un 35% de la frecuencia total, con velocidades que se centran

principalmente entre un 0 y 6 m/s. En la misma medida, se observan componente desde el Sur (S) y Sur Sureste

(SSE). Respecto a los datos modelados, se reproduce de manera correcta el patrón de vientos desde el Norte (N)

y Sur (S).

Figura 5 Rosa de Viento Ciclo Completo - Estación Alerce Periodo 01 enero 2022 - 31 diciembre 2022

Fuente: Elaboración propia, 2022

|Observado|Modelado|
|---|---|
|||

Fuente: Elaboración propia, 2025

Al observar el comportamiento espacial de los vientos en los diferentes periodos del día, en la Figura 6 se puede

apreciar en términos generales existe un patrón común tanto en los datos observados como modelados. Entre

las 00:00 y 11:00 horas los vientos dominan preferentemente desde el Norte (N) y Norte Noreste (NNE), mientras

que en horas de la tarde el patrón cambia levemente a vientos desde el Sur (S) y Sur Sureste (SSE).

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente_
_14_
_Bosquemar”_

Figura 6 Variabilidad temporal del viento - Estación Alerce

Fuente: Elaboración propia, 2022

|Col1|00:00 - 05:00 horas|06:00 - 11:00 horas|12:00 - 17:00 horas|18:00 - 23:00 horas|
|---|---|---|---|---|
|Observado|||||
|Modelado|||||

Fuente: Elaboración propia, 2025

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente Bosquemar”_ _15_

**5.4. Ciclo Estacional de la Velocidad del Viento**

En la Figura 7, se presenta el ciclo estacional de vientos observados en estación Alerce, presentando en el

eje “x” las horas del día y en el eje “y” los meses del año. Se puede apreciar para los datos observados un

leve ciclo estacional y un marcado ciclo diario a lo largo del año, con velocidad mínimas en las noches con
valores que varían entre 1 y 3 m/s, en cambio con velocidades máximas de 6 m/s en las horas diurnas.

Respecto a los datos modelados, se observa el mismo patrón.

En cuanto a la dirección del viento predominante, para el periodo de máxima velocidad, es decir entre las
09:00 y 19:00 horas se observa una componente desde el Sur (S) en los datos observados y modelados,
cambiando este patrón a vientos desde el Norte en horas de la mañana.

Figura 7 Ciclo estacional del viento - Estación Alerce Periodo 01 enero 2022 - 31 diciembre 2022

|Observado|Modelado|
|---|---|
|||

Fuente: Elaboración propia, 2025

**5.5. Ciclo Diario Velocidad del Viento**

En la siguiente figura se presentan los ciclos diarios promedio de la velocidad y dirección del viento, tanto

para los datos observados como modelados en la estación Alerce, donde se puede observar que en ambos

casos los valores mínimos se presentan en el periodo nocturno con valores que se mantienen

relativamente constantes hasta las 06:00 horas donde la velocidad comienza a aumentar levemente hasta

alcanzar el máximo diario a las 14:00 horas con una magnitud promedio de 4 m/s, respectivamente.

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente_
_16_
_Bosquemar”_

Figura 8 Ciclo diario de la velocidad del viento observada y modelada- Estación Alerce Periodo 01 enero

|Col1|2022 - 31 diciembre 2022|
|---|---|
|Observado||
|Modelado||

Fuente: Elaboración propia, 2025

Respecto al ciclo diario de dirección del viento se puede observar en los datos observados y modelados

que, a lo largo del día existe predominancia de vientos desde el Norte (N), Norte Noreste (NNE) y Norte

Noroeste (NNO) y vientos desde el Sur (S) y Sur Sureste (SSE), con mayor frecuencia de vientos entre las

11:00 y 20:00 horas, con vientos desde el Sur (S).

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente_
_17_
_Bosquemar”_

Figura 9 Ciclo diario de la dirección del viento observada y modelada- Estación Alerce Periodo 01 enero

|Col1|2022 - 31 diciembre 2022|
|---|---|
|Observado||
|Modelado||

Fuente: Elaboración propia, 2025

**5.5. Serie de tiempo de la temperatura**

La **¡Error! No se encuentra el origen de la referencia.** muestra los porcentajes de datos disponibles para l
a variable temperatura en la Estación Sierra Gorda, donde se puede observar que cuenta con un 99,97%
de datos válidos para el análisis.

Tabla 6 Estadísticas de Datos Meteorológicos Analizados de Temperatura

|Estación|Datos Totales|Porcentaje de Datos Válidos|
|---|---|---|
|Alerce|8.709|99,42%|

Fuente: Elaboración propia, 2025

La Figura 10 de la serie temporal para la temperatura registrada por la Estación Alerce muestra un

marcado ciclo anual durante el periodo analizado, con valores que en promedio varían entre 10 y 20°C,

tanto en los datos observados como modelados.

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente_
_18_
_Bosquemar”_

Figura 10 Serie de tiempo de la temperatura observada y modelada- Estación Alerce Periodo 01 enero

|Col1|2022 - 31 diciembre 2022|
|---|---|
|Observado||
|Modelado||

Fuente: Elaboración propia, 2025

**5.7. Ciclo estacional de la temperatura**
La Figura 11 presenta el ciclo estacional de la temperatura en Estación Alerce, presentando en el eje “x”
las horas del día y en el eje “y” los meses del año. Es posible observar un marcado ciclo estacional y un
marcado ciclo diario, con los máximos valores registrados entre enero y febrero y entre noviembre y
diciembre, entre las 10:00 y 19:00 horas, tanto en los datos observados como modelados.

Figura 11 Ciclo estacional de la temperatura - Estación Alerce Periodo

01 enero 2022 - 31 diciembre 2022

|Observado|Modelado|
|---|---|
|||

Fuente: Elaboración propia, 2025

**5.5. Ciclo diario de la temperatura**

En la siguiente figura se presenta el ciclo diario de la temperatura observada por la Estación Alerce junto
con su variabilidad en términos de los percentiles 5 y 95%. Al apreciar la curva promedio de temperatura
se puede observar un marcado ciclo diario con una leve amplitud entre la mínima y máxima de 6°C
aproximadamente, tanto en los datos observados como modelados. Los mínimos valores se presentan en
el periodo nocturno con temperaturas que se mantienen relativamente constantes hasta las 07:00 horas
donde progresivamente comienza a aumentar hasta alcanzar el máximo diario alrededor de las 14: horas
con una magnitud promedio de 14oC para los datos observados y 13°C para los datos modelados.

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente_
_19_
_Bosquemar”_

Figura 12 Serie de tiempo de la temperatura observada y modelada- Estación Alerce Periodo 01 enero

|Col1|2022 - 31 diciembre 2022|
|---|---|
|Observado||
|Modelado||

Fuente: Elaboración propia, 2025

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente_
_20_
_Bosquemar”_

**6. ANÁLISIS DE LA INCERTIDUMBRE**

El sistema de modelación WRF-CALPUFF, opera con una incertidumbre propia del modelo, la cual se

traduce en sobrestimación o subestimación de los aportes obtenidos en los puntos de interés ingresados

al modelo. Por dicha razón, para efectos de cuantificación y análisis se utilizó como variable incidente la

velocidad del viento, debido a que es la que mayor preponderancia tiene en la dispersión de

contaminantes atmosféricos.

En relación con lo indicado anteriormente, cabe señalar que, para cuantificar la incertidumbre del modelo,

se contrastó las velocidades del viento monitoreadas por la Estación Meteorológica Alerce durante el año

2022, disponibles en el sitio web del Sistema de Información Nacional de Calidad del Aire (SINCA), con los

datos obtenidos del modelo meteorológico en la misma localización.

A continuación, se realiza el análisis estadístico, agregando los estadígrafos base que solicita la “Guía para

el uso de modelos de Calidad del Aire en el SEIA” (2023), correspondientes al Sesgo, Error Medio

Cuadrático y el Coeficiente de Correlación.

**6.1. Raíz del Error Cuadrático Medio**

Corresponde al cálculo de la raíz cuadrada del promedio de las diferencias cuadradas de cada uno de los
valores del pronóstico y la observación. Este cálculo permite ponderar los errores positivos y negativos,
por lo cual en él están incluidos los errores sistemáticos y aleatorios de los modelos.

Dónde:

X1i : es el valor de la serie No 1

x2i : es el valor de la serie No2

N: es el número de valores analizado

**6.2. Sesgo**

Proporciona información sobre la tendencia del modelo a sobreestimar o subestimar una variable,

cuantificando el error sistemático del modelo.

**6.3. Coeficiente de Correlación**

Nos permite establecer la relación lineal entre los modelos utilizados y la observación y está acotada entre

-1 y 1.

_N_

##  ( x 1 i − x 1 () x 2 i −

_i_ = 1
##### =

##### ( x 1 − x 1 () x 2 − x 2 )

##### x − x x − x

1 _i_ 1 2 _i_

_i_ = 1
##### Corr =

1 _i_ 1

_i_

_i_

_i_

1 _i_ 1 2 _i_ 2

1

=

##### − ( N )1

1 2

##### − N )1 S S

##### −

Si Corr < 0 significa que las dos variables se correlacionan en sentido inverso. A valores altos de una de
ellas le suelen corresponder valores bajos de la otra y viceversa. Si Corr > 0 las dos variables se
correlacionan en sentido directo. A valores altos de una le corresponden valores altos de la otra. Si corr =
0 se dice que las variables están incorrelacionadas por lo tanto no puede establecerse ningún sentido de

covariación.

A continuación, se presentan los resultados obtenidos de los estadígrafos mencionados anteriormente
respecto a los datos monitoreados por la estación Viña del Mar.

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente_
_21_
_Bosquemar”_

Tabla 7 Estadígrafos de evaluación de desempeño del modelo para la velocidad del viento

|Serie de datos|Velocidad del viento|Col3|Temperatura|Col5|
|---|---|---|---|---|
|Serie de datos|Valor recomendado|Estación Alerce|Valor recomendado|Estación Alerce|
|SESGO|[-2,5;2,5] (m/s)|0,04|[-4;4] (°C)|-1,29|
|MAE|≤3 (m/s)|0,94|≤4 (°C)|1,69|
|RMSE|≤3,5 (m/s)|1,22|≤4,5 (°C)|2,15|
|CORR|>0,6|0,85|>0,8|0,94|

Fuente: Elaboración propia, 2025

En base a lo anteriormente expuesto respecto de la meteorología, es posible concluir que el modelo
representa de manera satisfactoria la dinámica del viento y temperatura observada ya que este reproduce
tanto los ciclos diarios como estacionales, sin embargo, este subestima los valores de temperatura y
sobrestima los de velocidad del viento en la Estación Alerce. En relación con los estadísticos evaluados, se
obtiene valores dentro de los parámetros recomendados.

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente_
_22_
_Bosquemar”_

**7. DATOS DE ENTRADA AL MODELO**

**7.1. Emisiones**

En el presente capitulo se muestran las emisiones asociadas a las fuentes del proyecto para el escenario
de construcción y operación. La Tabla 8 contiene las emisiones para la fase de construcción operación del

proyecto.

Tabla 8 Emisiones Atmosféricas Fase de Construcción más Operación

|Año|Fase|CO<br>(ton/año<br>)|COV<br>(ton/año<br>)|SOX<br>(ton/año<br>)|NOX<br>(ton/año<br>)|NH3<br>(ton/año<br>)|MP2,5<br>Total<br>(ton/año<br>)|MP10<br>Total<br>(ton/año<br>)|
|---|---|---|---|---|---|---|---|---|
|1|Construcción|0,3314|0,0674|0,0013|0,6999|0,0001|0,0876|0,3170|
|1|Operación Etapa A-B|0,0290|0,0072|0,0013|0,1231|0,0014|0,7434|1,4564|
|1|Total|0,3604|0,0746|0,0026|0,8231|0,0015|0,8309|1,7734|
|2|Construcción|0,2558|0,0450|0,0017|0,5222|0,0004|0,0955|0,4166|
|2|Operación Etapa A-B-C|0,0414|0,0104|0,0019|0,1761|0,0020|0,8417|1,8614|
|2|Total|0,2972|0,0553|0,0036|0,6983|0,0023|0,9372|2,2780|
|3|Construcción|0,2348|0,0536|0,0015|0,4734|0,0002|0,0592|0,2144|
|3|Operación Etapa A-B-C|0,0479|0,0120|0,0022|0,2036|0,0023|0,8929|2,0723|
|3|Total|0,2827|0,0656|0,0036|0,6770|0,0025|0,9521|2,2867|
|4|Construcción|0,2656|0,0491|0,0018|0,4996|0,0004|0,1214|0,6332|
|4|Operación Etapa A-B-C-D|0,0685|0,0162|0,0040|0,2923|0,0031|1,0282|2,6258|
|4|Total|0,3340|0,0653|0,0058|0,7919|0,0035|1,1496|3,2590|
|5|Construcción|0,1188|0,0297|0,0011|0,3290|0,0003|0,0764|0,3667|
|5|Operación Etapa A-B-C-D-E|0,0769|0,0180|0,0048|0,3287|0,0034|1,0834|2,8517|
|5|Total|0,1957|0,0476|0,0059|0,6576|0,0037|1,1598|3,2183|
|6|Construcción|0,2584|0,0488|0,0017|0,4512|0,0003|0,0881|0,4650|
|6|Operación Etapa A-B-C-D-E|0,0889|0,0204|0,0058|0,3805|0,0039|1,1625|3,1754|
|6|Total|0,3473|0,0693|0,0076|0,8317|0,0042|1,2506|3,6404|
|7|Construcción|0,2115|0,0325|0,0017|0,3738|0,0004|0,1082|0,6100|
|7|Operación Etapa A-B-C-D-E-F|0,1058|0,0239|0,0074|0,4536|0,0045|1,2737|3,6303|
|7|Total|0,3173|0,0564|0,0090|0,8274|0,0050|1,3819|4,2403|
|8|Construcción|0,1069|0,0330|0,0010|0,2711|0,0002|0,0459|0,2002|
|8|Operación Etapa A-B-C-D-E-F-<br>G|0,1145|0,0257|0,0082|0,4910|0,0049|1,3309|3,8644|
|8|Total|0,2213|0,0587|0,0091|0,7621|0,0051|1,3767|4,0645|
|9 y en<br>adelante|Operación Etapa A-B-C-D-E-F-<br>G|0,1298|0,0289|0,0095|0,5574|0,0055|1,4321|4,2784|

Fuente: Elaboración propia, 2025

Debido a que la zona es saturada por MP2,5, se utilizará este contaminante como criterio para seleccionar
los años a modelar. Como se ve en la tabla para construcción y operación el año a modelar es el número
7 y para operación corresponde al año 9.

La siguiente tabla muestra los parámetros ingresados a cada fuente de emisión del proyecto

Tabla 9 Parámetros Ingresados a Cada Fuente

|Tipo de Fuente|Parámetros|Valores|
|---|---|---|
|Fuentes Tipo Ruta para todas las fases|Inicial Sigma Y m|3,5|
|Fuentes Tipo Ruta para todas las fases|Inicial Sigma Z m|0|
|Fuentes Tipo Ruta para todas las fases|Altura Efectiva m|0|
|Fuentes Tipo Área-Polígono|Inicial Sigma Z m|0|
|Fuentes Tipo Área-Polígono|Altura Efectiva m|0|
|Fuentes Tipo Puntual Generadores|Altura del Escape m|1,47|
|Fuentes Tipo Puntual Generadores|Temperatura de Salida K|783,15|
|Fuentes Tipo Puntual Generadores|Diámetro Interno m|0,076|
|Fuentes Tipo Puntual Generadores|Velocidad de Salida m/s|59,78|

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente_
_23_
_Bosquemar”_

|Tipo de Fuente|Parámetros|Valores|
|---|---|---|
|Fuentes Tipo Puntual Calefactores Pellets|Altura del Escape m|5|
|Fuentes Tipo Puntual Calefactores Pellets|Temperatura de Salida K|409,15|
|Fuentes Tipo Puntual Calefactores Pellets|Diámetro Interno m|0,076|
|Fuentes Tipo Puntual Calefactores Pellets|Velocidad de Salida m/s|29,14|

Fuente: Elaboración propia, 2025

Los parámetros fueron estimados a través el promedio del ancho de las rutas, los generadores desde
fichas técnicas, los calefactores a través de fichas técnicas de calefactores. No se ingresan valores
superiores a 0 de sigma z y altura efectiva debido a que estos datos no se encuentran en bibliografía.

Las emisiones ingresadas al modelo se presentan en las siguientes tablas.

Tabla 10 Emisiones Ingresadas al Modelo Construcción y Operación Año 7

|Tipo de<br>Fuente|ID|Descripci<br>ón|SO2|SO4|NO|NO2|HNO3|NO3|CO|PM10|PM2.5|Unidad|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|ROAD|C7_1|Ruta<br>Hormigó<br>n|4,50E-09|2,37E-10|5,45E-07|6,20E-08|6,20E-09|6,20E-09|2,82E-08|2,61E-07|6,47E-08|g/s*m|
|ROAD|C7_2|Ruta<br>Botader<br>o 1|4,50E-09|2,37E-10|5,45E-07|6,20E-08|6,20E-09|6,20E-09|2,82E-08|2,14E-07|5,63E-08|g/s*m|
|ROAD|C7_3|Ruta<br>Botader<br>o 2|4,50E-09|2,37E-10|5,45E-07|6,20E-08|6,20E-09|6,20E-09|2,82E-08|2,14E-07|5,63E-08|g/s*m|
|ROAD|C7_4|RESPEL|4,50E-09|2,37E-10|5,45E-07|6,20E-08|6,20E-09|6,20E-09|2,82E-08|6,46E-09|6,12E-09|g/s*m|
|ROAD|C7_5|Ruta No<br>Pav<br>Interna|5,65E-09|2,97E-10|7,01E-07|7,96E-08|7,96E-09|7,96E-09|3,75E-08|9,21E-05|9,22E-06|g/s*m|
|ROAD|C7_6|Ruta Pav<br>Interna|4,50E-09|2,37E-10|5,45E-07|6,20E-08|6,20E-09|6,20E-09|2,82E-08|2,33E-06|5,67E-07|g/s*m|
|ROAD|C7_7|Ruta No<br>Pav Ext|4,50E-09|2,37E-10|5,45E-07|6,20E-08|6,20E-09|6,20E-09|2,82E-08|4,09E-05|4,09E-06|g/s*m|
|AREA_P<br>OLY|C7_8|Etapa G|1,36E-08|7,14E-10|3,98E-06|4,53E-07|4,53E-08|4,53E-08|3,48E-06|1,47E-06|7,51E-07|g/s*m2|
|AREA_P<br>OLY|C7_9|Erosión|0,00E+0<br>0|0,00E+0<br>0|0,00E+0<br>0|0,00E+0<br>0|0,00E+0<br>0|0,00E+0<br>0|0,00E+0<br>0|7,38E-08|1,13E-08|g/s*m2|
|ROAD|C7_11|Ruta<br>Calzada|4,50E-09|2,37E-10|5,45E-07|6,20E-08|6,20E-09|6,20E-09|2,82E-08|6,96E-09|6,24E-09|g/s*m|
|ROAD|C7_12|Ruta<br>Sodimac|4,50E-09|2,37E-10|5,45E-07|6,20E-08|6,20E-09|6,20E-09|2,82E-08|2,60E-08|1,08E-08|g/s*m|
|POINT|SRC_1 a<br>SCR_232|Pellets<br>Operació<br>n|0,00E+0<br>0|0,00E+0<br>0|0,00E+0<br>0|0,00E+0<br>0|0,00E+0<br>0|0,00E+0<br>0|0,00E+0<br>0|4,03E-04|4,03E-04|g/s|
|POINT|SRC_233<br>a 235|Generad<br>ores<br>Operació<br>n|2,39E-02|1,26E-03|3,36E-01|3,82E-02|3,82E-03|3,82E-03|8,22E-02|2,68E-02|2,68E-02|g/s|
|ROAD|SRC_237|Ruta 1<br>Operació<br>n|1,49E-07|7,83E-09|1,30E-05|1,48E-06|1,48E-07|1,48E-07|3,48E-06|1,13E-04|2,75E-05|g/s*m al<br>día|
|ROAD|SRC_238|Ruta 2<br>Operació<br>n|1,49E-07|7,83E-09|1,30E-05|1,48E-06|1,48E-07|1,48E-07|3,48E-06|1,13E-04|2,75E-05|g/s*m al<br>día|
|ROAD|SRC_239|Ruta 3<br>Operació<br>n|1,49E-07|7,83E-09|1,30E-05|1,48E-06|1,48E-07|1,48E-07|3,48E-06|1,13E-04|2,75E-05|g/s*m al<br>día|
|ROAD|SRC_240|Ruta 4<br>Operació<br>n|1,49E-07|7,83E-09|1,30E-05|1,48E-06|1,48E-07|1,48E-07|3,48E-06|1,13E-04|2,75E-05|g/s*m al<br>día|
|ROAD|SRC_241|Ruta 5<br>Operació<br>n|1,49E-07|7,83E-09|1,30E-05|1,48E-06|1,48E-07|1,48E-07|3,48E-06|1,13E-04|2,75E-05|g/s*m al<br>día|

Fuente: Elaboración propia, 2025

Tabla 11 Emisiones Ingresadas Operación Año 9

|Tipo de<br>Fuente|ID|Descripci<br>ón|SO2|SO4|NO|NO2|HNO3|NO3|CO|PM10|PM2.5|Unidad|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|POINT|SRC_1 a<br>SCR_232|Pellets<br>Operació<br>n|0,00E+0<br>0|0,00E+0<br>0|0,00E+0<br>0|0,00E+0<br>0|0,00E+0<br>0|0,00E+0<br>0|0,00E+0<br>0|4,03E-04|4,03E-04|g/s|
|POINT|SRC_233<br>a 236|Generad<br>ores<br>Operació<br>n|2,39E-02|1,26E-03|3,36E-01|3,82E-02|3,82E-03|3,82E-03|8,22E-02|2,68E-02|2,68E-02|g/s|
|ROAD|SRC_237|Ruta 1<br>Operació<br>n|1,80E-07|9,46E-09|1,57E-05|1,79E-06|1,79E-07|1,79E-07|4,20E-06|1,37E-04|3,32E-05|g/s*m al<br>día|
|ROAD|SRC_238|Ruta 2<br>Operació<br>n|1,80E-07|9,46E-09|1,57E-05|1,79E-06|1,79E-07|1,79E-07|4,20E-06|1,37E-04|3,32E-05|g/s*m al<br>día|

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente_
_24_
_Bosquemar”_

|Tipo de<br>Fuente|ID|Descripci<br>ón|SO2|SO4|NO|NO2|HNO3|NO3|CO|PM10|PM2.5|Unidad|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|ROAD|SRC_239|Ruta 3<br>Operació<br>n|1,80E-07|9,46E-09|1,57E-05|1,79E-06|1,79E-07|1,79E-07|4,20E-06|1,37E-04|3,32E-05|g/s*m al<br>día|
|ROAD|SRC_240|Ruta 4<br>Operació<br>n|1,80E-07|9,46E-09|1,57E-05|1,79E-06|1,79E-07|1,79E-07|4,20E-06|1,37E-04|3,32E-05|g/s*m al<br>día|
|ROAD|SRC_241|Ruta 5<br>Operació<br>n|1,80E-07|9,46E-09|1,57E-05|1,79E-06|1,79E-07|1,79E-07|4,20E-06|1,37E-04|3,32E-05|g/s*m al<br>día|

Fuente: Elaboración propia, 2025

Las fuentes de emisión consideras en el modelo se le agregaron “variable rates”, para la construcción se
le agrego un ciclo de funcionamiento de 8 a 18 horas durante los lunes a viernes. Para los generadores
debido a que su funcionamiento ocurre durante una emergencia y se estiman 10 horas se consideró su
modelación durante el día de menor temperatura, de menor capa de mezcla y de vientos más bajos
respecto a los datos modelados del punto donde emiten los generadores. El día considerado para la
modelación de los generadores corresponde al día 15 de julio del 2022. Para los calefactores de pellets se
utilizó el ciclo de operación de 9 a 20 horas.

Finalmente, para las rutas utilizadas por el proyecto para la operación, se buscaron distintas rutas
probables de utilización por donde se podrían desplazar los vehículos, el criterio de selección son rutas
principales de la ciudad. Además, para el uso de estas rutas se utilizó el “Estudio de Capacidad Vial”, del
plan regulador de Puerto Montt.

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente_
_25_
_Bosquemar”_

**7.2. Receptores**

Además de la meteorología y las emisiones, se deben considerar los receptores de las concentraciones
generadas por el proyecto, para esto la Tabla 12 muestra los puntos receptores considerados en el estudio
y en la Figura 13 se muestra la ubicación geográfica de los receptores.

Tabla 12 Receptores Considerados en el Proyecto

|Receptores|Tipo|Ubicación UTM-WGS-84-huso 19S|Col4|
|---|---|---|---|
|Receptores|Tipo|Este (m)|Norte (m)|
|Puerta Bosquemar|Primario|667.257|5.405.161|
|Colegio Bosquemar|Primario|666.926|5.405.339|
|Miradores Los Volcanes II|Primario|666.865|5.405.144|
|Bosquemar II|Primario|666.864|5.405.242|
|Loteo Bosquemar|Primario|667.026|5.405.642|
|Parque Costanera I|Primario|667.228|5.406.183|
|Parque Costanera III|Primario|667.532|5.405.945|
|Altos Tenglo III|Primario|668.048|5.405.765|
|Villa Juan XXIII|Primario|667.985|5.405.963|
|Brisamar|Primario|667.525|5.406.094|
|Los Albatros|Primario|667.708|5.406.391|
|Conjunto Los Lagos|Primario|667.976|5.406.521|
|Escuela Padre Alberto Hurtado|Primario|668.256|5.406.469|
|Población Juan Pablo II|Primario|668.205|5.406.699|
|Conjunto Habitacional Viento Sur|Primario|667.967|5.406.781|
|Población Vicuña Mackenna|Primario|668.408|5.406.951|
|Lomas de Cardonal|Primario|668.509|5.407.166|
|Alto Mackenna|Primario|668.698|5.407.252|
|Est Mirasol|Primario|669.587|5.406.020|
|Est Alerce|Primario|675.589|5.414.814|
|Est Puerto Varas|Primario|670.038|5.422.743|
|Villa Clotario Blest|Primario|668.517|5.406.009|
|Villa Los Poetas|Primario|668.957|5.406.520|
|Población Bernardo OHiggins|Primario|669.631|5.406.774|
|Terrazas de Angelmó|Primario|669.314|5.405.677|
|Villa San Antonio|Primario|669.679|5.405.282|
|Barrio Vicente Pérez Rosales|Primario|670.899|5.406.421|
|Villa Vicente Pérez Rosales|Primario|670.648|5.406.467|
|III-IV|Primario|666.694|5.404.758|
|Bosquemar IX|Primario|666.372|5.405.080|
|Llanos de Tenglo|Primario|665.502|5.404.343|
|Puerta Sur|Primario|667.502|5.407.981|

Fuente: Elaboración propia, 2025

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente_
_26_
_Bosquemar”_

Figura 13 Ubicación Geográfica de los Receptores

Fuente: Elaboración propia, 2025

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente_
_27_
_Bosquemar”_

**7.3. Topografía**

Otra variable importante dentro del estudio es la topografía, ya que esta puede indicarnos a través de sus
fallas geográficas como se van a dispersar los contaminantes, en la Figura 14 se muestran las curvas de
nivel asociadas a la topografía del área de estudio. Se destaca que el detalle topográfico se obtuvo del

modelo WRF.

Figura 14 Curvas de Nivel del Área de Estudio

Fuente: Elaboración propia, 2025

**7.4. Meteorología**

La meteorología ingresada al modelo CALPUFF proviene del modelo WRF y el año de modelación
meteorológica es el 2022. La modelación meteorológica fue analizada en el Capítulo 5 del presente

informe.

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente_
_28_
_Bosquemar”_

**8. RESULTADOS DE LA MODELACIÓN**

**8.1. Resultados**

En este capítulo se muestran los resultados de los contaminantes modelados con el sistema de modelación WRF-CALPUFF del proyecto para el escenario de construcción más operación del año 7. En la Tabla 13 y
Tabla 14 se encuentran las concentraciones en los receptores donde se evalúa las normas primarias de calidad del aire.

Tabla 13 Concentraciones obtenidas en los Receptores Norma Primaria Escenario Construcción más Operación Año 7

|Receptor|MP10 (ug/m3)|Col3|MP2,5 (ug/m3)|Col5|NO2 (ug/m3)|Col7|Col8|CO (ug/m3)|Col10|SO2 (ug/m3) Primario|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Receptor|Media Anual|P98 24 hrs|Media Anual|P98 24 hrs|Media Anual|P99 24 HR|P99 1 HR|P99 1 hrs|P99 8 hr|Media Anual|P99 24 hrs|P98,5 1 hr|
|Puerta Bosquemar|0,7514|3,0625|0,2583|1,2525|0,1232|1,2546|26,3160|20,6380|2,6008|0,0034|0,0064|0,0123|
|Colegio Bosquemar|0,9063|5,1116|0,2600|1,5540|0,0735|0,8606|15,4670|12,2940|1,9608|0,0013|0,0095|0,0260|
|Miradores Los Volcanes II|0,4045|3,2846|0,1402|1,4365|0,0761|1,2833|21,4820|18,1110|2,7104|0,0005|0,0055|0,0107|
|Bosquemar II|0,4532|4,1442|0,1583|1,6758|0,0711|1,2677|21,4000|16,6700|2,1649|0,0006|0,0070|0,0108|
|Loteo Bosquemar|0,7890|3,4827|0,2232|1,0218|0,0770|0,7780|12,0930|6,7945|1,1475|0,0014|0,0061|0,0172|
|Parque Costanera I|0,4609|1,7307|0,1271|0,5770|0,0613|0,4979|6,2317|3,0193|0,4556|0,0008|0,0036|0,0094|
|Parque Costanera III|0,6081|2,2391|0,1557|0,6012|0,0519|0,5226|6,0873|3,0749|0,4743|0,0010|0,0045|0,0142|
|Altos Tenglo III|0,4656|2,0591|0,1161|0,5119|0,0397|0,3387|4,3961|1,8630|0,4338|0,0010|0,0041|0,0086|
|Villa Juan XXIII|0,4977|2,2410|0,1248|0,5711|0,0400|0,3025|4,5122|1,5888|0,3296|0,0011|0,0050|0,0094|
|Brisamar|0,4908|2,0261|0,1261|0,5097|0,0481|0,3431|3,4368|1,5464|0,3400|0,0008|0,0040|0,0121|
|Los Albatros|0,3956|1,6178|0,0995|0,3997|0,0411|0,3197|4,6489|1,8187|0,2682|0,0008|0,0036|0,0086|
|Conjunto Los Lagos|0,3931|1,7203|0,0984|0,4228|0,0359|0,2079|4,3670|1,5650|0,2328|0,0010|0,0030|0,0084|
|Escuela Padre Alberto Hurtado|0,3533|1,5529|0,0878|0,4017|0,0280|0,1961|4,7179|0,8979|0,1875|0,0008|0,0034|0,0065|
|Población Juan Pablo II|0,3893|1,5819|0,0964|0,3970|0,0252|0,1768|1,9870|0,8310|0,1928|0,0008|0,0032|0,0083|
|Conjunto Habitacional Viento Sur|0,2488|1,1857|0,0626|0,3026|0,0288|0,1762|3,3242|0,9252|0,1745|0,0007|0,0022|0,0055|
|Población Vicuña Mackenna|0,2874|1,3673|0,0710|0,3410|0,0202|0,1333|2,8874|0,6812|0,1521|0,0006|0,0026|0,0062|
|Lomas de Cardonal|0,3048|1,4772|0,0751|0,3625|0,0182|0,1118|4,2146|0,7012|0,1361|0,0006|0,0025|0,0057|
|Alto Mackenna|0,2528|1,2713|0,0621|0,3104|0,0162|0,1039|3,3242|0,7069|0,1241|0,0005|0,0021|0,0046|

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente Bosquemar”_ _29_

|Receptor|MP10 (ug/m3)|Col3|MP2,5 (ug/m3)|Col5|NO2 (ug/m3)|Col7|Col8|CO (ug/m3)|Col10|SO2 (ug/m3) Primario|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Receptor|Media Anual|P98 24 hrs|Media Anual|P98 24 hrs|Media Anual|P99 24 HR|P99 1 HR|P99 1 hrs|P99 8 hr|Media Anual|P99 24 hrs|P98,5 1 hr|
|Est Mirasol|0,0728|0,3711|0,0183|0,0929|0,0101|0,0742|0,8286|0,2752|0,0567|0,0001|0,0009|0,0016|
|Est Alerce|0,0007|0,0047|0,0002|0,0023|0,0002|0,0020|0,0187|0,0034|0,0012|0,0000|0,0000|0,0000|
|Est Puerto Varas|0,0012|0,0071|0,0004|0,0028|0,0005|0,0032|0,0248|0,0095|0,0015|0,0000|0,0000|0,0000|
|Villa Clotario Blest|0,2281|1,0930|0,0571|0,2651|0,0276|0,2059|5,1329|1,0517|0,2110|0,0007|0,0024|0,0051|
|Villa Los Poetas|0,1831|1,0210|0,0452|0,2487|0,0177|0,1436|3,2848|0,9132|0,1399|0,0004|0,0022|0,0049|
|Población Bernardo OHiggins|0,1843|0,8960|0,0451|0,2173|0,0109|0,0942|1,5087|0,5021|0,1095|0,0003|0,0015|0,0033|
|Terrazas de Angelmó|0,0974|0,4852|0,0246|0,1194|0,0114|0,0820|0,8966|0,2872|0,0668|0,0002|0,0010|0,0020|
|Villa San Antonio|0,1734|0,8486|0,0433|0,2222|0,0101|0,0637|0,7173|0,4320|0,0785|0,0003|0,0012|0,0028|
|Barrio Vicente Pérez Rosales|0,0136|0,0879|0,0036|0,0253|0,0033|0,0256|0,2209|0,0461|0,0126|0,0000|0,0002|0,0004|
|Villa Vicente Pérez Rosales|0,0182|0,1115|0,0047|0,0318|0,0040|0,0324|0,2858|0,0700|0,0165|0,0000|0,0003|0,0005|
|III-IV|0,1951|2,4881|0,0586|0,5939|0,0693|1,3824|23,4730|22,1590|3,3862|0,0004|0,0055|0,0061|
|Bosquemar IX|0,1052|1,2183|0,0358|0,3834|0,0385|0,6510|10,5480|7,4060|1,1035|0,0002|0,0022|0,0030|
|Llanos de Tenglo|0,0205|0,2886|0,0071|0,1128|0,0086|0,1750|2,1658|1,0886|0,2372|0,0000|0,0006|0,0006|
|Puerta Sur|0,0375|0,2026|0,0110|0,0644|0,0081|0,0732|0,6651|0,2200|0,0397|0,0001|0,0004|0,0009|

Fuente: Elaboración propia, 2025

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente Bosquemar”_ _30_

Tabla 14 Concentraciones obtenidas en los Receptores Norma Primaria Escenario Operación año 9

|Receptor|MP10 (ug/m3)|Col3|MP2,5 (ug/m3)|Col5|NO2 (ug/m3)|Col7|Col8|CO (ug/m3)|Col10|SO2 (ug/m3) Primario|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Receptor|Media Anual|P98 24 hrs|Media Anual|P98 24 hrs|Media Anual|P99 24 HR|P99 1 HR|P99 1 hrs|P99 8 hr|Media Anual|P99 24 hrs|P99 1 hr|
|Puerta Bosquemar|0,7633|2,9913|0,2640|1,2050|0,0582|0,2178|7,1677|3,4032|0,2044|0,0034|0,0043|0,0108|
|Colegio Bosquemar|0,9542|5,6287|0,2781|1,6752|0,0242|0,2114|2,5780|2,4276|0,4777|0,0012|0,0079|0,0245|
|Miradores Los Volcanes II|0,3081|2,3834|0,1257|1,4192|0,0141|0,1671|1,8612|1,1623|0,2487|0,0003|0,0034|0,0084|
|Bosquemar II|0,4079|3,5630|0,1530|1,5521|0,0157|0,2041|2,3673|2,0515|0,3568|0,0004|0,0051|0,0100|
|Loteo Bosquemar|0,8530|3,6665|0,2438|1,1510|0,0384|0,1809|2,7356|1,8340|0,3752|0,0015|0,0058|0,0157|
|Parque Costanera I|0,5165|2,0442|0,1419|0,5836|0,0368|0,1765|2,9210|0,9407|0,1754|0,0008|0,0032|0,0085|
|Parque Costanera III|0,7095|2,5431|0,1812|0,6846|0,0431|0,1746|3,2808|1,1753|0,2343|0,0012|0,0037|0,0136|
|Altos Tenglo III|0,5507|2,3502|0,1374|0,5820|0,0389|0,1844|2,5467|1,5164|0,3028|0,0013|0,0049|0,0093|
|Villa Juan XXIII|0,5895|2,7032|0,1475|0,6748|0,0374|0,2533|3,7512|1,5493|0,2870|0,0012|0,0048|0,0100|
|Brisamar|0,5708|2,3129|0,1463|0,5989|0,0398|0,1923|2,3636|0,8799|0,2206|0,0009|0,0034|0,0119|
|Los Albatros|0,4638|1,8847|0,1166|0,4677|0,0379|0,1608|1,9178|1,2856|0,2063|0,0010|0,0031|0,0091|
|Conjunto Los Lagos|0,4653|2,0321|0,1162|0,5004|0,0341|0,1506|4,4750|0,9948|0,1810|0,0010|0,0028|0,0089|
|Escuela Padre Alberto Hurtado|0,4182|1,8524|0,1038|0,4499|0,0279|0,1317|2,7345|0,9888|0,1775|0,0009|0,0033|0,0068|
|Población Juan Pablo II|0,4625|1,9088|0,1144|0,4684|0,0258|0,1234|1,7600|0,8618|0,1703|0,0009|0,0027|0,0081|
|Conjunto Habitacional Viento Sur|0,2933|1,3841|0,0736|0,3521|0,0276|0,1229|3,2358|0,7594|0,1333|0,0008|0,0020|0,0060|
|Población Vicuña Mackenna|0,3415|1,5806|0,0843|0,3958|0,0207|0,0991|4,7807|0,7376|0,1458|0,0007|0,0025|0,0062|
|Lomas de Cardonal|0,3641|1,7654|0,0896|0,4289|0,0189|0,0960|6,0930|0,9289|0,1464|0,0007|0,0025|0,0058|
|Alto Mackenna|0,3021|1,5337|0,0742|0,3742|0,0162|0,0928|4,7306|0,7908|0,1347|0,0006|0,0024|0,0047|
|Est Mirasol|0,0865|0,4390|0,0216|0,1102|0,0096|0,0696|0,7384|0,2331|0,0510|0,0001|0,0008|0,0016|
|Est Alerce|0,0007|0,0052|0,0002|0,0022|0,0001|0,0007|0,0105|0,0017|0,0003|0,0000|0,0000|0,0000|
|Est Puerto Varas|0,0013|0,0073|0,0004|0,0031|0,0002|0,0012|0,0297|0,0046|0,0005|0,0000|0,0000|0,0000|
|Villa Clotario Blest|0,2705|1,2764|0,0675|0,3101|0,0263|0,1178|2,2523|0,8961|0,1346|0,0007|0,0022|0,0053|
|Villa Los Poetas|0,2182|1,2271|0,0538|0,2996|0,0165|0,1028|1,5863|0,7595|0,1099|0,0004|0,0020|0,0055|

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente Bosquemar”_ _31_

|Receptor|MP10 (ug/m3)|Col3|MP2,5 (ug/m3)|Col5|NO2 (ug/m3)|Col7|Col8|CO (ug/m3)|Col10|SO2 (ug/m3) Primario|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Receptor|Media Anual|P98 24 hrs|Media Anual|P98 24 hrs|Media Anual|P99 24 HR|P99 1 HR|P99 1 hrs|P99 8 hr|Media Anual|P99 24 hrs|P99 1 hr|
|Población Bernardo OHiggins|0,2208|1,0693|0,0540|0,2597|0,0098|0,0704|1,0263|0,5392|0,1008|0,0003|0,0017|0,0036|
|Terrazas de Angelmó|0,1157|0,5816|0,0291|0,1432|0,0110|0,0810|0,8941|0,3002|0,0672|0,0002|0,0011|0,0022|
|Villa San Antonio|0,2069|1,0179|0,0516|0,2655|0,0094|0,0589|0,6810|0,4794|0,0899|0,0003|0,0015|0,0033|
|Barrio Vicente Pérez Rosales|0,0158|0,0975|0,0041|0,0271|0,0026|0,0221|0,2273|0,0417|0,0103|0,0000|0,0002|0,0003|
|Villa Vicente Pérez Rosales|0,0213|0,1227|0,0055|0,0356|0,0033|0,0254|0,2842|0,0606|0,0147|0,0000|0,0003|0,0005|
|III-IV|0,0906|0,7701|0,0382|0,3498|0,0086|0,1081|1,2588|0,4477|0,0696|0,0001|0,0010|0,0022|
|Bosquemar IX|0,0753|0,7214|0,0303|0,3525|0,0076|0,1285|1,6422|0,3892|0,0698|0,0001|0,0011|0,0018|
|Llanos de Tenglo|0,0167|0,2011|0,0065|0,0977|0,0024|0,0367|0,5100|0,0830|0,0180|0,0000|0,0003|0,0004|
|Puerta Sur|0,0417|0,2368|0,0121|0,0695|0,0059|0,0492|0,5069|0,1152|0,0297|0,0001|0,0005|0,0008|

Fuente: Elaboración propia, 2025

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente Bosquemar”_ _32_

**8.2. Análisis Normativo**

En este capítulo se realizará la comparación de los aportes del proyecto respecto a los límites normativos.
Como se vio en el capítulo Línea de base la Estación de Monitoreo de Calidad del Aire Mirasol, el contaminante
MP2,5 se encuentra en saturación en sus estadísticos media anual y percentil 98 de 24 horas, debido a esto,
es que se compararán los aportes del proyecto con los límites de impacto significativo del criterio del SEA

A continuación, la Tabla 15, Tabla 16 contienen los valores porcentuales de la comparación de los aportes del
proyecto respecto a los límites de la norma, tanto para los escenarios de construcción más operación del año
7 y operación del proyecto del año 9.

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente_
_33_
_Bosquemar”_

Tabla 15 Concentraciones del Proyecto Comparados con la Normativa Primaria, Escenario Construcción más Operación Año 7

|Receptor|MP10 (ug/m3)|Col3|MP2,5 (ug/m3)|Col5|NO2 (ug/m3)|Col7|Col8|CO (ug/m3)|Col10|SO2 (ug/m3) Primario|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Receptor|Media Anual|P98 24 hrs|Media Anual|P98 24 hrs|Media Anual|P99 1 hr|P99 1 hr|P99 8 hrs|P99 1 hr|Media Anual|P99 24 hrs|P98,5 1 hr|
|Puerta Bosquemar|1,50%|2,36%|1,29%|2,51%|0,31%|1,25%|13,16%|0,07%|0,03%|0,01%|0,00%|0,00%|
|Colegio Bosquemar|1,81%|3,93%|1,30%|3,11%|0,18%|0,86%|7,73%|0,04%|0,02%|0,00%|0,01%|0,01%|
|Miradores Los Volcanes II|0,81%|2,53%|0,70%|2,87%|0,19%|1,28%|10,74%|0,06%|0,03%|0,00%|0,00%|0,00%|
|Bosquemar II|0,91%|3,19%|0,79%|3,35%|0,18%|1,27%|10,70%|0,06%|0,02%|0,00%|0,00%|0,00%|
|Loteo Bosquemar|1,58%|2,68%|1,12%|2,04%|0,19%|0,78%|6,05%|0,02%|0,01%|0,00%|0,00%|0,00%|
|Parque Costanera I|0,92%|1,33%|0,64%|1,15%|0,15%|0,50%|3,12%|0,01%|0,00%|0,00%|0,00%|0,00%|
|Parque Costanera III|1,22%|1,72%|0,78%|1,20%|0,13%|0,52%|3,04%|0,01%|0,00%|0,00%|0,00%|0,00%|
|Altos Tenglo III|0,93%|1,58%|0,58%|1,02%|0,10%|0,34%|2,20%|0,01%|0,00%|0,00%|0,00%|0,00%|
|Villa Juan XXIII|1,00%|1,72%|0,62%|1,14%|0,10%|0,30%|2,26%|0,01%|0,00%|0,00%|0,00%|0,00%|
|Brisamar|0,98%|1,56%|0,63%|1,02%|0,12%|0,34%|1,72%|0,01%|0,00%|0,00%|0,00%|0,00%|
|Los Albatros|0,79%|1,24%|0,50%|0,80%|0,10%|0,32%|2,32%|0,01%|0,00%|0,00%|0,00%|0,00%|
|Conjunto Los Lagos|0,79%|1,32%|0,49%|0,85%|0,09%|0,21%|2,18%|0,01%|0,00%|0,00%|0,00%|0,00%|
|Escuela Padre Alberto Hurtado|0,71%|1,19%|0,44%|0,80%|0,07%|0,20%|2,36%|0,00%|0,00%|0,00%|0,00%|0,00%|
|Población Juan Pablo II|0,78%|1,22%|0,48%|0,79%|0,06%|0,18%|0,99%|0,00%|0,00%|0,00%|0,00%|0,00%|
|Conjunto Habitacional Viento Sur|0,50%|0,91%|0,31%|0,61%|0,07%|0,18%|1,66%|0,00%|0,00%|0,00%|0,00%|0,00%|
|Población Vicuña Mackenna|0,57%|1,05%|0,36%|0,68%|0,05%|0,13%|1,44%|0,00%|0,00%|0,00%|0,00%|0,00%|
|Lomas de Cardonal|0,61%|1,14%|0,38%|0,72%|0,05%|0,11%|2,11%|0,00%|0,00%|0,00%|0,00%|0,00%|
|Alto Mackenna|0,51%|0,98%|0,31%|0,62%|0,04%|0,10%|1,66%|0,00%|0,00%|0,00%|0,00%|0,00%|
|Est Mirasol|0,15%|0,29%|0,09%|0,19%|0,03%|0,07%|0,41%|0,00%|0,00%|0,00%|0,00%|0,00%|
|Est Alerce|0,00%|0,00%|0,00%|0,00%|0,00%|0,00%|0,01%|0,00%|0,00%|0,00%|0,00%|0,00%|
|Est Puerto Varas|0,00%|0,01%|0,00%|0,01%|0,00%|0,00%|0,01%|0,00%|0,00%|0,00%|0,00%|0,00%|
|Villa Clotario Blest|0,46%|0,84%|0,29%|0,53%|0,07%|0,21%|2,57%|0,00%|0,00%|0,00%|0,00%|0,00%|
|Villa Los Poetas|0,37%|0,79%|0,23%|0,50%|0,04%|0,14%|1,64%|0,00%|0,00%|0,00%|0,00%|0,00%|

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente Bosquemar”_ _34_

|Receptor|MP10 (ug/m3)|Col3|MP2,5 (ug/m3)|Col5|NO2 (ug/m3)|Col7|Col8|CO (ug/m3)|Col10|SO2 (ug/m3) Primario|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Receptor|Media Anual|P98 24 hrs|Media Anual|P98 24 hrs|Media Anual|P99 1 hr|P99 1 hr|P99 8 hrs|P99 1 hr|Media Anual|P99 24 hrs|P98,5 1 hr|
|Población Bernardo OHiggins|0,37%|0,69%|0,23%|0,43%|0,03%|0,09%|0,75%|0,00%|0,00%|0,00%|0,00%|0,00%|
|Terrazas de Angelmó|0,19%|0,37%|0,12%|0,24%|0,03%|0,08%|0,45%|0,00%|0,00%|0,00%|0,00%|0,00%|
|Villa San Antonio|0,35%|0,65%|0,22%|0,44%|0,03%|0,06%|0,36%|0,00%|0,00%|0,00%|0,00%|0,00%|
|Barrio Vicente Pérez Rosales|0,03%|0,07%|0,02%|0,05%|0,01%|0,03%|0,11%|0,00%|0,00%|0,00%|0,00%|0,00%|
|Villa Vicente Pérez Rosales|0,04%|0,09%|0,02%|0,06%|0,01%|0,03%|0,14%|0,00%|0,00%|0,00%|0,00%|0,00%|
|III-IV|0,39%|1,91%|0,29%|1,19%|0,17%|1,38%|11,74%|0,07%|0,03%|0,00%|0,00%|0,00%|
|Bosquemar IX|0,21%|0,94%|0,18%|0,77%|0,10%|0,65%|5,27%|0,02%|0,01%|0,00%|0,00%|0,00%|
|Llanos de Tenglo|0,04%|0,22%|0,04%|0,23%|0,02%|0,17%|1,08%|0,00%|0,00%|0,00%|0,00%|0,00%|
|Puerta Sur|0,07%|0,16%|0,05%|0,13%|0,02%|0,07%|0,33%|0,00%|0,00%|0,00%|0,00%|0,00%|
|**Límite Normativo**|**50**|**130**|**20**|**50**|**40**|**100**|**200**|**30.000**|**10.000**|**60**|**150**|**350**|

Fuente: Elaboración propia, 2025

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente Bosquemar”_ _35_

Tabla 16 Concentraciones del Proyecto Comparados con la Normativa Primaria, Escenario Operación Año 9

|Receptor|MP10 (ug/m3)|Col3|MP2,5 (ug/m3)|Col5|NO2 (ug/m3)|Col7|Col8|CO (ug/m3)|Col10|SO2 (ug/m3) Primario|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Receptor|Media Anual|P98 24 hrs|Media Anual|P98 24 hrs|Media Anual|P99 1 hr|P99 1 hr|P99 8 hrs|P99 1 hr|Media Anual|P99 24 hrs|P98,5 1 hr|
|Puerta Bosquemar|1,53%|2,30%|1,32%|2,41%|0,15%|0,22%|3,58%|0,01%|0,00%|0,01%|0,00%|0,00%|
|Colegio Bosquemar|1,91%|4,33%|1,39%|3,35%|0,06%|0,21%|1,29%|0,01%|0,00%|0,00%|0,01%|0,01%|
|Miradores Los Volcanes II|0,62%|1,83%|0,63%|2,84%|0,04%|0,17%|0,93%|0,00%|0,00%|0,00%|0,00%|0,00%|
|Bosquemar II|0,82%|2,74%|0,77%|3,10%|0,04%|0,20%|1,18%|0,01%|0,00%|0,00%|0,00%|0,00%|
|Loteo Bosquemar|1,71%|2,82%|1,22%|2,30%|0,10%|0,18%|1,37%|0,01%|0,00%|0,00%|0,00%|0,00%|
|Parque Costanera I|1,03%|1,57%|0,71%|1,17%|0,09%|0,18%|1,46%|0,00%|0,00%|0,00%|0,00%|0,00%|
|Parque Costanera III|1,42%|1,96%|0,91%|1,37%|0,11%|0,17%|1,64%|0,00%|0,00%|0,00%|0,00%|0,00%|
|Altos Tenglo III|1,10%|1,81%|0,69%|1,16%|0,10%|0,18%|1,27%|0,01%|0,00%|0,00%|0,00%|0,00%|
|Villa Juan XXIII|1,18%|2,08%|0,74%|1,35%|0,09%|0,25%|1,88%|0,01%|0,00%|0,00%|0,00%|0,00%|
|Brisamar|1,14%|1,78%|0,73%|1,20%|0,10%|0,19%|1,18%|0,00%|0,00%|0,00%|0,00%|0,00%|
|Los Albatros|0,93%|1,45%|0,58%|0,94%|0,09%|0,16%|0,96%|0,00%|0,00%|0,00%|0,00%|0,00%|
|Conjunto Los Lagos|0,93%|1,56%|0,58%|1,00%|0,09%|0,15%|2,24%|0,00%|0,00%|0,00%|0,00%|0,00%|
|Escuela Padre Alberto Hurtado|0,84%|1,42%|0,52%|0,90%|0,07%|0,13%|1,37%|0,00%|0,00%|0,00%|0,00%|0,00%|
|Población Juan Pablo II|0,92%|1,47%|0,57%|0,94%|0,06%|0,12%|0,88%|0,00%|0,00%|0,00%|0,00%|0,00%|
|Conjunto Habitacional Viento Sur|0,59%|1,06%|0,37%|0,70%|0,07%|0,12%|1,62%|0,00%|0,00%|0,00%|0,00%|0,00%|
|Población Vicuña Mackenna|0,68%|1,22%|0,42%|0,79%|0,05%|0,10%|2,39%|0,00%|0,00%|0,00%|0,00%|0,00%|
|Lomas de Cardonal|0,73%|1,36%|0,45%|0,86%|0,05%|0,10%|3,05%|0,00%|0,00%|0,00%|0,00%|0,00%|
|Alto Mackenna|0,60%|1,18%|0,37%|0,75%|0,04%|0,09%|2,37%|0,00%|0,00%|0,00%|0,00%|0,00%|
|Est Mirasol|0,17%|0,34%|0,11%|0,22%|0,02%|0,07%|0,37%|0,00%|0,00%|0,00%|0,00%|0,00%|
|Est Alerce|0,00%|0,00%|0,00%|0,00%|0,00%|0,00%|0,01%|0,00%|0,00%|0,00%|0,00%|0,00%|
|Est Puerto Varas|0,00%|0,01%|0,00%|0,01%|0,00%|0,00%|0,01%|0,00%|0,00%|0,00%|0,00%|0,00%|
|Villa Clotario Blest|0,54%|0,98%|0,34%|0,62%|0,07%|0,12%|1,13%|0,00%|0,00%|0,00%|0,00%|0,00%|
|Villa Los Poetas|0,44%|0,94%|0,27%|0,60%|0,04%|0,10%|0,79%|0,00%|0,00%|0,00%|0,00%|0,00%|

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente Bosquemar”_ _36_

|Receptor|MP10 (ug/m3)|Col3|MP2,5 (ug/m3)|Col5|NO2 (ug/m3)|Col7|Col8|CO (ug/m3)|Col10|SO2 (ug/m3) Primario|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Receptor|Media Anual|P98 24 hrs|Media Anual|P98 24 hrs|Media Anual|P99 1 hr|P99 1 hr|P99 8 hrs|P99 1 hr|Media Anual|P99 24 hrs|P98,5 1 hr|
|Población Bernardo OHiggins|0,44%|0,82%|0,27%|0,52%|0,02%|0,07%|0,51%|0,00%|0,00%|0,00%|0,00%|0,00%|
|Terrazas de Angelmó|0,23%|0,45%|0,15%|0,29%|0,03%|0,08%|0,45%|0,00%|0,00%|0,00%|0,00%|0,00%|
|Villa San Antonio|0,41%|0,78%|0,26%|0,53%|0,02%|0,06%|0,34%|0,00%|0,00%|0,00%|0,00%|0,00%|
|Barrio Vicente Pérez Rosales|0,03%|0,08%|0,02%|0,05%|0,01%|0,02%|0,11%|0,00%|0,00%|0,00%|0,00%|0,00%|
|Villa Vicente Pérez Rosales|0,04%|0,09%|0,03%|0,07%|0,01%|0,03%|0,14%|0,00%|0,00%|0,00%|0,00%|0,00%|
|III-IV|0,18%|0,59%|0,19%|0,70%|0,02%|0,11%|0,63%|0,00%|0,00%|0,00%|0,00%|0,00%|
|Bosquemar IX|0,15%|0,55%|0,15%|0,71%|0,02%|0,13%|0,82%|0,00%|0,00%|0,00%|0,00%|0,00%|
|Llanos de Tenglo|0,03%|0,15%|0,03%|0,20%|0,01%|0,04%|0,25%|0,00%|0,00%|0,00%|0,00%|0,00%|
|Puerta Sur|0,08%|0,18%|0,06%|0,14%|0,01%|0,05%|0,25%|0,00%|0,00%|0,00%|0,00%|0,00%|
|**Límite Normativo**|**50**|**130**|**20**|**50**|**40**|**100**|**200**|**30.000**|**10.000**|**60**|**150**|**350**|

Fuente: Elaboración propia, 2025

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente Bosquemar”_ _37_

**8.3. Análisis del Impacto Significativo**

Tal como se menciona en el capítulo anterior, la línea de base de MP2,5 de la estación Mirasol se encuentra en
saturación en sus dos estadísticos normados. A continuación, las Tabla 17 y Tabla 18 muestra los aportes del
proyecto para el año 7 y año 9 en los receptores evaluados comparados con los límites del “Criterio de Evaluación
en el SIEA: Impacto de emisiones en zonas saturadas por material particulado respirable MP10 y material
particulado fino respirable MP2,5”. Se destaca que, para la comparación de los límites de impacto significativo, se
utilizó la tabla 1, ya que, el proyecto presenta aumento de las concentraciones mayor a 3 año.

Tabla 17 Análisis de Impacto Significativo MP2,5 μg/m3, Escenario Construcción más Operación del año 7

|Col1|Media Anual|Incremento<br>Concentración|%|P98 24H|Incremento<br>Concentración|%|
|---|---|---|---|---|---|---|
|Puerta Bosquemar|0,26|0,33|0,78|1,25|1,71|0,73|
|Colegio Bosquemar|0,26|0,33|0,79|1,55|1,71|0,91|
|Miradores Los Volcanes II|0,14|0,33|0,42|1,44|1,71|0,84|
|Bosquemar II|0,16|0,33|0,48|1,68|1,71|0,98|
|Loteo Bosquemar|0,22|0,33|0,68|1,02|1,71|0,60|
|Parque Costanera I|0,13|0,33|0,39|0,58|1,71|0,34|
|Parque Costanera III|0,16|0,33|0,47|0,60|1,71|0,35|
|Altos Tenglo III|0,12|0,33|0,35|0,51|1,71|0,30|
|Villa Juan XXIII|0,12|0,33|0,38|0,57|1,71|0,33|
|Brisamar|0,13|0,33|0,38|0,51|1,71|0,30|
|Los Albatros|0,10|0,33|0,30|0,40|1,71|0,23|
|Conjunto Los Lagos|0,10|0,33|0,30|0,42|1,71|0,25|
|Escuela Padre Alberto Hurtado|0,09|0,33|0,27|0,40|1,71|0,23|
|Población Juan Pablo II|0,10|0,33|0,29|0,40|1,71|0,23|
|Conjunto Habitacional Viento<br>Sur|0,06|0,33|0,19|0,30|1,71|0,18|
|Población Vicuña Mackenna|0,07|0,33|0,22|0,34|1,71|0,20|
|Lomas de Cardonal|0,08|0,33|0,23|0,36|1,71|0,21|
|Alto Mackenna|0,06|0,33|0,19|0,31|1,71|0,18|
|Est Mirasol|0,02|0,33|0,06|0,09|1,71|0,05|
|Est Alerce|0,00|0,33|0,00|0,00|1,71|0,00|
|Est Puerto Varas|0,00|0,33|0,00|0,00|1,71|0,00|
|Villa Clotario Blest|0,06|0,33|0,17|0,27|1,71|0,16|
|Villa Los Poetas|0,05|0,33|0,14|0,25|1,71|0,15|
|Población Bernardo OHiggins|0,05|0,33|0,14|0,22|1,71|0,13|
|Terrazas de Angelmó|0,02|0,33|0,07|0,12|1,71|0,07|
|Villa San Antonio|0,04|0,33|0,13|0,22|1,71|0,13|
|Barrio Vicente Pérez Rosales|0,00|0,33|0,01|0,03|1,71|0,01|
|Villa Vicente Pérez Rosales|0,00|0,33|0,01|0,03|1,71|0,02|
|III-IV|0,06|0,33|0,18|0,59|1,71|0,35|
|Bosquemar IX|0,04|0,33|0,11|0,38|1,71|0,22|
|Llanos de Tenglo|0,01|0,33|0,02|0,11|1,71|0,07|
|Puerta Sur|0,01|0,33|0,03|0,06|1,71|0,04|

Fuente: Elaboración propia, 2025

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente_
_38_
_Bosquemar”_

Tabla 18 Análisis de Impacto Significativo MP2,5 μg/m3, Escenario Operación del año 9

|Receptor|Media Anual|Incremento<br>Concentración|%|P98 24H|Incremento<br>Concentración|%|
|---|---|---|---|---|---|---|
|Puerta Bosquemar|0,26|0,33|80,00%|1,21|1,71|70,47%|
|Colegio Bosquemar|0,28|0,33|84,27%|1,68|1,71|97,96%|
|Miradores Los Volcanes II|0,13|0,33|38,08%|1,42|1,71|82,99%|
|Bosquemar II|0,15|0,33|46,37%|1,55|1,71|90,77%|
|Loteo Bosquemar|0,24|0,33|73,87%|1,15|1,71|67,31%|
|Parque Costanera I|0,14|0,33|43,00%|0,58|1,71|34,13%|
|Parque Costanera III|0,18|0,33|54,90%|0,68|1,71|40,03%|
|Altos Tenglo III|0,14|0,33|41,64%|0,58|1,71|34,04%|
|Villa Juan XXIII|0,15|0,33|44,69%|0,67|1,71|39,46%|
|Brisamar|0,15|0,33|44,34%|0,60|1,71|35,02%|
|Los Albatros|0,12|0,33|35,35%|0,47|1,71|27,35%|
|Conjunto Los Lagos|0,12|0,33|35,21%|0,50|1,71|29,26%|
|Escuela Padre Alberto Hurtado|0,10|0,33|31,44%|0,45|1,71|26,31%|
|Población Juan Pablo II|0,11|0,33|34,65%|0,47|1,71|27,39%|
|Conjunto Habitacional Viento<br>Sur|0,07|0,33|22,31%|0,35|1,71|20,59%|
|Población Vicuña Mackenna|0,08|0,33|25,55%|0,40|1,71|23,14%|
|Lomas de Cardonal|0,09|0,33|27,15%|0,43|1,71|25,08%|
|Alto Mackenna|0,07|0,33|22,49%|0,37|1,71|21,88%|
|Est Mirasol|0,02|0,33|6,56%|0,11|1,71|6,45%|
|Est Alerce|0,00|0,33|0,07%|0,00|1,71|0,13%|
|Est Puerto Varas|0,00|0,33|0,13%|0,00|1,71|0,18%|
|Villa Clotario Blest|0,07|0,33|20,47%|0,31|1,71|18,14%|
|Villa Los Poetas|0,05|0,33|16,31%|0,30|1,71|17,52%|
|Población Bernardo OHiggins|0,05|0,33|16,38%|0,26|1,71|15,19%|
|Terrazas de Angelmó|0,03|0,33|8,81%|0,14|1,71|8,38%|
|Villa San Antonio|0,05|0,33|15,63%|0,27|1,71|15,53%|
|Barrio Vicente Pérez Rosales|0,00|0,33|1,26%|0,03|1,71|1,59%|
|Villa Vicente Pérez Rosales|0,01|0,33|1,67%|0,04|1,71|2,08%|
|III-IV|0,04|0,33|11,58%|0,35|1,71|20,45%|
|Bosquemar IX|0,03|0,33|9,17%|0,35|1,71|20,61%|
|Llanos de Tenglo|0,01|0,33|1,97%|0,10|1,71|5,71%|
|Puerta Sur|0,01|0,33|3,67%|0,07|1,71|4,06%|

Fuente: Elaboración propia, 2025

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente_
_39_
_Bosquemar”_

**8.4. Puntos de Máximo Impacto**

En las siguientes tablas se muestran las concentraciones y ubicaciones de los puntos de máximo impacto (PMI)
para el escenario de construcción y operación del año 7 y la Operación del año 9 del proyecto, se destaca que estos
valores ya fueron corregidos por la incertidumbre.

Tabla 19 Punto Máximo Impacto, Escenario Construcción más Operación del año 7

|Contaminante|Estadístico|PMI|Limite<br>Normativo (LN)|PMI/LN|Ubicación UTM-WGS-84-huso-19S|Col7|
|---|---|---|---|---|---|---|
|Contaminante|Estadístico|PMI|Limite<br>Normativo (LN)|PMI/LN|Este (m)|Norte (m)|
|MP10 ug/m3|Media|1,37|50|2,74%|667478|5405743|
|MP10 ug/m3|P98|5,13|130|3,95%|667478|5405743|
|M2,5 ug/m3|Media|0,35|20|1,73%|667478|5405743|
|M2,5 ug/m3|P98|1,26|50|2,52%|667478|5405743|
|NO2 ug/m3|Media|0,09|40|0,24%|667456|5404744|
|NO2 ug/m3|P99 24H|1,02|100|1,02%|667456|5404744|
|NO2 ug/m3|P99 1H|18,79|200|9,40%|666453|5404767|
|CO ug/m3|P99 1H|15,92|30.000|0,05%|666453|5404767|
|CO ug/m3|P99 8H|2,27|10.000|0,02%|666453|5404767|
|SO2 ug/m3<br>Primaria|Media|0,00|60|0,00%|667456|5404744|
|SO2 ug/m3<br>Primaria|p99 24h|0,01|150|0,01%|667456|5404744|
|SO2 ug/m3<br>Primaria|p99 1H|0,03|350|0,01%|667456|5404744|

Fuente: Elaboración propia, 2025

Tabla 20 Punto Máximo Impacto, Escenario Operación del año 9

|Contaminante|Estadístico|PMI|Limite<br>Normativo (LN)|PMI/LN|Ubicación UTM-WGS-84-huso-19S|Col7|
|---|---|---|---|---|---|---|
|Contaminante|Estadístico|PMI|Limite<br>Normativo (LN)|PMI/LN|Este (m)|Norte (m)|
|MP10 ug/m3|Media|1,61|50|3,23%|667.478|5.405.743|
|MP10 ug/m3|P98|6,19|130|4,76%|667.478|5.405.743|
|M2,5 ug/m3|Media|0,41|20|2,03%|667.478|5.405.743|
|M2,5 ug/m3|P98|1,52|50|3,04%|667.478|5.405.743|
|NO2 ug/m3|Media|0,05|40|0,12%|667.478|5.405.743|
|NO2 ug/m3|P99 24H|0,28|100|0,28%|667.456|5.404.744|
|NO2 ug/m3|P99 1H|4,99|200|2,50%|667.478|5.405.743|
|CO ug/m3|P99 1H|3,50|30.000|0,01%|667.478|5.405.743|
|CO ug/m3|P99 8H|0,62|10.000|0,01%|667.478|5.405.743|
|SO2 ug/m3<br>Primaria|Media|0,00|60|0,00%|667.478|5.405.743|
|SO2 ug/m3<br>Primaria|p99 24h|0,01|150|0,01%|667.478|5.405.743|
|SO2 ug/m3<br>Primaria|p99 1H|0,03|350|0,01%|667.478|5.405.743|

Fuente: Elaboración propia, 2025

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente_
_40_
_Bosquemar”_

En la Figura 15 podemos ver los puntos de máximo impacto del escenario de construcción más operación del año
7 y en la Figura 16 se encuentran los puntos de máximo impacto del escenario de operación del año 9.

Figura 15 Ubicación de los PMI, Escenario Construcción Más Operación Año 7

Fuente: Elaboración propia, 2025

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente_
_41_
_Bosquemar”_

Figura 16 Ubicación de los PMI, Escenario Operación Año 9

Fuente: Elaboración propia, 2025

**8.5. Isoconcentraciones**

Las siguientes figuras muestran las isoconcentraciones del proyecto para el escenario de construcción y operación
del proyecto del año 7 y el año de la operación del año 9, y para cada contaminante considerado en el estudio.

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente_
_42_
_Bosquemar”_

Figura 17 Isolíneas de Concentración MP-10 Promedio Anual, Escenario Construcción más Operación Año 7

Fuente: Elaboración propia, 2025

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente Bosquemar”_ _43_

Figura 18 Isolíneas de Concentración MP-10 Percentil 98, Escenario Construcción más Operación Año 7

Fuente: Elaboración propia, 2025

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente Bosquemar”_ _44_

Figura 19 Isolíneas Concentración MP-2,5 Media Anual, Escenario Construcción más Operación Año 7

Fuente: Elaboración propia, 2025

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente Bosquemar”_ _45_

Figura 20 Isolíneas Concentración MP-2,5 Percentil 98, Escenario Construcción más Operación Año 7

Fuente: Elaboración propia, 2025

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente Bosquemar”_ _46_

Figura 21 Isolíneas de Concentración NO2 Media Anual, Escenario Construcción más Operación Año 7

Fuente: Elaboración propia, 2025

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente Bosquemar”_ _47_

Figura 22 Isolíneas de Concentración NO2, Percentil 99 1 Hora, Escenario Construcción más Operación Año 7

Fuente: Elaboración propia, 2025

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente Bosquemar”_ _48_

Figura 23 Isolíneas de Concentración NO2, Percentil 99 24 Horas, Escenario Construcción más Operación Año 7

Fuente: Elaboración propia, 2025

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente Bosquemar”_ _49_

Figura 24 Isolíneas de Concentración CO Percentil 99 1 Hora, Escenario Construcción más Operación Año 7

Fuente: Elaboración propia, 2025

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente Bosquemar”_ _50_

Figura 25 Isolíneas de Concentración CO Percentil 99 8 Horas, Escenario Construcción más Operación Año 7

Fuente: Elaboración propia, 2025

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente Bosquemar”_ _51_

Figura 26 Isolíneas de Concentración SO2 Media Anual, Escenario Construcción más Operación Año 7

Fuente: Elaboración propia, 2025

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente Bosquemar”_ _52_

Figura 27 Isolíneas de Concentración SO2, Percentil 99 24 Horas, Escenario Construcción más Operación Año 7

Fuente: Elaboración propia, 2025

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente Bosquemar”_ _53_

Figura 28 Isolíneas de Concentración SO2, Percentil 99 1 Hora, Escenario Construcción más Operación Año 7

Fuente: Elaboración propia, 2025

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente Bosquemar”_ _54_

Figura 29 Isolíneas de Concentración MP-10 Promedio Anual, Escenario Operación Año 9

Fuente: Elaboración propia, 2025

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente Bosquemar”_ _55_

Figura 30 Isolíneas de Concentración MP-10 Percentil 98, Escenario Operación Año 9

Fuente: Elaboración propia, 2025

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente Bosquemar”_ _56_

Figura 31 Isolíneas Concentración MP-2,5 Media Anual, Escenario Operación Año 9

Fuente: Elaboración propia, 2025

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente Bosquemar”_ _57_

Figura 32 Isolíneas Concentración MP-2,5 Percentil 98, Escenario Operación Año 9

Fuente: Elaboración propia, 2025

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente Bosquemar”_ _58_

Figura 33 Isolíneas de Concentración NO2 Media Anual, Escenario Operación Año 9

Fuente: Elaboración propia, 2025

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente Bosquemar”_ _59_

Figura 34 Isolíneas de Concentración NO2 Percentil 99, 1 Hora, Escenario Operación Año 9

Fuente: Elaboración propia, 2025

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente Bosquemar”_ _60_

Figura 35 Isolíneas de Concentración NO2 Percentil 99, 24 Horas, Escenario Operación Año 9

Fuente: Elaboración propia, 2025

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente Bosquemar”_ _61_

Figura 36 Isolíneas de Concentración CO Percentil 99 1 Hora, Escenario Operación Año 9

Fuente: Elaboración propia, 2025

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente Bosquemar”_ _62_

Figura 37 Isolíneas de Concentración CO Percentil 99 8 Horas, Escenario Operación Año 9

Fuente: Elaboración propia, 2025

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente Bosquemar”_ _63_

Figura 38 Isolíneas de Concentración SO2 Media Anual, Escenario Operación Año 9

Fuente: Elaboración propia, 2025

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente Bosquemar”_ _64_

Figura 39 Isolíneas de Concentración SO2 Percentil 99 24 Horas, Escenario Operación Año 9

Fuente: Elaboración propia, 2025

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente Bosquemar”_ _65_

Figura 40 Isolíneas de Concentración SO2, Percentil 99 1 Hora, Escenario Operación

Fuente: Elaboración propia, 2025

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente Bosquemar”_ _66_

**9. ÁREA DE INFLUENCIA**

El Área de influencia (AI) corresponde al área o espacio geográfico de donde se obtiene la información
necesaria para predecir y evaluar los impactos en los elementos del medio ambiente.

La “Guía Para la Descripción del Área de Influencia” del SEA 2017 indica lo siguiente para las áreas de
influencia del componente aire: _“Sobre los contaminantes del aire se puede indicar que las emisiones_
_atmosféricas de los proyectos en general pueden aumentar las concentraciones ambientales de_
_contaminantes e impactar en la calidad del recurso natural renovable aire; para determinar el AI para_
_este elemento, se busca cual es el mayor espacio geográfico comprendido por el emplazamiento de la_
_parte del proyecto que constituye la fuente de dichas emisiones. El aumento en la concentración_
_ambiental de contaminantes también puede generar riesgo para la salud de la población y por lo tanto_
_el AI para este elemento del medio ambiente se determina en relación con la presencia de población que_
_puede verse expuesta a dichos contaminantes”._

En base a lo anterior, el AI para el proyecto fue determinado en base a un criterio del límite normativo,
el cual corresponde a la formación de isoconcentraciones a un valor de corte respecto al límite de la
norma. Para las isoconcentraciones formadas bajo el criterio indicado anteriormente se realiza una
unión de estas con el fin de obtener el área geográfica de influencia del proyecto para los contaminantes
del aire. Para el caso de este proyecto se utilizó como corte los límites de impacto significativo del
“Criterio de Evaluación en el SIEA: Impacto de emisiones en zonas saturadas por material particulado
respirable MP10 y material particulado fino respirable MP2,5”, sin embargo, no se formaron
isoconcentraciones para esos límites. Con el fin de generar el área de influencia se optó por un límite
más restrictivo y fue utilizar el 1% de la norma del contaminante saturado, el resultado se muestra en la
siguiente figura.

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente_
_67_
_Bosquemar”_

Figura 41 Área de Influencia del Proyecto Fase de Construcción más Operación Año 7

Fuente: Elaboración propia, 2025

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente_
_68_
_Bosquemar”_

Figura 42 Área de Influencia del Proyecto Fase Operación Año 9

Fuente: Elaboración propia, 2025

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente_
_69_
_Bosquemar”_

**10. CONCLUSIONES**

Respecto a los resultados obtenidos en los capítulos anteriores de la modelación de la calidad del aire usando
CALPUFF se puede concluir lo siguiente:

**Contaminantes Norma de Calidad Primaria**

Las mayores concentraciones obtenidas se encuentran en los receptores cercanos al proyecto, ya que para el año

7 ocurre la actividad de construcción y para el año 9 se modelan las chimeneas de los calefactores a pellets del

proyecto.

**Área de Influencia**

Como se puede ver el área de influencia del proyecto para los contaminantes del aire es local, cerca de las
inmediaciones del proyecto y corresponde al contaminante en saturación MP2,5.

**Análisis Normativo**

Al comparar los resultados de los aportes del proyecto para el año 7 y año 9 con los límites de impacto significativo
del “Criterio de Evaluación en el SIEA: Impacto de emisiones en zonas saturadas por material particulado respirable
MP10 y material particulado fino respirable MP2,5”, podemos observar que no se superan estos límites en todos
los receptores evaluados.

**Puntos de Máximo Impacto**

Los puntos de máximo impacto para el escenario de construcción y operación se encuentran en zonas no habitadas
de la construcción del proyecto o en zonas no habitadas.

**Isoconcentraciones**

Respecto a las isoncentraciones, están son preferentemente cercanas al proyecto, y la mayoría de las líneas de
concentración no supera el 1 μg/m [3 ] para los contaminantes evaluados.

_Finalmente, se puede concluir que los aportes del proyecto son bajos en ambos escenarios donde no presentan_
_grandes aportes porcentuales respecto a la norma y que a pesar de modelar en el peor escenario no se sobrepasan_
_los límites de impacto significativo._

_Informe de emisiones atmosféricas, DIA “Conjunto Habitacional Don Vicente_
_70_
_Bosquemar”_

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1: Normativa Ambiental Vigente**

| Norma | Contaminante | Estadístico | Límite Noma | Referencia |
| --- | --- | --- | --- | --- |
| Primaria | MP10 | Media Anual | 50 μg/m3N | D.S. 12/21 MMA |
| Primaria | MP10 | Percentil 98 Diario | 130 μg/m3N | D.S. 12/21 MMA |
| Primaria | MP2,5 | Media Anual | 20 μg/m3 | D.S. 12/11 MMA |
| Primaria | MP2,5 | Percentil 98 Diario | 50 μg/m3 | D.S. 12/11 MMA |
| Primaria | SO2 | Media Anual | 60 μg/m3N | D.S. 104/19 MMA |
| Primaria | SO2 | Percentil 99 Diario | 150 μg/m3N | D.S. 104/19 MMA |
| Primaria | SO2 | Percentil 99 Horario | 350 μg/m3N | D.S. 104/19 MMA |
| Primaria | NO2 | Media Anual | 60 μg/m3N | D.S. 40/23 MMA |
| Primaria | NO2 | Percentil 99 Diario | 150 μg/m3N | D.S. 40/23 MMA |
| Primaria | NO2 | Percentil 99 Horario | 350 μg/m3N | D.S. 40/23 MMA |
| Primaria | CO | Percentil 8 Horas | 10.000 μg/m3N | D.S. 115/02 MINSEGPRES |
| Primaria | CO | Percentil 99 Horario | 30.000 μg/m3N | D.S. 115/02 MINSEGPRES |

**Tabla 2: Estación de Monitoreo**

| Estación | Coordenadas UTMa | Col3 | Contaminante | Fecha de Monitoreo |
| --- | --- | --- | --- | --- |
| Estación | Este (m) | Norte (m) | Norte (m) | Norte (m) |
| Mirasol | 669.585 | 5.406.017 | MP2,5 | Enero 2021 a diciembre<br>2023 |

**Tabla 3: Línea de Base Estación Mirasol**

| Contaminante | Estadístico | Año | ug/m3 | Norma | % Norma |
| --- | --- | --- | --- | --- | --- |
| MP2,5 ug/m3 | Media Anual | 2021 | 24 | 20 | 120 |
| MP2,5 ug/m3 | Percentil 98 24 horas | Percentil 98 24 horas | 112 | 50 | 224 |
| MP2,5 ug/m3 | Media Anual | 2022 | 29 | 20 | 144 |
| MP2,5 ug/m3 | Percentil 98 24 horas | Percentil 98 24 horas | 141 | 50 | 282 |
| MP2,5 ug/m3 | Media Anual | 2023 | 20 | 20 | 101 |
| MP2,5 ug/m3 | Percentil 98 24 horas | Percentil 98 24 horas | 110 | 50 | 220 |
| MP2,5 ug/m3 | Media Anual | 2024 | 20 | 20 | 100 |
| MP2,5 ug/m3 | Percentil 98 24 horas | Percentil 98 24 horas | 88 | 50 | 177 |

**Tabla 4: Ubicación Estación y Variables Meteorológica Analizada**

| Estación | Coordenadas UTM - WGS 84 | Col3 | Variables | Periodo |
| --- | --- | --- | --- | --- |
| Estación | Este (m) | Norte (m) | Norte (m) | Norte (m) |
| Alerce | 669.585 | 5.406.016 | Velocidad del viento<br>Dirección del viento<br>Temperatura | 01 de enero al 31 de<br>diciembre 2022 |

**Tabla 5: Estadísticas de Datos Meteorológicos Analizados**

| Estación | Datos Totales | Porcentaje de Datos Válidos | Porcentaje De Calma (%) | Col5 |
| --- | --- | --- | --- | --- |
| Estación | Datos Totales | Porcentaje de Datos Válidos | Periodo Diurno | Periodo Nocturno |
| Alerce | 8.698 | 99% | 5,84% | 25,41% |

**Tabla 6: Estadísticas de Datos Meteorológicos Analizados de Temperatura**

| Estación | Datos Totales | Porcentaje de Datos Válidos |
| --- | --- | --- |
| Alerce | 8.709 | 99,42% |

**Tabla 7: Estadígrafos de evaluación de desempeño del modelo para la velocidad del viento**

| Serie de datos | Velocidad del viento | Col3 | Temperatura | Col5 |
| --- | --- | --- | --- | --- |
| Serie de datos | Valor recomendado | Estación Alerce | Valor recomendado | Estación Alerce |
| SESGO | [-2,5;2,5] (m/s) | 0,04 | [-4;4] (°C) | -1,29 |
| MAE | ≤3 (m/s) | 0,94 | ≤4 (°C) | 1,69 |
| RMSE | ≤3,5 (m/s) | 1,22 | ≤4,5 (°C) | 2,15 |
| CORR | >0,6 | 0,85 | >0,8 | 0,94 |

**Tabla 8: Emisiones Atmosféricas Fase de Construcción más Operación**

| Año | Fase | CO<br>(ton/año<br>) | COV<br>(ton/año<br>) | SOX<br>(ton/año<br>) | NOX<br>(ton/año<br>) | NH3<br>(ton/año<br>) | MP2,5<br>Total<br>(ton/año<br>) | MP10<br>Total<br>(ton/año<br>) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Construcción | 0,3314 | 0,0674 | 0,0013 | 0,6999 | 0,0001 | 0,0876 | 0,3170 |
| 1 | Operación Etapa A-B | 0,0290 | 0,0072 | 0,0013 | 0,1231 | 0,0014 | 0,7434 | 1,4564 |
| 1 | Total | 0,3604 | 0,0746 | 0,0026 | 0,8231 | 0,0015 | 0,8309 | 1,7734 |
| 2 | Construcción | 0,2558 | 0,0450 | 0,0017 | 0,5222 | 0,0004 | 0,0955 | 0,4166 |
| 2 | Operación Etapa A-B-C | 0,0414 | 0,0104 | 0,0019 | 0,1761 | 0,0020 | 0,8417 | 1,8614 |
| 2 | Total | 0,2972 | 0,0553 | 0,0036 | 0,6983 | 0,0023 | 0,9372 | 2,2780 |
| 3 | Construcción | 0,2348 | 0,0536 | 0,0015 | 0,4734 | 0,0002 | 0,0592 | 0,2144 |
| 3 | Operación Etapa A-B-C | 0,0479 | 0,0120 | 0,0022 | 0,2036 | 0,0023 | 0,8929 | 2,0723 |
| 3 | Total | 0,2827 | 0,0656 | 0,0036 | 0,6770 | 0,0025 | 0,9521 | 2,2867 |
| 4 | Construcción | 0,2656 | 0,0491 | 0,0018 | 0,4996 | 0,0004 | 0,1214 | 0,6332 |
| 4 | Operación Etapa A-B-C-D | 0,0685 | 0,0162 | 0,0040 | 0,2923 | 0,0031 | 1,0282 | 2,6258 |
| 4 | Total | 0,3340 | 0,0653 | 0,0058 | 0,7919 | 0,0035 | 1,1496 | 3,2590 |
| 5 | Construcción | 0,1188 | 0,0297 | 0,0011 | 0,3290 | 0,0003 | 0,0764 | 0,3667 |
| 5 | Operación Etapa A-B-C-D-E | 0,0769 | 0,0180 | 0,0048 | 0,3287 | 0,0034 | 1,0834 | 2,8517 |
| 5 | Total | 0,1957 | 0,0476 | 0,0059 | 0,6576 | 0,0037 | 1,1598 | 3,2183 |
| 6 | Construcción | 0,2584 | 0,0488 | 0,0017 | 0,4512 | 0,0003 | 0,0881 | 0,4650 |
| 6 | Operación Etapa A-B-C-D-E | 0,0889 | 0,0204 | 0,0058 | 0,3805 | 0,0039 | 1,1625 | 3,1754 |
| 6 | Total | 0,3473 | 0,0693 | 0,0076 | 0,8317 | 0,0042 | 1,2506 | 3,6404 |
| 7 | Construcción | 0,2115 | 0,0325 | 0,0017 | 0,3738 | 0,0004 | 0,1082 | 0,6100 |
| 7 | Operación Etapa A-B-C-D-E-F | 0,1058 | 0,0239 | 0,0074 | 0,4536 | 0,0045 | 1,2737 | 3,6303 |
| 7 | Total | 0,3173 | 0,0564 | 0,0090 | 0,8274 | 0,0050 | 1,3819 | 4,2403 |
| 8 | Construcción | 0,1069 | 0,0330 | 0,0010 | 0,2711 | 0,0002 | 0,0459 | 0,2002 |
| 8 | Operación Etapa A-B-C-D-E-F-<br>G | 0,1145 | 0,0257 | 0,0082 | 0,4910 | 0,0049 | 1,3309 | 3,8644 |
| 8 | Total | 0,2213 | 0,0587 | 0,0091 | 0,7621 | 0,0051 | 1,3767 | 4,0645 |
| 9 y en<br>adelante | Operación Etapa A-B-C-D-E-F-<br>G | 0,1298 | 0,0289 | 0,0095 | 0,5574 | 0,0055 | 1,4321 | 4,2784 |

**Tabla 9: Parámetros Ingresados a Cada Fuente**

| Tipo de Fuente | Parámetros | Valores |
| --- | --- | --- |
| Fuentes Tipo Ruta para todas las fases | Inicial Sigma Y m | 3,5 |
| Fuentes Tipo Ruta para todas las fases | Inicial Sigma Z m | 0 |
| Fuentes Tipo Ruta para todas las fases | Altura Efectiva m | 0 |
| Fuentes Tipo Área-Polígono | Inicial Sigma Z m | 0 |
| Fuentes Tipo Área-Polígono | Altura Efectiva m | 0 |
| Fuentes Tipo Puntual Generadores | Altura del Escape m | 1,47 |
| Fuentes Tipo Puntual Generadores | Temperatura de Salida K | 783,15 |
| Fuentes Tipo Puntual Generadores | Diámetro Interno m | 0,076 |
| Fuentes Tipo Puntual Generadores | Velocidad de Salida m/s | 59,78 |

**Tabla 10: Emisiones Ingresadas al Modelo Construcción y Operación Año 7**

| Tipo de<br>Fuente | ID | Descripci<br>ón | SO2 | SO4 | NO | NO2 | HNO3 | NO3 | CO | PM10 | PM2.5 | Unidad |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ROAD | C7_1 | Ruta<br>Hormigó<br>n | 4,50E-09 | 2,37E-10 | 5,45E-07 | 6,20E-08 | 6,20E-09 | 6,20E-09 | 2,82E-08 | 2,61E-07 | 6,47E-08 | g/s*m |
| ROAD | C7_2 | Ruta<br>Botader<br>o 1 | 4,50E-09 | 2,37E-10 | 5,45E-07 | 6,20E-08 | 6,20E-09 | 6,20E-09 | 2,82E-08 | 2,14E-07 | 5,63E-08 | g/s*m |
| ROAD | C7_3 | Ruta<br>Botader<br>o 2 | 4,50E-09 | 2,37E-10 | 5,45E-07 | 6,20E-08 | 6,20E-09 | 6,20E-09 | 2,82E-08 | 2,14E-07 | 5,63E-08 | g/s*m |
| ROAD | C7_4 | RESPEL | 4,50E-09 | 2,37E-10 | 5,45E-07 | 6,20E-08 | 6,20E-09 | 6,20E-09 | 2,82E-08 | 6,46E-09 | 6,12E-09 | g/s*m |
| ROAD | C7_5 | Ruta No<br>Pav<br>Interna | 5,65E-09 | 2,97E-10 | 7,01E-07 | 7,96E-08 | 7,96E-09 | 7,96E-09 | 3,75E-08 | 9,21E-05 | 9,22E-06 | g/s*m |
| ROAD | C7_6 | Ruta Pav<br>Interna | 4,50E-09 | 2,37E-10 | 5,45E-07 | 6,20E-08 | 6,20E-09 | 6,20E-09 | 2,82E-08 | 2,33E-06 | 5,67E-07 | g/s*m |
| ROAD | C7_7 | Ruta No<br>Pav Ext | 4,50E-09 | 2,37E-10 | 5,45E-07 | 6,20E-08 | 6,20E-09 | 6,20E-09 | 2,82E-08 | 4,09E-05 | 4,09E-06 | g/s*m |
| AREA_P<br>OLY | C7_8 | Etapa G | 1,36E-08 | 7,14E-10 | 3,98E-06 | 4,53E-07 | 4,53E-08 | 4,53E-08 | 3,48E-06 | 1,47E-06 | 7,51E-07 | g/s*m2 |
| AREA_P<br>OLY | C7_9 | Erosión | 0,00E+0<br>0 | 0,00E+0<br>0 | 0,00E+0<br>0 | 0,00E+0<br>0 | 0,00E+0<br>0 | 0,00E+0<br>0 | 0,00E+0<br>0 | 7,38E-08 | 1,13E-08 | g/s*m2 |
| ROAD | C7_11 | Ruta<br>Calzada | 4,50E-09 | 2,37E-10 | 5,45E-07 | 6,20E-08 | 6,20E-09 | 6,20E-09 | 2,82E-08 | 6,96E-09 | 6,24E-09 | g/s*m |
| ROAD | C7_12 | Ruta<br>Sodimac | 4,50E-09 | 2,37E-10 | 5,45E-07 | 6,20E-08 | 6,20E-09 | 6,20E-09 | 2,82E-08 | 2,60E-08 | 1,08E-08 | g/s*m |
| POINT | SRC_1 a<br>SCR_232 | Pellets<br>Operació<br>n | 0,00E+0<br>0 | 0,00E+0<br>0 | 0,00E+0<br>0 | 0,00E+0<br>0 | 0,00E+0<br>0 | 0,00E+0<br>0 | 0,00E+0<br>0 | 4,03E-04 | 4,03E-04 | g/s |
| POINT | SRC_233<br>a 235 | Generad<br>ores<br>Operació<br>n | 2,39E-02 | 1,26E-03 | 3,36E-01 | 3,82E-02 | 3,82E-03 | 3,82E-03 | 8,22E-02 | 2,68E-02 | 2,68E-02 | g/s |
| ROAD | SRC_237 | Ruta 1<br>Operació<br>n | 1,49E-07 | 7,83E-09 | 1,30E-05 | 1,48E-06 | 1,48E-07 | 1,48E-07 | 3,48E-06 | 1,13E-04 | 2,75E-05 | g/s*m al<br>día |
| ROAD | SRC_238 | Ruta 2<br>Operació<br>n | 1,49E-07 | 7,83E-09 | 1,30E-05 | 1,48E-06 | 1,48E-07 | 1,48E-07 | 3,48E-06 | 1,13E-04 | 2,75E-05 | g/s*m al<br>día |
| ROAD | SRC_239 | Ruta 3<br>Operació<br>n | 1,49E-07 | 7,83E-09 | 1,30E-05 | 1,48E-06 | 1,48E-07 | 1,48E-07 | 3,48E-06 | 1,13E-04 | 2,75E-05 | g/s*m al<br>día |
| ROAD | SRC_240 | Ruta 4<br>Operació<br>n | 1,49E-07 | 7,83E-09 | 1,30E-05 | 1,48E-06 | 1,48E-07 | 1,48E-07 | 3,48E-06 | 1,13E-04 | 2,75E-05 | g/s*m al<br>día |
| ROAD | SRC_241 | Ruta 5<br>Operació<br>n | 1,49E-07 | 7,83E-09 | 1,30E-05 | 1,48E-06 | 1,48E-07 | 1,48E-07 | 3,48E-06 | 1,13E-04 | 2,75E-05 | g/s*m al<br>día |

**Tabla 11: Emisiones Ingresadas Operación Año 9**

| Tipo de<br>Fuente | ID | Descripci<br>ón | SO2 | SO4 | NO | NO2 | HNO3 | NO3 | CO | PM10 | PM2.5 | Unidad |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| POINT | SRC_1 a<br>SCR_232 | Pellets<br>Operació<br>n | 0,00E+0<br>0 | 0,00E+0<br>0 | 0,00E+0<br>0 | 0,00E+0<br>0 | 0,00E+0<br>0 | 0,00E+0<br>0 | 0,00E+0<br>0 | 4,03E-04 | 4,03E-04 | g/s |
| POINT | SRC_233<br>a 236 | Generad<br>ores<br>Operació<br>n | 2,39E-02 | 1,26E-03 | 3,36E-01 | 3,82E-02 | 3,82E-03 | 3,82E-03 | 8,22E-02 | 2,68E-02 | 2,68E-02 | g/s |
| ROAD | SRC_237 | Ruta 1<br>Operació<br>n | 1,80E-07 | 9,46E-09 | 1,57E-05 | 1,79E-06 | 1,79E-07 | 1,79E-07 | 4,20E-06 | 1,37E-04 | 3,32E-05 | g/s*m al<br>día |
| ROAD | SRC_238 | Ruta 2<br>Operació<br>n | 1,80E-07 | 9,46E-09 | 1,57E-05 | 1,79E-06 | 1,79E-07 | 1,79E-07 | 4,20E-06 | 1,37E-04 | 3,32E-05 | g/s*m al<br>día |

**Tabla 12: Receptores Considerados en el Proyecto**

| Receptores | Tipo | Ubicación UTM-WGS-84-huso 19S | Col4 |
| --- | --- | --- | --- |
| Receptores | Tipo | Este (m) | Norte (m) |
| Puerta Bosquemar | Primario | 667.257 | 5.405.161 |
| Colegio Bosquemar | Primario | 666.926 | 5.405.339 |
| Miradores Los Volcanes II | Primario | 666.865 | 5.405.144 |
| Bosquemar II | Primario | 666.864 | 5.405.242 |
| Loteo Bosquemar | Primario | 667.026 | 5.405.642 |
| Parque Costanera I | Primario | 667.228 | 5.406.183 |
| Parque Costanera III | Primario | 667.532 | 5.405.945 |
| Altos Tenglo III | Primario | 668.048 | 5.405.765 |
| Villa Juan XXIII | Primario | 667.985 | 5.405.963 |
| Brisamar | Primario | 667.525 | 5.406.094 |
| Los Albatros | Primario | 667.708 | 5.406.391 |
| Conjunto Los Lagos | Primario | 667.976 | 5.406.521 |
| Escuela Padre Alberto Hurtado | Primario | 668.256 | 5.406.469 |
| Población Juan Pablo II | Primario | 668.205 | 5.406.699 |
| Conjunto Habitacional Viento Sur | Primario | 667.967 | 5.406.781 |
| Población Vicuña Mackenna | Primario | 668.408 | 5.406.951 |
| Lomas de Cardonal | Primario | 668.509 | 5.407.166 |
| Alto Mackenna | Primario | 668.698 | 5.407.252 |
| Est Mirasol | Primario | 669.587 | 5.406.020 |
| Est Alerce | Primario | 675.589 | 5.414.814 |
| Est Puerto Varas | Primario | 670.038 | 5.422.743 |
| Villa Clotario Blest | Primario | 668.517 | 5.406.009 |
| Villa Los Poetas | Primario | 668.957 | 5.406.520 |
| Población Bernardo OHiggins | Primario | 669.631 | 5.406.774 |
| Terrazas de Angelmó | Primario | 669.314 | 5.405.677 |
| Villa San Antonio | Primario | 669.679 | 5.405.282 |
| Barrio Vicente Pérez Rosales | Primario | 670.899 | 5.406.421 |
| Villa Vicente Pérez Rosales | Primario | 670.648 | 5.406.467 |
| III-IV | Primario | 666.694 | 5.404.758 |
| Bosquemar IX | Primario | 666.372 | 5.405.080 |
| Llanos de Tenglo | Primario | 665.502 | 5.404.343 |
| Puerta Sur | Primario | 667.502 | 5.407.981 |

**Tabla 14: Concentraciones obtenidas en los Receptores Norma Primaria Escenario Operación año 9**

| Receptor | MP10 (ug/m3) | Col3 | MP2,5 (ug/m3) | Col5 | NO2 (ug/m3) | Col7 | Col8 | CO (ug/m3) | Col10 | SO2 (ug/m3) Primario | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor | Media Anual | P98 24 hrs | Media Anual | P98 24 hrs | Media Anual | P99 24 HR | P99 1 HR | P99 1 hrs | P99 8 hr | Media Anual | P99 24 hrs | P99 1 hr |
| Puerta Bosquemar | 0,7633 | 2,9913 | 0,2640 | 1,2050 | 0,0582 | 0,2178 | 7,1677 | 3,4032 | 0,2044 | 0,0034 | 0,0043 | 0,0108 |
| Colegio Bosquemar | 0,9542 | 5,6287 | 0,2781 | 1,6752 | 0,0242 | 0,2114 | 2,5780 | 2,4276 | 0,4777 | 0,0012 | 0,0079 | 0,0245 |
| Miradores Los Volcanes II | 0,3081 | 2,3834 | 0,1257 | 1,4192 | 0,0141 | 0,1671 | 1,8612 | 1,1623 | 0,2487 | 0,0003 | 0,0034 | 0,0084 |
| Bosquemar II | 0,4079 | 3,5630 | 0,1530 | 1,5521 | 0,0157 | 0,2041 | 2,3673 | 2,0515 | 0,3568 | 0,0004 | 0,0051 | 0,0100 |
| Loteo Bosquemar | 0,8530 | 3,6665 | 0,2438 | 1,1510 | 0,0384 | 0,1809 | 2,7356 | 1,8340 | 0,3752 | 0,0015 | 0,0058 | 0,0157 |
| Parque Costanera I | 0,5165 | 2,0442 | 0,1419 | 0,5836 | 0,0368 | 0,1765 | 2,9210 | 0,9407 | 0,1754 | 0,0008 | 0,0032 | 0,0085 |
| Parque Costanera III | 0,7095 | 2,5431 | 0,1812 | 0,6846 | 0,0431 | 0,1746 | 3,2808 | 1,1753 | 0,2343 | 0,0012 | 0,0037 | 0,0136 |
| Altos Tenglo III | 0,5507 | 2,3502 | 0,1374 | 0,5820 | 0,0389 | 0,1844 | 2,5467 | 1,5164 | 0,3028 | 0,0013 | 0,0049 | 0,0093 |
| Villa Juan XXIII | 0,5895 | 2,7032 | 0,1475 | 0,6748 | 0,0374 | 0,2533 | 3,7512 | 1,5493 | 0,2870 | 0,0012 | 0,0048 | 0,0100 |
| Brisamar | 0,5708 | 2,3129 | 0,1463 | 0,5989 | 0,0398 | 0,1923 | 2,3636 | 0,8799 | 0,2206 | 0,0009 | 0,0034 | 0,0119 |
| Los Albatros | 0,4638 | 1,8847 | 0,1166 | 0,4677 | 0,0379 | 0,1608 | 1,9178 | 1,2856 | 0,2063 | 0,0010 | 0,0031 | 0,0091 |
| Conjunto Los Lagos | 0,4653 | 2,0321 | 0,1162 | 0,5004 | 0,0341 | 0,1506 | 4,4750 | 0,9948 | 0,1810 | 0,0010 | 0,0028 | 0,0089 |
| Escuela Padre Alberto Hurtado | 0,4182 | 1,8524 | 0,1038 | 0,4499 | 0,0279 | 0,1317 | 2,7345 | 0,9888 | 0,1775 | 0,0009 | 0,0033 | 0,0068 |
| Población Juan Pablo II | 0,4625 | 1,9088 | 0,1144 | 0,4684 | 0,0258 | 0,1234 | 1,7600 | 0,8618 | 0,1703 | 0,0009 | 0,0027 | 0,0081 |
| Conjunto Habitacional Viento Sur | 0,2933 | 1,3841 | 0,0736 | 0,3521 | 0,0276 | 0,1229 | 3,2358 | 0,7594 | 0,1333 | 0,0008 | 0,0020 | 0,0060 |
| Población Vicuña Mackenna | 0,3415 | 1,5806 | 0,0843 | 0,3958 | 0,0207 | 0,0991 | 4,7807 | 0,7376 | 0,1458 | 0,0007 | 0,0025 | 0,0062 |
| Lomas de Cardonal | 0,3641 | 1,7654 | 0,0896 | 0,4289 | 0,0189 | 0,0960 | 6,0930 | 0,9289 | 0,1464 | 0,0007 | 0,0025 | 0,0058 |
| Alto Mackenna | 0,3021 | 1,5337 | 0,0742 | 0,3742 | 0,0162 | 0,0928 | 4,7306 | 0,7908 | 0,1347 | 0,0006 | 0,0024 | 0,0047 |
| Est Mirasol | 0,0865 | 0,4390 | 0,0216 | 0,1102 | 0,0096 | 0,0696 | 0,7384 | 0,2331 | 0,0510 | 0,0001 | 0,0008 | 0,0016 |
| Est Alerce | 0,0007 | 0,0052 | 0,0002 | 0,0022 | 0,0001 | 0,0007 | 0,0105 | 0,0017 | 0,0003 | 0,0000 | 0,0000 | 0,0000 |
| Est Puerto Varas | 0,0013 | 0,0073 | 0,0004 | 0,0031 | 0,0002 | 0,0012 | 0,0297 | 0,0046 | 0,0005 | 0,0000 | 0,0000 | 0,0000 |
| Villa Clotario Blest | 0,2705 | 1,2764 | 0,0675 | 0,3101 | 0,0263 | 0,1178 | 2,2523 | 0,8961 | 0,1346 | 0,0007 | 0,0022 | 0,0053 |
| Villa Los Poetas | 0,2182 | 1,2271 | 0,0538 | 0,2996 | 0,0165 | 0,1028 | 1,5863 | 0,7595 | 0,1099 | 0,0004 | 0,0020 | 0,0055 |

**Tabla 15: Concentraciones del Proyecto Comparados con la Normativa Primaria, Escenario Construcción más Operación Año 7**

| Receptor | MP10 (ug/m3) | Col3 | MP2,5 (ug/m3) | Col5 | NO2 (ug/m3) | Col7 | Col8 | CO (ug/m3) | Col10 | SO2 (ug/m3) Primario | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor | Media Anual | P98 24 hrs | Media Anual | P98 24 hrs | Media Anual | P99 1 hr | P99 1 hr | P99 8 hrs | P99 1 hr | Media Anual | P99 24 hrs | P98,5 1 hr |
| Puerta Bosquemar | 1,50% | 2,36% | 1,29% | 2,51% | 0,31% | 1,25% | 13,16% | 0,07% | 0,03% | 0,01% | 0,00% | 0,00% |
| Colegio Bosquemar | 1,81% | 3,93% | 1,30% | 3,11% | 0,18% | 0,86% | 7,73% | 0,04% | 0,02% | 0,00% | 0,01% | 0,01% |
| Miradores Los Volcanes II | 0,81% | 2,53% | 0,70% | 2,87% | 0,19% | 1,28% | 10,74% | 0,06% | 0,03% | 0,00% | 0,00% | 0,00% |
| Bosquemar II | 0,91% | 3,19% | 0,79% | 3,35% | 0,18% | 1,27% | 10,70% | 0,06% | 0,02% | 0,00% | 0,00% | 0,00% |
| Loteo Bosquemar | 1,58% | 2,68% | 1,12% | 2,04% | 0,19% | 0,78% | 6,05% | 0,02% | 0,01% | 0,00% | 0,00% | 0,00% |
| Parque Costanera I | 0,92% | 1,33% | 0,64% | 1,15% | 0,15% | 0,50% | 3,12% | 0,01% | 0,00% | 0,00% | 0,00% | 0,00% |
| Parque Costanera III | 1,22% | 1,72% | 0,78% | 1,20% | 0,13% | 0,52% | 3,04% | 0,01% | 0,00% | 0,00% | 0,00% | 0,00% |
| Altos Tenglo III | 0,93% | 1,58% | 0,58% | 1,02% | 0,10% | 0,34% | 2,20% | 0,01% | 0,00% | 0,00% | 0,00% | 0,00% |
| Villa Juan XXIII | 1,00% | 1,72% | 0,62% | 1,14% | 0,10% | 0,30% | 2,26% | 0,01% | 0,00% | 0,00% | 0,00% | 0,00% |
| Brisamar | 0,98% | 1,56% | 0,63% | 1,02% | 0,12% | 0,34% | 1,72% | 0,01% | 0,00% | 0,00% | 0,00% | 0,00% |
| Los Albatros | 0,79% | 1,24% | 0,50% | 0,80% | 0,10% | 0,32% | 2,32% | 0,01% | 0,00% | 0,00% | 0,00% | 0,00% |
| Conjunto Los Lagos | 0,79% | 1,32% | 0,49% | 0,85% | 0,09% | 0,21% | 2,18% | 0,01% | 0,00% | 0,00% | 0,00% | 0,00% |
| Escuela Padre Alberto Hurtado | 0,71% | 1,19% | 0,44% | 0,80% | 0,07% | 0,20% | 2,36% | 0,00% | 0,00% | 0,00% | 0,00% | 0,00% |
| Población Juan Pablo II | 0,78% | 1,22% | 0,48% | 0,79% | 0,06% | 0,18% | 0,99% | 0,00% | 0,00% | 0,00% | 0,00% | 0,00% |
| Conjunto Habitacional Viento Sur | 0,50% | 0,91% | 0,31% | 0,61% | 0,07% | 0,18% | 1,66% | 0,00% | 0,00% | 0,00% | 0,00% | 0,00% |
| Población Vicuña Mackenna | 0,57% | 1,05% | 0,36% | 0,68% | 0,05% | 0,13% | 1,44% | 0,00% | 0,00% | 0,00% | 0,00% | 0,00% |
| Lomas de Cardonal | 0,61% | 1,14% | 0,38% | 0,72% | 0,05% | 0,11% | 2,11% | 0,00% | 0,00% | 0,00% | 0,00% | 0,00% |
| Alto Mackenna | 0,51% | 0,98% | 0,31% | 0,62% | 0,04% | 0,10% | 1,66% | 0,00% | 0,00% | 0,00% | 0,00% | 0,00% |
| Est Mirasol | 0,15% | 0,29% | 0,09% | 0,19% | 0,03% | 0,07% | 0,41% | 0,00% | 0,00% | 0,00% | 0,00% | 0,00% |
| Est Alerce | 0,00% | 0,00% | 0,00% | 0,00% | 0,00% | 0,00% | 0,01% | 0,00% | 0,00% | 0,00% | 0,00% | 0,00% |
| Est Puerto Varas | 0,00% | 0,01% | 0,00% | 0,01% | 0,00% | 0,00% | 0,01% | 0,00% | 0,00% | 0,00% | 0,00% | 0,00% |
| Villa Clotario Blest | 0,46% | 0,84% | 0,29% | 0,53% | 0,07% | 0,21% | 2,57% | 0,00% | 0,00% | 0,00% | 0,00% | 0,00% |
| Villa Los Poetas | 0,37% | 0,79% | 0,23% | 0,50% | 0,04% | 0,14% | 1,64% | 0,00% | 0,00% | 0,00% | 0,00% | 0,00% |

**Tabla 16: Concentraciones del Proyecto Comparados con la Normativa Primaria, Escenario Operación Año 9**

| Receptor | MP10 (ug/m3) | Col3 | MP2,5 (ug/m3) | Col5 | NO2 (ug/m3) | Col7 | Col8 | CO (ug/m3) | Col10 | SO2 (ug/m3) Primario | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Receptor | Media Anual | P98 24 hrs | Media Anual | P98 24 hrs | Media Anual | P99 1 hr | P99 1 hr | P99 8 hrs | P99 1 hr | Media Anual | P99 24 hrs | P98,5 1 hr |
| Puerta Bosquemar | 1,53% | 2,30% | 1,32% | 2,41% | 0,15% | 0,22% | 3,58% | 0,01% | 0,00% | 0,01% | 0,00% | 0,00% |
| Colegio Bosquemar | 1,91% | 4,33% | 1,39% | 3,35% | 0,06% | 0,21% | 1,29% | 0,01% | 0,00% | 0,00% | 0,01% | 0,01% |
| Miradores Los Volcanes II | 0,62% | 1,83% | 0,63% | 2,84% | 0,04% | 0,17% | 0,93% | 0,00% | 0,00% | 0,00% | 0,00% | 0,00% |
| Bosquemar II | 0,82% | 2,74% | 0,77% | 3,10% | 0,04% | 0,20% | 1,18% | 0,01% | 0,00% | 0,00% | 0,00% | 0,00% |
| Loteo Bosquemar | 1,71% | 2,82% | 1,22% | 2,30% | 0,10% | 0,18% | 1,37% | 0,01% | 0,00% | 0,00% | 0,00% | 0,00% |
| Parque Costanera I | 1,03% | 1,57% | 0,71% | 1,17% | 0,09% | 0,18% | 1,46% | 0,00% | 0,00% | 0,00% | 0,00% | 0,00% |
| Parque Costanera III | 1,42% | 1,96% | 0,91% | 1,37% | 0,11% | 0,17% | 1,64% | 0,00% | 0,00% | 0,00% | 0,00% | 0,00% |
| Altos Tenglo III | 1,10% | 1,81% | 0,69% | 1,16% | 0,10% | 0,18% | 1,27% | 0,01% | 0,00% | 0,00% | 0,00% | 0,00% |
| Villa Juan XXIII | 1,18% | 2,08% | 0,74% | 1,35% | 0,09% | 0,25% | 1,88% | 0,01% | 0,00% | 0,00% | 0,00% | 0,00% |
| Brisamar | 1,14% | 1,78% | 0,73% | 1,20% | 0,10% | 0,19% | 1,18% | 0,00% | 0,00% | 0,00% | 0,00% | 0,00% |
| Los Albatros | 0,93% | 1,45% | 0,58% | 0,94% | 0,09% | 0,16% | 0,96% | 0,00% | 0,00% | 0,00% | 0,00% | 0,00% |
| Conjunto Los Lagos | 0,93% | 1,56% | 0,58% | 1,00% | 0,09% | 0,15% | 2,24% | 0,00% | 0,00% | 0,00% | 0,00% | 0,00% |
| Escuela Padre Alberto Hurtado | 0,84% | 1,42% | 0,52% | 0,90% | 0,07% | 0,13% | 1,37% | 0,00% | 0,00% | 0,00% | 0,00% | 0,00% |
| Población Juan Pablo II | 0,92% | 1,47% | 0,57% | 0,94% | 0,06% | 0,12% | 0,88% | 0,00% | 0,00% | 0,00% | 0,00% | 0,00% |
| Conjunto Habitacional Viento Sur | 0,59% | 1,06% | 0,37% | 0,70% | 0,07% | 0,12% | 1,62% | 0,00% | 0,00% | 0,00% | 0,00% | 0,00% |
| Población Vicuña Mackenna | 0,68% | 1,22% | 0,42% | 0,79% | 0,05% | 0,10% | 2,39% | 0,00% | 0,00% | 0,00% | 0,00% | 0,00% |
| Lomas de Cardonal | 0,73% | 1,36% | 0,45% | 0,86% | 0,05% | 0,10% | 3,05% | 0,00% | 0,00% | 0,00% | 0,00% | 0,00% |
| Alto Mackenna | 0,60% | 1,18% | 0,37% | 0,75% | 0,04% | 0,09% | 2,37% | 0,00% | 0,00% | 0,00% | 0,00% | 0,00% |
| Est Mirasol | 0,17% | 0,34% | 0,11% | 0,22% | 0,02% | 0,07% | 0,37% | 0,00% | 0,00% | 0,00% | 0,00% | 0,00% |
| Est Alerce | 0,00% | 0,00% | 0,00% | 0,00% | 0,00% | 0,00% | 0,01% | 0,00% | 0,00% | 0,00% | 0,00% | 0,00% |
| Est Puerto Varas | 0,00% | 0,01% | 0,00% | 0,01% | 0,00% | 0,00% | 0,01% | 0,00% | 0,00% | 0,00% | 0,00% | 0,00% |
| Villa Clotario Blest | 0,54% | 0,98% | 0,34% | 0,62% | 0,07% | 0,12% | 1,13% | 0,00% | 0,00% | 0,00% | 0,00% | 0,00% |
| Villa Los Poetas | 0,44% | 0,94% | 0,27% | 0,60% | 0,04% | 0,10% | 0,79% | 0,00% | 0,00% | 0,00% | 0,00% | 0,00% |

**Tabla 17: Análisis de Impacto Significativo MP2,5 μg/m3, Escenario Construcción más Operación del año 7**

| Col1 | Media Anual | Incremento<br>Concentración | % | P98 24H | Incremento<br>Concentración | % |
| --- | --- | --- | --- | --- | --- | --- |
| Puerta Bosquemar | 0,26 | 0,33 | 0,78 | 1,25 | 1,71 | 0,73 |
| Colegio Bosquemar | 0,26 | 0,33 | 0,79 | 1,55 | 1,71 | 0,91 |
| Miradores Los Volcanes II | 0,14 | 0,33 | 0,42 | 1,44 | 1,71 | 0,84 |
| Bosquemar II | 0,16 | 0,33 | 0,48 | 1,68 | 1,71 | 0,98 |
| Loteo Bosquemar | 0,22 | 0,33 | 0,68 | 1,02 | 1,71 | 0,60 |
| Parque Costanera I | 0,13 | 0,33 | 0,39 | 0,58 | 1,71 | 0,34 |
| Parque Costanera III | 0,16 | 0,33 | 0,47 | 0,60 | 1,71 | 0,35 |
| Altos Tenglo III | 0,12 | 0,33 | 0,35 | 0,51 | 1,71 | 0,30 |
| Villa Juan XXIII | 0,12 | 0,33 | 0,38 | 0,57 | 1,71 | 0,33 |
| Brisamar | 0,13 | 0,33 | 0,38 | 0,51 | 1,71 | 0,30 |
| Los Albatros | 0,10 | 0,33 | 0,30 | 0,40 | 1,71 | 0,23 |
| Conjunto Los Lagos | 0,10 | 0,33 | 0,30 | 0,42 | 1,71 | 0,25 |
| Escuela Padre Alberto Hurtado | 0,09 | 0,33 | 0,27 | 0,40 | 1,71 | 0,23 |
| Población Juan Pablo II | 0,10 | 0,33 | 0,29 | 0,40 | 1,71 | 0,23 |
| Conjunto Habitacional Viento<br>Sur | 0,06 | 0,33 | 0,19 | 0,30 | 1,71 | 0,18 |
| Población Vicuña Mackenna | 0,07 | 0,33 | 0,22 | 0,34 | 1,71 | 0,20 |
| Lomas de Cardonal | 0,08 | 0,33 | 0,23 | 0,36 | 1,71 | 0,21 |
| Alto Mackenna | 0,06 | 0,33 | 0,19 | 0,31 | 1,71 | 0,18 |
| Est Mirasol | 0,02 | 0,33 | 0,06 | 0,09 | 1,71 | 0,05 |
| Est Alerce | 0,00 | 0,33 | 0,00 | 0,00 | 1,71 | 0,00 |
| Est Puerto Varas | 0,00 | 0,33 | 0,00 | 0,00 | 1,71 | 0,00 |
| Villa Clotario Blest | 0,06 | 0,33 | 0,17 | 0,27 | 1,71 | 0,16 |
| Villa Los Poetas | 0,05 | 0,33 | 0,14 | 0,25 | 1,71 | 0,15 |
| Población Bernardo OHiggins | 0,05 | 0,33 | 0,14 | 0,22 | 1,71 | 0,13 |
| Terrazas de Angelmó | 0,02 | 0,33 | 0,07 | 0,12 | 1,71 | 0,07 |
| Villa San Antonio | 0,04 | 0,33 | 0,13 | 0,22 | 1,71 | 0,13 |
| Barrio Vicente Pérez Rosales | 0,00 | 0,33 | 0,01 | 0,03 | 1,71 | 0,01 |
| Villa Vicente Pérez Rosales | 0,00 | 0,33 | 0,01 | 0,03 | 1,71 | 0,02 |
| III-IV | 0,06 | 0,33 | 0,18 | 0,59 | 1,71 | 0,35 |
| Bosquemar IX | 0,04 | 0,33 | 0,11 | 0,38 | 1,71 | 0,22 |
| Llanos de Tenglo | 0,01 | 0,33 | 0,02 | 0,11 | 1,71 | 0,07 |
| Puerta Sur | 0,01 | 0,33 | 0,03 | 0,06 | 1,71 | 0,04 |

**Tabla 18: Análisis de Impacto Significativo MP2,5 μg/m3, Escenario Operación del año 9**

| Receptor | Media Anual | Incremento<br>Concentración | % | P98 24H | Incremento<br>Concentración | % |
| --- | --- | --- | --- | --- | --- | --- |
| Puerta Bosquemar | 0,26 | 0,33 | 80,00% | 1,21 | 1,71 | 70,47% |
| Colegio Bosquemar | 0,28 | 0,33 | 84,27% | 1,68 | 1,71 | 97,96% |
| Miradores Los Volcanes II | 0,13 | 0,33 | 38,08% | 1,42 | 1,71 | 82,99% |
| Bosquemar II | 0,15 | 0,33 | 46,37% | 1,55 | 1,71 | 90,77% |
| Loteo Bosquemar | 0,24 | 0,33 | 73,87% | 1,15 | 1,71 | 67,31% |
| Parque Costanera I | 0,14 | 0,33 | 43,00% | 0,58 | 1,71 | 34,13% |
| Parque Costanera III | 0,18 | 0,33 | 54,90% | 0,68 | 1,71 | 40,03% |
| Altos Tenglo III | 0,14 | 0,33 | 41,64% | 0,58 | 1,71 | 34,04% |
| Villa Juan XXIII | 0,15 | 0,33 | 44,69% | 0,67 | 1,71 | 39,46% |
| Brisamar | 0,15 | 0,33 | 44,34% | 0,60 | 1,71 | 35,02% |
| Los Albatros | 0,12 | 0,33 | 35,35% | 0,47 | 1,71 | 27,35% |
| Conjunto Los Lagos | 0,12 | 0,33 | 35,21% | 0,50 | 1,71 | 29,26% |
| Escuela Padre Alberto Hurtado | 0,10 | 0,33 | 31,44% | 0,45 | 1,71 | 26,31% |
| Población Juan Pablo II | 0,11 | 0,33 | 34,65% | 0,47 | 1,71 | 27,39% |
| Conjunto Habitacional Viento<br>Sur | 0,07 | 0,33 | 22,31% | 0,35 | 1,71 | 20,59% |
| Población Vicuña Mackenna | 0,08 | 0,33 | 25,55% | 0,40 | 1,71 | 23,14% |
| Lomas de Cardonal | 0,09 | 0,33 | 27,15% | 0,43 | 1,71 | 25,08% |
| Alto Mackenna | 0,07 | 0,33 | 22,49% | 0,37 | 1,71 | 21,88% |
| Est Mirasol | 0,02 | 0,33 | 6,56% | 0,11 | 1,71 | 6,45% |
| Est Alerce | 0,00 | 0,33 | 0,07% | 0,00 | 1,71 | 0,13% |
| Est Puerto Varas | 0,00 | 0,33 | 0,13% | 0,00 | 1,71 | 0,18% |
| Villa Clotario Blest | 0,07 | 0,33 | 20,47% | 0,31 | 1,71 | 18,14% |
| Villa Los Poetas | 0,05 | 0,33 | 16,31% | 0,30 | 1,71 | 17,52% |
| Población Bernardo OHiggins | 0,05 | 0,33 | 16,38% | 0,26 | 1,71 | 15,19% |
| Terrazas de Angelmó | 0,03 | 0,33 | 8,81% | 0,14 | 1,71 | 8,38% |
| Villa San Antonio | 0,05 | 0,33 | 15,63% | 0,27 | 1,71 | 15,53% |
| Barrio Vicente Pérez Rosales | 0,00 | 0,33 | 1,26% | 0,03 | 1,71 | 1,59% |
| Villa Vicente Pérez Rosales | 0,01 | 0,33 | 1,67% | 0,04 | 1,71 | 2,08% |
| III-IV | 0,04 | 0,33 | 11,58% | 0,35 | 1,71 | 20,45% |
| Bosquemar IX | 0,03 | 0,33 | 9,17% | 0,35 | 1,71 | 20,61% |
| Llanos de Tenglo | 0,01 | 0,33 | 1,97% | 0,10 | 1,71 | 5,71% |
| Puerta Sur | 0,01 | 0,33 | 3,67% | 0,07 | 1,71 | 4,06% |

**Tabla 19: Punto Máximo Impacto, Escenario Construcción más Operación del año 7**

| Contaminante | Estadístico | PMI | Limite<br>Normativo (LN) | PMI/LN | Ubicación UTM-WGS-84-huso-19S | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Contaminante | Estadístico | PMI | Limite<br>Normativo (LN) | PMI/LN | Este (m) | Norte (m) |
| MP10 ug/m3 | Media | 1,37 | 50 | 2,74% | 667478 | 5405743 |
| MP10 ug/m3 | P98 | 5,13 | 130 | 3,95% | 667478 | 5405743 |
| M2,5 ug/m3 | Media | 0,35 | 20 | 1,73% | 667478 | 5405743 |
| M2,5 ug/m3 | P98 | 1,26 | 50 | 2,52% | 667478 | 5405743 |
| NO2 ug/m3 | Media | 0,09 | 40 | 0,24% | 667456 | 5404744 |
| NO2 ug/m3 | P99 24H | 1,02 | 100 | 1,02% | 667456 | 5404744 |
| NO2 ug/m3 | P99 1H | 18,79 | 200 | 9,40% | 666453 | 5404767 |
| CO ug/m3 | P99 1H | 15,92 | 30.000 | 0,05% | 666453 | 5404767 |
| CO ug/m3 | P99 8H | 2,27 | 10.000 | 0,02% | 666453 | 5404767 |
| SO2 ug/m3<br>Primaria | Media | 0,00 | 60 | 0,00% | 667456 | 5404744 |
| SO2 ug/m3<br>Primaria | p99 24h | 0,01 | 150 | 0,01% | 667456 | 5404744 |
| SO2 ug/m3<br>Primaria | p99 1H | 0,03 | 350 | 0,01% | 667456 | 5404744 |

**Tabla 20: Punto Máximo Impacto, Escenario Operación del año 9**

| Contaminante | Estadístico | PMI | Limite<br>Normativo (LN) | PMI/LN | Ubicación UTM-WGS-84-huso-19S | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Contaminante | Estadístico | PMI | Limite<br>Normativo (LN) | PMI/LN | Este (m) | Norte (m) |
| MP10 ug/m3 | Media | 1,61 | 50 | 3,23% | 667.478 | 5.405.743 |
| MP10 ug/m3 | P98 | 6,19 | 130 | 4,76% | 667.478 | 5.405.743 |
| M2,5 ug/m3 | Media | 0,41 | 20 | 2,03% | 667.478 | 5.405.743 |
| M2,5 ug/m3 | P98 | 1,52 | 50 | 3,04% | 667.478 | 5.405.743 |
| NO2 ug/m3 | Media | 0,05 | 40 | 0,12% | 667.478 | 5.405.743 |
| NO2 ug/m3 | P99 24H | 0,28 | 100 | 0,28% | 667.456 | 5.404.744 |
| NO2 ug/m3 | P99 1H | 4,99 | 200 | 2,50% | 667.478 | 5.405.743 |
| CO ug/m3 | P99 1H | 3,50 | 30.000 | 0,01% | 667.478 | 5.405.743 |
| CO ug/m3 | P99 8H | 0,62 | 10.000 | 0,01% | 667.478 | 5.405.743 |
| SO2 ug/m3<br>Primaria | Media | 0,00 | 60 | 0,00% | 667.478 | 5.405.743 |
| SO2 ug/m3<br>Primaria | p99 24h | 0,01 | 150 | 0,01% | 667.478 | 5.405.743 |
| SO2 ug/m3<br>Primaria | p99 1H | 0,03 | 350 | 0,01% | 667.478 | 5.405.743 |
