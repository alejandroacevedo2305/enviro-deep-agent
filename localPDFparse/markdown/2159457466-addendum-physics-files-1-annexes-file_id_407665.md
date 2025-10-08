---
title: Sin título
author: Desconocido
date: D:20231020214202Z00'00'
language: es
type: report
pages: 62
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ADENDA PARQUE FOTOVOLTAICO JOSÉ SOLAR ANEXO 3.3 MODELACIÓN DE LA DISPERSIÓN ATMOSFÉRICA
-->

# ADENDA PARQUE FOTOVOLTAICO JOSÉ SOLAR ANEXO 3.3 MODELACIÓN DE LA DISPERSIÓN ATMOSFÉRICA

Elaborado por

|Col1|ANEXOS|TEBAL-DOC-032|
|---|---|---|
|<br>|**ANEXOS**|**VER 00**|
|<br>|**ANEXOS**|**Noviembre 2020**|
|AREA:<br>GERENCIA<br>ESTUDIOS<br>Y <br>DESARROLLO / OPERACIONES|RESPONSABLE: GERENTE GENERAL FECHA ACTUALIZACION: 000000|RESPONSABLE: GERENTE GENERAL FECHA ACTUALIZACION: 000000|

Documento preparado por: TEBAL, Estudios e ingeniería ambiental

Andrés de Fuenzalida 17, Oficina 34, Providencia, Santiago de Chile

Teléfono +56 2 2222 7059

Email info@Tebal.cl

Website [www.Tebal.cl](http://www.tebal.cl/)

#### REGISTRO DE CONTROL DE DOCUMENTO

|ANEXO 3.3: MODELACIÓN DE LA DISPERSIÓN ATMOSFÉRICA|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Versión**|**Elaboración y**<br>**Fecha**|**Firma**|**Revisión y**<br>**Fecha**|**Firma**|**Aprobación**<br>**TEBAL y**<br>**Fecha**|**Firma**|**Aprobación**<br>**Cliente y**<br>**Fecha**|**Firma**|
|00|EA<br>13-06-2023||JLR<br>14-06-2023||-|-|VMC<br>16-06-2023||
|01|SC<br>20-10-2023||JLR<br>20-10-2023||||||

## ÍNDICE DE CONTENIDOS

1 INTRODUCCIÓN .......................................................................................................................... 1

1.1 OBJETIVO GENERAL ..................................................................................................................... 4

1.2 ANTECEDENTES GENERALES DEL PROYECTO .............................................................................. 4

1.2.1 DESCRIPCIÓN ..................................................................................................................... 4

1.2.2 LOCALIZACIÓN ................................................................................................................... 4

1.3 MARCO LEGAL ............................................................................................................................. 5

1.4 METEOROLOGÍA DE LA ZONA DE ESTUDIO ................................................................................. 7

1.4.1 Velocidad y Dirección del Viento ....................................................................................... 8

1.4.1.1 Series De Tiempo ............................................................................................................... 8

1.4.1.2 Rosas De Viento ................................................................................................................ 9

1.4.1.3 Ciclo Estacional ................................................................................................................ 12

1.4.1.4 Ciclo Diario Velocidad Del Viento .................................................................................... 13

1.4.2 Temperatura ................................................................................................................... 15

1.4.2.1 Series De Tiempo ............................................................................................................. 15

1.4.2.2 Ciclo Estacional ................................................................................................................ 16

1.4.2.3 Ciclo Diario Velocidad Del Viento .................................................................................... 17

1.4.3 ANÁLISIS DE INCERTIDUMBRE ......................................................................................... 18

1.4.3.1 Sesgo ............................................................................................................................... 18

1.4.3.2 Error Absoluto Medio (MAE) ........................................................................................... 18

1.4.3.3 Raíz del Error Cuadrático Medio ..................................................................................... 18

1.5 MODELACIÓN DE DISPERSIÓN DE CONSTAMINANTES ............................................................. 20

1.5.1 Emisiones del Escenario Modelado ................................................................................. 20

1.5.2 Modelo de Dispersión Atmosférica ................................................................................. 21

1.5.2.1 Base Teórica .................................................................................................................... 21

1.5.2.2 Sistema de Modelación WRF - CALPUFF ......................................................................... 21

1.5.2.3 Variables de Entrada ingresadas al Sistema de Modelación ........................................... 23

1.5.3 RESULTADOS DE LA MODELACIÓN .................................................................................. 28

1.5.3.1 Aportes en Puntos de Máxima Concentración ................................................................ 31

1.5.4 Escenario Sinérgico ......................................................................................................... 33

1.5.1 Análisis de Cumplimiento de Normativa Ambiental ....................................................... 35

1.5.2 Mapas de Isoconcentraciones ......................................................................................... 38
1.5.3 Definición del Área de Influencia de la Componente Aire. ............................................. 54

2 CONCLUSIONES ......................................................................................................................... 56

## INDICE DE FIGURAS

Figura 1. Ubicación del Proyecto y Área de Modelación (Área de Estudio). ...................................... 3

i

Figura 2. Ubicación del Proyecto. ....................................................................................................... 5
Figura 3. Serie de tiempo observada y modelada velocidad del viento - Estación Rayentué Periodo
1 enero - 31 diciembre 2021 .............................................................................................................. 8

Figura 4. Serie de tiempo observada y modelada dirección del viento - Estación Rayentué Periodo 1

enero - 31 diciembre 2021 ................................................................................................................. 9

Figura 5. Rosa de Viento Ciclo Completo - Estación Rayentué Periodo 01 enero - 31 diciembre 2021

.......................................................................................................................................................... 10

Figura 6. Variabilidad temporal del viento observada y modelada - Estación Rayentué Periodo 1

enero - 31 diciembre 2021 ............................................................................................................... 11

Figura 7. Ciclo estacional del viento observado y modelado - Estación Rayentué Periodo 1 enero31 diciembre 2021 ............................................................................................................................ 12

Figura 8. Ciclo diario de la velocidad del viento observada y modelada- Estación Rayentué Periodo 1

enero - 31 diciembre 2021 ............................................................................................................... 13

Figura 9. Ciclo diario de la dirección del viento observada y modelada- Estación Rayentué Periodo

01 enero- 31 diciembre 2021 ........................................................................................................... 14

Figura 10. Serie de tiempo observada y modelada temperatura - Estación Rayentué Periodo 01

enero- 31 diciembre 2021 ................................................................................................................ 15

Figura 11. Ciclo estacional de la temperatura observada y modelada - Estación Rayentué Periodo 01

enero- 31 diciembre 2021 ................................................................................................................ 16

Figura 12. Ciclo diario de la temperatura observada y modelada- Estación Rayentué Periodo 01

enero- 31 diciembre 2021 ................................................................................................................ 17

Figura 13. Uso de Suelo. ................................................................................................................... 24
Figura 14. Ubicación Puntos de Interés. ........................................................................................... 26
Figura 15. Topografía del Área de Modelación. ................................................................................ 27
Figura 16. Ubicación de Puntos de Máxima Concentración, Peor Escenario. .................................. 32
Figura 17. Percentil 98 Promedio Diario de MP 10 . ............................................................................ 39
Figura 18. Promedio del Período de MP 10 . ....................................................................................... 40
Figura 19. Percentil 98 Promedio Diario de MP 2,5 . ........................................................................... 41
Figura 20. Promedio del Período de MP 2,5 . ....................................................................................... 42
Figura 21. Promedio del Período de MPS. ........................................................................................ 43
Figura 22. Promedio Mensual de MPS. ............................................................................................. 44
Figura 23. Percentil 98,5 Promedio Horario de SO 2 . ......................................................................... 45
Figura 24. Percentil 99 Promedio Diario de SO 2 . .............................................................................. 46
Figura 25. Percentil 99,7 Promedio Diario de SO 2 . ........................................................................... 47
Figura 26. Percentil 99,73 Promedio Horario de SO 2 . ....................................................................... 48
Figura 27. Promedio del Período de SO 2 . .......................................................................................... 49
Figura 28. Percentil 99 Máximo Horario de NO 2 . ............................................................................. 50
Figura 29. Promedio del Período de NO 2 . ......................................................................................... 51
Figura 30. Percentil 99 Máximo Horario de CO. ............................................................................... 52
Figura 31. Área de Influencia Componente Aire ............................................................................... 55

## INDICE DE TABLAS

Tabla 1. Coordenadas Vértices del Área de Modelación del Proyecto (Área de Estudio). ................. 1

Tabla 2. Normativa de Calidad del Aire Consideradas en el Estudio. ................................................. 5

Tabla 3 Localización de Referencia y Variables Meteorológicas Monitoreadas ................................. 7
Tabla 4 Estadísticas de Datos Meteorológicos Monitoreados ............................................................ 8

ii

Tabla 5. Estadísticas de Datos de Temperatura ................................................................................ 15
Tabla 6. Valor de Incertidumbre Variables Meteorológicas ............................................................. 19
Tabla 7. Emisiones del Proyecto Peor escenario Fase de Construcción. .......................................... 20

Tabla 8. Características Uso de Suelo. .............................................................................................. 23

Tabla 9. Localización Puntos Discretos. ............................................................................................ 25

Tabla 10. Aportes del Proyecto en Puntos de Interés de Material Particulado, Peor Escenario. ..... 29

<!-- INICIO TABLA 10 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- En esta sección se presentan los aportes obtenidos por la modelación del escenario más desfavorable del Proyecto en los puntos de interés poblacional y de recursos naturales (receptores discretos). En la -->

**Tabla 10: y Tabla 11 se muestran los aportes del proyecto en cada uno de los receptores de interés.**

| ID | PUNTOS DE INTERÉS | MP (μg/m3)<br>10 | Col4 | MP (μg/m3)<br>2,5 | Col6 | MPS (mg/m2día) | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **ID** | **PUNTOS DE INTERÉS** | **Primaria** | **Primaria** | **Primaria** | **Primaria** | **Secundaria** | **Secundaria** |
| **ID** | **PUNTOS DE INTERÉS** | **Media Anual** | **P98 Diario** | **Media Anual** | **P98 Diario** | **Media Anual** | **Media**<br>**Mensual** |
| R1 | Vivienda habitacional de un (1) piso, aledaña a ruta H-432 | 0,4445 | 2,1499 | 0,1353 | 0,6559 | 0,0065 | 0,0152 |
| R2 | Vivienda habitacional de un (1) piso, aledaña a ruta H-432 y el<br>“Camino a Santa Lucila” | 0,4124 | 2,0318 | 0,1255 | 0,6200 | 0,0061 | 0,0149 |
| R3 | Vivienda habitacional de un (1) piso, ubicada al norte del<br>Proyecto | 1,5957 | 5,2449 | 0,4840 | 1,5959 | 0,0290 | 0,0729 |
| R4 | Vivienda habitacional de dos pisos, ubicada dentro de agrícola,<br>al oeste del Proyecto<br> | 0,3588 | 1,8573 | 0,1076 | 0,5628 | 0,0069 | 0,0177 |
| R5 | ~~Oficina de administración (un piso) ubicada dentro de Agrícola~~<br>Santa Lucila LTDA | 0,3951 | 1,9602 | 0,1188 | 0,5955 | 0,0067 | 0,0177 |
| R6 | Vivienda Patronal de dos pisos, ubicada al oeste del Proyecto | 0,2764 | 1,3657 | 0,0821 | 0,4141 | 0,0054 | 0,0130 |
| R7 | Vivienda habitacional de un (1) piso, ubicada al oeste del<br>Proyecto | 0,1969 | 0,8991 | 0,0579 | 0,2726 | 0,0042 | 0,0076 |
| R8 | Vivienda habitacional de un (1) piso, ubicada al oeste del<br>Proyecto | 0,1886 | 0,9017 | 0,0552 | 0,2733 | 0,0042 | 0,0076 |
| R9 | Vivienda habitacional de un (1) piso, ubicada al norte de la Área<br>B del Proyecto | 0,1299 | 0,6198 | 0,0379 | 0,1858 | 0,0029 | 0,0056 |
| R10 | Vivienda habitacional de un (1) piso, localizada a un costado de<br>la Ruta H-418, al oeste del Proyecto | 0,2545 | 1,3482 | 0,0745 | 0,4052 | 0,0061 | 0,0145 |

<!-- Estadísticas: 12 filas, 8 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. **Tabla 11. Aportes del Proyecto en Puntos de Interés de Gases, Peor Escenario.** -->
<!-- FIN TABLA 10 -->

Tabla 11. Aportes del Proyecto en Puntos de Interés de Gases, Peor Escenario. ............................ 29
Tabla 12. Puntos de Máxima Concentración (PMC), Peor Escenario. ............................................... 31
Tabla 13. Cronograma Sinérgico. ...................................................................................................... 33
Tabla 14. Aportes Escenario sinérgico en Puntos de Interés de Material Particulado. .................... 34
Tabla 15. Aportes Escenario sinérgico en Puntos de Interés de Gases. ............................................ 34
Tabla 16. Análisis de Cumplimiento de Normativa Escenario sinérgico en Puntos de Interés de

Material Particulado. ........................................................................................................................ 36

Tabla 17. Análisis de Cumplimiento de Normativa Aportes Escenario sinérgico en Puntos de Interés

de Gases. .......................................................................................................................................... 37

Tabla 18 Límites normativos considerados para determinar el área de Influencia del Proyecto

54

## ÍNDICE DE TABLAS

Apéndice 2.17.1 - Archivos modelación CALPUFF y WRF

iii

### 1 INTRODUCCIÓN

En este Anexo se presentan los resultados de las concentraciones obtenidas al modelar la dispersión

atmosférica de material particulado sedimentable (MPS), material particulado respirable (MP10 y

MP2,5), dióxido de azufre (SO2), dióxido de nitrógeno (NO2) y monóxido de carbono (CO), para el

escenario anual de emisiones más desfavorable, el cual corresponde la fase de construcción del

proyecto “Fotovoltaico José Solar”, en adelante “el Proyecto”.

Se determinó que la fase de construcción, que tiene una duración de 6 meses, es el escenario para

modelar más desfavorable posible. Con el objetivo de realizar un análisis conservador se modeló un

año calendario con las emisiones de la fase de construcción constante los 365 días. Esto de acuerdo

con los resultados presentados en el Anexo 3.3 Estimación de Emisiones Atmosféricas de la DIA,

donde se muestra que durante la fase de construcción y cierre se desarrollarían los escenarios más

desfavorables en términos de calidad del aire para gases y material particulado, considerándose la

fase de construcción la fase más desfavorable en términos magnitud de emisiones y su distribución

espacial dada la cobertura que alcanzarían las diversas actividades emisivas.

La modelación de dispersión de material particulado y de gases asociados al Proyecto y que se

presenta a continuación fue desarrollada según los requerimientos de la “Guía para el Uso de

Modelos de Calidad del Aire en el SEIA, segunda edición 2023” del Servicio de Evaluación Ambiental.

Esta Guía indica como opción la aplicación del sistema de modelación atmosférica “WRFCALPUFF”, sistema de modelación que a su vez está definido por la agencia EPA como sistema de

referencia para simular la dispersión de contaminantes provenientes de centros industriales

ubicados en terreno complejo.

La meteorología utilizada en el sistema de modelación se obtuvo por medio del modelo

meteorológico de pronóstico _Weather Research and Forecasting Model_ (WRF), con todos los

parámetros indicados en la “Guía para el Uso de Modelos de Calidad del Aire en el SEIA, segunda

edición 2023”.

La modelación meteorológica realizada con el modelo WRF corresponde al año 2021. Esta

modelación tiene un área de dominio de 75 x 75 km, una resolución de espaciamiento de 1 km, y en

cuyo interior se encuentra ubicado el área de modelación CALPUFF, el sitio de emplazamiento del

Proyecto y los puntos de interés, como se observa en la Figura 1.

La Tabla 1 muestra las coordenadas de los vértices del área de modelación WRF.

**Tabla 1. Coordenadas Vértices del Área de Modelación del Proyecto (Área de Estudio).**

|VÉRTICE|COORDENADAS UTM (DATUM WGS-84 HUSO 18S)|Col3|
|---|---|---|
|**VÉRTICE**|**NORTE (M)**|**ESTE (M)**|
|Noreste|6229108,759|364359,059|
|Noroeste|6227683,765|287194,625|
|Suroeste|6150856,023|288624,816|

1

|VÉRTICE|COORDENADAS UTM (DATUM WGS-84 HUSO 18S)|Col3|
|---|---|---|
|**VÉRTICE**|**NORTE (M)**|**ESTE (M)**|
|Sureste <br>|6152306,420<br>|365791,273|

Fuente: Elaboración propia.

2

**Figura 1. Ubicación del Proyecto y Área de Modelación (Área de Estudio).**

Fuente: Elaboración propia.

3

#### 1.1 OBJETIVO GENERAL

Cuantificar los aportes en concentración e isoconcentraciones de SO2, NO2, CO, MPS, MP10 y MP2,5

con el sistema de modelación WRF-CALPUFF, en cada punto de interés ingresados al modelo de

dispersión de emisiones del escenario más desfavorable del Proyecto y determinar el cumplimiento

normativo de la calidad del aire por medio de la comparación de los niveles de concentración obtenidos

con los límites de la normativa ambiental vigente.

#### 1.2 ANTECEDENTES GENERALES DEL PROYECTO

**1.2.1** **DESCRIPCIÓN**

El Proyecto contempla la construcción y operación de un Parque Solar Fotovoltaico para generación de

energía eléctrica, constituido por un total de 16.980 módulos fotovoltaicos bifaciales monocristalinos

de 650 watts, que en conjunto tendrán una potencia máxima instalada de 11,0 MWp y una potencia

nominal de 9 MWac que serán inyectados al Sistema Eléctrico Nacional (SEN).

**1.2.2** **LOCALIZACIÓN**

El Proyecto se emplazará en la Región del Libertador General Bernardo O’Higgins, en la Provincia del

Cachapoal, específicamente en la comuna de Requínoa, a aproximadamente 1.077 m del límite urbano

de la localidad de El Abra.

4

**Figura 2. Ubicación del Proyecto.**

Fuente: Capitulo 1 Descripción del Proyecto.

#### 1.3 MARCO LEGAL

Para determinar el aporte del proyecto respecto de la normativa ambiental se consideraron las normas

primarias y secundarias de calidad del aire definidas en la legislación chilena.

La siguiente Tabla presenta los valores límites de referencia para el análisis del presente documento.

**Tabla 2. Normativa de Calidad del Aire Consideradas en el Estudio.**

|PARÁMETRO|TIPO DE NORMA|ESTADÍSTICO|VALOR|REFERENCIA|
|---|---|---|---|---|
|MPSa|Secundaria|Promedio del Periodo|100 mg/m2-día|D.S. N°04/92 MINAGRI|
|MPSa|Secundaria|Promedio Mensual|150 mg/m2-día|D.S. N°04/92 MINAGRI|
|MP10|Primaria|Promedio del periodo|50μg/m3N|D.S. N°45/02 MINSEGPRES|
|MP10|Primaria|Percentil 98 Diario|130μg/m3N|D.S. N°12/21 MMA|

a Norma de Referencia, ya que no existe una de cobertura nacional se utiliza de referencia una norma chilena local de la zona
de Huasco cuya finalidad es proteger los recursos silvoagropecuarios.

5

|PARÁMETRO|TIPO DE NORMA|ESTADÍSTICO|VALOR|REFERENCIA|
|---|---|---|---|---|
|MP2,5|Primaria|Promedio del Periodo|20μg/m3N|D.S. N°12/11 MMA|
|MP2,5|Primaria|Percentil 98 Diario|50μg/m3N|D.S. N°12/11 MMA|
|SO2|Primaria|Promedio del Periodo|60μg/m3N|D.S. N°104/18 MMA|
|SO2|Primaria|Percentil 99 Diario|150μg/m3N|D.S. N°104/18 MMA|
|SO2|Primaria|Percentil 98,5 Horario|350μg/m3N|D.S. N°104/18 MMA|
|SO2|Secundaria|Promedio del Periodo|80μg/m3N|D.S. N°22/10 MINSEGPRES|
|SO2|Secundaria|Percentil 99,7 Diario|365μg/m3N|D.S. N°22/10 MINSEGPRES|
|SO2|Secundaria|Percentil 99,73 Horario|1000μg/m3N|D.S. N°22/10 MINSEGPRES|
|NO2|Primaria|Promedio del Periodo|100μg/m3N|D.S. N°114/02 MINSEGPRES|
|NO2|Primaria|Percentil 99 Horario|400μg/m3N|D.S. N°114/02 MINSEGPRES|
|CO|Primaria|Percentil 99 8 horas|10.000μg/m3N|D.S. N°115/02 MINSEGPRES|
|CO|Primaria|Percentil 99 Horario|30.000μg/m3N|D.S. N°115/02 MINSEGPRES|

Fuente: Elaboración propia.

6

#### 1.4 METEOROLOGÍA DE LA ZONA DE ESTUDIO

La modelación atmosférica predice el estado del tiempo resolviendo mediante métodos numéricos las

ecuaciones matemáticas para la física y la dinámica de la atmósfera a partir de condiciones previas. De

esta manera, mediante el modelo meteorológico de pronóstico _Weather Research and Forecasting_

_Model_ (WRF) se han modelado y analizado las variables meteorológicas de mayor incidencia en la

dispersión de las emisiones generadas por el Proyecto.

El modelo WRF es un modelo de predicción numérica del tiempo diseñado para la investigación y para

aplicaciones operativas. Diversas instituciones han contribuido y siguen contribuyendo a su desarrollo,

con el firme objetivo de construir el modelo de pronóstico numérico de mesoescala de la siguiente

generación, para lograr un avance en el entendimiento de los procesos atmosféricos y en la predicción

de tiempo. Los principales componentes de este modelo son las fuentes externas de datos, como son

los datos de entrada y la información geográfica, el sistema de pre-procesamiento, el modelo WRF
ARW y los sistemas de post-procesamiento.

Las fuentes externas de datos contienen información necesaria para inicializar WRF. Éstos

corresponden a las observaciones convencionales o satélites de la atmósfera. De estos datos se

obtienen las condiciones iniciales y de borde para las simulaciones del WRF. También es necesario

entregarle datos sobre el terreno que contengan información sobre la orografía, uso de suelo, relieve

y vegetación, entre otros.

Este modelo se encuentra recomendado por la “Guía para el uso de modelos de calidad del aire en el

SEIA”, para la generación de datos meteorológicos, ya que, según indica, es uno de los modelos

meteorológicos de pronóstico más avanzados y completos, siendo empleado en la mayoría de los

proyectos relacionados con modelación atmosférica encargados por organismos estatales como el

Ministerio del Medio Ambiente (MMA) y la ex Comisión Nacional de Energía (CNE) (ahora Ministerio

de Energía).

Para generar la modelación meteorológica, se utilizan cuatro dominios anidados, donde cada celda es

de 27, 9, 3 y 1 kilómetros respectivamente, centrados en el Proyecto para un año calendario (2021) y

resolución horaria.

Dado que la meteorología la que media entre las emisiones y su impacto en los puntos receptores, se

realiza a continuación un análisis cualitativo y cuantitativo de la temperatura, velocidad y dirección del

viento observada y modelado, en la Estación Rayentué.

La Tabla 3 muestra la coordenada de localización, las variables analizadas en el presente estudio y el

periodo considerado.

**Tabla 3 Localización de Referencia y Variables Meteorológicas Monitoreadas**

|ESTACIÓN|COORDENADAS UTM<br>(DATUM WGS-84 HUSO 18S)|Col3|VARIABLES|PERIODO|
|---|---|---|---|---|
|**ESTACIÓN**|**NORTE (M)**|**ESTE (M)**|**ESTE (M)**|**ESTE (M)**|
|Rayentué|331.629.|6.200.845|Velocidad del viento<br>Dirección del viento<br>Temperatura|01 de enero al 31 de<br>diciembre 2021|

Fuente: Instituto de Investigaciones Agropecuarias (INIA).

7

**1.4.1** **Velocidad y Dirección del Viento**

**1.4.1.1** **Series De Tiempo**

La Tabla 4 muestra los porcentajes de calmas registrados por la Estación Rayentué. Cabe señalar que

se considera como calma los registros menores a 0,5 (m/s).

**Tabla 4. Estadísticas de Datos Meteorológicos Monitoreados.**

|ESTACIÓN|DATOS TOTALES|PORCENTAJE DE CALMA (%)|Col4|
|---|---|---|---|
|**ESTACIÓN**|**DATOS TOTALES**|**PERIODO DIURNO**|**PERIODO NOCTURNO**|
|Rayentué|8.760|100%|31%|

Fuente: Elaboración propia.

Para un análisis adecuado de las variables meteorológicas, de acuerdo con lo señalado en la “guía para

el uso de modelos de calidad del aire en el SEIA”, la serie de datos debe contener al menos un 75% de

datos válidos, para garantizar la calidad de un análisis de datos meteorológicos, lo que en este caso de

estudio se cumple para el periodo de estudio, ya que el registro con el que se cuenta en la Estación

Rayentué es de 100% de datos válidos.

La serie temporal de la velocidad del viento observada muestra un leve ciclo anual, registrando un

aumento de la velocidad entre octubre y diciembre, con valores que alcanzan los 3 m/s. El resto del

tiempo las velocidades varían en promedio en 2 m/s, con algunos eventos de mayor intensidad. Para

la serie modelada se observa un patrón similar, sin embargo, presenta una sobreestimación de la

velocidad del viento observada.

|OBSERVADO|Col2|
|---|---|
|**MODELADO**||

**Figura 3. Serie de tiempo observada y modelada velocidad del viento - Estación Rayentué**

**Periodo 1 enero - 31 diciembre 2021.**

Fuente: Elaboración propia.

8

Con respecto a la dirección del viento se observan un patrón dominante tanto en los datos observados
como modelados. Este patrón corresponde a vientos desde el Suroeste (S) correspondiendo a la línea
centrada entre 180 y 240°.

|OBSERVADO|Col2|
|---|---|
|**MODELADO**||

**Figura 4. Serie de tiempo observada y modelada dirección del viento - Estación Rayentué**

**Periodo 1 enero - 31 diciembre 2021**

Fuente: Elaboración propia

**1.4.1.2** **Rosas De Viento**

A continuación, se muestran los campos de viento anual y para diferentes periodos del día, los que

muestran la variabilidad temporal del viento modelado durante el periodo entre enero y diciembre de

2021 en la Estación Rayentué, indicando los porcentajes de frecuencia que el viento sopla en sus

diferentes direcciones.

9

|OBSERVADO|MODELADO|
|---|---|
|||

**Figura 5. Rosa de Viento Ciclo Completo - Estación Rayentué**

**Periodo 01 enero - 31 diciembre 2021**

Fuente: Elaboración propia

Observando el comportamiento desde las 00:00 a 23:00 horas, los registros muestran que la dirección

de máxima frecuencia corresponde por una parte a vientos procedentes desde Suroeste (SO) y Sur

Suroeste (SSO), explicando en conjunto un 75% de la frecuencia total. En relación con los datos

modelados, se observa el mismo patrón de vientos, sin embargo, se subestima la frecuencia de

ocurrencia de la componente Suroeste (SO) y sobrestiman los vientos desde Oeste Suroeste (OSO).

Al observar el comportamiento espacial de los vientos en los diferentes periodos del día, Figura 6, se

puede apreciar tanto en los datos observados como modelados un patrón dominante a lo largo del día

con vientos desde el Suroeste (SO) y Sur Suroeste (SSO) tanto en los datos observados como

modelados.

10

|OBSERVADO|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|**MODELADO**|||||

**Figura 6. Variabilidad temporal del viento observada y modelada - Estación Rayentué**

**Periodo 1 enero - 31 diciembre 2021**

Fuente: Elaboración propia.

11

**1.4.1.3** **Ciclo Estacional**

La Figura 7 muestra la evolución estacional y diaria de la velocidad y dirección del viento observado y

modelado en la Estación Rayentué, presentando en el eje “x” las horas del día y en el eje “y” los meses

del año. Es posible identificar un leve ciclo anual, con un aumento de la velocidad registrada entre los

meses de octubre y diciembre con valores que bordean 3 m/s entre las 13:00 y 17:00 horas. En relación

con los datos modelados, se observa este mismo aumento de la velocidad, sobrestimando este

aumento en 2 m/s aproximadamente.

En cuanto a la dirección del viento, se observa un patrón dominante tanto en los datos observados

como modelados, con vientos preferentemente desde el Suroeste (SO) y Oeste Suroeste (OSO).

|OBSERVADO|MODELADO|
|---|---|
|||

**Figura 7. Ciclo estacional del viento observado y modelado - Estación Rayentué**

**Periodo 1 enero - 31 diciembre 2021**

Fuente: Elaboración propia.

12

**1.4.1.4** **Ciclo Diario Velocidad Del Viento**

En la siguiente figura se presentan los ciclos diarios promedio de la velocidad del viento observado y

modelado en la Estación Rayentué.

Al apreciar la curva de velocidad promedio se puede observar un marcado ciclo diario, con los valores

mínimos presentados en el periodo nocturno con valores que se mantienen relativamente constantes

hasta las 06:00 horas donde la velocidad comienza a aumentar levemente hasta alcanzar el máximo

diario alrededor de las 15:00 horas con una magnitud promedio de 1,6 y 3,2 m/s, para los datos

observados y modelados, respectivamente.

|OBSERVADO|Col2|
|---|---|
|**MODELADO**||

**Figura 8. Ciclo diario de la velocidad del viento observada y modelada- Estación Rayentué**

**Periodo 1 enero - 31 diciembre 2021**

Fuente: Elaboración propia.

Respecto de la dirección del viento observada en Estación Rayentué se observan vientos con mayor

frecuencia desde el Suroeste (SO) y Sur Suroeste (SSO), variando su frecuencia de ocurrencia entre el

20 y 50%, tanto en los datos observados como modelados.

13

|OBSERVADO|Col2|
|---|---|
|**MODELADO**||

**Figura 9. Ciclo diario de la dirección del viento observada y modelada- Estación Rayentué**

**Periodo 01 enero- 31 diciembre 2021**

Fuente: Elaboración propia.

14

**1.4.2** **Temperatura**

**1.4.2.1** **Series De Tiempo**

La Tabla 5 muestra los porcentajes de datos disponibles para la variable temperatura en la Estación

Rayentué.

**Tabla 5. Estadísticas de Datos de Temperatura.**

|Estación|DATOS TOTALES|% DATOS TOTALES|
|---|---|---|
|Rayentué|8.760|100%|

Fuente: Elaboración propia.

La serie temporal de la temperatura registrada por la Estación Rayentué muestra un marcado ciclo

anual, disminuyendo la temperatura entre mayo y septiembre. Entre enero y abril y entre agosto y

diciembre la temperatura promedio varía en 20 °C, mientras que para el resto del periodo la

temperatura desciende alrededor de 10 °C, tanto en los datos observados como modelados.

|OBSERVADO|Col2|
|---|---|
|**MODELADO**||

**Figura 10. Serie de tiempo observada y modelada temperatura - Estación Rayentué**

**Periodo 01 enero- 31 diciembre 2021**

Fuente: Elaboración propia.

15

**1.4.2.2** **Ciclo Estacional**

La Figura 11 muestra la evolución estacional y diaria de la velocidad y dirección del viento observado y

modelado en la Estación Rayentué, presentando en el eje “x” las horas del día y en el eje “y” los meses

del año. Es posible observar un marcado ciclo estacional y diario, con los máximos valores registrados

entre enero y marzo y entre octubre y diciembre, entre las 10:00 y 21:00 horas, tanto en los datos

observados como modelados. Por otro lado, los mínimos valores se registran durante el periodo

invernal con valores de temperatura que rodean 10°C, tanto en los datos observados como modelados.

|OBSERVADO|MODELADO|
|---|---|
|||

**Figura 11. Ciclo estacional de la temperatura observada y modelada - Estación Rayentué**

**Periodo 01 enero- 31 diciembre 2021**

Fuente: Elaboración propia.

16

**1.4.2.3** **Ciclo Diario Velocidad Del Viento**

En la siguiente figura se presentan los ciclos diarios promedio de la temperatura observada y modelada

en la Estación Rayentué.

Al apreciar la curva promedio de temperatura se puede observar un marcado ciclo diario, con los

valores mínimos presentados en el periodo nocturno con valores que se mantienen relativamente

constantes hasta las 06:00 horas donde la temperatura comienza a aumentar hasta alcanzar el máximo

diario alrededor de las 16:00 horas con una magnitud promedio de 20°C, para los datos observados y

18°C para los datos modelados.

|OBSERVADO|Col2|
|---|---|
|**MODELADO**||

**Figura 12. Ciclo diario de la temperatura observada y modelada- Estación Rayentué**

**Periodo 01 enero- 31 diciembre 2021**

Fuente: Elaboración propia.

17

**1.4.3** **ANÁLISIS DE INCERTIDUMBRE**

Las variables meteorológicas de velocidad y dirección del viento son relevantes para el modelo debido

a que afectan de manera directa la forma en que se dispersan los contaminantes en la atmósfera. Por

esta razón es muy importante evaluar los errores entre los datos observados y modelados en forma

cualitativa y cuantitativa.

A continuación de acuerdo con lo recomendado por la Guía para el uso de modelos de calidad del aire

en el SEIA (segunda edición 2023) se presenta el análisis cuantitativo recomendado, donde se

presentan las métricas estadísticas del sesgo, error absoluto medio y la raíz del error cuadrático medio.

**1.4.3.1** **Sesgo**

Proporciona información sobre la tendencia del modelo a sobreestimar o subestimar una variable,

cuantificando el error sistemático del modelo.

"

SESGO= [1]

n [((S] [!]

!#$

**1.4.3.2** **Error Absoluto Medio (MAE)**

−O ! ) Ecuación 1

El error absoluto medio es el promedio del valor absoluto de la diferencia entre el pronóstico y la

observación donde N es el número total de comparaciones pronosticadas. Tomar el valor absoluto de

esta diferencia, fuerza a MAE a tener en cuento tanto errores positivos como negativos, así MAE hace

la medida del error total del modelo.

"

MAE= [1]

n [(|S] [!] [ −O] [!] [|]

!#$

**1.4.3.3** **Raíz del Error Cuadrático Medio**

Ecuación 2

La raíz del error cuadrático medio corresponde al cálculo de la raíz cuadrada del promedio de las

diferencias cuadradas de cada uno de los valores del pronóstico y la observación. Este cálculo permite

ponderar los errores positivos y negativos, por lo cual en él están incluidos los errores sistemáticos y

aleatorios de los modelos.

RMSE=

n

~~0~~ [1]

!#$

18

"

n [((S] [!] [ −O] [!] [)] [%]

Ecuación 3

El cuadrado de esta diferencia fuerza el RMSE para tener en cuenta tanto los errores positivos y

negativos, así el RMSE hace la medida del error total del modelo. La medida del error total incluye los

componentes sistemáticos y al azar, los cuales pueden separar usando medidas para el error

sistemático y el error al azar, tales como error de sesgo y desviación estándar.

Dónde:

n : Cantidad de datos

S : Valores obtenidos del modelo

O : Valores observados en estaciones meteorológicas

A continuación, se presentan los resultados obtenidos de los estadígrafos mencionados anteriormente

respecto a los datos monitoreados por la estación Los Despachos comparados con los recomendados

en la “Guía para el uso de modelos de calidad del aire en el SEIA, segunda edición 2023”.

**Tabla 6. Valor de Incertidumbre Variables Meteorológicas**

|ESTADÍSTICO|VELOCIDAD DEL VIENTO|Col3|TEMPERATURA|Col5|
|---|---|---|---|---|
|**ESTADÍSTICO**|**VALOR**<br>**RECOMENDADO**|**RESULTADO DE**<br>**ESTACIÓN**|**VALOR**<br>**RECOMENDADO**|**RESULTADO DE**<br>**ESTACIÓN**|
|SESGO|[-2,5;2,5] (m/s)|1,14|[-4;4] (m/s)|-0,05|
|MAE|≤3 (m/s)|1,19|≤4 (m/s)|2,61|
|RMSE|≤3,5 (m/s)|1,46|≤4,5 (m/s)|3,29|
|CORR|>0,6|0,68|>0,8|0,92|

Fuente: Elaboración propia.

En base a lo anteriormente expuesto respecto de la meteorología, es posible concluir que el modelo

representa de manera satisfactoria la dinámica del viento y temperatura observada ya que este

reproduce tanto los ciclos diarios como estacionales, sin embargo, este sobrestima los valores de

velocidad y subestima la temperatura. En relación con los estadísticos evaluados, se obtiene valores

dentro de los parámetros recomendados.

19

#### 1.5 MODELACIÓN DE DISPERSIÓN DE CONTAMINANTES

**1.5.1** **Emisiones del Escenario Modelado**

Con el fin de evaluar la dispersión de los contaminantes generados por las fuentes, como material

particulado (MP10), material particulado respirable fino (MP2,5), material particulado sedimentable

(MPS), dióxido de azufre (SO2), óxidos de nitrógeno (NOX) y monóxido de carbono (CO) para escenario

más desfavorable, se realizó una modelación de dispersión de contaminantes considerando las

emisiones generadas por el Proyecto en el peor escenario.

Cabe señalar que durante el AÑO 1 se desarrollará la fase de construcción de duración 6 meses. De

acuerdo con lo presentado en el Anexo 2-16 Estimación de Emisiones Atmosféricas, Tabla 58 de

emisiones totales del Proyecto, la fase de construcción es el escenario más desfavorable en términos

de calidad del aire para gases y material particulado, cuyas emisiones consideradas en la modelación

se presentan a continuación:

**Tabla 7. Emisiones del Proyecto Peor escenario Fase de Construcción.**

|FUENTE|MP|MP10|MP2,5|NOX|SO2|NH3|CO|COV|UNIDAD|
|---|---|---|---|---|---|---|---|---|---|
|Escarpe|0,030|0,030|0,005|-|-|-|-|-|ton/año|
|Nivelación|0,006|0,004|0,000|-|-|-|-|-|ton/año|
|Compactación|0,013|0,003|0,001|-|-|-|-|-|ton/año|
|Excavación|0,073|0,017|0,008|-|-|-|-|-|ton/año|
|Carga/Descarga|0,001|0,000|0,000|-|-|-|-|-|ton/año|
|Transito camino no<br>pavimentado|0,719|0,138|0,033|-|-|-|-|-|ton/año|
|Transito camino<br>pavimentado|0,337|0,216|0,022|-|-|-|-|-|ton/año|
|Combustión<br>vehículos|0,005|0,005|0,005|0,234|0,000|0,000|0,058|0,010|ton/año|
|Combustión<br>maquinaría fuera<br>de ruta|0,010|0,010|0,010|0,230|0,005|0,001|1,208|0,072|ton/año|
|Grupo Electrógeno|0,041|0,041|0,014 <br>|0,590 <br>|0,039 <br>|-|0,127|0,048|**ton/año**|

Fuente: Elaboración propia.

Es importante mencionar que la modelación se realizó bajo las directrices establecidas en la “Guía para

el Uso de Modelos de Calidad del Aire en el SEIA, segunda edición 2023” del Servicio de Evaluación

Ambiental, que indica que se debe realizar la modelación bajo el peor escenario emisivo para un año

calendario meteorológico que cubra todas las variables estacionales climáticas que puedan afectar en

la dispersión de los contaminantes.

En el caso de la modelación, además se consideró que las actividades constructivas, de movimiento de

tierra y combustión de maquinarias se están desarrollando simultáneamente en toda la superficie a

construir del parque solar, es decir se distribuyeron espacialmente sus emisiones en todos los metros

cuadrados que cubren los paneles, caminos y el área de la línea de transmisión eléctrica. Además, en

20

el caso de las vías pavimentadas y no pavimentadas se distribuyeron las emisiones en todos los metros

cuadrados que cubren estas vías considerando las emisiones de todos los vehículos, es decir que la flota

completa circula al mismo tiempo por toda las vías simultáneamente durante **un año** con el fin de

representar y evaluar la peor condición, ya que esto no ocurrirá debido a que existe una secuencia en

las actividades según la carta Gantt y la fase tienen una duración de 6 meses, de esta manera

conservadora se cubren todos los posibles escenarios que podrían ocurrir.

**1.5.2** **Modelo de Dispersión Atmosférica**

**1.5.2.1** **Base Teórica**

La aplicación de modelos de dispersión atmosférica permite determinar el aporte de las emisiones

provenientes de fuentes emisoras, en localidades y sectores aledaños a las instalaciones de un

determinado proyecto, permitiendo de este modo, asignar las cuotas de responsabilidad en los niveles

de calidad del aire medidos en su entorno.

Los modelos lagrangianos se caracterizan por hacer uso de un sistema de referencia que se ajusta al

movimiento atmosférico. Es decir, las emisiones, reacciones, deposición y mezclado de los

contaminantes se analizan para un volumen de aire que va cambiando su posición, de acuerdo con la

velocidad y dirección del viento. Bajo este esquema general, los modelos lagrangianos se pueden

clasificar como modelos de trayectoria y modelos gaussianos, de acuerdo con la geometría del sistema

de modelación. Los modelos de trayectoria pueden simular los procesos para una columna hipotética

de aire, en cambio, cuando la simulación se hace para una pluma de emisión, continua o discreta, se

trata de modelos gaussianos.

Los modelos gaussianos describen el transporte y mezcla de los contaminantes, asumiendo que las

emisiones presentan, en las direcciones horizontal y vertical, una distribución normal o de curva

gaussiana con una concentración máxima en el centro de la pluma. Generalmente estos modelos se

aplican para evaluar la dispersión de contaminantes provenientes de fuentes puntuales, aunque

también se aplican para simular emisiones de fuentes de área y de línea. Otra característica de este

tipo de modelos es que normalmente son aplicados para evaluar la dispersión de contaminantes

primarios no reactivos, aunque existen versiones que incluyen en su formulación consideraciones

especiales para poder simular procesos de deposición y transformación química.

**1.5.2.2** **Sistema de Modelación WRF - CALPUFF**

Para determinar el efecto que tendrán las emisiones de material particulado y gases provenientes de

la construcción del Proyecto, se utiliza un sistema acoplado de dos modelos: El modelo atmosférico

Weather Research and Forecasting (WRF), y el modelo CALPUFF, simulador de la dispersión de

contaminantes en la atmósfera. Ambos conforman el sistema de modelación WRF-CALPUFF.

 - **WRF**

[WRF es un modelo numérico de pronóstico e investigación atmosférica, desarrollado por el Centro](https://es.wikipedia.org/wiki/Centro_Nacional_de_Investigaci%C3%B3n_Atmosf%C3%A9rica)

[Nacional para la investigación Atmosférica (NCAR) y los Centros Nacionales para la Predicción](https://es.wikipedia.org/wiki/Centro_Nacional_de_Investigaci%C3%B3n_Atmosf%C3%A9rica)

Medioambiental (NCEP), ambas entidades norteamericanas. Destaca sobre otros modelos porque

considera los efectos de la superficie terrestre, lo que permite resolver o pronosticar los fenómenos

21

meteorológicos inducidos o influenciados por esa estructura. Su uso está aceptado por el Servicio de

Evaluación Ambiental en Chile, para ser aplicado dentro del Sistema de Evaluación de Impacto

Ambiental, ya que permite cubrir la necesidad de ampliar la resolución espacial que poseen las

estaciones de monitoreo.

La forma de trabajo de WRF comprende la resolución de las ecuaciones primitivas de la atmósfera,

utilizando una descripción euleriana. Además, es un modelo no hidrostático, es decir, incluye la

variación de presión en el eje vertical de la atmósfera dentro de sus ecuaciones. Su manejo comprende

dos componentes importantes, el primero de ellos corresponde al WRF Pre-processing System (WPS)

donde se preparan los archivos de entrada para las simulaciones y el WRF Model (núcleo dinámico)

donde se integran las ecuaciones dinámicas y termodinámicas, modelos de nubes, superficie, radiación,

microfísica, entre otros.

Las variables meteorológicas más importantes que inciden en la dispersión de las emisiones

atmosféricas corresponden a la temperatura, velocidad del viento y estabilidad atmosférica de la

localidad sometida a evaluación. Estas variables son utilizadas como entradas en los modelos de

dispersión de contaminantes, necesarios para predecir y evaluar los impactos ambientales actuales o

de futuros proyectos. Es por esta razón que es necesario introducir los resultados obtenidos del modelo

WRF al modelo CALPUFF.

 - **CALPUFF**

El modelo CALPUFF es un sistema avanzado de modelación meteorológica y de calidad el aire, no

estacionario, desarrollado por Sigma Research Corporation (SRC) a fines de la década de 1980 (url:

http://www.src.com). La versión número cinco del modelo está aprobada por la Agencia de Protección

Ambiental de los Estados Unidos (EPA), lo que convierte a este modelo en una herramienta

ampliamente utilizada a nivel mundial. De forma particular, al igual que WRF, el modelo CALPUFF está

aprobado por el Servicio de Evaluación Ambiental en Chile, para poder emplearlo dentro del Sistema

de Evaluación de Impacto Ambiental.

CALPUFF modela el transporte y dispersión de contaminantes emitidos por las fuentes emisoras en

forma de paquetes o _puff_ de material, procesándolos a través del dominio de modelación. Este modelo

incluye tres componentes principales: WRF, CALPUFF y CALPOST, además de una larga selección de

preprocesadores, diseñados para incluir datos meteorológicos y geofísicos en el modelo. WRF simula

campos de viento y temperatura en un dominio de modelación engrillado y tridimensional. CALPUFF

modela la dispersión de contaminantes y CALPOST procesa las salidas de CALPUFF creando archivos

con las tabulaciones necesarias que permitan la evaluación de resultados.

22

**1.5.2.3** **Variables de Entrada ingresadas al Sistema de Modelación**

El sistema de modelación WRF-CALPUFF requiere de la siguiente información de entrada:

 - **Archivos NCEP-FNL (Final):** Información de entrada para el modelo WRF, con una resolución

espacial de 1km x 1km (url: https://rda.ucar.edu/datasets/ds083.2/).

 - **Uso de Suelo** **[a]** **:** Esta información permite definir los coeficientes de rugosidad superficial, razón

de Bowen y albedo. Los usos de suelo presentes en el área de estudio se encuentran en la

siguiente tabla.

**Tabla 8. Características Uso de Suelo.**

|Uso de Suelo|Albedob|Col3|Razón de Bowenc|Col5|Rugosidad Superficial (cm)|Col7|
|---|---|---|---|---|---|---|
|**Uso de Suelo**|**Verano**|**Invierno**|**Verano**|**Invierno**|**Verano**|**Invierno**|
|Bosque Perenne de Coníferas|0,13|0,14|0,5|0,5|50|50|
|Bosque Perenne de latifoliadas|0,13|0,14|0,5|0,5|50|50|
|Bosque deciduo de latifoliada|0,13|0,14|0,5|0,5|50|50|
|Bosque Mixto|0,13|0,14|0,5|0,5|50|50|
|Matorral Cerrado|0,22|0,25|1,0|1,0|10|10|
|Matorral Abierto|0,20|0,24|1,0|1,0|11|10|
|Sabana Arboladas|0,20|0,20|1,0|1,0|15|15|
|Sabanas|0,20|0,20|1,0|1,0|15|15|
|Pastos|0,18|0,23|1,0|1,0|15|5|
|Humedales Permanentes|0,14|0,14|0,5|0,5|20|20|
|Cultivos|0,18|0,23|1,0|1,0|14|5|
|Urbano|0,18|0,18|1,5|1,5|50|50|
|Mosaico de cultivos|0,18|0,23|1,0|1,0|15|5|
|Nieve|55|70|0,5|0,5|5|5|
|Suelo desnudo|0,25|0,25|1,0|1,0|10|10|
|Agua|0,8|0,8|0,0|0,0|1|1|

Fuente: Elaboración propia.

La siguiente figura presenta los usos de suelo presentes en el área de estudio, indicados en la tabla

anterior.

a Información obtenida a partir de preprocesador CTGPROC.

b Albedo: reflectividad a la luz solar del suelo (expresada como fracción respecto a la unidad).

c Razón de Bowen: definida como la razón entre flujos sensibles y latentes, a nivel de superficie.

23

**Figura 13. Uso de Suelo.**

Fuente: Elaboración propia.

24

- **Data de emisiones** : Corresponde al valor emitido por cada fuente considerada en los diferentes

escenarios de modelación y su localización en el territorio. Para el presente estudio, las

emisiones utilizadas se encuentran en la Tabla 7 correspondiente al Peor escenario, la

modelación considera que todas las actividades del peor escenario de duración 6 meses se

ejecutan simultáneamente durante los 365 días del año, esto con el fin de evaluar cualquier

posible escenario emisivo.

- **Ubicación de puntos de interés** : Corresponde a la identificación de los receptores con

representación poblacional o de recursos naturales más próximos a las fuentes para evaluar

los niveles de aporte que se transportan a estos lo que permite la evaluación de los resultados

en comparación con la normativa aplicable.

En el caso del proyecto se identificaron los receptores de interés con representación

poblacional cuyas coordenadas de localización se encuentran en la Tabla 9. Adicionalmente, en

la Figura 14 se muestra la ubicación de dichos puntos.

**Tabla 9. Localización Puntos Discretos.**

|ID|PUNTOS DE INTERÉS|COORDENADAS UTM<br>(DATUM WGS-84 HUSO 19S)|Col4|
|---|---|---|---|
|**ID**|**PUNTOS DE INTERÉS**|**ESTE (m)**|**NORTE (m)**|
|R1|Vivienda habitacional de un (1) piso, aledaña a ruta H-432|330529|6208258|
|R2|Vivienda habitacional de un (1) piso, aledaña a ruta H-432 y<br>el “Camino a Santa Lucila”<br>|330566|6208193|
|R3|~~Vivienda habitacional de un (1) piso, ubicada al norte del~~<br>Proyecto|329632|6208964|
|R4|Vivienda habitacional de dos pisos, ubicada dentro de<br>agrícola, al oeste del Proyecto|329489|6207247|
|R5|Oficina de administración (un piso) ubicada dentro de<br>Agrícola Santa Lucila LTDA|329545|6207305|
|R6|Vivienda Patronal de dos pisos, ubicada al oeste del Proyecto|329602|6207147|
|R7|Vivienda habitacional de un (1) piso, ubicada al oeste del<br>Proyecto|329747|6207052|
|R8|Vivienda habitacional de un (1) piso, ubicada al oeste del<br>Proyecto|329738|6206993|
|R9|Vivienda habitacional de un (1) piso, ubicada al norte de la<br>Área B del Proyecto|329983|6206909|
|R10|Vivienda habitacional de un (1) piso, localizada a un costado<br>de la Ruta H-418, al oeste del Proyecto|329474|6206984|

Fuente: Elaboración propia.

25

**Figura 14. Ubicación Puntos de Interés.**

Fuente: Elaboración propia.

26

- **Topografía del área de modelación:** Esta información es obtenida de datos satelitales para la

zona de estudio y alimenta el modelo meteorológico WRF quien a su vez alimenta el modelo

de dispersión Calpuff. En la Figura 15 se presenta la topografía del área de modelación en tres

dimensiones, en la cual se observan las principales variaciones topográficas del terreno. Las

curvas de terreno están espaciadas cada 100 metros (el archivo digital de elevación fue adjunto

y tiene extensión *.grd).

**Figura 15. Topografía del Área de Modelación.**

Fuente: Elaboración propia.

27

**1.5.3** **RESULTADOS DE LA MODELACIÓN**

Mediante la aplicación del modelo WRF-CALPUFF fue posible obtener las concentraciones de material

particulado respirable (MP 10 ), material particulado respirable fino (MP 2,5 ), dióxido de azufre (SO 2 ),

óxidos de nitrógeno (NO 2 ) y monóxido de carbono (CO) y las depositación del material particulado

sedimentable (MPS), que aportará el proyecto, basándose en los campos de vientos generados por la

modelación meteorológica realizada con WRF.

Los aportes del Proyecto fueron evaluados en los sectores de su entorno, para el análisis de

cumplimiento de las normas primarias y secundarias de calidad del aire las que, de acuerdo con su

cumplimiento, permitirán al Titular determinar si el Proyecto generará efectos adversos significativos

sobre la salud de la población y sobre la calidad y cantidad de los recursos naturales renovables.

En esta sección se presentan los aportes obtenidos por la modelación del escenario más desfavorable

del Proyecto en los puntos de interés poblacional y de recursos naturales (receptores discretos). En la

Tabla 10 y Tabla 11 se muestran los aportes del proyecto en cada uno de los receptores de interés.

28

**Tabla 10. Aportes del Proyecto en Puntos de Interés de Material Particulado, Peor Escenario.**

|ID|PUNTOS DE INTERÉS|MP (μg/m3)<br>10|Col4|MP (μg/m3)<br>2,5|Col6|MPS (mg/m2día)|Col8|
|---|---|---|---|---|---|---|---|
|**ID**|**PUNTOS DE INTERÉS**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Secundaria**|**Secundaria**|
|**ID**|**PUNTOS DE INTERÉS**|**Media Anual**|**P98 Diario**|**Media Anual**|**P98 Diario**|**Media Anual**|**Media**<br>**Mensual**|
|R1|Vivienda habitacional de un (1) piso, aledaña a ruta H-432|0,4445|2,1499|0,1353|0,6559|0,0065|0,0152|
|R2|Vivienda habitacional de un (1) piso, aledaña a ruta H-432 y el<br>“Camino a Santa Lucila”|0,4124|2,0318|0,1255|0,6200|0,0061|0,0149|
|R3|Vivienda habitacional de un (1) piso, ubicada al norte del<br>Proyecto|1,5957|5,2449|0,4840|1,5959|0,0290|0,0729|
|R4|Vivienda habitacional de dos pisos, ubicada dentro de agrícola,<br>al oeste del Proyecto<br>|0,3588|1,8573|0,1076|0,5628|0,0069|0,0177|
|R5|~~Oficina de administración (un piso) ubicada dentro de Agrícola~~<br>Santa Lucila LTDA|0,3951|1,9602|0,1188|0,5955|0,0067|0,0177|
|R6|Vivienda Patronal de dos pisos, ubicada al oeste del Proyecto|0,2764|1,3657|0,0821|0,4141|0,0054|0,0130|
|R7|Vivienda habitacional de un (1) piso, ubicada al oeste del<br>Proyecto|0,1969|0,8991|0,0579|0,2726|0,0042|0,0076|
|R8|Vivienda habitacional de un (1) piso, ubicada al oeste del<br>Proyecto|0,1886|0,9017|0,0552|0,2733|0,0042|0,0076|
|R9|Vivienda habitacional de un (1) piso, ubicada al norte de la Área<br>B del Proyecto|0,1299|0,6198|0,0379|0,1858|0,0029|0,0056|
|R10|Vivienda habitacional de un (1) piso, localizada a un costado de<br>la Ruta H-418, al oeste del Proyecto|0,2545|1,3482|0,0745|0,4052|0,0061|0,0145|

Fuente: Elaboración propia.

**Tabla 11. Aportes del Proyecto en Puntos de Interés de Gases, Peor Escenario.**

|ID|PUNTOS DE INTERÉS|SO (μg/m3)<br>2|Col4|Col5|Col6|Col7|Col8|NO (μg/m3)<br>2|Col10|CO (μg/m3)|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**ID**|**PUNTOS DE INTERÉS**|**Primaria**|**Primaria**|**Primaria**|**Secundaria**|**Secundaria**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|
|**ID**|**PUNTOS DE INTERÉS**|**Media**<br>**Anual**|**P99**<br>**Diario**|**P98,5**<br>**Horario**|**Media**<br>**Anual**|**P99,7**<br>**Diario**|**P99,73**<br>**Horario**|**Media**<br>**Anual**|**P99**<br>**Horario**|**P99**<br>**8 Horas**|**P99**<br>**Horario**|
|R1|Vivienda habitacional de un (1) piso,<br>aledaña a ruta H-432|0,0166|0,0968|0,2798|0,0166|0,1268|0,6553|0,3240|18,8100|8,0740|34,1430|
|R2|Vivienda habitacional de un (1) piso,<br>aledaña a ruta H-432 y el “Camino a Santa<br>Lucila”|0,0153|0,0933|0,2561|0,0153|0,1187|0,6606|0,2991|17,7910|7,3916|32,0960|

29

|ID|PUNTOS DE INTERÉS|SO (μg/m3)<br>2|Col4|Col5|Col6|Col7|Col8|NO (μg/m3)<br>2|Col10|CO (μg/m3)|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**ID**|**PUNTOS DE INTERÉS**|**Primaria**|**Primaria**|**Primaria**|**Secundaria**|**Secundaria**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|
|**ID**|**PUNTOS DE INTERÉS**|**Media**<br>**Anual**|**P99**<br>**Diario**|**P98,5**<br>**Horario**|**Media**<br>**Anual**|**P99,7**<br>**Diario**|**P99,73**<br>**Horario**|**Media**<br>**Anual**|**P99**<br>**Horario**|**P99**<br>**8 Horas**|**P99**<br>**Horario**|
|R3|Vivienda habitacional de un (1) piso,<br>ubicada al norte del Proyecto|0,0633|0,2243|0,6709|0,0633|0,2334|1,1022|1,2564|28,8550|16,0270|51,2990|
|R4|Vivienda habitacional de dos pisos, ubicada<br>dentro de agrícola, al oeste del Proyecto|0,0123|0,0949|0,2498|0,0123|0,1262|0,4157|0,2891|10,3180|6,6557|17,8440|
|R5|Oficina de administración (un piso) ubicada<br>dentro de Agrícola Santa Lucila LTDA|0,0140|0,1032|0,2742|0,0140|0,1140|0,5152|0,3132|12,6590|7,0922|21,8150|
|R6|Vivienda Patronal de dos pisos, ubicada al<br>oeste del Proyecto|0,0085|0,0561|0,1648|0,0085|0,0693|0,3315|0,2285|9,4932|4,3077|16,7280|
|R7|Vivienda habitacional de un (1) piso,<br>ubicada al oeste del Proyecto<br>|0,0053|0,0400|0,0931|0,0053|0,0528|0,2512|0,1683|6,9006|2,7393|12,0630|
|R8|~~Vivienda habitacional de un (1) piso,~~<br>ubicada al oeste del Proyecto|0,0048|0,0386|0,0770|0,0048|0,0481|0,2395|0,1651|6,7992|2,5486|11,9650|
|R9|Vivienda habitacional de un (1) piso,<br>ubicada al norte de la Área B del Proyecto|0,0031|0,0242|0,0485|0,0031|0,0282|0,1786|0,1140|4,4728|2,2421|8,1018|
|R10|Vivienda habitacional de un (1) piso,<br>localizada a un costado de la Ruta H-418, al<br>oeste del Proyecto|0,0068|0,0610<br>|0,1378<br>|0,0068<br>|0,0727|0,2639|0,2265|7,4422|4,4069|12,6530|

Fuente: Elaboración propia.

30

**1.5.3.1** **Aportes en Puntos de Máxima Concentración**

La Tabla 12 presenta la ubicación de los Puntos de Máxima Concentración (PMC), tanto para el
material particulado (MP 10, MP 2,5 y MPS), como para los gases (SO 2, NO 2 y CO), durante el peor
escenario de emisiones del Proyecto.

**Tabla 12. Puntos de Máxima Concentración (PMC), Peor Escenario.**

|PARÁMETRO|ESTADÍSTICO|PMC|NORMA|UNIDAD|% NORMA|COORDENADAS UTM<br>(WGS84 HUSO 18S)|Col8|
|---|---|---|---|---|---|---|---|
|**PARÁMETRO**|**ESTADÍSTICO**|**PMC**|**NORMA**|**UNIDAD**|**% NORMA**|**Este (m)**|**Norte (m)**|
|MPS|Promedio del<br>Periodo|0,10|100|mg/m2-día|0,1%|326496|6190009|
|MPS|Promedio<br>mensual|0,21|150|150|0,1%|326496|6190009|
|MP10|Promedio del<br>Periodo|5,96|50|μg/m3 <br>|11,9%|326496|6190009|
|MP10|Percentil 98<br>Diario|12,86|130|130|9,9%|326496|6190009|
|MP2,5|Promedio del<br>Periodo<br>|1,81|20|20|9,1%|326496|6190009|
|MP2,5|~~Percentil 98~~<br>Diario|3,91|50|50|7,8%|326496|6190009|
|SO2|Promedio del<br>Periodo|0,1755|60|60|0,3%|326496|6190009|
|SO2|Percentil 99<br>Diario|0,6499|150|150|0,4%|326496|6190009|
|SO2|Percentil<br>98,5 Horario|1,4166|350|350|0,4%|326496|6190009|
|SO2|Promedio del<br>Periodo|0,1755|80|80|0,2%|326496|6190009|
|SO2|Percentil<br>99,7 Diario|0,6869|365|365|0,2%|326496|6190009|
|SO2|Percentil<br>99,73 Horario|2,049|1000|1000|0,2%|326496|6190009|
|NO2|Promedio del<br>Periodo|4,95|100|100|4,9%|326496|6190009|
|NO2|Percentil 99<br>Horario|46,11|400|400|11,5%|326496|6190009|
|CO|Percentil 99 8<br>Horas|35,35|10,000|10,000|0,4%|326496|6190009|
|CO|Percentil 99<br>Horario|82,32<br>|30,000<br>|30,000<br>|0,3%|326496|6190009|

Fuente: Elaboración propia.

31

**Figura 16. Ubicación de Puntos de Máxima Concentración, Peor Escenario.**

Fuente: Elaboración propia.

32

**1.5.4** **Escenario Sinérgico**

De acuerdo con la secuencia de las actividades constructivas, el proyecto PFV José Solar ejecutará su

fase de construcción, de duración 6 meses, e inmediatamente posterior a esto se iniciará su fase de

operación y en paralelo se ejecutará la fase de construcción del Proyecto contiguo PFV Juan Gonzalo

Solar de duración 6 meses, este cronograma de actividades se presenta a continuación.

**Tabla 13. Cronograma Sinérgico.**

|Actividad|Mes|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Actividad**|dic-<br>24|ene-<br>25|feb-<br>25|mar-<br>25|abr-<br>25|may-<br>25|jun-<br>25|jul-<br>25|ago-<br>25|sept-<br>25|oct-<br>25|nov-<br>25|dic-<br>25|
|Construcción PFV José Solar||||||||||||||
|Operación PFV José Solar||||||||||||||
|Construcción PFV Juan Gonzalo<br>Solar||||||||||||||

Fuente: Elaboración propia.

De acuerdo al cronograma antes expuesto, se realizó una modelación en conjunto que consideró la

modelación de los 6 meses de construcción del proyecto PFV José Solar y los seis meses posteriores de

su operación más la construcción del proyecto PFV Juan Gonzalo Solar, actividades secuenciadas para

un año cronológico de modelación, con el fin de representar el escenario sinérgico que se producirá y

poder con esto evaluar los niveles de aporte que recibirán los receptores de interés cercanos a las

fuentes antes identificada.

A continuación se presentan los resultados de la modelación sinérgica antes expuesta y su evaluación

respecto de los niveles normados.

33

**Tabla 14. Aportes Escenario sinérgico en Puntos de Interés de Material Particulado.**

|ID|PUNTOS DE INTERÉS|MP (μg/m3)<br>10|Col4|MP (μg/m3)<br>2,5|Col6|MPS (mg/m2día)|Col8|
|---|---|---|---|---|---|---|---|
|**ID**|**PUNTOS DE INTERÉS**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Secundaria**<br>|**Secundaria**<br>|
|**ID**|**PUNTOS DE INTERÉS**|**Media Anual**|**P98 Diario**|**Media Anual**|**P98 Diario**|**Media Anual**|~~**Media**~~<br>**Mensual**|
|R1|Vivienda habitacional de un (1) piso, aledaña a ruta H-432|0,3808|1,8850|0,0996|0,5753|0,0052|0,0096|
|R2|Vivienda habitacional de un (1) piso, aledaña a ruta H-432 y el<br>“Camino a Santa Lucila”|0,3579|1,8036|0,0932|0,5470|0,0049|0,0091|
|R3|Vivienda habitacional de un (1) piso, ubicada al norte del<br>Proyecto|0,9548|3,9732|0,2763|1,2071|0,0139|0,0298|
|R4|Vivienda habitacional de dos pisos, ubicada dentro de agrícola,<br>al oeste del Proyecto|1,7582|5,6861|0,2599|0,7868|0,0524|0,2083|
|R5|Oficina de administración (un piso) ubicada dentro de Agrícola<br>Santa Lucila LTDA|2,1245|5,8821|0,3151|0,8668|0,0577|0,1588|
|R6|Vivienda Patronal de dos pisos, ubicada al oeste del Proyecto<br>|0,9966|3,9418|0,1747|0,6304|0,0199|0,0668|
|R7|~~Vivienda habitacional de un (1) piso, ubicada al oeste del~~<br>Proyecto|0,9178|3,6099|0,1523|0,6022|0,0176|0,0604|
|R8|Vivienda habitacional de un (1) piso, ubicada al oeste del<br>Proyecto|0,8894|3,5392|0,1420|0,5768|0,0202|0,0799|
|R9|Vivienda habitacional de un (1) piso, ubicada al norte de la Área<br>B del Proyecto<br>|0,8624|3,2150|0,1714|0,5708|0,0118|0,0393|
|R10|~~Vivienda habitacional de un (1) piso, localizada a un costado de~~<br>la Ruta H-418, al oeste del Proyecto|0,6522|3,0428|0,1252|0,4958|0,0168|0,0920|

Fuente: Elaboración propia.

**Tabla 15. Aportes Escenario sinérgico en Puntos de Interés de Gases.**

|ID|PUNTOS DE INTERÉS|SO (μg/m3)<br>2|Col4|Col5|Col6|Col7|Col8|NO (μg/m3)<br>2|Col10|CO (μg/m3)|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**ID**|**PUNTOS DE INTERÉS**<br>|**Primaria**|**Primaria**|**Primaria**|**Secundaria**|**Secundaria**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|
|**ID**|**PUNTOS DE INTERÉS**<br>|**Media**<br>**Anual**|**P99**<br>**Diario**|**P98,5**<br>**Horario**|**Media**<br>**Anual**|**P99,7**<br>**Diario**|**P99,73**<br>**Horario**|**Media**<br>**Anual**|**P99**<br>**Horario**|**P99**<br>**8 Horas**|**P99**<br>**Horario**|
|R1|~~Vivienda habitacional de un (1) piso,~~<br>aledaña a ruta H-432|0,0155|0,0797|0,2163|0,0155|0,0968|0,5505|0,2997|18,0520|8,2171|34,5230|
|R2|Vivienda habitacional de un (1) piso,<br>aledaña a ruta H-432 y el “Camino a Santa<br>Lucila”|0,0145|0,0745|0,2069|0,0145|0,0933|0,5041|0,2815|17,0320|8,0093|33,7940|

34

|ID|PUNTOS DE INTERÉS|SO (μg/m3)<br>2|Col4|Col5|Col6|Col7|Col8|NO (μg/m3)<br>2|Col10|CO (μg/m3)|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**ID**|**PUNTOS DE INTERÉS**|**Primaria**|**Primaria**|**Primaria**|**Secundaria**|**Secundaria**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|
|**ID**|**PUNTOS DE INTERÉS**|**Media**<br>**Anual**|**P99**<br>**Diario**|**P98,5**<br>**Horario**|**Media**<br>**Anual**|**P99,7**<br>**Diario**|**P99,73**<br>**Horario**|**Media**<br>**Anual**|**P99**<br>**Horario**|**P99**<br>**8 Horas**|**P99**<br>**Horario**|
|R3|Vivienda habitacional de un (1) piso,<br>ubicada al norte del Proyecto<br>|0,0385|0,2025|0,4848|0,0385|0,2189|0,9139|0,7614|24,5400|14,7640|49,8330|
|R4|~~Vivienda habitacional de dos pisos, ubicada~~<br>dentro de agrícola, al oeste del Proyecto|0,0318|0,1564|0,3785|0,0318|0,1781|0,5558|0,6933|12,3560|13,7620|31,3350|
|R5|Oficina de administración (un piso) ubicada<br>dentro de Agrícola Santa Lucila LTDA|0,0426|0,2013|0,4494|0,0426|0,2199|0,6874|0,8962|16,1000|18,3030|38,5180|
|R6|Vivienda Patronal de dos pisos, ubicada al<br>oeste del Proyecto|0,0302|0,1751|0,4199|0,0302|0,1849|0,6363|0,6480|15,4320|15,2730|35,8800|
|R7|Vivienda habitacional de un (1) piso,<br>ubicada al oeste del Proyecto|0,0264|0,1615|0,4002|0,0264|0,1674|0,6138|0,5627|14,0800|9,9559|30,3950|
|R8|Vivienda habitacional de un (1) piso,<br>ubicada al oeste del Proyecto|0,0217|0,1425|0,3651|0,0217|0,1469|0,5529|0,4824|12,5250|9,4698|26,5680|
|R9|Vivienda habitacional de un (1) piso,<br>ubicada al norte de la Área B del Proyecto|0,0472|0,2124|0,4153|0,0472|0,2610|0,6653|0,9276|15,5330|10,6400|25,5640|
|R10|Vivienda habitacional de un (1) piso,<br>localizada a un costado de la Ruta H-418, al<br>oeste del Proyecto|0,0187|0,1047|0,2979|0,0187|0,1221|0,4406|0,4724|10,8090|9,3376|21,9290|

Fuente: Elaboración propia.

**1.5.1** **Análisis de Cumplimiento de Normativa Ambiental**

Para establecer el cumplimiento de la normativa ambiental vigente de calidad del aire, en la Tabla 16 y Tabla 17 se presentan los porcentajes

respecto a la norma de los aportes del escenario sinérgico en cada punto de interés. Es importante mencionar que los aportes en todos los

receptores evaluados no superan un 6% de los límites normados para cada contaminante evaluado.

De acuerdo con los resultados obtenidos, existe cumplimiento normativo para todas las fases del Proyecto. Además, se recala que la duración de

la fase donde ocurre el peor escenario (construcción), tendrá una duración limitada y no permanente en el tiempo, además la extensión espacial

de los aportes es limitada al área del Proyecto. Esto también considerando dado la tipología de Proyecto, el cual se caracteriza por bajas emisiones

durante su fase de operación.

35

**Tabla 16. Análisis de Cumplimiento de Normativa Escenario sinérgico en Puntos de Interés de Material Particulado.**

|ID|PUNTOS DE INTERÉS|MP (μg/m3)<br>10|Col4|MP (μg/m3)<br>2,5|Col6|MPS (mg/m2día)|Col8|
|---|---|---|---|---|---|---|---|
|**ID**|**PUNTOS DE INTERÉS**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Secundaria**|**Secundaria**|
|**ID**|**PUNTOS DE INTERÉS**|**Media Anual**|**P98 Diario**|**Media Anual**|**P98 Diario**|**Media Anual**|**Media Mensual**|
|R1|Vivienda habitacional de un (1) piso, aledaña a<br>ruta H-432|<1%|1%|<1%|1%|<1%|<1%|
|R2|Vivienda habitacional de un (1) piso, aledaña a<br>ruta H-432 y el “Camino a Santa Lucila”|<1%|1%|<1%|1%|<1%|<1%|
|R3|Vivienda habitacional de un (1) piso, ubicada al<br>norte del Proyecto|2%|3%|1%|2%|<1%|<1%|
|R4|Vivienda habitacional de dos pisos, ubicada dentro<br>de agrícola, al oeste del Proyecto|4%|4%|1%|2%|<1%|<1%|
|R5|Oficina de administración (un piso) ubicada dentro<br>de Agrícola Santa Lucila LTDA|4%|5%|2%|2%|<1%|<1%|
|R6|Vivienda Patronal de dos pisos, ubicada al oeste<br>del Proyecto|2%|3%|<1%|1%|<1%|<1%|
|R7|Vivienda habitacional de un (1) piso, ubicada al<br>oeste del Proyecto|2%|3%|<1%|1%|<1%|<1%|
|R8|Vivienda habitacional de un (1) piso, ubicada al<br>oeste del Proyecto|2%|3%|<1%|1%|<1%|<1%|
|R9|Vivienda habitacional de un (1) piso, ubicada al<br>norte de la Área B del Proyecto|2%|2%|<1%|1%|<1%|<1%|
|R10|Vivienda habitacional de un (1) piso, localizada a<br>un costado de la Ruta H-418, al oeste del Proyecto|1%|2%|<1%|<1%|<1%|<1%|
|**NORMA**|**NORMA**|**50**|**130**|**20**|**50**|**100**|**150**|

Fuente: Elaboración propia.

36

**Tabla 17. Análisis de Cumplimiento de Normativa Aportes Escenario sinérgico en Puntos de Interés de Gases.**

|ID|PUNTOS DE INTERÉS|SO2 (μg/m3)|Col4|Col5|Col6|Col7|Col8|NO2 (μg/m3)|Col10|CO (μg/m3)|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**ID**|**PUNTOS DE INTERÉS**<br>|**Primaria**|**Primaria**|**Primaria**|**Secundaria**|**Secundaria**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|
|**ID**|**PUNTOS DE INTERÉS**<br>|**Media**<br>**Anual**|**P99**<br>**Diario**|**P98,5**<br>**Horario**|**Media**<br>**Anual**|**P99,7**<br>**Diario**|**P99,73**<br>**Horario**|**Media**<br>**Anual**|**P99**<br>**Horario**|**P99**<br>**8 Horas**|**P99**<br>**Horario**|
|R1|~~Vivienda habitacional de un (1) piso, aledaña a~~<br>ruta H-432|<1%|<1%|<1%|<1%|<1%|<1%|<1%|5%|<1%|<1%|
|R2|Vivienda habitacional de un (1) piso, aledaña a<br>ruta H-432 y el “Camino a Santa Lucila”|<1%|<1%|<1%|<1%|<1%|<1%|<1%|4%|<1%|<1%|
|R3|Vivienda habitacional de un (1) piso, ubicada al<br>norte del Proyecto|<1%|<1%|<1%|<1%|<1%|<1%|<1%|6%|<1%|<1%|
|R4|Vivienda habitacional de dos pisos, ubicada<br>dentro de agrícola, al oeste del Proyecto|<1%|<1%|<1%|<1%|<1%|<1%|<1%|3%|<1%|<1%|
|R5|Oficina de administración (un piso) ubicada<br>dentro de Agrícola Santa Lucila LTDA|<1%|<1%|<1%|<1%|<1%|<1%|<1%|4%|<1%|<1%|
|R6|Vivienda Patronal de dos pisos, ubicada al oeste<br>del Proyecto|<1%|<1%|<1%|<1%|<1%|<1%|<1%|4%|<1%|<1%|
|R7|Vivienda habitacional de un (1) piso, ubicada al<br>oeste del Proyecto|<1%|<1%|<1%|<1%|<1%|<1%|<1%|4%|<1%|<1%|
|R8|Vivienda habitacional de un (1) piso, ubicada al<br>oeste del Proyecto|<1%|<1%|<1%|<1%|<1%|<1%|<1%|3%|<1%|<1%|
|R9|Vivienda habitacional de un (1) piso, ubicada al<br>norte de la Área B del Proyecto|<1%|<1%|<1%|<1%|<1%|<1%|<1%|4%|<1%|<1%|
|R10|Vivienda habitacional de un (1) piso, localizada<br>a un costado de la Ruta H-418, al oeste del<br>Proyecto|<1%|<1%|<1%|<1%|<1%|<1%|<1%|3%|<1%|<1%|
|**NORMA**|**NORMA**|**60**|**150**<br>|**350**<br>|**80**<br>|**365**|**1000**|**100**|**400**|**10000**|**30000**|

Fuente: Elaboración propia.

37

**1.5.2** **Mapas de Isoconcentraciones**

A continuación, se presentan las isolíneas de concentración de MP 10, MP 2,5, MPS, NO 2, CO y SO 2 en
el entorno del Proyecto para la fase de construcción del Proyecto.

38

**Figura 17. Percentil 98 Promedio Diario de MP** **10** **.**

Fuente: Elaboración propia.

39

**Figura 18. Promedio del Período de MP** **10** **.**

Fuente: Elaboración propia.

40

**Figura 19. Percentil 98 Promedio Diario de MP** **2,5** **.**

Fuente: Elaboración propia.

41

**Figura 20. Promedio del Período de MP** **2,5** **.**

Fuente: Elaboración propia.

42

**Figura 21. Promedio del Período de MPS.**

Fuente: Elaboración propia.

43

**Figura 22. Promedio Mensual de MPS.**

Fuente: Elaboración propia.

44

**Figura 23. Percentil 98,5 Promedio Horario de SO** **2** **.**

Fuente: Elaboración propia.

45

**Figura 24. Percentil 99 Promedio Diario de SO** **2** **.**

Fuente: Elaboración propia.

46

**Figura 25. Percentil 99,7 Promedio Diario de SO** **2** **.**

Fuente: Elaboración propia.

47

**Figura 26. Percentil 99,73 Promedio Horario de SO** **2** **.**

Fuente: Elaboración propia.

48

**Figura 27. Promedio del Período de SO** **2** **.**

Fuente: Elaboración propia.

49

**Figura 28. Percentil 99 Máximo Horario de NO2.**

**Fuente: Elaboración propia** **.**

50

**Figura 29. Promedio del Período de NO** **2** **.**

Fuente: Elaboración propia.

51

**Figura 30. Percentil 99 Máximo Horario de CO.**

Fuente: Elaboración propia.

52

**Figura 8. Percentil 99 Máximo 8 Horas de CO.**

Fuente: Elaboración propia.

53

**1.5.3** **Definición del Área de Influencia de la Componente Aire.**

De acuerdo a lo indicado en la “ _Guía sobre el Área de Influencia en el Sistema de Evaluación de_

_Impacto Ambiental_ ” del SEA (2017): En la letra a) del artículo 2 del Reglamento del SEIA se define

área de influencia (AI) como _El área o espacio geográfico, cuyos atributos, elementos naturales o_

_socioculturales deben ser considerados con la finalidad de definir si el proyecto o actividad genera o_

_presenta alguno de los efectos, características o circunstancias del artículo 11 de la Ley, o bien para_

_justificar la inexistencia de dichos efectos, características o circunstancias_ .

De esta manera se establece el criterio para la delimitación del área de Influencia general que

consiste en delimitar un área con las isoconcentraciones obtenidas en la modelación para cada

contaminante y estadístico normado, de acuerdo con los niveles porcentuales recomendados como
significativos (SIL) por la USEPA para los estándares nacionales de calidad del aire en EEUU (NAAQS [5] )
adaptados a la normativa chilena (Informe N°1575423, DICTUC 2022 [6] ) los cuales se muestran en la

siguiente tabla:

**Tabla 18. Límites normativos considerados para determinar el área de Influencia del Proyecto.**

|PARÁMETRO|PERIODO EVALUADO|SIL7<br>PORCENTUAL<br>USEPA [%]|RESPECTO DE LA NORMA CHILENA DE CALIDAD<br>DEL AIRE|Col5|
|---|---|---|---|---|
|**PARÁMETRO**|**PERIODO EVALUADO**|**SIL7 **<br>**PORCENTUAL**<br>**USEPA [%]**|**NORMA CHILENA**<br>**(μG/M3) **|**INCREMENTO SIGNIFICATIVO**<br>**EN LA CONCENTRACIÓN**<br>**(μG/M3) **|
|SO2|1 hora|4,0%|350|14,0|
|SO2|24 horas|1,4%|150|2,0|
|SO2|Promedio Anual|2,0%|60|1,2|
|NO2|1 hora|4,0%|400|16,0|
|NO2|Promedio Anual|1,0%|100|1,0|
|MP10|24 horas|3,3%|130|5,0|
|MP10|Promedio Anual|2,0%|50|1,0|
|MP2,5|24 horas|3,4%|50|1,7|
|MP2,5|Promedio Anual|1,7%|20|0,3|
|CO<br>|1 hora|5,0%|30.000|1500,0|
|CO<br>|8 horas<br>|4,9%<br>|10.000<br>|488,9<br>|

Fuente: Tabla 7-5 del informe Evaluación significancia del impacto de las emisiones de un proyecto o actividad en zonas

saturadas en el marco del SEIA, ID Licitación: 1588-16-LE21.

De acuerdo con la definición antes explicada a continuación se presenta el área de influencia general

para la componente aire.

5 NAAQS: National Ambient Air Quality Standards (Estándares Nacionales de calidad del Aire Ambiental)
6 Evaluación significancia del impacto de las emisiones de un proyecto o actividad en zonas saturadas en el marco del SEIA, ID Licitación:

1588-16-LE21

7 SILs: Significant Impact Levels (Niveles de Impacto significativos)

54

**Figura 31. Área de Influencia Componente Aire**

Fuente: Elaboración propia

55

### 2 CONCLUSIONES

Con respecto a la evaluación del cumplimiento normativo y de los posibles efectos adversos sobre

la calidad del aire y la salud de la población se realizó una modelación de la dispersión de las

emisiones antes calculadas en el área de influencia del Proyecto, para dos escenarios uno con la

ejecución continua de las actividades emisivas del proyecto PFV José Solar durante un año

calendario y la otro representando al escenario sinérgico que coincidirá en un año calendario entre

las fases de construcción del proyecto, su operación y la construcción del proyecto PFV Juan Gonzalo

Solar, estos análisis se desarrollaron de acuerdo con lo recomendado por la Guía para el uso de

modelos de calidad del aire en el SEIA (Servicio de Evaluación Ambiental, Segunda edición 2023).

De los resultados de la modelación de dispersión de contaminantes de material particulado

sedimentable (MPS), material particulado respirable (MP10 y MP2,5), dióxido de azufre (SO2),

dióxido de nitrógeno (NO2) y monóxido de carbono (CO) para los escenarios modelados más

desfavorable del Proyecto se desprende lo siguiente:

 - Los aportes del escenario sinérgico de material particulado (MPS, MP10 y MP2,5) en los

receptores de interés resultan ser inferiores al 5% de la norma en todos los estadísticos

normados, encontrándose este valor en el punto de interés R5 para el MP10 percentil 98.

Referente a los aportes de gases (NOx, SO2 y CO) generados por el Proyecto, estos no superan

al 6% de la norma en todas sus métricas, cuyo máximo corresponde al percentil 99 horario de

NO2 para el punto de interés R3.

 - Respecto a los puntos de máxima concentración evaluados para la modelación del proyecto

PFV José Solar desde la grilla de muestreo modelada de la fase de construcción, para todos

los contaminantes, estos se localizaron dentro del área del Proyecto cercanos a caminos

internos e instalación de faena, todos en un sector sin representación poblacional.

 - Adicionalmente, es importante agregar que no se supera ninguna norma en los Puntos de

máxima concentración para todos de los contaminantes evaluados, cabe mencionar que la

modelación se realizó para el peor escenario de construcción del proyecto PFV José Solar que

considera que las actividades de movimiento de tierra y combustión de maquinarías se están

desarrollando simultáneamente en todas las superficies intervenidas, la Línea de tensión y

caminos de acceso, es decir que se distribuyeron espacialmente sus emisiones en todos los

metros cuadrados que presenta obras el Proyecto. Además, en el caso de las vías

pavimentadas y no pavimentadas se distribuyeron las emisiones en todos los metros

cuadrados que cubren estas vías considerando las emisiones de todos los vehículos, es decir

que la flota completa circula al mismo tiempo por todas las vías simultáneamente durante un

año, con el fin de representar y evaluar la peor condición, ya que esto no ocurrirá debido a

que existe una secuencia en las actividades según la carta Gantt y la fase de construcción tiene

una duración de 6 meses. Además en la modelación se consideró que todo el NOx generado

es igual a NO2 como peor caso.

56

 - Finalmente, las isoconcentraciones obtenidas muestran que los contaminantes tienen una

dispersión local, ubicándose preferentemente sobre el Proyecto y sus fuentes de emisión

específicamente caminos internos, zonas de los paneles, instalaciones de faena y los caminos,

presentando una dispersión local y diluyéndose dentro de la misma zona de estudio no

logrando transportarse, concentradamente a localidades aledañas y alcanzando niveles no

significativos a una distancia de 200 metros desde las obras. Con respecto a las otras fuentes

o zonas donde se realizarán actividades emisivas como los caminos pavimentados, las

emisiones generadas de acuerdo con la modelación de dispersión no logran concentraciones

iguales o sobres el 1% de la norma por lo que no se generaron por el modelo

isoconcentraciones en estas zonas, considerando sus aportes no significativos.

 Con respecto al Área de Influencia esta se delimitó considerando los criterios utilizados para
establecer el área de estudio según la “Guía sobre el Área de Influencia en el Sistema de

Evaluación de Impacto Ambiental” del SEA (2017), con esto se obtuvo el área general que

corresponde al área generada por las isoconcentraciones en base a los niveles de SIL, cuya

suma determinó el área de influencia general para la componente.

De acuerdo con lo antes expuesto y los resultados obtenidos se demuestra que los aportes del

Proyecto en su escenario más desfavorable de construcción y el escenario sinérgico con el proyecto

PFV Juan Gonzalo Solar son poco significativos dada su magnitud relativa a la norma, extensión y

duración en el tiempo (6 meses y 12 meses, respectivamente) por lo que no modifican las actuales

condiciones de calidad del aire de su entorno. Esto dado que los aportes pierden significancia si se

considera la duración temporal (6 meses y 12 meses, respectivamente) y extensión espacial (local

al área de cada proyecto y su entorno inmediato), por lo que una emisión de duración limitada no

representa un aporte permanente que pueda modificar sustancialmente el comportamiento

temporal de la calidad del aire de la zona aledaña a las obras.

Además, es importante agregar que las emisiones aportadas durante la fase de operación son

mínimas en comparación a los escenarios evaluados.

En base a todo lo antes indicado se concluye que el Proyecto, no producirá efectos adversos

significativos sobre la calidad del aire ni sobre la salud de la población del área de influencia, ni

modificación las actuales condiciones de calidad del aire que impidan dar cumplimiento a la

normativa vigente.

57

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Coordenadas Vértices del Área de Modelación del Proyecto (Área de Estudio).****

| VÉRTICE | COORDENADAS UTM (DATUM WGS-84 HUSO 18S) | Col3 |
| --- | --- | --- |
| **VÉRTICE** | **NORTE (M)** | **ESTE (M)** |
| Noreste | 6229108,759 | 364359,059 |
| Noroeste | 6227683,765 | 287194,625 |
| Suroeste | 6150856,023 | 288624,816 |

**Tabla 2.: Normativa de Calidad del Aire Consideradas en el Estudio.****

| PARÁMETRO | TIPO DE NORMA | ESTADÍSTICO | VALOR | REFERENCIA |
| --- | --- | --- | --- | --- |
| MPSa | Secundaria | Promedio del Periodo | 100 mg/m2-día | D.S. N°04/92 MINAGRI |
| MPSa | Secundaria | Promedio Mensual | 150 mg/m2-día | D.S. N°04/92 MINAGRI |
| MP10 | Primaria | Promedio del periodo | 50μg/m3N | D.S. N°45/02 MINSEGPRES |
| MP10 | Primaria | Percentil 98 Diario | 130μg/m3N | D.S. N°12/21 MMA |

**Tabla 3: Localización de Referencia y Variables Meteorológicas Monitoreadas****

| ESTACIÓN | COORDENADAS UTM<br>(DATUM WGS-84 HUSO 18S) | Col3 | VARIABLES | PERIODO |
| --- | --- | --- | --- | --- |
| **ESTACIÓN** | **NORTE (M)** | **ESTE (M)** | **ESTE (M)** | **ESTE (M)** |
| Rayentué | 331.629. | 6.200.845 | Velocidad del viento<br>Dirección del viento<br>Temperatura | 01 de enero al 31 de<br>diciembre 2021 |

**Tabla 4.: Estadísticas de Datos Meteorológicos Monitoreados.****

| ESTACIÓN | DATOS TOTALES | PORCENTAJE DE CALMA (%) | Col4 |
| --- | --- | --- | --- |
| **ESTACIÓN** | **DATOS TOTALES** | **PERIODO DIURNO** | **PERIODO NOCTURNO** |
| Rayentué | 8.760 | 100% | 31% |

**Tabla 5.: Estadísticas de Datos de Temperatura.****

| Estación | DATOS TOTALES | % DATOS TOTALES |
| --- | --- | --- |
| Rayentué | 8.760 | 100% |

**Tabla 6.: Valor de Incertidumbre Variables Meteorológicas****

| ESTADÍSTICO | VELOCIDAD DEL VIENTO | Col3 | TEMPERATURA | Col5 |
| --- | --- | --- | --- | --- |
| **ESTADÍSTICO** | **VALOR**<br>**RECOMENDADO** | **RESULTADO DE**<br>**ESTACIÓN** | **VALOR**<br>**RECOMENDADO** | **RESULTADO DE**<br>**ESTACIÓN** |
| SESGO | [-2,5;2,5] (m/s) | 1,14 | [-4;4] (m/s) | -0,05 |
| MAE | ≤3 (m/s) | 1,19 | ≤4 (m/s) | 2,61 |
| RMSE | ≤3,5 (m/s) | 1,46 | ≤4,5 (m/s) | 3,29 |
| CORR | >0,6 | 0,68 | >0,8 | 0,92 |

**Tabla 7.: Emisiones del Proyecto Peor escenario Fase de Construcción.****

| FUENTE | MP | MP10 | MP2,5 | NOX | SO2 | NH3 | CO | COV | UNIDAD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Escarpe | 0,030 | 0,030 | 0,005 | - | - | - | - | - | ton/año |
| Nivelación | 0,006 | 0,004 | 0,000 | - | - | - | - | - | ton/año |
| Compactación | 0,013 | 0,003 | 0,001 | - | - | - | - | - | ton/año |
| Excavación | 0,073 | 0,017 | 0,008 | - | - | - | - | - | ton/año |
| Carga/Descarga | 0,001 | 0,000 | 0,000 | - | - | - | - | - | ton/año |
| Transito camino no<br>pavimentado | 0,719 | 0,138 | 0,033 | - | - | - | - | - | ton/año |
| Transito camino<br>pavimentado | 0,337 | 0,216 | 0,022 | - | - | - | - | - | ton/año |
| Combustión<br>vehículos | 0,005 | 0,005 | 0,005 | 0,234 | 0,000 | 0,000 | 0,058 | 0,010 | ton/año |
| Combustión<br>maquinaría fuera<br>de ruta | 0,010 | 0,010 | 0,010 | 0,230 | 0,005 | 0,001 | 1,208 | 0,072 | ton/año |
| Grupo Electrógeno | 0,041 | 0,041 | 0,014 <br> | 0,590 <br> | 0,039 <br> | - | 0,127 | 0,048 | **ton/año** |

**Tabla 8.: Características Uso de Suelo.****

| Uso de Suelo | Albedob | Col3 | Razón de Bowenc | Col5 | Rugosidad Superficial (cm) | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Uso de Suelo** | **Verano** | **Invierno** | **Verano** | **Invierno** | **Verano** | **Invierno** |
| Bosque Perenne de Coníferas | 0,13 | 0,14 | 0,5 | 0,5 | 50 | 50 |
| Bosque Perenne de latifoliadas | 0,13 | 0,14 | 0,5 | 0,5 | 50 | 50 |
| Bosque deciduo de latifoliada | 0,13 | 0,14 | 0,5 | 0,5 | 50 | 50 |
| Bosque Mixto | 0,13 | 0,14 | 0,5 | 0,5 | 50 | 50 |
| Matorral Cerrado | 0,22 | 0,25 | 1,0 | 1,0 | 10 | 10 |
| Matorral Abierto | 0,20 | 0,24 | 1,0 | 1,0 | 11 | 10 |
| Sabana Arboladas | 0,20 | 0,20 | 1,0 | 1,0 | 15 | 15 |
| Sabanas | 0,20 | 0,20 | 1,0 | 1,0 | 15 | 15 |
| Pastos | 0,18 | 0,23 | 1,0 | 1,0 | 15 | 5 |
| Humedales Permanentes | 0,14 | 0,14 | 0,5 | 0,5 | 20 | 20 |
| Cultivos | 0,18 | 0,23 | 1,0 | 1,0 | 14 | 5 |
| Urbano | 0,18 | 0,18 | 1,5 | 1,5 | 50 | 50 |
| Mosaico de cultivos | 0,18 | 0,23 | 1,0 | 1,0 | 15 | 5 |
| Nieve | 55 | 70 | 0,5 | 0,5 | 5 | 5 |
| Suelo desnudo | 0,25 | 0,25 | 1,0 | 1,0 | 10 | 10 |
| Agua | 0,8 | 0,8 | 0,0 | 0,0 | 1 | 1 |

**Tabla 9.: Localización Puntos Discretos.****

| ID | PUNTOS DE INTERÉS | COORDENADAS UTM<br>(DATUM WGS-84 HUSO 19S) | Col4 |
| --- | --- | --- | --- |
| **ID** | **PUNTOS DE INTERÉS** | **ESTE (m)** | **NORTE (m)** |
| R1 | Vivienda habitacional de un (1) piso, aledaña a ruta H-432 | 330529 | 6208258 |
| R2 | Vivienda habitacional de un (1) piso, aledaña a ruta H-432 y<br>el “Camino a Santa Lucila”<br> | 330566 | 6208193 |
| R3 | ~~Vivienda habitacional de un (1) piso, ubicada al norte del~~<br>Proyecto | 329632 | 6208964 |
| R4 | Vivienda habitacional de dos pisos, ubicada dentro de<br>agrícola, al oeste del Proyecto | 329489 | 6207247 |
| R5 | Oficina de administración (un piso) ubicada dentro de<br>Agrícola Santa Lucila LTDA | 329545 | 6207305 |
| R6 | Vivienda Patronal de dos pisos, ubicada al oeste del Proyecto | 329602 | 6207147 |
| R7 | Vivienda habitacional de un (1) piso, ubicada al oeste del<br>Proyecto | 329747 | 6207052 |
| R8 | Vivienda habitacional de un (1) piso, ubicada al oeste del<br>Proyecto | 329738 | 6206993 |
| R9 | Vivienda habitacional de un (1) piso, ubicada al norte de la<br>Área B del Proyecto | 329983 | 6206909 |
| R10 | Vivienda habitacional de un (1) piso, localizada a un costado<br>de la Ruta H-418, al oeste del Proyecto | 329474 | 6206984 |

**Tabla 11.: Aportes del Proyecto en Puntos de Interés de Gases, Peor Escenario.****

| ID | PUNTOS DE INTERÉS | SO (μg/m3)<br>2 | Col4 | Col5 | Col6 | Col7 | Col8 | NO (μg/m3)<br>2 | Col10 | CO (μg/m3) | Col12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ID** | **PUNTOS DE INTERÉS** | **Primaria** | **Primaria** | **Primaria** | **Secundaria** | **Secundaria** | **Secundaria** | **Primaria** | **Primaria** | **Primaria** | **Primaria** |
| **ID** | **PUNTOS DE INTERÉS** | **Media**<br>**Anual** | **P99**<br>**Diario** | **P98,5**<br>**Horario** | **Media**<br>**Anual** | **P99,7**<br>**Diario** | **P99,73**<br>**Horario** | **Media**<br>**Anual** | **P99**<br>**Horario** | **P99**<br>**8 Horas** | **P99**<br>**Horario** |
| R1 | Vivienda habitacional de un (1) piso,<br>aledaña a ruta H-432 | 0,0166 | 0,0968 | 0,2798 | 0,0166 | 0,1268 | 0,6553 | 0,3240 | 18,8100 | 8,0740 | 34,1430 |
| R2 | Vivienda habitacional de un (1) piso,<br>aledaña a ruta H-432 y el “Camino a Santa<br>Lucila” | 0,0153 | 0,0933 | 0,2561 | 0,0153 | 0,1187 | 0,6606 | 0,2991 | 17,7910 | 7,3916 | 32,0960 |

**Tabla 12.: Puntos de Máxima Concentración (PMC), Peor Escenario.****

| PARÁMETRO | ESTADÍSTICO | PMC | NORMA | UNIDAD | % NORMA | COORDENADAS UTM<br>(WGS84 HUSO 18S) | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **PARÁMETRO** | **ESTADÍSTICO** | **PMC** | **NORMA** | **UNIDAD** | **% NORMA** | **Este (m)** | **Norte (m)** |
| MPS | Promedio del<br>Periodo | 0,10 | 100 | mg/m2-día | 0,1% | 326496 | 6190009 |
| MPS | Promedio<br>mensual | 0,21 | 150 | 150 | 0,1% | 326496 | 6190009 |
| MP10 | Promedio del<br>Periodo | 5,96 | 50 | μg/m3 <br> | 11,9% | 326496 | 6190009 |
| MP10 | Percentil 98<br>Diario | 12,86 | 130 | 130 | 9,9% | 326496 | 6190009 |
| MP2,5 | Promedio del<br>Periodo<br> | 1,81 | 20 | 20 | 9,1% | 326496 | 6190009 |
| MP2,5 | ~~Percentil 98~~<br>Diario | 3,91 | 50 | 50 | 7,8% | 326496 | 6190009 |
| SO2 | Promedio del<br>Periodo | 0,1755 | 60 | 60 | 0,3% | 326496 | 6190009 |
| SO2 | Percentil 99<br>Diario | 0,6499 | 150 | 150 | 0,4% | 326496 | 6190009 |
| SO2 | Percentil<br>98,5 Horario | 1,4166 | 350 | 350 | 0,4% | 326496 | 6190009 |
| SO2 | Promedio del<br>Periodo | 0,1755 | 80 | 80 | 0,2% | 326496 | 6190009 |
| SO2 | Percentil<br>99,7 Diario | 0,6869 | 365 | 365 | 0,2% | 326496 | 6190009 |
| SO2 | Percentil<br>99,73 Horario | 2,049 | 1000 | 1000 | 0,2% | 326496 | 6190009 |
| NO2 | Promedio del<br>Periodo | 4,95 | 100 | 100 | 4,9% | 326496 | 6190009 |
| NO2 | Percentil 99<br>Horario | 46,11 | 400 | 400 | 11,5% | 326496 | 6190009 |
| CO | Percentil 99 8<br>Horas | 35,35 | 10,000 | 10,000 | 0,4% | 326496 | 6190009 |
| CO | Percentil 99<br>Horario | 82,32<br> | 30,000<br> | 30,000<br> | 0,3% | 326496 | 6190009 |

**Tabla 13.: Cronograma Sinérgico.****

| Actividad | Mes | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 | Col14 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Actividad** | dic-<br>24 | ene-<br>25 | feb-<br>25 | mar-<br>25 | abr-<br>25 | may-<br>25 | jun-<br>25 | jul-<br>25 | ago-<br>25 | sept-<br>25 | oct-<br>25 | nov-<br>25 | dic-<br>25 |
| Construcción PFV José Solar |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Operación PFV José Solar |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Construcción PFV Juan Gonzalo<br>Solar |  |  |  |  |  |  |  |  |  |  |  |  |  |

**Tabla 14.: Aportes Escenario sinérgico en Puntos de Interés de Material Particulado.****

| ID | PUNTOS DE INTERÉS | MP (μg/m3)<br>10 | Col4 | MP (μg/m3)<br>2,5 | Col6 | MPS (mg/m2día) | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **ID** | **PUNTOS DE INTERÉS** | **Primaria** | **Primaria** | **Primaria** | **Primaria** | **Secundaria**<br> | **Secundaria**<br> |
| **ID** | **PUNTOS DE INTERÉS** | **Media Anual** | **P98 Diario** | **Media Anual** | **P98 Diario** | **Media Anual** | ~~**Media**~~<br>**Mensual** |
| R1 | Vivienda habitacional de un (1) piso, aledaña a ruta H-432 | 0,3808 | 1,8850 | 0,0996 | 0,5753 | 0,0052 | 0,0096 |
| R2 | Vivienda habitacional de un (1) piso, aledaña a ruta H-432 y el<br>“Camino a Santa Lucila” | 0,3579 | 1,8036 | 0,0932 | 0,5470 | 0,0049 | 0,0091 |
| R3 | Vivienda habitacional de un (1) piso, ubicada al norte del<br>Proyecto | 0,9548 | 3,9732 | 0,2763 | 1,2071 | 0,0139 | 0,0298 |
| R4 | Vivienda habitacional de dos pisos, ubicada dentro de agrícola,<br>al oeste del Proyecto | 1,7582 | 5,6861 | 0,2599 | 0,7868 | 0,0524 | 0,2083 |
| R5 | Oficina de administración (un piso) ubicada dentro de Agrícola<br>Santa Lucila LTDA | 2,1245 | 5,8821 | 0,3151 | 0,8668 | 0,0577 | 0,1588 |
| R6 | Vivienda Patronal de dos pisos, ubicada al oeste del Proyecto<br> | 0,9966 | 3,9418 | 0,1747 | 0,6304 | 0,0199 | 0,0668 |
| R7 | ~~Vivienda habitacional de un (1) piso, ubicada al oeste del~~<br>Proyecto | 0,9178 | 3,6099 | 0,1523 | 0,6022 | 0,0176 | 0,0604 |
| R8 | Vivienda habitacional de un (1) piso, ubicada al oeste del<br>Proyecto | 0,8894 | 3,5392 | 0,1420 | 0,5768 | 0,0202 | 0,0799 |
| R9 | Vivienda habitacional de un (1) piso, ubicada al norte de la Área<br>B del Proyecto<br> | 0,8624 | 3,2150 | 0,1714 | 0,5708 | 0,0118 | 0,0393 |
| R10 | ~~Vivienda habitacional de un (1) piso, localizada a un costado de~~<br>la Ruta H-418, al oeste del Proyecto | 0,6522 | 3,0428 | 0,1252 | 0,4958 | 0,0168 | 0,0920 |

**Tabla 15.: Aportes Escenario sinérgico en Puntos de Interés de Gases.****

| ID | PUNTOS DE INTERÉS | SO (μg/m3)<br>2 | Col4 | Col5 | Col6 | Col7 | Col8 | NO (μg/m3)<br>2 | Col10 | CO (μg/m3) | Col12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ID** | **PUNTOS DE INTERÉS**<br> | **Primaria** | **Primaria** | **Primaria** | **Secundaria** | **Secundaria** | **Secundaria** | **Primaria** | **Primaria** | **Primaria** | **Primaria** |
| **ID** | **PUNTOS DE INTERÉS**<br> | **Media**<br>**Anual** | **P99**<br>**Diario** | **P98,5**<br>**Horario** | **Media**<br>**Anual** | **P99,7**<br>**Diario** | **P99,73**<br>**Horario** | **Media**<br>**Anual** | **P99**<br>**Horario** | **P99**<br>**8 Horas** | **P99**<br>**Horario** |
| R1 | ~~Vivienda habitacional de un (1) piso,~~<br>aledaña a ruta H-432 | 0,0155 | 0,0797 | 0,2163 | 0,0155 | 0,0968 | 0,5505 | 0,2997 | 18,0520 | 8,2171 | 34,5230 |
| R2 | Vivienda habitacional de un (1) piso,<br>aledaña a ruta H-432 y el “Camino a Santa<br>Lucila” | 0,0145 | 0,0745 | 0,2069 | 0,0145 | 0,0933 | 0,5041 | 0,2815 | 17,0320 | 8,0093 | 33,7940 |

**Tabla 16.: Análisis de Cumplimiento de Normativa Escenario sinérgico en Puntos de Interés de Material Particulado.****

| ID | PUNTOS DE INTERÉS | MP (μg/m3)<br>10 | Col4 | MP (μg/m3)<br>2,5 | Col6 | MPS (mg/m2día) | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **ID** | **PUNTOS DE INTERÉS** | **Primaria** | **Primaria** | **Primaria** | **Primaria** | **Secundaria** | **Secundaria** |
| **ID** | **PUNTOS DE INTERÉS** | **Media Anual** | **P98 Diario** | **Media Anual** | **P98 Diario** | **Media Anual** | **Media Mensual** |
| R1 | Vivienda habitacional de un (1) piso, aledaña a<br>ruta H-432 | <1% | 1% | <1% | 1% | <1% | <1% |
| R2 | Vivienda habitacional de un (1) piso, aledaña a<br>ruta H-432 y el “Camino a Santa Lucila” | <1% | 1% | <1% | 1% | <1% | <1% |
| R3 | Vivienda habitacional de un (1) piso, ubicada al<br>norte del Proyecto | 2% | 3% | 1% | 2% | <1% | <1% |
| R4 | Vivienda habitacional de dos pisos, ubicada dentro<br>de agrícola, al oeste del Proyecto | 4% | 4% | 1% | 2% | <1% | <1% |
| R5 | Oficina de administración (un piso) ubicada dentro<br>de Agrícola Santa Lucila LTDA | 4% | 5% | 2% | 2% | <1% | <1% |
| R6 | Vivienda Patronal de dos pisos, ubicada al oeste<br>del Proyecto | 2% | 3% | <1% | 1% | <1% | <1% |
| R7 | Vivienda habitacional de un (1) piso, ubicada al<br>oeste del Proyecto | 2% | 3% | <1% | 1% | <1% | <1% |
| R8 | Vivienda habitacional de un (1) piso, ubicada al<br>oeste del Proyecto | 2% | 3% | <1% | 1% | <1% | <1% |
| R9 | Vivienda habitacional de un (1) piso, ubicada al<br>norte de la Área B del Proyecto | 2% | 2% | <1% | 1% | <1% | <1% |
| R10 | Vivienda habitacional de un (1) piso, localizada a<br>un costado de la Ruta H-418, al oeste del Proyecto | 1% | 2% | <1% | <1% | <1% | <1% |
| **NORMA** | **NORMA** | **50** | **130** | **20** | **50** | **100** | **150** |

**Tabla 17.: Análisis de Cumplimiento de Normativa Aportes Escenario sinérgico en Puntos de Interés de Gases.****

| ID | PUNTOS DE INTERÉS | SO2 (μg/m3) | Col4 | Col5 | Col6 | Col7 | Col8 | NO2 (μg/m3) | Col10 | CO (μg/m3) | Col12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ID** | **PUNTOS DE INTERÉS**<br> | **Primaria** | **Primaria** | **Primaria** | **Secundaria** | **Secundaria** | **Secundaria** | **Primaria** | **Primaria** | **Primaria** | **Primaria** |
| **ID** | **PUNTOS DE INTERÉS**<br> | **Media**<br>**Anual** | **P99**<br>**Diario** | **P98,5**<br>**Horario** | **Media**<br>**Anual** | **P99,7**<br>**Diario** | **P99,73**<br>**Horario** | **Media**<br>**Anual** | **P99**<br>**Horario** | **P99**<br>**8 Horas** | **P99**<br>**Horario** |
| R1 | ~~Vivienda habitacional de un (1) piso, aledaña a~~<br>ruta H-432 | <1% | <1% | <1% | <1% | <1% | <1% | <1% | 5% | <1% | <1% |
| R2 | Vivienda habitacional de un (1) piso, aledaña a<br>ruta H-432 y el “Camino a Santa Lucila” | <1% | <1% | <1% | <1% | <1% | <1% | <1% | 4% | <1% | <1% |
| R3 | Vivienda habitacional de un (1) piso, ubicada al<br>norte del Proyecto | <1% | <1% | <1% | <1% | <1% | <1% | <1% | 6% | <1% | <1% |
| R4 | Vivienda habitacional de dos pisos, ubicada<br>dentro de agrícola, al oeste del Proyecto | <1% | <1% | <1% | <1% | <1% | <1% | <1% | 3% | <1% | <1% |
| R5 | Oficina de administración (un piso) ubicada<br>dentro de Agrícola Santa Lucila LTDA | <1% | <1% | <1% | <1% | <1% | <1% | <1% | 4% | <1% | <1% |
| R6 | Vivienda Patronal de dos pisos, ubicada al oeste<br>del Proyecto | <1% | <1% | <1% | <1% | <1% | <1% | <1% | 4% | <1% | <1% |
| R7 | Vivienda habitacional de un (1) piso, ubicada al<br>oeste del Proyecto | <1% | <1% | <1% | <1% | <1% | <1% | <1% | 4% | <1% | <1% |
| R8 | Vivienda habitacional de un (1) piso, ubicada al<br>oeste del Proyecto | <1% | <1% | <1% | <1% | <1% | <1% | <1% | 3% | <1% | <1% |
| R9 | Vivienda habitacional de un (1) piso, ubicada al<br>norte de la Área B del Proyecto | <1% | <1% | <1% | <1% | <1% | <1% | <1% | 4% | <1% | <1% |
| R10 | Vivienda habitacional de un (1) piso, localizada<br>a un costado de la Ruta H-418, al oeste del<br>Proyecto | <1% | <1% | <1% | <1% | <1% | <1% | <1% | 3% | <1% | <1% |
| **NORMA** | **NORMA** | **60** | **150**<br> | **350**<br> | **80**<br> | **365** | **1000** | **100** | **400** | **10000** | **30000** |

**Tabla 18.: Límites normativos considerados para determinar el área de Influencia del Proyecto.****

| PARÁMETRO | PERIODO EVALUADO | SIL7<br>PORCENTUAL<br>USEPA [%] | RESPECTO DE LA NORMA CHILENA DE CALIDAD<br>DEL AIRE | Col5 |
| --- | --- | --- | --- | --- |
| **PARÁMETRO** | **PERIODO EVALUADO** | **SIL7 **<br>**PORCENTUAL**<br>**USEPA [%]** | **NORMA CHILENA**<br>**(μG/M3) ** | **INCREMENTO SIGNIFICATIVO**<br>**EN LA CONCENTRACIÓN**<br>**(μG/M3) ** |
| SO2 | 1 hora | 4,0% | 350 | 14,0 |
| SO2 | 24 horas | 1,4% | 150 | 2,0 |
| SO2 | Promedio Anual | 2,0% | 60 | 1,2 |
| NO2 | 1 hora | 4,0% | 400 | 16,0 |
| NO2 | Promedio Anual | 1,0% | 100 | 1,0 |
| MP10 | 24 horas | 3,3% | 130 | 5,0 |
| MP10 | Promedio Anual | 2,0% | 50 | 1,0 |
| MP2,5 | 24 horas | 3,4% | 50 | 1,7 |
| MP2,5 | Promedio Anual | 1,7% | 20 | 0,3 |
| CO<br> | 1 hora | 5,0% | 30.000 | 1500,0 |
| CO<br> | 8 horas<br> | 4,9%<br> | 10.000<br> | 488,9<br> |
