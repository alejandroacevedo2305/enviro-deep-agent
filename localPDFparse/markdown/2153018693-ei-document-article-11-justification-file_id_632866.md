---
title: Sin título
author: Tania
date: D:20210831175743-04'00'
language: es
type: manual
pages: 62
has_toc: False
has_tables: True
extraction_quality: high
---

## DECLARACIÓN DE IMPACTO AMBIENTAL “Parque Solar Fotovoltaico Soledad”

### S.C.M. COSAYACH Yodo [REVISIÓN 0]

**Preparado para:**

Sociedad Contractual Minera COSAYACH Yodo

Amunátegui 178, piso 4, Santiago, Región Metropolitana.

Fono: 22-5406269

**Elaborado por:**

Minería y Medio Ambiente Ltda.

Monseñor Sotero Sanz 100, Of. 505, Providencia, Santiago, RM.

Teléfono: (56-2) 22442188

e-mail: jgalaz@myma.cl

|DECLARACIÓN DE IMPACTO AMBIENTAL<br>“Parque Solar Fotovoltaico Soledad”<br>Anexo 2-3: Modelación de Dispersión de Contaminantes|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
||||||||||
|0|27-08-2021|Revisión Interna|Revisión Interna|DD|CM|SA|||
|**REV **|**FECHA **|**EMITIDO PARA **|**EMITIDO PARA **|**POR **|**J. Proy. **|**Aprobó **|**J. Proy **|**Aprobó **|
|**REVISIONES**|**REVISIONES**|**REVISIONES**|**REVISIONES**|**MYMA**|**MYMA**|**MYMA**|**CLIENTE**|**CLIENTE**|
|**CONSULTOR**|**CONSULTOR**|**CONSULTOR**|**N° Documento**<br>**CÓDIGO MYMA**<br>**MY-53-2020 **|**N° Documento**<br>**CÓDIGO MYMA**<br>**MY-53-2020 **|**N° Documento**<br>**CÓDIGO MYMA**<br>**MY-53-2020 **|**N° Documento**<br>**CÓDIGO MYMA**<br>**MY-53-2020 **|**REV.**|**REV.**|
||||||||**0 **|**0 **|

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

### TABLA DE CONTENIDO

1 Introducción ................................................................................................................................... 4

2 Antecedentes generales del Proyecto ........................................................................................... 5

2.1 Descripción del Proyecto .......................................................................................................... 5

2.2 Emisiones .................................................................................................................................. 5

2.2.1 Fase de Construcción .................................................................................................. 5

2.2.2 Fase de Operación ....................................................................................................... 6

2.2.3 Fase de Cierre .............................................................................................................. 6

3 Descripción y justificación del modelo y los contaminates considerados ..................................... 7

3.1 Justificación del modelo seleccionado ..................................................................................... 7

3.2 Justificación de los contaminantes por modelar ...................................................................... 9

3.3 Norma de calidad del aire ....................................................................................................... 11

4 Configuración del modelo y análisis de incertidumbre ............................................................... 13

4.1 Características del dominio de modelación y su entorno ...................................................... 13

4.1.1 Dominio de modelación ............................................................................................ 13

4.1.2 Configuración del modelo ......................................................................................... 13

4.1.3 Meteorología ............................................................................................................. 14

4.1.4 Topografía ................................................................................................................. 15

4.2 Análisis de Incertidumbre del modelo WRF ........................................................................... 17

4.2.1 Análisis cualitativo ..................................................................................................... 18

4.2.2 Análisis Cuantitativo .................................................................................................. 24

5 Datos de entrada de modelo ....................................................................................................... 30

5.1 Fuentes de Emisión ................................................................................................................. 30

5.2 Receptores de interés ............................................................................................................. 32

6 Resultados de la modelación atmosférica ................................................................................... 34

6.1 Isocurvas ................................................................................................................................. 34

6.2 Puntos de máxima concentración (PMC) ............................................................................... 50

6.3 Aportes en receptores sensibles ............................................................................................. 51

6.3.1 Aportes fase del Proyecto ......................................................................................... 51

6.4 Calidad del Aire Observada ..................................................................................................... 53

6.5 Aportes en receptores sensibles ............................................................................................. 54

**REVISIÓN [0]** **i**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

7 Análisis de resultados y conclusiones .......................................................................................... 56

### LISTADO DE TABLAS

Tabla 2-1: Resumen de emisiones - Fase de Construcción. ............................................................... 5

<!-- INICIO TABLA 2-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **2.2.1** **Fase de Construcción** A continuación, se resumen de emisiones para la Fase de Construcción: -->

**Tabla 2-1: Resumen de emisiones - Fase de Construcción.****

| Obra/actividad | Emisiones [t/año] | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Obra/actividad** | **MPS** | **MP10 ** | **MP25 ** | **NOX ** | **SO2 ** | **CO** | **HC/COV** | **NH3 ** |
| **Excavación** | 15,47 | 3,48 | 1,62 | -- | -- | -- | -- | -- |
| **Transferencia de material** | 1,64 | 0,78 | 0,12 | -- | -- | -- | -- | -- |
| **Nivelación** | 0,09 | 0,03 | 0,00 | -- | -- | -- | -- | -- |
| **Compactación** | 1,42 | 0,32 | 0,15 | -- | -- | -- | -- | -- |
| **Perforaciones** | 0,89 | 0,27 | 0,04 | -- | -- | -- | -- | -- |
| **Maquinaria [75 ≤ P < 130]** | 0,06 | 0,06 | 0,06 | 0,72 | <0,01 | 0,38 | 0,07 | <0,01 |
| **Maquinaria [130 ≤ P < 560]** | 0,13 | 0,13 | 0,13 | 2,86 | 0,01 | 1,51 | 0,27 | <0,01 |
| **Grupo electrógeno** | 0,35 | 0,35 | 0,32 | 4,87 | 0,32 | 1,05 | <0,01 | <0,01 |
| **Vehículos en caminos pavimentados** | 6,99 | 1,34 | 0,32 | -- | -- | -- | -- | -- |
| **Vehículos en caminos industriales NO pavimentados** | 154,33 | 47,25 | 4,72 | -- | -- | -- | -- | -- |
| **Motor vehículos Camionetas** | <0,01 | <0,01 | <0,01 | 0,02 | <0,01 | 0,01 | <0,01 | <0,01 |
| **Motor vehículos Buses** | <0,01 | <0,01 | <0,01 | 0,10 | <0,01 | <0,01 | <0,01 | <0,01 |
| **Motor vehículos Pesados [> 32 t]** | <0,01 | <0,01 | <0,01 | 0,60 | <0,01 | 0,02 | <0,01 | <0,01 |
| **Total** | **181,37** | **54,00** | **7,50** | **9,18** | **0,33** | **2,97** | **0,34** | **<0,01** |

<!-- Estadísticas: 15 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Anexo 2.1: Inventario de Emisiones Atmosféricas del presente DIA. **REVISIÓN [0]** **5** -->
<!-- FIN TABLA 2-1 -->


Tabla 2-2: Resumen de emisiones - Fase de Operación. .................................................................... 6

<!-- INICIO TABLA 2-2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **2.2.2** **Fase de Operación** A continuación, se resumen las emisiones para la Fase de Operación: -->

**Tabla 2-2: Resumen de emisiones - Fase de Operación.****

| Actividad | Emisiones [t/año] | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Actividad** | **MPS** | **MP10 ** | **MP25 ** | **NOX ** | **SO2 ** | **CO** | **HC/COV** | **NH3 ** |
| **Vehículos en caminos pavimentados** | 0,5754 | 0,1104 | 0,0267 | -- | -- | -- | -- | -- |
| **Vehículos en caminos industriales NO pav.** | 36,102 | 11,051 | 1,1052 | -- | -- | -- | -- | -- |
| **Motor vehículos Camionetas** | 0,0012 | 0,0012 | 0,0012 | 0,0251 | 0,0001 | 0,0113 | 0,0011 | <0,0001 |
| **Motor vehículos Pesados** | 0,0003 | 0,0003 | 0,0003 | 0,0436 | 0,0001 | 0,0011 | 0,0001 | <0,0001 |
| **Total** | **36,678** | **11,163** | **1,133** | **0,068** | **0,000** | **0,012** | **0,001 ** | **0,000** |

<!-- Estadísticas: 6 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Anexo 2.1: Inventario de Emisiones Atmosféricas del presente DIA. **2.2.3** **Fase de Cierre** -->
<!-- FIN TABLA 2-2 -->


Tabla 2-3: Resumen de emisiones - Fase de Cierre. ........................................................................... 6

<!-- INICIO TABLA 2-3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **2.2.3** **Fase de Cierre** A continuación, se detalla el resumen de emisiones para la Fase de Cierre. -->

**Tabla 2-3: Resumen de emisiones - Fase de Cierre.****

| Actividad | MPS | MP<br>10 | MP<br>25 | NO<br>X | SO<br>2 | CO | HC/COV | NH<br>3 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Transferencia de material** | 1,64 | 0,78 | 0,12 | 0,00 | -- | -- | -- | -- |
| **Nivelación** | 0,09 | 0,03 | 0,00 | 0,00 | -- | -- | -- | -- |
| **Maquinaria [75 ≤ P < 130]** | 0,06 | 0,06 | 0,06 | 0,72 | <0,01 | 0,38 | 0,07 | <0,01 |
| **Maquinaria [130 ≤ P < 560]** | 0,13 | 0,13 | 0,13 | 2,86 | 0,01 | 1,51 | 0,27 | <0,01 |
| **Vehículos en caminos pavimentados** | 6,99 | 1,34 | 0,32 | 0,00 | -- | -- | -- | -- |
| **Vehículos en caminos industriales NO pavimentados** | 154,33 | 47,25 | 4,72 | 0,00 | -- | -- | -- | -- |
| **Motor vehículos Camionetas** | <0,01 | <0,01 | <0,01 | 0,02 | <0,01 | <0,01 | <0,01 | <0,01 |
| **Motor vehículos Buses** | <0,01 | <0,01 | <0,01 | 0,10 | <0,01 | <0,01 | <0,01 | <0,01 |
| **Motor vehículos Pesados [> 32 t]** | <0,01 | <0,01 | <0,01 | 0,60 | <0,01 | 0,02 | <0,01 | <0,01 |
| **Total** | **163,25** | **49,59** | **5,37** | **4,30** | **0,01** | **1,92** | **0,34** | **<0,01** |

<!-- Estadísticas: 10 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Anexo 2.1: Inventario de Emisiones Atmosféricas del presente DIA. **REVISIÓN [0]** **6** -->
<!-- FIN TABLA 2-3 -->


Tabla 3-1: Norma primaria de calidad del aire. ................................................................................. 12

<!-- INICIO TABLA 3-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **“Parque Solar Fotovoltaico Soledad”** SCM COSAYACH Yodo -->

**Tabla 3-1: Norma primaria de calidad del aire.****

| Parámetro | Cuerpo Legal | Estadístico | Valor |
| --- | --- | --- | --- |
| **MP10 ** | D.S. N°59/98 del<br>MINSEGPRES,<br>modificada por<br>D.S.N°45/01 del<br>MINSEGPRES | Promedio aritmético de tres años calendario consecutivos | 50<br>μg/m3 |
| **MP10 ** | D.S. N°59/98 del<br>MINSEGPRES,<br>modificada por<br>D.S.N°45/01 del<br>MINSEGPRES | Percentil 98 de las concentraciones de 24 horas registradas durante un<br>período anual | 150<br>μg/m3 |
| **MP2,5 ** | D.S. N°12/11 del<br>MMA | Promedio tri-anual de las concentraciones anuales | 20<br>μg/m3 |
| **MP2,5 ** | D.S. N°12/11 del<br>MMA | Percentil 98 de los promedios diarios registrados durante un año | 50<br>μg/m3 |
| **NO2 ** | D.S. N° 114/2002<br>del MINSEGPRES | Promedio aritmético de los valores de concentración anual de tres años<br>calendarios sucesivos | 100<br>μg/m3 |
| **NO2 ** | D.S. N° 114/2002<br>del MINSEGPRES | Promedio aritmético de tres años sucesivos del percentil 99 de los<br>máximos diarios de concentración de 1 hora registrados durante un año<br>calendario | 400<br>μg/m3 |
| **SO2 ** | D.S. N° 104/2019<br>del MMA | Promedio aritmético de tres años sucesivos del percentil 99 de las<br>concentraciones de 24 horas registradas durante un año calendario | 150<br>μg/m3 |
| **SO2 ** | D.S. N° 104/2019<br>del MMA | Promedio aritmético de los valores de concentración anual tres años<br>calendario sucesivos | 60<br>μg/m3 |
| **SO2 ** | D.S. N° 104/2019<br>del MMA | Promedio aritmético de tres años sucesivos del percentil 98,5 de las<br>concentraciones horarias registradas durante un año calendario | 350<br>μg/m3 |
| **CO** | D.S. N° 115/2002<br>del MINSEGPRES | Promedio aritmético de tres años sucesivos del percentil 99 de los<br>máximos diarios de concentración de 1 hora registrados durante un año<br>calendario | 30<br>mg/m3 |
| **CO** | D.S. N° 115/2002<br>del MINSEGPRES | Promedio aritmético de tres años sucesivos del percentil 99 de los<br>máximos diarios de concentración de 8 horas (promedio móvil)<br>registrados durante un año calendario | 10<br>mg/m3 |

<!-- Estadísticas: 11 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: MYMA, 2021. **Tabla 3-2: Norma secundaria de calidad del aire para el SO** **2** **y norma de referencia para el MPS.** -->
<!-- FIN TABLA 3-1 -->


Tabla 3-2: Norma secundaria de calidad del aire para el SO 2 y norma de referencia para el MPS. . 12

<!-- INICIO TABLA 3-2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |**CO**|D.S. N° 115/2002<br>del MINSEGPRES|Promedio aritmético de tres años sucesivos del percentil 99 de los<br>máximos diarios de concentración de 1 hora registrados durante un año<br>calendario|30<br>mg/m3| |**CO**|D.S. N° 115/2002<br>del MINSEGPRES|Promedio aritmético de tres años sucesivos del percentil 99 de los<br>máximos diarios de concentración de 8 horas (promedio móvil)<br>registrados durante un año calendario|10<br>mg/m3| Fuente: MYMA, 2021. -->

**Tabla 3-2: Norma secundaria de calidad del aire para el SO** **2** **y norma de referencia para el MPS.****

| Parámetro | Cuerpo Legal | Estadístico | Valor |
| --- | --- | --- | --- |
| **SO2 ** | D.S N° 22/10 del<br>MINSEGPRES | Promedio aritmético de tres años calendario sucesivos del<br>Percentil 99,73 de la concentración máxima de horaria | 1.000<br>μg/m3 |
| **SO2 ** | D.S N° 22/10 del<br>MINSEGPRES | Promedio aritmético anual | 80<br>μg/m3 |
| **SO2 ** | D.S N° 22/10 del<br>MINSEGPRES | Promedio aritmético de tres años calendario sucesivos del<br>Percentil 99,7 de las concentraciones diarias | 365<br>μg/m3 |
| **MPS** | Norma Suiza | Promedio aritmético mensual | 200<br>mg/m2día |
| **MPS** | Norma Suiza | Promedio aritmético anual | 100<br>mg/m2día |

<!-- Estadísticas: 5 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: MYMA, 2021. **REVISIÓN [0]** **12** -->
<!-- FIN TABLA 3-2 -->


Tabla 4-1: Descripción del archivo *.INP. .......................................................................................... 13

<!-- INICIO TABLA 4-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- permite ver las características o configuraciones de la modelación realizada. El archivo se estructura de acuerdo con lo que se presenta en la siguiente tabla: -->

**Tabla 4-1: Descripción del archivo *.INP.****

| ID | Descripción |
| --- | --- |
| * | Nombre de la modelación realizada. |
| 0 | Nombre de archivos de entrada y salida de la modelación. |
| 1 | Parámetros de control generales de la corrida: Fecha y hora de inicio, duración de la ejecución, frecuencia<br>temporal. Número de contaminantes. Configuración de reinicio para realizar una serie de ejecuciones de<br>continuación. Formato de datos meteorológicos y ajuste de tiempo promedio. |
| 2 | Opciones Técnicas. Variables de control que determinan los métodos para el tratamiento de la química,<br>deposición húmeda, depositación seca, dispersión, aumento de pluma, terreno. |
| 3 a,b | Listado de especies. Nombres de especies, especies habilitadas, emitidas y depositadas en seco. |
| 4 | Parámetros de control de cuadrícula. Especificación de cuadrículas meteorológicas, computacionales y de<br>muestreo, número de celdas, capas verticales y coordenadas de referencia. |
| 5 | Opciones de salida. Variables de control de impresión, variables de control de salida del disco. |
| 6a, b, c | Configuración del terreno complejo a escala de subcuadrícula (CTSG). Información que describe la ubicación, la<br>forma y la altura de la colina a escala de subcuadrícula. Ubicaciones y altitud de receptores. |
| 7 | Parámetros de deposición seca- Gases. Difusividad de contaminantes, constante de disociación, reactividad,<br>resistencia al mesófilo, coeficiente de la ley de Henry. |
| 8 | Parámetros de deposición seca - Partículas. Diámetro medio de masa geométrica. |

<!-- Estadísticas: 10 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- **REVISIÓN [0]** **13** **Anexo 2-3: Modelación de Dispersión de Contaminantes** -->
<!-- FIN TABLA 4-1 -->


Tabla 4-2: Detalle de Proyección cartográfica y coordenadas Archivo WRF. ................................... 14

<!-- INICIO TABLA 4-2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- La meteorología del sector se incorpora mediante el uso de un modelo meteorológico WRF. La configuración utilizada es detallada a continuación, en la Tabla 4-2. -->

**Tabla 4-2: Detalle de Proyección cartográfica y coordenadas Archivo WRF.****

| Proyección Cartográfica | Cónica conforme de Lambert (LCC) |
| --- | --- |
| Período | 1 Ene 2020 00:00 - 1 Ene 2021 20:00 |
| Origen | RLAT0 = 20,181S<br>RLAN0 = 69,770W<br>XLAT1= 19,871S<br>XLAT2 = 20,491S |
| Proyección | Lambert Conic Conformal |
| Datum | NWS-84 6370 km Radius, Global Sphere |
| Grilla | 100 x 100 km |
| Resolución | 1 x 1 km2 |
| Celdas verticales | 10 |

<!-- Estadísticas: 7 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: MYMA, 2021. Las variables meteorológicas que contiene el modelo para toda el área de estudio corresponden a -->
<!-- FIN TABLA 4-2 -->


Tabla 4-3: Parámetros meteorológicos utilizados en el análisis de incertidumbre. ......................... 18

<!-- INICIO TABLA 4-3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **“Parque Solar Fotovoltaico Soledad”** SCM COSAYACH Yodo -->

**Tabla 4-3: Parámetros meteorológicos utilizados en el análisis de incertidumbre.****

| Estación | Ubicación (Datum WGS84 - Huso 19S) | Col3 | Parámetros | Año |
| --- | --- | --- | --- | --- |
| **Estación** | **Este (m)** | **Norte (m)** | **Norte (m)** | **Norte (m)** |
| Pozo Almonte | 417.709 | 7.760.617 | Velocidad del Viento | 2020 |
| Pozo Almonte | 417.709 | 7.760.617 | Dirección del Viento | Dirección del Viento |
| Pozo Almonte | 417.709 | 7.760.617 | Temperatura Ambiental | Temperatura Ambiental |
| Soledad | 427.160 | 7.739.828 | Velocidad del Viento | 2020 |
| Soledad | 427.160 | 7.739.828 | Dirección del Viento | Dirección del Viento |
| Soledad | 427.160 | 7.739.828 | Temperatura Ambiental | Temperatura Ambiental |
| Alto Hospicio | 385.118 | 7.755.989 | Velocidad del Viento | 2020 |
| Alto Hospicio | 385.118 | 7.755.989 | Dirección del Viento | Dirección del Viento |
| Alto Hospicio | 385.118 | 7.755.989 | Temperatura Ambiental | Temperatura Ambiental |

<!-- Estadísticas: 10 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia en base a registros de la SMA. Adicionalmente, cabe destacar que, de acuerdo con los requerimientos del Servicio de Evaluación -->
<!-- FIN TABLA 4-3 -->


Tabla 4-4: Referencias de aceptabilidad para los estadígrafos de cada una de variables

<!-- INICIO TABLA 4-4 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- para el análisis de las variables meteorológicas modeladas frente a las observadas corresponden a las siguientes: -->

**Tabla 4-4: Referencias de aceptabilidad para los estadígrafos de cada una de variables meteorológicas.****

| Estación | BIAS | IOA | MGE | RMSE | r |
| --- | --- | --- | --- | --- | --- |
| Velocidad del Viento | ≤ ±0,5 *m/s+ | ≥ 0,60 | - | ≤ 2 *m/s+ | 1 |
| Dirección del Viento | ≤ ±10 *°+ | ≥ 0,60 | ≤ 30 *°+ | - | 1 |
| Temperatura | ≤ ±0,5 *°+ | ≥ 0,80 | ≤ 2 *°+ | - | 1 |

<!-- Estadísticas: 3 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia (en basa a documento nota al pie). Tal como se dijo anteriormente, la metodología denominada “Análisis de Incertidumbre” tiene por -->
<!-- FIN TABLA 4-4 -->

meteorológicas. ................................................................................................................................. 26

Tabla 4-5: Análisis cuantitativo del modelo. ..................................................................................... 27

<!-- INICIO TABLA 4-5 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- cabalidad los parámetros estadísticos y se dejan con rojo los parámetros estadísticos que superan las referencia de aceptabilidad óptima, independiente de su magnitud de superación: -->

**Tabla 4-5: Análisis cuantitativo del modelo.****

| Estación | Variable | BIAS | IOA | MGE | RMSE | r |
| --- | --- | --- | --- | --- | --- | --- |
| Alto Hospicio | Velocidad del viento | -0,3 | 0,7 | 0,8 | 1,0 | 0,8 |
| Alto Hospicio | Dirección del viento | -11,9 | 0,5 | 79,6 | 120,3 | 0,2 |
| Alto Hospicio | Temperatura | 2,3 | 0,6 | 2,4 | 2,9 | 0,9 |
| Pozo Almonte | Velocidad del viento | 0,0 | 0,8 | 0,9 | 1,2 | 0,9 |
| Pozo Almonte | Dirección del viento | 2,2 | 0,5 | 65,5 | 104,4 | 0,3 |
| Pozo Almonte | Temperatura | 1,1 | 0,7 | 2,3 | 2,7 | 1,0 |
| Soledad | Velocidad del viento | -0,2 | 0,7 | 0,9 | 1,3 | 0,8 |
| Soledad | Dirección del viento | 9,1 | 0,4 | 93,9 | 132,6 | 0,2 |
| Soledad | Temperatura | 0,8 | 0,7 | 3,2 | 3,7 | 1,0 |

<!-- Estadísticas: 9 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: MYMA, 2021. En base a estos parámetros obtenidos, es posible indicar que el modelo se adapta de mejor -->
<!-- FIN TABLA 4-5 -->


Tabla 5-1: Escenario de emisiones - Fase de Construcción. ............................................................. 30

<!-- INICIO TABLA 5-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- peor condición. A continuación, se presentan las emisiones consideradas por área modelada y posteriormente se presenta la distribución fuentes en el territorio. -->

**Tabla 5-1: Escenario de emisiones - Fase de Construcción.****

| Sector | Emisiones [t/año] | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Área modelo | Col11 | Col12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Sector** | **MPS** | **MP10** | **MP25 ** | **NOX ** | **SO2 ** | **CO** | **HC/COV** | **NH3 ** | **Largo** | **Ancho** | **Área** |
| **PFV** | 2,91 | 0,69 | 0,30 | <0,01 | <0,01 | <0,01 | <0,01 | <0,01 | -- | -- | 66.153 |
| **Línea de evacuación** | 17,13 | 4,72 | 2,15 | 8,46 | 0,33 | 2,95 | 0,34 | <0,01 | 1.771 | 1 | 1.771 |
| **Rutas Pavimentadas** | 154,34 | 47,25 | 4,73 | 0,24 | <0,01 | 0,01 | <0,01 | <0,01 | 72.279 | 5 | 361.394 |
| **Rutas No Pavimentadas** | 6,99 | 1,34 | 0,33 | 0,48 | <0,01 | 0,02 | <0,01 | <0,01 | 21.632 | 5 | 108.160 |
| **Total** | **181,37** | **54,00** | **7,50** | **9,18** | **0,33** | **2,97** | **0,34** | **<0,01** | -- | -- | -- |

<!-- Estadísticas: 6 filas, 12 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: MYMA, 2021. **REVISIÓN [0]** **30** -->
<!-- FIN TABLA 5-1 -->


Tabla 5-2: Receptores de Interés. ..................................................................................................... 32

<!-- INICIO TABLA 5-2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- La ubicación, descripción e ID de los receptores discretos a considerar se presenta a continuación en la siguiente tabla. -->

**Tabla 5-2: Receptores de Interés.****

| Tipo | ID | Coordenada LCC [m] | Col4 | Altitud [msnm] | Altura [m] | Descripción |
| --- | --- | --- | --- | --- | --- | --- |
| **Tipo** | **ID** | **X ** | **Y ** | **Y ** | **Y ** | **Y ** |
| Est.<br>Calidad<br>del aire | R_1 | -1.868,69 | -7.711,87 | 1.141,55 | 1,5 | Estación Pozo Almonte |
| Est.<br>Calidad<br>del aire | R_2 | 7.472,32 | -28.639,61 | 1.035,94 | 1,5 | Estación Soledad |
| Est.<br>Calidad<br>del aire | R_3 | -34.434,83 | -12.207,89 | 1.141,57 | 1,5 | Estación Alto Hospicio |

<!-- Estadísticas: 4 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: MYMA, 2021. **REVISIÓN [0]** **32** -->
<!-- FIN TABLA 5-2 -->


Tabla 6-1: Puntos de Máxima Concentración (PMC). ....................................................................... 50

<!-- INICIO TABLA 6-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- del escenario modelado, detallando el contaminante y su aporte, por estadístico. Además, se muestra las coordenadas de cada PMC. -->

**Tabla 6-1: Puntos de Máxima Concentración (PMC).****

| Parámetro | Estadístico | PMC | Norma | % Norma | Coordenadas UTM - WGS84 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Parámetro** | **Estadístico** | **PMC** | **Norma** | **% Norma** | **Este (m)** | **Norte (m)** |
| MPS [mg/m2-<br>día] | Promedio del Periodo | 25,48 | 100 | 25,48% | 417.658 | 7.743.407 |
| MPS [mg/m2-<br>día] | Promedio mensual | 33,92 | 200 | 16,96% | 16,96% | 16,96% |
| MP10<br>[ug/m3] | Promedio del Periodo | 23,24 | 50 | 46,47% | 46,47% | 46,47% |
| MP10<br>[ug/m3] | Percentil 98 Diario | 59,43 | 150 | 39,62% | 39,62% | 39,62% |
| MP2,5<br>[ug/m3] | Promedio del Periodo | 4,51 | 20 | 22,56% | 409.642 | 7.744.365 |
| MP2,5<br>[ug/m3] | Percentil 98 Diario | 9,35 | 50 | 18,70% | 18,70% | 18,70% |
| SO2 <br>[ug/m3] | Promedio del Periodo | 0,43 | 60 | 0,72% | 0,72% | 0,72% |
| SO2 <br>[ug/m3] | Percentil 99 Diario | 0,98 | 150 | 0,65% | 0,65% | 0,65% |
| SO2 <br>[ug/m3] | Percentil 98,5 Horario | 3,85 | 350 | 1,10% | 1,10% | 1,10% |
| SO2 <br>[ug/m3] | Promedio del Periodo | 0,43 | 80 | 0,54% | 0,54% | 0,54% |
| SO2 <br>[ug/m3] | Percentil 99,7 Diario | 1,02 | 365 | 0,28% | 0,28% | 0,28% |
| SO2 <br>[ug/m3] | Percentil 99,73 Horario | 4,57 | 1000 | 0,46% | 0,46% | 0,46% |
| NO2 <br>[ug/m3] | Promedio del Periodo | 10,90 | 100 | 10,90% | 10,90% | 10,90% |
| NO2 <br>[ug/m3] | Percentil 99 Horario | 125,19 | 400 | 31,30% | 31,30% | 31,30% |
| CO[ug/m3] | Percentil 99 8 Horas | 21,70 | 10000 | 0,22% | 0,22% | 0,22% |
| CO[ug/m3] | Percentil 99 Horario | 48,89 | 30000 | 0,16% | 0,16% | 0,16% |

<!-- Estadísticas: 17 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: MYMA, 2021. En la siguiente cartografía se presenta la localización de los PMC, en donde se puede ver que estos -->
<!-- FIN TABLA 6-1 -->


Tabla 6-2: Aporte del Proyecto - Fase de Construcción - Sin Corrección. ....................................... 52

<!-- INICIO TABLA 6-2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **“Parque Solar Fotovoltaico Soledad”** SCM COSAYACH Yodo -->

**Tabla 6-2: Aporte del Proyecto - Fase de Construcción - Sin Corrección.****

| Receptore<br>s de<br>Interés | MPS mg/m2d | Col3 | MP ug/m3<br>10 | Col5 | MP ug/m3<br>2.5 | Col7 | SO ug/m3<br>2 | Col9 | Col10 | Col11 | Col12 | Col13 | NO ug/m3<br>2 | Col15 | CO | Col17 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptore**<br>**s de**<br>**Interés** | Primaria | Primaria | Primaria | Primaria | Primaria | Primaria | Primaria | Primaria | Primaria | Secundaria | Secundaria | Secundaria | Primaria | Primaria | Primaria | Primaria |
| **Receptore**<br>**s de**<br>**Interés** | Media<br>Anual | Media<br>Mensual | Media<br>Anual | P98<br>Diario | Media<br>Anual | P98 Diario | Media<br>Anual | P99<br>Diario | P98.5<br>Horario | Media<br>Anual | P99.7<br>Diario | P99.73<br>Horario | Media<br>Anual | P99<br>Horario | P99 8<br>hrs. | P99<br>Horario |
| R_1 | 0,0351 | 0,0404 | 0,0321 | 0,0586 | 0,0071 | 0,0130 | 0,0001 | 0,0001 | 0,0003 | 0,0001 | 0,0001 | 0,0004 | 0,0083 | 0,0960 | 0,003 | 0,0074 |
| R_2 | 0,0322 | 0,0455 | 0,1679 | 0,5116 | 0,0176 | 0,0526 | 0,0001 | 0,0001 | 0,0002 | 0,0001 | 0,0001 | 0,0003 | 0,0015 | 0,0145 | 0,002 | 0,0040 |
| R_3 | 0,0108 | 0,0139 | 0,0099 | 0,0241 | 0,0022 | 0,0050 | <0,0001 | 0,0001 | 0,0002 | <0,0001 | 0,0001 | 0,0003 | 0,0024 | 0,0585 | 0,001 | 0,0038 |

<!-- Estadísticas: 5 filas, 17 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: MYMA, 2021. **Tabla 6-3: Aporte del Proyecto - Fase de Construcción - Con Corrección.** -->
<!-- FIN TABLA 6-2 -->


Tabla 6-3: Aporte del Proyecto - Fase de Construcción - Con Corrección. ...................................... 52

<!-- INICIO TABLA 6-3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |R_2|0,0322|0,0455|0,1679|0,5116|0,0176|0,0526|0,0001|0,0001|0,0002|0,0001|0,0001|0,0003|0,0015|0,0145|0,002|0,0040| |R_3|0,0108|0,0139|0,0099|0,0241|0,0022|0,0050|<0,0001|0,0001|0,0002|<0,0001|0,0001|0,0003|0,0024|0,0585|0,001|0,0038| Fuente: MYMA, 2021. -->

**Tabla 6-3: Aporte del Proyecto - Fase de Construcción - Con Corrección.****

| Receptore<br>s de<br>Interés | MPS mg/m2d | Col3 | MP ug/m3<br>10 | Col5 | MP ug/m3<br>2.5 | Col7 | SO ug/m3<br>2 | Col9 | Col10 | Col11 | Col12 | Col13 | NO ug/m3<br>2 | Col15 | CO | Col17 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptore**<br>**s de**<br>**Interés** | Primaria | Primaria | Primaria | Primaria | Primaria | Primaria | Primaria | Primaria | Primaria | Secundaria | Secundaria | Secundaria | Primaria | Primaria | Primaria | Primaria |
| **Receptore**<br>**s de**<br>**Interés** | Media<br>Anual | Media<br>Mensual | Media<br>Anual | P98<br>Diario | Media<br>Anual | P98 Diario | Media<br>Anual | P99<br>Diario | P98.5<br>Horario | Media<br>Anual | P99.7<br>Diario | P99.73<br>Horario | Media<br>Anual | P99<br>Horario | P99 8<br>hrs. | P99<br>Horario |
| R_1 | 0,0383 | 0,0440 | 0,0350 | 0,0639 | 0,0077 | 0,0142 | 0,0001 | 0,0001 | 0,0003 | 0,0001 | 0,0002 | 0,0004 | 0,0091 | 0,1047 | 0,003 | 0,0081 |
| R_2 | 0,0338 | 0,0478 | 0,1763 | 0,5372 | 0,0185 | 0,0553 | 0,0001 | 0,0001 | 0,0003 | 0,0001 | 0,0001 | 0,0003 | 0,0016 | 0,0152 | 0,002 | 0,0042 |
| R_3 | 0,0115 | 0,0148 | 0,0105 | 0,0255 | 0,0023 | 0,0053 | <0,0001 | 0,0001 | 0,0002 | <0,0001 | 0,0001 | 0,0003 | 0,0026 | 0,0620 | 0,001 | 0,0041 |

<!-- Estadísticas: 5 filas, 17 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: MYMA, 2021. **REVISIÓN [0]** **52** -->
<!-- FIN TABLA 6-3 -->


Tabla 6-4: Línea de Base Proyectada del Área de Estudio. ............................................................... 53

<!-- INICIO TABLA 6-4 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Anual), registrada se encuentra bajo el 68% de la normativa primaria de calidad del aire. En la siguiente tabla se presenta el resumen correspondiente a la Línea de Base del área de estudio -->

**Tabla 6-4: Línea de Base Proyectada del Área de Estudio.****

| Estación | Norma | Parámetro | Estadístico | 2018 | 2019 | 2020 | Promedio<br>trianual | Norma | % de la<br>norma |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Pozo<br>Almonte | Primaria | MP10 | Promedio Anual | 34,5 | 36,4 | 31,3 | 34,1 | 50 | 68% |
| Pozo<br>Almonte | Primaria | MP10 | Percentil 98 | 66,0 | 68,0 | 62,9 | 65,6 | 150 | 44% |
| Pozo<br>Almonte | Primaria | MP2,5 | Promedio Anual | 8,7 | 8,0 | 10,7 | 9,1 | 20 | 46% |
| Pozo<br>Almonte | Primaria | MP2,5 | Percentil 98 | 7,0 | 17,0 | 28,8 | 17,6 | 50 | 35% |
| Pozo<br>Almonte | Primaria | SO2 | Promedio Anual | 1,6 | 1,7 | 4,6 | 2,6 | 60 | 4% |
| Pozo<br>Almonte | Primaria | SO2 | Percentil 99 - Diario | 3,8 | 4,3 | 9,3 | 5,8 | 150 | 4% |
| Pozo<br>Almonte | Primaria | SO2 | Percentil 98,5 -<br>Horario | 5,3 | 6,2 | 12,8 | 8,1 | 350 | 2% |
| Pozo<br>Almonte | Secundaria | SO2 | Promedio Anual | 1,6 | 1,7 | 4,6 | 2,6 | 80 | 3% |
| Pozo<br>Almonte | Secundaria | SO2 | Percentil 99,7 - Diario | 4,0 | 4,6 | 13,7 | 7,4 | 365 | 2% |
| Pozo<br>Almonte | Secundaria | SO2 | Percentil 99,73 -<br>Horario | 7,9 | 11,5 | 27,5 | 15,6 | 1000 | 2% |
| Soledad | Primaria | SO2 | Promedio Anual | 4,6 | 3,4 | 4,8 | 4,3 | 60 | 7% |
| Soledad | Primaria | SO2 | Percentil 99 - Diario | 26,3 | 6,5 | 7,4 | 13,4 | 150 | 9% |
| Soledad | Primaria | SO2 | Percentil 98,5 -<br>Horario | 26,8 | 8,9 | 11,2 | 15,6 | 350 | 4% |
| Soledad | Secundaria | SO2 | Promedio Anual | 4,6 | 3,4 | 4,8 | 4,3 | 80 | 5% |
| Soledad | Secundaria | SO2 | Percentil 99,7 - Diario | 26,8 | 22,1 | 8,1 | 19,0 | 365 | 5% |
| Soledad | Secundaria | SO2 | Percentil 99,73 -<br>Horario | 42,0 | 20,1 | 19,6 | 27,2 | 1000 | 3% |
| Alto<br>Hospicio | Primaria | MP2,5 | Promedio Anual | 11,2 | 11,1 | 10,3 | 10,9 | 20 | 54% |
| Alto<br>Hospicio | Primaria | MP2,5 | Percentil 98 | 21,6 | 19,0 | 18,7 | 19,8 | 50 | 40% |

<!-- Estadísticas: 18 filas, 10 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: MYMA, 2021. **REVISIÓN [0]** **53** -->
<!-- FIN TABLA 6-4 -->


Tabla 6-5: Análisis de cumplimiento de Normativa Vigente. ............................................................ 54

<!-- INICIO TABLA 6-5 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- el análisis normativo en los receptores de interés para el escenario de modelación Construcción. En ellos se observa que los valores obtenidos son porcentualmente bajos respecto de la normativa para todos los receptores considerados. -->

**Tabla 6-5: Análisis de cumplimiento de Normativa Vigente.****

| Receptor de<br>Interés | MPS<br>mg/m2d | Col3 | MP<br>10<br>μg/m3 | Col5 | MP<br>2.5<br>μg/m3 | Col7 | SO<br>2<br>μg/m3 | Col9 | Col10 | Col11 | Col12 | Col13 | NO<br>2<br>μg/m3 | Col15 | CO<br>μg/m3 | Col17 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor de**<br>**Interés** | **Secundaria** | **Secundaria** | **Primaria** | **Primaria** | **Primaria** | **Primaria** | **Primaria** | **Primaria** | **Primaria** | **Secundaria** | **Secundaria** | **Secundaria** | **Primaria** | **Primaria** | **Primaria** | **Primaria** |
| **Receptor de**<br>**Interés** | **Media**<br>**Anual** | **Media**<br>**Mensual** | **Media**<br>**Anual** | **P98**<br>**Diario** | **Media**<br>**Anual** | **P98**<br>**Diario** | **Media**<br>**Anual** | **P99**<br>**Diario** | **P98,5**<br>**Hr** | **Media**<br>**Anual** | **P99.7**<br>**Diario** | **P99,73**<br>**Hr** | **Media**<br>**Anual** | **P99H** | **P99**<br>**8 hrs.** | **P99**<br>**Hr** |
| **Norma** | **100** | **200** | **50** | **150** | **20** | **50** | **60** | **150** | **350** | **80** | **365** | **1.000** | **100** | **400** | **10.000** | **30.000** |
| R1 | 0,04% | 0,02% | 0,07% | 0,04% | 0,04% | 0,03% | <0,01% | <0,01% | <0,01% | <0,01% | <0,01% | <0,01% | 0,01% | 0,03% | <0,01% | <0,01% |
| R2 | 0,03% | 0,02% | 0,35% | 0,36% | 0,09% | 0,11% | <0,01% | <0,01% | <0,01% | <0,01% | <0,01% | <0,01% | <0,01% | 0,00% | <0,01% | <0,01% |
| R3 | 0,01% | 0,01% | 0,02% | 0,02% | 0,01% | 0,01% | <0,01% | <0,01% | <0,01% | <0,01% | <0,01% | <0,01% | <0,01% | 0,02% | <0,01% | <0,01% |

<!-- Estadísticas: 6 filas, 17 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: MYMA, 2021. **REVISIÓN [0]** **54** -->
<!-- FIN TABLA 6-5 -->


Tabla 6-6: Análisis de cumplimiento de Normativa Vigente. ............................................................ 55

<!-- INICIO TABLA 6-6 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- corregidos con el factor estimado y línea base, se presenta el análisis normativo en las estaciones de monitoreo calidad del aire para el escenario de modelación. -->

**Tabla 6-6: Análisis de cumplimiento de Normativa Vigente.****

| ID | Estación | Contaminante | Estadístico | Norma | LB | AP | LB+AP | % Norma |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ID** | **Estación** | **Contaminante** | **Estadístico** | **Norma** | **ug/m3** | **ug/m3** | **ug/m3** | **ug/m3** |
| R_1 | Pozo Almonte | MP10 | Promedio Anual | 50 | 34,1 | 0,0350 | 34,1440 | 68% |
| R_1 | Pozo Almonte | MP10 | Percentil 98 | 150 | 65,6 | 0,0639 | 65,6936 | 44% |
| R_1 | Pozo Almonte | MP2,5 | Promedio Anual | 20 | 9,1 | 0,0077 | 9,1519 | 46% |
| R_1 | Pozo Almonte | MP2,5 | Percentil 98 | 50 | 17,6 | 0,0142 | 17,6281 | 35% |
| R_1 | Pozo Almonte | SO2 | Promedio Anual | 60 | 2,6 | 0,0001 | 2,6468 | 4% |
| R_1 | Pozo Almonte | SO2 | Percentil 99 - Diario | 150 | 5,8 | 0,0001 | 5,8098 | 4% |
| R_1 | Pozo Almonte | SO2 | Percentil 98,5 - Horario | 350 | 8,1 | 0,0003 | 8,0869 | 2% |
| R_1 | Pozo Almonte | SO2 | Promedio Anual | 80 | 2,6 | 0,0001 | 2,6468 | 3% |
| R_1 | Pozo Almonte | SO2 | Percentil 99,7 - Diario | 365 | 7,4 | 0,0002 | 7,4318 | 2% |
| R_1 | Pozo Almonte | SO2 | Percentil 99,73 - Horario | 1000 | 15,6 | 0,0004 | 15,6371 | 2% |
| R_2 | Soledad | SO2 | Promedio Anual | 60 | 4,3 | 0,0001 | 4,2825 | 7% |
| R_2 | Soledad | SO2 | Percentil 99 - Diario | 150 | 13,4 | 0,0001 | 13,4065 | 9% |
| R_2 | Soledad | SO2 | Percentil 98,5 - Horario | 350 | 15,6 | 0,0003 | 15,6436 | 4% |
| R_2 | Soledad | SO2 | Promedio Anual | 80 | 4,3 | 0,0001 | 4,2825 | 5% |
| R_2 | Soledad | SO2 | Percentil 99,7 - Diario | 365 | 19,0 | 0,0001 | 18,9864 | 5% |
| R_2 | Soledad | SO2 | Percentil 99,73 - Horario | 1000 | 27,2 | 0,0003 | 27,2403 | 3% |
| R_3 | Alto Hospicio | MP2,5 | Promedio Anual | 20 | 10,9 | 0,0023 | 10,8614 | 54% |
| R_3 | Alto Hospicio | MP2,5 | Percentil 98 | 50 | 19,8 | 0,0053 | 19,7837 | 40% |

<!-- Estadísticas: 19 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: MYMA, 2021 **REVISIÓN [0]** **55** -->
<!-- FIN TABLA 6-6 -->


### LISTADO DE FIGURAS

Figura 3-1: Representación gráfica del Modelo Tipo Puff y de Pluma. ............................................... 8

Figura 3-2: Dispersión de la Pluma a diferentes horas........................................................................ 9

Figura 3-3: Ciclos de formación de Ozono. ....................................................................................... 10

Figura 3-4: Esquema de Oxidación SO X y NO X. .................................................................................. 10

Figura 4-1: Topografía del sector. ..................................................................................................... 16

Figura 4-2: Ciclo diario y estacional de la temperatura observada y modelada. .............................. 19

Figura 4-3: Ciclo diario y mensual de la velocidad del viento observada y modelada. ..................... 21

**REVISIÓN [0]** **ii**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

Figura 4-4: Ciclo estacional horario de las direcciones promedio de los vientos [°] - Data Observada
y modelada. ....................................................................................................................................... 22

Figura 4-5: Ciclo estacional horario de las direcciones promedio de los vientos [°] - Data Observada
y modelada. ....................................................................................................................................... 23

Figura 4-6: Comparación frecuencias por dirección del viento. ....................................................... 28

Figura 4-7: Factor de corrección para cada estación en estudio. ..................................................... 29

Figura 5-1: Fuente de emisiones en el modelo - Fase de Construcción. .......................................... 31

Figura 5-2: Ubicación receptores discretos. ...................................................................................... 33

Figura 6-1: Curva isoconcentración - Fase de Construcción- MP 10 - Norma anual. ........................ 35

Figura 6-2: Curva isoconcentración - Fase de Construcción - MP 10 - Norma diaria (P98). ............. 36

Figura 6-3: Curva isoconcentración - Fase de Construcción - MP 2,5 - Norma anual. ...................... 37

Figura 6-4: Curva isoconcentración - Fase de Construcción- MP 2,5 - Norma diaria (P98). .............. 38

Figura 6-5: Curva isodepositación - Fase de Construcción - MPS - Norma mensual. ..................... 39

Figura 6-6: Curva isodepositación - Fase de Construcción - MPS - Norma Anual. .......................... 40

Figura 6-7: Curva isoconcentración - Fase de Construcción - SO 2 - Norma primaria anual. ........... 41

Figura 6-8: Curva isoconcentración - Fase de Construcción - SO 2 - Norma primaria diaria (P99). . 42

Figura 6-9: Curva isoconcentración - Fase de Construcción - SO 2 - Norma primaria horaria (P98,5).

........................................................................................................................................................... 43

Figura 6-10: Curva isoconcentración - Fase de Construcción - SO 2 - Norma secundaria diaria
(P99,7). .............................................................................................................................................. 44

Figura 6-11: Curva isoconcentración - Fase de Construcción - SO 2 - Norma secundaria horaria
(P99,73). ............................................................................................................................................ 45

Figura 6-12: Curva isoconcentración - Fase de Construcción - NO 2 - Norma anual. ...................... 46

Figura 6-13: Curva isoconcentración - Fase de Construcción - NO 2 - Norma horaria (P99). .......... 47

Figura 6-14: Curva isoconcentración - Fase de Construcción - CO - horaria (P99). ........................ 48

Figura 6-15: Curva isoconcentración - Fase de Construcción - CO - 8 horas (P99). ........................ 49

Figura 6-16: Localización de Puntos de Máxima Concentración. ...................................................... 51

### LISTADO APÉNDICES

Apéndice 2.2-1: Archivos Digitales de Modelación

**REVISIÓN [0]** **iii**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

### 1 INTRODUCCIÓN

El presente Anexo corresponde a la Modelación de Dispersión de Contaminantes del Proyecto

“Parque Solar Fotovoltaico Soledad”, en adelante “el Proyecto”, presentado por SCM COSAYACH

Yodo, en adelante “el Titular”.

El Proyecto que se presenta a evaluación contempla la construcción y operación de un Parque

Solar, constituido por 13.312 paneles fotovoltaicos de 445 Wp cada uno; que en conjunto tendrán

una potencia nominal de generación de 5,55 MW destinada para la operación y consumo de

energía eléctrica de la Faena Soledad, por un periodo de 25 años.

El parque solar se ubica en la Región de Tarapacá, Provincia del Tamarugal, Comuna de Pozo

Almonte. Al respecto, cabe destacar que, la zona de estudio, ni los sectores cercanos a ella, se

encuentran declarados como Zona de Latencia o Zona de Saturación por superación los límites de

concentración establecidos por las normas primarias de calidad del aire, por lo que no existen

planes de prevención o descontaminación que el proyecto deba cumplir.

La modelación fue realizada siguiendo los lineamientos de la _“Guía para el uso de modelos de_

_calidad del aire en el SEIA”_ (2012), en base a la metodología WRF-Calpuff y considera la evaluación

del escenario más desfavorable del Proyecto, correspondiente a la construcción del Proyecto, de

acuerdo con los antecedentes descritos en el Anexo 2.1: Inventario de Emisiones Atmosféricas del

presente DIA. Cabe destacar que el Proyecto corresponde a uno nuevo, y no una modificación de

una operación ya existente, por lo que no se considera la evaluación de un Caso Base, y los aportes

en de concentraciones y depositaciones (MPS) son sometidos a evaluación ambiental en su

totalidad, tanto en los receptores sensibles como en la grilla de modelación.

Los contaminantes considerados en esta modelación de emisiones corresponden al material

particulado (MPS, MP 10 y MP 2,5 ) y los siguientes gases: dióxidos de nitrógeno (NO 2 ), dióxidos de

azufre (SO 2 ) y monóxido de carbono (CO).

El dominio de modelación meteorológica definido corresponde a un área de 100 km x 100 km, en

él se han identificado como receptores de interés estaciones de monitoreo cercanas al Proyecto.

**REVISIÓN [0]** **4**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

### 2 ANTECEDENTES GENERALES DEL PROYECTO

**2.1** **Descripción del Proyecto**

El Proyecto se estructura en tres fases, correspondientes a las de Construcción, Operación y Cierre,

las cuales son descritas en los siguientes apartados, en donde se presenta las emisiones

resultantes y un resumen por año.

**2.2** **Emisiones**

**2.2.1** **Fase de Construcción**

A continuación, se resumen de emisiones para la Fase de Construcción:

**Tabla 2-1: Resumen de emisiones - Fase de Construcción.**

|Obra/actividad|Emisiones [t/año]|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Obra/actividad**|**MPS**|**MP10 **|**MP25 **|**NOX **|**SO2 **|**CO**|**HC/COV**|**NH3 **|
|**Excavación**|15,47|3,48|1,62|--|--|--|--|--|
|**Transferencia de material**|1,64|0,78|0,12|--|--|--|--|--|
|**Nivelación**|0,09|0,03|0,00|--|--|--|--|--|
|**Compactación**|1,42|0,32|0,15|--|--|--|--|--|
|**Perforaciones**|0,89|0,27|0,04|--|--|--|--|--|
|**Maquinaria [75 ≤ P < 130]**|0,06|0,06|0,06|0,72|<0,01|0,38|0,07|<0,01|
|**Maquinaria [130 ≤ P < 560]**|0,13|0,13|0,13|2,86|0,01|1,51|0,27|<0,01|
|**Grupo electrógeno**|0,35|0,35|0,32|4,87|0,32|1,05|<0,01|<0,01|
|**Vehículos en caminos pavimentados**|6,99|1,34|0,32|--|--|--|--|--|
|**Vehículos en caminos industriales NO pavimentados**|154,33|47,25|4,72|--|--|--|--|--|
|**Motor vehículos Camionetas**|<0,01|<0,01|<0,01|0,02|<0,01|0,01|<0,01|<0,01|
|**Motor vehículos Buses**|<0,01|<0,01|<0,01|0,10|<0,01|<0,01|<0,01|<0,01|
|**Motor vehículos Pesados [> 32 t]**|<0,01|<0,01|<0,01|0,60|<0,01|0,02|<0,01|<0,01|
|**Total**|**181,37**|**54,00**|**7,50**|**9,18**|**0,33**|**2,97**|**0,34**|**<0,01**|

Fuente: Anexo 2.1: Inventario de Emisiones Atmosféricas del presente DIA.

**REVISIÓN [0]** **5**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

**2.2.2** **Fase de Operación**

A continuación, se resumen las emisiones para la Fase de Operación:

**Tabla 2-2: Resumen de emisiones - Fase de Operación.**

|Actividad|Emisiones [t/año]|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Actividad**|**MPS**|**MP10 **|**MP25 **|**NOX **|**SO2 **|**CO**|**HC/COV**|**NH3 **|
|**Vehículos en caminos pavimentados**|0,5754|0,1104|0,0267|--|--|--|--|--|
|**Vehículos en caminos industriales NO pav.**|36,102|11,051|1,1052|--|--|--|--|--|
|**Motor vehículos Camionetas**|0,0012|0,0012|0,0012|0,0251|0,0001|0,0113|0,0011|<0,0001|
|**Motor vehículos Pesados**|0,0003|0,0003|0,0003|0,0436|0,0001|0,0011|0,0001|<0,0001|
|**Total**|**36,678**|**11,163**|**1,133**|**0,068**|**0,000**|**0,012**|**0,001 **|**0,000**|

Fuente: Anexo 2.1: Inventario de Emisiones Atmosféricas del presente DIA.

**2.2.3** **Fase de Cierre**

A continuación, se detalla el resumen de emisiones para la Fase de Cierre.

**Tabla 2-3: Resumen de emisiones - Fase de Cierre.**

|Actividad|MPS|MP<br>10|MP<br>25|NO<br>X|SO<br>2|CO|HC/COV|NH<br>3|
|---|---|---|---|---|---|---|---|---|
|**Transferencia de material**|1,64|0,78|0,12|0,00|--|--|--|--|
|**Nivelación**|0,09|0,03|0,00|0,00|--|--|--|--|
|**Maquinaria [75 ≤ P < 130]**|0,06|0,06|0,06|0,72|<0,01|0,38|0,07|<0,01|
|**Maquinaria [130 ≤ P < 560]**|0,13|0,13|0,13|2,86|0,01|1,51|0,27|<0,01|
|**Vehículos en caminos pavimentados**|6,99|1,34|0,32|0,00|--|--|--|--|
|**Vehículos en caminos industriales NO pavimentados**|154,33|47,25|4,72|0,00|--|--|--|--|
|**Motor vehículos Camionetas**|<0,01|<0,01|<0,01|0,02|<0,01|<0,01|<0,01|<0,01|
|**Motor vehículos Buses**|<0,01|<0,01|<0,01|0,10|<0,01|<0,01|<0,01|<0,01|
|**Motor vehículos Pesados [> 32 t]**|<0,01|<0,01|<0,01|0,60|<0,01|0,02|<0,01|<0,01|
|**Total**|**163,25**|**49,59**|**5,37**|**4,30**|**0,01**|**1,92**|**0,34**|**<0,01**|

Fuente: Anexo 2.1: Inventario de Emisiones Atmosféricas del presente DIA.

**REVISIÓN [0]** **6**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

### 3 DESCRIPCIÓN Y JUSTIFICACIÓN DEL MODELO Y LOS CONTAMINATES CONSIDERADOS

**3.1** **Justificación del modelo seleccionado**

La metodología utilizada para evaluar el impacto de las emisiones en el área de estudio

corresponde al sistema integrado “WRF-CALPUFF”. La elección de este tipo de sistema se basa en

las recomendaciones dadas en el punto 4.2 de la _“Guía para el uso de modelos de calidad del aire_

_en el SEIA”_ (2012), dado que las emisiones a considerar corresponden a emisiones de tipo

primarias, provenientes desde una fuente de emisión, en una superficie, o dominio de

modelación, de más de 5 kilómetros, entre fuentes y receptores.

El sistema de modelación, tal como su nombre lo indica, incluye dos componentes principales:

WRF y CALPUFF, además de una larga selección de preprocesadores, diseñados para incluir en el

modelo datos geofísicos y de usos de suelos, y postprocesadores como por ejemplo CALPOST, que

permiten convertir los resultados a los estadísticos considerados por las normas primarias y

secundarias de calidad del aire.

Respecto del **WRF** (Weather Research and Forecasting), tal como su nombre lo indica,

corresponde a un conjunto de datos (modelo numérico) de predicción meteorológica que permite

representar las condiciones climáticas de momento y lugar determinado. Este modelo ha sido

desarrollado por el NCAR (National Center for Atmospheric Research) y la NOAA (National Oceanic

and Atmospheric Administration) de los Estados Unidos.

El WRF es el modelo meteorológico recomendado por él SEA, del Gobierno de Chile, para la

generación de meteorología para estudios de calidad del aire. Lo anterior dado que, además de

sus avanzadas características, se ha ocupado en la mayoría de los Proyectos relacionados con

modelación atmosférica en cargados por organismos estatales de Chile, por lo que existe una

vasta experiencia de su aplicación en el País.

Por otra parte, **CALPUFF** es un modelo tipo “puff” Lagrangiano Gaussiano no estacionario capaz de

modelar el transporte y dispersión de contaminantes.

Los modelos tipo “puff” representan una pluma de contaminantes continua como un número

discreto de paquetes de material contaminante, tal como se muestra la siguiente figura:

**REVISIÓN [0]** **7**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

**Figura 3-1: Representación gráfica del Modelo Tipo Puff y de Pluma.**

Fuente: Asian Pacific Air Quality Group (APAQ Group), 2019.

El modelo evalúa la contribución de un “puff” en la concentración atmosférica de un punto de la

grilla en un instante determinado, para luego permitir que el “puff” se mueva, evolucione en

tamaño, fuerza, etc., hasta la próxima iteración, en el próxima punto de la grilla, respondiendo a la

meteorología del sector en la que se encuentre inmerso el “puff” en cada instante. Luego, la

concentración total en un receptor resultará de la sumatoria de las contribuciones de todos los

“puff”. La ecuación básica del modelo se muestra a continuación:

[ ( )] [ ( )]

( )

) ( )]
∑ [ (

Dónde:

C: Concentración (g/m [3] );

Q: Masa del contaminante en el “puff” (g);

σx: Coeficiente de dispersión en dirección del viento (m);

σy: Coeficiente de dispersión en dirección perpendicular al viento (m);

σz: Coeficiente de dispersión vertical (m);

da: Distancia desde el centro del “puff” hacia el receptor en el eje de la dirección del

viento (m);

dc: Distancia desde el centro del “puff” hacia el receptor en el eje perpendicular a la

dirección del viento (m);

g: Altura de la ecuación gaussiana (m);

H: Altura efectiva del “puff” (m);

h: Altura de la capa de mezcla (m).

**REVISIÓN [0]** **8**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

Para casos que involucran un alto grado de variabilidad espacial del flujo dentro de la capa límite,

tales como flujos ascendentes o descendentes o flujos a lo largo de un valle fluvial sinuoso, la

suposición de estado estacionario en línea recta puede ser poco válida incluso a algunos

kilómetros de la fuente, por lo que un modelo de puff puede ser el más apropiado.

Un modelo de tipo “puff” libera emisiones independientes de la fuente, a diferencia del modelo de

pluma, permitiendo que la bocanada responda a la meteorología que la rodea. Esto también

permite rastreos a través de múltiples períodos de muestreo hasta que se haya diluido

completamente o se haya rastreado en todo el dominio de modelado, tal como se observa en la

siguiente figura:

**Figura 3-2: Dispersión de la Pluma a diferentes horas.**

Fuente: Asian Pacific Air Quality Group (APAQ Group), 2019.

**3.2** **Justificación de los contaminantes por modelar**

Tal como está detallado en el inventario de emisiones del Proyecto, este en sus fases de

Construcción, Operación y Cierre generará emisiones primarias, directas desde sus fuentes, de los

contaminantes SO 2, NO 2, CO, HC/COVs, MPS, MP 10 y MP 2,5, propias de las actividades

correspondientes al proyecto, asociadas principalmente a movimientos de tierra, a las

maquinarias y a las generadas por el tránsito de Vehículos por caminos pavimentados y no

pavimentados.

Por otra parte, se encuentran los contaminantes secundarios, que corresponden a los

contaminantes que no se emite directamente de las fuentes emisoras, sino que, se produce por la

reacción de contaminantes primarios (emitidos directamente por la fuente emisora) con

contaminantes precursores que se encuentran en la atmósfera.

Uno de los principales contaminantes secundarios corresponde al Ozono (O 3 ), el cual necesita

como precursores NO X (NO + NO 2 ) y Compuestos Orgánicos Volátiles (COV) para su formación. En

la siguiente figura se presenta un esquema resumido de las reacciones involucradas en la

conversión de NO a NO 2 y formación de Ozono (O 3 ). El ciclo A, corresponde al ciclo NO-NO 2 -O 3 en

ausencia de COV, mientras que en el ciclo B se presenta el ciclo A con presencia de COV, siendo hv

la radiación solar necesaria para llevar a cabo la reacción. Las reacciones para la formación de

ozono como contaminante secundario son analizadas en detalle en el Anexo 2 de la “Guía para el

uso de modelos de calidad del aire en el SEIA”.

**REVISIÓN [0]** **9**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

**Figura 3-3: Ciclos de formación de Ozono.**

Fuente: Atkinson, 2000.

Así también, otros contaminantes atmosféricos que poseen origen secundario son los nitratos y

sulfatos que corresponden partículas sólidas (material particulado) cuyos precursores son los

óxidos de nitrógeno (NO X ) y óxidos de azufre (SO X ). En la siguiente figura se presenta el esquema

de oxidación para la formación de material particulado secundario (sulfatos y nitratos).

**Figura 3-4: Esquema de Oxidación SO** **X** **y NO** **X.**

Fuente: User’s Guide CALPUFF.

Respecto de los contaminantes secundarios como el Ozono, de acuerdo con lo indicado en el

punto 4.2.c de la “Guía para el Uso de Modelos de Calidad del Aire en el SEIA”, para su modelación

se requiere de la aplicación de complejos modelos fotoquímicos del tipo WRFChem, CAMx o

CMAQ cuyo uso debe analizarse caso a caso, considerando la magnitud del Proyecto y sus

impactos ambientales potenciales.

En base a lo presentado en los párrafos anteriores:

1) En virtud de la magnitud de las emisiones de óxidos de nitrógeno (NO X ) y compuestos

orgánicos volátiles (COV) que genera el Proyecto, la condición de NO saturación del

**REVISIÓN [0]** **10**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

contaminante Ozono en la zona de estudio, según lo indicado en la “Guía para el Uso de

Modelos de Calidad del Aire en el SEIA”, el presente Proyecto no cumple con las

características para generar un potencial impacto por formación de Ozono, por lo que no

requiere de una modelación de este contaminante secundario;

2) Se considera una modelación tipo PUFF de contaminantes primarios con una

transformación RIVAD, que permite considerar la formación de material particulado desde

los nitratos y sulfatos;

3) Por lo que, los contaminantes considerados para la modelación, en base a las

características del Proyecto, corresponden a SO 2, NO 2, CO, MPS, MP 10 (primarios y

secundarios por nitratos y sulfatos) y MP 2,5 (primarios y secundarios por nitratos y

sulfatos).

En base a lo anterior, en el siguiente apartado se detalla la norma de calidad del aire de los

contaminantes considerados.

**3.3** **Norma de calidad del aire**

Para realizar la evaluación de los aportes de concentraciones sobre la calidad del aire monitoreado

en la zona se ha considerado la normativa ambiental primaria y secundaria de calidad de aire

vigente para MPS, MP 10, MP 2,5, NO 2, SO 2 y CO, presentadas en las siguientes tablas:

**REVISIÓN [0]** **11**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

**Tabla 3-1: Norma primaria de calidad del aire.**

|Parámetro|Cuerpo Legal|Estadístico|Valor|
|---|---|---|---|
|**MP10 **|D.S. N°59/98 del<br>MINSEGPRES,<br>modificada por<br>D.S.N°45/01 del<br>MINSEGPRES|Promedio aritmético de tres años calendario consecutivos|50<br>μg/m3|
|**MP10 **|D.S. N°59/98 del<br>MINSEGPRES,<br>modificada por<br>D.S.N°45/01 del<br>MINSEGPRES|Percentil 98 de las concentraciones de 24 horas registradas durante un<br>período anual|150<br>μg/m3|
|**MP2,5 **|D.S. N°12/11 del<br>MMA|Promedio tri-anual de las concentraciones anuales|20<br>μg/m3|
|**MP2,5 **|D.S. N°12/11 del<br>MMA|Percentil 98 de los promedios diarios registrados durante un año|50<br>μg/m3|
|**NO2 **|D.S. N° 114/2002<br>del MINSEGPRES|Promedio aritmético de los valores de concentración anual de tres años<br>calendarios sucesivos|100<br>μg/m3|
|**NO2 **|D.S. N° 114/2002<br>del MINSEGPRES|Promedio aritmético de tres años sucesivos del percentil 99 de los<br>máximos diarios de concentración de 1 hora registrados durante un año<br>calendario|400<br>μg/m3|
|**SO2 **|D.S. N° 104/2019<br>del MMA|Promedio aritmético de tres años sucesivos del percentil 99 de las<br>concentraciones de 24 horas registradas durante un año calendario|150<br>μg/m3|
|**SO2 **|D.S. N° 104/2019<br>del MMA|Promedio aritmético de los valores de concentración anual tres años<br>calendario sucesivos|60<br>μg/m3|
|**SO2 **|D.S. N° 104/2019<br>del MMA|Promedio aritmético de tres años sucesivos del percentil 98,5 de las<br>concentraciones horarias registradas durante un año calendario|350<br>μg/m3|
|**CO**|D.S. N° 115/2002<br>del MINSEGPRES|Promedio aritmético de tres años sucesivos del percentil 99 de los<br>máximos diarios de concentración de 1 hora registrados durante un año<br>calendario|30<br>mg/m3|
|**CO**|D.S. N° 115/2002<br>del MINSEGPRES|Promedio aritmético de tres años sucesivos del percentil 99 de los<br>máximos diarios de concentración de 8 horas (promedio móvil)<br>registrados durante un año calendario|10<br>mg/m3|

Fuente: MYMA, 2021.

**Tabla 3-2: Norma secundaria de calidad del aire para el SO** **2** **y norma de referencia para el MPS.**

|Parámetro|Cuerpo Legal|Estadístico|Valor|
|---|---|---|---|
|**SO2 **|D.S N° 22/10 del<br>MINSEGPRES|Promedio aritmético de tres años calendario sucesivos del<br>Percentil 99,73 de la concentración máxima de horaria|1.000<br>μg/m3|
|**SO2 **|D.S N° 22/10 del<br>MINSEGPRES|Promedio aritmético anual|80<br>μg/m3|
|**SO2 **|D.S N° 22/10 del<br>MINSEGPRES|Promedio aritmético de tres años calendario sucesivos del<br>Percentil 99,7 de las concentraciones diarias|365<br>μg/m3|
|**MPS**|Norma Suiza|Promedio aritmético mensual|200<br>mg/m2día|
|**MPS**|Norma Suiza|Promedio aritmético anual|100<br>mg/m2día|

Fuente: MYMA, 2021.

**REVISIÓN [0]** **12**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

### 4 CONFIGURACIÓN DEL MODELO Y ANÁLISIS DE INCERTIDUMBRE

En esta sección se presenta las principales definiciones que permiten configuración el modelo, las

cuales permiten obtener los resultados de concentraciones y depositaciones en el área de estudio.

Así también se caracteriza el domino seleccionado.

**4.1** **Características del dominio de modelación y su entorno**

**4.1.1** **Dominio de modelación**

El dominio de modelación se compone de dos tipos de dominios, el meteorológico y el

computacional: El dominio meteorológico comprende un área de 100 km x 100 km,

correspondiente a la grilla del WRF ocupado, mientras que; El dominio computacional comprende

un área de 54 km x 41 km, que correspondiente a un área seleccionada para modelar, donde se

ubican las partes, obras y acciones del Proyecto, así como, también los receptores sensibles del

área de estudio.

**4.1.2** **Configuración del modelo**

El detalle de la configuración del modelo de dispersión de contaminantes se encuentra disponible

en el archivo denominado CALPUFF.INP (Apéndice), el cual corresponde a un archivo de texto que

permite ver las características o configuraciones de la modelación realizada. El archivo se

estructura de acuerdo con lo que se presenta en la siguiente tabla:

**Tabla 4-1: Descripción del archivo *.INP.**

|ID|Descripción|
|---|---|
|*|Nombre de la modelación realizada.|
|0|Nombre de archivos de entrada y salida de la modelación.|
|1|Parámetros de control generales de la corrida: Fecha y hora de inicio, duración de la ejecución, frecuencia<br>temporal. Número de contaminantes. Configuración de reinicio para realizar una serie de ejecuciones de<br>continuación. Formato de datos meteorológicos y ajuste de tiempo promedio.|
|2|Opciones Técnicas. Variables de control que determinan los métodos para el tratamiento de la química,<br>deposición húmeda, depositación seca, dispersión, aumento de pluma, terreno.|
|3 a,b|Listado de especies. Nombres de especies, especies habilitadas, emitidas y depositadas en seco.|
|4|Parámetros de control de cuadrícula. Especificación de cuadrículas meteorológicas, computacionales y de<br>muestreo, número de celdas, capas verticales y coordenadas de referencia.|
|5|Opciones de salida. Variables de control de impresión, variables de control de salida del disco.|
|6a, b, c|Configuración del terreno complejo a escala de subcuadrícula (CTSG). Información que describe la ubicación, la<br>forma y la altura de la colina a escala de subcuadrícula. Ubicaciones y altitud de receptores.|
|7|Parámetros de deposición seca- Gases. Difusividad de contaminantes, constante de disociación, reactividad,<br>resistencia al mesófilo, coeficiente de la ley de Henry.|
|8|Parámetros de deposición seca - Partículas. Diámetro medio de masa geométrica.|

**REVISIÓN [0]** **13**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

|ID|Descripción|
|---|---|
|9|Parámetros misceláneos de deposición seca. Resistencias de la cutícula y del suelo de referencia, reactividad<br>del contaminante de referencia, estado de la vegetación.|
|10|Parámetros de deposición húmeda. Coeficientes de barrido para cada contaminante y tipo de precipitación<br>(precipitación líquida y congelada).|
|11|Parámetros Químicos. Variables de control para la entrada de datos de ozono, concentraciones de fondo de<br>ozono y amoníaco, tasas de transformación nocturna.|
|12|Varios parámetros de dispersión y parámetros computacionales. Constantes de dispersión vertical, tasa de<br>dispersión por encima de la capa límite, distancia de cruce a coeficientes de dispersión dependientes del<br>tiempo, uso del suelo asociado con la dispersión urbana, controles de división de bocanadas, coeficientes de<br>trayectoria de la pluma, ley de potencia de la velocidad del viento, gradientes de temperatura y otros.|
|13a,b,<br>c|Parámetros de fuente puntual. Datos de fuentes puntuales, incluida la ubicación de la fuente, la elevación, los<br>parámetros de la chimenea, las emisiones, las unidades, las dimensiones del edificio, el ciclo de emisiones.|
|14a,b,<br>c|Parámetros de fuente de área. Datos de la fuente del área, incluida la ubicación de la fuente, la altura efectiva,<br>la elevación, los sigmas iniciales, las emisiones, las unidades, el ciclo de emisiones variables.|
|15a,b,<br>c|Parámetros de fuente lineal. Datos de la fuente como la ubicación de la fuente, la elevación, la longitud de la<br>línea, los parámetros de flotabilidad, la altura de liberación, las emisiones, las unidades, el ciclo de emisiones.|
|16a,b,<br>c|Parámetros de fuente de volumen. Datos de la fuente de volumen, incluida la ubicación de la fuente, la<br>elevación, la altura efectiva, los datos de tamaño inicial, las emisiones, las unidades, el ciclo de emisiones.|
|17a,b,|Información del receptor sin cuadrícula (discreta). Coordenadas del receptor y elevación del suelo.|

Fuente: A User’s Guide for the CALPUFF Dispersion Model.

**4.1.3** **Meteorología**

La meteorología del sector se incorpora mediante el uso de un modelo meteorológico WRF. La

configuración utilizada es detallada a continuación, en la Tabla 4-2.

**Tabla 4-2: Detalle de Proyección cartográfica y coordenadas Archivo WRF.**

|Proyección Cartográfica|Cónica conforme de Lambert (LCC)|
|---|---|
|Período|1 Ene 2020 00:00 - 1 Ene 2021 20:00|
|Origen|RLAT0 = 20,181S<br>RLAN0 = 69,770W<br>XLAT1= 19,871S<br>XLAT2 = 20,491S|
|Proyección|Lambert Conic Conformal|
|Datum|NWS-84 6370 km Radius, Global Sphere|
|Grilla|100 x 100 km|
|Resolución|1 x 1 km2|
|Celdas verticales|10|

Fuente: MYMA, 2021.

Las variables meteorológicas que contiene el modelo para toda el área de estudio corresponden a

las siguientes:

 - Campos de viento (Vectores);

 - Temperatura del aire (K);

 - Clases de Estabilidad;

 - Velocidad de fricción en la superficie (m/s);

**REVISIÓN [0]** **14**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

 - Altura de Capa de Mezcla (m);

 - Longitud de Monin-Obukhov (m);

 - Escala de velocidad convectiva (m/s);

 - Rango de precipitación (mm/hr);

 - Temperatura de superficie (K);

 - Densidad del aire (kg/m [3] );

 - Radiación solar (W/m [2] );

 - Humedad relativa (%);

 - Uso de suelo;

 - Índice de cobertura foliar;

 - Rugosidad superficial.

**4.1.4** **Topografía**

La topografía del área de estudio se ha extraído de Shuttle Radar Topography Mission, más

conocido como SRTM1, cuya resolución es aproximadamente 30 metros x 30 metros. El archivo

SRTM1 ha sido incorporado al modelo con el objetivo de proporcionar la altura de los puntos de

interés, correspondientes tanto a las fuentes como los receptores.

En la siguiente figura se presenta una imagen que grafica la topografía utilizada, en donde se

observa que: las mayores alturas del dominio de modelación se concentran hacia el este de la

figura, en la Cordillera de los Andes; las principales fuentes del Proyecto se encuentran una altura

aproximadamente de entre los 300 msnm y los 1300 metros sobre el nivel medio del mar.

**REVISIÓN [0]** **15**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

**Figura 4-1: Topografía del sector.**

Fuente: MYMA, 2021.

**REVISIÓN [0]** **16**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

**4.2** **Análisis de Incertidumbre del modelo WRF**

La modelación de la atmósfera está basada en uno de los mejores modelos meteorológicos

disponibles en la actualidad, correspondiente al WRF, el cual cuenta con un gran número de

parametrizaciones, las cuales, si son adecuadamente seleccionadas e implementadas, simulan de

muy buena manera gran parte de los procesos meteorológicos de meso-escala.

Cabe señalar que, independiente de las bondades del modelo utilizado, todo resultado obtenido

desde un modelo atmosférico requiere ser sometido a un proceso de validación, el que debe

desarrollarse para la condición meteorológica y de terreno descrita para el área a modelar. Este

proceso permite la detección de posibles inexactitudes en los datos modelados a partir de la

información meteorológica obtenida, dado que una mala implementación de alguna

parametrización puede llevar a errores significativos en la estimación de los vientos en superficie

y, con esto, de las trayectorias de los contaminantes atmosféricos por modelar, siendo así de esta

manera, subestimadas o sobreestimadas las concentraciones de los contaminantes modelados.

La metodología denominada “Análisis de Incertidumbre” tiene por objeto detectar las diferencias

entre el modelo meteorológico y la meteorología observada, estableciendo un factor de

corrección (FC), en caso de ser necesario, que permita compensar las concentraciones modeladas

de manera subestimadas en un determinado receptor.

Para realizar el análisis de incertidumbre se consideran las recomendaciones establecidas en la

Guía de modelación, donde, en su acápite 7, se menciona que cualquier modelo representa una

aproximación a la realidad y sus resultados tienen incertidumbres asociadas, las cuales se

expresan a través de diferencias entre lo estimado y lo observado.

El proceso consiste en evaluar en comparar cualitativa y cuantitativamente las variables

meteorológicas de mayor incidencia en el transporte de contaminantes, mediante métodos

cualitativos, cuantitativos y mediante técnicas estadísticas. En base a lo anterior, a continuación,

se presenta el análisis de incertidumbre en donde:

 - Primero, se realiza un análisis cualitativo en base a las series de tiempo, ciclos diarios y

ciclos anuales de las variables dirección y velocidad del viento, y temperatura para los

datos observados y modelados;

 - Segundo, se presenta un análisis cuantitativo estadístico, y finalmente;

 - Tercero, se presenta conclusiones respecto de los datos observados y del análisis de

incertidumbre.

La estación considerada para el análisis corresponde a la que se presenta en la siguiente Tabla 4-3,

en donde se indican los parámetros monitoreados y se detallan las coordenadas geográficas de su

localización. Además, de este mismo punto, desde el modelo meteorológico WRF, se obtuvieron

los datos modelados para el análisis de incertidumbre.

**REVISIÓN [0]** **17**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

**Tabla 4-3: Parámetros meteorológicos utilizados en el análisis de incertidumbre.**

|Estación|Ubicación (Datum WGS84 - Huso 19S)|Col3|Parámetros|Año|
|---|---|---|---|---|
|**Estación**|**Este (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|
|Pozo Almonte|417.709|7.760.617|Velocidad del Viento|2020|
|Pozo Almonte|417.709|7.760.617|Dirección del Viento|Dirección del Viento|
|Pozo Almonte|417.709|7.760.617|Temperatura Ambiental|Temperatura Ambiental|
|Soledad|427.160|7.739.828|Velocidad del Viento|2020|
|Soledad|427.160|7.739.828|Dirección del Viento|Dirección del Viento|
|Soledad|427.160|7.739.828|Temperatura Ambiental|Temperatura Ambiental|
|Alto Hospicio|385.118|7.755.989|Velocidad del Viento|2020|
|Alto Hospicio|385.118|7.755.989|Dirección del Viento|Dirección del Viento|
|Alto Hospicio|385.118|7.755.989|Temperatura Ambiental|Temperatura Ambiental|

Fuente: Elaboración propia en base a registros de la SMA.

Adicionalmente, cabe destacar que, de acuerdo con los requerimientos del Servicio de Evaluación

Ambiental (SEA) en su _“Guía para el uso de modelos de calidad del aire en el SEIA_ ” (2012) _,_ esta

estación de monitoreo cumple con el porcentaje mínimo de datos válidos de las variables

meteorológicas, correspondiente a un mínimo de 75% de los registros.

Respecto a los datos meteorológicos obtenidos del modelo es importante destacar que estos

también corresponden a datos del año 2020.

**4.2.1** **Análisis cualitativo**

A continuación, se detalla una comparación cualitativa de las variables dirección del viento,

velocidad del viento y temperatura, en sus ciclos diarios y mensuales, entre los registros de la

estación de monitoreo (datos observados) y lo registros pronosticado por el modelo WRF (datos

modelados), para la misma localización, con el fin de evaluar la capacidad predictiva del modelo.

**4.2.1.1** **Temperatura**

A continuación, para la variable meteorológica temperatura, en la Figura 4-2, se presenta el ciclo

diario promedio junto con el ciclo mensual promedio, en donde se agregan áreas que representan

el 90% de la muestra, es decir los datos que se encuentran entre los percentiles 5 y 95.

**REVISIÓN [0]** **18**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

**Figura 4-2: Ciclo diario y estacional de la temperatura observada y modelada.**

|Pozo Almonte|Col2|
|---|---|
|||
|**Soledad**|**Soledad**|
|||
|**Alto Hospicio**|**Alto Hospicio**|
|||

Fuente: MYMA, 2021.

En relación con las figura del ciclo diario de la temperatura observada y modelada, es posible

indicar que el modelo se adapta de buena forma a la realidad, ya que, además de reproducir la

variación promedio a través de las horas del día, también reproduce de buena manera el 90% de la

data. Respecto de esta variable, la estación que se adapta en menor medida corresponde a la de

Alto Hospicio.

Lo anterior, ya que los datos modelados reproducen correctamente el ciclo horario de la

temperatura, en el que los valores máximos se presentan en horas de las tarde, cercano a las

14:00, que posteriormente comienzan gradualmente a disminuir, hasta alcanzar los datos más

bajos a eso de las 07:00 AM, para luego comenzar con el incremento gradual nuevamente.

Ahora bien, también en la figura es posible apreciar que el modelo subestima los valores

extremos, dado que se subestiman los valores más altos en aproximadamente 3 [°C], que se

presentan a las 14:00 horas aproximadamente.

**REVISIÓN [0]** **19**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

Respecto a la variación mensual de la temperatura, es posible indicar que, al igual que para la

variación diaria, el modelo simula correctamente los valores promedio, pero subestima

ligeramente los valores extremos, de practicante todos los meses del año.

**4.2.1.2** **Velocidad del viento**

A continuación, para la variable meteorológica velocidad del viento, en las siguientes dos figuras

se presentan el ciclo diario promedio junto con el ciclo mensual promedio en metros por segundo,

en donde se agregan áreas que representan el 90% de la muestra, es decir los datos que se

encuentran entre los percentiles 5 y 95.

En relación con la figura del ciclo diario de la velocidad del viento observada y modelada, es

posible indicar que el modelo se adapta de buena forma a la realidad, ya que logra reproducir la

variación promedio a través de las horas del día. Lo anterior, ya que los datos modelados

reproducen correctamente el ciclo horario de la temperatura, en el que los valores máximos se

presentan en horas de las tarde, entre las 15:00 y las 16:00 hr de la tarde, y que posteriormente

comienzan gradualmente a disminuir, hasta alcanzar los datos más bajos, cercanos a los calmos,

entre las 00:00 y las 07:00 AM, para luego comenzar un incremento gradual nuevamente.

Ahora bien, también en las figuras de los ciclos horarios es posible apreciar que el modelo sobre

estima las velocidades de los vientos para las estacones de Alto Hospicio y Solado en

aproximadamente 2 m/s.

Respecto a la variación mensual de la velocidad del viento, es posible apreciar que, al igual que

para la variación diaria, el modelo simula correctamente la tendencia mensual de los valores

promedio, solo sobre estimando los valores extremos, en menos de 2 m/s, en las estaciones de

Soledad y Alto Hospicio.

**REVISIÓN [0]** **20**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

**Figura 4-3: Ciclo diario y mensual de la velocidad del viento observada y modelada.**

|Pozo Almonte|Col2|
|---|---|
|||
|**Soledad**|**Soledad**|
|||
|**Alto Hospicio**|**Alto Hospicio**|
|||

Fuente: MYMA, 2021.

**4.2.1.3** **Dirección del viento**

A continuación, en la siguiente figura, se ilustra las frecuencias acumuladas por dirección del

viento para el ciclo horario diario.

De las figuras de vientos presentadas es posible que el modelo simule claramente las tendencias

de las direcciones de los vientos en su variación horaria y mensual. En ella se observa que se

representan claramente las predominancias de los vientos, así como las influencia oceánica sobre

los vientos, que produce la variación día y noche, que se aprecia más marcada en las estaciones

Alto Hospicio y Pozo Almonte.

**REVISIÓN [0]** **21**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

**Figura 4-4: Ciclo estacional horario de las direcciones promedio de los vientos [°] - Data Observada y modelada.**

|Estación Soledad|Col2|
|---|---|
|||
|**Estación Pozo Almonte**|**Estación Pozo Almonte**|
|||

Fuente: MYMA, 2021.

**REVISIÓN [0]** **22**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

**Figura 4-5: Ciclo estacional horario de las direcciones promedio de los vientos [°] - Data Observada y modelada.**

|Estación Alto Hospicio|Col2|
|---|---|
|||

Fuente: MYMA, 2021.

**REVISIÓN [0]** **23**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

**4.2.2** **Análisis Cuantitativo**

A continuación, tal como lo recomienda la _“Guía para el uso de modelos de Calidad del Aire en el_

_SEIA”_ (2012), se realiza el análisis cuantitativo de la incertidumbre del modelo en base los
estadígrafos Sesgo (BIAS), el Índice de Ajuste (IOA), el Error Bruto Medio (MGE), el Coeficiente de

Correlación (r) y el Error Medio Cuadrático (RMSE), y mediante el establecimiento de un Factor de

Corrección, lo que es detallado en la siguiente metodología:

_**4.2.2.1**_ _**Metodología**_

La metodología de análisis de incertidumbre de los datos meteorológicos modelados frente a los

observados se desarrolla por medio de la comparación de diversos parámetros estadísticos

estimados frente a rangos de aceptabilidad. Complementariamente, en caso de que estos rangos

de aceptabilidad sean superados se establece un factor de corrección (FC) que permita suplir este

sobre o subestimación.

**a.** _**Sesgo**_ **(BIAS)**

Proporciona información sobre la tendencia del modelo WRF a sobreestimar o subestimar las

condiciones reales de una variable, cuantificando el error sistemático del modelo. Los resultados a

obtener se comparan con respecto a si son negativos o positivos, en el primer caso se interpreta

como que el modelo subestima el valor de las variables modeladas y viceversa. La fórmula para el

cálculo del sesgo es la siguiente:

∑ [( )]

Dónde:

`o` BIAS: Sesgo (unidad de la variable evaluada);

`o` N: Tamaño de la Muestra;

`o` M: Valor Modelado, y;

`o` O: Valor Observado.

**b.** **Índice de Ajuste (IOA)**

Aporta información sobre el comportamiento del modelo al comparar estadísticamente los valores

observados, con los valores modelados. Este corresponde a un estadístico robusto, ya que integra

los errores cuadráticos medios y absolutos:

∑ ( )

∑ (| | | |)

Dónde:

`o` IOA: Índice de ajuste (adimensional);

`o` N: Número de datos;

`o` Mi: Valor modelado;

`o` Oi: Valor observado, y;

**REVISIÓN [0]** **24**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

`o` Omean: Valor observado promedio.

_**c.**_ _**Error bruto medio (MGE)**_

El error bruto medio proporciona una buena estimación del error medio, independientemente de

si es una sobrestimación o una subestimación de los datos modelados frente a los datos

observados. El error bruto medio está en las mismas unidades que las cantidades consideradas:

[ ∑| |]

Dónde:

`o` MGE: Error bruto medio;

`o` N: Tamaño de la Muestra;

`o` M: Valor Modelado, y;

`o` O: Valor Observado.

_**d.**_ _**Coeficiente de Correlación (r)**_

A partir de este coeficiente se mide la relación lineal entre la variable modelada y la variable

observada. El resultado de este coeficiente se encuentra en el intervalo [-1, 1]. El resultado ideal

es 1, considerando este como la mejor capacidad del modelo para representar las condiciones

generadas. La fórmula para el cálculo del error cuadrático medio es la siguiente:

[ ∑( )] ̅̅̅̅( ̅̅̅)

Dónde:

`o` r: Coeficiente de Correlación;

`o` N: Tamaño de la Muestra;

`o` M: Valor Modelado;

`o` O: Valor Observado, y;

`o` σ: Desviación Estándar.

**e.** **Error Cuadrático Medio**

Este valor entre la diferencia promedio entre los valores promedios modelados y observados. La

fórmula para el cálculo del error cuadrático medio es la siguiente:

∑ [(] [)]
~~√~~

Dónde:

`o` RMSE: Error Cuadrático Medio;

`o` N: Tamaño de la Muestra;

`o` M: Valor Modelado;

**REVISIÓN [0]** **25**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

`o` O: Valor Observado.

Estos parámetros estadísticos son comparados con algunos rangos de aceptabilidad establecidos

referencialmente por la EPA. Al respecto, cabe destacar que, técnicamente no existen criterios

desempeño o rangos de aceptabilidad de las variables estadísticas para el análisis de

incertidumbre de los modelos meteorológicos de pronóstico, pero la EPA, en sus estudios, ha

intentado formular un conjunto de puntos de referencia de evaluación de modelos de mesoescala
basados en la literatura de evaluación de desempeño de MM5 [1] . En el documento (nota al pie)

establece que el propósito de estos puntos de referencia (o rangos de aceptabilidad) no es asignar

una calificación de aprobado o reprobado a una aplicación de modelo meteorológico en particular,

sino más bien poner sus resultados en un contexto útil. Por lo tanto, la idoneidad y adecuación de

los puntos de referencia deben considerarse cuidadosamente en función de los resultados de la

aplicación específica del modelo meteorológico que se esté examinando.

Los puntos de referencia o rangos de aceptabilidad, de cada uno de los estadígrafos considerados,

para el análisis de las variables meteorológicas modeladas frente a las observadas corresponden a

las siguientes:

**Tabla 4-4: Referencias de aceptabilidad para los estadígrafos de cada una de variables meteorológicas.**

|Estación|BIAS|IOA|MGE|RMSE|r|
|---|---|---|---|---|---|
|Velocidad del Viento|≤ ±0,5 *m/s+|≥ 0,60|-|≤ 2 *m/s+|1|
|Dirección del Viento|≤ ±10 *°+|≥ 0,60|≤ 30 *°+|-|1|
|Temperatura|≤ ±0,5 *°+|≥ 0,80|≤ 2 *°+|-|1|

Fuente: Elaboración propia (en basa a documento nota al pie).

Tal como se dijo anteriormente, la metodología denominada “Análisis de Incertidumbre” tiene por

objeto detectar las diferencias entre los valores observados y los modelados. En general en la

variable que se presentan mayores variaciones corresponde a la variable de dirección del viento,

por lo cual, en caso de ser necesario, se establecer un factor de corrección (FC) para las

direcciones del viento que pueden ser subestimadas por el modelo WRF y que, por lo tanto,

llevarían a subestimar las concentraciones ambientales en un determinado receptor.

El factor de corrección para variable dirección del viento, se determina calculando la frecuencia

relativa del viento para cada una de las direcciones respecto de la frecuencia total de las estas,

tanto para los datos observados como para los datos modelados. Por lo tanto, si denominamos X i

a las frecuencias observadas de cada una de las direcciones de viento (i) y W i a las frecuencias

modeladas, entonces matemáticamente las frecuencias relativas observadas (F obs ) corresponderán

a las calculadas de acuerdo con la ecuación 1:

( )
∑

Ecuación 1

1 Operational Evaluation Of The MM5 Meteorological Model Over The Continental United States. Prepared for: Mr. Pat

Dolwick, Office of Air Quality Planning and Standards, U.S. Environmental Protection Agency.

**REVISIÓN [0]** **26**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

Y las frecuencias relativas modeladas (F WRF ), corresponderán a las calculadas de acuerdo con la

ecuación 2:

( )
∑

Ecuación 2

De esta manera, al restar ambas frecuencias relativas obtenemos información respecto al grado de

subestimación o sobrestimación de las direcciones de viento que pueden favorecer el transporte

de los parámetros atmosféricos a modelar. En el caso de que la diferencia entre lo observado y lo

modelado sea mayor que cero, significaría que el modelo subestimó la dirección que favorece el

transporte de contaminantes, y por lo tanto se aplicará un factor de corrección dado por la

ecuación 3 a continuación:

[( ) ( ) ]

Ecuación 3

_**4.2.2.2**_ _**Análisis de incertidumbre del modelo WRF del área de estudio**_

En base a lo presentado en el apartado anterior, en la Tabla 4-5 se presentan los resultados de los

parámetros estadísticos utilizados para comparar los datos modelados con los datos observados

del modelo WRF para el área de estudio, para las variables de viento y temperatura en la estación

analizada. En ella se destaca con color verde las parámetros estadísticos que se cumplen a

cabalidad los parámetros estadísticos y se dejan con rojo los parámetros estadísticos que superan

las referencia de aceptabilidad óptima, independiente de su magnitud de superación:

**Tabla 4-5: Análisis cuantitativo del modelo.**

|Estación|Variable|BIAS|IOA|MGE|RMSE|r|
|---|---|---|---|---|---|---|
|Alto Hospicio|Velocidad del viento|-0,3|0,7|0,8|1,0|0,8|
|Alto Hospicio|Dirección del viento|-11,9|0,5|79,6|120,3|0,2|
|Alto Hospicio|Temperatura|2,3|0,6|2,4|2,9|0,9|
|Pozo Almonte|Velocidad del viento|0,0|0,8|0,9|1,2|0,9|
|Pozo Almonte|Dirección del viento|2,2|0,5|65,5|104,4|0,3|
|Pozo Almonte|Temperatura|1,1|0,7|2,3|2,7|1,0|
|Soledad|Velocidad del viento|-0,2|0,7|0,9|1,3|0,8|
|Soledad|Dirección del viento|9,1|0,4|93,9|132,6|0,2|
|Soledad|Temperatura|0,8|0,7|3,2|3,7|1,0|

Fuente: MYMA, 2021.

En base a estos parámetros obtenidos, es posible indicar que el modelo se adapta de mejor

manera para las variables velocidad del viento y temperatura, pero presenta una mayor impresión

en la componente meteorológica dirección del viento, por lo que se propone establecer un factor

de corrección que permita suplir esta diferencia.

Para la estación meteorológica considerada se graficaron las frecuencias relativas de las

direcciones del viento que favorecen el transporte de los parámetros atmosféricos a modelar,

hacia cada receptor, a modo de determinar los parámetros Frecuencia modelada (F WRF ) y

**REVISIÓN [0]** **27**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

Frecuencia observada (F obs ). El gráfico de las frecuencias relativas señaladas se realizó tanto para

los datos registrados en la estación monitoreara, como para los datos modelados con WRF.

|Col1|Figura 4-6: Comparación frecuencias por dirección del viento.|
|---|---|
|**Pozo Almonte**||
|**Soledad**||
|**Alto Hospicio**||

Fuente: MYMA, 2021.

Como se puede observar en la Figura anterior, si bien el modelo WRF presenta una tendencia

bastante similar a tendencia de la data observada, se subestima el tiempo en el que el viento

apunta a ciertas direcciones, dependiendo de la estación meteorológica.

**REVISIÓN [0]** **28**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

Por lo tanto, considerando el escenario más desfavorable de subestimación, se consideró una

corrección de la peor situación, lo que significa corregir las concentraciones determinadas para los

receptores cercanos con un factor de corrección que aumente las concentraciones, de acuerdo

con la fórmula señalada en el acápite anterior, que se presenta para cada una de la estaciones en

la siguiente tabla:

**Figura 4-7: Factor de corrección para cada estación en estudio.**

|Estación|Factores de corrección|
|---|---|
|Alto Hospicio|1,06|
|Pozo Almonte|1,09|
|Soledad|1,05|

Fuente: MYMA, 2021

**REVISIÓN [0]** **29**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

### 5 DATOS DE ENTRADA DE MODELO

A continuación, se presentan los datos de entrada utilizados para la modelación de la dispersión

de contaminantes, correspondientes a fuentes de emisión y receptores de interés.

**5.1** **Fuentes de Emisión**

Las fuentes de emisión del Proyecto corresponderán principalmente a fuentes del tipo Areal lineal,

Areal y Puntual, y se encuentran asociadas a la fuentes consideradas en el inventario de

emisiones.

Dada la magnitud de emisiones, es que el escenario de modelación corresponde a la Fase de

Construcción (que se ejecuta en 1 año), cuyas tasas de emisión, descripción, coordenadas en el

modelo, base de elevación, largo o área, son presentadas en las siguientes tablas.

Las tasas de emisión fueron estimadas de acuerdo con el inventario de emisiones y determinadas

para la modelación siguiendo la siguiente fórmula:

[ ]

[ ] [ ]

La temporalidad considerada corresponde al año calendario completo, con el objeto de evaluar la

peor condición. A continuación, se presentan las emisiones consideradas por área modelada y

posteriormente se presenta la distribución fuentes en el territorio.

**Tabla 5-1: Escenario de emisiones - Fase de Construcción.**

|Sector|Emisiones [t/año]|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Área modelo|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Sector**|**MPS**|**MP10**|**MP25 **|**NOX **|**SO2 **|**CO**|**HC/COV**|**NH3 **|**Largo**|**Ancho**|**Área**|
|**PFV**|2,91|0,69|0,30|<0,01|<0,01|<0,01|<0,01|<0,01|--|--|66.153|
|**Línea de evacuación**|17,13|4,72|2,15|8,46|0,33|2,95|0,34|<0,01|1.771|1|1.771|
|**Rutas Pavimentadas**|154,34|47,25|4,73|0,24|<0,01|0,01|<0,01|<0,01|72.279|5|361.394|
|**Rutas No Pavimentadas**|6,99|1,34|0,33|0,48|<0,01|0,02|<0,01|<0,01|21.632|5|108.160|
|**Total**|**181,37**|**54,00**|**7,50**|**9,18**|**0,33**|**2,97**|**0,34**|**<0,01**|--|--|--|

Fuente: MYMA, 2021.

**REVISIÓN [0]** **30**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

**Figura 5-1: Fuente de emisiones en el modelo - Fase de Construcción.**

Fuente: MYMA, 2021.

**REVISIÓN [0]** **31**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

**5.2** **Receptores de interés**

La ubicación, descripción e ID de los receptores discretos a considerar se presenta a continuación

en la siguiente tabla.

**Tabla 5-2: Receptores de Interés.**

|Tipo|ID|Coordenada LCC [m]|Col4|Altitud [msnm]|Altura [m]|Descripción|
|---|---|---|---|---|---|---|
|**Tipo**|**ID**|**X **|**Y **|**Y **|**Y **|**Y **|
|Est.<br>Calidad<br>del aire|R_1|-1.868,69|-7.711,87|1.141,55|1,5|Estación Pozo Almonte|
|Est.<br>Calidad<br>del aire|R_2|7.472,32|-28.639,61|1.035,94|1,5|Estación Soledad|
|Est.<br>Calidad<br>del aire|R_3|-34.434,83|-12.207,89|1.141,57|1,5|Estación Alto Hospicio|

Fuente: MYMA, 2021.

**REVISIÓN [0]** **32**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

**Figura 5-2: Ubicación receptores discretos.**

Fuente: MYMA, 2021.

**REVISIÓN [0]** **33**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

### 6 RESULTADOS DE LA MODELACIÓN ATMOSFÉRICA

Los resultados se presentan en isocurvas, para cada uno de los estadísticos considerados en las

normativas de calidad del aire aplicables al presente estudio. Posteriormente se presentan los

Puntos de Máxima Concentración y finalmente se presenta un análisis respecto a la concentración

esperada en los receptores sensibles dada la implementación del Proyecto.

**6.1** **Isocurvas**

En las siguientes figuras, se muestran las distintas curvas de isoconcentración, isodepositación

obtenidos como resultado del modelo de dispersión CALPUFF-WRF para Material Particulado

Respirable (MP 10 ), Material Particulado Fino Respirable (MP 2,5 ), Material Particulado Sedimentado

(MPS), Dióxido de Azufre (SO 2 ), Monóxido de Carbono (CO) y Dióxido de Nitrógeno (NO 2 ). Cabe

mencionar que estos resultados fueron adjuntados en el Apéndice 1 Archivos Digitales, para la

etapa de construcción.

**REVISIÓN [0]** **34**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

**Figura 6-1: Curva isoconcentración - Fase de Construcción- MP** **10** **- Norma anual.**

Fuente: MYMA, 2021.

**REVISIÓN [0]** **35**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

**Figura 6-2: Curva isoconcentración - Fase de Construcción - MP** **10** **- Norma diaria (P98).**

Fuente: MYMA, 2021.

**REVISIÓN [0]** **36**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

**Figura 6-3: Curva isoconcentración - Fase de Construcción - MP** **2,5** **- Norma anual.**

Fuente: MYMA, 2021.

**REVISIÓN [0]** **37**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

**Figura 6-4: Curva isoconcentración - Fase de Construcción- MP** **2,5** **- Norma diaria (P98).**

Fuente: MYMA, 2021.

**REVISIÓN [0]** **38**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

**Figura 6-5: Curva isodepositación - Fase de Construcción - MPS - Norma mensual.**

Fuente: MYMA, 2021.

**REVISIÓN [0]** **39**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

**Figura 6-6: Curva isodepositación - Fase de Construcción - MPS - Norma Anual.**

Fuente: MYMA, 2021.

**REVISIÓN [0]** **40**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

**Figura 6-7: Curva isoconcentración - Fase de Construcción - SO** **2** **- Norma primaria anual.**

Fuente: MYMA, 2021.

**REVISIÓN [0]** **41**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

**Figura 6-8: Curva isoconcentración - Fase de Construcción - SO** **2** **- Norma primaria diaria (P99).**

Fuente: MYMA, 2021.

**REVISIÓN [0]** **42**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

**Figura 6-9: Curva isoconcentración - Fase de Construcción - SO** **2** **- Norma primaria horaria (P98,5).**

Fuente: MYMA, 2021.

**REVISIÓN [0]** **43**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

**Figura 6-10: Curva isoconcentración - Fase de Construcción - SO** **2** **- Norma secundaria diaria (P99,7).**

Fuente: MYMA, 2021.

**REVISIÓN [0]** **44**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

**Figura 6-11: Curva isoconcentración - Fase de Construcción - SO** **2** **- Norma secundaria horaria (P99,73).**

Fuente: MYMA, 2021.

**REVISIÓN [0]** **45**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

**Figura 6-12: Curva isoconcentración - Fase de Construcción - NO** **2** **- Norma anual.**

Fuente: MYMA, 2021.

**REVISIÓN [0]** **46**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

**Figura 6-13: Curva isoconcentración - Fase de Construcción - NO** **2** **- Norma horaria (P99).**

Fuente: MYMA, 2021.

**REVISIÓN [0]** **47**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

**Figura 6-14: Curva isoconcentración - Fase de Construcción - CO - horaria (P99).**

Fuente: MYMA, 2021.

**REVISIÓN [0]** **48**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

**Figura 6-15: Curva isoconcentración - Fase de Construcción - CO - 8 horas (P99).**

Fuente: MYMA, 2021.

**REVISIÓN [0]** **49**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

**6.2** **Puntos de máxima concentración (PMC)**

A continuación, se detallan los Puntos de Máxima Concentración (PMC) con el factor de corrección

del escenario modelado, detallando el contaminante y su aporte, por estadístico. Además, se

muestra las coordenadas de cada PMC.

**Tabla 6-1: Puntos de Máxima Concentración (PMC).**

|Parámetro|Estadístico|PMC|Norma|% Norma|Coordenadas UTM - WGS84|Col7|
|---|---|---|---|---|---|---|
|**Parámetro**|**Estadístico**|**PMC**|**Norma**|**% Norma**|**Este (m)**|**Norte (m)**|
|MPS [mg/m2-<br>día]|Promedio del Periodo|25,48|100|25,48%|417.658|7.743.407|
|MPS [mg/m2-<br>día]|Promedio mensual|33,92|200|16,96%|16,96%|16,96%|
|MP10<br>[ug/m3]|Promedio del Periodo|23,24|50|46,47%|46,47%|46,47%|
|MP10<br>[ug/m3]|Percentil 98 Diario|59,43|150|39,62%|39,62%|39,62%|
|MP2,5<br>[ug/m3]|Promedio del Periodo|4,51|20|22,56%|409.642|7.744.365|
|MP2,5<br>[ug/m3]|Percentil 98 Diario|9,35|50|18,70%|18,70%|18,70%|
|SO2 <br>[ug/m3]|Promedio del Periodo|0,43|60|0,72%|0,72%|0,72%|
|SO2 <br>[ug/m3]|Percentil 99 Diario|0,98|150|0,65%|0,65%|0,65%|
|SO2 <br>[ug/m3]|Percentil 98,5 Horario|3,85|350|1,10%|1,10%|1,10%|
|SO2 <br>[ug/m3]|Promedio del Periodo|0,43|80|0,54%|0,54%|0,54%|
|SO2 <br>[ug/m3]|Percentil 99,7 Diario|1,02|365|0,28%|0,28%|0,28%|
|SO2 <br>[ug/m3]|Percentil 99,73 Horario|4,57|1000|0,46%|0,46%|0,46%|
|NO2 <br>[ug/m3]|Promedio del Periodo|10,90|100|10,90%|10,90%|10,90%|
|NO2 <br>[ug/m3]|Percentil 99 Horario|125,19|400|31,30%|31,30%|31,30%|
|CO[ug/m3]|Percentil 99 8 Horas|21,70|10000|0,22%|0,22%|0,22%|
|CO[ug/m3]|Percentil 99 Horario|48,89|30000|0,16%|0,16%|0,16%|

Fuente: MYMA, 2021.

En la siguiente cartografía se presenta la localización de los PMC, en donde se puede ver que estos

se concentran en el área de intervención del proyecto y en el camino de acceso a la faena.

**REVISIÓN [0]** **50**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

**Figura 6-16: Localización de Puntos de Máxima Concentración.**

Fuente: MYMA, 2021.

**6.3** **Aportes en receptores sensibles**

Se presentan los resultados obtenidos de la modelación y los resultados ponderados por el factor

de corrección determinado en el análisis de incertidumbre (sección 4.2.2.2) para el escenario

modelado.

**6.3.1** **Aportes fase del Proyecto**

En la Tabla 6-2 se presentan resultados obtenidos de la modelación y En la Tabla 6-3 los resultados

ponderados por el factor de corrección determinado en el análisis de incertidumbre

**REVISIÓN [0]** **51**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

**Tabla 6-2: Aporte del Proyecto - Fase de Construcción - Sin Corrección.**

|Receptore<br>s de<br>Interés|MPS mg/m2d|Col3|MP ug/m3<br>10|Col5|MP ug/m3<br>2.5|Col7|SO ug/m3<br>2|Col9|Col10|Col11|Col12|Col13|NO ug/m3<br>2|Col15|CO|Col17|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptore**<br>**s de**<br>**Interés**|Primaria|Primaria|Primaria|Primaria|Primaria|Primaria|Primaria|Primaria|Primaria|Secundaria|Secundaria|Secundaria|Primaria|Primaria|Primaria|Primaria|
|**Receptore**<br>**s de**<br>**Interés**|Media<br>Anual|Media<br>Mensual|Media<br>Anual|P98<br>Diario|Media<br>Anual|P98 Diario|Media<br>Anual|P99<br>Diario|P98.5<br>Horario|Media<br>Anual|P99.7<br>Diario|P99.73<br>Horario|Media<br>Anual|P99<br>Horario|P99 8<br>hrs.|P99<br>Horario|
|R_1|0,0351|0,0404|0,0321|0,0586|0,0071|0,0130|0,0001|0,0001|0,0003|0,0001|0,0001|0,0004|0,0083|0,0960|0,003|0,0074|
|R_2|0,0322|0,0455|0,1679|0,5116|0,0176|0,0526|0,0001|0,0001|0,0002|0,0001|0,0001|0,0003|0,0015|0,0145|0,002|0,0040|
|R_3|0,0108|0,0139|0,0099|0,0241|0,0022|0,0050|<0,0001|0,0001|0,0002|<0,0001|0,0001|0,0003|0,0024|0,0585|0,001|0,0038|

Fuente: MYMA, 2021.

**Tabla 6-3: Aporte del Proyecto - Fase de Construcción - Con Corrección.**

|Receptore<br>s de<br>Interés|MPS mg/m2d|Col3|MP ug/m3<br>10|Col5|MP ug/m3<br>2.5|Col7|SO ug/m3<br>2|Col9|Col10|Col11|Col12|Col13|NO ug/m3<br>2|Col15|CO|Col17|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptore**<br>**s de**<br>**Interés**|Primaria|Primaria|Primaria|Primaria|Primaria|Primaria|Primaria|Primaria|Primaria|Secundaria|Secundaria|Secundaria|Primaria|Primaria|Primaria|Primaria|
|**Receptore**<br>**s de**<br>**Interés**|Media<br>Anual|Media<br>Mensual|Media<br>Anual|P98<br>Diario|Media<br>Anual|P98 Diario|Media<br>Anual|P99<br>Diario|P98.5<br>Horario|Media<br>Anual|P99.7<br>Diario|P99.73<br>Horario|Media<br>Anual|P99<br>Horario|P99 8<br>hrs.|P99<br>Horario|
|R_1|0,0383|0,0440|0,0350|0,0639|0,0077|0,0142|0,0001|0,0001|0,0003|0,0001|0,0002|0,0004|0,0091|0,1047|0,003|0,0081|
|R_2|0,0338|0,0478|0,1763|0,5372|0,0185|0,0553|0,0001|0,0001|0,0003|0,0001|0,0001|0,0003|0,0016|0,0152|0,002|0,0042|
|R_3|0,0115|0,0148|0,0105|0,0255|0,0023|0,0053|<0,0001|0,0001|0,0002|<0,0001|0,0001|0,0003|0,0026|0,0620|0,001|0,0041|

Fuente: MYMA, 2021.

**REVISIÓN [0]** **52**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

**6.4** **Calidad del Aire Observada**

En el Anexo 3.1 Línea de Base Calidad del Aire se caracterizó la calidad del aire del sector en

estudio. A modo de resumen es posible indicar que: En el área de estudio existen 3 estaciones,

estas corresponden a Pozo Almonte, Soledad y Alto Hospicio, registrando los contaminantes MP 10,

MP 2,5 y SO 2 según corresponda. Los registros en general cubren el periodo entre el 2018 y el 2020,

lo que permite caracterizar la situación actual de la calidad del aire.

De acuerdo con los valores obtenidos para la línea de base de calidad de aire, todos los

contaminantes considerados, en todos sus estadísticos, se encuentran por debajo del valor

máximo normado, tanto para la normativa primaria de calidad del aire, como para la normativa

secundaria, en las distintas estaciones.

Todos los valores se encuentran cercanos o bajo el 50% del valor normado, con excepción del

MP 10, registrado en la estación de calidad del aire Pozo Almonte, el estadístico anual (Promedio

Anual), registrada se encuentra bajo el 68% de la normativa primaria de calidad del aire. En la

siguiente tabla se presenta el resumen correspondiente a la Línea de Base del área de estudio

**Tabla 6-4: Línea de Base Proyectada del Área de Estudio.**

|Estación|Norma|Parámetro|Estadístico|2018|2019|2020|Promedio<br>trianual|Norma|% de la<br>norma|
|---|---|---|---|---|---|---|---|---|---|
|Pozo<br>Almonte|Primaria|MP10|Promedio Anual|34,5|36,4|31,3|34,1|50|68%|
|Pozo<br>Almonte|Primaria|MP10|Percentil 98|66,0|68,0|62,9|65,6|150|44%|
|Pozo<br>Almonte|Primaria|MP2,5|Promedio Anual|8,7|8,0|10,7|9,1|20|46%|
|Pozo<br>Almonte|Primaria|MP2,5|Percentil 98|7,0|17,0|28,8|17,6|50|35%|
|Pozo<br>Almonte|Primaria|SO2|Promedio Anual|1,6|1,7|4,6|2,6|60|4%|
|Pozo<br>Almonte|Primaria|SO2|Percentil 99 - Diario|3,8|4,3|9,3|5,8|150|4%|
|Pozo<br>Almonte|Primaria|SO2|Percentil 98,5 -<br>Horario|5,3|6,2|12,8|8,1|350|2%|
|Pozo<br>Almonte|Secundaria|SO2|Promedio Anual|1,6|1,7|4,6|2,6|80|3%|
|Pozo<br>Almonte|Secundaria|SO2|Percentil 99,7 - Diario|4,0|4,6|13,7|7,4|365|2%|
|Pozo<br>Almonte|Secundaria|SO2|Percentil 99,73 -<br>Horario|7,9|11,5|27,5|15,6|1000|2%|
|Soledad|Primaria|SO2|Promedio Anual|4,6|3,4|4,8|4,3|60|7%|
|Soledad|Primaria|SO2|Percentil 99 - Diario|26,3|6,5|7,4|13,4|150|9%|
|Soledad|Primaria|SO2|Percentil 98,5 -<br>Horario|26,8|8,9|11,2|15,6|350|4%|
|Soledad|Secundaria|SO2|Promedio Anual|4,6|3,4|4,8|4,3|80|5%|
|Soledad|Secundaria|SO2|Percentil 99,7 - Diario|26,8|22,1|8,1|19,0|365|5%|
|Soledad|Secundaria|SO2|Percentil 99,73 -<br>Horario|42,0|20,1|19,6|27,2|1000|3%|
|Alto<br>Hospicio|Primaria|MP2,5|Promedio Anual|11,2|11,1|10,3|10,9|20|54%|
|Alto<br>Hospicio|Primaria|MP2,5|Percentil 98|21,6|19,0|18,7|19,8|50|40%|

Fuente: MYMA, 2021.

**REVISIÓN [0]** **53**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

**6.5** **Aportes en receptores sensibles**

De acuerdo con lo presentado anteriormente, considerando los resultados de la modelación corregidos con el factor estimado, se presenta

el análisis normativo en los receptores de interés para el escenario de modelación Construcción. En ellos se observa que los valores

obtenidos son porcentualmente bajos respecto de la normativa para todos los receptores considerados.

**Tabla 6-5: Análisis de cumplimiento de Normativa Vigente.**

|Receptor de<br>Interés|MPS<br>mg/m2d|Col3|MP<br>10<br>μg/m3|Col5|MP<br>2.5<br>μg/m3|Col7|SO<br>2<br>μg/m3|Col9|Col10|Col11|Col12|Col13|NO<br>2<br>μg/m3|Col15|CO<br>μg/m3|Col17|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor de**<br>**Interés**|**Secundaria**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|**Secundaria**|**Secundaria**|**Secundaria**|**Primaria**|**Primaria**|**Primaria**|**Primaria**|
|**Receptor de**<br>**Interés**|**Media**<br>**Anual**|**Media**<br>**Mensual**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P98**<br>**Diario**|**Media**<br>**Anual**|**P99**<br>**Diario**|**P98,5**<br>**Hr**|**Media**<br>**Anual**|**P99.7**<br>**Diario**|**P99,73**<br>**Hr**|**Media**<br>**Anual**|**P99H**|**P99**<br>**8 hrs.**|**P99**<br>**Hr**|
|**Norma**|**100**|**200**|**50**|**150**|**20**|**50**|**60**|**150**|**350**|**80**|**365**|**1.000**|**100**|**400**|**10.000**|**30.000**|
|R1|0,04%|0,02%|0,07%|0,04%|0,04%|0,03%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,01%|0,03%|<0,01%|<0,01%|
|R2|0,03%|0,02%|0,35%|0,36%|0,09%|0,11%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,00%|<0,01%|<0,01%|
|R3|0,01%|0,01%|0,02%|0,02%|0,01%|0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|<0,01%|0,02%|<0,01%|<0,01%|

Fuente: MYMA, 2021.

**REVISIÓN [0]** **54**

**Anexo 2-3: Modelación de Dispersión de**

**Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

De acuerdo con lo presentado anteriormente, considerando los resultados de la modelación

corregidos con el factor estimado y línea base, se presenta el análisis normativo en las estaciones

de monitoreo calidad del aire para el escenario de modelación.

**Tabla 6-6: Análisis de cumplimiento de Normativa Vigente.**

|ID|Estación|Contaminante|Estadístico|Norma|LB|AP|LB+AP|% Norma|
|---|---|---|---|---|---|---|---|---|
|**ID**|**Estación**|**Contaminante**|**Estadístico**|**Norma**|**ug/m3**|**ug/m3**|**ug/m3**|**ug/m3**|
|R_1|Pozo Almonte|MP10|Promedio Anual|50|34,1|0,0350|34,1440|68%|
|R_1|Pozo Almonte|MP10|Percentil 98|150|65,6|0,0639|65,6936|44%|
|R_1|Pozo Almonte|MP2,5|Promedio Anual|20|9,1|0,0077|9,1519|46%|
|R_1|Pozo Almonte|MP2,5|Percentil 98|50|17,6|0,0142|17,6281|35%|
|R_1|Pozo Almonte|SO2|Promedio Anual|60|2,6|0,0001|2,6468|4%|
|R_1|Pozo Almonte|SO2|Percentil 99 - Diario|150|5,8|0,0001|5,8098|4%|
|R_1|Pozo Almonte|SO2|Percentil 98,5 - Horario|350|8,1|0,0003|8,0869|2%|
|R_1|Pozo Almonte|SO2|Promedio Anual|80|2,6|0,0001|2,6468|3%|
|R_1|Pozo Almonte|SO2|Percentil 99,7 - Diario|365|7,4|0,0002|7,4318|2%|
|R_1|Pozo Almonte|SO2|Percentil 99,73 - Horario|1000|15,6|0,0004|15,6371|2%|
|R_2|Soledad|SO2|Promedio Anual|60|4,3|0,0001|4,2825|7%|
|R_2|Soledad|SO2|Percentil 99 - Diario|150|13,4|0,0001|13,4065|9%|
|R_2|Soledad|SO2|Percentil 98,5 - Horario|350|15,6|0,0003|15,6436|4%|
|R_2|Soledad|SO2|Promedio Anual|80|4,3|0,0001|4,2825|5%|
|R_2|Soledad|SO2|Percentil 99,7 - Diario|365|19,0|0,0001|18,9864|5%|
|R_2|Soledad|SO2|Percentil 99,73 - Horario|1000|27,2|0,0003|27,2403|3%|
|R_3|Alto Hospicio|MP2,5|Promedio Anual|20|10,9|0,0023|10,8614|54%|
|R_3|Alto Hospicio|MP2,5|Percentil 98|50|19,8|0,0053|19,7837|40%|

Fuente: MYMA, 2021

**REVISIÓN [0]** **55**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

### 7 ANÁLISIS DE RESULTADOS Y CONCLUSIONES

Según lo expuesto en el documento, se concluye que:

**Respecto a la descripción y justificación del modelo utilizado y los contaminantes modelados:**

El sistema de modelación utilizado corresponde al denominado “WRF-CALPUFF”, que

considera un modelo tipo “puff” Lagrangiano Gaussiano no estacionario y un modelo

meteorológico de predicción numérica a mesoescala no hidrostático. Este modelo sirve

para representar la dispersión de contaminantes en dominios de modelación cuyas

fuentes de emisión se ubican a más de 5 km de los receptores sensibles a analizar.

En base a las características intrínsecas del Proyecto, y a lo justificado en apartados

anterior, los contaminantes modelados corresponden a MPS, MP 10, MP 2,5 NO 2, SO 2 y CO.

**Línea de base de calidad del aire**

En el Anexo 3.1 Línea de Base Calidad del Aire se caracterizó la calidad del aire del sector

en estudio. A modo de resumen es posible indicar que: En el área de estudio existen 3

estaciones, estas corresponden a Pozo Almonte, Soledad y Alto Hospicio, registrando los

contaminantes MP 10, MP 2,5 y SO 2 según corresponda. Los registros en general cubren el

periodo entre el 2018 y el 2020, lo que permite caracterizar la situación actual de la

calidad del aire.

De acuerdo con los valores obtenidos para la línea de base de calidad de aire, todos los

contaminantes considerados, en todos sus estadísticos considerados, se encuentran por

debajo del valor máximo normado, tanto para la normativa primaria de calidad del aire,

como para la normativa secundaria, en las distintas estaciones. Además todos los valores

se encuentran cercanos o bajo el 50% del valor normado, con excepción del MP 10,

registrado en la estación de calidad del aire Pozo Almonte, el estadístico anual (Promedio

Anual), registrada se encuentra bajo el 68% de la normativa primaria de calidad del aire.

**Aportes del Proyecto:**

En relación con los resultados de la modelación, los aportes del proyecto en los puntos de

interés son los siguientes:

 - El aporte del proyecto en los puntos de interés tanto para el material particulado

MP 10, MP 2,5 y MPS como en los gases SO 2, NOx y CO resultan ser menores al 0,07% de

la norma para todos los estadísticos.

**REVISIÓN [0]** **56**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

Por otra parte, al comparar los valores de Línea de Base de Calidad del Aire (LBCA), con los

valores de LBCA más los aportes del Proyecto, es posible observar que:

 - No se supera los valores máximos de concentración de la normativa de calidad del aire

en ninguna estación de monitoreo en estudio. Todos los valores se encuentran

cercanos o bajo el 50 % del valor normado, con excepción del MP 10, registrado en la

estación de calidad del aire Pozo Almonte, el estadístico anual (Promedio Anual),

registrada se encuentra bajo el 68% de la normativa primaria de calidad del aire. Cabe

destacar que el mayor aporte proviene de la línea base, el proyecto contribuye con

menos del 0,13% del total de concentraciones en todos los estadísticos.

 - Respecto a los puntos de máxima concentración, se observa que, para todos los

contaminantes, estos se encuentran concentrados en las inmediaciones del proyecto,

por lo tanto, no ubicándose en sectores poblacionales, ni sobre receptores de flora y

fauna sensible o protegida.

 - Las isoconcentraciones obtenidas muestran que los contaminantes tienen una

dispersión local, ubicándose preferentemente sobre el proyecto y en los sitios

aledaños a camino de acceso.

En base a lo anterior, es posible indicar que el Proyecto no genera una alteración negativa

significativa de la condición basal de la calidad del aire.

**REVISIÓN [0]** **57**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

### APÉNDICE 2.2-1

## ARCHIVOS DIGITALES DE MODELACIÓN

### Proyecto “Parque Fotovoltaico Soledad” [REVISIÓN 0]

**REVISIÓN [0]** **58**

**Anexo 2-3: Modelación de Dispersión de Contaminantes**

**“Parque Solar Fotovoltaico Soledad”**

SCM COSAYACH Yodo

Los archivos digitales del presente Anexo fueron presentados en el Apéndice 2.2-1 del Anexo 2.2

del DIA.

Cabe mencionar que, de acuerdo a lo señalado en los artículos 31 y 32 (del Artículo Segundo) de la

Ley N° 20.417 que “Crea el Ministerio, el Servicio de Evaluación Ambiental y la Superintendencia

del Medio Ambiente” emanada por el Ministerio Secretaria General de la Presidencia; se informa

que dada la naturaleza de los documentos los archivos Digitales de Modelación de Dispersión

Atmosférica CALPUFF, no es posible agregarlos directamente al expediente electrónico, motivo

por el cual dicha información se encuentra disponible para el público en general en las oficinas del

Servicio de Evaluación Ambiental (SEA) de la Región Metropolitana. Los interesados en obtener

dicha documentación deben comunicarse con Oficina de Información y Atención Ciudadana del

SEA Regional, ingresando su requerimiento a través del siguiente formulario:

[http://www.portaltransparencia.cl/PortalPdT/web/guest](http://www.portaltransparencia.cl/PortalPdT/web/guest)

**REVISIÓN [0]** **59**