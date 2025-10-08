---
title: Sin título
author: EMwalnut@outlook.com
date: D:20221114182245-03'00'
language: es
type: report
pages: 78
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - CAPÍTULO 1: INTRODUCCIÓN
  - CAPÍTULO 2: ANÁLISIS DE LA INFORMACIÓN METEOROLÓGICA DE LA ZONA DEL PROYECTO
  - CAPÍTULO 3: IMPLEMENTACIÓN, APLICACIÓN Y RESULTADOS DEL MODELO METEOROLÓGICO WRF
  - CAPÍTULO 4: IMPLEMENTACIÓN, APLICACIÓN Y RESULTADOS DEL MODELO DE DISPERSIÓN CALPUFF
  - CAPÍTULO 5: CONCLUSIONES
  - CAPÍTULO 6: BIBLIOGRAFIA
-->

ESTUDIO EM2022/200-03: “Estudio de Dispersión de Olores del Proyecto
Ampliación y Regularización de Planta Ideal Quilicura”.

Better

Noviembre 2022

CAPÍTULO 1: INTRODUCCIÓN .................................................................................... 6

CAPÍTULO 2: ANÁLISIS DE LA INFORMACIÓN METEOROLÓGICA DE LA ZONA DEL

PROYECTO .................................................................................................................. 8

2.1 Introducción ................................................................................................................... 8

2.2 Descripción Topográfica y Climática de la Zona de Santiago ..................................... 8

2.3 Línea Base de Meteorología de la Zona de Santiago Durante el Año 2021 ................. 9

2.3.1 Series de Tiempo de Variables Meteorológicas Observadas en el Año 2021 ............... 11

2.3.2 Ciclos Diarios de Variables Meteorológicas Observadas Durante el Año 2021............ 13

2.3.3 Ciclos Estacionales de Variables Meteorológicas Observados Durante el Año 2021 .. 15

2.3.4 Rosas de Viento Observadas Durante el Año 2021 ......................................................... 17

CAPÍTULO 3: IMPLEMENTACIÓN, APLICACIÓN Y RESULTADOS DEL MODELO
METEOROLÓGICO WRF ............................................................................................. 20

3.1 Introducción ................................................................................................................. 20

3.2 Implementación del Modelo Meteorológico WRF ....................................................... 21

3.3 Resultados del Modelo WRF en la Zona de Santiago ................................................. 24

3.3.1 Series de Tiempo de Variables Meteorológicas Modeladas con WRF Año 2021 ......... 24

3.3.2 Ciclos Diarios de Variables Meteorológicas Modeladas con WRF para el Año 2021 ... 26

3.3.3 Ciclos Estacionales de Variables Meteorológicas Modeladas con WRF Durante el Año

2021 ............................................................................................................................................. 28

3.3.4 Rosas de Viento Modeladas con WRF Durante el Año 2021 .......................................... 30

3.4 Análisis de Incertidumbre de los Resultados del Modelo WRF Respecto de los Datos
Observados en Estaciones de Santiago Durante el Año 2021 ............................................... 32

3.4.1 Análisis Cualitativo Series de Tiempo Observados y Modelados con WRF, Año 2021 33

3.4.2 Análisis Cualitativo de Ciclos Diarios Observados y Modelados con WRF, Año 2021 . 37

3.4.3 Análisis Cualitativo de Ciclos Estacionales Observados y Modelados con WRF, Año

2021 ............................................................................................................................................. 40

i

3.4.4 Análisis Cualitativo de Rosas de Viento Observadas y Modeladas con WRF, Año 2021 .

............................................................................................................................................. 43

3.4.5 Análisis Cuantitativo .......................................................................................................... 46

CAPÍTULO 4: IMPLEMENTACIÓN, APLICACIÓN Y RESULTADOS DEL MODELO DE
DISPERSIÓN CALPUFF ............................................................................................. 48

4.1 Introducción ................................................................................................................. 48

4.2 Inventario de Emisiones de Olor .................................................................................. 49

4.2.1 Plan de Muestreo ............................................................................................................... 50

4.2.2 Análisis Olfatométrico ....................................................................................................... 51

4.2.3 Resultados Tasas de Emisión ........................................................................................... 52

4.3 Implementación y Aplicación del Modelo de Dispersión CALPUFF ........................... 55

4.3.1 Receptores de Grilla y Discretos ....................................................................................... 56

4.3.2 Implementación de Fuentes de Olor ................................................................................. 59

4.4 Resultados de la Aplicación del Sistema CALPUFF.................................................... 63

4.4.1 Área de Influencia .............................................................................................................. 63

4.4.2 Resultados Odorantes en Receptores Discretos ............................................................. 65

4.4.3 Curvas Odorantes .............................................................................................................. 68

4.4.4 Punto de Máxima Concentración Odorante ................................................................... 127

CAPÍTULO 5: CONCLUSIONES ................................................................................ 128

CAPÍTULO 6: BIBLIOGRAFIA ................................................................................... 130

ii

Tabla 1: Estaciones meteorológicas en el dominio de la zona de Santiago. .................................. 10

<!-- INICIO TABLA 1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Respecto al tratamiento de los datos, estos fueron revisados y validados siguiendo los lineamientos de la EPA, en relación a registros incoherentes, datos sin variación o saltos bruscos entre horas de cada variable y revisión de variabilidad diaria y estacionalidad. -->

**Tabla 1: Estaciones meteorológicas en el dominio de la zona de Santiago.**

| Estación | Abreviatura | Latitud | Longitud | Variables Medidas (%) | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Estación | Abreviatura | Latitud | Longitud | VV | DV | HR | T |
| Pudahuel | PU | -33,4377 | -70,7501 | 96,22 | 96,22 | 96,71 | 96,71 |
| Lo Pinto | LP | -33,2680 | -70,7322 | 98,03 | 80,78 | 98,23 | 98,24 |

<!-- Estadísticas: 3 filas, 8 columnas -->
<!-- Contexto posterior: -->
<!-- VV: velocidad de viento; DV: dirección de viento; HR: Humedad Relativa; T: temperatura. Figura 2: Ubicación de las estaciones meteorológicas ubicadas en la zona cercana a la -->
<!-- FIN TABLA 1 -->


Tabla 2: Características del dominio de modelación de la segunda grilla utilizada por el modelo

<!-- INICIO TABLA 2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- los -33,32822 latitud Sur y -70,725128 longitud Oeste. Las características generales de esta grilla se presentan en Tabla 2 y los dominios modelados se muestran en Figura 9. -->

**Tabla 2: Características del dominio de modelación de la segunda grilla utilizada por**

| el modelo WRF en la zona de Santiago. | Col2 |
| --- | --- |
| Características Grilla 2 de WRF | Características Grilla 2 de WRF |
| Resolución | 1,0 x 1,0 (km) |
| No de celdas en dirección X | 62 |
| No de celdas en dirección Y | 62 |
| Coordenadas del origen del dominio | Latitud: -33,32822; Longitud: -70,725128 |
| Total del área del dominio | 3.844 (km2) |

<!-- Estadísticas: 6 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Estudio EM2022/200-03 | Better “Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 22 Quilicura”. -->
<!-- FIN TABLA 2 -->

WRF en la zona de Santiago. ................................................................................................ 22

Tabla 3: Configuración de las principales parametrizaciones utilizadas en la modelación con WRF

<!-- INICIO TABLA 3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Respecto a la configuración del modelo, en relación a la física y dinámica, se consideraron las parametrizaciones del trabajo por el documento Guía para el uso de modelos de calidad del aire en el SEIA, 2012, cuyos principales esquemas son mostrados en la Tabla 3. -->

**Tabla 3: Configuración de las principales parametrizaciones utilizadas en la**

| Variable | Nombre | Esquema | Descripción |
| --- | --- | --- | --- |
| Microfísica | mp_physics | WSM5 | WSM (3 especies microfísicas) |
| Radiación de onda<br>larga | ra_lw_physics | RRTM | Modelo de transferencia<br>radiativa rápida que utiliza<br>tablas de eficiencia. Cuenta con<br>múltiples bandas |

<!-- Estadísticas: 2 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Estudio EM2022/200-03 | Better “Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 23 Quilicura”. -->
<!-- FIN TABLA 3 -->

para la zona de Santiago. ..................................................................................................... 23

Tabla 4: Estadísticos Matemáticos de Literatura. ............................................................................. 33

<!-- INICIO TABLA 4 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- observados y modelados. Las fórmulas y rango de estos estadísticos se presentan en Tabla 4. -->

**Tabla 4: Estadísticos Matemáticos de Literatura.**

| Estadístico | Ecuación | Rango |
| --- | --- | --- |
| RMSE | √∑(Mi−Oi)2<br>n<br>n<br>i=1<br> | (0, ∞) |
| BIASN | ∑<br>Mi−Oi<br>n<br>i=1<br>∑<br>Oi<br>n<br>i=1<br> | (-∞,∞) |
| R | ∑<br>(Mi−M) −(Oi−O)<br>n<br>i=1<br>{∑<br>(Mi−M)<br>2<br>n<br>i=1<br>∑<br>(Oi−O)2}<br>n<br>i=1<br>1/2 | [-1,1] |

<!-- Estadísticas: 3 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia en base a Wilks, 2011. 3.4.1 Análisis Cualitativo Series de Tiempo Observados y Modelados con WRF, Año -->
<!-- FIN TABLA 4 -->


Tabla 5: Resultados estadísticos obtenidos de la comparación de datos observados y modelados

<!-- INICIO TABLA 5 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- “Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 46 Quilicura”. Informe Final -->

**Tabla 5: Resultados estadísticos obtenidos de la comparación de datos observados y**

| Estadística | Variable | Unidad | Pudahuel | Lo Pinto |
| --- | --- | --- | --- | --- |
| BiasN | VV | m/s | 0,387 | 0,658 |
| BiasN | HR | % | 0,158 | 0,203 |
| BiasN | T | °C | 0,010 | -0,000 |
| RMSE | VV | m/s | 0,777 | 1,081 |
| RMSE | HR | % | 16,708 | 19,409 |
| RMSE | T | °C | 2,504 | 3,421 |
| R | VV | Adimensional | 0,809 | 0,721 |
| R | HR | Adimensional | 0,795 | 0,781 |
| R | T | Adimensional | 0,949 | 0,942 |

<!-- Estadísticas: 9 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- VV: velocidad de viento HR: humedad relativa T: temperatura del aire. Estudio EM2022/200-03 | Better -->
<!-- FIN TABLA 5 -->

con WRF en las estaciones de la zona de Santiago. .......................................................... 47

Tabla 6: Plan de Muestreo. .................................................................................................................. 50

<!-- INICIO TABLA 6 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- 4.2.1 Plan de Muestreo El muestreo se realizó durante 2 días, con un total de 30 muestras. Las unidades medidas se encuentran detalladas en Tabla 6. -->

**Tabla 6: Plan de Muestreo.**

| Unidad de Muestreo Sector | Total de<br>unidades | Área (m2) | Método de Muestreo | N° de Muestras |
| --- | --- | --- | --- | --- |
| GEM | 1 | 2,20 | FP | 3 |
| Ecualizador | 1 | 1,60 | FP | 3 |
| Dilub | 1 | 0,41 | FP | 3 |
| Estanque Lodos | 1 | 0,29 | FP | 3 |
| Deshidratador | 1 | 1,40 | FP | 3 |
| Salida Planta Grasas | 1 | 0,02 | FP | 3 |

<!-- Estadísticas: 6 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- Estudio EM2022/200-03 | Better “Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 50 Quilicura”. -->
<!-- FIN TABLA 6 -->


Tabla 7: Resultados toma y análisis de muestras. ........................................................................... 52

<!-- INICIO TABLA 7 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- 4.2.3 Resultados Tasas de Emisión Los resultados obtenidos durante la toma y el análisis de cada una de las muestras realizadas en la Planta de Producción de IDEAL en Quilicura se presentan en Tabla 7. -->

**Tabla 7: Resultados toma y análisis de muestras.**

| Id Muestra | Descripción | Fecha<br>Análisis | Hora<br>Análisis | Concentración<br>Olor (UO/m3) | Velocidad<br>salida (m/s) | Temperatura<br>salida (°C) | Presión<br>rel. (mbar) | HR salida<br>(%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 220022553 | GEM | 02-02-2022 | 15:44 | 378 | 0,21 | 28,63 | 980,1 | 59,4 |
| 220022554 | 220022554 | 220022554 | 16:00 | 367 | 0,21 | 28,63 | 980,1 | 59,4 |
| 220022555 | 220022555 | 220022555 | 16:11 | 128 | 0,21 | 28,63 | 980,1 | 59,4 |
| 220022541 | Ecualizador | 02-02-2022 | 16:39 | 10803 | 0,30 | 28,94 | 980,4 | 86,9 |
| 220022542 | 220022542 | 220022542 | 16:54 | 4063 | 0,30 | 28,94 | 980,4 | 86,9 |
| 220022543 | 220022543 | 220022543 | 17:02 | 3134 | 0,30 | 28,94 | 980,4 | 86,9 |
| 220022544 | Dilub | 02-02-2022 | 17:17 | 3411 | 0,32 | 27,17 | 981,3 | 75,9 |
| 220022545 | 220022545 | 220022545 | 17:26 | 1910 | 0,32 | 27,17 | 981,3 | 75,9 |
| 220022546 | 220022546 | 220022546 | 17:35 | 1486 | 0,32 | 27,17 | 981,3 | 75,9 |
| 220022547 | Estanque<br>Lodos | 02-02-2022 | 17:46 | 346 | 0,21 | 30,15 | 980,3 | 94,4 |
| 220022548 | 220022548 | 220022548 | 17:54 | 270 | 0,21 | 30,15 | 980,3 | 94,4 |
| 220022549 | 220022549 | 220022549 | 18:06 | 210 | 0,21 | 30,15 | 980,3 | 94,4 |
| 220022550 | Deshidratador | 02-02-2022 | 18:21 | 178 | 0,12 | 31,85 | 980,4 | 33,3 |
| 220022551 | 220022551 | 220022551 | 18:29 | 109 | 0,12 | 31,85 | 980,4 | 33,3 |
| 220022552 | 220022552 | 220022552 | 18:38 | 118 | 0,12 | 31,85 | 980,4 | 33,3 |
| 220022532 | Salida Planta<br>Grasas | 02-02-2022 | 18:46 | 4482 | 0,17 | 32,08 | 980,4 | 100 |
| 220022533 | 220022533 | 220022533 | 18:54 | 2989 | 0,17 | 32,08 | 980,4 | 100,0 |
| 220022534 | 220022534 | 220022534 | 19:06 | 3174 | 0,17 | 32,08 | 980,4 | 100,0 |
| 220022535 | Reactor<br>Biológico | 03-02-2022 | 16:05 | 685 | 1,52 | 29,56 | 980,4 | 100,0 |
| 220022536 | 220022536 | 220022536 | 16:24 | 412 | 1,52 | 29,56 | 980,4 | 100,0 |
| 220022537 | 220022537 | 220022537 | 16:35 | 269 | 1,52 | 29,56 | 980,4 | 100,0 |
| 220022538 | Sedimentador | 03-02-2022 | 15:26 | 294 | 1,38 | 29,19 | 957,3 | 85,9 |
| 220022539 | 220022539 | 220022539 | 15:46 | 486 | 1,38 | 29,19 | 957,3 | 85,9 |
| 220022540 | 220022540 | 220022540 | 15:54 | 546 | 1,38 | 29,19 | 957,3 | 85,9 |
| 220022529 | Área de<br>Contenedores | 03-02-2022 | 16:48 | 178 | 0,38 | 28,33 | 957,4 | 54,5 |
| 220022530 | 220022530 | 220022530 | 16:57 | 228 | 0,38 | 28,33 | 957,4 | 54,5 |

<!-- Estadísticas: 26 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Estudio EM2022/200-03 | Better “Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 52 Quilicura”. -->
<!-- FIN TABLA 7 -->


Tabla 8: Tasas de emisión................................................................................................................... 53

<!-- INICIO TABLA 8 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- En Tabla 8 se presentan los resultados de tasas de emisión, en unidades de concentración de olor por segundo y metro cuadrado para cada una de las muestras analizadas. -->

**Tabla 8: Tasas de emisión.**

| Id Muestra | Unidad | Área (m2)/unidad | Tasa de Emisión (UO/s*m2) |
| --- | --- | --- | --- |
| 220022553 | GEM | 2,20 | 1,50E-01 |
| 220022554 | 220022554 | 220022554 | 1,45E-01 |
| 220022555 | 220022555 | 220022555 | 5,07E-02 |
| 220022541 | Ecualizador | 1,60 | 8,40E+00 |
| 220022542 | 220022542 | 220022542 | 3,16E+00 |
| 220022543 | 220022543 | 220022543 | 2,44E+00 |
| 220022544 | Dilub | 0,41 | 1,12E+01 |
| 220022545 | 220022545 | 220022545 | 6,25E+00 |
| 220022546 | 220022546 | 220022546 | 4,86E+00 |
| 220022547 | Estanque Lodos | 0,29 | 1,03E+00 |
| 220022548 | 220022548 | 220022548 | 8,06E-01 |
| 220022549 | 220022549 | 220022549 | 6,27E-01 |
| 220022550 | Deshidratador | 1,40 | 6,27E-02 |
| 220022551 | 220022551 | 220022551 | 3,84E-02 |
| 220022552 | 220022552 | 220022552 | 4,16E-02 |
| 220022532 | Salida Planta Grasas | 0,02 | 7,08E+02 |
| 220022533 | 220022533 | 220022533 | 4,72E+02 |
| 220022534 | 220022534 | 220022534 | 5,02E+02 |
| 220022535 | Reactor Biológico | 60 | 1,99E+00 |
| 220022536 | 220022536 | 220022536 | 1,19E+00 |
| 220022537 | 220022537 | 220022537 | 7,80E-01 |
| 220022538 | Sedimentador | 11,25 | 7,57E-01 |
| 220022539 | 220022539 | 220022539 | 1,25E+00 |
| 220022540 | 220022540 | 220022540 | 1,41E+00 |
| 220022529 | Área de Contenedores | 12,09 | 2,27E-02 |
| 220022530 | 220022530 | 220022530 | 2,91E-02 |

<!-- Estadísticas: 26 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Estudio EM2022/200-03 | Better “Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 53 Quilicura”. -->
<!-- FIN TABLA 8 -->


Tabla 9: Tasas de emisión de olor por unidad y ranking de emisiones. .......................................... 54

<!-- INICIO TABLA 9 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Finalmente, las tasas de emisión de olor para cada una de las unidades medidas, determinadas en base a la media geométrica de los resultados de concentración de olor obtenidos en cada una de ellas se presentan en Tabla 9. -->

**Tabla 9: Tasas de emisión de olor por unidad y ranking de emisiones.**

| Unidad | Col2 | Tasa de Emisión de<br>Olor (UOE/s*m2) | Emisión (UO/S) | Ranking de<br>Emisión |
| --- | --- | --- | --- | --- |
| Planta de<br>Tratamiento de<br>Residuos<br>Industriales<br>Líquidos (PTAR) | GEM | 1,03E-01 | 2,27E-01 | 0,00% |
| Planta de<br>Tratamiento de<br>Residuos<br>Industriales<br>Líquidos (PTAR) | Ecualizador | 4,02E+00 | 6,43E+00 | 0,06% |
| Planta de<br>Tratamiento de<br>Residuos<br>Industriales<br>Líquidos (PTAR) | Dilub | 6,98E+00 | 2,85E+00 | 0,03% |
| Planta de<br>Tratamiento de<br>Residuos<br>Industriales<br>Líquidos (PTAR) | Estanque Lodos | 8,05E-01 | 2,34E-01 | 0,00%* |
| Planta de<br>Tratamiento de<br>Residuos<br>Industriales<br>Líquidos (PTAR) | Deshidratador | 4,64E-02 | 6,50E-02 | 0,00%* |
| Planta de<br>Tratamiento de<br>Residuos<br>Industriales<br>Líquidos (PTAR) | Salida Planta Grasas | 5,52E+02 | 8,66E+00 | 0,08% |
| Planta de<br>Tratamiento de<br>Residuos<br>Industriales<br>Líquidos (PTAR) | Reactor Biológico | 1,23E+00 | 7,37E+01 | 0,69% |
| Planta de<br>Tratamiento de<br>Residuos<br>Industriales<br>Líquidos (PTAR) | Sedimentador | 1,10E+00 | 1,24E+01 | 0,12% |
| Área de Contenedores | Área de Contenedores | 2,54E-02 | 3,07E-01 | 0,00%* |
| Galpón Producción | Galpón Producción | 5,13E+02 | 1,06E+04 | 99,02% |
| Total | Total | Total | 1,07E+04 | 100% |

<!-- Estadísticas: 11 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- (*) Valor inferior a 0,05. Como se observa en Tabla 9, la emisión total de la planta corresponde a 10746,1 UO/s y la unidad que presenta mayor emisión de olor es el Galpón de Producción con 10641,3 -->
<!-- FIN TABLA 9 -->


Tabla 10: Características del dominio de modelación utilizada por el modelo CALPUFF en la zona
de Quilicura-Santiago (archivo CALPUFF-Ready). ............................................................. 55

Tabla 11: Características del área de receptores de Grilla. ................................................................ 57

<!-- INICIO TABLA 11 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- “Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 56 Quilicura”. Informe Final -->

**Tabla 11: Características del área de receptores de Grilla.**

| Item | Características |
| --- | --- |
| Kilómetros en dirección X | 12,2 |
| Kilómetros en dirección Y | 12,2 |
| Resolución | 200 x 200 (m) |
| No de celdas en dirección X | 61 |
| No de celdas en dirección Y | 61 |
| Coordenadas de referencia del origen del dominio* | UTM-E: 332.957 (m), UTM-N: 6.304.314 (m) |
| Total de receptores | 3.721 |
| Área Total | 148,84 (km2) |

<!-- Estadísticas: 8 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- *: Coordenada de referencia en UTM datum WGS 84 (aproximada), el dominio está en proyección Lambert Conformal Conic (LCC). -->
<!-- FIN TABLA 11 -->


Tabla 12: Receptores discretos. ........................................................................................................... 58

<!-- INICIO TABLA 12 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- servicentro y centros comerciales. Es importante mencionar que el proyecto se encuentro emplazado en una zona industrial. Las características de estos receptores en la modelación, como su ubicación y distancia al proyecto, se presentan en Tabla 12 y en Figura 26 se muestra su ubicación. -->

**Tabla 12: Receptores discretos.**

| Receptor | Coordenadas UTM,<br>WGS 84 - Z19 | Col3 | Coordenadas LCC | Col5 | Altitud (1)<br>(m.s.n.m.) | Distancia al<br>Proyecto (2)<br>(m) |
| --- | --- | --- | --- | --- | --- | --- |
| Receptor | E (m) | N (m) | LCC-X (km) | LCC-Y (km) | LCC-Y (km) | LCC-Y (km) |
| R1 - Vivienda | 338.205 | 6.310.940 | -1,243 | -0,061 | 488 | 1.180 |
| R2 - Vivienda | 337.490 | 6.310.745 | -1,961 | -0,244 | 486 | 1.910 |
| R3 - Vivienda | 337.985 | 6.311.180 | -1,459 | 0,182 | 488 | 1.420 |
| R4 - Colegio | 339.270 | 6.308.810 | -0,213 | -2,209 | 487,5 | 1.820 |
| R5 - Vivienda | 338.630 | 6.308.720 | -0,855 | -2,288 | 486,5 | 2.090 |
| R6 - Servicentro | 339.170 | 6.309.110 | -0,309 | -1,907 | 487 | 1.540 |
| R7 - Centro de eventos | 337.760 | 6.309.720 | -1,708 | -1,274 | 485 | 1.980 |
| R8 - Centro Comercial | 340.600 | 6.310.290 | 1,141 | -0,751 | 489,5 | 1.090 |
| R9 - Centro Comercial | 341.265 | 6.310.655 | 1,812 | -0,397 | 519 | 1.170 |
| R10 - Vivienda | 337.825 | 6.313.220 | -1,585 | 2,225 | 492 | 2.750 |
| R11 - McDonals | 341.330 | 6.312.490 | 1,907 | 1,437 | 573,5 | 2.380 |
| R12 - Motel | 339.650 | 6.312.132 | 0,221 | 1,107 | 489 | 1.180 |
| R13 - Strip center | 339.379 | 6.312.624 | -0,041 | 1,603 | 492 | 1.650 |

<!-- Estadísticas: 14 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- 1: Altitud obtenida del terreno entregado por el modelo WRF en el formato CALMET. 2: Distancia mínima al proyecto: considera la distancia recta entre el receptor y la fuente de olor más cercana del proyecto. -->
<!-- FIN TABLA 12 -->


Tabla 13: Tipos de fuentes y emisiones de olor. ................................................................................. 59

<!-- INICIO TABLA 13 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- se contempla una ampliación que consiste en otro galpón de producción para la nueva línea de Takis, lo que incluye también un aumento en la planta de tratamiento de residuos industriales líquidos (PTAR) que se encuentra actualmente en operación. Las fuentes y emisiones consideradas en la modelación con CALPUFF se presentan en -->

**Tabla 13: para el escenario más desfavorable de emisión, correspondiente a la Operación**

| Escenario | Fuente de olor | Emisión (UO /s)<br>E |
| --- | --- | --- |
| Operación | PTAR | 1,297E+02 |
| Operación | Área de contenedores | 3,070E-01 |

<!-- Estadísticas: 2 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Estudio EM2022/200-03 | Better “Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 59 Quilicura”. -->
<!-- FIN TABLA 13 -->


Tabla 14: Coordenadas de las áreas donde se implementaron las fuentes de olor en el modelo

<!-- INICIO TABLA 14 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- La única fuente que se agrega en el escenario de Operación es el galpón nuevo. Las emisiones se implementaron considerando el peor escenario de emisiones, es decir, con emisiones continuas durante todo el año. -->

**Tabla 14: Coordenadas de las áreas donde se implementaron las fuentes de olor en el**

| Fuente | Col2 | Superficie<br>(m2) | Puntos | UTM (WGS 84 - Z19) | Col6 | Coordenadas LCC | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Fuente | Fuente | Superficie<br>(m2) | Puntos | Este (m) | Norte (m) | LCC-X (km) | LCC-Y (km) |
| PTAS | PTAS | 349 | 1 | 339.554 | 6.310.866 | 0,1041 | -0,1576 |
| PTAS | PTAS | 349 | 2 | 339.564 | 6.310.871 | 0,1150 | -0,1529 |
| PTAS | PTAS | 349 | 3 | 339.554 | 6.310.897 | 0,1055 | -0,1264 |
| PTAS | PTAS | 349 | 4 | 339.543 | 6.310.893 | 0,0937 | -0,1309 |
| Área de contenedores | Área de contenedores | 186 | 1 | 339.493 | 6.310.700 | 0,0412 | -0,3225 |
| Área de contenedores | Área de contenedores | 186 | 2 | 339.505 | 6.310.705 | 0,0526 | -0,3182 |
| Área de contenedores | Área de contenedores | 186 | 3 | 339.498 | 6.310.719 | 0,0460 | -0,3039 |
| Área de contenedores | Área de contenedores | 186 | 4 | 339.487 | 6.310.715 | 0,0354 | -0,3077 |
|  | área-1 | 4.992 | 1 | 339.408 | 6.310.904 | -0,0412 | -0,1167 |

<!-- Estadísticas: 10 filas, 8 columnas -->
<!-- Contexto posterior: -->
<!-- Estudio EM2022/200-03 | Better “Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 60 Quilicura”. -->
<!-- FIN TABLA 14 -->


CALPUFF. ............................................................................................................................... 60

Tabla 15: Normas de olor holandesa para Panaderías de bizcochos y pastelería. .......................... 63

<!-- INICIO TABLA 15 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- En Tabla 15 se indican los niveles de molestia de olores de dicha norma. Como se observa en esta tabla, el proyecto considera como norma de referencia 5,0 UO E /m [3] para el percentil 98 de las concentraciones horarias. -->

**Tabla 15: Normas de olor holandesa para Panaderías de bizcochos y pastelería.**

| Tipo de Instalación | Norma (UO /m3)<br>E |
| --- | --- |
| Panaderías de bizcochos y pastelería industrial | Percentil 98: 5,0 |

<!-- Estadísticas: 1 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- A continuación, se presentan los resultados de concentraciones odorantes modelados con CALPUFF en la zona de estudio. 4.4.1 Área de Influencia -->
<!-- FIN TABLA 15 -->


Tabla 16: Máximo horario, percentil 99,5 y percentil 98 de las concentraciones horarias de olor
modeladas por el sistema CALPUFF, escenario Operación. .............................................. 66

Tabla 17: Cantidad de excedencias horarias de la norma de referencia (5,0 UO E /m [3] ) en los

<!-- INICIO TABLA 17 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |R10|0,3|0,2|0,1|0,1|Si| |R11|0,2|0,2|0,1|0,1|Si| |R12|1,4|0,7|0,4|0,4|Si| |R13|0,8|0,4|0,2|0,2|Si| -->

**Tabla 17: Cantidad de excedencias horarias de la norma de referencia (5,0 UO E /m [3] ) en**

| ón. | Col2 | Col3 |
| --- | --- | --- |
| Punto Receptor | Excedencia de norma - Escenario<br>Operación | Excedencia de norma - Escenario<br>Operación |
| Punto Receptor | (%) | (h/año) |
| R1 | 0,000 | 0 |
| R2 | 0,000 | 0 |
| R3 | 0,000 | 0 |
| R4 | 0,000 | 0 |
| R5 | 0,000 | 0 |

<!-- Estadísticas: 7 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Estudio EM2022/200-03 | Better “Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 66 Quilicura”. -->
<!-- FIN TABLA 17 -->

receptores discretos modelados por el sistema CALPUFF, escenario de Operación. ..... 66

Tabla 18: Máximo horario, percentil 99,5 y percentil 98 de las concentraciones horarias de olor en

<!-- INICIO TABLA 18 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Como se observó en Figura 29 a Figura 31, las máximas concentraciones odorantes se presentaron muy cercanas y dentro del área de emplazamiento del Proyecto. Las concentraciones de olor y ubicación del Punto de Máxima Concentración Odorante se presentan en Tabla 18 para el escenario de Operación. -->

**Tabla 18: Máximo horario, percentil 99,5 y percentil 98 de las concentraciones horarias**

| de olor en el Punto de Máxima Concentración Odorante - Operación. | Col2 | Col3 |
| --- | --- | --- |
| Punto de Máxima Concentración de Olor - Escenario Operación | Punto de Máxima Concentración de Olor - Escenario Operación | Punto de Máxima Concentración de Olor - Escenario Operación |
| Máximo Horario (UOE/m3) | Máximo Horario (UOE/m3) | 16,62 |
| Ubicación | LCC-X (m) | -100 |
| Ubicación | LCC-Y (m) | -100 |
| Ubicación | UTM-E WGS 84 - Z19 (m) | 339.349 |
| Ubicación | UTM-N WGS 84 - Z19 (m) | 6.310.920 |
| Ubicación | Calle Cerro San Luis | Calle Cerro San Luis |
| Percentil 99,5 concentraciones horarias (UOE/m3) | Percentil 99,5 concentraciones horarias (UOE/m3) | 9,42 |
| Ubicación | LCC-X (m) | 100 |
| Ubicación | LCC-Y (m) | -300 |
| Ubicación | UTM-E WGS 84 - Z19 (m) | 339.552 |
| Ubicación | UTM-N WGS 84 - Z19 (m) | 6.310.724 |
| Ubicación | Dentro del área del Proyecto | Dentro del área del Proyecto |
| Percentil 98 concentraciones horarias (UOE/m3) | Percentil 98 concentraciones horarias (UOE/m3) | 6,10 |
| Ubicación | LCC-X (m) | -100 |
| Ubicación | LCC-Y (m) | -100 |
| Ubicación | UTM-E WGS 84 - Z19 (m) | 339.349 |
| Ubicación | UTM-N WGS 84 - Z19 (m) | 6.310.920 |
| Ubicación | Calle Cerro San Luis | Calle Cerro San Luis |

<!-- Estadísticas: 19 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Estudio EM2022/200-03 | Better “Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 127 Quilicura”. -->
<!-- FIN TABLA 18 -->

el Punto de Máxima Concentración Odorante - Escenario Operación. .......................... 127

iii

Figura 1: Topografía observada en la zona de Santiago. ..................................................................... 9

Figura 2: Ubicación de las estaciones meteorológicas ubicadas en la zona cercana a la planta
IDEAL en Santiago. ................................................................................................................ 10

Figura 3: Series de tiempo de variables meteorológicas observadas en las estaciones Pudahuel
(PU) y Lo Pinto (LP) durante el año 2021. ........................................................................... 12

Figura 4: Ciclos diarios de variables meteorológicas observadas en las estaciones Pudahuel (PU)
y Lo Pinto (LP) durante el año 2021. .................................................................................... 14

Figura 5: Ciclos estacionales de variables meteorológicas observadas en las estaciones Pudahuel
(PU) y Lo Pinto (LP) durante el año 2021. ........................................................................... 16

Figura 6: Rosas de viento observadas en estación Pudahuel (PU) durante el año 2021. ............... 18

Figura 7: Rosas de viento observadas en estación Lo Pinto (LP) durante el año 2021. ................. 19

Figura 8: Diagrama de operación del modelo meteorológico WRF. .................................................. 21

Figura 9: Dominios de modelación de WRF en la zona de Santiago. ................................................ 23

Figura 10: Series de tiempo de variables meteorológicas modeladas con WRF en las estaciones
Pudahuel (PU) y Lo Pinto (LP) durante el año 2021. .......................................................... 25

Figura 11: Ciclos diarios de variables meteorológicas modeladas con WRF en las estaciones
Pudahuel (PU) y Lo Pinto (LP) durante el año 2021. .......................................................... 27

Figura 12: Ciclos estacionales de variables meteorológicas modelados con WRF en las estaciones
Pudahuel (PU) y Lo Pinto (LP) durante el año 2021. .......................................................... 29

Figura 13: Rosas de viento obtenidas con datos modelados de WRF en las estaciones Pudahuel (PU)
y Lo Pinto (LP) durante el año 2021. .................................................................................... 31

Figura 14: Rosas de viento obtenidas con datos modelados de WRF en las estaciones Pudahuel (PU)
y Lo Pinto (LP) durante el año 2021. .................................................................................... 32

Figura 15: Comparación series de tiempo de variables meteorológicas observadas y modeladas con
WRF en estación Pudahuel (PU) durante el año 2021. ....................................................... 35

Figura 16: Comparación series de tiempo de variables meteorológicas observadas y modeladas con
WRF en estación Lo Pinto (LP) durante el año 2021. ......................................................... 36

Figura 17: Comparación de ciclos diarios de variables meteorológicas observados y modelados con
WRF en estación Pudahuel (PU) durante el año 2021. ....................................................... 38

Figura 18: Comparación de ciclos diarios de variables meteorológicas observados y modelados con
WRF en estación Lo Pinto (LP) durante el año 2021. ......................................................... 39

iv

Figura 19: Comparación de ciclos estacionales de variables meteorológicas observados y
modelados con WRF en estación Pudahuel (PU) durante el año 2021. ............................ 41

Figura 20: Comparación de ciclos estacionales de variables meteorológicas observados y
modelados con WRF en estación Lo Pinto (LP) durante el año 2021. .............................. 42

Figura 21: Comparación de rosas de viento observadas y modeladas con WRF en estación Pudahuel
(PU) durante el año 2021. ..................................................................................................... 44

Figura 22: Comparación de rosas de viento observadas y modeladas con WRF en estación Lo Pinto
(LP) durante el año 2021. ...................................................................................................... 45

Figura 23: Diagrama de operación del sistema de modelación WRF/CALPUFF/CalDesk. ................ 49

Figura 24: Dominio de modelación de CALPUFF, 62 x 62 km [2], en coordenadas LCC. ....................... 56

Figura 25: Área de receptores de grilla de CALPUFF, 12 x 12 km [2], en coordenadas LCC. ................. 57

Figura 26: Ubicación de Receptores discretos. .................................................................................... 59

Figura 27: Distribución de fuentes emisoras de olor del proyecto Planta Ideal Quilicura. a) Fuentes
en Google Earth, b) Fuentes implementadas en CALPUFF, en coordenadas LCC. ........... 62

Figura 28: Área de Influencia por dispersión de olor. ........................................................................... 65

Figura 29: Mapa de curvas isodoras de concentraciones máximas horarias del año 2021 modelados
con CALPUFF en la zona de estudio, escenario de Operación........................................... 69

Figura 30: Mapa de curvas isodoras percentil 99,5 de las concentraciones horarias del año 2021
modelados con CALPUFF en la zona de estudio, escenario de Operación. ...................... 70

Figura 31: Mapa de curvas isodoras percentil 98 de las concentraciones horarias del año 2021
modelados con CALPUFF en la zona de estudio, escenario de Operación. ...................... 71

v

# CAPÍTULO 1: INTRODUCCIÓN

En este documento EnviroModeling Spa. presenta el Informe Final correspondiente al:
“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta
Ideal Quilicura”. Este informe considera el escenario mas desfavorable correspondiente
al escenario de operación.

El proyecto consiste en la ampliación y regularización de las instalaciones de planta
IDEAL Cañaveral, la cual está en operación actualmente, y que consistirá en la nueva
línea de producción asociada a la elaboración de productos “Takis” y la construcción de
infraestructura de energía que generará una potencia eléctrica adicional a la planta. Esta
planta se encuentra ubicada en la comuna de Quilicura, Región Metropolitana.

El objetivo de este estudio consiste en evaluar los resultados del modelo CALPUFF
respecto a la dispersión de contaminantes de las fuentes emisoras, área de influencia y
cumplimiento normativo respecto a lo indicado en la “Guía para el uso de modelos de

calidad del aire en el SEIA”.

Para el logro de los objetivos, en primer lugar, se procedió a la elaboración de la línea
base meteorológica mediante la descarga de datos de la estación Pudahuel y Lo Pinto,
pertenecientes a la Red del Sistema de información Nacional de Calidad del Aire (SINCA)
y la red de la Dirección Meteorológica de Chile (DMC), respectivamente.

Posteriormente se realizó la modelación meteorológica con Weather Research and
Forecast Model (WRF) en modo diagnóstico para obtener la meteorología de la zona de
la ciudad de Santiago del año 2021, la cual fue utilizada como datos de entrada para la
ejecución del modelo de dispersión CALPUFF.

Finalmente se procedió a la modelación de dispersión de olores mediante el sistema
WRF/CALPUFF, recomendado por el SEA y EPA (USA) para emisiones en terreno
complejo. Este sistema se aplicó considerando los siguientes escenarios
meteorológico, topográfico y de emisiones:

Escenario Meteorológico: Corresponde al año 2021.

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 6
Quilicura”.

Informe Final

- Escenario Topográfico: La zona de estudio considera un área de 62 x 62 km [2],
cubriendo la zona del Proyecto, incluyendo la ciudad de Santiago.

Escenarios de Emisiones: Considera las emisiones del escenario de Operación.

El Inventario de Emisiones de la operación actual de la planta, fue realizado
mediante el método de olfatometría dinámica realizado por un laboratorio
certificado. Esto consistió en la obtención de muestras directas desde la fuente,
donde posteriormente fueron analizadas por un grupo de panelistas, para

finalmente obtener las tasas de emisión de las fuentes medidas. En base a estas

emisiones se determinó el escenario de operación considerando la ampliación de la
planta.

En el siguiente Capítulo de este documento se presenta la descripción de la información
meteorológica del proyecto en la zona de estudio. En el Capítulo 3 se presenta la
implementación, aplicación y resultados del modelo meteorológico WRF, además de la
comparación de los resultados de WRF con los datos observados en las estaciones de
la zona de interés. La implementación, aplicación y resultados del modelo de dispersión
CALPUFF se presenta en Capítulo 4. Finalmente, las conclusiones del estudio se
presentan en el Capítulo 5.

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 7
Quilicura”.

Informe Final

# CAPÍTULO 2: ANÁLISIS DE LA INFORMACIÓN METEOROLÓGICA DE LA ZONA DEL PROYECTO

## 2.1 Introducción

A continuación, se presenta una descripción de la zona donde se encuentra el proyecto
Planta IDEAL en Quilicura, considerando aspectos tales como: clima, características
topográficas y meteorología. Este proyecto se ubica en la comuna de Quilicura,
Provincia de Santiago, Región Metropolitana.

## 2.2 Descripción Topográfica y Climática de la Zona de Santiago

La cuenca de Santiago se emplaza en la zona central de Chile, aproximadamente a 80
km de la costa del Océano Pacífico, desde los 33° Sur hasta los 33,7° Sur y desde los
70,9° Oeste hasta los 70,5° Oeste aproximadamente. Posee una altitud media de 500
m.s.n.m. Se encuentra confinada al Este por la Cordillera de los Andes con una altitud
media de 4500 m, al Oeste por la Cordillera de la Costa de aproximadamente1500 m de
alto y tanto al Norte como al Sur por cadenas montañosas transversales (Orfanoz,
2016). En Figura 1 se presenta la topografía de la zona.

Respecto al clima de la ciudad de Santiago corresponde al tipo templado cálido con
lluvias invernales y estación seca prolongada. Las precipitaciones caen
preferentemente en los meses de invierno, lo que equivale al 80% de lo que cae en un
año.

Otro aspecto relevante corresponde a la baja humedad relativa debido a la situación de
continentalidad en que se encuentra la cuenca de Santiago. Esta es ligeramente superior
a 70% como promedio anual. Las amplitudes térmicas son altas, existen casi 13 °C de
diferencia entre el mes más cálido (enero) y el más frío (julio) y la diferencia media entre
las máximas y mínimas diarias es de 14 °C a 16 °C (Smith, 2011).

Respecto a los vientos, el viento predominante es Suroeste, siendo más persistente en
verano con una intensidad media de 15 km/h (Smith, 2011).

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 8
Quilicura”.

Informe Final

Fuente: Elaboración propia en base a los datos del Shuttle Radar Topography Mission (SRTM 1).

Figura 1: Topografía observada en la zona de Santiago.

## 2.3 Línea Base de Meteorología de la Zona de Santiago Durante el Año 2021

La información meteorológica del año 2021 del área de interés corresponde a los datos
extraídos desde las estaciones Pudahuel y Lo Pinto, perteneciente a la Red SINCA y la
red de la Dirección Meteorológica de Chile (DMC), respectivamente. La ubicación de
estas estaciones se puede ver en Figura 2.

Estas dos estaciones fueron elegidas en base a criterios de cercanía al proyecto y
porcentaje de disponibilidad de datos.

En Tabla 1 se muestran los porcentajes de datos válidos de las estaciones por variables
estudiadas, las cuales superan el 75% como mínimo de datos de calidad asegurada.

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 9
Quilicura”.

Informe Final

Respecto al tratamiento de los datos, estos fueron revisados y validados siguiendo los
lineamientos de la EPA, en relación a registros incoherentes, datos sin variación o saltos
bruscos entre horas de cada variable y revisión de variabilidad diaria y estacionalidad.

Tabla 1: Estaciones meteorológicas en el dominio de la zona de Santiago.

|Estación|Abreviatura|Latitud|Longitud|Variables Medidas (%)|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|Estación|Abreviatura|Latitud|Longitud|VV|DV|HR|T|
|Pudahuel|PU|-33,4377|-70,7501|96,22|96,22|96,71|96,71|
|Lo Pinto|LP|-33,2680|-70,7322|98,03|80,78|98,23|98,24|

VV: velocidad de viento; DV: dirección de viento; HR: Humedad Relativa; T: temperatura.

Figura 2: Ubicación de las estaciones meteorológicas ubicadas en la zona cercana a la

planta IDEAL en Santiago.

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 10
Quilicura”.

Informe Final

2.3.1 Series de Tiempo de Variables Meteorológicas Observadas en el Año 2021

La Figura 3 muestra las series de tiempo de las variables meteorológicas de las
estaciones Pudahuel (PU) y Lo Pinto (LP). En esta figura se visualiza integridad de los
datos en todo el año a pesar de la leve pérdida de datos en PU en noviembre, sin
embargo, cumple con la disponibilidad mayor al 75% de los datos en todas las variables,
siendo óptimo para el presente estudio (Tabla 1).

La velocidad de viento, al igual que la temperatura, muestra un aumento de la magnitud
en los meses de verano y lo inverso en invierno.

Respecto a la dirección de viento, se visualiza componentes dominantes Suroeste a lo
largo del año, con una modificación a Norte en PU y Este en LP en los meses de invierno.

Respecto a la humedad relativa, muestra un aumento de la magnitud en los meses de
invierno y una disminución en los meses de verano.

La temperatura muestra la variabilidad estacional, con mayores magnitudes en los
periodos de verano y menores, incluso bajo cero en los meses de invierno.

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 11
Quilicura”.

Informe Final

Figura 3: Series de tiempo de variables meteorológicas observadas en las estaciones

Pudahuel (PU) y Lo Pinto (LP) durante el año 2021.

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 12
Quilicura”.

Informe Final

2.3.2 Ciclos Diarios de Variables Meteorológicas Observadas Durante el Año 2021

Los ciclos diarios son construidos en base a los registros promedios de cada hora de
todo el año, con el fin de mostrar un comportamiento patrón de una cierta variable, en
este caso meteorológica. La zona sombreada corresponde al área delimitada por los
percentiles 5 y 95, el cual tiene como objetivo caracterizar la variabilidad de la velocidad
del viento, humedad relativa y temperatura.

Un poco distinto es lo que se visualiza en el ciclo de dirección de viento, el cual muestra
la frecuencia en términos de porcentaje, de las direcciones de viento registradas cada
22,5° a lo largo de todas las horas, desde 00 hasta 23, tomando en cuenta todos los
datos del año.

En la Figura 4 se muestran los ciclos diarios de las variables meteorológicas estudiadas,
velocidad y dirección de viento, humedad relativa y temperatura registrados en las
estaciones Pudahuel (PU) y Lo Pinto (LP).

Los ciclos diarios de velocidad de viento muestran el aumento de la magnitud después
de las 12:00 horas. Destaca estación PU con una mayor velocidad de viento respecto a
LP.

Los ciclos diarios de dirección de viento muestran en el día una componente Suroeste,
en PU se visualiza más marcado con casi un 70% de frecuencia durante 3 horas
aproximadamente, respecto a LP. En el periodo nocturno se aprecian diferencias entre
las estaciones, en PU el viento sigue siendo Suroeste, mientras que en LP el viento
cambia a Este.

Respecto a los ciclos diarios de la humedad relativa y temperatura, se observan
comportamientos inversos entre variables. Durante el día se observa, una máxima
magnitud de la temperatura de ciclo, mientras que la humedad relativa es el mínimo,
invirtiéndose la situación en el periodo nocturno.

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 13
Quilicura”.

Informe Final

Figura 4: Ciclos diarios de variables meteorológicas observadas en las estaciones

Pudahuel (PU) y Lo Pinto (LP) durante el año 2021.

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 14
Quilicura”.

Informe Final

2.3.3 Ciclos Estacionales de Variables Meteorológicas Observados Durante el Año

2021

Los ciclos estacionales corresponden a gráficos donde se muestra el ciclo diario en el
eje x y el ciclo anual en el eje y. La escala de color muestra la magnitud de la variable,
donde el color rojo muestra valores máximos y los colores azules los mínimos. En
particular, en el ciclo estacional de velocidad de viento se superponen vectores de viento
en la imagen, con la finalidad de mostrar la dirección de viento predominante promedio
a lo largo del día y del año.

En la Figura 5 se muestran los ciclos estacionales de las variables meteorológicas
estudiadas velocidad y dirección de viento, humedad relativa y temperatura en las
estaciones Pudahuel (PU) y Lo Pinto (LP).

Los ciclos estacionales de la velocidad de viento muestran valores máximos en el
periodo diurno y en los meses de verano en las dos estaciones, siendo la de mayor
velocidad en PU.

Respecto a la dirección de viento, el viento Suroeste diurno y a lo largo de todo el año es
dominante en ambas estaciones, mientras que en el periodo nocturno se aprecian
diferencias. En PU, periodo verano y nocturno, los vientos son Suroeste, mientras en LP
los vientos son Noroeste. En invierno y periodo nocturno los vientos muestran
componente Norte y Noreste en ambas estaciones, lo cual puede ser atribuido a bajas
presiones de sistemas frontales típicos de la zona central del país (Garreaud y Rutllant,
1996).

Los ciclos de humedad relativa muestran una disminución de la magnitud en el día y
durante el verano, mientras que en la noche y en el invierno la magnitud de la humedad
es la máxima.

Respecto a la temperatura, los gráficos muestran coincidencia en las estaciones, un
aumento de la magnitud durante el día y en los meses de verano, mientras que en el
periodo nocturno e invernal la magnitud disminuye notablemente.

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 15
Quilicura”.

Informe Final

Figura 5: Ciclos estacionales de variables meteorológicas observadas en las

estaciones Pudahuel (PU) y Lo Pinto (LP) durante el año 2021.

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 16
Quilicura”.

Informe Final

2.3.4 Rosas de Viento Observadas Durante el Año 2021

La variabilidad de la velocidad y dirección del viento es caracterizada adicionalmente
mediante las rosas de viento solicitadas por el documento oficial, “Guía para el uso de
Modelos de Calidad del Aire en el SEIA”.

En Figura 6 y Figura 7 se presentan las rosas de viento de las de las estaciones Pudahuel
(PU) y Lo Pinto (LP), donde en cada imagen se encuentran los cuatro rangos de tiempo
horarios por estación, los cuales son descritos a continuación:

 Periodo noche o madrugada, 01:00 a 06:00 horas: en ambas estaciones se

muestran velocidades que no superan el 1 m/s, siendo más cercano a las calmas
en LP. Respecto a la dirección de viento, en PU los vientos tienen dirección
Suroeste, mientras que en LP los vientos se visualizan Noreste.

 - Periodo mañana, 07:00 a 14:00 horas: En ambas estaciones la velocidad aumenta

alcanzando los 3 m/s, debido al factor radiativo (SEIA,2012). La dirección de
viento se muestra mayoritariamente Suroeste (18% aproximadamente) en PU y
Noreste en menor medida. En la estación LP el viento se visualiza Suroeste en
mayor medida (10% aproximadamente) y en menor medida Noreste.

 - Periodo tarde, 15:00 a 23:00 horas: la velocidad de viento alcanza los 3 m/s con

mayor frecuencia en ambas estaciones respecto al periodo de mañana, debido al
factor mecánico. La dirección es mayoritariamente Suroeste en ambas
estaciones.

 Periodo completo, 00:00 a 23:00 horas: la velocidad alcanza los 3 m/s en ambas

estaciones, teniendo mayor frecuencia en PU que en LP. La dirección de viento
visualizada es Suroeste en PU y en LP, y adicionalmente una dirección Noreste
solo en LP.

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 17
Quilicura”.

Informe Final

Figura 6: Rosas de viento observadas en estación Pudahuel (PU) durante el año 2021.

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 18
Quilicura”.

Informe Final

Figura 7: Rosas de viento observadas en estación Lo Pinto (LP) durante el año 2021.

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 19
Quilicura”.

Informe Final

# CAPÍTULO 3: IMPLEMENTACIÓN, APLICACIÓN Y RESULTADOS DEL MODELO METEOROLÓGICO WRF

## 3.1 Introducción

En este Capítulo se presenta la implementación y aplicación del modelo meteorológico
WRF v4.3 (Weather Research and Forecasting Model). WRF es uno de los modelos
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

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 20
Quilicura”.

Informe Final

Figura 8: Diagrama de operación del modelo meteorológico WRF.

## 3.2 Implementación del Modelo Meteorológico WRF

En esta sección se presenta la implementación y aplicación del modelo meteorológico
WRF para la generación de la meteorología requerida por el modelo CALPUFF para el
año 2021.

El modelo se implementó con dos grillas anidadas en la zona de la ciudad de Santiago.
Las condiciones de borde e iniciales de los datos históricos del año 2021 fueron
proporcionadas por GDAS de NOAA (National Oceanic and Atmospheric Administration),
de USA, con una resolución espacial de 0,25 grados.

Respecto a la topografía del dominio de modelación, fue obtenida a partir del proyecto
SRTM (del acrónimo inglés Shuttle Radar Topography Mission) con resolución de 3
segundos de grado (90 metros aproximadamente) y el uso de suelo a partir de la

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 21
Quilicura”.

Informe Final

información satelital MODIS (del acrónimo inglés Moderate-Resolution Imaging
Spectroradiometer) de la NASA con resolución de 15 segundos de grado.

El dominio de modelación utilizado en el área de Santiago consideró la grilla N° 2 de
WRF, por ser la que posee una resolución con tamaño de grilla de 1 km x 1 km para
definir la topografía y uso de suelo. Tiene dimensiones de 62 kilómetros en la dirección
Este-Oeste y 62 kilómetros en la dirección Norte-Sur, alrededor de su centro ubicado en
los -33,32822 latitud Sur y -70,725128 longitud Oeste.

Las características generales de esta grilla se presentan en Tabla 2 y los dominios
modelados se muestran en Figura 9.

Tabla 2: Características del dominio de modelación de la segunda grilla utilizada por

|el modelo WRF en la zona de Santiago.|Col2|
|---|---|
|Características Grilla 2 de WRF|Características Grilla 2 de WRF|
|Resolución|1,0 x 1,0 (km)|
|No de celdas en dirección X|62|
|No de celdas en dirección Y|62|
|Coordenadas del origen del dominio|Latitud: -33,32822; Longitud: -70,725128|
|Total del área del dominio|3.844 (km2)|

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 22
Quilicura”.

Informe Final

Figura 9: Dominios de modelación de WRF en la zona de Santiago.

Respecto a la configuración del modelo, en relación a la física y dinámica, se
consideraron las parametrizaciones del trabajo por el documento Guía para el uso de
modelos de calidad del aire en el SEIA, 2012, cuyos principales esquemas son
mostrados en la Tabla 3.

Tabla 3: Configuración de las principales parametrizaciones utilizadas en la
modelación con WRF para la zona de Santiago.

|Variable|Nombre|Esquema|Descripción|
|---|---|---|---|
|Microfísica|mp_physics|WSM5|WSM (3 especies microfísicas)|
|Radiación de onda<br>larga|ra_lw_physics|RRTM|Modelo de transferencia<br>radiativa rápida que utiliza<br>tablas de eficiencia. Cuenta con<br>múltiples bandas|

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 23
Quilicura”.

Informe Final

|Variable|Nombre|Esquema|Descripción|
|---|---|---|---|
|Radiación de onda<br>corta|ra_sw_physics|Dudhia scheme|Integración simple que permite<br>la absorción y dispersión por<br>nubes y a cielo despejado|
|Capa superficial|sf_sfclay_physics|MM5|Monin-Obukhov similaridad|
|Superficie|sf_Surface_physcis|Thermal Diffusion<br>Scheme|Esquema de difusión termal|
|Capa límite<br>planetaria|bl_pbl_physics|YSU scheme|QNSE|

## 3.3 Resultados del Modelo WRF en la Zona de Santiago

En la presente sección se muestran los resultados del modelo meteorológico WRF. Estos
provienen de las variables extraídas y elegidas de las coordenadas de las estaciones
monitoras de la red meteorológica presentada en la sección 2.3 del presente informe
(Tabla 1).

3.3.1 Series de Tiempo de Variables Meteorológicas Modeladas con WRF Año 2021

Las series de tiempo de velocidad y dirección de viento, humedad relativa y temperatura,
modeladas con WRF para el año 2021 se muestran en Figura 10 para las estaciones de
Pudahuel (PU) y Lo Pinto (LP) consideradas en la zona de Santiago.

En Figura 10 se observa en las series de velocidad que en todas las estaciones muestran
mayores magnitudes en los meses estivales, mientras que en invierno disminuyen.

Las series de dirección de viento muestran vientos de componente Suroeste en todas
las estaciones a lo largo del año, aunque con más tendencia Oeste en LP. Respecto a
invierno, en la estación PU varía a Sureste y en menor medida Noreste, mientras que en
la estación LP se visualiza marcadamente Noreste.

Las series de humedad relativa muestran magnitudes mayores en los meses de invierno,
mientras que en verano disminuyen los máximos de humedad relativa.

Finalmente, las series de temperatura muestran magnitudes mayores en los meses
estivales respecto a invernales, en todas las estaciones.

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 24
Quilicura”.

Informe Final

Figura 10: Series de tiempo de variables meteorológicas modeladas con WRF en las

estaciones Pudahuel (PU) y Lo Pinto (LP) durante el año 2021.

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 25
Quilicura”.

Informe Final

3.3.2 Ciclos Diarios de Variables Meteorológicas Modeladas con WRF para el Año 2021

En Figura 11 se muestran los ciclos diarios de las variables meteorológicas modeladas
con WRF para las estaciones Pudahuel (PU) y Lo Pinto (LP).

Los ciclos diarios modelados de velocidad de viento muestran un aumento de la
magnitud durante el día y una disminución en el periodo nocturno en todas las
estaciones. Destaca el aumento en la amplitud en las estaciones PU y LP.

Los ciclos diarios de dirección de viento muestran componentes similares en el periodo
diurno en las dos estaciones, esto es viento Suroeste. Durante la noche existen
divergencias, en PU se observa dirección Suroeste y en LP una dirección Noreste.

Respecto a la humedad relativa, el modelo muestra un aumento de la magnitud por la
noche y una disminución en el día en las dos estaciones.

Finalmente, respecto a los ciclos de las temperaturas, en todas las estaciones muestran
la máxima magnitud en el día, después de las 12:00 horas, mientras que la mínima se
visualiza a eso de las 06:00 horas.

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 26
Quilicura”.

Informe Final

Figura 11: Ciclos diarios de variables meteorológicas modeladas con WRF en las

estaciones Pudahuel (PU) y Lo Pinto (LP) durante el año 2021.

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 27
Quilicura”.

Informe Final

3.3.3 Ciclos Estacionales de Variables Meteorológicas Modeladas con WRF Durante el

Año 2021

En Figura 12 se muestran los ciclos estacionales de las variables meteorológicas
modeladas con WRF para el año 2021 para las estaciones Pudahuel (PU) y Lo Pinto (LP).

Respecto a la velocidad de viento, se observa que el modelo simuló las máximas
magnitudes en el periodo diurno y estival, mientras que las mínimas fueron modeladas
en el periodo nocturno y meses de invierno.

En el mismo gráfico, se observan los vectores de viento, los cuales indican que el modelo
reproduce vientos de componente Suroeste en el día y a lo largo del año en las dos
estaciones, mientras que en la noche los vientos modelados tienen dirección Sureste en
la estación PU en los meses de verano. En invierno, en PU los vientos modelados son de
componente Este. Una descripción aparte requiere la estación LP, para el periodo
nocturno y meses de invierno, los vientos modelados toman una dirección Noreste,
modificándose lentamente en los meses de transición de los equinoccios.

Analizando los ciclos estacionales de humedad relativa, estos muestran que el modelo
reproduce máximas magnitudes en el periodo nocturno, mientras que las mínimas
magnitudes son modeladas en el periodo diurno y a lo largo del año.

En cuanto a la temperatura, en ambas estaciones muestran un aumento de la magnitud
de la temperatura durante el día y en los meses de verano, mientras que la disminución
de la magnitud es visualizada en el periodo nocturno y en invierno.

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 28
Quilicura”.

Informe Final

Figura 12: Ciclos estacionales de variables meteorológicas modelados con WRF en las

estaciones Pudahuel (PU) y Lo Pinto (LP) durante el año 2021.

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 29
Quilicura”.

Informe Final

3.3.4 Rosas de Viento Modeladas con WRF Durante el Año 2021

Las rosas de viento modeladas en las estaciones Pudahuel (PU) y Lo Pinto (LP) se
presentan en Figura 13 y Figura 14, las que se presentan construidas para cuatro rangos
de tiempo horarios, los cuales son descritos a continuación:

 Periodo noche o madrugada, 01:00 a 06:00 horas: el modelo ha reproducido

vientos que levemente sobrepasan el 1 m/s en ambas estaciones. La dirección
de viento modelada muestra viento Sureste en estación PU y vientos Noreste y
Suroeste, aunque cercano al 4%, de frecuencia en estación LP.

 - Periodo mañana, 07:00 a 14:00 horas: en ambas estaciones la velocidad

modelada muestra magnitud levemente sobre los 3 m/s. La dirección de viento
muestra componente Suroeste en ambas estaciones, adicionalmente en LP, se
ve una dirección Noreste, con mucho menor recurrencia.

 Periodo tarde, 15:00 a 23:00 horas: en ambas estaciones se visualiza que el

modelo reproduce vientos que llegan a los 4 m/s en el caso de PU y llegando a 5
m/s en LP. La dirección de viento en PU muestra componentes Suroeste y
Sureste en menor medida, mientras que en LP es solo Suroeste.

 Periodo completo, 00:00 a 23:00 horas: se visualiza que la velocidad de viento

modelada alcanza los 4 m/s en ambas estaciones. Respecto a la dirección de
viento muestra vientos Suroeste y Sureste en estación PU, mientras que, en
estación LP muestra Suroeste y Noreste, siendo la dirección común y
mayormente recurrente la componente Suroeste la modelada.

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 30
Quilicura”.

Informe Final

Figura 13: Rosas de viento obtenidas con datos modelados de WRF en las estaciones

Pudahuel (PU) y Lo Pinto (LP) durante el año 2021.

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 31
Quilicura”.

Informe Final

Figura 14: Rosas de viento obtenidas con datos modelados de WRF en las estaciones

Pudahuel (PU) y Lo Pinto (LP) durante el año 2021.

## 3.4 Análisis de Incertidumbre de los Resultados del Modelo WRF Respecto de los Datos Observados en Estaciones de Santiago Durante el Año 2021

En esta sección se analiza el nivel de incertidumbre del modelo meteorológico WRF, de
forma cualitativa mediante la comparación de gráficos, de ciclos diarios y estacionales,
y de forma cuantitativa mediante estadísticos matemáticos obtenidos por comparación
entre los datos horarios de las observaciones y los resultados simulados con WRF.

Los estadísticos matemáticos calculados son los siguientes:

Error cuadrático medio (RMSE): entrega el grado de precisión entre los datos

pronosticados y observados.

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 32
Quilicura”.

Informe Final

Sesgo normalizado (BIASN): entrega el sesgo entre las series modeladas y

observadas.

Coeficiente de correlación (R): entrega el grado de relación lineal entre los datos

observados y modelados.

Las fórmulas y rango de estos estadísticos se presentan en Tabla 4.

Tabla 4: Estadísticos Matemáticos de Literatura.

|Estadístico|Ecuación|Rango|
|---|---|---|
|RMSE|√∑(Mi−Oi)2<br>n<br>n<br>i=1<br>|(0, ∞)|
|BIASN|∑<br>Mi−Oi<br>n<br>i=1<br>∑<br>Oi<br>n<br>i=1<br>|(-∞,∞)|
|R|∑<br>(Mi−M) −(Oi−O)<br>n<br>i=1<br>{∑<br>(Mi−M)<br>2<br>n<br>i=1<br>∑<br>(Oi−O)2}<br>n<br>i=1<br>1/2|[-1,1]|

Fuente: Elaboración propia en base a Wilks, 2011.

3.4.1 Análisis Cualitativo Series de Tiempo Observados y Modelados con WRF, Año

2021

En Figura 15 y Figura 16 se presenta la comparación de las series de tiempo de variables
meteorológicas observados a la izquierda y modelados con WRF a la derecha durante el
año 2021 para las estaciones Pudahuel (PU) y Lo Pinto (LP), respectivamente.

Analizando la velocidad de viento, el modelo se ajustó de mejor forma en magnitud en
estación PU, mientras que en LP se observa sobrestimación. De todas formas, el modelo
logra capturar la variabilidad estacional, representando la mayor magnitud en el periodo
de verano y menor magnitud en el periodo de invierno.

Adicionalmente el modelo logra representar unos máximos de velocidad visualizados
en el periodo de primavera en ambas estaciones, aunque en LP lo sobrestima (Figura
16).

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 33
Quilicura”.

Informe Final

Respecto a la dirección de viento, en estación PU, el modelo logra capturar el viento
Suroeste (200°) que se visualiza en ambas estaciones en gran parte del año. No
obstante, en invierno en estación PU, el modelo subestima las componentes Norte
(360°) y Noreste (80° aproximadamente) visualizada en las observaciones (Figura 15).
En estación LP el modelo sobrestima la componente Norte de la dirección Noreste del
periodo invernal (Figura 16).

En cuanto a la humedad relativa, el modelo reproduce la variabilidad estacional, aunque
con sesgos. En ambas estaciones el modelo sobrestima los mínimos de humedad
relativa en los meses de invierno, mientras que en verano el modelo sobrestima los
máximos.

Analizando el desempeño del modelo respecto a la temperatura, en ambas estaciones
el modelo sobrestima los mínimos y subestima los máximos, lo que indica que el modelo
reproduce una amplitud térmica de menor magnitud que la observada.

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 34
Quilicura”.

Informe Final

Figura 15: Comparación series de tiempo de variables meteorológicas observadas y

modeladas con WRF en estación Pudahuel (PU) durante el año 2021.

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 35
Quilicura”.

Informe Final

Figura 16: Comparación series de tiempo de variables meteorológicas observadas y

modeladas con WRF en estación Lo Pinto (LP) durante el año 2021.

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 36
Quilicura”.

Informe Final

3.4.2 Análisis Cualitativo de Ciclos Diarios Observados y Modelados con WRF, Año

2021

La comparación de ciclos diarios de variables meteorológicas observados a la izquierda
y modelados con WRF a la derecha, durante el año 2021 en las estaciones Pudahuel
(PU) y Lo Pinto (LP) se presentan en Figura 17 y Figura 18, respectivamente.

Revisando los ciclos de la velocidad de viento, se observa que el modelo logra capturar
la variabilidad diaria, representando el aumento de la magnitud en el día, y disminución
en la noche. Entre estaciones se visualiza la diferencia de la profundización de la
sobrestimación del modelo en LP respecto a PU, donde el modelo fue más preciso.

En cuanto a los ciclos de dirección de viento, en estación PU el modelo subestima la
componente Suroeste nocturna, reproduciendo más una tendencia Sur. Durante el día
el modelo reproduce la componente Suroeste observada, aunque muestra de forma
adicional casi un 40% de vientos de más tendencia hacia el Oeste de las observaciones
(Figura 17).

En estación LP el modelo subestima la componente Este nocturna y en el día el modelo
reproduce los vientos Suroeste observados (Figura 18).

Respecto a la humedad relativa, el modelo en todas las estaciones logra reproducir la
variabilidad horaria, con la disminución de la magnitud durante el día y el aumento
durante la noche. Sin embargo, algunos sesgos presentes es que en ambas estaciones
el modelo sobrestima los mínimos del día, y en la noche la humedad es constante, no
mostrando la variación vista en las observaciones.

Finalmente, respecto a la temperatura, el modelo en todas las estaciones logra
reproducir la variabilidad horaria, traducido en el aumento de la temperatura durante el
día y la disminución durante la noche. Sin embargo, el modelo muestra una
subestimación de los máximos y sobrestimación de los mínimos.

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 37
Quilicura”.

Informe Final

Figura 17: Comparación de ciclos diarios de variables meteorológicas observados y

modelados con WRF en estación Pudahuel (PU) durante el año 2021.

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 38
Quilicura”.

Informe Final

Figura 18: Comparación de ciclos diarios de variables meteorológicas observados y

modelados con WRF en estación Lo Pinto (LP) durante el año 2021.

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 39
Quilicura”.

Informe Final

3.4.3 Análisis Cualitativo de Ciclos Estacionales Observados y Modelados con WRF,

Año 2021

En Figura 19 y Figura 20 se presentan la comparación de los ciclos estacionales de
variables meteorológicas observados a la izquierda y modelados con WRF a la derecha,
durante el año 2021 en las estaciones Pudahuel (PU) y Lo Pinto (LP), respectivamente.

Revisando el desempeño del modelo en los ciclos estacionales de velocidad de viento,
se visualiza que el modelo en ambas estaciones logra reproducir el ciclo estacional y el
ciclo diario, sin embargo, en ambos casos el modelo sobrestima la magnitud.

Respecto a la dirección de viento, en estación PU el modelo reproduce los vientos
Suroeste del periodo diurno y a lo largo de todo el año, sin embargo, en los meses de
verano el modelo muestra Sureste mientras que las observaciones son Suroeste. En el
periodo de invierno el modelo muestra componente Este, mientras que en las
observaciones se visualiza componente Norte (Figura 19).

En la estación LP el viento reproduce los vientos Suroestes diurnos de todo el año, y los
vientos Noreste en los meses de invierno visualizados en las observaciones (Figura 20).

En cuanto a la humedad relativa, en ambas estaciones el modelo sobrestima a lo largo
de todo el día y del año la magnitud, representado por los colores menos azules que son
mostrados en las observaciones. Respecto al periodo nocturno y verano, en ambas
estaciones el modelo sobrestima la magnitud, mientras que en invierno y en el mismo
periodo nocturno el modelo subestima los máximos de humedad.

Finalmente, describiendo el ciclo de las temperaturas, el modelo subestimó la magnitud
en ambas estaciones, sin embargo, cumple con la captura de la variabilidad estacional
y diaria, donde logra reproducir los ciclos respectivos, esto es el aumento de la magnitud
de temperatura en el día y meses de verano y lo inverso por la noche y en los meses de
invierno.

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 40
Quilicura”.

Informe Final

Figura 19: Comparación de ciclos estacionales de variables meteorológicas

observados y modelados con WRF en estación Pudahuel (PU) durante el año
2021.

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 41
Quilicura”.

Informe Final

Figura 20: Comparación de ciclos estacionales de variables meteorológicas

observados y modelados con WRF en estación Lo Pinto (LP) durante el año
2021.

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 42
Quilicura”.

Informe Final

3.4.4 Análisis Cualitativo de Rosas de Viento Observadas y Modeladas con WRF, Año

2021

En la Figura 21 y Figura 22 se presenta la comparación de las rosas de viento en las
estaciones Pudahuel (PU) y Lo Pinto (LP). A continuación, se describe en detalle los
cuatro periodos mostrados por las rosas de viento construidas:

 - Periodo 01:00 a 06:00 horas: se visualiza en estación PU, la sobrestimación de la

velocidad de viento donde la frecuencia mostrada en las rosas de viento es mayor
en el modelo que las observaciones. Respecto a la dirección de viento el modelo
reproduce una componente Sureste, mientras que las observaciones muestran
un viento de componente Suroeste (Figura 21). En estación LP respecto a la
velocidad de viento, las observaciones muestran una mayor tendencia a las
calmas, mientras que el modelo muestra levemente mayores velocidades en este
periodo de tiempo. Respecto a la dirección en LP, el modelo subestima la
componente Noreste y sobrestima la componente Suroeste (Figura 22).

 Periodo 07:00 a 14:00 horas: en las estaciones PU y LP el modelo reproduce los

3 m/s mostrados en la escala de color y respecto a la dirección de viento
reproduce la dirección Suroeste en ambos casos. La diferencia se produce entre
estaciones, donde en PU, el modelo subestima la frecuencia de ocurrencia de la
dirección, mientras que en LP sobrestima.

 - Periodo 15:00 a 23:00 horas: en ambas estaciones el modelo sobrestima

levemente la velocidad de viento llegando a 4 m/s en PU y 5 m/s en LP. Respecto
a la dirección en PU, el modelo subestima la frecuencia de la dirección Suroeste
y sobrestima la dirección Sureste. En LP el modelo fue más preciso en la
reproducción de la componente Suroeste.

 - Periodo 00:00 a 23:00 horas: se visualizan en ambos casos, vientos de

magnitudes de 3 m/s e inclusive llegando a los 5 m/s en el caso de LP. Respecto
a la dirección de viento, en PU, el modelo subestima la componente Suroeste y
sobrestima la componente Sureste. En LP muestra una mayor variabilidad en la
dirección Suroeste respecto a lo mostrado en las observaciones y subestima la
componente Noreste.

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 43
Quilicura”.

Informe Final

Figura 21: Comparación de rosas de viento observadas y modeladas con WRF en

estación Pudahuel (PU) durante el año 2021.

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 44
Quilicura”.

Informe Final

Figura 22: Comparación de rosas de viento observadas y modeladas con WRF en

estación Lo Pinto (LP) durante el año 2021.

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 45
Quilicura”.

Informe Final

3.4.5 Análisis Cuantitativo

El análisis cuantitativo es realizado mediante la utilización de los estadísticos descritos
al inicio de la sección 3.4. Estos son resultados de la comparación entre las series de
datos observados y modelados con WRF, extraídos para las estaciones Pudahuel (PU)
y Lo Pinto (LP), los cuales se presentan en la en la Tabla 5, donde se consolida toda la
información. Estos estadísticos dan una muestra del desempeño del modelo en los
puntos geográficos analizados.

Considerando la tabla descrita se puede indicar lo siguiente:

 Respecto al BIASN, se tiene lo siguiente:

 - Velocidad de viento: el modelo sobrestima en ambas estaciones la
magnitud de la variable, siendo mayor en LP.

 - Humedad relativa: el modelo sobrestima en ambas estaciones la magnitud
de la variable, siendo mayor en LP.

 - Temperatura: el modelo sobrestima y subestima muy ligeramente en PU y
LP la magnitud de la variable.

 Respecto al RMSE, se tiene lo siguiente:

 - Velocidad de viento: el modelo fue más preciso en PU.

 - Humedad relativa: el modelo fue más preciso en PU.

 - Temperatura: el modelo fue más preciso en PU.

 Respecto al estadístico de correlación R, se puede inferir lo siguiente:

 - Velocidad de viento: el modelo tuvo un mayor grado de relación en la
estación PU.

 - Humedad relativa: el modelo tuvo un mayor grado de relación en la
estación PU.

 - Temperatura: el modelo tuvo un mayor grado de relación en la estación
PU.

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 46
Quilicura”.

Informe Final

Tabla 5: Resultados estadísticos obtenidos de la comparación de datos observados y
modelados con WRF en las estaciones de la zona de Santiago.

|Estadística|Variable|Unidad|Pudahuel|Lo Pinto|
|---|---|---|---|---|
|BiasN|VV|m/s|0,387|0,658|
|BiasN|HR|%|0,158|0,203|
|BiasN|T|°C|0,010|-0,000|
|RMSE|VV|m/s|0,777|1,081|
|RMSE|HR|%|16,708|19,409|
|RMSE|T|°C|2,504|3,421|
|R|VV|Adimensional|0,809|0,721|
|R|HR|Adimensional|0,795|0,781|
|R|T|Adimensional|0,949|0,942|

VV: velocidad de viento HR: humedad relativa T: temperatura del aire.

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 47
Quilicura”.

Informe Final

# CAPÍTULO 4: IMPLEMENTACIÓN, APLICACIÓN Y RESULTADOS DEL MODELO DE DISPERSIÓN CALPUFF

## 4.1 Introducción

El sistema de modelación CALPUFF, está actualmente aprobado por el Servicio de
Evaluación Ambiental (SEA) de Chile y por la EPA (USA) como modelo regulatorio para
evaluar el impacto de emisiones atmosféricas en escenarios de terreno y meteorología
compleja. Este sistema está compuesto por los modelos WRF y CALPUFF, cuya
descripción general es la siguiente:

WRF: Modelo euleriano de mesoescala y micrometeorológico capaz de generar la
meteorología requerida por el modelo CALPUFF con resolución de 1 km, para la
evaluación de contaminantes primarios.

CALPUFF: Modelo lagrangiano de dispersión tipo puff que permite simular el
transporte, dispersión e impacto de emisiones de contaminantes primarios de
procesos naturales y antropogénicos, utilizando la meteorología generada por WRF.

El análisis de resultados de los modelos WRF y CALPUFF se realiza con el software
CalDESK Advanced v2.99 [1] . Esta herramienta permite generar mapas de
isoconcentraciones de contaminantes y visualizar los resultados de todas las variables
entregadas por los modelos.

En Figura 23 se presenta un diagrama del sistema CALPUFF, donde se ilustran los
diferentes archivos de entrada requeridos por los modelos WRF y CALPUFF. Como se
observa en esta figura, WRF requiere la topografía y usos de suelos locales, junto con la
meteorología proporcionada por el sistema GFS (ver Capítulo 3). Por otra parte,
CALPUFF requiere, la meteorología generada por WRF con el formato de CALMET
(calmet.dat/CALPUFF-Ready) y la información de emisiones, entregada en el Inventario
de Emisiones que se presenta más adelante en este Capítulo.

1: Software de visualización y Análisis, Desarrollado por EnviroModeling Ltda., para el sistema CALPUFF.

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 48
Quilicura”.

Informe Final

Figura 23: Diagrama de operación del sistema de modelación WRF/CALPUFF/CalDesk.

## 4.2 Inventario de Emisiones de Olor

El proyecto consiste en la ampliación y regularización de las instalaciones de planta
IDEAL Cañaveral, la cual está en operación actualmente, y que consistirá en la nueva
línea de producción asociada a la elaboración de productos “Takis” y la construcción de
infraestructura de energía que generará una potencia eléctrica adicional a la planta.

La ampliación consiste en acondicionar un área disponible en la fábrica existente para
establecer instalaciones productivas y de servicio, esto considera la ampliación de sus
instalaciones en una superficie de 0,2 hectáreas (2.075,73 m [2] ).

Conjuntamente, la planta Ideal cuenta con una Planta de Tratamiento de Residuos
Industriales líquidos que se encuentra actualmente en operación. Dicha planta abastece
de tratamiento a efluentes industriales propios del proceso de la fábrica Ideal para
posteriormente ser evacuadas por el sistema de alcantarillado público, posterior a la
medición de los parámetros químicos, físicos y biológicos del agua.

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 49
Quilicura”.

Informe Final

La planta de Ideal se emplaza en una zona urbana, ubicada en Avenida Cañaveral #100
(con calle Cerro Portezuelo), en la comuna de Quilicura, provincia de Santiago, Región
Metropolitana de Santiago.

Las emisiones de olor del Proyecto se obtuvieron mediante un estudio de olfatometría
realizado por el laboratorio certificado ANAM, el que permitió evaluar la generación de
olores provenientes de la planta de producción. La metodología general, resultados
detallados y certificaciones del laboratorio se presentan en Apéndice A.

El estudio de olores se efectuó en dos etapas:

Toma de muestra en las fuentes de la planta.

Análisis olfatométrico de las muestras, análisis sensorial y determinación de las
tasas de emisión.

La toma de muestras se realizó los días 02 y 03 de febrero de 2022, en horario desde las
12:00 hasta las 15:05 horas en la primera jornada de medición y desde las 11:00 hasta
las 14:05 horas en la segunda jornada de medición.

La toma de muestras y análisis de concentración de olor, se realizaron utilizando como
referencia la normativa chilena NCh 3386:2015 “Calidad del Aire - Muestreo Estático
para Olfatometría” y análisis de concentración de olor según NCh 3190:2010 “Calidad
del Aire - Determinación de Olor por Olfatometría Dinámica”.

4.2.1 Plan de Muestreo

El muestreo se realizó durante 2 días, con un total de 30 muestras. Las unidades
medidas se encuentran detalladas en Tabla 6.

Tabla 6: Plan de Muestreo.

|Unidad de Muestreo Sector|Total de<br>unidades|Área (m2)|Método de Muestreo|N° de Muestras|
|---|---|---|---|---|
|GEM|1|2,20|FP|3|
|Ecualizador|1|1,60|FP|3|
|Dilub|1|0,41|FP|3|
|Estanque Lodos|1|0,29|FP|3|
|Deshidratador|1|1,40|FP|3|
|Salida Planta Grasas|1|0,02|FP|3|

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 50
Quilicura”.

Informe Final

|Unidad de Muestreo Sector|Total de<br>unidades|Área (m2)|Método de Muestreo|N° de Muestras|
|---|---|---|---|---|
|Reactor Biológico|1|60,00|FSP|3|
|Sedimentador|1|11,25|FSP|3|
|Área de Contenedores|1|12,09|FP|3|
|Galpón Producción|1|20,73|FF|3|
|Total|Total|Total|Total|30|

FP: Fuente Puntual FSP: Fuentes superficiales pasivas FF: Fuentes Fugitivas

4.2.2 Análisis Olfatométrico [2]

El laboratorio de olfatometría dinámica utilizado cumple con los requisitos de calidad
de las mediciones sensoriales, según lo establecido en la norma chilena NCh. 3.190.

El laboratorio de olfatometría dispone de un equipo TO8 y el panel de análisis está
formado por un mínimo de 4 personas previamente seleccionadas, conforme a la norma
chilena NCh. 3.190. El procedimiento de selección está diseñado para conseguir
personas con una sensibilidad promedio para captar olores.

Para la realización de los análisis olfatométricos, se emplea un olfatómetro (equipo
dilutor que permite obtener diluciones conocidas de una muestra) totalmente
controlado mediante un computador, con el objetivo de determinar la estimación de
umbral para la muestra en cuestión y por consiguiente la concentración de olor,
expresada en unidades de olor por metro cúbico. Por unidad de olor, se entiende el
número de diluciones necesarias para lograr lo que se denomina umbral de olor: que el
50% de los miembros del panel puedan distinguirlo.

La presentación de la muestra en el equipo olfatómetro, se efectúa a través del método
Sí/No, establecido en la Norma Chilena NCh 3.190, la preparación de las diluciones de
las muestras, el almacenamiento de las respuestas de los miembros del panel y la
interpretación estadística de los resultados son realizadas íntegramente por un
programa informático que posee el equipo olfatómetro.

Luego del análisis de cada una de las muestras y determinada la concentración de olor
para cada una, se efectúa el cálculo de la tasa de emisión de olores (UO E /m [2] s y UO/s).
Dependiendo del método de muestreo utilizado, es el procedimiento a seguir para

2 Fuente: Apéndice A.

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 51
Quilicura”.

Informe Final

determinar la tasa de emisión de las unidades, el que se presenta detalladamente en
Apéndice A.

4.2.3 Resultados Tasas de Emisión

Los resultados obtenidos durante la toma y el análisis de cada una de las muestras
realizadas en la Planta de Producción de IDEAL en Quilicura se presentan en Tabla 7.

Tabla 7: Resultados toma y análisis de muestras.

|Id Muestra|Descripción|Fecha<br>Análisis|Hora<br>Análisis|Concentración<br>Olor (UO/m3)|Velocidad<br>salida (m/s)|Temperatura<br>salida (°C)|Presión<br>rel. (mbar)|HR salida<br>(%)|
|---|---|---|---|---|---|---|---|---|
|220022553|GEM|02-02-2022|15:44|378|0,21|28,63|980,1|59,4|
|220022554|220022554|220022554|16:00|367|0,21|28,63|980,1|59,4|
|220022555|220022555|220022555|16:11|128|0,21|28,63|980,1|59,4|
|220022541|Ecualizador|02-02-2022|16:39|10803|0,30|28,94|980,4|86,9|
|220022542|220022542|220022542|16:54|4063|0,30|28,94|980,4|86,9|
|220022543|220022543|220022543|17:02|3134|0,30|28,94|980,4|86,9|
|220022544|Dilub|02-02-2022|17:17|3411|0,32|27,17|981,3|75,9|
|220022545|220022545|220022545|17:26|1910|0,32|27,17|981,3|75,9|
|220022546|220022546|220022546|17:35|1486|0,32|27,17|981,3|75,9|
|220022547|Estanque<br>Lodos|02-02-2022|17:46|346|0,21|30,15|980,3|94,4|
|220022548|220022548|220022548|17:54|270|0,21|30,15|980,3|94,4|
|220022549|220022549|220022549|18:06|210|0,21|30,15|980,3|94,4|
|220022550|Deshidratador|02-02-2022|18:21|178|0,12|31,85|980,4|33,3|
|220022551|220022551|220022551|18:29|109|0,12|31,85|980,4|33,3|
|220022552|220022552|220022552|18:38|118|0,12|31,85|980,4|33,3|
|220022532|Salida Planta<br>Grasas|02-02-2022|18:46|4482|0,17|32,08|980,4|100|
|220022533|220022533|220022533|18:54|2989|0,17|32,08|980,4|100,0|
|220022534|220022534|220022534|19:06|3174|0,17|32,08|980,4|100,0|
|220022535|Reactor<br>Biológico|03-02-2022|16:05|685|1,52|29,56|980,4|100,0|
|220022536|220022536|220022536|16:24|412|1,52|29,56|980,4|100,0|
|220022537|220022537|220022537|16:35|269|1,52|29,56|980,4|100,0|
|220022538|Sedimentador|03-02-2022|15:26|294|1,38|29,19|957,3|85,9|
|220022539|220022539|220022539|15:46|486|1,38|29,19|957,3|85,9|
|220022540|220022540|220022540|15:54|546|1,38|29,19|957,3|85,9|
|220022529|Área de<br>Contenedores|03-02-2022|16:48|178|0,38|28,33|957,4|54,5|
|220022530|220022530|220022530|16:57|228|0,38|28,33|957,4|54,5|

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 52
Quilicura”.

Informe Final

|Id Muestra|Descripción|Fecha<br>Análisis|Hora<br>Análisis|Concentración<br>Olor (UO/m3)|Velocidad<br>salida (m/s)|Temperatura<br>salida (°C)|Presión<br>rel. (mbar)|HR salida<br>(%)|
|---|---|---|---|---|---|---|---|---|
|220022531|||17:07|194|0,38|28,33|957,4|54,5|
|220022526|Galpón<br>Producción|03-02-2022|17:20|61|11,76|29,24|956,6|33,0|
|220022527|220022527|220022527|17:28|37|11,76|29,24|956,6|33,0|
|220022528|220022528|220022528|17:40|48|11,76|29,24|956,6|33,0|

En Tabla 8 se presentan los resultados de tasas de emisión, en unidades de
concentración de olor por segundo y metro cuadrado para cada una de las muestras
analizadas.

Tabla 8: Tasas de emisión.

|Id Muestra|Unidad|Área (m2)/unidad|Tasa de Emisión (UO/s*m2)|
|---|---|---|---|
|220022553|GEM|2,20|1,50E-01|
|220022554|220022554|220022554|1,45E-01|
|220022555|220022555|220022555|5,07E-02|
|220022541|Ecualizador|1,60|8,40E+00|
|220022542|220022542|220022542|3,16E+00|
|220022543|220022543|220022543|2,44E+00|
|220022544|Dilub|0,41|1,12E+01|
|220022545|220022545|220022545|6,25E+00|
|220022546|220022546|220022546|4,86E+00|
|220022547|Estanque Lodos|0,29|1,03E+00|
|220022548|220022548|220022548|8,06E-01|
|220022549|220022549|220022549|6,27E-01|
|220022550|Deshidratador|1,40|6,27E-02|
|220022551|220022551|220022551|3,84E-02|
|220022552|220022552|220022552|4,16E-02|
|220022532|Salida Planta Grasas|0,02|7,08E+02|
|220022533|220022533|220022533|4,72E+02|
|220022534|220022534|220022534|5,02E+02|
|220022535|Reactor Biológico|60|1,99E+00|
|220022536|220022536|220022536|1,19E+00|
|220022537|220022537|220022537|7,80E-01|
|220022538|Sedimentador|11,25|7,57E-01|
|220022539|220022539|220022539|1,25E+00|
|220022540|220022540|220022540|1,41E+00|
|220022529|Área de Contenedores|12,09|2,27E-02|
|220022530|220022530|220022530|2,91E-02|

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 53
Quilicura”.

Informe Final

|Id Muestra|Unidad|Área (m2)/unidad|Tasa de Emisión (UO/s*m2)|
|---|---|---|---|
|220022531|||2,48E-02|
|220022526|Galpón Producción|20,73|6,57E+02|
|220022527|220022527|220022527|3,98E+02|
|220022528|220022528|220022528|5,17E+02|

Finalmente, las tasas de emisión de olor para cada una de las unidades medidas,
determinadas en base a la media geométrica de los resultados de concentración de olor
obtenidos en cada una de ellas se presentan en Tabla 9.

Tabla 9: Tasas de emisión de olor por unidad y ranking de emisiones.

|Unidad|Col2|Tasa de Emisión de<br>Olor (UOE/s*m2)|Emisión (UO/S)|Ranking de<br>Emisión|
|---|---|---|---|---|
|Planta de<br>Tratamiento de<br>Residuos<br>Industriales<br>Líquidos (PTAR)|GEM|1,03E-01|2,27E-01|0,00%|
|Planta de<br>Tratamiento de<br>Residuos<br>Industriales<br>Líquidos (PTAR)|Ecualizador|4,02E+00|6,43E+00|0,06%|
|Planta de<br>Tratamiento de<br>Residuos<br>Industriales<br>Líquidos (PTAR)|Dilub|6,98E+00|2,85E+00|0,03%|
|Planta de<br>Tratamiento de<br>Residuos<br>Industriales<br>Líquidos (PTAR)|Estanque Lodos|8,05E-01|2,34E-01|0,00%*|
|Planta de<br>Tratamiento de<br>Residuos<br>Industriales<br>Líquidos (PTAR)|Deshidratador|4,64E-02|6,50E-02|0,00%*|
|Planta de<br>Tratamiento de<br>Residuos<br>Industriales<br>Líquidos (PTAR)|Salida Planta Grasas|5,52E+02|8,66E+00|0,08%|
|Planta de<br>Tratamiento de<br>Residuos<br>Industriales<br>Líquidos (PTAR)|Reactor Biológico|1,23E+00|7,37E+01|0,69%|
|Planta de<br>Tratamiento de<br>Residuos<br>Industriales<br>Líquidos (PTAR)|Sedimentador|1,10E+00|1,24E+01|0,12%|
|Área de Contenedores|Área de Contenedores|2,54E-02|3,07E-01|0,00%*|
|Galpón Producción|Galpón Producción|5,13E+02|1,06E+04|99,02%|
|Total|Total|Total|1,07E+04|100%|

(*) Valor inferior a 0,05.

Como se observa en Tabla 9, la emisión total de la planta corresponde a 10746,1 UO/s
y la unidad que presenta mayor emisión de olor es el Galpón de Producción con 10641,3
UO/s, correspondiente al 99,02% de la emisión total por segundo, seguido del Reactor
Biológico con 73,68 UO/s, correspondiente al 0,69% de la emisión total por segundo.

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 54
Quilicura”.

Informe Final

## 4.3 Implementación y Aplicación del Modelo de Dispersión CALPUFF

El modelo de dispersión CALPUFF se implementó para el año 2021 en la zona de estudio
utilizando el mismo dominio que el de WRF descrito en la Sección 3.2. El dominio
utilizado se presenta en Tabla 10, el que cubre un área de 62 x 62 km [2] con una resolución
de 1 km y que se muestra en Figura 24.

|Tabla 10: Características del dominio de modelación utilizada por el modelo CALPUFF en la zona de Quilicura-Santiago (archivo CALPUFF-Ready).|Col2|
|---|---|
|Características dominio CALPUFF-Ready|Características dominio CALPUFF-Ready|
|Resolución|1.000 x 1.000 (m)|
|No de celdas en dirección X|62|
|No de celdas en dirección Y|62|
|Coordenadas de referencia del origen del dominio*|UTM-E: 278.488 (m), UTM-N: 6.247.992 (m).|
|Total del área del dominio|3.844 (km2)|

*: Coordenada de referencia en UTM datum WGS 84 (aproximada), el dominio corresponde a la segunda

grilla anidada en la implementación del modelo WRF, la cual está en proyección Lambert Conformal Conic
(LCC).

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 55
Quilicura”.

Informe Final

Figura 24: Dominio de modelación de CALPUFF, 62 x 62 km [2], en coordenadas LCC.

4.3.1 Receptores de Grilla y Discretos

Como se mencionó anteriormente el modelo CALPUFF se implementó en un área de 62
x 62 km [2] con resolución de 1 km. Después de una primera corrida se determinó un zoom
en la zona circundante al proyecto para aumentar la resolución de cálculo de este
dominio, el que se disminuyó en CALPUFF a un área aproximada de 12,2 x 12,2 km [2] para
que entregue concentraciones en celdas de 200 metros de resolución. De esta forma,
CALPUFF entregó concentraciones para un área de 148,8 km [2] . Las características del
área de receptores tipo grilla se presentan en Tabla 11 se muestra en Figura 25.

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 56
Quilicura”.

Informe Final

Tabla 11: Características del área de receptores de Grilla.

|Item|Características|
|---|---|
|Kilómetros en dirección X|12,2|
|Kilómetros en dirección Y|12,2|
|Resolución|200 x 200 (m)|
|No de celdas en dirección X|61|
|No de celdas en dirección Y|61|
|Coordenadas de referencia del origen del dominio*|UTM-E: 332.957 (m), UTM-N: 6.304.314 (m)|
|Total de receptores|3.721|
|Área Total|148,84 (km2)|

*: Coordenada de referencia en UTM datum WGS 84 (aproximada), el dominio está en proyección Lambert

Conformal Conic (LCC).

Figura 25: Área de receptores de grilla de CALPUFF, 12 x 12 km [2], en coordenadas LCC.

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 57
Quilicura”.

Informe Final

En cuanto a los receptores discretos, se consideraron 13 receptores sensibles cercanos
a la planta de Ideal Cañaveral que corresponden a viviendas, colegio, centro de eventos,
servicentro y centros comerciales. Es importante mencionar que el proyecto se
encuentro emplazado en una zona industrial. Las características de estos receptores en
la modelación, como su ubicación y distancia al proyecto, se presentan en Tabla 12 y en
Figura 26 se muestra su ubicación.

Tabla 12: Receptores discretos.

|Receptor|Coordenadas UTM,<br>WGS 84 - Z19|Col3|Coordenadas LCC|Col5|Altitud (1)<br>(m.s.n.m.)|Distancia al<br>Proyecto (2)<br>(m)|
|---|---|---|---|---|---|---|
|Receptor|E (m)|N (m)|LCC-X (km)|LCC-Y (km)|LCC-Y (km)|LCC-Y (km)|
|R1 - Vivienda|338.205|6.310.940|-1,243|-0,061|488|1.180|
|R2 - Vivienda|337.490|6.310.745|-1,961|-0,244|486|1.910|
|R3 - Vivienda|337.985|6.311.180|-1,459|0,182|488|1.420|
|R4 - Colegio|339.270|6.308.810|-0,213|-2,209|487,5|1.820|
|R5 - Vivienda|338.630|6.308.720|-0,855|-2,288|486,5|2.090|
|R6 - Servicentro|339.170|6.309.110|-0,309|-1,907|487|1.540|
|R7 - Centro de eventos|337.760|6.309.720|-1,708|-1,274|485|1.980|
|R8 - Centro Comercial|340.600|6.310.290|1,141|-0,751|489,5|1.090|
|R9 - Centro Comercial|341.265|6.310.655|1,812|-0,397|519|1.170|
|R10 - Vivienda|337.825|6.313.220|-1,585|2,225|492|2.750|
|R11 - McDonals|341.330|6.312.490|1,907|1,437|573,5|2.380|
|R12 - Motel|339.650|6.312.132|0,221|1,107|489|1.180|
|R13 - Strip center|339.379|6.312.624|-0,041|1,603|492|1.650|

1: Altitud obtenida del terreno entregado por el modelo WRF en el formato CALMET.
2: Distancia mínima al proyecto: considera la distancia recta entre el receptor y la fuente de olor más cercana del

proyecto.

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 58
Quilicura”.

Informe Final

Figura 26: Ubicación de Receptores discretos.

4.3.2 Implementación de Fuentes de Olor

Las emisiones de olor del Proyecto se obtuvieron mediante la metodología de emisiones
de referencia, como lo recomienda la “Guía para la predicción y evaluación de impactos
por olor en el SEIA”. Tal como se presentó en sección 4.2, las emisiones de la planta se
obtuvieron mediante un estudio de olfatometría para la operación actual, emisiones que
se mantendrán durante la fase de Construcción del Proyecto. Para la fase de operación
se contempla una ampliación que consiste en otro galpón de producción para la nueva
línea de Takis, lo que incluye también un aumento en la planta de tratamiento de
residuos industriales líquidos (PTAR) que se encuentra actualmente en operación.

Las fuentes y emisiones consideradas en la modelación con CALPUFF se presentan en
Tabla 13 para el escenario más desfavorable de emisión, correspondiente a la Operación
del Proyecto.

Tabla 13: Tipos de fuentes y emisiones de olor.

|Escenario|Fuente de olor|Emisión (UO /s)<br>E|
|---|---|---|
|Operación|PTAR|1,297E+02|
|Operación|Área de contenedores|3,070E-01|

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 59
Quilicura”.

Informe Final

|Escenario|Fuente de olor|Emisión (UO /s)<br>E|
|---|---|---|
||Galpón Producción Actual|1,060E+04|
||Galpón Producción Nuevo (ampliación)|1,061E+03|

Las emisiones de la etapa de Operación presentadas en Tabla 13 se obtuvieron
mediante la referencia de las mediciones realizadas a la planta en el caso base. Las
emisiones de esta etapa se deben a lo siguiente:

- PTAR: Aumento de 200 m [3] /día a 248 m [3] /día de procesamiento (aumento de 2 m [3] /h).

Galpón de producción Nuevo: Se tomó como referencia el área de ambos galpones,
donde el galpón nuevo es aproximadamente un 10% del actual.

Las fuentes presentadas en Tabla 13 se implementaron en el modelo CALPUFF
considerando fuentes de área, cuyas coordenadas se muestran en Tabla 14 en
coordenadas UTM y su correspondiente coordenada Lambert Conformal Conic (LCC).
En esta tabla se presenta además la superficie correspondiente a la implementada en el
modelo CALPUFF. En el caso del galpón de producción actual, este se dividió en 4 áreas.
La única fuente que se agrega en el escenario de Operación es el galpón nuevo.

Las emisiones se implementaron considerando el peor escenario de emisiones, es decir,
con emisiones continuas durante todo el año.

Tabla 14: Coordenadas de las áreas donde se implementaron las fuentes de olor en el

modelo CALPUFF.

|Fuente|Col2|Superficie<br>(m2)|Puntos|UTM (WGS 84 - Z19)|Col6|Coordenadas LCC|Col8|
|---|---|---|---|---|---|---|---|
|Fuente|Fuente|Superficie<br>(m2)|Puntos|Este (m)|Norte (m)|LCC-X (km)|LCC-Y (km)|
|PTAS|PTAS|349|1|339.554|6.310.866|0,1041|-0,1576|
|PTAS|PTAS|349|2|339.564|6.310.871|0,1150|-0,1529|
|PTAS|PTAS|349|3|339.554|6.310.897|0,1055|-0,1264|
|PTAS|PTAS|349|4|339.543|6.310.893|0,0937|-0,1309|
|Área de contenedores|Área de contenedores|186|1|339.493|6.310.700|0,0412|-0,3225|
|Área de contenedores|Área de contenedores|186|2|339.505|6.310.705|0,0526|-0,3182|
|Área de contenedores|Área de contenedores|186|3|339.498|6.310.719|0,0460|-0,3039|
|Área de contenedores|Área de contenedores|186|4|339.487|6.310.715|0,0354|-0,3077|
||área-1|4.992|1|339.408|6.310.904|-0,0412|-0,1167|

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 60
Quilicura”.

Informe Final

|Fuente<br>Galpón<br>actual<br>área -2<br>área -3<br>área -4|Col2|Superficie<br>(m2)|Puntos|UTM (WGS 84 - Z19)|Col6|Coordenadas LCC|Col8|
|---|---|---|---|---|---|---|---|
|Fuente<br>Galpón<br>actual<br>área -2<br>área -3<br>área -4|Fuente<br>Galpón<br>actual<br>área -2<br>área -3<br>área -4|Superficie<br>(m2)|Puntos|Este (m)|Norte (m)|LCC-X (km)|LCC-Y (km)|
|Fuente<br>Galpón<br>actual<br>área -2<br>área -3<br>área -4|Fuente<br>Galpón<br>actual<br>área -2<br>área -3<br>área -4|Superficie<br>(m2)|2|339.495|6.310.941|0,0467|-0,0813|
|Fuente<br>Galpón<br>actual<br>área -2<br>área -3<br>área -4|Fuente<br>Galpón<br>actual<br>área -2<br>área -3<br>área -4|Superficie<br>(m2)|3|339.478|6.310.989|0,0303|-0,0338|
|Fuente<br>Galpón<br>actual<br>área -2<br>área -3<br>área -4|Fuente<br>Galpón<br>actual<br>área -2<br>área -3<br>área -4|Superficie<br>(m2)|4|339.387|6.310.955|-0,0607|-0,0663|
|Fuente<br>Galpón<br>actual<br>área -2<br>área -3<br>área -4|área -2|8.001|1|339.433|6.310.840|-0,0168|-0,1817|
|Fuente<br>Galpón<br>actual<br>área -2<br>área -3<br>área -4|área -2|8.001|2|339.540|6.310.881|0,0903|-0,1421|
|Fuente<br>Galpón<br>actual<br>área -2<br>área -3<br>área -4|área -2|8.001|3|339.514|6.310.947|0,0655|-0,0756|
|Fuente<br>Galpón<br>actual<br>área -2<br>área -3<br>área -4|área -2|8.001|4|339.408|6.310.904|-0,0411|-0,1171|
|Fuente<br>Galpón<br>actual<br>área -2<br>área -3<br>área -4|área -3|6.066|1|339.456|6.310.784|0,0053|-0,2385|
|Fuente<br>Galpón<br>actual<br>área -2<br>área -3<br>área -4|área -3|6.066|2|339.561|6.310.824|0,1109|-0,2001|
|Fuente<br>Galpón<br>actual<br>área -2<br>área -3<br>área -4|área -3|6.066|3|339.540|6.310.881|0,0912|-0,1427|
|Fuente<br>Galpón<br>actual<br>área -2<br>área -3<br>área -4|área -3|6.066|4|339.433|6.310.839|-0,0165|-0,1823|
|Fuente<br>Galpón<br>actual<br>área -2<br>área -3<br>área -4|área -4|5.035|1|339.481|6.310.720|0,0292|-0,3019|
|Fuente<br>Galpón<br>actual<br>área -2<br>área -3<br>área -4|área -4|5.035|2|339.548|6.310.765|0,0970|-0,2582|
|Fuente<br>Galpón<br>actual<br>área -2<br>área -3<br>área -4|área -4|5.035|3|339.548|6.310.818|0,0974|-0,2058|
|Fuente<br>Galpón<br>actual<br>área -2<br>área -3<br>área -4|área -4|5.035|4|339.456|6.310.783|0,0056|-0,2393|
|Galpón nuevo<br>(ampliación)|Galpón nuevo<br>(ampliación)|5.210|1|339.515|6.310.592|0,0608|-0,4311|
|Galpón nuevo<br>(ampliación)|Galpón nuevo<br>(ampliación)|5.210|2|339.562|6.310.611|0,1080|-0,4124|
|Galpón nuevo<br>(ampliación)|Galpón nuevo<br>(ampliación)|5.210|3|339.524|6.310.707|0,0717|-0,3159|
|Galpón nuevo<br>(ampliación)|Galpón nuevo<br>(ampliación)|5.210|4|339.477|6.310.688|0,0250|-0,3341|

El detalle de la distribución de las fuentes de área del Proyecto se ilustra en Figura 27.
En esta figura se muestran las fuentes consideradas en Google Earth, panel a), y las
fuentes implementadas en el modelo CALPUFF en coordenadas LCC.

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 61
Quilicura”.

Informe Final

Figura 27: Distribución de fuentes emisoras de olor del proyecto Planta Ideal Quilicura.

a) Fuentes en Google Earth, b) Fuentes implementadas en CALPUFF, en
coordenadas LCC.

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 62
Quilicura”.

Informe Final

## 4.4 Resultados de la Aplicación del Sistema CALPUFF

En esta sección se presentan los resultados del sistema de modelación CALPUFF,
considerando el año meteorológico 2021 y los escenarios de emisión de olores
presentados en la sección anterior.

Como en Chile no existe normativa que regule las concentraciones de olor se tomó como
referencia la normativa sobre olores holandesa en lo que respecta a Panaderías de
bizcochos y pastelería, específicamente en el titulo B4 del documento: “B4 Rusk and
pastry bakeries”.

En Tabla 15 se indican los niveles de molestia de olores de dicha norma. Como se
observa en esta tabla, el proyecto considera como norma de referencia 5,0 UO E /m [3] para
el percentil 98 de las concentraciones horarias.

Tabla 15: Normas de olor holandesa para Panaderías de bizcochos y pastelería.

|Tipo de Instalación|Norma (UO /m3)<br>E|
|---|---|
|Panaderías de bizcochos y pastelería industrial|Percentil 98: 5,0|

A continuación, se presentan los resultados de concentraciones odorantes modelados
con CALPUFF en la zona de estudio.

4.4.1 Área de Influencia

Como se presenta en la “Guía sobre el Área de Influencia en el Sistema de Evaluación de
Impacto Ambiental” del SEA (2017): En la letra a) del artículo 2 del Reglamento del SEIA
se define área de influencia (AI) como ‘El área o espacio geográfico, cuyos atributos,
elementos naturales o socioculturales deben ser considerados con la finalidad de definir
si el proyecto o actividad genera o presenta alguno de los efectos, características o
circunstancias del artículo 11 de la Ley, o bien para justificar la inexistencia de dichos
efectos, características o circunstancias’.

Criterio 1: El AI corresponde al área o espacio geográfico de donde se obtiene la
información necesaria para predecir y evaluar los impactos en los elementos del medio
ambiente. La predicción y evaluación de impactos ambientales se debe realizar tanto en
el caso que al SEIA se presente un EIA como una DIA. Si bien el capítulo de predicción y
evaluación de impactos no forma parte de los contenidos mínimos de una DIA, es
necesario realizar dicha predicción y evaluación para poder identificar los impactos

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 63
Quilicura”.

Informe Final

ambientales que el proyecto genera y estimarlos cuantitativa y cualitativamente
(predicción) y posteriormente evaluar su significancia (evaluación); lo anterior con el fin
de obtener los fundamentos necesarios para justificar la inexistencia de los ECC del
artículo 11 de la Ley, conforme a lo establecido en el Título II del Reglamento del SEIA.

Criterio 2: Cuando el Reglamento del SEIA se refiere al AI como un espacio geográfico,
se entiende no sólo el espacio terrestre, sino que, dependiendo del elemento del medio
ambiente receptor de impacto, éste puede ser también un espacio aéreo y/o acuático.

En este contexto es que se realizó la modelación con el sistema de modelación
WRF/CALPUFF, que consideró un área total de 62 x 62 km [2] y un área de evaluación de
12 x 12 km [2] (ver sección 4.3.1). Dentro de esta zona se obtuvo el área de Influencia de
olor que se presenta en Figura 28. Esta área fue obtenida a partir de la zona que cubre
la isolínea de concentración de olor de 1 UO E /m [3], considerado por definición como el
umbral de detección de olor, como la concentración teórica mínima para generar un
estímulo que pueda ser detectado en un porcentaje específico de la población, que por
convención generalmente se usa el 50% de la población.

El área de influencia estimada, rodeada por la isolínea de olor de 1 UO E /m [3], corresponde
a aproximadamente 320 ha alrededor del Proyecto. Esta área considera los resultados
del escenario de Operación, el cual tiene las mayores emisiones, asumiendo el peor
escenario. Esta isolínea considera valores puntuales a lo largo del año modelado, al ser
valores horarios que se presentan una vez al año, por lo que resulta de forma ovalada
alrededor del proyecto.

Cabe destacar, que la normativa referencial ocupada establece límites de concentración
iguales a 5,0 UO E /m [3] para este tipo de actividad, por lo cual se puede afirmar que las
concentraciones modeladas son de baja magnitud, lo que implica a su vez, que el área
de influencia simulada se encuentra sobreestimada.

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 64
Quilicura”.

Informe Final

Figura 28: Área de Influencia por dispersión de olor.

4.4.2 Resultados Odorantes en Receptores Discretos

Los resultados de concentraciones de olor modelados con CALPUFF se presentan como
máximo horario, percentil 99,5 y percentil 98 de las concentraciones horarias del año
2021 para el escenario de Operación del Proyecto en Tabla 16 en los receptores de
interés presentados anteriormente en Tabla 12. En esta tabla se muestra también la
norma de referencia utilizada.

Como se mencionó anteriormente (ver 4.3.1), se consideraron 13 receptores sensibles
cercanos a la planta de Ideal Cañaveral que corresponden a viviendas, colegio, centro
de eventos, servicentro y centros comerciales. Las características de estos receptores
se presentaron en Tabla 12.

En Tabla 16 se observa que las concentraciones de olor más altas se dan en los
receptores discretos R1 y R6, que son las primeras viviendas que se encuentran hacia
el Oeste del Proyecto y el servicentro que se encuentra hacia el Sur, respectivamente.
Sin embargo, ningún receptor supera la norma de olor tomada como referencia.

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 65
Quilicura”.

Informe Final

Por otra parte, en Tabla 17 se presenta la cantidad de excedencias horarias de la norma
de referencia (5,0 UO E /m [3] como percentil 98 de las concentraciones horarias), como
porcentaje anual y cantidad de horas al año. En esta tabla se observa que ninguno de
los receptores de interés tiene horas al año con concentraciones sobre 5,0 UO E /m [3] .

|bla 16: Máximo horario, percentil 99,5 y percentil 98 de las concentraciones horari de olor modeladas por el sistema CALPUFF, escenario Operación.|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|Escenario de Operación|Escenario de Operación|Escenario de Operación|Escenario de Operación|Escenario de Operación|Escenario de Operación|
|Punto<br>Receptor|Concentración modelada (UOE/m3)|Concentración modelada (UOE/m3)|Concentración modelada (UOE/m3)|Límite norma<br>referencia<br>(UOE/m3)|Cumplimiento<br>Normativo|
|Punto<br>Receptor|Máximo Horario|Percentil 99,5<br>conc. horarias|Percentil 98<br>conc. horarias|Percentil 98<br>conc. horarias|Percentil 98<br>conc. horarias|
|R1|3,1|1,1|0,5|5,0|Si|
|R2|1,0|0,3|0,1|0,1|Si|
|R3|1,3|0,5|0,3|0,3|Si|
|R4|1,6|0,6|0,3|0,3|Si|
|R5|1,3|0,4|0,2|0,2|Si|
|R6|2,6|0,9|0,4|0,4|Si|
|R7|0,8|0,3|0,1|0,1|Si|
|R8|2,4|0,9|0,4|0,4|Si|
|R9|0,5|0,3|0,2|0,2|Si|
|R10|0,3|0,2|0,1|0,1|Si|
|R11|0,2|0,2|0,1|0,1|Si|
|R12|1,4|0,7|0,4|0,4|Si|
|R13|0,8|0,4|0,2|0,2|Si|

Tabla 17: Cantidad de excedencias horarias de la norma de referencia (5,0 UO E /m [3] ) en

los receptores discretos modelados por el sistema CALPUFF, escenario de
Operación.

|ón.|Col2|Col3|
|---|---|---|
|Punto Receptor|Excedencia de norma - Escenario<br>Operación|Excedencia de norma - Escenario<br>Operación|
|Punto Receptor|(%)|(h/año)|
|R1|0,000|0|
|R2|0,000|0|
|R3|0,000|0|
|R4|0,000|0|
|R5|0,000|0|

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 66
Quilicura”.

Informe Final

|Punto Receptor|Excedencia de norma - Escenario<br>Operación|Col3|
|---|---|---|
|Punto Receptor|(%)|(h/año)|
|R6|0,000|0|
|R7|0,000|0|
|R8|0,000|0|
|R9|0,000|0|
|R10|0,000|0|
|R11|0,000|0|
|R12|0,000|0|
|R13|0,000|0|

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 67
Quilicura”.

Informe Final

4.4.3 Curvas Odorantes

Los resultados de la modelación de olor con CALPUFF para el escenario de Operación
se presentan también como isolíneas de máximas concentraciones horarias, percentil
99,5 de las concentraciones horarias y percentil 98 de las concentraciones horarias de
olor, como se indica en la “Guía a para la predicción y evaluación de impactos por olor
en el SEIA”, en Figura 29 a Figura 31.

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 68
Quilicura”.

Informe Final

Figura 29: Mapa de curvas isodoras de concentraciones máximas horarias del año 2021 modelados con CALPUFF en

la zona de estudio, escenario de Operación.

Estudio EM2022/200-03 | Better

69
“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal Quilicura”.

Informe Final

Figura 30: Mapa de curvas isodoras percentil 99,5 de las concentraciones horarias del año 2021 modelados con

CALPUFF en la zona de estudio, escenario de Operación.

Estudio EM2022/200-03 | Better

70
“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal Quilicura”.

Informe Final

Figura 31: Mapa de curvas isodoras percentil 98 de las concentraciones horarias del año 2021 modelados con

CALPUFF en la zona de estudio, escenario de Operación.

Estudio EM2022/200-03 | Better

71
“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal Quilicura”.

Informe Final

4.4.4 Punto de Máxima Concentración Odorante

Como se observó en Figura 29 a Figura 31, las máximas concentraciones odorantes se
presentaron muy cercanas y dentro del área de emplazamiento del Proyecto. Las
concentraciones de olor y ubicación del Punto de Máxima Concentración Odorante se
presentan en Tabla 18 para el escenario de Operación.

Tabla 18: Máximo horario, percentil 99,5 y percentil 98 de las concentraciones horarias

|de olor en el Punto de Máxima Concentración Odorante - Operación.|Col2|Col3|
|---|---|---|
|Punto de Máxima Concentración de Olor - Escenario Operación|Punto de Máxima Concentración de Olor - Escenario Operación|Punto de Máxima Concentración de Olor - Escenario Operación|
|Máximo Horario (UOE/m3)|Máximo Horario (UOE/m3)|16,62|
|Ubicación|LCC-X (m)|-100|
|Ubicación|LCC-Y (m)|-100|
|Ubicación|UTM-E WGS 84 - Z19 (m)|339.349|
|Ubicación|UTM-N WGS 84 - Z19 (m)|6.310.920|
|Ubicación|Calle Cerro San Luis|Calle Cerro San Luis|
|Percentil 99,5 concentraciones horarias (UOE/m3)|Percentil 99,5 concentraciones horarias (UOE/m3)|9,42|
|Ubicación|LCC-X (m)|100|
|Ubicación|LCC-Y (m)|-300|
|Ubicación|UTM-E WGS 84 - Z19 (m)|339.552|
|Ubicación|UTM-N WGS 84 - Z19 (m)|6.310.724|
|Ubicación|Dentro del área del Proyecto|Dentro del área del Proyecto|
|Percentil 98 concentraciones horarias (UOE/m3)|Percentil 98 concentraciones horarias (UOE/m3)|6,10|
|Ubicación|LCC-X (m)|-100|
|Ubicación|LCC-Y (m)|-100|
|Ubicación|UTM-E WGS 84 - Z19 (m)|339.349|
|Ubicación|UTM-N WGS 84 - Z19 (m)|6.310.920|
|Ubicación|Calle Cerro San Luis|Calle Cerro San Luis|

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 127
Quilicura”.

Informe Final

# CAPÍTULO 5: CONCLUSIONES

En este Capítulo se presentan las conclusiones correspondientes al Informe Final del
“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta
Ideal Quilicura”.

Los aportes de olor del Proyecto en la zona de estudio, que consideró un área de 62 x
62 km [2], se obtuvieron mediante la ejecución del modelo CALPUFF considerando la
meteorología entregada por el modelo WRF del año 2021 y las emisiones de olor de los
procesos emisores del Proyecto medidos mediante un estudio de olfatometría para la
operación actual.

Los resultados finales de este estudio permiten concluir lo siguiente:

 Las concentraciones de olor más altas se dan en los receptores discretos de

interés R1 y R6, que son las primeras viviendas que se encuentran hacia el Oeste
del Proyecto y el servicentro que se encuentra hacia el Sur, respectivamente. Sin
embargo, ningún receptor sensible considerado supera la norma de olor tomada
como referencia de 5,0 UO E /m [3] para el percentil 98 de las concentraciones
horarias. En los receptores sensibles no se observan valores horarios sobre la
norma en alguna hora del año modelado.

 - Las máximas concentraciones odorantes alcanzan a 6,1 UO E /m [3] como percentil

98, este valor se presenta concentrado en un área de la calle lateral al
emplazamiento de la planta Ideal. Los valores de máximas concentraciones se
dan en áreas dentro y fuera de la planta en forma muy concentrada.

 El área de influencia estimada tiene una forma de ovalada y corresponde a

aproximadamente 320 ha alrededor del Proyecto. Esta área fue obtenida a partir
de la zona que cubre la isolínea de concentración de olor máximo horario de 1
UO E /m [3], considerando que el umbral de detección de olor por definición es 1
UO E /m [3] como la concentración teórica mínima para generar un estímulo que
pueda ser detectado en un porcentaje específico de la población, que por
convención generalmente se usa el 50% de la población.

Cabe destacar, que la normativa referencial ocupada establece límites de
concentración iguales a 5,0 UO E /m [3] para este tipo de actividad, por lo cual se

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 128
Quilicura”.

Informe Final

puede afirmar que las concentraciones modeladas son de baja magnitud, lo que
implica a su vez, que el área de influencia simulada se encuentra sobreestimada.

De acuerdo al análisis presentado, estos resultados implican que los máximos
aportes de olor a la zona de estudio debido al Proyecto de la Planta Ideal Quilicura
no tienen un impacto significativo y no representan un peligro para la salud de
las personas del área de emplazamiento del proyecto, cumplimento la normativa
ambiental.

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 129
Quilicura”.

Informe Final

# CAPÍTULO 6: BIBLIOGRAFIA

Orfanoz, A. (2016). Estratificación vertical y transporte viento abajo de contaminantes
urbanos de Santiago de Chile (Doctoral dissertation, Tesis de maestría). Universidad de
Chile, Santiago de Chile).

Servicio de Evaluación Ambiental, SEA (2012). Guía para el uso de modelos de calidad
del aire en el SEIA.

Servicio de Evaluación Ambiental, SEA (2017). Guía para la Predicción y Evaluación de
Impactos por Olor en el SEIA.

Smith, P. (2011). Distribución termal intraurbana en Santiago de chile. Aporte a la
gestión ambiental de la ciudad a partir de la construcción de un modelo que permita
generar un mapa térmico de verano. Facultad de Ciencias Forestales y Conservación de
la Naturaleza. Universidad de Chile. Recuperado de:
http://mgpa.forestaluchile.cl/Tesis/Smith%20Pamela.pdf.

[Imagen comuna de Quilicura: https://www.ecured.cu/index.php?curid=739676](https://www.ecured.cu/index.php?curid=739676)

Imagen Región Metropolitana: De B1mbo - Trabajo propio, CC BY-SA 2.5,
[https://commons.wikimedia.org/w/index.php?curid=3082352](https://commons.wikimedia.org/w/index.php?curid=3082352)

Estudio EM2022/200-03 | Better

“Estudio de Dispersión de Olores del Proyecto Ampliación y Regularización de Planta Ideal 130
Quilicura”.

Informe Final