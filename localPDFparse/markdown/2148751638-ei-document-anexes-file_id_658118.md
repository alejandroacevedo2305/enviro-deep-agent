---
title: Tipo de Informe o Capítulo
author: Wen Rou Lee
date: D:20201014103238-03'00'
language: es
type: report
pages: 61
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Anexo 4.b Modelación de dispersión de contaminantes atmosféricos
-->

# Anexo 4.b Modelación de dispersión de contaminantes atmosféricos

## Declaración de Impacto Ambiental “Incorporación Caldera N°5 en Planta de Generación de Vapor EISA”

### Región del Maule

Agosto, 2020

Elaborado por:

**Gestión Ambiental Consultores S.A.**

General del Canto 421, Piso 6, Providencia.

Santiago, Chile - Fono: +56 2 2719 5600

www.gac.cl

|Proyecto GAC N°|Col2|2001007|Col4|Col5|
|---|---|---|---|---|
|Rev.|Elaboró|Revisó|Aprobó|Fecha de Aprobación|
|A|Julio Castro M.|Wen Rou Lee|||
|B|Julio Castro M.|M. Gabriela<br>Cienfuegos|||
||||||

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

**INDICE GENERAL**

**1** **Introducción ............................................................................................................................... 5**

**2** **Objetivos .................................................................................................................................... 5**

**3** **Metodología general ................................................................................................................... 6**

**4** **Caracterización calidad del aire ................................................................................................... 8**

4.1 Normativa Calidad del Aire Vigente .............................................................................................. 8

4.2 Monitoreo calidad del aire ............................................................................................................ 9

**5** **Modelo meteorológico .............................................................................................................. 11**

5.1 Justificación del Modelo Meteorológico ..................................................................................... 11

5.2 Descripción del Modelo Meteorológico ...................................................................................... 11

5.3 Dominio Modelación ................................................................................................................... 15

5.4 Topografía y Uso de Suelos ......................................................................................................... 18

5.5 Caracterización meteorológica de la zona y evaluación del modelo meteorológico.................. 20

5.5.1 Velocidad del Viento ........................................................................................................... 22

5.5.2 Dirección del Viento ............................................................................................................ 28

5.5.3 Temperatura ........................................................................................................................ 37

5.5.4 Altura capa de mezcla en zona modelada ........................................................................... 40

5.5.5 Análisis necesidad de uso de factor de ajuste del modelo meteorológico en base a la

velocidad del viento observada y modelada ....................................................................................... 41

5.5.6 Conclusiones modelo meteorológico .................................................................................. 42

**6** **Modelo calidad del aire ............................................................................................................. 43**

6.1 Justificación modelo calidad del aire .......................................................................................... 43

6.2 Descripción modelo de calidad del aire ...................................................................................... 43

**7** **Emisiones ingresadas al modelo ................................................................................................ 45**

**8** **Receptores ............................................................................................................................... 45**

8.1 Receptores discretos ................................................................................................................... 45

8.2 Receptores grilla .......................................................................................................................... 46

**9** **Resultados ................................................................................................................................ 47**

9.1 Análisis de resultados de modelación ......................................................................................... 47

9.1.1 Aporte modelado ................................................................................................................ 47

9.1.2 Concentraciones totales ...................................................................................................... 49

9.2 Mapas de gradientes espaciales de concentración (isoconcentraciones) .................................. 52

**10** **Conclusiones modelo de calidad del aire .................................................................................... 59**

i

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

**INDICE DE TABLAS**

Tabla 4-1: Normas Primarias de Calidad del Aire Vigentes en Chile ............................................................. 8

<!-- INICIO TABLA 4-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- (MP 10 ), para su fracción más fina (MP 2,5 ), y los gases dióxido de nitrógeno (NO 2 ), monóxido de carbono (CO) y dióxido de azufre (SO 2 ). Los valores umbrales de las normas citadas se presentan en la Tabla 4-1. -->

**Tabla 4-1: ** **Normas Primarias de Calidad del Aire Vigentes en Chile****

| Contaminante | Tipo de Norma | Estadístico | Límite Norma<br>(μg/m3N) | Referencia |
| --- | --- | --- | --- | --- |
| MP10 | Primaria anual | Media aritmética trianual | 50 | D.S.<br>N°59/1998 |
| MP10 | Primaria diaria | Percentil 98 de la de las concentraciones de 24<br>horas durante un año | 150 | 150 |
| MP2,5 | Primaria anual | Media aritmética trianual | 20 | D.S.<br>N°12/2011 |
| MP2,5 | Primaria diaria | Percentil 98 de la de las concentraciones de 24<br>horas durante un año | 50 | 50 |
| SO2 | Primaria anual | Media aritmética trianual | 60 | D.S.<br>No104/2018 |
| SO2 | Primaria diaria | Media aritmética trianual del Percentil 99 de<br>las concentraciones de 24 horas de cada año | 150 | 150 |
| SO2 | Primaria horaria | Media aritmética trianual del Percentil 98,5 de<br>las concentraciones de 1 hora de cada año | 350 | 350 |
| NO2 | Primaria horaria | Media aritmética trianual del Percentil 99 de<br>los máximos diarios de concentración de 1<br>hora de cada año | 400 | D.S.<br>N°114/2002 |
| NO2 | Primaria anual | Media aritmética trianual | 100 | 100 |
| O3 | Primaria 8 horas | Media aritmética trianual del Percentil 99 de<br>los máximos diarios de concentración de 8<br>horas de cada año | 120 | D.S. N°112/02 |
| CO | Primaria horaria | Media aritmética trianual del Percentil 99 de<br>los máximos diarios de concentración de 1<br>hora de cada año | 30000 | D.S. N°115/02 |
| CO | Primario 8 horas | Media aritmética trianual del Percentil 99 de<br>los máximos diarios de concentración de 8<br>hora de cada año | 10000 | 10000 |

<!-- Estadísticas: 12 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- 8 Fuente: Elaboración Propia -->
<!-- FIN TABLA 4-1 -->


Tabla 4-2: Coordenadas de ubicación de las estaciones de calidad del aire................................................. 9

<!-- INICIO TABLA 4-2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- posteriormente evaluar el aporte de las emisiones del Proyecto a las concentraciones ambientales de la zona. -->

**Tabla 4-2: Coordenadas de ubicación de las estaciones de calidad del aire.****

| Col1 | WGS84-Huso 19 | Col3 | Variable monitoreada |
| --- | --- | --- | --- |
| **Estación** | **UTM - E (m)** | **UTM - N (m)** | **UTM - N (m)** |
| Yerbas Buenas | 265.391 | 6.057.869 | MP10, MP2.5, NO2, CO, SO2, O3 |
| U. Maule | 262.216 | 6.075.477 | MP10, MP2.5 |
| La Florida | 256.889 | 6.075.395 | MP10, MP2.5, NO2, CO |

<!-- Estadísticas: 4 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. **Figura 4-1: Ubicación de las estaciones de calidad del aire.** -->
<!-- FIN TABLA 4-2 -->


Tabla 4-3: Concentraciones basales estaciones calidad del aire año 2019. ................................................ 10

<!-- INICIO TABLA 4-3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- latencia para MP10 y saturación de MP2.5, mientras que La Florida presenta solo saturación por MP2.5, pero esta última estación es la que presenta mayores concentraciones de MP2.5 de las dos estaciones. -->

**Tabla 4-3: Concentraciones basales estaciones calidad del aire año 2019.****

| Col1 | μg/m3 | Yerbas Buenas | Col4 | U. Maule | Col6 | La Florida | Col8 | Norma |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Contaminante** | **Tipo de Norma** | **LDB** | **% LDB_N** | **LDB** | **% LDB_N** | **LDB** | **% LDB_N** | **% LDB_N** |
| MP10 | Primaria anual | 25,7 | 51,4% | 41,7 | 83,3% | 39,7 | 79,5% | 50 |
| MP10 | Primaria diaria | 66,7 | 44,5% | 86,9 | 57,9% | 113,3 | 75,5% | 150 |
| MP2,5 | Primaria anual | 14,8 | 73,8% | 19,7 | 98,6% | 23,9 | 119,3% | 20 |
| MP2,5 | Primaria diaria | 45,8 | 91,6% | 62,9 | 125,8% | 94,7 | 189,3% | 50 |
| SO2 | Primaria anual | 2,4 | 4,0% | - | - | - | - | 60 |
| SO2 | Primaria diaria | 9,4 | 6,2% | - | - | - | - | 150 |
| SO2 | Primaria horaria | 14,7 | 4,2% | - | - | - | - | 350 |
| NO2 | Primaria anual | 8,4 | 8,4% | - | - | 16,2 | 16,2% | 100 |
| NO2 | Primaria horaria | 82,8 | 20,7% | - | - | 66,0 | 16,5% | 400 |
| CO | Primaria horaria | 1400,0 | 4,7% | - | - | 10971 | 36,6% | 30.000 |
| CO | Primario 8<br>horas | 606,8 | 6,1% | - | - | 6739 | 67,4% | 10.000 |
| O3 | Primaria 8 horas | 86,7 | 72,2% | - | - | - | - | 120 |

<!-- Estadísticas: 13 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. 10 -->
<!-- FIN TABLA 4-3 -->


Tabla 5-1: Definición de dominio de modelación. ...................................................................................... 12

<!-- INICIO TABLA 5-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **Figura 5-1: Extensiones de los dominios 1, 2, 3 y 4 en WRF.** Fuente: Elaboración propia, en base a Google Earth. -->

**Tabla 5-1: Definición de dominio de modelación.****

| Col1 | DX | DY | NX | NY | KMx | KMy | No Celdas |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Dominio 1 | 27 | 27 | 70 | 70 | 1.890 | 1.890 | 4.900 |
| Dominio 2 | 9 | 9 | 67 | 67 | 603 | 603 | 4.489 |
| Dominio 3 | 3 | 3 | 64 | 64 | 192 | 192 | 4.096 |
| Dominio 4 | 1 | 1 | 61 | 61 | 61 | 61 | 3.721 |

<!-- Estadísticas: 4 filas, 8 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. Donde, -->
<!-- FIN TABLA 5-1 -->


Tabla 5-2: Definición proyección dominios de modelación. ....................................................................... 13

<!-- INICIO TABLA 5-2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Anexo 4.b Modelación de dispersión de contaminantes fase de operación DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA -->

**Tabla 5-2: Definición proyección dominios de modelación.****

| Origen centro Dominio 1<br>y proyección LCC | Col2 |
| --- | --- |
| ref_lat | -35,61 |
| ref_lon | -71,58 |
| truelat1 | -30,61 |
| truelat2 | -40,61 |
| stand_lon | -71,58 |

<!-- Estadísticas: 5 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. Debido a la geomorfología del valle central de la Región del Maule y también la presencia de algunas -->
<!-- FIN TABLA 5-2 -->


Tabla 5-3: Características del Dominio de Modelación. .............................................................................. 16

<!-- INICIO TABLA 5-3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- atmosféricas de éste, lo que se corrobora más adelante en las gradientes de concentraciones estimadas por el modelo. -->

**Tabla 5-3: Características del Dominio de Modelación.****

| Característica | Eje X (km) | Eje Y (km) |
| --- | --- | --- |
| Espaciamiento | 1 | 1 |
| Longitud | 55 | 55 |

<!-- Estadísticas: 2 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. En la Figura 5-3, se presenta el dominio de modelación utilizado en CALPUFF, donde se destacan en azul -->
<!-- FIN TABLA 5-3 -->


Tabla 5-4. Coordenadas estaciones meteorológicas ................................................................................... 19

Tabla 5-5: Estadígrafos velocidad del viento, estaciones Yerbas Buenas y U. Maule. ................................ 27

<!-- INICIO TABLA 5-5 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- en U. Maule. Por otra parte, el modelo estima mayores frecuencias de condiciones de calma (vientos menores a 0,5 m/s) que los registros de las estaciones monitoras. -->

**Tabla 5-5: Estadígrafos velocidad del viento, estaciones Yerbas Buenas y U. Maule.****

| Col1 | Yerbas Buenas | Col3 | U. Maule | Col5 |
| --- | --- | --- | --- | --- |
| **Variable** | **Observado** | **Modelado** | **Observado** | **Modelado** |
| Promedio (m/s) | 1,50 | 3,75 | 1,416 | 1,51 |
| Mediana (m/s) | 1,40 | 3,60 | 1,25 | 1,50 |
| Porcentaje de calmas | 5,2% | 3,9% | 17,7% | 14,2% |

<!-- Estadísticas: 4 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. 27 -->
<!-- FIN TABLA 5-5 -->


Tabla 5-6: Estadígrafos de desempeño velocidad del viento. Año 2018. ................................................... 28

<!-- INICIO TABLA 5-6 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- modelo presenta una alta concordancia con el monitoreo de velocidad del viento U. Maule con un valor de 0,63 y una concordancia media-baja en estación Yerbas Buenas. -->

**Tabla 5-6: Estadígrafos de desempeño velocidad del viento. Año 2018.****

| Estación | N | Sesgo | FAC2 | SM | MAE | SMN | NMAE | ECM | r | IOA |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Yerbas Buenas | 7279 | 2,25 | 0,28 | 2,46 | 2,57 | 164,2% | 171,8% | 3,07 | 0,48 | -0,56 |
| U. Maule | 8710 | 0,10 | 0,77 | 0,09 | 0,54 | 6,7% | 38,0% | 0,69 | 0,68 | 0,63 |

<!-- Estadísticas: 2 filas, 11 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. ###### 5.5.2 Dirección del Viento -->
<!-- FIN TABLA 5-6 -->


Tabla 5-7: Estadígrafos de temperatura, estación U. Maule. ..................................................................... 39

<!-- INICIO TABLA 5-7 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- mediana respectivamente. Por otra parte, la Tabla 5-8 muestra un coeficiente de correlación (r) e índice de concordancia muy altos, con valores de 0,93 y 0,81 respectivamente. -->

**Tabla 5-7: Estadígrafos de temperatura, estación U. Maule.****

| Col1 | U. Maule | Col3 |
| --- | --- | --- |
| **Variable** | **Observado** | **Modelado** |
| Promedio (°C) | 15,03 | 15,69 |
| Mediana (°C) | 13,90 | 14,20 |
| Máximo (°C) | 36,70 | 39,30 |
| Mínimo (°C) | -1,50 | 1,10 |

<!-- Estadísticas: 5 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia 39 -->
<!-- FIN TABLA 5-7 -->


Tabla 5-8: Estadígrafos desempeño por temperatura, estación U. Maule, datos observados y modelados.

<!-- INICIO TABLA 5-8 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Anexo 4.b Modelación de dispersión de contaminantes fase de operación DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA -->

**Tabla 5-8: Estadígrafos desempeño por temperatura, estación U. Maule, datos observados y modelados.****

| Estación | n | Sesgo | FAC2 | SM | MAE | SMN | NMAE | ECM | r | IOA |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| U. Maule | 8710 | 0,66 | 0,96 | 0,64 | 2,18 | 4,3% | 14,5% | 2,86 | 0,93 | 0,81 |

<!-- Estadísticas: 1 filas, 11 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia ###### 5.5.4 Altura capa de mezcla en zona modelada -->
<!-- FIN TABLA 5-8 -->


..................................................................................................................................................................... 40

Tabla 5-9: Estadísticos velocidad del viento. ............................................................................................... 42

<!-- INICIO TABLA 5-9 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Anexo 4.b Modelación de dispersión de contaminantes fase de operación DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA -->

**Tabla 5-9: Estadísticos velocidad del viento.****

| Col1 | Yerbas Buenas | Col3 | U. Maule | Col5 |
| --- | --- | --- | --- | --- |
| **Variable** | **Observado** | **Modelado** | **Observado** | **Modelado** |
| Promedio (m/s) | 1,50 | 3,75 | 1,416 | 1,51 |
| Mediana (m/s) | 1,40 | 3,60 | 1,25 | 1,50 |
| Máximo (m/s) | 6,70 | 15,60 | 4,7 | 5,80 |
| Porcentaje de calmas | 5,2% | 3,9% | 17,7% | 14,2% |

<!-- Estadísticas: 5 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia **Tabla 5-10: Factor de corrección.** -->
<!-- FIN TABLA 5-9 -->


Tabla 5-10: Factor de corrección. ................................................................................................................ 42

<!-- INICIO TABLA 5-10 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Máximo (m/s)|6,70|15,60|4,7|5,80| |Porcentaje de calmas|5,2%|3,9%|17,7%|14,2%| Fuente: Elaboración propia -->

**Tabla 5-10: Factor de corrección.****

| Col1 | Yerbas Buenas | U. Maule | Promedio |
| --- | --- | --- | --- |
| Razón VV mod/obs promedio | 2,50 | 1,07 | 1,79 |
| Razón VV mod/obs mediana | 2,57 | 1,20 | 1,89 |

<!-- Estadísticas: 2 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. ###### 5.5.6 Conclusiones modelo meteorológico -->
<!-- FIN TABLA 5-10 -->


Tabla 7-1: Emisiones Caldera 5.................................................................................................................... 45

<!-- INICIO TABLA 7-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- caldera 5. La Tabla 7-2 muestra las características de la chimenea, cuyos datos fueron provistos por el mandante. -->

**Tabla 7-1: Emisiones Caldera 5****

| Combustible | Caudal | Concentración Máxima | Col4 | Col5 | Emisión Máxima | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Combustible** | **Caudal** | **MP** | **NOx** | **CO** | **MP** | **NOx** | **CO** |
| **Combustible** | **[Nm3/h]** | **[mg/Nm3]** | **[mg/Nm3]** | **[mg/Nm3]** | **[kg/h]** | **[kg/h]** | **[kg/h]** |
| Biomasa 100% | 76668 | 20 | 190,9 | 610 | 1,53 | 14,64 | 46,78 |

<!-- Estadísticas: 3 filas, 8 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: EISA **Tabla 7-2: Características de la fuente** -->
<!-- FIN TABLA 7-1 -->


Tabla 7-2: Características de la fuente ........................................................................................................ 45

<!-- INICIO TABLA 7-2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |**Combustible**|**[Nm3/h]**|**[mg/Nm3]**|**[mg/Nm3]**|**[mg/Nm3]**|**[kg/h]**|**[kg/h]**|**[kg/h]**| |Biomasa 100%|76668|20|190,9|610|1,53|14,64|46,78| Fuente: EISA -->

**Tabla 7-2: Características de la fuente****

| Parámetro | Valor | Unidad |
| --- | --- | --- |
| Altura chimenea | 20 | m |
| Diámetro interno chimenea | 1,57 | m |
| Velocidad salida gases | 20 | m/s |
| Temperatura salida gases | 140 | °C |

<!-- Estadísticas: 4 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: EISA La Tabla 7-3 muestra los factores de emisión ingresados al modelo. Para la especiación de NOx se utilizó -->
<!-- FIN TABLA 7-2 -->


Tabla 7-3: Factor de emisión ingresado al modelo ..................................................................................... 45

<!-- INICIO TABLA 7-3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- de manera conservadora una razón de NO/NO 2 de 80/20. En el caso del material particulado (MP), al ser este de combustión es considerado en un 100 % como MP2.5. -->

**Tabla 7-3: Factor de emisión ingresado al modelo****

| Factor de emisión | MP | NO | NO<br>2 | CO |
| --- | --- | --- | --- | --- |
| kg/h | 1,530 | 11,712 | 2,928 | 46,780 |
| g/s | 0,425 | 3,253 | 0,813 | 12,994 |

<!-- Estadísticas: 2 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración Propia ##### 8 RECEPTORES 8.1 Receptores discretos -->
<!-- FIN TABLA 7-3 -->


Tabla 8-1: Receptores de Interés definidos para la modelación ................................................................. 46

<!-- INICIO TABLA 8-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Anexo 4.b Modelación de dispersión de contaminantes fase de operación DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA -->

**Tabla 8-1: ** **Receptores de Interés definidos para la modelación****

| Receptor | Col2 | Descripción | UTM - WGS84 -H19 | Col5 |
| --- | --- | --- | --- | --- |
| **Receptor** | **Receptor** | **Descripción** | **X (m)** | **Y (m)** |
| 1 | R1 | Yerbas Buenas | 265.391 | 6.057.869 |
| 2 | R2 | U. Maule | 262.216 | 6.075.477 |
| 3 | R3 | La Florida | 256.889 | 6.075.395 |

<!-- Estadísticas: 4 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia . ##### 8.2 Receptores grilla -->
<!-- FIN TABLA 8-1 -->


Tabla 9-1: Resultados del modelo para el aporte del proyecto en la fase de operación sin factor de

<!-- INICIO TABLA 9-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Anexo 4.b Modelación de dispersión de contaminantes fase de operación DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA -->

**Tabla 9-1: Resultados del modelo para el aporte del proyecto en la fase de operación sin factor de corrección.****

| Contaminante | Tipo de Norma | μg/m3 | Col4 | Col5 | Col6 |
| --- | --- | --- | --- | --- | --- |
| **Contaminante** | **Tipo de Norma** | **Yerbas Buenas** | **U. Maule** | **La Florida** | **PMI** |
| MP10 | Primaria anual | 0,010 | 0,003 | 0,001 | 0,210 |
| MP10 | Primaria diaria | 0,110 | 0,031 | 0,013 | 0,770 |
| MP2,5 | Primaria anual | 0,010 | 0,003 | 0,001 | 0,210 |
| MP2,5 | Primaria diaria | 0,110 | 0,031 | 0,013 | 0,770 |
| NO2 | Primaria anual | 0,084 | 0,027 | 0,008 | 2,120 |
| NO2 | Primaria horaria | 15,831 | 4,077 | 1,060 | 35,100 |
| CO | Primaria horaria | 65,770 | 9,617 | 2,565 | 153,000 |
| CO | Primario 8 horas | 16,493 | 3,271 | 0,858 | 69,400 |

<!-- Estadísticas: 9 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. **Tabla 9-2: Resultados del modelo para el aporte del proyecto en la fase de operación con factor de corrección.** -->
<!-- FIN TABLA 9-1 -->


corrección. ................................................................................................................................................... 48

Tabla 9-2: Resultados del modelo para el aporte del proyecto en la fase de operación con factor de

<!-- INICIO TABLA 9-2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |CO|Primaria horaria|65,770|9,617|2,565|153,000| |CO|Primario 8 horas|16,493|3,271|0,858|69,400| Fuente: Elaboración propia. -->

**Tabla 9-2: Resultados del modelo para el aporte del proyecto en la fase de operación con factor de corrección.****

| Contaminante | Tipo de Norma | μg/m3 | Col4 | Col5 | Col6 |
| --- | --- | --- | --- | --- | --- |
| **Contaminante** | **Tipo de Norma** | **Yerbas Buenas** | **U. Maule** | **La Florida** | **PMI** |
| MP10 | Primaria anual | 0,019 | 0,006 | 0,002 | 0,397 |
| MP10 | Primaria diaria | 0,207 | 0,059 | 0,025 | 1,455 |
| MP2,5 | Primaria anual | 0,019 | 0,006 | 0,002 | 0,397 |
| MP2,5 | Primaria diaria | 0,207 | 0,059 | 0,025 | 1,455 |
| NO2 | Primaria anual | 0,159 | 0,051 | 0,014 | 4,007 |
| NO2 | Primaria horaria | 29,921 | 7,705 | 2,003 | 66,339 |
| CO | Primaria horaria | 124,305 | 18,175 | 4,847 | 289,170 |
| CO | Primario 8 horas | 31,172 | 6,183 | 1,621 | 131,166 |

<!-- Estadísticas: 9 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. **Tabla 9-3: Resultados del modelo para el aporte del proyecto en la fase de operación con factor de corrección.** -->
<!-- FIN TABLA 9-2 -->


corrección. ................................................................................................................................................... 48

Tabla 9-3: Resultados del modelo para el aporte del proyecto en la fase de operación con factor de

<!-- INICIO TABLA 9-3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |CO|Primaria horaria|124,305|18,175|4,847|289,170| |CO|Primario 8 horas|31,172|6,183|1,621|131,166| Fuente: Elaboración propia. -->

**Tabla 9-3: Resultados del modelo para el aporte del proyecto en la fase de operación con factor de corrección.****

| Contaminante | Tipo de Norma | Yerbas Buenas | U. Maule | La Florida | PMI |
| --- | --- | --- | --- | --- | --- |
| MP10 | Primaria anual | 0,04% | 0,01% | 0,00% | 0,79% |
| MP10 | Primaria diaria | 0,14% | 0,04% | 0,02% | 0,97% |
| MP2,5 | Primaria anual | 0,09% | 0,03% | 0,01% | 1,98% |
| MP2,5 | Primaria diaria | 0,41% | 0,12% | 0,05% | 2,91% |
| NO2 | Primaria anual | 0,16% | 0,05% | 0,01% | 4,01% |
| NO2 | Primaria horaria | 7,48% | 1,93% | 0,50% | 16,58% |
| CO | Primaria horaria | 0,41% | 0,06% | 0,02% | 0,96% |
| CO | Primario 8 horas | 0,31% | 0,06% | 0,02% | 1,31% |

<!-- Estadísticas: 8 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. 48 -->
<!-- FIN TABLA 9-3 -->


corrección. ................................................................................................................................................... 48

Tabla 9-4: Concentraciones totales Proyecto en estación Yerbas Buenas.................................................. 50

<!-- INICIO TABLA 9-4 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Anexo 4.b Modelación de dispersión de contaminantes fase de operación DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA -->

**Tabla 9-4: Concentraciones totales Proyecto en estación Yerbas Buenas****

| Contaminante | Tipo de Norma | LDB<br>[μg/m3] | % LDB_N | AP_O*<br>[μg/m3] | Aporte Proy.<br>[μg/m3] | %AP_N | Total<br>[μg/m3] | %Total_N | Norma<br>[μg/m3] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MP10 | Primaria anual | 25,69 | 51,4% | 1,43 | 0,02 | 0,0% | 27,14 | 54,3% | 50 |
| MP10 | Primaria diaria | 66,74 | 44,5% | 4,54 | 0,21 | 0,1% | 71,49 | 47,7% | 150 |
| MP2,5 | Primaria anual | 14,76 | 73,8% | 1,20 | 0,02 | 0,1% | 15,98 | 79,9% | 20 |
| MP2,5 | Primaria diaria | 45,78 | 91,6% | 3,83 | 0,21 | 0,4% | 49,82 | 99,6% | 50 |
| NO2 | Primaria anual | 8,43 | 8,4% | 2,09 | 0,16 | 0,2% | 10,68 | 10,7% | 100 |
| NO2 | Primaria horaria | 82,80 | 20,7% | 32,86 | 29,92 | 7,5% | 145,58 | 36,4% | 400 |
| CO | Primaria horaria | 1400,00 | 4,7% | 24,65 | 124,31 | 0,4% | 1548,96 | 5,2% | 30.000 |
| CO | Primario 8 horas | 606,77 | 6,1% | 12,37 | 31,17 | 0,3% | 650,31 | 6,5% | 10.000 |

<!-- Estadísticas: 8 filas, 10 columnas -->
<!-- Contexto posterior: -->
<!-- *se considera aporte estimado en DIA “Planta Cogeneración Cartulinas CMPC” para la fase de operación proyectada en el receptor Estación Bobadilla, el cual se encuentra a 1 kilometro al Este de Estación Yerbas Buenas. -->
<!-- FIN TABLA 9-4 -->


Tabla 9-5: Concentraciones totales Proyecto, en estación U. Maule. ........................................................ 50

<!-- INICIO TABLA 9-5 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Estación Yerbas Buenas. Fuente: Elaboración propia. -->

**Tabla 9-5: Concentraciones totales Proyecto, en estación U. Maule.****

| Contaminante | Tipo de Norma | LDB<br>[μg/m3] | % LDB_N | AP_Op<br>[μg/m3] | % AP_Op_N | CA_Op<br>[μg/m3] | % CA_Op _N | Norma<br>[μg/m3] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MP10 | Primaria anual | 41,67 | 83,3% | 0,01 | 0,0% | 41,68 | 83,4% | 50 |
| MP10 | Primaria diaria | 86,88 | 57,9% | 0,06 | 0,0% | 86,93 | 58,0% | 150 |
| MP2,5 | Primaria anual | 19,72 | 98,6% | 0,01 | 0,0% | 19,72 | 98,6% | 20 |
| MP2,5 | Primaria diaria | 62,92 | 125,8% | 0,06 | 0,1% | 62,98 | 126,0% | 50 |

<!-- Estadísticas: 4 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. **Tabla 9-6: Concentraciones totales Proyecto, en estación Florida.** -->
<!-- FIN TABLA 9-5 -->


Tabla 9-6: Concentraciones totales Proyecto, en estación Florida. ............................................................ 50

<!-- INICIO TABLA 9-6 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |MP2,5|Primaria anual|19,72|98,6%|0,01|0,0%|19,72|98,6%|20| |MP2,5|Primaria diaria|62,92|125,8%|0,06|0,1%|62,98|126,0%|50| Fuente: Elaboración propia. -->

**Tabla 9-6: Concentraciones totales Proyecto, en estación Florida.****

| Contaminante | Tipo de Norma | LDB<br>[μg/m3] | % LDB_N | AP_Op<br>[μg/m3] | % AP_Op_N | CA_Op<br>[μg/m3] | % CA_Op _N | Norma<br>[μg/m3] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MP10 | Primaria anual | 39,74 | 79,5% | 0,00 | 0,0% | 39,75 | 79,5% | 50 |
| MP10 | Primaria diaria | 113,29 | 75,5% | 0,03 | 0,0% | 113,32 | 75,5% | 150 |
| MP2,5 | Primaria anual | 23,87 | 119,3% | 0,00 | 0,0% | 23,87 | 119,3% | 20 |
| MP2,5 | Primaria diaria | 94,67 | 189,3% | 0,03 | 0,1% | 94,69 | 189,4% | 50 |

<!-- Estadísticas: 4 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- 50 Anexo 4.b -->
<!-- FIN TABLA 9-6 -->


ii

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

**INDICE DE FIGURAS**

Figura 3-1: Pasos Metodológicos .................................................................................................................. 7

Figura 4-1: Ubicación de las estaciones de calidad del aire. ......................................................................... 9

Figura 5-1: Extensiones de los dominios 1, 2, 3 y 4 en WRF. ...................................................................... 12

Figura 5-2: Uso de suelo dominio 4 WRF. ................................................................................................... 15

Figura 5-3: Dominio de Modelación del Proyecto. ...................................................................................... 17

Figura 5-4: Topografía del dominio de modelación. ................................................................................... 19

Figura 5-5: Ciclo diario de la velocidad del viento modelada y observada. Estación Yerbas Buenas, año

2019. ............................................................................................................................................................ 23

Figura 5-6: Ciclo mensual de la velocidad del viento modelada y observada. Estación Yerbas Buenas, año

2019. ............................................................................................................................................................ 24

Figura 5-7: Cuantiles condicionales e histograma de velocidad del viento observada y modelada, estación

Yerbas Buenas, año 2019. ........................................................................................................................... 25

Figura 5-8: Ciclo diario de la velocidad del viento modelada y observada. Estación U. Maule, año 2019. 26

Figura 5-9: Ciclo anual de la velocidad del viento modelada y observada. Estación U. Maule, año 2019. 26

Figura 5-10: Cuantiles condicionales e histograma de velocidad del viento observada y modelada,

estación U. Maule, año 2019. ...................................................................................................................... 27

Figura 5-11: Rosa de los vientos observada y modelada año 2019. Estación Yerbas Buenas. ................... 28

Figura 5-12: Gráfico polar con frecuencia de desviación entre direcciones de viento modeladas y

observadas por intervalos de diferencia en magnitud de velocidad del viento. Estación Yerbas Buenas.

Año 2019. .................................................................................................................................................... 29

Figura 5-13: Ciclo diario de la dirección del viento observada. Estación Yerbas Buenas. Año 2019. ......... 30

Figura 5-14: Ciclo diario de la dirección del viento modelada. Estación Yerbas Buenas. Año 2019. .......... 31

Figura 5-15: Ciclo estacional de la dirección y velocidad del viento observada. Estación Yerbas Buenas.

Año 2019. .................................................................................................................................................... 32

Figura 5-16: Ciclo estacional de la dirección y velocidad del viento modelada. Estación Yerbas Buenas.

Año 2019. .................................................................................................................................................... 32

Figura 5-17: Rosa de los vientos observada y modelada año 2019. Estación U. Maule. ............................ 33

Figura 5-18: Gráfico polar con frecuencia de desviación entre direcciones de viento modeladas y

observadas por intervalos de diferencia en magnitud de velocidad del viento. Estación U. Maule. Año

2019. ............................................................................................................................................................ 34

Figura 5-19: Ciclo diario de la dirección del viento observada. Estación U. Maule. Año 2019. .................. 35

Figura 5-20: Ciclo diario de la dirección del viento modelada. Estación U. Maule. Año 2019. ................... 35

Figura 5-21: Ciclo estacional de la dirección y velocidad del viento observada. Estación U. Maule. Año

2019. ............................................................................................................................................................ 36

Figura 5-22: Ciclo estacional de la dirección y velocidad del viento modelada. Estación U. Maule. Año

2019. ............................................................................................................................................................ 37

Figura 5-23: Ciclo diario de la temperatura modelada y observada, Estación U. Maule. Año 2019. ......... 38

Figura 5-24: Ciclo mensual de la temperatura modelada y observada, Estación U. Maule, año 2019. ..... 38

iii

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

Figura 5-25: Cuantiles condicionales e histograma de velocidad del viento observada y modelada,

estación U. Maule, año 2019. ...................................................................................................................... 39

Figura 5-26: Ciclo diario modelado altura de capa de mezcla. Estación Yerbas Buenas. Año 2019. .......... 41

Figura 8-1: Grilla de receptores ................................................................................................................... 46

Figura 9-1: Isoconcentraciones Fase de operación: MP2.5 Anual .............................................................. 53

Figura 9-2: Isoconcentraciones Fase de operación: MP2.5 diario .............................................................. 54

Figura 9-3: Isoconcentraciones Fase de operación: MP2.5 diario, acercamiento a Proyecto .................... 55

Figura 9-4: Isoconcentraciones fase de operación: NO 2 anual ................................................................... 56

Figura 9-5: Isoconcentraciones Fase de operación: NO 2 anual, acercamiento a Proyecto......................... 57

Figura 9-4: Isoconcentraciones fase de operación: NO 2 horario (umbral de corte 1% norma) .................. 58

iv

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

##### 1 INTRODUCCIÓN

El presente informe contiene los resultados de la dispersión de contaminantes atmosféricos del proyecto

**DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA**, en su fase de operación,

considerando material particulado y gases, de acuerdo con el máximo de emisiones estimadas al

considerar 100 % biomasa como combustible.

El Proyecto se localiza en la comuna de Yerbas Buenas, provincia de Linares, perteneciente a la Región

del Maule.

##### 2 OBJETIVOS

Los objetivos definidos dentro del estudio de calidad del aire corresponden a:

 - Caracterización de la calidad del aire de la zona.

 Generación de un campo meteorológico tridimensional con el modelo WRF, para ser utilizado

como entrada meteorológica para el modelo de dispersión de contaminantes CALPUFF.

 Análisis de incertidumbre de la modelación meteorológica.

 Modelación de dispersión de las emisiones estimadas para la fase de operación del Proyecto,

considerando para estimar el aporte de estas emisiones al nivel de concentraciones ambientales

de material particulado y gases.

 Evaluación de cumplimiento normativo de la calidad del aire proyectada, considerando los

aportes de la operación del Proyecto, estimado a partir de las concentraciones estimadas por el

modelo de dispersión más las concentraciones basales medidas en las estaciones de calidad del

aire disponibles.

5

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

##### 3 METODOLOGÍA GENERAL

En el presente documento se expone un escenario de modelación, correspondiente a la fase de

operación del Proyecto, considerando como insumo las emisiones máximas para la Caldera 5 provistas

por el “mandante” al utilizar 100 % de biomasa como combustible. La meteorología utilizada como input

a CALPUFF, corresponde a la generada con el modelo de mesoescala WRF para el año 2019 que se

describe en la sección 0.

Con la modelación del escenario se determinarán los aportes de éstos en la calidad del aire. La calidad

del aire proyectada para la fase de operación del Proyecto será estimada de acuerdo con la siguiente

ecuación.

**CA_Op = LDB +AP_O+ AP_Op**

En donde:

**CA_Op** : corresponde a la calidad del aire proyectada para la fase de operación del Proyecto.

**LDB** : corresponde a la línea base de calidad del aire medida en el área de estudio.

**AP_O:** corresponde al aporte de otros proyectos con RCA que aún no estén ejecución

**AP_Op** : corresponde al aporte en la calidad del aire de la fase de operación del Proyecto.

En el presente informe también se describe la configuración y simulación meteorológica realizada con el

modelo de pronóstico WRF y se realiza un análisis de incertidumbre a dicha modelación, comparando los

resultados de parámetros meteorológicos a nivel superficial respecto a los datos medidos en cuatro

estaciones de monitoreo meteorológico.

La metodología general seguida para el estudio se presenta a continuación en la Figura 3-1.

6

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

**Figura 3-1: Pasos Metodológicos**

Fuente: Elaboración propia.

7

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

##### 4 CARACTERIZACIÓN CALIDAD DEL AIRE

A continuación se presenta la normativa de calidad del aire utilizada para los contaminantes evaluados

en la modelación de dispersión de contaminantes.

##### 4.1 Normativa Calidad del Aire Vigente

En el país existen normas primarias de calidad del aire vigentes para el material particulado respirable

(MP 10 ), para su fracción más fina (MP 2,5 ), y los gases dióxido de nitrógeno (NO 2 ), monóxido de carbono

(CO) y dióxido de azufre (SO 2 ). Los valores umbrales de las normas citadas se presentan en la Tabla 4-1.

**Tabla 4-1:** **Normas Primarias de Calidad del Aire Vigentes en Chile**

|Contaminante|Tipo de Norma|Estadístico|Límite Norma<br>(μg/m3N)|Referencia|
|---|---|---|---|---|
|MP10|Primaria anual|Media aritmética trianual|50|D.S.<br>N°59/1998|
|MP10|Primaria diaria|Percentil 98 de la de las concentraciones de 24<br>horas durante un año|150|150|
|MP2,5|Primaria anual|Media aritmética trianual|20|D.S.<br>N°12/2011|
|MP2,5|Primaria diaria|Percentil 98 de la de las concentraciones de 24<br>horas durante un año|50|50|
|SO2|Primaria anual|Media aritmética trianual|60|D.S.<br>No104/2018|
|SO2|Primaria diaria|Media aritmética trianual del Percentil 99 de<br>las concentraciones de 24 horas de cada año|150|150|
|SO2|Primaria horaria|Media aritmética trianual del Percentil 98,5 de<br>las concentraciones de 1 hora de cada año|350|350|
|NO2|Primaria horaria|Media aritmética trianual del Percentil 99 de<br>los máximos diarios de concentración de 1<br>hora de cada año|400|D.S.<br>N°114/2002|
|NO2|Primaria anual|Media aritmética trianual|100|100|
|O3|Primaria 8 horas|Media aritmética trianual del Percentil 99 de<br>los máximos diarios de concentración de 8<br>horas de cada año|120|D.S. N°112/02|
|CO|Primaria horaria|Media aritmética trianual del Percentil 99 de<br>los máximos diarios de concentración de 1<br>hora de cada año|30000|D.S. N°115/02|
|CO|Primario 8 horas|Media aritmética trianual del Percentil 99 de<br>los máximos diarios de concentración de 8<br>hora de cada año|10000|10000|

8

Fuente: Elaboración Propia

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

##### 4.2 Monitoreo calidad del aire

La Tabla 4-2 y la Figura 4-1 muestran las coordenadas y ubicación de las tres estaciones de calidad del

aire utilizadas para obtener concentraciones basales de los distintos contaminantes medidos en la zona y

posteriormente evaluar el aporte de las emisiones del Proyecto a las concentraciones ambientales de la

zona.

**Tabla 4-2: Coordenadas de ubicación de las estaciones de calidad del aire.**

|Col1|WGS84-Huso 19|Col3|Variable monitoreada|
|---|---|---|---|
|**Estación**|**UTM - E (m)**|**UTM - N (m)**|**UTM - N (m)**|
|Yerbas Buenas|265.391|6.057.869|MP10, MP2.5, NO2, CO, SO2, O3|
|U. Maule|262.216|6.075.477|MP10, MP2.5|
|La Florida|256.889|6.075.395|MP10, MP2.5, NO2, CO|

Fuente: Elaboración propia.

**Figura 4-1: Ubicación de las estaciones de calidad del aire.**

Fuente: Elaboración propia.

9

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

La Tabla 4-3 muestra las concentraciones basales de las estaciones de calidad del aire disponibles en las

cercanías del Proyecto. Se puede apreciar que la estación Yerbas Buenas, ubicada a 1 kilómetro al nor
noroeste del Proyecto alcanza la latencia para la norma diaria de MP2.5. En tanto, las otras dos

estaciones, U. Maule y La Florida, ubicadas en la ciudad de Talca, U. Maule presenta condiciones de

latencia para MP10 y saturación de MP2.5, mientras que La Florida presenta solo saturación por MP2.5,

pero esta última estación es la que presenta mayores concentraciones de MP2.5 de las dos estaciones.

**Tabla 4-3: Concentraciones basales estaciones calidad del aire año 2019.**

|Col1|μg/m3|Yerbas Buenas|Col4|U. Maule|Col6|La Florida|Col8|Norma|
|---|---|---|---|---|---|---|---|---|
|**Contaminante**|**Tipo de Norma**|**LDB**|**% LDB_N**|**LDB**|**% LDB_N**|**LDB**|**% LDB_N**|**% LDB_N**|
|MP10|Primaria anual|25,7|51,4%|41,7|83,3%|39,7|79,5%|50|
|MP10|Primaria diaria|66,7|44,5%|86,9|57,9%|113,3|75,5%|150|
|MP2,5|Primaria anual|14,8|73,8%|19,7|98,6%|23,9|119,3%|20|
|MP2,5|Primaria diaria|45,8|91,6%|62,9|125,8%|94,7|189,3%|50|
|SO2|Primaria anual|2,4|4,0%|-|-|-|-|60|
|SO2|Primaria diaria|9,4|6,2%|-|-|-|-|150|
|SO2|Primaria horaria|14,7|4,2%|-|-|-|-|350|
|NO2|Primaria anual|8,4|8,4%|-|-|16,2|16,2%|100|
|NO2|Primaria horaria|82,8|20,7%|-|-|66,0|16,5%|400|
|CO|Primaria horaria|1400,0|4,7%|-|-|10971|36,6%|30.000|
|CO|Primario 8<br>horas|606,8|6,1%|-|-|6739|67,4%|10.000|
|O3|Primaria 8 horas|86,7|72,2%|-|-|-|-|120|

Fuente: Elaboración propia.

10

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

##### 5 MODELO METEOROLÓGICO 5.1 Justificación del Modelo Meteorológico

Según lo establecido por la Guía para el uso de Modelos de Calidad del Aire en el SEIA, la selección del

modelo meteorológico utilizado en el presente estudio se realizó fundamentándose en las condiciones

del dominio de modelación del área entorno al proyecto, motivo por el cual la Guía recomienda un

modelo que permita simular una meteorología heterogénea. Por esta razón, el campo meteorológico

tridimensional horario del año 2019 completo fue generado utilizando el modelo meteorológico WRF, en

su versión 4.0.3, y procesado con MMIF v3.2. Posteriormente esta información fue utilizada en el modelo

de calidad de aire CALPUFF.

##### 5.2 Descripción del Modelo Meteorológico

El modelo de investigación y pronóstico del tiempo (Weather Research and Forecasting - WRF) es un

sistema de predicción numérico de mesoscala de nueva generación, diseñado para servir pronósticos

operacionales y para estudio de la atmósfera.

Se crearon cuatro dominios anidados con resoluciones de grilla de 27, 9, 3 y 1 kilómetro

correspondientemente, los cuales se muestran en la Figura 5-1, en rojo se indica el dominio de

modelación más pequeño, el cual se utilizará para alimentar el modelo de dispersión CALPUFF. La Tabla

5-1 y la Tabla 5-2 muestran la definición de los dominios anidados utilizados en WRF y la proyección

geográfica, respectivamente.

11

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

**Figura 5-1: Extensiones de los dominios 1, 2, 3 y 4 en WRF.**

Fuente: Elaboración propia, en base a Google Earth.

**Tabla 5-1: Definición de dominio de modelación.**

|Col1|DX|DY|NX|NY|KMx|KMy|No Celdas|
|---|---|---|---|---|---|---|---|
|Dominio 1|27|27|70|70|1.890|1.890|4.900|
|Dominio 2|9|9|67|67|603|603|4.489|
|Dominio 3|3|3|64|64|192|192|4.096|
|Dominio 4|1|1|61|61|61|61|3.721|

Fuente: Elaboración propia.

Donde,

DX y DX son los tamaños de celda en dirección X y Y,

NX y NY son los números de celdas en dirección X e Y,

KMx y KMy corresponde al tamaño de los dominios en dirección X e Y

N° Celdas es el número de celdas total de cada dominio

12

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

**Tabla 5-2: Definición proyección dominios de modelación.**

|Origen centro Dominio 1<br>y proyección LCC|Col2|
|---|---|
|ref_lat|-35,61|
|ref_lon|-71,58|
|truelat1|-30,61|
|truelat2|-40,61|
|stand_lon|-71,58|

Fuente: Elaboración propia.

Debido a la geomorfología del valle central de la Región del Maule y también la presencia de algunas

zonas urbanas, el sector modelado presenta velocidades del viento promedio, para los niveles

superficiales, que son extremadamente bajas, velocidades que configuraciones típicas del modelo WRF

sobreestiman de manera considerable ya que no resuelven de manera satisfactoria el efecto superficie

del terreno en el comportamiento del viento. Por esta razón en el presente estudió se utilizó una

configuración mejorada del modelo para la cuenca en conjunto con una configuración para resolver los

efectos que el suelo urbano tiene sobre la meteorología local, mayores detalles de la configuración se

describen a continuación.

Para realizar la simulación con el modelo WRF se obtuvo la información de uso de suelos a partir de
información satelital de MODIS [1] de la NASA con resolución de 15 segundos de grado, información que

fue refinada con Wtools utilizando imágenes satelitales (ver Figura 5-2); e información de elevación de

terreno a partir de la información topográfica del SRTM (Misión de Radar Topográfico del Transbordador
Espacial de la NASA [2] ) con resolución de 3 segundos de grado, es decir 90 metros aproximadamente.

Condiciones iniciales y de borde fueron generadas a partir de los “datos operacionales de análisis
global” [3] de NCEP [4] con un grado de resolución espacial de 1° y temporal de 6 horas, complementada con

información de temperaturas de la superficie del mar obtenidas a partir de archivos en tiempo real de

“Sea Surface Temperature” de NCEP con resolución de 1/12 de grado.

Se utilizó la configuración de WRF publicada en el estudio de Saide, Mena‐Carrasco et al (2016) [5] de

pronóstico de MP2,5 en Santiago, con la principal excepción de que además se utilizó la opción de

1 https://modis.gsfc.nasa.gov/
2 https://www2.jpl.nasa.gov/srtm/
3 FNL (Final) Operational Global Analysis data
4 U.S. National Center of Environmental Prediction perteneciente a la NOAA
5 Saide, P. E., et al. (2016). "Air quality forecasting for winter‐time PM2. 5 episodes occurring in multiple cities in
central and southern Chile." Journal of Geophysical Research: Atmospheres 121(1): 558-575.

13

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

parametrización urbana BEP (Salamanca, Martilli et al. 2011) [6], la cual consiste en un modelo de "canopy

urbano" de multicapa, configuración que si bien no se utilizó en el mencionado estudio, éste recomienda

utilizarlo en trabajos futuros. La mencionada configuración urbana ha sido trabajada en el contexto del
Proyecto Fondecyt-1180894 [7], el cual se encuentra en ejecución. En trabajo precedente a la postulación

al Fondecyt se verificó la substancial mejora que produce la configuración urbana en la simulación

meteorológica para la cuenca de Santiago, particularmente en lo que respecta a la reducción en las

velocidades de vientos modeladas. Además se activaron para todos los dominios de la simulación las

opciones de "slope_rad" y "topo_shading", las cuales consideran el efecto de la pendiente del terreno en

el flujo de la radiación solar superficial y consideran los efectos de sombra que pueden generar las celdas

circundantes que posean elevación terreno mayor a la celda considerada, respectivamente.

Adicionalmente a lo ya mencionado, las principales parametrizaciones y configuraciones de las opciones

físicas del modelo son las siguientes:

a) Se utilizaron 44 niveles verticales ETA.

b) Para la estimación de la capa límite planetaria se utilizó el esquema de BouLac (Bougeault and

Lacarrere,1989) [8] para los 3 dominios, el cual es un modelo predicción de TKE ("turbulent kinetic

energy", energía cinética turbulenta) que permite utilizar el modelo de parametrización urbana

de edificios BEP (Building Environment Parameterization).

c) Para la estimación de la capa límite superficial se utilizó el esquema de eliminación de escala

cuasi-normal de la capa limite (QNSE) desarrollado por Sukoriansky, Galperin y Perov,

(Sukoriansky, Galperin et al. 2006) [9] .

d) Para la simulación de los intercambios de calor entre superficie y atmosfera se utilizó el “Noah

Land Surface Model”, opción compatible con la clasificación de uso de suelos utilizada en la

información satelital de MODIS de la NASA.

e) Por último, para la estimación de formación de nubes se utilizó el esquema convectivo de Betts

Miller-Janjic (Betts and Miller 1986, Janjic 1994)

6 Salamanca, F., et al. (2011). "A study of the urban boundary layer using different urban parameterizations and
high-resolution urban canopy parameters with WRF." Journal of Applied Meteorology and Climatology 50(5): 1107
1128.

7 Jorquera, H., Castro J. y Villalobos A.
8 Bougeault, P. and P. Lacarrere (1989). "Parameterization of Orography-Induced Turbulence in a Mesobeta--Scale
Model." Monthly Weather Review 117(8): 1872-1890.
9 Sukoriansky, S., et al. (2006). "A quasi-normal scale elimination model of turbulence and its application to stably
stratified flows." Nonlinear Processes in Geophysics 13(1): 9-22.

14

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

Como se muestra más adelante el modelo WRF logra obtener magnitudes de vientos bastante similares a

las medidas en Talca, pero en la zona del Proyecto la magnitud del viento modelado es

considerablemente mayor al viento medido en la estación meteorológica Yerbas Buenas.

La Figura 5-2 muestra el uso de suelo utilizado en lo modelos WRF y Calpuff. En este caso gran parte del

dominio de modelación considera el uso de suelo de cultivos y bosques.

**Figura 5-2: Uso de suelo dominio 4 WRF.**

Fuente: Elaboración propia, en base a Google Earth y Wtools.

##### 5.3 Dominio Modelación

El dominio de modelación considerado para el presente Proyecto corresponde a una grilla rectangular de

55 x 55 km, compuesta por celdas de 1 km por lado, la cual tiene la misma proyección utilizada por el

modelo WRF y corresponde a un subdominio del dominio 4 modelado con WRF, eliminando 5 celdas por

borde, siguiendo la recomendación de la guía de MMIF, el cual es el post-procesador utilizado para

extraer datos de WRF a CALPUFF. En la Tabla 5-3 se presentan las características del área

correspondiente al dominio de modelación. El dominio elegido abarca a lo menos el área de influencia

15

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

del Proyecto para los distintos componentes ambientales que pueden verse afectados por las emisiones

atmosféricas de éste, lo que se corrobora más adelante en las gradientes de concentraciones estimadas

por el modelo.

**Tabla 5-3: Características del Dominio de Modelación.**

|Característica|Eje X (km)|Eje Y (km)|
|---|---|---|
|Espaciamiento|1|1|
|Longitud|55|55|

Fuente: Elaboración propia.

En la Figura 5-3, se presenta el dominio de modelación utilizado en CALPUFF, donde se destacan en azul

las estaciones meteorológicas Yerbas Buenas, U. Maule y La Florida, las dos primeras son utilizadas en el

análisis de incertidumbre del modelo WRF para los parámetros de vientos y la estación U. Maule

también es utilizada para evaluar temperatura.

16

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

**Figura 5-3: Dominio de Modelación del Proyecto.**

2

Fuente: Elaboración propia.

17

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

##### 5.4 Topografía y Uso de Suelos

La fuente de información topográfica del dominio de modelación considerado en CALPUFF corresponde
a cartas topográficas digitales SRTM3 [10] de 90 metros de resolución, las cuales se utilizan el modelo WRF.

En CALPUFF se utilizó la información topográfica considerada por el modelo WRF. A continuación, se

presenta una imagen de la topografía, que corresponde al SRTM3 interpolado a la resolución de grilla de

1 kilómetro que utilizan los modelos WRF y CALPUFF en este caso.

La información relacionada con el uso de suelo, de igual manera que la elevación de terreno es utilizada

directamente del modelo WRF, la cual corresponde a información satelital de MODIS de la NASA con

resolución de 15 segundos de arco, la caracterización de uso de suelos para cada celda del dominio 4 de

WRF se puede observar en la Figura 5-2.

A continuación, en la Figura 5-4, se presenta gráficamente la topografía del dominio modelado, donde se

destacan en azul las estaciones meteorológicas y de calidad del aire, cuyas coordenadas se muestran en

la Tabla 5-4. Cabe destacar la gran complejidad de la geomorfología en el sector oriente del dominio.

10 https://www2.jpl.nasa.gov/srtm/

18

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

**Figura 5-4: Topografía del dominio de modelación.**

Fuente: Elaboración propia en base a información proporcionada por NASA.

**Tabla 5-4. Coordenadas estaciones meteorológicas**

|Col1|WGS84-Huso 19|Col3|
|---|---|---|
|**Estación**|**UTM - E (m)**|**UTM - N (m)**|
|Yerbas Buenas|265.391|6.057.869|
|Universidad Maule|262.216|6.075.477|
|La Florida|256.889|6.075.395|

Fuente: GAC

19

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

##### 5.5 Caracterización meteorológica de la zona y evaluación del modelo meteorológico

Para evaluar el desempeño de la modelación meteorológica utilizada en el modelo, se han analizado

estadísticamente los datos medidos de vientos en el año 2019 en la estación Yerbas Buenas, ubicada a 1

kilómetro al nor-noroeste (NNO) del Proyecto, en la U. Maule ubicada a 19 kilómetros al norte del

Proyecto, dentro del radio urbano de Talca, cuyas coordenadas se presentan en la Tabla 5-4. Para ello se

han extraído los resultados del modelo meteorológico para la coordenada ( _x,y_ ) donde se emplazan la

estaciones meteorológicas, a 10 metros de altura, coincidente con la altura del anemómetro de las

estaciones. Las variables consideradas para la evaluación corresponden a: velocidad del viento y

dirección del viento y temperatura. Para cada una, se evaluó el ciclo diario y la serie de tiempo. Es

importante tener en cuenta que los datos de las estaciones monitoras corresponden a datos medidos en

un punto, mientras que los datos obtenidos del modelo corresponden a datos representativos de una

celda de 1 x 1 kilómetros, especialmente en este caso donde la configuración geomorfológica de la zona

es muy compleja.

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

N

SP= [1]

n [∑(M] [i] [−O] [i] [)]

i=1

20

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

- **Error absoluto medio (MAE):** Este coeficiente se utiliza para medir el desempeño de modelos y

consiste en el promedio de los errores absolutos, este coeficiente ignora punto a punto si el

error es una subestimación o sobreestimación del modelo.

#### ( M i − O i )

MAE=

_n_
####  ( M i − O i

_i_ = 1

_i_

###### _n_

- **Sesgo medio normalizado (SMN):** Sesgo medio pero normalizado respecto a los valores

observados.

SMN=

∑ ni=1 (M i −O i )

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

N

1

r=
(1 −n) [∑(M] [i] σ [−M̅)] M

(O i −O [̅] )

σ o

i=1

σ M

21

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

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

A continuación, se presentan los resultados para las variables consideradas.

###### 5.5.1 Velocidad del Viento

Yerbas Buenas

En la Figura 5-5 se presenta el ciclo diario de la mediana de la velocidad del viento horaria modelada y

observada junto con los percentiles 5 y 95 de los datos en el punto correspondiente a la estación Yerbas

Buenas. En ella, se puede observar que la mediana modelada esta por sobre la observada durante todo

el día, alcanzando un sesgo mínimo de 1,5 m/s y un sesgo máximo de hasta 3 m/s.

22

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

**Figura 5-5: Ciclo diario de la velocidad del viento modelada y observada.**

**Estación Yerbas Buenas, año 2019.**

Fuente: Elaboración propia.

En la Figura 5-6 se presenta el ciclo anual de la mediana de la velocidad del viento observada y modelada

con los percentiles 5 y 95 en la estación Yerbas Buenas, donde es posible apreciar que el modelo estima

velocidades del viento mayores a las registradas en la estación monitora durante todos los meses del

año. La estacionalidad de la velocidad del viento es mucho más acentuada en la serie de tiempo

modelada que en la de los registros medidos en la estación. Cabe mencionar que la baja estacionalidad

de la velocidad del viento medida no es típica de una zona alejada de la costa.

23

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

**Figura 5-6: Ciclo mensual de la velocidad del viento modelada y observada.**

**Estación Yerbas Buenas, año 2019.**

Fuente: Elaboración propia.

En la Figura 5-7 es posible corroborar que el modelo estima magnitudes de velocidades del viento

muchas más altas que las magnitudes de velocidad del viento medidas en estación Yerbas Buenas para

todos los rangos de velocidad del viento.

24

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

**Figura 5-7: Cuantiles condicionales e histograma de velocidad del viento observada y modelada, estación Yerbas**

**Buenas, año 2019.**

Fuente: Elaboración propia.

U. Maule

En la Figura 5-8 se presenta el ciclo diario de la mediana de la velocidad del viento horaria modelada y

observada junto con los percentiles 5 y 95 de los datos en el punto correspondiente a la estación

meteorológica U. Maule. En ella, se puede observar que existe una muy alta correlación entre los ciclos

diarios modelados y observados, con la única excepción de que el modelo estima mayores velocidades

en horas de la noche y madrugada que los registros medidos en la estación.

25

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

**Figura 5-8: Ciclo diario de la velocidad del viento modelada y observada.**

**Estación U. Maule, año 2019.**

Fuente: Elaboración propia.

En la Figura 5-9 se presenta el ciclo anual de la mediana de la velocidad del viento observada y modelada

con los percentiles 5 y 95 en la estación meteorológica U. Maule, donde si bien se aprecian un sesgo

positivo sistemático entre ambos ciclos, éstos presentan una muy alta correlación.

**Figura 5-9: Ciclo anual de la velocidad del viento modelada y observada.**

**Estación U. Maule, año 2019.**

Fuente: Elaboración propia.

26

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

El gráfico de la Figura 5-10 muestra una muy alta correlación entre las velocidades del viento observadas

y modeladas en estación U. Maule, ya que el diagrama de dispersión muestra una mediana muy cercana

a la recta de 45 grados. En el histograma es posible apreciar frecuencias de vientos muy simulares para

los distintos intervalos de velocidades, solo con la excepción para las magnitudes de vientos medidas

menores de 0,5 m/s. y para magnitudes mayores a 3,6 m/s.

**Figura 5-10: Cuantiles condicionales e histograma de velocidad del viento observada y modelada, estación U.**

**Maule, año 2019.**

Fuente: Elaboración propia.

La Tabla 5-5 muestra los promedios y máximos de la velocidad del viento en conjunto con el porcentaje

de calmas, observado y modelado para ambas estaciones. El modelo estima velocidades de viento

considerablemente mayores a las observadas en Yerbas Buenas y levemente mayores a las observadas

en U. Maule. Por otra parte, el modelo estima mayores frecuencias de condiciones de calma (vientos

menores a 0,5 m/s) que los registros de las estaciones monitoras.

**Tabla 5-5: Estadígrafos velocidad del viento, estaciones Yerbas Buenas y U. Maule.**

|Col1|Yerbas Buenas|Col3|U. Maule|Col5|
|---|---|---|---|---|
|**Variable**|**Observado**|**Modelado**|**Observado**|**Modelado**|
|Promedio (m/s)|1,50|3,75|1,416|1,51|
|Mediana (m/s)|1,40|3,60|1,25|1,50|
|Porcentaje de calmas|5,2%|3,9%|17,7%|14,2%|

Fuente: Elaboración propia.

27

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

El análisis presentado anteriormente de los datos medidos y modelados en las estaciones Yerbas Buenas

y U. Maule muestran, al igual como se puede observar en la Tabla 5-6, que el modelo se asimila mucho

más a los datos medidos en la estación U. Maule que en la estación Yerbas Buenas. En resumen, el

modelo presenta una alta concordancia con el monitoreo de velocidad del viento U. Maule con un valor

de 0,63 y una concordancia media-baja en estación Yerbas Buenas.

**Tabla 5-6: Estadígrafos de desempeño velocidad del viento. Año 2018.**

|Estación|N|Sesgo|FAC2|SM|MAE|SMN|NMAE|ECM|r|IOA|
|---|---|---|---|---|---|---|---|---|---|---|
|Yerbas Buenas|7279|2,25|0,28|2,46|2,57|164,2%|171,8%|3,07|0,48|-0,56|
|U. Maule|8710|0,10|0,77|0,09|0,54|6,7%|38,0%|0,69|0,68|0,63|

Fuente: Elaboración propia.

###### 5.5.2 Dirección del Viento

Yerbas Buenas

En la Figura 5-11 se presenta la rosa de los vientos correspondiente a los valores de dirección del viento

modelada y observada en el punto correspondiente a la estación Yerbas Buenas. Es posible verificar que

a diferencia de la magnitud del viento el nivel de concordancia entre las direcciones modeladas y

observadas es alto. El modelo presenta de buena manera la componente principal del viento, pero

subestima las frecuencias del componente nor-noreste (NNE).

**Figura 5-11: Rosa de los vientos observada y modelada año 2019.**

**Estación Yerbas Buenas.**

|Observada|Modelada|
|---|---|
|||

Fuente: Elaboración propia.

28

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

En la Figura 5-12 se presenta un gráfico polar que indica la frecuencia de datos para la desviación del

viento modelado en grados respecto a la dirección del viento observado, es decir para las 8760 horas del

año se obtiene la diferencia (o delta) entre el viento modelado y observado, además en tonos de rojo se

indica frecuencia de datos con magnitudes de viento sobreestimadas respecto a lo observado y en tonos

de azul frecuencia de datos con magnitudes de viento subestimadas respecto a lo observado. A modo de

explicación, un modelo con direcciones de viento que coincidieran perfectamente con lo observado

presentaría un solo componente norte (0°) con una frecuencia del 100 % en el gráfico polar expuesto.

El gráfico muestra mayoritariamente tonos burdeos lo que se refleja en un delta promedio de la

magnitud del viento modelado de 2,5 m/s respecto al promedio observado. Respecto a las direcciones

de viento se puede ver observar que existe una rotación muy leve entre los datos observados y

modelados, donde las direcciones modeladas presentan una rotación promedio de solo 1,3 grados

respecto a las direcciones medidas en el sentido horario.

**Figura 5-12: Gráfico polar con frecuencia de desviación entre direcciones de viento modeladas y observadas por**

**intervalos de diferencia en magnitud de velocidad del viento. Estación Yerbas Buenas. Año 2019.**

Fuente: Elaboración propia.

La Figura 5-13 y la Figura 5-14 muestran las frecuencias de vientos observadas y modeladas para

distintas horas del día, donde es posible observar que tanto el modelo como los datos observados

29

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

presentan una componente predominante sur-suroeste (SSO). Al igual que en el ciclo diario de la

velocidad del viento es posible apreciar cierto desfase en los ciclos diarios de la frecuencia de viento.

**Figura 5-13: Ciclo diario de la dirección del viento observada. Estación Yerbas Buenas. Año 2019.**

Fuente: Elaboración propia.

30

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

**Figura 5-14: Ciclo diario de la dirección del viento modelada. Estación Yerbas Buenas. Año 2019.**

Fuente: Elaboración propia.

La Figura 5-15 y la Figura 5-16 muestran que tanto la velocidad del viento observada y modelada

presentan máximos durante horas de la tarde, los cuales son más acentuados durante los meses de

verano, nuevamente se puede apreciar un desfase entre los ciclos diarios modelados y observados con

un evidente sesgo positivo en la magnitud de los vientos.

31

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

**Figura 5-15: Ciclo estacional de la dirección y velocidad del viento observada.**

**Estación Yerbas Buenas. Año 2019.**

Fuente: Elaboración propia.

**Figura 5-16: Ciclo estacional de la dirección y velocidad del viento modelada.**

**Estación Yerbas Buenas. Año 2019.**

Fuente: Elaboración propia.

32

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

U. Maule

En la Figura 5-17 se presenta la rosa de los vientos correspondiente a los valores de dirección del viento

modelada y observada en el punto correspondiente a la estación U. Maule. La rosa de vientos observada

y modelada presentan el mismo componente predominante de vientos sur-suroeste (SSO) pero con una

pequeña rotación en el sentido horario.

**Figura 5-17: Rosa de los vientos observada y modelada año 2019.**

**Estación U. Maule.**

|Observada|Modelada|
|---|---|
|||

Fuente: Elaboración propia.

El gráfico polar de la Figura 5-18 muestra una frecuencia similar de datos en tonos burdeos y azules, pero

también una gran frecuencia de datos en color blanco, lo que indica en promedio una diferencia

moderada de velocidades de viento modeladas respecto a las observadas, el delta promedio de la

magnitud del viento modelado es de 0,1 m/s respecto al promedio observado. Respecto a las direcciones

de viento se puede ver que la mayoría de los datos no presentan desviaciones en la dirección de viento

mayores a los 45 grados respecto a los datos observados, es posible observar que existe una rotación

promedio de solo en 17,5 grados en sentido horario.

33

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

**Figura 5-18: Gráfico polar con frecuencia de desviación entre direcciones de viento modeladas y observadas por**

**intervalos de diferencia en magnitud de velocidad del viento. Estación U. Maule. Año 2019.**

Fuente: Elaboración propia.

La Figura 5-19 y la Figura 5-20 muestran las frecuencias de vientos observadas y modeladas para

distintas horas del día, donde es posible observar una alta correlación entre las direcciones de viento

modeladas y observadas más predominantes, predominantemente sur-suroeste (SSO), con el alcance de

que los datos medidos presentan algo más de variabilidad que los datos modelados.

34

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

**Figura 5-19: Ciclo diario de la dirección del viento observada. Estación U. Maule. Año 2019.**

Fuente: Elaboración propia.

**Figura 5-20: Ciclo diario de la dirección del viento modelada. Estación U. Maule. Año 2019.**

Fuente: Elaboración propia.

35

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

La Figura 5-21 y la Figura 5-22 muestran que tanto la velocidad del viento observada y modelada

presentan máximos durante horas de la tarde, los cuales son más acentuados durante los meses de

verano, también es posible ver que el modelo presenta ciclos diarios según mes del año muy similares a

los medidos. Se ve cierta diferencia entre los vectores promedio modelados y observados, especialmente

en invierno, en específico en el mes de junio.

**Figura 5-21: Ciclo estacional de la dirección y velocidad del viento observada.**

**Estación U. Maule. Año 2019.**

Fuente: Elaboración propia.

36

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

**Figura 5-22: Ciclo estacional de la dirección y velocidad del viento modelada.**

**Estación U. Maule. Año 2019.**

Fuente: Elaboración propia.

###### 5.5.3 Temperatura

A continuación, se analizan los ciclos diarios y mensuales de la temperatura observada y modelada en la

estación U. Maule

Estación U. Maule

En la Figura 5-23 se presenta el ciclo diario de las medianas de la temperatura horaria modelada y

observada junto con los percentiles 5 y 95 de los datos en el punto correspondiente a la estación U.

Maule. En ella se puede ver que el ciclo diario presenta muy alta correlación entre los datos observados y

modelados con amplitudes térmicas diarias muy similares.

37

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

**Figura 5-23: Ciclo diario de la temperatura modelada y observada,**

**Estación U. Maule. Año 2019.**

Fuente: Elaboración propia

En la Figura 5-24 se presenta el ciclo mensual de temperatura observada y modelada con los percentiles

5 y 95 en la estación U Maule, donde es posible apreciar que el ciclo mensual de temperatura estimado

por el modelo presenta una muy alta correlación respecto a los datos observados pero con un sesgo

mensual positivo en los primeros 5 meses del año.

**Figura 5-24: Ciclo mensual de la temperatura modelada y observada,**

**Estación U. Maule, año 2019.**

Fuente: Elaboración propia

38

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

El gráfico de dispersión de la Figura 5-25 muestra una muy alta correlación entre las temperaturas

observadas y modeladas en estación la estación U. Maule con diagramas también muy similares.

**Figura 5-25: Cuantiles condicionales e histograma de velocidad del viento observada y modelada, estación U.**

**Maule, año 2019.**

La Tabla 5-7 muestra el promedio, mediana máximo y mínimo de temperatura observada y modelada

para la estación U. Maule, donde el modelo presenta un sesgo de 0,66 °C y 0,30 °C para el promedio y

mediana respectivamente. Por otra parte, la Tabla 5-8 muestra un coeficiente de correlación (r) e índice

de concordancia muy altos, con valores de 0,93 y 0,81 respectivamente.

**Tabla 5-7: Estadígrafos de temperatura, estación U. Maule.**

|Col1|U. Maule|Col3|
|---|---|---|
|**Variable**|**Observado**|**Modelado**|
|Promedio (°C)|15,03|15,69|
|Mediana (°C)|13,90|14,20|
|Máximo (°C)|36,70|39,30|
|Mínimo (°C)|-1,50|1,10|

Fuente: Elaboración propia

39

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

**Tabla 5-8: Estadígrafos desempeño por temperatura, estación U. Maule, datos observados y modelados.**

|Estación|n|Sesgo|FAC2|SM|MAE|SMN|NMAE|ECM|r|IOA|
|---|---|---|---|---|---|---|---|---|---|---|
|U. Maule|8710|0,66|0,96|0,64|2,18|4,3%|14,5%|2,86|0,93|0,81|

Fuente: Elaboración propia

###### 5.5.4 Altura capa de mezcla en zona modelada

A continuación, se presenta un análisis cualitativo del comportamiento estacional y horario de la altura

de capa de mezcla modelada con el modelo WRF, se realiza un análisis cualitativo ya que no existen

datos medidos para dicho parámetro. La Figura 5-26 muestra el perfil diario promedio por mes del año

de la altura de capa de mezcla modelada en la estación Yerbas Buenas. Se puede apreciar que los

máximos diarios para todos los meses se alcanzan entre las 13:00 y 15:00 horas, alcanzando un máximo

diario promedio de unos 2000 metros de altura entre los meses de diciembre a febrero y un valor

máximo diario considerablemente más bajo durante los meses de invierno, donde el promedio del

máximo diario en el mes de julio alcanza solo unos 500 metros de altura. Se presenta una alta amplitud

estacional de la altura capa de mezcla debido a la lejanía de la costa. Se puede apreciar que la altura de

capa de mezcla se eleva más temprano y baja más tarde durante los meses de verano, mientras que en

los meses de invierno la capa de mezcla se mantiene durante más horas en niveles bajos, debido

principalmente a que las horas de luz diurna son menores en invierno. La variación temporal de la altura

de capa de mezcla modelada, tanto estacional como horaria, presenta un patrón típico de este

parámetro.

40

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

**Figura 5-26: Ciclo diario modelado altura de capa de mezcla.**

**Estación Yerbas Buenas. Año 2019.**

Fuente: Elaboración propia

###### 5.5.5 Análisis necesidad de uso de factor de ajuste del modelo meteorológico en base a la velocidad del viento observada y modelada

A partir de los datos observados y modelados en las estaciones Yerbas Buenas y U. Maule, se obtiene un

factor de corrección para las concentraciones estimadas con el modelo de dispersión, suponiendo de

manera conservadora, que las concentraciones atmosféricas presentan una relación lineal inversa con la

mediana de la velocidad del viento anual, en razón de 1:1. De esta manera se obtiene un factor de

corrección a partir del promedio de las razones entre la mediana de la velocidad del viento modelada y la

mediana de la velocidad del viento observada en ambas estaciones de 1,89. Se repite el mismo ejercicio

utilizando los promedios de las velocidades, obteniendo un factor de corrección de 1,79, cuyos detalles

se muestran en la Tabla 5-10. Como este factor es bastante mayor a 1 debido a que la magnitud de

viento modelada en Yerbas Buenas es considerablemente más alta que la medida en ese punto, se

considera utilizar un factor de corrección en las concentraciones estimadas por el modelo de 1,89.

41

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

**Tabla 5-9: Estadísticos velocidad del viento.**

|Col1|Yerbas Buenas|Col3|U. Maule|Col5|
|---|---|---|---|---|
|**Variable**|**Observado**|**Modelado**|**Observado**|**Modelado**|
|Promedio (m/s)|1,50|3,75|1,416|1,51|
|Mediana (m/s)|1,40|3,60|1,25|1,50|
|Máximo (m/s)|6,70|15,60|4,7|5,80|
|Porcentaje de calmas|5,2%|3,9%|17,7%|14,2%|

Fuente: Elaboración propia

**Tabla 5-10: Factor de corrección.**

|Col1|Yerbas Buenas|U. Maule|Promedio|
|---|---|---|---|
|Razón VV mod/obs promedio|2,50|1,07|1,79|
|Razón VV mod/obs mediana|2,57|1,20|1,89|

Fuente: Elaboración propia.

###### 5.5.6 Conclusiones modelo meteorológico

Se realiza una modelación con el modelo WRF para el año 2019, cuyo desempeño para la estimación de

viento se evaluó en la estación Yerbas Buenas, la que está ubicada a 1 kilómetro al nor-noroeste del

Proyecto y además se evaluaron los vientos y temperatura en la estación meteorológica U. Maule

ubicada a 19 kilómetros al norte del Proyecto en Talca. En la estación Yerbas Buenas el modelo presenta

un sesgo normalizado para la magnitud del viento de un 257% para la mediana y de un 250% para

promedio y en la estación U. Maule este sesgo es mucho más bajo, solo de un 20% para la mediana y de

un 7% para el promedio. Para la dirección del viento ambas estaciones presentan una alta concordancia

con una rotación promedio de 1,3 grados en sentido horarios en estación Yerbas Buenas y de 17,5

grados en sentido horario en estación U. Maule.

La concordancia en la temperatura modelada y observada en la estación U. Maule es muy alta, con una

muy alta correlación y alto índice de concordancia.

A partir de los datos de la magnitud del viento observados y modelados en las estaciones Yerbas Buenas

y U. Maule se obtiene un factor de corrección de 1,89.

Finalmente se analizó cualitativamente el comportamiento de la altura de capa de mezcla promedio

horaria por mes del año, cualitativamente ya que no existen datos medidos del parámetro, la cual

presenta un comportamiento estimado satisfactorio respecto al ciclo diario y estacional de dicho

parámetro.

42

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

##### 6 MODELO CALIDAD DEL AIRE 6.1 Justificación modelo calidad del aire

De acuerdo con lo establecido en la Guía para el uso de Modelos de Calidad del Aire en el SEIA, la

selección del modelo de Calidad del Aire se basa en la topografía compleja del área donde se emplaza el

proyecto y al alcance de las emisiones. Por esta razón, el modelo utilizado fue un modelo tipo “Puff”

como lo es CALPUFF.

##### 6.2 Descripción modelo de calidad del aire

La simulación del aporte del proyecto a las concentraciones de contaminantes se realizará mediante el

modelo CALPUFF, recomendado por la U.S. EPA para la evaluación de dispersión de contaminantes

desde fuentes continuas.

CALPUFF es un sistema de modelación avanzado para calidad del aire que considera además la

meteorología de carácter no permanente. Su desarrollo estuvo a cargo del “Sigma Research
Corporation”, mientras que su mantenimiento actual es responsabilidad de Exponent [11] . Debido a su

desempeño,

CALPUFF fue catalogado por la USEPA como modelo recomendado [12] para la evaluación del impacto en la

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

11 [www.src.com/calpuff/calpuff1.htm](http://www.src.com/calpuff/calpuff1.htm)
12 Los modelos de dispersión y calidad del aire recomendados por USEPA, así como su campo de aplicación, están contenidos en
el Appendix W del 40 CFR Part 51 “Directrices para Modelos de Calidad del Aire”
( [http://www.epa.gov/scram001/guidance_permit.htm#appw](http://www.epa.gov/scram001/guidance_permit.htm#appw) ).

43

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

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

por el modelo meteorológico WRF correspondiente al año 2017, fue procesada en MMIF v3.2 para ser

ingresada al modelo de dispersión CALPUFF de manera directa.

44

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

##### 7 EMISIONES INGRESADAS AL MODELO

La Tabla 7-1 muestra el caudal, concentraciones y emisiones estimadas en la chimenea de la futura

caldera 5. La Tabla 7-2 muestra las características de la chimenea, cuyos datos fueron provistos por el

mandante.

**Tabla 7-1: Emisiones Caldera 5**

|Combustible|Caudal|Concentración Máxima|Col4|Col5|Emisión Máxima|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Combustible**|**Caudal**|**MP**|**NOx**|**CO**|**MP**|**NOx**|**CO**|
|**Combustible**|**[Nm3/h]**|**[mg/Nm3]**|**[mg/Nm3]**|**[mg/Nm3]**|**[kg/h]**|**[kg/h]**|**[kg/h]**|
|Biomasa 100%|76668|20|190,9|610|1,53|14,64|46,78|

Fuente: EISA

**Tabla 7-2: Características de la fuente**

|Parámetro|Valor|Unidad|
|---|---|---|
|Altura chimenea|20|m|
|Diámetro interno chimenea|1,57|m|
|Velocidad salida gases|20|m/s|
|Temperatura salida gases|140|°C|

Fuente: EISA

La Tabla 7-3 muestra los factores de emisión ingresados al modelo. Para la especiación de NOx se utilizó

de manera conservadora una razón de NO/NO 2 de 80/20. En el caso del material particulado (MP), al ser

este de combustión es considerado en un 100 % como MP2.5.

**Tabla 7-3: Factor de emisión ingresado al modelo**

|Factor de emisión|MP|NO|NO<br>2|CO|
|---|---|---|---|---|
|kg/h|1,530|11,712|2,928|46,780|
|g/s|0,425|3,253|0,813|12,994|

Fuente: Elaboración Propia

##### 8 RECEPTORES 8.1 Receptores discretos

Los receptores para evaluar corresponden a 3 receptores discretos. Las coordenadas de la totalidad de

los receptores de interés se presentan en la Tabla 8-1 y en las figuras de isoconcentraciones se presenta

la ubicación de cada uno de ellos. Los 3 receptores, Yerbas Buenas, Universidad Maule y La Florida

corresponden a estaciones de monitoreo.

45

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

**Tabla 8-1:** **Receptores de Interés definidos para la modelación**

|Receptor|Col2|Descripción|UTM - WGS84 -H19|Col5|
|---|---|---|---|---|
|**Receptor**|**Receptor**|**Descripción**|**X (m)**|**Y (m)**|
|1|R1|Yerbas Buenas|265.391|6.057.869|
|2|R2|U. Maule|262.216|6.075.477|
|3|R3|La Florida|256.889|6.075.395|

Fuente: Elaboración propia .

##### 8.2 Receptores grilla

Para la modelación de cada escenario se generó una grilla de receptores con una resolución espacial de

1.000 × 1.000 metros, resolución concordante con la resolución del modelo meteorológico, con una

extensión de 55 × 55 km. Finalmente, el área de modelación considerada y la grilla de receptores se

observan en la Figura 8-1. A partir de estos receptores se generan mapas de isoconcentraciones para

cada uno de los contaminantes analizados.

**Figura 8-1: Grilla de receptores**

Fuente: Elaboración propia.

46

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

##### 9 RESULTADOS

A continuación, se presentan los resultados del modelo de dispersión para la operación del Proyecto.

##### 9.1 Análisis de resultados de modelación

###### 9.1.1 Aporte modelado

A continuación, se presentan los aportes del escenario modelado, correspondiente a la fase de

operación, a la concentración en los receptores discretos, considerando los estadígrafos de las normas

de calidad aplicables MP10, MP2,5, NO 2 y CO. Cabe recordar que las emisiones de material particulado

generadas por combustión son consideradas como 100% MP2.5 por ende en este caso el MP10 es igual

al MP2.5. Se consideró el mecanismo RIVAD en el modelo Calpuff por lo tanto el MP considera la

formación de nitratos provenientes del NOx.

En la Tabla 9-1 se muestran los resultados del modelo de dispersión en los distintos receptores de interés

más el punto de máximo impacto (PMI), sin considerar el factor de corrección meteorológico. La Tabla

9-2 muestra los aportes en concentraciones con un factor de corrección de 1,89. Por último, la Tabla 9-3

muestra el aporte relativo de la operación del Proyecto a los respectivos estándares de calidad del aire.

En la Tabla 9-3 es posible verificar que los aportes del Proyecto en calidad del aire, según las

estimaciones del modelo, no superan el 1 % de las respectivas normas de material particulado ni gases,

en ninguno de los receptores de interés, con la excepción del NO 2 horario el cual alcanza un 7,5% y un

1,9% en Yerbas Buenas y U. Maule respectivamente.

Los puntos de máximo impacto se encuentran todos cercanos a las obras del Proyecto, alcanzando un

máximo relativo a la normativa menor a 8 % para el material particulado, correspondiente al MP2.5

diario y de 16,6 % para los gases, correspondiente al NO 2 horario, el cual es seguido por un valor mucho

más bajo de solo 4 % para el NO 2 anual. Para el resto de los gases el aporte del Proyecto es marginal, no

superando un 1,5 % en el punto de máximo impacto. El PMI está ubicado al nor-noreste del Proyecto en

todos los casos, excepto para el NO 2 anual donde está ubicado a 3 kilómetros al nor-noreste del

Proyecto.

47

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

**Tabla 9-1: Resultados del modelo para el aporte del proyecto en la fase de operación sin factor de corrección.**

|Contaminante|Tipo de Norma|μg/m3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|**Contaminante**|**Tipo de Norma**|**Yerbas Buenas**|**U. Maule**|**La Florida**|**PMI**|
|MP10|Primaria anual|0,010|0,003|0,001|0,210|
|MP10|Primaria diaria|0,110|0,031|0,013|0,770|
|MP2,5|Primaria anual|0,010|0,003|0,001|0,210|
|MP2,5|Primaria diaria|0,110|0,031|0,013|0,770|
|NO2|Primaria anual|0,084|0,027|0,008|2,120|
|NO2|Primaria horaria|15,831|4,077|1,060|35,100|
|CO|Primaria horaria|65,770|9,617|2,565|153,000|
|CO|Primario 8 horas|16,493|3,271|0,858|69,400|

Fuente: Elaboración propia.

**Tabla 9-2: Resultados del modelo para el aporte del proyecto en la fase de operación con factor de corrección.**

|Contaminante|Tipo de Norma|μg/m3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|**Contaminante**|**Tipo de Norma**|**Yerbas Buenas**|**U. Maule**|**La Florida**|**PMI**|
|MP10|Primaria anual|0,019|0,006|0,002|0,397|
|MP10|Primaria diaria|0,207|0,059|0,025|1,455|
|MP2,5|Primaria anual|0,019|0,006|0,002|0,397|
|MP2,5|Primaria diaria|0,207|0,059|0,025|1,455|
|NO2|Primaria anual|0,159|0,051|0,014|4,007|
|NO2|Primaria horaria|29,921|7,705|2,003|66,339|
|CO|Primaria horaria|124,305|18,175|4,847|289,170|
|CO|Primario 8 horas|31,172|6,183|1,621|131,166|

Fuente: Elaboración propia.

**Tabla 9-3: Resultados del modelo para el aporte del proyecto en la fase de operación con factor de corrección.**

|Contaminante|Tipo de Norma|Yerbas Buenas|U. Maule|La Florida|PMI|
|---|---|---|---|---|---|
|MP10|Primaria anual|0,04%|0,01%|0,00%|0,79%|
|MP10|Primaria diaria|0,14%|0,04%|0,02%|0,97%|
|MP2,5|Primaria anual|0,09%|0,03%|0,01%|1,98%|
|MP2,5|Primaria diaria|0,41%|0,12%|0,05%|2,91%|
|NO2|Primaria anual|0,16%|0,05%|0,01%|4,01%|
|NO2|Primaria horaria|7,48%|1,93%|0,50%|16,58%|
|CO|Primaria horaria|0,41%|0,06%|0,02%|0,96%|
|CO|Primario 8 horas|0,31%|0,06%|0,02%|1,31%|

Fuente: Elaboración propia.

48

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

###### 9.1.2 Concentraciones totales

A continuación, se presentan las concentraciones totales para la fase de operación del Proyecto. Para

estimar las concentraciones totales proyectadas para dicha fase, es utilizada la metodología indicada en

la sección 3 del presente documento, y que se detalla a continuación.

Con los resultados de la modelación se determinará los aportes de éstos en la calidad del aire. La calidad

del aire proyectada para la fase de operación del Proyecto será estimada de acuerdo con la siguiente

ecuación.

**CA_Op = LDB +AP_O+ AP_Op**

En donde:

**CA_Op** : corresponde a la calidad del aire proyectada para la fase de operación del Proyecto.

**LDB** : corresponde a la línea base de calidad del aire medida en el área de estudio.

**AP_O:** corresponde al aporte de otros proyectos con RCA que aun no estén ejecución, en esta evaluación

se considera el aporte estimado en la DIA “Planta Cogeneración Cartulinas CMPC”.

**AP_Op** : corresponde al aporte en la calidad del aire de la fase de operación del Proyecto.

Para las tres variables mencionadas se estima el respectivo valor porcentual relativo a la norma de

calidad del aire correspondiente.

Los valores mencionados anteriormente se muestran en la Tabla 9-4, Tabla 9-5 y la Tabla 9-6 para las

estaciones Yerbas Buenas, U. Maule y La Florida, respectivamente.

Respecto a las concentraciones totales proyectadas, se constata superación de normas por

concentraciones basales de MP2.5 diario en la estación U. Maule y por MP2.5 anual y diario en la

estación Florida. Los aportes a las concentraciones ambientales de MP2.5 del Proyecto en estas dos

estaciones es despreciable, como se puede apreciar en la Tabla 9-5 y la Tabla 9-6, por lo tanto, no existe

un cambio en la situación basal. Los mayores aportes del Proyecto se generarían en la estación Yerbas

Buenas, donde solo el aporte en NO 2 horario supera el 1 % de la norma, sin embargo, se puede apreciar

que la concentración total de NO 2 horario proyectado en esta estación no supera el 30 % de la respectiva

norma de calidad del aire.

49

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

**Tabla 9-4: Concentraciones totales Proyecto en estación Yerbas Buenas**

|Contaminante|Tipo de Norma|LDB<br>[μg/m3]|% LDB_N|AP_O*<br>[μg/m3]|Aporte Proy.<br>[μg/m3]|%AP_N|Total<br>[μg/m3]|%Total_N|Norma<br>[μg/m3]|
|---|---|---|---|---|---|---|---|---|---|
|MP10|Primaria anual|25,69|51,4%|1,43|0,02|0,0%|27,14|54,3%|50|
|MP10|Primaria diaria|66,74|44,5%|4,54|0,21|0,1%|71,49|47,7%|150|
|MP2,5|Primaria anual|14,76|73,8%|1,20|0,02|0,1%|15,98|79,9%|20|
|MP2,5|Primaria diaria|45,78|91,6%|3,83|0,21|0,4%|49,82|99,6%|50|
|NO2|Primaria anual|8,43|8,4%|2,09|0,16|0,2%|10,68|10,7%|100|
|NO2|Primaria horaria|82,80|20,7%|32,86|29,92|7,5%|145,58|36,4%|400|
|CO|Primaria horaria|1400,00|4,7%|24,65|124,31|0,4%|1548,96|5,2%|30.000|
|CO|Primario 8 horas|606,77|6,1%|12,37|31,17|0,3%|650,31|6,5%|10.000|

*se considera aporte estimado en DIA “Planta Cogeneración Cartulinas CMPC” para la fase de operación proyectada en el receptor Estación Bobadilla, el cual se encuentra a 1 kilometro al Este de

Estación Yerbas Buenas.

Fuente: Elaboración propia.

**Tabla 9-5: Concentraciones totales Proyecto, en estación U. Maule.**

|Contaminante|Tipo de Norma|LDB<br>[μg/m3]|% LDB_N|AP_Op<br>[μg/m3]|% AP_Op_N|CA_Op<br>[μg/m3]|% CA_Op _N|Norma<br>[μg/m3]|
|---|---|---|---|---|---|---|---|---|
|MP10|Primaria anual|41,67|83,3%|0,01|0,0%|41,68|83,4%|50|
|MP10|Primaria diaria|86,88|57,9%|0,06|0,0%|86,93|58,0%|150|
|MP2,5|Primaria anual|19,72|98,6%|0,01|0,0%|19,72|98,6%|20|
|MP2,5|Primaria diaria|62,92|125,8%|0,06|0,1%|62,98|126,0%|50|

Fuente: Elaboración propia.

**Tabla 9-6: Concentraciones totales Proyecto, en estación Florida.**

|Contaminante|Tipo de Norma|LDB<br>[μg/m3]|% LDB_N|AP_Op<br>[μg/m3]|% AP_Op_N|CA_Op<br>[μg/m3]|% CA_Op _N|Norma<br>[μg/m3]|
|---|---|---|---|---|---|---|---|---|
|MP10|Primaria anual|39,74|79,5%|0,00|0,0%|39,75|79,5%|50|
|MP10|Primaria diaria|113,29|75,5%|0,03|0,0%|113,32|75,5%|150|
|MP2,5|Primaria anual|23,87|119,3%|0,00|0,0%|23,87|119,3%|20|
|MP2,5|Primaria diaria|94,67|189,3%|0,03|0,1%|94,69|189,4%|50|

50

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

|NO<br>2|Primaria anual|16,17|16,2%|0,01|0,0%|16,19|16,2%|100|
|---|---|---|---|---|---|---|---|---|
|NO2|Primaria horaria|66,03|16,5%|2,00|0,5%|68,03|17,0%|400|
|CO|Primaria horaria|10971,00|36,6%|4,85|0,0%|10975,85|36,6%|30.000|
|CO|Primario 8 horas|6739,00|67,4%|1,62|0,0%|6740,62|67,4%|10.000|

Fuente: Elaboración propia.

51

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

##### 9.2 Mapas de gradientes espaciales de concentración (isoconcentraciones)

A continuación, se presentan las curvas de isoconcentración por contaminante del aporte de la fase de

operación del Proyecto.

El valor estimado del punto de máxima concentración se indica en rojo en cada uno de los mapas, cabe

destacar que se han omitido los mapas de CO de 1 hora y CO de 8 horas; principalmente porque

presentan valores de concentración muy bajos, encontrándose su Punto de Máximo Impacto (PMI) por

debajo o muy cercano 1% de su respectiva norma. Como las concentraciones en general son muy bajas,

en la mayoría de los mapas no se ha utilizado el usual 1% de las normas respectivas como umbral de

significancia, sino que se ha utilizado como umbral de corte un 0,5% de la norma en todos los mapas

para poder visualizar de mejor manera la pluma de dispersión, excepto para el NO 2 horario donde se

utilizó un 1% de umbral de corte. Sin embargo, para el MP2.5 diario y para el NO 2 anual se agrega un

segundo mapa con un acercamiento al proyecto y considerando un umbral de un 1% de las respectivas

normas. La Figura 9-3 muestra el área de influencia del Proyecto por emisiones de MP2.5, el cual es el

contaminante de mayor interés en la zona, esto considerando los valores basales registrados tanto en

Yerbas Buenas como en las estaciones de calidad del aire localizadas en Talca.

52

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

**Figura 9-1: Isoconcentraciones Fase de operación: MP2.5 Anual**

 - Umbral de corte 0,5% norma

Fuente: Elaboración propia

53

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

**Figura 9-2: Isoconcentraciones Fase de operación: MP2.5 diario**

 - Umbral de corte 0,5 % norma

Fuente: Elaboración propia

54

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

**Figura 9-3: Isoconcentraciones Fase de operación: MP2.5 diario, acercamiento a Proyecto**

 - Umbral de corte 1% norma

Fuente: Elaboración propia

55

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

**Figura 9-4: Isoconcentraciones fase de operación: NO** **2** **anual**

 - Umbral de corte 0,5% norma

Fuente: Elaboración propia

56

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

**Figura 9-5: Isoconcentraciones Fase de operación: NO** **2** **anual, acercamiento a Proyecto**

 - Umbral de corte 1% norma

Fuente: Elaboración propia

57

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

**Figura 9-6: Isoconcentraciones fase de operación: NO** **2** **horario (umbral de corte 1% norma)**

Fuente: Elaboración propia

58

Anexo 4.b

Modelación de dispersión de contaminantes fase de operación
DIA Incorporación Caldera N°5 en Planta de Generación de Vapor EISA

##### 10 CONCLUSIONES MODELO DE CALIDAD DEL AIRE

Se realizó la modelación de un escenario correspondiente a la fase de operación del Proyecto. De los

resultados obtenidos para dicha fase, se concluye que:

 Respecto al cumplimiento de normativa en los receptores con registros de mediciones de calidad

del aire:

Las concentraciones totales proyectadas muestran que los aportes en concentraciones de la Caldera 5 no

cambian la situación basal de la calidad del aire en ninguno de los tres receptores evaluados.

Cabe destacar que en todos los casos y para todos los contaminantes evaluados, los aportes son de poca

relevancia, superando muy levemente el 1 % de las normas solo para el NO 2 horario en las estaciones de

calidad del aire Yerbas Buenas y U. Maule.

 Respecto al Punto de Máximo Impacto:

En las figuras se puede ver que los puntos de máximo impacto están ubicados a 800 metros al nor
noreste del Proyecto en todos los casos, excepto para el NO 2 anual donde está ubicado a 3 kilómetros

también al nor-noreste del Proyecto.

En conclusión, el Proyecto no altera la situación de la calidad del aire de la zona.

59

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 5-4.: Coordenadas estaciones meteorológicas****

| Col1 | WGS84-Huso 19 | Col3 |
| --- | --- | --- |
| **Estación** | **UTM - E (m)** | **UTM - N (m)** |
| Yerbas Buenas | 265.391 | 6.057.869 |
| Universidad Maule | 262.216 | 6.075.477 |
| La Florida | 256.889 | 6.075.395 |
