---
title: Sin título
author: EMwalnut@outlook.com
date: D:20231109211322-03'00'
language: es
type: report
pages: 149
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

ESTUDIO EM2023-200-54: “Estudio de Calidad de Aire del Proyecto Planta
Depuradora de RILes Empresa San Lorenzo”.

Ecoazul

Octubre 2023

CAPÍTULO 1: INTRODUCCIÓN .................................................................................. 11

CAPÍTULO 2: ANÁLISIS DE LA INFORMACIÓN METEOROLÓGICA DE LA ZONA DEL

PROYECTO ................................................................................................................ 13

2.1 Introducción ................................................................................................................. 13

2.2 Descripción Topográfica y Climática de la Zona de Estudio ...................................... 13

2.3 Línea Base Meteorológica de la Zona de Estudio Durante el Año 2022 .................... 15

2.3.1 Series de Tiempo de Variables Meteorológicas Observadas en el Año 2022 ............... 16

2.3.2 Ciclos Diarios de Variables Meteorológicas Observadas Durante el Año 2022............ 18

2.3.3 Ciclos Estacionales de Variables Meteorológicas Observados Durante el Año 2022 .. 20

2.3.4 Rosas de Viento Observadas Durante el Año 2022 ......................................................... 22

2.4 Línea Base de Calidad de Aire de la Zona de Estudio ................................................. 24

2.4.1 Descripción de la Red de Monitoreo de Calidad de Aire Existente en la Zona de Estudio

............................................................................................................................................. 24

2.4.2 Marco Jurídico Vigente en Chile ....................................................................................... 25

2.4.3 Información de Calidad de Aire para Material Particulado Respirable (MP10), Periodo
2020 - 2022. .......................................................................................................................................... 26

2.4.4 Información de Calidad de Aire para Dióxido de Azufre (SO 2 ), Periodo 2020 -2022. .. 28

2.4.5 Información de Calidad de Aire para Dióxido de Nitrógeno (NO 2 ), Periodo 2020 -2022.
............................................................................................................................................. 30

CAPÍTULO 3: IMPLEMENTACIÓN, APLICACIÓN Y RESULTADOS DEL MODELO
METEOROLÓGICO WRF ............................................................................................. 32

3.1 Introducción ................................................................................................................. 32

3.2 Implementación del Modelo Meteorológico WRF ....................................................... 33

3.3 Resultados del Modelo WRF en la Zona de Estudio ................................................... 35

3.3.1 Series de Tiempo de Variables Meteorológicas Modeladas con WRF Año 2022 ......... 35

3.3.2 Ciclos Diarios de Variables Meteorológicas Modeladas con WRF para el Año 2022 ... 38

3.3.3 Ciclos Estacionales de Variables Meteorológicas Modeladas con WRF Durante el Año

2022 ............................................................................................................................................. 40

i

3.3.4 Rosas de Viento Modeladas con WRF Durante el Año 2022 .......................................... 42

3.3.5 Campos de Viento Promedios Modelados con WRF durante el Año 2022 .................... 44

3.4 Análisis de Incertidumbre de los Resultados del Modelo WRF Respecto de los Datos
Observados en Estación Los Andes Durante el Año 2022 ..................................................... 56

3.4.1 Análisis Cualitativo Series de Tiempo Observados y Modelados con WRF, Año 2022 57

3.4.2 Análisis Cualitativo de Ciclos Diarios Observados y Modelados con WRF, Año 2022 . 60

3.4.3 Análisis Cualitativo de Ciclos Estacionales Observados y Modelados con WRF, Año

2022 ............................................................................................................................................. 62

3.4.4 Análisis Cualitativo de Rosas de Viento Observadas y Modeladas con WRF, Año 2022 .

............................................................................................................................................. 64

3.4.5 Análisis Cuantitativo .......................................................................................................... 66

CAPÍTULO 4: IMPLEMENTACIÓN, APLICACIÓN Y RESULTADOS DEL MODELO DE
DISPERSIÓN CALPUFF ............................................................................................. 68

4.1 Introducción ................................................................................................................. 68

4.2 Implementación y Aplicación del Modelo de Dispersión CALPUFF ........................... 69

4.2.1 Receptores de Grilla y Discretos ....................................................................................... 70

4.2.2 Implementación de Fuentes Emisoras de Contaminantes ............................................. 76

4.3 Resultados de la Aplicación del Sistema CALPUFF.................................................... 87

4.3.1 Escenario de Construcción ............................................................................................... 87

4.3.2 Escenario de Operación ................................................................................................... 111

4.3.3 Área de Influencia ............................................................................................................ 135

4.3.4 Análisis del Aporte del Proyecto ..................................................................................... 142

CAPÍTULO 5: CONCLUSIONES ................................................................................ 144

CAPÍTULO 6: BIBLIOGRAFIA ................................................................................... 146

ii

Tabla 1: Estaciones meteorológicas en el dominio de la zona de Estudio. ..................................... 15

<!-- INICIO TABLA 1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Respecto al tratamiento de los datos, estos fueron revisados y validados siguiendo los lineamientos de la EPA, en relación a registros incoherentes, datos sin variación o saltos bruscos entre horas de cada variable y revisión de variabilidad diaria y estacionalidad. -->

**Tabla 1: Estaciones meteorológicas en el dominio de la zona de Estudio.**

| Estación | Abreviatura | Latitud | Longitud | Variables Medidas (%) | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Estación | Abreviatura | Latitud | Longitud | VV | DV | HR | T |
| Los Andes | LA | -32.846426 | -70.586475 | 99,8 | 99,8 | 99,9 | 99,9 |

<!-- Estadísticas: 2 filas, 8 columnas -->
<!-- Contexto posterior: -->
<!-- VV: velocidad de viento; DV: dirección de viento; HR: Humedad Relativa; T: temperatura, S.D: Sin Datos Estudio EM2023/200-54 | Ecoazul -->
<!-- FIN TABLA 1 -->


Tabla 2: Estación monitora de calidad de aire en el dominio de la zona de estudio ...................... 24

<!-- INICIO TABLA 2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Las estaciones de monitoreo disponibles en la zona de estudio se presentan en Tabla 2. En esta tabla se indica su ubicación geográfica en coordenadas UTM (WGS 84) y la disponibilidad de datos de contaminantes. La ubicación de estas estaciones se muestra en Figura 7. -->

**Tabla 2: Estación monitora de calidad de aire en el dominio de la zona de estudio**

| Red | Estación | Coordenadas UTM<br>Datum WGS 84 - Z19 | Col4 | MP10 | MP2,5 | NO<br>2 | SO<br>2 | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Red | Estación | UTM-E (m) | UTM-N (m) | UTM-N (m) | UTM-N (m) | UTM-N (m) | UTM-N (m) | UTM-N (m) |
| Ministerio del Medio<br>Ambiente | Los Andes | 351.534 | 6.364.623 |  |  | X |  |  |

<!-- Estadísticas: 2 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Estudio EM2023/200-54 | Ecoazul 24 “Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” -->
<!-- FIN TABLA 2 -->


Tabla 3: Normas Primarias y Secundarias de calidad de aire de Chile para los contaminantes de

<!-- INICIO TABLA 3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- 25 “Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” Informe Final -->

**Tabla 3: Normas Primarias y Secundarias de calidad de aire de Chile para los**

| Contaminante | Periodo de Evaluación | Valor Norma | Norma |
| --- | --- | --- | --- |
| Material Particulado<br>Respirable<br>(MP10) | Concentración de 24 horas | 130 (μg/Nm3) | Norma Primaria<br>D.S. No 12/2021 del<br>MINISTERIO DEL<br>MEDIO AMBIENTE |
| Material Particulado<br>Respirable<br>(MP10) | Concentración anual | 50 (μg/Nm3) | 50 (μg/Nm3) |
| Material Particulado<br>Fino Respirable (MP2,5) | Concentración de 24 horas | 50 (μg/Nm3) | Norma Primaria<br>D.S. No 12/2011 del<br>MINISTERIO DEL<br>MEDIO AMBIENTE |
| Material Particulado<br>Fino Respirable (MP2,5) | Concentración anual | 20 (μg/Nm3) | 20 (μg/Nm3) |
| Dióxido de Nitrógeno<br>(NO2) | Concentración de 1 hora | 400 (μg/Nm3) | Norma Primaria<br>D.S. No 114/2002 del<br>MINSEGPRES |
| Dióxido de Nitrógeno<br>(NO2) | Concentración anual | 100 (μg/Nm3) | 100 (μg/Nm3) |
| Dióxido de Azufre (SO2) | Concentración anual | 60 (μg/Nm3) | Norma Primaria<br>D.S. No 104/2018 del<br>MINISTERIO DEL<br>MEDIO AMBIENTE |
| Dióxido de Azufre (SO2) | Concentración de 24 horas | 130 (μg/Nm3) | 130 (μg/Nm3) |
| Dióxido de Azufre (SO2) | Concentración de 1 hora | 350 (μg/Nm3) | 350 (μg/Nm3) |
| Dióxido de Azufre (SO2) | Concentración anual | 80 (μg/Nm3) | Norma Secundaria<br>DS No 22/2009<br>MINSEGPRES para la<br>zona norte |
| Dióxido de Azufre (SO2) | Concentración de 24 horas | 365 (μg/Nm3) | 365 (μg/Nm3) |
| Dióxido de Azufre (SO2) | Concentración de 1 hora | 1.000 (μg/Nm3) | 1.000 (μg/Nm3) |
| Monóxido de Carbono<br>(CO) | Concentración de 8 horas | 10.000 (μg/Nm3) | Norma Primaria<br>D.S. No 115/2002 del<br>MINSEGPRES |
| Monóxido de Carbono<br>(CO) | Concentración de 1 hora | 30.000 (μg/Nm3) | 30.000 (μg/Nm3) |
| Material Particulado<br>Sedimentable (MPS) | Concentración anual | 200 (mg/m2-día) | Ordenanza<br>Confederación Suiza |

<!-- Estadísticas: 15 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- 2.4.3 Información de Calidad de Aire para Material Particulado Respirable (MP10), Periodo 2020 - 2022. -->
<!-- FIN TABLA 3 -->

interés del Proyecto. .............................................................................................................. 26

Tabla 4: Concentración anual de MP10 registrada por la estación Los Andes. Periodo 20202022. ....................................................................................................................................... 27

<!-- INICIO TABLA 4 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Por otra parte, en Tabla 5 se presentan los Percentiles 98 de las concentraciones de 24 horas de MP10, registrados por la estación Catemu durante el periodo 2020 - 2022. En esta tabla se observa que, considerando la norma diaria del D.S. 12/2022, se supera la norma durante todos los años presentados. -->

**Tabla 4: Concentración anual de MP10 registrada por la estación Los Andes. Periodo**

| Estación | Año | % Datos<br>mensuales<br>válidos | Promedio<br>Anual<br>(μg/m3N) | Promedio<br>Trianual<br>(μg/m3N) | % de la Norma Anual (D.S. No 12/2022 del<br>Ministerio del Medio Ambiente, 50<br>μg/m3N) |
| --- | --- | --- | --- | --- | --- |
| Catemu | 2020 | 100 | 126,92 | 108,42 | 217 |
| Catemu | 2021 | 100 | 96,58 | 96,58 | 96,58 |
| Catemu | 2022 | 100 | 101,76 | 101,76 | 101,76 |

<!-- Estadísticas: 3 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- Tabla 5: Percentil 98 de las concentraciones 24 horas de MP10 registrada por la estación Los Andes. Periodo 2020 - 2022. |Estación|Año|% Datos 24<br>horas<br>válidos|Percentil 98<br>(μg/m3N)|% de la Norma Diaria (D.S. No 12/2022 del<br>Ministerio del Medio Ambiente, 130<br>μg/m3N)| -->
<!-- FIN TABLA 4 -->


Tabla 5: Percentil 98 de las concentraciones 24 horas de MP10 registrada por la estación Los

<!-- INICIO TABLA 5 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |---|---|---|---|---|---| |Catemu|2020|100|126,92|108,42|217| |Catemu|2021|100|96,58|96,58|96,58| |Catemu|2022|100|101,76|101,76|101,76| -->

**Tabla 5: Percentil 98 de las concentraciones 24 horas de MP10 registrada por la**

| Estación | Año | % Datos 24<br>horas<br>válidos | Percentil 98<br>(μg/m3N) | % de la Norma Diaria (D.S. No 12/2022 del<br>Ministerio del Medio Ambiente, 130<br>μg/m3N) |
| --- | --- | --- | --- | --- |
| Catemu | 2020 | 99,7 | 193,4 | 149 |
| Catemu | 2021 | 98,1 | 193,8 | 149 |
| Catemu | 2022 | 100,0 | 177,9 | 137 |

<!-- Estadísticas: 3 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- Estudio EM2023/200-54 | Ecoazul 27 “Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” -->
<!-- FIN TABLA 5 -->

Andes. Periodo 2020 - 2022. ............................................................................................... 27

Tabla 6: Concentración anual SO 2 registrada en la estación Catemu. Periodo 2020 - 2022........ 28

<!-- INICIO TABLA 6 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- durante el periodo considerado. Por otra parte, en Figura 9 se muestra la serie de tiempo de SO 2 registrada en la estación Catemu durante el periodo 2020 - 2022. -->

**Tabla 6: Concentración anual SO 2 registrada en la estación Catemu. Periodo 20202022.**

| Estación | Año | % Datos<br>mensuales<br>válidos | Promedio<br>Anual<br>(μg/m3N) | Promedio<br>Trianual<br>(μg/m3N) | % de la Norma anual (D.S. No 104/2019<br>del Ministerio del Medio Ambiente, 60<br>μg/m3N) |
| --- | --- | --- | --- | --- | --- |
| Catemu | 2020 | 100 | 12,07 | 11,91 | 20 |

<!-- Estadísticas: 1 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- Estudio EM2023/200-54 | Ecoazul 28 “Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” -->
<!-- FIN TABLA 6 -->


Tabla 7: Percentil 99 de las concentraciones diarias de SO 2 registrados en la estación Catemu.

<!-- INICIO TABLA 7 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Estación|Año|% Datos<br>mensuales<br>válidos|Promedio<br>Anual<br>(μg/m3N)|Promedio<br>Trianual<br>(μg/m3N)|% de la Norma anual (D.S. No 104/2019<br>del Ministerio del Medio Ambiente, 60<br>μg/m3N)| |---|---|---|---|---|---| ||2021|100|13,27||| ||2022|100|10,40|10,40|10,40| -->

**Tabla 7: Percentil 99 de las concentraciones diarias de SO 2 registrados en la estación**

| Estación | Año | % Datos 24<br>horas<br>válidos | Percentil 99<br>(μg/m3N) | Promedio<br>Trianual<br>(μg/m3N) | % de la Norma 24 horas (D.S. No<br>104/2019 del Ministerio del Medio<br>Ambiente, 150 μg/m3N) |
| --- | --- | --- | --- | --- | --- |
| Catemu | 2020 | 99 | 40,25 | 32,78 | 22 |
| Catemu | 2021 | 98 | 34,04 | 34,04 | 34,04 |
| Catemu | 2022 | 98 | 24,05 | 24,05 | 24,05 |

<!-- Estadísticas: 3 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- Tabla 8: Percentil 99 de las concentraciones de 1 hora de SO 2 registrada en la estación Catemu. Periodo 2020 - 2022. |Estación|Año|% Datos 1<br>hora<br>válidos|Percentil<br>98,5<br>(μg/m3N)|Promedio<br>Trianual<br>(μg/m3N)|% de la Norma 1 hora (D.S. No<br>104/2019 del Ministerio del Medio<br>Ambiente, 350 μg/m3N)| -->
<!-- FIN TABLA 7 -->

Periodo 2020 - 2022. ............................................................................................................ 29

Tabla 8: Percentil 99 de las concentraciones de 1 hora de SO 2 registrada en la estación Catemu.

<!-- INICIO TABLA 8 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |---|---|---|---|---|---| |Catemu|2020|99|40,25|32,78|22| |Catemu|2021|98|34,04|34,04|34,04| |Catemu|2022|98|24,05|24,05|24,05| -->

**Tabla 8: Percentil 99 de las concentraciones de 1 hora de SO 2 registrada en la estación**

| Estación | Año | % Datos 1<br>hora<br>válidos | Percentil<br>98,5<br>(μg/m3N) | Promedio<br>Trianual<br>(μg/m3N) | % de la Norma 1 hora (D.S. No<br>104/2019 del Ministerio del Medio<br>Ambiente, 350 μg/m3N) |
| --- | --- | --- | --- | --- | --- |
| Catemu | 2020 | 98 | 59,00 | 55,33 | 16 |
| Catemu | 2021 | 98 | 59,00 | 59,00 | 59,00 |
| Catemu | 2022 | 98 | 48,00 | 48,00 | 48,00 |

<!-- Estadísticas: 3 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- Estudio EM2023/200-54 | Ecoazul 29 “Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” -->
<!-- FIN TABLA 8 -->

Periodo 2020 - 2022. ............................................................................................................ 29

Tabla 9: Concentración anual NO 2 registrada en la estación Los Andes. Periodo 2020 - 2022. .. 30

<!-- INICIO TABLA 9 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- anual ni horaria. Por otra parte, en Figura 10 se muestra la serie de tiempo de NO 2 en la estación Los Andes disponibles en el SINCA, durante el periodo 2020 - 2022. -->

**Tabla 9: Concentración anual NO 2 registrada en la estación Los Andes. Periodo 2020**

| Col1 | - 2022. | Col3 | Col4 | Col5 | Col6 |
| --- | --- | --- | --- | --- | --- |
| Estación | Año | % Datos<br>trimensuales<br>válidos | Promedio<br>Anual<br>(μg/m3N) | Promedio<br>Trianual<br>(μg/m3N) | % de la Norma Anual (D.S. No 114/2013<br>del Ministerio Secretaría General de la<br>República, 100 μg/m3N) |
| Los Andes | 2020 | 100 | 18,97 | 21,21 | 21 |
| Los Andes | 2021 | 93 | 20,06 | 20,06 | 20,06 |

<!-- Estadísticas: 3 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- Estudio EM2023/200-54 | Ecoazul 30 “Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” -->
<!-- FIN TABLA 9 -->


Tabla 10: Percentil 99 de los máximos diarios de concentración de 1 hora de NO 2 registrada en la

<!-- INICIO TABLA 10 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Estación|Año|% Datos<br>trimensuales<br>válidos|Promedio<br>Anual<br>(μg/m3N)|Promedio<br>Trianual<br>(μg/m3N)|% de la Norma Anual (D.S. No 114/2013<br>del Ministerio Secretaría General de la<br>República, 100 μg/m3N)| |---|---|---|---|---|---| ||2022|84|24,61||| -->

**Tabla 10: Percentil 99 de los máximos diarios de concentración de 1 hora de NO 2**

| Estación | Año | % Datos<br>máximos<br>horarias<br>válidos | Percentil 99<br>(μg/m3N) | Promedio<br>Trianual<br>(μg/m3N) | % de la Norma 24 horas (D.S. No<br>114/2013 del Ministerio Secretaría<br>General de la República, 400<br>μg/m3N) |
| --- | --- | --- | --- | --- | --- |
| Los Andes | 2020 | 99 | 78,34 | 88,05 | 22 |
| Los Andes | 2021 | 92 | 81,29 | 81,29 | 81,29 |
| Los Andes | 2022 | 83 | 104,51 | 104,51 | 104,51 |

<!-- Estadísticas: 3 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- Figura 10: Series de tiempo de NO 2 observado en la estación Los Andes durante el periodo 2020 - 2022. -->
<!-- FIN TABLA 10 -->

estación Los Andes. Periodo 2020 - 2022. ........................................................................ 31

Tabla 11: Características del dominio de modelación de la segunda grilla utilizada por el modelo
WRF en la zona de Estudio. ................................................................................................... 34

Tabla 12: Configuración de las principales parametrizaciones utilizadas en la modelación con WRF

<!-- INICIO TABLA 12 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Respecto a la configuración del modelo, en relación a la física y dinámica, se consideraron las parametrizaciones del trabajo por el documento Guía para el uso de modelos de calidad del aire en el SEIA, 2012, cuyos principales esquemas son mostrados en Tabla 12. -->

**Tabla 12: Configuración de las principales parametrizaciones utilizadas en la**

| Variable | Nombre | Esquema | Descripción |
| --- | --- | --- | --- |
| Microfísica | mp_physics | WSM5 | WSM (3 especies microfísicas) |
| Radiación de onda<br>larga | ra_lw_physics | RRTM | Modelo de transferencia<br>radiativa rápida que utiliza<br>tablas de eficiencia. Cuenta<br>con 35iffusion bandas |
| Radiación de onda<br>corta | ra_sw_physics | Dudhia scheme | Integración simple que permite<br>la absorción y dispersión por<br>nubes y a cielo despejado |
| Capa superficial | sf_sfclay_physics | MM5 | Monin-Obukhov similaridad |
| Superficie | sf_surface_physcis | Thermal Diffusion<br>Scheme | Esquema de 35iffusion termal |
| Capa límite<br>planetaria | bl_pbl_physics | YSU scheme | QNSE |

<!-- Estadísticas: 6 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- ## 3.3 Resultados del Modelo WRF en la Zona de Estudio En la presente sección se muestran los resultados del modelo meteorológico WRF. Estos provienen de las variables extraídas en las coordenadas de la estación meteorológica -->
<!-- FIN TABLA 12 -->

para la zona de Estudio. ........................................................................................................ 35

Tabla 13: Estadísticos Matemáticos de Literatura. ............................................................................. 57

<!-- INICIO TABLA 13 -->
<!-- Confianza de extracción: 0.90 -->
<!-- Contexto previo: -->
<!-- observados y modelados. Las fórmulas y rango de estos estadísticos se presentan en Tabla 13. -->

**Tabla 13: Estadísticos Matemáticos de Literatura.**

| Estadístico | Ecuación | Rango |
| --- | --- | --- |
| RMSE | √∑(Mi−Oi)2<br>n<br>n<br>i=1<br> | , ∞ |
| BIASN | ∑<br>Mi−Oi<br>n<br>i=1<br>∑<br>Oi<br>n<br>i=1<br> | (-∞,∞ |
| MAE | 1<br>n∑ | Mi−Oi |
| R | 1<br>(1 −n)∑(Mi−M)<br>̅<br>σM<br>N<br>i=1<br>(Oi−O)<br>̅<br>σo<br> | [-1,1] |

<!-- Estadísticas: 4 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia en base a Wilks, 2011. 3.4.1 Análisis Cualitativo Series de Tiempo Observados y Modelados con WRF, Año -->
<!-- FIN TABLA 13 -->


Tabla 14: Resultados estadísticos obtenidos de la comparación de datos observados y modelados

<!-- INICIO TABLA 14 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- - Temperatura: entre las variables estudiadas es la que tiene la mejor relación con las observaciones, la más cercana a 1. -->

**Tabla 14: Resultados estadísticos obtenidos de la comparación de datos observados y**

| Estadística | Variable | Unidad | Estación Los Andes |
| --- | --- | --- | --- |
| BiasN | VV | m/s | 0,26 |
| BiasN | HR | % | 0,39 |
| BiasN | T | °C | -0,12 |
| RMSE | VV | m/s | 0,93 |
| RMSE | HR | % | 23,76 |
| RMSE | T | °C | 3,73 |
| MAE | VV | m/s | 0,65 |
| MAE | HR | % | 20,27 |
| MAE | T | °C | 2,98 |
| R | VV | Adimensional | 0,53 |
| R | HR | Adimensional | 0,68 |
| R | T | Adimensional | 0,94 |

<!-- Estadísticas: 12 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- VV: velocidad de viento HR: humedad relativa T: temperatura del aire. Estudio EM2023/200-54 | Ecoazul -->
<!-- FIN TABLA 14 -->

con WRF en las estaciones de la zona de estudio. ............................................................. 67

Tabla 15: Características del dominio de modelación utilizada por el modelo CALPUFF en la zona
de Estudio (archivo CALPUFF_Ready). ................................................................................ 69

Tabla 16: Coordenadas de receptores de interés en la zona del Proyecto........................................ 72

<!-- INICIO TABLA 16 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Informe Final mayor con respecto a los resultados de grilla, donde los resultados son interpolados para entregar las concentraciones en todo el dominio de modelación. -->

**Tabla 16: Coordenadas de receptores de interés en la zona del Proyecto.**

| Receptor | Descripción | UTM (WGS 84 - Z18) | Col4 | Altitud (1)<br>(m.s.n.m.) | LCC (km) | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Receptor | Descripción | Este (m) | Norte (m) | Norte (m) | LCC-X | LCC-Y |
| R1 | Los Andes | 351.534 | 6.364.623 | 877 | 14,840 | -9,596 |
| R2 | Catemu | 316.512 | 6.371.481 | 432 | -20,066 | -2,160 |
| R3 | Iglesia Almendral | 341.420 | 6.375.196 | 682 | 4,901 | 1,144 |
| R4 | Iglesia Curimón | 341.799 | 6.371.393 | 704 | 5,217 | -2,665 |
| R5 | Catedral San Felipe | 338.454 | 6.375.087 | 649 | 1,933 | 1,084 |
| R6 | Colegio Rinconada | 342.147 | 6.365.180 | 727 | 5,463 | -8,884 |
| R7 | Colegio Curimón | 339.688 | 6.372.404 | 675 | 3,123 | -1,620 |
| R8 | Vecino N°1 | 341.348 | 6.368.314 | 710 | 4,715 | -5,737 |
| R9 | Zona vecinal N°2 - 1 | 341.174 | 6.367.929 | 709 | 4,535 | -6,119 |
| R10 | Zona vecinal N°2 - 2 | 341.170 | 6.368.002 | 708 | 4,532 | -6,046 |
| R11 | Zona vecinal N°2 - 3 | 341.127 | 6.368.029 | 708 | 4,490 | -6,018 |
| R12 | Zona vecinal N°2 - 4 | 341.128 | 6.368.092 | 708 | 4,492 | -5,955 |
| R13 | Zona vecinal N°3 - 1 | 341.352 | 6.367.916 | 711 | 4,713 | -6,135 |
| R14 | Zona vecinal N°3 - 2 | 341.455 | 6.367.931 | 712 | 4,816 | -6,121 |
| R15 | Zona vecinal N°3 - 3 | 341.576 | 6.367.939 | 714 | 4,937 | -6,115 |
| R16 | vecino N°4 | 341.344 | 6.368.548 | 709 | 4,715 | -5,503 |
| R17 | zona vecinal N°5 - 1 | 340.872 | 6.367.770 | 707 | 4,230 | -6,273 |
| R18 | zona vecinal N°5 - 2 | 340.854 | 6.367.891 | 707 | 4,214 | -6,152 |
| R19 | zona vecinal N°5 - 3 | 340.835 | 6.368.043 | 706 | 4,198 | -5,999 |
| R20 | zona vecinal N°5 - 4 | 340.541 | 6.368.010 | 703 | 3,903 | -6,027 |
| R21 | zona vecinal N°5 - 5 | 340.596 | 6.367.764 | 706 | 3,954 | -6,274 |
| R22 | zona vecinal N°5 - 6 | 340.762 | 6.367.698 | 707 | 4,119 | -6,343 |
| R23 | zona vecinal que participó del<br>PAC - 1 | 340.128 | 6.367.859 | 703 | 3,488 | -6,172 |
| R24 | zona vecinal que participó del<br>PAC - 2 | 339.927 | 6.367.952 | 710 | 3,289 | -6,075 |
| R25 | zona vecinal que participó del<br>PAC - 3 | 339.863 | 6.368.062 | 711 | 3,226 | -5,964 |
| R26 | zona vecinal que participó del<br>PAC - 4 | 339.749 | 6.367.738 | 719 | 3,107 | -6,286 |
| R27 | zona vecinal que participó del<br>PAC - 5 | 339.764 | 6.367.928 | 716 | 3,125 | -6,097 |
| R28 | Escuela Bucalemu | 342.219 | 6.368.707 | 720 | 5,593 | -5,358 |
| R29 | Iglesia de Jesucristo<br>Fundamento Apostólico | 342.634 | 6.368.518 | 725 | 6,005 | -5,554 |
| R30 | Otras Viviendas - 1 | 341.972 | 6.368.585 | 717 | 5,344 | -5,476 |
| R31 | Otras Viviendas - 2 | 341.974 | 6.368.678 | 717 | 5,347 | -5,383 |

<!-- Estadísticas: 32 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- Estudio EM2023/200-54 | Ecoazul 72 “Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” -->
<!-- FIN TABLA 16 -->


Tabla 17: Emisiones de MPS, MP10, MP2,5, NOx, SO 2 y CO de las fases de Construcción y Operación

<!-- INICIO TABLA 17 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- resuspensión y combustión de motores debido al transporte vehicular se implementaron a través de caminos, también considerando caminos No Pavimentados y Pavimentados. Finalmente, la fuente de calderas, corresponden a 2 calderas que se implementaron como fuentes puntuales. -->

**Tabla 17: Emisiones de MPS, MP10, MP2,5, NOx, SO 2 y CO de las fases de Construcción**

| Actividad | Col2 | Emisión (t/año) | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Actividad | Actividad | MPS | MP10 | MP2,5 | NOx | SO2 | CO |
| Construcción | Construcción | Construcción | Construcción | Construcción | Construcción | Construcción | Construcción |
| Movimientos<br>de tierra | Excavaciones | 0,0214201 | 0,0043818 | 0,0022491 |  |  |  |
| Movimientos<br>de tierra | Carguío de material | 0,0008567 | 0,0004052 | 0,0000614 |  |  |  |
| Resuspensión vías NO pavimentadas | Resuspensión vías NO pavimentadas | 0,0082114 | 0,0007083 | 0,0000708 |  |  |  |
| Resuspensión vías pavimentadas | Resuspensión vías pavimentadas | 0,0075561 | 0,0003395 | 0,0000821 |  |  |  |
| Emisiones de combustión vehicular | Emisiones de combustión vehicular | 0,0000078 | 0,0000078 | 0,0000078 | 0,0003774 | 0,0000004 | 0,0000874 |
| Total | Total | 0,0380521 | 0,0058426 | 0,0024712 | 0,0003774 | 0,0000004 | 0,0000874 |
| Operación | Operación | Operación | Operación | Operación | Operación | Operación | Operación |
| Resuspensión vías NO pavimentadas | Resuspensión vías NO pavimentadas | 0,0417133 | 0,0127694 | 0,0012769 |  |  |  |
| Resuspensión vías pavimentadas | Resuspensión vías pavimentadas | 0,1087893 | 0,0208822 | 0,0050521 |  |  |  |
| Emisiones de combustión vehicular | Emisiones de combustión vehicular | 0,0005841 | 0,0005841 | 0,0005841 | 0,0285087 | 0,0000312 | 0,0064443 |
| Generador | Generador | 0,1239973 | 0,1239973 | 0,1239973 | 1,7639880 | 0,1159977 | 0,3799928 |

<!-- Estadísticas: 13 filas, 8 columnas -->
<!-- Contexto posterior: -->
<!-- Estudio EM2023/200-54 | Ecoazul 76 “Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” -->
<!-- FIN TABLA 17 -->

del Proyecto Planta Depuradora de RILes Empresa San Lorenzo. .................................... 76

Tabla 18: Coordenadas de las áreas y tramos donde se implementaron las fuentes emisoras de

<!-- INICIO TABLA 18 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Las fuentes presentadas en Tabla 17 se implementaron en el modelo CALPUFF considerando las coordenadas que se muestran en Tabla 18 y Tabla 19, en coordenadas UTM y su correspondiente coordenada Lambert Conformal Conic (LCC), para las fases de Construcción y Operación, respectivamente. -->

**Tabla 18: Coordenadas de las áreas y tramos donde se implementaron las fuentes**

| Fuente | Superficie o<br>longitud | Punto | UTM (WGS 84 Z19) | Col5 | LCC (km) | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Fuente | Superficie o<br>longitud | Punto | Este (m) | Norte (m) | LCC-X | LCC-Y |
| Planta | 1.812 m2 | 1 | 341.207 | 6.368.229 | 4,573 | -5,820 |
| Planta | 1.812 m2 | 2 | 341.236 | 6.368.244 | 4,602 | -5,805 |
| Planta | 1.812 m2 | 3 | 341.265 | 6.368.203 | 4,631 | -5,846 |
| Planta | 1.812 m2 | 4 | 341.229 | 6.368.185 | 4,594 | -5,863 |
| Camino No<br>Pavimentado | 64,1 m | 1 | 341.305 | 6.368.173 | 4,670 | -5,877 |
| Camino No<br>Pavimentado | 64,1 m | 2 | 341.258 | 6.368.217 | 4,623 | -5,833 |
| Camino Pavimentado | 13.794 m | 1 | 341.308 | 6.368.174 | 4,673 | -5,876 |
| Camino Pavimentado | 13.794 m | 2 | 341.440 | 6.368.234 | 4,806 | -5,819 |
| Camino Pavimentado | 13.794 m | 2 | 339.290 | 6.372.613 | 2,728 | -1,404 |
| Camino Pavimentado | 13.794 m | 3 | 338.502 | 6.372.840 | 1,944 | -1,164 |

<!-- Estadísticas: 11 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- Estudio EM2023/200-54 | Ecoazul 77 “Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” -->
<!-- FIN TABLA 18 -->

contaminantes atmosféricos en el modelo CALPUFF para la fase de Construcción del
Proyecto. ................................................................................................................................ 77

iii

Tabla 19: Coordenadas de las áreas y tramos donde se implementaron las fuentes emisoras de

<!-- INICIO TABLA 19 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Fuente|Superficie o<br>longitud|27|338.965|6.378.874|2,507|4,862| |Fuente|Superficie o<br>longitud|28|338.937|6.379.056|2,482|5,045| |Fuente|Superficie o<br>longitud|29|341.308|6.368.174|4,673|-5,876| |Fuente|Superficie o<br>longitud|30|341.440|6.368.234|4,806|-5,819| -->

**Tabla 19: Coordenadas de las áreas y tramos donde se implementaron las fuentes**

| Fuente | Superficie o<br>longitud | Punto | UTM (WGS 84 Z19) | Col5 | LCC (km) | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Fuente | Superficie o<br>longitud | Punto | Este (m) | Norte (m) | LCC-X | LCC-Y |
| Planta | 1.812 m2 | 1 | 341.207 | 6.368.229 | 4,573 | -5,820 |
| Planta | 1.812 m2 | 2 | 341.236 | 6.368.244 | 4,602 | -5,805 |
| Planta | 1.812 m2 | 3 | 341.265 | 6.368.203 | 4,631 | -5,846 |
| Planta | 1.812 m2 | 4 | 341.229 | 6.368.185 | 4,594 | -5,863 |

<!-- Estadísticas: 5 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- Estudio EM2023/200-54 | Ecoazul 78 “Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” -->
<!-- FIN TABLA 19 -->

contaminantes atmosféricos en el modelo CALPUFF para la fase de Operación del
Proyecto. ................................................................................................................................ 78

Tabla 20: Resultados de MP10 promedio anual y percentil 98 de las concentraciones diarias

<!-- INICIO TABLA 20 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Construcción del Proyecto se presentan en Tabla 20. Como se observa en esta tabla, el mayor aporte del proyecto como promedio anual es en el receptor 8 con 0,01 μg/Nm [3], y como percentil 98 de las concentraciones 24 horas en el receptor 12 con 0,07 μg/Nm [3] . Esto alcanza a menos de 1% de la norma anual y diaria correspondiente. -->

**Tabla 20: Resultados de MP10 promedio anual y percentil 98 de las concentraciones**

| Receptor | Concentración de MP10 (μg/m3) | Col3 |
| --- | --- | --- |
| Receptor | Promedio anual | Percentil 98 de las conc. 24 horas |
| R1 | 0,00 | 0,00 |
| R2 | 0,00 | 0,00 |
| R3 | 0,00 | 0,00 |
| R4 | 0,00 | 0,00 |
| R5 | 0,00 | 0,00 |
| R6 | 0,00 | 0,00 |

<!-- Estadísticas: 7 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Estudio EM2023/200-54 | Ecoazul “Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 87 -->
<!-- FIN TABLA 20 -->

modeladas por el sistema CALPUFF, Escenario fase de Construcción. ........................... 87

Tabla 21: Resultados de MP2,5 promedio anual y percentil 98 de las concentraciones diarias

<!-- INICIO TABLA 21 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Construcción del Proyecto se presentan en Tabla 21. Como se observa en esta tabla, el mayor aporte del proyecto como promedio anual es en el receptor 8 con 0,005 μg/Nm [3], y como percentil 98 de las concentraciones 24 horas en el receptor 12 con 0,03 μg/Nm [3] . Esto alcanza a menos de 1% de la norma anual y diaria correspondiente. -->

**Tabla 21: Resultados de MP2,5 promedio anual y percentil 98 de las concentraciones**

| Receptor | Concentración de MP2,5 (μg/m3) | Col3 |
| --- | --- | --- |
| Receptor | Promedio anual | Percentil 98 de las conc. 24 horas |
| R1 | 0,00 | 0,00 |
| R2 | 0,00 | 0,00 |
| R3 | 0,00 | 0,00 |
| R4 | 0,00 | 0,00 |
| R5 | 0,00 | 0,00 |
| R6 | 0,00 | 0,00 |
| R7 | 0,00 | 0,00 |
| R8 | 0,00 | 0,02 |
| R9 | 0,00 | 0,02 |
| R10 | 0,00 | 0,02 |
| R11 | 0,00 | 0,03 |
| R12 | 0,00 | 0,03 |
| R13 | 0,00 | 0,02 |
| R14 | 0,00 | 0,01 |
| R15 | 0,00 | 0,01 |
| R16 | 0,00 | 0,01 |
| R17 | 0,00 | 0,01 |
| R18 | 0,00 | 0,01 |
| R19 | 0,00 | 0,01 |
| R20 | 0,00 | 0,00 |
| R21 | 0,00 | 0,00 |
| R22 | 0,00 | 0,00 |
| R23 | 0,00 | 0,00 |

<!-- Estadísticas: 24 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Estudio EM2023/200-54 | Ecoazul “Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 91 -->
<!-- FIN TABLA 21 -->

modeladas por el sistema CALPUFF, Escenario fase de Construcción. ........................... 91

Tabla 22: Resultados de MPS promedio anual modelados por el sistema CALPUFF, Escenario fase

<!-- INICIO TABLA 22 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- interés para la fase de Construcción del Proyecto se presentan en Tabla 22. Como se observa en esta tabla, el mayor aporte del proyecto es en el receptor 8 con 0,13 mg/m [2] día como promedio anual. Esto es inferior a 1% de la norma de referencia. -->

**Tabla 22: Resultados de MPS promedio anual modelados por el sistema CALPUFF,**

| Receptor | Concentración de MPS (mg/m2-día) |
| --- | --- |
| Receptor | Promedio anual |
| R1 | 0,00 |
| R2 | 0,00 |
| R3 | 0,00 |
| R4 | 0,00 |
| R5 | 0,00 |
| R6 | 0,00 |
| R7 | 0,00 |
| R8 | 0,13 |
| R9 | 0,04 |
| R10 | 0,05 |
| R11 | 0,04 |
| R12 | 0,05 |
| R13 | 0,06 |
| R14 | 0,02 |
| R15 | 0,01 |
| R16 | 0,02 |
| R17 | 0,01 |
| R18 | 0,01 |
| R19 | 0,01 |
| R20 | 0,00 |
| R21 | 0,00 |
| R22 | 0,00 |
| R23 | 0,00 |
| R24 | 0,00 |

<!-- Estadísticas: 25 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Estudio EM2023/200-54 | Ecoazul “Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 95 -->
<!-- FIN TABLA 22 -->

de Construcción. .................................................................................................................... 95

Tabla 23: Resultados de NO 2 promedio anual y percentil 99 de las máximas diarias concentraciones

<!-- INICIO TABLA 23 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- concentraciones horarias modelados con CALPUFF en los receptores de interés para la fase de Construcción del Proyecto se presentan en Tabla 23. Como se observa en esta tabla, los aportes de este contaminante como promedio anual y percentil 99 de las concentraciones horarias son muy bajas y no alcanza a 1% de la norma respectiva. -->

**Tabla 23: Resultados de NO 2 promedio anual y percentil 99 de las máximas diarias**

| Receptor | Concentración de NO (μg/m3)<br>2 | Col3 |
| --- | --- | --- |
| Receptor | Promedio anual | Percentil 99 de las conc. 1 hora |
| R1 | 0,00 | 0,00 |
| R2 | 0,00 | 0,00 |
| R3 | 0,00 | 0,00 |
| R4 | 0,00 | 0,00 |
| R5 | 0,00 | 0,00 |
| R6 | 0,00 | 0,00 |
| R7 | 0,00 | 0,00 |
| R8 | 0,00 | 0,00 |
| R9 | 0,00 | 0,00 |
| R10 | 0,00 | 0,00 |
| R11 | 0,00 | 0,00 |
| R12 | 0,00 | 0,00 |
| R13 | 0,00 | 0,00 |
| R14 | 0,00 | 0,00 |
| R15 | 0,00 | 0,00 |
| R16 | 0,00 | 0,00 |
| R17 | 0,00 | 0,00 |
| R18 | 0,00 | 0,00 |
| R19 | 0,00 | 0,00 |
| R20 | 0,00 | 0,00 |
| R21 | 0,00 | 0,00 |
| R22 | 0,00 | 0,00 |
| R23 | 0,00 | 0,00 |

<!-- Estadísticas: 24 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Estudio EM2023/200-54 | Ecoazul “Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 98 -->
<!-- FIN TABLA 23 -->

horarias modeladas por el sistema CALPUFF, Escenario fase de Construcción. ............ 98

Tabla 24: Resultados de SO 2 promedio anual, percentil 99 de las concentraciones diarias y percentil

<!-- INICIO TABLA 24 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Construcción del Proyecto se presentan en Tabla 24. Como se observa en esta tabla, los aportes de este contaminante como promedio anual, percentil 99 de las concentraciones 24 horas y percentil 98,5 de las concentraciones de 1 hora son muy bajas y no alcanza a 1% de la norma respectiva. -->

**Tabla 24: Resultados de SO 2 promedio anual, percentil 99 de las concentraciones**

| Receptor | Concentración de SO (μg/m3)<br>2 | Col3 | Col4 |
| --- | --- | --- | --- |
| Receptor | Promedio anual | Perc. 99 de las conc. 24 hr | Perc. 98,5 de las conc. 1 hr |
| R1 | 0,00 | 0,00 | 0,00 |
| R2 | 0,00 | 0,00 | 0,00 |
| R3 | 0,00 | 0,00 | 0,00 |
| R4 | 0,00 | 0,00 | 0,00 |
| R5 | 0,00 | 0,00 | 0,00 |
| R6 | 0,00 | 0,00 | 0,00 |
| R7 | 0,00 | 0,00 | 0,00 |
| R8 | 0,00 | 0,00 | 0,00 |
| R9 | 0,00 | 0,00 | 0,00 |
| R10 | 0,00 | 0,00 | 0,00 |
| R11 | 0,00 | 0,00 | 0,00 |
| R12 | 0,00 | 0,00 | 0,00 |
| R13 | 0,00 | 0,00 | 0,00 |
| R14 | 0,00 | 0,00 | 0,00 |
| R15 | 0,00 | 0,00 | 0,00 |
| R16 | 0,00 | 0,00 | 0,00 |
| R17 | 0,00 | 0,00 | 0,00 |
| R18 | 0,00 | 0,00 | 0,00 |
| R19 | 0,00 | 0,00 | 0,00 |
| R20 | 0,00 | 0,00 | 0,00 |
| R21 | 0,00 | 0,00 | 0,00 |

<!-- Estadísticas: 22 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Estudio EM2023/200-54 | Ecoazul “Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 102 -->
<!-- FIN TABLA 24 -->

98,5 máximas concentraciones horarias modeladas por el sistema CALPUFF, Escenario
fase de Construcción. ......................................................................................................... 102

Tabla 25: Resultados de CO percentil 99 de las máximas diarias concentraciones de 8 y 1 horas

<!-- INICIO TABLA 25 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- horas, en los receptores de interés modelados con CALPUFF para la fase de Construcción del Proyecto se presentan en Tabla 25. En esta tabla se observa que el aporte del proyecto de CO en todos los receptores es bajo y no alcanza a 1% de la norma respectiva. -->

**Tabla 25: Resultados de CO percentil 99 de las máximas diarias concentraciones de 8**

| Receptor | Concentración de CO (μg/m3) | Col3 |
| --- | --- | --- |
| Receptor | Percentil 99 de las conc. 8 horas | Percentil 99 de las conc. 1 hora |
| R1 | 0,00 | 0,00 |
| R2 | 0,00 | 0,00 |
| R3 | 0,00 | 0,00 |
| R4 | 0,00 | 0,00 |
| R5 | 0,00 | 0,00 |
| R6 | 0,00 | 0,00 |
| R7 | 0,00 | 0,00 |
| R8 | 0,00 | 0,00 |
| R9 | 0,00 | 0,00 |
| R10 | 0,00 | 0,00 |
| R11 | 0,00 | 0,00 |
| R12 | 0,00 | 0,00 |
| R13 | 0,00 | 0,00 |
| R14 | 0,00 | 0,00 |
| R15 | 0,00 | 0,00 |
| R16 | 0,00 | 0,00 |
| R17 | 0,00 | 0,00 |
| R18 | 0,00 | 0,00 |
| R19 | 0,00 | 0,00 |
| R20 | 0,00 | 0,00 |
| R21 | 0,00 | 0,00 |
| R22 | 0,00 | 0,00 |

<!-- Estadísticas: 23 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Estudio EM2023/200-54 | Ecoazul “Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 107 -->
<!-- FIN TABLA 25 -->

modeladas por el sistema CALPUFF, Escenario fase de Construcción. ......................... 107

Tabla 26: Resultados de MP10 promedio anual y percentil 98 de las concentraciones diarias

<!-- INICIO TABLA 26 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- del Proyecto se presentan en Tabla 26. Como se observa en esta tabla, el mayor aporte del proyecto como promedio anual es en el receptor 8 con 2,28 μg/Nm [3], y como percentil 98 de las concentraciones 24 horas en el receptor 12 con 5,08 μg/Nm [3] . Esto alcanza a 5 y 4% de la norma anual y diaria correspondiente, respectivamente. -->

**Tabla 26: Resultados de MP10 promedio anual y percentil 98 de las concentraciones**

| Receptor | Concentración de MP10 (μg/m3) | Col3 |
| --- | --- | --- |
| Receptor | Promedio anual | Percentil 98 de las conc. 24 horas |
| R1 | 0,00 | 0,01 |
| R2 | 0,00 | 0,00 |
| R3 | 0,01 | 0,05 |
| R4 | 0,03 | 0,08 |
| R5 | 0,02 | 0,06 |
| R6 | 0,02 | 0,07 |
| R7 | 0,03 | 0,09 |
| R8 | 2,28 | 4,71 |
| R9 | 1,51 | 3,46 |
| R10 | 1,65 | 3,96 |
| R11 | 1,67 | 3,95 |
| R12 | 1,90 | 5,08 |
| R13 | 1,81 | 3,86 |
| R14 | 1,38 | 3,30 |
| R15 | 1,23 | 3,17 |
| R16 | 1,17 | 2,68 |
| R17 | 0,57 | 1,53 |
| R18 | 0,68 | 1,85 |
| R19 | 0,70 | 1,69 |
| R20 | 0,24 | 0,65 |

<!-- Estadísticas: 21 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Estudio EM2023/200-54 | Ecoazul “Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 111 -->
<!-- FIN TABLA 26 -->

modeladas por el sistema CALPUFF, Escenario fase de Operación. ............................... 111

Tabla 27: Resultados de MP2,5 promedio anual y percentil 98 de las concentraciones diarias

<!-- INICIO TABLA 27 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- del Proyecto se presentan en Tabla 27. Como se observa en esta tabla, el mayor aporte del proyecto como promedio anual es en el receptor 8 con 2,24 μg/Nm [3], y como percentil 98 de las concentraciones 24 horas en el receptor 12 con 5,07 μg/Nm [3] . Esto alcanza a menos de 11 y 10% de la norma anual y diaria correspondiente, respectivamente. -->

**Tabla 27: Resultados de MP2,5 promedio anual y percentil 98 de las concentraciones**

| Receptor | Concentración de MP2,5 (μg/m3) | Col3 |
| --- | --- | --- |
| Receptor | Promedio anual | Percentil 98 de las conc. 24 horas |
| R1 | 0,00 | 0,01 |
| R2 | 0,00 | 0,00 |
| R3 | 0,01 | 0,04 |
| R4 | 0,03 | 0,07 |
| R5 | 0,02 | 0,05 |
| R6 | 0,02 | 0,06 |
| R7 | 0,03 | 0,08 |
| R8 | 2,24 | 4,69 |
| R9 | 1,48 | 3,41 |
| R10 | 1,62 | 3,86 |
| R11 | 1,64 | 3,82 |
| R12 | 1,86 | 5,07 |
| R13 | 1,73 | 3,74 |
| R14 | 1,36 | 3,29 |
| R15 | 1,22 | 3,17 |
| R16 | 1,15 | 2,68 |
| R17 | 0,56 | 1,46 |
| R18 | 0,67 | 1,81 |
| R19 | 0,68 | 1,68 |
| R20 | 0,23 | 0,65 |
| R21 | 0,27 | 0,79 |
| R22 | 0,39 | 1,05 |
| R23 | 0,08 | 0,19 |

<!-- Estadísticas: 24 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Estudio EM2023/200-54 | Ecoazul “Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 115 -->
<!-- FIN TABLA 27 -->

modeladas por el sistema CALPUFF, Escenario fase de Operación. ............................... 115

Tabla 28: Resultados de MPS promedio anual modelados por el sistema CALPUFF, Escenario fase

<!-- INICIO TABLA 28 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- interés para la fase de Operación del Proyecto se presentan en Tabla 28. Como se observa en esta tabla, el mayor aporte del proyecto es en el receptor 8 con 2,52 mg/m [2] día como promedio anual. Esto alcanza a 1% de la norma de referencia. -->

**Tabla 28: Resultados de MPS promedio anual modelados por el sistema CALPUFF,**

| Receptor | Concentración de MPS (mg/m2-día) |
| --- | --- |
| Receptor | Promedio anual |
| R1 | 0,00 |
| R2 | 0,00 |
| R3 | 0,01 |
| R4 | 0,02 |
| R5 | 0,02 |
| R6 | 0,02 |
| R7 | 0,03 |
| R8 | 2,52 |
| R9 | 1,34 |
| R10 | 1,44 |
| R11 | 1,40 |
| R12 | 1,63 |
| R13 | 2,14 |
| R14 | 1,11 |
| R15 | 0,83 |
| R16 | 0,91 |
| R17 | 0,37 |
| R18 | 0,45 |
| R19 | 0,44 |
| R20 | 0,12 |
| R21 | 0,14 |
| R22 | 0,23 |
| R23 | 0,03 |
| R24 | 0,03 |

<!-- Estadísticas: 25 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Estudio EM2023/200-54 | Ecoazul “Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 119 -->
<!-- FIN TABLA 28 -->

de Operación. ....................................................................................................................... 119

Tabla 29: Resultados de NO 2 promedio anual y percentil 99 de las máximas diarias concentraciones

<!-- INICIO TABLA 29 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- tabla, el mayor aporte de este contaminante es en el receptor 8 con 3,07 y 89,22 μg/Nm [3], como promedio anual y percentil 99 de las concentraciones horarias, respectivamente. Esto alcanza a menos de 11 y 10% de la norma anual y diaria correspondiente, respectivamente. -->

**Tabla 29: Resultados de NO 2 promedio anual y percentil 99 de las máximas diarias**

| Receptor | Concentración de NO (μg/m3)<br>2 | Col3 |
| --- | --- | --- |
| Receptor | Promedio anual | Percentil 99 de las conc. 1 hora |
| R1 | 0,00 | 0,03 |
| R2 | 0,00 | 0,00 |
| R3 | 0,00 | 0,08 |
| R4 | 0,02 | 0,26 |
| R5 | 0,00 | 0,13 |
| R6 | 0,02 | 0,32 |
| R7 | 0,01 | 0,26 |
| R8 | 3,07 | 89,22 |
| R9 | 1,95 | 46,34 |
| R10 | 2,19 | 51,94 |
| R11 | 2,22 | 62,93 |
| R12 | 2,53 | 68,56 |
| R13 | 2,06 | 58,00 |
| R14 | 1,83 | 41,74 |
| R15 | 1,68 | 42,02 |
| R16 | 1,57 | 23,21 |
| R17 | 0,72 | 23,62 |
| R18 | 0,86 | 22,40 |
| R19 | 0,89 | 23,65 |
| R20 | 0,28 | 14,91 |
| R21 | 0,34 | 10,20 |

<!-- Estadísticas: 22 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Estudio EM2023/200-54 | Ecoazul “Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 122 -->
<!-- FIN TABLA 29 -->

horarias modeladas por el sistema CALPUFF, Escenario fase de Operación. ................ 122

Tabla 30: Resultados de SO 2 promedio anual, percentil 99 de las concentraciones diarias y percentil

<!-- INICIO TABLA 30 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- este contaminante como promedio anual son mayores en el receptor 8 con 2,01 μg/Nm [3], y en el receptor 12 con 5,12 y 11,42 μg/Nm [3] como percentil 99 de las concentraciones 24 horas y percentil 98,5 de las concentraciones de 1 hora, respectivamente. Esto alcanza a 3% de la norma anual, diaria y horaria correspondiente. -->

**Tabla 30: Resultados de SO 2 promedio anual, percentil 99 de las concentraciones**

| Receptor | Concentración de SO (μg/m3)<br>2 | Col3 | Col4 |
| --- | --- | --- | --- |
| Receptor | Promedio anual | Perc. 99 de las conc. 24 hr | Perc. 98,5 de las conc. 1 hr |
| R1 | 0,00 | 0,00 | 0,01 |
| R2 | 0,00 | 0,00 | 0,00 |
| R3 | 0,00 | 0,01 | 0,01 |
| R4 | 0,01 | 0,03 | 0,08 |
| R5 | 0,00 | 0,01 | 0,02 |
| R6 | 0,01 | 0,05 | 0,14 |
| R7 | 0,01 | 0,02 | 0,05 |
| R8 | 2,01 | 4,82 | 10,26 |
| R9 | 1,28 | 3,22 | 7,45 |
| R10 | 1,44 | 3,73 | 7,34 |
| R11 | 1,46 | 3,84 | 8,71 |
| R12 | 1,66 | 5,12 | 11,42 |
| R13 | 1,34 | 3,56 | 8,69 |
| R14 | 1,20 | 3,40 | 9,50 |
| R15 | 1,10 | 3,33 | 10,12 |
| R16 | 1,03 | 2,72 | 7,10 |
| R17 | 0,47 | 1,49 | 4,06 |
| R18 | 0,57 | 1,70 | 4,59 |
| R19 | 0,58 | 1,58 | 4,25 |
| R20 | 0,18 | 0,60 | 1,70 |

<!-- Estadísticas: 21 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Estudio EM2023/200-54 | Ecoazul “Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 126 -->
<!-- FIN TABLA 30 -->

98,5 máximas concentraciones horarias modeladas por el sistema CALPUFF, Escenario
fase de Operación. ............................................................................................................... 126

Tabla 31: Resultados de CO percentil 99 de las máximas diarias concentraciones de 8 y 1 horas

<!-- INICIO TABLA 31 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- horas, en los receptores de interés modelados con CALPUFF para la fase de Operación del Proyecto se presentan en Tabla 25. En esta tabla se observa que el mayor aporte de CO del proyecto es en el receptor 8 con 45,72 y 193,20 μg/Nm [3] como concentración 8 y 1 hora, respectivamente. Esto no alcanza a 1% de la norma respectiva. -->

**Tabla 31: Resultados de CO percentil 99 de las máximas diarias concentraciones de 8**

| Receptor | Concentración de CO (μg/m3) | Col3 |
| --- | --- | --- |
| Receptor | Percentil 99 de las conc. 8 horas | Percentil 99 de las conc. 1 hora |
| R1 | 0,05 | 0,09 |
| R2 | 0,01 | 0,02 |
| R3 | 0,27 | 0,93 |
| R4 | 0,41 | 1,37 |
| R5 | 0,32 | 0,88 |
| R6 | 0,47 | 1,49 |
| R7 | 0,36 | 1,23 |
| R8 | 45,72 | 193,20 |
| R9 | 26,21 | 99,92 |
| R10 | 28,75 | 115,60 |
| R11 | 34,40 | 145,17 |
| R12 | 41,55 | 151,23 |
| R13 | 28,09 | 128,28 |
| R14 | 25,75 | 107,13 |
| R15 | 26,76 | 93,95 |
| R16 | 20,86 | 62,09 |
| R17 | 12,39 | 50,88 |
| R18 | 11,88 | 52,13 |
| R19 | 12,22 | 53,93 |
| R20 | 5,65 | 33,42 |
| R21 | 7,26 | 23,86 |
| R22 | 8,87 | 27,74 |
| R23 | 1,37 | 5,27 |

<!-- Estadísticas: 24 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Estudio EM2023/200-54 | Ecoazul “Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 131 -->
<!-- FIN TABLA 31 -->

modeladas por el sistema CALPUFF, Escenario fase de Operación. ............................... 131

Tabla 32: Estimación del impacto del Proyecto Planta Depuradora de RILes Empresa San Lorenzo

<!-- INICIO TABLA 32 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- indican en Tabla 32 a Tabla 34, respectivamente. Como se observa en estas tablas, las normas de calidad de aire primarias solo se superan en la estación Catemu, esto antes de incluir los aportes del Proyecto. Como se observa también, el aporte del proyecto estas estaciones monitoras es casi despreciable. -->

**Tabla 32: Estimación del impacto del Proyecto Planta Depuradora de RILes Empresa**

| Estación | Concentración<br>basal Actual<br>(μg/m3N) | Aporte Total del<br>proyecto<br>(μg/m3N) | Total | Normativa<br>vigente | Porcentaje de la<br>norma |
| --- | --- | --- | --- | --- | --- |
| Concentración Anual de MP10 | Concentración Anual de MP10 | Concentración Anual de MP10 | Concentración Anual de MP10 | Concentración Anual de MP10 | Concentración Anual de MP10 |
| Catemu | 108,42 | 0,001 | 108,42 | 50 | 217 |
| Concentración 24 horas de MP10 | Concentración 24 horas de MP10 | Concentración 24 horas de MP10 | Concentración 24 horas de MP10 | Concentración 24 horas de MP10 | Concentración 24 horas de MP10 |
| Catemu | 177,9 | 0,003 | 177,90 | 130 | 137 |

<!-- Estadísticas: 4 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- Tabla 33: Estimación del impacto del Proyecto Planta Depuradora de RILes Empresa San Lorenzo a las concentraciones de SO 2 observadas en la estación Catemu. -->
<!-- FIN TABLA 32 -->

a las concentraciones de MP10 observadas en la estación Catemu. ............................. 142

Tabla 33: Estimación del impacto del Proyecto Planta Depuradora de RILes Empresa San Lorenzo

<!-- INICIO TABLA 33 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Concentración Anual de MP10|Concentración Anual de MP10|Concentración Anual de MP10|Concentración Anual de MP10|Concentración Anual de MP10|Concentración Anual de MP10| |Catemu|108,42|0,001|108,42|50|217| |Concentración 24 horas de MP10|Concentración 24 horas de MP10|Concentración 24 horas de MP10|Concentración 24 horas de MP10|Concentración 24 horas de MP10|Concentración 24 horas de MP10| |Catemu|177,9|0,003|177,90|130|137| -->

**Tabla 33: Estimación del impacto del Proyecto Planta Depuradora de RILes Empresa**

| Estación | Concentración<br>basal Actual<br>(μg/m3N) | Aporte Total del<br>proyecto<br>(μg/m3N) | Total | Normativa<br>vigente | Porcentaje de la<br>norma |
| --- | --- | --- | --- | --- | --- |
| Concentración Anual de SO2 | Concentración Anual de SO2 | Concentración Anual de SO2 | Concentración Anual de SO2 | Concentración Anual de SO2 | Concentración Anual de SO2 |
| Catemu | 11,91 | 0,000 | 11,91 | 60 | 20 |
| Concentración 24 horas de SO2 | Concentración 24 horas de SO2 | Concentración 24 horas de SO2 | Concentración 24 horas de SO2 | Concentración 24 horas de SO2 | Concentración 24 horas de SO2 |
| Catemu | 32,78 | 0,000 | 32,78 | 150 | 22 |
| Concentración horaria de SO2 | Concentración horaria de SO2 | Concentración horaria de SO2 | Concentración horaria de SO2 | Concentración horaria de SO2 | Concentración horaria de SO2 |
| Catemu | 55,33 | 0,001 | 55,33 | 350 | 16 |

<!-- Estadísticas: 6 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- Estudio EM2023/200-54 | Ecoazul “Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 142 -->
<!-- FIN TABLA 33 -->

a las concentraciones de SO 2 observadas en la estación Catemu. ................................ 142

iv

Tabla 34: Estimación del impacto del Proyecto Planta Depuradora de RILes Empresa San Lorenzo

<!-- INICIO TABLA 34 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- “Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 142 Informe Final -->

**Tabla 34: Estimación del impacto del Proyecto Planta Depuradora de RILes Empresa**

| Estación | Concentración<br>basal Actual<br>(μg/m3N) | Aporte Total del<br>proyecto<br>(μg/m3N) | Total | Normativa<br>vigente | Porcentaje de la<br>norma |
| --- | --- | --- | --- | --- | --- |
| Concentración Anual de NO2 | Concentración Anual de NO2 | Concentración Anual de NO2 | Concentración Anual de NO2 | Concentración Anual de NO2 | Concentración Anual de NO2 |
| Los Andes | 21,21 | 0,002 | 21,21 | 100 | 21 |
| Concentración horaria de NO2 | Concentración horaria de NO2 | Concentración horaria de NO2 | Concentración horaria de NO2 | Concentración horaria de NO2 | Concentración horaria de NO2 |
| Los Andes | 88,05 | 0,033 | 88,08 | 400 | 22 |

<!-- Estadísticas: 4 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- Estudio EM2023/200-54 | Ecoazul “Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 143 -->
<!-- FIN TABLA 34 -->

a las concentraciones de NO 2 observadas en observadas en la estación Los Andes. .. 143

v

Figura 1: Topografía observada del dominio de la zona de Estudio. ................................................ 14

Figura 2: Ubicación de la estación meteorológica Los Andes con respecto a la ubicación del
Proyecto. ................................................................................................................................ 16

Figura 3: Series de tiempo de variables meteorológicas observadas en la estación Los Andes
durante el año 2022. .............................................................................................................. 17

Figura 4: Ciclos diarios de variables meteorológicas observadas en la estación Los Andes durante
el año 2022. ............................................................................................................................ 19

Figura 5: Ciclos estacionales de variables meteorológicas observadas en la estación Los Andes
durante el año 2022. .............................................................................................................. 21

Figura 6: Rosas de viento obtenidas con datos de la estación Los Andes durante el año 2022. ... 23

Figura 7: Ubicación de las estaciones de calidad de aire de la zona de Estudio. ............................ 25

Figura 8: Serie de tiempo de MP10 observado en la estación Catemu durante el periodo 20202022. ....................................................................................................................................... 28

Figura 9: Serie de tiempo de SO 2 observado en la estación Catemu durante el periodo 2020 - 2022.

................................................................................................................................................ 30

Figura 10: Series de tiempo de NO 2 observado en la estación Los Andes durante el periodo 20202022. ....................................................................................................................................... 31

Figura 11: Diagrama de operación del modelo meteorológico WRF. .................................................. 33

Figura 12: Dominios de modelación de WRF en la zona de Estudio. .................................................. 34

Figura 13: Series de tiempo de variables meteorológicas modeladas con WRF en la estación Los

Andes durante el año 2022. .................................................................................................. 37

Figura 14: Ciclos diarios de variables meteorológicas modeladas con WRF en la estación Los Andes

durante el año 2022. .............................................................................................................. 39

Figura 15: Ciclos estacionales de variables meteorológicas modelados con WRF la estación Los
Andes durante el año 2022. .................................................................................................. 41

Figura 16: Rosas de viento modeladas con WRF en la estación Los Andes durante el año 2022. ... 43

Figura 17. Campos de vientos promedio de verano del año 2022, periodo nocturno de 22:00 a 05:00
horas. ...................................................................................................................................... 45

Figura 18. Campos de vientos promedio de verano del año 2022, periodo matutino de 06:00 a 13:00
horas. ...................................................................................................................................... 46

Figura 19. Campos de vientos promedio de verano del año 2022, periodo vespertino de 14:00 a 21:00
horas. ...................................................................................................................................... 47

vi

Figura 20. Campos de vientos promedio de otoño del año 2022, periodo nocturno de 22:00 a 05:00
horas. ...................................................................................................................................... 48

Figura 21. Campos de vientos promedio de otoño del año 2022, periodo matutino de 06:00 a 13:00
horas. ...................................................................................................................................... 49

Figura 22. Campos de vientos promedio de otoño del año 2022, periodo vespertino de 14:00 a 21:00
horas. ...................................................................................................................................... 50

Figura 23. Campos de vientos promedio de invierno del año 2022, periodo nocturno de 22:00 a 05:00
horas. ...................................................................................................................................... 51

Figura 24. Campos de vientos promedio de invierno del año 2022, periodo matutino de 06:00 a 13:00
horas. ...................................................................................................................................... 52

Figura 25. Campos de vientos promedio de invierno del año 2022, periodo vespertino de 14:00 a
21:00 horas. ........................................................................................................................... 53

Figura 26. Campos de vientos promedio de primavera del año 2022, periodo nocturno de 22:00 a
05:00 horas. ........................................................................................................................... 54

Figura 27. Campos de vientos promedio de primavera del año 2022, periodo matutino de 06:00 a
13:00 horas. ........................................................................................................................... 55

Figura 28. Campos de vientos promedio de primavera del año 2022, periodo vespertino de 14:00 a
21:00 horas. ........................................................................................................................... 56

Figura 29: Comparación variables meteorológicas observadas y modeladas con WRF en la estación
Los Andes durante el año 2022. ........................................................................................... 59

Figura 30: Comparación de ciclos diarios de variables meteorológicas observados y modelados con
WRF en estación Los Andes durante el año 2022. .............................................................. 61

Figura 31: Comparación de ciclos estacionales de variables meteorológicas observados y
modelados con WRF en estación Los Andes durante el año 2022. .................................. 63

Figura 32: Comparación de rosas de viento observadas y modeladas con WRF en estación Los
Andes durante el año 2022. .................................................................................................. 65

Figura 33: Diagrama de operación del sistema de modelación WRF/CALPUFF/CalDesk. ................ 69

Figura 34: Dominio de modelación de CALPUFF, 56 x 50 km [2], en coordenadas LCC. ....................... 70

Figura 35: Dominio de modelación de CALPUFF, 50 x 41 km [2], en coordenadas LCC. ....................... 71

Figura 36: Ubicación de Receptores de interés alrededor del Proyecto. ............................................ 74

Figura 37: Ubicación de Receptores de interés alrededor del Proyecto - acercamiento al área del
Proyecto. ................................................................................................................................ 75

vii

Figura 38: Fuentes emisoras de la fase de Construcción del proyecto Planta Depuradora de RILes
Empresa San Lorenzo. Fuentes en Google Earth. ............................................................... 83

Figura 39: Distribución de fuentes emisoras de la fase de Construcción del proyecto Planta
Depuradora de RILes Empresa San Lorenzo. Fuentes implementadas en CALPUFF, en
coordenadas LCC. ................................................................................................................. 84

Figura 40: Fuentes emisoras de la fase de Operación del proyecto Planta Depuradora de RILes
Empresa San Lorenzo. Fuentes en Google Earth. ............................................................... 85

Figura 41: Distribución de fuentes emisoras de la fase de Operación del proyecto Planta Depuradora
de RILes Empresa San Lorenzo. Fuentes implementadas en CALPUFF, en coordenadas

LCC.......................................................................................................................................... 86

Figura 42: Isolíneas de concentraciones promedio anual de MP10 en la zona de estudio. Escenario
meteorología año 2022 y escenario de emisiones fase de Construcción. ....................... 89

Figura 43: Isolíneas de percentiles 98 de concentraciones de 24 horas de MP10 primario en la zona
de estudio. Escenario meteorología año 2022 y escenario de emisiones fase de
Construcción. ......................................................................................................................... 90

Figura 44: Isolíneas de concentraciones promedio anual de MP2,5 en la zona de estudio. Escenario
meteorología año 2022 y escenario de emisiones fase de Construcción. ....................... 93

Figura 45: Isolíneas de percentiles 98 de concentraciones de 24 horas de MP2,5 primario en la zona
de estudio. Escenario meteorología año 2022 y escenario de emisiones fase de
Construcción. ......................................................................................................................... 94

Figura 46: Isolíneas de concentraciones promedio anual de MPS en la zona de estudio. Escenario
meteorología año 2022 y escenario de emisiones etapa de Construcción. ..................... 97

Figura 47: Isolíneas de concentraciones promedio anual de NO 2 en la zona de estudio. Escenario
meteorología año 2022 y escenario de emisiones fase de Construcción. ..................... 100

Figura 48: Isolíneas de percentiles 99 de concentraciones de 1 hora de NO 2 en la zona de estudio.
Escenario meteorología año 2022 y escenario de emisiones fase de Construcción. .... 101

Figura 49: Isolíneas de concentraciones promedio anual de SO 2 en la zona de estudio. Escenario
meteorología año 2022 y escenario de emisiones fase de Construcción. ..................... 104

Figura 50: Isolíneas de Percentil 99 de las concentraciones de 24 horas de SO 2 en la zona de estudio.
Escenario meteorología año 2022 y escenario de emisiones fase de Construcción. .... 105

Figura 51: Isolíneas de Percentil 98,5 de las concentraciones de 1 hora de SO 2 en la zona de estudio.
Escenario meteorología año 2022 y escenario de emisiones fase de Construcción. .... 106

viii

Figura 52: Isolíneas de Percentil 99 de los máximos diarios de las concentraciones de 8 horas de
CO en la zona de estudio. Escenario meteorología año 2022 y escenario de emisiones
fase de Construcción. ......................................................................................................... 109

Figura 53: Isolíneas de Percentil 99 de los máximos diarios de las concentraciones de 1 hora de CO
en la zona de estudio. Escenario meteorología año 2022 y escenario de emisiones fase
de Construcción. .................................................................................................................. 110

Figura 54: Isolíneas de concentraciones promedio anual de MP10 en la zona de estudio. Escenario
meteorología año 2022 y escenario de emisiones fase de Operación. ........................... 113

Figura 55: Isolíneas de percentiles 98 de concentraciones de 24 horas de MP10 primario en la zona
de estudio. Escenario meteorología año 2022 y escenario de emisiones fase de
Operación. ............................................................................................................................ 114

Figura 56: Isolíneas de concentraciones promedio anual de MP2,5 en la zona de estudio. Escenario
meteorología año 2022 y escenario de emisiones fase de Operación. ........................... 117

Figura 57: Isolíneas de percentiles 98 de concentraciones de 24 horas de MP2,5 primario en la zona
de estudio. Escenario meteorología año 2022 y escenario de emisiones fase de
Operación. ............................................................................................................................ 118

Figura 58: Isolíneas de concentraciones promedio anual de MPS en la zona de estudio. Escenario
meteorología año 2022 y escenario de emisiones etapa de Operación. ........................ 121

Figura 59: Isolíneas de concentraciones promedio anual de NO 2 en la zona de estudio. Escenario
meteorología año 2022 y escenario de emisiones fase de Operación. ........................... 124

Figura 60: Isolíneas de percentiles 99 de concentraciones de 1 hora de NO 2 en la zona de estudio.
Escenario meteorología año 2022 y escenario de emisiones fase de Operación. ......... 125

Figura 61: Isolíneas de concentraciones promedio anual de SO 2 en la zona de estudio. Escenario
meteorología año 2022 y escenario de emisiones fase de Operación. ........................... 128

Figura 62: Isolíneas de Percentil 99 de las concentraciones de 24 horas de SO 2 en la zona de estudio.
Escenario meteorología año 2022 y escenario de emisiones fase de Operación. ......... 129

Figura 63: Isolíneas de Percentil 98,5 de las concentraciones de 1 hora de SO 2 en la zona de estudio.
Escenario meteorología año 2022 y escenario de emisiones fase de Operación. ......... 130

Figura 64: Isolíneas de Percentil 99 de los máximos diarios de las concentraciones de 8 horas de
CO en la zona de estudio. Escenario meteorología año 2022 y escenario de emisiones
fase de Operación. ............................................................................................................... 133

Figura 65: Isolíneas de Percentil 99 de los máximos diarios de las concentraciones de 1 hora de CO
en la zona de estudio. Escenario meteorología año 2022 y escenario de emisiones fase
de Operación. ....................................................................................................................... 134

ix

Figura 66: Área de Influencia para Calidad de Aire por MP10. .......................................................... 136

Figura 67: Área de Influencia para Calidad de Aire por MP2,5. .......................................................... 137

Figura 68: Área de Influencia para Calidad de Aire por NO 2 . .............................................................. 138

Figura 69: Área de Influencia para Calidad de Aire por SO 2 . .............................................................. 139

Figura 70: Área de Influencia para Calidad de Aire por CO. ............................................................... 140

Figura 71: Área de Influencia para Calidad de Aire por MPS. ............................................................ 141

x

# CAPÍTULO 1: INTRODUCCIÓN

En este documento EnviroModeling Spa. Presenta a Ecoazul el Informe Final
correspondiente al estudio: “Estudio de Calidad de Aire del Proyecto Planta Depuradora
de RILes Empresa San Lorenzo”.

El objetivo de este estudio consiste en modelar la dispersión de contaminantes
atmosféricos del proyecto “Planta depuradora de RILes Empresa San Lorenzo” ubicado
en la Región del Valparaíso.

El proyecto consiste en la modificación del antiguo sistema de tratamiento de RILes de
las operaciones de la planta procesadora de pasas de Empresa San Lorenzo S.A. El
sistema de depuración diseñado es del tipo “lodos Activados”, el cuál tratará todos los
RILes estrictamente asociados al proceso productivo. Las instalaciones
agroindustriales de procesamiento de pasas se ubican en carretera San Martin s/n, en
específico en la Parcela N°10 de la parcelación Santa Verónica, sector de Bucalemu,
comuna de San Felipe, Región de Valparaíso.

Para el logro del objetivo de este estudio, en primer lugar, se procedió a la elaboración
de la línea base meteorológica para el año 2022 mediante la descarga de datos de la
estación Los Andes, pertenecientes a la Red del Sistema de información Nacional de
Calidad del Aire (SINCA).

Posteriormente se realizó la modelación meteorológica con Weather Research and
Forecast Model (WRF) en modo diagnóstico para obtener la meteorología de la zona del
Proyecto del año 2022, la cual fue utilizada como datos de entrada para la ejecución del
modelo de dispersión CALPUFF.

En segundo lugar, se realizó la modelación de contaminantes atmosféricos que
consideran las emisiones presentadas en Anexo de Estimación de Emisiones
Atmosféricas, para obtener el impacto de estas en la calidad del aire del área
circundante al Proyecto. Esto se llevó a cabo con el uso del sistema de modelación
WRF/CALPUFF, recomendado por el SEA y EPA (USA) para emisiones en terreno
complejo. Este sistema se aplicó considerando los siguientes escenarios
meteorológico, topográfico y de emisiones:

Estudio EM2023/200-54 | Ecoazul

11
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

Escenario Meteorológico: Corresponde al año 2022.

- Escenario Topográfico: La zona de estudio considera un área de 56 x 50 km [2],
cubriendo la zona del Proyecto, incluyendo las ciudades de San Felipe y Los Andes.

Escenarios de Emisiones: Considera las emisiones de las fases de construcción y
operación del Proyecto.

En el siguiente Capítulo de este documento se presenta la descripción de la información
meteorológica del proyecto en la zona de estudio. En el Capítulo 3 se presenta la
implementación, aplicación y resultados del modelo meteorológico WRF, además de la
comparación de los resultados de WRF con los datos observados en las estaciones de
la zona de interés. En Capítulo 4 se presenta la implementación, aplicación y resultados
del modelo de dispersión CALPUFF. Finalmente, las conclusiones del estudio se
presentan en el Capítulo 5.

Estudio EM2023/200-54 | Ecoazul

12
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

# CAPÍTULO 2: ANÁLISIS DE LA INFORMACIÓN METEOROLÓGICA DE LA ZONA DEL PROYECTO

## 2.1 Introducción

A continuación, se presenta una descripción de la zona de estudio donde se emplazará
el proyecto “Planta Depuradora de RILes Empresa San Lorenzo”, considerando aspectos
tales como: clima, características topográficas y meteorología. Este proyecto se ubicará
entre las ciudades de San Felipe y Los Andes, comuna de San Felipe, Provincia de
Valparaíso, Región de Valparaíso.

## 2.2 Descripción Topográfica y Climática de la Zona de Estudio

La zona de estudio se encuentra bajo la unidad geomorfológica correspondiente a
cuencas transicionales semiáridas, la que se caracteriza por poseer una orientación
norte-sur entre los dos sistemas orográficos más importantes: la cordillera de los Andes
y la cordillera de la Costa. Geológicamente corresponde a bloques hundidos y
basculados a diferentes profundidades con el frente monoclinal mirando hacia el graben
(Rojas, 2006).

La disposición en cuencas obedece a los frecuentes derrames de altura provenientes
del este, encadenando los sistemas andino y costero, creando umbrales orográficos de
eje este-oeste que encierran depresiones bien constituidas (Rojas, 2006).

La zona comprendida entre Los Andes y San Felipe se podría caracterizar como una
pequeña depresión central, con un valle de dimensiones similares tanto en dirección
norte-sur como este-oeste (15 x 15km2 aproximadamente). Al oeste de esta zona, la
morfología del valle cambia radicalmente, tomando características más similares a los
valles transversales de más al norte (Dirección General de Aguas, DGA, 2015).

La presencia de estas grandes estructuras es responsable de las variaciones en el curso
del río Aconcagua y de esta manera, en la dirección y disposición del propio valle. Estas
estructuras mayores tienen dos direcciones generales preferenciales: noroeste y
noreste, estas se presentan en todo el valle y determinan la morfología actual de toda la
cuenca. La litología sobre la cual se dispone esta cuenca es también un factor de
modelamiento, debido a que está sobre rocas intrusivas, que, al ser de mayor dureza, la

Estudio EM2023/200-54 | Ecoazul

13
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

erosión es menor y, por lo tanto, la profundidad y el ancho del valle es de menor orden
que sobre rocas sedimentarias. Por esto, la profundidad y el ancho de los valles sobre
intrusivos pueden crecer si estas rocas son afectadas por fallas (Comisión Nacional de
Riego, CNR, 2016).

El amplio fondo del valle está ocupado por una superficie inclinada muy llana, sin que
se reconozcan, en los costados, superficies secundarias correspondientes a antiguos
pisos del valle. Al pie de las montañas adyacentes, la superficie principal se confunde
con las acumulaciones coluviales que han descendido a lo largo de las pendientes hasta
el fondo de las rinconadas, cuando el río se aproxima a uno de los costados, arrastra los
materiales depositados (CNR, 2016).

En la Figura 1 se muestra la topografía de la zona de Estudio.

Figura 1: Topografía observada del dominio de la zona de Estudio.

La zona de estudio posee un clima de tipo mediterráneo cálido, el cual se desarrolla en
el valle del Aconcagua. Se caracteriza por ser un clima más seco y con una variación
térmica mayor que en la costa de la región.

Por ubicarse en el valle del río Aconcagua, tiene un clima mediterráneo con estación
seca prolongada, donde su característica principal es un invierno bien marcado con
temperaturas extremas que pueden llegar a 0 °C y en verano superar los 35 °C

Estudio EM2023/200-54 | Ecoazul

14
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

## 2.3 Línea Base Meteorológica de la Zona de Estudio Durante el Año 2022

La información meteorológica utilizada del área de interés corresponde a la registrada
por la estación meteorológica más cercana al proyecto. Esta información es la extraída
desde el sitio web SINCA para la estación Los Andes del año 2022. Esta estación se
encuentra localizada en la comuna de Los Andes, aproximadamente a 10 km del
proyecto, como se puede ver en Figura 2.

La Figura 3 muestra las series de tiempo de las variables meteorológicas registradas en
la estación Los Andes, observándose integridad en los datos de casi del 100%.

Descrito lo anterior, en Tabla 1 se muestra el porcentaje de datos válidos en estación
Los Andes para las variables velocidad y dirección de viento, humedad relativa y
temperatura, donde todas superan el 75% como mínimo de datos de calidad asegurada.

Respecto al tratamiento de los datos, estos fueron revisados y validados siguiendo los
lineamientos de la EPA, en relación a registros incoherentes, datos sin variación o saltos
bruscos entre horas de cada variable y revisión de variabilidad diaria y estacionalidad.

Tabla 1: Estaciones meteorológicas en el dominio de la zona de Estudio.

|Estación|Abreviatura|Latitud|Longitud|Variables Medidas (%)|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|Estación|Abreviatura|Latitud|Longitud|VV|DV|HR|T|
|Los Andes|LA|-32.846426|-70.586475|99,8|99,8|99,9|99,9|

VV: velocidad de viento; DV: dirección de viento; HR: Humedad Relativa; T: temperatura, S.D: Sin Datos

Estudio EM2023/200-54 | Ecoazul

15
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

Figura 2: Ubicación de la estación meteorológica Los Andes con respecto a la

ubicación del Proyecto.

2.3.1 Series de Tiempo de Variables Meteorológicas Observadas en el Año 2022

La Figura 3 muestra las series de tiempo de las variables meteorológicas de la estación
Los Andes. En esta figura se puede visualizar la integridad de los datos en todo el año,
en todas las variables meteorológicas.

Estudio EM2023/200-54 | Ecoazul

16
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

Figura 3: Series de tiempo de variables meteorológicas observadas en la estación Los

Andes durante el año 2022.

Estudio EM2023/200-54 | Ecoazul

17
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

2.3.2 Ciclos Diarios de Variables Meteorológicas Observadas Durante el Año 2022

Los ciclos diarios son construidos en base a los registros promedios de cada hora de
todo el año, con el fin de mostrar un comportamiento patrón de una cierta variable, en
este caso meteorológica. El área sombreada corresponde al área delimitada por los
percentiles 5 y 95, el cual tiene como objetivo caracterizar la variabilidad de la velocidad
del viento, humedad relativa y temperatura.

Un poco distinto es lo que se visualiza en el ciclo de dirección de viento, el cual muestra
la frecuencia en términos de porcentaje, de las direcciones de viento registradas, cada
22,5° a lo largo de todas las horas, desde 0:00 hasta 23:00, de todo el año.

En la Figura 4 se muestran los ciclos diarios de las observaciones meteorológicas en la
estación Los Andes para el año 2022.

La velocidad de viento se visualiza con un aumento de la magnitud durante el día en la
estación Los Andes.

Respecto a la dirección de viento, se visualiza viento noreste en el periodo nocturno y al
final del día. Mientras que en la tarde se visualiza viento oeste.

La temperatura muestra un ciclo diario con un aumento durante el día que alcanza los
25 °C como promedio.

Respecto a la humedad relativa, se observa un ciclo con máximos durante la noche, con
magnitudes sobre el 60%, en cuanto a las mínimas se presentan en la tarde.

Estudio EM2023/200-54 | Ecoazul

18
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

Figura 4: Ciclos diarios de variables meteorológicas observadas en la estación Los

Andes durante el año 2022.

Estudio EM2023/200-54 | Ecoazul

19
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

2.3.3 Ciclos Estacionales de Variables Meteorológicas Observados Durante el Año

2022

Los ciclos estacionales corresponden a gráficos donde se muestra el ciclo diario en el
eje x y el ciclo anual en el eje y. La escala de color muestra la magnitud de la variable,
donde el color rojo muestra valores máximos y los colores azules los mínimos. En
particular, en el ciclo estacional de velocidad de viento se superponen vectores de viento
en la imagen, con la finalidad de mostrar la dirección de viento predominante promedio
a lo largo del día y del año.

La Figura 5 muestra los ciclos estacionales de los registros observados de la velocidad
y dirección de viento, humedad relativa y temperatura en la estación Los Andes.

Respecto a la velocidad de viento se observa un aumento de la magnitud durante el día
y en los meses de primavera y verano.

Respecto a la dirección de viento, se visualizan vientos noreste en el periodo nocturno,
mientras que en el día cambian a noroeste en invierno y suroeste en verano.

El ciclo de la temperatura muestra un aumento de la magnitud en horas del día y en los
meses de verano y disminuyendo en el periodo nocturno y en los meses de invierno.

Con respecto a la humedad relativa, aumenta su magnitud en el periodo nocturno,
observándose la menor humedad durante los meses de otoño y primavera.

Estudio EM2023/200-54 | Ecoazul

20
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

Figura 5: Ciclos estacionales de variables meteorológicas observadas en la estación

Los Andes durante el año 2022.

Estudio EM2023/200-54 | Ecoazul

21
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

2.3.4 Rosas de Viento Observadas Durante el Año 2022

La variabilidad de la velocidad y dirección del viento es caracterizada mediante las rosas
de viento solicitadas por el documento oficial, “Guía para el uso de Modelos de Calidad
del Aire en el SEIA”.

En Figura 6 se presentan las rosas de viento para cuatro rangos de tiempo horarios para
la estación Los Andes, los cuales son descritos a continuación:

 Periodo noche o madrugada, 01:00 a 06:00 horas: el viento dominante es noreste

con magnitudes que llegan a 1 m/s.

 Periodo mañana, 07:00 a 14:00 horas: los vientos dominantes corresponden a

noreste y noroeste con magnitudes de hasta 2 m/s.

 Periodo tarde, 15:00 a 23:00 horas: los vientos dominantes son noreste y en

menor medida Suroeste, con magnitudes de hasta 4 m/s.

 Periodo completo, 00:00 a 23:00 horas: se visualizan las componentes noreste y

suroeste, donde la más significativa corresponde a la primera con casi un 20% de
frecuencia y magnitudes de 3 m/s.

Estudio EM2023/200-54 | Ecoazul

22
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

Figura 6: Rosas de viento obtenidas con datos de la estación Los Andes durante el año

2022.

Estudio EM2023/200-54 | Ecoazul

23
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

## 2.4 Línea Base de Calidad de Aire de la Zona de Estudio

En esta sección se presenta la línea base de calidad de aire disponible de la zona de
estudio en San Felipe y Los Andes, de acuerdo a la información ambiental registrada por
las estaciones de calidad de aire ubicadas en esta zona.

Por una parte, la información de NO 2 se obtuvo de información disponible en el portal
del Sistema de Información Nacional de Calidad de Aire (SINCA) para la estación Los
Andes, ubicada aproximadamente a 10 km del Proyecto. La información de SO 2 también
se obtuvo de la misma fuente para la estación Catemu, la cual se toma como referencia
para SO 2 ya que no son datos validados los disponibles. Esta estación se ubica
aproximadamente a 24 km del proyecto.

Por otra parte, la información de MP10 se obtuvo para la estación Catemu desde el
portal SNIFA (Sistema Nacional de Información de Fiscalización Ambiental), de los
informes de seguimiento ambiental presentados por Fundición Chagres de Anglo
American Sur S.A.

En el caso de MP2,5 y CO, no se encontró información disponible en alguna estación
cercana al proyecto que registren estos contaminantes.

La metodología empleada para la caracterización de la calidad del aire del área de
influencia del Proyecto incluye la localización de la estación de monitoreo, el análisis
estadístico y comparativo con normativa asociada a la calidad del aire.

2.4.1 Descripción de la Red de Monitoreo de Calidad de Aire Existente en la Zona de

Estudio

Las estaciones de monitoreo disponibles en la zona de estudio se presentan en Tabla 2.
En esta tabla se indica su ubicación geográfica en coordenadas UTM (WGS 84) y la
disponibilidad de datos de contaminantes. La ubicación de estas estaciones se muestra
en Figura 7.

Tabla 2: Estación monitora de calidad de aire en el dominio de la zona de estudio

|Red|Estación|Coordenadas UTM<br>Datum WGS 84 - Z19|Col4|MP10|MP2,5|NO<br>2|SO<br>2|CO|
|---|---|---|---|---|---|---|---|---|
|Red|Estación|UTM-E (m)|UTM-N (m)|UTM-N (m)|UTM-N (m)|UTM-N (m)|UTM-N (m)|UTM-N (m)|
|Ministerio del Medio<br>Ambiente|Los Andes|351.534|6.364.623|||X|||

Estudio EM2023/200-54 | Ecoazul

24
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

|Red|Estación|Coordenadas UTM<br>Datum WGS 84 - Z19|Col4|MP10|MP2,5|NO<br>2|SO<br>2|CO|
|---|---|---|---|---|---|---|---|---|
|Red|Estación|UTM-E (m)|UTM-N (m)|UTM-N (m)|UTM-N (m)|UTM-N (m)|UTM-N (m)|UTM-N (m)|
|Fundición Chagres de<br>Anglo American Sur S.A.|Catemu|316.512|6.371.481|X|||X||

Figura 7: Ubicación de las estaciones de calidad de aire de la zona de Estudio.

2.4.2 Marco Jurídico Vigente en Chile

Dentro del marco jurídico vigente en Chile existen las Normas de Calidad Primarias y
Secundarias de Calidad de Aire, las cuales han sido establecidas a través del Ministerio
Secretaría General de la Presidencia (MINSEGPRES) o Ministerio del Medio Ambiente.

Los valores límites y su periodo de evaluación para los contaminantes de interés del
Proyecto MP10, MP2,5, SO 2, NO 2, CO y MPS se presentan en Tabla 3.

Estudio EM2023/200-54 | Ecoazul

25
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

Tabla 3: Normas Primarias y Secundarias de calidad de aire de Chile para los
contaminantes de interés del Proyecto.

|Contaminante|Periodo de Evaluación|Valor Norma|Norma|
|---|---|---|---|
|Material Particulado<br>Respirable<br>(MP10)|Concentración de 24 horas|130 (μg/Nm3)|Norma Primaria<br>D.S. No 12/2021 del<br>MINISTERIO DEL<br>MEDIO AMBIENTE|
|Material Particulado<br>Respirable<br>(MP10)|Concentración anual|50 (μg/Nm3)|50 (μg/Nm3)|
|Material Particulado<br>Fino Respirable (MP2,5)|Concentración de 24 horas|50 (μg/Nm3)|Norma Primaria<br>D.S. No 12/2011 del<br>MINISTERIO DEL<br>MEDIO AMBIENTE|
|Material Particulado<br>Fino Respirable (MP2,5)|Concentración anual|20 (μg/Nm3)|20 (μg/Nm3)|
|Dióxido de Nitrógeno<br>(NO2)|Concentración de 1 hora|400 (μg/Nm3)|Norma Primaria<br>D.S. No 114/2002 del<br>MINSEGPRES|
|Dióxido de Nitrógeno<br>(NO2)|Concentración anual|100 (μg/Nm3)|100 (μg/Nm3)|
|Dióxido de Azufre (SO2)|Concentración anual|60 (μg/Nm3)|Norma Primaria<br>D.S. No 104/2018 del<br>MINISTERIO DEL<br>MEDIO AMBIENTE|
|Dióxido de Azufre (SO2)|Concentración de 24 horas|130 (μg/Nm3)|130 (μg/Nm3)|
|Dióxido de Azufre (SO2)|Concentración de 1 hora|350 (μg/Nm3)|350 (μg/Nm3)|
|Dióxido de Azufre (SO2)|Concentración anual|80 (μg/Nm3)|Norma Secundaria<br>DS No 22/2009<br>MINSEGPRES para la<br>zona norte|
|Dióxido de Azufre (SO2)|Concentración de 24 horas|365 (μg/Nm3)|365 (μg/Nm3)|
|Dióxido de Azufre (SO2)|Concentración de 1 hora|1.000 (μg/Nm3)|1.000 (μg/Nm3)|
|Monóxido de Carbono<br>(CO)|Concentración de 8 horas|10.000 (μg/Nm3)|Norma Primaria<br>D.S. No 115/2002 del<br>MINSEGPRES|
|Monóxido de Carbono<br>(CO)|Concentración de 1 hora|30.000 (μg/Nm3)|30.000 (μg/Nm3)|
|Material Particulado<br>Sedimentable (MPS)|Concentración anual|200 (mg/m2-día)|Ordenanza<br>Confederación Suiza|

2.4.3 Información de Calidad de Aire para Material Particulado Respirable (MP10),

Periodo 2020 - 2022.

La información de calidad del aire por MP10 registrada por la Catemu durante el periodo
2020 - 2022 se presenta en Tabla 4 como concentraciones promedio anuales de este
contaminante. En esta tabla se puede observar que esta estación se encuentra sobre la
norma correspondiente.

Estudio EM2023/200-54 | Ecoazul

26
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

Por otra parte, en Tabla 5 se presentan los Percentiles 98 de las concentraciones de 24
horas de MP10, registrados por la estación Catemu durante el periodo 2020 - 2022. En
esta tabla se observa que, considerando la norma diaria del D.S. 12/2022, se supera la
norma durante todos los años presentados.

Tabla 4: Concentración anual de MP10 registrada por la estación Los Andes. Periodo
2020 - 2022.

|Estación|Año|% Datos<br>mensuales<br>válidos|Promedio<br>Anual<br>(μg/m3N)|Promedio<br>Trianual<br>(μg/m3N)|% de la Norma Anual (D.S. No 12/2022 del<br>Ministerio del Medio Ambiente, 50<br>μg/m3N)|
|---|---|---|---|---|---|
|Catemu|2020|100|126,92|108,42|217|
|Catemu|2021|100|96,58|96,58|96,58|
|Catemu|2022|100|101,76|101,76|101,76|

Tabla 5: Percentil 98 de las concentraciones 24 horas de MP10 registrada por la
estación Los Andes. Periodo 2020 - 2022.

|Estación|Año|% Datos 24<br>horas<br>válidos|Percentil 98<br>(μg/m3N)|% de la Norma Diaria (D.S. No 12/2022 del<br>Ministerio del Medio Ambiente, 130<br>μg/m3N)|
|---|---|---|---|---|
|Catemu|2020|99,7|193,4|149|
|Catemu|2021|98,1|193,8|149|
|Catemu|2022|100,0|177,9|137|

Estudio EM2023/200-54 | Ecoazul

27
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

Figura 8: Serie de tiempo de MP10 observado en la estación Catemu durante el periodo

2020 - 2022.

2.4.4 Información de Calidad de Aire para Dióxido de Azufre (SO 2 ), Periodo 2020 -2022.

La información de calidad del aire por SO 2 registrada en la estación Catemu durante el
periodo 2020 - 2022 se presenta en Tabla 6 a Tabla 8, como promedio anual y percentil
99 de las concentraciones 24 horas y percentil 98,5 de las concentraciones horarias,
respectivamente.

Como se observa en estas tablas, no se superaría la norma de SO 2 en la estación Catemu
durante el periodo considerado.

Por otra parte, en Figura 9 se muestra la serie de tiempo de SO 2 registrada en la estación
Catemu durante el periodo 2020 - 2022.

Tabla 6: Concentración anual SO 2 registrada en la estación Catemu. Periodo 20202022.

|Estación|Año|% Datos<br>mensuales<br>válidos|Promedio<br>Anual<br>(μg/m3N)|Promedio<br>Trianual<br>(μg/m3N)|% de la Norma anual (D.S. No 104/2019<br>del Ministerio del Medio Ambiente, 60<br>μg/m3N)|
|---|---|---|---|---|---|
|Catemu|2020|100|12,07|11,91|20|

Estudio EM2023/200-54 | Ecoazul

28
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

|Estación|Año|% Datos<br>mensuales<br>válidos|Promedio<br>Anual<br>(μg/m3N)|Promedio<br>Trianual<br>(μg/m3N)|% de la Norma anual (D.S. No 104/2019<br>del Ministerio del Medio Ambiente, 60<br>μg/m3N)|
|---|---|---|---|---|---|
||2021|100|13,27|||
||2022|100|10,40|10,40|10,40|

Tabla 7: Percentil 99 de las concentraciones diarias de SO 2 registrados en la estación
Catemu. Periodo 2020 - 2022.

|Estación|Año|% Datos 24<br>horas<br>válidos|Percentil 99<br>(μg/m3N)|Promedio<br>Trianual<br>(μg/m3N)|% de la Norma 24 horas (D.S. No<br>104/2019 del Ministerio del Medio<br>Ambiente, 150 μg/m3N)|
|---|---|---|---|---|---|
|Catemu|2020|99|40,25|32,78|22|
|Catemu|2021|98|34,04|34,04|34,04|
|Catemu|2022|98|24,05|24,05|24,05|

Tabla 8: Percentil 99 de las concentraciones de 1 hora de SO 2 registrada en la estación
Catemu. Periodo 2020 - 2022.

|Estación|Año|% Datos 1<br>hora<br>válidos|Percentil<br>98,5<br>(μg/m3N)|Promedio<br>Trianual<br>(μg/m3N)|% de la Norma 1 hora (D.S. No<br>104/2019 del Ministerio del Medio<br>Ambiente, 350 μg/m3N)|
|---|---|---|---|---|---|
|Catemu|2020|98|59,00|55,33|16|
|Catemu|2021|98|59,00|59,00|59,00|
|Catemu|2022|98|48,00|48,00|48,00|

Estudio EM2023/200-54 | Ecoazul

29
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

Figura 9: Serie de tiempo de SO 2 observado en la estación Catemu durante el periodo

2020 - 2022.

2.4.5 Información de Calidad de Aire para Dióxido de Nitrógeno (NO 2 ), Periodo 20202022.

La información de calidad del aire por NO 2 registrada en la estación Los Andes durante
el periodo 2020 - 2022 se presenta en Tabla 9 y Tabla 10, como promedio anual y
percentil 99 de las concentraciones horarias, respectivamente. Como se aprecia en
estas tablas, en ninguna de las estaciones presentadas se superaría la norma de NO 2
anual ni horaria.

Por otra parte, en Figura 10 se muestra la serie de tiempo de NO 2 en la estación Los
Andes disponibles en el SINCA, durante el periodo 2020 - 2022.

Tabla 9: Concentración anual NO 2 registrada en la estación Los Andes. Periodo 2020

|Col1|- 2022.|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|Estación|Año|% Datos<br>trimensuales<br>válidos|Promedio<br>Anual<br>(μg/m3N)|Promedio<br>Trianual<br>(μg/m3N)|% de la Norma Anual (D.S. No 114/2013<br>del Ministerio Secretaría General de la<br>República, 100 μg/m3N)|
|Los Andes|2020|100|18,97|21,21|21|
|Los Andes|2021|93|20,06|20,06|20,06|

Estudio EM2023/200-54 | Ecoazul

30
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

|Estación|Año|% Datos<br>trimensuales<br>válidos|Promedio<br>Anual<br>(μg/m3N)|Promedio<br>Trianual<br>(μg/m3N)|% de la Norma Anual (D.S. No 114/2013<br>del Ministerio Secretaría General de la<br>República, 100 μg/m3N)|
|---|---|---|---|---|---|
||2022|84|24,61|||

Tabla 10: Percentil 99 de los máximos diarios de concentración de 1 hora de NO 2

registrada en la estación Los Andes. Periodo 2020 - 2022.

|Estación|Año|% Datos<br>máximos<br>horarias<br>válidos|Percentil 99<br>(μg/m3N)|Promedio<br>Trianual<br>(μg/m3N)|% de la Norma 24 horas (D.S. No<br>114/2013 del Ministerio Secretaría<br>General de la República, 400<br>μg/m3N)|
|---|---|---|---|---|---|
|Los Andes|2020|99|78,34|88,05|22|
|Los Andes|2021|92|81,29|81,29|81,29|
|Los Andes|2022|83|104,51|104,51|104,51|

Figura 10: Series de tiempo de NO 2 observado en la estación Los Andes durante el

periodo 2020 - 2022.

Estudio EM2023/200-54 | Ecoazul

31
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

# CAPÍTULO 3: IMPLEMENTACIÓN, APLICACIÓN Y RESULTADOS DEL MODELO METEOROLÓGICO WRF

## 3.1 Introducción

En este Capítulo se presenta la implementación y aplicación del modelo meteorológico
WRF v4.2 (Weather Research and Forecasting Model). WRF es uno de los modelos
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

En Figura 11 se presenta un diagrama de operación del modelo WRF. Como se observa
en esta figura, este sistema considera como información de entrada meteorología del
sistema GFS y/o datos de estaciones meteorológicas locales, además de topografía y
uso de suelos. Con los archivos de salida del modelo se puede obtener un archivo
formato tipo CALMET, el cual sirve de entrada para el modelo CALPUFF.

Estudio EM2023/200-54 | Ecoazul

32
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

Figura 11: Diagrama de operación del modelo meteorológico WRF.

## 3.2 Implementación del Modelo Meteorológico WRF

En esta sección se presenta la implementación y aplicación del modelo meteorológico
WRF para la generación de la meteorología requerida por el modelo CALPUFF para el
año 2022.

El modelo se implementó con dos grillas anidadas en la zona de ubicación del Proyecto,
Región de Valparaíso. Las condiciones de borde e iniciales de los datos históricos del
año 2022 fueron proporcionadas por GDAS de NOAA (National Oceanic and Atmospheric
Administration), de USA, con una resolución espacial de 0,25 grados.

Respecto a la topografía del dominio de modelación fue obtenida a partir del proyecto
SRTM (del acrónimo inglés Shuttle Radar Topography Mission) con resolución de 3
segundos de grado (90 m aproximadamente) y el uso de suelo a partir de la información
satelital MODIS (del acrónimo inglés Moderate-Resolution Imaging Spectroradiometer)
de la NASA con resolución de 15 segundos de grado.

Estudio EM2023/200-54 | Ecoazul

33
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

El dominio de modelación utilizado del área de Estudio consideró la grilla N° 2 de WRF,
por ser la que posee una resolución con tamaño de grilla de 1 km x 1 km para definir la
topografía y uso de suelo. Esta grilla tiene dimensiones de 67 kilómetros en la dirección
Este-Oeste y 61 kilómetros en la dirección Norte-Sur, alrededor de su centro ubicado en
los 32,760 latitud Sur y 70,745 longitud Oeste. Las características generales de esta
grilla se presentan en Tabla 11 y las 2 grillas anidadas modeladas se muestran en Figura
12.

|bla 11: Características del dominio de modelación de la segunda grilla utilizada el modelo WRF en la zona de Estudio.|Col2|
|---|---|
|Características Grilla 2 de WRF|Características Grilla 2 de WRF|
|Resolución|1 x 1 (km)|
|No de celdas en dirección X|67|
|No de celdas en dirección Y|61|
|Coordenadas del centro del dominio|Latitud: -32,760; Longitud: -70,745|

Figura 12: Dominios de modelación de WRF en la zona de Estudio.

Estudio EM2023/200-54 | Ecoazul

34
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

Respecto a la configuración del modelo, en relación a la física y dinámica, se
consideraron las parametrizaciones del trabajo por el documento Guía para el uso de
modelos de calidad del aire en el SEIA, 2012, cuyos principales esquemas son
mostrados en Tabla 12.

Tabla 12: Configuración de las principales parametrizaciones utilizadas en la

modelación con WRF para la zona de Estudio.

|Variable|Nombre|Esquema|Descripción|
|---|---|---|---|
|Microfísica|mp_physics|WSM5|WSM (3 especies microfísicas)|
|Radiación de onda<br>larga|ra_lw_physics|RRTM|Modelo de transferencia<br>radiativa rápida que utiliza<br>tablas de eficiencia. Cuenta<br>con 35iffusion bandas|
|Radiación de onda<br>corta|ra_sw_physics|Dudhia scheme|Integración simple que permite<br>la absorción y dispersión por<br>nubes y a cielo despejado|
|Capa superficial|sf_sfclay_physics|MM5|Monin-Obukhov similaridad|
|Superficie|sf_surface_physcis|Thermal Diffusion<br>Scheme|Esquema de 35iffusion termal|
|Capa límite<br>planetaria|bl_pbl_physics|YSU scheme|QNSE|

## 3.3 Resultados del Modelo WRF en la Zona de Estudio

En la presente sección se muestran los resultados del modelo meteorológico WRF. Estos
provienen de las variables extraídas en las coordenadas de la estación meteorológica
presentada en la sección 2.3 del presente informe (Tabla 1).

3.3.1 Series de Tiempo de Variables Meteorológicas Modeladas con WRF Año 2022

Las series de tiempo de velocidad y dirección de viento, humedad relativa y temperatura,
modeladas con WRF en la estación Los Andes para el año 2022 se muestran en Figura
13.

La velocidad de viento se mantiene bajo los 6 m/s. Se visualizan ciertos eventos de
máximos de velocidad de viento en los meses de primavera, lo que podría indicar que el

Estudio EM2023/200-54 | Ecoazul

35
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

modelo intenta reproducir ciertas ráfagas debido a eventos de inestabilidad atmosférica
en dicho periodo. Respecto a la dirección de viento en estación Los Andes no es posible
visualizar un patrón de la variable.

Con respecto a la temperatura modelada, se visualiza un aumento de la magnitud en los
meses de verano y una disminución en los meses de invierno. Esto al igual que la
humedad relativa, da un atisbo de una buena reproducción de las variables
meteorológicas por WRF en el dominio de interés.

Finalmente, en la humedad relativa no se visualiza un patrón definido.

Estudio EM2023/200-54 | Ecoazul

36
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

Figura 13: Series de tiempo de variables meteorológicas modeladas con WRF en la

estación Los Andes durante el año 2022.

Estudio EM2023/200-54 | Ecoazul

37
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

3.3.2 Ciclos Diarios de Variables Meteorológicas Modeladas con WRF para el Año 2022

Los ciclos diarios modelados en la estación Los Andes para el año 2022 se presentan
en la Figura 14.

Respecto a la velocidad de viento se visualiza que el modelo reproduce el ciclo con un
aumento de la magnitud en el día y una disminución en la noche.

Respecto a la dirección de viento, el modelo reproduce viento sureste durante la noche
y noroeste durante el día.

Comentando la temperatura modelada, se visualiza el aumento de la magnitud en el día
y la disminución por la noche.

Finalmente, respecto a la humedad relativa modelada, se visualiza que fue reproducido
el ciclo con el aumento de la magnitud en la noche y la diminución en el día.

Estudio EM2023/200-54 | Ecoazul

38
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

Figura 14: Ciclos diarios de variables meteorológicas modeladas con WRF en la

estación Los Andes durante el año 2022.

Estudio EM2023/200-54 | Ecoazul

39
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

3.3.3 Ciclos Estacionales de Variables Meteorológicas Modeladas con WRF Durante el

Año 2022

En la Figura 15 se muestran los ciclos estacionales de las variables meteorológicas
modeladas en la estación Los Andes durante el año 2022.

Comentando el ciclo estacional de la velocidad de viento, se visualiza un aumento de la
magnitud durante el día y en los meses de verano.

Respecto a la dirección de viento, el viento modelado es predominantemente noreste
por la noche durante y varía en la madrugada a noroeste en invierno. También se
observan direcciones norte y noroeste durante el día.

Describiendo la temperatura modelada en estación Los Andes, se visualizan los
máximos de temperatura en el día y en los meses de verano, mientras que en invierno y
periodo nocturno se modelan los mínimos.

Finalmente, respecto a la humedad relativa modelada, se observan los máximos en el
periodo nocturno durante todo el año, mientras que en el día es el mínimo de la variable.

Estudio EM2023/200-54 | Ecoazul

40
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

Figura 15: Ciclos estacionales de variables meteorológicas modelados con WRF la

estación Los Andes durante el año 2022.

Estudio EM2023/200-54 | Ecoazul

41
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

3.3.4 Rosas de Viento Modeladas con WRF Durante el Año 2022

En Figura 16 se presentan las rosas de viento construidas con las series de tiempo
modeladas en la estación Los Andes. En dicha figura se muestran cuatro rangos de
tiempo horarios, los cuales son descritos a continuación:

 Periodo noche o madrugada, 01:00 a 06:00 horas: se visualizan vientos de

tendencia noreste y en menor medida desde el oeste, con velocidades de hasta 2
m/s.

 - Periodo mañana, 07:00 a 14:00 horas: en estación Los Andes muestra vientos de

tendencia principalmente oeste y magnitudes que llegan a los 3 m/s.

 Periodo tarde, 15:00 a 23:00 horas: se visualiza componente noreste y oeste con

velocidades de hasta 4 m/s.

 Periodo completo, 00:00 a 23:00 horas: se visualizan componentes mayormente

noreste y oeste, con velocidades de hasta 4 m/s.

Estudio EM2023/200-54 | Ecoazul

42
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

Figura 16: Rosas de viento modeladas con WRF en la estación Los Andes durante el

año 2022.

Estudio EM2023/200-54 | Ecoazul

43
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

3.3.5 Campos de Viento Promedios Modelados con WRF durante el Año 2022

Los patrones espaciales de viento en el dominio de modelación se presentan mediante
mapas de viento, donde están representados los vientos en términos de su magnitud y
dirección.

En Figura 17 a Figura 28 se muestran los campos de vientos promedios de verano,
otoño, invierno y primavera del año 2022 para los siguientes periodos del día:

 Periodo noche o madrugada: 22:00 a 05:00 horas

 - Periodo mañana: 06:00 a 13:00 horas

 - Periodo tarde: 14:00 a 21:00 horas

En estas figuras se observan vientos mayormente predominantes desde el Sur que
varían a Suroeste durante la tarde. También se aprecia que los vientos son de mayor
magnitud durante los meses de primavera y verano.

Estudio EM2023/200-54 | Ecoazul

44
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

Figura 17. Campos de vientos promedio de verano del año 2022, periodo nocturno de

22:00 a 05:00 horas.

Estudio EM2023/200-54 | Ecoazul

45
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

Figura 18. Campos de vientos promedio de verano del año 2022, periodo matutino de

06:00 a 13:00 horas.

Estudio EM2023/200-54 | Ecoazul

46
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

Figura 19. Campos de vientos promedio de verano del año 2022, periodo vespertino de

14:00 a 21:00 horas.

Estudio EM2023/200-54 | Ecoazul

47
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

Figura 20. Campos de vientos promedio de otoño del año 2022, periodo nocturno de

22:00 a 05:00 horas.

Estudio EM2023/200-54 | Ecoazul

48
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

Figura 21. Campos de vientos promedio de otoño del año 2022, periodo matutino de

06:00 a 13:00 horas.

Estudio EM2023/200-54 | Ecoazul

49
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

Figura 22. Campos de vientos promedio de otoño del año 2022, periodo vespertino de

14:00 a 21:00 horas.

Estudio EM2023/200-54 | Ecoazul

50
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

Figura 23. Campos de vientos promedio de invierno del año 2022, periodo nocturno de

22:00 a 05:00 horas.

Estudio EM2023/200-54 | Ecoazul

51
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

Figura 24. Campos de vientos promedio de invierno del año 2022, periodo matutino de

06:00 a 13:00 horas.

Estudio EM2023/200-54 | Ecoazul

52
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

Figura 25. Campos de vientos promedio de invierno del año 2022, periodo vespertino

de 14:00 a 21:00 horas.

Estudio EM2023/200-54 | Ecoazul

53
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

Figura 26. Campos de vientos promedio de primavera del año 2022, periodo nocturno

de 22:00 a 05:00 horas.

Estudio EM2023/200-54 | Ecoazul

54
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

Figura 27. Campos de vientos promedio de primavera del año 2022, periodo matutino

de 06:00 a 13:00 horas.

Estudio EM2023/200-54 | Ecoazul

55
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

Figura 28. Campos de vientos promedio de primavera del año 2022, periodo vespertino

de 14:00 a 21:00 horas.

## 3.4 Análisis de Incertidumbre de los Resultados del Modelo WRF Respecto de los Datos Observados en Estación Los Andes Durante el Año 2022

En esta sección se analiza el nivel de incertidumbre del modelo meteorológico WRF, de
forma cualitativa mediante la comparación de gráficos, ciclos diarios y estacionales, y
de forma cuantitativa mediante estadísticos matemáticos obtenidos por comparación
entre los datos horarios de las observaciones y los resultados simulados con WRF.

Los estadísticos matemáticos calculados son los siguientes:

Error cuadrático medio (RMSE): entrega el grado de precisión entre los datos

pronosticados y observados.

Estudio EM2023/200-54 | Ecoazul

56
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

Sesgo normalizado (BIASN): entrega el sesgo entre las series modeladas y

observadas.

Error Absoluto Medio (MAE): Es la diferencia entre el valor pronosticado y el valor real

en cada punto pronosticado.

Coeficiente de correlación (R): entrega el grado de relación lineal entre los datos

observados y modelados.

Las fórmulas y rango de estos estadísticos se presentan en Tabla 13.

Tabla 13: Estadísticos Matemáticos de Literatura.

|Estadístico|Ecuación|Rango|
|---|---|---|
|RMSE|√∑(Mi−Oi)2<br>n<br>n<br>i=1<br>|, ∞|
|BIASN|∑<br>Mi−Oi<br>n<br>i=1<br>∑<br>Oi<br>n<br>i=1<br>|(-∞,∞|
|MAE|1<br>n∑|Mi−Oi|<br>n<br>i=1<br>|(-∞,∞|
|R|1<br>(1 −n)∑(Mi−M)<br>̅<br>σM<br>N<br>i=1<br>(Oi−O)<br>̅<br>σo<br>|[-1,1]|

Fuente: Elaboración propia en base a Wilks, 2011.

3.4.1 Análisis Cualitativo Series de Tiempo Observados y Modelados con WRF, Año

2022

En Figura 29 se presenta la comparación de las series de tiempo de variables
meteorológicas observados a la izquierda y modelados con WRF a la derecha, durante
el año 2022 en la estación Los Andes, respectivamente.

Estudio EM2023/200-54 | Ecoazul

57
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

Observando las series de tiempo de velocidad, se aprecia que el modelo sobrestimó
levemente la velocidad de viento, especialmente en los peak durante el invierno y
primavera.

Respecto a la dirección de viento, se visualiza que el modelo tiene una tendencia a
reproducir la variabilidad vista en las observaciones, sin embargo, se visualiza
diferencias principalmente en los meses invernales.

Revisando la temperatura modelada, se visualiza que el modelo reproduce bien el ciclo
diario, aunque subestima levemente la magnitud.

Respecto a la humedad relativa, se visualiza que el modelo sobreestimó levemente las
magnitudes a lo largo del año.

Estudio EM2023/200-54 | Ecoazul

58
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

Figura 29: Comparación variables meteorológicas observadas y modeladas con WRF

en la estación Los Andes durante el año 2022.

Estudio EM2023/200-54 | Ecoazul

59
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

3.4.2 Análisis Cualitativo de Ciclos Diarios Observados y Modelados con WRF, Año

2022

La comparación de ciclos diarios de variables meteorológicas observados a la izquierda
y modelados con WRF a la derecha, durante el año 2022 en la estación Los Andes se
presenta en Figura 30.

Respecto a los ciclos diarios de velocidad de viento, muestran que el modelo lo
reproduce relativamente bien.

Revisando la dirección de viento, el modelo en términos generales logra reproducir los
patrones diarios, aunque levemente desviados.

Comentando los ciclos de la temperatura, se visualiza que el modelo logra reproducir
bien el ciclo diario, aunque subestima levemente la magnitud.

Finalmente, respecto a la humedad relativa, el modelo reproduce las fluctuaciones del
ciclo diario, sin embargo, sobrestima las magnitudes durante todo el año.

Estudio EM2023/200-54 | Ecoazul

60
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

Figura 30: Comparación de ciclos diarios de variables meteorológicas observados y

modelados con WRF en estación Los Andes durante el año 2022.

Estudio EM2023/200-54 | Ecoazul

61
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

3.4.3 Análisis Cualitativo de Ciclos Estacionales Observados y Modelados con WRF,

Año 2022

En Figura 31 se presenta la comparación de los ciclos estacionales de variables
meteorológicas observados a la izquierda y modelados con WRF a la derecha, durante
el año 2022 en la estación Los Andes.

Analizando los ciclos estacionales de las variables meteorológicas modeladas por WRF,
se aprecia que el modelo reproduce el área de máximos de velocidad diurnos y verano,
expresado por la coloración verde amarilla.

Respecto a la dirección de viento, el modelo logra reproducir los vientos nocturnos
noreste. Durante el día, reproduce los vientos noroeste. Se observa una desviación
durante la noche en los meses de invierno donde en las observaciones se visualiza
viento noreste y el modelo reproduce viento noroeste.

Respecto a la temperatura, el modelo subestima en el periodo diurno y en los meses de

verano.

Finalmente, describiendo la humedad relativa, el modelo sobrestima la magnitud de la
variable durante todo el año.

Estudio EM2023/200-54 | Ecoazul

62
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

Figura 31: Comparación de ciclos estacionales de variables meteorológicas

observados y modelados con WRF en estación Los Andes durante el año
2022.

Estudio EM2023/200-54 | Ecoazul

63
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

3.4.4 Análisis Cualitativo de Rosas de Viento Observadas y Modeladas con WRF, Año

2022

La comparación de rosas de viento entre observaciones y modelado con WRF en la
estación Los Andes del año 2022 se presenta en Figura 32.

A continuación, se describe en detalle los cuatro periodos mostrados por las rosas de
viento construidas:

 Periodo 01:00 a 06:00 horas: en estación Los Andes el modelo reproduce una leve

desviación hacia el este. En cuanto a magnitudes las reproduce adecuadamente.

 Periodo 07:00 a 14:00 horas: se observa que el no reproduce los vientos

principales noreste y sobrestima la componente oeste.

 Periodo 15:00 a 23:00 horas: el modelo reproduce bien los vientos principales

noroeste y suroeste.

 Periodo 00:00 a 23:00 horas: en general el modelo reproduce bien las direcciones

promedio de la estación Los Andes, aunque con una leve desviación hacia el este.
En el caso de la componente suroeste, el modelo lo reproduce con una leve
desviación hacia el norte.

Estudio EM2023/200-54 | Ecoazul

64
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

Figura 32: Comparación de rosas de viento observadas y modeladas con WRF en

estación Los Andes durante el año 2022.

Estudio EM2023/200-54 | Ecoazul

65
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

3.4.5 Análisis Cuantitativo

El análisis cuantitativo es realizado mediante la utilización de los estadísticos descritos
al inicio de la sección 3.4. Estos son resultados de la comparación entre las series de
datos observados y modelados con WRF, extraídos en la estación Los Andes, los cuales
se presentan en la en la Tabla 14, donde se consolida toda la información. Estos
estadísticos dan una muestra del desempeño del modelo en el punto geográfico
analizados.

Considerando la tabla descrita se puede indicar lo siguiente:

- Analizado el estadístico BIASN,

 - Velocidad de Viento: El modelo sobrestima levemente las observaciones en

estación Los Andes, manteniéndose bajo 2,5 m/s.

 - Humedad Relativa: El modelo sobrestima levemente la humedad observada.

 - Temperatura: El modelo subestima las observaciones en Los Andes, muy por

debajo de los 4 oC.

Respecto al RMSE:

 - Velocidad de viento: el modelo en promedio tuvo una alta precisión, con valores

bajo los 3,5 m/s.

 - Temperatura: la precisión del modelo fue buena con valores menores a 4,5 °C.

Respecto al error absoluto medio, se puede apreciar lo siguiente:

 - Velocidad de viento: el modelo sobrestima levemente la magnitud de las

observaciones, manteniéndose bajo 3 m/s.

 - Temperatura: el modelo sobrestima levemente las observaciones, manteniéndose

bajo 4 °C.

Finalmente, respecto al estadístico de correlación R

 - Velocidad de viento: el modelo tuvo un grado de correlación aceptable, siendo

cercano a 0,6.

 - Humedad relativa: el modelo tuvo un grado de correlación aceptable, siendo

cercano a 0,7.

Estudio EM2023/200-54 | Ecoazul

66
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

 - Temperatura: entre las variables estudiadas es la que tiene la mejor relación con

las observaciones, la más cercana a 1.

Tabla 14: Resultados estadísticos obtenidos de la comparación de datos observados y

modelados con WRF en las estaciones de la zona de estudio.

|Estadística|Variable|Unidad|Estación Los Andes|
|---|---|---|---|
|BiasN|VV|m/s|0,26|
|BiasN|HR|%|0,39|
|BiasN|T|°C|-0,12|
|RMSE|VV|m/s|0,93|
|RMSE|HR|%|23,76|
|RMSE|T|°C|3,73|
|MAE|VV|m/s|0,65|
|MAE|HR|%|20,27|
|MAE|T|°C|2,98|
|R|VV|Adimensional|0,53|
|R|HR|Adimensional|0,68|
|R|T|Adimensional|0,94|

VV: velocidad de viento HR: humedad relativa T: temperatura del aire.

Estudio EM2023/200-54 | Ecoazul

67
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

# CAPÍTULO 4: IMPLEMENTACIÓN, APLICACIÓN Y RESULTADOS DEL MODELO DE DISPERSIÓN CALPUFF

## 4.1 Introducción

El sistema de modelación CALPUFF, está actualmente aprobado por el Servicio de
Evaluación Ambiental (SEA) de Chile y por la EPA (USA) como modelo regulatorio para
evaluar el impacto de emisiones atmosféricas en escenarios de terreno y meteorología
compleja. Este sistema está compuesto por los modelos WRF y CALPUFF, cuya
descripción general es la siguiente:

WRF: Modelo de mesoescala y micrometeorológico capaz de generar la
meteorología requerida por el modelo CALPUFF con resolución de 1 km, para la
evaluación de contaminantes primarios.

CALPUFF: Modelo lagrangiano de dispersión tipo puff que permite simular el
transporte, dispersión e impacto de emisiones de contaminantes primarios de
procesos naturales y antropogénicos, utilizando la meteorología generada por WRF.

El análisis de resultados de los modelos WRF y CALPUFF se realiza con el software
CalDESK Advanced v2.98 [1] . Esta herramienta permite generar mapas de
isoconcentraciones de contaminantes y visualizar los resultados de todas las variables
entregadas por los modelos.

En Figura 33 se presenta un diagrama del sistema CALPUFF, donde se ilustran los
diferentes archivos de entrada requeridos por los modelos WRF y CALPUFF. Como se
observa en esta figura, WRF requiere la topografía y usos de suelos locales, junto con la
meteorología proporcionada por el sistema GFS (ver Capítulo 3). Por otra parte,
CALPUFF requiere, la meteorología generada por WRF con el formato de CALMET
(calmet.dat) y la información de emisiones, entregada en el Inventario de Emisiones.

1: Software de visualización y Análisis, Desarrollado por Enviromodeling Ltda., para el sistema CALPUFF.

Estudio EM2023/200-54 | Ecoazul

68
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

Figura 33: Diagrama de operación del sistema de modelación WRF/CALPUFF/CalDesk.

## 4.2 Implementación y Aplicación del Modelo de Dispersión CALPUFF

El modelo de dispersión CALPUFF se implementó en la zona de estudio utilizando un
mismo dominio levemente menor al de WRF descrito en la Sección 3.2. El dominio
utilizado se presenta en Tabla 15, el que cubre un área de 56 x 50 km [2] con una resolución
de 1 km y que se muestra en Figura 34.

|Tabla 15: Características del dominio de modelación utilizada por el modelo CALPUFF en la zona de Estudio (archivo CALPUFF_Ready).|Col2|
|---|---|
|Características dominio CALPUFF-Ready|Características dominio CALPUFF-Ready|
|Resolución|1.000 x 1.000 (m)|
|No de celdas en dirección X|56|
|No de celdas en dirección Y|50|
|Coordenadas de referencia del origen del dominio*|UTM-E: 336.539 (m), UTM-N: 6.373.972 (m).|

Estudio EM2023/200-54 | Ecoazul

69
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

|Características dominio CALPUFF-Ready|Col2|
|---|---|
|Total del área del dominio|2.800 (km2)|

*: Coordenada de referencia en UTM datum WGS 84 (aproximada), el dominio corresponde a la segunda grilla

anidada en la implementación del modelo WRF, la cual está en proyección Lambert Conformal Conic (LCC).

Figura 34: Dominio de modelación de CALPUFF, 56 x 50 km [2], en coordenadas LCC.

4.2.1 Receptores de Grilla y Discretos

Como se mencionó anteriormente el modelo CALPUFF se implementó en un área de 56
x 50 km [2] con resolución de 1 km, tal como se presentó en Tabla 15. Sin embargo, se

Estudio EM2023/200-54 | Ecoazul

70
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

calcularon concentraciones para un área de 50 km x 41 km. De esta forma, CALPUFF
entregó concentraciones para un área de 2.050 km [2] . Esta área se muestra en Figura 35.

Figura 35: Dominio de modelación de CALPUFF, 50 x 41 km [2], en coordenadas LCC.

En cuanto a los receptores discretos, se consideraron 36 receptores de interés, de los
cuales 2 corresponden a estaciones de monitoreo de calidad de aire cercanas al
Proyecto ubicadas en Los Andes y Catemu y los 34 restantes se ubican alrededor del
Proyecto que representan a áreas habitadas (viviendas). Las características de estos
receptores, como su descripción, ubicación y altitud, se presentan en Tabla 16. La
ubicación de los receptores de interés alrededor del Proyecto se muestra en Figura 36 y
Figura 37.

Es importante mencionar que los resultados obtenidos mediante receptores discretos
son valores calculados por el modelo en el punto de interés, es decir, tiene una precisión

Estudio EM2023/200-54 | Ecoazul

71
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

mayor con respecto a los resultados de grilla, donde los resultados son interpolados
para entregar las concentraciones en todo el dominio de modelación.

Tabla 16: Coordenadas de receptores de interés en la zona del Proyecto.

|Receptor|Descripción|UTM (WGS 84 - Z18)|Col4|Altitud (1)<br>(m.s.n.m.)|LCC (km)|Col7|
|---|---|---|---|---|---|---|
|Receptor|Descripción|Este (m)|Norte (m)|Norte (m)|LCC-X|LCC-Y|
|R1|Los Andes|351.534|6.364.623|877|14,840|-9,596|
|R2|Catemu|316.512|6.371.481|432|-20,066|-2,160|
|R3|Iglesia Almendral|341.420|6.375.196|682|4,901|1,144|
|R4|Iglesia Curimón|341.799|6.371.393|704|5,217|-2,665|
|R5|Catedral San Felipe|338.454|6.375.087|649|1,933|1,084|
|R6|Colegio Rinconada|342.147|6.365.180|727|5,463|-8,884|
|R7|Colegio Curimón|339.688|6.372.404|675|3,123|-1,620|
|R8|Vecino N°1|341.348|6.368.314|710|4,715|-5,737|
|R9|Zona vecinal N°2 - 1|341.174|6.367.929|709|4,535|-6,119|
|R10|Zona vecinal N°2 - 2|341.170|6.368.002|708|4,532|-6,046|
|R11|Zona vecinal N°2 - 3|341.127|6.368.029|708|4,490|-6,018|
|R12|Zona vecinal N°2 - 4|341.128|6.368.092|708|4,492|-5,955|
|R13|Zona vecinal N°3 - 1|341.352|6.367.916|711|4,713|-6,135|
|R14|Zona vecinal N°3 - 2|341.455|6.367.931|712|4,816|-6,121|
|R15|Zona vecinal N°3 - 3|341.576|6.367.939|714|4,937|-6,115|
|R16|vecino N°4|341.344|6.368.548|709|4,715|-5,503|
|R17|zona vecinal N°5 - 1|340.872|6.367.770|707|4,230|-6,273|
|R18|zona vecinal N°5 - 2|340.854|6.367.891|707|4,214|-6,152|
|R19|zona vecinal N°5 - 3|340.835|6.368.043|706|4,198|-5,999|
|R20|zona vecinal N°5 - 4|340.541|6.368.010|703|3,903|-6,027|
|R21|zona vecinal N°5 - 5|340.596|6.367.764|706|3,954|-6,274|
|R22|zona vecinal N°5 - 6|340.762|6.367.698|707|4,119|-6,343|
|R23|zona vecinal que participó del<br>PAC - 1|340.128|6.367.859|703|3,488|-6,172|
|R24|zona vecinal que participó del<br>PAC - 2|339.927|6.367.952|710|3,289|-6,075|
|R25|zona vecinal que participó del<br>PAC - 3|339.863|6.368.062|711|3,226|-5,964|
|R26|zona vecinal que participó del<br>PAC - 4|339.749|6.367.738|719|3,107|-6,286|
|R27|zona vecinal que participó del<br>PAC - 5|339.764|6.367.928|716|3,125|-6,097|
|R28|Escuela Bucalemu|342.219|6.368.707|720|5,593|-5,358|
|R29|Iglesia de Jesucristo<br>Fundamento Apostólico|342.634|6.368.518|725|6,005|-5,554|
|R30|Otras Viviendas - 1|341.972|6.368.585|717|5,344|-5,476|
|R31|Otras Viviendas - 2|341.974|6.368.678|717|5,347|-5,383|

Estudio EM2023/200-54 | Ecoazul

72
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

|Receptor|Descripción|UTM (WGS 84 - Z18)|Col4|Altitud (1)<br>(m.s.n.m.)|LCC (km)|Col7|
|---|---|---|---|---|---|---|
|Receptor|Descripción|Este (m)|Norte (m)|Norte (m)|LCC-X|LCC-Y|
|R32|Otras Viviendas - 3|342.099|6.368.440|719|5,468|-5,623|
|R33|Otras Viviendas - 4|342.226|6.368.403|721|5,595|-5,662|
|R34|Otras Viviendas - 5|342.059|6.367.882|720|5,419|-6,180|
|R35|Otras Viviendas - 6|342.154|6.367.947|721|5,515|-6,117|
|R36|Otras Viviendas - 7|341.256|6.368.747|707|4,631|-5,302|

1: Altitud obtenida del terreno entregado por el modelo WRF en el formato CALMET, utilizada por CALPUFF.

Estudio EM2023/200-54 | Ecoazul

73
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

Figura 36: Ubicación de Receptores de interés alrededor del Proyecto.

Estudio EM2023/200-54 | Ecoazul

74
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

Figura 37: Ubicación de Receptores de interés alrededor del Proyecto - acercamiento al área del Proyecto.

Estudio EM2023/200-54 | Ecoazul

75
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

4.2.2 Implementación de Fuentes Emisoras de Contaminantes

La aplicación del modelo CALPUFF para el periodo meteorológico del año 2022
consideró los escenarios de emisiones de las fases de Construcción y Operación del
proyecto.

Las emisiones implementadas en CALPUFF se obtuvieron del Anexo Estimación de
Emisiones Atmosféricas. Estas emisiones distribuidas por fuentes se presentan en
Tabla 17 para los escenarios de Construcción y Operación. Para el escenario de
Construcción, las fuentes indicadas en esta tabla corresponden, por un lado, a
excavaciones y carguío de material, las que se implementaron en el modelo como fuente
de área ubicada en la zona de emplazamiento del Proyecto, de esta manera estos
procesos emisores fueron agrupados y definido utilizando polígonos para cubrir el área
abarcada por esta fuente. Por otro lado, para el transporte vehicular, las emisiones por
resuspensión y combustión de motores se implementaron a través de caminos,
considerando caminos No Pavimentados y Pavimentados.

En el caso del escenario de Operación, la fuente de generador eléctrico se implementó
en la zona de emplazamiento del Proyecto como un área. Las emisiones por
resuspensión y combustión de motores debido al transporte vehicular se
implementaron a través de caminos, también considerando caminos No Pavimentados
y Pavimentados. Finalmente, la fuente de calderas, corresponden a 2 calderas que se
implementaron como fuentes puntuales.

Tabla 17: Emisiones de MPS, MP10, MP2,5, NOx, SO 2 y CO de las fases de Construcción

y Operación del Proyecto Planta Depuradora de RILes Empresa San Lorenzo.

|Actividad|Col2|Emisión (t/año)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|Actividad|Actividad|MPS|MP10|MP2,5|NOx|SO2|CO|
|Construcción|Construcción|Construcción|Construcción|Construcción|Construcción|Construcción|Construcción|
|Movimientos<br>de tierra|Excavaciones|0,0214201|0,0043818|0,0022491||||
|Movimientos<br>de tierra|Carguío de material|0,0008567|0,0004052|0,0000614||||
|Resuspensión vías NO pavimentadas|Resuspensión vías NO pavimentadas|0,0082114|0,0007083|0,0000708||||
|Resuspensión vías pavimentadas|Resuspensión vías pavimentadas|0,0075561|0,0003395|0,0000821||||
|Emisiones de combustión vehicular|Emisiones de combustión vehicular|0,0000078|0,0000078|0,0000078|0,0003774|0,0000004|0,0000874|
|Total|Total|0,0380521|0,0058426|0,0024712|0,0003774|0,0000004|0,0000874|
|Operación|Operación|Operación|Operación|Operación|Operación|Operación|Operación|
|Resuspensión vías NO pavimentadas|Resuspensión vías NO pavimentadas|0,0417133|0,0127694|0,0012769||||
|Resuspensión vías pavimentadas|Resuspensión vías pavimentadas|0,1087893|0,0208822|0,0050521||||
|Emisiones de combustión vehicular|Emisiones de combustión vehicular|0,0005841|0,0005841|0,0005841|0,0285087|0,0000312|0,0064443|
|Generador|Generador|0,1239973|0,1239973|0,1239973|1,7639880|0,1159977|0,3799928|

Estudio EM2023/200-54 | Ecoazul

76
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

|Actividad|Emisión (t/año)|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|Actividad|MPS|MP10|MP2,5|NOx|SO2|CO|
|Calderas|0,0770008|0,0770008|0,0663064|0,1048220|0,0053482|0,1283160|
|Total|0,3520848|0,2352338|0,1972168|1,8973187|0,1213770|0,5147531|

Por otra parte, las emisiones de NO 2 se consideraron como el 10% del total de NOx y
como escenario de emisiones más conservador se consideraron en la modelación todas

las emisiones de SOx como SO 2 .

Las emisiones consideraron 1 año de periodo para cada fase de construcción y
operación. En el caso de las actividades del proyecto, como movimiento de tierra y
tránsito vehicular se consideró una jornada laboral de 9 a 18 horas, es decir 10 horas
diarias para cada fase (horas: 9, 10, 11, 12, 13, 14, 15, 16, 17 y 18) en ambas fases. No
se considera parar en la hora de almuerzo, más bien cambio de turnos.

Con respecto a las calderas y generadores eléctricos de la fase de operación, estas
emisiones se consideraron como continuas durante el año. Sin embargo, en el caso de
los generadores este es un escenario muy conservador, ya que en las emisiones de esta
fuente se consideraron 120 días de operación.

Las fuentes presentadas en Tabla 17 se implementaron en el modelo CALPUFF
considerando las coordenadas que se muestran en Tabla 18 y Tabla 19, en coordenadas
UTM y su correspondiente coordenada Lambert Conformal Conic (LCC), para las fases
de Construcción y Operación, respectivamente.

Tabla 18: Coordenadas de las áreas y tramos donde se implementaron las fuentes

emisoras de contaminantes atmosféricos en el modelo CALPUFF para la fase
de Construcción del Proyecto.

|Fuente|Superficie o<br>longitud|Punto|UTM (WGS 84 Z19)|Col5|LCC (km)|Col7|
|---|---|---|---|---|---|---|
|Fuente|Superficie o<br>longitud|Punto|Este (m)|Norte (m)|LCC-X|LCC-Y|
|Planta|1.812 m2|1|341.207|6.368.229|4,573|-5,820|
|Planta|1.812 m2|2|341.236|6.368.244|4,602|-5,805|
|Planta|1.812 m2|3|341.265|6.368.203|4,631|-5,846|
|Planta|1.812 m2|4|341.229|6.368.185|4,594|-5,863|
|Camino No<br>Pavimentado|64,1 m|1|341.305|6.368.173|4,670|-5,877|
|Camino No<br>Pavimentado|64,1 m|2|341.258|6.368.217|4,623|-5,833|
|Camino Pavimentado|13.794 m|1|341.308|6.368.174|4,673|-5,876|
|Camino Pavimentado|13.794 m|2|341.440|6.368.234|4,806|-5,819|
|Camino Pavimentado|13.794 m|2|339.290|6.372.613|2,728|-1,404|
|Camino Pavimentado|13.794 m|3|338.502|6.372.840|1,944|-1,164|

Estudio EM2023/200-54 | Ecoazul

77
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

|Fuente|Superficie o<br>longitud|Punto|UTM (WGS 84 Z19)|Col5|LCC (km)|Col7|
|---|---|---|---|---|---|---|
|Fuente|Superficie o<br>longitud|Punto|Este (m)|Norte (m)|LCC-X|LCC-Y|
|Fuente|Superficie o<br>longitud|3|338.237|6.373.073|1,683|-0,927|
|Fuente|Superficie o<br>longitud|4|337.505|6.373.567|0,960|-0,421|
|Fuente|Superficie o<br>longitud|5|337.429|6.373.849|0,888|-0,137|
|Fuente|Superficie o<br>longitud|6|337.349|6.374.211|0,813|0,226|
|Fuente|Superficie o<br>longitud|7|337.752|6.374.500|1,222|0,509|
|Fuente|Superficie o<br>longitud|8|338.072|6.375.628|1,561|1,631|
|Fuente|Superficie o<br>longitud|9|338.196|6.376.051|1,691|2,052|
|Fuente|Superficie o<br>longitud|10|338.711|6.375.938|2,204|1,930|
|Fuente|Superficie o<br>longitud|11|338.856|6.376.443|2,357|2,433|
|Fuente|Superficie o<br>longitud|12|338.822|6.376.483|2,324|2,474|
|Fuente|Superficie o<br>longitud|13|338.666|6.376.836|2,174|2,829|
|Fuente|Superficie o<br>longitud|14|338.527|6.377.326|2,043|3,321|
|Fuente|Superficie o<br>longitud|15|338.472|6.377.334|1,989|3,330|
|Fuente|Superficie o<br>longitud|16|338.482|6.377.429|2,000|3,425|
|Fuente|Superficie o<br>longitud|17|338.642|6.377.744|2,165|3,737|
|Fuente|Superficie o<br>longitud|18|338.737|6.378.004|2,264|3,996|
|Fuente|Superficie o<br>longitud|19|338.881|6.378.258|2,413|4,247|
|Fuente|Superficie o<br>longitud|20|338.896|6.378.291|2,428|4,280|
|Fuente|Superficie o<br>longitud|21|338.895|6.378.323|2,428|4,312|
|Fuente|Superficie o<br>longitud|22|338.830|6.378.556|2,366|4,546|
|Fuente|Superficie o<br>longitud|23|338.829|6.378.584|2,366|4,574|
|Fuente|Superficie o<br>longitud|24|338.842|6.378.604|2,379|4,594|
|Fuente|Superficie o<br>longitud|25|338.950|6.378.698|2,488|4,686|
|Fuente|Superficie o<br>longitud|26|338.965|6.378.769|2,505|4,757|
|Fuente|Superficie o<br>longitud|27|338.965|6.378.874|2,507|4,862|
|Fuente|Superficie o<br>longitud|28|338.937|6.379.056|2,482|5,045|
|Fuente|Superficie o<br>longitud|29|341.308|6.368.174|4,673|-5,876|
|Fuente|Superficie o<br>longitud|30|341.440|6.368.234|4,806|-5,819|

Tabla 19: Coordenadas de las áreas y tramos donde se implementaron las fuentes

emisoras de contaminantes atmosféricos en el modelo CALPUFF para la fase
de Operación del Proyecto.

|Fuente|Superficie o<br>longitud|Punto|UTM (WGS 84 Z19)|Col5|LCC (km)|Col7|
|---|---|---|---|---|---|---|
|Fuente|Superficie o<br>longitud|Punto|Este (m)|Norte (m)|LCC-X|LCC-Y|
|Planta|1.812 m2|1|341.207|6.368.229|4,573|-5,820|
|Planta|1.812 m2|2|341.236|6.368.244|4,602|-5,805|
|Planta|1.812 m2|3|341.265|6.368.203|4,631|-5,846|
|Planta|1.812 m2|4|341.229|6.368.185|4,594|-5,863|

Estudio EM2023/200-54 | Ecoazul

78
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

|Fuente|Superficie o<br>longitud|Punto|UTM (WGS 84 Z19)|Col5|LCC (km)|Col7|
|---|---|---|---|---|---|---|
|Fuente|Superficie o<br>longitud|Punto|Este (m)|Norte (m)|LCC-X|LCC-Y|
|Camino No<br>Pavimentado|64,1 m|1|341.305|6.368.173|4,670|-5,877|
|Camino No<br>Pavimentado|64,1 m|2|341.258|6.368.217|4,623|-5,833|
|Camino Pavimentado|13.794 m|1|341.308|6.368.174|4,673|-5,876|
|Camino Pavimentado|13.794 m|2|341.440|6.368.234|4,806|-5,819|
|Camino Pavimentado|13.794 m|2|339.290|6.372.613|2,728|-1,404|
|Camino Pavimentado|13.794 m|3|338.502|6.372.840|1,944|-1,164|
|Camino Pavimentado|13.794 m|3|338.237|6.373.073|1,683|-0,927|
|Camino Pavimentado|13.794 m|4|337.505|6.373.567|0,960|-0,421|
|Camino Pavimentado|13.794 m|5|337.429|6.373.849|0,888|-0,137|
|Camino Pavimentado|13.794 m|6|337.349|6.374.211|0,813|0,226|
|Camino Pavimentado|13.794 m|7|337.752|6.374.500|1,222|0,509|
|Camino Pavimentado|13.794 m|8|338.072|6.375.628|1,561|1,631|
|Camino Pavimentado|13.794 m|9|338.196|6.376.051|1,691|2,052|
|Camino Pavimentado|13.794 m|10|338.711|6.375.938|2,204|1,930|
|Camino Pavimentado|13.794 m|11|338.856|6.376.443|2,357|2,433|
|Camino Pavimentado|13.794 m|12|338.822|6.376.483|2,324|2,474|
|Camino Pavimentado|13.794 m|13|338.666|6.376.836|2,174|2,829|
|Camino Pavimentado|13.794 m|14|338.527|6.377.326|2,043|3,321|
|Camino Pavimentado|13.794 m|15|338.472|6.377.334|1,989|3,330|
|Camino Pavimentado|13.794 m|16|338.482|6.377.429|2,000|3,425|
|Camino Pavimentado|13.794 m|17|338.642|6.377.744|2,165|3,737|
|Camino Pavimentado|13.794 m|18|338.737|6.378.004|2,264|3,996|
|Camino Pavimentado|13.794 m|19|338.881|6.378.258|2,413|4,247|
|Camino Pavimentado|13.794 m|20|338.896|6.378.291|2,428|4,280|
|Camino Pavimentado|13.794 m|21|338.895|6.378.323|2,428|4,312|
|Camino Pavimentado|13.794 m|22|338.830|6.378.556|2,366|4,546|
|Camino Pavimentado|13.794 m|23|338.829|6.378.584|2,366|4,574|
|Camino Pavimentado|13.794 m|24|338.842|6.378.604|2,379|4,594|
|Camino Pavimentado|13.794 m|25|338.950|6.378.698|2,488|4,686|
|Camino Pavimentado|13.794 m|26|338.965|6.378.769|2,505|4,757|
|Camino Pavimentado|13.794 m|27|338.965|6.378.874|2,507|4,862|
|Camino Pavimentado|13.794 m|28|338.937|6.379.056|2,482|5,045|
|Camino Pavimentado|13.794 m|29|341.308|6.368.174|4,673|-5,876|
|Camino Pavimentado|13.794 m|30|341.440|6.368.234|4,806|-5,819|
|Camino Pavimentado<br>KDM|64.476 m|1|341.435|6.368.243|4,801|-5,809|
|Camino Pavimentado<br>KDM|64.476 m|2|340.341|6.370.448|3,744|-3,586|
|Camino Pavimentado<br>KDM|64.476 m|3|339.312|6.372.591|2,750|-1,427|
|Camino Pavimentado<br>KDM|64.476 m|4|339.746|6.372.495|3,183|-1,529|
|Camino Pavimentado<br>KDM|64.476 m|5|339.903|6.372.404|3,338|-1,624|

Estudio EM2023/200-54 | Ecoazul

79
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

|Fuente|Superficie o<br>longitud|Punto|UTM (WGS 84 Z19)|Col5|LCC (km)|Col7|
|---|---|---|---|---|---|---|
|Fuente|Superficie o<br>longitud|Punto|Este (m)|Norte (m)|LCC-X|LCC-Y|
|Fuente|Superficie o<br>longitud|6|340.092|6.373.126|3,539|-0,905|
|Fuente|Superficie o<br>longitud|7|339.935|6.373.168|3,383|-0,860|
|Fuente|Superficie o<br>longitud|8|339.758|6.373.173|3,206|-0,852|
|Fuente|Superficie o<br>longitud|9|338.554|6.373.635|2,010|-0,370|
|Fuente|Superficie o<br>longitud|10|338.160|6.373.583|1,615|-0,415|
|Fuente|Superficie o<br>longitud|11|337.910|6.373.661|1,366|-0,333|
|Fuente|Superficie o<br>longitud|12|337.726|6.373.796|1,184|-0,195|
|Fuente|Superficie o<br>longitud|13|337.265|6.374.428|0,733|0,444|
|Fuente|Superficie o<br>longitud|14|337.135|6.374.654|0,608|0,673|
|Fuente|Superficie o<br>longitud|15|336.946|6.374.795|0,421|0,816|
|Fuente|Superficie o<br>longitud|16|336.417|6.375.594|-0,095|1,624|
|Fuente|Superficie o<br>longitud|17|335.492|6.376.508|-1,005|2,554|
|Fuente|Superficie o<br>longitud|18|335.298|6.376.593|-1,198|2,641|
|Fuente|Superficie o<br>longitud|19|335.135|6.376.587|-1,360|2,638|
|Fuente|Superficie o<br>longitud|20|334.651|6.376.431|-1,847|2,491|
|Fuente|Superficie o<br>longitud|21|333.646|6.376.616|-2,849|2,692|
|Fuente|Superficie o<br>longitud|22|332.865|6.376.391|-3,634|2,479|
|Fuente|Superficie o<br>longitud|23|332.050|6.375.788|-4,459|1,890|
|Fuente|Superficie o<br>longitud|24|331.690|6.375.582|-4,822|1,690|
|Fuente|Superficie o<br>longitud|25|331.401|6.375.211|-5,117|1,323|
|Fuente|Superficie o<br>longitud|26|331.166|6.375.001|-5,356|1,118|
|Fuente|Superficie o<br>longitud|27|330.437|6.374.861|-6,087|0,990|
|Fuente|Superficie o<br>longitud|28|329.612|6.374.349|-6,920|0,492|
|Fuente|Superficie o<br>longitud|29|329.278|6.374.222|-7,256|0,370|
|Fuente|Superficie o<br>longitud|30|328.416|6.373.604|-8,128|-0,234|
|Fuente|Superficie o<br>longitud|31|328.040|6.373.493|-8,506|-0,339|
|Fuente|Superficie o<br>longitud|32|327.728|6.373.138|-8,824|-0,689|
|Fuente|Superficie o<br>longitud|33|326.603|6.372.423|-9,961|-1,384|
|Fuente|Superficie o<br>longitud|34|326.245|6.372.161|-10,323|-1,641|
|Fuente|Superficie o<br>longitud|35|326.067|6.371.870|-10,505|-1,929|
|Fuente|Superficie o<br>longitud|36|325.060|6.370.830|-11,529|-2,952|
|Fuente|Superficie o<br>longitud|37|324.458|6.370.587|-12,135|-3,185|
|Fuente|Superficie o<br>longitud|38|323.967|6.370.268|-12,632|-3,496|
|Fuente|Superficie o<br>longitud|39|322.321|6.369.603|-14,288|-4,134|
|Fuente|Superficie o<br>longitud|40|321.138|6.369.346|-15,476|-4,371|
|Fuente|Superficie o<br>longitud|41|319.996|6.368.346|-16,634|-5,352|
|Fuente|Superficie o<br>longitud|42|319.831|6.368.217|-16,801|-5,479|
|Fuente|Superficie o<br>longitud|43|319.526|6.368.199|-17,107|-5,492|
|Fuente|Superficie o<br>longitud|44|319.120|6.368.314|-17,511|-5,370|

Estudio EM2023/200-54 | Ecoazul

80
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

|Fuente|Superficie o<br>longitud|Punto|UTM (WGS 84 Z19)|Col5|LCC (km)|Col7|
|---|---|---|---|---|---|---|
|Fuente|Superficie o<br>longitud|Punto|Este (m)|Norte (m)|LCC-X|LCC-Y|
|Fuente|Superficie o<br>longitud|45|317.572|6.368.754|-19,051|-4,904|
|Fuente|Superficie o<br>longitud|46|317.346|6.368.672|-19,278|-4,983|
|Fuente|Superficie o<br>longitud|47|316.642|6.368.148|-19,991|-5,495|
|Fuente|Superficie o<br>longitud|48|315.478|6.367.637|-21,163|-5,986|
|Fuente|Superficie o<br>longitud|49|315.325|6.367.494|-21,318|-6,127|
|Fuente|Superficie o<br>longitud|50|315.148|6.366.721|-21,508|-6,897|
|Fuente|Superficie o<br>longitud|51|315.012|6.365.702|-21,661|-7,914|
|Fuente|Superficie o<br>longitud|52|314.651|6.365.345|-22,028|-8,265|
|Fuente|Superficie o<br>longitud|53|314.462|6.364.840|-22,225|-8,766|
|Fuente|Superficie o<br>longitud|54|314.231|6.364.141|-22,468|-9,461|
|Fuente|Superficie o<br>longitud|55|314.353|6.364.170|-22,345|-9,434|
|Fuente|Superficie o<br>longitud|56|318.015|6.363.584|-18,693|-10,081|
|Fuente|Superficie o<br>longitud|57|319.947|6.363.271|-16,767|-10,426|
|Fuente|Superficie o<br>longitud|58|323.116|6.363.575|-13,593|-10,174|
|Fuente|Superficie o<br>longitud|59|324.282|6.363.674|-12,426|-10,094|
|Fuente|Superficie o<br>longitud|60|325.122|6.363.359|-11,591|-10,423|
|Fuente|Superficie o<br>longitud|61|325.538|6.363.419|-11,174|-10,370|
|Fuente|Superficie o<br>longitud|62|325.999|6.363.295|-10,715|-10,502|
|Fuente|Superficie o<br>longitud|63|326.207|6.362.958|-10,512|-10,842|
|Fuente|Superficie o<br>longitud|64|326.295|6.362.162|-10,438|-11,640|
|Fuente|Superficie o<br>longitud|65|326.558|6.362.005|-10,178|-11,801|
|Fuente|Superficie o<br>longitud|66|326.834|6.362.028|-9,901|-11,782|
|Fuente|Superficie o<br>longitud|67|327.059|6.361.791|-9,681|-12,023|
|Fuente|Superficie o<br>longitud|68|327.491|6.361.072|-9,260|-12,749|
|Fuente|Superficie o<br>longitud|69|328.181|6.360.245|-8,583|-13,587|
|Fuente|Superficie o<br>longitud|70|329.716|6.359.145|-7,068|-14,713|
|Fuente|Superficie o<br>longitud|71|330.576|6.357.326|-6,238|-16,546|
|Fuente|Superficie o<br>longitud|72|330.600|6.356.606|-6,225|-17,266|
|Fuente|Superficie o<br>longitud|73|330.592|6.355.869|-6,245|-18,003|
|Fuente|Superficie o<br>longitud|74|330.559|6.354.802|-6,296|-19,069|
|Fuente|Superficie o<br>longitud|75|330.418|6.354.331|-6,445|-19,538|
|Fuente|Superficie o<br>longitud|76|330.100|6.353.075|-6,784|-20,788|
|Fuente|Superficie o<br>longitud|77|329.674|6.352.132|-7,226|-21,724|
|Chimenea caldera 2 (fuente puntual)|Chimenea caldera 2 (fuente puntual)|Chimenea caldera 2 (fuente puntual)|341.294|6.368.087|4,6577|-5,9628|
|chimenea caldera 3 (fuente puntual)|chimenea caldera 3 (fuente puntual)|chimenea caldera 3 (fuente puntual)|341.304|6.368.091|4,6678|-5,9590|

El detalle de la distribución de las fuentes de área y caminos del Proyecto se ilustran en
Figura 38 y Figura 39 para la fase de Construcción y Figura 40 y Figura 41 para la fase
de Operación. En las primeras figuras se muestran las fuentes consideradas en Google

Estudio EM2023/200-54 | Ecoazul

81
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

Earth, y en las segundas se muestran las fuentes implementadas en el modelo CALPUFF
en coordenadas Lambert Conformal Conic (LCC).

Estudio EM2023/200-54 | Ecoazul

82
“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo”

Informe Final

Figura 38: Fuentes emisoras de la fase de Construcción del proyecto Planta Depuradora de RILes Empresa San

Lorenzo. Fuentes en Google Earth.

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 83

Informe Final

Figura 39: Distribución de fuentes emisoras de la fase de Construcción del proyecto Planta Depuradora de RILes

Empresa San Lorenzo. Fuentes implementadas en CALPUFF, en coordenadas LCC.

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 84

Informe Final

Figura 40: Fuentes emisoras de la fase de Operación del proyecto Planta Depuradora de RILes Empresa San Lorenzo.

Fuentes en Google Earth.

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 85

Informe Final

Figura 41: Distribución de fuentes emisoras de la fase de Operación del proyecto Planta Depuradora de RILes Empresa

San Lorenzo. Fuentes implementadas en CALPUFF, en coordenadas LCC.

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 86

Informe Final

## 4.3 Resultados de la Aplicación del Sistema CALPUFF

En esta sección se presentan los resultados del sistema de modelación CALPUFF,
considerando el año meteorológico 2022 y el escenario de emisión de las fases de
Construcción y Operación del proyecto Planta Depuradora de RILes Empresa San
Lorenzo. Es importante volver a mencionar que los resultados presentados a
continuación consideran el peor escenario de emisiones.

Los resultados obtenidos se presentan para cada contaminante estimando la
estadística considerada en el marco jurídico vigente en Chile presentando en sección
2.4.2 para los receptores presentados en Tabla 16 y como isolíneas de concentraciones
de contaminantes en el dominio de modelación.

A continuación, se presentan los resultados en la calidad del aire de la zona de estudio
para cada uno de los escenarios y contaminantes considerados.

4.3.1 Escenario de Construcción

Resultados de Material Particulado Respirable (MP10)

Los resultados de MP10 promedio anual y percentil 98 de las concentraciones de 24
horas modelados con CALPUFF en los receptores de interés para la fase de
Construcción del Proyecto se presentan en Tabla 20. Como se observa en esta tabla, el
mayor aporte del proyecto como promedio anual es en el receptor 8 con 0,01 μg/Nm [3], y
como percentil 98 de las concentraciones 24 horas en el receptor 12 con 0,07 μg/Nm [3] .
Esto alcanza a menos de 1% de la norma anual y diaria correspondiente.

Tabla 20: Resultados de MP10 promedio anual y percentil 98 de las concentraciones

diarias modeladas por el sistema CALPUFF, Escenario fase de Construcción.

|Receptor|Concentración de MP10 (μg/m3)|Col3|
|---|---|---|
|Receptor|Promedio anual|Percentil 98 de las conc. 24 horas|
|R1|0,00|0,00|
|R2|0,00|0,00|
|R3|0,00|0,00|
|R4|0,00|0,00|
|R5|0,00|0,00|
|R6|0,00|0,00|

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 87

Informe Final

|Receptor|Concentración de MP10 (μg/m3)|Col3|
|---|---|---|
|Receptor|Promedio anual|Percentil 98 de las conc. 24 horas|
|R7|0,00|0,00|
|R8|0,01|0,04|
|R9|0,01|0,04|
|R10|0,01|0,05|
|R11|0,01|0,06|
|R12|0,01|0,07|
|R13|0,01|0,05|
|R14|0,00|0,03|
|R15|0,00|0,02|
|R16|0,00|0,02|
|R17|0,00|0,02|
|R18|0,00|0,02|
|R19|0,00|0,02|
|R20|0,00|0,01|
|R21|0,00|0,01|
|R22|0,00|0,01|
|R23|0,00|0,00|
|R24|0,00|0,00|
|R25|0,00|0,00|
|R26|0,00|0,00|
|R27|0,00|0,00|
|R28|0,00|0,00|
|R29|0,00|0,00|
|R30|0,00|0,01|
|R31|0,00|0,01|
|R32|0,00|0,01|
|R33|0,00|0,01|
|R34|0,00|0,01|
|R35|0,00|0,01|
|R36|0,00|0,01|

Estos resultados se muestran también como isolíneas de concentraciones promedio
anual y percentil 98 de las concentraciones de 24 horas de MP10 de la fase de
Construcción en Figura 42 y Figura 43, respectivamente.

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 88

Informe Final

Figura 42: Isolíneas de concentraciones promedio anual de MP10 en la zona de estudio. Escenario meteorología año

2022 y escenario de emisiones fase de Construcción.

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 89

Informe Final

Figura 43: Isolíneas de percentiles 98 de concentraciones de 24 horas de MP10 primario en la zona de estudio.

Escenario meteorología año 2022 y escenario de emisiones fase de Construcción.

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 90

Informe Final

Resultados de Material Particulado Fino Respirable (MP2,5)

Los resultados de MP2,5 promedio anual y percentil 98 de las concentraciones de 24
horas modelados con CALPUFF en los receptores de interés para la fase de
Construcción del Proyecto se presentan en Tabla 21. Como se observa en esta tabla, el
mayor aporte del proyecto como promedio anual es en el receptor 8 con 0,005 μg/Nm [3],
y como percentil 98 de las concentraciones 24 horas en el receptor 12 con 0,03 μg/Nm [3] .
Esto alcanza a menos de 1% de la norma anual y diaria correspondiente.

Tabla 21: Resultados de MP2,5 promedio anual y percentil 98 de las concentraciones

diarias modeladas por el sistema CALPUFF, Escenario fase de Construcción.

|Receptor|Concentración de MP2,5 (μg/m3)|Col3|
|---|---|---|
|Receptor|Promedio anual|Percentil 98 de las conc. 24 horas|
|R1|0,00|0,00|
|R2|0,00|0,00|
|R3|0,00|0,00|
|R4|0,00|0,00|
|R5|0,00|0,00|
|R6|0,00|0,00|
|R7|0,00|0,00|
|R8|0,00|0,02|
|R9|0,00|0,02|
|R10|0,00|0,02|
|R11|0,00|0,03|
|R12|0,00|0,03|
|R13|0,00|0,02|
|R14|0,00|0,01|
|R15|0,00|0,01|
|R16|0,00|0,01|
|R17|0,00|0,01|
|R18|0,00|0,01|
|R19|0,00|0,01|
|R20|0,00|0,00|
|R21|0,00|0,00|
|R22|0,00|0,00|
|R23|0,00|0,00|

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 91

Informe Final

|Receptor|Concentración de MP2,5 (μg/m3)|Col3|
|---|---|---|
|Receptor|Promedio anual|Percentil 98 de las conc. 24 horas|
|R24|0,00|0,00|
|R25|0,00|0,00|
|R26|0,00|0,00|
|R27|0,00|0,00|
|R28|0,00|0,00|
|R29|0,00|0,00|
|R30|0,00|0,00|
|R31|0,00|0,00|
|R32|0,00|0,00|
|R33|0,00|0,00|
|R34|0,00|0,00|
|R35|0,00|0,00|
|R36|0,00|0,00|

Estos resultados se muestran también como isolíneas de concentración promedio anual
y percentil 98 de las concentraciones de 24 horas de MP2,5 de la fase de Construcción
del Proyecto en Figura 44 y Figura 45, respectivamente.

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 92

Informe Final

Figura 44: Isolíneas de concentraciones promedio anual de MP2,5 en la zona de estudio. Escenario meteorología año

2022 y escenario de emisiones fase de Construcción.

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 93

Informe Final

Figura 45: Isolíneas de percentiles 98 de concentraciones de 24 horas de MP2,5 primario en la zona de estudio.

Escenario meteorología año 2022 y escenario de emisiones fase de Construcción.

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 94

Informe Final

Resultados de Material Particulado Sedimentable (MPS)

Los resultados de MPS promedio anual modelados con CALPUFF en los receptores de
interés para la fase de Construcción del Proyecto se presentan en Tabla 22. Como se

 observa en esta tabla, el mayor aporte del proyecto es en el receptor 8 con 0,13 mg/m [2]
día como promedio anual. Esto es inferior a 1% de la norma de referencia.

Tabla 22: Resultados de MPS promedio anual modelados por el sistema CALPUFF,

Escenario fase de Construcción.

|Receptor|Concentración de MPS (mg/m2-día)|
|---|---|
|Receptor|Promedio anual|
|R1|0,00|
|R2|0,00|
|R3|0,00|
|R4|0,00|
|R5|0,00|
|R6|0,00|
|R7|0,00|
|R8|0,13|
|R9|0,04|
|R10|0,05|
|R11|0,04|
|R12|0,05|
|R13|0,06|
|R14|0,02|
|R15|0,01|
|R16|0,02|
|R17|0,01|
|R18|0,01|
|R19|0,01|
|R20|0,00|
|R21|0,00|
|R22|0,00|
|R23|0,00|
|R24|0,00|

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 95

Informe Final

|Receptor|Concentración de MPS (mg/m2-día)|
|---|---|
|Receptor|Promedio anual|
|R25|0,00|
|R26|0,00|
|R27|0,00|
|R28|0,00|
|R29|0,00|
|R30|0,00|
|R31|0,01|
|R32|0,00|
|R33|0,00|
|R34|0,00|
|R35|0,00|
|R36|0,01|

Estos resultados se muestran también como isolíneas de concentraciones promedio
anual de MPS de la fase de Construcción del Proyecto en Figura 46.

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 96

Informe Final

Figura 46: Isolíneas de concentraciones promedio anual de MPS en la zona de estudio. Escenario meteorología año

2022 y escenario de emisiones etapa de Construcción.

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 97

Informe Final

- Resultados de Dióxido de Nitrógeno (NO 2 )

Los resultados de NO 2, promedio anual y percentil 99 de las máximas diarias
concentraciones horarias modelados con CALPUFF en los receptores de interés para la
fase de Construcción del Proyecto se presentan en Tabla 23. Como se observa en esta
tabla, los aportes de este contaminante como promedio anual y percentil 99 de las
concentraciones horarias son muy bajas y no alcanza a 1% de la norma respectiva.

Tabla 23: Resultados de NO 2 promedio anual y percentil 99 de las máximas diarias

concentraciones horarias modeladas por el sistema CALPUFF, Escenario fase
de Construcción.

|Receptor|Concentración de NO (μg/m3)<br>2|Col3|
|---|---|---|
|Receptor|Promedio anual|Percentil 99 de las conc. 1 hora|
|R1|0,00|0,00|
|R2|0,00|0,00|
|R3|0,00|0,00|
|R4|0,00|0,00|
|R5|0,00|0,00|
|R6|0,00|0,00|
|R7|0,00|0,00|
|R8|0,00|0,00|
|R9|0,00|0,00|
|R10|0,00|0,00|
|R11|0,00|0,00|
|R12|0,00|0,00|
|R13|0,00|0,00|
|R14|0,00|0,00|
|R15|0,00|0,00|
|R16|0,00|0,00|
|R17|0,00|0,00|
|R18|0,00|0,00|
|R19|0,00|0,00|
|R20|0,00|0,00|
|R21|0,00|0,00|
|R22|0,00|0,00|
|R23|0,00|0,00|

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 98

Informe Final

|Receptor|Concentración de NO (μg/m3)<br>2|Col3|
|---|---|---|
|Receptor|Promedio anual|Percentil 99 de las conc. 1 hora|
|R24|0,00|0,00|
|R25|0,00|0,00|
|R26|0,00|0,00|
|R27|0,00|0,00|
|R28|0,00|0,00|
|R29|0,00|0,00|
|R30|0,00|0,00|
|R31|0,00|0,00|
|R32|0,00|0,00|
|R33|0,00|0,00|
|R34|0,00|0,00|
|R35|0,00|0,00|
|R36|0,00|0,00|

Estos resultados se presentan también como isolíneas de concentración promedio
anual y Percentil 99 de las concentraciones horarias de NO 2 de la fase de Construcción
en Figura 47 y Figura 48, respectivamente.

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 99

Informe Final

Figura 47: Isolíneas de concentraciones promedio anual de NO 2 en la zona de estudio. Escenario meteorología año

2022 y escenario de emisiones fase de Construcción.

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 100

Informe Final

Figura 48: Isolíneas de percentiles 99 de concentraciones de 1 hora de NO 2 en la zona de estudio. Escenario

meteorología año 2022 y escenario de emisiones fase de Construcción.

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 101

Informe Final

- Resultados de Dióxido de Azufre (SO 2 )

Los resultados de SO 2, percentil 98,5 de las concentraciones de 1 hora, percentiles 99 y
99,7 de las concentraciones diarias y percentil 99,73 de las concentraciones de 1 hora
de SO 2, en los receptores de interés modelados con CALPUFF para la etapa de
Construcción del Proyecto se presentan en Tabla 24. Como se observa en esta tabla, los
aportes de este contaminante como promedio anual, percentil 99 de las
concentraciones 24 horas y percentil 98,5 de las concentraciones de 1 hora son muy
bajas y no alcanza a 1% de la norma respectiva.

Tabla 24: Resultados de SO 2 promedio anual, percentil 99 de las concentraciones

diarias y percentil 98,5 máximas concentraciones horarias modeladas por el
sistema CALPUFF, Escenario fase de Construcción.

|Receptor|Concentración de SO (μg/m3)<br>2|Col3|Col4|
|---|---|---|---|
|Receptor|Promedio anual|Perc. 99 de las conc. 24 hr|Perc. 98,5 de las conc. 1 hr|
|R1|0,00|0,00|0,00|
|R2|0,00|0,00|0,00|
|R3|0,00|0,00|0,00|
|R4|0,00|0,00|0,00|
|R5|0,00|0,00|0,00|
|R6|0,00|0,00|0,00|
|R7|0,00|0,00|0,00|
|R8|0,00|0,00|0,00|
|R9|0,00|0,00|0,00|
|R10|0,00|0,00|0,00|
|R11|0,00|0,00|0,00|
|R12|0,00|0,00|0,00|
|R13|0,00|0,00|0,00|
|R14|0,00|0,00|0,00|
|R15|0,00|0,00|0,00|
|R16|0,00|0,00|0,00|
|R17|0,00|0,00|0,00|
|R18|0,00|0,00|0,00|
|R19|0,00|0,00|0,00|
|R20|0,00|0,00|0,00|
|R21|0,00|0,00|0,00|

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 102

Informe Final

|R22|0,00|0,00|0,00|
|---|---|---|---|
|R23|0,00|0,00|0,00|
|R24|0,00|0,00|0,00|
|R25|0,00|0,00|0,00|
|R26|0,00|0,00|0,00|
|R27|0,00|0,00|0,00|
|R28|0,00|0,00|0,00|
|R29|0,00|0,00|0,00|
|R30|0,00|0,00|0,00|
|R31|0,00|0,00|0,00|
|R32|0,00|0,00|0,00|
|R33|0,00|0,00|0,00|
|R34|0,00|0,00|0,00|
|R35|0,00|0,00|0,00|
|R36|0,00|0,00|0,00|

Los resultados de SO 2 modelados con CALPUFF también se presentan como isolíneas
de promedio anual, percentil 98,5 de las concentraciones de 1 hora y percentiles 99 de
las concentraciones de 1 hora de SO 2 de la fase de Construcción en Figura 49 a Figura
51, respectivamente.

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 103

Informe Final

Figura 49: Isolíneas de concentraciones promedio anual de SO 2 en la zona de estudio. Escenario meteorología año

2022 y escenario de emisiones fase de Construcción.

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 104

Informe Final

Figura 50: Isolíneas de Percentil 99 de las concentraciones de 24 horas de SO 2 en la zona de estudio. Escenario

meteorología año 2022 y escenario de emisiones fase de Construcción.

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 105

Informe Final

Figura 51: Isolíneas de Percentil 98,5 de las concentraciones de 1 hora de SO 2 en la zona de estudio. Escenario

meteorología año 2022 y escenario de emisiones fase de Construcción.

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 106

Informe Final

Resultados de Monóxido de Carbono (CO)

Los resultados de CO, percentiles 99 de las máximas diarias concentraciones de 8 y 1
horas, en los receptores de interés modelados con CALPUFF para la fase de
Construcción del Proyecto se presentan en Tabla 25. En esta tabla se observa que el
aporte del proyecto de CO en todos los receptores es bajo y no alcanza a 1% de la norma
respectiva.

Tabla 25: Resultados de CO percentil 99 de las máximas diarias concentraciones de 8

y 1 horas modeladas por el sistema CALPUFF, Escenario fase de
Construcción.

|Receptor|Concentración de CO (μg/m3)|Col3|
|---|---|---|
|Receptor|Percentil 99 de las conc. 8 horas|Percentil 99 de las conc. 1 hora|
|R1|0,00|0,00|
|R2|0,00|0,00|
|R3|0,00|0,00|
|R4|0,00|0,00|
|R5|0,00|0,00|
|R6|0,00|0,00|
|R7|0,00|0,00|
|R8|0,00|0,00|
|R9|0,00|0,00|
|R10|0,00|0,00|
|R11|0,00|0,00|
|R12|0,00|0,00|
|R13|0,00|0,00|
|R14|0,00|0,00|
|R15|0,00|0,00|
|R16|0,00|0,00|
|R17|0,00|0,00|
|R18|0,00|0,00|
|R19|0,00|0,00|
|R20|0,00|0,00|
|R21|0,00|0,00|
|R22|0,00|0,00|

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 107

Informe Final

|Receptor|Concentración de CO (μg/m3)|Col3|
|---|---|---|
|Receptor|Percentil 99 de las conc. 8 horas|Percentil 99 de las conc. 1 hora|
|R23|0,00|0,00|
|R24|0,00|0,00|
|R25|0,00|0,00|
|R26|0,00|0,00|
|R27|0,00|0,00|
|R28|0,00|0,00|
|R29|0,00|0,00|
|R30|0,00|0,00|
|R31|0,00|0,00|
|R32|0,00|0,00|
|R33|0,00|0,00|
|R34|0,00|0,00|
|R35|0,00|0,00|
|R36|0,00|0,00|

Estos resultados se presentan también como isolíneas de Percentil 99 de los máximos
diarios de las concentraciones de 8 horas y de 1 hora de CO de la fase de Construcción
en Figura 52 y Figura 53.

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 108

Informe Final

Figura 52: Isolíneas de Percentil 99 de los máximos diarios de las concentraciones de 8 horas de CO en la zona de

estudio. Escenario meteorología año 2022 y escenario de emisiones fase de Construcción.

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 109

Informe Final

Figura 53: Isolíneas de Percentil 99 de los máximos diarios de las concentraciones de 1 hora de CO en la zona de

estudio. Escenario meteorología año 2022 y escenario de emisiones fase de Construcción.

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 110

Informe Final

4.3.2 Escenario de Operación

Resultados de Material Particulado Respirable (MP10)

Los resultados de MP10 promedio anual y percentil 98 de las concentraciones de 24
horas modelados con CALPUFF en los receptores de interés para la fase de Operación
del Proyecto se presentan en Tabla 26. Como se observa en esta tabla, el mayor aporte
del proyecto como promedio anual es en el receptor 8 con 2,28 μg/Nm [3], y como percentil
98 de las concentraciones 24 horas en el receptor 12 con 5,08 μg/Nm [3] . Esto alcanza a
5 y 4% de la norma anual y diaria correspondiente, respectivamente.

Tabla 26: Resultados de MP10 promedio anual y percentil 98 de las concentraciones

diarias modeladas por el sistema CALPUFF, Escenario fase de Operación.

|Receptor|Concentración de MP10 (μg/m3)|Col3|
|---|---|---|
|Receptor|Promedio anual|Percentil 98 de las conc. 24 horas|
|R1|0,00|0,01|
|R2|0,00|0,00|
|R3|0,01|0,05|
|R4|0,03|0,08|
|R5|0,02|0,06|
|R6|0,02|0,07|
|R7|0,03|0,09|
|R8|2,28|4,71|
|R9|1,51|3,46|
|R10|1,65|3,96|
|R11|1,67|3,95|
|R12|1,90|5,08|
|R13|1,81|3,86|
|R14|1,38|3,30|
|R15|1,23|3,17|
|R16|1,17|2,68|
|R17|0,57|1,53|
|R18|0,68|1,85|
|R19|0,70|1,69|
|R20|0,24|0,65|

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 111

Informe Final

|Receptor|Concentración de MP10 (μg/m3)|Col3|
|---|---|---|
|Receptor|Promedio anual|Percentil 98 de las conc. 24 horas|
|R21|0,28|0,81|
|R22|0,40|1,07|
|R23|0,09|0,20|
|R24|0,10|0,23|
|R25|0,09|0,24|
|R26|0,07|0,17|
|R27|0,08|0,19|
|R28|0,24|0,70|
|R29|0,13|0,47|
|R30|0,52|1,42|
|R31|0,46|1,29|
|R32|0,43|1,28|
|R33|0,32|1,03|
|R34|0,46|1,42|
|R35|0,39|1,25|
|R36|0,57|1,30|

Estos resultados se muestran también como isolíneas de concentraciones promedio
anual y percentil 98 de las concentraciones de 24 horas de MP10 de la fase de Operación
en Figura 54 y Figura 55, respectivamente.

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 112

Informe Final

Figura 54: Isolíneas de concentraciones promedio anual de MP10 en la zona de estudio. Escenario meteorología año

2022 y escenario de emisiones fase de Operación.

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 113

Informe Final

Figura 55: Isolíneas de percentiles 98 de concentraciones de 24 horas de MP10 primario en la zona de estudio.

Escenario meteorología año 2022 y escenario de emisiones fase de Operación.

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 114

Informe Final

Resultados de Material Particulado Fino Respirable (MP2,5)

Los resultados de MP2,5 promedio anual y percentil 98 de las concentraciones de 24
horas modelados con CALPUFF en los receptores de interés para la fase de Operación
del Proyecto se presentan en Tabla 27. Como se observa en esta tabla, el mayor aporte
del proyecto como promedio anual es en el receptor 8 con 2,24 μg/Nm [3], y como percentil
98 de las concentraciones 24 horas en el receptor 12 con 5,07 μg/Nm [3] . Esto alcanza a
menos de 11 y 10% de la norma anual y diaria correspondiente, respectivamente.

Tabla 27: Resultados de MP2,5 promedio anual y percentil 98 de las concentraciones

diarias modeladas por el sistema CALPUFF, Escenario fase de Operación.

|Receptor|Concentración de MP2,5 (μg/m3)|Col3|
|---|---|---|
|Receptor|Promedio anual|Percentil 98 de las conc. 24 horas|
|R1|0,00|0,01|
|R2|0,00|0,00|
|R3|0,01|0,04|
|R4|0,03|0,07|
|R5|0,02|0,05|
|R6|0,02|0,06|
|R7|0,03|0,08|
|R8|2,24|4,69|
|R9|1,48|3,41|
|R10|1,62|3,86|
|R11|1,64|3,82|
|R12|1,86|5,07|
|R13|1,73|3,74|
|R14|1,36|3,29|
|R15|1,22|3,17|
|R16|1,15|2,68|
|R17|0,56|1,46|
|R18|0,67|1,81|
|R19|0,68|1,68|
|R20|0,23|0,65|
|R21|0,27|0,79|
|R22|0,39|1,05|
|R23|0,08|0,19|

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 115

Informe Final

|Receptor|Concentración de MP2,5 (μg/m3)|Col3|
|---|---|---|
|Receptor|Promedio anual|Percentil 98 de las conc. 24 horas|
|R24|0,09|0,23|
|R25|0,09|0,23|
|R26|0,06|0,16|
|R27|0,07|0,18|
|R28|0,24|0,69|
|R29|0,13|0,47|
|R30|0,50|1,40|
|R31|0,45|1,27|
|R32|0,42|1,25|
|R33|0,31|1,03|
|R34|0,46|1,42|
|R35|0,39|1,23|
|R36|0,56|1,29|

Estos resultados se muestran también como isolíneas de concentración promedio anual
y percentil 98 de las concentraciones de 24 horas de MP2,5 de la fase de Operación del
Proyecto en Figura 56 y Figura 57, respectivamente.

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 116

Informe Final

Figura 56: Isolíneas de concentraciones promedio anual de MP2,5 en la zona de estudio. Escenario meteorología año

2022 y escenario de emisiones fase de Operación.

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 117

Informe Final

Figura 57: Isolíneas de percentiles 98 de concentraciones de 24 horas de MP2,5 primario en la zona de estudio.

Escenario meteorología año 2022 y escenario de emisiones fase de Operación.

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 118

Informe Final

Resultados de Material Particulado Sedimentable (MPS)

Los resultados de MPS promedio anual modelados con CALPUFF en los receptores de
interés para la fase de Operación del Proyecto se presentan en Tabla 28. Como se

 observa en esta tabla, el mayor aporte del proyecto es en el receptor 8 con 2,52 mg/m [2]
día como promedio anual. Esto alcanza a 1% de la norma de referencia.

Tabla 28: Resultados de MPS promedio anual modelados por el sistema CALPUFF,

Escenario fase de Operación.

|Receptor|Concentración de MPS (mg/m2-día)|
|---|---|
|Receptor|Promedio anual|
|R1|0,00|
|R2|0,00|
|R3|0,01|
|R4|0,02|
|R5|0,02|
|R6|0,02|
|R7|0,03|
|R8|2,52|
|R9|1,34|
|R10|1,44|
|R11|1,40|
|R12|1,63|
|R13|2,14|
|R14|1,11|
|R15|0,83|
|R16|0,91|
|R17|0,37|
|R18|0,45|
|R19|0,44|
|R20|0,12|
|R21|0,14|
|R22|0,23|
|R23|0,03|
|R24|0,03|

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 119

Informe Final

|Receptor|Concentración de MPS (mg/m2-día)|
|---|---|
|Receptor|Promedio anual|
|R25|0,03|
|R26|0,02|
|R27|0,02|
|R28|0,13|
|R29|0,03|
|R30|0,34|
|R31|0,33|
|R32|0,18|
|R33|0,11|
|R34|0,16|
|R35|0,13|
|R36|0,36|

Estos resultados se muestran también como isolíneas de concentraciones promedio
anual de MPS de la fase de Operación del Proyecto en Figura 58.

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 120

Informe Final

Figura 58: Isolíneas de concentraciones promedio anual de MPS en la zona de estudio. Escenario meteorología año

2022 y escenario de emisiones etapa de Operación.

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 121

Informe Final

- Resultados de Dióxido de Nitrógeno (NO 2 )

Los resultados de NO 2, promedio anual y percentil 99 de las máximas diarias
concentraciones horarias modelados con CALPUFF en los receptores de interés para la
fase de Operación del Proyecto se presentan en Tabla 29. Como se observa en esta
tabla, el mayor aporte de este contaminante es en el receptor 8 con 3,07 y 89,22 μg/Nm [3],
como promedio anual y percentil 99 de las concentraciones horarias, respectivamente.
Esto alcanza a menos de 11 y 10% de la norma anual y diaria correspondiente,
respectivamente.

Tabla 29: Resultados de NO 2 promedio anual y percentil 99 de las máximas diarias

concentraciones horarias modeladas por el sistema CALPUFF, Escenario fase
de Operación.

|Receptor|Concentración de NO (μg/m3)<br>2|Col3|
|---|---|---|
|Receptor|Promedio anual|Percentil 99 de las conc. 1 hora|
|R1|0,00|0,03|
|R2|0,00|0,00|
|R3|0,00|0,08|
|R4|0,02|0,26|
|R5|0,00|0,13|
|R6|0,02|0,32|
|R7|0,01|0,26|
|R8|3,07|89,22|
|R9|1,95|46,34|
|R10|2,19|51,94|
|R11|2,22|62,93|
|R12|2,53|68,56|
|R13|2,06|58,00|
|R14|1,83|41,74|
|R15|1,68|42,02|
|R16|1,57|23,21|
|R17|0,72|23,62|
|R18|0,86|22,40|
|R19|0,89|23,65|
|R20|0,28|14,91|
|R21|0,34|10,20|

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 122

Informe Final

|Receptor|Concentración de NO (μg/m3)<br>2|Col3|
|---|---|---|
|Receptor|Promedio anual|Percentil 99 de las conc. 1 hora|
|R22|0,49|12,57|
|R23|0,09|2,44|
|R24|0,11|2,17|
|R25|0,11|1,93|
|R26|0,07|1,04|
|R27|0,08|1,24|
|R28|0,29|6,56|
|R29|0,17|6,22|
|R30|0,63|14,46|
|R31|0,54|15,63|
|R32|0,57|15,15|
|R33|0,42|8,98|
|R34|0,63|18,49|
|R35|0,53|11,82|
|R36|0,75|12,79|

Estos resultados se presentan también como isolíneas de concentración promedio
anual y Percentil 99 de las concentraciones horarias de NO 2 de la fase de Operación en
Figura 59 y Figura 60, respectivamente.

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 123

Informe Final

Figura 59: Isolíneas de concentraciones promedio anual de NO 2 en la zona de estudio. Escenario meteorología año

2022 y escenario de emisiones fase de Operación.

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 124

Informe Final

Figura 60: Isolíneas de percentiles 99 de concentraciones de 1 hora de NO 2 en la zona de estudio. Escenario

meteorología año 2022 y escenario de emisiones fase de Operación.

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 125

Informe Final

- Resultados de Dióxido de Azufre (SO 2 )

Los resultados de SO 2, percentil 98,5 de las concentraciones de 1 hora, percentiles 99 y
99,7 de las concentraciones diarias y percentil 99,73 de las concentraciones de 1 hora
de SO 2, en los receptores de interés modelados con CALPUFF para la etapa de Operación
del Proyecto se presentan en Tabla 30. Como se observa en esta tabla, los aportes de
este contaminante como promedio anual son mayores en el receptor 8 con 2,01 μg/Nm [3],
y en el receptor 12 con 5,12 y 11,42 μg/Nm [3] como percentil 99 de las concentraciones
24 horas y percentil 98,5 de las concentraciones de 1 hora, respectivamente. Esto
alcanza a 3% de la norma anual, diaria y horaria correspondiente.

Tabla 30: Resultados de SO 2 promedio anual, percentil 99 de las concentraciones

diarias y percentil 98,5 máximas concentraciones horarias modeladas por el
sistema CALPUFF, Escenario fase de Operación.

|Receptor|Concentración de SO (μg/m3)<br>2|Col3|Col4|
|---|---|---|---|
|Receptor|Promedio anual|Perc. 99 de las conc. 24 hr|Perc. 98,5 de las conc. 1 hr|
|R1|0,00|0,00|0,01|
|R2|0,00|0,00|0,00|
|R3|0,00|0,01|0,01|
|R4|0,01|0,03|0,08|
|R5|0,00|0,01|0,02|
|R6|0,01|0,05|0,14|
|R7|0,01|0,02|0,05|
|R8|2,01|4,82|10,26|
|R9|1,28|3,22|7,45|
|R10|1,44|3,73|7,34|
|R11|1,46|3,84|8,71|
|R12|1,66|5,12|11,42|
|R13|1,34|3,56|8,69|
|R14|1,20|3,40|9,50|
|R15|1,10|3,33|10,12|
|R16|1,03|2,72|7,10|
|R17|0,47|1,49|4,06|
|R18|0,57|1,70|4,59|
|R19|0,58|1,58|4,25|
|R20|0,18|0,60|1,70|

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 126

Informe Final

|R21|0,22|0,83|2,10|
|---|---|---|---|
|R22|0,32|1,09|2,99|
|R23|0,06|0,17|0,46|
|R24|0,07|0,20|0,56|
|R25|0,07|0,21|0,53|
|R26|0,05|0,13|0,33|
|R27|0,05|0,15|0,37|
|R28|0,19|0,69|2,14|
|R29|0,11|0,49|1,27|
|R30|0,41|1,35|4,70|
|R31|0,35|0,00|3,99|
|R32|0,37|0,00|4,42|
|R33|0,28|0,00|3,32|
|R34|0,42|0,00|4,93|
|R35|0,35|0,00|4,07|
|R36|0,49|0,00|3,84|

Los resultados de SO 2 modelados con CALPUFF también se presentan como isolíneas
de promedio anual, percentil 98,5 de las concentraciones de 1 hora y percentiles 99 de
las concentraciones de 1 hora de SO 2 de la fase de Operación en Figura 61 a Figura 63,
respectivamente.

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 127

Informe Final

Figura 61: Isolíneas de concentraciones promedio anual de SO 2 en la zona de estudio. Escenario meteorología año

2022 y escenario de emisiones fase de Operación.

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 128

Informe Final

Figura 62: Isolíneas de Percentil 99 de las concentraciones de 24 horas de SO 2 en la zona de estudio. Escenario

meteorología año 2022 y escenario de emisiones fase de Operación.

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 129

Informe Final

Figura 63: Isolíneas de Percentil 98,5 de las concentraciones de 1 hora de SO 2 en la zona de estudio. Escenario

meteorología año 2022 y escenario de emisiones fase de Operación.

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 130

Informe Final

Resultados de Monóxido de Carbono (CO)

Los resultados de CO, percentiles 99 de las máximas diarias concentraciones de 8 y 1
horas, en los receptores de interés modelados con CALPUFF para la fase de Operación
del Proyecto se presentan en Tabla 25. En esta tabla se observa que el mayor aporte de
CO del proyecto es en el receptor 8 con 45,72 y 193,20 μg/Nm [3] como concentración 8 y
1 hora, respectivamente. Esto no alcanza a 1% de la norma respectiva.

Tabla 31: Resultados de CO percentil 99 de las máximas diarias concentraciones de 8

y 1 horas modeladas por el sistema CALPUFF, Escenario fase de Operación.

|Receptor|Concentración de CO (μg/m3)|Col3|
|---|---|---|
|Receptor|Percentil 99 de las conc. 8 horas|Percentil 99 de las conc. 1 hora|
|R1|0,05|0,09|
|R2|0,01|0,02|
|R3|0,27|0,93|
|R4|0,41|1,37|
|R5|0,32|0,88|
|R6|0,47|1,49|
|R7|0,36|1,23|
|R8|45,72|193,20|
|R9|26,21|99,92|
|R10|28,75|115,60|
|R11|34,40|145,17|
|R12|41,55|151,23|
|R13|28,09|128,28|
|R14|25,75|107,13|
|R15|26,76|93,95|
|R16|20,86|62,09|
|R17|12,39|50,88|
|R18|11,88|52,13|
|R19|12,22|53,93|
|R20|5,65|33,42|
|R21|7,26|23,86|
|R22|8,87|27,74|
|R23|1,37|5,27|

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 131

Informe Final

|Receptor|Concentración de CO (μg/m3)|Col3|
|---|---|---|
|Receptor|Percentil 99 de las conc. 8 horas|Percentil 99 de las conc. 1 hora|
|R24|1,43|5,02|
|R25|1,50|5,44|
|R26|0,96|3,83|
|R27|1,13|3,66|
|R28|6,76|14,22|
|R29|4,64|13,51|
|R30|13,96|31,48|
|R31|12,28|42,04|
|R32|12,09|33,81|
|R33|9,38|19,47|
|R34|12,29|40,64|
|R35|10,67|27,43|
|R36|9,30|32,49|

Estos resultados se presentan también como isolíneas de Percentil 99 de los máximos
diarios de las concentraciones de 8 horas y de 1 hora de CO de la fase de Operación en
Figura 64 y Figura 65.

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 132

Informe Final

Figura 64: Isolíneas de Percentil 99 de los máximos diarios de las concentraciones de 8 horas de CO en la zona de

estudio. Escenario meteorología año 2022 y escenario de emisiones fase de Operación.

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 133

Informe Final

Figura 65: Isolíneas de Percentil 99 de los máximos diarios de las concentraciones de 1 hora de CO en la zona de

estudio. Escenario meteorología año 2022 y escenario de emisiones fase de Operación.

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 134

Informe Final

4.3.3 Área de Influencia

El Área de Influencia de calidad de aire se presenta en Figura 66 a Figura 71. Estas áreas,
que consideran la estadística de cada norma que ocupa mayor área, se obtuvieron para
el escenario de operación del proyecto por tener mayores aportes y son las siguientes
isolíneas por cada contaminante:

 - MP10: isolínea de 1 μg/Nm [3] del Percentil 98 de las concentraciones 24 horas.

Corresponde a menos de 1% de la Norma primaria de objeto de protección de la
”salud de la población”.

 - MP2,5: isolínea de 0,5 μg/Nm [3] del Percentil 98 de las concentraciones 24 horas.

Corresponde al 1% de la Norma primaria objeto de protección de la ”salud de la
población”.

 - NO 2 : isolínea de 1 μg/Nm [3] del Percentil 99 de las concentraciones de 1 hora. Es

importante mencionar que este escenario muy conservador y corresponde al 0,25%
de la Norma primaria objeto de protección de la ”salud de la población”.

 - SO 2 : isolínea de 1 μg/Nm [3] del Percentil 98,5 de las concentraciones de 1 hora.

Corresponde al 0,3% de la Norma primaria objeto de protección de la ”salud de la
población”.

 - CO: isolínea de 150 μg/Nm [3] del Percentil 99 de las concentraciones de 1 hora.

Corresponde al 0,5% de la Norma primaria objeto de protección de la ”salud de la
población”.

 MPS: isolínea de 1 mg/m [2] -día del Promedio anual. Corresponde al 0,1% de la Norma
secundaria objeto de protección de” recursos naturales renovables (plantas y
animales silvestres)”.

En estas figuras se puede observar que, en el caso de normas primarias, el área que
cubre mayor superficie y contiene las demás áreas es la correspondiente a la de NO 2,
por lo tanto, la Figura 68 muestra el Área de Influencia con objeto de protección de salud
de las personas. En tanto, al Área de Influencia de recursos naturales corresponde a la
de MPS presentada en Figura 71.

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 135

Informe Final

Figura 66: Área de Influencia para Calidad de Aire por MP10.

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 136

Informe Final

Figura 67: Área de Influencia para Calidad de Aire por MP2,5.

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 137

Informe Final

Figura 68: Área de Influencia para Calidad de Aire por NO 2 .

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 138

Informe Final

Figura 69: Área de Influencia para Calidad de Aire por SO 2 .

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 139

Informe Final

Figura 70: Área de Influencia para Calidad de Aire por CO.

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 140

Informe Final

Figura 71: Área de Influencia para Calidad de Aire por MPS.

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 141

Informe Final

4.3.4 Análisis del Aporte del Proyecto

En esta sección se presenta el análisis del aporte del Proyecto Planta Depuradora de
RILes Empresa San Lorenzo a la calidad del aire observada en las estaciones de la zona
de estudio en las comunas de San Felipe y Los Andes.

Los impactos de MP10, SO 2 y NO 2 del Proyecto, considerando la meteorología del año
2022 en conjunto con la línea base de calidad de aire presentada en sección 2.4, se
indican en Tabla 32 a Tabla 34, respectivamente. Como se observa en estas tablas, las
normas de calidad de aire primarias solo se superan en la estación Catemu, esto antes
de incluir los aportes del Proyecto. Como se observa también, el aporte del proyecto
estas estaciones monitoras es casi despreciable.

Tabla 32: Estimación del impacto del Proyecto Planta Depuradora de RILes Empresa

San Lorenzo a las concentraciones de MP10 observadas en la estación

Catemu.

|Estación|Concentración<br>basal Actual<br>(μg/m3N)|Aporte Total del<br>proyecto<br>(μg/m3N)|Total|Normativa<br>vigente|Porcentaje de la<br>norma|
|---|---|---|---|---|---|
|Concentración Anual de MP10|Concentración Anual de MP10|Concentración Anual de MP10|Concentración Anual de MP10|Concentración Anual de MP10|Concentración Anual de MP10|
|Catemu|108,42|0,001|108,42|50|217|
|Concentración 24 horas de MP10|Concentración 24 horas de MP10|Concentración 24 horas de MP10|Concentración 24 horas de MP10|Concentración 24 horas de MP10|Concentración 24 horas de MP10|
|Catemu|177,9|0,003|177,90|130|137|

Tabla 33: Estimación del impacto del Proyecto Planta Depuradora de RILes Empresa

San Lorenzo a las concentraciones de SO 2 observadas en la estación Catemu.

|Estación|Concentración<br>basal Actual<br>(μg/m3N)|Aporte Total del<br>proyecto<br>(μg/m3N)|Total|Normativa<br>vigente|Porcentaje de la<br>norma|
|---|---|---|---|---|---|
|Concentración Anual de SO2|Concentración Anual de SO2|Concentración Anual de SO2|Concentración Anual de SO2|Concentración Anual de SO2|Concentración Anual de SO2|
|Catemu|11,91|0,000|11,91|60|20|
|Concentración 24 horas de SO2|Concentración 24 horas de SO2|Concentración 24 horas de SO2|Concentración 24 horas de SO2|Concentración 24 horas de SO2|Concentración 24 horas de SO2|
|Catemu|32,78|0,000|32,78|150|22|
|Concentración horaria de SO2|Concentración horaria de SO2|Concentración horaria de SO2|Concentración horaria de SO2|Concentración horaria de SO2|Concentración horaria de SO2|
|Catemu|55,33|0,001|55,33|350|16|

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 142

Informe Final

Tabla 34: Estimación del impacto del Proyecto Planta Depuradora de RILes Empresa

San Lorenzo a las concentraciones de NO 2 observadas en observadas en la
estación Los Andes.

|Estación|Concentración<br>basal Actual<br>(μg/m3N)|Aporte Total del<br>proyecto<br>(μg/m3N)|Total|Normativa<br>vigente|Porcentaje de la<br>norma|
|---|---|---|---|---|---|
|Concentración Anual de NO2|Concentración Anual de NO2|Concentración Anual de NO2|Concentración Anual de NO2|Concentración Anual de NO2|Concentración Anual de NO2|
|Los Andes|21,21|0,002|21,21|100|21|
|Concentración horaria de NO2|Concentración horaria de NO2|Concentración horaria de NO2|Concentración horaria de NO2|Concentración horaria de NO2|Concentración horaria de NO2|
|Los Andes|88,05|0,033|88,08|400|22|

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 143

Informe Final

# CAPÍTULO 5: CONCLUSIONES

En este Capítulo se presentan las conclusiones correspondientes al Informe Final del
“Estudio de Calidad de Aire del Proyecto Depuradora de RILES Empresa San Lorenzo”.

La ejecución del estudio consideró la meteorología del año 2022 generada por el modelo
meteorológico de mesoescala WRF, de acuerdo a los requerimientos del SEA. La
meteorología generada por WRF fue validada a través de un análisis de incertidumbre
considerando la meteorología de la estación Los Andes.

Los aportes del proyecto a la calidad del aire de la zona de estudio, que consideró un
área de 56 x 50 km [2], se obtuvieron mediante la ejecución del modelo CALPUFF
considerando la meteorología del año 2022 y las emisiones de las fases de Construcción
y Operación del Proyecto.

Los resultados finales de CALPUFF permiten concluir lo siguiente:

El mayor aporte del Proyecto en las concentraciones de MP10 de los receptores del
área de estudio alcanzan a 2,28 y 5,08 μg/m [3], como promedio anual y percentil 98
de las concentraciones 24 horas, respectivamente, alcanzando como máximo un 5%
de la norma correspondiente. Estas concentraciones se presentan en los
Receptores 8 y 12, los que se encuentran aproximadamente a 140 y 160 metros del
Proyecto, respectivamente.

El aporte del Proyecto de MP2,5 más alto en los receptores de interés alcanza a 2,24
y 5,07 μg/m [3] como promedio anual y percentil 98 de las concentraciones 24 horas,
respectivamente, alcanzando como máximo un 11% de la norma primaria. Estos
aportes más altos también se presentan en los receptores 8 y 12, respectivamente.

- Con respecto al NO 2, éste alcanza como máximo en los receptores a 3,07 y 89,22
μg/m [3] como promedio anual y percentil 99 de las concentraciones de 1 hora,
respectivamente, llegando a solo un 11% de la norma primaria.

- Con respecto al aporte del Proyecto de SO 2, el mayor aporte del proyecto es en los
receptores 8 y 12 con 2,01, 5,12 y 11,42 μg/Nm [3], como promedio anual, percentil 99
de las concentraciones 24 horas y percentil 98,5 de las concentraciones de 1 hora,
respectivamente. Esto alcanza a 3% de la norma anual, diaria y horaria,
respectivamente.

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 144

Informe Final

Por otra parte, el aporte del proyecto de CO en todos los receptores es bajo y no
alcanza a 1% de la norma respectiva.

Los resultados de Material Particulado (MP10 y MP2,5) y gases muestran que las
máximas concentraciones se concentran alrededor del emplazamiento del Proyecto
y se dispersan en bajas concentraciones a medida que nos alejamos del Proyecto.

- Con respecto al análisis de los aportes de MP10, SO 2 y NO 2 del Proyecto,
considerando la meteorología del año 2022 en conjunto con la línea base de calidad
de aire, se observa que las normas de calidad de aire primarias solo se superan en
la estación Catemu, esto antes de incluir los aportes del Proyecto. Como se observa
también, el aporte del proyecto estas estaciones monitoras es casi despreciable.

Estos resultados implican que los máximos aportes de contaminantes a la zona de
estudio tienen un bajo porcentaje de impacto en la calidad del aire y no representan
un peligro para la salud de las personas del área.

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 145

Informe Final

# CAPÍTULO 6: BIBLIOGRAFIA

SEA, (2023). Guía para el uso de modelos de calidad del aire en el SEIA.
[https://www.sea.gob.cl/sites/default/files/migration_files/guias/Guia_uso_modelo_ca](https://www.sea.gob.cl/sites/default/files/migration_files/guias/Guia_uso_modelo_calidad_del_aire_seia.pdf)
[lidad_del_aire_seia.pdf.](https://www.sea.gob.cl/sites/default/files/migration_files/guias/Guia_uso_modelo_calidad_del_aire_seia.pdf)

 Ciren (2019). Comuna San Felipe, Recursos Naturales. [https://www.sitrural.cl/wp](https://www.sitrural.cl/wp-content/uploads/2020/03/San-Felipe_rec_nat_1_v2.pdf)

 [content/uploads/2020/03/San](https://www.sitrural.cl/wp-content/uploads/2020/03/San-Felipe_rec_nat_1_v2.pdf) Felipe_rec_nat_1_v2.pdf

Norma de calidad del aire para MP10 (D.S. N° 59/1998 MINSEGPRES, modificado por
D.S. N° 12/2022, MMA)

Norma primaria de calidad del aire para MP2,5 (D.S. N° 12/2011 Ministerio del Medio
Ambiente)

Norma primaria de calidad del aire para NO 2 (D.S. N° 114/2002 del Ministerio Secretaría
General de la Presidencia)

Norma primaria de calidad del aire para CO (D.S. N° 115/2002 MINSEGPRES)

Norma primaria de calidad del aire para SO 2 (D.S. N° 104/2018 del Ministerio de Medio
Ambiente)

Norma secundaria de calidad del aire para SO 2 (D.S. N° 22/2009 del MINSEGPRES)

De Osmar Valdebenito, CC BY-SA 2.5,
[https://commons.wikimedia.org/w/index.php?curid=1650381](https://commons.wikimedia.org/w/index.php?curid=1650381)

De B1mbo - Trabajo propio, CC BY-SA 2.5,
[https://commons.wikimedia.org/w/index.php?curid=3077049](https://commons.wikimedia.org/w/index.php?curid=3077049)

Estudio EM2023/200-54 | Ecoazul

“Estudio de Calidad de Aire del Proyecto Planta Depuradora de RILes Empresa San Lorenzo” 146

Informe Final