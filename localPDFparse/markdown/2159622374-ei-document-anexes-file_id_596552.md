---
title: Sin título
author: admin
date: D:20230814161358-04'00'
language: es
type: report
pages: 101
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - PPR =  PPP (IV)
-->

###### ESTIMACIÓN DE EMISIONES Y MODELACIÓN ATMOSFÉRICA PROYECTO: “INCREMENTO DE LA AUTONOMÍA PARA ASEGURAR LA DISPONIBILIDAD DE COMBUSTIBLES, PLANTA MEJILLONES”

_Preparado por:_

_Para:_

Junio, 2023

**ÍNDICE DE CONTENIDOS**

1 Introducción ............................................................................................ 1

1.1 Alcances ................................................................................................. 3
2 Marco Legal ............................................................................................ 5
3 Meteorología de la Zona de Estudio ............................................................ 6
3.1 Series de Tiempo ..................................................................................... 7
3.2 Rosas de Viento ....................................................................................... 8

3.3 Ciclo Estacional ...................................................................................... 11

3.4 Ciclo Diario Velocidad del Viento ............................................................... 12
3.5 Análisis de Incertidumbre ........................................................................ 14
3.6 Descripción de Parámetros Estadísticos ..................................................... 14
3.6.1 Media .................................................................................................... 14

3.6.2 Moda ..................................................................................................... 14

3.6.3 Mediana ................................................................................................ 15
3.6.4 Desviación Estándar ................................................................................ 15
3.6.5 Raíz del Error Cuadrático Medio ................................................................ 15
3.6.6 Error Medio Cuadrático ............................................................................ 16
3.6.7 Sesgo .................................................................................................... 16
3.6.8 Coeficiente de correlación ........................................................................ 16
3.7 Análisis cuantitativo ................................................................................ 16
4 Estimación de Emisiones del Proyecto ....................................................... 18
4.1 Actividades Emisoras ............................................................................... 18
4.2 Método de Cálculo................................................................................... 19
4.3 Factores de Emisión ................................................................................ 20

4.4 Peso Promedio ........................................................................................ 28

4.4.1 Peso Promedio Caminos Pavimentados ...................................................... 28
4.5 Nivel de Actividad Etapa de Construcción ................................................... 31
4.5.1 Escarpe ................................................................................................. 31
4.5.2 Compactación ........................................................................................ 31
4.5.3 Nivelación .............................................................................................. 31
4.5.4 Excavación ............................................................................................. 32
4.5.5 Carga y Descarga de Material ................................................................... 32
4.5.6 Tránsito de Vehículos por Tipo de Carpeta.................................................. 33
4.5.7 Motor de Vehículos .................................................................................. 34
4.5.8 Motor de Maquinarias .............................................................................. 34
4.5.9 Grupo Electrógeno .................................................................................. 35
4.6 Nivel de actividad Etapa de Operación ....................................................... 36
4.6.1 Tránsito de Vehículos por tipo de carpeta. .................................................. 36
4.6.2 Motor de Vehículos .................................................................................. 36
4.7 Nivel de actividad Etapa de Cierre ............................................................. 37
4.7.1 Tránsito de Vehículos por tipo de carpeta. .................................................. 37
4.7.2 Motor de Vehículos .................................................................................. 37
4.8 Tasas de Emisión Escenario con Proyecto ................................................... 38
5 Modelación de Dispersión de Contaminantes .............................................. 41
5.1 Modelo de Dispersión Atmosférica ............................................................. 41
5.1.1 Base Teórica .......................................................................................... 41
5.1.2 Sistema de Modelación WRF - CALPUFF ..................................................... 41
5.2 Variables de Entrada ingresados al Sistema de Modelación ........................... 43
6 Resultados Modelación ............................................................................ 47

_**Inventario y modelación de emisiones ATM003-22**_

_Junio, 2023_

6.1 Campos de Viento ................................................................................... 47
6.2 Aportes Obtenidos de la Modelación .......................................................... 52
6.2.1 Aporte en Puntos de Interés ..................................................................... 52
6.2.2 Ajustes de Resultados de la Modelación por Incertidumbre ........................... 55
6.3 Aportes en Puntos de Máxima Concentración .............................................. 58
6.4 Análisis de Cumplimiento de Normativa Ambiental ...................................... 62
6.5 Mapas de Isoconcentraciones ................................................................... 64
7 Conclusiones .......................................................................................... 95

**ÍNDICE DE FIGURAS**

Figura N° 1 Ubicación del Proyecto y Área de Modelación ............................................ 4
Figura N° 2 Serie temporal horaria velocidad del viento Estación Jardín Infantil Integra Periodo enero a diciembre 2021 .............................................................................. 7
Figura N° 3 Frecuencia de ocurrencia dirección del viento Estación Jardín Infantil Integra Periodo enero a diciembre 2021 .............................................................................. 8
Figura N° 4 Rosa de Viento Ciclo Completo Estación Jardín Infantil Integra Periodo enero
a diciembre 2021 ................................................................................................... 9
Figura N° 5 Variabilidad temporal del viento - Estación Jardín Infantil Integra Periodo enero
a diciembre 2021 .................................................................................................. 10
Figura N° 6 Variabilidad estacional del viento - Estación Jardín Infantil Integra Periodo 01
enero 2021 - 31 diciembre 2021 ............................................................................ 11
Figura N° 7 Ciclos Diarios de Velocidad (m/s) y Dirección del Viento (°) Estación Jardín
Infantil Integra (Observado v/s Modelado) Periodo enero a diciembre 2021 ................. 13
Figura N° 8 Uso de Suelo ....................................................................................... 44
Figura N° 9 Ubicación Puntos de Interés .................................................................. 46
Figura N° 10 Campos de Viento a las 00:00 horas. ................................................... 48
Figura N° 11 Campos de Viento a las 06:00 horas .................................................... 49
Figura N° 12 Campos de Viento a las 12:00 horas .................................................... 50
Figura N° 13 Campos de Viento a las 18:00 horas. ................................................... 51
Figura N° 14 Ubicación de Puntos de Máximo Impacto, Fase Construcción más Operación
............................................................................................................ 60
Figura N° 15 Ubicación de Puntos de Máximo Impacto, Fase Operación ....................... 61
Figura N° 16 Percentil 98 Promedio Diario de MP10 Fase Construcción más Operación .. 65
Figura N° 17 Promedio del Período de MP10 Fase Construcción más Operación ............. 66
Figura N° 18 Percentil 98 Promedio Diario de MP2,5 Fase Construcción más Operación . 67
Figura N° 19 Promedio del Período de MP2,5 Fase Construcción más Operación ............ 68
Figura N° 20 Promedio del Período de MPS Fase Construcción más Operación .............. 69
Figura N° 21 Promedio del Período del Mes de MPS Fase Construcción más Operación ... 70
Figura N° 22 Percentil 99 Promedio Diario de SO2 Fase Construcción más Operación .... 71
Figura N° 23 Percentil 98,5 Promedio Horario de SO2 Fase Construcción más Operación72
Figura N° 24 Percentil 99,7 Promedio Diario de SO2 Fase Construcción más Operación . 73
Figura N° 25 Percentil 99,73 Promedio Horario de SO2 Fase Construcción más Operación
............................................................................................................ 74
Figura N° 26 Promedio del Período de SO2 Fase Construcción más Operación .............. 75
Figura N° 27 Percentil 99 Máximo Horario de NO2 Fase Construcción más Operación .... 76
Figura N° 28 Promedio del Período de NO2 Fase Construcción más Operación .............. 77
Figura N° 29 Percentil 99 Máximo Horario de CO Fase Construcción más Operación ...... 78
Figura N° 30 Percentil 99 Máximo 8 Horas de CO Fase Construcción más Operación ..... 79
Figura N° 31 Percentil 98 Promedio Diario de MP10 Fase Operación ............................ 80
Figura N° 32 Promedio del Período de MP10 Fase Operación ...................................... 81
Figura N° 33 Percentil 98 Promedio Diario de MP2,5 Fase Operación ........................... 82

_**Inventario y modelación de emisiones ATM003-22**_

_Junio, 2023_

Figura N° 34 Promedio del Período de MP2,5 Fase Operación ..................................... 83
Figura N° 35 Promedio del Período de MPS Fase Operación ........................................ 84
Figura N° 36 Promedio del Período del Mes de MPS Fase Operación ............................ 85
Figura N° 37 Percentil 99 Promedio Diario de SO2 Fase Operación .............................. 86
Figura N° 38 Percentil 98,5 Promedio Horario de SO2 Fase Operación ......................... 87
Figura N° 39 Percentil 99,7 Promedio Diario de SO2 Fase Operación ........................... 88
Figura N° 40 Percentil 99,73 Promedio Horario de SO2 Fase Operación ....................... 89
Figura N° 41 Promedio del Período de SO2 Fase Operación ........................................ 90
Figura N° 42 Percentil 99 Máximo Horario de NO2 Fase Operación .............................. 91
Figura N° 43 Promedio del Período de NO2 Fase Operación ........................................ 92
Figura N° 44 Percentil 99 Máximo Horario de CO Fase Operación ................................ 93
Figura N° 45 Percentil 99 Máximo 8 Horas de CO Fase Operación ............................... 94

_**Inventario y modelación de emisiones ATM003-22**_

_Junio, 2023_

**ÍNDICE DE TABLAS**

Tabla N° 1 Coordenadas de los Vértices del Área de Modelación .................................. 2

Tabla N° 2 Normas de Calidad del Aire Consideradas en el Estudio ............................. 5
Tabla N° 3 Localización de Referencia y Variables Meteorológicas Monitoreadas............. 6
Tabla N° 4 Estadísticas de Datos Meteorológicos Monitoreados .................................... 7
Tabla N° 5 Velocidad Promedio del Viento en m/s ..................................................... 14
Tabla N° 6 Valores de los indicadores estadísticos observados y modelados ................. 17
Tabla N° 7 Estadígrafos de evaluación de desempeño del modelo Velocidad del Viento .. 17
Tabla N° 8 Principales actividades emisoras fase construcción, operación y cierre ......... 18
Tabla N° 9 Factores de Emisión Considerados en el Cálculo ........................................ 20
Tabla N° 10 Valores Considerados en los Factores de Emisión .................................... 24
Tabla N° 11 Peso Promedio Vehículos (t) en Caminos Pavimentados Fase de Construcción
............................................................................................................ 29
Tabla N° 12 Peso Promedio Vehículos (t) en Caminos Pavimentados Fase de Operación 29
Tabla N° 13 Peso Promedio Vehículos (t) en Caminos Pavimentados Fase de Cierre ..... 30
Tabla N° 14 Nivel de Actividad Escarpe (km/año), Fase Construcción-año 1 ................. 31
Tabla N° 15 Nivel de Actividad Compactación (h/año), Fase Construcción-año 1 ........... 31
Tabla N° 16 Nivel de Actividad Nivelación (km), Fase Construcción-año 1 .................... 31
Tabla N° 17 Nivel de Actividad Horas de Excavación (h/año), Fase Construcción-año 1 . 32
Tabla N° 18 Nivel de Actividad Carga y Descarga de material (t/año), Fase Construcciónaño 1 ............................................................................................................ 32
Tabla N° 19 Cálculo del Nivel de Actividad para Tránsito de Vehículos por Caminos
Pavimentados (veh-km/año), Fase Construcción ....................................................... 34
Tabla N° 20 Cálculo del Nivel de Actividad para Motor de Maquinarias (h/año), Fase
Construcción- Año 1 y 2 ........................................................................................ 35
Tabla N° 21 Cálculo del Nivel de Actividad para Grupos Electrógenos Fase ConstrucciónAño 1 y 2 ............................................................................................................ 35
Tabla N° 22 Cálculo del Nivel de Actividad para Tránsito de Vehículos por Caminos
Pavimentados (veh-km/año), Fase Operación .......................................................... 36
Tabla N° 23 Cálculo del Nivel de Actividad para Tránsito de Vehículos por Caminos
Pavimentados (veh-km/año), Fase Cierre ................................................................ 37
Tabla N° 24 Tasas de Emisión Fase Construcción Año 1 (t/año) .................................. 39
Tabla N° 25 Tasas de Emisión Fase Construcción Año 2 (t/año) .................................. 39
Tabla N° 26 Tasas de Emisión Fase Operación (t/año) ............................................... 39
Tabla N° 27 Tasas de Emisión Fase Cierre (t/año) .................................................... 40
Tabla N° 28 Características del Uso de Suelo ........................................................... 43
Tabla N° 29 Localización Puntos Discretos ............................................................... 45
Tabla N° 30 Aporte de Proyecto COPEC Mejillones en Punto de interés, Fase Construcción
más Operación ..................................................................................................... 53
Tabla N° 31 Aporte de Proyecto COPEC Mejillones en Punto de interés, Fase Operación . 54
Tabla N° 32 Aporte de Proyecto COPEC Mejillones en Punto de interés, Fase Construcción
más Operación con Incertidumbre .......................................................................... 56
Tabla N° 33 Aporte de Proyecto COPEC Mejillones en Punto de interés, Fase Operación con
Incertidumbre ...................................................................................................... 57
Tabla N° 34 Localización Punto Máximo Impacto (PMI), Fase Construcción más Operación
............................................................................................................ 58
Tabla N° 35 Localización Punto Máximo Impacto (PMI), Fase Operación ...................... 59
Tabla N° 36 Análisis Normativo en Punto de interés, Fase Construcción más Operación . 62
Tabla N° 37 Análisis Normativo en Punto de interés, Fase Operación ........................... 63

_**Inventario y modelación de emisiones ATM003-22**_

_Junio, 2023_

**Resumen Ejecutivo**

El proyecto Incremento de la autonomía para asegurar la disponibilidad de
combustibles, Planta Mejillones, se localiza en la Región de Antofagasta en la
comuna de Mejillones. El presente documento tiene como objetivo identificar las
fuentes emisoras de material particulado MPS, MP 10, MP 2,5, dióxido de azufre (SO 2 ),
óxidos de nitrógeno (NO X ), monóxido de carbono (CO), compuestos orgánicos
volátiles (COV) y calcular las emisiones de estas fuentes para la fase de
construcción, operación y cierre.

Además de los resultados obtenidos de los inventarios de emisiones, se realizó la
modelación de la dispersión de contaminantes, mediante el modelo “WRFCALPUFF” para la fase de construcción año 1 más operación y operación del
proyecto.

Con respecto a los inventarios de emisiones de los escenarios de Construcción y
Operación y Cierre, se obtienen los siguientes resultados:

`o` Construcción año 1: 1,11 t de MP 2.5, 1,71 t de MP 10, 4,59 t de MPS,

0,52 t de SO 2, 9,84 t de NO X, 3,20 t de CO y 1,11 t de COVs.
`o` Construcción año 2: 0,39 t de MP 2.5, 0,56 t de MP 10, 1,52 t de MPS,

0,31 t de SO 2, 4,81 t de NO X, 1,05 t de CO y 0,39 t de COVs.
`o` Operación: 6,41 t de MP 2.5, 25,76 t de MP 10, 133,21 t de MPS, 0,04 t

de SO 2, 11,15 t de NO X, 2,63 t de CO y 0,51 t de COVs.

`o` Cierre: 0,01 t de MP 2.5, 0,05 t de MP 10, 0,25 t de MPS, <0,01 t de SO 2,

0,04 t de NO X, 0,01 t de CO y <0,01 t de COVs.

En relación con la modelación para la fase de operación se ingresaron 7 puntos de
interés para evaluar el impacto. De los cuales los valores más significativos para
particulas y gases se encuentran cercanos a las áreas del proyecto.

Respecto a los puntos máximo impacto, se observa que para todos los
contaminantes se encuentran concentrados prácticamente en los alrededores de
las inmediaciones de la planta.

Las isoconcentraciones obtenidas muestran que los contaminantes tienen una
dispersión local, ubicándose preferentemente en las cercanías de operación del
proyecto.

Finalmente, en base a los resultados obtenidos, se obtiene que los puntos de
interes no sobrepasan las normas primarias y secundarias de calidad del aire.

_**Inventario y modelación de emisiones ATM003-22**_

_Junio, 2023_

**1** **Introducción**

El proyecto está localizado en la comuna de Mejillones, Región de Antofagasta y
tiene como objetivo una ampliación de la planta existente que contempla
instalaciones de almacenamiento de combustible con 5 tanques de 32.500 m [3] de
capacidad máxima cada uno.

Para efectos de considerar el escenario más desfavorable desde el punto de vista
ambiental, las emisiones atmosféricas del Proyecto se han estimado asumiendo
que aquellas actividades de construcción que tienen el potencial de generar más
emisiones, se concentran en el primer año de la primera etapa de construcción,
considerando además las emisiones de la operación actual de la Planta, para
efectos de la modelación de calidad del aire. Es más, si bien el Proyecto contempla
dos etapas o momentos de construcción de tanques e instalaciones (ver numeral
1.5.10 del capítulo 1 de Descripción de Proyecto), se ha asumido como criterio
conservador, que dichas etapas se ejecutan simultáneamente (como si todo el
Proyecto se construyera en una sola etapa), concentrando las emisiones durante
dos años, pero además considerando para la modelación de efectos sobre la calidad
del aire el peor año, desde el punto de vista ambiental, de la generación de
emisiones; esto es, el primer año.

De esta forma, la evaluación de los impactos sobre la calidad del aire ha
considerado un escenario extremadamente desfavorable desde el punto de vista
ambiental, al concentrar todas las emisiones de la fase de construcción del Proyecto
para la primera etapa de esta fase.

Por su parte, la fase de operación no presenta actividades, dado que el proyecto
corresponde a un incremento de almacenamiento y no a un mayor despacho de
combustible, considerando solamente el flujo operacional de la Planta existente, el
que corresponde a las labores de mantenimiento de los tanques, retiro de residuos,
vehículos livianos y camiones de carga. Teniendo en cuenta lo anterior, si bien la
estimación de emisiones y la modelación de calidad del aire consideran una fase
de operación, esta corresponde a la operación de la Planta existente, dado que,
como se dijo, el presente proyecto no considera modificar el flujo de vehículos
actuales de dicha planta.

Además, se presentan los resultados de las concentraciones obtenidas al modelar
la dispersión atmosférica de material particulado sedimentable (MPS), material
particulado respirable (MP 10 y MP 2,5 ), dióxido de azufre (SO 2 ), dióxido de nitrógeno
(NO 2 ) y monóxido de carbono (CO), correspondiente a la fase deconstrucción año
1 más operación y operación de la Planta.

Adicionalmente, se informa los resultados de la modelación meteorológica realizada
con el modelo WRF y su validación, al comparar los resultados meteorológicos
modelados con los observados por una estación de monitoreo en la zona de estudio.

_**Inventario y modelación de emisiones ATM003-22**_ _1/95_

_Junio, 2023_

El área de modelación corresponde a una grilla de 72 km x 72 km, un espaciamiento
de 1 km y en cuyo interior se encuentra ubicado el sitio de emplazamiento del
Proyecto y los puntos de interés.

La siguiente tabla muestra las coordenadas de los vértices del área de modelación.

_**Tabla N° 1**_
_**Coordenadas de los Vértices del Área de Modelación**_

|Vértice|Coordenadas UTM|Col3|
|---|---|---|
|**Vértice**|**Este (m)**|**Norte (m)**|
|Noreste|393.675|7.483.324|
|Noroeste|320.590|7.483.351|
|Sureste|393.996|7.410.524|
|Suroeste|321.771|7.409.391|

Fuente: Algoritmos SpA, 2023.

Para la estimación de emisiones se utilizaron los factores de emisión definidos en
el documento “AP 42, Fifth Edition, Compilation of Air Pollutant Emission Factors,
Volume 1: Stationary Point and Area Sources, United States - Environmental
Protection Agency”, en el “Manual para el desarrollo de inventarios de emisiones
atmosféricas, MMA 2017”, en la “Guía para la Estimación de Emisiones
Atmosféricas para la Región Metropolitana, Octubre 2020” y en el “Informe Final
Servicio de recopilación y sistematización de factores de emisión al aire para el
Servicio de Evaluación Ambiental del año 2015.”

Cabe señalar que los factores de emisión establecidos en la Guía elaborada por la
SEREMI del Medio Ambiente son los mismos factores definidos por la EPA, pero se
encuentran adaptados al sistema de unidades utilizado a nivel nacional. Además,
la Guía define valores por defecto para las situaciones en las cuales no se cuentan
con mediciones (contenido de finos, porcentajes de humedad, etc.).

Los aportes de concentraciones de material particulado y de gases asociados al
Proyecto fueron obtenidos según los requerimientos de la “Guía para el Uso de
Modelos de Calidad del Aire en el SEIA, 2012” del Servicio de Evaluación Ambiental.
Esta Guía indica como opción la aplicación del sistema de modelación atmosférica
“WRF - CALPUFF”, sistema de modelación que a su vez está definido por la agencia
EPA como sistema de referencia para simular la dispersión de contaminantes
provenientes de centros industriales ubicados en terreno complejo.

La meteorología utilizada en el sistema de modelación se obtuvo por medio del
modelo meteorológico de pronóstico Weather Research and Forecasting Model
(WRF), con todos los parámetros indicados en la “Guía para el Uso de Modelos de
Calidad del Aire en el SEIA, 2012”.

En la Figura N° 1, se presenta el mapa con la ubicación del proyecto y el área de
modelación.

_**Inventario y modelación de emisiones ATM003-22**_ _2/95_

_Junio, 2023_

**1.1** **Alcances**

 - Estimar las emisiones de material particulado respirable (MP 10 ), material
particulado respirable fino (MP 2,5 ), material particulado sedimentable (MPS),
dióxido de azufre (SO 2 ), óxidos de nitrógeno (NO X ), monóxido de carbono
(CO) y compuestos orgánicos volátiles (COV) generados por las actividades
emisoras existentes en la fase de construcción, operación y construcción del
Proyecto COPEC Mejillones.

 Realizar la modelación y validación del modelo WRF mediante la
comparación con datos monitoreados.

 - Obtener aportes en concentración e isoconcentraciones de los
contaminantes normados SO 2, NO 2, CO, MPS, MP 10 y MP 2,5 con el sistema de
modelación WRF-CALPUFF, en cada punto de interés ingresado al modelo,
para el escenario de Construcción más Operación y Operación del proyecto.

 Realizar un análisis normativo del aporte del proyecto.

_**Inventario y modelación de emisiones ATM003-22**_ _3/95_

_Junio, 2023_

_**Figura N° 1**_
_**Ubicación del Proyecto y Área de Modelación**_

Fuente: Algoritmos SpA, 2023.

_**Inventario y modelación de emisiones ATM003-22**_ _4/95_

_Junio, 2023_

**2** **Marco Legal**

Para determinar el aporte del proyecto respecto de la normativa ambiental se
consideraron las normas primarias y secundarias de calidad del aire definidas en la
legislación chilena.

La siguiente tabla presenta los valores límites de referencia para el análisis del
presente documento.

_**Tabla N° 2**_

_**Normas de Calidad del Aire Consideradas en el Estudio**_

|Parámetro|Tipo de<br>Norma|Estadístico|Valor|Referencia|
|---|---|---|---|---|
|MPS|Secundaria|Promedio del<br>periodo|100 mg/m2día|D.S. N°04/92 MINAGRI|
|MPS|Secundaria|Promedio Mensual|150 mg/m2día|D.S. N°04/92 MINAGRI|
|MP10|Primaria|Promedio del<br>periodo|50g/m3N|D.S. N°45/02<br>MINSEGPRES|
|MP10|Primaria|Percentil 98 Diario|130g/m3N|D.S. N°12/21 MMA|
||Primaria|Promedio del<br>periodo|20g/m3N|D.S. N°12/11 MMA|
||Primaria|Percentil 98 Diario|50g/m3N|D.S. N°12/11 MMA|
|SO2|Primaria|Promedio del<br>periodo|60g/m3N|D.S. N°104/18 MMA|
|SO2|Primaria|Percentil 99 Diario|150g/m3N|D.S. N°104/18 MMA|
|SO2|Primaria|Percentil 98,5<br>Horario|350g/m3N|D.S. N°104/18 MMA|
|SO2|Secundaria|Promedio del<br>periodo|80g/m3N|D.S. N°22/10<br>MINSEGPRES|
|SO2|Secundaria|Percentil 99,7 Diario|365g/m3N|D.S. N°22/10<br>MINSEGPRES|
|SO2|Secundaria|Percentil 99,73<br>Horario|1.000g/m3N|D.S. N°22/10<br>MINSEGPRES|
|NO2|Primaria|Promedio del<br>periodo|100g/m3N|D.S. N°114/02<br>MINSEGPRES|
|NO2|Primaria|Percentil 99 Horario|400g/m3N|D.S. N°114/02<br>MINSEGPRES|
||Primaria|Percentil 99 8 horas|10.000<br>g/m3N|D.S. N°115/02<br>MINSEGPRES|
||Primaria|Percentil 99 Horario|30.000<br>g/m3N|D.S. N°115/02<br>MINSEGPRES|

Fuente: Biblioteca del Congreso Nacional de Chile.

_**Inventario y modelación de emisiones ATM003-22**_ _5/95_

_Junio, 2023_

**3** **Meteorología de la Zona de Estudio**

Las variables meteorológicas de mayor incidencia en la dispersión de las emisiones
atmosféricas generadas por el Proyecto, fueron obtenidas por medio del modelo
meteorológico de pronóstico Weather Research and Forecasting Model (WRF).

Este modelo es recomendado por la “Guía para el uso de modelos de calidad del
aire en el SEIA”, para la generación de datos meteorológicos, ya que, según indica,
es uno de los modelos meteorológicos de pronóstico más avanzados y completos,
siendo empleado en la mayoría de los proyectos relacionados con modelación
atmosférica encargados por organismos estatales como el Ministerio del Medio
Ambiente (MMA) y la ex Comisión Nacional de Energía (CNE) (ahora Ministerio de
Energía).

El WRF es un sistema de predicción numérico de mesoescala no hidrostático
(considera los movimientos verticales), usado con fines de pronóstico operacional
y en investigación de la atmósfera. Los principales componentes de este modelo
son las fuentes externas de datos, como son los datos de entrada y la información
geográfica, el sistema de pre procesamiento, el modelo WRF-ARW y los sistemas
de post procesamiento.

Las fuentes externas de datos contienen información necesaria para inicializar
WRF. Éstos corresponden a las observaciones convencionales o satélites de la
atmósfera. De estos datos se obtienen las condiciones iniciales y de borde para las
simulaciones del WRF. También es necesario entregarle datos sobre el terreno que
contengan información sobre la orografía, uso de suelo, relieve y vegetación, entre
otros.

Los modelos meteorológicos al representar una aproximación de la realidad, tienen
asociados errores e incertidumbres, es por este motivo que los resultados
obtenidos mediante la modelación con WRF serán comparados con las variables
meteorológicas registradas por la estación Jardín Infantil Integra con el fin de
evaluar la capacidad predictiva del modelo.

La Tabla N° 3 presenta las coordenadas de localización y las variables
meteorológicas monitoreadas en la estación antes mencionada.

_**Tabla N° 3**_
_**Localización de Referencia y Variables Meteorológicas Monitoreadas**_

|Estación|Coordenadas UTM|Col3|Variables|Periodo|
|---|---|---|---|---|
|**Estación**|**Este (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|
|Jardín<br>Infantil<br>Integra|352.064|7.444.407|Velocidad del viento<br>Dirección del viento|01 de enero al 31 de<br>diciembre 2021|

Fuente: Algoritmos, SpA 2023.

En las siguientes secciones se realiza un análisis comparativo entre la data
meteorológica registrada por la estación de monitoreo y lo simulado con WRF para
el periodo de registro (ver Tabla N° 3), con resolución horaria para las variables

_**Inventario y modelación de emisiones ATM003-22**_ _6/95_

_Junio, 2023_

meteorológicas de velocidad y dirección de viento, ya que estos parámetros
influyen directamente en el fenómeno de dispersión de contaminantes.

**3.1** **Series de Tiempo**

La Tabla N° 4 muestra los porcentajes de datos válidos y de calmas monitoreados
por la Estación Jardín Infantil Integra. Respecto a la velocidad del viento se
consideró como calma los registros menores a 0,5 (m/s).

_**Tabla N° 4**_
_**Estadísticas de Datos Meteorológicos Monitoreados**_

|Estación|Datos<br>Totales|Porcentaje de Calma (%)|Col4|Porcentaje Datos<br>Válidos (%)|
|---|---|---|---|---|
|**Estación**|**Datos**<br>**Totales**|**Periodo**<br>**Diurno**|**Periodo**<br>**Nocturno**|**Periodo**<br>**Nocturno**|
|Jardín Infantil<br>Integra|8.759|0%|1%|100%|

Fuente: Algoritmos SpA, 2023.

La serie temporal de la velocidad del viento registrada por la Estación Jardín Infantil
Integra, permiten un análisis cualitativo de los datos en términos de variabilidad,
amplitud de rango y frecuencia de los datos con que se cuenta. No se presentan
las series temporales generadas por el modelo WRF, ya que la información de
pronóstico dispone de la totalidad de los datos.

_**Figura N° 2**_
_**Serie temporal horaria velocidad del viento**_
_**Estación Jardín Infantil Integra - Periodo enero a diciembre 2021**_

Fuente: Algoritmos SpA, 2023.

La serie temporal de la velocidad del viento registrada por la estación Jardín Infantil
Integra no muestra ciclo anual ya que se observa el mismo patrón a lo largo de
todo el año, con velocidades que varían entre 2 y 4 m/s.

_**Inventario y modelación de emisiones ATM003-22**_ _7/95_

_Junio, 2023_

Con respecto a la dirección del viento, se identifica un patrón dominante, con
vientos preferentemente desde el Sur (S) correspondiente a la línea centrada en
180°.

_**Figura N° 3**_
_**Frecuencia de ocurrencia dirección del viento**_
_**Estación Jardín Infantil Integra - Periodo enero a diciembre 2021**_

Fuente: Algoritmos SpA, 2023 .

**3.2** **Rosas de Viento**

A continuación, se muestran los campos de viento anual y para diferentes periodos
del día, los que muestran la variabilidad temporal del viento durante el periodo
desde enero a diciembre del 2021 para la Estación Jardín Infantil Integra y la
modelación generada con WRF para dicha estación.

_**Inventario y modelación de emisiones ATM003-22**_ _8/95_

_Junio, 2023_

_**Figura N° 4**_
_**Rosa de Viento Ciclo Completo Estación Jardín Infantil Integra**_

_**Periodo enero a diciembre 2021**_

|Observado|Modelado|
|---|---|
|||

Fuente: Algoritmos SpA, 2023.

La rosa de viento del lado izquierdo de la Figura N° 4, corresponde a los registros
de la Estación Jardín Infantil Integra en la cual se puede observar que prevalecen
con mayor frecuencia vientos desde el Sur (S) y Sur Sureste (SSE), explicando en
conjunto un 55% de la frecuencia total.

Con respecto a lo modelado con WRF (lado derecho de la Figura N° 4), se obtiene
el mismo patrón de vientos observados, sin embargo, se sobrestima la frecuencia
de ocurrencia de los vientos desde el Sur Suroeste (SSO).

Al observar el comportamiento espacial de los vientos en los diferentes periodos
del día para la Estación Jardín Infantil Integra (parte superior de la Figura N° 5) se
puede apreciar que, principalmente a lo largo del todo el día se registran vientos
desde el Sur (S). Sin embargo, entre las 06:00 y 17:00 aparece un componente
desde el Noroeste (NO).

_**Inventario y modelación de emisiones ATM003-22**_ _9/95_

_Junio, 2023_

_**Figura N° 5**_
_**Variabilidad temporal del viento - Estación Jardín Infantil Integra**_

_**Periodo enero a diciembre 2021**_

|Col1|00:00 - 05:00 horas|06:00 - 11:00 horas|12:00 - 17:00 horas|18:00 - 23:00 horas|
|---|---|---|---|---|
|**_Observado_**|||||
|**_Modelado_**|||||

Fuente: Algoritmos SpA, 2023.

_**Inventario y modelación de emisiones ATM003-22**_ _10/95_
_Diciembre, 2021_

**3.3** **Ciclo Estacional**

La Figura N° 6 muestra la evolución estacional y diaria de la velocidad y dirección
del viento, presentando en el eje “x” las horas del día y en el eje “y” los meses del
año. Es posible observar un leve patrón diario, correspondiendo a vientos débiles
en horas de la noche y madrugada, con valores que varían entre 1 y 3 m/s a lo
largo de todo el año. Para el horario diurno, se observa un leve aumento entre
10:00 y 21:00 horas, con valores que alcanzan los 5 m/s. Respecto a los datos
modelados, se observa un patrón similar, donde no se observa un claro ciclo diario,
sin embargo se sobrestima la velocidad observada.

En cuanto a la dirección del viento observado por la estación Jardín Infantil Integra,
se obtienen vientos desde el Sur (S) principalmente entre las 00:00 y 09:00 horas
y 17:00 y 23:00 horas, tanto en los datos observados como modelados

_**Figura N° 6**_
_**Variabilidad estacional del viento - Estación Jardín Infantil Integra**_

_**-**_
_**Periodo 01 enero 2021**_ _**31 diciembre 2021**_

|Observado|Modelado|
|---|---|
|||

Fuente: Algoritmos SpA, 2023.

_**Inventario y modelación de emisiones ATM003-22**_ _11/95_

**3.4** **Ciclo Diario Velocidad del Viento**

A continuación, se presentan los ciclos diarios promedio de la velocidad y dirección
del viento monitoreada por la Estación Jardín Infantil Integra y lo modelado con
WRF para dicha estación.

Al apreciar la curva de velocidad promedio para la Estación Jardín Infantil Integra
(lado izquierdo superior de la Figura N° 7), esta presenta una condición homogénea
a lo largo de la madrugada, con una velocidad en torno a 2 m/s, aumentando a
partir de las 09:00 horas hasta alcanzar levemente el máximo alrededor de las
16:00 horas alcanzando un valor de 4 m/s. De los datos modelados se obtiene un
ciclo similar, ya que no existe un ciclo diario muy marcado, donde alcanza
levemente un máximo igual a 6 m/s.

Respecto de la dirección del viento observada en Estación Jardín Infantil Integra
(parte inferior izquierda de la Figura N° 7) se observa un patrón dominante de
vientos desde el Sur (S) entre las 00:00 y 09:00 horas y entre las 15:00 y 23:00
horas, a diferencia de lo que ocurre entre las 10:00 y 14:00 horas, donde los
vientos vienen desde el Norte Noroeste (NNO).

_**Inventario y modelación de emisiones ATM003-22**_ _12/95_

_**Figura N° 7**_
_**Ciclos Diarios de Velocidad (m/s) y Dirección del Viento (°)**_

_**Estación Jardín Infantil Integra (Observado v/s Modelado)**_

_**Periodo enero a diciembre 2021**_

|Observado|Modelado|
|---|---|
|||

Fuente: Algoritmos SpA, 2023.

_**Inventario y modelación de emisiones ATM003-22**_ _13/95_

_Diciembre, 2021_

**3.5** **Análisis de Incertidumbre**

La Tabla N° 5 presenta las diferencias entre las observaciones y los pronósticos de
los valores promedios de velocidad de viento para el periodo diurno y nocturno
para la Estación Jardín Infantil Integra.

_**Tabla N° 5**_
_**Velocidad Promedio del Viento en m/s**_

|Estación|Promedio<br>Observación|Promedio<br>Pronóstico WRF|% Sobrestimado<br>por pronóstico|
|---|---|---|---|
|Jardín Infantil<br>Integra|2,78|4,38|36%|

Fuente: Algoritmos SpA, 2023.

Al comparar los ciclos diarios promedios observados y de pronóstico para la
Estación Jardín Infantil Integra, se evidencia que el modelo reproduce
correctamente la trayectoria del viento, sobrestimando en un 36% los valores
modelados situación que genera condiciones favorables con respecto a la
ventilación en el área de interés, ya que la meteorología generada por el modelo
WRF al ser utilizada como dato de entrada para el modelo de dispersión CALPUFF.
Este último subestimaría el valor de la concentración de los contaminantes.

**3.6** **Descripción de Parámetros Estadísticos**

**3.6.1** **Media**

Valor característico de una serie de datos cuantitativos, se obtiene a partir de la
suma de todos sus valores dividida entre el número de sumandos. Cuando el
[conjunto es una muestra aleatoria recibe el nombre de media muestral siendo uno](https://es.wikipedia.org/wiki/Muestra_aleatoria)
[de los principales estadísticos muestrales.](https://es.wikipedia.org/wiki/Estad%C3%ADstico)

###### 1

## 

_n_

###### x = x

_i_
###### _n_

###### = n =

_i_

1

**3.6.2** **Moda**

Corresponde al valor que cuenta con una mayor frecuencia en una distribución de
datos, es decir, el número más repetido.

_**Inventario y modelación de emisiones ATM003-22**_ _14/95_

_Junio, 2023_

**3.6.3** **Mediana**

La mediana es la medida más robusta, resistente y más común de la tendencia
central de la distribución de datos. A diferencia de la media no se ve afectada por
valores extremos que pudieran ser anómalos.

**3.6.4** **Desviación Estándar**

Corresponde a la raíz cuadrada de la diferencia media cuadrática entre el error de
pronóstico y el error de pronóstico promedio (E). Se utiliza para medir la cantidad
de variabilidad en el pronóstico de variables meteorológicas. Cuanto mayor sea el
valor de la SD, mayor será la variabilidad del pronóstico

Para realizar la validación de los datos registrados por la estación Camanchaca, se
calculan diferentes estadísticos clásicos tales como:

**3.6.5** **Raíz del Error Cuadrático Medio**

Corresponde al cálculo de la raíz cuadrada del promedio de las diferencias
cuadradas de cada una de los valores del pronóstico y la observación. Este cálculo
permite ponderar los errores positivos y negativos, por lo cual en él están incluidos
los errores sistemáticos y aleatorios de los modelos.

Dónde:

X 1i : es el valor de la serie No 1

x 2i : es el valor de la serie No2

N: es el número de valores analizado

_**Inventario y modelación de emisiones ATM003-22**_ _15/95_

_Junio, 2023_

**3.6.6** **Error Medio Cuadrático**

El error medio cuadrático entrega las medidas de las diferencias en promedio entre
los valores modelados y los observados. Está definido como:

_N_ _abs_ ( _x_ 1 _i_ − _x_ 2 _i_
_MAE_ =

( _x_ 1 _i_ − _x_ 2 _i_ )

1 _i_ −

=
### 

_i_ = 1

_N_

_i_

1

**3.6.7** **Sesgo**

Proporciona información sobre la tendencia del modelo a sobreestimar o
subestimar una variable, cuantificando el error sistemático del modelo.

**3.6.8** **Coeficiente de correlación**

Nos permite establecer la relación lineal entre los modelos utilizados y la
observación y está acotada entre -1 y 1.

Si Corr < 0 significa que las dos variables se correlacionan en sentido inverso. A
valores altos de una de ellas le suelen corresponder valor bajos de la otra y
viceversa. Si Corr > 0 las dos variables se correlacionan en sentido directo.A
valores altos de una le corresponden valores altos de la otra. Si corr = 0 se dice
que las variables están incorrelacionadas por lo tanto no puede establecerse ningún
sentido de covariación.

**3.7** **Análisis cuantitativo**

Tanto la velocidad como la dirección del viento son variables meteorológicas
relevantes para el análisis de los datos de entrada del modelo y a objeto de
observar la dirección de las masas de aire. Debido a lo anterior, a continuación, se
presentan los resultados obtenidos al aplicar los estadísticos a los datos observados
y modelados para la velocidad del viento en la estación evaluada.

_**Inventario y modelación de emisiones ATM003-22**_ _16/95_

_Junio, 2023_

_**Tabla N° 6**_
_**Valores de los indicadores estadísticos observados y modelados**_

|Estadísticos|Unidad|Jardín Infantil Integra|Col4|
|---|---|---|---|
|**Estadísticos**|**Unidad**|**observado**|**modelado**|
|Media|m/s|2,79|4,38|
|Máximo|m/s|8,58|11,75|
|Mínimo|m/s|0,20|0,07|
|Moda|m/s|2,74|5,00|
|Mediana|m/s|2,70|4,45|
|Desviación estándar|--|1,23|2,07|

Fuente: Algoritmos SpA, 2023

Para complementar el análisis cualitativo, se presenta en la Tabla N° 7 un análisis
cuantitativo de las variables velocidad del viento que compara los valores
observados y modelados por medio de la utilización de tres estadígrafos
comúnmente utilizados para la evaluación del desempeño de modelos; Sesgo, Error
Cuadrático Medio y el coeficiente de correlación (r).

La siguiente tabla resume los estadígrafos de evaluación de desempeño del modelo
WRF respecto a los datos monitoreados por la estación Jardín Infantil Integra.

_**Tabla N° 7**_
_**Estadígrafos de evaluación de desempeño del modelo**_

_**Velocidad del Viento**_

|Estación|Serie de datos|Medida de Error|Col4|Col5|
|---|---|---|---|---|
|**Estación**|**Serie de datos**|**Sesgo**|**RMSE**|**Corr**|
|Jardín Infantil<br>Integra|Serie de Tiempo|1,60|2,40|0,51|
|Jardín Infantil<br>Integra|Ciclo Diario|1,60|1,67|0,85|

Fuente: Algoritmos SpA, 2023.

En base a lo anteriormente expuesto respecto de la meteorología, es posible
concluir que el modelo representa de manera satisfactoria la dinámica del viento
observado ya que este reproduce un ciclo anual de la velocidad junto a los patrones
en la dirección, sin embargo, este sobre estima los valores nocturnos. En relación
a los estadísticos evaluados, se obtiene un bajo sesgo, con un valor de error igual
a 1,60 para el ciclo diario. Finalmente al evaluar la correlación, obtenemos un valor
superior a 0,5 tanto en la serie temporal anual como en el ciclo diario.

_**Inventario y modelación de emisiones ATM003-22**_ _17/95_

_Junio, 2023_

**4** **Estimación de Emisiones del Proyecto**

**4.1** **Actividades Emisoras**

La Tabla N° 8 presenta las principales actividades emisoras de material particulado
respirable (MP 10 ), material particulado respirable fino (MP 2,5 ), material particulado
sedimentable (MPS), dióxido de azufre (SO 2 ), óxidos de nitrógeno (NO X ), monóxido
de carbono (CO) y compuestos orgánicos volátiles (COVs) para la fase de
construcción, operación y cierre del proyecto.

**Tabla N° 8**
**Principales actividades emisoras fase construcción, operación y cierre**

|Fase|Actividades|
|---|---|
|Construcción|• <br>Escarpe<br>• <br>Compactación<br>• <br>Nivelación<br>• <br>Excavación<br>• <br>Carga y Descarga de material<br>• <br>Tránsito por camino pavimentado<br>• <br>Motor Vehículos<br>• <br>Maquinaria<br>• <br>Grupo Electrógeno|
|Operación|• <br>Tránsito por camino pavimentado<br>• <br>Motor Vehículos|
|Cierre|• <br>Tránsito por camino pavimentado<br>• <br>Motor Vehículos|

Fuente: Algoritmos SpA, 2023

_**Inventario y modelación de emisiones ATM003-22**_ _18/95_

_Junio, 2023_

**4.2** **Método de Cálculo**

La ecuación general para determinar las emisiones de cualquier actividad es
definida por la EPA como sigue a continuación.

###### E= Fe · Na· (1 −

Ea

(I)
###### 100 [)]

Dónde:

###### E : Emisión Fe : Factor de emisión Na : Nivel de actividad Ea : Eficiencia de abatimiento

Las emisiones asociadas a cada una de las actividades antes descritas fueron
calculadas utilizando los factores de emisión definidos en el documento “AP 42,
Fifth Edition, Compilation of Air Pollutant Emission Factors, Volumen 1: Stationary
Point and Area Sources, United States - Environmental Protection Agency”, en el
“Manual para el desarrollo de inventarios de emisiones atmosféricas, MMA 2017”,
en la “Guía para la Estimación de Emisiones Atmosféricas para la Región
Metropolitana (Octubre 2020)” y en lo señalado en el documento del Servicio de
Evaluación Ambiental “Informe Final; Servicio de recopilación y sistematización de
factores de emisión al aire para el Servicio de Evaluación Ambiental”, publicado en
Julio del año 2015.

Para el caso del dióxido de azufre, la ecuación general (II) utilizada para el cálculo
de emisiones provenientes desde el motor de vehículos es la siguiente:

###### E SO 2 = 2 · CC· S comb (II)

Dónde:

###### E SO2 : Emisión SO 2 (kg/h) CC : Consumo de combustible (kg/h) S comb : Contenido de azufre del combustible (en peso m/m)

El contenido de azufre considerado para el cálculo de emisiones corresponde al
combustible Petróleo Diésel equivalente a 50 ppm (50/1.000.000 peso m/m).

Para determinar el consumo de combustible del motor de vehículos se considera la
velocidad de circulación de cada uno de ellos.

_**Inventario y modelación de emisiones ATM003-22**_ _19/95_

_Junio, 2023_

**4.3** **Factores de Emisión**

Los factores de emisión para material particulado MP 10, MP 2,5 y MPS y gases NO x,
SO 2, CO y COV considerados en el cálculo, se presentan en la siguiente tabla.

_**Tabla N° 9**_
_**Factores de Emisión Considerados en el Cálculo**_

|Fuente<br>Emisora|Factor|Col3|Ref.|Unidad|Variables|
|---|---|---|---|---|---|
|Escarpe|MP10 <br>MPS|5,7|(1)|kg/km|**-**|
|Escarpe|MP2,5|0,855|0,855|0,855|0,855|
|Compactación|MP2.5<br>MPS|3<br>,1<br>2<br>,1<br>60<br>,<br>2<br>_H_<br>_f_<br>_k_<br><br><br><br>|(1)|kg/h|f: % de finos del<br>material|
|Compactación|MP10|4<br>,1<br>5<br>,1<br>45<br>,<br>0<br>_H_<br>_f_<br>_k_<br><br><br><br>|4<br>,1<br>5<br>,1<br>45<br>,<br>0<br>_H_<br>_f_<br>_k_<br><br><br><br>|4<br>,1<br>5<br>,1<br>45<br>,<br>0<br>_H_<br>_f_<br>_k_<br><br><br><br>|H: %humedad<br>del material|
|Nivelación|MP10|k∙0,0056 ∙(V)2|(1)|Kg/km|k: Factor<br>tamaño de<br>partícula|
|Nivelación|MP2,5 <br>MPS|k∙0,0034 ∙(V)2,5|k∙0,0034 ∙(V)2,5|k∙0,0034 ∙(V)2,5|V: Velocidad<br>media de<br>Niveladora<br>(km/h)|
|Excavación|MP2,5|3<br>,1<br>2<br>,1<br>60<br>,<br>2<br>_H_<br>_f_<br>_k_<br><br><br><br>|(1)|kg/h|f: % de finos del<br>material|
|Excavación|MP10|4<br>,1<br>5<br>,1<br>45<br>,<br>0<br>_H_<br>_f_<br>_k_<br><br><br><br>|4<br>,1<br>5<br>,1<br>45<br>,<br>0<br>_H_<br>_f_<br>_k_<br><br><br><br>|4<br>,1<br>5<br>,1<br>45<br>,<br>0<br>_H_<br>_f_<br>_k_<br><br><br><br>|H:% humedad<br>del material|
|Excavación|MPS|3<br>,1<br>2<br>,1<br>60<br>,<br>2<br>_H_<br>_f_<br>_k_<br><br><br><br>|3<br>,1<br>2<br>,1<br>60<br>,<br>2<br>_H_<br>_f_<br>_k_<br><br><br><br>|3<br>,1<br>2<br>,1<br>60<br>,<br>2<br>_H_<br>_f_<br>_k_<br><br><br><br>|k: Factor<br>tamaño de<br>partícula|
|Carga y<br>descarga de<br>material|MP10 <br>MP2,5 <br>MPS|4,1<br>3,1<br>2<br>2,2<br>0016<br>,0<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>_H_<br>_u_<br>_k_<br>|(2)|kg/t|k: Factor<br>tamaño de<br>partícula|
|Fugitivas<br>caminos<br>pavimentados|MP10<br>MP2,5<br>MPS|[k ∙sL0,91 ∙(W ∙1,102311)1,02]|(3)|g/veh-km|sL: Carga de<br>fino de la<br>superficie<br>(g/m2)|
|Fugitivas<br>caminos<br>pavimentados|MP10<br>MP2,5<br>MPS|[k ∙sL0,91 ∙(W ∙1,102311)1,02]|(3)|g/veh-km|W: Peso<br>promedio del<br>camión (t)|
|Fugitivas<br>caminos<br>pavimentados|MP10<br>MP2,5<br>MPS|[k ∙sL0,91 ∙(W ∙1,102311)1,02]|(3)|g/veh-km|k: Factor<br>tamaño de<br>partícula|
|Motor de<br>camiones<br>pesados diésel<br>tipo 3 (EURO<br>III)|MP10 <br>MP2,5 <br>MPS|((0,10+(0,42*exp(((-<br>1)*0,04)*V)))+(0,86*<br>exp(((-1)*0,16)*V)))|(4)|g/veh-km<br>|V: Velocidad<br>camión (km/h)|
|Motor de<br>camiones<br>pesados diésel<br>tipo 3 (EURO<br>III)|SO2 <br>(CC)|((199,10+(496,04*exp(((-<br>1)*0,05)*V)))+ <br>(3.798,31*exp(((-<br>1)*0,57)*V)))|((199,10+(496,04*exp(((-<br>1)*0,05)*V)))+ <br>(3.798,31*exp(((-<br>1)*0,57)*V)))|((199,10+(496,04*exp(((-<br>1)*0,05)*V)))+ <br>(3.798,31*exp(((-<br>1)*0,57)*V)))|((199,10+(496,04*exp(((-<br>1)*0,05)*V)))+ <br>(3.798,31*exp(((-<br>1)*0,57)*V)))|
|Motor de<br>camiones<br>pesados diésel<br>tipo 3 (EURO<br>III)|CO|(1,25+(103,70/(1+exp((((-<br>1)*-1,39)+|(1,25+(103,70/(1+exp((((-<br>1)*-1,39)+|(1,25+(103,70/(1+exp((((-<br>1)*-1,39)+|(1,25+(103,70/(1+exp((((-<br>1)*-1,39)+|

_**Inventario y modelación de emisiones ATM003-22**_ _20/95_

_Junio, 2023_

|Fuente<br>Emisora|Factor|Col3|Ref.|Unidad|Variables|
|---|---|---|---|---|---|
|||(0,54*ln(V)))+(0,04*V)))))||||
||NOx|((5,58+(14,57*exp(((-<br>1)*0,05)*V))) <br>+(45,65*exp(((-1)*0,31)*V)))|((5,58+(14,57*exp(((-<br>1)*0,05)*V))) <br>+(45,65*exp(((-1)*0,31)*V)))|((5,58+(14,57*exp(((-<br>1)*0,05)*V))) <br>+(45,65*exp(((-1)*0,31)*V)))|((5,58+(14,57*exp(((-<br>1)*0,05)*V))) <br>+(45,65*exp(((-1)*0,31)*V)))|
||COV|((0,1359+(0,716*exp(((-<br>1)*0,0235)*V)))+(2,79878*ex<br>p(((-1)*0,12346)*V)))|((0,1359+(0,716*exp(((-<br>1)*0,0235)*V)))+(2,79878*ex<br>p(((-1)*0,12346)*V)))|((0,1359+(0,716*exp(((-<br>1)*0,0235)*V)))+(2,79878*ex<br>p(((-1)*0,12346)*V)))|((0,1359+(0,716*exp(((-<br>1)*0,0235)*V)))+(2,79878*ex<br>p(((-1)*0,12346)*V)))|
|Motor de<br>camiones<br>medianos<br>diésel tipo 3<br>(EURO III)|MP10 <br>MP2,5<br>MPS|(0,008+(0,48/(1+EXP((((-1)*<br>4,58)+(1,88*ln(V)))+<br>(-0,02*V)))))|(4)|g/veh-km<br>|V: Velocidad<br>camión (km/h)|
|Motor de<br>camiones<br>medianos<br>diésel tipo 3<br>(EURO III)|SO2 <br>(CC)|(1/(((-1,25E-06*(V2))+<br>(0,0002*V))+0,001))|(1/(((-1,25E-06*(V2))+<br>(0,0002*V))+0,001))|(1/(((-1,25E-06*(V2))+<br>(0,0002*V))+0,001))|(1/(((-1,25E-06*(V2))+<br>(0,0002*V))+0,001))|
|Motor de<br>camiones<br>medianos<br>diésel tipo 3<br>(EURO III)|CO|((0,73+(3,66*EXP(((-1)*<br>0,06)*V)))+(5,23*<br>EXP(((-1)*0,23)*V)))|((0,73+(3,66*EXP(((-1)*<br>0,06)*V)))+(5,23*<br>EXP(((-1)*0,23)*V)))|((0,73+(3,66*EXP(((-1)*<br>0,06)*V)))+(5,23*<br>EXP(((-1)*0,23)*V)))|((0,73+(3,66*EXP(((-1)*<br>0,06)*V)))+(5,23*<br>EXP(((-1)*0,23)*V)))|
|Motor de<br>camiones<br>medianos<br>diésel tipo 3<br>(EURO III)|NOx|((3,76+(8,84*EXP(((-1)*<br>0,06)*V)))+(32,81*<br>EXP(((-1)*0,33)*V)))|((3,76+(8,84*EXP(((-1)*<br>0,06)*V)))+(32,81*<br>EXP(((-1)*0,33)*V)))|((3,76+(8,84*EXP(((-1)*<br>0,06)*V)))+(32,81*<br>EXP(((-1)*0,33)*V)))|((3,76+(8,84*EXP(((-1)*<br>0,06)*V)))+(32,81*<br>EXP(((-1)*0,33)*V)))|
|Motor de<br>camiones<br>medianos<br>diésel tipo 3<br>(EURO III)|COV|(0,0837+(1,3210/(1+EXP((((-<br>1)*<br>4,5313)+(1,89348*LN(V)))+<br>(-0,0103*V)))))|(0,0837+(1,3210/(1+EXP((((-<br>1)*<br>4,5313)+(1,89348*LN(V)))+<br>(-0,0103*V)))))|(0,0837+(1,3210/(1+EXP((((-<br>1)*<br>4,5313)+(1,89348*LN(V)))+<br>(-0,0103*V)))))|(0,0837+(1,3210/(1+EXP((((-<br>1)*<br>4,5313)+(1,89348*LN(V)))+<br>(-0,0103*V)))))|
|Motor de buses<br>interurbanos<br>diésel tipo 3<br>(EURO III)|MP10 <br>MP2,5<br>MPS|(0,08+(1,07/(1+EXP((((-<br>1)*2,35)+(1,08*LN(V)))+(0,01<br>1*V)))))|(4)|g/veh-km|V: Velocidad<br>camión (km/h)|
|Motor de buses<br>interurbanos<br>diésel tipo 3<br>(EURO III)|SO2 <br>(CC)|((191,11+(700,03*EXP(((-<br>1)*0,053)*V)))+(3813,8*<br>EXP(((-1)*0,45)*V)))|((191,11+(700,03*EXP(((-<br>1)*0,053)*V)))+(3813,8*<br>EXP(((-1)*0,45)*V)))|((191,11+(700,03*EXP(((-<br>1)*0,053)*V)))+(3813,8*<br>EXP(((-1)*0,45)*V)))|((191,11+(700,03*EXP(((-<br>1)*0,053)*V)))+(3813,8*<br>EXP(((-1)*0,45)*V)))|
|Motor de buses<br>interurbanos<br>diésel tipo 3<br>(EURO III)|CO|((1,09+(6,47*EXP(((-<br>1)*0,046)*V)))+(15,001*EXP(<br>((-1)*0,22)*V)))|((1,09+(6,47*EXP(((-<br>1)*0,046)*V)))+(15,001*EXP(<br>((-1)*0,22)*V)))|((1,09+(6,47*EXP(((-<br>1)*0,046)*V)))+(15,001*EXP(<br>((-1)*0,22)*V)))|((1,09+(6,47*EXP(((-<br>1)*0,046)*V)))+(15,001*EXP(<br>((-1)*0,22)*V)))|
|Motor de buses<br>interurbanos<br>diésel tipo 3<br>(EURO III)|NOx|((5,305+(21,88*EXP(((-<br>1)*0,053)*V)))+(90,055*EXP(<br>((-1)*0,248)*V)))|((5,305+(21,88*EXP(((-<br>1)*0,053)*V)))+(90,055*EXP(<br>((-1)*0,248)*V)))|((5,305+(21,88*EXP(((-<br>1)*0,053)*V)))+(90,055*EXP(<br>((-1)*0,248)*V)))|((5,305+(21,88*EXP(((-<br>1)*0,053)*V)))+(90,055*EXP(<br>((-1)*0,248)*V)))|
|Motor de buses<br>interurbanos<br>diésel tipo 3<br>(EURO III)|COV|(0,227+(15,662/(1+EXP((((-<br>1)*-<br>0,5308)+(0,649*LN(V)))+<br>(0,027*V)))))|(0,227+(15,662/(1+EXP((((-<br>1)*-<br>0,5308)+(0,649*LN(V)))+<br>(0,027*V)))))|(0,227+(15,662/(1+EXP((((-<br>1)*-<br>0,5308)+(0,649*LN(V)))+<br>(0,027*V)))))|(0,227+(15,662/(1+EXP((((-<br>1)*-<br>0,5308)+(0,649*LN(V)))+<br>(0,027*V)))))|
|Motor de<br>vehículos<br>comerciales<br>diésel tipo 2<br>(EURO III)|MP10 <br>MP2,5<br>MPS|0,67*(0,000045*V2-<br>0,004885*V+0,1932)|(4)|g/veh-km|V: Velocidad<br>camión (km/h)|
|Motor de<br>vehículos<br>comerciales<br>diésel tipo 2<br>(EURO III)|SO2 <br>(CC)|0,0198*V2-2,506*V+137,42|0,0198*V2-2,506*V+137,42|0,0198*V2-2,506*V+137,42|0,0198*V2-2,506*V+137,42|
|Motor de<br>vehículos<br>comerciales<br>diésel tipo 2<br>(EURO III)|CO|0,82*(0,000223*V2-<br>0,026*V+1,076)|0,82*(0,000223*V2-<br>0,026*V+1,076)|0,82*(0,000223*V2-<br>0,026*V+1,076)|0,82*(0,000223*V2-<br>0,026*V+1,076)|
|Motor de<br>vehículos<br>comerciales<br>diésel tipo 2<br>(EURO III)|NOx|0.84*(0,000241*V2-<br>0,03181*V+2,0247)|0.84*(0,000241*V2-<br>0,03181*V+2,0247)|0.84*(0,000241*V2-<br>0,03181*V+2,0247)|0.84*(0,000241*V2-<br>0,03181*V+2,0247)|
|Motor de<br>vehículos<br>comerciales<br>diésel tipo 2<br>(EURO III)|COV|0,62*(0,0000175*V2-<br>0,00284*V+0,2162)|0,62*(0,0000175*V2-<br>0,00284*V+0,2162)|0,62*(0,0000175*V2-<br>0,00284*V+0,2162)|0,62*(0,0000175*V2-<br>0,00284*V+0,2162)|
|<br>||E= FEaj∙FC∙P|(4)|<br>g/h|<br>FEaj: Factor de<br>Emisión|

_**Inventario y modelación de emisiones ATM003-22**_ _21/95_

_Junio, 2023_

|Fuente<br>Emisora|Factor|Col3|Ref.|Unidad|Variables|
|---|---|---|---|---|---|
|Motor de<br>maquinarias||FEaj= FEEE∙TAF∙FD <br>FD= 1+ A <br>FEajMP10= FEaj−SMPaj <br>FEajMP2,5= FEajMP10∙0, 97 <br>SMPaj= BSCF∙7∙soxcnv∙0, 01<br>∙(soxbas<br>−soxdsl) <br>FE SO2 = (BSCF∙(1 −soxcnv)<br>−FEHCaj) ∙0,01<br>∗soxdsl∙2|||Ajustado (g/kW-<br>h)|
|Motor de<br>maquinarias||FEaj= FEEE∙TAF∙FD <br>FD= 1+ A <br>FEajMP10= FEaj−SMPaj <br>FEajMP2,5= FEajMP10∙0, 97 <br>SMPaj= BSCF∙7∙soxcnv∙0, 01<br>∙(soxbas<br>−soxdsl) <br>FE SO2 = (BSCF∙(1 −soxcnv)<br>−FEHCaj) ∙0,01<br>∗soxdsl∙2|||FC: Factor de<br>Carga|
|Motor de<br>maquinarias||FEaj= FEEE∙TAF∙FD <br>FD= 1+ A <br>FEajMP10= FEaj−SMPaj <br>FEajMP2,5= FEajMP10∙0, 97 <br>SMPaj= BSCF∙7∙soxcnv∙0, 01<br>∙(soxbas<br>−soxdsl) <br>FE SO2 = (BSCF∙(1 −soxcnv)<br>−FEHCaj) ∙0,01<br>∗soxdsl∙2|||P: Potencia de la<br>maquina (kw)|
|Motor de<br>maquinarias||FEaj= FEEE∙TAF∙FD <br>FD= 1+ A <br>FEajMP10= FEaj−SMPaj <br>FEajMP2,5= FEajMP10∙0, 97 <br>SMPaj= BSCF∙7∙soxcnv∙0, 01<br>∙(soxbas<br>−soxdsl) <br>FE SO2 = (BSCF∙(1 −soxcnv)<br>−FEHCaj) ∙0,01<br>∗soxdsl∙2|||FEEE: Factor de<br>Emisión en<br>Estado<br>Estacionario de<br>Equipo Nuevo<br>(g/kW-h)|
|Motor de<br>maquinarias||FEaj= FEEE∙TAF∙FD <br>FD= 1+ A <br>FEajMP10= FEaj−SMPaj <br>FEajMP2,5= FEajMP10∙0, 97 <br>SMPaj= BSCF∙7∙soxcnv∙0, 01<br>∙(soxbas<br>−soxdsl) <br>FE SO2 = (BSCF∙(1 −soxcnv)<br>−FEHCaj) ∙0,01<br>∗soxdsl∙2|||TAF: Factor de<br>ajuste<br>transiente|
|Motor de<br>maquinarias||FEaj= FEEE∙TAF∙FD <br>FD= 1+ A <br>FEajMP10= FEaj−SMPaj <br>FEajMP2,5= FEajMP10∙0, 97 <br>SMPaj= BSCF∙7∙soxcnv∙0, 01<br>∙(soxbas<br>−soxdsl) <br>FE SO2 = (BSCF∙(1 −soxcnv)<br>−FEHCaj) ∙0,01<br>∗soxdsl∙2|||FD: Factor de<br>deterioro|
|Motor de<br>maquinarias||FEaj= FEEE∙TAF∙FD <br>FD= 1+ A <br>FEajMP10= FEaj−SMPaj <br>FEajMP2,5= FEajMP10∙0, 97 <br>SMPaj= BSCF∙7∙soxcnv∙0, 01<br>∙(soxbas<br>−soxdsl) <br>FE SO2 = (BSCF∙(1 −soxcnv)<br>−FEHCaj) ∙0,01<br>∗soxdsl∙2|||A: Factor<br>empírico “A” del<br>factor de<br>deterioro|
|Motor de<br>maquinarias||FEaj= FEEE∙TAF∙FD <br>FD= 1+ A <br>FEajMP10= FEaj−SMPaj <br>FEajMP2,5= FEajMP10∙0, 97 <br>SMPaj= BSCF∙7∙soxcnv∙0, 01<br>∙(soxbas<br>−soxdsl) <br>FE SO2 = (BSCF∙(1 −soxcnv)<br>−FEHCaj) ∙0,01<br>∗soxdsl∙2|||SMPaj: Ajuste de<br>MP por<br>contenido de<br>Azufre (g/kW-h)|
|Motor de<br>maquinarias||FEaj= FEEE∙TAF∙FD <br>FD= 1+ A <br>FEajMP10= FEaj−SMPaj <br>FEajMP2,5= FEajMP10∙0, 97 <br>SMPaj= BSCF∙7∙soxcnv∙0, 01<br>∙(soxbas<br>−soxdsl) <br>FE SO2 = (BSCF∙(1 −soxcnv)<br>−FEHCaj) ∙0,01<br>∗soxdsl∙2|||BSCF: Consumo<br>especifico de<br>combustible de<br>freno (g/kW-h)|
|Motor de<br>maquinarias||FEaj= FEEE∙TAF∙FD <br>FD= 1+ A <br>FEajMP10= FEaj−SMPaj <br>FEajMP2,5= FEajMP10∙0, 97 <br>SMPaj= BSCF∙7∙soxcnv∙0, 01<br>∙(soxbas<br>−soxdsl) <br>FE SO2 = (BSCF∙(1 −soxcnv)<br>−FEHCaj) ∙0,01<br>∗soxdsl∙2|||7: Ratio en<br>gramos de<br>sulfato en el MP<br>por gramos de<br>azufre en el MP|
|Motor de<br>maquinarias||FEaj= FEEE∙TAF∙FD <br>FD= 1+ A <br>FEajMP10= FEaj−SMPaj <br>FEajMP2,5= FEajMP10∙0, 97 <br>SMPaj= BSCF∙7∙soxcnv∙0, 01<br>∙(soxbas<br>−soxdsl) <br>FE SO2 = (BSCF∙(1 −soxcnv)<br>−FEHCaj) ∙0,01<br>∗soxdsl∙2|||Soxcnv : Ratio<br>de gramos de<br>azufre en MP<br>por gramos de<br>azufre en<br>combustible|
|Motor de<br>maquinarias||FEaj= FEEE∙TAF∙FD <br>FD= 1+ A <br>FEajMP10= FEaj−SMPaj <br>FEajMP2,5= FEajMP10∙0, 97 <br>SMPaj= BSCF∙7∙soxcnv∙0, 01<br>∙(soxbas<br>−soxdsl) <br>FE SO2 = (BSCF∙(1 −soxcnv)<br>−FEHCaj) ∙0,01<br>∗soxdsl∙2|||0,01 :<br>Conversión de<br>porcentaje a<br>fracción|
|Motor de<br>maquinarias||FEaj= FEEE∙TAF∙FD <br>FD= 1+ A <br>FEajMP10= FEaj−SMPaj <br>FEajMP2,5= FEajMP10∙0, 97 <br>SMPaj= BSCF∙7∙soxcnv∙0, 01<br>∙(soxbas<br>−soxdsl) <br>FE SO2 = (BSCF∙(1 −soxcnv)<br>−FEHCaj) ∙0,01<br>∗soxdsl∙2|||Soxbas :<br>Contenido de<br>azufre del<br>combustible<br>utilizado en la<br>certificación [%]|
|Motor de<br>maquinarias||FEaj= FEEE∙TAF∙FD <br>FD= 1+ A <br>FEajMP10= FEaj−SMPaj <br>FEajMP2,5= FEajMP10∙0, 97 <br>SMPaj= BSCF∙7∙soxcnv∙0, 01<br>∙(soxbas<br>−soxdsl) <br>FE SO2 = (BSCF∙(1 −soxcnv)<br>−FEHCaj) ∙0,01<br>∗soxdsl∙2|||Soxdsl:<br>Contenido de<br>azufre del|

_**Inventario y modelación de emisiones ATM003-22**_ _22/95_

_Junio, 2023_

|Fuente<br>Emisora|Factor|Col3|Ref.|Unidad|Variables|
|---|---|---|---|---|---|
||||||combustible<br>utilizado por el<br>usuario [%]|
|Grupo<br>electrógeno<br>menor 600 HP|MP2,5 <br>MP10 <br>MPS|0,006078|(4)|kg/kg-<br>combusti<br>ble<br>|--|
|Grupo<br>electrógeno<br>menor 600 HP|NOx|0,086470|0,086470|0,086470|0,086470|
|Grupo<br>electrógeno<br>menor 600 HP|CO|0,018627|0,018627|0,018627|0,018627|
|Grupo<br>electrógeno<br>menor 600 HP|SO2|0,005686|0,005686|0,005686|0,005686|
|Grupo<br>electrógeno<br>menor 600 HP|COV|0,007060|0,007060|0,007060|0,007060|

(1) Factor obtenido desde AP42, 5th Edition: Capítulo 11, sección 11.9 “Western Surface Coal Mining”
(2) desde Capítulo 13, sección 13.2.4 “Aggregate Handling and Storage Piles”
(3) Factor obtenido desde AP42, 5th Edition: Capítulo 13, sección 13.2.1 “Paved Road”
(4) Factor obtenido desde Manual para el desarrollo de inventarios de emisiones atmosféricas (MMA 2017)

_**Inventario y modelación de emisiones ATM003-22**_ _23/95_

_Junio, 2023_

En la siguiente tabla se presentan los valores considerados en aquellos factores de
emisión que poseen variables para el escenario de estudio.

_**Tabla N° 10**_
_**Valores Considerados en los Factores de Emisión**_

|Fuente Emisora|Variables|Valor|Ref.|Col5|
|---|---|---|---|---|
|Compactación|k: Factor tamaño de partícula MP2,5|0,105|(5)|(5)|
|Compactación|k: Factor tamaño de partícula MP10|0,750|(5)|(5)|
|Compactación|k: Factor tamaño de partícula MPS|1,00|(5)|(5)|
|Compactación|f: % de finos del material|8,5|(6)|(6)|
|Compactación|H: % humedad del material|6,5|(6)|(6)|
|Nivelación|k: Factor tamaño de partícula MP2,5|0,031|(5)|(5)|
|Nivelación|k: Factor tamaño de partícula MP10|0,600|(5)|(5)|
|Nivelación|k: Factor tamaño de partícula MPS|1,000|(5)|(5)|
|Nivelación|V: Velocidad media de niveladora (km/h)|11,4|(6)|(6)|
|Excavación|k: Factor tamaño de partícula MP2,5|0,105|(5)|(5)|
|Excavación|k: Factor tamaño de partícula MP10|0,75|(5)|(5)|
|Excavación|k: Factor tamaño de partícula MPS|1,00|(5)|(5)|
|Excavación|f: % de finos del material|8,5|(6)|(6)|
|Excavación|H: % humedad del material|6,5|(6)|(6)|
|Carga y descarga de<br>material|k: Factor tamaño de partícula MP2,5|0,053|(7)|(7)|
|Carga y descarga de<br>material|k: Factor tamaño de partícula MP10|0,350|(7)|(7)|
|Carga y descarga de<br>material|k: Factor tamaño de partícula MPS|0,740|(7)|(7)|
|Carga y descarga de<br>material|H: Humedad del material (%)|6,5|(6)|(6)|
|Carga y descarga de<br>material|u: Velocidad del viento (m/s)|5,0|(6)|(6)|
|Fugitivas caminos<br>pavimentados|k: Factor tamaño de partícula MP2,5|0,15|(8)|(8)|
|Fugitivas caminos<br>pavimentados|k: Factor tamaño de partícula MP10|0,62|(8)|(8)|
|Fugitivas caminos<br>pavimentados|k: Factor tamaño de partícula MPS|3,23|(8)|(8)|
|Fugitivas caminos<br>pavimentados|f: % de finos del material caminos interiores y<br>acceso|0,7|(6)|(6)|
|Fugitivas caminos<br>pavimentados|W: Peso promedio flota camiones|-|(9)|(9)|
|Motor de Maquinarias|FEee: Factor Emisión >56 a 75 kw MP10 -MPS<br>(g/kw-h) Tier 3|0,40|(10)|(10)|

_**Inventario y modelación de emisiones ATM003-22**_ _24/95_

_Junio, 2023_

|Fuente Emisora|Variables|Valor|Ref.|
|---|---|---|---|
||FEee: Factor Emisión >75 a 130 kw MP10 -MPS<br>(g/kw-h) Tier 2|0,20|(10)|
||FEee: Factor Emisión >75 a 130 kw MP10 -MPS<br>(g/kw-h) Tier 3|0,30|(10)|
||FEee: Factor Emisión >130 a 225 kw MP10 -MPS<br>(g/kw-h) Tier 3|0,20|(10)|
||FEee: Factor Emisión >225 a 450 kw MP10 -MPS<br>(g/kw-h) Tier 3|0,20|(10)|
||FEee: Factor Emisión >56 a 75 kw MP2,5 (g/kw-h)<br>Tier 3|0,39|(10)|
||FEee: Factor Emisión >75 a 130 kw MP2,5 (g/kw-<br>h) Tier 2|0,19|(10)|
||FEee: Factor Emisión >75 a 130 kw MP2,5 (g/kw-<br>h) Tier 3|0,29|(10)|
||FEee: Factor Emisión >130 a 225 kw MP2,5 (g/kw-<br>h)|0,19|(10)|
||FEee: Factor Emisión >225 a 450 kw MP2,5 (g/kw-<br>h) Tier 3|0,19|(10)|
||FEee: Factor Emisión >56 a 75 kw NOX (g/kw-h)<br>Tier 3|4,00|(10)|
||FEee: Factor Emisión >75 a 130 kw NOX (g/kw-h)<br>Tier 2|5,50|(10)|
||FEee: Factor Emisión >75 a 130 kw NOX (g/kw-h)<br>Tier 3|3,00|(10)|
||FEee: Factor Emisión >130 a 225 kw NOX (g/kw-<br>h) Tier 3|3,00|(10)|
||FEee: Factor Emisión >225 a 450 kw NOX (g/kw-<br>h) Tier 3|3,00|(10)|
||>56 a 75 kw<br>Tier 3|3,20|(10)|
||>75 a 130 kw<br>Tier 2|1,20|(10)|
||>75 a 130 kw<br>Tier 3|1,20|(10)|
||>130 a 225 kw<br>Tier 3|1,00|(10)|
||>225 a 450 kw<br>Tier 3|1,10|(10)|
||FEee: Factor Emisión >56 a 75 kw HC (g/kw-h)<br>Tier 3|0,2|(10)|
||FEee: Factor Emisión >75 a 130 kw HC (g/kw-h)<br>Tier 2|0,5|(10)|
||FEee: Factor Emisión >75 a 130 kw HC (g/kw-h)<br>Tier 3|0,2|(10)|
||FEee: Factor Emisión >130 a 225 kw HC (g/kw-h)<br>Tier 3|0,2|(10)|
||FEee: Factor Emisión >225 a 450 kw HC (g/kw-h)<br>Tier 3|0,2|(10)|
||C: Factor de Carga|0,59|(10)|
||TAF: Factor de ajuste transiente MP2,5-MP10 -MPS<br>Bulldozer|2,4|(10)|

_**Inventario y modelación de emisiones ATM003-22**_ _25/95_

_Junio, 2023_

|Fuente Emisora|Variables|Valor|Ref.|
|---|---|---|---|
||TAF: Factor de ajuste transiente MP2,5-MP10 -MPS<br>Camiones Fuera de Carretera|1,5|(10)|
||TAF: Factor de ajuste transiente MP2,5-MP10 -MPS<br>Cargador Frontal|2,4|(10)|
||TAF: Factor de ajuste transiente MP2,5-MP10 -MPS<br>Excavadoras|1,5|(10)|
||TAF: Factor de ajuste transiente MP2,5-MP10 -MPS<br>Rodillos|2,0|(10)|
||TAF: Factor de ajuste transiente MP2,5-MP10 -MPS<br>Motoniveladora|1,5|(10)|
||TAF: Factor de ajuste transiente CO Bulldozer|2,6|(10)|
||TAF: Factor de ajuste transiente CO Camiones<br>Fuera de Carretera|1,5|(10)|
||TAF: Factor de ajuste transiente CO Cargador<br>Frontal|2,6|(10)|
||TAF: Factor de ajuste transiente CO Excavadoras|1,5|(10)|
||TAF: Factor de ajuste transiente CO Rodillos|2,6|(10)|
||TAF: Factor de ajuste transiente CO<br>Motoniveladora|1,5|(10)|
||TAF: Factor de ajuste transiente NOX Bulldozer|1,2|(10)|
||TAF: Factor de ajuste transiente NOX Camiones<br>Fuera de Carretera|1,0|(10)|
||TAF: Factor de ajuste transiente NOX Cargador<br>Frontal|1,2|(10)|
||TAF: Factor de ajuste transiente NOX Excavadoras|1,0|(10)|
||TAF: Factor de ajuste transiente NOX Rodillos|1,1|(10)|
||TAF: Factor de ajuste transiente NOX <br>Motoniveladora|1,2|(10)|
||TAF: Factor de ajuste transiente HC Bulldozer|2,3|(10)|
||TAF: Factor de ajuste transiente HC Camiones<br>Fuera de Carretera|1,1|(10)|
||TAF: Factor de ajuste transiente HC Cargador<br>Frontal|2,3|(10)|
||TAF: Factor de ajuste transiente HC Excavadoras|1,1|(10)|
||TAF: Factor de ajuste transiente HC Rodillos|2,3|(10)|
||TAF: Factor de ajuste transiente HC<br>Motoniveladora|1,1|(10)|
||A: Factor empírico “A” del factor de deterioro HC<br>Tier 2|0,034|(10)|
||A: Factor empírico “A” del factor de deterioro CO<br>Tier 2|0,101|(10)|
||A: Factor empírico “A” del factor de deterioro NOX <br>Tier 2|0,009|(10)|
||A: Factor empírico “A” del factor de deterioro MP<br>Tier 2|0,473|(10)|

_**Inventario y modelación de emisiones ATM003-22**_ _26/95_

_Junio, 2023_

|Fuente Emisora|Variables|Valor|Ref.|
|---|---|---|---|
||A: Factor empírico “A” del factor de deterioro HC<br>Tier 3|0,027|(10)|
||A: Factor empírico “A” del factor de deterioro CO<br>Tier 3|0,151|(10)|
||A: Factor empírico “A” del factor de deterioro NOX <br>Tier 3|0,008|(10)|
||A: Factor empírico “A” del factor de deterioro MP<br>Tier 3|0,473|(10)|
||Soxcnv|0,02247|(10)|
||Soxbas|0,330|(10)|
||Soxdsl|0,005|(10)|
|||248|(10)|
|||223|(10)|
|||223|(10)|
|||223|(10)|
|Motor de camiones<br>pesados, medianos,<br>buses interurbanos y<br>vehículos comerciales<br>diésel (EURO III)|v: Velocidad vehículos en caminos pavimentados|70|(11)|

(5) Factor obtenido desde AP42, 5th Edition: Capítulo 11, sección 11.9 “Western Surface Coal Mining”
(6) Factor obtenido desde Guía para la Estimación de Emisiones Atmosféricas en la Región Metropolitana (2020)
(7) Factor obtenido desde AP42, 5th Edition: Capítulo 13, sección 13.2.4 “Aggregate Handling and Storage Piles”
(8) Factor obtenido desde AP42, 5th Edition: Capítulo 13, sección 13.2.1 “Paved Road”
(9) Ver sección 4.4
(10) Valor de referencia obtenido desde el Manual para el desarrollo de inventarios de emisiones atmosféricas,

MMA, 2017
(11) Valor proporcionado por el cliente

_**Inventario y modelación de emisiones ATM003-22**_ _27/95_

_Junio, 2023_

**4.4** **Peso Promedio**

Para fase del proyecto se determinó el peso promedio de la flota de vehículos,
considerando proporciones de acuerdo con el número de viajes que realiza cada
vehículo que circulará por una misma vía:

_PPP_ = _PPC_ - _PV_ (III)

# PPR =  PPP (IV)

Dónde _:_

_PPP_ : Proporción por tipo de vehículo del total de la flota

_PPR_ : Peso medio (t)
_PPC_ : Peso medio asignado a cada tipo de vehículo (t)
_PV_ : (Viajes totales por tipo de vehículo) / (total de viajes de la flota)

**4.4.1** **Peso Promedio Caminos Pavimentados**

Los pesos promedio para la flota de vehículos que circularán por las vías
pavimentadas, en la fase de construcción, operación y cierre se presentan en la
siguiente tabla:

_**Inventario y modelación de emisiones ATM003-22**_ _28/95_

_Junio, 2023_

_**Tabla N° 11**_
_**Peso Promedio Vehículos (t) en Caminos Pavimentados**_

_**Fase de Construcción**_

|Transporte|Peso<br>Medio PPC|N° viajes<br>ida al año|Proporción<br>de viajes<br>(PV)|Proporción<br>por Peso<br>(PPP)|Peso<br>Promedio<br>t (PPR)|
|---|---|---|---|---|---|
|Camión Traslado de maquinaria|26|30|0,0146|0,3790|18|
|Camión Traslado de materiales e insumos|26|32|0,0155|0,4043|0,4043|
|Camión Traslado de hormigón|20|880|0,4276|8,7444|8,7444|
|Bus Traslado de Personal|13|792|0,3848|4,8952|4,8952|
|Material empréstito|22|110|0,0534|1,1759|1,1759|
|Residuos domiciliarios|22|156|0,0758|1,6676|1,6676|
|Residuos industriales no peligrosos|22|52|0,0253|0,5559|0,5559|
|Residuos peligrosos|22|6|0,0029|0,0641|0,0641|

Fuente: Algoritmos SpA, 2023, en base a información entregada por el cliente.

_**Tabla N° 12**_
_**Peso Promedio Vehículos (t) en Caminos Pavimentados**_

_**Fase de Operación**_

|Transporte|Peso Medio PPC|N° viajes ida al<br>año|Proporción de<br>viajes (PV)|Proporción por<br>Peso (PPP)|Peso Promedio<br>t (PPR)|
|---|---|---|---|---|---|
|Camión 3/4 Mantenimiento|13|3|0,0000|0,0000|25|
|Camión 3/4 Retiro de Residuos|13|6|0,0000|0,0000|0,0000|
|Vehículo liviano|3|1.825|0,0230|0,0580|0,0580|
|Camión de carga|26|78.475|0,9770|25,4020|25,4020|

Fuente: Algoritmos SpA, 2023, en base a información entregada por el cliente.

_**Inventario y modelación de emisiones ATM003-22**_ _29/95_

_Junio, 2023_

_**Tabla N° 13**_
_**Peso Promedio Vehículos (t) en Caminos Pavimentados**_

_**Fase de Cierre**_

|Transporte|Peso Medio<br>PPC|N° viajes<br>ida al año|Proporción<br>de viajes<br>(PV)|Proporción<br>por Peso<br>(PPP)|Peso<br>Promedio<br>t (PPR)|
|---|---|---|---|---|---|
|Camión Traslado de maquinaria|26|2|0,0070|0,1820|14|
|Camión Traslado de infraestructura desmantelada|26|20|0,0740|1,9240|1,9240|
|Camión Retiro de residuos industriales no peligroso|22|6|0,0220|0,4840|0,4840|
|Camión Retiro de residuos industriales peligrosos|22|2|0,0070|0,1540|0,1540|
|Bus Traslado de Personal|13|240|0,8890|11,3080|11,3080|

Fuente: Algoritmos SpA, 2023, en base a información entregada por el cliente.

_**Inventario y modelación de emisiones ATM003-22**_ _30/95_

_Junio, 2023_

**4.5** **Nivel de Actividad Etapa de Construcción**

**4.5.1** **Escarpe**

El nivel de actividad corresponde a los kilómetros recorridos por la maquinaria,
determinados a partir de las hectáreas a escarpar, las cuales deben ser
multiplicadas por el factor 3,57 [km/ha].

_**Tabla N° 14**_
_**Nivel de Actividad Escarpe (km/año), Fase Construcción-año 1**_

|Actividad|Área (ha)|Factor (km/ha)|Escarpe<br>(km/año)|
|---|---|---|---|
|Primera Etapa 3t - Escarpe|6,00|3,57|21,42|

Fuente: Algoritmos SpA, 2023, en base a información entregada por el cliente.

**4.5.2** **Compactación**

El nivel de actividad corresponde a las horas de compactación, que se obtienen en
base al área a recorrer, la cual debe ser dividida por el ancho y velocidad de la
compactadora, y multiplicada por el número de pasadas.

_**Tabla N° 15**_
_**Nivel de Actividad Compactación (h/año), Fase Construcción-año 1**_

|Actividad|Area (m2)|No<br>Pasadas|Ancho (m)|Velocidad<br>(km/h)|Compactación<br>(h)|
|---|---|---|---|---|---|
|Primera Etapa 3t<br>Compactación|60.000|5|2,13|12|11,72|

Fuente: Algoritmos SpA, 2023, en base a información entregada por el cliente.

**4.5.3** **Nivelación**

El nivel de actividad está asociado a los kilómetros recorridos por la niveladora,
determinados a partir del área a nivelar, el ancho de la maquinaria y el número de
pasadas. En la siguiente Tabla se presentan los kilómetros recorridos en la actividad
de nivelación.

_**Tabla N° 16**_
_**Nivel de Actividad Nivelación (km), Fase Construcción-año 1**_

|Actividad|Área de<br>Trabajo (m2)|Ancho<br>Niveladora<br>(m)|N° Pasadas|km recorridos|
|---|---|---|---|---|
|Primera Etapa 3t<br>Nivelación|60.000|3,70|5|81,08|

Fuente: Algoritmos SpA, 2023, en base a información entregada por el cliente

_**Inventario y modelación de emisiones ATM003-22**_ _31/95_

_Junio, 2023_

**4.5.4** **Excavación**

El nivel de actividad se determina dividiendo el volumen a excavar por el
rendimiento de la maquinaria utilizada en la excavación. Se considera que para una
máquina con capacidad de palada de 1,1 [m [3] ], se tiene un rendimiento igual a 66,3

[m [3] /h]. En la siguiente tabla se presenta el volumen a excavar y las horas de
excavación que se destinarán durante la fase del proyecto.

_**Tabla N° 17**_
_**Nivel de Actividad Horas de Excavación (h/año), Fase Construcción-año 1**_

|Actividad|Volúmen a excavar<br>(m3/año)|Horas de excavación<br>(h/año)|
|---|---|---|
|Primera Etapa 3t -<br>Excavación|16.680|251|
|Segunda Etapa 2t -<br>Excavación|11.120|168|

Fuente: Algoritmos SpA, 2023, en base a información entregada por el cliente.

**4.5.5** **Carga y Descarga de Material**

El nivel de actividad asociado a la carga y descarga del material, está definido por
la cantidad de material en el proceso, en toneladas al año.

La siguiente tabla presenta la cantidad de material a cargar y descargar (t/año)
para el primer año en la fase de Construcción.

_**Tabla N° 18**_
_**Nivel de Actividad Carga y Descarga de material (t/año),**_

_**Fase Construcción-año 1**_

|Actividad|Material (t/año)|
|---|---|
|Primera Etapa 3t - Carga y Descarga|37.530|
|Segunda Etapa 2t - Carga y Descarga|12.510|

Fuente: Algoritmos SpA, 2023, en base a información entregada por el cliente

_**Inventario y modelación de emisiones ATM003-22**_ _32/95_

_Junio, 2023_

**4.5.6** **Tránsito de Vehículos por Tipo de Carpeta.**

Para determinar el nivel de actividad asociado al tránsito de vehículos por caminos,
se requiere obtener los kilómetros totales recorridos por cada tipo de vehículo. Para
ello se ha considerado la siguiente ecuación (V):

_KTR_ = _VT_  _DR_ (V)
Dónde:

KTR : Kilómetros totales recorridos al año ida y vuelta (veh-km/año)
VT : Viajes totales (ida + vuelta) al año por tipo de vehículo (veh/año)

DR : Distancia recorrida en cada viaje de ida (km.)

Para estimar los viajes totales (ida + vuelta) al año que realizan los camiones y
vehículos, se consideró la siguiente ecuación (VI):

 _M_ 

_VT_ = 2 (VI)

 _CP_ 

Dónde:

VT : Viajes totales (ida + vuelta) al año por tipo de vehículo (veh/año)

M : Cantidad de material a transportar (t)
CP : Capacidad de carga del camión (t)

**4.5.6.1** **Tránsito de Vehículos Camino Pavimentado**

Las siguientes tablas presentan la cantidad de viajes ida al año por tipo de vehículo,
la distancia recorrida en cada viaje de ida y el nivel de actividad obtenidos al aplicar
la ecuación (V) y ecuación (VI) en caminos pavimentados para cada fase del
proyecto.

En la estimación de los kilómetros totales recorridos que realiza cada vehículo se
consideraron tanto los viajes de ida como los de vuelta.

_**Inventario y modelación de emisiones ATM003-22**_ _33/95_

_Junio, 2023_

_**Tabla N° 19**_
_**Cálculo del Nivel de Actividad para Tránsito de Vehículos**_
_**por Caminos Pavimentados (veh-km/año), Fase Construcción**_

|Transporte|Viajes<br>Año 1|Viajes<br>Año 2|Distancia<br>Camino<br>Pavimentado<br>(km)|Kilómetro<br>s Totales<br>(veh-<br>km/año)<br>[KTR] Año<br>1|Kilómetros<br>Totales<br>(veh-<br>km/año)<br>[KTR] Año<br>2|
|---|---|---|---|---|---|
|Camión Traslado de<br>maquinaria|30|0|11,82|709|0|
|Camión Traslado de<br>materiales e insumos|32|32|11,82|756|756|
|Camión Traslado de hormigón|880|0|11,82|20.803|0|
|Bus Traslado de Personal|792|792|11,82|18.723|18.723|
|Material empréstito|110|0|11,82|2.600|0|
|Residuos domiciliarios|156|156|11,82|3.688|3.688|
|Residuos industriales no<br>peligrosos|52|52|11,82|1.229|1.229|
|Residuos peligrosos|6|6|11,82|142|142|

Fuente: Algoritmos SpA, 2023, en base a información entregada por el cliente

**4.5.7** **Motor de Vehículos**

Para determinar el nivel de actividad asociado a la combustión interna de motores
de vehículos debido al tránsito por caminos se requiere obtener los kilómetros
totales recorridos por cada tipo de vehículo. Para ello se han considerado los
valores presentados en la sección anterior.

**4.5.8** **Motor de Maquinarias**

Para determinar el nivel de actividad asociado a la combustión interna de cada
motor de maquinarias se requiere obtener las horas de funcionamiento al año. Para
ello se ha considerado la siguiente ecuación (VII):

_HF_ = _C_  _HD_  _DA_ (VII)
Dónde:

HF : Horas de funcionamiento al año (h/año)

C : Cantidad de maquinarias
HD : Horas de funcionamiento al día por cada maquinaria (h/día)
DA : Días de funcionamiento al año por cada maquinaria (días/año)

En la siguiente tabla se presenta el tipo de maquinaria a utilizar, la potencia (HP)
y el nivel de actividad HF (h/año) obtenido al aplicar la ecuación (VII) para los
escenarios del Proyecto COPEC Mejillones.

_**Inventario y modelación de emisiones ATM003-22**_ _34/95_

_Junio, 2023_

_**Tabla N° 20**_
_**Cálculo del Nivel de Actividad para Motor de Maquinarias (h/año),**_

_**Fase Construcción- Año 1 y 2**_

|Actividad|Tipo de Maquinaria|(h/año 1)|(h/año 2)|Potencia<br>(kw)|
|---|---|---|---|---|
|Primera<br>Etapa 3t<br>Motor de<br>Maquinarias|Compactadora CAT CS533E|468|--|97|
|Primera<br>Etapa 3t<br>Motor de<br>Maquinarias|Motoniveladora CAT 120/120 AWD|468|--|93|
|Primera<br>Etapa 3t<br>Motor de<br>Maquinarias|Excavadora JCB 3CX 4X4 GLOBAL|702|--|69|
|Primera<br>Etapa 3t<br>Motor de<br>Maquinarias|Bulldozer CAT D6T|2.106|--|149|
|Primera<br>Etapa 3t<br>Motor de<br>Maquinarias|Cargador frontal JCB 422ZX|1.404|--|94|
|Primera<br>Etapa 3t<br>Motor de<br>Maquinarias|Fratasadora WACKER NEUSON<br>CT48-8A|936|546|6|
|Segunda<br>Etapa 2t<br>Motor de<br>Maquitarias|Motoniveladora CAT 120/120 AWD|468|--|93|
|Segunda<br>Etapa 2t<br>Motor de<br>Maquitarias|Excavadora JCB 3CX 4X4 GLOBAL|468|--|69|
|Segunda<br>Etapa 2t<br>Motor de<br>Maquitarias|Cargador frontal JCB 422ZX|468|--|94|
|Segunda<br>Etapa 2t<br>Motor de<br>Maquitarias|Fratasadora WACKER NEUSON<br>CT48-8A|936|546|6|

Fuente: Algoritmos SpA, 2023, en base a información entregada por el cliente

**4.5.9** **Grupo Electrógeno**

El nivel de actividad corresponde al consumo de combustible diésel que serán
utilizados durante la fase de construcción.

La siguiente tabla presenta cantidad, horas de funcionamiento al año y Consumo
combustible diésel para la fase del proyecto.

_**Tabla N° 21**_
_**Cálculo del Nivel de Actividad para Grupos Electrógenos**_

_**Fase Construcción-Año 1 y 2**_

|Actividad|Cantidad|h/año|Consumo<br>Comb<br>(l/h)|Densidad<br>Diésela<br>(kg/l)|Consumo<br>(kg de<br>Comb/<br>año 1)|Consumo<br>(kg de<br>Comb/<br>año 2)|
|---|---|---|---|---|---|---|
|Primera Etapa 3t<br>GE110 kva|1|2.340|26|0,84|51.106|29.812|
|Segunda Etapa 2t<br>GE 110 kva|1|1.872|26|0,84|40.884|23.849|

Fuente: Algoritmos SpA, 2023

Densidad Obtenida de Guia Metodológica para la Estimación de Emisiones provenientes de Fuentes Puntuales.

_**Inventario y modelación de emisiones ATM003-22**_ _35/95_

_Junio, 2023_

**4.6** **Nivel de actividad Etapa de Operación**

**4.6.1** **Tránsito de Vehículos por tipo de carpeta.**

**4.6.1.1** **Tránsito de Vehículos camino pavimentado**

La siguiente tabla presenta la cantidad de viajes al año por tipo de vehículo, la
distancia recorrida en cada viaje y el nivel de actividad obtenidos al aplicar la
ecuación (V) y ecuación (VI) en caminos pavimentados utilizados durante la fase
de operación del proyecto.

_**Tabla N° 22**_
_**Cálculo del Nivel de Actividad para Tránsito de Vehículos**_
_**por Caminos Pavimentados (veh-km/año), Fase Operación**_

|Transporte|Viajes|Distancia Camino<br>Pavimentado<br>(km)|Kilómetros Totales<br>(veh-km/año)<br>[KTR]|
|---|---|---|---|
|Camión 3/4 Mantenimiento|6|11,82|71|
|Camión 3/4 Retiro de Residuos|12|11,82|142|
|Vehículo liviano|3650|11,82|43.143|
|Vehículo de carga|156.950|11,82|1.855.149|

Fuente: Algoritmos SpA, 2023, en base a información entregada por el cliente

**4.6.2** **Motor de Vehículos**

Para determinar el nivel de actividad asociado a la combustión interna de motores
de vehículos debido al tránsito por caminos se requiere obtener los kilómetros
totales recorridos por cada tipo de vehículo. Para ello se han considerado los
valores presentados en la sección anterior 4.6.1.

_**Inventario y modelación de emisiones ATM003-22**_ _36/95_

_Junio, 2023_

**4.7** **Nivel de actividad Etapa de Cierre**

**4.7.1** **Tránsito de Vehículos por tipo de carpeta.**

**4.7.1.1** **Tránsito de Vehículos camino pavimentado**
La siguiente tabla presenta la cantidad de viajes al año por tipo de vehículo, la
distancia recorrida en cada viaje y el nivel de actividad obtenidos al aplicar la
ecuación (V) y ecuación (VI) en caminos pavimentados utilizados durante la fase
de cierre del proyecto.

_**Tabla N° 23**_
_**Cálculo del Nivel de Actividad para Tránsito de Vehículos**_

_**por Caminos Pavimentados (veh-km/año), Fase Cierre**_

|Transporte|Viajes|Distancia<br>Camino<br>Pavimentado<br>(km)|Kilómetros<br>Totales<br>(veh-<br>km/año)<br>[KTR]|
|---|---|---|---|
|Camión Traslado de maquinaria|4|11,82|47|
|Camión Traslado de infraestructura<br>desmantelada|40|11,82|473|
|Camión Retiro de residuos industriales no<br>peligroso|12|11,82|142|
|Camión Retiro de residuos industriales<br>peligrosos|4|11,82|47|
|Bus Traslado de Personal|480|11,82|5.674|

Fuente: Algoritmos SpA, 2023, en base a información entregada por el cliente

**4.7.2** **Motor de Vehículos**

Para determinar el nivel de actividad asociado a la combustión interna de motores
de vehículos debido al tránsito por caminos se requiere obtener los kilómetros
totales recorridos por cada tipo de vehículo. Para ello se han considerado los
valores presentados en la sección anterior 4.7.1.

_**Inventario y modelación de emisiones ATM003-22**_ _37/95_

_Junio, 2023_

**4.8** **Tasas de Emisión Escenario con Proyecto**

Al multiplicar los factores de emisión presentados en la sección 4.3 con los niveles
de actividad definidos en las secciones 4.5, 4.6 y 4.7se obtienen las tasas de
emisión anuales de MP 10, MP 2,5, MPS y gases SO 2, NO x, CO y COV del Proyecto
COPEC Mejillones.

A continuación, en las siguientes tablas, se encuentra el resumen de total de las
emisiones generadas durante la fase construcción, operación y construcción.

_**Inventario y modelación de emisiones ATM003-22**_ _38/95_

_Junio, 2023_

_**Tabla N° 24**_
_**Tasas de Emisión Fase Construcción Año 1 (t/año)**_

|Fuente|SO<br>2|NO<br>X|CO|MP<br>2.5|MP<br>10|MPS|COVs|Unidad|
|---|---|---|---|---|---|---|---|---|
|Escarpe|--|--|--|0,02|0,12|0,12|--|t/año|
|Compactación|--|--|--|0,01|0,01|0,06|--|t/año|
|Nivelación|--|--|--|0,13|0,26|1,25|--|t/año|
|Excavación|--|--|--|0,00|0,04|0,12|--|t/año|
|Carga y descarga de material|--|--|--|0,00|0,02|0,03|--|t/año|
|Transito camino pavimentado|--|--|--|0,10|0,41|2,15|--|t/año|
|Motor vehículos Caminos pavimentados|<0,01|0,28|0,07|0,01|0,01|0,01|0,01|t/año|
|Motor maquinaria|<0,01|1,59|1,42|0,28|0,29|0,29|0,33|t/año|
|Grupo Electrógeno|0,52|7,95|1,71|0,56|0,56|0,56|0,65|t/año|
|**Total**|**0,52**|**9,83**|**3,20**|**1,11**|**1,71**|**4,59**|**0,99**|**t/año**|

Fuente: Algoritmos SpA, 2023

_**Tabla N° 25**_
_**Tasas de Emisión Fase Construcción Año 2 (t/año)**_

|Fuente|SO<br>2|NO<br>X|CO|MP<br>2.5|MP<br>10|MPS|COVs|Unidad|
|---|---|---|---|---|---|---|---|---|
|Transito camino pavimentado|--|--|--|0,06|0,23|1,19|--|t/año|
|Motor vehículos Caminos pavimentados|<0,01|0,14|0,03|0,00|0,00|0,00|0,01|t/año|
|Motor maquinaria|<0,01|0,02|0,02|0,00|0,00|0,00|<0,01|t/año|
|Grupo Electrógeno|0,31|4,64|1,00|0,33|0,33|0,33|0,38|t/año|
|**Total**|**0,31**|**4,81**|**1,05**|**0,39**|**0,56**|**1,52**|**0,39**|**t/año**|

Fuente: Algoritmos SpA, 2023

_**Tabla N° 26**_
_**Tasas de Emisión Fase Operación (t/año)**_

|Fuente|SO<br>2|NO<br>X|CO|MP<br>2.5|MP<br>10|MPS|COVs|Unidad|
|---|---|---|---|---|---|---|---|---|
|Transito camino pavimentado|--|--|--|6,18|25,53|132,98|--|t/año|
|Motor vehículos Caminos pavimentados|0,04|11,15|2,63|0,23|0,23|0,23|0,51|t/año|
|**Total**|**0,04**|**11,15**|**2,63**|**6,41**|**25,76**|**133,21**|**0,51**|**t/año**|

Fuente: Algoritmos SpA, 2023

_**Inventario y modelación de emisiones ATM003-22**_ _39/95_

_Junio, 2023_

_**Tabla N° 27**_
_**Tasas de Emisión Fase Cierre (t/año)**_

|Fuente|SO<br>2|NO<br>X|CO|MP<br>2.5|MP<br>10|MPS|COVs|Unidad|
|---|---|---|---|---|---|---|---|---|
|Transito camino pavimentado|--|--|--|0,01|0,05|0,24|--|t/año|
|Motor vehículos Caminos pavimentados|<0,01|0,04|0,01|<0,01|<0,01|<0,01|<0,01|t/año|
|**Total**|**<0,01**|**0,04**|**0,01**|**0,01**|**0,05**|**0,25**|**<0,01**|**t/año**|

Fuente: Algoritmos SpA, 2023

_**Inventario y modelación de emisiones ATM003-22**_ _40/95_

_Junio, 2023_

**5** **Modelación de Dispersión de Contaminantes**

Con el fin de evaluar la dispersión de los contaminantes generados por las fuentes,
como material particulado (MP 10 ), material particulado respirable fino (MP 2,5 ),
material particulado sedimentable (MPS), dióxido de azufre (SO 2 ), óxidos de
nitrógeno (NO X ) y monóxido de carbono (CO) para la fase de operación del
Proyecto, se realizó una modelación de dispersión de contaminantes considerando
las emisiones generadas.

**5.1** **Modelo de Dispersión Atmosférica**

**5.1.1** **Base Teórica**

La aplicación de modelos de dispersión atmosférica permite determinar el aporte
de las emisiones provenientes de fuentes emisoras, en localidades y sectores
aledaños a las instalaciones de un determinado proyecto, permitiendo de este
modo, asignar las cuotas de responsabilidad en los niveles de calidad del aire
medidos en su entorno.

Los modelos lagrangianos se caracterizan por hacer uso de un sistema de
referencia que se ajusta al movimiento atmosférico. Es decir, las emisiones,
reacciones, deposición y mezclado de los contaminantes se analizan para un
volumen de aire que va cambiando su posición, de acuerdo con la velocidad y
dirección del viento. Bajo este esquema general, los modelos lagrangianos se
pueden clasificar como modelos de trayectoria y modelos gaussianos, de acuerdo
con la geometría del sistema de modelación. Los modelos de trayectoria pueden
simular los procesos para una columna hipotética de aire, en cambio, cuando la
simulación se hace para una pluma de emisión, contínua o discreta, se trata de
modelos gaussianos.

Los modelos gaussianos describen el transporte y mezcla de los contaminantes,
asumiendo que las emisiones presentan, en las direcciones horizontal y vertical,
una distribución normal o de curva gaussiana con una concentración máxima en el
centro de la pluma. Generalmente estos modelos se aplican para evaluar la
dispersión de contaminantes provenientes de fuentes puntuales, aunque también
se aplican para simular emisiones de fuentes de área y de línea. Otra característica
de este tipo de modelos es que normalmente son aplicados para evaluar la
dispersión de contaminantes primarios no reactivos, aunque existen versiones que
incluyen en su formulación consideraciones especiales para poder simular procesos
de deposición y transformación química.

**5.1.2** **Sistema de Modelación WRF - CALPUFF**

Para determinar el efecto que tendrán las emisiones de material particulado y gases
provenientes de la operación del Proyecto, se utiliza un sistema acoplado de dos
modelos: El modelo atmosférico Weather Research and Forecasting (WRF), y el
modelo CALPUFF, simulador de la dispersión de contaminantes en la atmósfera.
Ambos conforman el sistema de modelación WRF-CALPUFF.

_**Inventario y modelación de emisiones ATM003-22**_ _41/95_

_Junio, 2023_

 - **WRF**

WRF es un modelo numérico de pronóstico e investigación atmosférica,
[desarrollado por las el Centro Nacional para la investigación Atmosférica (NCAR) y](https://es.wikipedia.org/wiki/Centro_Nacional_de_Investigaci%C3%B3n_Atmosf%C3%A9rica)
los Centros Nacionales para la Predicción Medioambiental (NCEP), ambas entidades
norteamericanas. Destaca sobre otros modelos porque considera los efectos de la
superficie terrestre, lo que permite resolver o pronosticar los fenómenos
meteorológicos inducidos o influenciados por esa estructura. Su uso está aceptado
por el Servicio de Evaluación Ambiental en Chile, para ser aplicado dentro del
Sistema de Evaluación de Impacto Ambiental, ya que permite cubrir la necesidad
de ampliar la resolución espacial que poseen las estaciones de monitoreo.

La forma de trabajo de WRF comprende la resolución de las ecuaciones primitivas
de la atmósfera, utilizando una descripción euleriana. Además, es un modelo no
hidrostático, es decir, incluye la variación de presión en el eje vertical de la
atmósfera dentro de sus ecuaciones. Su manejo comprende dos componentes
importantes, el primero de ellos corresponde al WRF Pre-processing System (WPS)
donde se preparan los archivos de entrada para las simulaciones y el WRF Model
(núcleo dinámico) donde se integran las ecuaciones dinámicas y termodinámicas,
modelos de nubes, superficie, radiación, microfísica, entre otros.

Las variables meteorológicas más importantes que inciden en la dispersión de las
emisiones atmosféricas corresponden a la temperatura, velocidad del viento y
estabilidad atmosférica de la localidad sometida a evaluación. Estas variables son
utilizadas como entradas en los modelos de dispersión de contaminantes,
necesarios para predecir y evaluar los impactos ambientales actuales o de futuros
proyectos. Es por esta razón que es necesario introducir los resultados obtenidos
del modelo WRF al modelo CALPUFF.

 - **CALPUFF**

El modelo CALPUFF es un sistema avanzado de modelación meteorológica y de
calidad el aire, no estacionario, desarrollado por Sigma Research Corporation (SRC)
a fines de la década de 1980 (url: http://www.src.com). La versión número cinco
del modelo está aprobada por la Agencia de Protección Ambiental de los Estados
Unidos (EPA), lo que convierte a este modelo en una herramienta ampliamente
utilizada a nivel mundial. De forma particular, al igual que WRF, el modelo CALPUFF
está aprobado por el Servicio de Evaluación Ambiental en Chile, para poder
emplearlo dentro del Sistema de Evaluación de Impacto Ambiental.

CALPUFF modela el transporte y dispersión de contaminantes emitidos por las
fuentes emisoras en forma de paquetes o _puff_ de material, procesándolos a través
del dominio de modelación. Este modelo incluye tres componentes principales:
WRF, CALPUFF y CALPOST, además de una larga selección de preprocesadores,
diseñados para incluir datos meteorológicos y geofísicos en el modelo. WRF simula
campos de viento y temperatura en un dominio de modelación engrillado y
tridimensional. CALPUFF modela la dispersión de contaminantes y CALPOST
procesa las salidas de CALPUFF creando archivos con las tabulaciones necesarias
que permitan la evaluación de resultados.

_**Inventario y modelación de emisiones ATM003-22**_ _42/95_

_Junio, 2023_

**5.2** **Variables de Entrada ingresados al Sistema de Modelación**

El sistema de modelación WRF-CALPUFF requiere de la siguiente información de
entrada:

 **Archivos NCEP-FNL (Final):** Información de entrada para el modelo WRF,
con una resolución espacial de 1 km x 1 km (url:
https://rda.ucar.edu/datasets/ds083.2/).

 - **Uso de Suelo** **[b]** **:** Esta información permite definir los coeficientes de
rugosidad superficial, razón de Bowen y albedo. Los usos de suelo presentes
en el área de estudio se encuentran en la siguiente tabla.

_**Tabla N° 28**_
_**Características del Uso de Suelo**_

|Uso de Suelo|Albedoc|Col3|Razón de Bowend|Col5|Rugosidad<br>Superficial (cm)|Col7|
|---|---|---|---|---|---|---|
|**Uso de Suelo**|**Verano**|**Invierno**|**Verano**|**Invierno**|**Verano**|**Invierno**|
|Bosque Mixto|13|14|0.5|0.5|50|50|
|Mezcla de hierbas|20|24|1|1|11|10|
|Urbano|18|18|1.5|1.5|50|50|
|Escasa<br>vegetación|25|25|1|1|10|10|
|Cuerpos de agua|8|8|0|0|1|1|

Fuente: Algoritmos SpA, 2023

La siguiente figura presenta los usos de suelo presentes en el área de estudio,
indicados en la tabla anterior. Se destaca que la nomenclatura utilizada para definir
las categorías de uso de suelo proviene del modelo WRF-ARW a través de “USGS
24-Category Landuse and Landcover”.

Información obtenida a partir de preprocesador CTGPROC
Albedo: reflectividad a la luz solar del suelo (expresada como fracción respecto a la unidad)
d Razón de Bowen: definida como la razón entre flujos sensibles y latentes, a nivel de superficie.

_**Inventario y modelación de emisiones ATM003-22**_ _43/95_

_Junio, 2023_

_**Figura N° 8**_
_**Uso de Suelo**_

Fuente: Algoritmos SpA, 2023

_**Inventario y modelación de emisiones ATM003-22**_ _44/95_

_Junio, 2023_

- **Data de emisiones**, Corresponde al valor emitido por cada fuente
considerada en los diferentes escenarios de modelación (Ver capítulo 4)

**Ubicación de puntos de interés**, Esto permite la evaluación de los
resultados en comparación con la normativa aplicable. La ubicación de los
puntos de interés considerados se encuentra en la Tabla N° 29. En la Figura
N° 9, se muestra la ubicación de dicho punto.

_**Tabla N° 29**_
_**Localización Puntos Discretos**_ _**[e]**_

|Punto de<br>Interés|Identificación|Tipo de Punto<br>de Interés|Coordenadas UTM|Col5|Elevación (m)|
|---|---|---|---|---|---|
|**Punto de**<br>**Interés**|**Identificación**|**Tipo de Punto**<br>**de Interés**|**Este (m)**|**Norte (m)**|**Norte (m)**|
|1|R1|Receptor<br>Norma Primaria|360.032|7.449.126|42,61|
|2|R2|Receptor<br>Norma Primaria|359.518|7.449.160|22,75|
|3|R3|Receptor<br>Norma Primaria|359.020|7.448.755|24,78|
|4|R4|Receptor<br>Norma Primaria|359.002|7.448.292|35,87|
|5|R5|Receptor<br>Norma Primaria|359.264|7.447.777|45,76|
|6|R6|Receptor<br>Norma Primaria|359.408|7.448.534|38,32|
|7|R7|Receptor<br>Norma Primaria|352.716|7.444.460|21,90|

Fuente: Algoritmos SpA, 2023

 - **Topografía del área de modelación:** Esta información es obtenida de
datos satelitales para la zona de estudio.

Datum WGS84, coordenadas UTM.

_**Inventario y modelación de emisiones ATM003-22**_ _45/95_

_Junio, 2023_

_**Figura N° 9**_
_**Ubicación Puntos de Interés**_

Fuente: Algoritmos SpA, 2023

_**Inventario y modelación de emisiones ATM003-22**_ _46/95_

_Junio, 2023_

**6** **Resultados Modelación**

Se presentan los resultados obtenidos de la modelación atmosférica para este
estudio con el fin de evaluar el aporte de material particulado (MP 10 ), material
particulado respirable fino (MP 2,5 ), material particulado sedimentable (MPS),
dióxido de azufre (SO 2 ), óxidos de nitrógeno (NO X ) y monóxido de carbono (CO),
para el Proyecto COPEC Mejillones, fase de construcción año 1 más operación y
operación.

**6.1** **Campos de Viento**

Mediante la aplicación del modelo WRF se simuló el comportamiento de los campos
de vientos sobre el área del Proyecto, para cada una de las horas consideradas en
la modelación. Dichos campos de vientos permitirán determinar posteriormente la
dispersión de los contaminantes, a través de la aplicación del modelo CALPUFF.

A modo de ejemplo se seleccionó el día 07 de junio del año 2021 correspondiente
al Percentil 98 Diario de MP 10 del punto de máximo impacto de operación, para
representar el comportamiento de los vientos superficiales en horas
representativas del día, en la madrugada (06:00 hs.), a medio día (12:00 hs.),
durante la tarde (18:00 hs.) y en la noche (00:00 hs.).

_**Inventario y modelación de emisiones ATM003-22**_ _47/95_

_Junio, 2023_

_**Figura N° 10**_
_**Campos de Viento a las 00:00 horas.**_

Fuente: Algoritmos SpA, 2023

_**Inventario y modelación de emisiones ATM003-22**_ _48/95_

_Junio, 2023_

_**Figura N° 11**_
_**Campos de Viento a las 06:00 horas**_

Fuente: Algoritmos SpA, 2023

_**Inventario y modelación de emisiones ATM003-22**_ _49/95_

_Junio, 2023_

_**Figura N° 12**_
_**Campos de Viento a las 12:00 horas**_

Fuente: Algoritmos SpA, 2023

_**Inventario y modelación de emisiones ATM003-22**_ _50/95_

_Junio, 2023_

_**Figura N° 13**_
_**Campos de Viento a las 18:00 horas.**_

Fuente: Algoritmos SpA, 2023

_**Inventario y modelación de emisiones ATM003-22**_ _51/95_

_Junio, 2023_

**6.2** **Aportes Obtenidos de la Modelación**

Mediante la aplicación del modelo WRF-CALPUFF fue posible obtener las
concentraciones de material particulado respirable (MP 10 ), material particulado
respirable fino (MP 2,5 ), material particulado sedimentable (MPS), dióxido de azufre
(SO 2 ), óxidos de nitrógeno (NO 2 ) y monóxido de carbono (CO), que aportará el
proyecto, basándose en los campos de vientos generados por la modelación
meteorológica realizada con WRF.

Los aportes del proyecto fueron evaluados en los sectores de su entorno, para el
análisis de cumplimiento de las normas primarias y secundarias de calidad del aire
las que, de acuerdo con su cumplimiento, permitirá al titular determinar si el
proyecto generará efectos adversos significativos sobre la salud de la población y
sobre la calidad y cantidad de los recursos naturales renovables.

**6.2.1** **Aporte en Puntos de Interés**

En la siguiente tabla se presenta los aportes obtenidos por la modelación de la
construcción más operación y operación del proyecto en los puntos de interés.

_**Inventario y modelación de emisiones ATM003-22**_ _52/95_

_Junio, 2023_

_**Tabla N° 30**_
_**Aporte de Proyecto COPEC Mejillones en Punto de interés, Fase Construcción más Operación**_

|Receptor<br>de<br>Interés|MPS mg/m2día|Col3|MP ug/m3<br>10|Col5|MP ug/m3<br>2.5|Col7|SO ug/m3<br>2|Col9|Col10|Col11|Col12|Col13|NO ug/m3<br>2|Col15|CO ug/m3|Col17|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor**<br>**de**<br>**Interés**|**Secundaria**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Secundaria**|**Secundaria**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|
|**Receptor**<br>**de**<br>**Interés**|**Media Anual**|**Media Anual**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P99**<br>**Diario**|**P98,5**<br>**h **|**Media**<br>**Anual**|**P99,7**<br>**Diario**|**P99,73**<br>**h **|**Media**<br>**Anual**|**P99 h**|**P99**<br>**8 h**|**P99 h**|
|Norma|100|150|50|130|20|50|60|150|350|80|365|1.000|100|400|10.000|30.000|
|R1|0,60|0,72|0,61|1,44|0,19|0,42|0,01|0,02|0,06|0,01|0,03|0,12|0,42|5,22|0,44|1,44|
|R2|0,55|0,63|0,56|1,28|0,19|0,39|0,01|0,03|0,09|0,01|0,04|0,18|0,44|8,49|0,48|2,13|
|R3|0,65|0,72|0,63|1,34|0,22|0,48|0,01|0,04|0,12|0,01|0,06|0,27|0,57|11,07|0,76|3,24|
|R4|0,75|0,84|0,68|1,41|0,23|0,49|0,01|0,05|0,13|0,01|0,06|0,29|0,59|12,11|0,73|3,05|
|R5|0,80|0,91|0,69|1,47|0,23|0,52|0,01|0,04|0,12|0,01|0,06|0,29|0,54|12,49|0,71|3,22|
|R6|0,64|0,72|0,60|1,32|0,20|0,43|0,01|0,03|0,09|0,01|0,05|0,21|0,46|8,22|0,52|2,01|
|R7|0,08|0,11|0,12|0,41|0,05|0,19|0,00|0,02|0,03|0,00|0,02|0,10|0,11|5,46|0,32|1,42|

Fuente: Algoritmos SpA, 2023

_**Inventario y modelación de emisiones ATM003-22**_ _53/95_

_Junio, 2023_

_**Tabla N° 31**_
_**Aporte de Proyecto COPEC Mejillones en Punto de interés, Fase Operación**_

|Receptor<br>de<br>Interés|MPS mg/m2día|Col3|MP ug/m3<br>10|Col5|MP ug/m3<br>2.5|Col7|SO ug/m3<br>2|Col9|Col10|Col11|Col12|Col13|NO ug/m3<br>2|Col15|CO ug/m3|Col17|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor**<br>**de**<br>**Interés**|**Secundaria**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Secundaria**|**Secundaria**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|
|**Receptor**<br>**de**<br>**Interés**|**Media Anual**|**Media Anual**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P99**<br>**Diario**|**P98,5**<br>**h **|**Media**<br>**Anual**|**P99,7**<br>**Diario**|**P99,73**<br>**h **|**Media**<br>**Anual**|**P99 h**|**P99**<br>**8 h**|**P99 h**|
|Norma|100|150|50|130|20|50|60|150|350|80|365|1.000|100|400|10.000|30.000|
|R1|0,57|0,69|0,54|1,39|0,14|0,36|0,00|0,00|0,00|0,00|0,00|0,01|0,25|3,2|0,28|0,61|
|R2|0,51|0,59|0,48|1,13|0,13|0,30|0,00|0,00|0,00|0,00|0,00|0,01|0,23|2,85|0,25|0,56|
|R3|0,59|0,67|0,53|1,20|0,14|0,32|0,00|0,00|0,00|0,00|0,00|0,01|0,25|3,16|0,28|0,59|
|R4|0,70|0,79|0,57|1,29|0,15|0,34|0,00|0,00|0,00|0,00|0,00|0,01|0,28|3,24|0,31|0,62|
|R5|0,75|0,87|0,59|1,28|0,16|0,34|0,00|0,00|0,00|0,00|0,00|0,01|0,28|3,71|0,30|0,72|
|R6|0,60|0,68|0,52|1,23|0,14|0,33|0,00|0,00|0,00|0,00|0,00|0,01|0,24|2,88|0,27|0,59|
|R7|0,07|0,10|0,09|0,29|0,02|0,08|0,00|0,00|0,00|0,00|0,00|0,00|0,04|1,17|0,07|0,21|

Fuente: Algoritmos SpA, 2023

_**Inventario y modelación de emisiones ATM003-22**_ _54/95_

_Junio, 2023_

**6.2.2** **Ajustes de Resultados de la Modelación por Incertidumbre**

Acorde al análisis de incertidumbre de la modelación WRF presentado en el capítulo
del presente informe, en la evaluación cuantitativa (sección 3.5), se determinó que
que existía una sobre estimación del pronóstico de las velocidades de los vientos
de WRF en comparación con la meteorología monitoreada.

Esta sobrestimación de WRF, como archivo de entrada que alimenta la modelación
CALPUFF, implicaría una sub estimación de las concentraciones de los
contaminantes, ya que a mayor velocidad del viento existiría una mayor dispersión
de los contaminantes y por ende una menor concentración de éstos en la
atmósfera.

De acuerdo a lo antes expuesto se procede a integrar a los resultados de la
modelación la incertidumbre generada de acuerdo a la siguiente ecuación.

RM [′] = RM+ % de incertidumbre∗RM (VIII)

Dónde:

RM’ : Resultados de la modelación WRF-CALPUFF corregidos por incertidumbre
RM : Resultados modelación WRF-CALPUFF (concentraciones contaminantes)

_% de incertidumbre_ : 36%, porcentaje de sobrestimación alcanzado en la

evaluación cuantitativa del WRF (sección 3.5)

De acuerdo a lo antes expuesto, en las siguientes tablas se presentan los resultados
con la corrección por incertidumbre aplicada de acuerdo a la fórmula descrita (VIII).

_**Inventario y modelación de emisiones ATM003-22**_ _55/95_

_Junio, 2023_

_**Tabla N° 32**_
_**Aporte de Proyecto COPEC Mejillones en Punto de interés, Fase Construcción más Operación con**_

_**Incertidumbre**_

|Receptor<br>de<br>Interés|MPS mg/m2día|Col3|MP ug/m3<br>10|Col5|MP ug/m3<br>2.5|Col7|SO ug/m3<br>2|Col9|Col10|Col11|Col12|Col13|NO ug/m3<br>2|Col15|CO ug/m3|Col17|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor**<br>**de**<br>**Interés**|**Secundaria**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Secundaria**|**Secundaria**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|
|**Receptor**<br>**de**<br>**Interés**|**Media Anual**|**Media Anual**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P99**<br>**Diario**|**P98,5**<br>**h **|**Media**<br>**Anual**|**P99,7**<br>**Diario**|**P99,73**<br>**h **|**Media**<br>**Anual**|**P99**<br>** h**|**P99**<br>**8 h**|**P99**<br>**h **|
|Norma|100|150|50|130|20|50|60|150|350|80|365|1.000|100|400|10.000|30.000|
|R1|0,81|0,98|0,82|1,96|0,26|0,57|0,01|0,03|0,09|0,01|0,04|0,17|0,57|7,10|0,60|1,95|
|R2|0,74|0,86|0,76|1,73|0,25|0,53|0,01|0,04|0,12|0,01|0,05|0,24|0,60|11,55|0,65|2,90|
|R3|0,88|0,99|0,86|1,82|0,30|0,65|0,02|0,05|0,16|0,02|0,09|0,37|0,78|15,06|1,03|4,41|
|R4|1,02|1,14|0,93|1,91|0,31|0,67|0,02|0,06|0,17|0,02|0,09|0,40|0,80|16,47|0,99|4,15|
|R5|1,09|1,23|0,94|2,01|0,31|0,71|0,01|0,06|0,16|0,01|0,08|0,40|0,73|16,99|0,97|4,38|
|R6|0,86|0,99|0,82|1,79|0,27|0,58|0,01|0,05|0,12|0,01|0,07|0,29|0,63|11,18|0,71|2,73|
|R7|0,10|0,15|0,16|0,55|0,06|0,25|0,00|0,02|0,04|0,00|0,02|0,13|0,14|7,42|0,43|1,93|

Fuente: Algoritmos SpA, 2023

_**Inventario y modelación de emisiones ATM003-22**_ _56/95_

_Junio, 2023_

_**Tabla N° 33**_
_**Aporte de Proyecto COPEC Mejillones en Punto de interés, Fase Operación con Incertidumbre**_

|Receptor<br>de<br>Interés|MPS mg/m2día|Col3|MP ug/m3<br>10|Col5|MP ug/m3<br>2.5|Col7|SO ug/m3<br>2|Col9|Col10|Col11|Col12|Col13|NO ug/m3<br>2|Col15|CO ug/m3|Col17|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor**<br>**de**<br>**Interés**|**Secundaria**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Secundaria**|**Secundaria**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|
|**Receptor**<br>**de**<br>**Interés**|**Media Anual**|**Media Anual**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P99**<br>**Diario**|**P98,5**<br>**h **|**Media**<br>**Anual**|**P99,7**<br>**Diario**|**P99,73**<br>**h **|**Media**<br>**Anual**|**P99**<br>** h**|**P99**<br>**8 h**|**P99**<br>**h **|
|Norma|100|150|50|130|20|50|60|150|350|80|365|1.000|100|400|10.000|30.000|
|R1|0,77|0,93|0,73|1,89|0,19|0,49|0,00|0,00|0,01|0,00|0,00|0,01|0,34|4,35|0,38|0,83|
|R2|0,70|0,81|0,66|1,54|0,17|0,40|0,00|0,00|0,00|0,00|0,00|0,01|0,31|3,88|0,34|0,76|
|R3|0,81|0,91|0,72|1,63|0,19|0,44|0,00|0,00|0,01|0,00|0,00|0,01|0,34|4,30|0,39|0,80|
|R4|0,95|1,08|0,78|1,76|0,20|0,46|0,00|0,00|0,01|0,00|0,00|0,01|0,38|4,41|0,42|0,85|
|R5|1,03|1,18|0,81|1,74|0,21|0,46|0,00|0,00|0,01|0,00|0,00|0,01|0,38|5,04|0,40|0,98|
|R6|0,81|0,93|0,71|1,67|0,19|0,44|0,00|0,00|0,01|0,00|0,00|0,01|0,33|3,91|0,37|0,80|
|R7|0,09|0,13|0,12|0,39|0,03|0,11|0,00|0,00|0,00|0,00|0,00|0,00|0,05|1,59|0,10|0,28|

Fuente: Algoritmos SpA, 2023

_**Inventario y modelación de emisiones ATM003-22**_ _57/95_

_Junio, 2023_

**6.3** **Aportes en Puntos de Máxima Concentración**

Las siguientes tablas presentan la ubicación de los Puntos de Máximo Impacto
(PMI), para los contaminantes MP 10, MP 2,5, MPS, SO 2, NO 2 y CO, durante la fase de
construcción mas operación y operación del Proyecto.

_**Tabla N° 34**_
_**Localización Punto Máximo Impacto (PMI), Fase Construcción más**_

_**Operación**_

|Parámetro|Estadístico|PMI|Norma|Unidad|%<br>Norma|Coordenadas UTM -<br>WGS84|Col8|
|---|---|---|---|---|---|---|---|
|**Parámetro**|**Estadístico**|**PMI**|**Norma**|**Unidad**|**% **<br>**Norma**|**Este (m)**|**Norte (m)**|
|MPS|Promedio del<br>Periodo|18,36|100|mg/m2día|12,24%|358.339|7.446.124|
|MPS|Promedio<br>mensual|19,86|150|150|19,86%|358.339|7.446.124|
|MP10|Promedio del<br>Periodo|8,18|50|ug/m3|16,35%|361.343|7.446.152|
|MP10|Percentil 98<br>Diario|20,09|130|130|15,45%|361.343|7.446.152|
|MP2,5|Promedio del<br>Periodo|2,40|20|20|11,98%|358.339|7.446.124|
|MP2,5|Percentil 98<br>Diario|7,55|50|50|15,09%|358.339|7.446.124|
|SO2|Promedio del<br>Periodo|0,20|60|60|0,33%|357.337|7.446.114|
|SO2|Percentil 99<br>Diario|1,23|150|150|0,82%|357.337|7.446.114|
|SO2|Percentil 98,5<br>Horario|3,50|350|350|1,00%|357.337|7.446.114|
|SO2|Promedio del<br>Periodo|0,20|80|80|0,25%|357.337|7.446.114|
|SO2|Percentil 99,7<br>Diario|1,47|365|365|0,40%|357.337|7.446.114|
|SO2|Percentil 99,73<br>Horario|6,88|1.000|1.000|0,69%|357.337|7.446.114|
|NO2|Promedio del<br>Periodo|4,25|100|100|4,25%|357.337|7.446.114|
|NO2|Percentil 99<br>Horario|202,11|400|400|50,53%|358.339|7.446.124|
|CO<br>|Percentil 99 8<br>Horas|17,51|10.000|10.000|0,18%|357.337|7.446.114|
|CO<br>|Percentil 99<br>Horario<br>|72,69|30.000|30.000|0,24%|358.339|7.446.124|

Fuente: Algoritmos SpA, 2023

_**Inventario y modelación de emisiones ATM003-22**_ _58/95_

_Junio, 2023_

_**Tabla N° 35**_
_**Localización Punto Máximo Impacto (PMI), Fase Operación**_

|Parámetro|Estadístico|PMI|Norma|Unidad|%<br>Norma|Coordenadas UTM -<br>WGS84|Col8|
|---|---|---|---|---|---|---|---|
|**Parámetro**|**Estadístico**|**PMI**|**Norma**|**Unidad**|**% **<br>**Norma**|**Este (m)**|**Norte (m)**|
|MPS|Promedio del<br>Periodo|17,33|100|mg/m2día|17,33%|358.339|7.446.124|
|MPS|Promedio<br>mensual|18,68|150|150|12,45%|358.339|7.446.124|
|MP10|Promedio del<br>Periodo|7,93|50|ug/m3|15,86%|361.343|7.446.152|
|MP10|Percentil 98<br>Diario|19,26|130|130|14,82%|361.343|7.446.152|
|MP2,5|Promedio del<br>Periodo|2,04|20|20|10,21%|361.343|7.446.152|
|MP2,5|Percentil 98<br>Diario|5,07|50|50|10,14%|361.343|7.446.152|
|SO2|Promedio del<br>Periodo|0,01|60|60|0,02%|361.343|7.446.152|
|SO2|Percentil 99<br>Diario|0,03|150|150|0,02%|361.343|7.446.152|
|SO2|Percentil 98,5<br>Horario|0,06|350|350|0,02%|361.343|7.446.152|
|SO2|Promedio del<br>Periodo|0,01|80|80|0,01%|361.343|7.446.152|
|SO2|Percentil 99,7<br>Diario|0,03|365|365|0,01%|363.365|7.444.179|
|SO2|Percentil 99,73<br>Horario|0,16|1.000|1.000|0,02%|360.342|7.446.143|
|NO2|Promedio del<br>Periodo|2,77|100|100|2,77%|361.343|7.446.152|
|NO2|Percentil 99<br>Horario|89,15|400|400|22,29%|360.342|7.446.143|
|CO<br>|Percentil 99 8<br>Horas|4,57|10.000|10.000|0,05%|361.343|7.446.152|
|CO<br>|Percentil 99<br>Horario<br>|23,50|30.000|30.000|0,08%|361.343|7.446.152|

Fuente: Algoritmos SpA, 2023

Las siguientes figuras muestran la ubicación de los puntos de máximo impacto
para las fases construcción más operación y operación del proyecto.

_**Inventario y modelación de emisiones ATM003-22**_ _59/95_

_Junio, 2023_

_**Figura N° 14**_
_**Ubicación de Puntos de Máximo Impacto, Fase Construcción más Operación**_

Fuente: Algoritmos SpA, 2023

_**Inventario y modelación de emisiones ATM105-21**_ _60/75_

_Junio, 2023_

_**Figura N° 15**_
_**Ubicación de Puntos de Máximo Impacto, Fase Operación**_

Fuente: Algoritmos SpA, 2023

_**Inventario y modelación de emisiones ATM105-21**_ _61/75_

_Junio, 2023_

**6.4** **Análisis de Cumplimiento de Normativa Ambiental**

Para establecer el cumplimiento de la normativa ambiental vigente de calidad del aire para MP 10, MP 2,5, MPS, SO 2,
NO 2, y CO, en las siguientes tablas se muestra la comparación del Aporte del Proyecto (AP) con la normativa vigente
mediante el porcentaje que representa el aporte del Proyecto (%AP/Norma) para cada Receptor de Interés (RI).

_**Tabla N° 36**_
_**Análisis Normativo en Punto de interés, Fase Construcción más Operación**_

|RI|MPS<br>mg/m2día|Col3|MP ug/m3<br>10|Col5|MP ug/m3<br>2.5|Col7|SO ug/m3<br>2|Col9|Col10|Col11|Col12|Col13|NO ug/m3<br>2|Col15|CO ug/m3|Col17|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**RI**|**Secundaria**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Secundaria**|**Secundaria**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|
|**RI**|**Media Anual**|**Media Anual**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P99**<br>**Diario**|**P98,5 h**|**Media**<br>**Anual**|**P99,7**<br>**Diario**|**P99,73**<br>**h **|**Media**<br>**Anual**|**P99**<br>**h **|**P99**<br>**8 h**|**P99**<br>**h **|
|Nor<br>ma|100|150|50|130|20|50|60|150|350|80|365|1.000|100|400|10.000|30.000|
|R1|0,41%|0,49%|1,65%|1,51%|1,29%|1,15%|0,01%|0,02%|0,02%|0,01%|0,01%|0,02%|0,57%|1,77%|0,01%|0,01%|
|R2|0,37%|0,43%|1,53%|1,33%|1,26%|1,05%|0,02%|0,02%|0,03%|0,01%|0,01%|0,02%|0,60%|2,89%|0,01%|0,01%|
|R3|0,44%|0,49%|1,72%|1,40%|1,48%|1,30%|0,03%|0,04%|0,05%|0,02%|0,02%|0,04%|0,78%|3,76%|0,01%|0,01%|
|R4|0,51%|0,57%|1,85%|1,47%|1,56%|1,34%|0,03%|0,04%|0,05%|0,02%|0,02%|0,04%|0,80%|4,12%|0,01%|0,01%|
|R5|0,55%|0,61%|1,88%|1,54%|1,54%|1,41%|0,02%|0,04%|0,05%|0,02%|0,02%|0,04%|0,73%|4,25%|0,01%|0,01%|
|R6|0,43%|0,49%|1,64%|1,38%|1,34%|1,16%|0,02%|0,03%|0,04%|0,01%|0,02%|0,03%|0,63%|2,80%|0,01%|0,01%|
|R7|0,05%|0,07%|0,32%|0,42%|0,32%|0,50%|0,01%|0,02%|0,01%|0,00%|0,01%|0,01%|0,14%|1,86%|<0,01%|0,01%|

Fuente: Algoritmos SpA, 2023

_**Inventario y modelación de emisiones ATM003-22**_ _62/95_

_Junio, 2023_

_**Tabla N° 37**_
_**Análisis Normativo en Punto de interés, Fase Operación**_

|RI|MPS<br>mg/m2día|Col3|MP ug/m3<br>10|Col5|MP ug/m3<br>2.5|Col7|SO ug/m3<br>2|Col9|Col10|Col11|Col12|Col13|NO ug/m3<br>2|Col15|CO ug/m3|Col17|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**RI**|**Secundaria**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Secundaria**|**Secundaria**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|
|**RI**|**Media Anual**|**Media Anual**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P99**<br>**Diario**|**P98,5 h**|**Media**<br>**Anual**|**P99,7**<br>**Diario**|**P99,73**<br>**h **|**Media**<br>**Anual**|**P99**<br>**h **|**P99**<br>**8 h**|**P99**<br>**h **|
|Nor<br>ma|100|150|50|130|20|50|60|150|350|80|365|1.000|100|400|10.000|30.000|
|R1|0,77%|0,62%|1,47%|1,45%|0,96%|0,98%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,34%|1,09%|<0,01%|<0,01%|
|R2|0,70%|0,54%|1,31%|1,19%|0,86%|0,81%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,31%|0,97%|<0,01%|<0,01%|
|R3|0,81%|0,61%|1,43%|1,25%|0,94%|0,87%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,34%|1,07%|<0,01%|<0,01%|
|R4|0,95%|0,72%|1,56%|1,35%|1,02%|0,93%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,38%|1,10%|<0,01%|<0,01%|
|R5|1,03%|0,79%|1,61%|1,34%|1,06%|0,92%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,38%|1,26%|<0,01%|<0,01%|
|R6|0,81%|0,62%|1,42%|1,29%|0,93%|0,89%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,33%|0,98%|<0,01%|<0,01%|
|R7|0,09%|0,09%|0,24%|0,30%|0,16%|0,21%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,05%|0,40%|<0,01%|<0,01%|

Fuente: Algoritmos SpA, 2023

_**Inventario y modelación de emisiones ATM003-22**_ _63/95_

_Junio, 2023_

**6.5** **Mapas de Isoconcentraciones**

A continuación, se presentan las isolíneas de concentración de MP 10, MP 2,5, MPS,
NO 2, CO y SO 2, correspondiente a la fase de construcción más operación y
operación del proyecto.

_**Inventario y modelación de emisiones ATM003-22**_ _64/95_

_Junio, 2023_

_**Figura N° 16**_
_**Percentil 98 Promedio Diario de MP**_ _**10**_ _**Fase Construcción más Operación**_

Fuente: Algoritmos SpA, 2023

_**Inventario y modelación de emisiones ATM003-22**_ _65/95_

_Junio, 2023_

_**Figura N° 17**_
_**Promedio del Período de MP**_ _**10**_ _**Fase Construcción más Operación**_

Fuente: Algoritmos SpA, 2023

_**Inventario y modelación de emisiones ATM003-22**_ _66/95_

_Junio, 2023_

_**Figura N° 18**_
_**Percentil 98 Promedio Diario de MP**_ _**2,5**_ _**Fase Construcción más Operación**_

Fuente: Algoritmos SpA, 2023

_**Inventario y modelación de emisiones ATM003-22**_ _67/95_

_Junio, 2023_

_**Figura N° 19**_
_**Promedio del Período de MP**_ _**2,5**_ _**Fase Construcción más Operación**_

Fuente: Algoritmos SpA, 2023

_**Inventario y modelación de emisiones ATM003-22**_ _68/95_

_Junio, 2023_

_**Figura N° 20**_
_**Promedio del Período de MPS Fase Construcción más Operación**_

Fuente: Algoritmos SpA, 2023

_**Inventario y modelación de emisiones ATM003-22**_ _69/95_

_Junio, 2023_

_**Figura N° 21**_
_**Promedio del Período del Mes de MPS Fase Construcción más Operación**_

Fuente: Algoritmos SpA, 2023

_**Inventario y modelación de emisiones ATM003-22**_ _70/95_

_Junio, 2023_

_**Figura N° 22**_
_**Percentil 99 Promedio Diario de SO2 Fase Construcción más Operación**_

Fuente: Algoritmos SpA, 2023

_**Inventario y modelación de emisiones ATM003-22**_ _71/95_

_Junio, 2023_

_**Figura N° 23**_
_**Percentil 98,5 Promedio Horario de SO**_ _**2**_ _**Fase Construcción más Operación**_

Fuente: Algoritmos SpA, 2023

_**Inventario y modelación de emisiones ATM003-22**_ _72/95_

_Junio, 2023_

_**Figura N° 24**_
_**Percentil 99,7 Promedio Diario de SO**_ _**2**_ _**Fase Construcción más Operación**_

Fuente: Algoritmos SpA, 2023

_**Inventario y modelación de emisiones ATM003-22**_ _73/95_

_Junio, 2023_

_**Figura N° 25**_
_**Percentil 99,73 Promedio Horario de SO**_ _**2**_ _**Fase Construcción más Operación**_

Fuente: Algoritmos SpA, 2023

_**Inventario y modelación de emisiones ATM003-22**_ _74/95_

_Junio, 2023_

_**Figura N° 26**_
_**Promedio del Período de SO**_ _**2**_ _**Fase Construcción más Operación**_

Fuente: Algoritmos SpA, 2023

_**Inventario y modelación de emisiones ATM003-22**_ _75/95_

_Junio, 2023_

_**Figura N° 27**_
_**Percentil 99 Máximo Horario de NO**_ _**2**_ _**Fase Construcción más Operación**_

Fuente: Algoritmos SpA, 2023

_**Inventario y modelación de emisiones ATM003-22**_ _76/95_

_Junio, 2023_

_**Figura N° 28**_
_**Promedio del Período de NO**_ _**2**_ _**Fase Construcción más Operación**_

Fuente: Algoritmos SpA, 2023

_**Inventario y modelación de emisiones ATM003-22**_ _77/95_

_Junio, 2023_

_**Figura N° 29**_
_**Percentil 99 Máximo Horario de CO Fase Construcción más Operación**_

Fuente: Algoritmos SpA, 2023

_**Inventario y modelación de emisiones ATM003-22**_ _78/95_

_Junio, 2023_

_**Figura N° 30**_
_**Percentil 99 Máximo 8 Horas de CO Fase Construcción más Operación**_

Fuente: Algoritmos SpA, 2023

_**Inventario y modelación de emisiones ATM003-22**_ _79/95_

_Junio, 2023_

_**Figura N° 31**_
_**Percentil 98 Promedio Diario de MP**_ _**10**_ _**Fase Operación**_

Fuente: Algoritmos SpA, 2023

_**Inventario y modelación de emisiones ATM003-22**_ _80/95_

_Junio, 2023_

_**Figura N° 32**_
_**Promedio del Período de MP**_ _**10**_ _**Fase Operación**_

Fuente: Algoritmos SpA, 2023

_**Inventario y modelación de emisiones ATM003-22**_ _81/95_

_Junio, 2023_

_**Figura N° 33**_
_**Percentil 98 Promedio Diario de MP**_ _**2,5**_ _**Fase Operación**_

Fuente: Algoritmos SpA, 2023

_**Inventario y modelación de emisiones ATM003-22**_ _82/95_

_Junio, 2023_

_**Figura N° 34**_
_**Promedio del Período de MP**_ _**2,5**_ _**Fase Operación**_

Fuente: Algoritmos SpA, 2023

_**Inventario y modelación de emisiones ATM003-22**_ _83/95_

_Junio, 2023_

_**Figura N° 35**_
_**Promedio del Período de MPS Fase Operación**_

Fuente: Algoritmos SpA, 2023

_**Inventario y modelación de emisiones ATM003-22**_ _84/95_

_Junio, 2023_

_**Figura N° 36**_
_**Promedio del Período del Mes de MPS Fase Operación**_

Fuente: Algoritmos SpA, 2023

_**Inventario y modelación de emisiones ATM003-22**_ _85/95_

_Junio, 2023_

_**Figura N° 37**_
_**Percentil 99 Promedio Diario de SO**_ _**2**_ _**Fase Operación**_

Fuente: Algoritmos SpA, 2023

_**Inventario y modelación de emisiones ATM003-22**_ _86/95_

_Junio, 2023_

_**Figura N° 38**_
_**Percentil 98,5 Promedio Horario de SO**_ _**2**_ _**Fase Operación**_

Fuente: Algoritmos SpA, 2023

_**Inventario y modelación de emisiones ATM003-22**_ _87/95_

_Junio, 2023_

_**Figura N° 39**_
_**Percentil 99,7 Promedio Diario de SO**_ _**2**_ _**Fase Operación**_

Fuente: Algoritmos SpA, 2023

_**Inventario y modelación de emisiones ATM003-22**_ _88/95_

_Junio, 2023_

_**Figura N° 40**_
_**Percentil 99,73 Promedio Horario de SO**_ _**2**_ _**Fase Operación**_

Fuente: Algoritmos SpA, 2023

_**Inventario y modelación de emisiones ATM003-22**_ _89/95_

_Junio, 2023_

_**Figura N° 41**_
_**Promedio del Período de SO**_ _**2**_ _**Fase Operación**_

Fuente: Algoritmos SpA, 2023

_**Inventario y modelación de emisiones ATM003-22**_ _90/95_

_Junio, 2023_

_**Figura N° 42**_
_**Percentil 99 Máximo Horario de NO**_ _**2**_ _**Fase Operación**_

Fuente: Algoritmos SpA, 2023

_**Inventario y modelación de emisiones ATM003-22**_ _91/95_

_Junio, 2023_

_**Figura N° 43**_
_**Promedio del Período de NO**_ _**2**_ _**Fase Operación**_

Fuente: Algoritmos SpA, 2023

_**Inventario y modelación de emisiones ATM003-22**_ _92/95_

_Junio, 2023_

_**Figura N° 44**_
_**Percentil 99 Máximo Horario de CO Fase Operación**_

Fuente: Algoritmos SpA, 2023

_**Inventario y modelación de emisiones ATM003-22**_ _93/95_

_Junio, 2023_

_**Figura N° 45**_
_**Percentil 99 Máximo 8 Horas de CO Fase Operación**_

Fuente: Algoritmos SpA, 2023

_**Inventario y modelación de emisiones ATM003-22**_ _94/95_

_Junio, 2023_

**7** **Conclusiones**

De los resultados obtenidos en los cálculos de emisiones y la modelación de estas
emisiones para el Proyecto COPEC Mejillones, se desprende lo siguiente:

 Se realizó un inventario de emisiones de las principales actividades emisoras
existentes en la fase de construcción, operación y cierre del Proyecto COPEC
Mejillones. Para el inventario se consideraron los contaminantes: dióxido de
azufre (SO 2 ), óxidos de nitrógeno (NO X ), material particulado fino, grueso y
sedimentable (MP 2.5, MP 10 MPS), monóxido de carbono (CO) y compuestos
orgánicos volátiles (COVs).

 Las emisiones totales resultantes del inventario de emisiones para la fase
Construcción, Operación y Cierre corresponden a:

`o` Construcción año 1: 1,11 t de MP 2.5, 1,71 t de MP 10, 4,59 t de MPS,

0,52 t de SO 2, 9,84 t de NO X, 3,20 t de CO y 1,11 t de COVs.
`o` Construcción año 2: 0,39 t de MP 2.5, 0,56 t de MP 10, 1,52 t de MPS,

0,31 t de SO 2, 4,81 t de NO X, 1,05 t de CO y 0,39 t de COVs.
`o` Operación: 6,41 t de MP 2.5, 25,76 t de MP 10, 133,21 t de MPS, 0,04 t

de SO 2, 11,15 t de NO X, 2,63 t de CO y 0,51 t de COVs.

`o` Cierre: 0,01 t de MP 2.5, 0,05 t de MP 10, 0,25 t de MPS, <0,01 t de SO 2,

0,04 t de NO X, 0,01 t de CO y <0,01 t de COVs.

 En relación de los aportes del inventario las máximas emisiones provienen
de la fase de Operación de la actual Planta Mejillones. Con respecto a la fase
de Construcción, el mayor aporte para las particulas y los gases corresponde
al grupo electrógeno. Asimismo, para las fases de Operación y Cierre los
mayores aportes para las particulas corresponde al tránsito de caminos
pavimentados y para los gases proviene del motor de vehículos de caminos
pavimentados.

 Los puntos de interés con mayores concentraciones obtenidas del proyecto
son los que se ubican en las cercanías de sus imediaciones.

 Los puntos máximo impacto para todos los contaminantes se encuentran
concentrados en los alrededores de las instalaciones del proyecto en zonas
no pobladas.

 Las isoconcentraciones obtenidas muestran que los contaminantes tienen
una dispersión local, ubicándose preferentemente en los entornos del
proyecto.

 Finalmente, en base a los resultados obtenidos, los puntos de interés
considerados en el presente estudio no sobrepasan las normas primarias y
secundarias de calidad del aire.

_**Inventario y modelación de emisiones ATM003-22**_ _95/95_

_Junio, 2023_