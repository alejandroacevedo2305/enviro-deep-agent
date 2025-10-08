---
title: iembre 30 de 2011
author: Valeria P. Campos Bravo
date: D:20230515091050-04'00'
language: es
type: report
pages: 113
has_toc: False
has_tables: True
extraction_quality: high
---

**ESTIMACIÓN DE EMISIONES Y MODELACIÓN**

**ATMOSFÉRICA**

**PROYECTO ALBA**

_Preparado por:_

Abril, 2023

INFORME DE RESULTADOS

ATM037-23

**ESTIMACIÓN DE EMISIONES Y MODELACIÓN**

**ATMOSFÉRICA**

**PROYECTO ALBA**

|Versión del Documento|Col2|Col3|Col4|1|Col6|
|---|---|---|---|---|---|
|**_Responsable Elaboración_**|**_Responsable Elaboración_**|**_Responsable Revisión_**|**_Responsable Revisión_**|**_Responsable Aprobación_**|**_Responsable Aprobación_**|
|Nombre:|Nicolás Reinoso|Nombre|Stephanie Oviedo|Nombre|Mauricio Cifuentes|
|Cargo:|Ingeniero<br>Proyectos|Cargo|Jefe de Área|Cargo:|DAES|
|Fecha:|21-04-2023|Fecha:|21-04-2023|Fecha:|21-04-2023|
|Firma:||Firma:||Firma:||

Abril, 2023

**ÍNDICE DE CONTENIDOS**

1 Introducción ............................................................................................ 1
2 Objetivo ................................................................................................. 2
3 Alcances ................................................................................................. 2
4 Ubicación del Proyecto .............................................................................. 3
5 Marco Legal ............................................................................................ 5
6 Línea de Base .......................................................................................... 6
7 Meteorología de la Zona de Estudio ............................................................ 8
7.1 S ERIES DE T IEMPO ........................................................................................ 9

7.2 R OSAS DE V IENTO ....................................................................................... 11

7.3 C ICLO ESTACIONAL ...................................................................................... 13

7.4 C ICLO D IARIO V ELOCIDAD DEL V IENTO .............................................................. 14
8 Análisis Incertidumbre ............................................................................. 16
8.1 D ESCRIPCIÓN DE P ARÁMETROS E STADÍSTICOS ...................................................... 16

8.1.1 Media ................................................................................................. 16

8.1.2 Moda .................................................................................................. 16

8.1.3 Mediana .............................................................................................. 17
8.1.4 Desviación Estándar ............................................................................. 17
8.1.5 Raíz del Error Cuadrático Medio ............................................................. 17
8.1.6 Error Medio Cuadrático ......................................................................... 18
8.1.7 Sesgo ................................................................................................. 18
8.1.8 Coeficiente de correlación ..................................................................... 18
8.2 A NÁLISIS CUANTITATIVO ............................................................................... 19
9 Descripción del Proyecto .......................................................................... 20
10 Estimación de Emisiones del Proyecto ....................................................... 21
10.1 A CTIVIDADES E MISORAS ............................................................................... 21
10.2 M ÉTODO DE C ÁLCULO ................................................................................... 22
10.3 F ACTORES DE E MISIÓN ................................................................................. 23

10.4 P ESO P ROMEDIO ......................................................................................... 31

10.4.1 Peso Promedio Caminos Pavimentados ................................................ 31
10.5 N IVEL DE A CTIVIDAD E TAPA DE C ONSTRUCCIÓN .................................................... 36
10.5.1 Compactación .................................................................................. 36
10.5.2 Nivelación ........................................................................................ 36
10.5.3 Excavación ...................................................................................... 36
10.5.4 Carga y Descarga de Material ............................................................. 37
10.5.5 Tránsito de Vehículos por Tipo de Carpeta. .......................................... 37
10.5.6 Motor de Vehículos ........................................................................... 40
10.5.7 Motor de Maquinarias ........................................................................ 40
10.5.8 Grupo Electrógeno ............................................................................ 41
10.5.9 Fundición Sales Solares ..................................................................... 41
10.5.10 Combustión Gas Natural .................................................................... 42
10.5.11 Proyecto Adelaida ............................................................................. 42
10.6 N IVEL DE ACTIVIDAD E TAPA DE O PERACIÓN A CTUAL ............................................... 43
10.6.1 Tránsito de Vehículos por tipo de carpeta. ........................................... 43
10.6.2 Motor de Vehículos ........................................................................... 43

10.6.3 Emisiones Centrales .......................................................................... 44
10.6.4 Manejo de Carbón-Cancha Carbón ...................................................... 44
10.7 N IVEL DE ACTIVIDAD E TAPA DE O PERACIÓN CON P ROYECTO ...................................... 46
10.7.1 Tránsito de Vehículos por tipo de carpeta. ........................................... 46
10.7.2 Motor de Vehículos ........................................................................... 47

10.7.3 Emisiones Central Cochrane ............................................................... 47

_**Inventario y Modelación de Emisiones ATM037-23**_
_Proyecto Alba_

_Abril, 2023_

10.7.4 Demolición....................................................................................... 47
10.7.5 Manejo de Carbón-Cancha Carbón ...................................................... 48
10.7.6 Proyecto Adelaida ............................................................................. 50
10.8 N IVEL DE ACTIVIDAD E TAPA DE C IERRE .............................................................. 50
10.8.1 Tránsito de Vehículos por tipo de carpeta. ........................................... 50
10.8.2 Motor de Vehículos ........................................................................... 51
10.9 T ASAS DE E MISIÓN E SCENARIO CON P ROYECTO .................................................... 51
11 Modelación de Dispersión de Contaminantes .............................................. 56
11.1 M ODELO DE D ISPERSIÓN A TMOSFÉRICA .............................................................. 56
11.1.1 Base Teórica .................................................................................... 56
11.1.2 Sistema de Modelación WRF - CALPUFF ............................................... 56
11.2 V ARIABLES DE E NTRADA INGRESADOS AL S ISTEMA DE M ODELACIÓN ............................ 58
12 Resultados Modelación ............................................................................ 64

12.1 C AMPOS DE V IENTO ..................................................................................... 64
12.2 A PORTES O BTENIDOS DE LA M ODELACIÓN ........................................................... 69
12.2.1 Aporte en Puntos de Interés ............................................................... 69
12.2.2 Ajustes de Resultados de la Modelación por Incertidumbre .................... 73
12.3 A NÁLISIS DE C UMPLIMIENTO DE N ORMATIVA A MBIENTAL .......................................... 74

12.4 M APAS DE I SOCONCENTRACIONES .................................................................... 78

13 Conclusiones ........................................................................................ 105

**ÍNDICE DE FIGURAS**

Figura N° 1 Ubicación del Proyecto y Área de Modelación ............................................. 4
Figura N° 2 Serie temporal horaria velocidad del viento Estación Angamos I - Periodo
enero a diciembre 2021 ......................................................................................... 10
Figura N° 3 Frecuencia de ocurrencia dirección del viento Estación Angamos I - Periodo
enero a diciembre 2021 ......................................................................................... 10
Figura N° 4 Rosa de Viento Ciclo Completo Estación Angamos I Periodo enero a
diciembre 2021 .................................................................................................... 11
Figura N° 5 Variabilidad temporal del viento - Estación Angamos I Periodo enero a
diciembre 2021 .................................................................................................... 12
Figura N° 6 Variabilidad estacional del viento - Estación Angamos I Periodo 01 enero
2021 - 31 diciembre 2021 ..................................................................................... 13
Figura N° 7 Ciclos Diarios de Velocidad (m/s) y Dirección del Viento (°) Estación Angamos
I (Observado v/s Modelado) Periodo enero a diciembre 2021 ..................................... 15
Figura N° 8 Uso de Suelo ....................................................................................... 59
Figura N° 9 Topografía .......................................................................................... 61
Figura N° 10 Ubicación Puntos de Interés ................................................................ 63
Figura N° 11 Campos de Viento a las 00:00 horas. ................................................... 65
Figura N° 12 Campos de Viento a las 06:00 horas .................................................... 66
Figura N° 13 Campos de Viento a las 12:00 horas .................................................... 67
Figura N° 14 Campos de Viento a las 18:00 horas. ................................................... 68
Figura N° 16 Percentil 98 Promedio Diario de MP 10 Fase Construcción año 2 ................. 79
Figura N° 17 Promedio del Período de MP 10 Fase Construcción año 2 ........................... 80
Figura N° 18 Percentil 98 Promedio Diario de MP 2,5 Fase Construcción año 2 ................ 81
Figura N° 19 Promedio del Período de MP 2,5 Fase Construcción año 2 .......................... 82
Fuente: Algoritmos SpA, 2023Figura N° 20 Percentil 99 Promedio Diario de SO 2 Fase
Construcción año 2 ............................................................................................... 82
Figura N° 21 Percentil 98,5 Promedio Horario de SO 2 Fase Construcción año 2 ............. 84
Figura N° 22 Percentil 99,7 Promedio Diario de SO 2 Fase Construcción año 2 ............... 85

_**Inventario y Modelación de Emisiones ATM037-23**_
_Proyecto Alba_

_Abril, 2023_

Figura N° 23 Percentil 99,73 Promedio Horario de SO 2 Fase Construcción año 2 ........... 86
Figura N° 24 Promedio del Período de SO 2 Fase Construcción año 2 ............................ 87
Figura N° 25 Percentil 99 Máximo Horario de NO 2 Fase Construcción año 2 .................. 88
Figura N° 26 Promedio del Período de NO 2 Fase Construcción año 2 ............................ 89
Figura N° 27 Percentil 99 Máximo Horario de CO Fase Construcción año 2 ................... 90
Figura N° 28 Percentil 99 Máximo 8 Horas de CO Fase Construcción año 2 .................. 91
Figura N° 16 Percentil 98 Promedio Diario de MP 10 Fase Operación Con Proyecto .......... 92
Figura N° 17 Promedio del Período de MP 10 Fase Operación con Proyecto. .................... 93
Figura N° 18 Percentil 98 Promedio Diario de MP 2,5 Fase Operación con Proyecto .......... 94
Figura N° 19 Promedio del Período de MP 2,5 Fase Operación con Proyecto. ................... 95
Figura N° 20 Percentil 99 Promedio Diario de SO 2 Fase Operación con Proyecto. ........... 96
Figura N° 21 Percentil 98,5 Promedio Horario de SO 2 Fase Operación con Proyecto. ...... 97
Figura N° 22 Percentil 99,7 Promedio Diario de SO 2 Fase Operación con Proyecto. ........ 98
Figura N° 23 Percentil 99,73 Promedio Horario de SO 2 Fase Operación con Proyecto. .... 99
Figura N° 24 Promedio del Período de SO 2 Fase Operación con Proyecto. ................... 100
Figura N° 25 Percentil 99 Máximo Horario de NO 2 Fase Operación con Proyecto. ......... 101
Figura N° 26 Promedio del Período de NO 2 Fase Operación con Proyecto. ................... 102
Figura N° 27 Percentil 99 Máximo Horario de CO Fase Operación con Proyecto. .......... 103
Figura N° 28 Percentil 99 Máximo 8 Horas de CO Fase Operación con Proyecto. ......... 104

**ÍNDICE DE TABLAS**

Tabla N° 1 Coordenadas de los Vértices del Área de Modelación ................................... 1

Tabla N° 1 Normas de Calidad del Aire Consideradas en el Estudio .............................. 5
Tabla N° 2 Coordenadas de la Estación de monitoreo .................................................. 6
_Tabla N° 3 Línea de base de Calidad del Aire, Estación Jardín Infantil Integra_ ................. 6
_Tabla N° 4 Línea de base de Calidad del Aire, Estación Angamos I_ ................................ 6
_Tabla N° 5 Línea de base de Calidad del Aire, Estación Angamos II_ ............................... 7
Tabla N° 6 Localización de Referencia y Variables Meteorológicas Monitoreadas.............. 9
Tabla N° 7 Estadísticas de Datos Meteorológicos Monitoreados ..................................... 9
Tabla N° 8 Velocidad promedio del Viento en m/s ..................................................... 16
Tabla N° 9 Valores de los indicadores estadísticos observados y modelados ................. 19
Tabla N° 10 Estadígrafos de evaluación de desempeño del modelo Velocidad del Viento 19
Tabla N° 11 Principales actividades emisoras fase construcción, operación actual,
operación con proyecto y cierre. ............................................................................. 21
Tabla N° 12 Factores de Emisión Considerados en el Cálculo ...................................... 23
Tabla N° 13 Valores Considerados en los Factores de Emisión .................................... 27
Tabla N° 14 Peso Promedio Vehículos (t) en Caminos Pavimentados Fase de Construcción
.......................................................................................................................... 32
Tabla N° 15 Peso Promedio Vehículos (t) en Caminos No Pavimentados Fase de
Construcción ........................................................................................................ 33
Tabla N° 16 Peso Promedio Vehículos (t) en Caminos Pavimentados Fase de Operación
Actual ................................................................................................................. 34
Tabla N° 17 Peso Promedio Vehículos (t) en Caminos Pavimentados Fase de Operación
con Proyecto ........................................................................................................ 34
Tabla N° 18 Peso Promedio Vehículos (t) en Caminos Pavimentados Proyecto Adelaida 35
Tabla N° 19 Peso Promedio Vehículos (t) en Caminos Pavimentados Fase de Cierre ..... 35
Tabla N° 20 Nivel de Actividad Compactación (h/año) Fase Construcción-año 1 ............ 36
Tabla N° 21 Nivel de Actividad Nivelación (km) Fase Construcción-año 1 ..................... 36
Tabla N° 22 Nivel de Actividad Horas de Excavación (h/año) Fase Construcción-año 1 .. 36

_**Inventario y Modelación de Emisiones ATM037-23**_
_Proyecto Alba_

_Abril, 2023_

Tabla N° 23 Nivel de Actividad Carga y Descarga de material (t/año) Fase Construcción
año 1 y año 2 ....................................................................................................... 37
Tabla N° 24 Cálculo del Nivel de Actividad para Tránsito de Vehículos por Caminos
Pavimentados (veh-km/año) Fase Construcción Año 1 y 2 ......................................... 38
Tabla N° 25 Cálculo del Nivel de Actividad para Tránsito de Vehículos por Caminos No
Pavimentados (veh-km/año) Fase Construcción Año 1 y 2 ......................................... 39
Tabla N° 26 Cálculo del Nivel de Actividad para Motor de Maquinarias (h/año) Fase
Construcción- Año 1 y 2 ........................................................................................ 40
Tabla N° 27 Cálculo del Nivel de Actividad para Grupos Electrógenos Fase ConstrucciónAño 1 y 2 ............................................................................................................ 41
Tabla N° 28 Cálculo Fundición Sal Solar Fase Construcción-Año 2 ............................... 42
Tabla N° 29 Cálculo del Nivel de Actividad para consumo de combustible Gas Natural,
Fase Construcción-Año 2 ....................................................................................... 42
Tabla N° 30 Cálculo del Nivel de Actividad para Tránsito de Vehículos por Caminos
Pavimentados (veh-km/año) .................................................................................. 43
Tabla N° 31 Cálculo del Nivel de Actividad para Tránsito de Vehículos por Caminos
Pavimentados (veh-km/año) Fase Operación Actual .................................................. 43
Tabla N° 32 Emisiones Centrales, Situación Actual ................................................... 44
Tabla N° 33 Cálculo del Nivel de Actividad para Maquinaria en área de almacenamiento de
carbón, Situación Actual ....................................................................................... 44
Tabla N° 34 Cálculo del Nivel de Actividad para Combustión de Maquinarias (h/año)
Situación Actual ................................................................................................... 45
Tabla N° 35 Nivel de Actividad Carga y Descarga de Carbón(t/año), Situación Actual .... 45
Tabla N° 36 Nivel de Actividad transferencia de carbón en correas y torres (t/año),
situación actual .................................................................................................... 45
Tabla N° 37 Cálculo del Nivel de Actividad para Erosión Eólica, Situación Actual .......... 46
Tabla N° 38 Cálculo del Nivel de Actividad para Tránsito de Vehículos por Caminos
Pavimentados (veh-km/año) Fase Operación con Proyecto......................................... 46
Tabla N° 39 Emisiones Central Cochrane, situación futura ......................................... 47
Tabla N° 40 Cálculo del Nivel de Actividad para Demolición, Fase Operación con Proyecto
.......................................................................................................................... 48
Tabla N° 41 Cálculo del Nivel de Actividad para Maquinaria en área de almacenamiento de
carbón, Central Cochrane ...................................................................................... 48
Tabla N° 42 Cálculo del Nivel de Actividad para Combustión de Maquinarias (h/año) Fase
Operación con Proyecto. ........................................................................................ 48
Tabla N° 43 Nivel de Actividad Carga y Descarga de Carbón(t/año) ............................ 49
Tabla N° 44 Nivel de Actividad transferencia de carbón en correas y torres (t/año) ....... 49
Tabla N° 45 Cálculo del Nivel de Actividad para Erosión Eólica .................................... 49
Tabla N° 46 Cálculo del Nivel de Actividad para Tránsito de Vehículos por Caminos No
Pavimentados (veh-km/año), Fase Operación con proyecto. ...................................... 50
Tabla N° 47 Cálculo del Nivel de Actividad para Tránsito de Vehículos por Caminos
Pavimentados (veh-km/año) Fase de cierre ............................................................. 50
Tabla N° 48 Tasas de Emisión Fase Construcción Año 1 (t/año) .................................. 52
Tabla N° 49 Tasas de Emisión Fase Construcción Año 2 (t/año) .................................. 52
Tabla N° 50 Tasas de Emisión Fase Operación Actual (t/año) ..................................... 53
Tabla N° 51 Tasas de Emisión Fase Operación con Proyecto (t/año) ............................ 53
Tabla N° 52 Tasas de Emisión Fase Operación, Adelaida (t/año) ................................. 54
Tabla N° 53 Tasas de Emisión Fase Operación, Aerogeneradores (t/año) ..................... 54
Tabla N° 54 Tasas de Emisión Fase Operación con Proyecto, Alba-AdelaidaAerogeneradores (t/año) ....................................................................................... 54
Tabla N° 55 Tasas de Emisión Fase Cierre (t/año) .................................................... 55
Tabla N° 56 Características del Uso de Suelo ........................................................... 58

_**Inventario y Modelación de Emisiones ATM037-23**_
_Proyecto Alba_

_Abril, 2023_

Tabla N° 57 Localización Puntos Discretos ............................................................... 62
Tabla N° 58 Aporte de las fuentes de en Punto de interés, Fase Construcción Año 2 .... 70
Tabla N° 59 Aporte de las fuentes en Punto de interés, Fase Operación Actual ........... 70
Tabla N° 60 Aporte de Proyecto Alba en Punto de interés, Fase Operación con proyecto
(Sin Adelaida ni Aerogeneradores) .......................................................................... 71
Tabla N° 61 Aporte de Adelaida en Punto de interés, Fase Operación. ......................... 71
Tabla N° 62 Aporte de Aerogeneradores en Punto de interés, Fase Operación. ............. 72
Tabla N° 63 Aporte de Proyecto Alba en Punto de interés, Fase Operación con proyecto
(Con Adelaida y Aerogeneradores) .......................................................................... 72
Tabla N° 64 Análisis Normativo en Punto de interés, Fase Construcción Año 2 .............. 74
Tabla N° 65 Análisis Normativo en Punto de interés, Fase Operación Actual ................. 75
Tabla N° 66 Análisis Normativo en Punto de interés, Fase Operación con proyecto ........ 75
Tabla N° 67 Análisis Normativo en Punto de interés, Adelaida, Fase Operación ............. 76
Tabla N° 68 Análisis Normativo en Punto de interés, Aerogeneradores, Fase Operación . 76
Tabla N° 69 Análisis Normativo en Punto de interés, Alba, Adeliada y Aerogeneradores,
Fase Operación con proyecto ................................................................................. 77

_**Inventario y Modelación de Emisiones ATM037-23**_
_Proyecto Alba_

_Abril, 2023_

**1** **Introducción**

El proyecto Alba está localizado en la comuna de Mejillones, Región de Antofagasta
y tiene como objetivo el reemplazo del uso del carbón como insumo por sales
solares fundidas en la Central Termoeléctrica Angamos existente. Al comenzar a
funcionar el proyecto la Central Angamos deja de operar, y como consecuencia de
esto la cancha de carbón baja su utilización en un 50%.

El presente documento informa los resultados del inventario de emisiones en el
escenario de construcción, operación actual, operación con proyecto y cierre. La
fase de construcción tendrá una duración de 18 meses (año 1 y año 2). Asimismo,
la fase de operación actual se considera solamente el flujo operacional de la Planta,
el que corresponde a las labores de mantenimiento de los tanques, retiro de
residuos, vehículos livianos y camiones de carga, además de las emisiones de las
Centrales (Cochrane y Angamos) y su cancha de acopio de carbón. Finalmente, la
fase de Operación con proyecto considera flujo vehicular y acopio en cancha de
carbón además de la central Cochrane. Es importante mencionar que en la fase de
construcción (año 1 y año 2) y fase de operación con proyecto, se considera el
proyecto Adelaida y la actividad de acopio de partes y piezas de aerogeneradores,
el cual solo presenta flujo vehicular para su ejecución.

Además, se presentan los resultados de las concentraciones obtenidas al modelar
la dispersión atmosférica de material particulado respirable (MP 10 y MP 2,5 ), dióxido
de azufre (SO 2 ), dióxido de nitrógeno (NO 2 ) y monóxido de carbono (CO),
correspondiente a la fase de construcción año 2, fase de operación actual y fase de
operación con proyecto.

Adicionalmente, se informan los resultados de la modelación meteorológica
realizada con el modelo WRF y su validación, al comparar los resultados
meteorológicos modelados con los observados por una estación de monitoreo en
la zona de estudio.

El área de modelación corresponde a una grilla meteorológica de 72 km x 72 km,
un espaciamiento de 1 km y en cuyo interior se encuentra ubicado el sitio de
emplazamiento del Proyecto y los puntos de interés.

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

Fuente: Algoritmos SpA, 2022.

_**Inventario y Modelación de Emisiones ATM037-23**_ _1/106_
_Proyecto Alba_

_Abril, 2023_

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

**2** **Objetivo**

El objetivo de este documento corresponde a determinar las concentraciones y
aportes de las emisiones de MP 2,5, MP 10, CO, SO 2, NO 2 a percibirse en el entorno
del Proyecto Alba (Con Adelaida y Aerogeneradores).

**3** **Alcances**

✓ Estimar las emisiones de concentración de material particulado y gases

asociadas al Proyecto en la Etapa de Construcción (Año 1 y 2), Operación
Actual, Operación con Proyecto y Cierre.
✓ Realizar la modelación y validación del modelo WRF mediante la

comparación con datos monitoreados.
✓ Obtener aportes en concentración e isoconcentraciones de los
contaminantes normados SO 2, NO 2, CO, MP 10 y MP 2,5 con el sistema de

_**Inventario y Modelación de Emisiones ATM037-23**_ _2/106_
_Proyecto Alba_

_Abril, 2023_

modelación WRF-CALPUFF, en cada punto de interés ingresado al modelo,
para el escenario de construcción año 2, operación actual y operación con
proyecto (Con Adelaida y Aerogeneradores).

✓ Realizar un análisis normativo del aporte del proyecto.

**4** **Ubicación del Proyecto**

El proyecto Alba está localizado en la comuna de Mejillones, Región de
Antofagasta. La Figura N°1 siguiente muestra la ubicación espacial del
Proyecto.

_**Inventario y Modelación de Emisiones ATM037-23**_ _3/106_
_Proyecto Alba_

_Abril, 2023_

_**Figura N° 1**_
_**Ubicación del Proyecto y Área de Modelación**_

Fuente: Algoritmos SpA, 2023.

_**Inventario y Modelación de Emisiones ATM037-23**_ _4/106_
_Proyecto Alba_

_Abril, 2023_

**5** **Marco Legal**

Para determinar el aporte del proyecto respecto de la normativa ambiental se
consideraron las normas primarias y secundarias de calidad del aire definidas en la
legislación chilena.

La siguiente tabla presenta los valores límites de referencia para el análisis del
presente documento.

_**Tabla N° 2**_

_**Normas de Calidad del Aire Consideradas en el Estudio**_

|Parámetro|Tipo de<br>Norma|Estadístico|Valor|Referencia|
|---|---|---|---|---|
|MP10|Primaria|Promedio del<br>periodo|50g/m3N|D.S. N°45/02<br>MINSEGPRES|
|MP10|Primaria|Percentil 98 Diario|130g/m3N|D.S. N°59/98<br>MINSEGPRES|
|MP2,5|Primaria|Promedio del<br>periodo|20g/m3N|D.S. N°12/11 MMA|
|MP2,5|Primaria|Percentil 98 Diario|50g/m3N|D.S. N°12/11 MMA|
|SO2|Primaria|Promedio del<br>periodo|60g/m3N|D.S. N°104/18 MMA|
|SO2|Primaria|Percentil 99 Diario|150g/m3N|D.S. N°104/18 MMA|
|SO2|Primaria|Percentil 98,5<br>Horario|350g/m3N|D.S. N°104/18 MMA|
|SO2|Secundaria|Promedio del<br>periodo|80g/m3N|D.S. N°22/10<br>MINSEGPRES|
|SO2|Secundaria|Percentil 99,7 Diario|365g/m3N|D.S. N°22/10<br>MINSEGPRES|
|SO2|Secundaria|Percentil 99,73<br>Horario|1.000g/m3N|D.S. N°22/10<br>MINSEGPRES|
|NO2|Primaria|Promedio del<br>periodo|100g/m3N|D.S. N°114/02<br>MINSEGPRES|
|NO2|Primaria|Percentil 99 Horario|400g/m3N|D.S. N°114/02<br>MINSEGPRES|
|CO|Primaria|Percentil 99 8 horas|10.000<br>g/m3N|D.S. N°115/02<br>MINSEGPRES|
|CO|Primaria|Percentil 99 Horario|30.000<br>g/m3N|D.S. N°115/02<br>MINSEGPRES|

Fuente: Biblioteca del Congreso Nacional de Chile.

_**Inventario y Modelación de Emisiones ATM037-23**_ _5/106_
_Proyecto Alba_

_Abril, 2023_

**6** **Línea de Base**

Para caracterizar la línea de base de calidad del aire en el área del Proyecto se
considera las mediciones de material particulado y gases de las estaciones de
monitoreo cercanas al proyecto. Cabe destacar, que se consideran las estaciones
“Angamos I”, “Angamos II” y “Jardín Infantil Integra”, en donde en la última solo
se encuentra disponible el parámetro de dióxido de nitrógeno (NO 2 ) y, además, los
registros no se encuentran validados, la información es obtenida del Sistema de
Información Nacional de Calidad del Aire (SINCA).

La Tabla N° 3 muestra las especificaciones de las estaciones de monitoreo.

_**Tabla N° 3**_
_**Coordenadas de la Estación de monitoreo**_

|Estación|Coordenadas UTMa|Col3|Contaminante|Periodo evaluación|
|---|---|---|---|---|
|**Estación**|**Este (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|
|Jardín Infantil<br>Integra|352.064|7.444.407|NO2|Enero a diciembre del<br>2021|
|Angamos I|357.834|7.446.478|MP10- SO2 -NO2|Enero a diciembre del<br>2021|
|Angamos II|361.034|7.449.963|SO2|Enero a diciembre del<br>2021|

Fuente: Algoritmos 2023.

A continuación, se presentan los valores obtenidos de la línea de base de los
contaminantes monitoreados.

_**Tabla N° 4**_
_**Línea de base de Calidad del Aire, Estación Jardín Infantil Integra**_

|Parámetro|Tipo de Norma|Estadístico|Valora<br>(g/m3N)|Norma|% Norma|
|---|---|---|---|---|---|
|NO2|Primaria|Promedio del Periodo|3|100|3|
|NO2|Primaria|Percentil 99 Horario|29|400|7|

Fuente: Algoritmos 2023.

_**Tabla N° 5**_
_**Línea de base de Calidad del Aire, Estación Angamos I**_

|Parámetro|Tipo de Norma|Estadístico|Valora<br>(g/m3N)|Norma|% Norma|
|---|---|---|---|---|---|
|MP10|Primaria|Promedio del<br>periodo|23|50|46|
|MP10|Primaria|Percentil 98 Diario|39|130|30|

a Registros no validados, obtenidos del Sistema de Información Nacional de Calidad del Aire (SINCA).

_**Inventario y Modelación de Emisiones ATM037-23**_ _6/106_
_Proyecto Alba_

_Abril, 2023_

|Parámetro|Tipo de Norma|Estadístico|Valora<br>(g/m3N)|Norma|% Norma|
|---|---|---|---|---|---|
|SO2|Primaria|Promedio del<br>periodo|8|60|13|
|SO2|Primaria|Percentil 99 Diario|41|150|27|
|SO2|Primaria|Percentil 98,5<br>Horario|30|350|9|
|SO2|Secundaria|Promedio del<br>periodo|8|80|10|
|SO2|Secundaria|Percentil 99,7 Diario|55|365|15|
|SO2|Secundaria|Percentil 99,73<br>Horario|55|1.000|6|
|NO2|Primaria|Promedio del<br>periodo|7|100|7|
|NO2|Primaria|Percentil 99 Horario|44|400|11|

Fuente: Algoritmos 2023.

_**Tabla N° 6**_
_**Línea de base de Calidad del Aire, Estación Angamos II**_

|Parámetro|Tipo de Norma|Estadístico|Valora<br>(g/m3N)|Norma|% Norma|
|---|---|---|---|---|---|
|SO2|Primaria|Promedio del<br>periodo|7|60|12|
|SO2|Primaria|Percentil 99 Diario|26|150|17|
|SO2|Primaria|Percentil 98,5<br>Horario|32|350|9|
|SO2|Secundaria|Promedio del<br>periodo|7|80|9|
|SO2|Secundaria|Percentil 99,7 Diario|60|365|16|
|SO2|Secundaria|Percentil 99,73<br>Horario|85|1.000|9|

Fuente: Algoritmos 2023.

_**Inventario y Modelación de Emisiones ATM037-23**_ _7/106_
_Proyecto Alba_

_Abril, 2023_

**7** **Meteorología de la Zona de Estudio**

Las variables meteorológicas de mayor incidencia en la dispersión de las emisiones
atmosféricas generadas por el Proyecto fueron obtenidas por medio del modelo
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
geográfica, el sistema de pre-procesamiento, el modelo WRF-ARW y los sistemas
de post-procesamiento.

Las fuentes externas de datos contienen información necesaria para inicializar
WRF. Éstos corresponden a las observaciones convencionales o satélites de la
atmósfera. De estos datos se obtienen las condiciones iniciales y de borde para las
simulaciones del WRF. También es necesario entregarle datos sobre el terreno que
contengan información sobre la orografía, uso de suelo, relieve y vegetación, entre
otros.

Los modelos meteorológicos al representar una aproximación de la realidad tienen
asociados errores e incertidumbres, es por este motivo que los resultados
obtenidos mediante la modelación con WRF serán comparados con las variables
meteorológicas registradas por la estación Angamos I con el fin de evaluar la
capacidad predictiva del modelo.

La siguiente tabla presenta las coordenadas de localización y las variables
meteorológicas monitoreadas en la estación antes mencionada.

_**Inventario y Modelación de Emisiones ATM037-23**_ _8/106_
_Proyecto Alba_

_Abril, 2023_

_**Tabla N° 7**_
_**Localización de Referencia y Variables Meteorológicas Monitoreadas**_

|Estación|Coordenadas UTM|Col3|Variables|Periodo|
|---|---|---|---|---|
|**Estación**|**Este (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|
|Angamos I|357.834|7.446.478|Velocidad del viento<br>Dirección del viento|01 de enero al 31 de<br>diciembre 2021|

Fuente: Algoritmos, SpA 2023.

En las siguientes secciones se realiza un análisis comparativo entre la data
meteorológica registrada por las estaciones de monitoreo y lo simulado con WRF
para el periodo de registro, con resolución horaria para las variables meteorológicas
de velocidad y dirección de viento, ya que estos parámetros influyen directamente
en el fenómeno de dispersión de contaminantes.

**7.1** **Series de Tiempo**

La siguiente tabla muestra los porcentajes de datos válidos y de calmas
monitoreados por la Estación Angamos I. Respecto a la velocidad del viento se
consideró como calma los registros menores a 0,5 (m/s).

_**Tabla N° 8**_
_**Estadísticas de Datos Meteorológicos Monitoreados**_

|Estación|Datos<br>Totales|Porcentaje de Calma (%)|Col4|Porcentaje Datos<br>Válidos (%)|
|---|---|---|---|---|
|**Estación**|**Datos**<br>**Totales**|**Periodo**<br>**Diurno**|**Periodo**<br>**Nocturno**|**Periodo**<br>**Nocturno**|
|Angamos I|8.760|1%|3%|100%|

Fuente: Algoritmos SpA, 2023.

La serie temporal de la velocidad del viento registrada por la Estación Angamos I,
permiten un análisis cualitativo de los datos en términos de variabilidad, amplitud
de rango y frecuencia de los datos con que se cuenta. No se presentan las series
temporales generadas por el modelo WRF, ya que la información de pronóstico
dispone de la totalidad de los datos.

_**Inventario y Modelación de Emisiones ATM037-23**_ _9/106_
_Proyecto Alba_

_Abril, 2023_

_**Figura N° 2**_
_**Serie temporal horaria velocidad del viento**_
_**Estación Angamos I - Periodo enero a diciembre 2021**_

Fuente: Algoritmos SpA, 2023.

La serie temporal de la velocidad del viento registrada por la estación Angamos I
no muestra ciclo anual ya que se observa el mismo patrón a lo largo de todo el
año, con velocidades que varían alrededor de 5 m/s.

Con respecto a la dirección del viento, se identifican dos patrones dominantes. El
primero de ellos corresponde a vientos desde el Suroeste (SO) y Sur Suroeste
(SSO) correspondiendo a la línea centrada entre 180 y 240°. Por otro lado, se
observa un segundo patrón con vientos desde Norte (N), correspondiente a las
líneas centradas en 0 y 360°

_**Figura N° 3**_
_**Frecuencia de ocurrencia dirección del viento**_
_**Estación Angamos I - Periodo enero a diciembre 2021**_

Fuente: Algoritmos SpA, 2023.

_**Inventario y Modelación de Emisiones ATM037-23**_ _10/106_
_Proyecto Alba_

_Abril, 2023_

**7.2** **Rosas de Viento**

A continuación, se muestran los campos de viento anual y para diferentes periodos
del día, los que muestran la variabilidad temporal del viento durante el periodo
desde enero a diciembre del 2021 para la Estación Angamos I y la modelación
generada con WRF para dicha estación.

_**Figura N° 4**_
_**Rosa de Viento Ciclo Completo Estación Angamos I**_

_**Periodo enero a diciembre 2021**_

|Observado|Modelado|
|---|---|
|||

Fuente: Algoritmos SpA, 2023.

La rosa de viento del lado izquierdo de la figura anterior **¡Error! No se encuentra**
**el origen de la referencia.**, corresponde a los registros de la Estación Angamos
I en la cual se puede observar que prevalecen con mayor frecuencia vientos desde
el Sur Suroeste (SSO) y Suroeste (SSE), explicando en conjunto un 39% de la
frecuencia total. En menor medida se registran vientos desde el Norte (N) y Norte
Noroeste (NNO), explicando en conjunto un 30% de la frecuencia total.

Con respecto a lo modelado con WRF (lado derecho de la imagen anterior, se
obtiene el mismo patrón de vientos observados.

_**Inventario y Modelación de Emisiones ATM037-23**_ _11/106_
_Proyecto Alba_

_Abril, 2023_

_**Figura N° 5**_
_**Variabilidad temporal del viento - Estación Angamos I**_

_**Periodo enero a diciembre 2021**_

|Col1|00:00 - 05:00 horas|06:00 - 11:00 horas|12:00 - 17:00 horas|18:00 - 23:00 horas|
|---|---|---|---|---|
|**_Observado_**|||||
|**_Modelado_**||<br>|||

Fuente: Algoritmos SpA, 2023.

_**Inventario y Modelación de Emisiones ATM037-23**_ _12/106_
_Proyecto Alba_

_Abril, 2023_

Al observar el comportamiento espacial de los vientos en los diferentes periodos
del día para la Estación Angamos I se puede apreciar que, principalmente durante
el horario de madrugada y nocturno el viento dominante proviene desde el Sur
suroeste (SSO), mientras que duranta la tarde el viento proviene desde el norte
(N) y Norte Noreste (NNO), tanto en los datos observados como modelados.

**7.3** **Ciclo estacional**

La siguiente imagen muestra la evolución estacional y diaria de la velocidad y
dirección del viento, presentando en el eje “x” las horas del día y en el eje “y” los
meses del año. Es posible observar un marcado ciclo diario, correspondiendo a
vientos débiles en horas de la madrugada, con valores que varían entre 2 y 4 m/s
a lo largo de todo el año. Para el horario diurno, se observa un leve aumento entre
10:00 y 15:00 horas, con valores que alcanzan los 6 m/s, intensificando la
magnitud alrededor de las 17:00 y 21:00 horas. Respecto a los datos modelados,
se observa un patrón similar, sin embargo, la magnitud de la velocidad es menos
a la observada.

En cuanto a la dirección del viento observado por la estación Angamos I, se
obtienen vientos desde el Sur Suroeste (SSO) principalmente entre las 00:00 y
09:00 horas y 17:00 y 23:00 horas; y vientos desde el Norte (N) entre las 10:00
y 16:00 horas tanto en los datos observados como modelados.

_**Figura N° 6**_
_**Variabilidad estacional del viento - Estación Angamos I**_

_**Periodo 01 enero 2021 - 31 diciembre 2021**_

|Observado|Modelado|
|---|---|
|||

Fuente: Algoritmos SpA, 2023.

_**Inventario y Modelación de Emisiones ATM037-23**_ _13/106_
_Proyecto Alba_

_Abril, 2023_

**7.4** **Ciclo Diario Velocidad del Viento**

A continuación, se presentan los ciclos diarios promedio de la velocidad y dirección
del viento monitoreada por la Estación Angamos I y lo modelado con WRF para
dicha estación.

Al apreciar la curva de velocidad promedio para la Estación Angamos I (lado
izquierdo superior de la imagen siguiente), esta presenta una condición homogénea
a lo largo de la madrugada, con una velocidad en torno a 2 m/s, aumentando a
partir de las 09:00 horas hasta alcanzar dos máximos aparentes, el primero de
ellos alrededor de las 13:00 horas con un valor de 4,9 m/s y un segundo máximo
alrededor de las 19:00 horas alcanzando un valor de 5,6 m/s. De los datos
modelados se obtiene un ciclo similar, sin embargo, con valores subestimados.

Respecto de la dirección del viento observada en Estación Angamos I (parte inferior
izquierda de la imagen siguiente) se observa un marcado ciclo diario, con vientos
desde el Sur suroeste (SSO) entre las 00:00 y 09:00 horas y ente las 17:00 y
23:00 horas. Durante el horario de máxima velocidad del viento, este proviene
desde el Norte (N) y Norte Noroeste (NNO). Respecto a lo observado, este replica
el mismo patrón.

_**Inventario y Modelación de Emisiones ATM037-23**_ _14/106_
_Proyecto Alba_

_Abril, 2023_

_**Figura N° 7**_
_**Ciclos Diarios de Velocidad (m/s) y Dirección del Viento (°)**_

_**Estación Angamos I (Observado v/s Modelado)**_

_**Periodo enero a diciembre 2021**_

|Observado|Modelado|
|---|---|
|||

Fuente: Algoritmos SpA, 2023.

_**Inventario y Modelación de Emisiones ATM037-23**_ _15/106_
_Proyecto Alba_

_Abril, 2023_

**8** **Análisis Incertidumbre**

La siguiente tabla presenta las diferencias entre las observaciones y los pronósticos
de los valores promedios de velocidad de viento para la Estación Angamos I.

_**Tabla N° 9**_
_**Velocidad promedio del Viento en m/s**_

|Estación|Promedio<br>Observación|Promedio<br>Pronóstico WRF|% Sobrestimado<br>por pronóstico|
|---|---|---|---|
|Angamos I|3,66|2,87|-27|

Fuente: Algoritmos SpA, 2023.

Al comparar los ciclos diarios promedios observados y de pronóstico para la
Estación Angamos I, se obtiene que el modelo subestima los valores observados.
Esta situación genera condiciones desfavorables con respecto a la ventilación en el
área de interés, ya que la meteorología generada por el modelo WRF es utilizada
como dato de entrada para el modelo de dispersión CALPUFF. Debido a lo anterior,
no se realizará un ajuste a los resultados modelados debido a que esta
subestimación genera el escenario más desfavorable para la dispersión de
contaminantes en el área de interés.

**8.1** **Descripción de Parámetros Estadísticos**

**8.1.1** **Media**

Valor característico de una serie de datos cuantitativos, se obtiene a partir de la
suma de todos sus valores dividida entre el número de sumandos. Cuando el
[conjunto es una muestra aleatoria recibe el nombre de media muestral siendo uno](https://es.wikipedia.org/wiki/Muestra_aleatoria)
[de los principales estadísticos muestrales.](https://es.wikipedia.org/wiki/Estad%C3%ADstico)

###### 1

## 

_n_

###### x = _[x] i_ _n_

###### = n =

_i_

1

**8.1.2** **Moda**

Corresponde al valor que cuenta con una mayor frecuencia en una distribución de
datos, es decir, el número más repetido.

_**Inventario y Modelación de Emisiones ATM037-23**_ _16/106_
_Proyecto Alba_
_Abril, 2023_

**8.1.3** **Mediana**

La mediana es la medida más robusta, resistente y más común de la tendencia
central de la distribución de datos. A diferencia de la media no se ve afectada por
valores extremos que pudieran ser anómalos.

**8.1.4** **Desviación Estándar**

Corresponde a la raíz cuadrada de la diferencia media cuadrática entre el error de
pronóstico y el error de pronóstico promedio (E). Se utiliza para medir la cantidad
de variabilidad en el pronóstico de variables meteorológicas. Cuanto mayor sea el
valor de la SD, mayor será la variabilidad del pronóstico

Para realizar la validación de los datos registrados por la estación Camanchaca, se
calculan diferentes estadísticos clásicos tales como:

**8.1.5** **Raíz del Error Cuadrático Medio**

Corresponde al cálculo de la raíz cuadrada del promedio de las diferencias
cuadradas de cada uno de los valores del pronóstico y la observación. Este cálculo
permite ponderar los errores positivos y negativos, por lo cual en él están incluidos
los errores sistemáticos y aleatorios de los modelos.

Dónde:

X 1i : es el valor de la serie No 1

x 2i : es el valor de la serie No2

N: es el número de valores analizado

_**Inventario y Modelación de Emisiones ATM037-23**_ _17/106_
_Proyecto Alba_
_Abril, 2023_

**8.1.6** **Error Medio Cuadrático**

El error medio cuadrático entrega las medidas de las diferencias en promedio entre
los valores modelados y los observados. Está definido como:

**8.1.7** **Sesgo**

Proporciona información sobre la tendencia del modelo a sobreestimar o
subestimar una variable, cuantificando el error sistemático del modelo.

**8.1.8** **Coeficiente de correlación**

Nos permite establecer la relación lineal entre los modelos utilizados y la
observación y está acotada entre -1 y 1.

Si Corr < 0 significa que las dos variables se correlacionan en sentido inverso. A
valores altos de una de ellas le suelen corresponder valores bajos de la otra y
viceversa. Si Corr > 0 las dos variables se correlacionan en sentido directo.A
valores altos de una le corresponden valores altos de la otra. Si corr = 0 se dice
que las variables están incorrelacionadas por lo tanto no puede establecerse ningún
sentido de covariación.

_**Inventario y Modelación de Emisiones ATM037-23**_ _18/106_
_Proyecto Alba_
_Abril, 2023_

**8.2** **Análisis cuantitativo**

Tanto la velocidad como la dirección del viento son variables meteorológicas
relevantes para el análisis de los datos de entrada del modelo y al objeto de
observar la dirección de las masas de aire. Debido a lo anterior, a continuación, se
presenta los resultados obtenidos al aplicar los estadísticos a los datos observados
y modelados para la velocidad del viento en cada estación evaluada.

_**Tabla N° 10**_
_**Valores de los indicadores estadísticos observados y modelados**_

|Estadísticos|Unidad|Angamos I|Col4|
|---|---|---|---|
|**Estadísticos**|**Unidad**|**observado**|**modelado**|
|Media|m/s|3,63|2,87|
|Máximo|m/s|12,80|9,07|
|Mínimo|m/s|0,01|0,02|
|Moda|m/s|2,00|3,56|
|Mediana|m/s|3,40|2,85|
|Desviación estándar|--|2,04|1,61|

Fuente: Algoritmos SpA, 2023.

Para complementar el análisis cualitativo, se presenta en la siguiente tabla un
análisis cuantitativo de las variables velocidad del viento que compara los valores
observados y modelados por medio de la utilización de tres estadígrafos
comúnmente utilizados para la evaluación del desempeño de modelos; Sesgo, Error
Cuadrático Medio y el coeficiente de correlación (r).

A continuación, se los estadígrafos de evaluación de desempeño del modelo WRF
respecto a los datos monitoreados por la estación Angamos I.

_**Tabla N° 11**_
_**Estadígrafos de evaluación de desempeño del modelo**_

_**Velocidad del Viento**_

|Estación|Serie de datos|Medida de Error|Col4|Col5|
|---|---|---|---|---|
|**Estación**|**Serie de datos**|**Sesgo**|**RMSE**|**Corr**|
|Angamos I|Serie de Tiempo|-0,76|1,98|0,52|
|Angamos I|Ciclo Diario|-1,97|3,11|0,89|

Fuente: Algoritmos SpA, 2023.

_**Inventario y Modelación de Emisiones ATM037-23**_ _19/106_
_Proyecto Alba_
_Abril, 2023_

En base a lo anteriormente expuesto respecto de la meteorología, es posible
concluir que el modelo representa de manera satisfactoria la dinámica del viento
observado ya que este reproduce un ciclo anual de la velocidad junto a los patrones
en la dirección, sin embargo, este sobrestima los valores nocturnos. En relación
con los estadísticos evaluados, se obtiene un bajo sesgo, con un valor de error
igual a -0,76 para el ciclo diario. Finalmente, al evaluar la correlación, obtenemos
un valor superior a 0,5 tanto en la serie temporal anual como en el ciclo diario.

**9** **Descripción del Proyecto**

El proyecto Alba tiene como objetivo el reemplazo del uso del carbón como insumo
por sales solares fundidas en una planta termoeléctrica existente. Al comenzar a
funcionar el proyecto la central Angamos deja de operar, y como consecuencia de
esto la cancha de carbón baja su utilización en un 50%.

La fase de construcción tendrá una duración de 18 meses (año 1 y año 2).
Asimismo, la fase de operación considera solamente el flujo operacional de la
Central, el que corresponde a las labores de mantenimiento, retiro de residuos,
vehículos livianos y camiones de carga. Se consideraron además las emisiones de
la Central Cochrane. Finalmente, la fase de Operación con proyecto considera
principalmente flujo vehicular, además de la operación de la central Cochrane. Es
importante mencionar que en la fase de construcción (año 1 y año 2) y fase de
operación con proyecto, se considera el proyecto Adelaida, el cual solo presenta
flujo vehicular en su fase de operación y el proyecto de Aerogeneradores (anexo a
este proyecto), el cual solo considera flujo vehicular por caminos de diferentes
carpetas.

_**Inventario y Modelación de Emisiones ATM037-23**_ _20/106_
_Proyecto Alba_
_Abril, 2023_

**10** **Estimación de Emisiones del Proyecto**

**10.1** **Actividades Emisoras**

La Tabla N° 12 presenta las principales actividades emisoras de material
particulado respirable (MP 10 ), material particulado respirable fino (MP 2,5 ), dióxido
de azufre (SO 2 ), óxidos de nitrógeno (NO X ), monóxido de carbono (CO) y
compuestos orgánicos volátiles (COVs) para la fase de construcción, operación
actual, operación con proyecto y cierre.

**Tabla N° 12**
**Principales actividades emisoras fase construcción, operación actual,**

**operación con proyecto y cierre.**

|Fase|Actividades|
|---|---|
|Construcción|• <br>Compactación<br>• <br>Nivelación<br>• <br>Excavación<br>• <br>Carga y Descarga de material<br>• <br>Tránsito por camino pavimentado (incluye Aerogeneradores)<br>• <br>Tránsito por camino no pavimentado (incluye<br>Aerogeneradores)<br>• <br>Motor Vehículos<br>• <br>Maquinaria<br>• <br>Grupo Electrógeno<br>• <br>Fundición Sal Solar<br>• <br>Combustión Gas Natural<br>• <br>Proyecto Adelaida:<br>• <br>Tránsito camino pavimentado|
|Operación<br>actual|• <br>Tránsito por camino pavimentado<br>• <br>Motor Vehículos<br>• <br>Erosión Eólica<br>• <br>Centrales Angamos y Crochrane<br>• <br>Manejo del Carbón (Cancha Carbón)|
|Operación con<br>Proyecto|• <br>Tránsito por camino pavimentado (incluye Aerogeneradores)<br>• <br>Motor Vehículos<br>• <br>Erosión Eólica<br>• <br>Manejo del Carbón (Cancha Carbón)<br>• <br>Central Crochrane<br>• <br>Demolición<br>• <br>Proyecto Adelaida:<br>• <br>Tránsito camino pavimentado|
|Cierre|• <br>Tránsito por camino pavimentado<br>• <br>Motor Vehículos|

Fuente: Algoritmos SpA, 2023.

_**Inventario y Modelación de Emisiones ATM037-23**_ _21/106_
_Proyecto Alba_
_Abril, 2023_

**10.2** **Método de Cálculo**

La ecuación general para determinar las emisiones de cualquier actividad es
definida por la EPA como sigue a continuación.

E= Fe

 - Na· (1 −

Ea

(I)
100 ~~[)]~~

Dónde:

E : Emisión

Fe : Factor de emisión

Na : Nivel de actividad

Ea : Eficiencia de abatimiento

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

E SO 2 = 2 · CC· S comb (II)

Dónde:

E SO2 : Emisión SO 2 (kg/h)

CC : Consumo de combustible (kg/h)

S comb : Contenido de azufre del combustible (en peso m/m)

El contenido de azufre considerado para el cálculo de emisiones corresponde al
combustible Petróleo Diésel equivalente a 50 ppm (50/1.000.000 peso m/m).

Para determinar el consumo de combustible del motor de vehículos se considera la
velocidad de circulación de cada uno de ellos.

_**Inventario y Modelación de Emisiones ATM037-23**_ _22/106_
_Proyecto Alba_
_Abril, 2023_

**10.3** **Factores de Emisión**

Los factores de emisión para material particulado MP 10, MP 2,5 y MPS y gases NO x,
SO 2, CO y COV considerados en el cálculo, se presentan en la siguiente tabla.

_**Tabla N° 13**_
_**Factores de Emisión Considerados en el Cálculo**_

|Fuente<br>Emisora|Factor|Col3|Ref.|Unidad|Variables|
|---|---|---|---|---|---|
|Compactación|MP2.5<br>MPS|3,1<br>2<br>,1<br>60<br>,2<br>_H_<br>_f_<br>_k_<br><br><br><br>|(1)|kg/h|f: % de finos del<br>material|
|Compactación|MP10|4<br>,1<br>5<br>,1<br>45<br>,0<br>_H_<br>_f_<br>_k_<br><br><br><br>|4<br>,1<br>5<br>,1<br>45<br>,0<br>_H_<br>_f_<br>_k_<br><br><br><br>|4<br>,1<br>5<br>,1<br>45<br>,0<br>_H_<br>_f_<br>_k_<br><br><br><br>|H: %humedad<br>del material|
|Nivelación|MP10|k∙0,0056 ∙(V)2|(1)|Kg/km|k: Factor<br>tamaño de<br>partícula|
|Nivelación|MP2,5 <br>MPS|k∙0,0034 ∙(V)2,5|k∙0,0034 ∙(V)2,5|k∙0,0034 ∙(V)2,5|V: Velocidad<br>media de<br>Niveladora<br>(km/h)|
|Excavación|MP2,5|3,1<br>2<br>,1<br>60<br>,2<br>_H_<br>_f_<br>_k_<br><br><br><br>|(1)|kg/h|f: % de finos del<br>material|
|Excavación|MP10|4<br>,1<br>5<br>,1<br>45<br>,0<br>_H_<br>_f_<br>_k_<br><br><br><br>|4<br>,1<br>5<br>,1<br>45<br>,0<br>_H_<br>_f_<br>_k_<br><br><br><br>|4<br>,1<br>5<br>,1<br>45<br>,0<br>_H_<br>_f_<br>_k_<br><br><br><br>|H:% humedad<br>del material|
|Excavación|MPS|3,1<br>2<br>,1<br>60<br>,2<br>_H_<br>_f_<br>_k_<br><br><br><br>|3,1<br>2<br>,1<br>60<br>,2<br>_H_<br>_f_<br>_k_<br><br><br><br>|3,1<br>2<br>,1<br>60<br>,2<br>_H_<br>_f_<br>_k_<br><br><br><br>|k: Factor<br>tamaño de<br>partícula|
|Carga y<br>descarga de<br>material|MP10 <br>MP2,5 <br>MPS|4<br>,1<br>3,1<br>2<br>2,2<br>0016<br>,0<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>_H_<br>_u_<br>_k_<br>|(2)|kg/t|k: Factor<br>tamaño de<br>partícula|
|Fugitivas<br>caminos<br>pavimentados|MP10<br>MP2,5<br>MPS|[k ∙sL0,91 ∙(W ∙1,102311)1,02]|(3)|g/veh-km|sL: Carga de<br>fino de la<br>superficie<br>(g/m2)|
|Fugitivas<br>caminos<br>pavimentados|MP10<br>MP2,5<br>MPS|[k ∙sL0,91 ∙(W ∙1,102311)1,02]|(3)|g/veh-km|W: Peso<br>promedio del<br>camión (t)|
|Fugitivas<br>caminos<br>pavimentados|MP10<br>MP2,5<br>MPS|[k ∙sL0,91 ∙(W ∙1,102311)1,02]|(3)|g/veh-km|k: Factor<br>tamaño de<br>partícula|
|Fugitivas<br>caminos no<br>pavimentados|MP10<br>MP2,5|[k ∙281,9 ∙~~( ~~f<br>12)<br>0,9<br>∙~~( ~~W<br>2,7~~)~~<br>0,45<br>]|(2)|g/veh-km|f: % de finos del<br>material|
|Fugitivas<br>caminos no<br>pavimentados|MP10<br>MP2,5|[k ∙281,9 ∙~~( ~~f<br>12)<br>0,9<br>∙~~( ~~W<br>2,7~~)~~<br>0,45<br>]|(2)|g/veh-km|W: Peso<br>promedio del<br>camión|
|Fugitivas<br>caminos no<br>pavimentados|MPS|[k ∙281,9 ∙~~( ~~f<br>12)<br>0,7<br>∙~~( ~~W<br>2,7)<br>0,45<br>]|[k ∙281,9 ∙~~( ~~f<br>12)<br>0,7<br>∙~~( ~~W<br>2,7)<br>0,45<br>]|[k ∙281,9 ∙~~( ~~f<br>12)<br>0,7<br>∙~~( ~~W<br>2,7)<br>0,45<br>]|k: Factor<br>tamaño de<br>partícula|
|Motor de<br>camiones<br>pesados diésel<br>tipo 3 (EURO<br>III)|MP10 <br>MP2,5 <br>MPS|((0,10+(0,42*exp(((-<br>1)*0,04)*V)))+(0,86*<br>exp(((-1)*0,16)*V)))|(4)|g/veh-km<br>|V: Velocidad<br>camión (km/h)|
|Motor de<br>camiones<br>pesados diésel<br>tipo 3 (EURO<br>III)|SO2 <br>(CC)|((199,10+(496,04*exp(((-<br>1)*0,05)*V)))+|((199,10+(496,04*exp(((-<br>1)*0,05)*V)))+|((199,10+(496,04*exp(((-<br>1)*0,05)*V)))+|((199,10+(496,04*exp(((-<br>1)*0,05)*V)))+|

_**Inventario y Modelación de Emisiones ATM037-23**_ _23/106_
_Proyecto Alba_
_Abril, 2023_

|Fuente<br>Emisora|Factor|Col3|Ref.|Unidad|Variables|
|---|---|---|---|---|---|
|||(3.798,31*exp(((-<br>1)*0,57)*V)))||||
||CO|(1,25+(103,70/(1+exp((((-<br>1)*-1,39)+ <br>(0,54*ln(V)))+(0,04*V)))))|(1,25+(103,70/(1+exp((((-<br>1)*-1,39)+ <br>(0,54*ln(V)))+(0,04*V)))))|(1,25+(103,70/(1+exp((((-<br>1)*-1,39)+ <br>(0,54*ln(V)))+(0,04*V)))))|(1,25+(103,70/(1+exp((((-<br>1)*-1,39)+ <br>(0,54*ln(V)))+(0,04*V)))))|
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
||||(4)|||

_**Inventario y Modelación de Emisiones ATM037-23**_ _24/106_
_Proyecto Alba_
_Abril, 2023_

|Fuente<br>Emisora|Factor|Col3|Ref.|Unidad|Variables|
|---|---|---|---|---|---|
|<br>Motor de<br>maquinarias|MP10 <br>MP2,5 <br>MPS <br>CO <br>NOx <br>COV|E= FEaj∙FC∙P <br>FEaj= FEEE∙TAF∙FD <br>FD= 1+ A <br>FEajMP10= FEaj−SMPaj <br>FEajMP2,5= FEajMP10∙0, 97 <br>SMPaj= BSCF∙7∙soxcnv∙0, 01<br>∙(soxbas<br>−soxdsl) <br>FE SO2 = (BSCF∙(1 −soxcnv)<br>−FEHCaj) ∙0,01<br>∗soxdsl∙2||g/h|FEaj: Factor de<br>Emisión<br>Ajustado (g/kW-<br>h)|
|<br>Motor de<br>maquinarias|MP10 <br>MP2,5 <br>MPS <br>CO <br>NOx <br>COV|E= FEaj∙FC∙P <br>FEaj= FEEE∙TAF∙FD <br>FD= 1+ A <br>FEajMP10= FEaj−SMPaj <br>FEajMP2,5= FEajMP10∙0, 97 <br>SMPaj= BSCF∙7∙soxcnv∙0, 01<br>∙(soxbas<br>−soxdsl) <br>FE SO2 = (BSCF∙(1 −soxcnv)<br>−FEHCaj) ∙0,01<br>∗soxdsl∙2||g/h|FC: Factor de<br>Carga|
|<br>Motor de<br>maquinarias|MP10 <br>MP2,5 <br>MPS <br>CO <br>NOx <br>COV|E= FEaj∙FC∙P <br>FEaj= FEEE∙TAF∙FD <br>FD= 1+ A <br>FEajMP10= FEaj−SMPaj <br>FEajMP2,5= FEajMP10∙0, 97 <br>SMPaj= BSCF∙7∙soxcnv∙0, 01<br>∙(soxbas<br>−soxdsl) <br>FE SO2 = (BSCF∙(1 −soxcnv)<br>−FEHCaj) ∙0,01<br>∗soxdsl∙2||g/h|P: Potencia de la<br>maquina (kw)|
|<br>Motor de<br>maquinarias|MP10 <br>MP2,5 <br>MPS <br>CO <br>NOx <br>COV|E= FEaj∙FC∙P <br>FEaj= FEEE∙TAF∙FD <br>FD= 1+ A <br>FEajMP10= FEaj−SMPaj <br>FEajMP2,5= FEajMP10∙0, 97 <br>SMPaj= BSCF∙7∙soxcnv∙0, 01<br>∙(soxbas<br>−soxdsl) <br>FE SO2 = (BSCF∙(1 −soxcnv)<br>−FEHCaj) ∙0,01<br>∗soxdsl∙2||g/h|FEEE: Factor de<br>Emisión en<br>Estado<br>Estacionario de<br>Equipo Nuevo<br>(g/kW-h)|
|<br>Motor de<br>maquinarias|MP10 <br>MP2,5 <br>MPS <br>CO <br>NOx <br>COV|E= FEaj∙FC∙P <br>FEaj= FEEE∙TAF∙FD <br>FD= 1+ A <br>FEajMP10= FEaj−SMPaj <br>FEajMP2,5= FEajMP10∙0, 97 <br>SMPaj= BSCF∙7∙soxcnv∙0, 01<br>∙(soxbas<br>−soxdsl) <br>FE SO2 = (BSCF∙(1 −soxcnv)<br>−FEHCaj) ∙0,01<br>∗soxdsl∙2||g/h|TAF: Factor de<br>ajuste<br>transiente|
|<br>Motor de<br>maquinarias|MP10 <br>MP2,5 <br>MPS <br>CO <br>NOx <br>COV|E= FEaj∙FC∙P <br>FEaj= FEEE∙TAF∙FD <br>FD= 1+ A <br>FEajMP10= FEaj−SMPaj <br>FEajMP2,5= FEajMP10∙0, 97 <br>SMPaj= BSCF∙7∙soxcnv∙0, 01<br>∙(soxbas<br>−soxdsl) <br>FE SO2 = (BSCF∙(1 −soxcnv)<br>−FEHCaj) ∙0,01<br>∗soxdsl∙2||g/h|FD: Factor de<br>deterioro|
|<br>Motor de<br>maquinarias|MP10 <br>MP2,5 <br>MPS <br>CO <br>NOx <br>COV|E= FEaj∙FC∙P <br>FEaj= FEEE∙TAF∙FD <br>FD= 1+ A <br>FEajMP10= FEaj−SMPaj <br>FEajMP2,5= FEajMP10∙0, 97 <br>SMPaj= BSCF∙7∙soxcnv∙0, 01<br>∙(soxbas<br>−soxdsl) <br>FE SO2 = (BSCF∙(1 −soxcnv)<br>−FEHCaj) ∙0,01<br>∗soxdsl∙2||g/h|A: Factor<br>empírico “A” del<br>factor de<br>deterioro|
|<br>Motor de<br>maquinarias|MP10 <br>MP2,5 <br>MPS <br>CO <br>NOx <br>COV|E= FEaj∙FC∙P <br>FEaj= FEEE∙TAF∙FD <br>FD= 1+ A <br>FEajMP10= FEaj−SMPaj <br>FEajMP2,5= FEajMP10∙0, 97 <br>SMPaj= BSCF∙7∙soxcnv∙0, 01<br>∙(soxbas<br>−soxdsl) <br>FE SO2 = (BSCF∙(1 −soxcnv)<br>−FEHCaj) ∙0,01<br>∗soxdsl∙2||g/h|SMPaj: Ajuste de<br>MP por<br>contenido de<br>Azufre (g/kW-h)|
|<br>Motor de<br>maquinarias|MP10 <br>MP2,5 <br>MPS <br>CO <br>NOx <br>COV|E= FEaj∙FC∙P <br>FEaj= FEEE∙TAF∙FD <br>FD= 1+ A <br>FEajMP10= FEaj−SMPaj <br>FEajMP2,5= FEajMP10∙0, 97 <br>SMPaj= BSCF∙7∙soxcnv∙0, 01<br>∙(soxbas<br>−soxdsl) <br>FE SO2 = (BSCF∙(1 −soxcnv)<br>−FEHCaj) ∙0,01<br>∗soxdsl∙2||g/h|BSCF: Consumo<br>especifico de<br>combustible de<br>freno (g/kW-h)|
|<br>Motor de<br>maquinarias|MP10 <br>MP2,5 <br>MPS <br>CO <br>NOx <br>COV|E= FEaj∙FC∙P <br>FEaj= FEEE∙TAF∙FD <br>FD= 1+ A <br>FEajMP10= FEaj−SMPaj <br>FEajMP2,5= FEajMP10∙0, 97 <br>SMPaj= BSCF∙7∙soxcnv∙0, 01<br>∙(soxbas<br>−soxdsl) <br>FE SO2 = (BSCF∙(1 −soxcnv)<br>−FEHCaj) ∙0,01<br>∗soxdsl∙2||g/h|7: Ratio en<br>gramos de<br>sulfato en el MP<br>por gramos de<br>azufre en el MP|
|<br>Motor de<br>maquinarias|MP10 <br>MP2,5 <br>MPS <br>CO <br>NOx <br>COV|E= FEaj∙FC∙P <br>FEaj= FEEE∙TAF∙FD <br>FD= 1+ A <br>FEajMP10= FEaj−SMPaj <br>FEajMP2,5= FEajMP10∙0, 97 <br>SMPaj= BSCF∙7∙soxcnv∙0, 01<br>∙(soxbas<br>−soxdsl) <br>FE SO2 = (BSCF∙(1 −soxcnv)<br>−FEHCaj) ∙0,01<br>∗soxdsl∙2||g/h|Soxcnv : Ratio<br>de gramos de<br>azufre en MP<br>por gramos de<br>azufre en<br>combustible|
|<br>Motor de<br>maquinarias|MP10 <br>MP2,5 <br>MPS <br>CO <br>NOx <br>COV|E= FEaj∙FC∙P <br>FEaj= FEEE∙TAF∙FD <br>FD= 1+ A <br>FEajMP10= FEaj−SMPaj <br>FEajMP2,5= FEajMP10∙0, 97 <br>SMPaj= BSCF∙7∙soxcnv∙0, 01<br>∙(soxbas<br>−soxdsl) <br>FE SO2 = (BSCF∙(1 −soxcnv)<br>−FEHCaj) ∙0,01<br>∗soxdsl∙2||g/h|0,01 :<br>Conversión de<br>porcentaje a<br>fracción|
|<br>Motor de<br>maquinarias|MP10 <br>MP2,5 <br>MPS <br>CO <br>NOx <br>COV|E= FEaj∙FC∙P <br>FEaj= FEEE∙TAF∙FD <br>FD= 1+ A <br>FEajMP10= FEaj−SMPaj <br>FEajMP2,5= FEajMP10∙0, 97 <br>SMPaj= BSCF∙7∙soxcnv∙0, 01<br>∙(soxbas<br>−soxdsl) <br>FE SO2 = (BSCF∙(1 −soxcnv)<br>−FEHCaj) ∙0,01<br>∗soxdsl∙2||g/h|Soxbas :<br>Contenido de<br>azufre del<br>combustible<br>utilizado en la<br>certificación [%]|
|<br>Motor de<br>maquinarias|MP10 <br>MP2,5 <br>MPS <br>CO <br>NOx <br>COV|E= FEaj∙FC∙P <br>FEaj= FEEE∙TAF∙FD <br>FD= 1+ A <br>FEajMP10= FEaj−SMPaj <br>FEajMP2,5= FEajMP10∙0, 97 <br>SMPaj= BSCF∙7∙soxcnv∙0, 01<br>∙(soxbas<br>−soxdsl) <br>FE SO2 = (BSCF∙(1 −soxcnv)<br>−FEHCaj) ∙0,01<br>∗soxdsl∙2||g/h|Soxdsl:<br>Contenido de|

_**Inventario y Modelación de Emisiones ATM037-23**_ _25/106_
_Proyecto Alba_
_Abril, 2023_

|Fuente<br>Emisora|Factor|Col3|Ref.|Unidad|Variables|
|---|---|---|---|---|---|
||||||azufre del<br>combustible<br>utilizado por el<br>usuario [%]|
|Grupo<br>electrógeno<br>menor 600 HP|MP2,5 <br>MP10 <br>MPS|0,006078|(4)|kg/kg-<br>combusti<br>ble<br>|--|
|Grupo<br>electrógeno<br>menor 600 HP|NOx|0,086470|0,086470|0,086470|0,086470|
|Grupo<br>electrógeno<br>menor 600 HP|CO|0,018627|0,018627|0,018627|0,018627|
|Grupo<br>electrógeno<br>menor 600 HP|SO2|0,005686|0,005686|0,005686|0,005686|
|Grupo<br>electrógeno<br>menor 600 HP|COV|0,007060|0,007060|0,007060|0,007060|
|Demolición|MP10|1,0|(5)|kg/m2-<br>año|-|
|Demolición|MP2.5|0,1|0,1|0,1|0,1|
|Demolición|MPS|1,0|1,0|1,0|1,0|
|Erosión Eólica|MP10 <br>MP2,5<br>MPS|k∙~~( ~~s<br>1, 5~~)~~ ∙~~( ~~f<br>15)|(4)|kg/día-ha|k: Factor<br>tamaño de<br>partícula|
|Erosión Eólica|MP10 <br>MP2,5<br>MPS|k∙~~( ~~s<br>1, 5~~)~~ ∙~~( ~~f<br>15)|(4)|kg/día-ha|s: Contenido de<br>fino del material<br>(%)|
|Erosión Eólica|MP10 <br>MP2,5<br>MPS|k∙~~( ~~s<br>1, 5~~)~~ ∙~~( ~~f<br>15)|(4)|kg/día-ha|f: Porcentaje del<br>tiempo que el<br>viento excede<br>los 5,4 m/s|

(1) Factor obtenido desde AP42, 5th Edition: Capítulo 11, sección 11.9 “Western Surface Coal Mining”
(2) Factor obtenido desde AP42, 5th Edition: Capítulo 13, sección 13.2.4 “Aggregate Handling and Storage Piles”
(3) Factor obtenido desde AP42, 5th Edition: Capítulo 13, sección 13.2.1 “Paved Road”
(4) Factor obtenido desde Manual para el desarrollo de inventarios de emisiones atmosféricas (MMA 2017)
(5) Factor obtenido desde Guía para la Estimación de Emisiones Atmosféricas en la Región Metropolitana (2020)
(6) Factor obtenido desde AP42, 5th Edition: Capítulo 13, sección 13.2.2 “Unpaved Road”

_**Inventario y Modelación de Emisiones ATM037-23**_ _26/106_
_Proyecto Alba_
_Abril, 2023_

En la siguiente tabla se presentan los valores considerados en aquellos factores de
emisión que poseen variables para el escenario de estudio.

_**Tabla N° 14**_
_**Valores Considerados en los Factores de Emisión**_

|Fuente Emisora|Variables|Valor|Ref.|
|---|---|---|---|
|Compactación|k: Factor tamaño de partícula MP2,5|0,105|(7)|
|Compactación|k: Factor tamaño de partícula MP10|0,750|(7)|
|Compactación|k: Factor tamaño de partícula MPS|1,00|(7)|
|Compactación|f: % de finos del material|8,5|(8)|
|Compactación|H: % humedad del material|6,5|(8)|
|Nivelación|k: Factor tamaño de partícula MP2,5|0,031|(7)|
|Nivelación|k: Factor tamaño de partícula MP10|0,600|(7)|
|Nivelación|k: Factor tamaño de partícula MPS|1,000|(7)|
|Nivelación|V: Velocidad media de niveladora (km/h)|11,4|(8)|
|Excavación|k: Factor tamaño de partícula MP2,5|0,105|(7)|
|Excavación|k: Factor tamaño de partícula MP10|0,75|(7)|
|Excavación|k: Factor tamaño de partícula MPS|1,00|(7)|
|Excavación|f: % de finos del material|8,5|(8)|
|Excavación|H: % humedad del material|6,5|(8)|
|Carga y descarga de<br>material|k: Factor tamaño de partícula MP2,5|0,053|(9)|
|Carga y descarga de<br>material|k: Factor tamaño de partícula MP10|0,350|(9)|
|Carga y descarga de<br>material|k: Factor tamaño de partícula MPS|0,740|(9)|
|Carga y descarga de<br>material|H: Humedad del material (%)|6,5|(8)|
|Carga y descarga de<br>material|u: Velocidad del viento (m/s)|5,0|(8)|
|Fugitivas caminos<br>pavimentados|k: Factor tamaño de partícula MP2,5|0,15|(10)|
|Fugitivas caminos<br>pavimentados|k: Factor tamaño de partícula MP10|0,62|(10)|
|Fugitivas caminos<br>pavimentados|k: Factor tamaño de partícula MPS|3,23|(10)|
|Fugitivas caminos<br>pavimentados|f: % de finos del material caminos interiores y<br>acceso|0,7|(8)|
|Fugitivas caminos<br>pavimentados|W: Peso promedio flota camiones|-|(11)|
||k: Factor tamaño de partícula MP2,5|0,15|(10)|

_**Inventario y Modelación de Emisiones ATM037-23**_ _27/106_
_Proyecto Alba_
_Abril, 2023_

|Fuente Emisora|Variables|Valor|Ref.|
|---|---|---|---|
|Fugitivas caminos no<br>pavimentados|k: Factor tamaño de partícula MP10|1,50|(10)|
|Fugitivas caminos no<br>pavimentados|k: Factor tamaño de partícula MPS|4,90|(10)|
|Fugitivas caminos no<br>pavimentados|f: % de finos del material|8,5|(8)|
|Fugitivas caminos no<br>pavimentados|W: Peso promedio flota camiones|-|(11)|
|Erosión Eólica|k: Factor tamaño de partícula MP10|0,953|(12)|
|Erosión Eólica|k: Factor tamaño de partícula MP2,5|0,146|(12)|
|Erosión Eólica|k: Factor tamaño de partícula MPS|0,953|(12)|
|Erosión Eólica|s: Contenido de fino del material (%)|8,5|(8)|
|Erosión Eólica|f: Porcentaje del tiempo que el viento excede los<br>5,4 m/s|3,2|(14)|
|Motor de Maquinarias|FEee: Factor Emisión >56 a 75 kw MP10 -MPS<br>(g/kw-h) Tier 3|0,40|(12)|
|Motor de Maquinarias|FEee: Factor Emisión >75 a 130 kw MP10 -MPS<br>(g/kw-h) Tier 3|0,30|(12)|
|Motor de Maquinarias|FEee: Factor Emisión >130 a 225 kw MP10 -MPS<br>(g/kw-h) Tier 3|0,20|(12)|
|Motor de Maquinarias|FEee: Factor Emisión >225 a 450 kw MP10 -MPS<br>(g/kw-h) Tier 3|0,20|(12)|
|Motor de Maquinarias|FEee: Factor Emisión >56 a 75 kw MP2,5 (g/kw-h)<br>Tier 3|0,39|(12)|
|Motor de Maquinarias|FEee: Factor Emisión >75 a 130 kw MP2,5 (g/kw-<br>h) Tier 3|0,29|(12)|
|Motor de Maquinarias|FEee: Factor Emisión >130 a 225 kw MP2,5 (g/kw-<br>h)|0,19|(12)|
|Motor de Maquinarias|FEee: Factor Emisión >225 a 450 kw MP2,5 (g/kw-<br>h) Tier 3|0,19|(12)|
|Motor de Maquinarias|FEee: Factor Emisión >56 a 75 kw NOX (g/kw-h)<br>Tier 3|4,00|(12)|
|Motor de Maquinarias|FEee: Factor Emisión >75 a 130 kw NOX (g/kw-h)<br>Tier 3|3,00|(12)|
|Motor de Maquinarias|FEee: Factor Emisión >130 a 225 kw NOX (g/kw-<br>h) Tier 3|3,00|(12)|
|Motor de Maquinarias|FEee: Factor Emisión >225 a 450 kw NOX (g/kw-<br>h) Tier 3|3,00|(12)|
|Motor de Maquinarias|FEee: Factor Emisión >56 a 75 kw CO (g/kw-h)<br>Tier 3|3,20|(12)|
|Motor de Maquinarias|FEee: Factor Emisión >75 a 130 kw CO (g/kw-h)<br>Tier 3|1,20|(12)|
|Motor de Maquinarias|FEee: Factor Emisión >130 a 225 kw CO (g/kw-h)<br>Tier 3|1,00|(12)|
|Motor de Maquinarias|FEee: Factor Emisión >225 a 450 kw CO (g/kw-h)<br>Tier 3|1,10|(12)|
|Motor de Maquinarias|FEee: Factor Emisión >56 a 75 kw HC (g/kw-h)<br>Tier 3|0,2|(12)|
|Motor de Maquinarias|FEee: Factor Emisión >75 a 130 kw HC (g/kw-h)<br>Tier 3|0,2|(12)|

_**Inventario y Modelación de Emisiones ATM037-23**_ _28/106_
_Proyecto Alba_
_Abril, 2023_

|Fuente Emisora|Variables|Valor|Ref.|
|---|---|---|---|
||FEee: Factor Emisión >130 a 225 kw HC (g/kw-h)<br>Tier 3|0,2|(12)|
||FEee: Factor Emisión >225 a 450 kw HC (g/kw-h)<br>Tier 3|0,2|(12)|
||C: Factor de Carga|0,59<br>0,21|(12)|
||TAF: Factor de ajuste transiente MP2,5-MP10 -MPS<br>Bulldozer|2,4|(12)|
||TAF: Factor de ajuste transiente MP2,5-MP10 -MPS<br>Camiones Fuera de Carretera|1,5|(12)|
||TAF: Factor de ajuste transiente MP2,5-MP10 -MPS<br>Grúa Horquilla|1,5|(12)|
||TAF: Factor de ajuste transiente MP2,5-MP10 -MPS<br>Retro excavadoras|1,5|(12)|
||TAF: Factor de ajuste transiente MP2,5-MP10 -MPS<br>Otro material de construcción|1,5|(12)|
||TAF: Factor de ajuste transiente MP2,5-MP10 -MPS<br>Motoniveladora|1,5|(12)|
||TAF: Factor de ajuste transiente CO Bulldozer|2,6|(12)|
||TAF: Factor de ajuste transiente CO Camiones<br>Fuera de Carretera|1,5|(12)|
||TAF: Factor de ajuste transiente CO Grúa<br>Horquilla|1,5|(12)|
||TAF: Factor de ajuste transiente CO Retro<br>excavadoras|1,5|(12)|
||TAF: Factor de ajuste transiente CO Otro material<br>de construcción|1,5|(12)|
||TAF: Factor de ajuste transiente CO<br>Motoniveladora|1,5|(12)|
||TAF: Factor de ajuste transiente NOX Bulldozer|1,2|(12)|
||TAF: Factor de ajuste transiente NOX Camiones<br>Fuera de Carretera|1,0|(12)|
||TAF: Factor de ajuste transiente NOX Grúa<br>Horquilla|1,0|(12)|
||TAF: Factor de ajuste transiente NOX Retro<br>excavadoras|1,0|(12)|
||TAF: Factor de ajuste transiente NOX Otro<br>material de construcción|1,0|(12)|
||TAF: Factor de ajuste transiente NOX <br>Motoniveladora|1,0|(12)|
||TAF: Factor de ajuste transiente HC Bulldozer|2,3|(12)|
||TAF: Factor de ajuste transiente HC Camiones<br>Fuera de Carretera|1,1|(12)|
||TAF: Factor de ajuste transiente Grúa Horquilla|1,1|(12)|
||TAF: Factor de ajuste transiente HC Retro<br>excavadoras|1,1|(12)|
||TAF: Factor de ajuste transiente HC Otro material<br>de construcción|1,1|(12)|
||TAF: Factor de ajuste transiente HC<br>Motoniveladora|1,1|(12)|

_**Inventario y Modelación de Emisiones ATM037-23**_ _29/106_
_Proyecto Alba_
_Abril, 2023_

|Fuente Emisora|Variables|Valor|Ref.|
|---|---|---|---|
||A: Factor empírico “A” del factor de deterioro HC<br>Tier 3|0,027|(12)|
||A: Factor empírico “A” del factor de deterioro CO<br>Tier 3|0,151|(12)|
||A: Factor empírico “A” del factor de deterioro NOX <br>Tier 3|0,008|(12)|
||A: Factor empírico “A” del factor de deterioro MP<br>Tier 3|0,473|(12)|
||Soxcnv|0,02247|(12)|
||Soxbas|0,330|(12)|
||Soxdsl|0,005|(12)|
||BSFC >56 a 75 kw CO (g/kw-h)|248|(12)|
||BSFC >75 a 130 kw CO (g/kw-h)|223|(12)|
||BSFC >130 a 225 kw CO (g/kw-h)|223|(12)|
||BSFC >225 a 450 kw CO (g/kw-h)|223|(12)|
|Motor de camiones<br>pesados, medianos,<br>buses interurbanos y<br>vehículos comerciales<br>diésel (EURO III)|v: Velocidad vehículos en caminos pavimentados|70|(13)|

(7) Factor obtenido desde AP42, 5th Edition: Capítulo 11, sección 11.9 “Western Surface Coal Mining”
(8) Factor obtenido desde Guía para la Estimación de Emisiones Atmosféricas en la Región Metropolitana (2020)
(9) Factor obtenido desde AP42, 5th Edition: Capítulo 13, sección 13.2.4 “Aggregate Handling and Storage Piles”
(10) Factor obtenido desde AP42, 5th Edition: Capítulo 13, sección 13.2.1 “Paved Road”
(11) Ver sección 10.4
(12) Valor de referencia obtenido desde el Manual para el desarrollo de inventarios de emisiones atmosféricas,

MMA, 2017
(13) Valor proporcionado por el cliente
(14) Valor obtenido de la Estación Jardín Infantil, año 2021.

_**Inventario y Modelación de Emisiones ATM037-23**_ _30/106_
_Proyecto Alba_
_Abril, 2023_

**10.4** **Peso Promedio**

Para cada fase del proyecto se determinó el peso promedio de la flota de vehículos,
considerando proporciones de acuerdo con el número de viajes que realiza cada
vehículo que circulará por una misma vía:

_PPP_ = _PPC_ - _PV_ (III)

## PPR =  PPP (IV)

Dónde _:_

_PPP_ : Proporción por tipo de vehículo del total de la flota

_PPR_ : Peso medio (t)
_PPC_ : Peso medio asignado a cada tipo de vehículo (t)
_PV_ : (Viajes totales por tipo de vehículo) / (total de viajes de la flota)

**10.4.1** **Peso Promedio Caminos Pavimentados**

Los pesos promedio para la flota de vehículos que circularán por las vías
pavimentadas, en la fase de construcción, operación actual, operación con proyecto
y proyecto Adelaida, se presentan en la siguiente tabla:

_**Inventario y Modelación de Emisiones ATM037-23**_ _31/106_
_Proyecto Alba_
_Abril, 2023_

_**Tabla N° 15**_
_**Peso Promedio Vehículos (t) en Caminos Pavimentados**_

_**Fase de Construcción**_

|Transporte|Peso<br>Medio<br>PPC|Viajes<br>ida<br>año 1|Viajes<br>ida<br>año 2|Proporción<br>de viajes<br>año 1|Proporción<br>de viajes<br>año 2|Proporción<br>por Peso<br>año1|Proporción<br>por Peso<br>año2|Peso<br>Promedio<br>t año 1|Peso<br>Promedio<br>t año 2|
|---|---|---|---|---|---|---|---|---|---|
|Traslado de infraestructura para instalación de faenas|26|12|-|0,0010|-|0,0260|-|24,4|-|
|Retiro de infraestructura para instalación de faenas|26|-|12|-|0,0030|-|0,0780|-|23,7|
|Transporte de maquinarias al área del proyecto|26|12|-|0,0010|-|0,0260||24,4||
|Traslado de sales al proyecto|26|-|3.500|-|0,7640|-|19,8640|-|23,7|
|Traslado de equipos e infraestructura asociada al proyecto|26|100|-|0,0120|-|0,3120|-|24,4|-|
|Traslado de hormigón|21|480|-|0,0560|-|1,1480|-|24,4|-|
|Retiro de aguas servidas de baños químicos|22|156|156|0,0180|0,0340|0,3960|0,7480|24,4|23,7|
|Traslado de residuos domiciliarios|22|156|156|0,0180|0,0340|0,3960|0,7480|24,4|23,7|
|Retiro de residuos sólidos no peligrosos|22|12|12|0,0010|0,0030|0,0220|0,0660|24,4|23,7|
|Retiro de residuos sólidos peligrosos|22|12|12|0,0010|0,0030|0,0220|0,0660|24,4|23,7|
|Traslado de personal|13|730|730|0,0850|0,1590|1,1050|2,0670|24,4|23,7|
|Traslado de gas|22|-|4|-|0,0010|-|0,0220|-|23,7|
|Traslado del material de excavación|26|3.900|-|0,4550|-|11,8300|-|24,4|-|
|Traslado del material empréstito|26|3.000|-|0,3500|-|9,1000|-|24,4|-|
|Camiones Aljibe 30 m3|66|416|416|0,0460|0,0820|3,0360|5,4120|26,5|27,6|
|Camiones Aljibe 20 m3|46|104|104|0,0110|0,0200|0,5060|0,9200|26,5|27,6|
|Almacenamiento de partes de aerogeneradores-25 Camionesb|26|1.500|-|0,7490|-|19,4740|-|26,0|-|
|Almacenamiento de partes de aerogeneradores-6 Camionesc|26|504|-|0,2510|-|6,5260|-|26,0|-|

Fuente: Algoritmos SpA, 2023, en base a información entregada por el cliente.

b Acopio temporal de componentes de parques eólicos en sector industrial de Mejillones
c Acopio temporal de componentes de parques eólicos en sector industrial de Mejillones

_**Inventario y Modelación de Emisiones ATM037-23**_ _32/106_
_Proyecto Alba_

_Abril, 2023_

_**Tabla N° 16**_
_**Peso Promedio Vehículos (t) en Caminos No Pavimentados**_

_**Fase de Construcción**_

|Sector|Transporte|Peso<br>Medio<br>PPC|Viajes<br>ida<br>año 1|Viajes<br>ida<br>año 2|Proporción<br>de viajes<br>año 1|Proporción<br>de viajes<br>año 2|Proporción<br>por Peso<br>año1|Proporción<br>por Peso<br>año2|Peso<br>Promedio<br>t año 1|Peso<br>Promedio<br>t año 2|
|---|---|---|---|---|---|---|---|---|---|---|
|Entrada<br>Planta|Traslado de infraestructura para instalación de faenas|26|12|-|0,0010|-|0,0260|-|24,7|-|
|Entrada<br>Planta|Retiro de infraestructura para instalación de faenas|26|-|12|-|0,0030|-|0,0780|-|23,7|
|Entrada<br>Planta|Transporte de maquinarias al área del proyecto|26|12|-|0,0010|-|0,0260||24,7||
|Entrada<br>Planta|Traslado de sales al proyecto|26|-|3.500|-|0,7640|-|19,8640|-|23,7|
|Entrada<br>Planta|Traslado de equipos e infraestructura asociada al proyecto|26|100|-|0,0090|-|0,2340|-|24,7|-|
|Entrada<br>Planta|Traslado de hormigón|21|480|-|0,0450|-|0,9230|-|24,7|-|
|Entrada<br>Planta|Retiro de aguas servidas de baños químicos|22|156|156|0,0150|0,0340|0,3300|0,7480|24,7|23,7|
|Entrada<br>Planta|Traslado de residuos domiciliarios|22|156|156|0,0150|0,0340|0,3300|0,7480|24,7|23,7|
|Entrada<br>Planta|Retiro de residuos sólidos no peligrosos|22|12|12|0,0010|0,0030|0,0220|0,0660|24,7|23,7|
|Entrada<br>Planta|Retiro de residuos sólidos peligrosos|22|12|12|0,0010|0,0030|0,0220|0,0660|24,7|23,7|
|Entrada<br>Planta|Traslado de personal|13|730|730|0,0690|0,1590|0,8970|2,0670|24,7|23,7|
|Entrada<br>Planta|Traslado de gas|22|-|4|-|0,0010|-|0,0220|-|23,7|
|Entrada<br>Planta|Almacenamiento de partes de aerogeneradores-25 Camiones|26|1.500|-|0,1420|-|3,6920|-|24,7|-|
|Entrada<br>Planta|Almacenamiento de partes de aerogeneradores-6 Camiones|26|504|-|0,0480|-|1,2480|-|24,7|-|
|Entrada<br>Planta|Traslado del material de excavación|26|3.900|-|0,3690|-|9,5940|-|24,7|-|
|Entrada<br>Planta|Traslado del material empréstito|26|3.000|-|0,2840|-|7,3840|-|24,7|-|
|Entrada<br>Planta|Camiones Aljibe 30 m3|66|416|416|0,0370|0,0820|2,4420|5,4120|26,4|27,6|
|Entrada<br>Planta|Camiones Aljibe 20 m3|46|104|104|0,0090|0,0200|0,4140|0,9200|26,4|27,6|
|-|Almacenamiento de partes de aerogeneradores-25 Camiones|26|1.500|-|0,7490|-|19,4740|-|26,0|-|
|-|Almacenamiento de partes de aerogeneradores-6 Camiones|26|504|-|0,2510|-|6,5260|-|26,0|-|

Fuente: Algoritmos SpA, 2023, en base a información entregada por el cliente.

_**Inventario y Modelación de Emisiones ATM037-23**_ _33/106_
_Proyecto Alba_

_Abril, 2023_

_**Tabla N° 17**_
_**Peso Promedio Vehículos (t) en Caminos Pavimentados**_

_**Fase de Operación Actual**_

|Transporte|Peso Medio<br>PPC|N° viajes ida al<br>año|Proporción de<br>viajes (PV)|Proporción por<br>Peso (PPP)|Peso Promedio<br>t (PPR)|
|---|---|---|---|---|---|
|Buses Hualpén traslado de personal|13|1.095|0,0390|0,5070|12|
|Traslado Agua desmineralizada|16|1.460|0,0520|0,8060|0,8060|
|Traslado Cal y Petróleo diésel|26|1.460|0,0520|1,3520|1,3520|
|Traslado Ceniza|26|5.840|0,2070|5,3820|5,3820|
|Camionetas corporativas|4|14.235|0,5040|2,0160|2,0160|
|Proveedores|16|4.015|0,1420|2,2010|2,2010|
|Retiro de residuos domiciliarios|16|144|0,0050|0,0780|0,0780|
|Retiro RESPEL|16|2|0,0000|0,0000|0,0000|

Fuente: Algoritmos SpA, 2023, en base a información entregada por el cliente.

_**Tabla N° 18**_
_**Peso Promedio Vehículos (t) en Caminos Pavimentados**_

_**Fase de Operación con Proyecto**_

|Transporte|Peso<br>Medio PPC|N° viajes<br>ida al año|Proporción<br>de viajes<br>(PV)|Proporción<br>por Peso<br>(PPP)|Peso<br>Promedio<br>t (PPR)|
|---|---|---|---|---|---|
|Buses Hualpén traslado de personal|13|1.095|0,0480|0,6240|9|
|Traslado Agua desmineralizada|16|1.460|0,0640|0,9920|0,9920|
|Camionetas corporativas|4|14.235|0,6200|2,4800|2,4800|
|Proveedores|16|4.015|0,1750|2,7130|2,7130|
|Retiro de residuos domiciliarios|16|144|0,0060|0,0930|0,0930|
|Retiro RESPEL|16|2|0,0000|0,0000|0,0000|
|Almacenamiento de partes de aerogeneradores-25 Camiones|26|1.500|0,0650|1,6900|1,6900|
|Almacenamiento de partes de aerogeneradores-6 Camiones|26|504|0,0220|0,5720|0,5720|

Fuente: Algoritmos SpA, 2023, en base a información entregada por el cliente.

_**Inventario y Modelación de Emisiones ATM037-23**_ _34/106_
_Proyecto Alba_

_Abril, 2023_

_**Tabla N° 19**_
_**Peso Promedio Vehículos (t) en Caminos Pavimentados**_

_**Proyecto Adelaida**_

|Transporte|Peso Medio<br>PPC|N° viajes<br>ida al año|Proporción<br>de viajes<br>(PV)|Proporción<br>por Peso<br>(PPP)|Peso<br>Promedio<br>t (PPR)|
|---|---|---|---|---|---|
|H2-Camión Pesado|30|18.000|1,0000|30,0000|30|

Fuente: Algoritmos SpA, 2023, en base a información entregada por el cliente.

_**Tabla N° 20**_
_**Peso Promedio Vehículos (t) en Caminos Pavimentados**_

_**Fase de Cierre**_

|Transporte|Peso Medio<br>PPC|N° viajes<br>ida al año|Proporción<br>de viajes<br>(PV)|Proporción<br>por Peso<br>(PPP)|Peso<br>Promedio<br>t (PPR)|
|---|---|---|---|---|---|
|Retiro de infraestructura instalación de faenas|26|12|0,0030|0,0780|13,5|
|Transporte de maquinarias al área del proyecto|26|6|0,0020|0,0520|0,0520|
|Retiro de aguas servidas de baños químicos|22|156|0,0410|0,9020|0,9020|
|Retiro de residuos sólidos no peligrosos|22|24|0,0060|0,1320|0,1320|
|Retiro de residuos sólidos peligrosos|22|2|0,0010|0,0220|0,0220|
|Traslado de personal|13|3.650|0,9480|12,3240|12,3240|
|Camiones Aljibe 30m3|66|104|0,0260|1,7160|15,7|
|Camiones Aljibe 20m3|46|104|0,0260|1,1960|1,1960|

Fuente: Algoritmos SpA, 2023, en base a información entregada por el cliente.

_**Inventario y Modelación de Emisiones ATM037-23**_ _35/106_
_Proyecto Alba_

_Abril, 2023_

**10.5** **Nivel de Actividad Etapa de Construcción**

**10.5.1** **Compactación**

El nivel de actividad corresponde a las horas de compactación, que se obtienen en
base al área a recorrer, la cual debe ser dividida por el ancho y velocidad de la
compactadora, y multiplicada por el número de pasadas.

_**Tabla N° 21**_
_**Nivel de Actividad Compactación (h/año) Fase Construcción-año 1**_

|Actividad|Área (m2)|No<br>Pasadas|Ancho (m)|Velocidad<br>(km/h)|Compactación<br>(h)|
|---|---|---|---|---|---|
|Compactación<br>Motoniveladora|25.000|5|3,8|11|3,08|

Fuente: Algoritmos SpA, 2023, en base a información entregada por el cliente.

**10.5.2** **Nivelación**

El nivel de actividad está asociado a los kilómetros recorridos por la niveladora,
determinados a partir del área a nivelar, el ancho de la maquinaria y el número de
pasadas. En la siguiente Tabla se presentan los kilómetros recorridos en la actividad
de nivelación.

_**Tabla N° 22**_
_**Nivel de Actividad Nivelación (km) Fase Construcción-año 1**_

|Actividad|Área de<br>Trabajo (m2)|Ancho<br>Niveladora (m)|N° Pasadas|km recorridos|
|---|---|---|---|---|
|Nivelación<br>Motoniveladora|25.000|3,7|5|33,78|

Fuente: Algoritmos SpA, 2023, en base a información entregada por el cliente

**10.5.3** **Excavación**

El nivel de actividad se determina dividiendo el volumen a excavar por el
rendimiento de la maquinaria utilizada en la excavación. Se considera que para una
máquina con capacidad de palada de 1,1 [m [3] ], se tiene un rendimiento igual a
66,3 [d] [m [3] /h]. En la siguiente tabla se presenta el volumen a excavar y las horas
de excavación que se destinarán durante la fase del proyecto.

_**Tabla N° 23**_
_**Nivel de Actividad Horas de Excavación (h/año) Fase Construcción-año 1**_

|Actividad|Volúmen a excavar<br>(m3/año)|Horas de excavación<br>(h/año)|
|---|---|---|
|Excavación<br>Retro excavadora|90.000|1.357|

Fuente: Algoritmos SpA, 2023, en base a información entregada por el cliente.

d Valor obtenido en base a información enviada por cliente.

_**Inventario y Modelación de Emisiones ATM037-23**_ _36/106_
_Proyecto Alba_

_Abril, 2023_

**10.5.4** **Carga y Descarga de Material**

El nivel de actividad asociado a la carga y descarga del material, está definido por
la cantidad de material en el proceso, en toneladas al año.

La siguiente tabla presenta la cantidad de material a cargar y descargar (t/año)
para el primer año en la fase de Construcción.

_**Tabla N° 24**_
_**Nivel de Actividad Carga y Descarga de material (t/año)**_

_**Fase Construcción año 1 y año 2**_

|Actividad|Material Año 1<br>(t/año)|Material Año 2<br>(t/año)|
|---|---|---|
|Relleno con material empréstito|180.000|-|
|Sales|-|226.100|

Fuente: Algoritmos SpA, 2023, en base a información entregada por el cliente

**10.5.5** **Tránsito de Vehículos por Tipo de Carpeta.**

Para determinar el nivel de actividad asociado al tránsito de vehículos por caminos,
se requiere obtener los kilómetros totales recorridos por cada tipo de vehículo. Para
ello se ha considerado la siguiente ecuación (V):

_KTR_ = _VT_  _DR_ (V)
Dónde:

KTR : Kilómetros totales recorridos al año ida y vuelta (veh-km/año)
VT : Viajes totales (ida + vuelta) al año por tipo de vehículo (veh/año)

DR : Distancia recorrida en cada viaje de ida (km)

Para estimar los viajes totales (ida + vuelta) al año que realizan los camiones y
vehículos, se consideró la siguiente ecuación (VI):

_VT_ =  _M_   2 (VI)

 _CP_ 

Dónde:

VT : Viajes totales (ida + vuelta) al año por tipo de vehículo (veh/año)

M : Cantidad de material a transportar (t)
CP : Capacidad de carga del camión (t)

_**Inventario y Modelación de Emisiones ATM037-23**_ _37/106_
_Proyecto Alba_

_Abril, 2023_

**10.5.5.1** **Tránsito de Vehículos Camino Pavimentado**

Las siguientes tablas presentan la cantidad de viajes ida al año por tipo de vehículo,
la distancia recorrida en cada viaje de ida y el nivel de actividad obtenidos al aplicar
la ecuación (V) y ecuación (VI) en caminos pavimentados para la fase de
construcción del proyecto.

En la estimación de los kilómetros totales recorridos que realiza cada vehículo se
consideraron tanto los viajes de ida como los de vuelta.

_**Tabla N° 25**_
_**Cálculo del Nivel de Actividad para Tránsito de Vehículos**_
_**por Caminos Pavimentados (veh-km/año) Fase Construcción Año 1 y 2**_

|Transporte|Viajes|Distancia<br>Camino<br>Pavimentado<br>(km)|Kilómetros<br>Totales<br>(veh-<br>km/año)<br>[KTR] Año 1|Kilómetros<br>Totales<br>(veh-<br>km/año)<br>[KTR] Año 2|
|---|---|---|---|---|
|Traslado de infraestructura para<br>instalación de faenas|12|14|326|-|
|Retiro de infraestructura para<br>instalación de faenas|12|14|-|326|
|Transporte de maquinarias al<br>área del proyecto|12|14|326|-|
|Traslado de sales al proyecto|3.500|14|-|95.200|
|Traslado de equipos e<br>infraestructura asociada al<br>proyecto|100|14|2.720|-|
|Traslado de hormigón|480|14|13.056|-|
|Retiro de aguas servidas de<br>baños químicos|156|14|4.255|2.122|
|Traslado de residuos<br>domiciliarios|156||4.255|2.122|
|Retiro de residuos sólidos no<br>peligrosos|12|14|326|163|
|Retiro de residuos sólidos<br>peligrosos|2|14|326|163|
|Traslado de personal|730|14|19.856|9.928|
|Traslado de gas|4|14|-|109|
|Traslado del material de<br>excavación|3.900|14|109.200|-|
|Traslado del material<br>empréstito|3.000|14|84.000|-|
|Camiones Aljibe 30 m3|416|14|11.648|11.648|
|Camiones Aljibe 20 m3|104|14|2.912|2.912|
|Almacenamiento de partes de<br>aerogeneradores-25 Camiones|1.500|0,55|1.650|-|
|Almacenamiento de partes de<br>aerogeneradores-6 Camiones|504|0,55|554|-|

Fuente: Algoritmos SpA, 2023, en base a información entregada por el cliente

_**Inventario y Modelación de Emisiones ATM037-23**_ _38/106_
_Proyecto Alba_

_Abril, 2023_

**10.5.5.2** **Tránsito de Vehículos Camino No Pavimentado**

Las siguientes tablas presentan la cantidad de viajes ida al año por tipo de vehículo,
la distancia recorrida en cada viaje de ida y el nivel de actividad obtenidos al aplicar
la ecuación (V) y ecuación (VI) en caminos no pavimentados para la fase de
construcción del proyecto.

En la estimación de los kilómetros totales recorridos que realiza cada vehículo se
consideraron tanto los viajes de ida como los de vuelta.

_**Tabla N° 26**_
_**Cálculo del Nivel de Actividad para Tránsito de Vehículos**_
_**por Caminos No Pavimentados (veh-km/año) Fase Construcción Año 1 y**_

_**2**_

|Transporte|Viajes|Distancia<br>Camino<br>Pavimentado<br>(km)|Kilómetros<br>Totales<br>(veh-<br>km/año)<br>[KTR] Año 1|Kilómetros<br>Totales<br>(veh-<br>km/año)<br>[KTR] Año 2|
|---|---|---|---|---|
|Traslado de infraestructura para<br>instalación de faenas|12|0,2|5|-|
|Retiro de infraestructura para<br>instalación de faenas|12|0,2|-|5|
|Transporte de maquinarias al<br>área del proyecto|12|0,2|5|-|
|Traslado de sales al proyecto|3.500|0,2|-|1.400|
|Traslado de equipos e<br>infraestructura asociada al<br>proyecto|100|0,2|40|-|
|Traslado de hormigón|480|0,2|192|-|
|Retiro de aguas servidas de<br>baños químicos|156|0,2|63|62|
|Traslado de residuos<br>domiciliarios|156|0,2|63|62|
|Retiro de residuos sólidos no<br>peligrosos|12|0,2|5|5|
|Retiro de residuos sólidos<br>peligrosos|12|0,2|5|5|
|Traslado de personal|730|0,2|292|292|
|Traslado de gas|4|0,2|-|2|
|Almacenamiento de partes de<br>aerogeneradores-25 Camiones|1.500|0,2|600|-|
|Almacenamiento de partes de<br>aerogeneradores-6 Camiones|504|0,2|202|-|
|Traslado del material de<br>excavación|3.900|0,2|1.560|-|
|Traslado del material<br>empréstito|3.000|0,2|1.200|-|
|Camiones Aljibe 30 m3|416|0,2|166|166|
|Camiones Aljibe 20 m3|104|0,2|42|42|

_**Inventario y Modelación de Emisiones ATM037-23**_ _39/106_
_Proyecto Alba_

_Abril, 2023_

|Transporte|Viajes|Distancia<br>Camino<br>Pavimentado<br>(km)|Kilómetros<br>Totales<br>(veh-<br>km/año)<br>[KTR] Año 1|Kilómetros<br>Totales<br>(veh-<br>km/año)<br>[KTR] Año 2|
|---|---|---|---|---|
|Almacenamiento de partes de<br>aerogeneradores-25 Camiones|1.500|0,34|1.020|-|
|Almacenamiento de partes de<br>aerogeneradores-6 Camiones|504|0,34|343|-|

Fuente: Algoritmos SpA, 2023, en base a información entregada por el cliente

**10.5.6** **Motor de Vehículos**

Para determinar el nivel de actividad asociado a la combustión interna de motores
de vehículos debido al tránsito por caminos se requiere obtener los kilómetros
totales recorridos por cada tipo de vehículo. Para ello se han considerado los
valores presentados en la sección anterior.

**10.5.7** **Motor de Maquinarias**

Para determinar el nivel de actividad asociado a la combustión interna de cada
motor de maquinarias se requiere obtener las horas de funcionamiento al año. Para
ello se ha considerado la siguiente ecuación (VII):

_HF_ = _C_  _HD_  _DA_ (VII)
Dónde:

HF : Horas de funcionamiento al año (h/año)

C : Cantidad de maquinarias
HD : Horas de funcionamiento al día por cada maquinaria (h/día)
DA : Días de funcionamiento al año por cada maquinaria (días/año)

En la siguiente tabla se presenta el tipo de maquinaria a utilizar, la potencia (kW)
y el nivel de actividad HF (h/año) obtenido al aplicar la ecuación (VII) para el
escenario de construcción del Proyecto Alba .

_**Tabla N° 27**_
_**Cálculo del Nivel de Actividad para Motor de Maquinarias (h/año)**_

_**Fase Construcción- Año 1 y 2**_

|Tipo de Maquinaria|(h/año 1)|(h/año 2)|Potencia (kw)|Col5|
|---|---|---|---|---|
|Grúa|3.285|1.643|122|122|
|Vibrador Mecánico|1.440|-|4|4|
|Bulldozer|466|881|149|149|
|Compactadora|3|-|186|186|
|Motoniveladora|3|-|93|93|
|Retroexcavadora|678|-|69|69|
|Camiones Pluma|3.285|1.643|298|298|

_**Inventario y Modelación de Emisiones ATM037-23**_ _40/106_
_Proyecto Alba_

_Abril, 2023_

Grúa Horquilla 3.285 1.643 122
Fuente: Algoritmos SpA, 2023, en base a información entregada por el cliente

**10.5.8** **Grupo Electrógeno**

El nivel de actividad corresponde al consumo de combustible diésel que serán
utilizados durante la fase de construcción.

La siguiente tabla presenta cantidad, horas de funcionamiento al año y Consumo
combustible diésel para la fase del proyecto.

_**Tabla N° 28**_
_**Cálculo del Nivel de Actividad para Grupos Electrógenos**_

_**Fase Construcción-Año 1 y 2**_

|Actividad|Cantidad|(h/año)|Consumo<br>Comb<br>(l/h)|Densidad<br>Diésele<br>(kg/l)|Consumo<br>(kg de<br>Comb/<br>año 1)|Consumo<br>(kg de<br>Comb/<br>año 2)|
|---|---|---|---|---|---|---|
|GE 100 kva|1|8.760|26|0,84|191.318|95.659|

Fuente: Algoritmos SpA, 2023.

**10.5.9** **Fundición Sales Solares**

Hoy en día, las sales solares fundidas (60 % en peso de NaNO 3 - 40 % en peso de
KNO 3 ) se utilizan en la tecnología de almacenamiento de energía térmica, sin
embargo, la descomposición térmica de las sales de nitrato puede provocar
emisiones de NO x .

Según un estudio [f] el efecto de la descomposición térmica de la sal solar genera
impurezas. El único catión en los nitratos es el magnesio y, dado que se presenta
como nitrato, contribuye a la formación de NO x . Los resultados muestran que la
impureza Mg(NO 3 ) 2 es la principal fuente de emisión de NO x en las sales solares
debido a su descomposición térmica durante el proceso de fusión.

La descomposición del Mg(NO 3 ) 2 comienza a los 290° C y termina alrededor de los
440°C (MU y Perlmutter, 1982). El análisis del estudio muestra que la pérdida de
peso del 43% alcanzada hasta los 330°C y es debido a la pérdida de las moléculas
de agua; las pérdidas a temperaturas más altas son atribuidas a la descomposición
de Mg(NO 3 ) 2 en MgO. Por lo tanto, la presencia de Mg(NO 3 ) 2 puede producir NO x en
los puntos calientes durante la fusión de sal solar [c] .

La reacción principal en la descomposición del Mg(NO 3 ) 2 es (Niessen, 1973):

Mg(NO 3 ) 2 →MgO (s) + NO 2 (g) + NO(g) + O 2 (g) (VIII)

e Densidad Obtenida de Guía Metodológica para la Estimación de Emisiones provenientes de Fuentes Puntuales.
f Effect of the impurity magnesium nitrate in the thermal decomposition of the solar salt.

_**Inventario y Modelación de Emisiones ATM037-23**_ _41/106_
_Proyecto Alba_

_Abril, 2023_

De la ecuación (VIII), la cantidad de NO x producida se puede calcular, la cual
corresponde a 3,13 gr de NO x por cada gramo de Mg.

La Tabla N° 29 muestra la cantidad de sal solar utilizada en el proceso de fundición
y su contenido de Magnesio.

_**Tabla N° 29**_
_**Cálculo Fundición Sal Solar**_

_**Fase Construcción-Año 2**_

|Actividad|Cantidad (t)|% Mg|
|---|---|---|
|Fundición Sal Solar|85.000|0,016|

Fuente: Algoritmos SpA, 2022

**10.5.10** **Combustión Gas Natural**

El nivel de actividad corresponde al consumo de combustible gas natural que serán
utilizados durante la fundición de sal en la fase de construcción del año 2.

La siguiente tabla presenta cantidad de gas a utilizar, días de uso al año y Consumo
combustible gas natural para la fase del proyecto.

_**Tabla N° 30**_
_**Cálculo del Nivel de Actividad para consumo de combustible Gas Natural,**_

_**Fase Construcción-Año 2**_

|Actividad|Gas para utilizar<br>(kg/día)|Período<br>(días/año)|Consumo (ton de<br>Comb/ año 2)|
|---|---|---|---|
|Combustión Gas Natural|2.100|90|189|

Fuente: Algoritmos SpA, 2023

**10.5.11** **Proyecto Adelaida**

**10.5.11.1** **Tránsito de Vehículos Camino Pavimentado**

Las siguientes tablas presentan la cantidad de viajes ida al año por tipo de vehículo,
la distancia recorrida en cada viaje de ida y el nivel de actividad obtenidos al aplicar
la ecuación (V) y ecuación (VI) en caminos pavimentados.

En la estimación de los kilómetros totales recorridos que realiza cada vehículo se
consideraron tanto los viajes de ida como los de vuelta.

_**Inventario y Modelación de Emisiones ATM037-23**_ _42/106_
_Proyecto Alba_

_Abril, 2023_

_**Tabla N° 31**_
_**Cálculo del Nivel de Actividad para Tránsito de Vehículos**_

_**por Caminos Pavimentados (veh-km/año)**_

|Transporte|Viajes|Distancia<br>Camino<br>Pavimentado<br>(km)|Kilómetros<br>Totales<br>(veh-<br>km/año 1)<br>[KTR]|Kilómetros<br>Totales<br>(veh-<br>km/año 2)<br>[KTR]|
|---|---|---|---|---|
|H2-Camión Pesado|18.000|3,58|128.880|128.880|

Fuente: Algoritmos SpA, 2023, en base a información entregada por el cliente

**10.6** **Nivel de actividad Etapa de Operación Actual**

**10.6.1** **Tránsito de Vehículos por tipo de carpeta.**

**10.6.1.1** **Tránsito de Vehículos camino pavimentado**

La siguiente tabla presenta la cantidad de viajes al año por tipo de vehículo, la
distancia recorrida en cada viaje y el nivel de actividad obtenidos al aplicar la
ecuación (V) y ecuación (VI) en caminos pavimentados utilizados durante la fase
de operación actual del proyecto.

_**Tabla N° 32**_
_**Cálculo del Nivel de Actividad para Tránsito de Vehículos**_
_**por Caminos Pavimentados (veh-km/año) Fase Operación Actual**_

|Transporte|Viajes|Distancia<br>Camino<br>Pavimentado<br>(km)|Kilómetros<br>Totales<br>(veh-km/año)<br>[KTR]|
|---|---|---|---|
|Buses Hualpén traslado de personal|1.095|14|30.660|
|Traslado Agua desmineralizada|1.460|14|40.880|
|Traslado Cal y Petróleo diésel|1.460|14|40.880|
|Traslado Ceniza|5.840|14|163.520|
|Camionetas corporativas|14.235|14|398.580|
|Proveedores|4.015|14|112.420|
|Retiro de residuos domiciliarios|144|14|4.032|
|Retiro RESPEL|2|14|56|

Fuente: Algoritmos SpA, 2023, en base a información entregada por el cliente

**10.6.2** **Motor de Vehículos**

Para determinar el nivel de actividad asociado a la combustión interna de motores
de vehículos debido al tránsito por caminos se requiere obtener los kilómetros
totales recorridos por cada tipo de vehículo. Para ello se han considerado los
valores presentados en la sección anterior 10.6.1.

_**Inventario y Modelación de Emisiones ATM037-23**_ _43/106_
_Proyecto Alba_

_Abril, 2023_

**10.6.3** **Emisiones Centrales**

Las siguientes tablas presentan las emisiones de las centrales (días/año) para la
operación actual.

_**Tabla N° 33**_
_**Emisiones Centrales,**_

_**Situación Actual**_

|Fuente|NO<br>x<br>(t)|SO<br>2<br>(t)|MP<br>(t)|
|---|---|---|---|
|Central Angamos|2.544,7|3.118,6|279,0|
|Central Cochrane|1.702,5|1.928,9|151,6|

Fuente: Algoritmos SpA en base a información entregada por el cliente, 2023.

**10.6.4** **Manejo de Carbón-Cancha Carbón**

**10.6.4.1** **Maquinaria en el área de almacenamiento de carbón**
Se determinó el nivel de actividad asociado a la maquinaria utilizada para
almacenar carbón en la Central, con el objetivo de determinar el efecto sinérgico
de esta actividad y el Proyecto alba. Se considera la cantidad de material y las
horas de funcionamiento al año de la máquina.

La siguiente tabla presenta la cantidad de material (ton/año) y las horas de
funcionamiento al año (h/año)

_**Tabla N° 34**_
_**Cálculo del Nivel de Actividad para Maquinaria en área de**_

_**almacenamiento de carbón,**_

_**Situación Actual**_

|Fuente|Cantidad Material<br>(ton/año)|Horas operación (h/año)|
|---|---|---|
|Central Cochrane|1.992.400|13|
|Central Angamos|1.992.400|13|
|**Total**|3.984.800|26|

Fuente: Algoritmos SpA en base a información entregada por el cliente, 2023.

**10.6.4.2** **Motor de Maquinarias**

Para determinar el nivel de actividad asociado a la combustión interna de cada
motor de maquinarias se requiere obtener las horas de funcionamiento al año.

En la siguiente tabla se presenta el tipo de maquinaria a utilizar, la potencia (kW)
y el nivel de actividad HF (h/año) para el escenario de operación con proyecto. Es
importante mencionar que se consideran las horas de operación anual de ambas
centrales.

_**Inventario y Modelación de Emisiones ATM037-23**_ _44/106_
_Proyecto Alba_

_Abril, 2023_

_**Tabla N° 35**_
_**Cálculo del Nivel de Actividad para Combustión de Maquinarias (h/año)**_

_**Situación Actual**_

|Tipo de Maquinaria|(h/año)|Potencia (kw)|
|---|---|---|
|Bulldozer|3.646|264,0|
|Bulldozer|4.028|264,0|
|Cargador Frontal|6.322|204,0|
|Cargador Frontal|3.568|204,0|
|Cargador Frontal|8.442|204,0|

Fuente: Algoritmos SpA, 2023, en base a información entregada por el cliente

**10.6.4.3** **Carga y Descarga de Carbón**
El nivel de actividad asociado a la carga y descarga del Carbón, está definido por
la cantidad de material en el proceso, en toneladas al año.

La siguiente tabla presenta la cantidad de material a cargar y descargar (t/año)
para la fase de Operación con proyecto.

_**Tabla N° 36**_
_**Nivel de Actividad Carga y Descarga de Carbón(t/año),**_

_**Situación Actual**_

|Actividad|Material Año<br>(t/año)|
|---|---|
|Central Cochrane|1.992.400|
|Central Angamos|1.992.400|
|**Total**|3.984.800|

Fuente: Algoritmos SpA, 2023, en base a información entregada por el cliente

**10.6.4.4** **Transferencia de carbón en correas y torres.**
El nivel de actividad asociado a la transferencia de carbón en correas y torres está
definido por la cantidad de material en el proceso, en toneladas al año.

La siguiente tabla presenta la cantidad de transferencia de carbón (t/año) para la
Operación actual de ambas centrales.

_**Tabla N° 37**_
_**Nivel de Actividad transferencia de carbón en correas y torres (t/año),**_

_**situación actual**_

|Actividad|Material Año<br>(t/año)|
|---|---|
|Central Cochrane|1.992.400|
|Central Angamos|1.992.400|

_**Inventario y Modelación de Emisiones ATM037-23**_ _45/106_
_Proyecto Alba_

_Abril, 2023_

|Actividad|Material Año<br>(t/año)|
|---|---|
|**Total**|3.984.800|

Fuente: Algoritmos SpA, 2023, en base a información entregada por el cliente.

**10.6.4.5** **Erosión Eólica**

Para determinar el nivel de actividad de la erosión eólica, se requiere las áreas de
acopio expuestas y el periodo de exposición.

La siguiente tabla presenta la superficie de acopio (ha), los días de exposición
(días/año) y el nivel de actividad (ha-día/año) para la operación actual de ambas
centrales.

_**Tabla N° 38**_
_**Cálculo del Nivel de Actividad para Erosión Eólica,**_

_**Situación Actual**_

|Fuente|Área (Ha)|Días Exposición|Exposición Pila<br>(día-ha/año)|
|---|---|---|---|
|Cancha Carbón|22,5|365|8.213|

Fuente: Algoritmos SpA en base a información entregada por el cliente, 2023.

**10.7** **Nivel de actividad Etapa de Operación con Proyecto**

**10.7.1** **Tránsito de Vehículos por tipo de carpeta.**

**10.7.1.1** **Tránsito de Vehículos camino pavimentado**
La siguiente tabla presenta la cantidad de viajes al año por tipo de vehículo, la
distancia recorrida en cada viaje y el nivel de actividad obtenidos al aplicar la
ecuación (V) y ecuación (VI) en caminos pavimentados utilizados durante la fase
de operación con proyecto.

En la estimación de los kilómetros totales recorridos que realiza cada vehículo se
consideraron tanto los viajes de ida como los de vuelta.

_**Tabla N° 39**_
_**Cálculo del Nivel de Actividad para Tránsito de Vehículos**_
_**por Caminos Pavimentados (veh-km/año) Fase Operación con Proyecto**_

|Transporte|Viajes|Distancia Camino<br>Pavimentado (km)|Kilómetros Totales<br>(veh-km/año)<br>[KTR]|
|---|---|---|---|
|Buses Hualpén<br>traslado de personal|1.095|14|30.660|
|Traslado Agua<br>desmineralizada|1.460|14|40.880|
|Camionetas<br>corporativas|14.235|14|398.580|
|Proveedores|4.015|14|112.420|

_**Inventario y Modelación de Emisiones ATM037-23**_ _46/106_
_Proyecto Alba_

_Abril, 2023_

|Transporte|Viajes|Distancia Camino<br>Pavimentado (km)|Kilómetros Totales<br>(veh-km/año)<br>[KTR]|
|---|---|---|---|
|Retiro de residuos<br>domiciliarios|144|14|4.032|
|Retiro RESPEL|2|14|56|
|Almacenamiento de<br>partes de<br>aerogeneradores-25<br>Camiones|1.500|1|2.613|
|Almacenamiento de<br>partes de<br>aerogeneradores-6<br>Camiones|504|1|878|

Fuente: Algoritmos SpA, 2023, en base a información entregada por el cliente

**10.7.2** **Motor de Vehículos**

Para determinar el nivel de actividad asociado a la combustión interna de motores
de vehículos debido al tránsito por caminos se requiere obtener los kilómetros
totales recorridos por cada tipo de vehículo. Para ello se han considerado los
valores presentados en la sección anterior 10.7.1.

**10.7.3** **Emisiones Central Cochrane**

La siguiente tabla presenta las emisiones de la central (días/año) Cochrane, las
que ha sido incorporadas la situación con Proyecto, con el objeto de determinar el
efecto sinérgico de esta central con el Proyecto Alba.

_**Tabla N° 40**_
_**Emisiones Central Cochrane, situación futura**_

|Fuente|NO<br>x<br>(t)|SO<br>2<br>(t)|MP<br>(t)|
|---|---|---|---|
|Central Cochrane|1.702,5|1.928,9|151,6|

Fuente: Algoritmos SpA en base a información entregada por el cliente, 2023.

**10.7.4** **Demolición**

Para determinar el nivel de actividad de la demolición de la chimenea de la central
Angamos durante la fase de operación con proyecto, se requiere el período de
demolición y el área a demoler.

La siguiente tabla presenta la superficie de demolición (m [2] ) y los días de demolición
(año)

_**Inventario y Modelación de Emisiones ATM037-23**_ _47/106_
_Proyecto Alba_

_Abril, 2023_

_**Tabla N° 41**_
_**Cálculo del Nivel de Actividad para Demolición,**_

_**Fase Operación con Proyecto**_

|Fuente|Área (m2)|Tiempo Demolición (año)|
|---|---|---|
|Chimenea|50,3|0,1|

Fuente: Algoritmos SpA en base a información entregada por el cliente, 2023.

**10.7.5** **Manejo de Carbón-Cancha Carbón**

**10.7.5.1** **Maquinaria en el área de almacenamiento de carbón**

Para determinar el nivel de actividad asociado a la maquinaria utilizada para
almacenar carbón que continuará utilizando la Central Cochrane, se requiere la
cantidad de material y las horas de funcionamiento al año de la máquina.

La siguiente tabla presenta la cantidad de material (ton/año) y las horas de
funcionamiento al año (h/año)

_**Tabla N° 42**_
_**Cálculo del Nivel de Actividad para Maquinaria en área de**_

_**almacenamiento de carbón, Central Cochrane**_

|Fuente|Cantidad Material<br>(ton/año)|Horas operación (h/año)|
|---|---|---|
|Central Cochrane|1.992.400|13|

Fuente: Algoritmos SpA en base a información entregada por el cliente, 2023.

**10.7.5.2** **Motor de Maquinarias**

Para determinar el nivel de actividad asociado a la combustión interna de cada
motor de maquinarias se requiere obtener las horas de funcionamiento al año.

En la siguiente tabla se presenta el tipo de maquinaria a utilizar, la potencia (kW)
y el nivel de actividad HF (h/año) para el escenario de operación con proyecto.

_**Tabla N° 43**_
_**Cálculo del Nivel de Actividad para Combustión de Maquinarias (h/año)**_

_**Fase Operación con Proyecto.**_

|Tipo de Maquinaria|(h/año)|Potencia (kw)|
|---|---|---|
|Bulldozer|1.823|264,0|
|Bulldozer|2.014|264,0|
|Cargador Frontal|3.166|204,0|
|Cargador Frontal|1.784|204,0|
|Cargador Frontal|4.221|204,0|

Fuente: Algoritmos SpA, 2023, en base a información entregada por el cliente

_**Inventario y Modelación de Emisiones ATM037-23**_ _48/106_
_Proyecto Alba_

_Abril, 2023_

**10.7.5.3** **Carga y Descarga de Carbón**
El nivel de actividad asociado a la carga y descarga del Carbón, está definido por
la cantidad de material en el proceso, en toneladas al año.

La siguiente tabla presenta la cantidad de material a cargar y descargar (t/año).

_**Tabla N° 44**_
_**Nivel de Actividad Carga y Descarga de Carbón(t/año)**_

|Actividad|Material Año<br>(t/año)|
|---|---|
|Central Cochrane|1.992.400|

Fuente: Algoritmos SpA, 2023, en base a información entregada por el cliente

**10.7.5.4** **Transferencia de carbón en correas y torres.**
El nivel de actividad asociado a la transferencia de carbón en correas y torres está
definido por la cantidad de material en el proceso, en toneladas al año.

La siguiente tabla presenta la cantidad de transferencia de carbón (t/año).

_**Tabla N° 45**_
_**Nivel de Actividad transferencia de carbón en correas y torres (t/año)**_

|Actividad|Material Año<br>(t/año)|
|---|---|
|Central Cochrane|1.992.400|

Fuente: Algoritmos SpA, 2023, en base a información entregada por el cliente.

**10.7.5.5** **Erosión Eólica**

Para determinar el nivel de actividad de la erosión eólica, se requieren las áreas de
acopio expuestas y el periodo de exposición.

La siguiente tabla presenta la superficie de acopio (ha), los días de exposición
(días/año) y el nivel de actividad (ha-día/año).

_**Tabla N° 46**_
_**Cálculo del Nivel de Actividad para Erosión Eólica**_

|Fuente|Área (Ha)|Días<br>Exposición|Exposición<br>Pila<br>(día-ha/año)|
|---|---|---|---|
|Cancha Carbón|22,5|365|8.213|

Fuente: Algoritmos SpA en base a información entregada por el cliente, 2023.

_**Inventario y Modelación de Emisiones ATM037-23**_ _49/106_
_Proyecto Alba_

_Abril, 2023_

**10.7.6** **Proyecto Adelaida**

**10.7.6.1** **Tránsito de Vehículos Camino Pavimentado**

Las siguientes tablas presentan la cantidad de viajes ida al año por tipo de vehículo,
la distancia recorrida en cada viaje de ida y el nivel de actividad obtenidos al aplicar
la ecuación (V) y ecuación (VI) en caminos no pavimentados para la fase de
operación con proyecto.

En la estimación de los kilómetros totales recorridos que realiza cada vehículo se
consideraron tanto los viajes de ida como los de vuelta.

_**Tabla N° 47**_
_**Cálculo del Nivel de Actividad para Tránsito de Vehículos**_
_**por Caminos No Pavimentados (veh-km/año), Fase Operación con**_

_**proyecto.**_

|Transporte|Viajes|Distancia<br>Camino<br>Pavimentado<br>(km)|Kilómetros<br>Totales<br>(veh-km/año)<br>[KTR]|
|---|---|---|---|
|H2-Camión Pesado|18.000|3,58|128.880|

Fuente: Algoritmos SpA, 2023, en base a información entregada por el cliente

**10.8** **Nivel de actividad Etapa de Cierre**

**10.8.1** **Tránsito de Vehículos por tipo de carpeta.**

**10.8.1.1** **Tránsito de Vehículos camino pavimentado**
La siguiente tabla presenta la cantidad de viajes al año por tipo de vehículo, la
distancia recorrida en cada viaje y el nivel de actividad obtenidos al aplicar la
ecuación (V) y ecuación (VI) en caminos pavimentados utilizados durante la fase
de cierre del proyecto.

En la estimación de los kilómetros totales recorridos que realiza cada vehículo se
consideraron tanto los viajes de ida como los de vuelta.

_**Tabla N° 48**_
_**Cálculo del Nivel de Actividad para Tránsito de Vehículos**_
_**por Caminos Pavimentados (veh-km/año) Fase de cierre**_

|Transporte|Viajes ida|Distancia Camino<br>Pavimentado (km)|Kilómetros Totales<br>(veh-km/año)<br>[KTR]|
|---|---|---|---|
|Retiro de<br>infraestructura<br>instalación de faenas|12|14|326|
|Transporte de<br>maquinarias al área del<br>proyecto|6|14|163|

_**Inventario y Modelación de Emisiones ATM037-23**_ _50/106_
_Proyecto Alba_

_Abril, 2023_

|Transporte|Viajes ida|Distancia Camino<br>Pavimentado (km)|Kilómetros Totales<br>(veh-km/año)<br>[KTR]|
|---|---|---|---|
|Retiro de aguas<br>servidas de baños<br>químicos|156|14|4.255|
|Retiro de residuos<br>sólidos no peligrosos|24|14|653|
|Retiro de residuos<br>sólidos peligrosos|2|14|54|
|Traslado de personal|3.650|14|99.280|
|Camiones Aljibe 30 m3|104|14|2.912|
|Camiones Aljibe 20 m3|104|14|2.912|

Fuente: Algoritmos SpA, 2023, en base a información entregada por el cliente.

**10.8.2** **Motor de Vehículos**

Para determinar el nivel de actividad asociado a la combustión interna de motores
de vehículos debido al tránsito por caminos se requiere obtener los kilómetros
totales recorridos por cada tipo de vehículo. Para ello se han considerado los
valores presentados en la sección anterior 10.8.1.1.

**10.9** **Tasas de Emisión Escenario con Proyecto**

Al multiplicar los factores de emisión presentados en la sección 10.3 con los niveles
de actividad definidos en las secciones 10.5, 10.6, 10.7 y 5.8 se obtienen las tasas
de emisión anuales de MP 10, MP 2,5 y gases SO 2, NO x, CO y COV del Proyecto Alba.

A continuación, en las siguientes tablas, se encuentra el resumen de total de las
emisiones generadas durante la fase construcción, operación actual, operación con
proyecto y cierre, además de las tasas de emisiones de Proyecto Alba, Adelaida y
Aerogeneradores por si solos.

_**Inventario y Modelación de Emisiones ATM037-23**_ _51/106_
_Proyecto Alba_

_Abril, 2023_

_**Tabla N° 49**_
_**Tasas de Emisión Fase Construcción Año 1 (t/año)**_

|Fuente|SO<br>2|NO<br>X|CO|MP<br>2.5|MP<br>10|COVs|Unidad|
|---|---|---|---|---|---|---|---|
|Excavación|--|--|--|0,42|0,83|--|t/año|
|Compactación|--|--|--|<0,01|<0,01|--|t/año|
|Nivelación|--|--|--|<0,01|0,01|--|t/año|
|Carga y descarga de material|--|--|--|<0,01|0,03|--|t/año|
|Transito camino pavimentado|--|--|--|0,75|3,11|--|t/año|
|Motor vehículos Caminos pavimentados|<0,01|1,44|0,34|0,03|0,03|0,07|t/año|
|Transito camino no pavimentado|--|--|--|0,47|4,71|--|t/año|
|Motor vehículos Caminos no pavimentados|<0,01|0,03|<0,01|<0,01|<0,01|<0,01|t/año|
|Motor maquinaria|<0,01|3,39|2,27|0,47|0,48|0,45|t/año|
|Grupo Electrógeno|1,09|16,54|3,56|1,16|1,16|1,35|t/año|
|Transito camino pavimentado-Proyecto Adelaida|--|--|--|0,16|0,65|--|t/año|
|**Total**|**1,09**|**21,41**|**6,18**|**3,47**|**11,02**|**1,87**|**t/año**|

Fuente: Algoritmos SpA, 2023.

_**Tabla N° 50**_
_**Tasas de Emisión Fase Construcción Año 2 (t/año)**_

|Fuente|SO<br>2|NO<br>X|CO|MP<br>2.5|MP<br>10|COVs|Unidad|
|---|---|---|---|---|---|---|---|
|Carga y descarga de material|--|--|--|<0,01|0,03|--|t/año|
|Transito camino pavimentado|--|--|--|0,46|1,92|--|t/año|
|Motor vehículos Caminos pavimentados|<0,01|0,74|0,18|0,17|0,17|0,03|t/año|
|Transito camino no pavimentado|--|--|--|0,18|1,75|--|t/año|
|Motor vehículos Caminos no pavimentados|--|0,01|<0,01|<0,01|<0,01|<0,01|t/año|
|Motor maquinaria|<0,01|1,87|1,27|0,26|0,27|0,27|t/año|
|Grupo Electrógeno|0,54|8,27|1,78|0,58|0,58|0,68|t/año|
|fundición Sal Solar|--|42,57|--|--|--|--|t/año|
|Combustión Gas Natural|--|1,12|0,33|--|--|--|t/año|
|Transito camino pavimentado-Proyecto Adelaida|--|--|--|0,16|0,65|--|t/año|
|**Total**|**0,55**|**54,59**|**3,57**|**1,82**|**5,38**|**0,97**|**t/año**|

Fuente: Algoritmos SpA, 2023.

_**Inventario y Modelación de Emisiones ATM037-23**_ _52/106_
_Proyecto Alba_

_Abril, 2023_

_**Tabla N° 51**_
_**Tasas de Emisión Fase Operación Actual (t/año)**_

|Fuente|SO<br>2|NO<br>X|CO|MP<br>2.5|MP<br>10|COVs|Unidad|
|---|---|---|---|---|---|---|---|
|Transito camino pavimentado|--|--|--|1,23|5,08|--|t/año|
|Motor vehículos Caminos pavimentados|0,01|2,35|0,57|0,32|0,32|0,12|t/año|
|Maquinaria en área de almacenamiento de carbón|--|--|--|<0,01|<0,01|--|t/año|
|Combustión de motores de maquinaria|--|--|--|1,16|1,16|--|t/año|
|Carga y Descarga Carbón|--|--|--|0,14|0,92|--|t/año|
|Transferencia de carbón en correas y torres|--|--|--|0,18|0,18|--|t/año|
|Erosión eólica|--|--|--|0,24|1,53|--|t/año|
|Central Angamos|3.119|2.544,66|--|279,01|279,01|--|t/año|
|Central Cochrane|1.929|1.702,47|--|151,56|151,56|--|t/año|
|**Total**|**5.047,49**|**4.249,48**|**0,57**|**433,84**|**439,77**|**0,12**|**t/año**|

Fuente: Algoritmos SpA, 2023.

_**Tabla N° 52**_
_**Tasas de Emisión Fase Operación con Proyecto (t/año)**_

|Fuente|SO<br>2|NO<br>X|CO|MP<br>2.5|MP<br>10|COVs|Unidad|
|---|---|---|---|---|---|---|---|
|Transito camino pavimentado|--|--|--|0,40|1,66|8,63|t/año|
|Motor vehículos Caminos pavimentados|0,01|1,12|0,28|0,03|0,03|0,03|t/año|
|Central Cochrane|1.928,88|1.702,47|--|151,56|151,56|151,56|t/año|
|Demolición|--|--|--|0,30|2,97|2,97|t/año|
|Maquinaria en área de almacenamiento de carbón|--|--|--|<0,01|<0,01|--|t/año|
|Combustión de motores de maquinaria|--|--|--|0,58|0,58|--|t/año|
|Carga y Descarga Carbón|--|--|--|0,07|0,46|--|t/año|
|Transferencia de carbón en correas y torres|--|--|--|0,09|0,09|--|t/año|
|Erosión eólica|--|--|--|0,24|1,53|1,53|t/año|
|**Total**|**1.928,88**|**1703,60**|**0,28**|**153,27**|**158,88**|**164,73**|**t/año**|

Fuente: Algoritmos SpA, 2023.

_**Inventario y Modelación de Emisiones ATM037-23**_ _53/106_
_Proyecto Alba_

_Abril, 2023_

_**Tabla N° 53**_
_**Tasas de Emisión Fase Operación, Adelaida (t/año)**_

|Fuente|SO<br>2|NO<br>X|CO|MP<br>2.5|MP<br>10|COVs|Unidad|
|---|---|---|---|---|---|---|---|
|Transito camino pavimentado|--|--|--|0,157|0,647|--|t/año|
|**Total**|**--**|**--**|**--**|**0,157**|**0,647**|**--**|**t/año**|

Fuente: Algoritmos SpA, 2023.

_**Tabla N° 54**_
_**Tasas de Emisión Fase Operación, Aerogeneradores (t/año)**_

|Fuente|SO<br>2|NO<br>X|CO|MP<br>2.5|MP<br>10|COVs|Unidad|
|---|---|---|---|---|---|---|---|
|Transito camino pavimentado|--|--|--|<0,01|0,03|--|t/año|
|Motor vehículos Caminos pavimentados|--|0,01|<0,01|<0,01|<0,01|<0,01|t/año|
|Transito camino no pavimentado|--|--|--|0,19|1,9|--|t/año|
|Motor vehículos Caminos no pavimentados|--|0,01|<0,01|<0,01|<0,01|<0,01|t/año|
|**Total**|**--**|**0,02**|**<0,01**|**0,19**|**1,93**|**<0,01**|**t/año**|

Fuente: Algoritmos SpA, 2023.

_**Tabla N° 55**_
_**Tasas de Emisión Fase Operación con Proyecto, Alba-Adelaida-Aerogeneradores (t/año)**_

|Fuente|SO<br>2|NO<br>X|CO|MP<br>2.5|MP<br>10|COVs|Unidad|
|---|---|---|---|---|---|---|---|
|Transito camino pavimentado|--|--|--|0,55|2,29|--|t/año|
|Motor vehículos Caminos pavimentados|0,01|1,14|0,28|0,03|0,03|0,06|t/año|
|Central Cochrane|1928,88|1702,47|--|151,56|151,56|--|t/año|
|Demolición|--|--|--|0,30|2,97|--|t/año|
|Maquinaria en área de almacenamiento de carbón|--|--|--|<0,01|<0,01|--|t/año|
|Combustión de motores de maquinaria|--|--|--|0,58|0,58|--|t/año|
|Carga y Descarga Carbón|--|--|--|0,07|0,46|--|t/año|
|Transferencia de carbón en correas y torres|--|--|--|0,09|0,09|--|t/año|
|Tránsito camino pavimentado- Adelaida|--|--|--|0,16|0,65|--|t/año|
|Erosión eólica|--|--|--|0,24|1,53|--|t/año|
|**Total**|**1928,88**|**1703,61**|**0,28**|**153,58**|**160,17**|**0,06**|**t/año**|

Fuente: Algoritmos SpA, 2023.

_**Inventario y Modelación de Emisiones ATM037-23**_ _54/106_
_Proyecto Alba_

_Abril, 2023_

_**Tabla N° 56**_
_**Tasas de Emisión Fase Cierre (t/año)**_

|Fuente|SO<br>2|NO<br>X|CO|MP<br>2.5|MP<br>10|COVs|Unidad|
|---|---|---|---|---|---|---|---|
|Transito camino pavimentado|--|--|--|0,22|0,91|--|t/año|
|Motor vehículos Caminos pavimentados|<0,01|0,66|0,16|0,15|0,15|0,03|t/año|
|**Total**|**<0,01**|**0,66**|**0,16**|**0,37**|**1,07**|**0,03**|**t/año**|

Fuente: Algoritmos SpA, 2023.

_**Inventario y Modelación de Emisiones ATM037-23**_ _55/106_
_Proyecto Alba_

_Abril, 2023_

**11** **Modelación de Dispersión de Contaminantes**

Con el fin de evaluar la dispersión de los contaminantes generados por las fuentes,
como material particulado (MP 10 ), material particulado respirable fino (MP 2,5 ),
dióxido de azufre (SO 2 ), óxidos de nitrógeno (NO X ) y monóxido de carbono (CO)
para la fase de construcción año 2, fase de operación actual, fase de operación con
Proyecto, se realizó una modelación de dispersión de contaminantes considerando
las emisiones generadas.

**11.1** **Modelo de Dispersión Atmosférica**

**11.1.1** **Base Teórica**

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
simulación se hace para una pluma de emisión, continúa o discreta, se trata de
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

**11.1.2** **Sistema de Modelación WRF - CALPUFF**

Para determinar el efecto que tendrán las emisiones de material particulado y gases
provenientes de la operación del Proyecto, se utiliza un sistema acoplado de dos
modelos: El modelo atmosférico Weather Research and Forecasting (WRF), y el
modelo CALPUFF, simulador de la dispersión de contaminantes en la atmósfera.
Ambos conforman el sistema de modelación WRF-CALPUFF.

_**Inventario y Modelación de Emisiones ATM037-23**_ _56/106_
_Proyecto Alba_

_Abril, 2023_

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

_**Inventario y Modelación de Emisiones ATM037-23**_ _57/106_
_Proyecto Alba_

_Abril, 2023_

**11.2** **Variables de Entrada ingresados al Sistema de Modelación**

El sistema de modelación WRF-CALPUFF requiere de la siguiente información de
entrada:

 **Archivos NCEP-FNL (Final):** Información de entrada para el modelo WRF,
con una resolución espacial de 1 km x 1 km (url:
https://rda.ucar.edu/datasets/ds083.2/).

 - **Uso de Suelo** **[g]** **:** Esta información permite definir los coeficientes de
rugosidad superficial, razón de Bowen y albedo. Los usos de suelo presentes
en el área de estudio se encuentran en la siguiente tabla.

_**Tabla N° 57**_
_**Características del Uso de Suelo**_

|Uso de Suelo|Albedoh|Col3|Razón de Boweni|Col5|Rugosidad<br>Superficial (cm)|Col7|
|---|---|---|---|---|---|---|
|**Uso de Suelo**|**Verano**|**Invierno**|**Verano**|**Invierno**|**Verano**|**Invierno**|
|Bosque Mixto|13|14|0,5|0,5|50|50|
|Mezcla de hierbas|20|24|1|1|11|10|
|Urbano|18|18|1,5|1,5|50|50|
|Escasa<br>vegetación|25|25|1|1|10|10|
|Cuerpos de agua|8|8|0|0|1|1|

Fuente: Algoritmos SpA, 2023

La siguiente figura presenta los usos de suelo presentes en el área de estudio,
indicados en la tabla anterior. Se destaca que la nomenclatura utilizada para definir
las categorías de uso de suelo proviene del modelo WRF-ARW a través de “USGS
24-Category Landuse and Landcover”.

g Información obtenida a partir de preprocesador CTGPROC
h Albedo: reflectividad a la luz solar del suelo (expresada como fracción respecto a la unidad)
i Razón de Bowen: definida como la razón entre flujos sensibles y latentes, a nivel de superficie.

_**Inventario y Modelación de Emisiones ATM037-23**_ _58/106_
_Proyecto Alba_

_Abril, 2023_

_**Figura N° 8**_
_**Uso de Suelo**_

Fuente: Algoritmos SpA, 2023

_**Inventario y Modelación de Emisiones ATM037-23**_ _59/106_
_Proyecto Alba_

_Abril, 2023_

 - **Data de emisiones**, Corresponde al valor emitido por cada fuente
considerada en los diferentes escenarios de modelación (Ver capítulo 10)

 - **Topografía del área de modelación:** Esta información es obtenida de
datos satelitales para la zona de estudio. En la siguiente figura se muestra
la topografía donde está ubicado el proyecto.

_**Inventario y Modelación de Emisiones ATM037-23**_ _60/106_
_Proyecto Alba_

_Abril, 2023_

_**Figura N° 9**_

_**Topografía**_

Fuente: Algoritmos SpA, 2023

_**Inventario y Modelación de Emisiones ATM037-23**_ _61/106_
_Proyecto Alba_

_Abril, 2023_

 **Ubicación de puntos de interés**, Esto permite la evaluación de los
resultados en comparación con la normativa aplicable. La ubicación de los
puntos de interés considerados se encuentra en la Tabla N° 58. En la Figura
N° 10, se muestra la ubicación de dicho punto.

_**Tabla N° 58**_
_**Localización Puntos Discretos**_ _**[j]**_

|Punto de<br>Interés|Identificación|Tipo de Punto<br>de Interés|Coordenadas UTM|Col5|Elevación (m)|
|---|---|---|---|---|---|
|**Punto de**<br>**Interés**|**Identificación**|**Tipo de Punto**<br>**de Interés**|**Este (m)**|**Norte (m)**|**Norte (m)**|
|1|R1-Estación<br>Jardín Infantil|Receptor<br>Norma Primaria|352.064|7.444.407|13|
|2|R2-Mejillones|Receptor<br>Norma Primaria|352.716|7.444.460|17|
|3|R3-Estación<br>Angamos I|Receptor<br>Norma Primaria|357.834|7.446.478|39|
|4|R4-Estación<br>Angamos II|Receptor<br>Norma Primaria|360.837|7.449.621|38|

Fuente: Algoritmos SpA, 2023.

j Datum WGS84, coordenadas UTM.

_**Inventario y Modelación de Emisiones ATM037-23**_ _62/106_
_Proyecto Alba_

_Abril, 2023_

_**Figura N° 10**_
_**Ubicación Puntos de Interés**_

Fuente: Algoritmos SpA, 2023.

_**Inventario y Modelación de Emisiones ATM037-23**_ _63/106_
_Proyecto Alba_

_Abril, 2023_

**12** **Resultados Modelación**

Se presentan los resultados obtenidos de la modelación atmosférica para este
estudio con el fin de evaluar el aporte de material particulado (MP 10 ), material
particulado respirable fino (MP 2,5 ), dióxido de azufre (SO 2 ), óxidos de nitrógeno
(NO X ) y monóxido de carbono (CO), para el Proyecto Alba, en la fase de
construcción año 2, operación actual de ambas centrales y operación con proyecto.

**12.1** **Campos de Viento**

Mediante la aplicación del modelo WRF se simuló el comportamiento de los campos
de vientos sobre el área del Proyecto, para cada una de las horas consideradas en
la modelación. Dichos campos de vientos permitirán determinar posteriormente la
dispersión de los contaminantes, a través de la aplicación del modelo CALPUFF.

A modo de ejemplo se seleccionó el día 04 de julio del año 2021 correspondiente
al Percentil 99 Horario de NO 2 del punto de máximo impacto, para representar el
comportamiento de los vientos superficiales en horas representativas del día, en la
madrugada (06:00 hs.), a medio día (12:00 hs.), durante la tarde (18:00 hs.) y
en la noche (00:00 hs.).

_**Inventario y Modelación de Emisiones ATM037-23**_ _64/106_
_Proyecto Alba_

_Abril, 2023_

_**Figura N° 11**_
_**Campos de Viento a las 00:00 horas.**_

Fuente: Algoritmos SpA, 2023.

_**Inventario y Modelación de Emisiones ATM037-23**_ _65/106_
_Proyecto Alba_

_Abril, 2023_

_**Figura N° 12**_
_**Campos de Viento a las 06:00 horas**_

Fuente: Algoritmos SpA, 2023.

_**Inventario y Modelación de Emisiones ATM037-23**_ _66/106_
_Proyecto Alba_

_Abril, 2023_

_**Figura N° 13**_
_**Campos de Viento a las 12:00 horas**_

Fuente: Algoritmos SpA, 2023.

_**Inventario y Modelación de Emisiones ATM037-23**_ _67/106_
_Proyecto Alba_

_Abril, 2023_

_**Figura N° 14**_
_**Campos de Viento a las 18:00 horas.**_

Fuente: Algoritmos SpA, 2023.

_**Inventario y Modelación de Emisiones ATM037-23**_ _68/106_
_Proyecto Alba_

_Abril, 2023_

**12.2** **Aportes Obtenidos de la Modelación**

Mediante la aplicación del modelo WRF-CALPUFF fue posible obtener las
concentraciones de material particulado respirable (MP 10 ), material particulado
respirable fino (MP 2,5 ), dióxido de azufre (SO 2 ), óxidos de nitrógeno (NO 2 ) y
monóxido de carbono (CO), que aportará el proyecto, basándose en los campos de
vientos generados por la modelación meteorológica realizada con WRF.

Los aportes del proyecto fueron evaluados en los sectores de su entorno, para el
análisis de cumplimiento de las normas primarias y secundarias de calidad del aire
las que, de acuerdo con su cumplimiento, permitirá al titular determinar si el
proyecto generará efectos adversos significativos sobre la salud de la población y
sobre la calidad y cantidad de los recursos naturales renovables.

**12.2.1** **Aporte en Puntos de Interés**

En la siguiente tabla se presenta los aportes obtenidos por la modelación de la
construcción del proyecto, los aportes de las fuentes actuales de la planta y los
aportes de las fuentes del proyecto Alba en los puntos de interés. Es importante
mencionar que en la Tabla N° 60 solo considera las fuentes del proyecto Alba, la
Tabla N° 61 solo las fuentes del Proyecto Adelaida, la Tabla N° 62 solo las fuentes
del proyecto de Aerogeneradores y la Tabla N° 63 considera las fuentes del
proyecto Alba, proyecto Adelaida y Proyecto de Aerogeneradores.

_**Inventario y Modelación de Emisiones ATM037-23**_ _69/106_
_Proyecto Alba_

_Abril, 2023_

_**Tabla N° 59**_
_**Aporte de las fuentes de en Punto de interés, Fase Construcción Año 2**_

|Receptor de<br>Interés|MP ug/m<br>10|Col3|MP ug/m<br>2.5|Col5|SO ug/m<br>2 3|Col7|Col8|Col9|Col10|Col11|NO ug/m<br>2 3|Col13|CO ug/m<br>3|Col15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor de**<br>**Interés**|<br>**Primaria** <br><br>|<br>**Primaria** <br><br>|**Primaria** <br><br>|**Primaria** <br><br>|**Primaria**|**Primaria**|**Primaria**|**Secundaria**|**Secundaria**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|
|**Receptor de**<br>**Interés**|**Media** <br>**Anual**|**P98** <br>**Diario**|**Media** <br>**Anual**|**P98** <br>**Diario**|~~**Media**~~<br>**Anual**|~~**P99**~~<br>**Diario**|~~**P98.5**~~<br>**Horario**|<br>~~**Media**~~<br>**Anual**|~~**P99.7**~~<br>**Diario**|~~**P99.73**~~<br>**Horario**|<br>~~**Media**~~<br>**Anual** <br><br>|**P99**<br>**Horario**|~~**P99**~~<br>**8 H** <br><br>|**P99**<br>**Horario**|
|Norma <br>|50 <br>|130|20|50|60|150|350|80|365|1.000|100|400|10.000|30.000|
|R1- Estación <br>Jardín|0,06|0,27|0,03|0,24|<0,01|<0,01|<0,01|<0,01|<0,01|0,07|<0,01|3,44|<0,01|0,21|
|R2-Mejillones<br>|<br>0,06|0,33|0,06|0,3|<0,01|<0,01|<0,01|<0,01|<0,01|0,08|<0,01|4,43|<0,01|0,29|
|R3-Estación <br>Angamos I <br>|0,48|2,28|0,36|1,77|<0,01|0,09|<0,01|<0,01|0,10|0,34|0,80|26,16|0,41|1,55|
|R4-Estación <br>Angamos II|0,42|1,92|0,33|1,65|0,05|0,11|<0,01|0,05|<0,01|0,54|1,20|37,71|0,56|2,24|

Fuente: Algoritmos SpA, 2023

_**Tabla N° 60**_
_**Aporte de las fuentes en Punto de interés, Fase Operación Actual**_

|Receptor de<br>Interés|MP ug/m<br>10|Col3|MP ug/m<br>2.5|Col5|SO ug/m<br>2 3|Col7|Col8|Col9|Col10|Col11|NO ug/m<br>2 3|Col13|CO ug/m<br>3|Col15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor de** <br>**Interés **|**Primaria** <br><br>|**Primaria** <br><br>|**Primaria** <br><br>|**Primaria** <br><br>|**Primaria**|**Primaria**|**Primaria**|**Secundaria**|**Secundaria**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|
|**Receptor de** <br>**Interés **|**Media** <br>**Anual**|**P98** <br>**Diario**|**Media** <br>**Anual**|**P98** <br>**Diario**|~~**Media**~~<br>**Anual**|~~**P99**~~<br>**Diario**|~~**P98.5**~~<br>**Horario**|~~**Media**~~<br>**Anual**|~~**P99.7**~~<br>**Diario**|~~**P99.73**~~<br>**Horario**|~~**Media**~~<br>**Anual**|**P99**<br>**Horario**|<br>~~**P99**~~<br>**8 H**|**P99**<br>**Horario**|
|Norma <br>|50|130|20|50|60|150|350|80|365|1.000|100|400|10.000|30.000|
|R1- Estación <br>Jardín Infantil|1,49|6,91|1,48|6,89|1,68|10,65|15,13|1,68|14,97|43,10|1,45|76,43|<0,01|0,01|
|R2-Mejillones <br>|1,61|6,91|1,61|6,90|1,85|8,94|16,86|1,85|13,36|45,70|1,60|84,33|<0,01|0,02|
|R3-Estación <br>Angamos I <br>|3,11|11,37|3,04|11,34|6,14|26,72|74,95|6,14|29,37|156,23|6,24|241,37|<br>0,06|0,16|
|R4-Estación <br>Angamos II|3,58|10,55|3,52|10,49|9,12|29,47|116,49|9,12|33,43|212,58|8,96|343,80|<br>0,02|0,04|

Fuente: Algoritmos SpA, 2023

_**Inventario y Modelación de Emisiones ATM037-23**_ _70/106_
_Proyecto Alba_

_Abril, 2023_

_**Tabla N° 61**_
_**Aporte de Proyecto Alba en Punto de interés, Fase Operación con proyecto (Sin Adelaida ni**_

_**Aerogeneradores)**_

|Receptor de<br>Interés|MP ug/m<br>10|Col3|MP ug/m<br>2,5|Col5|SO ug/m<br>2 3|Col7|Col8|Col9|Col10|Col11|NO ug/m<br>2 3|Col13|CO ug/m<br>3|Col15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor de** <br>**Interés **|**Primaria** <br><br>|**Primaria** <br><br>|**Primaria** <br><br>|**Primaria** <br><br>|**Primaria**|**Primaria**|**Primaria**|**Secundaria**|**Secundaria**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|
|**Receptor de** <br>**Interés **|**Media** <br>**Anual**|**P98** <br>**Diario**|**Media** <br>**Anual**|**P98** <br>**Diario**|**Media**<br>**Anual**|**P99**<br>**Diario**|**P98.5**<br>**Horari**|**Media**<br>**Anual**|**P99.7**<br>**Diario**|**P99.**<br>**73**|**Media**<br>**Anual**|**P99**<br>**Horario**|<br>**P99**<br>**8 H**|**P99**<br>**Horario**|
|Norma <br>|50 <br>|130|20|50|60|150|350|80|365|1.000|100|400|10.000|30.000|
|R1- Estación Jardín<br>Infantil|<br>0,61|3,18|0,60|3,16|0,67|4,14|6,20|0,67|6,35|18,44|0,61|35,75|0,00|0,01|
|R2-Mejillones <br>|0,67|3,53|0,67|3,52|0,74|4,03|6,90|0,74|5,98|22,34|0,67|36,84|0,00|0,01|
|R3-Estación <br>Angamos I <br>|1,33|4,82|1,27|4,76|2,36|10,96|28,30|2,36|13,24|65,18|2,54|117,28|0,03|0,08|
|R4-Estación <br>Angamos II|1,53|4,12|1,47|4,11|4,14|14,16|56,20|4,14|17,37|113,94|4,24|183,51|0,01|0,02|

Fuente: Algoritmos SpA, 2023

_**Tabla N° 62**_
_**Aporte de Adelaida en Punto de interés, Fase Operación.**_

|Receptor de<br>Interés|MP ug/m<br>10|Col3|MP ug/m<br>2,5|Col5|SO ug/m<br>2 3|Col7|Col8|Col9|Col10|Col11|NO ug/m<br>2 3|Col13|CO ug/m<br>3|Col15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor de** <br>**Interés **|**Primaria** <br><br>|**Primaria** <br><br>|**Primaria** <br><br>|**Primaria** <br><br>|**Primaria**|**Primaria**|**Primaria**|**Secundaria**|**Secundaria**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|
|**Receptor de** <br>**Interés **|**Media** <br>**Anual**|**P98** <br>**Diario**|**Media** <br>**Anual**|**P98** <br>**Diario**|**Media**<br>**Anual**|**P99**<br>**Diario**|**P98.5**<br>**Horari**|**Media**<br>**Anual**|**P99.7**<br>**Diario**|**P99.**<br>**73**|**Media**<br>**Anual**|**P99**<br>**Horario**|<br>**P99**<br>**8 H**|**P99**<br>**Horario**|
|Norma <br>|50 <br>|130|20|50|60|150|350|80|365|1.000|100|400|10.000|30.000|
|R1- Estación Jardín<br>Infantil|<br><0,01|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|
|R2-Mejillones <br>|<0,01|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|
|R3-Estación <br>Angamos I <br>|0,02|0,09|0,01|0,02|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|
|R4-Estación <br>Angamos II|0,01|0,02|0,00|0,00|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|

Fuente: Algoritmos SpA, 2023

_**Inventario y Modelación de Emisiones ATM037-23**_ _71/106_
_Proyecto Alba_

_Abril, 2023_

_**Tabla N° 63**_
_**Aporte de Aerogeneradores en Punto de interés, Fase Operación.**_

|Receptor de<br>Interés|MP ug/m<br>10|Col3|MP ug/m<br>2,5|Col5|SO ug/m<br>2 3|Col7|Col8|Col9|Col10|Col11|NO ug/m<br>2 3|Col13|CO ug/m<br>3|Col15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor de** <br>**Interés **|**Primaria** <br><br>|**Primaria** <br><br>|**Primaria** <br><br>|**Primaria** <br><br>|**Primaria**|**Primaria**|**Primaria**|**Secundaria**|**Secundaria**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|
|**Receptor de** <br>**Interés **|**Media** <br>**Anual**|**P98** <br>**Diario**|**Media** <br>**Anual**|**P98** <br>**Diario**|**Media**<br>**Anual**|**P99**<br>**Diario**|**P98.5**<br>**Horari**|**Media**<br>**Anual**|**P99.7**<br>**Diario**|**P99.**<br>**73**|**Media**<br>**Anual**|**P99**<br>**Horario**|<br>**P99**<br>**8 H**|**P99**<br>**Horario**|
|Norma <br>|50 <br>|130|20|50|60|150|350|80|365|1.000|100|400|10.000|30.000|
|R1- Estación Jardín<br>Infantil|<br><0,01|0,02|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|
|R2-Mejillones <br>|<0,01|0,02|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|
|R3-Estación <br>Angamos I <br>|0,02|0,07|<0,01|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|
|R4-Estación <br>Angamos II|0,01|0,03|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|

Fuente: Algoritmos SpA, 2023

_**Tabla N° 64**_
_**Aporte de Proyecto Alba en Punto de interés, Fase Operación con proyecto (Con Adelaida y**_

_**Aerogeneradores)**_

|Receptor de<br>Interés|MP ug/m<br>10|Col3|MP ug/m<br>2,5|Col5|SO ug/m<br>2 3|Col7|Col8|Col9|Col10|Col11|NO ug/m<br>2 3|Col13|CO ug/m<br>3|Col15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor de** <br>**Interés **|**Primaria** <br><br>|**Primaria** <br><br>|**Primaria** <br><br>|**Primaria** <br><br>|**Primaria**|**Primaria**|**Primaria**|**Secundaria**|**Secundaria**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|
|**Receptor de** <br>**Interés **|**Media** <br>**Anual**|**P98** <br>**Diario**|**Media** <br>**Anual**|**P98** <br>**Diario**|**Media**<br>**Anual**|**P99**<br>**Diario**|**P98.5**<br>**Horari**|**Media**<br>**Anual**|**P99.7**<br>**Diario**|**P99.**<br>**73**|**Media**<br>**Anual**|**P99**<br>**Horario**|<br>**P99**<br>**8 H**|**P99**<br>**Horario**|
|Norma <br>|50 <br>|130|20|50|60|150|350|80|365|1.000|100|400|10.000|30.000|
|R1- Estación Jardín<br>Infantil|<br>0,61|3,20|0,60|3,16|0,67|4,14|6,20|0,67|6,35|18,44|0,61|35,75|<0,01|0,01|
|R2-Mejillones <br>|0,67|3,55|0,67|3,52|0,74|4,03|6,90|0,74|5,98|22,34|0,67|36,84|<0,01|0,01|
|R3-Estación <br>Angamos I <br>|1,37|4,98|1,28|4,77|2,36|10,96|28,30|2,36|13,24|65,18|2,54|117,29|0,03|0,08|
|R4-Estación <br>Angamos II|1,55|4,17|1,47|4,11|4,14|14,16|56,20|4,14|17,37|113,94|4,24|183,51|0,01|0,02|

Fuente: Algoritmos SpA, 2023

_**Inventario y Modelación de Emisiones ATM037-23**_ _72/106_
_Proyecto Alba_

_Abril, 2023_

**12.2.2** **Ajustes de Resultados de la Modelación por Incertidumbre**

Acorde al análisis de incertidumbre de la modelación WRF presentado en el capítulo
7 del presente informe, al comparar los ciclos diarios promedios observados y de
pronóstico para la Estación Angamos I, se obtiene que el modelo subestima los
valores observados. Esta situación genera condiciones desfavorables con respecto
a la ventilación en el área de interés, ya que la meteorología generada por el
modelo WRF es utilizada como dato de entrada para el modelo de dispersión
CALPUFF. Debido a lo anterior, no se realizará un ajuste a los resultados modelados
debido a que esta subestimación genera el escenario más desfavorable para la
dispersión de contaminantes en el área de interés.

_**Inventario y Modelación de Emisiones ATM037-23**_ _73/106_
_Proyecto Alba_

_Abril, 2023_

**12.3** **Análisis de Cumplimiento de Normativa Ambiental**

Para establecer el cumplimiento de la normativa ambiental vigente de calidad del aire para MP 10, MP 2,5, SO 2, NO 2, y
CO, en la siguiente tabla se muestra la comparación del Aporte del Proyecto (AP) con la normativa vigente mediante
el porcentaje que representa el aporte del Proyecto (%AP/Norma) para cada Receptor de Interés (RI). En las tabla N°
66, tabla N° 67 y tabla N°68 se muestran los aportes indivuales del proyecto Alba, Adelaida y Aerogeneradores,
respectivamente. En la tabla N°69 se muestra el aporte total del proyecto (Alba, Adelaida y Aerogeneradores) en la
fase de operación.

_**Tabla N° 65**_
_**Análisis Normativo en Punto de interés, Fase Construcción Año 2**_

|RECEPT<br>ORES|MP μg/m3<br>10|Col3|MP ug/m3<br>2,5|Col5|SO ug/m3<br>2|Col7|Col8|Col9|Col10|Col11|NO ug/m3<br>2|Col13|CO ug/m3|Col15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**RECEPT** <br>**ORES**|**Primaria** <br><br>|**Primaria** <br><br>|**Primaria** <br><br>|**Primaria** <br><br>|**Primaria** <br><br>|**Primaria** <br><br>|**Primaria** <br><br>|**Secundaria** <br><br><br>|**Secundaria** <br><br><br>|**Secundaria** <br><br><br>|**Primaria** <br>|**Primaria** <br>|**Primaria**|**Primaria**|
|**RECEPT** <br>**ORES**|**Media** <br>**Anual**|**P98** <br>**Diario**|**Media** <br>**Anual**|**P98** <br>**Diario**|**Media** <br>**Anual**|**P99** <br>**Diario**|**P98**<br>**Horario**|**Media** <br>**Anual**|**P99,7** <br>**Diario**|**P99,73** <br>**Horario**|**Media**<br>**Anual**|**P98** <br>**Horario**|**P99 **<br>**8 h**|**P99 **<br>**Horario**|
|Norma <br>|50|130|20|50|60|150|350|80|365|1.000|100|400|10.000|30.000|
|R1- <br>Estación <br>Jardín <br>Infantil <br>|0,12%|0,21%|0,15%|0,48%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,01%|<0,01%|0,86%|<0,01%|<0,01%|
|R2- <br>Mejillones <br>|0,12%|0,25%|0,30%|0,60%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,01%|<0,01%|1,11%|<0,01%|<0,01%|
|R3- <br>Estación <br>Angamos <br>I <br>|0,96%|1,75%|1,80%|3,54%|<0,01%|0,06%|<0,01%|<0,01%|0,03%|0,03%|0,80%|6,54%|<0,01%|0,01%|
|R4- <br>Estación <br>Angamos <br>II|0,84%|1,48%|1,65%|3,30%|0,08%|0,07%|<0,01%|0,06%|<0,01%|0,05%|1,20%|9,43%|0,01%|0,01%|

Fuente: Algoritmos SpA, 2023

_**Inventario y Modelación de Emisiones ATM037-23**_ _74/106_
_Proyecto Alba_

_Abril, 2023_

_**Tabla N° 66**_
_**Análisis Normativo en Punto de interés, Fase Operación Actual**_

|RECEPTORES|MP μg/m3<br>10|Col3|MP ug/m3<br>2,5|Col5|SO ug/m3<br>2|Col7|Col8|Col9|Col10|Col11|NO ug/m3<br>2|Col13|CO ug/m3|Col15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**RECEPTORES**|**Primaria** <br><br>|**Primaria** <br><br>|**Primaria** <br><br>|**Primaria** <br><br>|**Primaria** <br><br>|**Primaria** <br><br>|**Primaria** <br><br>|**Secundaria** <br><br><br>|**Secundaria** <br><br><br>|**Secundaria** <br><br><br>|**Primaria** <br><br><br>|**Primaria** <br><br><br>|**Primaria** <br><br>|**Primaria** <br><br>|
|**RECEPTORES**|**Media** <br>**Anual**|**P98** <br>**Diario**|**Media** <br>**Anual**|**P98** <br>**Diario**|**Media** <br>**Anual**|**P99** <br>**Diario**|**P98**<br>**Horario**|**Media** <br>**Anual**|**P99,7** <br>**Diario**|**P99,73** <br>**h**|**Media** <br>**Anual**|**P99** <br>**Horario**|**P99** <br>**8 h**|**P99** <br>**Horario**|
|Norma|50|130|20|50|60|150|350|80|365|1.000|100|400|10.000|30.000|
|R1- Estación <br>Jardín|3,0%|5,3%|7,4%|13,8%|2,8%|7,1%|4,3%|2,1%|4,1%|4,3%|1,4%|19,1%|<0,01%|<0,01%|
|R2-Mejillones <br>|3,2%|5,3%|8,0%|13,8%|3,1%|6,0%|4,8%|2,3%|3,7%|4,6%|1,6%|21,1%|<0,01%|<0,01%|
|R3-Estación <br>Angamos I <br>|6,2%|8,8%|15,2%|22,7%|10,2%|17,8%|21,4%|7,7%|8,1%|15,6%|6,2%|60,4%|<0,01%|<0,01%|
|R4-Estación <br>Angamos II|7,2%|8,1%|17,6%|21,0%|15,2%|19,7%|33,3%|11,4%|9,2%|21,3%|9,0%|86,0%|<0,01%|<0,01%|

Fuente: Algoritmos SpA, 2023

_**Tabla N° 67**_
_**Análisis Normativo en Punto de interés, Fase Operación con proyecto**_

|RECEPTORES|MP μg/m3<br>10|Col3|MP ug/m3<br>2,5|Col5|SO ug/m3<br>2|Col7|Col8|Col9|Col10|Col11|NO ug/m3<br>2|Col13|CO ug/m3|Col15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**RECEPTORES**|**Primaria** <br><br>|**Primaria** <br><br>|**Primaria** <br><br>|**Primaria** <br><br>|**Primaria** <br><br>|**Primaria** <br><br>|**Primaria** <br><br>|**Secundaria** <br><br><br>|**Secundaria** <br><br><br>|**Secundaria** <br><br><br>|**Primaria** <br><br><br>|**Primaria** <br><br><br>|**Primaria** <br><br>|**Primaria** <br><br>|
|**RECEPTORES**|**Media** <br>**Anual**|**P98** <br>**Diario**|**Media** <br>**Anual**|**P98** <br>**Diario**|**Media** <br>**Anual**|**P99** <br>**Diario**|**P98**<br>**Horario**|**Media** <br>**Anual**|**P99,7** <br>**Diario**|**P99,73** <br>**Horario**|<br>**Media** <br>**Anual**|**P99** <br>**Horario**|**P99** <br>**8 h**|**P99** <br>**Horario**|
|Norma <br>|50|130|20|50|60|150|350|80|365|1.000|100|400|10.000|30.000|
|R1- Estación Jardín <br>Infantil|1,2%|2,4%|3,0%|6,3%|1,1%|2,8%|1,8%|0,8%|1,7%|1,8%|0,6%|8,9%|<0,01%|<0,01%|
|R2-Mejillones <br>|1,3% <br>|2,7%|3,3%|7,0%|1,2%|2,7%|2,0%|0,9%|1,6%|2,2%|0,7%|9,2%|<0,01%|<0,01%|
|R3-Estación Angamos<br>I|<br>2,7%|3,7%|6,4%|9,5%|3,9%|7,3%|8,1%|2,9%|3,6%|6,5%|2,5%|29,3%|<0,01%|<0,01%|
|R4-Estación <br>Angamos|3,1%|3,2%|7,4%|8,2%|6,9%|9,4%|16,1%|5,2%|4,8%|11,4%|4,2%|45,9%|<0,01%|<0,01%|

Fuente: Algoritmos SpA, 2023

_**Inventario y Modelación de Emisiones ATM037-23**_ _75/106_
_Proyecto Alba_

_Abril, 2023_

_**Tabla N° 68**_
_**Análisis Normativo en Punto de interés, Adelaida, Fase Operación**_

|RECEPTORES|MP μg/m3<br>10|Col3|MP ug/m3<br>2,5|Col5|SO ug/m3<br>2|Col7|Col8|Col9|Col10|Col11|NO ug/m3<br>2|Col13|CO ug/m3|Col15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|<br>**RECEPTORES**|**Primaria** <br><br>|**Primaria** <br><br>|**Primaria** <br><br>|**Primaria** <br><br>|**Primaria** <br><br>|**Primaria** <br><br>|**Primaria** <br><br>|**Secundaria** <br><br><br>|**Secundaria** <br><br><br>|**Secundaria** <br><br><br>|**Primaria** <br><br>|**Primaria** <br><br>|**Primaria** <br><br>|**Primaria** <br><br>|
|<br>**RECEPTORES**|**Media** <br>**Anual**|**P98** <br>**Diario**|**Media** <br>**Anual**|**P98** <br>**Diario**|**Media** <br>**Anual**|**P99** <br>**Diario**|**P98**<br>**Horario**|**Media** <br>**Anual**|**P99,7** <br>**Diario**|**P99,73** <br>**Horario**|<br>**Media** <br>**Anual**|**P99** <br>**Horario**|**P99** <br>**8 h**|**P99** <br>**Horario**|
|Norma <br>|50|130|20|50|60|150|350|80|365|1.000|100|400|10.000|30.000|
|R1- Estación Jardín <br>Infantil|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|
|R2-Mejillones|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|
|R3-Estación <br>Angamos|<0,01%|0,1%|0,1%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|
|R4-Estación <br>Angamos|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|

Fuente: Algoritmos SpA, 2023

_**Tabla N° 69**_
_**Análisis Normativo en Punto de interés, Aerogeneradores, Fase Operación**_

|RECEPTORES|MP μg/m3<br>10|Col3|MP ug/m3<br>2,5|Col5|SO ug/m3<br>2|Col7|Col8|Col9|Col10|Col11|NO ug/m3<br>2|Col13|CO ug/m3|Col15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**RECEPTORES**|<br>**Primaria** <br><br>|<br>**Primaria** <br><br>|**Primaria** <br><br>|**Primaria** <br><br>|**Primaria** <br><br>|**Primaria** <br><br>|**Primaria** <br><br>|**Secundaria** <br><br><br>|**Secundaria** <br><br><br>|**Secundaria** <br><br><br>|**Primaria** <br><br>|**Primaria** <br><br>|**Primaria** <br><br>|**Primaria** <br><br>|
|**RECEPTORES**|**Media** <br>**Anual**|**P98** <br>**Diario**|**Media** <br>**Anual**|**P98** <br>**Diario**|**Media** <br>**Anual**|**P99** <br>**Diario**|**P98**<br>**Horario**|**Media** <br>**Anual**|**P99,7** <br>**Diario**|**P99,73** <br>**Horario**|**Media** <br>**Anual**|**P99** <br>**Horario**|**P99** <br>**8 h**|**P99** <br>**Horario**|
|Norma|50|130|20|50|60|150|350|80|365|1.000|100|400|10.000|30.000|
|R1- Estación <br>Jardín|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|
|R2-Mejillones|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|
|R3-Estación <br>Angamos|<0,01%|0,1%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|
|R4-Estación <br>Angamos|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|

Fuente: Algoritmos SpA, 2023

_**Inventario y Modelación de Emisiones ATM037-23**_ _76/106_
_Proyecto Alba_

_Abril, 2023_

_**Tabla N° 70**_
_**Análisis Normativo en Punto de interés, Alba, Adeliada y Aerogeneradores, Fase Operación con proyecto**_

|RECEPTORES|MP μg/m3<br>10|Col3|MP ug/m3<br>2,5|Col5|SO ug/m3<br>2|Col7|Col8|Col9|Col10|Col11|NO ug/m3<br>2|Col13|CO ug/m3|Col15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**RECEPTORES**|**Primaria** <br><br>|**Primaria** <br><br>|**Primaria** <br><br>|**Primaria** <br><br>|**Primaria** <br><br>|**Primaria** <br><br>|**Primaria** <br><br>|**Secundaria** <br><br><br>|**Secundaria** <br><br><br>|**Secundaria** <br><br><br>|**Primaria** <br><br><br>|**Primaria** <br><br><br>|**Primaria** <br><br>|**Primaria** <br><br>|
|**RECEPTORES**|**Media** <br>**Anual**|**P98** <br>**Diario**|**Media** <br>**Anual**|**P98** <br>**Diario**|**Media** <br>**Anual**|**P99** <br>**Diario**|**P98**<br>**Horario**|**Media** <br>**Anual**|**P99,7** <br>**Diario**|**P99,73** <br>**Horario**|<br>**Media** <br>**Anual**|**P99** <br>**Horario**|**P99** <br>**8 h**|**P99** <br>**Horario**|
|Norma <br>|50|130|20|50|60|150|350|80|365|1.000|100|400|10.000|30.000|
|R1- Estación Jardín <br>Infantil|1,2%|2,5%|3,0%|6,3%|1,1%|2,8%|1,8%|0,8%|1,7%|1,8%|0,6%|8,9%|<0,01%|<0,01%|
|R2-Mejillones <br>|1,3% <br>|2,7%|3,4%|7,0%|1,2%|2,7%|2,0%|0,9%|1,6%|2,2%|0,7%|9,2%|<0,01%|<0,01%|
|R3-Estación Angamos<br>I|<br>2,7%|3,8%|6,4%|9,5%|3,9%|7,3%|8,1%|2,9%|3,6%|6,5%|2,5%|29,3%|<0,01%|<0,01%|
|R4-Estación <br>Angamos|3,1%|3,2%|7,4%|8,2%|6,9%|9,4%|16,1%|5,2%|4,8%|11,4%|4,2%|45,9%|<0,01%|<0,01%|

Fuente: Algoritmos SpA, 2023

_**Inventario y Modelación de Emisiones ATM037-23**_ _77/106_
_Proyecto Alba_

_Abril, 2023_

**12.4** **Mapas de Isoconcentraciones**

A continuación, se presentan las isolíneas de concentración de MP 10, MP 2,5, NO 2, CO
y SO 2, correspondiente a la fase de construcción año 2 del proyecto y Operación
con proyecto (Alba, Adelaida y Aerogeneradores).

_**Inventario y Modelación de Emisiones ATM037-23**_ _78/106_
_Proyecto Alba_

_Abril, 2023_

_**Figura N° 15**_
_**Percentil 98 Promedio Diario de MP**_ _**10**_ _**Fase Construcción año 2**_

Fuente: Algoritmos SpA, 2023

_**Inventario y Modelación de Emisiones ATM037-23**_ _79/106_
_Proyecto Alba_

_Abril, 2023_

_**Figura N° 16**_
_**Promedio del Período de MP**_ _**10**_ _**Fase Construcción año 2**_

Fuente: Algoritmos SpA, 2023

_**Inventario y Modelación de Emisiones ATM037-23**_ _80/106_
_Proyecto Alba_

_Abril, 2023_

_**Figura N° 17**_
_**Percentil 98 Promedio Diario de MP**_ _**2,5**_ _**Fase Construcción año 2**_

Fuente: Algoritmos SpA, 2023

_**Inventario y Modelación de Emisiones ATM037-23**_ _81/106_
_Proyecto Alba_

_Abril, 2023_

_**Figura N° 18**_
_**Promedio del Período de MP**_ _**2,5**_ _**Fase Construcción año 2**_

Fuente: Algoritmos SpA, 2023

_**Inventario y Modelación de Emisiones ATM037-23**_ _82/106_
_Proyecto Alba_

_Abril, 2023_

_**Figura N° 19**_
_**Percentil 99 Promedio Diario de SO**_ _**2**_ _**Fase Construcción año 2**_

Fuente: Algoritmos SpA, 2023

_**Inventario y Modelación de Emisiones ATM037-23**_ _83/106_
_Proyecto Alba_

_Abril, 2023_

_**Figura N° 20**_
_**Percentil 98,5 Promedio Horario de SO**_ _**2**_ _**Fase Construcción año 2**_

Fuente: Algoritmos SpA, 2023

_**Inventario y Modelación de Emisiones ATM037-23**_ _84/106_
_Proyecto Alba_

_Abril, 2023_

_**Figura N° 21**_
_**Percentil 99,7 Promedio Diario de SO**_ _**2**_ _**Fase Construcción año 2**_

Fuente: Algoritmos SpA, 2023

_**Inventario y Modelación de Emisiones ATM037-23**_ _85/106_
_Proyecto Alba_

_Abril, 2023_

_**Figura N° 22**_
_**Percentil 99,73 Promedio Horario de SO**_ _**2**_ _**Fase Construcción año 2**_

Fuente: Algoritmos SpA, 2023

_**Inventario y Modelación de Emisiones ATM037-23**_ _86/106_
_Proyecto Alba_

_Abril, 2023_

_**Figura N° 23**_
_**Promedio del Período de SO**_ _**2**_ _**Fase Construcción año 2**_

Fuente: Algoritmos SpA, 2023

_**Inventario y Modelación de Emisiones ATM037-23**_ _87/106_
_Proyecto Alba_

_Abril, 2023_

_**Figura N° 24**_
_**Percentil 99 Máximo Horario de NO**_ _**2**_ _**Fase Construcción año 2**_

Fuente: Algoritmos SpA, 2023

_**Inventario y Modelación de Emisiones ATM037-23**_ _88/106_
_Proyecto Alba_

_Abril, 2023_

_**Figura N° 25**_
_**Promedio del Período de NO**_ _**2**_ _**Fase Construcción año 2**_

Fuente: Algoritmos SpA, 2023

_**Inventario y Modelación de Emisiones ATM037-23**_ _89/106_
_Proyecto Alba_

_Abril, 2023_

_**Figura N° 26**_
_**Percentil 99 Máximo Horario de CO Fase Construcción año 2**_

Fuente: Algoritmos SpA, 2023

_**Inventario y Modelación de Emisiones ATM037-23**_ _90/106_
_Proyecto Alba_

_Abril, 2023_

_**Figura N° 27**_
_**Percentil 99 Máximo 8 Horas de CO Fase Construcción año 2**_

Fuente: Algoritmos SpA, 2023

_**Inventario y Modelación de Emisiones ATM037-23**_ _91/106_
_Proyecto Alba_

_Abril, 2023_

_**Figura N° 28**_
_**Percentil 98 Promedio Diario de MP**_ _**10**_ _**Fase Operación Con Proyecto**_

Fuente: Algoritmos SpA, 2023

_**Inventario y Modelación de Emisiones ATM037-23**_ _92/106_
_Proyecto Alba_

_Abril, 2023_

_**Figura N° 29**_
_**Promedio del Período de MP**_ _**10**_ _**Fase Operación con Proyecto.**_

Fuente: Algoritmos SpA, 2023

_**Inventario y Modelación de Emisiones ATM037-23**_ _93/106_
_Proyecto Alba_

_Abril, 2023_

_**Figura N° 30**_
_**Percentil 98 Promedio Diario de MP**_ _**2,5**_ _**Fase Operación con Proyecto**_

Fuente: Algoritmos SpA, 2023

_**Inventario y Modelación de Emisiones ATM037-23**_ _94/106_
_Proyecto Alba_

_Abril, 2023_

_**Figura N° 31**_
_**Promedio del Período de MP**_ _**2,5**_ _**Fase Operación con Proyecto.**_

Fuente: Algoritmos SpA, 2023

_**Inventario y Modelación de Emisiones ATM037-23**_ _95/106_
_Proyecto Alba_

_Abril, 2023_

_**Figura N° 32**_
_**Percentil 99 Promedio Diario de SO**_ _**2**_ _**Fase Operación con Proyecto.**_

Fuente: Algoritmos SpA, 2023

_**Inventario y Modelación de Emisiones ATM037-23**_ _96/106_
_Proyecto Alba_

_Abril, 2023_

_**Figura N° 33**_
_**Percentil 98,5 Promedio Horario de SO**_ _**2**_ _**Fase Operación con Proyecto.**_

Fuente: Algoritmos SpA, 2023

_**Inventario y Modelación de Emisiones ATM037-23**_ _97/106_
_Proyecto Alba_

_Abril, 2023_

_**Figura N° 34**_
_**Percentil 99,7 Promedio Diario de SO**_ _**2**_ _**Fase Operación con Proyecto.**_

Fuente: Algoritmos SpA, 2023

_**Inventario y Modelación de Emisiones ATM037-23**_ _98/106_
_Proyecto Alba_

_Abril, 2023_

_**Figura N° 35**_
_**Percentil 99,73 Promedio Horario de SO**_ _**2**_ _**Fase Operación con Proyecto.**_

Fuente: Algoritmos SpA, 2023

_**Inventario y Modelación de Emisiones ATM037-23**_ _99/106_
_Proyecto Alba_

_Abril, 2023_

_**Figura N° 36**_
_**Promedio del Período de SO**_ _**2**_ _**Fase Operación con Proyecto.**_

Fuente: Algoritmos SpA, 2023

_**Inventario y Modelación de Emisiones ATM037-23**_ _100/106_
_Proyecto Alba_

_Abril, 2023_

_**Figura N° 37**_
_**Percentil 99 Máximo Horario de NO**_ _**2**_ _**Fase Operación con Proyecto.**_

Fuente: Algoritmos SpA, 2023

_**Inventario y Modelación de Emisiones ATM037-23**_ _101/106_
_Proyecto Alba_

_Abril, 2023_

_**Figura N° 38**_
_**Promedio del Período de NO**_ _**2**_ _**Fase Operación con Proyecto.**_

Fuente: Algoritmos SpA, 2023

_**Inventario y Modelación de Emisiones ATM037-23**_ _102/106_
_Proyecto Alba_

_Abril, 2023_

_**Figura N° 39**_
_**Percentil 99 Máximo Horario de CO Fase Operación con Proyecto.**_

Fuente: Algoritmos SpA, 2023

_**Inventario y Modelación de Emisiones ATM037-23**_ _103/106_
_Proyecto Alba_

_Abril, 2023_

_**Figura N° 40**_
_**Percentil 99 Máximo 8 Horas de CO Fase Operación con Proyecto.**_

Fuente: Algoritmos SpA, 2023

_**Inventario y Modelación de Emisiones ATM037-23**_ _104/106_
_Proyecto Alba_

_Abril, 2023_

**13** **Conclusiones**

De los resultados obtenidos en los cálculos de emisiones y la modelación de estas
emisiones para el Proyecto Alba, se desprende lo siguiente:

 Se realizó un inventario de emisiones de las principales actividades emisoras
existentes en la fase de construcción, operación actual, operación con
proyecto Alba (Alba, Adelaida y Aerogeneradores). Para el inventario se
consideraron los contaminantes: dióxido de azufre (SO 2 ), óxidos de
nitrógeno (NO X ), material particulado fino, grueso (MP 2.5 y MP 10 ), monóxido
de carbono (CO) y compuestos orgánicos volátiles (COVs).

 Las emisiones totales resultantes del inventario de emisiones para la fase
Construcción, Operación actual y Operación con proyecto corresponden a:

`o` Construcción año 1: 1,09 t de SO 2, 21,41 t de NO X, 6,18 t de CO, 3,47

t de MP 2.5, 11,02 t de MP 10 y 1,87 t de COVs.
`o` Construcción año 2: 0,55 t de SO 2, 54,59 t de NO X, 3,57 t de CO, 1,82

t de MP 2.5, 5,38 t de MP 10 y 0,97 t de COVs.
`o` Operación actual: 5.047,49 t de SO 2, 4.249,48 t de NO X, 0,57 t de

CO, 433,84 t de MP 2.5, 439,77 t de MP 10 y 0,12 t de COVs.

`o` Operación con Proyecto: 1.928,88 t de SO 2, 1.703,61 t de NO X, 0,28

t de CO, 153,71 t de MP 2.5, 160,67 t de MP 10 y 0,06 t de COVs.

`o` Cierre: 0,0024 t de SO 2, 0,66 t de NO X, 0,16 t de CO, 0,37 t de MP 2.5,

1,07 t de MP 10 y 0,03 t de COVs.

 Las tasas de emisiones de Adelaida y el proyecto de Aerogeneradores, son
significativamente bajas, por lo que no tienen una mayor incidencia en el
proyecto Alba.

 Con respecto a la fase de Construcción año 1 y año 2, el mayor aporte para
las partículas y los gases corresponde al movimiento de tierra y fundición de
sal, respectivamente. Asimismo, para las fases de Operación el mayor aporte
corresponde al flujo vehicular. En la fase de Cierre los mayores aportes para
las partículas corresponden al tránsito de caminos pavimentados y para los
gases proviene del motor de vehículos de caminos pavimentados.

 Sobre los aportes obtenidos en la modelación de la dispersión de
contaminantes del proyecto, en la fase de construcción año 2 podemos
indicar que las concentraciones obtenidas para la mayoría de los
contaminantes son menores a un 1 ug/m [3] . Los valores que más se destacan
para la construcción año 2 son los del contaminante NO 2 en su estadístico
percentil 99 horario, estas concentraciones se deben a la formación de NO X
debido a la descomposición de la sal, no obstante, estas concentraciones son
transitorias, por lo que no representan latencia o saturación. Para la fase de
operación con proyecto, también se destaca el mismo contaminante y
estadístico, lo cual se debe principalmente a la chimenea presente. En ambas
modelaciones se tiene que los aportes no superan la normativa establecida.

_**Inventario y Modelación de Emisiones ATM037-23**_ _105/106_
_Proyecto Alba_

_Abril, 2023_

 Respecto a los aportes de Adelaida y los Aerogeneradores, los aportes son
todos menores a 1 ug/m [3], para todos los contaminantes normados, por lo
tanto, no son un aporte significativo dentro del proyecto Alba.

 Las isoconcentraciones obtenidas para el escenario de construcción del
proyecto año 2 y operación con proyecto (Alba, Adelaida y Aerogeneradores)
muestran que los contaminantes tienen una dispersión local, ubicándose
preferentemente en los entornos del proyecto.

_**Inventario y Modelación de Emisiones ATM037-23**_ _106/106_
_Proyecto Alba_

_Abril, 2023_