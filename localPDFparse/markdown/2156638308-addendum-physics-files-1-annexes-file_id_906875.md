---
title: Sin título
author: Gabriela Arana Valenzuela
date: D:20230604111806-04'00'
language: es
type: report
pages: 198
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Anexo 21. Actualización de estimación y modelación de emisiones atmosféricas
  - Apéndice 1. Plan de Aplicación de Supresor de Polvo
-->

# Anexo 21. Actualización de estimación y modelación de emisiones atmosféricas

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_

**ÍNDICE**

**A.** **PRESENTACIÓN .................................................................................................................................... 1**

**B.** **OBJETIVOS ........................................................................................................................................... 3**

B.1 General........................................................................................................................................ 3

B.2 Específicos ................................................................................................................................... 3
**C.** **ÁREA DE INFLUENCIA........................................................................................................................... 4**
**D.** **INFORMACIÓN METEOROLÓGICA Y DE CALIDAD DE AIRE DE LA ZONA DE ESTUDIO ............................ 5**

D.1. Introducción y breve descripción de zona de estudio.................................................................... 5
D.2. Descripción Topográfica y Climática de la Zona de Estudio ........................................................... 6
D.3. Línea Base Meteorológica de la Zona de Estudio Durante el Año 2021 .......................................... 7

D.4. Línea Base de calidad del aire de la zona de Estudio ................................................................... 15
**E.** **IMPLEMENTACIÓN, APLICACIÓN Y RESULTADOS DEL MODELO METEOROLÓGICO WRF .................... 22**

E.1. Introducción .............................................................................................................................. 22

E.2. Implementación del modelo meteorológico WRF ....................................................................... 23

E.3. Resultados del modelo WRF en la zona de Estudio ..................................................................... 25

E.4. Análisis de incertidumbre de los resultados del modelo WRF respecto a los datos observados en
estaciones dentro del dominio de la zona de Estudio para el año 2021. .................................................. 31

E.5. Análisis cuantitativo ................................................................................................................... 40

**F.** **INVENTARIO DE EMISIONES DEL PROYECTO ...................................................................................... 41**

F.1. Introducción .............................................................................................................................. 41

F.2. Metodología de Cálculo de Emisiones Atmosféricas ................................................................... 41

F.3. Factores de Emisión de Contaminantes Atmosféricos ................................................................. 42

F.4. Cálculo de Factores de Emisión de Contaminantes Atmosféricos ................................................ 50

F.5. Niveles de Actividad del Proyecto .............................................................................................. 57
F.6. Cálculo de Emisiones de Partículas y Gases ................................................................................ 76
F.7. Resumen de Emisiones de Partículas y Gases ............................................................................. 99
**G.** **IMPLEMENTACIÓN, APLICACIÓN Y RESULTADOS DEL MODELO DE DISPERSIÓN CALPUFF ............... 104**

G.1 Introducción ............................................................................................................................ 104

G.2 Implementación y Aplicación del Modelo de Dispersión CALPUFF............................................. 105
G.3. Resultados de la Aplicación del Sistema CALPUFF ..................................................................... 140

**H.** **CONCLUSIONES ............................................................................................................................... 175**
**I.** **BIBLIOGRAFÍA .................................................................................................................................. 178**
**J.** **APÉNDICE ........................................................................................................................................ 179**
**A.** **PRESENTACIÓN ................................................................................................................................ 180**

**B.** **OBJETIVO......................................................................................................................................... 181**

**C.** **RESPONSABLES ................................................................................................................................ 181**

C.1. Gerencia del Proyecto. ............................................................................................................. 181
C.2. Jefe de Faena o Supervisor en terreno...................................................................................... 181
**D.** **PLAN DE APLICACIÓN Y CUIDADO DE SUPRESOR DE POLVO ............................................................ 182**

D.1. Restricción de la velocidad al interior de los caminos internos del Parque Eólico ...................... 182
D.2. Aplicación de supresor de Polvo en caminos a utilizar del Parque Eólico .................................. 182
D.3. Inspecciones preventivas y mantenciones correctivas ............................................................. 184

E. Frecuencia ............................................................................................................................... 186

E.1. Frecuencia de aplicación.......................................................................................................... 186
E.2. Frecuencia de mantención....................................................................................................... 187
**F.** **VERIFICACIÓN .................................................................................................................................. 188**

**G.** **Anexos ............................................................................................................................................ 189**

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ i

**FIGURAS**

**Figura** **1** . Proyecto Parque Eólico Dañicalqui. ............................................................................................ 1
**Figura** **2.** Área de Influencia para Calidad de Aire. ..................................................................................... 4
**Figura** **3.** Mapa Topográfico de la Zona. .................................................................................................... 7
**Figura** **4.** Área de estudio, ubicación del proyecto y estación meteorológica. ............................................ 9
**Figura** **5.** Series de tiempo de variables meteorológicas observadas en la estación Purén durante el año

2021. ....................................................................................................................................... 10

**Figura** **6.** Ciclos diarios de variables meteorológicas observadas en la estación Purén durante el año 2021.

.............................................................................................................................................. 12

**Figura** **7.** Ciclos estacionales de variables meteorológicas observadas en estación Purén durante el año

2021. ....................................................................................................................................... 13

**Figura** **8.** Rosas de viento de observaciones en estación Puren durante el año 2021. .............................. 14
**Figura** **9.** Ubicación de las estaciones de calidad del aire respecto al Proyecto. ....................................... 17
**Figura** **10.** Diagrama de operación del modelo meteorológico WRF. ......................................................... 23
**Figura** **11.** Dominios de modelación de WRF en la zona de Estudio con centro cercano a Cabrero. ............ 24
**Figura** **12.** Series de tiempo de variables meteorológicas modeladas en estación Purén durante el año 2021.

.............................................................................................................................................. 26

**Figura** **13.** Ciclos diarios de variables meteorológicas modeladas en estación Purén durante el año 2021. 27
**Figura** **14.** Ciclos estacionales de variables meteorológicas modeladas en estación Purén durante año 2021.

.............................................................................................................................................. 29

**Figura** **15** . Rosas de viento de datos modelados en estación Purén durante el año 2021. .......................... 31
**Figura** **16** . Comparación series de tiempo de variables meteorológicas observadas y modeladas con WRF en

estación Purén durante el año 2021. ........................................................................................ 33

**Figura** **17** . Comparación de ciclos diarios de variables meteorológicas observados y modelados con WRF en

estación Purén durante el año 2021. ........................................................................................ 35

**Figura** **18** . Comparación de ciclos estacionales de variables meteorológicas observados y modelados con

WRF en estación Purén durante el año 2021. ........................................................................... 37

**Figura** **19** . Comparación de Rosas de Viento con datos observados y modelados con WRF en estación Purén

durante el año 2021 ................................................................................................................ 39

**Figura** **20** . Caminos externos e internos con supresor de polvo en la fase de construcción del proyecto Parque

Eólico Dañicalqui. .................................................................................................................... 67
**Figura** **21** . Diagrama de operación del sistema de modelación WRF/CALPUFF/CalDesk. .......................... 105
**Figura** **22** . Dominio de modelación de CALPUFF, 95 x 95 km2, en coordenadas LCC. ............................... 106
**Figura** **23** . Área de receptores de grilla de CALPUFF, 80 x 73 km2, en coordenadas LCC........................... 107
**Figura** **24** . Ubicación de Receptores de interés alrededor del Proyecto. .................................................. 110
**Figura** **25** . Distribución de fuentes emisoras (caminos) del escenario del primer año de Construcción del

Proyecto Parque Eólico Dañicalqui. . ...................................................................................... 135
**Figura** **26** . Distribución de fuentes emisoras del escenario del primer año de Construcción del Proyecto

Parque Eólico Dañicalqui. Fuentes implementadas en CALPUFF, en coordenadas LCC. ............ 136
**Figura** **27** . Distribución de fuentes emisoras del escenario del primer año de Construcción del Proyecto

Parque Eólico Dañicalqui, Acercamiento al Proyecto. ............................................................. 137
**Figura** **28** . Distribución de fuentes emisoras del escenario del primer año de Construcción del Proyecto

Parque Eólico Dañicalqui, Acercamiento al Proyecto. Fuentes implementadas en CALPUFF, en

coordenadas LCC. .................................................................................................................. 138

**Figura** **29** . Ejemplo de distribución de fuentes emisoras del escenario del primer año de Construcción del

Proyecto Parque Eólico Dañicalqui, Acercamiento al Proyecto. Fuentes en Google Earth. ....... 139
**Figura** **30** . Ejemplo de distribución de fuentes emisoras del escenario del primer año de Construcción del

Proyecto Parque Eólico Dañicalqui, Acercamiento al Proyecto. Fuentes implementadas en
CALPUFF, en coordenadas LCC. .............................................................................................. 140
**Figura** **31** . Isolíneas de concentraciones promedio anual de MP10 en la zona de estudio. Escenario

meteorología año 2021 y escenario de emisiones del primer año de construcción. ................ 144

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ ii

**Figura** **32** . Isolíneas de percentiles 98 de concentraciones de 24 horas de MP10 primario en la zona de

estudio. Escenario meteorología año 2021 y escenario de emisiones del primer año de

construcción. ......................................................................................................................... 145

**Figura** **33** . Isolíneas de concentraciones promedio anual de MP2,5 en la zona de estudio. Escenario

meteorología año 2021 y escenario de emisiones del primer año de construcción. ................ 148
**Figura** **34** . Isolíneas de percentiles 98 de concentraciones de 24 horas de MP2,5 en la zona de estudio.

Escenario meteorología año 2021 y escenario de emisiones del primer año de construcción. . 149
**Figura** **35** . Isolíneas de concentraciones promedio anual de MPS en la zona de estudio. Escenario

meteorología año 2021 y escenario de emisiones del primer año de construcción. ................ 152
**Figura** **36** . Isolíneas de concentraciones promedio anual de NO2 en la zona de estudio. Escenario

meteorología año 2021 y escenario de emisiones del primer año de construcción. ................ 155
**Figura** **37** . Isolíneas de percentiles 99 de concentraciones de 1 hora de NO2 en la zona de estudio. Escenario

meteorología año 2021 y escenario de emisiones del primer año de construcción. ................ 156
**Figura** **38** . Isolíneas de concentraciones promedio anual de SO2 en la zona de estudio. Escenario

meteorología año 2021 y escenario de emisiones del primer año de construcción. ................ 161
**Figura** **39** . Isolíneas de Percentil 99 de las concentraciones de 24 horas de SO2 en la zona de estudio.

Escenario meteorología año 2021 y escenario de emisiones del primer año de construcción. . 162
**Figura** **40** . Isolíneas de Percentil 98,5 de las concentraciones de 1 hora de SO2 en la zona de estudio.

Escenario meteorología año 2021 y escenario de emisiones del primer año de construcción. . 163
**Figura** **41** . Isolíneas de Percentil 99,7 de las concentraciones de 24 horas de SO2 en la zona de estudio.

Escenario meteorología año 2021 y escenario de emisiones del primer año de construcción. . 164
**Figura** **42** . Isolíneas de Percentil 99,73 de las concentraciones de 1 hora de SO2 en la zona de estudio.

Escenario meteorología año 2021 y escenario de emisiones del primer año de construcción. . 165
**Figura** **43** . Isolíneas de Percentil 99 de los máximos diarios de las concentraciones de 8 horas de CO en la

zona de estudio. Escenario meteorología año 2021 y escenario de emisiones del primer año de

construcción. ......................................................................................................................... 168

**Figura** **44** . Isolíneas de Percentil 99 de los máximos diarios de las concentraciones de 1 hora de CO en la zona

de estudio. Escenario meteorología año 2021 y escenario de emisiones del primer año de

construcción. ......................................................................................................................... 169
**Figura** **45** . Área de Influencia para Calidad de Aire. ................................................................................. 173
**Figura** **46** . Caminos del Proyecto a los cuales le será aplicada la medida de Supresión de Polvo. ............. 184

**TABLAS**

**Tabla** **1** . Estaciones meteorológicas en el dominio de la zona de Estudio. ................................................ 8
**Tabla** **2.** Normas Primarias y Secundarias de calidad de aire de Chile para contaminantes atmosféricos. 15

**Tabla** **3.** Estaciones de monitoreo de calidad del aire ............................................................................ 17

**Tabla 4** . Percentil 98 de las concentraciones 24 horas de MP10 registrada por la estación SAPU. Período

2019-2021. .............................................................................................................................. 18

**Tabla 5.** Percentil 98 de las concentraciones 24 horas de MP10 registrada por la estación Quinel. Período

<!-- INICIO TABLA 5 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |---|---|---| |2019|107,8|**130**| |2020|90,6|90,6| |2021|110,7|110,7| -->

**Tabla 5: ** . Percentil 98 de las concentraciones 24 horas de MP10 registrada por la estación Quinel.**

| Año | Percentil 98 de las<br>Concentraciones 24 horas (μg/m3) | Norma D.S. No 59/1998 (μg/m3) |
| --- | --- | --- |
| 2019 | 46,6 | **130** |
| 2020 | 91,4 | 91,4 |
| 2021 | 211,5 | 211,5 |

<!-- Estadísticas: 3 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- **D.4.4.** **Resultados MP10 Concentración Anual** En **Tabla 6** y **Tabla 7** se presentan los Percentiles 98 las concentraciones promedio anuales de MP10, -->
<!-- FIN TABLA 5 -->


2019-2021. .............................................................................................................................. 18

**Tabla** **6.** Concentración anual de MP10 registrada en estación SAPU. Período 2019-2021 ...................... 18
**Tabla** **7.** Concentración anual de MP10 registrada en estación Quinel. Período 2019-2021 .................... 18
**Tabla** **8.** Percentil 99 de los máximos diarios de concentración de 1 hora de NO2 registrada en la estación

SAPU. Periodo 2019 - 2021. ..................................................................................................... 19

**Tabla** **9** . Percentil 99 de los máximos diarios de concentración de 1 hora de NO2 registrada en la estación
Quinel. Periodo 2019 - 2021. ................................................................................................... 19

**Tabla** **10** . Concentración anual NO2 registrada en la estación SAPU. Periodo 2019 - 2021. ...................... 19
**Tabla** **11** . Concentración anual NO2 registrada en la estación Quinel. Periodo 2019 - 2021. .................... 20
**Tabla** **12** . Percentil 98,5 de las concentraciones de 1 hora de SO2 registrada en la estación SAPU. Periodo

2019 - 2021. ............................................................................................................................ 20

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ iii

**Tabla** **13.** Percentil 99 de las concentraciones de 24 horas de SO2 registrada en la estación SAPU. Periodo

2019 - 2021. ............................................................................................................................ 20

**Tabla** **14** . Concentración anual SO2 registrada en la estación SAPU. Periodo 2019 - 2021. ....................... 21
**Tabla** **15.** Características del dominio de modelación de la segunda grilla utilizada por el modelo WRF en la

zona de Estudio. ...................................................................................................................... 24

**Tabla** **16** . Configuración de las principales parametrizaciones utilizadas en la modelación con WRF para la

zona de Estudio. ...................................................................................................................... 25

**Tabla** **17** . Estadísticos matemáticos de literatura. .................................................................................... 32

**Tabla** **18** . Resultados estadísticos obtenidos de la comparación de datos observados y modelados con WRF

en las estaciones del dominio de la zona de Estudio ................................................................. 40

**Tabla** **19** . Actividades del Proyecto generadoras de emisiones atmosféricas. ........................................... 41
**Tabla** **20** . Peso promedio vehículos del proyecto. .................................................................................... 45
**Tabla** **21** . Factores de emisión por contaminante según tipo de vehículo, en gramos por kilómetros de

vehículos recorrido. ................................................................................................................. 47

**Tabla** **22** . Factores de emisión por contaminante según potencia, tecnología Stage II, en gramos por kilowatt

hora. ....................................................................................................................................... 48

**Tabla** **23** . Factor de deterioro relativo a la vida útil de maquinaria diésel. ................................................ 49
**Tabla** **24** . Factor de ajuste transiente para maquinaria diésel. ................................................................. 49
**Tabla** **25** . Factor de emisión según potencia de grupo electrógeno. ......................................................... 50
**Tabla** **26** . Factores de emisión de MP10 del proyecto Parque Eólico Dañicalqui. ...................................... 51
**Tabla** **27** . Factores de emisión de MP2,5 del proyecto Parque Eólico Dañicalqui. ..................................... 52
**Tabla** **28** . Factores de emisión de MPS del proyecto Parque Eólico Dañicalqui. ........................................ 53
**Tabla** **29** . Factores de emisión de Gases del proyecto Parque Eólico Dañicalqui. ...................................... 54
**Tabla** **30** . Cronograma de actividades de la fase de Construcción del proyecto Parque Eólico Dañicalqui. 57
**Tabla** **31** . Factores utilizados para calcular los niveles de actividad del proyecto Parque Eólico Dañicalqui. ..

.............................................................................................................................................. 58

**Tabla** **32** . Nivel de actividad correspondiente a excavación del proyecto Parque Eólico Dañicalqui. ......... 58
**Tabla** **33** . Nivel de actividad correspondiente a carguío de material del proyecto Parque Eólico Dañicalqui..

.............................................................................................................................................. 59

**Tabla** **34** . Nivel de actividad correspondiente a descarga de material del proyecto Parque Eólico Dañicalqui.

.............................................................................................................................................. 59

**Tabla** **35** . Nivel de actividad correspondiente a compactación del proyecto Parque Eólico Dañicalqui. ..... 60
**Tabla** **36** . Nivel de actividad correspondiente a escarpe del proyecto Parque Eólico Dañicalqui. .............. 60
**Tabla** **37** . Cantidad de maquinaria fuera de ruta y horas de operación del proyecto Parque Eólico Dañicalqui.

.............................................................................................................................................. 61

**Tabla** **38** . Nivel de actividad correspondiente a maquinaria fuera de ruta del proyecto Parque Eólico
Dañicalqui. .............................................................................................................................. 61
**Tabla** **39** . Cantidad de viajes ida y vuelta y kilómetros a recorrer por caminos no pavimentados externos e
internos en la fase de construcción del proyecto Parque Eólico Dañicalqui, por tipo de vehículo. .

.............................................................................................................................................. 63

**Tabla** **40** . Distancias de caminos externos e internos con supresor de polvo en la fase de construcción del
proyecto Parque Eólico Dañicalqui. .......................................................................................... 66
**Tabla** **41** . Nivel de actividad correspondiente a distancia a recorrer por tránsito vehicular en caminos
externos e internos no pavimentados del proyecto Parque Eólico Dañicalqui, considerando sin y
con supresor de polvo.............................................................................................................. 67
**Tabla** **42** . Cantidad de viajes ida y vuelta y kilómetros a recorrer por caminos pavimentados en ruta N-85 en
la fase de construcción del proyecto Parque Eólico Dañicalqui, por tipo de vehículo. ................ 69
**Tabla** **43** . Cantidad de viajes y kilómetros a recorrer por caminos pavimentados en rutas 5 y 152 en la fase
de construcción del proyecto Parque Eólico Dañicalqui, por tipo de vehículo............................ 70
**Tabla** **44** . Nivel de actividad correspondiente a distancia a recorrer por tránsito vehicular en caminos
pavimentados del proyecto Parque Eólico Dañicalqui. .............................................................. 71

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ iv

**Tabla** **45** . Nivel de actividad correspondiente a distancia a recorrer por tránsito vehicular en caminos
pavimentados y no pavimentados para combustión de motores vehiculares del proyecto Parque
Eólico Dañicalqui. .................................................................................................................... 71
**Tabla** **46** . Nivel de actividad correspondiente a erosión eólica de la fase de construcción del proyecto Parque
Eólico Dañicalqui. .................................................................................................................... 72
**Tabla** **47** . Nivel de actividad correspondiente a funcionamiento de grupos electrógenos durante la fase de
construcción del proyecto Parque Eólico Dañicalqui. ................................................................ 72
**Tabla** **48** . Cantidad de viajes y kilómetros a recorrer por caminos no pavimentados externos e internos en
la fase de operación del proyecto Parque Eólico Dañicalqui, por tipo de vehículo. .................... 73
**Tabla** **49** . Nivel de actividad correspondiente a distancia a recorrer por tránsito vehicular en caminos
externos e internos no pavimentados en la fase de operación del proyecto Parque Eólico
Dañicalqui. .............................................................................................................................. 73
**Tabla** **50** . Cantidad de viajes y kilómetros a recorrer por caminos pavimentados en la fase de operación del
proyecto Parque Eólico Dañicalqui, por tipo de vehículo. ......................................................... 74
**Tabla** **51** . Nivel de actividad correspondiente a distancia a recorrer por tránsito vehicular en caminos
pavimentados de la fase de operación del proyecto Parque Eólico Dañicalqui. ......................... 74
**Tabla** **52** . Nivel de actividad correspondiente a distancia a recorrer por tránsito vehicular en caminos
pavimentados y no pavimentados para combustión de motores vehiculares de la fase de
operación del proyecto Parque Eólico Dañicalqui. .................................................................... 75
**Tabla** **53** . Cantidad de maquinaria fuera de ruta y horas de operación del proyecto Parque Eólico Dañicalqui,
fase de operación. ................................................................................................................... 75
**Tabla** **54** . Nivel de actividad correspondiente a maquinaria fuera de ruta del proyecto Parque Eólico
Dañicalqui, fase de operación. ................................................................................................. 75
**Tabla** **55** . Nivel de actividad correspondiente a funcionamiento de grupos electrógenos durante la fase de
construcción del proyecto Parque Eólico Dañicalqui. ................................................................ 76
**Tabla** **56** . Emisiones de MP10 debido a las actividades de la fase de Construcción del Proyecto Parque Eólico
Dañicalqui, Sectores Parque Eólico (PE) y Línea de Transmisión (LT). ........................................ 77
**Tabla** **57** . Emisiones de MP2,5 debido a las actividades de la fase de Construcción del Proyecto Parque Eólico
Dañicalqui, Sectores Parque Eólico (PE) y Línea de Transmisión (LT). ........................................ 80
**Tabla** **58** . Emisiones de MPS debido a las actividades de la fase de Construcción del Proyecto Parque Eólico
Dañicalqui, Sectores Parque Eólico (PE) y Línea de Transmisión (LT). ........................................ 84
**Tabla** **59** . Emisiones de NOx debido a las actividades de la fase de Construcción del Proyecto Parque Eólico
Dañicalqui, Sectores Parque Eólico (PE) y Línea de Transmisión (LT). ........................................ 88
**Tabla** **60** . Emisiones de CO debido a las actividades de la fase de Construcción del Proyecto Parque Eólico
Dañicalqui, Sectores Parque Eólico (PE) y Línea de Transmisión (LT). ........................................ 89
**Tabla** **61** . Emisiones de SOx debido a las actividades de la fase de Construcción del Proyecto Parque Eólico
Dañicalqui, Sectores Parque Eólico (PE) y Línea de Transmisión (LT). ........................................ 90
**Tabla** **62** . Emisiones de HC debido a las actividades de la fase de Construcción del Proyecto Parque Eólico
Dañicalqui, Sectores Parque Eólico (PE) y Línea de Transmisión (LT). ........................................ 91
**Tabla** **63** . Emisiones de MP10 debido a las actividades de la fase de Operación del Proyecto Parque Eólico
Dañicalqui, Sectores Parque Eólico (PE) y Línea de Transmisión (LT). ........................................ 93
**Tabla** **64** . Emisiones de MP2,5 debido a las actividades de la fase de Operación del Proyecto Parque Eólico
Dañicalqui, Sectores Parque Eólico (PE) y Línea de Transmisión (LT). ........................................ 94
**Tabla** **65** . Emisiones de MPS debido a las actividades de la fase de Operación del Proyecto Parque Eólico
Dañicalqui, Sectores Parque Eólico (PE) y Línea de Transmisión (LT). ........................................ 95
**Tabla** **66** . Emisiones de NOx debido a las actividades de la fase de Operación del Proyecto Parque Eólico
Dañicalqui, Sectores Parque Eólico (PE) y Línea de Transmisión (LT). ........................................ 96
**Tabla** **67** . Emisiones de CO debido a las actividades de la fase de Operación del Proyecto Parque Eólico
Dañicalqui, Sectores Parque Eólico (PE) y Línea de Transmisión (LT). ........................................ 96
**Tabla** **68** . Emisiones de SOx debido a las actividades de la fase de Operación del Proyecto Parque Eólico
Dañicalqui, Sectores Parque Eólico (PE) y Línea de Transmisión (LT). ........................................ 97
**Tabla** **69** . Emisiones de HC debido a las actividades de la fase de Operación del Proyecto Parque Eólico
Dañicalqui, Sectores Parque Eólico (PE) y Línea de Transmisión (LT). ........................................ 98

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ v

**Tabla** **70** . Resumen de emisiones de MP10, MP2,5, MPS, NOx, CO, SOx y HC debido a las actividades de
construcción del Proyecto Parque Eólico Dañicalqui, Sector Parque Eólico (PE). ....................... 99
**Tabla** **71** . Resumen de emisiones de MP10, MP2,5, MPS, NOx, CO, SOx y HC debido a las actividades de
construcción del Proyecto Parque Eólico Dañicalqui, Sector Línea de Transmisión (LT). .......... 100
**Tabla** **72** . Resumen de emisiones de MP10, MP2,5, MPS, NOx, CO, SOx y HC de la fase de construcción del
Proyecto Parque Eólico Dañicalqui. ........................................................................................ 101
**Tabla** **73** . Resumen de emisiones de MP10, MP2,5, MPS, NOx, CO, SOx y HC debido a las actividades de
construcción del Proyecto Parque Eólico Dañicalqui, Sector Parque Eólico (PE). ..................... 102
**Tabla** **74** . Resumen de emisiones de MP10, MP2,5, MPS, NOx, CO, SOx y HC de la fase de operación del
Proyecto Parque Eólico Dañicalqui. ........................................................................................ 103
**Tabla** **75** . Resumen de emisiones de MP10, MP2,5, MPS, NOx, CO, SOx y HC de la fase de cierre del Proyecto
Parque Eólico Dañicalqui. ....................................................................................................... 103
**Tabla** **76** . Características del dominio de modelación utilizada por el modelo CALPUFF en la zona del
Proyecto Parque Eólico Dañicalqui (archivo CALPUFF-Ready). ................................................ 105
**Tabla** **77** . Características del área de receptores de Grilla. ..................................................................... 106
**Tabla** **78** . Coordenadas de receptores de interés en la zona del Proyecto. ............................................. 108
**Tabla** **79** . Emisiones de MP10, MP2,5, MPS, NO2, SO2 y CO del primer año de construcción del Proyecto
Parque Eólico Dañicalqui. ....................................................................................................... 111
**Tabla** **80** . Coordenadas de las áreas donde se implementaron las fuentes emisoras de contaminantes
atmosféricos en el modelo CALPUFF. ..................................................................................... 112

**Tabla** **81** . Coordenadas de los tramos de zanja del circuito MT donde se implementaron las fuentes emisoras

de contaminantes atmosféricos en el modelo CALPUFF. ......................................................... 120

**Tabla** **82** . Coordenadas de los tramos de caminos donde se implementaron las fuentes emisoras de

contaminantes atmosféricos en el modelo CALPUFF. ............................................................. 124

**Tabla** **83** . Resultados de MP10 promedio anual y percentil 98 de las concentraciones diarias modeladas por

el sistema CALPUFF. ............................................................................................................... 141

**Tabla** **84** . Resultados de MP2,5 promedio anual y percentil 98 de las concentraciones diarias modeladas por

el sistema CALPUFF. ............................................................................................................... 146

**Tabla** **85** . Resultados de MPS promedio anual y máximo mensual modeladas por el sistema CALPUFF... 150
**Tabla** **86** . Resultados de NO2 promedio anual y percentil 99 de las máximas diarias concentraciones horarias
modeladas por el sistema CALPUFF. ....................................................................................... 153
**Tabla** **87** . Resultados de SO2 promedio anual, percentil 99 de las concentraciones diarias y percentil 98,5
de las concentraciones horarias modeladas por el sistema CALPUFF. ..................................... 157
**Tabla** **88** . Resultados de SO2 promedio anual, percentil 99,7 de las concentraciones diarias y percentil 99,73
de las concentraciones horarias modeladas por el sistema CALPUFF. ..................................... 159
**Tabla** **89** . Resultados de CO percentil 99 de las máximas diarias concentraciones de 8 y 1 horas modeladas
por el sistema CALPUFF. ........................................................................................................ 166
**Tabla** **90** . Resumen de los aportes de contaminantes atmosféricos que efectuará el Proyecto. .............. 171
**Tabla** **91** . Estimación del impacto del Proyecto Parque Eólico Dañicalqui a las concentraciones de MP10,
NO2 y SO2 observadas en la estación SAPU............................................................................ 174
**Tabla** **92** . Estimación del impacto del Parque Eólico Dañicalqui a las concentraciones de MP10 y NO2
observadas en la estación Quinel. .......................................................................................... 174

**Tabla** **93** . Distancias de caminos externos e internos con supresor de polvo en la fase de construcción del
proyecto Parque Eólico Dañicalqui. ........................................................................................ 182
**Tabla** **94** . Periodicidad de ejecución ...................................................................................................... 187

**Tabla** **95** . Frecuencia de mantención ..................................................................................................... 187

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ vi

**A.** **PRESENTACIÓN**

En el presente informe se expone la estimación y modelación de emisiones atmosféricas actualizadas del

proyecto denominado Parque Eólico Dañicalqui, según las observaciones realizadas en el Informe

Consolidado de Solicitud de Aclaraciones, Rectificaciones o Ampliaciones a la Declaración de Impacto

Ambiental del proyecto "Parque Eólico Dañicalqui", por lo que, la información añadida en Adenda se

presenta en **color azul.**

El Proyecto Eólico Dañicalqui, se encuentra ubicado entre las comunas de Yungay y Pemuco, Provincia de
Diguillín, Región del Ñuble, **Figura 1**, aproximadamente a 8,6 km al Suroeste de Pemuco, específicamente

en la ribera sur del Río Dañicalqui. El Proyecto, consiste en la construcción y operación de parque eólico

que consta de 14 aerogeneradores y una línea de transmisión de 220 kV, con una longitud de 5,37 km,

alcanzando una potencia máxima de 95,2 MW. Para la evacuación de su energía al Sistema Eléctrico

Nacional (SEN), el Proyecto contempla la conexión a la subestación Entre Ríos, propiedad de Transelec.

**Figura 1** . Proyecto Parque Eólico Dañicalqui.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 1

Para el logro de los objetivos del estudio, en primer lugar, se procedió a la elaboración de la línea base

meteorológica y de calidad del aire mediante la descargada de datos disponibles de las estaciones de la

Red SINCA y Dirección Meteorológica de Chile (DMC).

Posteriormente se realizó la modelación meteorológica con Weather Research and Forecast Model (WRF)

en modo diagnóstico para obtener la meteorología de las zonas del Proyecto, la cual fue utilizada como

datos de entrada para la ejecución del modelo de dispersión CALPUFF.

En segundo lugar, se actualizó el Inventario de Emisiones del Proyecto para las fases de construcción,

operación y cierre del Proyecto, según las observaciones del ICSARA correspondientes a estimación de

emisiones. En esta actualización se incorporan las emisiones de la fase de cierre como el escenario más

desfavorecedor de emisiones, además se incluye lo siguiente:

 - Actualización de factores de emisión por tránsito de vehículos en caminos no pavimentados,

considerando la fracción W/2,72 en lugar de W/3.

 - Actualización de factores de emisión por tránsito de vehículos en caminos pavimentados,

considerando la ponderación del peso promedio W por 1,1023 (Wx1,1023).

 - Actualización de factores de emisión de grupos electrógenos, utilizando la fórmula de la Guía para

la Estimación de Emisiones Atmosféricas en la Región Metropolitana, (octubre, 2020)

 - Actualización del Nivel de actividad por Compactación utilizando fórmula para obtener horas de

compactación y actualizando las áreas a compactar.

 - Actualización del Nivel de actividad por Escarpe actualizando las superficies a escarpar.

 - Se actualizan las emisiones de la planta de Hormigón.

Finalmente, se realizó la modelación de contaminantes atmosféricos que consideran las emisiones de la

fase de construcción y cierre actualizadas, considerado como el peor escenario de emisiones atmosféricas,

y con esto se obtuvieron las isolíneas de concentración del área circundante al Proyecto y los aportes de

contaminantes atmosféricos debido a las actividades del Proyecto. Esto se llevó a cabo con el uso del

sistema de modelación WRF/CALPUFF, recomendado por el Servicio de Evaluación Ambiental (SEA) y EPA

(USA) para emisiones en terreno complejo. Este sistema se aplicó considerando los siguientes escenarios

meteorológico, topográfico y de emisiones:

 - Escenario Meteorológico: Corresponde al año 2021.

 - Escenario Topográfico: La zona de estudio considera un área de 95 x 95 km [2], cubriendo la zona

del Proyecto.

 - Escenarios de Emisiones: Considera las emisiones del escenario de Construcción actualizado, el

que se distribuye durante dos años, siendo el primer año el más alto en emisiones atmosféricas

(ver **Tabla 72** ).

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 2

**B.** **OBJETIVOS**

**B.1** **General**

El objetivo de este estudio consiste en evaluar el impacto en la calidad del aire en el área de influencia del
Proyecto Parque Eólico Dañicalqui, ubicado en la Región del Ñuble, siguiendo los lineamientos según lo

indicado en la “Guía para el uso de modelos de calidad del aire en el SEIA”.

**B.2** **Específicos**

 - Caracterizar la meteorología y la calidad del aire de la zona en estudio.

 - Modelar la meteorología de la zona de estudio con el modelo WRF para el año 2021.

 - Actualizar el Inventario de Emisiones de contaminantes atmosféricos para las fases de

construcción y operación del Proyecto, según las observaciones correspondientes del ICSARA de

la DIA.

 - Modelar la dispersión de contaminantes atmosféricos mediante el sistema CALPUFF,

considerando el inventario actualizado.

 - Obtener los aportes de contaminantes atmosféricos del proyecto y evaluar su impacto en la

calidad del aire.

 - Determinar el área de Influencia de las emisiones atmosféricas del Proyecto

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 3

**C.** **ÁREA DE INFLUENCIA**

Como se presenta en la “Guía para el uso de modelos de calidad del aire en el SEIA” (SEA, 2023) y “Guía
sobre el Área de Influencia en el Sistema de Evaluación de Impacto Ambiental” del SEA (2017): En la letra

a) del artículo 2 del Reglamento del SEIA se define área de influencia (AI) como ‘El área o espacio

geográfico, cuyos atributos, elementos naturales o socioculturales deben ser considerados con la finalidad

de definir si el proyecto o actividad genera o presenta alguno de los efectos, características o

circunstancias del artículo 11 de la Ley, o bien para justificar la inexistencia de dichos efectos,

características o circunstancias’.

En este contexto se obtuvo el área de Influencia en calidad del aire del Proyecto, la que se presenta en la

**Figura 2** . Los criterios de su definición se presentan en **G.3.8. Determinación del área de influencia** del
presente documento y en **Capítulo 2. Determinación y Justificación del Área de Influencia** de la **DIA** .

**Figura 2.** Área de Influencia para Calidad de Aire.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 4

**D.** **INFORMACIÓN METEOROLÓGICA Y DE CALIDAD DE AIRE DE LA ZONA DE ESTUDIO**

**D.1.** **Introducción y breve descripción de zona de estudio**

El Proyecto se ubica entre las comunas de Yungay y Pemuco, Provincia de Diguillín, ambas comunas
pertenecientes a la región de Ñuble, aproximadamente a 8,6 km al Suroeste de Pemuco, específicamente

en la ribera sur del Río Dañicalqui. Este río es importante debido a que es el principal curso que drena la
sección latitudinal centro-sur de la región de Ñuble. Con una cuenca de 1.386 km [2], este río va colectando

los aportes de los cursos cordilleranos y sirve de suplemento de aguas destinadas al regadío a la zona

(BCN, 2022).

En términos demográficos las Comunas de Yungay y Pemuco tienen una población de 17.787 y 8.448

respectivamente, siendo Yungay la más numerosa en términos de asentamientos (INE, 2017).

Las principales actividades económicas se encuentran ligadas principalmente al sector agrícola y forestal.

A continuación, se presenta una descripción de la zona donde se emplazará el Proyecto Parque Eólico

Dañicalqui, considerando aspectos tales como: descripción topográfica y climática del área del proyecto.

Finalmente, en **sección D.3.** se presenta la información meteorológica de la estación más cercana al

proyecto, tal como lo recomienda la “Guía para el uso de Modelos de Calidad del Aire en el SEIA” (SEA,

2023)

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 5

.

**D.2.** **Descripción Topográfica y Climática de la Zona de Estudio**

El clima de la zona corresponde al templado de tipo mediterráneo, característico del valle central
longitudinal de la región de Ñuble. Este tipo de clima está moldeado por las condiciones sinópticas

subtropicales en Chile Central (PLADECO, 2018). Los pasos de sistemas frontales hacia el continente se

asocian a condiciones de inestabilidad ciclonal de invierno, en la medida que la celda de alta presión,

llamada anticiclón del pacífico sur se desplaza hacia el norte del Chile, dejando bajo predominio de masas

de aire frías y polares a las latitudes medias y altas de Chile. Durante los meses de verano, se producen

condiciones de déficit de precipitaciones o meses secos, correspondientes a condiciones estables

producto del desplazamiento hacia el sur del anticiclón descrito (Umaña, 2015).

Lo anterior trae como consecuencia que respecto a las precipitaciones en el periodo de invierno precipite

un 65 a 70% del total anual, mientras que en verano solo 5 a 6% (Umaña, 2015). En específico la media

anual es de aproximadamente 1.025 mm siendo el mes de julio más lluvioso, con 217 mm. (PLADECO,

2018).

Respecto al régimen térmico se caracteriza por una temperatura media anual de 14 °C, con la máxima en

el mes de enero de 28,8°C y la mínima en Julio de 3,5°C (PLADECO, 2018).

Respecto a la topografía de la región, a nivel macro la región de Ñuble presenta cuatro unidades

principales; Cordillera de los Andes, depresión intermedia, cordillera de la costa y planicies litorales. En

**Figura 3** se muestra la topografía de zona.

La cordillera de los Andes presenta alturas que bordean los 2.000 msnm. Destaca el complejo volcánico

Nevados de Chillán cuyas principales alturas corresponden a Volcán Nevado (3.212. msnm) y Volcán

Chillán (3.172 msnm).

Entre la Cordillera de los Andes y la depresión intermedia se presenta una formación transicional, llamada

Cordillera de Punilla o “la Montaña”, que corresponde a una estructura del relieve que se proyecta en la

zona de contacto entre ambas franjas del territorio descritas, a veces nombrada como precordillera y que
atraviesa el sur de la región del Maule y una amplia porción de la región de Ñuble.

La depresión intermedia o Valle Longitudinal se caracteriza por tener una topografía uniforme,

desarrollándose desde el pie occidental de la precordillera, hasta el contacto con la Cordillera de la Costa.

En general su desarrollo puede llegar a extensiones de hasta 80 kilómetros, aun cuando en promedio

fluctúa en torno a los 60 a 70 kilómetros de ancho, y cuya principal constitución litológica son gravas y

cantos rodados provenientes de la acción fluvio-glacial y volcánica del cuaternario reciente (menores a 2

millones de años antes del presente) (BCN, 2022).

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 6

A pesar de ser una sección homogénea se encuentra interrumpida por una serie de escorrentías menores

que fluyen desde la Cordillera de los Andes, hacia el Oeste.

La Cordillera de la Costa se presenta con alturas bajas y ondulada, con altitudes promedio inferiores a 400
msnm. En Ñuble destacan algunas elevaciones tales como Cerro Coiquén (908 m.s.n.m), el Cerro Guallipén

(774 m.s.n.m), y Cerro El Rincón (726 m.s.n.m). Uno de los principales aspectos es la generación de algunas

cuencas interiores, traducidos en pequeños valles interiores encerrados por cordones montañosos,

dentro de los que tienen mayor relevancia está el de Quirihue (BCN, 2022).

Finalmente, respecto a las planicies costeras, éstas se presentan variables, a lo largo de la región. Estas se

desarrollan muy estrechas o casi inexistentes, mientras que habitualmente en las desembocaduras de los

drenes locales se presentan más amplias, como en el estuario del Río Itata, o en las localidades de

Cobquecura y Buchupureo (BCN, 2022).

_Fuente: https://es-es.topographic-map.com/maps/tyvu/Chile/._

**Figura 3.** Mapa Topográfico de la Zona.

**D.3.** **Línea Base Meteorológica de la Zona de Estudio Durante el Año 2021**

La red meteorológica utilizada del área de interés corresponde a la extraída desde el sitio web SINCA para

la estación Purén, del año 2021. Esta estación es la más cercana al proyecto y se encuentra localizada en
la comuna de Chillán, Región de Ñuble, como se muestra en **Figura 4** .

La **Tabla 1** muestra el porcentaje de datos válidos de las estaciones escogidas para las variables velocidad

y dirección de viento, humedad relativa y temperatura, donde todas superan el 75% como mínimo de

datos de calidad asegurada.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 7

Respecto al tratamiento de los datos, estos fueron revisados y validados siguiendo los lineamientos de la

EPA, en relación con registros incoherentes, datos sin variación o saltos bruscos entre horas de cada

variable y revisión de variabilidad diaria y estacional.

**Tabla 1.** Estaciones meteorológicas en el dominio de la zona de Estudio.

|Estación|Latitud<br>(°)|Longitud<br>(°)|Variable medidas (%)|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**Estación**|**Latitud**<br>**(°)**|**Longitud**<br>**(°)**|**VV**|**DV**|**HR**|**T **|
|Purén|-36.616|-72.093|100|100|100|100|

_VV: velocidad de viento;_ _DV: dirección de viento;_ _HR: Humedad Relativa;_ _T: temperatura_

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 8

_Fuente: Cartografía Interactiva de los climas de Chile [en línea]._
**Figura 4.** Área de estudio, ubicación del proyecto y estación meteorológica.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 9

**D.3.1.** **Series de Tiempo de Variables Meteorológicas Observadas en el Año 2021**

La **Figura 5** muestra las series de tiempo de las variables meteorológicas de la estación Purén. En esta

figura se visualiza integridad de los datos en todo el periodo en todas las variables.

Respecto a la descripción de la magnitud de la velocidad de viento, se visualiza un leve aumento de la

magnitud en el periodo de verano en promedio, mientras que en invierno se ven unos máximos puntuales

que podrían corresponden a ráfagas por sistemas frontales que ocurren en la temporada invernal (ver

D.2. Descripción Topográfica y Climática de la Zona).

Respecto a la dirección de viento se visualiza viento Sur prácticamente durante todo el año y a la humedad

relativa muestra bajas magnitudes en los meses estivales, mientras que en invierno ocurren los máximos.

Finalmente comentando la temperatura, se observan las mayores magnitudes en los meses de verano,

mientras que las mínimas en los meses de invierno.

**Figura 5.** Series de tiempo de variables meteorológicas observadas en la estación Purén durante el año

2021.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 10

**D.3.2.** **Ciclos Diarios de Variables Meteorológicas Observadas Durante el Año 2021**

Los ciclos diarios son construidos en base a los registros promedios de cada hora de todo el año, con el fin

de mostrar un comportamiento patrón de una cierta variable, en este caso meteorológica. El área

sombreada corresponde al área delimitada por los percentiles 5 y 95, el cual tiene como objetivo

caracterizar la variabilidad de la velocidad del viento, humedad relativa y temperatura.

Un poco distinto es lo que se visualiza en el ciclo de dirección de viento, el cual muestra la frecuencia en

términos de porcentaje de las direcciones de viento registradas, cada 22,5° a lo largo de todas las horas,

desde 0:00 hasta 23:00, de todo el año.

En la **Figura 6**, se muestran los ciclos diarios de las observaciones en estación Purén.

Respecto a la velocidad de viento se visualiza un aumento de la magnitud en el día, alcanzando su máximo

entre las 16:00 y 17:00 horas y el mínimo a las 6:00 horas. Respecto a la amplitud, esta no es grande en

magnitud, visualizado en el área delimitada por los percentiles 5 y 95, lo que significa que la tendencia de

vientos es más bien de ocurrencia de calmas en promedio.

La dirección de viento presenta viento dominante Suroeste en promedio durante todas las horas del día,

siendo más marcado durante la noche que en el día con un 40% de la frecuencia en la noche, y un 30% en

el día.

El ciclo de la humedad relativa muestra la curva promedio mínima entre las 16:00 y 18:00 horas y la curva

promedio máxima a eso de las 6:00 de la mañana. El percentil 95 es prácticamente constante durante la

noche

Respecto a la temperatura ocurre lo inverso que la humedad relativa, con máxima magnitud entre las

16:00, 18:00 horas (sobre los 30°C percentil 95) y el mínimo aproximadamente a las 06:00 de la mañana.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 11

**Figura 6.** Ciclos diarios de variables meteorológicas observadas en la estación Purén durante el año

2021.

**D.3.3.** **Ciclos Estacionales de Variables Meteorológicas Observados Durante el Año 2021**

Los ciclos estacionales corresponden a gráficos donde se muestra el ciclo diario en el eje x y el ciclo anual

en el eje y. La escala de color muestra la magnitud de la variable, donde el color rojo muestra valores

máximos y los colores azules los mínimos. En particular, en el ciclo estacional de velocidad de viento se

superponen vectores de viento en la imagen, con la finalidad de mostrar la dirección de viento

predominante promedio a lo largo del día y del año.

La **Figura 7** muestra los ciclos estacionales de los registros observados para estación Purén

Respecto a la velocidad de viento, se visualiza máximos de velocidad en los periodos diurnos y meses

verano, y lo inverso en los periodos nocturnos y meses de invierno.

Respecto a la dirección de viento, se visualiza vientos Suroeste en los meses de verano, mientras que en

invierno se adiciona una componente Norte. No se aprecia cambio de patrón de viento entre día y noche.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 12

Respecto a la humedad relativa se visualiza que en los meses de invierno y periodo de noche la magnitud

es casi el 100%, mientras que en verano y en el día es mínima.

Finalmente comentando el ciclo de la temperatura, se visualiza lo inverso a la humedad relativa, con

máximos en el día y en los meses de verano, y mínimos en invierno y en la noche.

**Figura 7.** Ciclos estacionales de variables meteorológicas observadas en estación Purén durante el año

2021.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 13

**D.3.4.** **Rosas de Viento Observadas durante el Año 2021**

La variabilidad de la velocidad y dirección del viento es caracterizada mediante las rosas de viento

solicitadas por el documento oficial, “Guía para el uso de Modelos de Calidad del Aire en el SEIA”.

Adicionalmente las rosas de viento sirven para complementar el análisis del ciclo diario de los vientos

mostrados en la **Figura 6** .

En la **Figura 8** se presentan cuatro rangos de tiempo horarios para estación Purén, los cuales son descritos

a continuación:

 - Periodo noche o madrugada, 01:00 a 06:00 horas: predomina viento Suroeste y vientos de 2 m/s

como máximo.

 - Periodo mañana, 07:00 a 14:00 horas: sigue predominando viento Suroeste y con magnitud de 3

m/s como máximo.

 - Periodo tarde, 15:00 a 23:00 horas: el viento dominante corresponde a Suroeste y vientos de 3

m/s como máximo.

 - Periodo completo, 00:00 a 23:00 horas: sigue predominando viento Suroeste con vientos de 3 m/s

como máximo.

**Figura 8.** Rosas de viento de observaciones en estación Puren durante el año 2021.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 14

**D.4.** **Línea Base de calidad del aire de la zona de Estudio**

En esta sección se presenta la línea base de calidad de aire de la zona de Estudio, de acuerdo con la

información ambiental registrada por las estaciones de propiedad de la empresa Masisa y operadas por

la empresa SERPRAM, Sapu y Quinel cuyos datos fueron obtenidas del sitio web SNIFA.

Los estadísticos disponibles de los años 2019, 2020 y 2021 corresponden a las especies MP10, NO 2 y SO 2 .

La metodología empleada para la caracterización de la calidad del aire del área de influencia del Proyecto

incluye la localización de la estación de monitoreo, el análisis estadístico y comparativo con normativa

asociada a la calidad del aire.

**D.4.1.** **Marco jurídico vigente en Chile**

Dentro del marco jurídico vigente en Chile existen las Normas Primarias de Calidad de Aire, las cuales han

sido establecidas a través del Ministerio Secretaría General de la Presidencia (MINSEGPRES) o el Ministerio

del Medio Ambiente. También existen Normas Secundarias de Calidad de Aire, establecidas por el

MINSEGPRES o el Ministerio de Agricultura.

Los valores límites y su periodo de evaluación para los contaminantes de interés MP10, MP2,5, NO 2, SO 2

CO y MPS de las normas primarias y secundarias de calidad de aire vigentes en Chile se presentan en **Tabla**

**2** .

**Tabla 2.** Normas Primarias y Secundarias de calidad de aire de Chile para contaminantes atmosféricos.

|Contaminante|Periodo de Evaluación|Valor Norma|Norma|
|---|---|---|---|
|Material Particulado<br>Respirable<br>(MP10)|Concentración de 24 horas|130 (μg/Nm3)|Norma Primaria<br>D.S. No 12/2022 del<br>MINISTERIO DEL MEDIO<br>AMBIENTE|
|Material Particulado<br>Respirable<br>(MP10)|Concentración anual|50 (μg/Nm3)|50 (μg/Nm3)|
|Material Particulado Fino<br>Respirable (MP2,5)|Concentración de 24 horas|50 (μg/Nm3)|Norma Primaria<br>D.S. No 12/2011 del<br>MINISTERIO DEL MEDIO<br>AMBIENTE|
|Material Particulado Fino<br>Respirable (MP2,5)|Concentración anual|20 (μg/Nm3)|20 (μg/Nm3)|
|Dióxido de Nitrógeno<br>(NO2)|Concentración de 1 hora|400 (μg/Nm3)|Norma Primaria<br>D.S. No 114/2002 del<br>MINSEGPRES|
|Dióxido de Nitrógeno<br>(NO2)|Concentración anual|100 (μg/Nm3)|100 (μg/Nm3)|
|Dióxido de Azufre (SO2)|Concentración anual|60 (μg/Nm3)|Norma Primaria<br>D.S. No 104/2018 del<br>MINISTERIO DEL MEDIO<br>AMBIENTE|
|Dióxido de Azufre (SO2)|Concentración de 24 horas|150 (μg/Nm3)|150 (μg/Nm3)|
|Dióxido de Azufre (SO2)|Concentración de 1 hora|350 (μg/Nm3)|350 (μg/Nm3)|
|Dióxido de Azufre (SO2)|Concentración anual|80 (μg/Nm3)|Norma Secundaria<br>D.S. No 22/2009<br>MINSEGPRES para la zona<br>norte|
|Dióxido de Azufre (SO2)|Concentración de 24 horas|365 (μg/Nm3)|365 (μg/Nm3)|
|Dióxido de Azufre (SO2)|Concentración de 1 hora|1.000 (μg/Nm3)|1.000 (μg/Nm3)|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 15

|Contaminante|Periodo de Evaluación|Valor Norma|Norma|
|---|---|---|---|
|Monóxido de Carbono<br>(CO)|Concentración de 8 horas|10.000 (μg/Nm3)|Norma Primaria<br>D.S. No 115/2002 del<br>MINSEGPRES|
|Monóxido de Carbono<br>(CO)|Concentración de 1 hora|30.000 (μg/Nm3)|30.000 (μg/Nm3)|
|MPS|Concentración|100 (mg/m2-día)|D. Exento N° 4/1992 <br>MINISTERIO DE<br>AGRICULTURA|

Por otra parte, el área en que se emplazará el Proyecto no se encuentra regulada por ningún Plan de

Prevención y/o Descontaminación Atmosférica (PPDA), los PPDA más cercanos al Proyecto están
emplazados en las ciudades de Los Ángeles y Chillán, por otro lado, tampoco se ha declarado zona latente

o saturada por ningún contaminante atmosférico y ninguna de las estaciones consideradas en el presente

estudio cuenta con clasificación de “Estación de Monitoreo con Representatividad Poblacional” (EMRP)

por consiguiente, la información recopilada por éstas no permite verificar el cumplimiento de las normas

de calidad del aire. La calificación EMRP se obtiene mediante resolución de la Superintendencia de Medio

Ambiente (SMA), presentando todos los antecedentes técnicos que permitan verificar y asegurar que las

condiciones de emplazamiento y características técnicas de los equipos, cumplen ciertas condiciones que

aseguren que las mediciones registradas representan una condición general de la zona que se desea

representar y no son reflejo de eventos particulares y aislados (como una industria que impacta

directamente sobre la estación y no tiene impacto en toda la población de una ciudad), que alteren las

mediciones.

**D.4.2.** **Descripción de la red de monitoreo de calidad del aire en la zona de Estudio**

Las estaciones SINCA más cercanas corresponden a Chillán y Los Ángeles, las cuales fueron descartadas

para el análisis dada la distancia que existe entre éstas y el Proyecto (44 y 54 km, respectivamente). Para

determinar las estaciones de monitoreo de calidad del aire, se realizó una búsqueda identificando

aquellos proyectos ingresados al SEA que reportan monitoreo horario de calidad del aire a la

Superintendencia de Medio Ambiente en el Sistema Nacional de Información de Fiscalización Ambiental.

Por lo que, para caracterizar la calidad del aire del área en que se emplaza el Proyecto se han utilizado los

registros efectuados en dos estaciones de monitoreo instaladas por MASISA S.A. en la ciudad de Cabrero,

cuyo detalle se presenta en la **Tabla 3**, la estación SAPU que se encuentra dentro del Centro de Salud

Familiar (CESFAM) y la estación Quinel, la cual se ubica en una vivienda particular ubicada en la unión de

las calles Quinel y O’Higgins de la comuna de Cabrero. La ubicación de las estaciones se presenta en la

**Figura 9** .

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 16

Los registros para los años 2019 al 2021 fueron obtenidos desde los informes mensuales alojados en el

sitio web del Sistema Nacional de Información de Fiscalización Ambiental. Las estaciones no cuentan con

monitoreo de los contaminantes MP2,5, CO ni O 3 ni están clasificadas como Estación de Monitoreo con

Representación Poblacional (EMRP).

**Tabla 3** . Estaciones de monitoreo de calidad del aire

|Estación|Coordenadas UTM|Col3|Distancia al<br>Proyecto (km)|Altura sobre el<br>nivel del mar (m)|Contaminantes<br>medidos|
|---|---|---|---|---|---|
|**Estación**|**X (m)**|**Y (m)**|**Y (m)**|**Y (m)**|**Y (m)**|
|SAPU|731.369|5.897.676|18|130|MP10 - NO2 - SO2|
|Quinel|730.529|5.898.723|19|160|MP10 - NO2|

_Fuente: Sistema Nacional de Información de Fiscalización Ambiental._

**Figura 9.** Ubicación de las estaciones de calidad del aire respecto al Proyecto.

**D.4.3.** **Resultados MP10 Concentración Diaria**

En **Tabla 4** y **Tabla 5** se presentan los percentiles 98 de las concentraciones de 24 horas de MP10,

registrados en las estaciones SAPU y Quinel durante el periodo 2019-2021.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 17

Se aprecia que en estación SAPU no hay superación de norma, sin embargo, en estación Quinel, la

normativa es superada en un 62% para el año 2021.

**Tabla 4** . Percentil 98 de las concentraciones 24 horas de MP10 registrada por la estación SAPU.

Período 2019-2021.

|Año|Percentil 98 de las<br>Concentraciones 24 horas (μg/m3)|Norma D.S. No 59/1998 (μg/m3)|
|---|---|---|
|2019|107,8|**130**|
|2020|90,6|90,6|
|2021|110,7|110,7|

**Tabla 5** . Percentil 98 de las concentraciones 24 horas de MP10 registrada por la estación Quinel.

Período 2019-2021.

|Año|Percentil 98 de las<br>Concentraciones 24 horas (μg/m3)|Norma D.S. No 59/1998 (μg/m3)|
|---|---|---|
|2019|46,6|**130**|
|2020|91,4|91,4|
|2021|211,5|211,5|

**D.4.4.** **Resultados MP10 Concentración Anual**

En **Tabla 6** y **Tabla 7** se presentan los Percentiles 98 las concentraciones promedio anuales de MP10,

registrados en las estaciones SAPU y Quinel durante el periodo 2019-2021.

Se aprecia que en estación SAPU no hay superación de norma, sin embargo, en estación Quinel la

normativa es superada en un 48% para el año 2021.

**Tabla 6** . Concentración anual de MP10 registrada en estación SAPU. Período 2019-2021

|Año|Concentración Anual (μg/m3)|Norma D.S. No 12/2021 (μg/m3)|
|---|---|---|
|2019|38,2|**50**|
|2020|33,0|33,0|
|2021|31,1|31,1|
|**Promedio**|**34,1**|**34,1**|

**Tabla 7** . Concentración anual de MP10 registrada en estación Quinel. Período 2019-2021

|Año|Concentración Anual (μg/m3)|Norma D.S. No 12/2021 (μg/m3)|
|---|---|---|
|2019|15,1|**50**|
|2020|34,5|34,5|
|2021|73,9|73,9|
|**Promedio**|**41,1**|**41,1**|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 18

**D.4.5.** **Resultados NO** **2** **Concentración 1 hora**

En **Tabla 8** y **Tabla 9** se presentan los Percentiles 989 de las concentraciones de 1 hora de NO 2 registrados

en las estaciones SAPU y Quinel durante el periodo 2019-2021.

Se aprecia que en estación SAPU y Quinel no hay superación de norma, y los estadísticos están muy por

debajo del límite normativo.

**Tabla 8** . Percentil 99 de los máximos diarios de concentración de 1 hora de NO 2 registrada en la

estación SAPU. Periodo 2019 - 2021.

|Año|Percentil 99 de los máximos diarios<br>de concentración 1 hora (μg/m3)|Norma D.S. No 114/2002 (μg/m3)|
|---|---|---|
|2019|50,6|**400**|
|2020|49,5|49,5|
|2021|159,7|159,7|
|**Promedio**|**86,6**|**86,6**|

**Tabla 9.** Percentil 99 de los máximos diarios de concentración de 1 hora de NO 2 registrada en la

estación Quinel. Periodo 2019 - 2021.

|Año|Percentil 99 de los máximos diarios<br>de concentración 1 hora (μg/m3)|Norma D.S. No 114/2002 (μg/m3)|
|---|---|---|
|2019|139,6|**400**|
|2020|65,8|65,8|
|2021|82,4|82,4|
|**Promedio**|**95,9**|**95,9**|

**D.4.6.** **Resultados NO** **2** **Concentración Anual**

En **Tabla 10** y **Tabla 11** se presentan las concentraciones anuales de NO 2 registrados en las estaciones

SAPU y Quinel durante el periodo 2019-2021.

Se aprecia que en estación SAPU y Quinel no hay superación de norma, y los estadísticos están muy por

debajo del límite normativo.

**Tabla 10** . Concentración anual NO 2 registrada en la estación SAPU. Periodo 2019 - 2021.

|Año|Concentración Anual (μg/m3)|Norma D.S. No 114/2002 (μg/m3)|
|---|---|---|
|2019|11,9|**100**|
|2020|10,7|10,7|
|2021|8,5|8,5|
|**Promedio**|**10,4**|**10,4**|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 19

**Tabla 11** . Concentración anual NO 2 registrada en la estación Quinel. Periodo 2019 - 2021.

|Año|Concentración Anual (μg/m3)|Norma D.S. No 114/2002 (μg/m3)|
|---|---|---|
|2019|17,5|**100**|
|2020|14,7|14,7|
|2021|11,0|11,0|
|**Promedio**|**14,4**|**14,4**|

**D.4.7.** **Resultados SO** **2** **Concentración 1 hora**

En **Tabla 12** se presentan los Percentiles 98,5 de las concentraciones de 1 hora de SO 2 registrados en la

estación SAPU durante el periodo 2019-2021.

Visualizando los estadísticos se aprecia que no hay superación de norma, y además están muy por debajo

del límite normativo.

**Tabla 12** . Percentil 98,5 de las concentraciones de 1 hora de SO 2 registrada en la estación SAPU.

Periodo 2019 - 2021.

|Año|Percentil 98.5 concentración 1<br>hora (μg/m3)|Norma D.S. No 104/2019 (μg/m3)|
|---|---|---|
|2019|13,3|**350**|
|2020|14,7|14,7|
|2021|11,0|11,0|
|**Promedio**|**13,0**|**13,0**|

**D.4.8.** **Resultados SO** **2** **Concentración diaria**

En **Tabla 13** se presentan los Percentiles 99 de las concentraciones de 24 hora de SO2 registrados en la

estación SAPU durante el periodo 2019-2021.

Visualizando los estadísticos se aprecia que no hay superación de norma, y además están muy por debajo

del límite normativo.

**Tabla 13** . Percentil 99 de las concentraciones de 24 horas de SO 2 registrada en la estación SAPU.

Periodo 2019 - 2021.

|Año|Percentil 99 de concentración<br>diaria (μg/m3)|Norma D.S. No 104/2019 (μg/m3)|
|---|---|---|
|2019|13,0|**150**|
|2020|14,2|14,2|
|2021|10,4|10,4|
|**Promedio**|**12,5**|**12,5**|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 20

**D.4.9.** **Resultados SO** **2** **Concentración Anual**

Visualizando en **Tabla 14** los estadísticos que dan cuenta de la concentración anual, se aprecia que no hay

superación de norma, y además están muy por debajo del límite normativo.

**Tabla 14** . Concentración anual SO 2 registrada en la estación SAPU. Periodo 2019 - 2021.

|Año|Concentración Trimestral (μg/m3)|Norma D.S. No 104/2019 (μg/m3)|
|---|---|---|
|2019|5,0|**60**|
|2020|6,2|6,2|
|2021|6,4|6,4|
|**Promedio**|**5,9**|**5,9**|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 21

**E.** **IMPLEMENTACIÓN, APLICACIÓN Y RESULTADOS DEL MODELO METEOROLÓGICO WRF**

**E.1.** **Introducción**

En este Capítulo se presenta la implementación y aplicación del modelo meteorológico WRF v4.3

(Weather Research and Forecasting Model). Este modelo es el recomendado en el documento “Guía para

el uso de modelos de calidad del aire en el SEIA”, como información meteorológica de entrada a los

modelos de dispersión en condiciones de terreno complejo.

WRF es uno de los modelos meteorológicos de pronóstico más avanzados y completos. El modelo ofrece

una amplia gama de aplicaciones meteorológicas a través de escalas de decenas de metros a miles de

kilómetros.

WRF ofrece pronósticos operativos mediante una plataforma flexible y computacionalmente eficiente, al

tiempo que proporciona los últimos avances en la física numérica y de asimilación de datos aportados por

los desarrolladores a través de una amplia comunidad de investigación.

El modelo obtiene sus condiciones de borde de datos históricos globales del clima que son mantenidos

por centros operacionales de pronóstico del tiempo. Estos datos globales representan el estado completo

de la atmósfera en todo el planeta y son resultado de análisis informáticos sofisticados de datos

superficiales disponibles y de observaciones a niveles más altos. Cada período de análisis combina decenas

de miles de mediciones individuales tomadas en todo el globo terrestre.

Para poder incorporar la gama completa de fenómenos meteorológicos que ocurren en la atmósfera real

el modelo utiliza una configuración de grillas anidadas. El alcance de la grilla más gruesa es seleccionado

para capturar el efecto de los fenómenos de la escala sinóptica dentro de la región de interés, mientras

que la grilla más fina permite que el modelo desarrolle circulaciones regionales relacionadas con la

interacción de la atmósfera con la topografía.

En **Figura 10** se presenta un diagrama de operación del modelo WRF. Como se observa en esta figura, este

sistema considera como información de entrada meteorología del sistema GFS y/o datos de estaciones

meteorológicas locales, además de topografía y uso de suelos. Con los archivos de salida del modelo se

puede obtener un archivo formato tipo CALMET, el cual sirve de entrada para el modelo CALPUFF.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 22

**Figura 10.** Diagrama de operación del modelo meteorológico WRF.

**E.2.** **Implementación del modelo meteorológico WRF**

En esta sección se presenta la implementación y aplicación del modelo meteorológico WRF para la

generación de la meteorología requerida por el modelo CALPUFF para el año 2021.

El modelo se implementó con dos grillas anidadas cercano a la ciudad de Cabrero, para incorporar todas

las obras del Proyecto. Las condiciones de borde e iniciales de los datos históricos del año 2021 fueron

proporcionadas por GDAS de NOAA (National Oceanic and Atmospheric Administration), de USA, con una

resolución espacial de 0,25 grados.

Respecto a la topografía del dominio de modelación fue obtenida a partir del proyecto SRTM (del

acrónimo inglés Shuttle Radar Topography Mission) con resolución de 3 segundos de grado (90 m

aproximadamente) y el uso de suelo a partir de la información satelital MODIS (del acrónimo inglés

Moderate-Resolution Imaging Spectroradiometer) de la NASA con resolución de 15 segundos de grado.

El dominio de modelación utilizado en el área de estudio consideró la grilla N° 2 de WRF, por ser la que

posee una resolución con tamaño de grilla de 1 km x 1 km para definir la topografía y uso de suelo. Tiene

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 23

dimensiones de 106 kilómetros en la dirección Este-Oeste y 106 kilómetros en la dirección Norte-Sur,

alrededor de su centro ubicado en los 36,934 latitud Sur y 72,292 longitud Oeste.

Las características generales de esta grilla se presentan en **Tabla 15** y los dominios modelados se muestran

en **Figura 11** .

**Tabla 15.** Características del dominio de modelación de la segunda grilla utilizada por el modelo WRF

en la zona de Estudio.

|Características Grilla 2 de WRF|Col2|
|---|---|
|Resolución|1 x 1 km|
|No de celdas en dirección X|106|
|No de celdas en dirección Y|106|
|Coordenadas del origen del dominio|Lat: -36,934; Lon: -72,292|
|Total del área del dominio|11.236 (km2)|

**Figura 11.** Dominios de modelación de WRF en la zona de Estudio con centro cercano a Cabrero.

Respecto a la configuración del modelo, en relación con la física y dinámica, se consideraron las

parametrizaciones del trabajo descritas en el documento Guía para el uso de modelos de calidad del aire

en el SEIA, 2012, cuyos principales esquemas son mostrados en la **Tabla 16** .

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 24

**Tabla 16.** Configuración de las principales parametrizaciones utilizadas en la modelación con WRF para

la zona de Estudio.

|Variable|Nombre|Esquema|Descripción|
|---|---|---|---|
|Microfísica|mp_physics|WSM5|WSM (3 especies<br>microfísicas)|
|Radiación de onda larga|ra_lw_physics|RRTM|Modelo de<br>transferencia radiativa<br>rápida que utiliza<br>tablas de eficiencia.<br>Cuenta con múltiples<br>bandas|
|Radiación de onda corta|ra_sw_physics|Dudhia scheme|Integración simple que<br>permite la absorción y<br>dispersión por nubes y<br>a cielo despejado|
|Capa superficial|sf_sfclay_physics|MM5|Monin-Obukhov<br>similaridad|
|Superficie|sf_Surface_physcis|Thermal Diffusion<br>Scheme|Esquema de difusión<br>termal|
|Capa límite planetaria|bl_pbl_physics|YSU scheme|QNSE|

**E.3.** **Resultados del modelo WRF en la zona de Estudio**

En la presente sección se muestran los resultados del modelo meteorológico WRF. Estos provienen de las

variables extraídas de las coordenadas de la estación monitora de la red meteorológica presentada en la

**Tabla 1** de sección Clima y Meteorología.

**E.3.1.** **Series de Tiempo de Variables Meteorológicas Modeladas con WRF año 2021**

Las series de tiempo de las variables meteorológicas modeladas con WRF para el año 2021 se muestran

en **Figura 12** para estación Purén.

La velocidad de viento muestra mayores magnitudes en los meses de verano que en invierno y con algunos

episodios de máximos en invierno. Respecto a la dirección de viento la componente dominante

corresponde a Suroeste a lo largo del año.

Respecto a la humedad relativa, se visualiza magnitudes de 50% como mínimos en los meses de verano,

mientras que en invierno la humedad permanece con una mayor magnitud.

Finalmente comentando la temperatura modelada, se visualiza un aumento de la magnitud en los meses

de verano cercanos a 30°C como máximo y una disminución en los meses de invierno, con mínimos

cercanos a 0 °C incluso bajo cero.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 25

**Figura 12.** Series de tiempo de variables meteorológicas modeladas en estación Purén durante el año

2021.

**E.3.2.** **Ciclos Diarios de Variables Meteorológicas Modeladas con WRF para el Año 2021**

Los ciclos diarios son construidos en base a los registros promedios de cada hora de todo el año, con el fin

de mostrar un comportamiento patrón de una cierta variable, en este caso meteorológica. El área

sombreada corresponde al área delimitada por los percentiles 5 y 95, el cual tiene como objetivo

caracterizar la variabilidad de la velocidad del viento, humedad relativa y temperatura.

Un poco distinto es lo que se visualiza en el ciclo de dirección de viento, el cual muestra la frecuencia en

términos de porcentaje, de las direcciones de viento registradas, cada 22,5° a lo largo de todas las horas,

desde 0:00 hasta 23:00, de todo el año.

En la **Figura 13** se muestran los ciclos diarios de las variables meteorológicas modeladas en estación Purén.

Respecto a la velocidad de viento se visualiza un aumento de la magnitud en el día, alcanzando su

magnitud mayor antes de las 18:00 horas y una menor un poco después de las 06:00 horas.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 26

La dirección de viento presenta viento dominante Suroeste siendo más significativo en el día con casi un

40% de la frecuencia.

El ciclo de la humedad relativa muestra una disminución de la magnitud durante el día, aproximadamente

a las 15:00 horas, mientras que en la noche permanece con magnitud bastante alta, visualizado en la

convergencia de la curva promedio y el área sombreada.

Finalmente, respecto a la temperatura el mínimo se visualiza a eso de las 06:00 de la mañana con casi

10°C en la curva promedio, mientras que en el día con un promedio de 20°C a eso de las 15:00 horas.

**Figura 13.** Ciclos diarios de variables meteorológicas modeladas en estación Purén durante el año 2021.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 27

**E.3.3.** **Ciclos Estacionales de Variables Meteorológicas modeladas con WRF durante el Año 2021**

Los ciclos estacionales corresponden a gráficos donde se muestra el ciclo diario en el eje x y el ciclo anual

en el eje y. La escala de color muestra la magnitud de la variable, donde el color rojo muestra valores

máximos y los colores azules los mínimos. En particular, en el ciclo estacional de velocidad de viento se

superponen vectores de viento en la imagen, con la finalidad de mostrar la dirección de viento

predominante promedio a lo largo del día y del año.

La **Figura 14** muestra los ciclos estacionales de las variables meteorológicas modeladas en la estación

Purén.

Respecto a la velocidad de viento, se visualiza máximos de velocidad en los periodos diurnos y estivales,

y ocurriendo lo inverso en los periodos nocturnos e invernales.

Respecto a la dirección de viento, en estación Purén se visualizan vientos Suroeste en los meses de verano,

mientras que en invierno se adiciona la dirección Norte. No se aprecia cambio de patrón de viento entre

día y noche.

Respecto a la humedad relativa se visualiza una mayor magnitud en los meses de invierno y noche,

mientras que en verano y en el día está es menor.

Respecto a la temperatura, se visualizan máximos en el día y verano, y mínimos en invierno y noche.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 28

**Figura 14.** Ciclos estacionales de variables meteorológicas modeladas en estación Purén durante año

2021.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 29

**E.3.4.** **Rosas de Viento Modeladas con WRF durante el Año 2021**

La variabilidad de la velocidad y dirección del viento es caracterizada mediante las rosas de viento

solicitadas por el documento oficial, “Guía para el uso de Modelos de Calidad del Aire en el SEIA”.

Adicionalmente las rosas de viento sirven para complementar el análisis de los ciclos diarios y estacionales

mostrados con anterioridad.

En la **Figura 15** se presentan cuatro rangos de tiempo horarios para estación Purén, los cuales son

descritos a continuación:

 - Periodo noche o madrugada, 01:00 a 06:00 horas: predomina viento Suroeste y vientos de 3 m/s

con 16% de frecuencia.

 - Periodo mañana, 07:00 a 14:00 horas: sigue predominando viento Suroeste con vientos de mayor

magnitud, 4 m/s.

 - Periodo tarde, 15:00 a 23:00 horas: el viento dominante corresponde a Suroeste, aunque

aumentando la variabilidad hacia el Oeste y vientos de 4 m/s como máximo.

 - Periodo completo, 00:00 a 23:00 horas: para día completo en promedio para todo el año,

prevalece el viento Suroeste con casi un 12% de frecuencia y con vientos de 4 m/s como máximo.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 30

**Figura 15.** Rosas de viento de datos modelados en estación Purén durante el año 2021.

**E.4.** **Análisis de incertidumbre de los resultados del modelo WRF respecto a los datos observados en**

**estaciones dentro del dominio de la zona de Estudio para el año 2021.**

En esta sección se analiza el nivel de incertidumbre del modelo meteorológico WRF, de forma cualitativa

mediante la comparación de gráficos, series diarias, ciclos diarios y estacionales, y de forma cuantitativa

mediante estadísticos matemáticos obtenidos por comparación entre los datos horarios de las

observaciones y los resultados simulados con WRF.

Los estadísticos matemáticos calculados son los siguientes:

 - Error cuadrático medio (RMSE): entrega el grado de precisión entre los datos pronosticados y

observados.

 - Sesgo normalizado (BIASN): entrega el sesgo entre las series modeladas y observadas.

 - Coeficiente de correlación (R): entrega el grado de relación lineal entre los datos observados y

modelados.

Las fórmulas y rango de estos estadísticos se presentan en **Tabla 17** .

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 31

**Tabla 17.** Estadísticos matemáticos de literatura.

|Estación|Latitud (°)|Longitud (°)|
|---|---|---|
|RMSE|√∑(Mi−Oi)2<br>n<br>n<br>i=1<br>|(0, ∞)|
|BIASN|∑<br>Mi−Oi<br>n<br>i=1<br>∑<br>Oi<br>n<br>i=1<br>|(-∞,∞)|
|R|∑<br>(Mi−M) −(Oi−O)<br>n<br>i=1<br>{∑<br>(Mi−M)<br>2<br>n<br>i=1<br>∑<br>(Oi−O)2}<br>n<br>i=1<br>1/2|[-1,1]|

_Fuente: elaboración propia en base a Wilks, 2011._

**E.4.1.** **Análisis cualitativo series de tiempo observados y modelados con WRF, año 2021**

En **Figura 16** se presentan la comparación de las series de tiempo de variables meteorológicas observados

a la izquierda y modelados con WRF a la derecha, durante el año 2021 en estación Purén.

Observando las series de tiempo se aprecia que el modelo sobrestimó la frecuencia de máximos en los

meses de invierno respecto a las observaciones.

Respecto a la dirección de viento se visualiza similitud en el patrón de viento Suroeste a lo largo del año

expresado en la línea de puntos con mayor sombra levemente sobre los 200°.

Respecto a la humedad relativa se visualiza que el modelo sobreestimó las magnitudes a lo largo del año.

Revisando las temperaturas se visualiza una subestimación de los máximos y una sobrestimación de los

mínimos. Las máximas temperaturas observadas llegan sobre los 35 °C en el mes de enero, mientras que

el modelo solo alcanza 30 °C. Respecto a las mínimas temperaturas, las observaciones registran

temperaturas bajo 0 °C, mientras que el modelo llega a aproximadamente cero. Todo esto también

muestra que la amplitud térmica es subestimada de igual forma.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 32

**Figura 16.** Comparación series de tiempo de variables meteorológicas observadas y modeladas con WRF

en estación Purén durante el año 2021.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 33

**E.4.2.** **Análisis cualitativo ciclos diarios de datos observados y modelados con WRF, año 2021**

En **Figura 17** se presentan la comparación de los ciclos diarios de las variables meteorológicas observados

a la izquierda y modelados con WRF a la derecha, durante el año 2021 en estación Purén.

Respecto a la velocidad de viento los ciclos diarios del modelo muestran una sobrestimación de la

magnitud en términos del promedio.

Respecto a la dirección de viento el modelo logra reproducir la componente Suroeste observada, sin

embargo, se visualiza una sobrestimación de la dirección Suroeste en la noche en casi un 20%, mientras

que en el día subestima en un 20% aproximadamente.

Respecto al ciclo de la humedad relativa, el modelo reproduce el ciclo, sin embargo, sobrestima el máximo

y subestima los mínimos, al igual que la amplitud.

Finalmente, comentando la temperatura, se aprecia que el modelo reproduce el ciclo diario, sin embargo,

subestima las magnitudes máximas y sobrestima los mínimos al igual que la amplitud.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 34

**Figura 17.** Comparación de ciclos diarios de variables meteorológicas observados y modelados con WRF

en estación Purén durante el año 2021.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 35

**E.4.3** **Análisis cualitativo de ciclos estacionales de datos observados y modelados con WRF año**

**2021**

En **Figura 18** se presenta la comparación de los ciclos estacionales de variables meteorológicas observados

(Obs) a la izquierda y modelados (Mod) con WRF a la derecha, durante el año 2021 en estación Purén.

Analizando la velocidad de viento el modelo sobrestima la magnitud. Este reproduce las variaciones de

velocidad, tanto en la transición vespertina y luego en los cambios estacionales observados, julio y

octubre.

Respecto a la dirección de viento el modelo reprodujo los vientos observados Suroeste del día y en los

meses de verano, al igual que la variabilidad de vientos en el invierno, esto es vientos intercalados

Suroeste y Noreste.

Describiendo la humedad relativa, el modelo captura la estacionalidad y el ciclo diario, sin embargo,

sobrestima la magnitud.

Finalmente, respecto a la temperatura el modelo logra reproducir los ciclos, el modelo reproduce la mayor

magnitud en los meses de veranos y horas del día, y menores temperaturas en invierno y periodo

nocturno. La reproducción de la variable por parte del modelo tiene una divergencia la cual es la

subestimación de máximos y sobrestimación de mínimo ( **Figura 18** ).

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 36

**Figura 18.** Comparación de ciclos estacionales de variables meteorológicas observados y modelados con

WRF en estación Purén durante el año 2021.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 37

**E.4.4** **Análisis cualitativo de rosas de viento de datos observados y modelados con WRF, año**

**2021**

Las imágenes de rosas de viento, cuya comparación entre observaciones y modelado con WRF del año

2021 se presenta en **Figura 19** para estación Purén.

A continuación, se describe en detalle los cuatro periodos mostrados por las rosas de viento construidas:

 - Periodo 01:00 a 06:00 horas: el modelo subestima levemente el viento Suroeste, la velocidad es

levemente sobrestimada.

 - Periodo 07:00 a 14:00 horas: el modelo reproduce la dirección Suroeste, y sobrestima la

velocidad.

 - Periodo 15:00 a 23:00 horas: el modelo sobrestima levemente la dirección Oeste y la magnitud.

 - Periodo 00:00 a 23:00 horas: el modelo reproduce las componentes dominantes de las

observaciones, solo sobrestimando la magnitud.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 38

**Figura 19.** Comparación de Rosas de Viento con datos observados y modelados con WRF en estación

Purén durante el año 2021

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 39

**E.5.** **Análisis cuantitativo**

El análisis cuantitativo es realizado mediante la utilización de los estadísticos descritos al inicio de la

**sección E.4** . Estos son resultados de la comparación entre las series de datos observados y modelados con

WRF, extraídos para estación Purén, los cuales se presentan en la **Tabla 18**, donde se consolida toda la

información. Estos estadísticos dan cuenta del desempeño del modelo en los puntos geográficos

analizados.

Considerando la tabla descrita se puede indicar lo siguiente:

 - Respecto al BIASN, se tiene lo siguiente:

`o` Velocidad de viento: el modelo sobrestima levemente la magnitud de las observaciones.

`o` Humedad relativa: el modelo sobrestima levemente la magnitud de las observaciones.

`o` Temperatura: el modelo subestima las observaciones.

 - Respecto al RMSE, se tiene lo siguiente:

`o` Velocidad de viento: el modelo en promedio tuvo una precisión de 1,05 m/s.

`o` Humedad relativa: la imprecisión del modelo fue de 17,94%

`o` Temperatura: la precisión del modelo fue de 3,15°C.

 - Respecto al estadístico de correlación R, se puede inferir lo siguiente:

`o` Velocidad de viento: el modelo tuvo un grado de correlación aceptable.

`o` Humedad relativa: la relación de datos entre observaciones y modelo es lo

suficientemente alta.

`o` Temperatura: entre las variables estudiadas es la que tiene la mejor relación con las

observaciones, la más cercana a 1.

**Tabla 18.** Resultados estadísticos obtenidos de la comparación de datos observados y modelados con

WRF en las estaciones del dominio de la zona de Estudio

|Estadística|Variable|Unidad|Estación Purén|
|---|---|---|---|
|RMSE|VV|m/s|1,05|
|RMSE|HR|%|17,94|
|RMSE|T|°C|3,15|
|BIASN|VV|m/s|0,24|
|BIASN|HR|%|0,19|
|BIASN|T|°C|-0,11|
|R|VV|m/s|0,72|
|R|HR|%|0,86|
|R|T|°C|0,95|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 40

**F.** **INVENTARIO DE EMISIONES DEL PROYECTO**

**F.1.** **Introducción**

En este Capítulo se presenta el Inventario de emisiones de MP10, MP2,5, MPS, NOx, SOx, CO y HC, debido

a las actividades del Proyecto “Parque Eólico Dañicalqui”. Las actividades emisoras de contaminantes

atmosféricos del Proyecto identificadas se indican en **Tabla 19** .

**Tabla 19.** Actividades del Proyecto generadoras de emisiones atmosféricas.

|Actividad|Contaminante|
|---|---|
|**Fase Construcción y Cierre**|**Fase Construcción y Cierre**|
|Excavación|MP10, MP2,5 y MPS|
|Carga y Descarga de material|MP10, MP2,5 y MPS|
|Compactación|MP10, MP2,5 y MPS|
|Escarpe|MP10, MP2,5 y MPS|
|Maquinaria fuera de ruta|MP10, MP2,5, MPS, NOx, CO, SOx y HC|
|Resuspensión por tránsito por caminos pavimentados|MP10, MP2,5 y MPS|
|Resuspensión por tránsito por caminos no pavimentados|MP10, MP2,5 y MPS|
|Operación de vehículos|MP10, MP2,5, MPS, NOx, CO, SOx y HC|
|Erosión Eólica por acopio de material|MP10, MP2,5 y MPS|
|Grupos electrógenos|MP10, MP2,5, MPS, NOx, CO, SOx y HC|
|**Fase Operación**|**Fase Operación**|
|Resuspensión por tránsito por caminos pavimentados|MP10, MP2,5 y MPS|
|Resuspensión por tránsito por caminos no pavimentados|MP10, MP2,5 y MPS|
|Operación de vehículos|MP10, MP2,5, MPS, NOx, CO, SOx y HC|
|Grupos electrógenos*|MP10, MP2,5, MPS, NOx, CO, SOx y HC|

_*: Las emisiones de grupos electrógenos en la fase de operación es despreciable, por ser únicamente utilizadas en caso de_

_emergencia._

Es importante destacar que, las actividades de la fase de cierre son homólogas a la de construcción.

**F.2.** **Metodología de Cálculo de Emisiones Atmosféricas**

La metodología general para la estimación de emisiones de contaminantes atmosféricos, para cualquier

tipo de actividad o fuente identificada, corresponde a la aplicación de Factores de Emisión. La **Ecuación 1**

siguiente, presenta los diferentes enfoques que deben tenerse en cuenta en el cálculo de las emisiones.

Este factor de emisión se obtuvo del informe “Servicio de Recopilación y Sistematización de Factores de

Emisión al Aire para el Servicio de Evaluación Ambiental (SEA)”, mayo 2015.

Em = FE ∗ NA
ij ij j ∗[1 −

EC ij **Ecuación 1**

100 ~~[]]~~

Donde:

Em ij : Emisión de contaminante i debido al proceso j (kg/día, t/año).

FE ij : Factor de Emisión de la actividad o proceso j para el contaminante i (masa de contaminante

liberada por unidad de masa procesada; kg/t).

NA j : Nivel de Actividad del proceso j (kg/día, t/año).

EC ij : Eficiencia de Control de Emisiones del contaminante i para el proceso j (%).

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 41

Un Factor de Emisión es un valor representativo que intenta relacionar la cantidad de un contaminante

emitido a la atmósfera con una actividad asociada con la liberación de ese contaminante.

Los factores de emisión se han desarrollado y compilado a partir de la información de pruebas en fuentes,

estudios de balance de masa y estimaciones de ingeniería.

Los niveles de actividad son estimados de acuerdo a la información proporcionada por el titular del

Proyecto para cada fase. Depende del factor de emisión específico que se utiliza y la información que lo

alimenta está en función del Proyecto, sus fases y actividades, específicamente están dados por la

intensidad o duración de cada actividad dentro del Proyecto.

En la sección siguiente se presentan los factores de emisión considerados en la estimación de las

emisiones de fuentes asociadas a procesos relacionados con actividades de la fase de Construcción del

Proyecto.

**F.3.** **Factores de Emisión de Contaminantes Atmosféricos**

La información sobre factores de emisión fue obtenida principalmente de “Servicio de Recopilación y

Sistematización de Factores de Emisión al Aire para el Servicio de Evaluación Ambiental (SEA)”, mayo

2015. También se obtuvo información complementaria desde la “Guía para la estimación de emisiones

atmosféricas de proyectos Inmobiliarios para la Región Metropolitana” del Seremi de Medio Ambiente

RM (Actualización), octubre 2020.

A continuación, se describen los factores de emisiones de Material Particulado (MP10, MP2,5 y MPS) y

gases (NOx, CO, SOx y HC), producidas en las distintas actividades del proyecto. Además, se detalla el nivel

de actividad requerido para calcular las emisiones de estos contaminantes según cada factor:

- **Excavaciones o preparación de terreno:** Corresponde al factor de emisión de despeje de material

(bulldozing / overburden)

FE MPS y MP2,5 = k∗2,6 ∗

s [1,2]

**Ecuación 2**
M [1,3] [ (kg/h)]

FE MP10 = k∗0,45 ∗

s [1,5]

**Ecuación 3**
M [1,4] [ (kg/h)]

Donde:

FE: Factor de Emisión de MP en kilógramos emitidos por hora excavada, (kg/h).

s: Contenido de finos, % (bajo malla 200, 75 μm).

M: Humedad del material, %.

k: Factor aerodinámico, adimensional. 0,75 para MP10, 0,105 para MP2,5 y 1 para MPS.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 42

Este factor de emisión se obtuvo del informe “Servicio de Recopilación y Sistematización de Factores de

Emisión al Aire para el Servicio de Evaluación Ambiental (SEA)”, mayo 2015.

El nivel de actividad necesario para calcular estas emisiones es la cantidad de horas de funcionamiento de

la maquinaria.

- **Carga en camiones y descarga de material:** Corresponde al factor de emisión de carga de material en

camiones y de transferencia discreta de material utilizado directamente.

1,3

FE MP = k∗0,0016 ∗

[U]
( 2,

~~(~~ [M] 2

[U]

2,2 ~~[)]~~

2 [)]

1,4 [(kg/ton)] **Ecuación 4**

Donde:

FE: Factor de Emisión de MP en kilógramos emitidos por toneladas cargadas o descargadas de

material, (kg/t).

M: Humedad del material, %.

U: Velocidad del viento, (m/s).

k: Factor aerodinámico, adimensional. 0,35 para MP10, 0,053 para MP2,5 y 0,74 para MPS.

Este factor se obtuvo del informe “Servicio de Recopilación y Sistematización de Factores de Emisión al

Aire para el Servicio de Evaluación Ambiental (SEA)”, mayo 2015.

El nivel de actividad que se requiere para la estimación de estas emisiones es la cantidad de material

transferido en las distintas operaciones de carga y descarga de los camiones que transportan el material

extraído.

- **Compactación:** Corresponde al factor de emisión por compactación del terreno.

FE MPS y MP2,5 = k∗2,6 ∗

s [1,2]

**Ecuación 5**
M [1,3] [ (kg/h)]

FE MP10 = k∗0,45 ∗

s [1,5]

**Ecuación 6**
M [1,4] [ (kg/h)]

Donde:

FE: Factor de Emisión de MP en kilógramos emitidos por hora excavada, (kg/h).

s: Contenido de finos, % (bajo malla 200, 75 μm).

M: Humedad del material, %.

k: Factor aerodinámico, adimensional. 0,75 para MP10, 0,105 para MP2,5 y 1 para MPS.

Este factor se obtuvo del informe “Servicio de Recopilación y Sistematización de Factores de Emisión al

Aire para el Servicio de Evaluación Ambiental (SEA)”, mayo 2015.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 43

El nivel de actividad necesario para calcular estas emisiones es la cantidad de horas de funcionamiento de

la maquinaria compactadora.

- **Escarpes:** Corresponde al factor de emisión de preparación de terrenos (movimiento de tierra) y retiro

de cobertura vegetal.

FE **Ecuación 7**
MP10 y MPS = 5,7 ( km [k][g] ~~[)]~~

FE **Ecuación 8**
MP2,5 = 0,855 ( km [k][g] ~~[)]~~

Donde:

FE: Factor de Emisión de MP10 en kilogramos emitidos por kilómetro recorrido en el proceso de

escarpado de la cobertura vegetal, (kg/km).

Este factor se obtuvo del informe “Servicio de Recopilación y Sistematización de Factores de Emisión al

Aire para el Servicio de Evaluación Ambiental (SEA)”, mayo 2015.

El nivel de actividad se determina según la distancia que recorre el cargador frontal por el área a escarpar

(por defecto para 1 hectárea se recorre una distancia de 3,57 km [1] ).

- **Tránsito de vehículos en caminos no pavimentados:** Corresponde al factor de emisión debido a polvo

resuspendido por tránsito de vehículos livianos y pesados por caminos no pavimentados.

∗( 2,72 [W] ~~[)]~~

FE [s]
MPS,MP10 y MP2,5 = k ∗0,2819 ∗(

[s]

12 [)]

0,9

0,45

(kg/km) **Ecuación 9**

Donde:

FE: Factor de Emisión de MP en kilógramos emitidos por kilómetro recorrido por vehículo, (kg/km).

s: Contenido de finos de suelo, % (bajo malla 200, 75 μm).

W: Peso promedio de la flota, t.

k: Factor aerodinámico, adimensional. 1,5 para MP10, 0,15 para MP2,5 y 4,9 para MPS.

Este factor se obtuvo del informe “Guía para la estimación de emisiones atmosféricas en la Región

Metropolitana”, octubre 2020.

Para considerar el efecto de las lluvias, se puede aplicar un factor obtenido mediante la siguiente

ecuación.

FCP (Factor de corrección por lluvia camino no pavimentado) = 1 −

P

**[Ecuación 10]**
365

Donde:

P: Número de días en el año con precipitaciones superiores a 0,254 [mm].

1 Publicado en “Guía para la Estimación de Emisiones Atmosféricas en la Región Metropolitana” de la SEREMI de Medio Ambiente
de la RM, octubre 2020.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 44

Este factor se obtuvo del informe “Servicio de Recopilación y Sistematización de Factores de Emisión al

Aire para el Servicio de Evaluación Ambiental (SEA)”, mayo 2015.

El valor de P fue obtenido de la estación más cercana al proyecto con precipitaciones válidas, la estación

Yungay perteneciente a la red del INIA (Instituto de Investigaciones Agropecuarias) para el año 2021. Este

valor correspondió a 68 días, con lo que se obtuvo un valor de FCP= 0,8137.

El peso promedio de los camiones corresponde al peso promedio ponderado por el porcentaje de viajes

de cada categoría de peso (promedio cargado y sin carga). Los pesos promedios utilizados se indican en

**Tabla 20.**

Los niveles de actividad corresponden a los flujos vehiculares en caminos no pavimentados. Este flujo

corresponde al total de los kilómetros recorridos por todos los vehículos.

|bla 20. Peso promedio vehículos del proyecto.|Col2|Col3|
|---|---|---|
|**Peso y capacidad de carga de cada uno de los vehículos**|**Valor**|**Unidad**|
|**Camión rígido + 2 ejes **|**Camión rígido + 2 ejes **|**Camión rígido + 2 ejes **|
|Peso vacío|9,3|t|
|Peso con carga|31,5|t|
|Peso Promedio|20,4|t|
|**Camión Semiremolque**|**Camión Semiremolque**|**Camión Semiremolque**|
|Peso vacío|16|t|
|Peso con carga|40|t|
|Peso Promedio|28|t|
|**Liviano**|**Liviano**|**Liviano**|
|Peso vacío|2|t|
|Peso con carga|3|t|
|Peso Promedio|2,5|t|
|**Sobredimensionado**|**Sobredimensionado**|**Sobredimensionado**|
|Peso vacío|16|t|
|Peso con carga|60|t|
|Peso Promedio|38|t|
|**Aljibe**|**Aljibe**|**Aljibe**|
|Peso vacío|17|t|
|Peso con carga|27|t|
|Peso Promedio|22|t|
|**Camión 3/4**|**Camión 3/4**|**Camión 3/4**|
|Peso vacío|2,07|t|
|Peso con carga|5,7|t|
|Peso Promedio|3,885|t|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 45

- **Tránsito de vehículos en caminos pavimentados:** Corresponde al factor de emisión debido a polvo

resuspendido por tránsito de vehículos por caminos pavimentados.

FE MP = k ∗sL [0,91] ∗(W ∗1,1023) [1,02] (g/km) **Ecuación 11**

Donde:

FE: Factor de Emisión de MP en gramos emitidos por kilómetro recorrido por vehículo, (g/km).

sL: Carga superficial de finos (g/m [2] ).

W: Peso promedio de la flota, t.

k: Factor aerodinámico, adimensional. 0,62 para MP10, 0,15 para MP2,5 y 3,23 para MPS.

Para considerar el efecto de las lluvias, se puede aplicar un factor obtenido mediante la siguiente

ecuación.

FCP (Factor de corrección por lluvia camino pavimentado) = 1 −

P

**[Ecuación 12]**
4∗365

Donde:

P: Número de días en el año con precipitaciones superiores a 0,254 [mm].

Este factor se obtuvo del informe “Servicio de Recopilación y Sistematización de Factores de Emisión al

Aire para el Servicio de Evaluación Ambiental (SEA)”, mayo 2015.

El valor de P fue obtenido de la estación más cercana al proyecto con precipitaciones válidas, la estación

Yungay perteneciente a la red del INIA (Instituto de Investigaciones Agropecuarias) para el año 2021. Este

valor correspondió a 68 días, con lo que se obtuvo un valor de FCP= 0,953.

El peso promedio de los camiones corresponde al peso promedio ponderado por el porcentaje de viajes

de cada categoría de peso (promedio cargado y sin carga). Los pesos promedios utilizados se indican en

**Tabla 20.**

Los niveles de actividad corresponden a los flujos vehiculares en caminos pavimentados. Este flujo

corresponde al total de los kilómetros recorridos por todos los vehículos.

- **Combustión de vehículos:** Esta fuente considera las emisiones de MP y gases producto de la

combustión realizada al interior de los vehículos.

Los factores de emisión por contaminante según tipo de vehículo, en gramos por kilómetros de

vehículos recorrido, se presentan en **Tabla 21** .

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 46

**Tabla 21.** Factores de emisión por contaminante según tipo de vehículo, en gramos por kilómetros de

vehículos recorrido.

|Contaminante|Tipo de vehículo|FE (g/veh-km)|
|---|---|---|
|**MP**|Livianos|0,67*(4,5*10^-5*V^2-4,885*10^-3*V+0,1932)|
|**MP**|Pesados|((0,5224+(4,4906*10^-3*V))+(((-1,6281*10^-2-4,4906*10^-3)*(1-<br>EXP(((-1)* 2,4923*10^-2*V)))/2,4923*10^-2)))|
|**SOx**|Livianos|2*(0,0198*V^2-2,506*V+137,42)* Scomb/1000000|
|**SOx**|Pesados|2*((195,476155665251+(464,243926657849*EXP(((-<br>1)*0,0471738612383144)*V)))+(22777,7239789702*EXP(((-<br>1)*0,88418501143649)*V)))* Scomb/1000000|
|**NOx**|Livianos|0,84*(2,41*10^-4*V^2-3,181*10^-2*V+2,0247)|
|**NOx**|Pesados|((7,20536564798271+(16,4001356804762*EXP(((-<br>1)*0,0478197060782861)*V)))+(55,7002667265637*EXP(((-<br>1)*0,444673457893458)*V)))|
|**CO**|Livianos|0,82*(2,23*10^-4*V^2-2,6*10^-2*V+1,076)|
|**CO**|Pesados|(1/(((-0,00010960585101578<br>*(V2))+(0,0174064839534468*V))+0,0779217214718428))|
|**HC**|Livianos|0,62*(0,0000175*V^2-0,00284*V+0,2162)|
|**HC**|Pesados|((0,162905538155383+(0,828009789857126*exp(((-<br>1)*0,0248119637491787)*V))) +(2,67001448123625*exp(((-<br>1)*0,124882855805357)*V)))|

_V:_ _Velocidad promedio (km/h);_
_Scomb: Contenido de azufre en el diesel en m/m, considera 50 ppm._

El contenido de Azufre del combustible se consideró en 50 ppm y la velocidad promedio de los vehículos

del proyecto considera lo siguiente:

 - Vehículos sobredimensionados: 30 km/h en todo trayecto (caminos pavimentados y no

pavimentados).

 - Otros vehículos (pesados y livianos): 80 km/h en caminos pavimentados y 40 km/h en caminos no

pavimentados.

Este factor se obtuvo de la “Guía para la Estimación de Emisiones Atmosféricas de Proyectos Inmobiliarios

para la Región Metropolitana” 2012. Estos factores son basados en el modelo europeo de emisiones

COPERT IV, e incluyen la variable de la velocidad de los vehículos que son variables en el proyecto como

se menciona anteriormente.

El nivel de actividad requerido para estimar las emisiones de esta fuente corresponde a la distancia que

recorren, según tipo de vehículo.

- **Maquinarias fuera de Ruta:** Esta fuente considera las emisiones de MP y gases producto de la

combustión en maquinaria pesada. Estos factores dependen de la potencia de la maquinaria.

FE = FP ∗C ∗P ∗(1 + FD) ∗FA (g/h) **Ecuación 13**

Donde:

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 47

FE: Factor de Emisión de MP y gases en gramos emitidos por hora de funcionamiento maquinaria,

(g/h).

FP: Factor de emisión de contaminante según Potencia de maquinaria, (g/kW-h).

C: Porcentaje de carga. Para un escenario conservador se considera un valor de 0,8 para todas las

maquinarias.

P: Potencia Nominal, (kW).

FD: Factor de deterioro. Para un escenario conservador se considera maquinaria con 5 años de uso y

vida útil de 10 años.

FA: Factor de ajuste transiente de la maquinaria.

Este factor se obtuvo de la “Guía para la estimación de emisiones atmosféricas de proyectos Inmobiliarios

para la Región Metropolitana” del Seremi de Medio Ambiente RM (Actualización), octubre 2020.

El porcentaje de carga se utilizará 0,8 como el peor escenario de emisiones.

Los factores de emisión de contaminante según Potencia, los factores de deterioro relativo, factor de

ajuste transiente se presentan en **Tabla 22** a **Tabla 24** .

**Tabla 22.** Factores de emisión por contaminante según potencia, tecnología Stage II, en gramos por

kilowatt hora.

|Fuente de Emisión|Contaminante|Factor de Emisión (g/kW-h)|
|---|---|---|
|**Motores potencia entre 8**<br>**y 19 kW**|CO|5,00|
|**Motores potencia entre 8**<br>**y 19 kW**|NOx|11,20|
|**Motores potencia entre 8**<br>**y 19 kW**|MP|1,60|
|**Motores potencia entre 8**<br>**y 19 kW**|SOx|0,0081|
|**Motores potencia entre**<br>**19 y 37 kW**|CO|2,20|
|**Motores potencia entre**<br>**19 y 37 kW**|NOx|6,50|
|**Motores potencia entre**<br>**19 y 37 kW**|MP|0,40|
|**Motores potencia entre**<br>**19 y 37 kW**|SOx|0,0079|
|**Motores potencia entre**<br>**37 y 56 kW**|CO|2,20|
|**Motores potencia entre**<br>**37 y 56 kW**|NOx|5,50|
|**Motores potencia entre**<br>**37 y 56 kW**|MP|0,20|
|**Motores potencia entre**<br>**37 y 56 kW**|SOx|0,0078|
|**Motores potencia entre**<br>**56 y 75 kW**|CO|2,20|
|**Motores potencia entre**<br>**56 y 75 kW**|NOx|5,50|
|**Motores potencia entre**<br>**56 y 75 kW**|MP|0,20|
|**Motores potencia entre**<br>**56 y 75 kW**|SOx|0,0078|
|**Motores potencia entre**<br>**75 y 130 kW**|CO|1,50|
|**Motores potencia entre**<br>**75 y 130 kW**|NOx|5,20|
|**Motores potencia entre**<br>**75 y 130 kW**|MP|0,20|
|**Motores potencia entre**<br>**75 y 130 kW**|SOx|0,0077|
|**Motores potencia entre**<br>**130 y 560 kW**|CO|1,50|
|**Motores potencia entre**<br>**130 y 560 kW**|NOx|5,20|
|**Motores potencia entre**<br>**130 y 560 kW**|MP|0,10|
|**Motores potencia entre**<br>**130 y 560 kW**|SOx|0,0075|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 48

**Tabla 23.** Factor de deterioro relativo a la vida útil de maquinaria diésel.

|Tecnología|MP|NOx|CO|SOx|HC|
|---|---|---|---|---|---|
|**Stage II**|0,2365|0,0045|0,0505|-|0,017|

_Como promedio considera conservador maquinaria con la mitad de vida útil._

**Tabla 24.** Factor de ajuste transiente para maquinaria diésel.

|Tecnología|Factor de carga|MP|NOx|CO|SOx|HC|
|---|---|---|---|---|---|---|
|**Stage II**|C > 0,45|1,23|0,95|1,53|-|1,05|

Los niveles de actividad requeridos para calcular las emisiones de MP y gases de estas fuentes son:

potencia de la maquinaria y horas de funcionamiento.

- **Erosión Eólica:** El factor de emisión debido a “erosión eólica” se calcula como la suma de los

potenciales de erosión (P i ) de un metro cuadrado de superficie con N perturbaciones durante un año.

Por lo tanto, la emisión total se obtiene de la multiplicación de este factor por el área erosionada. El

factor de emisión de material particulado (MP) es el siguiente:

FE MP = k ∗10 ∗∑ Ni=1 P i (kg/ha/año) **Ecuación 14**
Con P i = 58 ∗(u i∗ −u t∗ ) 2 + 25 ∗(u i∗ −u t∗ ) y u i∗ = 0,053 ∗u 10+

t∗ ) 2 + 25 ∗(u i

t∗ ) y u i

Con P i = 58 ∗(u i∗ −u t∗ ) 2 + 25 ∗(u i∗ −u t∗ ) y u i∗ = 0,053 ∗u 10+ **Ecuación 15**

Donde:

FE: Factor de Emisión de MP en kilogramos emitidos por hectárea intervenida en un período de

tiempo, (kg/km).

N: Número de Perturbaciones.

P i : Potencial de erosión, g/m [2] .
u i [*] : Velocidad de fricción, m/s.

u 10 [+] : Ráfaga medida en Anemómetro más cercano a 10 metros del suelo, m/s.

u t [*] : Velocidad umbral de fricción, m/s.

k: Multiplicador de tamaño de partícula, adimensional. 0,5 para MP10; 0,075 para MP2,5 y 1 para

MPS.

La velocidad umbral (u t [*] ) o velocidad crítica, es la velocidad mínima con la cual se empieza a producir el

fenómeno de movimiento o transporte de las partículas (erosión).

Por lo tanto, cuando la velocidad de fricción (u*), que es una medida de la tensión de corte del viento
sobre superficies erosionables, supera la velocidad umbral, se produce el fenómeno de erosión (Si u [*] u t [*], entonces la Erosión >0).

i∗ −u t∗

∗
−u t

i∗ = 0,053 ∗u 10+

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 49

Este factor se obtuvo del informe “Servicio de Recopilación y Sistematización de Factores de Emisión al

Aire para el Servicio de Evaluación Ambiental (SEA)”, mayo 2015.

El potencial de erosión se puede obtener con la información de velocidad del viento, especialmente

ráfagas, registrada en las estaciones meteorológicas cercanas.

- **Grupos electrógenos:** Esta fuente considera las emisiones de MP y gases producto de la operación de

grupos electrógenos.

Los factores de emisión se obtuvieron de la “Guía para la Estimación de Emisiones Atmosféricas en la

Región Metropolitana”, del Seremi de Medio Ambiente RM, octubre 2020, y se presentan en **Tabla 25.**

**Tabla 25.** Factor de emisión según potencia de grupo electrógeno.

|Combustible|Unidad|CO|NOx|MP|SOx|HC*|
|---|---|---|---|---|---|---|
|Diesel (hasta 600 hp)|kg/kg combustible|0,0186271|0,08647|0,0060783|0,00568616|0,00706|

*: HC como COV en guía.

**F.4.** **Cálculo de Factores de Emisión de Contaminantes Atmosféricos**

Los resultados de los factores de emisiones de MP10, MP2,5, MPS y Gases (NOx, CO, SOx y HC) se

presentan en **Tabla 26** a **Tabla 29**, respectivamente.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 50

**Tabla 26.** Factores de emisión de MP10 del proyecto Parque Eólico Dañicalqui.

|Actividad|Col2|Parámetros para Factores de Emisión|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Factor Emisión|Col18|Col19|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Actividad**|**Actividad**|**k **|**s **|**U **|**sL**|**W **|**FCP**|**M **|**Σ Pi**|**V **|**P **|**FP**|**C **|**FD**|**FA**|**Fórmula**|**Valor**|**Unidad**|
|**Actividad**|**Actividad**|**k **|**% **|**m/s**|**g/m2 **|**t **|**t **|**% **|**% **|**km/h**|**kW**|**g/kW**|**g/kW**|**g/kW**|**g/kW**|**g/kW**|**g/kW**|**g/kW**|
|Excavaciones - preparación de terreno|Excavaciones - preparación de terreno|0,75|10,5|||||6,5||||||||k*0,45*(s^1,5/M^1,4)|8,36E-01|kg/h|
|Carga|Carga|0,35||5,0||||6,5||||||||k*0,0016*(U/2,2)^1,3/(M/2)^1,4|3,13E-04|kg/t|
|Descarga|Descarga|0,35||5,0||||6,5||||||||k*0,0016*(U/2,2)^1,3/(M/2)^1,4|3,13E-04|kg/t|
|Compactación|Compactación|0,75|10,5|||||6,5||||||||k*0,45*(s^1,5/M^1,4)|8,36E-01|kg/h|
|Escarpe|Escarpe|||||||||||||||5,7|5,70E+00|kg/km|
|Maquinaria fuera de ruta|Motoniveladora||||||||||95|0,2|0,8|0,2365|1,23|P*FP*C*(1+FD)*FA/1000|2,31E-02|kg/h|
|Maquinaria fuera de ruta|Compactadora||||||||||1043|0,045|0,8|0,2365|1,23|1,23|5,71E-02|kg/h|
|Maquinaria fuera de ruta|Bulldozer||||||||||161|0,1|0,8|0,2365|1,23|1,23|1,96E-02|kg/h|
|Maquinaria fuera de ruta|Retroexcavadora||||||||||71|0,2|0,8|0,2365|1,23|1,23|1,73E-02|kg/h|
|Maquinaria fuera de ruta|Grúa de apoyo||||||||||151|0,1|0,8|0,2365|1,23|1,23|1,84E-02|kg/h|
|Maquinaria fuera de ruta|Grúa principal||||||||||455|0,1|0,8|0,2365|1,23|1,23|5,54E-02|kg/h|
|Resuspensión camino No<br>Pavimentado|Camión rígido + 2 ejes|1,5|5|||20,4|0,814|||||||||k*0,2819*(s/12)^0,9*(W/2,72)^0,45*FCP|3,87E-01|kg/VKT|
|Resuspensión camino No<br>Pavimentado|Camión Semiremolque|1,5|5|||28|0,814||||||||||4,47E-01|kg/VKT|
|Resuspensión camino No<br>Pavimentado|Liviano|1,5|5|||2,5|0,814||||||||||1,51E-01|kg/VKT|
|Resuspensión camino No<br>Pavimentado|Sobredimensionado|1,5|5|||38|0,814||||||||||5,13E-01|kg/VKT|
|Resuspensión camino<br>Pavimentado|Camión rígido + 2 ejes|0,62|||0,2|20,4|0,953|||||||||k*(sL)^0,91*(W*1,1023)^1,02/1000*FCP|3,27E-03|kg/VKT|
|Resuspensión camino<br>Pavimentado|Camión Semiremolque|0,62|||0,2|28,0|0,953||||||||||4,52E-03|kg/VKT|
|Resuspensión camino<br>Pavimentado|liviano|0,62|||0,2|2,5|0,953||||||||||3,84E-04|kg/VKT|
|Resuspensión camino<br>Pavimentado|Sobredimensionado|0,62|||0,2|38,0|0,953||||||||||6,17E-03|kg/VKT|
|Combustión vehículos|Camión rígido + 2 ejes|||||||||80||||||((0,5224+(4,4906*10^-3*V))+(((-<br>1,6281*10^-2-4,4906*10^-3)*(1-EXP(((-<br>1)* 2,4923*10^-2*V)))/2,4923*10^-<br>2)))/1000|8,82E-04|kg/VKT|
|Combustión vehículos|Camión Semiremolque|||||||||80|||||||8,82E-04|kg/VKT|
|Combustión vehículos|liviano|||||||||80||||||0,67*(4,5*10^-5*V^2-4,885*10^-<br>3*V+0,1932)/1000|6,06E-05|kg/VKT|
|Combustión vehículos|Sobredimensionado|||||||||30||||||((0,5224+(4,4906*10^-3*V))+(((-<br>1,6281*10^-2-4,4906*10^-3)*(1-EXP(((-<br>1)* 2,4923*10^-2*V)))/2,4923*10^-<br>2)))/1000|6,57E-04|kg/VKT|
|Combustión vehículos|Camión rígido + 2 ejes|||||||||40||||||((0,5224+(4,4906*10^-3*V))+(((-<br>1,6281*10^-2-4,4906*10^-3)*(1-EXP(((-<br>1)* 2,4923*10^-2*V)))/2,4923*10^-<br>2)))/1000|7,02E-04|kg/VKT|
|Combustión vehículos|Camión Semiremolque|||||||||40|||||||7,02E-04|kg/VKT|
|Combustión vehículos|liviano|||||||||40||||||0,67*(4,5*10^-5*V^2-4,885*10^-<br>3*V+0,1932)/1000|4,68E-05|kg/VKT|
|Combustión vehículos|Sobredimensionado|||||||||30||||||((0,5224+(4,4906*10^-3*V))+(((-<br>1,6281*10^-2-4,4906*10^-3)*(1-EXP(((-<br>1)* 2,4923*10^-2*V)))/2,4923*10^-<br>2)))/1000|6,57E-04|kg/VKT|
|Erosión Eólica|Erosión Eólica|0,5|||||||1,53|||||||k * (Σ Pi) * 10<br>Pi = 58x(u*-ut*)^2+25x(u*-ut*)|7,63|kg/ha/año|
|Grupos electrógenos|Grupos electrógenos||||||||||88|||||6,08E-03|6,08E-03|kg/kg comb.|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 51

**Tabla 27.** Factores de emisión de MP2,5 del proyecto Parque Eólico Dañicalqui.

|Actividad|Col2|Parámetros para Factores de Emisión|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Factor Emisión|Col18|Col19|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Actividad**|**Actividad**|**k **|**s **|**U **|**sL**|**W **|**FCP**|**M **|**Σ Pi**|**V **|**P **|**FP**|**C **|**FD**|**FA**|**Fórmula**|**Valor**|**Unidad**|
|**Actividad**|**Actividad**|**k **|**% **|**m/s**|**g/m2 **|**t **|**t **|**% **|**% **|**km/h**|**kW**|**g/kW**|**g/kW**|**g/kW**|**g/kW**|**g/kW**|**g/kW**|**g/kW**|
|Excavaciones - preparación de terreno|Excavaciones - preparación de terreno|0,105|10,5|||||6,5||||||||k*2,6*(s^1,2/M^1,3)|4,03E-01|kg/h|
|Carga|Carga|0,053||5,0||||6,5||||||||k*0,0016*(U/2,2)^1,3/(M/2)^1,4|4,73E-05|kg/t|
|Descarga|Descarga|0,053||5,0||||6,5||||||||k*0,0016*(U/2,2)^1,3/(M/2)^1,4|4,73E-05|kg/t|
|Compactación|Compactación|0,105|10,5|||||6,5||||||||k*2,6*(s^1,2/M^1,3)|4,03E-01|kg/h|
|Escarpe|Escarpe|||||||||||||||0,855|8,55E-01|kg/km|
|Maquinaria fuera de ruta|Motoniveladora||||||||||95|0,2|0,8|0,2365|1,23|P*FP*C*(1+FD)*FA/1000|2,31E-02|kg/h|
|Maquinaria fuera de ruta|Compactadora||||||||||1043|0,045|0,8|0,2365|1,23|1,23|5,71E-02|kg/h|
|Maquinaria fuera de ruta|Bulldozer||||||||||161|0,1|0,8|0,2365|1,23|1,23|1,96E-02|kg/h|
|Maquinaria fuera de ruta|Retroexcavadora||||||||||71|0,2|0,8|0,2365|1,23|1,23|1,73E-02|kg/h|
|Maquinaria fuera de ruta|Grúa de apoyo||||||||||151|0,1|0,8|0,2365|1,23|1,23|1,84E-02|kg/h|
|Maquinaria fuera de ruta|Grúa principal||||||||||455|0,1|0,8|0,2365|1,23|1,23|5,54E-02|kg/h|
|Resuspensión camino No<br>Pavimentado|Camión rígido + 2 ejes|0,15|5|||20,4|0,814|||||||||k*0,2819*(s/12)^0,9*(W/2,72)^0,45*FCP|3,87E-02|kg/VKT|
|Resuspensión camino No<br>Pavimentado|Camión Semiremolque|0,15|5|||28|0,814||||||||||4,47E-02|kg/VKT|
|Resuspensión camino No<br>Pavimentado|liviano|0,15|5|||2,5|0,814||||||||||1,51E-02|kg/VKT|
|Resuspensión camino No<br>Pavimentado|Sobredimensionado|0,15|5|||38|0,814||||||||||5,13E-02|kg/VKT|
|Resuspensión camino<br>Pavimentado|Camión rígido + 2 ejes|0,15|||0,2|20,4|0,953|||||||||k*(sL)^0,91*(W*1,1023)^1,02/1000*FCP|7,91E-04|kg/VKT|
|Resuspensión camino<br>Pavimentado|Camión Semiremolque|0,15|||0,2|28,0|0,953||||||||||1,09E-03|kg/VKT|
|Resuspensión camino<br>Pavimentado|liviano|0,15|||0,2|2,5|0,953||||||||||9,30E-05|kg/VKT|
|Resuspensión camino<br>Pavimentado|Sobredimensionado|0,15|||0,2|38,0|0,953||||||||||1,49E-03|kg/VKT|
|Combustión vehículos|Camión rígido + 2 ejes|||||||||80||||||((0,5224+(4,4906*10^-3*V))+(((-<br>1,6281*10^-2-4,4906*10^-3)*(1-EXP(((-<br>1)* 2,4923*10^-2*V)))/2,4923*10^-<br>2)))/1000|8,82E-04|kg/VKT|
|Combustión vehículos|Camión Semiremolque|||||||||80|||||||8,82E-04|kg/VKT|
|Combustión vehículos|liviano|||||||||80||||||0,67*(4,5*10^-5*V^2-4,885*10^-<br>3*V+0,1932)/1000|6,06E-05|kg/VKT|
|Combustión vehículos|Sobredimensionado|||||||||30||||||((0,5224+(4,4906*10^-3*V))+(((-<br>1,6281*10^-2-4,4906*10^-3)*(1-EXP(((-<br>1)* 2,4923*10^-2*V)))/2,4923*10^-<br>2)))/1000|6,57E-04|kg/VKT|
|Combustión vehículos|Camión rígido + 2 ejes|||||||||40||||||((0,5224+(4,4906*10^-3*V))+(((-<br>1,6281*10^-2-4,4906*10^-3)*(1-EXP(((-<br>1)* 2,4923*10^-2*V)))/2,4923*10^-<br>2)))/1000|7,02E-04|kg/VKT|
|Combustión vehículos|Camión Semiremolque|||||||||40|||||||7,02E-04|kg/VKT|
|Combustión vehículos|liviano|||||||||40||||||0,67*(4,5*10^-5*V^2-4,885*10^-<br>3*V+0,1932)/1000|4,68E-05|kg/VKT|
|Combustión vehículos|Sobredimensionado|||||||||30||||||((0,5224+(4,4906*10^-3*V))+(((-<br>1,6281*10^-2-4,4906*10^-3)*(1-EXP(((-<br>1)* 2,4923*10^-2*V)))/2,4923*10^-<br>2)))/1000|6,57E-04|kg/VKT|
|Erosión Eólica|Erosión Eólica|0,075|||||||1,53|||||||k * (Σ Pi) * 10<br>Pi = 58x(u*-ut*)^2+25x(u*-ut*)|1,15|kg/ha/año|
|Grupos electrógenos|Grupos electrógenos||||||||||88|||||6,08E-03|6,08E-03|kg/kg comb.|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 52

**Tabla 28.** Factores de emisión de MPS del proyecto Parque Eólico Dañicalqui.

|Actividad|Col2|Parámetros para Factores de Emisión|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Factor Emisión|Col18|Col19|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Actividad**|**Actividad**|**k **|**s **|**U **|**sL**|**W **|**FCP**|**M **|**Σ Pi**|**V **|**P **|**FP**|**C **|**FD**|**FA**|**Fórmula**|**Valor**|**Unidad**|
|**Actividad**|**Actividad**|**k **|**% **|**m/s**|**g/m2 **|**t **|**t **|**% **|**% **|**km/h**|**kW**|**g/kW**|**g/kW**|**g/kW**|**g/kW**|**g/kW**|**g/kW**|**g/kW**|
|Excavaciones - preparación de terreno|Excavaciones - preparación de terreno|1|10,5|||||6,5||||||||k*2,6*(s^1,2/M^1,3)|3,83E+00|kg/h|
|Carga|Carga|0,74||5,0||||6,5||||||||k*0,0016*(U/2,2)^1,3/(M/2)^1,4|6,61E-04|kg/t|
|Descarga|Descarga|0,74||5,0||||6,5||||||||k*0,0016*(U/2,2)^1,3/(M/2)^1,4|6,61E-04|kg/t|
|Compactación|Compactación|1|10,5|||||6,5||||||||k*2,6*(s^1,2/M^1,3)|3,83E+00|kg/h|
|Escarpe|Escarpe|||||||||||||||5|5,70E+00|kg/km|
|Maquinaria fuera de ruta|Motoniveladora||||||||||95|0,2|0,8|0,2365|1,23|P*FP*C*(1+FD)*FA/1000|2,31E-02|kg/h|
|Maquinaria fuera de ruta|Compactadora||||||||||1043|0,045|0,8|0,2365|1,23|1,23|5,71E-02|kg/h|
|Maquinaria fuera de ruta|Bulldozer||||||||||161|0,1|0,8|0,2365|1,23|1,23|1,96E-02|kg/h|
|Maquinaria fuera de ruta|Retroexcavadora||||||||||71|0,2|0,8|0,2365|1,23|1,23|1,73E-02|kg/h|
|Maquinaria fuera de ruta|Grúa de apoyo||||||||||151|0,1|0,8|0,2365|1,23|1,23|1,84E-02|kg/h|
|Maquinaria fuera de ruta|Grúa principal||||||||||455|0,1|0,8|0,2365|1,23|1,23|5,54E-02|kg/h|
|Resuspensión camino No<br>Pavimentado|Camión rígido + 2 ejes|4,9|5|||20,4|0,814|||||||||k*0,2819*(s/12)^0,9*(W/2,72)^0,45*FCP|1,27E+00|kg/VKT|
|Resuspensión camino No<br>Pavimentado|Camión Semiremolque|4,9|5|||28|0,814||||||||||1,46E+00|kg/VKT|
|Resuspensión camino No<br>Pavimentado|liviano|4,9|5|||2,5|0,814||||||||||4,92E-01|kg/VKT|
|Resuspensión camino No<br>Pavimentado|Sobredimensionado|4,9|5|||38|0,814||||||||||1,67E+00|kg/VKT|
|Resuspensión camino<br>Pavimentado|Camión rígido + 2 ejes|3,23|||0,2|20,4|0,953|||||||||k*(sL)^0,91*(W*1,1023)^1,02/1000*FCP|1,70E-02|kg/VKT|
|Resuspensión camino<br>Pavimentado|Camión Semiremolque|3,23|||0,2|28,0|0,953||||||||||2,35E-02|kg/VKT|
|Resuspensión camino<br>Pavimentado|liviano|3,23|||0,2|2,5|0,953||||||||||2,00E-03|kg/VKT|
|Resuspensión camino<br>Pavimentado|Sobredimensionado|3,23|||0,2|38,0|0,953||||||||||3,21E-02|kg/VKT|
|Combustión vehículos|Camión rígido + 2 ejes|||||||||80||||||((0,5224+(4,4906*10^-3*V))+(((-<br>1,6281*10^-2-4,4906*10^-3)*(1-EXP(((-<br>1)* 2,4923*10^-2*V)))/2,4923*10^-<br>2)))/1000|8,82E-04|kg/VKT|
|Combustión vehículos|Camión Semiremolque|||||||||80|||||||8,82E-04|kg/VKT|
|Combustión vehículos|liviano|||||||||80||||||0,67*(4,5*10^-5*V^2-4,885*10^-<br>3*V+0,1932)/1000|6,06E-05|kg/VKT|
|Combustión vehículos|Sobredimensionado|||||||||30||||||((0,5224+(4,4906*10^-3*V))+(((-<br>1,6281*10^-2-4,4906*10^-3)*(1-EXP(((-<br>1)* 2,4923*10^-2*V)))/2,4923*10^-<br>2)))/1000|6,57E-04|kg/VKT|
|Combustión vehículos|Camión rígido + 2 ejes|||||||||40||||||((0,5224+(4,4906*10^-3*V))+(((-<br>1,6281*10^-2-4,4906*10^-3)*(1-EXP(((-<br>1)* 2,4923*10^-2*V)))/2,4923*10^-<br>2)))/1000|7,02E-04|kg/VKT|
|Combustión vehículos|Camión Semiremolque|||||||||40|||||||7,02E-04|kg/VKT|
|Combustión vehículos|liviano|||||||||40||||||0,67*(4,5*10^-5*V^2-4,885*10^-<br>3*V+0,1932)/1000|4,68E-05|kg/VKT|
|Combustión vehículos|Sobredimensionado|||||||||30||||||((0,5224+(4,4906*10^-3*V))+(((-<br>1,6281*10^-2-4,4906*10^-3)*(1-EXP(((-<br>1)* 2,4923*10^-2*V)))/2,4923*10^-<br>2)))/1000|6,57E-04|kg/VKT|
|Erosión Eólica|Erosión Eólica|1|||||||1,53|||||||k * (Σ Pi) * 10<br>Pi = 58x(u*-ut*)^2+25x(u*-ut*)|15,3|kg/ha/año|
|Grupos electrógenos|Grupos electrógenos||||||||||88|||||6,08E-03|6,08E-03|kg/kg comb.|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 53

**Tabla 29.** Factores de emisión de Gases del proyecto Parque Eólico Dañicalqui.

|Actividad|Col2|Parámetros para Factores de Emisión|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Factor Emisión|Col18|Col19|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Actividad**|**Actividad**|**k **|**s **|**U **|**sL**|**W **|**FCP**|**M **|**Σ Pi**|**V **|**P **|**FP**|**C **|**FD**|**FA**||||
|**Actividad**|**Actividad**|**k **|**% **|**m/s**|**g/m2 **|**t **|**t **|**% **|**% **|**km/h**|**kW**|**g/kW**|**g/kW**|**g/kW**|**g/kW**|**Fórmula**|**Valor**|**Unidad**|
|**NOx**|**NOx**|**NOx**|**NOx**|**NOx**|**NOx**|**NOx**|**NOx**|**NOx**|**NOx**|**NOx**|**NOx**|**NOx**|**NOx**|**NOx**|**NOx**|**NOx**|**NOx**|**NOx**|
|Maquinaria fuera<br>de ruta|Motoniveladora||||||||||95|5,2|0,8|0,0045|0,95|P*FP*C*(1+FD)*FA/1000|3.77E-01|kg/h|
|Maquinaria fuera<br>de ruta|Compactadora||||||||||1043|3,5|0,8|0,0045|0,95|0,95|2.79E+00|kg/h|
|Maquinaria fuera<br>de ruta|Bulldozer||||||||||161|5,2|0,8|0,0045|0,95|0,95|6.39E-01|kg/h|
|Maquinaria fuera<br>de ruta|Retroexcavadora||||||||||71|5,5|0,8|0,0045|0,95|0,95|2.98E-01|kg/h|
|Maquinaria fuera<br>de ruta|Grúa de apoyo||||||||||151|5,2|0,8|0,0045|0,95|0,95|5.99E-01|kg/h|
|Maquinaria fuera<br>de ruta|Grúa principal||||||||||455|5,2|0,8|0,0045|0,95|0,95|1.81E+00|kg/h|
|Combustión<br>vehículos<br>Pavimentado|Camión rígido + 2 ejes|||||||||80||||||((7,20536564798271+(16,4001356804762*EXP(((-<br>1)*0,0478197060782861)*V))) +(55,7002667265637*EXP(((-<br>1)*0,444673457893458)*V)))/1000|7.56E-03|kg/VKT|
|Combustión<br>vehículos<br>Pavimentado|Camión Semiremolque|||||||||80|||||||7.56E-03|kg/VKT|
|Combustión<br>vehículos<br>Pavimentado|liviano|||||||||80||||||0,84*(2,41*10^-4*V^2-3,181*10^-2*V+2,0247)/1000|8.59E-04|kg/VKT|
|Combustión<br>vehículos<br>Pavimentado|Sobredimensionado|||||||||30||||||((7,20536564798271+(16,4001356804762*EXP(((-<br>1)*0,0478197060782861)*V))) +(55,7002667265637*EXP(((-<br>1)*0,444673457893458)*V)))/1000|1.11E-02|kg/VKT|
|Combustión<br>vehículos No<br>Pavimentado|Camión rígido + 2 ejes|||||||||40||||||((7,20536564798271+(16,4001356804762*EXP(((-<br>1)*0,0478197060782861)*V))) +(55,7002667265637*EXP(((-<br>1)*0,444673457893458)*V)))/1000|9.63E-03|kg/VKT|
|Combustión<br>vehículos No<br>Pavimentado|Camión Semiremolque|||||||||40|||||||9.63E-03|kg/VKT|
|Combustión<br>vehículos No<br>Pavimentado|liviano|||||||||40||||||0,84*(2,41*10^-4*V^2-3,181*10^-2*V+2,0247)/1000|9.56E-04|kg/VKT|
|Combustión<br>vehículos No<br>Pavimentado|Sobredimensionado|||||||||30||||||((7,20536564798271+(16,4001356804762*EXP(((-<br>1)*0,0478197060782861)*V))) +(55,7002667265637*EXP(((-<br>1)*0,444673457893458)*V)))/1000|1.11E-02|kg/VKT|
|Grupos electrógenos|Grupos electrógenos||||||||||88|||||8,65E-02|8,65E-02|kg/kg comb.|
|**CO**|**CO**|**CO**|**CO**|**CO**|**CO**|**CO**|**CO**|**CO**|**CO**|**CO**|**CO**|**CO**|**CO**|**CO**|**CO**|**CO**|**CO**|**CO**|
|Maquinaria fuera<br>de ruta|Motoniveladora||||||||||95|1,5|0,8|0,0505|1,53|P*FP*C*(1+FD)*FA/1000|1.83E-01|kg/h|
|Maquinaria fuera<br>de ruta|Compactadora||||||||||1043|0,101|0,8|0,0505|1,53|1,53|1.35E-01|kg/h|
|Maquinaria fuera<br>de ruta|Bulldozer||||||||||161|1,5|0,8|0,0505|1,53|1,53|3.11E-01|kg/h|
|Maquinaria fuera<br>de ruta|Retroexcavadora||||||||||71|2,2|0,8|0,0505|1,53|1,53|2.01E-01|kg/h|
|Maquinaria fuera<br>de ruta|Grúa de apoyo||||||||||151|1,5|0,8|0,0505|1,53|1,53|2.91E-01|kg/h|
|Maquinaria fuera<br>de ruta|Grúa principal||||||||||455|1,5|0,8|0,0505|1,53|1,53|8.78E-01|kg/h|
|Combustión<br>vehículos<br>Pavimentado|Camión rígido + 2 ejes|||||||||80||||||(1/(((-<br>0,00010960585101578*(V2))+(0,0174064839534468*V))+0,0<br>779217214718428))/1000|1.30E-03|kg/VKT|
|Combustión<br>vehículos<br>Pavimentado|Camión Semiremolque|||||||||80|||||||1.30E-03|kg/VKT|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 54

|Actividad<br>liviano<br>Sobredimensionado|Col2|Parámetros para Factores de Emisión|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Factor Emisión|Col18|Col19|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Actividad**<br>liviano<br>Sobredimensionado|**Actividad**<br>liviano<br>Sobredimensionado|**k **|**s **|**U **|**sL**|**W **|**FCP**|**M **|**Σ Pi**|**V **|**P **|**FP**|**C **|**FD**|**FA**||||
|**Actividad**<br>liviano<br>Sobredimensionado|**Actividad**<br>liviano<br>Sobredimensionado|**k **|**% **|**m/s**|**g/m2 **|**t **|**t **|**% **|**% **|**km/h**|**kW**|**g/kW**|**g/kW**|**g/kW**|**g/kW**|**Fórmula**|**Valor**|**Unidad**|
|**Actividad**<br>liviano<br>Sobredimensionado|liviano|||||||||80||||||0,82*(2,23*10^-4*V^2-2,6*10^-2*V+1,076)/1000|3.47E-04|kg/VKT|
|**Actividad**<br>liviano<br>Sobredimensionado|Sobredimensionado|||||||||30||||||(1/(((-<br>0,00010960585101578*(V2))+(0,0174064839534468*V))+0,0<br>779217214718428))/1000|1.99E-03|kg/VKT|
|Combustión<br>vehículos No<br>Pavimentado|Camión rígido + 2 ejes|||||||||40||||||(1/(((-<br>0,00010960585101578*(V2))+(0,0174064839534468*V))+0,0<br>779217214718428))/1000|1.67E-03|kg/VKT|
|Combustión<br>vehículos No<br>Pavimentado|Camión Semiremolque|||||||||40|||||||1.67E-03|kg/VKT|
|Combustión<br>vehículos No<br>Pavimentado|liviano|||||||||40||||||0,82*(2,23*10^-4*V^2-2,6*10^-2*V+1,076)/1000|3.22E-04|kg/VKT|
|Combustión<br>vehículos No<br>Pavimentado|Sobredimensionado|||||||||30||||||(1/(((-<br>0,00010960585101578*(V2))+(0,0174064839534468*V))+0,0<br>779217214718428))/1000|1.99E-03|kg/VKT|
|Grupos electrógenos|Grupos electrógenos||||||||||88|||||1,86E-02|1,86E-02|kg/kg comb.|
|**SOx**|**SOx**|**SOx**|**SOx**|**SOx**|**SOx**|**SOx**|**SOx**|**SOx**|**SOx**|**SOx**|**SOx**|**SOx**|**SOx**|**SOx**|**SOx**|**SOx**|**SOx**|**SOx**|
|Maquinaria fuera<br>de ruta|Motoniveladora||||||||||95|0,0077|0,8|0|1|P*FP*C*(1+FD)*FA/1000|5.85E-04|kg/h|
|Maquinaria fuera<br>de ruta|Compactadora||||||||||1043|0,0077|0,8|0|1|1|6.26E-03|kg/h|
|Maquinaria fuera<br>de ruta|Bulldozer||||||||||161|0,0077|0,8|0|1|1|9.66E-04|kg/h|
|Maquinaria fuera<br>de ruta|Retroexcavadora||||||||||71|0,0077|0,8|0|1|1|4.43E-04|kg/h|
|Maquinaria fuera<br>de ruta|Grúa de apoyo||||||||||151|0,0077|0,8|0|1|1|9.06E-04|kg/h|
|Maquinaria fuera<br>de ruta|Grúa principal||||||||||455|0,0077|0,8|0|1|1|2.73E-03|kg/h|
|Combustión<br>vehículos<br>Pavimentado|Camión rígido + 2 ejes|||||||||80||||||2*((195,476155665251+(464,243926657849*EXP(((-<br>1)*0,0471738612383144)*V))) +(22777,7239789702*EXP(((-<br>1)*0,88418501143649)*V)))* Scomb/1000000/1000|2.06E-05|kg/VKT|
|Combustión<br>vehículos<br>Pavimentado|Camión Semiremolque|||||||||80|||||||2.06E-05|kg/VKT|
|Combustión<br>vehículos<br>Pavimentado|liviano|||||||||80||||||2*(0,0198*V^2-2,506*V+137,42)* Scomb/1000000/1000|6.37E-06|kg/VKT|
|Combustión<br>vehículos<br>Pavimentado|Sobredimensionado|||||||||30||||||2*((195,476155665251+(464,243926657849*EXP(((-<br>1)*0,0471738612383144)*V))) +(22777,7239789702*EXP(((-<br>1)*0,88418501143649)*V)))* Scomb/1000000/1000|3.08E-05|kg/VKT|
|Combustión<br>vehículos No<br>Pavimentado|Camión rígido + 2 ejes|||||||||40||||||2*((195,476155665251+(464,243926657849*EXP(((-<br>1)*0,0471738612383144)*V))) +(22777,7239789702*EXP(((-<br>1)*0,88418501143649)*V)))* Scomb/1000000/1000|2.66E-05|kg/VKT|
|Combustión<br>vehículos No<br>Pavimentado|Camión Semiremolque|||||||||40|||||||2.66E-05|kg/VKT|
|Combustión<br>vehículos No<br>Pavimentado|liviano|||||||||40||||||2*(0,0198*V^2-2,506*V+137,42)* Scomb/1000000/1000|6.89E-06|kg/VKT|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 55

|Actividad<br>Sobredimensionado|Col2|Parámetros para Factores de Emisión|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Factor Emisión|Col18|Col19|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Actividad**<br>Sobredimensionado|**Actividad**<br>Sobredimensionado|**k **|**s **|**U **|**sL**|**W **|**FCP**|**M **|**Σ Pi**|**V **|**P **|**FP**|**C **|**FD**|**FA**||||
|**Actividad**<br>Sobredimensionado|**Actividad**<br>Sobredimensionado|**k **|**% **|**m/s**|**g/m2 **|**t **|**t **|**% **|**% **|**km/h**|**kW**|**g/kW**|**g/kW**|**g/kW**|**g/kW**|**Fórmula**|**Valor**|**Unidad**|
|**Actividad**<br>Sobredimensionado|Sobredimensionado|||||||||30||||||2*((195,476155665251+(464,243926657849*EXP(((-<br>1)*0,0471738612383144)*V))) +(22777,7239789702*EXP(((-<br>1)*0,88418501143649)*V)))* Scomb/1000000/1000|3.08E-05|kg/VKT|
|Grupos electrógenos|Grupos electrógenos||||||||||88|||||5,69E-03|5,69E-03|kg/kg comb.|
|**HC**|**HC**|**HC**|**HC**|**HC**|**HC**|**HC**|**HC**|**HC**|**HC**|**HC**|**HC**|**HC**|**HC**|**HC**|**HC**|**HC**|**HC**|**HC**|
|Maquinaria fuera<br>de ruta|Motoniveladora||||||||||95|0,3|0,8|0,017|1,05|P*FP*C*(1+FD)*FA/1000|2.43E-02|kg/h|
|Maquinaria fuera<br>de ruta|Compactadora||||||||||1043|0,1|0,8|0,017|1,05|1,05|8.91E-02|kg/h|
|Maquinaria fuera<br>de ruta|Bulldozer||||||||||161|0,6|0,8|0,017|1,05|1,05|8.25E-02|kg/h|
|Maquinaria fuera<br>de ruta|Retroexcavadora||||||||||71|0,4|0,8|0,017|1,05|1,05|2.43E-02|kg/h|
|Maquinaria fuera<br>de ruta|Grúa de apoyo||||||||||151|0,3|0,8|0,017|1,05|1,05|3.87E-02|kg/h|
|Maquinaria fuera<br>de ruta|Grúa principal||||||||||455|0,3|0,8|0,017|1,05|1,05|1.17E-01|kg/h|
|Combustión<br>vehículos<br>Pavimentado|Camión rígido + 2 ejes|||||||||80||||||((0,162905538155383+(0,828009789857126*exp(((-<br>1)*0,0248119637491787)*V))) +(2,67001448123625*exp(((-<br>1)*0,124882855805357)*V)))|2.77E-01|kg/VKT|
|Combustión<br>vehículos<br>Pavimentado|Camión Semiremolque|||||||||80|||||||2.77E-01|kg/VKT|
|Combustión<br>vehículos<br>Pavimentado|liviano|||||||||80||||||0,62*(0,000017*V^2-<br>0,00284*V+0,2162)|6.06E-02|kg/VKT|
|Combustión<br>vehículos<br>Pavimentado|Sobredimensionado|||||||||30||||||((0,162905538155383+(0,828009789857126*exp(((-<br>1)*0,0248119637491787)*V)))+(2,67001448123625*exp(((-<br>1)*0,124882855805357)*V)))|6.19E-01|kg/VKT|
|Combustión<br>vehículos No<br>Pavimentado|Camión rígido + 2 ejes|||||||||40||||||((0,162905538155383+(0,828009789857126*exp(((-<br>1)*0,0248119637491787)*V))) +(2,67001448123625*exp(((-<br>1)*0,124882855805357)*V)))|4.88E-01|kg/VKT|
|Combustión<br>vehículos No<br>Pavimentado|Camión Semiremolque|||||||||40|||||||4.88E-01|kg/VKT|
|Combustión<br>vehículos No<br>Pavimentado|liviano|||||||||40||||||0,62*(0,0000175*V^2-<br>0,00284*V+0,2162)|8.05E-02|kg/VKT|
|Combustión<br>vehículos No<br>Pavimentado|Sobredimensionado|||||||||30||||||((0,162905538155383+(0,828009789857126*exp(((-<br>1)*0,0248119637491787)*V))) +(2,67001448123625*exp(((-<br>1)*0,124882855805357)*V)))|6.19E-01|kg/VKT|
|Grupos electrógenos|Grupos electrógenos||||||||||88|||||7,06E-03|7,06E-03|kg/kg comb.|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 56

**F.5.** **Niveles de Actividad del Proyecto**

**F.5.1 Fase de Construcción**

En esta sección se presentan los niveles de actividad de la fase de construcción del Proyecto utilizados

para el cálculo de emisiones de Gases y Partículas de esta fase. Es importante mencionar que, la

modelación de emisiones para la esta fase se realiza considerando el escenario más desfavorable, el cual

incluye el funcionamiento de todos los frentes de trabajo al mismo tiempo.

Esta fase está proyectada con una duración de 2 años y considera la construcción de 2 partes del proyecto,

el Parque Eólico (PE) y su Línea de Transmisión (LT) correspondiente. El cronograma de actividades se

presenta en **Tabla 30** .

**Tabla 30.** Cronograma de actividades de la fase de Construcción del proyecto Parque Eólico Dañicalqui.

|ACTIVIDAD FASE DE CONSTRUCCIÓN|Col2|Año 1|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Año 2|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|Col26|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**ACTIVIDAD FASE DE CONSTRUCCIÓN**|**ACTIVIDAD FASE DE CONSTRUCCIÓN**|**1 **|**2 **|**3 **|**4 **|**5 **|**6 **|**7 **|**8 **|**9 **|**1**<br>**0 **|**1**<br>**1 **|**1**<br>**2 **|**1**<br>**3 **|**1**<br>**4 **|**1**<br>**5 **|**1**<br>**6 **|**1**<br>**7 **|**1**<br>**8 **|**1**<br>**9 **|**2**<br>**0 **|**2**<br>**1 **|**2**<br>**2 **|**2**<br>**3 **|**2**<br>**4 **|
|**Generales**|Construcción de accesos y<br>puente en estero Culenco<br>y en río Dañicalqui|||||||||||||||||||||||||
|**Generales**|Topografía y mecánica de<br>suelo|||||||||||||||||||||||||
|**Generales**|Habilitación de instalación<br>de faenas y zona de acopio|||||||||||||||||||||||||
|**Generales**|Construcción de planta de<br>hormigón|||||||||||||||||||||||||
|**Parque Eólico**<br>**(PE)**|Construcción de caminos<br>proyectados, construcción<br>de obras de artes y puentes<br>internos|||||||||||||||||||||||||
|**Parque Eólico**<br>**(PE)**|Construcción de<br>fundaciones: Hormigonado|||||||||||||||||||||||||
|**Parque Eólico**<br>**(PE)**|Construcción de zanjas para<br>cableado eléctrico|||||||||||||||||||||||||
|**Parque Eólico**<br>**(PE)**|Montaje de los<br>aerogeneradores|||||||||||||||||||||||||
|**Línea de**<br>**Transmisión**<br>**(LT)**|Habilitación faja de<br>servidumbre|||||||||||||||||||||||||
|**Línea de**<br>**Transmisión**<br>**(LT)**|Materialización de<br>fundaciones de las<br>estructuras de la Línea de<br>transmisión|||||||||||||||||||||||||
|**Línea de**<br>**Transmisión**<br>**(LT)**|Montaje de estructuras de<br>línea de transmisión y<br>tendido de los conductores|||||||||||||||||||||||||
|**Línea de**<br>**Transmisión**<br>**(LT)**|Construcción de<br>subestación y sala de<br>control|||||||||||||||||||||||||
|**PE + LT**|Pruebas y puesta en<br>servicio|||||||||||||||||||||||||
|**PE + LT**|Limpieza general y retiro de<br>instalaciones|||||||||||||||||||||||||

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 57

En **Tabla 31** se indican los factores utilizados para calcular los niveles cada actividad que se presentan a

continuación en las siguientes secciones.

**Tabla 31.** Factores utilizados para calcular los niveles de actividad del proyecto Parque Eólico

Dañicalqui.

|Datos|Unidad|Cantidad|Cálculo de Actividad|
|---|---|---|---|
|Densidad del material|t/m3|1,610 (1)|Material de relleno y excavaciones|
|Rendimiento Excavadora (2)|m3/h|30|Horas de excavación de maquinaria|
|Rendimiento maquinaria escarpe (2)|km/ha|3,57|Kilómetros de escarpe|

_1:_ _Valor obtenido de promedio de densidad de muestras tomadas en terreno analizadas en laboratorio, valor incluye_

_efecto de esponjamiento de 1.2 (Anexo 3.2.1. Caracterización de edafología de la DIA, actualizado en_ _**Anexo 4 de la Adenda**_ _)_

_2:_ _Se asume el rendimiento de una retroexcavadora de acuerdo con la información de la Guía para la Estimación de_

_Emisiones Atmosféricas de Proyectos Inmobiliarios para la Región Metropolitana - 2019._

 - **Excavación**

El nivel de actividad correspondiente a Excavación por zona de trabajo se presenta en **Tabla 32** . Esta

información proviene de Ingeniería del proyecto para cada parte del proyecto. Con el rendimiento de la

maquinaria se obtuvieron las horas totales a usar. Se debe mencionar que, para la línea de transmisión

no se describen partes especificas dado que las actividades realizadas son de baja escala.

**Tabla 32.** Nivel de actividad correspondiente a excavación del proyecto Parque Eólico Dañicalqui.

|Parte del Proyecto|Información de<br>Cubicación|Unidad|Nivel actividad|Col5|Col6|Unidad|
|---|---|---|---|---|---|---|
|**Parte del Proyecto**|**Información de**<br>**Cubicación**|**Unidad**|**Año 1**|**Año 2**|**Total**|**Total**|
|**PE**|**PE**|**PE**|**PE**|**PE**|**PE**|**PE**|
|Plataformas, obras anexas(1) y caminos|374.609|m3|5.219|7.268|12.487|h|
|Aerogeneradores|54.217|m3|755|1.052|1.807|h|
|Puentes y obras de arte: Puente río Dañicalqui|797|m3|11|15|27|h|
|Puentes y obras de arte: Puente estero Culenco|105|m3|1|2|4|h|
|Puentes y obras de arte: Puente Canales|140|m3|2|3|5|h|
|Puentes y obras de arte: Obras de Arte|180|m3|3|3|6|h|
|Circuiros MT|5.801|m3|81|113|193|h|
|**LT**|**LT**|**LT**|**LT**|**LT**|**LT**|**LT**|
|Línea de Transmisión|2.520|m3|35|49|84|h|

_1:_ _Obras Anexas incluyen Instalación de Faenas, Planta de Hormigón y Subestación elevadora._

 - **Carguío de Material**

El nivel de actividad correspondiente al carguío de material se indica en la **Tabla 33** . Esta información fue

entregada por Ingeniería del proyecto para cada parte del proyecto. Con la densidad de material se

obtuvieron las toneladas a cargar.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 58

**Tabla 33.** Nivel de actividad correspondiente a carguío de material del proyecto Parque Eólico

Dañicalqui.

|Parte del Proyecto|Información de<br>Cubicación|Unidad|Nivel actividad|Col5|Col6|Unidad|
|---|---|---|---|---|---|---|
|**Parte del Proyecto**|**Información de**<br>**Cubicación**|**Unidad**|**Año 1**|**Año 2**|**Total**|**Total**|
|**PE**|**PE**|**PE**|**PE**|**PE**|**PE**|**PE**|
|Plataformas, obras anexas(1) y caminos|374.609|m3|252.098|351.023|603.121|t|
|Aerogeneradores|54.217|m3|36.486|50.804|87.290|t|
|Puentes y obras de arte: Puente río Dañicalqui|797|m3|536|747|1.283|t|
|Puentes y obras de arte: Puente estero Culenco|105|m3|71|98|169|t|
|Puentes y obras de arte: Puente Canales|140|m3|94|131|225|t|
|Puentes y obras de arte: Obras de Arte|180|m3|121|169|290|t|
|Circuiros MT|5.801|m3|3.904|5.436|9.340|t|
|Material de escarpe|32.020|m3|21.548|30.004|51.553|t|
|**LT**|**LT**|**LT**|**LT**|**LT**|**LT**|**LT**|
|Línea de Transmisión|2.520|m3|1.696|2.362|4.058|t|

_1:_ _Obras Anexas incluyen Instalación de Faenas, Planta de Hormigón y Subestación elevadora._

 - **Descarga de Material**

El nivel de actividad correspondiente a la descarga de material se presenta en la **Tabla 34.** Esta

información fue entregada por Ingeniería del proyecto para cada parte del proyecto. Con la densidad de

material se obtuvieron las toneladas a cargar. Este material corresponde a material que no se usa para

relleno como de fundaciones u otros y se va a acopio.

**Tabla 34.** Nivel de actividad correspondiente a descarga de material del proyecto Parque Eólico

Dañicalqui.

|Parte del Proyecto|Información de<br>Cubicación|Unidad|Nivel actividad|Col5|Col6|Unidad|
|---|---|---|---|---|---|---|
|**Parte del Proyecto**|**Información de**<br>**Cubicación**|**Unidad**|**Año 1**|**Año 2**|**Total**|**Total**|
|**PE**|**PE**|**PE**|**PE**|**PE**|**PE**|**PE**|
|Plataformas, obras anexas(1) y caminos|230.772|m3|155.301|216.242|371.543|t|
|Aerogeneradores|14.653|m3|9.861|13.731|23.592|t|
|Puentes y obras de arte: Puente río Dañicalqui|860|m3|578|806|1.384|t|
|Puentes y obras de arte: Puente estero Culenco|79|m3|53|74|128|t|
|Puentes y obras de arte: Puente Canales|106|m3|71|99|170|t|
|Puentes y obras de arte: Obras de Arte|119|m3|80|112|192|t|
|Material de escarpe|32.020|m3|21.548|30.004|51.553|t|
|**LT**|**LT**|**LT**|**LT**|**LT**|**LT**|**LT**|
|Línea de Transmisión|2.251|m3|1.515|2.109|3.624|t|

_1:_ _Obras Anexas incluyen Instalación de Faenas, Planta de Hormigón y Subestación elevadora._

 - **Compactación**

El nivel de actividad de compactación se indica en la **Tabla 35.** Esta información se actualizó con respecto

a la DIA y corresponde a las horas de compactación, las que se obtuvieron en base al área a recorrer,

número de pasadas, velocidad y ancho de la compactadora, como se muestra en la siguiente ecuación:

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 59

**Ecuación 16**

[m]

km [)] [ × N° pasadas]

Hrs.compactación =

ancho(m)×vel ~~(~~ [km] h

Área (m [2] )

[m]
h ~~[)]~~ [×1.000] ~~[(]~~ km

Se considera un ancho 2,44 metros, velocidad de 10 km/h y 5 pasadas.

**Tabla 35.** Nivel de actividad correspondiente a compactación del proyecto Parque Eólico Dañicalqui.

|Parte del Proyecto|Información de<br>Cubicación|Unidad|Nivel actividad|Col5|Col6|Unidad|
|---|---|---|---|---|---|---|
|**Parte del Proyecto**|**Información de**<br>**Cubicación**|**Unidad**|**Año 1**|**Año 2**|**Total**|**Total**|
|**PE**|**PE**|**PE**|**PE**|**PE**|**PE**|**PE**|
|Plataformas|79.800|m2|7|10|16|h|
|Subestación|5.100|m2|0,4|0,6|1|h|
|Caminos|69.300|m2|6|8|14|h|
|Instalación de faenas|17.900|m2|2|2|4|h|
|Planta de Hormigón|10.200|m2|1|1|2|h|
|Plataforma Acopio de Aspas|28.500|m2|2|3|6|h|
|Terraplén y corte|80.900|m2|7|10|17|h|
|**LT**|**LT**|**LT**|**LT**|**LT**|**LT**|**LT**|
|Zona de acopio LT|10.100|m2|1|1|2|h|

- **Escarpe**

El nivel de actividad de Escarpe se indica en **Tabla 36,** lo cual se actualizó con respecto al DIA con las áreas

entregadas por Ingeniería de los sitios a escarpar, y en conjunto con el rendimiento de la maquinaria se

obtuvieron los kilómetros a usar.

**Tabla 36.** Nivel de actividad correspondiente a escarpe del proyecto Parque Eólico Dañicalqui.

|Parte del Proyecto|Información de<br>Cubicación|Unidad|Nivel actividad|Col5|Col6|Unidad|
|---|---|---|---|---|---|---|
|**Parte del Proyecto**|**Información de**<br>**Cubicación**|**Unidad**|**Año 1**|**Año 2**|**Total**|**Total**|
|**PE**|**PE**|**PE**|**PE**|**PE**|**PE**|**PE**|
|Plataformas|7,98|ha|11,9|16,6|28,5|km|
|Subestación|0,51|ha|0,8|1,1|1,8|km|
|Caminos proyectos|6,93|ha|10,3|14,4|24,7|km|
|Instalación de faenas|1,79|ha|2,7|3,7|6,4|km|
|Planta de Hormigón|1,02|ha|1,5|2,1|3,6|km|
|Plataforma Acopio de Aspas|2,85|ha|4,3|5,9|10,2|km|
|Terraplén y corte|8,09|ha|12,1|16,8|28,9|km|
|**LT**|**LT**|**LT**|**LT**|**LT**|**LT**|**LT**|
|Zona de acopio LT|1,01|ha|1,5|2,1|3,6|km|

- **Maquinaria Fuera de Ruta**

El nivel de actividad correspondiente a horas de funcionamiento de maquinaria fuera de ruta. Esta

información se obtuvo con la cantidad de maquinaria y horas por día de funcionamiento entregada por

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 60

Ingeniería, lo que se indica en **Tabla 37** . Con la programación de la construcción del Proyecto se obtuvo

las horas de operación considerando trabajo de lunes a viernes y toda la maquinaria en funcionamiento.

El nivel de actividad obtenido se presenta en **Tabla 38** .

**Tabla 37.** Cantidad de maquinaria fuera de ruta y horas de operación del proyecto Parque Eólico

Dañicalqui.

|Maquinaria Construcción|Cantidad por día|Horas por día|
|---|---|---|
|Motoniveladora|4|9|
|Compactadora|3|9|
|Bulldozer|5|9|
|Retroexcavadora|5|9|
|Grúa de apoyo|1|7|
|Grúa principal|1|6|

**Tabla 38.** Nivel de actividad correspondiente a maquinaria fuera de ruta del proyecto Parque Eólico

Dañicalqui.

|Parte del Proyecto|Días de operación|Col3|Nivel actividad|Col5|Col6|Unidad|
|---|---|---|---|---|---|---|
|**Parte del Proyecto**|**Año 1**|**Año 2**|**Año 1**|**Año 2**|**Total**|**Total**|
|**PE**|**PE**|**PE**|**PE**|**PE**|**PE**|**PE**|
|Motoniveladora|352|22|12.672|792|13.464|h|
|Compactadora|352|22|9.504|594|10.098|h|
|Bulldozer|352|22|15.840|990|16.830|h|
|Retroexcavadora|374|198|16.830|8.910|25.740|h|
|Grúa de apoyo|0|154|0|1.078|1.078|h|
|Grúa principal|0|154|0|924|924|h|
|**LT**|**LT**|**LT**|**LT**|**LT**|**LT**|**LT**|
|Motoniveladora|88|198|3.168|7.128|10.296|h|
|Compactadora|88|198|2.376|5.346|7.722|h|
|Bulldozer|88|220|3.960|9.900|13.860|h|
|Retroexcavadora|88|220|3.960|9.900|13.860|h|
|Grúa de apoyo|0|88|0|616|616|h|
|Grúa principal|0|88|0|528|528|h|

- **Tránsito por Camino No Pavimentados**

El nivel de actividad correspondiente a distancia recorrida por vehículos en caminos no pavimentados fue

entregado por Ingeniería del proyecto para cada parte del proyecto, como cantidad de viajes (ida y vuelta)

y distancias en caminos no pavimentados a recorrer. De estas distancias se discriminó por caminos no

pavimentados con y sin control de emisiones.

En **Tabla 39** se muestran la cantidad de viajes ida y vuelta y distancias recorridas por cada tipo de vehículo

y actividad utilizado, separados por caminos externos e internos. Los caminos externos corresponden a

caminos pavimentados y no pavimentados existentes para acceder al proyecto y los internos son caminos

proyectados no pavimentados en la zona del Proyecto del parque eólico.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 61

También se presentan en la **Figura 20** y **Tabla 40** los tramos y las distancias de caminos no pavimentados

a incorporar control de emisiones por resuspensión. La eficiencia del supresor de polvo a aplicar varía

entre 90 y 95% (para efectos del cálculo de emisiones se consideró el valor más conservador de 90%).

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 62

**Tabla 39.** Cantidad de viajes ida y vuelta y kilómetros a recorrer por caminos no pavimentados externos e internos en la fase de

construcción del proyecto Parque Eólico Dañicalqui, por tipo de vehículo.

|Tipo<br>Camino|Nombre Item|Tipo vehículo|Cantidad de Viajes<br>(ida y vuelta)|Col5|Distancia<br>no pav. (km)|km no pavimentados|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Tipo**<br>**Camino**|**Nombre Item**|**Tipo vehículo**|**Año 1**|**Año 2**|**Año 2**|**Año 1**|**Año 2**|**Total**|
|**PE**|**PE**|**PE**|**PE**|**PE**|**PE**|**PE**|**PE**|**PE**|
|**Externo**|Construcción de accesos y puente|Camión Semiremolque|102|0|7,3|744,6|0|744,6|
|**Externo**|Topografía y mecánica de suelo|liviano|120|0|7,3|876|0|876|
|**Externo**|Habilitación de instalación de faenas y<br>zona de acopio|Camión Semiremolque|180|0|7,3|1.314|0|1.314|
|**Externo**|Construcción de planta de hormigón|Camión Semiremolque|120|0|7,3|876|0|876|
|**Externo**|Personal, combustible, agua, residuos|Camión rígido + 2 ejes|84|84|7,3|613,2|613,2|1.226,4|
|**Externo**|Personal, combustible, agua, residuos|Camión Semiremolque|396|396|7,3|2.890,8|2.890,8|5.781,6|
|**Externo**|Personal, combustible, agua, residuos|liviano|5.904|5.904|7,3|43.099,2|43.099,2|86.198,4|
|**Externo**|Construcción de caminos proyectados|Camión Semiremolque|13.125|2.625|7,3|95.812,5|19.162,5|114.975|
|**Externo**|Construcción de fundaciones:<br>Hormigonado|Camión Semiremolque|1.611|1.611|7,3|11.760,3|11.760,3|23.520,6|
|**Externo**|Construcción de zanjas para cableado<br>eléctrico|Camión Semiremolque|17|136|7,3|124,1|992,8|1.116,9|
|**Externo**|Montaje de Aerogeneradores|Camión rígido + 2 ejes|0|7|7,3|0|51,1|51,1|
|**Externo**|Montaje de Aerogeneradores|Camión Semiremolque|0|273|7,3|0|1.992,9|1.992,9|
|**Externo**|Montaje de Aerogeneradores|Sobredimensionado|0|70|7,3|0|511|511|
|**Externo**|Habilitación faja de servidumbre|Camión rígido + 2 ejes|0|120|7,3|0|876|876|
|**Externo**|Construcción de subestación y Sala de<br>Control|Camión Semiremolque|96|24|7,3|700,8|175,2|876|
|**Externo**|Pruebas y puesta en servicio|liviano|0|120|7,3|0|876|876|
|**Externo**|Limpieza general y retiro de<br>instalaciones|liviano|0|120|7,3|0|876|876|
|**Interno**|Construcción de accesos y puente|Camión rígido + 2 ejes|120|0|5,13|615,6|0|615,6|
|**Interno**|Construcción de accesos y puente|Camión Semiremolque|132|0|5,13|677,16|0|677,16|
|**Interno**|Topografía y mecánica de suelo|liviano|120|0|5,13|615,6|0|615,6|
|**Interno**|Construcción de planta de hormigón|Camión Semiremolque|120|0|5,13|615,6|0|615,6|
|**Interno**|Personal, combustible, agua, residuos|Camión rígido + 2 ejes|0|0|5,13|0|0|0|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 63

|Tipo<br>Camino|Nombre Item|Tipo vehículo|Cantidad de Viajes<br>(ida y vuelta)|Col5|Distancia<br>no pav. (km)|km no pavimentados|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Tipo**<br>**Camino**|**Nombre Item**|**Tipo vehículo**|**Año 1**|**Año 2**|**Año 2**|**Año 1**|**Año 2**|**Total**|
|**Tipo**<br>**Camino**|Personal, combustible, agua, residuos|Camión Semiremolque|324|324|5,13|1.662,12|1.662,12|3.324,24|
|**Tipo**<br>**Camino**|Personal, combustible, agua, residuos|liviano|5.688|5.688|5,13|29.179,44|29.179,44|58.358,88|
|**Tipo**<br>**Camino**|Construcción de caminos proyectados|Camión Semiremolque|21.405|4.281|5,13|109.807,65|21.961,53|131.769,18|
|**Tipo**<br>**Camino**|Construcción de fundaciones:<br>Hormigonado|Camión rígido + 2 ejes|3.342|3.342|5,13|17.144,46|17.144,46|34.288,92|
|**Tipo**<br>**Camino**|Construcción de fundaciones:<br>Hormigonado|Camión Semiremolque|2.103|2.103|5,13|10.788,39|10.788,39|21.576,78|
|**Tipo**<br>**Camino**|Construcción de zanjas para cableado<br>eléctrico|Camión rígido + 2 ejes|11|88|5,13|56,43|451,44|507,87|
|**Tipo**<br>**Camino**|Construcción de zanjas para cableado<br>eléctrico|Camión Semiremolque|48|384|5,13|246,24|1.969,92|2.216,16|
|**Tipo**<br>**Camino**|Montaje de Aerogeneradores|Camión rígido + 2 ejes|0|7|5,13|0|35,91|35,91|
|**Tipo**<br>**Camino**|Montaje de Aerogeneradores|Camión Semiremolque|0|273|5,13|0|1.400,49|1.400,49|
|**Tipo**<br>**Camino**|Montaje de Aerogeneradores|Sobredimensionado|0|70|5,13|0|359,1|359,1|
|**Tipo**<br>**Camino**|Habilitación faja de servidumbre|Camión rígido + 2 ejes|0|120|5,13|0|615,6|615,6|
|**Tipo**<br>**Camino**|Materialización de fundaciones de las<br>estructuras de la Línea de transmisión|Camión rígido + 2 ejes|0|45|5,13|0|230,85|230,85|
|**Tipo**<br>**Camino**|Materialización de fundaciones de las<br>estructuras de la Línea de transmisión|Camión Semiremolque|0|285|5,13|0|1.462,05|1.462,05|
|**Tipo**<br>**Camino**|Montaje de estructuras de línea de<br>transmisión y tendido de los<br>conductore|Camión Semiremolque|0|40|5,13|0|205,2|205,2|
|**Tipo**<br>**Camino**|Construcción de subestación y Sala de<br>Control|Camión Semiremolque|96|24|5,13|492,48|123,12|615,6|
|**Tipo**<br>**Camino**|Pruebas y puesta en servicio|liviano|0|120|5,13|0|615,6|615,6|
|**Tipo**<br>**Camino**|Limpieza general y retiro de<br>instalaciones|liviano|0|120|5,13|0|615,6|615,6|
|**LT**|**LT**|**LT**|**LT**|**LT**|**LT**|**LT**|**LT**|**LT**|
|**Externo**|Materialización de fundaciones de las<br>estructuras de la Línea de transmisión|Camión Semiremolque|0|155|3,1|0|480,5|480,5|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 64

|Tipo<br>Camino|Nombre Item|Tipo vehículo|Cantidad de Viajes<br>(ida y vuelta)|Col5|Distancia<br>no pav. (km)|km no pavimentados|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Tipo**<br>**Camino**|**Nombre Item**|**Tipo vehículo**|**Año 1**|**Año 2**|**Año 2**|**Año 1**|**Año 2**|**Total**|
|**Tipo**<br>**Camino**|Montaje de estructuras de línea de<br>transmisión y tendido de los<br>conductore|Camión Semiremolque|0|40|3,1|0|124|124|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 65

**Tabla 40.** Distancias de caminos externos e internos con supresor de polvo en la fase de construcción

del proyecto Parque Eólico Dañicalqui.

|Tipo Camino|Áreas con supresor Externo No Pavimentado|Distancia (m)|
|---|---|---|
|**Externo**|**Acceso PE**|**Acceso PE**|
|**Externo**|Área supresor 1|523|
|**Externo**|Área supresor 4|254|
|**Externo**|Área supresor 5|245|
|**Externo**|Área supresor 6|649|
|**Externo**|Área supresor 7|272|
|**Externo**|Área supresor 8|260|
|**Externo**|Área supresor 9|232|
|**Externo**|**Sub-Total PE**|**2.435**|
|**Externo**|**Acceso LT**|**Acceso LT**|
|**Externo**|Área supresor 2|405|
|**Externo**|**Sub-Total LT**|**405**|
|**Total Externo**|**Total Externo**|**2.840**|
|**Interno**|**Áreas con supresor Interno No Pavimentado**|**Distancia (m)**|
|**Interno**|Área supresor 3|276|
|**Interno**|Área supresor 4|113|
|**Total Interno**|**Total Interno**|**389**|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 66

**Figura 20.** Caminos externos e internos con supresor de polvo en la fase de construcción del proyecto

Parque Eólico Dañicalqui **.**

Con la información presentada anteriormente se obtiene el nivel de actividad por tránsito vehicular por

caminos no pavimentados externos e internos, con y sin supresor de polvo, que se indica en **Tabla 41** .

**Tabla 41.** Nivel de actividad correspondiente a distancia a recorrer por tránsito vehicular en caminos

externos e internos no pavimentados del proyecto Parque Eólico Dañicalqui, considerando

sin y con supresor de polvo.

|Tipo Camino|Tipo vehículo|Nivel actividad|Col4|Col5|Unidad|
|---|---|---|---|---|---|
|**Tipo Camino**|**Tipo vehículo**|**Año 1**|**Año 2**|**Total**|**Total**|
|**PE**|**PE**|**PE**|**PE**|**PE**|**PE**|
|Camino No Pavimentado<br>Externo (**sin Supresor de**<br>**Polvo**) Ruta N-85; SR/-861|Camión rígido + 2 ejes|409|1.027|1.435|km|
|Camino No Pavimentado<br>Externo (**sin Supresor de**<br>**Polvo**) Ruta N-85; SR/-861|Camión Semiremolque|76.123|24.641|100.764|km|
|Camino No Pavimentado<br>Externo (**sin Supresor de**<br>**Polvo**) Ruta N-85; SR/-861|liviano|29.307|29.891|59.197|km|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 67

|Tipo Camino|Tipo vehículo|Nivel actividad|Col4|Col5|Unidad|
|---|---|---|---|---|---|
|**Tipo Camino**|**Tipo vehículo**|**Año 1**|**Año 2**|**Total**|**Total**|
|**Tipo Camino**|Sobredimensionado|0|341|341|km|
|Camino No Pavimentado<br>Interno (**sin Supresor de**<br>**Polvo**)|Camión rígido + 2 ejes|16.465|17.077|33.543|km|
|Camino No Pavimentado<br>Interno (**sin Supresor de**<br>**Polvo**)|Camión Semiremolque|114.865|36.572|151.437|km|
|Camino No Pavimentado<br>Interno (**sin Supresor de**<br>**Polvo**)|liviano|27.536|28.105|55.640|km|
|Camino No Pavimentado<br>Interno (**sin Supresor de**<br>**Polvo**)|Sobredimensionado|0|332|332|km|
|Camino No Pavimentado<br>Externo (**con Supresor de**<br>**Polvo**) - Ruta N-85; SR/-861|Camión rígido + 2 ejes|205|514|718|km|
|Camino No Pavimentado<br>Externo (**con Supresor de**<br>**Polvo**) - Ruta N-85; SR/-861|Camión Semiremolque|38.100|12.333|50.434|km|
|Camino No Pavimentado<br>Externo (**con Supresor de**<br>**Polvo**) - Ruta N-85; SR/-861|liviano|14.668|14.961|29.629|km|
|Camino No Pavimentado<br>Externo (**con Supresor de**<br>**Polvo**) - Ruta N-85; SR/-861|Sobredimensionado|0|170|170|km|
|Camino No Pavimentado<br>Interno (**con Supresor de**<br>**Polvo**)|Camión rígido + 2 ejes|1.351|1.401|2.752|km|
|Camino No Pavimentado<br>Interno (**con Supresor de**<br>**Polvo**)|Camión Semiremolque|9.425|3.001|12.425|km|
|Camino No Pavimentado<br>Interno (**con Supresor de**<br>**Polvo**)|liviano|2.259|2.306|4.565|km|
|Camino No Pavimentado<br>Interno (**con Supresor de**<br>**Polvo**)|Sobredimensionado|0|27|27|km|
|**LT**|**LT**|**LT**|**LT**|**LT**|**LT**|
|Camino No Pavimentado<br>Externo (**sin Supresor de**<br>**Polvo**) - Ruta N-85; SR-857|Camión Semiremolque|0|526|526|km|
|Camino No Pavimentado<br>Externo (**con Supresor de**<br>**Polvo**) - Ruta N-85; SR-857|Camión Semiremolque|0|79|79|km|

- **Tránsito por Camino Pavimentados**

El nivel de actividad correspondiente a distancia recorrida por vehículos en caminos pavimentados fue

entregado por Ingeniería del proyecto para cada parte del proyecto, como cantidad de viajes (ida y vuelta)

y distancias en caminos pavimentados a recorrer. En **Tabla 42** se muestra la información de cantidad de

viajes ida y vuelta y distancias recorridas por ruta pavimentada N-85, los viajes y distancias recorridas

desde el puerto Lirquén hasta el cruce con ruta N-85, considerando la ruta 5 y 152, se presentan en **Tabla**

**43** .

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 68

**Tabla 42.** Cantidad de viajes ida y vuelta y kilómetros a recorrer por caminos pavimentados en ruta N-85 en la fase de construcción del

proyecto Parque Eólico Dañicalqui, por tipo de vehículo.

|Tipo|Nombre Item|Tipo vehículo|Cantidad de Viajes<br>(ida y vuelta)|Col5|Distancia pav.<br>(km)|km pavimentados|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Tipo**|**Nombre Item**|**Tipo vehículo**|**Año 1**|**Año 2**|**Año 2**|**año 1**|**año 2**|**Total**|
|**PE**|**PE**|**PE**|**PE**|**PE**|**PE**|**PE**|**PE**|**PE**|
|**Externo**|Construcción de accesos y puente|Camión Semiremolque|102|0|22,7|2.315,4|0|2.315,4|
|**Externo**|Topografía y mecánica de suelo|liviano|120|0|22,7|2.724|0|2.724|
|**Externo**|Habilitación de instalación de faenas y zona de<br>acopio|Camión Semiremolque|180|0|22,7|4.086|0|4.086|
|**Externo**|Construcción de planta de hormigón|Camión Semiremolque|120|0|22,7|2.724|0|2.724|
|**Externo**|Personal, combustible, agua, residuos|Camión rígido + 2 ejes|84|84|22,7|1.906,8|1.906,8|3.813,6|
|**Externo**|Personal, combustible, agua, residuos|Camión Semiremolque|396|396|22,7|8.989,2|8.989,2|17.978,4|
|**Externo**|Personal, combustible, agua, residuos|liviano|5.904|5.904|22,7|134.020,8|134.020,8|268.041,6|
|**Externo**|Construcción de caminos proyectados|Camión Semiremolque|13.125|2.625|22,7|297.937,5|59.587,5|357.525|
|**Externo**|Construcción de fundaciones: Hormigonado|Camión Semiremolque|1.611|1.611|22,7|36.569,7|36.569,7|73.139,4|
|**Externo**|Construcción de zanjas para cableado eléctrico|Camión Semiremolque|17|136|22,7|385,9|3.087,2|3.473,1|
|**Externo**|Montaje de Aerogeneradores|Camión rígido + 2 ejes|0|7|22,7|0|158,9|158,9|
|**Externo**|Montaje de Aerogeneradores|Camión Semiremolque|0|273|22,7|0|6.197,1|6.197,1|
|**Externo**|Montaje de Aerogeneradores|Sobredimensionado|0|70|22,7|0|1.589|1.589|
|**Externo**|Habilitación faja de servidumbre|Camión rígido + 2 ejes|0|120|22,7|0|2.724|2.724|
|**Externo**|Construcción de subestación y Sala de Control|Camión Semiremolque|96|24|22,7|2.179,2|544,8|2.724|
|**Externo**|Pruebas y puesta en servicio|liviano|0|120|22,7|0|2.724|2.724|
|**Externo**|Limpieza general y retiro de instalaciones|liviano|0|120|22,7|0|2.724|2.724|
|**LT**|**LT**|**LT**|**LT**|**LT**|**LT**|**LT**|**LT**|**LT**|
|**Externo**|Materialización de fundaciones de las<br>estructuras de la Línea de transmisión|Camión Semiremolque|0|155|16,4|0|2542|2542|
|**Externo**|Montaje de estructuras de línea de transmisión<br>y tendido de los conductore|Camión Semiremolque|0|40|16,4|0|656|656|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 69

**Tabla 43.** Cantidad de viajes y kilómetros a recorrer por caminos pavimentados en rutas 5 y 152 en la fase de construcción del proyecto

Parque Eólico Dañicalqui, por tipo de vehículo.

|Sector|Tipo vehículo|Cantidad de viajes Ruta 5-152|Col4|Col5|Distancia<br>pav. (km)|km pavimentados|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Sector**|**Tipo vehículo**|**Año 1**|**Año 2**|**Total**|**Total**|**Año 1**|**Año 2**|**Total**|
|**PE**|Camión rígido + 2 ejes|84|211|295|113|9.492|23.843|33.335|
|**PE**|Camión Semiremolque|15.647|5.065|20.712|113|1.768.111|572.345|2.340.456|
|**PE**|liviano|6.024|6.144|12.168|113|680.712|694.272|1.374.984|
|**PE**|Sobredimensionado|0|70|70|113|0|7.910|7.910|
|**LT**|Camión Semiremolque|0|195|195|113|0|22.035|22.035|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 70

El resumen del nivel de actividad correspondiente a distancia recorrida por vehículos en caminos

pavimentados se presenta en **Tabla 44** .

**Tabla 44.** Nivel de actividad correspondiente a distancia a recorrer por tránsito vehicular en caminos

pavimentados del proyecto Parque Eólico Dañicalqui.

|Tipo Camino|Tipo vehículo|Nivel actividad|Col4|Col5|Unidad|
|---|---|---|---|---|---|
|**Tipo Camino**|**Tipo vehículo**|**Año 1**|**Año 2**|**Total**|**Total**|
|**PE**|**PE**|**PE**|**PE**|**PE**|**PE**|
|Camino Pavimentado<br>Externo -<br>Ruta N-85; SR/-861|Camión rígido + 2 ejes|1.907|4.790|6.697|km|
|Camino Pavimentado<br>Externo -<br>Ruta N-85; SR/-861|Camión Semiremolque|355.187|114.976|470.162|km|
|Camino Pavimentado<br>Externo -<br>Ruta N-85; SR/-861|liviano|136.745|139.469|276.214|km|
|Camino Pavimentado<br>Externo -<br>Ruta N-85; SR/-861|Sobredimensionado|0|1.589|1.589|km|
|Camino Pavimentado<br>Externo -<br>Rutas 5 y 152|Camión rígido + 2 ejes|9.492|23.843|33.335|km|
|Camino Pavimentado<br>Externo -<br>Rutas 5 y 152|Camión Semiremolque|1.768.111|572.345|2.340.456|km|
|Camino Pavimentado<br>Externo -<br>Rutas 5 y 152|liviano|680.712|694.272|1.374.984|km|
|Camino Pavimentado<br>Externo -<br>Rutas 5 y 152|Sobredimensionado|0|7.910|7.910|km|
|**LT**|**LT**|**LT**|**LT**|**LT**|**LT**|
|Camino Pavimentado<br>Externo -<br>Ruta N-85; SR-857|Camión Semiremolque|0|3.198|3.198|km|
|Camino Pavimentado<br>Externo -<br>Rutas 5 y 152|Camión Semiremolque|0|22.035|22.035|km|

- **Combustión de motores vehiculares**

El nivel de actividad corresponde a la distancia recorrida por vehículos en caminos pavimentados y no

pavimentados. Estos niveles se presentan en **Tabla 45** .

**Tabla 45.** Nivel de actividad correspondiente a distancia a recorrer por tránsito vehicular en caminos

pavimentados y no pavimentados para combustión de motores vehiculares del proyecto

Parque Eólico Dañicalqui.

|Tipo de camino|Tipo vehículo|Nivel actividad|Col4|Col5|Unidad|
|---|---|---|---|---|---|
|**Tipo de camino**|**Tipo vehículo**|**Año 1**|**Año 2**|**Total**|**Total**|
|**PE**|**PE**|**PE**|**PE**|**PE**|**PE**|
|Combustión vehículos<br>Pavimentado|Camión rígido + 2 ejes|1.907|4.790|6.697|km|
|Combustión vehículos<br>Pavimentado|Camión Semiremolque|355.187|114.976|470.162|km|
|Combustión vehículos<br>Pavimentado|liviano|136.745|139.469|276.214|km|
|Combustión vehículos<br>Pavimentado|Sobredimensionado|0|1.589|1.589|km|
|Combustión vehículos<br>No Pavimentado|Camión rígido + 2 ejes|18.430|20.019|38.448|km|
|Combustión vehículos<br>No Pavimentado|Camión Semiremolque|238.513|76.547|315.060|km|
|Combustión vehículos<br>No Pavimentado|liviano|73.770|75.262|149.032|km|
|Combustión vehículos<br>No Pavimentado|Sobredimensionado|0|870|870|km|
|Combustión vehículos<br>No Pavimentado Ruta<br>5-152|Camión rígido + 2 ejes|9.492|23.843|33.335|km|
|Combustión vehículos<br>No Pavimentado Ruta<br>5-152|Camión Semiremolque|1.768.111|594.380|2.340.456|km|
|Combustión vehículos<br>No Pavimentado Ruta<br>5-152|liviano|680.712|694.272|1.374.984|km|
|Combustión vehículos<br>No Pavimentado Ruta<br>5-152|Sobredimensionado|0|7.910|7.910|km|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 71

|Tipo de camino|Tipo vehículo|Nivel actividad|Col4|Col5|Unidad|
|---|---|---|---|---|---|
|**Tipo de camino**|**Tipo vehículo**|**Año 1**|**Año 2**|**Total**|**Total**|
|**LT**|**LT**|**LT**|**LT**|**LT**|**LT**|
|Combustión vehículos<br>Pavimentado|Camión Semiremolque|0|3.198|3.198|km|
|Combustión vehículos<br>No Pavimentado|Camión Semiremolque|0|605|605|km|
|Combustión vehículos<br>No Pavimentado Ruta<br>5-152|Camión Semiremolque|0|22.035|22.035|km|

- **Erosión Eólica**

El nivel de actividad correspondiente a erosión eólica corresponde al área erosionable del Acopio, la que

se consideró conservadoramente como el total del acopio de 1,01 ha, tal como se indica en **Tabla 46** .

**Tabla 46.** Nivel de actividad correspondiente a erosión eólica de la fase de construcción del proyecto

Parque Eólico Dañicalqui.

|Actividad|Nivel actividad|Col3|Col4|Unidad|
|---|---|---|---|---|
|**Actividad**|**Año 1**|**Año 2**|**Total**|**Total**|
|**LT**|**LT**|**LT**|**LT**|**LT**|
|Acopio|1,01|1,01|1,01|ha|

- **Grupos electrógenos**

El nivel de actividad correspondiente a la cantidad de combustible utilizado por los grupos electrógenos a

usar se indica en **Tabla 47** . Esta información fue obtenida a partir de la cantidad de equipos y horas por

de funcionamiento entregada por Ingeniería. Los grupos electrógenos a utilizar corresponden a 2 equipos

diésel de 88 kW / 110 kVA con un rendimiento de 23,9 l/h. Para determinar el nivel de actividad se

consideraron 2.376 horas de uso anual para cada grupo electrógeno producto de las actividades de

construcción. En base a esto y la densidad del combustible (Diésel; 0,815 kg/l) se obtuvo la cantidad de

combustible anual.

**Tabla 47.** Nivel de actividad correspondiente a funcionamiento de grupos electrógenos durante la fase

de construcción del proyecto Parque Eólico Dañicalqui.

|Instalación|Cantidad de<br>equipos|Nivel actividad|Col4|Col5|Unidad|
|---|---|---|---|---|---|
|**Instalación**|**Cantidad de**<br>**equipos**|**Año 1**|**Año 2**|**Total**|**Total**|
|Instalación de faenas|2|104.180|104.180|208.361|kg comb|

**F.5.2. Fase de Operación**

En esta sección se presentan los niveles de actividad de la fase de operación del Proyecto utilizados para

el cálculo de emisiones de Gases y Partículas de esta fase. Esta fase tendrá una duración de 35 años y los

niveles de actividad que se presentarán a continuación son en base anual.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 72

- **Tránsito por Camino No Pavimentados**

El nivel de actividad correspondiente a distancia recorrida por vehículos en caminos no pavimentados fue

entregado por Ingeniería del proyecto para cada parte del proyecto, como cantidad de viajes y distancias

en caminos no pavimentados a recorrer.

Los viajes y distancias recorridas por cada tipo de vehículo y actividad utilizado, separados por caminos

externos e internos se muestran en **Tabla 48** . Los caminos externos corresponden a caminos no

pavimentados existentes para acceder al proyecto y los internos son caminos proyectados no

pavimentados en la zona del Proyecto del parque eólico.

**Tabla 48.** Cantidad de viajes y kilómetros a recorrer por caminos no pavimentados externos e internos

en la fase de operación del proyecto Parque Eólico Dañicalqui, por tipo de vehículo.

|Actividad|Tipo de<br>vehículo|Viajes<br>año|Distancia recorrida en<br>caminos no pavimentados|Col5|km no pavimentados|Col7|
|---|---|---|---|---|---|---|
|**Actividad**|**Tipo de**<br>**vehículo**|**Viajes**<br>**año**|**Caminos**<br>**Externos (de**<br>**acceso públicos)**|**Caminos**<br>**internos**|**Caminos**<br>**Externos (de**<br>**acceso públicos)**|**Caminos**<br>**internos**|
|Supervisión y mantenciones|Vehículo liviano|1.800|7,3|6|26.280|21.600|
|Mantención|Camión 3/4|12|7,3|6|175,2|144|
|Agua Potable|Aljibe|24|7,3|6|350,4|288|
|Residuos peligrosos|Camión 3/4|4|7,3|6|58,4|48|
|Residuos domiciliarios|Camión 3/4|48|7,3|6|700,8|576|

Con la información presentada anteriormente se obtiene el nivel de actividad por tránsito vehicular por

caminos no pavimentados externos e internos, que se indica en **Tabla 49** para la fase de operación.

**Tabla 49.** Nivel de actividad correspondiente a distancia a recorrer por tránsito vehicular en caminos

externos e internos no pavimentados en la fase de operación del proyecto Parque Eólico

Dañicalqui.

|Tipo Camino|Tipo vehículo|Nivel actividad|Unidad|
|---|---|---|---|
|Caminos No Pavimentados -<br>Externo|Vehículo liviano|26.280|km|
|Caminos No Pavimentados -<br>Externo|Camión 3/4 Mantención|175|km|
|Caminos No Pavimentados -<br>Externo|Aljibe|350|km|
|Caminos No Pavimentados -<br>Externo|Camión 3/4 - Residuos Peligrosos|58|km|
|Caminos No Pavimentados -<br>Externo|Camión 3/4 - Residuos Domiciliarios|701|km|
|Caminos No Pavimentados -<br>Interno|Vehículo liviano|21.600|km|
|Caminos No Pavimentados -<br>Interno|Camión 3/4 Mantención|144|km|
|Caminos No Pavimentados -<br>Interno|Aljibe|288|km|
|Caminos No Pavimentados -<br>Interno|Camión 3/4 - Residuos Peligrosos|48|km|
|Caminos No Pavimentados -<br>Interno|Camión 3/4 - Residuos Domiciliarios|576|km|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 73

- **Tránsito por Camino Pavimentados**

El nivel de actividad correspondiente a distancia recorrida por vehículos en caminos pavimentados fue

entregado por Ingeniería del proyecto para cada parte del proyecto, como cantidad de viajes y distancias

en caminos pavimentados a recorrer. Esta información se muestra en **Tabla 50** .

**Tabla 50.** Cantidad de viajes y kilómetros a recorrer por caminos pavimentados en la fase de operación

del proyecto Parque Eólico Dañicalqui, por tipo de vehículo.

|Actividad|Tipo de vehículo|Viajes año|Distancia de camino<br>pavimentado|km recorridos<br>pavimentados|
|---|---|---|---|---|
|**Ruta N-85**|**Ruta N-85**|**Ruta N-85**|**Ruta N-85**|**Ruta N-85**|
|Supervisión y mantenciones|Vehículo liviano|1.800|21|75.600|
|Mantención|Camión 3/4|12|21|504|
|Agua Potable|Aljibe|24|21|1.008|
|Residuos peligrosos|Camión 3/4|4|40|320|
|Residuos domiciliarios|Camión 3/4|48|40|3.840|
|**Ruta 5 y 152**|**Ruta 5 y 152**|**Ruta 5 y 152**|**Ruta 5 y 152**|**Ruta 5 y 152**|
|Supervisión y mantenciones|Vehículo liviano|1.800|113|406.800|
|Mantención|Camión 3/4|12|113|2.712|
|Agua Potable|Aljibe|24|113|5.424|
|Residuos peligrosos|Camión 3/4|4|113|904|
|Residuos domiciliarios|Camión 3/4|48|113|10.848|

El nivel de actividad correspondiente a distancia recorrida por vehículos en caminos pavimentados en la

fase de operación se presenta en **Tabla 51** .

**Tabla 51.** Nivel de actividad correspondiente a distancia a recorrer por tránsito vehicular en caminos

pavimentados de la fase de operación del proyecto Parque Eólico Dañicalqui.

|Tipo Camino|Tipo vehículo|Nivel actividad|Unidad|
|---|---|---|---|
|Caminos Pavimentados<br>Ruta N-85|Vehículo liviano|75.600|km|
|Caminos Pavimentados<br>Ruta N-85|Camión 3/4 Mantención|504|km|
|Caminos Pavimentados<br>Ruta N-85|Aljibe|1.008|km|
|Caminos Pavimentados<br>Ruta N-85|Camión 3/4 - Residuos Peligrosos|320|km|
|Caminos Pavimentados<br>Ruta N-85|Camión 3/4 - Residuos Domiciliarios|3.840|km|
|Caminos Pavimentados<br>Rutas 5 y 152|Vehículo liviano|406.800|km|
|Caminos Pavimentados<br>Rutas 5 y 152|Camión 3/4 Mantención|2.712|km|
|Caminos Pavimentados<br>Rutas 5 y 152|Aljibe|5.424|km|
|Caminos Pavimentados<br>Rutas 5 y 152|Camión 3/4 - Residuos Peligrosos|904|km|
|Caminos Pavimentados<br>Rutas 5 y 152|Camión 3/4 - Residuos Domiciliarios|10.848|km|

- **Combustión de motores vehiculares**

El nivel de actividad corresponde a la distancia recorrida por vehículos en caminos pavimentados y no

pavimentados. Estos niveles se presentan en **Tabla 52** .

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 74

**Tabla 52.** Nivel de actividad correspondiente a distancia a recorrer por tránsito vehicular en caminos

pavimentados y no pavimentados para combustión de motores vehiculares de la fase de

operación del proyecto Parque Eólico Dañicalqui.

|Tipo camino|Tipo vehículo|Nivel actividad|Unidad|
|---|---|---|---|
|Camino Pavimentados<br>Ruta 85|Vehículo liviano|75.600|km|
|Camino Pavimentados<br>Ruta 85|Camión 3/4 Mantención|504|km|
|Camino Pavimentados<br>Ruta 85|Aljibe|1.008|km|
|Camino Pavimentados<br>Ruta 85|Camión 3/4 - Residuos Peligrosos|320|km|
|Camino Pavimentados<br>Ruta 85|Camión 3/4 - Residuos Domiciliarios|3.840|km|
|Camino Pavimentados<br>Ruta 5 y 152|Vehículo liviano|406.800|km|
|Camino Pavimentados<br>Ruta 5 y 152|Camión 3/4 Mantención|2.712|km|
|Camino Pavimentados<br>Ruta 5 y 152|Aljibe|5.424|km|
|Camino Pavimentados<br>Ruta 5 y 152|Camión 3/4 - Residuos Peligrosos|904|km|
|Camino Pavimentados<br>Ruta 5 y 152|Camión 3/4 - Residuos Domiciliarios|10.848|km|
|Caminos No<br>Pavimentados|Vehículo liviano|47.880|km|
|Caminos No<br>Pavimentados|Camión 3/4 Mantención|319|km|
|Caminos No<br>Pavimentados|Aljibe|638|km|
|Caminos No<br>Pavimentados|Camión 3/4 - Residuos Peligrosos|106|km|
|Caminos No<br>Pavimentados|Camión 3/4 - Residuos Domiciliarios|1.277|km|

- **Maquinaria Fuera de Ruta**

El nivel de actividad correspondiente a horas de funcionamiento de maquinaria fuera de ruta. En esta fase

se utilizará una grúa pluma 1 vez al año por 8 horas para las actividades de desbroce de la LT, lo que se

indica en **Tabla 53** . El nivel de actividad obtenido se presenta en **Tabla 54** .

**Tabla 53.** Cantidad de maquinaria fuera de ruta y horas de operación del proyecto Parque Eólico

Dañicalqui, fase de operación.

|Maquinaria Construcción|Cantidad por día|Horas por día|
|---|---|---|
|Grúa pluma|1|8|

**Tabla 54.** Nivel de actividad correspondiente a maquinaria fuera de ruta del proyecto Parque Eólico

Dañicalqui, fase de operación.

|Parte del Proyecto|Nivel actividad|Unidad|
|---|---|---|
|Grúa pluma|8|h|

- **Grupos electrógenos**

El nivel de actividad correspondiente a la cantidad de combustible utilizado por los grupos electrógenos a

usar se indica en **Tabla 55** . Esta información fue obtenida a partir de la cantidad de equipos y horas por

de funcionamiento entregada por Ingeniería. Los grupos electrógenos a utilizar corresponden a 2 equipos

diésel de 88 kW / 110 kVA con un rendimiento de 23,9 l/h que se utilizará solo en caso de emergencia.

Para determinar el nivel de actividad se consideraron 120 horas de uso anual como peor condición

producto de las actividades de operación. En base a esto y la densidad del combustible (Diésel; 0,815 kg/l)

se obtuvo la cantidad de combustible anual.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 75

**Tabla 55.** Nivel de actividad correspondiente a funcionamiento de grupos electrógenos durante la fase

de construcción del proyecto Parque Eólico Dañicalqui.

|Equipo|Cantidad de equipos|Nivel actividad|Unidad|
|---|---|---|---|
|Grupo electrógenos de emergencia|2|2.630,82|kg comb|

**F.5.3. Fase de Cierre**

Los niveles de actividad de la fase de cierre del Proyecto son homólogos a la fase de construcción,

considerado como el peor escenario de actividades emisoras. Estos niveles se presentan en **sección F.5.1** .

**F.6.** **Cálculo de Emisiones de Partículas y Gases**

**F.6.1. Fase de Construcción**

Las emisiones de MP10, MP2,5, MPS, NOx, CO, SOx y HC debido a las actividades del proyecto Parque

Eólico Dañicalqui durante toda la fase de construcción se presentan en **Tabla 56** a **Tabla 62**,

respectivamente. En estas tablas se muestran las emisiones calculadas siguiendo la metodología indicada

en **Sección F.2.**, se indica cada factor según actividad emisora (presentados en **Sección F.3.** y **F.4.** ) y se

presenta el nivel de actividad expuesto en **Sección F.5** .

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 76

**Tabla 56.** Emisiones de MP10 debido a las actividades de la fase de Construcción del Proyecto Parque Eólico Dañicalqui, Sectores Parque

Eólico (PE) y Línea de Transmisión (LT).

|Sector|Actividad|Col3|Factor Emisión|Col5|Eficiencia<br>Mitigación|Nivel de Actividad|Col8|Col9|Unidad|Emisión MP10 (t/año)|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Sector**|**Actividad**|**Actividad**|**Valor**|**Unidad**|**Unidad**|**Año 1**|**Año 2**|**Total**|**Total**|**Año 1**|**Año 2**|**Total**|
|**PE**|Excavaciones -<br>preparación de<br>terreno|Plataformas y caminos|8,36E-01|kg/h|0%|5.219|7.268|12.487|h|4,36|6,07|10,43|
|**PE**|Excavaciones -<br>preparación de<br>terreno|Aerogeneradores|8,36E-01|kg/h|0%|755|1.052|1.807|h|0,63|0,88|1,51|
|**PE**|Excavaciones -<br>preparación de<br>terreno|Puentes y obras de arte: Puente río<br>Dañicalqui|8,36E-01|kg/h|0%|11|15|27|h|0,01|0,01|0,02|
|**PE**|Excavaciones -<br>preparación de<br>terreno|Puentes y obras de arte: Puente<br>estero Culenco|8,36E-01|kg/h|0%|1|2|4|h|0,00|0,00|0,00|
|**PE**|Excavaciones -<br>preparación de<br>terreno|Puentes y obras de arte: Puente<br>Canales|8,36E-01|kg/h|0%|2|3|5|h|0,00|0,00|0,00|
|**PE**|Excavaciones -<br>preparación de<br>terreno|Puentes y obras de arte: Obras de<br>Arte|8,36E-01|kg/h|0%|3|3|6|h|0,00|0,00|0,01|
|**PE**|Excavaciones -<br>preparación de<br>terreno|Circuiros MT|8,36E-01|kg/h|0%|81|113|193|h|0,07|0,09|0,16|
|**LT**|**LT**|Línea de Transmisión|8,36E-01|kg/h|0%|35|49|84|h|0,03|0,04|0,07|
|**PE**|Carga|Plataformas y caminos|3,13E-04|kg/t|0%|252.098|351.023|603.121|t|0,08|0,11|0,19|
|**PE**|Carga|Aerogeneradores|3,13E-04|kg/t|0%|36.486|50.804|87.290|t|0,01|0,02|0,03|
|**PE**|Carga|Puentes y obras de arte: Puente río<br>Dañicalqui|3,13E-04|kg/t|0%|536|747|1.283|t|0,00|0,00|0,00|
|**PE**|Carga|Puentes y obras de arte: Puente<br>estero Culenco|3,13E-04|kg/t|0%|71|98|169|t|0,00|0,00|0,00|
|**PE**|Carga|Puentes y obras de arte: Puente<br>Canales|3,13E-04|kg/t|0%|94|131|225|t|0,00|0,00|0,00|
|**PE**|Carga|Puentes y obras de arte: Obras de<br>Arte|3,13E-04|kg/t|0%|121|169|290|t|0,00|0,00|0,00|
|**PE**|Carga|Circuiros MT|3,13E-04|kg/t|0%|3.904|5.436|9.340|t|0,00|0,00|0,00|
|**PE**|Carga|Material de escarpe|3,13E-04|kg/t|0%|21.548|30.004|51.553|t|0,01|0,01|0,02|
|**LT**|**LT**|Línea de Transmisión|3,13E-04|kg/t|0%|1.696|2.362|4.058|t|0,00|0,00|0,00|
|**PE**|Descarga|Plataformas y caminos|3,13E-04|kg/t|0%|155.301|216.242|371.543|t|0,05|0,07|0,12|
|**PE**|Descarga|Aerogeneradores|3,13E-04|kg/t|0%|9.861|13.731|23.592|t|0,00|0,00|0,01|
|**PE**|Descarga|Puentes y obras de arte: Puente río<br>Dañicalqui|3,13E-04|kg/t|0%|578|806|1.384|t|0,00|0,00|0,00|
|**PE**|Descarga|Puentes y obras de arte: Puente<br>estero Culenco|3,13E-04|kg/t|0%|53|74|128|t|0,00|0,00|0,00|
|**PE**|Descarga|Puentes y obras de arte: Puente<br>Canales|3,13E-04|kg/t|0%|71|99|170|t|0,00|0,00|0,00|
|**PE**|Descarga|Puentes y obras de arte: Obras de<br>Arte|3,13E-04|kg/t|0%|80|112|192|t|0,00|0,00|0,00|
|**PE**|Descarga|Material de escarpe|3,13E-04|kg/t|0%|21.548|30.004|51.553|t|0,01|0,01|0,02|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 77

|Sector|Actividad<br>Línea de Transmisión|Col3|Factor Emisión|Col5|Eficiencia<br>Mitigación|Nivel de Actividad|Col8|Col9|Unidad|Emisión MP10 (t/año)|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Sector**|**Actividad**<br>Línea de Transmisión|**Actividad**<br>Línea de Transmisión|**Valor**|**Unidad**|**Unidad**|**Año 1**|**Año 2**|**Total**|**Total**|**Año 1**|**Año 2**|**Total**|
|**LT**|**LT**|Línea de Transmisión|3,13E-04|kg/t|0%|1.515|2.109|3.624|t|0,00|0,00|0,00|
|**PE**|Compactación|Plataformas|8,36E-01|kg/h|0%|7|10|16|h|0,01|0,01|0,01|
|**PE**|Compactación|Subestación|8,36E-01|kg/h|0%|0|1|1|h|0,00|0,00|0,00|
|**PE**|Compactación|Caminos|8,36E-01|kg/h|0%|6|8|14|h|0,00|0,01|0,01|
|**PE**|Compactación|Instalación de faenas|8,36E-01|kg/h|0%|2|2|4|h|0,00|0,00|0,00|
|**PE**|Compactación|Planta de Hormigón|8,36E-01|kg/h|0%|1|1|2|h|0,00|0,00|0,00|
|**PE**|Compactación|Plataforma Acopio de Aspas|8,36E-01|kg/h|0%|2|3|6|h|0,00|0,00|0,00|
|**PE**|Compactación|Terraplén y corte|8,36E-01|kg/h|0%|7|10|17|h|0,01|0,01|0,01|
|**LT**|**LT**|Zona de acopio LT|8,36E-01|kg/h|0%|1|1|2|h|0,00|0,00|0,00|
|**PE**|Escarpe|Plataformas|5,70E+00|kg/km|0%|12|17|28|km|0,07|0,09|0,16|
|**PE**|Escarpe|Subestación|5,70E+00|kg/km|0%|1|1|2|km|0,00|0,01|0,01|
|**PE**|Escarpe|Caminos|5,70E+00|kg/km|0%|10|14|25|km|0,06|0,08|0,14|
|**PE**|Escarpe|Instalación de faenas|5,70E+00|kg/km|0%|3|4|6|km|0,02|0,02|0,04|
|**PE**|Escarpe|Planta de Hormigón|5,70E+00|kg/km|0%|2|2|4|km|0,01|0,01|0,02|
|**PE**|Escarpe|Plataforma Acopio de Aspas|5,70E+00|kg/km|0%|4|6|10|km|0,02|0,03|0,06|
|**PE**|Escarpe|Terraplén y corte|5,70E+00|kg/km|0%|12|17|29|km|0,07|0,10|0,16|
|**LT**|**LT**|Zona de acopio LT|5,70E+00|kg/km|0%|2|2|4|km|0,01|0,01|0,02|
|**PE**|Maquinaria fuera de<br>ruta|Motoniveladora|2,31E-02|kg/h|0%|12.672|792|13.464|h|0,29|0,02|0,31|
|**PE**|Maquinaria fuera de<br>ruta|Compactadora|5,71E-02|kg/h|0%|9.504|594|10.098|h|0,54|0,03|0,58|
|**PE**|Maquinaria fuera de<br>ruta|Bulldozer|1,96E-02|kg/h|0%|15.840|990|16.830|h|0,31|0,02|0,33|
|**PE**|Maquinaria fuera de<br>ruta|Retroexcavadora|1,73E-02|kg/h|0%|16.830|8.910|25.740|h|0,29|0,15|0,44|
|**PE**|Maquinaria fuera de<br>ruta|Grúa de apoyo|1,84E-02|kg/h|0%|0|1.078|1.078|h|0,00|0,02|0,02|
|**PE**|Maquinaria fuera de<br>ruta|Grúa principal|5,54E-02|kg/h|0%|0|924|924|h|0,00|0,05|0,05|
|**LT**|Maquinaria fuera de<br>ruta|Motoniveladora|2,31E-02|kg/h|0%|3.168|7.128|10.296|h|0,07|0,16|0,24|
|**LT**|Maquinaria fuera de<br>ruta|Compactadora|5,71E-02|kg/h|0%|2.376|5.346|7.722|h|0,14|0,31|0,44|
|**LT**|Maquinaria fuera de<br>ruta|Bulldozer|1,96E-02|kg/h|0%|3.960|9.900|13.860|h|0,08|0,19|0,27|
|**LT**|Maquinaria fuera de<br>ruta|Retroexcavadora|1,73E-02|kg/h|0%|3.960|9.900|13.860|h|0,07|0,17|0,24|
|**LT**|Maquinaria fuera de<br>ruta|Grúa de apoyo|1,84E-02|kg/h|0%|0|616|616|h|0,00|0,01|0,01|
|**LT**|Maquinaria fuera de<br>ruta|Grúa principal|5,54E-02|kg/h|0%|0|528|528|h|0,00|0,03|0,03|
|**PE**|Resuspensión camino<br>No Pavimentado<br>Externo - Ruta N-<br>85;SR/-861 (SS)|Camión rígido + 2 ejes|3,87E-01|kg/VKT|0%|409|1.027|1.435|km|0,16|0,40|0,56|
|**PE**|Resuspensión camino<br>No Pavimentado<br>Externo - Ruta N-<br>85;SR/-861 (SS)|Camión Semiremolque|4,47E-01|kg/VKT|0%|76.123|24.641|100.764|km|34,01|11,01|45,02|
|**PE**|Resuspensión camino<br>No Pavimentado<br>Externo - Ruta N-<br>85;SR/-861 (SS)|liviano|1,51E-01|kg/VKT|0%|29.307|29.891|59.197|km|4,42|4,50|8,92|
|**PE**|Resuspensión camino<br>No Pavimentado<br>Externo - Ruta N-<br>85;SR/-861 (SS)|Sobredimensionado|5,13E-01|kg/VKT|0%|0|341|341|km|0,00|0,17|0,17|
|**PE**|Resuspensión camino<br>No Pavimentado<br>Interno (SS)|Camión rígido + 2 ejes|3,87E-01|kg/VKT|0%|16.465|17.077|33.543|km|6,38|6,62|13,00|
|**PE**|Resuspensión camino<br>No Pavimentado<br>Interno (SS)|Camión Semiremolque|4,47E-01|kg/VKT|0%|114.865|36.572|151.437|km|51,32|16,34|67,66|
|**PE**|Resuspensión camino<br>No Pavimentado<br>Interno (SS)|liviano|1,51E-01|kg/VKT|0%|27.536|28.105|55.640|km|4,15|4,23|8,38|
|**PE**|Resuspensión camino<br>No Pavimentado<br>Interno (SS)|Sobredimensionado|5,13E-01|kg/VKT|0%|0|332|332|km|0,00|0,17|0,17|
|**PE**||Camión rígido + 2 ejes|3,27E-03|kg/VKT|0%|1.907|4.790|6.697|km|0,01|0,02|0,02|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 78

|Sector|Actividad<br>Resuspensión camino Camión Semiremolque<br>Pavimentado Externo - liviano<br>Ruta N-85;SR/-861 Sobredimensionado|Col3|Factor Emisión|Col5|Eficiencia<br>Mitigación|Nivel de Actividad|Col8|Col9|Unidad|Emisión MP10 (t/año)|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Sector**|**Actividad**<br>Resuspensión camino<br>Pavimentado Externo -<br>Ruta N-85;SR/-861<br>Camión Semiremolque<br>liviano<br>Sobredimensionado|**Actividad**<br>Resuspensión camino<br>Pavimentado Externo -<br>Ruta N-85;SR/-861<br>Camión Semiremolque<br>liviano<br>Sobredimensionado|**Valor**|**Unidad**|**Unidad**|**Año 1**|**Año 2**|**Total**|**Total**|**Año 1**|**Año 2**|**Total**|
|**Sector**|**Actividad**<br>Resuspensión camino<br>Pavimentado Externo -<br>Ruta N-85;SR/-861<br>Camión Semiremolque<br>liviano<br>Sobredimensionado|Camión Semiremolque|4,52E-03|kg/VKT|0%|355.187|114.976|470.162|km|1,60|0,52|2,12|
|**Sector**|**Actividad**<br>Resuspensión camino<br>Pavimentado Externo -<br>Ruta N-85;SR/-861<br>Camión Semiremolque<br>liviano<br>Sobredimensionado|liviano|3,84E-04|kg/VKT|0%|136.745|139.469|276.214|km|0,05|0,05|0,11|
|**Sector**|**Actividad**<br>Resuspensión camino<br>Pavimentado Externo -<br>Ruta N-85;SR/-861<br>Camión Semiremolque<br>liviano<br>Sobredimensionado|Sobredimensionado|6,17E-03|kg/VKT|0%|0|1.589|1.589|km|0,00|0,01|0,01|
|**Sector**|Resuspensión camino<br>Pavimentado Externo -<br>Ruta 5-152|Camión rígido + 2 ejes|3,27E-03|kg/VKT|0%|9.492|23.843|33.335|km|0,03|0,08|0,11|
|**Sector**|Resuspensión camino<br>Pavimentado Externo -<br>Ruta 5-152|Camión Semiremolque|4,52E-03|kg/VKT|0%|1.768.111|572.345|2.340.456|km|7,99|2,59|10,57|
|**Sector**|Resuspensión camino<br>Pavimentado Externo -<br>Ruta 5-152|liviano|3,84E-04|kg/VKT|0%|680.712|694.272|1.374.984|km|0,26|0,27|0,53|
|**Sector**|Resuspensión camino<br>Pavimentado Externo -<br>Ruta 5-152|Sobredimensionado|6,17E-03|kg/VKT|0%|0|7.910|7.910|km|0,00|0,05|0,05|
|**LT**|Resusp. No<br>Pavimentado Externo -<br>Ruta N-85;SR-857 (SS)|Camión Semiremolque|4,47E-01|kg/VKT|0%|0|526|526|km|0,00|0,23|0,23|
|**LT**|Resusp. Pavimentado<br>Externo - Ruta N-<br>85;SR-857|Camión Semiremolque|4,52E-03|kg/VKT|0%|0|3.198|3.198|km|0,00|0,01|0,01|
|**LT**|Resusp. Pavimentado<br>Externo - Ruta 5-152|Camión Semiremolque|4,52E-03|kg/VKT|0%|0|22.035|22.035|km|0,00|0,10|0,10|
|**PE**|Resuspensión camino<br>No Pavimentado<br>Externo - Ruta N-<br>85;SR/-861 (CS)|Camión rígido + 2 ejes|3,87E-01|kg/VKT|90%|205|514|718|km|0,01|0,02|0,03|
|**PE**|Resuspensión camino<br>No Pavimentado<br>Externo - Ruta N-<br>85;SR/-861 (CS)|Camión Semiremolque|4,47E-01|kg/VKT|90%|38.100|12.333|50.434|km|1,70|0,55|2,25|
|**PE**|Resuspensión camino<br>No Pavimentado<br>Externo - Ruta N-<br>85;SR/-861 (CS)|liviano|1,51E-01|kg/VKT|90%|14.668|14.961|29.629|km|0,22|0,23|0,45|
|**PE**|Resuspensión camino<br>No Pavimentado<br>Externo - Ruta N-<br>85;SR/-861 (CS)|Sobredimensionado|5,13E-01|kg/VKT|90%|0|170|170|km|0,00|0,01|0,01|
|**PE**|Resuspensión camino<br>No Pavimentado<br>Interno (CS)|Camión rígido + 2 ejes|3,87E-01|kg/VKT|90%|1.351|1.401|2.752|km|0,05|0,05|0,11|
|**PE**|Resuspensión camino<br>No Pavimentado<br>Interno (CS)|Camión Semiremolque|4,47E-01|kg/VKT|90%|9.425|3.001|12.425|km|0,42|0,13|0,56|
|**PE**|Resuspensión camino<br>No Pavimentado<br>Interno (CS)|liviano|1,51E-01|kg/VKT|90%|2.259|2.306|4.565|km|0,03|0,03|0,07|
|**PE**|Resuspensión camino<br>No Pavimentado<br>Interno (CS)|Sobredimensionado|5,13E-01|kg/VKT|90%|0|27|27|km|0,00|0,00|0,00|
|**LT**|Resusp. No<br>Pavimentado Externo -<br>Ruta N-85;SR-857 (CS)|Camión Semiremolque|4,47E-01|kg/VKT|90%|0|79|79|km|0,00|0,00|0,00|
|**PE**|Combustión vehículos<br>Pavimentado|Camión rígido + 2 ejes|8,82E-04|kg/VKT|0%|1.907|4.790|6.697|km|0,00|0,00|0,01|
|**PE**|Combustión vehículos<br>Pavimentado|Camión Semiremolque|8,82E-04|kg/VKT|0%|355.187|114.976|470.162|km|0,31|0,10|0,41|
|**PE**|Combustión vehículos<br>Pavimentado|liviano|6,06E-05|kg/VKT|0%|136.745|139.469|276.214|km|0,01|0,01|0,02|
|**PE**|Combustión vehículos<br>Pavimentado|Sobredimensionado|6,57E-04|kg/VKT|0%|0|1.589|1.589|km|0,00|0,00|0,00|
|**PE**|Combustión vehículos<br>No Pavimentado|Camión rígido + 2 ejes|7,02E-04|kg/VKT|0%|18.430|20.019|38.448|km|0,01|0,01|0,03|
|**PE**|Combustión vehículos<br>No Pavimentado|Camión Semiremolque|7,02E-04|kg/VKT|0%|238.513|76.547|315.060|km|0,17|0,05|0,22|
|**PE**|Combustión vehículos<br>No Pavimentado|liviano|4,68E-05|kg/VKT|0%|73.770|75.262|149.032|km|0,00|0,00|0,01|
|**PE**|Combustión vehículos<br>No Pavimentado|Sobredimensionado|6,57E-04|kg/VKT|0%|0|870|870|km|0,00|0,00|0,00|
|**LT**|Combustión vehículos<br>Pavimentado|Camión rígido + 2 ejes|8,82E-04|kg/VKT|0%|0|0|0|km|0,00|0,00|0,00|
|**LT**|Combustión vehículos<br>Pavimentado|Camión Semiremolque|8,82E-04|kg/VKT|0%|0|3.198|3.198|km|0,00|0,00|0,00|
|**LT**|Combustión vehículos<br>Pavimentado|liviano|6,06E-05|kg/VKT|0%|0|0|0|km|0,00|0,00|0,00|
|**LT**|Combustión vehículos<br>Pavimentado|Sobredimensionado|6,57E-04|kg/VKT|0%|0|0|0|km|0,00|0,00|0,00|
|**LT**||Camión rígido + 2 ejes|7,02E-04|kg/VKT|0%|0|0|0|km|0,00|0,00|0,00|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 79

|Sector|Actividad<br>Camión Semiremolque<br>Combustión vehículos<br>liviano<br>No Pavimentado<br>Sobredimensionado|Col3|Factor Emisión|Col5|Eficiencia<br>Mitigación|Nivel de Actividad|Col8|Col9|Unidad|Emisión MP10 (t/año)|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Sector**|**Actividad**<br>Combustión vehículos<br>No Pavimentado<br>Camión Semiremolque<br>liviano<br>Sobredimensionado|**Actividad**<br>Combustión vehículos<br>No Pavimentado<br>Camión Semiremolque<br>liviano<br>Sobredimensionado|**Valor**|**Unidad**|**Unidad**|**Año 1**|**Año 2**|**Total**|**Total**|**Año 1**|**Año 2**|**Total**|
|**Sector**|**Actividad**<br>Combustión vehículos<br>No Pavimentado<br>Camión Semiremolque<br>liviano<br>Sobredimensionado|Camión Semiremolque|7,02E-04|kg/VKT|0%|0|605|605|km|0,00|0,00|0,00|
|**Sector**|**Actividad**<br>Combustión vehículos<br>No Pavimentado<br>Camión Semiremolque<br>liviano<br>Sobredimensionado|liviano|4,68E-05|kg/VKT|0%|0|0|0|km|0,00|0,00|0,00|
|**Sector**|**Actividad**<br>Combustión vehículos<br>No Pavimentado<br>Camión Semiremolque<br>liviano<br>Sobredimensionado|Sobredimensionado|6,57E-04|kg/VKT|0%|0|0|0|km|0,00|0,00|0,00|
|**PE**|Combustión vehículos<br>Pavimentado Ruta 5-<br>182|Camión rígido + 2 ejes|8,82E-04|kg/VKT|0%|9.492|23.843|33.335|km|0,01|0,02|0,03|
|**PE**|Combustión vehículos<br>Pavimentado Ruta 5-<br>182|Camión Semiremolque|8,82E-04|kg/VKT|0%|1.768.111|594.380|2.340.456|km|1,56|0,52|2,06|
|**PE**|Combustión vehículos<br>Pavimentado Ruta 5-<br>182|liviano|6,06E-05|kg/VKT|0%|680.712|694.272|1.374.984|km|0,04|0,04|0,08|
|**PE**|Combustión vehículos<br>Pavimentado Ruta 5-<br>182|Sobredimensionado|6,57E-04|kg/VKT|0%|0|7.910|7.910|km|0,00|0,01|0,01|
|**LT**|**LT**|Camión Semiremolque|8,82E-04|kg/VKT|0%|0|22.035|22.035|km|0,00|0,02|0,02|
|**LT**|Erosión Eólica|Acopio|7,6|kg/ha/año|0%|1,01|1,01|1,01|ha|0,01|0,01|0,01|
|**PE**|Grupos electrógenos|Instalación de faenas|6,08E-03|kg/kg comb.|0%|104.180|104.180|208.361|kg comb.|0,63|0,63|1,27|
|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**122,91 **|**58,74 **|**181,61 **|

**Tabla 57.** Emisiones de MP2,5 debido a las actividades de la fase de Construcción del Proyecto Parque Eólico Dañicalqui, Sectores Parque

Eólico (PE) y Línea de Transmisión (LT).

|Sector|Actividad|Col3|Factor Emisión|Col5|Eficiencia<br>Mitigación|Nivel de Actividad|Col8|Col9|Col10|Emisión MP2,5 (t/año)|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Sector**|**Actividad**|**Actividad**|**Valor**|**Unidad**|**Unidad**|**Año 1**|**Año 2**|**Total**|**Unidad**|**Año 1**|**Año 2**|**Total**|
|**PE**|Excavaciones -<br>preparación de<br>terreno|Plataformas y caminos|4,03E-01|kg/h|0%|5.219|7.268|12.487|h|2,10|2,93|5,03|
|**PE**|Excavaciones -<br>preparación de<br>terreno|Aerogeneradores|4,03E-01|kg/h|0%|755|1.052|1.807|h|0,30|0,42|0,73|
|**PE**|Excavaciones -<br>preparación de<br>terreno|Puentes y obras de arte: Puente río<br>Dañicalqui|4,03E-01|kg/h|0%|11|15|27|h|0,00|0,01|0,01|
|**PE**|Excavaciones -<br>preparación de<br>terreno|Puentes y obras de arte: Puente estero<br>Culenco|4,03E-01|kg/h|0%|1|2|4|h|0,00|0,00|0,00|
|**PE**|Excavaciones -<br>preparación de<br>terreno|Puentes y obras de arte: Puente<br>Canales|4,03E-01|kg/h|0%|2|3|5|h|0,00|0,00|0,00|
|**PE**|Excavaciones -<br>preparación de<br>terreno|Puentes y obras de arte: Obras de Arte|4,03E-01|kg/h|0%|3|3|6|h|0,00|0,00|0,00|
|**PE**|Excavaciones -<br>preparación de<br>terreno|Circuiros MT|4,03E-01|kg/h|0%|81|113|193|h|0,03|0,05|0,08|
|**LT**|**LT**|Línea de Transmisión|4,03E-01|kg/h|0%|35|49|84|h|0,01|0,02|0,03|
|**PE**|Carga|Plataformas y caminos|4,73E-05|kg/t|0%|252.098|351.023|603.121|t|0,01|0,02|0,03|
|**PE**|Carga|Aerogeneradores|4,73E-05|kg/t|0%|36.486|50.804|87.290|t|0,00|0,00|0,00|
|**PE**|Carga|Puentes y obras de arte: Puente río<br>Dañicalqui|4,73E-05|kg/t|0%|536|747|1.283|t|0,00|0,00|0,00|
|**PE**|Carga|Puentes y obras de arte: Puente estero<br>Culenco|4,73E-05|kg/t|0%|71|98|169|t|0,00|0,00|0,00|
|**PE**|Carga|Puentes y obras de arte: Puente<br>Canales|4,73E-05|kg/t|0%|94|131|225|t|0,00|0,00|0,00|
|**PE**|Carga|Puentes y obras de arte: Obras de Arte|4,73E-05|kg/t|0%|121|169|290|t|0,00|0,00|0,00|
|**PE**|Carga|Circuiros MT|4,73E-05|kg/t|0%|3.904|5.436|9.340|t|0,00|0,00|0,00|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 80

|Sector|Actividad<br>Material de escarpe<br>Línea de Transmisión|Col3|Factor Emisión|Col5|Eficiencia<br>Mitigación|Nivel de Actividad|Col8|Col9|Col10|Emisión MP2,5 (t/año)|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Sector**|**Actividad**<br>Material de escarpe<br>Línea de Transmisión|**Actividad**<br>Material de escarpe<br>Línea de Transmisión|**Valor**|**Unidad**|**Unidad**|**Año 1**|**Año 2**|**Total**|**Unidad**|**Año 1**|**Año 2**|**Total**|
|**Sector**|**Actividad**<br>Material de escarpe<br>Línea de Transmisión|Material de escarpe|4,73E-05|kg/t|0%|21.548|30.004|51.553|t|0,00|0,00|0,00|
|**LT**|**LT**|Línea de Transmisión|4,73E-05|kg/t|0%|1.696|2.362|4.058|t|0,00|0,00|0,00|
|**PE**|Descarga|Plataformas y caminos|4,73E-05|kg/t|0%|155.301|216.242|371.543|t|0,01|0,01|0,02|
|**PE**|Descarga|Aerogeneradores|4,73E-05|kg/t|0%|9.861|13.731|23.592|t|0,00|0,00|0,00|
|**PE**|Descarga|Puentes y obras de arte: Puente río<br>Dañicalqui|4,73E-05|kg/t|0%|578|806|1.384|t|0,00|0,00|0,00|
|**PE**|Descarga|Puentes y obras de arte: Puente estero<br>Culenco|4,73E-05|kg/t|0%|53|74|128|t|0,00|0,00|0,00|
|**PE**|Descarga|Puentes y obras de arte: Puente<br>Canales|4,73E-05|kg/t|0%|71|99|170|t|0,00|0,00|0,00|
|**PE**|Descarga|Puentes y obras de arte: Obras de Arte|4,73E-05|kg/t|0%|80|112|192|t|0,00|0,00|0,00|
|**PE**|Descarga|Material de escarpe|4,73E-05|kg/t|0%|21.548|30.004|51.553|t|0,00|0,00|0,00|
|**LT**|**LT**|Línea de Transmisión|4,73E-05|kg/t|0%|1.515|2.109|3.624|t|0,00|0,00|0,00|
|**PE**|Compactación|Plataformas|4,03E-01|kg/h|0%|7|10|16|h|0,003|0,004|0,007|
|**PE**|Compactación|Subestación|4,03E-01|kg/h|0%|0|1|1|h|0,000|0,000|0,000|
|**PE**|Compactación|Caminos|4,03E-01|kg/h|0%|6|8|14|h|0,002|0,003|0,006|
|**PE**|Compactación|Instalación de faenas|4,03E-01|kg/h|0%|2|2|4|h|0,001|0,001|0,001|
|**PE**|Compactación|Planta de Hormigón|4,03E-01|kg/h|0%|1|1|2|h|0,000|0,000|0,001|
|**PE**|Compactación|Plataforma Acopio de Aspas|4,03E-01|kg/h|0%|2|3|6|h|0,001|0,001|0,002|
|**PE**|Compactación|Terraplén y corte|4,03E-01|kg/h|0%|7|10|17|h|0,003|0,004|0,007|
|**LT**|**LT**|Zona de acopio LT|4,03E-01|kg/h|0%|1|1|2|h|0,000|0,000|0,001|
|**PE**|Escarpe|Plataformas|5,70E+00|kg/km|0%|12|17|28|km|0,07|0,09|0,16|
|**PE**|Escarpe|Subestación|5,70E+00|kg/km|0%|1|1|2|km|0,00|0,01|0,01|
|**PE**|Escarpe|Caminos|5,70E+00|kg/km|0%|10|14|25|km|0,06|0,08|0,14|
|**PE**|Escarpe|Instalación de faenas|5,70E+00|kg/km|0%|3|4|6|km|0,02|0,02|0,04|
|**PE**|Escarpe|Planta de Hormigón|5,70E+00|kg/km|0%|2|2|4|km|0,01|0,01|0,02|
|**PE**|Escarpe|Plataforma Acopio de Aspas|5,70E+00|kg/km|0%|4|6|10|km|0,02|0,03|0,06|
|**PE**|Escarpe|Terraplén y corte|5,70E+00|kg/km|0%|12|17|29|km|0,07|0,10|0,16|
|**LT **|**LT **|Zona de acopio LT|5,70E+00|kg/km|0%|2|2|4|km|0,01|0,01|0,02|
|**PE**|Maquinaria fuera de<br>ruta|Motoniveladora|2,31E-02|kg/h|0%|12.672|792|13.464|h|0,29|0,02|0,31|
|**PE**|Maquinaria fuera de<br>ruta|Compactadora|5,71E-02|kg/h|0%|9.504|594|10.098|h|0,54|0,03|0,58|
|**PE**|Maquinaria fuera de<br>ruta|Bulldozer|1,96E-02|kg/h|0%|15.840|990|16.830|h|0,31|0,02|0,33|
|**PE**|Maquinaria fuera de<br>ruta|Retroexcavadora|1,73E-02|kg/h|0%|16.830|8.910|25.740|h|0,29|0,15|0,44|
|**PE**|Maquinaria fuera de<br>ruta|Grúa de apoyo|1,84E-02|kg/h|0%|0|1.078|1.078|h|0,00|0,02|0,02|
|**PE**|Maquinaria fuera de<br>ruta|Grúa principal|5,54E-02|kg/h|0%|0|924|924|h|0,00|0,05|0,05|
|**LT**|Maquinaria fuera de<br>ruta|Motoniveladora|2,31E-02|kg/h|0%|3.168|7.128|10.296|h|0,07|0,16|0,24|
|**LT**|Maquinaria fuera de<br>ruta|Compactadora|5,71E-02|kg/h|0%|2.376|5.346|7.722|h|0,14|0,31|0,44|
|**LT**|Maquinaria fuera de<br>ruta|Bulldozer|1,96E-02|kg/h|0%|3.960|9.900|13.860|h|0,08|0,19|0,27|
|**LT**|Maquinaria fuera de<br>ruta|Retroexcavadora|1,73E-02|kg/h|0%|3.960|9.900|13.860|h|0,07|0,17|0,24|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 81

|Sector|Actividad<br>Grúa de apoyo<br>Grúa principal|Col3|Factor Emisión|Col5|Eficiencia<br>Mitigación|Nivel de Actividad|Col8|Col9|Col10|Emisión MP2,5 (t/año)|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Sector**|**Actividad**<br>Grúa de apoyo<br>Grúa principal|**Actividad**<br>Grúa de apoyo<br>Grúa principal|**Valor**|**Unidad**|**Unidad**|**Año 1**|**Año 2**|**Total**|**Unidad**|**Año 1**|**Año 2**|**Total**|
|**Sector**|**Actividad**<br>Grúa de apoyo<br>Grúa principal|Grúa de apoyo|1,84E-02|kg/h|0%|0|616|616|h|0,00|0,01|0,01|
|**Sector**|**Actividad**<br>Grúa de apoyo<br>Grúa principal|Grúa principal|5,54E-02|kg/h|0%|0|528|528|h|0,00|0,03|0,03|
|**PE**|Resuspensión camino<br>No Pavimentado<br>Externo - Ruta N-<br>85;SR/-861 (SS)|Camión rígido + 2 ejes|3,87E-02|kg/VKT|0%|409|1.027|1.435|km|0,02|0,04|0,06|
|**PE**|Resuspensión camino<br>No Pavimentado<br>Externo - Ruta N-<br>85;SR/-861 (SS)|Camión Semiremolque|4,47E-02|kg/VKT|0%|76.123|24.641|100.764|km|3,40|1,10|4,50|
|**PE**|Resuspensión camino<br>No Pavimentado<br>Externo - Ruta N-<br>85;SR/-861 (SS)|liviano|1,51E-02|kg/VKT|0%|29.307|29.891|59.197|km|0,44|0,45|0,89|
|**PE**|Resuspensión camino<br>No Pavimentado<br>Externo - Ruta N-<br>85;SR/-861 (SS)|Sobredimensionado|5,13E-02|kg/VKT|0%|0|341|341|km|0,00|0,02|0,02|
|**PE**|Resuspensión camino<br>No Pavimentado<br>Interno (SS)|Camión rígido + 2 ejes|3,87E-02|kg/VKT|0%|16.465|17.077|33.543|km|0,64|0,66|1,30|
|**PE**|Resuspensión camino<br>No Pavimentado<br>Interno (SS)|Camión Semiremolque|4,47E-02|kg/VKT|0%|114.865|36.572|151.437|km|5,13|1,63|6,77|
|**PE**|Resuspensión camino<br>No Pavimentado<br>Interno (SS)|liviano|1,51E-02|kg/VKT|0%|27.536|28.105|55.640|km|0,41|0,42|0,84|
|**PE**|Resuspensión camino<br>No Pavimentado<br>Interno (SS)|Sobredimensionado|5,13E-02|kg/VKT|0%|0|332|332|km|0,00|0,02|0,02|
|**PE**|Resuspensión camino<br>Pavimentado Externo -<br>Ruta N-85;SR/-861|Camión rígido + 2 ejes|7,91E-04|kg/VKT|0%|1.907|4.790|6.697|km|0,00|0,00|0,01|
|**PE**|Resuspensión camino<br>Pavimentado Externo -<br>Ruta N-85;SR/-861|Camión Semiremolque|1,09E-03|kg/VKT|0%|355.187|114.976|470.162|km|0,39|0,13|0,51|
|**PE**|Resuspensión camino<br>Pavimentado Externo -<br>Ruta N-85;SR/-861|liviano|9,30E-05|kg/VKT|0%|136.745|139.469|276.214|km|0,01|0,01|0,03|
|**PE**|Resuspensión camino<br>Pavimentado Externo -<br>Ruta N-85;SR/-861|Sobredimensionado|1,49E-03|kg/VKT|0%|0|1.589|1.589|km|0,00|0,00|0,00|
|**PE**|Resuspensión camino<br>Pavimentado Externo -<br>Ruta 5-152|Camión rígido + 2 ejes|7,91E-04|kg/VKT|0%|9.492|23.843|33.335|km|0,01|0,02|0,03|
|**PE**|Resuspensión camino<br>Pavimentado Externo -<br>Ruta 5-152|Camión Semiremolque|1,09E-03|kg/VKT|0%|1.768.111|572.345|2.340.456|km|1,93|0,63|2,56|
|**PE**|Resuspensión camino<br>Pavimentado Externo -<br>Ruta 5-152|liviano|9,30E-05|kg/VKT|0%|680.712|694.272|1.374.984|km|0,06|0,06|0,13|
|**PE**|Resuspensión camino<br>Pavimentado Externo -<br>Ruta 5-152|Sobredimensionado|1,49E-03|kg/VKT|0%|0|7.910|7.910|km|0,00|0,01|0,01|
|**LT**|Resusp. No<br>Pavimentado Externo -<br>Ruta N-85;SR-857 (SS)|Camión Semiremolque|4,47E-02|kg/VKT|0%|0|526|526|km|0,00|0,02|0,02|
|**LT**|Resusp. Pavimentado<br>Externo - Ruta N-<br>85;SR-857|Camión Semiremolque|1,09E-03|kg/VKT|0%|0|3.198|3.198|km|0,00|0,00|0,00|
|**LT**|Resusp. Pavimentado<br>Externo - Ruta 5-152|Camión Semiremolque|1,09E-03|kg/VKT|0%|0|22.035|22.035|km|0,00|0,02|0,02|
|**PE**|Resuspensión camino<br>No Pavimentado<br>Externo - Ruta N-<br>85;SR/-861 (CS)|Camión rígido + 2 ejes|3,87E-02|kg/VKT|90%|205|514|718|km|0,00|0,00|0,00|
|**PE**|Resuspensión camino<br>No Pavimentado<br>Externo - Ruta N-<br>85;SR/-861 (CS)|Camión Semiremolque|4,47E-02|kg/VKT|90%|38.100|12.333|50.434|km|0,17|0,06|0,23|
|**PE**|Resuspensión camino<br>No Pavimentado<br>Externo - Ruta N-<br>85;SR/-861 (CS)|liviano|1,51E-02|kg/VKT|90%|14.668|14.961|29.629|km|0,02|0,02|0,04|
|**PE**|Resuspensión camino<br>No Pavimentado<br>Externo - Ruta N-<br>85;SR/-861 (CS)|Sobredimensionado|5,13E-02|kg/VKT|90%|0|170|170|km|0,00|0,00|0,00|
|**PE**|Resuspensión camino<br>No Pavimentado<br>Interno (CS)|Camión rígido + 2 ejes|3,87E-02|kg/VKT|90%|1.351|1.401|2.752|km|0,01|0,01|0,01|
|**PE**|Resuspensión camino<br>No Pavimentado<br>Interno (CS)|Camión Semiremolque|4,47E-02|kg/VKT|90%|9.425|3.001|12.425|km|0,04|0,01|0,06|
|**PE**|Resuspensión camino<br>No Pavimentado<br>Interno (CS)|liviano|1,51E-02|kg/VKT|90%|2.259|2.306|4.565|km|0,00|0,00|0,01|
|**PE**|Resuspensión camino<br>No Pavimentado<br>Interno (CS)|Sobredimensionado|5,13E-02|kg/VKT|90%|0|27|27|km|0,00|0,00|0,00|
|**LT**|Resusp. No<br>Pavimentado Externo -<br>Ruta N-85;SR-857 (CS)|Camión Semiremolque|4,47E-02|kg/VKT|90%|0|79|79|km|0,00|0,00|0,00|
|**PE**|Combustión vehículos<br>Pavimentado|Camión rígido + 2 ejes|8,82E-04|kg/VKT|0%|1.907|4.790|6.697|km|0,00|0,00|0,01|
|**PE**|Combustión vehículos<br>Pavimentado|Camión Semiremolque|8,82E-04|kg/VKT|0%|355.187|114.976|470.162|km|0,31|0,10|0,41|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 82

|Sector|Actividad<br>liviano<br>Sobredimensionado|Col3|Factor Emisión|Col5|Eficiencia<br>Mitigación|Nivel de Actividad|Col8|Col9|Col10|Emisión MP2,5 (t/año)|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Sector**|**Actividad**<br>liviano<br>Sobredimensionado|**Actividad**<br>liviano<br>Sobredimensionado|**Valor**|**Unidad**|**Unidad**|**Año 1**|**Año 2**|**Total**|**Unidad**|**Año 1**|**Año 2**|**Total**|
|**Sector**|**Actividad**<br>liviano<br>Sobredimensionado|liviano|6,06E-05|kg/VKT|0%|136.745|139.469|276.214|km|0,01|0,01|0,02|
|**Sector**|**Actividad**<br>liviano<br>Sobredimensionado|Sobredimensionado|6,57E-04|kg/VKT|0%|0|1.589|1.589|km|0,00|0,00|0,00|
|**PE**|Combustión vehículos<br>No Pavimentado|Camión rígido + 2 ejes|7,02E-04|kg/VKT|0%|18.430|20.019|38.448|km|0,01|0,01|0,03|
|**PE**|Combustión vehículos<br>No Pavimentado|Camión Semiremolque|7,02E-04|kg/VKT|0%|238.513|76.547|315.060|km|0,17|0,05|0,22|
|**PE**|Combustión vehículos<br>No Pavimentado|liviano|4,68E-05|kg/VKT|0%|73.770|75.262|149.032|km|0,00|0,00|0,01|
|**PE**|Combustión vehículos<br>No Pavimentado|Sobredimensionado|6,57E-04|kg/VKT|0%|0|870|870|km|0,00|0,00|0,00|
|**LT**|Combustión vehículos<br>Pavimentado|Camión rígido + 2 ejes|8,82E-04|kg/VKT|0%|0|0|0|km|0,00|0,00|0,00|
|**LT**|Combustión vehículos<br>Pavimentado|Camión Semiremolque|8,82E-04|kg/VKT|0%|0|3.198|3.198|km|0,00|0,00|0,00|
|**LT**|Combustión vehículos<br>Pavimentado|liviano|6,06E-05|kg/VKT|0%|0|0|0|km|0,00|0,00|0,00|
|**LT**|Combustión vehículos<br>Pavimentado|Sobredimensionado|6,57E-04|kg/VKT|0%|0|0|0|km|0,00|0,00|0,00|
|**LT**|Combustión vehículos<br>No Pavimentado|Camión rígido + 2 ejes|7,02E-04|kg/VKT|0%|0|0|0|km|0,00|0,00|0,00|
|**LT**|Combustión vehículos<br>No Pavimentado|Camión Semiremolque|7,02E-04|kg/VKT|0%|0|605|605|km|0,00|0,00|0,00|
|**LT**|Combustión vehículos<br>No Pavimentado|liviano|4,68E-05|kg/VKT|0%|0|0|0|km|0,00|0,00|0,00|
|**LT**|Combustión vehículos<br>No Pavimentado|Sobredimensionado|6,57E-04|kg/VKT|0%|0|0|0|km|0,00|0,00|0,00|
|**PE**|Combustión vehículos<br>Pavimentado Ruta 5-<br>182|Camión rígido + 2 ejes|8,82E-04|kg/VKT|0%|9.492|23.843|33.335|km|0,01|0,02|0,03|
|**PE**|Combustión vehículos<br>Pavimentado Ruta 5-<br>182|Camión Semiremolque|8,82E-04|kg/VKT|0%|1.768.111|594.380|2.340.456|km|1,56|0,52|2,06|
|**PE**|Combustión vehículos<br>Pavimentado Ruta 5-<br>182|liviano|6,06E-05|kg/VKT|0%|680.712|694.272|1.374.984|km|0,04|0,04|0,08|
|**PE**|Combustión vehículos<br>Pavimentado Ruta 5-<br>182|Sobredimensionado|6,57E-04|kg/VKT|0%|0|7.910|7.910|km|0,00|0,01|0,01|
|**LT**|**LT**|Camión Semiremolque|8,82E-04|kg/VKT|0%|0|22.035|22.035|km|0,00|0,02|0,02|
|**LT**|Erosión Eólica|Acopio|15,3|kg/ha/año|0%|1,01|1,01|1,01|ha|0,02|0,02|0,02|
|**PE**|Grupos electrógenos|Instalación de faenas|6,08E-03|kg/kg comb.|0%|104.180|104.180|208.361|kg comb.|0,63|0,63|1,27|
|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**20,00**|**11,82**|**31,78**|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 83

**Tabla 58.** Emisiones de MPS debido a las actividades de la fase de Construcción del Proyecto Parque Eólico Dañicalqui, Sectores Parque

Eólico (PE) y Línea de Transmisión (LT).

|Sector|Actividad|Col3|Factor Emisión|Col5|Eficiencia<br>Mitigación|Nivel de Actividad|Col8|Col9|Col10|Emisión MPS (t/año)|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Sector**|**Actividad**|**Actividad**|**Valor**|**Unidad**|**Unidad**|**Año 1**|**Año 2**|**Total**|**Unidad**|**Año 1**|**Año 2**|**Total**|
|**PE**|Excavaciones -<br>preparación de<br>terreno|Plataformas y caminos|3,83E+00|kg/h|0%|5.219|7.268|12.487|h|20,01|27,86|47,87|
|**PE**|Excavaciones -<br>preparación de<br>terreno|Aerogeneradores|3,83E+00|kg/h|0%|755|1.052|1.807|h|2,90|4,03|6,93|
|**PE**|Excavaciones -<br>preparación de<br>terreno|Puentes y obras de arte: Puente río<br>Dañicalqui|3,83E+00|kg/h|0%|11|15|27|h|0,04|0,06|0,10|
|**PE**|Excavaciones -<br>preparación de<br>terreno|Puentes y obras de arte: Puente<br>estero Culenco|3,83E+00|kg/h|0%|1|2|4|h|0,01|0,01|0,01|
|**PE**|Excavaciones -<br>preparación de<br>terreno|Puentes y obras de arte: Puente<br>Canales|3,83E+00|kg/h|0%|2|3|5|h|0,01|0,01|0,02|
|**PE**|Excavaciones -<br>preparación de<br>terreno|Puentes y obras de arte: Obras de<br>Arte|3,83E+00|kg/h|0%|3|3|6|h|0,01|0,01|0,02|
|**PE**|Excavaciones -<br>preparación de<br>terreno|Circuiros MT|3,83E+00|kg/h|0%|81|113|193|h|0,31|0,43|0,74|
|**LT**|**LT**|Línea de Transmisión|3,83E+00|kg/h|0%|35|49|84|h|0,13|0,19|0,32|
|**PE**|Carga|Plataformas y caminos|6,61E-04|kg/t|0%|252.098|351.023|603.121|t|0,17|0,23|0,40|
|**PE**|Carga|Aerogeneradores|6,61E-04|kg/t|0%|36.486|50.804|87.290|t|0,02|0,03|0,06|
|**PE**|Carga|Puentes y obras de arte: Puente río<br>Dañicalqui|6,61E-04|kg/t|0%|536|747|1.283|t|0,00|0,00|0,00|
|**PE**|Carga|Puentes y obras de arte: Puente<br>estero Culenco|6,61E-04|kg/t|0%|71|98|169|t|0,00|0,00|0,00|
|**PE**|Carga|Puentes y obras de arte: Puente<br>Canales|6,61E-04|kg/t|0%|94|131|225|t|0,00|0,00|0,00|
|**PE**|Carga|Puentes y obras de arte: Obras de<br>Arte|6,61E-04|kg/t|0%|121|169|290|t|0,00|0,00|0,00|
|**PE**|Carga|Circuiros MT|6,61E-04|kg/t|0%|3.904|5.436|9.340|t|0,00|0,00|0,01|
|**PE**|Carga|Material de escarpe|6,61E-04|kg/t|0%|21.548|30.004|51.553|t|0,01|0,02|0,03|
|**LT**|**LT**|Línea de Transmisión|6,61E-04|kg/t|0%|1.696|2.362|4.058|t|0,00|0,00|0,00|
|**PE**|Descarga|Plataformas y caminos|6,61E-04|kg/t|0%|155.301|216.242|371.543|t|0,10|0,14|0,25|
|**PE**|Descarga|Aerogeneradores|6,61E-04|kg/t|0%|9.861|13.731|23.592|t|0,01|0,01|0,02|
|**PE**|Descarga|Puentes y obras de arte: Puente río<br>Dañicalqui|6,61E-04|kg/t|0%|578|806|1.384|t|0,00|0,00|0,00|
|**PE**|Descarga|Puentes y obras de arte: Puente<br>estero Culenco|6,61E-04|kg/t|0%|53|74|128|t|0,00|0,00|0,00|
|**PE**|Descarga|Puentes y obras de arte: Puente<br>Canales|6,61E-04|kg/t|0%|71|99|170|t|0,00|0,00|0,00|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 84

|Sector|Actividad<br>Puentes y obras de arte: Obras de<br>Arte<br>Material de escarpe<br>Línea de Transmisión|Col3|Factor Emisión|Col5|Eficiencia<br>Mitigación|Nivel de Actividad|Col8|Col9|Col10|Emisión MPS (t/año)|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Sector**|**Actividad**<br>Puentes y obras de arte: Obras de<br>Arte<br>Material de escarpe<br>Línea de Transmisión|**Actividad**<br>Puentes y obras de arte: Obras de<br>Arte<br>Material de escarpe<br>Línea de Transmisión|**Valor**|**Unidad**|**Unidad**|**Año 1**|**Año 2**|**Total**|**Unidad**|**Año 1**|**Año 2**|**Total**|
|**Sector**|**Actividad**<br>Puentes y obras de arte: Obras de<br>Arte<br>Material de escarpe<br>Línea de Transmisión|Puentes y obras de arte: Obras de<br>Arte|6,61E-04|kg/t|0%|80|112|192|t|0,00|0,00|0,00|
|**Sector**|**Actividad**<br>Puentes y obras de arte: Obras de<br>Arte<br>Material de escarpe<br>Línea de Transmisión|Material de escarpe|6,61E-04|kg/t|0%|21.548|30.004|51.553|t|0,01|0,02|0,03|
|**LT**|**LT**|Línea de Transmisión|6,61E-04|kg/t|0%|1.515|2.109|3.624|t|0,00|0,00|0,00|
|**PE**|Compactación|Plataformas|3,83E+00|kg/h|0%|7|10|16|h|0,03|0,04|0,06|
|**PE**|Compactación|Subestación|3,83E+00|kg/h|0%|0|1|1|h|0,00|0,00|0,00|
|**PE**|Compactación|Caminos|3,83E+00|kg/h|0%|6|8|14|h|0,02|0,03|0,05|
|**PE**|Compactación|Instalación de faenas|3,83E+00|kg/h|0%|2|2|4|h|0,01|0,01|0,01|
|**PE**|Compactación|Planta de Hormigón|3,83E+00|kg/h|0%|1|1|2|h|0,00|0,00|0,01|
|**PE**|Compactación|Plataforma Acopio de Aspas|3,83E+00|kg/h|0%|2|3|6|h|0,01|0,01|0,02|
|**PE**|Compactación|Terraplén y corte|3,83E+00|kg/h|0%|7|10|17|h|0,03|0,04|0,06|
|**LT**|**LT**|Zona de acopio LT|3,83E+00|kg/h|0%|1|1|2|h|0,00|0,00|0,01|
|**PE**|Escarpe|Plataformas|5,70E+00|kg/km|0%|12|17|28|km|0,07|0,09|0,16|
|**PE**|Escarpe|Subestación|5,70E+00|kg/km|0%|1|1|2|km|0,00|0,01|0,01|
|**PE**|Escarpe|Caminos|5,70E+00|kg/km|0%|10|14|25|km|0,06|0,08|0,14|
|**PE**|Escarpe|Instalación de faenas|5,70E+00|kg/km|0%|3|4|6|km|0,02|0,02|0,04|
|**PE**|Escarpe|Planta de Hormigón|5,70E+00|kg/km|0%|2|2|4|km|0,01|0,01|0,02|
|**PE**|Escarpe|Plataforma Acopio de Aspas|5,70E+00|kg/km|0%|4|6|10|km|0,02|0,03|0,06|
|**PE**|Escarpe|Terraplén y corte|5,70E+00|kg/km|0%|12|17|29|km|0,07|0,10|0,16|
|**LT**|**LT**|Zona de acopio LT|5,70E+00|kg/km|0%|2|2|4|km|0,01|0,01|0,02|
|**PE**|Maquinaria fuera de<br>ruta|Motoniveladora|2,31E-02|kg/h|0%|12.672|792|13.464|h|0,29|0,02|0,31|
|**PE**|Maquinaria fuera de<br>ruta|Compactadora|5,71E-02|kg/h|0%|9.504|594|10.098|h|0,54|0,03|0,58|
|**PE**|Maquinaria fuera de<br>ruta|Bulldozer|1,96E-02|kg/h|0%|15.840|990|16.830|h|0,31|0,02|0,33|
|**PE**|Maquinaria fuera de<br>ruta|Retroexcavadora|1,73E-02|kg/h|0%|16.830|8.910|25.740|h|0,29|0,15|0,44|
|**PE**|Maquinaria fuera de<br>ruta|Grúa de apoyo|1,84E-02|kg/h|0%|0|1.078|1.078|h|0,00|0,02|0,02|
|**PE**|Maquinaria fuera de<br>ruta|Grúa principal|5,54E-02|kg/h|0%|0|924|924|h|0,00|0,05|0,05|
|**LT**|Maquinaria fuera de<br>ruta|Motoniveladora|2,31E-02|kg/h|0%|3.168|7.128|10.296|h|0,07|0,16|0,24|
|**LT**|Maquinaria fuera de<br>ruta|Compactadora|5,71E-02|kg/h|0%|2.376|5.346|7.722|h|0,14|0,31|0,44|
|**LT**|Maquinaria fuera de<br>ruta|Bulldozer|1,96E-02|kg/h|0%|3.960|9.900|13.860|h|0,08|0,19|0,27|
|**LT**|Maquinaria fuera de<br>ruta|Retroexcavadora|1,73E-02|kg/h|0%|3.960|9.900|13.860|h|0,07|0,17|0,24|
|**LT**|Maquinaria fuera de<br>ruta|Grúa de apoyo|1,84E-02|kg/h|0%|0|616|616|h|0,00|0,01|0,01|
|**LT**|Maquinaria fuera de<br>ruta|Grúa principal|5,54E-02|kg/h|0%|0|528|528|h|0,00|0,03|0,03|
|**PE**|Resuspensión camino<br>No Pavimentado<br>Externo - Ruta N-<br>85;SR/-861 (SS)|Camión rígido + 2 ejes|1,27E+00|kg/VKT|0%|409|1.027|1.435|km|0,52|1,30|1,82|
|**PE**|Resuspensión camino<br>No Pavimentado<br>Externo - Ruta N-<br>85;SR/-861 (SS)|Camión Semiremolque|1,46E+00|kg/VKT|0%|76.123|24.641|100.764|km|111,11|35,97|147,07|
|**PE**|Resuspensión camino<br>No Pavimentado<br>Externo - Ruta N-<br>85;SR/-861 (SS)|liviano|4,92E-01|kg/VKT|0%|29.307|29.891|59.197|km|14,42|14,71|29,13|
|**PE**|Resuspensión camino<br>No Pavimentado<br>Externo - Ruta N-<br>85;SR/-861 (SS)|Sobredimensionado|1,67E+00|kg/VKT|0%|0|341|341|km|0,00|0,57|0,57|
|**PE**||Camión rígido + 2 ejes|1,27E+00|kg/VKT|0%|16.465|17.077|33.543|km|20,84|21,62|42,46|
|**PE**||Camión Semiremolque|1,46E+00|kg/VKT|0%|114.865|36.572|151.437|km|167,66|53,38|221,04|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 85

|Sector|Actividad<br>Resuspensión camino liviano<br>No Pavimentado<br>Sobredimensionado<br>Interno (SS)|Col3|Factor Emisión|Col5|Eficiencia<br>Mitigación|Nivel de Actividad|Col8|Col9|Col10|Emisión MPS (t/año)|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Sector**|**Actividad**<br>Resuspensión camino<br>No Pavimentado<br>Interno (SS)<br>liviano<br>Sobredimensionado|**Actividad**<br>Resuspensión camino<br>No Pavimentado<br>Interno (SS)<br>liviano<br>Sobredimensionado|**Valor**|**Unidad**|**Unidad**|**Año 1**|**Año 2**|**Total**|**Unidad**|**Año 1**|**Año 2**|**Total**|
|**Sector**|**Actividad**<br>Resuspensión camino<br>No Pavimentado<br>Interno (SS)<br>liviano<br>Sobredimensionado|liviano|4,92E-01|kg/VKT|0%|27.536|28.105|55.640|km|13,55|13,83|27,38|
|**Sector**|**Actividad**<br>Resuspensión camino<br>No Pavimentado<br>Interno (SS)<br>liviano<br>Sobredimensionado|Sobredimensionado|1,67E+00|kg/VKT|0%|0|332|332|km|0,00|0,56|0,56|
|**Sector**|Resuspensión camino<br>Pavimentado Externo -<br>Ruta N-85;SR/-861|Camión rígido + 2 ejes|1,70E-02|kg/VKT|0%|1.907|4.790|6.697|km|0,03|0,08|0,11|
|**Sector**|Resuspensión camino<br>Pavimentado Externo -<br>Ruta N-85;SR/-861|Camión Semiremolque|2,35E-02|kg/VKT|0%|355.187|114.976|470.162|km|8,36|2,71|11,06|
|**Sector**|Resuspensión camino<br>Pavimentado Externo -<br>Ruta N-85;SR/-861|liviano|2,00E-03|kg/VKT|0%|136.745|139.469|276.214|km|0,27|0,28|0,55|
|**Sector**|Resuspensión camino<br>Pavimentado Externo -<br>Ruta N-85;SR/-861|Sobredimensionado|3,21E-02|kg/VKT|0%|0|1.589|1.589|km|0,00|0,05|0,05|
|**Sector**|Resuspensión camino<br>Pavimentado Externo -<br>Ruta 5-152|Camión rígido + 2 ejes|1,70E-02|kg/VKT|0%|9.492|23.843|33.335|km|0,16|0,41|0,57|
|**Sector**|Resuspensión camino<br>Pavimentado Externo -<br>Ruta 5-152|Camión Semiremolque|2,35E-02|kg/VKT|0%|1.768.111|572.345|2.340.456|km|41,61|13,47|55,08|
|**Sector**|Resuspensión camino<br>Pavimentado Externo -<br>Ruta 5-152|liviano|2,00E-03|kg/VKT|0%|680.712|694.272|1.374.984|km|1,36|1,39|2,75|
|**Sector**|Resuspensión camino<br>Pavimentado Externo -<br>Ruta 5-152|Sobredimensionado|3,21E-02|kg/VKT|0%|0|7.910|7.910|km|0,00|0,25|0,25|
|**LT**|Resusp. No<br>Pavimentado Externo -<br>Ruta N-85;SR-857 (SS)|Camión Semiremolque|1,46E+00|kg/VKT|0%|0|526|526|km|0,00|0,77|0,77|
|**LT**|Resusp. Pavimentado<br>Externo - Ruta N-<br>85;SR-857|Camión Semiremolque|2,35E-02|kg/VKT|0%|0|3.198|3.198|km|0,00|0,08|0,08|
|**LT**|Resusp. Pavimentado<br>Externo - Ruta 5-152|Camión Semiremolque|2,35E-02|kg/VKT|0%|0|22.035|22.035|km|0,00|0,52|0,52|
|**PE**|Resuspensión camino<br>No Pavimentado<br>Externo - Ruta N-<br>85;SR/-861 (CS)|Camión rígido + 2 ejes|1,27E+00|kg/VKT|90%|205|514|718|km|0,03|0,07|0,09|
|**PE**|Resuspensión camino<br>No Pavimentado<br>Externo - Ruta N-<br>85;SR/-861 (CS)|Camión Semiremolque|1,46E+00|kg/VKT|90%|38.100|12.333|50.434|km|5,56|1,80|7,36|
|**PE**|Resuspensión camino<br>No Pavimentado<br>Externo - Ruta N-<br>85;SR/-861 (CS)|liviano|4,92E-01|kg/VKT|90%|14.668|14.961|29.629|km|0,72|0,74|1,46|
|**PE**|Resuspensión camino<br>No Pavimentado<br>Externo - Ruta N-<br>85;SR/-861 (CS)|Sobredimensionado|1,67E+00|kg/VKT|90%|0|170|170|km|0,00|0,03|0,03|
|**PE**|Resuspensión camino<br>No Pavimentado<br>Interno (CS)|Camión rígido + 2 ejes|1,27E+00|kg/VKT|90%|1.351|1.401|2.752|km|0,17|0,18|0,35|
|**PE**|Resuspensión camino<br>No Pavimentado<br>Interno (CS)|Camión Semiremolque|1,46E+00|kg/VKT|90%|9.425|3.001|12.425|km|1,38|0,44|1,81|
|**PE**|Resuspensión camino<br>No Pavimentado<br>Interno (CS)|liviano|4,92E-01|kg/VKT|90%|2.259|2.306|4.565|km|0,11|0,11|0,22|
|**PE**|Resuspensión camino<br>No Pavimentado<br>Interno (CS)|Sobredimensionado|1,67E+00|kg/VKT|90%|0|27|27|km|0,00|0,00|0,00|
|**LT**|Resusp. No<br>Pavimentado Externo -<br>Ruta N-85;SR-857 (CS)|Camión Semiremolque|1,46E+00|kg/VKT|90%|0|79|79|km|0,00|0,01|0,01|
|**PE**|Combustión vehículos<br>Pavimentado|Camión rígido + 2 ejes|8,82E-04|kg/VKT|0%|1.907|4.790|6.697|km|0,00|0,00|0,01|
|**PE**|Combustión vehículos<br>Pavimentado|Camión Semiremolque|8,82E-04|kg/VKT|0%|355.187|114.976|470.162|km|0,31|0,10|0,41|
|**PE**|Combustión vehículos<br>Pavimentado|liviano|6,06E-05|kg/VKT|0%|136.745|139.469|276.214|km|0,01|0,01|0,02|
|**PE**|Combustión vehículos<br>Pavimentado|Sobredimensionado|6,57E-04|kg/VKT|0%|0|1.589|1.589|km|0,00|0,00|0,00|
|**PE**|Combustión vehículos<br>No Pavimentado|Camión rígido + 2 ejes|7,02E-04|kg/VKT|0%|18.430|20.019|38.448|km|0,01|0,01|0,03|
|**PE**|Combustión vehículos<br>No Pavimentado|Camión Semiremolque|7,02E-04|kg/VKT|0%|238.513|76.547|315.060|km|0,17|0,05|0,22|
|**PE**|Combustión vehículos<br>No Pavimentado|liviano|4,68E-05|kg/VKT|0%|73.770|75.262|149.032|km|0,00|0,00|0,01|
|**PE**|Combustión vehículos<br>No Pavimentado|Sobredimensionado|6,57E-04|kg/VKT|0%|0|870|870|km|0,00|0,00|0,00|
|**LT**||Camión rígido + 2 ejes|8,82E-04|kg/VKT|0%|0|0|0|km|0,00|0,00|0,00|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 86

|Sector|Actividad<br>Camión Semiremolque<br>Combustión vehículos<br>liviano<br>Pavimentado<br>Sobredimensionado|Col3|Factor Emisión|Col5|Eficiencia<br>Mitigación|Nivel de Actividad|Col8|Col9|Col10|Emisión MPS (t/año)|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Sector**|**Actividad**<br>Combustión vehículos<br>Pavimentado<br>Camión Semiremolque<br>liviano<br>Sobredimensionado|**Actividad**<br>Combustión vehículos<br>Pavimentado<br>Camión Semiremolque<br>liviano<br>Sobredimensionado|**Valor**|**Unidad**|**Unidad**|**Año 1**|**Año 2**|**Total**|**Unidad**|**Año 1**|**Año 2**|**Total**|
|**Sector**|**Actividad**<br>Combustión vehículos<br>Pavimentado<br>Camión Semiremolque<br>liviano<br>Sobredimensionado|Camión Semiremolque|8,82E-04|kg/VKT|0%|0|3.198|3.198|km|0,00|0,00|0,00|
|**Sector**|**Actividad**<br>Combustión vehículos<br>Pavimentado<br>Camión Semiremolque<br>liviano<br>Sobredimensionado|liviano|6,06E-05|kg/VKT|0%|0|0|0|km|0,00|0,00|0,00|
|**Sector**|**Actividad**<br>Combustión vehículos<br>Pavimentado<br>Camión Semiremolque<br>liviano<br>Sobredimensionado|Sobredimensionado|6,57E-04|kg/VKT|0%|0|0|0|km|0,00|0,00|0,00|
|**LT**|Combustión vehículos<br>No Pavimentado|Camión rígido + 2 ejes|7,02E-04|kg/VKT|0%|0|0|0|km|0,00|0,00|0,00|
|**LT**|Combustión vehículos<br>No Pavimentado|Camión Semiremolque|7,02E-04|kg/VKT|0%|0|605|605|km|0,00|0,00|0,00|
|**LT**|Combustión vehículos<br>No Pavimentado|liviano|4,68E-05|kg/VKT|0%|0|0|0|km|0,00|0,00|0,00|
|**LT**|Combustión vehículos<br>No Pavimentado|Sobredimensionado|6,57E-04|kg/VKT|0%|0|0|0|km|0,00|0,00|0,00|
|**PE**|Combustión vehículos<br>Pavimentado Ruta 5-<br>182|Camión rígido + 2 ejes|8,82E-04|kg/VKT|0%|9.492|23.843|33.335|km|0,01|0,02|0,03|
|**PE**|Combustión vehículos<br>Pavimentado Ruta 5-<br>182|Camión Semiremolque|8,82E-04|kg/VKT|0%|1.768.111|594.380|2.340.456|km|1,56|0,52|2,06|
|**PE**|Combustión vehículos<br>Pavimentado Ruta 5-<br>182|liviano|6,06E-05|kg/VKT|0%|680.712|694.272|1.374.984|km|0,04|0,04|0,08|
|**PE**|Combustión vehículos<br>Pavimentado Ruta 5-<br>182|Sobredimensionado|6,57E-04|kg/VKT|0%|0|7.910|7.910|km|0,00|0,01|0,01|
|**LT**|**LT**|Camión Semiremolque|8,82E-04|kg/VKT|0%|0|22.035|22.035|km|0,00|0,02|0,02|
|**LT**|Erosión Eólica|Acopio|15,3|kg/ha/año|0%|1,01|1,01|1,01|ha|0,02|0,02|0,02|
|**PE**|Grupos electrógenos|Instalación de faenas|6,08E-03|kg/kg comb.|0%|104.180|104.180|208.361|kg comb.|0,63|0,63|1,27|
|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**416,52**|**201,49**|**617,97**|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 87

**Tabla 59.** Emisiones de NOx debido a las actividades de la fase de Construcción del Proyecto Parque Eólico Dañicalqui, Sectores Parque

Eólico (PE) y Línea de Transmisión (LT).

|Sector|Actividad|Col3|Factor Emisión|Col5|Eficiencia<br>Mitigación|Nivel de Actividad|Col8|Col9|Col10|Emisión NOx (t/año)|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Sector**|**Actividad**|**Actividad**|**Valor**|**Unidad**|**Unidad**|**Año 1**|**Año 2**|**Total**|**Unidad**|**Año 1**|**Año 2**|**Total**|
|**PE**|Maquinaria fuera de<br>ruta|Motoniveladora|3,77E-01|kg/h|0%|12.672|792|13.464|h|4,78|0,30|5,08|
|**PE**|Maquinaria fuera de<br>ruta|Compactadora|2,79E+00|kg/h|0%|9.504|594|10.098|h|26,49|1,66|28,14|
|**PE**|Maquinaria fuera de<br>ruta|Bulldozer|6,39E-01|kg/h|0%|15.840|990|16.830|h|10,12|0,63|10,76|
|**PE**|Maquinaria fuera de<br>ruta|Retroexcavadora|2,98E-01|kg/h|0%|16.830|8.910|25.740|h|5,02|2,66|7,67|
|**PE**|Maquinaria fuera de<br>ruta|Grúa de apoyo|5,99E-01|kg/h|0%|0|1.078|1.078|h|0,00|0,65|0,65|
|**PE**|Maquinaria fuera de<br>ruta|Grúa principal|1,81E+00|kg/h|0%|0|924|924|h|0,00|1,67|1,67|
|**LT**|Maquinaria fuera de<br>ruta|Motoniveladora|3,77E-01|kg/h|0%|3.168|7.128|10.296|h|1,19|2,69|3,88|
|**LT**|Maquinaria fuera de<br>ruta|Compactadora|2,79E+00|kg/h|0%|2.376|5.346|7.722|h|6,62|14,90|21,52|
|**LT**|Maquinaria fuera de<br>ruta|Bulldozer|6,39E-01|kg/h|0%|3.960|9.900|13.860|h|2,53|6,33|8,86|
|**LT**|Maquinaria fuera de<br>ruta|Retroexcavadora|2,98E-01|kg/h|0%|3.960|9.900|13.860|h|1,18|2,95|4,13|
|**LT**|Maquinaria fuera de<br>ruta|Grúa de apoyo|5,99E-01|kg/h|0%|0|616|616|h|0,00|0,37|0,37|
|**LT**|Maquinaria fuera de<br>ruta|Grúa principal|1,81E+00|kg/h|0%|0|528|528|h|0,00|0,95|0,95|
|**PE**|Combustión vehículos<br>Pavimentado|Camión rígido + 2 ejes|7,56E-03|kg/VKT|0%|1.907|4.790|6.697|km|0,01|0,04|0,05|
|**PE**|Combustión vehículos<br>Pavimentado|Camión Semiremolque|7,56E-03|kg/VKT|0%|355.187|114.976|470.162|km|2,69|0,87|3,56|
|**PE**|Combustión vehículos<br>Pavimentado|liviano|8,59E-04|kg/VKT|0%|136.745|139.469|276.214|km|0,12|0,12|0,24|
|**PE**|Combustión vehículos<br>Pavimentado|Sobredimensionado|1,11E-02|kg/VKT|0%|0|1.589|1.589|km|0,00|0,02|0,02|
|**PE**|Combustión vehículos<br>No Pavimentado|Camión rígido + 2 ejes|9,63E-03|kg/VKT|0%|18.430|20.019|38.448|km|0,18|0,19|0,37|
|**PE**|Combustión vehículos<br>No Pavimentado|Camión Semiremolque|9,63E-03|kg/VKT|0%|238.513|76.547|315.060|km|2,30|0,74|3,03|
|**PE**|Combustión vehículos<br>No Pavimentado|liviano|9,56E-04|kg/VKT|0%|73.770|75.262|149.032|km|0,07|0,07|0,14|
|**PE**|Combustión vehículos<br>No Pavimentado|Sobredimensionado|1,11E-02|kg/VKT|0%|0|870|870|km|0,00|0,01|0,01|
|**LT**|Combustión vehículos<br>Pavimentado|Camión rígido + 2 ejes|7,56E-03|kg/VKT|0%|0|0|0|km|0,00|0,00|0,00|
|**LT**|Combustión vehículos<br>Pavimentado|Camión Semiremolque|7,56E-03|kg/VKT|0%|0|3.198|3.198|km|0,00|0,02|0,02|
|**LT**|Combustión vehículos<br>Pavimentado|liviano|8,59E-04|kg/VKT|0%|0|0|0|km|0,00|0,00|0,00|
|**LT**|Combustión vehículos<br>Pavimentado|Sobredimensionado|1,11E-02|kg/VKT|0%|0|0|0|km|0,00|0,00|0,00|
|**LT**|Combustión vehículos<br>No Pavimentado|Camión rígido + 2 ejes|9,63E-03|kg/VKT|0%|0|0|0|km|0,00|0,00|0,00|
|**LT**|Combustión vehículos<br>No Pavimentado|Camión Semiremolque|9,63E-03|kg/VKT|0%|0|605|605|km|0,00|0,01|0,01|
|**LT**|Combustión vehículos<br>No Pavimentado|liviano|9,56E-04|kg/VKT|0%|0|0|0|km|0,00|0,00|0,00|
|**LT**|Combustión vehículos<br>No Pavimentado|Sobredimensionado|1,11E-02|kg/VKT|0%|0|0|0|km|0,00|0,00|0,00|
|**PE**|Combustión vehículos<br>Pavimentado Ruta 5-<br>182|Camión rígido + 2 ejes|7,56E-03|kg/VKT|0%|9.492|792|13.464|km|0,07|0,01|0,10|
|**PE**|Combustión vehículos<br>Pavimentado Ruta 5-<br>182|Camión Semiremolque|7,56E-03|kg/VKT|0%|1.768.111|594|10.098|km|13,37|0,00|0,08|
|**PE**|Combustión vehículos<br>Pavimentado Ruta 5-<br>182|liviano|8,59E-04|kg/VKT|0%|680.712|990|16.830|km|0,58|0,00|0,01|
|**PE**|Combustión vehículos<br>Pavimentado Ruta 5-<br>182|Sobredimensionado|1,11E-02|kg/VKT|0%|0|8.910|25.740|km|0,00|0,10|0,29|
|**LT**|**LT**|Camión Semiremolque|7,56E-03|kg/VKT|0%|0|1.078|1.078|km|0,00|0,01|0,01|
|**PE**|Grupos electrógenos|Instalación de faenas|8,65E-02|kg/kg comb.|0%|104.180|104.180|208.361|kg comb.|9,01|9,01|18,02|
|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**86,33 **|**46,96 **|**119,63 **|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 88

**Tabla 60.** Emisiones de CO debido a las actividades de la fase de Construcción del Proyecto Parque Eólico Dañicalqui, Sectores Parque Eólico

(PE) y Línea de Transmisión (LT).

|Sector|Actividad|Col3|Factor Emisión|Col5|Eficiencia<br>Mitigación|Nivel de Actividad|Col8|Col9|Col10|Emisión CO (t/año)|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Sector**|**Actividad**|**Actividad**|**Valor**|**Unidad**|**Unidad**|**Año 1**|**Año 2**|**Total**|**Unidad**|**Año 1**|**Año 2**|**Total**|
|**PE**|Maquinaria fuera de<br>ruta|Motoniveladora|1,83E-01|kg/h|0%|12.672|792|13.464|h|2,32|0,15|2,47|
|**PE**|Maquinaria fuera de<br>ruta|Compactadora|1,35E-01|kg/h|0%|9.504|594|10.098|h|1,29|0,08|1,37|
|**PE**|Maquinaria fuera de<br>ruta|Bulldozer|3,11E-01|kg/h|0%|15.840|990|16.830|h|4,92|0,31|5,23|
|**PE**|Maquinaria fuera de<br>ruta|Retroexcavadora|2,01E-01|kg/h|0%|16.830|8.910|25.740|h|3,38|1,79|5,17|
|**PE**|Maquinaria fuera de<br>ruta|Grúa de apoyo|2,91E-01|kg/h|0%|0|1.078|1.078|h|0,00|0,31|0,31|
|**PE**|Maquinaria fuera de<br>ruta|Grúa principal|8,78E-01|kg/h|0%|0|924|924|h|0,00|0,81|0,81|
|**LT**|Maquinaria fuera de<br>ruta|Motoniveladora|1,83E-01|kg/h|0%|3.168|7.128|10.296|h|0,58|1,31|1,89|
|**LT**|Maquinaria fuera de<br>ruta|Compactadora|1,35E-01|kg/h|0%|2.376|5.346|7.722|h|0,32|0,72|1,05|
|**LT**|Maquinaria fuera de<br>ruta|Bulldozer|3,11E-01|kg/h|0%|3.960|9.900|13.860|h|1,23|3,07|4,30|
|**LT**|Maquinaria fuera de<br>ruta|Retroexcavadora|2,01E-01|kg/h|0%|3.960|9.900|13.860|h|0,80|1,99|2,78|
|**LT**|Maquinaria fuera de<br>ruta|Grúa de apoyo|2,91E-01|kg/h|0%|0|616|616|h|0,00|0,18|0,18|
|**LT**|Maquinaria fuera de<br>ruta|Grúa principal|8,78E-01|kg/h|0%|0|528|528|h|0,00|0,46|0,46|
|**PE**|Combustión vehículos<br>Pavimentado|Camión rígido + 2 ejes|1,30E-03|kg/VKT|0%|1.907|4.790|6.697|km|0,00|0,01|0,01|
|**PE**|Combustión vehículos<br>Pavimentado|Camión Semiremolque|1,30E-03|kg/VKT|0%|355.187|114.976|470.162|km|0,46|0,15|0,61|
|**PE**|Combustión vehículos<br>Pavimentado|liviano|3,47E-04|kg/VKT|0%|136.745|139.469|276.214|km|0,05|0,05|0,10|
|**PE**|Combustión vehículos<br>Pavimentado|Sobredimensionado|1,99E-03|kg/VKT|0%|0|1.589|1.589|km|0,00|0,00|0,00|
|**PE**|Combustión vehículos<br>No Pavimentado|Camión rígido + 2 ejes|1,67E-03|kg/VKT|0%|18.430|20.019|38.448|km|0,03|0,03|0,06|
|**PE**|Combustión vehículos<br>No Pavimentado|Camión Semiremolque|1,67E-03|kg/VKT|0%|238.513|76.547|315.060|km|0,40|0,13|0,53|
|**PE**|Combustión vehículos<br>No Pavimentado|liviano|3,22E-04|kg/VKT|0%|73.770|75.262|149.032|km|0,02|0,02|0,05|
|**PE**|Combustión vehículos<br>No Pavimentado|Sobredimensionado|1,99E-03|kg/VKT|0%|0|870|870|km|0,00|0,00|0,00|
|**LT**|Combustión vehículos<br>Pavimentado|Camión rígido + 2 ejes|1,30E-03|kg/VKT|0%|0|0|0|km|0,00|0,00|0,00|
|**LT**|Combustión vehículos<br>Pavimentado|Camión Semiremolque|1,30E-03|kg/VKT|0%|0|3.198|3.198|km|0,00|0,00|0,00|
|**LT**|Combustión vehículos<br>Pavimentado|liviano|3,47E-04|kg/VKT|0%|0|0|0|km|0,00|0,00|0,00|
|**LT**|Combustión vehículos<br>Pavimentado|Sobredimensionado|1,99E-03|kg/VKT|0%|0|0|0|km|0,00|0,00|0,00|
|**LT**|Combustión vehículos<br>No Pavimentado|Camión rígido + 2 ejes|1,67E-03|kg/VKT|0%|0|0|0|km|0,00|0,00|0,00|
|**LT**|Combustión vehículos<br>No Pavimentado|Camión Semiremolque|1,67E-03|kg/VKT|0%|0|605|605|km|0,00|0,00|0,00|
|**LT**|Combustión vehículos<br>No Pavimentado|liviano|3,22E-04|kg/VKT|0%|0|0|0|km|0,00|0,00|0,00|
|**LT**|Combustión vehículos<br>No Pavimentado|Sobredimensionado|1,99E-03|kg/VKT|0%|0|0|0|km|0,00|0,00|0,00|
|**PE**|Combustión vehículos<br>Pavimentado Ruta 5-<br>182|Camión rígido + 2 ejes|1,30E-03|kg/VKT|0%|9.492|792|13.464|km|0,01|0,00|0,02|
|**PE**|Combustión vehículos<br>Pavimentado Ruta 5-<br>182|Camión Semiremolque|1,30E-03|kg/VKT|0%|1.768.111|594|10.098|km|2,30|0,00|0,01|
|**PE**|Combustión vehículos<br>Pavimentado Ruta 5-<br>182|liviano|3,47E-04|kg/VKT|0%|680.712|990|16.830|km|0,24|0,00|0,01|
|**PE**|Combustión vehículos<br>Pavimentado Ruta 5-<br>182|Sobredimensionado|1,99E-03|kg/VKT|0%|0|8.910|25.740|km|0,00|0,02|0,05|
|**LT**|**LT**|Camión Semiremolque|1,30E-03|kg/VKT|0%|0|1.078|1.078|km|0,00|0,00|0,00|
|**PE**|Grupos electrógenos|Instalación de faenas|1,86E-02|kg/kg comb.|0%|104.180|104.180|208.361|kg comb.|1,94|1,94|3,88|
|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**20,29 **|**13,54 **|**31,35 **|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 89

**Tabla 61.** Emisiones de SOx debido a las actividades de la fase de Construcción del Proyecto Parque Eólico Dañicalqui, Sectores Parque

Eólico (PE) y Línea de Transmisión (LT).

|Sector|Actividad|Col3|Factor Emisión|Col5|Eficiencia<br>Mitigación|Nivel de Actividad|Col8|Col9|Col10|Emisión SOx (t/año)|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Sector**|**Actividad**|**Actividad**|**Valor**|**Unidad**|**Unidad**|**Año 1**|**Año 2**|**Total**|**Unidad**|**Año 1**|**Año 2**|**Total**|
|**PE**|Maquinaria fuera de<br>ruta|Motoniveladora|5,85E-04|kg/h|0%|12.672|792|13.464|h|0,01|0,00|0,01|
|**PE**|Maquinaria fuera de<br>ruta|Compactadora|6,26E-03|kg/h|0%|9.504|594|10.098|h|0,06|0,00|0,06|
|**PE**|Maquinaria fuera de<br>ruta|Bulldozer|9,66E-04|kg/h|0%|15.840|990|16.830|h|0,02|0,00|0,02|
|**PE**|Maquinaria fuera de<br>ruta|Retroexcavadora|4,43E-04|kg/h|0%|16.830|8.910|25.740|h|0,01|0,00|0,01|
|**PE**|Maquinaria fuera de<br>ruta|Grúa de apoyo|9,06E-04|kg/h|0%|0|1.078|1.078|h|0,00|0,00|0,00|
|**PE**|Maquinaria fuera de<br>ruta|Grúa principal|2,73E-03|kg/h|0%|0|924|924|h|0,00|0,00|0,00|
|**LT**|Maquinaria fuera de<br>ruta|Motoniveladora|5,85E-04|kg/h|0%|3.168|7.128|10.296|h|0,00|0,00|0,01|
|**LT**|Maquinaria fuera de<br>ruta|Compactadora|6,26E-03|kg/h|0%|2.376|5.346|7.722|h|0,01|0,03|0,05|
|**LT**|Maquinaria fuera de<br>ruta|Bulldozer|9,66E-04|kg/h|0%|3.960|9.900|13.860|h|0,00|0,01|0,01|
|**LT**|Maquinaria fuera de<br>ruta|Retroexcavadora|4,43E-04|kg/h|0%|3.960|9.900|13.860|h|0,00|0,00|0,01|
|**LT**|Maquinaria fuera de<br>ruta|Grúa de apoyo|9,06E-04|kg/h|0%|0|616|616|h|0,00|0,00|0,00|
|**LT**|Maquinaria fuera de<br>ruta|Grúa principal|2,73E-03|kg/h|0%|0|528|528|h|0,00|0,00|0,00|
|**PE**|Combustión vehículos<br>Pavimentado|Camión rígido + 2 ejes|2,06E-05|kg/VKT|0%|1.907|4.790|6.697|km|0,00|0,00|0,00|
|**PE**|Combustión vehículos<br>Pavimentado|Camión Semiremolque|2,06E-05|kg/VKT|0%|355.187|114.976|470.162|km|0,01|0,00|0,01|
|**PE**|Combustión vehículos<br>Pavimentado|liviano|6,37E-06|kg/VKT|0%|136.745|139.469|276.214|km|0,00|0,00|0,00|
|**PE**|Combustión vehículos<br>Pavimentado|Sobredimensionado|3,08E-05|kg/VKT|0%|0|1.589|1.589|km|0,00|0,00|0,00|
|**PE**|Combustión vehículos<br>No Pavimentado|Camión rígido + 2 ejes|2,66E-05|kg/VKT|0%|18.430|20.019|38.448|km|0,00|0,00|0,00|
|**PE**|Combustión vehículos<br>No Pavimentado|Camión Semiremolque|2,66E-05|kg/VKT|0%|238.513|76.547|315.060|km|0,01|0,00|0,01|
|**PE**|Combustión vehículos<br>No Pavimentado|liviano|6,89E-06|kg/VKT|0%|73.770|75.262|149.032|km|0,00|0,00|0,00|
|**PE**|Combustión vehículos<br>No Pavimentado|Sobredimensionado|3,08E-05|kg/VKT|0%|0|870|870|km|0,00|0,00|0,00|
|**LT**|Combustión vehículos<br>Pavimentado|Camión rígido + 2 ejes|2,06E-05|kg/VKT|0%|0|0|0|km|0,00|0,00|0,00|
|**LT**|Combustión vehículos<br>Pavimentado|Camión Semiremolque|2,06E-05|kg/VKT|0%|0|3.198|3.198|km|0,00|0,00|0,00|
|**LT**|Combustión vehículos<br>Pavimentado|liviano|6,37E-06|kg/VKT|0%|0|0|0|km|0,00|0,00|0,00|
|**LT**|Combustión vehículos<br>Pavimentado|Sobredimensionado|3,08E-05|kg/VKT|0%|0|0|0|km|0,00|0,00|0,00|
|**LT**|Combustión vehículos<br>No Pavimentado|Camión rígido + 2 ejes|2,66E-05|kg/VKT|0%|0|0|0|km|0,00|0,00|0,00|
|**LT**|Combustión vehículos<br>No Pavimentado|Camión Semiremolque|2,66E-05|kg/VKT|0%|0|605|605|km|0,00|0,00|0,00|
|**LT**|Combustión vehículos<br>No Pavimentado|liviano|6,89E-06|kg/VKT|0%|0|0|0|km|0,00|0,00|0,00|
|**LT**|Combustión vehículos<br>No Pavimentado|Sobredimensionado|3,08E-05|kg/VKT|0%|0|0|0|km|0,00|0,00|0,00|
|**PE**|Combustión vehículos<br>Pavimentado Ruta 5-<br>182|Camión rígido + 2 ejes|2,06E-05|kg/VKT|0%|9.492|792|13.464|km|0,00|0,00|0,00|
|**PE**|Combustión vehículos<br>Pavimentado Ruta 5-<br>182|Camión Semiremolque|2,06E-05|kg/VKT|0%|1.768.111|594|10.098|km|0,04|0,00|0,00|
|**PE**|Combustión vehículos<br>Pavimentado Ruta 5-<br>182|liviano|6,37E-06|kg/VKT|0%|680.712|990|16.830|km|0,00|0,00|0,00|
|**PE**|Combustión vehículos<br>Pavimentado Ruta 5-<br>182|Sobredimensionado|3,08E-05|kg/VKT|0%|0|8.910|25.740|km|0,00|0,00|0,00|
|**LT**|**LT**|Camión Semiremolque|2,06E-05|kg/VKT|0%|0|1.078|1.078|km|0,00|0,00|0,00|
|**PE**|Grupos electrógenos|Instalación de faenas|5,69E-03|kg/kg comb.|0%|104.180|104.180|208.361|kg comb.|0,59|0,59|1,18|
|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**0,76 **|**0,67 **|**1,39 **|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 90

**Tabla 62.** Emisiones de HC debido a las actividades de la fase de Construcción del Proyecto Parque Eólico Dañicalqui, Sectores Parque Eólico

(PE) y Línea de Transmisión (LT).

|Sector|Actividad|Col3|Factor Emisión|Col5|Eficiencia<br>Mitigación|Nivel de Actividad|Col8|Col9|Col10|Emisión HC (t/año)|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Sector**|**Actividad**|**Actividad**|**Valor**|**Unidad**|**Unidad**|**Año 1**|**Año 2**|**Total**|**Unidad**|**Año 1**|**Año 2**|**Total**|
|**PE**|Maquinaria fuera de<br>ruta|Motoniveladora|2,43E-02|kg/h|0%|12.672|792|13.464|h|0,31|0,02|0,33|
|**PE**|Maquinaria fuera de<br>ruta|Compactadora|8,91E-02|kg/h|0%|9.504|594|10.098|h|0,85|0,05|0,90|
|**PE**|Maquinaria fuera de<br>ruta|Bulldozer|8,25E-02|kg/h|0%|15.840|990|16.830|h|1,31|0,08|1,39|
|**PE**|Maquinaria fuera de<br>ruta|Retroexcavadora|2,43E-02|kg/h|0%|16.830|8.910|25.740|h|0,41|0,22|0,62|
|**PE**|Maquinaria fuera de<br>ruta|Grúa de apoyo|3,87E-02|kg/h|0%|0|1.078|1.078|h|0,00|0,04|0,04|
|**PE**|Maquinaria fuera de<br>ruta|Grúa principal|1,17E-01|kg/h|0%|0|924|924|h|0,00|0,11|0,11|
|**LT**|Maquinaria fuera de<br>ruta|Motoniveladora|2,43E-02|kg/h|0%|3.168|7.128|10.296|h|0,08|0,17|0,25|
|**LT**|Maquinaria fuera de<br>ruta|Compactadora|8,91E-02|kg/h|0%|2.376|5.346|7.722|h|0,21|0,48|0,69|
|**LT**|Maquinaria fuera de<br>ruta|Bulldozer|8,25E-02|kg/h|0%|3.960|9.900|13.860|h|0,33|0,82|1,14|
|**LT**|Maquinaria fuera de<br>ruta|Retroexcavadora|2,43E-02|kg/h|0%|3.960|9.900|13.860|h|0,10|0,24|0,34|
|**LT**|Maquinaria fuera de<br>ruta|Grúa de apoyo|3,87E-02|kg/h|0%|0|616|616|h|0,00|0,02|0,02|
|**LT**|Maquinaria fuera de<br>ruta|Grúa principal|1,17E-01|kg/h|0%|0|528|528|h|0,00|0,06|0,06|
|**PE**|Combustión vehículos<br>Pavimentado|Camión rígido + 2 ejes|2,77E-01|kg/VKT|0%|1.907|4.790|6.697|km|0,53|1,33|1,85|
|**PE**|Combustión vehículos<br>Pavimentado|Camión Semiremolque|2,77E-01|kg/VKT|0%|355.187|114.976|470.162|km|98,31|31,82|130,13|
|**PE**|Combustión vehículos<br>Pavimentado|liviano|6,06E-02|kg/VKT|0%|136.745|139.469|276.214|km|8,29|8,46|16,75|
|**PE**|Combustión vehículos<br>Pavimentado|Sobredimensionado|6,19E-01|kg/VKT|0%|0|1.589|1.589|km|0,00|0,98|0,98|
|**PE**|Combustión vehículos<br>No Pavimentado|Camión rígido + 2 ejes|4,88E-01|kg/VKT|0%|18.430|20.019|38.448|km|8,99|9,77|18,76|
|**PE**|Combustión vehículos<br>No Pavimentado|Camión Semiremolque|4,88E-01|kg/VKT|0%|238.513|76.547|315.060|km|116,37|37,35|153,71|
|**PE**|Combustión vehículos<br>No Pavimentado|liviano|8,05E-02|kg/VKT|0%|73.770|75.262|149.032|km|5,94|6,06|11,99|
|**PE**|Combustión vehículos<br>No Pavimentado|Sobredimensionado|6,19E-01|kg/VKT|0%|0|870|870|km|0,00|0,54|0,54|
|**LT**|Combustión vehículos<br>Pavimentado|Camión rígido + 2 ejes|2,77E-01|kg/VKT|0%|0|0|0|km|0,00|0,00|0,00|
|**LT**|Combustión vehículos<br>Pavimentado|Camión Semiremolque|2,77E-01|kg/VKT|0%|0|3.198|3.198|km|0,00|0,89|0,89|
|**LT**|Combustión vehículos<br>Pavimentado|liviano|6,06E-02|kg/VKT|0%|0|0|0|km|0,00|0,00|0,00|
|**LT**|Combustión vehículos<br>Pavimentado|Sobredimensionado|6,19E-01|kg/VKT|0%|0|0|0|km|0,00|0,00|0,00|
|**LT**|Combustión vehículos<br>No Pavimentado|Camión rígido + 2 ejes|4,88E-01|kg/VKT|0%|0|0|0|km|0,00|0,00|0,00|
|**LT**|Combustión vehículos<br>No Pavimentado|Camión Semiremolque|4,88E-01|kg/VKT|0%|0|605|605|km|0,00|0,29|0,29|
|**LT**|Combustión vehículos<br>No Pavimentado|liviano|8,05E-02|kg/VKT|0%|0|0|0|km|0,00|0,00|0,00|
|**LT**|Combustión vehículos<br>No Pavimentado|Sobredimensionado|6,19E-01|kg/VKT|0%|0|0|0|km|0,00|0,00|0,00|
|**PE**|Combustión vehículos<br>Pavimentado Ruta 5-<br>182|Camión rígido + 2 ejes|2,77E-01|kg/VKT|0%|9.492|792|13.464|km|2,63|0,22|3,73|
|**PE**|Combustión vehículos<br>Pavimentado Ruta 5-<br>182|Camión Semiremolque|2,77E-01|kg/VKT|0%|1.768.111|594|10.098|km|489,39|0,16|2,79|
|**PE**|Combustión vehículos<br>Pavimentado Ruta 5-<br>182|liviano|6,06E-02|kg/VKT|0%|680.712|990|16.830|km|41,28|0,06|1,02|
|**PE**|Combustión vehículos<br>Pavimentado Ruta 5-<br>182|Sobredimensionado|6,19E-01|kg/VKT|0%|0|8.910|25.740|km|0,00|5,52|15,94|
|**LT**|**LT**|Camión Semiremolque|2,77E-01|kg/VKT|0%|0|1.078|1.078|km|0,00|0,30|0,30|
|**PE**|Grupos electrógenos|Instalación de faenas|7,06E-03|kg/kg comb.|0%|104.180|104.180|208.361|kg comb.|0,74|0,74|1,47|
|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**776,03 **|**106,79 **|**367,05 **|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 91

**F.6.2. Fase de Operación**

Las emisiones de MP10, MP2,5, MPS, NOx, CO, SOx y HC debido a las actividades del proyecto Parque

Eólico Dañicalqui durante toda la fase de operación se presentan en **Tabla 63** a **Tabla 69**, respectivamente.

En estas tablas se muestran las emisiones calculadas siguiendo la metodología indicada en **Sección F.2.**,

se indica cada factor según actividad emisora (presentados en **Sección F.3.** y **F.4.** ) y se presenta el nivel de

actividad expuesto en **Sección F.5** .

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 92

**Tabla 63.** Emisiones de MP10 debido a las actividades de la fase de Operación del Proyecto Parque Eólico Dañicalqui, Sectores Parque

Eólico (PE) y Línea de Transmisión (LT).

|Actividad|Col2|Factor Emisión|Col4|Eficiencia<br>Mitigación|Nivel de Actividad|Col7|Emisión MP10<br>(t/año)|
|---|---|---|---|---|---|---|---|
|**Actividad**|**Actividad**|**Valor**|**Unidad**|**Unidad**|**Cantidad**|**Unidad**|**Unidad**|
|Resuspensión caminos<br>Pavimentados Ruta 85|Vehículo liviano|3,84E-04|kg/VKT|0%|75.600|km/año|0,03|
|Resuspensión caminos<br>Pavimentados Ruta 85|Camión 3/4 Mantención|6,02E-04|kg/VKT|0%|504|km/año|0,00|
|Resuspensión caminos<br>Pavimentados Ruta 85|Aljibe|3,53E-03|kg/VKT|0%|1.008|km/año|0,00|
|Resuspensión caminos<br>Pavimentados Ruta 85|Camión 3/4 - Residuos Peligrosos|6,02E-04|kg/VKT|0%|320|km/año|0,00|
|Resuspensión caminos<br>Pavimentados Ruta 85|Camión 3/4 - Residuos Domiciliarios|6,02E-04|kg/VKT|0%|3.840|km/año|0,00|
|Resuspensión caminos<br>Pavimentados Ruta 5-152|Vehículo liviano|3,84E-04|kg/VKT|0%|406.800|km/año|0,16|
|Resuspensión caminos<br>Pavimentados Ruta 5-152|Camión 3/4 Mantención|6,02E-04|kg/VKT|0%|2.712|km/año|0,00|
|Resuspensión caminos<br>Pavimentados Ruta 5-152|Aljibe|3,53E-03|kg/VKT|0%|5.424|km/año|0,02|
|Resuspensión caminos<br>Pavimentados Ruta 5-152|Camión 3/4 - Residuos Peligrosos|6,02E-04|kg/VKT|0%|904|km/año|0,00|
|Resuspensión caminos<br>Pavimentados Ruta 5-152|Camión 3/4 - Residuos Domiciliarios|6,02E-04|kg/VKT|0%|10.848|km/año|0,01|
|Resuspensión caminos No<br>Pavimentados - Externo|Vehículo liviano|1,51E-01|kg/VKT|0%|26.280|km/año|3,96|
|Resuspensión caminos No<br>Pavimentados - Externo|Camión 3/4 Mantención|1,84E-01|kg/VKT|0%|175|km/año|0,03|
|Resuspensión caminos No<br>Pavimentados - Externo|Aljibe|4,01E-01|kg/VKT|0%|350|km/año|0,14|
|Resuspensión caminos No<br>Pavimentados - Externo|Camión 3/4 - Residuos Peligrosos|1,84E-01|kg/VKT|0%|58|km/año|0,01|
|Resuspensión caminos No<br>Pavimentados - Externo|Camión 3/4 - Residuos Domiciliarios|1,84E-01|kg/VKT|0%|701|km/año|0,13|
|Resuspensión caminos No<br>Pavimentados - Interno|Vehículo liviano|1,51E-01|kg/VKT|0%|21.600|km/año|3,25|
|Resuspensión caminos No<br>Pavimentados - Interno|Camión 3/4 Mantención|1,84E-01|kg/VKT|0%|144|km/año|0,03|
|Resuspensión caminos No<br>Pavimentados - Interno|Aljibe|4,01E-01|kg/VKT|0%|288|km/año|0,12|
|Resuspensión caminos No<br>Pavimentados - Interno|Camión 3/4 - Residuos Peligrosos|1,84E-01|kg/VKT|0%|48|km/año|0,01|
|Resuspensión caminos No<br>Pavimentados - Interno|Camión 3/4 - Residuos Domiciliarios|1,84E-01|kg/VKT|0%|576|km/año|0,11|
|Combustión vehículos<br>Pavimentado Ruta 85|Vehículo liviano|6,06E-05|kg/VKT|0%|75.600|km/año|0,00|
|Combustión vehículos<br>Pavimentado Ruta 85|Camión 3/4 Mantención|8,82E-04|kg/VKT|0%|504|km/año|0,00|
|Combustión vehículos<br>Pavimentado Ruta 85|Aljibe|8,82E-04|kg/VKT|0%|1.008|km/año|0,00|
|Combustión vehículos<br>Pavimentado Ruta 85|Camión 3/4 - Residuos Peligrosos|8,82E-04|kg/VKT|0%|320|km/año|0,00|
|Combustión vehículos<br>Pavimentado Ruta 85|Camión 3/4 - Residuos Domiciliarios|8,82E-04|kg/VKT|0%|3.840|km/año|0,00|
|Combustión vehículos<br>Pavimentado Ruta 5-152|Vehículo liviano|6,06E-05|kg/VKT|0%|406.800|km/año|0,02|
|Combustión vehículos<br>Pavimentado Ruta 5-152|Camión 3/4 Mantención|8,82E-04|kg/VKT|0%|2.712|km/año|0,00|
|Combustión vehículos<br>Pavimentado Ruta 5-152|Aljibe|8,82E-04|kg/VKT|0%|5.424|km/año|0,00|
|Combustión vehículos<br>Pavimentado Ruta 5-152|Camión 3/4 - Residuos Peligrosos|8,82E-04|kg/VKT|0%|904|km/año|0,00|
|Combustión vehículos<br>Pavimentado Ruta 5-152|Camión 3/4 - Residuos Domiciliarios|8,82E-04|kg/VKT|0%|10.848|km/año|0,01|
|Combustión vehículos No<br>Pavimentadas|Vehículo liviano|4,68E-05|kg/VKT|0%|47.880|km/año|0,00|
|Combustión vehículos No<br>Pavimentadas|Camión 3/4 Mantención|7,02E-04|kg/VKT|0%|47.880|km/año|0,03|
|Combustión vehículos No<br>Pavimentadas|Aljibe|7,02E-04|kg/VKT|0%|319|km/año|0,00|
|Combustión vehículos No<br>Pavimentadas|Camión 3/4 - Residuos Peligrosos|7,02E-04|kg/VKT|0%|638|km/año|0,00|
|Combustión vehículos No<br>Pavimentadas|Camión 3/4 - Residuos Domiciliarios|7,02E-04|kg/VKT|0%|106|km/año|0,00|
|Maquinaria fuera de ruta|Grúa pluma|1,84E-02|kg/h|0%|8|h|0,00|
|Grupos electrógenos|Emergencia|6,08E-03|kg/kg comb.|0%|2.631|kg comb.|0,02|
|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**8,11 **|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 93

**Tabla 64.** Emisiones de MP2,5 debido a las actividades de la fase de Operación del Proyecto Parque Eólico Dañicalqui, Sectores Parque

Eólico (PE) y Línea de Transmisión (LT).

|Actividad|Col2|Factor Emisión|Col4|Eficiencia<br>Mitigación|Nivel de Actividad|Col7|Emisión MP2,5<br>(t/año)|
|---|---|---|---|---|---|---|---|
|**Actividad**|**Actividad**|**Valor**|**Unidad**|**Unidad**|**Cantidad**|**Unidad**|**Unidad**|
|Resuspensión caminos<br>Pavimentados Ruta 85|Vehículo liviano|9,30E-05|kg/VKT|0%|75.600|km/año|0,01|
|Resuspensión caminos<br>Pavimentados Ruta 85|Camión 3/4 Mantención|1,46E-04|kg/VKT|0%|504|km/año|0,00|
|Resuspensión caminos<br>Pavimentados Ruta 85|Aljibe|8,55E-04|kg/VKT|0%|1.008|km/año|0,00|
|Resuspensión caminos<br>Pavimentados Ruta 85|Camión 3/4 - Residuos Peligrosos|1,46E-04|kg/VKT|0%|320|km/año|0,00|
|Resuspensión caminos<br>Pavimentados Ruta 85|Camión 3/4 - Residuos Domiciliarios|1,46E-04|kg/VKT|0%|3.840|km/año|0,00|
|Resuspensión caminos<br>Pavimentados Ruta 5-152|Vehículo liviano|9,30E-05|kg/VKT|0%|406.800|km/año|0,04|
|Resuspensión caminos<br>Pavimentados Ruta 5-152|Camión 3/4 Mantención|1,46E-04|kg/VKT|0%|2.712|km/año|0,00|
|Resuspensión caminos<br>Pavimentados Ruta 5-152|Aljibe|8,55E-04|kg/VKT|0%|5.424|km/año|0,00|
|Resuspensión caminos<br>Pavimentados Ruta 5-152|Camión 3/4 - Residuos Peligrosos|1,46E-04|kg/VKT|0%|904|km/año|0,00|
|Resuspensión caminos<br>Pavimentados Ruta 5-152|Camión 3/4 - Residuos Domiciliarios|1,46E-04|kg/VKT|0%|10.848|km/año|0,00|
|Resuspensión caminos No<br>Pavimentados - Externo|Vehículo liviano|1,51E-02|kg/VKT|0%|26.280|km/año|0,40|
|Resuspensión caminos No<br>Pavimentados - Externo|Camión 3/4 Mantención|1,84E-02|kg/VKT|0%|175|km/año|0,00|
|Resuspensión caminos No<br>Pavimentados - Externo|Aljibe|4,01E-02|kg/VKT|0%|350|km/año|0,01|
|Resuspensión caminos No<br>Pavimentados - Externo|Camión 3/4 - Residuos Peligrosos|1,84E-02|kg/VKT|0%|58|km/año|0,00|
|Resuspensión caminos No<br>Pavimentados - Externo|Camión 3/4 - Residuos Domiciliarios|1,84E-02|kg/VKT|0%|701|km/año|0,01|
|Resuspensión caminos No<br>Pavimentados - Interno|Vehículo liviano|1,51E-02|kg/VKT|0%|21.600|km/año|0,33|
|Resuspensión caminos No<br>Pavimentados - Interno|Camión 3/4 Mantención|1,84E-02|kg/VKT|0%|144|km/año|0,00|
|Resuspensión caminos No<br>Pavimentados - Interno|Aljibe|4,01E-02|kg/VKT|0%|288|km/año|0,01|
|Resuspensión caminos No<br>Pavimentados - Interno|Camión 3/4 - Residuos Peligrosos|1,84E-02|kg/VKT|0%|48|km/año|0,00|
|Resuspensión caminos No<br>Pavimentados - Interno|Camión 3/4 - Residuos Domiciliarios|1,84E-02|kg/VKT|0%|576|km/año|0,01|
|Combustión vehículos<br>Pavimentado Ruta 85|Vehículo liviano|6,06E-05|kg/VKT|0%|75.600|km/año|0,00|
|Combustión vehículos<br>Pavimentado Ruta 85|Camión 3/4 Mantención|8,82E-04|kg/VKT|0%|504|km/año|0,00|
|Combustión vehículos<br>Pavimentado Ruta 85|Aljibe|8,82E-04|kg/VKT|0%|1.008|km/año|0,00|
|Combustión vehículos<br>Pavimentado Ruta 85|Camión 3/4 - Residuos Peligrosos|8,82E-04|kg/VKT|0%|320|km/año|0,00|
|Combustión vehículos<br>Pavimentado Ruta 85|Camión 3/4 - Residuos Domiciliarios|8,82E-04|kg/VKT|0%|3.840|km/año|0,00|
|Combustión vehículos<br>Pavimentado Ruta 5-152|Vehículo liviano|6,06E-05|kg/VKT|0%|406.800|km/año|0,02|
|Combustión vehículos<br>Pavimentado Ruta 5-152|Camión 3/4 Mantención|8,82E-04|kg/VKT|0%|2.712|km/año|0,00|
|Combustión vehículos<br>Pavimentado Ruta 5-152|Aljibe|8,82E-04|kg/VKT|0%|5.424|km/año|0,00|
|Combustión vehículos<br>Pavimentado Ruta 5-152|Camión 3/4 - Residuos Peligrosos|8,82E-04|kg/VKT|0%|904|km/año|0,00|
|Combustión vehículos<br>Pavimentado Ruta 5-152|Camión 3/4 - Residuos Domiciliarios|8,82E-04|kg/VKT|0%|10.848|km/año|0,01|
|Combustión vehículos No<br>Pavimentadas|Vehículo liviano|4,68E-05|kg/VKT|0%|47.880|km/año|0,00|
|Combustión vehículos No<br>Pavimentadas|Camión 3/4 Mantención|7,02E-04|kg/VKT|0%|47.880|km/año|0,03|
|Combustión vehículos No<br>Pavimentadas|Aljibe|7,02E-04|kg/VKT|0%|319|km/año|0,00|
|Combustión vehículos No<br>Pavimentadas|Camión 3/4 - Residuos Peligrosos|7,02E-04|kg/VKT|0%|638|km/año|0,00|
|Combustión vehículos No<br>Pavimentadas|Camión 3/4 - Residuos Domiciliarios|7,02E-04|kg/VKT|0%|106|km/año|0,00|
|Maquinaria fuera de ruta|Grúa pluma|1,84E-02|kg/h|0%|8|h|0,00|
|Grupos electrógenos|Emergencia|6,08E-03|kg/kg comb.|0%|2.631|kg comb.|0,02|
|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**0,94 **|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 94

**Tabla 65.** Emisiones de MPS debido a las actividades de la fase de Operación del Proyecto Parque Eólico Dañicalqui, Sectores Parque Eólico

(PE) y Línea de Transmisión (LT).

|Actividad|Col2|Factor Emisión|Col4|Eficiencia<br>Mitigación|Nivel de Actividad|Col7|Emisión MPS<br>(t/año)|
|---|---|---|---|---|---|---|---|
|**Actividad**|**Actividad**|**Valor**|**Unidad**|**Unidad**|**Cantidad**|**Unidad**|**Unidad**|
|Resuspensión caminos<br>Pavimentados Ruta 85|Vehículo liviano|2,00E-03|kg/VKT|0%|75.600|km/año|0,15|
|Resuspensión caminos<br>Pavimentados Ruta 85|Camión 3/4 Mantención|3,14E-03|kg/VKT|0%|504|km/año|0,00|
|Resuspensión caminos<br>Pavimentados Ruta 85|Aljibe|1,84E-02|kg/VKT|0%|1.008|km/año|0,02|
|Resuspensión caminos<br>Pavimentados Ruta 85|Camión 3/4 - Residuos Peligrosos|3,14E-03|kg/VKT|0%|320|km/año|0,00|
|Resuspensión caminos<br>Pavimentados Ruta 85|Camión 3/4 - Residuos Domiciliarios|3,14E-03|kg/VKT|0%|3.840|km/año|0,01|
|Resuspensión caminos<br>Pavimentados Ruta 5-152|Vehículo liviano|2,00E-03|kg/VKT|0%|406.800|km/año|0,81|
|Resuspensión caminos<br>Pavimentados Ruta 5-152|Camión 3/4 Mantención|3,14E-03|kg/VKT|0%|2.712|km/año|0,01|
|Resuspensión caminos<br>Pavimentados Ruta 5-152|Aljibe|1,84E-02|kg/VKT|0%|5.424|km/año|0,10|
|Resuspensión caminos<br>Pavimentados Ruta 5-152|Camión 3/4 - Residuos Peligrosos|3,14E-03|kg/VKT|0%|904|km/año|0,00|
|Resuspensión caminos<br>Pavimentados Ruta 5-152|Camión 3/4 - Residuos Domiciliarios|3,14E-03|kg/VKT|0%|10.848|km/año|0,03|
|Resuspensión caminos No<br>Pavimentados - Externo|Vehículo liviano|4,92E-01|kg/VKT|0%|26.280|km/año|12,93|
|Resuspensión caminos No<br>Pavimentados - Externo|Camión 3/4 Mantención|6,00E-01|kg/VKT|0%|175|km/año|0,11|
|Resuspensión caminos No<br>Pavimentados - Externo|Aljibe|1,31E+00|kg/VKT|0%|350|km/año|0,46|
|Resuspensión caminos No<br>Pavimentados - Externo|Camión 3/4 - Residuos Peligrosos|6,00E-01|kg/VKT|0%|58|km/año|0,04|
|Resuspensión caminos No<br>Pavimentados - Externo|Camión 3/4 - Residuos Domiciliarios|6,00E-01|kg/VKT|0%|701|km/año|0,42|
|Resuspensión caminos No<br>Pavimentados - Interno|Vehículo liviano|4,92E-01|kg/VKT|0%|21.600|km/año|10,63|
|Resuspensión caminos No<br>Pavimentados - Interno|Camión 3/4 Mantención|6,00E-01|kg/VKT|0%|144|km/año|0,09|
|Resuspensión caminos No<br>Pavimentados - Interno|Aljibe|1,31E+00|kg/VKT|0%|288|km/año|0,38|
|Resuspensión caminos No<br>Pavimentados - Interno|Camión 3/4 - Residuos Peligrosos|6,00E-01|kg/VKT|0%|48|km/año|0,03|
|Resuspensión caminos No<br>Pavimentados - Interno|Camión 3/4 - Residuos Domiciliarios|6,00E-01|kg/VKT|0%|576|km/año|0,35|
|Combustión vehículos<br>Pavimentado Ruta 85|Vehículo liviano|6,06E-05|kg/VKT|0%|75.600|km/año|0,00|
|Combustión vehículos<br>Pavimentado Ruta 85|Camión 3/4 Mantención|8,82E-04|kg/VKT|0%|504|km/año|0,00|
|Combustión vehículos<br>Pavimentado Ruta 85|Aljibe|8,82E-04|kg/VKT|0%|1.008|km/año|0,00|
|Combustión vehículos<br>Pavimentado Ruta 85|Camión 3/4 - Residuos Peligrosos|8,82E-04|kg/VKT|0%|320|km/año|0,00|
|Combustión vehículos<br>Pavimentado Ruta 85|Camión 3/4 - Residuos Domiciliarios|8,82E-04|kg/VKT|0%|3.840|km/año|0,00|
|Combustión vehículos<br>Pavimentado Ruta 5-152|Vehículo liviano|6,06E-05|kg/VKT|0%|406.800|km/año|0,02|
|Combustión vehículos<br>Pavimentado Ruta 5-152|Camión 3/4 Mantención|8,82E-04|kg/VKT|0%|2.712|km/año|0,00|
|Combustión vehículos<br>Pavimentado Ruta 5-152|Aljibe|8,82E-04|kg/VKT|0%|5.424|km/año|0,00|
|Combustión vehículos<br>Pavimentado Ruta 5-152|Camión 3/4 - Residuos Peligrosos|8,82E-04|kg/VKT|0%|904|km/año|0,00|
|Combustión vehículos<br>Pavimentado Ruta 5-152|Camión 3/4 - Residuos Domiciliarios|8,82E-04|kg/VKT|0%|10.848|km/año|0,01|
|Combustión vehículos No<br>Pavimentadas|Vehículo liviano|4,68E-05|kg/VKT|0%|47.880|km/año|0,00|
|Combustión vehículos No<br>Pavimentadas|Camión 3/4 Mantención|7,02E-04|kg/VKT|0%|47.880|km/año|0,03|
|Combustión vehículos No<br>Pavimentadas|Aljibe|7,02E-04|kg/VKT|0%|319|km/año|0,00|
|Combustión vehículos No<br>Pavimentadas|Camión 3/4 - Residuos Peligrosos|7,02E-04|kg/VKT|0%|638|km/año|0,00|
|Combustión vehículos No<br>Pavimentadas|Camión 3/4 - Residuos Domiciliarios|7,02E-04|kg/VKT|0%|106|km/año|0,00|
|Maquinaria fuera de ruta|Grúa pluma|1,84E-02|kg/h|0%|8|h|0,00|
|Grupos electrógenos|Emergencia|6,08E-03|kg/kg comb.|0%|2.631|kg comb.|0,02|
|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**26,67 **|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 95

**Tabla 66.** Emisiones de NOx debido a las actividades de la fase de Operación del Proyecto Parque Eólico Dañicalqui, Sectores Parque Eólico

(PE) y Línea de Transmisión (LT).

|Actividad|Col2|Factor Emisión|Col4|Eficiencia<br>Mitigación|Nivel de Actividad|Col7|Emisión NOx<br>(t/año)|
|---|---|---|---|---|---|---|---|
|**Actividad**|**Actividad**|**Valor**|**Unidad**|**Unidad**|**Cantidad**|**Unidad**|**Unidad**|
|Combustión vehículos<br>Pavimentado Ruta 85|Vehículo liviano|8,59E-04|kg/VKT|0%|75.600|km/año|0,06|
|Combustión vehículos<br>Pavimentado Ruta 85|Camión 3/4 Mantención|7,56E-03|kg/VKT|0%|504|km/año|0,00|
|Combustión vehículos<br>Pavimentado Ruta 85|Aljibe|7,56E-03|kg/VKT|0%|1.008|km/año|0,01|
|Combustión vehículos<br>Pavimentado Ruta 85|Camión 3/4 - Residuos Peligrosos|7,56E-03|kg/VKT|0%|320|km/año|0,00|
|Combustión vehículos<br>Pavimentado Ruta 85|Camión 3/4 - Residuos Domiciliarios|7,56E-03|kg/VKT|0%|3.840|km/año|0,03|
|Combustión vehículos<br>Pavimentado Ruta 5-152|Vehículo liviano|8,59E-04|kg/VKT|0%|406.800|km/año|0,35|
|Combustión vehículos<br>Pavimentado Ruta 5-152|Camión 3/4 Mantención|7,56E-03|kg/VKT|0%|2.712|km/año|0,02|
|Combustión vehículos<br>Pavimentado Ruta 5-152|Aljibe|7,56E-03|kg/VKT|0%|5.424|km/año|0,04|
|Combustión vehículos<br>Pavimentado Ruta 5-152|Camión 3/4 - Residuos Peligrosos|7,56E-03|kg/VKT|0%|904|km/año|0,01|
|Combustión vehículos<br>Pavimentado Ruta 5-152|Camión 3/4 - Residuos Domiciliarios|7,56E-03|kg/VKT|0%|10.848|km/año|0,08|
|Combustión vehículos No<br>Pavimentadas|Vehículo liviano|9,56E-04|kg/VKT|0%|47.880|km/año|0,05|
|Combustión vehículos No<br>Pavimentadas|Camión 3/4 Mantención|9,63E-03|kg/VKT|0%|47.880|km/año|0,46|
|Combustión vehículos No<br>Pavimentadas|Aljibe|9,63E-03|kg/VKT|0%|319|km/año|0,00|
|Combustión vehículos No<br>Pavimentadas|Camión 3/4 - Residuos Peligrosos|9,63E-03|kg/VKT|0%|638|km/año|0,01|
|Combustión vehículos No<br>Pavimentadas|Camión 3/4 - Residuos Domiciliarios|9,63E-03|kg/VKT|0%|106|km/año|0,00|
|Maquinaria fuera de ruta|Grúa pluma|5,99E-01|kg/h|0%|8|h|0,00|
|Grupos electrógenos|Emergencia|8,65E-02|kg/kg comb.|0%|2.631|kg comb.|0,23|
|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**1,36 **|

**Tabla 67.** Emisiones de CO debido a las actividades de la fase de Operación del Proyecto Parque Eólico Dañicalqui, Sectores Parque Eólico

(PE) y Línea de Transmisión (LT).

|Actividad|Col2|Factor Emisión|Col4|Eficiencia<br>Mitigación|Nivel de Actividad|Col7|Emisión CO<br>(t/año)|
|---|---|---|---|---|---|---|---|
|**Actividad**|**Actividad**|**Valor**|**Unidad**|**Unidad**|**Cantidad**|**Unidad**|**Unidad**|
|Combustión vehículos<br>Pavimentado Ruta 85|Vehículo liviano|3,47E-04|kg/VKT|0%|75.600|km/año|0,03|
|Combustión vehículos<br>Pavimentado Ruta 85|Camión 3/4 Mantención|1,30E-03|kg/VKT|0%|504|km/año|0,00|
|Combustión vehículos<br>Pavimentado Ruta 85|Aljibe|1,30E-03|kg/VKT|0%|1.008|km/año|0,00|
|Combustión vehículos<br>Pavimentado Ruta 85|Camión 3/4 - Residuos Peligrosos|1,30E-03|kg/VKT|0%|320|km/año|0,00|
|Combustión vehículos<br>Pavimentado Ruta 85|Camión 3/4 - Residuos Domiciliarios|1,30E-03|kg/VKT|0%|3.840|km/año|0,00|
|Combustión vehículos<br>Pavimentado Ruta 5-152|Vehículo liviano|3,47E-04|kg/VKT|0%|406.800|km/año|0,14|
|Combustión vehículos<br>Pavimentado Ruta 5-152|Camión 3/4 Mantención|1,30E-03|kg/VKT|0%|2.712|km/año|0,00|
|Combustión vehículos<br>Pavimentado Ruta 5-152|Aljibe|1,30E-03|kg/VKT|0%|5.424|km/año|0,01|
|Combustión vehículos<br>Pavimentado Ruta 5-152|Camión 3/4 - Residuos Peligrosos|1,30E-03|kg/VKT|0%|904|km/año|0,00|
|Combustión vehículos<br>Pavimentado Ruta 5-152|Camión 3/4 - Residuos Domiciliarios|1,30E-03|kg/VKT|0%|10.848|km/año|0,01|
||Vehículo liviano|3,22E-04|kg/VKT|0%|47.880|km/año|0,02|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 96

|Actividad<br>Camión 3/4 Mantención<br>Combustión vehículos No Aljibe<br>Pavimentadas Camión 3/4 - Residuos Peligrosos<br>Camión 3/4 - Residuos Domiciliarios|Col2|Factor Emisión|Col4|Eficiencia<br>Mitigación|Nivel de Actividad|Col7|Emisión CO<br>(t/año)|
|---|---|---|---|---|---|---|---|
|**Actividad**<br>Combustión vehículos No<br>Pavimentadas<br>Camión 3/4 Mantención<br>Aljibe<br>Camión 3/4 - Residuos Peligrosos<br>Camión 3/4 - Residuos Domiciliarios|**Actividad**<br>Combustión vehículos No<br>Pavimentadas<br>Camión 3/4 Mantención<br>Aljibe<br>Camión 3/4 - Residuos Peligrosos<br>Camión 3/4 - Residuos Domiciliarios|**Valor**|**Unidad**|**Unidad**|**Cantidad**|**Unidad**|**Unidad**|
|**Actividad**<br>Combustión vehículos No<br>Pavimentadas<br>Camión 3/4 Mantención<br>Aljibe<br>Camión 3/4 - Residuos Peligrosos<br>Camión 3/4 - Residuos Domiciliarios|Camión 3/4 Mantención|1,67E-03|kg/VKT|0%|47.880|km/año|0,08|
|**Actividad**<br>Combustión vehículos No<br>Pavimentadas<br>Camión 3/4 Mantención<br>Aljibe<br>Camión 3/4 - Residuos Peligrosos<br>Camión 3/4 - Residuos Domiciliarios|Aljibe|1,67E-03|kg/VKT|0%|319|km/año|0,00|
|**Actividad**<br>Combustión vehículos No<br>Pavimentadas<br>Camión 3/4 Mantención<br>Aljibe<br>Camión 3/4 - Residuos Peligrosos<br>Camión 3/4 - Residuos Domiciliarios|Camión 3/4 - Residuos Peligrosos|1,67E-03|kg/VKT|0%|638|km/año|0,00|
|**Actividad**<br>Combustión vehículos No<br>Pavimentadas<br>Camión 3/4 Mantención<br>Aljibe<br>Camión 3/4 - Residuos Peligrosos<br>Camión 3/4 - Residuos Domiciliarios|Camión 3/4 - Residuos Domiciliarios|1,67E-03|kg/VKT|0%|106|km/año|0,00|
|Maquinaria fuera de ruta|Grúa pluma|2,91E-01|kg/h|0%|8|h|0,00|
|Grupos electrógenos|Emergencia|1,86E-02|kg/kg comb.|0%|2.631|kg comb.|0,05|
|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**0,35**|

**Tabla 68.** Emisiones de SOx debido a las actividades de la fase de Operación del Proyecto Parque Eólico Dañicalqui, Sectores Parque Eólico

(PE) y Línea de Transmisión (LT).

|Actividad|Col2|Factor Emisión|Col4|Eficiencia<br>Mitigación|Nivel de Actividad|Col7|Emisión SOx<br>(t/año)|
|---|---|---|---|---|---|---|---|
|**Actividad**|**Actividad**|**Valor**|**Unidad**|**Unidad**|**Cantidad**|**Unidad**|**Unidad**|
|Combustión vehículos<br>Pavimentado Ruta 85|Vehículo liviano|6,37E-06|kg/VKT|0%|75.600|km/año|0,00|
|Combustión vehículos<br>Pavimentado Ruta 85|Camión 3/4 Mantención|2,06E-05|kg/VKT|0%|504|km/año|0,00|
|Combustión vehículos<br>Pavimentado Ruta 85|Aljibe|2,06E-05|kg/VKT|0%|1.008|km/año|0,00|
|Combustión vehículos<br>Pavimentado Ruta 85|Camión 3/4 - Residuos Peligrosos|2,06E-05|kg/VKT|0%|320|km/año|0,00|
|Combustión vehículos<br>Pavimentado Ruta 85|Camión 3/4 - Residuos Domiciliarios|2,06E-05|kg/VKT|0%|3.840|km/año|0,00|
|Combustión vehículos<br>Pavimentado Ruta 5-152|Vehículo liviano|6,37E-06|kg/VKT|0%|406.800|km/año|0,00|
|Combustión vehículos<br>Pavimentado Ruta 5-152|Camión 3/4 Mantención|2,06E-05|kg/VKT|0%|2.712|km/año|0,00|
|Combustión vehículos<br>Pavimentado Ruta 5-152|Aljibe|2,06E-05|kg/VKT|0%|5.424|km/año|0,00|
|Combustión vehículos<br>Pavimentado Ruta 5-152|Camión 3/4 - Residuos Peligrosos|2,06E-05|kg/VKT|0%|904|km/año|0,00|
|Combustión vehículos<br>Pavimentado Ruta 5-152|Camión 3/4 - Residuos Domiciliarios|2,06E-05|kg/VKT|0%|10.848|km/año|0,00|
|Combustión vehículos No<br>Pavimentadas|Vehículo liviano|6,89E-06|kg/VKT|0%|47.880|km/año|0,00|
|Combustión vehículos No<br>Pavimentadas|Camión 3/4 Mantención|2,66E-05|kg/VKT|0%|47.880|km/año|0,00|
|Combustión vehículos No<br>Pavimentadas|Aljibe|2,66E-05|kg/VKT|0%|319|km/año|0,00|
|Combustión vehículos No<br>Pavimentadas|Camión 3/4 - Residuos Peligrosos|2,66E-05|kg/VKT|0%|638|km/año|0,00|
|Combustión vehículos No<br>Pavimentadas|Camión 3/4 - Residuos Domiciliarios|2,66E-05|kg/VKT|0%|106|km/año|0,00|
|Maquinaria fuera de ruta|Grúa pluma|9,06E-04|kg/h|0%|8|h|0,00|
|Grupos electrógenos|Emergencia|5,69E-03|kg/kg comb.|0%|2.631|kg comb.|0,01|
|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**0,02 **|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 97

**Tabla 69.** Emisiones de HC debido a las actividades de la fase de Operación del Proyecto Parque Eólico Dañicalqui, Sectores Parque Eólico

(PE) y Línea de Transmisión (LT).

|Actividad|Col2|Factor Emisión|Col4|Eficiencia<br>Mitigación|Nivel de Actividad|Col7|Emisión HC<br>(t/año)|
|---|---|---|---|---|---|---|---|
|**Actividad**|**Actividad**|**Valor**|**Unidad**|**Unidad**|**Cantidad**|**Unidad**|**Unidad**|
|Combustión vehículos<br>Pavimentado Ruta 85|Vehículo liviano|6,06E-02|kg/VKT|0%|75.600|km/año|4,58|
|Combustión vehículos<br>Pavimentado Ruta 85|Camión 3/4 Mantención|2,77E-01|kg/VKT|0%|504|km/año|0,14|
|Combustión vehículos<br>Pavimentado Ruta 85|Aljibe|2,77E-01|kg/VKT|0%|1.008|km/año|0,28|
|Combustión vehículos<br>Pavimentado Ruta 85|Camión 3/4 - Residuos Peligrosos|2,77E-01|kg/VKT|0%|320|km/año|0,09|
|Combustión vehículos<br>Pavimentado Ruta 85|Camión 3/4 - Residuos Domiciliarios|2,77E-01|kg/VKT|0%|3.840|km/año|1,06|
|Combustión vehículos<br>Pavimentado Ruta 5-152|Vehículo liviano|6,06E-02|kg/VKT|0%|406.800|km/año|24,67|
|Combustión vehículos<br>Pavimentado Ruta 5-152|Camión 3/4 Mantención|2,77E-01|kg/VKT|0%|2.712|km/año|0,75|
|Combustión vehículos<br>Pavimentado Ruta 5-152|Aljibe|2,77E-01|kg/VKT|0%|5.424|km/año|1,50|
|Combustión vehículos<br>Pavimentado Ruta 5-152|Camión 3/4 - Residuos Peligrosos|2,77E-01|kg/VKT|0%|904|km/año|0,25|
|Combustión vehículos<br>Pavimentado Ruta 5-152|Camión 3/4 - Residuos Domiciliarios|2,77E-01|kg/VKT|0%|10.848|km/año|3,00|
|Combustión vehículos No<br>Pavimentadas|Vehículo liviano|8,05E-02|kg/VKT|0%|47.880|km/año|3,85|
|Combustión vehículos No<br>Pavimentadas|Camión 3/4 Mantención|4,88E-01|kg/VKT|0%|47.880|km/año|23,36|
|Combustión vehículos No<br>Pavimentadas|Aljibe|4,88E-01|kg/VKT|0%|319|km/año|0,16|
|Combustión vehículos No<br>Pavimentadas|Camión 3/4 - Residuos Peligrosos|4,88E-01|kg/VKT|0%|638|km/año|0,31|
|Combustión vehículos No<br>Pavimentadas|Camión 3/4 - Residuos Domiciliarios|4,88E-01|kg/VKT|0%|106|km/año|0,05|
|Maquinaria fuera de ruta|Grúa pluma|3,87E-02|kg/h|0%|8|h|0,00|
|Grupos electrógenos|Emergencia|7,06E-03|kg/kg comb.|0%|2.631|kg comb.|0,02|
|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**Total (t/año)**|**64,08 **|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 98

**F.6.3. Fase de Cierre**

Las emisiones de contaminantes atmosféricos de la fase de cierre del Proyecto en el peor escenario son

homólogas a la fase de construcción. Estos niveles se presentan en **sección F.6.1** ., **Tabla 56** a **Tabla 62** .

**F.7.** **Resumen de Emisiones de Partículas y Gases**

**F.7.1.Fase de Construcción**

El resumen de las emisiones de MP10, MP2,5, MPS, NOx, CO, SOx y HC debido a las actividades de la fase

de construcción del proyecto Parque Eólico Dañicalqui, sector Parque Eólico (PE), se presenta en **Tabla**

**70** . En esta tabla se puede observar que las emisiones MP10 durante la fase de construcción del Proyecto

alcanzan a aproximadamente a 180 toneladas durante esta fase. Con respecto al MP2,5, las emisiones de

este contaminante alcanzan aproximadamente a 30 toneladas anuales. Por otra parte, las emisiones de

NOx durante la fase de construcción del proyecto alcanzarán a 80 toneladas.

**Tabla 70.** Resumen de emisiones de MP10, MP2,5, MPS, NOx, CO, SOx y HC debido a las actividades de

construcción del Proyecto Parque Eólico Dañicalqui, Sector Parque Eólico (PE).

|Sector|Actividad Fase Construcción|Emisión (t)|Col4|Col5|
|---|---|---|---|---|
|**Sector**|**ActividadFaseConstrucción**|**Año 1**|**Año 2**|**Total**|
|**MP10**|**MP10**|**MP10**|**MP10**|**MP10**|
|Parque Eólico (PE)|Excavaciones|5,07|7,07|12,14|
|Parque Eólico (PE)|Carga y descarga|0,16|0,22|0,38|
|Parque Eólico (PE)|Compactación|0,02|0,03|0,05|
|Parque Eólico (PE)|Escarpe|0,25|0,35|0,59|
|Parque Eólico (PE)|Maquinaria Fuera de ruta|1,44|0,30|1,73|
|Parque Eólico (PE)|Resuspensión caminos Pavimentados|9,94|3,58|13,52|
|Parque Eólico (PE)|Resuspensión caminos No Pavimentados|102,88|44,48|147,35|
|Parque Eólico (PE)|Combustión vehículos|2,12|0,78|2,88|
|Parque Eólico (PE)|Grupos electrógenos|0,63|0,63|1,27|
|Parque Eólico (PE)|**Total**|**122,50**|**57,42**|**179,91**|
|**MP2,5**|**MP2,5**|**MP2,5**|**MP2,5**|**MP2,5**|
|Parque Eólico (PE)|Excavaciones|2,44|3,40|5,85|
|Parque Eólico (PE)|Carga y descarga|0,02|0,03|0,06|
|Parque Eólico (PE)|Compactación|0,01|0,01|0,02|
|Parque Eólico (PE)|Escarpe|0,25|0,35|0,59|
|Parque Eólico (PE)|Maquinaria Fuera de ruta|1,44|0,30|1,73|
|Parque Eólico (PE)|Resuspensión caminos Pavimentados|2,41|0,87|3,27|
|Parque Eólico (PE)|Resuspensión caminos No Pavimentados|10,29|4,45|14,74|
|Parque Eólico (PE)|Combustión vehículos|2,12|0,78|2,88|
|Parque Eólico (PE)|Grupos electrógenos|0,63|0,63|1,27|
|Parque Eólico (PE)|**Total**|**19,60**|**10,82**|**30,40**|
|**MPS**|**MPS**|**MPS**|**MPS**|**MPS**|
|Parque Eólico (PE)|Excavaciones|23,28|32,42|55,70|
|Parque Eólico (PE)|Carga y descarga|0,33|0,46|0,79|
|Parque Eólico (PE)|Compactación|0,10|0,13|0,23|
|Parque Eólico (PE)|Escarpe|0,25|0,35|0,59|
|Parque Eólico (PE)|Maquinaria Fuera de ruta|1,44|0,30|1,73|
|Parque Eólico (PE)|Resuspensión caminos Pavimentados|51,80|18,64|70,43|
|Parque Eólico (PE)|Resuspensión caminos No Pavimentados|336,06|145,29|481,35|
|Parque Eólico (PE)|Combustión vehículos|2,12|0,78|2,88|
|Parque Eólico (PE)|Grupos electrógenos|0,63|0,63|1,27|
|Parque Eólico (PE)|**Total**|**416,00**|**198,99**|**614,98**|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 99

|Sector|Actividad Fase Construcción|Emisión (t)|Col4|Col5|
|---|---|---|---|---|
|**Sector**|**ActividadFaseConstrucción**|**Año 1**|**Año 2**|**Total**|
|**NOx**|**NOx**|**NOx**|**NOx**|**NOx**|
|Parque Eólico (PE)|Maquinaria Fuera de ruta|46,41|7,56|53,96|
|Parque Eólico (PE)|Combustión vehículos|19,39|2,19|7,93|
|Parque Eólico (PE)|Grupos electrógenos|9,01|9,01|18,02|
|Parque Eólico (PE)|**Total**|**74,81**|**18,73**|**79,88**|
|**CO**|**CO**|**CO**|**CO**|**CO**|
|Parque Eólico (PE)|Maquinaria Fuera de ruta|11,91|3,45|15,36|
|Parque Eólico (PE)|Combustión vehículos|3,51|0,42|1,45|
|Parque Eólico (PE)|Grupos electrógenos|1,94|1,94|3,88|
|Parque Eólico (PE)|**Total**|**17,36**|**5,80**|**20,68**|
|**SOx**|**SOx**|**SOx**|**SOx**|**SOx**|
|Parque Eólico (PE)|Maquinaria Fuera de ruta|0,09|0,01|0,10|
|Parque Eólico (PE)|Combustión vehículos|0,06|0,01|0,02|
|Parque Eólico (PE)|Grupos electrógenos|0,59|0,59|1,18|
|Parque Eólico (PE)|**Total**|**0,74**|**0,61**|**1,31**|
|**HC**|**HC**|**HC**|**HC**|**HC**|
|Parque Eólico (PE)|Maquinaria Fuera de ruta|2,87|0,52|3,39|
|Parque Eólico (PE)|Combustión vehículos|771,72|103,44|359,39|
|Parque Eólico (PE)|Grupos electrógenos|0,74|0,74|1,47|
|Parque Eólico (PE)|**Total**|**775,32**|**103,52**|**363,07**|

El resumen de las emisiones de MP10, MP2,5, MPS, NOx, CO, SOx y HC debido a las actividades de la fase

de construcción del proyecto Parque Eólico Dañicalqui, sector Línea de Transmisión (LT), se presenta en

**Tabla 71** . En esta tabla se puede observar que las emisiones de MP10 alcanzan a aproximadamente a 2

toneladas durante este periodo en el sector LT. Con respecto al MP2,5, las emisiones de este

contaminante alcanzan aproximadamente a 1,4 toneladas totales. Por otra parte, las emisiones de NOx

durante la fase de construcción del proyecto alcanzarán a 40 toneladas.

**Tabla 71.** Resumen de emisiones de MP10, MP2,5, MPS, NOx, CO, SOx y HC debido a las actividades de

construcción del Proyecto Parque Eólico Dañicalqui, Sector Línea de Transmisión (LT).

|Sector|Actividad Fase Construcción|Emisión (t)|Col4|Col5|
|---|---|---|---|---|
|**Sector**|**ActividadFaseConstrucción**|**Año 1**|**Año 2**|**Total**|
|**MP10**|**MP10**|**MP10**|**MP10**|**MP10**|
|Línea de Transmisión<br>(LT)|Excavaciones|0,03|0,04|0,07|
|Línea de Transmisión<br>(LT)|Carga y descarga|0,00|0,00|0,00|
|Línea de Transmisión<br>(LT)|Compactación|0,00|0,00|0,00|
|Línea de Transmisión<br>(LT)|Escarpe|0,01|0,01|0,02|
|Línea de Transmisión<br>(LT)|Maquinaria Fuera de ruta|0,35|0,88|1,23|
|Línea de Transmisión<br>(LT)|Resuspensión caminos Pavimentados|0,00|0,11|0,11|
|Línea de Transmisión<br>(LT)|Resuspensión caminos No Pavimentados|0,00|0,24|0,24|
|Línea de Transmisión<br>(LT)|Combustión vehículos|0,00|0,02|0,02|
|Línea de Transmisión<br>(LT)|Erosión eólica|0,01|0,01|0,01|
|Línea de Transmisión<br>(LT)|**Total**|**0,40**|**1,31**|**1,71**|
|**MP2,5**|**MP2,5**|**MP2,5**|**MP2,5**|**MP2,5**|
|Línea de Transmisión<br>(LT)|Excavaciones|0,01|0,02|0,03|
|Línea de Transmisión<br>(LT)|Carga y descarga|0,00|0,00|0,00|
|Línea de Transmisión<br>(LT)|Compactación|0,00|0,00|0,00|
|Línea de Transmisión<br>(LT)|Escarpe|0,01|0,01|0,02|
|Línea de Transmisión<br>(LT)|Maquinaria Fuera de ruta|0,35|0,88|1,23|
|Línea de Transmisión<br>(LT)|Resuspensión caminos Pavimentados|0,00|0,03|0,03|
|Línea de Transmisión<br>(LT)|Resuspensión caminos No Pavimentados|0,00|0,02|0,02|
|Línea de Transmisión<br>(LT)|Combustión vehículos|0,00|0,02|0,02|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 100

|Sector|Actividad Fase Construcción|Emisión (t)|Col4|Col5|
|---|---|---|---|---|
|**Sector**|**ActividadFaseConstrucción**|**Año 1**|**Año 2**|**Total**|
|**Sector**|Erosión eólica|0,02|0,02|0,02|
|**Sector**|**Total**|**0,39**|**1,00**|**1,38**|
|**MPS**|**MPS**|**MPS**|**MPS**|**MPS**|
|Línea de Transmisión<br>(LT)|Excavaciones|0,13|0,19|0,32|
|Línea de Transmisión<br>(LT)|Carga y descarga|0,00|0,00|0,01|
|Línea de Transmisión<br>(LT)|Compactación|0,00|0,00|0,01|
|Línea de Transmisión<br>(LT)|Escarpe|0,01|0,01|0,02|
|Línea de Transmisión<br>(LT)|Maquinaria Fuera de ruta|0,35|0,88|1,23|
|Línea de Transmisión<br>(LT)|Resuspensión caminos Pavimentados|0,00|0,59|0,59|
|Línea de Transmisión<br>(LT)|Resuspensión caminos No Pavimentados|0,00|0,78|0,78|
|Línea de Transmisión<br>(LT)|Combustión vehículos|0,00|0,02|0,02|
|Línea de Transmisión<br>(LT)|Erosión eólica|0,02|0,02|0,02|
|Línea de Transmisión<br>(LT)|**Total**|**0,52**|**2,49**|**3,00**|
|**NOx**|**NOx**|**NOx**|**NOx**|**NOx**|
|Línea de Transmisión<br>(LT)|Maquinaria Fuera de ruta|11,53|28,19|39,72|
|Línea de Transmisión<br>(LT)|Combustión vehículos|0,00|0,03|0,03|
|Línea de Transmisión<br>(LT)|**Total**|**11,53**|**28,22**|**39,75**|
|**CO**|**CO**|**CO**|**CO**|**CO**|
|Línea de Transmisión<br>(LT)|Maquinaria Fuera de ruta|2,93|7,74|10,66|
|Línea de Transmisión<br>(LT)|Combustión vehículos|0,00|0,01|0,01|
|Línea de Transmisión<br>(LT)|**Total**|**2,93**|**7,74**|**10,67**|
|**SOx**|**SOx**|**SOx**|**SOx**|**SOx**|
|Línea de Transmisión<br>(LT)|Maquinaria Fuera de ruta|0,02|0,05|0,08|
|Línea de Transmisión<br>(LT)|Combustión vehículos|0,00|0,00|0,00|
|Línea de Transmisión<br>(LT)|**Total**|**0,02**|**0,05**|**0,08**|
|**HC**|**HC**|**HC**|**HC**|**HC**|
|Línea de Transmisión<br>(LT)|Maquinaria Fuera de ruta|0,71|1,79|2,50|
|Línea de Transmisión<br>(LT)|Combustión vehículos|0,00|1,18|1,18|
|Línea de Transmisión<br>(LT)|**Total**|**0,71**|**2,97**|**3,68**|

En **Tabla 72** se presenta el resumen de las emisiones de MP10, MP2,5, MPS, NOx, CO, SOx y HC de la fase

de construcción del proyecto Parque Eólico Dañicalqui. En esta tabla se puede observar que el año que

presenta las más altas emisiones corresponde al primer año de construcción para todos los contaminantes

considerados.

**Tabla 72.** Resumen de emisiones de MP10, MP2,5, MPS, NOx, CO, SOx y HC de la fase de construcción

del Proyecto Parque Eólico Dañicalqui.

|Contaminante|Emisión (t)|Col3|Col4|
|---|---|---|---|
|**Contaminante**|**Año 1**|**Año 2**|**Total**|
|**MP10**|122,91|58,74|181,61|
|**MP2,5**|20,00|11,82|31,78|
|**MPS**|416,52|201,49|617,97|
|**NOx**|86,33|46,96|119,63|
|**CO**|20,29|13,54|31,35|
|**SOx**|0,76|0,67|1,39|
|**HC**|776,03|106,79|367,05|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 101

**F.7.2. Fase de Operación**

El resumen de las emisiones de MP10, MP2,5, MPS, NOx, CO, SOx y HC debido a las actividades de

operación del proyecto Parque Eólico Dañicalqui se presenta en **Tabla 73** . Los valores presentados en esta

tabla son en base anual.

**Tabla 73.** Resumen de emisiones de MP10, MP2,5, MPS, NOx, CO, SOx y HC debido a las actividades de

construcción del Proyecto Parque Eólico Dañicalqui, Sector Parque Eólico (PE).

|Actividad Fase Operación|Emisión (t/año)|
|---|---|
|**MP10**|**MP10**|
|Resuspensión caminos Pavimentados|0,22|
|Resuspensión caminos No Pavimentados|7,78|
|Combustión vehículos|0,09|
|Maquinaria Fuera de ruta|0,00|
|Grupos electrógenos|0,02|
|**Total**|**8,11**|
|**MP2,5**|**MP2,5**|
|Resuspensión caminos Pavimentados|0,05|
|Resuspensión caminos No Pavimentados|0,78|
|Combustión vehículos|0,09|
|Maquinaria Fuera de ruta|0,00|
|Grupos electrógenos|0,02|
|**Total**|**0,94**|
|**MPS**|**MPS**|
|Resuspensión caminos Pavimentados|1,14|
|Resuspensión caminos No Pavimentados|25,42|
|Combustión vehículos|0,09|
|Maquinaria Fuera de ruta|0,00|
|Grupos electrógenos|0,02|
|**Total**|**26,67**|
|**NOx**|**NOx**|
|Combustión vehículos|1,12|
|Maquinaria Fuera de ruta|0,00|
|Grupos electrógenos|0,23|
|**Total**|**1,36**|
|**CO**|**CO**|
|Combustión vehículos|0,30|
|Maquinaria Fuera de ruta|0,00|
|Grupos electrógenos|0,05|
|**Total**|**0,35**|
|**SOx**|**SOx**|
|Combustión vehículos|0,01|
|Maquinaria Fuera de ruta|0,00|
|Grupos electrógenos|0,01|
|**Total**|**0,02**|
|**HC**|**HC**|
|Combustión vehículos|64,06|
|Maquinaria Fuera de ruta|0,00|
|Grupos electrógenos|0,02|
|**Total**|**64,08**|

En **Tabla 74** se presenta el resumen de las emisiones de MP10, MP2,5, MPS, NOx, CO, SOx y HC de la fase

de operación del proyecto Parque Eólico Dañicalqui. En esta tabla se puede observar que las emisiones

de MP10 alcanzan a aproximadamente 8 toneladas anuales y las emisiones de MP2,5 llegarán a

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 102

aproximadamente 1 t/año. Con respecto al NOx durante la operación, las emisiones de este contaminante

alcanzan a 1 toneladas anual.

**Tabla 74.** Resumen de emisiones de MP10, MP2,5, MPS, NOx, CO, SOx y HC de la fase de operación del

Proyecto Parque Eólico Dañicalqui.

**F.7.3. Fase de Cierre**

|Contaminante|Emisión (t/año)|
|---|---|
|MP10|8,11|
|MP2,5|0,94|
|MPS|26,67|
|NOx|1,36|
|CO|0,35|
|SOx|0,020|
|HC|64,08|

El resumen de las emisiones de MP10, MP2,5, MPS, NOx, CO, SOx y HC de la fase de cierre del proyecto

Parque Eólico Dañicalqui se presenta en **Tabla 75** .

**Tabla 75.** Resumen de emisiones de MP10, MP2,5, MPS, NOx, CO, SOx y HC de la fase de cierre del

Proyecto Parque Eólico Dañicalqui.

|Contaminante|Emisión (t)|Col3|Col4|
|---|---|---|---|
|**Contaminante**|**Año 1**|**Año 2**|**Total**|
|**MP10**|123,54|59,37|182,88|
|**MP2,5**|20,63|12,45|33,05|
|**MPS**|417,15|202,12|619,24|
|**NOx**|95,34|55,97|137,65|
|**CO**|22,23|15,49|35,23|
|**SOx**|1,35|1,26|2,57|
|**HC**|776,77|107,52|368,52|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 103

**G.** **IMPLEMENTACIÓN, APLICACIÓN Y RESULTADOS DEL MODELO DE DISPERSIÓN CALPUFF**

**G.1** **Introducción**

El sistema de modelación CALPUFF, está actualmente aprobado por el Servicio de Evaluación Ambiental

(SEA) de Chile y por la EPA (USA) como modelo regulatorio para evaluar el impacto de emisiones

atmosféricas en escenarios de terreno y meteorología compleja. Este sistema está compuesto por los

modelos WRF y CALPUFF, cuya descripción general es la siguiente:

El sistema de modelación CALPUFF, está actualmente aprobado por el Servicio de Evaluación Ambiental

(SEA) de Chile y por la EPA (USA) como modelo regulatorio para evaluar el impacto de emisiones

atmosféricas en escenarios de terreno y meteorología compleja. Este sistema está compuesto por los

modelos WRF y CALPUFF, cuya descripción general es la siguiente:

 - WRF: Modelo de mesoescala y micrometeorológico capaz de generar la meteorología requerida

por el modelo CALPUFF con resolución de 1 km, para la evaluación de contaminantes primarios.

 - CALPUFF: Modelo lagrangiano de dispersión tipo puff que permite simular el transporte,

dispersión e impacto de emisiones de contaminantes primarios de procesos naturales y

antropogénicos, utilizando la meteorología generada por WRF.

El análisis de resultados de los modelos WRF y CALPUFF se realiza con el software CalDESK Advanced

v2.99 [2] . Esta herramienta permite generar mapas de isoconcentraciones de contaminantes y visualizar los

resultados de todas las variables entregadas por los modelos.

En **Figura 21** se presenta un diagrama del sistema CALPUFF, donde se ilustran los diferentes archivos de

entrada requeridos por los modelos WRF y CALPUFF. Como se observa en esta figura, WRF requiere la

topografía y usos de suelos locales, junto con la meteorología proporcionada por el sistema GFS. Por otra

parte, CALPUFF requiere, la meteorología generada por WRF con el formato de CALMET (calmet.dat) y la

información de emisiones, entregada en el Inventario de Emisiones ( **Sección F** ).

2: Software de visualización y Análisis para el sistema CALPUFF, desarrollado por EnviroModeling SpA..

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 104

**Figura 21.** Diagrama de operación del sistema de modelación WRF/CALPUFF/CalDesk.

**G.2** **Implementación y Aplicación del Modelo de Dispersión CALPUFF**

El modelo de dispersión CALPUFF se implementó en la zona de estudio utilizando el un dominio levemente

menor al de WRF descrito en la **Sección E.2** . El dominio utilizado se presenta en **Tabla 76**, el que cubre un

área de 95 x 95 km [2] con una resolución de 1 km y que se muestra en **Figura 22** .

**Tabla 76.** Características del dominio de modelación utilizada por el modelo CALPUFF en la zona del

Proyecto Parque Eólico Dañicalqui (archivo CALPUFF-Ready).

|Características dominio CALPUFF-Ready|Col2|
|---|---|
|Resolución|1.000 x 1.000 (m)|
|No de celdas en dirección X|95|
|No de celdas en dirección Y|95|
|Coordenadas de referencia del origen del dominio*|UTM-E: 692.336 (m), UTM-N: 5.862.889 (m).|
|Total del área del dominio|9.025 (km2)|

_*:_ _Coordenada de referencia en UTM datum WGS 84 (aproximada), el dominio corresponde a la segunda grilla anidada_

_en la implementación del modelo WRF, la cual está en proyección Lambert Conformal Conic (LCC)._

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 105

**Figura 22.** Dominio de modelación de CALPUFF, 95 x 95 km [2], en coordenadas LCC.

**G.2.1.** **Receptores de Grilla y Discretos**

Como se mencionó anteriormente el modelo CALPUFF se implementó en un área de 95 x 95 km [2] con

resolución de 1 km. Sin embargo, las concentraciones en receptores de grilla se calcularon en un área un

poco menor de 80 x 73 km [2] . De esta forma CALPUFF entregó concentraciones para un área aproximada

de 5.840 km [2] . En esta área además se dio un factor de anidamiento de 4, lo que implica que el modelo

calcula concentraciones cada 250 metros. Las características del área de receptores tipo grilla se

presentan en **Tabla 77** se muestra en **Figura 23** .

**Tabla 77.** Características del área de receptores de Grilla.

|Item|Características|
|---|---|
|Kilómetros en dirección X|80|
|Kilómetros en dirección Y|73|
|Factor de anidamiento de la cuadrícula de receptores|4|
|Celdas de receptores en X|320|
|Celdas de receptores en Y|292|
|Resolución|250 m|
|Coordenadas de referencia del origen del dominio*|UTM-E: 692.736 (m), UTM-N: 5.876.884 (m)|
|Total de receptores|93.440|

_*:_ _Coordenada de referencia en UTM datum WGS 84 (aproximada), el dominio está en proyección Lambert Conformal_

_Conic (LCC)._

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 106

**Figura 23.** Área de receptores de grilla de CALPUFF, 80 x 73 km [2], en coordenadas LCC.

Para evaluar las emisiones atmosféricas del Proyecto, se identificaron 455 potenciales receptores, sin

embargo, se consideran 73 receptores sensibles los cuales son los más representativos para la evaluación

y 2 estaciones de monitoreo de calidad de aire cercanas al Proyecto (SAPU y Quinel), que, si bien no son

receptores sensibles, se incluyen ya que aportan con información de caracterización basal. En la **Tabla 78**,

en la primera columna se muestra el número del receptor (R1 al R75) para el análisis del presente informe

y en la segunda columna la nomenclatura de los receptores (ID Proyecto) para mantener coherencia con

otras evaluaciones realizadas en el marco de la DIA, además se presenta la ubicación de los receptores,

coordenadas UTM y LCC, y altitud. La ubicación de los receptores de interés alrededor del Proyecto se

muestra en **Figura 24** .

Es importante mencionar que los resultados obtenidos mediante receptores discretos son valores

calculados por el modelo en el punto de interés, es decir, tiene una precisión mayor con respecto a los

resultados de grilla, donde los resultados son interpolados para entregar las concentraciones en todo el

dominio de modelación.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 107

**Tabla 78.** Coordenadas de receptores de interés en la zona del Proyecto.

|Receptor|ID Proyecto|UTM (WGS 84 - Z18)|Col4|Altitud (1)<br>(m.s.n.m.)|LCC (km)|Col7|
|---|---|---|---|---|---|---|
|**Receptor **|**ID Proyecto**|**Este (m)**|**Norte (m)**|**Norte (m)**|**LCC-X**|**LCC-Y**|
|R1|454|755,802|5,900,928|191.9|14.840|-7.673|
|R2|456|755,827|5,900,931|192.0|14.865|-7.669|
|R3|455|755,793|5,900,916|191.9|14.832|-7.685|
|R4|472|755,779|5,900,954|191.8|14.817|-7.648|
|R5|457-2|756,759|5,902,009|200.4|15.766|-6.566|
|R6|463|756,843|5,902,240|202.2|15.843|-6.332|
|R7|465|756,669|5,902,273|201.1|15.668|-6.304|
|R8|458|756,911|5,902,149|202.3|15.914|-6.421|
|R9|461|756,877|5,902,226|202.4|15.877|-6.345|
|R10|462|756,814|5,902,217|201.9|15.815|-6.356|
|R11|464|756,817|5,902,245|202.1|15.817|-6.328|
|R12|460|756,957|5,902,171|202.7|15.959|-6.398|
|R13|469|757,039|5,902,557|205.4|16.030|-6.010|
|R14|470|757,645|5,903,090|209.0|16.620|-5.460|
|R15|466|757,022|5,902,308|203.9|16.020|-6.259|
|R16|471|757,645|5,903,225|208.8|16.616|-5.325|
|R17|467|757,213|5,902,386|205.8|16.209|-6.176|
|R18|468|757,269|5,902,522|206.9|16.261|-6.039|
|R19|459|756,904|5,902,117|202.1|15.908|-6.454|
|R20|3|748,661|5,900,584|151.8|7.715|-8.220|
|R21|4|748,803|5,900,580|152.6|7.857|-8.220|
|R22|5|748,763|5,900,452|152.7|7.820|-8.349|
|R23|8|750,709|5,900,420|168.2|9.766|-8.325|
|R24|14|750,553|5,900,372|166.7|9.611|-8.378|
|R25|36|750,336|5,900,339|164.9|9.395|-8.417|
|R26|43|750,488|5,900,312|166.0|9.548|-8.440|
|R27|71|750,469|5,900,229|165.5|9.531|-8.523|
|R28|79|750,838|5,900,180|168.1|9.902|-8.562|
|R29|92|750,714|5,900,127|166.9|9.779|-8.618|
|R30|94|750,384|5,900,124|164.4|9.449|-8.630|
|R31|99|751,015|5,900,089|168.9|10.081|-8.648|
|R32|128|751,156|5,899,785|168.3|10.231|-8.947|
|R33|133|750,804|5,899,756|165.9|9.880|-8.986|
|R34|149|751,033|5,899,593|166.8|10.113|-9.143|
|R35|150|751,072|5,899,592|167.0|10.152|-9.142|
|R36|158|751,100|5,899,565|167.1|10.181|-9.169|
|R37|160|751,142|5,899,530|167.2|10.224|-9.202|
|R38|164|753,860|5,899,456|177.9|12.942|-9.199|
|R39|177|753,773|5,899,258|176.1|12.860|-9.399|
|R40|188|753,841|5,899,096|175.2|12.933|-9.559|
|R41|197|752,501|5,898,493|170.3|11.611|-10.200|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 108

|Receptor|ID Proyecto|UTM (WGS 84 - Z18)|Col4|Altitud (1)<br>(m.s.n.m.)|LCC (km)|Col7|
|---|---|---|---|---|---|---|
|**Receptor **|**ID Proyecto**|**Este (m)**|**Norte (m)**|**Norte (m)**|**LCC-X**|**LCC-Y**|
|R42|198|752,017|5,898,469|169.6|11.128|-10.238|
|R43|204|754,451|5,898,163|174.3|13.569|-10.474|
|R44|210|753,543|5,898,066|172.0|12.665|-10.597|
|R45|211|754,592|5,898,058|174.5|13.713|-10.575|
|R46|214|752,308|5,898,048|170.6|11.431|-10.650|
|R47|218|753,710|5,898,021|172.1|12.833|-10.637|
|R48|221|753,606|5,897,637|172.7|12.740|-11.024|
|R49|228|758,569|5,897,194|203.4|17.711|-11.325|
|R50|231|753,429|5,896,875|180.1|12.585|-11.790|
|R51|242|752,846|5,896,361|181.5|12.017|-12.320|
|R52|250|753,671|5,896,045|186.2|12.850|-12.613|
|R53|256|749,573|5,895,051|178.5|8.784|-13.723|
|R54|261|749,649|5,895,023|178.7|8.860|-13.748|
|R55|262|749,617|5,895,011|178.7|8.829|-13.761|
|R56|271|749,798|5,894,961|179.2|9.011|-13.806|
|R57|272|749,833|5,894,939|179.3|9.047|-13.827|
|R58|307|749,130|5,894,595|178.0|8.354|-14.191|
|R59|318|750,616|5,894,414|180.5|9.844|-14.329|
|R60|319|750,707|5,894,410|180.5|9.935|-14.331|
|R61|320|750,780|5,894,407|180.6|10.008|-14.332|
|R62|326|756,906|5,894,377|193.5|16.130|-14.187|
|R63|328|750,912|5,894,370|180.6|10.141|-14.365|
|R64|336|757,061|5,894,326|193.9|16.286|-14.234|
|R65|357|756,901|5,894,133|194.2|16.132|-14.431|
|R66|368|751,225|5,894,088|181.2|10.462|-14.638|
|R67|377|756,578|5,894,040|194.7|15.812|-14.533|
|R68|396|756,507|5,893,979|195.0|15.743|-14.596|
|R69|417|751,383|5,893,873|181.8|10.626|-14.848|
|R70|425|751,463|5,893,769|182.1|10.709|-14.950|
|R71|452|756,834|5,893,033|197.5|16.096|-15.532|
|R72|453|752,338|5,897,766|171.2|11.469|-10.931|
|R73|238|752,861|5,896,368|181.6|12.031|-12.313|
|R74|Estación SAPU|731,369|5,897,676|132.2|-9.482|-11.618|
|R75|Estación Quinel|730,529|5,898,723|131.2|-10.351|-10.595|

_1:_ _Altitud a utilizar en CALPUFF obtenida del terreno entregado por el modelo WRF en el formato CALMET._

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 109

**Figura 24.** Ubicación de Receptores de interés alrededor del Proyecto.

**G.2.2.** **Implementación de Fuentes Emisoras de Contaminantes**

La aplicación del modelo CALPUFF para el periodo meteorológico del año 2021 consideró el escenario de

emisiones de la fase de Construcción actualizado del proyecto Parque Eólico Dañicalqui presentado en

**Sección F.6.1.,** para el año 1 por ser el de mayores emisiones de contaminantes atmosféricos, es decir, el

peor escenario de emisiones. La fase de Operación no se considera en la modelación debido a que son

emisiones muy menores con respecto a las de construcción, por lo tanto, el mayor impacto del Proyecto

es en la fase de Construcción.

Las emisiones implementadas en CALPUFF para el primer año de escenario de construcción del Proyecto

se presentan en **Tabla 79** . Las emisiones de área corresponden a la distribución de las emisiones de

excavaciones, escarpe, compactación, carguío de material, descarga en relleno y maquinaria fuera de ruta,

presentadas en **Sección F.6.1**, las que se implementaron como fuentes de área en el lugar de

emplazamiento del proyecto. Por otro lado, la resuspensión por tránsito de vehículos por caminos

pavimentados y no pavimentados y combustión de vehículos se implementaron como fuentes de rutas.

La fuente zanja, al ser lineal también se implementó como una ruta.

Por otra parte, las emisiones de NO 2 se consideraron como el 10% del total de NOx y como escenario de

emisiones más conservador se consideraron en la modelación todas las emisiones de SOx como SO 2 .

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 110

Las fuentes de área se definieron utilizando polígonos para cubrir el área abarcada por cada fuente.

**Tabla 79.** Emisiones de MP10, MP2,5, MPS, NO 2, SO 2 y CO del primer año de construcción del Proyecto

Parque Eólico Dañicalqui.

|Sector|Fuente|Emisión contaminante (kg/año)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Sector**|**Fuente**|**MP10**|**MP2,5**|**MPS**|**NO2 **|**SO2 **|**CO**|
|**PE**|Para todas las áreas|5.940,97|3.605,20|21.705,40|4.611,14|89,21|11.709,26|
|**PE**|Fundaciones|642,60|305,81|2.920,10||||
|**PE**|Puente Río Dañicalqui|9,45|4,50|42,93||||
|**PE**|Puente Estero Culenco|1,24|0,59|5,66||||
|**PE**|Puente Canal|1,66|0,79|7,54||||
|**PE**|Obras de Arte|2,13|1,02|9,69||||
|**PE**|Instalación de faenas|649,75|649,08|654,34|900,85|592,39|1.940,58|
|**PE**|Planta de Hormigón|9,41|9,03|12,03|0,00|0,00|0,00|
|**PE**|Estación elevadora|4,70|4,51|6,01|0,00|0,00|0,00|
|**PE**|Plataformas|99,87|95,85|127,68||||
|**PE**|Zanja Circuiros MT|85,86|49,83|329,56|29,51|0,44|198,84|
|**PE**|Resuspensión caminos Pavimentados - Ruta 85|1.663,21|402,39|8.664,79||||
|**PE**|Resuspensión caminos Pavimentados - Rutas 5 y 152|8.279,42|2.003,08|43.133,09||||
|**PE**|Resuspensión caminos No Pavimentados**CS-EX**|1.931,28|193,13|6.308,86||||
|**PE**|Resuspensión caminos No Pavimentados**CS-IN**|509,87|53,03|1.660,85||||
|**PE**|Resuspensión caminos No Pavimentados**SS-EX**|38.586,01|3.858,60|126.047,62||||
|**PE**|Resuspensión caminos No Pavimentados**SS-IN**|61.912,77|6.244,17|202.126,08||||
|**PE**|Combustión Pavimentados 80 km/h|323,09|323,09|323,09|281,81|8,23|511,84|
|**PE**|Combustión No Pavimentados 40 km/h|183,82|183,82|183,82|254,41|7,34|452,85|
|**PE**|Combustión 30 km/h|0,00|0,00|0,00|0,00|0,00|0,00|
|**PE**|Combustión caminos Pavimentados - Rutas 5 y 152|0,00|0,00|0,00|0,00|0,00|0,00|
|**PE**|**Sub-Total**|**120.837,10**|**17.987,52**|**414.269,11**|**6.077,73**|**697,61**|**14.813,36**|
|**LT**|Torres LT|30,60|14,56|139,06||||
|**LT**|Torres y acopio (ZA)|363,50|363,50|363,50|1.152,78|22,30|2.927,31|
|**LT**|Acopio (ZA)|66,80|24,35|140,35||||
|**LT**|Resuspensión caminos Pavimentados - Ruta 85|0,00|0,00|0,00||||
|**LT**|Resuspensión caminos Pavimentados - Rutas 5 y 152|0,00|0,00|0,00||||
|**LT**|Resuspensión caminos No Pavimentados**CS-EX**|0,00|0,00|0,00||||
|**LT**|Resuspensión caminos No Pavimentados**SS-EX**|0,00|0,00|0,00||||
|**LT**|Combustión Pavimentados 80 km/h|0,00|0,00|0,00|0,00|0,00|0,00|
|**LT**|Combustión No Pavimentados 40 km/h|0,00|0,00|0,00|0,00|0,00|0,00|
|**LT**|Combustión 30 km/h|0,00|0,00|0,00|0,00|0,00|0,00|
|**LT**|Combustión caminos Pavimentados - Rutas 5 y 152|1.608,32|1.608,32|1.608,32|1.402,85|40,98|2.547,91|
|**LT**|**Sub-Total**|**2.069,22**|**2.010,74**|**2.251,23**|**2.555,64**|**63,28**|**5.475,23**|
|**Total**|**Total**|**122.906,32**|**19.998,26**|**416.520,35**|**8.633,37**|**760,88**|**20.288,58**|

Las fuentes presentadas en **Tabla 79** se implementaron en el modelo CALPUFF como áreas y tramos de

zanja y rutas considerando las coordenadas que se muestran en **Tabla 80** a **Tabla 82**, respectivamente, en

coordenadas UTM y su correspondiente coordenada Lambert Conformal Conic (LCC).

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 111

**Tabla 80.** Coordenadas de las áreas donde se implementaron las fuentes emisoras de contaminantes

atmosféricos en el modelo CALPUFF.

|Sector|Fuente|Superficie<br>(m2)|Punto|UTM (WGS 84 - Z18)|Col6|LCC (m)|Col8|
|---|---|---|---|---|---|---|---|
|**Sector**|**Fuente**|**Superficie**<br>**(m2) **|**Punto**|**Este (m)**|**Norte (m)**|**LCC-X**|**LCC-Y**|
|**PE**|Estacionamiento SE|140|1|750.341|5.897.953|9.468|-10.801|
|**PE**|Estacionamiento SE|140|2|750.332|5.897.932|9.460|-10.823|
|**PE**|Estacionamiento SE|140|3|750.338|5.897.929|9.466|-10.825|
|**PE**|Estacionamiento SE|140|4|750.347|5.897.951|9.474|-10.803|
|**PE**|Instalación de Faenas-1|7.446|1|754.453|5.897.039|13.603|-11.598|
|**PE**|Instalación de Faenas-1|7.446|2|754.479|5.897.105|13.627|-11.530|
|**PE**|Instalación de Faenas-1|7.446|3|754.380|5.897.151|13.526|-11.487|
|**PE**|Instalación de Faenas-1|7.446|4|754.369|5.897.072|13.518|-11.567|
|**PE**|Instalación de Faenas-2|5.231|1|754.380|5.897.151|13.526|-11.487|
|**PE**|Instalación de Faenas-2|5.231|2|754.306|5.897.138|13.453|-11.503|
|**PE**|Instalación de Faenas-2|5.231|3|754.277|5.897.092|13.426|-11.549|
|**PE**|Instalación de Faenas-2|5.231|4|754.369|5.897.072|13.518|-11.567|
|**PE**|Instalación de Faenas-3|5.248|1|754.277|5.897.092|13.426|-11.549|
|**PE**|Instalación de Faenas-3|5.248|2|754.308|5.897.001|13.459|-11.639|
|**PE**|Instalación de Faenas-3|5.248|3|754.334|5.896.985|13.486|-11.655|
|**PE**|Instalación de Faenas-3|5.248|4|754.369|5.897.072|13.518|-11.567|
|**PE**|Planta de Hormigón|10.218|1|754.453|5.897.039|13.603|-11.598|
|**PE**|Planta de Hormigón|10.218|2|754.369|5.897.072|13.518|-11.567|
|**PE**|Planta de Hormigón|10.218|3|754.334|5.896.985|13.486|-11.655|
|**PE**|Planta de Hormigón|10.218|4|754.403|5.896.915|13.557|-11.722|
|**PE**|Subestación|4.991|1|750.285|5.897.991|9.411|-10.764|
|**PE**|Subestación|4.991|2|750.255|5.897.922|9.384|-10.834|
|**PE**|Subestación|4.991|3|750.317|5.897.896|9.446|-10.858|
|**PE**|Subestación|4.991|4|750.346|5.897.966|9.473|-10.788|
|**PE**|Puente Río Dañicalqui|2.050|1|753.776|5.897.217|12.922|-11.438|
|**PE**|Puente Río Dañicalqui|2.050|2|753.801|5.897.208|12.947|-11.447|
|**PE**|Puente Río Dañicalqui|2.050|3|753.827|5.897.282|12.971|-11.373|
|**PE**|Puente Río Dañicalqui|2.050|4|753.803|5.897.291|12.946|-11.364|
|**PE**|Puente Estero Culenco|479|1|755.695|5.900.820|14.736|-7.784|
|**PE**|Puente Estero Culenco|479|2|755.680|5.900.798|14.722|-7.806|
|**PE**|Puente Estero Culenco|479|3|755.693|5.900.787|14.736|-7.817|
|**PE**|Puente Estero Culenco|479|4|755.710|5.900.812|14.751|-7.792|
|**PE**|Puente Canal|392|1|750.365|5.897.512|9.505|-11.241|
|**PE**|Puente Canal|392|2|750.363|5.897.498|9.503|-11.255|
|**PE**|Puente Canal|392|3|750.395|5.897.496|9.535|-11.256|
|**PE**|Puente Canal|392|4|750.393|5.897.508|9.533|-11.244|
|**PE**|Obra de Arte 1|526|1|751.698|5.897.155|10.847|-11.560|
|**PE**|Obra de Arte 1|526|2|751.703|5.897.136|10.853|-11.579|
|**PE**|Obra de Arte 1|526|3|751.731|5.897.142|10.880|-11.572|
|**PE**|Obra de Arte 1|526|4|751.725|5.897.160|10.874|-11.554|
|**PE**|Obra de Arte 2|224|1|754.381|5.896.876|13.536|-11.762|
|**PE**|Obra de Arte 2|224|2|754.393|5.896.885|13.548|-11.753|
|**PE**|Obra de Arte 2|224|3|754.384|5.896.897|13.539|-11.741|
|**PE**|Obra de Arte 2|224|4|754.373|5.896.887|13.527|-11.751|
|**PE**|Obra de Arte 3|297|1|754.373|5.896.505|13.538|-12.133|
|**PE**|Obra de Arte 3|297|2|754.387|5.896.501|13.552|-12.137|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 112

|Sector|Fuente|Superficie<br>(m2)|Punto|UTM (WGS 84 - Z18)|Col6|LCC (m)|Col8|
|---|---|---|---|---|---|---|---|
|**Sector**|**Fuente**|**Superficie**<br>**(m2) **|**Punto**|**Este (m)**|**Norte (m)**|**LCC-X**|**LCC-Y**|
|**Sector**|**Fuente**|**Superficie**<br>**(m2) **|3|754.384|5.896.523|13.549|-12.115|
|**Sector**|**Fuente**|**Superficie**<br>**(m2) **|4|754.370|5.896.527|13.534|-12.111|
|**Sector**|Obra de Arte 4|520|1|755.779|5.895.420|14.974|-13.177|
|**Sector**|Obra de Arte 4|520|2|755.794|5.895.433|14.988|-13.164|
|**Sector**|Obra de Arte 4|520|3|755.783|5.895.458|14.977|-13.139|
|**Sector**|Obra de Arte 4|520|4|755.768|5.895.445|14.962|-13.152|
|**Sector**|Obra de Arte 5|560|1|755.769|5.895.942|14.950|-12.656|
|**Sector**|Obra de Arte 5|560|2|755.793|5.895.939|14.973|-12.658|
|**Sector**|Obra de Arte 5|560|3|755.795|5.895.961|14.975|-12.636|
|**Sector**|Obra de Arte 5|560|4|755.770|5.895.965|14.949|-12.633|
|**Sector**|Obra de Arte 6|620|1|754.821|5.898.549|13.928|-10.078|
|**Sector**|Obra de Arte 6|620|2|754.819|5.898.571|13.925|-10.056|
|**Sector**|Obra de Arte 6|620|3|754.790|5.898.566|13.896|-10.062|
|**Sector**|Obra de Arte 6|620|4|754.796|5.898.543|13.903|-10.085|
|**Sector**|AG-1 Plataforma AA-1|1.533,4|1|750.342|5.897.534|9.481|-11.220|
|**Sector**|AG-1 Plataforma AA-1|1.533,4|2|750.353|5.897.536|9.492|-11.217|
|**Sector**|AG-1 Plataforma AA-1|1.533,4|3|750.316|5.897.664|9.452|-11.090|
|**Sector**|AG-1 Plataforma AA-1|1.533,4|4|750.305|5.897.661|9.440|-11.094|
|**Sector**|AG-1 Plataforma AA-2|527,6|1|750.348|5.897.552|9.487|-11.202|
|**Sector**|AG-1 Plataforma AA-2|527,6|2|750.354|5.897.553|9.493|-11.200|
|**Sector**|AG-1 Plataforma AA-2|527,6|3|750.330|5.897.638|9.466|-11.116|
|**Sector**|AG-1 Plataforma AA-2|527,6|4|750.324|5.897.636|9.461|-11.118|
|**Sector**|AG-1 Plataforma-1|3.676,6|1|750.245|5.897.644|9.381|-11.112|
|**Sector**|AG-1 Plataforma-1|3.676,6|2|750.263|5.897.580|9.401|-11.176|
|**Sector**|AG-1 Plataforma-1|3.676,6|3|750.316|5.897.594|9.454|-11.160|
|**Sector**|AG-1 Plataforma-1|3.676,6|4|750.298|5.897.659|9.434|-11.096|
|**Sector**|AG-1 Plataforma-2|2.404|1|750.287|5.897.586|9.425|-11.169|
|**Sector**|AG-1 Plataforma-2|2.404|2|750.330|5.897.457|9.471|-11.297|
|**Sector**|AG-1 Plataforma-2|2.404|3|750.344|5.897.461|9.485|-11.293|
|**Sector**|AG-1 Plataforma-2|2.404|4|750.307|5.897.592|9.444|-11.163|
|**Sector**|AG-1 Fundación|1.009|1|750.298|5.897.659|9.433|-11.096|
|**Sector**|AG-1 Fundación|1.009|2|750.286|5.897.686|9.421|-11.070|
|**Sector**|AG-1 Fundación|1.009|3|750.255|5.897.677|9.390|-11.080|
|**Sector**|AG-1 Fundación|1.009|4|750.259|5.897.649|9.395|-11.107|
|**Sector**|AG-2 Plataforma AA-1|1.462,9|1|750.443|5.897.503|9.584|-11.248|
|**Sector**|AG-2 Plataforma AA-1|1.462,9|2|750.419|5.897.502|9.559|-11.250|
|**Sector**|AG-2 Plataforma AA-1|1.462,9|3|750.538|5.897.442|9.679|-11.306|
|**Sector**|AG-2 Plataforma AA-1|1.462,9|4|750.543|5.897.453|9.685|-11.295|
|**Sector**|AG-2 Plataforma AA-2|524,5|1|750.430|5.897.489|9.571|-11.262|
|**Sector**|AG-2 Plataforma AA-2|524,5|2|750.509|5.897.450|9.651|-11.299|
|**Sector**|AG-2 Plataforma AA-2|524,5|3|750.512|5.897.455|9.653|-11.294|
|**Sector**|AG-2 Plataforma AA-2|524,5|4|750.433|5.897.495|9.573|-11.256|
|**Sector**|AG-2 Plataformas-1|3.676,6|1|750.571|5.897.508|9.711|-11.239|
|**Sector**|AG-2 Plataformas-1|3.676,6|2|750.511|5.897.538|9.650|-11.211|
|**Sector**|AG-2 Plataformas-1|3.676,6|3|750.486|5.897.489|9.626|-11.260|
|**Sector**|AG-2 Plataformas-1|3.676,6|4|750.546|5.897.459|9.687|-11.289|
|**Sector**|AG-2 Plataformas-2|1.955|1|750.498|5.897.513|9.638|-11.237|
|**Sector**|AG-2 Plataformas-2|1.955|2|750.383|5.897.568|9.522|-11.184|
|**Sector**|AG-2 Plataformas-2|1.955|3|750.384|5.897.551|9.523|-11.202|
|**Sector**|AG-2 Plataformas-2|1.955|4|750.490|5.897.498|9.631|-11.251|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 113

|Sector|Fuente|Superficie<br>(m2)|Punto|UTM (WGS 84 - Z18)|Col6|LCC (m)|Col8|
|---|---|---|---|---|---|---|---|
|**Sector**|**Fuente**|**Superficie**<br>**(m2) **|**Punto**|**Este (m)**|**Norte (m)**|**LCC-X**|**LCC-Y**|
|**Sector**|AG-2 Fundación|1.008|1|750.575|5.897.452|9.717|-11.295|
|**Sector**|AG-2 Fundación|1.008|2|750.590|5.897.484|9.730|-11.263|
|**Sector**|AG-2 Fundación|1.008|3|750.563|5.897.493|9.703|-11.254|
|**Sector**|AG-2 Fundación|1.008|4|750.547|5.897.461|9.688|-11.287|
|**Sector**|AG-3 Plataforma AA-1|1.574,6|1|750.953|5.897.416|10.095|-11.320|
|**Sector**|AG-3 Plataforma AA-1|1.574,6|2|750.947|5.897.406|10.090|-11.331|
|**Sector**|AG-3 Plataforma AA-1|1.574,6|3|751.066|5.897.346|10.210|-11.387|
|**Sector**|AG-3 Plataforma AA-1|1.574,6|4|751.072|5.897.357|10.215|-11.376|
|**Sector**|AG-3 Plataforma AA-2|527,6|1|750.962|5.897.398|10.104|-11.338|
|**Sector**|AG-3 Plataforma AA-2|527,6|2|750.959|5.897.393|10.102|-11.343|
|**Sector**|AG-3 Plataforma AA-2|527,6|3|751.038|5.897.354|10.181|-11.380|
|**Sector**|AG-3 Plataforma AA-2|527,6|4|751.040|5.897.359|10.184|-11.375|
|**Sector**|AG-3 Plataformas-1|3.676,6|1|751.099|5.897.412|10.241|-11.320|
|**Sector**|AG-3 Plataformas-1|3.676,6|2|751.040|5.897.442|10.181|-11.292|
|**Sector**|AG-3 Plataformas-1|3.676,6|3|751.014|5.897.393|10.157|-11.341|
|**Sector**|AG-3 Plataformas-1|3.676,6|4|751.075|5.897.363|10.218|-11.370|
|**Sector**|AG-3 Plataformas-2|2.176,8|1|751.027|5.897.417|10.169|-11.317|
|**Sector**|AG-3 Plataformas-2|2.176,8|2|750.904|5.897.476|10.044|-11.262|
|**Sector**|AG-3 Plataformas-2|2.176,8|3|750.897|5.897.463|10.038|-11.275|
|**Sector**|AG-3 Plataformas-2|2.176,8|4|751.019|5.897.402|10.161|-11.332|
|**Sector**|AG-3 Fundación|1.009|1|751.077|5.897.364|10.220|-11.369|
|**Sector**|AG-3 Fundación|1.009|2|751.100|5.897.351|10.244|-11.381|
|**Sector**|AG-3 Fundación|1.009|3|751.117|5.897.387|10.259|-11.345|
|**Sector**|AG-3 Fundación|1.009|4|751.093|5.897.397|10.235|-11.335|
|**Sector**|AG-4 Plataforma AA-1|1.564,6|1|751.443|5.897.165|10.592|-11.557|
|**Sector**|AG-4 Plataforma AA-1|1.564,6|2|751.449|5.897.175|10.598|-11.546|
|**Sector**|AG-4 Plataforma AA-1|1.564,6|3|751.333|5.897.241|10.480|-11.484|
|**Sector**|AG-4 Plataforma AA-1|1.564,6|4|751.328|5.897.231|10.475|-11.494|
|**Sector**|AG-4 Plataforma AA-2|527,6|1|751.424|5.897.190|10.572|-11.533|
|**Sector**|AG-4 Plataforma AA-2|527,6|2|751.427|5.897.195|10.575|-11.527|
|**Sector**|AG-4 Plataforma AA-2|527,6|3|751.350|5.897.238|10.497|-11.486|
|**Sector**|AG-4 Plataforma AA-2|527,6|4|751.347|5.897.233|10.494|-11.492|
|**Sector**|AG-4 Plataformas-1|3.676,7|1|751.355|5.897.144|10.504|-11.580|
|**Sector**|AG-4 Plataformas-1|3.676,7|2|751.413|5.897.111|10.563|-11.612|
|**Sector**|AG-4 Plataformas-1|3.676,7|3|751.440|5.897.159|10.589|-11.563|
|**Sector**|AG-4 Plataformas-1|3.676,7|4|751.381|5.897.192|10.529|-11.531|
|**Sector**|AG-4 Plataformas-2|2.127|1|751.376|5.897.184|10.525|-11.540|
|**Sector**|AG-4 Plataformas-2|2.127|2|751.258|5.897.251|10.405|-11.476|
|**Sector**|AG-4 Plataformas-2|2.127|3|751.251|5.897.238|10.398|-11.490|
|**Sector**|AG-4 Plataformas-2|2.127|4|751.368|5.897.169|10.517|-11.555|
|**Sector**|AG-4 Fundación|1.001|1|751.421|5.897.126|10.571|-11.597|
|**Sector**|AG-4 Fundación|1.001|2|751.445|5.897.111|10.595|-11.610|
|**Sector**|AG-4 Fundación|1.001|3|751.463|5.897.143|10.612|-11.579|
|**Sector**|AG-4 Fundación|1.001|4|751.440|5.897.157|10.589|-11.565|
|**Sector**|AG-5 Plataforma AA-1|1.535,2|1|751.915|5.897.226|11.062|-11.483|
|**Sector**|AG-5 Plataforma AA-1|1.535,2|2|751.912|5.897.236|11.058|-11.472|
|**Sector**|AG-5 Plataforma AA-1|1.535,2|3|751.786|5.897.193|10.934|-11.519|
|**Sector**|AG-5 Plataforma AA-1|1.535,2|4|751.790|5.897.182|10.938|-11.530|
|**Sector**|AG-5 Plataforma AA-2|527,6|1|751.897|5.897.231|11.043|-11.478|
|**Sector**|AG-5 Plataforma AA-2|527,6|2|751.895|5.897.237|11.041|-11.472|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 114

|Sector|Fuente|Superficie<br>(m2)|Punto|UTM (WGS 84 - Z18)|Col6|LCC (m)|Col8|
|---|---|---|---|---|---|---|---|
|**Sector**|**Fuente**|**Superficie**<br>**(m2) **|**Punto**|**Este (m)**|**Norte (m)**|**LCC-X**|**LCC-Y**|
|**Sector**|**Fuente**|**Superficie**<br>**(m2) **|3|751.812|5.897.208|10.959|-11.503|
|**Sector**|**Fuente**|**Superficie**<br>**(m2) **|4|751.813|5.897.203|10.961|-11.509|
|**Sector**|AG-5 Plataformas-1|3.676,6|1|751.856|5.897.197|11.004|-11.513|
|**Sector**|AG-5 Plataformas-1|3.676,6|2|751.792|5.897.175|10.940|-11.537|
|**Sector**|AG-5 Plataformas-1|3.676,6|3|751.810|5.897.123|10.960|-11.588|
|**Sector**|AG-5 Plataformas-1|3.676,6|4|751.873|5.897.145|11.022|-11.565|
|**Sector**|AG-5 Plataformas-2|1.950,5|1|751.993|5.897.218|11.140|-11.489|
|**Sector**|AG-5 Plataformas-2|1.950,5|2|751.986|5.897.230|11.132|-11.477|
|**Sector**|AG-5 Plataformas-2|1.950,5|3|751.859|5.897.188|11.007|-11.522|
|**Sector**|AG-5 Plataformas-2|1.950,5|4|751.864|5.897.173|11.012|-11.537|
|**Sector**|AG-5 Fundación|1.001|1|751.777|5.897.129|10.927|-11.584|
|**Sector**|AG-5 Fundación|1.001|2|751.804|5.897.139|10.953|-11.572|
|**Sector**|AG-5 Fundación|1.001|3|751.793|5.897.173|10.941|-11.539|
|**Sector**|AG-5 Fundación|1.001|4|751.767|5.897.163|10.916|-11.550|
|**Sector**|AG-6 Plataforma AA-1|1.595,7|1|751.995|5.897.250|11.141|-11.456|
|**Sector**|AG-6 Plataforma AA-1|1.595,7|2|751.996|5.897.238|11.142|-11.468|
|**Sector**|AG-6 Plataforma AA-1|1.595,7|3|752.128|5.897.249|11.274|-11.453|
|**Sector**|AG-6 Plataforma AA-1|1.595,7|4|752.127|5.897.261|11.273|-11.441|
|**Sector**|AG-6 Plataforma AA-2|527,6|1|752.098|5.897.265|11.243|-11.439|
|**Sector**|AG-6 Plataforma AA-2|527,6|2|752.010|5.897.257|11.156|-11.449|
|**Sector**|AG-6 Plataforma AA-2|527,6|3|752.011|5.897.251|11.157|-11.455|
|**Sector**|AG-6 Plataforma AA-2|527,6|4|752.098|5.897.259|11.244|-11.445|
|**Sector**|AG-6 Plataformas-1|3.676,6|1|752.130|5.897.232|11.276|-11.471|
|**Sector**|AG-6 Plataformas-1|3.676,6|2|752.062|5.897.226|11.209|-11.479|
|**Sector**|AG-6 Plataformas-1|3.676,6|3|752.068|5.897.171|11.216|-11.533|
|**Sector**|AG-6 Plataformas-1|3.676,6|4|752.134|5.897.177|11.282|-11.525|
|**Sector**|AG-6 Plataformas-2|1.770,9|1|752.063|5.897.216|11.210|-11.488|
|**Sector**|AG-6 Plataformas-2|1.770,9|2|751.965|5.897.208|11.112|-11.499|
|**Sector**|AG-6 Plataformas-2|1.770,9|3|751.924|5.897.193|11.071|-11.515|
|**Sector**|AG-6 Plataformas-2|1.770,9|4|752.065|5.897.199|11.212|-11.505|
|**Sector**|AG-6 Fundación|1.000|1|752.131|5.897.228|11.277|-11.474|
|**Sector**|AG-6 Fundación|1.000|2|752.133|5.897.193|11.280|-11.509|
|**Sector**|AG-6 Fundación|1.000|3|752.162|5.897.195|11.309|-11.507|
|**Sector**|AG-6 Fundación|1.000|4|752.158|5.897.231|11.304|-11.470|
|**Sector**|AG-7 Plataforma AA-1|1.536,3|1|752.350|5.897.258|11.495|-11.438|
|**Sector**|AG-7 Plataforma AA-1|1.536,3|2|752.345|5.897.248|11.491|-11.448|
|**Sector**|AG-7 Plataforma AA-1|1.536,3|3|752.468|5.897.196|11.615|-11.496|
|**Sector**|AG-7 Plataforma AA-1|1.536,3|4|752.472|5.897.207|11.619|-11.485|
|**Sector**|AG-7 Plataforma AA-2|527,6|1|752.360|5.897.242|11.506|-11.454|
|**Sector**|AG-7 Plataforma AA-2|527,6|2|752.358|5.897.237|11.504|-11.459|
|**Sector**|AG-7 Plataforma AA-2|527,6|3|752.439|5.897.202|11.586|-11.491|
|**Sector**|AG-7 Plataforma AA-2|527,6|4|752.441|5.897.208|11.588|-11.486|
|**Sector**|AG-7 Plataformas-1|3.676,6|1|752.497|5.897.265|11.642|-11.428|
|**Sector**|AG-7 Plataformas-1|3.676,6|2|752.435|5.897.290|11.580|-11.403|
|**Sector**|AG-7 Plataformas-1|3.676,6|3|752.413|5.897.240|11.559|-11.454|
|**Sector**|AG-7 Plataformas-1|3.676,6|4|752.475|5.897.214|11.622|-11.479|
|**Sector**|AG-7 Plataformas-2|2.071,6|1|752.423|5.897.264|11.569|-11.431|
|**Sector**|AG-7 Plataformas-2|2.071,6|2|752.297|5.897.316|11.441|-11.382|
|**Sector**|AG-7 Plataformas-2|2.071,6|3|752.292|5.897.302|11.436|-11.396|
|**Sector**|AG-7 Plataformas-2|2.071,6|4|752.417|5.897.249|11.563|-11.445|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 115

|Sector|Fuente|Superficie<br>(m2)|Punto|UTM (WGS 84 - Z18)|Col6|LCC (m)|Col8|
|---|---|---|---|---|---|---|---|
|**Sector**|**Fuente**|**Superficie**<br>**(m2) **|**Punto**|**Este (m)**|**Norte (m)**|**LCC-X**|**LCC-Y**|
|**Sector**|AG-7 Fundación|1.005|1|752.490|5.897.247|11.635|-11.445|
|**Sector**|AG-7 Fundación|1.005|2|752.475|5.897.214|11.622|-11.478|
|**Sector**|AG-7 Fundación|1.005|3|752.503|5.897.208|11.650|-11.484|
|**Sector**|AG-7 Fundación|1.005|4|752.517|5.897.239|11.663|-11.452|
|**Sector**|AG-8 Plataforma AA-1|1.595,7|1|754.039|5.896.722|13.198|-11.926|
|**Sector**|AG-8 Plataforma AA-1|1.595,7|2|754.039|5.896.734|13.198|-11.914|
|**Sector**|AG-8 Plataforma AA-1|1.595,7|3|753.906|5.896.737|13.065|-11.915|
|**Sector**|AG-8 Plataforma AA-1|1.595,7|4|753.906|5.896.725|13.065|-11.927|
|**Sector**|AG-8 Plataforma AA-2|527,6|1|754.023|5.896.734|13.182|-11.914|
|**Sector**|AG-8 Plataforma AA-2|527,6|2|754.023|5.896.740|13.182|-11.908|
|**Sector**|AG-8 Plataforma AA-2|527,6|3|753.935|5.896.742|13.094|-11.909|
|**Sector**|AG-8 Plataforma AA-2|527,6|4|753.935|5.896.736|13.094|-11.915|
|**Sector**|AG-8 Plataformas-1|3.505,7|1|753.987|5.896.678|13.147|-11.971|
|**Sector**|AG-8 Plataformas-1|3.505,7|2|754.053|5.896.677|13.214|-11.970|
|**Sector**|AG-8 Plataformas-1|3.505,7|3|754.054|5.896.722|13.213|-11.925|
|**Sector**|AG-8 Plataformas-1|3.505,7|4|753.965|5.896.724|13.124|-11.926|
|**Sector**|AG-8 Plataformas-2|1.777,8|1|753.851|5.896.726|13.010|-11.927|
|**Sector**|AG-8 Plataformas-2|1.777,8|2|753.850|5.896.711|13.010|-11.942|
|**Sector**|AG-8 Plataformas-2|1.777,8|3|753.972|5.896.708|13.132|-11.942|
|**Sector**|AG-8 Plataformas-2|1.777,8|4|753.965|5.896.723|13.124|-11.926|
|**Sector**|AG-8 Fundación|1.004|1|754.054|5.896.692|13.214|-11.955|
|**Sector**|AG-8 Fundación|1.004|2|754.081|5.896.692|13.241|-11.954|
|**Sector**|AG-8 Fundación|1.004|3|754.078|5.896.731|13.237|-11.915|
|**Sector**|AG-8 Fundación|1.004|4|754.054|5.896.733|13.213|-11.914|
|**Sector**|AG-9 Plataforma AA-1|942,8|1|754.317|5.896.376|13.486|-12.263|
|**Sector**|AG-9 Plataforma AA-1|942,8|2|754.322|5.896.378|13.491|-12.262|
|**Sector**|AG-9 Plataforma AA-1|942,8|3|754.267|5.896.511|13.432|-12.130|
|**Sector**|AG-9 Plataforma AA-1|942,8|4|754.259|5.896.508|13.425|-12.133|
|**Sector**|AG-9 Plataforma AA-2|508,1|1|754.299|5.896.403|13.468|-12.237|
|**Sector**|AG-9 Plataforma AA-2|508,1|2|754.304|5.896.405|13.473|-12.235|
|**Sector**|AG-9 Plataforma AA-2|508,1|3|754.266|5.896.492|13.432|-12.149|
|**Sector**|AG-9 Plataforma AA-2|508,1|4|754.261|5.896.490|13.427|-12.151|
|**Sector**|AG-9 Plataformas-1|3.676,5|1|754.305|5.896.449|13.471|-12.191|
|**Sector**|AG-9 Plataformas-1|3.676,5|2|754.334|5.896.382|13.503|-12.257|
|**Sector**|AG-9 Plataformas-1|3.676,5|3|754.381|5.896.400|13.550|-12.238|
|**Sector**|AG-9 Plataformas-1|3.676,5|4|754.353|5.896.466|13.519|-12.173|
|**Sector**|AG-9 Plataformas-2|1.921,3|1|754.326|5.896.457|13.493|-12.183|
|**Sector**|AG-9 Plataformas-2|1.921,3|2|754.271|5.896.583|13.434|-12.058|
|**Sector**|AG-9 Plataformas-2|1.921,3|3|754.258|5.896.578|13.421|-12.064|
|**Sector**|AG-9 Plataformas-2|1.921,3|4|754.313|5.896.452|13.480|-12.187|
|**Sector**|AG-9 Fundación|1.003|1|754.332|5.896.381|13.501|-12.258|
|**Sector**|AG-9 Fundación|1.003|2|754.342|5.896.357|13.511|-12.282|
|**Sector**|AG-9 Fundación|1.003|3|754.376|5.896.366|13.545|-12.271|
|**Sector**|AG-9 Fundación|1.003|4|754.365|5.896.394|13.533|-12.244|
|**Sector**|AG-10 Plataforma AA-1|1.595,6|1|754.680|5.896.450|13.846|-12.179|
|**Sector**|AG-10 Plataforma AA-1|1.595,6|2|754.548|5.896.469|13.714|-12.164|
|**Sector**|AG-10 Plataforma AA-1|1.595,6|3|754.546|5.896.457|13.713|-12.176|
|**Sector**|AG-10 Plataforma AA-1|1.595,6|4|754.678|5.896.438|13.845|-12.191|
|**Sector**|AG-10 Plataforma AA-2|527,6|1|754.562|5.896.455|13.728|-12.178|
|**Sector**|AG-10 Plataforma AA-2|527,6|2|754.561|5.896.449|13.728|-12.184|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 116

|Sector|Fuente|Superficie<br>(m2)|Punto|UTM (WGS 84 - Z18)|Col6|LCC (m)|Col8|
|---|---|---|---|---|---|---|---|
|**Sector**|**Fuente**|**Superficie**<br>**(m2) **|**Punto**|**Este (m)**|**Norte (m)**|**LCC-X**|**LCC-Y**|
|**Sector**|**Fuente**|**Superficie**<br>**(m2) **|3|754.648|5.896.437|13.815|-12.194|
|**Sector**|**Fuente**|**Superficie**<br>**(m2) **|4|754.649|5.896.442|13.816|-12.188|
|**Sector**|AG-10 Plataformas-1|3.676,2|1|754.688|5.896.512|13.853|-12.117|
|**Sector**|AG-10 Plataformas-1|3.676,2|2|754.622|5.896.521|13.787|-12.110|
|**Sector**|AG-10 Plataformas-1|3.676,2|3|754.614|5.896.467|13.780|-12.164|
|**Sector**|AG-10 Plataformas-1|3.676,2|4|754.680|5.896.457|13.847|-12.172|
|**Sector**|AG-10 Plataformas-2|2.192,7|1|754.618|5.896.493|13.783|-12.138|
|**Sector**|AG-10 Plataformas-2|2.192,7|2|754.482|5.896.510|13.647|-12.125|
|**Sector**|AG-10 Plataformas-2|2.192,7|3|754.480|5.896.495|13.646|-12.140|
|**Sector**|AG-10 Plataformas-2|2.192,7|4|754.615|5.896.476|13.781|-12.155|
|**Sector**|AG-10 Fundación|1.006|1|754.681|5.896.460|13.847|-12.170|
|**Sector**|AG-10 Fundación|1.006|2|754.707|5.896.455|13.874|-12.174|
|**Sector**|AG-10 Fundación|1.006|3|754.715|5.896.488|13.881|-12.140|
|**Sector**|AG-10 Fundación|1.006|4|754.686|5.896.495|13.851|-12.134|
|**Sector**|AG-11 Plataforma AA-1|1.595,7|1|754.998|5.896.390|14.166|-12.230|
|**Sector**|AG-11 Plataforma AA-1|1.595,7|2|754.998|5.896.402|14.166|-12.218|
|**Sector**|AG-11 Plataforma AA-1|1.595,7|3|754.865|5.896.405|14.033|-12.219|
|**Sector**|AG-11 Plataforma AA-1|1.595,7|4|754.865|5.896.393|14.033|-12.231|
|**Sector**|AG-11 Plataforma AA-2|527,6|1|754.969|5.896.403|14.137|-12.218|
|**Sector**|AG-11 Plataforma AA-2|527,6|2|754.969|5.896.409|14.137|-12.212|
|**Sector**|AG-11 Plataforma AA-2|527,6|3|754.881|5.896.410|14.049|-12.213|
|**Sector**|AG-11 Plataforma AA-2|527,6|4|754.881|5.896.404|14.049|-12.219|
|**Sector**|AG-11 Plataformas-1|3.676,4|1|754.930|5.896.384|14.098|-12.238|
|**Sector**|AG-11 Plataformas-1|3.676,4|2|754.930|5.896.329|14.100|-12.293|
|**Sector**|AG-11 Plataformas-1|3.676,4|3|754.997|5.896.328|14.167|-12.292|
|**Sector**|AG-11 Plataformas-1|3.676,4|4|754.998|5.896.383|14.166|-12.237|
|**Sector**|AG-11 Plataformas-2|2.089,5|1|754.930|5.896.375|14.099|-12.247|
|**Sector**|AG-11 Plataformas-2|2.089,5|2|754.794|5.896.377|13.963|-12.249|
|**Sector**|AG-11 Plataformas-2|2.089,5|3|754.794|5.896.362|13.963|-12.264|
|**Sector**|AG-11 Plataformas-2|2.089,5|4|754.930|5.896.359|14.099|-12.263|
|**Sector**|AG-11 Fundación|905|1|754.998|5.896.348|14.167|-12.272|
|**Sector**|AG-11 Fundación|905|2|755.030|5.896.357|14.199|-12.262|
|**Sector**|AG-11 Fundación|905|3|755.023|5.896.384|14.191|-12.236|
|**Sector**|AG-11 Fundación|905|4|754.998|5.896.385|14.167|-12.235|
|**Sector**|AG-12 Plataforma AA-1|1.595,7|1|755.228|5.896.387|14.396|-12.226|
|**Sector**|AG-12 Plataforma AA-1|1.595,7|2|755.228|5.896.375|14.396|-12.238|
|**Sector**|AG-12 Plataforma AA-1|1.595,7|3|755.361|5.896.373|14.529|-12.237|
|**Sector**|AG-12 Plataforma AA-1|1.595,7|4|755.361|5.896.385|14.529|-12.225|
|**Sector**|AG-12 Plataforma AA-2|527,6|1|755.332|5.896.391|14.500|-12.219|
|**Sector**|AG-12 Plataforma AA-2|527,6|2|755.244|5.896.393|14.412|-12.220|
|**Sector**|AG-12 Plataforma AA-2|527,6|3|755.244|5.896.387|14.412|-12.226|
|**Sector**|AG-12 Plataforma AA-2|527,6|4|755.332|5.896.385|14.500|-12.225|
|**Sector**|AG-12 Plataformas-1|3.676,4|1|755.293|5.896.367|14.462|-12.245|
|**Sector**|AG-12 Plataformas-1|3.676,4|2|755.293|5.896.312|14.463|-12.300|
|**Sector**|AG-12 Plataformas-1|3.676,4|3|755.360|5.896.311|14.530|-12.299|
|**Sector**|AG-12 Plataformas-1|3.676,4|4|755.361|5.896.366|14.529|-12.244|
|**Sector**|AG-12 Plataformas-2|2.028,7|1|755.293|5.896.357|14.462|-12.255|
|**Sector**|AG-12 Plataformas-2|2.028,7|2|755.157|5.896.359|14.326|-12.256|
|**Sector**|AG-12 Plataformas-2|2.028,7|3|755.157|5.896.345|14.326|-12.271|
|**Sector**|AG-12 Plataformas-2|2.028,7|4|755.293|5.896.342|14.462|-12.270|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 117

|Sector|Fuente|Superficie<br>(m2)|Punto|UTM (WGS 84 - Z18)|Col6|LCC (m)|Col8|
|---|---|---|---|---|---|---|---|
|**Sector**|**Fuente**|**Superficie**<br>**(m2) **|**Punto**|**Este (m)**|**Norte (m)**|**LCC-X**|**LCC-Y**|
|**Sector**|AG-12 Fundación|848|1|755.360|5.896.332|14.530|-12.278|
|**Sector**|AG-12 Fundación|848|2|755.389|5.896.337|14.559|-12.272|
|**Sector**|AG-12 Fundación|848|3|755.385|5.896.366|14.553|-12.243|
|**Sector**|AG-12 Fundación|848|4|755.361|5.896.367|14.530|-12.243|
|**Sector**|AG-13 Plataforma AA-1|1.595,5|1|755.709|5.896.328|14.878|-12.272|
|**Sector**|AG-13 Plataforma AA-1|1.595,5|2|755.697|5.896.324|14.867|-12.276|
|**Sector**|AG-13 Plataforma AA-1|1.595,5|3|755.744|5.896.199|14.916|-12.399|
|**Sector**|AG-13 Plataforma AA-1|1.595,5|4|755.755|5.896.204|14.928|-12.395|
|**Sector**|AG-13 Plataforma AA-2|527,6|1|755.707|5.896.297|14.878|-12.303|
|**Sector**|AG-13 Plataforma AA-2|527,6|2|755.702|5.896.295|14.872|-12.305|
|**Sector**|AG-13 Plataforma AA-2|527,6|3|755.732|5.896.212|14.905|-12.387|
|**Sector**|AG-13 Plataforma AA-2|527,6|4|755.738|5.896.214|14.910|-12.385|
|**Sector**|AG-13 Plataformas-1|3.480,3|1|755.749|5.896.344|14.918|-12.254|
|**Sector**|AG-13 Plataformas-1|3.480,3|2|755.709|5.896.328|14.878|-12.272|
|**Sector**|AG-13 Plataformas-1|3.480,3|3|755.740|5.896.244|14.911|-12.355|
|**Sector**|AG-13 Plataformas-1|3.480,3|4|755.774|5.896.282|14.944|-12.316|
|**Sector**|AG-13 Fundación|1.002|1|755.693|5.896.322|14.862|-12.278|
|**Sector**|AG-13 Fundación|1.002|2|755.732|5.896.337|14.901|-12.262|
|**Sector**|AG-13 Fundación|1.002|3|755.714|5.896.361|14.883|-12.238|
|**Sector**|AG-13 Fundación|1.002|4|755.686|5.896.348|14.855|-12.253|
|**Sector**|AG-14 Plataforma AA-1|1.595,7|1|756.246|5.895.147|15.448|-13.437|
|**Sector**|AG-14 Plataforma AA-1|1.595,7|2|756.255|5.895.155|15.457|-13.429|
|**Sector**|AG-14 Plataforma AA-1|1.595,7|3|756.166|5.895.254|15.366|-13.332|
|**Sector**|AG-14 Plataforma AA-1|1.595,7|4|756.157|5.895.246|15.357|-13.340|
|**Sector**|AG-14 Plataforma AA-2|527,6|1|756.236|5.895.176|15.437|-13.407|
|**Sector**|AG-14 Plataforma AA-2|527,6|2|756.240|5.895.180|15.441|-13.403|
|**Sector**|AG-14 Plataforma AA-2|527,6|3|756.182|5.895.246|15.381|-13.339|
|**Sector**|AG-14 Plataforma AA-2|527,6|4|756.177|5.895.242|15.377|-13.343|
|**Sector**|AG-14 Plataformas-1|3.365,6|1|756.165|5.895.238|15.365|-13.348|
|**Sector**|AG-14 Plataformas-1|3.365,6|2|756.125|5.895.204|15.326|-13.383|
|**Sector**|AG-14 Plataformas-1|3.365,6|3|756.172|5.895.156|15.375|-13.430|
|**Sector**|AG-14 Plataformas-1|3.365,6|4|756.209|5.895.189|15.410|-13.396|
|**Sector**|AG-14 Plataformas-2|2.043,2|1|756.141|5.895.218|15.342|-13.368|
|**Sector**|AG-14 Plataformas-2|2.043,2|2|756.049|5.895.318|15.246|-13.271|
|**Sector**|AG-14 Plataformas-2|2.043,2|3|756.038|5.895.308|15.236|-13.282|
|**Sector**|AG-14 Plataformas-2|2.043,2|4|756.130|5.895.208|15.331|-13.379|
|**Sector**|AG-14 Fundación|738|1|756.201|5.895.180|15.402|-13.405|
|**Sector**|AG-14 Fundación|738|2|756.169|5.895.152|15.372|-13.434|
|**Sector**|AG-14 Fundación|738|3|756.191|5.895.141|15.394|-13.444|
|**Sector**|AG-14 Fundación|738|4|756.210|5.895.165|15.412|-13.420|
|**PE**|Zona de acopio LT|9.930|1|749.478|5.901.605|8.502|-7.176|
|**PE**|Zona de acopio LT|9.930|2|749.407|5.901.647|8.430|-7.137|
|**PE**|Zona de acopio LT|9.930|3|749.451|5.901.458|8.479|-7.324|
|**PE**|Zona de acopio LT|9.930|4|749.509|5.901.471|8.537|-7.309|
|**PE**|LT-1|100|1|750.309|5.897.998|9.435|-10.757|
|**PE**|LT-1|100|2|750.319|5.897.998|9.445|-10.757|
|**PE**|LT-1|100|3|750.319|5.898.008|9.445|-10.747|
|**PE**|LT-1|100|4|750.309|5.898.008|9.435|-10.747|
|**PE**|LT-2|100|1|750.410|5.898.235|9.529|-10.517|
|**PE**|LT-2|100|2|750.420|5.898.236|9.539|-10.516|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 118

|Sector|Fuente|Superficie<br>(m2)|Punto|UTM (WGS 84 - Z18)|Col6|LCC (m)|Col8|
|---|---|---|---|---|---|---|---|
|**Sector**|**Fuente**|**Superficie**<br>**(m2) **|**Punto**|**Este (m)**|**Norte (m)**|**LCC-X**|**LCC-Y**|
|**Sector**|**Fuente**|**Superficie**<br>**(m2) **|3|750.419|5.898.246|9.538|-10.506|
|**Sector**|**Fuente**|**Superficie**<br>**(m2) **|4|750.409|5.898.245|9.528|-10.507|
|**Sector**|LT-3|100|1|750.487|5.898.422|9.601|-10.328|
|**Sector**|LT-3|100|2|750.497|5.898.422|9.611|-10.328|
|**Sector**|LT-3|100|3|750.497|5.898.432|9.610|-10.318|
|**Sector**|LT-3|100|4|750.487|5.898.432|9.600|-10.319|
|**Sector**|LT-4|100|1|750.316|5.898.608|9.424|-10.147|
|**Sector**|LT-4|100|2|750.327|5.898.608|9.436|-10.147|
|**Sector**|LT-4|100|3|750.327|5.898.617|9.435|-10.138|
|**Sector**|LT-4|100|4|750.316|5.898.618|9.425|-10.138|
|**Sector**|LT-5|100|1|750.144|5.898.794|9.247|-9.966|
|**Sector**|LT-5|100|2|750.154|5.898.794|9.258|-9.966|
|**Sector**|LT-5|100|3|750.154|5.898.803|9.257|-9.957|
|**Sector**|LT-5|100|4|750.144|5.898.804|9.247|-9.956|
|**Sector**|LT-6|100|1|750.067|5.899.006|9.164|-9.756|
|**Sector**|LT-6|100|2|750.077|5.899.006|9.174|-9.756|
|**Sector**|LT-6|100|3|750.076|5.899.016|9.173|-9.746|
|**Sector**|LT-6|100|4|750.066|5.899.016|9.164|-9.746|
|**Sector**|LT-7|100|1|749.984|5.899.226|9.076|-9.539|
|**Sector**|LT-7|100|2|749.995|5.899.225|9.087|-9.540|
|**Sector**|LT-7|100|3|749.996|5.899.235|9.087|-9.530|
|**Sector**|LT-7|100|4|749.986|5.899.235|9.077|-9.530|
|**Sector**|LT-8|100|1|749.903|5.899.444|8.989|-9.324|
|**Sector**|LT-8|100|2|749.914|5.899.443|8.999|-9.325|
|**Sector**|LT-8|100|3|749.915|5.899.452|9.000|-9.315|
|**Sector**|LT-8|100|4|749.905|5.899.453|8.990|-9.315|
|**Sector**|LT-9|100|1|749.857|5.899.725|8.934|-9.045|
|**Sector**|LT-9|100|2|749.868|5.899.724|8.945|-9.045|
|**Sector**|LT-9|100|3|749.867|5.899.734|8.944|-9.035|
|**Sector**|LT-9|100|4|749.857|5.899.734|8.934|-9.035|
|**Sector**|LT-10|100|1|749.806|5.900.025|8.874|-8.746|
|**Sector**|LT-10|100|2|749.816|5.900.025|8.884|-8.746|
|**Sector**|LT-10|100|3|749.816|5.900.035|8.885|-8.736|
|**Sector**|LT-10|100|4|749.807|5.900.035|8.875|-8.736|
|**Sector**|LT-11|100|1|749.724|5.900.374|8.783|-8.399|
|**Sector**|LT-11|100|2|749.736|5.900.374|8.795|-8.399|
|**Sector**|LT-11|100|3|749.736|5.900.383|8.795|-8.390|
|**Sector**|LT-11|100|4|749.724|5.900.383|8.783|-8.391|
|**Sector**|LT-12|100|1|749.667|5.900.624|8.719|-8.151|
|**Sector**|LT-12|100|2|749.678|5.900.623|8.730|-8.152|
|**Sector**|LT-12|100|3|749.678|5.900.633|8.730|-8.142|
|**Sector**|LT-12|100|4|749.669|5.900.634|8.720|-8.142|
|**Sector**|LT-13|100|1|749.619|5.900.835|8.665|-7.941|
|**Sector**|LT-13|100|2|749.630|5.900.837|8.676|-7.940|
|**Sector**|LT-13|100|3|749.628|5.900.846|8.674|-7.930|
|**Sector**|LT-13|100|4|749.618|5.900.845|8.664|-7.932|
|**Sector**|LT-14|100|1|749.551|5.901.129|8.589|-7.650|
|**Sector**|LT-14|100|2|749.561|5.901.128|8.599|-7.650|
|**Sector**|LT-14|100|3|749.562|5.901.139|8.599|-7.640|
|**Sector**|LT-14|100|4|749.552|5.901.139|8.589|-7.640|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 119

|Sector|Fuente|Superficie<br>(m2)|Punto|UTM (WGS 84 - Z18)|Col6|LCC (m)|Col8|
|---|---|---|---|---|---|---|---|
|**Sector**|**Fuente**|**Superficie**<br>**(m2) **|**Punto**|**Este (m)**|**Norte (m)**|**LCC-X**|**LCC-Y**|
|**Sector**|LT-15|100|1|749.485|5.901.410|8.515|-7.371|
|**Sector**|LT-15|100|2|749.496|5.901.410|8.526|-7.371|
|**Sector**|LT-15|100|3|749.496|5.901.420|8.526|-7.361|
|**Sector**|LT-15|100|4|749.486|5.901.420|8.515|-7.361|
|**Sector**|LT-16|100|1|749.422|5.901.688|8.444|-7.095|
|**Sector**|LT-16|100|2|749.432|5.901.687|8.454|-7.096|
|**Sector**|LT-16|100|3|749.432|5.901.697|8.454|-7.085|
|**Sector**|LT-16|100|4|749.422|5.901.698|8.444|-7.085|
|**Sector**|LT-17|100|1|749.120|5.901.870|8.137|-6.922|
|**Sector**|LT-17|100|2|749.130|5.901.870|8.147|-6.922|
|**Sector**|LT-17|100|3|749.130|5.901.880|8.147|-6.912|
|**Sector**|LT-17|100|4|749.120|5.901.880|8.137|-6.912|
|**Sector**|LT-18|100|1|748.820|5.902.050|7.832|-6.750|
|**Sector**|LT-18|100|2|748.832|5.902.050|7.844|-6.750|
|**Sector**|LT-18|100|3|748.831|5.902.060|7.843|-6.741|
|**Sector**|LT-18|100|4|748.821|5.902.059|7.833|-6.742|
|**Sector**|LT-19|100|1|748.780|5.902.237|7.787|-6.565|
|**Sector**|LT-19|100|2|748.791|5.902.238|7.797|-6.564|
|**Sector**|LT-19|100|3|748.790|5.902.247|7.796|-6.554|
|**Sector**|LT-19|100|4|748.779|5.902.246|7.785|-6.556|
|**Sector**|LT-20|100|1|748.737|5.902.429|7.738|-6.374|
|**Sector**|LT-20|100|2|748.748|5.902.430|7.749|-6.373|
|**Sector**|LT-20|100|3|748.747|5.902.440|7.748|-6.363|
|**Sector**|LT-20|100|4|748.737|5.902.439|7.738|-6.364|
|**Sector**|LT-21|100|1|748.564|5.902.504|7.564|-6.304|
|**Sector**|LT-21|100|2|748.561|5.902.495|7.561|-6.314|
|**Sector**|LT-21|100|3|748.570|5.902.492|7.570|-6.316|
|**Sector**|LT-21|100|4|748.574|5.902.501|7.573|-6.307|

_Plataforma AA: Plataforma de Acopia de Aspas._

**Tabla 81.** Coordenadas de los tramos de zanja del circuito MT donde se implementaron las fuentes

emisoras de contaminantes atmosféricos en el modelo CALPUFF.

|Sector|Fuente|Largo (m)|Punto|UTM (WGS 84 - Z18)|Col6|LCC (m)|Col8|
|---|---|---|---|---|---|---|---|
|**Sector**|**Fuente**|**Largo (m)**|**Punto**|**Este (m)**|**Norte (m)**|**LCC-X**|**LCC-Y**|
|**PE**|Zanja MT-1|304|1|750.329|5.897.926|9.458|-10.828|
|**PE**|Zanja MT-1|304|2|750.342|5.897.921|9.471|-10.833|
|**PE**|Zanja MT-1|304|3|750.334|5.897.900|9.463|-10.854|
|**PE**|Zanja MT-1|304|4|750.262|5.897.790|9.394|-10.967|
|**PE**|Zanja MT-1|304|5|750.261|5.897.785|9.394|-10.971|
|**PE**|Zanja MT-1|304|6|750.296|5.897.696|9.431|-11.059|
|**PE**|Zanja MT-1|304|7|750.306|5.897.662|9.442|-11.093|
|**PE**|Zanja MT-2|155|1|750.345|5.897.534|9.484|-11.219|
|**PE**|Zanja MT-2|155|2|750.351|5.897.528|9.491|-11.226|
|**PE**|Zanja MT-2|155|3|750.355|5.897.526|9.494|-11.227|
|**PE**|Zanja MT-2|155|4|750.369|5.897.515|9.509|-11.237|
|**PE**|Zanja MT-2|155|5|750.373|5.897.515|9.513|-11.237|
|**PE**|Zanja MT-2|155|6|750.385|5.897.510|9.525|-11.242|
|**PE**|Zanja MT-2|155|7|750.408|5.897.510|9.548|-11.242|
|**PE**|Zanja MT-2|155|8|750.441|5.897.512|9.581|-11.239|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 120

|Sector|Fuente|Largo (m)|Punto|UTM (WGS 84 - Z18)|Col6|LCC (m)|Col8|
|---|---|---|---|---|---|---|---|
|**Sector**|**Fuente**|**Largo (m)**|**Punto**|**Este (m)**|**Norte (m)**|**LCC-X**|**LCC-Y**|
|**Sector**|**Fuente**|**Largo (m)**|9|750.462|5.897.501|9.603|-11.249|
|**Sector**|**Fuente**|**Largo (m)**|10|750.486|5.897.489|9.626|-11.260|
|**Sector**|Zanja MT-3|475|1|750.562|5.897.453|9.703|-11.294|
|**Sector**|Zanja MT-3|475|2|750.592|5.897.439|9.733|-11.307|
|**Sector**|Zanja MT-3|475|3|750.619|5.897.433|9.761|-11.313|
|**Sector**|Zanja MT-3|475|4|750.629|5.897.432|9.771|-11.313|
|**Sector**|Zanja MT-3|475|5|750.648|5.897.430|9.790|-11.315|
|**Sector**|Zanja MT-3|475|6|750.671|5.897.431|9.812|-11.313|
|**Sector**|Zanja MT-3|475|7|750.688|5.897.436|9.830|-11.308|
|**Sector**|Zanja MT-3|475|8|750.750|5.897.447|9.891|-11.295|
|**Sector**|Zanja MT-3|475|9|750.836|5.897.463|9.977|-11.276|
|**Sector**|Zanja MT-3|475|10|750.844|5.897.465|9.985|-11.274|
|**Sector**|Zanja MT-3|475|11|750.863|5.897.462|10.004|-11.276|
|**Sector**|Zanja MT-3|475|12|750.901|5.897.452|10.042|-11.286|
|**Sector**|Zanja MT-3|475|13|751.015|5.897.396|10.158|-11.338|
|**Sector**|Zanja MT-4|350|1|751.071|5.897.355|10.214|-11.378|
|**Sector**|Zanja MT-4|350|2|751.132|5.897.326|10.276|-11.405|
|**Sector**|Zanja MT-4|350|3|751.175|5.897.308|10.320|-11.421|
|**Sector**|Zanja MT-4|350|4|751.231|5.897.279|10.377|-11.449|
|**Sector**|Zanja MT-4|350|5|751.245|5.897.269|10.391|-11.459|
|**Sector**|Zanja MT-4|350|6|751.380|5.897.191|10.528|-11.533|
|**Sector**|Zanja MT-5|365|1|751.439|5.897.157|10.588|-11.565|
|**Sector**|Zanja MT-5|365|2|751.472|5.897.145|10.622|-11.576|
|**Sector**|Zanja MT-5|365|3|751.502|5.897.136|10.651|-11.584|
|**Sector**|Zanja MT-5|365|4|751.525|5.897.133|10.675|-11.586|
|**Sector**|Zanja MT-5|365|5|751.560|5.897.131|10.709|-11.587|
|**Sector**|Zanja MT-5|365|6|751.631|5.897.138|10.780|-11.578|
|**Sector**|Zanja MT-5|365|7|751.652|5.897.138|10.802|-11.578|
|**Sector**|Zanja MT-5|365|8|751.696|5.897.145|10.845|-11.570|
|**Sector**|Zanja MT-5|365|9|751.705|5.897.145|10.854|-11.569|
|**Sector**|Zanja MT-5|365|10|751.714|5.897.143|10.863|-11.571|
|**Sector**|Zanja MT-5|365|11|751.724|5.897.150|10.873|-11.564|
|**Sector**|Zanja MT-5|365|12|751.793|5.897.175|10.941|-11.537|
|**Sector**|Zanja MT-6|114|1|751.856|5.897.197|11.004|-11.514|
|**Sector**|Zanja MT-6|114|2|751.915|5.897.217|11.062|-11.491|
|**Sector**|Zanja MT-6|114|3|751.927|5.897.217|11.074|-11.491|
|**Sector**|Zanja MT-6|114|4|751.937|5.897.222|11.084|-11.486|
|**Sector**|Zanja MT-6|114|5|751.965|5.897.224|11.112|-11.483|
|**Sector**|Zanja MT-7|360|1|751.990|5.897.226|11.137|-11.481|
|**Sector**|Zanja MT-7|360|2|752.090|5.897.234|11.237|-11.470|
|**Sector**|Zanja MT-7|360|3|752.161|5.897.238|11.307|-11.463|
|**Sector**|Zanja MT-7|360|4|752.296|5.897.261|11.442|-11.437|
|**Sector**|Zanja MT-7|360|5|752.316|5.897.260|11.462|-11.437|
|**Sector**|Zanja MT-7|360|6|752.348|5.897.256|11.493|-11.441|
|**Sector**|Zanja MT-8|1.772|1|752.496|5.897.209|11.643|-11.483|
|**Sector**|Zanja MT-8|1.772|2|752.557|5.897.183|11.705|-11.507|
|**Sector**|Zanja MT-8|1.772|3|752.572|5.897.172|11.720|-11.518|
|**Sector**|Zanja MT-8|1.772|4|752.581|5.897.161|11.729|-11.529|
|**Sector**|Zanja MT-8|1.772|5|752.584|5.897.152|11.733|-11.537|
|**Sector**|Zanja MT-8|1.772|6|752.588|5.897.140|11.737|-11.549|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 121

|Sector|Fuente|Largo (m)|Punto|UTM (WGS 84 - Z18)|Col6|LCC (m)|Col8|
|---|---|---|---|---|---|---|---|
|**Sector**|**Fuente**|**Largo (m)**|**Punto**|**Este (m)**|**Norte (m)**|**LCC-X**|**LCC-Y**|
|**Sector**|**Fuente**|**Largo (m)**|7|752.611|5.897.088|11.761|-11.600|
|**Sector**|**Fuente**|**Largo (m)**|8|752.642|5.897.020|11.794|-11.668|
|**Sector**|**Fuente**|**Largo (m)**|9|752.700|5.896.883|11.856|-11.802|
|**Sector**|**Fuente**|**Largo (m)**|10|752.707|5.896.873|11.863|-11.813|
|**Sector**|**Fuente**|**Largo (m)**|11|752.720|5.896.860|11.877|-11.825|
|**Sector**|**Fuente**|**Largo (m)**|12|752.725|5.896.858|11.882|-11.827|
|**Sector**|**Fuente**|**Largo (m)**|13|752.738|5.896.846|11.895|-11.839|
|**Sector**|**Fuente**|**Largo (m)**|14|752.750|5.896.839|11.907|-11.845|
|**Sector**|**Fuente**|**Largo (m)**|15|752.791|5.896.826|11.948|-11.857|
|**Sector**|**Fuente**|**Largo (m)**|16|752.826|5.896.816|11.984|-11.867|
|**Sector**|**Fuente**|**Largo (m)**|17|752.852|5.896.807|12.010|-11.875|
|**Sector**|**Fuente**|**Largo (m)**|18|752.870|5.896.801|12.028|-11.880|
|**Sector**|**Fuente**|**Largo (m)**|19|752.879|5.896.798|12.037|-11.882|
|**Sector**|**Fuente**|**Largo (m)**|20|752.885|5.896.798|12.043|-11.883|
|**Sector**|**Fuente**|**Largo (m)**|21|752.904|5.896.791|12.063|-11.889|
|**Sector**|**Fuente**|**Largo (m)**|22|752.909|5.896.790|12.067|-11.890|
|**Sector**|**Fuente**|**Largo (m)**|23|752.924|5.896.786|12.082|-11.894|
|**Sector**|**Fuente**|**Largo (m)**|24|752.963|5.896.774|12.121|-11.904|
|**Sector**|**Fuente**|**Largo (m)**|25|753.017|5.896.758|12.176|-11.918|
|**Sector**|**Fuente**|**Largo (m)**|26|753.074|5.896.740|12.234|-11.935|
|**Sector**|**Fuente**|**Largo (m)**|27|753.238|5.896.691|12.399|-11.979|
|**Sector**|**Fuente**|**Largo (m)**|28|753.306|5.896.671|12.468|-11.997|
|**Sector**|**Fuente**|**Largo (m)**|29|753.343|5.896.660|12.505|-12.007|
|**Sector**|**Fuente**|**Largo (m)**|30|753.404|5.896.642|12.566|-12.024|
|**Sector**|**Fuente**|**Largo (m)**|31|753.462|5.896.624|12.625|-12.040|
|**Sector**|**Fuente**|**Largo (m)**|32|753.497|5.896.615|12.660|-12.048|
|**Sector**|**Fuente**|**Largo (m)**|33|753.556|5.896.596|12.720|-12.065|
|**Sector**|**Fuente**|**Largo (m)**|34|753.633|5.896.574|12.797|-12.085|
|**Sector**|**Fuente**|**Largo (m)**|35|753.672|5.896.572|12.836|-12.086|
|**Sector**|**Fuente**|**Largo (m)**|36|753.711|5.896.580|12.875|-12.077|
|**Sector**|**Fuente**|**Largo (m)**|37|753.736|5.896.591|12.899|-12.066|
|**Sector**|**Fuente**|**Largo (m)**|38|753.746|5.896.596|12.909|-12.060|
|**Sector**|**Fuente**|**Largo (m)**|39|753.789|5.896.629|12.951|-12.026|
|**Sector**|**Fuente**|**Largo (m)**|40|753.817|5.896.648|12.978|-12.006|
|**Sector**|**Fuente**|**Largo (m)**|41|753.822|5.896.655|12.984|-11.999|
|**Sector**|**Fuente**|**Largo (m)**|42|753.840|5.896.664|13.001|-11.989|
|**Sector**|**Fuente**|**Largo (m)**|43|753.869|5.896.676|13.030|-11.977|
|**Sector**|**Fuente**|**Largo (m)**|44|753.892|5.896.681|13.052|-11.971|
|**Sector**|**Fuente**|**Largo (m)**|45|753.938|5.896.682|13.099|-11.969|
|**Sector**|**Fuente**|**Largo (m)**|46|753.985|5.896.680|13.146|-11.970|
|**Sector**|Zanja MT-9|393|1|754.053|5.896.678|13.214|-11.969|
|**Sector**|Zanja MT-9|393|2|754.063|5.896.676|13.224|-11.971|
|**Sector**|Zanja MT-9|393|3|754.068|5.896.675|13.229|-11.971|
|**Sector**|Zanja MT-9|393|4|754.078|5.896.671|13.239|-11.976|
|**Sector**|Zanja MT-9|393|5|754.094|5.896.655|13.255|-11.991|
|**Sector**|Zanja MT-9|393|6|754.102|5.896.646|13.264|-12.000|
|**Sector**|Zanja MT-9|393|7|754.120|5.896.624|13.282|-12.021|
|**Sector**|Zanja MT-9|393|8|754.136|5.896.615|13.299|-12.030|
|**Sector**|Zanja MT-9|393|9|754.156|5.896.602|13.319|-12.043|
|**Sector**|Zanja MT-9|393|10|754.175|5.896.592|13.338|-12.051|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 122

|Sector|Fuente|Largo (m)|Punto|UTM (WGS 84 - Z18)|Col6|LCC (m)|Col8|
|---|---|---|---|---|---|---|---|
|**Sector**|**Fuente**|**Largo (m)**|**Punto**|**Este (m)**|**Norte (m)**|**LCC-X**|**LCC-Y**|
|**Sector**|**Fuente**|**Largo (m)**|11|754.204|5.896.590|13.367|-12.053|
|**Sector**|**Fuente**|**Largo (m)**|12|754.225|5.896.594|13.388|-12.048|
|**Sector**|**Fuente**|**Largo (m)**|13|754.246|5.896.606|13.409|-12.036|
|**Sector**|**Fuente**|**Largo (m)**|14|754.260|5.896.572|13.423|-12.069|
|**Sector**|**Fuente**|**Largo (m)**|15|754.313|5.896.453|13.479|-12.187|
|**Sector**|Zanja MT-10|375|1|754.321|5.896.472|13.487|-12.168|
|**Sector**|Zanja MT-10|375|2|754.284|5.896.557|13.447|-12.084|
|**Sector**|Zanja MT-10|375|3|754.288|5.896.558|13.452|-12.083|
|**Sector**|Zanja MT-10|375|4|754.301|5.896.547|13.465|-12.093|
|**Sector**|Zanja MT-10|375|5|754.314|5.896.539|13.478|-12.100|
|**Sector**|Zanja MT-10|375|6|754.315|5.896.536|13.480|-12.104|
|**Sector**|Zanja MT-10|375|7|754.333|5.896.529|13.498|-12.110|
|**Sector**|Zanja MT-10|375|8|754.406|5.896.498|13.572|-12.139|
|**Sector**|Zanja MT-10|375|9|754.464|5.896.481|13.630|-12.154|
|**Sector**|Zanja MT-10|375|10|754.546|5.896.467|13.713|-12.166|
|**Sector**|Zanja MT-11|263|1|754.679|5.896.448|13.846|-12.181|
|**Sector**|Zanja MT-11|263|2|754.711|5.896.441|13.878|-12.187|
|**Sector**|Zanja MT-11|263|3|754.732|5.896.434|13.899|-12.194|
|**Sector**|Zanja MT-11|263|4|754.758|5.896.420|13.926|-12.207|
|**Sector**|Zanja MT-11|263|5|754.820|5.896.389|13.988|-12.236|
|**Sector**|Zanja MT-11|263|6|754.839|5.896.386|14.008|-12.239|
|**Sector**|Zanja MT-11|263|7|754.879|5.896.385|14.048|-12.238|
|**Sector**|Zanja MT-11|263|8|754.929|5.896.384|14.098|-12.238|
|**Sector**|Zanja MT-12|270|1|755.023|5.896.383|14.191|-12.236|
|**Sector**|Zanja MT-12|270|2|755.070|5.896.380|14.238|-12.238|
|**Sector**|Zanja MT-12|270|3|755.113|5.896.374|14.281|-12.243|
|**Sector**|Zanja MT-12|270|4|755.136|5.896.371|14.305|-12.245|
|**Sector**|Zanja MT-12|270|5|755.198|5.896.369|14.366|-12.245|
|**Sector**|Zanja MT-12|270|6|755.292|5.896.366|14.461|-12.246|
|**Sector**|Zanja MT-13|366|1|755.386|5.896.364|14.555|-12.245|
|**Sector**|Zanja MT-13|366|2|755.433|5.896.362|14.602|-12.246|
|**Sector**|Zanja MT-13|366|3|755.458|5.896.361|14.627|-12.246|
|**Sector**|Zanja MT-13|366|4|755.493|5.896.367|14.661|-12.240|
|**Sector**|Zanja MT-13|366|5|755.554|5.896.372|14.722|-12.233|
|**Sector**|Zanja MT-13|366|6|755.624|5.896.370|14.792|-12.233|
|**Sector**|Zanja MT-13|366|7|755.666|5.896.369|14.834|-12.232|
|**Sector**|Zanja MT-13|366|8|755.696|5.896.367|14.864|-12.233|
|**Sector**|Zanja MT-13|366|9|755.709|5.896.364|14.877|-12.236|
|**Sector**|Zanja MT-13|366|10|755.723|5.896.358|14.891|-12.241|
|**Sector**|Zanja MT-13|366|11|755.745|5.896.343|14.914|-12.256|
|**Sector**|Zanja MT-14|1.342|1|755.774|5.896.281|14.945|-12.317|
|**Sector**|Zanja MT-14|1.342|2|755.776|5.896.276|14.947|-12.322|
|**Sector**|Zanja MT-14|1.342|3|755.780|5.896.253|14.951|-12.345|
|**Sector**|Zanja MT-14|1.342|4|755.780|5.896.192|14.954|-12.406|
|**Sector**|Zanja MT-14|1.342|5|755.781|5.896.079|14.958|-12.519|
|**Sector**|Zanja MT-14|1.342|6|755.777|5.895.881|14.959|-12.716|
|**Sector**|Zanja MT-14|1.342|7|755.773|5.895.719|14.960|-12.878|
|**Sector**|Zanja MT-14|1.342|8|755.772|5.895.685|14.960|-12.912|
|**Sector**|Zanja MT-14|1.342|9|755.770|5.895.532|14.962|-13.065|
|**Sector**|Zanja MT-14|1.342|10|755.768|5.895.472|14.961|-13.125|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 123

|Sector|Fuente|Largo (m)|Punto|UTM (WGS 84 - Z18)|Col6|LCC (m)|Col8|
|---|---|---|---|---|---|---|---|
|**Sector**|**Fuente**|**Largo (m)**|**Punto**|**Este (m)**|**Norte (m)**|**LCC-X**|**LCC-Y**|
|**Sector**|**Fuente**|**Largo (m)**|11|755.776|5.895.434|14.970|-13.163|
|**Sector**|**Fuente**|**Largo (m)**|12|755.799|5.895.411|14.994|-13.185|
|**Sector**|**Fuente**|**Largo (m)**|13|755.830|5.895.396|15.026|-13.199|
|**Sector**|**Fuente**|**Largo (m)**|14|755.876|5.895.383|15.072|-13.211|
|**Sector**|**Fuente**|**Largo (m)**|15|755.919|5.895.367|15.116|-13.226|
|**Sector**|**Fuente**|**Largo (m)**|16|755.964|5.895.344|15.161|-13.248|
|**Sector**|**Fuente**|**Largo (m)**|17|756.002|5.895.317|15.199|-13.273|
|**Sector**|**Fuente**|**Largo (m)**|18|756.045|5.895.275|15.243|-13.314|
|**Sector**|**Fuente**|**Largo (m)**|19|756.168|5.895.150|15.371|-13.436|

**Tabla 82.** Coordenadas de los tramos de caminos donde se implementaron las fuentes emisoras de

contaminantes atmosféricos en el modelo CALPUFF.

|Sector|Fuente|Largo (m)|Punto|UTM (WGS 84 - Z18)|Col6|LCC (km)|Col8|
|---|---|---|---|---|---|---|---|
|**Sector**|**Fuente**|**Largo (m)**|**Punto**|**Este (m)**|**Norte (m)**|**LCC-X**|**LCC-Y**|
|PE|Área supresor 1|523|1|757.662|5.903.171|16.635|-5.379|
|PE|Área supresor 1|523|2|757.651|5.903.146|16.624|-5.404|
|PE|Área supresor 1|523|3|757.628|5.903.113|16.602|-5.438|
|PE|Área supresor 1|523|4|757.603|5.903.079|16.578|-5.473|
|PE|Área supresor 1|523|5|757.337|5.902.762|16,322|-5,797|
|LT|Área supresor 2|405|1|750.307|5.900.435|9.364|-8.322|
|LT|Área supresor 2|405|2|750.244|5.900.034|9.312|-8.724|
|PE|Área supresor 3|276|1|753.504|5.896.605|12.668|-12.058|
|PE|Área supresor 3|276|2|753.241|5.896.688|12.402|-11.983|
|PE|Área supresor 4 (Exterior)|254|1|754.725|5.898.196|13.842|-10.433|
|PE|Área supresor 4 (Exterior)|254|2|754.627|5.898.136|13.745|-10.496|
|PE|Área supresor 4 (Exterior)|254|3|754.578|5.898.088|13.698|-10.546|
|PE|Área supresor 4 (Exterior)|254|4|754.546|5.898.025|13.668|-10.610|
|PE|Área supresor 4 (Interior)|113|1|754.546|5.898.025|13.668|-10.610|
|PE|Área supresor 4 (Interior)|113|2|754.528|5.897.988|13.651|-10.646|
|PE|Área supresor 4 (Interior)|113|3|754.515|5.897.956|13.639|-10.679|
|PE|Área supresor 4 (Interior)|113|4|754.496|5.897.924|13.621|-10.712|
|PE|Área supresor 5|245|1|755.867|5.901.029|14.902|-7.570|
|PE|Área supresor 5|245|2|755.717|5.900.835|14.758|-7.768|
|PE|Área supresor 6|649|1|757.069|5.902.439|16.063|-6.127|
|PE|Área supresor 6|649|2|756.659|5.901.935|15.668|-6.642|
|PE|Área supresor 7|272|1|757.069|5.902.443|16.063|-6.123|
|PE|Área supresor 7|272|2|757.242|5.902.653|16.230|-5.909|
|PE|Área supresor 8|260|1|755.719|5.900.830|14.760|-7.773|
|PE|Área supresor 8|260|2|755.671|5.900.775|14.714|-7.830|
|PE|Área supresor 8|260|3|755.552|5.900.730|14.596|-7.878|
|PE|Área supresor 8|260|4|755.507|5.900.691|14.552|-7.918|
|PE|Área supresor 9|232|1|755.870|5.901.032|14.905|-7.567|
|PE|Área supresor 9|232|2|756.011|5.901.217|15.041|-7.379|
|PE|Acceso PE-1|143|1|757.337|5.902.762|16,322|-5,797|
|PE|Acceso PE-1|143|2|757.247|5.902.651|16.235|-5.911|
|PE|Acceso PE-2|966|1|756.658|5.901.935|15.667|-6.643|
|PE|Acceso PE-2|966|2|756.012|5.901.217|15.041|-7.379|
|PE|Acceso PE-3|2.795|1|755.506|5.900.689|14.552|-7.920|
|PE|Acceso PE-3|2.795|2|755.439|5.900.621|14.486|-7.990|
|PE|Acceso PE-3|2.795|3|755.404|5.900.448|14.456|-8.164|
|PE|Acceso PE-3|2.795|4|755.320|5.900.247|14.378|-8.367|
|PE|Acceso PE-3|2.795|5|755.007|5.899.579|14.084|-9.044|
|PE|Acceso PE-3|2.795|6|754.811|5.898.694|13.914|-9.934|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 124

|Sector|Fuente|Largo (m)|Punto|UTM (WGS 84 - Z18)|Col6|LCC (km)|Col8|
|---|---|---|---|---|---|---|---|
|**Sector**|**Fuente**|**Largo (m)**|**Punto**|**Este (m)**|**Norte (m)**|**LCC-X**|**LCC-Y**|
|**Sector**|**Fuente**|**Largo (m)**|7|754.812|5.898.523|13.919|-10.104|
|**Sector**|**Fuente**|**Largo (m)**|8|754.916|5.898.443|14.026|-10.181|
|**Sector**|**Fuente**|**Largo (m)**|9|754.939|5.898.384|14.051|-10.239|
|**Sector**|**Fuente**|**Largo (m)**|10|754.919|5.898.321|14.032|-10.303|
|**Sector**|**Fuente**|**Largo (m)**|11|754.793|5.898.237|13.908|-10.390|
|**Sector**|**Fuente**|**Largo (m)**|12|754.726|5.898.198|13.843|-10.432|
|LT|Acceso LT-1|3.400|1|749.487|5.901.600|8.511|-7.181|
|LT|Acceso LT-1|3.400|2|749.531|5.901.567|8.557|-7.212|
|LT|Acceso LT-1|3.400|3|749.537|5.901.563|8.562|-7.216|
|LT|Acceso LT-1|3.400|4|749.541|5.901.560|8.566|-7.219|
|LT|Acceso LT-1|3.400|5|749.545|5.901.558|8.570|-7.222|
|LT|Acceso LT-1|3.400|6|749.548|5.901.555|8.574|-7.225|
|LT|Acceso LT-1|3.400|7|749.552|5.901.553|8.578|-7.226|
|LT|Acceso LT-1|3.400|8|749.554|5.901.552|8.580|-7.228|
|LT|Acceso LT-1|3.400|9|749.560|5.901.546|8.585|-7.233|
|LT|Acceso LT-1|3.400|10|749.564|5.901.545|8.589|-7.234|
|LT|Acceso LT-1|3.400|11|749.566|5.901.543|8.592|-7.236|
|LT|Acceso LT-1|3.400|12|749.570|5.901.541|8.596|-7.237|
|LT|Acceso LT-1|3.400|13|749.575|5.901.541|8.601|-7.238|
|LT|Acceso LT-1|3.400|14|749.582|5.901.537|8.608|-7.241|
|LT|Acceso LT-1|3.400|15|749.587|5.901.536|8.613|-7.242|
|LT|Acceso LT-1|3.400|16|749.589|5.901.535|8.615|-7.243|
|LT|Acceso LT-1|3.400|17|749.595|5.901.532|8.621|-7.246|
|LT|Acceso LT-1|3.400|18|749.598|5.901.530|8.625|-7.248|
|LT|Acceso LT-1|3.400|19|749.601|5.901.529|8.627|-7.249|
|LT|Acceso LT-1|3.400|20|749.606|5.901.528|8.632|-7.250|
|LT|Acceso LT-1|3.400|21|749.610|5.901.526|8.636|-7.252|
|LT|Acceso LT-1|3.400|22|749.616|5.901.524|8.642|-7.253|
|LT|Acceso LT-1|3.400|23|749.620|5.901.523|8.646|-7.254|
|LT|Acceso LT-1|3.400|24|749.624|5.901.523|8.650|-7.255|
|LT|Acceso LT-1|3.400|25|749.628|5.901.522|8.654|-7.255|
|LT|Acceso LT-1|3.400|26|749.633|5.901.521|8.659|-7.256|
|LT|Acceso LT-1|3.400|27|749.637|5.901.520|8.663|-7.257|
|LT|Acceso LT-1|3.400|28|749.640|5.901.520|8.666|-7.257|
|LT|Acceso LT-1|3.400|29|749.645|5.901.518|8.671|-7.259|
|LT|Acceso LT-1|3.400|30|749.647|5.901.514|8.674|-7.262|
|LT|Acceso LT-1|3.400|31|749.650|5.901.513|8.677|-7.264|
|LT|Acceso LT-1|3.400|32|749.653|5.901.511|8.680|-7.265|
|LT|Acceso LT-1|3.400|33|749.658|5.901.509|8.685|-7.267|
|LT|Acceso LT-1|3.400|34|749.663|5.901.506|8.689|-7.270|
|LT|Acceso LT-1|3.400|35|749.667|5.901.504|8.694|-7.272|
|LT|Acceso LT-1|3.400|36|749.671|5.901.502|8.698|-7.274|
|LT|Acceso LT-1|3.400|37|749.676|5.901.497|8.703|-7.279|
|LT|Acceso LT-1|3.400|38|749.680|5.901.494|8.707|-7.282|
|LT|Acceso LT-1|3.400|39|749.684|5.901.491|8.711|-7.284|
|LT|Acceso LT-1|3.400|40|749.689|5.901.489|8.716|-7.286|
|LT|Acceso LT-1|3.400|41|749.692|5.901.486|8.720|-7.289|
|LT|Acceso LT-1|3.400|42|749.696|5.901.483|8.723|-7.292|
|LT|Acceso LT-1|3.400|43|749.700|5.901.481|8.727|-7.294|
|LT|Acceso LT-1|3.400|44|749.703|5.901.479|8.731|-7.296|
|LT|Acceso LT-1|3.400|45|749.707|5.901.478|8.735|-7.297|
|LT|Acceso LT-1|3.400|46|749.711|5.901.475|8.739|-7.300|
|LT|Acceso LT-1|3.400|47|749.715|5.901.473|8.742|-7.302|
|LT|Acceso LT-1|3.400|48|749.716|5.901.471|8.744|-7.304|
|LT|Acceso LT-1|3.400|49|749.722|5.901.469|8.750|-7.306|
|LT|Acceso LT-1|3.400|50|749.726|5.901.466|8.754|-7.308|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 125

|Sector|Fuente|Largo (m)|Punto|UTM (WGS 84 - Z18)|Col6|LCC (km)|Col8|
|---|---|---|---|---|---|---|---|
|**Sector**|**Fuente**|**Largo (m)**|**Punto**|**Este (m)**|**Norte (m)**|**LCC-X**|**LCC-Y**|
|**Sector**|**Fuente**|**Largo (m)**|51|749.730|5.901.464|8.757|-7.310|
|**Sector**|**Fuente**|**Largo (m)**|52|749.733|5.901.460|8.761|-7.314|
|**Sector**|**Fuente**|**Largo (m)**|53|749.736|5.901.457|8.764|-7.317|
|**Sector**|**Fuente**|**Largo (m)**|54|749.738|5.901.454|8.766|-7.320|
|**Sector**|**Fuente**|**Largo (m)**|55|749.742|5.901.451|8.770|-7.323|
|**Sector**|**Fuente**|**Largo (m)**|56|749.744|5.901.446|8.772|-7.328|
|**Sector**|**Fuente**|**Largo (m)**|57|749.746|5.901.443|8.774|-7.331|
|**Sector**|**Fuente**|**Largo (m)**|58|749.749|5.901.439|8.778|-7.335|
|**Sector**|**Fuente**|**Largo (m)**|59|749.752|5.901.435|8.781|-7.338|
|**Sector**|**Fuente**|**Largo (m)**|60|749.756|5.901.432|8.785|-7.342|
|**Sector**|**Fuente**|**Largo (m)**|61|749.759|5.901.429|8.787|-7.344|
|**Sector**|**Fuente**|**Largo (m)**|62|749.763|5.901.426|8.792|-7.347|
|**Sector**|**Fuente**|**Largo (m)**|63|749.767|5.901.425|8.796|-7.349|
|**Sector**|**Fuente**|**Largo (m)**|64|749.771|5.901.422|8.801|-7.351|
|**Sector**|**Fuente**|**Largo (m)**|65|749.775|5.901.420|8.804|-7.353|
|**Sector**|**Fuente**|**Largo (m)**|66|749.779|5.901.418|8.808|-7.354|
|**Sector**|**Fuente**|**Largo (m)**|67|749.783|5.901.417|8.812|-7.356|
|**Sector**|**Fuente**|**Largo (m)**|68|749.787|5.901.415|8.817|-7.358|
|**Sector**|**Fuente**|**Largo (m)**|69|749.790|5.901.414|8.820|-7.358|
|**Sector**|**Fuente**|**Largo (m)**|70|749.795|5.901.413|8.825|-7.359|
|**Sector**|**Fuente**|**Largo (m)**|71|749.799|5.901.413|8.829|-7.359|
|**Sector**|**Fuente**|**Largo (m)**|72|749.802|5.901.411|8.831|-7.361|
|**Sector**|**Fuente**|**Largo (m)**|73|749.808|5.901.410|8.837|-7.362|
|**Sector**|**Fuente**|**Largo (m)**|74|749.813|5.901.409|8.842|-7.362|
|**Sector**|**Fuente**|**Largo (m)**|75|749.817|5.901.409|8.846|-7.363|
|**Sector**|**Fuente**|**Largo (m)**|76|749.823|5.901.408|8.852|-7.364|
|**Sector**|**Fuente**|**Largo (m)**|77|749.826|5.901.407|8.855|-7.364|
|**Sector**|**Fuente**|**Largo (m)**|78|749.830|5.901.406|8.860|-7.365|
|**Sector**|**Fuente**|**Largo (m)**|79|749.835|5.901.404|8.864|-7.368|
|**Sector**|**Fuente**|**Largo (m)**|80|749.840|5.901.403|8.869|-7.368|
|**Sector**|**Fuente**|**Largo (m)**|81|749.846|5.901.402|8.875|-7.369|
|**Sector**|**Fuente**|**Largo (m)**|82|749.851|5.901.401|8.880|-7.370|
|**Sector**|**Fuente**|**Largo (m)**|83|749.856|5.901.400|8.885|-7.371|
|**Sector**|**Fuente**|**Largo (m)**|84|749.860|5.901.399|8.890|-7.371|
|**Sector**|**Fuente**|**Largo (m)**|85|749.865|5.901.398|8.895|-7.372|
|**Sector**|**Fuente**|**Largo (m)**|86|749.869|5.901.398|8.899|-7.373|
|**Sector**|**Fuente**|**Largo (m)**|87|749.873|5.901.398|8.903|-7.372|
|**Sector**|**Fuente**|**Largo (m)**|88|749.877|5.901.398|8.907|-7.372|
|**Sector**|**Fuente**|**Largo (m)**|89|749.881|5.901.398|8.911|-7.372|
|**Sector**|**Fuente**|**Largo (m)**|90|749.885|5.901.398|8.915|-7.372|
|**Sector**|**Fuente**|**Largo (m)**|91|749.891|5.901.398|8.920|-7.372|
|**Sector**|**Fuente**|**Largo (m)**|92|749.894|5.901.397|8.924|-7.372|
|**Sector**|**Fuente**|**Largo (m)**|93|749.898|5.901.398|8.927|-7.372|
|**Sector**|**Fuente**|**Largo (m)**|94|749.901|5.901.397|8.931|-7.372|
|**Sector**|**Fuente**|**Largo (m)**|95|749.906|5.901.396|8.936|-7.373|
|**Sector**|**Fuente**|**Largo (m)**|96|749.911|5.901.394|8.941|-7.375|
|**Sector**|**Fuente**|**Largo (m)**|97|749.915|5.901.392|8.944|-7.377|
|**Sector**|**Fuente**|**Largo (m)**|98|749.918|5.901.389|8.948|-7.380|
|**Sector**|**Fuente**|**Largo (m)**|99|749.922|5.901.387|8.952|-7.381|
|**Sector**|**Fuente**|**Largo (m)**|100|749.925|5.901.385|8.955|-7.384|
|**Sector**|**Fuente**|**Largo (m)**|101|749.930|5.901.382|8.960|-7.386|
|**Sector**|**Fuente**|**Largo (m)**|102|749.934|5.901.380|8.964|-7.388|
|**Sector**|**Fuente**|**Largo (m)**|103|749.937|5.901.378|8.967|-7.391|
|**Sector**|**Fuente**|**Largo (m)**|104|749.941|5.901.376|8.971|-7.392|
|**Sector**|**Fuente**|**Largo (m)**|105|749.944|5.901.372|8.974|-7.396|
|**Sector**|**Fuente**|**Largo (m)**|106|749.946|5.901.369|8.977|-7.399|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 126

|Sector|Fuente|Largo (m)|Punto|UTM (WGS 84 - Z18)|Col6|LCC (km)|Col8|
|---|---|---|---|---|---|---|---|
|**Sector**|**Fuente**|**Largo (m)**|**Punto**|**Este (m)**|**Norte (m)**|**LCC-X**|**LCC-Y**|
|**Sector**|**Fuente**|**Largo (m)**|107|749.949|5.901.366|8.980|-7.401|
|**Sector**|**Fuente**|**Largo (m)**|108|749.953|5.901.363|8.984|-7.405|
|**Sector**|**Fuente**|**Largo (m)**|109|749.957|5.901.360|8.987|-7.408|
|**Sector**|**Fuente**|**Largo (m)**|110|749.960|5.901.356|8.991|-7.411|
|**Sector**|**Fuente**|**Largo (m)**|111|749.965|5.901.353|8.995|-7.414|
|**Sector**|**Fuente**|**Largo (m)**|112|749.969|5.901.351|9.000|-7.417|
|**Sector**|**Fuente**|**Largo (m)**|113|749.973|5.901.348|9.004|-7.419|
|**Sector**|**Fuente**|**Largo (m)**|114|749.977|5.901.346|9.008|-7.421|
|**Sector**|**Fuente**|**Largo (m)**|115|749.981|5.901.346|9.012|-7.421|
|**Sector**|**Fuente**|**Largo (m)**|116|749.984|5.901.345|9.015|-7.422|
|**Sector**|**Fuente**|**Largo (m)**|117|749.990|5.901.346|9.021|-7.421|
|**Sector**|**Fuente**|**Largo (m)**|118|749.996|5.901.347|9.027|-7.419|
|**Sector**|**Fuente**|**Largo (m)**|119|749.999|5.901.349|9.030|-7.418|
|**Sector**|**Fuente**|**Largo (m)**|120|750.003|5.901.351|9.034|-7.415|
|**Sector**|**Fuente**|**Largo (m)**|121|750.008|5.901.351|9.039|-7.415|
|**Sector**|**Fuente**|**Largo (m)**|122|750.013|5.901.351|9.043|-7.415|
|**Sector**|**Fuente**|**Largo (m)**|123|750.017|5.901.352|9.048|-7.414|
|**Sector**|**Fuente**|**Largo (m)**|124|750.020|5.901.352|9.051|-7.414|
|**Sector**|**Fuente**|**Largo (m)**|125|750.026|5.901.352|9.057|-7.414|
|**Sector**|**Fuente**|**Largo (m)**|126|750.030|5.901.351|9.061|-7.414|
|**Sector**|**Fuente**|**Largo (m)**|127|750.034|5.901.353|9.065|-7.413|
|**Sector**|**Fuente**|**Largo (m)**|128|750.039|5.901.352|9.070|-7.413|
|**Sector**|**Fuente**|**Largo (m)**|129|750.042|5.901.351|9.073|-7.414|
|**Sector**|**Fuente**|**Largo (m)**|130|750.047|5.901.350|9.078|-7.415|
|**Sector**|**Fuente**|**Largo (m)**|131|750.050|5.901.350|9.081|-7.415|
|**Sector**|**Fuente**|**Largo (m)**|132|750.055|5.901.349|9.085|-7.416|
|**Sector**|**Fuente**|**Largo (m)**|133|750.059|5.901.348|9.090|-7.416|
|**Sector**|**Fuente**|**Largo (m)**|134|750.064|5.901.347|9.095|-7.417|
|**Sector**|**Fuente**|**Largo (m)**|135|750.069|5.901.347|9.100|-7.418|
|**Sector**|**Fuente**|**Largo (m)**|136|750.074|5.901.345|9.105|-7.420|
|**Sector**|**Fuente**|**Largo (m)**|137|750.077|5.901.342|9.108|-7.422|
|**Sector**|**Fuente**|**Largo (m)**|138|750.081|5.901.340|9.112|-7.424|
|**Sector**|**Fuente**|**Largo (m)**|139|750.084|5.901.338|9.116|-7.426|
|**Sector**|**Fuente**|**Largo (m)**|140|750.088|5.901.336|9.119|-7.428|
|**Sector**|**Fuente**|**Largo (m)**|141|750.092|5.901.334|9.123|-7.430|
|**Sector**|**Fuente**|**Largo (m)**|142|750.095|5.901.330|9.126|-7.434|
|**Sector**|**Fuente**|**Largo (m)**|143|750.098|5.901.327|9.130|-7.436|
|**Sector**|**Fuente**|**Largo (m)**|144|750.102|5.901.325|9.133|-7.439|
|**Sector**|**Fuente**|**Largo (m)**|145|750.104|5.901.321|9.135|-7.442|
|**Sector**|**Fuente**|**Largo (m)**|146|750.106|5.901.319|9.138|-7.445|
|**Sector**|**Fuente**|**Largo (m)**|147|750.108|5.901.313|9.140|-7.450|
|**Sector**|**Fuente**|**Largo (m)**|148|750.110|5.901.310|9.142|-7.453|
|**Sector**|**Fuente**|**Largo (m)**|149|750.112|5.901.307|9.145|-7.456|
|**Sector**|**Fuente**|**Largo (m)**|150|750.115|5.901.305|9.147|-7.458|
|**Sector**|**Fuente**|**Largo (m)**|151|750.124|5.901.276|9.157|-7.487|
|**Sector**|**Fuente**|**Largo (m)**|152|750.138|5.901.235|9.172|-7.528|
|**Sector**|**Fuente**|**Largo (m)**|153|750.148|5.901.204|9.183|-7.558|
|**Sector**|**Fuente**|**Largo (m)**|154|750.149|5.901.201|9.184|-7.561|
|**Sector**|**Fuente**|**Largo (m)**|155|750.162|5.901.178|9.197|-7.583|
|**Sector**|**Fuente**|**Largo (m)**|156|750.164|5.901.175|9.199|-7.586|
|**Sector**|**Fuente**|**Largo (m)**|157|750.166|5.901.172|9.202|-7.590|
|**Sector**|**Fuente**|**Largo (m)**|158|750.168|5.901.169|9.204|-7.593|
|**Sector**|**Fuente**|**Largo (m)**|159|750.171|5.901.164|9.207|-7.597|
|**Sector**|**Fuente**|**Largo (m)**|160|750.174|5.901.162|9.210|-7.599|
|**Sector**|**Fuente**|**Largo (m)**|161|750.176|5.901.159|9.212|-7.602|
|**Sector**|**Fuente**|**Largo (m)**|162|750.179|5.901.156|9.215|-7.605|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 127

|Sector|Fuente|Largo (m)|Punto|UTM (WGS 84 - Z18)|Col6|LCC (km)|Col8|
|---|---|---|---|---|---|---|---|
|**Sector**|**Fuente**|**Largo (m)**|**Punto**|**Este (m)**|**Norte (m)**|**LCC-X**|**LCC-Y**|
|**Sector**|**Fuente**|**Largo (m)**|163|750.181|5.901.152|9.218|-7.609|
|**Sector**|**Fuente**|**Largo (m)**|164|750.185|5.901.148|9.222|-7.613|
|**Sector**|**Fuente**|**Largo (m)**|165|750.188|5.901.144|9.225|-7.616|
|**Sector**|**Fuente**|**Largo (m)**|166|750.213|5.901.112|9.250|-7.648|
|**Sector**|**Fuente**|**Largo (m)**|167|750.232|5.901.096|9.270|-7.664|
|**Sector**|**Fuente**|**Largo (m)**|168|750.264|5.901.069|9.303|-7.690|
|**Sector**|**Fuente**|**Largo (m)**|169|750.276|5.901.065|9.314|-7.693|
|**Sector**|**Fuente**|**Largo (m)**|170|750.284|5.901.064|9.323|-7.694|
|**Sector**|**Fuente**|**Largo (m)**|171|750.290|5.901.080|9.329|-7.677|
|**Sector**|**Fuente**|**Largo (m)**|172|750.301|5.901.101|9.339|-7.656|
|**Sector**|**Fuente**|**Largo (m)**|173|750.313|5.901.121|9.350|-7.636|
|**Sector**|**Fuente**|**Largo (m)**|174|750.326|5.901.144|9.362|-7.612|
|**Sector**|**Fuente**|**Largo (m)**|175|750.345|5.901.172|9.381|-7.585|
|**Sector**|**Fuente**|**Largo (m)**|176|750.364|5.901.189|9.399|-7.567|
|**Sector**|**Fuente**|**Largo (m)**|177|750.387|5.901.204|9.421|-7.551|
|**Sector**|**Fuente**|**Largo (m)**|178|750.421|5.901.225|9.456|-7.529|
|**Sector**|**Fuente**|**Largo (m)**|179|750.441|5.901.242|9.474|-7.512|
|**Sector**|**Fuente**|**Largo (m)**|180|750.467|5.901.266|9.500|-7.487|
|**Sector**|**Fuente**|**Largo (m)**|181|750.485|5.901.285|9.518|-7.467|
|**Sector**|**Fuente**|**Largo (m)**|182|750.510|5.901.312|9.542|-7.440|
|**Sector**|**Fuente**|**Largo (m)**|183|750.526|5.901.346|9.556|-7.405|
|**Sector**|**Fuente**|**Largo (m)**|184|750.559|5.901.397|9.588|-7.354|
|**Sector**|**Fuente**|**Largo (m)**|185|750.577|5.901.431|9.606|-7.319|
|**Sector**|**Fuente**|**Largo (m)**|186|750.615|5.901.494|9.641|-7.255|
|**Sector**|**Fuente**|**Largo (m)**|187|750.662|5.901.563|9.687|-7.185|
|**Sector**|**Fuente**|**Largo (m)**|188|750.749|5.901.675|9.770|-7.070|
|**Sector**|**Fuente**|**Largo (m)**|189|750.765|5.901.703|9.786|-7.042|
|**Sector**|**Fuente**|**Largo (m)**|190|750.784|5.901.748|9.803|-6.996|
|**Sector**|**Fuente**|**Largo (m)**|191|750.834|5.901.877|9.849|-6.866|
|**Sector**|**Fuente**|**Largo (m)**|192|750.889|5.902.024|9.900|-6.718|
|**Sector**|**Fuente**|**Largo (m)**|193|750.932|5.902.133|9.940|-6.607|
|**Sector**|**Fuente**|**Largo (m)**|194|751.000|5.902.288|10.003|-6.450|
|**Sector**|**Fuente**|**Largo (m)**|195|751.082|5.902.477|10.080|-6.260|
|**Sector**|**Fuente**|**Largo (m)**|196|751.165|5.902.662|10.158|-6.072|
|**Sector**|**Fuente**|**Largo (m)**|197|751.242|5.902.837|10.230|-5.895|
|**Sector**|**Fuente**|**Largo (m)**|198|751.370|5.903.130|10.350|-5.599|
|**Sector**|**Fuente**|**Largo (m)**|199|751.368|5.903.135|10.347|-5.594|
|**Sector**|Acceso LT-2|637|1|750.276|5.901.069|9.315|-7.689|
|**Sector**|Acceso LT-2|637|2|750.261|5.900.949|9.303|-7.809|
|**Sector**|Acceso LT-2|637|3|750.253|5.900.903|9.297|-7.856|
|**Sector**|Acceso LT-2|637|4|750.252|5.900.873|9.296|-7.886|
|**Sector**|Acceso LT-2|637|5|750.299|5.900.740|9.347|-8.017|
|**Sector**|Acceso LT-2|637|6|750.303|5.900.617|9.354|-8.141|
|**Sector**|Acceso LT-2|637|7|750.301|5.900.441|9.357|-8.316|
|**Sector**|Acceso LT-3|656|1|750.244|5.900.034|9.312|-8.724|
|**Sector**|Acceso LT-3|656|2|750.242|5.899.875|9.314|-8.883|
|**Sector**|Acceso LT-3|656|3|750.210|5.899.756|9.286|-9.003|
|**Sector**|Acceso LT-3|656|4|749.891|5.899.576|8.973|-9.193|
|**Sector**|Acceso LT-3|656|5|749.886|5.899.571|8.968|-9.198|
|**Sector**|Acceso LT-4|1.879|1|750.207|5.899.759|9.283|-9.000|
|**Sector**|Acceso LT-4|1.879|2|750.174|5.899.464|9.258|-9.296|
|**Sector**|Acceso LT-4|1.879|3|750.161|5.899.399|9.247|-9.362|
|**Sector**|Acceso LT-4|1.879|4|750.147|5.899.342|9.235|-9.419|
|**Sector**|Acceso LT-4|1.879|5|750.148|5.899.285|9.237|-9.476|
|**Sector**|Acceso LT-4|1.879|6|750.106|5.899.193|9.198|-9.569|
|**Sector**|Acceso LT-4|1.879|7|750.098|5.899.144|9.191|-9.617|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 128

|Sector|Fuente|Largo (m)|Punto|UTM (WGS 84 - Z18)|Col6|LCC (km)|Col8|
|---|---|---|---|---|---|---|---|
|**Sector**|**Fuente**|**Largo (m)**|**Punto**|**Este (m)**|**Norte (m)**|**LCC-X**|**LCC-Y**|
|**Sector**|**Fuente**|**Largo (m)**|8|750.104|5.899.090|9.200|-9.671|
|**Sector**|**Fuente**|**Largo (m)**|9|750.119|5.899.021|9.217|-9.741|
|**Sector**|**Fuente**|**Largo (m)**|10|750.115|5.898.923|9.215|-9.839|
|**Sector**|**Fuente**|**Largo (m)**|11|750.078|5.898.701|9.184|-10.061|
|**Sector**|**Fuente**|**Largo (m)**|12|750.077|5.898.680|9.184|-10.082|
|**Sector**|**Fuente**|**Largo (m)**|13|750.203|5.898.449|9.316|-10.309|
|**Sector**|**Fuente**|**Largo (m)**|14|750.239|5.898.366|9.355|-10.391|
|**Sector**|**Fuente**|**Largo (m)**|15|750.274|5.898.285|9.392|-10.472|
|**Sector**|**Fuente**|**Largo (m)**|16|750.293|5.898.244|9.412|-10.511|
|**Sector**|**Fuente**|**Largo (m)**|17|750.307|5.898.208|9.427|-10.547|
|**Sector**|**Fuente**|**Largo (m)**|18|750.330|5.898.198|9.450|-10.556|
|**Sector**|**Fuente**|**Largo (m)**|19|750.343|5.898.207|9.463|-10.547|
|**Sector**|**Fuente**|**Largo (m)**|20|750.359|5.898.228|9.479|-10.526|
|**Sector**|**Fuente**|**Largo (m)**|21|750.368|5.898.261|9.487|-10.492|
|**Sector**|**Fuente**|**Largo (m)**|22|750.393|5.898.288|9.511|-10.465|
|**Sector**|**Fuente**|**Largo (m)**|23|750.440|5.898.333|9.556|-10.418|
|**Sector**|**Fuente**|**Largo (m)**|24|750.477|5.898.370|9.592|-10.381|
|PE|Camino Interior 1|2.916|1|754.495|5.897.923|13.620|-10.713|
|PE|Camino Interior 1|2.916|2|754.461|5.897.882|13.587|-10.755|
|PE|Camino Interior 1|2.916|3|754.327|5.897.757|13.456|-10.883|
|PE|Camino Interior 1|2.916|4|754.232|5.897.697|13.363|-10.946|
|PE|Camino Interior 1|2.916|5|754.149|5.897.675|13.281|-10.971|
|PE|Camino Interior 1|2.916|6|754.011|5.897.652|13.144|-10.997|
|PE|Camino Interior 1|2.916|7|753.917|5.897.579|13.053|-11.073|
|PE|Camino Interior 1|2.916|8|753.879|5.897.521|13.016|-11.132|
|PE|Camino Interior 1|2.916|9|753.778|5.897.159|12.925|-11.496|
|PE|Camino Interior 1|2.916|10|753.794|5.897.097|12.943|-11.558|
|PE|Camino Interior 1|2.916|11|753.846|5.897.044|12.996|-11.610|
|PE|Camino Interior 1|2.916|12|754.194|5.896.951|13.346|-11.692|
|PE|Camino Interior 1|2.916|13|754.328|5.896.895|13.482|-11.744|
|PE|Camino Interior 1|2.916|14|754.356|5.896.830|13.512|-11.809|
|PE|Camino Interior 1|2.916|15|754.264|5.896.605|13.426|-12.036|
|PE|Camino Interior 1|2.916|16|754.211|5.896.586|13.374|-12.057|
|PE|Camino Interior 1|2.916|17|754.126|5.896.615|13.288|-12.031|
|PE|Camino Interior 1|2.916|18|754.057|5.896.672|13.218|-11.975|
|PE|Camino Interior 1|2.916|19|753.901|5.896.679|13.062|-11.973|
|PE|Camino Interior 1|2.916|20|753.821|5.896.650|12.982|-12.004|
|PE|Camino Interior 1|2.916|21|753.721|5.896.576|12.885|-12.080|
|PE|Camino Interior 1|2.916|22|753.641|5.896.568|12.805|-12.091|
|PE|Camino Interior 1|2.916|23|753.507|5.896.606|12.670|-12.057|
|PE|Camino Interior 2|3.739|1|753.239|5.896.689|12.400|-11.982|
|PE|Camino Interior 2|3.739|2|752.724|5.896.841|11.881|-11.845|
|PE|Camino Interior 2|3.739|3|752.700|5.896.870|11.856|-11.816|
|PE|Camino Interior 2|3.739|4|752.575|5.897.153|11.723|-11.537|
|PE|Camino Interior 2|3.739|5|752.539|5.897.184|11.687|-11.506|
|PE|Camino Interior 2|3.739|6|752.351|5.897.260|11.497|-11.437|
|PE|Camino Interior 2|3.739|7|752.306|5.897.268|11.451|-11.429|
|PE|Camino Interior 2|3.739|8|752.121|5.897.239|11.267|-11.464|
|PE|Camino Interior 2|3.739|9|751.926|5.897.226|11.073|-11.483|
|PE|Camino Interior 2|3.739|10|751.715|5.897.154|10.864|-11.560|
|PE|Camino Interior 2|3.739|11|751.542|5.897.135|10.692|-11.584|
|PE|Camino Interior 2|3.739|12|751.475|5.897.150|10.624|-11.571|
|PE|Camino Interior 2|3.739|13|751.168|5.897.315|10.313|-11.414|
|PE|Camino Interior 2|3.739|14|750.904|5.897.442|10.045|-11.296|
|PE|Camino Interior 2|3.739|15|750.834|5.897.454|9.975|-11.285|
|PE|Camino Interior 2|3.739|16|750.664|5.897.423|9.806|-11.322|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 129

|Sector|Fuente|Largo (m)|Punto|UTM (WGS 84 - Z18)|Col6|LCC (km)|Col8|
|---|---|---|---|---|---|---|---|
|**Sector**|**Fuente**|**Largo (m)**|**Punto**|**Este (m)**|**Norte (m)**|**LCC-X**|**LCC-Y**|
|**Sector**|**Fuente**|**Largo (m)**|17|750.596|5.897.429|9.738|-11.317|
|**Sector**|**Fuente**|**Largo (m)**|18|750.432|5.897.507|9.571|-11.244|
|**Sector**|**Fuente**|**Largo (m)**|19|750.369|5.897.505|9.509|-11.248|
|**Sector**|**Fuente**|**Largo (m)**|20|750.338|5.897.530|9.477|-11.224|
|**Sector**|**Fuente**|**Largo (m)**|21|750.291|5.897.695|9.425|-11.060|
|**Sector**|**Fuente**|**Largo (m)**|22|750.256|5.897.788|9.388|-10.968|
|**Sector**|**Fuente**|**Largo (m)**|23|750.329|5.897.901|9.458|-10.853|
|**Sector**|**Fuente**|**Largo (m)**|24|750.351|5.897.953|9.478|-10.801|
|**Sector**|**Fuente**|**Largo (m)**|25|750.346|5.897.963|9.473|-10.791|
|**Sector**|Camino Interior 3|191|1|754.330|5.896.896|13.484|-11.743|
|**Sector**|Camino Interior 3|191|2|754.375|5.896.880|13.530|-11.758|
|**Sector**|Camino Interior 3|191|3|754.389|5.896.894|13.544|-11.744|
|**Sector**|Camino Interior 3|191|4|754.392|5.896.912|13.546|-11.726|
|**Sector**|Camino Interior 3|191|5|754.346|5.896.971|13.498|-11.668|
|**Sector**|Camino Interior 3|191|6|754.322|5.896.989|13.474|-11.651|
|**Sector**|Camino Interior 4|238|1|754.262|5.896.603|13.424|-12.038|
|**Sector**|Camino Interior 4|238|2|754.253|5.896.564|13.417|-12.077|
|**Sector**|Camino Interior 4|238|3|754.264|5.896.526|13.429|-12.115|
|**Sector**|Camino Interior 4|238|4|754.325|5.896.380|13.494|-12.259|
|**Sector**|Camino Interior 5|2.966|1|754.271|5.896.615|13.433|-12.026|
|**Sector**|Camino Interior 5|2.966|2|754.285|5.896.570|13.449|-12.071|
|**Sector**|Camino Interior 5|2.966|3|754.314|5.896.544|13.479|-12.096|
|**Sector**|Camino Interior 5|2.966|4|754.465|5.896.483|13.631|-12.152|
|**Sector**|Camino Interior 5|2.966|5|754.681|5.896.454|13.848|-12.175|
|**Sector**|Camino Interior 5|2.966|6|754.714|5.896.447|13.881|-12.181|
|**Sector**|Camino Interior 5|2.966|7|754.829|5.896.392|13.997|-12.233|
|**Sector**|Camino Interior 5|2.966|8|755.053|5.896.386|14.221|-12.233|
|**Sector**|Camino Interior 5|2.966|9|755.144|5.896.374|14.312|-12.242|
|**Sector**|Camino Interior 5|2.966|10|755.449|5.896.367|14.617|-12.241|
|**Sector**|Camino Interior 5|2.966|11|755.519|5.896.375|14.687|-12.230|
|**Sector**|Camino Interior 5|2.966|12|755.714|5.896.370|14.882|-12.229|
|**Sector**|Camino Interior 5|2.966|13|755.762|5.896.337|14.931|-12.261|
|**Sector**|Camino Interior 5|2.966|14|755.785|5.896.280|14.955|-12.317|
|**Sector**|Camino Interior 5|2.966|15|755.789|5.896.097|14.964|-12.500|
|**Sector**|Camino Interior 5|2.966|16|755.780|5.895.757|14.965|-12.841|
|**Sector**|Camino Interior 5|2.966|17|755.775|5.895.466|14.969|-13.132|
|**Sector**|Camino Interior 5|2.966|18|755.789|5.895.426|14.984|-13.171|
|**Sector**|Camino Interior 5|2.966|19|755.830|5.895.399|15.026|-13.197|
|**Sector**|Camino Interior 5|2.966|20|755.921|5.895.374|15.117|-13.219|
|**Sector**|Camino Interior 5|2.966|21|755.998|5.895.327|15.196|-13.264|
|**Sector**|Camino Interior 5|2.966|22|756.168|5.895.154|15.370|-13.431|
|**Sector**|Ruta N-85|22.758|1|736.364|5.908.534|-4.799|-0.625|
|**Sector**|Ruta N-85|22.758|2|736.977|5.908.480|-4.185|-0.662|
|**Sector**|Ruta N-85|22.758|3|737.790|5.908.487|-3.372|-0.632|
|**Sector**|Ruta N-85|22.758|4|738.823|5.908.486|-2.341|-0.604|
|**Sector**|Ruta N-85|22.758|5|739.220|5.908.495|-1.944|-0.584|
|**Sector**|Ruta N-85|22.758|6|739.369|5.908.493|-1.795|-0.581|
|**Sector**|Ruta N-85|22.758|7|739.940|5.908.002|-1.210|-1.056|
|**Sector**|Ruta N-85|22.758|8|740.261|5.907.725|-0.882|-1.323|
|**Sector**|Ruta N-85|22.758|9|740.644|5.907.462|-0.491|-1.575|
|**Sector**|Ruta N-85|22.758|10|740.839|5.907.401|-0.295|-1.630|
|**Sector**|Ruta N-85|22.758|11|740.926|5.907.388|-0.208|-1.641|
|**Sector**|Ruta N-85|22.758|12|740.999|5.907.377|-0.135|-1.650|
|**Sector**|Ruta N-85|22.758|13|741.322|5.907.157|0.195|-1.860|
|**Sector**|Ruta N-85|22.758|14|741.540|5.907.021|0.416|-1.990|
|**Sector**|Ruta N-85|22.758|15|742.595|5.906.396|1.488|-2.585|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 130

|Sector|Fuente|Largo (m)|Punto|UTM (WGS 84 - Z18)|Col6|LCC (km)|Col8|
|---|---|---|---|---|---|---|---|
|**Sector**|**Fuente**|**Largo (m)**|**Punto**|**Este (m)**|**Norte (m)**|**LCC-X**|**LCC-Y**|
|**Sector**|**Fuente**|**Largo (m)**|16|743.154|5.906.084|2.056|-2.880|
|**Sector**|**Fuente**|**Largo (m)**|17|743.500|5.905.936|2.406|-3.019|
|**Sector**|**Fuente**|**Largo (m)**|18|743.700|5.905.855|2.608|-3.094|
|**Sector**|**Fuente**|**Largo (m)**|19|743.975|5.905.783|2.885|-3.159|
|**Sector**|**Fuente**|**Largo (m)**|20|744.145|5.905.715|3.057|-3.221|
|**Sector**|**Fuente**|**Largo (m)**|21|744.348|5.905.731|3.258|-3.200|
|**Sector**|**Fuente**|**Largo (m)**|22|744.914|5.905.552|3.829|-3.363|
|**Sector**|**Fuente**|**Largo (m)**|23|745.152|5.905.478|4.069|-3.429|
|**Sector**|**Fuente**|**Largo (m)**|24|745.481|5.905.233|4.405|-3.665|
|**Sector**|**Fuente**|**Largo (m)**|25|745.743|5.905.070|4.672|-3.820|
|**Sector**|**Fuente**|**Largo (m)**|26|746.140|5.904.822|5.075|-4.057|
|**Sector**|**Fuente**|**Largo (m)**|27|746.498|5.904.509|5.442|-4.359|
|**Sector**|**Fuente**|**Largo (m)**|28|747.249|5.904.088|6.204|-4.759|
|**Sector**|**Fuente**|**Largo (m)**|29|747.369|5.904.043|6.326|-4.800|
|**Sector**|**Fuente**|**Largo (m)**|30|747.628|5.903.952|6.587|-4.884|
|**Sector**|**Fuente**|**Largo (m)**|31|748.402|5.903.799|7.365|-5.015|
|**Sector**|**Fuente**|**Largo (m)**|32|749.558|5.903.638|8.524|-5.143|
|**Sector**|**Fuente**|**Largo (m)**|33|749.896|5.903.575|8.863|-5.196|
|**Sector**|**Fuente**|**Largo (m)**|34|750.131|5.903.495|9.100|-5.269|
|**Sector**|**Fuente**|**Largo (m)**|35|750.288|5.903.491|9.258|-5.269|
|**Sector**|**Fuente**|**Largo (m)**|36|750.540|5.903.459|9.511|-5.293|
|**Sector**|**Fuente**|**Largo (m)**|37|751.219|5.903.132|10.199|-5.601|
|**Sector**|**Fuente**|**Largo (m)**|38|753.279|5.903.265|12.253|-5.410|
|**Sector**|**Fuente**|**Largo (m)**|39|755.537|5.903.405|14.505|-5.205|
|**Sector**|**Fuente**|**Largo (m)**|40|756.353|5.903.458|15.319|-5.130|
|**Sector**|**Fuente**|**Largo (m)**|41|756.698|5.903.506|15.662|-5.072|
|**Sector**|**Fuente**|**Largo (m)**|42|757.041|5.903.328|16.010|-5.240|
|**Sector**|**Fuente**|**Largo (m)**|43|757.479|5.903.249|16.450|-5.307|
|**Sector**|**Fuente**|**Largo (m)**|44|757.636|5.903.188|16.608|-5.362|
|PE LT|Rutas 5 y 152|113.000|1|736.368|5.908.546|-4.795|-0.614|
|PE LT|Rutas 5 y 152|113.000|2|736.489|5.909.133|-4.691|-0.023|
|PE LT|Rutas 5 y 152|113.000|3|736.471|5.909.170|-4.711|0.014|
|PE LT|Rutas 5 y 152|113.000|4|736.460|5.909.181|-4.721|0.024|
|PE LT|Rutas 5 y 152|113.000|5|736.445|5.909.185|-4.737|0.028|
|PE LT|Rutas 5 y 152|113.000|6|736.436|5.909.191|-4.746|0.033|
|PE LT|Rutas 5 y 152|113.000|7|736.423|5.909.202|-4.760|0.044|
|PE LT|Rutas 5 y 152|113.000|8|736.410|5.909.206|-4.772|0.047|
|PE LT|Rutas 5 y 152|113.000|9|736.393|5.909.215|-4.790|0.056|
|PE LT|Rutas 5 y 152|113.000|10|736.378|5.909.222|-4.805|0.063|
|PE LT|Rutas 5 y 152|113.000|11|736.369|5.909.225|-4.814|0.065|
|PE LT|Rutas 5 y 152|113.000|12|736.350|5.909.231|-4.833|0.070|
|PE LT|Rutas 5 y 152|113.000|13|736.335|5.909.235|-4.848|0.074|
|PE LT|Rutas 5 y 152|113.000|14|736.319|5.909.240|-4.864|0.078|
|PE LT|Rutas 5 y 152|113.000|15|736.303|5.909.241|-4.880|0.079|
|PE LT|Rutas 5 y 152|113.000|16|736.293|5.909.240|-4.891|0.078|
|PE LT|Rutas 5 y 152|113.000|17|736.279|5.909.240|-4.904|0.078|
|PE LT|Rutas 5 y 152|113.000|18|736.261|5.909.246|-4.923|0.083|
|PE LT|Rutas 5 y 152|113.000|19|736.248|5.909.249|-4.935|0.086|
|PE LT|Rutas 5 y 152|113.000|20|736.236|5.909.253|-4.948|0.089|
|PE LT|Rutas 5 y 152|113.000|21|736.220|5.909.257|-4.963|0.093|
|PE LT|Rutas 5 y 152|113.000|22|736.214|5.909.259|-4.969|0.095|
|PE LT|Rutas 5 y 152|113.000|23|736.192|5.909.265|-4.991|0.101|
|PE LT|Rutas 5 y 152|113.000|24|736.180|5.909.269|-5.004|0.104|
|PE LT|Rutas 5 y 152|113.000|25|736.168|5.909.272|-5.016|0.107|
|PE LT|Rutas 5 y 152|113.000|26|736.157|5.909.283|-5.027|0.117|
|PE LT|Rutas 5 y 152|113.000|27|736.157|5.909.297|-5.028|0.132|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 131

|Sector|Fuente|Largo (m)|Punto|UTM (WGS 84 - Z18)|Col6|LCC (km)|Col8|
|---|---|---|---|---|---|---|---|
|**Sector**|**Fuente**|**Largo (m)**|**Punto**|**Este (m)**|**Norte (m)**|**LCC-X**|**LCC-Y**|
|**Sector**|**Fuente**|**Largo (m)**|28|736.158|5.909.315|-5.027|0.149|
|**Sector**|**Fuente**|**Largo (m)**|29|736.162|5.909.332|-5.023|0.166|
|**Sector**|**Fuente**|**Largo (m)**|30|736.166|5.909.349|-5.020|0.184|
|**Sector**|**Fuente**|**Largo (m)**|31|736.171|5.909.366|-5.016|0.201|
|**Sector**|**Fuente**|**Largo (m)**|32|736.177|5.909.379|-5.010|0.214|
|**Sector**|**Fuente**|**Largo (m)**|33|736.189|5.909.387|-4.998|0.222|
|**Sector**|**Fuente**|**Largo (m)**|34|736.207|5.909.392|-4.980|0.228|
|**Sector**|**Fuente**|**Largo (m)**|35|736.222|5.909.399|-4.965|0.235|
|**Sector**|**Fuente**|**Largo (m)**|36|736.234|5.909.407|-4.954|0.243|
|**Sector**|**Fuente**|**Largo (m)**|37|736.252|5.909.412|-4.936|0.249|
|**Sector**|**Fuente**|**Largo (m)**|38|736.265|5.909.423|-4.923|0.260|
|**Sector**|**Fuente**|**Largo (m)**|39|736.278|5.909.434|-4.911|0.272|
|**Sector**|**Fuente**|**Largo (m)**|40|736.288|5.909.446|-4.901|0.284|
|**Sector**|**Fuente**|**Largo (m)**|41|736.298|5.909.462|-4.891|0.300|
|**Sector**|**Fuente**|**Largo (m)**|42|736.304|5.909.471|-4.886|0.310|
|**Sector**|**Fuente**|**Largo (m)**|43|736.315|5.909.487|-4.875|0.325|
|**Sector**|**Fuente**|**Largo (m)**|44|736.322|5.909.503|-4.868|0.342|
|**Sector**|**Fuente**|**Largo (m)**|45|736.329|5.909.516|-4.862|0.355|
|**Sector**|**Fuente**|**Largo (m)**|46|736.333|5.909.534|-4.858|0.373|
|**Sector**|**Fuente**|**Largo (m)**|47|736.335|5.909.556|-4.857|0.395|
|**Sector**|**Fuente**|**Largo (m)**|48|736.336|5.909.570|-4.857|0.410|
|**Sector**|**Fuente**|**Largo (m)**|49|736.338|5.909.592|-4.855|0.432|
|**Sector**|**Fuente**|**Largo (m)**|50|736.337|5.909.604|-4.856|0.443|
|**Sector**|**Fuente**|**Largo (m)**|51|736.339|5.909.611|-4.854|0.450|
|**Sector**|**Fuente**|**Largo (m)**|52|736.982|5.912.690|-4.300|3.545|
|**Sector**|**Fuente**|**Largo (m)**|53|737.400|5.913.810|-3.914|4.676|
|**Sector**|**Fuente**|**Largo (m)**|54|738.798|5.917.487|-2.621|8.390|
|**Sector**|**Fuente**|**Largo (m)**|55|738.434|5.920.214|-3.062|11.105|
|**Sector**|**Fuente**|**Largo (m)**|56|738.363|5.921.143|-3.159|12.032|
|**Sector**|**Fuente**|**Largo (m)**|57|738.332|5.921.619|-3.204|12.507|
|**Sector**|**Fuente**|**Largo (m)**|58|738.211|5.923.269|-3.371|14.152|
|**Sector**|**Fuente**|**Largo (m)**|59|740.529|5.927.969|-1.188|18.913|
|**Sector**|**Fuente**|**Largo (m)**|60|741.313|5.928.779|-0.428|19.745|
|**Sector**|**Fuente**|**Largo (m)**|61|742.276|5.929.488|0.514|20.481|
|**Sector**|**Fuente**|**Largo (m)**|62|743.457|5.932.152|1.620|23.176|
|**Sector**|**Fuente**|**Largo (m)**|63|743.459|5.932.816|1.603|23.840|
|**Sector**|**Fuente**|**Largo (m)**|64|744.013|5.933.974|2.123|25.013|
|**Sector**|**Fuente**|**Largo (m)**|65|744.142|5.934.339|2.242|25.381|
|**Sector**|**Fuente**|**Largo (m)**|66|745.543|5.936.573|3.579|27.654|
|**Sector**|**Fuente**|**Largo (m)**|67|745.589|5.937.294|3.605|28.374|
|**Sector**|**Fuente**|**Largo (m)**|68|745.973|5.937.794|3.974|28.886|
|**Sector**|**Fuente**|**Largo (m)**|69|746.540|5.939.060|4.505|30.166|
|**Sector**|**Fuente**|**Largo (m)**|70|747.493|5.939.804|5.437|30.937|
|**Sector**|**Fuente**|**Largo (m)**|71|747.278|5.939.933|5.218|31.060|
|**Sector**|**Fuente**|**Largo (m)**|72|746.919|5.939.980|4.858|31.096|
|**Sector**|**Fuente**|**Largo (m)**|73|746.140|5.939.690|4.088|30.785|
|**Sector**|**Fuente**|**Largo (m)**|74|745.199|5.939.314|3.158|30.382|
|**Sector**|**Fuente**|**Largo (m)**|75|744.924|5.939.262|2.884|30.322|
|**Sector**|**Fuente**|**Largo (m)**|76|743.888|5.939.540|1.841|30.571|
|**Sector**|**Fuente**|**Largo (m)**|77|743.711|5.939.591|1.663|30.617|
|**Sector**|**Fuente**|**Largo (m)**|78|743.543|5.939.570|1.496|30.592|
|**Sector**|**Fuente**|**Largo (m)**|79|743.405|5.939.541|1.359|30.558|
|**Sector**|**Fuente**|**Largo (m)**|80|743.238|5.939.520|1.193|30.533|
|**Sector**|**Fuente**|**Largo (m)**|81|743.041|5.939.508|0.996|30.515|
|**Sector**|**Fuente**|**Largo (m)**|82|742.884|5.939.519|0.839|30.522|
|**Sector**|**Fuente**|**Largo (m)**|83|742.717|5.939.498|0.673|30.496|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 132

|Sector|Fuente|Largo (m)|Punto|UTM (WGS 84 - Z18)|Col6|LCC (km)|Col8|
|---|---|---|---|---|---|---|---|
|**Sector**|**Fuente**|**Largo (m)**|**Punto**|**Este (m)**|**Norte (m)**|**LCC-X**|**LCC-Y**|
|**Sector**|**Fuente**|**Largo (m)**|84|742.560|5.939.509|0.515|30.503|
|**Sector**|**Fuente**|**Largo (m)**|85|742.432|5.939.511|0.387|30.501|
|**Sector**|**Fuente**|**Largo (m)**|86|742.275|5.939.522|0.230|30.508|
|**Sector**|**Fuente**|**Largo (m)**|87|742.137|5.939.493|0.094|30.475|
|**Sector**|**Fuente**|**Largo (m)**|88|742.049|5.939.518|0.005|30.498|
|**Sector**|**Fuente**|**Largo (m)**|89|741.892|5.939.529|-0.153|30.504|
|**Sector**|**Fuente**|**Largo (m)**|90|741.764|5.939.532|-0.280|30.503|
|**Sector**|**Fuente**|**Largo (m)**|91|741.617|5.939.574|-0.429|30.541|
|**Sector**|**Fuente**|**Largo (m)**|92|741.382|5.939.539|-0.663|30.499|
|**Sector**|**Fuente**|**Largo (m)**|93|741.254|5.939.541|-0.790|30.498|
|**Sector**|**Fuente**|**Largo (m)**|94|741.186|5.939.527|-0.858|30.482|
|**Sector**|**Fuente**|**Largo (m)**|95|741.038|5.939.569|-1.007|30.520|
|**Sector**|**Fuente**|**Largo (m)**|96|740.872|5.939.548|-1.172|30.495|
|**Sector**|**Fuente**|**Largo (m)**|97|740.695|5.939.600|-1.351|30.541|
|**Sector**|**Fuente**|**Largo (m)**|98|740.538|5.939.611|-1.508|30.547|
|**Sector**|**Fuente**|**Largo (m)**|99|740.420|5.939.645|-1.627|30.578|
|**Sector**|**Fuente**|**Largo (m)**|100|740.263|5.939.656|-1.784|30.584|
|**Sector**|**Fuente**|**Largo (m)**|101|740.136|5.939.658|-1.911|30.583|
|**Sector**|**Fuente**|**Largo (m)**|102|740.018|5.939.692|-2.030|30.614|
|**Sector**|**Fuente**|**Largo (m)**|103|739.832|5.939.711|-2.217|30.628|
|**Sector**|**Fuente**|**Largo (m)**|104|739.714|5.939.746|-2.336|30.659|
|**Sector**|**Fuente**|**Largo (m)**|105|739.577|5.939.716|-2.471|30.626|
|**Sector**|**Fuente**|**Largo (m)**|106|739.391|5.939.736|-2.658|30.640|
|**Sector**|**Fuente**|**Largo (m)**|107|739.264|5.939.738|-2.785|30.639|
|**Sector**|**Fuente**|**Largo (m)**|108|739.107|5.939.749|-2.942|30.645|
|**Sector**|**Fuente**|**Largo (m)**|109|738.942|5.939.728|-3.107|30.620|
|**Sector**|**Fuente**|**Largo (m)**|110|738.903|5.939.705|-3.144|30.596|
|**Sector**|**Fuente**|**Largo (m)**|111|738.440|5.939.873|-3.612|30.750|
|**Sector**|**Fuente**|**Largo (m)**|112|737.875|5.940.139|-4.184|31.000|
|**Sector**|**Fuente**|**Largo (m)**|113|737.554|5.940.369|-4.511|31.221|
|**Sector**|**Fuente**|**Largo (m)**|114|736.799|5.940.175|-5.260|31.006|
|**Sector**|**Fuente**|**Largo (m)**|115|733.034|5.940.238|-9.024|30.962|
|**Sector**|**Fuente**|**Largo (m)**|116|732.428|5.940.481|-9.637|31.188|
|**Sector**|**Fuente**|**Largo (m)**|117|730.146|5.940.595|-11.920|31.238|
|**Sector**|**Fuente**|**Largo (m)**|118|729.403|5.940.371|-12.657|30.992|
|**Sector**|**Fuente**|**Largo (m)**|119|728.935|5.940.102|-13.117|30.711|
|**Sector**|**Fuente**|**Largo (m)**|120|728.321|5.940.312|-13.737|30.903|
|**Sector**|**Fuente**|**Largo (m)**|121|727.489|5.939.993|-14.559|30.561|
|**Sector**|**Fuente**|**Largo (m)**|122|725.735|5.939.601|-16.301|30.120|
|**Sector**|**Fuente**|**Largo (m)**|123|724.566|5.939.473|-17.466|29.959|
|**Sector**|**Fuente**|**Largo (m)**|124|723.930|5.939.341|-18.097|29.809|
|**Sector**|**Fuente**|**Largo (m)**|125|723.751|5.939.225|-18.273|29.688|
|**Sector**|**Fuente**|**Largo (m)**|126|723.613|5.938.931|-18.402|29.390|
|**Sector**|**Fuente**|**Largo (m)**|127|723.409|5.938.782|-18.602|29.236|
|**Sector**|**Fuente**|**Largo (m)**|128|722.829|5.938.495|-19.174|28.933|
|**Sector**|**Fuente**|**Largo (m)**|129|722.191|5.937.984|-19.797|28.404|
|**Sector**|**Fuente**|**Largo (m)**|130|720.060|5.936.935|-21.897|27.295|
|**Sector**|**Fuente**|**Largo (m)**|131|718.936|5.936.377|-23.005|26.706|
|**Sector**|**Fuente**|**Largo (m)**|132|717.238|5.935.849|-24.686|26.130|
|**Sector**|**Fuente**|**Largo (m)**|133|715.135|5.936.237|-26.799|26.458|
|**Sector**|**Fuente**|**Largo (m)**|134|714.220|5.936.328|-27.717|26.524|
|**Sector**|**Fuente**|**Largo (m)**|135|713.965|5.936.261|-27.969|26.449|
|**Sector**|**Fuente**|**Largo (m)**|136|713.472|5.936.289|-28.463|26.464|
|**Sector**|**Fuente**|**Largo (m)**|137|713.084|5.936.135|-28.846|26.299|
|**Sector**|**Fuente**|**Largo (m)**|138|712.672|5.936.238|-29.261|26.390|
|**Sector**|**Fuente**|**Largo (m)**|139|712.098|5.935.974|-29.827|26.109|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 133

|Sector|Fuente|Largo (m)|Punto|UTM (WGS 84 - Z18)|Col6|LCC (km)|Col8|
|---|---|---|---|---|---|---|---|
|**Sector**|**Fuente**|**Largo (m)**|**Punto**|**Este (m)**|**Norte (m)**|**LCC-X**|**LCC-Y**|
|**Sector**|**Fuente**|**Largo (m)**|140|711.929|5.936.018|-29.997|26.149|
|**Sector**|**Fuente**|**Largo (m)**|141|711.736|5.936.049|-30.191|26.174|
|**Sector**|**Fuente**|**Largo (m)**|142|711.411|5.936.085|-30.517|26.201|
|**Sector**|**Fuente**|**Largo (m)**|143|711.070|5.936.021|-30.856|26.127|
|**Sector**|**Fuente**|**Largo (m)**|144|709.999|5.935.580|-31.914|25.657|
|**Sector**|**Fuente**|**Largo (m)**|145|709.632|5.935.487|-32.278|25.554|
|**Sector**|**Fuente**|**Largo (m)**|146|708.982|5.935.501|-32.928|25.549|
|**Sector**|**Fuente**|**Largo (m)**|147|708.653|5.935.451|-33.256|25.490|
|**Sector**|**Fuente**|**Largo (m)**|148|708.211|5.935.343|-33.694|25.369|
|**Sector**|**Fuente**|**Largo (m)**|149|707.957|5.935.209|-33.944|25.228|
|**Sector**|**Fuente**|**Largo (m)**|150|707.656|5.935.088|-34.242|25.099|
|**Sector**|**Fuente**|**Largo (m)**|151|707.281|5.935.105|-34.617|25.105|
|**Sector**|**Fuente**|**Largo (m)**|152|706.656|5.935.434|-35.251|25.416|
|**Sector**|**Fuente**|**Largo (m)**|153|705.988|5.935.596|-35.923|25.560|
|**Sector**|**Fuente**|**Largo (m)**|154|705.456|5.935.580|-36.455|25.528|
|**Sector**|**Fuente**|**Largo (m)**|155|704.856|5.935.519|-37.052|25.450|
|**Sector**|**Fuente**|**Largo (m)**|156|703.778|5.934.982|-38.114|24.883|
|**Sector**|**Fuente**|**Largo (m)**|157|702.892|5.934.109|-38.975|23.986|
|**Sector**|**Fuente**|**Largo (m)**|158|701.966|5.933.500|-39.884|23.351|
|**Sector**|**Fuente**|**Largo (m)**|159|700.848|5.933.011|-40.988|22.830|
|**Sector**|**Fuente**|**Largo (m)**|160|700.493|5.932.868|-41.338|22.677|
|**Sector**|**Fuente**|**Largo (m)**|161|700.196|5.932.642|-41.629|22.443|
|**Sector**|**Fuente**|**Largo (m)**|162|698.223|5.932.137|-43.586|21.882|

El detalle de la distribución de las fuentes de área y caminos del escenario de modelación del Proyecto se

ilustran en **Figura** 25 a **Figura** 30 **,** con acercamientos a distintas obras del proyecto. En estas figuras se

muestran las fuentes consideradas en Google Earth y las fuentes implementadas en el modelo CALPUFF

en coordenadas Lambert Conformal Conic (LCC), respectivamente.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 134

_Fuente: Elaboración Propia._

**Figura 25.** Distribución de fuentes emisoras (caminos) del escenario del primer año de Construcción del Proyecto Parque Eólico Dañicalqui.

.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 135

**Figura 26.** Distribución de fuentes emisoras del escenario del primer año de Construcción del Proyecto

Parque Eólico Dañicalqui. Fuentes implementadas en CALPUFF, en coordenadas LCC.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 136

_Fuente: Elaboración Propia._

**Figura 27.** Distribución de fuentes emisoras del escenario del primer año de Construcción del Proyecto

Parque Eólico Dañicalqui, Acercamiento al Proyecto.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 137

**Figura 28.** Distribución de fuentes emisoras del escenario del primer año de Construcción del Proyecto

Parque Eólico Dañicalqui, Acercamiento al Proyecto. Fuentes implementadas en CALPUFF, en

coordenadas LCC.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 138

**Figura 29.** Ejemplo de distribución de fuentes emisoras del escenario del primer año de Construcción

del Proyecto Parque Eólico Dañicalqui, Acercamiento al Proyecto. Fuentes en Google Earth.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 139

**Figura 30.** Ejemplo de distribución de fuentes emisoras del escenario del primer año de Construcción

del Proyecto Parque Eólico Dañicalqui, Acercamiento al Proyecto. Fuentes implementadas en

CALPUFF, en coordenadas LCC.

**G.3.** **Resultados de la Aplicación del Sistema CALPUFF**

En esta sección se presentan los resultados del sistema de modelación CALPUFF, considerando el año

meteorológico 2021 y el escenario de emisión del primer año de la fase de construcción del Proyecto

Parque Eólico Dañicalqui. Es importante volver a mencionar que los resultados presentados a

continuación consideran el peor escenario de emisiones.

Los resultados obtenidos se presentan para cada contaminante estimando la estadística considerada en

el marco jurídico vigente en Chile presentando en la sección de línea base de calidad de aire para los

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 140

receptores presentados en **Tabla 78** y como isolíneas de concentraciones de contaminantes en el dominio

de modelación.

A continuación, se presentan los resultados en la calidad del aire de la zona de estudio para cada uno de

los contaminantes considerados.

**G.3.1** **Resultados de Material Particulado Respirable (MP10)**

Los resultados de MP10 promedio anual y percentil 98 de las concentraciones de 24 horas modelados con

CALPUFF para el escenario de construcción del Proyecto, se presentan en **Tabla 83** para los receptores de

interés. Como se observa en esta tabla, el mayor aporte del proyecto es en los receptores 45 y 5 con 7,5

y 48,6 μg/Nm [3], como promedio anual y percentil 98 de las concentraciones 24 horas, respectivamente.

Esto alcanza a 15 y 37% de la norma anual y diaria correspondiente, respectivamente.

Estos resultados se muestran también como isolíneas de concentraciones promedio anual y percentil 98

de las concentraciones de 24 horas de MP10 en **Figura 31** y **Figura 32**, respectivamente.

**Tabla 83.** Resultados de MP10 promedio anual y percentil 98 de las concentraciones diarias modeladas

por el sistema CALPUFF.

|Receptor|Concentración de MP10 (μg/Nm3)|Col3|
|---|---|---|
|**Receptor**|**Promedio anual**|**Percentil 98 de las concentraciones 24**<br>**horas**|
|**R1**|7,0|37,0|
|**R2**|5,6|29,6|
|**R3**|7,1|36,8|
|**R4**|4,9|22,9|
|**R5**|7,1|48,6|
|**R6**|3,2|21,4|
|**R7**|3,6|17,7|
|**R8**|3,6|21,3|
|**R9**|4,4|29,7|
|**R10**|3,3|20,9|
|**R11**|3,0|17,8|
|**R12**|3,3|19,5|
|**R13**|1,8|10,4|
|**R14**|3,1|15,6|
|**R15**|3,2|17,7|
|**R16**|1,9|10,1|
|**R17**|2,6|13,8|
|**R18**|4,0|23,4|
|**R19**|3,8|23,4|
|**R20**|0,1|0,7|
|**R21**|0,1|0,6|
|**R22**|0,1|0,6|
|**R23**|0,2|1,5|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 141

|Receptor|Concentración de MP10 (μg/Nm3)|Col3|
|---|---|---|
|**Receptor**|**Promedio anual**|**Percentil 98 de las concentraciones 24**<br>**horas**|
|**R24**|0,2|1,6|
|**R25**|0,2|1,4|
|**R26**|0,2|1,6|
|**R27**|0,2|1,7|
|**R28**|0,3|1,8|
|**R29**|0,3|1,9|
|**R30**|0,2|1,7|
|**R31**|0,3|2,0|
|**R32**|0,4|2,2|
|**R33**|0,4|2,5|
|**R34**|0,4|2,6|
|**R35**|0,4|2,5|
|**R36**|0,5|2,6|
|**R37**|0,5|2,7|
|**R38**|0,8|4,7|
|**R39**|0,8|5,5|
|**R40**|0,9|5,8|
|**R41**|1,1|6,5|
|**R42**|1,2|6,8|
|**R43**|5,2|20,3|
|**R44**|1,3|7,8|
|**R45**|7,5|30,5|
|**R46**|1,9|10,5|
|**R47**|1,7|12,0|
|**R48**|2,1|15,4|
|**R49**|0,2|1,3|
|**R50**|3,9|22,8|
|**R51**|2,2|16,5|
|**R52**|2,4|17,7|
|**R53**|0,2|1,7|
|**R54**|0,2|1,7|
|**R55**|0,2|1,7|
|**R56**|0,2|2,0|
|**R57**|0,2|2,0|
|**R58**|0,1|1,2|
|**R59**|0,2|1,9|
|**R60**|0,2|1,9|
|**R61**|0,2|1,9|
|**R62**|0,4|3,7|
|**R63**|0,2|2,1|
|**R64**|0,4|3,2|
|**R65**|0,4|3,4|
|**R66**|0,2|1,9|
|**R67**|0,4|3,5|
|**R68**|0,4|3,6|
|**R69**|0,2|1,9|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 142

|Receptor|Concentración de MP10 (μg/Nm3)|Col3|
|---|---|---|
|**Receptor**|**Promedio anual**|**Percentil 98 de las concentraciones 24**<br>**horas**|
|**R70**|0,2|1,9|
|**R71**|0,2|1,6|
|**R72**|3,1|17,0|
|**R73**|2,3|16,8|
|**R74**|0,0|0,0|
|**R75**|0,0|0,0|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 143

**Figura 31.** Isolíneas de concentraciones promedio anual de MP10 en la zona de estudio. Escenario meteorología año 2021 y escenario de

emisiones del primer año de construcción.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 144

**Figura 32.** Isolíneas de percentiles 98 de concentraciones de 24 horas de MP10 primario en la zona de estudio. Escenario meteorología año

2021 y escenario de emisiones del primer año de construcción.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 145

**G.3.2.** **Resultados de Material Particulado Fino Respirable (MP2,5)**

Los resultados de MP2,5 promedio anual y percentil 98 de las concentraciones de 24 horas modelados

con CALPUFF del primer año del Proyecto, se presentan en **Tabla 84** para los receptores de interés. Como

se observa en esta tabla, el mayor aporte del proyecto es en los receptores 45 y 5 con 1,0 y 5,0 μg/Nm [3],

como promedio anual y percentil 98 de las concentraciones 24 horas, respectivamente. Esto alcanza a 5

y 10% de la norma anual y diaria correspondiente, respectivamente.

Estos resultados se muestran también como isolíneas de concentración promedio anual y percentil 98 de

las concentraciones de 24 horas de MP2,5 en **Figura 33** y **Figura 34**, respectivamente.

**Tabla 84.** Resultados de MP2,5 promedio anual y percentil 98 de las concentraciones diarias modeladas

por el sistema CALPUFF.

|Receptor|Concentración de MP2,5 (μg/Nm3)|Col3|
|---|---|---|
|**Receptor**|**Promedio anual**|**Percentil 98 de las concentraciones 24**<br>**horas**|
|**R1**|0,8|4,2|
|**R2**|0,6|3,5|
|**R3**|0,8|4,1|
|**R4**|0,6|2,7|
|**R5**|0,8|5,0|
|**R6**|0,4|2,2|
|**R7**|0,4|1,8|
|**R8**|0,4|2,2|
|**R9**|0,5|3,2|
|**R10**|0,4|2,2|
|**R11**|0,3|1,9|
|**R12**|0,4|2,1|
|**R13**|0,2|1,1|
|**R14**|0,4|1,7|
|**R15**|0,4|1,9|
|**R16**|0,2|1,2|
|**R17**|0,3|1,5|
|**R18**|0,4|2,5|
|**R19**|0,4|2,5|
|**R20**|0,0|0,2|
|**R21**|0,0|0,2|
|**R22**|0,0|0,2|
|**R23**|0,1|0,3|
|**R24**|0,1|0,3|
|**R25**|0,1|0,3|
|**R26**|0,1|0,4|
|**R27**|0,1|0,4|
|**R28**|0,1|0,4|
|**R29**|0,1|0,4|
|**R30**|0,1|0,4|
|**R31**|0,1|0,5|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 146

|Receptor|Concentración de MP2,5 (μg/Nm3)|Col3|
|---|---|---|
|**Receptor**|**Promedio anual**|**Percentil 98 de las concentraciones 24**<br>**horas**|
|**R32**|0,1|0,4|
|**R33**|0,1|0,6|
|**R34**|0,1|0,6|
|**R35**|0,1|0,6|
|**R36**|0,1|0,6|
|**R37**|0,1|0,6|
|**R38**|0,1|0,7|
|**R39**|0,1|0,7|
|**R40**|0,1|0,8|
|**R41**|0,2|1,0|
|**R42**|0,2|1,2|
|**R43**|0,7|3,1|
|**R44**|0,2|1,1|
|**R45**|1,0|3,7|
|**R46**|0,3|1,8|
|**R47**|0,2|1,4|
|**R48**|0,3|2,2|
|**R49**|0,0|0,2|
|**R50**|0,5|3,6|
|**R51**|0,3|2,0|
|**R52**|0,3|2,7|
|**R53**|0,0|0,3|
|**R54**|0,0|0,3|
|**R55**|0,0|0,3|
|**R56**|0,0|0,3|
|**R57**|0,0|0,4|
|**R58**|0,0|0,2|
|**R59**|0,0|0,3|
|**R60**|0,0|0,4|
|**R61**|0,0|0,4|
|**R62**|0,1|0,6|
|**R63**|0,0|0,4|
|**R64**|0,1|0,5|
|**R65**|0,1|0,5|
|**R66**|0,0|0,3|
|**R67**|0,1|0,5|
|**R68**|0,1|0,6|
|**R69**|0,0|0,3|
|**R70**|0,0|0,3|
|**R71**|0,0|0,2|
|**R72**|0,5|2,8|
|**R73**|0,3|2,3|
|**R74**|0,0|0,0|
|**R75**|0,0|0,0|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 147

**Figura 33.** Isolíneas de concentraciones promedio anual de MP2,5 en la zona de estudio. Escenario meteorología año 2021 y escenario de

emisiones del primer año de construcción.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 148

**Figura 34.** Isolíneas de percentiles 98 de concentraciones de 24 horas de MP2,5 en la zona de estudio. Escenario meteorología año 2021 y

escenario de emisiones del primer año de construcción.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 149

**G.3.3.** **Resultados de Material Particulado Sedimentable (MPS)**

Los resultados de MPS promedio anual y promedio máximo mensual modelados con CALPUFF del primer

año del Proyecto, se presentan en **Tabla 85** para los receptores de interés. Como se observa en esta tabla,

el mayor aporte del proyecto es en el receptor 5 con 64,9 mg/m [2] -día, lo alcanza a 65% la norma de MPS

tomada como referencia.

Estos resultados se muestran también como isolíneas de concentración promedio anual en **Figura 35** .

**Tabla 85.** Resultados de MPS promedio anual y máximo mensual modeladas por el sistema CALPUFF.

|Receptor|Concentración de MPS (mg/m2-día)|
|---|---|
|**Receptor**|**Promedio anual**|
|**R1**|56,4|
|**R2**|39,5|
|**R3**|57,4|
|**R4**|35,4|
|**R5**|64,9|
|**R6**|24,8|
|**R7**|35,5|
|**R8**|25,0|
|**R9**|36,6|
|**R10**|26,6|
|**R11**|23,6|
|**R12**|22,2|
|**R13**|10,0|
|**R14**|31,0|
|**R15**|21,1|
|**R16**|19,1|
|**R17**|16,6|
|**R18**|32,2|
|**R19**|27,0|
|**R20**|0,0|
|**R21**|0,0|
|**R22**|0,0|
|**R23**|0,1|
|**R24**|0,1|
|**R25**|0,1|
|**R26**|0,1|
|**R27**|0,1|
|**R28**|0,2|
|**R29**|0,2|
|**R30**|0,1|
|**R31**|0,2|
|**R32**|0,2|
|**R33**|0,2|
|**R34**|0,2|
|**R35**|0,2|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 150

|Receptor|Concentración de MPS (mg/m2-día)|
|---|---|
|**Receptor**|**Promedio anual**|
|**R36**|0,2|
|**R37**|0,2|
|**R38**|0,4|
|**R39**|0,4|
|**R40**|0,6|
|**R41**|0,8|
|**R42**|1,0|
|**R43**|32,5|
|**R44**|1,7|
|**R45**|51,0|
|**R46**|5,9|
|**R47**|3,8|
|**R48**|4,8|
|**R49**|0,1|
|**R50**|25,2|
|**R51**|10,8|
|**R52**|8,8|
|**R53**|0,1|
|**R54**|0,1|
|**R55**|0,1|
|**R56**|0,1|
|**R57**|0,1|
|**R58**|0,0|
|**R59**|0,1|
|**R60**|0,1|
|**R61**|0,1|
|**R62**|0,3|
|**R63**|0,1|
|**R64**|0,2|
|**R65**|0,2|
|**R66**|0,1|
|**R67**|0,3|
|**R68**|0,3|
|**R69**|0,1|
|**R70**|0,1|
|**R71**|0,1|
|**R72**|18,4|
|**R73**|11,3|
|**R74**|0,0|
|**R75**|0,0|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 151

**Figura 35.** Isolíneas de concentraciones promedio anual de MPS en la zona de estudio. Escenario meteorología año 2021 y escenario de

emisiones del primer año de construcción.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 152

**G.3.4.** **Resultados de Dióxido de Nitrógeno (NO** **2** **)**

Los resultados de NO 2, promedio anual y percentil 99 de las máximas diarias concentraciones horarias, en

los receptores de interés modelados con CALPUFF para el escenario del primer año de construcción del

Proyecto se presentan en **Tabla 86** . Como se observa en esta tabla, el mayor aporte del proyecto es en el

receptor 37 con 75,4 μg/Nm [3] como concentración de 1 hora, lo que alcanza a 19% de la norma horaria

correspondiente.

Estos resultados se presentan también como isolíneas de concentración promedio anual y Percentil 99 de

las concentraciones horarias de NO 2 en **Figura 36** y **Figura 37**, respectivamente.

**Tabla 86.** Resultados de NO 2 promedio anual y percentil 99 de las máximas diarias concentraciones

horarias modeladas por el sistema CALPUFF.

|Receptor|Concentración de NO (μg/Nm3)<br>2|Col3|
|---|---|---|
|**Receptor**|**Promedio anual**|**Percentil 99 de las concentraciones 1**<br>**hora**|
|**R1**|0,2|9,3|
|**R2**|0,1|6,8|
|**R3**|0,2|10,2|
|**R4**|0,1|6,5|
|**R5**|0,1|2,6|
|**R6**|0,0|2,9|
|**R7**|0,0|3,2|
|**R8**|0,1|2,5|
|**R9**|0,1|3,0|
|**R10**|0,0|2,9|
|**R11**|0,0|3,0|
|**R12**|0,0|2,5|
|**R13**|0,0|2,7|
|**R14**|0,1|2,8|
|**R15**|0,1|2,5|
|**R16**|0,1|2,3|
|**R17**|0,0|2,2|
|**R18**|0,0|2,2|
|**R19**|0,1|2,5|
|**R20**|0,0|9,6|
|**R21**|0,0|11,8|
|**R22**|0,0|6,6|
|**R23**|0,2|22,6|
|**R24**|0,2|23,7|
|**R25**|0,2|19,8|
|**R26**|0,2|25,7|
|**R27**|0,2|24,1|
|**R28**|0,3|17,5|
|**R29**|0,3|27,3|
|**R30**|0,2|23,7|
|**R31**|0,3|25,6|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 153

|Receptor|Concentración de NO (μg/Nm3)<br>2|Col3|
|---|---|---|
|**Receptor**|**Promedio anual**|**Percentil 99 de las concentraciones 1**<br>**hora**|
|**R32**|0,4|47,7|
|**R33**|0,4|28,0|
|**R34**|0,5|49,1|
|**R35**|0,5|49,9|
|**R36**|0,5|71,5|
|**R37**|0,4|75,4|
|**R38**|0,1|8,9|
|**R39**|0,1|9,1|
|**R40**|0,1|9,1|
|**R41**|0,2|28,4|
|**R42**|0,4|60,4|
|**R43**|0,2|14,2|
|**R44**|0,1|12,4|
|**R45**|0,4|19,1|
|**R46**|0,3|33,1|
|**R47**|0,1|11,2|
|**R48**|0,1|14,0|
|**R49**|0,0|1,8|
|**R50**|0,2|28,9|
|**R51**|0,2|16,6|
|**R52**|0,2|29,0|
|**R53**|0,1|18,5|
|**R54**|0,1|21,1|
|**R55**|0,1|20,8|
|**R56**|0,1|20,2|
|**R57**|0,1|20,0|
|**R58**|0,1|11,4|
|**R59**|0,1|10,0|
|**R60**|0,1|9,3|
|**R61**|0,1|10,6|
|**R62**|0,0|4,7|
|**R63**|0,1|14,6|
|**R64**|0,0|3,4|
|**R65**|0,0|4,5|
|**R66**|0,1|11,8|
|**R67**|0,0|4,8|
|**R68**|0,0|5,1|
|**R69**|0,1|8,8|
|**R70**|0,1|9,6|
|**R71**|0,0|2,2|
|**R72**|0,4|40,0|
|**R73**|0,2|16,4|
|**R74**|0,0|0,1|
|**R75**|0,0|0,1|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 154

**Figura 36.** Isolíneas de concentraciones promedio anual de NO 2 en la zona de estudio. Escenario meteorología año 2021 y escenario de

emisiones del primer año de construcción.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 155

**Figura 37.** Isolíneas de percentiles 99 de concentraciones de 1 hora de NO 2 en la zona de estudio. Escenario meteorología año 2021 y

escenario de emisiones del primer año de construcción.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 156

**G.3.5.** **Resultados de Dióxido de Azufre (SO** **2** **)**

Los resultados de SO 2, percentil 98,5 de las concentraciones de 1 hora, percentiles 99 y 99,7 de las

concentraciones diarias y percentil 99,73 de las concentraciones de 1 hora de SO 2, en los receptores de

interés modelados con CALPUFF para el escenario construcción del Proyecto se presentan en **Tabla 87** y

**Tabla 88** para la norma primaria y secundaria de calidad de aire, respectivamente. En estas tablas se

observa que el aporte de SO 2 del proyecto en todos los receptores es bajo y no alcanza a 1% de la norma

primaria respectiva. Con respecto a la norma secundaria, el receptor con aporte más alto alcanza a 1% de

la norma horaria secundaria para la zona sur del país.

Los resultados de SO 2 modelados con CALPUFF también se presentan como isolíneas de promedio anual,

percentil 98,5 de las concentraciones de 1 hora, percentiles 99 y 99,7 de las concentraciones diarias y

percentil 99,73 de las concentraciones de 1 hora de SO 2 en **Figura 38** a **Figura 42**, respectivamente.

**Tabla 87.** Resultados de SO 2 promedio anual, percentil 99 de las concentraciones diarias y percentil

98,5 de las concentraciones horarias modeladas por el sistema CALPUFF.

|Receptor|Concentración de SO (μg/Nm3) - Estadística norma primaria<br>2|Col3|Col4|
|---|---|---|---|
|**Receptor**|**Promedio anual**|**Percentil 99 de las**<br>**concentraciones 24 horas**|**Percentil 98,5 de las**<br>**concentraciones de 1 hora**|
|**R1**|0,01|0,04|0,08|
|**R2**|0,01|0,04|0,07|
|**R3**|0,01|0,04|0,08|
|**R4**|0,01|0,05|0,08|
|**R5**|0,00|0,02|0,04|
|**R6**|0,00|0,02|0,03|
|**R7**|0,00|0,02|0,03|
|**R8**|0,00|0,02|0,03|
|**R9**|0,00|0,02|0,04|
|**R10**|0,00|0,02|0,03|
|**R11**|0,00|0,02|0,03|
|**R12**|0,00|0,01|0,03|
|**R13**|0,00|0,02|0,03|
|**R14**|0,00|0,01|0,03|
|**R15**|0,00|0,01|0,03|
|**R16**|0,00|0,01|0,03|
|**R17**|0,00|0,01|0,03|
|**R18**|0,00|0,01|0,03|
|**R19**|0,00|0,02|0,03|
|**R20**|0,00|0,02|0,02|
|**R21**|0,00|0,02|0,02|
|**R22**|0,00|0,02|0,02|
|**R23**|0,02|0,11|0,22|
|**R24**|0,01|0,10|0,22|
|**R25**|0,01|0,14|0,19|
|**R26**|0,01|0,13|0,22|
|**R27**|0,02|0,14|0,24|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 157

|Receptor|Concentración de SO (μg/Nm3) - Estadística norma primaria<br>2|Col3|Col4|
|---|---|---|---|
|**Receptor**|**Promedio anual**|**Percentil 99 de las**<br>**concentraciones 24 horas**|**Percentil 98,5 de las**<br>**concentraciones de 1 hora**|
|**R28**|0,02|0,20|0,29|
|**R29**|0,02|0,14|0,28|
|**R30**|0,02|0,19|0,25|
|**R31**|0,02|0,16|0,25|
|**R32**|0,02|0,17|0,19|
|**R33**|0,03|0,26|0,45|
|**R34**|0,02|0,23|0,25|
|**R35**|0,02|0,25|0,24|
|**R36**|0,02|0,29|0,24|
|**R37**|0,02|0,24|0,25|
|**R38**|0,01|0,07|0,06|
|**R39**|0,01|0,07|0,06|
|**R40**|0,01|0,07|0,07|
|**R41**|0,01|0,07|0,09|
|**R42**|0,01|0,11|0,16|
|**R43**|0,05|0,30|0,75|
|**R44**|0,01|0,07|0,09|
|**R45**|0,09|0,49|1,16|
|**R46**|0,01|0,11|0,15|
|**R47**|0,01|0,08|0,14|
|**R48**|0,02|0,16|0,22|
|**R49**|0,00|0,02|0,03|
|**R50**|0,03|0,45|0,23|
|**R51**|0,01|0,16|0,09|
|**R52**|0,02|0,51|0,24|
|**R53**|0,01|0,07|0,11|
|**R54**|0,01|0,08|0,11|
|**R55**|0,01|0,08|0,10|
|**R56**|0,01|0,07|0,09|
|**R57**|0,01|0,07|0,08|
|**R58**|0,00|0,06|0,05|
|**R59**|0,00|0,04|0,05|
|**R60**|0,00|0,06|0,05|
|**R61**|0,00|0,06|0,05|
|**R62**|0,00|0,03|0,03|
|**R63**|0,00|0,05|0,05|
|**R64**|0,00|0,02|0,03|
|**R65**|0,00|0,02|0,03|
|**R66**|0,00|0,05|0,04|
|**R67**|0,00|0,03|0,04|
|**R68**|0,00|0,03|0,04|
|**R69**|0,00|0,04|0,04|
|**R70**|0,00|0,04|0,04|
|**R71**|0,00|0,02|0,02|
|**R72**|0,01|0,11|0,18|
|**R73**|0,01|0,17|0,09|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 158

|Receptor|Concentración de SO (μg/Nm3) - Estadística norma primaria<br>2|Col3|Col4|
|---|---|---|---|
|**Receptor**|**Promedio anual**|**Percentil 99 de las**<br>**concentraciones 24 horas**|**Percentil 98,5 de las**<br>**concentraciones de 1 hora**|
|**R74**|0,00|0,00|0,00|
|**R75**|0,00|0,00|0,00|

**Tabla 88.** Resultados de SO 2 promedio anual, percentil 99,7 de las concentraciones diarias y percentil

99,73 de las concentraciones horarias modeladas por el sistema CALPUFF.

|Receptor|Concentración de SO (μg/Nm3) - Estadística norma secundaria<br>2|Col3|Col4|
|---|---|---|---|
|**Receptor**|**Promedio anual**|**Percentil 99,7 de las conc. 24**<br>**horas**|**Percentil 99,73 de las conc. 1**<br>**hora**|
|**R1**|0,01|0,06|0,23|
|**R2**|0,01|0,06|0,21|
|**R3**|0,01|0,06|0,23|
|**R4**|0,01|0,07|0,22|
|**R5**|0,00|0,03|0,11|
|**R6**|0,00|0,03|0,10|
|**R7**|0,00|0,04|0,10|
|**R8**|0,00|0,02|0,09|
|**R9**|0,00|0,03|0,11|
|**R10**|0,00|0,03|0,11|
|**R11**|0,00|0,03|0,11|
|**R12**|0,00|0,02|0,09|
|**R13**|0,00|0,02|0,10|
|**R14**|0,00|0,02|0,07|
|**R15**|0,00|0,02|0,09|
|**R16**|0,00|0,02|0,07|
|**R17**|0,00|0,02|0,08|
|**R18**|0,00|0,02|0,08|
|**R19**|0,00|0,02|0,10|
|**R20**|0,00|0,03|0,11|
|**R21**|0,00|0,03|0,12|
|**R22**|0,00|0,03|0,12|
|**R23**|0,02|0,13|0,54|
|**R24**|0,01|0,16|0,54|
|**R25**|0,01|0,41|0,57|
|**R26**|0,01|0,20|0,55|
|**R27**|0,02|0,22|0,55|
|**R28**|0,02|0,26|0,77|
|**R29**|0,02|0,18|0,79|
|**R30**|0,02|0,38|0,63|
|**R31**|0,02|0,30|0,67|
|**R32**|0,02|0,19|1,02|
|**R33**|0,03|0,43|1,37|
|**R34**|0,02|0,33|1,37|
|**R35**|0,02|0,32|1,13|
|**R36**|0,02|0,34|1,16|
|**R37**|0,02|0,36|1,13|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 159

|Receptor|Concentración de SO (μg/Nm3) - Estadística norma secundaria<br>2|Col3|Col4|
|---|---|---|---|
|**Receptor**|**Promedio anual**|**Percentil 99,7 de las conc. 24**<br>**horas**|**Percentil 99,73 de las conc. 1**<br>**hora**|
|**R38**|0,01|0,09|0,39|
|**R39**|0,01|0,09|0,38|
|**R40**|0,01|0,10|0,40|
|**R41**|0,01|0,10|0,41|
|**R42**|0,01|0,15|0,74|
|**R43**|0,05|0,78|1,73|
|**R44**|0,01|0,12|0,43|
|**R45**|0,09|0,80|2,57|
|**R46**|0,01|0,17|0,66|
|**R47**|0,01|0,11|0,50|
|**R48**|0,02|0,72|0,78|
|**R49**|0,00|0,02|0,11|
|**R50**|0,03|0,73|1,71|
|**R51**|0,01|0,28|0,82|
|**R52**|0,02|0,68|1,19|
|**R53**|0,01|0,13|0,38|
|**R54**|0,01|0,13|0,37|
|**R55**|0,01|0,11|0,37|
|**R56**|0,01|0,11|0,32|
|**R57**|0,01|0,09|0,32|
|**R58**|0,00|0,08|0,28|
|**R59**|0,00|0,08|0,21|
|**R60**|0,00|0,08|0,22|
|**R61**|0,00|0,09|0,22|
|**R62**|0,00|0,04|0,13|
|**R63**|0,00|0,09|0,19|
|**R64**|0,00|0,04|0,11|
|**R65**|0,00|0,04|0,12|
|**R66**|0,00|0,10|0,23|
|**R67**|0,00|0,04|0,14|
|**R68**|0,00|0,04|0,15|
|**R69**|0,00|0,08|0,21|
|**R70**|0,00|0,05|0,19|
|**R71**|0,00|0,03|0,08|
|**R72**|0,01|0,11|0,69|
|**R73**|0,01|0,29|0,83|
|**R74**|0,00|0,00|0,00|
|**R75**|0,00|0,00|0,00|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 160

**Figura 38.** Isolíneas de concentraciones promedio anual de SO 2 en la zona de estudio. Escenario meteorología año 2021 y escenario de

emisiones del primer año de construcción.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 161

**Figura 39.** Isolíneas de Percentil 99 de las concentraciones de 24 horas de SO 2 en la zona de estudio. Escenario meteorología año 2021 y

escenario de emisiones del primer año de construcción.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 162

**Figura 40.** Isolíneas de Percentil 98,5 de las concentraciones de 1 hora de SO 2 en la zona de estudio. Escenario meteorología año 2021 y

escenario de emisiones del primer año de construcción.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 163

**Figura 41.** Isolíneas de Percentil 99,7 de las concentraciones de 24 horas de SO 2 en la zona de estudio. Escenario meteorología año 2021 y

escenario de emisiones del primer año de construcción.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 164

**Figura 42.** Isolíneas de Percentil 99,73 de las concentraciones de 1 hora de SO 2 en la zona de estudio. Escenario meteorología año 2021 y

escenario de emisiones del primer año de construcción.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 165

**G.3.6.** **Resultados de Monóxido de Carbono (CO)**

Los resultados de CO, percentiles 99 de las máximas diarias concentraciones de 8 y 1 horas, en los

receptores de interés modelados con CALPUFF para el escenario construcción del Proyecto se presentan

en **Tabla 89** . En esta tabla se observa que el aporte del proyecto de CO en todos los receptores es bajo y

no alcanza a 1% de la norma respectiva.

Estos resultados se presentan también como isolíneas de Percentil 99 de los máximos diarios de las

concentraciones de 8 horas y de 1 hora de CO en **Figura 43** y **Figura 44**, respectivamente.

**Tabla 89.** Resultados de CO percentil 99 de las máximas diarias concentraciones de 8 y 1 horas

modeladas por el sistema CALPUFF.

|Receptor|Concentración de CO (μg/Nm3)|Col3|
|---|---|---|
|**Receptor**|**Percentil 99 de las conc. 8 horas**|**Percentil 99 de las conc. 1 hora**|
|**R1**|5,5|27,8|
|**R2**|3,9|20,0|
|**R3**|6,0|31,4|
|**R4**|4,0|15,3|
|**R5**|1,3|4,6|
|**R6**|1,0|3,1|
|**R7**|0,9|3,6|
|**R8**|1,0|3,3|
|**R9**|1,4|5,8|
|**R10**|1,0|3,3|
|**R11**|1,0|3,3|
|**R12**|0,9|3,0|
|**R13**|0,8|2,5|
|**R14**|1,3|5,6|
|**R15**|1,1|3,5|
|**R16**|1,0|3,8|
|**R17**|0,8|2,7|
|**R18**|0,9|3,0|
|**R19**|1,0|3,1|
|**R20**|0,4|1,5|
|**R21**|0,5|1,4|
|**R22**|0,5|1,6|
|**R23**|1,8|8,7|
|**R24**|1,7|8,6|
|**R25**|2,8|8,3|
|**R26**|1,9|9,8|
|**R27**|2,1|10,9|
|**R28**|3,0|12,0|
|**R29**|2,3|10,2|
|**R30**|3,3|9,9|
|**R31**|4,0|17,3|
|**R32**|3,0|12,2|
|**R33**|5,1|22,2|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 166

|Receptor|Concentración de CO (μg/Nm3)|Col3|
|---|---|---|
|**Receptor**|**Percentil 99 de las conc. 8 horas**|**Percentil 99 de las conc. 1 hora**|
|**R34**|4,6|17,6|
|**R35**|4,1|18,2|
|**R36**|4,3|24,0|
|**R37**|4,1|22,2|
|**R38**|2,9|10,7|
|**R39**|2,1|9,0|
|**R40**|2,3|9,6|
|**R41**|4,3|17,8|
|**R42**|5,4|21,8|
|**R43**|6,6|27,7|
|**R44**|3,9|14,5|
|**R45**|11,1|49,2|
|**R46**|9,4|39,9|
|**R47**|4,1|12,6|
|**R48**|7,4|25,9|
|**R49**|1,0|3,4|
|**R50**|15,8|72,7|
|**R51**|6,4|28,9|
|**R52**|13,3|86,8|
|**R53**|2,0|7,8|
|**R54**|2,0|9,1|
|**R55**|2,0|9,0|
|**R56**|2,3|10,4|
|**R57**|2,3|10,4|
|**R58**|1,6|4,6|
|**R59**|1,7|5,8|
|**R60**|1,7|6,4|
|**R61**|1,7|6,3|
|**R62**|3,2|12,1|
|**R63**|1,9|6,3|
|**R64**|2,6|8,4|
|**R65**|2,5|10,9|
|**R66**|1,6|5,4|
|**R67**|3,2|12,3|
|**R68**|3,0|14,5|
|**R69**|1,5|4,3|
|**R70**|1,4|4,6|
|**R71**|1,5|4,2|
|**R72**|13,3|78,1|
|**R73**|6,4|30,0|
|**R74**|0,1|0,1|
|**R75**|0,1|0,1|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 167

**Figura 43.** Isolíneas de Percentil 99 de los máximos diarios de las concentraciones de 8 horas de CO en la zona de estudio. Escenario

meteorología año 2021 y escenario de emisiones del primer año de construcción.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 168

**Figura 44.** Isolíneas de Percentil 99 de los máximos diarios de las concentraciones de 1 hora de CO en la zona de estudio. Escenario

meteorología año 2021 y escenario de emisiones del primer año de construcción.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 169

**G.3.7. Resumen de Aportes del Proyecto en las Estaciones Monitoras de Cercanas al Proyecto**

**Modelados con CALPUFF**

El resumen de los aportes de contaminantes atmosféricos que efectuará el presente proyecto en

evaluación se presenta en **Tabla 90**, para la fase de Construcción del proyecto. En esta tabla se presenta

también el porcentaje de la norma de calidad de aire respectiva que tiene casa aporte. Como se menciona

anteriormente, la fase de Operación tiene emisiones insignificantes frente a la fase de Construcción.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 170

**Tabla 90.** Resumen de los aportes de contaminantes atmosféricos que efectuará el Proyecto.

|Fase/Aporte<br>Contaminante<br>(μg/m3N)|MP10|Col3|MP2,5|Col5|NO<br>2|Col7|SO<br>2|Col9|Col10|CO|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Fase/Aporte**<br>**Contaminante**<br>**(μg/m3N)**|**Conc.**<br>**anual**|**Conc. 24**<br>**horas**|**Conc.**<br>**anual**|**Conc. 24**<br>**horas**|**Conc.**<br>**anual**|**Conc.**<br>**horaria**|**Conc.**<br>**anual**|**Conc. 24**<br>**horas**|**Conc.**<br>**horaria**|**Conc. 8**<br>**horas**|**Conc.**<br>**horaria**|
|**Estación SAPU**|**Estación SAPU**|**Estación SAPU**|**Estación SAPU**|**Estación SAPU**|**Estación SAPU**|**Estación SAPU**|**Estación SAPU**|**Estación SAPU**|**Estación SAPU**|**Estación SAPU**|**Estación SAPU**|
|Construcción|0,004|0,048|0,001|0,007|0,0008|0,075|0,0000|0,0009|0,0007|0,089|0,086|
|% de la norma|0,009|0,037|0,004|0,014|0,0008|0,019|0,0001|0,0006|0,0002|0,001|0,000|
|**Estación Quinel**|**Estación Quinel**|**Estación Quinel**|**Estación Quinel**|**Estación Quinel**|**Estación Quinel**|**Estación Quinel**|**Estación Quinel**|**Estación Quinel**|**Estación Quinel**|**Estación Quinel**|**Estación Quinel**|
|Construcción|0,004|0,046|0,001|0,007|0,0007|0,054|0,0001|0,0009|0,0006|0,084|0,073|
|% de la norma|0,008|0,035|0,004|0,014|0,0007|0,014|0,0001|0,0006|0,0002|0,001|0,000|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 171

**G.3.8.** **Determinación del Área de Influencia**

Como se presenta en la “Guía sobre el Área de Influencia en el Sistema de Evaluación de Impacto

Ambiental” del SEA (2017): En la letra a) del artículo 2 del Reglamento del SEIA se define área de

influencia (AI) como ‘El área o espacio geográfico, cuyos atributos, elementos naturales o

socioculturales deben ser considerados con la finalidad de definir si el proyecto o actividad genera

o presenta alguno de los efectos, características o circunstancias del artículo 11 de la Ley, o bien

para justificar la inexistencia de dichos efectos, características o circunstancias’.

Criterio 1: El AI corresponde al área o espacio geográfico de donde se obtiene la información

necesaria para predecir y evaluar los impactos en los elementos del medio ambiente. La predicción

y evaluación de impactos ambientales se debe realizar tanto en el caso que al SEIA se presente un

EIA como una DIA. Si bien el capítulo de predicción y evaluación de impactos no forma parte de los

contenidos mínimos de una DIA, es necesario realizar dicha predicción y evaluación para poder

identificar los impactos ambientales que el proyecto genera y estimarlos cuantitativa y

cualitativamente (predicción) y posteriormente evaluar su significancia (evaluación); lo anterior con

el fin de obtener los fundamentos necesarios para justificar la inexistencia de los ECC del artículo 11

de la Ley, conforme a lo establecido en el Título II del Reglamento del SEIA.

Criterio 2: Cuando el Reglamento del SEIA se refiere al AI como un espacio geográfico, se entiende

no sólo el espacio terrestre, sino que, dependiendo del elemento del medio ambiente receptor de

impacto, éste puede ser también un espacio aéreo y/o acuático.

En este contexto se obtuvo el área de Influencia en calidad del aire del Proyecto, la que se presenta

en **Figura 45** . Esta área considera lo siguiente:

 - Conservadoramente, toda la zona que cubre las isolíneas de concentraciones de MP2,5,

considerando la de 1 μg/Nm [3] como percentil 98 de las concentraciones 24 horas que es la

que cubre mayor superficie en comparación con el promedio anual. Se considera este

contaminante debido a que el aporte de él es el más relevante en relación a la salud de la

población.

 - También se incluyen las fuentes del Proyecto que no quedan dentro de la isolínea

considerada, como caminos no pavimentados y fundaciones de LT.

El área de influencia del Proyecto estimada corresponde a aproximadamente 3.678 ha. El área

correspondiente a la isolínea de MP2,5 considerada abarca aproximadamente 3.496 ha. Es

importante mencionar que esta área está toda incluida en el dominio de modelación considerado

en el sistema de modelación WRF/CALPUFF.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 172

**Figura 45.** Área de Influencia para Calidad de Aire.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 173

**G.3.9.** **Análisis del Aporte del Proyecto**

En esta sección se presenta el análisis del aporte del Proyecto Parque Eólico Dañicalqui a la calidad

del aire observada en las estaciones SAPU y Quinel.

Los impactos de MP10, NO 2 y SO 2 del Proyecto, considerando la meteorología del año 2021 en

conjunto con la línea base de calidad de aire presentada anteriormente, se presentan en **Tabla 91** y

**Tabla 92**, respectivamente. No se consideran MP2,5, MPS ni CO debido a que no se monitorean en

las estaciones de la zona de estudio. Como se observa en estas tablas, las normas de calidad de aire

primarias no se superan en las estaciones de interés incluyendo los aportes del Proyecto, a

excepción de la norma diaria de MP10 en Quinel durante el año 2021. Sin embargo, esta norma está

sobrepasada sin el aporte del proyecto, el que es casi despreciable en esta estación,

correspondiente a 0,0460 μg/m [3] N.

**Tabla 91.** Estimación del impacto del Proyecto Parque Eólico Dañicalqui a las concentraciones de

MP10, NO 2 y SO 2 observadas en la estación SAPU.

|Contaminante|Col2|Concentración basal<br>Actual (μg/m3N)|Aporte Total del<br>proyecto (μg/m3N)|Total|Normativa<br>vigente|Porcentaje de<br>la norma|
|---|---|---|---|---|---|---|
|MP10|Concentración anual|34,1|0,0043|34,1|50|**68**|
|MP10|Concentración 24 horas|110,7|0,0484|110,7|150|**74**|
|NO2|Concentración anual|10,4|0,0008|10,4|100|**10**|
|NO2|Concentración horaria|86,6|0,0754|86,7|400|**22**|
|SO2|Concentración anual|5,9|0,0000|5,9|60|**10**|
|SO2|Concentración 24 horas|12,5|0,0009|12,5|150|**8 **|
|SO2|Concentración horaria|13|0,0007|13,0|350|**4 **|

**Tabla 92.** Estimación del impacto del Parque Eólico Dañicalqui a las concentraciones de MP10 y

NO 2 observadas en la estación Quinel.

|Contaminante|Col2|Concentración basal<br>Actual (μg/m3N)|Aporte Total del<br>proyecto (μg/m3N)|Total|Normativa<br>vigente|Porcentaje de<br>la norma|
|---|---|---|---|---|---|---|
|MP10|Concentración anual|41,1|0,0042|41,1|50|**82**|
|MP10|Concentración 24 horas|211,5|0,0460|211,5|150|**141**|
|NO2|Concentración anual|14,4|0,0007|14,4|100|**14**|
|NO2|Concentración horaria|95,9|0,0544|96,0|400|**24**|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 174

**H.** **CONCLUSIONES**

En este Capítulo se presentan las conclusiones correspondientes al Informe Final del **Anexo 21.**

**Actualización Estimación y modelación de emisiones atmosférica** de la **Adenda** .

En este estudio se desarrolló la estimación de emisiones de contaminantes atmosféricos de la fase

de construcción y operación del Proyecto.

Por otra parte, la ejecución del estudio consideró la meteorología del año 2021 generada por el

modelo meteorológico de mesoescala WRF, de acuerdo a los requerimientos del SEA. La

meteorología generada por WRF fue validada a través de un análisis de incertidumbre considerando

la meteorología de la estación Purén.

Los aportes del proyecto a la calidad del aire de la zona de estudio, que consideró un área de 95 x

95 km [2], se obtuvieron mediante la ejecución del modelo CALPUFF considerando la meteorología del

año 2021 y las emisiones de la fase de construcción del primer año, por ser el peor escenario de

emisiones atmosféricas.

Los resultados finales de CALPUFF permiten concluir lo siguiente:

 - Durante la fase de construcción del Proyecto, las emisiones de MP10 alcanzan a

aproximadamente a 182 toneladas durante toda la fase. Con respecto al MP2,5, las

emisiones de este contaminante alcanzan aproximadamente a 32 toneladas. Por otra parte,

las emisiones de NOx durante toda la fase de construcción del proyecto alcanzarán a 120

toneladas.

 - Durante la fase de operación, las emisiones de MP10 alcanzan a aproximadamente 8

toneladas anuales y las emisiones de MP2,5 llegarán a aproximadamente 1 t/año. Con

respecto al NOx, las emisiones de este contaminante alcanzan a 1 toneladas anual durante

la operación.

 - Las más altas emisiones del Proyecto se producirían durante el primer año de la fase

construcción para todos los contaminantes considerados. La actividad que tiene mayor

emisión corresponde a la resuspensión por tránsito en caminos no pavimentados.

 - En el escenario Construcción, las concentraciones de MP10 en los receptores de interés en

el área de estudio alcanzan como máximo a 7,5 y 48,6 μg/Nm [3] como promedio anual y

percentil 98 de las concentraciones 24 horas (Receptores 45 y 5, respectivamente),

respectivamente, alcanzando como máximo un 37% de la norma.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 175

 - El aporte del Proyecto de MP2,5 más alto en los receptores considerados alcanza 1,0 y 5,0

μg/Nm [3] como promedio anual y percentil 98 de las concentraciones 24 horas (Receptores

45 y 5,), respectivamente, alcanzando como máximo menos de 10% de la norma primaria.

 - Con respecto al NO 2, éste alcanza como máximo en los receptores considerados a 75,4

μg/Nm [3] como percentil 99 de las concentraciones de 1 hora (R37), llegando solo a un 19%

de la norma primaria.

 - El aporte de SO 2 del Proyecto de la fase de Construcción en los receptores considerados en

la zona del Proyecto alcanza como máximo a menos de 1% de la norma primaria de este

contaminante. Con respecto a la norma secundaria, el receptor con aporte más alto alcanza

a 1% de la norma secundaria horaria para la zona sur del país.

 - Por otra parte, el Proyecto tendría un aporte máximo de CO en los receptores de

aproximadamente 16 y 92 μg/m [3] N como percentil 99 de las concentraciones de 8 y 1 hora,

respectivamente, llegando a mucho menos de 1% de la norma primaria.

 - En el caso del MPS, el mayor aporte del proyecto es en el receptor 5 con 64,9 mg/m [2] -día, lo

alcanza a 65% la norma de MPS tomada como referencia.

 - Los resultados de MP10 muestran que las máximas concentraciones serían en la zona de

caminos no pavimentados de acceso internos del Proyecto que unen a los aerogeneradores

cercanos a la Instalación de faenas, extendiéndose hacia la entrada del camino exterior

desde la ruta N-85. Estas concentraciones se presentan en forma concentrada en esta área

y se dispersan con bajos con bajos impactos en el resto del área de estudio.

 - En cuanto a los gases, las concentraciones también se concentran alrededor de los caminos

no pavimentados internos y externos del PE y se dispersan en bajas concentraciones a

medida que nos alejamos del Proyecto.

 - Los aportes del Proyecto en la calidad del aire por MP10 en las estaciones SAPU y Quinel

alcanzan a 0,004 μg/m [3] como promedio anual en ambas estaciones y a 0,048 y 0,046 μg/m [3]

como percentil 98 de las concentraciones 24 horas, respectivamente. Con respecto a los

aportes de MP2,5, alcanzan a 0,001 μg/m [3] como promedio anual y a 0,007 μg/m [3] como

percentil 98 de las concentraciones 24 horas, en ambas estaciones. Estos aportes son casi

despreciables en estas estaciones, alcanzado como máximo un 0,1% de las normas de estos

contaminantes.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 176

 - Las normas de calidad de aire primarias no se superan en las estaciones SAPU y Quinel

incluyendo los aportes del Proyecto, a excepción de la norma diaria de MP10 en Quinel

durante el año 2021. Sin embargo, esta norma está sobrepasada sin el aporte del proyecto,

el que es casi despreciable en esta estación, correspondiente a 0,0460 μg/m [3] N.

 - Estos resultados implican que los máximos aportes de contaminantes a la zona de estudio

tienen un bajo porcentaje de impacto en la calidad del aire y no representan un peligro para

la salud de las personas del área.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 177

**I.** **BIBLIOGRAFÍA**

 - SEA, (2012). Guía para el uso de modelos de calidad del aire en el SEIA.

 - BCN, (2022). https://www.bcn.cl/siit/nuestropais/region16

 - Norma de calidad del aire para MP10 (D.S. N° 59/1998 MINSEGPRES, modificado por D.S. N°

12/2022, MMA)

 - Norma primaria de calidad del aire para MP2,5 (D.S. N° 12/2011 Ministerio del Medio

Ambiente)

 - Norma primaria de calidad del aire para NO 2 (D.S. N° 114/2002 del Ministerio Secretaría

General de la Presidencia)

 - Norma primaria de calidad del aire para CO (D.S. N° 115/2002 MINSEGPRES)

 - Norma primaria de calidad del aire para SO 2 (D.S. N° 104/2018 del Ministerio de Medio

Ambiente)

 - Norma secundaria de calidad del aire para SO 2 (D.S. N° 22/2009 del MINSEGPRES)

 - Norma secundaria de calidad de aire (D. Exento N° 4/1992 del Ministerio de Agricultura)

 - PLADECO, 2018. Plan de desarrollo comuna 2014-2017 Informe final. Recuperado el 19 de

Agosto de 2022.

 - PLADECO, 2016. Informe preliminar, Plan de desarrollo Comunal 2011-2015. Recuperado el

19 de Agosto de 2022 desde

[http://www.munipemuco.cl/transparencia/arch_desc/muni_descarga_1317.pdf](http://www.munipemuco.cl/transparencia/arch_desc/muni_descarga_1317.pdf)

 - Servicio de Evaluación Ambiental (SEA), 2015. Recopilación y Sistematización de Factores

de Emisión al Aire.

 Umaña, B. (2015). Caracterización de la Provincia de Ñuble y una propuesta estratégica para

el desarrollo del territorio. _Concepción, Chile: Editorial Universidad del Bio-Bio_ .

 - Wilks, D. S. (2011). Statistical methods in the atmospheric sciences (Vol. 100). Academic

press.

 - De derivative work: Janitoalevic - Este archivo deriva de: Mapa loc Biobío.svg de B1mbo, CC

BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=50212397

 De derivative work: Janitoalevic - Este archivo deriva de: Provincia de Ñuble.svg de B1mbo,

CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=50211914

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 178

**J.** **APÉNDICE**

# Apéndice 1. Plan de Aplicación de Supresor de Polvo

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 179

**A.** **PRESENTACIÓN**

El proyecto Parque Eólico Dañicalqui (en adelante “El Proyecto” o “Parque Eólico”), ubicado en las
comunas de Yungay y Pemuco, Región de Ñuble y Provincia del Diguillin, contempla la

implementación de medidas para el control de emisiones de polvo en su fase de construcción, las

que incluyen: la limitación de velocidad de desplazamiento al interior del Proyecto, para minimizar

el desgaste de los caminos y minimizar la polución; la aplicación de un supresor de polvo tipo

biodegradable por riego superficial en los caminos internos y camino de acceso del Parque Eólico.

En general, las medidas anteriormente mencionadas permitirán estabilizar y/o controlar las de

emisiones de polvo, evitando la pérdida de partículas finas del suelo, y optimizando la vida útil de

los caminos internos del Parque Eólico, aminorando los efectos de la acción abrasiva del tránsito o

“tracción”.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 180

**B.** **OBJETIVO**

Entregar las directrices y asegurar la efectividad y mantención de caminos internos de Proyecto

Parque Eólico Dañicalqui.l

**C.** **RESPONSABLES**

Los responsables dentro del proyecto de asegurar que los procedimientos del presente Plan se lleven

a cabo de forma efectiva, se definen a continuación.

**C.1.** **Gerencia del Proyecto.**

## • Aprobar, apoyar y promover la aplicación del presente Plan y sus modificaciones. • Brindar los recursos necesarios para la implementación y adecuado manejo de las practicas

mencionadas en el presente Plan.

## • Velar por el cumplimiento íntegro de este Plan en terreno.

**C.2.** **Jefe de Faena o Supervisor en terreno**

## • Será el responsable de velar en todo momento por la seguridad del personal a su cargo

que realizará las actividades de mantención.

## • Implementación y supervisión de la correcta ejecución del trabajo de acuerdo con los pasos

y procedimientos establecidos y de las indicaciones de su mando directo.

## • Será el responsable de la aplicación del programa y de verificar y llevar los registros del

presente Plan (libros de registro y anotaciones, registros fotográficos, etc.).

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 181

**D.** **PLAN DE APLICACIÓN Y CUIDADO DE SUPRESOR DE POLVO**

**D.1.** **Restricción de la velocidad al interior de los caminos internos del Parque Eólico**

El Proyecto contará con un Reglamento de Conducción Vehicular Interna, en el cual se encontrarán

incorporadas, entre otras, variables de límites de restricción vehicular de:

 - Camiones sobredimensionados (partes y piezas de los aerogeneradores) tendrán una

velocidad de 30 km/h en cualquier tipo de ruta.

 - Vehículos no sobredimensionados (vehículos livianos, camiones de insumos, partes y piezas

de la línea de transmisión) en rutas pavimentadas tendrán una velocidad de 80 km/h y en

rutas no pavimentadas una velocidad de 40 km/h

**D.2.** **Aplicación de supresor de Polvo en caminos a utilizar del Parque Eólico**

Como medida de estabilización de los caminos de acceso principales, el Proyecto considera la

aplicación un supresor de polvo tipo biodegradable mediante riego superficial, por medio de camión

aljibe, y su posterior perfilamiento mediante uso de motoniveladora y rodillo compactador, de tal

manera de asegurar la correcta formación de la costra superficial.

Se estima la aplicación de una dosis de 3 kg/m [2 ] de producto, donde cada litro de solución podrá

disolver hasta 1,5 kg de supresor de polvo a granel.

En la **Tabla 40** y **Figura 46**, se presentan los caminos a los cuales les será aplicada la presente medida.

**Tabla 93.** **Distancias de caminos externos e internos con supresor de polvo en la** **fase** **de**

**construcción del proyecto Parque Eólico Dañicalqui.**

|Tipo Camino|Áreas con supresor Externo No Pavimentado|Distancia (m)|
|---|---|---|
|**Externo**|**Acceso PE**|**Acceso PE**|
|**Externo**|Área supresor 1|523|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 182

|Col1|Área supresor 4|254|
|---|---|---|
||Área supresor 5|245|
||Área supresor 6|649|
||Área supresor 7|272|
||Área supresor 8|260|
||Área supresor 9|232|
||**Sub-Total PE**|**2.435**|
||**Acceso LT**|**Acceso LT**|
||Área supresor 2|405|
||**Sub-Total LT**|**405**|
|**Total Externo**|**Total Externo**|**2.840**|
|**Interno**|**Áreas con supresor Interno No Pavimentado**|**Distancia (m)**|
|**Interno**|Área supresor 3|276|
|**Interno**|Área supresor 4|113|
|**Total Interno**|**Total Interno**|**389**|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 183

**Figura 46.** Caminos del Proyecto a los cuales le será aplicada la medida de Supresión de Polvo.

**D.3.** **Inspecciones preventivas y mantenciones correctivas**

Para asegurar la correcta implementación de las medidas asociadas al Plan aplicación y cuidado de

supresor de polvo, se implementarán inspecciones preventivas y mantenciones correctivas, las

cuales se detallan a continuación.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 184

D.3.1. Inspecciones preventivas.

Como parte del Plan de aplicación y cuidado de supresor de polvo, se considera la realización de

inspecciones visuales preventivas a todos los caminos del Proyecto a los cuales le será aplicado el

supresor de polvo. En la **Figura 1** se presentan las rutas y caminos de acceso que se encontrarán

dentro de las inspecciones preventivas programadas.

Esta inspección visual preventiva tendrá por objetivo verificar el estado de los caminos. Para el caso

específico de aquellos caminos a los que se les haya aplicado supresor de polvo, se comprobará que

la carpeta de rodado se encuentre en óptimas condiciones sobre el camino y no presente daños en su

cobertura. Para el caso específico de las vías externas se verificará el estado de la carpeta de rodado

para detectar posibles deterioros.

Con el fin de mantener un control del monitoreo visual del estado de los caminos, cada una de estas

inspecciones quedará registrada a través de actas en donde se indicará la fecha de realización,

localización o tramo de los caminos inspeccionados y estados de estos. Además, y como respaldo, se

incluirá un registro fotográfico fechado y georreferenciado (WGS 84 UTM 18S) de los puntos de

monitoreo efectuados.

D.3.2. Mantenciones correctivas

Dadas las condiciones climáticas de la zona de localización del Proyecto, y al constante tránsito

vehicular proyectado para la fase de construcción del Proyecto, la capa de supresor de polvo aplicada

en los caminos principales podría deteriorarse. Por estos efectos, se ha estimado la implementación

de mantenciones correctivas, que corresponden a las rehabilitaciones o reacondicionamientos en

aquellos lugares puntuales de las zonas o tramos de los caminos que se requiera, es decir, en donde

la capa de supresor de polvo se haya deteriorado por el tránsito vehicular y contemplan su “re
aplicación”, cuando corresponda.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 185

Dentro de estas actividades se destacan principalmente:

a) Los bacheos o perfilados puntuales, para baches aislados que consiste básicamente en

extraer el material necesario, rellenar con material granular mezclado con la sal y compactar.

b) Riegos superficiales con supresor de polvo para restituir el material superficial perdido, para

caminos con buena regularidad superficial, o;

c) Escarificado y reposición de material granular y compactado, para caminos desgastados.

Cada una de estas actividades se realizará según la necesidad de la zona o tramo del camino.

Para cada una de las mantenciones realizadas, se elaborará un acta como registro de las medidas

ejecutadas para el reacondicionamiento del camino y la capa de supresor de polvo.

D.3.3. Equipamiento

Para la mantención del supresor de polvo se utilizará el siguiente equipamiento:

## • Camión Aljibe. • Motoniveladora. • Rodillo compactador.

Cabe señalar que los operadores, así como también personal que se encuentre realizando el

monitoreo o seguimiento, deberán contar con equipos de protección personal adecuados, los cuales

serán designados y evaluados por el respectivo Prevencionista de Riesgo presente en terreno.

**E.** **Frecuencia**

**E.1.** **Frecuencia de aplicación**

La periodicidad de ejecución de las medidas se presenta en la siguiente tabla.

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 186

**Tabla 94.** Periodicidad de ejecución

|Tipo de actividad|Fase de construcción, frecuencia3|
|---|---|
|Aplicación de Supresor de<br>Polvo caminos|Dos días, tres veces al año|

**E.2.** **Frecuencia de mantención**

Por otro lado, en la siguiente Tabla, se presenta la frecuencia de mantención de las medidas del Plan

de Mantención de Caminos.

**Tabla 95.** Frecuencia de mantención

|Tipo de actividad|Fase de construcción, frecuencia|
|---|---|
|Inspección Preventiva|Mensual|
|Mantención correctiva|Anual|

Sin perjuicio de lo anterior, se aplicarán estas medidas con anterioridad a la frecuencia antes

mencionada, en caso de que se detecte deterioro del producto en algún camino, durante una

inspección preventiva, que requiera de la aplicación de las medidas mencionadas previamente, tales

como ahuellamientos o calaminas debido al constante tránsito de vehículos.

Cada una de las mantenciones será programada y notificada al personal previamente, con el fin de

impedir las interferencias con las actividades de construcción del Proyecto, instalando la señalética

de advertencia correspondiente en el camino y asegurando que no se realice el tránsito vehicular

en dicha zona hasta que este se encuentre nuevamente operativo y en óptimas condiciones.

3 Estas medidas no serán aplicadas en meses de invierno

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 187

**F.** **VERIFICACIÓN**

Las medidas de verificación que se emplearan para garantizar el cumplimiento del presente este Plan

de Mantención son las siguientes:

## • Registro de la Aplicación de Supresor de Polvo en caminos principales (Anexo 1). • Registro de las Inspecciones Preventivas (Anexo 2). • Registro de las Mantenciones, acompañado de registro visual (Anexo 3).

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 188

**G.** **ANEXOS**

**ANEXO 1. REGISTRO DE APLICACIÓN DE SUPRESOR DE POLVO**

|Col1|REGISTRO DE APLICACIÓN DE SUPRESOR DE<br>POLVO CAMINOS PRINCIPALES|Col3|Código:<br>Revisión:<br>Fecha de rev: dd/mm/aaaa|
|---|---|---|---|
|**Encargado**<br>**de**<br>**la**<br>**inspección**||||
|**Fecha**||||
|**Tipo de evidencia**||||
|**Localización o tramo**||||
|**Cantidad aplicada** <br>**(m3)**||||
|**Proveedor**||||
|**REGISTRO FOTOGRÁFICO**|**REGISTRO FOTOGRÁFICO**|**REGISTRO FOTOGRÁFICO**|**REGISTRO FOTOGRÁFICO**|
|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|||
|OBSERVACIONES:<br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|OBSERVACIONES:<br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|OBSERVACIONES:<br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|OBSERVACIONES:<br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 189

**ANEXO 2. REGISTRO INSPECCIONES PREVENTIVAS**

|Col1|REGISTRO DE INSPECCIÓN PREVENTIVA|Col3|Código:<br>Revisión:<br>Fecha de rev: dd/mm/aaaa|
|---|---|---|---|
|**Encargado**<br>**de**<br>**la**<br>**inspección**||||
|**Fecha**||||
|**Tipo de evidencia**||||
|**Localización o tramo**||||
|**REGISTRO FOTOGRÁFICO**|**REGISTRO FOTOGRÁFICO**|**REGISTRO FOTOGRÁFICO**|**REGISTRO FOTOGRÁFICO**|
|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|||
|OBSERVACIONES:<br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|OBSERVACIONES:<br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|OBSERVACIONES:<br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|OBSERVACIONES:<br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 190

**ANEXO 3: REGISTRO MANTENCIÓN**

|Col1|REGISTRO DE MANTENCIÓN DE CAMINOS|Col3|Código:<br>Revisión:<br>Fecha de rev: dd/mm/aaaa|
|---|---|---|---|
|**Encargado**<br>**de**<br>**la**<br>**mantención**||||
|**Fecha**||||
|**Tipo de evidencia**||||
|**Localización o tramo**||||
|**REGISTRO FOTOGRÁFICO**|**REGISTRO FOTOGRÁFICO**|**REGISTRO FOTOGRÁFICO**|**REGISTRO FOTOGRÁFICO**|
|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|||
|OBSERVACIONES:<br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|OBSERVACIONES:<br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|OBSERVACIONES:<br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|OBSERVACIONES:<br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|

_ADENDA DIA PROYECTO PARQUE EÓLICO DAÑICALQUI_ 191

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: ** Estaciones meteorológicas en el dominio de la zona de Estudio.**

| Estación | Latitud<br>(°) | Longitud<br>(°) | Variable medidas (%) | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Estación** | **Latitud**<br>**(°)** | **Longitud**<br>**(°)** | **VV** | **DV** | **HR** | **T ** |
| Purén | -36.616 | -72.093 | 100 | 100 | 100 | 100 |

**Tabla 2.: ** Normas Primarias y Secundarias de calidad de aire de Chile para contaminantes atmosféricos.**

| Contaminante | Periodo de Evaluación | Valor Norma | Norma |
| --- | --- | --- | --- |
| Material Particulado<br>Respirable<br>(MP10) | Concentración de 24 horas | 130 (μg/Nm3) | Norma Primaria<br>D.S. No 12/2022 del<br>MINISTERIO DEL MEDIO<br>AMBIENTE |
| Material Particulado<br>Respirable<br>(MP10) | Concentración anual | 50 (μg/Nm3) | 50 (μg/Nm3) |
| Material Particulado Fino<br>Respirable (MP2,5) | Concentración de 24 horas | 50 (μg/Nm3) | Norma Primaria<br>D.S. No 12/2011 del<br>MINISTERIO DEL MEDIO<br>AMBIENTE |
| Material Particulado Fino<br>Respirable (MP2,5) | Concentración anual | 20 (μg/Nm3) | 20 (μg/Nm3) |
| Dióxido de Nitrógeno<br>(NO2) | Concentración de 1 hora | 400 (μg/Nm3) | Norma Primaria<br>D.S. No 114/2002 del<br>MINSEGPRES |
| Dióxido de Nitrógeno<br>(NO2) | Concentración anual | 100 (μg/Nm3) | 100 (μg/Nm3) |
| Dióxido de Azufre (SO2) | Concentración anual | 60 (μg/Nm3) | Norma Primaria<br>D.S. No 104/2018 del<br>MINISTERIO DEL MEDIO<br>AMBIENTE |
| Dióxido de Azufre (SO2) | Concentración de 24 horas | 150 (μg/Nm3) | 150 (μg/Nm3) |
| Dióxido de Azufre (SO2) | Concentración de 1 hora | 350 (μg/Nm3) | 350 (μg/Nm3) |
| Dióxido de Azufre (SO2) | Concentración anual | 80 (μg/Nm3) | Norma Secundaria<br>D.S. No 22/2009<br>MINSEGPRES para la zona<br>norte |
| Dióxido de Azufre (SO2) | Concentración de 24 horas | 365 (μg/Nm3) | 365 (μg/Nm3) |
| Dióxido de Azufre (SO2) | Concentración de 1 hora | 1.000 (μg/Nm3) | 1.000 (μg/Nm3) |

**Tabla 3: ** . Estaciones de monitoreo de calidad del aire**

| Estación | Coordenadas UTM | Col3 | Distancia al<br>Proyecto (km) | Altura sobre el<br>nivel del mar (m) | Contaminantes<br>medidos |
| --- | --- | --- | --- | --- | --- |
| **Estación** | **X (m)** | **Y (m)** | **Y (m)** | **Y (m)** | **Y (m)** |
| SAPU | 731.369 | 5.897.676 | 18 | 130 | MP10 - NO2 - SO2 |
| Quinel | 730.529 | 5.898.723 | 19 | 160 | MP10 - NO2 |

**Tabla 4: ** . Percentil 98 de las concentraciones 24 horas de MP10 registrada por la estación SAPU.**

| Año | Percentil 98 de las<br>Concentraciones 24 horas (μg/m3) | Norma D.S. No 59/1998 (μg/m3) |
| --- | --- | --- |
| 2019 | 107,8 | **130** |
| 2020 | 90,6 | 90,6 |
| 2021 | 110,7 | 110,7 |

**Tabla 6: ** . Concentración anual de MP10 registrada en estación SAPU. Período 2019-2021**

| Año | Concentración Anual (μg/m3) | Norma D.S. No 12/2021 (μg/m3) |
| --- | --- | --- |
| 2019 | 38,2 | **50** |
| 2020 | 33,0 | 33,0 |
| 2021 | 31,1 | 31,1 |
| **Promedio** | **34,1** | **34,1** |

**Tabla 7: ** . Concentración anual de MP10 registrada en estación Quinel. Período 2019-2021**

| Año | Concentración Anual (μg/m3) | Norma D.S. No 12/2021 (μg/m3) |
| --- | --- | --- |
| 2019 | 15,1 | **50** |
| 2020 | 34,5 | 34,5 |
| 2021 | 73,9 | 73,9 |
| **Promedio** | **41,1** | **41,1** |

**Tabla 8: ** . Percentil 99 de los máximos diarios de concentración de 1 hora de NO 2 registrada en la**

| Año | Percentil 99 de los máximos diarios<br>de concentración 1 hora (μg/m3) | Norma D.S. No 114/2002 (μg/m3) |
| --- | --- | --- |
| 2019 | 50,6 | **400** |
| 2020 | 49,5 | 49,5 |
| 2021 | 159,7 | 159,7 |
| **Promedio** | **86,6** | **86,6** |

**Tabla 9.: ** Percentil 99 de los máximos diarios de concentración de 1 hora de NO 2 registrada en la**

| Año | Percentil 99 de los máximos diarios<br>de concentración 1 hora (μg/m3) | Norma D.S. No 114/2002 (μg/m3) |
| --- | --- | --- |
| 2019 | 139,6 | **400** |
| 2020 | 65,8 | 65,8 |
| 2021 | 82,4 | 82,4 |
| **Promedio** | **95,9** | **95,9** |

**Tabla 10: ** . Concentración anual NO 2 registrada en la estación SAPU. Periodo 2019 - 2021.**

| Año | Concentración Anual (μg/m3) | Norma D.S. No 114/2002 (μg/m3) |
| --- | --- | --- |
| 2019 | 11,9 | **100** |
| 2020 | 10,7 | 10,7 |
| 2021 | 8,5 | 8,5 |
| **Promedio** | **10,4** | **10,4** |

**Tabla 11: ** . Concentración anual NO 2 registrada en la estación Quinel. Periodo 2019 - 2021.**

| Año | Concentración Anual (μg/m3) | Norma D.S. No 114/2002 (μg/m3) |
| --- | --- | --- |
| 2019 | 17,5 | **100** |
| 2020 | 14,7 | 14,7 |
| 2021 | 11,0 | 11,0 |
| **Promedio** | **14,4** | **14,4** |

**Tabla 12: ** . Percentil 98,5 de las concentraciones de 1 hora de SO 2 registrada en la estación SAPU.**

| Año | Percentil 98.5 concentración 1<br>hora (μg/m3) | Norma D.S. No 104/2019 (μg/m3) |
| --- | --- | --- |
| 2019 | 13,3 | **350** |
| 2020 | 14,7 | 14,7 |
| 2021 | 11,0 | 11,0 |
| **Promedio** | **13,0** | **13,0** |

**Tabla 13: ** . Percentil 99 de las concentraciones de 24 horas de SO 2 registrada en la estación SAPU.**

| Año | Percentil 99 de concentración<br>diaria (μg/m3) | Norma D.S. No 104/2019 (μg/m3) |
| --- | --- | --- |
| 2019 | 13,0 | **150** |
| 2020 | 14,2 | 14,2 |
| 2021 | 10,4 | 10,4 |
| **Promedio** | **12,5** | **12,5** |

**Tabla 14: ** . Concentración anual SO 2 registrada en la estación SAPU. Periodo 2019 - 2021.**

| Año | Concentración Trimestral (μg/m3) | Norma D.S. No 104/2019 (μg/m3) |
| --- | --- | --- |
| 2019 | 5,0 | **60** |
| 2020 | 6,2 | 6,2 |
| 2021 | 6,4 | 6,4 |
| **Promedio** | **5,9** | **5,9** |

**Tabla 15.: ** Características del dominio de modelación de la segunda grilla utilizada por el modelo WRF**

| Características Grilla 2 de WRF | Col2 |
| --- | --- |
| Resolución | 1 x 1 km |
| No de celdas en dirección X | 106 |
| No de celdas en dirección Y | 106 |
| Coordenadas del origen del dominio | Lat: -36,934; Lon: -72,292 |
| Total del área del dominio | 11.236 (km2) |

**Tabla 16.: ** Configuración de las principales parametrizaciones utilizadas en la modelación con WRF para**

| Variable | Nombre | Esquema | Descripción |
| --- | --- | --- | --- |
| Microfísica | mp_physics | WSM5 | WSM (3 especies<br>microfísicas) |
| Radiación de onda larga | ra_lw_physics | RRTM | Modelo de<br>transferencia radiativa<br>rápida que utiliza<br>tablas de eficiencia.<br>Cuenta con múltiples<br>bandas |
| Radiación de onda corta | ra_sw_physics | Dudhia scheme | Integración simple que<br>permite la absorción y<br>dispersión por nubes y<br>a cielo despejado |
| Capa superficial | sf_sfclay_physics | MM5 | Monin-Obukhov<br>similaridad |
| Superficie | sf_Surface_physcis | Thermal Diffusion<br>Scheme | Esquema de difusión<br>termal |
| Capa límite planetaria | bl_pbl_physics | YSU scheme | QNSE |

**Tabla 17.: ** Estadísticos matemáticos de literatura.**

| Estación | Latitud (°) | Longitud (°) |
| --- | --- | --- |
| RMSE | √∑(Mi−Oi)2<br>n<br>n<br>i=1<br> | (0, ∞) |
| BIASN | ∑<br>Mi−Oi<br>n<br>i=1<br>∑<br>Oi<br>n<br>i=1<br> | (-∞,∞) |
| R | ∑<br>(Mi−M) −(Oi−O)<br>n<br>i=1<br>{∑<br>(Mi−M)<br>2<br>n<br>i=1<br>∑<br>(Oi−O)2}<br>n<br>i=1<br>1/2 | [-1,1] |

**Tabla 18.: ** Resultados estadísticos obtenidos de la comparación de datos observados y modelados con**

| Estadística | Variable | Unidad | Estación Purén |
| --- | --- | --- | --- |
| RMSE | VV | m/s | 1,05 |
| RMSE | HR | % | 17,94 |
| RMSE | T | °C | 3,15 |
| BIASN | VV | m/s | 0,24 |
| BIASN | HR | % | 0,19 |
| BIASN | T | °C | -0,11 |
| R | VV | m/s | 0,72 |
| R | HR | % | 0,86 |
| R | T | °C | 0,95 |

**Tabla 19.: ** Actividades del Proyecto generadoras de emisiones atmosféricas.**

| Actividad | Contaminante |
| --- | --- |
| **Fase Construcción y Cierre** | **Fase Construcción y Cierre** |
| Excavación | MP10, MP2,5 y MPS |
| Carga y Descarga de material | MP10, MP2,5 y MPS |
| Compactación | MP10, MP2,5 y MPS |
| Escarpe | MP10, MP2,5 y MPS |
| Maquinaria fuera de ruta | MP10, MP2,5, MPS, NOx, CO, SOx y HC |
| Resuspensión por tránsito por caminos pavimentados | MP10, MP2,5 y MPS |
| Resuspensión por tránsito por caminos no pavimentados | MP10, MP2,5 y MPS |
| Operación de vehículos | MP10, MP2,5, MPS, NOx, CO, SOx y HC |
| Erosión Eólica por acopio de material | MP10, MP2,5 y MPS |
| Grupos electrógenos | MP10, MP2,5, MPS, NOx, CO, SOx y HC |
| **Fase Operación** | **Fase Operación** |
| Resuspensión por tránsito por caminos pavimentados | MP10, MP2,5 y MPS |
| Resuspensión por tránsito por caminos no pavimentados | MP10, MP2,5 y MPS |
| Operación de vehículos | MP10, MP2,5, MPS, NOx, CO, SOx y HC |
| Grupos electrógenos* | MP10, MP2,5, MPS, NOx, CO, SOx y HC |

**Tabla 20.: ****

| bla 20. Peso promedio vehículos del proyecto. | Col2 | Col3 |
| --- | --- | --- |
| **Peso y capacidad de carga de cada uno de los vehículos** | **Valor** | **Unidad** |
| **Camión rígido + 2 ejes ** | **Camión rígido + 2 ejes ** | **Camión rígido + 2 ejes ** |
| Peso vacío | 9,3 | t |
| Peso con carga | 31,5 | t |
| Peso Promedio | 20,4 | t |
| **Camión Semiremolque** | **Camión Semiremolque** | **Camión Semiremolque** |
| Peso vacío | 16 | t |
| Peso con carga | 40 | t |
| Peso Promedio | 28 | t |
| **Liviano** | **Liviano** | **Liviano** |
| Peso vacío | 2 | t |
| Peso con carga | 3 | t |
| Peso Promedio | 2,5 | t |
| **Sobredimensionado** | **Sobredimensionado** | **Sobredimensionado** |
| Peso vacío | 16 | t |
| Peso con carga | 60 | t |
| Peso Promedio | 38 | t |
| **Aljibe** | **Aljibe** | **Aljibe** |
| Peso vacío | 17 | t |
| Peso con carga | 27 | t |
| Peso Promedio | 22 | t |
| **Camión 3/4** | **Camión 3/4** | **Camión 3/4** |
| Peso vacío | 2,07 | t |
| Peso con carga | 5,7 | t |
| Peso Promedio | 3,885 | t |

**Tabla 21.: ** Factores de emisión por contaminante según tipo de vehículo, en gramos por kilómetros de**

| Contaminante | Tipo de vehículo | FE (g/veh-km) |
| --- | --- | --- |
| **MP** | Livianos | 0,67*(4,5*10^-5*V^2-4,885*10^-3*V+0,1932) |
| **MP** | Pesados | ((0,5224+(4,4906*10^-3*V))+(((-1,6281*10^-2-4,4906*10^-3)*(1-<br>EXP(((-1)* 2,4923*10^-2*V)))/2,4923*10^-2))) |
| **SOx** | Livianos | 2*(0,0198*V^2-2,506*V+137,42)* Scomb/1000000 |
| **SOx** | Pesados | 2*((195,476155665251+(464,243926657849*EXP(((-<br>1)*0,0471738612383144)*V)))+(22777,7239789702*EXP(((-<br>1)*0,88418501143649)*V)))* Scomb/1000000 |
| **NOx** | Livianos | 0,84*(2,41*10^-4*V^2-3,181*10^-2*V+2,0247) |
| **NOx** | Pesados | ((7,20536564798271+(16,4001356804762*EXP(((-<br>1)*0,0478197060782861)*V)))+(55,7002667265637*EXP(((-<br>1)*0,444673457893458)*V))) |
| **CO** | Livianos | 0,82*(2,23*10^-4*V^2-2,6*10^-2*V+1,076) |
| **CO** | Pesados | (1/(((-0,00010960585101578<br>*(V2))+(0,0174064839534468*V))+0,0779217214718428)) |
| **HC** | Livianos | 0,62*(0,0000175*V^2-0,00284*V+0,2162) |
| **HC** | Pesados | ((0,162905538155383+(0,828009789857126*exp(((-<br>1)*0,0248119637491787)*V))) +(2,67001448123625*exp(((-<br>1)*0,124882855805357)*V))) |

**Tabla 22.: ** Factores de emisión por contaminante según potencia, tecnología Stage II, en gramos por**

| Fuente de Emisión | Contaminante | Factor de Emisión (g/kW-h) |
| --- | --- | --- |
| **Motores potencia entre 8**<br>**y 19 kW** | CO | 5,00 |
| **Motores potencia entre 8**<br>**y 19 kW** | NOx | 11,20 |
| **Motores potencia entre 8**<br>**y 19 kW** | MP | 1,60 |
| **Motores potencia entre 8**<br>**y 19 kW** | SOx | 0,0081 |
| **Motores potencia entre**<br>**19 y 37 kW** | CO | 2,20 |
| **Motores potencia entre**<br>**19 y 37 kW** | NOx | 6,50 |
| **Motores potencia entre**<br>**19 y 37 kW** | MP | 0,40 |
| **Motores potencia entre**<br>**19 y 37 kW** | SOx | 0,0079 |
| **Motores potencia entre**<br>**37 y 56 kW** | CO | 2,20 |
| **Motores potencia entre**<br>**37 y 56 kW** | NOx | 5,50 |
| **Motores potencia entre**<br>**37 y 56 kW** | MP | 0,20 |
| **Motores potencia entre**<br>**37 y 56 kW** | SOx | 0,0078 |
| **Motores potencia entre**<br>**56 y 75 kW** | CO | 2,20 |
| **Motores potencia entre**<br>**56 y 75 kW** | NOx | 5,50 |
| **Motores potencia entre**<br>**56 y 75 kW** | MP | 0,20 |
| **Motores potencia entre**<br>**56 y 75 kW** | SOx | 0,0078 |
| **Motores potencia entre**<br>**75 y 130 kW** | CO | 1,50 |
| **Motores potencia entre**<br>**75 y 130 kW** | NOx | 5,20 |
| **Motores potencia entre**<br>**75 y 130 kW** | MP | 0,20 |
| **Motores potencia entre**<br>**75 y 130 kW** | SOx | 0,0077 |
| **Motores potencia entre**<br>**130 y 560 kW** | CO | 1,50 |
| **Motores potencia entre**<br>**130 y 560 kW** | NOx | 5,20 |
| **Motores potencia entre**<br>**130 y 560 kW** | MP | 0,10 |
| **Motores potencia entre**<br>**130 y 560 kW** | SOx | 0,0075 |

**Tabla 23.: ** Factor de deterioro relativo a la vida útil de maquinaria diésel.**

| Tecnología | MP | NOx | CO | SOx | HC |
| --- | --- | --- | --- | --- | --- |
| **Stage II** | 0,2365 | 0,0045 | 0,0505 | - | 0,017 |

**Tabla 24.: ** Factor de ajuste transiente para maquinaria diésel.**

| Tecnología | Factor de carga | MP | NOx | CO | SOx | HC |
| --- | --- | --- | --- | --- | --- | --- |
| **Stage II** | C > 0,45 | 1,23 | 0,95 | 1,53 | - | 1,05 |

**Tabla 25.: ** Factor de emisión según potencia de grupo electrógeno.**

| Combustible | Unidad | CO | NOx | MP | SOx | HC* |
| --- | --- | --- | --- | --- | --- | --- |
| Diesel (hasta 600 hp) | kg/kg combustible | 0,0186271 | 0,08647 | 0,0060783 | 0,00568616 | 0,00706 |

**Tabla 26.: ** Factores de emisión de MP10 del proyecto Parque Eólico Dañicalqui.**

| Actividad | Col2 | Parámetros para Factores de Emisión | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 | Col14 | Col15 | Col16 | Factor Emisión | Col18 | Col19 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Actividad** | **Actividad** | **k ** | **s ** | **U ** | **sL** | **W ** | **FCP** | **M ** | **Σ Pi** | **V ** | **P ** | **FP** | **C ** | **FD** | **FA** | **Fórmula** | **Valor** | **Unidad** |
| **Actividad** | **Actividad** | **k ** | **% ** | **m/s** | **g/m2 ** | **t ** | **t ** | **% ** | **% ** | **km/h** | **kW** | **g/kW** | **g/kW** | **g/kW** | **g/kW** | **g/kW** | **g/kW** | **g/kW** |
| Excavaciones - preparación de terreno | Excavaciones - preparación de terreno | 0,75 | 10,5 |  |  |  |  | 6,5 |  |  |  |  |  |  |  | k*0,45*(s^1,5/M^1,4) | 8,36E-01 | kg/h |
| Carga | Carga | 0,35 |  | 5,0 |  |  |  | 6,5 |  |  |  |  |  |  |  | k*0,0016*(U/2,2)^1,3/(M/2)^1,4 | 3,13E-04 | kg/t |
| Descarga | Descarga | 0,35 |  | 5,0 |  |  |  | 6,5 |  |  |  |  |  |  |  | k*0,0016*(U/2,2)^1,3/(M/2)^1,4 | 3,13E-04 | kg/t |
| Compactación | Compactación | 0,75 | 10,5 |  |  |  |  | 6,5 |  |  |  |  |  |  |  | k*0,45*(s^1,5/M^1,4) | 8,36E-01 | kg/h |
| Escarpe | Escarpe |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 5,7 | 5,70E+00 | kg/km |
| Maquinaria fuera de ruta | Motoniveladora |  |  |  |  |  |  |  |  |  | 95 | 0,2 | 0,8 | 0,2365 | 1,23 | P*FP*C*(1+FD)*FA/1000 | 2,31E-02 | kg/h |
| Maquinaria fuera de ruta | Compactadora |  |  |  |  |  |  |  |  |  | 1043 | 0,045 | 0,8 | 0,2365 | 1,23 | 1,23 | 5,71E-02 | kg/h |
| Maquinaria fuera de ruta | Bulldozer |  |  |  |  |  |  |  |  |  | 161 | 0,1 | 0,8 | 0,2365 | 1,23 | 1,23 | 1,96E-02 | kg/h |
| Maquinaria fuera de ruta | Retroexcavadora |  |  |  |  |  |  |  |  |  | 71 | 0,2 | 0,8 | 0,2365 | 1,23 | 1,23 | 1,73E-02 | kg/h |
| Maquinaria fuera de ruta | Grúa de apoyo |  |  |  |  |  |  |  |  |  | 151 | 0,1 | 0,8 | 0,2365 | 1,23 | 1,23 | 1,84E-02 | kg/h |
| Maquinaria fuera de ruta | Grúa principal |  |  |  |  |  |  |  |  |  | 455 | 0,1 | 0,8 | 0,2365 | 1,23 | 1,23 | 5,54E-02 | kg/h |
| Resuspensión camino No<br>Pavimentado | Camión rígido + 2 ejes | 1,5 | 5 |  |  | 20,4 | 0,814 |  |  |  |  |  |  |  |  | k*0,2819*(s/12)^0,9*(W/2,72)^0,45*FCP | 3,87E-01 | kg/VKT |
| Resuspensión camino No<br>Pavimentado | Camión Semiremolque | 1,5 | 5 |  |  | 28 | 0,814 |  |  |  |  |  |  |  |  |  | 4,47E-01 | kg/VKT |
| Resuspensión camino No<br>Pavimentado | Liviano | 1,5 | 5 |  |  | 2,5 | 0,814 |  |  |  |  |  |  |  |  |  | 1,51E-01 | kg/VKT |
| Resuspensión camino No<br>Pavimentado | Sobredimensionado | 1,5 | 5 |  |  | 38 | 0,814 |  |  |  |  |  |  |  |  |  | 5,13E-01 | kg/VKT |
| Resuspensión camino<br>Pavimentado | Camión rígido + 2 ejes | 0,62 |  |  | 0,2 | 20,4 | 0,953 |  |  |  |  |  |  |  |  | k*(sL)^0,91*(W*1,1023)^1,02/1000*FCP | 3,27E-03 | kg/VKT |
| Resuspensión camino<br>Pavimentado | Camión Semiremolque | 0,62 |  |  | 0,2 | 28,0 | 0,953 |  |  |  |  |  |  |  |  |  | 4,52E-03 | kg/VKT |
| Resuspensión camino<br>Pavimentado | liviano | 0,62 |  |  | 0,2 | 2,5 | 0,953 |  |  |  |  |  |  |  |  |  | 3,84E-04 | kg/VKT |
| Resuspensión camino<br>Pavimentado | Sobredimensionado | 0,62 |  |  | 0,2 | 38,0 | 0,953 |  |  |  |  |  |  |  |  |  | 6,17E-03 | kg/VKT |
| Combustión vehículos | Camión rígido + 2 ejes |  |  |  |  |  |  |  |  | 80 |  |  |  |  |  | ((0,5224+(4,4906*10^-3*V))+(((-<br>1,6281*10^-2-4,4906*10^-3)*(1-EXP(((-<br>1)* 2,4923*10^-2*V)))/2,4923*10^-<br>2)))/1000 | 8,82E-04 | kg/VKT |
| Combustión vehículos | Camión Semiremolque |  |  |  |  |  |  |  |  | 80 |  |  |  |  |  |  | 8,82E-04 | kg/VKT |
| Combustión vehículos | liviano |  |  |  |  |  |  |  |  | 80 |  |  |  |  |  | 0,67*(4,5*10^-5*V^2-4,885*10^-<br>3*V+0,1932)/1000 | 6,06E-05 | kg/VKT |
| Combustión vehículos | Sobredimensionado |  |  |  |  |  |  |  |  | 30 |  |  |  |  |  | ((0,5224+(4,4906*10^-3*V))+(((-<br>1,6281*10^-2-4,4906*10^-3)*(1-EXP(((-<br>1)* 2,4923*10^-2*V)))/2,4923*10^-<br>2)))/1000 | 6,57E-04 | kg/VKT |
| Combustión vehículos | Camión rígido + 2 ejes |  |  |  |  |  |  |  |  | 40 |  |  |  |  |  | ((0,5224+(4,4906*10^-3*V))+(((-<br>1,6281*10^-2-4,4906*10^-3)*(1-EXP(((-<br>1)* 2,4923*10^-2*V)))/2,4923*10^-<br>2)))/1000 | 7,02E-04 | kg/VKT |
| Combustión vehículos | Camión Semiremolque |  |  |  |  |  |  |  |  | 40 |  |  |  |  |  |  | 7,02E-04 | kg/VKT |
| Combustión vehículos | liviano |  |  |  |  |  |  |  |  | 40 |  |  |  |  |  | 0,67*(4,5*10^-5*V^2-4,885*10^-<br>3*V+0,1932)/1000 | 4,68E-05 | kg/VKT |
| Combustión vehículos | Sobredimensionado |  |  |  |  |  |  |  |  | 30 |  |  |  |  |  | ((0,5224+(4,4906*10^-3*V))+(((-<br>1,6281*10^-2-4,4906*10^-3)*(1-EXP(((-<br>1)* 2,4923*10^-2*V)))/2,4923*10^-<br>2)))/1000 | 6,57E-04 | kg/VKT |
| Erosión Eólica | Erosión Eólica | 0,5 |  |  |  |  |  |  | 1,53 |  |  |  |  |  |  | k * (Σ Pi) * 10<br>Pi = 58x(u*-ut*)^2+25x(u*-ut*) | 7,63 | kg/ha/año |
| Grupos electrógenos | Grupos electrógenos |  |  |  |  |  |  |  |  |  | 88 |  |  |  |  | 6,08E-03 | 6,08E-03 | kg/kg comb. |

**Tabla 27.: ** Factores de emisión de MP2,5 del proyecto Parque Eólico Dañicalqui.**

| Actividad | Col2 | Parámetros para Factores de Emisión | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 | Col14 | Col15 | Col16 | Factor Emisión | Col18 | Col19 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Actividad** | **Actividad** | **k ** | **s ** | **U ** | **sL** | **W ** | **FCP** | **M ** | **Σ Pi** | **V ** | **P ** | **FP** | **C ** | **FD** | **FA** | **Fórmula** | **Valor** | **Unidad** |
| **Actividad** | **Actividad** | **k ** | **% ** | **m/s** | **g/m2 ** | **t ** | **t ** | **% ** | **% ** | **km/h** | **kW** | **g/kW** | **g/kW** | **g/kW** | **g/kW** | **g/kW** | **g/kW** | **g/kW** |
| Excavaciones - preparación de terreno | Excavaciones - preparación de terreno | 0,105 | 10,5 |  |  |  |  | 6,5 |  |  |  |  |  |  |  | k*2,6*(s^1,2/M^1,3) | 4,03E-01 | kg/h |
| Carga | Carga | 0,053 |  | 5,0 |  |  |  | 6,5 |  |  |  |  |  |  |  | k*0,0016*(U/2,2)^1,3/(M/2)^1,4 | 4,73E-05 | kg/t |
| Descarga | Descarga | 0,053 |  | 5,0 |  |  |  | 6,5 |  |  |  |  |  |  |  | k*0,0016*(U/2,2)^1,3/(M/2)^1,4 | 4,73E-05 | kg/t |
| Compactación | Compactación | 0,105 | 10,5 |  |  |  |  | 6,5 |  |  |  |  |  |  |  | k*2,6*(s^1,2/M^1,3) | 4,03E-01 | kg/h |
| Escarpe | Escarpe |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 0,855 | 8,55E-01 | kg/km |
| Maquinaria fuera de ruta | Motoniveladora |  |  |  |  |  |  |  |  |  | 95 | 0,2 | 0,8 | 0,2365 | 1,23 | P*FP*C*(1+FD)*FA/1000 | 2,31E-02 | kg/h |
| Maquinaria fuera de ruta | Compactadora |  |  |  |  |  |  |  |  |  | 1043 | 0,045 | 0,8 | 0,2365 | 1,23 | 1,23 | 5,71E-02 | kg/h |
| Maquinaria fuera de ruta | Bulldozer |  |  |  |  |  |  |  |  |  | 161 | 0,1 | 0,8 | 0,2365 | 1,23 | 1,23 | 1,96E-02 | kg/h |
| Maquinaria fuera de ruta | Retroexcavadora |  |  |  |  |  |  |  |  |  | 71 | 0,2 | 0,8 | 0,2365 | 1,23 | 1,23 | 1,73E-02 | kg/h |
| Maquinaria fuera de ruta | Grúa de apoyo |  |  |  |  |  |  |  |  |  | 151 | 0,1 | 0,8 | 0,2365 | 1,23 | 1,23 | 1,84E-02 | kg/h |
| Maquinaria fuera de ruta | Grúa principal |  |  |  |  |  |  |  |  |  | 455 | 0,1 | 0,8 | 0,2365 | 1,23 | 1,23 | 5,54E-02 | kg/h |
| Resuspensión camino No<br>Pavimentado | Camión rígido + 2 ejes | 0,15 | 5 |  |  | 20,4 | 0,814 |  |  |  |  |  |  |  |  | k*0,2819*(s/12)^0,9*(W/2,72)^0,45*FCP | 3,87E-02 | kg/VKT |
| Resuspensión camino No<br>Pavimentado | Camión Semiremolque | 0,15 | 5 |  |  | 28 | 0,814 |  |  |  |  |  |  |  |  |  | 4,47E-02 | kg/VKT |
| Resuspensión camino No<br>Pavimentado | liviano | 0,15 | 5 |  |  | 2,5 | 0,814 |  |  |  |  |  |  |  |  |  | 1,51E-02 | kg/VKT |
| Resuspensión camino No<br>Pavimentado | Sobredimensionado | 0,15 | 5 |  |  | 38 | 0,814 |  |  |  |  |  |  |  |  |  | 5,13E-02 | kg/VKT |
| Resuspensión camino<br>Pavimentado | Camión rígido + 2 ejes | 0,15 |  |  | 0,2 | 20,4 | 0,953 |  |  |  |  |  |  |  |  | k*(sL)^0,91*(W*1,1023)^1,02/1000*FCP | 7,91E-04 | kg/VKT |
| Resuspensión camino<br>Pavimentado | Camión Semiremolque | 0,15 |  |  | 0,2 | 28,0 | 0,953 |  |  |  |  |  |  |  |  |  | 1,09E-03 | kg/VKT |
| Resuspensión camino<br>Pavimentado | liviano | 0,15 |  |  | 0,2 | 2,5 | 0,953 |  |  |  |  |  |  |  |  |  | 9,30E-05 | kg/VKT |
| Resuspensión camino<br>Pavimentado | Sobredimensionado | 0,15 |  |  | 0,2 | 38,0 | 0,953 |  |  |  |  |  |  |  |  |  | 1,49E-03 | kg/VKT |
| Combustión vehículos | Camión rígido + 2 ejes |  |  |  |  |  |  |  |  | 80 |  |  |  |  |  | ((0,5224+(4,4906*10^-3*V))+(((-<br>1,6281*10^-2-4,4906*10^-3)*(1-EXP(((-<br>1)* 2,4923*10^-2*V)))/2,4923*10^-<br>2)))/1000 | 8,82E-04 | kg/VKT |
| Combustión vehículos | Camión Semiremolque |  |  |  |  |  |  |  |  | 80 |  |  |  |  |  |  | 8,82E-04 | kg/VKT |
| Combustión vehículos | liviano |  |  |  |  |  |  |  |  | 80 |  |  |  |  |  | 0,67*(4,5*10^-5*V^2-4,885*10^-<br>3*V+0,1932)/1000 | 6,06E-05 | kg/VKT |
| Combustión vehículos | Sobredimensionado |  |  |  |  |  |  |  |  | 30 |  |  |  |  |  | ((0,5224+(4,4906*10^-3*V))+(((-<br>1,6281*10^-2-4,4906*10^-3)*(1-EXP(((-<br>1)* 2,4923*10^-2*V)))/2,4923*10^-<br>2)))/1000 | 6,57E-04 | kg/VKT |
| Combustión vehículos | Camión rígido + 2 ejes |  |  |  |  |  |  |  |  | 40 |  |  |  |  |  | ((0,5224+(4,4906*10^-3*V))+(((-<br>1,6281*10^-2-4,4906*10^-3)*(1-EXP(((-<br>1)* 2,4923*10^-2*V)))/2,4923*10^-<br>2)))/1000 | 7,02E-04 | kg/VKT |
| Combustión vehículos | Camión Semiremolque |  |  |  |  |  |  |  |  | 40 |  |  |  |  |  |  | 7,02E-04 | kg/VKT |
| Combustión vehículos | liviano |  |  |  |  |  |  |  |  | 40 |  |  |  |  |  | 0,67*(4,5*10^-5*V^2-4,885*10^-<br>3*V+0,1932)/1000 | 4,68E-05 | kg/VKT |
| Combustión vehículos | Sobredimensionado |  |  |  |  |  |  |  |  | 30 |  |  |  |  |  | ((0,5224+(4,4906*10^-3*V))+(((-<br>1,6281*10^-2-4,4906*10^-3)*(1-EXP(((-<br>1)* 2,4923*10^-2*V)))/2,4923*10^-<br>2)))/1000 | 6,57E-04 | kg/VKT |
| Erosión Eólica | Erosión Eólica | 0,075 |  |  |  |  |  |  | 1,53 |  |  |  |  |  |  | k * (Σ Pi) * 10<br>Pi = 58x(u*-ut*)^2+25x(u*-ut*) | 1,15 | kg/ha/año |
| Grupos electrógenos | Grupos electrógenos |  |  |  |  |  |  |  |  |  | 88 |  |  |  |  | 6,08E-03 | 6,08E-03 | kg/kg comb. |

**Tabla 28.: ** Factores de emisión de MPS del proyecto Parque Eólico Dañicalqui.**

| Actividad | Col2 | Parámetros para Factores de Emisión | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 | Col14 | Col15 | Col16 | Factor Emisión | Col18 | Col19 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Actividad** | **Actividad** | **k ** | **s ** | **U ** | **sL** | **W ** | **FCP** | **M ** | **Σ Pi** | **V ** | **P ** | **FP** | **C ** | **FD** | **FA** | **Fórmula** | **Valor** | **Unidad** |
| **Actividad** | **Actividad** | **k ** | **% ** | **m/s** | **g/m2 ** | **t ** | **t ** | **% ** | **% ** | **km/h** | **kW** | **g/kW** | **g/kW** | **g/kW** | **g/kW** | **g/kW** | **g/kW** | **g/kW** |
| Excavaciones - preparación de terreno | Excavaciones - preparación de terreno | 1 | 10,5 |  |  |  |  | 6,5 |  |  |  |  |  |  |  | k*2,6*(s^1,2/M^1,3) | 3,83E+00 | kg/h |
| Carga | Carga | 0,74 |  | 5,0 |  |  |  | 6,5 |  |  |  |  |  |  |  | k*0,0016*(U/2,2)^1,3/(M/2)^1,4 | 6,61E-04 | kg/t |
| Descarga | Descarga | 0,74 |  | 5,0 |  |  |  | 6,5 |  |  |  |  |  |  |  | k*0,0016*(U/2,2)^1,3/(M/2)^1,4 | 6,61E-04 | kg/t |
| Compactación | Compactación | 1 | 10,5 |  |  |  |  | 6,5 |  |  |  |  |  |  |  | k*2,6*(s^1,2/M^1,3) | 3,83E+00 | kg/h |
| Escarpe | Escarpe |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 5 | 5,70E+00 | kg/km |
| Maquinaria fuera de ruta | Motoniveladora |  |  |  |  |  |  |  |  |  | 95 | 0,2 | 0,8 | 0,2365 | 1,23 | P*FP*C*(1+FD)*FA/1000 | 2,31E-02 | kg/h |
| Maquinaria fuera de ruta | Compactadora |  |  |  |  |  |  |  |  |  | 1043 | 0,045 | 0,8 | 0,2365 | 1,23 | 1,23 | 5,71E-02 | kg/h |
| Maquinaria fuera de ruta | Bulldozer |  |  |  |  |  |  |  |  |  | 161 | 0,1 | 0,8 | 0,2365 | 1,23 | 1,23 | 1,96E-02 | kg/h |
| Maquinaria fuera de ruta | Retroexcavadora |  |  |  |  |  |  |  |  |  | 71 | 0,2 | 0,8 | 0,2365 | 1,23 | 1,23 | 1,73E-02 | kg/h |
| Maquinaria fuera de ruta | Grúa de apoyo |  |  |  |  |  |  |  |  |  | 151 | 0,1 | 0,8 | 0,2365 | 1,23 | 1,23 | 1,84E-02 | kg/h |
| Maquinaria fuera de ruta | Grúa principal |  |  |  |  |  |  |  |  |  | 455 | 0,1 | 0,8 | 0,2365 | 1,23 | 1,23 | 5,54E-02 | kg/h |
| Resuspensión camino No<br>Pavimentado | Camión rígido + 2 ejes | 4,9 | 5 |  |  | 20,4 | 0,814 |  |  |  |  |  |  |  |  | k*0,2819*(s/12)^0,9*(W/2,72)^0,45*FCP | 1,27E+00 | kg/VKT |
| Resuspensión camino No<br>Pavimentado | Camión Semiremolque | 4,9 | 5 |  |  | 28 | 0,814 |  |  |  |  |  |  |  |  |  | 1,46E+00 | kg/VKT |
| Resuspensión camino No<br>Pavimentado | liviano | 4,9 | 5 |  |  | 2,5 | 0,814 |  |  |  |  |  |  |  |  |  | 4,92E-01 | kg/VKT |
| Resuspensión camino No<br>Pavimentado | Sobredimensionado | 4,9 | 5 |  |  | 38 | 0,814 |  |  |  |  |  |  |  |  |  | 1,67E+00 | kg/VKT |
| Resuspensión camino<br>Pavimentado | Camión rígido + 2 ejes | 3,23 |  |  | 0,2 | 20,4 | 0,953 |  |  |  |  |  |  |  |  | k*(sL)^0,91*(W*1,1023)^1,02/1000*FCP | 1,70E-02 | kg/VKT |
| Resuspensión camino<br>Pavimentado | Camión Semiremolque | 3,23 |  |  | 0,2 | 28,0 | 0,953 |  |  |  |  |  |  |  |  |  | 2,35E-02 | kg/VKT |
| Resuspensión camino<br>Pavimentado | liviano | 3,23 |  |  | 0,2 | 2,5 | 0,953 |  |  |  |  |  |  |  |  |  | 2,00E-03 | kg/VKT |
| Resuspensión camino<br>Pavimentado | Sobredimensionado | 3,23 |  |  | 0,2 | 38,0 | 0,953 |  |  |  |  |  |  |  |  |  | 3,21E-02 | kg/VKT |
| Combustión vehículos | Camión rígido + 2 ejes |  |  |  |  |  |  |  |  | 80 |  |  |  |  |  | ((0,5224+(4,4906*10^-3*V))+(((-<br>1,6281*10^-2-4,4906*10^-3)*(1-EXP(((-<br>1)* 2,4923*10^-2*V)))/2,4923*10^-<br>2)))/1000 | 8,82E-04 | kg/VKT |
| Combustión vehículos | Camión Semiremolque |  |  |  |  |  |  |  |  | 80 |  |  |  |  |  |  | 8,82E-04 | kg/VKT |
| Combustión vehículos | liviano |  |  |  |  |  |  |  |  | 80 |  |  |  |  |  | 0,67*(4,5*10^-5*V^2-4,885*10^-<br>3*V+0,1932)/1000 | 6,06E-05 | kg/VKT |
| Combustión vehículos | Sobredimensionado |  |  |  |  |  |  |  |  | 30 |  |  |  |  |  | ((0,5224+(4,4906*10^-3*V))+(((-<br>1,6281*10^-2-4,4906*10^-3)*(1-EXP(((-<br>1)* 2,4923*10^-2*V)))/2,4923*10^-<br>2)))/1000 | 6,57E-04 | kg/VKT |
| Combustión vehículos | Camión rígido + 2 ejes |  |  |  |  |  |  |  |  | 40 |  |  |  |  |  | ((0,5224+(4,4906*10^-3*V))+(((-<br>1,6281*10^-2-4,4906*10^-3)*(1-EXP(((-<br>1)* 2,4923*10^-2*V)))/2,4923*10^-<br>2)))/1000 | 7,02E-04 | kg/VKT |
| Combustión vehículos | Camión Semiremolque |  |  |  |  |  |  |  |  | 40 |  |  |  |  |  |  | 7,02E-04 | kg/VKT |
| Combustión vehículos | liviano |  |  |  |  |  |  |  |  | 40 |  |  |  |  |  | 0,67*(4,5*10^-5*V^2-4,885*10^-<br>3*V+0,1932)/1000 | 4,68E-05 | kg/VKT |
| Combustión vehículos | Sobredimensionado |  |  |  |  |  |  |  |  | 30 |  |  |  |  |  | ((0,5224+(4,4906*10^-3*V))+(((-<br>1,6281*10^-2-4,4906*10^-3)*(1-EXP(((-<br>1)* 2,4923*10^-2*V)))/2,4923*10^-<br>2)))/1000 | 6,57E-04 | kg/VKT |
| Erosión Eólica | Erosión Eólica | 1 |  |  |  |  |  |  | 1,53 |  |  |  |  |  |  | k * (Σ Pi) * 10<br>Pi = 58x(u*-ut*)^2+25x(u*-ut*) | 15,3 | kg/ha/año |
| Grupos electrógenos | Grupos electrógenos |  |  |  |  |  |  |  |  |  | 88 |  |  |  |  | 6,08E-03 | 6,08E-03 | kg/kg comb. |

**Tabla 29.: ** Factores de emisión de Gases del proyecto Parque Eólico Dañicalqui.**

| Actividad | Col2 | Parámetros para Factores de Emisión | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 | Col14 | Col15 | Col16 | Factor Emisión | Col18 | Col19 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Actividad** | **Actividad** | **k ** | **s ** | **U ** | **sL** | **W ** | **FCP** | **M ** | **Σ Pi** | **V ** | **P ** | **FP** | **C ** | **FD** | **FA** |  |  |  |
| **Actividad** | **Actividad** | **k ** | **% ** | **m/s** | **g/m2 ** | **t ** | **t ** | **% ** | **% ** | **km/h** | **kW** | **g/kW** | **g/kW** | **g/kW** | **g/kW** | **Fórmula** | **Valor** | **Unidad** |
| **NOx** | **NOx** | **NOx** | **NOx** | **NOx** | **NOx** | **NOx** | **NOx** | **NOx** | **NOx** | **NOx** | **NOx** | **NOx** | **NOx** | **NOx** | **NOx** | **NOx** | **NOx** | **NOx** |
| Maquinaria fuera<br>de ruta | Motoniveladora |  |  |  |  |  |  |  |  |  | 95 | 5,2 | 0,8 | 0,0045 | 0,95 | P*FP*C*(1+FD)*FA/1000 | 3.77E-01 | kg/h |
| Maquinaria fuera<br>de ruta | Compactadora |  |  |  |  |  |  |  |  |  | 1043 | 3,5 | 0,8 | 0,0045 | 0,95 | 0,95 | 2.79E+00 | kg/h |
| Maquinaria fuera<br>de ruta | Bulldozer |  |  |  |  |  |  |  |  |  | 161 | 5,2 | 0,8 | 0,0045 | 0,95 | 0,95 | 6.39E-01 | kg/h |
| Maquinaria fuera<br>de ruta | Retroexcavadora |  |  |  |  |  |  |  |  |  | 71 | 5,5 | 0,8 | 0,0045 | 0,95 | 0,95 | 2.98E-01 | kg/h |
| Maquinaria fuera<br>de ruta | Grúa de apoyo |  |  |  |  |  |  |  |  |  | 151 | 5,2 | 0,8 | 0,0045 | 0,95 | 0,95 | 5.99E-01 | kg/h |
| Maquinaria fuera<br>de ruta | Grúa principal |  |  |  |  |  |  |  |  |  | 455 | 5,2 | 0,8 | 0,0045 | 0,95 | 0,95 | 1.81E+00 | kg/h |
| Combustión<br>vehículos<br>Pavimentado | Camión rígido + 2 ejes |  |  |  |  |  |  |  |  | 80 |  |  |  |  |  | ((7,20536564798271+(16,4001356804762*EXP(((-<br>1)*0,0478197060782861)*V))) +(55,7002667265637*EXP(((-<br>1)*0,444673457893458)*V)))/1000 | 7.56E-03 | kg/VKT |
| Combustión<br>vehículos<br>Pavimentado | Camión Semiremolque |  |  |  |  |  |  |  |  | 80 |  |  |  |  |  |  | 7.56E-03 | kg/VKT |
| Combustión<br>vehículos<br>Pavimentado | liviano |  |  |  |  |  |  |  |  | 80 |  |  |  |  |  | 0,84*(2,41*10^-4*V^2-3,181*10^-2*V+2,0247)/1000 | 8.59E-04 | kg/VKT |
| Combustión<br>vehículos<br>Pavimentado | Sobredimensionado |  |  |  |  |  |  |  |  | 30 |  |  |  |  |  | ((7,20536564798271+(16,4001356804762*EXP(((-<br>1)*0,0478197060782861)*V))) +(55,7002667265637*EXP(((-<br>1)*0,444673457893458)*V)))/1000 | 1.11E-02 | kg/VKT |
| Combustión<br>vehículos No<br>Pavimentado | Camión rígido + 2 ejes |  |  |  |  |  |  |  |  | 40 |  |  |  |  |  | ((7,20536564798271+(16,4001356804762*EXP(((-<br>1)*0,0478197060782861)*V))) +(55,7002667265637*EXP(((-<br>1)*0,444673457893458)*V)))/1000 | 9.63E-03 | kg/VKT |
| Combustión<br>vehículos No<br>Pavimentado | Camión Semiremolque |  |  |  |  |  |  |  |  | 40 |  |  |  |  |  |  | 9.63E-03 | kg/VKT |
| Combustión<br>vehículos No<br>Pavimentado | liviano |  |  |  |  |  |  |  |  | 40 |  |  |  |  |  | 0,84*(2,41*10^-4*V^2-3,181*10^-2*V+2,0247)/1000 | 9.56E-04 | kg/VKT |
| Combustión<br>vehículos No<br>Pavimentado | Sobredimensionado |  |  |  |  |  |  |  |  | 30 |  |  |  |  |  | ((7,20536564798271+(16,4001356804762*EXP(((-<br>1)*0,0478197060782861)*V))) +(55,7002667265637*EXP(((-<br>1)*0,444673457893458)*V)))/1000 | 1.11E-02 | kg/VKT |
| Grupos electrógenos | Grupos electrógenos |  |  |  |  |  |  |  |  |  | 88 |  |  |  |  | 8,65E-02 | 8,65E-02 | kg/kg comb. |
| **CO** | **CO** | **CO** | **CO** | **CO** | **CO** | **CO** | **CO** | **CO** | **CO** | **CO** | **CO** | **CO** | **CO** | **CO** | **CO** | **CO** | **CO** | **CO** |
| Maquinaria fuera<br>de ruta | Motoniveladora |  |  |  |  |  |  |  |  |  | 95 | 1,5 | 0,8 | 0,0505 | 1,53 | P*FP*C*(1+FD)*FA/1000 | 1.83E-01 | kg/h |
| Maquinaria fuera<br>de ruta | Compactadora |  |  |  |  |  |  |  |  |  | 1043 | 0,101 | 0,8 | 0,0505 | 1,53 | 1,53 | 1.35E-01 | kg/h |
| Maquinaria fuera<br>de ruta | Bulldozer |  |  |  |  |  |  |  |  |  | 161 | 1,5 | 0,8 | 0,0505 | 1,53 | 1,53 | 3.11E-01 | kg/h |
| Maquinaria fuera<br>de ruta | Retroexcavadora |  |  |  |  |  |  |  |  |  | 71 | 2,2 | 0,8 | 0,0505 | 1,53 | 1,53 | 2.01E-01 | kg/h |
| Maquinaria fuera<br>de ruta | Grúa de apoyo |  |  |  |  |  |  |  |  |  | 151 | 1,5 | 0,8 | 0,0505 | 1,53 | 1,53 | 2.91E-01 | kg/h |
| Maquinaria fuera<br>de ruta | Grúa principal |  |  |  |  |  |  |  |  |  | 455 | 1,5 | 0,8 | 0,0505 | 1,53 | 1,53 | 8.78E-01 | kg/h |
| Combustión<br>vehículos<br>Pavimentado | Camión rígido + 2 ejes |  |  |  |  |  |  |  |  | 80 |  |  |  |  |  | (1/(((-<br>0,00010960585101578*(V2))+(0,0174064839534468*V))+0,0<br>779217214718428))/1000 | 1.30E-03 | kg/VKT |
| Combustión<br>vehículos<br>Pavimentado | Camión Semiremolque |  |  |  |  |  |  |  |  | 80 |  |  |  |  |  |  | 1.30E-03 | kg/VKT |

**Tabla 30.: ** Cronograma de actividades de la fase de Construcción del proyecto Parque Eólico Dañicalqui.**

| ACTIVIDAD FASE DE CONSTRUCCIÓN | Col2 | Año 1 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 | Col14 | Año 2 | Col16 | Col17 | Col18 | Col19 | Col20 | Col21 | Col22 | Col23 | Col24 | Col25 | Col26 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ACTIVIDAD FASE DE CONSTRUCCIÓN** | **ACTIVIDAD FASE DE CONSTRUCCIÓN** | **1 ** | **2 ** | **3 ** | **4 ** | **5 ** | **6 ** | **7 ** | **8 ** | **9 ** | **1**<br>**0 ** | **1**<br>**1 ** | **1**<br>**2 ** | **1**<br>**3 ** | **1**<br>**4 ** | **1**<br>**5 ** | **1**<br>**6 ** | **1**<br>**7 ** | **1**<br>**8 ** | **1**<br>**9 ** | **2**<br>**0 ** | **2**<br>**1 ** | **2**<br>**2 ** | **2**<br>**3 ** | **2**<br>**4 ** |
| **Generales** | Construcción de accesos y<br>puente en estero Culenco<br>y en río Dañicalqui |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **Generales** | Topografía y mecánica de<br>suelo |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **Generales** | Habilitación de instalación<br>de faenas y zona de acopio |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **Generales** | Construcción de planta de<br>hormigón |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **Parque Eólico**<br>**(PE)** | Construcción de caminos<br>proyectados, construcción<br>de obras de artes y puentes<br>internos |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **Parque Eólico**<br>**(PE)** | Construcción de<br>fundaciones: Hormigonado |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **Parque Eólico**<br>**(PE)** | Construcción de zanjas para<br>cableado eléctrico |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **Parque Eólico**<br>**(PE)** | Montaje de los<br>aerogeneradores |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **Línea de**<br>**Transmisión**<br>**(LT)** | Habilitación faja de<br>servidumbre |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **Línea de**<br>**Transmisión**<br>**(LT)** | Materialización de<br>fundaciones de las<br>estructuras de la Línea de<br>transmisión |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **Línea de**<br>**Transmisión**<br>**(LT)** | Montaje de estructuras de<br>línea de transmisión y<br>tendido de los conductores |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **Línea de**<br>**Transmisión**<br>**(LT)** | Construcción de<br>subestación y sala de<br>control |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **PE + LT** | Pruebas y puesta en<br>servicio |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **PE + LT** | Limpieza general y retiro de<br>instalaciones |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

**Tabla 31.: ** Factores utilizados para calcular los niveles de actividad del proyecto Parque Eólico**

| Datos | Unidad | Cantidad | Cálculo de Actividad |
| --- | --- | --- | --- |
| Densidad del material | t/m3 | 1,610 (1) | Material de relleno y excavaciones |
| Rendimiento Excavadora (2) | m3/h | 30 | Horas de excavación de maquinaria |
| Rendimiento maquinaria escarpe (2) | km/ha | 3,57 | Kilómetros de escarpe |

**Tabla 32.: ** Nivel de actividad correspondiente a excavación del proyecto Parque Eólico Dañicalqui.**

| Parte del Proyecto | Información de<br>Cubicación | Unidad | Nivel actividad | Col5 | Col6 | Unidad |
| --- | --- | --- | --- | --- | --- | --- |
| **Parte del Proyecto** | **Información de**<br>**Cubicación** | **Unidad** | **Año 1** | **Año 2** | **Total** | **Total** |
| **PE** | **PE** | **PE** | **PE** | **PE** | **PE** | **PE** |
| Plataformas, obras anexas(1) y caminos | 374.609 | m3 | 5.219 | 7.268 | 12.487 | h |
| Aerogeneradores | 54.217 | m3 | 755 | 1.052 | 1.807 | h |
| Puentes y obras de arte: Puente río Dañicalqui | 797 | m3 | 11 | 15 | 27 | h |
| Puentes y obras de arte: Puente estero Culenco | 105 | m3 | 1 | 2 | 4 | h |
| Puentes y obras de arte: Puente Canales | 140 | m3 | 2 | 3 | 5 | h |
| Puentes y obras de arte: Obras de Arte | 180 | m3 | 3 | 3 | 6 | h |
| Circuiros MT | 5.801 | m3 | 81 | 113 | 193 | h |
| **LT** | **LT** | **LT** | **LT** | **LT** | **LT** | **LT** |
| Línea de Transmisión | 2.520 | m3 | 35 | 49 | 84 | h |

**Tabla 33.: ** Nivel de actividad correspondiente a carguío de material del proyecto Parque Eólico**

| Parte del Proyecto | Información de<br>Cubicación | Unidad | Nivel actividad | Col5 | Col6 | Unidad |
| --- | --- | --- | --- | --- | --- | --- |
| **Parte del Proyecto** | **Información de**<br>**Cubicación** | **Unidad** | **Año 1** | **Año 2** | **Total** | **Total** |
| **PE** | **PE** | **PE** | **PE** | **PE** | **PE** | **PE** |
| Plataformas, obras anexas(1) y caminos | 374.609 | m3 | 252.098 | 351.023 | 603.121 | t |
| Aerogeneradores | 54.217 | m3 | 36.486 | 50.804 | 87.290 | t |
| Puentes y obras de arte: Puente río Dañicalqui | 797 | m3 | 536 | 747 | 1.283 | t |
| Puentes y obras de arte: Puente estero Culenco | 105 | m3 | 71 | 98 | 169 | t |
| Puentes y obras de arte: Puente Canales | 140 | m3 | 94 | 131 | 225 | t |
| Puentes y obras de arte: Obras de Arte | 180 | m3 | 121 | 169 | 290 | t |
| Circuiros MT | 5.801 | m3 | 3.904 | 5.436 | 9.340 | t |
| Material de escarpe | 32.020 | m3 | 21.548 | 30.004 | 51.553 | t |
| **LT** | **LT** | **LT** | **LT** | **LT** | **LT** | **LT** |
| Línea de Transmisión | 2.520 | m3 | 1.696 | 2.362 | 4.058 | t |

**Tabla 34.: ** Nivel de actividad correspondiente a descarga de material del proyecto Parque Eólico**

| Parte del Proyecto | Información de<br>Cubicación | Unidad | Nivel actividad | Col5 | Col6 | Unidad |
| --- | --- | --- | --- | --- | --- | --- |
| **Parte del Proyecto** | **Información de**<br>**Cubicación** | **Unidad** | **Año 1** | **Año 2** | **Total** | **Total** |
| **PE** | **PE** | **PE** | **PE** | **PE** | **PE** | **PE** |
| Plataformas, obras anexas(1) y caminos | 230.772 | m3 | 155.301 | 216.242 | 371.543 | t |
| Aerogeneradores | 14.653 | m3 | 9.861 | 13.731 | 23.592 | t |
| Puentes y obras de arte: Puente río Dañicalqui | 860 | m3 | 578 | 806 | 1.384 | t |
| Puentes y obras de arte: Puente estero Culenco | 79 | m3 | 53 | 74 | 128 | t |
| Puentes y obras de arte: Puente Canales | 106 | m3 | 71 | 99 | 170 | t |
| Puentes y obras de arte: Obras de Arte | 119 | m3 | 80 | 112 | 192 | t |
| Material de escarpe | 32.020 | m3 | 21.548 | 30.004 | 51.553 | t |
| **LT** | **LT** | **LT** | **LT** | **LT** | **LT** | **LT** |
| Línea de Transmisión | 2.251 | m3 | 1.515 | 2.109 | 3.624 | t |

**Tabla 35.: ** Nivel de actividad correspondiente a compactación del proyecto Parque Eólico Dañicalqui.**

| Parte del Proyecto | Información de<br>Cubicación | Unidad | Nivel actividad | Col5 | Col6 | Unidad |
| --- | --- | --- | --- | --- | --- | --- |
| **Parte del Proyecto** | **Información de**<br>**Cubicación** | **Unidad** | **Año 1** | **Año 2** | **Total** | **Total** |
| **PE** | **PE** | **PE** | **PE** | **PE** | **PE** | **PE** |
| Plataformas | 79.800 | m2 | 7 | 10 | 16 | h |
| Subestación | 5.100 | m2 | 0,4 | 0,6 | 1 | h |
| Caminos | 69.300 | m2 | 6 | 8 | 14 | h |
| Instalación de faenas | 17.900 | m2 | 2 | 2 | 4 | h |
| Planta de Hormigón | 10.200 | m2 | 1 | 1 | 2 | h |
| Plataforma Acopio de Aspas | 28.500 | m2 | 2 | 3 | 6 | h |
| Terraplén y corte | 80.900 | m2 | 7 | 10 | 17 | h |
| **LT** | **LT** | **LT** | **LT** | **LT** | **LT** | **LT** |
| Zona de acopio LT | 10.100 | m2 | 1 | 1 | 2 | h |

**Tabla 36.: ** Nivel de actividad correspondiente a escarpe del proyecto Parque Eólico Dañicalqui.**

| Parte del Proyecto | Información de<br>Cubicación | Unidad | Nivel actividad | Col5 | Col6 | Unidad |
| --- | --- | --- | --- | --- | --- | --- |
| **Parte del Proyecto** | **Información de**<br>**Cubicación** | **Unidad** | **Año 1** | **Año 2** | **Total** | **Total** |
| **PE** | **PE** | **PE** | **PE** | **PE** | **PE** | **PE** |
| Plataformas | 7,98 | ha | 11,9 | 16,6 | 28,5 | km |
| Subestación | 0,51 | ha | 0,8 | 1,1 | 1,8 | km |
| Caminos proyectos | 6,93 | ha | 10,3 | 14,4 | 24,7 | km |
| Instalación de faenas | 1,79 | ha | 2,7 | 3,7 | 6,4 | km |
| Planta de Hormigón | 1,02 | ha | 1,5 | 2,1 | 3,6 | km |
| Plataforma Acopio de Aspas | 2,85 | ha | 4,3 | 5,9 | 10,2 | km |
| Terraplén y corte | 8,09 | ha | 12,1 | 16,8 | 28,9 | km |
| **LT** | **LT** | **LT** | **LT** | **LT** | **LT** | **LT** |
| Zona de acopio LT | 1,01 | ha | 1,5 | 2,1 | 3,6 | km |

**Tabla 37.: ** Cantidad de maquinaria fuera de ruta y horas de operación del proyecto Parque Eólico**

| Maquinaria Construcción | Cantidad por día | Horas por día |
| --- | --- | --- |
| Motoniveladora | 4 | 9 |
| Compactadora | 3 | 9 |
| Bulldozer | 5 | 9 |
| Retroexcavadora | 5 | 9 |
| Grúa de apoyo | 1 | 7 |
| Grúa principal | 1 | 6 |

**Tabla 38.: ** Nivel de actividad correspondiente a maquinaria fuera de ruta del proyecto Parque Eólico**

| Parte del Proyecto | Días de operación | Col3 | Nivel actividad | Col5 | Col6 | Unidad |
| --- | --- | --- | --- | --- | --- | --- |
| **Parte del Proyecto** | **Año 1** | **Año 2** | **Año 1** | **Año 2** | **Total** | **Total** |
| **PE** | **PE** | **PE** | **PE** | **PE** | **PE** | **PE** |
| Motoniveladora | 352 | 22 | 12.672 | 792 | 13.464 | h |
| Compactadora | 352 | 22 | 9.504 | 594 | 10.098 | h |
| Bulldozer | 352 | 22 | 15.840 | 990 | 16.830 | h |
| Retroexcavadora | 374 | 198 | 16.830 | 8.910 | 25.740 | h |
| Grúa de apoyo | 0 | 154 | 0 | 1.078 | 1.078 | h |
| Grúa principal | 0 | 154 | 0 | 924 | 924 | h |
| **LT** | **LT** | **LT** | **LT** | **LT** | **LT** | **LT** |
| Motoniveladora | 88 | 198 | 3.168 | 7.128 | 10.296 | h |
| Compactadora | 88 | 198 | 2.376 | 5.346 | 7.722 | h |
| Bulldozer | 88 | 220 | 3.960 | 9.900 | 13.860 | h |
| Retroexcavadora | 88 | 220 | 3.960 | 9.900 | 13.860 | h |
| Grúa de apoyo | 0 | 88 | 0 | 616 | 616 | h |
| Grúa principal | 0 | 88 | 0 | 528 | 528 | h |

**Tabla 39.: ** Cantidad de viajes ida y vuelta y kilómetros a recorrer por caminos no pavimentados externos e internos en la fase de**

| Tipo<br>Camino | Nombre Item | Tipo vehículo | Cantidad de Viajes<br>(ida y vuelta) | Col5 | Distancia<br>no pav. (km) | km no pavimentados | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Tipo**<br>**Camino** | **Nombre Item** | **Tipo vehículo** | **Año 1** | **Año 2** | **Año 2** | **Año 1** | **Año 2** | **Total** |
| **PE** | **PE** | **PE** | **PE** | **PE** | **PE** | **PE** | **PE** | **PE** |
| **Externo** | Construcción de accesos y puente | Camión Semiremolque | 102 | 0 | 7,3 | 744,6 | 0 | 744,6 |
| **Externo** | Topografía y mecánica de suelo | liviano | 120 | 0 | 7,3 | 876 | 0 | 876 |
| **Externo** | Habilitación de instalación de faenas y<br>zona de acopio | Camión Semiremolque | 180 | 0 | 7,3 | 1.314 | 0 | 1.314 |
| **Externo** | Construcción de planta de hormigón | Camión Semiremolque | 120 | 0 | 7,3 | 876 | 0 | 876 |
| **Externo** | Personal, combustible, agua, residuos | Camión rígido + 2 ejes | 84 | 84 | 7,3 | 613,2 | 613,2 | 1.226,4 |
| **Externo** | Personal, combustible, agua, residuos | Camión Semiremolque | 396 | 396 | 7,3 | 2.890,8 | 2.890,8 | 5.781,6 |
| **Externo** | Personal, combustible, agua, residuos | liviano | 5.904 | 5.904 | 7,3 | 43.099,2 | 43.099,2 | 86.198,4 |
| **Externo** | Construcción de caminos proyectados | Camión Semiremolque | 13.125 | 2.625 | 7,3 | 95.812,5 | 19.162,5 | 114.975 |
| **Externo** | Construcción de fundaciones:<br>Hormigonado | Camión Semiremolque | 1.611 | 1.611 | 7,3 | 11.760,3 | 11.760,3 | 23.520,6 |
| **Externo** | Construcción de zanjas para cableado<br>eléctrico | Camión Semiremolque | 17 | 136 | 7,3 | 124,1 | 992,8 | 1.116,9 |
| **Externo** | Montaje de Aerogeneradores | Camión rígido + 2 ejes | 0 | 7 | 7,3 | 0 | 51,1 | 51,1 |
| **Externo** | Montaje de Aerogeneradores | Camión Semiremolque | 0 | 273 | 7,3 | 0 | 1.992,9 | 1.992,9 |
| **Externo** | Montaje de Aerogeneradores | Sobredimensionado | 0 | 70 | 7,3 | 0 | 511 | 511 |
| **Externo** | Habilitación faja de servidumbre | Camión rígido + 2 ejes | 0 | 120 | 7,3 | 0 | 876 | 876 |
| **Externo** | Construcción de subestación y Sala de<br>Control | Camión Semiremolque | 96 | 24 | 7,3 | 700,8 | 175,2 | 876 |
| **Externo** | Pruebas y puesta en servicio | liviano | 0 | 120 | 7,3 | 0 | 876 | 876 |
| **Externo** | Limpieza general y retiro de<br>instalaciones | liviano | 0 | 120 | 7,3 | 0 | 876 | 876 |
| **Interno** | Construcción de accesos y puente | Camión rígido + 2 ejes | 120 | 0 | 5,13 | 615,6 | 0 | 615,6 |
| **Interno** | Construcción de accesos y puente | Camión Semiremolque | 132 | 0 | 5,13 | 677,16 | 0 | 677,16 |
| **Interno** | Topografía y mecánica de suelo | liviano | 120 | 0 | 5,13 | 615,6 | 0 | 615,6 |
| **Interno** | Construcción de planta de hormigón | Camión Semiremolque | 120 | 0 | 5,13 | 615,6 | 0 | 615,6 |
| **Interno** | Personal, combustible, agua, residuos | Camión rígido + 2 ejes | 0 | 0 | 5,13 | 0 | 0 | 0 |

**Tabla 40.: ** Distancias de caminos externos e internos con supresor de polvo en la fase de construcción**

| Tipo Camino | Áreas con supresor Externo No Pavimentado | Distancia (m) |
| --- | --- | --- |
| **Externo** | **Acceso PE** | **Acceso PE** |
| **Externo** | Área supresor 1 | 523 |
| **Externo** | Área supresor 4 | 254 |
| **Externo** | Área supresor 5 | 245 |
| **Externo** | Área supresor 6 | 649 |
| **Externo** | Área supresor 7 | 272 |
| **Externo** | Área supresor 8 | 260 |
| **Externo** | Área supresor 9 | 232 |
| **Externo** | **Sub-Total PE** | **2.435** |
| **Externo** | **Acceso LT** | **Acceso LT** |
| **Externo** | Área supresor 2 | 405 |
| **Externo** | **Sub-Total LT** | **405** |
| **Total Externo** | **Total Externo** | **2.840** |
| **Interno** | **Áreas con supresor Interno No Pavimentado** | **Distancia (m)** |
| **Interno** | Área supresor 3 | 276 |
| **Interno** | Área supresor 4 | 113 |
| **Total Interno** | **Total Interno** | **389** |

**Tabla 41.: ** Nivel de actividad correspondiente a distancia a recorrer por tránsito vehicular en caminos**

| Tipo Camino | Tipo vehículo | Nivel actividad | Col4 | Col5 | Unidad |
| --- | --- | --- | --- | --- | --- |
| **Tipo Camino** | **Tipo vehículo** | **Año 1** | **Año 2** | **Total** | **Total** |
| **PE** | **PE** | **PE** | **PE** | **PE** | **PE** |
| Camino No Pavimentado<br>Externo (**sin Supresor de**<br>**Polvo**) Ruta N-85; SR/-861 | Camión rígido + 2 ejes | 409 | 1.027 | 1.435 | km |
| Camino No Pavimentado<br>Externo (**sin Supresor de**<br>**Polvo**) Ruta N-85; SR/-861 | Camión Semiremolque | 76.123 | 24.641 | 100.764 | km |
| Camino No Pavimentado<br>Externo (**sin Supresor de**<br>**Polvo**) Ruta N-85; SR/-861 | liviano | 29.307 | 29.891 | 59.197 | km |

**Tabla 42.: ** Cantidad de viajes ida y vuelta y kilómetros a recorrer por caminos pavimentados en ruta N-85 en la fase de construcción del**

| Tipo | Nombre Item | Tipo vehículo | Cantidad de Viajes<br>(ida y vuelta) | Col5 | Distancia pav.<br>(km) | km pavimentados | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Tipo** | **Nombre Item** | **Tipo vehículo** | **Año 1** | **Año 2** | **Año 2** | **año 1** | **año 2** | **Total** |
| **PE** | **PE** | **PE** | **PE** | **PE** | **PE** | **PE** | **PE** | **PE** |
| **Externo** | Construcción de accesos y puente | Camión Semiremolque | 102 | 0 | 22,7 | 2.315,4 | 0 | 2.315,4 |
| **Externo** | Topografía y mecánica de suelo | liviano | 120 | 0 | 22,7 | 2.724 | 0 | 2.724 |
| **Externo** | Habilitación de instalación de faenas y zona de<br>acopio | Camión Semiremolque | 180 | 0 | 22,7 | 4.086 | 0 | 4.086 |
| **Externo** | Construcción de planta de hormigón | Camión Semiremolque | 120 | 0 | 22,7 | 2.724 | 0 | 2.724 |
| **Externo** | Personal, combustible, agua, residuos | Camión rígido + 2 ejes | 84 | 84 | 22,7 | 1.906,8 | 1.906,8 | 3.813,6 |
| **Externo** | Personal, combustible, agua, residuos | Camión Semiremolque | 396 | 396 | 22,7 | 8.989,2 | 8.989,2 | 17.978,4 |
| **Externo** | Personal, combustible, agua, residuos | liviano | 5.904 | 5.904 | 22,7 | 134.020,8 | 134.020,8 | 268.041,6 |
| **Externo** | Construcción de caminos proyectados | Camión Semiremolque | 13.125 | 2.625 | 22,7 | 297.937,5 | 59.587,5 | 357.525 |
| **Externo** | Construcción de fundaciones: Hormigonado | Camión Semiremolque | 1.611 | 1.611 | 22,7 | 36.569,7 | 36.569,7 | 73.139,4 |
| **Externo** | Construcción de zanjas para cableado eléctrico | Camión Semiremolque | 17 | 136 | 22,7 | 385,9 | 3.087,2 | 3.473,1 |
| **Externo** | Montaje de Aerogeneradores | Camión rígido + 2 ejes | 0 | 7 | 22,7 | 0 | 158,9 | 158,9 |
| **Externo** | Montaje de Aerogeneradores | Camión Semiremolque | 0 | 273 | 22,7 | 0 | 6.197,1 | 6.197,1 |
| **Externo** | Montaje de Aerogeneradores | Sobredimensionado | 0 | 70 | 22,7 | 0 | 1.589 | 1.589 |
| **Externo** | Habilitación faja de servidumbre | Camión rígido + 2 ejes | 0 | 120 | 22,7 | 0 | 2.724 | 2.724 |
| **Externo** | Construcción de subestación y Sala de Control | Camión Semiremolque | 96 | 24 | 22,7 | 2.179,2 | 544,8 | 2.724 |
| **Externo** | Pruebas y puesta en servicio | liviano | 0 | 120 | 22,7 | 0 | 2.724 | 2.724 |
| **Externo** | Limpieza general y retiro de instalaciones | liviano | 0 | 120 | 22,7 | 0 | 2.724 | 2.724 |
| **LT** | **LT** | **LT** | **LT** | **LT** | **LT** | **LT** | **LT** | **LT** |
| **Externo** | Materialización de fundaciones de las<br>estructuras de la Línea de transmisión | Camión Semiremolque | 0 | 155 | 16,4 | 0 | 2542 | 2542 |
| **Externo** | Montaje de estructuras de línea de transmisión<br>y tendido de los conductore | Camión Semiremolque | 0 | 40 | 16,4 | 0 | 656 | 656 |

**Tabla 43.: ** Cantidad de viajes y kilómetros a recorrer por caminos pavimentados en rutas 5 y 152 en la fase de construcción del proyecto**

| Sector | Tipo vehículo | Cantidad de viajes Ruta 5-152 | Col4 | Col5 | Distancia<br>pav. (km) | km pavimentados | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Sector** | **Tipo vehículo** | **Año 1** | **Año 2** | **Total** | **Total** | **Año 1** | **Año 2** | **Total** |
| **PE** | Camión rígido + 2 ejes | 84 | 211 | 295 | 113 | 9.492 | 23.843 | 33.335 |
| **PE** | Camión Semiremolque | 15.647 | 5.065 | 20.712 | 113 | 1.768.111 | 572.345 | 2.340.456 |
| **PE** | liviano | 6.024 | 6.144 | 12.168 | 113 | 680.712 | 694.272 | 1.374.984 |
| **PE** | Sobredimensionado | 0 | 70 | 70 | 113 | 0 | 7.910 | 7.910 |
| **LT** | Camión Semiremolque | 0 | 195 | 195 | 113 | 0 | 22.035 | 22.035 |

**Tabla 44.: ** Nivel de actividad correspondiente a distancia a recorrer por tránsito vehicular en caminos**

| Tipo Camino | Tipo vehículo | Nivel actividad | Col4 | Col5 | Unidad |
| --- | --- | --- | --- | --- | --- |
| **Tipo Camino** | **Tipo vehículo** | **Año 1** | **Año 2** | **Total** | **Total** |
| **PE** | **PE** | **PE** | **PE** | **PE** | **PE** |
| Camino Pavimentado<br>Externo -<br>Ruta N-85; SR/-861 | Camión rígido + 2 ejes | 1.907 | 4.790 | 6.697 | km |
| Camino Pavimentado<br>Externo -<br>Ruta N-85; SR/-861 | Camión Semiremolque | 355.187 | 114.976 | 470.162 | km |
| Camino Pavimentado<br>Externo -<br>Ruta N-85; SR/-861 | liviano | 136.745 | 139.469 | 276.214 | km |
| Camino Pavimentado<br>Externo -<br>Ruta N-85; SR/-861 | Sobredimensionado | 0 | 1.589 | 1.589 | km |
| Camino Pavimentado<br>Externo -<br>Rutas 5 y 152 | Camión rígido + 2 ejes | 9.492 | 23.843 | 33.335 | km |
| Camino Pavimentado<br>Externo -<br>Rutas 5 y 152 | Camión Semiremolque | 1.768.111 | 572.345 | 2.340.456 | km |
| Camino Pavimentado<br>Externo -<br>Rutas 5 y 152 | liviano | 680.712 | 694.272 | 1.374.984 | km |
| Camino Pavimentado<br>Externo -<br>Rutas 5 y 152 | Sobredimensionado | 0 | 7.910 | 7.910 | km |
| **LT** | **LT** | **LT** | **LT** | **LT** | **LT** |
| Camino Pavimentado<br>Externo -<br>Ruta N-85; SR-857 | Camión Semiremolque | 0 | 3.198 | 3.198 | km |
| Camino Pavimentado<br>Externo -<br>Rutas 5 y 152 | Camión Semiremolque | 0 | 22.035 | 22.035 | km |

**Tabla 45.: ** Nivel de actividad correspondiente a distancia a recorrer por tránsito vehicular en caminos**

| Tipo de camino | Tipo vehículo | Nivel actividad | Col4 | Col5 | Unidad |
| --- | --- | --- | --- | --- | --- |
| **Tipo de camino** | **Tipo vehículo** | **Año 1** | **Año 2** | **Total** | **Total** |
| **PE** | **PE** | **PE** | **PE** | **PE** | **PE** |
| Combustión vehículos<br>Pavimentado | Camión rígido + 2 ejes | 1.907 | 4.790 | 6.697 | km |
| Combustión vehículos<br>Pavimentado | Camión Semiremolque | 355.187 | 114.976 | 470.162 | km |
| Combustión vehículos<br>Pavimentado | liviano | 136.745 | 139.469 | 276.214 | km |
| Combustión vehículos<br>Pavimentado | Sobredimensionado | 0 | 1.589 | 1.589 | km |
| Combustión vehículos<br>No Pavimentado | Camión rígido + 2 ejes | 18.430 | 20.019 | 38.448 | km |
| Combustión vehículos<br>No Pavimentado | Camión Semiremolque | 238.513 | 76.547 | 315.060 | km |
| Combustión vehículos<br>No Pavimentado | liviano | 73.770 | 75.262 | 149.032 | km |
| Combustión vehículos<br>No Pavimentado | Sobredimensionado | 0 | 870 | 870 | km |
| Combustión vehículos<br>No Pavimentado Ruta<br>5-152 | Camión rígido + 2 ejes | 9.492 | 23.843 | 33.335 | km |
| Combustión vehículos<br>No Pavimentado Ruta<br>5-152 | Camión Semiremolque | 1.768.111 | 594.380 | 2.340.456 | km |
| Combustión vehículos<br>No Pavimentado Ruta<br>5-152 | liviano | 680.712 | 694.272 | 1.374.984 | km |
| Combustión vehículos<br>No Pavimentado Ruta<br>5-152 | Sobredimensionado | 0 | 7.910 | 7.910 | km |

**Tabla 46.: ** Nivel de actividad correspondiente a erosión eólica de la fase de construcción del proyecto**

| Actividad | Nivel actividad | Col3 | Col4 | Unidad |
| --- | --- | --- | --- | --- |
| **Actividad** | **Año 1** | **Año 2** | **Total** | **Total** |
| **LT** | **LT** | **LT** | **LT** | **LT** |
| Acopio | 1,01 | 1,01 | 1,01 | ha |

**Tabla 47.: ** Nivel de actividad correspondiente a funcionamiento de grupos electrógenos durante la fase**

| Instalación | Cantidad de<br>equipos | Nivel actividad | Col4 | Col5 | Unidad |
| --- | --- | --- | --- | --- | --- |
| **Instalación** | **Cantidad de**<br>**equipos** | **Año 1** | **Año 2** | **Total** | **Total** |
| Instalación de faenas | 2 | 104.180 | 104.180 | 208.361 | kg comb |

**Tabla 48.: ** Cantidad de viajes y kilómetros a recorrer por caminos no pavimentados externos e internos**

| Actividad | Tipo de<br>vehículo | Viajes<br>año | Distancia recorrida en<br>caminos no pavimentados | Col5 | km no pavimentados | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Actividad** | **Tipo de**<br>**vehículo** | **Viajes**<br>**año** | **Caminos**<br>**Externos (de**<br>**acceso públicos)** | **Caminos**<br>**internos** | **Caminos**<br>**Externos (de**<br>**acceso públicos)** | **Caminos**<br>**internos** |
| Supervisión y mantenciones | Vehículo liviano | 1.800 | 7,3 | 6 | 26.280 | 21.600 |
| Mantención | Camión 3/4 | 12 | 7,3 | 6 | 175,2 | 144 |
| Agua Potable | Aljibe | 24 | 7,3 | 6 | 350,4 | 288 |
| Residuos peligrosos | Camión 3/4 | 4 | 7,3 | 6 | 58,4 | 48 |
| Residuos domiciliarios | Camión 3/4 | 48 | 7,3 | 6 | 700,8 | 576 |

**Tabla 49.: ** Nivel de actividad correspondiente a distancia a recorrer por tránsito vehicular en caminos**

| Tipo Camino | Tipo vehículo | Nivel actividad | Unidad |
| --- | --- | --- | --- |
| Caminos No Pavimentados -<br>Externo | Vehículo liviano | 26.280 | km |
| Caminos No Pavimentados -<br>Externo | Camión 3/4 Mantención | 175 | km |
| Caminos No Pavimentados -<br>Externo | Aljibe | 350 | km |
| Caminos No Pavimentados -<br>Externo | Camión 3/4 - Residuos Peligrosos | 58 | km |
| Caminos No Pavimentados -<br>Externo | Camión 3/4 - Residuos Domiciliarios | 701 | km |
| Caminos No Pavimentados -<br>Interno | Vehículo liviano | 21.600 | km |
| Caminos No Pavimentados -<br>Interno | Camión 3/4 Mantención | 144 | km |
| Caminos No Pavimentados -<br>Interno | Aljibe | 288 | km |
| Caminos No Pavimentados -<br>Interno | Camión 3/4 - Residuos Peligrosos | 48 | km |
| Caminos No Pavimentados -<br>Interno | Camión 3/4 - Residuos Domiciliarios | 576 | km |

**Tabla 50.: ** Cantidad de viajes y kilómetros a recorrer por caminos pavimentados en la fase de operación**

| Actividad | Tipo de vehículo | Viajes año | Distancia de camino<br>pavimentado | km recorridos<br>pavimentados |
| --- | --- | --- | --- | --- |
| **Ruta N-85** | **Ruta N-85** | **Ruta N-85** | **Ruta N-85** | **Ruta N-85** |
| Supervisión y mantenciones | Vehículo liviano | 1.800 | 21 | 75.600 |
| Mantención | Camión 3/4 | 12 | 21 | 504 |
| Agua Potable | Aljibe | 24 | 21 | 1.008 |
| Residuos peligrosos | Camión 3/4 | 4 | 40 | 320 |
| Residuos domiciliarios | Camión 3/4 | 48 | 40 | 3.840 |
| **Ruta 5 y 152** | **Ruta 5 y 152** | **Ruta 5 y 152** | **Ruta 5 y 152** | **Ruta 5 y 152** |
| Supervisión y mantenciones | Vehículo liviano | 1.800 | 113 | 406.800 |
| Mantención | Camión 3/4 | 12 | 113 | 2.712 |
| Agua Potable | Aljibe | 24 | 113 | 5.424 |
| Residuos peligrosos | Camión 3/4 | 4 | 113 | 904 |
| Residuos domiciliarios | Camión 3/4 | 48 | 113 | 10.848 |

**Tabla 51.: ** Nivel de actividad correspondiente a distancia a recorrer por tránsito vehicular en caminos**

| Tipo Camino | Tipo vehículo | Nivel actividad | Unidad |
| --- | --- | --- | --- |
| Caminos Pavimentados<br>Ruta N-85 | Vehículo liviano | 75.600 | km |
| Caminos Pavimentados<br>Ruta N-85 | Camión 3/4 Mantención | 504 | km |
| Caminos Pavimentados<br>Ruta N-85 | Aljibe | 1.008 | km |
| Caminos Pavimentados<br>Ruta N-85 | Camión 3/4 - Residuos Peligrosos | 320 | km |
| Caminos Pavimentados<br>Ruta N-85 | Camión 3/4 - Residuos Domiciliarios | 3.840 | km |
| Caminos Pavimentados<br>Rutas 5 y 152 | Vehículo liviano | 406.800 | km |
| Caminos Pavimentados<br>Rutas 5 y 152 | Camión 3/4 Mantención | 2.712 | km |
| Caminos Pavimentados<br>Rutas 5 y 152 | Aljibe | 5.424 | km |
| Caminos Pavimentados<br>Rutas 5 y 152 | Camión 3/4 - Residuos Peligrosos | 904 | km |
| Caminos Pavimentados<br>Rutas 5 y 152 | Camión 3/4 - Residuos Domiciliarios | 10.848 | km |

**Tabla 52.: ** Nivel de actividad correspondiente a distancia a recorrer por tránsito vehicular en caminos**

| Tipo camino | Tipo vehículo | Nivel actividad | Unidad |
| --- | --- | --- | --- |
| Camino Pavimentados<br>Ruta 85 | Vehículo liviano | 75.600 | km |
| Camino Pavimentados<br>Ruta 85 | Camión 3/4 Mantención | 504 | km |
| Camino Pavimentados<br>Ruta 85 | Aljibe | 1.008 | km |
| Camino Pavimentados<br>Ruta 85 | Camión 3/4 - Residuos Peligrosos | 320 | km |
| Camino Pavimentados<br>Ruta 85 | Camión 3/4 - Residuos Domiciliarios | 3.840 | km |
| Camino Pavimentados<br>Ruta 5 y 152 | Vehículo liviano | 406.800 | km |
| Camino Pavimentados<br>Ruta 5 y 152 | Camión 3/4 Mantención | 2.712 | km |
| Camino Pavimentados<br>Ruta 5 y 152 | Aljibe | 5.424 | km |
| Camino Pavimentados<br>Ruta 5 y 152 | Camión 3/4 - Residuos Peligrosos | 904 | km |
| Camino Pavimentados<br>Ruta 5 y 152 | Camión 3/4 - Residuos Domiciliarios | 10.848 | km |
| Caminos No<br>Pavimentados | Vehículo liviano | 47.880 | km |
| Caminos No<br>Pavimentados | Camión 3/4 Mantención | 319 | km |
| Caminos No<br>Pavimentados | Aljibe | 638 | km |
| Caminos No<br>Pavimentados | Camión 3/4 - Residuos Peligrosos | 106 | km |
| Caminos No<br>Pavimentados | Camión 3/4 - Residuos Domiciliarios | 1.277 | km |

**Tabla 53.: ** Cantidad de maquinaria fuera de ruta y horas de operación del proyecto Parque Eólico**

| Maquinaria Construcción | Cantidad por día | Horas por día |
| --- | --- | --- |
| Grúa pluma | 1 | 8 |

**Tabla 54.: ** Nivel de actividad correspondiente a maquinaria fuera de ruta del proyecto Parque Eólico**

| Parte del Proyecto | Nivel actividad | Unidad |
| --- | --- | --- |
| Grúa pluma | 8 | h |

**Tabla 55.: ** Nivel de actividad correspondiente a funcionamiento de grupos electrógenos durante la fase**

| Equipo | Cantidad de equipos | Nivel actividad | Unidad |
| --- | --- | --- | --- |
| Grupo electrógenos de emergencia | 2 | 2.630,82 | kg comb |

**Tabla 56.: ** Emisiones de MP10 debido a las actividades de la fase de Construcción del Proyecto Parque Eólico Dañicalqui, Sectores Parque**

| Sector | Actividad | Col3 | Factor Emisión | Col5 | Eficiencia<br>Mitigación | Nivel de Actividad | Col8 | Col9 | Unidad | Emisión MP10 (t/año) | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Sector** | **Actividad** | **Actividad** | **Valor** | **Unidad** | **Unidad** | **Año 1** | **Año 2** | **Total** | **Total** | **Año 1** | **Año 2** | **Total** |
| **PE** | Excavaciones -<br>preparación de<br>terreno | Plataformas y caminos | 8,36E-01 | kg/h | 0% | 5.219 | 7.268 | 12.487 | h | 4,36 | 6,07 | 10,43 |
| **PE** | Excavaciones -<br>preparación de<br>terreno | Aerogeneradores | 8,36E-01 | kg/h | 0% | 755 | 1.052 | 1.807 | h | 0,63 | 0,88 | 1,51 |
| **PE** | Excavaciones -<br>preparación de<br>terreno | Puentes y obras de arte: Puente río<br>Dañicalqui | 8,36E-01 | kg/h | 0% | 11 | 15 | 27 | h | 0,01 | 0,01 | 0,02 |
| **PE** | Excavaciones -<br>preparación de<br>terreno | Puentes y obras de arte: Puente<br>estero Culenco | 8,36E-01 | kg/h | 0% | 1 | 2 | 4 | h | 0,00 | 0,00 | 0,00 |
| **PE** | Excavaciones -<br>preparación de<br>terreno | Puentes y obras de arte: Puente<br>Canales | 8,36E-01 | kg/h | 0% | 2 | 3 | 5 | h | 0,00 | 0,00 | 0,00 |
| **PE** | Excavaciones -<br>preparación de<br>terreno | Puentes y obras de arte: Obras de<br>Arte | 8,36E-01 | kg/h | 0% | 3 | 3 | 6 | h | 0,00 | 0,00 | 0,01 |
| **PE** | Excavaciones -<br>preparación de<br>terreno | Circuiros MT | 8,36E-01 | kg/h | 0% | 81 | 113 | 193 | h | 0,07 | 0,09 | 0,16 |
| **LT** | **LT** | Línea de Transmisión | 8,36E-01 | kg/h | 0% | 35 | 49 | 84 | h | 0,03 | 0,04 | 0,07 |
| **PE** | Carga | Plataformas y caminos | 3,13E-04 | kg/t | 0% | 252.098 | 351.023 | 603.121 | t | 0,08 | 0,11 | 0,19 |
| **PE** | Carga | Aerogeneradores | 3,13E-04 | kg/t | 0% | 36.486 | 50.804 | 87.290 | t | 0,01 | 0,02 | 0,03 |
| **PE** | Carga | Puentes y obras de arte: Puente río<br>Dañicalqui | 3,13E-04 | kg/t | 0% | 536 | 747 | 1.283 | t | 0,00 | 0,00 | 0,00 |
| **PE** | Carga | Puentes y obras de arte: Puente<br>estero Culenco | 3,13E-04 | kg/t | 0% | 71 | 98 | 169 | t | 0,00 | 0,00 | 0,00 |
| **PE** | Carga | Puentes y obras de arte: Puente<br>Canales | 3,13E-04 | kg/t | 0% | 94 | 131 | 225 | t | 0,00 | 0,00 | 0,00 |
| **PE** | Carga | Puentes y obras de arte: Obras de<br>Arte | 3,13E-04 | kg/t | 0% | 121 | 169 | 290 | t | 0,00 | 0,00 | 0,00 |
| **PE** | Carga | Circuiros MT | 3,13E-04 | kg/t | 0% | 3.904 | 5.436 | 9.340 | t | 0,00 | 0,00 | 0,00 |
| **PE** | Carga | Material de escarpe | 3,13E-04 | kg/t | 0% | 21.548 | 30.004 | 51.553 | t | 0,01 | 0,01 | 0,02 |
| **LT** | **LT** | Línea de Transmisión | 3,13E-04 | kg/t | 0% | 1.696 | 2.362 | 4.058 | t | 0,00 | 0,00 | 0,00 |
| **PE** | Descarga | Plataformas y caminos | 3,13E-04 | kg/t | 0% | 155.301 | 216.242 | 371.543 | t | 0,05 | 0,07 | 0,12 |
| **PE** | Descarga | Aerogeneradores | 3,13E-04 | kg/t | 0% | 9.861 | 13.731 | 23.592 | t | 0,00 | 0,00 | 0,01 |
| **PE** | Descarga | Puentes y obras de arte: Puente río<br>Dañicalqui | 3,13E-04 | kg/t | 0% | 578 | 806 | 1.384 | t | 0,00 | 0,00 | 0,00 |
| **PE** | Descarga | Puentes y obras de arte: Puente<br>estero Culenco | 3,13E-04 | kg/t | 0% | 53 | 74 | 128 | t | 0,00 | 0,00 | 0,00 |
| **PE** | Descarga | Puentes y obras de arte: Puente<br>Canales | 3,13E-04 | kg/t | 0% | 71 | 99 | 170 | t | 0,00 | 0,00 | 0,00 |
| **PE** | Descarga | Puentes y obras de arte: Obras de<br>Arte | 3,13E-04 | kg/t | 0% | 80 | 112 | 192 | t | 0,00 | 0,00 | 0,00 |
| **PE** | Descarga | Material de escarpe | 3,13E-04 | kg/t | 0% | 21.548 | 30.004 | 51.553 | t | 0,01 | 0,01 | 0,02 |

**Tabla 57.: ** Emisiones de MP2,5 debido a las actividades de la fase de Construcción del Proyecto Parque Eólico Dañicalqui, Sectores Parque**

| Sector | Actividad | Col3 | Factor Emisión | Col5 | Eficiencia<br>Mitigación | Nivel de Actividad | Col8 | Col9 | Col10 | Emisión MP2,5 (t/año) | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Sector** | **Actividad** | **Actividad** | **Valor** | **Unidad** | **Unidad** | **Año 1** | **Año 2** | **Total** | **Unidad** | **Año 1** | **Año 2** | **Total** |
| **PE** | Excavaciones -<br>preparación de<br>terreno | Plataformas y caminos | 4,03E-01 | kg/h | 0% | 5.219 | 7.268 | 12.487 | h | 2,10 | 2,93 | 5,03 |
| **PE** | Excavaciones -<br>preparación de<br>terreno | Aerogeneradores | 4,03E-01 | kg/h | 0% | 755 | 1.052 | 1.807 | h | 0,30 | 0,42 | 0,73 |
| **PE** | Excavaciones -<br>preparación de<br>terreno | Puentes y obras de arte: Puente río<br>Dañicalqui | 4,03E-01 | kg/h | 0% | 11 | 15 | 27 | h | 0,00 | 0,01 | 0,01 |
| **PE** | Excavaciones -<br>preparación de<br>terreno | Puentes y obras de arte: Puente estero<br>Culenco | 4,03E-01 | kg/h | 0% | 1 | 2 | 4 | h | 0,00 | 0,00 | 0,00 |
| **PE** | Excavaciones -<br>preparación de<br>terreno | Puentes y obras de arte: Puente<br>Canales | 4,03E-01 | kg/h | 0% | 2 | 3 | 5 | h | 0,00 | 0,00 | 0,00 |
| **PE** | Excavaciones -<br>preparación de<br>terreno | Puentes y obras de arte: Obras de Arte | 4,03E-01 | kg/h | 0% | 3 | 3 | 6 | h | 0,00 | 0,00 | 0,00 |
| **PE** | Excavaciones -<br>preparación de<br>terreno | Circuiros MT | 4,03E-01 | kg/h | 0% | 81 | 113 | 193 | h | 0,03 | 0,05 | 0,08 |
| **LT** | **LT** | Línea de Transmisión | 4,03E-01 | kg/h | 0% | 35 | 49 | 84 | h | 0,01 | 0,02 | 0,03 |
| **PE** | Carga | Plataformas y caminos | 4,73E-05 | kg/t | 0% | 252.098 | 351.023 | 603.121 | t | 0,01 | 0,02 | 0,03 |
| **PE** | Carga | Aerogeneradores | 4,73E-05 | kg/t | 0% | 36.486 | 50.804 | 87.290 | t | 0,00 | 0,00 | 0,00 |
| **PE** | Carga | Puentes y obras de arte: Puente río<br>Dañicalqui | 4,73E-05 | kg/t | 0% | 536 | 747 | 1.283 | t | 0,00 | 0,00 | 0,00 |
| **PE** | Carga | Puentes y obras de arte: Puente estero<br>Culenco | 4,73E-05 | kg/t | 0% | 71 | 98 | 169 | t | 0,00 | 0,00 | 0,00 |
| **PE** | Carga | Puentes y obras de arte: Puente<br>Canales | 4,73E-05 | kg/t | 0% | 94 | 131 | 225 | t | 0,00 | 0,00 | 0,00 |
| **PE** | Carga | Puentes y obras de arte: Obras de Arte | 4,73E-05 | kg/t | 0% | 121 | 169 | 290 | t | 0,00 | 0,00 | 0,00 |
| **PE** | Carga | Circuiros MT | 4,73E-05 | kg/t | 0% | 3.904 | 5.436 | 9.340 | t | 0,00 | 0,00 | 0,00 |

**Tabla 58.: ** Emisiones de MPS debido a las actividades de la fase de Construcción del Proyecto Parque Eólico Dañicalqui, Sectores Parque**

| Sector | Actividad | Col3 | Factor Emisión | Col5 | Eficiencia<br>Mitigación | Nivel de Actividad | Col8 | Col9 | Col10 | Emisión MPS (t/año) | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Sector** | **Actividad** | **Actividad** | **Valor** | **Unidad** | **Unidad** | **Año 1** | **Año 2** | **Total** | **Unidad** | **Año 1** | **Año 2** | **Total** |
| **PE** | Excavaciones -<br>preparación de<br>terreno | Plataformas y caminos | 3,83E+00 | kg/h | 0% | 5.219 | 7.268 | 12.487 | h | 20,01 | 27,86 | 47,87 |
| **PE** | Excavaciones -<br>preparación de<br>terreno | Aerogeneradores | 3,83E+00 | kg/h | 0% | 755 | 1.052 | 1.807 | h | 2,90 | 4,03 | 6,93 |
| **PE** | Excavaciones -<br>preparación de<br>terreno | Puentes y obras de arte: Puente río<br>Dañicalqui | 3,83E+00 | kg/h | 0% | 11 | 15 | 27 | h | 0,04 | 0,06 | 0,10 |
| **PE** | Excavaciones -<br>preparación de<br>terreno | Puentes y obras de arte: Puente<br>estero Culenco | 3,83E+00 | kg/h | 0% | 1 | 2 | 4 | h | 0,01 | 0,01 | 0,01 |
| **PE** | Excavaciones -<br>preparación de<br>terreno | Puentes y obras de arte: Puente<br>Canales | 3,83E+00 | kg/h | 0% | 2 | 3 | 5 | h | 0,01 | 0,01 | 0,02 |
| **PE** | Excavaciones -<br>preparación de<br>terreno | Puentes y obras de arte: Obras de<br>Arte | 3,83E+00 | kg/h | 0% | 3 | 3 | 6 | h | 0,01 | 0,01 | 0,02 |
| **PE** | Excavaciones -<br>preparación de<br>terreno | Circuiros MT | 3,83E+00 | kg/h | 0% | 81 | 113 | 193 | h | 0,31 | 0,43 | 0,74 |
| **LT** | **LT** | Línea de Transmisión | 3,83E+00 | kg/h | 0% | 35 | 49 | 84 | h | 0,13 | 0,19 | 0,32 |
| **PE** | Carga | Plataformas y caminos | 6,61E-04 | kg/t | 0% | 252.098 | 351.023 | 603.121 | t | 0,17 | 0,23 | 0,40 |
| **PE** | Carga | Aerogeneradores | 6,61E-04 | kg/t | 0% | 36.486 | 50.804 | 87.290 | t | 0,02 | 0,03 | 0,06 |
| **PE** | Carga | Puentes y obras de arte: Puente río<br>Dañicalqui | 6,61E-04 | kg/t | 0% | 536 | 747 | 1.283 | t | 0,00 | 0,00 | 0,00 |
| **PE** | Carga | Puentes y obras de arte: Puente<br>estero Culenco | 6,61E-04 | kg/t | 0% | 71 | 98 | 169 | t | 0,00 | 0,00 | 0,00 |
| **PE** | Carga | Puentes y obras de arte: Puente<br>Canales | 6,61E-04 | kg/t | 0% | 94 | 131 | 225 | t | 0,00 | 0,00 | 0,00 |
| **PE** | Carga | Puentes y obras de arte: Obras de<br>Arte | 6,61E-04 | kg/t | 0% | 121 | 169 | 290 | t | 0,00 | 0,00 | 0,00 |
| **PE** | Carga | Circuiros MT | 6,61E-04 | kg/t | 0% | 3.904 | 5.436 | 9.340 | t | 0,00 | 0,00 | 0,01 |
| **PE** | Carga | Material de escarpe | 6,61E-04 | kg/t | 0% | 21.548 | 30.004 | 51.553 | t | 0,01 | 0,02 | 0,03 |
| **LT** | **LT** | Línea de Transmisión | 6,61E-04 | kg/t | 0% | 1.696 | 2.362 | 4.058 | t | 0,00 | 0,00 | 0,00 |
| **PE** | Descarga | Plataformas y caminos | 6,61E-04 | kg/t | 0% | 155.301 | 216.242 | 371.543 | t | 0,10 | 0,14 | 0,25 |
| **PE** | Descarga | Aerogeneradores | 6,61E-04 | kg/t | 0% | 9.861 | 13.731 | 23.592 | t | 0,01 | 0,01 | 0,02 |
| **PE** | Descarga | Puentes y obras de arte: Puente río<br>Dañicalqui | 6,61E-04 | kg/t | 0% | 578 | 806 | 1.384 | t | 0,00 | 0,00 | 0,00 |
| **PE** | Descarga | Puentes y obras de arte: Puente<br>estero Culenco | 6,61E-04 | kg/t | 0% | 53 | 74 | 128 | t | 0,00 | 0,00 | 0,00 |
| **PE** | Descarga | Puentes y obras de arte: Puente<br>Canales | 6,61E-04 | kg/t | 0% | 71 | 99 | 170 | t | 0,00 | 0,00 | 0,00 |

**Tabla 59.: ** Emisiones de NOx debido a las actividades de la fase de Construcción del Proyecto Parque Eólico Dañicalqui, Sectores Parque**

| Sector | Actividad | Col3 | Factor Emisión | Col5 | Eficiencia<br>Mitigación | Nivel de Actividad | Col8 | Col9 | Col10 | Emisión NOx (t/año) | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Sector** | **Actividad** | **Actividad** | **Valor** | **Unidad** | **Unidad** | **Año 1** | **Año 2** | **Total** | **Unidad** | **Año 1** | **Año 2** | **Total** |
| **PE** | Maquinaria fuera de<br>ruta | Motoniveladora | 3,77E-01 | kg/h | 0% | 12.672 | 792 | 13.464 | h | 4,78 | 0,30 | 5,08 |
| **PE** | Maquinaria fuera de<br>ruta | Compactadora | 2,79E+00 | kg/h | 0% | 9.504 | 594 | 10.098 | h | 26,49 | 1,66 | 28,14 |
| **PE** | Maquinaria fuera de<br>ruta | Bulldozer | 6,39E-01 | kg/h | 0% | 15.840 | 990 | 16.830 | h | 10,12 | 0,63 | 10,76 |
| **PE** | Maquinaria fuera de<br>ruta | Retroexcavadora | 2,98E-01 | kg/h | 0% | 16.830 | 8.910 | 25.740 | h | 5,02 | 2,66 | 7,67 |
| **PE** | Maquinaria fuera de<br>ruta | Grúa de apoyo | 5,99E-01 | kg/h | 0% | 0 | 1.078 | 1.078 | h | 0,00 | 0,65 | 0,65 |
| **PE** | Maquinaria fuera de<br>ruta | Grúa principal | 1,81E+00 | kg/h | 0% | 0 | 924 | 924 | h | 0,00 | 1,67 | 1,67 |
| **LT** | Maquinaria fuera de<br>ruta | Motoniveladora | 3,77E-01 | kg/h | 0% | 3.168 | 7.128 | 10.296 | h | 1,19 | 2,69 | 3,88 |
| **LT** | Maquinaria fuera de<br>ruta | Compactadora | 2,79E+00 | kg/h | 0% | 2.376 | 5.346 | 7.722 | h | 6,62 | 14,90 | 21,52 |
| **LT** | Maquinaria fuera de<br>ruta | Bulldozer | 6,39E-01 | kg/h | 0% | 3.960 | 9.900 | 13.860 | h | 2,53 | 6,33 | 8,86 |
| **LT** | Maquinaria fuera de<br>ruta | Retroexcavadora | 2,98E-01 | kg/h | 0% | 3.960 | 9.900 | 13.860 | h | 1,18 | 2,95 | 4,13 |
| **LT** | Maquinaria fuera de<br>ruta | Grúa de apoyo | 5,99E-01 | kg/h | 0% | 0 | 616 | 616 | h | 0,00 | 0,37 | 0,37 |
| **LT** | Maquinaria fuera de<br>ruta | Grúa principal | 1,81E+00 | kg/h | 0% | 0 | 528 | 528 | h | 0,00 | 0,95 | 0,95 |
| **PE** | Combustión vehículos<br>Pavimentado | Camión rígido + 2 ejes | 7,56E-03 | kg/VKT | 0% | 1.907 | 4.790 | 6.697 | km | 0,01 | 0,04 | 0,05 |
| **PE** | Combustión vehículos<br>Pavimentado | Camión Semiremolque | 7,56E-03 | kg/VKT | 0% | 355.187 | 114.976 | 470.162 | km | 2,69 | 0,87 | 3,56 |
| **PE** | Combustión vehículos<br>Pavimentado | liviano | 8,59E-04 | kg/VKT | 0% | 136.745 | 139.469 | 276.214 | km | 0,12 | 0,12 | 0,24 |
| **PE** | Combustión vehículos<br>Pavimentado | Sobredimensionado | 1,11E-02 | kg/VKT | 0% | 0 | 1.589 | 1.589 | km | 0,00 | 0,02 | 0,02 |
| **PE** | Combustión vehículos<br>No Pavimentado | Camión rígido + 2 ejes | 9,63E-03 | kg/VKT | 0% | 18.430 | 20.019 | 38.448 | km | 0,18 | 0,19 | 0,37 |
| **PE** | Combustión vehículos<br>No Pavimentado | Camión Semiremolque | 9,63E-03 | kg/VKT | 0% | 238.513 | 76.547 | 315.060 | km | 2,30 | 0,74 | 3,03 |
| **PE** | Combustión vehículos<br>No Pavimentado | liviano | 9,56E-04 | kg/VKT | 0% | 73.770 | 75.262 | 149.032 | km | 0,07 | 0,07 | 0,14 |
| **PE** | Combustión vehículos<br>No Pavimentado | Sobredimensionado | 1,11E-02 | kg/VKT | 0% | 0 | 870 | 870 | km | 0,00 | 0,01 | 0,01 |
| **LT** | Combustión vehículos<br>Pavimentado | Camión rígido + 2 ejes | 7,56E-03 | kg/VKT | 0% | 0 | 0 | 0 | km | 0,00 | 0,00 | 0,00 |
| **LT** | Combustión vehículos<br>Pavimentado | Camión Semiremolque | 7,56E-03 | kg/VKT | 0% | 0 | 3.198 | 3.198 | km | 0,00 | 0,02 | 0,02 |
| **LT** | Combustión vehículos<br>Pavimentado | liviano | 8,59E-04 | kg/VKT | 0% | 0 | 0 | 0 | km | 0,00 | 0,00 | 0,00 |
| **LT** | Combustión vehículos<br>Pavimentado | Sobredimensionado | 1,11E-02 | kg/VKT | 0% | 0 | 0 | 0 | km | 0,00 | 0,00 | 0,00 |
| **LT** | Combustión vehículos<br>No Pavimentado | Camión rígido + 2 ejes | 9,63E-03 | kg/VKT | 0% | 0 | 0 | 0 | km | 0,00 | 0,00 | 0,00 |
| **LT** | Combustión vehículos<br>No Pavimentado | Camión Semiremolque | 9,63E-03 | kg/VKT | 0% | 0 | 605 | 605 | km | 0,00 | 0,01 | 0,01 |
| **LT** | Combustión vehículos<br>No Pavimentado | liviano | 9,56E-04 | kg/VKT | 0% | 0 | 0 | 0 | km | 0,00 | 0,00 | 0,00 |
| **LT** | Combustión vehículos<br>No Pavimentado | Sobredimensionado | 1,11E-02 | kg/VKT | 0% | 0 | 0 | 0 | km | 0,00 | 0,00 | 0,00 |
| **PE** | Combustión vehículos<br>Pavimentado Ruta 5-<br>182 | Camión rígido + 2 ejes | 7,56E-03 | kg/VKT | 0% | 9.492 | 792 | 13.464 | km | 0,07 | 0,01 | 0,10 |
| **PE** | Combustión vehículos<br>Pavimentado Ruta 5-<br>182 | Camión Semiremolque | 7,56E-03 | kg/VKT | 0% | 1.768.111 | 594 | 10.098 | km | 13,37 | 0,00 | 0,08 |
| **PE** | Combustión vehículos<br>Pavimentado Ruta 5-<br>182 | liviano | 8,59E-04 | kg/VKT | 0% | 680.712 | 990 | 16.830 | km | 0,58 | 0,00 | 0,01 |
| **PE** | Combustión vehículos<br>Pavimentado Ruta 5-<br>182 | Sobredimensionado | 1,11E-02 | kg/VKT | 0% | 0 | 8.910 | 25.740 | km | 0,00 | 0,10 | 0,29 |
| **LT** | **LT** | Camión Semiremolque | 7,56E-03 | kg/VKT | 0% | 0 | 1.078 | 1.078 | km | 0,00 | 0,01 | 0,01 |
| **PE** | Grupos electrógenos | Instalación de faenas | 8,65E-02 | kg/kg comb. | 0% | 104.180 | 104.180 | 208.361 | kg comb. | 9,01 | 9,01 | 18,02 |
| **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **86,33 ** | **46,96 ** | **119,63 ** |

**Tabla 60.: ** Emisiones de CO debido a las actividades de la fase de Construcción del Proyecto Parque Eólico Dañicalqui, Sectores Parque Eólico**

| Sector | Actividad | Col3 | Factor Emisión | Col5 | Eficiencia<br>Mitigación | Nivel de Actividad | Col8 | Col9 | Col10 | Emisión CO (t/año) | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Sector** | **Actividad** | **Actividad** | **Valor** | **Unidad** | **Unidad** | **Año 1** | **Año 2** | **Total** | **Unidad** | **Año 1** | **Año 2** | **Total** |
| **PE** | Maquinaria fuera de<br>ruta | Motoniveladora | 1,83E-01 | kg/h | 0% | 12.672 | 792 | 13.464 | h | 2,32 | 0,15 | 2,47 |
| **PE** | Maquinaria fuera de<br>ruta | Compactadora | 1,35E-01 | kg/h | 0% | 9.504 | 594 | 10.098 | h | 1,29 | 0,08 | 1,37 |
| **PE** | Maquinaria fuera de<br>ruta | Bulldozer | 3,11E-01 | kg/h | 0% | 15.840 | 990 | 16.830 | h | 4,92 | 0,31 | 5,23 |
| **PE** | Maquinaria fuera de<br>ruta | Retroexcavadora | 2,01E-01 | kg/h | 0% | 16.830 | 8.910 | 25.740 | h | 3,38 | 1,79 | 5,17 |
| **PE** | Maquinaria fuera de<br>ruta | Grúa de apoyo | 2,91E-01 | kg/h | 0% | 0 | 1.078 | 1.078 | h | 0,00 | 0,31 | 0,31 |
| **PE** | Maquinaria fuera de<br>ruta | Grúa principal | 8,78E-01 | kg/h | 0% | 0 | 924 | 924 | h | 0,00 | 0,81 | 0,81 |
| **LT** | Maquinaria fuera de<br>ruta | Motoniveladora | 1,83E-01 | kg/h | 0% | 3.168 | 7.128 | 10.296 | h | 0,58 | 1,31 | 1,89 |
| **LT** | Maquinaria fuera de<br>ruta | Compactadora | 1,35E-01 | kg/h | 0% | 2.376 | 5.346 | 7.722 | h | 0,32 | 0,72 | 1,05 |
| **LT** | Maquinaria fuera de<br>ruta | Bulldozer | 3,11E-01 | kg/h | 0% | 3.960 | 9.900 | 13.860 | h | 1,23 | 3,07 | 4,30 |
| **LT** | Maquinaria fuera de<br>ruta | Retroexcavadora | 2,01E-01 | kg/h | 0% | 3.960 | 9.900 | 13.860 | h | 0,80 | 1,99 | 2,78 |
| **LT** | Maquinaria fuera de<br>ruta | Grúa de apoyo | 2,91E-01 | kg/h | 0% | 0 | 616 | 616 | h | 0,00 | 0,18 | 0,18 |
| **LT** | Maquinaria fuera de<br>ruta | Grúa principal | 8,78E-01 | kg/h | 0% | 0 | 528 | 528 | h | 0,00 | 0,46 | 0,46 |
| **PE** | Combustión vehículos<br>Pavimentado | Camión rígido + 2 ejes | 1,30E-03 | kg/VKT | 0% | 1.907 | 4.790 | 6.697 | km | 0,00 | 0,01 | 0,01 |
| **PE** | Combustión vehículos<br>Pavimentado | Camión Semiremolque | 1,30E-03 | kg/VKT | 0% | 355.187 | 114.976 | 470.162 | km | 0,46 | 0,15 | 0,61 |
| **PE** | Combustión vehículos<br>Pavimentado | liviano | 3,47E-04 | kg/VKT | 0% | 136.745 | 139.469 | 276.214 | km | 0,05 | 0,05 | 0,10 |
| **PE** | Combustión vehículos<br>Pavimentado | Sobredimensionado | 1,99E-03 | kg/VKT | 0% | 0 | 1.589 | 1.589 | km | 0,00 | 0,00 | 0,00 |
| **PE** | Combustión vehículos<br>No Pavimentado | Camión rígido + 2 ejes | 1,67E-03 | kg/VKT | 0% | 18.430 | 20.019 | 38.448 | km | 0,03 | 0,03 | 0,06 |
| **PE** | Combustión vehículos<br>No Pavimentado | Camión Semiremolque | 1,67E-03 | kg/VKT | 0% | 238.513 | 76.547 | 315.060 | km | 0,40 | 0,13 | 0,53 |
| **PE** | Combustión vehículos<br>No Pavimentado | liviano | 3,22E-04 | kg/VKT | 0% | 73.770 | 75.262 | 149.032 | km | 0,02 | 0,02 | 0,05 |
| **PE** | Combustión vehículos<br>No Pavimentado | Sobredimensionado | 1,99E-03 | kg/VKT | 0% | 0 | 870 | 870 | km | 0,00 | 0,00 | 0,00 |
| **LT** | Combustión vehículos<br>Pavimentado | Camión rígido + 2 ejes | 1,30E-03 | kg/VKT | 0% | 0 | 0 | 0 | km | 0,00 | 0,00 | 0,00 |
| **LT** | Combustión vehículos<br>Pavimentado | Camión Semiremolque | 1,30E-03 | kg/VKT | 0% | 0 | 3.198 | 3.198 | km | 0,00 | 0,00 | 0,00 |
| **LT** | Combustión vehículos<br>Pavimentado | liviano | 3,47E-04 | kg/VKT | 0% | 0 | 0 | 0 | km | 0,00 | 0,00 | 0,00 |
| **LT** | Combustión vehículos<br>Pavimentado | Sobredimensionado | 1,99E-03 | kg/VKT | 0% | 0 | 0 | 0 | km | 0,00 | 0,00 | 0,00 |
| **LT** | Combustión vehículos<br>No Pavimentado | Camión rígido + 2 ejes | 1,67E-03 | kg/VKT | 0% | 0 | 0 | 0 | km | 0,00 | 0,00 | 0,00 |
| **LT** | Combustión vehículos<br>No Pavimentado | Camión Semiremolque | 1,67E-03 | kg/VKT | 0% | 0 | 605 | 605 | km | 0,00 | 0,00 | 0,00 |
| **LT** | Combustión vehículos<br>No Pavimentado | liviano | 3,22E-04 | kg/VKT | 0% | 0 | 0 | 0 | km | 0,00 | 0,00 | 0,00 |
| **LT** | Combustión vehículos<br>No Pavimentado | Sobredimensionado | 1,99E-03 | kg/VKT | 0% | 0 | 0 | 0 | km | 0,00 | 0,00 | 0,00 |
| **PE** | Combustión vehículos<br>Pavimentado Ruta 5-<br>182 | Camión rígido + 2 ejes | 1,30E-03 | kg/VKT | 0% | 9.492 | 792 | 13.464 | km | 0,01 | 0,00 | 0,02 |
| **PE** | Combustión vehículos<br>Pavimentado Ruta 5-<br>182 | Camión Semiremolque | 1,30E-03 | kg/VKT | 0% | 1.768.111 | 594 | 10.098 | km | 2,30 | 0,00 | 0,01 |
| **PE** | Combustión vehículos<br>Pavimentado Ruta 5-<br>182 | liviano | 3,47E-04 | kg/VKT | 0% | 680.712 | 990 | 16.830 | km | 0,24 | 0,00 | 0,01 |
| **PE** | Combustión vehículos<br>Pavimentado Ruta 5-<br>182 | Sobredimensionado | 1,99E-03 | kg/VKT | 0% | 0 | 8.910 | 25.740 | km | 0,00 | 0,02 | 0,05 |
| **LT** | **LT** | Camión Semiremolque | 1,30E-03 | kg/VKT | 0% | 0 | 1.078 | 1.078 | km | 0,00 | 0,00 | 0,00 |
| **PE** | Grupos electrógenos | Instalación de faenas | 1,86E-02 | kg/kg comb. | 0% | 104.180 | 104.180 | 208.361 | kg comb. | 1,94 | 1,94 | 3,88 |
| **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **20,29 ** | **13,54 ** | **31,35 ** |

**Tabla 61.: ** Emisiones de SOx debido a las actividades de la fase de Construcción del Proyecto Parque Eólico Dañicalqui, Sectores Parque**

| Sector | Actividad | Col3 | Factor Emisión | Col5 | Eficiencia<br>Mitigación | Nivel de Actividad | Col8 | Col9 | Col10 | Emisión SOx (t/año) | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Sector** | **Actividad** | **Actividad** | **Valor** | **Unidad** | **Unidad** | **Año 1** | **Año 2** | **Total** | **Unidad** | **Año 1** | **Año 2** | **Total** |
| **PE** | Maquinaria fuera de<br>ruta | Motoniveladora | 5,85E-04 | kg/h | 0% | 12.672 | 792 | 13.464 | h | 0,01 | 0,00 | 0,01 |
| **PE** | Maquinaria fuera de<br>ruta | Compactadora | 6,26E-03 | kg/h | 0% | 9.504 | 594 | 10.098 | h | 0,06 | 0,00 | 0,06 |
| **PE** | Maquinaria fuera de<br>ruta | Bulldozer | 9,66E-04 | kg/h | 0% | 15.840 | 990 | 16.830 | h | 0,02 | 0,00 | 0,02 |
| **PE** | Maquinaria fuera de<br>ruta | Retroexcavadora | 4,43E-04 | kg/h | 0% | 16.830 | 8.910 | 25.740 | h | 0,01 | 0,00 | 0,01 |
| **PE** | Maquinaria fuera de<br>ruta | Grúa de apoyo | 9,06E-04 | kg/h | 0% | 0 | 1.078 | 1.078 | h | 0,00 | 0,00 | 0,00 |
| **PE** | Maquinaria fuera de<br>ruta | Grúa principal | 2,73E-03 | kg/h | 0% | 0 | 924 | 924 | h | 0,00 | 0,00 | 0,00 |
| **LT** | Maquinaria fuera de<br>ruta | Motoniveladora | 5,85E-04 | kg/h | 0% | 3.168 | 7.128 | 10.296 | h | 0,00 | 0,00 | 0,01 |
| **LT** | Maquinaria fuera de<br>ruta | Compactadora | 6,26E-03 | kg/h | 0% | 2.376 | 5.346 | 7.722 | h | 0,01 | 0,03 | 0,05 |
| **LT** | Maquinaria fuera de<br>ruta | Bulldozer | 9,66E-04 | kg/h | 0% | 3.960 | 9.900 | 13.860 | h | 0,00 | 0,01 | 0,01 |
| **LT** | Maquinaria fuera de<br>ruta | Retroexcavadora | 4,43E-04 | kg/h | 0% | 3.960 | 9.900 | 13.860 | h | 0,00 | 0,00 | 0,01 |
| **LT** | Maquinaria fuera de<br>ruta | Grúa de apoyo | 9,06E-04 | kg/h | 0% | 0 | 616 | 616 | h | 0,00 | 0,00 | 0,00 |
| **LT** | Maquinaria fuera de<br>ruta | Grúa principal | 2,73E-03 | kg/h | 0% | 0 | 528 | 528 | h | 0,00 | 0,00 | 0,00 |
| **PE** | Combustión vehículos<br>Pavimentado | Camión rígido + 2 ejes | 2,06E-05 | kg/VKT | 0% | 1.907 | 4.790 | 6.697 | km | 0,00 | 0,00 | 0,00 |
| **PE** | Combustión vehículos<br>Pavimentado | Camión Semiremolque | 2,06E-05 | kg/VKT | 0% | 355.187 | 114.976 | 470.162 | km | 0,01 | 0,00 | 0,01 |
| **PE** | Combustión vehículos<br>Pavimentado | liviano | 6,37E-06 | kg/VKT | 0% | 136.745 | 139.469 | 276.214 | km | 0,00 | 0,00 | 0,00 |
| **PE** | Combustión vehículos<br>Pavimentado | Sobredimensionado | 3,08E-05 | kg/VKT | 0% | 0 | 1.589 | 1.589 | km | 0,00 | 0,00 | 0,00 |
| **PE** | Combustión vehículos<br>No Pavimentado | Camión rígido + 2 ejes | 2,66E-05 | kg/VKT | 0% | 18.430 | 20.019 | 38.448 | km | 0,00 | 0,00 | 0,00 |
| **PE** | Combustión vehículos<br>No Pavimentado | Camión Semiremolque | 2,66E-05 | kg/VKT | 0% | 238.513 | 76.547 | 315.060 | km | 0,01 | 0,00 | 0,01 |
| **PE** | Combustión vehículos<br>No Pavimentado | liviano | 6,89E-06 | kg/VKT | 0% | 73.770 | 75.262 | 149.032 | km | 0,00 | 0,00 | 0,00 |
| **PE** | Combustión vehículos<br>No Pavimentado | Sobredimensionado | 3,08E-05 | kg/VKT | 0% | 0 | 870 | 870 | km | 0,00 | 0,00 | 0,00 |
| **LT** | Combustión vehículos<br>Pavimentado | Camión rígido + 2 ejes | 2,06E-05 | kg/VKT | 0% | 0 | 0 | 0 | km | 0,00 | 0,00 | 0,00 |
| **LT** | Combustión vehículos<br>Pavimentado | Camión Semiremolque | 2,06E-05 | kg/VKT | 0% | 0 | 3.198 | 3.198 | km | 0,00 | 0,00 | 0,00 |
| **LT** | Combustión vehículos<br>Pavimentado | liviano | 6,37E-06 | kg/VKT | 0% | 0 | 0 | 0 | km | 0,00 | 0,00 | 0,00 |
| **LT** | Combustión vehículos<br>Pavimentado | Sobredimensionado | 3,08E-05 | kg/VKT | 0% | 0 | 0 | 0 | km | 0,00 | 0,00 | 0,00 |
| **LT** | Combustión vehículos<br>No Pavimentado | Camión rígido + 2 ejes | 2,66E-05 | kg/VKT | 0% | 0 | 0 | 0 | km | 0,00 | 0,00 | 0,00 |
| **LT** | Combustión vehículos<br>No Pavimentado | Camión Semiremolque | 2,66E-05 | kg/VKT | 0% | 0 | 605 | 605 | km | 0,00 | 0,00 | 0,00 |
| **LT** | Combustión vehículos<br>No Pavimentado | liviano | 6,89E-06 | kg/VKT | 0% | 0 | 0 | 0 | km | 0,00 | 0,00 | 0,00 |
| **LT** | Combustión vehículos<br>No Pavimentado | Sobredimensionado | 3,08E-05 | kg/VKT | 0% | 0 | 0 | 0 | km | 0,00 | 0,00 | 0,00 |
| **PE** | Combustión vehículos<br>Pavimentado Ruta 5-<br>182 | Camión rígido + 2 ejes | 2,06E-05 | kg/VKT | 0% | 9.492 | 792 | 13.464 | km | 0,00 | 0,00 | 0,00 |
| **PE** | Combustión vehículos<br>Pavimentado Ruta 5-<br>182 | Camión Semiremolque | 2,06E-05 | kg/VKT | 0% | 1.768.111 | 594 | 10.098 | km | 0,04 | 0,00 | 0,00 |
| **PE** | Combustión vehículos<br>Pavimentado Ruta 5-<br>182 | liviano | 6,37E-06 | kg/VKT | 0% | 680.712 | 990 | 16.830 | km | 0,00 | 0,00 | 0,00 |
| **PE** | Combustión vehículos<br>Pavimentado Ruta 5-<br>182 | Sobredimensionado | 3,08E-05 | kg/VKT | 0% | 0 | 8.910 | 25.740 | km | 0,00 | 0,00 | 0,00 |
| **LT** | **LT** | Camión Semiremolque | 2,06E-05 | kg/VKT | 0% | 0 | 1.078 | 1.078 | km | 0,00 | 0,00 | 0,00 |
| **PE** | Grupos electrógenos | Instalación de faenas | 5,69E-03 | kg/kg comb. | 0% | 104.180 | 104.180 | 208.361 | kg comb. | 0,59 | 0,59 | 1,18 |
| **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **0,76 ** | **0,67 ** | **1,39 ** |

**Tabla 62.: ** Emisiones de HC debido a las actividades de la fase de Construcción del Proyecto Parque Eólico Dañicalqui, Sectores Parque Eólico**

| Sector | Actividad | Col3 | Factor Emisión | Col5 | Eficiencia<br>Mitigación | Nivel de Actividad | Col8 | Col9 | Col10 | Emisión HC (t/año) | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Sector** | **Actividad** | **Actividad** | **Valor** | **Unidad** | **Unidad** | **Año 1** | **Año 2** | **Total** | **Unidad** | **Año 1** | **Año 2** | **Total** |
| **PE** | Maquinaria fuera de<br>ruta | Motoniveladora | 2,43E-02 | kg/h | 0% | 12.672 | 792 | 13.464 | h | 0,31 | 0,02 | 0,33 |
| **PE** | Maquinaria fuera de<br>ruta | Compactadora | 8,91E-02 | kg/h | 0% | 9.504 | 594 | 10.098 | h | 0,85 | 0,05 | 0,90 |
| **PE** | Maquinaria fuera de<br>ruta | Bulldozer | 8,25E-02 | kg/h | 0% | 15.840 | 990 | 16.830 | h | 1,31 | 0,08 | 1,39 |
| **PE** | Maquinaria fuera de<br>ruta | Retroexcavadora | 2,43E-02 | kg/h | 0% | 16.830 | 8.910 | 25.740 | h | 0,41 | 0,22 | 0,62 |
| **PE** | Maquinaria fuera de<br>ruta | Grúa de apoyo | 3,87E-02 | kg/h | 0% | 0 | 1.078 | 1.078 | h | 0,00 | 0,04 | 0,04 |
| **PE** | Maquinaria fuera de<br>ruta | Grúa principal | 1,17E-01 | kg/h | 0% | 0 | 924 | 924 | h | 0,00 | 0,11 | 0,11 |
| **LT** | Maquinaria fuera de<br>ruta | Motoniveladora | 2,43E-02 | kg/h | 0% | 3.168 | 7.128 | 10.296 | h | 0,08 | 0,17 | 0,25 |
| **LT** | Maquinaria fuera de<br>ruta | Compactadora | 8,91E-02 | kg/h | 0% | 2.376 | 5.346 | 7.722 | h | 0,21 | 0,48 | 0,69 |
| **LT** | Maquinaria fuera de<br>ruta | Bulldozer | 8,25E-02 | kg/h | 0% | 3.960 | 9.900 | 13.860 | h | 0,33 | 0,82 | 1,14 |
| **LT** | Maquinaria fuera de<br>ruta | Retroexcavadora | 2,43E-02 | kg/h | 0% | 3.960 | 9.900 | 13.860 | h | 0,10 | 0,24 | 0,34 |
| **LT** | Maquinaria fuera de<br>ruta | Grúa de apoyo | 3,87E-02 | kg/h | 0% | 0 | 616 | 616 | h | 0,00 | 0,02 | 0,02 |
| **LT** | Maquinaria fuera de<br>ruta | Grúa principal | 1,17E-01 | kg/h | 0% | 0 | 528 | 528 | h | 0,00 | 0,06 | 0,06 |
| **PE** | Combustión vehículos<br>Pavimentado | Camión rígido + 2 ejes | 2,77E-01 | kg/VKT | 0% | 1.907 | 4.790 | 6.697 | km | 0,53 | 1,33 | 1,85 |
| **PE** | Combustión vehículos<br>Pavimentado | Camión Semiremolque | 2,77E-01 | kg/VKT | 0% | 355.187 | 114.976 | 470.162 | km | 98,31 | 31,82 | 130,13 |
| **PE** | Combustión vehículos<br>Pavimentado | liviano | 6,06E-02 | kg/VKT | 0% | 136.745 | 139.469 | 276.214 | km | 8,29 | 8,46 | 16,75 |
| **PE** | Combustión vehículos<br>Pavimentado | Sobredimensionado | 6,19E-01 | kg/VKT | 0% | 0 | 1.589 | 1.589 | km | 0,00 | 0,98 | 0,98 |
| **PE** | Combustión vehículos<br>No Pavimentado | Camión rígido + 2 ejes | 4,88E-01 | kg/VKT | 0% | 18.430 | 20.019 | 38.448 | km | 8,99 | 9,77 | 18,76 |
| **PE** | Combustión vehículos<br>No Pavimentado | Camión Semiremolque | 4,88E-01 | kg/VKT | 0% | 238.513 | 76.547 | 315.060 | km | 116,37 | 37,35 | 153,71 |
| **PE** | Combustión vehículos<br>No Pavimentado | liviano | 8,05E-02 | kg/VKT | 0% | 73.770 | 75.262 | 149.032 | km | 5,94 | 6,06 | 11,99 |
| **PE** | Combustión vehículos<br>No Pavimentado | Sobredimensionado | 6,19E-01 | kg/VKT | 0% | 0 | 870 | 870 | km | 0,00 | 0,54 | 0,54 |
| **LT** | Combustión vehículos<br>Pavimentado | Camión rígido + 2 ejes | 2,77E-01 | kg/VKT | 0% | 0 | 0 | 0 | km | 0,00 | 0,00 | 0,00 |
| **LT** | Combustión vehículos<br>Pavimentado | Camión Semiremolque | 2,77E-01 | kg/VKT | 0% | 0 | 3.198 | 3.198 | km | 0,00 | 0,89 | 0,89 |
| **LT** | Combustión vehículos<br>Pavimentado | liviano | 6,06E-02 | kg/VKT | 0% | 0 | 0 | 0 | km | 0,00 | 0,00 | 0,00 |
| **LT** | Combustión vehículos<br>Pavimentado | Sobredimensionado | 6,19E-01 | kg/VKT | 0% | 0 | 0 | 0 | km | 0,00 | 0,00 | 0,00 |
| **LT** | Combustión vehículos<br>No Pavimentado | Camión rígido + 2 ejes | 4,88E-01 | kg/VKT | 0% | 0 | 0 | 0 | km | 0,00 | 0,00 | 0,00 |
| **LT** | Combustión vehículos<br>No Pavimentado | Camión Semiremolque | 4,88E-01 | kg/VKT | 0% | 0 | 605 | 605 | km | 0,00 | 0,29 | 0,29 |
| **LT** | Combustión vehículos<br>No Pavimentado | liviano | 8,05E-02 | kg/VKT | 0% | 0 | 0 | 0 | km | 0,00 | 0,00 | 0,00 |
| **LT** | Combustión vehículos<br>No Pavimentado | Sobredimensionado | 6,19E-01 | kg/VKT | 0% | 0 | 0 | 0 | km | 0,00 | 0,00 | 0,00 |
| **PE** | Combustión vehículos<br>Pavimentado Ruta 5-<br>182 | Camión rígido + 2 ejes | 2,77E-01 | kg/VKT | 0% | 9.492 | 792 | 13.464 | km | 2,63 | 0,22 | 3,73 |
| **PE** | Combustión vehículos<br>Pavimentado Ruta 5-<br>182 | Camión Semiremolque | 2,77E-01 | kg/VKT | 0% | 1.768.111 | 594 | 10.098 | km | 489,39 | 0,16 | 2,79 |
| **PE** | Combustión vehículos<br>Pavimentado Ruta 5-<br>182 | liviano | 6,06E-02 | kg/VKT | 0% | 680.712 | 990 | 16.830 | km | 41,28 | 0,06 | 1,02 |
| **PE** | Combustión vehículos<br>Pavimentado Ruta 5-<br>182 | Sobredimensionado | 6,19E-01 | kg/VKT | 0% | 0 | 8.910 | 25.740 | km | 0,00 | 5,52 | 15,94 |
| **LT** | **LT** | Camión Semiremolque | 2,77E-01 | kg/VKT | 0% | 0 | 1.078 | 1.078 | km | 0,00 | 0,30 | 0,30 |
| **PE** | Grupos electrógenos | Instalación de faenas | 7,06E-03 | kg/kg comb. | 0% | 104.180 | 104.180 | 208.361 | kg comb. | 0,74 | 0,74 | 1,47 |
| **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **776,03 ** | **106,79 ** | **367,05 ** |

**Tabla 63.: ** Emisiones de MP10 debido a las actividades de la fase de Operación del Proyecto Parque Eólico Dañicalqui, Sectores Parque**

| Actividad | Col2 | Factor Emisión | Col4 | Eficiencia<br>Mitigación | Nivel de Actividad | Col7 | Emisión MP10<br>(t/año) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Actividad** | **Actividad** | **Valor** | **Unidad** | **Unidad** | **Cantidad** | **Unidad** | **Unidad** |
| Resuspensión caminos<br>Pavimentados Ruta 85 | Vehículo liviano | 3,84E-04 | kg/VKT | 0% | 75.600 | km/año | 0,03 |
| Resuspensión caminos<br>Pavimentados Ruta 85 | Camión 3/4 Mantención | 6,02E-04 | kg/VKT | 0% | 504 | km/año | 0,00 |
| Resuspensión caminos<br>Pavimentados Ruta 85 | Aljibe | 3,53E-03 | kg/VKT | 0% | 1.008 | km/año | 0,00 |
| Resuspensión caminos<br>Pavimentados Ruta 85 | Camión 3/4 - Residuos Peligrosos | 6,02E-04 | kg/VKT | 0% | 320 | km/año | 0,00 |
| Resuspensión caminos<br>Pavimentados Ruta 85 | Camión 3/4 - Residuos Domiciliarios | 6,02E-04 | kg/VKT | 0% | 3.840 | km/año | 0,00 |
| Resuspensión caminos<br>Pavimentados Ruta 5-152 | Vehículo liviano | 3,84E-04 | kg/VKT | 0% | 406.800 | km/año | 0,16 |
| Resuspensión caminos<br>Pavimentados Ruta 5-152 | Camión 3/4 Mantención | 6,02E-04 | kg/VKT | 0% | 2.712 | km/año | 0,00 |
| Resuspensión caminos<br>Pavimentados Ruta 5-152 | Aljibe | 3,53E-03 | kg/VKT | 0% | 5.424 | km/año | 0,02 |
| Resuspensión caminos<br>Pavimentados Ruta 5-152 | Camión 3/4 - Residuos Peligrosos | 6,02E-04 | kg/VKT | 0% | 904 | km/año | 0,00 |
| Resuspensión caminos<br>Pavimentados Ruta 5-152 | Camión 3/4 - Residuos Domiciliarios | 6,02E-04 | kg/VKT | 0% | 10.848 | km/año | 0,01 |
| Resuspensión caminos No<br>Pavimentados - Externo | Vehículo liviano | 1,51E-01 | kg/VKT | 0% | 26.280 | km/año | 3,96 |
| Resuspensión caminos No<br>Pavimentados - Externo | Camión 3/4 Mantención | 1,84E-01 | kg/VKT | 0% | 175 | km/año | 0,03 |
| Resuspensión caminos No<br>Pavimentados - Externo | Aljibe | 4,01E-01 | kg/VKT | 0% | 350 | km/año | 0,14 |
| Resuspensión caminos No<br>Pavimentados - Externo | Camión 3/4 - Residuos Peligrosos | 1,84E-01 | kg/VKT | 0% | 58 | km/año | 0,01 |
| Resuspensión caminos No<br>Pavimentados - Externo | Camión 3/4 - Residuos Domiciliarios | 1,84E-01 | kg/VKT | 0% | 701 | km/año | 0,13 |
| Resuspensión caminos No<br>Pavimentados - Interno | Vehículo liviano | 1,51E-01 | kg/VKT | 0% | 21.600 | km/año | 3,25 |
| Resuspensión caminos No<br>Pavimentados - Interno | Camión 3/4 Mantención | 1,84E-01 | kg/VKT | 0% | 144 | km/año | 0,03 |
| Resuspensión caminos No<br>Pavimentados - Interno | Aljibe | 4,01E-01 | kg/VKT | 0% | 288 | km/año | 0,12 |
| Resuspensión caminos No<br>Pavimentados - Interno | Camión 3/4 - Residuos Peligrosos | 1,84E-01 | kg/VKT | 0% | 48 | km/año | 0,01 |
| Resuspensión caminos No<br>Pavimentados - Interno | Camión 3/4 - Residuos Domiciliarios | 1,84E-01 | kg/VKT | 0% | 576 | km/año | 0,11 |
| Combustión vehículos<br>Pavimentado Ruta 85 | Vehículo liviano | 6,06E-05 | kg/VKT | 0% | 75.600 | km/año | 0,00 |
| Combustión vehículos<br>Pavimentado Ruta 85 | Camión 3/4 Mantención | 8,82E-04 | kg/VKT | 0% | 504 | km/año | 0,00 |
| Combustión vehículos<br>Pavimentado Ruta 85 | Aljibe | 8,82E-04 | kg/VKT | 0% | 1.008 | km/año | 0,00 |
| Combustión vehículos<br>Pavimentado Ruta 85 | Camión 3/4 - Residuos Peligrosos | 8,82E-04 | kg/VKT | 0% | 320 | km/año | 0,00 |
| Combustión vehículos<br>Pavimentado Ruta 85 | Camión 3/4 - Residuos Domiciliarios | 8,82E-04 | kg/VKT | 0% | 3.840 | km/año | 0,00 |
| Combustión vehículos<br>Pavimentado Ruta 5-152 | Vehículo liviano | 6,06E-05 | kg/VKT | 0% | 406.800 | km/año | 0,02 |
| Combustión vehículos<br>Pavimentado Ruta 5-152 | Camión 3/4 Mantención | 8,82E-04 | kg/VKT | 0% | 2.712 | km/año | 0,00 |
| Combustión vehículos<br>Pavimentado Ruta 5-152 | Aljibe | 8,82E-04 | kg/VKT | 0% | 5.424 | km/año | 0,00 |
| Combustión vehículos<br>Pavimentado Ruta 5-152 | Camión 3/4 - Residuos Peligrosos | 8,82E-04 | kg/VKT | 0% | 904 | km/año | 0,00 |
| Combustión vehículos<br>Pavimentado Ruta 5-152 | Camión 3/4 - Residuos Domiciliarios | 8,82E-04 | kg/VKT | 0% | 10.848 | km/año | 0,01 |
| Combustión vehículos No<br>Pavimentadas | Vehículo liviano | 4,68E-05 | kg/VKT | 0% | 47.880 | km/año | 0,00 |
| Combustión vehículos No<br>Pavimentadas | Camión 3/4 Mantención | 7,02E-04 | kg/VKT | 0% | 47.880 | km/año | 0,03 |
| Combustión vehículos No<br>Pavimentadas | Aljibe | 7,02E-04 | kg/VKT | 0% | 319 | km/año | 0,00 |
| Combustión vehículos No<br>Pavimentadas | Camión 3/4 - Residuos Peligrosos | 7,02E-04 | kg/VKT | 0% | 638 | km/año | 0,00 |
| Combustión vehículos No<br>Pavimentadas | Camión 3/4 - Residuos Domiciliarios | 7,02E-04 | kg/VKT | 0% | 106 | km/año | 0,00 |
| Maquinaria fuera de ruta | Grúa pluma | 1,84E-02 | kg/h | 0% | 8 | h | 0,00 |
| Grupos electrógenos | Emergencia | 6,08E-03 | kg/kg comb. | 0% | 2.631 | kg comb. | 0,02 |
| **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **8,11 ** |

**Tabla 64.: ** Emisiones de MP2,5 debido a las actividades de la fase de Operación del Proyecto Parque Eólico Dañicalqui, Sectores Parque**

| Actividad | Col2 | Factor Emisión | Col4 | Eficiencia<br>Mitigación | Nivel de Actividad | Col7 | Emisión MP2,5<br>(t/año) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Actividad** | **Actividad** | **Valor** | **Unidad** | **Unidad** | **Cantidad** | **Unidad** | **Unidad** |
| Resuspensión caminos<br>Pavimentados Ruta 85 | Vehículo liviano | 9,30E-05 | kg/VKT | 0% | 75.600 | km/año | 0,01 |
| Resuspensión caminos<br>Pavimentados Ruta 85 | Camión 3/4 Mantención | 1,46E-04 | kg/VKT | 0% | 504 | km/año | 0,00 |
| Resuspensión caminos<br>Pavimentados Ruta 85 | Aljibe | 8,55E-04 | kg/VKT | 0% | 1.008 | km/año | 0,00 |
| Resuspensión caminos<br>Pavimentados Ruta 85 | Camión 3/4 - Residuos Peligrosos | 1,46E-04 | kg/VKT | 0% | 320 | km/año | 0,00 |
| Resuspensión caminos<br>Pavimentados Ruta 85 | Camión 3/4 - Residuos Domiciliarios | 1,46E-04 | kg/VKT | 0% | 3.840 | km/año | 0,00 |
| Resuspensión caminos<br>Pavimentados Ruta 5-152 | Vehículo liviano | 9,30E-05 | kg/VKT | 0% | 406.800 | km/año | 0,04 |
| Resuspensión caminos<br>Pavimentados Ruta 5-152 | Camión 3/4 Mantención | 1,46E-04 | kg/VKT | 0% | 2.712 | km/año | 0,00 |
| Resuspensión caminos<br>Pavimentados Ruta 5-152 | Aljibe | 8,55E-04 | kg/VKT | 0% | 5.424 | km/año | 0,00 |
| Resuspensión caminos<br>Pavimentados Ruta 5-152 | Camión 3/4 - Residuos Peligrosos | 1,46E-04 | kg/VKT | 0% | 904 | km/año | 0,00 |
| Resuspensión caminos<br>Pavimentados Ruta 5-152 | Camión 3/4 - Residuos Domiciliarios | 1,46E-04 | kg/VKT | 0% | 10.848 | km/año | 0,00 |
| Resuspensión caminos No<br>Pavimentados - Externo | Vehículo liviano | 1,51E-02 | kg/VKT | 0% | 26.280 | km/año | 0,40 |
| Resuspensión caminos No<br>Pavimentados - Externo | Camión 3/4 Mantención | 1,84E-02 | kg/VKT | 0% | 175 | km/año | 0,00 |
| Resuspensión caminos No<br>Pavimentados - Externo | Aljibe | 4,01E-02 | kg/VKT | 0% | 350 | km/año | 0,01 |
| Resuspensión caminos No<br>Pavimentados - Externo | Camión 3/4 - Residuos Peligrosos | 1,84E-02 | kg/VKT | 0% | 58 | km/año | 0,00 |
| Resuspensión caminos No<br>Pavimentados - Externo | Camión 3/4 - Residuos Domiciliarios | 1,84E-02 | kg/VKT | 0% | 701 | km/año | 0,01 |
| Resuspensión caminos No<br>Pavimentados - Interno | Vehículo liviano | 1,51E-02 | kg/VKT | 0% | 21.600 | km/año | 0,33 |
| Resuspensión caminos No<br>Pavimentados - Interno | Camión 3/4 Mantención | 1,84E-02 | kg/VKT | 0% | 144 | km/año | 0,00 |
| Resuspensión caminos No<br>Pavimentados - Interno | Aljibe | 4,01E-02 | kg/VKT | 0% | 288 | km/año | 0,01 |
| Resuspensión caminos No<br>Pavimentados - Interno | Camión 3/4 - Residuos Peligrosos | 1,84E-02 | kg/VKT | 0% | 48 | km/año | 0,00 |
| Resuspensión caminos No<br>Pavimentados - Interno | Camión 3/4 - Residuos Domiciliarios | 1,84E-02 | kg/VKT | 0% | 576 | km/año | 0,01 |
| Combustión vehículos<br>Pavimentado Ruta 85 | Vehículo liviano | 6,06E-05 | kg/VKT | 0% | 75.600 | km/año | 0,00 |
| Combustión vehículos<br>Pavimentado Ruta 85 | Camión 3/4 Mantención | 8,82E-04 | kg/VKT | 0% | 504 | km/año | 0,00 |
| Combustión vehículos<br>Pavimentado Ruta 85 | Aljibe | 8,82E-04 | kg/VKT | 0% | 1.008 | km/año | 0,00 |
| Combustión vehículos<br>Pavimentado Ruta 85 | Camión 3/4 - Residuos Peligrosos | 8,82E-04 | kg/VKT | 0% | 320 | km/año | 0,00 |
| Combustión vehículos<br>Pavimentado Ruta 85 | Camión 3/4 - Residuos Domiciliarios | 8,82E-04 | kg/VKT | 0% | 3.840 | km/año | 0,00 |
| Combustión vehículos<br>Pavimentado Ruta 5-152 | Vehículo liviano | 6,06E-05 | kg/VKT | 0% | 406.800 | km/año | 0,02 |
| Combustión vehículos<br>Pavimentado Ruta 5-152 | Camión 3/4 Mantención | 8,82E-04 | kg/VKT | 0% | 2.712 | km/año | 0,00 |
| Combustión vehículos<br>Pavimentado Ruta 5-152 | Aljibe | 8,82E-04 | kg/VKT | 0% | 5.424 | km/año | 0,00 |
| Combustión vehículos<br>Pavimentado Ruta 5-152 | Camión 3/4 - Residuos Peligrosos | 8,82E-04 | kg/VKT | 0% | 904 | km/año | 0,00 |
| Combustión vehículos<br>Pavimentado Ruta 5-152 | Camión 3/4 - Residuos Domiciliarios | 8,82E-04 | kg/VKT | 0% | 10.848 | km/año | 0,01 |
| Combustión vehículos No<br>Pavimentadas | Vehículo liviano | 4,68E-05 | kg/VKT | 0% | 47.880 | km/año | 0,00 |
| Combustión vehículos No<br>Pavimentadas | Camión 3/4 Mantención | 7,02E-04 | kg/VKT | 0% | 47.880 | km/año | 0,03 |
| Combustión vehículos No<br>Pavimentadas | Aljibe | 7,02E-04 | kg/VKT | 0% | 319 | km/año | 0,00 |
| Combustión vehículos No<br>Pavimentadas | Camión 3/4 - Residuos Peligrosos | 7,02E-04 | kg/VKT | 0% | 638 | km/año | 0,00 |
| Combustión vehículos No<br>Pavimentadas | Camión 3/4 - Residuos Domiciliarios | 7,02E-04 | kg/VKT | 0% | 106 | km/año | 0,00 |
| Maquinaria fuera de ruta | Grúa pluma | 1,84E-02 | kg/h | 0% | 8 | h | 0,00 |
| Grupos electrógenos | Emergencia | 6,08E-03 | kg/kg comb. | 0% | 2.631 | kg comb. | 0,02 |
| **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **0,94 ** |

**Tabla 65.: ** Emisiones de MPS debido a las actividades de la fase de Operación del Proyecto Parque Eólico Dañicalqui, Sectores Parque Eólico**

| Actividad | Col2 | Factor Emisión | Col4 | Eficiencia<br>Mitigación | Nivel de Actividad | Col7 | Emisión MPS<br>(t/año) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Actividad** | **Actividad** | **Valor** | **Unidad** | **Unidad** | **Cantidad** | **Unidad** | **Unidad** |
| Resuspensión caminos<br>Pavimentados Ruta 85 | Vehículo liviano | 2,00E-03 | kg/VKT | 0% | 75.600 | km/año | 0,15 |
| Resuspensión caminos<br>Pavimentados Ruta 85 | Camión 3/4 Mantención | 3,14E-03 | kg/VKT | 0% | 504 | km/año | 0,00 |
| Resuspensión caminos<br>Pavimentados Ruta 85 | Aljibe | 1,84E-02 | kg/VKT | 0% | 1.008 | km/año | 0,02 |
| Resuspensión caminos<br>Pavimentados Ruta 85 | Camión 3/4 - Residuos Peligrosos | 3,14E-03 | kg/VKT | 0% | 320 | km/año | 0,00 |
| Resuspensión caminos<br>Pavimentados Ruta 85 | Camión 3/4 - Residuos Domiciliarios | 3,14E-03 | kg/VKT | 0% | 3.840 | km/año | 0,01 |
| Resuspensión caminos<br>Pavimentados Ruta 5-152 | Vehículo liviano | 2,00E-03 | kg/VKT | 0% | 406.800 | km/año | 0,81 |
| Resuspensión caminos<br>Pavimentados Ruta 5-152 | Camión 3/4 Mantención | 3,14E-03 | kg/VKT | 0% | 2.712 | km/año | 0,01 |
| Resuspensión caminos<br>Pavimentados Ruta 5-152 | Aljibe | 1,84E-02 | kg/VKT | 0% | 5.424 | km/año | 0,10 |
| Resuspensión caminos<br>Pavimentados Ruta 5-152 | Camión 3/4 - Residuos Peligrosos | 3,14E-03 | kg/VKT | 0% | 904 | km/año | 0,00 |
| Resuspensión caminos<br>Pavimentados Ruta 5-152 | Camión 3/4 - Residuos Domiciliarios | 3,14E-03 | kg/VKT | 0% | 10.848 | km/año | 0,03 |
| Resuspensión caminos No<br>Pavimentados - Externo | Vehículo liviano | 4,92E-01 | kg/VKT | 0% | 26.280 | km/año | 12,93 |
| Resuspensión caminos No<br>Pavimentados - Externo | Camión 3/4 Mantención | 6,00E-01 | kg/VKT | 0% | 175 | km/año | 0,11 |
| Resuspensión caminos No<br>Pavimentados - Externo | Aljibe | 1,31E+00 | kg/VKT | 0% | 350 | km/año | 0,46 |
| Resuspensión caminos No<br>Pavimentados - Externo | Camión 3/4 - Residuos Peligrosos | 6,00E-01 | kg/VKT | 0% | 58 | km/año | 0,04 |
| Resuspensión caminos No<br>Pavimentados - Externo | Camión 3/4 - Residuos Domiciliarios | 6,00E-01 | kg/VKT | 0% | 701 | km/año | 0,42 |
| Resuspensión caminos No<br>Pavimentados - Interno | Vehículo liviano | 4,92E-01 | kg/VKT | 0% | 21.600 | km/año | 10,63 |
| Resuspensión caminos No<br>Pavimentados - Interno | Camión 3/4 Mantención | 6,00E-01 | kg/VKT | 0% | 144 | km/año | 0,09 |
| Resuspensión caminos No<br>Pavimentados - Interno | Aljibe | 1,31E+00 | kg/VKT | 0% | 288 | km/año | 0,38 |
| Resuspensión caminos No<br>Pavimentados - Interno | Camión 3/4 - Residuos Peligrosos | 6,00E-01 | kg/VKT | 0% | 48 | km/año | 0,03 |
| Resuspensión caminos No<br>Pavimentados - Interno | Camión 3/4 - Residuos Domiciliarios | 6,00E-01 | kg/VKT | 0% | 576 | km/año | 0,35 |
| Combustión vehículos<br>Pavimentado Ruta 85 | Vehículo liviano | 6,06E-05 | kg/VKT | 0% | 75.600 | km/año | 0,00 |
| Combustión vehículos<br>Pavimentado Ruta 85 | Camión 3/4 Mantención | 8,82E-04 | kg/VKT | 0% | 504 | km/año | 0,00 |
| Combustión vehículos<br>Pavimentado Ruta 85 | Aljibe | 8,82E-04 | kg/VKT | 0% | 1.008 | km/año | 0,00 |
| Combustión vehículos<br>Pavimentado Ruta 85 | Camión 3/4 - Residuos Peligrosos | 8,82E-04 | kg/VKT | 0% | 320 | km/año | 0,00 |
| Combustión vehículos<br>Pavimentado Ruta 85 | Camión 3/4 - Residuos Domiciliarios | 8,82E-04 | kg/VKT | 0% | 3.840 | km/año | 0,00 |
| Combustión vehículos<br>Pavimentado Ruta 5-152 | Vehículo liviano | 6,06E-05 | kg/VKT | 0% | 406.800 | km/año | 0,02 |
| Combustión vehículos<br>Pavimentado Ruta 5-152 | Camión 3/4 Mantención | 8,82E-04 | kg/VKT | 0% | 2.712 | km/año | 0,00 |
| Combustión vehículos<br>Pavimentado Ruta 5-152 | Aljibe | 8,82E-04 | kg/VKT | 0% | 5.424 | km/año | 0,00 |
| Combustión vehículos<br>Pavimentado Ruta 5-152 | Camión 3/4 - Residuos Peligrosos | 8,82E-04 | kg/VKT | 0% | 904 | km/año | 0,00 |
| Combustión vehículos<br>Pavimentado Ruta 5-152 | Camión 3/4 - Residuos Domiciliarios | 8,82E-04 | kg/VKT | 0% | 10.848 | km/año | 0,01 |
| Combustión vehículos No<br>Pavimentadas | Vehículo liviano | 4,68E-05 | kg/VKT | 0% | 47.880 | km/año | 0,00 |
| Combustión vehículos No<br>Pavimentadas | Camión 3/4 Mantención | 7,02E-04 | kg/VKT | 0% | 47.880 | km/año | 0,03 |
| Combustión vehículos No<br>Pavimentadas | Aljibe | 7,02E-04 | kg/VKT | 0% | 319 | km/año | 0,00 |
| Combustión vehículos No<br>Pavimentadas | Camión 3/4 - Residuos Peligrosos | 7,02E-04 | kg/VKT | 0% | 638 | km/año | 0,00 |
| Combustión vehículos No<br>Pavimentadas | Camión 3/4 - Residuos Domiciliarios | 7,02E-04 | kg/VKT | 0% | 106 | km/año | 0,00 |
| Maquinaria fuera de ruta | Grúa pluma | 1,84E-02 | kg/h | 0% | 8 | h | 0,00 |
| Grupos electrógenos | Emergencia | 6,08E-03 | kg/kg comb. | 0% | 2.631 | kg comb. | 0,02 |
| **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **26,67 ** |

**Tabla 66.: ** Emisiones de NOx debido a las actividades de la fase de Operación del Proyecto Parque Eólico Dañicalqui, Sectores Parque Eólico**

| Actividad | Col2 | Factor Emisión | Col4 | Eficiencia<br>Mitigación | Nivel de Actividad | Col7 | Emisión NOx<br>(t/año) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Actividad** | **Actividad** | **Valor** | **Unidad** | **Unidad** | **Cantidad** | **Unidad** | **Unidad** |
| Combustión vehículos<br>Pavimentado Ruta 85 | Vehículo liviano | 8,59E-04 | kg/VKT | 0% | 75.600 | km/año | 0,06 |
| Combustión vehículos<br>Pavimentado Ruta 85 | Camión 3/4 Mantención | 7,56E-03 | kg/VKT | 0% | 504 | km/año | 0,00 |
| Combustión vehículos<br>Pavimentado Ruta 85 | Aljibe | 7,56E-03 | kg/VKT | 0% | 1.008 | km/año | 0,01 |
| Combustión vehículos<br>Pavimentado Ruta 85 | Camión 3/4 - Residuos Peligrosos | 7,56E-03 | kg/VKT | 0% | 320 | km/año | 0,00 |
| Combustión vehículos<br>Pavimentado Ruta 85 | Camión 3/4 - Residuos Domiciliarios | 7,56E-03 | kg/VKT | 0% | 3.840 | km/año | 0,03 |
| Combustión vehículos<br>Pavimentado Ruta 5-152 | Vehículo liviano | 8,59E-04 | kg/VKT | 0% | 406.800 | km/año | 0,35 |
| Combustión vehículos<br>Pavimentado Ruta 5-152 | Camión 3/4 Mantención | 7,56E-03 | kg/VKT | 0% | 2.712 | km/año | 0,02 |
| Combustión vehículos<br>Pavimentado Ruta 5-152 | Aljibe | 7,56E-03 | kg/VKT | 0% | 5.424 | km/año | 0,04 |
| Combustión vehículos<br>Pavimentado Ruta 5-152 | Camión 3/4 - Residuos Peligrosos | 7,56E-03 | kg/VKT | 0% | 904 | km/año | 0,01 |
| Combustión vehículos<br>Pavimentado Ruta 5-152 | Camión 3/4 - Residuos Domiciliarios | 7,56E-03 | kg/VKT | 0% | 10.848 | km/año | 0,08 |
| Combustión vehículos No<br>Pavimentadas | Vehículo liviano | 9,56E-04 | kg/VKT | 0% | 47.880 | km/año | 0,05 |
| Combustión vehículos No<br>Pavimentadas | Camión 3/4 Mantención | 9,63E-03 | kg/VKT | 0% | 47.880 | km/año | 0,46 |
| Combustión vehículos No<br>Pavimentadas | Aljibe | 9,63E-03 | kg/VKT | 0% | 319 | km/año | 0,00 |
| Combustión vehículos No<br>Pavimentadas | Camión 3/4 - Residuos Peligrosos | 9,63E-03 | kg/VKT | 0% | 638 | km/año | 0,01 |
| Combustión vehículos No<br>Pavimentadas | Camión 3/4 - Residuos Domiciliarios | 9,63E-03 | kg/VKT | 0% | 106 | km/año | 0,00 |
| Maquinaria fuera de ruta | Grúa pluma | 5,99E-01 | kg/h | 0% | 8 | h | 0,00 |
| Grupos electrógenos | Emergencia | 8,65E-02 | kg/kg comb. | 0% | 2.631 | kg comb. | 0,23 |
| **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **1,36 ** |

**Tabla 67.: ** Emisiones de CO debido a las actividades de la fase de Operación del Proyecto Parque Eólico Dañicalqui, Sectores Parque Eólico**

| Actividad | Col2 | Factor Emisión | Col4 | Eficiencia<br>Mitigación | Nivel de Actividad | Col7 | Emisión CO<br>(t/año) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Actividad** | **Actividad** | **Valor** | **Unidad** | **Unidad** | **Cantidad** | **Unidad** | **Unidad** |
| Combustión vehículos<br>Pavimentado Ruta 85 | Vehículo liviano | 3,47E-04 | kg/VKT | 0% | 75.600 | km/año | 0,03 |
| Combustión vehículos<br>Pavimentado Ruta 85 | Camión 3/4 Mantención | 1,30E-03 | kg/VKT | 0% | 504 | km/año | 0,00 |
| Combustión vehículos<br>Pavimentado Ruta 85 | Aljibe | 1,30E-03 | kg/VKT | 0% | 1.008 | km/año | 0,00 |
| Combustión vehículos<br>Pavimentado Ruta 85 | Camión 3/4 - Residuos Peligrosos | 1,30E-03 | kg/VKT | 0% | 320 | km/año | 0,00 |
| Combustión vehículos<br>Pavimentado Ruta 85 | Camión 3/4 - Residuos Domiciliarios | 1,30E-03 | kg/VKT | 0% | 3.840 | km/año | 0,00 |
| Combustión vehículos<br>Pavimentado Ruta 5-152 | Vehículo liviano | 3,47E-04 | kg/VKT | 0% | 406.800 | km/año | 0,14 |
| Combustión vehículos<br>Pavimentado Ruta 5-152 | Camión 3/4 Mantención | 1,30E-03 | kg/VKT | 0% | 2.712 | km/año | 0,00 |
| Combustión vehículos<br>Pavimentado Ruta 5-152 | Aljibe | 1,30E-03 | kg/VKT | 0% | 5.424 | km/año | 0,01 |
| Combustión vehículos<br>Pavimentado Ruta 5-152 | Camión 3/4 - Residuos Peligrosos | 1,30E-03 | kg/VKT | 0% | 904 | km/año | 0,00 |
| Combustión vehículos<br>Pavimentado Ruta 5-152 | Camión 3/4 - Residuos Domiciliarios | 1,30E-03 | kg/VKT | 0% | 10.848 | km/año | 0,01 |
|  | Vehículo liviano | 3,22E-04 | kg/VKT | 0% | 47.880 | km/año | 0,02 |

**Tabla 68.: ** Emisiones de SOx debido a las actividades de la fase de Operación del Proyecto Parque Eólico Dañicalqui, Sectores Parque Eólico**

| Actividad | Col2 | Factor Emisión | Col4 | Eficiencia<br>Mitigación | Nivel de Actividad | Col7 | Emisión SOx<br>(t/año) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Actividad** | **Actividad** | **Valor** | **Unidad** | **Unidad** | **Cantidad** | **Unidad** | **Unidad** |
| Combustión vehículos<br>Pavimentado Ruta 85 | Vehículo liviano | 6,37E-06 | kg/VKT | 0% | 75.600 | km/año | 0,00 |
| Combustión vehículos<br>Pavimentado Ruta 85 | Camión 3/4 Mantención | 2,06E-05 | kg/VKT | 0% | 504 | km/año | 0,00 |
| Combustión vehículos<br>Pavimentado Ruta 85 | Aljibe | 2,06E-05 | kg/VKT | 0% | 1.008 | km/año | 0,00 |
| Combustión vehículos<br>Pavimentado Ruta 85 | Camión 3/4 - Residuos Peligrosos | 2,06E-05 | kg/VKT | 0% | 320 | km/año | 0,00 |
| Combustión vehículos<br>Pavimentado Ruta 85 | Camión 3/4 - Residuos Domiciliarios | 2,06E-05 | kg/VKT | 0% | 3.840 | km/año | 0,00 |
| Combustión vehículos<br>Pavimentado Ruta 5-152 | Vehículo liviano | 6,37E-06 | kg/VKT | 0% | 406.800 | km/año | 0,00 |
| Combustión vehículos<br>Pavimentado Ruta 5-152 | Camión 3/4 Mantención | 2,06E-05 | kg/VKT | 0% | 2.712 | km/año | 0,00 |
| Combustión vehículos<br>Pavimentado Ruta 5-152 | Aljibe | 2,06E-05 | kg/VKT | 0% | 5.424 | km/año | 0,00 |
| Combustión vehículos<br>Pavimentado Ruta 5-152 | Camión 3/4 - Residuos Peligrosos | 2,06E-05 | kg/VKT | 0% | 904 | km/año | 0,00 |
| Combustión vehículos<br>Pavimentado Ruta 5-152 | Camión 3/4 - Residuos Domiciliarios | 2,06E-05 | kg/VKT | 0% | 10.848 | km/año | 0,00 |
| Combustión vehículos No<br>Pavimentadas | Vehículo liviano | 6,89E-06 | kg/VKT | 0% | 47.880 | km/año | 0,00 |
| Combustión vehículos No<br>Pavimentadas | Camión 3/4 Mantención | 2,66E-05 | kg/VKT | 0% | 47.880 | km/año | 0,00 |
| Combustión vehículos No<br>Pavimentadas | Aljibe | 2,66E-05 | kg/VKT | 0% | 319 | km/año | 0,00 |
| Combustión vehículos No<br>Pavimentadas | Camión 3/4 - Residuos Peligrosos | 2,66E-05 | kg/VKT | 0% | 638 | km/año | 0,00 |
| Combustión vehículos No<br>Pavimentadas | Camión 3/4 - Residuos Domiciliarios | 2,66E-05 | kg/VKT | 0% | 106 | km/año | 0,00 |
| Maquinaria fuera de ruta | Grúa pluma | 9,06E-04 | kg/h | 0% | 8 | h | 0,00 |
| Grupos electrógenos | Emergencia | 5,69E-03 | kg/kg comb. | 0% | 2.631 | kg comb. | 0,01 |
| **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **0,02 ** |

**Tabla 69.: ** Emisiones de HC debido a las actividades de la fase de Operación del Proyecto Parque Eólico Dañicalqui, Sectores Parque Eólico**

| Actividad | Col2 | Factor Emisión | Col4 | Eficiencia<br>Mitigación | Nivel de Actividad | Col7 | Emisión HC<br>(t/año) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Actividad** | **Actividad** | **Valor** | **Unidad** | **Unidad** | **Cantidad** | **Unidad** | **Unidad** |
| Combustión vehículos<br>Pavimentado Ruta 85 | Vehículo liviano | 6,06E-02 | kg/VKT | 0% | 75.600 | km/año | 4,58 |
| Combustión vehículos<br>Pavimentado Ruta 85 | Camión 3/4 Mantención | 2,77E-01 | kg/VKT | 0% | 504 | km/año | 0,14 |
| Combustión vehículos<br>Pavimentado Ruta 85 | Aljibe | 2,77E-01 | kg/VKT | 0% | 1.008 | km/año | 0,28 |
| Combustión vehículos<br>Pavimentado Ruta 85 | Camión 3/4 - Residuos Peligrosos | 2,77E-01 | kg/VKT | 0% | 320 | km/año | 0,09 |
| Combustión vehículos<br>Pavimentado Ruta 85 | Camión 3/4 - Residuos Domiciliarios | 2,77E-01 | kg/VKT | 0% | 3.840 | km/año | 1,06 |
| Combustión vehículos<br>Pavimentado Ruta 5-152 | Vehículo liviano | 6,06E-02 | kg/VKT | 0% | 406.800 | km/año | 24,67 |
| Combustión vehículos<br>Pavimentado Ruta 5-152 | Camión 3/4 Mantención | 2,77E-01 | kg/VKT | 0% | 2.712 | km/año | 0,75 |
| Combustión vehículos<br>Pavimentado Ruta 5-152 | Aljibe | 2,77E-01 | kg/VKT | 0% | 5.424 | km/año | 1,50 |
| Combustión vehículos<br>Pavimentado Ruta 5-152 | Camión 3/4 - Residuos Peligrosos | 2,77E-01 | kg/VKT | 0% | 904 | km/año | 0,25 |
| Combustión vehículos<br>Pavimentado Ruta 5-152 | Camión 3/4 - Residuos Domiciliarios | 2,77E-01 | kg/VKT | 0% | 10.848 | km/año | 3,00 |
| Combustión vehículos No<br>Pavimentadas | Vehículo liviano | 8,05E-02 | kg/VKT | 0% | 47.880 | km/año | 3,85 |
| Combustión vehículos No<br>Pavimentadas | Camión 3/4 Mantención | 4,88E-01 | kg/VKT | 0% | 47.880 | km/año | 23,36 |
| Combustión vehículos No<br>Pavimentadas | Aljibe | 4,88E-01 | kg/VKT | 0% | 319 | km/año | 0,16 |
| Combustión vehículos No<br>Pavimentadas | Camión 3/4 - Residuos Peligrosos | 4,88E-01 | kg/VKT | 0% | 638 | km/año | 0,31 |
| Combustión vehículos No<br>Pavimentadas | Camión 3/4 - Residuos Domiciliarios | 4,88E-01 | kg/VKT | 0% | 106 | km/año | 0,05 |
| Maquinaria fuera de ruta | Grúa pluma | 3,87E-02 | kg/h | 0% | 8 | h | 0,00 |
| Grupos electrógenos | Emergencia | 7,06E-03 | kg/kg comb. | 0% | 2.631 | kg comb. | 0,02 |
| **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **Total (t/año)** | **64,08 ** |

**Tabla 70.: ** Resumen de emisiones de MP10, MP2,5, MPS, NOx, CO, SOx y HC debido a las actividades de**

| Sector | Actividad Fase Construcción | Emisión (t) | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Sector** | **ActividadFaseConstrucción** | **Año 1** | **Año 2** | **Total** |
| **MP10** | **MP10** | **MP10** | **MP10** | **MP10** |
| Parque Eólico (PE) | Excavaciones | 5,07 | 7,07 | 12,14 |
| Parque Eólico (PE) | Carga y descarga | 0,16 | 0,22 | 0,38 |
| Parque Eólico (PE) | Compactación | 0,02 | 0,03 | 0,05 |
| Parque Eólico (PE) | Escarpe | 0,25 | 0,35 | 0,59 |
| Parque Eólico (PE) | Maquinaria Fuera de ruta | 1,44 | 0,30 | 1,73 |
| Parque Eólico (PE) | Resuspensión caminos Pavimentados | 9,94 | 3,58 | 13,52 |
| Parque Eólico (PE) | Resuspensión caminos No Pavimentados | 102,88 | 44,48 | 147,35 |
| Parque Eólico (PE) | Combustión vehículos | 2,12 | 0,78 | 2,88 |
| Parque Eólico (PE) | Grupos electrógenos | 0,63 | 0,63 | 1,27 |
| Parque Eólico (PE) | **Total** | **122,50** | **57,42** | **179,91** |
| **MP2,5** | **MP2,5** | **MP2,5** | **MP2,5** | **MP2,5** |
| Parque Eólico (PE) | Excavaciones | 2,44 | 3,40 | 5,85 |
| Parque Eólico (PE) | Carga y descarga | 0,02 | 0,03 | 0,06 |
| Parque Eólico (PE) | Compactación | 0,01 | 0,01 | 0,02 |
| Parque Eólico (PE) | Escarpe | 0,25 | 0,35 | 0,59 |
| Parque Eólico (PE) | Maquinaria Fuera de ruta | 1,44 | 0,30 | 1,73 |
| Parque Eólico (PE) | Resuspensión caminos Pavimentados | 2,41 | 0,87 | 3,27 |
| Parque Eólico (PE) | Resuspensión caminos No Pavimentados | 10,29 | 4,45 | 14,74 |
| Parque Eólico (PE) | Combustión vehículos | 2,12 | 0,78 | 2,88 |
| Parque Eólico (PE) | Grupos electrógenos | 0,63 | 0,63 | 1,27 |
| Parque Eólico (PE) | **Total** | **19,60** | **10,82** | **30,40** |
| **MPS** | **MPS** | **MPS** | **MPS** | **MPS** |
| Parque Eólico (PE) | Excavaciones | 23,28 | 32,42 | 55,70 |
| Parque Eólico (PE) | Carga y descarga | 0,33 | 0,46 | 0,79 |
| Parque Eólico (PE) | Compactación | 0,10 | 0,13 | 0,23 |
| Parque Eólico (PE) | Escarpe | 0,25 | 0,35 | 0,59 |
| Parque Eólico (PE) | Maquinaria Fuera de ruta | 1,44 | 0,30 | 1,73 |
| Parque Eólico (PE) | Resuspensión caminos Pavimentados | 51,80 | 18,64 | 70,43 |
| Parque Eólico (PE) | Resuspensión caminos No Pavimentados | 336,06 | 145,29 | 481,35 |
| Parque Eólico (PE) | Combustión vehículos | 2,12 | 0,78 | 2,88 |
| Parque Eólico (PE) | Grupos electrógenos | 0,63 | 0,63 | 1,27 |
| Parque Eólico (PE) | **Total** | **416,00** | **198,99** | **614,98** |

**Tabla 71.: ** Resumen de emisiones de MP10, MP2,5, MPS, NOx, CO, SOx y HC debido a las actividades de**

| Sector | Actividad Fase Construcción | Emisión (t) | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Sector** | **ActividadFaseConstrucción** | **Año 1** | **Año 2** | **Total** |
| **MP10** | **MP10** | **MP10** | **MP10** | **MP10** |
| Línea de Transmisión<br>(LT) | Excavaciones | 0,03 | 0,04 | 0,07 |
| Línea de Transmisión<br>(LT) | Carga y descarga | 0,00 | 0,00 | 0,00 |
| Línea de Transmisión<br>(LT) | Compactación | 0,00 | 0,00 | 0,00 |
| Línea de Transmisión<br>(LT) | Escarpe | 0,01 | 0,01 | 0,02 |
| Línea de Transmisión<br>(LT) | Maquinaria Fuera de ruta | 0,35 | 0,88 | 1,23 |
| Línea de Transmisión<br>(LT) | Resuspensión caminos Pavimentados | 0,00 | 0,11 | 0,11 |
| Línea de Transmisión<br>(LT) | Resuspensión caminos No Pavimentados | 0,00 | 0,24 | 0,24 |
| Línea de Transmisión<br>(LT) | Combustión vehículos | 0,00 | 0,02 | 0,02 |
| Línea de Transmisión<br>(LT) | Erosión eólica | 0,01 | 0,01 | 0,01 |
| Línea de Transmisión<br>(LT) | **Total** | **0,40** | **1,31** | **1,71** |
| **MP2,5** | **MP2,5** | **MP2,5** | **MP2,5** | **MP2,5** |
| Línea de Transmisión<br>(LT) | Excavaciones | 0,01 | 0,02 | 0,03 |
| Línea de Transmisión<br>(LT) | Carga y descarga | 0,00 | 0,00 | 0,00 |
| Línea de Transmisión<br>(LT) | Compactación | 0,00 | 0,00 | 0,00 |
| Línea de Transmisión<br>(LT) | Escarpe | 0,01 | 0,01 | 0,02 |
| Línea de Transmisión<br>(LT) | Maquinaria Fuera de ruta | 0,35 | 0,88 | 1,23 |
| Línea de Transmisión<br>(LT) | Resuspensión caminos Pavimentados | 0,00 | 0,03 | 0,03 |
| Línea de Transmisión<br>(LT) | Resuspensión caminos No Pavimentados | 0,00 | 0,02 | 0,02 |
| Línea de Transmisión<br>(LT) | Combustión vehículos | 0,00 | 0,02 | 0,02 |

**Tabla 72.: ** Resumen de emisiones de MP10, MP2,5, MPS, NOx, CO, SOx y HC de la fase de construcción**

| Contaminante | Emisión (t) | Col3 | Col4 |
| --- | --- | --- | --- |
| **Contaminante** | **Año 1** | **Año 2** | **Total** |
| **MP10** | 122,91 | 58,74 | 181,61 |
| **MP2,5** | 20,00 | 11,82 | 31,78 |
| **MPS** | 416,52 | 201,49 | 617,97 |
| **NOx** | 86,33 | 46,96 | 119,63 |
| **CO** | 20,29 | 13,54 | 31,35 |
| **SOx** | 0,76 | 0,67 | 1,39 |
| **HC** | 776,03 | 106,79 | 367,05 |

**Tabla 73.: ** Resumen de emisiones de MP10, MP2,5, MPS, NOx, CO, SOx y HC debido a las actividades de**

| Actividad Fase Operación | Emisión (t/año) |
| --- | --- |
| **MP10** | **MP10** |
| Resuspensión caminos Pavimentados | 0,22 |
| Resuspensión caminos No Pavimentados | 7,78 |
| Combustión vehículos | 0,09 |
| Maquinaria Fuera de ruta | 0,00 |
| Grupos electrógenos | 0,02 |
| **Total** | **8,11** |
| **MP2,5** | **MP2,5** |
| Resuspensión caminos Pavimentados | 0,05 |
| Resuspensión caminos No Pavimentados | 0,78 |
| Combustión vehículos | 0,09 |
| Maquinaria Fuera de ruta | 0,00 |
| Grupos electrógenos | 0,02 |
| **Total** | **0,94** |
| **MPS** | **MPS** |
| Resuspensión caminos Pavimentados | 1,14 |
| Resuspensión caminos No Pavimentados | 25,42 |
| Combustión vehículos | 0,09 |
| Maquinaria Fuera de ruta | 0,00 |
| Grupos electrógenos | 0,02 |
| **Total** | **26,67** |
| **NOx** | **NOx** |
| Combustión vehículos | 1,12 |
| Maquinaria Fuera de ruta | 0,00 |
| Grupos electrógenos | 0,23 |
| **Total** | **1,36** |
| **CO** | **CO** |
| Combustión vehículos | 0,30 |
| Maquinaria Fuera de ruta | 0,00 |
| Grupos electrógenos | 0,05 |
| **Total** | **0,35** |
| **SOx** | **SOx** |
| Combustión vehículos | 0,01 |
| Maquinaria Fuera de ruta | 0,00 |
| Grupos electrógenos | 0,01 |
| **Total** | **0,02** |
| **HC** | **HC** |
| Combustión vehículos | 64,06 |
| Maquinaria Fuera de ruta | 0,00 |
| Grupos electrógenos | 0,02 |
| **Total** | **64,08** |

**Tabla 74.: ** Resumen de emisiones de MP10, MP2,5, MPS, NOx, CO, SOx y HC de la fase de operación del**

| Contaminante | Emisión (t/año) |
| --- | --- |
| MP10 | 8,11 |
| MP2,5 | 0,94 |
| MPS | 26,67 |
| NOx | 1,36 |
| CO | 0,35 |
| SOx | 0,020 |
| HC | 64,08 |

**Tabla 75.: ** Resumen de emisiones de MP10, MP2,5, MPS, NOx, CO, SOx y HC de la fase de cierre del**

| Contaminante | Emisión (t) | Col3 | Col4 |
| --- | --- | --- | --- |
| **Contaminante** | **Año 1** | **Año 2** | **Total** |
| **MP10** | 123,54 | 59,37 | 182,88 |
| **MP2,5** | 20,63 | 12,45 | 33,05 |
| **MPS** | 417,15 | 202,12 | 619,24 |
| **NOx** | 95,34 | 55,97 | 137,65 |
| **CO** | 22,23 | 15,49 | 35,23 |
| **SOx** | 1,35 | 1,26 | 2,57 |
| **HC** | 776,77 | 107,52 | 368,52 |

**Tabla 76.: ** Características del dominio de modelación utilizada por el modelo CALPUFF en la zona del**

| Características dominio CALPUFF-Ready | Col2 |
| --- | --- |
| Resolución | 1.000 x 1.000 (m) |
| No de celdas en dirección X | 95 |
| No de celdas en dirección Y | 95 |
| Coordenadas de referencia del origen del dominio* | UTM-E: 692.336 (m), UTM-N: 5.862.889 (m). |
| Total del área del dominio | 9.025 (km2) |

**Tabla 77.: ** Características del área de receptores de Grilla.**

| Item | Características |
| --- | --- |
| Kilómetros en dirección X | 80 |
| Kilómetros en dirección Y | 73 |
| Factor de anidamiento de la cuadrícula de receptores | 4 |
| Celdas de receptores en X | 320 |
| Celdas de receptores en Y | 292 |
| Resolución | 250 m |
| Coordenadas de referencia del origen del dominio* | UTM-E: 692.736 (m), UTM-N: 5.876.884 (m) |
| Total de receptores | 93.440 |

**Tabla 78.: ** Coordenadas de receptores de interés en la zona del Proyecto.**

| Receptor | ID Proyecto | UTM (WGS 84 - Z18) | Col4 | Altitud (1)<br>(m.s.n.m.) | LCC (km) | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Receptor ** | **ID Proyecto** | **Este (m)** | **Norte (m)** | **Norte (m)** | **LCC-X** | **LCC-Y** |
| R1 | 454 | 755,802 | 5,900,928 | 191.9 | 14.840 | -7.673 |
| R2 | 456 | 755,827 | 5,900,931 | 192.0 | 14.865 | -7.669 |
| R3 | 455 | 755,793 | 5,900,916 | 191.9 | 14.832 | -7.685 |
| R4 | 472 | 755,779 | 5,900,954 | 191.8 | 14.817 | -7.648 |
| R5 | 457-2 | 756,759 | 5,902,009 | 200.4 | 15.766 | -6.566 |
| R6 | 463 | 756,843 | 5,902,240 | 202.2 | 15.843 | -6.332 |
| R7 | 465 | 756,669 | 5,902,273 | 201.1 | 15.668 | -6.304 |
| R8 | 458 | 756,911 | 5,902,149 | 202.3 | 15.914 | -6.421 |
| R9 | 461 | 756,877 | 5,902,226 | 202.4 | 15.877 | -6.345 |
| R10 | 462 | 756,814 | 5,902,217 | 201.9 | 15.815 | -6.356 |
| R11 | 464 | 756,817 | 5,902,245 | 202.1 | 15.817 | -6.328 |
| R12 | 460 | 756,957 | 5,902,171 | 202.7 | 15.959 | -6.398 |
| R13 | 469 | 757,039 | 5,902,557 | 205.4 | 16.030 | -6.010 |
| R14 | 470 | 757,645 | 5,903,090 | 209.0 | 16.620 | -5.460 |
| R15 | 466 | 757,022 | 5,902,308 | 203.9 | 16.020 | -6.259 |
| R16 | 471 | 757,645 | 5,903,225 | 208.8 | 16.616 | -5.325 |
| R17 | 467 | 757,213 | 5,902,386 | 205.8 | 16.209 | -6.176 |
| R18 | 468 | 757,269 | 5,902,522 | 206.9 | 16.261 | -6.039 |
| R19 | 459 | 756,904 | 5,902,117 | 202.1 | 15.908 | -6.454 |
| R20 | 3 | 748,661 | 5,900,584 | 151.8 | 7.715 | -8.220 |
| R21 | 4 | 748,803 | 5,900,580 | 152.6 | 7.857 | -8.220 |
| R22 | 5 | 748,763 | 5,900,452 | 152.7 | 7.820 | -8.349 |
| R23 | 8 | 750,709 | 5,900,420 | 168.2 | 9.766 | -8.325 |
| R24 | 14 | 750,553 | 5,900,372 | 166.7 | 9.611 | -8.378 |
| R25 | 36 | 750,336 | 5,900,339 | 164.9 | 9.395 | -8.417 |
| R26 | 43 | 750,488 | 5,900,312 | 166.0 | 9.548 | -8.440 |
| R27 | 71 | 750,469 | 5,900,229 | 165.5 | 9.531 | -8.523 |
| R28 | 79 | 750,838 | 5,900,180 | 168.1 | 9.902 | -8.562 |
| R29 | 92 | 750,714 | 5,900,127 | 166.9 | 9.779 | -8.618 |
| R30 | 94 | 750,384 | 5,900,124 | 164.4 | 9.449 | -8.630 |
| R31 | 99 | 751,015 | 5,900,089 | 168.9 | 10.081 | -8.648 |
| R32 | 128 | 751,156 | 5,899,785 | 168.3 | 10.231 | -8.947 |
| R33 | 133 | 750,804 | 5,899,756 | 165.9 | 9.880 | -8.986 |
| R34 | 149 | 751,033 | 5,899,593 | 166.8 | 10.113 | -9.143 |
| R35 | 150 | 751,072 | 5,899,592 | 167.0 | 10.152 | -9.142 |
| R36 | 158 | 751,100 | 5,899,565 | 167.1 | 10.181 | -9.169 |
| R37 | 160 | 751,142 | 5,899,530 | 167.2 | 10.224 | -9.202 |
| R38 | 164 | 753,860 | 5,899,456 | 177.9 | 12.942 | -9.199 |
| R39 | 177 | 753,773 | 5,899,258 | 176.1 | 12.860 | -9.399 |
| R40 | 188 | 753,841 | 5,899,096 | 175.2 | 12.933 | -9.559 |
| R41 | 197 | 752,501 | 5,898,493 | 170.3 | 11.611 | -10.200 |

**Tabla 79.: ** Emisiones de MP10, MP2,5, MPS, NO 2, SO 2 y CO del primer año de construcción del Proyecto**

| Sector | Fuente | Emisión contaminante (kg/año) | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Sector** | **Fuente** | **MP10** | **MP2,5** | **MPS** | **NO2 ** | **SO2 ** | **CO** |
| **PE** | Para todas las áreas | 5.940,97 | 3.605,20 | 21.705,40 | 4.611,14 | 89,21 | 11.709,26 |
| **PE** | Fundaciones | 642,60 | 305,81 | 2.920,10 |  |  |  |
| **PE** | Puente Río Dañicalqui | 9,45 | 4,50 | 42,93 |  |  |  |
| **PE** | Puente Estero Culenco | 1,24 | 0,59 | 5,66 |  |  |  |
| **PE** | Puente Canal | 1,66 | 0,79 | 7,54 |  |  |  |
| **PE** | Obras de Arte | 2,13 | 1,02 | 9,69 |  |  |  |
| **PE** | Instalación de faenas | 649,75 | 649,08 | 654,34 | 900,85 | 592,39 | 1.940,58 |
| **PE** | Planta de Hormigón | 9,41 | 9,03 | 12,03 | 0,00 | 0,00 | 0,00 |
| **PE** | Estación elevadora | 4,70 | 4,51 | 6,01 | 0,00 | 0,00 | 0,00 |
| **PE** | Plataformas | 99,87 | 95,85 | 127,68 |  |  |  |
| **PE** | Zanja Circuiros MT | 85,86 | 49,83 | 329,56 | 29,51 | 0,44 | 198,84 |
| **PE** | Resuspensión caminos Pavimentados - Ruta 85 | 1.663,21 | 402,39 | 8.664,79 |  |  |  |
| **PE** | Resuspensión caminos Pavimentados - Rutas 5 y 152 | 8.279,42 | 2.003,08 | 43.133,09 |  |  |  |
| **PE** | Resuspensión caminos No Pavimentados**CS-EX** | 1.931,28 | 193,13 | 6.308,86 |  |  |  |
| **PE** | Resuspensión caminos No Pavimentados**CS-IN** | 509,87 | 53,03 | 1.660,85 |  |  |  |
| **PE** | Resuspensión caminos No Pavimentados**SS-EX** | 38.586,01 | 3.858,60 | 126.047,62 |  |  |  |
| **PE** | Resuspensión caminos No Pavimentados**SS-IN** | 61.912,77 | 6.244,17 | 202.126,08 |  |  |  |
| **PE** | Combustión Pavimentados 80 km/h | 323,09 | 323,09 | 323,09 | 281,81 | 8,23 | 511,84 |
| **PE** | Combustión No Pavimentados 40 km/h | 183,82 | 183,82 | 183,82 | 254,41 | 7,34 | 452,85 |
| **PE** | Combustión 30 km/h | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| **PE** | Combustión caminos Pavimentados - Rutas 5 y 152 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| **PE** | **Sub-Total** | **120.837,10** | **17.987,52** | **414.269,11** | **6.077,73** | **697,61** | **14.813,36** |
| **LT** | Torres LT | 30,60 | 14,56 | 139,06 |  |  |  |
| **LT** | Torres y acopio (ZA) | 363,50 | 363,50 | 363,50 | 1.152,78 | 22,30 | 2.927,31 |
| **LT** | Acopio (ZA) | 66,80 | 24,35 | 140,35 |  |  |  |
| **LT** | Resuspensión caminos Pavimentados - Ruta 85 | 0,00 | 0,00 | 0,00 |  |  |  |
| **LT** | Resuspensión caminos Pavimentados - Rutas 5 y 152 | 0,00 | 0,00 | 0,00 |  |  |  |
| **LT** | Resuspensión caminos No Pavimentados**CS-EX** | 0,00 | 0,00 | 0,00 |  |  |  |
| **LT** | Resuspensión caminos No Pavimentados**SS-EX** | 0,00 | 0,00 | 0,00 |  |  |  |
| **LT** | Combustión Pavimentados 80 km/h | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| **LT** | Combustión No Pavimentados 40 km/h | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| **LT** | Combustión 30 km/h | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| **LT** | Combustión caminos Pavimentados - Rutas 5 y 152 | 1.608,32 | 1.608,32 | 1.608,32 | 1.402,85 | 40,98 | 2.547,91 |
| **LT** | **Sub-Total** | **2.069,22** | **2.010,74** | **2.251,23** | **2.555,64** | **63,28** | **5.475,23** |
| **Total** | **Total** | **122.906,32** | **19.998,26** | **416.520,35** | **8.633,37** | **760,88** | **20.288,58** |

**Tabla 80.: ** Coordenadas de las áreas donde se implementaron las fuentes emisoras de contaminantes**

| Sector | Fuente | Superficie<br>(m2) | Punto | UTM (WGS 84 - Z18) | Col6 | LCC (m) | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Sector** | **Fuente** | **Superficie**<br>**(m2) ** | **Punto** | **Este (m)** | **Norte (m)** | **LCC-X** | **LCC-Y** |
| **PE** | Estacionamiento SE | 140 | 1 | 750.341 | 5.897.953 | 9.468 | -10.801 |
| **PE** | Estacionamiento SE | 140 | 2 | 750.332 | 5.897.932 | 9.460 | -10.823 |
| **PE** | Estacionamiento SE | 140 | 3 | 750.338 | 5.897.929 | 9.466 | -10.825 |
| **PE** | Estacionamiento SE | 140 | 4 | 750.347 | 5.897.951 | 9.474 | -10.803 |
| **PE** | Instalación de Faenas-1 | 7.446 | 1 | 754.453 | 5.897.039 | 13.603 | -11.598 |
| **PE** | Instalación de Faenas-1 | 7.446 | 2 | 754.479 | 5.897.105 | 13.627 | -11.530 |
| **PE** | Instalación de Faenas-1 | 7.446 | 3 | 754.380 | 5.897.151 | 13.526 | -11.487 |
| **PE** | Instalación de Faenas-1 | 7.446 | 4 | 754.369 | 5.897.072 | 13.518 | -11.567 |
| **PE** | Instalación de Faenas-2 | 5.231 | 1 | 754.380 | 5.897.151 | 13.526 | -11.487 |
| **PE** | Instalación de Faenas-2 | 5.231 | 2 | 754.306 | 5.897.138 | 13.453 | -11.503 |
| **PE** | Instalación de Faenas-2 | 5.231 | 3 | 754.277 | 5.897.092 | 13.426 | -11.549 |
| **PE** | Instalación de Faenas-2 | 5.231 | 4 | 754.369 | 5.897.072 | 13.518 | -11.567 |
| **PE** | Instalación de Faenas-3 | 5.248 | 1 | 754.277 | 5.897.092 | 13.426 | -11.549 |
| **PE** | Instalación de Faenas-3 | 5.248 | 2 | 754.308 | 5.897.001 | 13.459 | -11.639 |
| **PE** | Instalación de Faenas-3 | 5.248 | 3 | 754.334 | 5.896.985 | 13.486 | -11.655 |
| **PE** | Instalación de Faenas-3 | 5.248 | 4 | 754.369 | 5.897.072 | 13.518 | -11.567 |
| **PE** | Planta de Hormigón | 10.218 | 1 | 754.453 | 5.897.039 | 13.603 | -11.598 |
| **PE** | Planta de Hormigón | 10.218 | 2 | 754.369 | 5.897.072 | 13.518 | -11.567 |
| **PE** | Planta de Hormigón | 10.218 | 3 | 754.334 | 5.896.985 | 13.486 | -11.655 |
| **PE** | Planta de Hormigón | 10.218 | 4 | 754.403 | 5.896.915 | 13.557 | -11.722 |
| **PE** | Subestación | 4.991 | 1 | 750.285 | 5.897.991 | 9.411 | -10.764 |
| **PE** | Subestación | 4.991 | 2 | 750.255 | 5.897.922 | 9.384 | -10.834 |
| **PE** | Subestación | 4.991 | 3 | 750.317 | 5.897.896 | 9.446 | -10.858 |
| **PE** | Subestación | 4.991 | 4 | 750.346 | 5.897.966 | 9.473 | -10.788 |
| **PE** | Puente Río Dañicalqui | 2.050 | 1 | 753.776 | 5.897.217 | 12.922 | -11.438 |
| **PE** | Puente Río Dañicalqui | 2.050 | 2 | 753.801 | 5.897.208 | 12.947 | -11.447 |
| **PE** | Puente Río Dañicalqui | 2.050 | 3 | 753.827 | 5.897.282 | 12.971 | -11.373 |
| **PE** | Puente Río Dañicalqui | 2.050 | 4 | 753.803 | 5.897.291 | 12.946 | -11.364 |
| **PE** | Puente Estero Culenco | 479 | 1 | 755.695 | 5.900.820 | 14.736 | -7.784 |
| **PE** | Puente Estero Culenco | 479 | 2 | 755.680 | 5.900.798 | 14.722 | -7.806 |
| **PE** | Puente Estero Culenco | 479 | 3 | 755.693 | 5.900.787 | 14.736 | -7.817 |
| **PE** | Puente Estero Culenco | 479 | 4 | 755.710 | 5.900.812 | 14.751 | -7.792 |
| **PE** | Puente Canal | 392 | 1 | 750.365 | 5.897.512 | 9.505 | -11.241 |
| **PE** | Puente Canal | 392 | 2 | 750.363 | 5.897.498 | 9.503 | -11.255 |
| **PE** | Puente Canal | 392 | 3 | 750.395 | 5.897.496 | 9.535 | -11.256 |
| **PE** | Puente Canal | 392 | 4 | 750.393 | 5.897.508 | 9.533 | -11.244 |
| **PE** | Obra de Arte 1 | 526 | 1 | 751.698 | 5.897.155 | 10.847 | -11.560 |
| **PE** | Obra de Arte 1 | 526 | 2 | 751.703 | 5.897.136 | 10.853 | -11.579 |
| **PE** | Obra de Arte 1 | 526 | 3 | 751.731 | 5.897.142 | 10.880 | -11.572 |
| **PE** | Obra de Arte 1 | 526 | 4 | 751.725 | 5.897.160 | 10.874 | -11.554 |
| **PE** | Obra de Arte 2 | 224 | 1 | 754.381 | 5.896.876 | 13.536 | -11.762 |
| **PE** | Obra de Arte 2 | 224 | 2 | 754.393 | 5.896.885 | 13.548 | -11.753 |
| **PE** | Obra de Arte 2 | 224 | 3 | 754.384 | 5.896.897 | 13.539 | -11.741 |
| **PE** | Obra de Arte 2 | 224 | 4 | 754.373 | 5.896.887 | 13.527 | -11.751 |
| **PE** | Obra de Arte 3 | 297 | 1 | 754.373 | 5.896.505 | 13.538 | -12.133 |
| **PE** | Obra de Arte 3 | 297 | 2 | 754.387 | 5.896.501 | 13.552 | -12.137 |

**Tabla 81.: ** Coordenadas de los tramos de zanja del circuito MT donde se implementaron las fuentes**

| Sector | Fuente | Largo (m) | Punto | UTM (WGS 84 - Z18) | Col6 | LCC (m) | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Sector** | **Fuente** | **Largo (m)** | **Punto** | **Este (m)** | **Norte (m)** | **LCC-X** | **LCC-Y** |
| **PE** | Zanja MT-1 | 304 | 1 | 750.329 | 5.897.926 | 9.458 | -10.828 |
| **PE** | Zanja MT-1 | 304 | 2 | 750.342 | 5.897.921 | 9.471 | -10.833 |
| **PE** | Zanja MT-1 | 304 | 3 | 750.334 | 5.897.900 | 9.463 | -10.854 |
| **PE** | Zanja MT-1 | 304 | 4 | 750.262 | 5.897.790 | 9.394 | -10.967 |
| **PE** | Zanja MT-1 | 304 | 5 | 750.261 | 5.897.785 | 9.394 | -10.971 |
| **PE** | Zanja MT-1 | 304 | 6 | 750.296 | 5.897.696 | 9.431 | -11.059 |
| **PE** | Zanja MT-1 | 304 | 7 | 750.306 | 5.897.662 | 9.442 | -11.093 |
| **PE** | Zanja MT-2 | 155 | 1 | 750.345 | 5.897.534 | 9.484 | -11.219 |
| **PE** | Zanja MT-2 | 155 | 2 | 750.351 | 5.897.528 | 9.491 | -11.226 |
| **PE** | Zanja MT-2 | 155 | 3 | 750.355 | 5.897.526 | 9.494 | -11.227 |
| **PE** | Zanja MT-2 | 155 | 4 | 750.369 | 5.897.515 | 9.509 | -11.237 |
| **PE** | Zanja MT-2 | 155 | 5 | 750.373 | 5.897.515 | 9.513 | -11.237 |
| **PE** | Zanja MT-2 | 155 | 6 | 750.385 | 5.897.510 | 9.525 | -11.242 |
| **PE** | Zanja MT-2 | 155 | 7 | 750.408 | 5.897.510 | 9.548 | -11.242 |
| **PE** | Zanja MT-2 | 155 | 8 | 750.441 | 5.897.512 | 9.581 | -11.239 |

**Tabla 82.: ** Coordenadas de los tramos de caminos donde se implementaron las fuentes emisoras de**

| Sector | Fuente | Largo (m) | Punto | UTM (WGS 84 - Z18) | Col6 | LCC (km) | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Sector** | **Fuente** | **Largo (m)** | **Punto** | **Este (m)** | **Norte (m)** | **LCC-X** | **LCC-Y** |
| PE | Área supresor 1 | 523 | 1 | 757.662 | 5.903.171 | 16.635 | -5.379 |
| PE | Área supresor 1 | 523 | 2 | 757.651 | 5.903.146 | 16.624 | -5.404 |
| PE | Área supresor 1 | 523 | 3 | 757.628 | 5.903.113 | 16.602 | -5.438 |
| PE | Área supresor 1 | 523 | 4 | 757.603 | 5.903.079 | 16.578 | -5.473 |
| PE | Área supresor 1 | 523 | 5 | 757.337 | 5.902.762 | 16,322 | -5,797 |
| LT | Área supresor 2 | 405 | 1 | 750.307 | 5.900.435 | 9.364 | -8.322 |
| LT | Área supresor 2 | 405 | 2 | 750.244 | 5.900.034 | 9.312 | -8.724 |
| PE | Área supresor 3 | 276 | 1 | 753.504 | 5.896.605 | 12.668 | -12.058 |
| PE | Área supresor 3 | 276 | 2 | 753.241 | 5.896.688 | 12.402 | -11.983 |
| PE | Área supresor 4 (Exterior) | 254 | 1 | 754.725 | 5.898.196 | 13.842 | -10.433 |
| PE | Área supresor 4 (Exterior) | 254 | 2 | 754.627 | 5.898.136 | 13.745 | -10.496 |
| PE | Área supresor 4 (Exterior) | 254 | 3 | 754.578 | 5.898.088 | 13.698 | -10.546 |
| PE | Área supresor 4 (Exterior) | 254 | 4 | 754.546 | 5.898.025 | 13.668 | -10.610 |
| PE | Área supresor 4 (Interior) | 113 | 1 | 754.546 | 5.898.025 | 13.668 | -10.610 |
| PE | Área supresor 4 (Interior) | 113 | 2 | 754.528 | 5.897.988 | 13.651 | -10.646 |
| PE | Área supresor 4 (Interior) | 113 | 3 | 754.515 | 5.897.956 | 13.639 | -10.679 |
| PE | Área supresor 4 (Interior) | 113 | 4 | 754.496 | 5.897.924 | 13.621 | -10.712 |
| PE | Área supresor 5 | 245 | 1 | 755.867 | 5.901.029 | 14.902 | -7.570 |
| PE | Área supresor 5 | 245 | 2 | 755.717 | 5.900.835 | 14.758 | -7.768 |
| PE | Área supresor 6 | 649 | 1 | 757.069 | 5.902.439 | 16.063 | -6.127 |
| PE | Área supresor 6 | 649 | 2 | 756.659 | 5.901.935 | 15.668 | -6.642 |
| PE | Área supresor 7 | 272 | 1 | 757.069 | 5.902.443 | 16.063 | -6.123 |
| PE | Área supresor 7 | 272 | 2 | 757.242 | 5.902.653 | 16.230 | -5.909 |
| PE | Área supresor 8 | 260 | 1 | 755.719 | 5.900.830 | 14.760 | -7.773 |
| PE | Área supresor 8 | 260 | 2 | 755.671 | 5.900.775 | 14.714 | -7.830 |
| PE | Área supresor 8 | 260 | 3 | 755.552 | 5.900.730 | 14.596 | -7.878 |
| PE | Área supresor 8 | 260 | 4 | 755.507 | 5.900.691 | 14.552 | -7.918 |
| PE | Área supresor 9 | 232 | 1 | 755.870 | 5.901.032 | 14.905 | -7.567 |
| PE | Área supresor 9 | 232 | 2 | 756.011 | 5.901.217 | 15.041 | -7.379 |
| PE | Acceso PE-1 | 143 | 1 | 757.337 | 5.902.762 | 16,322 | -5,797 |
| PE | Acceso PE-1 | 143 | 2 | 757.247 | 5.902.651 | 16.235 | -5.911 |
| PE | Acceso PE-2 | 966 | 1 | 756.658 | 5.901.935 | 15.667 | -6.643 |
| PE | Acceso PE-2 | 966 | 2 | 756.012 | 5.901.217 | 15.041 | -7.379 |
| PE | Acceso PE-3 | 2.795 | 1 | 755.506 | 5.900.689 | 14.552 | -7.920 |
| PE | Acceso PE-3 | 2.795 | 2 | 755.439 | 5.900.621 | 14.486 | -7.990 |
| PE | Acceso PE-3 | 2.795 | 3 | 755.404 | 5.900.448 | 14.456 | -8.164 |
| PE | Acceso PE-3 | 2.795 | 4 | 755.320 | 5.900.247 | 14.378 | -8.367 |
| PE | Acceso PE-3 | 2.795 | 5 | 755.007 | 5.899.579 | 14.084 | -9.044 |
| PE | Acceso PE-3 | 2.795 | 6 | 754.811 | 5.898.694 | 13.914 | -9.934 |

**Tabla 83.: ** Resultados de MP10 promedio anual y percentil 98 de las concentraciones diarias modeladas**

| Receptor | Concentración de MP10 (μg/Nm3) | Col3 |
| --- | --- | --- |
| **Receptor** | **Promedio anual** | **Percentil 98 de las concentraciones 24**<br>**horas** |
| **R1** | 7,0 | 37,0 |
| **R2** | 5,6 | 29,6 |
| **R3** | 7,1 | 36,8 |
| **R4** | 4,9 | 22,9 |
| **R5** | 7,1 | 48,6 |
| **R6** | 3,2 | 21,4 |
| **R7** | 3,6 | 17,7 |
| **R8** | 3,6 | 21,3 |
| **R9** | 4,4 | 29,7 |
| **R10** | 3,3 | 20,9 |
| **R11** | 3,0 | 17,8 |
| **R12** | 3,3 | 19,5 |
| **R13** | 1,8 | 10,4 |
| **R14** | 3,1 | 15,6 |
| **R15** | 3,2 | 17,7 |
| **R16** | 1,9 | 10,1 |
| **R17** | 2,6 | 13,8 |
| **R18** | 4,0 | 23,4 |
| **R19** | 3,8 | 23,4 |
| **R20** | 0,1 | 0,7 |
| **R21** | 0,1 | 0,6 |
| **R22** | 0,1 | 0,6 |
| **R23** | 0,2 | 1,5 |

**Tabla 84.: ** Resultados de MP2,5 promedio anual y percentil 98 de las concentraciones diarias modeladas**

| Receptor | Concentración de MP2,5 (μg/Nm3) | Col3 |
| --- | --- | --- |
| **Receptor** | **Promedio anual** | **Percentil 98 de las concentraciones 24**<br>**horas** |
| **R1** | 0,8 | 4,2 |
| **R2** | 0,6 | 3,5 |
| **R3** | 0,8 | 4,1 |
| **R4** | 0,6 | 2,7 |
| **R5** | 0,8 | 5,0 |
| **R6** | 0,4 | 2,2 |
| **R7** | 0,4 | 1,8 |
| **R8** | 0,4 | 2,2 |
| **R9** | 0,5 | 3,2 |
| **R10** | 0,4 | 2,2 |
| **R11** | 0,3 | 1,9 |
| **R12** | 0,4 | 2,1 |
| **R13** | 0,2 | 1,1 |
| **R14** | 0,4 | 1,7 |
| **R15** | 0,4 | 1,9 |
| **R16** | 0,2 | 1,2 |
| **R17** | 0,3 | 1,5 |
| **R18** | 0,4 | 2,5 |
| **R19** | 0,4 | 2,5 |
| **R20** | 0,0 | 0,2 |
| **R21** | 0,0 | 0,2 |
| **R22** | 0,0 | 0,2 |
| **R23** | 0,1 | 0,3 |
| **R24** | 0,1 | 0,3 |
| **R25** | 0,1 | 0,3 |
| **R26** | 0,1 | 0,4 |
| **R27** | 0,1 | 0,4 |
| **R28** | 0,1 | 0,4 |
| **R29** | 0,1 | 0,4 |
| **R30** | 0,1 | 0,4 |
| **R31** | 0,1 | 0,5 |

**Tabla 85.: ** Resultados de MPS promedio anual y máximo mensual modeladas por el sistema CALPUFF.**

| Receptor | Concentración de MPS (mg/m2-día) |
| --- | --- |
| **Receptor** | **Promedio anual** |
| **R1** | 56,4 |
| **R2** | 39,5 |
| **R3** | 57,4 |
| **R4** | 35,4 |
| **R5** | 64,9 |
| **R6** | 24,8 |
| **R7** | 35,5 |
| **R8** | 25,0 |
| **R9** | 36,6 |
| **R10** | 26,6 |
| **R11** | 23,6 |
| **R12** | 22,2 |
| **R13** | 10,0 |
| **R14** | 31,0 |
| **R15** | 21,1 |
| **R16** | 19,1 |
| **R17** | 16,6 |
| **R18** | 32,2 |
| **R19** | 27,0 |
| **R20** | 0,0 |
| **R21** | 0,0 |
| **R22** | 0,0 |
| **R23** | 0,1 |
| **R24** | 0,1 |
| **R25** | 0,1 |
| **R26** | 0,1 |
| **R27** | 0,1 |
| **R28** | 0,2 |
| **R29** | 0,2 |
| **R30** | 0,1 |
| **R31** | 0,2 |
| **R32** | 0,2 |
| **R33** | 0,2 |
| **R34** | 0,2 |
| **R35** | 0,2 |

**Tabla 86.: ** Resultados de NO 2 promedio anual y percentil 99 de las máximas diarias concentraciones**

| Receptor | Concentración de NO (μg/Nm3)<br>2 | Col3 |
| --- | --- | --- |
| **Receptor** | **Promedio anual** | **Percentil 99 de las concentraciones 1**<br>**hora** |
| **R1** | 0,2 | 9,3 |
| **R2** | 0,1 | 6,8 |
| **R3** | 0,2 | 10,2 |
| **R4** | 0,1 | 6,5 |
| **R5** | 0,1 | 2,6 |
| **R6** | 0,0 | 2,9 |
| **R7** | 0,0 | 3,2 |
| **R8** | 0,1 | 2,5 |
| **R9** | 0,1 | 3,0 |
| **R10** | 0,0 | 2,9 |
| **R11** | 0,0 | 3,0 |
| **R12** | 0,0 | 2,5 |
| **R13** | 0,0 | 2,7 |
| **R14** | 0,1 | 2,8 |
| **R15** | 0,1 | 2,5 |
| **R16** | 0,1 | 2,3 |
| **R17** | 0,0 | 2,2 |
| **R18** | 0,0 | 2,2 |
| **R19** | 0,1 | 2,5 |
| **R20** | 0,0 | 9,6 |
| **R21** | 0,0 | 11,8 |
| **R22** | 0,0 | 6,6 |
| **R23** | 0,2 | 22,6 |
| **R24** | 0,2 | 23,7 |
| **R25** | 0,2 | 19,8 |
| **R26** | 0,2 | 25,7 |
| **R27** | 0,2 | 24,1 |
| **R28** | 0,3 | 17,5 |
| **R29** | 0,3 | 27,3 |
| **R30** | 0,2 | 23,7 |
| **R31** | 0,3 | 25,6 |

**Tabla 87.: ** Resultados de SO 2 promedio anual, percentil 99 de las concentraciones diarias y percentil**

| Receptor | Concentración de SO (μg/Nm3) - Estadística norma primaria<br>2 | Col3 | Col4 |
| --- | --- | --- | --- |
| **Receptor** | **Promedio anual** | **Percentil 99 de las**<br>**concentraciones 24 horas** | **Percentil 98,5 de las**<br>**concentraciones de 1 hora** |
| **R1** | 0,01 | 0,04 | 0,08 |
| **R2** | 0,01 | 0,04 | 0,07 |
| **R3** | 0,01 | 0,04 | 0,08 |
| **R4** | 0,01 | 0,05 | 0,08 |
| **R5** | 0,00 | 0,02 | 0,04 |
| **R6** | 0,00 | 0,02 | 0,03 |
| **R7** | 0,00 | 0,02 | 0,03 |
| **R8** | 0,00 | 0,02 | 0,03 |
| **R9** | 0,00 | 0,02 | 0,04 |
| **R10** | 0,00 | 0,02 | 0,03 |
| **R11** | 0,00 | 0,02 | 0,03 |
| **R12** | 0,00 | 0,01 | 0,03 |
| **R13** | 0,00 | 0,02 | 0,03 |
| **R14** | 0,00 | 0,01 | 0,03 |
| **R15** | 0,00 | 0,01 | 0,03 |
| **R16** | 0,00 | 0,01 | 0,03 |
| **R17** | 0,00 | 0,01 | 0,03 |
| **R18** | 0,00 | 0,01 | 0,03 |
| **R19** | 0,00 | 0,02 | 0,03 |
| **R20** | 0,00 | 0,02 | 0,02 |
| **R21** | 0,00 | 0,02 | 0,02 |
| **R22** | 0,00 | 0,02 | 0,02 |
| **R23** | 0,02 | 0,11 | 0,22 |
| **R24** | 0,01 | 0,10 | 0,22 |
| **R25** | 0,01 | 0,14 | 0,19 |
| **R26** | 0,01 | 0,13 | 0,22 |
| **R27** | 0,02 | 0,14 | 0,24 |

**Tabla 88.: ** Resultados de SO 2 promedio anual, percentil 99,7 de las concentraciones diarias y percentil**

| Receptor | Concentración de SO (μg/Nm3) - Estadística norma secundaria<br>2 | Col3 | Col4 |
| --- | --- | --- | --- |
| **Receptor** | **Promedio anual** | **Percentil 99,7 de las conc. 24**<br>**horas** | **Percentil 99,73 de las conc. 1**<br>**hora** |
| **R1** | 0,01 | 0,06 | 0,23 |
| **R2** | 0,01 | 0,06 | 0,21 |
| **R3** | 0,01 | 0,06 | 0,23 |
| **R4** | 0,01 | 0,07 | 0,22 |
| **R5** | 0,00 | 0,03 | 0,11 |
| **R6** | 0,00 | 0,03 | 0,10 |
| **R7** | 0,00 | 0,04 | 0,10 |
| **R8** | 0,00 | 0,02 | 0,09 |
| **R9** | 0,00 | 0,03 | 0,11 |
| **R10** | 0,00 | 0,03 | 0,11 |
| **R11** | 0,00 | 0,03 | 0,11 |
| **R12** | 0,00 | 0,02 | 0,09 |
| **R13** | 0,00 | 0,02 | 0,10 |
| **R14** | 0,00 | 0,02 | 0,07 |
| **R15** | 0,00 | 0,02 | 0,09 |
| **R16** | 0,00 | 0,02 | 0,07 |
| **R17** | 0,00 | 0,02 | 0,08 |
| **R18** | 0,00 | 0,02 | 0,08 |
| **R19** | 0,00 | 0,02 | 0,10 |
| **R20** | 0,00 | 0,03 | 0,11 |
| **R21** | 0,00 | 0,03 | 0,12 |
| **R22** | 0,00 | 0,03 | 0,12 |
| **R23** | 0,02 | 0,13 | 0,54 |
| **R24** | 0,01 | 0,16 | 0,54 |
| **R25** | 0,01 | 0,41 | 0,57 |
| **R26** | 0,01 | 0,20 | 0,55 |
| **R27** | 0,02 | 0,22 | 0,55 |
| **R28** | 0,02 | 0,26 | 0,77 |
| **R29** | 0,02 | 0,18 | 0,79 |
| **R30** | 0,02 | 0,38 | 0,63 |
| **R31** | 0,02 | 0,30 | 0,67 |
| **R32** | 0,02 | 0,19 | 1,02 |
| **R33** | 0,03 | 0,43 | 1,37 |
| **R34** | 0,02 | 0,33 | 1,37 |
| **R35** | 0,02 | 0,32 | 1,13 |
| **R36** | 0,02 | 0,34 | 1,16 |
| **R37** | 0,02 | 0,36 | 1,13 |

**Tabla 89.: ** Resultados de CO percentil 99 de las máximas diarias concentraciones de 8 y 1 horas**

| Receptor | Concentración de CO (μg/Nm3) | Col3 |
| --- | --- | --- |
| **Receptor** | **Percentil 99 de las conc. 8 horas** | **Percentil 99 de las conc. 1 hora** |
| **R1** | 5,5 | 27,8 |
| **R2** | 3,9 | 20,0 |
| **R3** | 6,0 | 31,4 |
| **R4** | 4,0 | 15,3 |
| **R5** | 1,3 | 4,6 |
| **R6** | 1,0 | 3,1 |
| **R7** | 0,9 | 3,6 |
| **R8** | 1,0 | 3,3 |
| **R9** | 1,4 | 5,8 |
| **R10** | 1,0 | 3,3 |
| **R11** | 1,0 | 3,3 |
| **R12** | 0,9 | 3,0 |
| **R13** | 0,8 | 2,5 |
| **R14** | 1,3 | 5,6 |
| **R15** | 1,1 | 3,5 |
| **R16** | 1,0 | 3,8 |
| **R17** | 0,8 | 2,7 |
| **R18** | 0,9 | 3,0 |
| **R19** | 1,0 | 3,1 |
| **R20** | 0,4 | 1,5 |
| **R21** | 0,5 | 1,4 |
| **R22** | 0,5 | 1,6 |
| **R23** | 1,8 | 8,7 |
| **R24** | 1,7 | 8,6 |
| **R25** | 2,8 | 8,3 |
| **R26** | 1,9 | 9,8 |
| **R27** | 2,1 | 10,9 |
| **R28** | 3,0 | 12,0 |
| **R29** | 2,3 | 10,2 |
| **R30** | 3,3 | 9,9 |
| **R31** | 4,0 | 17,3 |
| **R32** | 3,0 | 12,2 |
| **R33** | 5,1 | 22,2 |

**Tabla 90.: ** Resumen de los aportes de contaminantes atmosféricos que efectuará el Proyecto.**

| Fase/Aporte<br>Contaminante<br>(μg/m3N) | MP10 | Col3 | MP2,5 | Col5 | NO<br>2 | Col7 | SO<br>2 | Col9 | Col10 | CO | Col12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Fase/Aporte**<br>**Contaminante**<br>**(μg/m3N)** | **Conc.**<br>**anual** | **Conc. 24**<br>**horas** | **Conc.**<br>**anual** | **Conc. 24**<br>**horas** | **Conc.**<br>**anual** | **Conc.**<br>**horaria** | **Conc.**<br>**anual** | **Conc. 24**<br>**horas** | **Conc.**<br>**horaria** | **Conc. 8**<br>**horas** | **Conc.**<br>**horaria** |
| **Estación SAPU** | **Estación SAPU** | **Estación SAPU** | **Estación SAPU** | **Estación SAPU** | **Estación SAPU** | **Estación SAPU** | **Estación SAPU** | **Estación SAPU** | **Estación SAPU** | **Estación SAPU** | **Estación SAPU** |
| Construcción | 0,004 | 0,048 | 0,001 | 0,007 | 0,0008 | 0,075 | 0,0000 | 0,0009 | 0,0007 | 0,089 | 0,086 |
| % de la norma | 0,009 | 0,037 | 0,004 | 0,014 | 0,0008 | 0,019 | 0,0001 | 0,0006 | 0,0002 | 0,001 | 0,000 |
| **Estación Quinel** | **Estación Quinel** | **Estación Quinel** | **Estación Quinel** | **Estación Quinel** | **Estación Quinel** | **Estación Quinel** | **Estación Quinel** | **Estación Quinel** | **Estación Quinel** | **Estación Quinel** | **Estación Quinel** |
| Construcción | 0,004 | 0,046 | 0,001 | 0,007 | 0,0007 | 0,054 | 0,0001 | 0,0009 | 0,0006 | 0,084 | 0,073 |
| % de la norma | 0,008 | 0,035 | 0,004 | 0,014 | 0,0007 | 0,014 | 0,0001 | 0,0006 | 0,0002 | 0,001 | 0,000 |

**Tabla 91.: ** Estimación del impacto del Proyecto Parque Eólico Dañicalqui a las concentraciones de**

| Contaminante | Col2 | Concentración basal<br>Actual (μg/m3N) | Aporte Total del<br>proyecto (μg/m3N) | Total | Normativa<br>vigente | Porcentaje de<br>la norma |
| --- | --- | --- | --- | --- | --- | --- |
| MP10 | Concentración anual | 34,1 | 0,0043 | 34,1 | 50 | **68** |
| MP10 | Concentración 24 horas | 110,7 | 0,0484 | 110,7 | 150 | **74** |
| NO2 | Concentración anual | 10,4 | 0,0008 | 10,4 | 100 | **10** |
| NO2 | Concentración horaria | 86,6 | 0,0754 | 86,7 | 400 | **22** |
| SO2 | Concentración anual | 5,9 | 0,0000 | 5,9 | 60 | **10** |
| SO2 | Concentración 24 horas | 12,5 | 0,0009 | 12,5 | 150 | **8 ** |
| SO2 | Concentración horaria | 13 | 0,0007 | 13,0 | 350 | **4 ** |

**Tabla 92.: ** Estimación del impacto del Parque Eólico Dañicalqui a las concentraciones de MP10 y**

| Contaminante | Col2 | Concentración basal<br>Actual (μg/m3N) | Aporte Total del<br>proyecto (μg/m3N) | Total | Normativa<br>vigente | Porcentaje de<br>la norma |
| --- | --- | --- | --- | --- | --- | --- |
| MP10 | Concentración anual | 41,1 | 0,0042 | 41,1 | 50 | **82** |
| MP10 | Concentración 24 horas | 211,5 | 0,0460 | 211,5 | 150 | **141** |
| NO2 | Concentración anual | 14,4 | 0,0007 | 14,4 | 100 | **14** |
| NO2 | Concentración horaria | 95,9 | 0,0544 | 96,0 | 400 | **24** |

**Tabla 93.: ** **Distancias de caminos externos e internos con supresor de polvo en la** **fase** **de****

| Tipo Camino | Áreas con supresor Externo No Pavimentado | Distancia (m) |
| --- | --- | --- |
| **Externo** | **Acceso PE** | **Acceso PE** |
| **Externo** | Área supresor 1 | 523 |

**Tabla 94.: ** Periodicidad de ejecución**

| Tipo de actividad | Fase de construcción, frecuencia3 |
| --- | --- |
| Aplicación de Supresor de<br>Polvo caminos | Dos días, tres veces al año |

**Tabla 95.: ** Frecuencia de mantención**

| Tipo de actividad | Fase de construcción, frecuencia |
| --- | --- |
| Inspección Preventiva | Mensual |
| Mantención correctiva | Anual |
