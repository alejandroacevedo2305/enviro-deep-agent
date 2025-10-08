---
title: iembre 30 de 2011
author: Valeria P. Campos Bravo
date: D:20230601153136-04'00'
language: es
type: report
pages: 121
has_toc: False
has_tables: True
extraction_quality: high
---

**MODELACIÓN DE EMISIONES ATMOSFÉRICAS PLANTA**

**JUCOSOL**

_Preparado por:_

_Para:_

Mayo, 2023

INFORME DE RESULTADOS

ATM064-22

**MODELACIÓN DE EMISIONES ATMOSFÉRICAS PLANTA**

**JUCOSOL**

_Preparado para:_

|Versión del Documento|Col2|Col3|Col4|1|Col6|
|---|---|---|---|---|---|
|**_Responsable Elaboración_**|**_Responsable Elaboración_**|**_Responsable Revisión_**|**_Responsable Revisión_**|**_Responsable Aprobación_**|**_Responsable Aprobación_**|
|Nombre:|Stephanie Oviedo|Nombre:|Stephanie Oviedo|Nombre:|Stephanie Oviedo|
|Cargo:|Jefe proyecto|Cargo|Jefe proyecto|Cargo:|Jefe proyecto|
|Fecha:|30-05-2023|Fecha:|30-05-2023|Fecha:|30-05-2023|
|Firma:||Firma:||Firma:||

Mayo, 2023

**ÍNDICE DE CONTENIDOS**

1 Introducción ................................................................................................ 1

1.1 Alcances 2
2 Marco Legal ................................................................................................ 4
3 Situación Actual de Calidad del Aire ............................................................... 6
4 Meteorología de la Zona de Estudio ................................................................ 7
4.1 Series de Tiempo ......................................................................................... 8
4.1.1 Estación Escuela Agrícola .............................................................................. 9
4.2 Rosas de Viento ......................................................................................... 10

4.3 Ciclo estacional.......................................................................................... 13

4.4 Ciclo Diario Velocidad del Viento .................................................................. 14
4.4.1 Estación Los Andes .................................................................................... 16

4.5 Rosas de Viento ......................................................................................... 17

4.6 Ciclo Estacional ......................................................................................... 20

4.7 Ciclo Diario Velocidad del Viento .................................................................. 21
5 Análisis de Incertidumbre ........................................................................... 23
5.1 Estación Escuela Agrícola ............................................................................ 23
5.2 Estación Los Andes .................................................................................... 23
5.3 Descripción de Parámetros Estadísticos ........................................................ 24
5.3.1 Media ................................................................................................ 24

5.3.2 Moda ................................................................................................ 24

5.3.3 Mediana ................................................................................................ 24
5.3.4 Desviación Estándar ................................................................................... 24
5.3.5 Raíz del Error Cuadrático Medio ................................................................... 25
5.3.6 Error Medio Cuadrático ............................................................................... 25
5.3.7 Sesgo ................................................................................................ 25
5.3.8 Coeficiente de correlación ........................................................................... 26
5.4 Análisis cuantitativo ................................................................................... 27
6 Estimación de Emisiones del Proyecto .......................................................... 28
6.1 Actividades Emisoras .................................................................................. 28
6.2 Tasas de Emisión Escenario con Proyecto ...................................................... 29
7 Modelación de Dispersión de Contaminantes ................................................. 31
7.1 Modelo de Dispersión Atmosférica ................................................................ 31
7.1.1 Base Teórica ............................................................................................. 31
7.1.2 Sistema de Modelación WRF - CALPUFF ........................................................ 31
7.2 Variables de Entrada ingresados al Sistema de Modelación .............................. 33
8 Resultados Modelación ............................................................................... 38
8.1 Campos de Viento ...................................................................................... 38
8.2 Aportes Obtenidos de la Modelación ............................................................. 43
8.2.1 Aporte en Puntos de Interés ........................................................................ 43
8.2.2 Ajustes de Resultados de la Modelación por Incertidumbre .............................. 50
8.3 Aportes en Puntos de Máxima Concentración ................................................. 57
8.4 Comparación Estaciones de Monitoreo con Línea de Base ................................ 63
8.5 Mapas de Isoconcentraciones ...................................................................... 70
9 Área de Influencia .................................................................................... 113

10 Conclusiones ........................................................................................... 115

_**Modelación de Emisiones ATM064-22**_
_Proyecto Planta Jucosol_

_Mayo, 2023_

**ÍNDICE DE TABLAS**

Tabla N°1 Coordenadas de los Vértices del Área de Modelación ..................................... 1

Tabla N°2 Normas de Calidad del Aire Consideradas en el Estudio ................................. 4
Tabla N°3 Coordenadas de la Estación de Monitoreo .................................................... 6
Tabla N°4 Línea de Base de calidad del aire para Norma Primaria de Material Particulado
MP10 y MP2,5 .................................................................................................. 6
Tabla N°5 Localización de Referencia y Variables Meteorológicas Monitoreadas................ 8
Tabla N°6 Estadísticas de Datos Meteorológicos Monitoreados ....................................... 8
Tabla N° 7 Velocidad promedio del Viento en m/s ...................................................... 23
Tabla N° 8 Velocidad Promedio del Viento en m/s ...................................................... 23
Tabla N°9 Valores de los indicadores estadísticos observados y modelados ................... 27
Tabla N°10 Estadígrafos de evaluación de desempeño del modelo Velocidad del Viento .. 27
Tabla N°10 Principales actividades emisoras fase construcción y operación ................... 28
Tabla N°11 Tasas de Emisión Fase Construcción y Operación ...................................... 30
Tabla N° 13 Características del Uso de Suelo ............................................................ 33
Tabla N° 14 Localización Puntos Discretos ................................................................ 35
Tabla N° 15 Aporte Planta Jucosol en Punto de interés, Fase Construcción .................... 44
Tabla N° 16 Aporte Planta Jucosol en Punto de interés, Fase Operación ........................ 46
Tabla N° 17 Aporte Planta Jucosol en Punto de interés, Fase Cierre ............................. 48
Tabla N° 18 Aporte Planta Jucosol Punto de interés con Incertidumbre del 56%, Fase de
Construcción ................................................................................................ 51
Tabla N° 19 Aporte Planta Jucosol, Punto de interés con Incertidumbre del 56%, Fase
Operación ................................................................................................ 53
Tabla N° 20 Aporte Planta Jucosol Punto de interés con Incertidumbre del 56%en Punto de
interés, Fase Cierre ................................................................................................ 54
Tabla N° 21 Localización Punto Máximo Impacto (PMI), Fase Construcción ................... 57
Tabla N° 22 Localización Punto Máximo Impacto (PMI), Fase Operación ....................... 58
Tabla N° 23 Localización Punto Máximo Impacto (PMI), Fase Cierre ............................. 59
Tabla N° 24 Relación entre la línea base (LB) y los datos modelados (DM) con ajuste de
incertidumbre, Fase Construcción ............................................................................ 63
Tabla N° 25 Relación entre la línea base (LB) y los datos modelados (DM) con ajuste de
incertidumbre, Fase Operación ................................................................................ 63
Tabla N° 26 Relación entre la línea base (LB) y los datos modelados (DM) con ajuste de
incertidumbre, Fase Cierre ...................................................................................... 63
Tabla N° 27 Porcentaje de aporte según normativa en puntos de interés, con incertidumbre
Fase de Construcción ............................................................................................. 64
Tabla N° 28 Porcentaje de aporte según normativa en puntos de interés, con incertidumbre
Fase de Operación ................................................................................................ 66
Tabla N° 29 Porcentaje de aporte según normativa en puntos de interés, con incertidumbre
Fase de Cierre 68

**ÍNDICE DE FIGURAS**

Figura N° 1 Ubicación del Proyecto y Dominio de Modelación ........................................ 1
Figura N° 2 Serie temporal horaria velocidad del viento - Estación Escuela Agrícola Periodo
enero a diciembre 2021 ............................................................................................ 9
Figura N° 3 Frecuencia de ocurrencia dirección del viento - Estación Escuela Agrícola Periodo
enero a diciembre 2021 .......................................................................................... 10
Figura N° 4 Rosa de Viento Ciclo Completo Estación Escuela Agrícola Periodo enero a
diciembre 2021 ................................................................................................ 11

_**Modelación de Emisiones ATM064-22**_
_Proyecto Planta Jucosol_

_Mayo, 2023_

Figura N° 5 Variabilidad temporal del viento - Estación Escuela Agrícola Periodo enero a
diciembre 2021 ................................................................................................ 12
Figura N° 6 Variabilidad estacional del viento - Estación Escuela Agrícola Periodo 01 enero
2021 - 31 diciembre 2021 ...................................................................................... 13
Figura N° 7 Ciclos Diarios de Velocidad (m/s) y Dirección del Viento (°) Estación Escuela
Agrícola (Observado v/s Modelado) Periodo enero a diciembre 2021 ............................ 15
Figura N° 8 Serie temporal horaria velocidad del viento - Estación Los Andes Periodo enero
a diciembre 2021 ................................................................................................ 16
Figura N° 9 Frecuencia de ocurrencia dirección del viento - Estación Los Andes Periodo enero
a diciembre 2021 ................................................................................................ 17
Figura N° 10 Rosa de Viento Ciclo Completo Estación Los Andes Periodo enero a diciembre
2021 ................................................................................................ 18
Figura N° 11 Variabilidad temporal del viento - Estación Los Andes Periodo enero a diciembre
2021 ................................................................................................ 19
Figura N° 12 Variabilidad estacional del viento - Estación Los Andes Periodo 01 enero 2021
- 31 diciembre 2021 .............................................................................................. 20
Figura N° 13 Ciclos Diarios de Velocidad (m/s) y Dirección del Viento (°) Estación Los Andes
(Observado v/s Modelado) Periodo enero a diciembre 2021 ........................................ 22
Figura N° 14 Uso de Suelo ...................................................................................... 34
Figura N° 15 Ubicación Puntos Discretos ................................................................... 37
Figura N° 11 Campos de Viento a las 00:00 horas. .................................................... 39
Figura N° 12 Campos de Viento a las 06:00 horas ..................................................... 40
Figura N° 13 Campos de Viento a las 12:00 horas ..................................................... 41
Figura N° 14 Campos de Viento a las 18:00 horas. .................................................... 42
Figura N° 20 Ubicación de Puntos de Máximo Impacto, Fase Construcción .................... 60
Figura N° 21 Ubicación de Puntos de Máximo Impacto, Fase Operación ........................ 61
Figura N° 22 Ubicación de Puntos de Máximo Impacto, Fase Cierre .............................. 62
Figura N° 23 Percentil 98 Promedio Diario de MP10, Fase Construcción ........................ 71
Figura N° 24 Promedio del Período de MP10, Fase Construcción .................................. 72
Figura N° 25 Percentil 98 Promedio Diario de MP2,5, Fase Construcción ....................... 73
Figura N° 26 Promedio del Período de MP2,5, Fase Construcción ................................. 74
Figura N° 27 Promedio del Período de MPS, Fase Construcción .................................... 75
Figura N° 28 Percentil 98,5 Promedio Horario de SO2, Fase Construcción ..................... 76
Figura N° 29 Percentil 99 Promedio Diario de SO2, Fase Construcción .......................... 77
Figura N° 30 Percentil 99,7 Promedio Diario de SO2, Fase Construcción ....................... 78
Figura N° 31 Percentil 99,73 Promedio Horario de SO2, Fase Construcción ................... 79
Figura N° 32 Promedio del Período de SO2, Fase Construcción .................................... 80
Figura N° 33 Percentil 99 Máximo Horario de NO2, Fase Construcción .......................... 81
Figura N° 34 Promedio del Período de NO2, Fase Construcción .................................... 82
Figura N° 35 Percentil 99 Máximo Horario de CO, Fase Construcción ............................ 83
Figura N° 36 Percentil 99 Máximo 8 Horas de CO, Fase Construcción ........................... 84
Figura N° 37 Percentil 98 Promedio Diario de MP10, Fase Operación ............................ 85
Figura N° 38 Promedio del Período de MP10, Fase Operación ...................................... 86
Figura N° 39 Percentil 98 Promedio Diario de MP2,5, Fase Operación ........................... 87
Figura N° 40 Promedio del Período de MP2,5, Fase Operación ..................................... 88
Figura N° 41 Promedio del Período de MPS, Fase Operación ........................................ 89
Figura N° 42 Percentil 98,5 Promedio Horario de SO2, Fase Operación ......................... 90
Figura N° 43 Percentil 99 Promedio Diario de SO2, Fase Operación .............................. 91
Figura N° 44 Percentil 99,7 Promedio Diario de SO2, Fase Operación ........................... 92
Figura N° 45 Percentil 99,73 Promedio Horario de SO2, Fase Operación ....................... 93
Figura N° 46 Promedio del Período de SO2, Fase Operación ........................................ 94
Figura N° 47 Percentil 99 Máximo Horario de NO2, Fase Operación .............................. 95

_**Modelación de Emisiones ATM064-22**_
_Proyecto Planta Jucosol_

_Mayo, 2023_

Figura N° 48 Promedio del Período de NO2, Fase Operación ........................................ 96
Figura N° 49 Percentil 99 Máximo Horario de CO, Fase Operación ................................ 97
Figura N° 50 Percentil 99 Máximo 8 Horas de CO, Fase Operación ............................... 98
Figura N° 51 Percentil 98 Promedio Diario de MP10, Fase Cierre .................................. 99
Figura N° 52 Promedio del Período de MP10, Fase Cierre .......................................... 100
Figura N° 53 Percentil 98 Promedio Diario de MP2,5, Fase Cierre ............................... 101
Figura N° 54 Promedio del Período de MP2,5, Fase Cierre ......................................... 102
Figura N° 55 Promedio del Período de MPS, Fase Cierre ............................................ 103
Figura N° 56 Percentil 98,5 Promedio Horario de SO2, Fase Cierre ............................. 104
Figura N° 57 Percentil 99 Promedio Diario de SO2, Fase Cierre ................................. 105
Figura N° 58 Percentil 99,7 Promedio Diario de SO2, Fase Cierre ............................... 106
Figura N° 59 Percentil 99,73 Promedio Horario de SO2, Fase Cierre ........................... 107
Figura N° 60 Promedio del Período de SO2, Fase Cierre ............................................ 108
Figura N° 61 Percentil 99 Máximo Horario de NO2, Fase Cierre.................................. 109
Figura N° 62 Promedio del Período de NO2, Fase Cierre............................................ 110
Figura N° 63 Percentil 99 Máximo Horario de CO, Fase Cierre ................................... 111
Figura N° 64 Percentil 99 Máximo 8 Horas de CO, Fase Cierre ................................... 112
Figura N° 51 Área de Influencia ............................................................................. 113

_**Modelación de Emisiones ATM064-22**_
_Proyecto Planta Jucosol_

_Mayo, 2023_

**1** **Introducción**

La empresa Jucosol ubicada en San Felipe en la Región de Valparaíso, se dedica a
la producción de jugo concentrado de uva desde 1975, también conocido como
mosto. La mayor parte de su producción es exportada hacia Norte América, Europa
y Asia. La empresa presenta un gran compromiso con el medio ambiente, lo que la
ha llevado a implementar ERNC y alternativas de reutilización de agua.

A solicitud de DAES, Algoritmos y Mediciones Ambientales SpA, realizó el Servicio
de modelación de emisiones atmosférica para proyecto Planta Jucosol. La
modelación de emisiones se realizó a través del sistema WRF-CALPUFF.

El presente informe muestra las emisiones totales extraídas del inventario de
emisiones entregado por el cliente y las concentraciones obtenidas al modelar la
dispersión atmosférica de material particulado sedimentable (MPS), material
particulado respirable (MP 10 y MP 2,5 ), dióxido de azufre (SO 2 ), dióxido de nitrógeno
(NO x ) y monóxido de carbono (CO) correspondiente a la fase de construcción y
operación y cierre del proyecto Planta Jucosol. Además, se informa los resultados
de la modelación meteorológica realizada con el modelo WRF y su validación, al
comparar los resultados meteorológicos modelados con los observados por dos
estaciones de monitoreo en la zona de estudio. El área de modelación corresponde
a una grilla de 12 km x 13 km, un espaciamiento de 1 km y en cuyo interior se
encuentra ubicado el sitio de emplazamiento de la planta y los puntos de interés.
La siguiente tabla muestra las coordenadas de los vértices del área de modelación.

_**Tabla N°1**_
_**Coordenadas de los Vértices del Área de Modelación**_ _**[a]**_

|Vértice|Coordenadas UTMa|Col3|
|---|---|---|
|**Vértice**|**Este (m)**|**Norte (m)**|
|Noreste|352.440|6.376.880|
|Noroeste|340.418|6.376.696|
|Sureste|352.641|6.363.916|
|Suroeste|340.617|6.363.728|

Fuente: Algoritmos SpA, 2023.

Los aportes de concentraciones de material particulado y de gases asociados al
Proyecto fueron obtenidos según los requerimientos de la “Guía para el Uso de
Modelos de Calidad del Aire en el SEIA, 2012” del Servicio de Evaluación Ambiental.
Esta Guía indica como opción la aplicación del sistema de modelación atmosférica
“WRF - CALPUFF”, sistema de modelación que a su vez está definido por la agencia
EPA como sistema de referencia para simular la dispersión de contaminantes
provenientes de centros industriales ubicados en terreno complejo.

a Coordenadas tomadas según Datum WGS-84

_**Modelación de Emisiones ATM064-22**_ _1/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

La meteorología utilizada en el sistema de modelación se obtuvo por medio del
modelo meteorológico de pronóstico Weather Research and Forecasting Model
(WRF), con todos los parámetros indicados en la “Guía para el Uso de Modelos de
Calidad del Aire en el SEIA, 2012”. Dicha información es referente al entorno del
proyecto y corresponde al periodo comprendido entre el 1 de enero hasta el 31 de
diciembre del 2021.

En la Figura N° 1, se presenta el mapa con la ubicación del proyecto y el área de
modelación.

**1.1** **Alcances**

 Realizar el modelo meteorológico WRF y validarlo mediante la comparación
con datos monitoreados.

 - Obtener aportes en concentración e isoconcentraciones de los
contaminantes normados SO 2, NO x, CO, MPS, MP 10 y MP 2,5 con el sistema de
modelación WRF-CALPUFF, en cada punto de interés ingresado al modelo,
para el escenario Construcción, Operación y Cierre

_**Modelación de Emisiones ATM064-22**_ _2/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 1**_
_**Ubicación del Proyecto y Dominio de Modelación**_

Fuente: Algoritmos SpA, 2023.

_**Modelación de Emisiones ATM064-22**_ _3/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

**2** **Marco Legal**

Para determinar el aporte del proyecto respecto de la normativa ambiental se
consideraron las normas primarias y secundarias de calidad del aire definidas en la
legislación chilena.

Para el caso del MPS, de acuerdo a los criterios establecidos por la Dirección
Regional del SEA, es posible utilizar las normas de referencia de los Estados que
se establecen en el Artículo 11° Normas de referencia, del Decreto Supremo N°
40/2012 del Reglamento del SEIA, que indica: “Las normas de calidad ambiental y
de emisión que se utilizarán como referencia para los efectos de evaluar si se
genera o presenta el riesgo indicado en la letra a) y los efectos adversos señalados
en la letra b), ambas del artículo 11 de la Ley, serán aquellas vigentes en los
siguientes Estados: República Federal de Alemania, República Argentina, Australia,
República Federativa del Brasil, Canadá, Reino de España, Estados Unidos
Mexicanos, Estados Unidos de América, Nueva Zelandia, Reino de los Países Bajos,
República Italiana, Japón, Reino de Suecia y Confederación Suiza.

Debido a lo anterior, considera como referencia lo señalado por la norma suiza
“Ordenanza sobre la concentración de la pureza del aire (OAPC) de 1985, revisada
el 2009, que establece en el artículo 2 párrafo 5 que el límite como concentración
anual de Material Particulado Sedimentable es de 200 mg/m [2] día.

La Tabla N°2 presenta los valores límites de referencia para el análisis del presente
documento.

_**Tabla N°2**_

_**Normas de Calidad del Aire Consideradas en el Estudio**_

|Parámetro|Tipo de<br>Norma|Estadístico|Valor|Referencia|
|---|---|---|---|---|
|MPS|Secundaria|Promedio del<br>periodo|200 mg/m2-día|Norma Suizaa|
|MP10|Primaria|Promedio del<br>periodo|50g/m3N|D.S. N°45/02<br>MINSEGPRES|
|MP10|Primaria|Percentil 98<br>Diario|130g/m3N|D.S. N°12/21 MMA|
|MP2,5|Primaria|Promedio del<br>periodo|20g/m3N|D.S. N°12/11 MMA|
|MP2,5|Primaria|Percentil 98<br>Diario|50g/m3N|D.S. N°12/11 MMA|
|SO2|Primaria|Promedio del<br>periodo|60g/m3N|D.S. N°104/18 MMA|
|SO2|Primaria|Percentil 99<br>Diario|150g/m3N|D.S. N°104/18 MMA|

_**Modelación de Emisiones ATM064-22**_ _4/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

|Parámetro|Tipo de<br>Norma|Estadístico|Valor|Referencia|
|---|---|---|---|---|
|||Percentil 98,5<br>Horario|350g/m3N|D.S. N°104/18 MMA|
|SO2|Secundaria|Promedio del<br>periodo|80g/m3N|D.S. N°22/10<br>MINSEGPRES|
|SO2|Secundaria|Percentil 99,7<br>Diario|365g/m3N|D.S. N°22/10<br>MINSEGPRES|
|SO2|Secundaria|Percentil<br>99,73 Horario|1.000g/m3N|D.S. N°22/10<br>MINSEGPRES|
|NO2|Primaria|Promedio del<br>periodo|100g/m3N|D.S. N°114/02<br>MINSEGPRES|
|NO2|Primaria|Percentil 99<br>Horario|400g/m3N|D.S. N°114/02<br>MINSEGPRES|
|CO|Primaria|Percentil 99 8<br>horas|10.000g/m3N|D.S. N°115/02<br>MINSEGPRES|
|CO|Primaria|Percentil 99<br>Horario|30.000g/m3N|D.S. N°115/02<br>MINSEGPRES|

Fuente: Biblioteca del Congreso Nacional de Chile.
a Ordenanza sobre la concentración de la pureza del aire, Consejo Federal Suizo, año 1985.

_**Modelación de Emisiones ATM064-22**_ _5/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

**3** **Situación Actual de Calidad del Aire**

Para caracterizar la línea de base de calidad del aire en el área del Proyecto se
consideran las mediciones de NO 2 para la siguiente estación:

_**Tabla N°3**_
_**Coordenadas de la Estación de Monitoreo**_

|Estación|Coordenadas UTMa|Col3|Contaminante|Periodo evaluación|
|---|---|---|---|---|
|**Estación**|**Este (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|
|Los Andes|351.534|6.364.623|NO2|Enero a diciembre del 2021|

Fuente: Algoritmos SpA, 2023.

A continuación, se presentan los valores obtenidos al aplicar la normativa vigente.

_**Tabla N°4**_
_**Línea de Base de calidad del aire para Norma Primaria de**_

_**Material Particulado MP**_ _**10**_ _**y MP**_ _**2,5**_

|Estación|Parámetro|Estadístico|Valor<br>(g/m3N)|Norma|% Norma|
|---|---|---|---|---|---|
|Los Andes|NO2|Promedio del Periodo|23,78|100|24%|
|Los Andes|NO2|Percentil 99 Horario|104,06|400|26%|

Fuente: Algoritmos SpA, 2023.

_**Modelación de Emisiones ATM064-22**_ _6/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

**4** **Meteorología de la Zona de Estudio**

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
meteorológicas registradas por la estación Escuela Agrícola y Los Andes con el fin
de evaluar la capacidad predictiva del modelo.

La Tabla N°5 presenta las coordenadas de localización y las variables
meteorológicas monitoreadas en las estaciones antes mencionada.

_**Modelación de Emisiones ATM064-22**_ _7/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Tabla N°5**_
_**Localización de Referencia y Variables Meteorológicas Monitoreadas**_

|Estación|Coordenadas UTM|Col3|Variables|Periodo|
|---|---|---|---|---|
|**Estación**|**Este (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|
|Escuela<br>Agrícola|340.736|6.375.149|Velocidad del viento<br>Dirección del viento|01 de enero al 31 de<br>diciembre 2021|
|Los Andes|351.534|6.364.623|Velocidad del viento<br>Dirección del viento|01 de enero al 31 de<br>diciembre 2021|

Fuente: Algoritmos, SpA 2023.

En las siguientes secciones se realiza un análisis comparativo entre la data
meteorológica registrada por las estaciones de monitoreo y lo simulado con WRF
para el periodo de registro (ver Tabla N°5), con resolución horaria para las
variables meteorológicas de velocidad y dirección de viento, ya que estos
parámetros influyen directamente en el fenómeno de dispersión de contaminantes.

**4.1** **Series de Tiempo**

La Tabla N°6 muestra los porcentajes de datos válidos y de calmas monitoreados
por las Estaciones. Respecto a la velocidad del viento se consideró como calma los
registros menores a 0,5 (m/s).

_**Tabla N°6**_
_**Estadísticas de Datos Meteorológicos Monitoreados**_

|Estación|Datos<br>Totales|Porcentaje de Calma (%)|Col4|Porcentaje Datos<br>Válidos (%)|
|---|---|---|---|---|
|**Estación**|**Datos**<br>**Totales**|**Periodo**<br>**Diurno**|**Periodo**<br>**Nocturno**|**Periodo**<br>**Nocturno**|
|Escuela<br>Agrícola|8.388|23%|38%|96%|
|Los Andes|8.704|11%|38%|100%|

Fuente: Algoritmos SpA, 2023.

La serie temporal de la velocidad del viento registrada por la Estación Escuela
Agrícola y Estación Los Andes, permiten un análisis cualitativo de los datos en
términos de variabilidad, amplitud de rango y frecuencia de los datos con que se
cuenta. No se presentan las series temporales generadas por el modelo WRF, ya
que la información de pronóstico dispone de la totalidad de los datos.

_**Modelación de Emisiones ATM064-22**_ _8/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

**4.1.1** **Estación Escuela Agrícola**

_**Figura N° 2**_
_**Serie temporal horaria velocidad del viento - Estación Escuela Agrícola**_

_**Periodo enero a diciembre 2021**_

Fuente: Algoritmos SpA, 2023.

La serie temporal de la velocidad del viento registrada por la estación Escuela
Agrícola muestra un comportamiento anual homogéneo, ya que no existen
diferencias aparentes entre invierno y verano. Las velocidades varían
principalmente alrededor de 2 m/s.

Con respecto a la dirección del viento, se identifican dos patrones dominantes. El
primero de ellos corresponde a vientos preferentemente desde el Norte (N) y Norte
Noreste (NNE) correspondiente a la línea centrada entre 300 y 360°. El segundo
corresponde a vientos desde el Este Noreste (ENE), correspondiente s la línea
centrada entre 120° y 180°.

_**Modelación de Emisiones ATM064-22**_ _9/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 3**_
_**Frecuencia de ocurrencia dirección del viento - Estación Escuela Agrícola**_

_**Periodo enero a diciembre 2021**_

Fuente: Algoritmos SpA, 2023.

**4.2** **Rosas de Viento**

A continuación, se muestran los campos de viento anual y para diferentes periodos
del día, los que muestran la variabilidad temporal del viento durante el periodo
desde enero a diciembre del 2021 para la Estación Escuela Agrícola y la modelación
generada con WRF para dicha estación.

_**Modelación de Emisiones ATM064-22**_ _10/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 4**_
_**Rosa de Viento Ciclo Completo Estación Escuela Agrícola**_

_**Periodo enero a diciembre 2021**_

|Observado|Modelado|
|---|---|
|||

Fuente: Algoritmos SpA, 2023.

La rosa de viento del lado izquierdo de la Figura N°4, corresponde a los registros
de la Estación Escuela Agrícola en la cual se puede observar que prevalecen con
mayor frecuencia vientos desde Norte (N) y Norte Noroeste (NNO) explicando en
conjunto un 36% de la frecuencia total. En menor medida se observan vientos
desde el Sureste (SE) y Sur Sureste (SSE), explicando el 16% de la frecuencia
total.

Con respecto a lo modelado con WRF (lado derecho de la Figura N°4), se obtiene
el mismo patrón de vientos observados, destacando una pequeña variación en
cuanto a la dirección, sin embargo, los vientos proceden del mismo cuadrante.

_**Modelación de Emisiones ATM064-22**_ _11/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 5**_
_**Variabilidad temporal del viento - Estación Escuela Agrícola**_

_**Periodo enero a diciembre 2021**_

|Col1|00:00 - 05:00 horas|06:00 - 11:00 horas|12:00 - 17:00 horas|18:00 - 23:00 horas|
|---|---|---|---|---|
|**_Observado_**|||||
|**_Modelado_**||<br>|||

Fuente: Algoritmos SpA, 2023.

_**Modelación de Emisiones ATM064-22**_ _12/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

Al observar el comportamiento espacial de los vientos en los diferentes periodos
del día para la Estación Escuela Agrícola (parte superior de la Figura N°5) se puede
apreciar que, principalmente entre las 00:00 y 12:00 horas los vientos proceden
con una mayor frecuencia desde Este Sureste (ESE), patrón que cambia entre las
12:00 y 23:00 donde los vientos más frecuentes provienen desde el Norte (N).

**4.3** **Ciclo estacional**

La Figura N°6 muestra la evolución estacional y diaria de la velocidad y dirección
del viento, presentando en el eje “x” las horas del día y en el eje “y” los meses del
año. Es posible observar un patrón similar a lo largo de todo el año, ya que no se
observan cambios significativos en la velocidad del viento, comportándose de
manera homogénea tanto en invierno como verano y durante la noche y el día.

En cuanto a la dirección del viento observado por la estación Escuela Agrícola, se
obtienen vientos desde el Este Noreste (ENE) principalmente entre las 00:00 y
08:00 horas a lo largo de todo el año, mientras que en las horas de la tarde
prevalecen vientos desde el Norte (N).

_**Figura N° 6**_
_**Variabilidad estacional del viento - Estación Escuela Agrícola**_

_**Periodo 01 enero 2021 - 31 diciembre 2021**_

|Observado|Modelado|
|---|---|
|||

Fuente: Algoritmos SpA, 2023.

_**Modelación de Emisiones ATM064-22**_ _13/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

**4.4** **Ciclo Diario Velocidad del Viento**

A continuación, se presentan los ciclos diarios promedio de la velocidad y dirección
del viento monitoreada por la Estación Escuela Agrícola y lo modelado con WRF
para dicha estación.

Al apreciar la curva de velocidad promedio para la Estación Escuela Agrícola (lado
izquierdo superior de la Figura N°7), esta presenta una condición homogénea a lo
largo del día, con una velocidad que varía entre 1 y 1,4 m/s, alcanzando el máximo
a las 15:00 horas, a diferencia de los datos modelados donde se observa un ciclo
diario un poco más marcado, alcanzando un máximo a las 16:00 horas con un valor
de 2,8 m/s.

Respecto de la dirección del viento (parte inferior izquierda de la Figura N°7) no se
observa un marcado ciclo diario, ya que se puede observar que la mayor frecuencia
de vientos se registra para la componente Norte (N).

_**Modelación de Emisiones ATM064-22**_ _14/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 7**_
_**Ciclos Diarios de Velocidad (m/s) y Dirección del Viento (°)**_

_**Estación Escuela Agrícola (Observado v/s Modelado)**_

_**Periodo enero a diciembre 2021**_

|Observado|Modelado|
|---|---|
|||

Fuente: Algoritmos SpA, 2023.

_**Modelación de Emisiones ATM064-22**_ _15/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

**4.4.1** **Estación Los Andes**

_**Figura N° 8**_
_**Serie temporal horaria velocidad del viento - Estación Los Andes**_

_**Periodo enero a diciembre 2021**_

Fuente: Algoritmos SpA, 2023.

La serie temporal de la velocidad del viento registrada por la estación Los Andes
muestra un leve ciclo anual, con las máximas velocidades registradas entre
septiembre y marzo, correspondiendo a los meses de primavera y verano, y las
mínimas velocidades entre abril y agosto, centradas en el periodo de otoño
invierno.

Con respecto a la dirección del viento, se identifican dos patrones dominantes. El
primero de ellos corresponde a vientos preferentemente desde el Norte Noreste
(NNE) correspondiente a la línea centrada entre 0 y 60°. El segundo corresponde
a vientos desde el Oeste Suroeste (OSO), correspondiente s la línea centrada en
240°.

_**Modelación de Emisiones ATM064-22**_ _16/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 9**_
_**Frecuencia de ocurrencia dirección del viento - Estación Los Andes**_

_**Periodo enero a diciembre 2021**_

Fuente: Algoritmos SpA, 2023.

**4.5** **Rosas de Viento**

A continuación, se muestran los campos de viento anual y para diferentes periodos
del día, los que muestran la variabilidad temporal del viento durante el periodo
desde enero a diciembre del 2021 para la Estación Los Andes y la modelación
generada con WRF para dicha estación.

_**Modelación de Emisiones ATM064-22**_ _17/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 10**_
_**Rosa de Viento Ciclo Completo Estación Los Andes**_

_**Periodo enero a diciembre 2021**_

|Observado|Modelado|
|---|---|
|||

Fuente: Algoritmos SpA, 2023.

La rosa de viento del lado izquierdo de la Figura N° 10, corresponde a los registros
de la Estación Los Andes en la cual se puede observar que prevalecen con mayor
frecuencia vientos desde Norte Noreste (NNE) y Noreste (NE) explicando en
conjunto un 59% de la frecuencia total. En menor medida se observan vientos
desde el Oeste Suroeste (OSO), explicando el 10% de la frecuencia total.

Con respecto a lo modelado con WRF (lado derecho de la Figura N° 10) se obtiene
el mismo patrón de vientos observados, sin embargo, se subestima la frecuencia
de ocurrencia de los vientos desde el Norte Noreste (NNE) y sobrestima los vientos
desde el Este Noreste (ENE), sin embargo, ambos provienen desde el mismo
cuadrante.

_**Modelación de Emisiones ATM064-22**_ _18/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 11**_
_**Variabilidad temporal del viento - Estación Los Andes**_

_**Periodo enero a diciembre 2021**_

|Col1|00:00 - 05:00 horas|06:00 - 11:00 horas|12:00 - 17:00 horas|18:00 - 23:00 horas|
|---|---|---|---|---|
|**_Observado_**|||||
|**_Modelado_**||<br>|||

Fuente: Algoritmos SpA, 2023.

_**Modelación de Emisiones ATM064-22**_ _19/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

Al observar el comportamiento espacial de los vientos en los diferentes periodos
del día para la Estación Los Andes (parte superior de la Figura N° 11) se puede
apreciar que, principalmente a lo largo del todo el día se registran vientos desde el
Norte Noreste (NNE), excepto en el periodo desde las 12:00 y 17:00 donde el
viento preferentemente proviene desde el Oeste Suroeste (OSO).

**4.6** **Ciclo Estacional**

La Figura N° 12 muestra la evolución estacional y diaria de la velocidad y dirección
del viento, presentando en el eje “x” las horas del día y en el eje “y” los meses del
año. Es posible observar un patrón diario representativo, correspondiendo a vientos
débiles en horas de la noche y madrugada, con valores que varían entre 0,5 y 1
m/s a lo largo de todo el año. Para el horario diurno, se observan los máximos
valores entre 14:00 y 17:00 horas, siendo levemente más intensas las velocidades
en primavera verano con valores que alcanzan los 3 m/s a diferencia del periodo
invernal donde las velocidades no sobrepasan los 2 m/s.

En cuanto a la dirección del viento observado por la estación Los Andes, se obtienen
vientos desde el Norte Noreste (NNE) principalmente entre las 00:00 y 08:00 horas
a lo largo de todo el año. Mientras que en las horas del prevalecen vientos desde
el Oeste Suroeste (OSO).

_**Figura N° 12**_
_**Variabilidad estacional del viento - Estación Los Andes**_

_**Periodo 01 enero 2021 - 31 diciembre 2021**_

|Observado|Modelado|
|---|---|
|||

Fuente: Algoritmos SpA, 2023.

_**Inventario y modelación de Olores ATM062-22**_ _20/114_
_Estudio Olores Biofiltro Jucosol_

_Mayo, 2023_

**4.7** **Ciclo Diario Velocidad del Viento**

A continuación, se presentan los ciclos diarios promedio de la velocidad y dirección
del viento monitoreada por la Estación Los Andes y lo modelado con WRF para
dicha estación.

Al apreciar la curva de velocidad promedio para la Estación Los Andes (lado
izquierdo superior de la Figura N° 13), esta presenta una condición homogénea a
lo largo de la madrugada, con unas velocidades menores a 1 m/s, aumentando a
partir de las 10:00 horas hasta alcanzar el máximo alrededor de las 16:00 horas
alcanzando un valor de 2,1 m/s. De los datos modelados se obtiene un ciclo similar,
con un máximo igual a 2,5 m/s.

Respecto de la dirección del viento (parte inferior izquierda de la Figura N° 13) se
observa un marcado ciclo diario con vientos desde el Norte Noreste (NNE) entre
las 00:00- 09:00 y 18:00 y 00:00 horas. Por otro lado, durante las horas de
máxima velocidad, el viento viene preferentemente desde el Oeste Suroeste
(OSO).

_**Inventario y modelación de Olores ATM062-22**_ _21/114_
_Estudio Olores Biofiltro Jucosol_

_Mayo, 2023_

_**Figura N° 13**_
_**Ciclos Diarios de Velocidad (m/s) y Dirección del Viento (°)**_

_**Estación Los Andes (Observado v/s Modelado)**_

_**Periodo enero a diciembre 2021**_

|Observado|Modelado|
|---|---|
|||

Fuente: Algoritmos SpA, 2023.

_**Modelación de Emisiones ATM064-22**_ _22/144_
_Proyecto Planta Jucosol_

_Mayo, 2023_

**5** **Análisis de Incertidumbre**

**5.1** **Estación Escuela Agrícola**

La Tabla N° 7 presenta las diferencias entre las observaciones y los pronósticos de
los valores promedios de velocidad de viento para el periodo diurno y nocturno
para la Estación Escuela Agrícola.

_**Tabla N° 7**_
_**Velocidad promedio del Viento en m/s**_

|Estación|Periodo|Promedio<br>Observación|Promedio<br>Pronóstico WRF|%<br>Sobrestimado<br>por pronóstico|
|---|---|---|---|---|
|Escuela<br>Agrícola|Diurno|1,07|1,89|43%|
|Escuela<br>Agrícola|Nocturno|0,76|1,75|56%|

Fuente: Algoritmos SpA, 2023.

Al comparar los ciclos diarios promedios observados y de pronóstico para la
Estación Escuela Agrícola, se evidencia que el modelo reproduce correctamente la
trayectoria del viento, presentando la mayor diferencia en el horario nocturno,
sobrestimando en 56% los valores modelados situación que genera condiciones
favorables con respecto a la ventilación en el área de interés, ya que la
meteorología generada por el modelo WRF al ser utilizada como dato de entrada
para el modelo de dispersión CALPUFF. Este último sobrestimaría el valor de la
concentración de los contaminantes.

**5.2** **Estación Los Andes**

La Tabla N° 8 presenta las diferencias entre las observaciones y los pronósticos de
los valores promedios de velocidad de viento para el periodo diurno y nocturno
para la Estación Los Andes.

_**Tabla N° 8**_
_**Velocidad Promedio del Viento en m/s**_

|Estación|Periodo|Promedio<br>Observación|Promedio<br>Pronóstico WRF|%<br>Sobrestimado<br>por pronóstico|
|---|---|---|---|---|
|Los Andes|Diurno|1,25|1,40|11%|
|Los Andes|Nocturno|0,95|1,52|38%|

Fuente: Algoritmos SpA, 2023.

_**Modelación de Emisiones ATM064-22**_ _23/144_
_Proyecto Planta Jucosol_

_Mayo, 2023_

Al comparar los ciclos diarios promedios observados y de pronóstico para la
Estación Los Andes, se evidencia que el modelo reproduce correctamente la
trayectoria del viento, presentando la mayor diferencia en el horario nocturno,
sobrestimando en 38% los valores modelados situación que genera condiciones
favorables con respecto a la ventilación en el área de interés, ya que la
meteorología generada por el modelo WRF al ser utilizada como dato de entrada
para el modelo de dispersión CALPUFF. Este último sobrestimaría el valor de la
concentración de los contaminantes.

**5.3** **Descripción de Parámetros Estadísticos**

**5.3.1** **Media**

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

**5.3.2** **Moda**

Corresponde al valor que cuenta con una mayor frecuencia en una distribución de
datos, es decir, el número más repetido.

**5.3.3** **Mediana**

La mediana es la medida más robusta, resistente y más común de la tendencia
central de la distribución de datos. A diferencia de la media no se ve afectada por
valores extremos que pudieran ser anómalos.

**5.3.4** **Desviación Estándar**

Corresponde a la raíz cuadrada de la diferencia media cuadrática entre el error de
pronóstico y el error de pronóstico promedio (E). Se utiliza para medir la cantidad
de variabilidad en el pronóstico de variables meteorológicas. Cuanto mayor sea el
valor de la SD, mayor será la variabilidad del pronóstico

_**Modelación de Emisiones ATM064-22**_ _24/144_
_Proyecto Planta Jucosol_

_Mayo, 2023_

Para realizar la validación de los datos registrados por la estación Camanchaca, se
calculan diferentes estadísticos clásicos tales como:

**5.3.5** **Raíz del Error Cuadrático Medio**

Corresponde al cálculo de la raíz cuadrada del promedio de las diferencias
cuadradas de cada uno de los valores del pronóstico y la observación. Este cálculo
permite ponderar los errores positivos y negativos, por lo cual en él están incluidos
los errores sistemáticos y aleatorios de los modelos.

Dónde:

X 1i : es el valor de la serie No 1

x 2i : es el valor de la serie No2

N: es el número de valores analizado

**5.3.6** **Error Medio Cuadrático**

El error medio cuadrático entrega las medidas de las diferencias en promedio entre
los valores modelados y los observados. Está definido como:

_N_ _abs_ ( _x_ 1 _i_ − _x_ 2 _i_
_MAE_ =

( _x_ 1 _i_ − _x_ 2 _i_ )

1 _i_ −

=
#### 

_N_

_i_

= 1

**5.3.7** **Sesgo**

Proporciona información sobre la tendencia del modelo a sobreestimar o
subestimar una variable, cuantificando el error sistemático del modelo.

_**Modelación de Emisiones ATM064-22**_ _25/144_
_Proyecto Planta Jucosol_

_Mayo, 2023_

**5.3.8** **Coeficiente de correlación**

Nos permite establecer la relación lineal entre los modelos utilizados y la
observación y está acotada entre -1 y 1.

Si Corr < 0 significa que las dos variables se correlacionan en sentido inverso. A
valores altos de una de ellas le suelen corresponder valores bajos de la otra y
viceversa. Si Corr > 0 las dos variables se correlacionan en sentido directo. A
valores altos de una le corresponden valores altos de la otra. Si corr = 0 se dice
que las variables están incorrelacionadas por lo tanto no puede establecerse ningún
sentido de covariación.

_**Modelación de Emisiones ATM064-22**_ _26/144_
_Proyecto Planta Jucosol_

_Mayo, 2023_

**5.4** **Análisis cuantitativo**

Tanto la velocidad como la dirección del viento son variables meteorológicas
relevantes para el análisis de los datos de entrada del modelo y al objeto de
observar la dirección de las masas de aire. Debido a lo anterior, a continuación, se
presenta en la Tabla N°8 los resultados obtenidos al aplicar los estadísticos a los
datos observados y modelados para la velocidad del viento en cada estación
evaluada.

_**Tabla N°9**_
_**Valores de los indicadores estadísticos observados y modelados**_

|Estadísticos|Unidad|Escuela Agrícola|Col4|Los Andes|Col6|
|---|---|---|---|---|---|
|**Estadísticos**|**Unidad**|**observado**|**modelado**|**observado**|**modelado**|
|Media|m/s|0,93|1,83|1,11|1,46|
|Máximo|m/s|4,06|8,77|6,36|10,32|
|Mínimo|m/s|0,02|0,02|0,00|0,01|
|Moda|m/s|1,11|1,19|0,15|1,05|
|Mediana|m/s|0,89|1,70|0,93|1,27|
|Desviación<br>estándar|--|0,58|1,10|0,85|0,86|

Fuente: Algoritmos SpA, 2023.

Para complementar el análisis cualitativo, se presenta en la Tabla N°9 un análisis
cuantitativo de las variables velocidad del viento que compara los valores
observados y modelados por medio de la utilización de tres estadígrafos
comúnmente utilizados para la evaluación del desempeño de modelos; Sesgo, Error
Cuadrático Medio y el coeficiente de correlación (r).

A continuación, se los estadígrafos de evaluación de desempeño del modelo WRF
respecto a los datos monitoreados por la estación Escuela Agrícola.

_**Tabla N°10**_
_**Estadígrafos de evaluación de desempeño del modelo**_

_**Velocidad del Viento**_

|Estación|Serie de datos|Medida de Error|Col4|Col5|
|---|---|---|---|---|
|**Estación**|**Serie de datos**|**Sesgo**|**RMSE**|**Corr**|
|Escuela<br>Agrícola|Serie de Tiempo|0,90|1,33|0,52|
|Escuela<br>Agrícola|Ciclo Diario|0,75|0,81|0,98|

_**Modelación de Emisiones ATM064-22**_ _27/144_
_Proyecto Planta Jucosol_

_Mayo, 2023_

|Estación|Serie de datos|Medida de Error|Col4|Col5|
|---|---|---|---|---|
|**Estación**|**Serie de datos**|**Sesgo**|**RMSE**|**Corr**|
|Los Andes|Serie de Tiempo|0,35|0,92|0,50|
|Los Andes|Ciclo Diario|0,35|0,48|0,77|

Fuente: Algoritmos SpA, 2023.

En base a lo anteriormente expuesto respecto de la meteorología, es posible
concluir que el modelo representa de manera satisfactoria la dinámica del viento
observado ya que este reproduce un ciclo anual de la velocidad junto a los patrones
en la dirección, sin embargo, este sobrestima los valores nocturnos. En relación
con los estadísticos evaluados, en la estación Escuela Agrícola se obtiene un bajo
sesgo, con un valor de error igual a 0,9 m/s para la serie temporal y 0,75 m/s para
el ciclo diario y al evaluar la correlación, obtenemos un valor superior a 0,52 tanto
en la serie temporal anual como en el ciclo diario. Para la estación Los Andes se
obtiene un bajo sesgo, con un valor de error igual a 0,35 m/s para el ciclo diario,
la correlación es superior a 0,57 tanto en la serie temporal anual como en el ciclo
diario.

**6** **Estimación de Emisiones del Proyecto**

**6.1** **Actividades Emisoras**

La Tabla N°11 presenta las principales actividades emisoras de material particulado
respirable (MP 10 ), material particulado respirable fino (MP 2,5 ), material particulado
sedimentable (MPS), dióxido de azufre (SO 2 ), óxidos de nitrógeno (NO X ) y
monóxido de carbono (CO), en la fase de construcción y operación.

_**Tabla N°11**_
_**Principales actividades emisoras fase construcción y operación**_

|Fase|Actividades|
|---|---|
|Construcción|• <br>Escarpe de superficie<br>• <br>Excavación<br>• <br>Traslado de personal<br>• <br>Traslado de insumos, equipamiento e infraestructura<br>• <br>Traslado de Residuos sólidos industriales<br>• <br>Traslado de residuos peligrosos<br>• <br>Traslado de aguas servidas (baños químicos)|
|Operación|• <br>Traslado de personal<br>• <br>Traslado de lodos<br>• <br>Traslado de insumos<br>• <br>Traslado de humus<br>• <br>Traslado de residuos no peligrosos|

_**Modelación de Emisiones ATM064-22**_ _28/144_
_Proyecto Planta Jucosol_

_Mayo, 2023_

Fuente: Algoritmos SpA, 2023

**6.2** **Tasas de Emisión Escenario con Proyecto**

A continuación, en la siguiente tabla se presenta el resumen de total de las
emisiones generadas durante la fase de construcción, operación y cierre.

_**Modelación de Emisiones ATM064-22**_ _29/144_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Tabla N°12**_
_**Tasas de Emisión Fase Construcción, Operación y cierre**_

|Fuente|SO<br>2|NO<br>X|CO|MP<br>2,5|MP<br>10|MPS|Unidad|
|---|---|---|---|---|---|---|---|
|Construcción|0,02|0,31|0,07|0,01|0,05|0,21|ton/año|
|Operación|<0,01|0,05|0,01|0,04|0,17|0,87|ton/año|
|Cierre|0,02|0,30|0,06|0,01|0,02|0,07|ton/año|

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _30/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

**7** **Modelación de Dispersión de Contaminantes**

Con el fin de evaluar la dispersión de los contaminantes generados por las fuentes,
como material particulado (MP 10 ), material particulado respirable fino (MP 2,5 ),
material particulado sedimentable (MPS), dióxido de azufre (SO 2 ), óxidos de
nitrógeno (NO X ) y monóxido de carbono (CO) para la fase de construcción y
operación del Proyecto, se realizó una modelación de dispersión de contaminantes
considerando las emisiones generadas en la fase de construcción y operación del
Proyecto.

**7.1** **Modelo de Dispersión Atmosférica**

**7.1.1** **Base Teórica**

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
simulación se hace para una pluma de emisión, continua o discreta, se trata de
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

**7.1.2** **Sistema de Modelación WRF - CALPUFF**

Para determinar el efecto que tendrán las emisiones de material particulado y gases
provenientes de la operación del Proyecto, se utiliza un sistema acoplado de dos
modelos: El modelo atmosférico Weather Research and Forecasting (WRF), y el
modelo CALPUFF, simulador de la dispersión de contaminantes en la atmósfera.
Ambos conforman el sistema de modelación WRF-CALPUFF.

_**Modelación de Emisiones ATM064-22**_ _31/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

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

_**Modelación de Emisiones ATM064-22**_ _32/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

procesa las salidas de CALPUFF creando archivos con las tabulaciones necesarias
que permitan la evaluación de resultados.

**7.2** **Variables de Entrada ingresados al Sistema de Modelación**

El sistema de modelación WRF-CALPUFF requiere de la siguiente información de
entrada:

 **Archivos NCEP-FNL (Final):** Información de entrada para el modelo WRF,
con una resolución espacial de 1 km x 1 km (url:
https://rda.ucar.edu/datasets/ds083.2/).

 - **Uso de Suelo** **[b]** **:** Esta información permite definir los coeficientes de
rugosidad superficial, razón de Bowen y albedo. Los usos de suelo presentes
en el área de estudio se encuentran en la siguiente tabla.

_**Tabla N° 13**_
_**Características del Uso de Suelo**_

|Uso de Suelo|Albedoc|Col3|Razón de Bowend|Col5|Rugosidad<br>Superficial (cm)|Col7|
|---|---|---|---|---|---|---|
|**Uso de Suelo**|**Verano**|**Invierno**|**Verano**|**Invierno**|**Verano**|**Invierno**|
|Bosque aguja de<br>hoja perenne|12|12|1|1|50|50|
|Bosque hoja<br>caduca|16|17|1|1|50|50|
|Bosque Mixto|13|14|0,5|0,5|50|50|
|Matorral|22|25|1|1|10|10|
|Mezcla de hierbas|20|24|1|1|11|10|
|Pradera|19|23|1|1|12|10|
|Pastos de cultivos<br>mixtos|18|23|1|1|15|5|
|Urbano|18|18|1,5|1,5|50|50|
|Mosaico de<br>bosques de<br>cultivo|16|20|1|1|20|20|

Fuente: Algoritmos SpA, 2023

La siguiente figura presenta los usos de suelo presentes en el área de estudio,
indicados en la tabla anterior.

b Información obtenida a partir de preprocesador CTGPROC
c Albedo: reflectividad a la luz solar del suelo (expresada como fracción respecto a la unidad)
d Razón de Bowen: definida como la razón entre flujos sensibles y latentes, a nivel de superficie.

_**Modelación de Emisiones ATM064-22**_ _33/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 14**_
_**Uso de Suelo**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _34/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

 - **Data de emisiones**, Corresponde al valor emitido por cada fuente
considerada en la fase de construcción, operación y cierre, con un ciclo de
producción para las tres fases que van desde las 08:00 hrs a las 20:00 hrs.
(Ver capítulo 6.2).

 **Ubicación de puntos de interés**, Esto permite la evaluación de los
resultados en comparación con la normativa aplicable. La ubicación de los
puntos de interés considerados se encuentra en la Tabla N° 14. En la Figura
N° 15, se muestra la ubicación de dicho punto.

_**Tabla N° 14**_
_**Localización Puntos Discretos**_ _**[e]**_

|Punto de Interés|Coordenadas UTM|Col3|
|---|---|---|
|**Punto de Interés**|**Este (m)**|**Norte (m)**|
|R1_OLOR|346.715|6.370.642|
|R2_OLOR|346.902|6.370.730|
|R3_OLOR|346.590|6.370.988|
|R4_OLOR|346.396|6.370.990|
|R5_OLOR|346.973|6.370.900|
|R6_OLOR|346.417|6.370.611|
|R1_RUIDO|346.732|6.370.654|
|R2_RUIDO|346.893|6.370.710|
|R3_RUIDO|346.487|6.371.049|
|R4_RUIDO|346.422|6.371.060|
|R5_RUIDO|346.411|6.370.613|
|R6_RUIDO|346.589|6.370.986|
|R7|346.074|6.370.311|
|R8|346.772|6.370.410|
|R9|347.331|6.370.546|
|R10|347.663|6.370.397|
|R11|348.087|6.370.295|
|R12|348.848|6.369.936|
|R13|349.481|6.369.578|
|R14|349.854|6.369.480|
|R15|350.396|6.369.264|
|R16|350.754|6.369.102|

e Datum WGS84, coordenadas UTM

_**Modelación de Emisiones ATM064-22**_ _35/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

|Punto de Interés|Coordenadas UTM|Col3|
|---|---|---|
|**Punto de Interés**|**Este (m)**|**Norte (m)**|
|R17|351.305|6.368.904|
|R18|351.645|6.368.815|
|R19|351.532|6.368.509|
|R20|351.161|6.367.879|
|R21|350.765|6.366.800|
|SINCA LOS ANDES|351.534|6.364.623|

Fuente: Algoritmos SpA, 2023

 - **Topografía del área de modelación:** Esta información es obtenida de
datos satelitales para la zona de estudio.

_**Modelación de Emisiones ATM064-22**_ _36/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 15**_
_**Ubicación Puntos Discretos**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _37/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

**8** **Resultados Modelación**

Se presentan los resultados obtenidos de la modelación atmosférica para este
estudio con el fin de evaluar el aporte de material particulado (MP 10 ), material
particulado respirable fino (MP 2,5 ), material particulado sedimentable (MPS),
dióxido de azufre (SO 2 ), óxidos de nitrógeno (NO X ) y monóxido de carbono (CO),
para el Proyecto Planta Jucosol, durante la fase de construcción y operación 2021.

**8.1** **Campos de Viento**

Mediante la aplicación del modelo WRF se simuló el comportamiento de los campos
de vientos sobre el área del Proyecto, para cada una de las horas consideradas en
la modelación. Dichos campos de vientos permitirán determinar posteriormente la
dispersión de los contaminantes, a través de la aplicación del modelo CALPUFF.

A modo de ejemplo se seleccionó el día 28 de julio del año 2021 para representar
el comportamiento de los vientos superficiales en horas representativas del día, en
la madrugada (06:00 hrs.), a medio día (12:00 hrs.), durante la tarde (18:00 hrs.)
y en la noche (00:00 hrs.).

_**Modelación de Emisiones ATM064-22**_ _38/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 16**_
_**Campos de Viento a las 00:00 horas.**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _39/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 17**_
_**Campos de Viento a las 06:00 horas**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _40/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 18**_
_**Campos de Viento a las 12:00 horas**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _41/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 19**_
_**Campos de Viento a las 18:00 horas.**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _42/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

**8.2** **Aportes Obtenidos de la Modelación**

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

**8.2.1** **Aporte en Puntos de Interés**

En la siguiente tabla se presenta los aportes obtenidos por la modelación de la
Construcción, Operación y Cierre del proyecto en los puntos de interés.

_**Modelación de Emisiones ATM064-22**_ _43/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Tabla N° 15**_
_**Aporte Planta Jucosol en Punto de interés, Fase Construcción**_

|Receptor de<br>Interés|MPS<br>mg/m2d|MP<br>10<br>μg/m3|Col4|MP<br>2,5<br>μg/m3|Col6|SO<br>2<br>μg/m3|Col8|Col9|Col10|Col11|Col12|NO<br>2<br>μg/m3|Col14|CO<br>μg/m3|Col16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor de**<br>**Interés**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Secundaria**|**Secundaria**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|
|**Receptor de**<br>**Interés**|**Media**<br>**Anual**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P99**<br>**Diario**|**P98,5**<br>**Hr**|**Media**<br>**Anual**|**P99,7**<br>**Diario**|**P99,7**<br>**3 Hr**|**Media**<br>**Anual**|**P99H**|**P99**<br>**8 hrs**|**P99**<br>**Hr**|
|R1_OLOR|0,10|0,02|0,05|0,01|0,03|0,01|0,04|0,12|0,01|0,05|0,30|0,10|4,15|1,75|0,43|
|R2_OLOR|0,08|0,01|0,03|0,01|0,01|0,01|0,02|0,05|0,01|0,02|0,11|0,05|2,88|1,03|0,16|
|R3_OLOR|0,03|0,01|0,04|<0,01|0,02|<0,01|0,05|0,04|0,00|0,08|0,16|0,02|3,59|3,32|0,50|
|R4_OLOR|0,02|0,01|0,05|<0,01|0,02|<0,01|0,06|0,05|0,00|0,08|0,28|0,04|9,69|4,61|0,60|
|R5_OLOR|0,03|0,01|0,02|<0,01|0,01|<0,01|0,01|0,03|0,00|0,01|0,07|0,02|1,84|0,67|0,12|
|R6_OLOR|0,08|0,02|0,11|0,01|0,06|0,01|0,05|0,16|0,01|0,06|0,31|0,08|6,54|2,57|0,54|
|R1_RUIDO|0,10|0,02|0,04|0,01|0,02|0,01|0,04|0,11|0,01|0,04|0,21|0,09|3,53|1,55|0,31|
|R2_RUIDO|0,08|0,01|0,03|0,01|0,01|0,01|0,02|0,05|0,01|0,02|0,11|0,05|2,86|1,02|0,17|
|R3_RUIDO|0,02|0,01|0,03|<0,01|0,02|<0,01|0,02|0,03|0,00|0,03|0,10|0,02|2,62|1,59|0,24|
|R4_RUIDO|0,02|0,00|0,03|<0,01|0,02|<0,01|0,02|0,02|0,00|0,04|0,12|0,02|2,58|1,41|0,24|
|R5_RUIDO|0,08|0,02|0,10|0,01|0,05|0,01|0,05|0,16|0,01|0,05|0,30|0,08|5,51|2,46|0,53|
|R6_RUIDO|0,03|0,01|0,04|<0,01|0,02|<0,01|0,05|0,04|<0,01|0,08|0,16|0,02|3,84|3,71|0,52|
|R7|0,01|0,01|0,03|<0,01|0,02|<0,01|0,01|0,04|<0,01|0,02|0,07|0,04|4,68|0,93|0,15|
|R8|0,04|0,01|0,03|0,01|0,02|<0,01|0,02|0,06|<0,01|0,02|0,13|0,07|3,94|1,01|0,20|
|R9|0,18|0,01|0,03|<0,01|0,01|<0,01|<0,01|0,01|<0,01|<0,01|0,03|0,02|1,64|0,32|0,05|
|R10|0,10|0,01|0,02|<0,01|<0,01|<0,01|<0,01|0,00|<0,01|<0,01|0,01|0,01|0,64|0,11|0,02|
|R11|0,28|0,01|0,02|<0,01|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,01|0,26|0,04|0,01|
|R12|0,23|0,01|0,03|<0,01|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,17|0,03|0,01|
|R13|0,02|0,00|0,01|<0,01|0,00|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,11|0,02|0,00|

_**Modelación de Emisiones ATM064-22**_ _44/144_
_Proyecto Planta Jucosol_

_Mayo, 2023_

|Receptor de<br>Interés|MPS<br>mg/m2d|MP<br>10<br>μg/m3|Col4|MP<br>2,5<br>μg/m3|Col6|SO<br>2<br>μg/m3|Col8|Col9|Col10|Col11|Col12|NO<br>2<br>μg/m3|Col14|CO<br>μg/m3|Col16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor de**<br>**Interés**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Secundaria**|**Secundaria**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|
|**Receptor de**<br>**Interés**|**Media**<br>**Anual**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P99**<br>**Diario**|**P98,5**<br>**Hr**|**Media**<br>**Anual**|**P99,7**<br>**Diario**|**P99,7**<br>**3 Hr**|**Media**<br>**Anual**|**P99H**|**P99**<br>**8 hrs**|**P99**<br>**Hr**|
|R14|0,04|<0,01|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,08|0,02|<0,01|
|R15|0,13|0,01|0,04|<0,01|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,06|0,04|0,01|
|R16|0,05|<0,01|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,05|0,01|<0,01|
|R17|0,02|<0,01|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,04|0,01|<0,01|
|R18|0,02|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,03|0,01|<0,01|
|R19|0,11|0,01|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,03|0,01|<0,01|
|R20|0,07|<0,01|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,04|0,01|<0,01|
|R21|0,12|0,01|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,04|0,01|<0,01|
|SINCA_LOS_<br>ANDES|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,01|<0,01|<0,01|

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _45/144_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Tabla N° 16**_
_**Aporte Planta Jucosol en Punto de interés, Fase Operación**_

|Receptor de<br>Interés|MPS<br>mg/m2d|MP<br>10<br>μg/m3|Col4|MP<br>2,5<br>μg/m3|Col6|SO<br>2<br>μg/m3|Col8|Col9|Col10|Col11|Col12|NO<br>2<br>μg/m3|Col14|CO<br>μg/m3|Col16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor de**<br>**Interés**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Secundaria**|**Secundaria**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|
|**Receptor de**<br>**Interés**|**Media Anual**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P99**<br>**Diario**|**P98,5**<br>**Hr**|**Media**<br>**Anual**|**P99,7**<br>**Diario**|**P99,7**<br>**3 Hr**|**Media**<br>**Anual**|**P99H**|**P99**<br>**8 hrs**|**P99**<br>**Hr**|
|R1_OLOR|0,11|0,01|0,04|0,00|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,07|0,02|0,01|
|R2_OLOR|0,29|0,02|0,05|0,00|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,07|0,03|0,01|
|R3_OLOR|0,41|0,04|0,14|0,01|0,02|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,10|0,05|0,01|
|R4_OLOR|0,07|0,01|0,07|<0,01|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,08|0,02|0,01|
|R5_OLOR|0,14|0,01|0,04|<0,01|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,07|0,03|0,01|
|R6_OLOR|0,05|0,01|0,04|<0,01|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,05|0,01|0,00|
|R1_RUIDO|0,11|0,01|0,04|<0,01|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,07|0,02|0,01|
|R2_RUIDO|0,25|0,02|0,05|<0,01|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,07|0,03|0,01|
|R3_RUIDO|0,04|0,01|0,04|<0,01|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,08|0,02|0,01|
|R4_RUIDO|0,04|0,01|0,04|<0,01|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,08|0,02|0,01|
|R5_RUIDO|0,05|0,01|0,04|<0,01|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,05|0,01|0,00|
|R6_RUIDO|0,43|0,05|0,15|0,01|0,02|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,10|0,05|0,01|
|R7|0,01|0,00|0,02|<0,01|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,04|0,01|0,00|
|R8|0,07|0,01|0,04|<0,01|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,06|0,02|0,01|
|R9|0,91|0,04|0,11|0,01|0,03|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,10|0,07|0,02|
|R10|0,50|0,02|0,07|0,01|0,02|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,11|0,04|0,01|
|R11|1,41|0,05|0,12|0,01|0,03|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,01|0,09|0,08|0,02|
|R12|1,15|0,06|0,14|0,02|0,03|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,01|0,10|0,11|0,03|
|R13|0,10|0,01|0,04|0,00|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,00|0,11|0,02|0,01|

_**Modelación de Emisiones ATM064-22**_ _46/144_
_Proyecto Planta Jucosol_

_Mayo, 2023_

|Receptor de<br>Interés|MPS<br>mg/m2d|MP<br>10<br>μg/m3|Col4|MP<br>2,5<br>μg/m3|Col6|SO<br>2<br>μg/m3|Col8|Col9|Col10|Col11|Col12|NO<br>2<br>μg/m3|Col14|CO<br>μg/m3|Col16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor de**<br>**Interés**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Secundaria**|**Secundaria**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|
|**Receptor de**<br>**Interés**|**Media Anual**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P99**<br>**Diario**|**P98,5**<br>**Hr**|**Media**<br>**Anual**|**P99,7**<br>**Diario**|**P99,7**<br>**3 Hr**|**Media**<br>**Anual**|**P99H**|**P99**<br>**8 hrs**|**P99**<br>**Hr**|
|R14|0,19|0,02|0,07|0,01|0,02|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,00|0,17|0,05|0,01|
|R15|0,67|0,06|0,18|0,01|0,05|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,01|0,16|0,23|0,04|
|R16|0,23|0,02|0,06|0,01|0,02|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,10|0,04|0,01|
|R17|0,11|0,01|0,03|0,00|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,08|0,03|0,01|
|R18|0,11|0,01|0,02|0,00|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,06|0,02|<0,01|
|R19|0,57|0,03|0,05|0,01|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,08|0,03|0,01|
|R20|0,31|0,02|0,05|0,00|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,11|0,04|0,01|
|R21|0,59|0,03|0,05|0,01|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,01|0,14|0,05|0,01|
|SINCA_LOS_<br>ANDES|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,01|<0,01|<0,01|

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _47/144_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Tabla N° 17**_
_**Aporte Planta Jucosol en Punto de interés, Fase Cierre**_

|Receptor de<br>Interés|MPS<br>mg/m2d|MP<br>10<br>μg/m3|Col4|MP<br>2,5<br>μg/m3|Col6|SO<br>2<br>μg/m3|Col8|Col9|Col10|Col11|Col12|NO<br>2<br>μg/m3|Col14|CO<br>μg/m3|Col16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor de**<br>**Interés**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Secundaria**|**Secundaria**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|
|**Receptor de**<br>**Interés**|**Media Anual**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P99**<br>**Diario**|**P98,5**<br>**Hr**|**Media**<br>**Anual**|**P99,7**<br>**Diario**|**P99,7**<br>**3 Hr**|**Media**<br>**Anual**|**P99H**|**P99**<br>**8 hrs**|**P99**<br>**Hr**|
|R1_OLOR|0,03|0,02|0,04|0,01|0,03|0,01|0,04|0,12|0,01|0,05|0,30|0,11|3,92|1,73|0,43|
|R2_OLOR|0,03|0,01|0,02|<0,01|0,01|0,01|0,02|0,05|0,01|0,02|0,11|0,05|3,06|1,12|0,17|
|R3_OLOR|0,01|<0,01|0,03|<0,01|0,02|0,00|0,04|0,04|<0,01|0,06|0,16|0,02|3,82|2,88|0,47|
|R4_OLOR|0,01|0,01|0,05|<0,01|0,02|<0,01|0,06|0,05|<0,01|0,09|0,24|0,04|8,33|3,85|0,59|
|R5_OLOR|0,01|<0,01|0,01|<0,01|0,01|<0,01|0,01|0,03|<0,01|0,01|0,07|0,02|1,86|0,66|0,11|
|R6_OLOR|0,02|0,01|0,06|0,01|0,04|0,01|0,05|0,16|0,01|0,06|0,33|0,10|6,29|2,65|0,51|
|R1_RUIDO|0,03|0,01|0,04|0,01|0,02|0,01|0,04|0,11|0,01|0,04|0,21|0,10|3,59|1,58|0,31|
|R2_RUIDO|0,03|0,01|0,02|<0,01|0,01|0,01|0,02|0,05|0,01|0,02|0,12|0,06|2,93|1,05|0,17|
|R3_RUIDO|<0,01|0,00|0,02|<0,01|0,01|<0,01|0,02|0,03|0,00|0,03|0,10|0,02|3,51|1,85|0,24|
|R4_RUIDO|<0,01|0,00|0,02|<0,01|0,01|<0,01|0,02|0,02|0,00|0,04|0,11|0,02|2,68|1,25|0,21|
|R5_RUIDO|0,01|0,01|0,06|0,01|0,03|0,01|0,05|0,16|0,01|0,05|0,31|0,10|7,96|2,55|0,52|
|R6_RUIDO|0,01|<0,01|0,03|<0,01|0,02|0,00|0,04|0,04|<0,01|0,06|0,16|0,02|3,73|2,89|0,48|
|R7|<0,01|<0,01|0,02|<0,01|0,02|0,00|0,01|0,04|<0,01|0,02|0,08|0,05|4,59|0,86|0,15|
|R8|0,01|0,01|0,02|<0,01|0,01|0,00|0,02|0,06|<0,01|0,02|0,13|0,07|3,93|0,99|0,20|
|R9|0,06|<0,01|0,01|<0,01|0,01|<0,01|<0,01|0,01|<0,01|<0,01|0,03|0,02|1,68|0,31|0,05|
|R10|0,04|<0,01|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,01|0,01|0,63|0,10|0,02|
|R11|0,10|<0,01|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,01|0,26|0,04|0,01|
|R12|0,08|<0,01|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,00|0,17|0,03|0,01|
|R13|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,11|0,02|<0,01|

_**Modelación de Emisiones ATM064-22**_ _48/144_
_Proyecto Planta Jucosol_

_Mayo, 2023_

|Receptor de<br>Interés|MPS<br>mg/m2d|MP<br>10<br>μg/m3|Col4|MP<br>2,5<br>μg/m3|Col6|SO<br>2<br>μg/m3|Col8|Col9|Col10|Col11|Col12|NO<br>2<br>μg/m3|Col14|CO<br>μg/m3|Col16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor de**<br>**Interés**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Secundaria**|**Secundaria**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|
|**Receptor de**<br>**Interés**|**Media Anual**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P99**<br>**Diario**|**P98,5**<br>**Hr**|**Media**<br>**Anual**|**P99,7**<br>**Diario**|**P99,7**<br>**3 Hr**|**Media**<br>**Anual**|**P99H**|**P99**<br>**8 hrs**|**P99**<br>**Hr**|
|R14|0,01|<0,01|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,08|0,01|<0,01|
|R15|0,05|<0,01|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,06|0,01|<0,01|
|R16|0,02|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,04|0,01|<0,01|
|R17|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,04|0,01|<0,01|
|R18|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,03|0,01|<0,01|
|R19|0,04|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,03|0,01|<0,01|
|R20|0,02|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,03|0,01|<0,01|
|R21|0,04|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,03|0,01|<0,01|
|SINCA_LOS_<br>ANDES|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,01|<0,01|<0,01|

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _49/144_
_Proyecto Planta Jucosol_

_Mayo, 2023_

**8.2.2** **Ajustes de Resultados de la Modelación por Incertidumbre**

De acuerdo con el análisis de incertidumbre de la modelación WRF presentado en
el capítulo 5 del presente informe, en la evaluación cuantitativa se determinó que
existía una sobreestimación del pronóstico de las velocidades de los vientos de WRF
en comparación con la meteorología monitoreada.

Esta sobrestimación de WRF, como archivo de entrada que alimenta la modelación
CALPUFF, implicaría una subestimación de las concentraciones de los
contaminantes, ya que a mayor velocidad del viento existiría una mayor dispersión
de los contaminantes y por ende una menor concentración de éstos en la
atmósfera.

De acuerdo con lo antes expuesto se procede a integrar a los resultados de la
modelación la incertidumbre generada, para esto se escogió el máximo porcentaje
de sobrestimación alcanzado (56%) y fue aplicado de acuerdo con la siguiente
ecuación:

RM [′] = RM + % de incertidumbre ∗RM (IX)

Dónde:

RM’ : Resultados de la modelación WRF-CALPUFF corregidos por incertidumbre
RM : Resultados modelación WRF-CALPUFF (concentraciones contaminantes)

% de incertidumbre : 56%, mayor porcentaje de sobrestimación alcanzado en
la evaluación cuantitativa del WRF (sección 5 del presente
informe).

De acuerdo con lo antes expuesto, en las siguientes tablas se presentan los
resultados con la corrección por incertidumbre aplicada de acuerdo a la fórmula
descrita (IX).

_**Modelación de Emisiones ATM064-22**_ _50/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Tabla N° 18**_
_**Aporte Planta Jucosol**_
_**Punto de interés con Incertidumbre del 56%, Fase de Construcción**_

|Receptor de<br>Interés|MPS<br>mg/m2d|MP<br>10<br>μg/m3|Col4|MP<br>2,5<br>μg/m3|Col6|SO<br>2<br>μg/m3|Col8|Col9|Col10|Col11|Col12|NO<br>2<br>μg/m3|Col14|CO<br>μg/m3|Col16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor de**<br>**Interés**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Secundaria**|**Secundaria**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|
|**Receptor de**<br>**Interés**|**Media Anual**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P99**<br>**Diario**|**P98,5**<br>**Hr**|**Media**<br>**Anual**|**P99,7**<br>**Diario**|**P99,7**<br>**3 Hr**|**Media**<br>**Anual**|**P99H**|**P99**<br>**8 hrs**|**P99**<br>**Hr**|
|R1_OLOR|0,17|0,03|0,08|0,02|0,04|0,02|0,07|0,18|0,02|0,08|0,46|0,16|6,47|2,73|0,67|
|R2_OLOR|0,45|0,02|0,04|0,01|0,02|0,01|0,03|0,08|0,01|0,04|0,17|0,07|4,49|1,61|0,25|
|R3_OLOR|0,65|0,01|0,06|0,01|0,03|0,00|0,07|0,06|0,00|0,12|0,25|0,03|5,59|5,18|0,78|
|R4_OLOR|0,11|0,01|0,07|0,01|0,04|0,01|0,09|0,08|0,01|0,12|0,43|0,06|15,11|7,18|0,93|
|R5_OLOR|0,21|0,01|0,03|0,00|0,01|0,00|0,02|0,04|0,00|0,02|0,10|0,03|2,86|1,05|0,18|
|R6_OLOR|0,07|0,03|0,17|0,02|0,09|0,01|0,07|0,25|0,01|0,09|0,49|0,13|10,21|4,01|0,84|
|R1_RUIDO|0,18|0,03|0,07|0,02|0,04|0,02|0,06|0,17|0,02|0,06|0,33|0,15|5,51|2,42|0,49|
|R2_RUIDO|0,39|0,02|0,04|0,01|0,02|0,01|0,03|0,08|0,01|0,03|0,17|0,08|4,46|1,60|0,26|
|R3_RUIDO|0,07|0,01|0,05|0,00|0,03|<0,01|0,03|0,04|0,00|0,05|0,16|0,02|4,08|2,49|0,37|
|R4_RUIDO|0,06|0,01|0,05|0,00|0,02|<0,01|0,03|0,04|0,00|0,07|0,18|0,03|4,03|2,19|0,37|
|R5_RUIDO|0,07|0,03|0,16|0,02|0,08|0,01|0,07|0,25|0,01|0,08|0,46|0,13|8,60|3,84|0,83|
|R6_RUIDO|0,67|0,01|0,06|0,01|0,03|0,00|0,07|0,06|0,00|0,13|0,26|0,03|5,99|5,78|0,81|
|R7|0,01|0,01|0,05|0,01|0,02|0,00|0,02|0,06|0,00|0,03|0,12|0,07|7,30|1,45|0,23|
|R8|0,11|0,02|0,04|0,01|0,02|0,01|0,03|0,09|0,01|0,03|0,20|0,10|6,15|1,57|0,31|
|R9|1,41|0,01|0,04|<0,01|0,01|<0,01|0,01|0,02|<0,01|0,01|0,04|0,03|2,55|0,50|0,07|
|R10|0,78|0,01|0,02|<0,01|0,01|<0,01|0,00|0,01|0,00|<0,01|0,01|0,01|0,99|0,17|0,03|
|R11|2,20|0,02|0,04|<0,01|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,01|0,01|0,41|0,06|0,02|
|R12|1,80|0,02|0,04|0,01|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,01|0,26|0,05|0,01|

_**Modelación de Emisiones ATM064-22**_ _51/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

|Receptor de<br>Interés|MPS<br>mg/m2d|MP<br>10<br>μg/m3|Col4|MP<br>2,5<br>μg/m3|Col6|SO<br>2<br>μg/m3|Col8|Col9|Col10|Col11|Col12|NO<br>2<br>μg/m3|Col14|CO<br>μg/m3|Col16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor de**<br>**Interés**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Secundaria**|**Secundaria**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|
|**Receptor de**<br>**Interés**|**Media Anual**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P99**<br>**Diario**|**P98,5**<br>**Hr**|**Media**<br>**Anual**|**P99,7**<br>**Diario**|**P99,7**<br>**3 Hr**|**Media**<br>**Anual**|**P99H**|**P99**<br>**8 hrs**|**P99**<br>**Hr**|
|R13|0,15|0,00|0,01|0,00|0,00|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,17|0,03|0,01|
|R14|0,29|0,01|0,02|<0,01|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,13|0,02|0,01|
|R15|1,04|0,02|0,06|<0,01|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,10|0,06|0,01|
|R16|0,37|0,01|0,02|<0,01|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,08|0,02|<0,01|
|R17|0,17|<0,01|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,06|0,01|<0,01|
|R18|0,17|<0,01|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,05|0,01|<0,01|
|R19|0,88|0,01|0,02|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,05|0,01|<0,01|
|R20|0,49|0,01|0,02|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,05|0,01|<0,01|
|R21|0,92|0,01|0,02|<0,01|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,06|0,02|<0,01|
|SINCA_LOS_<br>ANDES|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,02|<0,01|<0,01|

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _52/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Tabla N° 19**_
_**Aporte Planta Jucosol,**_
_**Punto de interés con Incertidumbre del 56%, Fase Operación**_

|Receptor de<br>Interés|MPS<br>mg/m2d|MP<br>10<br>μg/m3|Col4|MP<br>2,5<br>μg/m3|Col6|SO<br>2<br>μg/m3|Col8|Col9|Col10|Col11|Col12|NO<br>2<br>μg/m3|Col14|CO<br>μg/m3|Col16|Col17|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor de**<br>**Interés**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Secundaria**|**Secundaria**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|
|**Receptor de**<br>**Interés**|**Media Anual**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P99**<br>**Diario**|**P98,5**<br>**Hr**|**Media**<br>**Anual**|**P99,7**<br>**Diario**|**P99,7**<br>**3 Hr**|**Media**<br>**Anual**|**P99H**|**P99**<br>**8 hrs**|**P99**<br>**Hr**|**P99**<br>**Hr**|
|R1_OLOR|0,17|0,02|0,07|0,00|0,02|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,10|0,03|0,01|0,01|
|R2_OLOR|0,45|0,03|0,09|0,01|0,02|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,12|0,04|0,01|0,01|
|R3_OLOR|0,65|0,07|0,22|0,01|0,04|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,16|0,07|0,02|0,02|
|R4_OLOR|0,11|0,02|0,11|0,00|0,02|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,12|0,04|0,01|0,01|
|R5_OLOR|0,21|0,02|0,06|0,00|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,11|0,04|0,01|0,01|
|R6_OLOR|0,07|0,01|0,06|0,00|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,09|0,02|0,01|0,01|
|R1_RUIDO|0,18|0,02|0,07|0,00|0,02|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,11|0,04|0,01|0,01|
|R2_RUIDO|0,39|0,03|0,08|0,01|0,02|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,12|0,04|0,01|0,01|
|R3_RUIDO|0,07|0,01|0,06|0,00|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,12|0,04|0,01|0,01|
|R4_RUIDO|0,06|0,01|0,06|0,00|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,12|0,04|0,01|0,01|
|R5_RUIDO|0,07|0,01|0,06|0,00|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,09|0,02|0,01|0,01|
|R6_RUIDO|0,67|0,07|0,23|0,01|0,04|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,16|0,07|0,02|0,02|
|R7|0,01|0,01|0,03|0,00|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,06|0,01|0,00|0,00|
|R8|0,11|0,01|0,06|0,00|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,09|0,03|0,01|0,01|
|R9|1,41|0,06|0,18|0,01|0,05|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,01|0,16|0,12|0,03|0,03|
|R10|0,78|0,04|0,11|0,01|0,03|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,01|0,18|0,06|0,02|0,02|
|R11|2,20|0,07|0,18|0,02|0,05|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,01|0,14|0,13|0,03|0,03|
|R12|1,80|0,09|0,21|0,02|0,05|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,01|0,15|0,18|0,04|0,04|
|R13|0,15|0,02|0,07|0,00|0,02|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,17|0,03|0,01|0,01|

_**Modelación de Emisiones ATM064-22**_ _53/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

|Receptor de<br>Interés|MPS<br>mg/m2d|MP<br>10<br>μg/m3|Col4|MP<br>2,5<br>μg/m3|Col6|SO<br>2<br>μg/m3|Col8|Col9|Col10|Col11|Col12|NO<br>2<br>μg/m3|Col14|CO<br>μg/m3|Col16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor de**<br>**Interés**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Secundaria**|**Secundaria**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|
|**Receptor de**<br>**Interés**|**Media Anual**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P99**<br>**Diario**|**P98,5**<br>**Hr**|**Media**<br>**Anual**|**P99,7**<br>**Diario**|**P99,7**<br>**3 Hr**|**Media**<br>**Anual**|**P99H**|**P99**<br>**8 hrs**|**P99**<br>**Hr**|
|R14|0,29|0,03|0,11|0,01|0,03|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,01|0,27|0,07|0,02|
|R15|1,04|0,09|0,28|0,02|0,07|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,01|0,25|0,36|0,06|
|R16|0,37|0,04|0,10|0,01|0,02|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,01|0,15|0,06|0,02|
|R17|0,17|0,02|0,05|0,00|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,13|0,04|0,01|
|R18|0,17|0,01|0,04|0,00|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,09|0,03|0,01|
|R19|0,88|0,04|0,08|0,01|0,02|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,01|0,12|0,05|0,01|
|R20|0,49|0,03|0,07|0,01|0,02|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,01|0,17|0,06|0,01|
|R21|0,92|0,04|0,09|0,01|0,02|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,01|0,21|0,08|0,01|
|SINCA_LOS_<br>ANDES|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,00|0,01|<0,01|<0,01|

Fuente: Algoritmos SpA, 2023

_**Tabla N° 20**_
_**Aporte Planta Jucosol**_
_**Punto de interés con Incertidumbre del 56%en Punto de interés, Fase Cierre**_

|Receptor de<br>Interés|MPS<br>mg/m2d|MP<br>10<br>μg/m3|Col4|MP<br>2,5<br>μg/m3|Col6|SO<br>2<br>μg/m3|Col8|Col9|Col10|Col11|Col12|NO<br>2<br>μg/m3|Col14|CO<br>μg/m3|Col16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor de**<br>**Interés**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Secundaria**|**Secundaria**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|
|**Receptor de**<br>**Interés**|**Media Anual**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P99**<br>**Diario**|**P98,5**<br>**Hr**|**Media**<br>**Anual**|**P99,7**<br>**Diario**|**P99,7**<br>**3 Hr**|**Media**<br>**Anual**|**P99H**|**P99**<br>**8 hrs**|**P99**<br>**Hr**|
|R1_OLOR|0,05|0,02|0,07|0,01|0,04|0,02|0,07|0,19|0,02|0,08|0,46|0,18|6,12|2,71|0,67|
|R2_OLOR|0,05|0,01|0,03|0,01|0,02|0,01|0,03|0,08|0,01|0,04|0,17|0,08|4,77|1,75|0,27|
|R3_OLOR|0,01|0,01|0,05|0,00|0,03|0,00|0,06|0,06|0,00|0,09|0,25|0,04|5,96|4,49|0,73|
|R4_OLOR|0,01|0,01|0,07|0,01|0,04|0,01|0,10|0,07|0,01|0,14|0,38|0,06|12,99|6,01|0,93|

_**Modelación de Emisiones ATM064-22**_ _54/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

|Receptor de<br>Interés|MPS<br>mg/m2d|MP<br>10<br>μg/m3|Col4|MP<br>2,5<br>μg/m3|Col6|SO<br>2<br>μg/m3|Col8|Col9|Col10|Col11|Col12|NO<br>2<br>μg/m3|Col14|CO<br>μg/m3|Col16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor de**<br>**Interés**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Secundaria**|**Secundaria**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|
|**Receptor de**<br>**Interés**|**Media Anual**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P99**<br>**Diario**|**P98,5**<br>**Hr**|**Media**<br>**Anual**|**P99,7**<br>**Diario**|**P99,7**<br>**3 Hr**|**Media**<br>**Anual**|**P99H**|**P99**<br>**8 hrs**|**P99**<br>**Hr**|
|R5_OLOR|0,02|0,00|0,02|<0,01|0,01|<0,01|0,01|0,04|<0,01|0,02|0,11|0,03|2,90|1,03|0,18|
|R6_OLOR|0,02|0,02|0,09|0,01|0,05|0,01|0,07|0,25|0,01|0,09|0,51|0,15|9,81|4,13|0,79|
|R1_RUIDO|0,05|0,02|0,06|0,01|0,03|0,02|0,06|0,17|0,02|0,07|0,32|0,16|5,60|2,46|0,49|
|R2_RUIDO|0,04|0,01|0,03|0,01|0,02|0,01|0,03|0,08|0,01|0,03|0,19|0,09|4,58|1,64|0,26|
|R3_RUIDO|0,01|0,00|0,03|<0,01|0,02|<0,01|0,04|0,04|0,00|0,05|0,16|0,03|5,48|2,88|0,37|
|R4_RUIDO|0,01|0,00|0,03|<0,01|0,02|<0,01|0,03|0,04|0,00|0,06|0,18|0,03|4,18|1,95|0,33|
|R5_RUIDO|0,02|0,02|0,09|0,01|0,05|0,01|0,08|0,26|0,01|0,08|0,49|0,15|12,42|3,97|0,82|
|R6_RUIDO|0,01|0,01|0,05|0,00|0,03|<0,01|0,06|0,06|0,00|0,09|0,25|0,04|5,81|4,51|0,74|
|R7|<0,01|0,01|0,03|0,00|0,02|<0,01|0,02|0,06|0,00|0,03|0,12|0,08|7,16|1,34|0,23|
|R8|0,02|0,01|0,04|0,01|0,02|0,01|0,03|0,09|0,01|0,03|0,21|0,11|6,13|1,54|0,31|
|R9|0,10|0,01|0,02|<0,01|0,01|<0,01|0,01|0,02|0,00|0,01|0,04|0,03|2,63|0,48|0,07|
|R10|0,05|0,00|0,01|<0,01|0,01|<0,01|<0,01|0,01|0,00|<0,01|0,01|0,02|0,98|0,16|0,03|
|R11|0,15|0,01|0,01|<0,01|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,01|0,01|0,41|0,06|0,01|
|R12|0,12|0,01|0,02|<0,01|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,01|0,27|0,05|0,01|
|R13|0,01|0,00|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,17|0,03|0,01|
|R14|0,02|0,00|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,12|0,02|0,01|
|R15|0,07|0,01|0,02|<0,01|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,10|0,02|<0,01|
|R16|0,03|0,00|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,06|0,01|<0,01|
|R17|0,01|0,00|0,00|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,06|0,01|<0,01|
|R18|0,01|0,00|0,00|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,05|0,01|<0,01|
|R19|0,06|0,00|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,05|0,01|<0,01|

_**Modelación de Emisiones ATM064-22**_ _55/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

|Receptor de<br>Interés|MPS<br>mg/m2d|MP<br>10<br>μg/m3|Col4|MP<br>2,5<br>μg/m3|Col6|SO<br>2<br>μg/m3|Col8|Col9|Col10|Col11|Col12|NO<br>2<br>μg/m3|Col14|CO<br>μg/m3|Col16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor de**<br>**Interés**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Secundaria**|**Secundaria**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|
|**Receptor de**<br>**Interés**|**Media Anual**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P99**<br>**Diario**|**P98,5**<br>**Hr**|**Media**<br>**Anual**|**P99,7**<br>**Diario**|**P99,7**<br>**3 Hr**|**Media**<br>**Anual**|**P99H**|**P99**<br>**8 hrs**|**P99**<br>**Hr**|
|R20|0,04|0,00|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,05|0,01|<0,01|
|R21|0,06|0,00|0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,05|0,01|<0,01|
|SINCA_LOS_<br>ANDES|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|<0,01|0,02|<0,01|<0,01|

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _56/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

**8.3** **Aportes en Puntos de Máxima Concentración**

La siguiente tabla presenta la ubicación de los Puntos de Máximo Impacto (PMI),
para los contaminantes MP 10, MP 2,5, MPS, SO 2, NO 2 y CO, durante la fase de
construcción, operación y cierre del Proyecto.

_**Tabla N° 21**_
_**Localización Punto Máximo Impacto (PMI), Fase Construcción**_

|Parámetro|Estadístico|PMI|Norma|Unidad|%<br>Norma|Coordenadas UTM -<br>WGS84|Col8|
|---|---|---|---|---|---|---|---|
|**Parámetro**|**Estadístico**|**PMI**|**Norma**|**Unidad**|**% **<br>**Norma**|**Este (m)**|**Norte (m)**|
|MPS|Promedio<br>del Periodo|10,94|200|mg/m2-<br>día|5,47%|346.618|6.370.861|
|MP10|Promedio<br>del Periodo|2,95|50|μg/m3|5,90%|346.618|6.370.861|
|MP10|Percentil 98<br>Diario|6,57|130|130|5,06%|346.618|6.370.861|
|MP2,5|Promedio<br>del Periodo|1,57|20|20|7,84%|346.618|6.370.861|
|MP2,5|Percentil 98<br>Diario|3,49|50|50|6,99%|346.618|6.370.861|
|SO2|Promedio<br>del Periodo|2,98|60|60|4,97%|346.618|6.370.861|
|SO2|Percentil 99<br>Diario|6,93|150|150|4,62%|346.618|6.370.861|
|SO2|Percentil<br>98,5 Diario|19,13|350|350|5,47%|346.618|6.370.861|
|SO2|Promedio<br>del Periodo|2,98|80|80|3,73%|346.618|6.370.861|
|SO2|Percentil<br>99,7 Diario|7,33|365|365|2,01%|346.618|6.370.861|
|SO2|Percentil<br>99,73<br>Horario|23,46|1.000|1.000|2,35%|346.618|6.370.861|
|NO2|Promedio<br>del Periodo|6,34|100|100|6,34%|346.618|6.370.861|
|NO2|Percentil 99<br>Diario|56,95|400|400|14,24%|346.618|6.370.861|
|CO<br>|Percentil 99<br>8 Horas|52,81|10.000|10.000|0,38%|346.618|6.370.861|
|CO<br>|Percentil 99<br>Horario<br>|113,98|30.000|30.000|0,53%|346.618|6.370.861|

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _57/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Tabla N° 22**_
_**Localización Punto Máximo Impacto (PMI), Fase Operación**_

|Parámetro|Estadístico|PMI|Norma|Unidad|%<br>Norma|Coordenadas UTM -<br>WGS84|Col8|
|---|---|---|---|---|---|---|---|
|**Parámetro**|**Estadístico**|**PMI**|**Norma**|**Unidad**|**% **<br>**Norma**|**Este (m)**|**Norte (m)**|
|MPS|Promedio<br>del Periodo|3,66|200|mg/m2-<br>día|1,83%|347.123|6.370.669|
|MP10|Promedio<br>del Periodo|0,32|50|μg/m3|0,63%|346.556|6.371.007|
|MP10|Percentil 98<br>Diario|0,97|130|130|0,74%|346.597|6.370.960|
|MP2,5|Promedio<br>del Periodo|0,04|20|20|0,20%|346.818|6.370.904|
|MP2,5|Percentil 98<br>Diario|0,11|50|50|0,23%|346.597|6.370.960|
|SO2|Promedio<br>del Periodo|<0,01|60|60|<0,01%|346.818|6.370.904|
|SO2|Percentil 99<br>Diario|<0,01|150|150|<0,01%|346.798|6.370.923|
|SO2|Percentil<br>98,5 Diario|<0,01|350|350|<0,01%|346.437|6.370.918|
|SO2|Promedio<br>del Periodo|<0,01|80|80|<0,01%|346.818|6.370.904|
|SO2|Percentil<br>99,7 Diario|<0,01|365|365|<0,01%|346.798|6.370.923|
|SO2|Percentil<br>99,73<br>Horario|<0,01|1.000|1.000|<0,01%|346.798|6.370.943|
|NO2|Promedio<br>del Periodo|0,01|100|100|0,01%|350.650|6.369.427|
|NO2|Percentil 99<br>Diario|0,37|400|400|0,09%|346.757|6.370.943|
|CO|Percentil 99<br>8 Horas|0,05|10.000|10.000|<0,01%|346.798|6.370.923|
|CO|Percentil 99<br>Horario|0,33|30.000|30.000|<0,01%|346.798|6.370.923|

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _58/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Tabla N° 23**_
_**Localización Punto Máximo Impacto (PMI), Fase Cierre**_

|Parámetro|Estadístico|PMI|Norma|Unidad|%<br>Norma|Coordenadas UTM -<br>WGS84|Col8|
|---|---|---|---|---|---|---|---|
|**Parámetro**|**Estadístico**|**PMI**|**Norma**|**Unidad**|**% **<br>**Norma**|**Este (m)**|**Norte (m)**|
|MPS|Promedio<br>del Periodo|6,22|200|mg/m2-<br>día|3,11%|346.618|6.370.861|
|MP10|Promedio<br>del Periodo|2,18|50|μg/m3|4,37%|346.618|6.370.861|
|MP10|Percentil 98<br>Diario|5,85|130|130|4,50%|346.618|6.370.861|
|MP2,5|Promedio<br>del Periodo|1,16|20|20|5,80%|346.618|6.370.861|
|MP2,5|Percentil 98<br>Diario|3,11|50|50|6,22%|346.618|6.370.861|
|SO2|Promedio<br>del Periodo|2,22|60|60|3,70%|346.618|6.370.861|
|SO2|Percentil 99<br>Diario|6,30|150|150|4,20%|346.618|6.370.861|
|SO2|Percentil<br>98,5 Diario|19,74|350|350|5,64%|346.618|6.370.861|
|SO2|Promedio<br>del Periodo|2,22|80|80|2,77%|346.618|6.370.861|
|SO2|Percentil<br>99,7 Diario|6,85|365|365|1,88%|346.618|6.370.861|
|SO2|Percentil<br>99,73<br>Horario|25,88|1.000|1.000|2,59%|346.618|6.370.861|
|NO2|Promedio<br>del Periodo|56,25|100|100|4,51%|346.618|6.370.861|
|NO2|Percentil 99<br>Diario|63,95|400|400|15,99%|346.618|6.370.861|
|CO<br>|Percentil 99<br>8 Horas|83,75|10.000|10.000|0,56%|346.618|6.370.861|
|CO<br>|Percentil 99<br>Horario<br>|130,65|30.000|30.000|0,44%|346.618|6.370.861|

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _59/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 20**_
_**Ubicación de Puntos de Máximo Impacto, Fase Construcción**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _60/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 21**_
_**Ubicación de Puntos de Máximo Impacto, Fase Operación**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _61/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 22**_
_**Ubicación de Puntos de Máximo Impacto, Fase Cierre**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _62/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

**8.4** **Comparación Estaciones de Monitoreo con Línea de Base**

En la siguiente tabla, muestra la relación entre la línea base (LB) y los datos
modelados (DM) con ajuste de incertidumbre.

_**Tabla N° 24**_
_**Relación entre la línea base (LB) y los datos modelados (DM) con ajuste**_

_**de incertidumbre, Fase Construcción**_

|Estación|Parámetro|Estadístico|AP|Lb|AP+Lb|Norma|%<br>Norma|
|---|---|---|---|---|---|---|---|
|**Estación**|**Parámetro**|**Estadístico**|**(ug/m3N)**|**(ug/m3N)**|**(ug/m3N)**|**(ug/m3N)**|**(ug/m3N)**|
|Los Andes<br>|NO2 <br>|Promedio<br>del Periodo|<0,01|23,8|23,8|100|24%|
|Los Andes<br>|NO2 <br>|Percentil 99<br>Horario<br>|0,02|104,1|104,1|400|26%|

Fuente: Algoritmos SpA, 2023

_**Tabla N° 25**_
_**Relación entre la línea base (LB) y los datos modelados (DM) con ajuste**_

_**de incertidumbre, Fase Operación**_

|Estación|Parámetro|Estadístico|AP|Lb|AP+Lb|Norma|%<br>Norma|
|---|---|---|---|---|---|---|---|
|**Estación**|**Parámetro**|**Estadístico**|**(ug/m3N)**|**(ug/m3N)**|**(ug/m3N)**|**(ug/m3N)**|**(ug/m3N)**|
|Los Andes<br>|NO2 <br>|Promedio<br>del Periodo|<0,01|23,8|23,8|100|24%|
|Los Andes<br>|NO2 <br>|Percentil 99<br>Horario<br>|<0,01|104,1|104,1|400|26%|

Fuente: Algoritmos SpA, 2023

_**Tabla N° 26**_
_**Relación entre la línea base (LB) y los datos modelados (DM) con ajuste**_

_**de incertidumbre, Fase Cierre**_

|Estación|Parámetro|Estadístico|AP|Lb|AP+Lb|Norma|%<br>Norma|
|---|---|---|---|---|---|---|---|
|**Estación**|**Parámetro**|**Estadístico**|**(ug/m3N)**|**(ug/m3N)**|**(ug/m3N)**|**(ug/m3N)**|**(ug/m3N)**|
|Los Andes<br>|NO2 <br>|Promedio<br>del Periodo|<0,01|23,8|23,8|100|24%|
|Los Andes<br>|NO2 <br>|Percentil 99<br>Horario<br>|0,02|104,1|104,1|400|26%|

Fuente: Algoritmos SpA, 2023

**8.5** **Porcentaje de aporte según normativa en puntos de interés**

_**Modelación de Emisiones ATM064-22**_ _63/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Tabla N° 27**_
_**Porcentaje de aporte según normativa en puntos de interés, con incertidumbre**_

_**Fase de Construcción**_

|Receptor de<br>Interés|MPS<br>mg/m2d|MP<br>10<br>μg/m3|Col4|MP<br>2,5<br>μg/m3|Col6|SO<br>2<br>μg/m3|Col8|Col9|Col10|Col11|Col12|NO<br>2<br>μg/m3|Col14|CO<br>μg/m3|Col16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor de**<br>**Interés**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Secundaria**|**Secundaria**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|
|**Receptor de**<br>**Interés**|**Media Anual**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P99**<br>**Diario**|**P98,5**<br>**Hr**|**Media**<br>**Anual**|**P99,7**<br>**Diario**|**P99,7**<br>**3 Hr**|**Media**<br>**Anual**|**P99H**|**P99**<br>**8 hrs**|**P99**<br>**Hr**|
|R1_OLOR|0,08%|0,07%|0,06%|0,09%|0,09%|0,03%|0,05%|0,05%|0,03%|0,02%|0,05%|0,16%|1,62%|0,01%|0,01%|
|R2_OLOR|0,22%|0,04%|0,03%|0,04%|0,04%|0,01%|0,02%|0,02%|0,01%|0,01%|0,02%|0,07%|1,12%|0,01%|0,00%|
|R3_OLOR|0,32%|0,02%|0,05%|0,03%|0,07%|0,01%|0,05%|0,02%|0,01%|0,03%|0,02%|0,03%|1,40%|0,02%|0,01%|
|R4_OLOR|0,06%|0,02%|0,06%|0,03%|0,07%|0,01%|0,06%|0,02%|0,01%|0,03%|0,04%|0,06%|3,78%|0,02%|0,01%|
|R5_OLOR|0,11%|0,02%|0,02%|0,02%|0,03%|<0,01%|0,01%|0,01%|0,00%|0,01%|0,01%|0,03%|0,72%|0,00%|0,00%|
|R6_OLOR|0,04%|0,06%|0,13%|0,08%|0,17%|0,02%|0,05%|0,07%|0,02%|0,02%|0,05%|0,13%|2,55%|0,01%|0,01%|
|R1_RUIDO|0,09%|0,06%|0,05%|0,08%|0,07%|0,03%|0,04%|0,05%|0,02%|0,02%|0,03%|0,15%|1,38%|0,01%|<0,01%|
|R2_RUIDO|0,20%|0,04%|0,03%|0,04%|0,04%|0,01%|0,02%|0,02%|0,01%|0,01%|0,02%|0,08%|1,12%|0,01%|<0,01%|
|R3_RUIDO|0,03%|0,02%|0,04%|0,02%|0,05%|<0,01%|0,02%|0,01%|0,00%|0,01%|0,02%|0,02%|1,02%|0,01%|<0,01%|
|R4_RUIDO|0,03%|0,02%|0,04%|0,02%|0,05%|<0,01%|0,02%|0,01%|0,00%|0,02%|0,02%|0,03%|1,01%|0,01%|<0,01%|
|R5_RUIDO|0,04%|0,06%|0,12%|0,08%|0,17%|0,02%|0,05%|0,07%|0,02%|0,02%|0,05%|0,13%|2,15%|0,01%|0,01%|
|R6_RUIDO|0,33%|0,02%|0,05%|0,03%|0,07%|0,01%|0,05%|0,02%|0,01%|0,04%|0,03%|0,03%|1,50%|0,02%|0,01%|
|R7|0,01%|0,02%|0,04%|0,03%|0,05%|0,01%|0,01%|0,02%|<0,01%|0,01%|0,01%|0,07%|1,82%|0,00%|<0,01%|
|R8|0,05%|0,03%|0,03%|0,04%|0,05%|0,01%|0,02%|0,02%|0,01%|0,01%|0,02%|0,10%|1,54%|0,01%|<0,01%|
|R9|0,71%|0,03%|0,03%|0,02%|0,03%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,03%|0,64%|<0,01%|<0,01%|
|R10|0,39%|0,02%|0,02%|0,02%|0,02%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,01%|0,25%|<0,01%|<0,01%|
|R11|1,10%|0,03%|0,03%|0,02%|0,02%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,01%|0,10%|<0,01%|<0,01%|
|R12|0,90%|0,04%|0,03%|0,03%|0,02%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,01%|0,07%|<0,01%|<0,01%|

_**Modelación de Emisiones ATM064-22**_ _64/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

|Receptor de<br>Interés|MPS<br>mg/m2d|MP<br>10<br>μg/m3|Col4|MP<br>2,5<br>μg/m3|Col6|SO<br>2<br>μg/m3|Col8|Col9|Col10|Col11|Col12|NO<br>2<br>μg/m3|Col14|CO<br>μg/m3|Col16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor de**<br>**Interés**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Secundaria**|**Secundaria**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|
|**Receptor de**<br>**Interés**|**Media Anual**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P99**<br>**Diario**|**P98,5**<br>**Hr**|**Media**<br>**Anual**|**P99,7**<br>**Diario**|**P99,7**<br>**3 Hr**|**Media**<br>**Anual**|**P99H**|**P99**<br>**8 hrs**|**P99**<br>**Hr**|
|R13|0,08%|0,01%|0,01%|0,01%|0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,04%|<0,01%|<0,01%|
|R14|0,15%|0,01%|0,02%|0,01%|0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,03%|<0,01%|<0,01%|
|R15|0,52%|0,04%|0,04%|0,02%|0,03%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,02%|<0,01%|<0,01%|
|R16|0,18%|0,02%|0,01%|0,01%|0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,02%|<0,01%|<0,01%|
|R17|0,09%|0,01%|0,01%|0,01%|0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,02%|<0,01%|<0,01%|
|R18|0,09%|0,01%|0,01%|0,01%|0,00%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,01%|<0,01%|<0,01%|
|R19|0,44%|0,02%|0,01%|0,01%|0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,01%|<0,01%|<0,01%|
|R20|0,24%|0,01%|0,01%|0,01%|0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,01%|<0,01%|<0,01%|
|R21|0,46%|0,02%|0,01%|0,01%|0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,01%|<0,01%|<0,01%|
|SINCA_LOS_AND<br>ES|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,01%|<0,01%|<0,01%|

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _65/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Tabla N° 28**_
_**Porcentaje de aporte según normativa en puntos de interés, con incertidumbre**_

_**Fase de Operación**_

|Receptor de<br>Interés|MPS<br>mg/m2d|MP<br>10<br>μg/m3|Col4|MP<br>2,5<br>μg/m3|Col6|SO<br>2<br>μg/m3|Col8|Col9|Col10|Col11|Col12|NO<br>2<br>μg/m3|Col14|CO<br>μg/m3|Col16|Col17|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor de**<br>**Interés**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Secundaria**|**Secundaria**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|
|**Receptor de**<br>**Interés**|**Media Anual**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P99**<br>**Diario**|**P98,5**<br>**Hr**|**Media**<br>**Anual**|**P99,7**<br>**Diario**|**P99,7**<br>**3 Hr**|**Media**<br>**Anual**|**P99H**|**P99**<br>**8 hrs**|**P99**<br>**Hr**|**P99**<br>**Hr**|
|R1_OLOR|0,08%|0,04%|0,05%|0,02%|0,03%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,03%|<0,01%|<0,01%|<0,01%|
|R2_OLOR|0,22%|0,06%|0,07%|0,04%|0,04%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,03%|<0,01%|<0,01%|<0,01%|
|R3_OLOR|0,32%|0,14%|0,17%|0,05%|0,07%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,04%|<0,01%|<0,01%|<0,01%|
|R4_OLOR|0,06%|0,04%|0,09%|0,02%|0,04%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,03%|<0,01%|<0,01%|<0,01%|
|R5_OLOR|0,11%|0,03%|0,05%|0,02%|0,03%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,03%|<0,01%|<0,01%|<0,01%|
|R6_OLOR|0,04%|0,03%|0,04%|0,01%|0,03%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,02%|<0,01%|<0,01%|<0,01%|
|R1_RUIDO|0,09%|0,04%|0,05%|0,02%|0,03%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,03%|<0,01%|<0,01%|<0,01%|
|R2_RUIDO|0,20%|0,05%|0,06%|0,03%|0,04%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,03%|<0,01%|<0,01%|<0,01%|
|R3_RUIDO|0,03%|0,02%|0,05%|0,01%|0,03%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,03%|<0,01%|<0,01%|<0,01%|
|R4_RUIDO|0,03%|0,02%|0,05%|0,01%|0,02%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,03%|<0,01%|<0,01%|<0,01%|
|R5_RUIDO|0,04%|0,03%|0,04%|0,01%|0,03%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,02%|<0,01%|<0,01%|<0,01%|
|R6_RUIDO|0,33%|0,14%|0,18%|0,05%|0,07%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,04%|<0,01%|<0,01%|<0,01%|
|R7|0,01%|0,01%|0,03%|0,01%|0,02%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,02%|<0,01%|<0,01%|<0,01%|
|R8|0,05%|0,03%|0,04%|0,02%|0,03%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,02%|<0,01%|<0,01%|<0,01%|
|R9|0,71%|0,11%|0,14%|0,07%|0,09%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,01%|0,04%|<0,01%|<0,01%|<0,01%|
|R10|0,39%|0,07%|0,08%|0,05%|0,06%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,01%|0,04%|<0,01%|<0,01%|<0,01%|
|R11|1,10%|0,14%|0,14%|0,09%|0,09%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,01%|0,03%|<0,01%|<0,01%|<0,01%|
|R12|0,90%|0,19%|0,16%|0,12%|0,11%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,01%|0,04%|<0,01%|<0,01%|<0,01%|
|R13|0,08%|0,04%|0,05%|0,02%|0,04%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,04%|<0,01%|<0,01%|<0,01%|

_**Modelación de Emisiones ATM064-22**_ _66/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

|Receptor de<br>Interés|MPS<br>mg/m2d|MP<br>10<br>μg/m3|Col4|MP<br>2,5<br>μg/m3|Col6|SO<br>2<br>μg/m3|Col8|Col9|Col10|Col11|Col12|NO<br>2<br>μg/m3|Col14|CO<br>μg/m3|Col16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor de**<br>**Interés**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Secundaria**|**Secundaria**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|
|**Receptor de**<br>**Interés**|**Media Anual**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P99**<br>**Diario**|**P98,5**<br>**Hr**|**Media**<br>**Anual**|**P99,7**<br>**Diario**|**P99,7**<br>**3 Hr**|**Media**<br>**Anual**|**P99H**|**P99**<br>**8 hrs**|**P99**<br>**Hr**|
|R14|0,15%|0,07%|0,08%|0,04%|0,05%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,01%|0,07%|<0,01%|<0,01%|
|R15|0,52%|0,17%|0,21%|0,11%|0,14%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,01%|0,06%|<0,01%|<0,01%|
|R16|0,18%|0,07%|0,07%|0,04%|0,05%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,01%|0,04%|<0,01%|<0,01%|
|R17|0,09%|0,04%|0,04%|0,02%|0,03%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,00%|0,03%|<0,01%|<0,01%|
|R18|0,09%|0,02%|0,03%|0,02%|0,02%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,00%|0,02%|<0,01%|<0,01%|
|R19|0,44%|0,08%|0,06%|0,05%|0,04%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,01%|0,03%|<0,01%|<0,01%|
|R20|0,24%|0,06%|0,06%|0,04%|0,04%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,01%|0,04%|<0,01%|<0,01%|
|R21|0,46%|0,09%|0,07%|0,05%|0,04%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,01%|0,05%|<0,01%|<0,01%|
|SINCA_LOS_AND<br>ES|0,00%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _67/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Tabla N° 29**_
_**Porcentaje de aporte según normativa en puntos de interés, con incertidumbre**_

|Col1|Col2|Col3|Col4|Col5|Col6|Fase de Cierre|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor de**<br>**Interés**|~~**MPS**~~<br>**mg/m2d **|~~**MP**~~**10** <br>**μg/m3 **|~~**MP**~~**10** <br>**μg/m3 **|~~**MP**~~**2,5** <br>**μg/m3 **|~~**MP**~~**2,5** <br>**μg/m3 **|~~**SO**~~**2** <br>**μg/m3 **|~~**SO**~~**2** <br>**μg/m3 **|~~**SO**~~**2** <br>**μg/m3 **|~~**SO**~~**2** <br>**μg/m3 **|~~**SO**~~**2** <br>**μg/m3 **|~~**SO**~~**2** <br>**μg/m3 **|~~**NO**~~**2** <br>**μg/m3 **|~~**NO**~~**2** <br>**μg/m3 **|~~**CO**~~<br>**μg/m3 **|~~**CO**~~<br>**μg/m3 **||
|**Receptor de**<br>**Interés**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Secundaria**|**Secundaria**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|
|**Receptor de**<br>**Interés**|**Media Anual**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P99**<br>**Diario**|**P98,5**<br>**Hr**|**Media**<br>**Anual**|**P99,7**<br>**Diario**|**P99,7**<br>**3 Hr**|**Media**<br>**Anual**|**P99H**|**P99**<br>**8 hrs**|**P99**<br>**Hr**|**P99**<br>**Hr**|
|R1_OLOR|0,02%|0,05%|0,05%|0,07%|0,08%|0,03%|0,05%|0,05%|0,03%|0,02%|0,05%|0,18%|1,53%|0,01%|0,01%|0,01%|
|R2_OLOR|0,02%|0,02%|0,02%|0,03%|0,04%|0,01%|0,02%|0,02%|0,01%|0,01%|0,02%|0,08%|1,19%|0,01%|0,00%|0,00%|
|R3_OLOR|0,01%|0,01%|0,04%|0,02%|0,06%|0,01%|0,04%|0,02%|0,01%|0,03%|0,02%|0,04%|1,49%|0,01%|0,01%|0,01%|
|R4_OLOR|0,01%|0,02%|0,05%|0,03%|0,08%|0,01%|0,07%|0,02%|0,01%|0,04%|0,04%|0,06%|3,25%|0,02%|0,01%|0,01%|
|R5_OLOR|0,01%|0,01%|0,01%|0,01%|0,02%|0,00%|0,01%|0,01%|0,00%|0,01%|0,01%|0,03%|0,72%|<0,01%|<0,01%|<0,01%|
|R6_OLOR|0,01%|0,04%|0,07%|0,06%|0,11%|0,02%|0,05%|0,07%|0,02%|0,02%|0,05%|0,15%|2,45%|0,01%|0,01%|0,01%|
|R1_RUIDO|0,02%|0,05%|0,05%|0,07%|0,07%|0,03%|0,04%|0,05%|0,02%|0,02%|0,03%|0,16%|1,40%|0,01%|<0,01%|<0,01%|
|R2_RUIDO|0,02%|0,02%|0,02%|0,03%|0,04%|0,01%|0,02%|0,02%|0,01%|0,01%|0,02%|0,09%|1,14%|0,01%|<0,01%|<0,01%|
|R3_RUIDO|<0,01%|0,01%|0,02%|0,01%|0,04%|0,00%|0,02%|0,01%|0,00%|0,01%|0,02%|0,03%|1,37%|0,01%|<0,01%|<0,01%|
|R4_RUIDO|<0,01%|0,01%|0,02%|0,01%|0,04%|0,00%|0,02%|0,01%|0,00%|0,02%|0,02%|0,03%|1,05%|0,01%|<0,01%|<0,01%|
|R5_RUIDO|0,01%|0,04%|0,07%|0,05%|0,11%|0,02%|0,05%|0,07%|0,02%|0,02%|0,05%|0,15%|3,10%|0,01%|0,01%|0,01%|
|R6_RUIDO|0,01%|0,01%|0,04%|0,02%|0,06%|0,01%|0,04%|0,02%|0,01%|0,02%|0,03%|0,04%|1,45%|0,02%|0,01%|0,01%|
|R7|0,00%|0,01%|0,03%|0,02%|0,05%|0,01%|0,01%|0,02%|0,00%|0,01%|0,01%|0,08%|1,79%|0,00%|<0,01%|<0,01%|
|R8|0,01%|0,02%|0,03%|0,03%|0,05%|0,01%|0,02%|0,02%|0,01%|0,01%|0,02%|0,11%|1,53%|0,01%|<0,01%|<0,01%|
|R9|0,05%|0,01%|0,01%|0,02%|0,02%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,03%|0,66%|<0,01%|<0,01%|<0,01%|
|R10|0,03%|0,01%|0,01%|0,01%|0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,02%|0,25%|<0,01%|<0,01%|<0,01%|
|R11|0,08%|0,01%|0,01%|0,01%|0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,01%|0,10%|<0,01%|<0,01%|<0,01%|
|R12|0,06%|0,01%|0,01%|0,01%|0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,01%|0,07%|<0,01%|<0,01%|<0,01%|
|R13|0,01%|<0,01%|<0,01%|<0,01%|0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,00%|0,04%|<0,01%|<0,01%|<0,01%|

_**Modelación de Emisiones ATM064-22**_ _68/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

|Receptor de<br>Interés|MPS<br>mg/m2d|MP<br>10<br>μg/m3|Col4|MP<br>2,5<br>μg/m3|Col6|SO<br>2<br>μg/m3|Col8|Col9|Col10|Col11|Col12|NO<br>2<br>μg/m3|Col14|CO<br>μg/m3|Col16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor de**<br>**Interés**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Secundaria**|**Secundaria**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|
|**Receptor de**<br>**Interés**|**Media Anual**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P99**<br>**Diario**|**P98,5**<br>**Hr**|**Media**<br>**Anual**|**P99,7**<br>**Diario**|**P99,7**<br>**3 Hr**|**Media**<br>**Anual**|**P99H**|**P99**<br>**8 hrs**|**P99**<br>**Hr**|
|R14|0,01%|0,01%|0,01%|0,01%|0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,03%|<0,01%|<0,01%|
|R15|0,04%|0,01%|0,02%|0,01%|0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,03%|<0,01%|<0,01%|
|R16|0,01%|0,01%|0,01%|0,01%|0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,02%|<0,01%|<0,01%|
|R17|0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,01%|<0,01%|<0,01%|
|R18|0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,01%|<0,01%|<0,01%|
|R19|0,03%|0,01%|<0,01%|0,01%|0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,01%|<0,01%|<0,01%|
|R20|0,02%|0,01%|<0,01%|0,01%|0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,01%|<0,01%|<0,01%|
|R21|0,03%|0,01%|0,01%|0,01%|0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,01%|<0,01%|<0,01%|
|SINCA_LOS_AND<br>ES|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,01%|<0,01%|<0,01%|

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _69/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

**8.6** **Mapas de Isoconcentraciones**

A continuación, se presentan las isolíneas de concentración de MP 10, MP 2,5, MPS,
NO 2, CO y SO 2, correspondiente a la fase de construcción, operación y cierre.

_**Modelación de Emisiones ATM064-22**_ _70/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 23**_
_**Percentil 98 Promedio Diario de MP**_ _**10**_ _**, Fase Construcción**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _71/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 24**_
_**Promedio del Período de MP**_ _**10**_ _**, Fase Construcción**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _72/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 25**_
_**Percentil 98 Promedio Diario de MP**_ _**2,5**_ _**, Fase Construcción**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _73/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 26**_
_**Promedio del Período de MP**_ _**2,5**_ _**, Fase Construcción**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _74/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 27**_
_**Promedio del Período de MPS, Fase Construcción**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _75/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 28**_
_**Percentil 98,5 Promedio Horario de SO**_ _**2**_ _**, Fase Construcción**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _76/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 29**_
_**Percentil 99 Promedio Diario de SO**_ _**2**_ _**, Fase Construcción**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _77/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 30**_
_**Percentil 99,7 Promedio Diario de SO**_ _**2**_ _**, Fase Construcción**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _78/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 31**_
_**Percentil 99,73 Promedio Horario de SO**_ _**2**_ _**, Fase Construcción**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _79/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 32**_
_**Promedio del Período de SO**_ _**2**_ _**, Fase Construcción**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _80/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 33**_
_**Percentil 99 Máximo Horario de NO**_ _**2**_ _**, Fase Construcción**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _81/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 34**_
_**Promedio del Período de NO**_ _**2**_ _**, Fase Construcción**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _82/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 35**_
_**Percentil 99 Máximo Horario de CO, Fase Construcción**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _83/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 36**_
_**Percentil 99 Máximo 8 Horas de CO, Fase Construcción**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _84/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 37**_
_**Percentil 98 Promedio Diario de MP**_ _**10**_ _**, Fase Operación**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _85/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 38**_
_**Promedio del Período de MP**_ _**10**_ _**, Fase Operación**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _86/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 39**_
_**Percentil 98 Promedio Diario de MP**_ _**2,5**_ _**, Fase Operación**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _87/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 40**_
_**Promedio del Período de MP**_ _**2,5**_ _**, Fase Operación**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _88/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 41**_
_**Promedio del Período de MPS, Fase Operación**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _89/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 42**_
_**Percentil 98,5 Promedio Horario de SO**_ _**2**_ _**, Fase Operación**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _90/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 43**_
_**Percentil 99 Promedio Diario de SO**_ _**2**_ _**, Fase Operación**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _91/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 44**_
_**Percentil 99,7 Promedio Diario de SO**_ _**2**_ _**, Fase Operación**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _92/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 45**_
_**Percentil 99,73 Promedio Horario de SO**_ _**2**_ _**, Fase Operación**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _93/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 46**_
_**Promedio del Período de SO**_ _**2**_ _**, Fase Operación**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _94/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 47**_
_**Percentil 99 Máximo Horario de NO**_ _**2**_ _**, Fase Operación**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _95/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 48**_
_**Promedio del Período de NO**_ _**2**_ _**, Fase Operación**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _96/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 49**_
_**Percentil 99 Máximo Horario de CO, Fase Operación**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _97/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 50**_
_**Percentil 99 Máximo 8 Horas de CO, Fase Operación**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _98/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 51**_
_**Percentil 98 Promedio Diario de MP**_ _**10**_ _**, Fase Cierre**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _99/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 52**_
_**Promedio del Período de MP**_ _**10**_ _**, Fase Cierre**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _100/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 53**_
_**Percentil 98 Promedio Diario de MP**_ _**2,5**_ _**, Fase Cierre**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _101/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 54**_
_**Promedio del Período de MP**_ _**2,5**_ _**, Fase Cierre**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _102/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 55**_
_**Promedio del Período de MPS, Fase Cierre**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _103/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 56**_
_**Percentil 98,5 Promedio Horario de SO**_ _**2**_ _**, Fase Cierre**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _104/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 57**_
_**Percentil 99 Promedio Diario de SO**_ _**2**_ _**, Fase Cierre**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _105/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 58**_
_**Percentil 99,7 Promedio Diario de SO**_ _**2**_ _**, Fase Cierre**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _106/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 59**_
_**Percentil 99,73 Promedio Horario de SO**_ _**2**_ _**, Fase Cierre**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _107/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 60**_
_**Promedio del Período de SO**_ _**2**_ _**, Fase Cierre**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _108/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 61**_
_**Percentil 99 Máximo Horario de NO**_ _**2**_ _**, Fase Cierre**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _109/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 62**_
_**Promedio del Período de NO**_ _**2**_ _**, Fase Cierre**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _110/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 63**_
_**Percentil 99 Máximo Horario de CO, Fase Cierre**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _111/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

_**Figura N° 64**_
_**Percentil 99 Máximo 8 Horas de CO, Fase Cierre**_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _112/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

**9** **Área de Influencia**

El área de influencia para el componente calidad del aire se ha determinado sobre la base
del área o espacio geográfico de donde se obtuvo la información para predecir y evaluar
los impactos en los elementos del medio ambiente. Para ello, se consideraron las isolíneas
de las concentraciones de MPS que se alcanzarán productos de las partes, obras y acciones
del Proyecto realizadas durante la fase de construcción (corresponde a la fase de mayor
emisión de material particulado).

En tal sentido, el área de influencia se encuentra dada por las isolíneas de las
concentraciones obtenidas por las emisiones de MPS del Proyecto, dado que representan
una mayor extensión de superficie que las isolíneas de las concentraciones del resto de los
contaminantes, permitiendo de esta forma evaluar los impactos de todos los
contaminantes, referidos a calidad del aire, generados por las partes, obras y acciones del
Proyecto, teniendo en consideración los valores límites de concentración que se establecen
en las normas primarias de calidad del aire y/o de referencia.

De acuerdo con lo anterior, el área de influencia para calidad del aire corresponde a las
isolíneas de concentración de MPS, tal como se muestra en la siguiente figura.

_**Figura N° 65**_
_**Área de Influencia**_

_**Modelación de Emisiones ATM064-22**_ _113/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

Fuente: Algoritmos SpA, 2023

_**Modelación de Emisiones ATM064-22**_ _114/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_

**10** **Conclusiones**

De los resultados obtenidos de la modelación, los aportes del Proyecto Planta
Jucosol, en los puntos de interés son los siguientes:

 El aporte del proyecto en los puntos de interés para la fase de construcción
para el material particulado resulta ser menor al 0,17%, 0,13% y 0,22% de
la norma para todos los estadísticos de MP2,5, MP10 y MPS respectivamente;
con respecto a los gases SO2, NOx CO, los aportes del proyecto son menores
al 3,78% de la norma en todos sus estadísticos. Ahora bien, para la fase
operación se desprende que para el material particulado los aportes son del
0,14 %, 0,21% y 1,1% de la norma para todos los estadísticos de MP2,5,
MP10 y MPS respectivamente; para los gases SO2, NOx y CO, se tiene que
los aportes con respecto a la norma no supera el 0,07% en todos sus
estadísticos. Respecto a cierre ningún contaminante supera los límites
normativos al igual que construcción y operación.

 Al analizar los resultados de la modelación del proyecto en estudio en las
estaciones de monitoreo y línea de base, se obtiene para la fase de
construcción que en la estación Los Andes se tiene que el aporte del NO 2 es
del 24 y 26%% de la norma para los estadísticos promedio del período y
percentil 99 horario para todas las fases modeladas.

 Las isoconcentraciones obtenidas muestran que, en la fase de construcción
y operación, los contaminantes tienen una dispersión local, donde existe una
leve dispersión al este y sureste del proyecto, debido a la dirección del viento
de la zona y las fuentes tipo caminos que van hacia esa dirección.

_**Modelación de Emisiones ATM064-22**_ _115/114_
_Proyecto Planta Jucosol_

_Mayo, 2023_