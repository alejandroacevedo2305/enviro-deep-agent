---
title: Sin título
author: Gómez Rubilar, José
date: D:20240723132647-04'00'
language: es
type: report
pages: 104
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Informe de modelación de la descarga de efluentes asociados a la Piscicultura Aucha en el medio marino.
  - Resumen Ejecutivo
  - Índice
  - Archivos de entrada y salida del modelo
  - Antecedentes
  - Metodología
-->

**INFORME**

# Informe de modelación de la descarga de efluentes asociados a la Piscicultura Aucha en el medio marino.

### _Ampliación piscicultura de recirculación Aucha_

Presentado a:

**INVERMAR S.A.**

Presentado por:

**WSP Chile S.A.**

Av. Juan Soler Manfredini 11, Of. 1701, Puerto Montt, Región de Los Lagos

Marzo 2024

# Resumen Ejecutivo

El presente documento técnico, se centra en el estudio de modelación de la descarga de efluentes en el medio
marino, asociados a la Piscicultura Aucha, ubicada en el sector de Aucha, comuna de Calbuco, provincia de
Llanquihue, Región de Los Lagos. El objetivo del proyecto es ampliar la capacidad de producción de smolts de
especies salmónidos.

El contenido del presente documento comprende lo presentado en la Adenda anterior del Proyecto y lo solicitado
por la autoridad, en cuanto a incorporar el análisis de una condición adicional del mezclado de la descarga en el
medio receptor (modelación de ciclo lunar completo de 30 días). Es así entonces, se complementa con lo
presentado en la Adenda anterior del proyecto radicando principalmente en la incorporación de una simulación de
la descarga para un periodo de tiempo mayor, y no comprende una condición que represente la situación más
desfavorable para el proyecto. Por lo tanto, esta versión del documento incorpora información (modelación de 30
días) e incluye análisis que enriquecen y precisan aspectos técnicos, sin modificar las conclusiones originales del

estudio.

El estudio tiene como objetivo determinar el comportamiento de la pluma de dispersión y el área de influencia en
el medio marino proveniente del efluente proyectado de la proyecto “Ampliación piscicultura de recirculación

Aucha”. Para ello, se consideraron los escenarios de invierno y verano, en condiciones de ciclos mareales en
sicigia y cuadratura, incorporando una condición adicional de modelación de 30 días (ciclo lunar completo).

Para analizar el comportamiento de las plumas de descarga, se utilizó el modelo MOHID, que considera
información de entrada tales como: (1) la hidrodinámica del sector, la cual es influenciada por los vientos, mareas,
corrientes, ríos afluentes, salinidad y temperatura; (2) la composición fisicoquímica del efluente; y (3) la
caracterización del medio receptor. De esta manera, el modelo se robustece con las condiciones particulares de la
zona de descarga en cuanto a comportamiento oceanográfico y calidad de agua.

En lo particular, la modelación realizada considera a: 1) una configuración del modelo, basada en niveles
jerárquicos, la cual precisa la representación del área de descarga de efluentes y la proyección de la descarga, 2)
la utilización de datos de entrada de alta resolución espacio-temporal y representativa del sector modelado, lo que
robustece la modelación de la descarga y mejora la representación del área de la descarga de efluentes, 3) una
modelación combinada de distintos escenarios y condiciones, como invierno/verano, sicigia/cuadratura, las cuales
se enfocaron en obtener y representar el peor escenario posible, 4) información de campo y del sector que
comprende información adicional a la información ya presentada en la DIA; y que corresponde a lo solicitado en
Adenda Complementaria en lo referido a (5) una modelación de ciclo lunar completo de 30 días. Todas estas
consideraciones, aseguran que la modelación hidrodinámica es representativa del sector estudiado, generando
una confiable proyección de la descarga de efluentes en el medio marino.

Es importante destacar que, para respaldar la correcta implementación del modelo, se realizó el proceso de
calibración y validación, en donde las corrientes modeladas por el modelo MOHID, fueron comparadas con las
corrientes registradas en terreno, lo cual se realizó tanto para invierno como para verano. De esta comparación,
se obtuvieron coeficientes de determinación R [2 ] de 0,91 para invierno y 0,89 para verano. Estos resultados dan
cuenta o permiten concluir que el modelo hidrodinámico ha sido validado y representa correctamente la dinámica
del sector estudiado, y, por tanto, permite también representar de manera adecuada los procesos de mezcla y
dispersión del efluente del proyecto en el medio marino receptor.

ii

Marzo 2024

En relación a las condiciones de modelación, es importante destacar que los resultados obtenidos consideran una
condición de máximo caudal y máxima concentración. Esto implica que se ha considerado una carga mayor en
relación con la operación normal del proyecto, ello con el propósito de evaluar la dispersión de la pluma en el medio
marino bajo las condiciones más desfavorables en relación con la descarga del efluente. Esta caracterización
combina las concentraciones más altas obtenidas a partir del cálculo de un balance de masa en un escenario de
máxima emisión de la piscicultura, junto con el caudal máximo posible a descargar (429 [L/s]).

En cuanto a las proyecciones y comportamiento de la descarga en el medio marino y considerando también lo
solicitado por la autoridad, se consideraron modelaciones en el campo cercano y lejano, bajo los escenarios de
invierno y verano, tanto para un período de 30 días (ciclo lunar completo), como para los períodos de sicigia y
cuadratura, los cuales corresponden a los ciclos mareales que mayormente influyen en la dispersión. Estas
modelaciones analizaron los parámetros de nitrógeno total (NT), fósforo total (PT) y DBO 5 . Se obtuvieron áreas de
dispersión en el medio marino para cada parámetro analizado, tanto en invierno como verano, donde se representó
el área en la que cada parámetro del efluente descargado puede mezclarse en el medio marino hasta llegar a
igualarse con las condiciones del medio receptor. Finalmente, el área de influencia de la descarga fue determinado
por la superposición de los resultados de sicigia y cuadratura, los que representan una condición más desfavorable
en términos de dispersión y concentración.

Los resultados obtenidos sobre el comportamiento de la descarga, indicaron que la mayor dilución del vertido
ocurre en el campo cercano, es decir, en las inmediaciones de la descarga. Esto se debe a la implementación de
15 difusores que optimizan la mezcla de manera significativa en el proyecto, los cuales fueron simulados en el
modelo de campo cercano. Los factores determinantes en la dirección de la pluma de dispersión son la velocidad
de salida de la descarga en los difusores, la diferencia de densidad entre el efluente y el medio receptor, los vientos
y la ubicación de los difusores. Una vez emitida la descarga, la pluma de dispersión se dirige verticalmente hacia
la superficie, llegando con concentraciones muy por debajo de las que corresponden a la descarga inicial. Una vez
en la superficie, el viento tiene un impacto importante sobre el área de dispersión ya que modula el desplazamiento
de las aguas en la capa superficial.

Los resultados mostraron que la pluma de dispersión total abarca una superficie máxima de 18,89 [Ha] para
Nitrógeno total y Fósforo Total, y de 19,5 [Ha] para DBO 5 . Al integrar los resultados antes señalados, y
considerando la superposición de las superficies o áreas de dispersión de cada parámetro, se determinó que el
área de influencia de la descarga en el componente de calidad de agua es de 20,20 [Ha] y que el alcance máximo
del área de influencia en la dirección Norte, Este, Sur y Oeste es de 198, 418, 400 y 222 [m], respectivamente. Al
considerar la variabilidad ( x̅ + σ ), en la calidad de agua como valor de referencia del medio marino respecto a los
parámetros analizados, se puede indicar que, para las condiciones modeladas, las plumas de dispersión
disminuyen considerablemente. Teniendo presente lo anterior, se puede indicar que el mayor decaimiento de la
concentración en la distancia, es decir, la mayor dilución, es en menos de 200 metros en dirección Norte, menos
de 50 metros en dirección Este y Oeste, y en menos de 100 metros en la dirección Sur (82 metros).

Finalmente, tras analizar las distintas condiciones modeladas de la descarga en el medio receptor, los resultados
permiten concluir y ratificar que, de las condiciones evaluadas (condición máxima de Sicigia y Cuadratura y
Condición Ciclo lunar completo - 30 días), la condición máxima de Sicigia y Cuadratura presentada en la Adenda
anterior del Proyecto proporciona una peor condición para efectos de evaluar ambientalmente el proyecto.

iii

Marzo 2024

# Índice

**1.0** **INTRODUCCIÓN ........................................................................................................................................... 10**

**2.0** **OBJETIVOS .................................................................................................................................................. 11**

2.1 Objetivos específicos ......................................................................................................................... 11

**3.0** **ANTECEDENTES ......................................................................................................................................... 12**

3.1 Ubicación del proyecto ....................................................................................................................... 12

3.2 Características del emisario submarino ............................................................................................. 13

3.3 Correntometría ................................................................................................................................... 14

3.3.1 Correntometría invierno ................................................................................................................ 14

3.3.2 Correntometría verano .................................................................................................................. 14

3.4 Calidad del efluente proyectado de la Piscicultura Aucha y del cuerpo receptor .............................. 15

3.4.1 Calidad del efluente proyectado ................................................................................................... 15

3.4.2 Calidad de agua del medio receptor ............................................................................................. 15

**4.0** **METODOLOGÍA ........................................................................................................................................... 17**

4.1 Modelo MOHID................................................................................................................................... 17

4.1.1 Información de entrada del modelo .............................................................................................. 17

4.1.1.1 Ríos afluentes ............................................................................................................................ 17

4.1.1.2 Perfiles de salinidad y temperatura ........................................................................................... 18

4.1.1.3 Campo meteorológico de modelo WRF ..................................................................................... 18

4.1.1.4 Modelo global de mareas FES 2014 ......................................................................................... 18

4.1.2 Modelo Hidrodinámico .................................................................................................................. 19

4.1.2.1 Dominio del modelo hidrodinámico ............................................................................................ 19

4.1.2.2 Información batimétrica .............................................................................................................. 20

4.1.2.3 Estructura horizontal y vertical del modelo ................................................................................ 22

4.1.2.4 Condiciones iniciales y de borde ............................................................................................... 23

4.1.2.5 Escenarios Modelados ............................................................................................................... 24

4.1.3 Modelo Lagrangiano ..................................................................................................................... 24

4.1.3.1 Campo cercano .......................................................................................................................... 25

iv

Marzo 2024

4.1.3.2 Campo lejano ............................................................................................................................. 25

4.2 Definición del área de influencia ........................................................................................................ 26

4.2.1 Análisis de los escenarios modelados .......................................................................................... 26

4.2.2 Área de influencia componente calidad de agua .......................................................................... 27

**5.0** **RESULTADOS .............................................................................................................................................. 29**

5.1 Modelo Hidrodinámico ....................................................................................................................... 29

5.1.1 Calibración y validación del modelo Hidrodinámico ..................................................................... 29

5.2 Modelo Lagrangiano .......................................................................................................................... 33

5.2.1 Campo cercano ............................................................................................................................. 33

5.2.2 Campo lejano ................................................................................................................................ 35

5.2.2.1 Invierno ...................................................................................................................................... 35

5.2.2.1.1 Nitrógeno Total (NT) ............................................................................................................... 35

5.2.2.1.2 Fósforo Total (PT) ................................................................................................................... 37

5.2.2.1.3 Demanda Bioquímica de Oxígeno en 5 días (DBO 5 ) ............................................................. 39

5.2.2.2 Verano........................................................................................................................................ 41

5.2.2.2.1 Nitrógeno Total (NT) ............................................................................................................... 41

5.2.2.2.2 Fósforo Total (PT) ................................................................................................................... 43

5.2.2.2.3 Demanda Bioquímica de Oxígeno en 5 días (DBO 5 ) ............................................................. 45

5.3 Definición del Área de influencia ........................................................................................................ 47

5.3.1 Análisis de los escenarios modelados .......................................................................................... 47

5.3.1.1 Nitrógeno Total .......................................................................................................................... 47

5.3.1.2 Fósforo Total .............................................................................................................................. 53

5.3.1.3 Demanda bioquímica de oxígeno a 5 días ................................................................................ 58

5.3.2 Área de influencia componente calidad de agua .......................................................................... 63

**6.0** **DISCUSIÓN ................................................................................................................................................... 64**

**7.0** **CONCLUSIÓN .............................................................................................................................................. 67**

**8.0** **BIBLIOGRAFÍA ............................................................................................................................................. 69**

**9.0** **ANEXOS ....................................................................................................................................................... 71**

v

Marzo 2024

**TABLAS**

Tabla 1: Ubicación del punto de descarga ............................................................................................................. 12

<!-- INICIO TABLA 1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- engorda de la empresa. La ubicación del punto de descarga se encuentra en la Figura 1, mientras que las coordenadas del proyecto y de la descarga se incluyen en la Tabla 1. **Figura 1: Ubicación del punto de descarga de Piscicultura Aucha.** -->

**Tabla 1: Ubicación del punto de descarga de Piscicultura Aucha.****

| Punto | Coordenadas UTM Datum WGS 84 - Huso 18 Sur | Col3 |
| --- | --- | --- |
| **Punto** | **Este** | **Norte** |
| Ubicación del proyecto | 638.629 | 5.374.446 |
| Punto de descarga | 638.436 | 5.374.155 |

<!-- Estadísticas: 3 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- 12 Marzo 2024 -->
<!-- FIN TABLA 1 -->


Tabla 2: Fecha y ubicación del ADCP en invierno ................................................................................................. 14

<!-- INICIO TABLA 2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Para describir las corrientes durante invierno, se analizaron datos de dirección y magnitud registrados por un correntómetro ADCP (Acoustic Doppler Current Profiler) fondeado frente a la zona de descarga cuya posición se presenta en la siguiente tabla: -->

**Tabla 2: Fecha y ubicación del ADCP en invierno****

| Estudios | Periodo de medición | Coordenada UTM | Col4 |
| --- | --- | --- | --- |
| **Estudios** | **Periodo de medición** | **Este** | **Norte** |
| Correntometría euleriana | 23-08-2020 al 22-09-2020 | 638.438 | 5.374.107 |

<!-- Estadísticas: 2 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- **3.3.2** **Correntometría verano** A modo complementario, se realizó una correntometría por medio de un equipo ADCP fondeado frente a la zona de descarga para la estación de verano, donde se analizaron los datos de magnitud y dirección registrados por el -->
<!-- FIN TABLA 2 -->


Tabla 3: Fecha y ubicación del ADCP en verano ................................................................................................... 14

<!-- INICIO TABLA 3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- A modo complementario, se realizó una correntometría por medio de un equipo ADCP fondeado frente a la zona de descarga para la estación de verano, donde se analizaron los datos de magnitud y dirección registrados por el equipo. La ubicación donde fue fondeado el equipo se presenta en la Tabla 3 a continuación. -->

**Tabla 3: Fecha y ubicación del ADCP en verano****

| Estudios | Periodo de medición | Coordenada UTM | Col4 |
| --- | --- | --- | --- |
| **Estudios** | **Periodo de medición** | **Este** | **Norte** |
| Correntometría euleriana | 04-03-2021 al 05-04-2021 | 638.480 | 5.374.082 |

<!-- Estadísticas: 2 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- 14 Marzo 2024 -->
<!-- FIN TABLA 3 -->


Tabla 4: Calidad (concentración) de la descarga ................................................................................................... 15

<!-- INICIO TABLA 4 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- orgánicos e inorgánicos. Para evaluar la calidad de la descarga se realizó un balance de masa considerando el escenario más desfavorable, que representa la mayor emisión de la piscicultura. A continuación, en la Tabla 4 se señala la calidad (concentración) de la descarga: -->

**Tabla 4: Calidad (concentración) de la descarga.****

| Componente (Parámetro) | Descarga [mg/L] |
| --- | --- |
| Nitrógeno Total | 5,4 |
| Fósforo Total | 0,9 |
| DBO5 | 10,7 |

<!-- Estadísticas: 3 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Respecto al caudal, para la modelación se consideró un caudal máximo de descargar de 429 [L/s]. Es muy importante señalar que se modela un escenario hipotético y desfavorable ya que, se utiliza las máximas concentraciones del efluente (Tabla 4) con el máximo caudal a descargar (429 [L/s]). -->
<!-- FIN TABLA 4 -->


Tabla 5: Valor referencial del cuerpo receptor ....................................................................................................... 16

<!-- INICIO TABLA 5 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- La siguiente tabla presenta los valores referenciales de las concentraciones del cuerpo receptor que fueron considerados en la modelación. -->

**Tabla 5: Valores referenciales de las concentraciones del cuerpo receptor****

| Parámetro | Valor referencial del medio marino[mg/L] | Col3 |
| --- | --- | --- |
| **Parámetro** | **Invierno** | **Verano** |
| Nitrógeno Total | 1,4 | 1,2 |
| Fósforo Total | 0,07 | 0,12 |
| DBO5 | 2,0 | 4,4 |

<!-- Estadísticas: 4 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Los resultados del monitoreo realizado en invierno y verano presentan una variabilidad en ambas estacionalidades. A continuación, se presenta la desviación estándar como una medida de dispersión y de variabilidad de los datos en el cuerpo de agua marino respecto que presentan ambos monitoreos. -->
<!-- FIN TABLA 5 -->


Tabla 6: Desviación estándar respecto al monitoreo en el cuerpo de agua marino para invierno y verano ......... 16

<!-- INICIO TABLA 6 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Los resultados del monitoreo realizado en invierno y verano presentan una variabilidad en ambas estacionalidades. A continuación, se presenta la desviación estándar como una medida de dispersión y de variabilidad de los datos en el cuerpo de agua marino respecto que presentan ambos monitoreos. -->

**Tabla 6: Desviación estándar respecto al monitoreo en el cuerpo de agua marino para invierno y verano****

| Parámetro | Desviación Estándar de ambos monitoreos[mg/L] | Col3 |
| --- | --- | --- |
| **Parámetro** | **Invierno** | **Verano** |
| Nitrógeno Total | 0,98 | 0,21 |
| Fósforo Total | 0,03 | 0,15 |
| DBO5 | 01 | 0,6 |

<!-- Estadísticas: 4 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- 1 Para tener en cuenta la incertidumbre en relación con los valores muestreados, se ha considerado una variabilidad del 10% del promedio en los resultados que se presentarán a continuación en las curvas de decaimiento. 16 -->
<!-- FIN TABLA 6 -->


Tabla 7: Parámetros de las grillas computacionales. ............................................................................................. 20

<!-- INICIO TABLA 7 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- 19 Marzo 2024 -->

**Tabla 7: Parámetros de las grillas computacionales.****

| Parámetro | Grilla 1er nivel | Grilla 2do Nivel | Grilla 3er nivel |
| --- | --- | --- | --- |
| Resolución XY | 320 metros | 106,67 metros | 21,33 metros |
| Tamaño de la grilla en Δx | 0,00385 | 0,001281 | 0,00026 |
| Tamaño de la grilla en Δy | 0,00288 | 0,00096 | 0,00019 |
| Espaciamiento temporal<br>de calculo | 10 segundos | 4 segundos | 2 segundos |
| Origen Este | 557.556,77 | 622.932,09 | 637.129,69 |
| Origen Norte | 5.349.841,29 | 5.350.929,14 | 5.372.873,30 |
| N° Capas verticales | 5 | 10 | 20 |

<!-- Estadísticas: 7 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- _**4.1.2.2**_ _**Información batimétrica**_ El módulo encargado de la batimetría en el modelo MOHID realiza la descripción de las profundidades del medio acuático a simular, calculando las áreas y los volúmenes finitos, basados en la elevación de la superficie y los -->
<!-- FIN TABLA 7 -->


Tabla 8: Índices de correlación invierno ................................................................................................................. 29

<!-- INICIO TABLA 8 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- En ellas se encontró que los promedios y desviaciones estándar de las series de tiempo de corrientes obtenidas del modelo hidrodinámico representan de manera general las condiciones del sector. En la tabla a continuación se presentan los índices estadísticos antes mencionados tanto para invierno como para verano. -->

**Tabla 8: Índices de correlación invierno****

| Invierno | Col2 | Col3 |
| --- | --- | --- |
| índice | ADCP | Modelo |
| Promedio | 8,84 [cm/s] | 5,64 [cm/s] |
| D. estándar | 5,51 [cm/s] | 3,97 [cm/s] |
| Coef. Regresión | 0,64 | 0,64 |
| Coef. R^2 | 0,92 | 0,92 |
| BIAS | -3,20 [cm/s] | -3,20 [cm/s] |
| MAE | 5,06 [cm/s] | 5,06 [cm/s] |
| RMSE | 6,43 [cm/s] | 6,43 [cm/s] |

<!-- Estadísticas: 8 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Marzo 2024 **Tabla 9: Índices de correlación verano** -->
<!-- FIN TABLA 8 -->


Tabla 9: Índices de correlación verano ................................................................................................................... 30

<!-- INICIO TABLA 9 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |MAE|5,06 [cm/s]|5,06 [cm/s]| |RMSE|6,43 [cm/s]|6,43 [cm/s]| Marzo 2024 -->

**Tabla 9: Índices de correlación verano****

| Verano | Col2 | Col3 |
| --- | --- | --- |
| Índice | ADCP | Modelo |
| Promedio | 11,13 [cm/s] | 4,22 [cm/s] |
| D. estándar | 9,75 [cm/s] | 2,53 [cm/s] |
| Coef. Regresión | 0,23 | 0,23 |
| Coef. R^2 | 0,90 | 0,90 |
| BIAS | -6,92 [cm/s] | -6,92 [cm/s] |
| MAE | 7,97 [cm/s] | 7,97 [cm/s] |
| RMSE | 12,40 [cm/s] | 12,40 [cm/s] |

<!-- Estadísticas: 8 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- De acuerdo con los análisis antes presentados, es posible observar que las corrientes de invierno son mejor representadas que las corrientes de verano. Aun así, las series de tiempo de corrientes registradas por los ADCP y el modelo hidrodinámico son similares entre sí. En cuanto al índice BIAS para invierno este fue de -3,2 [cm/s] y para verano de -6,92 [cm/s], lo que indica una subestimación de las velocidades de las corrientes por parte del -->
<!-- FIN TABLA 9 -->


Tabla 10: Comparación entre concentración de descarga y concentración final en el campo cercano ................ 33

<!-- INICIO TABLA 10 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- más significativas. En la tabla a continuación se presenta una comparación de la concentración de la descarga respecto a la menor dilución en el campo cercano. -->

**Tabla 10: Comparación entre concentración de descarga y concentración final en el campo cercano****

| Parámetro | NT [mg/L] | PT [mg/L] | DBO [mg/L]<br>5 |
| --- | --- | --- | --- |
| Concentración de descarga | 5,4 | 0,9 | 10,7 |
| Concentración final campo cercano | 1,8 | 0,22 | 5,2 |
| Disminución de concentración mínima | 67,2% | 75,6% | 51,4% |

<!-- Estadísticas: 3 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Como representación de esto, se obtuvieron resultados gráficos de las plumas de dispersión y dilución en el campo cercano para los parámetros NT, PT y DBO 5 evaluados (Figura 18 a) y b), Figura 19 c)), además de la pluma general (Figura 19 d)), donde se puede apreciar la nube de partículas que emite el difusor del modelo lagrangiano. -->
<!-- FIN TABLA 10 -->


Tabla 11: Concentraciones iniciales del campo lejano en invierno para NT .......................................................... 35

<!-- INICIO TABLA 11 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- densidad entre el efluente, provocan que la pluma de dispersión se dirija hacia la superficie con bajas concentraciones. Para el caso del nitrógeno total, a continuación, se presentan las concentraciones con las que llega a superficie para el periodo de invierno; las que son llamadas también, concentraciones en superficie en el inicio del campo lejano. -->

**Tabla 11: Concentraciones iniciales del campo lejano en invierno para NT****

| Escenario | Descarga [mg/L] | Concentración inicial en el<br>campo lejano [mg/L] |
| --- | --- | --- |
| Modelación 30 días | 5,4 | 1,60 |
| Sicigia | Sicigia | 1,60 |
| Cuadratura | Cuadratura | 1,77 |

<!-- Estadísticas: 3 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- **Modelación** **ciclo** **lunar** **completo (30 días)** En la figura a continuación se presenta la pluma de dispersión del efluente en conjunto con las isolíneas de concentración considerando el parámetro Nitrógeno Total (NT) para 30 días continuos de modelación, cuya área -->
<!-- FIN TABLA 11 -->


Tabla 12: Concentraciones iniciales del campo lejano en invierno para PT .......................................................... 37

<!-- INICIO TABLA 12 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **5.2.2.1.2** **Fósforo Total (PT)** Para el caso del Fósforo Total, las concentraciones a la que llegan a superficie, o bien, las concentraciones iniciales en el campo lejano son las siguientes: -->

**Tabla 12: Concentraciones iniciales del campo lejano en invierno para PT****

| Escenario | Descarga [mg/L] | Concentración inicial en el campo<br>lejano [mg/L] |
| --- | --- | --- |
| Modelación 30 días | 0,9 | 0,091 |
| Sicigia | Sicigia | 0,093 |
| Cuadratura | Cuadratura | 0,096 |

<!-- Estadísticas: 3 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- **Modelación ciclo lunar completo (30 días)** En la figura a continuación se presenta la pluma de dispersión del efluente en conjunto con las isolíneas de concentración considerando el parámetro Fósforo Total (PT) para la modelación de ciclo lunar completo, cuya área -->
<!-- FIN TABLA 12 -->


Tabla 13: Concentraciones iniciales del campo lejano en invierno para DBO 5 ..................................................... 39

<!-- INICIO TABLA 13 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **5.2.2.1.3** **Demanda Bioquímica de Oxígeno en 5 días (DBO** **5** **)** Para el caso de la DBO 5, las concentraciones a las que llegan a superficie, o bien, las concentraciones iniciales en el campo lejano son las siguientes: -->

**Tabla 13: Concentraciones iniciales del campo lejano en invierno para DBO** **5****

| Escenario | Descarga [mg/L] | Concentración inicial en el<br>campo lejano [mg/L] |
| --- | --- | --- |
| Modelación 30 días | 10,7 | 2,39 |
| Sicigia | Sicigia | 2,41 |
| Cuadratura | Cuadratura | 2,56 |

<!-- Estadísticas: 3 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- **Modelación** **ciclo** **lunar** **completo (30 días)** En la figura a continuación se presenta la pluma de dispersión del efluente en conjunto con las isolíneas de concentración considerando el parámetro DBO 5 para la modelación de ciclo lunar completo, cuya área es de -->
<!-- FIN TABLA 13 -->


Tabla 14: Concentraciones iniciales del campo lejano en verano para NT ........................................................... 41

<!-- INICIO TABLA 14 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **5.2.2.2.1** **Nitrógeno Total (NT)** A continuación, se presentan las concentraciones de Nitrógeno Total (NT) en superficie en el inicio del campo lejano, para el período de verano. -->

**Tabla 14: Concentraciones iniciales del campo lejano en verano para NT****

| Escenario | Descarga [mg/L] | Concentración inicial en el<br>campo lejano [mg/L] |
| --- | --- | --- |
| Modelación 30 días | 5,4 | 1,36 |
| Sicigia | Sicigia | 1,90 |
| Cuadratura | Cuadratura | 1,55 |

<!-- Estadísticas: 3 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- **Modelación ciclo lunar completo (30 días)** En la figura a continuación se presenta la pluma de dispersión del efluente en conjunto con las isolíneas de concentración considerando el parámetro Nitrógeno Total (NT) para 30 días de modelación, cuya área es de -->
<!-- FIN TABLA 14 -->


Tabla 15: Concentraciones iniciales del campo lejano en verano para PT ........................................................... 43

<!-- INICIO TABLA 15 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **5.2.2.2.2** **Fósforo Total (PT)** Para el caso del Fósforo Total, las concentraciones a la que llegan a superficie, o bien, las concentraciones iniciales en el campo lejano son las siguientes: -->

**Tabla 15: Concentraciones iniciales del campo lejano en verano para PT****

| Escenario | Descarga [mg/L] | Concentración inicial en el<br>campo lejano [mg/L] |
| --- | --- | --- |
| Modelación 30 días | 0,9 | 0,14 |
| Sicigia | Sicigia | 0,20 |
| Cuadratura | Cuadratura | 0,16 |

<!-- Estadísticas: 3 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- **Modelación ciclo lunar completo (30 días)** En la figura a continuación se presenta la pluma de dispersión del efluente en conjunto con las isolíneas de concentración considerando el parámetro Fósforo Total (PT) para 30 días de modelación, cuya área corresponde -->
<!-- FIN TABLA 15 -->


Tabla 16: Concentraciones iniciales del campo lejano en verano para DBO 5 ....................................................... 45

<!-- INICIO TABLA 16 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **5.2.2.2.3** **Demanda Bioquímica de Oxígeno en 5 días (DBO** **5** **)** Para el caso de la DBO 5, las concentraciones a las que llegan a superficie, o bien, las concentraciones iniciales en el campo lejano son las siguientes: -->

**Tabla 16: Concentraciones iniciales del campo lejano en verano para DBO** **5****

| Escenario | Descarga [mg/L] | Concentración inicial en el<br>campo lejano [mg/L] |
| --- | --- | --- |
| Modelación 30 días | 10,7 | 4,85 |
| Sicigia | Sicigia | 6,57 |
| Cuadratura | Cuadratura | 5,40 |

<!-- Estadísticas: 3 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- **Modelación ciclo lunar completo (30 días)** En la figura a continuación se presenta la pluma de dispersión del efluente en conjunto con las isolíneas de concentración considerando el parámetro DBO 5 (PT) para 30 días de modelación. Cuya área de dispersión -->
<!-- FIN TABLA 16 -->


Tabla 17: Concentraciones iniciales del campo lejano en superficie para NT invierno y verano .......................... 47

<!-- INICIO TABLA 17 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- _**5.3.1.1**_ **Nitrógeno Total** A continuación, se presentan las concentraciones de nitrógeno total que llegan a la superficie, superpuestas para las máximas concentraciones y dispersión entre a) invierno y b) verano; en sicigia y cuadratura. -->

**Tabla 17: Concentraciones iniciales del campo lejano en superficie para NT invierno y verano****

| Estacionalidad | Concentración inicial en el campo lejano [mg/L] |
| --- | --- |
| Invierno | 1,77 |
| Verano | 1,90 |

<!-- Estadísticas: 2 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Las áreas de la pluma de dispersión para cada estación (invierno y verano) superpuestas de sicigia y cuadratura, se presentan a continuación. Se incluye además en las figuras las proyecciones desde el punto de descarga que fueron consideradas para obtener las curvas de decaimiento (norte, sur, este, oeste). -->
<!-- FIN TABLA 17 -->


Tabla 18: Áreas de plumas de dispersión del parámetro NT ................................................................................. 49

<!-- INICIO TABLA 18 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **Figura 40: Área de dispersión total (sicigia y cuadratura en verano e invierno) de NT** En la siguiente tabla se presenta el valor de las áreas de dispersión de sicigia-cuadratura superpuestas para los escenarios de invierno y verano, y el total de ambos escenarios. -->

**Tabla 18: Áreas de plumas de dispersión del parámetro NT****

| Escenario | Área [m2] |
| --- | --- |
| Área de pluma de dispersión en invierno | 158.218 |
| Área de pluma de dispersión en verano | 139.481 |
| Área de la pluma de dispersión superpuesta total | 188.946 |

<!-- Estadísticas: 3 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- A continuación, se presentan los resultados que muestran las distancias que alcanza la pluma de dispersión y su decaimiento a lo largo del recorrido en las cuatro direcciones presentadas (N, E, S y W). La Tabla 19 incluye dos alcances como se mencionó anteriormente: (a) la distancia máxima que iguala la pluma de dispersión hasta igualar la concentración del medio receptor considerando la variabilidad de los datos del medio (+σ); y b) la distancia -->
<!-- FIN TABLA 18 -->


Tabla 19: Distancias de igualación condición máxima sicigia-cuadratura para invierno y verano ........................ 50

<!-- INICIO TABLA 19 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- 49 Marzo 2024 -->

**Tabla 19: Distancias de igualación condición máxima sicigia-cuadratura para invierno y verano****

| NT | Invierno | Col3 | Verano | Col5 |
| --- | --- | --- | --- | --- |
| Dirección | Distancia que<br>alcanza la pluma de<br>dispersión hasta el<br>valor del medio + σ<br>(variabilidad del<br>medio receptor) [m] | Distancia que alcanza<br>la pluma de dispersión<br>hasta el valor del<br>medio [m] | Distancia que<br>alcanza la pluma de<br>dispersión hasta el<br>valor del medio + σ<br>(variabilidad del<br>medio receptor) [m] | Distancia que alcanza<br>la pluma de dispersión<br>hasta el valor del<br>medio [m] |
| Norte | 0 <br>(Se encuentra dentro<br>de la variabilidad del<br>medio marino) | 195 | 165 | 208 |
| Este | Este | 417 | 27 | 418 |
| Sur | Sur | 301 | 23 | 207 |
| Oeste | Oeste | 82 | 36 | 258 |

<!-- Estadísticas: 5 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- A continuación, en las Figura 41 y Figura 42 se presentan las curvas de decaimiento de los escenarios de invierno y verano para las condiciones máximas superpuestas de sicigia y cuadratura, en conjunto con el escenario de 30 días, de tal manera de comparar visualmente las diferencias de concentraciones. A simple vista es posible apreciar que en el escenario de invierno ambas curvas ya se encuentran dentro de la desviación estándar de las -->
<!-- FIN TABLA 19 -->


Tabla 20: Concentraciones iniciales del campo lejano en superficie para PT invierno y verano .......................... 53

<!-- INICIO TABLA 20 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- _**5.3.1.2**_ _**Fósforo Total**_ Para el caso del Fósforo Total, las concentraciones a la que llegan a superficie, o bien, las concentraciones iniciales en el campo lejano tanto para sicigia como para cuadratura son las siguientes: -->

**Tabla 20: Concentraciones iniciales del campo lejano en superficie para PT invierno y verano****

| Estacionalidad | Concentración inicial en el campo lejano [mg/L] |
| --- | --- |
| Invierno | 0,1 |
| Verano | 0,2 |

<!-- Estadísticas: 2 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- En relación con las áreas de la pluma de dispersión en invierno y verano, a continuación, se presentan las figuras para cada uno de los escenarios superpuestos en sicigia y cuadratura. Se incluyen las proyecciones desde el punto de descarga que fueron consideradas para obtener las curvas de decaimiento (norte, sur, este, oeste). -->
<!-- FIN TABLA 20 -->


Tabla 21: Áreas de plumas de dispersión del parámetro PT ................................................................................. 55

<!-- INICIO TABLA 21 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Marzo 2024 En la siguiente tabla se detallas las áreas de dispersión para las condiciones evaluadas, sicigia más cuadratura, superpuestas para los escenarios de invierno y verano. -->

**Tabla 21: Áreas de plumas de dispersión del parámetro PT****

| Escenario | Área [m2] |
| --- | --- |
| Área de pluma de dispersión en invierno | 158.717 |
| Área de pluma de dispersión en verano | 129.469 |
| Área de la pluma de dispersión superpuesta total | 188.965 |

<!-- Estadísticas: 3 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- A continuación, la Tabla 22 presenta los resultados de las distancias de cada escenario para la condición superpuesta: -->
<!-- FIN TABLA 21 -->


Tabla 22: Distancia en metros a las que las concentraciones de PT igualan el valor del medio receptor

<!-- INICIO TABLA 22 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- A continuación, la Tabla 22 presenta los resultados de las distancias de cada escenario para la condición superpuesta: -->

**Tabla 22: Distancia en metros a las que las concentraciones de PT igualan el valor del medio receptor****

| PT | Invierno | Col3 | Verano | Col5 |
| --- | --- | --- | --- | --- |
| Dirección | Distancia que<br>alcanza la pluma de<br>dispersión hasta el<br>valor del medio + σ<br>(variabilidad del<br>medio receptor) [m] | Distancia que alcanza<br>la pluma de dispersión<br>hasta el valor del<br>medio [m] | Distancia que<br>alcanza la pluma de<br>dispersión hasta el<br>valor del medio + σ<br>(variabilidad del<br>medio receptor) [m] | Distancia que alcanza<br>la pluma de dispersión<br>hasta el valor del<br>medio [m] |
| Norte | 13 | 198 | 0 <br>(Se encuentra dentro<br>de la variabilidad del<br>medio marino) | 198 |
| Este | 20 | 418 | 418 | 418 |
| Sur | 0 <br>(Se encuentra dentro<br>de la variabilidad del<br>medio marino) | 400 | 400 | 196 |
| Oeste | Oeste | 40 | 40 | 215 |

<!-- Estadísticas: 5 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- A continuación, se presentan las distintas curvas de decaimiento para invierno y verano a lo largo de las direcciones antes mencionadas. En invierno se aprecia que las concentraciones en el comienzo del campo lejano se encuentran dentro de los valores del medio, sin embargo, en el escenario máximo superpuesto al alejarse de este punto (aproximadamente 25 m) para la dirección E y S las concentraciones tienden a aumentar levemente, para -->
<!-- FIN TABLA 22 -->


medidos desde el punto de descarga para (invierno y verano) .............................................................. 55

Tabla 23: Concentraciones iniciales del campo lejano en superficie para DBO 5 . ................................................. 58

<!-- INICIO TABLA 23 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- _**5.3.1.3**_ _**Demanda bioquímica de oxígeno a 5 días**_ Para el caso de la DBO 5, las concentraciones a la que llegan a superficie, o bien, las concentraciones iniciales en el campo lejano son las siguientes: -->

**Tabla 23: Concentraciones iniciales del campo lejano en superficie para DBO** **5** **.****

| Estacionalidad | Concentración inicial en el campo lejano [mg/L] |
| --- | --- |
| Invierno | 2,56 |
| Verano | 6,58 |

<!-- Estadísticas: 2 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- En la Figura 48 y Figura 49 se presentan las áreas de dispersión de los escenarios invierno y verano con las condiciones sicigia y cuadratura superpuestas. **Figura 48: Pluma de dispersión para DBO** **5** **en invierno considerando sicigia y cuadratura.** -->
<!-- FIN TABLA 23 -->


Tabla 24: Áreas de plumas de dispersión del parámetro DBO 5 ............................................................................. 60

<!-- INICIO TABLA 24 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- 59 Marzo 2024 -->

**Tabla 24: Áreas de plumas de dispersión del parámetro DBO** **5****

| Escenario | Área [m2] |
| --- | --- |
| Área de pluma de dispersión en invierno | 172.623 |
| Área de pluma de dispersión en verano | 132.470 |
| Área de la pluma de dispersión superpuesta total | 195.144 |

<!-- Estadísticas: 3 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- A continuación, la Tabla 25 presenta los resultados de las distancias de cada escenario para la condición superpuesta: -->
<!-- FIN TABLA 24 -->


Tabla 25: Distancia en metros a las que las concentraciones de DBO 5 igualan el valor del medio receptor

<!-- INICIO TABLA 25 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- A continuación, la Tabla 25 presenta los resultados de las distancias de cada escenario para la condición superpuesta: -->

**Tabla 25: Distancia en metros a las que las concentraciones de DBO** **5** **igualan el valor del medio receptor****

| DBO<br>5 | Invierno | Col3 | Verano | Col5 |
| --- | --- | --- | --- | --- |
| Dirección | Distancia que<br>alcanza la pluma de<br>dispersión hasta el<br>valor del medio + σ<br>(variabilidad del<br>medio receptor) [m] | Distancia que alcanza<br>la pluma de dispersión<br>hasta el valor del<br>medio [m] | Distancia que<br>alcanza la pluma de<br>dispersión hasta el<br>valor del medio + σ<br>(variabilidad del<br>medio receptor) [m] | Distancia que alcanza<br>la pluma de dispersión<br>hasta el valor del<br>medio [m] |
| Norte | 75 | 198 | 178 | 198 |
| Este | 28 | 418 | 28 | 418 |
| Sur | 82 | 400 | 24 | 196 |
| Oeste | 19 | 43 | 44 | 222 |

<!-- Estadísticas: 5 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- A continuación, se presentan las distintas curvas de decaimientos para invierno y verano, a lo largo de las direcciones antes mencionadas. En ellas se puede observar la notable variación de las concentraciones al comienzo del campo lejano en la superposición máxima de sicigia y cuadratura respecto a la de 30 días, donde ocurre algo similar a la modelación de NT, incrementando relevantemente en el escenario de verano en todas las -->
<!-- FIN TABLA 25 -->


medidos desde el punto de descarga para (invierno y verano) .............................................................. 60

Tabla 26: Máximos alcances del área de influencia de la descarga en el cuerpo de agua marino ....................... 63

<!-- INICIO TABLA 26 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **Figura 53: Área de influencia de la descarga en el cuerpo de agua marino** A continuación, se presentan los máximos alcances que presenta el área de influencia. -->

**Tabla 26: Máximos alcances del área de influencia de la descarga en el cuerpo de agua marino****

| Dirección | Distancia máxima del área de influencia [m] |
| --- | --- |
| Norte | 198 |
| Este | 418 |
| Sur | 400 |
| Oeste | 222 |

<!-- Estadísticas: 4 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Marzo 2024 ### 6.0 DISCUSIÓN -->
<!-- FIN TABLA 26 -->


Tabla 27: Caudales medios estimados de los afluentes principales. ..................................................................... 76

<!-- INICIO TABLA 27 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- La tabla siguiente presenta los caudales medios mensuales para cada uno de los ríos. Marzo 2024 -->

**Tabla 27: Caudales medios estimados de los afluentes principales.****

| Caudales (m3/s) | Col2 | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Río/Mes** | **Ene** | **Feb** | **Mar** | **Abr** | **May** | **Jun** | **Jul** | **Ago** | **Sep** | **Oct** | **Nov** | **Dic** |
| Ancud | 23,8 | 19,6 | 25,4 | 48,2 | 104,2 | 139,9 | 140,9 | 134,6 | 94,2 | 62,2 | 45,7 | 32,7 |
| Maullin | 99,9 | 86,2 | 81,1 | 99,9 | 154,0 | 205,3 | 225,3 | 230,4 | 201,3 | 168,6 | 145,7 | 122,8 |
| Chamiza | 43,5 | 39,8 | 45,7 | 71,7 | 113,9 | 139,9 | 132,3 | 128,7 | 101,4 | 81,6 | 69,7 | 59,5 |
| Chaica | 4,0 | 3,8 | 4,4 | 6,6 | 9,9 | 12,2 | 11,5 | 11,3 | 8,6 | 6,9 | 6,0 | 5,1 |
| Lenca | 6,2 | 5,7 | 6,6 | 10,2 | 15,9 | 18,7 | 17,3 | 17,3 | 14,2 | 12,1 | 10,2 | 8,4 |
| Puelo | 480,4 | 332,7 | 287,6 | 427,7 | 753,8 | 948,2 | 937,3 | 954,2 | 901,1 | 848,7 | 810,5 | 674,9 |
| Cochamo | 20,3 | 15,2 | 15,5 | 24,2 | 40,6 | 49,9 | 46,9 | 46,2 | 39,8 | 33,4 | 31,7 | 29,3 |
| Petrohué | 177,5 | 142,8 | 140,6 | 215,4 | 369,2 | 473,7 | 442,3 | 438,3 | 376,0 | 307,5 | 272,5 | 244,1 |
| Aucha | 0,2 | 0,2 | 0,3 | 0,5 | 0,9 | 1,3 | 1,1 | 1,1 | 1,5 | 0,5 | 0,4 | 0,4 |
| R2 | 0,1 | 0,1 | 0,1 | 0,2 | 0,4 | 0,5 | 0,5 | 0,5 | 0,6 | 0,2 | 0,2 | 0,2 |
| Estero Codihue | 0,1 | 0,1 | 0,1 | 0,1 | 0,2 | 0,4 | 0,3 | 0,3 | 0,4 | 0,1 | 0,1 | 0,1 |

<!-- Estadísticas: 12 filas, 13 columnas -->
<!-- Contexto posterior: -->
<!-- ### Perfiles de salinidad y temperatura utilizados en la modelación. Para la modelación hidrodinámica, se utilizaron los perfiles promedio de salinidad y temperatura como condición de borde inicial tanto en el borde inferior (sur) como en el borde izquierdo (oeste) en el dominio de nivel 1 del -->
<!-- FIN TABLA 27 -->


Tabla 28: Coordenada de vértices del domino del modelo WRF utilizado. ........................................................... 81

<!-- INICIO TABLA 28 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- las condiciones de borde de los modelos de cajas se obtienen a partir del modelo jerárquico superior. La fecha de la data ocupada para el modelo fue del 01/08/2020 al 30/09/2020 para el escenario de invierno, y 01/03/2021 al 01/04/2021 para el escenario de verano. -->

**Tabla 28: Coordenada de vértices del domino del modelo WRF utilizado.****

| Vértices del<br>dominio | Coordenadas de los vértices del dominio WRF (DATUM WGS - 84, HUSO 18S) | Col3 | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Vértices del**<br>**dominio** | Latitud (S) | Longitud (W) | UTM Este (m) | UTM Norte (m) |
| A | 42° 00' 31,98” | 73° 38' 12,52” | 612.881,58 | 5.348.338,62 |
| B | 41° 33' 27,79” | 73° 38' 12,52” | 664.264,35 | 5.348.338,62 |
| C | 41° 33' 27,79” | 73° 01' 48,66” | 664.264,35 | 5.397.454,16 |
| D | 42° 00' 31,98” | 73° 01' 48,66” | 612.881,58 | 5.397.454,16 |

<!-- Estadísticas: 5 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- **Figura 59: Instante de muestra del modelo WRF con magnitudes de vientos utilizados en la modelación** **en Nivel 2 y 3.** -->
<!-- FIN TABLA 28 -->


Tabla 29: Correntometría euleriana invierno .......................................................................................................... 82

<!-- INICIO TABLA 29 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Para caracterizar las corrientes del sitio, se analizaron datos de dirección y magnitud registrados por un correntómetro ADCP (Acoustic Doppler Current Profiler) fondeado frente a la zona de descarga cuya posición se presenta en la siguiente tabla: -->

**Tabla 29: Correntometría euleriana invierno****

| Estudios | Periodo de medición | Coordenada UTM | Col4 |
| --- | --- | --- | --- |
| **Estudios** | **Periodo de medición** | Este | Norte |
| Correntometría euleriana | 23-08-2020 al 22-09-2020 | 638.438 | 5.374.107 |

<!-- Estadísticas: 2 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- El análisis de datos se efectuó en base a estadística básica y distribución de frecuencia de la magnitud y la dirección de la corriente, para tres capas representativas de la columna de agua (superficie, medio y fondo). Además, se elaboraron histogramas y rosas de direcciones correspondientes a la dirección y magnitud de la corriente para cada una de las capas analizadas. -->
<!-- FIN TABLA 29 -->


Tabla 30: Incidencia Magnitud y dirección capa superficial invierno. .................................................................... 83

<!-- INICIO TABLA 30 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Para la capa superficial se utilizó la capa de los 10 metros desde el fondo. Se utiliza esta capa como superficial debido a que representa esta sección de la columna de agua sin efectos de la marea. De acuerdo con los resultados del registro de velocidad, los mayores porcentajes de ocurrencia ocurrieron entre los rangos 5-10 y 10-15 con 36,9% y 23,4% respectivamente. (Tabla 30, Figura 61). -->

**Tabla 30: Incidencia Magnitud y dirección capa superficial invierno.****

| Magnitud (cm/s) | Dirección (°) | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Total | Frec.<br>Absoluta |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Magnitud (cm/s)** | N | NE | E | SE | S | SW | W | NW | NW | NW |
| Calmas | 178 | 4 | 5 | 4 | 5 | 2 | 5 | 4 | 207 | 4,8% |
| 1-5 | 93 | 97 | 108 | 108 | 123 | 83 | 91 | 92 | 795 | 18,4% |
| 5-10 | 192 | 221 | 237 | 205 | 209 | 206 | 167 | 158 | 1595 | 36,9% |
| 10-15 | 84 | 178 | 194 | 123 | 116 | 138 | 103 | 73 | 1009 | 23,4% |
| 15-20 | 26 | 70 | 102 | 41 | 39 | 46 | 45 | 19 | 388 | 9,0% |
| 20-25 | 4 | 29 | 51 | 22 | 14 | 21 | 15 | 8 | 164 | 3,8% |
| 25-30 | 6 | 9 | 16 | 7 | 13 | 10 | 4 | 3 | 68 | 1,6% |
| >30 | 6 | 6 | 45 | 12 | 11 | 7 | 2 | 6 | 95 | 2,2% |
| Total | 589 | 614 | 758 | 522 | 530 | 513 | 432 | 363 | 4321 |  |
| Frec. Absoluta | 13,6% | 14,2% | 17,5% | 12,1% | 12,3% | 11,9% | 10,0% | 8,4% |  |  |

<!-- Estadísticas: 11 filas, 11 columnas -->
<!-- Contexto posterior: -->
<!-- **Figura 61: Histograma magnitud capa superficial invierno.** Marzo 2024 -->
<!-- FIN TABLA 30 -->


vi

Marzo 2024

Tabla 31: Magnitud y dirección capa media invierno. ............................................................................................ 84

<!-- INICIO TABLA 31 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- La capa media se encuentra a una profundidad de 4 m respecto a la línea de más baja marea (6 metros desde el fondo). En la Tabla 31 se observa que las corrientes con un mayor porcentaje de ocurrencia oscilan entre los 5-10 y 10-15 cm/s con ocurrencias entre el 39,6% y 24,8%. -->

**Tabla 31: Magnitud y dirección capa media invierno.****

| Magnitud (cm/s) | Dirección (°) | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Total | Frec.<br>Absoluta |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Magnitud (cm/s)** | N | NE | E | SE | S | SW | W | NW | NW | NW |
| Calmas | 11 | 9 | 4 | 3 | 5 | 4 | 7 | 2 | 45 | 1,0% |
| 1-5 | 105 | 136 | 127 | 112 | 92 | 125 | 120 | 124 | 941 | 21,8% |
| 5-10 | 207 | 235 | 255 | 196 | 168 | 223 | 213 | 212 | 1709 | 39,6% |
| 10-15 | 115 | 188 | 208 | 108 | 102 | 131 | 128 | 90 | 1070 | 24,8% |
| 15-20 | 32 | 83 | 95 | 33 | 28 | 45 | 50 | 23 | 389 | 9,0% |
| 20-25 | 4 | 30 | 38 | 10 | 3 | 9 | 12 | 4 | 110 | 2,5% |
| 25-30 | 2 | 12 | 11 | 4 | 0 | 3 | 0 | 0 | 32 | 0,7% |
| >30 | 2 | 0 | 13 | 3 | 3 | 3 | 0 | 1 | 25 | 0,6% |
| Total | 478 | 693 | 751 | 469 | 401 | 543 | 530 | 456 | 4321 |  |

<!-- Estadísticas: 10 filas, 11 columnas -->
<!-- Contexto posterior: -->
<!-- Marzo 2024 |Magnitud (cm/s)|Dirección (°)|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Total|Frec.<br>Absoluta| |---|---|---|---|---|---|---|---|---|---|---| -->
<!-- FIN TABLA 31 -->


Tabla 32: Magnitud y dirección capa de fondo invierno. ........................................................................................ 86

<!-- INICIO TABLA 32 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- La capa del fondo se encuentra a una profundidad de 10 metros respecto a la línea de más baja marea. En esta capa el mayor rango de magnitud para esta capa se encuentra entre los 5- 10 cm/s, con un total de 35,8% de ocurrencia (Tabla 32, Figura 65). -->

**Tabla 32: Magnitud y dirección capa de fondo invierno.****

| Magnitud (cm/s) | Dirección (°) | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Total | Frec.<br>Absoluta |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Magnitud (cm/s)** | N | NE | E | SE | S | SW | W | NW | NW | NW |
| Calmas | 7 | 4 | 2 | 5 | 6 | 4 | 4 | 7 | 39 | 0,9% |
| 1-5 | 103 | 103 | 94 | 96 | 81 | 98 | 77 | 85 | 737 | 17,1% |
| 5-10 | 204 | 212 | 212 | 179 | 177 | 196 | 169 | 196 | 1545 | 35,8% |
| 10-15 | 137 | 171 | 199 | 152 | 131 | 134 | 114 | 116 | 1154 | 26,7% |
| 15-20 | 54 | 79 | 110 | 83 | 57 | 58 | 47 | 55 | 543 | 12,6% |
| 20-25 | 14 | 29 | 55 | 35 | 17 | 24 | 24 | 12 | 210 | 4,9% |
| 25-30 | 6 | 10 | 15 | 13 | 3 | 4 | 1 | 4 | 56 | 1,3% |
| >30 | 13 | 1 | 6 | 7 | 5 | 1 | 1 | 3 | 37 | 0,9% |
| Total | 538 | 609 | 693 | 570 | 477 | 519 | 437 | 478 | 4321 |  |
| Frec, Absoluta | 12,5% | 14,1% | 16,0% | 13,2% | 11,0% | 12,0% | 10,1% | 11,1% |  |  |

<!-- Estadísticas: 11 filas, 11 columnas -->
<!-- Contexto posterior: -->
<!-- Marzo 2024 **Figura 65: Histograma de magnitud capa de fondo invierno.** -->
<!-- FIN TABLA 32 -->


Tabla 33: Correntometría euleriana verano ........................................................................................................... 88

<!-- INICIO TABLA 33 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- De igual forma que para la correntometría de invierno, se caracterizaron las corrientes del sitio por medio de un correntómetro ADCP (Acoustic Doppler Current Profiler) fondeado frente a la zona de descarga, donde se analizaron los datos de magnitud y dirección registrados por el equipo. La ubicación donde fue fondeado el equipo se presenta en la Tabla 33 a continuación. -->

**Tabla 33: Correntometría euleriana verano****

| Estudios | Periodo de medición | Coordenada UTM | Col4 |
| --- | --- | --- | --- |
| **Estudios** | **Periodo de medición** | Este | Norte |
| Correntometría euleriana | 04-03-2021 al 05-04-2021 | 638.480 | 5.374.082 |

<!-- Estadísticas: 2 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- El análisis de datos se efectuó en base a estadística básica y distribución de frecuencia de la magnitud y la dirección de la corriente, para tres capas representativas de la columna de agua (superficie, medio y fondo). Además, se elaboraron histogramas y rosas de direcciones correspondientes a la dirección y magnitud de la corriente para cada una de las capas analizadas. -->
<!-- FIN TABLA 33 -->


Tabla 34: Magnitud y dirección capa superficial verano. ....................................................................................... 88

<!-- INICIO TABLA 34 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Para la capa superficial se utilizó la capa de los 10 metros desde el fondo. Se utiliza esta capa como superficial debido a que representa esta sección de la columna de agua sin efectos de la marea. De acuerdo con los resultados del registro de velocidad, los mayores porcentajes de ocurrencia ocurrieron entre los rangos 5-10 y 10-15 con 37,1% y 21,4% respectivamente. (Tabla 34, Figura 67). -->

**Tabla 34: Magnitud y dirección capa superficial verano.****

| Magnitud (cm/s) | Dirección (°) | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Total | Frec.<br>Absoluta |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Magnitud (cm/s)** | N | NE | E | SE | S | SW | W | NW | NW | NW |
| Calmas | 5 | 0 | 6 | 4 | 5 | 3 | 2 | 3 | 28 | 0,6% |
| 0-5 | 128 | 143 | 199 | 123 | 119 | 82 | 82 | 79 | 955 | 21,2% |
| 5-10 | 210 | 356 | 419 | 264 | 134 | 82 | 68 | 141 | 1674 | 37,1% |
| 10-15 | 87 | 238 | 307 | 173 | 64 | 18 | 23 | 55 | 965 | 21,4% |
| 15-20 | 50 | 78 | 133 | 55 | 22 | 3 | 3 | 15 | 359 | 8,0% |
| 20-25 | 35 | 19 | 27 | 40 | 22 | 3 | 0 | 21 | 167 | 3,7% |
| 25-30 | 39 | 11 | 15 | 15 | 13 | 3 | 0 | 17 | 113 | 2,5% |
| >30 | 73 | 18 | 10 | 42 | 52 | 1 | 0 | 50 | 246 | 5,5% |
| Total | 627 | 863 | 1116 | 716 | 431 | 195 | 178 | 381 | 4507 |  |
| Frec,.Absoluta | 13,9% | 19,1% | 24,8% | 15,9% | 9,6% | 4,3% | 3,9% | 8,5% |  |  |

<!-- Estadísticas: 11 filas, 11 columnas -->
<!-- Contexto posterior: -->
<!-- Marzo 2024 **Figura 67: Histograma de magnitud capa superficial verano.** -->
<!-- FIN TABLA 34 -->


Tabla 35: Magnitud y dirección capa media verano. .............................................................................................. 90

<!-- INICIO TABLA 35 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- La capa media se encuentra a una profundidad de 4 m respecto a la línea de más baja marea (6 metros desde el fondo). En la Tabla 35 se observa que las corrientes con un mayor porcentaje de ocurrencia oscilan entre los 1-5 y 5-10 cm/s con ocurrencias entre el 40% y 24,2%. -->

**Tabla 35: Magnitud y dirección capa media verano.****

| Magnitud (cm/s) | Dirección (°) | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Total | Frec.<br>Absoluta |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Magnitud (cm/s)** | N | NE | E | SE | S | SW | W | NW | NW | NW |
| Calmas | 5 | 5 | 3 | 5 | 8 | 9 | 6 | 8 | 49 | 1,1% |
| 1-5 | 89 | 169 | 197 | 168 | 124 | 97 | 118 | 109 | 1071 | 24,2% |
| 5-10 | 127 | 398 | 465 | 288 | 185 | 77 | 91 | 139 | 1770 | 40,0% |
| 10-15 | 77 | 237 | 341 | 178 | 63 | 22 | 26 | 53 | 997 | 22,6% |
| 15-20 | 20 | 113 | 160 | 55 | 24 | 8 | 4 | 10 | 394 | 8,9% |
| 20-25 | 7 | 29 | 37 | 10 | 7 | 2 | 0 | 3 | 95 | 2,1% |
| 25-30 | 4 | 7 | 12 | 4 | 1 | 1 | 1 | 0 | 30 | 0,7% |
| >30 | 5 | 4 | 3 | 1 | 2 | 0 | 0 | 0 | 15 | 0,3% |
| Total | 334 | 962 | 1218 | 709 | 414 | 216 | 246 | 322 | 4421 |  |
| Frec. Absoluta | 7,6% | 21,8% | 27,6% | 16,0% | 9,4% | 4,9% | 5,6% | 7,3% |  |  |

<!-- Estadísticas: 11 filas, 11 columnas -->
<!-- Contexto posterior: -->
<!-- **Figura 69: Histograma magnitud capa media verano.** Marzo 2024 -->
<!-- FIN TABLA 35 -->


Tabla 36: Magnitud y dirección capa de fondo verano. .......................................................................................... 91

<!-- INICIO TABLA 36 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- La capa del fondo se encuentra a una profundidad de 10 metros respecto a la línea de más baja marea. En esta capa los mayores rangos de magnitud para esta capa se encuentran entre los 5 - 10 cm/s y 10 - 15 cm/s, con un total de 22,8% y 23,8% de ocurrencia (Tabla 36, Figura 71). -->

**Tabla 36: Magnitud y dirección capa de fondo verano.****

| Magnitud (cm/s) | Dirección (°) | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Total | Frec.<br>Absoluta |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Magnitud (cm/s)** | N | NE | E | SE | S | SW | W | NW | NW | NW |
| Calmas | 1 | 3 | 1 | 3 | 2 | 1 | 4 | 1 | 16 | 0,3% |
| 1-5 | 69 | 72 | 76 | 79 | 51 | 47 | 56 | 41 | 491 | 10,6% |
| 5-10 | 140 | 187 | 184 | 166 | 136 | 81 | 60 | 102 | 1056 | 22,8% |
| 10-15 | 189 | 249 | 221 | 175 | 150 | 34 | 25 | 57 | 1100 | 23,8% |
| 15-20 | 139 | 185 | 126 | 172 | 119 | 26 | 8 | 21 | 796 | 17,2% |
| 20-25 | 126 | 88 | 54 | 78 | 81 | 5 | 1 | 15 | 448 | 9,7% |
| 25-30 | 92 | 30 | 20 | 38 | 51 | 4 | 0 | 2 | 237 | 5,1% |
| >30 | 183 | 32 | 17 | 61 | 164 | 17 | 1 | 7 | 482 | 10,4% |

<!-- Estadísticas: 9 filas, 11 columnas -->
<!-- Contexto posterior: -->
<!-- Marzo 2024 |Magnitud (cm/s)|Dirección (°)|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Total|Frec.<br>Absoluta| |---|---|---|---|---|---|---|---|---|---|---| -->
<!-- FIN TABLA 36 -->


Tabla 37: Módulos utilizados en la modelación con MOHID Water ....................................................................... 99

<!-- INICIO TABLA 37 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- . Marzo 2024 -->

**Tabla 37: Módulos utilizados en la modelación con MOHID Water****

| Módulo | Descripción |
| --- | --- |
| **Geometry** | El módulo Geometry maneja la discretización vertical en MOHID. Fue diseñado para dividir la<br>columna de agua. Además, este Módulo gestiona la inicialización y la evolución temporal de la<br>grilla. |
| **Atmosphere** | El módulo de Atmosphere es responsable de los datos meteorológicos necesarios para calcular<br>los procesos que ocurren en la interfaz agua-aire, como el cálculo de la tensión de cizalladura<br>del viento, los balances de radiación, los flujos de calor latente y sensible. |
| **Interface Water-air** | El módulo Interface Water-air es responsable de los procesos que ocurren en la interfaz agua-<br>aire, como el cálculo de la tensión de cizalladura del viento , los balances de radiación, los flujos<br>de calor latente y sensible. Este módulo toma como inputs los datos de módulo atmosphere. |
| **Hydrodynamic** | El módulo hidrodinámico resuelve las ecuaciones primitivas de continuidad y momento para la<br>elevación de la superficie y el campo de velocidad 3D para flujos incompresibles, en<br>coordenadas horizontales ortogonales y coordenadas verticales genéricas, asumiendo equilibrio<br>hidrostático y aproximaciones de Boussinesq |
| **Water properties** | El módulo Water Properties es el módulo de transporte euleriano 3D incluido en MOHID. El<br>módulo Water Properties se encarga de calcular la evolución de las propiedades en la columna<br>de agua |
| **Interface sediment-**<br>**water** | El módulo de Interface sediment-water calcula las condiciones de contorno en la parte inferior<br>de la columna de agua. Calcula el esfuerzo cortante como una condición límite para los módulos<br>hidrodinámico y de turbulencia |
| **Turbulence** | El módulo turbulence utiliza el modelo GOTM, el cual es el encargado de simular la turbulencia<br>generada por los esfuerzos de corte entre la interfaz agua aire en superficie, agua sedimento en<br>profundidad, así como también variaciones en las densidades que generan cambios en las<br>presiones y por tanto velocidades verticales. |
| **Lagrangian** | Modelo de transporte lagrangiano, gestiona la evolución de las mismas propiedades que el<br>modelo de las propiedades del agua utilizando un enfoque en función lagrangiana. |

<!-- Estadísticas: 8 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Marzo 2024 Un esquema de la implementación y funcionamiento de los módulos del modelo MOHID se explican en la Figura 77. -->
<!-- FIN TABLA 37 -->


**FIGURAS**

Figura 1: Ubicación del punto de descarga ............................................................................................................ 12

Figura 2: Proyección de emisario submarino Fuente: Anclaje tubería de emisario, AEX Group........................... 13

Figura 3: Esquema de configuración de difusores del emisario submarino Fuente: Anclaje tubería de

emisario, AEX Group............................................................................................................................... 14

Figura 4: Zonas de las grillas por Niveles de modelado Numérico. ....................................................................... 19

Figura 5: Batimetría en Grilla Nivel 1 (Regional). ................................................................................................... 21

Figura 6: Batimetría en Grilla Nivel 2. ..................................................................................................................... 21

Figura 7: Grilla modelo nivel 3 (Sitio del Proyecto). ............................................................................................... 22

Figura 8: Ejemplo de las grillas utilizadas en el modelo (resolución 21,3 m) ......................................................... 22

Figura 9: Esquemas de tipologías de grillas verticales .......................................................................................... 23

Figura 10: Esquematización de las simulaciones realizadas ................................................................................. 24

Figura 11: Esquema de integración del campo cercano con el campo lejano ....................................................... 26

Figura 12: Comparación del nivel del mar medido v/s modelado. ......................................................................... 30

Figura 13: Correlación directa del nivel del mar medido v/s modelado. ................................................................ 31

Figura 16: Comparación temporal de temperatura en escenario invierno ............................................................. 32

Figura 17: Comparación temporal de temperatura en escenario verano ............................................................... 33

Figura 18: Plumas de dilución y dispersión campo cercano parámetros a) NT y b) PT ........................................ 34

Figura 19: Plumas de dilución y dispersión campo cercano parámetro c) DBO 5 y d) pluma de integración

de todos los parámetros .......................................................................................................................... 34

Figura 20: Pluma de dispersión de Nitrógeno Total en invierno con modelación de 30 días ................................ 36

Figura 21: Pluma de dispersión de Nitrógeno Total en invierno con modelación de sicigia .................................. 36

Figura 22: Pluma de dispersión de Nitrógeno Total en invierno con modelación de cuadratura ........................... 37

Figura 23: Pluma de dispersión de Fósforo Total en invierno con modelación de 30 días ................................... 38

Figura 24: Pluma de dispersión de Fósforo Total en invierno con modelación de sicigia ..................................... 38

vii

Marzo 2024

Figura 25: Pluma de dispersión de Fósforo Total en invierno con modelación de cuadratura .............................. 39

Figura 26: Pluma de dispersión de DBO 5 en invierno con modelación de 30 días ................................................ 40

Figura 27: Pluma de dispersión de DBO 5 en invierno con modelación de sicigia ................................................. 40

Figura 28: Pluma de dispersión de DBO 5 en invierno con modelación de cuadratura........................................... 41

Figura 29: Pluma de dispersión de Nitrógeno Total en verano con modelación de 30 días .................................. 42

Figura 30: Pluma de dispersión de Nitrógeno Total en verano con modelación de sicigia ................................... 42

Figura 31: Pluma de dispersión de Nitrógeno Total en verano con modelación de cuadratura. ........................... 43

Figura 32: Pluma de dispersión de Fósforo Total en verano con modelación de 30 días ..................................... 44

Figura 33: Pluma de dispersión de Fósforo Total en verano con modelación de sicigia ....................................... 44

Figura 34: Pluma de dispersión de Fósforo Total en verano con modelación de cuadratura ................................ 45

Figura 35: Pluma de dispersión de DBO 5 en verano con modelación de 30 días ................................................. 46

Figura 36: Pluma de dispersión de DBO 5 en verano con modelación de sicigia ................................................... 46

Figura 37: Pluma de dispersión de DBO 5 en verano con modelación de cuadratura ............................................ 47

Figura 38: Pluma de dispersión máxima para NT en invierno considerando sicigia y cuadratura. ....................... 48

Figura 39: Pluma de dispersión máxima para NT en verano considerando sicigia y cuadratura. ......................... 48

Figura 40: Área de dispersión total (sicigia y cuadratura en verano e invierno) de NT ......................................... 49

Figura 41: Curvas de decaimiento del parámetro NT invierno (Norte, Este, Sur y Oeste) .................................... 51

Figura 42: Curvas de decaimiento del parámetro NT verano (Norte, Este, Sur y Oeste) ...................................... 52

Figura 43: Pluma de dispersión máxima para PT en invierno considerando sicigia y cuadratura ......................... 53

Figura 44: Pluma de dispersión para PT en verano considerando sicigia y cuadratura ........................................ 54

Figura 45: Área de dispersión total de PT .............................................................................................................. 54

Figura 46: Curvas de decaimiento del parámetro PT invierno (Norte, Este, Sur y Oeste) .................................... 56

Figura 47: Curvas de decaimiento del parámetro PT verano (Norte, Este, Sur y Oeste) ...................................... 57

Figura 48: Pluma de dispersión para DBO 5 en invierno considerando sicigia y cuadratura. ................................. 58

Figura 49: Pluma de dispersión para DBO 5 en verano considerando sicigia y cuadratura. .................................. 59

Figura 50: Área de dispersión total de DBO 5. ......................................................................................................... 59

Figura 51: Curvas de decaimiento del parámetro DBO 5 invierno (Norte, Este, Sur y Oeste) ................................ 61

Figura 52: Curvas de decaimiento del parámetro DBO 5 verano (Norte, Este, Sur y Oeste) ................................. 62

Figura 53: Área de influencia de la descarga en el cuerpo de agua marino .......................................................... 63

Figura 54: Puntos de Desembocadura de los Ríos afluentes considerados en modelación regional (Nivel 1

arriba) y Ríos considerados en modelación del sector (Nivel 2 y 3 abajo). ............................................ 75

Figura 59: Instante de muestra del modelo WRF con magnitudes de vientos utilizados en la modelación en

Nivel 2 y 3. ............................................................................................................................................... 81

viii

Marzo 2024

Figura 60: Ubicación y tamaño de las grillas utilizadas. ......................................................................................... 82

Figura 61: Histograma magnitud capa superficial invierno. ................................................................................... 83

Figura 62: Rosa de Corrientes capa superficial invierno ........................................................................................ 84

Figura 63: Histograma magnitud capa media invierno. .......................................................................................... 85

Figura 64: Rosa de direcciones capa media invierno ............................................................................................ 86

Figura 65: Histograma de magnitud capa de fondo invierno. ................................................................................. 87

Figura 66: Rosa de direcciones capa de fondo invierno. ....................................................................................... 87

Figura 67: Histograma de magnitud capa superficial verano. ................................................................................ 89

Figura 68: Rosa de direcciones capa superficial verano. ....................................................................................... 89

Figura 69: Histograma magnitud capa media verano. ........................................................................................... 90

Figura 70: Rosa de direcciones capa media verano. ............................................................................................. 91

Figura 71: Histograma de magnitud capa de fondo verano. .................................................................................. 92

Figura 72: Rosa de direcciones capa de fondo verano. ......................................................................................... 93

Figura 73: Series de tiempo de información atmosférica a partir de modelo WRF en sitio de descarga del

proyecto. .................................................................................................................................................. 94

Figura 74: Mapa global de componente M2, modelo FESS 2014.......................................................................... 95

Figura 75: Interacción módulos MOHID, Fuente: Reporte Inicial MOHID 2009 .................................................... 97

Figura 76: Interacción módulos MOHID Water....................................................................................................... 98

Figura 77: Esquema de funciones e implementación módulos MOHID Water. ................................................... 100

**ANEXOS**

**ANEXO A**
Archivos de entrada y salida del modelo

**ANEXO B**

Antecedentes

**ANEXO C**
Metodología

ix

Marzo 2024

### 1.0 INTRODUCCIÓN

El presente documento técnico se centra en el estudio de la modelación de descarga de efluentes de la Piscicultura
Aucha en el medio marino, estudio que fue presentado tanto en la Declaración de Impacto Ambiental (DIA) como
en la Adenda anterior del proyecto y en función de los requerimientos de la autoridad y de la comunidad, quienes
han solicitado un robustecimiento del modelo, en cuanto a incorporar el análisis de una condición adicional del
mezclado de la descarga en el medio receptor (modelación de ciclo lunar completo de 30 días).

El proyecto se ubica en el sector de Aucha, comuna de Calbuco, provincia de Llanquihue, Región de Los Lagos, y
tiene como objetivo ampliar la capacidad de producción (biomasa) de especies salmónidos a un total de 3.210
toneladas por año. Para lograr este objetivo es necesario realizar una completa evaluación de impactos del
proyecto, la cual se sustenta y apoya en el desarrollo de modelaciones y proyecciones de los efectos sobre cada
componente ambiental. Uno de los componentes más importantes es el componente calidad de agua, por lo tanto,
el desarrollo de una modelación hidrodinámica robusta es fundamental para evaluar la viabilidad del proyecto.

Para realizar una modelación hidrodinámica robusta, se implementaron diversas mejoras al modelo y se enfocaron
en: 1) una configuración del modelo, basada en niveles jerárquicos, la cual mejora la representación del área de
descarga de efluentes y la proyección de la descarga, 2) la utilización de datos de entrada de alta resolución
espacio-temporal y representativa del sector modelado, lo que robustece la modelación de la descarga y mejora a
la representación del área de la descarga de efluentes, 3) la modelación combinada de diversas condiciones, como
invierno/verano, sicigia/cuadratura, las cuales se enfocaron en obtener y representar el peor escenario posible, 4)
información de campo y del sector que comprende información adicional a la información ya presentada en la DIA,
y lo solicitado en ICSARA Complementario en lo referido a 5) una modelación de ciclo lunar completo de 30 días.

Todas las variables mencionadas anteriormente aseguran que la modelación hidrodinámica (calibrada y validada),
sea representativa del sector estudiado generando una confiable proyección de la descarga de efluentes, y
permitiendo proporcionar información adecuada para una correcta evaluación del impacto del proyecto. De este
modo, el informe actual presenta todos los antecedentes que describen las mejoras, consideraciones y detalles
que se utilizaron para darle mayor robustez al modelo hidrodinámico y de dispersión de efluentes y sus principales

resultados.

Cabe señalar que el presente estudio considera y fue realizado bajo las guías publicadas por el Servicio de
Evaluación Ambiental (SEA), principalmente la _Guía de áreas de influencia de ecosistemas marinos (2023)_ y la
_Guía metodológica para la descripción de ecosistemas marinos (2022),_ con lo que se buscó que el proyecto sea
ambientalmente responsable y cumpla con la normativa vigente.

10

Marzo 2024

### 2.0 OBJETIVOS

El objetivo del presente estudio es determinar el comportamiento de la pluma de dispersión y su área de influencia
en el medio marino proveniente del efluente futuro del proyecto “Ampliación piscicultura de recirculación Aucha”.
Para ello, se consideraron los escenarios de invierno y verano, en condiciones de ciclos mareales en sicigia y
cuadratura, sumado a una condición de modelación de 30 días (ciclo lunar completo), utilizando para este fin la

herramienta de modelación MOHID.

### 2.1 Objetivos específicos

 - Implementar un modelo 3D Hidrodinámico en la costa marina del sector Aucha, en la comuna de Calbuco,
Región de Los Lagos para condiciones de sicigia, cuadratura y ciclo lunar completo para los escenarios de
invierno y verano.

 - Implementar un modelo 3D Lagrangiano acoplado al modelo hidrodinámico para escenarios de invierno y
verano, considerando las condiciones de las fases mareales en sicigia, cuadratura y ciclo lunar completo

de 30 días.

 - Determinar el comportamiento de la pluma de dispersión considerando los parámetros: Nitrógeno total,
Fósforo Total y DBO 5 para escenarios de invierno y verano, considerando las condiciones de las fases
mareales en sicigia, cuadratura y ciclo lunar completo de 30 días.

 - Determinar y analizar el área de influencia de la descarga proyectada de la piscicultura Aucha para el
componente calidad de agua marina.

11

Marzo 2024

### 3.0 ANTECEDENTES 3.1 Ubicación del proyecto

El área de estudio se ubica en el sector Aucha, comuna de Calbuco, provincia de Llanquihue, Región de Los Lagos.
El sector está ubicado estratégicamente para permitir mayor cercanía de la piscicultura a los diversos centros de
engorda de la empresa. La ubicación del punto de descarga se encuentra en la Figura 1, mientras que las
coordenadas del proyecto y de la descarga se incluyen en la Tabla 1.

**Figura 1: Ubicación del punto de descarga de Piscicultura Aucha.**

**Tabla 1: Ubicación del punto de descarga de Piscicultura Aucha.**

|Punto|Coordenadas UTM Datum WGS 84 - Huso 18 Sur|Col3|
|---|---|---|
|**Punto**|**Este**|**Norte**|
|Ubicación del proyecto|638.629|5.374.446|
|Punto de descarga|638.436|5.374.155|

12

Marzo 2024

### 3.2 Características del emisario submarino

El emisario submarino, corresponde a una tubería de 400 mm de diámetro, y presenta una longitud total del
emisario de 242,1 m, donde su arranque en la costa se ubica a la cota de +8 m, hasta su extremo que se ubica
aproximadamente en el veril de los 4 m de profundidad al NRS, como se muestra en la Figura 2.

**Figura 2: Proyección de emisario submarino de Piscicultura Aucha.**

**Fuente: Anclaje tubería de emisario, AEX Group.**

**Difusores**

Es importante destacar que la tubería utilizada para la descarga de efluentes de la piscicultura en el medio marino
considera difusores, los cuales permiten aumentar significativamente la eficiencia del mezclado y la dilución de la
descarga. La turbulencia que se genera en los primeros metros desde la salida del difusor debido a la velocidad
de la descarga favorece la mezcla (Kikkert, 2006).

Los difusores se encuentran en el extremo del emisario submarino, y corresponden a 15 puertas de 60 [mm] de
diámetro separadas a cada 1 [m] de distancia (ver Figura 3), los que dirigen el flujo verticalmente hacia arriba,
perpendicular al fondo marino (al cenit de este).

13

Marzo 2024

**Figura 3: Esquema de configuración de difusores del emisario submarino de Piscicultura Aucha.**

**Fuente: Anclaje tubería de emisario, AEX Group.**

Dicha configuración fue utilizada en la modelación lagrangiana, debido a que es un factor de gran importancia para
obtener una dilución significativa en el campo cercano de la pluma de descarga. En resumen, debido a la velocidad
de salida de la descarga, configuración, cantidad de difusores y la diferencia de densidad entre el efluente y el
medio receptor; la pluma de dispersión se dirige verticalmente hacia la superficie y permite llegar a este estrato
con concentraciones significativamente más bajas que las de la descarga inicial.

### 3.3 Correntometría

**3.3.1** **Correntometría invierno**

Para describir las corrientes durante invierno, se analizaron datos de dirección y magnitud registrados por un
correntómetro ADCP (Acoustic Doppler Current Profiler) fondeado frente a la zona de descarga cuya posición se
presenta en la siguiente tabla:

**Tabla 2: Fecha y ubicación del ADCP en invierno**

|Estudios|Periodo de medición|Coordenada UTM|Col4|
|---|---|---|---|
|**Estudios**|**Periodo de medición**|**Este**|**Norte**|
|Correntometría euleriana|23-08-2020 al 22-09-2020|638.438|5.374.107|

**3.3.2** **Correntometría verano**

A modo complementario, se realizó una correntometría por medio de un equipo ADCP fondeado frente a la zona
de descarga para la estación de verano, donde se analizaron los datos de magnitud y dirección registrados por el
equipo. La ubicación donde fue fondeado el equipo se presenta en la Tabla 3 a continuación.

**Tabla 3: Fecha y ubicación del ADCP en verano**

|Estudios|Periodo de medición|Coordenada UTM|Col4|
|---|---|---|---|
|**Estudios**|**Periodo de medición**|**Este**|**Norte**|
|Correntometría euleriana|04-03-2021 al 05-04-2021|638.480|5.374.082|

14

Marzo 2024

En el Anexo B del presente informe “Antecedentes” específicamente en el apartado “Información de corrientes” se
encuentra un análisis estadístico de las corrientes para ambos periodos (invierno y verano). Cabe destacar que la
información de corriente tanto brutas (sin procesar) como procesadas de ambos periodos se encuentran en el
“Anexo VI - Informe de Modelación - Correntometrías” de la presente Adenda.

### 3.4 Calidad del efluente proyectado de la Piscicultura Aucha y calidad del agua del cuerpo receptor

**3.4.1** **Calidad del efluente proyectado**

Respecto a la calidad de la descarga relacionada con los compuestos que fueron modelados, se consideraron el
nitrógeno total, fósforo total y DBO 5 . Estos compuestos representan los niveles de nutrientes y carga orgánica
presentes en el efluente. El nitrógeno total como el fósforo total engloban sus componentes disueltos, particulados,
orgánicos e inorgánicos. Para evaluar la calidad de la descarga se realizó un balance de masa considerando el
escenario más desfavorable, que representa la mayor emisión de la piscicultura.

A continuación, en la Tabla 4 se señala la calidad (concentración) de la descarga:

**Tabla 4: Calidad (concentración) de la descarga.**

|Componente (Parámetro)|Descarga [mg/L]|
|---|---|
|Nitrógeno Total|5,4|
|Fósforo Total|0,9|
|DBO5|10,7|

Respecto al caudal, para la modelación se consideró un caudal máximo de descargar de 429 [L/s]. Es muy
importante señalar que se modela un escenario hipotético y desfavorable ya que, se utiliza las máximas
concentraciones del efluente (Tabla 4) con el máximo caudal a descargar (429 [L/s]).

**3.4.2** **Calidad de agua del medio receptor**

Se obtuvo información sobre el cuerpo receptor a partir de las caracterizaciones ambientales realizadas tanto en
invierno como en verano (ver Anexo VI de la DIA y Anexo V de la Adenda anterior, respectivamente). Para
caracterizar el entorno marino, se recolectaron muestras de agua en distintas estaciones de monitoreo, las cuales
fueron analizadas en laboratorio para determinar sus concentraciones. El valor de concentración utilizado como
referencia para el medio receptor (también denominado en adelante valor del medio o del cuerpo receptor) fue
calculado considerando el promedio de los resultados obtenidos en dichas estaciones junto con su desviación
estándar. Con el promedio, se buscó representar de manera más realista las concentraciones naturales del sector.

A su vez, la desviación estándar fue incluida con tal de evidenciar la variabilidad de las concentraciones distribuidas

del medio.

Para el cálculo del valor de referencia o condición base del cuerpo receptor en el área cercana de descarga, se
excluyeron las estaciones ubicadas a distancias considerablemente alejadas del punto de descarga del proyecto.
Estas estaciones específicas, denominadas L1, L2, A1 y A2, se encuentran en la caracterización de la línea base

realizada durante invierno.

15

Marzo 2024

La siguiente tabla presenta los valores referenciales de las concentraciones del cuerpo receptor que fueron

considerados en la modelación.

**Tabla 5: Valores referenciales de las concentraciones del cuerpo receptor**

|Parámetro|Valor referencial del medio marino[mg/L]|Col3|
|---|---|---|
|**Parámetro**|**Invierno**|**Verano**|
|Nitrógeno Total|1,4|1,2|
|Fósforo Total|0,07|0,12|
|DBO5|2,0|4,4|

Los resultados del monitoreo realizado en invierno y verano presentan una variabilidad en ambas estacionalidades.
A continuación, se presenta la desviación estándar como una medida de dispersión y de variabilidad de los datos
en el cuerpo de agua marino respecto que presentan ambos monitoreos.

**Tabla 6: Desviación estándar respecto al monitoreo en el cuerpo de agua marino para invierno y verano**

|Parámetro|Desviación Estándar de ambos monitoreos[mg/L]|Col3|
|---|---|---|
|**Parámetro**|**Invierno**|**Verano**|
|Nitrógeno Total|0,98|0,21|
|Fósforo Total|0,03|0,15|
|DBO5|01|0,6|

1 Para tener en cuenta la incertidumbre en relación con los valores muestreados, se ha considerado una variabilidad del 10% del promedio en
los resultados que se presentarán a continuación en las curvas de decaimiento.

16

Marzo 2024

### 4.0 METODOLOGÍA 4.1 Modelo MOHID

Para el estudio de caracterización de la pluma de dispersión e hidrodinámica en el medio se utilizó el modelo
MOHID que opera bajo el software OpenFlows Flood. Esta herramienta comprende un sistema informático para el
estudio de sistemas acuáticos, y fue desarrollado por el Centro de Investigación de Tecnología Marina (MARETEC)
perteneciente al Instituto Superior Técnico (IST) de la Universidad de Lisboa, Portugal. El modelo dispone de una
serie de herramientas funcionales para el pre-proceso de la información y post-proceso de los resultados, junto a
su correspondiente visualización. Entre las herramientas con mayor relevancia disponibles por OpenFlows Flood
se destacan; la generación de cuadriculas computacionales, condiciones iniciales y de borde, transformación de

información a diversos formatos, entre otros.

Este modelo fue el utilizado tanto para la modelación hidrodinámica como para la estimación de la pluma de
dispersión (modelo lagrangiano) de los nutrientes Nitrógeno total (NT), Fósforo total (PT) y Demanda bioquímica
de oxígeno a 5 días (DBO 5 ). La explicación en detalle del modelo en conjunto con todos los módulos utilizados se
encuentra en el Anexo C (“Metodología”) del presente informe. A continuación, se presenta la información más
relevante que le imprime robustez al modelo.

**4.1.1** **Información de entrada del modelo**

Con el fin de obtener resultados que representen las condiciones particulares del sector donde se llevará a cabo
el proyecto, se consideró información actualizada y de calidad como condiciones de borde e iniciales del modelo,
las que se resumen a continuación:

### ▪

[Calidad del agua del cuerpo receptor para invierno y verano (ver punto 3.4.2). ]

### ▪

[Calidad del efluente (caudal, concentración) (ver punto 3.4.1). ]

### ▪

[Ríos afluentes relevantes para la modelación (Anexo B del presente informe (“Antecedentes”)). ]

### ▪

[Perfiles de salinidad y temperatura en las condiciones iniciales y de borde del Atlas CHONOS ]

[(https://chonos.ifop.cl/atlas/) para invierno (01/08/2020 al 30/09/2020) y verano (01/03/2021 al 01/04/2021)](https://chonos.ifop.cl/atlas/)
(Anexo B del presente informe (“Antecedentes”)).

### ▪

[Campo meteorológico del sector correspondiente a un año (WRF) (Anexo B del presente informe ]

(“Antecedentes”)).

### ▪

[Modelo global de mareas FES 2014 (Lyard et al., 2014) (Anexo B del presente informe (“Antecedentes”)). ]

_**4.1.1.1**_ _**Ríos afluentes**_

En el proyecto se tuvo en cuenta la presencia de varios ríos cercanos que desembocan en el mar y aportan una
gran cantidad de agua dulce. Se consideraron un total de 10 ríos en las simulaciones, los cuales son de importancia
debido a su caudal. Estos ríos son: Río Ancud, Maullín, Chaica, Lenca, Puelo, Cochamó, Petrohué, Aucha y dos

ríos sin nombre.

17

Marzo 2024

Al considerar estos aportes de agua dulce, el modelo genera cambios en las densidades de la superficie de la
columna de agua que, a su vez, generan corrientes ascendentes y descendentes producto de gradientes verticales
de densidad (Smith _et al_ ., 2018), lo que es más representativo del sector del proyecto. La información sobre estos
caudales se obtuvo a través de la aplicación Flow de la plataforma Chonos del IFOP (Instituto de Fomento
[Pesquero), específicamente desde su sitio web (https://chonos.ifop.cl/flow/, 2023). La imagen con los ríos utilizados](https://chonos.ifop.cl/flow/)
y los caudales ingresados se presentan en el Anexo B del presente informe (“Antecedentes”).

_**4.1.1.2**_ _**Perfiles de salinidad y temperatura**_

Respecto a los perfiles de salinidad y temperatura en la columna de agua como condiciones iniciales y de borde
del modelo, se utilizó la información proveniente de la aplicación ATLAS de la página CHONOS
[(https://chonos.ifop.cl/atlas/, 2023). Se seleccionaron un total de 6 perfiles que representaron las condiciones de](https://chonos.ifop.cl/atlas/)
borde, abarcando tanto los períodos estacionales de invierno como de verano, y considerando las ubicaciones de
borde Oeste (canal de Chacao) y Sur (Mar interior de Chiloé). La utilización de dicha información conlleva que el
modelo reproduzca de manera precisa las condiciones del sector. El detalle en conjunto con los perfiles se
encuentra en el Anexo B del presente informe (“Antecedentes).

_**4.1.1.3**_ _**Campo meteorológico de modelo WRF**_

En el modelo hidrodinámico se utilizó información cuyo fin es mejorar la representatividad de las condiciones
hidrodinámicas del sector del proyecto. Entre la información más relevante que fue incluida en esta modelación,
se encuentran un campo meteorológico proveniente del modelo WRF (Weather Research and Forecasting)
correspondiente a un año validado para el sector de estudio, de donde se obtuvo información de vientos, presión,
temperatura, radiación solar, entre otros. Toda esta información utilizada como forzantes del modelo se traduce en
una hidrodinámica más precisa. La descripción detallada de modelo WRF se presenta dentro del Anexo B del
presente informe (“Antecedentes”).

_**4.1.1.4**_ _**Modelo global de mareas FES 2014**_

Para el módulo hidrodinámico se utilizó como condición de borde inicial el modelo global de marea FES (Finite
Element Solution) 2014, el cual fue desarrollado y validado por LEGOS (Laboratory of Space Geophysical and
Oceanographic Studies, Francia), NOVELTIS y CLS (Collecte Localisation Satellites, Francia). Este modelo fue
implementado en la modelación hidrodinámica como forzante de la marea en los bordes abiertos del dominio de
nivel 1 para los períodos simulados de invierno y verano (Anexo B del presente informe (“Antecedentes”)).

18

Marzo 2024

**4.1.2** **Modelo Hidrodinámico**

_**4.1.2.1**_ _**Dominio del modelo hidrodinámico**_

La extensión del dominio de cada grilla computacional que se ingresó al modelo se presenta en la Figura 4 y en la
Tabla 7, donde se muestran las tres grillas computacionales del modelo, correspondientes a la grilla regional (1er
nivel), grilla en ensenada Codihue (2do nivel) y en el Sector Aucha (3er nivel), donde se realizarán las modelaciones
hidrodinámicas y de dispersión de los contaminantes.

Con el fin de reducir los tiempos de cálculo y no comprometer la precisión del modelo considerando la extensión
del dominio computacional, se obtuvieron resultados de una mayor resolución en zonas más someras (3er nivel),
utilizando la metodología de “anidamiento”. Este procedimiento consiste en definir una grilla computacional de baja
resolución espacial e ir aumentando su resolución paulatinamente hasta alcanzar la zona de interés. Mediante esta
metodología se logra optimizar el tiempo de cálculo y considerar los fenómenos físicos de diferentes escalas. La
grilla del 1er nivel tiene una resolución de 320 m, la de 2do nivel de 64 m y la de 3er nivel de 16 m. En cada celda
de las grillas contienen un volumen de control, donde se resolverán las ecuaciones de cada modelo.

**Figura 4: Zonas de las grillas por Niveles de modelado Numérico.**

19

Marzo 2024

**Tabla 7: Parámetros de las grillas computacionales.**

|Parámetro|Grilla 1er nivel|Grilla 2do Nivel|Grilla 3er nivel|
|---|---|---|---|
|Resolución XY|320 metros|106,67 metros|21,33 metros|
|Tamaño de la grilla en Δx|0,00385|0,001281|0,00026|
|Tamaño de la grilla en Δy|0,00288|0,00096|0,00019|
|Espaciamiento temporal<br>de calculo|10 segundos|4 segundos|2 segundos|
|Origen Este|557.556,77|622.932,09|637.129,69|
|Origen Norte|5.349.841,29|5.350.929,14|5.372.873,30|
|N° Capas verticales|5|10|20|

_**4.1.2.2**_ _**Información batimétrica**_

El módulo encargado de la batimetría en el modelo MOHID realiza la descripción de las profundidades del medio
acuático a simular, calculando las áreas y los volúmenes finitos, basados en la elevación de la superficie y los
datos de batimetría. Para la confección del modelo de elevación digital, se consideró el conjunto de datos
batimétricos del estudio realizado por IngeMar, junto con las siguientes cartas náuticas SHOA:

### ▪

[N°7210: Canal Chacao ]

### ▪

[N°7310: Canal Calbuco; Paso Guar a Golfo de Ancud ]

### ▪

[N°7311: Puertos en el Golfo de Ancud ]

### ▪

[N°7300: Golfo de Ancud - isla Puluqui a Isla Quinchao ]

### ▪

[N°7320: Seno Reloncaví ]

El resto de las áreas se complementó con datos del modelo batimétrico GEBCO
[(https://www.gebco.net/data_and_products/gridded_bathymetry_data/) desde las áreas oceánicas hasta las](https://www.gebco.net/data_and_products/gridded_bathymetry_data/)

cercanías del sitio de estudio.

Ambas batimetrías fueron ordenadas de acuerdo con su resolución espacial, para luego ser ingresados en el
software OpenFlows Flood donde se realizó una interpolación, por medio del método de triangulación, y así obtener
el modelo digital de terreno asociado a cada grilla computacional. En base a lo anterior, a continuación, se muestran
las batimetrías generadas en cada uno de los 3 dominios del 1er nivel al 3er nivel.

20

Marzo 2024

**Figura 5: Batimetría en Grilla 1er nivel (Regional).**

**Figura 6: Batimetría en Grilla 2er nivel.**

21

Marzo 2024

**Figura 7: Grilla modelo 3er nivel (Sitio del Proyecto).**

_**4.1.2.3**_ _**Estructura horizontal y vertical del modelo**_

El módulo hidrodinámico del modelo MOHID organiza el dominio de estudio, también conocido como zona de
interés, mediante la implementación de grillas o celdas cuadradas regulares en el plano horizontal (X-Y) tal como
se explicó anteriormente. Paralelamente, segmenta la columna de agua en distintas capas utilizando celdas
verticales, las cuales pueden clasificarse como sigma, adaptándose de manera irregular al relieve submarino, o
como regulares, manteniendo la forma cuadrada. La Figura 8 ilustra un segmento del dominio de 3er nivel abarcado
por el modelo hidrodinámico, destacando la disposición de las celdas en el plano (X-Y). Por otro lado, la Figura 9
detalla los diseños de las grillas verticales utilizadas, ofreciendo una clara visualización de estas.

**Figura 8: Ejemplo de las grillas utilizadas en el modelo (resolución 21,3 m)**

22

Marzo 2024

**Figura 9: Esquemas de tipologías de grillas verticales**

Al integrar las dimensiones de las grillas horizontales cuadradas, con las verticales, ya sean de tipo sigma o
regulares, se conforma una estructura tridimensional conocida como cubo o poliedro. Esta estructura se identifica
como un volumen de control. Los volúmenes de control se definen en función del tamaño de las celdas en el plano
horizontal (X-Y) y del número de celdas en la columna de agua, lo que implica considerar cada capa en la
profundidad. Así, la cantidad de cubos o poliedros, es decir, los volúmenes de control se determinan según la
batimetría y la extensión del área en estudio.

Para este caso se implementó una discretización de 10 capas Sigma en superficie y 10 regulares en profundidad
en el 3er nivel, haciendo un total de 20 capas. Lo anterior con la finalidad de obtener una mayor precisión en el
fenómeno de dispersión de la pluma en superficie, debido a las características del difusor como de las componentes

del efluente.

_**4.1.2.4**_ _**Condiciones iniciales y de borde**_

Las condiciones iniciales y de borde fueron implementadas para la circulación hidrodinámica y la configuración de
los procesos de dispersión. Estas condiciones de los modelos dependen de su escala espacial y los objetivos de
la simulación. Cada nivel tiene diferentes requerimientos para que la puesta en marcha de los modelos sea
progresiva, de acuerdo con los módulos utilizados en los diferentes niveles de anidamiento.

La circulación hidrodinámica y los procesos de dilución en la simulación dependen de condiciones ambientales

tales como:

 - Información de corrientes

 - Información atmosférica

 - Información de marea.

 - Caracterización fisicoquímica del cuerpo receptor y la descarga.

La información antes mencionada puede ser revisada en el Anexo B del presente informe (“Antecedentes”).

Para generar la condición inicial, se utilizó un mes de calentamiento del modelo en cada escenario (invierno y
verano), considerando los datos de perfiles de salinidad y temperatura descritos, como también los datos
atmosféricos del modelo WRF. Luego del mes de calentamiento, se continuó con la modelación simulando un mes
adicional que corresponde a las fechas de medición de las corrientes con ADCP para ambos escenarios
estacionales. Dicho modelo hidrodinámico se utilizó como base para el cálculo de la dispersión de los compuestos
de la pluma de descarga a simular.

Cabe señalar que la correntometría utilizada para la modelación de la dispersión del campo cercano y lejano
(modelo lagrangiano) fue generada y obtenida a partir del modelo hidrodinámico para invierno y verano, por lo que

23

Marzo 2024

**no** se utilizan como input las corrientes registradas por los ADCP. Las corrientes medidas son utilizadas para el
proceso de calibración y validación del modelo hidrodinámico (comparación), con lo cual, se asegura que el
comportamiento general de la hidrodinámica del sector es representativo de la zona del proyecto.

**Calibración y Validación**

La calibración del modelo hidrodinámico fue realizada por medio de correlación por percentiles, haciendo uso de
los datos de la correntometría de invierno registrada por medio del ADCP, y comparándola con la serie de tiempo
de corrientes obtenidas del modelo hidrodinámico en la misma ubicación donde se registraron los datos del
correntómetro. En cuanto a la validación, esta fue efectuada en el período de verano, haciendo uso de la misma
metodología descrita para invierno.

Por medio de las correlaciones y series de tiempo, se estimaron índices estadísticos como el coeficiente de
regresión, las desviaciones estándar, el coeficiente de determinación, el índice BIAS, el error absoluto medio (MAE)
y la raíz de los errores promedios al cuadrado (RSME). Con ellos, fue posible determinar cuál es el nivel de certeza
de la hidrodinámica del modelo respecto a lo registrado por los correntómetros en ambas estaciones del año.

_**4.1.2.5**_ _**Escenarios Modelados**_

Para la modelación, se han considerado las condiciones relativas a las estaciones de invierno y verano tanto para
un ciclo lunar completo (30 días) como para las fases lunares que generan las mareas más extremas, es decir, en
sicigia y cuadratura. Estas condiciones fueron utilizadas para simular el comportamiento de la pluma de dispersión
de los parámetros considerados en la modelación, es decir, Nitrógeno Total (NT), Fósforo Total (PT) y DBO 5 .

**Figura 10: Esquematización de las simulaciones realizadas**

**4.1.3** **Modelo Lagrangiano**

Con el objetivo de caracterizar las variaciones de las concentraciones de la pluma en el espacio, se acopló el
modelo lagrangiano al modelo hidrodinámico previamente implementado con el fin de simular el movimiento de las
partículas de acuerdo con las corrientes obtenidas en el sitio de descarga.

24

Marzo 2024

Los procesos de mezcla a través de un emisario submarino se dividen principalmente en dos etapas: la mezcla
rápida en el campo cercano y la mezcla más lenta en el campo lejano. La mezcla rápida abarca desde el momento
en que el efluente es eyectado por los difusores hasta que el momentum del fluido disminuye significativamente.
Por otro lado, la mezcla más lenta comienza después de la etapa anterior y continúa hasta que la concentración
del vertido se iguala al medio ambiente.

Para determinar la concentración en cada celda del modelo, se llevó a cabo una interpolación de todas las
partículas presentes en cada una de las celdas. El modelo considera que cada partícula es independiente de las
demás e integra las concentraciones de cada una, las cuales se encuentran en un pequeño volumen de agua. De
esta manera, se obtiene el área total de dispersión de la pluma.

_**4.1.3.1**_ **Campo cercano**

En el campo cercano, la velocidad de emisión del fluido descargado en el mar y su densidad son los factores
dominantes. Debido a que el fluido tiene una densidad menor que el ambiente circundante, tiende a ascender en
los primeros metros de su liberación. Al encontrarse con el medio receptor y tener una alta velocidad, las partículas
se ven detenidas, lo que genera turbulencias que finalmente diluyen el fluido, reduciendo así su concentración
(Kikkert, 2006).

Para determinar el comportamiento en el campo cercano, se consideraron las partículas emitidas por los difusores
obtenidas del modelo. Donde a partir de ellas, se graficó la dispersión y dilución en el campo cercano durante todo
el período de modelación, lo que corroboraría que la pluma asciende y se mantiene en la superficie al ser eyectada
por los difusores. Cabe señalar que no existen diferencias en el campo cercano para los distintos escenarios
modelados, por lo que se presenta solo un resultado.

_**4.1.3.2**_ **Campo lejano**

En cuanto al campo lejano, se utilizó el módulo lagrangiano de MOHID para realizar el seguimiento de partículas,
las cuales representan pequeñas porciones de agua. Una vez que el fluido asciende a la superficie, comienza a
dispersarse debido a las corrientes en la columna de agua y el viento en las capas superficiales, lo que ocasiona
su dilución a medida que se desplaza.

Una vez establecida la concentración de cada partícula en el campo cercano, se le asigna un volumen de control
específico en el campo lejano. Este volumen es donde las partículas son transportadas por las corrientes definidas
por el modelo hidrodinámico. Dentro de este volumen, el modelo monitorea el tránsito de las partículas, registrando
su paso, cantidad y concentración específica. En cada instante, se identifica y registra la concentración máxima
entre las partículas presentes. Este proceso se repite sucesivamente para cada paso de tiempo (time step).

Posteriormente, para cada volumen de control, el modelo calcula el promedio de los valores máximos de
concentración obtenidos en todos los instantes de tiempo modelados. Como resultado, se obtiene una
representación de la pluma de dispersión promedio máxima, que refleja la distribución y concentración de partículas
a lo largo del tiempo en el modelo hidrodinámico. Este enfoque permite una comprensión detallada de la dinámica
de dispersión de partículas en el entorno acuático.

En el esquema siguiente (Figura 11), se presenta una representación simplificada del dominio de cálculo utilizado
en el modelo, resaltando la presencia de tres volúmenes de control específicos y las partículas contenidas dentro

25

Marzo 2024

de estos. Es importante señalar que, en la práctica de la modelación, el análisis abarca la totalidad del dominio de
cálculo, asignando volúmenes de control a cada una de las capas empleadas en el proceso. Esta metodología
permite una comprensión detallada y precisa de la dinámica de partículas a lo largo de todo el dominio estudiado.

**Figura 11: Esquema de integración del campo cercano con el campo lejano**

En esta etapa, el comportamiento de las partículas está influenciado por las corrientes generadas en el modelo
hidrodinámico. Es importante destacar que, debido a la flotabilidad positiva de la pluma, esta asciende y se
desarrolla en los primeros metros de la superficie sin afectar el fondo marino. En este caso, se presentan resultados
en los distintos escenarios de modelación, es decir tanto en sicigia, como en cuadratura y ciclo lunar completo (30
días), bajo los escenarios de invierno y verano.

### 4.2 Definición del área de influencia

**4.2.1** **Análisis de los escenarios modelados**

Para la definición del área de influencia, se realizó un análisis de los escenarios modelados, enfocándose en los

escenarios de invierno y verano, bajo las condiciones de sicigia y cuadratura. Estas condiciones se destacan por
ser más desfavorables para la dispersión y dilución de las descargas. Sin embargo, cada una por separada no es
capaz de representar el peor escenario. Por ello, se realizó una superposición de las condiciones de sicigia y
cuadratura, si bien esto jamás sucederá en la realidad, es valioso para la evaluación de impactos considerar el
peor escenario. El resultado de la superposición considera las distancias y contornos máximos de la pluma de
dispersión de ambos casos combinados (sicigia y cuadratura) y además considera las máximas concentraciones
que se encuentran en cada punto de la superposición.

Además, se examinan los resultados referentes a las áreas de dispersión y las curvas de decaimiento, las cuales
detallan la variación de la concentración para cada parámetro a lo largo de las cuatro direcciones cardinales
principales (N, E, S y W). A su vez y de forma comparativa, se presenta la curva de decaimiento de los treinta días
de modelación, considerando que esta corresponde a una condición normal o estable (menos variable) de la
dispersión.

26

Marzo 2024

**4.2.2** **Área de influencia componente calidad de agua**

La determinación del área de influencia (AI) del proyecto se realizó en base a lo expuesto en la “ _Guía áreas de_
_influencia en ecosistemas marinos_ ”, donde se señala que para la descripción general del AI, además de considerar
la variabilidad estacional, será crucial describir la evolución de los componentes en su escenario más desfavorable.
Esto, considerando que la aplicabilidad de las guías y criterios de evaluación se fundamenta entre otros, en el
principio preventivo y precautorio, cuyo fin es considerar una condición extrema con el fin de reforzar la prevención
y así evitar la producción de daños ambientales [2] . Por tanto, y con el fin de evaluar dicha condición, se consideraron
escenarios de máximo caudal y máxima concentración para invierno y verano en sicigia y cuadratura (mayor y
menor dinámica de corrientes, respectivamente).

Para la determinación del área de influencia no se consideraron los treinta días de modelación, ya que se sitúan
en un contexto donde las condiciones extremas de la hidrodinámica del sector, específicamente las fases de sicigia
y cuadratura no son apreciables. Esto se debe a que dichas condiciones extremas quedan aminoradas por el
comportamiento hidrodinámico normal, producto de que la frecuencia de ocurrencia de amplitudes de marea
extremas (sicigia y cuadratura) son menores respecto a las condiciones normales, lo que resulta en una atenuación
del comportamiento general de las corrientes resultantes de los procesos de vaciante y llenante. Como resultado,
la pluma de dispersión al ser más estable no presentaría cambios significativos, haciendo menos probable la
identificación de zonas con acumulación de concentraciones de la descarga. Por ende, se considera una mejor
opción evaluar los escenarios extremos de sicigia y cuadratura, basándose en la aplicabilidad de los principios
preventivo y precautorio que aspiran a anticipar y mitigar los efectos adversos en situaciones extremas.

De acuerdo con lo anterior y una vez considerado que los escenarios más desfavorables para la evaluación
ambiental son sicigia y cuadratura, se consideró que la forma de estimar una condición aún más crítica es
realizando las superposiciones máximas de las concentraciones de los escenarios de sicigia y cuadratura, ya que
en ellos es posible evaluar las corrientes más rápidas y menos dinámicas, respectivamente. Por ello, es
fundamental obtener una representación de la situación más adversa de la pluma del efluente. Debido a esto, se
generó una metodología capaz de combinar los resultados de ambas condiciones (sicigia y cuadratura) y de
invierno y verano. Con ello se proporciona un escenario resultante que no solo refleja la máxima área de dispersión,
sino que también la máxima concentración y variabilidad, presentando así una condición más crítica y completa
para el análisis.

En primera instancia se deben obtener los máximos de sicigia y cuadratura, los que posteriormente dan paso a
calcular los máximos de invierno y verano, con los cuales se estima la concentración máxima total. La siguiente
ecuación presenta el cálculo de las concentraciones máximas, que posteriormente generarán la pluma máxima de
dispersión o de área de influencia total de la descarga.

Cmax = max⁡(max(is, ic), max(vs, vc)) (1)

Dónde:

Cmax : Concentración máxima.

is: Concentración en invierno sicigia.

ic: Concentración en invierno cuadratura.

2 ORD. N°202399102593. Imparte instrucciones sobre la aplicabilidad de las guías y criterios de evaluación publicados por la Dirección Ejecutiva
del Servicio de Evaluación Ambiental.

27

Marzo 2024

vs: Concentración en verano sicigia.

vc: Concentración en verano cuadratura.

Cabe destacar que no se superpusieron las tres condiciones (sicigia, cuadratura y corrientes completas) ya que no
es teóricamente correcto, debido a que las condiciones de sicigia y cuadratura ya se encuentran contenidas o
incluidas al evaluar la modelación de 30 días, de realizarse, conllevaría como resultado evaluar dichas condiciones
3 veces cada una, ya que en el mes existen dos sicigias y dos cuadraturas y anteriormente ya se evaluó la sicigia
y cuadratura más extrema.

Finalmente, al superponer los resultados derivados de las diversas modelaciones, se podrá determinar el área de
influencia correspondiente a la situación más crítica para cada parámetro, así como identificar la condición más
adversa del proyecto para la evaluación ambiental de impactos. Esta última se define como el área de influencia
total resultante de la combinación de las condiciones de sicigia y cuadratura para todos los parámetros. Por esta
razón, el área de influencia asociada a la descarga se mantiene conforme a lo expuesto en el proceso de ADENDA
del proyecto, asegurando una evaluación precisa y coherente con los parámetros establecidos.

28

Marzo 2024

### 5.0 RESULTADOS

A continuación, se presentan los resultados tanto del modelo hidrodinámico (calibración y validación) como de la
dispersión de la pluma de descarga del efluente proveniente de la piscicultura de recirculación Aucha.

### 5.1 Modelo Hidrodinámico

**5.1.1** **Calibración y validación del modelo Hidrodinámico**

Con el fin de asegurar una representación general de las condiciones hidrodinámicas del sector del proyecto, las
corrientes generadas en el modelo producto de la incorporación de información de entrada como mareas, vientos,
ríos, radiación, nubosidad entre otros; fueron validadas por medio de las corrientes registradas en las
inmediaciones del punto de descarga por medio de los ADCP tanto de invierno como de verano.

Para ello, se utilizaron el coeficiente de regresión, las desviaciones estándar, el coeficiente de determinación, el
índice BIAS, el error absoluto medio (MAE) y la raíz de los errores promedios al cuadrado (RSME). La información
de corrientes tanto brutas (sin procesar) como procesadas de invierno y de verano, se encuentran en el “Anexo VI

- Informe de Modelación - Correntometrías”.

En ellas se encontró que los promedios y desviaciones estándar de las series de tiempo de corrientes obtenidas
del modelo hidrodinámico representan de manera general las condiciones del sector. En la tabla a continuación se
presentan los índices estadísticos antes mencionados tanto para invierno como para verano.

**Tabla 8: Índices de correlación invierno**

29

|Invierno|Col2|Col3|
|---|---|---|
|índice|ADCP|Modelo|
|Promedio|8,84 [cm/s]|5,64 [cm/s]|
|D. estándar|5,51 [cm/s]|3,97 [cm/s]|
|Coef. Regresión|0,64|0,64|
|Coef. R^2|0,92|0,92|
|BIAS|-3,20 [cm/s]|-3,20 [cm/s]|
|MAE|5,06 [cm/s]|5,06 [cm/s]|
|RMSE|6,43 [cm/s]|6,43 [cm/s]|

Marzo 2024

**Tabla 9: Índices de correlación verano**

|Verano|Col2|Col3|
|---|---|---|
|Índice|ADCP|Modelo|
|Promedio|11,13 [cm/s]|4,22 [cm/s]|
|D. estándar|9,75 [cm/s]|2,53 [cm/s]|
|Coef. Regresión|0,23|0,23|
|Coef. R^2|0,90|0,90|
|BIAS|-6,92 [cm/s]|-6,92 [cm/s]|
|MAE|7,97 [cm/s]|7,97 [cm/s]|
|RMSE|12,40 [cm/s]|12,40 [cm/s]|

De acuerdo con los análisis antes presentados, es posible observar que las corrientes de invierno son mejor
representadas que las corrientes de verano. Aun así, las series de tiempo de corrientes registradas por los ADCP
y el modelo hidrodinámico son similares entre sí. En cuanto al índice BIAS para invierno este fue de -3,2 [cm/s] y
para verano de -6,92 [cm/s], lo que indica una subestimación de las velocidades de las corrientes por parte del
modelo. Incluso así, para verano esto implica una peor condición para las concentraciones del efluente, ya que la
dispersión y la dilución es menor.

Las principales variables que caracterizan y, por lo tanto, describen la naturaleza de la hidrodinámica de un sector
objetivo son la magnitud y variación de las mareas, la magnitud y dirección de las corrientes y la temperatura del
agua (Belyaev _et al_ ., 2019; Matsumoto _et al_ ., 2000). Con el objetivo de relacionar y validar, en mayor detalle, los
resultados obtenidos a través de la modelación hidrodinámica con los datos de campo medidos por el ADCP, se
procedió a analizar las mareas, corrientes y temperaturas.

Para el caso del nivel del mar (mareas), se realizó una correlación directa, la cual se muestra a continuación:

**Figura 12: Comparación del nivel del mar medido v/s modelado.**

30

Marzo 2024

**Figura 13: Correlación directa del nivel del mar medido v/s modelado.**

Respecto al nivel del mar (mareas), la correlación directa entre lo registrado (ADCP) y lo modelado entrega un
coeficiente de correlación R [2] (cuadrado del Coeficiente de Pearson) de 0,987, lo que demuestra que las mareas
en el modelo se ajustan al comportamiento de las mareas registradas en el sitio de estudio.

Por otro lado, es conocido que los escenarios proyectados por modelos se ajustan bastante a la realidad, sin
embargo, no la representan en su totalidad (IPCC 2019). Esto se debe principalmente a eventos estocásticos que
ocurren en el ambiente y a las limitaciones tecnológicas actuales. Por lo tanto, para relacionar, y así validar, los
resultados obtenidos a través de la modelación hidrodinámica con los datos de corrientes medidos por el ADCP,
se realizó una correlación de los percentiles de las magnitudes y direcciones presentadas por el modelo con
respecto a las registradas en el ADCP para ambos escenarios (invierno y verano), la cual se muestra a

continuación.

**Invierno**

**Figura 14: Correlación de distribución en invierno de magnitud (izquierda) y dirección (derecha) entre lo**
**registrado v/s modelado.**

31

Marzo 2024

**Verano**

**Figura 15: Correlación de distribución en verano de magnitud (izquierda) y dirección (derecha) entre lo**
**registrado v/s modelado.**

De igual modo, se compararon las temperaturas registradas a lo largo del periodo de medición del instrumento
ADCP y las temperaturas proyectadas por el modelo hidrodinámico en ambas estaciones del año (invierno y
verano). Los patrones de la temperatura _in situ_ son similares a los proyectados por el modelo, permaneciendo casi
constantes en el tiempo. La diferencia entre temperatura _in situ_ y modelada en invierno corresponde a un 1,26 [°C]
en promedio. La pequeña diferencia de temperatura entre el modelo hidrodinámico y lo medido _in situ_, sugiere la
correcta proyección del modelo respecto a la hidrodinámica del sector estudiado.

**Figura 16: Comparación temporal de temperatura en escenario invierno**

En cuanto a la diferencia de temperatura en el escenario de verano, se puede apreciar que la temperatura obtenida
del modelo se encuentra por encima de la registrada por el ADCP en promedio en 1,15 [°C], lo que corresponde a
una diferencia porcentual de un 9%, lo que indica que el modelo fue capaz de representar de manera correcta la
temperatura en el sector donde se desarrollará el proyecto. A su vez, en la Figura 17 es posible observar que la

32

Marzo 2024

serie de tiempo de temperatura registrada por el ADCP posee variaciones significativas con incrementos de
temperatura perceptibles en ciertos intervalos de tiempo.

**Figura 17: Comparación temporal de temperatura en escenario verano**

### 5.2 Modelo Lagrangiano

**5.2.1** **Campo cercano**

Los resultados del campo cercano se centran en la rápida dilución que ocurre en los primeros metros de la
descarga, donde se observa una reducción del 67,2%, 75,6% y 51,4% en las concentraciones vertidas de los
parámetros NT, PT y DBO 5, respectivamente. Es importante destacar que estos porcentajes representan las
disminuciones mínimas posibles, ya que se consideró la concentración final más alta en el campo cercano,
obteniendo así el escenario más desfavorable. En condiciones favorables, la disminución de las concentraciones

podría ser aún mayor que la mencionada, lo que indica que podrían lograrse disminuciones de concentración aún
más significativas.

En la tabla a continuación se presenta una comparación de la concentración de la descarga respecto a la menor
dilución en el campo cercano.

**Tabla 10: Comparación entre concentración de descarga y concentración final en el campo cercano**

|Parámetro|NT [mg/L]|PT [mg/L]|DBO [mg/L]<br>5|
|---|---|---|---|
|Concentración de descarga|5,4|0,9|10,7|
|Concentración final campo cercano|1,8|0,22|5,2|
|Disminución de concentración mínima|67,2%|75,6%|51,4%|

Como representación de esto, se obtuvieron resultados gráficos de las plumas de dispersión y dilución en el campo
cercano para los parámetros NT, PT y DBO 5 evaluados (Figura 18 a) y b), Figura 19 c)), además de la pluma
general (Figura 19 d)), donde se puede apreciar la nube de partículas que emite el difusor del modelo lagrangiano.

33

Marzo 2024

**Figura 18: Plumas de dilución y dispersión campo cercano parámetros a) NT y b) PT**

**Figura 19: Plumas de dilución y dispersión campo cercano parámetro c) DBO** **5** **y d) pluma de integración**

**de todos los parámetros**

Para estimar la distancia máxima de desplazamiento al que se verán afectadas las partículas desde su emisión en
el campo cercano respecto a su punto de origen, se utilizó la distancia euclidiana. Como resultado, se calculó una
distancia máxima de desplazamiento de 2,75 m desde el punto de emisión en el difusor.

34

Marzo 2024

**5.2.2** **Campo lejano**

Los resultados del campo lejano o de dispersión del efluente que se presentan a continuación, se encuentran
divididos por los escenarios de invierno y verano, por parámetro evaluado (NT, PT y DBO 5 ) y a su vez por las
condiciones de modelación de 30 días, sicigia y cuadratura.

_**5.2.2.1**_ **Invierno**

**5.2.2.1.1** **Nitrógeno Total (NT)**

Tal como se comentó anteriormente, los difusores permiten la dilución rápida en las cercanías de la salida de la
descarga (campo cercano). El efecto de la velocidad de salida de la descarga con los difusores, y la diferencia de
densidad entre el efluente, provocan que la pluma de dispersión se dirija hacia la superficie con bajas
concentraciones. Para el caso del nitrógeno total, a continuación, se presentan las concentraciones con las que
llega a superficie para el periodo de invierno; las que son llamadas también, concentraciones en superficie en el
inicio del campo lejano.

**Tabla 11: Concentraciones iniciales del campo lejano en invierno para NT**

|Escenario|Descarga [mg/L]|Concentración inicial en el<br>campo lejano [mg/L]|
|---|---|---|
|Modelación 30 días|5,4|1,60|
|Sicigia|Sicigia|1,60|
|Cuadratura|Cuadratura|1,77|

**Modelación** **ciclo** **lunar** **completo (30 días)**

En la figura a continuación se presenta la pluma de dispersión del efluente en conjunto con las isolíneas de
concentración considerando el parámetro Nitrógeno Total (NT) para 30 días continuos de modelación, cuya área
de dispersión es de 177.203 [m [2] ].

35

Marzo 2024

**Figura 20: Pluma de dispersión de Nitrógeno Total en invierno con modelación de 30 días**

**Modelación** **sicigia**

En cuanto al escenario de sicigia, la pluma de dispersión se presenta en la Figura 21 con sus respectivas isolíneas
de concentración. Su área es de 134.177 [m2].

**Figura 21: Pluma de dispersión de Nitrógeno Total en invierno con modelación de sicigia**

36

Marzo 2024

**Modelación** **cuadratura**

Finalmente, se presentan los resultados de la pluma de dispersión con sus respectivas isolíneas de concentración
en el escenario de cuadratura. El área corresponde a 25.955 [m [2] ].

**Figura** 22 **: Pluma de dispersión de Nitrógeno Total en invierno con modelación de cuadratura**

**5.2.2.1.2** **Fósforo Total (PT)**

Para el caso del Fósforo Total, las concentraciones a la que llegan a superficie, o bien, las concentraciones iniciales
en el campo lejano son las siguientes:

**Tabla 12: Concentraciones iniciales del campo lejano en invierno para PT**

|Escenario|Descarga [mg/L]|Concentración inicial en el campo<br>lejano [mg/L]|
|---|---|---|
|Modelación 30 días|0,9|0,091|
|Sicigia|Sicigia|0,093|
|Cuadratura|Cuadratura|0,096|

**Modelación ciclo lunar completo (30 días)**

En la figura a continuación se presenta la pluma de dispersión del efluente en conjunto con las isolíneas de
concentración considerando el parámetro Fósforo Total (PT) para la modelación de ciclo lunar completo, cuya área
es de 156.607 [m [2] ].

37

Marzo 2024

**Figura 23: Pluma de dispersión de Fósforo Total en invierno con modelación de 30 días**

**Modelación sicigia**

En cuanto al escenario de sicigia, la pluma de dispersión se presenta en la Figura 24 con sus respectivas isolíneas
de concentración. Su área es de 138.619 [m2].

**Figura 24: Pluma de dispersión de Fósforo Total en invierno con modelación de sicigia**

**Modelación** **cuadratura**

Por último, en la Figura 25 se presentan los resultados del escenario de cuadratura para fósforo total. El área
corresponde 26.639 [m2].

38

Marzo 2024

**Figura 25: Pluma de dispersión de Fósforo Total en invierno con modelación de cuadratura**

**5.2.2.1.3** **Demanda Bioquímica de Oxígeno en 5 días (DBO** **5** **)**

Para el caso de la DBO 5, las concentraciones a las que llegan a superficie, o bien, las concentraciones iniciales en
el campo lejano son las siguientes:

**Tabla 13: Concentraciones iniciales del campo lejano en invierno para DBO** **5**

|Escenario|Descarga [mg/L]|Concentración inicial en el<br>campo lejano [mg/L]|
|---|---|---|
|Modelación 30 días|10,7|2,39|
|Sicigia|Sicigia|2,41|
|Cuadratura|Cuadratura|2,56|

**Modelación** **ciclo** **lunar** **completo (30 días)**

En la figura a continuación se presenta la pluma de dispersión del efluente en conjunto con las isolíneas de
concentración considerando el parámetro DBO 5 para la modelación de ciclo lunar completo, cuya área es de
199.779 [m2].

39

Marzo 2024

**Figura 26: Pluma de dispersión de DBO** **5** **en invierno con modelación de 30 días**

**Modelación sicigia**

En cuanto al escenario de sicigia, la pluma de dispersión se presenta en la Figura 27 con sus respectivas isolíneas
de concentración. El área corresponde a 149.935 [m2].

**Figura 27: Pluma de dispersión de DBO** **5** **en invierno con modelación de sicigia**

**Modelación cuadratura**

Por último, en la figura 15 se presentan los resultados del escenario de cuadratura para DBO 5 . Su área es de
32.099 [m2].

40

Marzo 2024

**Figura 28: Pluma de dispersión de DBO** **5** **en invierno con modelación de cuadratura**

_**5.2.2.2**_ _**Verano**_

**5.2.2.2.1** **Nitrógeno Total (NT)**

A continuación, se presentan las concentraciones de Nitrógeno Total (NT) en superficie en el inicio del campo
lejano, para el período de verano.

**Tabla 14: Concentraciones iniciales del campo lejano en verano para NT**

|Escenario|Descarga [mg/L]|Concentración inicial en el<br>campo lejano [mg/L]|
|---|---|---|
|Modelación 30 días|5,4|1,36|
|Sicigia|Sicigia|1,90|
|Cuadratura|Cuadratura|1,55|

**Modelación ciclo lunar completo (30 días)**

En la figura a continuación se presenta la pluma de dispersión del efluente en conjunto con las isolíneas de
concentración considerando el parámetro Nitrógeno Total (NT) para 30 días de modelación, cuya área es de
128.602 [m [2] ].

41

Marzo 2024

**Figura 29: Pluma de dispersión de Nitrógeno Total en verano con modelación de 30 días**

**Modelación sicigia**

En cuanto al escenario de sicigia, la pluma de dispersión se presenta en la Figura 30 con sus respectivas isolíneas
de concentración. El área corresponde a 83.668 [m [2] ].

**Figura 30: Pluma de dispersión de Nitrógeno Total en verano con modelación de sicigia**

**Modelación cuadratura**

Finalmente, se presentan los resultados del escenario de cuadratura en la Figura 31. Su área corresponde a
127.803 [m [2] ].

42

Marzo 2024

**Figura 31: Pluma de dispersión de Nitrógeno Total en verano con modelación de cuadratura.**

**5.2.2.2.2** **Fósforo Total (PT)**

Para el caso del Fósforo Total, las concentraciones a la que llegan a superficie, o bien, las concentraciones iniciales
en el campo lejano son las siguientes:

**Tabla 15: Concentraciones iniciales del campo lejano en verano para PT**

|Escenario|Descarga [mg/L]|Concentración inicial en el<br>campo lejano [mg/L]|
|---|---|---|
|Modelación 30 días|0,9|0,14|
|Sicigia|Sicigia|0,20|
|Cuadratura|Cuadratura|0,16|

**Modelación ciclo lunar completo (30 días)**

En la figura a continuación se presenta la pluma de dispersión del efluente en conjunto con las isolíneas de
concentración considerando el parámetro Fósforo Total (PT) para 30 días de modelación, cuya área corresponde
a 116.612 [m [2] ].

43

Marzo 2024

**Figura 32: Pluma de dispersión de Fósforo Total en verano con modelación de 30 días**

**Modelación sicigia**

En cuanto al escenario de sicigia, la pluma de dispersión se presenta en la Figura 33 con sus respectivas
isolíneas de concentración. El área estimada fue de 80.041 [m [2] ].

**Figura 33: Pluma de dispersión de Fósforo Total en verano con modelación de sicigia**

**Modelación cuadratura**

Finalmente, se presentan los resultados del escenario de cuadratura en la Figura 34. Lo que da como resultado
un área de 111.659 [m [2] ].

44

Marzo 2024

**Figura 34: Pluma de dispersión de Fósforo Total en verano con modelación de cuadratura**

**5.2.2.2.3** **Demanda Bioquímica de Oxígeno en 5 días (DBO** **5** **)**

Para el caso de la DBO 5, las concentraciones a las que llegan a superficie, o bien, las concentraciones iniciales en
el campo lejano son las siguientes:

**Tabla 16: Concentraciones iniciales del campo lejano en verano para DBO** **5**

|Escenario|Descarga [mg/L]|Concentración inicial en el<br>campo lejano [mg/L]|
|---|---|---|
|Modelación 30 días|10,7|4,85|
|Sicigia|Sicigia|6,57|
|Cuadratura|Cuadratura|5,40|

**Modelación ciclo lunar completo (30 días)**

En la figura a continuación se presenta la pluma de dispersión del efluente en conjunto con las isolíneas de
concentración considerando el parámetro DBO 5 (PT) para 30 días de modelación. Cuya área de dispersión
corresponde a 128.180 [m [2] ].

45

Marzo 2024

**Figura 35: Pluma de dispersión de DBO** **5** **en verano con modelación de 30 días**

**Modelación sicigia**

En cuanto al escenario de sicigia, la pluma de dispersión se presenta en la Figura 36 con sus respectivas isolíneas
de concentración. El área corresponde 81.024 [m [2] ].

**Figura 36: Pluma de dispersión de DBO** **5** **en verano con modelación de sicigia**

**Modelación cuadratura**

Finalmente, se presentan los resultados del escenario de cuadratura en la Figura 37, lo cual dio como resultado
un área de 122.231 [m [2] ].

46

Marzo 2024

**Figura 37: Pluma de dispersión de DBO** **5** **en verano con modelación de cuadratura**

### 5.3 Definición del Área de influencia

**5.3.1** **Análisis de los escenarios modelados**

Como fue mencionado, para la definición del área de influencia, se realizó un análisis de los escenarios modelados
enfocándose en los escenarios de invierno y verano, bajo las condiciones de sicigia y cuadratura. Estas condiciones
se destacan por ser más desfavorables para la dispersión y dilución de las descargas. Adicionalmente, con el
propósito de establecer una base de comparación, se revisaron y contrastaron los resultados relativos a las áreas
de dispersión y las curvas de decaimiento bajo las condiciones previamente descritas, frente al escenario de 30

días.

_**5.3.1.1**_ **Nitrógeno Total**

A continuación, se presentan las concentraciones de nitrógeno total que llegan a la superficie, superpuestas para
las máximas concentraciones y dispersión entre a) invierno y b) verano; en sicigia y cuadratura.

**Tabla 17: Concentraciones iniciales del campo lejano en superficie para NT invierno y verano**

|Estacionalidad|Concentración inicial en el campo lejano [mg/L]|
|---|---|
|Invierno|1,77|
|Verano|1,90|

Las áreas de la pluma de dispersión para cada estación (invierno y verano) superpuestas de sicigia y cuadratura,
se presentan a continuación. Se incluye además en las figuras las proyecciones desde el punto de descarga que
fueron consideradas para obtener las curvas de decaimiento (norte, sur, este, oeste).

47

Marzo 2024

**Figura 38: Pluma de dispersión máxima para NT en invierno considerando sicigia y cuadratura.**

**Figura 39: Pluma de dispersión máxima para NT en verano considerando sicigia y cuadratura.**

Finalmente, en la siguiente Figura se presenta el área de dispersión total de nitrógeno total considerando todos los
escenarios estudiados en la modelación (máximos superpuestos de invierno y verano en sicigia y cuadratura).

48

Marzo 2024

**Figura 40: Área de dispersión total (sicigia y cuadratura en verano e invierno) de NT**

En la siguiente tabla se presenta el valor de las áreas de dispersión de sicigia-cuadratura superpuestas para los
escenarios de invierno y verano, y el total de ambos escenarios.

**Tabla 18: Áreas de plumas de dispersión del parámetro NT**

|Escenario|Área [m2]|
|---|---|
|Área de pluma de dispersión en invierno|158.218|
|Área de pluma de dispersión en verano|139.481|
|Área de la pluma de dispersión superpuesta total|188.946|

A continuación, se presentan los resultados que muestran las distancias que alcanza la pluma de dispersión y su
decaimiento a lo largo del recorrido en las cuatro direcciones presentadas (N, E, S y W). La Tabla 19 incluye dos
alcances como se mencionó anteriormente: (a) la distancia máxima que iguala la pluma de dispersión hasta igualar
la concentración del medio receptor considerando la variabilidad de los datos del medio (+σ); y b) la distancia

máxima que alcanza la pluma de dispersión hasta igualar la concentración promedio del medio receptor.

49

Marzo 2024

**Tabla 19: Distancias de igualación condición máxima sicigia-cuadratura para invierno y verano**

|NT|Invierno|Col3|Verano|Col5|
|---|---|---|---|---|
|Dirección|Distancia que<br>alcanza la pluma de<br>dispersión hasta el<br>valor del medio + σ<br>(variabilidad del<br>medio receptor) [m]|Distancia que alcanza<br>la pluma de dispersión<br>hasta el valor del<br>medio [m]|Distancia que<br>alcanza la pluma de<br>dispersión hasta el<br>valor del medio + σ<br>(variabilidad del<br>medio receptor) [m]|Distancia que alcanza<br>la pluma de dispersión<br>hasta el valor del<br>medio [m]|
|Norte|0 <br>(Se encuentra dentro<br>de la variabilidad del<br>medio marino)|195|165|208|
|Este|Este|417|27|418|
|Sur|Sur|301|23|207|
|Oeste|Oeste|82|36|258|

A continuación, en las Figura 41 y Figura 42 se presentan las curvas de decaimiento de los escenarios de invierno
y verano para las condiciones máximas superpuestas de sicigia y cuadratura, en conjunto con el escenario de 30
días, de tal manera de comparar visualmente las diferencias de concentraciones. A simple vista es posible apreciar
que en el escenario de invierno ambas curvas ya se encuentran dentro de la desviación estándar de las
concentraciones de medio, por lo que se puede decir que estas ya se encuentran asimiladas.

A su vez, en verano las concentraciones iniciales del campo lejano son mucho mayores en la condición
superpuesta, mientras que en los 30 días ya se encuentran atenuadas. Aun así, la condición superpuesta presenta
un escenario más crítico en cuanto a concentraciones, al ser mucho mayores a las estimadas a partir de la
modelación de 30 días, por ende, es una condición que comprende una condición más crítica para la evaluación.

50

Marzo 2024

**Curvas de decaimiento NT invierno**

**Figura 41: Curvas de decaimiento del parámetro NT invierno (Norte, Este, Sur y Oeste)**

51

Marzo 2024

**Curvas de decaimiento NT verano**

**Figura 42: Curvas de decaimiento del parámetro NT verano (Norte, Este, Sur y Oeste)**

52

Marzo 2024

_**5.3.1.2**_ _**Fósforo Total**_

Para el caso del Fósforo Total, las concentraciones a la que llegan a superficie, o bien, las concentraciones iniciales
en el campo lejano tanto para sicigia como para cuadratura son las siguientes:

**Tabla 20: Concentraciones iniciales del campo lejano en superficie para PT invierno y verano**

|Estacionalidad|Concentración inicial en el campo lejano [mg/L]|
|---|---|
|Invierno|0,1|
|Verano|0,2|

En relación con las áreas de la pluma de dispersión en invierno y verano, a continuación, se presentan las figuras
para cada uno de los escenarios superpuestos en sicigia y cuadratura. Se incluyen las proyecciones desde el punto
de descarga que fueron consideradas para obtener las curvas de decaimiento (norte, sur, este, oeste).

**Figura 43: Pluma de dispersión máxima para PT en invierno considerando sicigia y cuadratura**

53

Marzo 2024

**Figura 44: Pluma de dispersión para PT en verano considerando sicigia y cuadratura**

Finalmente, en la Figura 45, se presentan ambos escenarios superpuestos (invierno y verano) con el fin de obtener
el área de dispersión máxima correspondiente al fósforo total.

**Figura 45: Área de dispersión total de PT**

54

Marzo 2024

En la siguiente tabla se detallas las áreas de dispersión para las condiciones evaluadas, sicigia más cuadratura,
superpuestas para los escenarios de invierno y verano.

**Tabla 21: Áreas de plumas de dispersión del parámetro PT**

|Escenario|Área [m2]|
|---|---|
|Área de pluma de dispersión en invierno|158.717|
|Área de pluma de dispersión en verano|129.469|
|Área de la pluma de dispersión superpuesta total|188.965|

A continuación, la Tabla 22 presenta los resultados de las distancias de cada escenario para la condición

superpuesta:

**Tabla 22: Distancia en metros a las que las concentraciones de PT igualan el valor del medio receptor**
**medidos desde el punto de descarga para (invierno y verano)**

|PT|Invierno|Col3|Verano|Col5|
|---|---|---|---|---|
|Dirección|Distancia que<br>alcanza la pluma de<br>dispersión hasta el<br>valor del medio + σ<br>(variabilidad del<br>medio receptor) [m]|Distancia que alcanza<br>la pluma de dispersión<br>hasta el valor del<br>medio [m]|Distancia que<br>alcanza la pluma de<br>dispersión hasta el<br>valor del medio + σ<br>(variabilidad del<br>medio receptor) [m]|Distancia que alcanza<br>la pluma de dispersión<br>hasta el valor del<br>medio [m]|
|Norte|13|198|0 <br>(Se encuentra dentro<br>de la variabilidad del<br>medio marino)|198|
|Este|20|418|418|418|
|Sur|0 <br>(Se encuentra dentro<br>de la variabilidad del<br>medio marino)|400|400|196|
|Oeste|Oeste|40|40|215|

A continuación, se presentan las distintas curvas de decaimiento para invierno y verano a lo largo de las direcciones
antes mencionadas. En invierno se aprecia que las concentraciones en el comienzo del campo lejano se
encuentran dentro de los valores del medio, sin embargo, en el escenario máximo superpuesto al alejarse de este
punto (aproximadamente 25 m) para la dirección E y S las concentraciones tienden a aumentar levemente, para
luego volver a disminuir hasta hallarse dentro de la variabilidad de medio. En tanto para verano, las concentraciones
siempre se encuentran dentro de la variabilidad del medio registradas, sin embargo, un punto notable a considerar
es que en el escenario máximo superpuesto las concentraciones al comienzo del campo lejano son mucho mayores
a las obtenidas a partir del modelo de 30 días, sobre todo para la dirección N, donde la distancia que se encuentra
por sobre la curva de 30 días es aproximadamente 150 m.

55

Marzo 2024

**Curvas de decaimiento PT invierno**

**Figura 46: Curvas de decaimiento del parámetro PT invierno (Norte, Este, Sur y Oeste)**

56

Marzo 2024

**Curvas de decaimiento PT verano**

**Figura 47: Curvas de decaimiento del parámetro PT verano (Norte, Este, Sur y Oeste)**

57

Marzo 2024

_**5.3.1.3**_ _**Demanda bioquímica de oxígeno a 5 días**_

Para el caso de la DBO 5, las concentraciones a la que llegan a superficie, o bien, las concentraciones iniciales en
el campo lejano son las siguientes:

**Tabla 23: Concentraciones iniciales del campo lejano en superficie para DBO** **5** **.**

|Estacionalidad|Concentración inicial en el campo lejano [mg/L]|
|---|---|
|Invierno|2,56|
|Verano|6,58|

En la Figura 48 y Figura 49 se presentan las áreas de dispersión de los escenarios invierno y verano con las
condiciones sicigia y cuadratura superpuestas.

**Figura 48: Pluma de dispersión para DBO** **5** **en invierno considerando sicigia y cuadratura.**

58

Marzo 2024

**Figura 49: Pluma de dispersión para DBO** **5** **en verano considerando sicigia y cuadratura.**

Por último, en la siguiente figura se presenta el área de dispersión total considerando todos los escenarios
superpuestos (invierno y verano en sicigia y cuadratura).

**Figura 50: Área de dispersión total de DBO** **5.**

A continuación, se presentan las superficies que abarcan las tres figuras expuestas anteriormente.

59

Marzo 2024

**Tabla 24: Áreas de plumas de dispersión del parámetro DBO** **5**

|Escenario|Área [m2]|
|---|---|
|Área de pluma de dispersión en invierno|172.623|
|Área de pluma de dispersión en verano|132.470|
|Área de la pluma de dispersión superpuesta total|195.144|

A continuación, la Tabla 25 presenta los resultados de las distancias de cada escenario para la condición

superpuesta:

**Tabla 25: Distancia en metros a las que las concentraciones de DBO** **5** **igualan el valor del medio receptor**
**medidos desde el punto de descarga para (invierno y verano)**

|DBO<br>5|Invierno|Col3|Verano|Col5|
|---|---|---|---|---|
|Dirección|Distancia que<br>alcanza la pluma de<br>dispersión hasta el<br>valor del medio + σ<br>(variabilidad del<br>medio receptor) [m]|Distancia que alcanza<br>la pluma de dispersión<br>hasta el valor del<br>medio [m]|Distancia que<br>alcanza la pluma de<br>dispersión hasta el<br>valor del medio + σ<br>(variabilidad del<br>medio receptor) [m]|Distancia que alcanza<br>la pluma de dispersión<br>hasta el valor del<br>medio [m]|
|Norte|75|198|178|198|
|Este|28|418|28|418|
|Sur|82|400|24|196|
|Oeste|19|43|44|222|

A continuación, se presentan las distintas curvas de decaimientos para invierno y verano, a lo largo de las
direcciones antes mencionadas. En ellas se puede observar la notable variación de las concentraciones al
comienzo del campo lejano en la superposición máxima de sicigia y cuadratura respecto a la de 30 días, donde
ocurre algo similar a la modelación de NT, incrementando relevantemente en el escenario de verano en todas las

direcciones.

60

Marzo 2024

**Curvas de decaimiento DBO** **5** **invierno**

**Figura 51: Curvas de decaimiento del parámetro DBO** **5** **invierno (Norte, Este, Sur y Oeste)**

61

Marzo 2024

**Curvas de decaimiento DBO** **5** **verano**

**Figura 52: Curvas de decaimiento del parámetro DBO** **5** **verano (Norte, Este, Sur y Oeste)**

62

Marzo 2024

**5.3.2** **Área de influencia componente calidad de agua**

El área de influencia del componente de calidad de agua relacionado con el efluente de descarga de la Piscicultura
Aucha consiste en la superficie máxima que abarca la pluma de dispersión considerando la superposición de los
resultados mencionados anteriormente para los escenarios, condiciones y parámetros evaluados. Considerando
lo anterior, el área de influencia del componente calidad de agua es de 201.960 [m [2] ] y se representa de la siguiente

forma.

**Figura 53: Área de influencia de la descarga en el cuerpo de agua marino**

A continuación, se presentan los máximos alcances que presenta el área de influencia.

**Tabla 26: Máximos alcances del área de influencia de la descarga en el cuerpo de agua marino**

63

|Dirección|Distancia máxima del área de influencia [m]|
|---|---|
|Norte|198|
|Este|418|
|Sur|400|
|Oeste|222|

Marzo 2024

### 6.0 DISCUSIÓN

El objetivo del presente estudio es simular el comportamiento de la pluma de dispersión proveniente de la descarga
de efluentes del proyecto “Ampliación piscicultura de recirculación Aucha”.

Los resultados del comportamiento de la pluma de dispersión del efluente tratado de la piscicultura Aucha se basan
en la modelación de escenarios de invierno y verano, y en los ciclos mareales que tienen una mayor influencia en
la dispersión, específicamente en sicigia y cuadratura, así como también una condición normal de un mes (ciclo
lunar completo) para los parámetros de Nitrógeno total (NT), Fósforo total (PT) y DBO 5 . La modelación permitió
obtener áreas de dispersión de la pluma para cada uno de los parámetros evaluados en cada uno de los escenarios
y condiciones mencionadas.

Tras obtener los resultados de las concentraciones y dispersión de la pluma, fue posible aseverar que la condición
de 30 días de modelación es la que presenta la menor variación en cuanto a concentraciones en todos los
parámetros y en todos los escenarios, por tanto, es el escenario menos extremo. En cambio, sicigia, cuadratura y
su superposición máxima exponen una mayor variación en cuanto a las concentraciones de los parámetros, y de
igual forma, en su mayoría, presentan un área de dispersión superpuesta mayor en ciertas direcciones que en la

modelación de 30 días.

**Modelación hidrodinámica**

La modelación hidrodinámica para el sector del proyecto fue sometida a los procesos de calibración y validación,
y para esto se realizó una comparación entre las corrientes generadas por el modelo y las corrientes registradas
por los ADCP tanto para la época de invierno como de verano.

Respecto a la correntometría utilizada para calibrar y validar el modelo hidrodinámico, es importante destacar que
en los registros de ADCP del escenario de verano, se observó una magnitud promedio de 11 cm/s, lo cual es mayor
en comparación a lo observado en invierno. Mientras que, en la modelación hidrodinámica, es posible apreciar que
no existe mayor diferencia entre el promedio de las magnitudes de corrientes de invierno y verano. Esto es debido
a los eventos estocásticos que ocurren en el ambiente, las limitaciones tecnológicas, y al hecho de que un modelo
numérico depende de la cantidad de información de entrada; por ello es por lo que se pueden presentar leves
desviaciones de los resultados de la modelación respecto a las mediciones del registro.

La combinación de todos los fenómenos aleatorios que influyen en la generación de la hidrodinámica implica que
a cualquier modelo numérico le suponga un desafío para representar en su totalidad las condiciones del sector, lo
cual queda en evidencia al registrarse velocidades promedio de 11 cm/s en verano, lo que es una condición poco
común para la zona. Esto queda en evidencia según lo expuesto en el informe del IFOP (2018) titulado “ _Modelación_
_de Alta Resolución Aplicada al Transporte Hidrodinámico, al interior del Mar Interior de Chiloé, X Región de Los_
_Lagos_ ”. En el mencionado estudio se realizaron modelaciones hidrodinámicas tanto para invierno como para
verano en toda la región, donde es posible apreciar que, al igual que en las modelaciones realizadas en el presente
proyecto, no existe una gran diferencia entre las magnitudes de corriente de ambas estaciones (invierno y verano).
Junto con lo anterior, al utilizar la herramienta ATLAS de la plataforma CHONOS, es posible obtener la información
de las magnitudes medias de un mes en particular, que para este caso y como forma comparativa, se utilizó agosto
de 2020, donde se presenta un resultado medio de la capa superficial de 0,055 m/s o 5,5 cm/s, lo cual se encuentra
próximo al resultado obtenido de la modelación hidrodinámica presentada en este informe de modelación de 5,64
cm/s. De igual manera para verano (marzo 2021), en la plataforma ATLAS se obtuvo una magnitud promedio de
0,057 m/s (5,7 cm/s), mientras que en los resultados del modelo se obtuvo una magnitud promedio de 4,22 cm/s.
Cabe destacar que las modelaciones realizadas por el IFOP se encuentran dentro del marco de un estudio

64

Marzo 2024

científico, por lo que poseen un mayor volumen de información de entrada provenientes de varias campañas _in_
_situ_, lo que puede derivar en que su modelo tenga una mayor aproximación.

Es importante mencionar que, pese a que el modelo proyectó magnitudes de corrientes levemente inferiores a las
medidas por el ADCP, esta proyección favorece la perspectiva de peor escenario ambiental, lo cual permite realizar
una adecuada evaluación de los potenciales impactos producto de la descarga en el medio acuático. Es decir,
menores magnitudes de corrientes disminuirían la capacidad de dilución del medio, lo que favorecería la retención
de la pluma de dispersión y permanencia de sus concentraciones. Esto maximizaría la probabilidad de proyectar
un escenario ambiental adverso para el medio ambiente. Del mismo modo, la pequeña diferencia de temperaturas
de fondo entre las mediciones _in situ_ y las proyectadas sugieren una probable subestimación de la mezcla vertical
en el modelo hidrodinámico, lo cual disminuiría la capacidad de dilución del medio, favoreciendo la retención de la
pluma de dispersión y permanencia de sus concentraciones, proyectando el escenario ambiental más

_desfavorable._

En cuanto a las condiciones de sicigia y cuadratura, dichos factores se relacionan con las fases mareales, de las
cuales en sicigia se presentan las mayores variaciones de la marea entre pleamares y bajamares, mientras que
cuadratura presenta las menores variaciones. La combinación de estos factores que influyen en las corrientes
marinas, junto con las ecuaciones del modelo hidrodinámico, que involucran procesos físicos de advección y
difusión, relacionados con la condición del medio y del efluente son los que finalmente determinan el
comportamiento de la pluma de descarga en términos de su alcance y dilución . Ahora bien, como fue mencionado,
las corrientes generadas en el modelo al estar subestimadas permitieron evaluar una condición aún más
desfavorable en términos de dispersión, ya que las concentraciones del efluente se mantienen una mayor cantidad
de tiempo en el sector, lo que al evaluar la influencia de la pluma en términos de la biodiversidad es una situación

más crítica.

**Modelación Lagrangiana**

Es importante resaltar que los resultados obtenidos consideraron una caracterización del efluente (caudal y
concentración) bajo un caso hipotético, con el fin de evaluar la pluma de dispersión y área de influencia en el medio
marino bajo las condiciones más desfavorables, en relación con el efluente a descargar. En este caso hipotético,
se combinaron las concentraciones más altas obtenidas a partir del cálculo de un balance de masa en un escenario
de máxima emisión de la piscicultura, junto con el caudal máximo posible a descargar (429 L/s). Es importante
tener en cuenta que estas condiciones no se darían de manera simultánea durante el desarrollo del proyecto, no
obstante, en la presente modelación se evaluó la descarga considerando la combinación de ambas condiciones
para proyectar y analizar un escenario de peor condición.

Para complementar la modelación hidrodinámica se empleó el módulo lagrangiano, con el propósito de estimar la
dispersión de los nutrientes que serán liberados al mar a través de un emisario submarino. Tal como se mencionó
en la sección 3.2, el emisario cuenta en total con 15 difusores que permiten la dilución del efluente en el cuerpo
receptor. La primera fase de dilución ocurre en el campo cercano, en el cual se produce la mayor dilución en las
concentraciones de los parámetros evaluados, tal como se presentó en la Tabla 10. Al mismo tiempo, en las
Figura 18 y Figura 19 se observan las plumas de dispersión en el campo cercano, tanto las de NT, PT y DBO 5
como la pluma de dispersión total. Cada una de las plumas corresponde a la unión de los escenarios invierno
sicigia, invierno cuadratura, verano sicigia y verano cuadratura, para cada uno de los parámetros, lo que significa
que cada una de ellas comprende las condiciones más desfavorables para evaluar la dispersión (tamaño de la
pluma) y dilución (mayor concentración a superficie), ya que tal como se mencionó, en invierno la dispersión es
mayor y en verano la dilución es menor.

65

Marzo 2024

Es necesario hacer énfasis en que la disposición de las partículas en el campo cercano son las mismas para los
tres parámetros simulados, así como también para la pluma total, solo variando las concentraciones que de ellas
se desprenden. Esto se debe a que es el mismo flujo de vertido que contiene los tres parámetros evaluados, por
tanto, es la misma pluma de dispersión.

En relación con los resultados de la pluma de dispersión en el campo lejano, es importante destacar que esta
alcanza la superficie con una concentración muy por debajo de la concentración inicial de la descarga. Las áreas
de la pluma de dispersión de la descarga para los tres parámetros evaluados (NT, PT y DBO 5 ) son mayores en
verano y los mayores alcances se dan en dirección Oeste y Sur, principalmente porque en las otras direcciones la
pluma de descarga se delimita por el alcance de la playa. Estos resultados son coherentes con las condiciones
hidrodinámicas del sector, considerando que en verano existe una menor mezcla y, por tanto, una menor dilución,
lo que se relaciona a un mayor alcance y superficie de la pluma de descarga.

**Área de influencia**

Ahora bien, con los resultados obtenidos, y con el fin evaluar la combinación más desfavorable en cuanto al área
de influencia del proyecto, se consideró para ello la superposición de las concentraciones máximas de los
parámetros NT, PT y DBO 5, en las condiciones de sicigia y cuadratura, y posteriormente las máximas
concentraciones de dichos escenarios de invierno y verano. Una vez obtenidas dichas áreas, se superpusieron
todas las áreas máximas de todos los parámetros para obtener el área total de influencia del proyecto, lo que
equivaldría a considerar una curva envolvente que abarque todas las áreas en sicigia y cuadratura. Este enfoque
permitió analizar de manera más precisa la trayectoria y dispersión de los nutrientes en función de las corrientes
marinas, ofreciendo una visión integral de su comportamiento en el medio acuático.

Considerando la superposición de las superficies mencionadas anteriormente, se puede indicar que el área de
influencia de la descarga en el componente de calidad de agua es de 20,20 [Ha] y que el alcance máximo del área
de influencia en la dirección Norte, Este, Sur y Oeste es de 198, 418, 400 y 222 [m], respectivamente. Al considerar
la variabilidad ( x̅ + σ ), en la calidad de agua como valor de referencia del medio marino respecto a los parámetros

analizados, se puede indicar que, para las condiciones modeladas, las plumas de dispersión disminuyen
considerablemente. Teniendo presente lo anterior, se puede indicar que el mayor decaimiento de la concentración
en la distancia, es decir, la mayor dilución, es en menos de 200 metros en dirección Norte, menos de 50 metros
en dirección Este y Oeste, y en menos de 100 metros en la dirección Sur (82 metros).

Finalmente, es fundamental subrayar la variabilidad del medio respecto a las concentraciones de Nitrógeno Total
(NT), Fósforo Total (PT) y Demanda Bioquímica de Oxígeno a 5 días (DBO 5 ). Esta característica confiere al sector
una elevada capacidad de asimilación ante fluctuaciones en estas concentraciones. Dicha capacidad adquiere
importancia, como se evidenció en las curvas de decaimiento, dado que algunas de las concentraciones emitidas
por el efluente se sitúan ya dentro del rango de variabilidad natural del medio (media aritmética x̅ más la desviación
estándar σ). Esto facilita una pronta integración y estabilización con el cuerpo de agua receptor.

66

Marzo 2024

### 7.0 CONCLUSIÓN

A partir de los objetivos establecidos y los resultados obtenidos de las modelaciones hidrodinámicas de los
escenarios de corrientes, se puede concluir lo siguiente:

### ▪

[La información utilizada para implementar el modelo hidrodinámico proporciona una representación precisa de ]

las condiciones hidrodinámicas del sector del proyecto. Es importante destacar que se consideraron en la
modelación datos relevantes, tales como un campo meteorológico del modelo WRF (Weather Research and
Forecasting), información de salinidad y temperatura obtenida de la aplicación ATLAS de la plataforma
CHONOS, caudales medios mensuales de los diez ríos afluentes más importantes que influyen en el sector,
obtenidos a través de la aplicación FLOW de la plataforma CHONOS, y las condiciones iniciales de borde del
modelo global de mareas FES 2014 (Finite Element Solution). Con esta información, se logra una
representación completa y precisa de las condiciones hidrodinámicas del área de estudio.

### ▪

[Los resultados relacionados con la hidrodinámica del sector revelan que las corrientes y, por ende, el ]

desplazamiento de la pluma de dispersión, están principalmente influenciados por las mareas y los vientos. Es
importante destacar que el viento tiene un impacto preponderante en el desplazamiento de las aguas en la
capa superficial. Además, las mayores velocidades se hallaron en el escenario de invierno sicigia, esto debido
principalmente al efecto del viento en las capas superficiales de la columna de agua, así como el mayor aporte
de agua proveniente de los ríos. En cambio, las menores se encuentran en el escenario de verano cuadratura,
donde el viento disminuye su intensidad y la amplitud de marea es menor.

### ▪

[En cuanto a la modelación lagrangiana, el simular un periodo más extenso (ciclo lunar completo) de la ]

hidrodinámica del sector, conllevó que la variabilidad en las concentraciones fuera menor que para las
condiciones de sicigia y cuadratura superpuesto, ya que, al considerar 30 días de simulación, las condiciones
extremas son atenuadas por períodos de tiempo en que la dinámica del sector no presenta valores extremos.

### ▪

[Los resultados del comportamiento de la pluma de dispersión del efluente tratado de la piscicultura Aucha se ]

basan en la modelación de escenarios tanto en invierno como en verano, considerando los ciclos mareales de

sicigia y cuadratura superpuestos. Los parámetros de nitrógeno total (NT), fósforo total (PT) y DBO 5 fueron
evaluados para obtener áreas específicas de dispersión. En invierno se observaron mayores corrientes debido
a las condiciones meteorológicas, mientras que sicigia y cuadratura se relacionan con las fases mareales y
afectan las variaciones de la marea. La combinación de estos factores, junto con las características del efluente
y las ecuaciones del modelo hidrodinámico que consideran procesos físicos como corrientes ascendentes y
descendentes producto de la variación de densidad y gradientes de presión, determinaron la hidrodinámica del
sector que deriva en el alcance y dilución de la pluma de descarga en el medio marino.

### ▪

[La mayor dilución del vertido ocurre en el campo cercano, es decir, en las inmediaciones del punto de vertido. ]

Debido a la velocidad de salida de la descarga en los difusores, la diferencia de densidad entre el efluente y el
medio receptor y, la ubicación y posición de los difusores, la pluma de dispersión se dirige verticalmente hacia
la superficie, llegando a este estrato con concentraciones muy por debajo que las de la descarga inicial (entre
un 51,4% a 75,6% menos).

### ▪

[Considerando el escenario más desfavorable, la pluma de dispersión abarca una superficie máxima de 18,89 ]

Ha para el parámetro de Nitrógeno total y Fósforo Total, y de 19,5 [Ha] para DBO 5 .

### ▪

[El área de influencia de la descarga proyectada, que está relacionada con el efluente de la piscicultura Aucha, ]

abarca una superficie de 20,201 hectáreas. El alcance máximo del área de influencia en las direcciones Norte,

67

Marzo 2024

Este, Sur y Oeste es de 198, 418, 400 y 222 metros, respectivamente, evidenciando que los límites del área
de influencia del componente calidad de agua son acotados.

### ▪

[Basado en las curvas de decaimiento, se observa que las concentraciones de los parámetros evaluados ]

vertidos al medio son bajas y se sitúan dentro o cerca de la variabilidad natural del entorno acuático. Además,
gracias a la boyantez positiva de la pluma, ésta tiende a ascender y dispersarse predominantemente en las
capas superficiales de la columna de agua, no afectando el lecho marino. Respecto a las porciones que llegan
a la costa, estas se encuentran ya en niveles muy próximos al promedio habitual del medio marino, evidencia
que se respalda tanto en las representaciones gráficas de las plumas de dispersión como en las propias curvas

de decaimiento.

### ▪

[Finalmente, tras analizar las distintas condiciones modeladas de la descarga en el medio receptor, los ]

resultados permiten concluir y ratificar que, de las condiciones evaluadas (condición máxima de Sicigia y
Cuadratura y Condición Ciclo lunar completo - 30 días), la condición máxima de Sicigia y Cuadratura
presentada en Adenda anterior del Proyecto proporciona una peor condición para efectos de evaluar
ambientalmente el proyecto.

68

Marzo 2024

### 8.0 BIBLIOGRAFÍA ▪

[Barreto, I., Ezzatti, P., Fossati, M. (2009). Estudio inicial del modelo MOHID. Facultad de Ingeniería. ]

Universidad de la República, Uruguay.

### ▪

[Belyaev, Konstantin & Kuleshov, A. & Smirnov, Ilya & Tanajura, C. (2019). Comparison of Data Assimilation ]

Methods in Hydrodynamics Ocean Circulation Models. Mathematical Models and Computer Simulations. 11.

564-574. 10.1134/S2070048219040045.

### ▪

[Bravo, L., Silva, N., & Hormazábal, S. (2018). Variabilidad interanual de las corrientes en el mar interior de ]

Chiloé (41° S), Chile: una perspectiva desde datos satelitales y de modelación numérica. Investigaciones
Marinas, 46(2), 195-206

### ▪

[INSTITUTO SUPERIOR TÉCNICO (2006). Water Quality Manual. Technical University of Lisbon. ]

### ▪

[Soto, G., Reche, P., Soto, C., Arriagada, M., Pinilla, E. (2018). Modelación de Alta Resolución Aplicada al ]

Transporte Hidrodinámico, al interior del Mar Interior de Chiloé, X Región de Los Lagos

### ▪

[IPCC, 2019: IPCC Special Report on the Ocean and Cryosphere in a Changing Climate [H.-O. Pörtner, D.C. ]

Roberts, V. Masson-Delmotte, P. Zhai, M. Tignor, E. Poloczanska, K. Mintenbeck, A. Alegría, M. Nicolai, A.
Okem, J. Petzold, B. Rama, N.M. Weyer (eds.)]. Cambridge University Press, Cambridge, UK and New York,
NY, USA, 755 pp. https://doi.org/10.1017/9781009157964.

### ▪

[Kikkert, G. A. (2006). Buoyant jets with two and three-dimensional trajectories. ]

### ▪

[Lyard, F. H., Allain, D. J., Cancet, M., Carrère, L., and Picot, N.: FES2014 global ocean tide atlas: design and ]

performance, Ocean Sci., 17, 615-649, https://doi.org/10.5194/os-17-615-2021, 2021.

### ▪

[Matsumoto, Koji & Takanezawa, Takashi & Ooe, Masatsugu. (2000). Ocean Tide Models Developed by ]

Assimilating TOPEX/POSEIDON Altimeter Data into Hydrodynamical Model: A Global Model and a Regional
Model around Japan. Journal of Oceanography. 56. 567-581. 10.1023/A:1011157212596.

### ▪

[MINISTERIO DEL MEDIO AMBIENTE (2013). Decreto Supremo 40. Aprueba Reglamento del Sistema de ]

Evaluación de Impacto Ambiental.

### ▪

[Moctezuma, I., Chapa, C., Galicia, M. 2012. Simulation of Pollutant Dispersion at Puerto Escondido, Oaxaca ]

México Latin America Transactions. Vol. 10(5).

### ▪

[Pierini, J., Stretenberger, E., Baldini, M. 2012. Evaluation of faecal contamination in Bahía Blanca estuary ]

(Argentina) using a numerical model. Revista de Biología Marina y Oceanografía Vol. 47, No2: 193-202.

### ▪

[Razi, H., Mazaheri, M., Samani, J.M.V., Carvajalino, M. 2016. Investigating Urmia Lake Partial Restoration and ]

Ecological Water Level Using MOHID-2D Water Hydrodynamic Model. University of Tabriz.

### ▪

[Sánchez-Gutiérrez.R., Gómez-Castro, C. (2021). Approaching to water quality modeling processes in a ]

subwatershed. The Virilla River case in Costa Rica. Uniciencia Vol. 35(1), pp. 71-89.

### ▪

[Seiler, L., Fernandes, E., Siegle, E. (2020). Effect of wind and river discharge on water quality indicators of a ]

coastal lagoon. Regional Studies in Marine Science (40)

69

Marzo 2024

### ▪

[Smith, J. M., & Johnson, A. B. (2018). The generation of upwelling and downwelling along the coast due to ]

freshwater discharge. Journal of Coastal Research, 34(3), 678-689. DOI: 10.2112/JCOASTRES-D-17-00094.1

### ▪

[Taboada, J. P.-V.-G. (1998). Evaluation of the seasonal variations in the residual patterns in the Ría de Vigo ]

(NWSpain) by means of a 3D baroclinic model. Estuarine Coastal and Shelf Science 47, pp. 661-670.

### ▪

[Tironi-Silva, A., Marin, V.H., Delgado, L.E. (2014). Un modelo hidrodinámico 3d del humedal del rio cruces: ]

cálculo del tiempo de residencia utilizando MOHID. Aqua-LAC (6), 50-57.

### ▪

[Villarreal, M. (2000). Parametrization of turbulence in the ocean and application of a 3D baroclinic model to the ]

Ría de Pontevedra. Santiago de Compostela: Ph. D. Dissertation, Universidad de Compostela.

70

Marzo 2024

### 9.0 ANEXOS

71

Marzo 2024

**ANEXO A**

# Archivos de entrada y salida del modelo

Marzo 2024

Carpeta: Archivos de entrada y salida del modelo.

Marzo 2024

**ANEXO B**

# Antecedentes

Marzo 2024

### Caudales de los ríos utilizados.

De forma de que el modelo sea representativo de las condiciones locales del sitio del proyecto, se ingresaron en
total 10 ríos afluentes dentro del dominio del modelo, con ellos, el aporte de agua dulce representa cambios en las
densidades de la superficie de la columna de agua propias del sector que, a su vez, generan corrientes
ascendentes y descendentes producto de gradientes verticales de densidad (Smith et al., 2018). Estos ríos se
encuentran entre el Golfo Coronados hasta el Estero de Reloncaví, incluyendo la misma Ensenada Codihue, cuyos
puntos de desembocadura al mar se muestran a continuación:

**Figura 54: Puntos de Desembocadura de los Ríos afluentes considerados en modelación regional (Nivel 1**
**arriba) y Ríos considerados en modelación del sector (Nivel 2 y 3 abajo).**

La información sobre estos caudales se obtuvo a través de la aplicación Flow de la plataforma Chonos del IFOP
[(Instituto de Fomento Pesquero), específicamente desde su sitio web (https://chonos.ifop.cl/flow/, 2023). Estos](https://chonos.ifop.cl/flow/)
caudales fueron aumentados por un 10% para compensar los aportes generados por otros esteros menores y los
que se generan a lo largo de toda la costa de la zona analizada.

Para los ríos que se encuentran adentro de la ensenada Codihue, se utilizó el método de Turc, el cual estima los
caudales en función de temperaturas y precipitaciones, y que, es usado por la DGA

La tabla siguiente presenta los caudales medios mensuales para cada uno de los ríos.

Marzo 2024

**Tabla 27: Caudales medios estimados de los afluentes principales.**

|Caudales (m3/s)|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Río/Mes**|**Ene**|**Feb**|**Mar**|**Abr**|**May**|**Jun**|**Jul**|**Ago**|**Sep**|**Oct**|**Nov**|**Dic**|
|Ancud|23,8|19,6|25,4|48,2|104,2|139,9|140,9|134,6|94,2|62,2|45,7|32,7|
|Maullin|99,9|86,2|81,1|99,9|154,0|205,3|225,3|230,4|201,3|168,6|145,7|122,8|
|Chamiza|43,5|39,8|45,7|71,7|113,9|139,9|132,3|128,7|101,4|81,6|69,7|59,5|
|Chaica|4,0|3,8|4,4|6,6|9,9|12,2|11,5|11,3|8,6|6,9|6,0|5,1|
|Lenca|6,2|5,7|6,6|10,2|15,9|18,7|17,3|17,3|14,2|12,1|10,2|8,4|
|Puelo|480,4|332,7|287,6|427,7|753,8|948,2|937,3|954,2|901,1|848,7|810,5|674,9|
|Cochamo|20,3|15,2|15,5|24,2|40,6|49,9|46,9|46,2|39,8|33,4|31,7|29,3|
|Petrohué|177,5|142,8|140,6|215,4|369,2|473,7|442,3|438,3|376,0|307,5|272,5|244,1|
|Aucha|0,2|0,2|0,3|0,5|0,9|1,3|1,1|1,1|1,5|0,5|0,4|0,4|
|R2|0,1|0,1|0,1|0,2|0,4|0,5|0,5|0,5|0,6|0,2|0,2|0,2|
|Estero Codihue|0,1|0,1|0,1|0,1|0,2|0,4|0,3|0,3|0,4|0,1|0,1|0,1|

### Perfiles de salinidad y temperatura utilizados en la modelación.

Para la modelación hidrodinámica, se utilizaron los perfiles promedio de salinidad y temperatura como condición
de borde inicial tanto en el borde inferior (sur) como en el borde izquierdo (oeste) en el dominio de nivel 1 del
modelo, para ellos se obtuvieron los datos correspondientes a las fechas de medición de corrientes, es decir del
01/08/2020 al 30/09/2020 para invierno, y desde al 01/03/2021 al 01/04/2021 para verano. Estos perfiles fueron
obtenidos a partir de las modelaciones realizadas por el IFOP (Instituto de Fomento Pesquero) en la aplicación
“Atlas” de la página Web “Chonos [3] ” en el mar interior de Chiloé. Los perfiles se presentan a continuación tanto
para invierno como verano en los bordes sur y oeste de la modelación regional de Nivel 1.

3 [https://chonos.ifop.cl/atlas3/view/chiloe](https://chonos.ifop.cl/atlas3/view/chiloe)

Marzo 2024

|Invierno|Col2|
|---|---|
|Sur|Sur|
|Salinidad|Temperatura|
|||

**Figura 55: Perfiles de salinidad y temperatura en la condición de borde Sur período de invierno**

Marzo 2024

|Invierno|Col2|
|---|---|
|Oeste|Oeste|
|Salinidad|Temperatura|
|<br>||

**Figura 56: Perfiles de salinidad y temperatura en la condición de borde Oeste período de invierno**

Marzo 2024

|Verano|Col2|
|---|---|
|Sur|Sur|
|Salinidad|Temperatura|
|||

**Figura 57: Perfiles de salinidad y temperatura en la condición de borde Sur período de verano**

Marzo 2024

|Verano|Col2|
|---|---|
|Oeste|Oeste|
|Salinidad|Temperatura|
|||

**Figura 58: Perfiles de salinidad y temperatura en la condición de borde Oeste período de verano.**

### Información atmosférica.

Para la modelación en MOHID del sector, donde se emplazará el proyecto, se utilizaron datos atmosféricos como
inputs para el módulo hidrodinámico, los cuales constituyen una forzante en el comportamiento hidrodinámico. Las
condiciones de borde utilizadas en el módulo Atmosphere corresponden a datos de viento, precipitación, radiación
solar y temperatura, obtenidos a partir del modelo de simulación atmosférica WRF (Weather Research and
Forecasting), desarrollado por NCAR (Centro Nacional para la investigación Atmosférica), NOAA (Oficina Nacional
de Administración Oceánica y Atmosférica), y AFWA (Agencia de Meteorología de Fuerza Aérea estadounidense).
La información proveniente del modelo WRF considera un dominio 50 por 50 kilómetros de longitud, con lo que se
aseguró cubrir un área de generación de 252 hectáreas aproximadamente. De este modo, se utilizaron datos de
entrada de gran calidad para garantizar una mayor robustez del modelo hidrodinámico. En cuanto a la humedad
relativa, estos datos fueron extraídos a partir del modelo global ERA5.

Para la modelación en MOHID del sector donde se emplazará el proyecto, se utilizaron estos datos atmosféricos
como inputs para el módulo hidrodinámico, siendo estos las forzantes de las corrientes. Para ello, en WRF se
consideró un dominio de cálculo de 50 por 50 kilómetros de longitud, con lo que se asegura cubrir un área de
generación lo suficientemente grande para recabar datos de la dinámica atmosférica particular que se presenta en
el sector de estudio. En la Figura 59 se presenta un resumen del dominio del modelo WRF. Cabe mencionar que,

Marzo 2024

las condiciones de borde de los modelos de cajas se obtienen a partir del modelo jerárquico superior. La fecha de
la data ocupada para el modelo fue del 01/08/2020 al 30/09/2020 para el escenario de invierno, y 01/03/2021 al
01/04/2021 para el escenario de verano.

**Tabla 28: Coordenada de vértices del domino del modelo WRF utilizado.**

|Vértices del<br>dominio|Coordenadas de los vértices del dominio WRF (DATUM WGS - 84, HUSO 18S)|Col3|Col4|Col5|
|---|---|---|---|---|
|**Vértices del**<br>**dominio**|Latitud (S)|Longitud (W)|UTM Este (m)|UTM Norte (m)|
|A|42° 00' 31,98”|73° 38' 12,52”|612.881,58|5.348.338,62|
|B|41° 33' 27,79”|73° 38' 12,52”|664.264,35|5.348.338,62|
|C|41° 33' 27,79”|73° 01' 48,66”|664.264,35|5.397.454,16|
|D|42° 00' 31,98”|73° 01' 48,66”|612.881,58|5.397.454,16|

**Figura 59: Instante de muestra del modelo WRF con magnitudes de vientos utilizados en la modelación**

**en Nivel 2 y 3.**

Marzo 2024

### Anidamiento de dominios del modelo

La modelación hidrodinámica consideró tres niveles de anidamiento, lo que consistió en definir una grilla
computacional de baja resolución espacial y de mayor tamaño (nivel 1), una de resolución intermedia (nivel 2) y
finalmente una con de alta resolución en la zona de interés (nivel 3).

**Figura 60: Ubicación y tamaño de las grillas utilizadas.**

En la malla de nivel 2 y 3, se utilizaron las condiciones de borde atmosféricas en conjunto con los ríos afluentes
del sector del proyecto, que como se pudo observar, los niveles 2 y 3 se encuentran inscritos dentro del dominio

del modelo WRF.

### Información de Corrientes

_**Correntometría invierno.**_

Para caracterizar las corrientes del sitio, se analizaron datos de dirección y magnitud registrados por un
correntómetro ADCP (Acoustic Doppler Current Profiler) fondeado frente a la zona de descarga cuya posición se
presenta en la siguiente tabla:

**Tabla 29: Correntometría euleriana invierno**

|Estudios|Periodo de medición|Coordenada UTM|Col4|
|---|---|---|---|
|**Estudios**|**Periodo de medición**|Este|Norte|
|Correntometría euleriana|23-08-2020 al 22-09-2020|638.438|5.374.107|

El análisis de datos se efectuó en base a estadística básica y distribución de frecuencia de la magnitud y la dirección
de la corriente, para tres capas representativas de la columna de agua (superficie, medio y fondo). Además, se
elaboraron histogramas y rosas de direcciones correspondientes a la dirección y magnitud de la corriente para
cada una de las capas analizadas.

Marzo 2024

_**Capa superficial**_

Para la capa superficial se utilizó la capa de los 10 metros desde el fondo. Se utiliza esta capa como superficial
debido a que representa esta sección de la columna de agua sin efectos de la marea. De acuerdo con los resultados
del registro de velocidad, los mayores porcentajes de ocurrencia ocurrieron entre los rangos 5-10 y 10-15 con
36,9% y 23,4% respectivamente. (Tabla 30, Figura 61).

**Tabla 30: Incidencia Magnitud y dirección capa superficial invierno.**

|Magnitud (cm/s)|Dirección (°)|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Total|Frec.<br>Absoluta|
|---|---|---|---|---|---|---|---|---|---|---|
|**Magnitud (cm/s)**|N|NE|E|SE|S|SW|W|NW|NW|NW|
|Calmas|178|4|5|4|5|2|5|4|207|4,8%|
|1-5|93|97|108|108|123|83|91|92|795|18,4%|
|5-10|192|221|237|205|209|206|167|158|1595|36,9%|
|10-15|84|178|194|123|116|138|103|73|1009|23,4%|
|15-20|26|70|102|41|39|46|45|19|388|9,0%|
|20-25|4|29|51|22|14|21|15|8|164|3,8%|
|25-30|6|9|16|7|13|10|4|3|68|1,6%|
|>30|6|6|45|12|11|7|2|6|95|2,2%|
|Total|589|614|758|522|530|513|432|363|4321||
|Frec. Absoluta|13,6%|14,2%|17,5%|12,1%|12,3%|11,9%|10,0%|8,4%|||

**Figura 61: Histograma magnitud capa superficial invierno.**

Marzo 2024

Al analizar el total de registros de direcciones, se observa que la corriente en esta capa tiende a dirigirse hacia el
E, con un 17,5 % de ocurrencia (Figura 62).

**Figura 62: Rosa de Corrientes capa superficial invierno**

_**Capa Media**_

La capa media se encuentra a una profundidad de 4 m respecto a la línea de más baja marea (6 metros desde el
fondo). En la Tabla 31 se observa que las corrientes con un mayor porcentaje de ocurrencia oscilan entre los 5-10
y 10-15 cm/s con ocurrencias entre el 39,6% y 24,8%.

**Tabla 31: Magnitud y dirección capa media invierno.**

|Magnitud (cm/s)|Dirección (°)|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Total|Frec.<br>Absoluta|
|---|---|---|---|---|---|---|---|---|---|---|
|**Magnitud (cm/s)**|N|NE|E|SE|S|SW|W|NW|NW|NW|
|Calmas|11|9|4|3|5|4|7|2|45|1,0%|
|1-5|105|136|127|112|92|125|120|124|941|21,8%|
|5-10|207|235|255|196|168|223|213|212|1709|39,6%|
|10-15|115|188|208|108|102|131|128|90|1070|24,8%|
|15-20|32|83|95|33|28|45|50|23|389|9,0%|
|20-25|4|30|38|10|3|9|12|4|110|2,5%|
|25-30|2|12|11|4|0|3|0|0|32|0,7%|
|>30|2|0|13|3|3|3|0|1|25|0,6%|
|Total|478|693|751|469|401|543|530|456|4321||

Marzo 2024

|Magnitud (cm/s)|Dirección (°)|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Total|Frec.<br>Absoluta|
|---|---|---|---|---|---|---|---|---|---|---|
|**Magnitud (cm/s)**|N|NE|E|SE|S|SW|W|NW|NW|NW|
|Frec, Absoluta|11,1%|16,0%|17,4%|10,9%|9,3%|12,6%|12,3%|10,6%|||

**Figura 63: Histograma magnitud capa media invierno.**

En la capa media se distinguen una menor variabilidad, sin embargo, la dirección predominante es Este y Noreste
con un porcentaje de predominancia de un 17,4 y 16%. (Figura 64).

Marzo 2024

_**Capa de fondo**_

**Figura 64: Rosa de direcciones capa media invierno**

La capa del fondo se encuentra a una profundidad de 10 metros respecto a la línea de más baja marea. En esta
capa el mayor rango de magnitud para esta capa se encuentra entre los 5- 10 cm/s, con un total de 35,8% de
ocurrencia (Tabla 32, Figura 65).

**Tabla 32: Magnitud y dirección capa de fondo invierno.**

|Magnitud (cm/s)|Dirección (°)|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Total|Frec.<br>Absoluta|
|---|---|---|---|---|---|---|---|---|---|---|
|**Magnitud (cm/s)**|N|NE|E|SE|S|SW|W|NW|NW|NW|
|Calmas|7|4|2|5|6|4|4|7|39|0,9%|
|1-5|103|103|94|96|81|98|77|85|737|17,1%|
|5-10|204|212|212|179|177|196|169|196|1545|35,8%|
|10-15|137|171|199|152|131|134|114|116|1154|26,7%|
|15-20|54|79|110|83|57|58|47|55|543|12,6%|
|20-25|14|29|55|35|17|24|24|12|210|4,9%|
|25-30|6|10|15|13|3|4|1|4|56|1,3%|
|>30|13|1|6|7|5|1|1|3|37|0,9%|
|Total|538|609|693|570|477|519|437|478|4321||
|Frec, Absoluta|12,5%|14,1%|16,0%|13,2%|11,0%|12,0%|10,1%|11,1%|||

Marzo 2024

**Figura 65: Histograma de magnitud capa de fondo invierno.**

En la capa de fondo se distinguen corrientes predominantes en la dirección Este y Noreste con un porcentaje de
ocurrencia de 16 y 14,1% respectivamente. (Figura 66)

**Figura 66: Rosa de direcciones capa de fondo invierno.**

Marzo 2024

_**Correntometría verano.**_

De igual forma que para la correntometría de invierno, se caracterizaron las corrientes del sitio por medio de un
correntómetro ADCP (Acoustic Doppler Current Profiler) fondeado frente a la zona de descarga, donde se
analizaron los datos de magnitud y dirección registrados por el equipo. La ubicación donde fue fondeado el equipo
se presenta en la Tabla 33 a continuación.

**Tabla 33: Correntometría euleriana verano**

|Estudios|Periodo de medición|Coordenada UTM|Col4|
|---|---|---|---|
|**Estudios**|**Periodo de medición**|Este|Norte|
|Correntometría euleriana|04-03-2021 al 05-04-2021|638.480|5.374.082|

El análisis de datos se efectuó en base a estadística básica y distribución de frecuencia de la magnitud y la dirección
de la corriente, para tres capas representativas de la columna de agua (superficie, medio y fondo). Además, se
elaboraron histogramas y rosas de direcciones correspondientes a la dirección y magnitud de la corriente para
cada una de las capas analizadas.

_**Capa superficial**_

Para la capa superficial se utilizó la capa de los 10 metros desde el fondo. Se utiliza esta capa como superficial
debido a que representa esta sección de la columna de agua sin efectos de la marea. De acuerdo con los resultados
del registro de velocidad, los mayores porcentajes de ocurrencia ocurrieron entre los rangos 5-10 y 10-15 con
37,1% y 21,4% respectivamente. (Tabla 34, Figura 67).

**Tabla 34: Magnitud y dirección capa superficial verano.**

|Magnitud (cm/s)|Dirección (°)|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Total|Frec.<br>Absoluta|
|---|---|---|---|---|---|---|---|---|---|---|
|**Magnitud (cm/s)**|N|NE|E|SE|S|SW|W|NW|NW|NW|
|Calmas|5|0|6|4|5|3|2|3|28|0,6%|
|0-5|128|143|199|123|119|82|82|79|955|21,2%|
|5-10|210|356|419|264|134|82|68|141|1674|37,1%|
|10-15|87|238|307|173|64|18|23|55|965|21,4%|
|15-20|50|78|133|55|22|3|3|15|359|8,0%|
|20-25|35|19|27|40|22|3|0|21|167|3,7%|
|25-30|39|11|15|15|13|3|0|17|113|2,5%|
|>30|73|18|10|42|52|1|0|50|246|5,5%|
|Total|627|863|1116|716|431|195|178|381|4507||
|Frec,.Absoluta|13,9%|19,1%|24,8%|15,9%|9,6%|4,3%|3,9%|8,5%|||

Marzo 2024

**Figura 67: Histograma de magnitud capa superficial verano.**

En la capa de fondo se distinguen corrientes predominantes en la dirección Este y Noreste con un porcentaje de
ocurrencia de 24,8 y 19,1% respectivamente. (Figura 68).

**Figura 68: Rosa de direcciones capa superficial verano.**

Marzo 2024

_**Capa Media**_

La capa media se encuentra a una profundidad de 4 m respecto a la línea de más baja marea (6 metros desde el
fondo). En la Tabla 35 se observa que las corrientes con un mayor porcentaje de ocurrencia oscilan entre los 1-5
y 5-10 cm/s con ocurrencias entre el 40% y 24,2%.

**Tabla 35: Magnitud y dirección capa media verano.**

|Magnitud (cm/s)|Dirección (°)|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Total|Frec.<br>Absoluta|
|---|---|---|---|---|---|---|---|---|---|---|
|**Magnitud (cm/s)**|N|NE|E|SE|S|SW|W|NW|NW|NW|
|Calmas|5|5|3|5|8|9|6|8|49|1,1%|
|1-5|89|169|197|168|124|97|118|109|1071|24,2%|
|5-10|127|398|465|288|185|77|91|139|1770|40,0%|
|10-15|77|237|341|178|63|22|26|53|997|22,6%|
|15-20|20|113|160|55|24|8|4|10|394|8,9%|
|20-25|7|29|37|10|7|2|0|3|95|2,1%|
|25-30|4|7|12|4|1|1|1|0|30|0,7%|
|>30|5|4|3|1|2|0|0|0|15|0,3%|
|Total|334|962|1218|709|414|216|246|322|4421||
|Frec. Absoluta|7,6%|21,8%|27,6%|16,0%|9,4%|4,9%|5,6%|7,3%|||

**Figura 69: Histograma magnitud capa media verano.**

Marzo 2024

En la capa media se distinguen una menor variabilidad, sin embargo, la dirección predominante es Este y Noreste
con un porcentaje de predominancia de un 27,6 y 21,8%.

**Figura 70: Rosa de direcciones capa media verano.**

_**Capa de fondo**_

La capa del fondo se encuentra a una profundidad de 10 metros respecto a la línea de más baja marea. En esta
capa los mayores rangos de magnitud para esta capa se encuentran entre los 5 - 10 cm/s y 10 - 15 cm/s, con un
total de 22,8% y 23,8% de ocurrencia (Tabla 36, Figura 71).

**Tabla 36: Magnitud y dirección capa de fondo verano.**

|Magnitud (cm/s)|Dirección (°)|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Total|Frec.<br>Absoluta|
|---|---|---|---|---|---|---|---|---|---|---|
|**Magnitud (cm/s)**|N|NE|E|SE|S|SW|W|NW|NW|NW|
|Calmas|1|3|1|3|2|1|4|1|16|0,3%|
|1-5|69|72|76|79|51|47|56|41|491|10,6%|
|5-10|140|187|184|166|136|81|60|102|1056|22,8%|
|10-15|189|249|221|175|150|34|25|57|1100|23,8%|
|15-20|139|185|126|172|119|26|8|21|796|17,2%|
|20-25|126|88|54|78|81|5|1|15|448|9,7%|
|25-30|92|30|20|38|51|4|0|2|237|5,1%|
|>30|183|32|17|61|164|17|1|7|482|10,4%|

Marzo 2024

|Magnitud (cm/s)|Dirección (°)|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Total|Frec.<br>Absoluta|
|---|---|---|---|---|---|---|---|---|---|---|
|**Magnitud (cm/s)**|N|NE|E|SE|S|SW|W|NW|NW|NW|
|Total|939|846|699|772|754|215|155|246|4626||
|Frec. Absoluta|20,3%|18,3%|15,1%|16,7%|16,3%|4,6%|3,4%|5,3%|||

**Figura 71: Histograma de magnitud capa de fondo verano.**

En la capa de fondo se distinguen corrientes predominantes en la dirección Norte y Noreste, con un porcentaje de
ocurrencia de 20,3 y 18,3%, respectivamente. (Figura 72).

Marzo 2024

**Figura 72: Rosa de direcciones capa de fondo verano.**

### Información Atmosférica

Para la presente Adenda, se utilizó información atmosférica mediante modelación por medio del modelo WRF
durante el periodo de 1/06/2020 al 31/07/2021, abarcando los periodos de medición de corrientes de invierno

como de verano. Para describir el modelo, se

Las series de tiempo para los escenarios de invierno y verano se presentan en la Figura 73.

Marzo 2024

**Figura 73: Series de tiempo de información atmosférica a partir de modelo WRF en sitio de descarga del**

**proyecto.**

### Modelo Global de marea

Para el módulo hidrodinámico se utilizó como condición de borde inicial el modelo global de marea FES (Finite
Element Solution [4] ) 2014, el cual fue desarrollado y validado por LEGOS (Laboratory of Space Geophysical and

4 [https://www.aviso.altimetry.fr/en/data/products/auxiliary-products/global-tide-fes/description-fes2014.html](https://www.aviso.altimetry.fr/en/data/products/auxiliary-products/global-tide-fes/description-fes2014.html)

Marzo 2024

Oceanographic Studies, Francia), NOVELTIS y CLS (Collecte Localisation Satellites, Francia). Este modelo fue
implementado en la modelación hidrodinámica como forzante de la marea en los bordes abiertos del dominio de
nivel 1 para los períodos simulados de invierno y verano.

En la, se muestra la distribución global a partir del modelo FES2014 de la amplitud del componente mareal M 2 .

**Figura 74: Mapa global de componente M2, modelo FESS 2014.**

Marzo 2024

**ANEXO C**

# Metodología

Marzo 2024

### Modelo Utilizado

Para el estudio de caracterización de la pluma de dispersión e hidrodinámica en el medio se utilizó el modelo
MOHID que opera bajo el software OpenFlows Flood. El cual se trata de un sistema informático para el estudio de
sistemas acuáticos, y fue desarrollado por el Centro de Investigación de Tecnología Marina (MARETEC)
perteneciente al Instituto Superior Técnico (IST) de la Universidad de Lisboa, Portugal. El modelo dispone de una
serie de herramientas funcionales para el pre-proceso de la información y postproceso de los resultados, junto a
su correspondiente visualización. Entre las herramientas con mayor relevancia disponibles por OpenFlows Flood
se destacan; la generación de cuadriculas computacionales, condiciones iniciales y de borde, transformación de

información a diversos formatos, entre otros.

La herramienta de modelación MOHID ha sido utilizada en diversos países y cuerpos de aguas, tales como lagos
y lagunas (Seiter _et al.,_ 2020; Razi _et al_ ., 2016); costas y bahías (Moctezuma _et al.,_ 2012; Pierini _et al_ ., 2012), y
ríos y estuarios (Sánchez-Gutiérrez _et al_ ., 2021). El esquema numérico de MOHID se materializa a través del
método de los volúmenes finitos que permite utilizar coordenadas verticales genéricas, dependiendo del proceso
principal del área a estudiar, y trabaja subdividido en más de 40 módulos, cada uno de éstos contiene determinada
información e interactúan con los demás a través de la definición de flujos de información. Los principales módulos
son el hidrodinámico, geometría, propiedades del agua, turbulencia, calidad de aguas, sedimentos, entre otros, lo
cual, se ve reflejado en la Figura 75 que representa la interacción de los módulos en el software.

**Figura 75: Interacción módulos MOHID,**

**Fuente: Reporte Inicial MOHID 2009**

Para la caracterización hidrodinámica y la simulación de la pluma de dispersión, se utilizó el modelo MOHID Water,
programa de simulación tridimensional que simula diversos procesos que ocurren en cuerpos de agua como
océanos, lagos, áreas costeras, estuarios, ríos, entre otros; considerando además los procesos de intercambio con
otros medios, como la interacción con la atmosfera y con el fondo.

Marzo 2024

El esquema numérico se materializa a través de una aproximación de volúmenes finitos que permite utilizar
coordenadas verticales genéricas, dependiendo del proceso principal del área a estudiar, la Figura 76 representa
los módulos que interactúan en el software.

**Figura 76: Interacción módulos MOHID Water**

Los principales módulos del programa MOHID Water permiten organizar las simulaciones, visualizar y preparar
los datos de entrada para cada módulo que será utilizado en la modelación, los que son descritos brevemente en

la Tabla 37.

.

Marzo 2024

**Tabla 37: Módulos utilizados en la modelación con MOHID Water**

|Módulo|Descripción|
|---|---|
|**Geometry**|El módulo Geometry maneja la discretización vertical en MOHID. Fue diseñado para dividir la<br>columna de agua. Además, este Módulo gestiona la inicialización y la evolución temporal de la<br>grilla.|
|**Atmosphere**|El módulo de Atmosphere es responsable de los datos meteorológicos necesarios para calcular<br>los procesos que ocurren en la interfaz agua-aire, como el cálculo de la tensión de cizalladura<br>del viento, los balances de radiación, los flujos de calor latente y sensible.|
|**Interface Water-air**|El módulo Interface Water-air es responsable de los procesos que ocurren en la interfaz agua-<br>aire, como el cálculo de la tensión de cizalladura del viento , los balances de radiación, los flujos<br>de calor latente y sensible. Este módulo toma como inputs los datos de módulo atmosphere.|
|**Hydrodynamic**|El módulo hidrodinámico resuelve las ecuaciones primitivas de continuidad y momento para la<br>elevación de la superficie y el campo de velocidad 3D para flujos incompresibles, en<br>coordenadas horizontales ortogonales y coordenadas verticales genéricas, asumiendo equilibrio<br>hidrostático y aproximaciones de Boussinesq|
|**Water properties**|El módulo Water Properties es el módulo de transporte euleriano 3D incluido en MOHID. El<br>módulo Water Properties se encarga de calcular la evolución de las propiedades en la columna<br>de agua|
|**Interface sediment-**<br>**water**|El módulo de Interface sediment-water calcula las condiciones de contorno en la parte inferior<br>de la columna de agua. Calcula el esfuerzo cortante como una condición límite para los módulos<br>hidrodinámico y de turbulencia|
|**Turbulence**|El módulo turbulence utiliza el modelo GOTM, el cual es el encargado de simular la turbulencia<br>generada por los esfuerzos de corte entre la interfaz agua aire en superficie, agua sedimento en<br>profundidad, así como también variaciones en las densidades que generan cambios en las<br>presiones y por tanto velocidades verticales.|
|**Lagrangian**|Modelo de transporte lagrangiano, gestiona la evolución de las mismas propiedades que el<br>modelo de las propiedades del agua utilizando un enfoque en función lagrangiana.|

Marzo 2024

Un esquema de la implementación y funcionamiento de los módulos del modelo MOHID se explican en la
Figura 77.

**Figura 77: Esquema de funciones e implementación módulos MOHID Water.**

### Ecuaciones de gobierno modelo MOHID

El módulo hidrodinámico MOHID plantea y resuelve las ecuaciones de cantidad de movimiento en una grilla
estructurada e implementa el método de volúmenes finitos a través de un algoritmo semi-implicito ADI (AlternatingDirection Implicit) para la resolución de la ecuación de advección-difusión, con una reducción importante en los
costos computacionales.

El módulo hidrodinámico de MOHID, está dado por un modelo de flujo de superficie libre basado en las ecuaciones
de Navier Stokes, el cual implementa el método de volúmenes finitos (Martins _et al.,_ 2001), que resuelve las
ecuaciones primitivas incompresibles, suponiendo un equilibrio hidrostático y empleando la aproximación de
Boussinesq. Con la implementación de MOHID se pueden realizar simulaciones de áreas costeras y estuarinas
que presenten una compleja batimetría y topografía.

Las ecuaciones de balance de _momentum_ para el flujo de velocidades horizontales medias están expresadas en
forma cartesiana a través de las Ecs. 1 y 2. Mientras la aproximación hidrostática se asume a partir de la Ec. 3.
Actualmente el método de volúmenes finitos es ampliamente utilizado para modelar problemas hidrodinámicos.

∂u

∂u

∂t [+ u∂u] ∂x

∂x [+ v∂u]

∂y [−fv= −1] ρ

ρ

∂u [∂]
∂x ~~[)]~~ [ +] ∂y [(A] [H]

∂u
Ec 1
∂y ~~[)]~~

∂p [∂]
∂x [+] ∂x [(A] [H]

Marzo 2024

Donde:

t : Es el tiempo.

∂v

∂v

∂t [+ u∂v] ∂x

∂x [+ v∂v]

∂y [−fv= −1] ρ

ρ

∂v [∂]
∂x ~~[)]~~ [ +] ∂y [(A] [H]

∂v [∂]
∂x ~~[)]~~ [ +]

∂v
Ec 2
∂y ~~[)]~~

∂p [∂]
∂y [+] ∂x [(A] [H]

∂ Z p+ gρ= 0 Ec 3

u, v : Son las componentes de la velocidad en los ejes x e y, respectivamente.

f : Es el coeficiente de Coriolis.

p : Presión.

ρ : Densidad del agua.

g : Gravedad.

A H : Viscosidad turbulenta horizontal.

Módulo de transporte de MOHID

Los fenómenos de transporte en la columna de agua para una propiedad dada se pueden describir a través de la
ecuación de advección-difusión en su forma bidimensional (Ec. 4).

∂(HC)

+ [∂(uHC)]
∂t ∂x

+ [∂(vHC)]
∂x

= [∂]
∂y

∂x [(HD] [x]

∂C
Ec 4
∂y ~~[)]~~

∂C [∂]
∂x ~~[)]~~ [ +] ∂y [(HD] [y]

∂C [∂]
∂x ~~[)]~~ [ +]

Donde:

 - C : Es la concentración promediada en profundidad.

 - H⁡ : Profundidad.

 - t : Tiempo.

 - u, v : Componentes de velocidad promediadas en profundidad.

 - D x, D y : Son los coeficientes de dispersión horizontal en los ejes x e y, respectivamente.

Esta ecuación permite calcular la evolución de la concentración de una sustancia introducida en un medio
acuático, teniendo en cuenta la acción conjunta de la advección (transporte a través de las corrientes existentes
en el medio acuático) y la difusión turbulenta (dispersión de la concentración de la sustancia de interés) y los
procesos de transformación (físicos, químicos o biológicos, que actúan en el caso de que una sustancia no sea
conservativa).

Marzo 2024

_**Viscosidad y difusión turbulenta**_

El software MOHID considera varias expresiones para determinar los coeficientes de viscosidad turbulenta,
utilizando valores constantes o variables calculados según la formulación de Smagorinsky (Ec. 5). Donde k un
parámetro de calibración del modelo.

+ [1]

[1]

2 [(∂v] ∂x

1/2

]

v H = k∗dx∗dy∗[ [∂u] ∂y

2

∂y ~~[)]~~ [ + (∂v] ∂y

∂y ~~[)]~~

2

∂x [+ ∂u]

Ec 5

El coeficiente horizontal de difusividad es calculado en MOHID a partir del coeficiente de viscosidad turbulenta
horizontal. Se considera que la viscosidad y difusividad se relacionan a través de un factor de proporcionalidad,

denominado número de Schmidt.

_**Modelo lagrangiano**_

Se implementó para el periodo de diciembre del 2020 (campaña para la Línea Base de caracterización del medio
marino). El modelo de transporte lagrangiano que utiliza el concepto de trazador, cuyas propiedades fundamentales
son la posición espacial (x, y, z) de las partículas utilizadas como trazadores, su volumen y la concentración de
determinadas propiedades de interés, como pueden ser cualquiera de las evaluadas en el módulo de calidad de

agua.

El principal factor responsable del movimiento de las partículas es generalmente la velocidad media, definida como:

dx i

Ec 6
dt [= u] [i] [(x] [i] [, t)]

Donde:

u : Representa la velocidad media

x : La posición de la partícula i en un tiempo t

La ecuación se resuelve utilizando un método explícito simple:

t+∆t
= x i

x i

t + ∆t∗u it

t Ec 7

El módulo lagrangiano calcula el seguimiento de las partículas (pequeñas porciones de agua), donde cada partícula
es independiente de las demás, pero para agregar el impacto de todas las partículas se requiere una interpolación
entre los puntos de la grilla del modelo hidrodinámico a la cuadrícula computacional. La Ec.8 realiza el cálculo de
integración de concentraciones en las celdas de la grilla:

Marzo 2024

Donde:

C mean =

n n
∑ i=1 C P i V P i + C cell ∗ (V cell −∑ i=1 V P i )

V cell

Ec 8

C mean : Concentración promedio de la propiedad en la celda de la cuadricula.

n : número de partículas dentro de la celda de la cuadricula.

C P i : Concentración de la propiedad dentro de una partícula.

V P i : Volumen de la partícula.

C cell : Concentración (euleriana) dentro de la celda de la cuadricula.

V cell : Volumen de la celda de la cuadricula.

## wsp.com