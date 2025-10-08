---
title: Sin título
author: RGSU
date: D:20190124104202-03'00'
language: es
type: manual
pages: 20
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - “MEMORIA DE CÁLCULO MODIFICACIÓN RÍO COPIAPÓ”
-->

# “MEMORIA DE CÁLCULO MODIFICACIÓN RÍO COPIAPÓ”

## Elaborado para:

ENERO 2019

Memoria de Cáculo

Proyecto de modificación de cauce río Copiapó
Descarga Planta de Tratamiento de Aguas Servidas San Pedro

**ÍNDICE GENERAL**

**1** **ANTECEDENTES GENERALES ....................................................................................3**

**2** **OBJETIVOS ..............................................................................................................5**

**2.1** **Objetivo General.................................................................................................5**

**2.2** **Objetivos Específicos ..........................................................................................5**

**3** **HIDROLOGÍA ...........................................................................................................6**

**3.1** **Caudales Máximos Instantáneos Anuales............................................................6**

_**3.1.1**_ _**Análisis de Frecuencia ..................................................................................7**_

_**3.1.2**_ _**Calidad de Ajuste .........................................................................................8**_

**4** **HIDRÁULICA .......................................................................................................... 12**

**4.1** **Caudales de Modelación ................................................................................... 12**

**4.2** **Rugosidad de Manning ..................................................................................... 12**

**4.3** **Geomorfología del Cauce .................................................................................. 13**

**5** **ESTUDIO DE SOCAVACIÓN Y ARRASTRE DE SEDIMIENTOS ..................................... 14**

**6** **ANÁLISIS DE RESULTADOS ..................................................................................... 17**

**7** **CONCLUSIONES ..................................................................................................... 19**

1

Memoria de Cáculo

Proyecto de modificación de cauce río Copiapó
Descarga Planta de Tratamiento de Aguas Servidas San Pedro

**ÍNDICE DE FIGURAS**

Figura 1. Imagen representativa de la ubicación del estudio ................................................. 4

Figura 2. Vista río Copiapó ................................................................................................. 13

Figura 3. Áreas de inundación para T=100 años ................................................................. 18

Figura 4. Sección crítica que desborda en ribera norte del Río Copiapó ............................ 18

**ÍNDICE DE TABLAS**

Tabla 1: Caudales Máximos Anuales en la estación “Río Copiapó en Ciudad de Copiapó”. . 6

Tabla 2: Caudales máximos instantáneos en la zona de proyecto. ....................................... 7

<!-- INICIO TABLA 2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- respaldo digital se presenta la forma matemática de las distribuciones utilizadas. En la Tabla 2 se muestran las distribuciones obtenidas mediante el análisis de frecuencia. -->

**Tabla 2: Caudales máximos instantáneos en la zona de proyecto.****

| T<br>(años) | DISTRIBUCIÓN (m3/s) | Col3 | Col4 | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **T **<br>**(años)** | **Normal** | **Log Normal**<br>**2 Parámetros** | **Log Normal**<br>**3 Parámetros** | **Pearson tipo III** | **Log Pearson tipo III** | **Gumbel** |
| 100 | 25.45 | 36.92 | 38.53 | 42.59 | 223.36 | 34.35 |
| 50 | 22.91 | 25.26 | 30.59 | 32.39 | 74.28 | 29.10 |
| 25 | 20.09 | 16.57 | 23.34 | 23.08 | 24.78 | 23.82 |
| 10 | 15.73 | 8.62 | 14.68 | 12.37 | 5.79 | 16.69 |
| 5 | 11.64 | 4.67 | 8.73 | 5.78 | 1.90 | 11.05 |
| 2 | 3.81 | 1.45 | 1.31 | -0.04 | 0.40 | 2.54 |

<!-- Estadísticas: 7 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- _Fuente: Elaboración propia_ 7 -->
<!-- FIN TABLA 2 -->


Tabla 3: Parámetros para el test Chi-Cuadrado .................................................................... 8

<!-- INICIO TABLA 3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- para las distribuciones consideradas. **3.1.2.1** **Test Chi-Cuadrado** -->

**Tabla 3: Parámetros para el test Chi-Cuadrado****

| Distribución | Parámetros p | No intervalos m | m-p-1 | χ2<br>,1- |
| --- | --- | --- | --- | --- |
| Normal | 2 | 6 | 3 | 7,81 |
| Log-Normal 2 | 2 | 6 | 3 | 7,81 |
| Log-Normal 3 | 3 | 6 | 2 | 5,99 |
| Pearson III | 3 | 6 | 2 | 5,99 |
| Log-Pearson III | 3 | 6 | 2 | 5,99 |
| Gumbel | 2 | 6 | 3 | 7,81 |

<!-- Estadísticas: 6 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- _Fuente: Elaboración propia_ 8 -->
<!-- FIN TABLA 3 -->


Tabla 4: Resultados test Chi-Cuadrado.................................................................................. 9

<!-- INICIO TABLA 4 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Memoria de Cáculo Proyecto de modificación de cauce río Copiapó Descarga Planta de Tratamiento de Aguas Servidas San Pedro -->

**Tabla 4: Resultados test Chi-Cuadrado****

| No<br>rango | Límite rango | Col3 | Normal | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Log-Normal 2 | Col13 | Col14 | Col15 | Col16 | Col17 | Col18 | Col19 | Col20 | Col21 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **No**<br>**rango** | **inferior** | **superior** | **ni** | **ni** | **pi** | **pi** | **npi** | **npi** | **npi** | **ξ2 ** | **ni** | **ni** | **pi** | **pi** | **pi** | **npi** | **npi** | **npi** | **npi** | **ξ2 ** |
| 1 | -14 | -7 | 3 | 3 | 0.10 | 0.10 | 2.90 | 2.90 | 2.90 | 0.003 | 0 | 0 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.000 |
| 2 | -7 | 0 | 7 | 7 | 0.23 | 0.23 | 6.77 | 6.77 | 6.77 | 0.008 | 0 | 0 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.000 |
| 3 | 0 | 7 | 9 | 9 | 0.29 | 0.29 | 8.71 | 8.71 | 8.71 | 0.010 | 27 | 27 | 0.87 | 0.87 | 0.87 | 26.13 | 26.13 | 26.13 | 26.13 | 0.029 |
| 4 | 7 | 14 | 7 | 7 | 0.23 | 0.23 | 6.77 | 6.77 | 6.77 | 0.008 | 2 | 2 | 0.06 | 0.06 | 0.06 | 1.94 | 1.94 | 1.94 | 1.94 | 0.002 |
| 5 | 14 | 21 | 3 | 3 | 0.10 | 0.10 | 2.90 | 2.90 | 2.90 | 0.003 | 1 | 1 | 0.03 | 0.03 | 0.03 | 0.97 | 0.97 | 0.97 | 0.97 | 0.001 |
| 6 | 21 | 42 | 1 | 1 | 0.03 | 0.03 | 0.97 | 0.97 | 0.97 | 0.001 | 0 | 0 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.000 |
| **Total** | **Total** | **Total** | **30** | **30** | **0.97** | **0.97** | **29.03** | **29.03** | **29.03** | **0.032** | **30** | **30** | **0.97** | **0.97** | **0.97** | **29.03** | **29.03** | **29.03** | **29.03** | **0.032** |
| **Total** | **Total** | **Total** | **ξ2 teórico** | **ξ2 teórico** | **ξ2 teórico** | **ξ2 teórico** | **ξ2 teórico** | **ξ2 teórico** | **ξ2 teórico** | **7.81** | **ξ2 teórico** | **ξ2 teórico** | **ξ2 teórico** | **ξ2 teórico** | **ξ2 teórico** | **ξ2 teórico** | **ξ2 teórico** | **ξ2 teórico** | **ξ2 teórico** | **7.81** |
| **Total** | **Total** | **Total** | **Condición** | **Condición** | **Condición** | **Condición** | **Condición** | **Condición** | **Condición** | **CUMPLE** | **Condición** | **Condición** | **Condición** | **Condición** | **Condición** | **Condición** | **Condición** | **Condición** | **Condición** | **CUMPLE** |
| **No**<br>**rango** | **Límite rango** | **Límite rango** | **Log-Normal 3** | **Log-Normal 3** | **Log-Normal 3** | **Log-Normal 3** | **Log-Normal 3** | **Log-Normal 3** | **Log-Normal 3** | **Log-Normal 3** | **Pearson III** | **Pearson III** | **Pearson III** | **Pearson III** | **Pearson III** | **Pearson III** | **Pearson III** | **Pearson III** | **Pearson III** | **Pearson III** |
| **No**<br>**rango** | **inferior** | **superior** | **ni** | **ni** | **pi** | **pi** | **Npi** | **Npi** | **ξ2 ** | **ξ2 ** | **ni** | **ni** | **pi** | **pi** | **npi** | **npi** | **npi** | **ξ2 ** | **ξ2 ** | **ξ2 ** |
| 1 | -14 | -7 | 0 | 0 | 0.00 | 0.00 | 0.00 | 0.00 | 0.000 | 0.000 | 0 | 0 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.000 | 0.000 | 0.000 |
| 2 | -7 | 0 | 12 | 12 | 0.39 | 0.39 | 11.61 | 11.61 | 0.013 | 0.013 | 12 | 12 | 0.39 | 0.39 | 11.61 | 11.61 | 11.61 | 0.013 | 0.013 | 0.013 |
| 3 | 0 | 7 | 11 | 11 | 0.35 | 0.35 | 10.65 | 10.65 | 0.012 | 0.012 | 11 | 11 | 0.35 | 0.35 | 10.65 | 10.65 | 10.65 | 0.012 | 0.012 | 0.012 |
| 4 | 7 | 14 | 4 | 4 | 0.13 | 0.13 | 3.87 | 3.87 | 0.004 | 0.004 | 4 | 4 | 0.13 | 0.13 | 3.87 | 3.87 | 3.87 | 0.004 | 0.004 | 0.004 |
| 5 | 14 | 21 | 2 | 2 | 0.06 | 0.06 | 1.94 | 1.94 | 0.002 | 0.002 | 2 | 2 | 0.06 | 0.06 | 1.94 | 1.94 | 1.94 | 0.002 | 0.002 | 0.002 |
| 6 | 21 | 42 | 1 | 1 | 0.03 | 0.03 | 0.97 | 0.97 | 0.001 | 0.001 | 1 | 1 | 0.03 | 0.03 | 0.97 | 0.97 | 0.97 | 0.001 | 0.001 | 0.001 |
| **Total** | **Total** | **Total** | **30** | **30** | **0.97** | **0.97** | **29.03** | **29.03** | **0.032** | **0.032** | **30** | **30** | **0.97** | **0.97** | **29.03** | **29.03** | **29.03** | **0.032** | **0.032** | **0.032** |
| **Total** | **Total** | **Total** | **ξ2 teórico** | **ξ2 teórico** | **ξ2 teórico** | **ξ2 teórico** | **ξ2 teórico** | **ξ2 teórico** | **5.99** | **5.99** | **ξ2 teórico** | **ξ2 teórico** | **ξ2 teórico** | **ξ2 teórico** | **ξ2 teórico** | **ξ2 teórico** | **ξ2 teórico** | **7.81** | **7.81** | **7.81** |
| **Total** | **Total** | **Total** | **Condición** | **Condición** | **Condición** | **Condición** | **Condición** | **Condición** | **CUMPLE** | **CUMPLE** | **Condición** | **Condición** | **Condición** | **Condición** | **Condición** | **Condición** | **Condición** | **CUMPLE** | **CUMPLE** | **CUMPLE** |
| **No**<br>**rango** | **Límite rango** | **Límite rango** | **Límite rango** | **Log-Pearson III** | **Log-Pearson III** | **Log-Pearson III** | **Log-Pearson III** | **Log-Pearson III** | **Log-Pearson III** | **Log-Pearson III** | **Log-Pearson III** | **Gumbel** | **Gumbel** | **Gumbel** | **Gumbel** | **Gumbel** | **Gumbel** | **Gumbel** | **Gumbel** | **Gumbel** |
| **No**<br>**rango** | **inferior** | **superior** | **superior** | **ni** | **ni** | **pi** | **pi** | **Npi** | **Npi** | **ξ2 ** | **ξ2 ** | **ni** | **ni** | **pi** | **pi** | **pi** | **npi** | **npi** | **ξ2 ** | **ξ2 ** |
| 1 | -14 | -7 | -7 | 0 | 0 | 0.00 | 0.00 | 0.00 | 0.00 | 0.000 | 0.000 | 2 | 2 | 0.06 | 0.06 | 0.06 | 1.94 | 1.94 | 0.002 | 0.002 |
| 2 | -7 | 0 | 0 | 12 | 12 | 0.39 | 0.39 | 11.61 | 11.61 | 0.013 | 0.013 | 9 | 9 | 0.29 | 0.29 | 0.29 | 8.71 | 8.71 | 0.010 | 0.010 |
| 3 | 0 | 7 | 7 | 11 | 11 | 0.35 | 0.35 | 10.65 | 10.65 | 0.012 | 0.012 | 10 | 10 | 0.32 | 0.32 | 0.32 | 9.68 | 9.68 | 0.011 | 0.011 |
| 4 | 7 | 14 | 14 | 4 | 4 | 0.13 | 0.13 | 3.87 | 3.87 | 0.004 | 0.004 | 5 | 5 | 0.16 | 0.16 | 0.16 | 4.84 | 4.84 | 0.005 | 0.005 |
| 5 | 14 | 21 | 21 | 2 | 2 | 0.06 | 0.06 | 1.94 | 1.94 | 0.002 | 0.002 | 3 | 3 | 0.10 | 0.10 | 0.10 | 2.90 | 2.90 | 0.003 | 0.003 |
| 6 | 21 | 42 | 42 | 1 | 1 | 0.03 | 0.03 | 0.97 | 0.97 | 0.001 | 0.001 | 1 | 1 | 0.03 | 0.03 | 0.03 | 0.97 | 0.97 | 0.001 | 0.001 |
| **Total** | **Total** | **Total** | **Total** | **30** | **30** | **0.97** | **0.97** | **29.03** | **29.03** | **0.032** | **0.032** | **30** | **30** | **0.97** | **0.97** | **0.97** | **29.03** | **29.03** | **0.032** | **0.032** |
| **Total** | **Total** | **Total** | **Total** | **ξ2 teórico** | **ξ2 teórico** | **ξ2 teórico** | **ξ2 teórico** | **ξ2 teórico** | **ξ2 teórico** | **5.99** | **5.99** | **ξ2 teórico** | **ξ2 teórico** | **ξ2 teórico** | **ξ2 teórico** | **ξ2 teórico** | **ξ2 teórico** | **ξ2 teórico** | **7.81** | **7.81** |
| **Total** | **Total** | **Total** | **Total** | **Condición** | **Condición** | **Condición** | **Condición** | **Condición** | **Condición** | **CUMPLE** | **CUMPLE** | **Condición** | **Condición** | **Condición** | **Condición** | **Condición** | **Condición** | **Condición** | **CUMPLE** | **CUMPLE** |

<!-- Estadísticas: 32 filas, 21 columnas -->
<!-- Contexto posterior: -->
<!-- _Fuente: Elaboración propia_ 9 -->
<!-- FIN TABLA 4 -->


Tabla 5: Resultados test Kolmogorov-Smirnov ................................................................... 10

Tabla 6: Caudales máximos instantáneos con Distribución Log-Pearson tipo III. ............... 11

<!-- INICIO TABLA 6 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- 100 años de período de retorno, determinados mediante la distribución Log-Pearson tipo III. -->

**Tabla 6: Caudales máximos instantáneos con Distribución Log-Pearson tipo III.****

| T (años) | Q (m3/s)<br>Distribución Log Pearson tipo III |
| --- | --- |
| 100 | 223.36 |
| 50 | 74.28 |
| 25 | 24.78 |
| 10 | 5.79 |
| 5 | 1.90 |
| 2 | 0.40 |

<!-- Estadísticas: 6 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- _Fuente: Elaboración propia_ 11 -->
<!-- FIN TABLA 6 -->


Tabla 7: Caudales máximos instantáneos (m [3] /s). ............................................................... 12

<!-- INICIO TABLA 7 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Los caudales empleados en la modelación hidráulica del cauce corresponden a los obtenidos en el análisis Hidrológico antes mencionado, los cuales se indican en la Tabla 7. -->

**Tabla 7: Caudales máximos instantáneos (m** **[3]** **/s).****

| T=2 | T=5 | T=10 | T=25 | T=50 | T=100 |
| --- | --- | --- | --- | --- | --- |
| 0.40 | 1.90 | 5.79 | 24.78 | 74.28 | 223.36 |

<!-- Estadísticas: 1 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- _Fuente: Elaboración propia_ **4.2** **Rugosidad de Manning** -->
<!-- FIN TABLA 7 -->


Tabla 8: Variables empleadas en el cálculo de socavación por ducto. ............................... 16

<!-- INICIO TABLA 8 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Memoria de Cáculo Proyecto de modificación de cauce río Copiapó Descarga Planta de Tratamiento de Aguas Servidas San Pedro -->

**Tabla 8: Variables empleadas en el cálculo de socavación por ducto.****

| Diámetro ducto descarga | (mm) | 200 |
| --- | --- | --- |
| Caudal | (m3/s) | 0.0022 |
| D84 | (mm) | 7.67 |
| D16 | (mm) | 0.075 |
| D50 | (mm) | 0.0625 |
|  |  | 10.11 |

<!-- Estadísticas: 5 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- _Fuente: Elaboración propia_ **Tabla 9: Resultados cálculo de socavación por ducto.** -->
<!-- FIN TABLA 8 -->


Tabla 9: Resultados cálculo de socavación por ducto. ........................................................ 16

<!-- INICIO TABLA 9 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |D50|(mm)|0.0625| |||10.11| _Fuente: Elaboración propia_ -->

**Tabla 9: Resultados cálculo de socavación por ducto.****

| Autor | Socavación | Longitud | Ancho | Tipo de Descarga |
| --- | --- | --- | --- | --- |
| Bohan | 0.09 | 2.28 | 1.03 | hd <0.5d y hd>0.5d |
| Abt et al | 0.07 | 2.28 | 1.03 | Libre hd ≤ 0.45 |
| Abt et al Modificada | 0.10 | 2.28 | 1.03 | Libre hd ≤ 0.45d |
| Rajaratnam y Berry | -0.16 | 2.28 | 1.03 | Ahogada Q > 6.4D500.5d2 |
| Ruff et al | 0.16 | 2.28 | 1.03 | Libre hd ≤ 0.45d |
| Breusers y Raudkivi | 0.00 | 2.28 | 1.03 | Ahogada |

<!-- Estadísticas: 6 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- _Fuente: Elaboración propia_ Luego, considerando las recomendaciones del Manual de Carreteras para descargas libres, se -->
<!-- FIN TABLA 9 -->


2

Memoria de Cáculo

Proyecto de modificación de cauce río Copiapó
Descarga Planta de Tratamiento de Aguas Servidas San Pedro

**1** **ANTECEDENTES GENERALES**

El presente estudio se efectúa por solicitud de Felipe Montoya García, quien, actuando

como el asesor ambiental de la Declaración de Impacto Ambiental del proyecto de la Planta

de Tratamiento de Aguas Residuales San Pedro, requiere el proyecto de modificación de

cauce sobre el río Copiapó para la descarga de las aguas tratadas desde la Planta de

Tratamientos de Aguas Residuales San Pedro, para lo cual se contemplan los siguientes

análisis dentro del presente estudio:

- Determinación de los caudales máximos instantáneos asociados a los periodos de

retorno de 2, 5, 10, 25, 50 y 100 años en la zona de proyecto, a partir de datos

fluviométricos entregados por la estación Río Copiapó en la Ciudad de Copiapó.

- La modelación hidráulica del cauce con los caudales de crecida, para determinar la

posibilidad que se produzcan anegamientos en la Planta de Tratamientos proyectada.

La modificación de cauce del río Copiapó contempla la descarga de las aguas servidas

tratadas, provenientes de la planta de tratamiento, ubicada en la comuna de Copiapó, cuya

coordenada de la descarga corresponde al punto 348.066,71 m E; 6.975.546,05 m N, en

sistema UTM Datum WGS84 19J.

Por otro lado, se debe señalar que, para llevar a cabo los estudios antes descrito, se realizó

un levantamiento topográfico del sector en julio de 2017, donde se consideró las

singularidades existentes en terreno y en una extensión de 1000 metros aproximadamente.

La ubicación de la zona de estudio, se muestran en la Figura 1

3

Memoria de Cáculo

Proyecto de modificación de cauce río Copiapó
Descarga Planta de Tratamiento de Aguas Servidas San Pedro

**Figura 1. Imagen representativa de la ubicación del estudio**

_Fuente: Elaboración propia_

4

Memoria de Cáculo

Proyecto de modificación de cauce río Copiapó
Descarga Planta de Tratamiento de Aguas Servidas San Pedro

**2** **OBJETIVOS**

**2.1** **Objetivo General**

Realizar un diseño sostenible en el tiempo, de modo que la obra proyectada sobre el cauce

no genere un perjuicio sobre terceros o sobre el cauce como tal.

**2.2** **Objetivos Específicos**

Los objetivos específicos del proyecto son los siguientes:

- Efectuar un análisis hidrológico, para determinar los caudales máximos

instantáneos asociados a los períodos de retorno de 2, 5, 10, 20, 25, 50 y 100 años

en la zona de interés.

- Realizar un análisis hidráulico vinculado a la geomorfología del cauce, y así

determinar la capacidad hidráulica de éste y su comportamiento frente a los

caudales de crecida.

- Determinar la socavación generada sobre el cauce para la condición de diseño, y

definir el sello de fundación de la descarga desde la Planta de Tratamiento de Aguas

Servidas.

5

Memoria de Cáculo

Proyecto de modificación de cauce río Copiapó
Descarga Planta de Tratamiento de Aguas Servidas San Pedro

**3** **HIDROLOGÍA**

Los análisis efectuados en el presente capítulo se basan en las indicaciones señaladas en el

Manual de Carreteras, en los tópicos pertinentes para determinar los caudales máximos

instantáneos con datos de caudales disponibles de una estación fluviométrica.

Para el estudio hidrológico, se considera los caudales instantáneos de los últimos 30 años

hidrológicos, desde 1987 hasta 2016, que fueron registrados de la estación fluviométrica
“RIO COPIAPÓ EN CIUDAD DE COPIAPÓ”, la cual es la más cercana a la zona de estudio.

**3.1** **Caudales Máximos Instantáneos Anuales**

Para determinar los caudales máximos instantáneos anuales asociados a las crecidas con

periodo de retorno de 2, 5, 10, 25, 50 y 100 años, se recurre al registro de la estación
fluviométrica “RIO COPIAPÓ EN CIUDAD DE COPIAPÓ”, donde en la Tabla 1 se muestra los

caudales máximos instantáneos anuales de los últimos 30 años.

**Tabla 1: Caudales Máximos Anuales en la estación “Río Copiapó en Ciudad de Copiapó”.**

**Año Hidrológico** **Q (m** **[3]** **/s)** **Año Hidrológico** **Q (m** **[3]** **/s)**

1987 21.90 2002 0.27

1988 20.90 2003 0.43

1989 1.94 2004 0.25

1990 0.47 2005 0.30

1991 3.11 2006 0.21

1992 0.37 2007 0.30

1993 0.69 2008 0.41

1994 0.30 2009 0.28

1995 0.42 2010 0.49

1996 0.58 2011 0.77

1997 41.78 2012 0.33

1998 16.24 2013 0.23

1999 0.31 2014 0.05

2000 0.62 2015 0.09

2001 0.24 2016 0.14

|Año Hidrológico|Q (m3/s)|
|---|---|
|1987|21.90|
|1988|20.90|
|1989|1.94|
|1990|0.47|
|1991|3.11|
|1992|0.37|
|1993|0.69|
|1994|0.30|
|1995|0.42|
|1996|0.58|
|1997|41.78|
|1998|16.24|
|1999|0.31|
|2000|0.62|
|2001|0.24|

|Año Hidrológico|Q (m3/s)|
|---|---|
|2002|0.27|
|2003|0.43|
|2004|0.25|
|2005|0.30|
|2006|0.21|
|2007|0.30|
|2008|0.41|
|2009|0.28|
|2010|0.49|
|2011|0.77|
|2012|0.33|
|2013|0.23|
|2014|0.05|
|2015|0.09|
|2016|0.14|
|2017|1.76|

_Fuente: Elaboración propia_

En base a lo anterior, se procede a determinar la distribución estadística mediante un

análisis de frecuencia, que permita representar los caudales de crecidas asociados a los

períodos de retorno 2, 5, 10, 25, 50 y 100 años.

6

Memoria de Cáculo

Proyecto de modificación de cauce río Copiapó
Descarga Planta de Tratamiento de Aguas Servidas San Pedro

Para seleccionar la distribución estadística adecuada, se efectúa posterior al análisis de

frecuencia, los test de calidad de ajustes, los que entregan como resultado, la distribución

que más se aproxima a los datos obtenidos empíricamente. Lo mencionado anteriormente

se presenta en el acápite 3.1.1 y 3.1.2 respectivamente.

**3.1.1** **Análisis de Frecuencia**

Posterior a la transposición por áreas se realiza un análisis de frecuencia a la serie de datos,

utilizando la función DISTRIB del software de distribución libre SMADA 6.0. El programa

realiza el ajuste de las distribuciones Normal, Log-Normal de 2 parámetros, Log-Normal de

3 parámetros, Pearson tipo III, Log-Pearson tipo III de 3 parámetros y Gumbel a la serie de

datos confeccionada a través de la función de densidad de probabilidad Weibull. En el

respaldo digital se presenta la forma matemática de las distribuciones utilizadas. En la Tabla

2 se muestran las distribuciones obtenidas mediante el análisis de frecuencia.

**Tabla 2: Caudales máximos instantáneos en la zona de proyecto.**

|T<br>(años)|DISTRIBUCIÓN (m3/s)|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**T **<br>**(años)**|**Normal**|**Log Normal**<br>**2 Parámetros**|**Log Normal**<br>**3 Parámetros**|**Pearson tipo III**|**Log Pearson tipo III**|**Gumbel**|
|100|25.45|36.92|38.53|42.59|223.36|34.35|
|50|22.91|25.26|30.59|32.39|74.28|29.10|
|25|20.09|16.57|23.34|23.08|24.78|23.82|
|10|15.73|8.62|14.68|12.37|5.79|16.69|
|5|11.64|4.67|8.73|5.78|1.90|11.05|
|2|3.81|1.45|1.31|-0.04|0.40|2.54|

_Fuente: Elaboración propia_

7

Memoria de Cáculo

Proyecto de modificación de cauce río Copiapó
Descarga Planta de Tratamiento de Aguas Servidas San Pedro

**3.1.2** **Calidad de Ajuste**

Para determinar la calidad del ajuste de las distintas distribuciones de probabilidad a los

datos, se realizan las pruebas estadísticas con los métodos del test de bondad de ajuste

Chi-Cuadrado y de Kolmogorov - Smirnov.

La Tabla 3 muestra la cantidad de parámetros, intervalos y el valor Chi-Cuadrado teórico

para las distribuciones consideradas.

**3.1.2.1** **Test Chi-Cuadrado**

**Tabla 3: Parámetros para el test Chi-Cuadrado**

|Distribución|Parámetros p|No intervalos m|m-p-1|χ2<br>,1-|
|---|---|---|---|---|
|Normal|2|6|3|7,81|
|Log-Normal 2|2|6|3|7,81|
|Log-Normal 3|3|6|2|5,99|
|Pearson III|3|6|2|5,99|
|Log-Pearson III|3|6|2|5,99|
|Gumbel|2|6|3|7,81|

_Fuente: Elaboración propia_

8

Memoria de Cáculo

Proyecto de modificación de cauce río Copiapó
Descarga Planta de Tratamiento de Aguas Servidas San Pedro

**Tabla 4: Resultados test Chi-Cuadrado**

|No<br>rango|Límite rango|Col3|Normal|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Log-Normal 2|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**No**<br>**rango**|**inferior**|**superior**|**ni**|**ni**|**pi**|**pi**|**npi**|**npi**|**npi**|**ξ2 **|**ni**|**ni**|**pi**|**pi**|**pi**|**npi**|**npi**|**npi**|**npi**|**ξ2 **|
|1|-14|-7|3|3|0.10|0.10|2.90|2.90|2.90|0.003|0|0|0.00|0.00|0.00|0.00|0.00|0.00|0.00|0.000|
|2|-7|0|7|7|0.23|0.23|6.77|6.77|6.77|0.008|0|0|0.00|0.00|0.00|0.00|0.00|0.00|0.00|0.000|
|3|0|7|9|9|0.29|0.29|8.71|8.71|8.71|0.010|27|27|0.87|0.87|0.87|26.13|26.13|26.13|26.13|0.029|
|4|7|14|7|7|0.23|0.23|6.77|6.77|6.77|0.008|2|2|0.06|0.06|0.06|1.94|1.94|1.94|1.94|0.002|
|5|14|21|3|3|0.10|0.10|2.90|2.90|2.90|0.003|1|1|0.03|0.03|0.03|0.97|0.97|0.97|0.97|0.001|
|6|21|42|1|1|0.03|0.03|0.97|0.97|0.97|0.001|0|0|0.00|0.00|0.00|0.00|0.00|0.00|0.00|0.000|
|**Total**|**Total**|**Total**|**30**|**30**|**0.97**|**0.97**|**29.03**|**29.03**|**29.03**|**0.032**|**30**|**30**|**0.97**|**0.97**|**0.97**|**29.03**|**29.03**|**29.03**|**29.03**|**0.032**|
|**Total**|**Total**|**Total**|**ξ2 teórico**|**ξ2 teórico**|**ξ2 teórico**|**ξ2 teórico**|**ξ2 teórico**|**ξ2 teórico**|**ξ2 teórico**|**7.81**|**ξ2 teórico**|**ξ2 teórico**|**ξ2 teórico**|**ξ2 teórico**|**ξ2 teórico**|**ξ2 teórico**|**ξ2 teórico**|**ξ2 teórico**|**ξ2 teórico**|**7.81**|
|**Total**|**Total**|**Total**|**Condición**|**Condición**|**Condición**|**Condición**|**Condición**|**Condición**|**Condición**|**CUMPLE**|**Condición**|**Condición**|**Condición**|**Condición**|**Condición**|**Condición**|**Condición**|**Condición**|**Condición**|**CUMPLE**|
|**No**<br>**rango**|**Límite rango**|**Límite rango**|**Log-Normal 3**|**Log-Normal 3**|**Log-Normal 3**|**Log-Normal 3**|**Log-Normal 3**|**Log-Normal 3**|**Log-Normal 3**|**Log-Normal 3**|**Pearson III**|**Pearson III**|**Pearson III**|**Pearson III**|**Pearson III**|**Pearson III**|**Pearson III**|**Pearson III**|**Pearson III**|**Pearson III**|
|**No**<br>**rango**|**inferior**|**superior**|**ni**|**ni**|**pi**|**pi**|**Npi**|**Npi**|**ξ2 **|**ξ2 **|**ni**|**ni**|**pi**|**pi**|**npi**|**npi**|**npi**|**ξ2 **|**ξ2 **|**ξ2 **|
|1|-14|-7|0|0|0.00|0.00|0.00|0.00|0.000|0.000|0|0|0.00|0.00|0.00|0.00|0.00|0.000|0.000|0.000|
|2|-7|0|12|12|0.39|0.39|11.61|11.61|0.013|0.013|12|12|0.39|0.39|11.61|11.61|11.61|0.013|0.013|0.013|
|3|0|7|11|11|0.35|0.35|10.65|10.65|0.012|0.012|11|11|0.35|0.35|10.65|10.65|10.65|0.012|0.012|0.012|
|4|7|14|4|4|0.13|0.13|3.87|3.87|0.004|0.004|4|4|0.13|0.13|3.87|3.87|3.87|0.004|0.004|0.004|
|5|14|21|2|2|0.06|0.06|1.94|1.94|0.002|0.002|2|2|0.06|0.06|1.94|1.94|1.94|0.002|0.002|0.002|
|6|21|42|1|1|0.03|0.03|0.97|0.97|0.001|0.001|1|1|0.03|0.03|0.97|0.97|0.97|0.001|0.001|0.001|
|**Total**|**Total**|**Total**|**30**|**30**|**0.97**|**0.97**|**29.03**|**29.03**|**0.032**|**0.032**|**30**|**30**|**0.97**|**0.97**|**29.03**|**29.03**|**29.03**|**0.032**|**0.032**|**0.032**|
|**Total**|**Total**|**Total**|**ξ2 teórico**|**ξ2 teórico**|**ξ2 teórico**|**ξ2 teórico**|**ξ2 teórico**|**ξ2 teórico**|**5.99**|**5.99**|**ξ2 teórico**|**ξ2 teórico**|**ξ2 teórico**|**ξ2 teórico**|**ξ2 teórico**|**ξ2 teórico**|**ξ2 teórico**|**7.81**|**7.81**|**7.81**|
|**Total**|**Total**|**Total**|**Condición**|**Condición**|**Condición**|**Condición**|**Condición**|**Condición**|**CUMPLE**|**CUMPLE**|**Condición**|**Condición**|**Condición**|**Condición**|**Condición**|**Condición**|**Condición**|**CUMPLE**|**CUMPLE**|**CUMPLE**|
|**No**<br>**rango**|**Límite rango**|**Límite rango**|**Límite rango**|**Log-Pearson III**|**Log-Pearson III**|**Log-Pearson III**|**Log-Pearson III**|**Log-Pearson III**|**Log-Pearson III**|**Log-Pearson III**|**Log-Pearson III**|**Gumbel**|**Gumbel**|**Gumbel**|**Gumbel**|**Gumbel**|**Gumbel**|**Gumbel**|**Gumbel**|**Gumbel**|
|**No**<br>**rango**|**inferior**|**superior**|**superior**|**ni**|**ni**|**pi**|**pi**|**Npi**|**Npi**|**ξ2 **|**ξ2 **|**ni**|**ni**|**pi**|**pi**|**pi**|**npi**|**npi**|**ξ2 **|**ξ2 **|
|1|-14|-7|-7|0|0|0.00|0.00|0.00|0.00|0.000|0.000|2|2|0.06|0.06|0.06|1.94|1.94|0.002|0.002|
|2|-7|0|0|12|12|0.39|0.39|11.61|11.61|0.013|0.013|9|9|0.29|0.29|0.29|8.71|8.71|0.010|0.010|
|3|0|7|7|11|11|0.35|0.35|10.65|10.65|0.012|0.012|10|10|0.32|0.32|0.32|9.68|9.68|0.011|0.011|
|4|7|14|14|4|4|0.13|0.13|3.87|3.87|0.004|0.004|5|5|0.16|0.16|0.16|4.84|4.84|0.005|0.005|
|5|14|21|21|2|2|0.06|0.06|1.94|1.94|0.002|0.002|3|3|0.10|0.10|0.10|2.90|2.90|0.003|0.003|
|6|21|42|42|1|1|0.03|0.03|0.97|0.97|0.001|0.001|1|1|0.03|0.03|0.03|0.97|0.97|0.001|0.001|
|**Total**|**Total**|**Total**|**Total**|**30**|**30**|**0.97**|**0.97**|**29.03**|**29.03**|**0.032**|**0.032**|**30**|**30**|**0.97**|**0.97**|**0.97**|**29.03**|**29.03**|**0.032**|**0.032**|
|**Total**|**Total**|**Total**|**Total**|**ξ2 teórico**|**ξ2 teórico**|**ξ2 teórico**|**ξ2 teórico**|**ξ2 teórico**|**ξ2 teórico**|**5.99**|**5.99**|**ξ2 teórico**|**ξ2 teórico**|**ξ2 teórico**|**ξ2 teórico**|**ξ2 teórico**|**ξ2 teórico**|**ξ2 teórico**|**7.81**|**7.81**|
|**Total**|**Total**|**Total**|**Total**|**Condición**|**Condición**|**Condición**|**Condición**|**Condición**|**Condición**|**CUMPLE**|**CUMPLE**|**Condición**|**Condición**|**Condición**|**Condición**|**Condición**|**Condición**|**Condición**|**CUMPLE**|**CUMPLE**|

_Fuente: Elaboración propia_

9

Memoria de Cáculo

Proyecto de modificación de cauce río Copiapó
Descarga Planta de Tratamiento de Aguas Servidas San Pedro

**3.1.2.2** **Test Kolmogorv-Smirnov**

**Tabla 5: Resultados test Kolmogorov-Smirnov**

|F<br>0|P<br>0||F -P |<br>0 0|P<br>0||F -P |<br>0 0|P<br>0||F -P |<br>0 0|P<br>0||F -P |<br>0 0|P<br>0||F -P |<br>0 0|P<br>0||F -P |<br>0 0|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**F0 **|**N **|**N **|**LN 2**|**LN 2**|**LN 3**|**LN 3**|**P III**|**P III**|**LP III**|**LP III**|**G **|**G **|
|0.03|0.34|0.31|0.00|0.03|0.42|0.38|0.51|0.48|0.00|0.03|0.38|0.35|
|0.07|0.34|0.28|0.00|0.07|0.42|0.35|0.52|0.45|0.00|0.07|0.38|0.32|
|0.10|0.35|0.25|0.05|0.05|0.42|0.32|0.52|0.42|0.14|0.04|0.39|0.29|
|0.13|0.35|0.22|0.08|0.05|0.43|0.30|0.53|0.40|0.29|0.16|0.39|0.26|
|0.17|0.35|0.18|0.10|0.07|0.43|0.26|0.53|0.37|0.33|0.17|0.39|0.22|
|0.20|0.35|0.15|0.10|0.10|0.43|0.23|0.53|0.33|0.35|0.15|0.39|0.19|
|0.23|0.35|0.12|0.10|0.13|0.43|0.20|0.53|0.30|0.36|0.12|0.39|0.16|
|0.27|0.35|0.08|0.12|0.15|0.43|0.17|0.54|0.27|0.38|0.12|0.39|0.13|
|0.30|0.35|0.05|0.12|0.18|0.43|0.13|0.54|0.24|0.39|0.09|0.39|0.09|
|0.33|0.35|0.02|0.13|0.21|0.43|0.10|0.54|0.21|0.41|0.07|0.39|0.06|
|0.37|0.35|0.01|0.13|0.24|0.43|0.07|0.54|0.17|0.41|0.04|0.39|0.03|
|0.40|0.35|0.05|0.13|0.27|0.43|0.03|0.54|0.14|0.41|0.01|0.39|0.01|
|0.43|0.35|0.08|0.14|0.30|0.44|0.00|0.54|0.11|0.43|0.01|0.39|0.04|
|0.47|0.35|0.11|0.15|0.32|0.44|0.03|0.54|0.08|0.45|0.02|0.39|0.07|
|0.50|0.36|0.14|0.16|0.34|0.44|0.06|0.55|0.05|0.47|0.03|0.40|0.10|
|0.53|0.36|0.18|0.18|0.35|0.44|0.09|0.55|0.02|0.50|0.03|0.40|0.14|
|0.57|0.36|0.21|0.19|0.38|0.44|0.12|0.55|0.01|0.51|0.05|0.40|0.17|
|0.60|0.36|0.24|0.19|0.41|0.44|0.16|0.55|0.05|0.52|0.08|0.40|0.20|
|0.63|0.36|0.27|0.21|0.42|0.45|0.19|0.56|0.08|0.54|0.09|0.40|0.23|
|0.67|0.36|0.31|0.22|0.45|0.45|0.22|0.56|0.11|0.55|0.11|0.40|0.26|
|0.70|0.36|0.34|0.26|0.44|0.45|0.25|0.57|0.13|0.59|0.11|0.41|0.29|
|0.73|0.37|0.37|0.27|0.46|0.46|0.28|0.57|0.16|0.61|0.13|0.41|0.32|
|0.77|0.37|0.40|0.30|0.47|0.46|0.31|0.58|0.19|0.63|0.13|0.41|0.35|
|0.80|0.37|0.43|0.33|0.47|0.47|0.33|0.58|0.22|0.66|0.14|0.42|0.38|
|0.83|0.42|0.41|0.58|0.25|0.54|0.30|0.66|0.17|0.80|0.03|0.47|0.36|
|0.87|0.47|0.40|0.71|0.16|0.60|0.27|0.72|0.15|0.85|0.02|0.53|0.34|
|0.90|0.91|0.01|0.96|0.06|0.91|0.01|0.93|0.03|0.94|0.04|0.89|0.01|
|0.93|0.97|0.03|0.97|0.03|0.95|0.01|0.95|0.02|0.95|0.02|0.94|0.01|
|0.97|0.97|0.00|0.97|0.00|0.95|0.02|0.95|0.01|0.95|0.02|0.95|0.02|
|1.00|0.97|0.03|0.97|0.03|0.97|0.03|0.97|0.03|0.97|0.03|0.97|0.03|
||||||||||||||
|**D **||**0.428**||**0.474**||**0.385**||**0.478**||**0.165**||**0.384**|

_Fuente: Elaboración propia_

10

Memoria de Cáculo

Proyecto de modificación de cauce río Copiapó
Descarga Planta de Tratamiento de Aguas Servidas San Pedro

En atención al análisis de los gráficos que presentan el ajuste de cada distribución a los

datos, el coeficiente de determinación del ajuste, los resultados del test Chi-Cuadrado y

test Kolmogorv-Smirnov, la distribución que mejor ajusta a serie de caudales generados en

la estación “ _Río Copiapó en Ciudad de Copiapó_ ” es la distribución **Log Pearson tipo III** .

En la Tabla 6 se presentan los caudales máximos instantáneos asociados a 2, 5, 10, 25, 50 y

100 años de período de retorno, determinados mediante la distribución Log-Pearson tipo

III.

**Tabla 6: Caudales máximos instantáneos con Distribución Log-Pearson tipo III.**

|T (años)|Q (m3/s)<br>Distribución Log Pearson tipo III|
|---|---|
|100|223.36|
|50|74.28|
|25|24.78|
|10|5.79|
|5|1.90|
|2|0.40|

_Fuente: Elaboración propia_

11

Memoria de Cáculo

Proyecto de modificación de cauce río Copiapó
Descarga Planta de Tratamiento de Aguas Servidas San Pedro

**4** **HIDRÁULICA**

En el presente capítulo se describen las variables para realizar la modelación hidráulica del

río Copiapó. Para ello se utiliza el software HEC-RAS 4.1.0.

Para modelar al cauce se introdujeron; las condiciones de borde, la geomorfología

compuesta por la topografía y batimetría, los caudales máximos instantáneos y, finalmente

los coeficientes de rugosidad de Manning obtenidas del texto _“Hidráulica de Canales_

_Abiertos”, Ven Te Chow_ .

Los resultados de la modelación hidráulica, donde se detalla los niveles de aguas máximos,

velocidades medias de escurrimiento, número de Froude y otras propiedades del cauce, se

presentan en el Anexo N°1: Tablas de Resultados de la Modelación Hidráulica.

**4.1** **Caudales de Modelación**

Los caudales empleados en la modelación hidráulica del cauce corresponden a los

obtenidos en el análisis Hidrológico antes mencionado, los cuales se indican en la Tabla 7.

**Tabla 7: Caudales máximos instantáneos (m** **[3]** **/s).**

|T=2|T=5|T=10|T=25|T=50|T=100|
|---|---|---|---|---|---|
|0.40|1.90|5.79|24.78|74.28|223.36|

_Fuente: Elaboración propia_

**4.2** **Rugosidad de Manning**

Para determinar el coeficiente de rugosidad de manning se recurre a la bibliografía

“Hidráulica de Canales Abiertos, Ven Te Chow”, donde en este caso, se considera una

rugosidad de **0.035**, dado que el cauce al tener un ancho mayor a 30 m, con una sección

irregular y rugosa se asocia al valor señalado.

12

Memoria de Cáculo

Proyecto de modificación de cauce río Copiapó
Descarga Planta de Tratamiento de Aguas Servidas San Pedro

**4.3** **Geomorfología del Cauce**

Con el objeto de tener las características geomorfológicas del sector, se realizó un

levantamiento topográfico además de un levantamiento batimétrico abarcando el cauce

principal y sus planicies de inundación.

En la Figura 2 se muestra la vista obtenida de la opción _“View 3D”_ de HEC RAS 4.1.0.

**Figura 2. Vista río Copiapó**

_Fuente: Elaboración propia_

13

Memoria de Cáculo

Proyecto de modificación de cauce río Copiapó
Descarga Planta de Tratamiento de Aguas Servidas San Pedro

**5** **ESTUDIO DE SOCAVACIÓN Y ARRASTRE DE SEDIMIENTOS**

Para el dimensionamiento mínimo del pedraplén que protegerá al terreno de la socavación en el

pie de la descarga, es necesario evaluar los efectos que se produce el flujo que evacúa hacia río.

Para ello, se recurre a la ec. 3.707.404(3).1 del Manual de Carreteras:

_x_



Donde:

S : Socavación (m)

_S_  _A_  _Q_ _x_  _g_  _B_
_d_ _d_ _y_ _D_ _w_

  

_y_

_z_

_g_

_w_

50

d : Diámetro del ducto (m)

Q : Caudal total descargado (m [3] /s)

##  : Desviación estándar de sedimento del lecho erosionable =

_g_

_D_ 50 : Diámetro 50% que pasa (mm)

A, B, w, x, y, z : Parámetros definidos en la Tabla 3.707.404.F

14

Memoria de Cáculo

Proyecto de modificación de cauce río Copiapó
Descarga Planta de Tratamiento de Aguas Servidas San Pedro

De igual forma, las dimensiones en planta de la fosa de socavación, para caracterizar la longitud

y ancho de dicha fosa, se calculan considerando en base a fórmulas desarrolladas por Abt et all,

cuyas expresiones se muestran a continuación:

Para la longitud de la Fosa, _[L]_ [ (m): ] _s_

_L_ _s_ _Q_ .058
 3.9
_d_ _d_ .145

Para el ancho de la Fosa, _B_ (m): _s_

_B_ _s_ _Q_ .066
 1.4
_d_ _d_ .165

Alternativamente pueden emplearse las recomendaciones de Hoffmans:

Para la longitud de la Fosa, _L_ (m): _s_

_L_ _s_  7  _S_

Para el ancho de la Fosa, _B_ (m): _s_

_B_ _s_  5  _S_

Finalmente, para una estimación preliminar de protecciones al pie de descargas, en base a

enrocados, se puede hacer uso de la relación de Bohan, la cual se presenta a continuación:

_Q_
_De_ ,010

,010
5,1

_d_

Donde:

De : Diámetro nominal del enrocado en (m)

d : Diámetro del ducto (mm)

Q : Caudal en m [3] /s

Las variables y dimensiones de estas fórmulas son las mismas de la fórmula de socavación.

15

Memoria de Cáculo

Proyecto de modificación de cauce río Copiapó
Descarga Planta de Tratamiento de Aguas Servidas San Pedro

**Tabla 8: Variables empleadas en el cálculo de socavación por ducto.**

|Diámetro ducto descarga|(mm)|200|
|---|---|---|
|Caudal|(m3/s)|0.0022|
|D84|(mm)|7.67|
|D16|(mm)|0.075|
|D50|(mm)|0.0625|
|||10.11|

_Fuente: Elaboración propia_

**Tabla 9: Resultados cálculo de socavación por ducto.**

|Autor|Socavación|Longitud|Ancho|Tipo de Descarga|
|---|---|---|---|---|
|Bohan|0.09|2.28|1.03|hd <0.5d y hd>0.5d|
|Abt et al|0.07|2.28|1.03|Libre hd ≤ 0.45|
|Abt et al Modificada|0.10|2.28|1.03|Libre hd ≤ 0.45d|
|Rajaratnam y Berry|-0.16|2.28|1.03|Ahogada Q > 6.4D500.5d2|
|Ruff et al|0.16|2.28|1.03|Libre hd ≤ 0.45d|
|Breusers y Raudkivi|0.00|2.28|1.03|Ahogada|

_Fuente: Elaboración propia_

Luego, considerando las recomendaciones del Manual de Carreteras para descargas libres, se

opta por utilizar el valor medio de las fórmulas de Abt et al, Abt et al Modificada y Ruff et al.,

obteniendo de esta manera, una profundidad de **0.10 metros de socavación**, mientras que la

**longitud y ancho de socavación son de 2.28 y 1.03 metros respectivamente.**

16

Memoria de Cáculo

Proyecto de modificación de cauce río Copiapó
Descarga Planta de Tratamiento de Aguas Servidas San Pedro

**6** **ANÁLISIS DE RESULTADOS**

En primer lugar, es importante aclarar que, para la modelación hidráulica del cauce en estudio,

se consideraron los siguientes antecedentes:

- Los caudales máximos instantáneos considerados en el presente estudio se determinaron

a partir de 30 años de registros, de acuerdo a la metodología del Manual de Carreteras.

- La vegetación existente a la fecha observada en terreno, considerando que este

antecedente afecta directamente a la rugosidad del cauce.

- La topografía del cauce y sus planicies de inundación se realizó en julio de 2017.

En cuanto a los resultados obtenidos, se tiene lo siguiente:

- No se presente variación del eje hidráulico para los caudales analizados producto de la

descarga desde la planta de tratamiento de aguas servidas.

- En relación al sello de fundación, se definió a una profundidad de 30 cm, la cual equivale

a la mínima recomendada por el Manual de Carretera para este tipo de obras, dado que

no se genera socavación para la crecida asociada a un período de retorno de 100 años en

el tramo del río donde se proyecta la obra de descarga.

- El largo y ancho del pedraplén en el pie de la descarga se proyecta en 17.00x3.00 metros,

que superan a los valores calculados en el acápite 5, por lo que en este sentido se cumple

con la protección de la ribera del río para este fenómeno.

- El cauce en el tramo que colinda con el terreno donde se emplazará la Planta de

Tratamientos se desborda sólo para el caudal con periodo de retorno de 100 años.

- De acuerdo a lo anterior, se propone como medida preventiva, levantar el terreno donde

se emplazará la Planta de Tratamientos al menos a la cota de **227.60m**, considerando que

la cota de desborde para el T=100 años es de 226.88m, lo que equivale a una altura de

aguas de 3.59m, y para ésta, se requiere una revancha de 0.72m (20% de la altura).

17

Memoria de Cáculo

Proyecto de modificación de cauce río Copiapó
Descarga Planta de Tratamiento de Aguas Servidas San Pedro

**Figura 3. Áreas de inundación para T=100 años**

_Fuente: Elaboración propia_

**Figura 4. Sección crítica que desborda en ribera norte del Río Copiapó**

_Fuente: Elaboración propia_

18

Memoria de Cáculo

Proyecto de modificación de cauce río Copiapó
Descarga Planta de Tratamiento de Aguas Servidas San Pedro

**7** **CONCLUSIONES**

Respondiendo al objetivo de la modificación de cauce, se tiene que las obras proyectadas no

generarán perjuicios sobre terceros o al cauce como tal debido a:

- El eje hidráulico del río Copiapó no se verá afectado por el caudal de descarga proveniente

de la planta de tratamiento, dado que representa un porcentaje mínimo (casi nulo) en

relación al flujo de agua que conduce el río, considerando además la gran capacidad del

porteo de éste.

- La crecida asociada a un periodo de retorno de 100 años sobre el río Copiapó, genera

anegamiento en el terreno donde se emplazará la futura Planta de Tratamiento de Aguas

Residuales de San Pedro **.**

- Como medida de resguardo, se propone levantar el terreno a una cota mínima de 227.60

metros, con la cual se evitará anegamientos sobre la Planta de Tratamientos, asegurando

una revancha de 72 cm, equivalente al 20% de la altura de aguas para la crecida

extraordinaria de 100 años.

Cabe señalar que, bajo las restantes crecidas modeladas, equivalentes a los periodos de

retorno de 2, 5, 10, 25 y 50 años, no generan anegamientos para las condiciones actuales

del terreno de la Planta de Tratamientos.

**Richard Sepúlveda Ubilla**

**RUN: 16.863.644-K**

**Ingeniero Civil**

19