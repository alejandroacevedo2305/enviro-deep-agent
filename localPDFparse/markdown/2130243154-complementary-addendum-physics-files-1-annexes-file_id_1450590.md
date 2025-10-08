---
title: Cover Page
author: Cristián Palma/Chile/GHD/AU
date: D:20151216121242-03'00'
language: es
type: report
pages: 47
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Declaración de Impacto Ambiental Planta Desaladora Tocopilla
  - Índice
-->

### Aguas de Antofagasta S.A.

## ADENDA N° 1

# Declaración de Impacto Ambiental Planta Desaladora Tocopilla

## Anexo P - Modelación de material particulado sedimentable

#### Preparada por Diciembre de 2015

# Índice

1 Introducción 1

2 Objetivos 2

2.1 General 2

2.2 Específicos 2

3 Antecedentes 3

3.1 Descripción del Proyecto 3

3.2 Localización del Proyecto 3

4 Modelación de Calidad del Aire 5

4.1 Descripción y justificación del modelo 5

4.2 Características del dominio de modelación y su entorno 5

4.3 Escenarios de modelación 9

4.4 Datos meteorológicos observados 10

4.5 Presentación de resultados de la modelación meteorológica 17

4.6 Análisis de datos meteorológicos 25

4.7 Presentación de los resultados de la modelación de calidad del aire 34

5 Conclusiones 38

6 Referencias 39

#### Índice de Tablas

Tabla 4-1 Vértices dominio de modelación Calpuff 7

Tabla 4-2 Receptores discretos considerados en la modelación 7

Tabla 4-3 Vértices dominio de modelación WRF 9

Tabla 4-4 Características del dominio de modelación WRF 9

Tabla 4-5 Tasa de emisión de material particulado sedimentable 9

Tabla 4-6 Coordenadas Estación Meteorológica Supersite (Ex Escuela E-10) 10

Tabla 4-7 Índices estadísticos para Velocidad del viento y Temperatura 32

Tabla 4-8 Índices estadísticos para Velocidad del viento y Temperatura por periodo

del día 33

Tabla 4-9 Aporte del Proyecto, MPS (mg/m [2] -día) 36

Tabla 4-10 Aporte del Proyecto en el PMI 37

DIA Planta Desaladora Tocopilla | Adenda N° 1 - Anexo P - Modelación material particulado sedimentable I ii

#### Índice de Figuras

Figura 3-1 Ubicación del Proyecto a escala local 4

Figura 4-1 Dominio de modelación Calpuff 6

Figura 4-2 Localización de los receptores discretos modelación 8

Figura 4-3 Serie de tiempo de Temperatura, Estación Supersite - 2012 11

Figura 4-4 Ciclo diario promedio de Temperatura, Supersite - 2012 11

Figura 4-5 Serie de tiempo de Velocidad del viento, Supersite - 2012 12

Figura 4-6 Ciclo diario promedio de Velocidad del viento, Supersite - 2012 13

Figura 4-7 Serie de tiempo de Dirección del viento, Supersite - 2012 13

Figura 4-8 Ciclo diario de Dirección del viento, Supersite- 2012 14

Figura 4-9 Rosas de viento por periodo del día, Supersite - 2012 15

Figura 4-10 Serie de tiempo de humedad relativa, Supersite - 2012 16

Figura 4-11 Ciclo diario promedio de Humedad relativa, Supersite - 2012 16

Figura 4-12 Serie de tiempo de Velocidad del viento, WRF - 2012 17

Figura 4-13 Serie de tiempo de Dirección del viento, WRF - 2012 17

Figura 4-14 Ciclo diario promedio de Velocidad del viento, WRF - 2012 18

Figura 4-15 Ciclo diario de Dirección del viento, WRF - 2012 18

Figura 4-16 Rosas de viento por periodo del día, WRF - 2012 19

Figura 4-17 Mapa de viento a las 00:00 horas 21

Figura 4-18 Mapa de viento a las 06:00 horas 22

Figura 4-19 Mapa de viento a las 12:00 horas 23

Figura 4-20 Mapa de viento a las 18:00 horas 24

Figura 4-21 Ciclo diario de Velocidad del viento observado y simulado - Año 2012 25

Figura 4-22 Ciclo diario de Dirección del viento observado y simulado - Año 2012 26

Figura 4-23 Rosa de viento observada y simulada - Año 2012 27

Figura 4-24 Rosa de vientos observada y simulada - periodos 00:00 - 05: 00 hrs y

06:00 - 11:00 hrs 28

Figura 4-25 Rosa de vientos observada y simulada - periodos 12:00 - 17: 00 hrs y

18:00 - 23:00 hrs 29

Figura 4-26 Ciclo diario de Temperatura observado y simulado, Año 2012 31

Figura 4-27 Isoconcentraciones Promedio Anual de MPS (Límite Norma 200
mg/m [2] /día) 35

#### Índice de Apéndices

Apéndice P.1 Tasas de emisión ingresadas al modelo CALPUFF

Apéndice P.2 Archivos de modelación Calpuff

DIA Planta Desaladora Tocopilla | Adenda N° 1 - Anexo P - Modelación material particulado sedimentable I iii

### 1 Introducción

El presente informe ha sido elaborado con la finalidad de evaluar las concentraciones ambientales de
material particulado sedimentable (MPS) en los receptores sensibles identificados para el Proyecto
**Planta Desaladora Tocopilla**, ubicado en la comuna Tocopilla, Provincia de Tocopilla, Región de
Antofagasta.

El Proyecto consiste en la construcción y operación de una planta desaladora de agua de mar, diseñada
para producir 200 l/s de agua potable, sobre la base de la desalación por osmosis inversa. Para ello, el
agua de mar será captada por cuatro torres de captación ubicadas a 650 m de la costa, en el lado norte
de la ciudad de Tocopilla, a una profundidad de 29 m, para luego ser transportada por una tubería de
captación de 650 m de longitud y 1,2 m de diámetro, hasta una cámara de succión ubicada dentro de la
planta elevadora de agua de mar. Desde aquí, el agua de mar será impulsada hasta el edificio de
procesos de la Planta Desaladora, a través de una tubería de impulsión 220 m de longitud y 0,5 m de
diámetro, donde mediante un proceso de osmosis inversa se producirá agua potable, con una eficiencia
entre 45% y 50% respecto del agua captada del mar.

La modelación de la dispersión de material particulado sedimentable, fue realizada a través del modelo
de dispersión de contaminantes recomendado por la U.S. EPA, CALPUFF View V.6.42, ajustándose a los
lineamientos propuestos en la “Guía para el uso de Modelos de Calidad del Aire en el SEIA” que
incorpora la meteorología de pronóstico mediante modelación numérica Weather Research and
Forecasting Model (WRF).

Finalmente, se presentan las figuras de isoconcentraciones y las tablas de impacto que provienen del
modelo desarrollado bajo plataforma CALPUFF View.

DIA Planta Desaladora Tocopilla | Adenda N° 1 - Anexo P - Modelación material particulado sedimentable I 1

### 2 Objetivos

2.1 General

Evaluar las concentraciones ambientales de material particulado sedimentable (MPS) en los receptores
sensibles identificados para el Proyecto **Planta Desaladora Tocopilla**, producto de las emisiones
atmosféricas generadas durante su fase de construcción.

2.2 Específicos

- Modelar la dispersión atmosférica de las emisiones de MPS generadas durante la fase de
construcción del Proyecto mediante el modelo CALPUFF View, incorporando como dato de entrada,
la meteorología de pronóstico desarrollada a partir del modelo numérico Weather Research and
Forecasting Model (WRF), proporcionado por la División Evaluación Ambiental y Participación

Ciudadana del SEA.

- Comparar las concentraciones de MPS registradas en los receptores sensibles identificados, con el
nivel máximo establecido en la normativa de referencia para el contaminante.

- Analizar la incertidumbre del modelo de dispersión utilizado, a partir de la comparación de la
meteorología de pronóstico WRF y la meteorología local observada, con el fin de evaluar su
capacidad de representar la dispersión atmosférica de los contaminantes.

DIA Planta Desaladora Tocopilla | Adenda N° 1 - Anexo P - Modelación material particulado sedimentable I 2

### 3 Antecedentes

3.1 Descripción del Proyecto

El Proyecto consiste en la construcción y operación de una planta desaladora de agua de mar, diseñada
para producir 200 l/s de agua potable, sobre la base de la desalación por osmosis inversa. Para ello, el
agua de mar será captada por cuatro torres de captación ubicadas a 650 m de la costa, en el lado norte
de la ciudad de Tocopilla, a una profundidad de 29 m, para luego ser transportada por una tubería de
captación de 650 m de longitud y 1,2 m de diámetro, hasta una cámara de succión ubicada dentro de la
planta elevadora de agua de mar. Desde aquí, el agua de mar será impulsada hasta el edificio de
procesos de la Planta Desaladora, a través de una tubería de impulsión 220 m de longitud y 0,5 m de
diámetro, donde mediante un proceso de osmosis inversa se producirá agua potable, con una eficiencia
entre 45% y 50% respecto del agua captada del mar.

Posteriormente, el agua de rechazo o salmuera proveniente del proceso de osmosis inversa, será
descargada al mar en forma gravitacional por medio de una tubería de 240 m de longitud y 0,63 m de
diámetro, que se une a un emisario submarino, de aproximadamente 225 m de longitud y 0,63 m de

diámetro.

Finalmente, el agua potable será impulsada desde el edificio de procesos, a través de una tubería de 3,25
km de longitud y 0,5 m de diámetro, cuyo trazado pasará por parte de las calles 3 Marías; Orella; Isabel
Riquelme y Miraflores y Ruta 1, hasta llegar al recinto estanque Esmeralda existente, para luego ser
distribuida a través del actual sistema de distribución de Aguas de Antofagasta S.A. en la ciudad de
Tocopilla.

La fase de construcción del Proyecto tendrá una duración de 24 meses, mientras que la fase de
operación tendrá una duración estimada de 20 años.

3.2 Localización del Proyecto

Administrativamente, el Proyecto se localiza en la Región de Antofagasta, provincia de Tocopilla, Comuna
de Tocopilla.

En la siguiente Figura 3-1 se visualiza la ubicación de las principales obras del Proyecto, a escala local.

DIA Planta Desaladora Tocopilla | Adenda N° 1 - Anexo P - Modelación material particulado sedimentable I 3

Figura 3-1 Ubicación del Proyecto a escala local

Fuente: Elaboración propia.

DIA Planta Desaladora Tocopilla | Adenda N° 1 - Anexo P - Modelación material particulado sedimentable I 4

### 4 Modelación de Calidad del Aire

4.1 Descripción y justificación del modelo

Para determinar las concentraciones de MPS en los receptores sensibles identificados, producto de las
emisiones asociadas al escenario de mayor emisión, se utilizó el software de modelación atmosférica
CALPUFF View V. 6.0, recomendado por la Agencia de Protección Ambiental de los Estados Unidos (USEPA) y la Guía para el Uso de Modelos de Calidad del Aire en el SEIA; en conjunto con la meteorología
de pronóstico obtenida mediante modelación numérica “Weather Research and Forecasting Model
(WRF)”.

El sistema de modelación CALPUFF incluye tres componentes principales: WRF, CALPUFF y CALPOST,
además de una amplia selección de preprocesadores diseñados para incluir en el modelo datos
meteorológicos y geofísicos. Cada uno de estos componentes se describe brevemente a continuación:

- CALPUFF es un modelo no estacionario, de dispersión de _puffs_, que es capaz de simular la
distribución espacial de varios contaminantes en forma simultánea, a medida que son transportados,
modificados por reacciones químicas y depositadas en la superficie. Las salidas de CALPUFF
consisten en concentraciones en cada punto receptor o en formato de grilla, para cada hora de

modelación.

- WRF corresponde al modelo meteorológico de pronóstico más avanzado y completo mantenido por
NCAR [1] /NOAA [2] de Estados Unidos, capaz de simular campos de viento y temperatura en un dominio
de modelación engrillado y tridimensional. Dichos campos de vientos permiten determinar
posteriormente la dispersión de los contaminantes, a través de la aplicación del modelo CALPUFF.

El modelo WRF, integra las variables relativas a uso de suelo, topografía, albedo, rugosidad, entre
otras, con fuente de información provista por el Land Cover Institute del U.S. Geological Survey
(USGS) en EE.UU.

- CALPOST es una herramienta que permite obtener promedios móviles, máximos impactos,
percentiles, tabla de máximos impactos, estimaciones de visibilidad, etc., a partir de las series de
tiempos de concentraciones generadas por CALPUFF.

4.2 Características del dominio de modelación y su entorno

La extensión del área de modelación para MPS, se definió en función de los receptores sensibles, la
magnitud del Proyecto y las emisiones generadas. Este dominio comprendió una grilla de dimensión
vertical de 8 km por 7 km de dimensión horizontal, y está definida por celdas de 1 km por 1 km, tal como
se observa en la Figura 4-1.

1 National Center for Atmospheric Research

2 National Oceanic and Atmospheric Administration

DIA Planta Desaladora Tocopilla | Adenda N° 1 - Anexo P - Modelación material particulado sedimentable I 5

Figura 4-1 Dominio de modelación Calpuff

Fuente: Elaboración propia.

DIA Planta Desaladora Tocopilla | Adenda N° 1 - Anexo P - Modelación material particulado sedimentable I 6

Las coordenadas de los vértices de área de modelación Calpuff se presentan en la siguiente Tabla 4-1.

<!-- INICIO TABLA 4-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- DIA Planta Desaladora Tocopilla | Adenda N° 1 - Anexo P - Modelación material particulado sedimentable I 6 Las coordenadas de los vértices de área de modelación Calpuff se presentan en la siguiente Tabla 4-1. -->

**Tabla 4-1: Vértices dominio de modelación Calpuff**

| Vértice | Coordenadas UTM WGS 84 H 19S | Col3 |
| --- | --- | --- |
| **Vértice** | **Este [m]** | **Norte [m]** |
| V1 | 373.277 | 7.561.594 |
| V2 | 380.288 | 7.561.638 |
| V3 | 380.338 | 7.553.672 |
| V4 | 373.328 | 7.553.628 |

<!-- Estadísticas: 5 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. En relación a los receptores discretos considerados en la modelación, éstos correspondieron a las estaciones de calidad del aire presentes en la ciudad, y aquellas viviendas representativas del sector por -->
<!-- FIN TABLA 4-1 -->


Tabla 4-1 Vértices dominio de modelación Calpuff

|Vértice|Coordenadas UTM WGS 84 H 19S|Col3|
|---|---|---|
|**Vértice**|**Este [m]**|**Norte [m]**|
|V1|373.277|7.561.594|
|V2|380.288|7.561.638|
|V3|380.338|7.553.672|
|V4|373.328|7.553.628|

Fuente: Elaboración propia.

En relación a los receptores discretos considerados en la modelación, éstos correspondieron a las
estaciones de calidad del aire presentes en la ciudad, y aquellas viviendas representativas del sector por
dónde pasará la tubería de agua potable del proyecto. La Tabla 4-2 indica las coordenadas de los
receptores, mientras que la Figura 4-2 presenta su ubicación espacial.

Tabla 4-2 Receptores discretos considerados en la modelación

|Receptor|Coordenadas UTM WGS 84 H 19S|Col3|
|---|---|---|
|**Receptor**|**Este [m]**|**Norte [m]**|
|Estación Gendarmería|377.833|7.559.990|
|Estación Supersite (Ex Escuela E-10)|377.352|7.557.219|
|Estación Gobernación|376.374|7.556.617|
|Estación Bomberos|375.319|7.554.741|
|Población Tres Marías|377.653|7.559.935|
|Vivienda 1 calle Orella|376.914|7.557.920|
|Vivienda 2 calle Orella|377.024|7.557.795|
|Vivienda 3 calle Orella|377.135|7.557.670|
|Vivienda 4 calle Isabel Riquelme|377.236|7.557.681|
|Vivienda 5 calle Miraflores|377.400|7.557.728|
|Vivienda 6 calle Miraflores|377.571|7.557.533|
|Vivienda 7 calle Miraflores|377.742|7.557.338|

Fuente: Elaboración propia.

DIA Planta Desaladora Tocopilla | Adenda N° 1 - Anexo P - Modelación material particulado sedimentable I 7

Figura 4-2 Localización de los receptores discretos modelación

Fuente: Elaboración propia.

DIA Planta Desaladora Tocopilla | Adenda N° 1 - Anexo P - Modelación material particulado sedimentable I 8

La grilla de modelación meteorológica WRF utilizada, correspondió a un área de resolución 62 km por 62
km, de tamaño de celda 1 km x 1 km. En la siguiente Tabla 4-3 se presentan las coordenadas de sus
vértices y en Tabla 4-3 sus principales características.

Tabla 4-3 Vértices dominio de modelación WRF

|Vértice|Coordenadas UTM WGS 84 H 19S|Col3|
|---|---|---|
|**Vértice**|**Este [m]**|**Norte [m]**|
|V1|369.096|7.589.449|
|V2|431.185|7.589.838|
|V3|431.577|7.528.109|
|V4|369.487|7.527.711|

Fuente: Elaboración propia.

Tabla 4-4 Características del dominio de modelación WRF

**Características del dominio de modelación WRF**

|Período modelado|1 de enero de 2012 00:00 al 31 de diciembre de 2012 23:00|
|---|---|
|Latitud del centro del dominio|22.073 S|
|Longitud del centro del dominio|69.966 W|
|Datum|NWS-84|
|Resolución|1 km|
|Tamaño del dominio|62 km x 62 km|
|Zona Horaria|UTC/GMT UTC - 4 horas|

Fuente: Servicio de Evaluación Ambiental. 2012.

4.3 Escenarios de modelación

El escenario de modelación considerado en la presente evaluación corresponde al de mayor emisión para
el Proyecto; el cual según lo presentado en la Tabla 4-5 corresponde al de construcción para el primer

año.

Cabe señalar que, la modelación consideró un desarrollo simultáneo de las actividades constructivas,
configurando de esta forma un escenario conservador.

Tabla 4-5 Tasa de emisión de material particulado sedimentable

|Actividad emisora|Emisiones<br>construcción [ton/año]|Col3|Emisiones<br>operación [ton/año]|Emisiones cierre<br>[ton/año]|
|---|---|---|---|---|
|**Actividad emisora**|**Año 1**|**Año 2**|**Año 2**|**Año 2**|
|Escarpe|---|---|---|---|
|Excavaciones|2,69|---|---|---|
|Compactación|0,15|---|---|---|
|Carga y descarga de material|0,04|---|---|---|
|Circulación vehículos livianos caminos|0,30|---|---|---|

DIA Planta Desaladora Tocopilla | Adenda N° 1 - Anexo P - Modelación material particulado sedimentable I 9

|Actividad emisora|Emisiones<br>construcción [ton/año]|Col3|Emisiones<br>operación [ton/año]|Emisiones cierre<br>[ton/año]|
|---|---|---|---|---|
|**Actividad emisora**|**Año 1**|**Año 2**|**Año 2**|**Año 2**|
|no pavimentados|||||
|Circulación vehículos pesados caminos<br>no pavimentados|1,26|---|---|---|
|Circulación vehículos caminos<br>pavimentados|1,17|0,90|0,04|0,74|
|Gases combustión vehículos|---|---|---|---|
|Gases combustión maquinaria|---|---|---|---|
|Gases combustión generadores|---|---|---|---|
|**Total [ton/año]**|**5,62**|**0,90**|**0,04**|**0,74**|

Fuente: elaboración propia.

Las tasas de emisión ingresadas al modelo CALPUFF, así como el tipo de fuente considerada se
presentan en el Apéndice P.1, del presente documento.

4.4 Datos meteorológicos observados

Los datos meteorológicos observados utilizados para evaluar el resultado del modelo de pronóstico,
corresponden a los registrados en el año 2012 por la Estación de Monitoreo Supersite (Ex Escuela E-10),
perteneciente a la red de monitoreo de E-CL S.A. (Ex Electroandina), la cual se ubica según lo indicado
en Figura 4-2 y en Tabla 4-6.

<!-- INICIO TABLA 4-6 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Los datos meteorológicos observados utilizados para evaluar el resultado del modelo de pronóstico, corresponden a los registrados en el año 2012 por la Estación de Monitoreo Supersite (Ex Escuela E-10), perteneciente a la red de monitoreo de E-CL S.A. (Ex Electroandina), la cual se ubica según lo indicado en Figura 4-2 y en Tabla 4-6. -->

**Tabla 4-6: Coordenadas Estación Meteorológica Supersite (Ex Escuela E-10)**

| Estación | Coordenadas UTM WGS 84 H 19S | Col3 |
| --- | --- | --- |
| **Estación** | **Este [m]** | **Norte [m]** |
| Supersite | 377.352 | 7.557.219 |

<!-- Estadísticas: 2 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. A continuación se presenta el análisis de los datos meteorológicos observados para temperatura, velocidad y dirección del viento, y humedad relativa, incluyendo series de tiempo, ciclos diarios y -->
<!-- FIN TABLA 4-6 -->


Tabla 4-6 Coordenadas Estación Meteorológica Supersite (Ex Escuela E-10)

|Estación|Coordenadas UTM WGS 84 H 19S|Col3|
|---|---|---|
|**Estación**|**Este [m]**|**Norte [m]**|
|Supersite|377.352|7.557.219|

Fuente: Elaboración propia.

A continuación se presenta el análisis de los datos meteorológicos observados para temperatura,
velocidad y dirección del viento, y humedad relativa, incluyendo series de tiempo, ciclos diarios y

estacionales, rosas de viento, etc.

4.4.1 Temperatura

4.4.1.1 Serie de tiempo

La Figura 4-3 presenta la serie de tiempo horaria de temperatura registradas durante el año 2012 en la
Estación Supersite. De acuerdo a la distribución de los datos presentados, se observa que durante todo
el periodo se presenta una continuidad de información, siendo el porcentaje de registros válidos 95% del
total de registros para un año completo (8.784 registros).

De acuerdo a la distribución de los datos presentados se observa un descenso de la temperatura en el
mes de junio, para luego ascender durante el mes de septiembre. Los máximos valores registrados se

DIA Planta Desaladora Tocopilla | Adenda N° 1 - Anexo P - Modelación material particulado sedimentable I 10

alcanzan durante los meses de diciembre y febrero, mientras que en el mes de julio se registran las
mínimas temperaturas. La temperatura promedio anual alcanza los 18,06 °C.

Figura 4-3 Serie de tiempo de Temperatura, Estación Supersite - 2012

Fuente: elaboración propia.

4.4.1.2 Ciclo diario

El ciclo diario de temperatura promedio para el periodo 2012 se muestra en la Figura 4-4,
específicamente en la línea de color azul. Adicionalmente se presentan los límites superiores e inferiores
los percentiles 95 y 5, respectivamente.

Se observa una escasa variación de temperatura promedio inter-horaria, obteniéndose una diferencia
entre mínimas y máximas de 4° C. Las máximas temperaturas se presentan entre las 08:00 y 18:00
horas, mientras que las mínimas se presentan entre las 22:00 y 06:00 horas.

Figura 4-4 Ciclo diario promedio de Temperatura, Supersite - 2012

Fuente: elaboración propia.

DIA Planta Desaladora Tocopilla | Adenda N° 1 - Anexo P - Modelación material particulado sedimentable I 11

4.4.2 Velocidad del viento

4.4.2.1 Series de tiempo

La Figura 4-5 presenta la serie de tiempo horaria de velocidad del viento registrada en la Estación
Escuela E-10, durante los meses de enero a diciembre del año 2012. Se identifica una amplia densidad
de información, obteniéndose un porcentaje de registros válidos para el periodo del 95%.

Se observan en general bajas velocidades del viento, alcanzándose durante el año un promedio de 1,97
m/s. Las mayores velocidades de viento se presentan durante las temporadas de primavera y verano,
mientras que las menores se registran en otoño específicamente entre los meses de mayo a julio.

Figura 4-5 Serie de tiempo de Velocidad del viento, Supersite - 2012

Fuente: elaboración propia.

Cabe señalar que la distribución de los datos no da cuenta de eventos significativos de errores de
calibración y/o inconsistencia física del equipo de medición utilizado.

4.4.2.2 Ciclo diario

La Figura 4-6 presenta el ciclo diario promedio de velocidad del viento para el periodo en estudio. Se
observa que las menores velocidades se presentan entre la 23:00 y 03:00 horas con valores que no
superan 1 m/s. Por su parte las máximas velocidades se presentan entre las 13:00 y las 18:00 horas con
registros por sobre 3 m/s.

DIA Planta Desaladora Tocopilla | Adenda N° 1 - Anexo P - Modelación material particulado sedimentable I 12

Figura 4-6 Ciclo diario promedio de Velocidad del viento, Supersite - 2012

Fuente: elaboración propia

4.4.3 Dirección del viento

4.4.3.1 Serie de tiempo

La Figura 4-7 presenta la serie de tiempo horaria de dirección del viento registrada en la Supersite
durante el año 2012. De acuerdo a la distribución de los datos presentados se observa una amplia
densidad de información obteniéndose un 95% de registros válidos para el periodo.

Se observa una tendencia de concentración de registros en el rango observado de 250 a 300°, es decir
vientos provenientes principalmente de direcciones SW, WSW y W. No obstante lo anterior, se destaca la
procedencia de vientos de dirección ENE durante los meses de abril a agosto.

Figura 4-7 Serie de tiempo de Dirección del viento, Supersite - 2012

Fuente: elaboración propia.

Cabe destacar que la distribución de los datos no da cuenta de eventos significativos de errores de
calibración y/o inconsistencia física del equipo de medición utilizado.

DIA Planta Desaladora Tocopilla | Adenda N° 1 - Anexo P - Modelación material particulado sedimentable I 13

4.4.3.2 Ciclo diario

La Figura 4-8 presenta el ciclo diario de dirección del viento para el periodo en estudio para la Estación
Escuela E-10, en donde se observa que durante las primeras horas de la madrugada y de la mañana
(03:00 - 09:00 hrs.), las direcciones predominantes, con un 50% de los datos, corresponden a E y ENE.
Para el ciclo diurno (09:00 - 21:00 hrs.) predominan con un 50% del tiempo, las direcciones SW, WSW y
W principalmente.

Figura 4-8 Ciclo diario de Dirección del viento, Supersite- 2012

Fuente: elaboración propia.

4.4.3.3 Rosas de viento

A partir del análisis de las rosas de viento por periodo del día, presentadas en la Figura 4-9, se observa
que durante el horario 00:00 - 05:00 hrs., no existe una tendencia marcada en términos de procedencia
de los vientos, destacándose las componentes E y ENE con una participación equivalente al 13% en
ambos casos. Se destaca el hecho que durante un 11,01% del tiempo se registran situaciones de calma,
es decir, velocidades de viento por debajo de 0,5 m/s. La velocidad promedio del viento durante este
período alcanza 1,00 m/s, por debajo del promedio diario registrado en 1,94 m/s.

Posteriormente, en el periodo diurno comprendido entre las 06:00 y 11:00 hrs., se observa que los vientos
provienen notoriamente desde tres direcciones correspondientes a ENE; W y WNW, en todos los casos
con un 16% de participación. La velocidad promedio del viento durante este período alcanza 1,75 m/s,
muy similar al promedio diario, registrándose calmas durante un 2,54% del tiempo.

Para el horario comprendido entre las 12:00 y 17:00 hrs., se observa un cambio respecto al periodo
anterior, registrándose vientos cuya procedencia corresponde a E y WSW, con un porcentaje de
participación equivalente al 32% y 37%, respectivamente. Durante este periodo la velocidad del viento
promedio alcanza 3,32 m/s, por sobre el promedio diario registrado en 1,94 m/s. El porcentaje de calmas
corresponde a un 0,44%.

Finalmente, para el periodo entre las 18:00 y las 23:00 hrs., se observa que continúan predominando los
vientos provenientes de dirección WSW, con un 22% de participación y vientos provenientes de dirección
SW con un 24% de participación. Durante este período la velocidad promedio del viento alcanza 1,73
m/s, con un porcentaje de calmas correspondiente a 2,58%.

DIA Planta Desaladora Tocopilla | Adenda N° 1 - Anexo P - Modelación material particulado sedimentable I 14

Figura 4-9 Rosas de viento por periodo del día, Supersite - 2012

|Col1|Col2|
|---|---|
|**Rosa de Viento Periodo 00:00 AM - 05: 00 AM**<br>**Entre 01/01/2012 00:00 hrs. y el 31/12/2012 23:00 hrs. **|**Rosa de Viento Periodo 06:00 AM - 11: 00 AM**<br>**Entre 01/01/2012 00:00 hrs. y el 31/12/2012 23:00 hrs.**|
|||
|**Rosa de Viento Periodo 12:00 PM - 17: 00 PM**<br>**Entre 01/01/2012 00:00 hrs. y el 31/12/2012 23:00 hrs.**|**Rosa de Viento Periodo 18:00 PM - 23: 00 PM**<br>**Entre 01/01/2012 00:00 hrs. y el 31/12/2012 23:00 hrs.**|

Fuente: elaboración propia.

4.4.4 Humedad relativa

4.4.4.1 Serie de tiempo

La Figura 4-10 presenta la serie de tiempo horaria de humedad relativa del aire registrada en la Estación
de Monitoreo Escuela E-10, durante el año 2012. En general, se identifican valores homogéneos de

DIA Planta Desaladora Tocopilla | Adenda N° 1 - Anexo P - Modelación material particulado sedimentable I 15

humedad relativa a lo largo del año; con valores que oscilan entre 45 y 80%. A partir de los datos
observados se establece para el sector una media de 65,78%.

Figura 4-10 Serie de tiempo de humedad relativa, Supersite - 2012

Fuente: elaboración propia.

4.4.4.2 Ciclo diario

La Figura 4-11 presenta el ciclo diario de humedad relativa para el periodo en estudio, en donde se
observa que durante las 11:00 y las 17:00 hrs se registran los menores valores de humedad relativa,

alcanzando su mínimo a las 14:00 hrs. con un 57%.

De la gráfica se desprende que el comportamiento de la humedad relativa tiene directa relación con la
curva que describe la temperatura en la zona en estudio (Figura 4-4), siendo ambas variables
inversamente proporcionales.

Figura 4-11 Ciclo diario promedio de Humedad relativa, Supersite - 2012

Fuente: elaboración propia.

DIA Planta Desaladora Tocopilla | Adenda N° 1 - Anexo P - Modelación material particulado sedimentable I 16

4.5 Presentación de resultados de la modelación meteorológica

4.5.1 Series de tiempo

La Figura 4-12 presenta la serie de tiempo horaria de velocidad del viento proveniente de la modelación
numérica WRF en la Estación Supersite; para el mismo año de análisis de información meteorológica de
superficie (año 2012).

Se observan en general altas velocidades del viento, alcanzándose durante el año un promedio de 3,23
m/s. Las mayores velocidades de viento se presentan durante las temporadas de primavera y verano,
mientras que las menores se registran en otoño específicamente entre los meses de mayo a julio.

Figura 4-12 Serie de tiempo de Velocidad del viento, WRF - 2012

Fuente: elaboración propia.

En el caso de la direcciones de los vientos correspondiente a la línea de concentración superior (entre
200 y 250°) se aprecia una marcada presencia de vientos provenientes del dominio SW y WSW durante

todo el año.

Figura 4-13 Serie de tiempo de Dirección del viento, WRF - 2012

Fuente: elaboración propia.

DIA Planta Desaladora Tocopilla | Adenda N° 1 - Anexo P - Modelación material particulado sedimentable I 17

4.5.2 Ciclos diarios

La Figura 4-14 presenta el ciclo diario promedio de velocidad del viento para el periodo modelado en
estudio. Se observa que las menores velocidades se presentan entre la 00:00 y 07:00 horas con valores
que no superan 1,5 m/s. Por su parte las máximas velocidades se presentan entre las 11:00 y las 18:00
horas con registros por sobre 5 m/s.

Figura 4-14 Ciclo diario promedio de Velocidad del viento, WRF - 2012

|Col1|Promedio|
|---|---|
||Rango 90% Observado|

Fuente: elaboración propia.

La Figura 4-15 presenta el ciclo diario de dirección del viento proveniente del modelo WRF para la
Estación Supersite, en donde es posible observar que no existe una tendencia definida en términos de
procedencia de dirección de vientos durante la madrugada y primeras horas de la mañana (00:00 - 07:00
hrs.). Durante el día en cambio (07:00 - 21:00 hrs.), las direcciones predominantes corresponden a WSW
y SW principalmente, con un 50% de los registros.

Figura 4-15 Ciclo diario de Dirección del viento, WRF - 2012

Fuente: elaboración propia.

DIA Planta Desaladora Tocopilla | Adenda N° 1 - Anexo P - Modelación material particulado sedimentable I 18

4.5.3 Rosas de viento

A partir del análisis de las rosas de viento por periodo del día, presentadas en la Figura 4-16, se observa
que durante el horario 00:00 - 05:00 hrs., existe una tendencia marcada en términos de procedencia de
los vientos, destacándose las componentes E y ENE con una participación equivalente al 13% y 11%,
respectivamente. Se destaca el hecho que durante un 11,14% del tiempo se registran situaciones de
calma, es decir, velocidades de viento por debajo de 0,5 m/s. La velocidad promedio del viento durante
este período alcanza 1,17 m/s, por debajo del promedio diario registrado en 3,21 m/s.

Posteriormente, en el periodo diurno comprendido entre las 06:00 y 11:00 hrs., se observa que los vientos
provienen notoriamente desde direcciones SW y WSW, con un porcentaje de participación equivalente al
35% y 23%, respectivamente. La velocidad promedio del viento durante este período alcanza 3,04 m/s,
muy similar al promedio diario, registrándose calmas durante un 5,39% del tiempo.

Para el horario comprendido entre las 12:00 y 17:00 hrs., se mantiene lo observado respecto al periodo
anterior, registrándose vientos cuya procedencia corresponde a SW y WSW, con un porcentaje de
participación equivalente al 69% y 26%, respectivamente. Durante este periodo la velocidad del viento
promedio alcanza 5,84 m/s, por sobre el promedio diario registrado en 3,21 m/s. No se registran calmas
en este periodo del día.

Finalmente, para el periodo entre las 18:00 y las 23:00 hrs., se observa que continúan predominando los
vientos provenientes de dirección SW, con un 42% de participación y vientos provenientes de dirección
WSW con un 22% de participación. Durante este período la velocidad promedio del viento alcanza 2,79
m/s, con un porcentaje de calmas correspondiente a 6,39%.

Figura 4-16 Rosas de viento por periodo del día, WRF - 2012

|Col1|Col2|
|---|---|
|**Rosa de Viento Periodo 00:00 AM - 05: 00 AM**<br>**Entre 01/01/2012 00:00 hrs. y el 30/12/2012 23:00 hrs. **|**Rosa de Viento Periodo 06:00 AM - 11: 00 AM**<br>**Entre 01/01/2012 00:00 hrs. y el 30/12/2012 23:00 hrs.**|

DIA Planta Desaladora Tocopilla | Adenda N° 1 - Anexo P - Modelación material particulado sedimentable I 19

|Col1|Col2|
|---|---|
|**Rosa de Viento Periodo 12:00 PM - 17: 00 PM**<br>**Entre 01/01/2012 00:00 hrs. y el 30/12/2012 23:00 hrs.**|**Rosa de Viento Periodo 18:00 PM - 23: 00 PM**<br>**Entre 01/01/2012 00:00 hrs. y el 30/12/2012 23:00 hrs.**|

Fuente: elaboración propia.

4.5.4 Mapas de viento

A continuación se presentan los mapas de viento que representan el comportamiento de los vientos para
distintas horas del día para un día típico de invierno a través de vectores de longitud proporcional a la
velocidad del viento que poseen.

DIA Planta Desaladora Tocopilla | Adenda N° 1 - Anexo P - Modelación material particulado sedimentable I 20

Figura 4-17 Mapa de viento a las 00:00 horas

Fuente: elaboración propia.

DIA Planta Desaladora Tocopilla | Adenda N° 1 - Anexo P - Modelación material particulado sedimentable I 21

Figura 4-18 Mapa de viento a las 06:00 horas

Fuente: elaboración propia.

DIA Planta Desaladora Tocopilla | Adenda N° 1 - Anexo P - Modelación material particulado sedimentable I 22

Figura 4-19 Mapa de viento a las 12:00 horas

Fuente: elaboración propia.

DIA Planta Desaladora Tocopilla | Adenda N° 1 - Anexo P - Modelación material particulado sedimentable I 23

Figura 4-20 Mapa de viento a las 18:00 horas

Fuente: elaboración propia.

DIA Planta Desaladora Tocopilla | Adenda N° 1 - Anexo P - Modelación material particulado sedimentable I 24

4.6 Análisis de datos meteorológicos

4.6.1 Comparación entre modelo y observaciones

Como es sabido, todos los modelos tienen asociados errores e incertidumbres, es por ello que es muy
importante evaluar estos errores, comparando los resultados del modelo con las observaciones en forma
cualitativa y cuantitativa.

A continuación se desarrolla la respectiva evaluación cualitativa y cuantitativa del modelo de pronóstico
WRF a partir de la información meteorológica de superficie obtenida de la Estación Supersite (Escuela E10), para el año 2012.

4.6.1.1 Evaluación cualitativa

La evaluación cualitativa, se basa principalmente en la comparación de los ciclos diarios de velocidad y
dirección del viento, para los datos observados y simulados, por ser estas las variables que tienen mayor
incidencia en los procesos de dispersión de contaminantes. Adicionalmente se incluye el análisis del ciclo
diario de la temperatura para ambas situaciones.

- **Velocidad del viento**

La Figura 4-21 presenta el gráfico del ciclo diario de velocidad del viento obtenido a partir de las
mediciones de superficie y modelación meteorológica WRF para la Estación Supersite. Como se puede
observar, el modelo meteorológico tiene un buen comportamiento durante la madrugada y primeras horas
de la mañana (00:00 - 07:00 hrs) con diferencias que no sobrepasan los 0,4 m/s. Avanzando el día el
modelo tiende a sobreestimar la velocidad del viento, específicamente durante el periodo diurno, donde la

máxima diferencia se obtiene a las 12:00 hrs., con un valor cercano a los 3 m/s.

Durante este período la velocidad promedio del viento, - para la situación observada y modelada -,
alcanza 1,97 m/s y 3,23 m/s, respectivamente.

Figura 4-21 Ciclo diario de Velocidad del viento observado y simulado - Año 2012

Fuente: elaboración propia.

DIA Planta Desaladora Tocopilla | Adenda N° 1 - Anexo P - Modelación material particulado sedimentable I 25

- **Dirección del viento**

La Figura 4-22 muestra la comparación de los ciclos diarios de dirección del viento por horario del día
para valores observados y simulados en la Estación Supersite. Se desprende de la gráfica que existe una
correcta correlación de información, específicamente en el periodo diurno, donde es evidente diferenciar
direcciones de vientos en el rango 250 -300° en ambos casos.

Figura 4-22 Ciclo diario de Dirección del viento observado y simulado - Año 2012

**Observado Estación Supersite**

**Simulado WRF en Estación Supersite**

Fuente: elaboración propia.

Por otra parte, al realizar la comparación de la rosa de vientos anual, presentada en la Figura 4-23, se
observa que para la situación observacional existe una marcada ocurrencia de vientos procedentes de
direcciones SW, WSW y W con porcentajes de ocurrencia de 11%, 19% y 16%, respectivamente. Por su
parte la situación modelada con WRF sobreestima la dirección de vientos procedente de la componente

SW, alcanzando un 39% de ocurrencia; además de elevar la intensidad de la velocidad del viento.

El promedio de velocidad del viento durante todo el periodo para la situación observada es de 1,97 m/s
con un 4,78% de calmas, por su parte la situación modelada entrega un promedio de velocidad de 3,23

m/s con un 5,73% de calmas.

DIA Planta Desaladora Tocopilla | Adenda N° 1 - Anexo P - Modelación material particulado sedimentable I 26

Figura 4-23 Rosa de viento observada y simulada - Año 2012

Fuente: elaboración propia.

DIA Planta Desaladora Tocopilla | Adenda N° 1 - Anexo P - Modelación material particulado sedimentable I 27

A continuación las siguientes Figura 4-24 y Figura 4-25 presentan los campos de viento representativos
del área de influencia del Proyecto asociados a diferentes periodos del día.

|Figura 4-24 Rosa de vientos observada y 06:00 - 11:00 hrs|simulada - periodos 00:00 - 05: 00 hrs y|
|---|---|
|||
|**Observado Estación Supersite**<br>**Rosa de Viento Periodo 00:00 AM - 05: 00 AM**<br>**Entre 01/01/2012 00:00 hrs. y el 31/12/2012 23:00 hrs.**|**Simulado WRF Estación Supersite**<br>**Rosa de Viento Periodo 00:00 AM - 05: 00 AM**<br>**Entre 01/01/2012 00:00 hrs. y el 30/12/2012 23:00 hrs.**|
|||
|**Observado Estación Supersite**<br>**Rosa de Viento Periodo 06:00 AM - 11: 00 AM**<br>**Entre 01/01/2012 00:00 hrs. y el 31/12/2012 23:00 hrs.**|**Simulado WRF Estación Supersite**<br>**Rosa de Viento Periodo 06:00 AM - 11: 00 AM**<br>**Entre 01/01/2012 00:00 hrs. y el 30/12/2012 23:00 hrs.**|

Fuente: elaboración propia.

DIA Planta Desaladora Tocopilla | Adenda N° 1 - Anexo P - Modelación material particulado sedimentable I 28

Como se puede apreciar en la Figura anterior, durante el periodo 00:00 y 05:00 hrs., la meteorología
modelada con WRF reproduce de buena manera la dirección y la magnitud de la velocidad del viento,
donde en ambos casos predominan las direcciones E y ENE, con porcentajes similares de ocurrencia.

El promedio de la velocidad del viento durante este periodo es de 1 m/s para la situación observada y
1,17 m/s para la situación simulada. El porcentaje de calmas alcanza 11,01% para la situación observada
y 11,14% para la situación modelada.

Durante el período comprendido entre las 06:00 y las 11:00 hrs., se observa claramente la transición al
período diurno, apareciendo con fuerza los vientos provenientes del W y WNW con un 16% de
ocurrencia. Sin perjuicio de lo anterior, continúan predominando los vientos provenientes del ENE,
presentes durante un 16% del tiempo.

Durante este período la velocidad promedio del viento, - para la situación observada y modelada -,
alcanza 1,75 m/s y 3,04 m/s, respectivamente. El porcentaje de calmas alcanza 2,54% para la situación
observada y 5,39% para la situación modelada.

|Figura 4-25 Rosa de vientos observada y 18:00 - 23:00 hrs|simulada - periodos 12:00 - 17: 00 hrs y|
|---|---|
|||
|**Observado Estación Supersite**<br>**Rosa de Viento Periodo 12:00 PM - 17: 00 PM**<br>**Entre 01/01/2012 00:00 hrs. y el 31/12/2012 23:00 hrs.**|**Simulado WRF**<br>**Rosa de Viento Periodo 12:00 PM - 17: 00 PM**<br>**Entre 01/01/2012 00:00 hrs. y el 30/12/2012 23:00 hrs.**|

DIA Planta Desaladora Tocopilla | Adenda N° 1 - Anexo P - Modelación material particulado sedimentable I 29

|Col1|Col2|
|---|---|
|**Observado Estación Supersite**<br>**Rosa de Viento Periodo 18:00 PM - 23: 00 PM**<br>**Entre 01/01/2012 00:00 hrs. y el 31/12/2012 23:00 hrs.**|**Simulado WRF**<br>**Rosa de Viento Periodo 18:00 PM - 23: 00 PM**<br>**Entre 01/01/2012 00:00 hrs. y el 30/12/2012 23:00 hrs.**|

Fuente: elaboración propia.

Al comparar la meteorología simulada con WRF con la meteorología observada durante el periodo 12:00
- 17:00 hrs., se observa un buen comportamiento del modelo en términos de procedencia de los vientos,
no así en el caso de las magnitudes de los campos vectoriales donde el modelo tiende a sobreestimar

estos valores.

Durante este período la velocidad promedio del viento, - para la situación observada y modelada -,
alcanza 3,32 m/s y 5,84 m/s, respectivamente. El porcentaje de calmas alcanza 0,44% para la situación
observada y 0% para la situación modelada.

Finalmente, para el periodo 18:00 - 23:00 hrs., se evidencia que la meteorología modelada reproduce de
buena forma la dirección de viento durante, pero no así la magnitud de la velocidad. La dirección
predominante en ambos casos corresponde a la componente SW donde se presenta en un 20% para la
situación observada y 42% para la situación simulada. Cabe destacar la presencia de vientos
procedentes de la componente N en el escenario observado.

El promedio de la velocidad del viento durante este periodo es de 1,73 m/s para la situación observada y
2,79 m/s para la situación simulada. El porcentaje de calmas alcanza 2,58% para la situación observada y
6,39% para la situación modelada.

- **Temperatura**

El ciclo diario de temperatura promedio para el escenario observado y simulado en la Supersite se
muestra en la Figura 4-26. Se observa que el modelo meteorológico reproduce correctamente la
trayectoria promedio diaria de temperatura durante todo el día, pero tiende a sobrestimar lo valores
aproximadamente en 2 °C.

Durante este período la temperatura promedio, - para la situación observada y modelada -, alcanza
18,06 °C y 20,15 °C, respectivamente.

DIA Planta Desaladora Tocopilla | Adenda N° 1 - Anexo P - Modelación material particulado sedimentable I 30

Figura 4-26 Ciclo diario de Temperatura observado y simulado, Año 2012

Fuente: elaboración propia.

4.6.1.2 Evaluación cuantitativa

Para la evaluación cuantitativa del modelo se han utilizado las métricas estadísticas: Media del Error

(ME), Raíz del Error Cuadrático Medio (MSE, por sus siglas en inglés) y Media del Error Absoluto (MAE,
por sus siglas en inglés). Las variables incluidas en esta evaluación corresponden a temperatura y

velocidad del viento.

La descripción de cada uno de los índices estadísticos se presenta a continuación:

 - **Media del Error (ME):** La media del error corresponde a la diferencia entre el promedio
pronosticado y el promedio observado, y por lo tanto expresa el Sesgo del pronóstico.
Pronósticos en promedio muy altos exhiben ME > 0 y pronósticos en promedio muy bajos
muestran ME < 0. ME tiene gran ventaja respecto a otras medidas ya que tiene en cuenta si el
error expresa subestimación o sobrestimación y se representa por la siguiente ecuación:

n

ME= [1]

n [ ∑(y] [k] [−o] [k] [)]

= y̅ − o̅

k=1

Donde:

y k _:_ Valor simulado para la fila k

o k _:_ Valor observado de la estación de superficie para la fila k

_n:_ Número de valores analizados

- **Raíz del Error Cuadrático Medio (MSE):** Una medida de precisión del error es la media del error
cuadrático MSE= 1 [ ∑] n (y − o ) [2]

1

n [ ∑] nk=1 (y k − o k ) [2] . MSE es el promedio de la diferencia cuadrada entre el

pronóstico y la observación. Ya que MSE computa el error cuadrático de los pronósticos éste es
más sensible a los errores extremos. En ocasiones MSE se representa mejor a través de su raíz,
la cual tiene las mismas dimensiones físicas a los pronósticos y observaciones y de esta manera

DIA Planta Desaladora Tocopilla | Adenda N° 1 - Anexo P - Modelación material particulado sedimentable I 31

se puede concebir como una magnitud típica del error del pronóstico. Un valor de MSE igual a
cero indica un ajuste perfecto.

n

RMSE= √ [1]

n

n [ ∑(y] [k] [−o] [k] [)] [2]

k=1

Donde:

y k _:_ Valor simulado para la fila k

o k _:_ Valor observado de la estación de superficie para la fila k

_n:_ Número de valores analizados

- **Media del Error Absoluto (MAE):** La Media del Error Absoluto es el promedio aritmético de los
valores absolutos de las diferencias entre el valor pronosticado y el observado, es una magnitud
típica para los errores del pronóstico en un conjunto de pronósticos y observaciones y es
frecuentemente usado como una medida de verificación. Un MAE es igual a cero si el pronóstico es
perfecto y aumenta positivamente a medida que el pronóstico se aleja de la observación.

n

MAE= [1]

n [ ∑|y] [k] [−o] [k] [|]

k=1

Donde:

y k _:_ Valor simulado para la fila k

o k _:_ Valor observado de la estación de superficie para la fila k

_n:_ Número de valores analizados

A continuación se presenta el resultado de los estadísticos y variables meteorológicas consideradas para

la evaluación cuantitativa de la modelación WRF.

Tabla 4-7 Índices estadísticos para Velocidad del viento y Temperatura

|Estadístico|Velocidad del viento|Temperatura|
|---|---|---|
|Media del Error (ME)|1,27|2,09|
|Raíz del Error Cuadrático Medio (MSE)|2,21|3,14|
|Media del Error Absoluto (MAE)|1,66|2,61|

Fuente: elaboración propia.

El análisis estadístico de la serie temporal de velocidad del viento y temperatura muestra que los valores
de ME; MSE y MAE son mayores a cero, por lo que en ambos casos el modelo de pronóstico

sobreestima los valores observados.

DIA Planta Desaladora Tocopilla | Adenda N° 1 - Anexo P - Modelación material particulado sedimentable I 32

Por otra parte, el análisis estadístico de la serie temporal para diferentes periodos del día presentado en
la Tabla 4-8, dan cuenta que existen ciertos horarios donde el modelo no representa de la mejor forma los
valores meteorológicos observados, es así por ejemplo que en el horario 12:00 - 17:00 hrs., se observan
los mayores valores para los tres estadísticos en el caso de la velocidad del viento, y en el horario 06:00
- 11:00 hrs., los mayores valores para temperatura. Esto se explica por la ubicación de la estación, la
cual está cercana a la costa donde se generan los flujos turbulentos propios del anticiclón del pacífico.

La situación antes descrita, específicamente para la dirección del viento, tiene directa relación con el
alcance que tendrán las emisiones y el grado de dilución inicial de ellas, ya que a mayor velocidad del
viento mayor es el alcance de las emisiones y la capacidad de dilución de éstas, por tanto menores serán
los valores de concentración calculados en los receptores (subestimación de las concentraciones
calculadas por el modelo).

Tabla 4-8 Índices estadísticos para Velocidad del viento y Temperatura por

periodo del día

|Estadístico|Periodo|Velocidad del viento|Temperatura|
|---|---|---|---|
|Media del Error (ME)|00:00 - 05:00|0,16|2,09|
|Media del Error (ME)|06:00 - 11:00|1,30|2,11|
|Media del Error (ME)|12:00 - 17:00|2,55|2,09|
|Media del Error (ME)|18:00 - 23:00|1,08|2,07|
|Raíz del Error Cuadrático Medio<br>(MSE)<br>|00:00 - 05:00|0,98|2,93|
|Raíz del Error Cuadrático Medio<br>(MSE)<br>|06:00 - 11:00|2,41|3,29|
|Raíz del Error Cuadrático Medio<br>(MSE)<br>|12:00 - 17:00|2,98|3,28|
|Raíz del Error Cuadrático Medio<br>(MSE)<br>|18:00 - 23:00|1,98|3,06|
|Media del Error Absoluto (MAE)|00:00 - 05:00|0,72|2,43|
|Media del Error Absoluto (MAE)|06:00 - 11:00|1,90|2,76|
|Media del Error Absoluto (MAE)|12:00 - 17:00|2,58|2,72|
|Media del Error Absoluto (MAE)|18:00 - 23:00|1,47|2,52|

Fuente: elaboración propia.

En base al análisis de incertidumbre realizado, se deduce que de forma general el modelo meteorológico
WRF es capaz de representar las variables meteorológicas observadas para el área de modelación del
Proyecto; reduciendo de esta forma el error de los valores de concentración obtenidos en los receptores.
Cabe señalar que el modelo WRF es uno de los modelos de pronóstico meteorológico más avanzados y
completos a nivel mundial, empleado en la mayoría de los proyectos relacionados con modelación
atmosférica encargados por organismos estatales del país.

DIA Planta Desaladora Tocopilla | Adenda N° 1 - Anexo P - Modelación material particulado sedimentable I 33

4.7 Presentación de los resultados de la modelación de calidad del aire

A continuación, se presentan los resultados de la modelación de la dispersión de los contaminantes
emitidos en la construcción del Proyecto, realizada bajo plataforma de simulación CALPUFF View 6.42
con meteorología de pronóstico WRF.

4.7.1 Mapas de impacto

En la siguiente figura se muestra el mapa de proyección de las concentraciones de material particulado
sedimentable para el escenario de mayor emisión del Proyecto, el cual corresponde al primer año de
construcción. Los archivos de modelación se adjuntan en formato digital en el Apéndice P.2.

DIA Planta Desaladora Tocopilla | Adenda N° 1 - Anexo P - Modelación material particulado sedimentable I 34

Figura 4-27 Isoconcentraciones Promedio Anual de MPS (Límite Norma 200

mg/m [2] /día)

Fuente: elaboración propia.

DIA Planta Desaladora Tocopilla | Adenda N° 1 - Anexo P - Modelación material particulado sedimentable I 35

4.7.2 Tablas de aporte del Proyecto

Debido a que en Chile no existe una norma de calidad primaria para MPS y la normativa secundaria solo
se limita a la cuenca del río Huasco (D.S. 4/1992); es por ello que para evaluar los efectos de este tipo de
emisiones sobre la población, se ha establecido como límite máximo referencial el valor indicado en la
Norma Suiza (Ordenanza sobre el control de la contaminación del aire de 1985, revisada en julio de 2010
por el Consejo Federal Suizo), que indica que este valor no debe superar los **200 mg/m** **[2]** **/día** .

A continuación en la Tabla 4-9 se presentan las concentraciones finales calculadas en cada uno de los
receptores de interés considerados por el Proyecto en evaluación para MPS.

Tabla 4-9 Aporte del Proyecto, MPS (mg/m [2] -día)

|Receptor|Coordenadas UTM<br>WGS 84 H 19 S|Col3|Aporte del<br>Proyecto [mg/m2 -<br>día]|Valor norma<br>[mg/m2 - día]|Porcentaje de la<br>norma (%)<br>Aporte Proyecto|
|---|---|---|---|---|---|
|**Receptor**|**Este (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|
|Estación Gendarmería|377.833|7.559.990|0,028|200|0,014|
|Estación Supersite (Ex Escuela E-10)|377.352|7.557.219|0,006|200|0,003|
|Estación Gobernación|376.374|7.556.617|0,001|200|0,001|
|Estación Bomberos|375.319|7.554.741|0,0001|200|0,000|
|Población Tres Marías|377.653|7.559.935|0,016|200|0,008|
|Vivienda 1 calle Orella|376.914|7.557.920|0,018|200|0,009|
|Vivienda 2 calle Orella|377.024|7.557.795|0,013|200|0,007|
|Vivienda 3 calle Orella|377.135|7.557.670|0,011|200|0,006|
|Vivienda 4 calle Isabel Riquelme|377.236|7.557.681|0,010|200|0,005|
|Vivienda 5 calle Miraflores|377.400|7.557.728|0,010|200|0,005|
|Vivienda 6 calle Miraflores|377.571|7.557.533|0,009|200|0,003|
|Vivienda 7 calle Miraflores|377.742|7.557.338|0,016|200|0,008|

Fuente: elaboración propia.

De la tabla anterior se observa, que los aportes del Proyecto evaluados en los puntos de interés, no
superan la normativa de calidad del aire de referencia, en ninguno de los receptores.

La siguiente Tabla 4-10 presenta el valor calculado y las coordenadas de ubicación del Punto de Máximo
Impacto (PMI), para material particulado sedimentable.

DIA Planta Desaladora Tocopilla | Adenda N° 1 - Anexo P - Modelación material particulado sedimentable I 36

Tabla 4-10 Aporte del Proyecto en el PMI

|PMI|Coordenadas UTM WGS 84<br>H 19 S|Col3|PMI MPS [mg/m2 - día]|Valor norma<br>(mg/m2 - día)|Porcentaje de la<br>norma (%)<br>Aporte Proyecto|
|---|---|---|---|---|---|
|**PMI**|**Este [m]**|**Norte [m]**|**Norte [m]**|**Norte [m]**|**Norte [m]**|
|PMI|376.798|7.559.126|0,04|200|0,02|

Fuente: elaboración propia.

DIA Planta Desaladora Tocopilla | Adenda N° 1 - Anexo P - Modelación material particulado sedimentable I 37

### 5 Conclusiones

Se realizó una modelación de la dispersión atmosférica de las emisiones de MPS, generadas por el
Proyecto, mediante el modelo CALPUFF View, incorporando como dato de entrada, la meteorología de
pronóstico desarrollada a partir del modelo numérico Weather Research and Forecasting Model (WRF).

La modelación consideró las emisiones del Proyecto en evaluación, para el escenario de mayor emisión
calculado para el primer año de construcción.

Para la modelación se definieron como receptores sensibles aquellas estaciones de medición de calidad
del aire ubicadas en la ciudad de Tocopilla, correspondientes a las estaciones Gobernación, Supersite,
Bomberos y Gendarmería, todas estaciones declaradas con representatividad poblacional (EMRP), y
aquellas viviendas representativas de los sectores por donde se construirá la tubería de agua potable del
Proyecto.

Los resultados para la modelación indican que las concentraciones de MPS, registradas en estos
receptores, resultan menores al 0,01% del valor indicado en la normativa de referencia considerada en el
presente documento. De acuerdo a lo anterior, es posible establecer que la ejecución del Proyecto no

incrementará considerablemente las concentraciones existentes de línea base de este contaminante en

los receptores.

Adicionalmente, cabe señalar que el Punto de Máximo Impacto (PMI) calculado, se localiza sobre un área
próxima al Proyecto, no afectando de esta manera algún sector poblado o recurso natural renovable

existente.

Según los resultados antes presentados se puede concluir que el Proyecto no generará efectos adversos
sobre la salud de la población ni la calidad de los recursos renovables durante todas sus etapas.

DIA Planta Desaladora Tocopilla | Adenda N° 1 - Anexo P - Modelación material particulado sedimentable I 38

### 6 Referencias

 - Guía para el uso de modelos de calidad del aire en el SEIA; Servicio de Evaluación Ambiental

2012.

 - Ordenanza sobre el control de la contaminación del aire, 1985, revisada en julio de 2010 por el
Consejo Federal Suizo.

DIA Planta Desaladora Tocopilla | Adenda N° 1 - Anexo P - Modelación material particulado sedimentable I 39

## Apéndices

**Apéndice P.1** **Tasas de emisión de MPS ingresadas al modelo CALPUFF**

|Fuente de emisión|Nombre modelo|ID modelo|Tipo de fuente|Emisión g/s|Área m2|Emisión g/s m2|
|---|---|---|---|---|---|---|
|**Excavación**|||||||
|Edificio de procesos|Edificio|SRC_1|Areal|0,05|7100|6,7E-06|
|Planta Elevadora de agua de mar|Planta_Elev|SRC_2|Areal|0,01|300|1,7E-05|
|Camino de acceso Edificio de Procesos|Camino_Edif|SRC_13|Area - Línea|0,12|5300|2,2E-05|
|Camino de acceso Planta Elevadora de agua de mar|Camino_Plant1|SRC_14|Area - Línea|0,00|1600|1,0E-06|
|Camino de acceso Planta Elevadora de agua de mar|Camino_Plant2|SRC_19|Area - Línea|0,00|2900|5,5E-07|
|Tuberías de captación de agua de mar y emisario de<br>descarga de salmuera|Tuberia1|SRC_4|Area - Línea|0,00|240|1,3E-05|
|Tuberías de impulsión de agua de mar y descarga de<br>salmuera|Tuberia2|SRC_3|Area - Línea|0,01|960|1,0E-05|
|Tubería de impulsión de agua potable|Tuberia3_1|SRC_15|Area - Línea|0,00|582|2,2E-06|
|Tubería de impulsión de agua potable|Tuberia3_2|SRC_22|Area - Línea|0,01|2340|2,3E-06|
|Obras de protección|Protección|SRC_5|Areal|0,01|1000|5,7E-06|
|**Compactación**|||||||
|Edificio de procesos|Edificio|SRC_1|Areal|0,013|7100|1,8E-06|
|Planta Elevadora de agua de mar|Planta_Elev|SRC_2|Areal|0,001|300|1,8E-06|
|Camino de acceso Edificio de Procesos|Camino_Edif|SRC_13|Area - Línea|0,039|5300|7,3E-06|
|Camino de acceso Planta Elevadora de agua de mar|Camino_Plant1|SRC_4|Area - Línea|0,016|1600|1,0E-05|
|Camino de acceso Planta Elevadora de agua de mar|Camino_Plant2|SRC_19|Area - Línea|0,016|2900|5,7E-06|
|Tuberías de captación de agua de mar y emisario de<br>descarga de salmuera|Tuberia1|SRC_4|Area - Línea|0,002|240|7,3E-06|
|Tuberías de impulsión de agua de mar y descarga de<br>salmuera|Tuberia2|SRC_3|Area - Línea|0,007|960|7,3E-06|
|Tubería de impulsión de agua potable|Tuberia3_1|SRC_15|Area - Línea|0,004|582|7,3E-06|
|Tubería de impulsión de agua potable|Tuberia3_2|SRC_22|Area - Línea|0,018|2340|7,5E-06|
|**Carga y descarga de material**|||||||
|Edificio de procesos|Edificio|SRC_1|Areal|0,0003|7100|3,6E-08|
|Planta Elevadora de agua de mar|Planta_Elev|SRC_2|Areal|0,0000|300|1,3E-07|
|Camino de acceso Edificio de Procesos|Camino_Edif|SRC_13|Area - Línea|0,0004|5300|8,1E-08|
|Camino de acceso Planta Elevadora de agua de mar|Camino_Plant1|SRC_4|Area - Línea|0,0001|1600|4,9E-08|
|Camino de acceso Planta Elevadora de agua de mar|Camino_Plant2|SRC_19|Area - Línea|0,0001|2900|2,7E-08|
|Tuberías de captación de agua de mar y emisario de|Tuberia1|SRC_4|Area - Línea|0,0001|240|2,3E-07|

|Fuente de emisión|Nombre modelo|ID modelo|Tipo de fuente|Emisión g/s|Área m2|Emisión g/s m2|
|---|---|---|---|---|---|---|
|descarga de salmuera|||||||
|Tuberías de impulsión de agua de mar y descarga de<br>salmuera|Tuberia2|SRC_3|Area - Línea|0,0002|960|1,8E-07|
|Tubería de impulsión de agua potable|Tuberia3_1|SRC_15|Area - Línea|0,0000|582|3,9E-08|
|Tubería de impulsión de agua potable|Tuberia3_2|SRC_22|Area - Línea|0,0001|2340|4,0E-08|
|Obras de protección|Protección|SRC_5|Areal|0,0001|1000|1,3E-07|
|**Tránsito vehículos liv caminos no pavimentados**|||||||
|Camino de acceso Edificio de Procesos|Camino_Edif|SRC_13|Area - Línea|0,025|5300|4,6E-06|
|Camino de acceso Planta Elevadora de agua de mar|Camino_Plant1|SRC_4|Area - Línea|0,005|1600|3,3E-06|
|**Tránsito vehículos pes caminos no pavimentados**|||||||
|Camino de acceso Edificio de Procesos|Camino_Edif|SRC_13|Area - Línea|0,23|5300|4,4E-05|
|Camino de acceso Planta Elevadora de agua de mar|Camino_Plant1|SRC_4|Area - Línea|0,005|1600|2,6E-05|
|**Tránsito vehículos caminos pavimentados**|||||||
|18 de Septiembre|Camino_18Septiembre|SRC_20|Area - Línea|0,037|6000|6,1E-06|
|Calle 3 Marías|Camino3Marias_Tuberia3|SRC_16|Area - Línea|0,016|1000|1,6E-05|
|Miraflores|CaminoMiraflores_Tuberia3|SRC_23|Area - Línea|0,013|1250|1,0E-05|
|Pasaje Esmeralda|CaminoEsmeralda_Tuberia3|SRC_18|Area - Línea|0,005|500|9,9E-06|
|Ruta 1|Camino_Ruta1|SRC_21|Area - Línea|0,071|8050|8,8E-06|
|Ruta 1|CaminoRuta1_Tuberia3|SRC_17|Area - Línea|0,094|8050|1,2E-05|
|Camino de acceso Edificio de Procesos|Camino_Edif|SRC_13|Area - Línea|0,000|5300|0,0E+00|
|Camino de acceso Planta Elevadora de agua de mar|Camino_Plant1|SRC_4|Area - Línea|0,000|4500|0,0E+00|
|**Total**||||**0,85**||**2,78 E-4**|

**Apéndice P.2** **Archivos de modelación Calpuff**

Se adjuntan en formato digital.

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 4-2: Receptores discretos considerados en la modelación**

| Receptor | Coordenadas UTM WGS 84 H 19S | Col3 |
| --- | --- | --- |
| **Receptor** | **Este [m]** | **Norte [m]** |
| Estación Gendarmería | 377.833 | 7.559.990 |
| Estación Supersite (Ex Escuela E-10) | 377.352 | 7.557.219 |
| Estación Gobernación | 376.374 | 7.556.617 |
| Estación Bomberos | 375.319 | 7.554.741 |
| Población Tres Marías | 377.653 | 7.559.935 |
| Vivienda 1 calle Orella | 376.914 | 7.557.920 |
| Vivienda 2 calle Orella | 377.024 | 7.557.795 |
| Vivienda 3 calle Orella | 377.135 | 7.557.670 |
| Vivienda 4 calle Isabel Riquelme | 377.236 | 7.557.681 |
| Vivienda 5 calle Miraflores | 377.400 | 7.557.728 |
| Vivienda 6 calle Miraflores | 377.571 | 7.557.533 |
| Vivienda 7 calle Miraflores | 377.742 | 7.557.338 |

**Tabla 4-3: Vértices dominio de modelación WRF**

| Vértice | Coordenadas UTM WGS 84 H 19S | Col3 |
| --- | --- | --- |
| **Vértice** | **Este [m]** | **Norte [m]** |
| V1 | 369.096 | 7.589.449 |
| V2 | 431.185 | 7.589.838 |
| V3 | 431.577 | 7.528.109 |
| V4 | 369.487 | 7.527.711 |

**Tabla 4-4: Características del dominio de modelación WRF**

| Período modelado | 1 de enero de 2012 00:00 al 31 de diciembre de 2012 23:00 |
| --- | --- |
| Latitud del centro del dominio | 22.073 S |
| Longitud del centro del dominio | 69.966 W |
| Datum | NWS-84 |
| Resolución | 1 km |
| Tamaño del dominio | 62 km x 62 km |
| Zona Horaria | UTC/GMT UTC - 4 horas |

**Tabla 4-5: Tasa de emisión de material particulado sedimentable**

| Actividad emisora | Emisiones<br>construcción [ton/año] | Col3 | Emisiones<br>operación [ton/año] | Emisiones cierre<br>[ton/año] |
| --- | --- | --- | --- | --- |
| **Actividad emisora** | **Año 1** | **Año 2** | **Año 2** | **Año 2** |
| Escarpe | --- | --- | --- | --- |
| Excavaciones | 2,69 | --- | --- | --- |
| Compactación | 0,15 | --- | --- | --- |
| Carga y descarga de material | 0,04 | --- | --- | --- |
| Circulación vehículos livianos caminos | 0,30 | --- | --- | --- |

**Tabla 4-7: Índices estadísticos para Velocidad del viento y Temperatura**

| Estadístico | Velocidad del viento | Temperatura |
| --- | --- | --- |
| Media del Error (ME) | 1,27 | 2,09 |
| Raíz del Error Cuadrático Medio (MSE) | 2,21 | 3,14 |
| Media del Error Absoluto (MAE) | 1,66 | 2,61 |

**Tabla 4-8: Índices estadísticos para Velocidad del viento y Temperatura por**

| Estadístico | Periodo | Velocidad del viento | Temperatura |
| --- | --- | --- | --- |
| Media del Error (ME) | 00:00 - 05:00 | 0,16 | 2,09 |
| Media del Error (ME) | 06:00 - 11:00 | 1,30 | 2,11 |
| Media del Error (ME) | 12:00 - 17:00 | 2,55 | 2,09 |
| Media del Error (ME) | 18:00 - 23:00 | 1,08 | 2,07 |
| Raíz del Error Cuadrático Medio<br>(MSE)<br> | 00:00 - 05:00 | 0,98 | 2,93 |
| Raíz del Error Cuadrático Medio<br>(MSE)<br> | 06:00 - 11:00 | 2,41 | 3,29 |
| Raíz del Error Cuadrático Medio<br>(MSE)<br> | 12:00 - 17:00 | 2,98 | 3,28 |
| Raíz del Error Cuadrático Medio<br>(MSE)<br> | 18:00 - 23:00 | 1,98 | 3,06 |
| Media del Error Absoluto (MAE) | 00:00 - 05:00 | 0,72 | 2,43 |
| Media del Error Absoluto (MAE) | 06:00 - 11:00 | 1,90 | 2,76 |
| Media del Error Absoluto (MAE) | 12:00 - 17:00 | 2,58 | 2,72 |
| Media del Error Absoluto (MAE) | 18:00 - 23:00 | 1,47 | 2,52 |

**Tabla 4-9: Aporte del Proyecto, MPS (mg/m [2] -día)**

| Receptor | Coordenadas UTM<br>WGS 84 H 19 S | Col3 | Aporte del<br>Proyecto [mg/m2 -<br>día] | Valor norma<br>[mg/m2 - día] | Porcentaje de la<br>norma (%)<br>Aporte Proyecto |
| --- | --- | --- | --- | --- | --- |
| **Receptor** | **Este (m)** | **Norte (m)** | **Norte (m)** | **Norte (m)** | **Norte (m)** |
| Estación Gendarmería | 377.833 | 7.559.990 | 0,028 | 200 | 0,014 |
| Estación Supersite (Ex Escuela E-10) | 377.352 | 7.557.219 | 0,006 | 200 | 0,003 |
| Estación Gobernación | 376.374 | 7.556.617 | 0,001 | 200 | 0,001 |
| Estación Bomberos | 375.319 | 7.554.741 | 0,0001 | 200 | 0,000 |
| Población Tres Marías | 377.653 | 7.559.935 | 0,016 | 200 | 0,008 |
| Vivienda 1 calle Orella | 376.914 | 7.557.920 | 0,018 | 200 | 0,009 |
| Vivienda 2 calle Orella | 377.024 | 7.557.795 | 0,013 | 200 | 0,007 |
| Vivienda 3 calle Orella | 377.135 | 7.557.670 | 0,011 | 200 | 0,006 |
| Vivienda 4 calle Isabel Riquelme | 377.236 | 7.557.681 | 0,010 | 200 | 0,005 |
| Vivienda 5 calle Miraflores | 377.400 | 7.557.728 | 0,010 | 200 | 0,005 |
| Vivienda 6 calle Miraflores | 377.571 | 7.557.533 | 0,009 | 200 | 0,003 |
| Vivienda 7 calle Miraflores | 377.742 | 7.557.338 | 0,016 | 200 | 0,008 |

**Tabla 4-10: Aporte del Proyecto en el PMI**

| PMI | Coordenadas UTM WGS 84<br>H 19 S | Col3 | PMI MPS [mg/m2 - día] | Valor norma<br>(mg/m2 - día) | Porcentaje de la<br>norma (%)<br>Aporte Proyecto |
| --- | --- | --- | --- | --- | --- |
| **PMI** | **Este [m]** | **Norte [m]** | **Norte [m]** | **Norte [m]** | **Norte [m]** |
| PMI | 376.798 | 7.559.126 | 0,04 | 200 | 0,02 |
