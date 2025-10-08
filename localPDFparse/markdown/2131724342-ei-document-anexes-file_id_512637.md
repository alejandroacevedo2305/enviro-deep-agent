---
title: CAPÍTULO 1
author: Jorge
date: D:20160818121608-03'00'
language: es
type: report
pages: 120
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - INFORME MODELAMIENTO DE LA DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS
-->

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

# INFORME MODELAMIENTO DE LA DISPERSIÓN DE CONTAMINANTES ATMOSFERICOS

## PROYECTO NAVIO II

### Preparada para: EXSA Chile SpA

Napoleón 3200, oficina 1003, Las Condes

### Preparada por: BORDOLI & Consultores Asociados EIRL

Av. O’Higgins 1338, Oficina 1002, Antofagasta
Teléfono (56-55) 2255181
Web: www.bordoli.cl
E mail: jbordoli@bordoli.cl

Agosto 2016

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 1
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**INDICE DE MATERIAS**

1. INTRODUCCIÓN ............................................................................................................................................................... 5

2. DESCRIPCIÓN Y JUSTIFICACIÓN DEL MODELO ........................................................................................................ 10

3. ESCENARIO METEOROLÓGICO ................................................................................................................................... 12

3.1 DATOS OBSERVADOS ............................................................................................................................................ 27

3.2 SERIES DE TIEMPO. ................................................................................................................................................ 28

3.3 CAMPOS DE VIENTO ............................................................................................................................................... 30

3.4 CALIDAD DEL AIRE EN ANTOFAGASTA ................................................................................................................ 30
4. BASES DE DATOS Y ARCHIVOS DE MODELACIÓN .................................................................................................... 32

4.1 ARCHIVOS DE ENTRADA Y SALIDA DE LA MODELACIÓN .................................................................................. 32
5. CARACTERÍSTICAS DEL DOMINIO DE MODELACIÓN Y SU ENTORNO ................................................................... 33

5.1 LOCALIZACIÓN ........................................................................................................................................................ 33
5.2 ÁREA DE MODELAMIENTO ..................................................................................................................................... 34

5.3 GRILLA DE MODELAMIENTO .................................................................................................................................. 35
5.4 TOPOGRAFÍA DEL ÁREA DE MODELAMIENTO .................................................................................................... 36
5.5 RECEPTORES EN EL ÁREA DE MODELAMIENTO ............................................................................................... 37
5.6 SUELOS DEL ÁREA DE MODELAMIENTO ............................................................................................................. 38
6. FUENTES DE EMISIÓN .................................................................................................................................................. 39

6.1 ACTIVIDADES EMISORAS ....................................................................................................................................... 39

6.1.1 Fase de Construcción ......................................................................................................................................... 39
6.1.2 Fase de Operación .............................................................................................................................................. 41
6.1.3 Fase de Cierre ..................................................................................................................................................... 43

6.2 PESO PROMEDIO DE LA FLOTA ............................................................................................................................ 45
6.3 METODOLOGÍA PARA LA ESTIMACIÓN DE EMISIONES .................................................................................... 47
6.3.1 Metodología para la estimación de emisiones de las actividades ....................................................................... 47
6.3.2 Metodología para la estimación de emisiones de maquinarias ........................................................................... 48
6.3.3 Metodología para la estimación de emisiones de vehículos ............................................................................... 48
6.3.4 Metodología para la estimación de emisiones de Ggeneradores Eléctricos ....................................................... 49
6.3.5 Metodología para la estimación de emisiones por combustión en Calderas a GLP .......................................... 49
7. FACTORES DE EMISIÓN ................................................................................................................................................ 50

7.1 FACTORES DE EMISIÓN PARA MATERIAL PARTICULADO RESUSPENDIDO ................................................... 50
7.2 FACTORES DE EMISIÓN PARA LA ESTIMACIÓN DE EMISIONES DE GASES Y MATERIAL PARTICULADO. . 53

8. NIVELES DE ACTIVIDAD ................................................................................................................................................ 55

9. MEDIDAS DE MITIGACIÓN CAMINOS ........................................................................................................................... 57

10. RESULTADOS INVENTARIO DE EMISIONES ............................................................................................................... 59

11. RESULTADOS DE LA MODELACIÓN ............................................................................................................................ 68

11.1 RESULTADOS DEL MODELO .................................................................................................................................. 68

11.1.1 Cumplimiento Normas De Calidad Ambiental Primaria ....................................................................................... 68
11.1.2 Cumplimiento Normas de Calidad Ambiental Secundaria .................................................................................... 71
12. ANÁLISIS DE INCERTIDUMBRE .................................................................................................................................... 73

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 2
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

12.1 ANÁLISIS CUALITATIVO DE LOS CAMPOS DE VIENTOS .................................................................................... 73
12.2 ANÁLISIS CUANTITATIVO PARA EL CÁLCULO DE INCERTIDUMBRE ................................................................ 73

12.3 AJUSTE EMISIONES DEL PROYECTO ................................................................................................................... 74
13. ANÁLISIS DE CUMPLIMIENTO NORMATIVO VIGENTE ............................................................................................... 78

13.1 ANÁLISIS DE CUMPLIMIENTO NORMATIVO VIGENTE PARA MP10 ................................................................... 78
13.2 ANÁLISIS DE CUMPLIMIENTO NORMATIVO VIGENTE PARA MP2,5 .................................................................. 78
13.3 ANÁLISIS DE CUMPLIMIENTO NORMATIVO VIGENTE PARA MPS ..................................................................... 78
13.4 ANÁLISIS DE CUMPLIMIENTO NORMATIVO VIGENTE PARA GASES CO .......................................................... 78
13.5 ANÁLISIS DE CUMPLIMIENTO NORMATIVO VIGENTE PARA GASES NO2 ........................................................ 78
13.6 ANÁLISIS DE CUMPLIMIENTO NORMATIVO VIGENTE PARA GASES SO2 ........................................................ 79
13.7 PUNTOS DE MÁXIMO IMPACTO ............................................................................................................................. 79

14. CONCLUSIONES ............................................................................................................................................................. 80

15. MAPAS DE ISOCONCENTRACIONES ........................................................................................................................... 81

**INDICE DE TABLAS**

Tabla 1: Normas de Calidad Ambiental Primarias y Secundarias .............................................................................................. 9

<!-- INICIO TABLA 1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Informe de Emisiones Declaración de Impacto Ambiental Proyecto NAVÍO II -->

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
| CO | Percentil 99,máx.8 horas12 | 10.000 (μg/m3N) | NP DS 115/2002 |
| CO | Percentil 99, máx. 1 hora13 | 30.000 (μg/m3N) | NP DS 115/2002 |

<!-- Estadísticas: 15 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- 1 Promedio Anual: se refiere a la concentración promedio anual. Se considera sobrepasada la norma cuando la concentración anual calculada como promedio aritmético de tres años calendario consecutivos, sea mayor o igual a lo indicado a la tabla. -->
<!-- FIN TABLA 1 -->


Tabla 2: Información de la Orden de los Datos WRF ............................................................................................................... 13

Tabla 3: Información General de la Estación Meteorológica .................................................................................................... 28

Tabla 4: Información para el modelamiento .............................................................................................................................. 31

<!-- INICIO TABLA 4 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Proyecto NAVÍO II A continuación se presentan los resultados obtenidos del monitoreo realizado y el análisis comparativo con respecto a la normativa vigente: -->

**Tabla 4: Información para el modelamiento****

| Contaminantes | Norma de calidad del aire | Valores Normados | 2013<br>(no válido) | 2014<br>(válido) | 2015<br>(válido) |
| --- | --- | --- | --- | --- | --- |
| MP2,5 | D.S. N° 12/2011 | Promedio Anual: 20 μg/m3 | 13,74 (referencial) | 13,74 (referencial) | 13,74 (referencial) |
| MP2,5 | D.S. N° 12/2011 | P98 24 horas: 50 μg/m3 | 44,14 | 26,73 | 23,97 |
| MP10 | D.S. N° 59/1998, modificado<br>por D.S. N° 45/2001 | Promedio Anual: 50 μg/m3 | 40,89 (referencial) | 40,89 (referencial) | 40,89 (referencial) |
| MP10 | D.S. N° 59/1998, modificado<br>por D.S. N° 45/2001 | P98 24 horas: 150 μg/m3 | 80,76 | 65,04 | 66,63 |

<!-- Estadísticas: 4 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- **BORDOLI & Consultores EIRL** Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 31 Antofagasta -->
<!-- FIN TABLA 4 -->


Tabla 5: Información para el modelamiento .............................................................................................................................. 32

Tabla 6: Archivos de entrada y salida de la modelación ........................................................................................................... 32

<!-- INICIO TABLA 6 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **4.1 Archivos de entrada y salida de la modelación** Los archivos de entrada y salida de la modelación, para cada etapa del proyecto y que se anexan en forma digital (DVD), son los siguientes: -->

**Tabla 6: Archivos de entrada y salida de la modelación****

| CALMET | GEO.DAT |
| --- | --- |
| CALMET | CALMET.DAT |
| CALMET | CALMET.LST |
| CALMET | CALMET.INP |
| CALPUF | CALPUFF.LST |
| CALPUF | CALPUFF.INP |
| CALPUF | CONS.INP |
| CALPOST | CALPOST.DAT |
| CALPOST | CALPOST.LST |
| CALPOST | CALPOST.INP |
| ARCHIVOS COMPLEMENTARIOS | Dry Flux Data File |
| ARCHIVOS COMPLEMENTARIOS | Wet Flux Data |

<!-- Estadísticas: 11 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- **BORDOLI & Consultores EIRL** Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 32 Antofagasta -->
<!-- FIN TABLA 6 -->


Tabla 7: Ubicación y descripción de puntos receptores sensibles ............................................................................................ 37

<!-- INICIO TABLA 7 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- generados por las actividades de las distintas fases del proyecto NAVÍO II. Para identificar los receptores sensibles y definir la línea base de aire, se realizó una campaña de terreno el día 14 de Junio de 2015, identificándose 3 receptores, los cuales se presentan en la tabla 7. -->

**Tabla 7: Ubicación y descripción de puntos receptores sensibles****

| Punto | Descripción | Coordenadas UTM | Col4 |
| --- | --- | --- | --- |
| **Punto** | **Descripción** | **WGS 84 Huso 19S** | **WGS 84 Huso 19S** |
| **Punto** | **Descripción** | **Este** | **Norte** |
| R1 | Ciudad de Mejillones | 351.437 | 7.443.881 |
| R2 | Cruce Ruta B400 con Ruta 1 | 354.333 | 7.415.321 |
| R3 | Cerro Moreno | 353.572 | 7.407.780 |

<!-- Estadísticas: 5 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- **Figura 22: Emplazamiento de Puntos Receptores Sensibles** **BORDOLI & Consultores EIRL** Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 37 -->
<!-- FIN TABLA 7 -->


Tabla 8: Actividad Generadora de Emisiones - Fase de Construcción ..................................................................................... 39

<!-- INICIO TABLA 8 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- pesados y livianos y funcionamiento de grupos electrógenos. La siguiente tabla, presenta las características de las actividades del proyecto generadoras de emisiones atmosféricas, durante la fase de construcción. -->

**Tabla 8: Actividad Generadora de Emisiones - Fase de Construcción****

| Actividad Generadora de Emisiones - Fase de Construcción | Col2 | Col3 | Col4 | Tipo de<br>Contaminante |
| --- | --- | --- | --- | --- |
| **Actividad** | **Parámetros** | **Unidad** | **Duración**<br>**Actividad** | **Duración**<br>**Actividad** |
| **Escarpado área total del proyecto**<br>(preparación de terreno) | Área Total: 115.436 | m2 | 30 días | MP10 <br>MP2.5 <br>MPS |
| **Excavaciones** | Volumen: 1862 | m3 | 30 días | 30 días |
| **Excavaciones** | Densidad: 1,8 | ton/m3 | ton/m3 | ton/m3 |
| **Transferencia de Material** | **Transferencia de Material** | **Transferencia de Material** | **Transferencia de Material** | **Transferencia de Material** |
| Carga y descarga de material de<br>excavaciones | Volumen: 1862 | m3 | 30 días | 30 días |
| Carga y descarga de material de<br>excavaciones | Densidad: 1,8 | ton/m3 | ton/m3 | ton/m3 |
| Carga y descarga de material para<br>construcción de parapetos (canchas de<br>nitratos y polvorines)) | Volumen: 40.006 | m3 | 30 días | 30 días |
| Carga y descarga de material para<br>construcción de parapetos (canchas de<br>nitratos y polvorines)) | Densidad: 1,8 | ton/m3 | ton/m3 | ton/m3 |
| Carga y descarga de áridos | Volumen: 600 | m3 | 60 días | 60 días |
| Carga y descarga de áridos | Densidad: 1,6 | ton/m3 | ton/m3 | ton/m3 |
| Carga y Descarga material para llenos) | Volumen: 21.056 | m3 | 30 días | 30 días |
| Carga y Descarga material para llenos) | Densidad: 1,8 | ton/m3 | ton/m3 | ton/m3 |
| **Tránsito de Vehículos por Caminos Pavimentados** | **Tránsito de Vehículos por Caminos Pavimentados** | **Tránsito de Vehículos por Caminos Pavimentados** | **Tránsito de Vehículos por Caminos Pavimentados** | **Tránsito de Vehículos por Caminos Pavimentados** |
| Transporte Materiales de Construcción | Viajes totales: 180 | viajes | 180 días | 180 días |
| Transporte Materiales de Construcción | Longitud: 35 | km | km | km |
| Transporte otros Materiales de Construcción | Viajes totales: 180 | viajes | 180 días | MP10 <br>MP2.5 |
| Transporte otros Materiales de Construcción | Longitud: 35 | km | km | km |

<!-- Estadísticas: 18 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- **BORDOLI & Consultores EIRL** Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 39 Antofagasta -->
<!-- FIN TABLA 8 -->


Tabla 9: Maquinarias Utilizados en Fase de Construcción ....................................................................................................... 41

<!-- INICIO TABLA 9 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Informe de Emisiones Declaración de Impacto Ambiental Proyecto NAVÍO II -->

**Tabla 9: Maquinarias Utilizados en Fase de Construcción****

| Equipo | Cantidad | Potencia<br>Nominal KW | Operación<br>Diaria (horas) |
| --- | --- | --- | --- |
| Bulldozer CAT modelo D5K o similar | 1 | 72 | 15 |
| Cargador frontal CAT modelo 924HZ o similar | 1 | 106 | 30 |
| Retroexcavadora CAT modelo 416F o similar | 1 | 65 | 30 |
| Compactador CAT Modelo CB-434D o similar | 1 | 62 | 15 |
| Motoniveladora CAT modelo 120M2 AWD o similar | 1 | 108 | 15 |
| Excavadora CAT modelo 315C o similar | 1 | 82 | 30 |

<!-- Estadísticas: 6 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 10: Vehículos Utilizados en Fase de Construcción** |Actividad|Categoría<br>Vehículo|N°<br>Viajes/día|Trayecto<br>Pavimentado<br>(km)|Trayecto No<br>Pavimentado<br>(km)|Velocidad<br>Circulación<br>Pavimentado<br>(km/h)|Velocidad<br>Circulación No<br>Pavimentado<br>(km/h)| |---|---|---|---|---|---|---| -->
<!-- FIN TABLA 9 -->


Tabla 10: Vehículos Utilizados en Fase de Construcción ......................................................................................................... 41

<!-- INICIO TABLA 10 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Retroexcavadora CAT modelo 416F o similar|1|65|30| |Compactador CAT Modelo CB-434D o similar|1|62|15| |Motoniveladora CAT modelo 120M2 AWD o similar|1|108|15| |Excavadora CAT modelo 315C o similar|1|82|30| -->

**Tabla 10: Vehículos Utilizados en Fase de Construcción****

| Actividad | Categoría<br>Vehículo | N°<br>Viajes/día | Trayecto<br>Pavimentado<br>(km) | Trayecto No<br>Pavimentado<br>(km) | Velocidad<br>Circulación<br>Pavimentado<br>(km/h) | Velocidad<br>Circulación No<br>Pavimentado<br>(km/h) |
| --- | --- | --- | --- | --- | --- | --- |
| Transporte Materiales de<br>Construcción | Diésel Tipo 3 | 1 | 30 | 3,75 | 100 | 30 |
| Transporte Otros Materiales<br>de Construcción | Diésel Tipo 3 | 19 | 30 | 1 | 100 | 30 |
| Transporte Árido Para<br>Construcción | Diésel Tipo 3 | 1 | 30 | 3,75 | 100 | 30 |
| Transporte Hormigón | Diésel Tipo 3 | 1 | 30 | 3,75 | 100 | 30 |
| Transporte de Agua Industrial<br>Para Construcción y Riego | Diésel Tipo 3 | 1 | 30 | 3,75 | 100 | 30 |
| Transporte Material para<br>Relleno | Diésel Tipo 3 | 1 | 30 | 3,75 | 100 | 30 |
| Transporte H2O Servidas | Diésel Tipo 3 | 1 | 30 | 3,75 | 100 | 30 |
| Transporte Residuos | Diésel Tipo 3 | 1 | 30 | 3,75 | 100 | 30 |
| Transporte Personal<br>Construcción Planta | Buses<br>Particulares | 1 | 30 | 3,75 | 100 | 30 |
| Transporte Supervisión | Comerciales<br>Diésel Tipo 2 | 2 | 30 | 3,75 | 100 | 30 |

<!-- Estadísticas: 10 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 11: Generadores Utilizados en Fase de Construcción** |Equipo|Cantidad|Tipo de<br>Combustible|Potencia (KW)|Operación Diaria<br>(horas)| |---|---|---|---|---| -->
<!-- FIN TABLA 10 -->


Tabla 11: Generadores Utilizados en Fase de Construcción .................................................................................................... 41

<!-- INICIO TABLA 11 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Transporte H2O Servidas|Diésel Tipo 3|1|30|3,75|100|30| |Transporte Residuos|Diésel Tipo 3|1|30|3,75|100|30| |Transporte Personal<br>Construcción Planta|Buses<br>Particulares|1|30|3,75|100|30| |Transporte Supervisión|Comerciales<br>Diésel Tipo 2|2|30|3,75|100|30| -->

**Tabla 11: Generadores Utilizados en Fase de Construcción****

| Equipo | Cantidad | Tipo de<br>Combustible | Potencia (KW) | Operación Diaria<br>(horas) |
| --- | --- | --- | --- | --- |
| Generador | 2 | Diésel | 24 | 24 |

<!-- Estadísticas: 1 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- **6.1.2 Fase de Operación** En esta fase del proyecto, las emisiones de MPS, MP10, MP2.5 y gases de combustión, se generan como consecuencia de las actividades de circulación de vehículos por caminos pavimentados, circulación de vehículos -->
<!-- FIN TABLA 11 -->


Tabla 12: Actividad Generadora de Emisiones - Fase de Operación ....................................................................................... 42

<!-- INICIO TABLA 12 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Proyecto NAVÍO II La siguiente tabla, presenta las características de las actividades del proyecto generadoras de emisiones atmosféricas, durante la fase de operación. -->

**Tabla 12: Actividad Generadora de Emisiones - Fase de Operación****

| Actividad Generadora de Emisiones - Fase de Operación | Col2 | Col3 | Col4 | Tipo de<br>Contaminante |
| --- | --- | --- | --- | --- |
| **Actividad** | **Parámetros** | **Unidad** | **Duración**<br>**Actividad** | **Duración**<br>**Actividad** |
| **Tránsito de Vehículos por Caminos Pavimentados** | **Tránsito de Vehículos por Caminos Pavimentados** | **Tránsito de Vehículos por Caminos Pavimentados** | **Tránsito de Vehículos por Caminos Pavimentados** |  |
| Transporte de agua potable | Viajes totales: 1 | viajes | 365 días/año | MP10 <br>MP2.5<br>MPS |
| Transporte de agua potable | Longitud: 35 | km | km | km |
| Transporte de Agua Industrial | Viajes totales: 2 | viajes | 365 días/año | 365 días/año |
| Transporte de Agua Industrial | Longitud: 35 | km | km | km |
| Transporte de Combustible (Petróleo Diésel) | Viajes totales: 1 | viajes | 365 días/año | 365 días/año |
| Transporte de Combustible (Petróleo Diésel) | Longitud: 35 | km | km | km |
| Transporte Materiales Primas e Insumos | Viajes totales: 6 | viajes | 365 días/año | 365 días/año |
| Transporte Materiales Primas e Insumos | Longitud: 35 | km | km | km |
| Transporte de Productos | Viajes totales: 9 | viajes | 365 días/año | 365 días/año |
| Transporte de Productos | Longitud: 35 | km | km | km |
| Transporte de Residuos | Viajes totales: 4 | viajes | 365 días/año | 365 días/año |
| Transporte de Residuos | Longitud: 35 | km | km | km |
| Transporte de Personal | Viajes totales: 8 | viajes | 365 días/año | 365 días/año |
| Transporte de Personal | Longitud: 35 | km | km | km |
| **Tránsito de Vehículos Livianos por Caminos No Pavimentados** | **Tránsito de Vehículos Livianos por Caminos No Pavimentados** | **Tránsito de Vehículos Livianos por Caminos No Pavimentados** | **Tránsito de Vehículos Livianos por Caminos No Pavimentados** |  |
| Transporte de Personal | Viajes totales: 8 | viajes | 365 días/año | MP10 <br>MP2.5<br>MPS |
| Transporte de Personal | Longitud: 3,75 | km | km | km |
| **Tránsito de Vehículos Pesados por Caminos No Pavimentados** | **Tránsito de Vehículos Pesados por Caminos No Pavimentados** | **Tránsito de Vehículos Pesados por Caminos No Pavimentados** | **Tránsito de Vehículos Pesados por Caminos No Pavimentados** |  |
| Transporte de agua potable | Viajes totales: 1 | viajes | 365 días/año | MP10 <br>MP2.5<br>MPS |
| Transporte de agua potable | Longitud: 3,75 | km | km | km |
| Transporte de Agua Industrial | Viajes totales: 2 | viajes | 365 días/año | 365 días/año |
| Transporte de Agua Industrial | Longitud: 3,75 | km | km | km |
| Transporte de Combustible (Petróleo Diésel) | Viajes totales: 1 | viajes | 365 días/año | 365 días/año |
| Transporte de Combustible (Petróleo Diésel) | Longitud: 3,75 | km | km | km |
| Transporte Materiales Primas e Insumos | Viajes totales: 6 | viajes | 365 días/año | 365 días/año |
| Transporte Materiales Primas e Insumos | Longitud: 3,75 | km | km | km |
| Transporte de Productos | Viajes totales: 9 | viajes | 365 días/año | 365 días/año |
| Transporte de Productos | Longitud: 3,75 | km | km | km |
| Transporte Interno de Materias Primas | Viajes totales: 6 | viajes | 365 días/año | 365 días/año |
| Transporte Interno de Materias Primas | Longitud: 3,75 | km | km | km |
| Transporte de Residuos | Viajes totales: 4 | viajes | 365 días/año | 365 días/año |
| Transporte de Residuos | Longitud: 3,75 | km | km | km |
| **Emisiones de Gases** de Combustión de maquinarias y vehículos | **Emisiones de Gases** de Combustión de maquinarias y vehículos | **Emisiones de Gases** de Combustión de maquinarias y vehículos | **Emisiones de Gases** de Combustión de maquinarias y vehículos | CO, HC,<br>NOx, CC, y MP |
| **Emisiones de Gases** de Equipos Generadores | **Emisiones de Gases** de Equipos Generadores | **Emisiones de Gases** de Equipos Generadores | **Emisiones de Gases** de Equipos Generadores | CO, NOx, MP10, y<br>SOx |

<!-- Estadísticas: 36 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- **BORDOLI & Consultores EIRL** Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 42 Antofagasta -->
<!-- FIN TABLA 12 -->


Tabla 13: Equipos y/o Maquinarias Utilizados en Fase de Operación ...................................................................................... 43

<!-- INICIO TABLA 13 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Informe de Emisiones Declaración de Impacto Ambiental Proyecto NAVÍO II -->

**Tabla 13: Equipos y/o Maquinarias Utilizados en Fase de Operación****

| Actividad | Categoría<br>Vehículo | N°<br>Viajes/día | Trayecto<br>Pavimentado<br>(km) | Trayecto No<br>Pavimentado<br>(km) | Velocidad<br>Circulación<br>Pavimentado<br>(km/h) | Velocidad<br>Circulación No<br>Pavimentado<br>(km/h) |
| --- | --- | --- | --- | --- | --- | --- |
| Transporte de agua potable | Diésel Tipo 3 | 1 | 30 | 3,75 | 100 | 30 |
| Transporte de Agua Industrial | Diésel Tipo 3 | 2 | 30 | 3,75 | 100 | 30 |
| Transporte de Combustible<br>(Petróleo Diésel) | Diésel Tipo 3 | 1 | 30 | 3,75 | 100 | 30 |
| Transporte de Materias<br>primas | Diésel Tipo 3 | 6 | 30 | 3,75 | 100 | 30 |
| Transporte de Producto<br>(Emulsión) | Diésel Tipo 3 | 8 | 30 | 3,75 | 100 | 30 |
| Transporte de Producto<br>(Anfo) | Diésel Tipo 3 | 1 | 30 | 3,75 | 100 | 30 |
| Transporte de Residuos | Diésel Tipo 3 | 6 | 30 | 3,75 | 100 | 30 |
| Transporte Interno de<br>materias primas y productos | Diésel Tipo 3 | 4 | 30 | 3 | 100 | 30 |
| Transporte Personal de<br>Operaciones | Buses<br>Particulares | 2 | 30 | 3,75 | 100 | 30 |
| Transporte Supervisores | Comerciales<br>Diésel Tipo 2 | 6 | 30 | 3,75 | 100 | 30 |

<!-- Estadísticas: 10 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- **6.1.3 Fase de Cierre** En esta fase del proyecto, las emisiones de MPS, MP10, MP2.5 y gases de combustión, se generan como consecuencia de las actividades de nivelación del terreno, transferencia de material para la nivelación, -->
<!-- FIN TABLA 13 -->

Tabla 14: Vehículos Utilizados en Etapa de Operación ............................................................................................................ 43

Tabla 15: Actividad Generadora de Emisiones - Fase de Cierre .............................................................................................. 44

<!-- INICIO TABLA 15 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Informe de Emisiones Declaración de Impacto Ambiental Proyecto NAVÍO II -->

**Tabla 15: Actividad Generadora de Emisiones - Fase de Cierre****

| Actividad Generadora de Emisiones - Fase de Cierre | Col2 | Col3 | Col4 | Tipo de<br>Contaminante |
| --- | --- | --- | --- | --- |
| **Actividad** | **Parámetros** | **Unidad** | **Duración**<br>**Actividad** | **Duración**<br>**Actividad** |
| **Reperfilado del área** | Volumen: 20.000 | m3 | 30 días | MP10 <br>MP2.5<br>MPS |
| **Reperfilado del área** | Densidad: 1,8 | ton/m3 | ton/m3 | ton/m3 |
| **Tránsito de Vehículos por Caminos Pavimentados** | **Tránsito de Vehículos por Caminos Pavimentados** | **Tránsito de Vehículos por Caminos Pavimentados** | **Tránsito de Vehículos por Caminos Pavimentados** | **Tránsito de Vehículos por Caminos Pavimentados** |
| Transporte Material de Desarme | Viajes totales: 1 | viajes | 180 días | 180 días |
| Transporte Material de Desarme | Longitud: 35 | km | km | km |
| Transporte Residuos Varios | Viajes totales: 1 | viajes | 180 días | 180 días |
| Transporte Residuos Varios | Longitud: 35 | km | km | km |
| Transporte de Personal | Viajes totales: 3 | viajes | 180 días | 180 días |
| Transporte de Personal | Longitud: 35 | km | km | km |
| Transporte de Supervisión | Viajes totales: 1 | viajes | 180 días | 180 días |
| Transporte de Supervisión | Longitud: 35 | km | km | km |
| **Tránsito de Vehículos Livianos por Caminos No Pavimentados** | **Tránsito de Vehículos Livianos por Caminos No Pavimentados** | **Tránsito de Vehículos Livianos por Caminos No Pavimentados** | **Tránsito de Vehículos Livianos por Caminos No Pavimentados** | MP10 <br>MP2.5<br>MPS |
| Transporte de Personal | Viajes totales: 3 | viajes | 180 días | 180 días |
| Transporte de Personal | Longitud: 3,75 | km | km | km |
| Transporte de Supervisión | Viajes totales: 1 | viajes | 180 días | 180 días |
| Transporte de Supervisión | Longitud: 3,75 | km | km | km |
| **Tránsito de Vehículos Pesados por Caminos No Pavimentados** | **Tránsito de Vehículos Pesados por Caminos No Pavimentados** | **Tránsito de Vehículos Pesados por Caminos No Pavimentados** | **Tránsito de Vehículos Pesados por Caminos No Pavimentados** | **Tránsito de Vehículos Pesados por Caminos No Pavimentados** |
| Transporte Material de Desarme | Viajes totales: 1 | viajes | 180 días | 180 días |
| Transporte Material de Desarme | Longitud: 3,75 | km | km | km |
| Transporte Riego Caminos | Viajes totales: 3 | viajes | 180 días | 180 días |
| Transporte Riego Caminos | Longitud: 3,75 | km | km | km |
| Transporte de Materiales Excedentes | Viajes totales: 1 | viajes | 180 días | 180 días |
| Transporte de Materiales Excedentes | Longitud: 3,75 | km | km | km |
| Transporte de Residuos Varios | Viajes totales: 1 | viajes | 180 días | 180 días |
| Transporte de Residuos Varios | Longitud: 3,75 | km | km | km |
| **Emisiones de Gases** de Combustión de maquinarias y vehículos | **Emisiones de Gases** de Combustión de maquinarias y vehículos | **Emisiones de Gases** de Combustión de maquinarias y vehículos | **Emisiones de Gases** de Combustión de maquinarias y vehículos | CO, HC,<br>NOx, CC, y MP |
| **Emisiones de Gases** de Equipos Generadores<br> | **Emisiones de Gases** de Equipos Generadores<br> | **Emisiones de Gases** de Equipos Generadores<br> | **Emisiones de Gases** de Equipos Generadores<br> | CO, NOx, MP10, y<br>SOx |

<!-- Estadísticas: 28 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 16: Equipos y/o Maquinarias Utilizados en Fase de Cierre** |Equipo|Cantidad|Potencia<br>Nominal KW|Operación<br>Diaria (horas)| |---|---|---|---| -->
<!-- FIN TABLA 15 -->


Tabla 16: Equipos y/o Maquinarias Utilizados en Fase de Cierre ............................................................................................ 44

<!-- INICIO TABLA 16 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Transporte de Residuos Varios|Viajes totales: 1|viajes|180 días|180 días| |Transporte de Residuos Varios|Longitud: 3,75|km|km|km| |**Emisiones de Gases** de Combustión de maquinarias y vehículos|**Emisiones de Gases** de Combustión de maquinarias y vehículos|**Emisiones de Gases** de Combustión de maquinarias y vehículos|**Emisiones de Gases** de Combustión de maquinarias y vehículos|CO, HC,<br>NOx, CC, y MP| |**Emisiones de Gases** de Equipos Generadores<br>|**Emisiones de Gases** de Equipos Generadores<br>|**Emisiones de Gases** de Equipos Generadores<br>|**Emisiones de Gases** de Equipos Generadores<br>|CO, NOx, MP10, y<br>SOx| -->

**Tabla 16: Equipos y/o Maquinarias Utilizados en Fase de Cierre****

| Equipo | Cantidad | Potencia<br>Nominal KW | Operación<br>Diaria (horas) |
| --- | --- | --- | --- |
| Bulldozer CAT modelo D5K o similar | 1 | 72 | 15 |
| Cargador frontal CAT modelo 924HZ o similar | 1 | 106 | 30 |

<!-- Estadísticas: 2 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- **BORDOLI & Consultores EIRL** Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 44 Antofagasta -->
<!-- FIN TABLA 16 -->

Tabla 17: Vehículos Utilizados en Etapa de Cierre ................................................................................................................... 45

<!-- INICIO TABLA 17 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Informe de Emisiones Declaración de Impacto Ambiental Proyecto NAVÍO II -->

**Tabla 17: Vehículos Utilizados en Etapa de Cierre****

| Actividad | Categoría<br>Vehículo | N°<br>Viajes/día | Trayecto<br>Pavimentado<br>(km) | Trayecto No<br>Pavimentado<br>(km) | Velocidad<br>Circulación<br>Pavimentado<br>(km/h) | Velocidad<br>Circulación No<br>Pavimentado<br>(km/h) |
| --- | --- | --- | --- | --- | --- | --- |
| Transporte Material de<br>Desarme | Diésel Tipo 3 | 1 | 35 | 3,75 | 100 | 30 |
| Transporte Residuos Varios | Diésel Tipo 3 | 1 | 35 | 3,75 | 100 | 30 |
| Transporte Riego Caminos | Diésel Tipo 3 | 3 | 35 | 3,75 | 100 | 30 |
| Transporte Personal de<br>Cierre | Buses<br>Particulares | 1 | 35 | 3,75 | 100 | 30 |
| Transporte Supervisores | Comerciales<br>Diésel Tipo 2 | 3 | 35 | 3,75 | 100 | 30 |

<!-- Estadísticas: 5 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 18: Generadores Utilizados en Fase de Cierre** |Equipo|Cantidad|Tipo de<br>Combustible|Potencia (KW)|Operación Diaria<br>(horas)| |---|---|---|---|---| -->
<!-- FIN TABLA 17 -->


Tabla 18: Generadores Utilizados en Fase de Cierre ............................................................................................................... 45

<!-- INICIO TABLA 18 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Transporte Residuos Varios|Diésel Tipo 3|1|35|3,75|100|30| |Transporte Riego Caminos|Diésel Tipo 3|3|35|3,75|100|30| |Transporte Personal de<br>Cierre|Buses<br>Particulares|1|35|3,75|100|30| |Transporte Supervisores|Comerciales<br>Diésel Tipo 2|3|35|3,75|100|30| -->

**Tabla 18: Generadores Utilizados en Fase de Cierre****

| Equipo | Cantidad | Tipo de<br>Combustible | Potencia (KW) | Operación Diaria<br>(horas) |
| --- | --- | --- | --- | --- |
| Generador<br> | 1 | Diésel | 12 | 24 |

<!-- Estadísticas: 1 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- **6.2 Peso Promedio de la Flota** El peso promedio de la flota (PPF) se determinó de acuerdo a la proporción de peso de los vehículos considerados en la flota (PPV), proporción de viajes por tipo de vehículos considerados en la flota (VPV) y el -->
<!-- FIN TABLA 18 -->


Tabla 19: Peso Promedio de la Flota en Fase de Construcción ............................................................................................... 46

<!-- INICIO TABLA 19 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Proyecto NAVÍO II pavimentadas y no pavimentadas, y los pesos promedios de la flota. -->

**Tabla 19: Peso Promedio de la Flota en Fase de Construcción****

| Vehículos | Cantidad<br>de Viajes<br>Totales<br>(VTP) | Capacidad<br>de carga<br>(ton) | Peso<br>Vacío<br>(ton) | Peso<br>Cargado<br>(ton) | Peso<br>Promedio<br>(PMV) | Proporción<br>en Peso<br>(PPV) | Peso<br>Promedio<br>Flota<br>(PPF) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Transporte Materiales de<br>Construcción | 1 | 30 | 15 | 45 | 30 | 0,97 | **27,10** |
| Transporte de material para<br>relleno y construcción de<br>parapetos | 19 | 30 | 15 | 45 | 30 | 18,39 | 18,39 |
| Transporte Otros Materiales<br>de Construcción | 1 | 30 | 15 | 45 | 30 | 0,97 | 0,97 |
| Transporte Árido Para<br>Construcción | 1 <br> | 30 | 15 | 45 | 30 | 0,97 | 0,97 |
| Transporte Hormigón | 1 <br> | 30 | 15 | 45 | 30 | 0,97 | 0,97 |
| Transporte de H2O Potable | 1 | 30 | 15 | 45 | 30 | 0,97 | 0,97 |
| Transporte de Agua<br>Industrial Para<br>Construcción y Riego | 5 <br> | 15 | 7,5 | 22,5 | 15 | 2,42 | 2,42 |
| Transporte H2O Servidas | 1 <br> | 15 | 7,5 | 22,5 | 15 | 0,48 | 0,48 |
| Transporte Residuos | 1 | 30 | 15 | 45 | 30 | 0,97 | 0,97 |
| **TOTAL** | **31** |  |  |  |  |  |  |

<!-- Estadísticas: 10 filas, 8 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 20: Peso Promedio de la Flota en Fase de Operación** |Vehículos|Cantidad<br>de Viajes<br>Diarios<br>(VTP)|Capacidad<br>de carga<br>(ton)|Peso<br>Vacío<br>(ton)|Peso<br>Cargado<br>(ton)|Peso<br>Promedio<br>(PMV)|Proporción<br>en Peso<br>(PPV)|Peso<br>Promedio<br>Flota<br>(PPF)| |---|---|---|---|---|---|---|---| -->
<!-- FIN TABLA 19 -->


Tabla 20: Peso Promedio de la Flota en Fase de Operación ................................................................................................... 46

<!-- INICIO TABLA 20 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Transporte de Agua<br>Industrial Para<br>Construcción y Riego|5 <br>|15|7,5|22,5|15|2,42|2,42| |Transporte H2O Servidas|1 <br>|15|7,5|22,5|15|0,48|0,48| |Transporte Residuos|1|30|15|45|30|0,97|0,97| |**TOTAL**|**31**||||||| -->

**Tabla 20: Peso Promedio de la Flota en Fase de Operación****

| Vehículos | Cantidad<br>de Viajes<br>Diarios<br>(VTP) | Capacidad<br>de carga<br>(ton) | Peso<br>Vacío<br>(ton) | Peso<br>Cargado<br>(ton) | Peso<br>Promedio<br>(PMV) | Proporción<br>en Peso<br>(PPV) | Peso<br>Promedio<br>Flota<br>(PPF) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Transporte de agua potable | 1 | 15 | 7,5 | 22,5 | 15 | 0,52 | **25,34** |
| Transporte de Agua<br>Industrial | 2 | 15 | 7,5 | 22,5 | 15 | 1,03 | 1,03 |
| Transporte de Combustible<br>(Petróleo Diésel) | 1 | 30 | 15 | 45 | 30 | 1,03 | 1,03 |
| Transporte de Materias<br>primas | 6 | 30 | 15 | 45 | 30 | 6,21 | 6,21 |
| Transporte de Productos | 9 | 30 | 15 | 45 | 30 | 9,31 | 9,31 |
| Transporte de Residuos | 6 | 15 | 7,5 | 22,5 | 15 | 3,10 | 3,10 |
| Transporte Interno de<br>materias primas y<br>productos | 4 | 30 | 15 | 45 | 30 | 4,14 | 4,14 |
| **TOTAL** | **29** |  |  |  |  |  |  |

<!-- Estadísticas: 8 filas, 8 columnas -->
<!-- Contexto posterior: -->
<!-- **BORDOLI & Consultores EIRL** Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 46 Antofagasta -->
<!-- FIN TABLA 20 -->


Tabla 21: Peso Promedio de la Flota en Fase de Cierre .......................................................................................................... 47

<!-- INICIO TABLA 21 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Informe de Emisiones Declaración de Impacto Ambiental Proyecto NAVÍO II -->

**Tabla 21: Peso Promedio de la Flota en Fase de Cierre****

| Vehículos | Cantidad<br>de Viajes<br>Diarios<br>(VTP) | Capacidad<br>de carga<br>(ton) | Peso<br>Vacío<br>(ton) | Peso<br>Cargado<br>(ton) | Peso<br>Promedio<br>(PMV) | Proporción<br>en Peso<br>(PPV) | Peso<br>Promedio<br>Flota<br>(PPF) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Transporte Material de<br>Desarme | 1 | 30 | 15 | 45 | 30 | 6 | 18 |
| Transporte Residuos Varios | 1 | 15 | 7.5 | 22,5 | 15 | 3 | 3 |
| Transporte Riego Caminos | 3 | 15 | 7.5 | 22,5 | 15 | 9 | 9 |
| **TOTAL** | **5 ** |  |  |  |  |  |  |

<!-- Estadísticas: 4 filas, 8 columnas -->
<!-- Contexto posterior: -->
<!-- **6.3 Metodología Para La Estimación De Emisiones** La ecuación general para estimar las emisiones de cualquier actividad, es la siguiente: -->
<!-- FIN TABLA 21 -->


Tabla 22: Factor de Emisión Escarpes ..................................................................................................................................... 50

<!-- INICIO TABLA 22 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **7.1 Factores De Emisión Para Material Particulado Resuspendido** Las expresiones de factores de emisión para la estimación de emisiones de material particulado resuspendido, se presentan a continuación [14] . -->

**Tabla 22: Factor de Emisión Escarpes****

| Factor de Emisión (fe) | fe = k*0,570 |
| --- | --- |
| Unidades | kg/km |
| Parámetros | No utiliza parámetros<br>K: Factor según tamaño de partícula<br> PM10 = 0,75<br> PM2.5 = 0,105<br> MPS = 1 |
| Fuente | Compilation of Air Pollutant Emission Factors, AP 42, 5th Edition: Chapter 13, Section<br>13.2.3“Heavy Construction Operations, 2010” |
| Descripción | Corresponde al factor de emisión de preparación de terrenos (movimiento de tierra) y retiro<br>de cobertura vegetal. La unidad de este factor corresponde a kilógramos emitidos por<br>kilómetro recorrido en el proceso de escarpado de la cobertura vegetal. |
| Nivel de actividad | El nivel de actividad se determina según la distancia que recorre el cargador frontal por el<br>área a escapar. Por defecto para 1 hectárea se recorre una distancia de 3,57 km |

<!-- Estadísticas: 5 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- 14 Fuente de Información: Guía para la estimación de emisiones atmosféricas de proyectos inmobiliarios para la Región Metropolitana del Ministerio del Medio Ambiente, [enero 2012]. -->
<!-- FIN TABLA 22 -->


Tabla 23: Factor de Emisión Excavaciones .............................................................................................................................. 51

<!-- INICIO TABLA 23 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Proyecto NAVÍO II Mitigación No aplican medidas de mitigación -->

**Tabla 23: Factor de Emisión Excavaciones****

| Factor de Emisión (fe) | fe = 0.45*k*(s^1.5/M^1.4) [Para PM10 y PM2.5]<br>fe = 2.6*s^1.2/M^1.3 [Para MPS] |
| --- | --- |
| Unidades | kg/h |
| Parámetros | K: Factor según tamaño de partícula<br> PM10 = 0.75<br> PM2.5 = 0,105<br> MPS = 2.6<br>s: % de finos del suelo [8,5 valor por defecto]<br>M: % humedad material [6,5 valor por defecto] |
| Fuente | Compilation of Air Pollutant Emission Factors, AP 42, 5th Edition: Chapter 11, Section 11.9<br>“Western Surface Coal Mining, 1998”, Table 11.9-2. |
| Descripción | Corresponde al factor de emisión de despeje de material (bulldozing / overburden)<br>escalado por 0,75 para ser aplicado a MP10. La unidad de este factor corresponde a<br>kilógramos emitidos por hora excavada |
| Nota | El nivel de actividad se determina a través del rendimiento de la maquinaria y el volumen a<br>escavar. Por defecto se considerará para una retroexcavadora con capacidad de palada<br>de 1 m3 un rendimiento igual a 30 m3/hr. |
| Mitigación | No aplican medidas de mitigación. |

<!-- Estadísticas: 6 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 24: Factor de Emisión Transferencia de Material (Carguío y Volteo de Camiones)** |Factor de Emisión (fe)|fe = 0.0016*k*(U/2.2)^1.3/(M/2)^1.4| |---|---| -->
<!-- FIN TABLA 23 -->


Tabla 24: Factor de Emisión Transferencia de Material (Carguío y Volteo de Camiones) ....................................................... 51

<!-- INICIO TABLA 24 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Fuente|Compilation of Air Pollutant Emission Factors, AP 42, 5th Edition: Chapter 11, Section 11.9<br>“Western Surface Coal Mining, 1998”, Table 11.9-2.| |Descripción|Corresponde al factor de emisión de despeje de material (bulldozing / overburden)<br>escalado por 0,75 para ser aplicado a MP10. La unidad de este factor corresponde a<br>kilógramos emitidos por hora excavada| |Nota|El nivel de actividad se determina a través del rendimiento de la maquinaria y el volumen a<br>escavar. Por defecto se considerará para una retroexcavadora con capacidad de palada<br>de 1 m3 un rendimiento igual a 30 m3/hr.| |Mitigación|No aplican medidas de mitigación.| -->

**Tabla 24: Factor de Emisión Transferencia de Material (Carguío y Volteo de Camiones)****

| Factor de Emisión (fe) | fe = 0.0016*k*(U/2.2)^1.3/(M/2)^1.4 |
| --- | --- |
| Unidades | kg/ton |
| Parámetros | K: Factor según tamaño de partícula<br> PM10 = 0,35<br> PM2.5 = 0,053<br> MPS = 0.74<br>U: Velocidad del viento (m/s) [5 m/s valor por defecto]<br>M: Humedad del material [6,5 valor por defecto] |
| Fuente | Compilation of Air Pollutant Emission Factors, AP 42: Chapter 13, Section 13.2.4<br>“Aggregate Handling and Storage Piles, 2006”. |
| Descripción | Corresponde al factor de emisión de transferencia discreta de material utilizado<br>directamente. La unidad de este factor corresponde a kilogramos emitidos por cada<br>tonelada de material cargado o descargado. |
| Mitigación<br> | No aplican medidas de mitigación. |

<!-- Estadísticas: 5 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 25: Factores de Emisión Resuspensión de MP por Circulación de Vehículos en Caminos Pavimentados** |Factor de Emisión (fe)|fe = k*(sL)^0.91*W^1.02| |---|---| -->
<!-- FIN TABLA 24 -->


Tabla 25: Factores de Emisión Resuspensión de MP por Circulación de Vehículos en Caminos Pavimentados ................... 51

<!-- INICIO TABLA 25 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Parámetros|K: Factor según tamaño de partícula<br> PM10 = 0,35<br> PM2.5 = 0,053<br> MPS = 0.74<br>U: Velocidad del viento (m/s) [5 m/s valor por defecto]<br>M: Humedad del material [6,5 valor por defecto]| |Fuente|Compilation of Air Pollutant Emission Factors, AP 42: Chapter 13, Section 13.2.4<br>“Aggregate Handling and Storage Piles, 2006”.| |Descripción|Corresponde al factor de emisión de transferencia discreta de material utilizado<br>directamente. La unidad de este factor corresponde a kilogramos emitidos por cada<br>tonelada de material cargado o descargado.| |Mitigación<br>|No aplican medidas de mitigación.| -->

**Tabla 25: Factores de Emisión Resuspensión de MP por Circulación de Vehículos en Caminos Pavimentados****

| Factor de Emisión (fe) | fe = k*(sL)^0.91*W^1.02 |
| --- | --- |
| Unidades | gr/ton |

<!-- Estadísticas: 1 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- **BORDOLI & Consultores EIRL** Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 51 Antofagasta -->
<!-- FIN TABLA 25 -->


**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 3
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

Tabla 26: Factor de Emisión Resuspensión de MP10 Circulación de Vehículos Livianos en Caminos No Pavimentados ...... 52

<!-- INICIO TABLA 26 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |---|---| |Fuente|Compilation of Air Pollutant Emission Factors, AP-42: Chapter 13, Section 13.2.1 “Paved<br>Roads, 2011”.| |Descripción|Corresponde al factor de emisión de material particulado resuspendido por tránsito de<br>vehículos por caminos pavimentados. La unidad de este factor de emisión es gramos de<br>MP10 emitidos por kilómetro recorrido.| |Mitigación<br>|No aplican medidas de mitigación.| -->

**Tabla 26: Factor de Emisión Resuspensión de MP10 Circulación de Vehículos Livianos en Caminos No****

| Factor de Emisión (fe) | fe = 281.9*k*(s/12)*(S/30)^0.5/(M/0.5)^0.2 |
| --- | --- |
| Unidades | g/km |
| Parámetros | K: Factor según tamaño de partícula<br> PM10 = 1.5<br> PM2.5 = 0,15<br> MPS = 4.9<br>s: % de finos del suelo [8,5 valor por defecto]<br>S: Velocidad de los vehículos en km/h<br>M: % humedad material. [6,5 valor por defecto] |
| Fuente | Compilation of Air Pollutant Emission Factors, AP 42: Chapter 13, Section 13.2.2<br>“Unpaved Roads, 2006”. |
| Descripción | Corresponde al factor de emisión de tránsito por caminos no pavimentados determinado<br>para caminos de acceso público. La unidad de este factor de emisión es gramos de MP10<br>emitidos por kilómetro recorrido |
| Nota | Dadas las características de la flota utilizada en la determinación de este factor de<br>emisión, su aplicación se reconoce válida para una flota de vehículos pesados, es decir,<br>cuyo peso promedio exceda las 2,7 toneladas métricas.<br>Contenido de % de finos del suelo - valor por defecto 8,5%<br>Contenido de humedad del suelo - valor por defecto 6,5% |
| Mitigación | Como medida de abatimiento se considera el regadío diario (4 riegos diarios) del camino<br>que une el km 2.3 del bay-pass con la obra (1850 m) |

<!-- Estadísticas: 6 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 27: Factor de Emisión Resuspensión de MP10 Circulación de Vehículos Pesados en Caminos No** **Pavimentados** |Factor de Emisión (fe)|fe = 281.9*k*(s/12)^0.9*(W/3)^0.45 [Para MP10 y MP2.5]<br>Fe = 281,9*4.9*(s/12) ^0,7*(W/3) ^0,45 [Para MPS]| -->
<!-- FIN TABLA 26 -->


Tabla 27: Factor de Emisión Resuspensión de MP10 Circulación de Vehículos Pesados en Caminos No Pavimentados ..... 52

<!-- INICIO TABLA 27 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Fuente|Compilation of Air Pollutant Emission Factors, AP 42: Chapter 13, Section 13.2.2<br>“Unpaved Roads, 2006”.| |Descripción|Corresponde al factor de emisión de tránsito por caminos no pavimentados determinado<br>para caminos de acceso público. La unidad de este factor de emisión es gramos de MP10<br>emitidos por kilómetro recorrido| |Nota|Dadas las características de la flota utilizada en la determinación de este factor de<br>emisión, su aplicación se reconoce válida para una flota de vehículos pesados, es decir,<br>cuyo peso promedio exceda las 2,7 toneladas métricas.<br>Contenido de % de finos del suelo - valor por defecto 8,5%<br>Contenido de humedad del suelo - valor por defecto 6,5%| |Mitigación|Como medida de abatimiento se considera el regadío diario (4 riegos diarios) del camino<br>que une el km 2.3 del bay-pass con la obra (1850 m)| -->

**Tabla 27: Factor de Emisión Resuspensión de MP10 Circulación de Vehículos Pesados en Caminos No****

| Factor de Emisión (fe) | fe = 281.9*k*(s/12)^0.9*(W/3)^0.45 [Para MP10 y MP2.5]<br>Fe = 281,9*4.9*(s/12) ^0,7*(W/3) ^0,45 [Para MPS] |
| --- | --- |
| Unidades | g/km |
| Parámetros | K: Factor según tamaño de partícula<br> PM10 = 1.5<br> PM2.5 = 0,15 |

<!-- Estadísticas: 2 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- **BORDOLI & Consultores EIRL** Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 52 Antofagasta -->
<!-- FIN TABLA 27 -->


Tabla 28: Factores de Emisión de Gases y MP de Maquinarias .............................................................................................. 53

<!-- INICIO TABLA 28 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Los factores de emisión de gases y material particulado de combustión, asociados a la operación de la maquinaria, vehículos, generadores y calderas, durante las distintas fases del proyecto, se presentan en las tablas siguientes: -->

**Tabla 28: Factores de Emisión de Gases y MP de Maquinarias****

| Factor de Emisión (fe) | E= (FP × t × C × P) |
| --- | --- |
| Unidades | gr/día |
| Parámetros | FP: factor según potencia<br>t: tiempo de operación diaria (h)<br>C: Porcentaje de carga<br>P: Potencia Nominal (kw) |
| Fuente | Guía para la Estimación de Emisiones Atmosféricas de Proyectos Inmobiliarios para la<br>Región Metropolitana, Tabla 4.9 |
| Descripción | Corresponde al factor de emisión de combustión de los motores de la maquinaria fuera de<br>ruta. |
| Mitigación | No aplican medidas de mitigación. |

<!-- Estadísticas: 5 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 29: Factor de Emisión en Función de la Potencia (g/kW-h)** |Contaminante|0-20|20-37|37-75|75-130|>130| |---|---|---|---|---|---| -->
<!-- FIN TABLA 28 -->


Tabla 29: Factor de Emisión en Función de la Potencia (g/kW-h) ............................................................................................ 53

<!-- INICIO TABLA 29 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Parámetros|FP: factor según potencia<br>t: tiempo de operación diaria (h)<br>C: Porcentaje de carga<br>P: Potencia Nominal (kw)| |Fuente|Guía para la Estimación de Emisiones Atmosféricas de Proyectos Inmobiliarios para la<br>Región Metropolitana, Tabla 4.9| |Descripción|Corresponde al factor de emisión de combustión de los motores de la maquinaria fuera de<br>ruta.| |Mitigación|No aplican medidas de mitigación.| -->

**Tabla 29: Factor de Emisión en Función de la Potencia (g/kW-h)****

| Contaminante | 0-20 | 20-37 | 37-75 | 75-130 | >130 |
| --- | --- | --- | --- | --- | --- |
| CO | 8.38 | 6.43 | 5.06 | 3.76 | 3.00 |
| HC | 3.87 | 2.96 | 2.33 | 1.72 | 1.35 |
| NOx | 14.36 | 14.36 | 14.36 | 14.36 | 14.36 |
| MP | 2.22 | 1.81 | 1.51 | 1.23 | 1.10 |

<!-- Estadísticas: 4 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- **BORDOLI & Consultores EIRL** Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 53 Antofagasta -->
<!-- FIN TABLA 29 -->


Tabla 30: Factor de Emisión Para Gases y MP de Vehículos .................................................................................................. 54

<!-- INICIO TABLA 30 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Informe de Emisiones Declaración de Impacto Ambiental Proyecto NAVÍO II -->

**Tabla 30: Factor de Emisión Para Gases y MP de Vehículos****

| Categoría | Contaminante | Factor Emisión [g/km] |
| --- | --- | --- |
| Camiones Pesados<br>Diésel Tipo 3 | CO | (1,24588358438859+(103,700537481749/(1+exp((((-1)*-<br>1,3906312471446)+(0,543451750078654*ln(V)))+(0,0390066425998189*V)))<br>)) |
| Camiones Pesados<br>Diésel Tipo 3 | HC | ((0,135938586321894+(0,71588074810547*exp(((-<br>1)*0,0234666513590177)*V)))+(2,79878282504916*exp(((-<br>1)*0,123459782380517)*V))) |
| Camiones Pesados<br>Diésel Tipo 3 | NOx | ((5,58300975720938+(14,5724996214701*exp(((-<br>1)*0,0510403515051286)*V)))+(45,651882800859*exp(((-<br>1)*0,309240087785118)*V))) |
| Camiones Pesados<br>Diésel Tipo 3 | CC | ((199,101296810716+(496,037924788222*exp(((-<br>1)*0,0466183266185801)*V)))+(3798,31076366067*exp(((-<br>1)*0,573715458508514)*V))) |
| Camiones Pesados<br>Diésel Tipo 3 | MP | ((0,100820480611018+(0,424449762706025*exp(((-<br>1)*0,0416436785215947)*V)))+(0,864328026775096*exp(((-<br>1)*0,159945936589218)*V))) |
| Camiones Medianos<br>Diésel Tipo 3 | CO | ((0,731687393919072+(3,6645785309034*exp(((-<br>1)*0,0563683393170761)*V)))+(5,23028829144801*exp(((-<br>1)*0,22940672493427)*V))) |
| Camiones Medianos<br>Diésel Tipo 3 | HC | (0,0837360334457316+(1,32104434472513/(1+exp((((-<br>1)*4,53135180004797)+(1,89348725872261*ln(V)))+(-<br>0,0103853145584935*V))))) |
| Camiones Medianos<br>Diésel Tipo 3 | NOx | ((3,75961273247849+(8,83991867276675*exp(((-<br>1)*0,0582095437791065)*V)))+(32,8119093290992*exp(((-<br>1)*0,324655578422129)*V))) |
| Camiones Medianos<br>Diésel Tipo 3 | CC | (1/(((-1,25110663618204E-<br>06*(V2))+(0,000164240816414678*V))+0,00147486189135326)) |
| Camiones Medianos<br>Diésel Tipo 3 | MP | (0,00753000339418102+(0,481778214802105/(1+exp((((-<br>1)*4,57741464608742)+(1,88064486426566*ln(V)))+(-<br>0,0224165794949045*V))))) |
| Vehículos Comerciales<br>Diésel Tipo 2<br> | CO | 0,82*(0,000223*V^2-0,026*k18+1,076) |
| Vehículos Comerciales<br>Diésel Tipo 2<br> | HC | 0,62*(0.0000175*V 2-0,00284*V+0,2162) |
| Vehículos Comerciales<br>Diésel Tipo 2<br> | NOx | 0,84*(0.000241*V 2-0,03181*V+2,0247) |
| Vehículos Comerciales<br>Diésel Tipo 2<br> | CC | 0,0198*V 2-2,506*V+137,42 |
| Vehículos Comerciales<br>Diésel Tipo 2<br> | MP | 0,67*(0.000045*V 2-0,004885*V+0,1932) |

<!-- Estadísticas: 15 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 31: Factor de Emisión por Combustión en Grupos Generadores** |Factores De Emisión para Grupos Generadores (Factor de Emisión (kg/kw-h)|Col2|Col3|Col4|Col5|Col6|Col7| |---|---|---|---|---|---|---| -->
<!-- FIN TABLA 30 -->

Tabla 31: Factor de Emisión por Combustión en Grupos Generadores ................................................................................... 54

<!-- INICIO TABLA 31 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Vehículos Comerciales<br>Diésel Tipo 2<br>|HC|0,62*(0.0000175*V 2-0,00284*V+0,2162)| |Vehículos Comerciales<br>Diésel Tipo 2<br>|NOx|0,84*(0.000241*V 2-0,03181*V+2,0247)| |Vehículos Comerciales<br>Diésel Tipo 2<br>|CC|0,0198*V 2-2,506*V+137,42| |Vehículos Comerciales<br>Diésel Tipo 2<br>|MP|0,67*(0.000045*V 2-0,004885*V+0,1932)| -->

**Tabla 31: Factor de Emisión por Combustión en Grupos Generadores****

| Factores De Emisión para Grupos Generadores (Factor de Emisión (kg/kw-h) | Col2 | Col3 | Col4 | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Contaminante** | **MP** | **MP10** | **MP2.5** | **CO** | **NOx** | **SOx** |
| Petróleo Diésel (hasta 600 hp) | 0.00134 | 0.00134 | 0.00134 | 0.00406 | 0.0188 | 0.00125 |

<!-- Estadísticas: 2 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- **BORDOLI & Consultores EIRL** Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 54 Antofagasta -->
<!-- FIN TABLA 31 -->


Tabla 32: Factor de Emisión para Calderas a GLP .................................................................................................................. 55

<!-- INICIO TABLA 32 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Informe de Emisiones Declaración de Impacto Ambiental Proyecto NAVÍO II -->

**Tabla 32: Factor de Emisión para Calderas a GLP****

| Factores De Emisión para Calderas Diésel (Factor de Emisión (kg/kg petróleo diésel) | Col2 | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Contaminante** | **MP** | **MP10** | **MP2.5** | **CO** | **NOx** | **VOC** | **SOx** |
| Diésel | 0,00028 | 0,00028 | 0,00014 | 0,00004 | 0,00071 | 0,00283 | 0,0001 |

<!-- Estadísticas: 2 filas, 8 columnas -->
<!-- Contexto posterior: -->
<!-- **8.** **NIVELES DE ACTIVIDAD** El nivel de actividad (Na) utilizado para calcular las emisiones de cada actividad, en cada una de las fases del proyecto, se presenta en las tablas siguientes: -->
<!-- FIN TABLA 32 -->


Tabla 33: Nivel de Actividad Etapa de Construcción ................................................................................................................ 55

<!-- INICIO TABLA 33 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **8.** **NIVELES DE ACTIVIDAD** El nivel de actividad (Na) utilizado para calcular las emisiones de cada actividad, en cada una de las fases del proyecto, se presenta en las tablas siguientes: -->

**Tabla 33: Nivel de Actividad Etapa de Construcción****

| Actividad Generadora de Emisiones - Fase de Construcción | Nivel de Actividad (Na | Col3 |
| --- | --- | --- |
| **Actividad** | **Cantidad** | **Unidad** |
| **Escarpado Área total del Proyecto**(preparación de terreno) | 1,37 | km/día |
| **Excavaciones** | 2,07 | h/día |
| **Transferencia de Material** | **Transferencia de Material** | **Transferencia de Material** |
| Carga y descarga de material de excavaciones | 111,69 | ton/día |
| Carga y descarga de material para construcción de parapetos (canchas de<br>nitratos y polvorines) | 2400,36 | 2400,36 |
| Carga y descarga de áridos | 16,00 | 16,00 |
| Carga y Descarga material para rellenos | 1263,36 | 1263,36 |
| **Tránsito de Vehículos por Caminos Pavimentados** | **Tránsito de Vehículos por Caminos Pavimentados** | **Tránsito de Vehículos por Caminos Pavimentados** |
| Transporte Materiales de Construcción | 52,76 | km/día |
| Transporte Otros Materiales de Construcción | 45,69 | 45,69 |
| Transporte Árido Para Construcción | 37,33 | 37,33 |
| Transporte Hormigón | 37,33 | 37,33 |
| Transporte de H2O Potable | 37,33 | 37,33 |
| Transporte de Agua Industrial Para Construcción y Riego | 70,00 | 70,00 |
| Transporte H2O Servidas | 70,00 | 70,00 |
| Transporte Residuos | 38,89 | 38,89 |
| Transporte Personal Construcción Planta | 140,00 | 140,00 |
| Transporte Supervisión | 280,00 | 280,00 |
| **Tránsito de Vehículos Livianos por Caminos No Pavimentados**(duración actividad: días) | **Tránsito de Vehículos Livianos por Caminos No Pavimentados**(duración actividad: días) | **Tránsito de Vehículos Livianos por Caminos No Pavimentados**(duración actividad: días) |
| Transporte Personal Construcción Planta | 15,00 | km/día |
| Transporte Supervisión | 30,00 | 30,00 |
| **Tránsito de Vehículos Pesados por Caminos No Pavimentados**(duración actividad: días) | **Tránsito de Vehículos Pesados por Caminos No Pavimentados**(duración actividad: días) | **Tránsito de Vehículos Pesados por Caminos No Pavimentados**(duración actividad: días) |
| Transporte Materiales de Construcción | 5,65 | km/día |
| Transporte de material para relleno y construcción de parapetos | 37,01 | 37,01 |
| Transporte Otros Materiales de Construcción | 4,90 | 4,90 |
| Transporte Árido Para Construcción | 4,00 | 4,00 |
| Transporte Hormigón | 4,00 | 4,00 |
| Transporte de Agua Industrial Para Construcción y Riego | 4,00 | 4,00 |
| Transporte H2O Servidas | 7,50 | 7,50 |
| Transporte Material para Relleno | 10,80 | 10,80 |
| Transporte Residuos<br> | 4,17 | 4,17 |

<!-- Estadísticas: 32 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- **BORDOLI & Consultores EIRL** Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 55 Antofagasta -->
<!-- FIN TABLA 33 -->


Tabla 34: Nivel de Actividad Etapa de Operación ..................................................................................................................... 56

<!-- INICIO TABLA 34 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Informe de Emisiones Declaración de Impacto Ambiental Proyecto NAVÍO II -->

**Tabla 34: Nivel de Actividad Etapa de Operación****

| Actividad Generadora de Emisiones - Fase de Operación | Nivel de Actividad (Na | Col3 |
| --- | --- | --- |
| **Actividad** | **Cantidad** | **Unidad** |
| **Tránsito de Vehículos por Caminos Pavimentados** | **Tránsito de Vehículos por Caminos Pavimentados** | **Tránsito de Vehículos por Caminos Pavimentados** |
| Transporte de agua potable | 38,50 | km/día |
| Transporte de Agua Industrial | 140,00 | 140,00 |
| Transporte de Combustible (Petróleo Diésel) | 42,47 | 42,47 |
| Transporte de Materias Primas | 447,38 | 447,38 |
| Transporte de Productos (Emulsión) | 544,44 | 544,44 |
| Transporte de Producto (Anfo) | 70,00 | 70,00 |
| Transporte de Residuos | 259,00 | 259,00 |
| Transporte Personal de Operaciones | 140,00 | 140,00 |
| Transporte Supervisores | 420,00 | 420,00 |
| **Tránsito de Vehículos Livianos por Caminos No Pavimentados** | **Tránsito de Vehículos Livianos por Caminos No Pavimentados** | **Tránsito de Vehículos Livianos por Caminos No Pavimentados** |
| Transporte Personal de Operaciones | 15,00 | km/día |
| Transporte Supervisores | 45,00 | 45,00 |
| **Tránsito de Vehículos Pesados por Caminos No Pavimentados** | **Tránsito de Vehículos Pesados por Caminos No Pavimentados** | **Tránsito de Vehículos Pesados por Caminos No Pavimentados** |
| Transporte de agua potable | 4,13 | km/día |
| Transporte de Agua Industrial | 15,00 | 15,00 |
| Transporte de Combustible (Petróleo Diésel) | 4,55 | 4,55 |
| Transporte de Materias Primas | 47,93 | 47,93 |
| Transporte de Producto (Emulsión) | 58,33 | 58,33 |
| Transporte de Producto (Anfo) | 7,50 | 7,50 |
| Transporte Interno de materias primas y productos | 47,93 | 47,93 |
| Transporte de Residuos<br> | 27,75 | 27,75 |

<!-- Estadísticas: 23 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 35: Nivel de Actividad Etapa de Cierre** |Actividad Generadora de Emisiones - Fase de Cierre|Nivel de Actividad (Na|Col3| |---|---|---| -->
<!-- FIN TABLA 34 -->


Tabla 35: Nivel de Actividad Etapa de Cierre ........................................................................................................................... 56

<!-- INICIO TABLA 35 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Transporte de Producto (Emulsión)|58,33|58,33| |Transporte de Producto (Anfo)|7,50|7,50| |Transporte Interno de materias primas y productos|47,93|47,93| |Transporte de Residuos<br>|27,75|27,75| -->

**Tabla 35: Nivel de Actividad Etapa de Cierre****

| Actividad Generadora de Emisiones - Fase de Cierre | Nivel de Actividad (Na | Col3 |
| --- | --- | --- |
| **Actividad** | **Cantidad** | **Unidad** |
| **Reperfilamiento área del proyecto** | 0,24 | h/día |
| **Tránsito de Vehículos por Caminos Pavimentados** | **Tránsito de Vehículos por Caminos Pavimentados** | **Tránsito de Vehículos por Caminos Pavimentados** |
| Transporte Material de Desarme | 55,03 | km/día |
| Transporte Residuos Varios | 70,00 |  |
| Transporte Riego Caminos | 22,50 |  |
| Transporte de Personal | 70,00 |  |
| Transporte de Supervisión | 210,00 |  |
| **Tránsito de Vehículos Livianos por Caminos No Pavimentados** | **Tránsito de Vehículos Livianos por Caminos No Pavimentados** | **Tránsito de Vehículos Livianos por Caminos No Pavimentados** |
| Transporte Personal de Cierre | 7,50 | km/día |
| Transporte Supervisión de Cierre | 22,50 | 22,50 |
| **Tránsito de Vehículos Pesados por Caminos No Pavimentados**(viajes/día) | **Tránsito de Vehículos Pesados por Caminos No Pavimentados**(viajes/día) | **Tránsito de Vehículos Pesados por Caminos No Pavimentados**(viajes/día) |
| Transporte Material de Desarme | 5,90 | km/día |
| Transporte Riego Caminos | 22,50 | 22,50 |
| Transporte Residuos Varios<br> | 5,90 | 5,90 |

<!-- Estadísticas: 15 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- **BORDOLI & Consultores EIRL** Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 56 Antofagasta -->
<!-- FIN TABLA 35 -->


Tabla 36: Factores de Emisión (MP10, MP2.5 y MPS) - Actividades Fase de Construcción ................................................... 59

<!-- INICIO TABLA 36 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **10.** **RESULTADOS INVENTARIO DE EMISIONES** Las tablas siguientes muestran los resultados del inventario de emisiones. -->

**Tabla 36: Factores de Emisión (MP10, MP2.5 y MPS) - Actividades Fase de Construcción****

| ACTIVIDAD | Actividad Específica | Parámetros para<br>Factores de Emisión | Col4 | Col5 | Factor de<br>emisión<br>PM10 | Factor de<br>emisión<br>PM2.5 | Factor<br>emisión<br>MPS |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **ACTIVIDAD** | **Actividad Específica** | **k10 ** | **k2,5 ** | **kMPS ** | **kMPS ** | **kMPS ** | **kMPS ** |
| Escarpe | Escarpe Área Total | 0,75 | 0,105 | 1 | 4,2750 | 0,5985 | 5,7000 |
| Excavaciones | Excavación totales | 0,75 | 0,105 | 2,6 | 0,6086 | 0,0852 | 2,9750 |
| Carguío y Volteo de<br>Camiones | Carga y descarga de material<br>de excavaciones | 0,35 | 0,053 | 0,74 | 0,0003 | 0,0000 | 0,0007 |
| Carguío y Volteo de<br>Camiones | Carga y descarga de material<br>para construcción de<br>parapetos (canchas de<br>nitratos y polvorines) | 0,35 | 0,053 | 0,74 | 0,0003 | 0,0000 | 0,0007 |
| Carguío y Volteo de<br>Camiones | Carga y descarga de áridos | 0,35 | 0,053 | 0,74 | 0,0003 | 0,0000 | 0,0007 |
| Carguío y Volteo de<br>Camiones | Carga y Descarga material<br>para rellenos | 0,35 | 0,053 | 0,74 | 0,0003 | 0,0000 | 0,0007 |
| Tránsito de Vehículos<br>por Caminos<br>Pavimentados | Transporte Materiales de<br>Construcción | 0,62 | 0,15 | 3,23 | 0,0130 | 0,0031 | 0,0676 |
| Tránsito de Vehículos<br>por Caminos<br>Pavimentados | Transporte Otros Materiales<br>de Construcción | 0,62 | 0,15 | 3,23 | 0,0130 | 0,0031 | 0,0676 |
| Tránsito de Vehículos<br>por Caminos<br>Pavimentados | Transporte Árido Para<br>Construcción | 0,62 | 0,15 | 3,23 | 0,0130 | 0,0031 | 0,0676 |
| Tránsito de Vehículos<br>por Caminos<br>Pavimentados | Transporte Hormigón | 0,62 | 0,15 | 3,23 | 0,0130 | 0,0031 | 0,0676 |
| Tránsito de Vehículos<br>por Caminos<br>Pavimentados | Transporte de H2O Potable | 0,62 | 0,15 | 3,23 | 0,0130 | 0,0031 | 0,0676 |
| Tránsito de Vehículos<br>por Caminos<br>Pavimentados | Transporte de Agua Industrial<br>Para Construcción y Riego | 0,62 | 0,15 | 3,23 | 0,0130 | 0,0031 | 0,0676 |
| Tránsito de Vehículos<br>por Caminos<br>Pavimentados | Transporte H2O Servidas | 0,62 | 0,15 | 3,23 | 0,0130 | 0,0031 | 0,0676 |
| Tránsito de Vehículos<br>por Caminos<br>Pavimentados | Transporte Residuos | 0,62 | 0,15 | 3,23 | 0,0130 | 0,0031 | 0,0676 |
| Tránsito de Vehículos<br>por Caminos<br>Pavimentados | Transporte Personal<br>Construcción Planta | 0,62 | 0,15 | 3,23 | 0,0029 | 0,0007 | 0,0149 |
| Tránsito de Vehículos<br>por Caminos<br>Pavimentados | Transporte Supervisión | 0,62 | 0,15 | 3,23 | 0,0012 | 0,0003 | 0,0064 |
| Transito Vehículos<br>Livianos por Caminos<br>No Pavimentados | Transporte Personal<br>Construcción Planta | 1,5 | 0,15 | 4,9 | 0,2071 | 0,0207 | 0,6764 |
| Transito Vehículos<br>Livianos por Caminos<br>No Pavimentados | Transporte Supervisión | 1,5 | 0,15 | 4,9 | 0,2071 | 0,0207 | 0,6764 |
| Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados | Transporte Materiales de<br>Construcción | 1,5 | 0,15 | 4,9 | 0,8347 | 0,0835 | 2,9214 |
| Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados | Transporte de material para<br>relleno y construcción de<br>parapetos | 1,5 | 0,15 | 4,9 | 0,8347 | 0,0835 | 2,9214 |
| Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados | Transporte Otros Materiales<br>de Construcción | 1,5 | 0,15 | 4,9 | 0,8347 | 0,0835 | 2,9214 |
| Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados | Transporte Árido Para<br>Construcción | 1,5 | 0,15 | 4,9 | 0,8347 | 0,0835 | 2,9214 |
| Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados | Transporte Hormigón | 1,5 | 0,15 | 4,9 | 0,8347 | 0,0835 | 2,9214 |
| Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados | Transporte de H2O Potable | 1,5 | 0,15 | 4,9 | 0,8347 | 0,0835 | 2,9214 |

<!-- Estadísticas: 25 filas, 8 columnas -->
<!-- Contexto posterior: -->
<!-- **BORDOLI & Consultores EIRL** Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 59 Antofagasta -->
<!-- FIN TABLA 36 -->

Tabla 37: Factores de Emisión (MP10, MP2.5 y MPS) - Actividades Fase de Operación ....................................................... 60

<!-- INICIO TABLA 37 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Col1|Transporte de Agua Industrial<br>Para Construcción y Riego|1,5|0,15|4,9|0,8347|0,0835|2,9214| |---|---|---|---|---|---|---|---| ||Transporte H2O Servidas|1,5|0,15|4,9|0,8347|0,0835|2,9214| ||Transporte Residuos|1,5|0,15|4,9|0,8347|0,0835|2,9214| -->

**Tabla 37: Factores de Emisión (MP10, MP2.5 y MPS) - Actividades Fase de Operación****

| ACTIVIDAD | Actividad Específica | Parámetros para<br>Factores de Emisión | Col4 | Col5 | Factor de<br>emisión<br>PM10 | Factor de<br>emisión<br>PM2.5 | Factor<br>emisión<br>MPS |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **ACTIVIDAD** | **Actividad Específica** | **k10 ** | **k2,5 ** | **kMPS ** | **kMPS ** | **kMPS ** | **kMPS ** |
| Tránsito por Caminos<br>Pavimentados | Transporte de agua potable | 0,62 | 0,15 | 3,23 | 0,0121 | 0,0029 | 0,0631 |
| Tránsito por Caminos<br>Pavimentados | Transporte de Agua<br>Industrial | 0,62 | 0,15 | 3,23 | 0,0121 | 0,0029 | 0,0631 |
| Tránsito por Caminos<br>Pavimentados | Transporte de Combustible<br>(Petróleo Diésel) | 0,62 | 0,15 | 3,23 | 0,0121 | 0,0029 | 0,0631 |
| Tránsito por Caminos<br>Pavimentados | Transporte de Materias<br>Primas | 0,62 | 0,15 | 3,23 | 0,0121 | 0,0029 | 0,0631 |
| Tránsito por Caminos<br>Pavimentados | Transporte de Producto<br>(Emulsión) | 0,62 | 0,15 | 3,23 | 0,0121 | 0,0029 | 0,0631 |
| Tránsito por Caminos<br>Pavimentados | Transporte de Producto<br>(Anfo) | 0,62 | 0,15 | 3,23 | 0,0121 | 0,0029 | 0,0631 |
| Tránsito por Caminos<br>Pavimentados | Transporte de Residuos | 0,62 | 0,15 | 3,23 | 0,0121 | 0,0029 | 0,0631 |
| Tránsito por Caminos<br>Pavimentados | Transporte Personal de<br>Operaciones | 0,62 | 0,15 | 3,23 | 0,0029 | 0,0007 | 0,0149 |
| Tránsito por Caminos<br>Pavimentados | Transporte Supervisores | 0,62 | 0,15 | 3,23 | 0,0012 | 0,0003 | 0,0064 |
| Transito Vehículos<br>Livianos por Caminos<br>No Pavimentados | Transporte Personal de<br>Operaciones | 1,5 | 0,15 | 4,9 | 0,2071 | 0,0207 | 0,6764 |
| Transito Vehículos<br>Livianos por Caminos<br>No Pavimentados | Transporte Supervisores | 1,5 | 0,15 | 4,9 | 0,2071 | 0,0207 | 0,6764 |
| Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados | Transporte de agua potable | 1,5 | 0,15 | 4,9 | 0,8099 | 0,0810 | 2,8344 |
| Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados | Transporte de Agua<br>Industrial | 1,5 | 0,15 | 4,9 | 0,8099 | 0,0810 | 2,8344 |
| Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados | Transporte de Combustible<br>(Petróleo Diésel) | 1,5 | 0,15 | 4,9 | 0,8099 | 0,0810 | 2,8344 |
| Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados | Transporte de Materias<br>Primas | 1,5 | 0,15 | 4,9 | 0,8099 | 0,0810 | 2,8344 |
| Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados | Transporte de Producto<br>(Emulsión) | 1,5 | 0,15 | 4,9 | 0,8099 | 0,0810 | 2,8344 |
| Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados | Transporte de Producto<br>(Anfo) | 1,5 | 0,15 | 4,9 | 0,8099 | 0,0810 | 2,8344 |
| Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados | Transporte Interno de<br>materias primas y productos | 1,5 | 0,15 | 4,9 | 0,8099 | 0,0810 | 2,8344 |
| Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados | Transporte de Residuos | 1,5 | 0,15 | 4,9 | 0,8099 | 0,0810 | 2,8344 |

<!-- Estadísticas: 20 filas, 8 columnas -->
<!-- Contexto posterior: -->
<!-- **BORDOLI & Consultores EIRL** Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 60 Antofagasta -->
<!-- FIN TABLA 37 -->


Tabla 38: Factores de Emisión (MP10, MP2.5 y MPS) - Actividades Fase de Cierre .............................................................. 61

<!-- INICIO TABLA 38 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Informe de Emisiones Declaración de Impacto Ambiental Proyecto NAVÍO II -->

**Tabla 38: Factores de Emisión (MP10, MP2.5 y MPS) - Actividades Fase de Cierre****

| ACTIVIDAD | Actividad Específica | Parámetros para<br>Factores de Emisión | Col4 | Col5 | Factor de<br>emisión<br>PM10 | Factor de<br>emisión<br>PM2.5 | Factor<br>emisión<br>MPS |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **ACTIVIDAD** | **Actividad Específica** | **k10 ** | **k2,5 ** | **kMPS ** | **kMPS ** | **kMPS ** | **kMPS ** |
| Reperfilado | Reperfilamiento 10% del<br>Área total del Proyecto | 0,75 | 0,105 | 1 | 4,2750 | 0,5985 | 5,7000 |
| Tránsito por Caminos<br>Pavimentados" | Transporte Material de<br>Desarme | 0,62 | 0,15 | 3,23 | 0,0085 | 0,0021 | 0,0445 |
| Tránsito por Caminos<br>Pavimentados" | Transporte Residuos Varios | 0,62 | 0,15 | 3,23 | 0,0085 | 0,0021 | 0,0445 |
|  | Transporte Riego Caminos | 0,62 | 0,15 | 3,23 | 0,0085 | 0,0021 | 0,0445 |
|  | Transporte de Personal | 0,62 | 0,15 | 3,23 | 0,0029 | 0,0007 | 0,0149 |
|  | Transporte de Supervisión | 0,62 | 0,15 | 3,23 | 0,0012 | 0,0003 | 0,0064 |
| Transito Vehículos<br>Livianos por Caminos<br>No Pavimentados | Personal Cierre de Faena | 1,5 | 0,15 | 4,9 | 0,2071 | 0,0207 | 0,6764 |
| Transito Vehículos<br>Livianos por Caminos<br>No Pavimentados | Supervisión | 1,5 | 0,15 | 4,9 | 0,2071 | 0,0207 | 0,6764 |
| Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados | Transporte Material de<br>Desarme | 1,5 | 0,15 | 4,9 | 0,6943 | 0,0694 | 2,4301 |
| Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados | Transporte Riego Caminos | 1,5 | 0,15 | 4,9 | 0,6943 | 0,0694 | 2,4301 |
| Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados | Transporte Residuos Varios | 1,5 | 0,15 | 4,9 | 0,6943 | 0,0694 | 2,4301 |

<!-- Estadísticas: 12 filas, 8 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 39: Emisiones (MP10, MP2.5 y MPS) - Actividades Etapa de Construcción** |ACTIVIDAD|Actividad Específica|Emisiones Diarias<br>(kg/día)|Col4|Col5|Emisiones Anuales<br>(ton/año)|Col7|Col8| |---|---|---|---|---|---|---|---| -->
<!-- FIN TABLA 38 -->


Tabla 39: Emisiones (MP10, MP2.5 y MPS) - Actividades Etapa de Construcción ................................................................. 61

<!-- INICIO TABLA 39 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Transito Vehículos<br>Livianos por Caminos<br>No Pavimentados|Supervisión|1,5|0,15|4,9|0,2071|0,0207|0,6764| |Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados|Transporte Material de<br>Desarme|1,5|0,15|4,9|0,6943|0,0694|2,4301| |Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados|Transporte Riego Caminos|1,5|0,15|4,9|0,6943|0,0694|2,4301| |Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados|Transporte Residuos Varios|1,5|0,15|4,9|0,6943|0,0694|2,4301| -->

**Tabla 39: Emisiones (MP10, MP2.5 y MPS) - Actividades Etapa de Construcción****

| ACTIVIDAD | Actividad Específica | Emisiones Diarias<br>(kg/día) | Col4 | Col5 | Emisiones Anuales<br>(ton/año) | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **ACTIVIDAD** | **Actividad Específica** | **PM10 ** | **PM2.5 ** | **MPS** | **PM10 ** | **PM2.5 ** | **MPS** |
| Escarpe | Escarpe Área Total | 5,87 | 0,82 | 7,83 | 0,18 | 0,02 | 0,23 |
| Excavaciones | Excavación totales | 1,26 | 0,18 | 6,15 | 0,04 | 0,01 | 0,18 |
| Carguío y Volteo de<br>Camiones | Carga y descarga de material de<br>excavaciones | 0,03 | 0,01 | 0,07 | 0,00 | 0,00 | 0,00 |
| Carguío y Volteo de<br>Camiones | Carga y descarga de material para<br>construcción de parapetos (canchas de<br>nitratos y polvorines) | 0,75 | 0,11 | 1,59 | 0,02 | 0,00 | 0,05 |
| Carguío y Volteo de<br>Camiones | Carga y descarga de áridos | 0,01 | 0,00 | 0,01 | 0,00 | 0,00 | 0,00 |
| Carguío y Volteo de<br>Camiones | Carga y Descarga material para rellenos | 0,39 | 0,06 | 0,84 | 0,01 | 0,00 | 0,03 |
| Tránsito de Vehículos<br>por Caminos<br>Pavimentados | Transporte Materiales de Construcción | 0,68 | 0,17 | 3,57 | 0,12 | 0,03 | 0,64 |
| Tránsito de Vehículos<br>por Caminos<br>Pavimentados | Transporte Otros Materiales de<br>Construcción | 0,59 | 0,14 | 3,09 | 0,11 | 0,03 | 0,56 |
| Tránsito de Vehículos<br>por Caminos<br>Pavimentados | Transporte Árido Para Construcción | 0,48 | 0,12 | 2,52 | 0,03 | 0,01 | 0,15 |
| Tránsito de Vehículos<br>por Caminos<br>Pavimentados | Transporte Hormigón | 0,48 | 0,12 | 2,52 | 0,03 | 0,01 | 0,15 |
| Tránsito de Vehículos<br>por Caminos<br>Pavimentados | Transporte de H2O Potable | 0,48 | 0,12 | 2,52 | 0,09 | 0,02 | 0,45 |
| Tránsito de Vehículos<br>por Caminos<br>Pavimentados | Transporte de Agua Industrial Para<br>Construcción y Riego | 4,54 | 1,10 | 23,66 | 0,82 | 0,20 | 4,26 |
| Tránsito de Vehículos<br>por Caminos<br>Pavimentados | Transporte H2O Servidas | 0,91 | 0,22 | 4,73 | 0,16 | 0,04 | 0,85 |
| Tránsito de Vehículos<br>por Caminos<br>Pavimentados | Transporte Residuos | 0,50 | 0,12 | 2,63 | 0,09 | 0,02 | 0,47 |
| Tránsito de Vehículos<br>por Caminos<br>Pavimentados | Transporte Personal Construcción<br>Planta | 0,40 | 0,10 | 2,08 | 0,07 | 0,02 | 0,38 |
| Tránsito de Vehículos<br>por Caminos<br>Pavimentados | Transporte Supervisión | 0,34 | 0,08 | 1,79 | 0,06 | 0,01 | 0,32 |
| Transito Vehículos | Transporte Personal Construcción | 0,78 | 0,08 | 2,54 | 0,14 | 0,01 | 0,46 |

<!-- Estadísticas: 18 filas, 8 columnas -->
<!-- Contexto posterior: -->
<!-- **BORDOLI & Consultores EIRL** Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 61 Antofagasta -->
<!-- FIN TABLA 39 -->

Tabla 40: Emisiones (MP10, MP2.5 y MPS) - Actividades Fase de Operación ........................................................................ 62

<!-- INICIO TABLA 40 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados|Transporte de Agua Industrial Para<br>Construcción y Riego|7,83|0,78|27,39|1,41|0,14|4,93| |Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados|Transporte H2O Servidas|2,25|0,23|7,89|0,41|0,04|1,42| |Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados|Transporte Residuos|0,87|0,09|3,04|0,16|0,02|0,55| |**TOTALES**|**TOTALES**|**43,45**|**6,03**|**155,03**|**6,26**|**0,86**|**24,12**| -->

**Tabla 40: Emisiones (MP10, MP2.5 y MPS) - Actividades Fase de Operación****

| ACTIVIDAD | Actividad Específica | Emisiones Diarias<br>(kg/día) | Col4 | Col5 | Emisiones Anuales<br>(ton/año) | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **ACTIVIDAD** | **Actividad Específica** | **PM10 ** | **PM2.5 ** | **MPS** | **PM10 ** | **PM2.5 ** | **MPS** |
| Tránsito por Caminos<br>Pavimentados | Transporte de agua potable | 0,47 | 0,11 | 2,43 | 0,01 | 0,00 | 0,07 |
| Tránsito por Caminos<br>Pavimentados | Transporte de Agua Industrial | 1,70 | 0,41 | 8,84 | 0,05 | 0,01 | 0,27 |
| Tránsito por Caminos<br>Pavimentados | Transporte de Combustible (Petróleo<br>Diésel) | 0,51 | 0,12 | 2,68 | 0,02 | 0,00 | 0,08 |
| Tránsito por Caminos<br>Pavimentados | Transporte de Materias Primas | 5,42 | 1,31 | 28,24 | 0,16 | 0,04 | 0,85 |
| Tránsito por Caminos<br>Pavimentados | Transporte de Producto (Emulsión) | 6,60 | 1,60 | 34,36 | 0,20 | 0,05 | 1,03 |
| Tránsito por Caminos<br>Pavimentados | Transporte de Producto (Anfo) | 0,85 | 0,21 | 4,42 | 0,03 | 0,01 | 0,13 |
| Tránsito por Caminos<br>Pavimentados | Transporte de Residuos | 3,14 | 0,76 | 16,35 | 0,09 | 0,02 | 0,49 |
| Tránsito por Caminos<br>Pavimentados | Transporte Personal de Operaciones | 0,40 | 0,10 | 2,08 | 0,01 | 0,00 | 0,06 |
| Tránsito por Caminos<br>Pavimentados | Transporte Supervisores | 0,51 | 0,12 | 2,68 | 0,02 | 0,00 | 0,08 |
| Transito Vehículos<br>Livianos por Caminos<br>No Pavimentados | Transporte Personal de Operaciones | 0,78 | 0,08 | 2,54 | 0,02 | 0,00 | 0,08 |
| Transito Vehículos<br>Livianos por Caminos<br>No Pavimentados | Transporte Supervisores | 2,33 | 0,23 | 7,61 | 0,07 | 0,01 | 0,23 |
| Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados | Transporte de agua potable | 0,84 | 0,08 | 2,92 | 0,03 | 0,00 | 0,09 |
| Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados | Transporte de Agua Industrial | 3,04 | 0,30 | 10,63 | 0,09 | 0,01 | 0,32 |
| Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados | Transporte de Combustible (Petróleo<br>Diésel) | 0,92 | 0,09 | 3,22 | 0,03 | 0,00 | 0,10 |
| Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados | Transporte de Materias Primas | 9,70 | 0,97 | 33,97 | 0,29 | 0,03 | 1,02 |
| Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados | Transporte de Producto (Emulsión) | 11,81 | 1,18 | 41,34 | 0,35 | 0,04 | 1,24 |
| Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados | Transporte de Producto (Anfo) | 1,52 | 0,15 | 5,31 | 0,05 | 0,00 | 0,16 |
| Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados | Transporte Interno de materias primas y<br>productos | 9,70 | 0,97 | 33,97 | 0,29 | 0,03 | 1,02 |
| Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados | Transporte de Residuos | 5,62 | 0,56 | 19,66 | 0,17 | 0,02 | 0,59 |
| **TOTALES** | **TOTALES** | **65,85** | **9,37** | **263,24** | **1,98** | **0,28** | **7,90** |

<!-- Estadísticas: 21 filas, 8 columnas -->
<!-- Contexto posterior: -->
<!-- **BORDOLI & Consultores EIRL** Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 62 Antofagasta -->
<!-- FIN TABLA 40 -->


Tabla 41: Emisiones (MP10, MP2.5 y MPS) - Actividades Fase de Cierre .............................................................................. 63

<!-- INICIO TABLA 41 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Informe de Emisiones Declaración de Impacto Ambiental Proyecto NAVÍO II -->

**Tabla 41: Emisiones (MP10, MP2.5 y MPS) - Actividades Fase de Cierre****

| ACTIVIDAD | Actividad Específica | Emisiones Diarias<br>(kg/día) | Col4 | Col5 | Emisiones Anuales<br>(ton/año) | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **ACTIVIDAD** | **Actividad Específica** | **PM10 ** | **PM2.5 ** | **MPS** | **PM10 ** | **PM2.5 ** | **MPS** |
| Reperfilado | Reperfilamiento 10% del Área total del<br>Proyecto | 1,02 | 0,14 | 1,36 | 0,03 | 0,00 | 0,04 |
| Tránsito por Caminos<br>Pavimentados" | Transporte Material de Desarme | 0,47 | 0,11 | 2,45 | 0,08 | 0,02 | 0,44 |
| Tránsito por Caminos<br>Pavimentados" | Transporte Residuos Varios | 0,60 | 0,14 | 3,12 | 0,11 | 0,03 | 0,56 |
| Tránsito por Caminos<br>Pavimentados" | Transporte Riego Caminos | 0,19 | 0,05 | 1,00 | 0,03 | 0,01 | 0,18 |
| Tránsito por Caminos<br>Pavimentados" | Transporte de Personal | 0,20 | 0,05 | 1,04 | 0,04 | 0,01 | 0,19 |
| Tránsito por Caminos<br>Pavimentados" | Transporte de Supervisión | 0,26 | 0,06 | 1,34 | 0,05 | 0,01 | 0,24 |
| Transito Vehículos<br>Livianos por Caminos<br>No Pavimentados | Personal Cierre de Faena | 1,55 | 0,16 | 5,07 | 0,05 | 0,00 | 0,15 |
| Transito Vehículos<br>Livianos por Caminos<br>No Pavimentados | Supervisión | 4,66 | 0,47 | 15,22 | 0,14 | 0,01 | 0,46 |
| Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados | Transporte Material de Desarme | 1,02 | 0,10 | 3,58 | 0,18 | 0,02 | 0,64 |
| Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados | Transporte Riego Caminos | 3,91 | 0,39 | 13,67 | 0,70 | 0,07 | 2,46 |
| Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados | Transporte Residuos Varios | 1,30 | 0,13 | 4,56 | 0,23 | 0,02 | 0,82 |
| TOTALES | TOTALES | **15,18** | **1,80** | **52,41** | **1,65** | **0,21** | **6,19** |

<!-- Estadísticas: 13 filas, 8 columnas -->
<!-- Contexto posterior: -->
<!-- **BORDOLI & Consultores EIRL** Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 63 Antofagasta -->
<!-- FIN TABLA 41 -->


Tabla 42: Emisiones de Gases y MP Combustión de Motores [kg/día] - Fase de Construcción .............................................. 64

<!-- INICIO TABLA 42 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Informe de Emisiones Declaración de Impacto Ambiental Proyecto NAVÍO II -->

**Tabla 42: Emisiones de Gases y MP Combustión de Motores [kg/día] - Fase de Construcción****

| Emisiones de Gases y Material Particulado Asociado a la Combustión de Motores [kg/día] | Col2 | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Equipo** | **Cantidad** | **Potencia**<br>**Nominal kw** | **Operación**<br>**Diaria**<br>**(horas)** | **CO** | **HC** | **NOx** | **MP** | **MP10 ** | **MP2,5 ** |
| Bulldozer CAT modelo D5K o similar | 1 | 72 | 15 | 0,08 | 0,03 | 0,22 | 0,02 | 0,02 | 0,02 |
| Cargador frontal CAT modelo 924HZ o similar | 1 | 106 | 30 | 0,11 | 0,05 | 0,43 | 0,04 | 0,04 | 0,04 |
| Retroexcavadora CAT modelo 416F o similar | 1 | 65 | 30 | 0,15 | 0,07 | 0,43 | 0,05 | 0,05 | 0,05 |
| Compactador CAT Modelo CB-434D o similar | 1 | 62 | 15 | 0,08 | 0,03 | 0,22 | 0,02 | 0,02 | 0,02 |
| Motoniveladora CAT modelo 120M2 AWD o similar | 1 | 108 | 15 | 0,06 | 0,03 | 0,22 | 0,02 | 0,02 | 0,02 |
| Excavadora CAT modelo 315C o similar | 1 | 82 | 30 | 0,11 | 0,07 | 0,43 | 0,05 | 0,05 | 0,05 |
| **TOTAL FASE DE CONSTRUCCIÓN** | **TOTAL FASE DE CONSTRUCCIÓN** | **TOTAL FASE DE CONSTRUCCIÓN** | **TOTAL FASE DE CONSTRUCCIÓN** | **0,59** | **0,29** | **1,94** | **0,19** | **0,19** | **0,19** |

<!-- Estadísticas: 8 filas, 10 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 43: Emisiones de Gases y MP Combustión de Motores [kg/día] - Fase de Operación** |Emisiones de Gases y Material Particulado Asociado a la Combustión de Motores [kg/día]|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10| |---|---|---|---|---|---|---|---|---|---| -->
<!-- FIN TABLA 42 -->

Tabla 43: Emisiones de Gases y MP Combustión de Motores [kg/día] - Fase de Operación .................................................. 64

<!-- INICIO TABLA 43 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Compactador CAT Modelo CB-434D o similar|1|62|15|0,08|0,03|0,22|0,02|0,02|0,02| |Motoniveladora CAT modelo 120M2 AWD o similar|1|108|15|0,06|0,03|0,22|0,02|0,02|0,02| |Excavadora CAT modelo 315C o similar|1|82|30|0,11|0,07|0,43|0,05|0,05|0,05| |**TOTAL FASE DE CONSTRUCCIÓN**|**TOTAL FASE DE CONSTRUCCIÓN**|**TOTAL FASE DE CONSTRUCCIÓN**|**TOTAL FASE DE CONSTRUCCIÓN**|**0,59**|**0,29**|**1,94**|**0,19**|**0,19**|**0,19**| -->

**Tabla 43: Emisiones de Gases y MP Combustión de Motores [kg/día] - Fase de Operación****

| Emisiones de Gases y Material Particulado Asociado a la Combustión de Motores [kg/día] | Col2 | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Equipo** | **Cantidad** | **Potencia**<br>**Nominal kw** | **Operación**<br>**Diaria**<br>**(horas)** | **CO** | **HC** | **NOx** | **MP** | **MP10 ** | **MP2,5 ** |
| Grúa Horquilla | 4 | 30 | 24 | 0,62 | 0,28 | 1,38 | 0,17 | 0,17 | 0,17 |
| **TOTAL FASE DE OPERACIÓN** | **TOTAL FASE DE OPERACIÓN** | **TOTAL FASE DE OPERACIÓN** | **TOTAL FASE DE OPERACIÓN** | **0,62** | **0,28** | **1,38** | **0,17** | **0,17** | **0,17** |

<!-- Estadísticas: 3 filas, 10 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 44: Emisiones de Gases y MP Combustión de Motores [kg/día] - Fase de Cierre** |Emisiones de Gases y Material Particulado Asociado a la Combustión de Motores [kg/día]|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10| |---|---|---|---|---|---|---|---|---|---| -->
<!-- FIN TABLA 43 -->


Tabla 44: Emisiones de Gases y MP Combustión de Motores [kg/día] - Fase de Cierre ......................................................... 64

<!-- INICIO TABLA 44 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |---|---|---|---|---|---|---|---|---|---| |**Equipo**|**Cantidad**|**Potencia**<br>**Nominal kw**|**Operación**<br>**Diaria**<br>**(horas)**|**CO**|**HC**|**NOx**|**MP**|**MP10 **|**MP2,5 **| |Grúa Horquilla|4|30|24|0,62|0,28|1,38|0,17|0,17|0,17| |**TOTAL FASE DE OPERACIÓN**|**TOTAL FASE DE OPERACIÓN**|**TOTAL FASE DE OPERACIÓN**|**TOTAL FASE DE OPERACIÓN**|**0,62**|**0,28**|**1,38**|**0,17**|**0,17**|**0,17**| -->

**Tabla 44: Emisiones de Gases y MP Combustión de Motores [kg/día] - Fase de Cierre****

| Emisiones de Gases y Material Particulado Asociado a la Combustión de Motores [kg/día] | Col2 | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Equipo** | **Cantidad** | **Potencia**<br>**Nominal kw** | **Operación**<br>**Diaria**<br>**(horas)** | **CO** | **HC** | **NOx** | **MP** | **MP10 ** | **MP2,5 ** |
| Bulldozer CAT modelo D5K o similar | 1 | 72 | 15 | 0,08 | 0,03 | 0,22 | 0,02 | 0,02 | 0,02 |
| Cargador frontal CAT modelo 924HZ o similar | 1 | 106 | 30 | 0,11 | 0,05 | 0,43 | 0,04 | 0,04 | 0,04 |
| **TOTAL FASE DE CIERRE** | **TOTAL FASE DE CIERRE** | **TOTAL FASE DE CIERRE** | **TOTAL FASE DE CIERRE** | **0,19** | **0,09** | **0,65** | **0,06** | **0,06** | **0,06** |

<!-- Estadísticas: 4 filas, 10 columnas -->
<!-- Contexto posterior: -->
<!-- **BORDOLI & Consultores EIRL** Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 64 Antofagasta -->
<!-- FIN TABLA 44 -->


Tabla 45: Emisiones de Gases y MP Asociado a Vehículos [kg/día] - Fase de Construcción ................................................. 65

<!-- INICIO TABLA 45 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Informe de Emisiones Declaración de Impacto Ambiental Proyecto NAVÍO II -->

**Tabla 45: Emisiones de Gases y MP Asociado a Vehículos [kg/día] - Fase de Construcción****

| Vehículo | N°<br>Viajes/día | Distancia (km) | Col4 | Velocidad km/h | Col6 | CO | HC | NOx | MP | MP<br>10 | MP<br>2,5 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Vehículo** | **N°**<br>**Viajes/día** | **CP** | **CNP** | **CP** | **CNP** | **CNP** | **CNP** | **CNP** | **CNP** | **CNP** | **CNP** |
| Transporte Materiales de Construcción | 1 | 35 | 3,75 | 100 | 30 | 0,041 | 0,007 | 0,174 | 0,003 | 0,002 | 0,002 |
| Transporte de material para relleno y<br>construcción de parapetos | 19 | 35 | 1 | 100 | 30 | 0,508 | 0,095 | 2,550 | 0,050 | 0,001 | 0,001 |
| Transporte Otros Materiales de Construcción | 1 | 35 | 3,75 | 100 | 30 | 0,036 | 0,006 | 0,151 | 0,003 | 0,000 | 0,000 |
| Transporte Árido Para Construcción | 1 | 35 | 3,75 | 100 | 30 | 0,029 | 0,005 | 0,123 | 0,002 | 0,000 | 0,000 |
| Transporte Hormigón | 1 | 35 | 3,75 | 100 | 30 | 0,029 | 0,005 | 0,123 | 0,002 | 0,000 | 0,000 |
| Transporte de H2O Potable | 1 | 35 | 3,75 | 100 | 30 | 0,017 | 0,003 | 0,081 | 0,002 | 0,001 | 0,001 |
| Transporte de Agua Industrial Para<br>Construcción y Riego | 1 | 35 | 3,75 | 100 | 30 | 0,054 | 0,009 | 0,231 | 0,005 | 0,004 | 0,004 |
| Transporte H2O Servidas | 1 | 35 | 3,75 | 100 | 30 | 0,045 | 0,009 | 0,219 | 0,004 | 0,001 | 0,001 |
| Transporte Residuos | 1 | 35 | 3,75 | 100 | 30 | 0,017 | 0,003 | 0,085 | 0,002 | 0,001 | 0,001 |
| Transporte Personal Construcción Planta | 2 | 35 | 3,75 | 100 | 30 | 0,101 | 0,023 | 0,453 | 0,009 | 0,009 | 0,009 |
| Transporte Supervisión | 4 | 35 | 3,75 | 100 | 30 | 0,087 | 0,011 | 0,164 | 0,015 | 0,014 | 0,014 |
| Transporte Materiales de Construcción | 1 | 35 | 3,75 | 100 | 30 | 0,041 | 0,007 | 0,174 | 0,003 | 0,002 | 0,002 |
| Transporte de material para relleno y<br>construcción de parapetos | 19 | 35 | 1 | 100 | 30 | 0,508 | 0,095 | 2,550 | 0,050 | 0,001 | 0,001 |
| Transporte Otros Materiales de Construcción | 1 | 35 | 3,75 | 100 | 30 | 0,036 | 0,006 | 0,151 | 0,003 | 0,000 | 0,000 |
| Transporte Árido Para Construcción | 1 | 35 | 3,75 | 100 | 30 | 0,029 | 0,005 | 0,123 | 0,002 | 0,000 | 0,000 |
| Transporte Hormigón | 1 | 35 | 3,75 | 100 | 30 | 0,029 | 0,005 | 0,123 | 0,002 | 0,000 | 0,000 |
| Transporte de H2O Potable | 1 | 35 | 3,75 | 100 | 30 | 0,017 | 0,003 | 0,081 | 0,002 | 0,001 | 0,001 |
| Transporte de Agua Industrial Para<br>Construcción y Riego | 1 | 35 | 3,75 | 100 | 30 | 0,054 | 0,009 | 0,231 | 0,005 | 0,004 | 0,004 |
| **TOTALES FASE DE CONSTRUCCIÓN** | **TOTALES FASE DE CONSTRUCCIÓN** | **TOTALES FASE DE CONSTRUCCIÓN** | **TOTALES FASE DE CONSTRUCCIÓN** | **TOTALES FASE DE CONSTRUCCIÓN** | **TOTALES FASE DE CONSTRUCCIÓN** | **0,965** | **0,176** | **4,355** | **0,098** | **0,034** | **0,034** |

<!-- Estadísticas: 20 filas, 12 columnas -->
<!-- Contexto posterior: -->
<!-- CP: Camino Pavimentado - CNP: Camino No Pavimentado **BORDOLI & Consultores EIRL** Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 65 -->
<!-- FIN TABLA 45 -->

Tabla 46: Emisiones de Gases y MP Asociado a Vehículos [kg/día] - Etapa de Operación .................................................... 66

<!-- INICIO TABLA 46 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Informe de Emisiones Declaración de Impacto Ambiental Proyecto NAVÍO II -->

**Tabla 46: Emisiones de Gases y MP Asociado a Vehículos [kg/día] - Etapa de Operación****

| Vehículo | N°<br>Viajes/día | Distancia (km) | Col4 | Velocidad km/h | Col6 | CO | HC | NOx | MP | MP<br>10 | MP<br>2,5 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Vehículo** | **N°**<br>**Viajes/día** | **CP** | **CNP** | **CP** | **CNP** | **CNP** | **CNP** | **CNP** | **CNP** | **CNP** | **CNP** |
| Transporte de agua potable | 1 | 35 | 3,75 | 100 | 30 | 0,017 | 0,003 | 0,084 | 0,002 | 0,001 | 0,001 |
| Transporte de Agua Industrial | 2 | 35 | 3,75 | 100 | 30 | 0,063 | 0,012 | 0,305 | 0,006 | 0,001 | 0,001 |
| Transporte de Combustible (Petróleo Diésel) | 1 | 35 | 3,75 | 100 | 30 | 0,033 | 0,006 | 0,140 | 0,003 | 0,002 | 0,002 |
| Transporte de Materias primas | 6 | 35 | 3,75 | 100 | 30 | 0,348 | 0,059 | 1,478 | 0,030 | 0,002 | 0,002 |
| Transporte de Producto (Emulsión) | 8 | 35 | 3,75 | 100 | 30 | 0,423 | 0,072 | 1,799 | 0,036 | 0,002 | 0,002 |
| Transporte de Producto (Anfo) | 1 | 35 | 3,75 | 100 | 30 | 0,054 | 0,009 | 0,231 | 0,005 | 0,002 | 0,002 |
| Transporte de Residuos | 6 | 35 | 3,75 | 100 | 30 | 0,200 | 0,038 | 0,974 | 0,019 | 0,001 | 0,001 |
| Transporte Interno de materias primas y<br>productos | 4 | 0 | 3 | 100 | 30 | 0,028 | 0,006 | 0,097 | 0,003 | 0,002 | 0,002 |
| Transporte Personal de Operaciones | 2 | 35 | 3,75 | 100 | 30 | 0,101 | 0,023 | 0,453 | 0,009 | 0,009 | 0,009 |
| Transporte Supervisores | 6 | 35 | 3,75 | 100 | 30 | 0,131 | 0,016 | 0,245 | 0,023 | 0,014 | 0,014 |
| **TOTALES FASE DE OPERACIÓN** | **TOTALES FASE DE OPERACIÓN** | **TOTALES FASE DE OPERACIÓN** | **TOTALES FASE DE OPERACIÓN** | **TOTALES FASE DE OPERACIÓN** | **TOTALES FASE DE OPERACIÓN** | **1,40** | **0,24** | **5,81** | **0,13** | **0,04** | **0,04** |

<!-- Estadísticas: 12 filas, 12 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 47: Emisiones de Gases y MP Asociado a Vehículos [kg/día] - Etapa de Cierre** |Vehículo|N°<br>Viajes/día|Distancia (km)|Col4|Velocidad km/h|Col6|CO|HC|NOx|MP|MP<br>10|MP<br>2,5| |---|---|---|---|---|---|---|---|---|---|---|---| -->
<!-- FIN TABLA 46 -->


Tabla 47: Emisiones de Gases y MP Asociado a Vehículos [kg/día] - Etapa de Cierre ........................................................... 66

<!-- INICIO TABLA 47 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Transporte Interno de materias primas y<br>productos|4|0|3|100|30|0,028|0,006|0,097|0,003|0,002|0,002| |Transporte Personal de Operaciones|2|35|3,75|100|30|0,101|0,023|0,453|0,009|0,009|0,009| |Transporte Supervisores|6|35|3,75|100|30|0,131|0,016|0,245|0,023|0,014|0,014| |**TOTALES FASE DE OPERACIÓN**|**TOTALES FASE DE OPERACIÓN**|**TOTALES FASE DE OPERACIÓN**|**TOTALES FASE DE OPERACIÓN**|**TOTALES FASE DE OPERACIÓN**|**TOTALES FASE DE OPERACIÓN**|**1,40**|**0,24**|**5,81**|**0,13**|**0,04**|**0,04**| -->

**Tabla 47: Emisiones de Gases y MP Asociado a Vehículos [kg/día] - Etapa de Cierre****

| Vehículo | N°<br>Viajes/día | Distancia (km) | Col4 | Velocidad km/h | Col6 | CO | HC | NOx | MP | MP<br>10 | MP<br>2,5 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Vehículo** | **N°**<br>**Viajes/día** | **CP** | **CNP** | **CP** | **CNP** | **CNP** | **CNP** | **CNP** | **CNP** | **CNP** | **CNP** |
| Transporte Material de Desarme | 1 | 35 | 3,75 | 100 | 30 | 0,043 | 0,007 | 0,182 | 0,004 | 0,002 | 0,002 |
| Transporte Residuos Varios | 1 | 35 | 3,75 | 100 | 30 | 0,043 | 0,007 | 0,182 | 0,004 | 0,002 | 0,002 |
| Transporte Riego Caminos | 3 | 35 | 3,75 | 100 | 30 | 0,094 | 0,018 | 0,457 | 0,009 | 0,001 | 0,001 |
| Transporte Personal de Cierre | 1 | 35 | 3,75 | 100 | 30 | 0,051 | 0,012 | 0,226 | 0,005 | 0,009 | 0,009 |
| Transporte Supervisores | 3 | 35 | 3,75 | 100 | 30 | 0,065 | 0,008 | 0,123 | 0,012 | 0,014 | 0,014 |
| **TOTALES FASE DE CIERRE** | **TOTALES FASE DE CIERRE** | **TOTALES FASE DE CIERRE** | **TOTALES FASE DE CIERRE** | **TOTALES FASE DE CIERRE** | **TOTALES FASE DE CIERRE** | **0,296** | **0,052** | **1,170** | **0,033** | **0,027** | **0,027** |

<!-- Estadísticas: 7 filas, 12 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 48: Emisiones de Gases y Material Particulado Asociado a Combustión en Grupos Generadores** |Fase Proyecto|Potencia<br>(kw)|Combustibles<br>(tipo)|Operación<br>(h/día)|Cantidad|MP|MP10|MP2,5|CO|NOx|SOx| |---|---|---|---|---|---|---|---|---|---|---| -->
<!-- FIN TABLA 47 -->


Tabla 48: Emisiones de Gases y Material Particulado Asociado a Combustión en Grupos Generadores ............................... 66

<!-- INICIO TABLA 48 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Transporte Riego Caminos|3|35|3,75|100|30|0,094|0,018|0,457|0,009|0,001|0,001| |Transporte Personal de Cierre|1|35|3,75|100|30|0,051|0,012|0,226|0,005|0,009|0,009| |Transporte Supervisores|3|35|3,75|100|30|0,065|0,008|0,123|0,012|0,014|0,014| |**TOTALES FASE DE CIERRE**|**TOTALES FASE DE CIERRE**|**TOTALES FASE DE CIERRE**|**TOTALES FASE DE CIERRE**|**TOTALES FASE DE CIERRE**|**TOTALES FASE DE CIERRE**|**0,296**|**0,052**|**1,170**|**0,033**|**0,027**|**0,027**| -->

**Tabla 48: Emisiones de Gases y Material Particulado Asociado a Combustión en Grupos Generadores****

| Fase Proyecto | Potencia<br>(kw) | Combustibles<br>(tipo) | Operación<br>(h/día) | Cantidad | MP | MP10 | MP2,5 | CO | NOx | SOx |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Construcción | 24 | Diésel | 24,00 | 2,00 | 1,54 | 1,54 | 1,54 | 4,68 | 21,66 | 1,44 |
| Operación | 0 | 0 | 0 | 0 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| Cierre | 12 | Diésel | 24,00 | 1,00 | 0,39 | 0,39 | 0,39 | 1,17 | 5,41 | 0,36 |

<!-- Estadísticas: 3 filas, 11 columnas -->
<!-- Contexto posterior: -->
<!-- **BORDOLI & Consultores EIRL** Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 66 Antofagasta -->
<!-- FIN TABLA 48 -->


Tabla 49: Resumen Emisiones Fase de Construcción ............................................................................................................. 67

<!-- INICIO TABLA 49 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Proyecto NAVÍO II **TABLAS RESUMEN DE EMISIONES POR FASES DEL PROYECTO** -->

**Tabla 49: Resumen Emisiones Fase de Construcción****

| Fase de Construcción | MP10 | Col3 | MP2,5 | Col5 | MPS | Col7 | CO | Col9 | HC | Col11 | NOx | Col13 | SO<br>X | Col15 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Fase de Construcción** | **kg/día** | **ton/año** | **kg/día** | **ton/año** | **kg/día** | **ton/año** | **kg/día** | **ton/año** | **kg/día** | **ton/año** | **kg/día** | **ton/año** | **kg/día** | **ton/año** |
| Actividades | 43,45 | 6,26 | 6,03 | 0,86 | 155,03 | 21,15 | --- | --- | --- | --- | --- | --- | --- | --- |
| Maquinarias | 0,19 | 0,01 | 0,19 | 0,01 | 0,19 | 0,01 | 0,59 | 0,02 | 0,29 | 0,01 | 1,94 | 0,06 | --- | --- |
| Vehículos | 0,03 | 0,01 | 0,03 | 0,01 | 0,10 | 0,02 | 0,97 | 0,17 | 0,18 | 0,03 | 4,36 | 0,78 | --- | --- |
| Generadores | 1,54 | 0,28 | 1,54 | 0,28 | 1,54 | 0,28 | 4,68 | 0,84 | --- | --- | 21,66 | 3,90 | 1,44 | 0,26 |
| **TOTAL** | **45,21** | **6,55** | **7,79** | **1,15** | **156,86** | **21,45** | **6,24** | **1,03** | **0,47** | **0,04** | **27,96** | **4,74** | **1,44** | **0,26** |

<!-- Estadísticas: 6 filas, 15 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 50: Resumen Emisiones Fase de Operación** |Fase de Construcción|MP10|Col3|MP2,5|Col5|MPS|Col7|CO|Col9|HC|Col11|NOx|Col13|SO<br>X|Col15| |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---| -->
<!-- FIN TABLA 49 -->


Tabla 50: Resumen Emisiones Fase de Operación .................................................................................................................. 67

<!-- INICIO TABLA 50 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Maquinarias|0,19|0,01|0,19|0,01|0,19|0,01|0,59|0,02|0,29|0,01|1,94|0,06|---|---| |Vehículos|0,03|0,01|0,03|0,01|0,10|0,02|0,97|0,17|0,18|0,03|4,36|0,78|---|---| |Generadores|1,54|0,28|1,54|0,28|1,54|0,28|4,68|0,84|---|---|21,66|3,90|1,44|0,26| |**TOTAL**|**45,21**|**6,55**|**7,79**|**1,15**|**156,86**|**21,45**|**6,24**|**1,03**|**0,47**|**0,04**|**27,96**|**4,74**|**1,44**|**0,26**| -->

**Tabla 50: Resumen Emisiones Fase de Operación****

| Fase de Construcción | MP10 | Col3 | MP2,5 | Col5 | MPS | Col7 | CO | Col9 | HC | Col11 | NOx | Col13 | SO<br>X | Col15 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Fase de Construcción** | **kg/día** | **ton/año** | **kg/día** | **ton/año** | **kg/día** | **ton/año** | **kg/día** | **ton/año** | **kg/día** | **ton/año** | **kg/día** | **ton/año** | **kg/día** | **ton/año** |
| Actividades | 65,85 | 1,98 | 9,37 | 0,28 | 263,24 | 7,90 | --- | --- | --- | --- | --- | --- | --- | --- |
| Maquinarias | 1,17 | 0,43 | 1,17 | 0,43 | 1,17 | 0,43 | 0,62 | 0,23 | 0,28 | 0,10 | 1,38 | 0,50 | --- | --- |
| Vehículos | 0,04 | 0,01 | 0,04 | 0,01 | 0,13 | 0,05 | 1,40 | 0,51 | 0,24 | 0,09 | 5,81 | 2,12 | --- | --- |
| Caldera | 1,82 | 0,66 | 0,91 | 0,33 | 1,82 | 0,66 | 0,26 | 0,09 | --- | --- | 4,62 | 1,69 | 0,65 | 0,24 |
| **TOTAL** | **68,88** | **3,09** | **11,49** | **1,05** | **266,36** | **9,04** | **2,28** | **0,83** | **0,52** | **0,19** | **11,81** | **4,31** | **0,65** | **0,24** |

<!-- Estadísticas: 6 filas, 15 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 51: Resumen Emisiones Fase de Cierre** |Fase de Construcción|MP10|Col3|MP2,5|Col5|MPS|Col7|CO|Col9|HC|Col11|NOx|Col13|SO<br>X|Col15| |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---| -->
<!-- FIN TABLA 50 -->


Tabla 51: Resumen Emisiones Fase de Cierre ........................................................................................................................ 67

<!-- INICIO TABLA 51 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Maquinarias|1,17|0,43|1,17|0,43|1,17|0,43|0,62|0,23|0,28|0,10|1,38|0,50|---|---| |Vehículos|0,04|0,01|0,04|0,01|0,13|0,05|1,40|0,51|0,24|0,09|5,81|2,12|---|---| |Caldera|1,82|0,66|0,91|0,33|1,82|0,66|0,26|0,09|---|---|4,62|1,69|0,65|0,24| |**TOTAL**|**68,88**|**3,09**|**11,49**|**1,05**|**266,36**|**9,04**|**2,28**|**0,83**|**0,52**|**0,19**|**11,81**|**4,31**|**0,65**|**0,24**| -->

**Tabla 51: Resumen Emisiones Fase de Cierre****

| Fase de Construcción | MP10 | Col3 | MP2,5 | Col5 | MPS | Col7 | CO | Col9 | HC | Col11 | NOx | Col13 | SO<br>X | Col15 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Fase de Construcción** | **kg/día** | **ton/año** | **kg/día** | **ton/año** | **kg/día** | **ton/año** | **kg/día** | **ton/año** | **kg/día** | **ton/año** | **kg/día** | **ton/año** | **kg/día** | **ton/año** |
| Actividades | 15,18 | 1,65 | 1,80 | 0,21 | 52,41 | 6,19 | --- | --- | --- | --- | --- | --- | --- | --- |
| Maquinarias | 0,06 | 0,00 | 0,06 | 0,00 | 0,06 | 0,00 | 0,19 | 0,01 | 0,09 | 0,00 | 0,65 | 0,02 | --- | --- |
| Vehículos | 0,03 | 0,00 | 0,03 | 0,00 | 0,03 | 0,01 | 0,30 | 0,05 | 0,05 | 0,01 | 1,17 | 0,21 | --- | --- |
| Generadores | 0,39 | 0,07 | 0,39 | 0,07 | 0,39 | 0,07 | 1,17 | 0,21 | --- | --- | 5,41 | 0,97 | 0,36 | 0,06 |
| **TOTAL** | **15,66** | **1,73** | **2,28** | **0,29** | **52,89** | **6,27** | **1,66** | **0,27** | **0,14** | **0,01** | **7,23** | **1,20** | **0,36** | **0,06** |

<!-- Estadísticas: 6 filas, 15 columnas -->
<!-- Contexto posterior: -->
<!-- **BORDOLI & Consultores EIRL** Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 67 Antofagasta -->
<!-- FIN TABLA 51 -->


Tabla 52: Aportes del Proyecto Etapa de Construcción ........................................................................................................... 69

<!-- INICIO TABLA 52 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Informe de Emisiones Declaración de Impacto Ambiental Proyecto NAVÍO II -->

**Tabla 52: Aportes del Proyecto Etapa de Construcción****

| Parámetro | Estadístico | Limite<br>Norma<br>(μg/m3N) | Concentración<br>(μg/m3N)<br>Receptor R1 | %<br>Respecto<br>de la<br>Norma | Concentración<br>(μg/m3N)<br>Receptor R2 | %<br>Respecto<br>de la<br>Norma | Concentración<br>(μg/m3N)<br>Receptor R3 | %<br>Respecto<br>de la<br>Norma |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MP10 | Percentil 98 Promedio 24 horas | 150 | 1.3155E-02 | 0,0 | 1.4254E-01 | 0,1 | 5.7171E-02 | 0,0 |
| MP10 | Promedio Anual | 50 | 3.1842E-03 | 0,0 | 2.4825E-02 | 0,0 | 1.3341E-02 | 0,0 |
| MP2,5 | Percentil 98 Promedio Diario | 50 | 2.4289E-03 | 0,0 | 2.9371E-02 | 0,1 | 1.2303E-02 | 0,0 |
| MP2,5 | Promedio Trianual | 20 | 5.8081E-04 | 0,0 | 5.3983E-03 | 0,0 | 3.1806E-03 | 0,0 |
| CO | Percentil 99, máx. 1 hora | 30000 | 2.1765E-02 | 0,0 | 4.1358E-01 | 0,0 | 1.3078E-01 | 0,0 |
| CO | Percentil 99, máx. 8 hora | 10000 | 6.1757E-03 | 0,0 | 6.0662E-02 | 0,0 | 1.8508E-02 | 0,0 |
| NO2 | Percentil 99, máx. 1 hora | 400 | 6.3795E-03 | 0,0 | 1.2543E-01 | 0,0 | 4.5199E-02 | 0,0 |
| NO2 | Promedio, Anual | 100 | 2.2116E-04 | 0,0 | 6.2973E-04 | 0,0 | 1.7340E-04 | 0,0 |
| SO2 | Promedio Diario, percentil 99 | 250 | 4.9733E-04 | 0,0 | 4.3611E-03 | 0,0 | 1.9543E-03 | 0,0 |

<!-- Estadísticas: 9 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 53: Aportes del Proyecto Etapa de Operación** |Parámetro|Estadístico|Limite<br>Norma<br>(μg/m3N)|Concentración<br>(μg/m3N)<br>Receptor R1|%<br>Respecto<br>de la<br>Norma|Concentración<br>(μg/m3N)<br>Receptor R2|%<br>Respecto<br>de la<br>Norma|Concentración<br>(μg/m3N)<br>Receptor R3|%<br>Respecto<br>de la<br>Norma| |---|---|---|---|---|---|---|---|---| -->
<!-- FIN TABLA 52 -->


Tabla 53: Aportes del Proyecto Etapa de Operación ................................................................................................................ 69

<!-- INICIO TABLA 53 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |CO|Percentil 99, máx. 8 hora|10000|6.1757E-03|0,0|6.0662E-02|0,0|1.8508E-02|0,0| |NO2|Percentil 99, máx. 1 hora|400|6.3795E-03|0,0|1.2543E-01|0,0|4.5199E-02|0,0| |NO2|Promedio, Anual|100|2.2116E-04|0,0|6.2973E-04|0,0|1.7340E-04|0,0| |SO2|Promedio Diario, percentil 99|250|4.9733E-04|0,0|4.3611E-03|0,0|1.9543E-03|0,0| -->

**Tabla 53: Aportes del Proyecto Etapa de Operación****

| Parámetro | Estadístico | Limite<br>Norma<br>(μg/m3N) | Concentración<br>(μg/m3N)<br>Receptor R1 | %<br>Respecto<br>de la<br>Norma | Concentración<br>(μg/m3N)<br>Receptor R2 | %<br>Respecto<br>de la<br>Norma | Concentración<br>(μg/m3N)<br>Receptor R3 | %<br>Respecto<br>de la<br>Norma |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MP10 | Percentil 98 Promedio 24 horas | 150 | 9.0914E-03 | 0,0 | 4.7899E-01 | 0,3 | 2.7619E-01 | 0,2 |
| MP10 | Promedio Anual | 50 | 2.4207E-03 | 0,0 | 1.0734E-01 | 0,2 | 7.6398E-02 | 0,2 |
| MP2,5 | Percentil 98 Promedio Diario | 50 | 1.2288E-03 | 0,0 | 1.1392E-01 | 0,2 | 6.5819E-02 | 0,1 |
| MP2,5 | Promedio Trianual | 20 | 3.4733E-04 | 0,0 | 2.5146E-02 | 0,1 | 1.8298E-02 | 0,1 |
| CO | Percentil 99, máx. 1 hora | 30000 | 3.4157E-04 | 0,0 | 5.7060E-03 | 0,0 | 2.1247E-03 | 0,0 |
| CO | Percentil 99, máx. 8 hora | 10000 | 9.6569E-05 | 0,0 | 8.3185E-04 | 0,0 | 2.9792E-04 | 0,0 |
| NO2 | Percentil 99, máx. 1 hora | 400 | 5.2153E-04 | 0,0 | 1.1042E-02 | 0,0 | 3.5428E-03 | 0,0 |
| NO2 | Promedio, Anual | 100 | 1.8547E-05 | 0,0 | 5.8313E-05 | 0,0 | 1.4703E-05 | 0,0 |
| SO2 | Promedio Diario, percentil 99 | 250 | 9.1351E-06 | 0,0 | 8.0107E-05 | 0,0 | 3.5897E-05 | 0,0 |

<!-- Estadísticas: 9 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- **BORDOLI & Consultores EIRL** Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 69 Antofagasta -->
<!-- FIN TABLA 53 -->


Tabla 54: Aportes del Proyecto Etapa de Cierre ....................................................................................................................... 70

<!-- INICIO TABLA 54 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Informe de Emisiones Declaración de Impacto Ambiental Proyecto NAVÍO II -->

**Tabla 54: Aportes del Proyecto Etapa de Cierre****

| Parámetro | Estadístico | Limite<br>Norma<br>(μg/m3N) | Concentración<br>(μg/m3N)<br>Receptor R1 | %<br>Respecto<br>de la<br>Norma | Concentración<br>(μg/m3N)<br>Receptor R2 | %<br>Respecto<br>de la<br>Norma | Concentración<br>(μg/m3N)<br>Receptor R3 | %<br>Respecto<br>de la<br>Norma |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MP10 | Percentil 98 Promedio 24 horas | 150 | 3.8186E-03 | 0,0 | 4.8393E-02 | 0,0 | 1.8999E-02 | 0,0 |
| MP10 | Promedio Anual | 50 | 9.3101E-04 | 0,0 | 8.5522E-03 | 0,0 | 4.9495E-03 | 0,0 |
| MP2,5 | Percentil 98 Promedio Diario | 50 | 1.7551E-03 | 0,0 | 1.7081E-02 | 0,0 | 6.9109E-03 | 0,0 |
| MP2,5 | Promedio Trianual | 20 | 4.1729E-04 | 0,0 | 2.6432E-03 | 0,0 | 1.3706E-03 | 0,0 |
| CO | Percentil 99, máx. 1 hora | 30000 | 3.8580E-02 | 0,0 | 6.2226E-01 | 0,0 | 2.3259E-01 | 0,0 |
| CO | Percentil 99, máx. 8 hora | 10000 | 1.0944E-02 | 0,0 | 9.5579E-02 | 0,0 | 3.1790E-02 | 0,0 |
| NO2 | Percentil 99, máx. 1 hora | 400 | 4.5705E-05 | 0,0 | 8.4182E-03 | 0,0 | 2.9319E-04 | 0,1 |
| NO2 | Promedio, Anual | 100 | 1.5837E-06 | 0,0 | 4.4271E-06 | 0,0 | 1.2499E-06 | 0,0 |
| SO2 | Promedio Diario, percentil 99 | 250 | 4.9733E-04 | 0,0 | 4.3611E-03 | 0,0 | 1.9543E-03 | 0,0 |

<!-- Estadísticas: 9 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- **BORDOLI & Consultores EIRL** Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 70 Antofagasta -->
<!-- FIN TABLA 54 -->

Tabla 55: Aportes del Proyecto Etapa de Construcción ........................................................................................................... 71

<!-- INICIO TABLA 55 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Proyecto NAVÍO II **11.1.2 Cumplimiento Normas de Calidad Ambiental Secundaria** -->

**Tabla 55: Aportes del Proyecto Etapa de Construcción****

| Parámetro | Estadístico | Limite<br>Norma<br>(μg/m3N) | Concentración<br>(μg/m3N)<br>Receptor R1 | %<br>Respecto<br>de la<br>Norma | Concentración<br>(μg/m3N)<br>Receptor R2 | %<br>Respecto<br>de la<br>Norma | Concentración<br>(μg/m3N)<br>Receptor R3 | %<br>Respecto<br>de la<br>Norma |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MPS | Promedio Mensual | 150 | 3.6090E-06 | 0,0 | 2.0141E-05 | 0,0 | 1.0122E-05 | 0,0 |
| MPS | Promedio Anual | 50 | 7.6163E-07 | 0,0 | 5.6058E-06 | 0,0 | 3.0713E-06 | 0,0 |
| SO2 | Promedio Anual | 50 | 1.4248E-04 | 0,0 | 3.9239E-04 | 0,0 | 1.1823E-04 | 0,0 |
| SO2 | Percentil 99.7 Conc. Diaria | 20 | 4.9733E-04 | 0,0 | 4.3611E-03 | 0,0 | 1.9543E-03 | 0,0 |
| SO2 | Percentil 99.73 Conc. 1 hora | 30000 | 4.9733E-04 | 0,0 | 4.3611E-03 | 0,0 | 1.9543E-03 | 0,0 |

<!-- Estadísticas: 5 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 56: Aportes del Proyecto Etapa de Operación** |Parámetro|Estadístico|Limite<br>Norma<br>(μg/m3N)|Concentración<br>(μg/m3N)<br>Receptor R1|%<br>Respecto<br>de la<br>Norma|Concentración<br>(μg/m3N)<br>Receptor R2|%<br>Respecto<br>de la<br>Norma|Concentración<br>(μg/m3N)<br>Receptor R3|%<br>Respecto<br>de la<br>Norma| |---|---|---|---|---|---|---|---|---| -->
<!-- FIN TABLA 55 -->


Tabla 56: Aportes del Proyecto Etapa de Operación ................................................................................................................ 71

<!-- INICIO TABLA 56 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |MPS|Promedio Anual|50|7.6163E-07|0,0|5.6058E-06|0,0|3.0713E-06|0,0| |SO2|Promedio Anual|50|1.4248E-04|0,0|3.9239E-04|0,0|1.1823E-04|0,0| |SO2|Percentil 99.7 Conc. Diaria|20|4.9733E-04|0,0|4.3611E-03|0,0|1.9543E-03|0,0| |SO2|Percentil 99.73 Conc. 1 hora|30000|4.9733E-04|0,0|4.3611E-03|0,0|1.9543E-03|0,0| -->

**Tabla 56: Aportes del Proyecto Etapa de Operación****

| Parámetro | Estadístico | Limite<br>Norma<br>(μg/m3N) | Concentración<br>(μg/m3N)<br>Receptor R1 | %<br>Respecto<br>de la<br>Norma | Concentración<br>(μg/m3N)<br>Receptor R2 | %<br>Respecto<br>de la<br>Norma | Concentración<br>(μg/m3N)<br>Receptor R3 | %<br>Respecto<br>de la<br>Norma |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MPS | Promedio Mensual | 150 | 4.3922E-06 | 0,0 | 1.0331E-04 | 0,0 | 6.0299E-05 | 0,0 |
| MPS | Promedio Anual | 50 | 9.9611E-07 | 0,0 | 3.3152E-05 | 0,0 | 1.9603E-05 | 0,0 |
| SO2 | Promedio Anual | 50 | 2.6172E-06 | 0,0 | 7.2075E-06 | 0,0 | 2.1718E-06 | 0,0 |
| SO2 | Percentil 99.7 Conc. Diaria | 20 | 9.1351E-06 | 0,0 | 8.0107E-05 | 0,0 | 3.5897E-05 | 0,0 |
| SO2 | Percentil 99.73 Conc. 1 hora | 30000 | 9.1351E-06 | 0,0 | 8.0107E-05 | 0,0 | 3.5897E-05 | 0,0 |

<!-- Estadísticas: 5 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- **BORDOLI & Consultores EIRL** Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 71 Antofagasta -->
<!-- FIN TABLA 56 -->


Tabla 57: Aportes del Proyecto Etapa de Cierre ....................................................................................................................... 72

<!-- INICIO TABLA 57 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Informe de Emisiones Declaración de Impacto Ambiental Proyecto NAVÍO II -->

**Tabla 57: Aportes del Proyecto Etapa de Cierre****

| Parámetro | Estadístico | Limite<br>Norma<br>(μg/m3N) | Concentración<br>(μg/m3N)<br>Receptor R1 | %<br>Respecto<br>de la<br>Norma | Concentración<br>(μg/m3N)<br>Receptor R2 | %<br>Respecto<br>de la<br>Norma | Concentración<br>(μg/m3N)<br>Receptor R3 | %<br>Respecto<br>de la<br>Norma |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MPS | Promedio Mensual | 150 | 9.5607E-07 | 0,0 | 6.9136E-06 | 0,0 | 3.7460E-06 | 0,0 |
| MPS | Promedio Anual | 50 | 2.0358E-07 | 0,0 | 2.0600E-06 | 0,0 | 1.1654E-06 | 0,0 |
| SO2 | Promedio Anual | 50 | 1.4248E-04 | 0,0 | 3.9239E-04 | 0,0 | 1.1823E-04 | 0,0 |
| SO2 | Percentil 99.7 Conc. Diaria | 20 | 9.6468E-05 | 0,0 | 1.0409E-04 | 0,0 | 9.4402E-05 | 0,0 |
| SO2 | Percentil 99.73 Conc. 1 hora | 30000 | 4.9733E-04 | 0,0 | 4.3611E-03 | 0,0 | 1.9543E-03 | 0,0 |

<!-- Estadísticas: 5 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Nota 1: Tablas 55, 56 y 57 los aportes de MPS en cada uno de los receptores, se expresan en mg/m [2] día Nota 2: Tablas 55, 56 y 57 los aportes de SO 2 en cada uno de los receptores, se expresan en μg/m [3] N **BORDOLI & Consultores EIRL** -->
<!-- FIN TABLA 57 -->

Tabla 58: Velocidad promedio del Viento en m/s ...................................................................................................................... 74

<!-- INICIO TABLA 58 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Informe de Emisiones Declaración de Impacto Ambiental Proyecto NAVÍO II -->

**Tabla 58: Velocidad promedio del Viento en m/s****

| Estación | Promedio Observado | Promedio Pronostico WRF | % de Variación |
| --- | --- | --- | --- |
| Cerro Moreno | 3,6 | 2,5 |  |

<!-- Estadísticas: 1 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- _% Error_ _V_ = % de error entre los valores modelado y observado de la velocidad del viento. (Valor modelado) = 2,53 m/s -->
<!-- FIN TABLA 58 -->


Tabla 59: Aportes del Proyecto Etapa de Construcción ........................................................................................................... 75

<!-- INICIO TABLA 59 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Informe de Emisiones Declaración de Impacto Ambiental Proyecto NAVÍO II -->

**Tabla 59: Aportes del Proyecto Etapa de Construcción con aplicación de factor de corrección****

| Parámetro | Estadístico | Limite<br>Norma<br>(μg/m3N) | Concentración<br>(μg/m3N)<br>Receptor R1 | %<br>Respecto<br>de la<br>Norma | Concentración<br>(μg/m3N)<br>Receptor R2 | %<br>Respecto<br>de la<br>Norma | Concentración<br>(μg/m3N)<br>Receptor R3 | %<br>Respecto<br>de la<br>Norma |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MP10 | Percentil 98 Promedio 24 horas | 150 | 1,71E-02 | 0,0 | 1,85E-01 | 0,1 | 7,43E-02 | 0,0 |
| MP10 | Promedio Anual | 50 | 4,14E-03 | 0,0 | 3,23E-02 | 0,1 | 1,73E-02 | 0,0 |
| MP2,5 | Percentil 98 Promedio Diario | 50 | 3,16E-03 | 0,0 | 3,82E-02 | 0,1 | 1,60E-02 | 0,0 |
| MP2,5 | Promedio Trianual | 20 | 7,55E-04 | 0,0 | 7,01E-03 | 0,0 | 4,13E-03 | 0,0 |
| CO | Percentil 99, máx. 1 hora | 30000 | 2,83E-02 | 0,0 | 5,37E-01 | 0,0 | 1,70E-01 | 0,0 |
| CO | Percentil 99, máx. 8 hora | 10000 | 8,02E-03 | 0,0 | 7,88E-02 | 0,0 | 2,40E-02 | 0,0 |
| NO2 | Percentil 99, máx. 1 hora | 400 | 8,29E-03 | 0,0 | 1,63E-01 | 0,0 | 5,87E-02 | 0,0 |
| NO2 | Promedio, Anual | 100 | 2,87E-04 | 0,0 | 8,18E-04 | 0,0 | 2,25E-04 | 0,0 |
| SO2 | Promedio Diario, percentil 99 | 250 | 6,46E-04 | 0,0 | 5,67E-03 | 0,0 | 2,54E-03 | 0,0 |

<!-- Estadísticas: 9 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 60: Aportes del Proyecto Etapa de Operación con aplicación de factor de corrección** |Parámetro|Estadístico|Limite<br>Norma<br>(μg/m3N)|Concentración<br>(μg/m3N)<br>Receptor R1|%<br>Respecto<br>de la<br>Norma|Concentración<br>(μg/m3N)<br>Receptor R2|%<br>Respecto<br>de la<br>Norma|Concentración<br>(μg/m3N)<br>Receptor R3|%<br>Respecto<br>de la<br>Norma| |---|---|---|---|---|---|---|---|---| -->
<!-- FIN TABLA 59 -->


Tabla 60: Aportes del Proyecto Etapa de Operación ................................................................................................................ 75

<!-- INICIO TABLA 60 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |CO|Percentil 99, máx. 8 hora|10000|8,02E-03|0,0|7,88E-02|0,0|2,40E-02|0,0| |NO2|Percentil 99, máx. 1 hora|400|8,29E-03|0,0|1,63E-01|0,0|5,87E-02|0,0| |NO2|Promedio, Anual|100|2,87E-04|0,0|8,18E-04|0,0|2,25E-04|0,0| |SO2|Promedio Diario, percentil 99|250|6,46E-04|0,0|5,67E-03|0,0|2,54E-03|0,0| -->

**Tabla 60: Aportes del Proyecto Etapa de Operación con aplicación de factor de corrección****

| Parámetro | Estadístico | Limite<br>Norma<br>(μg/m3N) | Concentración<br>(μg/m3N)<br>Receptor R1 | %<br>Respecto<br>de la<br>Norma | Concentración<br>(μg/m3N)<br>Receptor R2 | %<br>Respecto<br>de la<br>Norma | Concentración<br>(μg/m3N)<br>Receptor R3 | %<br>Respecto<br>de la<br>Norma |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MP10 | Percentil 98 Promedio 24 horas | 150 | 1,18E-02 | 0,0 | 6,22E-01 | 0,4 | 3,59E-01 | 0,2 |
| MP10 | Promedio Anual | 50 | 3,14E-03 | 0,0 | 1,39E-01 | 0,3 | 9,93E-02 | 0,2 |
| MP2,5 | Percentil 98 Promedio Diario | 50 | 1,60E-03 | 0,0 | 1,48E-01 | 0,3 | 8,55E-02 | 0,2 |
| MP2,5 | Promedio Trianual | 20 | 4,51E-04 | 0,0 | 3,27E-02 | 0,2 | 2,38E-02 | 0,1 |
| CO | Percentil 99, máx. 1 hora | 30000 | 4,44E-04 | 0,0 | 7,41E-03 | 0,0 | 2,76E-03 | 0,0 |
| CO | Percentil 99, máx. 8 hora | 10000 | 1,25E-04 | 0,0 | 1,08E-03 | 0,0 | 3,87E-04 | 0,0 |
| NO2 | Percentil 99, máx. 1 hora | 400 | 6,78E-04 | 0,0 | 1,43E-02 | 0,0 | 4,60E-03 | 0,0 |
| NO2 | Promedio, Anual | 100 | 2,41E-05 | 0,0 | 7,58E-05 | 0,0 | 1,91E-05 | 0,0 |
| SO2 | Promedio Diario, percentil 99 | 250 | 1,19E-05 | 0,0 | 1,04E-04 | 0,0 | 4,66E-05 | 0,0 |

<!-- Estadísticas: 9 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- **BORDOLI & Consultores EIRL** Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 75 Antofagasta -->
<!-- FIN TABLA 60 -->

Tabla 61: Aportes del Proyecto Etapa de Cierre ....................................................................................................................... 76

<!-- INICIO TABLA 61 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Informe de Emisiones Declaración de Impacto Ambiental Proyecto NAVÍO II -->

**Tabla 61: Aportes del Proyecto Etapa de Cierre con aplicación de factor de corrección****

| Parámetro | Estadístico | Limite<br>Norma<br>(μg/m3N) | Concentración<br>(μg/m3N)<br>Receptor R1 | %<br>Respecto<br>de la<br>Norma | Concentración<br>(μg/m3N)<br>Receptor R2 | %<br>Respecto<br>de la<br>Norma | Concentración<br>(μg/m3N)<br>Receptor R3 | %<br>Respecto<br>de la<br>Norma |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MP10 | Percentil 98 Promedio 24 horas | 150 | 4,96E-03 | 0,0 | 6,29E-02 | 0,0 | 2,47E-02 | 0,0 |
| MP10 | Promedio Anual | 50 | 1,21E-03 | 0,0 | 1,11E-02 | 0,0 | 6,43E-03 | 0,0 |
| MP2,5 | Percentil 98 Promedio Diario | 50 | 2,28E-03 | 0,0 | 2,22E-02 | 0,0 | 8,98E-03 | 0,0 |
| MP2,5 | Promedio Trianual | 20 | 5,42E-04 | 0,0 | 3,43E-03 | 0,0 | 1,78E-03 | 0,0 |
| CO | Percentil 99, máx. 1 hora | 30000 | 5,01E-02 | 0,0 | 8,08E-01 | 0,0 | 3,02E-01 | 0,0 |
| CO | Percentil 99, máx. 8 hora | 10000 | 1,42E-02 | 0,0 | 1,24E-01 | 0,0 | 4,13E-02 | 0,0 |
| NO2 | Percentil 99, máx. 1 hora | 400 | 5,62E-05 | 0,0 | 1,03E-02 | 0,0 | 3,60E-04 | 0,0 |
| NO2 | Promedio, Anual | 100 | 1,95E-06 | 0,0 | 5,44E-06 | 0,0 | 1,54E-06 | 0,0 |
| SO2 | Promedio Diario, percentil 99 | 250 | 6,46E-04 | 0,0 | 5,67E-03 | 0,0 | 2,54E-03 | 0,0 |

<!-- Estadísticas: 9 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 62: Aportes del Proyecto Etapa de Construcción con aplicación de factor de corrección** |Parámetro|Estadístico|Limite<br>Norma<br>(μg/m3N)|Concentración<br>(μg/m3N)<br>Receptor R1|%<br>Respecto<br>de la<br>Norma|Concentración<br>(μg/m3N)<br>Receptor R2|%<br>Respecto<br>de la<br>Norma|Concentración<br>(μg/m3N)<br>Receptor R3|%<br>Respecto<br>de la<br>Norma| |---|---|---|---|---|---|---|---|---| -->
<!-- FIN TABLA 61 -->


Tabla 62: Aportes del Proyecto Etapa de Construcción con aplicación de factor de corrección .............................................. 76

<!-- INICIO TABLA 62 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |CO|Percentil 99, máx. 8 hora|10000|1,42E-02|0,0|1,24E-01|0,0|4,13E-02|0,0| |NO2|Percentil 99, máx. 1 hora|400|5,62E-05|0,0|1,03E-02|0,0|3,60E-04|0,0| |NO2|Promedio, Anual|100|1,95E-06|0,0|5,44E-06|0,0|1,54E-06|0,0| |SO2|Promedio Diario, percentil 99|250|6,46E-04|0,0|5,67E-03|0,0|2,54E-03|0,0| -->

**Tabla 62: Aportes del Proyecto Etapa de Construcción con aplicación de factor de corrección****

| Parámetro | Estadístico | Limite<br>Norma<br>(μg/m3N) | Concentración<br>(μg/m3N)<br>Receptor R1 | %<br>Respecto<br>de la<br>Norma | Concentración<br>(μg/m3N)<br>Receptor R2 | %<br>Respecto<br>de la<br>Norma | Concentración<br>(μg/m3N)<br>Receptor R3 | %<br>Respecto<br>de la<br>Norma |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MPS | Promedio Mensual | 150 | 4,69E-06 | 0,0 | 2,62E-05 | 0,0 | 1,32E-05 | 0,0 |
| MPS | Promedio Anual | 50 | 9,90E-07 | 0,0 | 7,28E-06 | 0,0 | 3,99E-06 | 0,0 |
| SO2 | Promedio Anual | 50 | 1,85E-04 | 0,0 | 5,10E-04 | 0,0 | 1,54E-04 | 0,0 |
| SO2 | Percentil 99.7 Conc. Diaria | 20 | 6,46E-04 | 0,0 | 5,67E-03 | 0,0 | 2,54E-03 | 0,0 |
| SO2 | Percentil 99.73 Conc. 1 hora | 30000 | 6,46E-04 | 0,0 | 5,67E-03 | 0,0 | 2,54E-03 | 0,0 |

<!-- Estadísticas: 5 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- **BORDOLI & Consultores EIRL** Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 76 Antofagasta -->
<!-- FIN TABLA 62 -->


Tabla 63 Aportes del Proyecto Etapa de Operación con aplicación de factor de corrección ................................................... 77
Tabla 64 Aportes del Proyecto Etapa de Cierre con aplicación de factor de corrección .......................................................... 77

Tabla 65: Puntos de Máximo Impacto - Fase de Construcción ................................................................................................ 79

<!-- INICIO TABLA 65 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **13.7 Puntos de Máximo Impacto** De acuerdo con los resultados de la modelación, los puntos de máximo impacto generados por el proyecto, en cada una de sus fases, se presentan en las siguientes tablas, indicando ubicación en coordenadas UTM WGS84 Huso 19S y concentración máxima: -->

**Tabla 65: Puntos de Máximo Impacto - Fase de Construcción****

| Parámetro | Estadístico | Coordenada WGS-84 | Col4 | Concentración<br>(μg/m3N) |
| --- | --- | --- | --- | --- |
| **Parámetro** | **Estadístico** | **Este** | **Norte** | **Norte** |
| MP10 | Percentil 98 Promedio 24 horas | 359.500 | 7.414.375 | 56,31 |
| MP10 | Promedio Anual | 359.500 | 7.414.375 | 25,2 |
| MP2,5 | Percentil 98 Promedio Diario | 359.500 | 7.414.375 | 14,92 |
| MP2,5 | Promedio Trianual | 359.500 | 7.414.375 | 4,38 |
| CO | Percentil 99, máx. 1 hora | 359.500 | 7.414.375 | 314,22 |
| CO | Percentil 99, máx. 8 hora | 359.500 | 7.414.375 | 89,88 |
| NO2 | Percentil 99, máx. 1 hora | 359.500 | 7.414.375 | 220,16 |
| NO2 | Promedio, Anual | 359.500 | 7.414.375 | 1,06 |
| SO2 | Percentil 99.73 Concentración 1 hora | 359.500 | 7.414.375 | 95,4 |
| SO2 | Promedio Diario, percentil 99 | 359.500 | 7.414.375 | 9,16 |
| SO2 | Promedio, Anual | 359.500 | 7.414.375 | 0,9 |

<!-- Estadísticas: 12 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- **BORDOLI & Consultores EIRL** Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 79 Antofagasta -->
<!-- FIN TABLA 65 -->


Tabla 66: Puntos de Máximo Impacto - Fase de Operación ..................................................................................................... 80

<!-- INICIO TABLA 66 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **BORDOLI & Consultores EIRL** Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 79 Antofagasta -->

**Tabla 66: Puntos de Máximo Impacto - Fase de Operación****

| Parámetro | Estadístico | Coordenada WGS-84 | Col4 | Concentración<br>(μg/m3N) |
| --- | --- | --- | --- | --- |
| **Parámetro** | **Estadístico** | **Este** | **Norte** | **Norte** |
| MP10 | Percentil 98 Promedio 24 horas | 359.500 | 7.414.375 | 16,82 |
| MP10 | Promedio Anual | 358.500 | 7.414.375 | 3,23 |
| MP2,5 | Percentil 98 Promedio Diario | 359.500 | 7.414.375 | 1,69 |
| MP2,5 | Promedio Trianual | 358.500 | 7.414.375 | 0,32 |
| CO | Percentil 99, máx. 1 hora | 359.500 | 7.414.375 | 3,08 |
| CO | Percentil 99, máx. 8 hora | 359.500 | 7.414.375 | 0,9 |
| NO2 | Percentil 99, máx. 1 hora | 359.500 | 7.414.375 | 1,03 |
| NO2 | Promedio, Anual | 359.500 | 7.414.375 | 0,04 |
| SO2 | Percentil 99.73 Concentración 1 hora | 359.500 | 7.414.375 | 1,75 |
| SO2 | Promedio Diario, percentil 99 | 359.500 | 7.414.375 | 0,17 |
| SO2 | Promedio, Anual | 359.500 | 7.414.375 | 0,02 |

<!-- Estadísticas: 12 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 67: Puntos de Máximo Impacto - Fase de Cierre** |Parámetro|Estadístico|Coordenada WGS-84|Col4|Concentración<br>(μg/m3N)| |---|---|---|---|---| -->
<!-- FIN TABLA 66 -->


Tabla 67: Puntos de Máximo Impacto - Fase de Cierre ............................................................................................................ 80

<!-- INICIO TABLA 67 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |NO2|Promedio, Anual|359.500|7.414.375|0,04| |SO2|Percentil 99.73 Concentración 1 hora|359.500|7.414.375|1,75| |SO2|Promedio Diario, percentil 99|359.500|7.414.375|0,17| |SO2|Promedio, Anual|359.500|7.414.375|0,02| -->

**Tabla 67: Puntos de Máximo Impacto - Fase de Cierre****

| Parámetro | Estadístico | Coordenada WGS-84 | Col4 | Concentración<br>(μg/m3N) |
| --- | --- | --- | --- | --- |
| **Parámetro** | **Estadístico** | Este | Norte | Norte |
| MP10 | Percentil 98 Promedio 24 horas | 359.500 | 7.414.375 | 25,04 |
| MP10 | Promedio Anual | 359.500 | 7.414.375 | 3,69 |
| MP2,5 | Percentil 98 Promedio Diario | 359.500 | 7.414.375 | 19,36 |
| MP2,5 | Promedio Trianual | 359.500 | 7.414.375 | 2,75 |
| CO | Percentil 99, máx. 1 hora | 359.500 | 7.414.375 | 418,69 |
| CO | Percentil 99, máx. 8 hora | 359.500 | 7.414.375 | 141,88 |
| NO2 | Percentil 99, máx. 1 hora | 359.500 | 7.414.375 | 675,14 |
| NO2 | Promedio, Anual | 359.500 | 7.414.375 | 16,77 |
| SO2 | Percentil 99.73 Concentración 1 hora | 359.500 | 7.414.375 | 95,4 |
| SO2 | Promedio Diario, percentil 99 | 359.500 | 7.414.375 | 9,16 |
| SO2 | Promedio, Anual | 359.500 | 7.414.375 | 0,9 |

<!-- Estadísticas: 12 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- **14.** **CONCLUSIONES** Los resultados obtenidos de la modelación realizada y el análisis efectuado en los apartados anteriores, indican que el proyecto, en general, no presenta impactos en la calidad del aire en ninguno de los receptores analizados, -->
<!-- FIN TABLA 67 -->


**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 4
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**INDICE DE FIGURAS**

Figura 1: Rosa de Vientos ......................................................................................................................................................... 14
Figura 2: Campo de vientos a las 00:00 h ................................................................................................................................ 15

Figura 3: Campo de vientos a las 02:00 h ................................................................................................................................ 16

Figura 4: Campo de vientos a las 04:00 h ................................................................................................................................ 17
Figura 5: Campo de vientos a las 06:00 h ................................................................................................................................ 18

Figura 6: Campo de vientos a las 08:00 h ................................................................................................................................ 19

Figura 7: Campo de vientos a las 10:00 h ................................................................................................................................ 20
Figura 8: Campo de vientos a las 12:00 h ................................................................................................................................ 21

Figura 9: Campo de vientos a las 14:00 h ................................................................................................................................ 22

Figura 10: Campo de vientos a las 16:00 h .............................................................................................................................. 23
Figura 11: Campo de vientos a las 18:00 h .............................................................................................................................. 24

Figura 12: Campo de vientos a las 20:00 h .............................................................................................................................. 25

Figura 13: Campo de vientos a las 22:00 h .............................................................................................................................. 26

Figura 14: Ubicación Estación Meteorológica ........................................................................................................................... 27

Figura 15: Serie de tiempo registros horarios de velocidad del viento - Estación Cerro Moreno ............................................. 27

Figura 16: Serie de tiempo registros horarios de Dirección del viento - Estación Cerro Moreno.............................................. 27
Figura 17: Rosa de Viento Estación Cerro Moreno v/s Rosa de Viento modelada con WRF. ................................................. 30

Figura 18: División Político-Administrativa ................................................................................................................................ 33
Figura 19: Área de Modelamiento ............................................................................................................................................. 34
Figura 20: Grilla Meteorológica de Modelamiento .................................................................................................................... 35
Figura 21: Topografía del Área de Modelación ......................................................................................................................... 36

Figura 22: Emplazamiento de Puntos Receptores Sensibles ................................................................................................... 37
Figura 23: Emplazamiento de Puntos Receptores Sensibles ................................................................................................... 38

Figura 24: Mapa de Isoconcentración Material Particulado MP10 - Etapa de Construcción (24 h) .......................................... 82

Figura 25: Mapa de Isoconcentración Material Particulado MP10 - Etapa de Construcción (Anual) ....................................... 83
Figura 26: Mapa de Isoconcentración Material Particulado MP2.5 - Etapa de Construcción (24 h) ......................................... 84

Figura 27: Mapa de Isoconcentración Material Particulado MP2.5 - Etapa de Construcción (Anual) ...................................... 85

Figura 28: Mapa de Isodepositación Material Particulado Sedimentable MPS - Etapa de Construcción (24h) ....................... 86
Figura 29: Mapa de Isodepositación Material Particulado Sedimentable MPS - Etapa de Construcción (Anual) .................... 87

Figura 30: Mapa de Isoconcentración Gases CO - Etapa de Construcción (1h) ...................................................................... 88

Figura 31: Mapa de Isoconcentración Gases CO - Etapa de Construcción (8h) ...................................................................... 89
Figura 32: Mapa de Isoconcentración Gases NO2 - Etapa de Construcción (1 h) ................................................................... 90

Figura 33: Mapa de Isoconcentración Gases NO2 - Etapa de Construcción (Anual) ............................................................... 91

Figura 34: Mapa de Isoconcentración Gases SO2 - Etapa de Construcción (1h) .................................................................... 92
Figura 35: Mapa de Isoconcentración Gases SO2 - Etapa de Construcción (24h) ................................................................. 93

Figura 36: Mapa de Isoconcentración Gases SO2 - Etapa de Construcción (Anual) ............................................................... 94

Figura 37: Mapa de Isoconcentración Material Particulado MP10 - Etapa de Operación (24 h) .............................................. 95
Figura 38: Mapa de Isoconcentración Material Particulado MP10 - Etapa de Operación (Anual) ............................................ 96

Figura 39: Mapa de Isoconcentración Material Particulado MP2.5 - Etapa de Operación (24 h) ............................................. 97

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 5
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

Figura 40: Mapa de Isoconcentración Material Particulado MP2.5 - Etapa de Operación (Anual) ........................................... 98

Figura 41: Mapa de Isodepositación Material Particulado Sedimentable MPS - Etapa de Operación (24h) ............................ 99
Figura 42: Mapa de Isodepositación Material Particulado Sedimentable MPS - Etapa de Operación (Anual) ....................... 100

Figura 43: Mapa de Isoconcentración Gases CO - Etapa de Operación (1h) ........................................................................ 101

Figura 44: Mapa de Isoconcentración Gases CO - Etapa de Operación (8h) ........................................................................ 102
Figura 45: Mapa de Isoconcentración Gases NO2 - Etapa de Operación (1 h) ..................................................................... 103

Figura 46: Mapa de Isoconcentración Gases NO2 - Etapa de Operación (Anual) ................................................................. 104

Figura 47: Mapa de Isoconcentración Gases SO2 - Etapa de Operación (1h) ....................................................................... 105
Figura 48: Mapa de Isoconcentración Gases SO2 - Etapa de Operación (24h) ..................................................................... 106

Figura 49: Mapa de Isoconcentración Gases SO2 - Etapa de Operación (Anual) ................................................................. 107

Figura 50: Mapa de Isoconcentración Material Particulado MP10 - Etapa de Cierre (24 h) ................................................... 108
Figura 51: Mapa de Isoconcentración Material Particulado MP10 - Etapa de Cierre (Anual) ................................................. 109

Figura 52: Mapa de Isoconcentración Material Particulado MP2.5 - Etapa de Cierre (24 h) .................................................. 110

Figura 53: Mapa de Isoconcentración Material Particulado MP2.5 - Etapa de Cierre (Anual) ................................................ 111
Figura 54: Mapa de Isodepositación Material Particulado Sedimentable MPS - Etapa de Cierre (24h) ................................. 112

Figura 55: Mapa de Isodepositación Material Particulado Sedimentable MPS - Etapa de Cierre (Anual) ............................. 113

Figura 56: Mapa de Isoconcentración Gases CO - Etapa de Cierre (1h) ............................................................................... 114
Figura 57: Mapa de Isoconcentración Gases CO - Etapa de Cierre (8h) ............................................................................... 115

Figura 58: Mapa de Isoconcentración Gases NO2 - Etapa de Cierre (1 h) ............................................................................ 116

Figura 59: Mapa de Isoconcentración Gases NO2 - Etapa de Cierre (Anual) ........................................................................ 117
Figura 60: Mapa de Isoconcentración Gases SO2 - Etapa de Cierre (1h) ............................................................................. 118

Figura 61: Mapa de Isoconcentración Gases SO2 - Etapa de Cierre (24h) ........................................................................... 119

Figura 62: Mapa de Isoconcentración Gases SO2 - Etapa de Cierre (Anual) ........................................................................ 120

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 6
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**1.** **INTRODUCCIÓN**

En este documento se presenta el inventario de emisiones de material particulado y los resultados obtenidos de
la modelación atmosférica de dispersión de contaminantes generados durante las distintas fases del Proyecto
“NAVÍO II” de EXSA Chile SpA. Estas emisiones corresponden específicamente a material particulado respirable
(MP 10 y MP 2.5 ), gases (CO, HC, NOx, SOx), y material particulado sedimentable (MPS), las cuales son
generadas por las actividades de escarpe, excavaciones, carguío y transporte, tránsito de vehículos por caminos
pavimentados, tránsito de vehículos livianos y vehículos pesados por caminos no pavimentados, y utilización de
maquinarias, equipos, vehículos y generadores eléctricos.

El proyecto “NAVÍO II”, en adelante el “Proyecto”, consiste en la construcción de una planta para la fabricación
de emulsión matriz (agente oxidante) de clasificación 5.1 (sustancia comburente) y una planta de fabricación de
agente de voladura ANFO de clasificación 1.5 (explosivo insensible que tienen riesgo de explosión de toda la
masa), ambas clasificaciones de acuerdo a la NCh 382 of 2004.

La Emulsión Matriz es la materia prima que se utiliza para la fabricación de agentes de voladura, se clasifica
como un producto oxidante que no contiene materia explosiva alguna en su composición. Básicamente una
emulsión, es un sistema que contiene dos fases liquidas inmiscibles entre sí, en la cual una de las fases se
dispersa como pequeñas gotas dentro de la otra. La emulsión Matriz se forma al mezclar una solución acuosa en
base a sales oxidantes, con una solución combustible que contiene petróleo diésel, aceites minerales y
emulsificantes para mejorar la estabilidad de la mezcla de aquellas dos soluciones inmiscibles.

El ANFO es un agente de voladura granular seco, que se compone de nitrato de amonio granulado y petróleo
diésel. EL ANFO requiere de un cebo energético para detonar (un cebo es un explosivo que se inicia desde un
detonador o cordón detonante).

Las principales materias primas que se utilizan en la fabricación de ambos compuestos son el nitrato de amonio
y combustible diésel. El Nitrato de Amonio será almacenado en maxi bags de 1,0 a 1,3 toneladas, en canchas
especialmente habilitadas para esta labor y en total cumplimiento de las normas establecidas por la legislación
vigente. El combustible Diésel será almacenado en estanques dentro de las instalaciones, el cual se conectará
con las unidades de fabricación mediante un sistema de cañerías rígidas.

Adicionalmente a la planta de fabricación y canchas de almacenamiento de nitrato de amonio, se considera la
construcción de ocho polvorines de los cuales, siete polvorines serán para almacenamiento de productos tales
como dinamitas, emulsiones encartuchadas, booster de pentolitas y un polvorín para almacenamiento de
sistemas de iniciación (detonadores) y la construcción de talleres, caldera, instalaciones administrativas,
bodegas, tanques de petróleo diésel, tanque de agua, un comedor, sistema de distribución de agua potable y
alcantarillado, red de suministro eléctrico e iluminación, sistemas de protección tormentas y descargas eléctricas,

red contra incendio entre otros.

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 7
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

En resumen, el proyecto considera as siguientes instalaciones:

a) Una planta de emulsión matriz con una capacidad de fabricación de 7.000 ton/mes
b) Una planta de fabricación de ANFO con capacidad de fabricación de 300 ton/mes.
c) Una caldera y sistema de aire comprimido
d) Una planta de tratamiento de agua de lavado (lavado camiones)
e) Una unidad de mantenimiento de camiones
f) Cuatro polvorines con capacidad para 23 toneladas c/u
g) Dos polvorines con capacidad para 22 toneladas c/u
h) Un polvorín con capacidad para 14 toneladas
i) Un polvorín con capacidad para 3.000 kg (iniciadores)
j) Siete canchas de almacenamiento de nitrato de amonio
k) Una unidad de control de acceso y vigilancia
l) Un área de control de pesaje y romana camiones
m) Tres bodega de almacenamiento de productos químicos
n) Una bodega de almacenamiento de residuos peligrosos
o) Un taller planta y bodega de insumos de operación
p) Una caseta área nitrato
q) Un baño químico (área polvorines)

El proyecto contempla además, obras anexas, tales como instalaciones administrativas, una bodega de
materiales generales, un comedor, sistema de agua potable y alcantarillado, red de suministro eléctrico e
iluminación, sistemas de protección tormentas y descargas eléctricas, red contra incendio entre otros.

El proyecto “NAVÍO II” se ubica en la Región y Provincia de Antofagasta, Comuna de Antofagasta.

Para realizar la estimación de las emisiones atmosféricas asociadas al proyecto, se utilizaron los siguientes
documentos de referencia: “Recopilación y Sistematización de Factores de Emisión al Aire, mayo 2015”,
publicado en la página web del SEA”, la Guía para la Estimación de Emisiones Atmosféricas de Proyectos
Inmobiliarios para la Región Metropolitana del Ministerio del Medio Ambiente (2012), la Guía Metodológica para
la Estimación de Emisiones Atmosféricas de Fuentes Fijas y Móviles en el Registro de Emisiones y
Transferencia de Contaminantes (Conama, 2009), Factores de Emisión Recomendados por la Environmental
Protection Agency (US EPA) en sus Documentos AP-42 (Fifth Edition, Compilation of Air Pollutant Emission
Factors) y la Guía para el Uso de Modelos de Calidad del Aire en el SEIA (2012).

Los resultados de la modelación atmosférica, se han analizado tomando en consideración los límites máximos

permisibles establecidos en las normas primarias y secundarias de calidad del aire establecido en la legislación
chilena, los cuales se presentan en la tabla 1 siguiente:

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 8
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

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
|CO|Percentil 99,máx.8 horas12|10.000 (μg/m3N)|NP DS 115/2002|
|CO|Percentil 99, máx. 1 hora13|30.000 (μg/m3N)|NP DS 115/2002|

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
12 Percentil 99: se refiere al promedio aritmético de tres años sucesivos, del percentil 99 de los máximos diarios

de concentración de 8 horas registrados durante un año calendario. Se considera sobrepasada la norma con
un valor igual o superior indicado en la tabla.
13 Percentil 99: se refiere al promedio aritmético de tres años sucesivos, del percentil 99 de los máximos diarios

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 9
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**2.** **DESCRIPCIÓN Y JUSTIFICACIÓN DEL MODELO**

Cualquier modelo que se ocupe para los fines que persigue el SEIA debe cumplir con las siguientes

características:

- Disponer de documentación completa que describa sus fundamentos conceptuales, ecuaciones matemáticas,

y los tipos de datos de entrada y de salida junto con sus respectivos formatos;

- Estar escrito en un lenguaje de programación común y con un código abierto;

- Ser de uso libre;

- Disponer de documentación sobre su evaluación, en forma de informes técnicos, publicaciones científicas o

equivalente; y

- Contar con desarrollo y soporte técnico actualizado de parte de su comunidad de usuarios o desarrolladores.

Los modelos recomendados en la “Guía para el Uso de Modelos de Calidad del Aire en el SEIA”, elaborada por
el Servicio de Evaluación Ambiental (SEA), cumplen con los requisitos anteriores.

El modelo recomendado en la guía citada, para contaminantes primarios, en dominio de modelación de menos
de 5 km, es el AERMOD, ya que a esta escala, se puede suponer una meteorología homogénea. Por lo tanto es
aceptable utilizar un modelo Gaussiano para modelar contaminantes primarios. Dado que la información
meteorológica de entrada en este caso debe ser de carácter observacional, los 5 km deben considerarse desde
la estación meteorológica (no la fuente emisora).

En el caso de que alguno de los bordes del dominio espacial de modelación esté a más de 5 km de la fuente de
emisión, lo más adecuado es utilizar un modelo que permita simular meteorología heterogénea. Los modelos
capaces de esto son los de tipo “puff” o Eulerianos. El modelo tipo “puff” recomendado es el modelo CALPUFF;
en el caso de modelos Eulerianos, se recomiendan los modelos WRF-Chem, CAMx y CMAQ

En todos los casos, también se debe analizar si existen factores que podrían perturbar el carácter lineal de los
campos de viento dentro del dominio, situación en que debe utilizarse un modelo como el descrito en el párrafo
anterior, incluso si se verifica la distancia máxima de 5 km desde la estación.

Debido a que no se cuenta con una estación de monitoreo meteorológico de superficie para obtener datos
observados a menos de 5 km de las fuentes emisoras, será necesario crear un dominio de modelación mayor,
por lo tanto, en el presente estudio, se utilizará el modelo de dispersión de contaminantes CALPUFF. Este
modelo creado por científicos del ASG (Grupo de Estudios Atmosféricos de TRC Solutions), corresponde a un
avanzado sistema de modelación meteorológica y de calidad del aire.

Este modelo ha sido adoptado por la Agencia de Protección Medioambiental de los Estados Unidos (EPA por

de concentración de 1 hora registrados durante un año calendario. Se considera sobrepasada la norma con un
valor igual o superior indicado en la tabla.

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 10
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

sus siglas en inglés) en su Guía para Modelos de Calidad del Aire como el preferido para la evaluación de
transporte de contaminantes a gran escala y como una base caso a caso para determinadas aplicaciones que
involucran condiciones meteorológicas complejas.

Este modelo (CALPUFF) está formado principalmente por tres componentes y un set de programas de pre- y
post-procesamiento. Estos componentes son:

CALMET: modelo meteorológico que desarrolla campos horarios de viento y temperatura en un dominio de
modelación de grilla tridimensional. Contiene además parametrizaciones de flujos de laderas, efectos
cinemáticos y de bloqueo del terreno, un procedimiento de minimización de divergencia y un modelo
micrometeorológico para capas límites sobre tierra y agua. En el archivo producido por CALMET están también
incluidos campos bidimensionales asociados como altura de mezcla, características de la superficie y
propiedades de dispersión.

CALPUFF: modelo de transporte y dispersión lagrangiano, gaussiano, no estacionario, que contiene módulos
para efectos de terreno complejo, transporte sobre agua, deposiciones secas y húmedas y transformaciones
químicas simples. El modelo advecta "puffs" o bocanadas de material emitido desde fuentes modeladas,
simulando procesos de dispersión y transformación en el camino. Típicamente usa los campos generados por
CALMET, o como opción puede usar datos meteorológicos más simples no grillados muy similares a modelos de
plumas existentes. En la distribución resultante de "puffs", a lo largo del período simulado, incorpora
explícitamente variaciones temporales y espaciales en los campos meteorológicos seleccionados. Los archivos
de salida primarios de CALPUFF contienen concentraciones o flujos de deposiciones horarias evaluadas en
lugares seleccionados de recepción.

CALPOST: procesador de los archivos de CALPUFF, produciendo tablas que resumen los resultados de la
simulación, identificando por ejemplo las concentraciones máximas promedios de tres horas y las segundas más
altas en cada receptor. Cuando se realizan modelaciones relacionadas a visibilidad, CALPOST usa
concentraciones de CALPUFF para calcular coeficientes de extinción y mediciones relacionadas a visibilidad,
reportándolas para los tiempos promediados y lugares seleccionados.

Cada uno de estos programas tiene una interfaz gráfica, existiendo además otros numerosos procesadores que
pueden ser utilizados para preparar datos geofísicos (como el terreno y uso de suelo), meteorológicos (como
precipitación o datos provenientes de boyas), o interfaces a otros modelos como el MM5, WRF, modelos RUC o

RAMS.

Para seleccionar el modelo adecuado, se consideraron los criterios establecidos en la Guía para el Uso de
Modelos de Calidad del Aire en el SEIA, (apartado 4.2, modelos recomendados, pág. 17). CALPUFF, resulto ser
el más adecuado, considerando que los datos disponibles para establecer el dominio espacial de la modelación,

se sitúan a más de 5 km de la fuente de emisión.

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 11
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**3.** **ESCENARIO METEOROLÓGICO**

El escenario meteorológico utilizado para la modelación, fue obtenido a través del modelo meteorológico de
pronostico Weather Research and Forecasting Model (WRF), adquiridos a la empresa Lakes Environmental, con
un domino de 100 km por 100 km, una resolución de 4 km y el periodo de data año 2015.

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 12
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Tabla 2: Información de la Orden de los Datos WRF**

Order #: MET168453

Company: B&CA Asesorías Ambientales
Data Type: CALMET-Ready WRF Data (3D.DAT Format)

Resolution: 4 km

Domain: 100x100 km

Period: Jan 01, 2015 hour 00 - Dec 31, 2015 hour 23

Latitude: 23.375814 S

Longitude: 70.165503 W

Datum: WGS 84

UMT Zone: -19

Site Time Zone: UTC - 4

Closest City: Mejillones, Baquedano, Antofagasta
Country: Chile

WRF es uno de los modelos meteorológicos de pronóstico más avanzados y completos y es mantenido por
NCAR9/ NOAA10 de Estados Unidos. Además, se ha ocupado en la mayoría de los proyectos relacionados con
modelación atmosférica encargados por organismos estatales, como la ex-CONAMA y la Comisión Nacional de
Energía (CNE) en los últimos años.

Campos de viento

Respecto a la dirección del viento, se puede apreciar que la dirección de viento predominante es SWW, con una
velocidad que fluctúa principalmente entre 1 y 6 m/s, con un porcentaje de calma de 2,40 %.

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 13
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 1: Rosa de Vientos**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 14
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 2: Campo de vientos a las 00:00 h**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 15
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 3: Campo de vientos a las 02:00 h**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 16
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 4: Campo de vientos a las 04:00 h**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 17
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 5: Campo de vientos a las 06:00 h**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 18
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 6: Campo de vientos a las 08:00 h**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 19
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 7: Campo de vientos a las 10:00 h**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 20
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 8: Campo de vientos a las 12:00 h**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 21
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 9: Campo de vientos a las 14:00 h**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 22
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 10: Campo de vientos a las 16:00 h**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 23
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 11: Campo de vientos a las 18:00 h**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 24
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 12: Campo de vientos a las 20:00 h**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 25
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 13: Campo de vientos a las 22:00 h**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 26
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**3.1 Datos observados**

Los datos de meteorología de superficie observados, provienen de la Estación Cerro Moreno, localizada
aproximadamente a 10 km en dirección Suroeste respecto al área del proyecto.

**Figura 14: Ubicación Estación Meteorológica**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 27
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Tabla 3: Información General de la Estación Meteorológica**

Código : SCFA
Región : Antofagasta
Provincia : Antofagasta
Comuna : Antofagasta

Coordenadas UTM : 353.572 E - 7.407.781 N

Huso horario : 19S

La estación “Estación Cerro Moreno” se encuentra dentro del área de modelación que se presenta en la figura

14.

Se ha considerado en el presente análisis la información disponible registrada en la Estación de Cerro Moreno,
entre el 1° de enero de 2015 al 31 de diciembre de 2015, la que será comparada con la información utilizada
para el modelamiento y que corresponde al modelo meteorológicos de pronóstico WRF (correspondiente al
mismo período)

**3.2 Series de tiempo.**

Las estadísticas de datos válidos monitoreado en la Estación Cerro Moreno, es la siguiente:

 - Datos totales: 8.760

 - Datos disponibles: 8.311

 - % datos válidos: 94,8 %

 - % de Calma: 2,96 %

Las series de tiempo presentadas a continuación para las variables de dirección y velocidad del viento, permiten
un análisis cualitativo de los datos en términos de completitud de la serie. En estas se puede observar la
variabilidad, amplitud de rango y frecuencia de los datos con que se cuenta.

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 28
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 15: Serie de tiempo registros horarios de velocidad del viento - Estación Cerro Moreno, periodo 01.01.15 al**

**31-12-15**

**Figura 16: Serie de tiempo registros horarios de Dirección del viento - Estación Cerro Moreno, periodo 01.01.15 al**

**31-12-15**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 29
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

En las series de tiempo de la Estación Cerro Moreno, se aprecia densidad de registros, mostrando regularidad
en la concentración de puntos para ambos gráficos (dirección y velocidad), se aprecia un leve descenso de las
velocidades entre los meses de abril a agosto. En el caso de la direcciones de los vientos se aprecia que
predominan los vientos de la dirección Suroeste.

**3.3 Campos de viento**

La figura 17, muestran la Rosa de Viento generada con los datos observados de la Estación Cerro Moreno
durante el periodo (01.01.2015al 31.12 2015) y la Rosa de Viento generada con el modelo de pronostico WRF
durante el mismo período, en el mismo punto de localización de la Estación Cerro Moreno.

**Figura 17: Rosa de Viento Estación Cerro Moreno v/s Rosa de Viento modelada con WRF.**

En la Rosa obtenida en base a las mediciones meteorológicas de la Estación Cerro Moreno, se observa que la
dirección predominante de los vientos es (SW) con intensidades de los vientos de moderadas a intensas. Puede
apreciarse que el modelo de pronostico WRF representa con bastante exactitud la condición de los vientos, tanto

en dirección como en velocidad.

**3.4 Calidad del aire en Antofagasta**

La información sobre Calidad de Aire en Antofagasta, corresponde a la registrada en la Estación de monitoreo
Antofagasta, ubicada en las coordenadas 358.874 E 7.387.875 N, correspondiente al período 2013 al 2015.

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 30
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

A continuación se presentan los resultados obtenidos del monitoreo realizado y el análisis comparativo con
respecto a la normativa vigente:

**Tabla 4: Información para el modelamiento**

|Contaminantes|Norma de calidad del aire|Valores Normados|2013<br>(no válido)|2014<br>(válido)|2015<br>(válido)|
|---|---|---|---|---|---|
|MP2,5|D.S. N° 12/2011|Promedio Anual: 20 μg/m3|13,74 (referencial)|13,74 (referencial)|13,74 (referencial)|
|MP2,5|D.S. N° 12/2011|P98 24 horas: 50 μg/m3|44,14|26,73|23,97|
|MP10|D.S. N° 59/1998, modificado<br>por D.S. N° 45/2001|Promedio Anual: 50 μg/m3|40,89 (referencial)|40,89 (referencial)|40,89 (referencial)|
|MP10|D.S. N° 59/1998, modificado<br>por D.S. N° 45/2001|P98 24 horas: 150 μg/m3|80,76|65,04|66,63|

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 31
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**4.** **BASES DE DATOS Y ARCHIVOS DE MODELACIÓN**

La base de datos para la modelación CALMET-CALPUFF considero la siguiente información:

**Tabla 5: Información para el modelamiento**

 - Emisiones generadas por las actividades del proyecto en cada una de sus fases.

 - Ubicación geográfica del proyecto

 - Área de modelamiento

 - Grilla de modelamiento

 - Topografía del área de modelación

**4.1 Archivos de entrada y salida de la modelación**

Los archivos de entrada y salida de la modelación, para cada etapa del proyecto y que se anexan en forma
digital (DVD), son los siguientes:

**Tabla 6: Archivos de entrada y salida de la modelación**

|CALMET|GEO.DAT|
|---|---|
|CALMET|CALMET.DAT|
|CALMET|CALMET.LST|
|CALMET|CALMET.INP|
|CALPUF|CALPUFF.LST|
|CALPUF|CALPUFF.INP|
|CALPUF|CONS.INP|
|CALPOST|CALPOST.DAT|
|CALPOST|CALPOST.LST|
|CALPOST|CALPOST.INP|
|ARCHIVOS COMPLEMENTARIOS|Dry Flux Data File|
|ARCHIVOS COMPLEMENTARIOS|Wet Flux Data|

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 32
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**5.** **CARACTERÍSTICAS DEL DOMINIO DE MODELACIÓN Y SU ENTORNO**

**5.1 Localización**

El proyecto se ubica en la Región y Provincia de Antofagasta, Comunas de Antofagasta y Mejillones. En la figura
siguiente se puede apreciar la ubicación del proyecto.

**Figura 18: División Político-Administrativa**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 33
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**5.2 Área de modelamiento**

El área o dominio de modelación considerado tiene su origen en las coordenadas UTM WGS84 19S - E: 333.000
y N: 7.386.875 A partir de este punto, el dominio considera un área de 50 kilómetros en la dirección Este y 67
kilómetros en la dirección Norte, que incluye la totalidad de las fuentes emisoras del proyecto y los receptor en
Antofagasta y Mejillones.

**Figura 19: Área de Modelamiento**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 34
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**5.3 Grilla de modelamiento**

La grilla de modelamiento utilizada corresponde a un dominio de 50 x 67 km con espaciamiento de 4 km.

**Figura 20: Grilla Meteorológica de Modelamiento**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 35
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**5.4 Topografía del área de modelamiento**

La topografía del área de modelamiento se ha obtenido satelitalmente mediante la aplicación de archivos de
terreno del software Calpuff View. La siguiente figura ilustra las curvas de nivel para el área de modelamiento.

**Figura 21: Topografía del Área de Modelación**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 36
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**5.5 Receptores en el área de modelamiento**

El área de influencia (AI) para el componente aire se determinó en función de los receptores sensibles
(asentamiento humano), que puedan verse afectados por las emisiones de material particulado y gases,
generados por las actividades de las distintas fases del proyecto NAVÍO II.

Para identificar los receptores sensibles y definir la línea base de aire, se realizó una campaña de terreno el día
14 de Junio de 2015, identificándose 3 receptores, los cuales se presentan en la tabla 7.

**Tabla 7: Ubicación y descripción de puntos receptores sensibles**

|Punto|Descripción|Coordenadas UTM|Col4|
|---|---|---|---|
|**Punto**|**Descripción**|**WGS 84 Huso 19S**|**WGS 84 Huso 19S**|
|**Punto**|**Descripción**|**Este**|**Norte**|
|R1|Ciudad de Mejillones|351.437|7.443.881|
|R2|Cruce Ruta B400 con Ruta 1|354.333|7.415.321|
|R3|Cerro Moreno|353.572|7.407.780|

**Figura 22: Emplazamiento de Puntos Receptores Sensibles**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 37
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**5.6 Suelos del área de modelamiento**

La siguiente figura ilustra el tipo de suelo en el área de modelamiento.

**Figura 23: Emplazamiento de Puntos Receptores Sensibles**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 38
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**6.** **FUENTES DE EMISIÓN**

**6.1 Actividades emisoras**

Las emisiones a la atmósfera que generará el Proyecto “NAVÍO II”, en sus distintas fases, corresponderán a
emisiones fugitivas de material particulado respirable MP 10, MP 2.5, material particulado sedimentable (MPS),
gases de combustión de vehículos y maquinarias y gases de equipos generadores, que serán utilizados en las
distintas fases que comprende este proyecto.

**6.1.1 Fase de Construcción**

En esta fase del proyecto, las emisiones de MPS, MP10, MP2.5 y gases de combustión, se generan como
consecuencia de las actividades de escarpe, excavaciones, transferencia de material, circulación de vehículos
por caminos pavimentados y por caminos no pavimentados, operación de maquinarias, operación de vehículos
pesados y livianos y funcionamiento de grupos electrógenos.

La siguiente tabla, presenta las características de las actividades del proyecto generadoras de emisiones
atmosféricas, durante la fase de construcción.

**Tabla 8: Actividad Generadora de Emisiones - Fase de Construcción**

|Actividad Generadora de Emisiones - Fase de Construcción|Col2|Col3|Col4|Tipo de<br>Contaminante|
|---|---|---|---|---|
|**Actividad**|**Parámetros**|**Unidad**|**Duración**<br>**Actividad**|**Duración**<br>**Actividad**|
|**Escarpado área total del proyecto**<br>(preparación de terreno)|Área Total: 115.436|m2|30 días|MP10 <br>MP2.5 <br>MPS|
|**Excavaciones**|Volumen: 1862|m3|30 días|30 días|
|**Excavaciones**|Densidad: 1,8|ton/m3|ton/m3|ton/m3|
|**Transferencia de Material**|**Transferencia de Material**|**Transferencia de Material**|**Transferencia de Material**|**Transferencia de Material**|
|Carga y descarga de material de<br>excavaciones|Volumen: 1862|m3|30 días|30 días|
|Carga y descarga de material de<br>excavaciones|Densidad: 1,8|ton/m3|ton/m3|ton/m3|
|Carga y descarga de material para<br>construcción de parapetos (canchas de<br>nitratos y polvorines))|Volumen: 40.006|m3|30 días|30 días|
|Carga y descarga de material para<br>construcción de parapetos (canchas de<br>nitratos y polvorines))|Densidad: 1,8|ton/m3|ton/m3|ton/m3|
|Carga y descarga de áridos|Volumen: 600|m3|60 días|60 días|
|Carga y descarga de áridos|Densidad: 1,6|ton/m3|ton/m3|ton/m3|
|Carga y Descarga material para llenos)|Volumen: 21.056|m3|30 días|30 días|
|Carga y Descarga material para llenos)|Densidad: 1,8|ton/m3|ton/m3|ton/m3|
|**Tránsito de Vehículos por Caminos Pavimentados**|**Tránsito de Vehículos por Caminos Pavimentados**|**Tránsito de Vehículos por Caminos Pavimentados**|**Tránsito de Vehículos por Caminos Pavimentados**|**Tránsito de Vehículos por Caminos Pavimentados**|
|Transporte Materiales de Construcción|Viajes totales: 180|viajes|180 días|180 días|
|Transporte Materiales de Construcción|Longitud: 35|km|km|km|
|Transporte otros Materiales de Construcción|Viajes totales: 180|viajes|180 días|MP10 <br>MP2.5|
|Transporte otros Materiales de Construcción|Longitud: 35|km|km|km|

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 39
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

|Transporte Árido Para Construcción|Viajes totales: 60|viajes|60 días|MPS|
|---|---|---|---|---|
|Transporte Árido Para Construcción|Longitud: 35|km|km|km|
|Transporte Hormigón|Viajes totales: 60|viajes|60 días|60 días|
|Transporte Hormigón|Longitud: 35|km|km|km|
|Transporte Agua Potable|Viajes totales: 180|viajes|180 días|180 días|
|Transporte Agua Potable|Longitud: 35|km|km|km|
|Transporte Agua Industrial para<br>Construcción y Riesgo|Viajes totales: 180|viajes|180 días|180 días|
|Transporte Agua Industrial para<br>Construcción y Riesgo|Longitud: 35|km|km|km|
|Transporte Aguas Servidas|Viajes totales: 180|viajes|180 días|180 días|
|Transporte Aguas Servidas|Longitud: 35|km|km|km|
|Transporte Residuos|Viajes totales: 180|viajes|180 días|180 días|
|Transporte Residuos|Longitud: 35|km|km|km|
|Transporte de Personal|Viajes totales: 360|viajes|180 días|180 días|
|Transporte de Personal|Longitud: 35|km|km|km|
|Transporte de Supervisores|Viajes totales: 720|viajes|180 días|180 días|
|Transporte de Supervisores|Longitud: 35|km|km|km|
|**Tránsito de Vehículos Livianos por Caminos No Pavimentados**|**Tránsito de Vehículos Livianos por Caminos No Pavimentados**|**Tránsito de Vehículos Livianos por Caminos No Pavimentados**|**Tránsito de Vehículos Livianos por Caminos No Pavimentados**|**Tránsito de Vehículos Livianos por Caminos No Pavimentados**|
|Transporte de Personal|Viajes totales: 360|viajes|180 días|180 días|
|Transporte de Personal|Longitud: 3,75|km|km|km|
|Transporte de Supervisores|Viajes totales: 720|viajes|180 días|180 días|
|Transporte de Supervisores|Longitud: 3,75|km|km|km|
|**Tránsito de Vehículos Pesados por Caminos No Pavimentados**|**Tránsito de Vehículos Pesados por Caminos No Pavimentados**|**Tránsito de Vehículos Pesados por Caminos No Pavimentados**|**Tránsito de Vehículos Pesados por Caminos No Pavimentados**|**Tránsito de Vehículos Pesados por Caminos No Pavimentados**|
|Transporte Materiales de Construcción|Viajes totales: 180|viajes|180 días|180 días|
|Transporte Materiales de Construcción|Longitud: 3,75|km|km|km|
|Transporte material para relleno y<br>construcción de parapetos|Viajes totales: 3.420|viajes|180 días|180 días|
|Transporte material para relleno y<br>construcción de parapetos|Longitud: 1|km|km|km|
|Transporte otros Materiales de Construcción|Viajes totales: 180|viajes|180 días|180 días|
|Transporte otros Materiales de Construcción|Longitud: 3,75|km|km|km|
|Transporte Árido Para Construcción|Viajes totales: 60|viajes|60 días|60 días|
|Transporte Árido Para Construcción|Longitud: 3,75|km|km|km|
|Transporte Hormigón|Viajes totales: 60|viajes|60 días|60 días|
|Transporte Hormigón|Longitud: 3,75|km|km|km|
|Transporte Agua Potable|Viajes totales: 180|viajes|180 días|180 días|
|Transporte Agua Potable|Longitud: 3,75|km|km|km|
|Transporte Agua Industrial para<br>Construcción y Riesgo|Viajes totales: 180|viajes|180 días|180 días|
|Transporte Agua Industrial para<br>Construcción y Riesgo|Longitud: 3,75|km|km|km|
|Transporte Aguas Servidas|Viajes totales: 180|viajes|180 días|180 días|
|Transporte Aguas Servidas|Longitud: 3,75|km|km|km|
|Transporte Residuos|Viajes totales: 180|viajes|180 días|180 días|
|Transporte Residuos|Longitud: 3,75|km|km|km|
|**Emisiones de Gases** de Combustión de maquinarias y vehículos|**Emisiones de Gases** de Combustión de maquinarias y vehículos|**Emisiones de Gases** de Combustión de maquinarias y vehículos|**Emisiones de Gases** de Combustión de maquinarias y vehículos|CO, HC,<br>NOx, CC, y MP|
|**Emisiones de Gases** de Equipos Generadores|**Emisiones de Gases** de Equipos Generadores|**Emisiones de Gases** de Equipos Generadores|**Emisiones de Gases** de Equipos Generadores|CO, NOx, MP10, y<br>SOx|

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 40
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Tabla 9: Maquinarias Utilizados en Fase de Construcción**

|Equipo|Cantidad|Potencia<br>Nominal KW|Operación<br>Diaria (horas)|
|---|---|---|---|
|Bulldozer CAT modelo D5K o similar|1|72|15|
|Cargador frontal CAT modelo 924HZ o similar|1|106|30|
|Retroexcavadora CAT modelo 416F o similar|1|65|30|
|Compactador CAT Modelo CB-434D o similar|1|62|15|
|Motoniveladora CAT modelo 120M2 AWD o similar|1|108|15|
|Excavadora CAT modelo 315C o similar|1|82|30|

**Tabla 10: Vehículos Utilizados en Fase de Construcción**

|Actividad|Categoría<br>Vehículo|N°<br>Viajes/día|Trayecto<br>Pavimentado<br>(km)|Trayecto No<br>Pavimentado<br>(km)|Velocidad<br>Circulación<br>Pavimentado<br>(km/h)|Velocidad<br>Circulación No<br>Pavimentado<br>(km/h)|
|---|---|---|---|---|---|---|
|Transporte Materiales de<br>Construcción|Diésel Tipo 3|1|30|3,75|100|30|
|Transporte Otros Materiales<br>de Construcción|Diésel Tipo 3|19|30|1|100|30|
|Transporte Árido Para<br>Construcción|Diésel Tipo 3|1|30|3,75|100|30|
|Transporte Hormigón|Diésel Tipo 3|1|30|3,75|100|30|
|Transporte de Agua Industrial<br>Para Construcción y Riego|Diésel Tipo 3|1|30|3,75|100|30|
|Transporte Material para<br>Relleno|Diésel Tipo 3|1|30|3,75|100|30|
|Transporte H2O Servidas|Diésel Tipo 3|1|30|3,75|100|30|
|Transporte Residuos|Diésel Tipo 3|1|30|3,75|100|30|
|Transporte Personal<br>Construcción Planta|Buses<br>Particulares|1|30|3,75|100|30|
|Transporte Supervisión|Comerciales<br>Diésel Tipo 2|2|30|3,75|100|30|

**Tabla 11: Generadores Utilizados en Fase de Construcción**

|Equipo|Cantidad|Tipo de<br>Combustible|Potencia (KW)|Operación Diaria<br>(horas)|
|---|---|---|---|---|
|Generador|2|Diésel|24|24|

**6.1.2 Fase de Operación**

En esta fase del proyecto, las emisiones de MPS, MP10, MP2.5 y gases de combustión, se generan como
consecuencia de las actividades de circulación de vehículos por caminos pavimentados, circulación de vehículos
pesados y livianos por caminos no pavimentados, operación de caldera y operación del generador eléctrico.

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 41
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

La siguiente tabla, presenta las características de las actividades del proyecto generadoras de emisiones
atmosféricas, durante la fase de operación.

**Tabla 12: Actividad Generadora de Emisiones - Fase de Operación**

|Actividad Generadora de Emisiones - Fase de Operación|Col2|Col3|Col4|Tipo de<br>Contaminante|
|---|---|---|---|---|
|**Actividad**|**Parámetros**|**Unidad**|**Duración**<br>**Actividad**|**Duración**<br>**Actividad**|
|**Tránsito de Vehículos por Caminos Pavimentados**|**Tránsito de Vehículos por Caminos Pavimentados**|**Tránsito de Vehículos por Caminos Pavimentados**|**Tránsito de Vehículos por Caminos Pavimentados**||
|Transporte de agua potable|Viajes totales: 1|viajes|365 días/año|MP10 <br>MP2.5<br>MPS|
|Transporte de agua potable|Longitud: 35|km|km|km|
|Transporte de Agua Industrial|Viajes totales: 2|viajes|365 días/año|365 días/año|
|Transporte de Agua Industrial|Longitud: 35|km|km|km|
|Transporte de Combustible (Petróleo Diésel)|Viajes totales: 1|viajes|365 días/año|365 días/año|
|Transporte de Combustible (Petróleo Diésel)|Longitud: 35|km|km|km|
|Transporte Materiales Primas e Insumos|Viajes totales: 6|viajes|365 días/año|365 días/año|
|Transporte Materiales Primas e Insumos|Longitud: 35|km|km|km|
|Transporte de Productos|Viajes totales: 9|viajes|365 días/año|365 días/año|
|Transporte de Productos|Longitud: 35|km|km|km|
|Transporte de Residuos|Viajes totales: 4|viajes|365 días/año|365 días/año|
|Transporte de Residuos|Longitud: 35|km|km|km|
|Transporte de Personal|Viajes totales: 8|viajes|365 días/año|365 días/año|
|Transporte de Personal|Longitud: 35|km|km|km|
|**Tránsito de Vehículos Livianos por Caminos No Pavimentados**|**Tránsito de Vehículos Livianos por Caminos No Pavimentados**|**Tránsito de Vehículos Livianos por Caminos No Pavimentados**|**Tránsito de Vehículos Livianos por Caminos No Pavimentados**||
|Transporte de Personal|Viajes totales: 8|viajes|365 días/año|MP10 <br>MP2.5<br>MPS|
|Transporte de Personal|Longitud: 3,75|km|km|km|
|**Tránsito de Vehículos Pesados por Caminos No Pavimentados**|**Tránsito de Vehículos Pesados por Caminos No Pavimentados**|**Tránsito de Vehículos Pesados por Caminos No Pavimentados**|**Tránsito de Vehículos Pesados por Caminos No Pavimentados**||
|Transporte de agua potable|Viajes totales: 1|viajes|365 días/año|MP10 <br>MP2.5<br>MPS|
|Transporte de agua potable|Longitud: 3,75|km|km|km|
|Transporte de Agua Industrial|Viajes totales: 2|viajes|365 días/año|365 días/año|
|Transporte de Agua Industrial|Longitud: 3,75|km|km|km|
|Transporte de Combustible (Petróleo Diésel)|Viajes totales: 1|viajes|365 días/año|365 días/año|
|Transporte de Combustible (Petróleo Diésel)|Longitud: 3,75|km|km|km|
|Transporte Materiales Primas e Insumos|Viajes totales: 6|viajes|365 días/año|365 días/año|
|Transporte Materiales Primas e Insumos|Longitud: 3,75|km|km|km|
|Transporte de Productos|Viajes totales: 9|viajes|365 días/año|365 días/año|
|Transporte de Productos|Longitud: 3,75|km|km|km|
|Transporte Interno de Materias Primas|Viajes totales: 6|viajes|365 días/año|365 días/año|
|Transporte Interno de Materias Primas|Longitud: 3,75|km|km|km|
|Transporte de Residuos|Viajes totales: 4|viajes|365 días/año|365 días/año|
|Transporte de Residuos|Longitud: 3,75|km|km|km|
|**Emisiones de Gases** de Combustión de maquinarias y vehículos|**Emisiones de Gases** de Combustión de maquinarias y vehículos|**Emisiones de Gases** de Combustión de maquinarias y vehículos|**Emisiones de Gases** de Combustión de maquinarias y vehículos|CO, HC,<br>NOx, CC, y MP|
|**Emisiones de Gases** de Equipos Generadores|**Emisiones de Gases** de Equipos Generadores|**Emisiones de Gases** de Equipos Generadores|**Emisiones de Gases** de Equipos Generadores|CO, NOx, MP10, y<br>SOx|

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 42
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Tabla 13: Equipos y/o Maquinarias Utilizados en Fase de Operación**

|Equipo|Cantidad|Potencia Nominal<br>(KW)|Operación Diaria<br>(horas)|
|---|---|---|---|
|Grúa Horquilla<br>|4|30|24|

**Tabla 14: Vehículos Utilizados en Etapa de Operación**

|Actividad|Categoría<br>Vehículo|N°<br>Viajes/día|Trayecto<br>Pavimentado<br>(km)|Trayecto No<br>Pavimentado<br>(km)|Velocidad<br>Circulación<br>Pavimentado<br>(km/h)|Velocidad<br>Circulación No<br>Pavimentado<br>(km/h)|
|---|---|---|---|---|---|---|
|Transporte de agua potable|Diésel Tipo 3|1|30|3,75|100|30|
|Transporte de Agua Industrial|Diésel Tipo 3|2|30|3,75|100|30|
|Transporte de Combustible<br>(Petróleo Diésel)|Diésel Tipo 3|1|30|3,75|100|30|
|Transporte de Materias<br>primas|Diésel Tipo 3|6|30|3,75|100|30|
|Transporte de Producto<br>(Emulsión)|Diésel Tipo 3|8|30|3,75|100|30|
|Transporte de Producto<br>(Anfo)|Diésel Tipo 3|1|30|3,75|100|30|
|Transporte de Residuos|Diésel Tipo 3|6|30|3,75|100|30|
|Transporte Interno de<br>materias primas y productos|Diésel Tipo 3|4|30|3|100|30|
|Transporte Personal de<br>Operaciones|Buses<br>Particulares|2|30|3,75|100|30|
|Transporte Supervisores|Comerciales<br>Diésel Tipo 2|6|30|3,75|100|30|

**6.1.3 Fase de Cierre**

En esta fase del proyecto, las emisiones de MPS, MP10, MP2.5 y gases de combustión, se generan como
consecuencia de las actividades de nivelación del terreno, transferencia de material para la nivelación,
circulación de vehículos en caminos pavimentados, circulación de vehículos pesados y livianos por caminos no
pavimentados, operación de maquinarias, operación de vehículos pesados y livianos.

La siguiente tabla, presenta las características de las actividades del proyecto generadoras de emisiones
atmosféricas, durante la fase de cierre.

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 43
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Tabla 15: Actividad Generadora de Emisiones - Fase de Cierre**

|Actividad Generadora de Emisiones - Fase de Cierre|Col2|Col3|Col4|Tipo de<br>Contaminante|
|---|---|---|---|---|
|**Actividad**|**Parámetros**|**Unidad**|**Duración**<br>**Actividad**|**Duración**<br>**Actividad**|
|**Reperfilado del área**|Volumen: 20.000|m3|30 días|MP10 <br>MP2.5<br>MPS|
|**Reperfilado del área**|Densidad: 1,8|ton/m3|ton/m3|ton/m3|
|**Tránsito de Vehículos por Caminos Pavimentados**|**Tránsito de Vehículos por Caminos Pavimentados**|**Tránsito de Vehículos por Caminos Pavimentados**|**Tránsito de Vehículos por Caminos Pavimentados**|**Tránsito de Vehículos por Caminos Pavimentados**|
|Transporte Material de Desarme|Viajes totales: 1|viajes|180 días|180 días|
|Transporte Material de Desarme|Longitud: 35|km|km|km|
|Transporte Residuos Varios|Viajes totales: 1|viajes|180 días|180 días|
|Transporte Residuos Varios|Longitud: 35|km|km|km|
|Transporte de Personal|Viajes totales: 3|viajes|180 días|180 días|
|Transporte de Personal|Longitud: 35|km|km|km|
|Transporte de Supervisión|Viajes totales: 1|viajes|180 días|180 días|
|Transporte de Supervisión|Longitud: 35|km|km|km|
|**Tránsito de Vehículos Livianos por Caminos No Pavimentados**|**Tránsito de Vehículos Livianos por Caminos No Pavimentados**|**Tránsito de Vehículos Livianos por Caminos No Pavimentados**|**Tránsito de Vehículos Livianos por Caminos No Pavimentados**|MP10 <br>MP2.5<br>MPS|
|Transporte de Personal|Viajes totales: 3|viajes|180 días|180 días|
|Transporte de Personal|Longitud: 3,75|km|km|km|
|Transporte de Supervisión|Viajes totales: 1|viajes|180 días|180 días|
|Transporte de Supervisión|Longitud: 3,75|km|km|km|
|**Tránsito de Vehículos Pesados por Caminos No Pavimentados**|**Tránsito de Vehículos Pesados por Caminos No Pavimentados**|**Tránsito de Vehículos Pesados por Caminos No Pavimentados**|**Tránsito de Vehículos Pesados por Caminos No Pavimentados**|**Tránsito de Vehículos Pesados por Caminos No Pavimentados**|
|Transporte Material de Desarme|Viajes totales: 1|viajes|180 días|180 días|
|Transporte Material de Desarme|Longitud: 3,75|km|km|km|
|Transporte Riego Caminos|Viajes totales: 3|viajes|180 días|180 días|
|Transporte Riego Caminos|Longitud: 3,75|km|km|km|
|Transporte de Materiales Excedentes|Viajes totales: 1|viajes|180 días|180 días|
|Transporte de Materiales Excedentes|Longitud: 3,75|km|km|km|
|Transporte de Residuos Varios|Viajes totales: 1|viajes|180 días|180 días|
|Transporte de Residuos Varios|Longitud: 3,75|km|km|km|
|**Emisiones de Gases** de Combustión de maquinarias y vehículos|**Emisiones de Gases** de Combustión de maquinarias y vehículos|**Emisiones de Gases** de Combustión de maquinarias y vehículos|**Emisiones de Gases** de Combustión de maquinarias y vehículos|CO, HC,<br>NOx, CC, y MP|
|**Emisiones de Gases** de Equipos Generadores<br>|**Emisiones de Gases** de Equipos Generadores<br>|**Emisiones de Gases** de Equipos Generadores<br>|**Emisiones de Gases** de Equipos Generadores<br>|CO, NOx, MP10, y<br>SOx|

**Tabla 16: Equipos y/o Maquinarias Utilizados en Fase de Cierre**

|Equipo|Cantidad|Potencia<br>Nominal KW|Operación<br>Diaria (horas)|
|---|---|---|---|
|Bulldozer CAT modelo D5K o similar|1|72|15|
|Cargador frontal CAT modelo 924HZ o similar|1|106|30|

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 44
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Tabla 17: Vehículos Utilizados en Etapa de Cierre**

|Actividad|Categoría<br>Vehículo|N°<br>Viajes/día|Trayecto<br>Pavimentado<br>(km)|Trayecto No<br>Pavimentado<br>(km)|Velocidad<br>Circulación<br>Pavimentado<br>(km/h)|Velocidad<br>Circulación No<br>Pavimentado<br>(km/h)|
|---|---|---|---|---|---|---|
|Transporte Material de<br>Desarme|Diésel Tipo 3|1|35|3,75|100|30|
|Transporte Residuos Varios|Diésel Tipo 3|1|35|3,75|100|30|
|Transporte Riego Caminos|Diésel Tipo 3|3|35|3,75|100|30|
|Transporte Personal de<br>Cierre|Buses<br>Particulares|1|35|3,75|100|30|
|Transporte Supervisores|Comerciales<br>Diésel Tipo 2|3|35|3,75|100|30|

**Tabla 18: Generadores Utilizados en Fase de Cierre**

|Equipo|Cantidad|Tipo de<br>Combustible|Potencia (KW)|Operación Diaria<br>(horas)|
|---|---|---|---|---|
|Generador<br>|1|Diésel|12|24|

**6.2 Peso Promedio de la Flota**

El peso promedio de la flota (PPF) se determinó de acuerdo a la proporción de peso de los vehículos
considerados en la flota (PPV), proporción de viajes por tipo de vehículos considerados en la flota (VPV) y el
peso promedio del tipo de vehículos considerados en la flota (PMV), aplicando la siguiente formulación:

**PPF = Σ PPV**

**PPV = PMV * PV**

**PV = VTP / TVF**

Dónde:

PPF : Peso promedio de la flota (ton)
PPV : Proporción de peso de los vehículos considerados en la flota
PMV : Peso promedio del tipo de vehículos considerados en la flota (ton)
VP : Proporción de viajes por tipo de vehículos respecto de los viajes totales de la flota
VTP : Viajes por tipo de Vehículos
TVF : Total de viajes de la Flota

Las tablas siguientes presentan el peso promedio asignado a cada tipo de vehículos que circulara por caminos

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 45
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

pavimentadas y no pavimentadas, y los pesos promedios de la flota.

**Tabla 19: Peso Promedio de la Flota en Fase de Construcción**

|Vehículos|Cantidad<br>de Viajes<br>Totales<br>(VTP)|Capacidad<br>de carga<br>(ton)|Peso<br>Vacío<br>(ton)|Peso<br>Cargado<br>(ton)|Peso<br>Promedio<br>(PMV)|Proporción<br>en Peso<br>(PPV)|Peso<br>Promedio<br>Flota<br>(PPF)|
|---|---|---|---|---|---|---|---|
|Transporte Materiales de<br>Construcción|1|30|15|45|30|0,97|**27,10**|
|Transporte de material para<br>relleno y construcción de<br>parapetos|19|30|15|45|30|18,39|18,39|
|Transporte Otros Materiales<br>de Construcción|1|30|15|45|30|0,97|0,97|
|Transporte Árido Para<br>Construcción|1 <br>|30|15|45|30|0,97|0,97|
|Transporte Hormigón|1 <br>|30|15|45|30|0,97|0,97|
|Transporte de H2O Potable|1|30|15|45|30|0,97|0,97|
|Transporte de Agua<br>Industrial Para<br>Construcción y Riego|5 <br>|15|7,5|22,5|15|2,42|2,42|
|Transporte H2O Servidas|1 <br>|15|7,5|22,5|15|0,48|0,48|
|Transporte Residuos|1|30|15|45|30|0,97|0,97|
|**TOTAL**|**31**|||||||

**Tabla 20: Peso Promedio de la Flota en Fase de Operación**

|Vehículos|Cantidad<br>de Viajes<br>Diarios<br>(VTP)|Capacidad<br>de carga<br>(ton)|Peso<br>Vacío<br>(ton)|Peso<br>Cargado<br>(ton)|Peso<br>Promedio<br>(PMV)|Proporción<br>en Peso<br>(PPV)|Peso<br>Promedio<br>Flota<br>(PPF)|
|---|---|---|---|---|---|---|---|
|Transporte de agua potable|1|15|7,5|22,5|15|0,52|**25,34**|
|Transporte de Agua<br>Industrial|2|15|7,5|22,5|15|1,03|1,03|
|Transporte de Combustible<br>(Petróleo Diésel)|1|30|15|45|30|1,03|1,03|
|Transporte de Materias<br>primas|6|30|15|45|30|6,21|6,21|
|Transporte de Productos|9|30|15|45|30|9,31|9,31|
|Transporte de Residuos|6|15|7,5|22,5|15|3,10|3,10|
|Transporte Interno de<br>materias primas y<br>productos|4|30|15|45|30|4,14|4,14|
|**TOTAL**|**29**|||||||

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 46
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Tabla 21: Peso Promedio de la Flota en Fase de Cierre**

|Vehículos|Cantidad<br>de Viajes<br>Diarios<br>(VTP)|Capacidad<br>de carga<br>(ton)|Peso<br>Vacío<br>(ton)|Peso<br>Cargado<br>(ton)|Peso<br>Promedio<br>(PMV)|Proporción<br>en Peso<br>(PPV)|Peso<br>Promedio<br>Flota<br>(PPF)|
|---|---|---|---|---|---|---|---|
|Transporte Material de<br>Desarme|1|30|15|45|30|6|18|
|Transporte Residuos Varios|1|15|7.5|22,5|15|3|3|
|Transporte Riego Caminos|3|15|7.5|22,5|15|9|9|
|**TOTAL**|**5 **|||||||

**6.3 Metodología Para La Estimación De Emisiones**

La ecuación general para estimar las emisiones de cualquier actividad, es la siguiente:

Dónde:

_E_ : Emisiones (Ton/año)

_fe_ : Factor de emisión

_Na_ : Nivel de actividad

_Ea_ : Eficiencia de abatimiento

**6.3.1 Metodología para la estimación de emisiones de las actividades**

Las emisiones de material particulado (MP 10, MP 2.5, MPS), generadas por las actividades del proyecto, en cada
una de sus fases, se han estimado utilizando el documento de referencia “Recopilación y Sistematización de
Factores de Emisión al Aire, mayo 2015”, publicado en la página web del SEA”, la Guía para la estimación de
emisiones atmosféricas de proyectos inmobiliarios para la Región Metropolitana del Ministerio del Medio
Ambiente, [enero 2012] y los factores de emisión del Manual AP 42 de la EPA (Fifth Edition, Compilation of Air
Pollutant Emission Factors, Volume 1: Stationary Point and Area Sources, United States - Environmental
Protection Agency).

Para el cálculo de los factores de emisiones, se han utilizado los valores por defecto que establece la Guía para
la estimación de emisiones atmosféricas de proyectos inmobiliarios para la Región Metropolitana del Ministerio
del Medio Ambiente, [enero 2012].

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 47
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

Las emisiones han sido estimadas en kg/día y ton/año, de acuerdo a la programación de las actividades.

**6.3.2 Metodología para la estimación de emisiones de maquinarias**

La metodología utilizada para determinar las emisiones de material particulado de combustión y gases asociados
a la operación de la maquinaria, durante cada una de las fases del proyecto, corresponde a la que se presenta
en el documentos de referencia “Recopilación y Sistematización de Factores de Emisión al Aire, mayo 2015”,
publicado en la página web del SEA” y la Guía para la Estimación de Emisiones Atmosféricas de Proyectos
Inmobiliarios para la Región Metropolitana (Enero 2012).

La ecuación general para estimar las emisiones de material particulado de combustión y gases asociados a la
operación de la maquinaria, es la siguiente:

**E = (FP * t * C * P)**

Dónde:

FP: factor según potencia
t: tiempo de operación diaria (h)
C: Porcentaje de carga
P: Potencia Nominal (kw)

**6.3.3 Metodología para la estimación de emisiones de vehículos**

La metodología utilizada para determinar las emisiones de material particulado de combustión y gases de la flota
de vehículos, en cada una de las fases del proyecto, corresponde a la que se presenta en la Guía para la
Estimación de Emisiones Atmosféricas de Proyectos Inmobiliarios para la Región Metropolitana (Enero 2012).

Las categorías de los vehículos que conforman la flota de vehículos del proyecto, es la siguiente:

Camiones Pesados Diésel Tipo 3: Corresponden a camiones pesados con peso bruto superior a 16 toneladas
cuya fecha de inscripción en el Registro Nacional de Vehículos Motorizados sea posterior a septiembre del año
2003. Estos buses deben cumplir con la normativa EPA 98 o Euro III. Notar que esta fecha de aplicación tiene
aún cierto grado de incerteza y será aclarada una vez que la autoridad por decreto lo establezca.

Camiones Medianos Diésel Tipo 3. Corresponden a camiones medianos con peso bruto entre 7.5 y 16 toneladas
cuya fecha de inscripción en el Registro Nacional de Vehículos Motorizados sea posterior a septiembre del año
2003. Estos buses deben cumplir con la normativa EPA 98 o Euro III. Notar que esta fecha de aplicación tiene
aún cierto grado de incerteza y será aclarada una vez que la autoridad por decreto lo establezca.

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 48
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

Vehículos Comerciales Diésel Tipo 2: Corresponden a los vehículos livianos de pasajeros o carga liviana,
privados o comerciales y que funcionan con combustible diésel, principalmente del tipo jeep, camioneta o furgón
cuya fecha de inscripción en el registro Nacional de Vehículos Motorizados sea posterior a septiembre del año
2003 cumpliendo con la normativa EPA 94 federal o la Euro III. Notar que la normativa específica y la fecha de
aplicación tienen aún cierto grado de incerteza y será aclarada una vez que la autoridad por decreto lo

establezca.

El nivel de actividad (Na) corresponde a la cantidad de kilómetros que circula cada vehículo.

**6.3.4 Metodología para la estimación de emisiones de Ggeneradores Eléctricos**

La metodología utilizada para determinar las emisiones de material particulado de combustión y gases de los
generadores eléctricos, en cada una de las fases del proyecto, corresponde a la que se presenta en la “Guía
para la Estimación de Emisiones Atmosféricas de Proyectos Inmobiliarios para la Región Metropolitana, enero
2012, (ref. Compilation of Air Pollutant Emission Factors, AP 42: Chapter 3, Section 3.3 “Gasoline And Diesel
Industrial Engines, table 3.3-1).

**6.3.5 Metodología para la estimación de emisiones por combustión en Calderas a GLP**

La metodología utilizada para determinar las emisiones de material particulado de combustión y gases de la
Calderas a GLP, considerada para la fase de operación del proyecto, corresponde a la que se presenta en la
“Guía Metodológica Para la Estimación de Emisiones Atmosféricas de Fuentes Fijas y Móviles en el Registro de
Emisiones y Transferencia de Contaminantes, 2009 Comisión Nacional del Medio Ambiente, tabla 4 (ref. AP-42
de la EPA, LPG Combustion, Industrial Boilers, Quinta Edición/1998).

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 49
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**7.** **FACTORES DE EMISIÓN**

Los factores de emisión (fe) corresponden a ecuaciones o expresiones matemáticas que permiten estimar tasas
unitarias de emisiones atmosféricas. Para el caso específico de las operaciones relacionadas con este proyecto,
en cada una de sus fases, se utilizaron los modelos matemáticos para factores de emisión, propuestos en el
Manuel AP-42 (Compilation of Air Pollutant Emission Factors), de la Agencia de Protección del Ambiente de los
EE.UU. (U.S. EPA) y la Guía para la estimación de emisiones atmosféricas de proyectos inmobiliarios para la
Región Metropolitana del Ministerio del Medio Ambiente, [enero 2012].

Estos factores de emisión, proporcionan un valor representativo de la cantidad de agentes contaminante por
unidad de peso, volumen, distancia o duración de la actividad. En muchos casos, los factores de emisión
representan la media de un conjunto de datos disponibles y, por lo general, se asume como representativo de
períodos de largo plazo.

A continuación se presentan los factores de emisión utilizados para estimar las emisiones del proyecto. En
primer lugar, se presentan los factores de emisión de material particulado resuspendido y posteriormente los
factores de emisión de material particulado y gases asociados a procesos de combustión.

**7.1 Factores De Emisión Para Material Particulado Resuspendido**

Las expresiones de factores de emisión para la estimación de emisiones de material particulado resuspendido,
se presentan a continuación [14] .

**Tabla 22: Factor de Emisión Escarpes**

|Factor de Emisión (fe)|fe = k*0,570|
|---|---|
|Unidades|kg/km|
|Parámetros|No utiliza parámetros<br>K: Factor según tamaño de partícula<br> PM10 = 0,75<br> PM2.5 = 0,105<br> MPS = 1|
|Fuente|Compilation of Air Pollutant Emission Factors, AP 42, 5th Edition: Chapter 13, Section<br>13.2.3“Heavy Construction Operations, 2010”|
|Descripción|Corresponde al factor de emisión de preparación de terrenos (movimiento de tierra) y retiro<br>de cobertura vegetal. La unidad de este factor corresponde a kilógramos emitidos por<br>kilómetro recorrido en el proceso de escarpado de la cobertura vegetal.|
|Nivel de actividad|El nivel de actividad se determina según la distancia que recorre el cargador frontal por el<br>área a escapar. Por defecto para 1 hectárea se recorre una distancia de 3,57 km|

14 Fuente de Información: Guía para la estimación de emisiones atmosféricas de proyectos inmobiliarios para la

Región Metropolitana del Ministerio del Medio Ambiente, [enero 2012].

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 50
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

Mitigación No aplican medidas de mitigación

**Tabla 23: Factor de Emisión Excavaciones**

|Factor de Emisión (fe)|fe = 0.45*k*(s^1.5/M^1.4) [Para PM10 y PM2.5]<br>fe = 2.6*s^1.2/M^1.3 [Para MPS]|
|---|---|
|Unidades|kg/h|
|Parámetros|K: Factor según tamaño de partícula<br> PM10 = 0.75<br> PM2.5 = 0,105<br> MPS = 2.6<br>s: % de finos del suelo [8,5 valor por defecto]<br>M: % humedad material [6,5 valor por defecto]|
|Fuente|Compilation of Air Pollutant Emission Factors, AP 42, 5th Edition: Chapter 11, Section 11.9<br>“Western Surface Coal Mining, 1998”, Table 11.9-2.|
|Descripción|Corresponde al factor de emisión de despeje de material (bulldozing / overburden)<br>escalado por 0,75 para ser aplicado a MP10. La unidad de este factor corresponde a<br>kilógramos emitidos por hora excavada|
|Nota|El nivel de actividad se determina a través del rendimiento de la maquinaria y el volumen a<br>escavar. Por defecto se considerará para una retroexcavadora con capacidad de palada<br>de 1 m3 un rendimiento igual a 30 m3/hr.|
|Mitigación|No aplican medidas de mitigación.|

**Tabla 24: Factor de Emisión Transferencia de Material (Carguío y Volteo de Camiones)**

|Factor de Emisión (fe)|fe = 0.0016*k*(U/2.2)^1.3/(M/2)^1.4|
|---|---|
|Unidades|kg/ton|
|Parámetros|K: Factor según tamaño de partícula<br> PM10 = 0,35<br> PM2.5 = 0,053<br> MPS = 0.74<br>U: Velocidad del viento (m/s) [5 m/s valor por defecto]<br>M: Humedad del material [6,5 valor por defecto]|
|Fuente|Compilation of Air Pollutant Emission Factors, AP 42: Chapter 13, Section 13.2.4<br>“Aggregate Handling and Storage Piles, 2006”.|
|Descripción|Corresponde al factor de emisión de transferencia discreta de material utilizado<br>directamente. La unidad de este factor corresponde a kilogramos emitidos por cada<br>tonelada de material cargado o descargado.|
|Mitigación<br>|No aplican medidas de mitigación.|

**Tabla 25: Factores de Emisión Resuspensión de MP por Circulación de Vehículos en Caminos Pavimentados**

|Factor de Emisión (fe)|fe = k*(sL)^0.91*W^1.02|
|---|---|
|Unidades|gr/ton|

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 51
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

|Parámetros|K: Factor según tamaño de partícula<br>PM10 = 0,62<br>PM2.5 = 0,15<br>MPS = 3.23<br>sL: Carga de fino de la superficie, (g/m2)<br>W: Peso promedio del flujo total de la flota que circula por las vías (Toneladas)|
|---|---|
|Fuente|Compilation of Air Pollutant Emission Factors, AP-42: Chapter 13, Section 13.2.1 “Paved<br>Roads, 2011”.|
|Descripción|Corresponde al factor de emisión de material particulado resuspendido por tránsito de<br>vehículos por caminos pavimentados. La unidad de este factor de emisión es gramos de<br>MP10 emitidos por kilómetro recorrido.|
|Mitigación<br>|No aplican medidas de mitigación.|

**Tabla 26: Factor de Emisión Resuspensión de MP10 Circulación de Vehículos Livianos en Caminos No**
**Pavimentados**

|Factor de Emisión (fe)|fe = 281.9*k*(s/12)*(S/30)^0.5/(M/0.5)^0.2|
|---|---|
|Unidades|g/km|
|Parámetros|K: Factor según tamaño de partícula<br> PM10 = 1.5<br> PM2.5 = 0,15<br> MPS = 4.9<br>s: % de finos del suelo [8,5 valor por defecto]<br>S: Velocidad de los vehículos en km/h<br>M: % humedad material. [6,5 valor por defecto]|
|Fuente|Compilation of Air Pollutant Emission Factors, AP 42: Chapter 13, Section 13.2.2<br>“Unpaved Roads, 2006”.|
|Descripción|Corresponde al factor de emisión de tránsito por caminos no pavimentados determinado<br>para caminos de acceso público. La unidad de este factor de emisión es gramos de MP10<br>emitidos por kilómetro recorrido|
|Nota|Dadas las características de la flota utilizada en la determinación de este factor de<br>emisión, su aplicación se reconoce válida para una flota de vehículos pesados, es decir,<br>cuyo peso promedio exceda las 2,7 toneladas métricas.<br>Contenido de % de finos del suelo - valor por defecto 8,5%<br>Contenido de humedad del suelo - valor por defecto 6,5%|
|Mitigación|Como medida de abatimiento se considera el regadío diario (4 riegos diarios) del camino<br>que une el km 2.3 del bay-pass con la obra (1850 m)|

**Tabla 27: Factor de Emisión Resuspensión de MP10 Circulación de Vehículos Pesados en Caminos No**
**Pavimentados**

|Factor de Emisión (fe)|fe = 281.9*k*(s/12)^0.9*(W/3)^0.45 [Para MP10 y MP2.5]<br>Fe = 281,9*4.9*(s/12) ^0,7*(W/3) ^0,45 [Para MPS]|
|---|---|
|Unidades|g/km|
|Parámetros|K: Factor según tamaño de partícula<br> PM10 = 1.5<br> PM2.5 = 0,15|

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 52
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

|Col1|MPS = 4.9<br>s: % de finos del suelo [8,5 valor por defecto]<br>W: Peso promedio de la flota que circula por las vías (ton)|
|---|---|
|Fuente|Compilation of Air Pollutant Emission Factors, AP 42: Chapter 13, Section 13.2.2<br>“Unpaved Roads”.|
|Descripción|Corresponde al factor de emisión de tránsito por caminos no pavimentados determinado<br>para sitios industriales. La unidad de este factor de emisión es gramos de MP10 emitidos<br>por kilómetro recorrido.|
|Nota|Dadas las características de la flota utilizada en la determinación de este factor de<br>emisión, su aplicación se reconoce válida para una flota de vehículos pesados, es decir,<br>cuyo peso promedio exceda las 2,7 toneladas métricas.<br>El titular deberá proveer el peso promedio de la flota que circula por las vías relevantes.<br>En caso de no hacerlo, el peso promedio por defecto será el peso promedio de la flota<br>generada por la actividad del proyecto.<br>Contenido de % de finos del suelo - valor por defecto 8,5%|
|Mitigación|Como medida de abatimiento se considera el regadío diario (4 riegos diarios) del camino<br>que une el km 2.3 del bay-pass con la obra (1850 m)|

**7.2 Factores de Emisión Para la Estimación de Emisiones de Gases y Material Particulado.**

Los factores de emisión de gases y material particulado de combustión, asociados a la operación de la
maquinaria, vehículos, generadores y calderas, durante las distintas fases del proyecto, se presentan en las
tablas siguientes:

**Tabla 28: Factores de Emisión de Gases y MP de Maquinarias**

|Factor de Emisión (fe)|E= (FP × t × C × P)|
|---|---|
|Unidades|gr/día|
|Parámetros|FP: factor según potencia<br>t: tiempo de operación diaria (h)<br>C: Porcentaje de carga<br>P: Potencia Nominal (kw)|
|Fuente|Guía para la Estimación de Emisiones Atmosféricas de Proyectos Inmobiliarios para la<br>Región Metropolitana, Tabla 4.9|
|Descripción|Corresponde al factor de emisión de combustión de los motores de la maquinaria fuera de<br>ruta.|
|Mitigación|No aplican medidas de mitigación.|

**Tabla 29: Factor de Emisión en Función de la Potencia (g/kW-h)**

|Contaminante|0-20|20-37|37-75|75-130|>130|
|---|---|---|---|---|---|
|CO|8.38|6.43|5.06|3.76|3.00|
|HC|3.87|2.96|2.33|1.72|1.35|
|NOx|14.36|14.36|14.36|14.36|14.36|
|MP|2.22|1.81|1.51|1.23|1.10|

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 53
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Tabla 30: Factor de Emisión Para Gases y MP de Vehículos**

|Categoría|Contaminante|Factor Emisión [g/km]|
|---|---|---|
|Camiones Pesados<br>Diésel Tipo 3|CO|(1,24588358438859+(103,700537481749/(1+exp((((-1)*-<br>1,3906312471446)+(0,543451750078654*ln(V)))+(0,0390066425998189*V)))<br>))|
|Camiones Pesados<br>Diésel Tipo 3|HC|((0,135938586321894+(0,71588074810547*exp(((-<br>1)*0,0234666513590177)*V)))+(2,79878282504916*exp(((-<br>1)*0,123459782380517)*V)))|
|Camiones Pesados<br>Diésel Tipo 3|NOx|((5,58300975720938+(14,5724996214701*exp(((-<br>1)*0,0510403515051286)*V)))+(45,651882800859*exp(((-<br>1)*0,309240087785118)*V)))|
|Camiones Pesados<br>Diésel Tipo 3|CC|((199,101296810716+(496,037924788222*exp(((-<br>1)*0,0466183266185801)*V)))+(3798,31076366067*exp(((-<br>1)*0,573715458508514)*V)))|
|Camiones Pesados<br>Diésel Tipo 3|MP|((0,100820480611018+(0,424449762706025*exp(((-<br>1)*0,0416436785215947)*V)))+(0,864328026775096*exp(((-<br>1)*0,159945936589218)*V)))|
|Camiones Medianos<br>Diésel Tipo 3|CO|((0,731687393919072+(3,6645785309034*exp(((-<br>1)*0,0563683393170761)*V)))+(5,23028829144801*exp(((-<br>1)*0,22940672493427)*V)))|
|Camiones Medianos<br>Diésel Tipo 3|HC|(0,0837360334457316+(1,32104434472513/(1+exp((((-<br>1)*4,53135180004797)+(1,89348725872261*ln(V)))+(-<br>0,0103853145584935*V)))))|
|Camiones Medianos<br>Diésel Tipo 3|NOx|((3,75961273247849+(8,83991867276675*exp(((-<br>1)*0,0582095437791065)*V)))+(32,8119093290992*exp(((-<br>1)*0,324655578422129)*V)))|
|Camiones Medianos<br>Diésel Tipo 3|CC|(1/(((-1,25110663618204E-<br>06*(V2))+(0,000164240816414678*V))+0,00147486189135326))|
|Camiones Medianos<br>Diésel Tipo 3|MP|(0,00753000339418102+(0,481778214802105/(1+exp((((-<br>1)*4,57741464608742)+(1,88064486426566*ln(V)))+(-<br>0,0224165794949045*V)))))|
|Vehículos Comerciales<br>Diésel Tipo 2<br>|CO|0,82*(0,000223*V^2-0,026*k18+1,076)|
|Vehículos Comerciales<br>Diésel Tipo 2<br>|HC|0,62*(0.0000175*V 2-0,00284*V+0,2162)|
|Vehículos Comerciales<br>Diésel Tipo 2<br>|NOx|0,84*(0.000241*V 2-0,03181*V+2,0247)|
|Vehículos Comerciales<br>Diésel Tipo 2<br>|CC|0,0198*V 2-2,506*V+137,42|
|Vehículos Comerciales<br>Diésel Tipo 2<br>|MP|0,67*(0.000045*V 2-0,004885*V+0,1932)|

**Tabla 31: Factor de Emisión por Combustión en Grupos Generadores**

|Factores De Emisión para Grupos Generadores (Factor de Emisión (kg/kw-h)|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**Contaminante**|**MP**|**MP10**|**MP2.5**|**CO**|**NOx**|**SOx**|
|Petróleo Diésel (hasta 600 hp)|0.00134|0.00134|0.00134|0.00406|0.0188|0.00125|

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 54
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Tabla 32: Factor de Emisión para Calderas a GLP**

|Factores De Emisión para Calderas Diésel (Factor de Emisión (kg/kg petróleo diésel)|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Contaminante**|**MP**|**MP10**|**MP2.5**|**CO**|**NOx**|**VOC**|**SOx**|
|Diésel|0,00028|0,00028|0,00014|0,00004|0,00071|0,00283|0,0001|

**8.** **NIVELES DE ACTIVIDAD**

El nivel de actividad (Na) utilizado para calcular las emisiones de cada actividad, en cada una de las fases del
proyecto, se presenta en las tablas siguientes:

**Tabla 33: Nivel de Actividad Etapa de Construcción**

|Actividad Generadora de Emisiones - Fase de Construcción|Nivel de Actividad (Na|Col3|
|---|---|---|
|**Actividad**|**Cantidad**|**Unidad**|
|**Escarpado Área total del Proyecto**(preparación de terreno)|1,37|km/día|
|**Excavaciones**|2,07|h/día|
|**Transferencia de Material**|**Transferencia de Material**|**Transferencia de Material**|
|Carga y descarga de material de excavaciones|111,69|ton/día|
|Carga y descarga de material para construcción de parapetos (canchas de<br>nitratos y polvorines)|2400,36|2400,36|
|Carga y descarga de áridos|16,00|16,00|
|Carga y Descarga material para rellenos|1263,36|1263,36|
|**Tránsito de Vehículos por Caminos Pavimentados**|**Tránsito de Vehículos por Caminos Pavimentados**|**Tránsito de Vehículos por Caminos Pavimentados**|
|Transporte Materiales de Construcción|52,76|km/día|
|Transporte Otros Materiales de Construcción|45,69|45,69|
|Transporte Árido Para Construcción|37,33|37,33|
|Transporte Hormigón|37,33|37,33|
|Transporte de H2O Potable|37,33|37,33|
|Transporte de Agua Industrial Para Construcción y Riego|70,00|70,00|
|Transporte H2O Servidas|70,00|70,00|
|Transporte Residuos|38,89|38,89|
|Transporte Personal Construcción Planta|140,00|140,00|
|Transporte Supervisión|280,00|280,00|
|**Tránsito de Vehículos Livianos por Caminos No Pavimentados**(duración actividad: días)|**Tránsito de Vehículos Livianos por Caminos No Pavimentados**(duración actividad: días)|**Tránsito de Vehículos Livianos por Caminos No Pavimentados**(duración actividad: días)|
|Transporte Personal Construcción Planta|15,00|km/día|
|Transporte Supervisión|30,00|30,00|
|**Tránsito de Vehículos Pesados por Caminos No Pavimentados**(duración actividad: días)|**Tránsito de Vehículos Pesados por Caminos No Pavimentados**(duración actividad: días)|**Tránsito de Vehículos Pesados por Caminos No Pavimentados**(duración actividad: días)|
|Transporte Materiales de Construcción|5,65|km/día|
|Transporte de material para relleno y construcción de parapetos|37,01|37,01|
|Transporte Otros Materiales de Construcción|4,90|4,90|
|Transporte Árido Para Construcción|4,00|4,00|
|Transporte Hormigón|4,00|4,00|
|Transporte de Agua Industrial Para Construcción y Riego|4,00|4,00|
|Transporte H2O Servidas|7,50|7,50|
|Transporte Material para Relleno|10,80|10,80|
|Transporte Residuos<br>|4,17|4,17|

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 55
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Tabla 34: Nivel de Actividad Etapa de Operación**

|Actividad Generadora de Emisiones - Fase de Operación|Nivel de Actividad (Na|Col3|
|---|---|---|
|**Actividad**|**Cantidad**|**Unidad**|
|**Tránsito de Vehículos por Caminos Pavimentados**|**Tránsito de Vehículos por Caminos Pavimentados**|**Tránsito de Vehículos por Caminos Pavimentados**|
|Transporte de agua potable|38,50|km/día|
|Transporte de Agua Industrial|140,00|140,00|
|Transporte de Combustible (Petróleo Diésel)|42,47|42,47|
|Transporte de Materias Primas|447,38|447,38|
|Transporte de Productos (Emulsión)|544,44|544,44|
|Transporte de Producto (Anfo)|70,00|70,00|
|Transporte de Residuos|259,00|259,00|
|Transporte Personal de Operaciones|140,00|140,00|
|Transporte Supervisores|420,00|420,00|
|**Tránsito de Vehículos Livianos por Caminos No Pavimentados**|**Tránsito de Vehículos Livianos por Caminos No Pavimentados**|**Tránsito de Vehículos Livianos por Caminos No Pavimentados**|
|Transporte Personal de Operaciones|15,00|km/día|
|Transporte Supervisores|45,00|45,00|
|**Tránsito de Vehículos Pesados por Caminos No Pavimentados**|**Tránsito de Vehículos Pesados por Caminos No Pavimentados**|**Tránsito de Vehículos Pesados por Caminos No Pavimentados**|
|Transporte de agua potable|4,13|km/día|
|Transporte de Agua Industrial|15,00|15,00|
|Transporte de Combustible (Petróleo Diésel)|4,55|4,55|
|Transporte de Materias Primas|47,93|47,93|
|Transporte de Producto (Emulsión)|58,33|58,33|
|Transporte de Producto (Anfo)|7,50|7,50|
|Transporte Interno de materias primas y productos|47,93|47,93|
|Transporte de Residuos<br>|27,75|27,75|

**Tabla 35: Nivel de Actividad Etapa de Cierre**

|Actividad Generadora de Emisiones - Fase de Cierre|Nivel de Actividad (Na|Col3|
|---|---|---|
|**Actividad**|**Cantidad**|**Unidad**|
|**Reperfilamiento área del proyecto**|0,24|h/día|
|**Tránsito de Vehículos por Caminos Pavimentados**|**Tránsito de Vehículos por Caminos Pavimentados**|**Tránsito de Vehículos por Caminos Pavimentados**|
|Transporte Material de Desarme|55,03|km/día|
|Transporte Residuos Varios|70,00||
|Transporte Riego Caminos|22,50||
|Transporte de Personal|70,00||
|Transporte de Supervisión|210,00||
|**Tránsito de Vehículos Livianos por Caminos No Pavimentados**|**Tránsito de Vehículos Livianos por Caminos No Pavimentados**|**Tránsito de Vehículos Livianos por Caminos No Pavimentados**|
|Transporte Personal de Cierre|7,50|km/día|
|Transporte Supervisión de Cierre|22,50|22,50|
|**Tránsito de Vehículos Pesados por Caminos No Pavimentados**(viajes/día)|**Tránsito de Vehículos Pesados por Caminos No Pavimentados**(viajes/día)|**Tránsito de Vehículos Pesados por Caminos No Pavimentados**(viajes/día)|
|Transporte Material de Desarme|5,90|km/día|
|Transporte Riego Caminos|22,50|22,50|
|Transporte Residuos Varios<br>|5,90|5,90|

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 56
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**9.** **MEDIDAS DE MITIGACIÓN CAMINOS**

Se considera como medida de mitigación de material particulado, el riego de caminos no pavimentados. A esta
medida se le asigna una efectividad en función al incremento en la humedad del camino que se consigue de
acuerdo a la siguiente expresión:

Ea = 75 * (M’ -1), para 1 ≤ M’ ≤ 2
Ea = 62 + 6.7 * (M’ -1), para 2 ≤ M’ ≤ 5

Donde M’ es el incremento promedio de la humedad del terreno medida en cantidad de veces.

La primera consideración tomada en cuenta, se relaciona con los fenómenos de humectación, los cuales ocurren
en la capa superior del camino, en un espesor no mayor de 2 cm.

La segunda consideración, se relaciona con la humectación inicial y final que se desea lograr. Por defecto se
considera una humedad de 6.5%, en consecuencia para aumentar al doble, se deberá realizar una humectación
que permita lograr un 13% final, es decir realizar un aumento neto de 6,5%.

Para determinar el volumen de agua que se requiere para incrementar la humedad del camino al doble, se
puede aplicar la siguiente fórmula:

**Va = [% Humedad * Mc] / Da**

Dónde:

Va : Volumen de agua
Mc: Masa del camino (ton/m2)
Da : Densidad del agua

Datos de entrada:

Longitud camino a regar: 3.750 m
Ancho camino a regar: 3 m

Área total resultante a regar: 11.250 m2

Densidad del material del camino: 1.8 ton/m3

Profundidad de la capa humectada: 2 cm por m2

Mc = Densidad del camino * Volumen de camino

Mc = 1.8 [ton/m3] * 0.02 [m3/m2] = 0,036 [ton/m2]

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 57
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

Va = [% Humedad * Mc] / Da
Va = [6.5/100] * 0.036 / 1
Va = 0.0023 m3 por m2 de camino a regar

Volumen de agua a incorporar para compensar la evaporación

Tasa de Evaporación: 2.500 mm al año (ref. M etodología para la estimación de recarga de cuencas altiplánicas y
precordilleranas de vertiente pacífica en el norte de Chile, XV, I, II y III regiones, Ministerio de Obras Públicas,
Dirección General de Aguas, Tabla 4-15, p.85)

Evaporación Horaria: (2.5/(365*24) = 0.00029 m3/m2h
Vrep (12 horas) = 0.00029*12= 0.00348 m3/m2
Volumen de agua requerida para lograr una eficiencia de 75% = Va + Vrep = 0.0023 m3/m2+ 0.00348 m3/m2

Lo anterior implica que para aumentar al doble la humectación de caminos, que ocupan un área total de 11.250
m2, se requiere un volumen de agua de 65 m3/día. Utilizando camiones de 15 m3 de capacidad, se requieren 4
regadíos diarios.

Conforme a lo anterior, la eficiencia de la medida propuesta se calcula en 75%

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 58
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**10.** **RESULTADOS INVENTARIO DE EMISIONES**

Las tablas siguientes muestran los resultados del inventario de emisiones.

**Tabla 36: Factores de Emisión (MP10, MP2.5 y MPS) - Actividades Fase de Construcción**

|ACTIVIDAD|Actividad Específica|Parámetros para<br>Factores de Emisión|Col4|Col5|Factor de<br>emisión<br>PM10|Factor de<br>emisión<br>PM2.5|Factor<br>emisión<br>MPS|
|---|---|---|---|---|---|---|---|
|**ACTIVIDAD**|**Actividad Específica**|**k10 **|**k2,5 **|**kMPS **|**kMPS **|**kMPS **|**kMPS **|
|Escarpe|Escarpe Área Total|0,75|0,105|1|4,2750|0,5985|5,7000|
|Excavaciones|Excavación totales|0,75|0,105|2,6|0,6086|0,0852|2,9750|
|Carguío y Volteo de<br>Camiones|Carga y descarga de material<br>de excavaciones|0,35|0,053|0,74|0,0003|0,0000|0,0007|
|Carguío y Volteo de<br>Camiones|Carga y descarga de material<br>para construcción de<br>parapetos (canchas de<br>nitratos y polvorines)|0,35|0,053|0,74|0,0003|0,0000|0,0007|
|Carguío y Volteo de<br>Camiones|Carga y descarga de áridos|0,35|0,053|0,74|0,0003|0,0000|0,0007|
|Carguío y Volteo de<br>Camiones|Carga y Descarga material<br>para rellenos|0,35|0,053|0,74|0,0003|0,0000|0,0007|
|Tránsito de Vehículos<br>por Caminos<br>Pavimentados|Transporte Materiales de<br>Construcción|0,62|0,15|3,23|0,0130|0,0031|0,0676|
|Tránsito de Vehículos<br>por Caminos<br>Pavimentados|Transporte Otros Materiales<br>de Construcción|0,62|0,15|3,23|0,0130|0,0031|0,0676|
|Tránsito de Vehículos<br>por Caminos<br>Pavimentados|Transporte Árido Para<br>Construcción|0,62|0,15|3,23|0,0130|0,0031|0,0676|
|Tránsito de Vehículos<br>por Caminos<br>Pavimentados|Transporte Hormigón|0,62|0,15|3,23|0,0130|0,0031|0,0676|
|Tránsito de Vehículos<br>por Caminos<br>Pavimentados|Transporte de H2O Potable|0,62|0,15|3,23|0,0130|0,0031|0,0676|
|Tránsito de Vehículos<br>por Caminos<br>Pavimentados|Transporte de Agua Industrial<br>Para Construcción y Riego|0,62|0,15|3,23|0,0130|0,0031|0,0676|
|Tránsito de Vehículos<br>por Caminos<br>Pavimentados|Transporte H2O Servidas|0,62|0,15|3,23|0,0130|0,0031|0,0676|
|Tránsito de Vehículos<br>por Caminos<br>Pavimentados|Transporte Residuos|0,62|0,15|3,23|0,0130|0,0031|0,0676|
|Tránsito de Vehículos<br>por Caminos<br>Pavimentados|Transporte Personal<br>Construcción Planta|0,62|0,15|3,23|0,0029|0,0007|0,0149|
|Tránsito de Vehículos<br>por Caminos<br>Pavimentados|Transporte Supervisión|0,62|0,15|3,23|0,0012|0,0003|0,0064|
|Transito Vehículos<br>Livianos por Caminos<br>No Pavimentados|Transporte Personal<br>Construcción Planta|1,5|0,15|4,9|0,2071|0,0207|0,6764|
|Transito Vehículos<br>Livianos por Caminos<br>No Pavimentados|Transporte Supervisión|1,5|0,15|4,9|0,2071|0,0207|0,6764|
|Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados|Transporte Materiales de<br>Construcción|1,5|0,15|4,9|0,8347|0,0835|2,9214|
|Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados|Transporte de material para<br>relleno y construcción de<br>parapetos|1,5|0,15|4,9|0,8347|0,0835|2,9214|
|Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados|Transporte Otros Materiales<br>de Construcción|1,5|0,15|4,9|0,8347|0,0835|2,9214|
|Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados|Transporte Árido Para<br>Construcción|1,5|0,15|4,9|0,8347|0,0835|2,9214|
|Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados|Transporte Hormigón|1,5|0,15|4,9|0,8347|0,0835|2,9214|
|Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados|Transporte de H2O Potable|1,5|0,15|4,9|0,8347|0,0835|2,9214|

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 59
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

|Col1|Transporte de Agua Industrial<br>Para Construcción y Riego|1,5|0,15|4,9|0,8347|0,0835|2,9214|
|---|---|---|---|---|---|---|---|
||Transporte H2O Servidas|1,5|0,15|4,9|0,8347|0,0835|2,9214|
||Transporte Residuos|1,5|0,15|4,9|0,8347|0,0835|2,9214|

**Tabla 37: Factores de Emisión (MP10, MP2.5 y MPS) - Actividades Fase de Operación**

|ACTIVIDAD|Actividad Específica|Parámetros para<br>Factores de Emisión|Col4|Col5|Factor de<br>emisión<br>PM10|Factor de<br>emisión<br>PM2.5|Factor<br>emisión<br>MPS|
|---|---|---|---|---|---|---|---|
|**ACTIVIDAD**|**Actividad Específica**|**k10 **|**k2,5 **|**kMPS **|**kMPS **|**kMPS **|**kMPS **|
|Tránsito por Caminos<br>Pavimentados|Transporte de agua potable|0,62|0,15|3,23|0,0121|0,0029|0,0631|
|Tránsito por Caminos<br>Pavimentados|Transporte de Agua<br>Industrial|0,62|0,15|3,23|0,0121|0,0029|0,0631|
|Tránsito por Caminos<br>Pavimentados|Transporte de Combustible<br>(Petróleo Diésel)|0,62|0,15|3,23|0,0121|0,0029|0,0631|
|Tránsito por Caminos<br>Pavimentados|Transporte de Materias<br>Primas|0,62|0,15|3,23|0,0121|0,0029|0,0631|
|Tránsito por Caminos<br>Pavimentados|Transporte de Producto<br>(Emulsión)|0,62|0,15|3,23|0,0121|0,0029|0,0631|
|Tránsito por Caminos<br>Pavimentados|Transporte de Producto<br>(Anfo)|0,62|0,15|3,23|0,0121|0,0029|0,0631|
|Tránsito por Caminos<br>Pavimentados|Transporte de Residuos|0,62|0,15|3,23|0,0121|0,0029|0,0631|
|Tránsito por Caminos<br>Pavimentados|Transporte Personal de<br>Operaciones|0,62|0,15|3,23|0,0029|0,0007|0,0149|
|Tránsito por Caminos<br>Pavimentados|Transporte Supervisores|0,62|0,15|3,23|0,0012|0,0003|0,0064|
|Transito Vehículos<br>Livianos por Caminos<br>No Pavimentados|Transporte Personal de<br>Operaciones|1,5|0,15|4,9|0,2071|0,0207|0,6764|
|Transito Vehículos<br>Livianos por Caminos<br>No Pavimentados|Transporte Supervisores|1,5|0,15|4,9|0,2071|0,0207|0,6764|
|Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados|Transporte de agua potable|1,5|0,15|4,9|0,8099|0,0810|2,8344|
|Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados|Transporte de Agua<br>Industrial|1,5|0,15|4,9|0,8099|0,0810|2,8344|
|Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados|Transporte de Combustible<br>(Petróleo Diésel)|1,5|0,15|4,9|0,8099|0,0810|2,8344|
|Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados|Transporte de Materias<br>Primas|1,5|0,15|4,9|0,8099|0,0810|2,8344|
|Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados|Transporte de Producto<br>(Emulsión)|1,5|0,15|4,9|0,8099|0,0810|2,8344|
|Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados|Transporte de Producto<br>(Anfo)|1,5|0,15|4,9|0,8099|0,0810|2,8344|
|Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados|Transporte Interno de<br>materias primas y productos|1,5|0,15|4,9|0,8099|0,0810|2,8344|
|Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados|Transporte de Residuos|1,5|0,15|4,9|0,8099|0,0810|2,8344|

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 60
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Tabla 38: Factores de Emisión (MP10, MP2.5 y MPS) - Actividades Fase de Cierre**

|ACTIVIDAD|Actividad Específica|Parámetros para<br>Factores de Emisión|Col4|Col5|Factor de<br>emisión<br>PM10|Factor de<br>emisión<br>PM2.5|Factor<br>emisión<br>MPS|
|---|---|---|---|---|---|---|---|
|**ACTIVIDAD**|**Actividad Específica**|**k10 **|**k2,5 **|**kMPS **|**kMPS **|**kMPS **|**kMPS **|
|Reperfilado|Reperfilamiento 10% del<br>Área total del Proyecto|0,75|0,105|1|4,2750|0,5985|5,7000|
|Tránsito por Caminos<br>Pavimentados"|Transporte Material de<br>Desarme|0,62|0,15|3,23|0,0085|0,0021|0,0445|
|Tránsito por Caminos<br>Pavimentados"|Transporte Residuos Varios|0,62|0,15|3,23|0,0085|0,0021|0,0445|
||Transporte Riego Caminos|0,62|0,15|3,23|0,0085|0,0021|0,0445|
||Transporte de Personal|0,62|0,15|3,23|0,0029|0,0007|0,0149|
||Transporte de Supervisión|0,62|0,15|3,23|0,0012|0,0003|0,0064|
|Transito Vehículos<br>Livianos por Caminos<br>No Pavimentados|Personal Cierre de Faena|1,5|0,15|4,9|0,2071|0,0207|0,6764|
|Transito Vehículos<br>Livianos por Caminos<br>No Pavimentados|Supervisión|1,5|0,15|4,9|0,2071|0,0207|0,6764|
|Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados|Transporte Material de<br>Desarme|1,5|0,15|4,9|0,6943|0,0694|2,4301|
|Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados|Transporte Riego Caminos|1,5|0,15|4,9|0,6943|0,0694|2,4301|
|Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados|Transporte Residuos Varios|1,5|0,15|4,9|0,6943|0,0694|2,4301|

**Tabla 39: Emisiones (MP10, MP2.5 y MPS) - Actividades Etapa de Construcción**

|ACTIVIDAD|Actividad Específica|Emisiones Diarias<br>(kg/día)|Col4|Col5|Emisiones Anuales<br>(ton/año)|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**ACTIVIDAD**|**Actividad Específica**|**PM10 **|**PM2.5 **|**MPS**|**PM10 **|**PM2.5 **|**MPS**|
|Escarpe|Escarpe Área Total|5,87|0,82|7,83|0,18|0,02|0,23|
|Excavaciones|Excavación totales|1,26|0,18|6,15|0,04|0,01|0,18|
|Carguío y Volteo de<br>Camiones|Carga y descarga de material de<br>excavaciones|0,03|0,01|0,07|0,00|0,00|0,00|
|Carguío y Volteo de<br>Camiones|Carga y descarga de material para<br>construcción de parapetos (canchas de<br>nitratos y polvorines)|0,75|0,11|1,59|0,02|0,00|0,05|
|Carguío y Volteo de<br>Camiones|Carga y descarga de áridos|0,01|0,00|0,01|0,00|0,00|0,00|
|Carguío y Volteo de<br>Camiones|Carga y Descarga material para rellenos|0,39|0,06|0,84|0,01|0,00|0,03|
|Tránsito de Vehículos<br>por Caminos<br>Pavimentados|Transporte Materiales de Construcción|0,68|0,17|3,57|0,12|0,03|0,64|
|Tránsito de Vehículos<br>por Caminos<br>Pavimentados|Transporte Otros Materiales de<br>Construcción|0,59|0,14|3,09|0,11|0,03|0,56|
|Tránsito de Vehículos<br>por Caminos<br>Pavimentados|Transporte Árido Para Construcción|0,48|0,12|2,52|0,03|0,01|0,15|
|Tránsito de Vehículos<br>por Caminos<br>Pavimentados|Transporte Hormigón|0,48|0,12|2,52|0,03|0,01|0,15|
|Tránsito de Vehículos<br>por Caminos<br>Pavimentados|Transporte de H2O Potable|0,48|0,12|2,52|0,09|0,02|0,45|
|Tránsito de Vehículos<br>por Caminos<br>Pavimentados|Transporte de Agua Industrial Para<br>Construcción y Riego|4,54|1,10|23,66|0,82|0,20|4,26|
|Tránsito de Vehículos<br>por Caminos<br>Pavimentados|Transporte H2O Servidas|0,91|0,22|4,73|0,16|0,04|0,85|
|Tránsito de Vehículos<br>por Caminos<br>Pavimentados|Transporte Residuos|0,50|0,12|2,63|0,09|0,02|0,47|
|Tránsito de Vehículos<br>por Caminos<br>Pavimentados|Transporte Personal Construcción<br>Planta|0,40|0,10|2,08|0,07|0,02|0,38|
|Tránsito de Vehículos<br>por Caminos<br>Pavimentados|Transporte Supervisión|0,34|0,08|1,79|0,06|0,01|0,32|
|Transito Vehículos|Transporte Personal Construcción|0,78|0,08|2,54|0,14|0,01|0,46|

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 61
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

|Livianos por Caminos<br>No Pavimentados|Planta|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|Livianos por Caminos<br>No Pavimentados|Transporte Supervisión|1,55|0,16|5,07|0,28|0,03|0,91|
|Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados|Transporte Materiales de Construcción|1,18|0,12|4,13|0,21|0,02|0,74|
|Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados|Transporte de material para relleno y<br>construcción de parapetos|7,72|0,77|27,03|1,39|0,14|4,86|
|Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados|Transporte Otros Materiales de<br>Construcción|1,02|0,10|3,58|0,18|0,02|0,64|
|Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados|Transporte Árido Para Construcción|0,83|0,08|2,92|0,05|0,01|0,18|
|Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados|Transporte Hormigón|0,83|0,08|2,92|0,05|0,01|0,18|
|Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados|Transporte de H2O Potable|0,83|0,08|2,92|0,15|0,02|0,53|
|Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados|Transporte de Agua Industrial Para<br>Construcción y Riego|7,83|0,78|27,39|1,41|0,14|4,93|
|Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados|Transporte H2O Servidas|2,25|0,23|7,89|0,41|0,04|1,42|
|Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados|Transporte Residuos|0,87|0,09|3,04|0,16|0,02|0,55|
|**TOTALES**|**TOTALES**|**43,45**|**6,03**|**155,03**|**6,26**|**0,86**|**24,12**|

**Tabla 40: Emisiones (MP10, MP2.5 y MPS) - Actividades Fase de Operación**

|ACTIVIDAD|Actividad Específica|Emisiones Diarias<br>(kg/día)|Col4|Col5|Emisiones Anuales<br>(ton/año)|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**ACTIVIDAD**|**Actividad Específica**|**PM10 **|**PM2.5 **|**MPS**|**PM10 **|**PM2.5 **|**MPS**|
|Tránsito por Caminos<br>Pavimentados|Transporte de agua potable|0,47|0,11|2,43|0,01|0,00|0,07|
|Tránsito por Caminos<br>Pavimentados|Transporte de Agua Industrial|1,70|0,41|8,84|0,05|0,01|0,27|
|Tránsito por Caminos<br>Pavimentados|Transporte de Combustible (Petróleo<br>Diésel)|0,51|0,12|2,68|0,02|0,00|0,08|
|Tránsito por Caminos<br>Pavimentados|Transporte de Materias Primas|5,42|1,31|28,24|0,16|0,04|0,85|
|Tránsito por Caminos<br>Pavimentados|Transporte de Producto (Emulsión)|6,60|1,60|34,36|0,20|0,05|1,03|
|Tránsito por Caminos<br>Pavimentados|Transporte de Producto (Anfo)|0,85|0,21|4,42|0,03|0,01|0,13|
|Tránsito por Caminos<br>Pavimentados|Transporte de Residuos|3,14|0,76|16,35|0,09|0,02|0,49|
|Tránsito por Caminos<br>Pavimentados|Transporte Personal de Operaciones|0,40|0,10|2,08|0,01|0,00|0,06|
|Tránsito por Caminos<br>Pavimentados|Transporte Supervisores|0,51|0,12|2,68|0,02|0,00|0,08|
|Transito Vehículos<br>Livianos por Caminos<br>No Pavimentados|Transporte Personal de Operaciones|0,78|0,08|2,54|0,02|0,00|0,08|
|Transito Vehículos<br>Livianos por Caminos<br>No Pavimentados|Transporte Supervisores|2,33|0,23|7,61|0,07|0,01|0,23|
|Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados|Transporte de agua potable|0,84|0,08|2,92|0,03|0,00|0,09|
|Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados|Transporte de Agua Industrial|3,04|0,30|10,63|0,09|0,01|0,32|
|Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados|Transporte de Combustible (Petróleo<br>Diésel)|0,92|0,09|3,22|0,03|0,00|0,10|
|Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados|Transporte de Materias Primas|9,70|0,97|33,97|0,29|0,03|1,02|
|Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados|Transporte de Producto (Emulsión)|11,81|1,18|41,34|0,35|0,04|1,24|
|Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados|Transporte de Producto (Anfo)|1,52|0,15|5,31|0,05|0,00|0,16|
|Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados|Transporte Interno de materias primas y<br>productos|9,70|0,97|33,97|0,29|0,03|1,02|
|Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados|Transporte de Residuos|5,62|0,56|19,66|0,17|0,02|0,59|
|**TOTALES**|**TOTALES**|**65,85**|**9,37**|**263,24**|**1,98**|**0,28**|**7,90**|

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 62
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Tabla 41: Emisiones (MP10, MP2.5 y MPS) - Actividades Fase de Cierre**

|ACTIVIDAD|Actividad Específica|Emisiones Diarias<br>(kg/día)|Col4|Col5|Emisiones Anuales<br>(ton/año)|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**ACTIVIDAD**|**Actividad Específica**|**PM10 **|**PM2.5 **|**MPS**|**PM10 **|**PM2.5 **|**MPS**|
|Reperfilado|Reperfilamiento 10% del Área total del<br>Proyecto|1,02|0,14|1,36|0,03|0,00|0,04|
|Tránsito por Caminos<br>Pavimentados"|Transporte Material de Desarme|0,47|0,11|2,45|0,08|0,02|0,44|
|Tránsito por Caminos<br>Pavimentados"|Transporte Residuos Varios|0,60|0,14|3,12|0,11|0,03|0,56|
|Tránsito por Caminos<br>Pavimentados"|Transporte Riego Caminos|0,19|0,05|1,00|0,03|0,01|0,18|
|Tránsito por Caminos<br>Pavimentados"|Transporte de Personal|0,20|0,05|1,04|0,04|0,01|0,19|
|Tránsito por Caminos<br>Pavimentados"|Transporte de Supervisión|0,26|0,06|1,34|0,05|0,01|0,24|
|Transito Vehículos<br>Livianos por Caminos<br>No Pavimentados|Personal Cierre de Faena|1,55|0,16|5,07|0,05|0,00|0,15|
|Transito Vehículos<br>Livianos por Caminos<br>No Pavimentados|Supervisión|4,66|0,47|15,22|0,14|0,01|0,46|
|Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados|Transporte Material de Desarme|1,02|0,10|3,58|0,18|0,02|0,64|
|Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados|Transporte Riego Caminos|3,91|0,39|13,67|0,70|0,07|2,46|
|Transito Vehículos<br>Pesados por Caminos<br>No Pavimentados|Transporte Residuos Varios|1,30|0,13|4,56|0,23|0,02|0,82|
|TOTALES|TOTALES|**15,18**|**1,80**|**52,41**|**1,65**|**0,21**|**6,19**|

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 63
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Tabla 42: Emisiones de Gases y MP Combustión de Motores [kg/día] - Fase de Construcción**

|Emisiones de Gases y Material Particulado Asociado a la Combustión de Motores [kg/día]|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Equipo**|**Cantidad**|**Potencia**<br>**Nominal kw**|**Operación**<br>**Diaria**<br>**(horas)**|**CO**|**HC**|**NOx**|**MP**|**MP10 **|**MP2,5 **|
|Bulldozer CAT modelo D5K o similar|1|72|15|0,08|0,03|0,22|0,02|0,02|0,02|
|Cargador frontal CAT modelo 924HZ o similar|1|106|30|0,11|0,05|0,43|0,04|0,04|0,04|
|Retroexcavadora CAT modelo 416F o similar|1|65|30|0,15|0,07|0,43|0,05|0,05|0,05|
|Compactador CAT Modelo CB-434D o similar|1|62|15|0,08|0,03|0,22|0,02|0,02|0,02|
|Motoniveladora CAT modelo 120M2 AWD o similar|1|108|15|0,06|0,03|0,22|0,02|0,02|0,02|
|Excavadora CAT modelo 315C o similar|1|82|30|0,11|0,07|0,43|0,05|0,05|0,05|
|**TOTAL FASE DE CONSTRUCCIÓN**|**TOTAL FASE DE CONSTRUCCIÓN**|**TOTAL FASE DE CONSTRUCCIÓN**|**TOTAL FASE DE CONSTRUCCIÓN**|**0,59**|**0,29**|**1,94**|**0,19**|**0,19**|**0,19**|

**Tabla 43: Emisiones de Gases y MP Combustión de Motores [kg/día] - Fase de Operación**

|Emisiones de Gases y Material Particulado Asociado a la Combustión de Motores [kg/día]|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Equipo**|**Cantidad**|**Potencia**<br>**Nominal kw**|**Operación**<br>**Diaria**<br>**(horas)**|**CO**|**HC**|**NOx**|**MP**|**MP10 **|**MP2,5 **|
|Grúa Horquilla|4|30|24|0,62|0,28|1,38|0,17|0,17|0,17|
|**TOTAL FASE DE OPERACIÓN**|**TOTAL FASE DE OPERACIÓN**|**TOTAL FASE DE OPERACIÓN**|**TOTAL FASE DE OPERACIÓN**|**0,62**|**0,28**|**1,38**|**0,17**|**0,17**|**0,17**|

**Tabla 44: Emisiones de Gases y MP Combustión de Motores [kg/día] - Fase de Cierre**

|Emisiones de Gases y Material Particulado Asociado a la Combustión de Motores [kg/día]|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Equipo**|**Cantidad**|**Potencia**<br>**Nominal kw**|**Operación**<br>**Diaria**<br>**(horas)**|**CO**|**HC**|**NOx**|**MP**|**MP10 **|**MP2,5 **|
|Bulldozer CAT modelo D5K o similar|1|72|15|0,08|0,03|0,22|0,02|0,02|0,02|
|Cargador frontal CAT modelo 924HZ o similar|1|106|30|0,11|0,05|0,43|0,04|0,04|0,04|
|**TOTAL FASE DE CIERRE**|**TOTAL FASE DE CIERRE**|**TOTAL FASE DE CIERRE**|**TOTAL FASE DE CIERRE**|**0,19**|**0,09**|**0,65**|**0,06**|**0,06**|**0,06**|

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 64
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Tabla 45: Emisiones de Gases y MP Asociado a Vehículos [kg/día] - Fase de Construcción**

|Vehículo|N°<br>Viajes/día|Distancia (km)|Col4|Velocidad km/h|Col6|CO|HC|NOx|MP|MP<br>10|MP<br>2,5|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Vehículo**|**N°**<br>**Viajes/día**|**CP**|**CNP**|**CP**|**CNP**|**CNP**|**CNP**|**CNP**|**CNP**|**CNP**|**CNP**|
|Transporte Materiales de Construcción|1|35|3,75|100|30|0,041|0,007|0,174|0,003|0,002|0,002|
|Transporte de material para relleno y<br>construcción de parapetos|19|35|1|100|30|0,508|0,095|2,550|0,050|0,001|0,001|
|Transporte Otros Materiales de Construcción|1|35|3,75|100|30|0,036|0,006|0,151|0,003|0,000|0,000|
|Transporte Árido Para Construcción|1|35|3,75|100|30|0,029|0,005|0,123|0,002|0,000|0,000|
|Transporte Hormigón|1|35|3,75|100|30|0,029|0,005|0,123|0,002|0,000|0,000|
|Transporte de H2O Potable|1|35|3,75|100|30|0,017|0,003|0,081|0,002|0,001|0,001|
|Transporte de Agua Industrial Para<br>Construcción y Riego|1|35|3,75|100|30|0,054|0,009|0,231|0,005|0,004|0,004|
|Transporte H2O Servidas|1|35|3,75|100|30|0,045|0,009|0,219|0,004|0,001|0,001|
|Transporte Residuos|1|35|3,75|100|30|0,017|0,003|0,085|0,002|0,001|0,001|
|Transporte Personal Construcción Planta|2|35|3,75|100|30|0,101|0,023|0,453|0,009|0,009|0,009|
|Transporte Supervisión|4|35|3,75|100|30|0,087|0,011|0,164|0,015|0,014|0,014|
|Transporte Materiales de Construcción|1|35|3,75|100|30|0,041|0,007|0,174|0,003|0,002|0,002|
|Transporte de material para relleno y<br>construcción de parapetos|19|35|1|100|30|0,508|0,095|2,550|0,050|0,001|0,001|
|Transporte Otros Materiales de Construcción|1|35|3,75|100|30|0,036|0,006|0,151|0,003|0,000|0,000|
|Transporte Árido Para Construcción|1|35|3,75|100|30|0,029|0,005|0,123|0,002|0,000|0,000|
|Transporte Hormigón|1|35|3,75|100|30|0,029|0,005|0,123|0,002|0,000|0,000|
|Transporte de H2O Potable|1|35|3,75|100|30|0,017|0,003|0,081|0,002|0,001|0,001|
|Transporte de Agua Industrial Para<br>Construcción y Riego|1|35|3,75|100|30|0,054|0,009|0,231|0,005|0,004|0,004|
|**TOTALES FASE DE CONSTRUCCIÓN**|**TOTALES FASE DE CONSTRUCCIÓN**|**TOTALES FASE DE CONSTRUCCIÓN**|**TOTALES FASE DE CONSTRUCCIÓN**|**TOTALES FASE DE CONSTRUCCIÓN**|**TOTALES FASE DE CONSTRUCCIÓN**|**0,965**|**0,176**|**4,355**|**0,098**|**0,034**|**0,034**|

CP: Camino Pavimentado - CNP: Camino No Pavimentado

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 65
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Tabla 46: Emisiones de Gases y MP Asociado a Vehículos [kg/día] - Etapa de Operación**

|Vehículo|N°<br>Viajes/día|Distancia (km)|Col4|Velocidad km/h|Col6|CO|HC|NOx|MP|MP<br>10|MP<br>2,5|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Vehículo**|**N°**<br>**Viajes/día**|**CP**|**CNP**|**CP**|**CNP**|**CNP**|**CNP**|**CNP**|**CNP**|**CNP**|**CNP**|
|Transporte de agua potable|1|35|3,75|100|30|0,017|0,003|0,084|0,002|0,001|0,001|
|Transporte de Agua Industrial|2|35|3,75|100|30|0,063|0,012|0,305|0,006|0,001|0,001|
|Transporte de Combustible (Petróleo Diésel)|1|35|3,75|100|30|0,033|0,006|0,140|0,003|0,002|0,002|
|Transporte de Materias primas|6|35|3,75|100|30|0,348|0,059|1,478|0,030|0,002|0,002|
|Transporte de Producto (Emulsión)|8|35|3,75|100|30|0,423|0,072|1,799|0,036|0,002|0,002|
|Transporte de Producto (Anfo)|1|35|3,75|100|30|0,054|0,009|0,231|0,005|0,002|0,002|
|Transporte de Residuos|6|35|3,75|100|30|0,200|0,038|0,974|0,019|0,001|0,001|
|Transporte Interno de materias primas y<br>productos|4|0|3|100|30|0,028|0,006|0,097|0,003|0,002|0,002|
|Transporte Personal de Operaciones|2|35|3,75|100|30|0,101|0,023|0,453|0,009|0,009|0,009|
|Transporte Supervisores|6|35|3,75|100|30|0,131|0,016|0,245|0,023|0,014|0,014|
|**TOTALES FASE DE OPERACIÓN**|**TOTALES FASE DE OPERACIÓN**|**TOTALES FASE DE OPERACIÓN**|**TOTALES FASE DE OPERACIÓN**|**TOTALES FASE DE OPERACIÓN**|**TOTALES FASE DE OPERACIÓN**|**1,40**|**0,24**|**5,81**|**0,13**|**0,04**|**0,04**|

**Tabla 47: Emisiones de Gases y MP Asociado a Vehículos [kg/día] - Etapa de Cierre**

|Vehículo|N°<br>Viajes/día|Distancia (km)|Col4|Velocidad km/h|Col6|CO|HC|NOx|MP|MP<br>10|MP<br>2,5|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Vehículo**|**N°**<br>**Viajes/día**|**CP**|**CNP**|**CP**|**CNP**|**CNP**|**CNP**|**CNP**|**CNP**|**CNP**|**CNP**|
|Transporte Material de Desarme|1|35|3,75|100|30|0,043|0,007|0,182|0,004|0,002|0,002|
|Transporte Residuos Varios|1|35|3,75|100|30|0,043|0,007|0,182|0,004|0,002|0,002|
|Transporte Riego Caminos|3|35|3,75|100|30|0,094|0,018|0,457|0,009|0,001|0,001|
|Transporte Personal de Cierre|1|35|3,75|100|30|0,051|0,012|0,226|0,005|0,009|0,009|
|Transporte Supervisores|3|35|3,75|100|30|0,065|0,008|0,123|0,012|0,014|0,014|
|**TOTALES FASE DE CIERRE**|**TOTALES FASE DE CIERRE**|**TOTALES FASE DE CIERRE**|**TOTALES FASE DE CIERRE**|**TOTALES FASE DE CIERRE**|**TOTALES FASE DE CIERRE**|**0,296**|**0,052**|**1,170**|**0,033**|**0,027**|**0,027**|

**Tabla 48: Emisiones de Gases y Material Particulado Asociado a Combustión en Grupos Generadores**

|Fase Proyecto|Potencia<br>(kw)|Combustibles<br>(tipo)|Operación<br>(h/día)|Cantidad|MP|MP10|MP2,5|CO|NOx|SOx|
|---|---|---|---|---|---|---|---|---|---|---|
|Construcción|24|Diésel|24,00|2,00|1,54|1,54|1,54|4,68|21,66|1,44|
|Operación|0|0|0|0|0,00|0,00|0,00|0,00|0,00|0,00|
|Cierre|12|Diésel|24,00|1,00|0,39|0,39|0,39|1,17|5,41|0,36|

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 66
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**TABLAS RESUMEN DE EMISIONES POR FASES DEL PROYECTO**

**Tabla 49: Resumen Emisiones Fase de Construcción**

|Fase de Construcción|MP10|Col3|MP2,5|Col5|MPS|Col7|CO|Col9|HC|Col11|NOx|Col13|SO<br>X|Col15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Fase de Construcción**|**kg/día**|**ton/año**|**kg/día**|**ton/año**|**kg/día**|**ton/año**|**kg/día**|**ton/año**|**kg/día**|**ton/año**|**kg/día**|**ton/año**|**kg/día**|**ton/año**|
|Actividades|43,45|6,26|6,03|0,86|155,03|21,15|---|---|---|---|---|---|---|---|
|Maquinarias|0,19|0,01|0,19|0,01|0,19|0,01|0,59|0,02|0,29|0,01|1,94|0,06|---|---|
|Vehículos|0,03|0,01|0,03|0,01|0,10|0,02|0,97|0,17|0,18|0,03|4,36|0,78|---|---|
|Generadores|1,54|0,28|1,54|0,28|1,54|0,28|4,68|0,84|---|---|21,66|3,90|1,44|0,26|
|**TOTAL**|**45,21**|**6,55**|**7,79**|**1,15**|**156,86**|**21,45**|**6,24**|**1,03**|**0,47**|**0,04**|**27,96**|**4,74**|**1,44**|**0,26**|

**Tabla 50: Resumen Emisiones Fase de Operación**

|Fase de Construcción|MP10|Col3|MP2,5|Col5|MPS|Col7|CO|Col9|HC|Col11|NOx|Col13|SO<br>X|Col15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Fase de Construcción**|**kg/día**|**ton/año**|**kg/día**|**ton/año**|**kg/día**|**ton/año**|**kg/día**|**ton/año**|**kg/día**|**ton/año**|**kg/día**|**ton/año**|**kg/día**|**ton/año**|
|Actividades|65,85|1,98|9,37|0,28|263,24|7,90|---|---|---|---|---|---|---|---|
|Maquinarias|1,17|0,43|1,17|0,43|1,17|0,43|0,62|0,23|0,28|0,10|1,38|0,50|---|---|
|Vehículos|0,04|0,01|0,04|0,01|0,13|0,05|1,40|0,51|0,24|0,09|5,81|2,12|---|---|
|Caldera|1,82|0,66|0,91|0,33|1,82|0,66|0,26|0,09|---|---|4,62|1,69|0,65|0,24|
|**TOTAL**|**68,88**|**3,09**|**11,49**|**1,05**|**266,36**|**9,04**|**2,28**|**0,83**|**0,52**|**0,19**|**11,81**|**4,31**|**0,65**|**0,24**|

**Tabla 51: Resumen Emisiones Fase de Cierre**

|Fase de Construcción|MP10|Col3|MP2,5|Col5|MPS|Col7|CO|Col9|HC|Col11|NOx|Col13|SO<br>X|Col15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Fase de Construcción**|**kg/día**|**ton/año**|**kg/día**|**ton/año**|**kg/día**|**ton/año**|**kg/día**|**ton/año**|**kg/día**|**ton/año**|**kg/día**|**ton/año**|**kg/día**|**ton/año**|
|Actividades|15,18|1,65|1,80|0,21|52,41|6,19|---|---|---|---|---|---|---|---|
|Maquinarias|0,06|0,00|0,06|0,00|0,06|0,00|0,19|0,01|0,09|0,00|0,65|0,02|---|---|
|Vehículos|0,03|0,00|0,03|0,00|0,03|0,01|0,30|0,05|0,05|0,01|1,17|0,21|---|---|
|Generadores|0,39|0,07|0,39|0,07|0,39|0,07|1,17|0,21|---|---|5,41|0,97|0,36|0,06|
|**TOTAL**|**15,66**|**1,73**|**2,28**|**0,29**|**52,89**|**6,27**|**1,66**|**0,27**|**0,14**|**0,01**|**7,23**|**1,20**|**0,36**|**0,06**|

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 67
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**11.** **RESULTADOS DE LA MODELACIÓN**

Mediante la aplicación del modelo CALPUFF fue posible obtener las concentraciones de material particulado
respirable (MP 10 ), material particulado respirable fino (MP 2,5 ), material particulado sedimentable (MPS), y
concentraciones de gases (SO 2, NOx, CO y HC), que aportará el Proyecto en cada una de sus fases
(construcción, operación y cierre). A continuación se presentan los resultados del modelo, análisis de los
resultados y mapas de Isoconcentración.

**11.1 Resultados del Modelo**

Las siguientes tablas resúmenes, presentan los resultados obtenidos de la modelación para cada fase del
proyecto. Cabe señalar, que no se ha realizado el análisis de cumplimiento de la normativa para material
particulado MP 2.5 ni MPS, debido a que no se cuenta con registros de línea de base para dichos contaminante.

**11.1.1 Cumplimiento Normas de Calidad Ambiental Primaria**

Las siguientes tablas presentan las concentraciones de cada contaminante en cada uno de los receptores y su
nivel respecto de la norma respectiva:

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 68
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Tabla 52: Aportes del Proyecto Etapa de Construcción**

|Parámetro|Estadístico|Limite<br>Norma<br>(μg/m3N)|Concentración<br>(μg/m3N)<br>Receptor R1|%<br>Respecto<br>de la<br>Norma|Concentración<br>(μg/m3N)<br>Receptor R2|%<br>Respecto<br>de la<br>Norma|Concentración<br>(μg/m3N)<br>Receptor R3|%<br>Respecto<br>de la<br>Norma|
|---|---|---|---|---|---|---|---|---|
|MP10|Percentil 98 Promedio 24 horas|150|1.3155E-02|0,0|1.4254E-01|0,1|5.7171E-02|0,0|
|MP10|Promedio Anual|50|3.1842E-03|0,0|2.4825E-02|0,0|1.3341E-02|0,0|
|MP2,5|Percentil 98 Promedio Diario|50|2.4289E-03|0,0|2.9371E-02|0,1|1.2303E-02|0,0|
|MP2,5|Promedio Trianual|20|5.8081E-04|0,0|5.3983E-03|0,0|3.1806E-03|0,0|
|CO|Percentil 99, máx. 1 hora|30000|2.1765E-02|0,0|4.1358E-01|0,0|1.3078E-01|0,0|
|CO|Percentil 99, máx. 8 hora|10000|6.1757E-03|0,0|6.0662E-02|0,0|1.8508E-02|0,0|
|NO2|Percentil 99, máx. 1 hora|400|6.3795E-03|0,0|1.2543E-01|0,0|4.5199E-02|0,0|
|NO2|Promedio, Anual|100|2.2116E-04|0,0|6.2973E-04|0,0|1.7340E-04|0,0|
|SO2|Promedio Diario, percentil 99|250|4.9733E-04|0,0|4.3611E-03|0,0|1.9543E-03|0,0|

**Tabla 53: Aportes del Proyecto Etapa de Operación**

|Parámetro|Estadístico|Limite<br>Norma<br>(μg/m3N)|Concentración<br>(μg/m3N)<br>Receptor R1|%<br>Respecto<br>de la<br>Norma|Concentración<br>(μg/m3N)<br>Receptor R2|%<br>Respecto<br>de la<br>Norma|Concentración<br>(μg/m3N)<br>Receptor R3|%<br>Respecto<br>de la<br>Norma|
|---|---|---|---|---|---|---|---|---|
|MP10|Percentil 98 Promedio 24 horas|150|9.0914E-03|0,0|4.7899E-01|0,3|2.7619E-01|0,2|
|MP10|Promedio Anual|50|2.4207E-03|0,0|1.0734E-01|0,2|7.6398E-02|0,2|
|MP2,5|Percentil 98 Promedio Diario|50|1.2288E-03|0,0|1.1392E-01|0,2|6.5819E-02|0,1|
|MP2,5|Promedio Trianual|20|3.4733E-04|0,0|2.5146E-02|0,1|1.8298E-02|0,1|
|CO|Percentil 99, máx. 1 hora|30000|3.4157E-04|0,0|5.7060E-03|0,0|2.1247E-03|0,0|
|CO|Percentil 99, máx. 8 hora|10000|9.6569E-05|0,0|8.3185E-04|0,0|2.9792E-04|0,0|
|NO2|Percentil 99, máx. 1 hora|400|5.2153E-04|0,0|1.1042E-02|0,0|3.5428E-03|0,0|
|NO2|Promedio, Anual|100|1.8547E-05|0,0|5.8313E-05|0,0|1.4703E-05|0,0|
|SO2|Promedio Diario, percentil 99|250|9.1351E-06|0,0|8.0107E-05|0,0|3.5897E-05|0,0|

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 69
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Tabla 54: Aportes del Proyecto Etapa de Cierre**

|Parámetro|Estadístico|Limite<br>Norma<br>(μg/m3N)|Concentración<br>(μg/m3N)<br>Receptor R1|%<br>Respecto<br>de la<br>Norma|Concentración<br>(μg/m3N)<br>Receptor R2|%<br>Respecto<br>de la<br>Norma|Concentración<br>(μg/m3N)<br>Receptor R3|%<br>Respecto<br>de la<br>Norma|
|---|---|---|---|---|---|---|---|---|
|MP10|Percentil 98 Promedio 24 horas|150|3.8186E-03|0,0|4.8393E-02|0,0|1.8999E-02|0,0|
|MP10|Promedio Anual|50|9.3101E-04|0,0|8.5522E-03|0,0|4.9495E-03|0,0|
|MP2,5|Percentil 98 Promedio Diario|50|1.7551E-03|0,0|1.7081E-02|0,0|6.9109E-03|0,0|
|MP2,5|Promedio Trianual|20|4.1729E-04|0,0|2.6432E-03|0,0|1.3706E-03|0,0|
|CO|Percentil 99, máx. 1 hora|30000|3.8580E-02|0,0|6.2226E-01|0,0|2.3259E-01|0,0|
|CO|Percentil 99, máx. 8 hora|10000|1.0944E-02|0,0|9.5579E-02|0,0|3.1790E-02|0,0|
|NO2|Percentil 99, máx. 1 hora|400|4.5705E-05|0,0|8.4182E-03|0,0|2.9319E-04|0,1|
|NO2|Promedio, Anual|100|1.5837E-06|0,0|4.4271E-06|0,0|1.2499E-06|0,0|
|SO2|Promedio Diario, percentil 99|250|4.9733E-04|0,0|4.3611E-03|0,0|1.9543E-03|0,0|

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 70
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**11.1.2 Cumplimiento Normas de Calidad Ambiental Secundaria**

**Tabla 55: Aportes del Proyecto Etapa de Construcción**

|Parámetro|Estadístico|Limite<br>Norma<br>(μg/m3N)|Concentración<br>(μg/m3N)<br>Receptor R1|%<br>Respecto<br>de la<br>Norma|Concentración<br>(μg/m3N)<br>Receptor R2|%<br>Respecto<br>de la<br>Norma|Concentración<br>(μg/m3N)<br>Receptor R3|%<br>Respecto<br>de la<br>Norma|
|---|---|---|---|---|---|---|---|---|
|MPS|Promedio Mensual|150|3.6090E-06|0,0|2.0141E-05|0,0|1.0122E-05|0,0|
|MPS|Promedio Anual|50|7.6163E-07|0,0|5.6058E-06|0,0|3.0713E-06|0,0|
|SO2|Promedio Anual|50|1.4248E-04|0,0|3.9239E-04|0,0|1.1823E-04|0,0|
|SO2|Percentil 99.7 Conc. Diaria|20|4.9733E-04|0,0|4.3611E-03|0,0|1.9543E-03|0,0|
|SO2|Percentil 99.73 Conc. 1 hora|30000|4.9733E-04|0,0|4.3611E-03|0,0|1.9543E-03|0,0|

**Tabla 56: Aportes del Proyecto Etapa de Operación**

|Parámetro|Estadístico|Limite<br>Norma<br>(μg/m3N)|Concentración<br>(μg/m3N)<br>Receptor R1|%<br>Respecto<br>de la<br>Norma|Concentración<br>(μg/m3N)<br>Receptor R2|%<br>Respecto<br>de la<br>Norma|Concentración<br>(μg/m3N)<br>Receptor R3|%<br>Respecto<br>de la<br>Norma|
|---|---|---|---|---|---|---|---|---|
|MPS|Promedio Mensual|150|4.3922E-06|0,0|1.0331E-04|0,0|6.0299E-05|0,0|
|MPS|Promedio Anual|50|9.9611E-07|0,0|3.3152E-05|0,0|1.9603E-05|0,0|
|SO2|Promedio Anual|50|2.6172E-06|0,0|7.2075E-06|0,0|2.1718E-06|0,0|
|SO2|Percentil 99.7 Conc. Diaria|20|9.1351E-06|0,0|8.0107E-05|0,0|3.5897E-05|0,0|
|SO2|Percentil 99.73 Conc. 1 hora|30000|9.1351E-06|0,0|8.0107E-05|0,0|3.5897E-05|0,0|

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 71
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Tabla 57: Aportes del Proyecto Etapa de Cierre**

|Parámetro|Estadístico|Limite<br>Norma<br>(μg/m3N)|Concentración<br>(μg/m3N)<br>Receptor R1|%<br>Respecto<br>de la<br>Norma|Concentración<br>(μg/m3N)<br>Receptor R2|%<br>Respecto<br>de la<br>Norma|Concentración<br>(μg/m3N)<br>Receptor R3|%<br>Respecto<br>de la<br>Norma|
|---|---|---|---|---|---|---|---|---|
|MPS|Promedio Mensual|150|9.5607E-07|0,0|6.9136E-06|0,0|3.7460E-06|0,0|
|MPS|Promedio Anual|50|2.0358E-07|0,0|2.0600E-06|0,0|1.1654E-06|0,0|
|SO2|Promedio Anual|50|1.4248E-04|0,0|3.9239E-04|0,0|1.1823E-04|0,0|
|SO2|Percentil 99.7 Conc. Diaria|20|9.6468E-05|0,0|1.0409E-04|0,0|9.4402E-05|0,0|
|SO2|Percentil 99.73 Conc. 1 hora|30000|4.9733E-04|0,0|4.3611E-03|0,0|1.9543E-03|0,0|

Nota 1: Tablas 55, 56 y 57 los aportes de MPS en cada uno de los receptores, se expresan en mg/m [2] día
Nota 2: Tablas 55, 56 y 57 los aportes de SO 2 en cada uno de los receptores, se expresan en μg/m [3] N

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 72
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**12.** **ANÁLISIS DE INCERTIDUMBRE**

**12.1 Análisis cualitativo de los campos de vientos**

Respecto de la dirección de los vientos en la estaciones, no existen mayores diferencias entre lo observado y lo

modelado.

De acuerdo con la información presentada en el apartado 3.3 (Campos de Vientos), los campos de vientos
provienen principalmente de la dirección SW.

Al comparar los datos anteriores con los campos de vientos generados por el modelo utilizando meteorología
WRF, se aprecia que existe bastante similitud con el modelo de pronóstico.

Conforme a lo anterior, se puede concluir que en gran parte del día coinciden las direcciones de los vientos.

A partir de lo anterior se puede sostener que el modelo meteorológico predice de buena forma el
comportamiento espacial de los flujos de viento, ya que las diferencias entre las direcciones del viento se
manejan en un rango aceptable de variación.

**12.2 Análisis cuantitativo para el cálculo de incertidumbre**

El análisis cuantitativo consiste en determinar el % de variación que experimenta la velocidad promedio del

viento entre los valores utilizados en el modelo versus los valores observados de velocidad del viento.

De acuerdo a los datos registrados en la Estación Cerro Moreno, la velocidad promedio del viento registrada por
dicha estación, (considerando un universo de 8.311 datos, que representan el 94.8% del total de datos del año
2015), es de 3.6 m/s

Al modelar con WRF en el punto de localización de la Estación Cerro Moreno, el modelo arroja un valor
promedio de velocidad del viento para el mismo período de 3.35 m/s

Las velocidades promedios registradas en las estaciones de monitoreo (valor observado) versus las
representadas por el modelo (valor modelado) se tiene que:

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 73
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Tabla 58: Velocidad promedio del Viento en m/s**

|Estación|Promedio Observado|Promedio Pronostico WRF|% de Variación|
|---|---|---|---|
|Cerro Moreno|3,6|2,5||

_% Error_
_V_ = % de error entre los valores modelado y observado de la velocidad del viento.

(Valor modelado) = 2,53 m/s
(Valor observado) = 3,61 m/s

2,53 (m/s) - 3,61 (m/s)
% de Error = [x] 100

3,61 (m/s)

% de Error = 29,92%

Conforme a lo anterior, se observa que el modelo subestima las velocidades de los vientos con respecto a los
datos observados de la Estación Cerro Moreno y por lo tanto subestima las emisiones en un 29,92%

**12.3 Ajuste Emisiones del Proyecto**

Conforme al error determinado en la aplicación del modelo, se corrigen los valores presentados en las tablas 52
a la 57, aplicando un factor de corrección de 1,2992

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 74
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Tabla 59: Aportes del Proyecto Etapa de Construcción con aplicación de factor de corrección**

|Parámetro|Estadístico|Limite<br>Norma<br>(μg/m3N)|Concentración<br>(μg/m3N)<br>Receptor R1|%<br>Respecto<br>de la<br>Norma|Concentración<br>(μg/m3N)<br>Receptor R2|%<br>Respecto<br>de la<br>Norma|Concentración<br>(μg/m3N)<br>Receptor R3|%<br>Respecto<br>de la<br>Norma|
|---|---|---|---|---|---|---|---|---|
|MP10|Percentil 98 Promedio 24 horas|150|1,71E-02|0,0|1,85E-01|0,1|7,43E-02|0,0|
|MP10|Promedio Anual|50|4,14E-03|0,0|3,23E-02|0,1|1,73E-02|0,0|
|MP2,5|Percentil 98 Promedio Diario|50|3,16E-03|0,0|3,82E-02|0,1|1,60E-02|0,0|
|MP2,5|Promedio Trianual|20|7,55E-04|0,0|7,01E-03|0,0|4,13E-03|0,0|
|CO|Percentil 99, máx. 1 hora|30000|2,83E-02|0,0|5,37E-01|0,0|1,70E-01|0,0|
|CO|Percentil 99, máx. 8 hora|10000|8,02E-03|0,0|7,88E-02|0,0|2,40E-02|0,0|
|NO2|Percentil 99, máx. 1 hora|400|8,29E-03|0,0|1,63E-01|0,0|5,87E-02|0,0|
|NO2|Promedio, Anual|100|2,87E-04|0,0|8,18E-04|0,0|2,25E-04|0,0|
|SO2|Promedio Diario, percentil 99|250|6,46E-04|0,0|5,67E-03|0,0|2,54E-03|0,0|

**Tabla 60: Aportes del Proyecto Etapa de Operación con aplicación de factor de corrección**

|Parámetro|Estadístico|Limite<br>Norma<br>(μg/m3N)|Concentración<br>(μg/m3N)<br>Receptor R1|%<br>Respecto<br>de la<br>Norma|Concentración<br>(μg/m3N)<br>Receptor R2|%<br>Respecto<br>de la<br>Norma|Concentración<br>(μg/m3N)<br>Receptor R3|%<br>Respecto<br>de la<br>Norma|
|---|---|---|---|---|---|---|---|---|
|MP10|Percentil 98 Promedio 24 horas|150|1,18E-02|0,0|6,22E-01|0,4|3,59E-01|0,2|
|MP10|Promedio Anual|50|3,14E-03|0,0|1,39E-01|0,3|9,93E-02|0,2|
|MP2,5|Percentil 98 Promedio Diario|50|1,60E-03|0,0|1,48E-01|0,3|8,55E-02|0,2|
|MP2,5|Promedio Trianual|20|4,51E-04|0,0|3,27E-02|0,2|2,38E-02|0,1|
|CO|Percentil 99, máx. 1 hora|30000|4,44E-04|0,0|7,41E-03|0,0|2,76E-03|0,0|
|CO|Percentil 99, máx. 8 hora|10000|1,25E-04|0,0|1,08E-03|0,0|3,87E-04|0,0|
|NO2|Percentil 99, máx. 1 hora|400|6,78E-04|0,0|1,43E-02|0,0|4,60E-03|0,0|
|NO2|Promedio, Anual|100|2,41E-05|0,0|7,58E-05|0,0|1,91E-05|0,0|
|SO2|Promedio Diario, percentil 99|250|1,19E-05|0,0|1,04E-04|0,0|4,66E-05|0,0|

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 75
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Tabla 61: Aportes del Proyecto Etapa de Cierre con aplicación de factor de corrección**

|Parámetro|Estadístico|Limite<br>Norma<br>(μg/m3N)|Concentración<br>(μg/m3N)<br>Receptor R1|%<br>Respecto<br>de la<br>Norma|Concentración<br>(μg/m3N)<br>Receptor R2|%<br>Respecto<br>de la<br>Norma|Concentración<br>(μg/m3N)<br>Receptor R3|%<br>Respecto<br>de la<br>Norma|
|---|---|---|---|---|---|---|---|---|
|MP10|Percentil 98 Promedio 24 horas|150|4,96E-03|0,0|6,29E-02|0,0|2,47E-02|0,0|
|MP10|Promedio Anual|50|1,21E-03|0,0|1,11E-02|0,0|6,43E-03|0,0|
|MP2,5|Percentil 98 Promedio Diario|50|2,28E-03|0,0|2,22E-02|0,0|8,98E-03|0,0|
|MP2,5|Promedio Trianual|20|5,42E-04|0,0|3,43E-03|0,0|1,78E-03|0,0|
|CO|Percentil 99, máx. 1 hora|30000|5,01E-02|0,0|8,08E-01|0,0|3,02E-01|0,0|
|CO|Percentil 99, máx. 8 hora|10000|1,42E-02|0,0|1,24E-01|0,0|4,13E-02|0,0|
|NO2|Percentil 99, máx. 1 hora|400|5,62E-05|0,0|1,03E-02|0,0|3,60E-04|0,0|
|NO2|Promedio, Anual|100|1,95E-06|0,0|5,44E-06|0,0|1,54E-06|0,0|
|SO2|Promedio Diario, percentil 99|250|6,46E-04|0,0|5,67E-03|0,0|2,54E-03|0,0|

**Tabla 62: Aportes del Proyecto Etapa de Construcción con aplicación de factor de corrección**

|Parámetro|Estadístico|Limite<br>Norma<br>(μg/m3N)|Concentración<br>(μg/m3N)<br>Receptor R1|%<br>Respecto<br>de la<br>Norma|Concentración<br>(μg/m3N)<br>Receptor R2|%<br>Respecto<br>de la<br>Norma|Concentración<br>(μg/m3N)<br>Receptor R3|%<br>Respecto<br>de la<br>Norma|
|---|---|---|---|---|---|---|---|---|
|MPS|Promedio Mensual|150|4,69E-06|0,0|2,62E-05|0,0|1,32E-05|0,0|
|MPS|Promedio Anual|50|9,90E-07|0,0|7,28E-06|0,0|3,99E-06|0,0|
|SO2|Promedio Anual|50|1,85E-04|0,0|5,10E-04|0,0|1,54E-04|0,0|
|SO2|Percentil 99.7 Conc. Diaria|20|6,46E-04|0,0|5,67E-03|0,0|2,54E-03|0,0|
|SO2|Percentil 99.73 Conc. 1 hora|30000|6,46E-04|0,0|5,67E-03|0,0|2,54E-03|0,0|

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 76
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Tabla 63 Aportes del Proyecto Etapa de Operación con aplicación de factor de corrección**

|Parámetro|Estadístico|Limite<br>Norma<br>(μg/m3N)|Concentración<br>(μg/m3N)<br>Receptor R1|%<br>Respecto<br>de la<br>Norma|Concentración<br>(μg/m3N)<br>Receptor R2|%<br>Respecto<br>de la<br>Norma|Concentración<br>(μg/m3N)<br>Receptor R3|%<br>Respecto<br>de la<br>Norma|
|---|---|---|---|---|---|---|---|---|
|MPS|Promedio Mensual|150|5,71E-06|0,0|1,34E-04|0,0|7,83E-05|0,0|
|MPS|Promedio Anual|50|1,29E-06|0,0|4,31E-05|0,0|2,55E-05|0,0|
|SO2|Promedio Anual|50|3,40E-06|0,0|9,36E-06|0,0|2,82E-06|0,0|
|SO2|Percentil 99.7 Conc. Diaria|20|1,19E-05|0,0|1,04E-04|0,0|4,66E-05|0,0|
|SO2|Percentil 99.73 Conc. 1 hora|30000|1,19E-05|0,0|1,04E-04|0,0|4,66E-05|0,0|

**Tabla 64 Aportes del Proyecto Etapa de Cierre con aplicación de factor de corrección**

|Parámetro|Estadístico|Limite<br>Norma<br>(μg/m3N)|Concentración<br>(μg/m3N)<br>Receptor R1|%<br>Respecto<br>de la<br>Norma|Concentración<br>(μg/m3N)<br>Receptor R2|%<br>Respecto<br>de la<br>Norma|Concentración<br>(μg/m3N)<br>Receptor R3|%<br>Respecto<br>de la<br>Norma|
|---|---|---|---|---|---|---|---|---|
|MPS|Promedio Mensual|150|1,24E-06|0,0|8,98E-06|0,0|4,87E-06|0,0|
|MPS|Promedio Anual|50|2,64E-07|0,0|2,68E-06|0,0|1,51E-06|0,0|
|SO2|Promedio Anual|50|1,85E-04|0,0|5,10E-04|0,0|1,54E-04|0,0|
|SO2|Percentil 99.7 Conc. Diaria|20|1,25E-04|0,0|1,35E-04|0,0|1,23E-04|0,0|
|SO2|Percentil 99.73 Conc. 1 hora|30000|6,46E-04|0,0|5,67E-03|0,0|2,54E-03|0,0|

Nota 1: Tablas 62, 63 y 64 los aportes de MPS en cada uno de los receptores, se expresan en mg/m [2] día
Nota 2: Tablas 62, 63 y 64 los aportes de SO 2 en cada uno de los receptores, se expresan en μg/m [3] N

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 77
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**13.** **ANÁLISIS DE CUMPLIMIENTO NORMATIVO VIGENTE**

El presente estudio de dispersión de emisiones atmosféricas ha considerado 3 receptores de interés
(asentamientos humanos) localizados en el entorno al área del proyecto. Sobre estos receptores se ha
determinado el nivel de impacto que generara el proyecto en cada una de sus fases.

**13.1 Análisis de Cumplimiento Normativo Vigente Para MP10**

Se puede observar que el proyecto, en ninguna de sus fases genera impactos significativos sobre la calidad del
aire por MP10. El mayor impacto se genera durante la fase de operación sobre el receptor número 2 con 0,62
μg/m [3] N como promedio de 24 horas, lo que representa un 0,4% respecto del valor de la norma.

**13.2 Análisis de Cumplimiento Normativo Vigente Para Mp2,5**

Se puede observar que el proyecto, en ninguna de sus fases genera impactos significativos sobre la calidad del
aire por MP2,5. El mayor impacto se genera durante la fase de operación sobre el receptor número 2 con 0,14
μg/m [3] N como promedio de 24 horas, lo que representa un 0,3% respecto del valor de la norma.

**13.3 Análisis de Cumplimiento Normativo Vigente Para MPS**

No existen zonas biológicas de interés cercanas al área del proyecto por lo que se han defino como receptores
biológicos los mismos receptores humanos anteriormente analizados. Respecto de ello se puede señalar que no
existe impacto sobre alguno de ellos ya que todos los valores son extremadamente bajos, representando un nulo
aporte (0,0% respecto del valor de la norma).

**13.4 Análisis de Cumplimiento Normativo Vigente Para Gases CO**

Se puede observar que el proyecto, en ninguna de sus fases genera impactos significativos sobre la calidad del
aire por CO en los receptores analizados ya que todos los valores son extremadamente bajos, representando un
nulo aporte (0,0% respecto del valor de la norma) en cada uno de ellos.

**13.5 Análisis de Cumplimiento Normativo Vigente Para Gases NO** **2**

Se puede observar que el proyecto, en ninguna de sus fases genera impactos significativos sobre la calidad del

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 78
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

aire por NO 2 en los receptores analizados ya que todos los valores son extremadamente bajos, representando
un nulo aporte (0,0% respecto del valor de la norma) en cada uno de ellos.

**13.6 Análisis de Cumplimiento Normativo Vigente Para Gases SO** **2**

Se puede observar que el proyecto, en ninguna de sus fases genera impactos significativos sobre la calidad del
aire por SO 2 en los receptores analizados ya que todos los valores son extremadamente bajos, representando un
nulo aporte (0,0% respecto del valor de la norma) en cada uno de ellos.

**13.7 Puntos de Máximo Impacto**

De acuerdo con los resultados de la modelación, los puntos de máximo impacto generados por el proyecto, en
cada una de sus fases, se presentan en las siguientes tablas, indicando ubicación en coordenadas UTM WGS84 Huso 19S y concentración máxima:

**Tabla 65: Puntos de Máximo Impacto - Fase de Construcción**

|Parámetro|Estadístico|Coordenada WGS-84|Col4|Concentración<br>(μg/m3N)|
|---|---|---|---|---|
|**Parámetro**|**Estadístico**|**Este**|**Norte**|**Norte**|
|MP10|Percentil 98 Promedio 24 horas|359.500|7.414.375|56,31|
|MP10|Promedio Anual|359.500|7.414.375|25,2|
|MP2,5|Percentil 98 Promedio Diario|359.500|7.414.375|14,92|
|MP2,5|Promedio Trianual|359.500|7.414.375|4,38|
|CO|Percentil 99, máx. 1 hora|359.500|7.414.375|314,22|
|CO|Percentil 99, máx. 8 hora|359.500|7.414.375|89,88|
|NO2|Percentil 99, máx. 1 hora|359.500|7.414.375|220,16|
|NO2|Promedio, Anual|359.500|7.414.375|1,06|
|SO2|Percentil 99.73 Concentración 1 hora|359.500|7.414.375|95,4|
|SO2|Promedio Diario, percentil 99|359.500|7.414.375|9,16|
|SO2|Promedio, Anual|359.500|7.414.375|0,9|

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 79
Antofagasta

**Tabla 66: Puntos de Máximo Impacto - Fase de Operación**

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

|Parámetro|Estadístico|Coordenada WGS-84|Col4|Concentración<br>(μg/m3N)|
|---|---|---|---|---|
|**Parámetro**|**Estadístico**|**Este**|**Norte**|**Norte**|
|MP10|Percentil 98 Promedio 24 horas|359.500|7.414.375|16,82|
|MP10|Promedio Anual|358.500|7.414.375|3,23|
|MP2,5|Percentil 98 Promedio Diario|359.500|7.414.375|1,69|
|MP2,5|Promedio Trianual|358.500|7.414.375|0,32|
|CO|Percentil 99, máx. 1 hora|359.500|7.414.375|3,08|
|CO|Percentil 99, máx. 8 hora|359.500|7.414.375|0,9|
|NO2|Percentil 99, máx. 1 hora|359.500|7.414.375|1,03|
|NO2|Promedio, Anual|359.500|7.414.375|0,04|
|SO2|Percentil 99.73 Concentración 1 hora|359.500|7.414.375|1,75|
|SO2|Promedio Diario, percentil 99|359.500|7.414.375|0,17|
|SO2|Promedio, Anual|359.500|7.414.375|0,02|

**Tabla 67: Puntos de Máximo Impacto - Fase de Cierre**

|Parámetro|Estadístico|Coordenada WGS-84|Col4|Concentración<br>(μg/m3N)|
|---|---|---|---|---|
|**Parámetro**|**Estadístico**|Este|Norte|Norte|
|MP10|Percentil 98 Promedio 24 horas|359.500|7.414.375|25,04|
|MP10|Promedio Anual|359.500|7.414.375|3,69|
|MP2,5|Percentil 98 Promedio Diario|359.500|7.414.375|19,36|
|MP2,5|Promedio Trianual|359.500|7.414.375|2,75|
|CO|Percentil 99, máx. 1 hora|359.500|7.414.375|418,69|
|CO|Percentil 99, máx. 8 hora|359.500|7.414.375|141,88|
|NO2|Percentil 99, máx. 1 hora|359.500|7.414.375|675,14|
|NO2|Promedio, Anual|359.500|7.414.375|16,77|
|SO2|Percentil 99.73 Concentración 1 hora|359.500|7.414.375|95,4|
|SO2|Promedio Diario, percentil 99|359.500|7.414.375|9,16|
|SO2|Promedio, Anual|359.500|7.414.375|0,9|

**14.** **CONCLUSIONES**

Los resultados obtenidos de la modelación realizada y el análisis efectuado en los apartados anteriores, indican
que el proyecto, en general, no presenta impactos en la calidad del aire en ninguno de los receptores analizados,
y por lo tanto, no compromete la salud de la población.

Con respecto a si generan efectos adversos significativos sobre los recursos naturales del sector, al igual que en
el caso anterior, no se presentan impactos en ninguna de las zonas analizadas, en consecuencia, no se
presentan efectos adversos significativos sobre los recursos naturales.

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 80
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**15.** **MAPAS DE ISOCONCENTRACIONES**

En las siguientes figuras se presentan las curvas de Isoconcentración para la etapa de mayores emisiones y que
corresponde a la etapa de operación. Como puede apreciarse en las tablas de resultados y láminas de
Isoconcentración, el proyecto no genera ningún tipo impactos significativos en la calidad del aire en zona
poblada.

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 81
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 24: Mapa de Isoconcentración Material Particulado MP10 - Etapa de Construcción (24 h)**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 82
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 25: Mapa de Isoconcentración Material Particulado MP10 - Etapa de Construcción (Anual)**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 83
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 26: Mapa de Isoconcentración Material Particulado MP2.5 - Etapa de Construcción (24 h)**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 84
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 27: Mapa de Isoconcentración Material Particulado MP2.5 - Etapa de Construcción (Anual)**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 85
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 28: Mapa de Isodepositación Material Particulado Sedimentable MPS - Etapa de Construcción (24h)**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 86
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 29: Mapa de Isodepositación Material Particulado Sedimentable MPS - Etapa de Construcción (Anual)**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 87
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 30: Mapa de Isoconcentración Gases CO - Etapa de Construcción (1h)**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 88
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 31: Mapa de Isoconcentración Gases CO - Etapa de Construcción (8h)**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 89
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 32: Mapa de Isoconcentración Gases NO2 - Etapa de Construcción (1 h)**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 90
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 33: Mapa de Isoconcentración Gases NO2 - Etapa de Construcción (Anual)**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 91
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 34: Mapa de Isoconcentración Gases SO2 - Etapa de Construcción (1h)**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 92
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 35: Mapa de Isoconcentración Gases SO2 - Etapa de Construcción (24h)**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 93
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 36: Mapa de Isoconcentración Gases SO2 - Etapa de Construcción (Anual)**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 94
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 37: Mapa de Isoconcentración Material Particulado MP10 - Etapa de Operación (24 h)**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 95
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 38: Mapa de Isoconcentración Material Particulado MP10 - Etapa de Operación (Anual)**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 96
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 39: Mapa de Isoconcentración Material Particulado MP2.5 - Etapa de Operación (24 h)**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 97
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 40: Mapa de Isoconcentración Material Particulado MP2.5 - Etapa de Operación (Anual)**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 98
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 41: Mapa de Isodepositación Material Particulado Sedimentable MPS - Etapa de Operación (24h)**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 99
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 42: Mapa de Isodepositación Material Particulado Sedimentable MPS - Etapa de Operación (Anual)**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 100
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 43: Mapa de Isoconcentración Gases CO - Etapa de Operación (1h)**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 101
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 44: Mapa de Isoconcentración Gases CO - Etapa de Operación (8h)**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 102
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 45: Mapa de Isoconcentración Gases NO2 - Etapa de Operación (1 h)**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 103
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 46: Mapa de Isoconcentración Gases NO2 - Etapa de Operación (Anual)**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 104
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 47: Mapa de Isoconcentración Gases SO2 - Etapa de Operación (1h)**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 105
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 48: Mapa de Isoconcentración Gases SO2 - Etapa de Operación (24h)**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 106
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 49: Mapa de Isoconcentración Gases SO2 - Etapa de Operación (Anual)**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 107
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 50: Mapa de Isoconcentración Material Particulado MP10 - Etapa de Cierre (24 h)**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 108
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 51: Mapa de Isoconcentración Material Particulado MP10 - Etapa de Cierre (Anual)**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 109
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 52: Mapa de Isoconcentración Material Particulado MP2.5 - Etapa de Cierre (24 h)**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 110
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 53: Mapa de Isoconcentración Material Particulado MP2.5 - Etapa de Cierre (Anual)**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 111
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 54: Mapa de Isodepositación Material Particulado Sedimentable MPS - Etapa de Cierre (24h)**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 112
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 55: Mapa de Isodepositación Material Particulado Sedimentable MPS - Etapa de Cierre (Anual)**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 113
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 56: Mapa de Isoconcentración Gases CO - Etapa de Cierre (1h)**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 114
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 57: Mapa de Isoconcentración Gases CO - Etapa de Cierre (8h)**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 115
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 58: Mapa de Isoconcentración Gases NO2 - Etapa de Cierre (1 h)**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 116
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 59: Mapa de Isoconcentración Gases NO2 - Etapa de Cierre (Anual)**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 117
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 60: Mapa de Isoconcentración Gases SO2 - Etapa de Cierre (1h)**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 118
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 61: Mapa de Isoconcentración Gases SO2 - Etapa de Cierre (24h)**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 119
Antofagasta

Informe de Emisiones
Declaración de Impacto Ambiental

Proyecto NAVÍO II

**Figura 62: Mapa de Isoconcentración Gases SO2 - Etapa de Cierre (Anual)**

**BORDOLI & Consultores EIRL**
Avenida O’Higgins #1338, Oficina 1002, Edificio Mackenzie pág. 120
Antofagasta

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 63: Aportes del Proyecto Etapa de Operación con aplicación de factor de corrección****

| Parámetro | Estadístico | Limite<br>Norma<br>(μg/m3N) | Concentración<br>(μg/m3N)<br>Receptor R1 | %<br>Respecto<br>de la<br>Norma | Concentración<br>(μg/m3N)<br>Receptor R2 | %<br>Respecto<br>de la<br>Norma | Concentración<br>(μg/m3N)<br>Receptor R3 | %<br>Respecto<br>de la<br>Norma |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MPS | Promedio Mensual | 150 | 5,71E-06 | 0,0 | 1,34E-04 | 0,0 | 7,83E-05 | 0,0 |
| MPS | Promedio Anual | 50 | 1,29E-06 | 0,0 | 4,31E-05 | 0,0 | 2,55E-05 | 0,0 |
| SO2 | Promedio Anual | 50 | 3,40E-06 | 0,0 | 9,36E-06 | 0,0 | 2,82E-06 | 0,0 |
| SO2 | Percentil 99.7 Conc. Diaria | 20 | 1,19E-05 | 0,0 | 1,04E-04 | 0,0 | 4,66E-05 | 0,0 |
| SO2 | Percentil 99.73 Conc. 1 hora | 30000 | 1,19E-05 | 0,0 | 1,04E-04 | 0,0 | 4,66E-05 | 0,0 |

**Tabla 64: Aportes del Proyecto Etapa de Cierre con aplicación de factor de corrección****

| Parámetro | Estadístico | Limite<br>Norma<br>(μg/m3N) | Concentración<br>(μg/m3N)<br>Receptor R1 | %<br>Respecto<br>de la<br>Norma | Concentración<br>(μg/m3N)<br>Receptor R2 | %<br>Respecto<br>de la<br>Norma | Concentración<br>(μg/m3N)<br>Receptor R3 | %<br>Respecto<br>de la<br>Norma |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MPS | Promedio Mensual | 150 | 1,24E-06 | 0,0 | 8,98E-06 | 0,0 | 4,87E-06 | 0,0 |
| MPS | Promedio Anual | 50 | 2,64E-07 | 0,0 | 2,68E-06 | 0,0 | 1,51E-06 | 0,0 |
| SO2 | Promedio Anual | 50 | 1,85E-04 | 0,0 | 5,10E-04 | 0,0 | 1,54E-04 | 0,0 |
| SO2 | Percentil 99.7 Conc. Diaria | 20 | 1,25E-04 | 0,0 | 1,35E-04 | 0,0 | 1,23E-04 | 0,0 |
| SO2 | Percentil 99.73 Conc. 1 hora | 30000 | 6,46E-04 | 0,0 | 5,67E-03 | 0,0 | 2,54E-03 | 0,0 |
