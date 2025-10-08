---
title: Tipo de Informe o Capítulo
author: Wen Rou Lee
date: D:20190605193842-04'00'
language: es
type: report
pages: 98
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Anexo 2-1B: Modelación de calidad del aire
-->

# Anexo 2-1B: Modelación de calidad del aire

## Declaración de Impacto Ambiental “Proyecto Minero 3H”

### Región de Valparaíso, Chile

Junio, 2019

Elaborado por:

**Gestión Ambiental Consultores S.A.**

General del canto 421, piso 6, Providencia

Fono: +56 2 2719 5600

www.gac.cl

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**INDICE GENERAL**

**1** **Introducción ............................................................................................................................... 5**

**2** **Objetivos .................................................................................................................................... 5**

**3** **Metodología general ................................................................................................................... 6**
**4** **CARACTERIZACIÓN METEOROLÓGICA DEL ÁREA DEL PROYECTO .................................................. 8**

4.1 Velocidad del Viento ..................................................................................................................... 9

4.2 Dirección del Viento .................................................................................................................... 11

4.3 Temperatura ................................................................................................................................ 15

**5** **caracterización calidad del aire .................................................................................................. 16**

5.1 Normativa Calidad del Aire Vigente ............................................................................................ 16

5.2 Monitoreo calidad del aire .......................................................................................................... 17

**6** **MODELO METEOROLÓGICO....................................................................................................... 20**

6.1 Justificación del Modelo Meteorológico ..................................................................................... 20

6.2 Descripción del Modelo Meteorológico ...................................................................................... 20

6.3 Dominio Modelación ................................................................................................................... 24

6.4 Topografía y Uso de Suelos ......................................................................................................... 28

6.5 Evaluación del Modelo Meteorológico ....................................................................................... 30

6.5.1 Velocidad del Viento ........................................................................................................... 32

6.5.2 Dirección del Viento ............................................................................................................ 39

6.5.3 Temperatura ........................................................................................................................ 50

6.5.4 Altura capa de mezcla en zona modelada ........................................................................... 55

6.5.1 Análisis necesidad de uso de factor de ajuste del modelo meteorológico en base a la

velocidad del viento observada y modelada ....................................................................................... 56

6.5.2 Conclusiones modelo meteorológico .................................................................................. 57

**7** **Modelo calidad del aire ............................................................................................................. 58**

7.1 Justificación modelo calidad del aire .......................................................................................... 58

7.2 Descripción modelo de calidad del aire ...................................................................................... 58

**8** **Receptores ............................................................................................................................... 60**

8.1 Receptores discretos ................................................................................................................... 60

8.2 Receptores grilla .......................................................................................................................... 62

**9** **Fuentes de emisión ................................................................................................................... 63**

**10** **Resultados ................................................................................................................................ 64**

10.1 Análisis de resultados de modelación ......................................................................................... 64

10.1.1 Aporte modelado ................................................................................................................ 64

10.1.2 Concentraciones totales ...................................................................................................... 79

10.2 Mapas de gradientes espaciales de concentración (isoconcentraciones) .................................. 82

**11** **Conclusiones modelo de calidad del aire .................................................................................... 97**

**Apéndice I: Archivos de modelación**

i

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**INDICE DE TABLAS**

Tabla 4-1: Coordenadas de ubicación de las estaciones meteorológicas. .................................................... 8

<!-- INICIO TABLA 4-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- velocidad, dirección del viento y temperatura para Nuevo Amanecer y de velocidad y dirección del viento para Catemu Meteorológica. -->

**Tabla 4-1: Coordenadas de ubicación de las estaciones meteorológicas.****

| Col1 | WGS84-Huso 19 | Col3 | Variable monitoreada |
| --- | --- | --- | --- |
| Estación | UTM - E (m) | UTM - N (m) | UTM - N (m) |
| Nuevo Amanecer | 315.243 | 6.376.191 | Viento y temperatura |
| Catemu Meteorológica | 316.480 | 6.368.520 | Viento |

<!-- Estadísticas: 3 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- (*) Huso 19S, Datum WGS84 **Figura 4.1: Ubicación de las estaciones meteorológicas.** -->
<!-- FIN TABLA 4-1 -->


Tabla 4-2: Caracterización de los datos meteorológicos, % de completitud Año 2018. ............................... 9

<!-- INICIO TABLA 4-2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- La disponibilidad de los datos registrados se presenta en la Tabla 4-2 donde se observa que se tiene sobre un 99% de disponibilidad de información, excepto para dirección del viento en Nuevo Amanecer. -->

**Tabla 4-2: Caracterización de los datos meteorológicos, % de completitud Año 2018.****

| Estación | Velocidad del<br>viento | Dirección del viento | Temperatura |
| --- | --- | --- | --- |
| Nuevo Amanecer | 99,3% | 92,0 % | 99,8 % |
| Catemu Meteorológica | 99,9% | 99,9% | - |

<!-- Estadísticas: 2 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. A continuación se presenta un resumen de los resultados del monitoreo de variables meteorológicas -->
<!-- FIN TABLA 4-2 -->


Tabla 4-3: Resumen Velocidad del viento, estaciones Nuevo Amanecer y Catemu Meteorológica. ........... 9

<!-- INICIO TABLA 4-3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- horario de 4,80 (m/s), la estación Catemu Meteorológica presenta velocidades mucho más altas con un promedio 4,07 (m/s) y un valor máximo horario mayor con 12,7 (m/s). -->

**Tabla 4-3: Resumen Velocidad del viento, estaciones Nuevo Amanecer y Catemu Meteorológica.****

| Variable | Nuevo Amanecer | Catemu Meteorológica |
| --- | --- | --- |
| Promedio (m/s) | 1,25 | 4,07 |
| Mediana (m/s) | 0,90 | 3,50 |
| Máximo (m/s) | 4,80 | 12,70 |
| Porcentaje de calmas | 26,3% | 1,7% |

<!-- Estadísticas: 4 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. La Figura 4.2 muestra el ciclo diario del viento observado en la estación Nuevo Amanecer, donde las -->
<!-- FIN TABLA 4-3 -->


Tabla 4-4: Resumen temperatura, estaciones Nuevo Amanecer. Año 2018. ............................................. 15

<!-- INICIO TABLA 4-4 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- La Tabla 4-4 muestra el resumen de los datos de temperatura en las estaciones Nuevo Amanecer. Donde la temperatura promedio es de 16,9 (°C) y el máximo anual es 38,0 (°C). -->

**Tabla 4-4: Resumen temperatura, estaciones Nuevo Amanecer. Año 2018.****

| Variable | Nuevo Amanecer |
| --- | --- |
| Promedio (°C) | 16,9 |
| Mediana (°C) | 15,6 |
| Máxima (°C) | 38,0 |
| Mínimo (°C) | 0,4 |

<!-- Estadísticas: 4 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. El ciclo diario promedio junto con su variabilidad en término de los percentiles 5 y 95 se presenta en la -->
<!-- FIN TABLA 4-4 -->


Tabla 5-1. Normas Primarias de Calidad del Aire Vigentes en Chile ........................................................... 16

Tabla 5-2: Coordenadas de ubicación de las estaciones de calidad del aire............................................... 17

<!-- INICIO TABLA 5-2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- La Tabla 5-2 y Figura 5.1 muestran las coordenadas y ubicación de las estaciones de calidad del aire consideradas. -->

**Tabla 5-2: Coordenadas de ubicación de las estaciones de calidad del aire.****

| Col1 | WGS84-Huso 19 | Col3 | Variable monitoreada |
| --- | --- | --- | --- |
| Estación | UTM - E (m) | UTM - N (m) | UTM - N (m) |
| Nuevo Amanecer | 315.243 | 6.376.191 | MP10, MP2.5, MPS |
| Catemu | 316.307 | 6.371.159 | MP10 |

<!-- Estadísticas: 3 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. **Figura 5.1: Ubicación de las estaciones de calidad del aire.** -->
<!-- FIN TABLA 5-2 -->


Tabla 5-3: Completitud datos medidos de calidad del aire año 2018. ........................................................ 18

<!-- INICIO TABLA 5-3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Anexo 2-1B: Modelación de calidad del aire DIA “Proyecto Minero 3H” -->

**Tabla 5-3: Completitud datos medidos de calidad del aire año 2018.****

| Contaminante | MP10 | MP2.5 | MPS |
| --- | --- | --- | --- |
| Nuevo Amanecer | 98% | 93% | 100% |
| Catemu | 100% | - | - |

<!-- Estadísticas: 2 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. La Tabla 5-4 muestra el promedio anual año 2018 en las estaciones Nuevo Amanecer y Catemu, donde se -->
<!-- FIN TABLA 5-3 -->


Tabla 5-4: MP10 promedio anual año 2018 ................................................................................................ 18

<!-- INICIO TABLA 5-4 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- ninguna excedencia a la norma mientras que la estación Catemu tiene un solo valor sobre 150 μg/m [3] N, ambas estaciones no exceden el umbral de la norma para el percentil 98. -->

**Tabla 5-4: MP10 promedio anual año 2018****

| Estación | Promedio<br>(μg/m3N) | Norma<br>(μg/m3N) | % de la<br>Norma Anual |
| --- | --- | --- | --- |
| Nuevo Amanecer | 45.9 | 50 | 92% |
| Catemu | 67.5 | 67.5 | 135% |

<!-- Estadísticas: 2 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. **Tabla 5-5: MP10 diario año 2018** -->
<!-- FIN TABLA 5-4 -->


Tabla 5-5: MP10 diario año 2018 ................................................................................................................ 18

<!-- INICIO TABLA 5-5 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Nuevo Amanecer|45.9|50|92%| |Catemu|67.5|67.5|135%| Fuente: Elaboración propia. -->

**Tabla 5-5: MP10 diario año 2018****

| Estación | N° Excedencia | Percentil 98 | Norma | % de la<br>Norma 24<br>horas |
| --- | --- | --- | --- | --- |
| **Estación** | **> 150 μg/m3N** | **(μg/m3N)** | **(μg/m3N)** | **(μg/m3N)** |
| Nuevo Amanecer | 0 | 93.5 | 150 | 62% |
| Catemu | 1 | 131.7 | 131.7 | 88% |

<!-- Estadísticas: 3 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. La Tabla 5-6 y Tabla 5-7 muestra el promedio anual año 2018 y promedio diario, respectivamente, para -->
<!-- FIN TABLA 5-5 -->


Tabla 5-6: MP2.5 promedio anual 2018 ...................................................................................................... 18

<!-- INICIO TABLA 5-6 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- el MP2.5 en la estación Nuevo Amanecer, donde se puede apreciar que ambas estaciones se encuentran muy per debajo del umbral de las normas respectivas. -->

**Tabla 5-6: MP2.5 promedio anual 2018****

| Estación | Promedio<br>(μg/m3N) | Norma<br>(μg/m3N) | % de la<br>Norma Anual |
| --- | --- | --- | --- |
| Nuevo Amanecer | 10.8 | 20 | 54% |

<!-- Estadísticas: 1 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. 18 -->
<!-- FIN TABLA 5-6 -->


Tabla 5-7: MP2.5 diario año 2018 ............................................................................................................... 19

<!-- INICIO TABLA 5-7 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Anexo 2-1B: Modelación de calidad del aire DIA “Proyecto Minero 3H” -->

**Tabla 5-7: MP2.5 diario año 2018****

| Estación | N° Excedencia | Percentil 98 | Norma | % de la<br>Norma 24<br>horas |
| --- | --- | --- | --- | --- |
| **Estación** | **> 50 μg/m3N** | **(μg/m3N)** | **(μg/m3N)** | **(μg/m3N)** |
| Nuevo Amanecer | 0 | 26.0 | 50 | 52% |

<!-- Estadísticas: 2 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. La Tabla 5-8 muestra el valor promedio año 2018 de MPS en estación Catemu el cual se encuentra a -->
<!-- FIN TABLA 5-7 -->


Tabla 5-8: MPS anual año 2018 ................................................................................................................... 19

<!-- INICIO TABLA 5-8 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- La Tabla 5-8 muestra el valor promedio año 2018 de MPS en estación Catemu el cual se encuentra a menos del 50 % del umbral de la norma de referencia Suiza. -->

**Tabla 5-8: MPS anual año 2018****

| Estación | Promedio<br>(mg/m2_dia) | Norma<br>(mg/m2_dia)1 | % de la<br>Norma Anual |
| --- | --- | --- | --- |
| Nuevo Amanecer | 99.2 | 200 | 49.6% |

<!-- Estadísticas: 1 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. 1 Debido a la presencia de flora y fauna nativa en los sectores cercanos al proyecto, se ha evaluado el impacto del material particulado sedimentable. Para lo anterior se consideró como referencia la norma Suiza, para valores de -->
<!-- FIN TABLA 5-8 -->


Tabla 6-1: Definición de dominio de modelación. ...................................................................................... 22

<!-- INICIO TABLA 6-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Anexo 2-1B: Modelación de calidad del aire DIA “Proyecto Minero 3H” -->

**Tabla 6-1: Definición de dominio de modelación.****

| Col1 | DX | DY | NX | NY | KMx | KMy | No Celdas |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Dominio 1 | 27 | 27 | 58 | 67 | 1566 | 1809 | 3886 |
| Dominio 2 | 9 | 9 | 55 | 64 | 495 | 576 | 3520 |
| Dominio 3 | 3 | 3 | 52 | 61 | 156 | 183 | 3172 |
| Dominio 4 | 1 | 1 | 49 | 58 | 49 | 58 | 2842 |

<!-- Estadísticas: 4 filas, 8 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. **Tabla 6-2: Definición proyección dominios de modelación.** -->
<!-- FIN TABLA 6-1 -->


Tabla 6-2: Definición proyección dominios de modelación. ....................................................................... 22

<!-- INICIO TABLA 6-2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Dominio 3|3|3|52|61|156|183|3172| |Dominio 4|1|1|49|58|49|58|2842| Fuente: Elaboración propia. -->

**Tabla 6-2: Definición proyección dominios de modelación.****

| Origen centro Dominio 1 y<br>proyección LCC | Col2 |
| --- | --- |
| ref_lat | -32,75 |
| ref_lon | -70,96 |
| truelat1 | -27,75 |
| truelat2 | -37,75 |
| stand_lon | -71,96 |

<!-- Estadísticas: 5 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. Para realizar la simulación con el modelo WRF se obtuvo la información de uso de suelos a partir de información satelital de MODIS [2] de la NASA con resolución de 15 segundos de grado, información que -->
<!-- FIN TABLA 6-2 -->


Tabla 6-3: Características del Dominio de Modelación. .............................................................................. 25

<!-- INICIO TABLA 6-3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Anexo 2-1B: Modelación de calidad del aire DIA “Proyecto Minero 3H” -->

**Tabla 6-3: Características del Dominio de Modelación.****

| Característica | Eje X (km) | Eje Y (km) |
| --- | --- | --- |
| Espaciamiento | 1 | 1 |
| Longitud | 36 | 47 |

<!-- Estadísticas: 2 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. En la Figura 6.3, se presenta el dominio de modelación utilizado en CALPUFF, donde se destacan en rojo -->
<!-- FIN TABLA 6-3 -->


Tabla 6-4. Coordenadas estaciones meteorológicas ................................................................................... 29

Tabla 6-5: Estadígrafos velocidad del viento, estaciones Nuevo Amanecer y Catemu. .............................. 39

<!-- INICIO TABLA 6-5 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Anexo 2-1B: Modelación de calidad del aire DIA “Proyecto Minero 3H” -->

**Tabla 6-5: Estadígrafos velocidad del viento, estaciones Nuevo Amanecer y Catemu.****

| Col1 | Nuevo Amanecer | Col3 | Catemu Met | Col5 |
| --- | --- | --- | --- | --- |
| **Variable** | **Observado** | **Modelado** | **Observado** | **Modelado** |
| Promedio (m/s) | 1,25 | 1,69 | 4,07 | 4,38 |
| Mediana (m/s) | 0,90 | 1,00 | 3,50 | 4,20 |
| Máximo (m/s) | 4,80 | 12,80 | 12,70 | 13,40 |
| Porcentaje de calmas | 26,3% | 40,7% | 1,7% | 9,6% |

<!-- Estadísticas: 5 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. El análisis presentado anteriormente de los datos medidos y modelados en las estaciones Nuevo -->
<!-- FIN TABLA 6-5 -->


**Tabla 6-6: Estadígrafos de desempeño velocidad del viento. Año 2018.** ................................................. 39

<!-- INICIO TABLA 6-6 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- resumen, el modelo presenta una alta concordancia con el monitoreo de velocidad del viento en estación Catemu y una concordancia media-alta en estación Nuevo Amanecer. -->

**Tabla 6-6: Estadígrafos de desempeño velocidad del viento. Año 2018.****

| Estación | n | Sesgo | FAC2 | SM | MAE | SMN | NMAE | ECM | r | IOA |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Nuevo Amanecer | 8697 | 0,44 | 0,58 | 0,45 | 0,89 | 35,9% | 71,2% | 1,38 | 0,76 | 0,44 |
| Catemu | 8753 | 0,31 | 0,68 | 0,31 | 1,59 | 7,5% | 38,9% | 1,98 | 0,77 | 0,64 |

<!-- Estadísticas: 2 filas, 11 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. ###### 6.5.2 Dirección del Viento -->
<!-- FIN TABLA 6-6 -->


**Tabla 6-7: Estadígrafos de temperatura, estación Nuevo Amanecer.** ...................................................... 53

<!-- INICIO TABLA 6-7 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- mediana respectivamente. Por otra parte, la Tabla 6-8 muestra un coeficiente de correlación (r) e índice de concordancia altos, con valores de 0,84 y 0,73 respectivamente. -->

**Tabla 6-7: Estadígrafos de temperatura, estación Nuevo Amanecer.****

| Col1 | Nuevo Amanecer | Col3 |
| --- | --- | --- |
| **Variable** | **Observado** | **Modelado** |
| Promedio (°C) | 16,9 | 18,1 |
| Mediana (°C) | 15,6 | 17,7 |
| Máximo (°C) | 38,0 | 34,3 |
| Mínimo (°C) | 0,4 | 1,3 |

<!-- Estadísticas: 5 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- 53 Anexo 2-1B: Modelación de calidad del aire -->
<!-- FIN TABLA 6-7 -->


**Tabla 6-8: Estadígrafos desempeño por temperatura, estación Nuevo Amanecer, datos observados y**

<!-- INICIO TABLA 6-8 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- DIA “Proyecto Minero 3H” Fuente: Elaboración propia -->

**Tabla 6-8: Estadígrafos desempeño por temperatura, estación Nuevo Amanecer, datos observados y modelados.****

| Estación | n | Sesgo | FAC2 | SM | MAE | SMN | NMAE | ECM | r | IOA |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Nuevo Amanecer | 8743 | 1,17 | 0,95 | 1,18 | 3,09 | 7,0% | 18,3% | 3,93 | 0,84 | 0,73 |

<!-- Estadísticas: 1 filas, 11 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia 54 -->
<!-- FIN TABLA 6-8 -->


**modelados.** ................................................................................................................................................. 54

**Tabla 6-9: Factor de corrección.** ................................................................................................................. 56

<!-- INICIO TABLA 6-9 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- la de los datos observados, tal como se muestra en la misma tabla, se desestima la necesidad de utilizar un factor de corrección en las concentraciones estimadas por el modelo. -->

**Tabla 6-9: ** **Factor de corrección** **.****

| Col1 | Nuevo Amanecer | Col3 | Catemu Met | Col5 |
| --- | --- | --- | --- | --- |
| **Variable** | **Observado** | **Modelado** | **Observado** | **Modelado** |
| Promedio (m/s) | 1,25 | 1,69 | 4,07 | 4,38 |
| Mediana (m/s) | 0,90 | 1,00 | 3,50 | 4,20 |
| Máximo (m/s) | 4,80 | 12,80 | 12,70 | 13,40 |
| Porcentaje de calmas | 26,3% | 40,7% | 1,7% | 9,6% |

<!-- Estadísticas: 5 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia 56 -->
<!-- FIN TABLA 6-9 -->


Tabla 8-1. Receptores de Interés definidos para la modelación ................................................................. 60

Tabla 9-1 Resumen de emisiones incorporadas al modelo situación actual (base). .................................. 63

Tabla 9-2 Resumen de emisiones incorporadas al modelo fase de operación. .......................................... 63
Tabla 10-1 Resultados del modelo para el aporte del proyecto en situación actual (base) [μg/m [3] ]. ........ 66
Tabla 10-2 Resultados del modelo para el aporte del proyecto en fase operación futura [μg/m [3] ]. .......... 68

Tabla 10-3 Resultados del modelo para el delta operación futura en relación a la operación actual

[μg/m [3] ]. ....................................................................................................................................................... 71

Tabla 10-4 Porcentaje del delta operación futura en relación a la operación actual respecto a la norma. 73

Tabla 10-5 Porcentaje del modelo para el aporte del proyecto en fase operación futura respecto a la

norma. ......................................................................................................................................................... 76

Tabla 10-6 Concentraciones totales MP10 anual, aporte del Proyecto en la fase de operación futura. ... 80

Tabla 10-7 Concentraciones totales MP10 diario, aporte del Proyecto en la fase de operación futura. ... 80

Tabla 10-8 Concentraciones totales MP2,5 anual, aporte del Proyecto en la fase de operación futura. .. 80

Tabla 10-9 Concentraciones totales MP2,5 diario, aporte del Proyecto en la fase de operación futura. .. 80

Tabla 10-10 Depositación total MPS anual, aporte del Proyecto en la fase de operación futura. ............. 81

ii

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**INDICE DE FIGURAS**

Figura 3-1. Pasos Metodológicos .................................................................................................................. 7

Figura 4.1: Ubicación de las estaciones meteorológicas. .............................................................................. 8

Figura 4.2: Ciclo diario de la velocidad del viento observada. Estación Nuevo Amanecer. Año 2018. ...... 10

Figura 4.3: Ciclo diario de la velocidad del viento observada. Estación Catemu Meteorológica. Año 2018

..................................................................................................................................................................... 10

Figura 4.4: Rosas de viento observado. Estación Nuevo Amanecer. Año 2018. ......................................... 11

Figura 4.5: Ciclo Diario de la Dirección del Viento Observada. Estación Nuevo Amanecer. Año 2018. ..... 12

Figura 4.6: Ciclo estacional de la dirección y velocidad del viento observada. Estación Nuevo Amanecer.

Año 2018. .................................................................................................................................................... 12

Figura 4.7: Rosas de viento observado. Estación Catemu Meteorológica. Año 2018. ................................ 13

Figura 4.8: Ciclo diario de la dirección del viento observada. Estación Catemu Meteorológica. Año 2018.

..................................................................................................................................................................... 14

Figura 4.9: Ciclo estacional de la dirección y velocidad del viento observada. Estación Catemu

Meteorológica. Año 2018. ........................................................................................................................... 14

Figura 4.10: Ciclo diario de temperatura observada. Estación Nuevo Amanecer. Año 2018. .................... 15

Figura 5.1: Ubicación de las estaciones de calidad del aire. ....................................................................... 17

Figura 6.1: Extensiones de los dominios 1, 2, 3 y 4 en WRF. ...................................................................... 21

Figura 6.2: Uso de suelo dominio 4 WRF. ................................................................................................... 24

Figura 6.3: Dominio de Modelación del Proyecto. ...................................................................................... 26

Figura 6.4: Dominio de Modelación del Proyecto y límites comunales. ..................................................... 27

Figura 6.5: Topografía del dominio de modelación. ................................................................................... 29

Figura 6.6: Ciclo diario de la velocidad del viento modelada y observada. Estación Nuevo Amanecer, año

2018. ............................................................................................................................................................ 33

Figura 6.7: Ciclo mensual de la velocidad del viento modelada y observada. Estación Nuevo Amanecer,

año 2018. ..................................................................................................................................................... 34

Figura 6.8: Cuantiles condicionales e histograma de velocidad del viento observada y modelada, estación

Nuevo Amanecer, año 2018. ....................................................................................................................... 35

Figura 6.9: Ciclo diario de la velocidad del viento modelada y observada. Estación Catemu, año 2018. .. 36

Figura 6.10: Ciclo mensual de la velocidad del viento modelada y observada. Estación Catemu, año 2018.

..................................................................................................................................................................... 37

Figura 6.11: Cuantiles condicionales e histograma de velocidad del viento observada y modelada,

estación Catemu, año 2018. ........................................................................................................................ 38

Figura 6.12: Rosa de los vientos observada y modelada año 2018. Estación Nuevo Amanecer. ............... 40

Figura 6.13: Rosa de los vientos observada años 2014 al 2018. Estación Nuevo Amanecer. ..................... 41

Figura 6.14: Gráfico polar con frecuencia de desviación entre direcciones de viento modeladas y

observadas por intervalos de diferencia en magnitud de velocidad del viento. Estación Nuevo Amanecer.

Año 2018. .................................................................................................................................................... 42

Figura 6.15: Ciclo diario de la dirección del viento observada. Estación Nuevo Amanecer. Año 2018. ..... 43

Figura 6.16: Ciclo diario de la dirección del viento modelada. Estación Nuevo Amanecer. Año 2018. ...... 43

iii

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

Figura 6.17: Ciclo estacional de la dirección y velocidad del viento observada. Estación Nuevo Amanecer.

Año 2018. .................................................................................................................................................... 44

Figura 6.18: Ciclo estacional de la dirección y velocidad del viento modelada. Estación Nuevo Amanecer.

Año 2018. .................................................................................................................................................... 45

Figura 6.19: Rosa de los vientos observada y modelada año 2018. Estación Catemu. .............................. 46

Figura 6.20: Gráfico polar con frecuencia de desviación entre direcciones de viento modeladas y

observadas por intervalos de diferencia en magnitud de velocidad del viento. Estación Catemu. Año

2018. ............................................................................................................................................................ 47

Figura 6.21: Ciclo diario de la dirección del viento observada. Estación Catemu. Año 2018. .................... 48

Figura 6.22: Ciclo diario de la dirección del viento modelada. Estación Catemu. Año 2018. ..................... 48

Figura 6.23: Ciclo estacional de la dirección y velocidad del viento observada. Estación Catemu. Año

2018. ............................................................................................................................................................ 49

Figura 6.24: Ciclo estacional de la dirección y velocidad del viento modelada. Estación Catemu. Año 2018.

..................................................................................................................................................................... 50

**Figura 6-25: Ciclo diario de la temperatura modelada y observada, Estación Nuevo Amanecer. Año**

**2018.** ............................................................................................................................................................ 51

**Figura 6-26: Ciclo mensual de la temperatura modelada y observada, Estación Nuevo Amanecer, año**

**2018.** ............................................................................................................................................................ 52

Figura 6.27: Cuantiles condicionales e histograma de velocidad del viento observada y modelada,

estación Catemu, año 2018. ........................................................................................................................ 53

Figura 6.28: Ciclo diario modelado altura de capa de mezcla. Estación Nuevo Amanecer. Año 2018. ...... 55

Figura 8-1. Grilla de receptores ................................................................................................................... 62

Figura 9-1. Fuentes emisoras ingresadas al modelo ................................................................................... 64

Figura 10-1. Isoconcentraciones fase de operación actual: MP10 Anual ................................................... 83

Figura 10-2. Isoconcentraciones fase de operación futura: MP10 Anual ................................................... 84

Figura 10-3. Isoconcentraciones fase de operación actual: MP10 Diario ................................................... 85

Figura 10-4. Isoconcentraciones fase de operación futura: MP10 Diario ................................................... 86

Figura 10-5. Isoconcentraciones fase de operación actual: MP2,5 Anual .................................................. 87

Figura 10-6. Isoconcentraciones fase de operación futura: MP2,5 Anual .................................................. 88

Figura 10-7. Isoconcentraciones fase de operación actual: MP2,5 Diario .................................................. 89

Figura 10-8. Isoconcentraciones fase de operación futura: MP2,5 Diario .................................................. 90

Figura 10-9. Isoconcentraciones fase de operación actual: NO 2 anual ....................................................... 91

Figura 10-10. Isoconcentraciones fase de operación futura: NO 2 anual .................................................... 92

Figura 10-11. Isoconcentraciones fase de operación actual: NO 2 horario .................................................. 93

Figura 10-12. Isoconcentraciones fase de operación futura: NO 2 horario ................................................. 94

Figura 10-13. Isoconcentraciones fase de operación actual: MPS Anual ................................................... 95

Figura 10-14. Isoconcentraciones fase de operación futura: MPS Anual ................................................... 96

iv

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

##### 1 INTRODUCCIÓN

En el presente documento corresponde al estudio de modelación meteorológica y de calidad del aire del

Proyecto “Aumento de Capacidad Minas 3H” de la Sociedad Minera 3H. El Proyecto que se presenta al

Servicio de Evaluación Ambiental mediante esta DIA consiste en la agrupación de las minas Cajón,

Penosa, Patricia, +40 y Chorreada, cada una de ellas con tasas de extracción de mineral menor a 5

toneladas mensuales.

Se considera una fase de construcción, que consiste en el mejoramiento del botadero, la construcción de

un casino para la alimentación de los trabajadores y la instalación de containers baño y oficina al exterior

minas, una fase operación en la que se proyecta el aumento total de las operaciones mencionadas y

agrupadas a 30 toneladas de extracción de mineral mensuales con 11 años de vida útil y por último una

fase de cierre.

Este documento presenta la modelación meteorológica con el modelo WRF, el análisis de incertidumbre

del modelo WRF y la modelación de dispersión de las emisiones atmosféricas con el modelo CALPUFF y

siguiendo los lineamientos indicados en la Guía para el Uso de Modelos de Calidad del Aire en el SEIA.

Estas emisiones fueron estimadas y reportadas en el Anexo 2-1A: Estimación de emisiones atmosféricas.

##### 2 OBJETIVOS

Los objetivos definidos dentro del estudio de calidad del aire corresponden a:

 Generación de un campo meteorológico tridimensional con el modelo WRF, para ser utilizado

como entrada meteorológica para el modelo de dispersión de contaminantes CALPUFF.

 Análisis de incertidumbre de la modelación meteorológica.

 Modelación de dispersión de las emisiones estimadas para la de operación del Proyecto,

considerando escenario futuro y base con el modelo CALPUFF para estimar el aporte de estas

emisiones al nivel de concentraciones ambientales de material particulado y gases.

 Evaluación de cumplimiento normativo de la calidad del aire proyectada, considerando los

aportes de fases de operación del proyecto, estimado a partir del delta entre el escenario futuro

y el escenario base.

5

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

##### 3 METODOLOGÍA GENERAL

En el presente documento se presenta un escenario de modelación, correspondiente a la fase de

operación del Proyecto, considerando como insumo la descripción del Proyecto en dicha fase y los

escenarios futuros (con Proyecto) y base. Solo se modela el escenario de operación ya que este es el que

presenta mayores emisiones respecto a los escenarios de construcción y cierre, además considerando

que la operación del Proyecto es también considerablemente más extensa en tiempo que las otras dos

fases del Proyecto. Los resultados del inventario de emisiones fueron insumos para la modelación de

dispersión realizada con el modelo CALPUFF. La meteorología utilizada como input a CALPUFF,

corresponde a la generada con el modelo de mesoescala WRF para el año 2018 y que se describe en la

sección 4.

Con la modelación del escenario se determinarán los aportes de éstos en la calidad del aire. La calidad

del aire proyectada para la fase de construcción del Proyecto será estimada de acuerdo con la siguiente

ecuación.

**CA_Co = LB - F_Op_a + F_Op_f**

En donde:

**CA_Co** : corresponde a la calidad del aire proyectada para operación futura del Proyecto.

**LB** : corresponde a la línea base de calidad del aire medida en el área de estudio.

**F_Op_f** : corresponde al aporte en la calidad del aire de la fase de operación futura del Proyecto.

**F_Op_a:** corresponde al aporte de en la calidad del aire de la actividad actual del complejo minero.

En el presente informe también se describe la configuración y simulación meteorológica realizada con el

modelo de pronóstico WRF y se realiza un análisis de incertidumbre a dicha modelación, comparando los

resultados de parámetros meteorológicos a nivel superficial respecto a los datos medidos en cuatro

estaciones de monitoreo meteorológico.

La metodología general seguida para el estudio se presenta a continuación en la Figura 3-1.

6

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**Figura 3-1. Pasos Metodológicos**

Fuente: Elaboración propia.

7

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

##### 4 CARACTERIZACIÓN METEOROLÓGICA DEL ÁREA DEL PROYECTO

La información meteorológica de superficie utilizada para la caracterización del área del Proyecto,

corresponde a las mediciones registradas en dos estaciones meteorológicas en el sector,

correspondiente a las estaciones Nuevo Amanecer y Catemu Meteorológica. Las coordenadas de ambas

estaciones se indican en la Tabla 4-1:. Para la caracterización meteorológica se cuenta con registros de

velocidad, dirección del viento y temperatura para Nuevo Amanecer y de velocidad y dirección del viento

para Catemu Meteorológica.

**Tabla 4-1: Coordenadas de ubicación de las estaciones meteorológicas.**

|Col1|WGS84-Huso 19|Col3|Variable monitoreada|
|---|---|---|---|
|Estación|UTM - E (m)|UTM - N (m)|UTM - N (m)|
|Nuevo Amanecer|315.243|6.376.191|Viento y temperatura|
|Catemu Meteorológica|316.480|6.368.520|Viento|

(*) Huso 19S, Datum WGS84

**Figura 4.1: Ubicación de las estaciones meteorológicas.**

Fuente: Elaboración propia, en base a Google Earth.

8

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

La disponibilidad de los datos registrados se presenta en la Tabla 4-2 donde se observa que se tiene

sobre un 99% de disponibilidad de información, excepto para dirección del viento en Nuevo Amanecer.

**Tabla 4-2: Caracterización de los datos meteorológicos, % de completitud Año 2018.**

|Estación|Velocidad del<br>viento|Dirección del viento|Temperatura|
|---|---|---|---|
|Nuevo Amanecer|99,3%|92,0 %|99,8 %|
|Catemu Meteorológica|99,9%|99,9%|-|

Fuente: Elaboración propia.

A continuación se presenta un resumen de los resultados del monitoreo de variables meteorológicas

medidos durante el año 2018 en la zona del proyecto.

##### 4.1 Velocidad del Viento

En la Tabla 4-3 se presenta la velocidad promedio de las estaciones, en ella se observa que la velocidad

promedio del viento para el año 2018 de estación Nuevo Amanecer es de 1,25 (m/s) con un máximo

horario de 4,80 (m/s), la estación Catemu Meteorológica presenta velocidades mucho más altas con un

promedio 4,07 (m/s) y un valor máximo horario mayor con 12,7 (m/s).

**Tabla 4-3: Resumen Velocidad del viento, estaciones Nuevo Amanecer y Catemu Meteorológica.**

|Variable|Nuevo Amanecer|Catemu Meteorológica|
|---|---|---|
|Promedio (m/s)|1,25|4,07|
|Mediana (m/s)|0,90|3,50|
|Máximo (m/s)|4,80|12,70|
|Porcentaje de calmas|26,3%|1,7%|

Fuente: Elaboración propia.

La Figura 4.2 muestra el ciclo diario del viento observado en la estación Nuevo Amanecer, donde las

máximas diarias se presentan entre las 15:00 y 16:00 horas con una mediana de 3 (m/s), horario en que

además aumenta la desviación estándar de las magnitudes de viento.

9

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**Figura 4.2: Ciclo diario de la velocidad del viento observada. Estación Nuevo Amanecer. Año 2018.**

Fuente: Elaboración propia.

La estación Catemu Meteorológica presentada en la Figura 4.3 magnitudes de viento considerablemente

mayores que la estación Nuevo Amanecer, donde las horas de mayor magnitud del viento presentan una

mediana de 7 m/s entre las 13:00 y 19:00 horas.

**Figura 4.3: Ciclo diario de la velocidad del viento observada. Estación Catemu Meteorológica. Año 2018**

Fuente: Elaboración propia.

10

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

##### 4.2 Dirección del Viento

Estación Nuevo Amanecer

La Figura 4.4 muestra que la estación Nuevo Amanecer presenta una clara predominancia de viento este

(E) durante el día y viento oeste (O) durante la noche.

**Figura 4.4: Rosas de viento observado. Estación Nuevo Amanecer. Año 2018.**

Fuente: Elaboración propia.

La Figura 4.5 confirma la gran frecuencia de viento este (E) que se presenta durante las horas del día,

frecuencia que disminuye considerablemente en horas de la madrugada y primeras horas de la mañana,

entre las 22:00 y las 10:00 horas, donde se observa mayor frecuencia de viento oeste (O).

11

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**Figura 4.5: Ciclo Diario de la Dirección del Viento Observada. Estación Nuevo Amanecer. Año 2018.**

Fuente: Elaboración propia.

La Figura 4.6 muestra la predominancia del viento este (E) durante todo el año en especial en los meses

de primavera y verano en gran parte del día, en tanto para los meses de invierno la dirección del viento

tiende a revertirse.

**Figura 4.6: Ciclo estacional de la dirección y velocidad del viento observada.**

**Estación Nuevo Amanecer. Año 2018.**

Fuente: Elaboración propia.

12

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

Estación Catemu Meteorológica

En la Figura 4.7 se presentan la rosa de viento anual obtenida a partir de la serie de datos. En esta se

observa un predominio de los vientos provenientes desde el suroeste (SO), durante 20% del tiempo, con

un 40 % de frecuencia al considerar las componentes vecinas, esta componente sigue del valle en la zona

de la estación y es viento que proviene del océano. Existe una segunda componente que corresponde al

viento montaña valle por efecto del cordón montañoso ubicado al sureste (SE) de la estación

meteorológica, esta componente sureste tiene una frecuencia de un 20%.

**Figura 4.7: Rosas de viento observado. Estación Catemu Meteorológica. Año 2018.**

Fuente: Elaboración propia.

En la Figura 4.8 se presenta el ciclo diario de dirección del viento observada, en dicho gráfico, se puede

corroborar que las componentes de viento principales ocurren entre las 12:00 y 24:00 horas.

13

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**Figura 4.8: Ciclo diario de la dirección del viento observada. Estación Catemu Meteorológica. Año 2018.**

Fuente: Elaboración propia.

En la Figura 4.9, se muestra el ciclo estacional de dirección y velocidad del viento observada. En dicho

gráfico, se observa una gran variabilidad en la dirección del viento tanto diaria como estacional. Las

principales componentes descritas anteriormente ocurren principalmente entre las 12:00 y 24:00 horas,

la componente suroeste (SO) predomina entre enero y mayo y la sureste (SE) entre julio y diciembre.

**Figura 4.9: Ciclo estacional de la dirección y velocidad del viento observada.**

**Estación Catemu Meteorológica. Año 2018.**

Fuente: Elaboración propia.

14

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

##### 4.3 Temperatura

Estación Nuevo Amanecer

La Tabla 4-4 muestra el resumen de los datos de temperatura en las estaciones Nuevo Amanecer. Donde

la temperatura promedio es de 16,9 (°C) y el máximo anual es 38,0 (°C).

**Tabla 4-4: Resumen temperatura, estaciones Nuevo Amanecer. Año 2018.**

|Variable|Nuevo Amanecer|
|---|---|
|Promedio (°C)|16,9|
|Mediana (°C)|15,6|
|Máxima (°C)|38,0|
|Mínimo (°C)|0,4|

Fuente: Elaboración propia.

El ciclo diario promedio junto con su variabilidad en término de los percentiles 5 y 95 se presenta en la

Figura 4.10. La hora en que se registra la mayor mediana horaria de temperatura, correspondiente a las

16:00 horas, con un valor de 26 °C, mientras que la mediana de la temperatura mínima es de 10,5 °C

obtenida a las 07:00 horas.

**Figura 4.10: Ciclo diario de temperatura observada. Estación Nuevo Amanecer. Año 2018.**

Fuente: Elaboración propia

15

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

##### 5 CARACTERIZACIÓN CALIDAD DEL AIRE

A continuación se presenta la normativa de calidad del aire utilizada para los contaminantes evaluados

en la modelación de dispersión de contaminantes. Debido a que no existen estaciones de calidad del aire

cercana al área de proyecto no es posible determinar la concentración base de los contaminantes

normados.

##### 5.1 Normativa Calidad del Aire Vigente

En el país existen normas primarias de calidad del aire vigentes para el material particulado respirable

(MP 10 ), para su fracción más fina (MP 2,5 ), y los gases dióxido de nitrógeno (NO 2 ), monóxido de carbono

(CO) y dióxido de azufre (SO 2 ). Los valores umbrales de las normas citadas se presentan en la Tabla 5-1.

**Tabla 5-1.** **Normas Primarias de Calidad del Aire Vigentes en Chile**

|Contaminante|Valor umbral de<br>la Norma|Unidad|Período de aplicación de la norma|
|---|---|---|---|
|Material Particulado<br>Respirable (MP10)|150|μg/m3|Percentil 98 de la media aritmética diaria durante un año|
|Material Particulado<br>Respirable (MP10)|50|50|Media aritmética trianual|
|Material Particulado<br>Respirable (MP2,5)|50|μg/m3|Percentil 98 de la media aritmética diaria durante un año|
|Material Particulado<br>Respirable (MP2,5)|20|20|Media aritmética trianual|
|Dióxido de nitrógeno<br>(NO2)|400|μg/m3|Percentil 99 de la media aritmética horaria trianual|
|Dióxido de nitrógeno<br>(NO2)|100|100|Media aritmética trianual|
|Monóxido de carbono<br>(CO)|30.000|μg/m3|Percentil 99 de la media aritmética horaria trianual|
|Monóxido de carbono<br>(CO)|10.000|10.000|Percentil 99 de la media aritmética de 8 horas trianual|
|Dióxido de azufre (SO2)|350|μg/m3|Percentil 98.5 de la media aritmética horaria trianual|
|Dióxido de azufre (SO2)|150|150|Percentil 99 de la media aritmética diaria trianual|
|Dióxido de azufre (SO2)|60|60|Media aritmética trianual|

Fuente: MP 10 : D.S. No 59, de 1998, del MINSEGPRES; MP 2,5 : D.S. No 12, de 2011 MMA; CO: D.S. No 115, de 2002 MINSEGPRES;

NO 2 : D.S. No 114, de 2002 MINSEGPRES; SO 2 : D.S. No 104, de 2018 MINSEGPRES.

16

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

##### 5.2 Monitoreo calidad del aire

La Tabla 5-2 y Figura 5.1 muestran las coordenadas y ubicación de las estaciones de calidad del aire

consideradas.

**Tabla 5-2: Coordenadas de ubicación de las estaciones de calidad del aire.**

|Col1|WGS84-Huso 19|Col3|Variable monitoreada|
|---|---|---|---|
|Estación|UTM - E (m)|UTM - N (m)|UTM - N (m)|
|Nuevo Amanecer|315.243|6.376.191|MP10, MP2.5, MPS|
|Catemu|316.307|6.371.159|MP10|

Fuente: Elaboración propia.

**Figura 5.1: Ubicación de las estaciones de calidad del aire.**

Fuente: Elaboración propia, en base a Google Earth.

A continuación en la Tabla 5-3 se muestra la completitud de datos medidos de calidad del aire para el

año 2018 en estaciones Nuevo Amanecer y Catemu y posteriormente se muestran los resultados para las

normas de calidad del aire vigentes o de referencia respectivas.

17

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**Tabla 5-3: Completitud datos medidos de calidad del aire año 2018.**

|Contaminante|MP10|MP2.5|MPS|
|---|---|---|---|
|Nuevo Amanecer|98%|93%|100%|
|Catemu|100%|-|-|

Fuente: Elaboración propia.

La Tabla 5-4 muestra el promedio anual año 2018 en las estaciones Nuevo Amanecer y Catemu, donde se

puede apreciar que la estación Catemu supera la norma anual de MP10 mientras que la estación Nuevo

Amanecer esta bajo el umbral de la norma. En la Tabla 5-5 se muestra el cumplimiento de la norma

diaria de MP10 de ambas estaciones donde se verifica que la estación Nuevo Amanecer no presenta

ninguna excedencia a la norma mientras que la estación Catemu tiene un solo valor sobre 150 μg/m [3] N,

ambas estaciones no exceden el umbral de la norma para el percentil 98.

**Tabla 5-4: MP10 promedio anual año 2018**

|Estación|Promedio<br>(μg/m3N)|Norma<br>(μg/m3N)|% de la<br>Norma Anual|
|---|---|---|---|
|Nuevo Amanecer|45.9|50|92%|
|Catemu|67.5|67.5|135%|

Fuente: Elaboración propia.

**Tabla 5-5: MP10 diario año 2018**

|Estación|N° Excedencia|Percentil 98|Norma|% de la<br>Norma 24<br>horas|
|---|---|---|---|---|
|**Estación**|**> 150 μg/m3N**|**(μg/m3N)**|**(μg/m3N)**|**(μg/m3N)**|
|Nuevo Amanecer|0|93.5|150|62%|
|Catemu|1|131.7|131.7|88%|

Fuente: Elaboración propia.

La Tabla 5-6 y Tabla 5-7 muestra el promedio anual año 2018 y promedio diario, respectivamente, para

el MP2.5 en la estación Nuevo Amanecer, donde se puede apreciar que ambas estaciones se encuentran

muy per debajo del umbral de las normas respectivas.

**Tabla 5-6: MP2.5 promedio anual 2018**

|Estación|Promedio<br>(μg/m3N)|Norma<br>(μg/m3N)|% de la<br>Norma Anual|
|---|---|---|---|
|Nuevo Amanecer|10.8|20|54%|

Fuente: Elaboración propia.

18

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**Tabla 5-7: MP2.5 diario año 2018**

|Estación|N° Excedencia|Percentil 98|Norma|% de la<br>Norma 24<br>horas|
|---|---|---|---|---|
|**Estación**|**> 50 μg/m3N**|**(μg/m3N)**|**(μg/m3N)**|**(μg/m3N)**|
|Nuevo Amanecer|0|26.0|50|52%|

Fuente: Elaboración propia.

La Tabla 5-8 muestra el valor promedio año 2018 de MPS en estación Catemu el cual se encuentra a

menos del 50 % del umbral de la norma de referencia Suiza.

**Tabla 5-8: MPS anual año 2018**

|Estación|Promedio<br>(mg/m2_dia)|Norma<br>(mg/m2_dia)1|% de la<br>Norma Anual|
|---|---|---|---|
|Nuevo Amanecer|99.2|200|49.6%|

Fuente: Elaboración propia.

1 Debido a la presencia de flora y fauna nativa en los sectores cercanos al proyecto, se ha evaluado el impacto del
material particulado sedimentable. Para lo anterior se consideró como referencia la norma Suiza, para valores de
depositación anual. Lo anterior de acuerdo con los valores obtenidos de documento del SEIA “Normas de calidad
primarias e Información complementaria” (http://www.sea.gob.cl/documentacion/normas-de-calidad-y-valoresreferenciales)

19

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

##### 6 MODELO METEOROLÓGICO 6.1 Justificación del Modelo Meteorológico

Según lo establecido por la Guía para el uso de Modelos de Calidad del Aire en el SEIA, la selección del

modelo meteorológico utilizado en el presente estudio se realizó fundamentándose en las condiciones

del dominio de modelación del área entorno al proyecto, motivo por el cual la Guía recomienda un

modelo que permita simular una meteorología heterogénea. Por esta razón, el campo meteorológico

tridimensional horario del año 2018 completo fue generado utilizando el modelo meteorológico WRF, en

su versión 4.0.3, y procesado con MMIF v3.2. Posteriormente esta información fue utilizada en el modelo

de calidad de aire CALPUFF.

##### 6.2 Descripción del Modelo Meteorológico

El modelo de investigación y pronóstico del tiempo (Weather Research and Forecasting - WRF) es un

sistema de predicción numérico de mesoscala de nueva generación, diseñado para servir pronósticos

operacionales y para estudio de la atmósfera.

Se crearon cuatro dominios anidados con resoluciones de grilla de 27, 9, 3 y 1 kilómetro

correspondientemente, los cuales se muestran en la Figura 6.1, en rojo se indica el dominio de

modelación más pequeño, el cual se utilizará para alimentar el modelo de dispersión CALPUFF. La Tabla

6-1 y la Tabla 6-2 muestran la definición de los dominios anidados utilizados en WRF y la proyección

geográfica, respectivamente.

20

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**Figura 6.1: Extensiones de los dominios 1, 2, 3 y 4 en WRF.**

Fuente: Elaboración propia, en base a Google Earth.

21

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**Tabla 6-1: Definición de dominio de modelación.**

|Col1|DX|DY|NX|NY|KMx|KMy|No Celdas|
|---|---|---|---|---|---|---|---|
|Dominio 1|27|27|58|67|1566|1809|3886|
|Dominio 2|9|9|55|64|495|576|3520|
|Dominio 3|3|3|52|61|156|183|3172|
|Dominio 4|1|1|49|58|49|58|2842|

Fuente: Elaboración propia.

**Tabla 6-2: Definición proyección dominios de modelación.**

|Origen centro Dominio 1 y<br>proyección LCC|Col2|
|---|---|
|ref_lat|-32,75|
|ref_lon|-70,96|
|truelat1|-27,75|
|truelat2|-37,75|
|stand_lon|-71,96|

Fuente: Elaboración propia.

Para realizar la simulación con el modelo WRF se obtuvo la información de uso de suelos a partir de
información satelital de MODIS [2] de la NASA con resolución de 15 segundos de grado, información que

fue refinada con Wtools utilizando imágenes satelitales e información de elevación de terreno a partir de

la información topográfica del SRTM (Misión de Radar Topográfico del Transbordador Espacial de la
NASA [3] ) con resolución de 3 segundos de grado, es decir 90 metros aproximadamente. Condiciones
iniciales y de borde fueron generadas a partir de los “datos operacionales de análisis global” [4] de NCEP [5]

con un grado de resolución espacial de 1° y temporal de 6 horas, complementada con información de

temperaturas de la superficie del mar obtenidas a partir de archivos en tiempo real de “Sea Surface

Temperature” de NCEP con resolución de 1/12 de grado.

Se utilizó la configuración publicada por el SEA pero con las siguientes modificaciones: se seleccionó la

opción Noah Land Surface Model para poder usar información de uso de suelo de mayor resolución.

Además se activaron para todos los dominios de la simulación las opciones de "slope_rad",

"topo_shading" y “topo_wind”, la primera opción considera el efecto de la pendiente del terreno en el

flujo de la radiación solar superficial, la segunda considera los efectos de sombra que pueden generar las

celdas circundantes que posean elevación terreno mayor a la celda considerada y la última considera una

2 https://modis.gsfc.nasa.gov/

3 https://www2.jpl.nasa.gov/srtm/

4 FNL (Final) Operational Global Analysis data

5 U.S. National Center of Environmental Prediction perteneciente a la NOAA

22

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

corrección topográfica para vientos de superficie para representar resistencia adicional de la topografía

de la subgrilla y además el cálculo de flujo mejorado en las cimas de las colinas, respectivamente. La

opción “topo_wind” (Jimenez and Dudhia, JAMC 2012) fue utilizada ya que en en la zona predominan los

vientos superficiales de baja magnitud, en parte debido a la complicada geomorfología de la zona, esto

vientos superficiales de baja magnitud no son resueltos fácilmente por el modelo WRF.

Las principales parametrizaciones y configuraciones de las opciones físicas del modelo son las siguientes:

a) Se utilizaron 45 niveles verticales ETA.

b) Para la estimación de la capa limite planetaria se utilizó el esquema de la universidad de Yonsei,

ya que este es el único esquema que permite utilizar la opción “topo_wind”. Este es un esquema

no local de coeficientes de difusión K con capa de arrastre explícita y perfil de coeficientes K

parabólico en capa mixta inestable.

c) Para la estimación de la capa límite superficial se utilizó el esquema de similaridad de MM5.

Basado en Monin-Obukhov con subcapa viscosa de Carslon-Boland y funciones estándar de

similitud.

d) Para la simulación de los intercambios de calor entre superficie y atmosfera se utilizó el “Noah

Land Surface Model”, opción compatible con la clasificación de uso de suelos utilizada en la

información satelital de MODIS de la NASA.

e) Por último para la estimación de formación de nubes se utilizó el esquema convectivo de Betts

Miller-Janjic (Betts and Miller 1986, Janjic 1994)

23

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**Figura 6.2: Uso de suelo dominio 4 WRF.**

Fuente: Elaboración propia, en base a Google Earth y Wtools.

##### 6.3 Dominio Modelación

El dominio de modelación considerado para el presente Proyecto corresponde a una grilla rectangular de

75 x 55 km, compuesta por celdas de 1 km por lado, la cual tiene la misma proyección utilizada por el

modelo WRF y corresponde a un subdominio del dominio 4 modelado con WRF, eliminando 5 celdas por

borde, siguiendo la recomendación de la guía de MMIF, el cual es el post-procesador utilizado para

extraer datos de WRF a CALPUFF. En la El dominio elegido abarca a lo menos el área de influencia del

Proyecto para los distintos componentes ambientales que pueden verse afectados por las emisiones

atmosféricas de éste, lo que se corrobora más adelante en las gradientes de concentraciones estimadas

por el modelo.

Tabla 6-3 se presentan las características del área correspondiente al dominio de modelación. El dominio

elegido abarca a lo menos el área de influencia del Proyecto para los distintos componentes ambientales

que pueden verse afectados por las emisiones atmosféricas de éste, lo que se corrobora más adelante en

las gradientes de concentraciones estimadas por el modelo.

24

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**Tabla 6-3: Características del Dominio de Modelación.**

|Característica|Eje X (km)|Eje Y (km)|
|---|---|---|
|Espaciamiento|1|1|
|Longitud|36|47|

Fuente: Elaboración propia.

En la Figura 6.3, se presenta el dominio de modelación utilizado en CALPUFF, donde se destacan en rojo

la estación meteorológica Nuevo Amanecer y Catemu Meteorológica, la cuales será utilizadas en el

análisis de incertidumbre del modelo WRF para los parámetros de vientos y con marcadores cuadrados

de distintos colores se pueden ver las 5 minas que son parte del Proyecto, las que se encuentran todas

muy cercanas a la estación de monitoreo mencionada.

25

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**Figura 6.3: Dominio de Modelación del Proyecto.**

Fuente: Elaboración propia.

26

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

La Figura 6.4 muestra la grilla de modelación utilizada en el modelo CALPUFF respecto al dominio 4 del
modelo WRF, el cual se muestra en color rojo. La grilla de modelación abarca parte de las Región de
Valparaíso, incluyendo gran parte las Provincias de San Felipe de Aconcagua, Quillota y Petorca,
abarcando principalmente las comunas de Catemu, Panquehue, Hijuelas y Llaillay; y parte de las
comunas de Cabildo, Putaendo, El Melón, San Felipe y la Calera. Cabe mencionar que el área de
modelación corresponde al área de estudio, el área de influencia del componente aire se obtendrá de los
resultados del modelo de dispersión.

**Figura 6.4: Dominio de Modelación del Proyecto y límites comunales.**

Fuente: Elaboración propia.

27

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

##### 6.4 Topografía y Uso de Suelos

La fuente de información topográfica del dominio de modelación considerado en CALPUFF corresponde
a cartas topográficas digitales SRTM3 [6] de 90 metros de resolución, las cuales se utilizan el modelo WRF.

En CALPUFF se utilizó la información topográfica considerada por el modelo WRF. A continuación, se

presenta una imagen de la topografía, que corresponde al SRTM3 interpolado a la resolución de grilla de

1 kilómetro que utilizan los modelos WRF y CALPUFF en este caso.

La información relacionada con el uso de suelo, de igual manera que la elevación de terreno es utilizada

directamente del modelo WRF, la cual corresponde a información satelital de MODIS de la NASA con

resolución de 15 segundos de arco, la caracterización de uso de suelos para cada celda del dominio 4 de

WRF se puede observar en la Figura 6.2.

A continuación, en la Figura 6.5, se presenta gráficamente la topografía del dominio modelado, donde se

destacan en rojo las estaciones meteorológicas utilizada en el análisis de incertidumbre del modelo WRF,

cuyas coordenadas se muestran en la Tabla 6-4. Cabe destacar la gran complejidad de la geomorfología

de la zona.

6 https://www2.jpl.nasa.gov/srtm/

28

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**Figura 6.5: Topografía del dominio de modelación.**

Fuente: Elaboración propia en base a información proporcionada por NASA.

**Tabla 6-4. Coordenadas estaciones meteorológicas**

|Col1|WGS84-Huso 19|Col3|
|---|---|---|
|Estación|UTM - E (m)|UTM - N (m)|
|Nuevo Amanecer|315.243|6.376.191|
|Catemu Meteorológica|316.480|6.368.520|

Fuente: GAC

29

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

##### 6.5 Evaluación del Modelo Meteorológico

Para evaluar el desempeño de la modelación meteorológica utilizada en el modelo, se han analizado

estadísticamente los datos medidos de vientos en el año 2018 en la estación Nuevo Amanecer, ubicada a

menos de 500 metros al sureste de Mina Patricia, la cual es la mina más cercana del Proyecto a la

estación monitorea y en la estación Catemu, ubicada a 8 kilómetros al sur del proyecto, las coordenadas

se presentan en la Tabla 6-4. Para ello se han extraído los resultados del modelo meteorológico para la

coordenada ( _x,y_ ) donde se emplazan la estaciones meteorológica, a 10 metros de altura, coincidente con

la altura del anemómetro de la estación. Las variables consideradas para la evaluación corresponden a:

velocidad del viento y dirección del viento y temperatura. Para cada una, se evaluó el ciclo diario y la

serie de tiempo. Es importante tener en cuenta que los datos de la estación monitora corresponden a

datos medidos en un punto, mientras que los datos obtenidos del modelo corresponden a datos

representativos de una celda de 1 x 1 kilómetros, especialmente en este caso donde la configuración

geomorfológica de la zona es muy compleja.

Para la evaluación del modelo, además de comparaciones gráficas, se han utilizado distintos

estadígrafos, los que se describen a continuación:

 - **n** corresponde al número total de pares completos

 - **Sesgo:** Corresponde a la diferencia entre el promedio modelado y el promedio observado

 - **FAC2:** Predicción fraccionada, o factor de predicciones dentro de un factor de dos de las

observaciones

0,5 ≤ [M] [i]

O i

≤2

**Sesgo medio (SM):** Éste representa la tendencia del modelo a sobrestimar o subestimar las

condiciones reales, cuantificando así el error sistemático del modelo. Para valores negativos el

modelo tiende a subestimar el valor de las variables modeladas, y para valores positivos, el

modelo tiende a sobreestimar.

30

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

N

SP= [1]

n [∑(M] [i] [−O] [i] [)]

i=1

- **Error absoluto medio (MAE):** Este coeficiente se utiliza para medir el desempeño de modelos y

consiste en el promedio de los errores absolutos, este coeficiente ignora punto a punto si el

error es una subestimación o sobreestimación del modelo.

###### M − O
#### ( i i )

MAE=

_n_
####  ( M i − O i

_i_ = 1

_i_

###### _n_

- **Sesgo medio normalizado (SMN):** Sesgo medio pero normalizado respecto a los valores

observados.

SMN= [∑] ni=1 (M i −O i )

∑ ni=1 (O i )

- **Error absoluto medio normalizado (NMAE** ): Corresponde al MAE pero normalizado respecto a

los valores observados.

_n_

###### ( M i − O i )

_M_ − _O_

−

_i_ _i_


_i_ = 1

_O_

_NMAE_

_i_ = 1
_i_

=

_n_

- **Error Cuadrático Medio (ECM):** Éste entrega la diferencia promedio entre los valores modelados

y observados.

n

n

i=1

ECM= √∑ [(M] [i] [−O] [i] [)] [2]

n

n

i=1

- **Coeficiente de Correlación (r):** Este coeficiente entrega una medida de la relación lineal entre la

variable modelada y la observada. El valor del coeficiente varía en el intervalo [-1,1]. Para el caso

de la modelación, entre más cercano a 1, mejor es la capacidad del modelo de representar las

condiciones atmosféricas.

31

N

1

r=
(1 −n) [∑(M] [i] σ [−M̅)] M

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

(O i −O [̅] )

σ o

i=1

σ M

**Índice de concordancia (IOA):** Éste corresponde al índice de concordancia revisado (Willmott et

al. 2011). El valor del coeficiente varía en el intervalo [-1,1], donde 1 representa un modelo

perfecto, un valor de 0,5 indica que la suma de las magnitudes de error son la mitad de la suma

de las magnitudes de las desviaciones observadas, por lo general un IOA mayor que 0,5 indica un

modelo con buen desempeño. Un coeficiente con valor de 0,0 indica que la suma de las

magnitudes de error es equivalente a la suma de las magnitudes de las desviaciones observadas

y un valor de -0,5 indica que son el doble.

IOA= 1,0 −

c∑∑ ni=ni=11 |M|O i −O i −O [̅] i || cuando ∑ ni=1 |M i −O i | ≤ c∑ ni=1 |O i −O [̅] |

IOA=

c∑∑ ni=1ni= |M 1 |O i −O i −O [̅] i || −1,0 cuando ∑ ni=1 |M i −O i | - c∑ ni=1 |O i −O [̅] |

Con c = 2.

A continuación se presentan los resultados para las variables consideradas.

###### 6.5.1 Velocidad del Viento

Nuevo Amanecer

En la Figura 6.6 se presenta el ciclo diario de la mediana de la velocidad del viento horaria modelada y

observada junto con los percentiles 5 y 95 de los datos en el punto correspondiente a la estación Nuevo

Amanecer. En ella, se puede observar que la mediana modelada esta por sobre la observada entre las 10

y 19 horas, alcanzando un sesgo de hasta 1 m/s, pero durante las horas de la noche y madrugada la

situación se revierte, es decir el modelo estima velocidades más bajas de viento que los valores

observados durante esas horas. La amplitud entre los percentiles 5 y 95 de los datos modelados es

mayor respecto a la amplitud de los datos observados durante casi todas las horas del día.

32

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**Figura 6.6: Ciclo diario de la velocidad del viento modelada y observada.**

**Estación Nuevo Amanecer, año 2018.**

Fuente: Elaboración propia.

En la Figura 6.7 se presenta el ciclo anual de la mediana de la velocidad del viento observada y modelada

con los percentiles 5 y 95 en la estación Nuevo Amanecer, donde es posible apreciar que el modelo

estima velocidades del viento mayores a las registradas en la estación monitora durante horas del

verano y menores que los datos observados en los meses de invierno. La estacionalidad de la velocidad

del viento es mucho más acentuada en la serie de tiempo modelada que en la de los registros medidos

en la estación. Cabe mencionar que la baja estacionalidad de la velocidad del viento medida no es típica

de una zona alejada de la costa.

33

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**Figura 6.7: Ciclo mensual de la velocidad del viento modelada y observada.**

**Estación Nuevo Amanecer, año 2018.**

Fuente: Elaboración propia.

En la Figura 6.8 es posible corroborar que el modelo estima velocidades del viento muy similares a las

medidas por la estación monitoras para magnitudes que van entre los 2 m/s y 4 m/s, pero el modelo

estimar menores velocidades de vientos que los registros medidos en la estación monitor para

velocidades medidas menores a 2 m/s y estima mayores velocidades de vientos respecto a los registros

medidos para velocidades de vientos mayores a 4 m/s.

34

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**Figura 6.8: Cuantiles condicionales e histograma de velocidad del viento observada y modelada, estación Nuevo**

**Amanecer, año 2018.**

Fuente: Elaboración propia.

Catemu

Como se muestra en la sección de evaluación de dirección del viento, la concordancia de la dirección del

viento modelado y observado no es muy alta, por esta razón se evalúa el modelo WRF en un segundo

punto correspondiente a la estación meteorológica Catemu. En la Figura 6.9 se presenta el ciclo diario de

la mediana de la velocidad del viento horaria modelada y observada junto con los percentiles 5 y 95 de

los datos en el punto correspondiente a la estación meteorológica Catemu. En ella, se puede observar

que existe una muy alta correlación entre los ciclos diarios modelados y observados, con la única

excepción de que el modelo estima mayores velocidades en horas punta que los registros medidos en la

estación.

35

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**Figura 6.9: Ciclo diario de la velocidad del viento modelada y observada.**

**Estación Catemu, año 2018.**

Fuente: Elaboración propia.

En la Figura 6.10 se presenta el ciclo anual de la mediana de la velocidad del viento observada y

modelada con los percentiles 5 y 95 en la estación meteorológica Catemu, donde si bien se aprecian

algunas diferencias entre ambos ciclos, en algunos meses específicos que presentan sesgos, se observa

que tanto el ciclo mensual de los datos modelados como los observados presentan una clara

estacionalidad de la velocidad del viento. A diferencia de los datos medidos en estación Nuevo

Amanecer, la estación meteorológica Catemu presenta una clara estacionalidad en la velocidad de los

vientos.

36

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**Figura 6.10: Ciclo mensual de la velocidad del viento modelada y observada.**

**Estación Catemu, año 2018.**

Fuente: Elaboración propia.

El grafico de Figura 6.11 muestra una muy alta correlación entre las velocidades del viento observadas y

modeladas en estación meteorológica Catemu, ya que el diagrama de dispersión muestra una mediana

muy cercana a la recta de 45 grados. En el histograma es posible apreciar frecuencias de vientos muy

simulares para los distintos intervalos de velocidades, solo con la excepción entre los 2 y 3,4 m/s donde

el modelo presenta menor frecuencia de estas velocidades que los registros medidos.

37

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**Figura 6.11: Cuantiles condicionales e histograma de velocidad del viento observada y modelada, estación**

**Catemu, año 2018.**

Fuente: Elaboración propia.

La Tabla 6-5 muestra los promedios y máximos de la velocidad del viento en conjunto con el porcentaje

de calmas, observado y modelado para ambas estaciones. El modelo estima velocidades de viento

levemente mayores a las observadas, tanto para en el caso de los promedios como para las medianas,

pero no superando sesgos de un 20%. Por otra parte, el modelo estimar mayores frecuencias de

condiciones de calma (vientos menores a 0,5 m/s) que los registros de las estaciones monitoras.

38

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**Tabla 6-5: Estadígrafos velocidad del viento, estaciones Nuevo Amanecer y Catemu.**

|Col1|Nuevo Amanecer|Col3|Catemu Met|Col5|
|---|---|---|---|---|
|**Variable**|**Observado**|**Modelado**|**Observado**|**Modelado**|
|Promedio (m/s)|1,25|1,69|4,07|4,38|
|Mediana (m/s)|0,90|1,00|3,50|4,20|
|Máximo (m/s)|4,80|12,80|12,70|13,40|
|Porcentaje de calmas|26,3%|40,7%|1,7%|9,6%|

Fuente: Elaboración propia.

El análisis presentado anteriormente de los datos medidos y modelados en las estaciones Nuevo

Amanecer y meteorológica Catemu muestran, al igual como se puede observar en la Tabla 6-6, que el

modelo se asimila mucho más a los datos medidos en la estación meteorológica Catemu que en la

estación Nuevo Amanecer. Ya que, si bien ambas en ambas estaciones los datos modelados y

observados presentan una alta correlación con índices de correlación r superiores a 0,75 en ambos

casos, el sesgo normalizado (NMAE) es considerablemente menor en Catemu, estación que presenta un

índice de concordancia IOA también considerablemente mayor a la de la estación Nuevo Amanecer. En

resumen, el modelo presenta una alta concordancia con el monitoreo de velocidad del viento en

estación Catemu y una concordancia media-alta en estación Nuevo Amanecer.

**Tabla 6-6: Estadígrafos de desempeño velocidad del viento. Año 2018.**

|Estación|n|Sesgo|FAC2|SM|MAE|SMN|NMAE|ECM|r|IOA|
|---|---|---|---|---|---|---|---|---|---|---|
|Nuevo Amanecer|8697|0,44|0,58|0,45|0,89|35,9%|71,2%|1,38|0,76|0,44|
|Catemu|8753|0,31|0,68|0,31|1,59|7,5%|38,9%|1,98|0,77|0,64|

Fuente: Elaboración propia.

###### 6.5.2 Dirección del Viento

Nuevo Amanecer

En la Figura 6.12 se presenta la rosa de los vientos correspondiente a los valores de dirección del viento

modelada y observada en el punto correspondiente a la estación Nuevo Amanecer. Es posible verificar

que el nivel de concordancia entre las direcciones modeladas y observadas no es alto, el modelo

presenta una rotación de casi 90 grados respecto a los datos observados. Esto se puede deber a la alta

complejidad de la geomorfología de la zona de la estación Nuevo Amanecer, la cual puede ser

complicada para ser resuelta por el modelo WRF y también probablemente suavizada al considerar una

resolución horizontal de celda de 1 km por 1 km. Una segunda razón puede deberse a un problema en el

instrumento de medición de dirección del viento, por esta razón en la Figura 6.13 se muestran las rosas

39

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

de vientos de los datos registrados en la estación Nuevo Amanecer desde el año 2014 al 2018, donde es

posible verificar una gran diferencia entre las rosas de vientos de los años 2014 y 2015 respecto a las

rosas de vientos de los años 2016, 2017 y 2018. Debido a la incertidumbre generada por la diferencia en

las rosas de vientos entre los años mencionados se decidió evaluar el modelo en un segundo punto, el

cual corresponde a la estación meteorológica Catemu.

**Figura** **6.12:** **Rosa** **de** **los** **vientos** **observada** **y** **modelada** **año** **2018.**

**Estación Nuevo Amanecer.**

|Observada|Modelada|
|---|---|
|||

Fuente: Elaboración propia.

40

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**Figura** **6.13:** **Rosa** **de** **los** **vientos** **observada** **años** **2014** **al** **2018.**

**Estación Nuevo Amanecer.**

Fuente: Elaboración propia.

En la Figura 6.14 se presenta un gráfico polar que indica la frecuencia de datos para la desviación del

viento modelado en grados respecto a la dirección del viento observado, es decir para las 8760 horas del

año se obtiene la diferencia (o delta) entre el viento modelado y observado, además en tonos de rojo se

indica frecuencia de datos con magnitudes de viento sobreestimadas respecto a lo observado y en tonos

de azul frecuencia de datos con magnitudes de viento subestimadas respecto a lo observado. A modo de

explicación, un modelo con direcciones de viento que coincidieran perfectamente con lo observado

presentaría un solo componente norte (0°) con una frecuencia del 100 % en el gráfico polar expuesto.

El gráfico muestra una mayor cantidad de frecuencia de datos en tonos burdeos que azules, pero

también una gran frecuencia de datos en color blanco, lo que indica en promedio una diferencia

moderada de velocidades de viento modeladas respecto a las observadas, el delta promedio de la

magnitud del viento modelado es de un 0,5 m/s respecto al promedio observado. Respecto a las

direcciones de viento se puede ver observar que existe una rotación muy marcada entre los datos

observados y modelados, donde las direcciones modeladas presentan una rotación promedio de 77,3

41

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

grados respecto a las direcciones medidas. Las posibles razones de esto ya se discutieron antes en el

presente documento.

**Figura 6.14: Gráfico polar con frecuencia de desviación entre direcciones de viento modeladas y observadas por**

**intervalos de diferencia en magnitud de velocidad del viento. Estación Nuevo Amanecer. Año 2018.**

Fuente: Elaboración propia.

La Figura 6.15 y la Figura 6.16 muestran las frecuencias de vientos observadas y modeladas para distintas

horas del día, donde es posible observar que durante el periodo diurno el modelo presenta con mayor

frecuencia una rotación de 70 - 90 grados respecto a los datos observados en sentido horario y con

menor frecuencia una rotación de la misma magnitud pero contrasentido horario. Durante horas de la

noche y madrugada la rotación es menor del modelo respecto a lo datos observados.

42

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**Figura 6.15: Ciclo diario de la dirección del viento observada. Estación Nuevo Amanecer. Año 2018.**

Fuente: Elaboración propia.

**Figura 6.16: Ciclo diario de la dirección del viento modelada. Estación Nuevo Amanecer. Año 2018.**

Fuente: Elaboración propia.

43

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

La Figura 6.17 y la Figura 6.18 muestran que tanto la velocidad del viento observada y modelada

presentan máximos durante horas de la tarde, los cuales son más acentuados durante los meses de

verano, es posible ver que el modelo presenta ciclos diarios según mes del año muy similares a los

medidos pero estima vientos de mayor magnitud que las observadas, especialmente en horas del

mediodía y tarde en los meses de verano.

**Figura 6.17: Ciclo estacional de la dirección y velocidad del viento observada.**

**Estación Nuevo Amanecer. Año 2018.**

Fuente: Elaboración propia.

44

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**Figura 6.18: Ciclo estacional de la dirección y velocidad del viento modelada.**

**Estación Nuevo Amanecer. Año 2018.**

Fuente: Elaboración propia.

Catemu

En la Figura 6.19 se presenta la rosa de los vientos correspondiente a los valores de dirección del viento

modelada y observada en el punto correspondiente a la estación meteorológica Catemu. Es posible

observar que en este punto las direcciones modeladas se asemejan mucho más a las observadas que en

el caso de Nuevo Amanecer. La rosa de vientos observada y modelada presentan el mismo componente

predominante de vientos suroeste (SO) con una pequeña rotación, sin embargo los datos medidos

presentan una mayor variación en las direcciones de vientos que los vientos estimados por WRF, esto se

puede deber al efecto local en la dirección viento de los cerros ubicados al sur de la estación

meteorológica Catemu, los cuales WRF no es capaz de resolver con una resolución de celda de 1 km.

45

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**Figura** **6.19:** **Rosa** **de** **los** **vientos** **observada** **y** **modelada** **año** **2018.**

**Estación Catemu.**

|Observada|Modelada|
|---|---|
|||

Fuente: Elaboración propia.

El gráfico polar de la Figura 6.20 muestra una frecuencia similar de datos en tonos burdeos y azules,

pero también una gran frecuencia de datos en color blanco, lo que indica en promedio una diferencia

moderada de velocidades de viento modeladas respecto a las observadas, el delta promedio de la

magnitud del viento modelado es de un 0,3 m/s respecto al promedio observado. Respecto a las

direcciones de viento se puede ver que la mayoría de los datos no presentan desviaciones en la dirección

de viento mayores a los 45 grados respecto a los datos observados, pero existe un numero de datos no

menor con desviaciones de 90 grados, a pesar de lo anterior, es posible observar que de todas maneras

existe una rotación promedio de solo en 28,8 grados en sentido horario.

46

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**Figura 6.20: Gráfico polar con frecuencia de desviación entre direcciones de viento modeladas y observadas por**

**intervalos de diferencia en magnitud de velocidad del viento. Estación Catemu. Año 2018.**

Fuente: Elaboración propia.

La Figura 6.21 y Figura 6.22 muestran las frecuencias de vientos observadas y modeladas para distintas

horas del día, donde es posible observar una alta correlación entre las direcciones de viento modeladas y

observadas más predominantes, predominantemente suroeste (SO), con la principal excepción de que

en horas de la tarde la estación meteorológica registra cierta frecuencia de vientos sureste (SE).

47

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**Figura 6.21: Ciclo diario de la dirección del viento observada. Estación Catemu. Año 2018.**

Fuente: Elaboración propia.

**Figura 6.22: Ciclo diario de la dirección del viento modelada. Estación Catemu. Año 2018.**

Fuente: Elaboración propia.

48

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

La Figura 6.23 y la muestran que tanto la velocidad del viento observada y modelada presentan máximos

durante horas de la tarde, los cuales son más acentuados durante los meses de verano, es posible ver

que el modelo presenta ciclos diarios según mes del año muy similares a los medidos. Se ve cierta

diferencia entre los vectores promedio modelados y observados, especialmente en invierno.

**Figura 6.23: Ciclo estacional de la dirección y velocidad del viento observada.**

**Estación Catemu. Año 2018.**

Fuente: Elaboración propia.

49

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**Figura 6.24: Ciclo estacional de la dirección y velocidad del viento modelada.**

**Estación Catemu. Año 2018.**

Fuente: Elaboración propia.

###### 6.5.3 Temperatura

A continuación se analizan los ciclos diarios y mensuales de la temperatura observada y modelada en la

estación Nuevo Amanecer

Estación Nuevo Amanecer

En la Figura 6-25 se presenta el ciclo diario de las medianas de la temperatura horaria modelada y

observada junto con los percentiles 5 y 95 de los datos en el punto correspondiente a la estación Nuevo

Amanecer. En ella se puede ver que el ciclo diario presenta buena correlación entre los datos observados

y modelados pero el modelo estima una amplitud térmica diaria menor a la observada.

50

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**Figura 6-25: Ciclo diario de la temperatura modelada y observada,**

**Estación Nuevo Amanecer. Año 2018.**

Fuente: Elaboración propia

En la Figura 6-26 se presenta el ciclo mensual de temperatura observada y modelada con los percentiles

5 y 95 en la estación Nuevo Amanecer, donde es posible apreciar que el ciclo mensual de temperatura

estimado por el modelo presenta una alta correlación respecto a los datos observados pero con un sesgo

mensual positivo.

51

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**Figura 6-26: Ciclo mensual de la temperatura modelada y observada,**

**Estación Nuevo Amanecer, año 2018.**

Fuente: Elaboración propia

El gráfico de dispersión de la Figura 6.27 muestra una muy alta correlación entre las temperaturas

observadas y modeladas en estación la estación Nuevo Amanecer, por otra parte los diagramas en la

misma figura indican que el modelo estima temperaturas en general de 1 °C a 2 °C más altas que las

medidas en la estación monitora.

52

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**Figura 6.27: Cuantiles condicionales e histograma de velocidad del viento observada y modelada, estación**

**Catemu, año 2018.**

La

Tabla **6-7** muestra el promedio, mediana máximo y mínimo de temperatura observada y modelada para

la estación Nuevo Amanecer, donde el modelo presenta un sesgo de 1,2 °C y 2,1 °C para el promedio y

mediana respectivamente. Por otra parte, la Tabla 6-8 muestra un coeficiente de correlación (r) e índice

de concordancia altos, con valores de 0,84 y 0,73 respectivamente.

**Tabla 6-7: Estadígrafos de temperatura, estación Nuevo Amanecer.**

|Col1|Nuevo Amanecer|Col3|
|---|---|---|
|**Variable**|**Observado**|**Modelado**|
|Promedio (°C)|16,9|18,1|
|Mediana (°C)|15,6|17,7|
|Máximo (°C)|38,0|34,3|
|Mínimo (°C)|0,4|1,3|

53

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

Fuente: Elaboración propia

**Tabla 6-8: Estadígrafos desempeño por temperatura, estación Nuevo Amanecer, datos observados y modelados.**

|Estación|n|Sesgo|FAC2|SM|MAE|SMN|NMAE|ECM|r|IOA|
|---|---|---|---|---|---|---|---|---|---|---|
|Nuevo Amanecer|8743|1,17|0,95|1,18|3,09|7,0%|18,3%|3,93|0,84|0,73|

Fuente: Elaboración propia

54

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

###### 6.5.4 Altura capa de mezcla en zona modelada

A continuación se presenta un análisis cualitativo del comportamiento estacional y horario de la altura

de capa de mezcla modelada con el modelo WRF, se realiza un análisis cualitativo ya que no existen

datos medidos para dicho parámetro. La Figura 6.28 muestra el perfil diario promedio por mes del año

de la altura de capa de mezcla modelada en la estación Cuerpo de Bomberos. Se puede apreciar que los

máximos diarios para todos los meses se alcanzan entre las 13:00 y 15:00 horas, alcanzando un máximo

diario promedio de unos 2000 metros de altura entre los meses de diciembre a febrero y un valor

máximo diario considerablemente más bajo durante los meses de invierno, donde el promedio del

máximo diario en el mes de julio alcanza solo unos 700 metros de altura, se presenta una alta amplitud

estacional de la altura capa de mezcla debido a la lejanía de la costa. Se puede apreciar que la altura de

capa de mezcla se eleva más temprano y baja más tarde durante los meses de verano, mientras que en

los meses de invierno la capa de mezcla se mantiene durante más horas en niveles bajos, debido

principalmente a que las horas de luz diurna son menores en invierno. La variación temporal de la altura

de capa de mezcla modelada, tanto estacional como horaria, presenta un patrón típico de este

parámetro.

**Figura 6.28: Ciclo diario modelado altura de capa de mezcla.**

**Estación Nuevo Amanecer. Año 2018.**

Fuente: Elaboración propia

55

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

###### 6.5.1 Análisis necesidad de uso de factor de ajuste del modelo meteorológico en base a la velocidad del viento observada y modelada

A partir de los datos observados y modelados en las estaciones Nuevo Amanecer y Catemu, se obtiene

un factor de corrección para las concentraciones estimadas con el modelo de dispersión, suponiendo de

manera conservadora, que las concentraciones atmosféricas presentan una relación lineal inversa con la

mediana de la velocidad del viento anual, en razón de 1:1. De esta manera se obtiene un factor de

corrección a partir del promedio de las razones entre la mediana de la velocidad del viento modelada y la

mediana de la velocidad del viento observada en ambas estaciones, obteniendo un factor de corrección

de 1,16, se repite lo mismo pero utilizando los promedio de velocidades, en este caso se obtiene un

factor de corrección de 1,21, los detalles se muestran en la Tabla 6-9. Como este factor es levemente

mayor a 1 y por otra parte el modelo estima una frecuencia de calmas considerablemente más alta que

la de los datos observados, tal como se muestra en la misma tabla, se desestima la necesidad de utilizar

un factor de corrección en las concentraciones estimadas por el modelo.

**Tabla 6-9:** **Factor de corrección** **.**

|Col1|Nuevo Amanecer|Catemu Met.|Promedio|
|---|---|---|---|
|Razón VV mod/obs promedio|1,35|1,08|1,21|
|Razón VV mod/obs mediana|1,11|1,20|1,16|

|Col1|Nuevo Amanecer|Col3|Catemu Met|Col5|
|---|---|---|---|---|
|**Variable**|**Observado**|**Modelado**|**Observado**|**Modelado**|
|Promedio (m/s)|1,25|1,69|4,07|4,38|
|Mediana (m/s)|0,90|1,00|3,50|4,20|
|Máximo (m/s)|4,80|12,80|12,70|13,40|
|Porcentaje de calmas|26,3%|40,7%|1,7%|9,6%|

Fuente: Elaboración propia

56

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

###### 6.5.2 Conclusiones modelo meteorológico

Se realiza una modelación con el modelo WRF para el año 2018, cuyo desempeño para la estimación de

vientos y temperatura se evaluó en la estación Nuevo Amanecer, la que está ubicada a menos de 500

metros al sureste de Mina Patricia y de manera complementaria se evaluaron los vientos en estación

meteorológica Catemu ubicada a 8 kilómetros al sur del proyecto. En la estación Nuevo amanecer el

modelo presenta un sesgo normalizado para el promedio de la magnitud del viento de un 11% y para la

mediana y de un 35% para promedio y en la estación Catemu este sesgo de un 20% para la mediana y de

un 8% para el promedio, en conclusión el sesgo entre las velocidades modeladas y observadas en las dos

estaciones evaluadas es bajo. Las rosas de vientos modeladas y observadas presentan una baja

concordancia en estación Nuevo Amanecer y un nivel de concordancia mucho más alto en el caso de la

estación meteorológica Catemu. La poca concordancia de la dirección del viento en Nuevo Amanecer en

mayor o menor manera se debe a dos razones: una situación meteorológica de microescala que el

modelo no es capaz de resolver debido a la alta complejidad geomorfológica de la zona o a la

incertidumbre en el monitoreo de la dirección del viento, respecto a esto último, al comparar las rosas

de vientos medidas entre los años 2014 y 2018, estas presentan diferencias importantes, lo que puede

indicar una alta incertidumbre en la dirección de vientos que se está midiendo en esa estación monitora.

Para el caso de la temperatura el modelo presenta un sesgo positivo de 1,2 °C en Nuevo Amanecer y una

correlación alta.

A partir de los datos de la magnitud del viento observados y modelados en las estaciones Nuevo

Amanecer y meteorológica Catemu se obtuvo un factor de corrección de 1,16. Como este factor es

levemente mayor a 1 y por otra parte el modelo estima una frecuencia de calmas considerablemente

más alta que la de los datos observados, se desestima la necesidad de utilizar un factor de corrección en

las concentraciones estimadas por el modelo.

Finalmente se analizó cualitativamente el comportamiento de la altura de capa de mezcla promedio

horaria por mes del año, cualitativamente ya que no existen datos medidos del parámetro, la cual

presenta un comportamiento estimado satisfactorio respecto al ciclo diario y estacional de dicho

parámetro.

57

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

##### 7 MODELO CALIDAD DEL AIRE 7.1 Justificación modelo calidad del aire

De acuerdo con lo establecido en la Guía para el uso de Modelos de Calidad del Aire en el SEIA, la

selección del modelo de Calidad del Aire se basa en la topografía compleja del área donde se emplaza el

proyecto y al alcance de las emisiones. Por esta razón, el modelo utilizado fue un modelo tipo “Puff”

como lo es CALPUFF.

##### 7.2 Descripción modelo de calidad del aire

La simulación del aporte del proyecto a las concentraciones de contaminantes se realizará mediante el

modelo CALPUFF, recomendado por la U.S. EPA para la evaluación de dispersión de contaminantes

desde fuentes continuas.

CALPUFF es un sistema de modelación avanzado para calidad del aire que considera además la

meteorología de carácter no permanente. Su desarrollo estuvo a cargo del “Sigma Research
Corporation”, mientras que su mantenimiento actual es responsabilidad de Exponent [7] . Debido a su

desempeño,

CALPUFF fue catalogado por la USEPA como modelo recomendado [8] para la evaluación del impacto en la

calidad del aire de distintos tipos de proyectos, especialmente aquellos donde es necesario considerar la

variación en el tiempo y en el espacio de las condiciones meteorológicas y su incidencia en el transporte,

transformación y remoción de contaminantes.

El sistema de modelación está compuesto por los siguientes componentes principales:

 - CALMET: es un modelo meteorológico que genera campos de viento tridimensionales horarios,

en base a registros superficiales y del perfil de altura. Además, las salidas de este modelo

entregan información en el dominio de la modelación sobre alturas de la capa de mezcla,

características superficiales y propiedades de dispersión.

 - CALPUFF: corresponde a un modelo Lagrangiano-Gaussiano de transporte y dispersión de soplos

o “puff” emitidos por las fuentes consideradas por el proyecto. De esta forma, a partir de la

información de emisiones y meteorología proporcionada, el programa simula el proceso de

7 [www.src.com/calpuff/calpuff1.htm](http://www.src.com/calpuff/calpuff1.htm)
8 Los modelos de dispersión y calidad del aire recomendados por USEPA, así como su campo de aplicación, están contenidos en
el Appendix W del 40 CFR Part 51 “Directrices para Modelos de Calidad del Aire”
( [http://www.epa.gov/scram001/guidance_permit.htm#appw](http://www.epa.gov/scram001/guidance_permit.htm#appw) ).

58

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

dispersión y transformación de los contaminantes, en un rango de validez desde metros hasta

cientos de kilómetros.

 - CALPOST: es un programa utilizado para el post-procesamiento de los resultados obtenidos en la

modelación de CALPUFF, permitiendo calcular las concentraciones en los receptores según los

promedios requeridos por cada norma. Además, es capaz de gestionar los datos de cada

contaminante según el período de tiempo requerido, ordenando las máximas concentraciones

obtenidas e identificando el momento en que cada una de éstas suceden (hora, día, mes y año).

Dentro de las capacidades del sistema de modelación se destacan los siguientes puntos:

 - Permite modelar transporte de largo alcance (hasta 200 Km).

 - Simula procesos meteorológicos complejos tales como: velocidades de vientos muy bajas,

estancamiento, fumigación y recirculación.

 - Es capaz de incorporar efectos debidos a la proximidad al borde costero o a causa de topografía

compleja.

 - Modela contaminantes de forma simultánea fuentes de diverso tipo y que modifican su nivel de

actividad a lo largo del tiempo.

 - Permite diferenciar entre contaminantes inertes y aquellos que experimentan transformaciones

de primer orden.

El modelo en esta ocasión se utilizó con el mecanismo químico Rivad/Isorropia (mech=6 en CALPUFF),

este mecanismo estima la proporción entre el NO y NO 2 y además los nitratos (NO 3 ) y sulfatos (SO 4 ),

éstos fueron agregados a las concentraciones de MP10 y MP2.5 estimadas por el modelo.

Cabe mencionar que, siguiendo los lineamientos de la Guía para el Uso de Modelos de Calidad del Aire

en el SEIA, no fue utilizado el modelo meteorológico CALMET, por esta razón la meteorología modelada

por el modelo meteorológico WRF correspondiente al año 2018, fue procesada en MMIF v3.2 para ser

ingresada al modelo de dispersión CALPUFF de manera directa.

59

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

##### 8 RECEPTORES 8.1 Receptores discretos

Los receptores para evaluar corresponden a 10 receptores discretos donde se evalúa calidad del aire (R1

a R10) y los siguientes 64 receptores (R11 a R74) corresponden a receptores donde se evalúa el impacto

del material particulado sedimentable debido a la presencia de flora y fauna nativas. Las coordenadas de la

totalidad de los receptores de interés se presentan en la Tabla 8-1, lo receptores “E. Nuevo Amanecer” y
“E. Catemu” corresponden a estaciones de calidad del aire, mientras que El Cobre, Ñilhue, Cerrillos de

Catemu, Catemu, Lo Campo, A1 y A3 corresponden a sectores poblados.

**Tabla 8-1.** **Receptores de Interés definidos para la modelación**

|Receptor|Nombre|UTM-X|UTM-Y|
|---|---|---|---|
|R_1|E. Nuevo Amanecer|316.374|6.374.730|
|R_2|El Cobre|316.375|6.374.728|
|R_3|Ñilhue|316.379|6.374.731|
|R_4|Cerrillos de Catemu|316.378|6.374.734|
|R_5|E. Catemu|316.375|6.374.725|
|R_6|Catemu|316.375|6.374.725|
|R_7|E. Met. Catemu|316.375|6.374.722|
|R_8|Lo Campo|316.381|6.374.723|
|R_9|A1 (sector sur El Seco)|316.374|6.374.745|
|R_10|A3 (sector norte El Seco)|316.374|6.374.746|
|R_11|F4|316.373|6.374.747|
|R_12|MPS 1|316.373|6.374.726|
|R_13|MPS 2|316.374|6.374.727|
|R_14|MPS 3|316.375|6.374.728|
|R_15|MPS 4|316.374|6.374.728|
|R_16|MPS 5|316.374|6.374.729|
|R_17|MPS 6|316.374|6.374.729|
|R_18|MPS 7|316.374|6.374.730|
|R_19|MPS 8|316.373|6.374.726|
|R_20|MPS 9|316.373|6.374.726|
|R_21|MPS 10|316.373|6.374.726|
|R_22|MPS 11|316.373|6.374.726|
|R_23|MPS 12|316.373|6.374.727|
|R_24|MPS 13|316.373|6.374.727|
|R_25|MPS 14|316.373|6.374.727|
|R_26|MPS 15|316.374|6.374.727|
|R_27|MPS 16|316.374|6.374.727|
|R_28|MPS 17|316.374|6.374.727|

60

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

|Receptor|Nombre|UTM-X|UTM-Y|
|---|---|---|---|
|R_29|MPS 18|316.374|6.374.727|
|R_30|MPS 19|316.374|6.374.727|
|R_31|MPS 20|316.374|6.374.727|
|R_32|MPS 21|316.375|6.374.727|
|R_33|MPS 22|316.375|6.374.727|
|R_34|MPS 23|316.375|6.374.727|
|R_35|MPS 24|316.374|6.374.727|
|R_36|MPS 25|316.374|6.374.727|
|R_37|MPS 26|316.374|6.374.727|
|R_38|MPS 27|316.375|6.374.727|
|R_39|MPS 28|316.374|6.374.728|
|R_40|MPS 29|316.374|6.374.728|
|R_41|MPS 30|316.374|6.374.728|
|R_42|MPS 31|316.375|6.374.728|
|R_43|MPS 32|316.375|6.374.728|
|R_44|MPS 33|316.374|6.374.728|
|R_45|MPS 34|316.375|6.374.728|
|R_46|MPS 35|316.374|6.374.728|
|R_47|MPS 36|316.375|6.374.728|
|R_48|MPS 37|316.375|6.374.728|
|R_49|MPS 38|316.374|6.374.728|
|R_50|MPS 39|316.374|6.374.728|
|R_51|MPS 40|316.374|6.374.728|
|R_52|MPS 41|316.374|6.374.728|
|R_53|MPS 42|316.374|6.374.728|
|R_54|MPS 43|316.374|6.374.729|
|R_55|MPS 44|316.374|6.374.729|
|R_56|MPS 45|316.374|6.374.729|
|R_57|MPS 46|316.374|6.374.729|
|R_58|MPS 47|316.374|6.374.729|
|R_59|MPS 48|316.374|6.374.729|
|R_60|MPS 49|316.374|6.374.729|
|R_61|MPS 50|316.374|6.374.729|
|R_62|MPS 51|316.374|6.374.729|
|R_63|MPS 52|316.374|6.374.730|
|R_64|MPS 53|316.374|6.374.730|
|R_65|MPS 54|316.374|6.374.730|
|R_66|MPS 55|316.374|6.374.730|
|R_67|MPS 56|316.374|6.374.730|
|R_68|MPS 57|316.374|6.374.730|
|R_69|MPS 58|316.374|6.374.730|

61

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

|Receptor|Nombre|UTM-X|UTM-Y|
|---|---|---|---|
|R_70|MPS 59|316.374|6.374.730|
|R_71|MPS 60|316.374|6.374.730|
|R_72|MPS 61|316.374|6.374.731|
|R_73|MPS 62|316.374|6.374.730|
|R_74|MPS 63|316.374|6.374.730|

Fuente: Elaboración propia.

##### 8.2 Receptores grilla

Para la modelación de cada escenario se generó una grilla de receptores con una resolución espacial de

1.000 × 1.000 metros, resolución concordante con la resolución del modelo meteorológico, con una

extensión de 38 × 47 km. Finalmente, el área de modelación considerada y la grilla de receptores se

observan en la Figura 8-1. A partir de estos receptores se generan mapas de isoconcentraciones para

cada uno de los contaminantes analizados.

**Figura 8-1. Grilla de receptores**

Fuente: Elaboración propia.

62

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

##### 9 FUENTES DE EMISIÓN

En la Tabla 9-1 y Tabla 9-2 se resume las emisiones ingresadas al modelo, que corresponden a las

emisiones de la situación actual y situación de operación futura, respectivamente, del complejo minero.

**Tabla 9-1 Resumen de emisiones incorporadas al modelo situación actual (base).**

|Actividad|Resumen emisiones situación actual (t/año)|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Actividad**|**MP30**|**MP10**|**MP2,5**|**HC**|**NOx**|**CO**|**NH3 **|**SO2 **|
|Transferencia de material|0,23|0,11|0,02|-|-|-|-|-|
|Tránsito en camino no<br>pavimentado|11,38|2,01|0,49|-|-|-|-|-|
|Tránsito en camino<br>pavimentado|3,59|0,69|0,17|-|-|-|-|-|
|Combustión vehicular|0,03|0,03|0,03|0,07|1,21|0,31|0,00|0,14|
|Maquinaria|0,77|0,77|0,75|1,24|8,89|8,28|-|0,03|
|Generadores|1,61|0,81|0,19|0,00|22,95|4,96|0,04|1,22|
|**Total (t/año)**|**17,61**|**4,42**|**1,64**|**1,31**|**33,05**|**13,55**|**0,04**|**1,38**|

Fuente: Elaboración propia.

**Tabla 9-2 Resumen de emisiones incorporadas al modelo fase de operación.**

|Actividad|Resumen emisiones fase de operación (t/año)|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Actividad**|**MP30**|**MP10**|**MP2,5**|**HC**|**NOx**|**CO**|**NH3 **|**SO2 **|
|Transferencia de material|0,51|0,24|0,04|-|-|-|-|-|
|Tránsito en camino no<br>pavimentado|55,79|9,87|2,39|-|-|-|-|-|
|Tránsito en camino<br>pavimentado|1,84|0,35|0,09|-|-|-|-|-|
|Combustión vehicular|0,06|0,06|0,06|0,14|2,21|0,62|0,00|0,25|
|Maquinaria|1,38|1,38|1,34|2,23|15,78|14,85|-|0,05|
|Generadores|3,89|1,95|0,47|0,00|55,41|11,97|0,10|2,94|
|**Total (t/año)**|**63,47**|**13,86**|**4,38**|**2,36**|**73,40**|**27,44**|**0,10**|**3,24**|

Fuente: Elaboración propia.

63

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**Figura 9-1. Fuentes emisoras ingresadas al modelo**

Fuente: Elaboración propia.

##### 10 RESULTADOS

A continuación, se presentan los resultados de concentración ambiental obtenidos a partir de emisiones

del modelo de dispersión, para los escenarios correspondientes a la operación actual (base) y operación

futura de Minas 3H.

##### 10.1 Análisis de resultados de modelación

###### 10.1.1 Aporte modelado

A continuación, se presentan los aportes, de ambos escenarios modelados, en los receptores discretos,

considerando los estadígrafos de las normas de calidad aplicables MP10, MP2,5, NO 2, SO 2, CO y MPS.

Cabe recordar que tanto el MP10 como el MP2.5 estimado por el modelo consideran la formación de

nitratos y sulfatos provenientes del NOx y SO 2 respectivamente.

64

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

En la Tabla 10-1 se muestran los resultados del modelo de dispersión en los distintos receptores de

interés para la situación actual (base) del Proyecto, los primeros 10 receptores corresponden a sitios

poblados, mientras que los receptores restantes corresponden a sitios de interés por protección de flora

o fauna. Los mayores aportes en la situación actual del Proyecto se presentan en la estación Nuevo

Amanecer y receptores A1 y A3. La Tabla 10-2 muestra la misma información, pero para fase de

operación futura del Proyecto, donde los principales aportes también se presentan en los mismos tres

receptores antes mencionados.

En la Tabla 10-3 se muestra el aporte neto del Proyecto, al descontar del aporte de la operación futura

de Minas 3H el aporte actual del complejo. En la Tabla 10-4 se muestra que solo en el receptor A1 se

supera muy levemente el 1% de la norma anual de MP10 y las normas de MP2.5. Ya en Nuevo Amanecer

los aportes son menores al 1% de las normas respectivas. Para el caso del MPS no se supera el 42% de la

norma de referencia en ninguno de los puntos evaluados, pese a la cercanía de los receptores de interés

a las fuentes emisoras evaluadas.

Por último la Tabla 10-5 muestra el porcentaje respecto a las normas del aporte total de la operación

futura del Proyecto, sin descontar la operación actual (la cual ya es parte de la línea de base), en este

caso es posible verificar que en ningún punto se supera el 2% de las respectivas normas, con la

excepción del NO 2 horario, el cual llega a un 4,1%.

65

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**Tabla 10-1 Resultados del modelo para el aporte del proyecto en situación actual (base) [μg/m** **[3]** **].**

|Receptor|Nombre|MP10 anual|MP10 diario|MP2.5 anual|MP2.5 diario|NO anual<br>2|NO horario<br>2|SO anual<br>2|SO diario<br>2|SO horario<br>2|CO 1h|CO 8h|MPS anual|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R_1|E. Nuevo Amanecer|0,35|0,69|0,12|0,24|0,53|9,33|0,03|0,08|0,16|5,03|1,41|2,47|
|R_2|El Cobre|0,17|0,33|0,05|0,11|0,28|1,79|0,03|0,06|0,11|0,79|0,30|-|
|R_3|Ñilhue|0,01|0,03|0,01|0,02|0,07|1,24|0,00|0,01|0,01|0,33|0,10|-|
|R_4|Cerrillos de Catemu|0,01|0,03|0,01|0,02|0,07|1,67|0,00|0,01|0,02|0,40|0,11|-|
|R_5|E. Catemu|0,05|0,29|0,02|0,12|0,13|1,79|0,01|0,07|0,15|0,58|0,39|-|
|R_6|Catemu|0,09|0,42|0,03|0,18|0,16|2,17|0,02|0,10|0,21|0,73|0,51|-|
|R_7|E. Met Catemu|0,01|0,02|0,00|0,02|0,04|0,37|0,00|0,01|0,01|0,10|0,04|-|
|R_8|Lo Campo|0,00|0,01|0,00|0,01|0,02|0,13|0,00|0,00|0,00|0,04|0,02|-|
|R_9|A1|0,21|0,49|0,08|0,18|0,46|10,47|0,03|0,07|0,15|6,27|1,28|-|
|R_10|A3|0,71|1,35|0,22|0,42|0,67|7,45|0,04|0,10|0,20|4,35|2,17|-|
|R_11|F4|-|-|-|-|-|-|-|-|-|-|-|33,20|
|R_12|MPS 1|-|-|-|-|-|-|-|-|-|-|-|12,22|
|R_13|MPS 2|-|-|-|-|-|-|-|-|-|-|-|40,55|
|R_14|MPS 3|-|-|-|-|-|-|-|-|-|-|-|33,10|
|R_15|MPS 4|-|-|-|-|-|-|-|-|-|-|-|42,01|
|R_16|MPS 5|-|-|-|-|-|-|-|-|-|-|-|22,84|
|R_17|MPS 6|-|-|-|-|-|-|-|-|-|-|-|43,95|
|R_18|MPS 7|-|-|-|-|-|-|-|-|-|-|-|64,12|
|R_19|MPS 8|-|-|-|-|-|-|-|-|-|-|-|12,34|
|R_20|MPS 9|-|-|-|-|-|-|-|-|-|-|-|26,58|
|R_21|MPS 10|-|-|-|-|-|-|-|-|-|-|-|16,82|
|R_22|MPS 11|-|-|-|-|-|-|-|-|-|-|-|5,63|
|R_23|MPS 12|-|-|-|-|-|-|-|-|-|-|-|3,93|
|R_24|MPS 13|-|-|-|-|-|-|-|-|-|-|-|32,22|
|R_25|MPS 14|-|-|-|-|-|-|-|-|-|-|-|36,99|
|R_26|MPS 15|-|-|-|-|-|-|-|-|-|-|-|12,51|
|R_27|MPS 16|-|-|-|-|-|-|-|-|-|-|-|43,85|
|R_28|MPS 17|-|-|-|-|-|-|-|-|-|-|-|39,75|
|R_29|MPS 18|-|-|-|-|-|-|-|-|-|-|-|41,05|
|R_30|MPS 19|-|-|-|-|-|-|-|-|-|-|-|38,22|
|R_31|MPS 20|-|-|-|-|-|-|-|-|-|-|-|32,80|

66

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

|Receptor|Nombre|MP10 anual|MP10 diario|MP2.5 anual|MP2.5 diario|NO anual<br>2|NO horario<br>2|SO anual<br>2|SO diario<br>2|SO horario<br>2|CO 1h|CO 8h|MPS anual|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R_32|MPS 21|-|-|-|-|-|-|-|-|-|-|-|4,90|
|R_33|MPS 22|-|-|-|-|-|-|-|-|-|-|-|26,10|
|R_34|MPS 23|-|-|-|-|-|-|-|-|-|-|-|41,14|
|R_35|MPS 24|-|-|-|-|-|-|-|-|-|-|-|54,26|
|R_36|MPS 25|-|-|-|-|-|-|-|-|-|-|-|76,85|
|R_37|MPS 26|-|-|-|-|-|-|-|-|-|-|-|76,82|
|R_38|MPS 27|-|-|-|-|-|-|-|-|-|-|-|83,00|
|R_39|MPS 28|-|-|-|-|-|-|-|-|-|-|-|72,11|
|R_40|MPS 29|-|-|-|-|-|-|-|-|-|-|-|57,42|
|R_41|MPS 30|-|-|-|-|-|-|-|-|-|-|-|67,57|
|R_42|MPS 31|-|-|-|-|-|-|-|-|-|-|-|62,67|
|R_43|MPS 32|-|-|-|-|-|-|-|-|-|-|-|48,23|
|R_44|MPS 33|-|-|-|-|-|-|-|-|-|-|-|52,66|
|R_45|MPS 34|-|-|-|-|-|-|-|-|-|-|-|25,12|
|R_46|MPS 35|-|-|-|-|-|-|-|-|-|-|-|47,27|
|R_47|MPS 36|-|-|-|-|-|-|-|-|-|-|-|40,59|
|R_48|MPS 37|-|-|-|-|-|-|-|-|-|-|-|37,41|
|R_49|MPS 38|-|-|-|-|-|-|-|-|-|-|-|42,09|
|R_50|MPS 39|-|-|-|-|-|-|-|-|-|-|-|42,86|
|R_51|MPS 40|-|-|-|-|-|-|-|-|-|-|-|34,46|
|R_52|MPS 41|-|-|-|-|-|-|-|-|-|-|-|30,75|
|R_53|MPS 42|-|-|-|-|-|-|-|-|-|-|-|41,10|
|R_54|MPS 43|-|-|-|-|-|-|-|-|-|-|-|39,85|
|R_55|MPS 44|-|-|-|-|-|-|-|-|-|-|-|44,28|
|R_56|MPS 45|-|-|-|-|-|-|-|-|-|-|-|49,93|
|R_57|MPS 46|-|-|-|-|-|-|-|-|-|-|-|22,21|
|R_58|MPS 47|-|-|-|-|-|-|-|-|-|-|-|22,11|
|R_59|MPS 48|-|-|-|-|-|-|-|-|-|-|-|49,96|
|R_60|MPS 49|-|-|-|-|-|-|-|-|-|-|-|53,25|
|R_61|MPS 50|-|-|-|-|-|-|-|-|-|-|-|74,31|
|R_62|MPS 51|-|-|-|-|-|-|-|-|-|-|-|33,17|
|R_63|MPS 52|-|-|-|-|-|-|-|-|-|-|-|91,57|
|R_64|MPS 53|-|-|-|-|-|-|-|-|-|-|-|36,73|
|R_65|MPS 54|-|-|-|-|-|-|-|-|-|-|-|116,31|

67

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

|Receptor|Nombre|MP10 anual|MP10 diario|MP2.5 anual|MP2.5 diario|NO anual<br>2|NO horario<br>2|SO anual<br>2|SO diario<br>2|SO horario<br>2|CO 1h|CO 8h|MPS anual|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R_66|MPS 55|-|-|-|-|-|-|-|-|-|-|-|110,88|
|R_67|MPS 56|-|-|-|-|-|-|-|-|-|-|-|118,28|
|R_68|MPS 57|-|-|-|-|-|-|-|-|-|-|-|111,58|
|R_69|MPS 58|-|-|-|-|-|-|-|-|-|-|-|16,79|
|R_70|MPS 59|-|-|-|-|-|-|-|-|-|-|-|18,34|
|R_71|MPS 60|-|-|-|-|-|-|-|-|-|-|-|81,09|
|R_72|MPS 61|-|-|-|-|-|-|-|-|-|-|-|52,04|
|R_73|MPS 62|-|-|-|-|-|-|-|-|-|-|-|18,51|
|R_74|MPS 63|-|-|-|-|-|-|-|-|-|-|-|6,57|

Fuente: Elaboración propia.

**Tabla 10-2 Resultados del modelo para el aporte del proyecto en fase operación futura [μg/m** **[3]** **].**

|Receptor|Nombre|MP10 anual|MP10 diario|MP2.5 anual|MP2.5 diario|NO anual<br>2|NO horario<br>2|SO anual<br>2|SO diario<br>2|SO horario<br>2|CO 1h|CO 8h|MPS anual|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R_1|E. Nuevo Amanecer|0,65|1,36|0,27|0,58|0,96|14,69|0,04|0,10|0,17|8,94|2,52|3,75|
|R_2|El Cobre|0,15|0,27|0,06|0,12|0,30|3,62|0,02|0,04|0,06|1,25|0,46|-|
|R_3|Ñilhue|0,03|0,07|0,02|0,06|0,13|1,80|0,00|0,01|0,02|0,64|0,22|-|
|R_4|Cerrillos de Catemu|0,03|0,06|0,02|0,05|0,14|2,54|0,01|0,01|0,03|0,66|0,21|-|
|R_5|E. Catemu|0,06|0,20|0,03|0,09|0,14|1,75|0,01|0,04|0,08|0,63|0,23|-|
|R_6|Catemu|0,08|0,28|0,04|0,12|0,17|2,30|0,01|0,05|0,10|0,72|0,30|-|
|R_7|E. Met Catemu|0,02|0,04|0,01|0,03|0,07|0,70|0,00|0,01|0,01|0,19|0,09|-|
|R_8|Lo Campo|0,01|0,02|0,01|0,02|0,04|0,26|0,00|0,00|0,01|0,08|0,04|-|
|R_9|A1|0,86|1,72|0,37|0,84|0,98|16,39|0,05|0,12|0,20|11,49|2,35|-|
|R_10|A3|0,92|2,08|0,34|0,74|1,11|13,52|0,04|0,10|0,17|7,80|4,02|-|
|R_11|F4|-|-|-|-|-|-|-|-|-|-|-|33,20|
|R_12|MPS 1|-|-|-|-|-|-|-|-|-|-|-|12,22|
|R_13|MPS 2|-|-|-|-|-|-|-|-|-|-|-|40,55|
|R_14|MPS 3|-|-|-|-|-|-|-|-|-|-|-|33,10|
|R_15|MPS 4|-|-|-|-|-|-|-|-|-|-|-|42,01|
|R_16|MPS 5|-|-|-|-|-|-|-|-|-|-|-|22,84|
|R_17|MPS 6|-|-|-|-|-|-|-|-|-|-|-|43,95|
|R_18|MPS 7|-|-|-|-|-|-|-|-|-|-|-|64,12|
|R_19|MPS 8|-|-|-|-|-|-|-|-|-|-|-|12,34|
|R_20|MPS 9|-|-|-|-|-|-|-|-|-|-|-|26,58|

68

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

|Receptor|Nombre|MP10 anual|MP10 diario|MP2.5 anual|MP2.5 diario|NO anual<br>2|NO horario<br>2|SO anual<br>2|SO diario<br>2|SO horario<br>2|CO 1h|CO 8h|MPS anual|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R_21|MPS 10|-|-|-|-|-|-|-|-|-|-|-|16,82|
|R_22|MPS 11|-|-|-|-|-|-|-|-|-|-|-|5,63|
|R_23|MPS 12|-|-|-|-|-|-|-|-|-|-|-|3,93|
|R_24|MPS 13|-|-|-|-|-|-|-|-|-|-|-|32,22|
|R_25|MPS 14|-|-|-|-|-|-|-|-|-|-|-|36,99|
|R_26|MPS 15|-|-|-|-|-|-|-|-|-|-|-|12,51|
|R_27|MPS 16|-|-|-|-|-|-|-|-|-|-|-|43,85|
|R_28|MPS 17|-|-|-|-|-|-|-|-|-|-|-|39,75|
|R_29|MPS 18|-|-|-|-|-|-|-|-|-|-|-|41,05|
|R_30|MPS 19|-|-|-|-|-|-|-|-|-|-|-|38,22|
|R_31|MPS 20|-|-|-|-|-|-|-|-|-|-|-|32,80|
|R_32|MPS 21|-|-|-|-|-|-|-|-|-|-|-|4,90|
|R_33|MPS 22|-|-|-|-|-|-|-|-|-|-|-|26,10|
|R_34|MPS 23|-|-|-|-|-|-|-|-|-|-|-|41,14|
|R_35|MPS 24|-|-|-|-|-|-|-|-|-|-|-|54,26|
|R_36|MPS 25|-|-|-|-|-|-|-|-|-|-|-|76,85|
|R_37|MPS 26|-|-|-|-|-|-|-|-|-|-|-|76,82|
|R_38|MPS 27|-|-|-|-|-|-|-|-|-|-|-|83,00|
|R_39|MPS 28|-|-|-|-|-|-|-|-|-|-|-|72,11|
|R_40|MPS 29|-|-|-|-|-|-|-|-|-|-|-|57,42|
|R_41|MPS 30|-|-|-|-|-|-|-|-|-|-|-|67,57|
|R_42|MPS 31|-|-|-|-|-|-|-|-|-|-|-|62,67|
|R_43|MPS 32|-|-|-|-|-|-|-|-|-|-|-|48,23|
|R_44|MPS 33|-|-|-|-|-|-|-|-|-|-|-|52,66|
|R_45|MPS 34|-|-|-|-|-|-|-|-|-|-|-|25,12|
|R_46|MPS 35|-|-|-|-|-|-|-|-|-|-|-|47,27|
|R_47|MPS 36|-|-|-|-|-|-|-|-|-|-|-|40,59|
|R_48|MPS 37|-|-|-|-|-|-|-|-|-|-|-|37,41|
|R_49|MPS 38|-|-|-|-|-|-|-|-|-|-|-|42,09|
|R_50|MPS 39|-|-|-|-|-|-|-|-|-|-|-|42,86|
|R_51|MPS 40|-|-|-|-|-|-|-|-|-|-|-|34,46|
|R_52|MPS 41|-|-|-|-|-|-|-|-|-|-|-|30,75|
|R_53|MPS 42|-|-|-|-|-|-|-|-|-|-|-|41,10|
|R_54|MPS 43|-|-|-|-|-|-|-|-|-|-|-|39,85|

69

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

|Receptor|Nombre|MP10 anual|MP10 diario|MP2.5 anual|MP2.5 diario|NO anual<br>2|NO horario<br>2|SO anual<br>2|SO diario<br>2|SO horario<br>2|CO 1h|CO 8h|MPS anual|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R_55|MPS 44|-|-|-|-|-|-|-|-|-|-|-|44,28|
|R_56|MPS 45|-|-|-|-|-|-|-|-|-|-|-|49,93|
|R_57|MPS 46|-|-|-|-|-|-|-|-|-|-|-|22,21|
|R_58|MPS 47|-|-|-|-|-|-|-|-|-|-|-|22,11|
|R_59|MPS 48|-|-|-|-|-|-|-|-|-|-|-|49,96|
|R_60|MPS 49|-|-|-|-|-|-|-|-|-|-|-|53,25|
|R_61|MPS 50|-|-|-|-|-|-|-|-|-|-|-|74,31|
|R_62|MPS 51|-|-|-|-|-|-|-|-|-|-|-|33,17|
|R_63|MPS 52|-|-|-|-|-|-|-|-|-|-|-|91,57|
|R_64|MPS 53|-|-|-|-|-|-|-|-|-|-|-|36,73|
|R_65|MPS 54|-|-|-|-|-|-|-|-|-|-|-|116,31|
|R_66|MPS 55|-|-|-|-|-|-|-|-|-|-|-|110,88|
|R_67|MPS 56|-|-|-|-|-|-|-|-|-|-|-|118,28|
|R_68|MPS 57|-|-|-|-|-|-|-|-|-|-|-|111,58|
|R_69|MPS 58|-|-|-|-|-|-|-|-|-|-|-|16,79|
|R_70|MPS 59|-|-|-|-|-|-|-|-|-|-|-|18,34|
|R_71|MPS 60|-|-|-|-|-|-|-|-|-|-|-|81,09|
|R_72|MPS 61|-|-|-|-|-|-|-|-|-|-|-|52,04|
|R_73|MPS 62|-|-|-|-|-|-|-|-|-|-|-|18,51|
|R_74|MPS 63|-|-|-|-|-|-|-|-|-|-|-|6,57|

Fuente: Elaboración propia.

70

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**Tabla 10-3 Resultados del modelo para el delta operación futura en relación a la operación actual [μg/m** **[3]** **].**

|Receptor|Nombre|MP10 anual|MP10 diario|MP2.5 anual|MP2.5 diario|NO anual<br>2|NO horario<br>2|SO anual<br>2|SO diario<br>2|SO horario<br>2|CO 1h|CO 8h|MPS anual|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R_1|E. Nuevo Amanecer|0,31|0,67|0,15|0,34|0,43|5,36|0,01|0,02|0,01|3,91|1,11|1,28|
|R_2|El Cobre|-0,01|-0,05|0,00|0,01|0,02|1,83|-0,01|-0,02|-0,05|0,46|0,17|-|
|R_3|Ñilhue|0,02|0,04|0,01|0,04|0,06|0,56|0,00|0,00|0,01|0,31|0,11|-|
|R_4|Cerrillos de Catemu|0,01|0,04|0,01|0,03|0,07|0,87|0,00|0,01|0,01|0,26|0,10|-|
|R_5|E. Catemu|0,00|-0,09|0,00|-0,03|0,02|-0,04|0,00|-0,03|-0,08|0,05|-0,15|-|
|R_6|Catemu|-0,01|-0,15|0,00|-0,05|0,01|0,14|-0,01|-0,05|-0,11|-0,01|-0,20|-|
|R_7|E. Met Catemu|0,01|0,02|0,01|0,01|0,03|0,33|0,00|0,00|0,00|0,10|0,04|-|
|R_8|Lo Campo|0,01|0,01|0,00|0,01|0,02|0,13|0,00|0,00|0,00|0,04|0,02|-|
|R_9|A1|0,65|1,23|0,29|0,66|0,51|5,92|0,02|0,05|0,05|5,22|1,07|-|
|R_10|A3|0,21|0,73|0,12|0,32|0,44|6,07|0,00|0,00|-0,03|3,45|1,85|-|
|R_11|F4|-|-|-|-|-|-|-|-|-|-|-|16,76|
|R_12|MPS 1|-|-|-|-|-|-|-|-|-|-|-|11,39|
|R_13|MPS 2|-|-|-|-|-|-|-|-|-|-|-|40,43|
|R_14|MPS 3|-|-|-|-|-|-|-|-|-|-|-|32,60|
|R_15|MPS 4|-|-|-|-|-|-|-|-|-|-|-|41,39|
|R_16|MPS 5|-|-|-|-|-|-|-|-|-|-|-|20,79|
|R_17|MPS 6|-|-|-|-|-|-|-|-|-|-|-|36,76|
|R_18|MPS 7|-|-|-|-|-|-|-|-|-|-|-|36,52|
|R_19|MPS 8|-|-|-|-|-|-|-|-|-|-|-|9,46|
|R_20|MPS 9|-|-|-|-|-|-|-|-|-|-|-|25,55|
|R_21|MPS 10|-|-|-|-|-|-|-|-|-|-|-|14,58|
|R_22|MPS 11|-|-|-|-|-|-|-|-|-|-|-|5,24|
|R_23|MPS 12|-|-|-|-|-|-|-|-|-|-|-|3,74|
|R_24|MPS 13|-|-|-|-|-|-|-|-|-|-|-|32,07|
|R_25|MPS 14|-|-|-|-|-|-|-|-|-|-|-|36,89|
|R_26|MPS 15|-|-|-|-|-|-|-|-|-|-|-|12,40|
|R_27|MPS 16|-|-|-|-|-|-|-|-|-|-|-|43,74|
|R_28|MPS 17|-|-|-|-|-|-|-|-|-|-|-|39,64|
|R_29|MPS 18|-|-|-|-|-|-|-|-|-|-|-|40,93|
|R_30|MPS 19|-|-|-|-|-|-|-|-|-|-|-|38,08|
|R_31|MPS 20|-|-|-|-|-|-|-|-|-|-|-|32,66|
|R_32|MPS 21|-|-|-|-|-|-|-|-|-|-|-|4,75|
|R_33|MPS 22|-|-|-|-|-|-|-|-|-|-|-|25,87|

71

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

|Receptor|Nombre|MP10 anual|MP10 diario|MP2.5 anual|MP2.5 diario|NO anual<br>2|NO horario<br>2|SO anual<br>2|SO diario<br>2|SO horario<br>2|CO 1h|CO 8h|MPS anual|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R_34|MPS 23|-|-|-|-|-|-|-|-|-|-|-|40,97|
|R_35|MPS 24|-|-|-|-|-|-|-|-|-|-|-|54,10|
|R_36|MPS 25|-|-|-|-|-|-|-|-|-|-|-|76,69|
|R_37|MPS 26|-|-|-|-|-|-|-|-|-|-|-|76,63|
|R_38|MPS 27|-|-|-|-|-|-|-|-|-|-|-|82,80|
|R_39|MPS 28|-|-|-|-|-|-|-|-|-|-|-|71,91|
|R_40|MPS 29|-|-|-|-|-|-|-|-|-|-|-|57,25|
|R_41|MPS 30|-|-|-|-|-|-|-|-|-|-|-|67,35|
|R_42|MPS 31|-|-|-|-|-|-|-|-|-|-|-|62,41|
|R_43|MPS 32|-|-|-|-|-|-|-|-|-|-|-|47,93|
|R_44|MPS 33|-|-|-|-|-|-|-|-|-|-|-|52,46|
|R_45|MPS 34|-|-|-|-|-|-|-|-|-|-|-|24,75|
|R_46|MPS 35|-|-|-|-|-|-|-|-|-|-|-|46,87|
|R_47|MPS 36|-|-|-|-|-|-|-|-|-|-|-|40,16|
|R_48|MPS 37|-|-|-|-|-|-|-|-|-|-|-|36,89|
|R_49|MPS 38|-|-|-|-|-|-|-|-|-|-|-|41,51|
|R_50|MPS 39|-|-|-|-|-|-|-|-|-|-|-|42,37|
|R_51|MPS 40|-|-|-|-|-|-|-|-|-|-|-|33,86|
|R_52|MPS 41|-|-|-|-|-|-|-|-|-|-|-|30,02|
|R_53|MPS 42|-|-|-|-|-|-|-|-|-|-|-|40,41|
|R_54|MPS 43|-|-|-|-|-|-|-|-|-|-|-|39,02|
|R_55|MPS 44|-|-|-|-|-|-|-|-|-|-|-|43,48|
|R_56|MPS 45|-|-|-|-|-|-|-|-|-|-|-|48,76|
|R_57|MPS 46|-|-|-|-|-|-|-|-|-|-|-|20,84|
|R_58|MPS 47|-|-|-|-|-|-|-|-|-|-|-|18,38|
|R_59|MPS 48|-|-|-|-|-|-|-|-|-|-|-|47,51|
|R_60|MPS 49|-|-|-|-|-|-|-|-|-|-|-|48,22|
|R_61|MPS 50|-|-|-|-|-|-|-|-|-|-|-|60,92|
|R_62|MPS 51|-|-|-|-|-|-|-|-|-|-|-|19,15|
|R_63|MPS 52|-|-|-|-|-|-|-|-|-|-|-|68,91|
|R_64|MPS 53|-|-|-|-|-|-|-|-|-|-|-|5,21|
|R_65|MPS 54|-|-|-|-|-|-|-|-|-|-|-|65,57|
|R_66|MPS 55|-|-|-|-|-|-|-|-|-|-|-|72,50|
|R_67|MPS 56|-|-|-|-|-|-|-|-|-|-|-|72,88|

72

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

|Receptor|Nombre|MP10 anual|MP10 diario|MP2.5 anual|MP2.5 diario|NO anual<br>2|NO horario<br>2|SO anual<br>2|SO diario<br>2|SO horario<br>2|CO 1h|CO 8h|MPS anual|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R_68|MPS 57|-|-|-|-|-|-|-|-|-|-|-|61,19|
|R_69|MPS 58|-|-|-|-|-|-|-|-|-|-|-|-2,34|
|R_70|MPS 59|-|-|-|-|-|-|-|-|-|-|-|1,66|
|R_71|MPS 60|-|-|-|-|-|-|-|-|-|-|-|39,15|
|R_72|MPS 61|-|-|-|-|-|-|-|-|-|-|-|23,48|
|R_73|MPS 62|-|-|-|-|-|-|-|-|-|-|-|-5,03|
|R_74|MPS 63|-|-|-|-|-|-|-|-|-|-|-|-0,60|

Fuente: Elaboración propia.

**Tabla 10-4 Porcentaje del delta operación futura en relación a la operación actual respecto a la norma.**

|Receptor|Nombre|MP10 anual|MP10 diario|MP2.5 anual|MP2.5 diario|NO anual<br>2|NO horario<br>2|SO anual<br>2|SO diario<br>2|SO horario<br>2|CO 1h|CO 8h|MPS anual|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R_1|E. Nuevo Amanecer|0,6%|0,4%|0,8%|0,7%|0,4%|1,3%|0,0%|0,0%|0,0%|0,0%|0,0%|0,6%|
|R_2|El Cobre|0,0%|0,0%|0,0%|0,0%|0,0%|0,5%|0,0%|0,0%|0,0%|0,0%|0,0%|-|
|R_3|Ñilhue|0,0%|0,0%|0,1%|0,1%|0,1%|0,1%|0,0%|0,0%|0,0%|0,0%|0,0%|-|
|R_4|Cerrillos de Catemu|0,0%|0,0%|0,1%|0,1%|0,1%|0,2%|0,0%|0,0%|0,0%|0,0%|0,0%|-|
|R_5|E. Catemu|0,0%|-0,1%|0,0%|-0,1%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|-|
|R_6|Catemu|0,0%|-0,1%|0,0%|-0,1%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|-|
|R_7|E. Met Catemu|0,0%|0,0%|0,0%|0,0%|0,0%|0,1%|0,0%|0,0%|0,0%|0,0%|0,0%|-|
|R_8|Lo Campo|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|-|
|R_9|A1|1,3%|0,8%|1,4%|1,3%|0,5%|1,5%|0,0%|0,0%|0,0%|0,0%|0,0%|-|
|R_10|A3|0,4%|0,5%|0,6%|0,6%|0,4%|1,5%|0,0%|0,0%|0,0%|0,0%|0,0%|-|
|R_11|F4|-|-|-|-|-|-|-|-|-|-|-|8,4%|
|R_12|MPS 1|-|-|-|-|-|-|-|-|-|-|-|5,7%|
|R_13|MPS 2|-|-|-|-|-|-|-|-|-|-|-|20,2%|
|R_14|MPS 3|-|-|-|-|-|-|-|-|-|-|-|16,3%|
|R_15|MPS 4|-|-|-|-|-|-|-|-|-|-|-|20,7%|
|R_16|MPS 5|-|-|-|-|-|-|-|-|-|-|-|10,4%|
|R_17|MPS 6|-|-|-|-|-|-|-|-|-|-|-|18,4%|
|R_18|MPS 7|-|-|-|-|-|-|-|-|-|-|-|18,3%|
|R_19|MPS 8|-|-|-|-|-|-|-|-|-|-|-|4,7%|
|R_20|MPS 9|-|-|-|-|-|-|-|-|-|-|-|12,8%|
|R_21|MPS 10|-|-|-|-|-|-|-|-|-|-|-|7,3%|
|R_22|MPS 11|-|-|-|-|-|-|-|-|-|-|-|2,6%|

73

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

|Receptor|Nombre|MP10 anual|MP10 diario|MP2.5 anual|MP2.5 diario|NO anual<br>2|NO horario<br>2|SO anual<br>2|SO diario<br>2|SO horario<br>2|CO 1h|CO 8h|MPS anual|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R_23|MPS 12|-|-|-|-|-|-|-|-|-|-|-|1,9%|
|R_24|MPS 13|-|-|-|-|-|-|-|-|-|-|-|16,0%|
|R_25|MPS 14|-|-|-|-|-|-|-|-|-|-|-|18,4%|
|R_26|MPS 15|-|-|-|-|-|-|-|-|-|-|-|6,2%|
|R_27|MPS 16|-|-|-|-|-|-|-|-|-|-|-|21,9%|
|R_28|MPS 17|-|-|-|-|-|-|-|-|-|-|-|19,8%|
|R_29|MPS 18|-|-|-|-|-|-|-|-|-|-|-|20,5%|
|R_30|MPS 19|-|-|-|-|-|-|-|-|-|-|-|19,0%|
|R_31|MPS 20|-|-|-|-|-|-|-|-|-|-|-|16,3%|
|R_32|MPS 21|-|-|-|-|-|-|-|-|-|-|-|2,4%|
|R_33|MPS 22|-|-|-|-|-|-|-|-|-|-|-|12,9%|
|R_34|MPS 23|-|-|-|-|-|-|-|-|-|-|-|20,5%|
|R_35|MPS 24|-|-|-|-|-|-|-|-|-|-|-|27,1%|
|R_36|MPS 25|-|-|-|-|-|-|-|-|-|-|-|38,3%|
|R_37|MPS 26|-|-|-|-|-|-|-|-|-|-|-|38,3%|
|R_38|MPS 27|-|-|-|-|-|-|-|-|-|-|-|41,4%|
|R_39|MPS 28|-|-|-|-|-|-|-|-|-|-|-|36,0%|
|R_40|MPS 29|-|-|-|-|-|-|-|-|-|-|-|28,6%|
|R_41|MPS 30|-|-|-|-|-|-|-|-|-|-|-|33,7%|
|R_42|MPS 31|-|-|-|-|-|-|-|-|-|-|-|31,2%|
|R_43|MPS 32|-|-|-|-|-|-|-|-|-|-|-|24,0%|
|R_44|MPS 33|-|-|-|-|-|-|-|-|-|-|-|26,2%|
|R_45|MPS 34|-|-|-|-|-|-|-|-|-|-|-|12,4%|
|R_46|MPS 35|-|-|-|-|-|-|-|-|-|-|-|23,4%|
|R_47|MPS 36|-|-|-|-|-|-|-|-|-|-|-|20,1%|
|R_48|MPS 37|-|-|-|-|-|-|-|-|-|-|-|18,4%|
|R_49|MPS 38|-|-|-|-|-|-|-|-|-|-|-|20,8%|
|R_50|MPS 39|-|-|-|-|-|-|-|-|-|-|-|21,2%|
|R_51|MPS 40|-|-|-|-|-|-|-|-|-|-|-|16,9%|
|R_52|MPS 41|-|-|-|-|-|-|-|-|-|-|-|15,0%|
|R_53|MPS 42|-|-|-|-|-|-|-|-|-|-|-|20,2%|
|R_54|MPS 43|-|-|-|-|-|-|-|-|-|-|-|19,5%|
|R_55|MPS 44|-|-|-|-|-|-|-|-|-|-|-|21,7%|
|R_56|MPS 45|-|-|-|-|-|-|-|-|-|-|-|24,4%|

74

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

|Receptor|Nombre|MP10 anual|MP10 diario|MP2.5 anual|MP2.5 diario|NO anual<br>2|NO horario<br>2|SO anual<br>2|SO diario<br>2|SO horario<br>2|CO 1h|CO 8h|MPS anual|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R_57|MPS 46|-|-|-|-|-|-|-|-|-|-|-|10,4%|
|R_58|MPS 47|-|-|-|-|-|-|-|-|-|-|-|9,2%|
|R_59|MPS 48|-|-|-|-|-|-|-|-|-|-|-|23,8%|
|R_60|MPS 49|-|-|-|-|-|-|-|-|-|-|-|24,1%|
|R_61|MPS 50|-|-|-|-|-|-|-|-|-|-|-|30,5%|
|R_62|MPS 51|-|-|-|-|-|-|-|-|-|-|-|9,6%|
|R_63|MPS 52|-|-|-|-|-|-|-|-|-|-|-|34,5%|
|R_64|MPS 53|-|-|-|-|-|-|-|-|-|-|-|2,6%|
|R_65|MPS 54|-|-|-|-|-|-|-|-|-|-|-|32,8%|
|R_66|MPS 55|-|-|-|-|-|-|-|-|-|-|-|36,2%|
|R_67|MPS 56|-|-|-|-|-|-|-|-|-|-|-|36,4%|
|R_68|MPS 57|-|-|-|-|-|-|-|-|-|-|-|30,6%|
|R_69|MPS 58|-|-|-|-|-|-|-|-|-|-|-|-1,2%|
|R_70|MPS 59|-|-|-|-|-|-|-|-|-|-|-|0,8%|
|R_71|MPS 60|-|-|-|-|-|-|-|-|-|-|-|19,6%|
|R_72|MPS 61|-|-|-|-|-|-|-|-|-|-|-|11,7%|
|R_73|MPS 62|-|-|-|-|-|-|-|-|-|-|-|-2,5%|
|R_74|MPS 63|-|-|-|-|-|-|-|-|-|-|-|-0,3%|

Fuente: Elaboración propia.

75

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**Tabla 10-5 Porcentaje del modelo para el aporte del proyecto en fase operación futura respecto a la norma.**

|Receptor|Nombre|MP10<br>anual|MP10<br>diario|MP2.5<br>anual|MP2.5<br>diario|NO2<br>anual|NO2<br>horario|SO2<br>anual|SO2<br>diario|SO2<br>horario|CO<br>1h|CO<br>8h|MPS<br>anual|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R_1|E. Nuevo Amanecer|1,3%|0,9%|1,3%|1,2%|1,0%|3,7%|0,1%|0,1%|0,0%|0,0%|0,0%|1,9%|
|R_2|El Cobre|0,3%|0,2%|0,3%|0,2%|0,3%|0,9%|0,0%|0,0%|0,0%|0,0%|0,0%|-|
|R_3|Ñilhue|0,1%|0,0%|0,1%|0,1%|0,1%|0,4%|0,0%|0,0%|0,0%|0,0%|0,0%|-|
|R_4|Cerrillos de Catemu|0,1%|0,0%|0,1%|0,1%|0,1%|0,6%|0,0%|0,0%|0,0%|0,0%|0,0%|-|
|R_5|E. Catemu|0,1%|0,1%|0,1%|0,2%|0,1%|0,4%|0,0%|0,0%|0,0%|0,0%|0,0%|-|
|R_6|Catemu|0,2%|0,2%|0,2%|0,2%|0,2%|0,6%|0,0%|0,0%|0,0%|0,0%|0,0%|-|
|R_7|E. Met Catemu|0,0%|0,0%|0,1%|0,1%|0,1%|0,2%|0,0%|0,0%|0,0%|0,0%|0,0%|-|
|R_8|Lo Campo|0,0%|0,0%|0,0%|0,0%|0,0%|0,1%|0,0%|0,0%|0,0%|0,0%|0,0%|-|
|R_9|A1|1,7%|1,1%|1,8%|1,7%|1,0%|4,1%|0,1%|0,1%|0,1%|0,0%|0,0%|-|
|R_10|A3|1,8%|1,4%|1,7%|1,5%|1,1%|3,4%|0,1%|0,1%|0,0%|0,0%|0,0%|-|
|R_11|F4|-|-|-|-|-|-|-|-|-|-|-|16,6%|
|R_12|MPS 1|-|-|-|-|-|-|-|-|-|-|-|6,1%|
|R_13|MPS 2|-|-|-|-|-|-|-|-|-|-|-|20,3%|
|R_14|MPS 3|-|-|-|-|-|-|-|-|-|-|-|16,5%|
|R_15|MPS 4|-|-|-|-|-|-|-|-|-|-|-|21,0%|
|R_16|MPS 5|-|-|-|-|-|-|-|-|-|-|-|11,4%|
|R_17|MPS 6|-|-|-|-|-|-|-|-|-|-|-|22,0%|
|R_18|MPS 7|-|-|-|-|-|-|-|-|-|-|-|32,1%|
|R_19|MPS 8|-|-|-|-|-|-|-|-|-|-|-|6,2%|
|R_20|MPS 9|-|-|-|-|-|-|-|-|-|-|-|13,3%|
|R_21|MPS 10|-|-|-|-|-|-|-|-|-|-|-|8,4%|
|R_22|MPS 11|-|-|-|-|-|-|-|-|-|-|-|2,8%|
|R_23|MPS 12|-|-|-|-|-|-|-|-|-|-|-|2,0%|
|R_24|MPS 13|-|-|-|-|-|-|-|-|-|-|-|16,1%|
|R_25|MPS 14|-|-|-|-|-|-|-|-|-|-|-|18,5%|
|R_26|MPS 15|-|-|-|-|-|-|-|-|-|-|-|6,3%|
|R_27|MPS 16|-|-|-|-|-|-|-|-|-|-|-|21,9%|
|R_28|MPS 17|-|-|-|-|-|-|-|-|-|-|-|19,9%|
|R_29|MPS 18|-|-|-|-|-|-|-|-|-|-|-|20,5%|
|R_30|MPS 19|-|-|-|-|-|-|-|-|-|-|-|19,1%|
|R_31|MPS 20|-|-|-|-|-|-|-|-|-|-|-|16,4%|
|R_32|MPS 21|-|-|-|-|-|-|-|-|-|-|-|2,5%|

76

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

|Receptor|Nombre|MP10<br>anual|MP10<br>diario|MP2.5<br>anual|MP2.5<br>diario|NO2<br>anual|NO2<br>horario|SO2<br>anual|SO2<br>diario|SO2<br>horario|CO<br>1h|CO<br>8h|MPS<br>anual|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R_33|MPS 22|-|-|-|-|-|-|-|-|-|-|-|13,0%|
|R_34|MPS 23|-|-|-|-|-|-|-|-|-|-|-|20,6%|
|R_35|MPS 24|-|-|-|-|-|-|-|-|-|-|-|27,1%|
|R_36|MPS 25|-|-|-|-|-|-|-|-|-|-|-|38,4%|
|R_37|MPS 26|-|-|-|-|-|-|-|-|-|-|-|38,4%|
|R_38|MPS 27|-|-|-|-|-|-|-|-|-|-|-|41,5%|
|R_39|MPS 28|-|-|-|-|-|-|-|-|-|-|-|36,1%|
|R_40|MPS 29|-|-|-|-|-|-|-|-|-|-|-|28,7%|
|R_41|MPS 30|-|-|-|-|-|-|-|-|-|-|-|33,8%|
|R_42|MPS 31|-|-|-|-|-|-|-|-|-|-|-|31,3%|
|R_43|MPS 32|-|-|-|-|-|-|-|-|-|-|-|24,1%|
|R_44|MPS 33|-|-|-|-|-|-|-|-|-|-|-|26,3%|
|R_45|MPS 34|-|-|-|-|-|-|-|-|-|-|-|12,6%|
|R_46|MPS 35|-|-|-|-|-|-|-|-|-|-|-|23,6%|
|R_47|MPS 36|-|-|-|-|-|-|-|-|-|-|-|20,3%|
|R_48|MPS 37|-|-|-|-|-|-|-|-|-|-|-|18,7%|
|R_49|MPS 38|-|-|-|-|-|-|-|-|-|-|-|21,0%|
|R_50|MPS 39|-|-|-|-|-|-|-|-|-|-|-|21,4%|
|R_51|MPS 40|-|-|-|-|-|-|-|-|-|-|-|17,2%|
|R_52|MPS 41|-|-|-|-|-|-|-|-|-|-|-|15,4%|
|R_53|MPS 42|-|-|-|-|-|-|-|-|-|-|-|20,5%|
|R_54|MPS 43|-|-|-|-|-|-|-|-|-|-|-|19,9%|
|R_55|MPS 44|-|-|-|-|-|-|-|-|-|-|-|22,1%|
|R_56|MPS 45|-|-|-|-|-|-|-|-|-|-|-|25,0%|
|R_57|MPS 46|-|-|-|-|-|-|-|-|-|-|-|11,1%|
|R_58|MPS 47|-|-|-|-|-|-|-|-|-|-|-|11,1%|
|R_59|MPS 48|-|-|-|-|-|-|-|-|-|-|-|25,0%|
|R_60|MPS 49|-|-|-|-|-|-|-|-|-|-|-|26,6%|
|R_61|MPS 50|-|-|-|-|-|-|-|-|-|-|-|37,2%|
|R_62|MPS 51|-|-|-|-|-|-|-|-|-|-|-|16,6%|
|R_63|MPS 52|-|-|-|-|-|-|-|-|-|-|-|45,8%|
|R_64|MPS 53|-|-|-|-|-|-|-|-|-|-|-|18,4%|
|R_65|MPS 54|-|-|-|-|-|-|-|-|-|-|-|58,2%|

77

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

|Receptor|Nombre|MP10<br>anual|MP10<br>diario|MP2.5<br>anual|MP2.5<br>diario|NO2<br>anual|NO2<br>horario|SO2<br>anual|SO2<br>diario|SO2<br>horario|CO<br>1h|CO<br>8h|MPS<br>anual|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R_66|MPS 55|-|-|-|-|-|-|-|-|-|-|-|55,4%|
|R_67|MPS 56|-|-|-|-|-|-|-|-|-|-|-|59,1%|
|R_68|MPS 57|-|-|-|-|-|-|-|-|-|-|-|55,8%|
|R_69|MPS 58|-|-|-|-|-|-|-|-|-|-|-|8,4%|
|R_70|MPS 59|-|-|-|-|-|-|-|-|-|-|-|9,2%|
|R_71|MPS 60|-|-|-|-|-|-|-|-|-|-|-|40,5%|
|R_72|MPS 61|-|-|-|-|-|-|-|-|-|-|-|26,0%|
|R_73|MPS 62|-|-|-|-|-|-|-|-|-|-|-|9,3%|
|R_74|MPS 63|-|-|-|-|-|-|-|-|-|-|-|3,3%|

Fuente: Elaboración propia.

78

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

###### 10.1.2 Concentraciones totales

A continuación, se presentan las concentraciones totales para la fase de operación futura del Proyecto.

Para estimar las concentraciones totales proyectadas para dicha fase, es utilizada la metodología

indicada en la sección 3 del presente documento, y que se describe brevemente a continuación.

Con la modelación del escenario se determinarán los aportes de éstos en la calidad del aire. La calidad

del aire proyectada para la fase de operación futura del Proyecto será estimada de acuerdo con la

siguiente ecuación.

**CA_Co = LB - F_Op_a + F_Op_f**

En donde:

**CA_Co** : corresponde a la calidad del aire proyectada para operación futura del Proyecto.

**LB** : corresponde a la línea base de calidad del aire medida en el área de estudio.

**F_Op_f** : corresponde al aporte en la calidad del aire de la fase de operación futura del Proyecto.

**F_Op_a:** corresponde al aporte de en la calidad del aire de la actividad actual del complejo minero.

En las tablas siguientes (Tabla 10-6 a Tabla 10-10) se evalúa la calidad del aire (o el MPS) en las

estaciones monitoras donde se cuenta con datos medidos. En estación Nuevo Amanecer, la cual está a

menos de 300 metros al Este del Proyecto, se evalúa el MP10, MP2.5 y MPS, mientras que en la estación

Catemu ubicada a menos de 5 kilómetros al sur de Planta Catemu solo se evalúa MP10.

Respecto a las concentraciones totales proyectadas, en estación Nuevo Amanecer la condición respecto

a la situación basal cambia muy levemente, en menos de un 1 % respecto a las normas respectivas, tanto

para el MP10, MP2.5 y MPS. En el caso de la estación Catemu no existe un aumento en el MP10 anual y

el MP10 diario se reduce muy levemente con el Proyecto (0,1 % respecto a la norma).

79

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**Tabla 10-6 Concentraciones totales MP10 anual, aporte del Proyecto en la fase de operación futura.**

|Receptor|LB|% Norma_LB|F_Op_a|% Norma_OP_a|F_Op_f|% Norma_OP_f|Total|Norma|% Norma Total|
|---|---|---|---|---|---|---|---|---|---|
|E. Nuevo Amanecer|45,9|91,8%|0,35|0,7%|0,65|1,3%|46,2|50|92,4%|
|E. Catemu|67,5|135,0%|0,05|0,1%|0,06|0,1%|67,5|50|135,0%|

Fuente: Elaboración propia.

**Tabla 10-7 Concentraciones totales MP10 diario, aporte del Proyecto en la fase de operación futura.**

|Receptor|LB|% Norma_LB|F_Op_a|% Norma_OP_a|F_Op_f|% Norma_OP_f|Total|Norma|% Norma Total|
|---|---|---|---|---|---|---|---|---|---|
|E. Nuevo Amanecer|93,5|62,3%|0,69|0,5%|1,36|0,9%|94,2|150|62,8%|
|E. Catemu|131,7|87,8%|0,29|0,2%|0,20|0,1%|131,6|150|87,7%|

Fuente: Elaboración propia.

**Tabla 10-8 Concentraciones totales MP2,5 anual, aporte del Proyecto en la fase de operación futura.**

|Receptor|LB|% Norma_LB|F_Op_a|% Norma_OP_a|F_Op_f|% Norma_OP_f|Total|Norma|% Norma Total|
|---|---|---|---|---|---|---|---|---|---|
|E. Nuevo Amanecer|10,8|54,0%|0,12|0,6%|0,27|1,3%|11,0|20|54,8%|

Fuente: Elaboración propia.

**Tabla 10-9 Concentraciones totales MP2,5 diario, aporte del Proyecto en la fase de operación futura.**

|Receptor|LB|% Norma_LB|F_Op_a|% Norma_OP_a|F_Op_f|% Norma_OP_f|Total|Norma|% Norma Total|
|---|---|---|---|---|---|---|---|---|---|
|E. Nuevo Amanecer|26,0|52,0%|0,24|0,5%|0,58|1,2%|26,3|50|52,7%|

Fuente: Elaboración propia.

80

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**Tabla 10-10 Depositación total MPS anual, aporte del Proyecto en la fase de operación futura.**

|Receptor|LB|% Norma_LB|F_Op_a|% Norma_OP_a|F_Op_f|% Norma_OP_f|Total|Norma|% Norma Total|
|---|---|---|---|---|---|---|---|---|---|
|E. Nuevo Amanecer|99,2|49,6%|2,47|1,2%|3,75|1,9%|100,5|200|50,2%|

Fuente: Elaboración propia.

81

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

##### 10.2 Mapas de gradientes espaciales de concentración (isoconcentraciones)

A continuación, se presentan las curvas de isoconcentración por contaminante del aporte de la fase de

construcción del Proyecto.

El valor estimado del punto de máxima concentración se indica en rojo en cada uno de los mapas, cabe

estacar que se han omitido los mapas de SO 2 anual, SO 2 diario, SO 2 secundario diario, SO 2 secundario

horario, CO de 1 hora y CO de 8 horas; principalmente porque presentan valores de concentración muy

bajos, encontrándose su punto de máximo impacto por debajo o muy cercano 1% de su respectiva

norma.

En las figuras se puede ver que los puntos de máximo impacto están en las inmediaciones del Proyecto,

en ninguno de los casos el punto de máximo impacto supera las normas respectivas.

82

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**Figura 10-1. Isoconcentraciones fase de operación actual: MP10 Anual**

Fuente: Elaboración propia

83

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**Figura 10-2. Isoconcentraciones fase de operación futura: MP10 Anual**

Fuente: Elaboración propia

84

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**Figura 10-3. Isoconcentraciones fase de operación actual: MP10 Diario**

Fuente: Elaboración propia

85

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**Figura 10-4. Isoconcentraciones fase de operación futura: MP10 Diario**

Fuente: Elaboración propia

86

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**Figura 10-5. Isoconcentraciones fase de operación actual: MP2,5 Anual**

Fuente: Elaboración propia

87

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**Figura 10-6. Isoconcentraciones fase de operación futura: MP2,5 Anual**

Fuente: Elaboración propia

88

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**Figura 10-7. Isoconcentraciones fase de operación actual: MP2,5 Diario**

Fuente: Elaboración propia

89

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**Figura 10-8. Isoconcentraciones fase de operación futura: MP2,5 Diario**

Fuente: Elaboración propia

90

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**Figura 10-9. Isoconcentraciones fase de operación actual: NO** **2** **anual**

Fuente: Elaboración propia

91

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**Figura 10-10. Isoconcentraciones fase de operación futura: NO** **2** **anual**

Fuente: Elaboración propia

92

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**Figura 10-11. Isoconcentraciones fase de operación actual: NO** **2** **horario**

Fuente: Elaboración propia

93

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**Figura 10-12. Isoconcentraciones fase de operación futura: NO** **2** **horario**

Fuente: Elaboración propia

94

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**Figura 10-13. Isoconcentraciones fase de operación actual: MPS Anual**

Fuente: Elaboración propia

95

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

**Figura 10-14. Isoconcentraciones fase de operación futura: MPS Anual**

Fuente: Elaboración propia

96

Anexo 2-1B: Modelación de calidad del aire

DIA “Proyecto Minero 3H”

##### 11 CONCLUSIONES MODELO DE CALIDAD DEL AIRE

A partir del análisis realizado, es posible concluir que:

Se realizó la modelación de un escenario, correspondientes a la fase de operación del Proyecto,

considerando operación actual y operación futura. De los resultados obtenidos para dicha fase, se

concluye que:

Respecto al cumplimiento de normativa en los receptores con registros de mediciones de calidad del

aire:

Respecto a las concentraciones totales proyectadas, en estación Nuevo Amanecer aumentan levemente

las concentraciones respecto a las normas de MP10, MP2.5 y MPS en menos de un 1% en todos los

casos. Para el caso de la estación Catemu el aumento en concentraciones es nulo, incluso el MP10 diario

disminuye levemente (0,1 %). En ambas estaciones se mantienen las condiciones actuales de la calidad

del aire.

Cabe destacar que en todos los casos y para todos los contaminantes evaluados, los aportes netos del

Proyecto son de poca relevancia, superando muy levemente el 1 % de las normas solo en el receptor A1

(Sector el Seco Sur) para MP10 anual, MP2.5 anual y diario y NO2 horario y solo el NO 2 horario en las

estaciones de calidad del aire Nuevo Amanecer.

Respecto al Punto de Máximo Impacto:

Es posible verificar en las figuras que estos están en las inmediaciones del Proyecto, en ninguno de los

casos el punto de máximo impacto supera las normas respectivas.

97

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 5-1.: ** **Normas Primarias de Calidad del Aire Vigentes en Chile****

| Contaminante | Valor umbral de<br>la Norma | Unidad | Período de aplicación de la norma |
| --- | --- | --- | --- |
| Material Particulado<br>Respirable (MP10) | 150 | μg/m3 | Percentil 98 de la media aritmética diaria durante un año |
| Material Particulado<br>Respirable (MP10) | 50 | 50 | Media aritmética trianual |
| Material Particulado<br>Respirable (MP2,5) | 50 | μg/m3 | Percentil 98 de la media aritmética diaria durante un año |
| Material Particulado<br>Respirable (MP2,5) | 20 | 20 | Media aritmética trianual |
| Dióxido de nitrógeno<br>(NO2) | 400 | μg/m3 | Percentil 99 de la media aritmética horaria trianual |
| Dióxido de nitrógeno<br>(NO2) | 100 | 100 | Media aritmética trianual |
| Monóxido de carbono<br>(CO) | 30.000 | μg/m3 | Percentil 99 de la media aritmética horaria trianual |
| Monóxido de carbono<br>(CO) | 10.000 | 10.000 | Percentil 99 de la media aritmética de 8 horas trianual |
| Dióxido de azufre (SO2) | 350 | μg/m3 | Percentil 98.5 de la media aritmética horaria trianual |
| Dióxido de azufre (SO2) | 150 | 150 | Percentil 99 de la media aritmética diaria trianual |
| Dióxido de azufre (SO2) | 60 | 60 | Media aritmética trianual |

**Tabla 6-4.: Coordenadas estaciones meteorológicas****

| Col1 | WGS84-Huso 19 | Col3 |
| --- | --- | --- |
| Estación | UTM - E (m) | UTM - N (m) |
| Nuevo Amanecer | 315.243 | 6.376.191 |
| Catemu Meteorológica | 316.480 | 6.368.520 |

**Tabla 8-1.: ** **Receptores de Interés definidos para la modelación****

| Receptor | Nombre | UTM-X | UTM-Y |
| --- | --- | --- | --- |
| R_1 | E. Nuevo Amanecer | 316.374 | 6.374.730 |
| R_2 | El Cobre | 316.375 | 6.374.728 |
| R_3 | Ñilhue | 316.379 | 6.374.731 |
| R_4 | Cerrillos de Catemu | 316.378 | 6.374.734 |
| R_5 | E. Catemu | 316.375 | 6.374.725 |
| R_6 | Catemu | 316.375 | 6.374.725 |
| R_7 | E. Met. Catemu | 316.375 | 6.374.722 |
| R_8 | Lo Campo | 316.381 | 6.374.723 |
| R_9 | A1 (sector sur El Seco) | 316.374 | 6.374.745 |
| R_10 | A3 (sector norte El Seco) | 316.374 | 6.374.746 |
| R_11 | F4 | 316.373 | 6.374.747 |
| R_12 | MPS 1 | 316.373 | 6.374.726 |
| R_13 | MPS 2 | 316.374 | 6.374.727 |
| R_14 | MPS 3 | 316.375 | 6.374.728 |
| R_15 | MPS 4 | 316.374 | 6.374.728 |
| R_16 | MPS 5 | 316.374 | 6.374.729 |
| R_17 | MPS 6 | 316.374 | 6.374.729 |
| R_18 | MPS 7 | 316.374 | 6.374.730 |
| R_19 | MPS 8 | 316.373 | 6.374.726 |
| R_20 | MPS 9 | 316.373 | 6.374.726 |
| R_21 | MPS 10 | 316.373 | 6.374.726 |
| R_22 | MPS 11 | 316.373 | 6.374.726 |
| R_23 | MPS 12 | 316.373 | 6.374.727 |
| R_24 | MPS 13 | 316.373 | 6.374.727 |
| R_25 | MPS 14 | 316.373 | 6.374.727 |
| R_26 | MPS 15 | 316.374 | 6.374.727 |
| R_27 | MPS 16 | 316.374 | 6.374.727 |
| R_28 | MPS 17 | 316.374 | 6.374.727 |

**Tabla 9-1: Resumen de emisiones incorporadas al modelo situación actual (base).****

| Actividad | Resumen emisiones situación actual (t/año) | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Actividad** | **MP30** | **MP10** | **MP2,5** | **HC** | **NOx** | **CO** | **NH3 ** | **SO2 ** |
| Transferencia de material | 0,23 | 0,11 | 0,02 | - | - | - | - | - |
| Tránsito en camino no<br>pavimentado | 11,38 | 2,01 | 0,49 | - | - | - | - | - |
| Tránsito en camino<br>pavimentado | 3,59 | 0,69 | 0,17 | - | - | - | - | - |
| Combustión vehicular | 0,03 | 0,03 | 0,03 | 0,07 | 1,21 | 0,31 | 0,00 | 0,14 |
| Maquinaria | 0,77 | 0,77 | 0,75 | 1,24 | 8,89 | 8,28 | - | 0,03 |
| Generadores | 1,61 | 0,81 | 0,19 | 0,00 | 22,95 | 4,96 | 0,04 | 1,22 |
| **Total (t/año)** | **17,61** | **4,42** | **1,64** | **1,31** | **33,05** | **13,55** | **0,04** | **1,38** |

**Tabla 9-2: Resumen de emisiones incorporadas al modelo fase de operación.****

| Actividad | Resumen emisiones fase de operación (t/año) | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Actividad** | **MP30** | **MP10** | **MP2,5** | **HC** | **NOx** | **CO** | **NH3 ** | **SO2 ** |
| Transferencia de material | 0,51 | 0,24 | 0,04 | - | - | - | - | - |
| Tránsito en camino no<br>pavimentado | 55,79 | 9,87 | 2,39 | - | - | - | - | - |
| Tránsito en camino<br>pavimentado | 1,84 | 0,35 | 0,09 | - | - | - | - | - |
| Combustión vehicular | 0,06 | 0,06 | 0,06 | 0,14 | 2,21 | 0,62 | 0,00 | 0,25 |
| Maquinaria | 1,38 | 1,38 | 1,34 | 2,23 | 15,78 | 14,85 | - | 0,05 |
| Generadores | 3,89 | 1,95 | 0,47 | 0,00 | 55,41 | 11,97 | 0,10 | 2,94 |
| **Total (t/año)** | **63,47** | **13,86** | **4,38** | **2,36** | **73,40** | **27,44** | **0,10** | **3,24** |

**Tabla 10-1: Resultados del modelo para el aporte del proyecto en situación actual (base) [μg/m** **[3]** **].****

| Receptor | Nombre | MP10 anual | MP10 diario | MP2.5 anual | MP2.5 diario | NO anual<br>2 | NO horario<br>2 | SO anual<br>2 | SO diario<br>2 | SO horario<br>2 | CO 1h | CO 8h | MPS anual |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R_1 | E. Nuevo Amanecer | 0,35 | 0,69 | 0,12 | 0,24 | 0,53 | 9,33 | 0,03 | 0,08 | 0,16 | 5,03 | 1,41 | 2,47 |
| R_2 | El Cobre | 0,17 | 0,33 | 0,05 | 0,11 | 0,28 | 1,79 | 0,03 | 0,06 | 0,11 | 0,79 | 0,30 | - |
| R_3 | Ñilhue | 0,01 | 0,03 | 0,01 | 0,02 | 0,07 | 1,24 | 0,00 | 0,01 | 0,01 | 0,33 | 0,10 | - |
| R_4 | Cerrillos de Catemu | 0,01 | 0,03 | 0,01 | 0,02 | 0,07 | 1,67 | 0,00 | 0,01 | 0,02 | 0,40 | 0,11 | - |
| R_5 | E. Catemu | 0,05 | 0,29 | 0,02 | 0,12 | 0,13 | 1,79 | 0,01 | 0,07 | 0,15 | 0,58 | 0,39 | - |
| R_6 | Catemu | 0,09 | 0,42 | 0,03 | 0,18 | 0,16 | 2,17 | 0,02 | 0,10 | 0,21 | 0,73 | 0,51 | - |
| R_7 | E. Met Catemu | 0,01 | 0,02 | 0,00 | 0,02 | 0,04 | 0,37 | 0,00 | 0,01 | 0,01 | 0,10 | 0,04 | - |
| R_8 | Lo Campo | 0,00 | 0,01 | 0,00 | 0,01 | 0,02 | 0,13 | 0,00 | 0,00 | 0,00 | 0,04 | 0,02 | - |
| R_9 | A1 | 0,21 | 0,49 | 0,08 | 0,18 | 0,46 | 10,47 | 0,03 | 0,07 | 0,15 | 6,27 | 1,28 | - |
| R_10 | A3 | 0,71 | 1,35 | 0,22 | 0,42 | 0,67 | 7,45 | 0,04 | 0,10 | 0,20 | 4,35 | 2,17 | - |
| R_11 | F4 | - | - | - | - | - | - | - | - | - | - | - | 33,20 |
| R_12 | MPS 1 | - | - | - | - | - | - | - | - | - | - | - | 12,22 |
| R_13 | MPS 2 | - | - | - | - | - | - | - | - | - | - | - | 40,55 |
| R_14 | MPS 3 | - | - | - | - | - | - | - | - | - | - | - | 33,10 |
| R_15 | MPS 4 | - | - | - | - | - | - | - | - | - | - | - | 42,01 |
| R_16 | MPS 5 | - | - | - | - | - | - | - | - | - | - | - | 22,84 |
| R_17 | MPS 6 | - | - | - | - | - | - | - | - | - | - | - | 43,95 |
| R_18 | MPS 7 | - | - | - | - | - | - | - | - | - | - | - | 64,12 |
| R_19 | MPS 8 | - | - | - | - | - | - | - | - | - | - | - | 12,34 |
| R_20 | MPS 9 | - | - | - | - | - | - | - | - | - | - | - | 26,58 |
| R_21 | MPS 10 | - | - | - | - | - | - | - | - | - | - | - | 16,82 |
| R_22 | MPS 11 | - | - | - | - | - | - | - | - | - | - | - | 5,63 |
| R_23 | MPS 12 | - | - | - | - | - | - | - | - | - | - | - | 3,93 |
| R_24 | MPS 13 | - | - | - | - | - | - | - | - | - | - | - | 32,22 |
| R_25 | MPS 14 | - | - | - | - | - | - | - | - | - | - | - | 36,99 |
| R_26 | MPS 15 | - | - | - | - | - | - | - | - | - | - | - | 12,51 |
| R_27 | MPS 16 | - | - | - | - | - | - | - | - | - | - | - | 43,85 |
| R_28 | MPS 17 | - | - | - | - | - | - | - | - | - | - | - | 39,75 |
| R_29 | MPS 18 | - | - | - | - | - | - | - | - | - | - | - | 41,05 |
| R_30 | MPS 19 | - | - | - | - | - | - | - | - | - | - | - | 38,22 |
| R_31 | MPS 20 | - | - | - | - | - | - | - | - | - | - | - | 32,80 |

**Tabla 10-2: Resultados del modelo para el aporte del proyecto en fase operación futura [μg/m** **[3]** **].****

| Receptor | Nombre | MP10 anual | MP10 diario | MP2.5 anual | MP2.5 diario | NO anual<br>2 | NO horario<br>2 | SO anual<br>2 | SO diario<br>2 | SO horario<br>2 | CO 1h | CO 8h | MPS anual |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R_1 | E. Nuevo Amanecer | 0,65 | 1,36 | 0,27 | 0,58 | 0,96 | 14,69 | 0,04 | 0,10 | 0,17 | 8,94 | 2,52 | 3,75 |
| R_2 | El Cobre | 0,15 | 0,27 | 0,06 | 0,12 | 0,30 | 3,62 | 0,02 | 0,04 | 0,06 | 1,25 | 0,46 | - |
| R_3 | Ñilhue | 0,03 | 0,07 | 0,02 | 0,06 | 0,13 | 1,80 | 0,00 | 0,01 | 0,02 | 0,64 | 0,22 | - |
| R_4 | Cerrillos de Catemu | 0,03 | 0,06 | 0,02 | 0,05 | 0,14 | 2,54 | 0,01 | 0,01 | 0,03 | 0,66 | 0,21 | - |
| R_5 | E. Catemu | 0,06 | 0,20 | 0,03 | 0,09 | 0,14 | 1,75 | 0,01 | 0,04 | 0,08 | 0,63 | 0,23 | - |
| R_6 | Catemu | 0,08 | 0,28 | 0,04 | 0,12 | 0,17 | 2,30 | 0,01 | 0,05 | 0,10 | 0,72 | 0,30 | - |
| R_7 | E. Met Catemu | 0,02 | 0,04 | 0,01 | 0,03 | 0,07 | 0,70 | 0,00 | 0,01 | 0,01 | 0,19 | 0,09 | - |
| R_8 | Lo Campo | 0,01 | 0,02 | 0,01 | 0,02 | 0,04 | 0,26 | 0,00 | 0,00 | 0,01 | 0,08 | 0,04 | - |
| R_9 | A1 | 0,86 | 1,72 | 0,37 | 0,84 | 0,98 | 16,39 | 0,05 | 0,12 | 0,20 | 11,49 | 2,35 | - |
| R_10 | A3 | 0,92 | 2,08 | 0,34 | 0,74 | 1,11 | 13,52 | 0,04 | 0,10 | 0,17 | 7,80 | 4,02 | - |
| R_11 | F4 | - | - | - | - | - | - | - | - | - | - | - | 33,20 |
| R_12 | MPS 1 | - | - | - | - | - | - | - | - | - | - | - | 12,22 |
| R_13 | MPS 2 | - | - | - | - | - | - | - | - | - | - | - | 40,55 |
| R_14 | MPS 3 | - | - | - | - | - | - | - | - | - | - | - | 33,10 |
| R_15 | MPS 4 | - | - | - | - | - | - | - | - | - | - | - | 42,01 |
| R_16 | MPS 5 | - | - | - | - | - | - | - | - | - | - | - | 22,84 |
| R_17 | MPS 6 | - | - | - | - | - | - | - | - | - | - | - | 43,95 |
| R_18 | MPS 7 | - | - | - | - | - | - | - | - | - | - | - | 64,12 |
| R_19 | MPS 8 | - | - | - | - | - | - | - | - | - | - | - | 12,34 |
| R_20 | MPS 9 | - | - | - | - | - | - | - | - | - | - | - | 26,58 |

**Tabla 10-3: Resultados del modelo para el delta operación futura en relación a la operación actual [μg/m** **[3]** **].****

| Receptor | Nombre | MP10 anual | MP10 diario | MP2.5 anual | MP2.5 diario | NO anual<br>2 | NO horario<br>2 | SO anual<br>2 | SO diario<br>2 | SO horario<br>2 | CO 1h | CO 8h | MPS anual |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R_1 | E. Nuevo Amanecer | 0,31 | 0,67 | 0,15 | 0,34 | 0,43 | 5,36 | 0,01 | 0,02 | 0,01 | 3,91 | 1,11 | 1,28 |
| R_2 | El Cobre | -0,01 | -0,05 | 0,00 | 0,01 | 0,02 | 1,83 | -0,01 | -0,02 | -0,05 | 0,46 | 0,17 | - |
| R_3 | Ñilhue | 0,02 | 0,04 | 0,01 | 0,04 | 0,06 | 0,56 | 0,00 | 0,00 | 0,01 | 0,31 | 0,11 | - |
| R_4 | Cerrillos de Catemu | 0,01 | 0,04 | 0,01 | 0,03 | 0,07 | 0,87 | 0,00 | 0,01 | 0,01 | 0,26 | 0,10 | - |
| R_5 | E. Catemu | 0,00 | -0,09 | 0,00 | -0,03 | 0,02 | -0,04 | 0,00 | -0,03 | -0,08 | 0,05 | -0,15 | - |
| R_6 | Catemu | -0,01 | -0,15 | 0,00 | -0,05 | 0,01 | 0,14 | -0,01 | -0,05 | -0,11 | -0,01 | -0,20 | - |
| R_7 | E. Met Catemu | 0,01 | 0,02 | 0,01 | 0,01 | 0,03 | 0,33 | 0,00 | 0,00 | 0,00 | 0,10 | 0,04 | - |
| R_8 | Lo Campo | 0,01 | 0,01 | 0,00 | 0,01 | 0,02 | 0,13 | 0,00 | 0,00 | 0,00 | 0,04 | 0,02 | - |
| R_9 | A1 | 0,65 | 1,23 | 0,29 | 0,66 | 0,51 | 5,92 | 0,02 | 0,05 | 0,05 | 5,22 | 1,07 | - |
| R_10 | A3 | 0,21 | 0,73 | 0,12 | 0,32 | 0,44 | 6,07 | 0,00 | 0,00 | -0,03 | 3,45 | 1,85 | - |
| R_11 | F4 | - | - | - | - | - | - | - | - | - | - | - | 16,76 |
| R_12 | MPS 1 | - | - | - | - | - | - | - | - | - | - | - | 11,39 |
| R_13 | MPS 2 | - | - | - | - | - | - | - | - | - | - | - | 40,43 |
| R_14 | MPS 3 | - | - | - | - | - | - | - | - | - | - | - | 32,60 |
| R_15 | MPS 4 | - | - | - | - | - | - | - | - | - | - | - | 41,39 |
| R_16 | MPS 5 | - | - | - | - | - | - | - | - | - | - | - | 20,79 |
| R_17 | MPS 6 | - | - | - | - | - | - | - | - | - | - | - | 36,76 |
| R_18 | MPS 7 | - | - | - | - | - | - | - | - | - | - | - | 36,52 |
| R_19 | MPS 8 | - | - | - | - | - | - | - | - | - | - | - | 9,46 |
| R_20 | MPS 9 | - | - | - | - | - | - | - | - | - | - | - | 25,55 |
| R_21 | MPS 10 | - | - | - | - | - | - | - | - | - | - | - | 14,58 |
| R_22 | MPS 11 | - | - | - | - | - | - | - | - | - | - | - | 5,24 |
| R_23 | MPS 12 | - | - | - | - | - | - | - | - | - | - | - | 3,74 |
| R_24 | MPS 13 | - | - | - | - | - | - | - | - | - | - | - | 32,07 |
| R_25 | MPS 14 | - | - | - | - | - | - | - | - | - | - | - | 36,89 |
| R_26 | MPS 15 | - | - | - | - | - | - | - | - | - | - | - | 12,40 |
| R_27 | MPS 16 | - | - | - | - | - | - | - | - | - | - | - | 43,74 |
| R_28 | MPS 17 | - | - | - | - | - | - | - | - | - | - | - | 39,64 |
| R_29 | MPS 18 | - | - | - | - | - | - | - | - | - | - | - | 40,93 |
| R_30 | MPS 19 | - | - | - | - | - | - | - | - | - | - | - | 38,08 |
| R_31 | MPS 20 | - | - | - | - | - | - | - | - | - | - | - | 32,66 |
| R_32 | MPS 21 | - | - | - | - | - | - | - | - | - | - | - | 4,75 |
| R_33 | MPS 22 | - | - | - | - | - | - | - | - | - | - | - | 25,87 |

**Tabla 10-4: Porcentaje del delta operación futura en relación a la operación actual respecto a la norma.****

| Receptor | Nombre | MP10 anual | MP10 diario | MP2.5 anual | MP2.5 diario | NO anual<br>2 | NO horario<br>2 | SO anual<br>2 | SO diario<br>2 | SO horario<br>2 | CO 1h | CO 8h | MPS anual |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R_1 | E. Nuevo Amanecer | 0,6% | 0,4% | 0,8% | 0,7% | 0,4% | 1,3% | 0,0% | 0,0% | 0,0% | 0,0% | 0,0% | 0,6% |
| R_2 | El Cobre | 0,0% | 0,0% | 0,0% | 0,0% | 0,0% | 0,5% | 0,0% | 0,0% | 0,0% | 0,0% | 0,0% | - |
| R_3 | Ñilhue | 0,0% | 0,0% | 0,1% | 0,1% | 0,1% | 0,1% | 0,0% | 0,0% | 0,0% | 0,0% | 0,0% | - |
| R_4 | Cerrillos de Catemu | 0,0% | 0,0% | 0,1% | 0,1% | 0,1% | 0,2% | 0,0% | 0,0% | 0,0% | 0,0% | 0,0% | - |
| R_5 | E. Catemu | 0,0% | -0,1% | 0,0% | -0,1% | 0,0% | 0,0% | 0,0% | 0,0% | 0,0% | 0,0% | 0,0% | - |
| R_6 | Catemu | 0,0% | -0,1% | 0,0% | -0,1% | 0,0% | 0,0% | 0,0% | 0,0% | 0,0% | 0,0% | 0,0% | - |
| R_7 | E. Met Catemu | 0,0% | 0,0% | 0,0% | 0,0% | 0,0% | 0,1% | 0,0% | 0,0% | 0,0% | 0,0% | 0,0% | - |
| R_8 | Lo Campo | 0,0% | 0,0% | 0,0% | 0,0% | 0,0% | 0,0% | 0,0% | 0,0% | 0,0% | 0,0% | 0,0% | - |
| R_9 | A1 | 1,3% | 0,8% | 1,4% | 1,3% | 0,5% | 1,5% | 0,0% | 0,0% | 0,0% | 0,0% | 0,0% | - |
| R_10 | A3 | 0,4% | 0,5% | 0,6% | 0,6% | 0,4% | 1,5% | 0,0% | 0,0% | 0,0% | 0,0% | 0,0% | - |
| R_11 | F4 | - | - | - | - | - | - | - | - | - | - | - | 8,4% |
| R_12 | MPS 1 | - | - | - | - | - | - | - | - | - | - | - | 5,7% |
| R_13 | MPS 2 | - | - | - | - | - | - | - | - | - | - | - | 20,2% |
| R_14 | MPS 3 | - | - | - | - | - | - | - | - | - | - | - | 16,3% |
| R_15 | MPS 4 | - | - | - | - | - | - | - | - | - | - | - | 20,7% |
| R_16 | MPS 5 | - | - | - | - | - | - | - | - | - | - | - | 10,4% |
| R_17 | MPS 6 | - | - | - | - | - | - | - | - | - | - | - | 18,4% |
| R_18 | MPS 7 | - | - | - | - | - | - | - | - | - | - | - | 18,3% |
| R_19 | MPS 8 | - | - | - | - | - | - | - | - | - | - | - | 4,7% |
| R_20 | MPS 9 | - | - | - | - | - | - | - | - | - | - | - | 12,8% |
| R_21 | MPS 10 | - | - | - | - | - | - | - | - | - | - | - | 7,3% |
| R_22 | MPS 11 | - | - | - | - | - | - | - | - | - | - | - | 2,6% |

**Tabla 10-5: Porcentaje del modelo para el aporte del proyecto en fase operación futura respecto a la norma.****

| Receptor | Nombre | MP10<br>anual | MP10<br>diario | MP2.5<br>anual | MP2.5<br>diario | NO2<br>anual | NO2<br>horario | SO2<br>anual | SO2<br>diario | SO2<br>horario | CO<br>1h | CO<br>8h | MPS<br>anual |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R_1 | E. Nuevo Amanecer | 1,3% | 0,9% | 1,3% | 1,2% | 1,0% | 3,7% | 0,1% | 0,1% | 0,0% | 0,0% | 0,0% | 1,9% |
| R_2 | El Cobre | 0,3% | 0,2% | 0,3% | 0,2% | 0,3% | 0,9% | 0,0% | 0,0% | 0,0% | 0,0% | 0,0% | - |
| R_3 | Ñilhue | 0,1% | 0,0% | 0,1% | 0,1% | 0,1% | 0,4% | 0,0% | 0,0% | 0,0% | 0,0% | 0,0% | - |
| R_4 | Cerrillos de Catemu | 0,1% | 0,0% | 0,1% | 0,1% | 0,1% | 0,6% | 0,0% | 0,0% | 0,0% | 0,0% | 0,0% | - |
| R_5 | E. Catemu | 0,1% | 0,1% | 0,1% | 0,2% | 0,1% | 0,4% | 0,0% | 0,0% | 0,0% | 0,0% | 0,0% | - |
| R_6 | Catemu | 0,2% | 0,2% | 0,2% | 0,2% | 0,2% | 0,6% | 0,0% | 0,0% | 0,0% | 0,0% | 0,0% | - |
| R_7 | E. Met Catemu | 0,0% | 0,0% | 0,1% | 0,1% | 0,1% | 0,2% | 0,0% | 0,0% | 0,0% | 0,0% | 0,0% | - |
| R_8 | Lo Campo | 0,0% | 0,0% | 0,0% | 0,0% | 0,0% | 0,1% | 0,0% | 0,0% | 0,0% | 0,0% | 0,0% | - |
| R_9 | A1 | 1,7% | 1,1% | 1,8% | 1,7% | 1,0% | 4,1% | 0,1% | 0,1% | 0,1% | 0,0% | 0,0% | - |
| R_10 | A3 | 1,8% | 1,4% | 1,7% | 1,5% | 1,1% | 3,4% | 0,1% | 0,1% | 0,0% | 0,0% | 0,0% | - |
| R_11 | F4 | - | - | - | - | - | - | - | - | - | - | - | 16,6% |
| R_12 | MPS 1 | - | - | - | - | - | - | - | - | - | - | - | 6,1% |
| R_13 | MPS 2 | - | - | - | - | - | - | - | - | - | - | - | 20,3% |
| R_14 | MPS 3 | - | - | - | - | - | - | - | - | - | - | - | 16,5% |
| R_15 | MPS 4 | - | - | - | - | - | - | - | - | - | - | - | 21,0% |
| R_16 | MPS 5 | - | - | - | - | - | - | - | - | - | - | - | 11,4% |
| R_17 | MPS 6 | - | - | - | - | - | - | - | - | - | - | - | 22,0% |
| R_18 | MPS 7 | - | - | - | - | - | - | - | - | - | - | - | 32,1% |
| R_19 | MPS 8 | - | - | - | - | - | - | - | - | - | - | - | 6,2% |
| R_20 | MPS 9 | - | - | - | - | - | - | - | - | - | - | - | 13,3% |
| R_21 | MPS 10 | - | - | - | - | - | - | - | - | - | - | - | 8,4% |
| R_22 | MPS 11 | - | - | - | - | - | - | - | - | - | - | - | 2,8% |
| R_23 | MPS 12 | - | - | - | - | - | - | - | - | - | - | - | 2,0% |
| R_24 | MPS 13 | - | - | - | - | - | - | - | - | - | - | - | 16,1% |
| R_25 | MPS 14 | - | - | - | - | - | - | - | - | - | - | - | 18,5% |
| R_26 | MPS 15 | - | - | - | - | - | - | - | - | - | - | - | 6,3% |
| R_27 | MPS 16 | - | - | - | - | - | - | - | - | - | - | - | 21,9% |
| R_28 | MPS 17 | - | - | - | - | - | - | - | - | - | - | - | 19,9% |
| R_29 | MPS 18 | - | - | - | - | - | - | - | - | - | - | - | 20,5% |
| R_30 | MPS 19 | - | - | - | - | - | - | - | - | - | - | - | 19,1% |
| R_31 | MPS 20 | - | - | - | - | - | - | - | - | - | - | - | 16,4% |
| R_32 | MPS 21 | - | - | - | - | - | - | - | - | - | - | - | 2,5% |

**Tabla 10-6: Concentraciones totales MP10 anual, aporte del Proyecto en la fase de operación futura.****

| Receptor | LB | % Norma_LB | F_Op_a | % Norma_OP_a | F_Op_f | % Norma_OP_f | Total | Norma | % Norma Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E. Nuevo Amanecer | 45,9 | 91,8% | 0,35 | 0,7% | 0,65 | 1,3% | 46,2 | 50 | 92,4% |
| E. Catemu | 67,5 | 135,0% | 0,05 | 0,1% | 0,06 | 0,1% | 67,5 | 50 | 135,0% |

**Tabla 10-7: Concentraciones totales MP10 diario, aporte del Proyecto en la fase de operación futura.****

| Receptor | LB | % Norma_LB | F_Op_a | % Norma_OP_a | F_Op_f | % Norma_OP_f | Total | Norma | % Norma Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E. Nuevo Amanecer | 93,5 | 62,3% | 0,69 | 0,5% | 1,36 | 0,9% | 94,2 | 150 | 62,8% |
| E. Catemu | 131,7 | 87,8% | 0,29 | 0,2% | 0,20 | 0,1% | 131,6 | 150 | 87,7% |

**Tabla 10-8: Concentraciones totales MP2,5 anual, aporte del Proyecto en la fase de operación futura.****

| Receptor | LB | % Norma_LB | F_Op_a | % Norma_OP_a | F_Op_f | % Norma_OP_f | Total | Norma | % Norma Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E. Nuevo Amanecer | 10,8 | 54,0% | 0,12 | 0,6% | 0,27 | 1,3% | 11,0 | 20 | 54,8% |

**Tabla 10-9: Concentraciones totales MP2,5 diario, aporte del Proyecto en la fase de operación futura.****

| Receptor | LB | % Norma_LB | F_Op_a | % Norma_OP_a | F_Op_f | % Norma_OP_f | Total | Norma | % Norma Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E. Nuevo Amanecer | 26,0 | 52,0% | 0,24 | 0,5% | 0,58 | 1,2% | 26,3 | 50 | 52,7% |

**Tabla 10-10: Depositación total MPS anual, aporte del Proyecto en la fase de operación futura.****

| Receptor | LB | % Norma_LB | F_Op_a | % Norma_OP_a | F_Op_f | % Norma_OP_f | Total | Norma | % Norma Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E. Nuevo Amanecer | 99,2 | 49,6% | 2,47 | 1,2% | 3,75 | 1,9% | 100,5 | 200 | 50,2% |
