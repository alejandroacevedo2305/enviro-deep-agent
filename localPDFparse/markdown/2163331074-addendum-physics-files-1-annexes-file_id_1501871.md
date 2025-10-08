---
title: Memoria de aguas lluvias Cesar Ponce.docx
author: Rodrigo Sepúlveda Chamblas
date: D:20241204181018-03'00'
language: es
type: report
pages: 35
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE COMITÉS DE VIVIENDAS SOCIALES “ALTOS DE ORIENTE II” “SALVADOR ALLENDE” COMUNA DE CHILLÁN
-->

## MEMORIA DE CÁLCULO

# PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE COMITÉS DE VIVIENDAS SOCIALES “ALTOS DE ORIENTE II” “SALVADOR ALLENDE” COMUNA DE CHILLÁN

diciembre de 2024

PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE
### i
COMUNA DE CHILLÁN

**ÍNDICE GENERAL**

**1** **ANTECEDENTES GENERALES .............................................................................. 1**

1.1 Descripción de las modificaciones sobre el Canal 1 ................................................ 3

1.2 Descripción de las modificaciones sobre el Canal 2. ............................................... 4

1.3 Descripción de Canal 4 a incorporar ........................................................................ 4

**2** **OBJETIVOS ................................................................................................................. 5**

2.1 Objetivo General ...................................................................................................... 5

2.2 Objetivos Específicos .............................................................................................. 5

**3** **HIDROLOGÍA ............................................................................................................. 6**

3.1 Consideraciones Generales ...................................................................................... 6

3.2 Método Racional ...................................................................................................... 6
_3.2.1_ _Área Aportante ................................................................................................. 7_
_3.2.2_ _Coeficiente de Escorrentía ............................................................................... 8_
_3.2.3_ _Intensidad de precipitación .............................................................................. 9_

3.3 Caudales Máximos Instantáneos ............................................................................ 12

**4** **ANÁLISIS HIDRÁULICO ........................................................................................ 15**

4.1 Caudales de Modelación ........................................................................................ 15

4.2 Coeficiente de Rugosidad de Manning .................................................................. 18

**5** **ESTUDIO DE ARRASTRE DE SEDIMENTOS .................................................... 19**

5.1 SOCAVACIÓN GENERAL .................................................................................. 19

_5.1.1_ _Método de Lischtvan - Levediev .................................................................... 19_

5.2 SOCAVACIÓN EN LA DESCARGA .................................................................. 23

5.3 DISEÑO DECANTADOR .................................................................................... 24

**6** **VERIFICACIÓN LAGUNA DE REGULACIÓN .................................................. 26**

**7** **ANÁLISIS DE RESULTADOS................................................................................. 27**

**8** **CONCLUSIONES ...................................................................................................... 30**

PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE
### ii
COMUNA DE CHILLÁN

**ÍNDICE DE FIGURAS**

Figura 1: Imagen representativa de la ubicación del proyecto. .............................................. 1

Figura 2: Ubicación de los cauces en estudio. ........................................................................ 2

Figura 3: Descripción de las modificaciones sobre el Canal 1. .............................................. 3

Figura 4: Subcuencas aportantes a los cauces. ....................................................................... 7

Figura 5: Subcuencas del loteo proyectado. ........................................................................... 8

Figura 6: Puntos de modelación - Situación Base. .............................................................. 15

Figura 7: Puntos de modelación en HEC RAS - Situación Proyectada. .............................. 16

Figura 8: Puntos de modelación en EPA SWMM - Situación Proyectada. ......................... 16

Figura 9: Esquemas para cálculo de socavación según Método de Lischtvan - Levediev. . 20

Figura 10: Análisis granulométrico. ..................................................................................... 22

PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE
### iii
COMUNA DE CHILLÁN

**ÍNDICE DE TABLAS**

Tabla 1: Intensidades de Precipitación para tormentas con duración menor a 120 minutos. . 9

<!-- INICIO TABLA 1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Las intensidades de precipitación asociadas a los distintos períodos de retorno se obtuvieron del Cuadro N° 3.1.2-7 del Plan Maestro, el cual se detalla a continuación. -->

**Tabla 1: Intensidades de Precipitación para tormentas con duración menor a 120 minutos.****

| Duración<br>(min) | T=2 | T=5 | T=10 | T=25 | T=50 | T=100 |
| --- | --- | --- | --- | --- | --- | --- |
| 10 | 38.90 | 53.30 | 62.80 | 74.80 | 83.70 | 92.60 |
| 20 | 26.60 | 35.00 | 40.50 | 47.40 | 52.60 | 57.70 |
| 30 | 21.40 | 28.20 | 32.60 | 38.30 | 42.50 | 46.70 |
| 40 | 18.50 | 24.80 | 29.00 | 34.20 | 38.20 | 42.00 |
| 50 | 16.90 | 23.30 | 27.50 | 32.90 | 36.80 | 40.80 |
| 60 | 15.80 | 20.90 | 24.20 | 28.40 | 31.50 | 34.60 |
| 70 | 15.10 | 20.30 | 23.70 | 28.00 | 31.20 | 34.40 |
| 80 | 14.10 | 18.90 | 22.10 | 26.10 | 29.10 | 32.10 |
| 90 | 13.60 | 18.40 | 21.50 | 25.50 | 28.50 | 31.40 |
| 100 | 13.10 | 18.20 | 21.50 | 25.70 | 28.80 | 31.90 |
| 110 | 12.50 | 17.10 | 20.10 | 23.90 | 26.70 | 29.60 |
| 120 | 11.90 | 16.20 | 19.00 | 22.50 | 25.10 | 27.70 |

<!-- Estadísticas: 12 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- _**3.2.3.1**_ _**Tiempo de Concentración**_ El tiempo de concentración del área aportante se define como el tiempo necesario para que -->
<!-- FIN TABLA 1 -->


Tabla 2: Métodos para calcular el tiempo de concentración. ............................................... 10

<!-- INICIO TABLA 2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE ### 10 COMUNA DE CHILLÁN -->

**Tabla 2: Métodos para calcular el tiempo de concentración.****

| Método | Expresión | Condiciones de Uso |
| --- | --- | --- |
| Norma Española<br>ó Témez | 19<br>.0<br>76<br>.0<br>18<br>_S_<br>_L_<br>_Tc_<br><br>= | Para cuencas naturales de cabecera en zonas urbanas. |
| California<br>Highway and<br>Publics Works | <br><br>385<br>.0<br>3<br>57<br><br><br><br><br><br><br>=<br>_H_<br>_L_<br>_Tc_ | Adaptación de la fórmula de Kirpich para cuencas de<br>montaña. Aplicable a cuencas urbanas con abundates<br>espacios libres o poco desarrollados, como parques, parcelas<br>y similares. |
| Giandotti | )<br>8.0<br>(<br>)<br>5.1<br>4<br>(<br>60<br>5.0<br>5.0<br>_Hm_<br>_L_<br>_A_<br>_Tc_<br><br><br>+<br><br><br>=<br><br><br><br> | Para cuencas menores a 200 hectáreas y con pendiente. |
| SCS (1975) | (<br>)<br>(<br>)<br>5.0<br>7.0<br>8.0<br>1900<br>9<br>1000<br>7.<br>258<br>_S_<br>_CN_<br>_L_<br>_Tc_<br><br>−<br><br>= | Desarrollada para cuencas rurales, aplicable a cuencas<br>urbanas con abundante espacios libres. |
| Kirpich (1940) | <br><br><br><br>385<br>.0<br>77<br>.0<br>0195<br>.0<br>_S_<br>_L_<br>_Tc_<br><br>=<br><br> | Desarrollada con datos SCS para áreas rurales Tennessee.<br>Aplicable a cuencas urbanas con abundantes espacios libres<br>o poco desarrollados, como parques, parcelas y similares. |
| Izzard (1946) | <br>(<br>)<br>333<br>.0<br>667<br>.0<br>33<br>.0<br>0000276<br>.0<br>28<br>.<br>525<br>_S_<br>_i_<br>_L_<br>_c_<br>_i_<br>_Tc_<br><br><br>+<br><br><br>= | Desarrollada en experimentos de laboratorio. Aplicable a<br>sectores urbanos típicos como calles, patios, pasajes, etc. |
| Federal Aviation<br>Agency (1970) | <br>(<br>)<br>333<br>.0<br>5.0<br>1.1<br>26<br>.3<br>_S_<br>_L_<br>_C_<br>_Tc_<br><br>−<br><br>= | Desarrollada para aeropuertos. Aplicable en sectores planos<br>desarrollados con poca vegetación, como estacionamientos<br>grandes, sectores de grandes industrias. |
| Morgali y Linsley<br>(1965) | 3.0<br>4.0<br>6.0<br>6.0<br>7<br>_S_<br>_i_<br>_n_<br>_L_<br>_Tc_<br><br><br><br>= | Fórmula de flujo superficial. Aplicable a sectores urbanos<br>típicos como calles, patios, pasajes, etc. |

<!-- Estadísticas: 8 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE ### 11 COMUNA DE CHILLÁN -->
<!-- FIN TABLA 2 -->


Tabla 3: Parámetros para determinar el Tc para las áreas aportantes a los canales. ............ 11

<!-- INICIO TABLA 3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- ### 11 COMUNA DE CHILLÁN Los parámetros de entrada para calcular los tiempos de concentración se muestran en la Tabla 3. -->

**Tabla 3: Parámetros para determinar el Tc para las áreas aportantes a los canales.****

| Cuenca | Tipo de<br>Superficie | Parámetros | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Cuenca** | **Tipo de**<br>**Superficie** | **Largo**<br>**(m)** | **Área**<br>**(km2) ** | **H **<br>**(m)** | **Hm**<br>**(m)** | **CN** | **S **<br>**(m/m)** | **I **<br>**(mm/hr)** | **Coef.**<br>**Retardo** | **Coef.**<br>**Escorrentía** | **Manning** |
| A1 | Urbana | 225.00 | 0.042 | 1.00 | 0.50 | 92 | 0.004 | 53.00 | 0.012 | 0.70 | 0.03 |
| A2 | Rural | 550.00 | 0.053 | 1.00 | 0.50 | 83 | 0.002 | 35.00 | 0.060 | 0.15 | 0.10 |
| A3 | Rural | 480.00 | 0.061 | 1.00 | 0.50 | 83 | 0.002 | 41.00 | 0.060 | 0.15 | 0.10 |
| A4 | Rural | 500.00 | 0.048 | 1.00 | 0.50 | 83 | 0.002 | 38.00 | 0.060 | 0.15 | 0.10 |
| A5-1 | Urbana | 165.00 | 0.001 | 0.80 | 0.40 | 92 | 0.005 | 62.00 | 0.012 | 0.70 | 0.03 |
| A5-2 | Urbana | 65.00 | 0.041 | 0.40 | 0.20 | 83 | 0.006 | 92.60 | 0.012 | 0.70 | 0.03 |
| A6 | Rural | 410.00 | 0.043 | 1.00 | 0.50 | 83 | 0.002 | 42.00 | 0.060 | 0.15 | 0.10 |

<!-- Estadísticas: 8 filas, 12 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 4: Tiempos de concentración de las áreas aportantes a los canales.** |Cuenca|Tiempos de Concentración|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Método<br>Empleado|Tc (min)<br>considerado|Tc (hr)<br>considerado| |---|---|---|---|---|---|---|---|---|---|---|---| -->
<!-- FIN TABLA 3 -->


Tabla 4: Tiempos de concentración de las áreas aportantes a los canales. ........................... 11

<!-- INICIO TABLA 4 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |A4|Rural|500.00|0.048|1.00|0.50|83|0.002|38.00|0.060|0.15|0.10| |A5-1|Urbana|165.00|0.001|0.80|0.40|92|0.005|62.00|0.012|0.70|0.03| |A5-2|Urbana|65.00|0.041|0.40|0.20|83|0.006|92.60|0.012|0.70|0.03| |A6|Rural|410.00|0.043|1.00|0.50|83|0.002|42.00|0.060|0.15|0.10| -->

**Tabla 4: Tiempos de concentración de las áreas aportantes a los canales.****

| Cuenca | Tiempos de Concentración | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Método<br>Empleado | Tc (min)<br>considerado | Tc (hr)<br>considerado |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Cuenca** | **N.**<br>**Española** | **California** | **Giandotti** | **SCS** | **Kirpich** | **Izzard** | **F.**<br>**Aviation** | **Morgali** | **Morgali** | **Morgali** | **Morgali** |
| A1 | 16.21 | 10.18 | 122.33 | 24.10 | 10.16 | 18.15 | 118.75 | 22.84 | Promedio:<br>Morgali e Izzard | 20.49 | 0.34 |
| A2 | 37.90 | 28.58 | 185.18 | 108.48 | 28.52 | 196.09 | 593.83 | 124.11 | Promedio:<br>N. Española, y SCS | 73.19 | 1.22 |
| A3 | 33.30 | 24.42 | 180.72 | 90.88 | 24.37 | 161.66 | 530.17 | 103.06 | Promedio:<br>N. Española, y SCS | 62.09 | 1.03 |
| A4 | 34.62 | 25.60 | 172.69 | 95.84 | 25.55 | 174.49 | 548.51 | 110.22 | Promedio:<br>N. Española, y SCS | 65.23 | 1.09 |
| A5-1 | 12.60 | 10.00 | 46.68 | 18.01 | 10.00 | 14.60 | 98.79 | 17.35 | Promedio:<br>Morgali e Izzard | 15.97 | 0.27 |
| A5-2 | 10.00 | 10.00 | 152.35 | 10.68 | 10.00 | 10.00 | 57.27 | 10.00 | Promedio:<br>Morgali e Izzard | 10.00 | 0.17 |
| A6 | 28.67 | 20.35 | 153.62 | 74.04 | 20.31 | 143.36 | 464.93 | 88.57 | Promedio:<br>N. Española, y SCS | 51.36 | 0.86 |

<!-- Estadísticas: 8 filas, 12 columnas -->
<!-- Contexto posterior: -->
<!-- PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE ### 12 COMUNA DE CHILLÁN -->
<!-- FIN TABLA 4 -->


Tabla 5: Intensidades de Precipitación (mm/hr). .................................................................. 12

<!-- INICIO TABLA 5 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- De acuerdo a lo anterior, se presenta en la Tabla 5 las intensidades de precipitación asociada a los periodos de retorno para las subcuencas que aportan a los canales. -->

**Tabla 5: Intensidades de Precipitación (mm/hr).****

| Cuenca | Intensidad (mm/hr) | Col3 | Col4 | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Cuenca** | **T-2** | **T-5** | **T-10** | **T-25** | **T-50** | **T-100** |
| A1 | 27.04 | 35.81 | 41.59 | 48.89 | 54.35 | 59.63 |
| A2 | 14.46 | 19.41 | 22.66 | 26.77 | 29.88 | 32.82 |
| A3 | 15.67 | 21.01 | 24.51 | 28.94 | 32.28 | 35.46 |
| A4 | 15.30 | 20.52 | 23.94 | 28.27 | 31.54 | 34.65 |
| A5-1 | 30.57 | 40.37 | 46.84 | 55.00 | 61.10 | 67.02 |
| A5-2 | 38.49 | 50.57 | 58.57 | 68.64 | 76.15 | 83.49 |
| A6 | 17.21 | 23.02 | 26.83 | 31.66 | 35.29 | 38.76 |

<!-- Estadísticas: 8 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- **3.3** **Caudales Máximos Instantáneos** Luego de efectuado el análisis hidrológico de la cuenca en estudio, se presenta en la Tabla 6 -->
<!-- FIN TABLA 5 -->


Tabla 6: Caudales máximos instantáneos de las áreas aportantes a los canales (m [3] /s). ....... 12

<!-- INICIO TABLA 6 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Luego de efectuado el análisis hidrológico de la cuenca en estudio, se presenta en la Tabla 6 los caudales máximos instantáneos asociados a los distintos períodos de retorno. -->

**Tabla 6: Caudales máximos instantáneos de las áreas aportantes a los canales (m** **[3]** **/s).****

| Cuenca | Caudales (m3/s) | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Cuenca** | **T-2** | **T-5** | **T-10** | **T-25** | **T-50** | **T-100** | **T-150** |
| A1 | 0.219 | 0.290 | 0.336 | 0.395 | 0.440 | 0.482 | 0.513 |
| A2 | 0.032 | 0.043 | 0.050 | 0.059 | 0.066 | 0.072 | 0.077 |
| A3 | 0.040 | 0.053 | 0.062 | 0.073 | 0.081 | 0.089 | 0.095 |
| A4 | 0.031 | 0.041 | 0.048 | 0.057 | 0.063 | 0.070 | 0.074 |
| A5-1 | 0.008 | 0.010 | 0.012 | 0.014 | 0.016 | 0.017 | 0.019 |
| A5-2 | 0.308 | 0.404 | 0.468 | 0.549 | 0.609 | 0.667 | 0.709 |
| A6 | 0.031 | 0.042 | 0.049 | 0.057 | 0.064 | 0.070 | 0.075 |

<!-- Estadísticas: 8 filas, 8 columnas -->
<!-- Contexto posterior: -->
<!-- En las Tabla 7 y Tabla 8 se presentan el resumen para los cálculos de los caudales máximos instantáneos, tanto para las áreas aportantes a los canales a modificar como los caudales -->
<!-- FIN TABLA 6 -->


Tabla 7: Resumen de las variables para el cálculo de los caudales máximos instantáneos

<!-- INICIO TABLA 7 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE ### 13 COMUNA DE CHILLÁN -->

**Tabla 7: Resumen de las variables para el cálculo de los caudales máximos instantáneos aportados a los canales en estudio.****

| Cuenca | Área<br>(km2) | Tipo de<br>superficie | Coeficiente<br>de<br>escorrentía | Tc<br>(min) | Intensidad (mm/hr) | Col7 | Col8 | Col9 | Col10 | Col11 | Caudales (m3/s) | Col13 | Col14 | Col15 | Col16 | Col17 | Col18 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Cuenca** | **Área**<br>**(km2) ** | **Tipo de**<br>**superficie** | **Coeficiente**<br>**de**<br>**escorrentía** | **Tc**<br>**(min)** | **T-2** | **T-5** | **T-10** | **T-25** | **T-50** | **T-100** | **T-2** | **T-5** | **T-10** | **T-25** | **T-50** | **T-100** | **T-150** |
| A1 | 0.042 | Urbana | 0.70 | 20.49 | 27.04 | 35.81 | 41.59 | 48.89 | 54.35 | 59.63 | 0.219 | 0.290 | 0.336 | 0.395 | 0.440 | 0.482 | 0.513 |
| A2 | 0.053 | Rural | 0.15 | 73.19 | 14.46 | 19.41 | 22.66 | 26.77 | 29.88 | 32.82 | 0.032 | 0.043 | 0.050 | 0.059 | 0.066 | 0.072 | 0.077 |
| A3 | 0.061 | Rural | 0.15 | 62.09 | 15.67 | 21.01 | 24.51 | 28.94 | 32.28 | 35.46 | 0.040 | 0.053 | 0.062 | 0.073 | 0.081 | 0.089 | 0.095 |
| A4 | 0.048 | Rural | 0.15 | 65.23 | 15.30 | 20.52 | 23.94 | 28.27 | 31.54 | 34.65 | 0.031 | 0.041 | 0.048 | 0.057 | 0.063 | 0.070 | 0.074 |
| A5-1 | 0.001 | Urbana | 0.70 | 15.97 | 30.57 | 40.37 | 46.84 | 55.00 | 61.10 | 67.02 | 0.008 | 0.010 | 0.012 | 0.014 | 0.016 | 0.017 | 0.019 |
| A5-2 | 0.041 | Urbana | 0.70 | 10.00 | 38.49 | 50.57 | 58.57 | 68.64 | 76.15 | 83.49 | 0.308 | 0.404 | 0.468 | 0.549 | 0.609 | 0.667 | 0.709 |
| A6 | 0.043 | Rural | 0.15 | 51.36 | 17.21 | 23.02 | 26.83 | 31.66 | 35.29 | 38.76 | 0.031 | 0.042 | 0.049 | 0.057 | 0.064 | 0.070 | 0.075 |

<!-- Estadísticas: 8 filas, 18 columnas -->
<!-- Contexto posterior: -->
<!-- PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE ### 14 COMUNA DE CHILLÁN -->
<!-- FIN TABLA 7 -->


aportados a los canales en estudio. ....................................................................................... 13

Tabla 8: Resumen de las variables para el cálculo de los caudales máximos instantáneos

<!-- INICIO TABLA 8 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE ### 14 COMUNA DE CHILLÁN -->

**Tabla 8: Resumen de las variables para el cálculo de los caudales máximos instantáneos subcuencas del loteo.****

| Subcuenca | Área<br>ha | Área<br>km2 | Coeficiente<br>de<br>escorrentía | Tc<br>(min) | Intensidad (mm/hr) | Col7 | Col8 | Col9 | Col10 | Col11 | Caudales (m3/s) | Col13 | Col14 | Col15 | Col16 | Col17 | Col18 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Subcuenca** | **Área**<br>**ha** | **Área**<br>**km2 ** | **Coeficiente**<br>**de**<br>**escorrentía** | **Tc**<br>**(min)** | **T-2** | **T-5** | **T-10** | **T-25** | **T-50** | **T-100** | **T-2** | **T-5** | **T-10** | **T-25** | **T-50** | **T-100** | **T-150** |
| S1 | 0.11 | 0.0011 | 0.70 | 10.00 | 38.90 | 53.30 | 62.80 | 74.80 | 83.70 | 92.60 | 0.008 | 0.011 | 0.013 | 0.016 | 0.018 | 0.020 | 0.021 |
| S2 | 0.11 | 0.0011 | 0.70 | 10.00 | 38.90 | 53.30 | 62.80 | 74.80 | 83.70 | 92.60 | 0.008 | 0.011 | 0.013 | 0.016 | 0.018 | 0.020 | 0.021 |
| S3 | 0.08 | 0.0008 | 0.70 | 10.00 | 38.90 | 53.30 | 62.80 | 74.80 | 83.70 | 92.60 | 0.006 | 0.008 | 0.010 | 0.012 | 0.013 | 0.014 | 0.015 |
| S4 | 0.03 | 0.0003 | 0.70 | 10.00 | 38.90 | 53.30 | 62.80 | 74.80 | 83.70 | 92.60 | 0.002 | 0.003 | 0.004 | 0.004 | 0.005 | 0.005 | 0.006 |
| S5 | 0.27 | 0.0027 | 0.70 | 10.00 | 38.90 | 53.30 | 62.80 | 74.80 | 83.70 | 92.60 | 0.020 | 0.028 | 0.033 | 0.039 | 0.044 | 0.049 | 0.052 |
| S6 | 0.14 | 0.0014 | 0.70 | 10.00 | 38.90 | 53.30 | 62.80 | 74.80 | 83.70 | 92.60 | 0.011 | 0.015 | 0.017 | 0.020 | 0.023 | 0.025 | 0.027 |
| S7 | 0.07 | 0.0007 | 0.70 | 10.00 | 38.90 | 53.30 | 62.80 | 74.80 | 83.70 | 92.60 | 0.005 | 0.007 | 0.009 | 0.010 | 0.011 | 0.013 | 0.014 |
| S8 | 0.06 | 0.0006 | 0.70 | 10.00 | 38.90 | 53.30 | 62.80 | 74.80 | 83.70 | 92.60 | 0.005 | 0.006 | 0.007 | 0.009 | 0.010 | 0.011 | 0.012 |
| S9 | 0.06 | 0.0006 | 0.70 | 10.00 | 38.90 | 53.30 | 62.80 | 74.80 | 83.70 | 92.60 | 0.005 | 0.006 | 0.007 | 0.009 | 0.010 | 0.011 | 0.012 |
| S10 | 0.25 | 0.0025 | 0.70 | 10.00 | 38.90 | 53.30 | 62.80 | 74.80 | 83.70 | 92.60 | 0.019 | 0.026 | 0.031 | 0.036 | 0.041 | 0.045 | 0.048 |
| S11 | 0.13 | 0.0013 | 0.70 | 10.00 | 38.90 | 53.30 | 62.80 | 74.80 | 83.70 | 92.60 | 0.010 | 0.013 | 0.016 | 0.019 | 0.021 | 0.023 | 0.025 |
| S12 | 0.24 | 0.0024 | 0.70 | 10.00 | 38.90 | 53.30 | 62.80 | 74.80 | 83.70 | 92.60 | 0.018 | 0.025 | 0.029 | 0.035 | 0.039 | 0.043 | 0.046 |
| S13 | 0.22 | 0.0022 | 0.70 | 10.00 | 38.90 | 53.30 | 62.80 | 74.80 | 83.70 | 92.60 | 0.017 | 0.023 | 0.027 | 0.032 | 0.036 | 0.040 | 0.042 |
| S14 | 0.07 | 0.0007 | 0.70 | 10.00 | 38.90 | 53.30 | 62.80 | 74.80 | 83.70 | 92.60 | 0.005 | 0.007 | 0.009 | 0.010 | 0.011 | 0.013 | 0.014 |
| S15 | 0.25 | 0.0025 | 0.70 | 10.00 | 38.90 | 53.30 | 62.80 | 74.80 | 83.70 | 92.60 | 0.019 | 0.026 | 0.031 | 0.036 | 0.041 | 0.045 | 0.048 |
| S16 | 0.11 | 0.0011 | 0.70 | 10.00 | 38.90 | 53.30 | 62.80 | 74.80 | 83.70 | 92.60 | 0.008 | 0.011 | 0.013 | 0.016 | 0.018 | 0.020 | 0.021 |
| S17 | 0.04 | 0.0004 | 0.70 | 10.00 | 38.90 | 53.30 | 62.80 | 74.80 | 83.70 | 92.60 | 0.003 | 0.004 | 0.005 | 0.006 | 0.007 | 0.007 | 0.008 |
| S18 | 0.05 | 0.0005 | 0.70 | 10.00 | 38.90 | 53.30 | 62.80 | 74.80 | 83.70 | 92.60 | 0.004 | 0.005 | 0.006 | 0.007 | 0.008 | 0.009 | 0.010 |
| S19 | 0.04 | 0.0004 | 0.70 | 10.00 | 38.90 | 53.30 | 62.80 | 74.80 | 83.70 | 92.60 | 0.003 | 0.004 | 0.005 | 0.006 | 0.007 | 0.007 | 0.008 |
| S20 | 0.14 | 0.0014 | 0.70 | 10.00 | 38.90 | 53.30 | 62.80 | 74.80 | 83.70 | 92.60 | 0.011 | 0.015 | 0.017 | 0.020 | 0.023 | 0.025 | 0.027 |
| S21 | 0.03 | 0.0003 | 0.70 | 10.00 | 38.90 | 53.30 | 62.80 | 74.80 | 83.70 | 92.60 | 0.002 | 0.003 | 0.004 | 0.004 | 0.005 | 0.005 | 0.006 |
| S22 | 0.06 | 0.0006 | 0.70 | 10.00 | 38.90 | 53.30 | 62.80 | 74.80 | 83.70 | 92.60 | 0.005 | 0.006 | 0.007 | 0.009 | 0.010 | 0.011 | 0.012 |
| S23 | 0.17 | 0.0017 | 0.70 | 10.00 | 38.90 | 53.30 | 62.80 | 74.80 | 83.70 | 92.60 | 0.013 | 0.018 | 0.021 | 0.025 | 0.028 | 0.031 | 0.033 |

<!-- Estadísticas: 24 filas, 18 columnas -->
<!-- Contexto posterior: -->
<!-- PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE ### 15 COMUNA DE CHILLÁN -->
<!-- FIN TABLA 8 -->


subcuencas del loteo. ............................................................................................................ 14

Tabla 9: Caudales Máximos Instantáneos - Situación Base en HEC RAS. ......................... 17

<!-- INICIO TABLA 9 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE ### 17 COMUNA DE CHILLÁN -->

**Tabla 9: Caudales Máximos Instantáneos - Situación Base en HEC RAS.****

| River | Reach | RS | T-10 | T-100 | T-150 |
| --- | --- | --- | --- | --- | --- |
| CANAL 1 | TRAMO 1 | 982 | 0.336 | 0.482 | 0.513 |
| CANAL 1 | TRAMO 1 | 160 | 0.386 | 0.555 | 0.590 |
| CANAL 1 | TRAMO 2 | 100 | 0.916 | 1.311 | 1.394 |
| CANAL 1 | TRAMO 3 | 70 | 0.977 | 1.398 | 1.487 |
| CANAL 1 | TRAMO 3 | 50 | 1.025 | 1.468 | 1.562 |
| CANAL 2-A | CANAL 2-A | 100 | 0.062 | 0.089 | 0.095 |
| CANAL 2-B | CANAL 2-B | 91.49 | 0.468 | 0.667 | 0.709 |
| CANAL 3-A | CANAL 3-A | 130 | 0.048 | 0.070 | 0.074 |
| CANAL 3-B | CANAL 3-B | 50 | 0.012 | 0.017 | 0.019 |

<!-- Estadísticas: 9 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 10: Caudales Máximos Instantáneos - Situación Proyectada en HEC RAS.** |River|Reach|RS|T-10|T-100|T-150| |---|---|---|---|---|---| -->
<!-- FIN TABLA 9 -->


Tabla 10: Caudales Máximos Instantáneos - Situación Proyectada en HEC RAS. ............. 17

<!-- INICIO TABLA 10 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |CANAL 2-A|CANAL 2-A|100|0.062|0.089|0.095| |CANAL 2-B|CANAL 2-B|91.49|0.468|0.667|0.709| |CANAL 3-A|CANAL 3-A|130|0.048|0.070|0.074| |CANAL 3-B|CANAL 3-B|50|0.012|0.017|0.019| -->

**Tabla 10: Caudales Máximos Instantáneos - Situación Proyectada en HEC RAS.****

| River | Reach | RS | T-10 | T-100 | T-150 |
| --- | --- | --- | --- | --- | --- |
| CANAL 1 | TRAMO 1 | 20 | 1.138 | 1.641 | 1.748 |
| CANAL 1 | TRAMO 2 | 80 | 1.262 | 1.820 | 1.939 |
| CANAL 2-A | TRAMO 1 | 110 | 0.062 | 0.089 | 0.095 |
| CANAL 3-A | TRAMO 1 | 130 | 0.048 | 0.070 | 0.074 |
| CANAL 3-B | TRAMO 1 | 50 | 0.012 | 0.017 | 0.019 |
| CANAL 4 | CANAL 4 | 160 | 0.050 | 0.072 | 0.077 |

<!-- Estadísticas: 6 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 11: Caudales Máximos Instantáneos - Situación Proyectada en EPA SWMM.** |CAUDALES A EPA SWMM (m3/s)|Col2|Col3|Col4|Col5|Col6|Col7|Col8| |---|---|---|---|---|---|---|---| -->
<!-- FIN TABLA 10 -->


Tabla 11: Caudales Máximos Instantáneos - Situación Proyectada en EPA SWMM. ........ 17

<!-- INICIO TABLA 11 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |CANAL 2-A|TRAMO 1|110|0.062|0.089|0.095| |CANAL 3-A|TRAMO 1|130|0.048|0.070|0.074| |CANAL 3-B|TRAMO 1|50|0.012|0.017|0.019| |CANAL 4|CANAL 4|160|0.050|0.072|0.077| -->

**Tabla 11: Caudales Máximos Instantáneos - Situación Proyectada en EPA SWMM.****

| CAUDALES A EPA SWMM (m3/s) | Col2 | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **NODO** | **T-2** | **T-5** | **T-10** | **T-25** | **T-50** | **T-100** | **T-150** |
| 1 | 0.219 | 0.290 | 0.336 | 0.395 | 0.440 | 0.482 | 0.513 |
| 2 | 0.008 | 0.011 | 0.013 | 0.016 | 0.018 | 0.020 | 0.021 |
| 4 | 0.017 | 0.023 | 0.027 | 0.032 | 0.036 | 0.040 | 0.042 |
| 5 | 0.045 | 0.062 | 0.073 | 0.087 | 0.098 | 0.108 | 0.116 |
| 6 | 0.019 | 0.026 | 0.031 | 0.036 | 0.041 | 0.045 | 0.048 |
| 7 | 0.017 | 0.023 | 0.027 | 0.032 | 0.036 | 0.040 | 0.042 |
| 15 | 0.308 | 0.404 | 0.468 | 0.549 | 0.609 | 0.667 | 0.709 |
| 14 | 0.030 | 0.041 | 0.049 | 0.058 | 0.065 | 0.072 | 0.077 |
| 8 | 0.018 | 0.025 | 0.029 | 0.035 | 0.039 | 0.043 | 0.046 |
| 12 | 0.018 | 0.025 | 0.029 | 0.035 | 0.039 | 0.043 | 0.046 |
| 11 | 0.010 | 0.013 | 0.016 | 0.019 | 0.021 | 0.023 | 0.025 |
| 13 | 0.019 | 0.026 | 0.031 | 0.036 | 0.041 | 0.045 | 0.048 |
| 9 | 0.005 | 0.007 | 0.009 | 0.010 | 0.011 | 0.013 | 0.014 |
| 19 | 0.102 | 0.137 | 0.160 | 0.189 | 0.211 | 0.231 | 0.247 |

<!-- Estadísticas: 15 filas, 8 columnas -->
<!-- Contexto posterior: -->
<!-- PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE ### 18 COMUNA DE CHILLÁN -->
<!-- FIN TABLA 11 -->


Tabla 12: Resumen de los coeficientes de rugosidad. .......................................................... 18

<!-- INICIO TABLA 12 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Chow. Los coeficientes determinados según el procedimiento anterior se muestran en la Tabla 12. -->

**Tabla 12: Resumen de los coeficientes de rugosidad.****

| Tipo de Sección | Coeficiente de Rugosidad | Descripción |
| --- | --- | --- |
| Sección en tierra | 0.035 | Cauce con pasto corto y algunas malezas. |
| Tubo de Hormigón | 0.015 | Superficie de hormigón con desgaste. |
| Tubo de HDPE | 0.012 | Superficie de HDPE con desgaste. |

<!-- Estadísticas: 3 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE ### 19 COMUNA DE CHILLÁN -->
<!-- FIN TABLA 12 -->


Tabla 13: Granulometría. ...................................................................................................... 21

<!-- INICIO TABLA 13 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- de 1 metro cercana al punto de descarga proyectado, donde se obtuvo la siguiente granulometría. -->

**Tabla 13: Granulometría.****

| Tamiz | Abertura<br>mm | % que<br>pasa |
| --- | --- | --- |
| 80.00 | 80.00 | 100.00 |
| 63.00 | 63.00 | 100.00 |
| 50.00 | 50.00 | 100.00 |
| 37.50 | 37.50 | 100.00 |
| 25.00 | 25.00 | 100.00 |
| 3/4 | 19.00 | 100.00 |
| 3/8 | 9.50 | 100.00 |
| No 4 | 4.75 | 100.00 |
| No 10 | 2.00 | 95.00 |
| No 20 | 0.85 | 83.32 |
| No 40 | 0.43 | 79.00 |
| No 60 | 0.25 | 70.00 |
| No 200 | 0.08 | 61.00 |

<!-- Estadísticas: 13 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE ### 22 COMUNA DE CHILLÁN -->
<!-- FIN TABLA 13 -->


Tabla 14: Resumen de la socavación del lecho Canal 4. ...................................................... 22

<!-- INICIO TABLA 14 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- A continuación, se muestra en la Tabla 14 los resultados que se obtuvieron para el tramo donde se contempla la modificación de cauce. -->

**Tabla 14: Resumen de la socavación del lecho Canal 4.****

| RS | Socavación máxima<br>(m) |
| --- | --- |
| 160 | 0.02 |
| 150 | 0.03 |
| 140 | 0.03 |
| 130 | 0.04 |
| 120 | 0.05 |
| 110 | 0.04 |
| 100 | 0.04 |
| 90 | 0.03 |
| 80 | 0.02 |
| 70 | 0.00 |
| 60 | 0.00 |
| 50 | 0.01 |
| 40 | 0.02 |
| 30 | 0.01 |
| 20 | 0.01 |
| 10 | 0.00 |

<!-- Estadísticas: 16 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. **Tabla 15: Resumen de la socavación del lecho Canal 2-A.** -->
<!-- FIN TABLA 14 -->


Tabla 15: Resumen de la socavación del lecho Canal 2-A................................................... 22

<!-- INICIO TABLA 15 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |20|0.01| |10|0.00| Fuente: Elaboración propia. -->

**Tabla 15: Resumen de la socavación del lecho Canal 2-A.****

| RS | Socavación máxima<br>(m) |
| --- | --- |
| 130 | 0.05 |
| 120 | 0.04 |
| 110 | 0.05 |
| 100 | 0.00 |
| 90 | 0.02 |
| 80 | 0.02 |
| 70 | 0.02 |

<!-- Estadísticas: 7 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE ### 23 -->
<!-- FIN TABLA 15 -->


Tabla 16: Variables empleadas en el cálculo de socavación por ducto. ............................... 23

<!-- INICIO TABLA 16 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- 50 Las variables y dimensiones de estas fórmulas son las mismas de la fórmula de socavación. -->

**Tabla 16: Variables empleadas en el cálculo de socavación por ducto.****

| Diámetro ducto descarga | (mm) | 1050 |
| --- | --- | --- |
| Caudal | (m~~3~~/s) | 1.207 |
| D84 | (mm) | 1.325 |
| D16 | (mm) | 0.075 |
| D50 | (mm)<br> | 0.159 |
|  |  | 4.023 |

<!-- Estadísticas: 5 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 17: Resultados cálculo de socavación por ducto.** |Autor|Socavación|Longitudi|Ancho|Tipo de Descarga| |---|---|---|---|---| -->
<!-- FIN TABLA 16 -->


Tabla 17: Resultados cálculo de socavación por ducto. ....................................................... 23

<!-- INICIO TABLA 17 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |D84|(mm)|1.325| |D16|(mm)|0.075| |D50|(mm)<br>|0.159| |||4.023| -->

**Tabla 17: Resultados cálculo de socavación por ducto.****

| Autor | Socavación | Longitudi | Ancho | Tipo de Descarga |
| --- | --- | --- | --- | --- |
| Bohan | 12.79 | 0.56 | 0.06 | hd <0.5d y hd>0.5d |
| Abt et al | 15.49 | 0.56 | 0.06 | Libre hd ≤ 0.45 |
| Abt et al Modificada | 22.32 | 0.56 | 0.06 | Libre hd ≤ 0.45d |
| Rajaratnam y Berry | 1.79 | 0.56 | 0.06 | Ahogada Q > 6.4D500.5d2 |
| Ruff et al | 21.59 | 0.56 | 0.06 | Libre hd ≤ 0.45d |
| Breusers y Raudkivi | 2.12 | 0.56 | 0.06 | Ahogada<br> |
| **PROMEDIO** | **12.69** | **0.56** | **0.06** |  |

<!-- Estadísticas: 7 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- Luego, considerando las recomendaciones del Manual de Carreteras para descargas libres, se opta por utilizar el valor de la fórmula de Abt et al Modificada, obteniendo de esta manera, -->
<!-- FIN TABLA 17 -->


Tabla 18: Parámetros de ingreso para cálculo de decantador. .............................................. 25

<!-- INICIO TABLA 18 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE ### 25 COMUNA DE CHILLÁN -->

**Tabla 18: Parámetros de ingreso para cálculo de decantador.****

| Cauce | Eficiencia<br>(n) | Q<br>(m3/s) | Diámetro partícula<br>(mm) | Reynolds |
| --- | --- | --- | --- | --- |
| Canal 2-A | 90 (%) | 0.070 | 1 | 100 |
| Canal 4 | 90 (%) | 0.162 | 1 | 100 |

<!-- Estadísticas: 2 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- Luego, se obtiene un área en planta de **3.65 m** **[2]** . Para la forma en planta del decantador, se recurre a la siguiente expresión: -->
<!-- FIN TABLA 18 -->


Tabla 19: Resultados cálculo de decantador......................................................................... 25

<!-- INICIO TABLA 19 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- H> [Q] BW [≈0.20 (m)] -->

**Tabla 19: Resultados cálculo de decantador.****

| Cauce | Área<br>(m2) | Largo<br>(m) | Ancho<br>(m) | Alto<br>(m) |
| --- | --- | --- | --- | --- |
| Canal 2-A | 3.65 | 4.27 | 0.85 | 0.14 |
| Canal 4 | 3.65 | 4.27 | 0.85 | 0.32 |

<!-- Estadísticas: 2 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- Es importante señalar que, por efectos de limpieza y vida útil de las obras decantadoras, se opta por definir una profundidad de 20 cm y 40 cm, para el Canal 2-A y Canal 4 -->
<!-- FIN TABLA 19 -->


Tabla 20: Diferencia de caudal entre la situación actual y proyectada (m [3] /s). ..................... 28

<!-- INICIO TABLA 20 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- todas las subcuencas aportantes, donde se consideró dentro de la verificación, el área del loteo en su condición urbanizada. -->

**Tabla 20: Diferencia de caudal entre la situación actual y** **proyectada (m** **[3]** **/s).****

| Condición loteo | T-10 | T-100 | T-150 |
| --- | --- | --- | --- |
| Actual (Rural) | 0.071 | 0.105 | 0.131 |
| Proyectada (Urbanizada) | 0.333 | 0.492 | 0.493 |
| **Diferencia** | 0.262 | 0.386 | 0.362 |

<!-- Estadísticas: 3 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 21: Diferencia Eje Hidráulico entre situación actual y** **proyectada T-100 años (m).** |RS|Sit. Actual|Sit. Proy.|Diferencia| |---|---|---|---| -->
<!-- FIN TABLA 20 -->


Tabla 21: Diferencia Eje Hidráulico entre situación actual y proyectada T-100 años (m). . 28

<!-- INICIO TABLA 21 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |---|---|---|---| |Actual (Rural)|0.071|0.105|0.131| |Proyectada (Urbanizada)|0.333|0.492|0.493| |**Diferencia**|0.262|0.386|0.362| -->

**Tabla 21: Diferencia Eje Hidráulico entre situación actual y** **proyectada T-100 años (m).****

| RS | Sit. Actual | Sit. Proy. | Diferencia |
| --- | --- | --- | --- |
| 70 | 154.09 | 154.18 | 0.09 |
| 60 | 154.01 | 154.09 | 0.08 |
| 50 | 153.94 | 154.01 | 0.07 |
| 40 | 153.88 | 153.95 | 0.07 |
| 30 | 153.85 | 153.92 | 0.07 |
| 20 | 153.82 | 153.89 | 0.07 |
| 10 | 153.8 | 153.87 | 0.07 |
| **PROMEDIO** | **PROMEDIO** | **PROMEDIO** | **0.07** |

<!-- Estadísticas: 8 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 22: Diferencia Eje Hidráulico entre situación actual y** **proyectada T-150 años (m).** |RS|Sit. Actual|Sit. Proy.|Diferencia| |---|---|---|---| -->
<!-- FIN TABLA 21 -->


Tabla 22: Diferencia Eje Hidráulico entre situación actual y proyectada T-150 años (m). . 28

<!-- INICIO TABLA 22 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |30|153.85|153.92|0.07| |20|153.82|153.89|0.07| |10|153.8|153.87|0.07| |**PROMEDIO**|**PROMEDIO**|**PROMEDIO**|**0.07**| -->

**Tabla 22: Diferencia Eje Hidráulico entre situación actual y** **proyectada T-150 años (m).****

| RS | Sit. Actual | Sit. Proy. | Diferencia |
| --- | --- | --- | --- |
| 70 | 154.11 | 154.21 | 0.10 |
| 60 | 154.03 | 154.11 | 0.08 |
| 50 | 153.96 | 154.03 | 0.07 |
| 40 | 153.90 | 153.97 | 0.07 |
| 30 | 153.87 | 153.94 | 0.07 |
| 20 | 153.84 | 153.91 | 0.07 |
| 10 | 153.82 | 153.89 | 0.07 |
| **PROMEDIO** | **PROMEDIO** | **PROMEDIO** | **0.08** |

<!-- Estadísticas: 8 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 23: Relación h/D Colector Canal 1 Proyectado T-100 años (m).** |Nodo EPA SWMM|Col2|Tramo|Diámetro (mm)|Tirante (m)|Relación h/D| |---|---|---|---|---|---| -->
<!-- FIN TABLA 22 -->


PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE
### iv
COMUNA DE CHILLÁN

Tabla 23: Relación h/D Colector Canal 1 Proyectado T-100 años (m). ............................... 28

<!-- INICIO TABLA 23 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |30|153.87|153.94|0.07| |20|153.84|153.91|0.07| |10|153.82|153.89|0.07| |**PROMEDIO**|**PROMEDIO**|**PROMEDIO**|**0.08**| -->

**Tabla 23: Relación h/D Colector Canal 1 Proyectado T-100 años (m).****

| Nodo EPA SWMM | Col2 | Tramo | Diámetro (mm) | Tirante (m) | Relación h/D |
| --- | --- | --- | --- | --- | --- |
| 1 | 1 (Existente) | 1 (Existente) | 800 | 0.47 | 59% |
| 2 | 3 | 2 (Proyectado) | 1050 | 0.46 | 44% |
| 3 | 4 | 3 (Proyectado) | 1050 | 0.48 | 46% |
| 4 | 5 | 4 (Proyectado) | 1050 | 0.51 | 49% |
| 5 | 6 | 5 (Proyectado) | 1050 | 0.54 | 51% |
| 6 | 7 | 6 (Proyectado) | 1050 | 0.65 | 62% |
| 7 | 17 (Muro Boca) | 7 (Proyectado) | 1050 | 0.73 | 70% |

<!-- Estadísticas: 7 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE ### 29 COMUNA DE CHILLÁN -->
<!-- FIN TABLA 23 -->


Tabla 24: Relación h/D Colector Canal 1 Proyectado T-150 años (m). ............................... 29

<!-- INICIO TABLA 24 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE ### 29 COMUNA DE CHILLÁN -->

**Tabla 24: Relación h/D Colector Canal 1 Proyectado T-150 años (m).****

| Nodo EPA SWMM | Col2 | Tramo | Diámetro (mm) | Tirante (m) | Relación h/D |
| --- | --- | --- | --- | --- | --- |
| 1 | 2 | 1 (Existente) | 800 | 0.49 | 61% |
| 2 | 3 | 2 (Proyectado) | 1050 | 0.48 | 46% |
| 3 | 4 | 3 (Proyectado) | 1050 | 0.50 | 48% |
| 4 | 5 | 4 (Proyectado) | 1050 | 0.53 | 50% |
| 5 | 6 | 5 (Proyectado) | 1050 | 0.57 | 54% |
| 6 | 7 | 6 (Proyectado) | 1050 | 0.68 | 65% |
| 7 | 17 (Muro Boca) | 7 (Proyectado) | 1050 | 0.77 | 73% |

<!-- Estadísticas: 7 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 25: Relación h/D Colector Canal 2 Proyectado T-100 años (m).** |Nodo EPA SWMM|Col2|Tramo|Diámetro (mm)|Tirante (m)|Relación h/D| |---|---|---|---|---|---| -->
<!-- FIN TABLA 24 -->


Tabla 25: Relación h/D Colector Canal 2 Proyectado T-100 años (m). ............................... 29

<!-- INICIO TABLA 25 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |4|5|4 (Proyectado)|1050|0.53|50%| |5|6|5 (Proyectado)|1050|0.57|54%| |6|7|6 (Proyectado)|1050|0.68|65%| |7|17 (Muro Boca)|7 (Proyectado)|1050|0.77|73%| -->

**Tabla 25: Relación h/D Colector Canal 2 Proyectado T-100 años (m).****

| Nodo EPA SWMM | Col2 | Tramo | Diámetro (mm) | Tirante (m) | Relación h/D |
| --- | --- | --- | --- | --- | --- |
| 15 | 14 | 1 (Existente) | 600 | 0.60 | 100% |
| 14 | 8 | 2 (Proyectado) | 800 | 0.55 | 69% |
| 8 | 7 | 3 (Proyectado) | 1050 | 0.62 | 59% |

<!-- Estadísticas: 3 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 26: Relación h/D Colector Canal 2 Proyectado T-150 años (m).** |Nodo EPA SWMM|Col2|Tramo|Diámetro (mm)|Tirante (m)|Relación h/D| |---|---|---|---|---|---| -->
<!-- FIN TABLA 25 -->


Tabla 26: Relación h/D Colector Canal 2 Proyectado T-150 años (m). ............................... 29

<!-- INICIO TABLA 26 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |---|---|---|---|---|---| |15|14|1 (Existente)|600|0.60|100%| |14|8|2 (Proyectado)|800|0.55|69%| |8|7|3 (Proyectado)|1050|0.62|59%| -->

**Tabla 26: Relación h/D Colector Canal 2 Proyectado T-150 años (m).****

| Nodo EPA SWMM | Col2 | Tramo | Diámetro (mm) | Tirante (m) | Relación h/D |
| --- | --- | --- | --- | --- | --- |
| 15 | 14 | 1 (Existente) | 600 | 0.60 | 100% |
| 14 | 8 | 2 (Proyectado) | 800 | 0.57 | 71% |
| 8 | 7 | 3 (Proyectado) | 1050 | 0.65 | 62% |

<!-- Estadísticas: 3 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE ### 30 COMUNA DE CHILLÁN -->
<!-- FIN TABLA 26 -->


PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE
### 1
COMUNA DE CHILLÁN

**1** **ANTECEDENTES** **GENERALES**

La presente solicitud de aprobación de modificación de cauce se consulta sobre tres cauces

artificiales sin nombre, siendo peticionaria la Constructora José Miguel García Ltda., RUT:

78.592.680-3, representada mediante mandato especial por el Sr. Guillermo Torres Núñez,

RUT: 14.372.323-2, ambos domiciliados para estos efectos en Calle Bernardo O ́Higgins

630, Of. 405, comuna de Concepción. El profesional patrocinante del proyecto es el

Ingeniero Civil, Sr. Richard Sepúlveda Ubilla, RUT: 16.863.644-K.

En relación a los cauces a modificar, éstos corresponden a cuerpos de agua sin nombre, los

cuales se observan que sólo conducen aguas lluvias. Su ubicación yace en el Sector Libertad

Oriente de la comuna de Chillán, provincia de Ñuble, región del Biobío.

La presente modificación de cauce nace con el proyecto de urbanización de los loteos de

viviendas sociales asociados a los Comités “Altos de Oriente II” y “Salvador Allende”, los

cuales contemplan 72 y 52 soluciones habitacionales.

En la Figura 1 se muestra esquemáticamente la ubicación del proyecto, obtenida a través de

la imagen satelital de Google Earth.

**Figura 1: Imagen representativa de la ubicación del proyecto.**

En la Figura 2 se muestra esquemáticamente los trazados actuales de los cauces en estudio,

los cuales, para efectos de presentación, se denominaron como; Canal 1, Canal 2 (dividido

para efectos de modelación como Canal 2-A, Canal 2-B) y Canal 3 (dividido para efectos de

modelación como Canal 3-A, Canal 3-B). Sobre este último, cabe aclarar que no se proyecta

realizarle intervenciones, sólo se presenta como parte del estudio.

PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE
### 2
COMUNA DE CHILLÁN

**Figura 2: Ubicación de los cauces en estudio.**

El presente informe contiene la modelación hidráulica de los cauces para la condición actual

y con proyecto, en donde se demostrará la influencia de las intervenciones que se proyectan

realizar en relación a lo actual. Este estudio se complementará con el análisis hidrológico

para los caudales máximos instantáneos asociados a los períodos de retorno de 10, 100 y 150

años, dado a los criterios de diseño establecidos por las _“Guías Metodológicas para_

_Presentación y Revisión Técnica de Proyectos de Modificación de Cauces Naturales y_

_Artificiales”_ y el Plan Maestro de Evacuación y Drenaje de Aguas Lluvias de Chillán y

Chillán Viejo.

En cuanto a la modelación hidráulica, ésta se efectuará con el software HEC RAS para la

condición actual y proyectada de los canales abiertos, mientras que, para la red de tuberías

proyectadas, tanto para el entubamiento de los canales como los colectores de aguas lluvias,

se realizará con el software EPA SWMM.

A su vez, se contempla el cálculo de socavación producido por la descarga de aguas lluvias,

el cual tendrá la finalidad de definir las dimensiones del pedraplén para proteger al terreno

de este fenómeno.

Por otro lado, en los siguientes acápites se hace una descripción de las modificaciones e

incorporaciones que contempla el proyecto.

PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE
### 3
COMUNA DE CHILLÁN

**1.1** **Descripción de las modificaciones sobre el Canal 1**

a) El entubamiento del Canal 1 entre las coordenadas E 762.276,28m; N

5.944.520,37m y E 762.273,99m; N 5.944.231,58m.

b) La eliminación del tubo existente del Canal 1 dentro de los límites del loteo,

específicamente entre las coordenadas E 762.276,28m; N 5.944.520,37m y E

762.241,50m; N 5.944.360,17m.

c) La eliminación del trazado en tierra del Canal 1 dentro de los límites del loteo,

específicamente entre las coordenadas N E 762.241,50m; N 5.944.360,17m y E

762.205,12m; N 5.944.228,72m.

d) La incorporación de un Canal en tierra inmediatamente aguas abajo al entubamiento

proyectado, el que conectará con el nuevo trazado del Canal 2-A. Este último se

proyecta su desembocadura en el trazado existente en tierra del Canal 1 a mantener,

el cual se demarca con color rojo en la Figura 3.

e) El nuevo canal en tierra descrito en el punto d) se proyecta con un ancho basal de 1

metro, taludes de 1:1, y una altura variable entre un rango de 3.40 a 3.70 metros

aproximadamente.

f) En la salida del entubamiento proyectado hacia el nuevo canal en tierra se contempla

un muro de boca y alas, revestido en el fondo con pedraplén.

**Figura 3: Descripción de las modificaciones sobre el Canal 1.**

PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE
### 4
COMUNA DE CHILLÁN

**1.2** **Descripción de las modificaciones sobre el Canal 2.**

a) El entubamiento del Canal 2-B entre las coordenadas E 762.150,06m; N

5.944.274,40m y E 762.273,93m; N 5.944.241,82m.

b) La eliminación del trazado en tierra del Canal 2-A y Canal 2-B dentro de los límites

del loteo, específicamente entre las coordenadas E 762.150,06m; N 5.944.274,40m

y E 762.213,18m; N 5.944.258,46m, respectivamente.

c) El cambio de trazado y sección del Canal 2-A, el cual captará las aguas provenientes

del Canal 1 y el nuevo cauce, denominado para estos efectos como “Canal 4”, cuya

descripción se detalla en el acápite 1.3.

**1.3** **Descripción de Canal 4 a incorporar**

Con la finalidad de captar las aguas que escurren superficialmente de oriente a poniente, y

evitar que ingresen al loteo, se proyecta un nuevo cauce denominado como “Canal 4”, en

todo el costado oriente del loteo, el cual será en tierra y sus dimensiones serán de 1 metro de

ancho basal, taludes de 1:1, y una altura variable entre un rango de 0.50 a 0.80 metros

aproximadamente.

Tal como se menciona en el punto c) del acápite 1.2, las aguas del Canal 4 desembocarán al

nuevo trazado del Canal 2-A.

A su vez, cabe señalar que el canal será revestido con pedraplén en una longitud de 20 metros

aguas arriba a la desembocadura al Canal 2-A

Las coordenadas mencionadas se encuentran en sistema UTM Datum WGS84 18H.

PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE
### 5
COMUNA DE CHILLÁN

**2** **OBJETIVOS**

**2.1** **Objetivo General**

Realizar un diseño sostenible en el tiempo, de modo que las obras proyectadas sobre los

cauces no generen un perjuicio sobre terceros o sobre el cauce como tal.

**2.2** **Objetivos Específicos**

Los objetivos específicos del proyecto son los siguientes:

 - Efectuar un análisis hidrológico, para determinar los caudales de escorrentía

superficial correspondientes a los aportes de los sectores aledaños al cauce en

cuestión.

 - Realizar un análisis hidráulico vinculado a la geomorfología del cauce, y así

determinar la capacidad hidráulica de éste para ambas situaciones.

 - Realizar una modelación de los caudales hidrológicos asociados a los periodos de

retorno 10, 100 y 150 años para determinar el comportamiento del cauce tanto para

la situación actual como proyectada.

PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE
### 6
COMUNA DE CHILLÁN

**3** **HIDROLOGÍA**

**3.1** **Consideraciones Generales**

Los análisis efectuados en el presente capítulo se basan de las indicaciones señaladas en;

_“Guías Metodológicas para Presentación y Revisión Técnica de Proyectos de_

_Modificaciones de Cauces Naturales y Artificiales_ ”, el _“Manual de Cálculo de Crecidas y_

_Caudales Mínimos en Cuencas sin información Fluviométrica”_ y el _“Plan Maestro de_

_Evacuación y Drenaje de Aguas lluvias de Chillán y Chillán Viejo”_, considerando que las

cuencas aportantes a los cauces en estudio no poseen control fluviométrico.

Específicamente, para determinar los caudales máximos instantáneos se recurre al acápite

2.5.2.2.1, punto b) de la _“Guías Metodológicas para Presentación y Revisión Técnica de_

_Proyectos de Modificaciones de Cauces Naturales y Artificiales_ ”, en donde se identifica que

para cuencas menores a 20 km [2], se podrá aplicar el Método Racional.

**3.2** **Método Racional**

El método racional supone que el escurrimiento máximo proveniente de una tormenta es

proporcional a la lluvia caída. Luego, la expresión que permite calcular los caudales máximos

instantáneos asociados a los distintos períodos de retorno es:

Q= [C∙I∙A]

3.6

Donde:

Q : Caudal máximo instantáneo asociado a los períodos de retorno (m [3] /s).

C : Coeficiente de escorrentía de la cuenca aportante.

I : Intensidad de lluvia (mm/hr).

A : Área aportante (km [2] ).

Para obtener los parámetros del método racional descritos anteriormente, se recurre al

Manual de Carreteras, donde se presenta criterios e indicaciones para determinar dichas

variables.

PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE
### 7
COMUNA DE CHILLÁN

_**3.2.1**_ _**Área Aportante**_

En relación a las áreas aportantes en estudio, se hace una diferencia entre las subcuencas que

aportan a los canales y las subcuencas que serán partes de la urbanización proyectada, para

lo cual éstas se detallan en los puntos 3.2.1.1 y 3.2.1.2 respectivamente.

_**3.2.1.1**_ _**Área Aportante a los Canales en Estudio**_

De acuerdo al proyecto de Evacuación de Aguas Lluvias Loteos Chillán 200+299+598

Viviendas, aprobado por la DOH, se han determinado las áreas aportantes a la zona de

proyecto las que se ilustran en la Figura 4, cuya lámina se adjunta en el Anexo N°3.

**Figura 4: Subcuencas aportantes a los cauces.**

PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE
### 8
COMUNA DE CHILLÁN

_**3.2.1.2**_ _**Subcuencas del loteo proyectado**_

En base al proyecto de aguas lluvias elaborado por EFEM, se definieron las subcuencas

indicadas en la Figura 5, las cuales son consideradas dentro del análisis de la situación

proyectada.

**Figura 5: Subcuencas del loteo proyectado.**

_**3.2.2**_ _**Coeficiente de Escorrentía**_

Los coeficientes de escorrentía empleados corresponden a los informados en el “Proyecto de

Evacuación de Aguas Lluvias Loteos Chillán 200+299+598 Viviendas”, aprobado por la

DOH, en el que se menciona que para la condición natural se emplea un coeficiente de 0.15,

mientras que en la condición urbanizada se utiliza un valor de 0.70. Asimismo, se identifican

dichos valores en la lámina 8/74 del Plan Maestro denominada _“Coeficientes de Escorrentías_

_Uso Actual y Futuro del Suelo (2/2)”_, donde el sector en análisis se enmarca en la zona 10D.

PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE
### 9
COMUNA DE CHILLÁN

_**3.2.3**_ _**Intensidad de precipitación**_

Las intensidades de precipitación asociadas a los distintos períodos de retorno se obtuvieron

del Cuadro N° 3.1.2-7 del Plan Maestro, el cual se detalla a continuación.

**Tabla 1: Intensidades de Precipitación para tormentas con duración menor a 120 minutos.**

|Duración<br>(min)|T=2|T=5|T=10|T=25|T=50|T=100|
|---|---|---|---|---|---|---|
|10|38.90|53.30|62.80|74.80|83.70|92.60|
|20|26.60|35.00|40.50|47.40|52.60|57.70|
|30|21.40|28.20|32.60|38.30|42.50|46.70|
|40|18.50|24.80|29.00|34.20|38.20|42.00|
|50|16.90|23.30|27.50|32.90|36.80|40.80|
|60|15.80|20.90|24.20|28.40|31.50|34.60|
|70|15.10|20.30|23.70|28.00|31.20|34.40|
|80|14.10|18.90|22.10|26.10|29.10|32.10|
|90|13.60|18.40|21.50|25.50|28.50|31.40|
|100|13.10|18.20|21.50|25.70|28.80|31.90|
|110|12.50|17.10|20.10|23.90|26.70|29.60|
|120|11.90|16.20|19.00|22.50|25.10|27.70|

_**3.2.3.1**_ _**Tiempo de Concentración**_

El tiempo de concentración del área aportante se define como el tiempo necesario para que

la partícula de agua hidráulicamente más alejada alcance la salida de la cuenca. Para evaluar

este parámetro se utiliza la expresión más representativa de las indicadas en la Tabla 2.

PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE
### 10
COMUNA DE CHILLÁN

**Tabla 2: Métodos para calcular el tiempo de concentración.**

|Método|Expresión|Condiciones de Uso|
|---|---|---|
|Norma Española<br>ó Témez|19<br>.0<br>76<br>.0<br>18<br>_S_<br>_L_<br>_Tc_<br><br>=|Para cuencas naturales de cabecera en zonas urbanas.|
|California<br>Highway and<br>Publics Works|<br><br>385<br>.0<br>3<br>57<br><br><br><br><br><br><br>=<br>_H_<br>_L_<br>_Tc_|Adaptación de la fórmula de Kirpich para cuencas de<br>montaña. Aplicable a cuencas urbanas con abundates<br>espacios libres o poco desarrollados, como parques, parcelas<br>y similares.|
|Giandotti|)<br>8.0<br>(<br>)<br>5.1<br>4<br>(<br>60<br>5.0<br>5.0<br>_Hm_<br>_L_<br>_A_<br>_Tc_<br><br><br>+<br><br><br>=<br><br><br><br>|Para cuencas menores a 200 hectáreas y con pendiente.|
|SCS (1975)|(<br>)<br>(<br>)<br>5.0<br>7.0<br>8.0<br>1900<br>9<br>1000<br>7.<br>258<br>_S_<br>_CN_<br>_L_<br>_Tc_<br><br>−<br><br>=|Desarrollada para cuencas rurales, aplicable a cuencas<br>urbanas con abundante espacios libres.|
|Kirpich (1940)|<br><br><br><br>385<br>.0<br>77<br>.0<br>0195<br>.0<br>_S_<br>_L_<br>_Tc_<br><br>=<br><br>|Desarrollada con datos SCS para áreas rurales Tennessee.<br>Aplicable a cuencas urbanas con abundantes espacios libres<br>o poco desarrollados, como parques, parcelas y similares.|
|Izzard (1946)|<br>(<br>)<br>333<br>.0<br>667<br>.0<br>33<br>.0<br>0000276<br>.0<br>28<br>.<br>525<br>_S_<br>_i_<br>_L_<br>_c_<br>_i_<br>_Tc_<br><br><br>+<br><br><br>=|Desarrollada en experimentos de laboratorio. Aplicable a<br>sectores urbanos típicos como calles, patios, pasajes, etc.|
|Federal Aviation<br>Agency (1970)|<br>(<br>)<br>333<br>.0<br>5.0<br>1.1<br>26<br>.3<br>_S_<br>_L_<br>_C_<br>_Tc_<br><br>−<br><br>=|Desarrollada para aeropuertos. Aplicable en sectores planos<br>desarrollados con poca vegetación, como estacionamientos<br>grandes, sectores de grandes industrias.|
|Morgali y Linsley<br>(1965)|3.0<br>4.0<br>6.0<br>6.0<br>7<br>_S_<br>_i_<br>_n_<br>_L_<br>_Tc_<br><br><br><br>=|Fórmula de flujo superficial. Aplicable a sectores urbanos<br>típicos como calles, patios, pasajes, etc.|

PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE
### 11
COMUNA DE CHILLÁN

Los parámetros de entrada para calcular los tiempos de concentración se muestran en la Tabla 3.

**Tabla 3: Parámetros para determinar el Tc para las áreas aportantes a los canales.**

|Cuenca|Tipo de<br>Superficie|Parámetros|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Cuenca**|**Tipo de**<br>**Superficie**|**Largo**<br>**(m)**|**Área**<br>**(km2) **|**H **<br>**(m)**|**Hm**<br>**(m)**|**CN**|**S **<br>**(m/m)**|**I **<br>**(mm/hr)**|**Coef.**<br>**Retardo**|**Coef.**<br>**Escorrentía**|**Manning**|
|A1|Urbana|225.00|0.042|1.00|0.50|92|0.004|53.00|0.012|0.70|0.03|
|A2|Rural|550.00|0.053|1.00|0.50|83|0.002|35.00|0.060|0.15|0.10|
|A3|Rural|480.00|0.061|1.00|0.50|83|0.002|41.00|0.060|0.15|0.10|
|A4|Rural|500.00|0.048|1.00|0.50|83|0.002|38.00|0.060|0.15|0.10|
|A5-1|Urbana|165.00|0.001|0.80|0.40|92|0.005|62.00|0.012|0.70|0.03|
|A5-2|Urbana|65.00|0.041|0.40|0.20|83|0.006|92.60|0.012|0.70|0.03|
|A6|Rural|410.00|0.043|1.00|0.50|83|0.002|42.00|0.060|0.15|0.10|

**Tabla 4: Tiempos de concentración de las áreas aportantes a los canales.**

|Cuenca|Tiempos de Concentración|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Método<br>Empleado|Tc (min)<br>considerado|Tc (hr)<br>considerado|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Cuenca**|**N.**<br>**Española**|**California**|**Giandotti**|**SCS**|**Kirpich**|**Izzard**|**F.**<br>**Aviation**|**Morgali**|**Morgali**|**Morgali**|**Morgali**|
|A1|16.21|10.18|122.33|24.10|10.16|18.15|118.75|22.84|Promedio:<br>Morgali e Izzard|20.49|0.34|
|A2|37.90|28.58|185.18|108.48|28.52|196.09|593.83|124.11|Promedio:<br>N. Española, y SCS|73.19|1.22|
|A3|33.30|24.42|180.72|90.88|24.37|161.66|530.17|103.06|Promedio:<br>N. Española, y SCS|62.09|1.03|
|A4|34.62|25.60|172.69|95.84|25.55|174.49|548.51|110.22|Promedio:<br>N. Española, y SCS|65.23|1.09|
|A5-1|12.60|10.00|46.68|18.01|10.00|14.60|98.79|17.35|Promedio:<br>Morgali e Izzard|15.97|0.27|
|A5-2|10.00|10.00|152.35|10.68|10.00|10.00|57.27|10.00|Promedio:<br>Morgali e Izzard|10.00|0.17|
|A6|28.67|20.35|153.62|74.04|20.31|143.36|464.93|88.57|Promedio:<br>N. Española, y SCS|51.36|0.86|

PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE
### 12
COMUNA DE CHILLÁN

Cabe mencionar que, el tiempo considerado para las subcuencas urbanizadas del futuro loteo

corresponde a 10 minutos.

De acuerdo a lo anterior, se presenta en la Tabla 5 las intensidades de precipitación asociada

a los periodos de retorno para las subcuencas que aportan a los canales.

**Tabla 5: Intensidades de Precipitación (mm/hr).**

|Cuenca|Intensidad (mm/hr)|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**Cuenca**|**T-2**|**T-5**|**T-10**|**T-25**|**T-50**|**T-100**|
|A1|27.04|35.81|41.59|48.89|54.35|59.63|
|A2|14.46|19.41|22.66|26.77|29.88|32.82|
|A3|15.67|21.01|24.51|28.94|32.28|35.46|
|A4|15.30|20.52|23.94|28.27|31.54|34.65|
|A5-1|30.57|40.37|46.84|55.00|61.10|67.02|
|A5-2|38.49|50.57|58.57|68.64|76.15|83.49|
|A6|17.21|23.02|26.83|31.66|35.29|38.76|

**3.3** **Caudales Máximos Instantáneos**

Luego de efectuado el análisis hidrológico de la cuenca en estudio, se presenta en la Tabla 6

los caudales máximos instantáneos asociados a los distintos períodos de retorno.

**Tabla 6: Caudales máximos instantáneos de las áreas aportantes a los canales (m** **[3]** **/s).**

|Cuenca|Caudales (m3/s)|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Cuenca**|**T-2**|**T-5**|**T-10**|**T-25**|**T-50**|**T-100**|**T-150**|
|A1|0.219|0.290|0.336|0.395|0.440|0.482|0.513|
|A2|0.032|0.043|0.050|0.059|0.066|0.072|0.077|
|A3|0.040|0.053|0.062|0.073|0.081|0.089|0.095|
|A4|0.031|0.041|0.048|0.057|0.063|0.070|0.074|
|A5-1|0.008|0.010|0.012|0.014|0.016|0.017|0.019|
|A5-2|0.308|0.404|0.468|0.549|0.609|0.667|0.709|
|A6|0.031|0.042|0.049|0.057|0.064|0.070|0.075|

En las Tabla 7 y Tabla 8 se presentan el resumen para los cálculos de los caudales máximos

instantáneos, tanto para las áreas aportantes a los canales a modificar como los caudales

calculados de las futuras subcuencas del loteo.

PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE
### 13
COMUNA DE CHILLÁN

**Tabla 7: Resumen de las variables para el cálculo de los caudales máximos instantáneos aportados a los canales en estudio.**

|Cuenca|Área<br>(km2)|Tipo de<br>superficie|Coeficiente<br>de<br>escorrentía|Tc<br>(min)|Intensidad (mm/hr)|Col7|Col8|Col9|Col10|Col11|Caudales (m3/s)|Col13|Col14|Col15|Col16|Col17|Col18|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Cuenca**|**Área**<br>**(km2) **|**Tipo de**<br>**superficie**|**Coeficiente**<br>**de**<br>**escorrentía**|**Tc**<br>**(min)**|**T-2**|**T-5**|**T-10**|**T-25**|**T-50**|**T-100**|**T-2**|**T-5**|**T-10**|**T-25**|**T-50**|**T-100**|**T-150**|
|A1|0.042|Urbana|0.70|20.49|27.04|35.81|41.59|48.89|54.35|59.63|0.219|0.290|0.336|0.395|0.440|0.482|0.513|
|A2|0.053|Rural|0.15|73.19|14.46|19.41|22.66|26.77|29.88|32.82|0.032|0.043|0.050|0.059|0.066|0.072|0.077|
|A3|0.061|Rural|0.15|62.09|15.67|21.01|24.51|28.94|32.28|35.46|0.040|0.053|0.062|0.073|0.081|0.089|0.095|
|A4|0.048|Rural|0.15|65.23|15.30|20.52|23.94|28.27|31.54|34.65|0.031|0.041|0.048|0.057|0.063|0.070|0.074|
|A5-1|0.001|Urbana|0.70|15.97|30.57|40.37|46.84|55.00|61.10|67.02|0.008|0.010|0.012|0.014|0.016|0.017|0.019|
|A5-2|0.041|Urbana|0.70|10.00|38.49|50.57|58.57|68.64|76.15|83.49|0.308|0.404|0.468|0.549|0.609|0.667|0.709|
|A6|0.043|Rural|0.15|51.36|17.21|23.02|26.83|31.66|35.29|38.76|0.031|0.042|0.049|0.057|0.064|0.070|0.075|

PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE
### 14
COMUNA DE CHILLÁN

**Tabla 8: Resumen de las variables para el cálculo de los caudales máximos instantáneos subcuencas del loteo.**

|Subcuenca|Área<br>ha|Área<br>km2|Coeficiente<br>de<br>escorrentía|Tc<br>(min)|Intensidad (mm/hr)|Col7|Col8|Col9|Col10|Col11|Caudales (m3/s)|Col13|Col14|Col15|Col16|Col17|Col18|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Subcuenca**|**Área**<br>**ha**|**Área**<br>**km2 **|**Coeficiente**<br>**de**<br>**escorrentía**|**Tc**<br>**(min)**|**T-2**|**T-5**|**T-10**|**T-25**|**T-50**|**T-100**|**T-2**|**T-5**|**T-10**|**T-25**|**T-50**|**T-100**|**T-150**|
|S1|0.11|0.0011|0.70|10.00|38.90|53.30|62.80|74.80|83.70|92.60|0.008|0.011|0.013|0.016|0.018|0.020|0.021|
|S2|0.11|0.0011|0.70|10.00|38.90|53.30|62.80|74.80|83.70|92.60|0.008|0.011|0.013|0.016|0.018|0.020|0.021|
|S3|0.08|0.0008|0.70|10.00|38.90|53.30|62.80|74.80|83.70|92.60|0.006|0.008|0.010|0.012|0.013|0.014|0.015|
|S4|0.03|0.0003|0.70|10.00|38.90|53.30|62.80|74.80|83.70|92.60|0.002|0.003|0.004|0.004|0.005|0.005|0.006|
|S5|0.27|0.0027|0.70|10.00|38.90|53.30|62.80|74.80|83.70|92.60|0.020|0.028|0.033|0.039|0.044|0.049|0.052|
|S6|0.14|0.0014|0.70|10.00|38.90|53.30|62.80|74.80|83.70|92.60|0.011|0.015|0.017|0.020|0.023|0.025|0.027|
|S7|0.07|0.0007|0.70|10.00|38.90|53.30|62.80|74.80|83.70|92.60|0.005|0.007|0.009|0.010|0.011|0.013|0.014|
|S8|0.06|0.0006|0.70|10.00|38.90|53.30|62.80|74.80|83.70|92.60|0.005|0.006|0.007|0.009|0.010|0.011|0.012|
|S9|0.06|0.0006|0.70|10.00|38.90|53.30|62.80|74.80|83.70|92.60|0.005|0.006|0.007|0.009|0.010|0.011|0.012|
|S10|0.25|0.0025|0.70|10.00|38.90|53.30|62.80|74.80|83.70|92.60|0.019|0.026|0.031|0.036|0.041|0.045|0.048|
|S11|0.13|0.0013|0.70|10.00|38.90|53.30|62.80|74.80|83.70|92.60|0.010|0.013|0.016|0.019|0.021|0.023|0.025|
|S12|0.24|0.0024|0.70|10.00|38.90|53.30|62.80|74.80|83.70|92.60|0.018|0.025|0.029|0.035|0.039|0.043|0.046|
|S13|0.22|0.0022|0.70|10.00|38.90|53.30|62.80|74.80|83.70|92.60|0.017|0.023|0.027|0.032|0.036|0.040|0.042|
|S14|0.07|0.0007|0.70|10.00|38.90|53.30|62.80|74.80|83.70|92.60|0.005|0.007|0.009|0.010|0.011|0.013|0.014|
|S15|0.25|0.0025|0.70|10.00|38.90|53.30|62.80|74.80|83.70|92.60|0.019|0.026|0.031|0.036|0.041|0.045|0.048|
|S16|0.11|0.0011|0.70|10.00|38.90|53.30|62.80|74.80|83.70|92.60|0.008|0.011|0.013|0.016|0.018|0.020|0.021|
|S17|0.04|0.0004|0.70|10.00|38.90|53.30|62.80|74.80|83.70|92.60|0.003|0.004|0.005|0.006|0.007|0.007|0.008|
|S18|0.05|0.0005|0.70|10.00|38.90|53.30|62.80|74.80|83.70|92.60|0.004|0.005|0.006|0.007|0.008|0.009|0.010|
|S19|0.04|0.0004|0.70|10.00|38.90|53.30|62.80|74.80|83.70|92.60|0.003|0.004|0.005|0.006|0.007|0.007|0.008|
|S20|0.14|0.0014|0.70|10.00|38.90|53.30|62.80|74.80|83.70|92.60|0.011|0.015|0.017|0.020|0.023|0.025|0.027|
|S21|0.03|0.0003|0.70|10.00|38.90|53.30|62.80|74.80|83.70|92.60|0.002|0.003|0.004|0.004|0.005|0.005|0.006|
|S22|0.06|0.0006|0.70|10.00|38.90|53.30|62.80|74.80|83.70|92.60|0.005|0.006|0.007|0.009|0.010|0.011|0.012|
|S23|0.17|0.0017|0.70|10.00|38.90|53.30|62.80|74.80|83.70|92.60|0.013|0.018|0.021|0.025|0.028|0.031|0.033|

PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE
### 15
COMUNA DE CHILLÁN

**4** **ANÁLISIS** **HIDRÁULICO**

En el presente capítulo se describen las variables para realizar la modelación hidráulica de la

situación actual como con el proyecto. Para ello se utiliza el software HEC-RAS 4.1.0 en la

situación actual y proyectada para los canales abiertos, mientras que se utiliza el software

EPA SWMM 5.0 en la red de tuberías proyectada dentro del loteo, en las que se enmarcan

los entubamientos proyectados sobre el Canal 1 y Canal 2-B y, a su vez, la red colectora de

aguas lluvias.

Para modelar al cauce se introdujeron; las condiciones de borde, la geomorfología compuesta

por la topografía del cauce, los caudales máximos instantáneos asociado a los periodos de

retorno de 10, 100 y 150 años y, finalmente los coeficientes de rugosidad de Manning

obtenidas del texto _“Hidráulica de Canales Abiertos”, Ven Te Chow_ .

**4.1** **Caudales de Modelación**

La ubicación de los caudales modelados dentro de los cauces, tanto en la situación base como

proyectada, se muestra en la Figura 6.

**Figura 6: Puntos de modelación - Situación Base.**

PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE
### 16
COMUNA DE CHILLÁN

**Figura 7: Puntos de modelación en HEC RAS - Situación Proyectada.**

**Figura 8: Puntos de modelación en EPA SWMM - Situación Proyectada.**

A continuación, en la Tabla 9 se muestran los caudales máximos instantáneos de los cauces

en los distintos puntos.

PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE
### 17
COMUNA DE CHILLÁN

**Tabla 9: Caudales Máximos Instantáneos - Situación Base en HEC RAS.**

|River|Reach|RS|T-10|T-100|T-150|
|---|---|---|---|---|---|
|CANAL 1|TRAMO 1|982|0.336|0.482|0.513|
|CANAL 1|TRAMO 1|160|0.386|0.555|0.590|
|CANAL 1|TRAMO 2|100|0.916|1.311|1.394|
|CANAL 1|TRAMO 3|70|0.977|1.398|1.487|
|CANAL 1|TRAMO 3|50|1.025|1.468|1.562|
|CANAL 2-A|CANAL 2-A|100|0.062|0.089|0.095|
|CANAL 2-B|CANAL 2-B|91.49|0.468|0.667|0.709|
|CANAL 3-A|CANAL 3-A|130|0.048|0.070|0.074|
|CANAL 3-B|CANAL 3-B|50|0.012|0.017|0.019|

**Tabla 10: Caudales Máximos Instantáneos - Situación Proyectada en HEC RAS.**

|River|Reach|RS|T-10|T-100|T-150|
|---|---|---|---|---|---|
|CANAL 1|TRAMO 1|20|1.138|1.641|1.748|
|CANAL 1|TRAMO 2|80|1.262|1.820|1.939|
|CANAL 2-A|TRAMO 1|110|0.062|0.089|0.095|
|CANAL 3-A|TRAMO 1|130|0.048|0.070|0.074|
|CANAL 3-B|TRAMO 1|50|0.012|0.017|0.019|
|CANAL 4|CANAL 4|160|0.050|0.072|0.077|

**Tabla 11: Caudales Máximos Instantáneos - Situación Proyectada en EPA SWMM.**

|CAUDALES A EPA SWMM (m3/s)|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**NODO**|**T-2**|**T-5**|**T-10**|**T-25**|**T-50**|**T-100**|**T-150**|
|1|0.219|0.290|0.336|0.395|0.440|0.482|0.513|
|2|0.008|0.011|0.013|0.016|0.018|0.020|0.021|
|4|0.017|0.023|0.027|0.032|0.036|0.040|0.042|
|5|0.045|0.062|0.073|0.087|0.098|0.108|0.116|
|6|0.019|0.026|0.031|0.036|0.041|0.045|0.048|
|7|0.017|0.023|0.027|0.032|0.036|0.040|0.042|
|15|0.308|0.404|0.468|0.549|0.609|0.667|0.709|
|14|0.030|0.041|0.049|0.058|0.065|0.072|0.077|
|8|0.018|0.025|0.029|0.035|0.039|0.043|0.046|
|12|0.018|0.025|0.029|0.035|0.039|0.043|0.046|
|11|0.010|0.013|0.016|0.019|0.021|0.023|0.025|
|13|0.019|0.026|0.031|0.036|0.041|0.045|0.048|
|9|0.005|0.007|0.009|0.010|0.011|0.013|0.014|
|19|0.102|0.137|0.160|0.189|0.211|0.231|0.247|

PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE
### 18
COMUNA DE CHILLÁN

**4.2** **Coeficiente de Rugosidad de Manning**

El coeficiente de rugosidad para la modelación del cauce se determina a partir de las

características que presenten las secciones transversales en base a una inspección visual del

terreno, describiendo las características principales de la sección de escurrimiento y

asignándole un coeficiente de acuerdo al texto “Hidráulica de Canales Abiertos”, Ven Te

Chow.

Los coeficientes determinados según el procedimiento anterior se muestran en la Tabla 12.

**Tabla 12: Resumen de los coeficientes de rugosidad.**

|Tipo de Sección|Coeficiente de Rugosidad|Descripción|
|---|---|---|
|Sección en tierra|0.035|Cauce con pasto corto y algunas malezas.|
|Tubo de Hormigón|0.015|Superficie de hormigón con desgaste.|
|Tubo de HDPE|0.012|Superficie de HDPE con desgaste.|

PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE
### 19
COMUNA DE CHILLÁN

**5** **ESTUDIO** **DE** **ARRASTRE** **DE** **SEDIMENTOS**

En el presente capítulo se presenta el estudio de socavación general (en acápite 5.1) de los

canales que se encontrarán en tierra para la situación con proyecto, con la finalidad de

determinar en primer lugar si presentan alteración del fondo y, en función de lo anterior, se

calculará los decantadores (en acápite 5.3) necesarios para atrapar los sedimentos que puedan

ingresar a las obras proyectadas.

**5.1** **SOCAVACIÓN GENERAL**

El cauce experimenta un proceso de socavación cuando ocurre una profundización de su

lecho en un determinado tramo, debido a un desequilibrio entre la tasa de entrada y salida de

sedimento desde el mencionado tramo.

En un cauce natural, el desbalance de las tasas mencionadas anteriormente varía de acuerdo

a los cambios que está sometido el caudal. Usualmente el mayor desbalance ocurre asociado

al caudal peak del hidrograma.

Es necesario mencionar que la condición más desfavorable de socavación constituye un

factor determinante en el diseño de las fundaciones de obras implementadas en el cauce. Para

determinar el mencionado fenómeno, se procede a determinar la socavación del estero

mediante el método de Lischtvan - Levediev, el cual se presenta en el acápite 5.1.1.

_**5.1.1**_ _**Método de Lischtvan - Levediev**_

En este método se estima el valor medio de la socavación general, se hace una distinción

explícita acerca del tipo de sección representativa del cauce. En efecto, el método distingue

entre un cauce con secciones bien definidas (cauce principal con planicies de inundación) de

uno con múltiples sub-secciones y brazos en estiaje. Además, el método permite estimar la

socavación general en lechos constituidos por sedimentos cohesivos a partir de una

caracterización simple de la resistencia a la erosión de este tipo de lechos.

Para el caso de cauces con sección principal y planicies de inundación, el método es aplicable

globalmente y también por franjas. Para cada una de ellas se determina la profundidad

máxima de escurrimiento, incluyendo la de la situación socavada de acuerdo con las

siguientes relaciones.

PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE
### 20
COMUNA DE CHILLÁN



 _q_ _j_ 

 .068   _D_ .028  

1

+1

_q_ _j_ _X_ +1 Sedimentos no - Cohesivos
_h_ =

_j_  .068   _D_ .028  

_q_ _j_ _X_

=

_j_  .068   _D_ .028  

=
  .028 

_X_ +




.068   _D_ .028



 _q_ _j_ 

 .060     _S_ .118   

1

+1

_X_

_q_ _j_ _X_ +1 Sedimentos Cohesivos
_h_ =

_j_  .060     _S_ .118   

_j_
_j_ = 

=
  .118 

_X_ +




.060   .118

_S_

Donde:

_h_
= Altura del escurrimiento en la franja socavada j, expresado en m. _j_

_q_ = Caudal por unidad de ancho de la franja socavada, j, en m _j_ 3 /m/s

_D_ = Diámetro medio del sedimento de la curva granulométrica, expresado en mm

 _S_ = Peso volumétrico del material seco en ton/m 3

 = Coeficiente función de la probabilidad de excedencia del caudal de diseño
 = Coeficiente que considera influencia del sedimento en suspensión

_X_ = Parámetro de la fórmula de arrastre crítico

### n = Rugosidad de Manning

_i_ = Pendiente media del lecho

Para obtener los valores de los coeficientes ,  y _X_, se deben considerar las tablas

3.707.405.A, 3.707.405.B y 3.707.405.C respectivamente del Manual de Carreteras.

**Figura 9: Esquemas para cálculo de socavación según Método de Lischtvan - Levediev.**

Fuente: Manual de Carreteras

PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE
### 21
COMUNA DE CHILLÁN

Para el caso de cauces con múltiples sub-secciones se utiliza para cada franja la siguiente

relación:



=

[]

 _q_ _j_ 

 []

_V_

 _c_ 1 [] 

.0536

_q_
_h_ =

[]

_j_

1 [] 

_j_

=

_j_  []
_V_

_c_



Donde V c1 es la velocidad crítica expresada en m/s para un escurrimiento de 1 m de

profundidad media que se obtiene de la tabla 3.707.405.D del Manual de Carreteras, para

sedimentos no cohesivos y de la tabla 3.707.405.E para sedimentos cohesivos,  tiene el

mismo significado de la fórmula para cauces con sección principal y planicies de inundación.

Es necesario mencionar que en este caso se tienen sedimentos no cohesivos.

Para el reconocimiento del suelo, se ejecutó la extracción de una muestra a una profundidad

de 1 metro cercana al punto de descarga proyectado, donde se obtuvo la siguiente

granulometría.

**Tabla 13: Granulometría.**

|Tamiz|Abertura<br>mm|% que<br>pasa|
|---|---|---|
|80.00|80.00|100.00|
|63.00|63.00|100.00|
|50.00|50.00|100.00|
|37.50|37.50|100.00|
|25.00|25.00|100.00|
|3/4|19.00|100.00|
|3/8|9.50|100.00|
|No 4|4.75|100.00|
|No 10|2.00|95.00|
|No 20|0.85|83.32|
|No 40|0.43|79.00|
|No 60|0.25|70.00|
|No 200|0.08|61.00|

PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE
### 22
COMUNA DE CHILLÁN

**Figura 10: Análisis granulométrico.**

A continuación, se muestra en la Tabla 14 los resultados que se obtuvieron para el tramo

donde se contempla la modificación de cauce.

**Tabla 14: Resumen de la socavación del lecho Canal 4.**

|RS|Socavación máxima<br>(m)|
|---|---|
|160|0.02|
|150|0.03|
|140|0.03|
|130|0.04|
|120|0.05|
|110|0.04|
|100|0.04|
|90|0.03|
|80|0.02|
|70|0.00|
|60|0.00|
|50|0.01|
|40|0.02|
|30|0.01|
|20|0.01|
|10|0.00|

Fuente: Elaboración propia.

**Tabla 15: Resumen de la socavación del lecho Canal 2-A.**

|RS|Socavación máxima<br>(m)|
|---|---|
|130|0.05|
|120|0.04|
|110|0.05|
|100|0.00|
|90|0.02|
|80|0.02|
|70|0.02|

Fuente: Elaboración propia.

PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE
### 23
COMUNA DE CHILLÁN

Considerando que, en general en ambos cauces se presentan valores no superiores a los 5 cm

de socavación para la crecida de 100 años, se propone decantadores a la entrada del tramo

entubado del Canal 1, específicamente en la captación de aguas arriba a la C.I. MDC N°8,

cuyo detalle se presenta en el plano 2-8 de la situación proyectada. El diseño de cada

decantador se ilustra en el acápite 5.3 de esta memoria de cálculo.

**5.2** **SOCAVACIÓN EN LA DESCARGA**

Para el dimensionamiento mínimo del pedraplén que protegerá al terreno de la socavación en

el pie de la descarga del entubamiento del canal 1, es necesario evaluar los efectos que se

produce el flujo que evacúa hacia cauce. Para ello, se recurre a la ec. 3.707.404(3).1 del

Manual de Carreteras:

_x_



_S_ = _A_  _Q_ _x_  _g_ + _B_
_d_ _d_ _y_ _D_ _w_

=  +

_y_

_z_

_g_

_w_

50

Las variables y dimensiones de estas fórmulas son las mismas de la fórmula de socavación.

**Tabla 16: Variables empleadas en el cálculo de socavación por ducto.**

|Diámetro ducto descarga|(mm)|1050|
|---|---|---|
|Caudal|(m~~3~~/s)|1.207|
|D84|(mm)|1.325|
|D16|(mm)|0.075|
|D50|(mm)<br>|0.159|
|||4.023|

**Tabla 17: Resultados cálculo de socavación por ducto.**

|Autor|Socavación|Longitudi|Ancho|Tipo de Descarga|
|---|---|---|---|---|
|Bohan|12.79|0.56|0.06|hd <0.5d y hd>0.5d|
|Abt et al|15.49|0.56|0.06|Libre hd ≤ 0.45|
|Abt et al Modificada|22.32|0.56|0.06|Libre hd ≤ 0.45d|
|Rajaratnam y Berry|1.79|0.56|0.06|Ahogada Q > 6.4D500.5d2|
|Ruff et al|21.59|0.56|0.06|Libre hd ≤ 0.45d|
|Breusers y Raudkivi|2.12|0.56|0.06|Ahogada<br>|
|**PROMEDIO**|**12.69**|**0.56**|**0.06**||

Luego, considerando las recomendaciones del Manual de Carreteras para descargas libres, se

opta por utilizar el valor de la fórmula de Abt et al Modificada, obteniendo de esta manera,

una profundidad de **12.69 metros de socavación**, mientras que la **longitud y ancho de**

**socavación son de 0.56 y 0.06 metros respectivamente.**

PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE
### 24
COMUNA DE CHILLÁN

**5.3** **DISEÑO DECANTADOR**

Para el diseño de los decantadores que se proyectan en los puntos de captación de cada canal,

se ha considerado lo expuesto en el manual _“Técnicas Alternativas para Soluciones de Aguas_

_Lluvias en Sectores Urbanos”_, específicamente la metodología planteada en el acápite 4.4.5,

el cual entrega la información necesaria para el dimensionamiento de este tipo de obras.

A continuación, se indica el procedimiento para el diseño de los decantadores.

1. Para determinar el área en planta se recurre a la siguiente expresión:

− [VA]

n= 1 −e

Q

Donde:

n: Eficiencia de remoción (se adopta un valor de 90%).

V: Velocidad de sedimentación (cm/s).

A: Área en planta (m [2] ) (se despeja de la ecuación).

Q: Caudal de diseño (m [3] /s) (se selecciona para estos efectos, el caudal de T=100 de la
quebrada 1).

2. La velocidad de sedimentación se obtiene de la siguiente manera:

V [2−n] = [4d] [1+n] [g][(][ρ] [s] [−ρ] [f] [)]

3Cρ f

Donde:

V: Velocidad de sedimentación (cm/s).

d: Diámetro de la partícula (cm).

g: Aceleración de gravedad (981 cm/s [2] ).

ρ s : Masa específica del sólido (2.65 T/m [3] ).

ρ f : Masa específica del fluido (1 T/m [3] ).

C= 2aR [−n]

R: Número de Reynolds R=

Vd

v

a, n: Coeficientes adimensionales que están en
función de R.

Dado lo anterior, en la Tabla 18 se detallan los
parámetros de ingreso para el cálculo de los
decantadores.

PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE
### 25
COMUNA DE CHILLÁN

**Tabla 18: Parámetros de ingreso para cálculo de decantador.**

|Cauce|Eficiencia<br>(n)|Q<br>(m3/s)|Diámetro partícula<br>(mm)|Reynolds|
|---|---|---|---|---|
|Canal 2-A|90 (%)|0.070|1|100|
|Canal 4|90 (%)|0.162|1|100|

Luego, se obtiene un área en planta de **3.65 m** **[2]** .

Para la forma en planta del decantador, se recurre a la siguiente expresión:

L
B [≥5]

Donde, L es el largo y B el ancho.

Por otro lado, la profundidad se calcula mediante la siguiente expresión:

H> [Q]

BW [≈0.20 (m)]

**Tabla 19: Resultados cálculo de decantador.**

|Cauce|Área<br>(m2)|Largo<br>(m)|Ancho<br>(m)|Alto<br>(m)|
|---|---|---|---|---|
|Canal 2-A|3.65|4.27|0.85|0.14|
|Canal 4|3.65|4.27|0.85|0.32|

Es importante señalar que, por efectos de limpieza y vida útil de las obras decantadoras, se

opta por definir una profundidad de 20 cm y 40 cm, para el Canal 2-A y Canal 4

respectivamente, superando a lo obtenido por cálculo.

Por efectos constructivos, se adopta un **largo de 4.5 metros** para ambos canales y un **ancho**

**de 2 metros** para el Canal 2-A y un **ancho de 1.50 metros** para el Canal 4, debido a su

geometría.

PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE
### 26
COMUNA DE CHILLÁN

**6** **VERIFICACIÓN** **LAGUNA** **DE** **REGULACIÓN**

Considerando que las aguas de los cauces a modificar tienen como destino la Laguna de

Regulación existente aguas abajo, en el presente capítulo se evaluará la capacidad de este

elemento para la condición con proyecto, teniendo como precedente su geometría existente

y ejecutada a la fecha, además del proyecto de aguas lluvias elaborado por EFEM y aprobado

por DOH, los cuales se adjuntan en los Anexos N°4, 5 y 9.

Como complemento de lo anterior, se indica a continuación las principales consideraciones

de la laguna existente. Se adjunta en el respaldo digital la planilla de cálculo con lo

presentado.

Terreno Total = 68.4 ha

Terreno Urb. = 19.07 ha (Contempla los nuevos proyectos)

Terreno No Urb. = 49.32 ha

Tc = 110 min 6604.22 seg

2Tc = 220 min 13208.43 seg

I 5 = 15.95 mm/hr

I 10 = 18.65 mm/hr

I 100 = 27.11 mm/hr

c tierra = 0.15

c urbano = 0.70

c ponderado = 0.30
Q 5 tierra = 0.455 m [3] /s 454.63 L/s

Q 10 tierra = 0.532 m [3] /s 531.56 L/s

Q 10 urbano = 1.075 m [3] /s 1075.02 L/s
Q 100 urbano+rural = 1.562 [m] [3] [/s] 1562.14 L/s

V estim estanque = 6806.14 m [3]

Qme = 1.562 m [3] /s 1562.14 L/s
Qevac max = 0.446 m [3] /s 445.57 L/s

t vaciado = 5.71 horas

Volumen máx requerido = 4860.32 m [3]

Largo Exist. = 60.00 m

Ancho Basal Exist. = 53.60 m

Talud = 1:1

H máx. = 1.80 m

Área Transversal Laguna = 99.72 m [2]

Volumen Exist. = 5983.2 m [3]

PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE
### 27
COMUNA DE CHILLÁN

**7** **ANÁLISIS** **DE** **RESULTADOS**

En primer lugar, es importante aclarar que, para la modelación hidráulica y estudio

hidrológico del cauce en estudio se consideraron los siguientes antecedentes:

 - Criterios de diseños propuestos por el Manual de Normas y Procedimientos para la

Administración de Recursos Hídricos.

 - Manual de Cálculo de Crecidas para Cuencas sin Información Fluviométrica.

 - Manual de Carreteras.

 - Código de Normas de Pavimentación del MINVU.

 - Técnicas Alternativas para Soluciones de Aguas Lluvias en Sectores Urbanos del

MINVU.

 - La vegetación existente a la fecha observada en terreno, considerando que este

antecedente afecta directamente a la rugosidad de los cauces.

 - La topografía del cauce y sus planicies de inundación se realizó en octubre de 2017.

 - Proyecto de Aguas Lluvias elaborado por EFEM.

En cuanto a los resultados obtenidos, se tiene lo siguiente:

 - Si bien al urbanizar el predio se está aumentando la escorrentía superficial, en la

situación con proyecto la variación del caudal representa un leve aumento en el eje

hidráulico, donde se observa que en promedio éste se eleva en 7 cm para la condición

de diseño, en el tramo del Canal 1 existente que no será intervenido (ver Tabla 21 y

Tabla 22).

 - El colector proyectado sobre el Canal 1 y el colector del Canal 2 cumplen con la

condición de diseño (T-100 años), puesto que el eje hidráulico no supera la relación

de h/D=70%, lo cual se detalla en la Tabla 23 y Tabla 25.

 - A su vez, se verificó que para el caudal con T=150 años el colector no funcionará a

presión (ver Tabla 24 y Tabla 26).

PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE
### 28
COMUNA DE CHILLÁN

 - Para evitar la socavación en el pie de la descarga del entubamiento del Canal 1 se

proyecta un revestimiento con pedraplén en el fondo canal abierto existente,

superando las dimensiones mínimas obtenidas por cálculo.

 - Por otro lado, se verificó que las dimensiones actuales de la Laguna de Regulación

existente aguas abajo tiene la capacidad de almacenar y regular las aguas lluvias de

todas las subcuencas aportantes, donde se consideró dentro de la verificación, el área

del loteo en su condición urbanizada.

**Tabla 20: Diferencia de caudal entre la situación actual y** **proyectada (m** **[3]** **/s).**

|Condición loteo|T-10|T-100|T-150|
|---|---|---|---|
|Actual (Rural)|0.071|0.105|0.131|
|Proyectada (Urbanizada)|0.333|0.492|0.493|
|**Diferencia**|0.262|0.386|0.362|

**Tabla 21: Diferencia Eje Hidráulico entre situación actual y** **proyectada T-100 años (m).**

|RS|Sit. Actual|Sit. Proy.|Diferencia|
|---|---|---|---|
|70|154.09|154.18|0.09|
|60|154.01|154.09|0.08|
|50|153.94|154.01|0.07|
|40|153.88|153.95|0.07|
|30|153.85|153.92|0.07|
|20|153.82|153.89|0.07|
|10|153.8|153.87|0.07|
|**PROMEDIO**|**PROMEDIO**|**PROMEDIO**|**0.07**|

**Tabla 22: Diferencia Eje Hidráulico entre situación actual y** **proyectada T-150 años (m).**

|RS|Sit. Actual|Sit. Proy.|Diferencia|
|---|---|---|---|
|70|154.11|154.21|0.10|
|60|154.03|154.11|0.08|
|50|153.96|154.03|0.07|
|40|153.90|153.97|0.07|
|30|153.87|153.94|0.07|
|20|153.84|153.91|0.07|
|10|153.82|153.89|0.07|
|**PROMEDIO**|**PROMEDIO**|**PROMEDIO**|**0.08**|

**Tabla 23: Relación h/D Colector Canal 1 Proyectado T-100 años (m).**

|Nodo EPA SWMM|Col2|Tramo|Diámetro (mm)|Tirante (m)|Relación h/D|
|---|---|---|---|---|---|
|1|1 (Existente)|1 (Existente)|800|0.47|59%|
|2|3|2 (Proyectado)|1050|0.46|44%|
|3|4|3 (Proyectado)|1050|0.48|46%|
|4|5|4 (Proyectado)|1050|0.51|49%|
|5|6|5 (Proyectado)|1050|0.54|51%|
|6|7|6 (Proyectado)|1050|0.65|62%|
|7|17 (Muro Boca)|7 (Proyectado)|1050|0.73|70%|

PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE
### 29
COMUNA DE CHILLÁN

**Tabla 24: Relación h/D Colector Canal 1 Proyectado T-150 años (m).**

|Nodo EPA SWMM|Col2|Tramo|Diámetro (mm)|Tirante (m)|Relación h/D|
|---|---|---|---|---|---|
|1|2|1 (Existente)|800|0.49|61%|
|2|3|2 (Proyectado)|1050|0.48|46%|
|3|4|3 (Proyectado)|1050|0.50|48%|
|4|5|4 (Proyectado)|1050|0.53|50%|
|5|6|5 (Proyectado)|1050|0.57|54%|
|6|7|6 (Proyectado)|1050|0.68|65%|
|7|17 (Muro Boca)|7 (Proyectado)|1050|0.77|73%|

**Tabla 25: Relación h/D Colector Canal 2 Proyectado T-100 años (m).**

|Nodo EPA SWMM|Col2|Tramo|Diámetro (mm)|Tirante (m)|Relación h/D|
|---|---|---|---|---|---|
|15|14|1 (Existente)|600|0.60|100%|
|14|8|2 (Proyectado)|800|0.55|69%|
|8|7|3 (Proyectado)|1050|0.62|59%|

**Tabla 26: Relación h/D Colector Canal 2 Proyectado T-150 años (m).**

|Nodo EPA SWMM|Col2|Tramo|Diámetro (mm)|Tirante (m)|Relación h/D|
|---|---|---|---|---|---|
|15|14|1 (Existente)|600|0.60|100%|
|14|8|2 (Proyectado)|800|0.57|71%|
|8|7|3 (Proyectado)|1050|0.65|62%|

PROYECTO DE MODIFICACIÓN DE CAUCE CANALES ARTIFICIALES SIN NOMBRE
### 30
COMUNA DE CHILLÁN

**8** **CONCLUSIONES**

En base a los resultados obtenidos de la modelación hidráulica y el análisis hidrológico, se

concluye que es factible ejecutar las obras sobre de descarga de aguas lluvias sobre el cauce

sin generar perjuicios a terceros, puesto que:

 Si bien se producen leves aumentos en el eje hidráulico en algunos tramos del canal

para la condición con proyecto, no se generarán desbordes sobre el cauce en todo el

tramo analizado.

 Los entubamientos proyectados sobre los Canales 1 y 2 cumplen con la condición de

diseño y verificación, en cuanto las revanchas establecidas y flujo libre.

 Se propone decantadores en las captaciones de los canales en tierra, con el fin de

retener las partículas finas que puedan alterar el ingreso del flujo de agua a las obras

proyectadas.

 Por otro lado, se propone proteger el terreno del cauce receptor al colector un

pedraplén que permitirá evitar la socavación en el punto de descarga.

 Finalmente, se verificó que la Laguna de Regulación tiene la capacidad de almacenar

y regular las aguas de las actuales áreas aportantes, considerando el área del loteo en

su condición urbanizada. Del mismo modo se evaluó que el ducto que evacúa las

aguas de la laguna regula el caudal máximo de salida, por lo que desde dicho elemento

no saldrá un caudal mayor a lo que aportan las áreas aportantes en la condición de 10

años de la situación natural o rural.

**Richard Sepúlveda Ubilla**

**RUT: 16.863.644-K**

**Ingeniero Civil**