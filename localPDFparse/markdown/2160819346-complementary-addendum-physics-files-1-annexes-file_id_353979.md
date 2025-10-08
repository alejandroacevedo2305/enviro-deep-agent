---
title: Inventario de emisiones y modelación de calidad del airE
author: carlos
date: D:20240705150550-04'00'
language: es
type: report
pages: 32
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - MODELACIÓN DE EMISIONES ATMOSFÉRICAS ADENDA 2 Declaración de Impacto Ambiental, Proyecto: “Central BESS Halcón 7”
-->

# MODELACIÓN DE EMISIONES ATMOSFÉRICAS ADENDA 2 Declaración de Impacto Ambiental, Proyecto: “Central BESS Halcón 7”

Región de Arica y Parinacota.

Julio 2024.

_Modelación de Emisiones Atmosféricas, Adenda 2, DIA: “Central BESS Halcón 7”_

**ÍNDICE**

_**1**_ _**Introducción .............................................................................................................. 3**_

_**2**_ _**Emplazamiento del Proyecto ................................................................................... 3**_

_**3**_ _**Cronograma del Proyecto ........................................................................................ 4**_

_**4**_ _**Emisiones Proyecto.................................................................................................. 4**_

_**5**_ _**Modelación de Calidad del Aire ............................................................................... 5**_

**5.1** **Descripción del Modelo Utilizado .................................................................................... 5**

**5.2** **Dominio de Modelación .................................................................................................... 7**

**5.3** **Topografía .......................................................................................................................... 8**

**5.4** **Características Meteorológicas ....................................................................................... 9**
**5.4.1** **Series de tiempo ........................................................................................................ 9**

**5.5** **Ubicación de Receptores ............................................................................................... 13**

**5.6** **Normativa ......................................................................................................................... 15**

**9.7** **Escenario de Modelación ............................................................................................... 15**

**9.8** **Resultados en punto de mayor concentración ............................................................ 16**

**9.9** **Comparación con norma de calidad ............................................................................. 16**

_**6**_ _**Mapas de Isoconcentraciones ............................................................................... 20**_

**6.1** **Fase de Construcción ..................................................................................................... 20**

**6.2** **Fase de Operación .......................................................................................................... 23**

**6.3** **Fase de Cierre .................................................................................................................. 26**

_**7**_ _**Área de Influencia ................................................................................................... 29**_

_**8**_ _**Conclusión .............................................................................................................. 31**_

_**9**_ _**Anexos .................................................................................................................... 31**_

**9.1** **Anexo 1: Archivos de modelación AERMOD (Formato Rar) ...................................... 31**

w w w . i g e m a . c l

P á g i n a | 1

_Modelación de Emisiones Atmosféricas, Adenda 2, DIA: “Central BESS Halcón 7”_

**ÍNDICE DE TABLAS**

Tabla 4-1 Resultados Emisiones Fase de Construcción Año 1 ..................................................................... 4
Tabla 5-1 Información de Estación Meteorológica ........................................................................................ 9
Tabla 5-2 Receptores cercanos .................................................................................................................. 13
Tabla 5-3 Receptores MPS cercanos ......................................................................................................... 14
Tabla 5-4 Normativa de calidad del aire usada de referencia ..................................................................... 15
Tabla 5-5 Resultados punto de mayor concentración Fase de Construcción ............................................. 16
Tabla 5-6 Resultados punto de mayor concentración Fase de Operación .................................................. 16
Tabla 5-7 Resultados punto de mayor concentración Fase de Cierre ........................................................ 16
Tabla 5-8 Aporte de MP 10 y MP 2,5 del Proyecto en receptores cercanos Fase de Construcción ................ 17
Tabla 5-9 Aporte MPS del Proyecto en receptores cercanos Fase de Construcción .................................. 17
Tabla 5-10 Aporte de MP 10 y MP 2,5 del Proyecto en receptores cercanos Fase de Operación ................ 18
Tabla 5-11 Aporte MPS del Proyecto en receptores cercanos Fase de Operación .................................. 18
Tabla 5-12 Aporte de MP10 y MP2,5 del Proyecto en receptores cercanos Fase de Cierre .................... 19
Tabla 5-13 Aporte MPS del Proyecto en receptores cercanos Fase de Cierre ......................................... 19

**ÍNDICE DE FIGURAS**

Figura 2-1 Emplazamiento del Proyecto, Coordenadas UTM WGS 84 H19S ................................................... 3
Figura 3-1 Cronograma del Proyecto. ................................................................................................................ 4
Figura 5-1 Diagrama General de Sistema de Modelación Aermod ................................................................ 6
Figura 5-2 Dominio de Modelación. UTM WGS 84, H 19S............................................................................. 7
Figura 5-3 Mapa de Topográfico 2D. UTM, WGS 84, H 19s .......................................................................... 8
Figura 5-4 Serie del tiempo velocidad del viento, m/s .................................................................................... 9
Figura 5-5 Serie de tiempo dirección del viento ........................................................................................... 10
Figura 5-6 Rosa de los Vientos, Promedio Horario. ..................................................................................... 10
Figura 5-7 Ciclo 24 horas de dirección del viento ......................................................................................... 11
Figura 5-8 Gráficos de series de tiempo, Temperatura ................................................................................ 11
Figura 5-9 Gráficos de series en el tiempo Humedad Relativa .................................................................... 12
Figura 5-10 Gráfico de serie en el tiempo Radiación Solar ........................................................................ 12
Figura 5-11 Receptores Humanos ............................................................................................................. 13
Figura 5-12 Receptores MPS ..................................................................................................................... 14
Figura 6-1 Mapa Isocentración MP 10 24 hrs P98 Fase de Construcción ...................................................... 20
Figura 6-2 Mapa Isocentración MP 10 Anual Fase de Construcción .............................................................. 20
Figura 6-3 Mapa Isocentración MP 2,5 24 hrs P98 Fase de Construcción ..................................................... 21
Figura 6-4 Mapa Isocentración MP 2,5 Anual Fase de Construcción ............................................................. 21
Figura 6-5 Mapa isodeposición MPS Anual Fase de Construcción .............................................................. 22
Figura 6-6 Mapa Isocentración MP10 24 hrs P98 Fase de Operación ......................................................... 23
Figura 6-7 Mapa Isocentración MP 10 Anual Fase de Operación .................................................................. 23
Figura 6-8 Mapa Isocentración MP 2,5 24 hrs P98 Fase de Operación .......................................................... 24
Figura 6-9 Mapa Isocentración MP 2,5 Anual Fase de Operación .................................................................. 24
Figura 6-10 Mapa isodeposición MPS Anual Fase de Operación .............................................................. 25
Figura 6-11 Mapa Isocentración MP 10 24 hrs P98 Fase de Cierre............................................................. 26
Figura 6-12 Mapa Isocentración MP 10 Anual Fase de Cierre ..................................................................... 26
Figura 6-13 Mapa Isocentración MP 2,5 24 hrs P98 Fase de Cierre ............................................................ 27
Figura 6-14 Mapa Isocentración MP 2,5 Anual Fase de Cierre .................................................................... 27
Figura 6-15 Mapa isodeposición MPS Anual Fase de Cierre..................................................................... 28
Figura 7-1 Área de Influencia de Calidad del Aire ........................................................................................ 30

w w w . i g e m a . c l

P á g i n a | 2

_Modelación de Emisiones Atmosféricas, Adenda 2, DIA: “Central BESS Halcón 7”_

**1** **Introducción**

En el presente documento se desarrolla el informe de modelación de material particulado
de Emisiones Atmosféricas asociadas a las actividades del Proyecto: “Central BESS Halcón
7”. Las emisiones modeladas corresponden a Material Particulado; MP 2,5, MP 10 y MPS, para
las fases de Construcción, Operación y Cierre.

La modelación de material particulado se realiza, utilizando el Modelo Aermod, el cual se
encuentra dentro los Software recomendados por la “Guía para Uso de Modelos de Calidad
del Aire en el SEA” del Servicio de Evaluación Ambiental, 2023.

**2** **Emplazamiento del Proyecto**

El Proyecto se ubicará administrativamente en la Región de Arica y Parinacota, Provincia
del Arica, Comuna de Arica.

A continuación, en la Figura 2-1 se presenta la localización del proyecto, cuya
representación cartográfica fue elaborada utilizando coordenadas UTM Datum WGS84,
H19 Sur.

**Figura 2-1 Emplazamiento del Proyecto, Coordenadas UTM WGS 84 H19S**

_Fuente: Elaboración propia._

w w w . i g e m a . c l

P á g i n a | 3

_Modelación de Emisiones Atmosféricas, Adenda 2, DIA: “Central BESS Halcón 7”_

**3** **Cronograma del Proyecto**

El Proyecto considera una fase de Construcción de 18 meses, luego se estima que tenga
una vida útil de 30 años, una vez cumplido este tiempo se evaluará la viabilidad y factibilidad
económica para extender su vida útil, de no ser factible se procederá a su cierre, que se
estima que tendrá una duración de 6 meses.

La Figura 3-1, presenta el cronograma general para cada una de las fases del Proyecto
(Construcción, Operación y Cierre).

**Figura 3-1 Cronograma del Proyecto.**

|Fase|Construcción<br>(meses)|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Operación<br>(años)|Col17|Col18|Col19|Col20|Col21|Col22|Cierre<br>(meses)|Col24|Col25|Col26|Col27|Col28|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Fase**|1|2|3|4|5|6|7|8|9|10|11|12|...|18|1|5|10|15|20|25|30|1|2|3|4|5|6|
|Construcción||||||||||||||||||||||||||||
|Operación||||||||||||||||||||||||||||
|Cierre||||||||||||||||||||||||||||

_Fuente: DIA “Central BESS halcón 7”._

**4** **Emisiones Proyecto**

En el presente capítulo se presenta el resumen de las emisiones atmosféricas del proyecto,
la cuales fueron obtenidas del informe de Actualización Inventario y Modelación de
Emisiones Atmosféricas, presentado en el Anexo 1.2 de la Adenda del “ _Central BESS_
_Halcón 7_ .”

**Tabla 4-1** **Emisiones Central Bess Halcón 7**

|FASE|Emisión, t/año|Col3|Col4|
|---|---|---|---|
|**FASE**|**MP**|**MP10 **|**MP2,5 **|
|Construcción (Año 1)|9,66|2,62|0,41|
|Operación|1,10|0,31|0,03|
|Cierre|4,78|1,29|0,21|

_Fuente: Actualización Inventario y Modelación de Emisiones Atmosféricas, presentado en el Anexo 1.2 de la Adenda del_

_proyecto “Central BESS Halcón 7.”_

w w w . i g e m a . c l

P á g i n a | 4

_Modelación de Emisiones Atmosféricas, Adenda 2, DIA: “Central BESS Halcón 7”_

**5** **Modelación de Calidad del Aire**

**5.1** **Descripción del Modelo Utilizado**

Se desarrolla la modelación de material particulado usando el Modelo Aermod, el cual se
encuentra dentro los Software recomendados por la “Guía para Uso de Modelos de Calidad
del Aire en el SEA” del Servicio de Evaluación Ambiental, 2023.

El programa de modelamiento AERMOD de dispersión de aire, incorpora modelos de la
U.S. EPA dentro de una interfaz como son: ISCST3, ISC-PRIME, AERMOD y AERMODPRIME. Estos son usados extensamente para estimar la concentración de los parámetros
evaluados y deposición desde una amplia variedad de fuentes. Incluye un amplio rango de
opciones para modelar impactos en la calidad del aire debido a fuentes de contaminación.
El modelo de dispersión requiere una serie de datos de entrada como son el tipo y ubicación
de la fuente, tipo de contaminantes emitidos, datos meteorológicos que influyen en el
transporte y dispersión de contaminantes. Asimismo, considera la naturaleza de la
topografía de la zona, integrando coordenadas de ubicación de fuentes y receptores, y
niveles de altitud.

La ecuación de distribución gaussiana emplea cálculos que requieren dos parámetros de
dispersión (σy y σz) para identificar la variación de las concentraciones de contaminantes
que se encuentran viento abajo de la emisión. Esta ecuación determina las concentraciones
de contaminantes en cualquier punto del espacio.

En la Figura 5-1 se muestra de manera esquemática el funcionamiento del modelo, donde
se compone de un módulo de modelación meteorológica AERMET, otro de procesamiento
de superficie AERMAP, y por último el módulo que realiza la modelación de dispersión de
los contaminantes atmosféricos Aermod.

w w w . i g e m a . c l

P á g i n a | 5

_Modelación de Emisiones Atmosféricas, Adenda 2, DIA: “Central BESS Halcón 7”_

**Figura 5-1** **Diagrama General de Sistema de Modelación Aermod**

_Fuente: Elaboración en Propia en base Aermod Modeling System, EPA_

w w w . i g e m a . c l

P á g i n a | 6

_Modelación de Emisiones Atmosféricas, Adenda 2, DIA: “Central BESS Halcón 7”_

**5.2** **Dominio de Modelación**

La Guía para el Uso de Modelos de Calidad del Aire en el SEIA, hace referencia al Dominio
de Modelación exponiendo lo siguiente: “la extensión del área de modelación, o dominio
espacial, se define en función de la magnitud del proyecto y sus emisiones, así como de la
presencia de receptores susceptibles de ser afectados...”.

Para efecto de evaluar el aporte en la calidad del aire por el Proyecto, se desarrolló la
modelación mediante el uso del Software AERMOD, con un dominio de 20x20 km, con un
tamaño de celda de 1 x 1 km.

**Figura 5-2** **Dominio de Modelación. UTM WGS 84, H 19S.**

_Fuente: Elaboración Propia._

w w w . i g e m a . c l

P á g i n a | 7

_Modelación de Emisiones Atmosféricas, Adenda 2, DIA: “Central BESS Halcón 7”_

**5.3** **Topografía**

En la siguiente Tabla se muestra la topografía del dominio, que fue obtenida de las bases
satelitales topográficas SRTM3, que poseen una cobertura global con aproximadamente 90
m de resolución.

**Figura 5-3** **Mapa de Topográfico 2D. UTM, WGS 84, H 19s**

_Fuente: Elaboración propia._

w w w . i g e m a . c l

P á g i n a | 8

_Modelación de Emisiones Atmosféricas, Adenda 2, DIA: “Central BESS Halcón 7”_

**5.4** **Características Meteorológicas**

La información meteorológica fue obtenida de la estación La Violeta Open, Arica. Los datos
son accesibles desde el sitio web [https://agrometeorologia.cl/# El periodo considerado](https://agrometeorologia.cl/)
corresponde de enero a diciembre 2023.

En Tabla 5-1 se presenta las coordenadas de ubicación de la Estación La Violeta Open.

**Tabla 5-1** **Información de Estación Meteorológica**

|Nombre de la<br>estación|Coordenada UTM WGS 84<br>H 19s (m)|Col3|Parámetros meteorológicos medidos|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Nombre**<br>**de**<br>**la**<br>**estación**|**Coordenada UTM WGS 84**<br>**H 19s (m)**|**Coordenada UTM WGS 84**<br>**H 19s (m)**|**HR**|**TA**|**DV**|**VV**|**R **|**P **|
|La Violeta Open|E 372271|N 7952960|X|X|X|X|X|X|

_Fuente: Elaboración propia._

HR: humedad relativa; TA: Temperatura ambiente; DV: dirección del viento; VV: velocidad
del viento, R: Radiación P: Presión atmosférica.

La estación La Violeta Open, en el periodo analizado cuenta con 8.740 datos registrados,
lo que representa un 99% de completitud de datos.

**5.4.1 Series de tiempo**

A continuación, se presentan los gráficos de series de tiempo.

**5.4.1.1** _**Velocidad y Dirección del Viento**_

De acuerdo con la información recopilada, el promedio horario de velocidad del viento
promedio del periodo es de 0,6 m/s.

El gráfico de serie de tiempo de la variable meteorológica velocidad del viento, se
representa en la Figura 5-4.

**Figura 5-4** **Serie del tiempo velocidad del viento, m/s**

_Fuente: Elaboración propia_

w w w . i g e m a . c l

P á g i n a | 9

_Modelación de Emisiones Atmosféricas, Adenda 2, DIA: “Central BESS Halcón 7”_

En la Figura 5-5 se presenta la serie de tiempo del promedio diario de la dirección del viento,
en la que la dirección predominante es la componente NorOeste.

**Figura 5-5** **Serie de tiempo dirección del viento**

_Fuente: Elaboración propia_

En la Figura 5-6 se presenta la Rosa de los Vientos. De los datos registrados, un 28,2% se
encuentra entre un 0,5 y 2,1 m/s, un 9,8% entre 2,1 y 3,6 m/s mientras que las Calmas
están en 61,7%.

**Figura 5-6** **Rosa de los Vientos, Promedio Horario.**

_Fuente: Elaboración Propia._

w w w . i g e m a . c l

P á g i n a | 10

_Modelación de Emisiones Atmosféricas, Adenda 2, DIA: “Central BESS Halcón 7”_

En la Figura 5-7 se presenta el ciclo horario de la dirección del viento para el periodo
analizado. Se observa que, durante el día, la dirección predominante es Noroeste.

**Figura 5-7** **Ciclo 24 horas de dirección del viento**

_Fuente: Elaboración Propia_

**5.4.1.2** _**Temperatura**_

En el gráfico de la Figura 5-8 se presenta la temperatura promedio horaria. La media anual
fue de 20,6 °C. En periodo otoño-invierno disminuye la temperatura, siendo estas las
temperaturas más bajas del año. Las temperaturas extremas registradas correspondieron
a 8,9 °C en julio y 33,1 °C en marzo.

**Figura 5-8** **Gráficos de series de tiempo, Temperatura**

_Fuente: Elaboración Propia._

**5.4.1.3** _**Humedad Relativa**_

La serie del tiempo de la variable humedad relativa, es presentada en el gráfico de la Figura
5-9 donde es posible observar que en general presentó valores dentro de un rango de
38,3% y 93,6%, con un promedio diario anual de 71,8%.

w w w . i g e m a . c l

P á g i n a | 11

_Modelación de Emisiones Atmosféricas, Adenda 2, DIA: “Central BESS Halcón 7”_

**Figura 5-9** **Gráficos de series en el tiempo Humedad Relativa**

_Fuente: Elaboración Propia_

**5.4.1.4** _**Radiación solar**_

El gráfico de serie de tiempo de la variable meteorológica radiación solar, se presenta en la
Figura 5-10, donde se observa una marcada curva que disminuye en los meses de otoñoinvierno. Los mayores valores fueron presentados en los meses de primavera-verano, con
una máxima de 999 W/m [2 ] en febrero y septiembre de 2023.

**Figura 5-10** **Gráfico de serie en el tiempo Radiación Solar**

_Fuente: Elaboración Propia_

w w w . i g e m a . c l

P á g i n a | 12

_Modelación de Emisiones Atmosféricas, Adenda 2, DIA: “Central BESS Halcón 7”_

**5.5** **Ubicación de Receptores**

**Tabla 5-2** **Receptores cercanos**

|Receptor|Coordenadas UTM, WGS 84<br>Huso 19|Col3|Distancia desde<br>perímetro|
|---|---|---|---|
|**Receptor**|**X, m**|**Y, m**|**m **|
|1|367993|7954589|2.000|
|2|368758|7954166|1.630|
|3|369454|7954141|1.250|
|4|369846|7953744|1.580|

_Fuente: Elaboración Propia._

**Figura 5-11** **Receptores Humanos**

_Fuente: Elaboración Propia_

w w w . i g e m a . c l

P á g i n a | 13

_Modelación de Emisiones Atmosféricas, Adenda 2, DIA: “Central BESS Halcón 7”_

**Tabla 5-3** **Receptores MPS cercanos**

|Receptor|Coordenadas UTM, WGS 84<br>Huso 19|Col3|Distancia desde<br>perímetro,|
|---|---|---|---|
|**Receptor**|**X, m**|**Y, m**|**m **|
|1: Pequeños Granjeros|383374|7955176|13.366|
|2: Asoc Wali Qhantati|381998|7954457|12.026|

_Fuente: Elaboración Propia._

**Figura 5-12** **Receptores MPS**

_Fuente: Elaboración Propia_

w w w . i g e m a . c l

P á g i n a | 14

_Modelación de Emisiones Atmosféricas, Adenda 2, DIA: “Central BESS Halcón 7”_

**5.6** **Normativa**

La normativa de referencia utilizada para comparar la concentración de material particulado
y gases generados por el Proyecto se presenta en la Tabla 5-4.

<!-- INICIO TABLA 5-4 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **5.6** **Normativa** La normativa de referencia utilizada para comparar la concentración de material particulado y gases generados por el Proyecto se presenta en la Tabla 5-4. -->

**Tabla 5-4: ** **Normativa de calidad del aire usada de referencia****

| Parámetro | Estadístico | Valor Normado | Normativa |
| --- | --- | --- | --- |
| MP10 | Anual | 50 μg/m3 | D.S. N° 12/22 MMA |
| MP10 | Percentil 98 24 horas | 130 μg/m3 | 130 μg/m3 |
| MP2,5 | Anual | 20 μg/m3 | D.S. N° 12/10 MMA |
| MP2,5 | Percentil 98 24 horas | 50 μg/m3 | 50 μg/m3 |

<!-- Estadísticas: 4 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- _Fuente: Elaboración Propia_ **9.7** **Escenario de Modelación** -->
<!-- FIN TABLA 5-4 -->


**Tabla 5-4** **Normativa de calidad del aire usada de referencia**

|Parámetro|Estadístico|Valor Normado|Normativa|
|---|---|---|---|
|MP10|Anual|50 μg/m3|D.S. N° 12/22 MMA|
|MP10|Percentil 98 24 horas|130 μg/m3|130 μg/m3|
|MP2,5|Anual|20 μg/m3|D.S. N° 12/10 MMA|
|MP2,5|Percentil 98 24 horas|50 μg/m3|50 μg/m3|

_Fuente: Elaboración Propia_

**9.7** **Escenario de Modelación**

El escenario considerado para la modelación corresponde a las emisiones de Fase de
Construcción (Año 1 peor escenario), Fase Operación y Fase de Cierre.

Para la modelación, de acuerdo con los requerimientos metodológicos, se efectuó la
recopilación, procesamiento y selección de datos de entrada necesarios para alimentar el
modelo de dispersión.

En el presente apartado se exponen los resultados obtenidos de la modelación de
dispersión de MP 10, MP 2,5, MPS

Esta sección está separada por los resultados de modelación en punto de mayor
concentración y el aporte en receptores cercanos al Proyecto.

w w w . i g e m a . c l

P á g i n a | 15

_Modelación de Emisiones Atmosféricas, Adenda 2, DIA: “Central BESS Halcón 7”_

**9.8** **Resultados en punto de mayor concentración**

A continuación, se presentan los resultados obtenidos del punto de mayor concentración.

**Tabla 5-5** **Resultados punto de mayor concentración Fase de Construcción**

|Parámetro|Estadístico|Unidad|Valor<br>modelado|Coordenada UTM, WGS 84, Huso 19|Col6|
|---|---|---|---|---|---|
|**Parámetro**|**Estadístico**|**Unidad**|**Valor**<br>**modelado**|**Este**|**Norte**|
|MP10|24 horas P98|μg/m3|3,96|373147|7955050|
|MP10|Anual|μg/m3|1,74|373147|7955050|
|MP2,5|24 horas P98|μg/m3|0,4|373147|7955050|
|MP2,5|Anual|μg/m3|0,18|373147|7955050|
|MPS|Anual|mg/m2 día|0,86|373147|7955050|

_Fuente: Elaboración Propia_

**Tabla 5-6** **Resultados punto de mayor concentración Fase de Operación**

|Parámetro|Estadístico|Unidad|Valor<br>modelado|Coordenada UTM, WGS 84, Huso 19|Col6|
|---|---|---|---|---|---|
|**Parámetro**|**Estadístico**|**Unidad**|**Valor**<br>**modelado**|**Este**|**Norte**|
|MP10|24 horas P98|μg/m3|0,57|373147|7955050|
|MP10|Anual|μg/m3|0,25|373147|7955050|
|MP2,5|24 horas P98|μg/m3|0,96|373147|7955050|
|MP2,5|Anual|μg/m3|0,03|373147|7955050|
|MPS|Anual|mg/m2 día|0,12|373147|7955050|

_Fuente: Elaboración Propia_

**Tabla 5-7** **Resultados punto de mayor concentración Fase de Cierre**

|Parámetro|Estadístico|Unidad|Valor<br>modelado|Coordenada UTM, WGS 84, Huso 19|Col6|
|---|---|---|---|---|---|
|**Parámetro**|**Estadístico**|**Unidad**|**Valor**<br>**modelado**|**Este**|**Norte**|
|MP10|24 horas P98|μg/m3|0,06|373147|7955050|
|MP10|Anual|μg/m3|0,02|373147|7955050|
|MP2,5|24 horas P98|μg/m3|0,01|373147|7955050|
|MP2,5|Anual|μg/m3|0,01|373147|7955050|
|MPS|Anual|mg/m2 día|0,08|373147|7955050|

_Fuente: Elaboración Propia_

De acuerdo con los resultados obtenidos en el punto de mayor concentración, todos ellos
se encuentran bajo las normas de calidad del aire usadas como referencia.

**9.9** **Comparación con norma de calidad**

En las tablas siguientes, se exponen los resultados obtenidos de la modelación de calidad
del aire en el receptor cercano, presentando además la relación porcentual del aporte del
Proyecto con respecto a la normativa de referencia utilizada.

w w w . i g e m a . c l

P á g i n a | 16

_Modelación de Emisiones Atmosféricas, Adenda 2, DIA: “Central BESS Halcón 7”_

**Tabla 5-8** **Aporte de MP** **10** **y MP** **2,5** **del Proyecto en receptores cercanos Fase de**

**Construcción**

|Receptor|Contaminante|Estadístico|Aporte del Proyecto,<br>ug/m3|Normativa, ug/m3|Porcentaje<br>respecto a<br>normativa, %|
|---|---|---|---|---|---|
|R1|MP10|24 hrs P98|0,29|130|0,22%|
|R1|MP10|Anual|0,11|50|0,22%|
|R1|MP2,5|24 hrs P98|0,04|50|0,08%|
|R1|MP2,5|Anual|0,02|20|0,10%|
|R2|MP10|24 hrs P98|0,22|130|0,17%|
|R2|MP10|Anual|0,11|50|0,22%|
|R2|MP2,5|24 hrs P98|0,03|50|0,06%|
|R2|MP2,5|Anual|0,01|20|0,05%|
|R3|MP10|24 hrs P98|0,22|130|0,17%|
|R3|MP10|Anual|0,1|50|0,20%|
|R3|MP2,5|24 hrs P98|0,03|50|0,06%|
|R3|MP2,5|Anual|0,01|20|0,05%|
|R4|MP10|24 hrs P98|0,28|130|0,22%|
|R4|MP10|Anual|0,11|50|0,22%|
|R4|MP2,5|24 hrs P98|0,04|50|0,08%|
|R4|MP2,5|Anual|0,02|20|0,10%|

_Fuente: Elaboración Propia_

**Tabla 5-9** **Aporte MPS del Proyecto en receptores cercanos Fase de Construcción**

|Receptor|Contaminante|Estadístico|Aporte del Proyecto,<br>mg/m2 día|Normativa,<br>mg/m2 día|Porcentaje<br>respecto a<br>normativa, %|
|---|---|---|---|---|---|
|R1 MPS|MPS|Anual|0,02|200|0,01%|
|R2 MPS|MPS|Anual|0,01|200|0,01%|

_Fuente: Elaboración Propia_

w w w . i g e m a . c l

P á g i n a | 17

_Modelación de Emisiones Atmosféricas, Adenda 2, DIA: “Central BESS Halcón 7”_

**Tabla 5-10** **Aporte de MP** **10** **y MP** **2,5** **del Proyecto en receptores cercanos Fase de**

**Operación**

|Receptor|Contaminante|Estadístico|Aporte del Proyecto,<br>ug/m3|Normativa, ug/m3|Porcentaje<br>respecto a<br>normativa, %|
|---|---|---|---|---|---|
|R1|MP10|24 hrs P98|0,04|130|0,03%|
|R1|MP10|Anual|0,02|50|0,04%|
|R1|MP2,5|24 hrs P98|0,004|50|0,01%|
|R1|MP2,5|Anual|0,002|20|0,01%|
|R2|MP10|24 hrs P98|0,04|130|0,03%|
|R2|MP10|Anual|0,01|50|0,02%|
|R2|MP2,5|24 hrs P98|0,003|50|0,01%|
|R2|MP2,5|Anual|0,001|20|0,01%|
|R3|MP10|24 hrs P98|0,03|130|0,02%|
|R3|MP10|Anual|0,01|50|0,02%|
|R3|MP2,5|24 hrs P98|0,003|50|0,01%|
|R3|MP2,5|Anual|0,001|20|0,01%|
|R4|MP10|24 hrs P98|0,02|130|0,02%|
|R4|MP10|Anual|0,01|50|0,02%|
|R4|MP2,5|24 hrs P98|0,003|50|0,01%|
|R4|MP2,5|Anual|0,001|20|0,01%|

_Fuente: Elaboración Propia_

**Tabla 5-11** **Aporte MPS del Proyecto en receptores cercanos Fase de Operación**

|Receptor|Contaminante|Estadístico|Aporte del Proyecto,<br>mg/m2 día|Normativa,<br>mg/m2 día|Porcentaje<br>respecto a<br>normativa, %|
|---|---|---|---|---|---|
|R1 MPS|MPS|Anual|0,003|200|0,002%|
|R2 MPS|MPS|Anual|0,001|200|0,001%|

_Fuente: Elaboración Propia_

w w w . i g e m a . c l

P á g i n a | 18

_Modelación de Emisiones Atmosféricas, Adenda 2, DIA: “Central BESS Halcón 7”_

**Tabla 5-12** **Aporte de MP10 y MP2,5 del Proyecto en receptores cercanos Fase de Cierre**

|Receptor|Contaminante|Estadístico|Aporte del Proyecto,<br>ug/m3|Normativa, ug/m3|Porcentaje<br>respecto a<br>normativa, %|
|---|---|---|---|---|---|
|R1|MP10|24 hrs P98|0,001|130|0,0008%|
|R1|MP10|Anual|0,003|50|0,0060%|
|R1|MP2,5|24 hrs P98|0,0006|50|0,0012%|
|R1|MP2,5|Anual|0,003|20|0,0150%|
|R2|MP10|24 hrs P98|0,0001|130|0,0001%|
|R2|MP10|Anual|0,001|50|0,0020%|
|R2|MP2,5|24 hrs P98|0,00004|50|0,0001%|
|R2|MP2,5|Anual|0,0003|20|0,0015%|
|R3|MP10|24 hrs P98|0,0001|130|0,0001%|
|R3|MP10|Anual|0,001|50|0,0020%|
|R3|MP2,5|24 hrs P98|0,00003|50|0,0001%|
|R3|MP2,5|Anual|0,0002|20|0,0010%|
|R4|MP10|24 hrs P98|0,0003|130|0,0002%|
|R4|MP10|Anual|0,001|50|0,0020%|
|R4|MP2,5|24 hrs P98|0,00007|50|0,0001%|
|R4|MP2,5|Anual|0,0001|20|0,0005%|

_Fuente: Elaboración Propia_

**Tabla 5-13** **Aporte MPS del Proyecto en receptores cercanos Fase de Cierre**

|Receptor|Contaminante|Estadístico|Aporte del Proyecto,<br>mg/m2 día|Normativa,<br>mg/m2 día|Porcentaje<br>respecto a<br>normativa, %|
|---|---|---|---|---|---|
|R1 MPS|MPS|Anual|0,002|200|0,001%|
|R2 MPS|MPS|Anual|0,002|200|0,001%|

_Fuente: Elaboración Propia_

De acuerdo con los resultados obtenidos de la modelación en las tres Fases del Proyecto,
el aporte de material particulado en receptores cercanos no es significativo respecto a las
normas de calidad del aire usadas de referencia.

w w w . i g e m a . c l

P á g i n a | 19

_Modelación de Emisiones Atmosféricas, Adenda 2, DIA: “Central BESS Halcón 7”_

**6** **Mapas de Isoconcentraciones**

**6.1** **Fase de Construcción**

**Figura 6-1** **Mapa Isocentración MP** **10** **24 hrs P98 Fase de Construcción**

_Fuente: Elaboración Propia_

**Figura 6-2** **Mapa Isocentración MP** **10** **Anual Fase de Construcción**

_Fuente: Elaboración Propia_

w w w . i g e m a . c l

P á g i n a | 20

_Modelación de Emisiones Atmosféricas, Adenda 2, DIA: “Central BESS Halcón 7”_

**Figura 6-3** **Mapa Isocentración MP** **2,5** **24 hrs P98 Fase de Construcción**

_Fuente: Elaboración Propia_

**Figura 6-4** **Mapa Isocentración MP** **2,5** **Anual Fase de Construcción**

_Fuente: Elaboración Propia_

w w w . i g e m a . c l

P á g i n a | 21

_Modelación de Emisiones Atmosféricas, Adenda 2, DIA: “Central BESS Halcón 7”_

**Figura 6-5** **Mapa isodeposición MPS Anual Fase de Construcción**

_Fuente: Elaboración Propia_

w w w . i g e m a . c l

P á g i n a | 22

_Modelación de Emisiones Atmosféricas, Adenda 2, DIA: “Central BESS Halcón 7”_

**6.2** **Fase de Operación**

**Figura 6-6** **Mapa Isocentración MP10 24 hrs P98 Fase de Operación**

_Fuente: Elaboración Propia_

**Figura 6-7** **Mapa Isocentración MP** **10** **Anual Fase de Operación**

_Fuente: Elaboración Propia_

w w w . i g e m a . c l

P á g i n a | 23

_Modelación de Emisiones Atmosféricas, Adenda 2, DIA: “Central BESS Halcón 7”_

**Figura 6-8** **Mapa Isocentración MP** **2,5** **24 hrs P98 Fase de Operación**

_Fuente: Elaboración Propia_

**Figura 6-9** **Mapa Isocentración MP** **2,5** **Anual Fase de Operación**

_Fuente: Elaboración Propia_

w w w . i g e m a . c l

P á g i n a | 24

_Modelación de Emisiones Atmosféricas, Adenda 2, DIA: “Central BESS Halcón 7”_

**Figura 6-10** **Mapa isodeposición MPS Anual Fase de Operación**

_Fuente: Elaboración Propia_

w w w . i g e m a . c l

P á g i n a | 25

_Modelación de Emisiones Atmosféricas, Adenda 2, DIA: “Central BESS Halcón 7”_

**6.3** **Fase de Cierre**

**Figura 6-11** **Mapa Isocentración MP** **10** **24 hrs P98 Fase de Cierre**

_Fuente: Elaboración Propia_

**Figura 6-12** **Mapa Isocentración MP** **10** **Anual Fase de Cierre**

_Fuente: Elaboración Propia_

w w w . i g e m a . c l

P á g i n a | 26

_Modelación de Emisiones Atmosféricas, Adenda 2, DIA: “Central BESS Halcón 7”_

**Figura 6-13** **Mapa Isocentración MP** **2,5** **24 hrs P98 Fase de Cierre**

_Fuente: Elaboración Propia_

**Figura 6-14** **Mapa Isocentración MP** **2,5** **Anual Fase de Cierre**

_Fuente: Elaboración Propia_

w w w . i g e m a . c l

P á g i n a | 27

_Modelación de Emisiones Atmosféricas, Adenda 2, DIA: “Central BESS Halcón 7”_

**Figura 6-15** **Mapa isodeposición MPS Anual Fase de Cierre**

_Fuente: Elaboración Propia_

w w w . i g e m a . c l

P á g i n a | 28

_Modelación de Emisiones Atmosféricas, Adenda 2, DIA: “Central BESS Halcón 7”_

**7** **Área de Influencia**

El área de influencia corresponde al espacio geográfico cuyos atributos, elementos
naturales o socioculturales deben ser considerados con la finalidad de definir si el proyecto
o actividad genera o presenta alguno de los efectos, características o circunstancias del
artículo 11 de la Ley N° 19.300, o bien para justificar su inexistencia. (Ref. letra a) del
artículo 2 del Reglamento del SEIA).

Dada esta definición, se efectuó una delimitación del área de influencia considerando el
entono de las obras del Proyecto y caminos de acceso no pavimentados, que es donde se
generan las mayores emisiones del Proyecto, incluyendo dentro de este, el punto de
máxima concentración obtenido de la modelación. Es importante destacar que el aporte de
material particulado al ambiente y receptores cercanos, obtenidas de la modelación, no son
significativas respecto de las normas de calidad del aire usadas de referencia, tal como se
presenta en la Sección 9.8 y 9.9 del presente documento.

Por lo expuesto anteriormente, es posible inferir con los resultados de la modelación que el
Proyecto no presenta alguno de los efectos, características o circunstancias del artículo 11
de la Ley N°19.300.

El espacio geográfico se presenta en la Figura 7-1. La superficie del Área de Influencia es
en torno a 1.542 ha.

w w w . i g e m a . c l

P á g i n a | 29

_Modelación de Emisiones Atmosféricas, Adenda 2, DIA: “Central BESS Halcón 7”_

**Figura 7-1** **Área de Influencia de Calidad del Aire**

_Fuente: Elaboración Propia._

w w w . i g e m a . c l

P á g i n a | 30

_Modelación de Emisiones Atmosféricas, Adenda 2, DIA: “Central BESS Halcón 7”_

**8** **Conclusión**

De acuerdo con los resultados de la estimación de emisiones presentada, en la Adenda del
Proyecto en evaluación, se modelaron las fases de construcción, operación y cierre. La fase
del proyecto que generará la mayor cantidad de emisiones atmosféricas corresponde al año
1 de la fase de construcción. Las mayores emisiones de material particulado son producto
del tránsito vehicular, por lo que las emisiones se generaran de forma esporádica y en bajas
cantidades.

Conforme con los valores obtenidos en la modelación, estos se encuentran bajo los valores
establecidos en la normativa de referencia de calidad del aire.

Respecto al aporte de MPS en receptores identificados, no es significativo con respecto a
la norma de Confederación Suiza utilizada como referencia.

Por lo expuesto anteriormente, es posible inferir con los resultados de la modelación que el
Proyecto no presenta alguno de los efectos, características o circunstancias del artículo 11
de la Ley N°19.300.

**9** **Anexos**

**9.1** **Anexo 3.1.1 de la Adenda Complementaria: Archivos de modelación AERMOD**
**(Formato Rar)**

w w w . i g e m a . c l

P á g i n a | 31

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 4-1: ** **Emisiones Central Bess Halcón 7****

| FASE | Emisión, t/año | Col3 | Col4 |
| --- | --- | --- | --- |
| **FASE** | **MP** | **MP10 ** | **MP2,5 ** |
| Construcción (Año 1) | 9,66 | 2,62 | 0,41 |
| Operación | 1,10 | 0,31 | 0,03 |
| Cierre | 4,78 | 1,29 | 0,21 |

**Tabla 5-1: ** **Información de Estación Meteorológica****

| Nombre de la<br>estación | Coordenada UTM WGS 84<br>H 19s (m) | Col3 | Parámetros meteorológicos medidos | Col5 | Col6 | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Nombre**<br>**de**<br>**la**<br>**estación** | **Coordenada UTM WGS 84**<br>**H 19s (m)** | **Coordenada UTM WGS 84**<br>**H 19s (m)** | **HR** | **TA** | **DV** | **VV** | **R ** | **P ** |
| La Violeta Open | E 372271 | N 7952960 | X | X | X | X | X | X |

**Tabla 5-2: ** **Receptores cercanos****

| Receptor | Coordenadas UTM, WGS 84<br>Huso 19 | Col3 | Distancia desde<br>perímetro |
| --- | --- | --- | --- |
| **Receptor** | **X, m** | **Y, m** | **m ** |
| 1 | 367993 | 7954589 | 2.000 |
| 2 | 368758 | 7954166 | 1.630 |
| 3 | 369454 | 7954141 | 1.250 |
| 4 | 369846 | 7953744 | 1.580 |

**Tabla 5-3: ** **Receptores MPS cercanos****

| Receptor | Coordenadas UTM, WGS 84<br>Huso 19 | Col3 | Distancia desde<br>perímetro, |
| --- | --- | --- | --- |
| **Receptor** | **X, m** | **Y, m** | **m ** |
| 1: Pequeños Granjeros | 383374 | 7955176 | 13.366 |
| 2: Asoc Wali Qhantati | 381998 | 7954457 | 12.026 |

**Tabla 5-5: ** **Resultados punto de mayor concentración Fase de Construcción****

| Parámetro | Estadístico | Unidad | Valor<br>modelado | Coordenada UTM, WGS 84, Huso 19 | Col6 |
| --- | --- | --- | --- | --- | --- |
| **Parámetro** | **Estadístico** | **Unidad** | **Valor**<br>**modelado** | **Este** | **Norte** |
| MP10 | 24 horas P98 | μg/m3 | 3,96 | 373147 | 7955050 |
| MP10 | Anual | μg/m3 | 1,74 | 373147 | 7955050 |
| MP2,5 | 24 horas P98 | μg/m3 | 0,4 | 373147 | 7955050 |
| MP2,5 | Anual | μg/m3 | 0,18 | 373147 | 7955050 |
| MPS | Anual | mg/m2 día | 0,86 | 373147 | 7955050 |

**Tabla 5-6: ** **Resultados punto de mayor concentración Fase de Operación****

| Parámetro | Estadístico | Unidad | Valor<br>modelado | Coordenada UTM, WGS 84, Huso 19 | Col6 |
| --- | --- | --- | --- | --- | --- |
| **Parámetro** | **Estadístico** | **Unidad** | **Valor**<br>**modelado** | **Este** | **Norte** |
| MP10 | 24 horas P98 | μg/m3 | 0,57 | 373147 | 7955050 |
| MP10 | Anual | μg/m3 | 0,25 | 373147 | 7955050 |
| MP2,5 | 24 horas P98 | μg/m3 | 0,96 | 373147 | 7955050 |
| MP2,5 | Anual | μg/m3 | 0,03 | 373147 | 7955050 |
| MPS | Anual | mg/m2 día | 0,12 | 373147 | 7955050 |

**Tabla 5-7: ** **Resultados punto de mayor concentración Fase de Cierre****

| Parámetro | Estadístico | Unidad | Valor<br>modelado | Coordenada UTM, WGS 84, Huso 19 | Col6 |
| --- | --- | --- | --- | --- | --- |
| **Parámetro** | **Estadístico** | **Unidad** | **Valor**<br>**modelado** | **Este** | **Norte** |
| MP10 | 24 horas P98 | μg/m3 | 0,06 | 373147 | 7955050 |
| MP10 | Anual | μg/m3 | 0,02 | 373147 | 7955050 |
| MP2,5 | 24 horas P98 | μg/m3 | 0,01 | 373147 | 7955050 |
| MP2,5 | Anual | μg/m3 | 0,01 | 373147 | 7955050 |
| MPS | Anual | mg/m2 día | 0,08 | 373147 | 7955050 |

**Tabla 5-8: ** **Aporte de MP** **10** **y MP** **2,5** **del Proyecto en receptores cercanos Fase de****

| Receptor | Contaminante | Estadístico | Aporte del Proyecto,<br>ug/m3 | Normativa, ug/m3 | Porcentaje<br>respecto a<br>normativa, % |
| --- | --- | --- | --- | --- | --- |
| R1 | MP10 | 24 hrs P98 | 0,29 | 130 | 0,22% |
| R1 | MP10 | Anual | 0,11 | 50 | 0,22% |
| R1 | MP2,5 | 24 hrs P98 | 0,04 | 50 | 0,08% |
| R1 | MP2,5 | Anual | 0,02 | 20 | 0,10% |
| R2 | MP10 | 24 hrs P98 | 0,22 | 130 | 0,17% |
| R2 | MP10 | Anual | 0,11 | 50 | 0,22% |
| R2 | MP2,5 | 24 hrs P98 | 0,03 | 50 | 0,06% |
| R2 | MP2,5 | Anual | 0,01 | 20 | 0,05% |
| R3 | MP10 | 24 hrs P98 | 0,22 | 130 | 0,17% |
| R3 | MP10 | Anual | 0,1 | 50 | 0,20% |
| R3 | MP2,5 | 24 hrs P98 | 0,03 | 50 | 0,06% |
| R3 | MP2,5 | Anual | 0,01 | 20 | 0,05% |
| R4 | MP10 | 24 hrs P98 | 0,28 | 130 | 0,22% |
| R4 | MP10 | Anual | 0,11 | 50 | 0,22% |
| R4 | MP2,5 | 24 hrs P98 | 0,04 | 50 | 0,08% |
| R4 | MP2,5 | Anual | 0,02 | 20 | 0,10% |

**Tabla 5-9: ** **Aporte MPS del Proyecto en receptores cercanos Fase de Construcción****

| Receptor | Contaminante | Estadístico | Aporte del Proyecto,<br>mg/m2 día | Normativa,<br>mg/m2 día | Porcentaje<br>respecto a<br>normativa, % |
| --- | --- | --- | --- | --- | --- |
| R1 MPS | MPS | Anual | 0,02 | 200 | 0,01% |
| R2 MPS | MPS | Anual | 0,01 | 200 | 0,01% |

**Tabla 5-10: ** **Aporte de MP** **10** **y MP** **2,5** **del Proyecto en receptores cercanos Fase de****

| Receptor | Contaminante | Estadístico | Aporte del Proyecto,<br>ug/m3 | Normativa, ug/m3 | Porcentaje<br>respecto a<br>normativa, % |
| --- | --- | --- | --- | --- | --- |
| R1 | MP10 | 24 hrs P98 | 0,04 | 130 | 0,03% |
| R1 | MP10 | Anual | 0,02 | 50 | 0,04% |
| R1 | MP2,5 | 24 hrs P98 | 0,004 | 50 | 0,01% |
| R1 | MP2,5 | Anual | 0,002 | 20 | 0,01% |
| R2 | MP10 | 24 hrs P98 | 0,04 | 130 | 0,03% |
| R2 | MP10 | Anual | 0,01 | 50 | 0,02% |
| R2 | MP2,5 | 24 hrs P98 | 0,003 | 50 | 0,01% |
| R2 | MP2,5 | Anual | 0,001 | 20 | 0,01% |
| R3 | MP10 | 24 hrs P98 | 0,03 | 130 | 0,02% |
| R3 | MP10 | Anual | 0,01 | 50 | 0,02% |
| R3 | MP2,5 | 24 hrs P98 | 0,003 | 50 | 0,01% |
| R3 | MP2,5 | Anual | 0,001 | 20 | 0,01% |
| R4 | MP10 | 24 hrs P98 | 0,02 | 130 | 0,02% |
| R4 | MP10 | Anual | 0,01 | 50 | 0,02% |
| R4 | MP2,5 | 24 hrs P98 | 0,003 | 50 | 0,01% |
| R4 | MP2,5 | Anual | 0,001 | 20 | 0,01% |

**Tabla 5-11: ** **Aporte MPS del Proyecto en receptores cercanos Fase de Operación****

| Receptor | Contaminante | Estadístico | Aporte del Proyecto,<br>mg/m2 día | Normativa,<br>mg/m2 día | Porcentaje<br>respecto a<br>normativa, % |
| --- | --- | --- | --- | --- | --- |
| R1 MPS | MPS | Anual | 0,003 | 200 | 0,002% |
| R2 MPS | MPS | Anual | 0,001 | 200 | 0,001% |

**Tabla 5-12: ** **Aporte de MP10 y MP2,5 del Proyecto en receptores cercanos Fase de Cierre****

| Receptor | Contaminante | Estadístico | Aporte del Proyecto,<br>ug/m3 | Normativa, ug/m3 | Porcentaje<br>respecto a<br>normativa, % |
| --- | --- | --- | --- | --- | --- |
| R1 | MP10 | 24 hrs P98 | 0,001 | 130 | 0,0008% |
| R1 | MP10 | Anual | 0,003 | 50 | 0,0060% |
| R1 | MP2,5 | 24 hrs P98 | 0,0006 | 50 | 0,0012% |
| R1 | MP2,5 | Anual | 0,003 | 20 | 0,0150% |
| R2 | MP10 | 24 hrs P98 | 0,0001 | 130 | 0,0001% |
| R2 | MP10 | Anual | 0,001 | 50 | 0,0020% |
| R2 | MP2,5 | 24 hrs P98 | 0,00004 | 50 | 0,0001% |
| R2 | MP2,5 | Anual | 0,0003 | 20 | 0,0015% |
| R3 | MP10 | 24 hrs P98 | 0,0001 | 130 | 0,0001% |
| R3 | MP10 | Anual | 0,001 | 50 | 0,0020% |
| R3 | MP2,5 | 24 hrs P98 | 0,00003 | 50 | 0,0001% |
| R3 | MP2,5 | Anual | 0,0002 | 20 | 0,0010% |
| R4 | MP10 | 24 hrs P98 | 0,0003 | 130 | 0,0002% |
| R4 | MP10 | Anual | 0,001 | 50 | 0,0020% |
| R4 | MP2,5 | 24 hrs P98 | 0,00007 | 50 | 0,0001% |
| R4 | MP2,5 | Anual | 0,0001 | 20 | 0,0005% |

**Tabla 5-13: ** **Aporte MPS del Proyecto en receptores cercanos Fase de Cierre****

| Receptor | Contaminante | Estadístico | Aporte del Proyecto,<br>mg/m2 día | Normativa,<br>mg/m2 día | Porcentaje<br>respecto a<br>normativa, % |
| --- | --- | --- | --- | --- | --- |
| R1 MPS | MPS | Anual | 0,002 | 200 | 0,001% |
| R2 MPS | MPS | Anual | 0,002 | 200 | 0,001% |
