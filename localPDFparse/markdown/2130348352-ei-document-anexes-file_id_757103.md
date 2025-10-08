---
title: CAPÍTULO 1
author: Jorge
date: D:20150313195600-03'00'
language: es
type: report
pages: 104
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - INFORME MODELAMIENTO DE LA DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS
-->

# INFORME MODELAMIENTO DE LA DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS

## PROYECTO EXTRACCIÓN Y PROCESAMIENTO DE ÁRIDOS SECTOR AGUADA DE LA TECA

Febrero - 2015

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 1

## INDICE DE MATERIAS

1. INTRODUCCIÓN .............................................................................................................................. 7
2. DESCRIPCIÓN Y JUSTIFICACIÓN DEL MODELO ........................................................................ 9
3. ESCENARIO METEOROLÓGICO ................................................................................................. 10

3.1 Datos Observados ................................................................................................................ 18

3.2 Series de Tiempo. ................................................................................................................ 20
3.3 Campos de Viento ................................................................................................................ 21
4. BASES DE DATOS Y ARCHIVOS DE MODELACIÓN .................................................................. 23

4.1 Archivos de Entrada y Salida de la Modelación ................................................................... 23
5. CARACTERÍSTICAS DEL DOMINIO DE MODELACIÓN Y SU ENTORNO ................................. 24

5.1 Localización .......................................................................................................................... 24
5.2 Área de Modelamiento ......................................................................................................... 25

5.3 Grilla de Modelamiento ........................................................................................................ 26
5.4 Topografía del Área de Modelamiento ................................................................................. 27
5.5 Receptores en el Área de Modelamiento ............................................................................. 28
5.6 Suelos del Área de Modelamiento ....................................................................................... 29
6. FUENTES DE EMISIÓN ................................................................................................................. 30

6.1 Actividades Emisoras ........................................................................................................... 30

6.2 Metodología para la Estimación de Emisiones .................................................................... 33
6.2.1 Metodología para la estimación de emisiones de las actividades ............................. 34
6.2.2 Metodología para la estimación de emisiones de maquinarias ................................. 34
6.2.3 Metodología para la estimación de emisiones de vehículos ..................................... 35
6.2.4 Metodología para la estimación de emisiones por combustión en generadores ....... 37
7. FACTORES DE EMISIÓN .............................................................................................................. 38

7.1 Factores de Emisión para Material Particulado Resuspendido ........................................... 38
7.2 Factores de Emisión para la Estimación de Emisin de Gases y Material Particulado. ........ 42

8. NIVELES DE ACTIVIDAD .............................................................................................................. 43
9. MEDIDAS DE MITIGACIÓN CAMINOS ......................................................................................... 46

10. RESULTADOS INVENTARIO DE EMISIONES ............................................................................. 46
11. RESULTADOS DE LA MODELACIÓN ........................................................................................... 55

11.1 Resultados del Modelo ......................................................................................................... 55

11.1.1 Cumplimiento Normas De Calidad Ambiental Primaria ............................................. 55
11.1.2 Cumplimiento Normas De Calidad Ambiental Secundaria ....................................... 58
12. ANÁLISIS DE INCERTIDUMBRE .................................................................................................. 60

12.1 Análisis Cualitativo de los Campos de Vientos ...................................................................... 60
12.2 Análisis Cuantitativo para el Cálculo de Incertidumbre .......................................................... 60
13. ANÁLISIS DE CUMPLIMIENTO NORMATIVO VIGENTE ............................................................. 61

14. CONCLUSIONES ........................................................................................................................... 65

15. MAPAS DE ISOCONCENTRACIONES ......................................................................................... 65

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 2

## INDICE DE TABLAS

Tabla 1: Normas de Calidad Ambiental Primarias y Secundarias ....................................................... 8

<!-- INICIO TABLA 1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- siguiente: Informe de Emisiones Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 7 -->

**Tabla 1: Normas de Calidad Ambiental Primarias y Secundarias****

| Parámetro | Unidad Estadística | Límite Máximo<br>Permitido | Referencia Legal |
| --- | --- | --- | --- |
| MP 10 | Promedio Anual1 | 50 (μg/m3N) | NP DS 20/2013 |
| MP 10 | Percentil 98 Promedio 24 horas2 | 150 (μg/m3N) | NP DS 20/2013 |
| MP 2.5 | Promedio Trianual3 | 20 (μg/m3N) | NP DS 12/2011 |
| MP 2.5 | Percentil 98 Promedio Diario4 | 50 (μg/m3N) | NP DS 12/2011 |
| MPS | Promedio Mensual | 150 mg/m2dia | NS DE 4/1992 |
| MPS | Promedio Anual | 100 mg/m2dia | NS DE 4/1992 |
| SO2 | Promedio Anual5 | 80 (μg/m3N) | NP DS 113/2002 |
| SO2 | Promedio Diario, percentil 996 | 250 (μg/m3N) | NP DS 113/2002 |
| SO2 | Promedio Anual7 | 80 (μg/m3N) | NS DS 185/1991 |
| SO2 | Percentil 99.7 Concentración Diaria8 | 365 (μg/m3N) | NS DS 185/1991 |
| SO2 | Percentil 99.73 Concentración 1 hora9 | 1000 (μg/m3N) | NS DS 185/1991 |
| NO2 | Promedio Anual10 | 100 (μg/m3N) | NP DS 114/2002 |
| NO2 | Percentil 99, máx. 1 hora11 | 400 (μg/m3N) | NP DS 114/2002 |

<!-- Estadísticas: 13 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- 1 Promedio Anual: se refiere a la concentración promedio anual. Se considera sobrepasada la norma cuando la concentración anual calculada como promedio aritmético de tres años calendario consecutivos, sea mayor o igual a lo indicado a la tabla. -->
<!-- FIN TABLA 1 -->


Tabla 2: Información de la Orden de los Datos WRF ........................................................................ 10

Tabla 3: Información general de la Estación Meteorológica .............................................................. 19
Tabla 4: Línea de Base de MP y Gases - Estación Centro................................................................ 19

<!-- INICIO TABLA 4 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Se ha considerado en el presente análisis la información disponible registrada en la Estación Central, entre el 1° de enero de 2013 al 31 de diciembre de 2013, la que será comparada con la información utilizada para el modelamiento y que corresponde al modelo meteorológicos de pronóstico WRF (correspondiente al mismo período) -->

**Tabla 4: Línea de Base de MP y Gases - Estación Centro****

| Contaminante | Tipo de<br>Norma | Estadístico | Valor<br>(μg/m3N | Norma | %<br>Norma |
| --- | --- | --- | --- | --- | --- |
| MP10 | Primaria | Promedio del período<br>Percentil 98 diario | 41.9<br>44.3 | 50<br>150 | 83.1<br>29.5 |
| MP2,5 | Primaria | Promedio del período<br>Percentil 98 diario | 12.18<br>14.3 | 20<br>50 | 60.9<br>28.6 |
| SO2 | Primaria | Promedio del período<br>Percentil 99 diario | 4.8<br>4.5 | 80<br>250 | 6 <br>1.8 |
| NO2 | Primaria | Promedio del período<br>Percentil 99 horario | 19.5<br>19.5 | 100<br>400 | 19.5<br>4.9 |
| CO | Primaria | Percentil 99 en 8 horas<br>Percentil 99 horario | 372.1<br>372.1 | 10000<br>30000 | 3.7<br>1.2 |

<!-- Estadísticas: 5 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- 14 Fuente de Información: página web http://sinca.mma.gob.cl Informe de Emisiones Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 19 -->
<!-- FIN TABLA 4 -->


Tabla 5: Información Para el Modelamiento....................................................................................... 23

Tabla 6: Archivos de Entrada y Salida de la Modelación, .................................................................. 23

<!-- INICIO TABLA 6 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **4.1 Archivos de Entrada y Salida de la Modelación** Los archivos de entrada y salida de la modelación, para cada etapa del proyecto y que se anexan en forma digital (DVD), son los siguientes: -->

**Tabla 6: Archivos de Entrada y Salida de la Modelación,****

| CALMET | GEO.DAT<br>CALMET.DAT<br>CALMET.LST<br>CALMET.INP |
| --- | --- |
| CALPUF | CALPUFF.LST<br>CALPUFF.INP<br>CONS.INP |
| CALPOST | CALPOST.DAT<br>CALPOST.LST<br>CALPOST.INP |
| ARCHIVOS<br>COMPLEMENTARIOS | Dry Flux Data File<br>Wet Flux Data |

<!-- Estadísticas: 3 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Informe de Emisiones Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 23 **5. CARACTERÍSTICAS DEL DOMINIO DE MODELACIÓN Y SU ENTORNO** -->
<!-- FIN TABLA 6 -->

Tabla 7: Ubicación Receptores Humanos .......................................................................................... 28

<!-- INICIO TABLA 7 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Calama, San Pedro de Atacama y Chiu-Chiu. El siguiente cuadro presenta las coordenadas UTM en Datum WGS-84 Huso 19, de las habitaciones más cercaba al área del proyecto en cada una de las localidades señaladas: -->

**Tabla 7: Ubicación Receptores Humanos****

| Localidad | Este | Norte |
| --- | --- | --- |
| Calama<br>San Pedro de Atacama<br>Chiu-Chiu | 510069<br>581754<br>535607 | 7513907<br>7467110<br>7526387 |

<!-- Estadísticas: 1 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- **Figura 22: Ubicación del Receptor** Debido a que no se han identificado receptores biológicos, dentro del área de modelamiento, se consideraran los mismos puntos señalados en la tabla anterior, como receptores -->
<!-- FIN TABLA 7 -->

Tabla 8: Actividad Generadora de Emisiones - Etapa de Construcción ............................................ 30

<!-- INICIO TABLA 8 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- La siguiente tabla, presenta las actividades del proyecto generadoras de emisiones atmosféricas -->

**Tabla 8: Actividad Generadora de Emisiones - Etapa de Construcción****

| Etapa del<br>Proyecto | Actividad Generadora de Emisiones | Col3 | Tipo de<br>Contaminante |
| --- | --- | --- | --- |
| Etapa del<br>Proyecto | Actividad | Descripción Datos | Descripción Datos |
| Etapa de<br>Construcción | **Escarpado área Instalación**<br>**Campamento**(preparación de terreno) | Área Total: 400 m2<br>Duración: 90 días | MP10 <br>MP2.5 <br>MPS |
| Etapa de<br>Construcción | **Escarpado área Instalación Planta de**<br>**Chancado y Selección de Materiales**<br>(preparación de terreno) | Área Total: 2.500 m2<br>Duración: 90 días | Área Total: 2.500 m2<br>Duración: 90 días |
| Etapa de<br>Construcción | **Tránsito de Vehículos por Caminos**<br>**Pavimentados**(viajes/día) | Longitud Total (50 km)<br>Duración (días) | Longitud Total (50 km)<br>Duración (días) |
| Etapa de<br>Construcción | - Transporte Equipos Planta: 1 | 1 | 1 |
| Etapa de<br>Construcción | - Transporte Estructura Pesada: 3 | 1 | 1 |
| Etapa de<br>Construcción | - Camión Grúa para montaje e instalación: 1 | 1 | 1 |
| Etapa de<br>Construcción | - Transporte Petróleo: 1 | 12 | 12 |
| Etapa de<br>Construcción | - Transporte Agua Potable: 1 | 12 | 12 |
| Etapa de<br>Construcción | - Transporte Personal y Supervisión: 2 | 90 | 90 |
| Etapa de<br>Construcción | **Tránsito de Vehículos Livianos por**<br>**Caminos No Pavimentados**(viajes/día)<br>- Transporte de Personal y Supervisión: 2 | Longitud Total (1,5 km)<br>Duración (días)<br>2 | Longitud Total (1,5 km)<br>Duración (días)<br>2 |
| Etapa de<br>Construcción | **Tránsito de Vehículos Pesados por**<br>**Caminos No Pavimentados**(viajes/día) | Longitud Total (1,5 km)<br>Duración (días) | Longitud Total (1,5 km)<br>Duración (días) |
| Etapa de<br>Construcción | - Transporte Equipos Planta: 1 | 1 | 1 |
| Etapa de<br>Construcción | - Transporte Estructura Pesada: 3 | 1 | 1 |

<!-- Estadísticas: 14 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Informe de Emisiones Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 30 |Etapa de<br>Construcción|- Camión Grúa para montaje e instalación: 1|1|MP<br>10<br>MP<br>2.5<br>MPS| -->
<!-- FIN TABLA 8 -->

Tabla 9: Actividad Generadora de Emisiones - Etapa de Operación ................................................ 31

<!-- INICIO TABLA 9 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Etapa de<br>Construcción|- Transporte Petróleo: 1|12|12| |Etapa de<br>Construcción|- Transporte Agua Potable: 1|12|12| |Etapa de<br>Construcción|**Emisiones de Gases** de Combustión de maquinarias y vehículos|**Emisiones de Gases** de Combustión de maquinarias y vehículos|CO, HC,<br>NOx, CC, y MP| |Etapa de<br>Construcción|**Emisiones de Gases** de Equipos Generadores|**Emisiones de Gases** de Equipos Generadores|CO, NOx, MP10, y<br>SOx| -->

**Tabla 9: Actividad Generadora de Emisiones - Etapa de Operación****

| Etapa del<br>proyecto | Actividad Generadora de Emisiones | Col3 | Tipo de<br>Contaminante |
| --- | --- | --- | --- |
| Etapa del<br>proyecto | Actividad | Descripción datos | Descripción datos |
| Etapa de<br>Operación | **Excavación Área 1 y 2**<br>**(**Extracción de áridos) | Área Total: 14.183 ha<br>Duración: 2.190 días | MP10 <br>MP2.5 <br>MPS |
| Etapa de<br>Operación | **Transferencia de Material**<br>(Carga y descarga de áridos en acopio<br>intermedio) | Área: 100 m2<br>Duración: 2.190 días | Área: 100 m2<br>Duración: 2.190 días |
| Etapa de<br>Operación | **Transferencia de Material**<br>(Carga y descarga de áridos en buzón<br>alimentación Planta) | Área: 100 m2<br>Duración: 2.190 días | Área: 100 m2<br>Duración: 2.190 días |
| Etapa de<br>Operación | **Tránsito de Vehículos por Caminos**<br>**Pavimentados**(viajes/día) | <br>Longitud Total (50 km)<br>Duración (días) | <br>Longitud Total (50 km)<br>Duración (días) |
| Etapa de<br>Operación | - Transporte Petróleo: 1 | 2190 | 2190 |
| Etapa de<br>Operación | - Transporte Agua Potable: 1 | 312 | 312 |
| Etapa de<br>Operación | - Transporte de Residuos Varios: 1 | 312 | 312 |
| Etapa de<br>Operación | - Transporte Personal y Supervisión: 2 | 2190 | 2190 |
| Etapa de<br>Operación | **Tránsito de Vehículos Livianos por**<br>**Caminos No Pavimentados (**viajes/día) <br>- Transporte de personal y Supervisión: 2 | Longitud Total (1,5 km)<br>Duración (días)<br>2190 | Longitud Total (1,5 km)<br>Duración (días)<br>2190 |
| Etapa de<br>Operación | **Tránsito de Vehículos Pesados por**<br>**Caminos No Pavimentados**(viajes/día) <br>- Transporte interno de áridos a la planta: 55 | Longitud Total (0,6 km)<br>Duración (días)<br>2190 | Longitud Total (0,6 km)<br>Duración (días)<br>2190 |
| Etapa de<br>Operación | **Tránsito de Vehículos Pesados por**<br>**Caminos No Pavimentados**(viajes/día) | Longitud Total (1,5 km)<br>Duración (días) | Longitud Total (1,5 km)<br>Duración (días) |
| Etapa de<br>Operación | - Transporte Petróleo: 1 | 2190 | 2190 |
| Etapa de<br>Operación | - Transporte Agua Potable: 1 | 312 | 312 |
| Etapa de<br>Operación | - Transporte de Residuos Varios: 1 | 312 | 312 |

<!-- Estadísticas: 15 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Informe de Emisiones Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 31 |Etapa de<br>Operación|Proceso Chancado<br>(Emisiones del proceso de trituración)|Cantidad de equipos:1<br>Área: 5,25 m2<br>Total: 1.643,84 ton/día<br>Duración: 2.190 días|MP<br>10<br>MP<br>2.5<br>MPS| -->
<!-- FIN TABLA 9 -->

Tabla 10: Actividad Generadora de Emisiones - Etapa de Cierre ...................................................... 33

<!-- INICIO TABLA 10 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Etapa de<br>Operación|**Emisiones de Gases** por Combustión en Equipos Generadores|**Emisiones de Gases** por Combustión en Equipos Generadores|CO, NOx,<br>MPS, MP10, <br>MP2.5, SOx, COV| Informe de Emisiones Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 32 -->

**Tabla 10: Actividad Generadora de Emisiones - Etapa de Cierre****

| Etapa del<br>proyecto | Actividad Generadora de Emisiones | Col3 | Tipo de<br>Contaminante |
| --- | --- | --- | --- |
| Etapa del<br>proyecto | Actividad | Descripción datos | Descripción datos |
| Etapa de<br>Cierre | **Escarpado**<br>- Reperfilamiento área Planta<br>- Reperfilamiento Camino | Área de Reperfilamiento:<br>Planta: 25.000 m2<br>Camino: 10.500 m3<br>Duración: 90 días | MP10 <br>MP2.5 <br>MPS |
| Etapa de<br>Cierre | **Tránsito de Vehículos por Caminos**<br>**Pavimentados**(viajes/día) <br>- Transporte Petróleo: 1<br>- Transito Equipos Planta: 1<br>- Transporte Estructura Pesada: 3<br>- Transporte Camión Grúa: 1<br>- Transporte Agua Potable: 1<br>- Transporte Personal y Supervisión: 2 | Longitud de camino: 50 km<br>Duración: 90 días | Longitud de camino: 50 km<br>Duración: 90 días |
| Etapa de<br>Cierre | **Tránsito de Vehículos Livianos por**<br>**Caminos No Pavimentados**<br>(viajes/día) <br>- Transporte Personal y Supervisión: 2 | Longitud de camino: 1.5 km<br>Duración: 90 días | Longitud de camino: 1.5 km<br>Duración: 90 días |
| Etapa de<br>Cierre | **Tránsito de Vehículos Pesados por**<br>**Caminos No Pavimentados**<br>(viajes/día) <br>- Transporte Petróleo: 1<br>- Transito Equipos Planta: 1<br>- Transporte Estructura Pesada: 3<br>- Transporte Camión Grúa: 1<br>- Transporte Agua Potable: 1 | Longitud de camino: 1.5 km<br>Duración: 90 días | Longitud de camino: 1.5 km<br>Duración: 90 días |
| Etapa de<br>Cierre | **Emisiones de Gases** de Combustión de maquinarias y vehículos | **Emisiones de Gases** de Combustión de maquinarias y vehículos | CO, HC,<br>NOx, y MPS, MP10, <br>MP2.5 |
| Etapa de<br>Cierre | **Emisiones de Gases** de Equipos Generadores | **Emisiones de Gases** de Equipos Generadores | CO, NOx,<br>MPS, MP10, MP2.5, <br>SOx, COV |

<!-- Estadísticas: 7 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- **6.2 Metodología para la Estimación de Emisiones** La ecuación general para estimar las emisiones de cualquier actividad, es la siguiente: -->
<!-- FIN TABLA 10 -->

Tabla 11: Maquinarias Utilizados en Etapa de Construcción ............................................................... 35

<!-- INICIO TABLA 11 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- P: Potencia Nominal (kw) Informe de Emisiones Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 34 -->

**Tabla 11: Maquinarias Utilizados en Etapa de Construcción****

| Equipo | Cantidad | Potencia<br>Nominal kw | Operación<br>Diaria (horas) |
| --- | --- | --- | --- |
| Excavadora 1.5 m3 | 1 | 120 | 12 |
| Cargador Frontal W190B | 1 | 160 | 12 |
| Cargador Frontal 721 E | 1 | 160 | 12 |

<!-- Estadísticas: 3 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 13: Maquinarias Utilizados en Etapa de Cierre** |Equipo|Cantidad|Potencia<br>Nominal kw|Operación<br>Diaria (horas)| |---|---|---|---| -->
<!-- FIN TABLA 11 -->

Tabla 12: Maquinarias Utilizados en Etapa de Operación ................................................................... 35
Tabla 13: Maquinarias Utilizados en Etapa de Cierre .......................................................................... 35

<!-- INICIO TABLA 13 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |---|---|---|---| |Excavadora 1.5 m3|1|120|12| |Cargador Frontal W190B|1|160|12| |Cargador Frontal 721 E|1|160|12| -->

**Tabla 13: Maquinarias Utilizados en Etapa de Cierre****

| Equipo | Cantidad | Potencia<br>Nominal kw | Operación<br>Diaria (horas) |
| --- | --- | --- | --- |
| Motoniveladora | 1 | 137 | 12 |

<!-- Estadísticas: 1 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- **6.2.3 Metodología para la estimación de emisiones de vehículos** La metodología utilizada para determinar las emisiones de material particulado de combustión y gases de la flota de vehículos, en cada una de las etapas del proyecto, -->
<!-- FIN TABLA 13 -->

Tabla 14: Vehículos Utilizados en Etapa de Construcción .................................................................. 36

<!-- INICIO TABLA 14 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- decreto lo establezca. El nivel de actividad (Na) corresponde a la cantidad de kilómetros que circula cada vehículo. -->

**Tabla 14: Vehículos Utilizados en Etapa de Construcción****

| Vehículo | Categoría | N°<br>Viajes/día | Distancia<br>(km) | Velocidad km/h |
| --- | --- | --- | --- | --- |
| Camión Transporte Petróleo | Pesado Diésel Tipo 3 | 1 | 51.5 | 100 |
| Camión Transporte Equipos Planta | Pesado Diésel Tipo 3 | 1 | 51.5 | 100 |
| Camión Transporte Estructura<br>Pesada | Pesado Diésel Tipo 3 | 3 | 51.5 | 100 |
| Camión Grúa | Pesado Diésel Tipo 3 | 1 | 51.5 | 100 |
| Camión Transporte Agua Potable | Pesado Diésel Tipo 3 | 1 | 51.5 | 100 |
| Camionetas Transporte Personal y<br>Supervisión | Comerciales Diésel Tipo 2 | 2 | 51.5 | 100 |

<!-- Estadísticas: 6 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 15: Vehículos Utilizados en Etapa de Operación** |Vehículo|Categoría|N°<br>Viajes/día|Distancia<br>(km)|Velocidad km/h| |---|---|---|---|---| -->
<!-- FIN TABLA 14 -->

Tabla 15: Vehículos Utilizados en Etapa de Operación ....................................................................... 36

<!-- INICIO TABLA 15 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Camión Transporte Estructura<br>Pesada|Pesado Diésel Tipo 3|3|51.5|100| |Camión Grúa|Pesado Diésel Tipo 3|1|51.5|100| |Camión Transporte Agua Potable|Pesado Diésel Tipo 3|1|51.5|100| |Camionetas Transporte Personal y<br>Supervisión|Comerciales Diésel Tipo 2|2|51.5|100| -->

**Tabla 15: Vehículos Utilizados en Etapa de Operación****

| Vehículo | Categoría | N°<br>Viajes/día | Distancia<br>(km) | Velocidad km/h |
| --- | --- | --- | --- | --- |
| Camión Transporte Áridos | Pesado Diésel Tipo 3 | 55 | 0.6 | 50 |
| Camión Transporte Petróleo | Pesado Diésel Tipo 3 | 1 | 51.5 | 100 |
| Camión Transporte Agua Potable | Pesado Diésel Tipo 3 | 1 | 51.5 | 100 |
| Camión Transporte Residuos Varios | Pesado Diésel Tipo 3 | 1 | 51.5 | 100 |
| Camionetas Transporte Personal y<br>Supervisión | Comerciales Diésel Tipo 2 | 2 | 51.5 | 100 |

<!-- Estadísticas: 5 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 16: Vehículos Utilizados en Etapa de Cierre** |Vehículo|Categoría|N°<br>Viajes/día|Distancia<br>(km)|Velocidad km/h| |---|---|---|---|---| -->
<!-- FIN TABLA 15 -->

Tabla 16: Vehículos Utilizados en Etapa de Cierre .............................................................................. 36

<!-- INICIO TABLA 16 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Camión Transporte Petróleo|Pesado Diésel Tipo 3|1|51.5|100| |Camión Transporte Agua Potable|Pesado Diésel Tipo 3|1|51.5|100| |Camión Transporte Residuos Varios|Pesado Diésel Tipo 3|1|51.5|100| |Camionetas Transporte Personal y<br>Supervisión|Comerciales Diésel Tipo 2|2|51.5|100| -->

**Tabla 16: Vehículos Utilizados en Etapa de Cierre****

| Vehículo | Categoría | N°<br>Viajes/día | Distancia<br>(km) | Velocidad km/h |
| --- | --- | --- | --- | --- |
| Camión Transporte Petróleo | Pesado Diésel Tipo 3 | 1 | 51.5 | 100 |
| Camión Transporte Estructura<br>Pesada | Pesado Diésel Tipo 3 | 3 | 51.5 | 100 |
| Camión Transporte Equipos Planta | Pesado Diésel Tipo 3 | 1 | 51.5 | 100 |
| Camión Grúa | Pesado Diésel Tipo 3 | 1 | 51.5 | 100 |
| Camión Transporte Agua Potable | Pesado Diésel Tipo 3 | 1 | 51.5 | 100 |
| Camionetas Transporte Personal y<br>Supervisión | Comerciales Diésel Tipo 2 | 2 | 51.5 | 100 |

<!-- Estadísticas: 6 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- Informe de Emisiones Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 36 **Tabla 17: Peso Promedio de la Flota** -->
<!-- FIN TABLA 16 -->


Tabla 17: Peso Promedio de la Flota ................................................................................................... 37

<!-- INICIO TABLA 17 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Camionetas Transporte Personal y<br>Supervisión|Comerciales Diésel Tipo 2|2|51.5|100| Informe de Emisiones Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 36 -->

**Tabla 17: Peso Promedio de la Flota****

| Vehículos | Capacidad de<br>carga (ton) | Peso Vacío<br>(ton) | Peso<br>Cargado<br>(ton) | Peso<br>Promedio) |
| --- | --- | --- | --- | --- |
| Camión Transporte de Áridos | 30 | 19 | 49 | 34 |
| Camión Transporte Estructura Pesada | 30 | 19 | 49 | 34 |
| Camión Transporte Equipos Planta | 30 | 19 | 49 | 34 |
| Camión Grúa | 30 | 19 | 49 | 34 |
| Camión Transporte de Petróleo | 30 | 19 | 49 | 34 |
| Camión Transporte de Residuos varios | 30 | 19 | 49 | 34 |
| Camión Agua | 30 | 19 | 49 | 34 |
| Camionetas Transporte de Supervisión | 0.15 | 2.5 | 2.65 | 2.58 |

<!-- Estadísticas: 8 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- **6.2.4 Metodología para la estimación de emisiones por combustión en generadores** **eléctricos** -->
<!-- FIN TABLA 17 -->


Tabla 18: Generadores ......................................................................................................................... 37

<!-- INICIO TABLA 18 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Internal Combustion Sources), tablas 3.4-1 y 3.4-2. El porcentaje de azufre es de máximo 1% en el combustible de acuerdo al Decreto Supremo 132/2004 Ministerio de Minería Reglamento de Seguridad Minera Artículo 131, para equipos de minería, incluido casas de fuerza. Por lo tanto S=1. -->

**Tabla 18: Generadores****

| Etapa Proyecto | Potencia (kw) por<br>Generador | Horas<br>Operación Día | Cantidad |
| --- | --- | --- | --- |
| Construcción | 480 | 12 | 1 |
| Operación | 480 | 12 | 1 |
| Cierre | 480 | 12 | 1 |

<!-- Estadísticas: 3 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Informe de Emisiones Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 37 **7. FACTORES DE EMISIÓN** -->
<!-- FIN TABLA 18 -->


Tabla 19: Factor de Emisión Escarpes ................................................................................................ 38

<!-- INICIO TABLA 19 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **7.1 Factores de Emisión para Material Particulado Resuspendido** Las expresiones de factores de emisión para la estimación de emisiones de material particulado resuspendido, se presentan a continuación [16] . -->

**Tabla 19: Factor de Emisión Escarpes****

| Factor de Emisión (fe) | fe = k*0,570 |
| --- | --- |
| Unidades | kg/km |
| Parámetros | No utiliza parámetros<br>K: Factor según tamaño de partícula<br> PM10 = 0,75<br> PM2.5 = 0,105<br> MPS = 1 |
| Fuente | Compilation of Air Pollutant Emission Factors, AP 42, 5th Edition: Chapter 13,<br>Section 13.2.3“Heavy Construction Operations, 2010” |
| Descripción | Corresponde al factor de emisión de preparación de terrenos (movimiento de<br>tierra) y retiro de cobertura vegetal. La unidad de este factor corresponde a<br>kilógramos emitidos por kilómetro recorrido en el proceso de escarpado de la |

<!-- Estadísticas: 4 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- 16 Fuente de Información: Guía para la estimación de emisiones atmosféricas de proyectos inmobiliarios para la Región Metropolitana del Ministerio del Medio Ambiente, [enero 2012]. -->
<!-- FIN TABLA 19 -->


Tabla 20: Factor de Emisión Excavaciones ......................................................................................... 39

<!-- INICIO TABLA 20 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|cobertura vegetal.| |---|---| |Nivel de actividad|El nivel de actividad se determina según la distancia que recorre el cargador<br>frontal por el área a escapar. Por defecto para 1 hectárea se recorre una distancia<br>de 3,57 km| |Mitigación|No aplican medidas de mitigación| -->

**Tabla 20: Factor de Emisión Excavaciones****

| Factor de Emisión (fe) | fe = 0.45*k*(s^1.5/M^1.4) [Para PM10 y PM2.5]<br>fe = 2.6*s^1.2/M^1.3 [Para MPS] |
| --- | --- |
| Unidades | kg/h |
| Parámetros | K: Factor según tamaño de partícula<br> PM10 = 0.75<br> PM2.5 = 0,105<br> MPS = 2.6<br>s: % de finos del suelo [8,5 valor por defecto]<br>M: % humedad material [6,5 valor por defecto] |
| Fuente | Compilation of Air Pollutant Emission Factors, AP 42, 5th Edition: Chapter 11,<br>Section 11.9 “Western Surface Coal Mining, 1998”, Table 11.9-2. |
| Descripción | Corresponde al factor de emisión de despeje de material (bulldozing / overburden)<br>escalado por 0,75 para ser aplicado a MP10. La unidad de este factor corresponde<br>a kilógramos emitidos por hora excavada |
| Nota | El nivel de actividad se determina a través del rendimiento de la maquinaria y el<br>volumen a escavar. Por defecto se considerará para una retroexcavadora con<br>capacidad de palada de 1 m3 un rendimiento igual a 30 m3/hr. |
| Mitigación | No aplican medidas de mitigación. |

<!-- Estadísticas: 6 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 21: Factor de Emisión Transferencia de Material (Carguío y Volteo de Camiones)** |Factor de Emisión (fe)|fe = 0.0016*k*(U/2.2)^1.3/(M/2)^1.4| |---|---| -->
<!-- FIN TABLA 20 -->


Tabla 21: Factor de Emisión Transferencia de Material (Carguío y Volteo de Camiones) .................. 39

<!-- INICIO TABLA 21 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Fuente|Compilation of Air Pollutant Emission Factors, AP 42, 5th Edition: Chapter 11,<br>Section 11.9 “Western Surface Coal Mining, 1998”, Table 11.9-2.| |Descripción|Corresponde al factor de emisión de despeje de material (bulldozing / overburden)<br>escalado por 0,75 para ser aplicado a MP10. La unidad de este factor corresponde<br>a kilógramos emitidos por hora excavada| |Nota|El nivel de actividad se determina a través del rendimiento de la maquinaria y el<br>volumen a escavar. Por defecto se considerará para una retroexcavadora con<br>capacidad de palada de 1 m3 un rendimiento igual a 30 m3/hr.| |Mitigación|No aplican medidas de mitigación.| -->

**Tabla 21: Factor de Emisión Transferencia de Material (Carguío y Volteo de Camiones)****

| Factor de Emisión (fe) | fe = 0.0016*k*(U/2.2)^1.3/(M/2)^1.4 |
| --- | --- |
| Unidades | kg/ton |
| Parámetros | K: Factor según tamaño de partícula<br> PM10 = 0,35<br> PM2.5 = 0,053<br> MPS = 0.74<br>U: Velocidad del viento (m/s) [5 m/s valor por defecto]<br>M: Humedad del material [6,5 valor por defecto] |
| Fuente | Compilation of Air Pollutant Emission Factors, AP 42: Chapter 13, Section 13.2.4<br>“Aggregate Handling and Storage Piles, 2006”. |
| Descripción | Corresponde al factor de emisión de transferencia discreta de material utilizado<br>directamente. La unidad de este factor corresponde a kilogramos emitidos por<br>cada tonelada de material cargado o descargado. |
| Mitigación | No aplican medidas de mitigación. |

<!-- Estadísticas: 5 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Informe de Emisiones Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 39 **Tabla 22: Factores de Emisión Resuspensión de MP por Circulación de Vehículos en Caminos** -->
<!-- FIN TABLA 21 -->

Tabla 22: Factores de Emisión Resuspensión de MP por Circulación de Vehículos en Caminos

<!-- INICIO TABLA 22 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Mitigación|No aplican medidas de mitigación.| Informe de Emisiones Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 39 -->

**Tabla 22: Factores de Emisión Resuspensión de MP por Circulación de Vehículos en Caminos****

| Factor de Emisión (fe) | fe = k*(sL)^0.91*W^1.02 |
| --- | --- |
| Unidades | gr/ton |
| Parámetros | K: Factor según tamaño de partícula<br> PM10 = 0,62<br> PM2.5 = 0,15<br> MPS = 3.23<br>sL: Carga de fino de la superficie, (g/m2)<br>W: Peso promedio del flujo total de la flota que circula por las vías (Toneladas) |
| Fuente | Compilation of Air Pollutant Emission Factors, AP-42: Chapter 13, Section 13.2.1<br>“Paved Roads, 2011”. |
| Descripción | Corresponde al factor de emisión de material particulado resuspendido por<br>tránsito de vehículos por caminos pavimentados. La unidad de este factor de<br>emisión es gramos de MP10 emitidos por kilómetro recorrido. |
| Mitigación | No aplican medidas de mitigación. |

<!-- Estadísticas: 5 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 23: Factor de Emisión Resuspensión de MP10 Circulación de Vehículos Livianos en** **Caminos No Pavimentados** -->
<!-- FIN TABLA 22 -->


Pavimentados ....................................................................................................................... 40

Tabla 23: Factor de Emisión Resuspensión de MP10 Circulación de Vehículos Livianos en

<!-- INICIO TABLA 23 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Parámetros|K: Factor según tamaño de partícula<br> PM10 = 0,62<br> PM2.5 = 0,15<br> MPS = 3.23<br>sL: Carga de fino de la superficie, (g/m2)<br>W: Peso promedio del flujo total de la flota que circula por las vías (Toneladas)| |Fuente|Compilation of Air Pollutant Emission Factors, AP-42: Chapter 13, Section 13.2.1<br>“Paved Roads, 2011”.| |Descripción|Corresponde al factor de emisión de material particulado resuspendido por<br>tránsito de vehículos por caminos pavimentados. La unidad de este factor de<br>emisión es gramos de MP10 emitidos por kilómetro recorrido.| |Mitigación|No aplican medidas de mitigación.| -->

**Tabla 23: Factor de Emisión Resuspensión de MP10 Circulación de Vehículos Livianos en****

| Factor de Emisión (fe) | fe = 281.9*k*(s/12)*(S/30)^0.5/(M/0.5)^0.2 |
| --- | --- |
| Unidades | g/km |
| Parámetros | K: Factor según tamaño de partícula<br> PM10 = 1.5<br> PM2.5 = 0,15<br> MPS = 4.9<br>s: % de finos del suelo [8,5 valor por defecto]<br>S: Velocidad de los vehículos en km/h<br>M: % humedad material. [6,5 valor por defecto] |
| Fuente | Compilation of Air Pollutant Emission Factors, AP 42: Chapter 13, Section 13.2.2<br>“Unpaved Roads, 2006”. |
| Descripción | Corresponde al factor de emisión de tránsito por caminos no pavimentados<br>determinado para caminos de acceso público. La unidad de este factor de emisión<br>es gramos de MP10 emitidos por kilómetro recorrido |
| Nota | Dadas las características de la flota utilizada en la determinación de este factor de<br>emisión, su aplicación se reconoce válida para una flota de vehículos pesados, es<br>decir, cuyo peso promedio exceda las 2,7 toneladas métricas.<br>Contenido de % de finos del suelo - valor por defecto 8,5%<br>Contenido de humedad del suelo - valor por defecto 6,5% |
| Mitigación | Como medida de abatimiento se considera el mejoramiento de caminos mediante<br>la aplicación de una capa de gravilla. |

<!-- Estadísticas: 6 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 24: Factor de Emisión Resuspensión de MP10 Circulación de Vehículos Pesados en** **Caminos No Pavimentados** -->
<!-- FIN TABLA 23 -->


Caminos No Pavimentados .................................................................................................. 40

Tabla 24: Factor de Emisión Resuspensión de MP10 Circulación de Vehículos Pesados en

<!-- INICIO TABLA 24 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Fuente|Compilation of Air Pollutant Emission Factors, AP 42: Chapter 13, Section 13.2.2<br>“Unpaved Roads, 2006”.| |Descripción|Corresponde al factor de emisión de tránsito por caminos no pavimentados<br>determinado para caminos de acceso público. La unidad de este factor de emisión<br>es gramos de MP10 emitidos por kilómetro recorrido| |Nota|Dadas las características de la flota utilizada en la determinación de este factor de<br>emisión, su aplicación se reconoce válida para una flota de vehículos pesados, es<br>decir, cuyo peso promedio exceda las 2,7 toneladas métricas.<br>Contenido de % de finos del suelo - valor por defecto 8,5%<br>Contenido de humedad del suelo - valor por defecto 6,5%| |Mitigación|Como medida de abatimiento se considera el mejoramiento de caminos mediante<br>la aplicación de una capa de gravilla.| -->

**Tabla 24: Factor de Emisión Resuspensión de MP10 Circulación de Vehículos Pesados en****

| Factor de Emisión (fe) | fe = 281.9*k*(s/12)^0.9*(W/3)^0.45 [Para MP10 y MP2.5]<br>Fe = 281,9*4.9*(s/12) ^0,7*(W/3) ^0,45 [Para MPS] |
| --- | --- |
| Unidades | g/km |
| Parámetros | K: Factor según tamaño de partícula |

<!-- Estadísticas: 2 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Informe de Emisiones Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 40 |Col1|PM10 = 1.5<br>PM2.5 = 0,15<br>MPS = 4.9<br>s: % de finos del suelo [8,5 valor por defecto]<br>W: Peso promedio de la flota que circula por las vías (ton)| -->
<!-- FIN TABLA 24 -->


Caminos No Pavimentados .................................................................................................. 40

Tabla 25: Factores de Emisión de Cintas Transportadoras ................................................................. 41

<!-- INICIO TABLA 25 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Fuente|Compilation of Air Pollutant Emission Factors, AP 42: Chapter 13, Section 13.2.2<br>“Unpaved Roads”.| |Descripción|Corresponde al factor de emisión de transito por caminos no pavimentados<br>determinado para sitios industriales. La unidad de este factor de emisión es<br>gramos de MP10 emitidos por kilómetro recorrido.| |Nota|Dadas las características de la flota utilizada en la determinación de este factor de<br>emisión, su aplicación se reconoce válida para una flota de vehículos pesados, es<br>decir, cuyo peso promedio exceda las 2,7 toneladas métricas.<br>El titular deberá proveer el peso promedio de la flota que circula por las vías<br>relevantes. En caso de no hacerlo, el peso promedio por defecto será el peso<br>promedio de la flota generada por la actividad del proyecto.<br>Contenido de % de finos del suelo - valor por defecto 8,5%| |Mitigación|Como medida de abatimiento se considera el mejoramiento de caminos mediante<br>la aplicación de una capa de gravilla.| -->

**Tabla 25: Factores de Emisión de Cintas Transportadoras****

| Factor de Emisión (fe) | Fe = k |
| --- | --- |
| Unidades | kg/ton |
| Parámetros | Factor según tamaño de partícula<br> PM10 = 0.0006<br> PM2.5 = 0,0006<br> MPS = 0.0015<br>Nota: debido a que no existen valores para MP2,5, se considera el peor escenario<br>en que PM10 = PM2,5 |
| Fuente | AP 42: Charper 11, Sectión 11.19,2, Table 11.19.2-1 r" |
| Descripción | Corresponde al factor de emisión de emisiones generadas en traspasos cintas<br>trasportadoras |
| Mitigación | No aplican medidas de mitigación. |

<!-- Estadísticas: 5 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 26: Factores de Emisión Erosión en Pilas, Acopios** |Factor de Emisión (fe)|Fe = k * s/1,5 * f/15| |---|---| -->
<!-- FIN TABLA 25 -->

Tabla 26: Factores de Emisión Erosión en Pilas, Acopios ................................................................... 41

<!-- INICIO TABLA 26 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Parámetros|Factor según tamaño de partícula<br> PM10 = 0.0006<br> PM2.5 = 0,0006<br> MPS = 0.0015<br>Nota: debido a que no existen valores para MP2,5, se considera el peor escenario<br>en que PM10 = PM2,5| |Fuente|AP 42: Charper 11, Sectión 11.19,2, Table 11.19.2-1 r"| |Descripción|Corresponde al factor de emisión de emisiones generadas en traspasos cintas<br>trasportadoras| |Mitigación|No aplican medidas de mitigación.| -->

**Tabla 26: Factores de Emisión Erosión en Pilas, Acopios****

| Factor de Emisión (fe) | Fe = k * s/1,5 * f/15 |
| --- | --- |
| Unidades | kg/ha |
| Parámetros | Factor según tamaño de partícula<br> PM10 = 0.5<br> PM2.5 = 0,075<br> MPS = 1<br>s: contenido de fino del material (%).[8,5 valor por defecto]<br>f: porcentaje del tiempo en el que el viento excede los 5,4 m/s. [9,8 %] |
| Fuente | Industria del Árido en Chile, Tomo I, Sistematización de Antecedentes Técnicos y<br>Ambientales, 2001 |
| Descripción | Corresponde al factor de emisión para acopio de productos intermedios y finales<br>utilizado directamente |
| Mitigación | No aplican medidas de mitigación. |

<!-- Estadísticas: 5 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Informe de Emisiones Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 41 **7.2 Factores de Emisión para la Estimación de Emisiones de Gases y Material** -->
<!-- FIN TABLA 26 -->

Tabla 27: Factores de Emisión de Gases y MP de Maquinarias ......................................................... 42

<!-- INICIO TABLA 27 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Los factores de emisión de gases y material particulado de combustión, asociados a la operación de la maquinaria, vehículos, generadores, calderas y equipos de secado y fusión durante las distintas etapas del proyecto, se presentan en las tablas siguientes: -->

**Tabla 27: Factores de Emisión de Gases y MP de Maquinarias****

| Factor de Emisión (fe) | E= (FP × t × C × P) |
| --- | --- |
| Unidades | gr/día |
| Parámetros | FP: factor según potencia<br>t: tiempo de operación diaria (h)<br>C: Porcentaje de carga<br>P: Potencia Nominal (kw) |
| Fuente | Guía para la Estimación de Emisiones Atmosféricas de Proyectos Inmobiliarios<br>para la Región Metropolitana, Tabla 4.9 |
| Descripción | Corresponde al factor de emisión de combustión de los motores de la maquinaria<br>fuera de ruta. |
| Mitigación | No aplican medidas de mitigación. |

<!-- Estadísticas: 5 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 28: Factor de Emisión en Función de la Potencia (g/kW-h)** |Contaminante|0-20|20-37|37-75|75-130|>130| |---|---|---|---|---|---| -->
<!-- FIN TABLA 27 -->

Tabla 28: Factor de Emisión en Función de la Potencia (g/kW-h) ....................................................... 42

<!-- INICIO TABLA 28 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Parámetros|FP: factor según potencia<br>t: tiempo de operación diaria (h)<br>C: Porcentaje de carga<br>P: Potencia Nominal (kw)| |Fuente|Guía para la Estimación de Emisiones Atmosféricas de Proyectos Inmobiliarios<br>para la Región Metropolitana, Tabla 4.9| |Descripción|Corresponde al factor de emisión de combustión de los motores de la maquinaria<br>fuera de ruta.| |Mitigación|No aplican medidas de mitigación.| -->

**Tabla 28: Factor de Emisión en Función de la Potencia (g/kW-h)****

| Contaminante | 0-20 | 20-37 | 37-75 | 75-130 | >130 |
| --- | --- | --- | --- | --- | --- |
| CO | 8.38 | 6.43 | 5.06 | 3.76 | 3.00 |
| HC | 3.87 | 2.96 | 2.33 | 1.72 | 1.35 |
| NOx | 14.36 | 14.36 | 14.36 | 14.36 | 14.36 |
| MP | 2.22 | 1.81 | 1.51 | 1.23 | 1.10 |

<!-- Estadísticas: 4 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 29: Factor de Emisión Para Gases y MP de Vehículos** [17] |Categoría|Contaminante|Factor Emisión [g/km]| |---|---|---| -->
<!-- FIN TABLA 28 -->

Tabla 29: Factor de Emisión Para Gases y MP de Vehículos ............................................................. 42

<!-- INICIO TABLA 29 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |CO|8.38|6.43|5.06|3.76|3.00| |HC|3.87|2.96|2.33|1.72|1.35| |NOx|14.36|14.36|14.36|14.36|14.36| |MP|2.22|1.81|1.51|1.23|1.10| -->

**Tabla 29: Factor de Emisión Para Gases y MP de Vehículos** [17]**

| Categoría | Contaminante | Factor Emisión [g/km] |
| --- | --- | --- |
| Camiones Pesados<br>Diésel Tipo 3 | CO | (1,24588358438859+(103,700537481749/(1+exp((((-1)*-<br>1,3906312471446)+(0,543451750078654*ln(V)))+(0,0390066425998189*<br>V))))) |
| Camiones Pesados<br>Diésel Tipo 3 | HC | ((0,135938586321894+(0,71588074810547*exp(((-<br>1)*0,0234666513590177)*V)))+(2,79878282504916*exp(((-<br>1)*0,123459782380517)*V))) |

<!-- Estadísticas: 2 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- 17 Anexo 2 de la Guía para la estimación de emisiones atmosféricas de proyectos inmobiliarios para la Región Metropolitana, [2006]. Informe de Emisiones -->
<!-- FIN TABLA 29 -->

Tabla 30: Factor de Emisión por Combustión en Grupos Generadores .............................................. 43

<!-- INICIO TABLA 30 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Vehículos<br>Comerciales Diésel<br>Tipo 2|HC|0,62*(0.0000175*V 2-0,00284*V+0,2162)| |Vehículos<br>Comerciales Diésel<br>Tipo 2|NOx|0,84*(0.000241*V 2-0,03181*V+2,0247)| |Vehículos<br>Comerciales Diésel<br>Tipo 2|CC|0,0198*V 2-2,506*V+137,42| |Vehículos<br>Comerciales Diésel<br>Tipo 2|MP|0,67*(0.000045*V 2-0,004885*V+0,1932)| -->

**Tabla 30: Factor de Emisión por Combustión en Grupos Generadores** [18]**

| FACTORES DE EMISION GRUPOS GENERADORES (kg/kw-h) | Col2 | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Contaminante | **CO** | **NOx** | **MPS** | **MP 10** | **MP 2.5** | **SOx** | **COV** |
| Petróleo N°6 | 0,003 | 0,0146 | 0,000426 | 0,00026 | 0,000218 | 0,004919 | 0,000019 |

<!-- Estadísticas: 2 filas, 8 columnas -->
<!-- Contexto posterior: -->
<!-- **8. NIVELES DE ACTIVIDAD** El nivel de actividad (Na) utilizado para calcular las emisiones de cada actividad, en cada una de las fases del proyecto, se presenta en las tablas siguientes: -->
<!-- FIN TABLA 30 -->

Tabla 31: Nivel de Actividad Etapa de Construcción ........................................................................... 43

<!-- INICIO TABLA 31 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **8. NIVELES DE ACTIVIDAD** El nivel de actividad (Na) utilizado para calcular las emisiones de cada actividad, en cada una de las fases del proyecto, se presenta en las tablas siguientes: -->

**Tabla 31: Nivel de Actividad Etapa de Construcción****

| ACTIVIDAD | Actividad Específica | Nivel de Actividad | Col4 |
| --- | --- | --- | --- |
| **ACTIVIDAD** | Actividad Específica | Cantidad | Unidad |
| Escarpe | Escarpe Área Instalación Campamento | 0.14 | km/día |
| Escarpe | Escarpe Área Instalación Planta de Chancado<br>y Selección de Materiales | 0.89 | 0.89 |

<!-- Estadísticas: 3 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- 18 AP42 de la EPA, Chapter 3 (Stationary Internal Combustion Sources), tablas: 3.4-1; 3.4-2; 3-4-3 Informe de Emisiones Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 43 -->
<!-- FIN TABLA 31 -->

Tabla 32: Nivel de Actividad Etapa de Operación ................................................................................ 44

<!-- INICIO TABLA 32 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Transito Vehículos Pesados<br>Por Caminos No Pavimentados|Transporte Estructura Pesada|9|9| |Transito Vehículos Pesados<br>Por Caminos No Pavimentados|Transporte Camión Grúa Montaje e Instalación|3|3| |Transito Vehículos Pesados<br>Por Caminos No Pavimentados|Transporte Petróleo|3|3| |Transito Vehículos Pesados<br>Por Caminos No Pavimentados|Transporte Agua Potable|3|3| -->

**Tabla 32: Nivel de Actividad Etapa de Operación****

| ACTIVIDAD | Actividad Específica | Nivel de Actividad | Col4 |
| --- | --- | --- | --- |
| **ACTIVIDAD** | Actividad Específica | Cantidad | Unidad |
| Excavaciones | Excavaciones Área 1 y 2 de Extracción de<br>Áridos | 27,40 | h/día |
| Carguío y Volteo de Camiones | Carga y descarga de áridos de acopio<br>intermedio | 1.643,84 | ton/día |
| Carguío y Volteo de Camiones | Carga y descarga de áridos en buzón<br>alimentación Planta | 1.643,84 | 1.643,84 |
| Tránsito Por Caminos<br>Pavimentados | Transporte de Petróleo | 100 | km/día |
| Tránsito Por Caminos<br>Pavimentados | Transporte Agua Potable | 100 | 100 |
| Tránsito Por Caminos<br>Pavimentados | Transporte de Residuos varios | 52,0 | 52,0 |
| Tránsito Por Caminos<br>Pavimentados | Transporte de Personal y Supervisión | 200 | 200 |
| Transito Vehículos Livianos<br>Por Caminos No Pavimentados | Transporte de Personal y Supervisión | 6 | km/día |
| Transito Vehículos Pesados<br>Por Caminos No Pavimentados | Transporte interno de Áridos a la Planta | 65,75 | km/día |
| Transito Vehículos Pesados<br>Por Caminos No Pavimentados | Transporte de Petróleo | 3 | 3 |
| Transito Vehículos Pesados<br>Por Caminos No Pavimentados | Transporte de Agua Potable | 3 | 3 |
| Transito Vehículos Pesados<br>Por Caminos No Pavimentados | Transporte de Residuos Varios | 3 | 3 |
| Chancado | Chancador primario | 1.643,84 | Ton/día |
| Harneado | Harnero primario | 1.643,84 | Ton/día |
| Harneado | Harnero Secundario | 410,96 | 410,96 |

<!-- Estadísticas: 16 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Informe de Emisiones Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 44 |Cintas Transportadoras|Alimentación Harnero Primario.|1.643,84|Ton/día| -->
<!-- FIN TABLA 32 -->

Tabla 33: Nivel de Actividad Etapa de Cierre....................................................................................... 45

<!-- INICIO TABLA 33 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Erosión de Materiales en Pila|Acopio de Material Grueso|0,05|ha/día| |Erosión de Materiales en Pila|Acopio de Material Graba|0,05|0,05| |Erosión de Materiales en Pila|Acopios de Material Gravilla|0,05|0,05| |Erosión de Materiales en Pila|Acopio de Material Arena|0,05|0,05| -->

**Tabla 33: Nivel de Actividad Etapa de Cierre****

| ACTIVIDAD | Actividad Específica | Nivel de Actividad | Col4 |
| --- | --- | --- | --- |
| **ACTIVIDAD** | Actividad Específica | Cantidad | Unidad |
| Reperfilamiento | Reperfilamiento área Planta | 0,89 | km/día |
| Reperfilamiento | Reperfilamiento área Camino | 3,75 | 3,75 |
| Tránsito Por Caminos<br>Pavimentados | Transporte Equipos Planta | 100 | km/día |
| Tránsito Por Caminos<br>Pavimentados | Transporte Estructura Pesada | 300 | 300 |
| Tránsito Por Caminos<br>Pavimentados | Transporte Camión Grúa para Desmontaje | 100 | 100 |
| Tránsito Por Caminos<br>Pavimentados | Transporte de Petróleo | 100 | 100 |
| Tránsito Por Caminos<br>Pavimentados | Transporte de Agua Potable | 100 | 100 |
| Tránsito Por Caminos<br>Pavimentados | Transporte de Personal y Supervisión | 200 | 200 |
| Transito Vehículos Livianos<br>Por Caminos No Pavimentados | Transporte de Personal y Supervisión | 6 | km/día |
| Transito Vehículos Pesados<br>Por Caminos No Pavimentados | Transporte de Petróleo | 3 | km/día |
| Transito Vehículos Pesados<br>Por Caminos No Pavimentados | Transporte de Equipos Planta | 3 | 3 |
| Transito Vehículos Pesados<br>Por Caminos No Pavimentados | Transporte de Estructura Pesada | 9 | 9 |
| Transito Vehículos Pesados<br>Por Caminos No Pavimentados | Transporte Camión Grúa para Desmontaje | 3 | 3 |
| Transito Vehículos Pesados<br>Por Caminos No Pavimentados | Transporte Camión Grúa para Desmontaje | 3 | 3 |

<!-- Estadísticas: 15 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Informe de Emisiones Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 45 **9.** **MEDIDAS DE MITIGACIÓN CAMINOS** -->
<!-- FIN TABLA 33 -->

Tabla 34: Factores de Emisión (MP10, MP2.5 y MPS) - Actividades Etapa de Construcción ........... 46

<!-- INICIO TABLA 34 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **10. RESULTADOS INVENTARIO DE EMISIONES** Las tablas siguientes muestran los resultados del inventario de emisiones. -->

**Tabla 34: Factores de Emisión (MP10, MP2.5 y MPS) - Actividades Etapa de Construcción****

| ACTIVIDAD | Actividad Específica | Parámetros para Factores<br>de Emisión | Col4 | Col5 | Factor de<br>emisión<br>PM10 | Factor de<br>emisión<br>PM2.5 | Factor de<br>emisión<br>MPS | Unidad |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ACTIVIDAD** | Actividad Específica | k10 | k2,5 | kMPS | kMPS | kMPS | kMPS | kMPS |
| Escarpe | Escarpe Área Instalación<br>Campamento | 0,75 | 0,105 | 1 | 4,28E+00 | 5,99E-01 | 5,70E+00 | kg/km |
| Escarpe | Escarpe Área Instalación<br>Planta de Chancado y<br>Selección de Materiales | 0,75 | 0,105 | 1 | 4,28E+00 | 5,99E-01 | 5,70E+00 | 5,70E+00 |
| Tránsito de Vehículos<br>Por Caminos<br>Pavimentados | Transporte Equipos Planta | 0,62 | 0,15 | 3,23 | 1,64E-02 | 3,96E-03 | 8,52E-02 | kg/km |
| Tránsito de Vehículos<br>Por Caminos<br>Pavimentados | Transporte Estructura<br>Pesada | 0,62 | 0,15 | 3,23 | 1,64E-02 | 3,96E-03 | 8,52E-02 | 8,52E-02 |
| Tránsito de Vehículos<br>Por Caminos<br>Pavimentados | Camión Grúa Para Montaje<br>e Instalación | 0,62 | 0,15 | 3,23 | 1,64E-02 | 3,96E-03 | 8,52E-02 | 8,52E-02 |
| Tránsito de Vehículos<br>Por Caminos<br>Pavimentados | Transporte Petróleo | 0,62 | 0,15 | 3,23 | 1,64E-02 | 3,96E-03 | 8,52E-02 | 8,52E-02 |
| Tránsito de Vehículos<br>Por Caminos<br>Pavimentados | Transporte Agua Potable | 0,62 | 0,15 | 3,23 | 1,64E-02 | 3,96E-03 | 8,52E-02 | 8,52E-02 |
| Tránsito de Vehículos<br>Por Caminos<br>Pavimentados | Transporte de Personal y<br>Supervisión | 0,62 | 0,15 | 3,23 | 1,18E-03 | 2,85E-04 | 6,14E-03 | 6,14E-03 |
| Transito Vehículos<br>Livianos Por Caminos<br>No Pavimentados | Transporte de Personal y<br>Supervisión | 1,5 | 0,15 | 4,9 | 3,27E-01 | 3,27E-02 | 1,07E+00 | kg/km |
| Transito Vehículos<br>Pesados Por Caminos<br>No Pavimentados | Transporte Equipos Planta | 1,5 | 0,15 | 4,9 | 9,24E-01 | 9,24E-02 | 3,02E+00 | kg/km |
| Transito Vehículos<br>Pesados Por Caminos<br>No Pavimentados | Transporte Estructura<br>Pesada | 1,5 | 0,15 | 4,9 | 9,24E-01 | 9,24E-02 | 3,02E+00 | 3,02E+00 |
| Transito Vehículos<br>Pesados Por Caminos<br>No Pavimentados | Camión Grúa Para Montaje<br>e Instalación | 1,5 | 0,15 | 4,9 | 9,24E-01 | 9,24E-02 | 3,02E+00 | 3,02E+00 |
| Transito Vehículos<br>Pesados Por Caminos<br>No Pavimentados | Transporte Petróleo | 1,5 | 0,15 | 4,9 | 9,24E-01 | 9,24E-02 | 3,02E+00 | 3,02E+00 |
| Transito Vehículos<br>Pesados Por Caminos<br>No Pavimentados | Transporte Agua Potable | 1,5 | 0,15 | 4,9 | 9,24E-01 | 9,24E-02 | 3,02E+00 | 3,02E+00 |

<!-- Estadísticas: 15 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Informe de Emisiones Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 46 **Tabla 35: Factores de Emisión (MP10, MP2.5 y MPS) - Actividades Etapa de Operación** -->
<!-- FIN TABLA 34 -->

Tabla 35: Factores de Emisión (MP10, MP2.5 y MPS) - Actividades Etapa de Operación ................ 47

<!-- INICIO TABLA 35 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Transito Vehículos<br>Pesados Por Caminos<br>No Pavimentados|Transporte Agua Potable|1,5|0,15|4,9|9,24E-01|9,24E-02|3,02E+00|3,02E+00| Informe de Emisiones Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 46 -->

**Tabla 35: Factores de Emisión (MP10, MP2.5 y MPS) - Actividades Etapa de Operación****

| ACTIVIDAD | Actividad Específica | Parámetros para Factores<br>de Emisión | Col4 | Col5 | Factor de<br>emisión<br>PM10 | Factor de<br>emisión<br>PM2.5 | Factor de<br>emisión<br>MPS | Unidad |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ACTIVIDAD** | Actividad Específica | k10 | k2,5 | kMPS | kMPS | kMPS | kMPS | kMPS |
| Excavaciones | Excavación Área 1 y 2 de<br>extracción de áridos | 0,75 | 0,105 | 2,6 | 6,09E-01 | 8,52E-02 | 2,98E+00 | kg/h |
| Carguío y Volteo<br>de Camiones | Carga y descarga de<br>áridos en acopio<br>intermedio | 0,35 | 0,053 | 0,74 | 3,13E-04 | 4,73E-05 | 6,61E-04 | kg/ton |
| Carguío y Volteo<br>de Camiones | Carga y descarga de<br>áridos en buzón<br>alimentación Planta | 0,35 | 0,053 | 0,74 | 3,13E-04 | 4,73E-05 | 6,61E-04 | 6,61E-04 |
| Tránsito Por Caminos<br>Pavimentados | Transporte Petróleo | 0,62 | 0,15 | 3,23 | 1,64E-02 | 3,96E-03 | 8,52E-02 | kg/km |
| Tránsito Por Caminos<br>Pavimentados | Transporte Agua Potable | 0,62 | 0,15 | 3,23 | 1,64E-02 | 3,96E-03 | 8,52E-02 | 8,52E-02 |
| Tránsito Por Caminos<br>Pavimentados | Transporte de Residuos<br>varios | 0,62 | 0,15 | 3,23 | 1,64E-02 | 3,96E-03 | 8,52E-02 | 8,52E-02 |
| Tránsito Por Caminos<br>Pavimentados | Transporte de Personal y<br>Supervisión | 0,62 | 0,15 | 3,23 | 1,18E-03 | 2,85E-04 | 6,14E-03 | 6,14E-03 |
| Transito Vehículos<br>Livianos Por Caminos<br>No Pavimentados | Transporte de Personal y<br>Supervisión | 1,5 | 0,15 | 4,9 | 3,27E-01 | 3,27E-02 | 1,07E+00 | kg/km |
| Transito Vehículos<br>Pesados Por Caminos<br>No Pavimentados | Transporte Interno de<br>Áridos a la Planta | 1,5 | 0,15 | 4,9 | 9,24E-01 | 9,24E-02 | 3,02E+00 | kg/km |
| Transito Vehículos<br>Pesados Por Caminos<br>No Pavimentados | Transporte Petróleo | 1,5 | 0,15 | 4,9 | 9,24E-01 | 9,24E-02 | 3,02E+00 | 3,02E+00 |
| Transito Vehículos<br>Pesados Por Caminos<br>No Pavimentados | Transporte Agua Potable | 1,5 | 0,15 | 4,9 | 9,24E-01 | 9,24E-02 | 3,02E+00 | 3,02E+00 |
| Transito Vehículos<br>Pesados Por Caminos<br>No Pavimentados | Transporte de Residuos<br>varios | 1,5 | 0,15 | 4,9 | 9,24E-01 | 9,24E-02 | 3,02E+00 | 3,02E+00 |
| Chancado | Chancado Primario | 0,02 | 0,02 | 0,2 | 2,0E-02 | 2,0E-02 | 2,0E-01 | kg/ton |
| Harneado | Harnero Primario | 0,0043 | 0,0043 | 0,012 | 4,3E-03 | 4,3E-03 | 1,2E-02 | kg/ton |
| Harneado | Harnero Secundario | 0,036 | 0,036 | 0,15 | 3,6E-02 | 3,6E-02 | 1,5E-01 | 1,5E-01 |
| Cintas Transportadoras | Cinta transportadora de<br>alimentación harnero<br>primario<br>(1 traspaso) | 0,0006 | 0,0006 | 0,0015 | 5,5E-04 | 5,5E-04 | 1,5E-03 | kg/ton |
| Cintas Transportadoras | Cinta transportadora<br>material graba<br>(1 traspaso) | 0,0006 | 0,0006 | 0,0015 | 5,5E-04 | 5,5E-04 | 1,5E-03 | 1,5E-03 |
| Cintas Transportadoras | Cinta transportadora<br>material gravilla<br>(1 traspaso) | 0,0006 | 0,0006 | 0,0015 | 5,5E-04 | 5,5E-04 | 1,5E-03 | 1,5E-03 |
| Cintas Transportadoras | Cinta transportadora<br>material grueso<br>(1 traspaso) | 0,0006 | 0,0006 | 0,0015 | 5,5E-04 | 5,5E-04 | 1,5E-03 | 1,5E-03 |
| Cintas Transportadoras | Cinta transportadora al<br>harnero secundario<br>(1 traspaso) | 0,0006 | 0,0006 | 0,0015 | 5,5E-04 | 5,5E-04 | 1,5E-03 | 1,5E-03 |

<!-- Estadísticas: 21 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Informe de Emisiones Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 47 |Cintas Transportadoras|Cinta transportadora<br>acopio arena<br>(1 traspaso)|0,0006|0,0006|0,0015|5,5E-04|5,5E-04|1,5E-03|kg/ton| -->
<!-- FIN TABLA 35 -->

Tabla 36: Factores de Emisión (MP10, MP2.5 y MPS) - Actividades Etapa de Cierre ....................... 48

<!-- INICIO TABLA 36 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Erosión en Pilas|Acopio de material grueso|0,5|0,075|1|3,04|0,46|6,08|kg/ha| |Erosión en Pilas|Acopio de material graba|0,5|0,075|1|3,04|0,46|6,08|6,08| |Erosión en Pilas|Acopio de material gravilla|0,5|0,075|1|3,04|0,46|6,08|6,08| |Erosión en Pilas|Acopio de material arena|0,5|0,075|1|3,04|0,46|6,08|6,08| -->

**Tabla 36: Factores de Emisión (MP10, MP2.5 y MPS) - Actividades Etapa de Cierre****

| ACTIVIDAD | Actividad Específica | Parámetros para<br>Factores de Emisión | Col4 | Col5 | Factor de<br>emisión<br>PM10 | Factor de<br>emisión<br>PM2.5 | Factor de<br>emisión<br>MPS | Unidad |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ACTIVIDAD | Actividad Específica | k10 | k2,5 | kMPS | kMPS | kMPS | kMPS | kMPS |
| Reperfilado | Reperfilamiento área<br>Planta | 0,75 | 0,105 | 1 | 4,28E+00 | 5,99E-01 | 5,70E+00 | kg/h |
| Reperfilado | Reperfilamiento área<br>Camino | 0,75 | 0,105 | 1 | 4,28E+00 | 5,99E-01 | 5,70E+00 | 5,70E+00 |
| Tránsito Por Caminos<br>Pavimentados | Transporte Equipos Planta | 0,62 | 0,15 | 3,23 | 1,64E-02 | 3,96E-03 | 8,52E-02 | kg/km |
| Tránsito Por Caminos<br>Pavimentados | Transporte Estructura<br>Pesada | 0,62 | 0,15 | 3,23 | 1,64E-02 | 3,96E-03 | 8,52E-02 | 8,52E-02 |
| Tránsito Por Caminos<br>Pavimentados | Camión Grúa Para<br>Montaje e Instalación | 0,62 | 0,15 | 3,23 | 1,64E-02 | 3,96E-03 | 8,52E-02 | 8,52E-02 |
| Tránsito Por Caminos<br>Pavimentados | Transporte Petróleo | 0,62 | 0,15 | 3,23 | 1,64E-02 | 3,96E-03 | 8,52E-02 | 8,52E-02 |
| Tránsito Por Caminos<br>Pavimentados | Transporte Agua Potable | 0,62 | 0,15 | 3,23 | 1,64E-02 | 3,96E-03 | 8,52E-02 | 8,52E-02 |
| Tránsito Por Caminos<br>Pavimentados | Transporte de Personal y<br>Supervisión | 0,62 | 0,15 | 3,23 | 1,18E-03 | 2,85E-04 | 6,14E-03 | 6,14E-03 |
| Transito Vehículos<br>Livianos Por Caminos<br>No Pavimentados | Transporte de Personal y<br>Supervisión | 1,5 | 0,15 | 4,9 | 3,27E-01 | 3,27E-02 | 1,07E+00 | kg/km |
| Transito Vehículos<br>Pesados<br>Por Caminos No<br>Pavimentados | Transporte Equipos Planta | 1,5 | 0,15 | 4,9 | 9,24E-01 | 9,24E-02 | 3,02E+00 | 3,02E+00 |
| Transito Vehículos<br>Pesados<br>Por Caminos No<br>Pavimentados | Transporte Estructura<br>Pesada | 1,5 | 0,15 | 4,9 | 9,24E-01 | 9,24E-02 | 3,02E+00 | kg/km |
| Transito Vehículos<br>Pesados<br>Por Caminos No<br>Pavimentados | Camión Grúa Para<br>Montaje e Instalación | 1,5 | 0,15 | 4,9 | 9,24E-01 | 9,24E-02 | 3,02E+00 | 3,02E+00 |
| Transito Vehículos<br>Pesados<br>Por Caminos No<br>Pavimentados | Transporte Petróleo | 1,5 | 0,15 | 4,9 | 9,24E-01 | 9,24E-02 | 3,02E+00 | 3,02E+00 |
| Transito Vehículos<br>Pesados<br>Por Caminos No<br>Pavimentados | Transporte Agua Potable | 1,5 | 0,15 | 4,9 | 9,24E-01 | 9,24E-02 | 3,02E+00 | 3,02E+00 |

<!-- Estadísticas: 15 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Informe de Emisiones Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 48 **Tabla 37: Emisiones (MP10, MP2.5 y MPS) - Actividades Etapa de Construcción** -->
<!-- FIN TABLA 36 -->

Tabla 37: Emisiones (MP10, MP2.5 y MPS) - Actividades Etapa de Construcción ............................ 49

<!-- INICIO TABLA 37 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Transito Vehículos<br>Pesados<br>Por Caminos No<br>Pavimentados|Transporte Agua Potable|1,5|0,15|4,9|9,24E-01|9,24E-02|3,02E+00|3,02E+00| Informe de Emisiones Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 48 -->

**Tabla 37: Emisiones (MP10, MP2.5 y MPS) - Actividades Etapa de Construcción****

| ACTIVIDAD | Actividad Específica | Emisiones Diarias (kg/día) | Col4 | Col5 | Emisiones Anuales (ton/año) | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **ACTIVIDAD** | Actividad Específica | Emisiones<br>PM10 | Emisiones<br>PM2.5 | Emisiones<br>MPS | Emisiones<br>PM10 | Emisiones<br>PM2.5 | Emisiones<br>MPS |
| Escarpe | Escarpe Área Instalación<br>Campamento | 0,6105 | 0,0855 | 0,8140 | 0,0006 | 0,0001 | 0,0008 |
| Escarpe | Escarpe Área Instalación<br>Planta de Chancado y<br>Selección de Materiales | 3,8154 | 0,5342 | 5,0873 | 0,0038 | 0,0005 | 0,0051 |
| Tránsito de Vehículos Por<br>Caminos Pavimentados | Transporte Equipos Planta | 1,6351 | 0,3956 | 8,5182 | 0,0016 | 0,0004 | 0,0085 |
| Tránsito de Vehículos Por<br>Caminos Pavimentados | Transporte Estructura Pesada | 4,9052 | 1,1868 | 25,5547 | 0,0049 | 0,0012 | 0,0256 |
| Tránsito de Vehículos Por<br>Caminos Pavimentados | Camión Grúa Para Montaje e<br>Instalación | 1,6351 | 0,3956 | 8,5182 | 0,0016 | 0,0004 | 0,0085 |
| Tránsito de Vehículos Por<br>Caminos Pavimentados | Transporte Petróleo | 1,6351 | 0,3956 | 8,5182 | 0,0196 | 0,0047 | 0,1022 |
| Tránsito de Vehículos Por<br>Caminos Pavimentados | Transporte Agua Potable | 1,6351 | 0,3956 | 8,5182 | 0,0196 | 0,0047 | 0,1022 |
| Tránsito de Vehículos Por<br>Caminos Pavimentados | Transporte de Personal y<br>Supervisión | 0,2357 | 0,0570 | 1,2278 | 0,0212 | 0,0051 | 0,1105 |
| Transito Vehículos<br>Livianos Por Caminos No<br>Pavimentados | Transporte de Personal y<br>Supervisión | 1,9644 | 0,1964 | 6,4170 | 0,1768 | 0,0177 | 0,5775 |
| Transito Vehículos<br>Pesados Por Caminos No<br>Pavimentados | Transporte Equipos Planta | 2,7732 | 0,2773 | 9,0591 | 0,0028 | 0,0003 | 0,0091 |
| Transito Vehículos<br>Pesados Por Caminos No<br>Pavimentados | Transporte Estructura Pesada | 8,3196 | 0,8320 | 27,1774 | 0,0083 | 0,0008 | 0,0272 |
| Transito Vehículos<br>Pesados Por Caminos No<br>Pavimentados | Camión Grúa Para Montaje e<br>Instalación | 2,7732 | 0,2773 | 9,0591 | 0,0028 | 0,0003 | 0,0091 |
| Transito Vehículos<br>Pesados Por Caminos No<br>Pavimentados | Transporte Petróleo | 2,7732 | 0,2773 | 9,0591 | 0,0333 | 0,0033 | 0,1087 |
| Transito Vehículos<br>Pesados Por Caminos No<br>Pavimentados | Transporte Agua Potable | 2,7732 | 0,2773 | 9,0591 | 0,0333 | 0,0033 | 0,1087 |
| **TOTALES EMISIONES ETAPA DE CONSTRUCCIÓN** | **TOTALES EMISIONES ETAPA DE CONSTRUCCIÓN** | **37,48** | **5,58** | **136,59** | **0,33** | **0,04** | **1,20** |

<!-- Estadísticas: 16 filas, 8 columnas -->
<!-- Contexto posterior: -->
<!-- Informe de Emisiones Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 49 **Tabla 38: Emisiones (MP10, MP2.5 y MPS) - Actividades Etapa de Operación** -->
<!-- FIN TABLA 37 -->


Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 3

Tabla 38: Emisiones (MP10, MP2.5 y MPS) - Actividades Etapa de Operación ................................ 50

<!-- INICIO TABLA 38 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |**TOTALES EMISIONES ETAPA DE CONSTRUCCIÓN**|**TOTALES EMISIONES ETAPA DE CONSTRUCCIÓN**|**37,48**|**5,58**|**136,59**|**0,33**|**0,04**|**1,20**| Informe de Emisiones Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 49 -->

**Tabla 38: Emisiones (MP10, MP2.5 y MPS) - Actividades Etapa de Operación****

| ACTIVIDAD | Actividad Específica | Emisiones Diarias (kg/día) | Col4 | Col5 | Emisiones Anuales (ton/año) | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **ACTIVIDAD** | Actividad Específica | Emisiones<br>PM10 | Emisiones<br>PM2.5 | Emisiones<br>MPS | Emisiones<br>PM10 | Emisiones<br>PM2.5 | Emisiones<br>MPS |
| Excavaciones | Excavación Área 1 y 2 de<br>extracción de áridos | 16,6736 | 2,3343 | 81,5072 | 6,0859 | 0,8520 | 29,7501 |
| Carguío y Volteo<br>de Camiones | Carga y descarga de áridos<br>en acopio intermedio | 0,5140 | 0,0778 | 1,0866 | 0,1876 | 0,0284 | 0,3966 |
| Carguío y Volteo<br>de Camiones | Carga y descarga de áridos<br>en buzón alimentación Planta | 0,5140 | 0,0778 | 1,0866 | 0,1876 | 0,0284 | 0,3966 |
| Tránsito Por Caminos<br>Pavimentados | Transporte Petróleo | 1,6351 | 0,3956 | 8,5182 | 0,5968 | 0,1444 | 3,1092 |
| Tránsito Por Caminos<br>Pavimentados | Transporte Agua Potable | 1,6351 | 0,3956 | 8,5182 | 0,5968 | 0,1444 | 3,1092 |
| Tránsito Por Caminos<br>Pavimentados | Transporte de Residuos<br>varios | 1,6351 | 0,3956 | 8,5182 | 0,5968 | 0,1444 | 3,1092 |
| Tránsito Por Caminos<br>Pavimentados | Transporte de Personal y<br>Supervisión | 0,2357 | 0,0570 | 1,2278 | 0,0860 | 0,0208 | 0,4481 |
| Transito Vehículos<br>Livianos Por Caminos<br>No Pavimentados | Transporte de Personal y<br>Supervisión | 1,9644 | 0,1964 | 6,4170 | 0,7170 | 0,0717 | 2,3422 |
| Transito Vehículos<br>Pesados Por Caminos<br>No Pavimentados | Transporte Interno de Áridos a<br>la Planta | 60,7826 | 6,0783 | 198,5566 | 22,1857 | 2,2186 | 72,4732 |
| Transito Vehículos<br>Pesados Por Caminos<br>No Pavimentados | Transporte Petróleo | 2,7732 | 0,2773 | 9,0591 | 1,0122 | 0,1012 | 3,3066 |
| Transito Vehículos<br>Pesados Por Caminos<br>No Pavimentados | Transporte Agua Potable | 2,7732 | 0,2773 | 9,0591 | 0,8652 | 0,0865 | 2,8265 |
| Transito Vehículos<br>Pesados Por Caminos<br>No Pavimentados | Transporte de Residuos<br>varios | 2,7732 | 0,2773 | 9,0591 | 0,8652 | 0,0865 | 2,8265 |
| Chancado | Chancado Primario | 32,8767 | 32,8767 | 328,7671 | 12,0000 | 12,0000 | 120,0000 |
| Harneado | Harnero Primario | 7,0685 | 7,0685 | 19,7260 | 2,5800 | 2,5800 | 7,2000 |
| Harneado | Harnero Secundario | 14,7945 | 14,7945 | 61,6438 | 5,4000 | 5,4000 | 22,5000 |
| Cintas Transportadoras<br>Cintas Transportadoras | Cinta transportadora de<br>alimentación harnero primario<br>(1 traspaso) | 0,9041 | 0,9041 | 2,4658 | 0,3300 | 0,3300 | 0,9000 |
| Cintas Transportadoras<br>Cintas Transportadoras | Cinta transportadora material<br>graba<br>(1 traspaso) | 0,2260 | 0,2260 | 0,6164 | 0,0825 | 0,0825 | 0,2250 |
| Cintas Transportadoras<br>Cintas Transportadoras | Cinta transportadora material<br>gravilla<br>(1 traspaso) | 0,2260 | 0,2260 | 0,6164 | 0,0825 | 0,0825 | 0,2250 |
| Cintas Transportadoras<br>Cintas Transportadoras | Cinta transportadora material<br>grueso<br>(1 traspaso) | 0,2260 | 0,2260 | 0,6164 | 0,0825 | 0,0825 | 0,2250 |
| Cintas Transportadoras<br>Cintas Transportadoras | Cinta transportadora al<br>harnero secundario<br>(1 traspaso) | 0,2260 | 0,2260 | 0,6164 | 0,0825 | 0,0825 | 0,2250 |
| Cintas Transportadoras<br>Cintas Transportadoras | Cinta transportadora acopio<br>arena<br>(1 traspaso) | 0,2260 | 0,2260 | 0,6164 | 0,0825 | 0,0825 | 0,2250 |

<!-- Estadísticas: 22 filas, 8 columnas -->
<!-- Contexto posterior: -->
<!-- Informe de Emisiones Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 50 |Erosión en Pilas|Acopio de material grueso|0,1521|0,0228|0,3041|0,0555|0,0083|0,1110| -->
<!-- FIN TABLA 38 -->

Tabla 39: Factores de Emisión (MP10, MP2.5 y MPS) - Actividades Etapa de Cierre ....................... 51

<!-- INICIO TABLA 39 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Erosión en Pilas|Acopio de material graba|0,1521|0,0228|0,3041|0,0555|0,0083|0,1110| |Erosión en Pilas|Acopio de material gravilla|0,1521|0,0228|0,3041|0,0555|0,0083|0,1110| |Erosión en Pilas|Acopio de material arena|0,1521|0,0228|0,3041|0,0555|0,0083|0,1110| |**TOTALES EMISIONES ETAPA DE OPERACIÓN**|**TOTALES EMISIONES ETAPA DE OPERACIÓN**|**134,62**|**65,37**|**678,01**|**48,84**|**23,83**|**246,51**| -->

**Tabla 39: Factores de Emisión (MP10, MP2.5 y MPS) - Actividades Etapa de Cierre****

| ACTIVIDAD | Actividad Específica | Emisiones Diarias (kg/día) | Col4 | Col5 | Emisiones Anuales (ton/año) | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ACTIVIDAD | Actividad Específica | Emisiones<br>PM10 | Emisiones<br>PM2.5 | Emisiones<br>MPS | Emisiones<br>PM10 | Emisiones<br>PM2.5 | Emisiones<br>MPS |
| Reperfilado | Reperfilamiento área Planta | 3,8154 | 0,5342 | 5,0873 | 0,0038 | 0,0005 | 0,0051 |
| Reperfilado | Reperfilamiento área Camino | 16,0248 | 2,2435 | 21,3665 | 0,0160 | 0,0022 | 0,0214 |
| Tránsito Por Caminos<br>Pavimentados | Transporte Equipos Planta | 1,6351 | 0,3956 | 8,5182 | 0,1472 | 0,0356 | 0,7666 |
| Tránsito Por Caminos<br>Pavimentados | Transporte Estructura<br>Pesada | 4,9052 | 1,1868 | 25,5547 | 0,4415 | 0,1068 | 2,2999 |
| Tránsito Por Caminos<br>Pavimentados | Camión Grúa Para Montaje e<br>Instalación | 1,6351 | 0,3956 | 8,5182 | 0,1472 | 0,0356 | 0,7666 |
| Tránsito Por Caminos<br>Pavimentados | Transporte Petróleo | 1,6351 | 0,3956 | 8,5182 | 0,1472 | 0,0356 | 0,7666 |
| Tránsito Por Caminos<br>Pavimentados | Transporte Agua Potable | 1,6351 | 0,3956 | 8,5182 | 0,1472 | 0,0356 | 0,7666 |
| Tránsito Por Caminos<br>Pavimentados | Transporte de Personal y<br>Supervisión | 0,2357 | 0,0570 | 1,2278 | 0,0212 | 0,0051 | 0,1105 |
| Transito Vehículos<br>Livianos Por Caminos<br>No Pavimentados | Transporte de Personal y<br>Supervisión | 1,9644 | 0,1964 | 6,4170 | 0,1768 | 0,0177 | 0,5775 |
| Transito Vehículos<br>Pesados<br>Por Caminos No<br>Pavimentados | Transporte Equipos Planta | 2,7732 | 0,2773 | 9,0591 | 0,2496 | 0,0250 | 0,8153 |
| Transito Vehículos<br>Pesados<br>Por Caminos No<br>Pavimentados | Transporte Estructura<br>Pesada | 8,3196 | 0,8320 | 27,1774 | 0,7488 | 0,0749 | 2,4460 |
| Transito Vehículos<br>Pesados<br>Por Caminos No<br>Pavimentados | Camión Grúa Para Montaje e<br>Instalación | 2,7732 | 0,2773 | 9,0591 | 0,2496 | 0,0250 | 0,8153 |
| Transito Vehículos<br>Pesados<br>Por Caminos No<br>Pavimentados | Transporte Petróleo | 2,7732 | 0,2773 | 9,0591 | 0,2496 | 0,0250 | 0,8153 |
| Transito Vehículos<br>Pesados<br>Por Caminos No<br>Pavimentados | Transporte Agua Potable | 2,7732 | 0,2773 | 9,0591 | 0,2496 | 0,0250 | 0,8153 |
| **TOTALES EMISIONES ETAPA DE CIERRE** | **TOTALES EMISIONES ETAPA DE CIERRE** | **52,90** | **7,74** | **157,14** | **3,00** | **0,45** | **11,79** |

<!-- Estadísticas: 16 filas, 8 columnas -->
<!-- Contexto posterior: -->
<!-- Informe de Emisiones Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 51 **Tabla 40: Emisiones de Gases y MP Combustión de Motores [kg/día] - Etapa de Construcción** -->
<!-- FIN TABLA 39 -->

Tabla 40: Emisiones de Gases y MP Combustión de Motores [kg/día] - Etapa de Construcción ....... 52

<!-- INICIO TABLA 40 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |**TOTALES EMISIONES ETAPA DE CIERRE**|**TOTALES EMISIONES ETAPA DE CIERRE**|**52,90**|**7,74**|**157,14**|**3,00**|**0,45**|**11,79**| Informe de Emisiones Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 51 -->

**Tabla 40: Emisiones de Gases y MP Combustión de Motores [kg/día] - Etapa de Construcción****

| Emisiones de Gases y Material Particulado Asociado a la Combustión de Motores [kg/día] | Col2 | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Equipo | Cantidad | Potencia<br>Nominal kw | Operación<br>Diaria (horas) | CO | HC | NOx | MP |
| Motoniveladora | 1 | 137 | 12 | 0,04 | 0,02 | 0,17 | 0,01 |
| **TOTAL** | **TOTAL** | **TOTAL** | **TOTAL** | **0,04** | **0,02** | **0,17** | **0,01** |

<!-- Estadísticas: 3 filas, 8 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 41: Emisiones de Gases y MP Combustión de Motores [kg/día] - Etapa de Operación** |Emisiones de Gases y Material Particulado Asociado a la Combustión de Motores [kg/día]|Col2|Col3|Col4|Col5|Col6|Col7|Col8| |---|---|---|---|---|---|---|---| -->
<!-- FIN TABLA 40 -->

Tabla 41: Emisiones de Gases y MP Combustión de Motores [kg/día] - Etapa de Operación ........... 52

<!-- INICIO TABLA 41 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |---|---|---|---|---|---|---|---| |Equipo|Cantidad|Potencia<br>Nominal kw|Operación<br>Diaria (horas)|CO|HC|NOx|MP| |Motoniveladora|1|137|12|0,04|0,02|0,17|0,01| |**TOTAL**|**TOTAL**|**TOTAL**|**TOTAL**|**0,04**|**0,02**|**0,17**|**0,01**| -->

**Tabla 41: Emisiones de Gases y MP Combustión de Motores [kg/día] - Etapa de Operación****

| Emisiones de Gases y Material Particulado Asociado a la Combustión de Motores [kg/día] | Col2 | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Equipo | Cantidad | Potencia<br>Nominal kw | Operación<br>Diaria (horas) | CO | HC | NOx | MP |
| Excavadora de 1.5 m3 | 1 | 120 | 12 | 0,05 | 0,02 | 0,17 | 0,01 |
| Cargador Frontal W190B | 1 | 160 | 12 | 0,04 | 0,02 | 0,17 | 0,01 |
| Cargador Frontal 721E | 1 | 160 | 12 | 0,04 | 0,02 | 0,17 | 0,01 |
| **TOTAL** | **TOTAL** | **TOTAL** | **TOTAL** | **0,117** | **0,053** | **0,517** | **0,041** |

<!-- Estadísticas: 5 filas, 8 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 42: Emisiones de Gases y MP Combustión de Motores [kg/día] - Etapa de Cierre** |Equipo|Cantidad|Potencia<br>Nominal kw|Operación<br>Diaria (horas)|CO|HC|NOx|MP| |---|---|---|---|---|---|---|---| -->
<!-- FIN TABLA 41 -->

Tabla 42: Emisiones de Gases y MP Combustión de Motores [kg/día] - Etapa de Cierre .................. 52

<!-- INICIO TABLA 42 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Excavadora de 1.5 m3|1|120|12|0,05|0,02|0,17|0,01| |Cargador Frontal W190B|1|160|12|0,04|0,02|0,17|0,01| |Cargador Frontal 721E|1|160|12|0,04|0,02|0,17|0,01| |**TOTAL**|**TOTAL**|**TOTAL**|**TOTAL**|**0,117**|**0,053**|**0,517**|**0,041**| -->

**Tabla 42: Emisiones de Gases y MP Combustión de Motores [kg/día] - Etapa de Cierre****

| Vehículo | N°<br>Viajes/día | Distancia<br>(km) | Velocidad<br>km/h | CO | HC | NOx | MP |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Camión Transporte Petróleo | 1 | 51,5 | 100 | 0,133 | 0,021 | 0,584 | 0,011 |
| Camión Transporte Equipos Planta | 1 | 51,5 | 100 | 0,133 | 0,021 | 0,584 | 0,011 |
| Camión Transporte Estructura Pesada | 3 | 51,5 | 100 | 0,398 | 0,063 | 1,752 | 0,033 |
| Camión Grúa Para Montaje e<br>Instalación | 1 | 51,5 | 100 | 0,133 | 0,021 | 0,584 | 0,011 |
| Camión Transporte Agua Potable | 1 | 51,5 | 100 | 0,133 | 0,021 | 0,584 | 0,011 |
| Camionetas Transporte Personal y<br>Supervisión | 2 | 51,5 | 100 | 0,119 | 0,014 | 0,217 | 0,021 |
| **TOTALES** | **TOTALES** | **TOTALES** | **TOTALES** | **1,048** | **0,161** | **4,306** | **0,099** |

<!-- Estadísticas: 7 filas, 8 columnas -->
<!-- Contexto posterior: -->
<!-- Informe de Emisiones Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 52 **Tabla 44: Emisiones de Gases y MP Asociado a Vehículos [kg/día] - Etapa de Operación** -->
<!-- FIN TABLA 42 -->

Tabla 43: Emisiones de Gases y MP Asociado a Vehículos [kg/día] - Etapa de Construcción ........... 52
Tabla 44: Emisiones de Gases y MP Asociado a Vehículos [kg/día] - Etapa de Operación ............... 53

<!-- INICIO TABLA 44 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |**TOTALES**|**TOTALES**|**TOTALES**|**TOTALES**|**1,048**|**0,161**|**4,306**|**0,099**| Informe de Emisiones Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 52 -->

**Tabla 44: Emisiones de Gases y MP Asociado a Vehículos [kg/día] - Etapa de Operación****

| Vehículo | N°<br>Viajes/día | Distancia<br>(km) | Velocidad<br>km/h | CO | HC | NOx | MP |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Camión Transporte Áridos | 55 | 0,6 | 50 | 0,111 | 0,024 | 0,443 | 0,010 |
| Camión Transporte Petróleo | 1 | 51,5 | 100 | 0,133 | 0,021 | 0,584 | 0,011 |
| Camión Transporte Agua Potable | 1 | 51,5 | 100 | 0,133 | 0,021 | 0,584 | 0,011 |
| Camión Transporte Residuos Varios | 1 | 51,5 | 100 | 0,133 | 0,021 | 0,584 | 0,011 |
| Camionetas Transporte Personal y<br>Supervisión | 2 | 51,5 | 100 | 0,056 | 0,015 | 0,179 | 0,008 |
| **TOTALES** | **TOTALES** | **TOTALES** | **TOTALES** | **0,322** | **0,057** | **1,348** | **0,031** |

<!-- Estadísticas: 6 filas, 8 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 45: Emisiones de Gases y MP Asociado a Vehículos [kg/día] - Etapa de Cierre** |Vehículo|N°<br>Viajes/día|Distancia<br>(km)|Velocidad<br>km/h|CO|HC|NOx|MP| |---|---|---|---|---|---|---|---| -->
<!-- FIN TABLA 44 -->

Tabla 45: Emisiones de Gases y MP Asociado a Vehículos [kg/día] - Etapa de Cierre ...................... 53

<!-- INICIO TABLA 45 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Camión Transporte Agua Potable|1|51,5|100|0,133|0,021|0,584|0,011| |Camión Transporte Residuos Varios|1|51,5|100|0,133|0,021|0,584|0,011| |Camionetas Transporte Personal y<br>Supervisión|2|51,5|100|0,056|0,015|0,179|0,008| |**TOTALES**|**TOTALES**|**TOTALES**|**TOTALES**|**0,322**|**0,057**|**1,348**|**0,031**| -->

**Tabla 45: Emisiones de Gases y MP Asociado a Vehículos [kg/día] - Etapa de Cierre****

| Vehículo | N°<br>Viajes/día | Distancia<br>(km) | Velocidad<br>km/h | CO | HC | NOx | MP |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Camión Transporte Petróleo | 1 | 51,5 | 100 | 0,133 | 0,021 | 0,584 | 0,011 |
| Camión Transporte Equipos Planta | 1 | 51,5 | 100 | 0,133 | 0,021 | 0,584 | 0,011 |
| Camión Transporte Estructura Pesada | 3 | 51,5 | 100 | 0,398 | 0,063 | 1,752 | 0,033 |
| Camión Grúa Para Desmontaje de<br>~~Instalación~~ | 1 | 51,5 | 100 | 0,133 | 0,021 | 0,584 | 0,011 |
| Camión Transporte Agua Potable | 1 | 51,5 | 100 | 0,133 | 0,021 | 0,584 | 0,011 |
| Camionetas Transporte Personal y<br>Supervisión | 2 | 51,5 | 100 | 0,119 | 0,014 | 0,217 | 0,021 |
| **TOTALES** | **TOTALES** | **TOTALES** | **TOTALES** | **1,048** | **0,161** | **4,306** | **0,099** |

<!-- Estadísticas: 7 filas, 8 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 46: Emisiones de Gases y Material Particulado Asociado a Combustión en Grupos** **Generadores** -->
<!-- FIN TABLA 45 -->

Tabla 46: Emisiones de Gases y Material Particulado Asociado a Combustión en Grupos

<!-- INICIO TABLA 46 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Camión Grúa Para Desmontaje de<br>~~Instalación~~|1|51,5|100|0,133|0,021|0,584|0,011| |Camión Transporte Agua Potable|1|51,5|100|0,133|0,021|0,584|0,011| |Camionetas Transporte Personal y<br>Supervisión|2|51,5|100|0,119|0,014|0,217|0,021| |**TOTALES**|**TOTALES**|**TOTALES**|**TOTALES**|**1,048**|**0,161**|**4,306**|**0,099**| -->

**Tabla 46: Emisiones de Gases y Material Particulado Asociado a Combustión en Grupos****

| Etapa Proyecto | Potencia<br>(kw) | Combustibles<br>(tipo) | Operación<br>(h/día) | Cantidad | CO | NOx | MP<br>10 | SOx |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Construcción | 480 | Diésel | 12 | 1 | 23,39 | 108,29 | 7,72 | 7,20 |
| Operación | 480 | Diésel | 12 | 1 | 23,39 | 108,29 | 7,72 | 7,20 |
| Cierre | 480 | Diésel | 12 | 1 | 23,39 | 108,29 | 7,72 | 7,20 |

<!-- Estadísticas: 3 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Informe de Emisiones Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 53 **TABLAS RESUMEN DE EMISIONES POR FASES DEL PROYECTO** -->
<!-- FIN TABLA 46 -->


Generadores ......................................................................................................................... 53

Tabla 47: Resumen Emisiones Fase de Construcción ........................................................................ 54

<!-- INICIO TABLA 47 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Informe de Emisiones Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 53 **TABLAS RESUMEN DE EMISIONES POR FASES DEL PROYECTO** -->

**Tabla 47: Resumen Emisiones Fase de Construcción****

| Fase de Construcción | MP10 | Col3 | MP2,5 | Col5 | MPS | Col7 | CO | Col9 | HC | Col11 | NOx | Col13 | SO<br>X | Col15 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Fase de Construcción** | kg/día | ton/año | kg/día | ton/año | kg/día | ton/año | kg/día | ton/año | kg/día | ton/año | kg/día | ton/año | kg/día | ton/año |
| Actividades | 33,11 | 0,33 | 4,97 | 0,04 | 130,75 | 1,20 | --- | --- | --- | --- | --- | --- | --- | --- |
| Maquinarias | --- | --- | --- | --- | 0,01 | 0,00 | 0,04 | 0,00 | 0,02 | 0,00 | 0,17 | 0,02 | --- | --- |
| Vehículos | --- | --- | --- | --- | 0,10 | 0,01 | 1,05 | 0,09 | 0,16 | 0,01 | 4,31 | 0,39 | --- | --- |
| Generadores | 7,72 | 0,69 | --- | --- | --- | --- | 23,39 | 2,11 | --- | --- | 108,29 | 9,75 | 7,20 | 0,65 |
| **TOTAL** | **40,83** | **1,02** | **4,97** | **0,04** | **130,86** | **1,21** | **24,47** | **2,20** | **0,18** | **0,02** | **112,77** | **10,15** | **7,20** | **0,65** |

<!-- Estadísticas: 6 filas, 15 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 48: Resumen Emisiones Fase de Operación** |Fase de Construcción|MP10|Col3|MP2,5|Col5|MPS|Col7|CO|Col9|HC|Col11|NOx|Col13|SO<br>X|Col15| |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---| -->
<!-- FIN TABLA 47 -->


Tabla 48: Resumen Emisiones Fase de Operación ............................................................................. 54

<!-- INICIO TABLA 48 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Maquinarias|---|---|---|---|0,01|0,00|0,04|0,00|0,02|0,00|0,17|0,02|---|---| |Vehículos|---|---|---|---|0,10|0,01|1,05|0,09|0,16|0,01|4,31|0,39|---|---| |Generadores|7,72|0,69|---|---|---|---|23,39|2,11|---|---|108,29|9,75|7,20|0,65| |**TOTAL**|**40,83**|**1,02**|**4,97**|**0,04**|**130,86**|**1,21**|**24,47**|**2,20**|**0,18**|**0,02**|**112,77**|**10,15**|**7,20**|**0,65**| -->

**Tabla 48: Resumen Emisiones Fase de Operación****

| Fase de Construcción | MP10 | Col3 | MP2,5 | Col5 | MPS | Col7 | CO | Col9 | HC | Col11 | NOx | Col13 | SO<br>X | Col15 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Fase de Construcción** | kg/día | ton/año | kg/día | ton/año | kg/día | ton/año | kg/día | ton/año | kg/día | ton/año | kg/día | ton/año | kg/día | ton/año |
| Actividades | 134,62 | 48,84 | 65,37 | 23,83 | 678,01 | 246.51 | --- | --- | --- | --- | --- | --- | --- | --- |
| Maquinarias | --- | --- | --- | --- | 0,04 | 0,01 | 0,12 | 0,04 | 0,05 | 0,02 | 0,52 | 0,19 | --- | --- |
| Vehículos | --- | --- | --- | --- | 0,03 | 0,01 | 0,32 | 0,12 | 0,06 | 0,02 | 1,35 | 0,49 | --- | --- |
| Generadores | 7,72 | 2,82 | --- | --- | --- | --- | 23,39 | 8,54 | --- | --- | 108,29 | 39,53 | 7,20 | 2,63 |
| **TOTAL** | **142,34** | **51,66** | **65,37** | **23,83** | **678,08** | **0,03** | **23,83** | **8,70** | **0,11** | **0,04** | **110,16** | **40,21** | **7,20** | **2,63** |

<!-- Estadísticas: 6 filas, 15 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 49: Resumen Emisiones Fase de Cierre** |Fase de Construcción|MP10|Col3|MP2,5|Col5|MPS|Col7|CO|Col9|HC|Col11|NOx|Col13|SO<br>X|Col15| |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---| -->
<!-- FIN TABLA 48 -->


Tabla 49: Resumen Emisiones Fase de Cierre ................................................................................... 54

<!-- INICIO TABLA 49 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Maquinarias|---|---|---|---|0,04|0,01|0,12|0,04|0,05|0,02|0,52|0,19|---|---| |Vehículos|---|---|---|---|0,03|0,01|0,32|0,12|0,06|0,02|1,35|0,49|---|---| |Generadores|7,72|2,82|---|---|---|---|23,39|8,54|---|---|108,29|39,53|7,20|2,63| |**TOTAL**|**142,34**|**51,66**|**65,37**|**23,83**|**678,08**|**0,03**|**23,83**|**8,70**|**0,11**|**0,04**|**110,16**|**40,21**|**7,20**|**2,63**| -->

**Tabla 49: Resumen Emisiones Fase de Cierre****

| Fase de Construcción | MP10 | Col3 | MP2,5 | Col5 | MPS | Col7 | CO | Col9 | HC | Col11 | NOx | Col13 | SO<br>X | Col15 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Fase de Construcción** | kg/día | ton/año | kg/día | ton/año | kg/día | ton/año | kg/día | ton/año | kg/día | ton/año | kg/día | ton/año | kg/día | ton/año |
| Actividades | 33,66 | 3,03 | 5,05 | 0,45 | 131,49 | 11.86 | --- | --- | --- | --- | --- | --- | --- | --- |
| Maquinarias | --- | --- | --- | --- | 0,01 | 0,00 | 0,04 | 0,00 | 0,02 | 0,00 | 0,17 | 0,02 |  |  |
| Vehículos | --- | --- | --- | --- | 0,10 | 0,01 | 1,05 | 0,09 | 0,16 | 0,01 | 4,31 | 0,39 |  |  |
| Generadores | 7,72 | 0,69 | --- | --- | --- | --- | 23,39 | 2,11 | --- | --- | 108,29 | 9,75 | 7,20 | 0,65 |
| **TOTAL** | **41,38** | **3,72** | **5,05** | **0,45** | **131,60** | **0,01** | **24,47** | **2,20** | **0,18** | **0,02** | **112,77** | **10,15** | **7,20** | **0,65** |

<!-- Estadísticas: 6 filas, 15 columnas -->
<!-- Contexto posterior: -->
<!-- Informe de Emisiones Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 54 **11. RESULTADOS DE LA MODELACIÓN** -->
<!-- FIN TABLA 49 -->


Tabla 50: Aportes del Proyecto Etapa de Construcción ...................................................................... 56

<!-- INICIO TABLA 50 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- los receptores y su nivel respecto de la norma respectiva: Informe de Emisiones Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 55 -->

**Tabla 50: Aportes del Proyecto Etapa de Construcción****

| Parámetro | Estadístico | Limite Norma<br>(μg/m3N) | Concentración<br>(μg/m3N)<br>Calama | % Respecto<br>de la Norma | Concentración<br>(μg/m3N)<br>San Pedro | % Respecto<br>de la Norma | Concentración<br>(μg/m3N)<br>Chiu-Chiu | % Respecto<br>de la Norma |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MP10 | Percentil 98 Promedio 24 horas | 150 | 0,07760 | **0,1** | 0,01650 | **0,0** | 0,00616 | **0,0** |
| MP10 | Promedio Anual | 50 | 0,01430 | **0,0** | 0,00201 | **0,0** | 0,00067 | **0,0** |
| MP2,5 | Percentil 98 Promedio Diario | 50 | 0,01900 | **0,0** | 0,00100 | **0,0** | 0,00100 | **0,0** |
| MP2,5 | Promedio Trianual | 20 | 0,00300 | **0,0** | 0,00000 | **0,0** | 0,00000 | **0,0** |
| CO | Percentil 99, máx. 1 hora | 30000 | 0,04990 | **0,0** | 0,09370 | **0,0** | 0,04160 | **0,0** |
| CO | Percentil 99, máx. 8 hora | 10000 | 0,01210 | **0,0** | 0,04630 | **0,0** | 0,01020 | **0,0** |
| NO2 | Percentil 99, máx. 1 hora | 400 | 0,16500 | **0,0** | 0,32000 | **0,1** | 0,12300 | **0,0** |
| NO2 | Promedio, Anual | 100 | 0,00221 | **0,0** | 0,00983 | **0,0** | 0,00122 | **0,0** |
| SO2 | Promedio Diario, percentil 99 | 250 | 0,00067 | **0,0** | 0,00288 | **0,0** | 0,00044 | **0,0** |
| SO2 | Promedio, Anual | 80 | 0,00007 | **0,0** | 0,00035 | **0,0** | 0,00004 | **0,0** |

<!-- Estadísticas: 10 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 51: Aportes del Proyecto Etapa de Operación** |Parámetro|Estadístico|Limite Norma<br>(μg/m3N)|Concentración<br>(μg/m3N)<br>Calama|% Respecto<br>de la Norma|Concentración<br>(μg/m3N)<br>San Pedro|% Respecto<br>de la Norma|Concentración<br>(μg/m3N)<br>Chiu-Chiu|% Respecto<br>de la Norma| |---|---|---|---|---|---|---|---|---| -->
<!-- FIN TABLA 50 -->

Tabla 51: Aportes del Proyecto Etapa de Operación ........................................................................... 56

<!-- INICIO TABLA 51 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |NO2|Percentil 99, máx. 1 hora|400|0,16500|**0,0**|0,32000|**0,1**|0,12300|**0,0**| |NO2|Promedio, Anual|100|0,00221|**0,0**|0,00983|**0,0**|0,00122|**0,0**| |SO2|Promedio Diario, percentil 99|250|0,00067|**0,0**|0,00288|**0,0**|0,00044|**0,0**| |SO2|Promedio, Anual|80|0,00007|**0,0**|0,00035|**0,0**|0,00004|**0,0**| -->

**Tabla 51: Aportes del Proyecto Etapa de Operación****

| Parámetro | Estadístico | Limite Norma<br>(μg/m3N) | Concentración<br>(μg/m3N)<br>Calama | % Respecto<br>de la Norma | Concentración<br>(μg/m3N)<br>San Pedro | % Respecto<br>de la Norma | Concentración<br>(μg/m3N)<br>Chiu-Chiu | % Respecto<br>de la Norma |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MP10 | Percentil 98 Promedio 24 horas | 150 | 0,17000 | **0,1** | 0,72200 | **0,5** | 0,11200 | **0,1** |
| MP10 | Promedio Anual | 50 | 0,02060 | **0,0** | 0,07620 | **0,2** | 0,01090 | **0,0** |
| MP2,5 | Percentil 98 Promedio Diario | 50 | 0,15100 | **0,3** | 0,66100 | **1,3** | 0,10100 | **0,2** |
| MP2,5 | Promedio Trianual | 20 | 0,01720 | **0,1** | 0,06940 | **0,3** | 0,00981 | **0,0** |
| CO | Percentil 99, máx. 1 hora | 30000 | 0,26400 | **0,0** | 0,47200 | **0,0** | 0,22100 | **0,0** |
| CO | Percentil 99, máx. 8 hora | 10000 | 0,09040 | **0,0** | 0,22700 | **0,0** | 0,05560 | **0,0** |
| NO2 | Percentil 99, máx. 1 hora | 400 | 0,81100 | **0,2** | 1,54000 | **0,4** | 0,59200 | **0,1** |

<!-- Estadísticas: 7 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Informe de Emisiones Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 56 |NO2|Promedio, Anual|100|0,01220|0,0|0,04170|0,0|0,00660|0,0| -->
<!-- FIN TABLA 51 -->

Tabla 52: Aportes del Proyecto Etapa de Cierre .................................................................................. 57

<!-- INICIO TABLA 52 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |NO2|Promedio, Anual|100|0,01220|0,0|0,04170|0,0|0,00660|0,0| |---|---|---|---|---|---|---|---|---| |SO2|Promedio Diario, percentil 99|250|0,00067|**0,0**|0,00288|**0,0**|0,00044|**0,0**| |SO2|Promedio, Anual|80|0,00008|**0,0**|0,00032|**0,0**|0,00005|**0,0**| -->

**Tabla 52: Aportes del Proyecto Etapa de Cierre****

| Parámetro | Estadístico | Limite Norma<br>(μg/m3N) | Concentración<br>(μg/m3N)<br>Calama | % Respecto<br>de la Norma | Concentración<br>(μg/m3N)<br>San Pedro | % Respecto<br>de la Norma | Concentración<br>(μg/m3N)<br>Chiu-Chiu | % Respecto<br>de la Norma |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MP10 | Percentil 98 Promedio 24 horas | 150 | 0,07760 | **0,1** | 0,01650 | **0,0** | 0,00616 | **0,0** |
| MP10 | Promedio Anual | 50 | 0,01430 | **0,0** | 0,00201 | **0,0** | 0,00067 | **0,0** |
| MP2,5 | Percentil 98 Promedio Diario | 50 | 0,01880 | **0,0** | 0,00146 | **0,0** | 0,00135 | **0,0** |
| MP2,5 | Promedio Trianual | 20 | 0,00342 | **0,0** | 0,00019 | **0,0** | 0,00013 | **0,0** |
| CO | Percentil 99, máx. 1 hora | 30000 | 0,05080 | **0,0** | 0,09540 | **0,0** | 0,04230 | **0,0** |
| CO | Percentil 99, máx. 8 hora | 10000 | 0,01230 | **0,0** | 0,04710 | **0,0** | 0,01040 | **0,0** |
| NO2 | Percentil 99, máx. 1 hora | 400 | 0,16900 | **0,0** | 0,32600 | **0,1** | 0,12600 | **0,0** |
| NO2 | Promedio, Anual | 100 | 0,00225 | **0,0** | 0,01000 | **0,0** | 0,00124 | **0,0** |
| SO2 | Promedio Diario, percentil 99 | 250 | 0,00067 | **0,0** | 0,00288 | **0,0** | 0,00044 | **0,0** |
| SO2 | Promedio, Anual | 80 | 0,00007 | **0,0** | 0,00035 | **0,0** | 0,00004 | **0,0** |

<!-- Estadísticas: 10 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Informe de Emisiones Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 57 **11.1.2 Cumplimiento Normas De Calidad Ambiental Secundaria** -->
<!-- FIN TABLA 52 -->

Tabla 53: Aportes del Proyecto Etapa de Construcción ...................................................................... 58

<!-- INICIO TABLA 53 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Informe de Emisiones Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 57 **11.1.2 Cumplimiento Normas De Calidad Ambiental Secundaria** -->

**Tabla 53: Aportes del Proyecto Etapa de Construcción****

| Parámetro | Estadístico | Limite Norma | Aporte en<br>Calama | % Respecto<br>de la Norma | Aporte en San<br>Pedro | % Respecto<br>de la Norma | Aporte en<br>Chiu-Chiu | % Respecto<br>de la Norma |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MPS | Promedio Mensual | 150 | 0.002 | **0,0** | 0.0003 | **0,0** | 0.0001 | **0,0** |
| MPS | Promedio Anual | 100 | 0.0005 | **0,0** | 0.00004 | **0,0** | 0.00002 | **0,0** |
| SO2 | Promedio Anual | 80 | 0,00007 | **0,0** | 0,00035 | **0,0** | 0,00004 | **0,0** |
| SO2 | Percentil 99.7 Concentración Diaria | 365 | 0,00067 | **0,0** | 0,00288 | **0,0** | 0,00044 | **0,0** |
| SO2 | Percentil 99.73 Concentración 1 hora | 1000 | 0,00561 | **0,0** | 0,01120 | **0,0** | 0,00423 | **0,0** |

<!-- Estadísticas: 5 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Nota 1: Los aportes de MPS en cada uno de los receptores, se expresan en mg/m [2] día Nota 2: Los aportes de SO 2 en cada uno de los receptores, se expresan en μ g/m [3] N -->
<!-- FIN TABLA 53 -->

Tabla 54: Aportes del Proyecto Etapa de Operación ........................................................................... 58

<!-- INICIO TABLA 54 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Nota 1: Los aportes de MPS en cada uno de los receptores, se expresan en mg/m [2] día Nota 2: Los aportes de SO 2 en cada uno de los receptores, se expresan en μ g/m [3] N -->

**Tabla 54: Aportes del Proyecto Etapa de Operación****

| Parámetro | Estadístico | Limite Norma | Aporte en<br>Calama | % Respecto<br>de la Norma | Aporte en San<br>Pedro | % Respecto<br>de la Norma | Aporte en<br>Chiu-Chiu | % Respecto<br>de la Norma |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MPS | Promedio Mensual | 150 | 0.007 | **0,0** | 0.036 | **0,0** | 0.004 | **0,0** |
| MPS | Promedio Anual | 100 | 0.001 | **0,0** | 0.003 | **0,0** | 0.0005 | **0,0** |
| SO2 | Promedio Anual | 80 | 0,00008 | **0,0** | 0,00032 | **0,0** | 0,00005 | **0,0** |
| SO2 | Percentil 99.7 Concentración Diaria | 365 | 0,00067 | **0,0** | 0,00288 | **0,0** | 0,00044 | **0,0** |
| SO2 | Percentil 99.73 Concentración 1 hora | 1000 | 0,00561 | **0,0** | 0,01120 | **0,0** | 0,00423 | **0,0** |

<!-- Estadísticas: 5 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Nota 1: Los aportes de MPS en cada uno de los receptores, se expresan en mg/m [2] día Nota 2: Los aportes de SO 2 en cada uno de los receptores, se expresan en μ g/m [3] N -->
<!-- FIN TABLA 54 -->

Tabla 55: Aportes del Proyecto Etapa de Cierre .................................................................................. 59

<!-- INICIO TABLA 55 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Nota 2: Los aportes de SO 2 en cada uno de los receptores, se expresan en μ g/m [3] N Informe de Emisiones Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 58 -->

**Tabla 55: Aportes del Proyecto Etapa de Cierre****

| Parámetro | Estadístico | Limite Norma | Aporte en<br>Calama | % Respecto<br>de la Norma | Aporte en San<br>Pedro | % Respecto<br>de la Norma | Aporte en<br>Chiu-Chiu | % Respecto<br>de la Norma |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MPS | Promedio Mensual | 150 | 0.002 | **0,0** | 0.0003 | **0,0** | 0.0001 | **0,0** |
| MPS | Promedio Anual | 100 | 0.0005 | **0,0** | 0.00004 | **0,0** | 0.00002 | **0,0** |
| SO2 | Promedio Anual | 80 | 0,00225 | **0,0** | 0,01000 | **0,0** | 0,00124 | **0,0** |
| SO2 | Percentil 99.7 Concentración Diaria | 365 | 0,00067 | **0,0** | 0,00288 | **0,0** | 0,00044 | **0,0** |
| SO2 | Percentil 99.73 Concentración 1 hora | 1000 | 0,00561 | **0,0** | 0,01120 | **0,0** | 0,00423 | **0,0** |

<!-- Estadísticas: 5 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Nota 1: Los aportes de MPS en cada uno de los receptores, se expresan en mg/m [2] día Nota 2: Los aportes de SO 2 en cada uno de los receptores, se expresan en μ g/m [3] N -->
<!-- FIN TABLA 55 -->

Tabla 56: Velocidad promedio del Viento en m/s ................................................................................. 61

<!-- INICIO TABLA 56 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- versus las representadas por el modelo (valor modelado) se tiene que: Informe de Emisiones Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 60 -->

**Tabla 56: Velocidad promedio del Viento en m/s****

| Estación | Promedio Observado | Promedio Pronostico<br>WRF | % de Variación |
| --- | --- | --- | --- |
| Estación Centro | 2.97 | 3.35 | 12.8 |

<!-- Estadísticas: 1 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- _% Error_ _V_ = % de error entre los valores modelado y observado de la velocidad del viento. (Valor modelado) = 3.35 m/s -->
<!-- FIN TABLA 56 -->

Tabla 57: Puntos de Máximo Impacto - Etapa de Construcción ......................................................... 63

<!-- INICIO TABLA 57 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- De acuerdo con los resultados de la modelación, los puntos de máximo impacto generados por el proyecto en la etapa de operación (etapa en la que se generan las máximas emisiones), se localizan en las siguientes coordenadas UTM WGS84: -->

**Tabla 57: Puntos de Máximo Impacto - Etapa de Construcción****

| Parámetro | Estadístico | Coordenada WGS-84 | Col4 | Concentración<br>(μg/m3N) |
| --- | --- | --- | --- | --- |
| Parámetro | Estadístico | Este | Norte | Norte |
| MP10 | Percentil 98 Promedio 24 horas | 552136 | 7492499 | 9.12 |
| MP10 | Promedio Anual | 552136 | 7492499 | 1.55 |
| MP2,5 | Percentil 98 Promedio Diario | 552136 | 7492499 | 0.93 |
| MP2,5 | Promedio Trianual | 552136 | 7492499 | 0.15 |
| CO | Percentil 99, máx. 1 hora | 552136 | 7492499 | 171.3 |
| CO | Percentil 99, máx. 8 hora | 552136 | 7492499 | 36.02 |
| NO2 | Percentil 99, máx. 1 hora | 552136 | 7492499 | 557.26 |
| NO2 | Promedio, Anual | 552136 | 7492499 | 9.15 |
| SO2 | Percentil 99.73 Conc. 1 hora | 552136 | 7492499 | 5.12 |
| SO2 | Promedio Diario, percentil 99 | 552136 | 7492499 | 0.49 |
| SO2 | Promedio, Anual | 552136 | 7492499 | 0.1 |

<!-- Estadísticas: 12 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- Informe de Emisiones Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 63 **Tabla 58: Puntos de Máximo Impacto - Etapa de Operación** -->
<!-- FIN TABLA 57 -->

Tabla 58: Puntos de Máximo Impacto - Etapa de Operación.............................................................. 64

<!-- INICIO TABLA 58 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |SO2|Promedio, Anual|552136|7492499|0.1| Informe de Emisiones Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 63 -->

**Tabla 58: Puntos de Máximo Impacto - Etapa de Operación****

| Parámetro | Estadístico | Coordenada WGS-84 | Col4 | Concentración<br>(μg/m3N) |
| --- | --- | --- | --- | --- |
| Parámetro | Estadístico | Este | Norte | Norte |
| MP10 | Percentil 98 Promedio 24 horas | 552136 | 7492499 | 321.49 |
| MP10 | Promedio Anual | 552136 | 7492499 | 54.14 |
| MP2,5 | Percentil 98 Promedio Diario | 552136 | 7492499 | 2.94 |
| MP2,5 | Promedio Trianual | 552136 | 7492499 | 44.54 |
| CO | Percentil 99, máx. 1 hora | 552136 | 7492499 | 1.629,5 |
| CO | Percentil 99, máx. 8 hora | 552136 | 7492499 | 332.89 |
| NO2 | Percentil 99, máx. 1 hora | 552136 | 7492499 | 5.367,3 |
| NO2 | Promedio, Anual | 552136 | 7492499 | 71.28 |
| SO2 | Percentil 99.73 Conc. 1 hora | 552136 | 7492499 | 5.12 |
| SO2 | Promedio Diario, percentil 99 | 552136 | 7492499 | 0.49 |
| SO2 | Promedio, Anual | 552136 | 7492499 | 0.09 |

<!-- Estadísticas: 12 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 59: Puntos de Máximo Impacto - Etapa de Cierre** |Parámetro|Estadístico|Coordenada WGS-84|Col4|Concentración<br>(μg/m3N)| |---|---|---|---|---| -->
<!-- FIN TABLA 58 -->

Tabla 59: Puntos de Máximo Impacto - Etapa de Cierre .................................................................... 64

<!-- INICIO TABLA 59 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |NO2|Promedio, Anual|552136|7492499|71.28| |SO2|Percentil 99.73 Conc. 1 hora|552136|7492499|5.12| |SO2|Promedio Diario, percentil 99|552136|7492499|0.49| |SO2|Promedio, Anual|552136|7492499|0.09| -->

**Tabla 59: Puntos de Máximo Impacto - Etapa de Cierre****

| Parámetro | Estadístico | Coordenada WGS-84 | Col4 | Concentración<br>(μg/m3N) |
| --- | --- | --- | --- | --- |
| Parámetro | Estadístico | Este | Norte | Norte |
| MP10 | Percentil 98 Promedio 24 horas | 552136 | 7492499 | 9.16 |
| MP10 | Promedio Anual | 552136 | 7492499 | 1.56 |
| MP2,5 | Percentil 98 Promedio Diario | 552136 | 7492499 | 0.93 |
| MP2,5 | Promedio Trianual | 552136 | 7492499 | 0.15 |
| CO | Percentil 99, máx. 1 hora | 552136 | 7492499 | 171.3 |
| CO | Percentil 99, máx. 8 hora | 552136 | 7492499 | 35.02 |
| NO2 | Percentil 99, máx. 1 hora | 552136 | 7492499 | 557.26 |
| NO2 | Promedio, Anual | 552136 | 7492499 | 9.23 |
| SO2 | Percentil 99.73 Conc. 1 hora | 552136 | 7492499 | 5.0 |
| SO2 | Promedio Diario, percentil 99 | 552136 | 7492499 | 0.49 |
| SO2 | Promedio, Anual | 552136 | 7492499 | 0.1 |

<!-- Estadísticas: 12 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- Informe de Emisiones Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 64 **14. CONCLUSIONES** -->
<!-- FIN TABLA 59 -->


Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 4

## INDICE DE FIGURAS

Figura 1: Rosa de Vientos ................................................................................................................... 11
Figura 2: Campo de vientos a las 00:00 h ........................................................................................... 12
Figura 3: Campo de vientos a las 02:00 h ........................................................................................... 12
Figura 4: Campo de vientos a las 04:00 h ........................................................................................... 13
Figura 5: Campo de vientos a las 06:00 h ........................................................................................... 13
Figura 6: Campo de vientos a las 08:00 h ........................................................................................... 14
Figura 7: Campo de vientos a las 10:00 h ........................................................................................... 14
Figura 8: Campo de vientos a las 12:00 h ........................................................................................... 15
Figura 9: Campo de vientos a las 14:00 h ........................................................................................... 15
Figura 10: Campo de vientos a las 16:00 h ........................................................................................... 16
Figura 11: Campo de vientos a las 18:00 h ........................................................................................... 16
Figura 12: Campo de vientos a las 20:00 h ........................................................................................... 17
Figura 13: Campo de vientos a las 22:00 h ........................................................................................... 17
Figura 14: Ubicación Estación Meteorológica Estación Centro ............................................................ 18
Figura 15: Serie de tiempo para registros horarios de velocidad del viento - Estación Centro,

periodo 01.01.2013 al 31-12-2013 ....................................................................................... 20
Figura 16: Serie de tiempo para registros horarios de Dirección del viento - Estación Centro,

periodo 01.01.2013 al 31-12-2013 ....................................................................................... 21
Figura 17: Rosa de Viento Estación Centro v/s Rosa de Viento modelada con WRF .......................... 22
Figura 18: Ubicación Geográfica ........................................................................................................... 24
Figura 19: Área de Modelamiento ......................................................................................................... 25
Figura 20: Grilla de Modelamiento ........................................................................................................ 26
Figura 21: Topografía del Área de Modelación ..................................................................................... 27
Figura 22: Ubicación del Receptor ........................................................................................................ 28
Figura 23: Suelos ................................................................................................................................... 29
Figura 24: Mapa de Isoconcentración Material Particulado MP10 - Etapa de Construcción (24

h) .......................................................................................................................................... 66
Figura 25: Mapa de Isoconcentración Material Particulado MP10 - Etapa de Construcción

(Anual) .................................................................................................................................. 67
Figura 26: Mapa de Isoconcentración Material Particulado MP2.5 - Etapa de Construcción (24

h) .......................................................................................................................................... 68
Figura 27: Mapa de Isoconcentración Material Particulado MP2.5 - Etapa de Construcción

(Anual) .................................................................................................................................. 69
Figura 28: Mapa de Isoconcentración Gases CO - Etapa de Construcción (1h) .................................. 70
Figura 29: Mapa de Isoconcentración Gases CO - Etapa de Construcción (8h) .................................. 71
Figura 30: Mapa de Isoconcentración Gases NO2 - Etapa de Construcción (1 h) ............................... 72
Figura 31: Mapa de Isoconcentración Gases NO2 - Etapa de Construcción (Anual) ........................... 73
Figura 32: Mapa de Isoconcentración Gases SO2 - Etapa de Construcción (1h) ................................ 74
Figura 33: Mapa de Isoconcentración Gases SO2 - Etapa de Construcción (24h) ............................. 75
Figura 34: Mapa de Isoconcentración Gases SO2 - Etapa de Construcción (Anual) ........................... 76

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 5

Figura 35: Mapa de Isodepositación Material Particulado Sedimentable MPS - Etapa de

Construcción (24h) ............................................................................................................... 77
Figura 36: Mapa de Isodepositación Material Particulado Sedimentable MPS - Etapa de

Construcción (Anual) ............................................................................................................ 78
Figura 37: Mapa de Isoconcentración Material Particulado MP10 - Etapa de Operación (24 h) .......... 79
Figura 38: Mapa de Isoconcentración Material Particulado MP10 - Etapa de Operación (Anual)........ 80
Figura 39: Mapa de Isoconcentración Material Particulado MP2.5 - Etapa de Operación (24 h) ......... 81
Figura 40: Mapa de Isoconcentración Material Particulado MP2.5 - Etapa de Operación (Anual) ...... 82
Figura 41: Mapa de Isoconcentración Gases CO - Etapa de Operación (1h) ...................................... 83
Figura 42: Mapa de Isoconcentración Gases CO - Etapa de Operación (8h) ...................................... 84
Figura 43: Mapa de Isoconcentración Gases NO2 - Etapa de Operación (1 h) ................................... 85
Figura 44: Mapa de Isoconcentración Gases NO2 - Etapa de Operación (Anual) ............................... 86
Figura 45: Mapa de Isoconcentración Gases SO2 - Etapa de Operación (1h) ..................................... 87
Figura 46: Mapa de Isoconcentración Gases SO2 - Etapa de Operación (24h)................................... 88
Figura 47: Mapa de Isoconcentración Gases SO2 - Etapa de Operación (Anual) ............................... 89
Figura 48: Mapa de Isodepositación Material Particulado Sedimentable MPS - Etapa de

Operación (24h).................................................................................................................... 90
Figura 49: Mapa de Isodepositación Material Particulado Sedimentable MPS - Etapa de

Operación (Anual) ................................................................................................................ 91
Figura 50: Mapa de Isoconcentración Material Particulado MP10 - Etapa de Cierre (24 h) ................. 92
Figura 51: Mapa de Isoconcentración Material Particulado MP10 - Etapa de Cierre (Anual) .............. 93
Figura 52: Mapa de Isoconcentración Material Particulado MP2.5 - Etapa de Cierre (24 h) ................ 94
Figura 53: Mapa de Isoconcentración Material Particulado MP2.5 - Etapa de Cierre (Anual) ............. 95
Figura 54: Mapa de Isoconcentración Gases CO - Etapa de Cierre (1h) ............................................. 96
Figura 55: Mapa de Isoconcentración Gases CO - Etapa de Cierre (8h) ............................................. 97
Figura 56: Mapa de Isoconcentración Gases NO2 - Etapa de Cierre (1 h) .......................................... 98
Figura 57: Mapa de Isoconcentración Gases NO2 - Etapa de Cierre (Anual) ...................................... 99
Figura 58: Mapa de Isoconcentración Gases SO2 - Etapa de Cierre (1h) ......................................... 100
Figura 59: Mapa de Isoconcentración Gases SO2 - Etapa de Cierre (24h) ....................................... 101
Figura 60: Mapa de Isoconcentración Gases SO2 - Etapa de Cierre (Anual) .................................... 102
Figura 61: Mapa de Isodepositación Material Particulado Sedimentable MPS - Etapa de Cierre

(24h) ................................................................................................................................... 103
Figura 62: Mapa de Isodepositación Material Particulado Sedimentable MPS - Etapa de Cierre

(Anual) ................................................................................................................................ 104

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 6

**1. INTRODUCCIÓN**

En el presente informe se desarrolla el inventario de emisiones de material particulado y se
presentan los resultados de la modelación atmosférica de dispersión de contaminantes
generados durante las distintas etapas del Proyecto “Extracción y Procesamiento de Áridos
Sector Aguada de la Teca” de Áridos San Pedro SpA. Estas emisiones corresponden
específicamente a material particulado respirable (MP 10 y MP 2.5 ), gases (CO, HC, NOx,
SOx), y material particulado sedimentable (MPS), las cuales son generadas por las
actividades de escarpe, excavaciones, carguío y transporte, tránsito de vehículos por
caminos pavimentados, tránsito de vehículos livianos y vehículos pesados por caminos no
pavimentados, procesos de chancado, harneado, transporte de material por cintas
transportadoras, erosión de materiales en pila y utilización de maquinarias, equipos,
vehículos y generadores eléctricos.

El proyecto “Extracción y Procesamiento de Áridos Sector Aguada de la Teca” consiste en la
extracción y procesamiento de áridos, proveniente del inmueble de propiedad de la
Comunidad Indígena Atacameña de Rio Grande, para lo cual el Titular ya cuenta con un
contrato de cuentas en participación con dicha Comunidad, adjunto en el anexo N°1. El
proyecto se localizará aproximadamente en el km 50 del camino San Pedro de Atacama
(Ruta CH-23), comuna de San Pedro de Atacama, Provincia del Loa, Región de
Antofagasta. El proyecto contempla la extracción de un volumen total de 1.800.000 m [3] de
áridos, en un período de 6 años y abarca una superficie total de 14,473 hectáreas.

Para realizar la estimación de las emisiones atmosféricas asociadas al proyecto, se
utilizaron: la Guía para la Estimación de Emisiones Atmosféricas de Proyectos Inmobiliarios
para la Región Metropolitana del Ministerio del Medio Ambiente (2012), la Guía
Metodológica para la Estimación de Emisiones Atmosféricas de Fuentes Fijas y Móviles en
el Registro de Emisiones y Transferencia de Contaminantes (Conama, 2009), Factores de
Emisión Recomendados por la Environmental Protection Agency (US EPA) en sus
Documentos AP-42 (Fifth Edition, Compilation of Air Pollutant Emission Factors) y la Guía
para el Uso de Modelos de Calidad del Aire en el SEIA (2012).

Los resultados de la modelación atmosférica, se han analizado tomando en consideración
los límites máximos permisibles establecidos en las normas primarias y secundarias de
calidad del aire establecido en la legislación chilena, los cuales se presentan en la tabla 1
siguiente:

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 7

**Tabla 1: Normas de Calidad Ambiental Primarias y Secundarias**

|Parámetro|Unidad Estadística|Límite Máximo<br>Permitido|Referencia Legal|
|---|---|---|---|
|MP 10|Promedio Anual1|50 (μg/m3N)|NP DS 20/2013|
|MP 10|Percentil 98 Promedio 24 horas2|150 (μg/m3N)|NP DS 20/2013|
|MP 2.5|Promedio Trianual3|20 (μg/m3N)|NP DS 12/2011|
|MP 2.5|Percentil 98 Promedio Diario4|50 (μg/m3N)|NP DS 12/2011|
|MPS|Promedio Mensual|150 mg/m2dia|NS DE 4/1992|
|MPS|Promedio Anual|100 mg/m2dia|NS DE 4/1992|
|SO2|Promedio Anual5|80 (μg/m3N)|NP DS 113/2002|
|SO2|Promedio Diario, percentil 996|250 (μg/m3N)|NP DS 113/2002|
|SO2|Promedio Anual7|80 (μg/m3N)|NS DS 185/1991|
|SO2|Percentil 99.7 Concentración Diaria8|365 (μg/m3N)|NS DS 185/1991|
|SO2|Percentil 99.73 Concentración 1 hora9|1000 (μg/m3N)|NS DS 185/1991|
|NO2|Promedio Anual10|100 (μg/m3N)|NP DS 114/2002|
|NO2|Percentil 99, máx. 1 hora11|400 (μg/m3N)|NP DS 114/2002|

1 Promedio Anual: se refiere a la concentración promedio anual. Se considera sobrepasada la norma cuando la

concentración anual calculada como promedio aritmético de tres años calendario consecutivos, sea mayor o
igual a lo indicado a la tabla.
2 Percentil 98, 24 horas: se refiere a la concentración promedio de 24 horas. Se considera sobrepasada la

norma cuando el Percentil 98 de las concentraciones de 24horas registradas durante un período anual sea
mayor o igual a ese valor de la tabla.
3 Promedio Trianual: se refiere al promedio tri-anual de las concentraciones anuales. Se considera sobrepasada

la norma cuando el valor sea mayor al indicado en la tabla.
4 Percentil 98, Promedio Diario: se refiere a la percentil 98 de los promedios diarios registrados durante un año.
Se considera sobrepasada la norma cuando el valor sea mayor al indicado en la tabla

5 Promedio Anual: se refiere al promedio aritmético de los valores de concentración anual de tres años
calendarios sucesivos. Se considera sobrepasada la norma con un valor igual o superior indicado en la tabla.
6 Promedio Diario, Percentil 99: se refiere al promedio aritmético de tres años sucesivos, del percentil 99 de las
concentraciones de 24 horas registradas durante un año calendario. Se considera sobrepasada la norma con
un valor igual o superior indicado en la tabla.
7 Promedio Anual: se refiere al promedio aritmético de los valores de concentración anual de tres años

calendarios sucesivos. Se considera sobrepasada la norma con un valor mayor o igual al doble del nivel
indicado en la tabla.
8 Percentil 99.7: se refiere al promedio aritmético de tres años calendario sucesivo de los valores del percentil

99,7 de las concentraciones de 24 horas registradas cada año. Se considera sobrepasada la norma con un
valor mayor o igual al doble del nivel indicado en la tabla.
9 Percentil 99.73: se refiere al promedio aritmético de tres años calendario sucesivo de los valores del percentil

99,73 de las concentraciones de 1 hora registradas cada año. Se considera sobrepasada la norma con un valor
mayor o igual al doble del nivel indicado en la tabla.
10 Promedio Anual: se refiere al promedio aritmético de los valores de concentración anual de tres años

calendarios sucesivos. Se considera sobrepasada la norma con un valor igual o superior indicado en la tabla.
11 Percentil 99: se refiere al promedio aritmético de tres años sucesivos del percentil 99 de los máximos diarios de

concentración de 1 hora registrados durante un año calendario. Se considera sobrepasada la norma con un
valor igual o superior indicado en la tabla.

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 8

|CO|Percentil 99,máx.8 horas12|10.000 (μg/m3N)|NP DS 115/2002|
|---|---|---|---|
|CO|Percentil 99, máx. 1 hora13|30.000 (μg/m3N)|NP DS 115/2002|

**2. DESCRIPCIÓN Y JUSTIFICACIÓN DEL MODELO**

En el presente estudio, se ha utilizado el modelo de dispersión de contaminantes CALPUFF.
Este modelo creado por científicos del ASG (Grupo de Estudios Atmosféricos de TRC
Solutions), corresponde a un avanzado sistema de modelación meteorológica y de calidad

del aire.

El modelo ha sido adoptado por la Agencia de Protección Medioambiental de los Estados
Unidos (EPA por sus siglas en inglés) en su Guía para Modelos de Calidad del Aire como el
preferido para la evaluación de transporte de contaminantes a gran escala y como una base
caso a caso para determinadas aplicaciones que involucran condiciones meteorológicas
complejas.

Está formado principalmente por tres componentes y un set de programas de pre- y postprocesamiento. Estos componentes son:

CALMET: modelo meteorológico que desarrolla campos horarios de viento y temperatura en
un dominio de modelación de grilla tridimensional. Contiene además parametrizaciones de
flujos de laderas, efectos cinemáticos y de bloqueo del terreno, un procedimiento de
minimización de divergencia y un modelo micrometeorológico para capas límites sobre tierra
y agua. En el archivo producido por CALMET están también incluidos campos
bidimensionales asociados como altura de mezcla, características de la superficie y
propiedades de dispersión.

CALPUFF: modelo de transporte y dispersión lagrangiano, gaussiano, no estacionario, que
contiene módulos para efectos de terreno complejo, transporte sobre agua, deposiciones
secas y húmedas y transformaciones químicas simples. El modelo advecta "puffs" o
bocanadas de material emitido desde fuentes modeladas, simulando procesos de dispersión
y transformación en el camino. Típicamente usa los campos generados por CALMET, o

12 Percentil 99: se refiere al promedio aritmético de tres años sucesivos, del percentil 99 de los máximos diarios

de concentración de 8 horas registrados durante un año calendario. Se considera sobrepasada la norma con
un valor igual o superior indicado en la tabla.
13 Percentil 99: se refiere al promedio aritmético de tres años sucesivos, del percentil 99 de los máximos diarios

de concentración de 1 hora registrados durante un año calendario. Se considera sobrepasada la norma con un
valor igual o superior indicado en la tabla.

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 9

como opción puede usar datos meteorológicos más simples no grillados muy similares a
modelos de plumas existentes. En la distribución resultante de "puffs", a lo largo del período
simulado, incorpora explícitamente variaciones temporales y espaciales en los campos
meteorológicos seleccionados. Los archivos de salida primarios de CALPUFF contienen
concentraciones o flujos de deposiciones horarias evaluadas en lugares seleccionados de
recepción.

CALPOST: procesador de los archivos de CALPUFF, produciendo tablas que resumen los
resultados de la simulación, identificando por ejemplo las concentraciones máximas
promedios de tres horas y las segundas más altas en cada receptor. Cuando se realizan
modelaciones relacionadas a visibilidad, CALPOST usa concentraciones de CALPUFF para
calcular coeficientes de extinción y mediciones relacionadas a visibilidad, reportándolas para
los tiempos promediados y lugares seleccionados.

Cada uno de estos programas tiene una interfaz gráfica, existiendo además otros
numerosos procesadores que pueden ser utilizados para preparar datos geofísicos (como el
terreno y uso de suelo), meteorológicos (como precipitación o datos provenientes de boyas),
o interfaces a otros modelos como el MM5, WRF, modelos RUC o RAMS.

Para seleccionar el modelo adecuado, se consideraron los criterios establecidos en la Guía
para el Uso de Modelos de Calidad del Aire en el SEIA, (apartado 4.2, modelos
recomendados, pág. 17). Calpuff, resulto ser el más adecuado, considerando que los datos
disponibles para establecer el dominio espacial de la modelación, se sitúan a más de 5 km

de la fuente de emisión.

**3. ESCENARIO METEOROLÓGICO**

El escenario meteorológico utilizado para la modelación, fue obtenido a través del modelo
meteorológico de pronostico Weather Research and Forecasting Model (WRF), adquiridos a
la empresa Lakes Environmental, con un domino de 100 km por 100 km, una resolución de 4
km y el periodo de data año 2013.

**Tabla 2: Información de la Orden de los Datos WRF**

Order #: MET145564
Company: B&CA Asesorias Ambientales
Data Type: CALMET-Ready WRF Data (3D.DAT Format)
Resolution: 4 km

Domain: 100x100 km

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 10

Period: Jan 01, 2013 hour 00 - Dec 31, 2013 hour 23
Latitude: 22.67394 S
Longitude: 68.53142 W
Datum: WGS 84

UMT Zone: -19

Site Time Zone: UTC - 4
Closest City: Calama
Country: Chile

WRF es uno de los modelos meteorológicos de pronóstico más avanzados y completos y es
mantenido por NCAR9/ NOAA10 de Estados Unidos. Además, se ha ocupado en la mayoría
de los proyectos relacionados con modelación atmosférica encargados por organismos
estatales, como la ex-CONAMA y la Comisión Nacional de Energía (CNE) en los últimos

cinco años.

Campos de viento

Respecto a la dirección del viento, se puede apreciar que la dirección de viento
predominante es SWW, luego E y en tercer lugar NWW, con una velocidad que fluctúa
principalmente entre 5 y 8 m/s

**Figura 1: Rosa de Vientos**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 11

**Figura 2: Campo de vientos a las 00:00 h**

**Figura 3: Campo de vientos a las 02:00 h**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 12

**Figura 4: Campo de vientos a las 04:00 h**

**Figura 5: Campo de vientos a las 06:00 h**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 13

**Figura 6: Campo de vientos a las 08:00 h**

**Figura 7: Campo de vientos a las 10:00 h**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 14

**Figura 8: Campo de vientos a las 12:00 h**

**Figura 9: Campo de vientos a las 14:00 h**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 15

**Figura 10: Campo de vientos a las 16:00 h**

**Figura 11: Campo de vientos a las 18:00 h**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 16

**Figura 12: Campo de vientos a las 20:00 h**

**Figura 13: Campo de vientos a las 22:00 h**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 17

**3.1 Datos Observados**

En consideración a que en el área del proyecto no existen estaciones meteorológicas ni de
calidad del aire, para efectos de realizar este análisis, se ha consultado la información
disponible en el SINCA. La caracterización de la línea de base de calidad del aire imperante
en el área de influencia del proyecto y datos meteorológicos de superficie observados,
corresponden a la estación “Estación Centro” ubicada en la Comuna de Calama, cuyas
coordenadas UTM en Datum WGS-84 Huso 19S, son: 7.516.056 N - 507.371 E

**Figura 14: Ubicación Estación Meteorológica Estación Centro**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 18

**Tabla 3: Información general de la Estación Meteorológica** **[14]**

Propietario Codelco División Chuquicamata
Operador CIMM Tecnologías y Servicios S.A.
Región de Antofagasta
Provincia El Loa

Comuna Calama
Coordenadas UTM 507371 E 7516056 N

Huso horario 19
Recepción de datos en línea
Inicio de operación reportada 2012-10-12

La estación “Estación Centro” se encuentra dentro del área de modelación que se presenta
en la figura 14

Se ha considerado en el presente análisis la información disponible registrada en la Estación
Central, entre el 1° de enero de 2013 al 31 de diciembre de 2013, la que será comparada
con la información utilizada para el modelamiento y que corresponde al modelo
meteorológicos de pronóstico WRF (correspondiente al mismo período)

**Tabla 4: Línea de Base de MP y Gases - Estación Centro**

|Contaminante|Tipo de<br>Norma|Estadístico|Valor<br>(μg/m3N|Norma|%<br>Norma|
|---|---|---|---|---|---|
|MP10|Primaria|Promedio del período<br>Percentil 98 diario|41.9<br>44.3|50<br>150|83.1<br>29.5|
|MP2,5|Primaria|Promedio del período<br>Percentil 98 diario|12.18<br>14.3|20<br>50|60.9<br>28.6|
|SO2|Primaria|Promedio del período<br>Percentil 99 diario|4.8<br>4.5|80<br>250|6 <br>1.8|
|NO2|Primaria|Promedio del período<br>Percentil 99 horario|19.5<br>19.5|100<br>400|19.5<br>4.9|
|CO|Primaria|Percentil 99 en 8 horas<br>Percentil 99 horario|372.1<br>372.1|10000<br>30000|3.7<br>1.2|

14 Fuente de Información: página web http://sinca.mma.gob.cl

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 19

**3.2 Series de Tiempo.**

Las estadísticas de datos válidos monitoreado en la Estación Centro, es la siguiente:

Datos totales: 7.778

% datos válidos: 88.8%

% de Calma: 65.4 %

Las series de tiempo presentadas a continuación para las variables de dirección y velocidad
del viento, permiten un análisis cualitativo de los datos en términos de completitud de la
serie. En estas se puede observar la variabilidad, amplitud de rango y frecuencia de los
datos con que se cuenta.

**Figura 15: Serie de tiempo para registros horarios de velocidad del viento - Estación Centro,**

**periodo 01.01.2013 al 31-12-2013**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 20

**Figura 16: Serie de tiempo para registros horarios de Dirección del viento - Estación Centro,**

**periodo 01.01.2013 al 31-12-2013**

En las series de tiempo de la Estación Centro, se aprecia densidad de registros, mostrando
regularidad en la concentración de puntos para ambos gráficos (dirección y velocidad), se
aprecia un leve descenso de las velocidades entre los meses de abril a agosto. En el caso
de la direcciones de los vientos se aprecia que predominan los vientos de la dirección SWW
y en segundo lugar los vientos de dirección EEW

**3.3 Campos de Viento**

La figura 17, muestran la Rosa de Viento generada con los datos observados de la Estación
Centro durante el periodo (01.01.2013 al 31.12 2013) y la Rosa de Viento generada con el
modelo de pronostico WRF durante el mismo período, en el mismo punto de localización de

la Estación Centro

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 21

**Figura 17: Rosa de Viento Estación Centro v/s Rosa de Viento modelada con WRF**

Rosa de Viento Estación Centro Rosa de Viento modelada con WRF

En la Rosa obtenida en base a las mediciones meteorológicas de la Estación Centro, se
observa que la dirección predominante de los vientos es (SWW) con intensidades de los
vientos de moderadas a intensas. Puede apreciarse que el modelo de pronostico WRF
representa con bastante exactitud la condición de los vientos, tanto en dirección como en

velocidad.

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 22

**4. BASES DE DATOS Y ARCHIVOS DE MODELACIÓN**

La base de datos para la modelación CALMET-CALPUFF considero la siguiente

información:

**Tabla 5: Información Para el Modelamiento**

 - Emisiones generadas por las actividades del proyecto en cada una de sus etapas.

 - Ubicación geográfica del proyecto

 - Área de modelamiento

 - Grilla de modelamiento

 - Topografía del área de modelación

**4.1 Archivos de Entrada y Salida de la Modelación**

Los archivos de entrada y salida de la modelación, para cada etapa del proyecto y que se
anexan en forma digital (DVD), son los siguientes:

**Tabla 6: Archivos de Entrada y Salida de la Modelación,**

|CALMET|GEO.DAT<br>CALMET.DAT<br>CALMET.LST<br>CALMET.INP|
|---|---|
|CALPUF|CALPUFF.LST<br>CALPUFF.INP<br>CONS.INP|
|CALPOST|CALPOST.DAT<br>CALPOST.LST<br>CALPOST.INP|
|ARCHIVOS<br>COMPLEMENTARIOS|Dry Flux Data File<br>Wet Flux Data|

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 23

**5. CARACTERÍSTICAS DEL DOMINIO DE MODELACIÓN Y SU ENTORNO**

**5.1 Localización**

El Proyecto se localiza en la Región de Antofagasta, Provincia del Loa y Comuna de San
Pedro de Atacama, a unos 50 km al sureste de la ciudad de Calama, aproximadamente a
3.160 m.s.n.m. La ubicación del Proyecto se muestra en la Figura 18 en el contexto del
sector Aguada de la Teca.

**Figura 18: Ubicación Geográfica**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 24

**5.2 Área de Modelamiento**

El área o dominio de modelación considerado tiene su origen en las coordenadas UTM
WGS84 19S - E: 498.136 y N: 7.442.498 A partir de este punto, el dominio considera un
área de 100 kilómetros en la dirección Este y 100 kilómetros en la dirección Norte, que
incluye la totalidad de las fuentes emisoras del proyecto y el receptor más cercanos
(Calama, Chiu Chiu y San Pedro de Atacama).

**Figura 19: Área de Modelamiento**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 25

**5.3 Grilla de Modelamiento**

La grilla de modelamiento utilizada corresponde a un dominio de 100 x 100 km con
espaciamiento de 4 km.

**Figura 20: Grilla de Modelamiento**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 26

**5.4 Topografía del Área de Modelamiento**

La topografía del área de modelamiento se ha obtenido satelitalmente. La siguiente figura
ilustra las curvas de nivel para el área de modelamiento.

**Figura 21: Topografía del Área de Modelación**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 27

**5.5 Receptores en el Área de Modelamiento**

Se definen como los receptores más cercanos al área del proyecto, las poblaciones de
Calama, San Pedro de Atacama y Chiu-Chiu. El siguiente cuadro presenta las coordenadas
UTM en Datum WGS-84 Huso 19, de las habitaciones más cercaba al área del proyecto en

cada una de las localidades señaladas:

**Tabla 7: Ubicación Receptores Humanos**

|Localidad|Este|Norte|
|---|---|---|
|Calama<br>San Pedro de Atacama<br>Chiu-Chiu|510069<br>581754<br>535607|7513907<br>7467110<br>7526387|

**Figura 22: Ubicación del Receptor**

Debido a que no se han identificado receptores biológicos, dentro del área de modelamiento,
se consideraran los mismos puntos señalados en la tabla anterior, como receptores
biológicos.

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 28

**5.6 Suelos del Área de Modelamiento**

Los suelos del área de modelamiento se caracterizan por su escaso a nulo desarrollo, con
ausencia de materia orgánica y desprovisto de vegetación como resultado de la interacción
de las escasas precipitaciones y altas temperaturas; ambas características típicas del

desierto de Atacama.

En general, el suelo productivo en la comuna de San Pedro es escaso, no existen
condiciones para la formación de suelos ricos en materia orgánica para el desarrollo de la
agricultura. Sólo existen unas pequeñas superficies asociadas a los ayllus y en menor
medida, en las quebradas de las localidades al sureste del Salar de Atacama donde se
cultiva en terrazas, escalones que fabrica el agricultor y riega a través de canales [15]

La siguiente figura ilustra el tipo de suelo en el área de modelamiento.

**Figura 23: Suelos**

15 Ilustre Municipalidad de San Pedro de Atacama. 2010. Memoria Explicativa Actualización de Plan
Regulador Comunal de San Pedro de Atacama .

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 29

**6. FUENTES DE EMISIÓN**

**6.1 Actividades Emisoras**

Las emisiones a la atmósfera que generará el Proyecto “Extracción y Procesamiento de
Áridos Sector Aguada de la Teca”, en sus distintas etapas, corresponderán a emisiones
fugitivas de material particulado respirable MP 10, MP 2.5, material particulado sedimentable
(MPS), gases de combustión de vehículos y maquinarias y gases de equipos generadores,
que serán utilizados en las distintas etapas que comprende este proyecto.

La siguiente tabla, presenta las actividades del proyecto generadoras de emisiones

atmosféricas

**Tabla 8: Actividad Generadora de Emisiones - Etapa de Construcción**

|Etapa del<br>Proyecto|Actividad Generadora de Emisiones|Col3|Tipo de<br>Contaminante|
|---|---|---|---|
|Etapa del<br>Proyecto|Actividad|Descripción Datos|Descripción Datos|
|Etapa de<br>Construcción|**Escarpado área Instalación**<br>**Campamento**(preparación de terreno)|Área Total: 400 m2<br>Duración: 90 días|MP10 <br>MP2.5 <br>MPS|
|Etapa de<br>Construcción|**Escarpado área Instalación Planta de**<br>**Chancado y Selección de Materiales**<br>(preparación de terreno)|Área Total: 2.500 m2<br>Duración: 90 días|Área Total: 2.500 m2<br>Duración: 90 días|
|Etapa de<br>Construcción|**Tránsito de Vehículos por Caminos**<br>**Pavimentados**(viajes/día)|Longitud Total (50 km)<br>Duración (días)|Longitud Total (50 km)<br>Duración (días)|
|Etapa de<br>Construcción|- Transporte Equipos Planta: 1|1|1|
|Etapa de<br>Construcción|- Transporte Estructura Pesada: 3|1|1|
|Etapa de<br>Construcción|- Camión Grúa para montaje e instalación: 1|1|1|
|Etapa de<br>Construcción|- Transporte Petróleo: 1|12|12|
|Etapa de<br>Construcción|- Transporte Agua Potable: 1|12|12|
|Etapa de<br>Construcción|- Transporte Personal y Supervisión: 2|90|90|
|Etapa de<br>Construcción|**Tránsito de Vehículos Livianos por**<br>**Caminos No Pavimentados**(viajes/día)<br>- Transporte de Personal y Supervisión: 2|Longitud Total (1,5 km)<br>Duración (días)<br>2|Longitud Total (1,5 km)<br>Duración (días)<br>2|
|Etapa de<br>Construcción|**Tránsito de Vehículos Pesados por**<br>**Caminos No Pavimentados**(viajes/día)|Longitud Total (1,5 km)<br>Duración (días)|Longitud Total (1,5 km)<br>Duración (días)|
|Etapa de<br>Construcción|- Transporte Equipos Planta: 1|1|1|
|Etapa de<br>Construcción|- Transporte Estructura Pesada: 3|1|1|

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 30

|Etapa de<br>Construcción|- Camión Grúa para montaje e instalación: 1|1|MP<br>10<br>MP<br>2.5<br>MPS|
|---|---|---|---|
|Etapa de<br>Construcción|- Transporte Petróleo: 1|12|12|
|Etapa de<br>Construcción|- Transporte Agua Potable: 1|12|12|
|Etapa de<br>Construcción|**Emisiones de Gases** de Combustión de maquinarias y vehículos|**Emisiones de Gases** de Combustión de maquinarias y vehículos|CO, HC,<br>NOx, CC, y MP|
|Etapa de<br>Construcción|**Emisiones de Gases** de Equipos Generadores|**Emisiones de Gases** de Equipos Generadores|CO, NOx, MP10, y<br>SOx|

**Tabla 9: Actividad Generadora de Emisiones - Etapa de Operación**

|Etapa del<br>proyecto|Actividad Generadora de Emisiones|Col3|Tipo de<br>Contaminante|
|---|---|---|---|
|Etapa del<br>proyecto|Actividad|Descripción datos|Descripción datos|
|Etapa de<br>Operación|**Excavación Área 1 y 2**<br>**(**Extracción de áridos)|Área Total: 14.183 ha<br>Duración: 2.190 días|MP10 <br>MP2.5 <br>MPS|
|Etapa de<br>Operación|**Transferencia de Material**<br>(Carga y descarga de áridos en acopio<br>intermedio)|Área: 100 m2<br>Duración: 2.190 días|Área: 100 m2<br>Duración: 2.190 días|
|Etapa de<br>Operación|**Transferencia de Material**<br>(Carga y descarga de áridos en buzón<br>alimentación Planta)|Área: 100 m2<br>Duración: 2.190 días|Área: 100 m2<br>Duración: 2.190 días|
|Etapa de<br>Operación|**Tránsito de Vehículos por Caminos**<br>**Pavimentados**(viajes/día)|<br>Longitud Total (50 km)<br>Duración (días)|<br>Longitud Total (50 km)<br>Duración (días)|
|Etapa de<br>Operación|- Transporte Petróleo: 1|2190|2190|
|Etapa de<br>Operación|- Transporte Agua Potable: 1|312|312|
|Etapa de<br>Operación|- Transporte de Residuos Varios: 1|312|312|
|Etapa de<br>Operación|- Transporte Personal y Supervisión: 2|2190|2190|
|Etapa de<br>Operación|**Tránsito de Vehículos Livianos por**<br>**Caminos No Pavimentados (**viajes/día) <br>- Transporte de personal y Supervisión: 2|Longitud Total (1,5 km)<br>Duración (días)<br>2190|Longitud Total (1,5 km)<br>Duración (días)<br>2190|
|Etapa de<br>Operación|**Tránsito de Vehículos Pesados por**<br>**Caminos No Pavimentados**(viajes/día) <br>- Transporte interno de áridos a la planta: 55|Longitud Total (0,6 km)<br>Duración (días)<br>2190|Longitud Total (0,6 km)<br>Duración (días)<br>2190|
|Etapa de<br>Operación|**Tránsito de Vehículos Pesados por**<br>**Caminos No Pavimentados**(viajes/día)|Longitud Total (1,5 km)<br>Duración (días)|Longitud Total (1,5 km)<br>Duración (días)|
|Etapa de<br>Operación|- Transporte Petróleo: 1|2190|2190|
|Etapa de<br>Operación|- Transporte Agua Potable: 1|312|312|
|Etapa de<br>Operación|- Transporte de Residuos Varios: 1|312|312|

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 31

|Etapa de<br>Operación|Proceso Chancado<br>(Emisiones del proceso de trituración)|Cantidad de equipos:1<br>Área: 5,25 m2<br>Total: 1.643,84 ton/día<br>Duración: 2.190 días|MP<br>10<br>MP<br>2.5<br>MPS|
|---|---|---|---|
|Etapa de<br>Operación|**Harnero Primario**|Cantidad de equipos:1<br>Área: 5,25 m2 <br>Total: 1.643,84 ton/día<br>Duración: 2.190 días|Cantidad de equipos:1<br>Área: 5,25 m2 <br>Total: 1.643,84 ton/día<br>Duración: 2.190 días|
|Etapa de<br>Operación|**Harnero Secundario**|Cantidad de equipos:1<br>Área: 5,25 m2 <br>Total: 410,96 ton/día<br>Duración: 2.190 días|Cantidad de equipos:1<br>Área: 5,25 m2 <br>Total: 410,96 ton/día<br>Duración: 2.190 días|
|Etapa de<br>Operación|**Cintas Transportadora 1**<br>- alimentación harnero primario|Largo: 18 m<br>Ancho: 1 m<br>Cantidad de traspasos: 1|Largo: 18 m<br>Ancho: 1 m<br>Cantidad de traspasos: 1|
|Etapa de<br>Operación|**Cintas Transportadora 2**<br>- transportador material grava|Largo: 12 m<br>Ancho: 1 m<br>Cantidad de traspasos: 1|Largo: 12 m<br>Ancho: 1 m<br>Cantidad de traspasos: 1|
|Etapa de<br>Operación|**Cintas Transportadora 3**<br>- transportador gravilla|Largo: 12 m<br>Ancho: 1 m<br>Cantidad de traspasos: 1|Largo: 12 m<br>Ancho: 1 m<br>Cantidad de traspasos: 1|
|Etapa de<br>Operación|**Cintas Transportadora 4**<br>- transportador material grueso|Largo: 12 m<br>Ancho: 1 m<br>Cantidad de traspasos: 1|Largo: 12 m<br>Ancho: 1 m<br>Cantidad de traspasos: 1|
|Etapa de<br>Operación|**Cintas Transportadora 5**<br>- alimentación harnero secundario|Largo: 12 m<br>Ancho: 1 m<br>Cantidad de traspasos: 1|Largo: 12 m<br>Ancho: 1 m<br>Cantidad de traspasos: 1|
|Etapa de<br>Operación|**Cintas Transportadora 6**<br>- transportador al acopio de arenas|Largo: 12 m<br>Ancho: 1 m<br>Cantidad de traspasos: 1|Largo: 12 m<br>Ancho: 1 m<br>Cantidad de traspasos: 1|
|Etapa de<br>Operación|**Erosión de Materiales en Pila**<br>- Acopios material grueso <br>- Acopios material grava <br>- Acopios material gravilla <br>- Acopios material arena|**Área de Acopio:**<br>- Material grueso: 500 m2 <br>- Material grava: 500 m2 <br>- Material gravilla: 500 m2 <br>- Material arena: 500 m2|**Área de Acopio:**<br>- Material grueso: 500 m2 <br>- Material grava: 500 m2 <br>- Material gravilla: 500 m2 <br>- Material arena: 500 m2|
|Etapa de<br>Operación|**Emisiones de Gases** de Combustión de maquinarias y vehículos|**Emisiones de Gases** de Combustión de maquinarias y vehículos|CO, HC,<br>NOx, y MPS,<br>MP10, MP2.5|
|Etapa de<br>Operación|**Emisiones de Gases** por Combustión en Equipos Generadores|**Emisiones de Gases** por Combustión en Equipos Generadores|CO, NOx,<br>MPS, MP10, <br>MP2.5, SOx, COV|

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 32

**Tabla 10: Actividad Generadora de Emisiones - Etapa de Cierre**

|Etapa del<br>proyecto|Actividad Generadora de Emisiones|Col3|Tipo de<br>Contaminante|
|---|---|---|---|
|Etapa del<br>proyecto|Actividad|Descripción datos|Descripción datos|
|Etapa de<br>Cierre|**Escarpado**<br>- Reperfilamiento área Planta<br>- Reperfilamiento Camino|Área de Reperfilamiento:<br>Planta: 25.000 m2<br>Camino: 10.500 m3<br>Duración: 90 días|MP10 <br>MP2.5 <br>MPS|
|Etapa de<br>Cierre|**Tránsito de Vehículos por Caminos**<br>**Pavimentados**(viajes/día) <br>- Transporte Petróleo: 1<br>- Transito Equipos Planta: 1<br>- Transporte Estructura Pesada: 3<br>- Transporte Camión Grúa: 1<br>- Transporte Agua Potable: 1<br>- Transporte Personal y Supervisión: 2|Longitud de camino: 50 km<br>Duración: 90 días|Longitud de camino: 50 km<br>Duración: 90 días|
|Etapa de<br>Cierre|**Tránsito de Vehículos Livianos por**<br>**Caminos No Pavimentados**<br>(viajes/día) <br>- Transporte Personal y Supervisión: 2|Longitud de camino: 1.5 km<br>Duración: 90 días|Longitud de camino: 1.5 km<br>Duración: 90 días|
|Etapa de<br>Cierre|**Tránsito de Vehículos Pesados por**<br>**Caminos No Pavimentados**<br>(viajes/día) <br>- Transporte Petróleo: 1<br>- Transito Equipos Planta: 1<br>- Transporte Estructura Pesada: 3<br>- Transporte Camión Grúa: 1<br>- Transporte Agua Potable: 1|Longitud de camino: 1.5 km<br>Duración: 90 días|Longitud de camino: 1.5 km<br>Duración: 90 días|
|Etapa de<br>Cierre|**Emisiones de Gases** de Combustión de maquinarias y vehículos|**Emisiones de Gases** de Combustión de maquinarias y vehículos|CO, HC,<br>NOx, y MPS, MP10, <br>MP2.5|
|Etapa de<br>Cierre|**Emisiones de Gases** de Equipos Generadores|**Emisiones de Gases** de Equipos Generadores|CO, NOx,<br>MPS, MP10, MP2.5, <br>SOx, COV|

**6.2 Metodología para la Estimación de Emisiones**

La ecuación general para estimar las emisiones de cualquier actividad, es la siguiente:

Dónde:

_E_ : Emisión (Ton/año)
_fe_ : Factor de emisión

_Na_ : Nivel de la actividad

_Ea_ : Eficiencia de abatimiento

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 33

**6.2.1 Metodología para la estimación de emisiones de las actividades**

Las emisiones de material particulado (MP 10, MP 2.5, MPS), generadas por las actividades del
proyecto, en cada una de sus etapas, se han estimado utilizando la Guía para la estimación
de emisiones atmosféricas de proyectos inmobiliarios para la Región Metropolitana del
Ministerio del Medio Ambiente, [enero 2012] y los factores de emisión del Manual AP 42 de
la EPA (Fifth Edition, Compilation of Air Pollutant Emission Factors, Volume 1: Stationary
Point and Area Sources, United States - Environmental Protection Agency).

Para el cálculo de los factores de emisiones, se han utilizado los valores por defecto que
establece la Guía para la estimación de emisiones atmosféricas de proyectos inmobiliarios
para la Región Metropolitana del Ministerio del Medio Ambiente, [enero 2012].

Las emisiones han sido estimadas en kg/día y ton/año, de acuerdo a la programación de las

actividades.

**6.2.2 Metodología para la estimación de emisiones de maquinarias**

La metodología utilizada para determinar las emisiones de material particulado de
combustión y gases asociados a la operación de la maquinaria, durante cada una de las
etapas del proyecto, corresponde a la que se presenta en la Guía para la Estimación de
Emisiones Atmosféricas de Proyectos Inmobiliarios para la Región Metropolitana (Enero
2012).

La ecuación general para estimar las emisiones de material particulado de combustión y
gases asociados a la operación de la maquinaria, es la siguiente:

E = (FP * t * C * P)

Dónde:

FP: factor según potencia
t: tiempo de operación diaria (h)
C: Porcentaje de carga
P: Potencia Nominal (kw)

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 34

**Tabla 11: Maquinarias Utilizados en Etapa de Construcción**

|Equipo|Cantidad|Potencia<br>Nominal kw|Operación<br>Diaria (horas)|
|---|---|---|---|
|Motoniveladora|1|137|12|

**Tabla 12: Maquinarias Utilizados en Etapa de Operación**

|Equipo|Cantidad|Potencia<br>Nominal kw|Operación<br>Diaria (horas)|
|---|---|---|---|
|Excavadora 1.5 m3|1|120|12|
|Cargador Frontal W190B|1|160|12|
|Cargador Frontal 721 E|1|160|12|

**Tabla 13: Maquinarias Utilizados en Etapa de Cierre**

|Equipo|Cantidad|Potencia<br>Nominal kw|Operación<br>Diaria (horas)|
|---|---|---|---|
|Motoniveladora|1|137|12|

**6.2.3 Metodología para la estimación de emisiones de vehículos**

La metodología utilizada para determinar las emisiones de material particulado de
combustión y gases de la flota de vehículos, en cada una de las etapas del proyecto,
corresponde a la que se presenta en la Guía para la Estimación de Emisiones Atmosféricas
de Proyectos Inmobiliarios para la Región Metropolitana (Enero 2012).

Las categorías de los vehículos que conforman la flota de vehículos del proyecto, es la
siguiente:

Camiones Pesados Diésel Tipo 3: Corresponden a camiones pesados con peso bruto
superior a 16 toneladas cuya fecha de inscripción en el Registro Nacional de Vehículos
Motorizados sea posterior a septiembre del año 2003. Estos buses deben cumplir con la
normativa EPA 98 o Euro III. Notar que esta fecha de aplicación tiene aún cierto grado de
incerteza y será aclarada una vez que la autoridad por decreto lo establezca.

Vehículos Comerciales Diésel Tipo 2: Corresponden a los vehículos livianos de pasajeros o
carga liviana, privados o comerciales y que funcionan con combustible diésel, principalmente
del tipo jeep, camioneta o furgón cuya fecha de inscripción en el registro Nacional de
Vehículos Motorizados sea posterior a septiembre del año 2003 cumpliendo con la

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 35

normativa EPA 94 federal o la Euro III. Notar que la normativa específica y la fecha de
aplicación tienen aún cierto grado de incerteza y será aclarada una vez que la autoridad por

decreto lo establezca.

El nivel de actividad (Na) corresponde a la cantidad de kilómetros que circula cada vehículo.

**Tabla 14: Vehículos Utilizados en Etapa de Construcción**

|Vehículo|Categoría|N°<br>Viajes/día|Distancia<br>(km)|Velocidad km/h|
|---|---|---|---|---|
|Camión Transporte Petróleo|Pesado Diésel Tipo 3|1|51.5|100|
|Camión Transporte Equipos Planta|Pesado Diésel Tipo 3|1|51.5|100|
|Camión Transporte Estructura<br>Pesada|Pesado Diésel Tipo 3|3|51.5|100|
|Camión Grúa|Pesado Diésel Tipo 3|1|51.5|100|
|Camión Transporte Agua Potable|Pesado Diésel Tipo 3|1|51.5|100|
|Camionetas Transporte Personal y<br>Supervisión|Comerciales Diésel Tipo 2|2|51.5|100|

**Tabla 15: Vehículos Utilizados en Etapa de Operación**

|Vehículo|Categoría|N°<br>Viajes/día|Distancia<br>(km)|Velocidad km/h|
|---|---|---|---|---|
|Camión Transporte Áridos|Pesado Diésel Tipo 3|55|0.6|50|
|Camión Transporte Petróleo|Pesado Diésel Tipo 3|1|51.5|100|
|Camión Transporte Agua Potable|Pesado Diésel Tipo 3|1|51.5|100|
|Camión Transporte Residuos Varios|Pesado Diésel Tipo 3|1|51.5|100|
|Camionetas Transporte Personal y<br>Supervisión|Comerciales Diésel Tipo 2|2|51.5|100|

**Tabla 16: Vehículos Utilizados en Etapa de Cierre**

|Vehículo|Categoría|N°<br>Viajes/día|Distancia<br>(km)|Velocidad km/h|
|---|---|---|---|---|
|Camión Transporte Petróleo|Pesado Diésel Tipo 3|1|51.5|100|
|Camión Transporte Estructura<br>Pesada|Pesado Diésel Tipo 3|3|51.5|100|
|Camión Transporte Equipos Planta|Pesado Diésel Tipo 3|1|51.5|100|
|Camión Grúa|Pesado Diésel Tipo 3|1|51.5|100|
|Camión Transporte Agua Potable|Pesado Diésel Tipo 3|1|51.5|100|
|Camionetas Transporte Personal y<br>Supervisión|Comerciales Diésel Tipo 2|2|51.5|100|

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 36

**Tabla 17: Peso Promedio de la Flota**

|Vehículos|Capacidad de<br>carga (ton)|Peso Vacío<br>(ton)|Peso<br>Cargado<br>(ton)|Peso<br>Promedio)|
|---|---|---|---|---|
|Camión Transporte de Áridos|30|19|49|34|
|Camión Transporte Estructura Pesada|30|19|49|34|
|Camión Transporte Equipos Planta|30|19|49|34|
|Camión Grúa|30|19|49|34|
|Camión Transporte de Petróleo|30|19|49|34|
|Camión Transporte de Residuos varios|30|19|49|34|
|Camión Agua|30|19|49|34|
|Camionetas Transporte de Supervisión|0.15|2.5|2.65|2.58|

**6.2.4 Metodología para la estimación de emisiones por combustión en generadores**

**eléctricos**

La metodología utilizada para determinar las emisiones de material particulado de
combustión y gases de los generadores eléctricos, en cada una de las etapas del proyecto,
corresponde a la que se presenta en el documento AP42 de la EPA, Chapter 3 (Stationary
Internal Combustion Sources), tablas 3.4-1 y 3.4-2.
El porcentaje de azufre es de máximo 1% en el combustible de acuerdo al Decreto Supremo
132/2004 Ministerio de Minería Reglamento de Seguridad Minera Artículo 131, para equipos
de minería, incluido casas de fuerza. Por lo tanto S=1.

**Tabla 18: Generadores**

|Etapa Proyecto|Potencia (kw) por<br>Generador|Horas<br>Operación Día|Cantidad|
|---|---|---|---|
|Construcción|480|12|1|
|Operación|480|12|1|
|Cierre|480|12|1|

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 37

**7. FACTORES DE EMISIÓN**

Los factores de emisión (fe) corresponden a ecuaciones o expresiones matemáticas que
permiten estimar tasas unitarias de emisiones atmosféricas. Para el caso específico de las
operaciones relacionadas con este proyecto, en cada una de sus etapas, se utilizaron los
modelos matemáticos para factores de emisión, propuestos en el Manuel AP-42
(Compilation of Air Pollutant Emission Factors), de la Agencia de Protección del Ambiente de
los EE.UU. (U.S. EPA) y la Guía para la estimación de emisiones atmosféricas de proyectos
inmobiliarios para la Región Metropolitana del Ministerio del Medio Ambiente, [enero 2012].

Estos factores de emisión, proporcionan un valor representativo de la cantidad de agentes
contaminante por unidad de peso, volumen, distancia o duración de la actividad. En muchos
casos, los factores de emisión representan la media de un conjunto de datos disponibles y,
por lo general, se asume como representativo de períodos de largo plazo.

A continuación se presentan los factores de emisión utilizados para estimar las emisiones
del proyecto. En primer lugar, se presentan los factores de emisión de material particulado
resuspendido y posteriormente los factores de emisión de material particulado y gases
asociados a procesos de combustión.

**7.1 Factores de Emisión para Material Particulado Resuspendido**

Las expresiones de factores de emisión para la estimación de emisiones de material
particulado resuspendido, se presentan a continuación [16] .

**Tabla 19: Factor de Emisión Escarpes**

|Factor de Emisión (fe)|fe = k*0,570|
|---|---|
|Unidades|kg/km|
|Parámetros|No utiliza parámetros<br>K: Factor según tamaño de partícula<br> PM10 = 0,75<br> PM2.5 = 0,105<br> MPS = 1|
|Fuente|Compilation of Air Pollutant Emission Factors, AP 42, 5th Edition: Chapter 13,<br>Section 13.2.3“Heavy Construction Operations, 2010”|
|Descripción|Corresponde al factor de emisión de preparación de terrenos (movimiento de<br>tierra) y retiro de cobertura vegetal. La unidad de este factor corresponde a<br>kilógramos emitidos por kilómetro recorrido en el proceso de escarpado de la|

16 Fuente de Información: Guía para la estimación de emisiones atmosféricas de proyectos inmobiliarios para la

Región Metropolitana del Ministerio del Medio Ambiente, [enero 2012].

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 38

|Col1|cobertura vegetal.|
|---|---|
|Nivel de actividad|El nivel de actividad se determina según la distancia que recorre el cargador<br>frontal por el área a escapar. Por defecto para 1 hectárea se recorre una distancia<br>de 3,57 km|
|Mitigación|No aplican medidas de mitigación|

**Tabla 20: Factor de Emisión Excavaciones**

|Factor de Emisión (fe)|fe = 0.45*k*(s^1.5/M^1.4) [Para PM10 y PM2.5]<br>fe = 2.6*s^1.2/M^1.3 [Para MPS]|
|---|---|
|Unidades|kg/h|
|Parámetros|K: Factor según tamaño de partícula<br> PM10 = 0.75<br> PM2.5 = 0,105<br> MPS = 2.6<br>s: % de finos del suelo [8,5 valor por defecto]<br>M: % humedad material [6,5 valor por defecto]|
|Fuente|Compilation of Air Pollutant Emission Factors, AP 42, 5th Edition: Chapter 11,<br>Section 11.9 “Western Surface Coal Mining, 1998”, Table 11.9-2.|
|Descripción|Corresponde al factor de emisión de despeje de material (bulldozing / overburden)<br>escalado por 0,75 para ser aplicado a MP10. La unidad de este factor corresponde<br>a kilógramos emitidos por hora excavada|
|Nota|El nivel de actividad se determina a través del rendimiento de la maquinaria y el<br>volumen a escavar. Por defecto se considerará para una retroexcavadora con<br>capacidad de palada de 1 m3 un rendimiento igual a 30 m3/hr.|
|Mitigación|No aplican medidas de mitigación.|

**Tabla 21: Factor de Emisión Transferencia de Material (Carguío y Volteo de Camiones)**

|Factor de Emisión (fe)|fe = 0.0016*k*(U/2.2)^1.3/(M/2)^1.4|
|---|---|
|Unidades|kg/ton|
|Parámetros|K: Factor según tamaño de partícula<br> PM10 = 0,35<br> PM2.5 = 0,053<br> MPS = 0.74<br>U: Velocidad del viento (m/s) [5 m/s valor por defecto]<br>M: Humedad del material [6,5 valor por defecto]|
|Fuente|Compilation of Air Pollutant Emission Factors, AP 42: Chapter 13, Section 13.2.4<br>“Aggregate Handling and Storage Piles, 2006”.|
|Descripción|Corresponde al factor de emisión de transferencia discreta de material utilizado<br>directamente. La unidad de este factor corresponde a kilogramos emitidos por<br>cada tonelada de material cargado o descargado.|
|Mitigación|No aplican medidas de mitigación.|

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 39

**Tabla 22: Factores de Emisión Resuspensión de MP por Circulación de Vehículos en Caminos**

**Pavimentados**

|Factor de Emisión (fe)|fe = k*(sL)^0.91*W^1.02|
|---|---|
|Unidades|gr/ton|
|Parámetros|K: Factor según tamaño de partícula<br> PM10 = 0,62<br> PM2.5 = 0,15<br> MPS = 3.23<br>sL: Carga de fino de la superficie, (g/m2)<br>W: Peso promedio del flujo total de la flota que circula por las vías (Toneladas)|
|Fuente|Compilation of Air Pollutant Emission Factors, AP-42: Chapter 13, Section 13.2.1<br>“Paved Roads, 2011”.|
|Descripción|Corresponde al factor de emisión de material particulado resuspendido por<br>tránsito de vehículos por caminos pavimentados. La unidad de este factor de<br>emisión es gramos de MP10 emitidos por kilómetro recorrido.|
|Mitigación|No aplican medidas de mitigación.|

**Tabla 23: Factor de Emisión Resuspensión de MP10 Circulación de Vehículos Livianos en**

**Caminos No Pavimentados**

|Factor de Emisión (fe)|fe = 281.9*k*(s/12)*(S/30)^0.5/(M/0.5)^0.2|
|---|---|
|Unidades|g/km|
|Parámetros|K: Factor según tamaño de partícula<br> PM10 = 1.5<br> PM2.5 = 0,15<br> MPS = 4.9<br>s: % de finos del suelo [8,5 valor por defecto]<br>S: Velocidad de los vehículos en km/h<br>M: % humedad material. [6,5 valor por defecto]|
|Fuente|Compilation of Air Pollutant Emission Factors, AP 42: Chapter 13, Section 13.2.2<br>“Unpaved Roads, 2006”.|
|Descripción|Corresponde al factor de emisión de tránsito por caminos no pavimentados<br>determinado para caminos de acceso público. La unidad de este factor de emisión<br>es gramos de MP10 emitidos por kilómetro recorrido|
|Nota|Dadas las características de la flota utilizada en la determinación de este factor de<br>emisión, su aplicación se reconoce válida para una flota de vehículos pesados, es<br>decir, cuyo peso promedio exceda las 2,7 toneladas métricas.<br>Contenido de % de finos del suelo - valor por defecto 8,5%<br>Contenido de humedad del suelo - valor por defecto 6,5%|
|Mitigación|Como medida de abatimiento se considera el mejoramiento de caminos mediante<br>la aplicación de una capa de gravilla.|

**Tabla 24: Factor de Emisión Resuspensión de MP10 Circulación de Vehículos Pesados en**

**Caminos No Pavimentados**

|Factor de Emisión (fe)|fe = 281.9*k*(s/12)^0.9*(W/3)^0.45 [Para MP10 y MP2.5]<br>Fe = 281,9*4.9*(s/12) ^0,7*(W/3) ^0,45 [Para MPS]|
|---|---|
|Unidades|g/km|
|Parámetros|K: Factor según tamaño de partícula|

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 40

|Col1|PM10 = 1.5<br>PM2.5 = 0,15<br>MPS = 4.9<br>s: % de finos del suelo [8,5 valor por defecto]<br>W: Peso promedio de la flota que circula por las vías (ton)|
|---|---|
|Fuente|Compilation of Air Pollutant Emission Factors, AP 42: Chapter 13, Section 13.2.2<br>“Unpaved Roads”.|
|Descripción|Corresponde al factor de emisión de transito por caminos no pavimentados<br>determinado para sitios industriales. La unidad de este factor de emisión es<br>gramos de MP10 emitidos por kilómetro recorrido.|
|Nota|Dadas las características de la flota utilizada en la determinación de este factor de<br>emisión, su aplicación se reconoce válida para una flota de vehículos pesados, es<br>decir, cuyo peso promedio exceda las 2,7 toneladas métricas.<br>El titular deberá proveer el peso promedio de la flota que circula por las vías<br>relevantes. En caso de no hacerlo, el peso promedio por defecto será el peso<br>promedio de la flota generada por la actividad del proyecto.<br>Contenido de % de finos del suelo - valor por defecto 8,5%|
|Mitigación|Como medida de abatimiento se considera el mejoramiento de caminos mediante<br>la aplicación de una capa de gravilla.|

**Tabla 25: Factores de Emisión de Cintas Transportadoras**

|Factor de Emisión (fe)|Fe = k|
|---|---|
|Unidades|kg/ton|
|Parámetros|Factor según tamaño de partícula<br> PM10 = 0.0006<br> PM2.5 = 0,0006<br> MPS = 0.0015<br>Nota: debido a que no existen valores para MP2,5, se considera el peor escenario<br>en que PM10 = PM2,5|
|Fuente|AP 42: Charper 11, Sectión 11.19,2, Table 11.19.2-1 r"|
|Descripción|Corresponde al factor de emisión de emisiones generadas en traspasos cintas<br>trasportadoras|
|Mitigación|No aplican medidas de mitigación.|

**Tabla 26: Factores de Emisión Erosión en Pilas, Acopios**

|Factor de Emisión (fe)|Fe = k * s/1,5 * f/15|
|---|---|
|Unidades|kg/ha|
|Parámetros|Factor según tamaño de partícula<br> PM10 = 0.5<br> PM2.5 = 0,075<br> MPS = 1<br>s: contenido de fino del material (%).[8,5 valor por defecto]<br>f: porcentaje del tiempo en el que el viento excede los 5,4 m/s. [9,8 %]|
|Fuente|Industria del Árido en Chile, Tomo I, Sistematización de Antecedentes Técnicos y<br>Ambientales, 2001|
|Descripción|Corresponde al factor de emisión para acopio de productos intermedios y finales<br>utilizado directamente|
|Mitigación|No aplican medidas de mitigación.|

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 41

**7.2 Factores de Emisión para la Estimación de Emisiones de Gases y Material**

**Particulado.**

Los factores de emisión de gases y material particulado de combustión, asociados a la
operación de la maquinaria, vehículos, generadores, calderas y equipos de secado y fusión
durante las distintas etapas del proyecto, se presentan en las tablas siguientes:

**Tabla 27: Factores de Emisión de Gases y MP de Maquinarias**

|Factor de Emisión (fe)|E= (FP × t × C × P)|
|---|---|
|Unidades|gr/día|
|Parámetros|FP: factor según potencia<br>t: tiempo de operación diaria (h)<br>C: Porcentaje de carga<br>P: Potencia Nominal (kw)|
|Fuente|Guía para la Estimación de Emisiones Atmosféricas de Proyectos Inmobiliarios<br>para la Región Metropolitana, Tabla 4.9|
|Descripción|Corresponde al factor de emisión de combustión de los motores de la maquinaria<br>fuera de ruta.|
|Mitigación|No aplican medidas de mitigación.|

**Tabla 28: Factor de Emisión en Función de la Potencia (g/kW-h)**

|Contaminante|0-20|20-37|37-75|75-130|>130|
|---|---|---|---|---|---|
|CO|8.38|6.43|5.06|3.76|3.00|
|HC|3.87|2.96|2.33|1.72|1.35|
|NOx|14.36|14.36|14.36|14.36|14.36|
|MP|2.22|1.81|1.51|1.23|1.10|

**Tabla 29: Factor de Emisión Para Gases y MP de Vehículos** [17]

|Categoría|Contaminante|Factor Emisión [g/km]|
|---|---|---|
|Camiones Pesados<br>Diésel Tipo 3|CO|(1,24588358438859+(103,700537481749/(1+exp((((-1)*-<br>1,3906312471446)+(0,543451750078654*ln(V)))+(0,0390066425998189*<br>V)))))|
|Camiones Pesados<br>Diésel Tipo 3|HC|((0,135938586321894+(0,71588074810547*exp(((-<br>1)*0,0234666513590177)*V)))+(2,79878282504916*exp(((-<br>1)*0,123459782380517)*V)))|

17 Anexo 2 de la Guía para la estimación de emisiones atmosféricas de proyectos inmobiliarios para la Región
Metropolitana, [2006].

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 42

|Col1|NOx|((5,58300975720938+(14,5724996214701*exp(((-<br>1)*0,0510403515051286)*V)))+(45,651882800859*exp(((-<br>1)*0,309240087785118)*V)))|
|---|---|---|
||CC|((199,101296810716+(496,037924788222*exp(((-<br>1)*0,0466183266185801)*V)))+(3798,31076366067*exp(((-<br>1)*0,573715458508514)*V)))|
||MP|((0,100820480611018+(0,424449762706025*exp(((-<br>1)*0,0416436785215947)*V)))+(0,864328026775096*exp(((-<br>1)*0,159945936589218)*V)))|
|Vehículos<br>Comerciales Diésel<br>Tipo 2|CO|0,82*(0,000223*V^2-0,026*k18+1,076)|
|Vehículos<br>Comerciales Diésel<br>Tipo 2|HC|0,62*(0.0000175*V 2-0,00284*V+0,2162)|
|Vehículos<br>Comerciales Diésel<br>Tipo 2|NOx|0,84*(0.000241*V 2-0,03181*V+2,0247)|
|Vehículos<br>Comerciales Diésel<br>Tipo 2|CC|0,0198*V 2-2,506*V+137,42|
|Vehículos<br>Comerciales Diésel<br>Tipo 2|MP|0,67*(0.000045*V 2-0,004885*V+0,1932)|

**Tabla 30: Factor de Emisión por Combustión en Grupos Generadores** [18]

|FACTORES DE EMISION GRUPOS GENERADORES (kg/kw-h)|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|Contaminante|**CO**|**NOx**|**MPS**|**MP 10**|**MP 2.5**|**SOx**|**COV**|
|Petróleo N°6|0,003|0,0146|0,000426|0,00026|0,000218|0,004919|0,000019|

**8. NIVELES DE ACTIVIDAD**

El nivel de actividad (Na) utilizado para calcular las emisiones de cada actividad, en cada
una de las fases del proyecto, se presenta en las tablas siguientes:

**Tabla 31: Nivel de Actividad Etapa de Construcción**

|ACTIVIDAD|Actividad Específica|Nivel de Actividad|Col4|
|---|---|---|---|
|**ACTIVIDAD**|Actividad Específica|Cantidad|Unidad|
|Escarpe|Escarpe Área Instalación Campamento|0.14|km/día|
|Escarpe|Escarpe Área Instalación Planta de Chancado<br>y Selección de Materiales|0.89|0.89|

18 AP42 de la EPA, Chapter 3 (Stationary Internal Combustion Sources), tablas: 3.4-1; 3.4-2; 3-4-3

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 43

|Tránsito de Vehículos Por Caminos<br>Pavimentados|Transporte Equipos Planta|100|km/día|
|---|---|---|---|
|Tránsito de Vehículos Por Caminos<br>Pavimentados|Transporte Estructura Pesada|300|300|
|Tránsito de Vehículos Por Caminos<br>Pavimentados|Transporte Camión Grúa Montaje e Instalación|100|100|
|Tránsito de Vehículos Por Caminos<br>Pavimentados|Transporte Petróleo|100|100|
|Tránsito de Vehículos Por Caminos<br>Pavimentados|Transporte Agua Potable|100|100|
|Tránsito de Vehículos Por Caminos<br>Pavimentados|Transporte Personal y Supervisión|200|200|
|Transito Vehículos Livianos<br>Por Caminos No Pavimentados|Transporte Personal y Supervisión|6|km/día|
|Transito Vehículos Pesados<br>Por Caminos No Pavimentados|Transporte Equipos Planta|3|km/día|
|Transito Vehículos Pesados<br>Por Caminos No Pavimentados|Transporte Estructura Pesada|9|9|
|Transito Vehículos Pesados<br>Por Caminos No Pavimentados|Transporte Camión Grúa Montaje e Instalación|3|3|
|Transito Vehículos Pesados<br>Por Caminos No Pavimentados|Transporte Petróleo|3|3|
|Transito Vehículos Pesados<br>Por Caminos No Pavimentados|Transporte Agua Potable|3|3|

**Tabla 32: Nivel de Actividad Etapa de Operación**

|ACTIVIDAD|Actividad Específica|Nivel de Actividad|Col4|
|---|---|---|---|
|**ACTIVIDAD**|Actividad Específica|Cantidad|Unidad|
|Excavaciones|Excavaciones Área 1 y 2 de Extracción de<br>Áridos|27,40|h/día|
|Carguío y Volteo de Camiones|Carga y descarga de áridos de acopio<br>intermedio|1.643,84|ton/día|
|Carguío y Volteo de Camiones|Carga y descarga de áridos en buzón<br>alimentación Planta|1.643,84|1.643,84|
|Tránsito Por Caminos<br>Pavimentados|Transporte de Petróleo|100|km/día|
|Tránsito Por Caminos<br>Pavimentados|Transporte Agua Potable|100|100|
|Tránsito Por Caminos<br>Pavimentados|Transporte de Residuos varios|52,0|52,0|
|Tránsito Por Caminos<br>Pavimentados|Transporte de Personal y Supervisión|200|200|
|Transito Vehículos Livianos<br>Por Caminos No Pavimentados|Transporte de Personal y Supervisión|6|km/día|
|Transito Vehículos Pesados<br>Por Caminos No Pavimentados|Transporte interno de Áridos a la Planta|65,75|km/día|
|Transito Vehículos Pesados<br>Por Caminos No Pavimentados|Transporte de Petróleo|3|3|
|Transito Vehículos Pesados<br>Por Caminos No Pavimentados|Transporte de Agua Potable|3|3|
|Transito Vehículos Pesados<br>Por Caminos No Pavimentados|Transporte de Residuos Varios|3|3|
|Chancado|Chancador primario|1.643,84|Ton/día|
|Harneado|Harnero primario|1.643,84|Ton/día|
|Harneado|Harnero Secundario|410,96|410,96|

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 44

|Cintas Transportadoras|Alimentación Harnero Primario.|1.643,84|Ton/día|
|---|---|---|---|
|Cintas Transportadoras|Transportador Material Graba|410,96|410,96|
|Cintas Transportadoras|Transportador Material Gravilla|410,96|410,96|
|Cintas Transportadoras|Transportador Material Grueso|410,96|410,96|
|Cintas Transportadoras|Alimentación Harnero Secundario|410,96|410,96|
|Cintas Transportadoras|Transportador Material Arena|410,96|410,96|
|Erosión de Materiales en Pila|Acopio de Material Grueso|0,05|ha/día|
|Erosión de Materiales en Pila|Acopio de Material Graba|0,05|0,05|
|Erosión de Materiales en Pila|Acopios de Material Gravilla|0,05|0,05|
|Erosión de Materiales en Pila|Acopio de Material Arena|0,05|0,05|

**Tabla 33: Nivel de Actividad Etapa de Cierre**

|ACTIVIDAD|Actividad Específica|Nivel de Actividad|Col4|
|---|---|---|---|
|**ACTIVIDAD**|Actividad Específica|Cantidad|Unidad|
|Reperfilamiento|Reperfilamiento área Planta|0,89|km/día|
|Reperfilamiento|Reperfilamiento área Camino|3,75|3,75|
|Tránsito Por Caminos<br>Pavimentados|Transporte Equipos Planta|100|km/día|
|Tránsito Por Caminos<br>Pavimentados|Transporte Estructura Pesada|300|300|
|Tránsito Por Caminos<br>Pavimentados|Transporte Camión Grúa para Desmontaje|100|100|
|Tránsito Por Caminos<br>Pavimentados|Transporte de Petróleo|100|100|
|Tránsito Por Caminos<br>Pavimentados|Transporte de Agua Potable|100|100|
|Tránsito Por Caminos<br>Pavimentados|Transporte de Personal y Supervisión|200|200|
|Transito Vehículos Livianos<br>Por Caminos No Pavimentados|Transporte de Personal y Supervisión|6|km/día|
|Transito Vehículos Pesados<br>Por Caminos No Pavimentados|Transporte de Petróleo|3|km/día|
|Transito Vehículos Pesados<br>Por Caminos No Pavimentados|Transporte de Equipos Planta|3|3|
|Transito Vehículos Pesados<br>Por Caminos No Pavimentados|Transporte de Estructura Pesada|9|9|
|Transito Vehículos Pesados<br>Por Caminos No Pavimentados|Transporte Camión Grúa para Desmontaje|3|3|
|Transito Vehículos Pesados<br>Por Caminos No Pavimentados|Transporte Camión Grúa para Desmontaje|3|3|

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 45

**9.** **MEDIDAS DE MITIGACIÓN CAMINOS**

Se considera solo como medida de mitigación de material particulado, el mejoramiento del
camino interno mediante aplicación de una capa de gravilla.

**10. RESULTADOS INVENTARIO DE EMISIONES**

Las tablas siguientes muestran los resultados del inventario de emisiones.

**Tabla 34: Factores de Emisión (MP10, MP2.5 y MPS) - Actividades Etapa de Construcción**

|ACTIVIDAD|Actividad Específica|Parámetros para Factores<br>de Emisión|Col4|Col5|Factor de<br>emisión<br>PM10|Factor de<br>emisión<br>PM2.5|Factor de<br>emisión<br>MPS|Unidad|
|---|---|---|---|---|---|---|---|---|
|**ACTIVIDAD**|Actividad Específica|k10|k2,5|kMPS|kMPS|kMPS|kMPS|kMPS|
|Escarpe|Escarpe Área Instalación<br>Campamento|0,75|0,105|1|4,28E+00|5,99E-01|5,70E+00|kg/km|
|Escarpe|Escarpe Área Instalación<br>Planta de Chancado y<br>Selección de Materiales|0,75|0,105|1|4,28E+00|5,99E-01|5,70E+00|5,70E+00|
|Tránsito de Vehículos<br>Por Caminos<br>Pavimentados|Transporte Equipos Planta|0,62|0,15|3,23|1,64E-02|3,96E-03|8,52E-02|kg/km|
|Tránsito de Vehículos<br>Por Caminos<br>Pavimentados|Transporte Estructura<br>Pesada|0,62|0,15|3,23|1,64E-02|3,96E-03|8,52E-02|8,52E-02|
|Tránsito de Vehículos<br>Por Caminos<br>Pavimentados|Camión Grúa Para Montaje<br>e Instalación|0,62|0,15|3,23|1,64E-02|3,96E-03|8,52E-02|8,52E-02|
|Tránsito de Vehículos<br>Por Caminos<br>Pavimentados|Transporte Petróleo|0,62|0,15|3,23|1,64E-02|3,96E-03|8,52E-02|8,52E-02|
|Tránsito de Vehículos<br>Por Caminos<br>Pavimentados|Transporte Agua Potable|0,62|0,15|3,23|1,64E-02|3,96E-03|8,52E-02|8,52E-02|
|Tránsito de Vehículos<br>Por Caminos<br>Pavimentados|Transporte de Personal y<br>Supervisión|0,62|0,15|3,23|1,18E-03|2,85E-04|6,14E-03|6,14E-03|
|Transito Vehículos<br>Livianos Por Caminos<br>No Pavimentados|Transporte de Personal y<br>Supervisión|1,5|0,15|4,9|3,27E-01|3,27E-02|1,07E+00|kg/km|
|Transito Vehículos<br>Pesados Por Caminos<br>No Pavimentados|Transporte Equipos Planta|1,5|0,15|4,9|9,24E-01|9,24E-02|3,02E+00|kg/km|
|Transito Vehículos<br>Pesados Por Caminos<br>No Pavimentados|Transporte Estructura<br>Pesada|1,5|0,15|4,9|9,24E-01|9,24E-02|3,02E+00|3,02E+00|
|Transito Vehículos<br>Pesados Por Caminos<br>No Pavimentados|Camión Grúa Para Montaje<br>e Instalación|1,5|0,15|4,9|9,24E-01|9,24E-02|3,02E+00|3,02E+00|
|Transito Vehículos<br>Pesados Por Caminos<br>No Pavimentados|Transporte Petróleo|1,5|0,15|4,9|9,24E-01|9,24E-02|3,02E+00|3,02E+00|
|Transito Vehículos<br>Pesados Por Caminos<br>No Pavimentados|Transporte Agua Potable|1,5|0,15|4,9|9,24E-01|9,24E-02|3,02E+00|3,02E+00|

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 46

**Tabla 35: Factores de Emisión (MP10, MP2.5 y MPS) - Actividades Etapa de Operación**

|ACTIVIDAD|Actividad Específica|Parámetros para Factores<br>de Emisión|Col4|Col5|Factor de<br>emisión<br>PM10|Factor de<br>emisión<br>PM2.5|Factor de<br>emisión<br>MPS|Unidad|
|---|---|---|---|---|---|---|---|---|
|**ACTIVIDAD**|Actividad Específica|k10|k2,5|kMPS|kMPS|kMPS|kMPS|kMPS|
|Excavaciones|Excavación Área 1 y 2 de<br>extracción de áridos|0,75|0,105|2,6|6,09E-01|8,52E-02|2,98E+00|kg/h|
|Carguío y Volteo<br>de Camiones|Carga y descarga de<br>áridos en acopio<br>intermedio|0,35|0,053|0,74|3,13E-04|4,73E-05|6,61E-04|kg/ton|
|Carguío y Volteo<br>de Camiones|Carga y descarga de<br>áridos en buzón<br>alimentación Planta|0,35|0,053|0,74|3,13E-04|4,73E-05|6,61E-04|6,61E-04|
|Tránsito Por Caminos<br>Pavimentados|Transporte Petróleo|0,62|0,15|3,23|1,64E-02|3,96E-03|8,52E-02|kg/km|
|Tránsito Por Caminos<br>Pavimentados|Transporte Agua Potable|0,62|0,15|3,23|1,64E-02|3,96E-03|8,52E-02|8,52E-02|
|Tránsito Por Caminos<br>Pavimentados|Transporte de Residuos<br>varios|0,62|0,15|3,23|1,64E-02|3,96E-03|8,52E-02|8,52E-02|
|Tránsito Por Caminos<br>Pavimentados|Transporte de Personal y<br>Supervisión|0,62|0,15|3,23|1,18E-03|2,85E-04|6,14E-03|6,14E-03|
|Transito Vehículos<br>Livianos Por Caminos<br>No Pavimentados|Transporte de Personal y<br>Supervisión|1,5|0,15|4,9|3,27E-01|3,27E-02|1,07E+00|kg/km|
|Transito Vehículos<br>Pesados Por Caminos<br>No Pavimentados|Transporte Interno de<br>Áridos a la Planta|1,5|0,15|4,9|9,24E-01|9,24E-02|3,02E+00|kg/km|
|Transito Vehículos<br>Pesados Por Caminos<br>No Pavimentados|Transporte Petróleo|1,5|0,15|4,9|9,24E-01|9,24E-02|3,02E+00|3,02E+00|
|Transito Vehículos<br>Pesados Por Caminos<br>No Pavimentados|Transporte Agua Potable|1,5|0,15|4,9|9,24E-01|9,24E-02|3,02E+00|3,02E+00|
|Transito Vehículos<br>Pesados Por Caminos<br>No Pavimentados|Transporte de Residuos<br>varios|1,5|0,15|4,9|9,24E-01|9,24E-02|3,02E+00|3,02E+00|
|Chancado|Chancado Primario|0,02|0,02|0,2|2,0E-02|2,0E-02|2,0E-01|kg/ton|
|Harneado|Harnero Primario|0,0043|0,0043|0,012|4,3E-03|4,3E-03|1,2E-02|kg/ton|
|Harneado|Harnero Secundario|0,036|0,036|0,15|3,6E-02|3,6E-02|1,5E-01|1,5E-01|
|Cintas Transportadoras|Cinta transportadora de<br>alimentación harnero<br>primario<br>(1 traspaso)|0,0006|0,0006|0,0015|5,5E-04|5,5E-04|1,5E-03|kg/ton|
|Cintas Transportadoras|Cinta transportadora<br>material graba<br>(1 traspaso)|0,0006|0,0006|0,0015|5,5E-04|5,5E-04|1,5E-03|1,5E-03|
|Cintas Transportadoras|Cinta transportadora<br>material gravilla<br>(1 traspaso)|0,0006|0,0006|0,0015|5,5E-04|5,5E-04|1,5E-03|1,5E-03|
|Cintas Transportadoras|Cinta transportadora<br>material grueso<br>(1 traspaso)|0,0006|0,0006|0,0015|5,5E-04|5,5E-04|1,5E-03|1,5E-03|
|Cintas Transportadoras|Cinta transportadora al<br>harnero secundario<br>(1 traspaso)|0,0006|0,0006|0,0015|5,5E-04|5,5E-04|1,5E-03|1,5E-03|

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 47

|Cintas Transportadoras|Cinta transportadora<br>acopio arena<br>(1 traspaso)|0,0006|0,0006|0,0015|5,5E-04|5,5E-04|1,5E-03|kg/ton|
|---|---|---|---|---|---|---|---|---|
|Erosión en Pilas|Acopio de material grueso|0,5|0,075|1|3,04|0,46|6,08|kg/ha|
|Erosión en Pilas|Acopio de material graba|0,5|0,075|1|3,04|0,46|6,08|6,08|
|Erosión en Pilas|Acopio de material gravilla|0,5|0,075|1|3,04|0,46|6,08|6,08|
|Erosión en Pilas|Acopio de material arena|0,5|0,075|1|3,04|0,46|6,08|6,08|

**Tabla 36: Factores de Emisión (MP10, MP2.5 y MPS) - Actividades Etapa de Cierre**

|ACTIVIDAD|Actividad Específica|Parámetros para<br>Factores de Emisión|Col4|Col5|Factor de<br>emisión<br>PM10|Factor de<br>emisión<br>PM2.5|Factor de<br>emisión<br>MPS|Unidad|
|---|---|---|---|---|---|---|---|---|
|ACTIVIDAD|Actividad Específica|k10|k2,5|kMPS|kMPS|kMPS|kMPS|kMPS|
|Reperfilado|Reperfilamiento área<br>Planta|0,75|0,105|1|4,28E+00|5,99E-01|5,70E+00|kg/h|
|Reperfilado|Reperfilamiento área<br>Camino|0,75|0,105|1|4,28E+00|5,99E-01|5,70E+00|5,70E+00|
|Tránsito Por Caminos<br>Pavimentados|Transporte Equipos Planta|0,62|0,15|3,23|1,64E-02|3,96E-03|8,52E-02|kg/km|
|Tránsito Por Caminos<br>Pavimentados|Transporte Estructura<br>Pesada|0,62|0,15|3,23|1,64E-02|3,96E-03|8,52E-02|8,52E-02|
|Tránsito Por Caminos<br>Pavimentados|Camión Grúa Para<br>Montaje e Instalación|0,62|0,15|3,23|1,64E-02|3,96E-03|8,52E-02|8,52E-02|
|Tránsito Por Caminos<br>Pavimentados|Transporte Petróleo|0,62|0,15|3,23|1,64E-02|3,96E-03|8,52E-02|8,52E-02|
|Tránsito Por Caminos<br>Pavimentados|Transporte Agua Potable|0,62|0,15|3,23|1,64E-02|3,96E-03|8,52E-02|8,52E-02|
|Tránsito Por Caminos<br>Pavimentados|Transporte de Personal y<br>Supervisión|0,62|0,15|3,23|1,18E-03|2,85E-04|6,14E-03|6,14E-03|
|Transito Vehículos<br>Livianos Por Caminos<br>No Pavimentados|Transporte de Personal y<br>Supervisión|1,5|0,15|4,9|3,27E-01|3,27E-02|1,07E+00|kg/km|
|Transito Vehículos<br>Pesados<br>Por Caminos No<br>Pavimentados|Transporte Equipos Planta|1,5|0,15|4,9|9,24E-01|9,24E-02|3,02E+00|3,02E+00|
|Transito Vehículos<br>Pesados<br>Por Caminos No<br>Pavimentados|Transporte Estructura<br>Pesada|1,5|0,15|4,9|9,24E-01|9,24E-02|3,02E+00|kg/km|
|Transito Vehículos<br>Pesados<br>Por Caminos No<br>Pavimentados|Camión Grúa Para<br>Montaje e Instalación|1,5|0,15|4,9|9,24E-01|9,24E-02|3,02E+00|3,02E+00|
|Transito Vehículos<br>Pesados<br>Por Caminos No<br>Pavimentados|Transporte Petróleo|1,5|0,15|4,9|9,24E-01|9,24E-02|3,02E+00|3,02E+00|
|Transito Vehículos<br>Pesados<br>Por Caminos No<br>Pavimentados|Transporte Agua Potable|1,5|0,15|4,9|9,24E-01|9,24E-02|3,02E+00|3,02E+00|

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 48

**Tabla 37: Emisiones (MP10, MP2.5 y MPS) - Actividades Etapa de Construcción**

|ACTIVIDAD|Actividad Específica|Emisiones Diarias (kg/día)|Col4|Col5|Emisiones Anuales (ton/año)|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**ACTIVIDAD**|Actividad Específica|Emisiones<br>PM10|Emisiones<br>PM2.5|Emisiones<br>MPS|Emisiones<br>PM10|Emisiones<br>PM2.5|Emisiones<br>MPS|
|Escarpe|Escarpe Área Instalación<br>Campamento|0,6105|0,0855|0,8140|0,0006|0,0001|0,0008|
|Escarpe|Escarpe Área Instalación<br>Planta de Chancado y<br>Selección de Materiales|3,8154|0,5342|5,0873|0,0038|0,0005|0,0051|
|Tránsito de Vehículos Por<br>Caminos Pavimentados|Transporte Equipos Planta|1,6351|0,3956|8,5182|0,0016|0,0004|0,0085|
|Tránsito de Vehículos Por<br>Caminos Pavimentados|Transporte Estructura Pesada|4,9052|1,1868|25,5547|0,0049|0,0012|0,0256|
|Tránsito de Vehículos Por<br>Caminos Pavimentados|Camión Grúa Para Montaje e<br>Instalación|1,6351|0,3956|8,5182|0,0016|0,0004|0,0085|
|Tránsito de Vehículos Por<br>Caminos Pavimentados|Transporte Petróleo|1,6351|0,3956|8,5182|0,0196|0,0047|0,1022|
|Tránsito de Vehículos Por<br>Caminos Pavimentados|Transporte Agua Potable|1,6351|0,3956|8,5182|0,0196|0,0047|0,1022|
|Tránsito de Vehículos Por<br>Caminos Pavimentados|Transporte de Personal y<br>Supervisión|0,2357|0,0570|1,2278|0,0212|0,0051|0,1105|
|Transito Vehículos<br>Livianos Por Caminos No<br>Pavimentados|Transporte de Personal y<br>Supervisión|1,9644|0,1964|6,4170|0,1768|0,0177|0,5775|
|Transito Vehículos<br>Pesados Por Caminos No<br>Pavimentados|Transporte Equipos Planta|2,7732|0,2773|9,0591|0,0028|0,0003|0,0091|
|Transito Vehículos<br>Pesados Por Caminos No<br>Pavimentados|Transporte Estructura Pesada|8,3196|0,8320|27,1774|0,0083|0,0008|0,0272|
|Transito Vehículos<br>Pesados Por Caminos No<br>Pavimentados|Camión Grúa Para Montaje e<br>Instalación|2,7732|0,2773|9,0591|0,0028|0,0003|0,0091|
|Transito Vehículos<br>Pesados Por Caminos No<br>Pavimentados|Transporte Petróleo|2,7732|0,2773|9,0591|0,0333|0,0033|0,1087|
|Transito Vehículos<br>Pesados Por Caminos No<br>Pavimentados|Transporte Agua Potable|2,7732|0,2773|9,0591|0,0333|0,0033|0,1087|
|**TOTALES EMISIONES ETAPA DE CONSTRUCCIÓN**|**TOTALES EMISIONES ETAPA DE CONSTRUCCIÓN**|**37,48**|**5,58**|**136,59**|**0,33**|**0,04**|**1,20**|

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 49

**Tabla 38: Emisiones (MP10, MP2.5 y MPS) - Actividades Etapa de Operación**

|ACTIVIDAD|Actividad Específica|Emisiones Diarias (kg/día)|Col4|Col5|Emisiones Anuales (ton/año)|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**ACTIVIDAD**|Actividad Específica|Emisiones<br>PM10|Emisiones<br>PM2.5|Emisiones<br>MPS|Emisiones<br>PM10|Emisiones<br>PM2.5|Emisiones<br>MPS|
|Excavaciones|Excavación Área 1 y 2 de<br>extracción de áridos|16,6736|2,3343|81,5072|6,0859|0,8520|29,7501|
|Carguío y Volteo<br>de Camiones|Carga y descarga de áridos<br>en acopio intermedio|0,5140|0,0778|1,0866|0,1876|0,0284|0,3966|
|Carguío y Volteo<br>de Camiones|Carga y descarga de áridos<br>en buzón alimentación Planta|0,5140|0,0778|1,0866|0,1876|0,0284|0,3966|
|Tránsito Por Caminos<br>Pavimentados|Transporte Petróleo|1,6351|0,3956|8,5182|0,5968|0,1444|3,1092|
|Tránsito Por Caminos<br>Pavimentados|Transporte Agua Potable|1,6351|0,3956|8,5182|0,5968|0,1444|3,1092|
|Tránsito Por Caminos<br>Pavimentados|Transporte de Residuos<br>varios|1,6351|0,3956|8,5182|0,5968|0,1444|3,1092|
|Tránsito Por Caminos<br>Pavimentados|Transporte de Personal y<br>Supervisión|0,2357|0,0570|1,2278|0,0860|0,0208|0,4481|
|Transito Vehículos<br>Livianos Por Caminos<br>No Pavimentados|Transporte de Personal y<br>Supervisión|1,9644|0,1964|6,4170|0,7170|0,0717|2,3422|
|Transito Vehículos<br>Pesados Por Caminos<br>No Pavimentados|Transporte Interno de Áridos a<br>la Planta|60,7826|6,0783|198,5566|22,1857|2,2186|72,4732|
|Transito Vehículos<br>Pesados Por Caminos<br>No Pavimentados|Transporte Petróleo|2,7732|0,2773|9,0591|1,0122|0,1012|3,3066|
|Transito Vehículos<br>Pesados Por Caminos<br>No Pavimentados|Transporte Agua Potable|2,7732|0,2773|9,0591|0,8652|0,0865|2,8265|
|Transito Vehículos<br>Pesados Por Caminos<br>No Pavimentados|Transporte de Residuos<br>varios|2,7732|0,2773|9,0591|0,8652|0,0865|2,8265|
|Chancado|Chancado Primario|32,8767|32,8767|328,7671|12,0000|12,0000|120,0000|
|Harneado|Harnero Primario|7,0685|7,0685|19,7260|2,5800|2,5800|7,2000|
|Harneado|Harnero Secundario|14,7945|14,7945|61,6438|5,4000|5,4000|22,5000|
|Cintas Transportadoras<br>Cintas Transportadoras|Cinta transportadora de<br>alimentación harnero primario<br>(1 traspaso)|0,9041|0,9041|2,4658|0,3300|0,3300|0,9000|
|Cintas Transportadoras<br>Cintas Transportadoras|Cinta transportadora material<br>graba<br>(1 traspaso)|0,2260|0,2260|0,6164|0,0825|0,0825|0,2250|
|Cintas Transportadoras<br>Cintas Transportadoras|Cinta transportadora material<br>gravilla<br>(1 traspaso)|0,2260|0,2260|0,6164|0,0825|0,0825|0,2250|
|Cintas Transportadoras<br>Cintas Transportadoras|Cinta transportadora material<br>grueso<br>(1 traspaso)|0,2260|0,2260|0,6164|0,0825|0,0825|0,2250|
|Cintas Transportadoras<br>Cintas Transportadoras|Cinta transportadora al<br>harnero secundario<br>(1 traspaso)|0,2260|0,2260|0,6164|0,0825|0,0825|0,2250|
|Cintas Transportadoras<br>Cintas Transportadoras|Cinta transportadora acopio<br>arena<br>(1 traspaso)|0,2260|0,2260|0,6164|0,0825|0,0825|0,2250|

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 50

|Erosión en Pilas|Acopio de material grueso|0,1521|0,0228|0,3041|0,0555|0,0083|0,1110|
|---|---|---|---|---|---|---|---|
|Erosión en Pilas|Acopio de material graba|0,1521|0,0228|0,3041|0,0555|0,0083|0,1110|
|Erosión en Pilas|Acopio de material gravilla|0,1521|0,0228|0,3041|0,0555|0,0083|0,1110|
|Erosión en Pilas|Acopio de material arena|0,1521|0,0228|0,3041|0,0555|0,0083|0,1110|
|**TOTALES EMISIONES ETAPA DE OPERACIÓN**|**TOTALES EMISIONES ETAPA DE OPERACIÓN**|**134,62**|**65,37**|**678,01**|**48,84**|**23,83**|**246,51**|

**Tabla 39: Factores de Emisión (MP10, MP2.5 y MPS) - Actividades Etapa de Cierre**

|ACTIVIDAD|Actividad Específica|Emisiones Diarias (kg/día)|Col4|Col5|Emisiones Anuales (ton/año)|Col7|Col8|
|---|---|---|---|---|---|---|---|
|ACTIVIDAD|Actividad Específica|Emisiones<br>PM10|Emisiones<br>PM2.5|Emisiones<br>MPS|Emisiones<br>PM10|Emisiones<br>PM2.5|Emisiones<br>MPS|
|Reperfilado|Reperfilamiento área Planta|3,8154|0,5342|5,0873|0,0038|0,0005|0,0051|
|Reperfilado|Reperfilamiento área Camino|16,0248|2,2435|21,3665|0,0160|0,0022|0,0214|
|Tránsito Por Caminos<br>Pavimentados|Transporte Equipos Planta|1,6351|0,3956|8,5182|0,1472|0,0356|0,7666|
|Tránsito Por Caminos<br>Pavimentados|Transporte Estructura<br>Pesada|4,9052|1,1868|25,5547|0,4415|0,1068|2,2999|
|Tránsito Por Caminos<br>Pavimentados|Camión Grúa Para Montaje e<br>Instalación|1,6351|0,3956|8,5182|0,1472|0,0356|0,7666|
|Tránsito Por Caminos<br>Pavimentados|Transporte Petróleo|1,6351|0,3956|8,5182|0,1472|0,0356|0,7666|
|Tránsito Por Caminos<br>Pavimentados|Transporte Agua Potable|1,6351|0,3956|8,5182|0,1472|0,0356|0,7666|
|Tránsito Por Caminos<br>Pavimentados|Transporte de Personal y<br>Supervisión|0,2357|0,0570|1,2278|0,0212|0,0051|0,1105|
|Transito Vehículos<br>Livianos Por Caminos<br>No Pavimentados|Transporte de Personal y<br>Supervisión|1,9644|0,1964|6,4170|0,1768|0,0177|0,5775|
|Transito Vehículos<br>Pesados<br>Por Caminos No<br>Pavimentados|Transporte Equipos Planta|2,7732|0,2773|9,0591|0,2496|0,0250|0,8153|
|Transito Vehículos<br>Pesados<br>Por Caminos No<br>Pavimentados|Transporte Estructura<br>Pesada|8,3196|0,8320|27,1774|0,7488|0,0749|2,4460|
|Transito Vehículos<br>Pesados<br>Por Caminos No<br>Pavimentados|Camión Grúa Para Montaje e<br>Instalación|2,7732|0,2773|9,0591|0,2496|0,0250|0,8153|
|Transito Vehículos<br>Pesados<br>Por Caminos No<br>Pavimentados|Transporte Petróleo|2,7732|0,2773|9,0591|0,2496|0,0250|0,8153|
|Transito Vehículos<br>Pesados<br>Por Caminos No<br>Pavimentados|Transporte Agua Potable|2,7732|0,2773|9,0591|0,2496|0,0250|0,8153|
|**TOTALES EMISIONES ETAPA DE CIERRE**|**TOTALES EMISIONES ETAPA DE CIERRE**|**52,90**|**7,74**|**157,14**|**3,00**|**0,45**|**11,79**|

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 51

**Tabla 40: Emisiones de Gases y MP Combustión de Motores [kg/día] - Etapa de Construcción**

|Emisiones de Gases y Material Particulado Asociado a la Combustión de Motores [kg/día]|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|Equipo|Cantidad|Potencia<br>Nominal kw|Operación<br>Diaria (horas)|CO|HC|NOx|MP|
|Motoniveladora|1|137|12|0,04|0,02|0,17|0,01|
|**TOTAL**|**TOTAL**|**TOTAL**|**TOTAL**|**0,04**|**0,02**|**0,17**|**0,01**|

**Tabla 41: Emisiones de Gases y MP Combustión de Motores [kg/día] - Etapa de Operación**

|Emisiones de Gases y Material Particulado Asociado a la Combustión de Motores [kg/día]|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|Equipo|Cantidad|Potencia<br>Nominal kw|Operación<br>Diaria (horas)|CO|HC|NOx|MP|
|Excavadora de 1.5 m3|1|120|12|0,05|0,02|0,17|0,01|
|Cargador Frontal W190B|1|160|12|0,04|0,02|0,17|0,01|
|Cargador Frontal 721E|1|160|12|0,04|0,02|0,17|0,01|
|**TOTAL**|**TOTAL**|**TOTAL**|**TOTAL**|**0,117**|**0,053**|**0,517**|**0,041**|

**Tabla 42: Emisiones de Gases y MP Combustión de Motores [kg/día] - Etapa de Cierre**

|Equipo|Cantidad|Potencia<br>Nominal kw|Operación<br>Diaria (horas)|CO|HC|NOx|MP|
|---|---|---|---|---|---|---|---|
|Motoniveladora|1|137|12|0,04|0,02|0,17|0,01|
|**TOTAL**|**TOTAL**|**TOTAL**|**TOTAL**|0,04|0,02|0,17|0,01|

**Tabla 43: Emisiones de Gases y MP Asociado a Vehículos [kg/día] - Etapa de Construcción**

|Vehículo|N°<br>Viajes/día|Distancia<br>(km)|Velocidad<br>km/h|CO|HC|NOx|MP|
|---|---|---|---|---|---|---|---|
|Camión Transporte Petróleo|1|51,5|100|0,133|0,021|0,584|0,011|
|Camión Transporte Equipos Planta|1|51,5|100|0,133|0,021|0,584|0,011|
|Camión Transporte Estructura Pesada|3|51,5|100|0,398|0,063|1,752|0,033|
|Camión Grúa Para Montaje e<br>Instalación|1|51,5|100|0,133|0,021|0,584|0,011|
|Camión Transporte Agua Potable|1|51,5|100|0,133|0,021|0,584|0,011|
|Camionetas Transporte Personal y<br>Supervisión|2|51,5|100|0,119|0,014|0,217|0,021|
|**TOTALES**|**TOTALES**|**TOTALES**|**TOTALES**|**1,048**|**0,161**|**4,306**|**0,099**|

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 52

**Tabla 44: Emisiones de Gases y MP Asociado a Vehículos [kg/día] - Etapa de Operación**

|Vehículo|N°<br>Viajes/día|Distancia<br>(km)|Velocidad<br>km/h|CO|HC|NOx|MP|
|---|---|---|---|---|---|---|---|
|Camión Transporte Áridos|55|0,6|50|0,111|0,024|0,443|0,010|
|Camión Transporte Petróleo|1|51,5|100|0,133|0,021|0,584|0,011|
|Camión Transporte Agua Potable|1|51,5|100|0,133|0,021|0,584|0,011|
|Camión Transporte Residuos Varios|1|51,5|100|0,133|0,021|0,584|0,011|
|Camionetas Transporte Personal y<br>Supervisión|2|51,5|100|0,056|0,015|0,179|0,008|
|**TOTALES**|**TOTALES**|**TOTALES**|**TOTALES**|**0,322**|**0,057**|**1,348**|**0,031**|

**Tabla 45: Emisiones de Gases y MP Asociado a Vehículos [kg/día] - Etapa de Cierre**

|Vehículo|N°<br>Viajes/día|Distancia<br>(km)|Velocidad<br>km/h|CO|HC|NOx|MP|
|---|---|---|---|---|---|---|---|
|Camión Transporte Petróleo|1|51,5|100|0,133|0,021|0,584|0,011|
|Camión Transporte Equipos Planta|1|51,5|100|0,133|0,021|0,584|0,011|
|Camión Transporte Estructura Pesada|3|51,5|100|0,398|0,063|1,752|0,033|
|Camión Grúa Para Desmontaje de<br>~~Instalación~~|1|51,5|100|0,133|0,021|0,584|0,011|
|Camión Transporte Agua Potable|1|51,5|100|0,133|0,021|0,584|0,011|
|Camionetas Transporte Personal y<br>Supervisión|2|51,5|100|0,119|0,014|0,217|0,021|
|**TOTALES**|**TOTALES**|**TOTALES**|**TOTALES**|**1,048**|**0,161**|**4,306**|**0,099**|

**Tabla 46: Emisiones de Gases y Material Particulado Asociado a Combustión en Grupos**

**Generadores**

|Etapa Proyecto|Potencia<br>(kw)|Combustibles<br>(tipo)|Operación<br>(h/día)|Cantidad|CO|NOx|MP<br>10|SOx|
|---|---|---|---|---|---|---|---|---|
|Construcción|480|Diésel|12|1|23,39|108,29|7,72|7,20|
|Operación|480|Diésel|12|1|23,39|108,29|7,72|7,20|
|Cierre|480|Diésel|12|1|23,39|108,29|7,72|7,20|

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 53

**TABLAS RESUMEN DE EMISIONES POR FASES DEL PROYECTO**

**Tabla 47: Resumen Emisiones Fase de Construcción**

|Fase de Construcción|MP10|Col3|MP2,5|Col5|MPS|Col7|CO|Col9|HC|Col11|NOx|Col13|SO<br>X|Col15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Fase de Construcción**|kg/día|ton/año|kg/día|ton/año|kg/día|ton/año|kg/día|ton/año|kg/día|ton/año|kg/día|ton/año|kg/día|ton/año|
|Actividades|33,11|0,33|4,97|0,04|130,75|1,20|---|---|---|---|---|---|---|---|
|Maquinarias|---|---|---|---|0,01|0,00|0,04|0,00|0,02|0,00|0,17|0,02|---|---|
|Vehículos|---|---|---|---|0,10|0,01|1,05|0,09|0,16|0,01|4,31|0,39|---|---|
|Generadores|7,72|0,69|---|---|---|---|23,39|2,11|---|---|108,29|9,75|7,20|0,65|
|**TOTAL**|**40,83**|**1,02**|**4,97**|**0,04**|**130,86**|**1,21**|**24,47**|**2,20**|**0,18**|**0,02**|**112,77**|**10,15**|**7,20**|**0,65**|

**Tabla 48: Resumen Emisiones Fase de Operación**

|Fase de Construcción|MP10|Col3|MP2,5|Col5|MPS|Col7|CO|Col9|HC|Col11|NOx|Col13|SO<br>X|Col15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Fase de Construcción**|kg/día|ton/año|kg/día|ton/año|kg/día|ton/año|kg/día|ton/año|kg/día|ton/año|kg/día|ton/año|kg/día|ton/año|
|Actividades|134,62|48,84|65,37|23,83|678,01|246.51|---|---|---|---|---|---|---|---|
|Maquinarias|---|---|---|---|0,04|0,01|0,12|0,04|0,05|0,02|0,52|0,19|---|---|
|Vehículos|---|---|---|---|0,03|0,01|0,32|0,12|0,06|0,02|1,35|0,49|---|---|
|Generadores|7,72|2,82|---|---|---|---|23,39|8,54|---|---|108,29|39,53|7,20|2,63|
|**TOTAL**|**142,34**|**51,66**|**65,37**|**23,83**|**678,08**|**0,03**|**23,83**|**8,70**|**0,11**|**0,04**|**110,16**|**40,21**|**7,20**|**2,63**|

**Tabla 49: Resumen Emisiones Fase de Cierre**

|Fase de Construcción|MP10|Col3|MP2,5|Col5|MPS|Col7|CO|Col9|HC|Col11|NOx|Col13|SO<br>X|Col15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Fase de Construcción**|kg/día|ton/año|kg/día|ton/año|kg/día|ton/año|kg/día|ton/año|kg/día|ton/año|kg/día|ton/año|kg/día|ton/año|
|Actividades|33,66|3,03|5,05|0,45|131,49|11.86|---|---|---|---|---|---|---|---|
|Maquinarias|---|---|---|---|0,01|0,00|0,04|0,00|0,02|0,00|0,17|0,02|||
|Vehículos|---|---|---|---|0,10|0,01|1,05|0,09|0,16|0,01|4,31|0,39|||
|Generadores|7,72|0,69|---|---|---|---|23,39|2,11|---|---|108,29|9,75|7,20|0,65|
|**TOTAL**|**41,38**|**3,72**|**5,05**|**0,45**|**131,60**|**0,01**|**24,47**|**2,20**|**0,18**|**0,02**|**112,77**|**10,15**|**7,20**|**0,65**|

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 54

**11. RESULTADOS DE LA MODELACIÓN**

Mediante la aplicación del modelo CALPUFF fue posible obtener las concentraciones de
material particulado respirable (MP 10 ), material particulado respirable fino (MP 2,5 ), material
particulado sedimentable (MPS), y concentraciones de gases (SO 2, NOx, CO y HC), que
aportará el Proyecto en su etapa de construcción, operación y cierre. A continuación se
presentan los resultados del modelo, análisis de los resultados y mapas de

Isoconcentración.

**11.1 Resultados del Modelo**

Las siguientes tablas resúmenes, presentan los resultados obtenidos de la modelación para
cada etapa del proyecto. Cabe señalar, que no se ha realizado el análisis de cumplimiento
de la normativa para material particulado MP 2.5 ni MPS, debido a que no se cuenta con
registros de línea de base para dichos contaminante.

**11.1.1 Cumplimiento Normas De Calidad Ambiental Primaria**

Las siguientes tablas presentan las concentraciones de cada contaminante en cada uno de
los receptores y su nivel respecto de la norma respectiva:

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 55

**Tabla 50: Aportes del Proyecto Etapa de Construcción**

|Parámetro|Estadístico|Limite Norma<br>(μg/m3N)|Concentración<br>(μg/m3N)<br>Calama|% Respecto<br>de la Norma|Concentración<br>(μg/m3N)<br>San Pedro|% Respecto<br>de la Norma|Concentración<br>(μg/m3N)<br>Chiu-Chiu|% Respecto<br>de la Norma|
|---|---|---|---|---|---|---|---|---|
|MP10|Percentil 98 Promedio 24 horas|150|0,07760|**0,1**|0,01650|**0,0**|0,00616|**0,0**|
|MP10|Promedio Anual|50|0,01430|**0,0**|0,00201|**0,0**|0,00067|**0,0**|
|MP2,5|Percentil 98 Promedio Diario|50|0,01900|**0,0**|0,00100|**0,0**|0,00100|**0,0**|
|MP2,5|Promedio Trianual|20|0,00300|**0,0**|0,00000|**0,0**|0,00000|**0,0**|
|CO|Percentil 99, máx. 1 hora|30000|0,04990|**0,0**|0,09370|**0,0**|0,04160|**0,0**|
|CO|Percentil 99, máx. 8 hora|10000|0,01210|**0,0**|0,04630|**0,0**|0,01020|**0,0**|
|NO2|Percentil 99, máx. 1 hora|400|0,16500|**0,0**|0,32000|**0,1**|0,12300|**0,0**|
|NO2|Promedio, Anual|100|0,00221|**0,0**|0,00983|**0,0**|0,00122|**0,0**|
|SO2|Promedio Diario, percentil 99|250|0,00067|**0,0**|0,00288|**0,0**|0,00044|**0,0**|
|SO2|Promedio, Anual|80|0,00007|**0,0**|0,00035|**0,0**|0,00004|**0,0**|

**Tabla 51: Aportes del Proyecto Etapa de Operación**

|Parámetro|Estadístico|Limite Norma<br>(μg/m3N)|Concentración<br>(μg/m3N)<br>Calama|% Respecto<br>de la Norma|Concentración<br>(μg/m3N)<br>San Pedro|% Respecto<br>de la Norma|Concentración<br>(μg/m3N)<br>Chiu-Chiu|% Respecto<br>de la Norma|
|---|---|---|---|---|---|---|---|---|
|MP10|Percentil 98 Promedio 24 horas|150|0,17000|**0,1**|0,72200|**0,5**|0,11200|**0,1**|
|MP10|Promedio Anual|50|0,02060|**0,0**|0,07620|**0,2**|0,01090|**0,0**|
|MP2,5|Percentil 98 Promedio Diario|50|0,15100|**0,3**|0,66100|**1,3**|0,10100|**0,2**|
|MP2,5|Promedio Trianual|20|0,01720|**0,1**|0,06940|**0,3**|0,00981|**0,0**|
|CO|Percentil 99, máx. 1 hora|30000|0,26400|**0,0**|0,47200|**0,0**|0,22100|**0,0**|
|CO|Percentil 99, máx. 8 hora|10000|0,09040|**0,0**|0,22700|**0,0**|0,05560|**0,0**|
|NO2|Percentil 99, máx. 1 hora|400|0,81100|**0,2**|1,54000|**0,4**|0,59200|**0,1**|

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 56

|NO2|Promedio, Anual|100|0,01220|0,0|0,04170|0,0|0,00660|0,0|
|---|---|---|---|---|---|---|---|---|
|SO2|Promedio Diario, percentil 99|250|0,00067|**0,0**|0,00288|**0,0**|0,00044|**0,0**|
|SO2|Promedio, Anual|80|0,00008|**0,0**|0,00032|**0,0**|0,00005|**0,0**|

**Tabla 52: Aportes del Proyecto Etapa de Cierre**

|Parámetro|Estadístico|Limite Norma<br>(μg/m3N)|Concentración<br>(μg/m3N)<br>Calama|% Respecto<br>de la Norma|Concentración<br>(μg/m3N)<br>San Pedro|% Respecto<br>de la Norma|Concentración<br>(μg/m3N)<br>Chiu-Chiu|% Respecto<br>de la Norma|
|---|---|---|---|---|---|---|---|---|
|MP10|Percentil 98 Promedio 24 horas|150|0,07760|**0,1**|0,01650|**0,0**|0,00616|**0,0**|
|MP10|Promedio Anual|50|0,01430|**0,0**|0,00201|**0,0**|0,00067|**0,0**|
|MP2,5|Percentil 98 Promedio Diario|50|0,01880|**0,0**|0,00146|**0,0**|0,00135|**0,0**|
|MP2,5|Promedio Trianual|20|0,00342|**0,0**|0,00019|**0,0**|0,00013|**0,0**|
|CO|Percentil 99, máx. 1 hora|30000|0,05080|**0,0**|0,09540|**0,0**|0,04230|**0,0**|
|CO|Percentil 99, máx. 8 hora|10000|0,01230|**0,0**|0,04710|**0,0**|0,01040|**0,0**|
|NO2|Percentil 99, máx. 1 hora|400|0,16900|**0,0**|0,32600|**0,1**|0,12600|**0,0**|
|NO2|Promedio, Anual|100|0,00225|**0,0**|0,01000|**0,0**|0,00124|**0,0**|
|SO2|Promedio Diario, percentil 99|250|0,00067|**0,0**|0,00288|**0,0**|0,00044|**0,0**|
|SO2|Promedio, Anual|80|0,00007|**0,0**|0,00035|**0,0**|0,00004|**0,0**|

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 57

**11.1.2 Cumplimiento Normas De Calidad Ambiental Secundaria**

**Tabla 53: Aportes del Proyecto Etapa de Construcción**

|Parámetro|Estadístico|Limite Norma|Aporte en<br>Calama|% Respecto<br>de la Norma|Aporte en San<br>Pedro|% Respecto<br>de la Norma|Aporte en<br>Chiu-Chiu|% Respecto<br>de la Norma|
|---|---|---|---|---|---|---|---|---|
|MPS|Promedio Mensual|150|0.002|**0,0**|0.0003|**0,0**|0.0001|**0,0**|
|MPS|Promedio Anual|100|0.0005|**0,0**|0.00004|**0,0**|0.00002|**0,0**|
|SO2|Promedio Anual|80|0,00007|**0,0**|0,00035|**0,0**|0,00004|**0,0**|
|SO2|Percentil 99.7 Concentración Diaria|365|0,00067|**0,0**|0,00288|**0,0**|0,00044|**0,0**|
|SO2|Percentil 99.73 Concentración 1 hora|1000|0,00561|**0,0**|0,01120|**0,0**|0,00423|**0,0**|

Nota 1: Los aportes de MPS en cada uno de los receptores, se expresan en mg/m [2] día

Nota 2: Los aportes de SO 2 en cada uno de los receptores, se expresan en μ g/m [3] N

**Tabla 54: Aportes del Proyecto Etapa de Operación**

|Parámetro|Estadístico|Limite Norma|Aporte en<br>Calama|% Respecto<br>de la Norma|Aporte en San<br>Pedro|% Respecto<br>de la Norma|Aporte en<br>Chiu-Chiu|% Respecto<br>de la Norma|
|---|---|---|---|---|---|---|---|---|
|MPS|Promedio Mensual|150|0.007|**0,0**|0.036|**0,0**|0.004|**0,0**|
|MPS|Promedio Anual|100|0.001|**0,0**|0.003|**0,0**|0.0005|**0,0**|
|SO2|Promedio Anual|80|0,00008|**0,0**|0,00032|**0,0**|0,00005|**0,0**|
|SO2|Percentil 99.7 Concentración Diaria|365|0,00067|**0,0**|0,00288|**0,0**|0,00044|**0,0**|
|SO2|Percentil 99.73 Concentración 1 hora|1000|0,00561|**0,0**|0,01120|**0,0**|0,00423|**0,0**|

Nota 1: Los aportes de MPS en cada uno de los receptores, se expresan en mg/m [2] día

Nota 2: Los aportes de SO 2 en cada uno de los receptores, se expresan en μ g/m [3] N

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 58

**Tabla 55: Aportes del Proyecto Etapa de Cierre**

|Parámetro|Estadístico|Limite Norma|Aporte en<br>Calama|% Respecto<br>de la Norma|Aporte en San<br>Pedro|% Respecto<br>de la Norma|Aporte en<br>Chiu-Chiu|% Respecto<br>de la Norma|
|---|---|---|---|---|---|---|---|---|
|MPS|Promedio Mensual|150|0.002|**0,0**|0.0003|**0,0**|0.0001|**0,0**|
|MPS|Promedio Anual|100|0.0005|**0,0**|0.00004|**0,0**|0.00002|**0,0**|
|SO2|Promedio Anual|80|0,00225|**0,0**|0,01000|**0,0**|0,00124|**0,0**|
|SO2|Percentil 99.7 Concentración Diaria|365|0,00067|**0,0**|0,00288|**0,0**|0,00044|**0,0**|
|SO2|Percentil 99.73 Concentración 1 hora|1000|0,00561|**0,0**|0,01120|**0,0**|0,00423|**0,0**|

Nota 1: Los aportes de MPS en cada uno de los receptores, se expresan en mg/m [2] día

Nota 2: Los aportes de SO 2 en cada uno de los receptores, se expresan en μ g/m [3] N

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 59

**12. ANÁLISIS DE INCERTIDUMBRE**

**12.1 Análisis Cualitativo de los Campos de Vientos**

Respecto de la dirección de los vientos en la estaciones, no existen mayores diferencias
entre lo observado y lo modelado.

De acuerdo con la información presentada en el apartado 3.3 (Campos de Vientos), los
campos de vientos provienen principalmente de la dirección SWW y en segundo lugar los

vientos de dirección EES

Al comparar los datos anteriores con los campos de vientos generados por el modelo
utilizando meteorología WRF, se aprecia que existe bastante similitud con el modelo de
pronóstico.

Conforme a lo anterior, se puede concluir que en gran parte del día coinciden las direcciones

de los vientos.

A partir de lo anterior se puede sostener que el modelo meteorológico predice de buena
forma el comportamiento espacial de los flujos de viento, ya que las diferencias entre las
direcciones del viento se manejan en un rango aceptable de variación.

**12.2 Análisis Cuantitativo para el Cálculo de Incertidumbre**

El análisis cuantitativo consiste en determinar el % de variación que experimenta la
velocidad promedio del viento entre los valores utilizados en el modelo versus los valores

observados de velocidad del viento.

De acuerdo a los datos registrados en la Estación Centro de Codelco, la velocidad promedio
del viento registrada por dicha estación, (considerando un universo de 7.778 datos, que
representan el 88.8% del total de datos de un año), es de 2.97 m/s

Al modelar con WRF en el punto de localización de la Estación Centro, el modelo arroja un
valor promedio de velocidad del viento para el mismo período de 3.35 m/s

Las velocidades promedios registradas en las estaciones de monitoreo (valor observado)
versus las representadas por el modelo (valor modelado) se tiene que:

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 60

**Tabla 56: Velocidad promedio del Viento en m/s**

|Estación|Promedio Observado|Promedio Pronostico<br>WRF|% de Variación|
|---|---|---|---|
|Estación Centro|2.97|3.35|12.8|

_% Error_
_V_ = % de error entre los valores modelado y observado de la velocidad del viento.

(Valor modelado) = 3.35 m/s
(Valor observado) = 2.97 m/s

−2, 97 [m] s
% de error= [3, 35 m] [s] x100

2, 97 ~~[m]~~ s

% de error= 12, 8

Conforme a lo anterior, se observa que el modelo sobrestima las velocidades de los vientos
con respecto a los datos observados de la Estación Centro, en un 12.8%.

Dado que el error (12.8%), es relativamente pequeño se puede decir que la velocidad media
considerada en el modelamiento es representativa ante la situación observada. Luego, a
partir de la comparación de los campos de vientos modelados con los registros de la
estación meteorológica Estación Centro, se puede sostener que el modelo meteorológico
CALMET predice de manera adecuada el comportamiento espacial del flujo de vientos en el
área de modelación, por lo que los resultados obtenidos del modelo son representativos del
escenario que generaría la implementación del Proyecto.

**13. ANÁLISIS DE CUMPLIMIENTO NORMATIVO VIGENTE**

El presente estudio de dispersión de emisiones atmosféricas ha considerado 3 receptores
de interés (asentamientos humanos) que corresponden a las localidades de Calama, San
Pedro de Atacama y Chiu-Chiu. Sobre estas localidades se ha determinado el nivel de
impacto que generara el proyecto en cada una de sus etapas.

**13.1. Análisis de Cumplimiento Normativo vigente para MP** **10**

Se puede observar que el proyecto, en su etapa de construcción, no genera impacto

% de error= [3, 35 m] −2, 97 [s] [m] s

x100
2, 97 ~~[m]~~ s

% de error= 12, 8

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 61

(respecto del percentil 98 promedio 24 horas), en ninguno de los receptores analizados.

La calidad del aire de Calama, San Pedro de Atacama y Chiu Chiu, con aportes de 0,07760,
0,01650 y 0,00616 μg/m3N respectivamente, lo que representa aproximadamente el 0,1 0,0 y 0,0% del percentil 98 promedio 24 horas establecido en la Norma Primaria de MP10.
En la etapa de operación, el aporte en los mismos receptores anteriores, se presenta en
0,17000 - 0,72200 y 0,11200 μg/m3N, representando un 0.1 - 0,5 y 0,1% en comparación al
percentil 98 promedio 24 horas establecido en la Norma Primaria de MP10. En la etapa de
Cierre se presentan los mismos valores que en la etapa de construcción por lo que no se
presenta impacto.

Respecto del promedio anual establecido en la Norma Primaria DS 20/2013, el proyecto no
presenta impactos, ya que el mayor valor obtenido es inferior a 1 μg/m [3] N

**13.2. Análisis de Cumplimiento Normativo vigente para MP** **2,5**

Se puede observar que el proyecto, no presenta impactos en la calidad del aire, ya que
todos los valores obtenidos son inferiores a 1 μg/m [3] N

**13.3. Análisis de Cumplimiento Normativo vigente para MPS**

No existen zonas biológicas de interés cercanas al área del proyecto por lo que se han
defino como receptores biológicos los mismos receptores humanos anteriormente
analizados. Respecto de ello, puede señalarse que en ninguno de los tres receptores se
presenta impacto por este concepto, el aporte es nulo en todos los receptores.

**13.4. Análisis de Cumplimiento Normativo vigente para Gases CO**

El análisis efectuado en cada etapa del proyecto, indica que el aporte de gases CO en cada
uno de los 3 receptores analizados, es muy bajo, alcanzando un valor máximo de 0.47
μg/m [3] N que representa un 0.0003% del valor de la norma (DS 115/2002)

**13.5. Análisis de Cumplimiento Normativo vigente para Gases NO2**

El análisis efectuado en cada etapa del proyecto, indica que el mayor aporte de gases NO 2
generado por el proyecto, se presenta en la etapa de operación, con 1.54 μg/m [3] N que

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 62

representa un 0.4 % del percentil 99, máx. 1 hora. Sin embargo respecto del promedio
anual, el aporte representa menos del 1%

**13.6. Análisis de Cumplimiento Normativo vigente para Gases SO2**

El análisis efectuado en cada etapa del proyecto, indica que no existe aporte de gases SO 2
en ninguno de los 3 receptores analizados, por lo tanto el proyecto no presenta efecto
sinérgico con otros proyectos evaluados en la zona y cumple 100% con la Norma Primaria
establecida en el DS 113/2002 y la Norma Secundaria establecida en el DS 185/1991.

**13.7 Puntos de Máximo Impacto**

De acuerdo con los resultados de la modelación, los puntos de máximo impacto generados
por el proyecto en la etapa de operación (etapa en la que se generan las máximas
emisiones), se localizan en las siguientes coordenadas UTM WGS84:

**Tabla 57: Puntos de Máximo Impacto - Etapa de Construcción**

|Parámetro|Estadístico|Coordenada WGS-84|Col4|Concentración<br>(μg/m3N)|
|---|---|---|---|---|
|Parámetro|Estadístico|Este|Norte|Norte|
|MP10|Percentil 98 Promedio 24 horas|552136|7492499|9.12|
|MP10|Promedio Anual|552136|7492499|1.55|
|MP2,5|Percentil 98 Promedio Diario|552136|7492499|0.93|
|MP2,5|Promedio Trianual|552136|7492499|0.15|
|CO|Percentil 99, máx. 1 hora|552136|7492499|171.3|
|CO|Percentil 99, máx. 8 hora|552136|7492499|36.02|
|NO2|Percentil 99, máx. 1 hora|552136|7492499|557.26|
|NO2|Promedio, Anual|552136|7492499|9.15|
|SO2|Percentil 99.73 Conc. 1 hora|552136|7492499|5.12|
|SO2|Promedio Diario, percentil 99|552136|7492499|0.49|
|SO2|Promedio, Anual|552136|7492499|0.1|

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 63

**Tabla 58: Puntos de Máximo Impacto - Etapa de Operación**

|Parámetro|Estadístico|Coordenada WGS-84|Col4|Concentración<br>(μg/m3N)|
|---|---|---|---|---|
|Parámetro|Estadístico|Este|Norte|Norte|
|MP10|Percentil 98 Promedio 24 horas|552136|7492499|321.49|
|MP10|Promedio Anual|552136|7492499|54.14|
|MP2,5|Percentil 98 Promedio Diario|552136|7492499|2.94|
|MP2,5|Promedio Trianual|552136|7492499|44.54|
|CO|Percentil 99, máx. 1 hora|552136|7492499|1.629,5|
|CO|Percentil 99, máx. 8 hora|552136|7492499|332.89|
|NO2|Percentil 99, máx. 1 hora|552136|7492499|5.367,3|
|NO2|Promedio, Anual|552136|7492499|71.28|
|SO2|Percentil 99.73 Conc. 1 hora|552136|7492499|5.12|
|SO2|Promedio Diario, percentil 99|552136|7492499|0.49|
|SO2|Promedio, Anual|552136|7492499|0.09|

**Tabla 59: Puntos de Máximo Impacto - Etapa de Cierre**

|Parámetro|Estadístico|Coordenada WGS-84|Col4|Concentración<br>(μg/m3N)|
|---|---|---|---|---|
|Parámetro|Estadístico|Este|Norte|Norte|
|MP10|Percentil 98 Promedio 24 horas|552136|7492499|9.16|
|MP10|Promedio Anual|552136|7492499|1.56|
|MP2,5|Percentil 98 Promedio Diario|552136|7492499|0.93|
|MP2,5|Promedio Trianual|552136|7492499|0.15|
|CO|Percentil 99, máx. 1 hora|552136|7492499|171.3|
|CO|Percentil 99, máx. 8 hora|552136|7492499|35.02|
|NO2|Percentil 99, máx. 1 hora|552136|7492499|557.26|
|NO2|Promedio, Anual|552136|7492499|9.23|
|SO2|Percentil 99.73 Conc. 1 hora|552136|7492499|5.0|
|SO2|Promedio Diario, percentil 99|552136|7492499|0.49|
|SO2|Promedio, Anual|552136|7492499|0.1|

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 64

**14. CONCLUSIONES**

Los resultados obtenidos de la modelación realizada y el análisis efectuado en los apartados
anteriores, indican que el proyecto, en general, no presenta impactos en la calidad del aire
en ninguno de los tres receptores analizados, y por tanto, no compromete la salud de la
población.

Con respecto a si generan efectos adversos significativos sobre los recursos naturales del
sector, al igual que en el caso anterior, no se presentan impactos en ninguna de las zonas
analizadas, en consecuencia, no se presentan efectos adversos significativos sobre los

recursos naturales.

**15. MAPAS DE ISOCONCENTRACIONES**

En las siguientes figuras se presentan las curvas de Isoconcentración para la etapa de
mayores emisiones y que corresponde a la etapa de operación. Como puede apreciarse en
las tablas de resultados y láminas de Isoconcentración, el proyecto no genera ningún tipo
impactos significativos en la calidad del aire en zona poblada.

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 65

**Figura 24: Mapa de Isoconcentración Material Particulado MP10 - Etapa de Construcción (24 h)**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 66

**Figura 25: Mapa de Isoconcentración Material Particulado MP10 - Etapa de Construcción (Anual)**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 67

**Figura 26: Mapa de Isoconcentración Material Particulado MP2.5 - Etapa de Construcción (24 h)**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 68

**Figura 27: Mapa de Isoconcentración Material Particulado MP2.5 - Etapa de Construcción (Anual)**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 69

**Figura 28: Mapa de Isoconcentración Gases CO - Etapa de Construcción (1h)**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 70

**Figura 29: Mapa de Isoconcentración Gases CO - Etapa de Construcción (8h)**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 71

**Figura 30: Mapa de Isoconcentración Gases NO2 - Etapa de Construcción (1 h)**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 72

**Figura 31: Mapa de Isoconcentración Gases NO2 - Etapa de Construcción (Anual)**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 73

**Figura 32: Mapa de Isoconcentración Gases SO2 - Etapa de Construcción (1h)**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 74

**Figura 33: Mapa de Isoconcentración Gases SO2 - Etapa de Construcción (24h)**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 75

**Figura 34: Mapa de Isoconcentración Gases SO2 - Etapa de Construcción (Anual)**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 76

**Figura 35: Mapa de Isodepositación Material Particulado Sedimentable MPS - Etapa de Construcción (24h)**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 77

**Figura 36: Mapa de Isodepositación Material Particulado Sedimentable MPS - Etapa de Construcción (Anual)**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 78

**Figura 37: Mapa de Isoconcentración Material Particulado MP10 - Etapa de Operación (24 h)**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 79

**Figura 38: Mapa de Isoconcentración Material Particulado MP10 - Etapa de Operación (Anual)**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 80

**Figura 39: Mapa de Isoconcentración Material Particulado MP2.5 - Etapa de Operación (24 h)**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 81

**Figura 40: Mapa de Isoconcentración Material Particulado MP2.5 - Etapa de Operación (Anual)**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 82

**Figura 41: Mapa de Isoconcentración Gases CO - Etapa de Operación (1h)**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 83

**Figura 42: Mapa de Isoconcentración Gases CO - Etapa de Operación (8h)**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 84

**Figura 43: Mapa de Isoconcentración Gases NO2 - Etapa de Operación (1 h)**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 85

**Figura 44: Mapa de Isoconcentración Gases NO2 - Etapa de Operación (Anual)**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 86

**Figura 45: Mapa de Isoconcentración Gases SO2 - Etapa de Operación (1h)**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 87

**Figura 46: Mapa de Isoconcentración Gases SO2 - Etapa de Operación (24h)**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 88

**Figura 47: Mapa de Isoconcentración Gases SO2 - Etapa de Operación (Anual)**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 89

**Figura 48: Mapa de Isodepositación Material Particulado Sedimentable MPS - Etapa de Operación (24h)**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 90

**Figura 49: Mapa de Isodepositación Material Particulado Sedimentable MPS - Etapa de Operación (Anual)**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 91

**Figura 50: Mapa de Isoconcentración Material Particulado MP10 - Etapa de Cierre (24 h)**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 92

**Figura 51: Mapa de Isoconcentración Material Particulado MP10 - Etapa de Cierre (Anual)**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 93

**Figura 52: Mapa de Isoconcentración Material Particulado MP2.5 - Etapa de Cierre (24 h)**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 94

**Figura 53: Mapa de Isoconcentración Material Particulado MP2.5 - Etapa de Cierre (Anual)**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 95

**Figura 54: Mapa de Isoconcentración Gases CO - Etapa de Cierre (1h)**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 96

**Figura 55: Mapa de Isoconcentración Gases CO - Etapa de Cierre (8h)**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 97

**Figura 56: Mapa de Isoconcentración Gases NO2 - Etapa de Cierre (1 h)**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 98

**Figura 57: Mapa de Isoconcentración Gases NO2 - Etapa de Cierre (Anual)**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 99

**Figura 58: Mapa de Isoconcentración Gases SO2 - Etapa de Cierre (1h)**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 100

**Figura 59: Mapa de Isoconcentración Gases SO2 - Etapa de Cierre (24h)**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 101

**Figura 60: Mapa de Isoconcentración Gases SO2 - Etapa de Cierre (Anual)**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 102

**Figura 61: Mapa de Isodepositación Material Particulado Sedimentable MPS - Etapa de Cierre (24h)**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 103

**Figura 62: Mapa de Isodepositación Material Particulado Sedimentable MPS - Etapa de Cierre (Anual)**

Informe de Emisiones
Proyecto Extracción y Procesamiento de Áridos Sector Aguada de la Teca 104