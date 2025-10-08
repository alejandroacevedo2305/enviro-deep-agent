---
title: Sin título
author: EMwalnut@outlook.com
date: D:20210609102625-04'00'
language: es
type: report
pages: 58
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - CAPÍTULO 1: INTRODUCCIÓN
  - CAPÍTULO 2: ANÁLISIS DE LA INFORMACIÓN METEOROLÓGICA DE LA ZONA DE ESTUDIO
  - CAPÍTULO 3: IMPLEMENTACIÓN, APLICACIÓN Y RESULTADOS DEL MODELO METEOROLÓGICO WRF DE LA ZONA DE ESTUDIO
  - CAPÍTULO 5: IMPLEMENTACIÓN, APLICACIÓN Y RESULTADOS DEL MODELO DE DISPERSIÓN CALPUFF
  - CAPÍTULO 5: CONCLUSIONES
  - BIBLIOGRAFÍA
-->

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles
en Planta Unifrutti Romeral”.

Ambiente y Energía Industrial

Junio 2021

INFORME FINAL v2

CAPÍTULO 1: INTRODUCCIÓN .................................................................................... 1

CAPÍTULO 2: ANÁLISIS DE LA INFORMACIÓN METEOROLÓGICA DE LA ZONA DE

ESTUDIO ..................................................................................................................... 2

2.1 Introducción ................................................................................................................... 2

2.2 Descripción Climatológica de la Comuna de Romeral ................................................. 2

2.3 Descripción Demográfica y Topográfica de la Comuna de Romeral ........................... 2

2.4 Información Meteorológica de Comuna de Romeral durante el año 2020 .................. 3

2.4.1 Series de Tiempo De Variables Meteorológicas del Año 2020 .................................................... 5

2.4.2 Ciclos Diarios y Estacionales de Variables Meteorológicas del Año 2020 ................................. 6

CAPÍTULO 3: IMPLEMENTACIÓN, APLICACIÓN Y RESULTADOS DEL MODELO
METEOROLÓGICO WRF DE LA ZONA DE ESTUDIO ................................................... 12

3.1 Introducción ................................................................................................................. 12

3.2 Implementación WRF .................................................................................................. 13

3.3 Resultados del modelo WRF en la Comuna de Romeral ............................................ 16

3.3.1 Series de Tiempo de Variables Meteorológicas Modeladas con WRF del año 2020 ............... 16

3.3.2 Ciclos Diarios y Estacionales de Variables Meteorológicas del Año 2020 ............................... 18

3.4 Análisis de Incertidumbre de los Resultados del Modelo WRF Respecto de los Datos
Observados en la Comuna de Romeral Durante el Año 2020 ................................................ 23

3.4.1 Análisis Cualitativo ........................................................................................................................ 24

3.4.2 Análisis Cuantitativo ..................................................................................................................... 28

CAPÍTULO 5: IMPLEMENTACIÓN, APLICACIÓN Y RESULTADOS DEL MODELO DE
DISPERSIÓN CALPUFF ............................................................................................. 29

4.1 Introducción ................................................................................................................. 29

4.2 Implementación y Aplicación del Modelo de Dispersión CALPUFF ........................... 31

4.2.1 Receptores de Grilla y Discretos .................................................................................................. 32

i

4.2.2 Inventario de Emisiones de Olor ................................................................................................... 35

4.3 Resultados de la Aplicación del Sistema CALPUFF.................................................... 40

4.3.1 Resultados Odorantes en Receptores Discretos ........................................................................ 40

4.3.2 Curvas Odorantes .......................................................................................................................... 42

4.3.3 Punto de Máxima Concentración Odorante ................................................................................ 46

4.3.4 Área de Influencia .......................................................................................................................... 46

CAPÍTULO 5: CONCLUSIONES .................................................................................. 48

BIBLIOGRAFÍA .......................................................................................................... 50

ii

Tabla 1: Estaciones Meteorológicas Comuna de Romeral ................................................................. 4

<!-- INICIO TABLA 1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Informe Final v2 y dirección de viento y datos sin variación por más de dos horas en las variables analizadas. -->

**Tabla 1: Estaciones Meteorológicas Comuna de Romeral**

| Estación | Abreviatura | Latitud | longitud | Variables Medidas (%) | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Estación | Abreviatura | Latitud | longitud | VV | DV | T |
| Curicó | CU | -34,97 | -71,23 | 99,4 | 99,4 | 99,4 |

<!-- Estadísticas: 2 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- VV: velocidad de viento; DV: dirección de viento; T: temperatura Figura 2: Ubicación de estación meteorológica Curicó. -->
<!-- FIN TABLA 1 -->


Tabla 2: Configuración de las grillas utilizadas en las corridas del modelo WRF, dominio de

<!-- INICIO TABLA 2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- “Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti Romeral” 13 Informe Final v2 -->

**Tabla 2: Configuración de las grillas utilizadas en las corridas del modelo WRF,**

| Características | Grillas | Col3 |
| --- | --- | --- |
| Características | 1 | 2 |
| N° celdas en dirección E-W | 61 | 61 |
| N° celdas en dirección N-S | 61 | 61 |
| Resolución en dirección E-W | 3.000 m | 1.000 m |
| Resolución en dirección N-S | 3.000 m | 1.000 m |

<!-- Estadísticas: 5 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- El dominio de modelación utilizado del Área de Romeral consideró la grilla N° 2 de WRF, por ser la que posee una resolución con tamaño de grilla de 1000 x 1000 metros para definir la topografía y uso de suelo. Tiene dimensiones de 61 kilómetros en la dirección Este-Oeste y 61 kilómetros en la dirección Norte-Sur, alrededor de su origen ubicado en -->
<!-- FIN TABLA 2 -->

modelación Comuna de Romeral. ........................................................................................ 14

Tabla 3: Características del dominio de modelación de la segunda grilla utilizada por el modelo
WRF en la comuna de Romeral. ............................................................................................ 14

Tabla 4: Configuración de las principales parametrizaciones utilizadas en la modelación con WRF

<!-- INICIO TABLA 4 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Respecto a la configuración del modelo, en relación a la física y dinámica, se consideraron las parametrizaciones del trabajo realizado por SEA, 2012, cuyos principales esquemas son mostrados en la Tabla 4. -->

**Tabla 4: Configuración de las principales parametrizaciones utilizadas en la**

| Variable | Nombre | Esquema | Descripción |
| --- | --- | --- | --- |
| Microfísica | mp_physics | WSM5 | WSM (3 especies microfísicas) |
| Radiación de onda<br>larga | ra_lw_physics | RRTM | Modelo de transferencia<br>radiativa rápida que utiliza<br>tablas de eficiencia. Cuenta con<br>múltiples bandas |

<!-- Estadísticas: 2 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- “Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti Romeral” 15 Informe Final v2 -->
<!-- FIN TABLA 4 -->

para la Comuna de Romeral. ................................................................................................ 15

Tabla 5: Estadísticos Matemáticos de Literatura. ............................................................................. 23

<!-- INICIO TABLA 5 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- observados y modelados. Las fórmulas y rango de estos estadísticos se presentan en Tabla 5. -->

**Tabla 5: Estadísticos Matemáticos de Literatura.**

| Estadístico | Ecuación | Rango |
| --- | --- | --- |
| RMSE | √∑(Mi−Oi)2<br>n<br>n<br>i=1<br> | (0, ∞) |
| BIASN | ∑<br>Mi−Oi<br>n<br>i=1<br>∑<br>Oi<br>n<br>i=1<br> | (-∞,∞) |
| R | 1<br>(1 −n)∑(Mi−M)<br>̅̅̅̅<br>σM<br>N<br>i=1<br>(Oi−O)<br>̅̅̅̅<br>σo<br> | [-1,1] |

<!-- Estadísticas: 3 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia en base a Wilks, 2011. “Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti Romeral” 23 -->
<!-- FIN TABLA 5 -->


Tabla 6: Resultados estadísticos obtenidos de la comparación de datos observados y modelados

<!-- INICIO TABLA 6 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- al inicio de la sección 3.4. Estos son resultados de la comparación entre las series de datos observados y modelados con WRF, extraídos para la estación Curicó, los cuales se presentan en Tabla 6. Estos estadísticos dan una muestra del desempeño del modelo en los puntos geográficos analizados. -->

**Tabla 6: Resultados estadísticos obtenidos de la comparación de datos observados y**

| Estadística | Variable | Unidad | Curicó |
| --- | --- | --- | --- |
| BiasN | VV | m/s | 0,50 |
| BiasN | T | °C | -0,14 |
| RMSE | VV | m/s | 1,34 |
| RMSE | T | °C | 3,33 |
| R | VV | Adimensional | 0,66 |
| R | T | Adimensional | 0,95 |

<!-- Estadísticas: 6 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- VV: velocidad de viento T: temperatura del aire. El modelo sobrestimó levemente los resultados de velocidad de viento, respaldado mediante el índice positivo del BiasN. Respecto a la temperatura, esta fue subestimada. -->
<!-- FIN TABLA 6 -->

con WRF en la estación Curicó ............................................................................................. 28

Tabla 7: Características del dominio de modelación utilizada por el modelo CALPUFF en la
comuna de San Clemente (archivo CALPUFF_Ready). ....................................................... 31

Tabla 8: Características del área de receptores de Grilla. ................................................................ 33

<!-- INICIO TABLA 8 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- “Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti Romeral” 32 Informe Final v2 -->

**Tabla 8: Características del área de receptores de Grilla.**

| Item | Características |
| --- | --- |
| Kilómetros en dirección X | 15,2 |
| Kilómetros en dirección Y | 10,2 |
| Resolución | 200 x 200 (m) |
| No de celdas en dirección X | 76 |
| No de celdas en dirección Y | 51 |
| Coordenadas de referencia del origen del dominio* | UTM-E: 293.027 (m), UTM-N: 6.123.886 (m) |
| Total de receptores | 3.876 |
| Área Total | 155,04 (km2) |

<!-- Estadísticas: 8 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- *: Coordenada de referencia en UTM datum WGS 84 (aproximada), el dominio está en proyección Lambert Conformal Conic (LCC). -->
<!-- FIN TABLA 8 -->


Tabla 9: Receptores discretos. ........................................................................................................... 34

<!-- INICIO TABLA 9 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- En cuanto a los receptores discretos, se consideraron 7 receptores cercanos a la planta de Unifrutti que corresponden a viviendas. Las características de estos receptores, como su ubicación y distancia al proyecto, se presentan en Tabla 9, y en Figura 21 se muestra su ubicación. -->

**Tabla 9: Receptores discretos.**

| Receptor | Coordenadas UTM, WGS 84 - Z19 | Col3 | Altitud (m.s.n.m.) | Distancia al Proyecto*<br>(m) |
| --- | --- | --- | --- | --- |
| Receptor | E (m) | N (m) | N (m) | N (m) |
| R1 | 300.016 | 6.127.638 | 242 | 720 |
| R2 | 300.427 | 6.128.723 | 257 | 740 |
| R3 | 300.107 | 6.129.352 | 254 | 930 |
| R4 | 299.702 | 6.129.156 | 249 | 630 |
| R5 | 299.469 | 6.128.853 | 245 | 368 |
| R6 | 299.209 | 6.128.382 | 244 | 392 |
| R7 | 299.299 | 6.127.809 | 241 | 668 |

<!-- Estadísticas: 8 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- *: Distancia mínima al proyecto: considera la distancia recta entre el receptor y la fuente de olor más cercana del proyecto. -->
<!-- FIN TABLA 9 -->


Tabla 10: Tipos de fuentes y emisiones de olor. ................................................................................. 37

<!-- INICIO TABLA 10 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- correspondientes se obtuvieron las emisiones de olor del proyecto, las que se presentan en Tabla 10. En esta tabla se observa que alcanzan a 186 UO E /s. Estos resultados son conservadores debido a que los factores son considerados como tal y son propios para tratamiento de Riles, además que se considera que todas están al aire libre. -->

**Tabla 10: Tipos de fuentes y emisiones de olor.**

| Fuente | A (m2) | Tipo de fuente | FE (UO /s-m2)<br>E | Emisión (UO /s)<br>E |
| --- | --- | --- | --- | --- |
| Cámara 1 | 1,0 | Fuente difusa pasiva | 9,5 | 9,5 |
| Filtro rotatorio | 6,8 | Fuente difusa pasiva | 7,5 | 50,9 |
| Cámara 2 | 1,0 | Fuente difusa pasiva | 6 | 6,0 |
| Cámara de contención | 1,0 | Fuente difusa pasiva | 6 | 6,0 |
| Decantador | 4,9 | Fuente difusa pasiva | 1,3 | 6,4 |
| Lecho de secado | 6,25 | Fuente difusa pasiva | 8 | 50,0 |
| Decantador | 4,9 | Fuente difusa pasiva | 1,3 | 6,4 |
| Lecho de secado | 6,25 | Fuente difusa pasiva | 8 | 50,0 |
| Cámara monitoreo | 1,0 | Fuente difusa pasiva | 0,6 | 0,6 |
| Descarga canal | 1,0 | Fuente difusa pasiva | 0,6 | 0,6 |
| Total | Total | Total | Total | 186,4 |

<!-- Estadísticas: 11 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- “Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti Romeral” 37 Informe Final v2 -->
<!-- FIN TABLA 10 -->


Tabla 11: Coordenadas de las áreas donde se implementaron las fuentes de olor en el modelo

<!-- INICIO TABLA 11 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- incluyeron las emisiones de todos los procesos unitarios de Tabla 10. Las emisiones se implementaron considerando el peor escenario de emisiones, es decir, con emisiones continuas durante todo el año. -->

**Tabla 11: Coordenadas de las áreas donde se implementaron las fuentes de olor en el**

| Obra<br>Permanente | Superficie<br>(m2) | Puntos | UTM (WGS 84 Z19) | Col5 | LCC (m) | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Obra<br>Permanente | Superficie<br>(m2) | Puntos | Este | Norte | LCC-X | LCC-Y |
| Zona de<br>Pretratamiento | 62 | 1 | 299.694,00 | 6.128.367,00 | -3.839 | -6.264 |
| Zona de<br>Pretratamiento | 62 | 2 | 299.700,00 | 6.128.364,00 | -3.833 | -6.267 |
| Zona de<br>Pretratamiento | 62 | 3 | 299.695,00 | 6.128.358,00 | -3.838 | -6.273 |
| Zona de<br>Pretratamiento | 62 | 4 | 299.689,00 | 6.128.360,00 | -3.844 | -6.271 |

<!-- Estadísticas: 5 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- El detalle de la distribución de las fuentes de área del Proyecto se ilustra en Figura 23. En esta figura se muestran las fuentes consideradas en Google Earth, panel a), y las fuentes implementadas en el modelo CALPUFF en coordenadas LCC. -->
<!-- FIN TABLA 11 -->


CALPUFF. ............................................................................................................................... 38

Tabla 12: Normas de olor holandesa para tratamiento de Riles. ....................................................... 40

<!-- INICIO TABLA 12 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- En Tabla 12 se indican los niveles de molestia de olores de dicha norma. Como el proyecto es existente emplazado en una zona rural se considera como norma de referencia 3,5 UO E /m [3] para el percentil 98 de las concentraciones horarias. -->

**Tabla 12: Normas de olor holandesa para tratamiento de Riles.**

| Tipo de Instalación | Área | Norma (UO /m3)<br>E |
| --- | --- | --- |
| Existente | Urbanas domésticas | Percentil 98: 1,0 |
| Existente | Rurales o sitios industriales | Percentil 98: 3,5 |
| Nuevas | Urbanas domésticas | Percentil 98: 0,5 |
| Nuevas | Rurales o sitios industriales | Percentil 98: 1,5 |

<!-- Estadísticas: 4 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- A continuación, se presentan los resultados de concentraciones odorantes modelados con CALPUFF en la zona de estudio. 4.3.1 Resultados Odorantes en Receptores Discretos -->
<!-- FIN TABLA 12 -->


Tabla 13: Máximo horario, percentil 99,5 y percentil 98 de las concentraciones horarias de olor

<!-- INICIO TABLA 13 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Por otra parte, en Tabla 14 se presenta la cantidad de excedencias horarias de la norma de referencia de 3,5 UO E /m [3], como porcentaje anual y cantidad de horas al año. En esta tabla se observa que en ningún receptor se superó la concentración de 3,5 UO E /m [3] durante el año. -->

**Tabla 13: Máximo horario, percentil 99,5 y percentil 98 de las concentraciones horarias**

| Punto<br>Receptor | Concentración modelada (UO /m3)<br>E | Col3 | Col4 | Límite norma<br>referencia<br>(UO /m3)<br>E | Cumplimiento<br>Normativo |
| --- | --- | --- | --- | --- | --- |
| Punto<br>Receptor | Máximo Horario | Percentil 99,5<br>conc. horarias | Percentil 98<br>conc. horarias | Percentil 98<br>conc. horarias | Percentil 98<br>conc. horarias |
| R1 | 0,03 | 0,01 | 0,00 | 3,5 | Si |
| R2 | 0,09 | 0,06 | 0,03 | 0,03 | Si |
| R3 | 0,05 | 0,03 | 0,01 | 0,01 | Si |
| R4 | 0,09 | 0,05 | 0,02 | 0,02 | Si |
| R5 | 0,06 | 0,03 | 0,02 | 0,02 | Si |
| R6 | 0,06 | 0,03 | 0,02 | 0,02 | Si |
| R7 | 0,03 | 0,01 | 0,01 | 0,01 | Si |

<!-- Estadísticas: 8 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- Tabla 14: Cantidad de excedencias horarias de la norma de referencia (3,5 UO E /m [3] ) en los receptores discretos modelados por el sistema CALPUFF, año 2020. -->
<!-- FIN TABLA 13 -->

modeladas por el sistema CALPUFF, del año 2020. ........................................................... 41

Tabla 14: Cantidad de excedencias horarias de la norma de referencia (3,5 UO E /m [3] ) en los

<!-- INICIO TABLA 14 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |R4|0,09|0,05|0,02|0,02|Si| |R5|0,06|0,03|0,02|0,02|Si| |R6|0,06|0,03|0,02|0,02|Si| |R7|0,03|0,01|0,01|0,01|Si| -->

**Tabla 14: Cantidad de excedencias horarias de la norma de referencia (3,5 UO E /m [3] ) en**

| Punto<br>Receptor | Excedencia de norma | Col3 |
| --- | --- | --- |
| Punto<br>Receptor | (%) | (h/año) |
| R1 | 0,000 | 0 |
| R2 | 0,000 | 0 |
| R3 | 0,000 | 0 |
| R4 | 0,000 | 0 |
| R5 | 0,000 | 0 |
| R6 | 0,000 | 0 |
| R7 | 0,000 | 0 |

<!-- Estadísticas: 8 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- “Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti Romeral” 41 Informe Final v2 -->
<!-- FIN TABLA 14 -->

receptores discretos modelados por el sistema CALPUFF, año 2020. ............................. 41

Tabla 15: Máximo horario, percentil 99,5 y percentil 98 de las concentraciones horarias de olor en

<!-- INICIO TABLA 15 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Como se observa en Figura 24 a Figura 26, las máximas concentraciones odorantes se presentan en una zona cercana al área de riego oeste del Proyecto. Las concentraciones de olor y ubicación del Punto de Máxima Concentración Odorante se presentan en Tabla 15. -->

**Tabla 15: Máximo horario, percentil 99,5 y percentil 98 de las concentraciones horarias**

| de olor en el Punto de Máxima Concentración Odorante. | Col2 | Col3 |
| --- | --- | --- |
| Punto de Máxima Concentración | Punto de Máxima Concentración | Punto de Máxima Concentración |
| Máximo Horario (UOE/m3) | Máximo Horario (UOE/m3) | 1,2 |
| Percentil 99,5 concentraciones horarias (UOE/m3) | Percentil 99,5 concentraciones horarias (UOE/m3) | 0,66 |
| Percentil 98 concentraciones horarias (UOE/m3) | Percentil 98 concentraciones horarias (UOE/m3) | 0,38 |
| Ubicación | LCC-X (m) | -3.900 |
| Ubicación | LCC-Y (m) | -6.300 |
| Ubicación | UTM-E WGS 84 - Z19 (m) | 299.634 |
| Ubicación | UTM-N WGS 84 - Z19 (m) | 6.128.330 |

<!-- Estadísticas: 8 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- 4.3.4 Área de Influencia El Área de Influencia por dispersión de olor se presenta en Figura 27. Esta área es muy conservadora dado que fue obtenida a partir de la zona que cubre la isolínea de -->
<!-- FIN TABLA 15 -->

el Punto de Máxima Concentración Odorante. ................................................................... 46

iii

Figura 1: Topografía Área de Romeral. .................................................................................................. 3

Figura 2: Ubicación de estación meteorológica Curicó........................................................................ 4

Figura 3: Series de tiempo de variables meteorológicas. .................................................................... 5

Figura 4: Diagramas de Caja y Bigotes variables meteorológicas observados en estación Curicó. 6

Figura 5: Ciclos diarios de velocidad y dirección de viento y temperatura observados en estación
Curicó. ...................................................................................................................................... 8

Figura 6: Ciclos estacionales de velocidad y dirección de viento y temperatura observados en
estación Curicó. ..................................................................................................................... 10

Figura 7: Rosas de viento observadas en estación Curicó. ............................................................... 11

Figura 8: Diagrama de operación del modelo meteorológico WRF. .................................................. 13

Figura 9: Dominios de modelación de WRF......................................................................................... 15

Figura 10: Series de tiempo de velocidad de viento y temperatura modelado en la estación Curicó.

................................................................................................................................................ 17

Figura 11: Diagramas de Caja y Bigotes de velocidad de viento y temperatura modelado en la
estación Curicó. ..................................................................................................................... 17

Figura 12: Ciclos diarios de velocidad y dirección del viento y temperatura modelados con WRF en
la estación Curicó. ................................................................................................................. 19

Figura 13: Ciclos estacionales de velocidad y dirección del viento y temperatura modelado con WRF
en la estación Curicó. ............................................................................................................ 21

Figura 14: Rosas de Vientos modeladas con WRF en la estación Curicó ........................................... 22

Figura 15: Comparación de ciclos diarios de velocidad y dirección del viento y temperatura
observados y modelados con WRF en estación Curicó. .................................................... 25

Figura 16: Comparación de ciclos estacionales de velocidad y dirección del viento y temperatura
observados y modelados con WRF en estación Curicó. .................................................... 26

Figura 17: Comparación de Rosas de Viento observadas y modeladas con WRF en estación Curicó.

................................................................................................................................................ 27

Figura 18: Diagrama de operación del sistema de modelación WRF/CALPUFF/CalDesk. ................ 30

Figura 19: Dominio de modelación de CALPUFF, 50 x 50 km [2], en coordenadas LCC. ....................... 32

Figura 20: Área de receptores de grilla de CALPUFF, 15 x 10 km [2], en coordenadas LCC. ................. 33

Figura 21: Ubicación de Receptores discretos. .................................................................................... 35

Figura 22: Esquema del sistema de acondicionamiento de Riles de Planta Unifrutti Romeral. ....... 36

iv

Figura 23: Distribución de fuentes emisoras de olor de sistema de tratamiento de Riles de planta
Unifrutti. a) Fuentes en Google Earth, b) Fuentes implementadas en CALPUFF, en
coordenadas LCC. ................................................................................................................. 39

Figura 24: Mapa de curvas isodoras de concentraciones máximas horarias del año 2020 modelados
con CALPUFF en la zona de estudio. ................................................................................... 43

Figura 25: Mapa de curvas isodoras percentil 99,5 de las concentraciones horarias del año 2020
modelados con CALPUFF en la zona de estudio. ............................................................... 44

Figura 26: Mapa de curvas isodoras percentil 98 de las concentraciones horarias del año 2020
modelados con CALPUFF en la zona de estudio. ............................................................... 45

Figura 27: Área de Influencia por dispersión de olor. ........................................................................... 47

v

# CAPÍTULO 1: INTRODUCCIÓN

En este documento EnviroModeling Spa. presenta el Informe Final correspondiente al:
“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta

Unifrutti Romeral”.

El objetivo de este estudio consiste en evaluar el impacto en la generación de olores
debido a la operación del Sistema de tratamiento de Riles en planta Unifrutti Comuna de

Romeral Chile.

Para el logro de este objetivo, en primer lugar, se corrió el modelo meteorológico
Weather Research and Forecast Model (WRF) en modo diagnóstico para obtener la
meteorología de la zona de comuna de Romeral, Talca Chile.

En segundo lugar, se realizó la modelación de dispersión de olores que consideran las
emisiones de la misma especie, para obtener el impacto de estas en la calidad del aire
del área circundante al Proyecto. Esto se llevó a cabo con el uso del sistema de
modelación WRF/CALPUFF, recomendado por el SEA y EPA (USA) para emisiones en
terreno complejo. Este sistema se aplicó considerando los siguientes escenarios
meteorológico, topográfico y de emisiones:

Escenario Meteorológico: Corresponde al año 2020.

- Escenario Topográfico: La zona de estudio considera un área de 50 x 50 km [2],
cubriendo la zona del Proyecto, incluyendo la comuna de Romeral.

Escenarios de Emisiones Considera las emisiones de olor debido a los procesos del

sistema de tratamiento de Riles.

En el siguiente Capítulo de este documento se presenta la descripción de la información
meteorológica del proyecto en la zona de estudio. En el Capítulo 3 se presenta la
implementación, aplicación y resultados del modelo meteorológico WRF. En Capítulo 4
se presenta la implementación, aplicación y resultados del modelo de dispersión
CALPUFF. Finalmente, las conclusiones del estudio se presentan en el Capítulo 5.

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti
Romeral” 1

Informe Final v2

# CAPÍTULO 2: ANÁLISIS DE LA INFORMACIÓN METEOROLÓGICA DE LA ZONA DE ESTUDIO

## 2.1 Introducción

A continuación, se presenta una descripción de la zona donde se emplaza la Planta
Unifrutti en la Comuna de Romeral, considerando aspectos tales como: clima,
características topográficas y meteorología.

## 2.2 Descripción Climatológica de la Comuna de Romeral

El clima donde se encuentra emplazada la comuna de Romeral corresponde al tipo
“mediterráneo con diferencias en sentido norte-sur, es una estación seca de seis meses
en el norte, a cuatro meses en el sur. La temperatura media es de 19 °C y con extremas
de 30 °C, durante el periodo de verano; en cambio en invierno las temperaturas mínimas
medias son de 7 °C. Este clima comienza a cambiar a medida que se asciende hacia la
precordillera hasta aproximadamente los 2.000 m presentando un descenso en
temperaturas y aumento en las precipitaciones (Insunza, 2012).

## 2.3 Descripción Demográfica y Topográfica de la Comuna de Romeral

La comuna de Romeral (-34,93° S, -71,32° W) tiene una población de 15.187 habitantes
correspondiente al 1,45% del total de la región y al 0,09% del total país (INE, 2017). El
relieve corresponde a un valle longitudinal que se encuentra emplazado entre la
precordillera y la Cordillera de la Costa, alcanzando un ancho de 40 km frente a Linares
con un largo de 170 km. Es de tipo plano y se encuentra interrumpido por numerosos
ríos de sentido este-oeste.

La topografía del área de Romeral se muestra en Figura 1.

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti
Romeral” 2

Informe Final v2

[Fuente: https://es-uy.topographic-map.com/.](https://es-uy.topographic-map.com/)

Figura 1: Topografía Área de Romeral.

## 2.4 Información Meteorológica de Comuna de Romeral durante el año 2020

La red meteorológica en el dominio de interés utilizada corresponde a la estación de
nombre Curicó, la cual pertenece a la Red del Sistema de Información nacional de
Calidad del Aire (SINCA) que actualmente se encuentra en operación en el dominio de
interés. Su ubicación se muestra en Figura 2.

En Tabla 1 se presenta la información acerca de la ubicación y porcentaje de datos
válidos de las variables meteorológicas velocidad y dirección del viento y temperatura
registrada en la estación de monitoreo mencionada anteriormente, durante el periodo
enero - diciembre del año 2020.

Los datos fueron revisados y validados siguiendo los lineamientos de la EPA, en relación
a registros incoherentes y datos sin variación en una cierta cantidad de horas. Esto
significa que fueron descartados registros negativos como por ejemplo en la velocidad

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti
Romeral” 3

Informe Final v2

y dirección de viento y datos sin variación por más de dos horas en las variables
analizadas.

Tabla 1: Estaciones Meteorológicas Comuna de Romeral

|Estación|Abreviatura|Latitud|longitud|Variables Medidas (%)|Col6|Col7|
|---|---|---|---|---|---|---|
|Estación|Abreviatura|Latitud|longitud|VV|DV|T|
|Curicó|CU|-34,97|-71,23|99,4|99,4|99,4|

VV: velocidad de viento; DV: dirección de viento; T: temperatura

Figura 2: Ubicación de estación meteorológica Curicó.

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti
Romeral”
4

Informe Final v2

2.4.1 Series de Tiempo De Variables Meteorológicas del Año 2020

Las series de tiempo de velocidad de viento y temperatura de la estación Curicó se
presentan en Figura 3. De estas series de tiempo se desprende la integridad de los datos
en las estaciones, donde no se aprecia pérdida significativa de datos, lo cual es un buen
indicativo de la representatividad de la estacionalidad del año con fines de análisis y
representatividad de la meteorología local.

En términos generales, la variable temperatura presenta sus máximos de magnitud en
el periodo de verano, mientras que los mínimos son en invierno.

Figura 3: Series de tiempo de variables meteorológicas.

Los registros de velocidad de viento muestran valores máximos en verano y mínimos
en invierno, estos representados por los extremos y por la posición del rango
intercuartílico representado por la caja central. En verano la posición es superior
respecto a los meses de invierno.

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti
Romeral”
5

Informe Final v2

En invierno, se aprecian extremos anómalos de velocidad de viento, representados por
los puntos rojos, los cuales pueden representar ráfagas asociadas a frentes fríos típicos
de la estación de invierno en Chile Central.

Respecto a la temperatura, los registros muestran la disminución de los cuartiles 1 y 3
y sus respectivos valores atípicos en los meses de invierno. Adicionalmente, la
variabilidad también disminuye en esta misma temporada. En el periodo estival, ocurre
lo inverso, visualizándose un aumento en las temperaturas máximas y mínimas y en la
amplitud térmica expresada por los cuartiles 1 y 3 de la caja central, llegando casi a los
30 °C.

Figura 4: Diagramas de Caja y Bigotes variables meteorológicas observados en
estación Curicó.

2.4.2 Ciclos Diarios y Estacionales de Variables Meteorológicas del Año 2020

Los ciclos diarios son construidos en base a los registros promedios de cada hora del
día, con el fin de mostrar un comportamiento patrón de una cierta variable, en este caso

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti
Romeral” 6

Informe Final v2

meteorológica. El área sombreada corresponde al área delimitada por los percentiles 5
y 95, el cual tiene como objetivo mostrar la amplitud de cada variable.

En la Figura 5 se muestran los ciclos diarios típicos de las variables, donde la velocidad
de viento y la temperatura presentan un alza de la magnitud en el periodo diurno y una
disminución en el nocturno. Esto es documentando en Stull, 1988, indicando que a
medida que el aire circundante del suelo es calentado por la superficie terrestre con los
primeros rayos del sol, se inicia la producción convectiva de energía cinética turbulenta,
produciendo turbulencia atmosférica, y un aumento en la altura de la capa límite
atmosférica, fuertes movimientos verticales, aumento de la velocidad de viento y la
temperatura.

Respecto al ciclo de la dirección de viento se visualiza un leve cambio en el periodo
nocturno respecto al diurno. En el primero, un 30% de las muestras indican dirección
predominante sur, mientras que a partir de las 10:00 horas hasta las 19:00 horas, la
dirección cambia a suroeste, con un 40% de las frecuencias.

Las rosas de vientos, coinciden respecto a lo mostrado por el ciclo diario, donde se
visualiza mayoritariamente el viento de componente sur en la noche, mientras que en el
día la dirección se inclina hacia vientos provenientes desde el suroeste (Figura 7)

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti
Romeral”
7

Informe Final v2

Figura 5: Ciclos diarios de velocidad y dirección de viento y temperatura observados
en estación Curicó.

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti
Romeral” 8

Informe Final v2

En la Figura 6 se muestran los ciclos estacionales de velocidad y dirección de viento en
la figura superior y temperatura en la figura inferior, del año 2020, en la estación Curicó.

El ciclo estacional consiste en un gráfico donde se muestra el ciclo diario en el eje x y el
ciclo anual en el eje y. Los colores muestran la magnitud de la variable, donde el color
rojo muestra valores máximos y los colores azules los mínimos. Además,
particularmente en el ciclo estacional de velocidad de viento se superponen vectores de
viento en el mapa de colores, con la finalidad de mostrar la dirección de viento
predominante promedio a lo largo del día y del año.

Respecto a la velocidad de viento, los registros muestran valores máximos en el periodo
diurno y periodo estival. Lo contrario ocurre en invierno y en las noches, donde los
vientos presentan una tendencia más bien de características de brisa tipo “calma”.

La dirección del viento muestra un viento predominante sur a lo largo del año,
exceptuando los meses de junio y julio, cuya dirección cambia a componente este en la
noche y norte durante el día, probablemente debido a sistemas frontales que se
presentan en la zona en dicho periodo (Figura 6).

Finalmente, la temperatura muestra magnitudes máximas en verano y en el periodo
diurno cercanas a los 30 °C, mientras que en invierno y en el periodo nocturno se
presentan temperaturas mínimas cercanas a los 0 °C (Figura 6).

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti
Romeral” 9

Informe Final v2

Figura 6: Ciclos estacionales de velocidad y dirección de viento y temperatura
observados en estación Curicó.

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti
Romeral” 10

Informe Final v2

Figura 7: Rosas de viento observadas en estación Curicó.

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti
Romeral” 11

Informe Final v2

# CAPÍTULO 3: IMPLEMENTACIÓN, APLICACIÓN Y RESULTADOS DEL MODELO METEOROLÓGICO WRF DE LA ZONA DE ESTUDIO

## 3.1 Introducción

En este Capítulo se presenta la implementación y aplicación del modelo meteorológico
WRF v4.1.5 (Weather Research and Forecasting Model). WRF es uno de los modelos
meteorológicos de pronóstico más avanzados y completos. El modelo ofrece una
amplia gama de aplicaciones meteorológicas a través de escalas de decenas de metros
a miles de kilómetros.

WRF ofrece pronósticos operativos mediante una plataforma flexible y
computacionalmente eficiente, al tiempo que proporciona los últimos avances en la
física, numéricos y de asimilación de datos aportados por los desarrolladores a través
de una amplia comunidad de investigación.

El modelo obtiene sus condiciones de borde de datos históricos globales del clima que
son mantenidos por centros operacionales de pronóstico del tiempo. Estos datos
globales representan el estado completo de la atmósfera en todo el planeta y son
resultado de análisis informáticos sofisticados de datos superficiales disponibles y de
observaciones a niveles más altos. Cada período de análisis combina decenas de miles
de mediciones individuales tomadas en todo el globo terrestre.

Para poder incorporar la gama completa de fenómenos meteorológicos que ocurren en
la atmósfera real el modelo utiliza una configuración de grillas anidadas. El alcance de
la grilla más gruesa es seleccionado para capturar el efecto de los fenómenos de la
escala sinóptica dentro de la región de interés, mientras que la grilla más fina permite
que el modelo desarrolle circulaciones regionales relacionadas con la interacción de la
atmósfera con la topografía.

En Figura 8 se presenta un diagrama de operación del modelo WRF. Como se observa
en esta figura, este sistema considera como información de entrada meteorología del
sistema GFS y/o datos de estaciones meteorológicas locales, además de topografía y
uso de suelos. Con los archivos de salida del modelo se puede obtener un archivo
formato tipo CALMET, el cual sirve de entrada para el modelo CALPUFF.

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti
Romeral” 12

Informe Final v2

Figura 8: Diagrama de operación del modelo meteorológico WRF.

## 3.2 Implementación WRF

En esta sección se presenta la implementación y aplicación del modelo meteorológico
WRF para la generación de la meteorología requerida por el modelo CALPUFF para el
año 2020.

El modelo se implementó con dos grillas anidadas en la zona de Romeral. Las
condiciones de borde e iniciales de los datos históricos del año 2020 fueron
proporcionadas por GDAS de NOAA (National Oceanic and Atmospheric Administration),
de USA, con una resolución espacial de 0,25 grados. Las características de la
configuración de las grillas anidadas se presentan en Tabla 2.

Respecto a la topografía del dominio de modelación fue obtenida a partir del proyecto
SRTM (del acrónimo inglés Shuttle Radar Topography Mission) con resolución de 3
segundos de grado (90 m aproximadamente) y el uso de suelo a partir de la información
satelital MODIS (del acrónimo inglés Moderate-Resolution Imaging Spectroradiometer)
de la NASA con resolución de 15 segundos de grado.

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti
Romeral” 13

Informe Final v2

Tabla 2: Configuración de las grillas utilizadas en las corridas del modelo WRF,
dominio de modelación Comuna de Romeral.

|Características|Grillas|Col3|
|---|---|---|
|Características|1|2|
|N° celdas en dirección E-W|61|61|
|N° celdas en dirección N-S|61|61|
|Resolución en dirección E-W|3.000 m|1.000 m|
|Resolución en dirección N-S|3.000 m|1.000 m|

El dominio de modelación utilizado del Área de Romeral consideró la grilla N° 2 de WRF,
por ser la que posee una resolución con tamaño de grilla de 1000 x 1000 metros para
definir la topografía y uso de suelo. Tiene dimensiones de 61 kilómetros en la dirección
Este-Oeste y 61 kilómetros en la dirección Norte-Sur, alrededor de su origen ubicado en
los -34,97494358 latitud Sur y -71,23395418 longitud Oeste.

Las características generales de esta grilla se presentan en Tabla 3 y los dominios
modelados se muestran en Figura 9.

|bla 3: Características del dominio de modelación de la segunda grilla utilizada el modelo WRF en la comuna de Romeral.|Col2|
|---|---|
|Características Grilla 2 de WRF|Características Grilla 2 de WRF|
|Resolución|1.000 x 1.000 (m)|
|No de celdas en dirección X|61|
|No de celdas en dirección Y|61|
|Coordenadas del origen del dominio|Latitud: -34,9749; Longitud: -71,2339|
|Total del área del dominio|3721 (km2)|

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti
Romeral” 14

Informe Final v2

Figura 9: Dominios de modelación de WRF.

Respecto a la configuración del modelo, en relación a la física y dinámica, se
consideraron las parametrizaciones del trabajo realizado por SEA, 2012, cuyos
principales esquemas son mostrados en la Tabla 4.

Tabla 4: Configuración de las principales parametrizaciones utilizadas en la
modelación con WRF para la Comuna de Romeral.

|Variable|Nombre|Esquema|Descripción|
|---|---|---|---|
|Microfísica|mp_physics|WSM5|WSM (3 especies microfísicas)|
|Radiación de onda<br>larga|ra_lw_physics|RRTM|Modelo de transferencia<br>radiativa rápida que utiliza<br>tablas de eficiencia. Cuenta con<br>múltiples bandas|

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti
Romeral” 15

Informe Final v2

|Variable|Nombre|Esquema|Descripción|
|---|---|---|---|
|Radiación de onda<br>corta|ra_sw_physics|Dudhia scheme|Integración simple que permite<br>la absorción y dispersión por<br>nubes y a cielo despejado|
|Capa superficial|sf_sfclay_physics|MM5|Monin-Obukhov similaridad|
|Superficie|sf_surface_physcis|Thermal Diffusion<br>Scheme|Esquema de difusión termal|
|Capa límite<br>planetaria|bl_pbl_physics|YSU scheme|QNSE|

## 3.3 Resultados del modelo WRF en la Comuna de Romeral

En la presente sección se muestran los resultados del modelo meteorológico WRF. Los
resultados obtenidos provienen de las variables extraídas de las coordenadas de las
estaciones de la red meteorológica presentadas en la sección 2.4 del presente informe
(Tabla 1).

3.3.1 Series de Tiempo de Variables Meteorológicas Modeladas con WRF del año 2020

Las series de tiempo de velocidad de viento y temperatura modeladas con WRF para el
año 2020 en la estación Curicó de la zona de la Comuna de Romeral se presentan en la
Figura 10. En esta figura se aprecia que el modelo WRF simula el típico aumento de la
temperatura en los meses de verano y la disminución en el periodo invernal en ambas
estaciones. La velocidad de viento presenta una alta variabilidad, profundizada en los
meses de invierno, probablemente debido al paso de sistemas frontales.

Por otra parte, en la Figura 11 se muestran los gráficos de diagrama de caja y bigotes
de velocidad de viento y temperatura en la estación Curicó para el año 2020. La
velocidad de viento modelada muestra valores atípicos en todos los meses del año,
visualizados en los meses de invierno, sobre los 10 m/s. La variabilidad también
aumenta en los meses de invierno indicado por los extremos de la caja de 1 m/s y 3 m/s.

La temperatura, muestra valores atípicos que aparecen en invierno cercano a los 20°C y
una variabilidad reducida aproximada de 5 °C indicado por los extremos de la caja en el
mismo periodo invernal. En verano las temperaturas máximas aumentan a 30 °C,
mientras que la amplitud es cercana a los 10 °C.

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti
Romeral” 16

Informe Final v2

Figura 10: Series de tiempo de velocidad de viento y temperatura modelado en la

estación Curicó.

Figura 11: Diagramas de Caja y Bigotes de velocidad de viento y temperatura

modelado en la estación Curicó.

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti
Romeral” 17

Informe Final v2

3.3.2 Ciclos Diarios y Estacionales de Variables Meteorológicas del Año 2020

Los ciclos diarios de velocidad y dirección de viento y temperatura en la estación Curicó
del año 2020 modelados con WRF en la Comuna de Romeral se presentan en Figura 12.
Por otra parte, los ciclos estacionales modelados para estas mismas variables se
presentan en Figura 13.

Los ciclos diarios de velocidad de viento simulados con WRF, mostrados en Figura 12
indican el cambio de magnitud entre periodo nocturno y diurno visualizado por el
crecimiento del área sombreada y el promedio durante el día expresada en la línea
continua. Respecto a la variabilidad, la simulación muestra que esta es máxima en el
día, mientras que en la noche se aprecian condiciones de calma.

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti
Romeral” 18

Informe Final v2

Figura 12: Ciclos diarios de velocidad y dirección del viento y temperatura modelados

con WRF en la estación Curicó.

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti
Romeral” 19

Informe Final v2

Respecto a la dirección de viento el modelo reproduce un viento de dirección sur con un
30% de las frecuencias en el periodo nocturno, mientras que en el día la componente
Respecto a la dirección de viento, el viento proveniente dominante es sur en el periodo
nocturno, mientras que en el día se modifica a suroeste en un rango entre 30% y 40% de
las muestras. En la transición vespertina se reproduce un viento de componente norte.
Las rosas de viento respaldan lo indicado en el ciclo de diario de dirección de viento,
mostrando las mismas tendencias en los periodos analizados, logrando presenciar una
componente única en el periodo nocturno y suroeste en el día (Figura 14).

La temperatura muestra el típico estándar día y noche con el crecimiento y disminución
de la magnitud de la variable lo que sería aceptable acorde a las observaciones
mostradas en la Figura 5.

Lo descrito es reforzado con las figuras de los ciclos estacionales en estación Curicó
(Figura 13) donde se visualiza que el modelo logra capturar el patrón diario en cada
variable, visualizando el eje “y” de cada gráfico, y además el estándar anual, con
máximos de magnitud en el periodo estival como es el caso para la temperatura y
mínimos en el invernal.

Respecto a la velocidad de viento, el modelo muestra el fortalecimiento de esta variable
en el periodo desde la transición de primavera hasta diciembre. La dirección de viento
es modelada a lo largo del año con una componente dominante sur y suroeste,
exceptuando los meses de junio y julio donde la componente cambia a noreste, lo que
podría ser un atisbo de la captura de sistemas frontales en Chile Centro-Sur.

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti
Romeral” 20

Informe Final v2

Figura 13: Ciclos estacionales de velocidad y dirección del viento y temperatura

modelado con WRF en la estación Curicó.

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti
Romeral” 21

Informe Final v2

Figura 14: Rosas de Vientos modeladas con WRF en la estación Curicó

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti
Romeral” 22

Informe Final v2

## 3.4 Análisis de Incertidumbre de los Resultados del Modelo WRF Respecto de los Datos Observados en la Comuna de Romeral Durante el Año 2020

En esta sección se analiza el nivel de incertidumbre del modelo meteorológico WRF, de
forma cualitativa mediante la comparación de gráficos, de ciclos diarios y estacionales
y de forma cuantitativa, mediante estadísticos matemáticos obtenidos por comparación
entre los datos horarios de las observaciones y los resultados simulados con WRF.

Los estadísticos matemáticos calculados son los siguientes:

Error cuadrático medio (RMSE): entrega el grado de precisión entre los datos

pronosticados y observados.

Sesgo normalizado (BIASN): entrega el sesgo entre las series modeladas y

observadas.

Coeficiente de correlación (R): entrega el grado de relación lineal entre los datos

observados y modelados.

Las fórmulas y rango de estos estadísticos se presentan en Tabla 5.

Tabla 5: Estadísticos Matemáticos de Literatura.

|Estadístico|Ecuación|Rango|
|---|---|---|
|RMSE|√∑(Mi−Oi)2<br>n<br>n<br>i=1<br>|(0, ∞)|
|BIASN|∑<br>Mi−Oi<br>n<br>i=1<br>∑<br>Oi<br>n<br>i=1<br>|(-∞,∞)|
|R|1<br>(1 −n)∑(Mi−M)<br>̅̅̅̅<br>σM<br>N<br>i=1<br>(Oi−O)<br>̅̅̅̅<br>σo<br>|[-1,1]|

Fuente: Elaboración propia en base a Wilks, 2011.

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti
Romeral” 23

Informe Final v2

3.4.1 Análisis Cualitativo

En la Figura 15 y Figura 16 se presenta la comparación de los ciclos diarios y
estacionales observados a la izquierda y modelados a la derecha con WRF, de las
variables velocidad y dirección de viento y temperatura durante el año 2020 en la
estación Curicó.

Describiendo los ciclos diarios, en términos generales el modelo logra capturar los
ciclos diarios de las variables observadas en la estación mostrada en estación Curicó.
En particular, la variabilidad de la velocidad de viento es sobrestimada siguiendo el área
sombreada compuesta por los percentiles 5 y 95, en las estaciones mostradas, al igual
que la magnitud.

Respecto a la dirección de viento existe un sesgo de la componente nor-oeste, la cual
no es registrada por las observaciones en estación Curicó en la transición vespertina,
sin embargo, en términos generales el modelo simula bien la dirección.

Las rosas de viento coinciden en la aceptable reproducción de los patrones de dirección
de viento a lo largo del ciclo. Solo se visualiza la sobrestimación del escalar de la
variable y la exageración en la frecuencia de vientos dominantes como son sur y
suroeste (Figura 18).

Respecto a los ciclos estacionales, el modelo (Cuadro Derecha) muestra un buen
desempeño en términos cualitativos en las variables presentadas en estación Curicó.

Analizando la dirección de viento, el modelo logra capturar los patrones de mesoescala
del punto de interés. Esto se traduce en la reproducción de los vientos de tipo suroeste
a lo largo del año y en el cambio de dirección de viento a componente noreste en los
meses de junio y julio. Sin embargo, presenta una anomalía en el periodo diurno del mes
de agosto, donde el modelo reproduce una componente noreste la cual no es vista en
las observaciones.

Respecto a la velocidad de viento el modelo reproduce parcialmente el ciclo estacional
y diario de la variable. La sobrestimación del modelo se muestra en todos los periodos
del ciclo diario y estacional.

La temperatura fue correctamente simulada logrando reproducir el ciclo diario y anual
de la variable. También se visualiza que, en promedio, la magnitud es bastante
aproximada respecto a las observaciones.

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti
Romeral” 24

Informe Final v2

Observados Modelados

Figura 15: Comparación de ciclos diarios de velocidad y dirección del viento y

temperatura observados y modelados con WRF en estación Curicó.

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti
Romeral” 25

Informe Final v2

Observados Modelados

Figura 16: Comparación de ciclos estacionales de velocidad y dirección del viento y

temperatura observados y modelados con WRF en estación Curicó.

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti
Romeral” 26

Informe Final v2

Observadas Modeladas

Figura 17: Comparación de Rosas de Viento observadas y modeladas con WRF en estación Curicó.

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti Romeral”

27
Informe Final v2

3.4.2 Análisis Cuantitativo

El análisis cuantitativo es realizado mediante la utilización de los estadísticos descritos
al inicio de la sección 3.4. Estos son resultados de la comparación entre las series de
datos observados y modelados con WRF, extraídos para la estación Curicó, los cuales
se presentan en Tabla 6. Estos estadísticos dan una muestra del desempeño del modelo
en los puntos geográficos analizados.

Tabla 6: Resultados estadísticos obtenidos de la comparación de datos observados y
modelados con WRF en la estación Curicó

|Estadística|Variable|Unidad|Curicó|
|---|---|---|---|
|BiasN|VV|m/s|0,50|
|BiasN|T|°C|-0,14|
|RMSE|VV|m/s|1,34|
|RMSE|T|°C|3,33|
|R|VV|Adimensional|0,66|
|R|T|Adimensional|0,95|

VV: velocidad de viento T: temperatura del aire.

El modelo sobrestimó levemente los resultados de velocidad de viento, respaldado
mediante el índice positivo del BiasN. Respecto a la temperatura, esta fue subestimada.

Respecto al RMSE, estos valores fueron de baja magnitud, en cada variable, indicando
que la precisión del modelo fue bastante aceptable

Finalmente, respecto a la relación entre datos observados y modelados, todas las
variables presentan una buena correlación, de 0,66 hacia arriba, siendo la de menor
desempeño la velocidad de viento y la de mejor, la temperatura.

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti
Romeral” 28

Informe Final v2

# CAPÍTULO 5: IMPLEMENTACIÓN, APLICACIÓN Y RESULTADOS DEL MODELO DE DISPERSIÓN CALPUFF

## 4.1 Introducción

La dispersión de olores debido a la operación del sistema de acondicionamiento de Riles
de la planta Unifrutti Romeral se obtuvo mediante la modelación con el sistema
WRF/CALPUFF.

El sistema de modelación CALPUFF, está actualmente aprobado por el Servicio de
Evaluación Ambiental (SEA) de Chile y por la EPA (USA) como modelo regulatorio para
evaluar el impacto de emisiones atmosféricas en escenarios de terreno y meteorología
compleja. Este sistema está compuesto por los modelos WRF y CALPUFF, cuya
descripción general es la siguiente:

WRF: Modelo de mesoescala y micrometeorológico capaz de generar la
meteorología requerida por el modelo CALPUFF, para la evaluación de
contaminantes primarios.

CALPUFF: Modelo lagrangiano de dispersión tipo puff que permite simular el
transporte, dispersión e impacto de emisiones de contaminantes primarios de
procesos naturales y antropogénicos, utilizando la meteorología generada por WRF.

El análisis de resultados de los modelos WRF y CALPUFF se realiza con el software
CalDESK Advanced v2.98 [1] . Esta herramienta permite generar mapas de
isoconcentraciones de contaminantes y visualizar los resultados de todas las variables
entregadas por los modelos.

En Figura 18 se presenta un diagrama del sistema CALPUFF, donde se ilustran los
diferentes archivos de entrada requeridos por los modelos WRF y CALPUFF. Como se
observa en esta figura, WRF requiere la topografía y usos de suelos locales, junto con la
meteorología proporcionada por el sistema GFS (ver Capítulo 3). Por otra parte,
CALPUFF requiere, la meteorología generada por WRF con el formato de CALMET
(calmet.dat) y la información de emisiones.

1: Software de visualización y Análisis, Desarrollado por EnviroModeling Spa., para el sistema CALPUFF.

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti
Romeral” 29

Informe Final v2

Figura 18: Diagrama de operación del sistema de modelación WRF/CALPUFF/CalDesk.

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti Romeral”

30
Informe Final v2

## 4.2 Implementación y Aplicación del Modelo de Dispersión CALPUFF

El modelo de dispersión CALPUFF se implementó en la zona de estudio utilizando la
meteorología del año 2020 modelada con WRF, en un dominio levemente menor que el
de WRF descrito en la Sección 3.2. El dominio utilizado se presenta en Tabla 7, el que
cubre un área de 50 x 50 km [2] con una resolución de 1 km muestra en Figura 19.

|Tabla 7: Características del dominio de modelación utilizada por el modelo CALPUFF en la comuna de San Clemente (archivo CALPUFF_Ready).|Col2|
|---|---|
|Características dominio CALPUFF-Ready|Características dominio CALPUFF-Ready|
|Resolución|1.000 x 1.000 (m)|
|No de celdas en dirección X|50|
|No de celdas en dirección Y|50|
|Coordenadas de referencia del origen del dominio*|UTM-E: 278.939 (m), UTM-N: 6.109.176 (m).|
|Total del área del dominio|2.500 (km2)|

*: Coordenada de referencia en UTM datum WGS 84 (aproximada), el dominio corresponde a la segunda

grilla anidada en la implementación del modelo WRF, la cual está en proyección Lambert Conformal Conic
(LCC).

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti
Romeral” 31

Informe Final v2

Figura 19: Dominio de modelación de CALPUFF, 50 x 50 km [2], en coordenadas LCC.

4.2.1 Receptores de Grilla y Discretos

Como se mencionó anteriormente el modelo CALPUFF se implementó en un área de 50
x 50 km [2] con resolución de 1 km. Después de una primera corrida se determinó un zoom
en la zona circundante al proyecto para aumentar la resolución de cálculo de este
dominio, el que se disminuyó en CALPUFF a un área aproximada de 15 x 10 km [2] para
que entregue concentraciones en celdas de 200 m de resolución. De esta forma
CALPUFF entregó concentraciones para un área de 155 km [2] . Las características del área
de receptores tipo grilla se presentan en Tabla 8 se muestra en Figura 20.

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti
Romeral” 32

Informe Final v2

Tabla 8: Características del área de receptores de Grilla.

|Item|Características|
|---|---|
|Kilómetros en dirección X|15,2|
|Kilómetros en dirección Y|10,2|
|Resolución|200 x 200 (m)|
|No de celdas en dirección X|76|
|No de celdas en dirección Y|51|
|Coordenadas de referencia del origen del dominio*|UTM-E: 293.027 (m), UTM-N: 6.123.886 (m)|
|Total de receptores|3.876|
|Área Total|155,04 (km2)|

*: Coordenada de referencia en UTM datum WGS 84 (aproximada), el dominio está en proyección Lambert

Conformal Conic (LCC).

Figura 20: Área de receptores de grilla de CALPUFF, 15 x 10 km [2], en coordenadas LCC.

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti
Romeral” 33

Informe Final v2

En cuanto a los receptores discretos, se consideraron 7 receptores cercanos a la planta
de Unifrutti que corresponden a viviendas. Las características de estos receptores,
como su ubicación y distancia al proyecto, se presentan en Tabla 9, y en Figura 21 se
muestra su ubicación.

Tabla 9: Receptores discretos.

|Receptor|Coordenadas UTM, WGS 84 - Z19|Col3|Altitud (m.s.n.m.)|Distancia al Proyecto*<br>(m)|
|---|---|---|---|---|
|Receptor|E (m)|N (m)|N (m)|N (m)|
|R1|300.016|6.127.638|242|720|
|R2|300.427|6.128.723|257|740|
|R3|300.107|6.129.352|254|930|
|R4|299.702|6.129.156|249|630|
|R5|299.469|6.128.853|245|368|
|R6|299.209|6.128.382|244|392|
|R7|299.299|6.127.809|241|668|

*: Distancia mínima al proyecto: considera la distancia recta entre el receptor y la fuente de olor más

cercana del proyecto.

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti
Romeral” 34

Informe Final v2

Figura 21: Ubicación de Receptores discretos.

4.2.2 Inventario de Emisiones de Olor

La planta Unifrutti, se encuentra emplazada en la Comuna de Romeral en la Longitudinal
Sur km 186, en la Provincia de Curicó, VII Región del Maule, dedicada a la exportación
de fruta fresca en donde se procesa la Especie Pera. El presente proyecto consiste en la
construcción y operación de un Sistema de Acondicionamiento para los Residuos
Industriales Líquidos (RILes).

En la actualidad, los RILes se generan principalmente en el proceso de lavado que se
realiza principalmente durante la recepción de las frutas y camiones; así como por los
efluentes de condensadores, las cuales dan lugar a un RIL crudo que cumple,
previamente, con los parámetros establecidos en la Tabla I del D.S N° 90/2000.

El sistema de acondicionamiento propuesto tiene como finalidad garantizar y/o
asegurar que el volumen de 200 m [3] /día que se generan en un periodo 15 días, y que
generalmente se realiza entre el 15 de febrero y el 15 de marzo, cuando se desarrollan
los procesos de recepción y embalaje de Pera, y de 5 m [3] /día de RILes durante todo el
resto del año, elimine cualquier residuo de polvo, tierra y materia extrañas que puedan
incorporarse al RIL.

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti
Romeral” 35

Informe Final v2

El diagrama de operación del sistema de tratamiento de Riles de la planta se presenta
en Figura 22.

Figura 22: Esquema del sistema de acondicionamiento de Riles de Planta Unifrutti

Romeral.

Las emisiones de olor del Proyecto se obtuvieron mediante la metodología de factores
de emisión, como lo recomienda la “Guía para la predicción y evaluación de impactos
por olor en el SEIA”.

La Ecuación 1 siguiente, presenta los diferentes enfoques que deben tenerse en cuenta,
en el cálculo de las emisiones:

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti
Romeral” 36

Informe Final v2

Em : FE ∗ NA Ecuación 1
j j j

Donde:

Em j : Emisión de olor debido al proceso j (uo/día, uo/s).

FE j : Factor de Emisión de olor de la actividad o proceso j (uo/s-m, uo/s-m [2] ).

NA j : Nivel de Actividad del proceso j (m, m [2] ).

Un Factor de Emisión es un valor representativo que intenta relacionar la cantidad de un
contaminante emitido a la atmósfera con una actividad asociada con la liberación de

ese contaminante.

Los factores de emisión considerados en la estimación de las emisiones de olor de las
fuentes asociadas a procesos de la planta de tratamiento de Riles se obtuvieron del
“Informe Final: Servicio de Recopilación y Sistematización de Factores de Emisión al
Aire, para el Servicio de Evaluación Ambiental, 2015”.

Considerando las operaciones mostradas en Figura 22 y sus factores de emisión
correspondientes se obtuvieron las emisiones de olor del proyecto, las que se presentan
en Tabla 10. En esta tabla se observa que alcanzan a 186 UO E /s. Estos resultados son
conservadores debido a que los factores son considerados como tal y son propios para
tratamiento de Riles, además que se considera que todas están al aire libre.

Tabla 10: Tipos de fuentes y emisiones de olor.

|Fuente|A (m2)|Tipo de fuente|FE (UO /s-m2)<br>E|Emisión (UO /s)<br>E|
|---|---|---|---|---|
|Cámara 1|1,0|Fuente difusa pasiva|9,5|9,5|
|Filtro rotatorio|6,8|Fuente difusa pasiva|7,5|50,9|
|Cámara 2|1,0|Fuente difusa pasiva|6|6,0|
|Cámara de contención|1,0|Fuente difusa pasiva|6|6,0|
|Decantador|4,9|Fuente difusa pasiva|1,3|6,4|
|Lecho de secado|6,25|Fuente difusa pasiva|8|50,0|
|Decantador|4,9|Fuente difusa pasiva|1,3|6,4|
|Lecho de secado|6,25|Fuente difusa pasiva|8|50,0|
|Cámara monitoreo|1,0|Fuente difusa pasiva|0,6|0,6|
|Descarga canal|1,0|Fuente difusa pasiva|0,6|0,6|
|Total|Total|Total|Total|186,4|

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti
Romeral” 37

Informe Final v2

Las fuentes presentadas en Tabla 10 se implementaron en el modelo CALPUFF
considerando fuentes de área, cuyas coordenadas se muestran en Tabla 11 en
coordenadas UTM y su correspondiente coordenada Lambert Conformal Conic (LCC).
Como se observa en esta tabla se consideró 1 fuente, en la zona de pretratamiento se
incluyeron las emisiones de todos los procesos unitarios de Tabla 10.

Las emisiones se implementaron considerando el peor escenario de emisiones, es decir,
con emisiones continuas durante todo el año.

Tabla 11: Coordenadas de las áreas donde se implementaron las fuentes de olor en el

modelo CALPUFF.

|Obra<br>Permanente|Superficie<br>(m2)|Puntos|UTM (WGS 84 Z19)|Col5|LCC (m)|Col7|
|---|---|---|---|---|---|---|
|Obra<br>Permanente|Superficie<br>(m2)|Puntos|Este|Norte|LCC-X|LCC-Y|
|Zona de<br>Pretratamiento|62|1|299.694,00|6.128.367,00|-3.839|-6.264|
|Zona de<br>Pretratamiento|62|2|299.700,00|6.128.364,00|-3.833|-6.267|
|Zona de<br>Pretratamiento|62|3|299.695,00|6.128.358,00|-3.838|-6.273|
|Zona de<br>Pretratamiento|62|4|299.689,00|6.128.360,00|-3.844|-6.271|

El detalle de la distribución de las fuentes de área del Proyecto se ilustra en Figura 23.
En esta figura se muestran las fuentes consideradas en Google Earth, panel a), y las
fuentes implementadas en el modelo CALPUFF en coordenadas LCC.

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti
Romeral” 38

Informe Final v2

Figura 23: Distribución de fuentes emisoras de olor de sistema de tratamiento de Riles

de planta Unifrutti. a) Fuentes en Google Earth, b) Fuentes implementadas
en CALPUFF, en coordenadas LCC.

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti
Romeral” 39

Informe Final v2

## 4.3 Resultados de la Aplicación del Sistema CALPUFF

En esta sección se presentan los resultados del sistema de modelación CALPUFF,
considerando el año meteorológico 2020 y el escenario de emisión de olores
presentados en la sección anterior.

Como en Chile no existe normativa que regule las concentraciones de olor se tomó como
referencia la normativa sobre olores holandesa en lo que respecta a la regularización de
instalaciones para el tratamiento de Riles, la cual hace diferencias para plantas nuevas
o existentes, en zonas urbanas o rurales.

En Tabla 12 se indican los niveles de molestia de olores de dicha norma. Como el
proyecto es existente emplazado en una zona rural se considera como norma de
referencia 3,5 UO E /m [3] para el percentil 98 de las concentraciones horarias.

Tabla 12: Normas de olor holandesa para tratamiento de Riles.

|Tipo de Instalación|Área|Norma (UO /m3)<br>E|
|---|---|---|
|Existente|Urbanas domésticas|Percentil 98: 1,0|
|Existente|Rurales o sitios industriales|Percentil 98: 3,5|
|Nuevas|Urbanas domésticas|Percentil 98: 0,5|
|Nuevas|Rurales o sitios industriales|Percentil 98: 1,5|

A continuación, se presentan los resultados de concentraciones odorantes modelados
con CALPUFF en la zona de estudio.

4.3.1 Resultados Odorantes en Receptores Discretos

Los resultados de concentraciones de olor modelados con CALPUFF se presentan en
Tabla 13 como máximo horario, percentil 99,5 y percentil 98 de las concentraciones
horarias del año 2020, en los receptores de interés presentados anteriormente en Tabla
9. En esta tabla se muestra también la norma de referencia utilizada.

En Tabla 13 se observa que las concentraciones de olor más altas se dan en los
receptores discretos R2 y R4, los que se encuentran hacia el noreste y norte del área de

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti
Romeral” 40

Informe Final v2

emplazamiento de la planta, respectivamente. Sin embargo, ningún receptor supera la
norma de olor tomada como referencia.

Por otra parte, en Tabla 14 se presenta la cantidad de excedencias horarias de la norma
de referencia de 3,5 UO E /m [3], como porcentaje anual y cantidad de horas al año. En esta
tabla se observa que en ningún receptor se superó la concentración de 3,5 UO E /m [3]
durante el año.

Tabla 13: Máximo horario, percentil 99,5 y percentil 98 de las concentraciones horarias

de olor modeladas por el sistema CALPUFF, del año 2020.

|Punto<br>Receptor|Concentración modelada (UO /m3)<br>E|Col3|Col4|Límite norma<br>referencia<br>(UO /m3)<br>E|Cumplimiento<br>Normativo|
|---|---|---|---|---|---|
|Punto<br>Receptor|Máximo Horario|Percentil 99,5<br>conc. horarias|Percentil 98<br>conc. horarias|Percentil 98<br>conc. horarias|Percentil 98<br>conc. horarias|
|R1|0,03|0,01|0,00|3,5|Si|
|R2|0,09|0,06|0,03|0,03|Si|
|R3|0,05|0,03|0,01|0,01|Si|
|R4|0,09|0,05|0,02|0,02|Si|
|R5|0,06|0,03|0,02|0,02|Si|
|R6|0,06|0,03|0,02|0,02|Si|
|R7|0,03|0,01|0,01|0,01|Si|

Tabla 14: Cantidad de excedencias horarias de la norma de referencia (3,5 UO E /m [3] ) en

los receptores discretos modelados por el sistema CALPUFF, año 2020.

|Punto<br>Receptor|Excedencia de norma|Col3|
|---|---|---|
|Punto<br>Receptor|(%)|(h/año)|
|R1|0,000|0|
|R2|0,000|0|
|R3|0,000|0|
|R4|0,000|0|
|R5|0,000|0|
|R6|0,000|0|
|R7|0,000|0|

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti
Romeral” 41

Informe Final v2

4.3.2 Curvas Odorantes

Los resultados de la modelación de olor con CALPUFF se presentan también como
isolíneas de máximas concentraciones horarias, percentil 99,5 de las concentraciones
horarias y percentil 98 de las concentraciones horarias de olor en Figura 24 a Figura 26,
respectivamente, como se indica en la “Guía a para la predicción y evaluación de
impactos por olor en el SEIA”.

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti
Romeral” 42

Informe Final v2

Figura 24: Mapa de curvas isodoras de concentraciones máximas horarias del año 2020 modelados con CALPUFF en

la zona de estudio.

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti Romeral”

43
Informe Final v2

Figura 25: Mapa de curvas isodoras percentil 99,5 de las concentraciones horarias del año 2020 modelados con

CALPUFF en la zona de estudio.

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti Romeral”

44
Informe Final v2

Figura 26: Mapa de curvas isodoras percentil 98 de las concentraciones horarias del año 2020 modelados con

CALPUFF en la zona de estudio.

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti Romeral”

45
Informe Final v2

4.3.3 Punto de Máxima Concentración Odorante

Como se observa en Figura 24 a Figura 26, las máximas concentraciones odorantes se
presentan en una zona cercana al área de riego oeste del Proyecto. Las concentraciones
de olor y ubicación del Punto de Máxima Concentración Odorante se presentan en Tabla
15.

Tabla 15: Máximo horario, percentil 99,5 y percentil 98 de las concentraciones horarias

|de olor en el Punto de Máxima Concentración Odorante.|Col2|Col3|
|---|---|---|
|Punto de Máxima Concentración|Punto de Máxima Concentración|Punto de Máxima Concentración|
|Máximo Horario (UOE/m3)|Máximo Horario (UOE/m3)|1,2|
|Percentil 99,5 concentraciones horarias (UOE/m3)|Percentil 99,5 concentraciones horarias (UOE/m3)|0,66|
|Percentil 98 concentraciones horarias (UOE/m3)|Percentil 98 concentraciones horarias (UOE/m3)|0,38|
|Ubicación|LCC-X (m)|-3.900|
|Ubicación|LCC-Y (m)|-6.300|
|Ubicación|UTM-E WGS 84 - Z19 (m)|299.634|
|Ubicación|UTM-N WGS 84 - Z19 (m)|6.128.330|

4.3.4 Área de Influencia

El Área de Influencia por dispersión de olor se presenta en Figura 27. Esta área es muy
conservadora dado que fue obtenida a partir de la zona que cubre la isolínea de
concentración de olor de 0,1 UO E /m [3], considerando que el umbral de detección de olor
por definición es 1 UO E /m [3] como la concentración teórica mínima para generar un
estímulo que pueda ser detectado en un porcentaje específico de la población, que por
convención generalmente se usa el 50% de la población.

El área de influencia estimada, rodeada por la isolínea de olor de 0,1 UO E /m [3], tiene una
forma elipsoidal y corresponde a aproximadamente 96 ha alrededor del Proyecto.

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti
Romeral” 46

Informe Final v2

Figura 27: Área de Influencia por dispersión de olor.

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti
Romeral”
47

Informe Final v2

# CAPÍTULO 5: CONCLUSIONES

En este Capítulo se presentan las conclusiones correspondientes al Informe Final del
“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta
Unifrutti Romeral”.

En este estudio se consideró la meteorología del año 2020 generada por el modelo
meteorológico de mesoescala WRF, de acuerdo a los requerimientos del SEA. La
meteorología generada por WRF fue validada a través de un análisis de incertidumbre
considerando la meteorología de la estación Universidad Católica del Maule.

Los aportes de olor del Proyecto en la zona de estudio, que consideró un área de 50 x
50 km [2], se obtuvieron mediante la ejecución del modelo CALPUFF considerando la
meteorología del año 2020 y las emisiones de olor del sistema de tratamiento de Riles
calculada en base a factores de emisión obtenidos del “Informe Final del Servicio de
recopilación y sistematización de factores de emisión al aire para el Servicio de
Evaluación Ambiental”.

Los resultados finales de este estudio permiten concluir lo siguiente:

 Las concentraciones de olor más altas se dan en los receptores discretos de

interés R2 y R4, los que se encuentran hacia el noreste (812 m) y norte (780 m)
del área de emplazamiento de la panta de Riles, respectivamente. Sin embargo,
ningún receptor supera la norma de olor tomada como referencia de 3,5 UO E /m [3]
para el percentil 98 de las concentraciones horarias ni tampoco para el año
completo.

 - Las máximas concentraciones odorantes alcanzan a 0,38 UO E /m [3] como percentil

98, este valor no supera la norma de referencia y se presenta en una zona muy
cercana al área de emplazamiento de la panta de Riles del Proyecto.

 El área de influencia estimada tiene una forma casi elipsoidal y corresponde a

aproximadamente 96 ha alrededor del Proyecto. Esta área es muy conservadora
dado que fue obtenida a partir de la zona que cubre la isolínea de concentración
de olor de 0,1 UO E /m [3], considerando que el umbral de detección de olor por
definición es 1 UO E /m [3] como la concentración teórica mínima para generar un
estímulo que pueda ser detectado en un porcentaje específico de la población,
que por convención generalmente se usa el 50% de la población.

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti
Romeral” 48

Informe Final v2

De acuerdo al análisis presentado, estos resultados implican que los máximos

aportes de olor a la zona de estudio debido al Proyecto de Sistema de
Acondicionamiento de Riles en planta Unifrutti Romeral no tienen un impacto
significativo y no representan un peligro para la salud de las personas del área
de emplazamiento del proyecto, cumplimento la normativa ambiental.

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti
Romeral” 49

Informe Final v2

# BIBLIOGRAFÍA

Insunza, J. (2012). Meteorología descriptiva. Departamento de Geofísica, Universidad
de Concepción, Concepción, 2-34.

INE, (2017). Síntesis de resultados Censo 2017.

 - - [https://www.censo2017.cl/descargas/home/sintesis](https://www.censo2017.cl/descargas/home/sintesis-de-resultados-censo2017.pdf) de resultados censo2017.pdf

SEA, (2012). Guía para el uso de modelos de calidad del aire en el SEIA.
https://www.sea.gob.cl/sites/default/files/migration_files/guias/Guia_uso_modelo_ca
lidad_del_aire_seia.pdf

Stull, R. B. (2012). An introduction to boundary layer meteorology (Vol. 13). Springer
Science & Business Media.

Wilks, D. S. (2011). Statistical methods in the atmospheric sciences (Vol. 100). Academic

press.

SEA, (2017). Guía para la Predicción y Evaluación de Impactos por Olor en el SEIA.
https://sea.gob.cl/sites/default/files/imce/archivos/2017/12/21/guia_pye_impactos_
por_olor_171221.pdf.

Netherlands Emission Guidelines for Air, Chapter 3.3 Special Regulations for Specific
Processes, Section G.3 "Sewage Treatment Installations, Abril 2003" (páginas 117 a
122).

BS Consultores, (2015). Informe Final del Servicio de recopilación y sistematización de
factores de emisión al aire para el Servicio de Evaluación Ambiental.
https://www.sea.gob.cl/documentacion/normas-de-calidad-y-valores-referenciales.

De B1mbo - Trabajo propio, CC BY-SA 2.5,
https://commons.wikimedia.org/w/index.php?curid=2584667.

De B1mbo - Trabajo propio, CC BY-SA 2.5,
https://commons.wikimedia.org/w/index.php?curid=3082394.

“Estudio de Dispersión de Olores para Sistema de Acondicionamiento de Riles en Planta Unifrutti
Romeral” 50

Informe Final v2