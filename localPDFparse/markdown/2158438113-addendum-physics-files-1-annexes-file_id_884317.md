---
title: Sin título
author: Soledad Mediavilla
date: D:20230609101817-04'00'
language: es
type: report
pages: 33
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ADENDA DECLARACIÓN DE IMPACTO AMBIENTAL “AMPLIACIÓN EN SE ANA MARÍA Y SECCIONAMIENTO LÍNEA 2X220 kV FRONTERA - MARÍA ELENA” ANEXO 6: Estudio Hidráulico Junio 2023
-->

# ADENDA DECLARACIÓN DE IMPACTO AMBIENTAL “AMPLIACIÓN EN SE ANA MARÍA Y SECCIONAMIENTO LÍNEA 2X220 kV FRONTERA - MARÍA ELENA” ANEXO 6: Estudio Hidráulico Junio 2023

**ÍNDICE**

1. INTRODUCCIÓN ........................................................................................................................... 3

1.1. Descripción general del proyecto........................................................................................ 3

1.2. Objetivo del estudio ............................................................................................................ 4

1.3. Alcance del estudio ............................................................................................................. 4

1.4. Referencias .......................................................................................................................... 4

2. ANTECEDENTES HIDROLÓGICOS ................................................................................................. 5

2.1. Cuenca hidrográfica ............................................................................................................ 5

2.2. Estaciones meteorológicas .................................................................................................. 5

2.3. Cauce natural ...................................................................................................................... 5

3. CÁLCULO HIDROLÓGICO ............................................................................................................. 6

3.1. Análisis de frecuencia .......................................................................................................... 6

3.2. Criterios y metodología utilizada ...................................................................................... 13

4. MODELACIÓN HIDRÁULICA ....................................................................................................... 14

4.1. Representación del cauce ................................................................................................. 14

4.2. Coeficiente de Manning .................................................................................................... 15

4.3. Caudal de simulación ........................................................................................................ 15

5. CONCLUSIONES ......................................................................................................................... 17

6. APÉNDICES ................................................................................................................................ 18

6.1. Perfiles Transversales de modelación ............................................................................... 18

6.2 Barimetría .......................................................................................................................... 29

**Anexo 6 Adenda**
P á g i n a | i
**Estudio Hidráulico**

**ÍNDICE DE FIGURAS**

Figura 1-1: Área de Estudio y Quebrada Rio Seco. ........................................................................ 3

Figura 3-1: Resultado y análisis de datos de frecuencia - distribución Gumbel. ........................ 12

Figura 4-1: Términos utilizados en la ecuación de energía. ........................................................ 14

Figura 4-2: Valores de n-manning sugeridos para cauces naturales. .......................................... 15

Figura 4-3: Zona de modelación. ................................................................................................. 16

Figura 4-4: Resultados de modelación. ....................................................................................... 17

**Anexo 6 Adenda**
P á g i n a | ii
**Estudio Hidráulico**

**1.** **INTRODUCCIÓN**

**1.1.** **Descripción general del proyecto**

La presente sección da cuenta de los antecedentes que caracterizan las condiciones hidráulicas y

el análisis de crecida del estero Rio Seco en la comuna de Ana María, asociado al área del

emplazamiento del proyecto “Ampliación en S/E Ana María y Seccionamiento Línea 2x220kV

Frontera - María Elena”.

Para ello, se realiza un análisis de las condiciones de borde del río en las proximidades del área de

emplazamiento, junto con modelaciones que permiten determinar si existirían posibles

inundaciones que afecten el proyecto, para un período de retorno de 100 años

**Figura 1-1: Área de Estudio y Quebrada Rio Seco.**

Fuente: Elaboración propia.

**Anexo 6 Adenda**
P á g i n a | 3
**Estudio Hidráulico**

**1.2.** **Objetivo del estudio**

El objetivo del presente informe es determinar el comportamiento hidráulico de la quebrada río

Seco, asociada a las obras del proyecto, ante eventos de crecidas causadas por precipitaciones con

un período de retorno de 100 años. Los resultados de este informe permiten definir la necesidad o

no, de proyectar obras hidráulicas de defensas o medidas de mitigación, para asegurar la

integridad del proyecto.

**1.3.** **Alcance del estudio**

En este informe, se realizan las siguientes tareas:

 - Delimitación de la cuenca aportante al proyecto, mediante análisis de cartografía y

topografía disponible.

 - Determinación de los parámetros hidrológicos asociados a la cuenca aportante, realizando

en particular el análisis de frecuencia de precipitaciones máximas en 24 horas disponibles

en la página web de la dirección general de Aguas.

 - Cálculo del caudal máximo de crecida, utilizando los parámetros hidrológicos

determinados previamente.

 - Modelación hidráulica de la quebrada Rio Seco, utilizando el caudal máximo de crecida

calculado previamente.

**1.4.** **Referencias**

Para la elaboración de este informe, se han consultado las siguientes referencias:

 - Ayala Riquelme, L., Cabrera Fajardo, G., González González, D., Isensee Martínez, P., Lagos

Rehfeld, J., & Pérez Soto, F. (1995). Manual de cálculo de crecidas y caudales mínimos en

cuencas sin información fluviométrica. Santiago: Dirección General de aguas, Ministerio de

Obras Públicas.

 - Brunner, G. W. (1995). HEC-RAS River Analysis System. Hydraulic Reference Manual.

Versión 1.0. Hydrologic Engineering Center Davis CA.

 - Dirección General de Aguas. 2021. Información Oficial Hidrometeorológica y de Calidad de

Aguas en Línea. [online] Disponible en: <https://snia.mop.gob.cl/BNAConsultas/reportes>

[Fecha de consulta 21 March 2021].

**Anexo 6 Adenda**
P á g i n a | 4
**Estudio Hidráulico**

**2.** **ANTECEDENTES HIDROLÓGICOS**

**2.1.** **Cuenca hidrográfica**

El área de estudio se ubica, según las cuencas del banco general de aguas, en la “Subcuenca del río

Loa, entre río San Salvador y Quebrada Amarga”, la cual presenta una superficie aproximada de

12.858 km [2] ”.

**2.2.** **Estaciones meteorológicas**

Para poder estimar los caudales de crecida a distintos periodos de retorno que pueden influir en el

proyecto, se requieren datos meteorológicos (precipitaciones máximas anuales en 24 horas), lo

más cercanos posibles al sitio o la zona de estudio. Considerando lo anterior, se utilizan los datos

meteorológicos adquiridos desde la estación fluviométrica “Quillagua”, ubicada a 32 km de la zona

de estudio, y que cuenta con registros históricos desde 1977 hasta la actualidad.

**2.3.** **Cauce natural**

El área de estudio se enmarca en una zona aledaña a la quebrada Rio Seco, ubicada en la comuna

de Santa Ana. La delimitación y el reconocimiento de la red asociada se realiza tanto en terreno

como a través de la utilización de la información cartográfica disponible. Por otro lado, se utiliza

una batimetría realizada a lo largo del cauce del estero, la que, a su vez, se confecciona 500 m

aguas arriba y abajo desde las obras del Proyecto.

**Anexo 6 Adenda**
P á g i n a | 5
**Estudio Hidráulico**

**3.** **CÁLCULO HIDROLÓGICO**

**3.1.** **Análisis de frecuencia**

Como se menciona previamente, la cuenca asociada se analizó mediante datos meteorológicos

históricos obtenidos de la estación “Quillagua” ubicada a 32 km aproximadamente de la zona del

proyecto.

**Tabla 3-1:** **Precipitaciones máximas anuales en 24 horas, estación “Quillagua”.**

<!-- INICIO TABLA 3-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- históricos obtenidos de la estación “Quillagua” ubicada a 32 km aproximadamente de la zona del proyecto. -->

**Tabla 3-1: ** **Precipitaciones máximas anuales en 24 horas, estación “Quillagua”.****

| Fecha | Pp máxima en 24 horas<br>(mm) |
| --- | --- |
| 1970 | 0 |
| 1971 | 0 |
| 1972 | 0 |
| 1973 | 0 |
| 1974 | 0 |
| 1975 | 0 |
| 1978 | 0 |
| 1979 | 0 |
| 1980 | 0 |
| 1981 | 0 |
| 1982 | 0 |
| 1983 | 0 |
| 1984 | 0,4 |
| 1985 | 0 |
| 1986 | 0 |
| 1987 | 0 |
| 1988 | 0 |
| 1989 | 0 |
| 1990 | 0 |
| 1991 | 0 |
| 1992 | 1 |
| 1993 | 0 |
| 1994 | 0 |

<!-- Estadísticas: 23 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- |Fecha|Pp máxima en 24 horas<br>(mm)| |---|---| |1995|0| |1996|0| -->
<!-- FIN TABLA 3-1 -->


**Anexo 6 Adenda**
P á g i n a | 6
**Estudio Hidráulico**

|Fecha|Pp máxima en 24 horas<br>(mm)|
|---|---|
|1970|0|
|1971|0|
|1972|0|
|1973|0|
|1974|0|
|1975|0|
|1978|0|
|1979|0|
|1980|0|
|1981|0|
|1982|0|
|1983|0|
|1984|0,4|
|1985|0|
|1986|0|
|1987|0|
|1988|0|
|1989|0|
|1990|0|
|1991|0|
|1992|1|
|1993|0|
|1994|0|

|Fecha|Pp máxima en 24 horas<br>(mm)|
|---|---|
|1995|0|
|1996|0|
|1997|0|
|1998|0|
|1999|0|
|2000|0|
|2001|3|
|2002|0,2|
|2003|0|
|2004|0|
|2005|0,5|
|2006|0|
|2007|0|
|2008|0|
|2009|0|
|2010|0|
|2011|0|
|2012|0,6|
|2013|0,5|
|2014|0|
|2015|2,4|
|2016|0|
|2017|0|
|2018|1,8|
|2019|5,4|
|2020|0,0|

Fuente _**:**_ DGA.

**Anexo 6 Adenda**
P á g i n a | 7
**Estudio Hidráulico**

**Tabla 3-2:** **Estadígrafos de la muestra de precipitaciones.**

<!-- INICIO TABLA 3-2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **Anexo 6 Adenda** P á g i n a | 7 **Estudio Hidráulico** -->

**Tabla 3-2: ** **Estadígrafos de la muestra de precipitaciones.****

| log (x)= | 0.65 | Prom (log (x))= | -1.46 |
| --- | --- | --- | --- |
| **s (x)= ** | 1.21 | **s (log(x))= ** | 1.28 |
| **Cs= ** | 2.918 | **Cs(log(x))= ** | 1.256 |
| **K= ** | 0.486 | **K(log(x))= ** | 0.209 |

<!-- Estadísticas: 3 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. La serie de precipitaciones fue evaluada para las cinco distribuciones de frecuencia utilizadas en -->
<!-- FIN TABLA 3-2 -->


|log (x)=|0.65|Prom (log (x))=|-1.46|
|---|---|---|---|
|**s (x)= **|1.21|**s (log(x))= **|1.28|
|**Cs= **|2.918|**Cs(log(x))= **|1.256|
|**K= **|0.486|**K(log(x))= **|0.209|

Fuente: Elaboración propia.

La serie de precipitaciones fue evaluada para las cinco distribuciones de frecuencia utilizadas en

hidrología, estas son: Normal, Log Normal, Pearson, Log Pearson y Gumbel.

A los resultados obtenidos por las distintas distribuciones, se le aplicó una prueba de bondad de

ajuste test chi [2], donde se relaciona la dispersión de estos resultados con respecto a su distribución

correspondiente. Los parámetros, aplicación del test y resultados se observan en las siguientes

tablas:

**Tabla 3-3:** **Parámetros de las distribuciones.**

<!-- INICIO TABLA 3-3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- correspondiente. Los parámetros, aplicación del test y resultados se observan en las siguientes tablas: -->

**Tabla 3-3: ** **Parámetros de las distribuciones.****

| Año | Normal | Log-Normal | Pearson | Log-Pearson | Gumbel |
| --- | --- | --- | --- | --- | --- |
| u | 0.65 | -1.46 |  |  |  |
| s | 1.21 | 1.28 |  |  |  |
| a |  |  | 0.5666 | 1.2430 |  |
| b |  |  | 0.4699 | 2.5368 |  |
| c |  |  | -0.1811 | -3.4971 |  |
| yn |  |  |  |  | 0.534 |
| s n |  |  |  |  | 1.098 |

<!-- Estadísticas: 7 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente **:** Elaboración propia. **Anexo 6 Adenda** P á g i n a | 8 -->
<!-- FIN TABLA 3-3 -->


|Año|Normal|Log-Normal|Pearson|Log-Pearson|Gumbel|
|---|---|---|---|---|---|
|u|0.65|-1.46||||
|s|1.21|1.28||||
|a|||0.5666|1.2430||
|b|||0.4699|2.5368||
|c|||-0.1811|-3.4971||
|yn|||||0.534|
|s n|||||1.098|

Fuente **:** Elaboración propia.

**Anexo 6 Adenda**
P á g i n a | 8
**Estudio Hidráulico**

**Tabla 3-4:** **Aplicación del test distribución normal.**

<!-- INICIO TABLA 3-4 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **Anexo 6 Adenda** P á g i n a | 8 **Estudio Hidráulico** -->

**Tabla 3-4: ** **Aplicación del test distribución normal.****

| Col1 | Col2 | 0 | 0 | fi | Fi (e) | e | c2 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0 | 1 | 23 | 0,852 | 0,664 | 0,664 | 0,053 |
| 2 | 1 | 2 | 1 | 0,037 | 0,903 | 0,239 | 0,171 |
| 3 | 2 | 3 | 2 | 0,074 | 0,985 | 0,082 | 0,001 |
| 4 | 3 | 4 | 0 | 0,000 | 0,999 | 0,014 | 0,014 |
| 5 | 4 | 5 | 1 | 0,037 | 1,000 | 0,001 | 1,133 |
| 6 | 5 | 5 | 0 | 0,000 | 1,000 | 0,000 | 0,000 |
| 7 | 5 | 5 | 0 | 0,000 | 1,000 | 0,000 | 0,000 |
| 8 | 5 | 5 | 0 | 0,000 | 1,000 | 0,000 | 0,000 |
| 9 | 5 | 5 | 0 | 0,000 | 1,000 | 0,000 | 0,000 |
| 10 | 5 | 5 | 0 | 0,000 | 1,000 | 0,000 | 0,000 |

<!-- Estadísticas: 10 filas, 8 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. **Tabla 3-5:** **Aplicación del test distribución log-normal.** -->
<!-- FIN TABLA 3-4 -->


|Col1|Col2|0|0|fi|Fi (e)|e|c2|
|---|---|---|---|---|---|---|---|
|1|0|1|23|0,852|0,664|0,664|0,053|
|2|1|2|1|0,037|0,903|0,239|0,171|
|3|2|3|2|0,074|0,985|0,082|0,001|
|4|3|4|0|0,000|0,999|0,014|0,014|
|5|4|5|1|0,037|1,000|0,001|1,133|
|6|5|5|0|0,000|1,000|0,000|0,000|
|7|5|5|0|0,000|1,000|0,000|0,000|
|8|5|5|0|0,000|1,000|0,000|0,000|
|9|5|5|0|0,000|1,000|0,000|0,000|
|10|5|5|0|0,000|1,000|0,000|0,000|

Fuente: Elaboración propia.

**Tabla 3-5:** **Aplicación del test distribución log-normal.**

<!-- INICIO TABLA 3-5 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |9|5|5|0|0,000|1,000|0,000|0,000| |10|5|5|0|0,000|1,000|0,000|0,000| Fuente: Elaboración propia. -->

**Tabla 3-5: ** **Aplicación del test distribución log-normal.****

| Col1 | Col2 | 0 | 0 | fi | Fi (e) | e | c2 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0 | 1 | 23 | 0,852 | 0,895 | 0,895 | 0,002 |
| 2 | 1 | 2 | 1 | 0,037 | 0,961 | 0,066 | 0,013 |
| 3 | 2 | 3 | 2 | 0,074 | 0,980 | 0,020 | 0,149 |
| 4 | 3 | 4 | 0 | 0,000 | 0,989 | 0,008 | 0,008 |
| 5 | 4 | 5 | 1 | 0,037 | 1,000 | 0,011 | 0,059 |
| 6 | 5 | 5 | 0 | 0,000 | 1,000 | 0,000 | 0,000 |
| 7 | 5 | 5 | 0 | 0,000 | 1,000 | 0,000 | 0,000 |
| 8 | 5 | 5 | 0 | 0,000 | 1,000 | 0,000 | 0,000 |
| 9 | 5 | 5 | 0 | 0,000 | 1,000 | 0,000 | 0,000 |
| 10 | 5 | 5 | 0 | 0,000 | 1,000 | 0,000 | 0,000 |

<!-- Estadísticas: 10 filas, 8 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente _:_ Elaboración propia. **Anexo 6 Adenda** P á g i n a | 9 -->
<!-- FIN TABLA 3-5 -->


|Col1|Col2|0|0|fi|Fi (e)|e|c2|
|---|---|---|---|---|---|---|---|
|1|0|1|23|0,852|0,895|0,895|0,002|
|2|1|2|1|0,037|0,961|0,066|0,013|
|3|2|3|2|0,074|0,980|0,020|0,149|
|4|3|4|0|0,000|0,989|0,008|0,008|
|5|4|5|1|0,037|1,000|0,011|0,059|
|6|5|5|0|0,000|1,000|0,000|0,000|
|7|5|5|0|0,000|1,000|0,000|0,000|
|8|5|5|0|0,000|1,000|0,000|0,000|
|9|5|5|0|0,000|1,000|0,000|0,000|
|10|5|5|0|0,000|1,000|0,000|0,000|

Fuente _:_ Elaboración propia.

**Anexo 6 Adenda**
P á g i n a | 9
**Estudio Hidráulico**

**Tabla 3-6:** **Aplicación del test distribución Pearson**

<!-- INICIO TABLA 3-6 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **Anexo 6 Adenda** P á g i n a | 9 **Estudio Hidráulico** -->

**Tabla 3-6: ** **Aplicación del test distribución Pearson****

| Col1 | Col2 | 0 | 0 | fi | y | Fi (e) | e | c2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0 | 1 | 23 | 0,852 | 0,760 | 0,797 | 0,797 | 0,004 |
| 2 | 1 | 2 | 1 | 0,037 | 1,361 | 0,909 | 0,112 | 0,050 |
| 3 | 2 | 3 | 2 | 0,074 | 1,961 | 0,957 | 0,048 | 0,015 |
| 4 | 3 | 4 | 0 | 0,000 | 2,562 | 0,979 | 0,022 | 0,022 |
| 5 | 4 | 5 | 1 | 0,037 | 3,162 | 1,000 | 0,021 | 0,011 |
| 6 | 5 | 5 | 0 | 0,000 | 3,162 | 1,000 | 0,000 | 0,000 |
| 7 | 5 | 5 | 0 | 0,000 | 3,162 | 1,000 | 0,000 | 0,000 |
| 8 | 5 | 5 | 0 | 0,000 | 3,162 | 1,000 | 0,000 | 0,000 |
| 9 | 5 | 5 | 0 | 0,000 | 3,162 | 1,000 | 0,000 | 0,000 |
| 10 | 5 | 5 | 0 | 0,000 | 3,162 | 1,000 | 0,000 | 0,000 |

<!-- Estadísticas: 10 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia **Tabla 3-7:** **Aplicación del test distribución Log-Pearson** -->
<!-- FIN TABLA 3-6 -->


|Col1|Col2|0|0|fi|y|Fi (e)|e|c2|
|---|---|---|---|---|---|---|---|---|
|1|0|1|23|0,852|0,760|0,797|0,797|0,004|
|2|1|2|1|0,037|1,361|0,909|0,112|0,050|
|3|2|3|2|0,074|1,961|0,957|0,048|0,015|
|4|3|4|0|0,000|2,562|0,979|0,022|0,022|
|5|4|5|1|0,037|3,162|1,000|0,021|0,011|
|6|5|5|0|0,000|3,162|1,000|0,000|0,000|
|7|5|5|0|0,000|3,162|1,000|0,000|0,000|
|8|5|5|0|0,000|3,162|1,000|0,000|0,000|
|9|5|5|0|0,000|3,162|1,000|0,000|0,000|
|10|5|5|0|0,000|3,162|1,000|0,000|0,000|

Fuente: Elaboración propia

**Tabla 3-7:** **Aplicación del test distribución Log-Pearson**

<!-- INICIO TABLA 3-7 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |9|5|5|0|0,000|3,162|1,000|0,000|0,000| |10|5|5|0|0,000|3,162|1,000|0,000|0,000| Fuente: Elaboración propia -->

**Tabla 3-7: ** **Aplicación del test distribución Log-Pearson****

| Col1 | Col2 | 0 | 0 | fi | y | Fi (e) | e | c2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0 | 1 | 23 | 0,852 | 4,531 | 0,890 | 0,890 | 0,002 |
| 2 | 1 | 2 | 1 | 0,037 | 5,338 | 0,930 | 0,040 | 0,000 |
| 3 | 2 | 3 | 2 | 0,074 | 5,823 | 0,950 | 0,020 | 0,146 |
| 4 | 3 | 4 | 0 | 0,000 | 6,171 | 0,960 | 0,010 | 0,010 |
| 5 | 4 | 5 | 1 | 0,037 | 6,443 | 0,970 | 0,010 | 0,073 |
| 6 | 5 | 5 | 0 | 0,000 | 6,443 | 0,970 | 0,000 | 0,000 |
| 7 | 5 | 5 | 0 | 0,000 | 6,443 | 0,970 | 0,000 | 0,000 |
| 8 | 5 | 5 | 0 | 0,000 | 6,443 | 0,970 | 0,000 | 0,000 |
| 9 | 5 | 5 | 0 | 0,000 | 6,443 | 0,970 | 0,000 | 0,000 |
| 10 | 5 | 5 | 0 | 0,000 | 6,443 | 0,970 | 0,000 | 0,000 |

<!-- Estadísticas: 10 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia **Anexo 6 Adenda** P á g i n a | 10 -->
<!-- FIN TABLA 3-7 -->


|Col1|Col2|0|0|fi|y|Fi (e)|e|c2|
|---|---|---|---|---|---|---|---|---|
|1|0|1|23|0,852|4,531|0,890|0,890|0,002|
|2|1|2|1|0,037|5,338|0,930|0,040|0,000|
|3|2|3|2|0,074|5,823|0,950|0,020|0,146|
|4|3|4|0|0,000|6,171|0,960|0,010|0,010|
|5|4|5|1|0,037|6,443|0,970|0,010|0,073|
|6|5|5|0|0,000|6,443|0,970|0,000|0,000|
|7|5|5|0|0,000|6,443|0,970|0,000|0,000|
|8|5|5|0|0,000|6,443|0,970|0,000|0,000|
|9|5|5|0|0,000|6,443|0,970|0,000|0,000|
|10|5|5|0|0,000|6,443|0,970|0,000|0,000|

Fuente: Elaboración propia

**Anexo 6 Adenda**
P á g i n a | 10
**Estudio Hidráulico**

**Tabla 3-8:** **Aplicación del test distribución Gumbel.**

<!-- INICIO TABLA 3-8 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **Anexo 6 Adenda** P á g i n a | 10 **Estudio Hidráulico** -->

**Tabla 3-8: ** **Aplicación del test distribución Gumbel.****

| Col1 | Col2 | 0 | 0 | fi | y | Fi (e) | e | c2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0 | 1 | 23 | 0,852 | 0,999 | 0,692 | 0,692 | 0,037 |
| 2 | 1 | 2 | 1 | 0,037 | 1,961 | 0,869 | 0,177 | 0,111 |
| 3 | 2 | 3 | 2 | 0,074 | 2,923 | 0,948 | 0,079 | 0,000 |
| 4 | 3 | 4 | 0 | 0,000 | 3,885 | 0,980 | 0,032 | 0,032 |
| 5 | 4 | 5 | 1 | 0,037 | 4,847 | 1,000 | 0,020 | 0,014 |
| 6 | 5 | 5 | 0 | 0,000 | 4,847 | 1,000 | 0,000 | 0,000 |
| 7 | 5 | 5 | 0 | 0,000 | 4,847 | 1,000 | 0,000 | 0,000 |
| 8 | 5 | 5 | 0 | 0,000 | 4,847 | 1,000 | 0,000 | 0,000 |
| 9 | 5 | 5 | 0 | 0,000 | 4,847 | 1,000 | 0,000 | 0,000 |
| 10 | 5 | 5 | 0 | 0,000 | 4,847 | 1,000 | 0,000 | 0,000 |

<!-- Estadísticas: 10 filas, 9 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. **Tabla 3-9:** **Resultados del test Chi** **[2 ]** -->
<!-- FIN TABLA 3-8 -->


|Col1|Col2|0|0|fi|y|Fi (e)|e|c2|
|---|---|---|---|---|---|---|---|---|
|1|0|1|23|0,852|0,999|0,692|0,692|0,037|
|2|1|2|1|0,037|1,961|0,869|0,177|0,111|
|3|2|3|2|0,074|2,923|0,948|0,079|0,000|
|4|3|4|0|0,000|3,885|0,980|0,032|0,032|
|5|4|5|1|0,037|4,847|1,000|0,020|0,014|
|6|5|5|0|0,000|4,847|1,000|0,000|0,000|
|7|5|5|0|0,000|4,847|1,000|0,000|0,000|
|8|5|5|0|0,000|4,847|1,000|0,000|0,000|
|9|5|5|0|0,000|4,847|1,000|0,000|0,000|
|10|5|5|0|0,000|4,847|1,000|0,000|0,000|

Fuente: Elaboración propia.

**Tabla 3-9:** **Resultados del test Chi** **[2 ]**

<!-- INICIO TABLA 3-9 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |9|5|5|0|0,000|4,847|1,000|0,000|0,000| |10|5|5|0|0,000|4,847|1,000|0,000|0,000| Fuente: Elaboración propia. -->

**Tabla 3-9: ** **Resultados del test Chi** **[2 ]****

| Distribución | c2 Calculado | No Param. | u | c2 Límite | Resto |
| --- | --- | --- | --- | --- | --- |
| Normal | 37,04 | 2 | 2 | 5,99 | -31,05 |
| Log-Normal | 6,25 | 2 | 2 | 5,99 | -0,26 |
| Pearson | 5,23 | 3 | 1 | 3,84 | 0,76 |
| Log-Pearson | 6,24 | 3 | 1 | 3,84 | -2,40 |
| Gumbel | 2,75 | 2 | 2 | 5,99 | 1,1 |

<!-- Estadísticas: 5 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. Considerando los resultados de la prueba de ajustes, se determina que la distribución de Gumbel -->
<!-- FIN TABLA 3-9 -->


|Distribución|c2 Calculado|No Param.|u|c2 Límite|Resto|
|---|---|---|---|---|---|
|Normal|37,04|2|2|5,99|-31,05|
|Log-Normal|6,25|2|2|5,99|-0,26|
|Pearson|5,23|3|1|3,84|0,76|
|Log-Pearson|6,24|3|1|3,84|-2,40|
|Gumbel|2,75|2|2|5,99|1,1|

Fuente: Elaboración propia.

Considerando los resultados de la prueba de ajustes, se determina que la distribución de Gumbel

es la que presenta de mejor manera la muestra de datos.

La Tabla 3-10, resume los resultados obtenidos a partir de la distribución Gumbel para distintos

periodos de retorno.

**Anexo 6 Adenda**
P á g i n a | 11
**Estudio Hidráulico**

**Tabla 3-10: Resultados del test Chi** **[2 ]**

<!-- INICIO TABLA 3-10 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **Anexo 6 Adenda** P á g i n a | 11 **Estudio Hidráulico** -->

**Tabla 3-10: Resultados del test Chi** **[2 ]****

| Período de retorno | Pp (mm) |
| --- | --- |
| 2 | 0,5 |
| 5 | 1,7 |
| 10 | 2,5 |
| 20 | 3,3 |
| 50 | 4,4 |
| 100 | 5,1 |

<!-- Estadísticas: 6 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. **Figura 3-1: Resultado y análisis de datos de frecuencia - distribución Gumbel.** -->
<!-- FIN TABLA 3-10 -->


|Período de retorno|Pp (mm)|
|---|---|
|2|0,5|
|5|1,7|
|10|2,5|
|20|3,3|
|50|4,4|
|100|5,1|

Fuente: Elaboración propia.

**Figura 3-1: Resultado y análisis de datos de frecuencia - distribución Gumbel.**

**Anexo 6 Adenda**
P á g i n a | 12
**Estudio Hidráulico**

**3.2.** **Criterios y metodología utilizada**

La determinación del caudal de crecida y del hidrograma de crecida para la cuenca asociada a la

quebrada Rio Seco, se realiza mediante el software HEC-HMS v4.6.1, desarrollado por el Cuerpo

de Ingenieros del ejército de EE.UU. Este software se basa en el método SCS Curva Número, el

que, a su vez, utiliza los parámetros descritos en la Tabla 11.

**Tabla 3-11: Parámetros utilizados en cálculo del caudal**

<!-- INICIO TABLA 3-11 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- de Ingenieros del ejército de EE.UU. Este software se basa en el método SCS Curva Número, el que, a su vez, utiliza los parámetros descritos en la Tabla 11. -->

**Tabla 3-11: Parámetros utilizados en cálculo del caudal****

| Parámetro | Valor |
| --- | --- |
| Área (km2) | 2167 |
| Longitud de escurrimiento superficial (m) | 101680 |
| Cota Max | 2923 |
| Cota min | 1071 |
| Curva Número | 74 |
| Tiempo de concentración (min) | 653.65 |

<!-- Estadísticas: 6 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente **:** Elaboración propia. La determinación de los parámetros Área, Longitud, Cota máx. y Cota min, se realiza mediante los modelos digitales de elevación y archivos shapefile, utilizando herramientas del software -->
<!-- FIN TABLA 3-11 -->


|Parámetro|Valor|
|---|---|
|Área (km2)|2167|
|Longitud de escurrimiento superficial (m)|101680|
|Cota Max|2923|
|Cota min|1071|
|Curva Número|74|
|Tiempo de concentración (min)|653.65|

Fuente **:** Elaboración propia.

La determinación de los parámetros Área, Longitud, Cota máx. y Cota min, se realiza mediante los
modelos digitales de elevación y archivos shapefile, utilizando herramientas del software
computacional ArcGIS 10.4.

Por su parte, la determinación del parámetro Curva Número para toda la zona de estudio se
realiza con la herramienta HEC-GEOHMS, la que a su vez incorpora los siguientes parámetros:

- Modelo digital de elevación

- Grupos hidrológicos presentes en el área de estudio

- Coberturas vegetales presentes en el área de estudio

Considerando esto, los modelos digitales de elevación asociados corresponden a los descritos
previamente (Topografía de detalle con curvas de nivel cada 1 metro), mientras que el grupo
hidrológico utilizado fue determinado de forma bibliográfica. Por otro lado, las coberturas
vegetales utilizadas corresponden a las coberturas de suelos disponibles en la página web de
Infraestructura de datos Geoespaciales de Chile.

Finalmente, la determinación del tiempo de concentración se realiza mediante el método del
Manual DGA capítulo 2.2, cuya fórmula es la siguiente:

Donde:

- Tc = Tiempo de concentración de la cuenca según el método california

- L = Longitud del Cauce principal

**Anexo 6 Adenda**
P á g i n a | 13
**Estudio Hidráulico**

- H = Desnivel máximo de la cuenca

Con los parámetros calculados, se obtiene el caudal de crecida para un periodo de retorno (T=100)
para la cuenca de la quebrada río Seco, el que corresponde a un Q=9.3 m3/s.

**4.** **MODELACIÓN HIDRÁULICA**

En este capítulo se muestra el procedimiento y resultados de la modelación hidráulica de los

cauces que influyen en el sitio de emplazamiento del proyecto, con una crecida con periodo de

retorno T = 100 años.

**4.1.** **Representación del cauce**

Para modelar el eje hidráulico de los afluentes asociados a las quebradas estudiadas, se utilizó el

software HEC-RAS v5.0.5, desarrollado por el cuerpo de Ingenieros del Ejército de EE.UU. Este

software, calcula la cota máxima del espejo de agua para distintas secciones de un cauce,

considerando la topografía, y sus características naturales, la rugosidad del lecho y la existencia de

interferencias u otras estructuras, definiendo así, el eje hidráulico. En lo principal, se consideró

lecho fijo, régimen permanente y flujo unidimensional. La Figura 4-1 muestra de manera gráfica

los términos involucrados en la ecuación de energía y la manera como ellas interactúan entre sí.

**Figura 4-1: Términos utilizados en la ecuación de energía.**

Fuente: González de Vallejo (2002).

**Anexo 6 Adenda**
P á g i n a | 14
**Estudio Hidráulico**

**4.2.** **Coeficiente de Manning**

Considerando la batimetría entregada para este estudio, se observa como la caja del río

corresponde a un estero de gran envergadura, con anchos que sobrepasan los 30m, por lo que se

adoptan coeficientes de Manning inferiores a los correspondientes a cauces secundarios, basados

en la Figura 4-2.

**Figura 4-2: Valores de n-manning sugeridos para cauces naturales.**

Fuente: González de Vallejos (2002).

**4.3.** **Caudal de simulación**

Para la simulación, se utiliza el caudal simulado y obtenido en los capítulos anteriores,

correspondiente a 9.3 m3/s.

La Figura 4-3 muestra la zona de modelación y los perfiles transversales trazados a lo largo del

cauce.

**Anexo 6 Adenda**
P á g i n a | 15
**Estudio Hidráulico**

**Figura 4-3: Zona de modelación.**

Fuente: Elaboración propia.

Asimismo, la Figura 4-4 muestra los alcances de la inundación que generarían los caudales

asociados al periodo de retorno de 100 años determinado para el análisis.

Al respecto, los resultados obtenidos permiten interpretar lo siguiente:

- Las inundaciones obtenidas, presentan láminas de agua similares que no sobrepasan los

6.5 m de altura en las zonas de mayor inundación.

- Asimismo, considerando el caudal obtenido, se observa como para el área de Proyecto, no

se determinan inundaciones que se acerquen o sobrepasen los límites de este.

- Lo anterior, podría relacionarse con los límites de la caja del cauce, los que se observa en la

imagen batimétrica, que se sitúan fuera del área de Proyecto.

**Anexo 6 Adenda**
P á g i n a | 16
**Estudio Hidráulico**

**Figura 4-4: Resultados de modelación.**

Fuente: Elaboración propia.

**5.** **CONCLUSIONES**

Se calculó el caudal máximo asociado a la cuenca vinculada a la quebrada río Seco, con un periodo

de retorno de T = 100 años, basado en la información de precipitaciones máximas en 24 horas

proporcionada por la estación meteorológica “Quillagua”, según la Dirección General de Aguas

(DGA).

El caudal obtenido corresponde a 9.3 m [3] /s, el que se utiliza en la modelación.

Los resultados obtenidos indican que, no existiría problema de desborde de la quebrada Rio Seco,

por crecidas de lluvia, dado que las láminas de agua no excederían las riberas de dicho cauce

(Apéndice 6.1).

**Anexo 6 Adenda**
P á g i n a | 17
**Estudio Hidráulico**

**6.** **APÉNDICES**

**6.1.** **Perfiles Transversales de modelación**

A continuación, se presentan los perfiles transversales modelados con sus respectivas láminas de

agua. Los perfiles se disponen de Norte a Sur, totalizando 23 perfiles transversales.

**Anexo 6 Adenda**
P á g i n a | 18
**Estudio Hidráulico**

**Anexo 6 Adenda**
P á g i n a | 19
**Estudio Hidráulico**

**Anexo 6 Adenda**
P á g i n a | 20
**Estudio Hidráulico**

**Anexo 6 Adenda**
P á g i n a | 21
**Estudio Hidráulico**

**Anexo 6 Adenda**
P á g i n a | 22
**Estudio Hidráulico**

**Anexo 6 Adenda**
P á g i n a | 23
**Estudio Hidráulico**

**Anexo 6 Adenda**
P á g i n a | 24
**Estudio Hidráulico**

**Anexo 6 Adenda**
P á g i n a | 25
**Estudio Hidráulico**

**Anexo 6 Adenda**
P á g i n a | 26
**Estudio Hidráulico**

**Anexo 6 Adenda**
P á g i n a | 27
**Estudio Hidráulico**

**Anexo 6 Adenda**
P á g i n a | 28
**Estudio Hidráulico**

**6.2** **BARIMETRÍA**

A continuación, se presentan los planos asociados a la batimetría realizada en el área del Proyecto,

los cuales se anexan en el presente informe y de manera independiente con el fin de detallarlos en

mejor calidad de imagen, en caso de que se requiera.

**Anexo 6 Adenda**
P á g i n a | 29
**Estudio Hidráulico**

**Anexo 6 Adenda**
P á g i n a | 30
**Estudio Hidráulico**

**Anexo 6 Adenda**
P á g i n a | 31
**Estudio Hidráulico**

**Anexo 6 Adenda**
P á g i n a | 32
**Estudio Hidráulico**