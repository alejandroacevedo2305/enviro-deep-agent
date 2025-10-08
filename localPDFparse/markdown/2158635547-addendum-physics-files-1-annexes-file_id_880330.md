---
title: Sin título
author: Nicolas Sepulveda
date: D:20230802153319-04'00'
language: es
type: report
pages: 75
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - “Modificación Proyecto Inmobiliario Valle Noble”
  - 1 Introducción.
  - 2 Objetivos.
  - 3 Marco Legal Regulatorio.
  - 4 Justificación de los modelos utilizados en el estudio.
  - 5 Metodología
  - 6 Resultados
  - 7 Análisis de incertidumbre
  - 8 Conclusión
  - 9 Bibliografía
-->

### INFORME MODELACIÓN DE PARTÍCULAS

# “Modificación Proyecto Inmobiliario Valle Noble”

**Julio** **,** **2023**

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 2 de 75

## Contenidos|

1 Introducción. ....................................................................................................... 3

2 Objetivos. ........................................................................................................... 4

3 Marco Legal Regulatorio. ...................................................................................... 5

3.1 Estado de la Calidad del Aire .......................................................................... 6

3.2 Línea de Base ............................................................................................... 6

4 Justificación de los modelos utilizados en el estudio. .............................................. 11

4.1 Uso modelo CALPUFF ................................................................................... 11

4.2 Uso modelo WRF ......................................................................................... 13

5 Metodología ....................................................................................................... 14

5.1 Estimación de Emisiones: Determinación del Año de Modelación ...................... 14

5.2 Modelación meteorológica ............................................................................. 14

5.3 Modelación de partículas............................................................................... 18

5.3.1 Fuentes de Emisión ............................................................................... 18

5.3.2 Receptores Discretos. ............................................................................ 22

6 Resultados ......................................................................................................... 26

6.1 . Modelamiento meteorológico ...................................................................... 26

6.1.1 Caracterización de la velocidad y dirección de los vientos Anual ................. 26

6.1.2 Caracterización de la velocidad y dirección de los vientos Estacional .......... 28

6.1.3 Caracterización de la Temperatura del Aire .............................................. 38

6.1.4 Caracterización de la Precipitación .......................................................... 40

6.1.5 Altura Capa de meza .............................................................................. 41

6.2 Concentraciones Modeladas .......................................................................... 43

6.2.1 Dispersión e Isoconcentración Material Particulado Respirable MP10 .......... 43

6.2.2 Dispersión e Isoconcentración Material Particulado Fino Respirable MP 2.5 . 47

6.2.3 Modelación discreta de las emisiones contaminantes ................................ 51

6.3 Aporte a la estación de Monitorio de Representatividad Poblacional (EMRP) ...... 67

7 Análisis de incertidumbre .................................................................................... 68

7.1 Análisis cualitativo ........................................................................................ 69

7.2 Análisis cuantitativo ...................................................................................... 71

8 Conclusión ......................................................................................................... 73

9 Bibliografía ......................................................................................................... 75

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

# 1 Introducción.

Página 3 de 75

El proyecto “ **Proyecto Inmobiliario Valle Noble** ” fue presentado por Consorcio

Inmobiliario Palomares S.A. al SEIA mediante una Declaración de Impacto Ambiental el 16

de octubre de 2008 y fue calificado ambientalmente favorable el día 4 de marzo del 2009

mediante la Resolución Exenta N°35/2009. La situación del proyecto con RCA N°35/2009,

en adelante proyecto original, contemplaba la construcción de 1.411 viviendas unifamiliares

en la comuna de Concepción, a ejecutarse en 9 etapas que contemplaban el desarrollo de

la urbanización y edificación de manera simultánea. La superficie total empleada por el

proyecto inmobiliario corresponde a 50 hectáreas.

El proyecto en evaluación, denominado “ **Modificación Proyecto Inmobiliario Valle**

**Noble** ”, presentado por Inmobiliaria Valle Noble S.A, consiste en la modificación de la RCA

N°35/2009, cuyo objetivo es aumentar el número de unidades habitacionales pasando de

1.411 a 1.616, sin modificar la superficie original del proyecto aprobada anteriormente, es

decir, 50 ha.

Con este estudio se busca predecir la concentración de material particulado grueso y fino

(MP 10 y MP 2,5 ), además de evaluar su contribución en puntos receptores de interés y en las

estaciones de calidad del aire más cercanas, esto último respecto a su situación basal.

La modelación de las emisiones se realizó en base a los resultados obtenido de la estimación

de emisiones atmosférica. Considerando como escenario de máxima emisión del proyecto,

correspondiente al año de operación total de éste.

La evaluación de la dispersión y concentración de las emisiones de material particulado se

realizó mediante el programa CALPUFF, el cual es un modelo de dispersión usado

ampliamente para simulaciones de concentraciones ambientales de las emisiones normales,

con el objeto de establecer, desarrollar y analizar escenarios de emisión y regulación. A su

vez, CALPUFF es recomendado por el Ministerio de Medio Ambiente en la “Guía para el Uso

de Modelos de Calidad del Aire en el SEIA”, publicada el año 2023. Los resultados y análisis

de esta evaluación se presentan en el siguiente informe.

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 4 de 75

# 2 Objetivos.

El presente informe, tiene como objetivo general evaluar el efecto en la atmósfera debido a

las emisiones de contaminantes generadas por el proyecto **“Modificación Proyecto**

**Inmobiliario Valle Noble”** y cuantificar sus concentraciones.

Para lo anterior se plantean los siguientes objetivos específicos:

 - Evaluar en términos de concentración, el alcance de las emisiones de MP 10 y MP 2,5

en la atmósfera.

 Evaluar la concentración de MP 10 y MP 2,5 en receptores que actualmente se

encuentren cercanos al proyecto, así como en las estaciones de calidad del aire

emplazadas cercanos a éste.

 Determinar la afectación a la salud de las personas debido al aporte a la

concentración basal de MP 10 y MP 2,5 en la ciudad, dado el desarrollo del proyecto.

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

# 3 Marco Legal Regulatorio.

Página 5 de 75

Actualmente, los contaminantes MP 10 y MP 2,5 están regulados bajo normas de calidad

primaria, cuyo objetivo es proteger la salud de las personas de los efectos agudos y crónicos

de la exposición de estos contaminantes con un riesgo aceptable. Para esto, se fijan límites

de concentración permitidos, condiciones de superación de la norma y los niveles que dan

paso a situaciones de emergencia ambiental.

El material particulado respirable MP 10 es regulado por el D.S. N°12/2022 del Ministerio del

Medio Ambiente, mientras el material particulado fino respirable MP 2,5 es regulado por el

D.S. N°12/2011 del Ministerio del Medio Ambiente.

En la Tabla 1 se aprecian los valores del límite anual y diario para los contaminante MP10 y

MP 2,5, además de los rangos que dan origen a situaciones de alerta, preemergencia y

emergencia ambiental.

**Tabla 1 Valores normados para MP10 y MP2,5 en Chile.**

|Nivel|MP (μg/m3N)<br>10|MP (μg/m3)<br>2,5|
|---|---|---|
|**Concentración Anual**|50|20|
|**Concentración 24 horas**|130|50|
|**Alerta**|180-229|80-109|
|**Preemergencia**|230-329|110-169|
|**Emergencia**|330 o superior|170 o superior|

Fuente: En base a D.S. 12/2022 MMA y D.S. 12/2011 MMA

No obstante, la superación del límite normativo de MP 10 no es motivo de condiciones de

superación de la norma, sino que se considera que la norma es incumplida bajo las

siguientes condiciones:

 - Cuando el promedio de la concentración anual de tres años consecutivos sea igual o

supere los 50 μg/m3.

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 6 de 75

 - Si el percentil 98 (P98) de las concentraciones de 24 horas durante un año sea igual

o superior a 130 μg/m3.

 - Si durante un año se registrasen siete o más días cuya concentración sea mayor a

130 μg/m3.

En el mismo contexto, las condiciones de superación de la norma de MP 2,5 son las que se

describen a continuación:

 - Cuando el promedio de la concentración anual de tres años consecutivos sea igual o

supere los 20 μg/m3.

 - Si el percentil 98 (P98) de las concentraciones de 24 horas durante un año sea igual

o superior a 50 μg/m3.

#### 3.1 Estado de la Calidad del Aire

La ciudad de Concepción forma parte de la conurbación de Concepción Metropolitano, la

cual ha sido declarada zona latente por sus concentraciones de 24 horas de MP 10, mediante

el D.S. N°6/2006 del MINSEGPRES. Adicionalmente, el D.S. N°15/2015 del MMA declara

zona saturada por MP 2,5 .

Esta situación dio inicio al proceso de elaboración del Plan de Prevención Atmosférica en

2011 por las concentraciones de MP 10, al que posteriormente se suma el mandato de

adicionar a él las medidas para el cumplimiento de la norma de MP 2,5 en 2016, iniciando la

elaboración del Plan de Prevención y Descontaminación Atmosférica de Concepción

Metropolitano.

#### 3.2 Línea de Base

El proyecto inmobiliario en evaluación se ubica a 5,5 km de la Estación de Monitoreo con

Representación Poblacional (EMRP) Kingston College, siendo la más cercana. A partir de los

datos disponibles en el Sistema de Información Nacional de Calidad del Aire (SINCA), se

seleccionó la data de MP 10 y MP 2,5 entre los años 2019 - 2022.

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 7 de 75

En la siguiente figura se presenta el promedio trianual de las concentraciones de MP 10 . En

ella se observa que los resultados hablan de una situación de pleno cumplimiento normativo,

registrando concentraciones de 26,1 μg/m [3] entre los años 2019 - 2022 y, 25,0 μg/m [3] entre

los años 2020 - 2022, bajo el límite de la concentración de 50 μg/m [3] y en tendencia a la

disminución de la concentración. Las magnitudes de concentración no sólo hablan de una

condición de no saturación, sino que también de no latencia al menos por la concentración

trianual.

**Figura 1 Concentración trianual de MP** **10** **en la EMRP Kingston College**

Del mismo modo, se analizó la concentración 24 horas de MP 10, cuyos resultados se

presentan en la Figura 2. Los resultados demuestran que al menos para el periodo escogido,

en la EMRP Kingston College, no hay una situación de superación de la norma o de estar el

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 8 de 75

80% de la concentración normada (130 μg/m [3] ), sino que en amplia holgura respecto a la

concentración registrada. Respecto a la tendencia de las concentraciones, se observa una

tendencia a la disminución de la concentración promedio 24 horas a excepción del año 2022

en donde las concentraciones registradas son mayores dentro del rango de tiempo

seleccionado.

**Figura 2 Concentración 24 h de MP** **10** **en la EMRP Kingston College**

Cabe destacar que esta situación no implica que el estado de la calidad del aire en

Concepción Metropolitano haya salido de la situación de latencia por MP 10 en su

concentración 24 h tal como fue definido en el D.S. N°6/2006 del MINSEGPRES, pues esta

decisión corresponde a un análisis técnico acabado que incluye otras EMRP; sino que, en

particular para la determinación de la línea de base de este proyecto, se utilizarán los datos

más cercanos cuyos resultados fueron los ya detallados.

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 9 de 75

En relación con las concentraciones de MP 2,5 registradas, se observa que la concentración

trianual se encuentra a más del 70% de la norma promedio trianual de 20 μg/m [3] . En general,

se observa que las concentraciones de MP 2,5 como promedio trianual son de similar

magnitud, tal como se observa en la Figura 3.

**Figura 3 Concentración trianual de MP** **2,5** **en la EMRP Kingston College.**

A continuación, se presentan los resultados para la concentración 24 horas de MP 2,5 de

donde se observa que sus magnitudes se encuentran dentro del límite normativo establecido

por el D.S. N°12/2011 del MMA. En general se observa una tendencia a la disminución de

la concentración de MP 2,5 como promedio diario, salvo en el año 2022 en donde la

concentración es >80% de la norma.

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 10 de 75

**Figura 4 Concentración 24 h de MP2,5 en la EMRP Kingston College**

Al igual que en el caso del MP 10, se deja de manifiesto que esta situación no implica que el

estado de la calidad del aire en Concepción Metropolitano haya salido de la situación de

saturación por MP 2,5 en su concentración 24 h tal como fue definido en el D.S. N°15/2015

del MMA, pues esta decisión corresponde a un análisis técnico acabado que incluye otras

EMRP; sino que en particular para la determinación de la línea de base de éste proyecto, se

utilizarán los datos más cercanos cuyos resultados fueron los ya detallados.

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 11 de 75

# 4 Justificación de los modelos utilizados en el estudio.

El Servicio de Evaluación Ambiental en la “Guía para el Uso de Modelos de Calidad del Aire

en el SEIA” (2023) hace una serie de recomendaciones para la modelación de contaminantes

primarios [1] y secundarios en el aire. En la actualidad, esta guía es el único documento

existente como parámetro para la modelación de calidad del aire y tiene como objetivo

uniformar los criterios, exigencias técnicas y antecedentes para la evaluación de los impactos

asociados a este componente de proyectos que ingresen al Servicio de Evaluación

Ambiental. Dentro de las recomendaciones de la guía está el uso del modelo de dispersión

CALPUFF y sugiere la utilización del modelo meteorológico WRF, los cuales fueron utilizados

en la modelación de las partículas del proyecto en evaluación.

A continuación, se presenta la justificación de los modelos utilizados para la ejecución de la

modelación de dispersión y concentración de emisiones partículas en el aire.

#### 4.1 Uso modelo CALPUFF

La modelación de dispersión atmosférica de partículas provenientes del proyecto se realizó

con un modelo tipo “Puff”, específicamente el modelo CALPUFF. Tal como lo define la guía,

los modelos tipo “puff” son una combinación entre los modelos Gaussianos y los modelos

Lagrangeanos, en el sentido de que esencialmente calculan la dispersión de contaminantes

provenientes de una emisión instantánea, llamada “puff”, a lo largo de una trayectoria. Su

aproximación matemática consiste en estimar la dispersión en forma Gaussiana en cada

punto de una trayectoria; es decir, los modelos tipo “puff” sólo requieren una trayectoria

por “puff”, lo que hace su cálculo mucho más rápido. En el caso de emisiones continuas, se

simulan las trayectorias y la dispersión Gaussiana de muchos “puffs”, como es en el caso de

1 Los contaminantes primarios son los producidos directamente por la actividad humana o la naturaleza a la atmósfera,
dentro de los cuales caben las emisiones contaminantes.

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 12 de 75

las emisiones de partículas generadas por el proyecto en evaluación. Al respecto, el modelo

tipo “puff” recomendado por la Guía es el modelo CALPUFF.

Así mismo, es un modelo completo que incorpora herramientas para procesar datos

meteorológicos y geofísicos, modelos de dispersión y post procesamiento. Dicho modelo es

recomendado por la Agencia de Protección Ambiental de los Estados Unidos (EPA) para

modelar transporte a larga distancia de contaminantes.

CALPUFF se compone de tres módulos:

 CALMET: Es un modelo meteorológico que desarrolla campos horarios de viento y

temperatura en una grilla de tres dimensiones. También asocia campos en dos

dimensiones de altura y usos de suelo. Este modelo fue reemplazado por el WRF, tal

como lo recomienda la guía antes citada.

 CALPUFF: Es un modelo de transporte y dispersión de partículas y gases emitidos

desde fuentes modeladas, simulando procesos de dispersión y transformación.

CALPUFF utiliza los datos generados por CALMET. Los archivos de salida de CALPUFF

contienen las concentraciones horarias o deposición por hora de flujos evaluados en

receptores seleccionados.

 - CALPOST: Es usado para procesar aquellos archivos generados por CALMET y

CALPUFF, produciendo tabulaciones que resumen los resultados de la simulación.

Ecuación del modelo CALPUFF

La ecuación básica que utiliza el modelo para realizar la modelación es la siguiente:

[−d] 2σ y [2][a2] ~~[]]~~

Q
C=
2πσ x σ y

∗g∗exp

~~[~~ [−d] 2σ x [2][a2]

[−d] 2σ x [2][a2] [] ∗exp] ~~[[]~~ [−d] 2σ y [2][a2]

2
g=

1
2 σ z

∞

∑e

n=∞

xp

~~[~~ [−(H] [e] 2σ [+ 2nh)] z [2] [2] ]

(2π ~~)~~

Dónde:

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

C, es concentración a nivel del suelo (g/m3)

Q, es masa de contaminantes (g) en la nube.

Página 13 de 75

σ x, es desviación estándar (m) de la distribución de Gauss en el viento a lo largo de

la dirección.

σ y, es desviación estándar (m) de la distribución de Gauss en el viento de costado

σ z, es desviación estándar (m) de la distribución de Gauss en la dirección vertical.

d a, es distancia (m) del centro de la nube al receptor en la dirección del viento a lo

largo.

d c, es distancia (m) del centro de la nube al receptor en la dirección de viento

cruzado.

g, es el término vertical (m-1) de la ecuación Gaussiana.

H, es la altura afectiva (m) desde el nivel del suelo del hojaldre.

h, es la altura de la capa de mezcla.

El terreno en el cual se realizará la modelación de las emisiones de partículas se considera

heterogéneo, debido a las distintas unidades geomorfológicas. Por esta razón y en

consistencia con las recomendaciones del SEA para la modelación de partículas en sus guías,

se consideró utilizar el modelo CALPUFF para simular la dispersión y concentración de las

emisiones de partículas generadas por la futura operación del proyecto.

#### 4.2 Uso modelo WRF

El modelo Weather Research and Forecasting (WRF), es un modelo numérico de cuatro

dimensiones, recomendado para la generación de datos meteorológicos y es uno de los

modelos de pronóstico meteorológicos más avanzados. Debido a la falta de una red robusta

de estaciones meteorológicas, la “Guía para el Uso de Modelos de Calidad del Aire en el

SEIA” (SEA, 2023) recomienda el uso de WRF por sobre el uso del CALMET. Además, el

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 14 de 75

mismo documento, sugiere el uso del WRF para la modelación de dispersión de

contaminantes con CALPUFF.

# 5 Metodología

#### 5.1 Estimación de Emisiones: Determinación del Año de Modelación

En el anexo 4.3 de la Adenda se presenta el Informe de Estimación de Emisiones para el

proyecto, cuyos resultados han demostrado que las emisiones son mayores cuando éste

alcanza la operación total de todas las unidades habitacionales.

En total, se modelaron 36,48 ton/año de MP 10 y 15,23 ton/año de MP 2,5 ; con relación a los

gases NOx, SOx y NH 3, se modelaron 52,95 ton/año, 0,14 ton/año y 0,04 ton/año,

respectivamente.

Respecto a la distribución de las emisiones, 25,11 ton/año de MP 10 y 6,10 ton/año de MP 2,5

corresponde a emisiones indirectas atribuibles al tránsito fuera del sitio del proyecto. Cabe

destacar que, como parte de los criterios de evaluación, la estimación de emisiones

consideró en distintas proporciones rutas hacia las comunas de Concepción, Chiguayante,

Tomé, Talcahuano, San Pedro de La Paz, Penco, Lota, Hualqui, Hualpén y Coronel, tal como

se presentó en la Figura 3 del anexo 4.3 de la Adenda, basado en los datos preliminares de

la Encuesta Origen - Destino de Viajes del Gran Concepción (SECTRA, 2017). Del mismo

modo, la simulación asume que estas son “nuevas emisiones” que se originan con el

proyecto, en definitiva, asume que las familias adquieren una vivienda y un vehículo

particular siendo un escenario poco frecuente.

#### 5.2 Modelación meteorológica

El WRF se realizó para la zona circundante al proyecto, el esquema metodológico de su

seteo se presenta en la figura a continuación.

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 15 de 75

**Figura 5. Esquema simplificado de la metodología para la elaboración de un**

**modelo meteorológico**

Las variables espaciotemporales del modelo se presentan a continuación:

! IBYR = 2022 !

! IBMO = 1 !

! IBDY = 1 !

! IBHR = 0 !

! IEYR = 2023 !

! IEMO = 1 !

! IEDY = 1 !

! IEHR = 0 !

! XBTZ = -4 !

! IRLG = 8761 !

! METDAT = WRF_Concepcion_2022.met !

! PMAP = LCC !

! RLAT0 = 36.817S !

! RLON0 = 72.998W !

! XLAT1 = 36.399S !

! XLAT2 = 37.399S !

! DATUM = NWS-84 !

! NX = 53 !

! NY = 53 !

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 16 de 75

! NZ = 10 !

! DGRIDKM = 1.000000 !

! ZFACE = 0., 20., 40.00, 80.00, 160.00, 320.00, 640.00, 1200.00, 2000.00,

3000.00, 4000.00 !

! XORIGKM = -26.500 !

! YORIGKM = -26.500 !

! IURB1 = 13 !

! IURB2 = 13 !

Como se puede observar, el seteo espacial del WRF se alineó a lo planteado en el apartado

4.3.3. de la “Guía para el Uso de Modelos de Calidad del Aire en el SEIA” (SEA, 2023), en

donde señala que el número de celdas mínimo ha de ser 50 x 50, con una resolución espacial

de 1 km para el último dominio, siendo este el tercer de los dominios anidados. En la Figura

6 se observa el dominio de la modelación meteorológica, de donde se puede observar su

amplia extensión, la que permite incluir los procesos a mesoescala y sinóptica [2], de modo de

que el modelo sea capaz de simular los procesos de transporte, dispersión y transformación

de contaminantes a distintas escalas temporales.

2 Es importante tener presente que el dominio de modelación utilizado de 53 km x 53 km corresponde
al último de los dominios anidados, los cuales son exponencialmente mayores:
Dominio 1: 477 km x 477 km y,
Dominio 2: 159 km x 159m.

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 17 de 75

**Figura 6 Dominio de Modelación Meteorológico**

En relación con su temporalidad, el modelo meteorológico fue seteado para el año 2022 y

simula las distintas variables con temporalidad de 1 hora para todos los días del año 2022.

Cabe señalar que la selección del año corresponde al año más cercano al actual, toda vez

que el análisis de correlación entre las variables meteorológicas y las concentraciones de

MP 10 registradas en las EMRP no arrojaron correlaciones diferenciales que demostraran que

un año en particular fuese el peor para la simulación meteorológica.

Cabe mencionar que el seteo del modelo meteorológico se realizó a partir de data satelital

y no a partir de datos registrados en las estaciones meteorológicas. En el Anexo 4.4.2 se

presenta el archivo namelist.input y namelist.wps, en donde se presentan los parámetros

físicos y dinámicas utilizados.

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

#### 5.3 Modelación de partículas

Página 18 de 75

En términos generales, la modelación de partículas se realizó según el siguiente esquema

metodológico y que se detalla en los siguientes acápites.

**Figura 7 Esquema metodológico**

El modelo de dispersión CALPUFF también permite la simulación de la transformación de MP

secundario en el aire, para lo cual se incluyeron las tasas de emisión de gases precursores

y las propias de MP.

5.3.1 Fuentes de Emisión

A continuación, se presenta un cuadro resumen con la descripción de las fuentes de emisión:

**Tabla 2 Fuentes de Emisión**

|Etapa del<br>proyecto|Actividades|Contami-<br>nantes<br>simulados|Tasa de<br>Emisión|Horas de<br>operación|Meses de<br>Operación|Tipo<br>de<br>Fuente|Características<br>Geométricas|
|---|---|---|---|---|---|---|---|
|Operación|Calefacción<br>Residencial|MP10<br>MP2,5<br>SOX <br>NOX <br>NH3|Ver<br>Anexo<br>4.3 de la<br>Adenda|12 horas|Marzo<br>- <br>Septiembre|De área|Polígono|
|Operación|Tránsito<br>Interno|Tránsito<br>Interno|Tránsito<br>Interno|3 <br>min/vehículo|Todos|Móvil|Polígono|
|Operación|Tránsito<br>Externo|Tránsito<br>Externo|Tránsito<br>Externo|20<br>min/vehículo|Todos|Móvil|Polígono|

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 19 de 75

En los Anexo 4.3 de la Adenda se presenta complementariamente a la tabla precedente:

 - Tasas de emisión simuladas calculadas en: máxima, mínima y promedio para cada

contaminante.

 - Número de horas al día, días a la semana y meses de operación.

En el Anexo 4.4.1 de la Adenda se presenta un archivo Excel con los datos ingresados al

modelo, el que incluye:

 - Coordenadas de los polígonos.

 - Tasas de emisión.

 - Contaminantes modelados.

 - Elevación del terreno.

Complementariamente, en el Anexo 4.4.1 se presentan todos los archivos de seteo del

modelo de Calpuff.

Para la simulación de las distintas actividades se tomaron los siguientes supuestos:

 - Calefacción residencial, de acuerdo con lo indicado en el anexo 4.3 Informe de

Estimación de Emisiones, apartado 4.2.1.1. el 59,4% de las viviendas utilizan leña

como método de calefacción de acuerdo con el estudio “Actualización de inventario

de emisiones atmosféricas y modelación de contaminantes del Concepción

Metropolitano, año 2013” (SICAM). Por lo tanto, se hicieron polígonos por sector que

representaran espacialmente esta distribución, representado en un total de 97

polígonos, los cuales se presentan en la Figura 8.

A estas fuentes se le atribuye 10,70 ton/año de MP 10 y 9,90 ton/año de MP 2,5 ; cabe

señalar que en la actualización del informe de emisiones (anexo 4.3 de la presente

Adenda), las emisiones son menores, ya que, en relación con la versión del informe

de estimación de emisiones presentado en la DIA (anexo 4.1), la nueva actualización

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 20 de 75

rectifica las emisiones de las últimas unidades habitacionales, las que incluyen un

sistema de calefacción integrado. Para suponer peores escenarios, la modelación de

partículas se realizó sin esta corrección, considerando las emisiones máximas

estimadas.

 - Transito Interno, esta actividad se realizó mediante la simulación de 65 polígonos

que concentran todas las emisiones de esta actividad en las calles arteriales del

proyecto, tal como se pueden ver en la Figura 9.

De acuerdo con la estimación de emisiones del proyecto, esta actividad genera 2,03

ton/año de MP 10 y 0,49 ton/año de MP 2,5, las cuales fueron simuladas en su totalidad

por los 65 polígonos que se construyeron para su simulación.

 - Tránsito Externo, para la estimación de emisiones se consideraron las 10 comunas

que forman parte del Gran Concepción, tal como se detalló en extenso en el apartado

3.2.2.1 del Anexo 4.3 de la Adenda, Informe de Estimación de Emisiones. De acuerdo

con los resultados planteados en la Tabla 60 del Anexo 4.3 de la Adenda, las

emisiones por todas estas rutas (10 en total, una para cada comuna) generan 25,08

ton/año de MP 10 y 6,07 ton/año de MP 2,5 .

Sin embargo, para simplificar la simulación se considera que las 25,08 ton/año de

MP 10 y 6,07 ton/año de MP 2,5 se generan en las rutas de mayor proporción de viajes

con destino a las comunas de Talcahuano y Concepción. Esta decisión se basa en

simular peores escenarios en las rutas más arteriales del Gran Concepción, las que

además se utilizan para llegar a las otras comunas que forman parte del estudio pero

que se excluyeron físicamente de la modelación, simulando el total de las emisiones

sólo en dos rutas.

Para su simulación se realizaron 42 polígonos, los que se presentan en la Figura 10.

En el Anexo 4.4.3 se encuentra un archivo digital que incluye todos los polígonos de

modelación para revisión.

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 21 de 75

**Figura 8. Polígonos de Modelación representativos de Calefacción.**

**Figura 9 Polígonos de Modelación representativos de Tránsito Interno**

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 22 de 75

**Figura 10 Polígonos de Modelación representativos de Tránsito Externo**

5.3.2 Receptores Discretos.

Para efectos de este estudio, se tomaron dos criterios:

1. Receptores dentro del sitio del proyecto, estos son representativos de viviendas y

otros que forman parte del proyecto. Se entiende que, en algunos casos, estos también

son fuentes de emisión.

En total receptores, se identificaron 30 receptores, algunos con edificaciones en altura,

por lo que se simuló la concentración a distintas alturas, las que se pueden ver en la

Tabla 3 y espacialmente en la Figura 11.

**Tabla 3 Receptores de Valle Noble**

|Receptor|Descripción|Coordenada UTM (m) HUSO 18 S|Col4|Altura (m)|
|---|---|---|---|---|
|**Receptor**|**Descripción**|**Este**|**Norte**|**Norte**|
|1|Colegio|677.827|5.923.434|1,6|
|1|Colegio|677.827|5.923.434|3,6|

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 23 de 75

|Receptor|Descripción|Coordenada UTM (m) HUSO 18 S|Col4|Altura (m)|
|---|---|---|---|---|
|**Receptor**|**Descripción**|**Este**|**Norte**|**Norte**|
|**Receptor**|**Descripción**|||5,6|
|2|Supermercado|677.889|5.923.401|1,6|
|3|Casas|677.767|5.923.407|1,6|
|4|Casas|677.743|5.923.486|1,6|
|5|Casas|677.718|5.923.572|1,6|
|6|Casas|677.887|5.923.571|1,6|
|7|Casas|677.747|5.923.716|1,6|
|8|Casas|677.899|5.923.660|1,6|
|9|Edificio|677.991|5.923.659|1,6|
|9|Edificio|677.991|5.923.659|7,6|
|9|Edificio|677.991|5.923.659|13,6|
|10|Casas|677.978|5.923.360|1,6|
|11|Casas|678.101|5.923.410|1,6|
|12|Casas|678.241|5.923.375|1,6|
|13|Casas|678.105|5.923.469|1,6|
|14|Casas|677.991|5.923.574|1,6|
|15|Casas|678.165|5.923.556|1,6|
|16|Casas|678.272|5.923.297|1,6|
|17|Casas|678.438|5.923.388|1,6|
|18|Casas|678.485|5.923.464|1,6|
|19|Casas|678.289|5.923.453|1,6|
|20|Casas|678.377|5.923.548|1,6|
|21|Casas|678.591|5.923.488|1,6|
|22|Casas|678.755|5.923.470|1,6|
|23|Casas|678.734|5.923.630|1,6|
|24|Casas|678.588|5.923.652|1,6|
|25|Edificio|678.428|5.923.708|1,6|
|25|Edificio|678.428|5.923.708|7,6|
|25|Edificio|678.428|5.923.708|13,6|
|26|Casas|678.654|5.923.821|1,6|
|27|Casas|678.622|5.923.727|1,6|
|28|Casas|678.768|5.923.717|1,6|
|29|Casas|678.779|5.923.868|1,6|
|30|Casas|678.709|5.923.938|1,6|

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

**Figura 11 Receptores en Valle Noble**

Página 24 de 75

2. Receptores fuera del sitio del proyecto, estos son representativos de

viviendas y otros cercanos al proyecto.

En total se consideraros 11 receptores, cuya información se presenta a

continuación:

**Tabla 4 Receptores cercanos al proyecto**

|Receptor|Descripción|Coordenada UTM (m) HUSO 18 S|Col4|Altura (m)|
|---|---|---|---|---|
|**Receptor**|**Descripción**|**Este**|**Norte**|**Norte**|
|1|Casas|679.321|5.923.971|1,6|
|2|Lugar de Trabajo|678.589|5.923.062|1,6|
|3|Lugar de Trabajo|677.893|5.923.243|1,6|
|4|Edificio|678.002|5.922.973|1,6|
|4|Edificio|678.002|5.922.973|3,6|
|4|Edificio|678.002|5.922.973|5,6|
|5|Lugar de Trabajo|677.590|5.923.456|1,6|

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 25 de 75

|Receptor|Descripción|Coordenada UTM (m) HUSO 18 S|Col4|Altura (m)|
|---|---|---|---|---|
|**Receptor**|**Descripción**|**Este**|**Norte**|**Norte**|
|6|Casas|677.672|5.923.001|1,6|
|7|Casas|677.463|5.923.300|1,6|
|8|Universidad|677.072|5.923.025|1,6|
|9|Colegio|677.053|5.923.270|1,6|
|9|Colegio|677.053|5.923.270|3,6|
|10|Lugar de Trabajo|677.199|5.923.573|1,6|
|11|Edificio|676.680|5.923.676|1,6|
|11|Edificio|676.680|5.923.676|3,6|
|11|Edificio|676.680|5.923.676|5,6|

**Figura 12 Receptores cercanos al proyecto**

En el Anexo 4.4.4 se presenta un archivo digital con los receptores.

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 26 de 75

# 6 Resultados

#### 6.1 . Modelamiento meteorológico

6.1.1 Caracterización de la velocidad y dirección de los vientos Anual

En la Figura 13 se presenta la rosa de los vientos anual, construida en base a las salidas del

modelo WRF, para el año 2022

**Figura 13. Rosa de los vientos anual**

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 27 de 75

La rosa de vientos resultante da cuenta que los vientos simulados tienen su origen desde la

componente oeste, nor noroeste y oeste suroeste. Los vientos entre estas coordenadas

abarcan un 33,6% del total de las direcciones de origen de los vientos en la zona. El origen

de los vientos con mayor frecuencia es la componente oeste, con un 16,1% del origen de

los vientos totales, seguida por la componente nor noroeste, con un 9,4%.

En la siguiente figura podemos ver la frecuencia de la velocidad de viento. Se observa una

mayor tendencia a vientos entre 0,5 - 2,1 m/s los cuales representan un 34,1% del total de

velocidades simuladas, mientras que los vientos entre 2,1 - 3,6 m/s y 3,6 - 5,7 m/s

representan un 33,6 % y un 20,2%. Podemos ver que la influencia de vientos más extremos,

como las calmas y aquellos cuya rapidez es mayor 5,7 m/s es baja, representando un 12,1%

del total de los vientos modelados.

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 28 de 75

**Figura 14. Frecuencia de la velocidad de los vientos anual**

6.1.2 Caracterización de la velocidad y dirección de los vientos Estacional

6.1.2.1 Caracterización de la velocidad y dirección del viento, verano

En la Figura 15 se presenta la rosa de los vientos para los meses de verano, construida en

base a las salidas del modelo WRF, para el año 2022.

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

**Figura 15. Rosa de los vientos en verano**

Página 29 de 75

La rosa de vientos resultante da cuenta que los vientos simulados tienen su origen desde

las componentes oeste, oeste suroeste y oeste noroeste. Los vientos entre estas

coordenadas abarcan un 46% del total de las direcciones de origen de los vientos en la

zona. El origen de los vientos con mayor frecuencia es la componente oeste, con un 24,7%

del origen de los vientos totales, seguida por la componente oeste suroeste, con un 11,4%.

En la Figura 16 podemos ver la frecuencia de la velocidad de viento para los meses de

verano. Se observa una mayor tendencia a vientos entre 0,5 - 2,1 m/s, los cuales

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 30 de 75

representan un 34,6% del total de velocidades simuladas, seguido por los vientos entre 2,1

- 3,6 m/s y 3,6 - 5,7 m/s, con un 33,5 % y 24,0 %, respectivamente. Además, podemos

observar un poco influencia de rapideces extremas, siendo los viento calmos y aquellos

sobre 5,7 m/s un 8,0 % del total.

**Figura 16. Frecuencia de la velocidad de los vientos en verano**

6.1.2.2 Caracterización de la velocidad y dirección del viento, otoño.

En la Figura 17 se presenta la rosa de los vientos para los meses de otoño, construida en

base a las salidas del modelo WRF, para el año 2022.

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

**Figura 17 Rosa de los vientos en otoño**

Página 31 de 75

La rosa de vientos resultante da cuenta que los vientos simulados tienen su origen desde

las componentes oeste, noreste y sur. Los vientos entre estas coordenadas abarcan un

33,6% del total de las direcciones de origen de los vientos en la zona. El origen de los

vientos con mayor frecuencia es el componente oeste, con un 13% del origen de los vientos

totales, seguido por los vientos con origen del noreste con un 10,4 %.

En la Figura 18 podemos ver la frecuencia de la velocidad de viento para los meses de

otoño. Asimismo, podemos observar que hay tendencia a modelar vientos entre 0,5 - 2,1

m/s, los cuales representan un 34,8% del total, seguidas por los vientos entre 2,1 - 3,6 m/s

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 32 de 75

y 3,6 - 5,7 m/s con un 33,5% y 18,6%, respectivamente. Además, podemos observar como

los vientos extremos, como las calmas y aquellos con una rapidez mayor a 5,7 m/s

representan un 13,1% del total.

**Figura 18 Frecuencia de la velocidad de los vientos en otoño**

6.1.2.3 Caracterización de la velocidad y dirección del viento, invierno.

En la Figura 19 se presenta la rosa de los vientos para los meses de invierno, construida en

base a las salidas del modelo WRF, para el año 2022.

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

**Figura 19 Rosa de los vientos en invierno**

Página 33 de 75

La rosa de vientos resultante da cuenta que los vientos simulados tienen su origen desde

las componentes este, norte y noreste. Los vientos entre estas coordenadas abarcan un

36,9% del total de las direcciones de origen de los vientos en la zona. El origen de los

vientos con mayor frecuencia es el componente este, con un 13,8% del origen de los vientos

totales, seguido por los vientos con origen del norte, con un 12%.

En la Figura 20 podemos ver la frecuencia de la velocidad de viento para los meses de

invierno. Podemos observar que hay tendencia a modelar vientos entre 0,5 - 2,1 m/s, los

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 34 de 75

cuales representan un 31,7% del total de velocidades simuladas, seguido por los vientos

entre 2,1 - 3,6 m/s y 3,6 - 5,7 m/s, con un 31,0% y un 20% del total. Además, podemos

ver que los vientos extremos, como las calmas y aquellas rapideces mayores a 5,7 m/s

representan un 17,3%.

**Figura 20 Frecuencia de la velocidad de los vientos en invierno**

6.1.2.4 Caracterización de la velocidad y dirección del viento, primavera.

En la Figura 21 se presenta la rosa de los vientos para los meses de primavera, construida

en base a las salidas del modelo WRF, para el año 2022.

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

**Figura 21 Rosa de los vientos en primavera**

Página 35 de 75

La rosa de vientos resultante da cuenta que los vientos simulados tienen su origen desde

las componentes oeste, oeste suroeste y nor noroeste. Los vientos entre estas coordenadas

abarcan un 39,6% del total de las direcciones de origen de los vientos en la zona. El origen

de los vientos con mayor frecuencia es la componente oeste, con un 20,6% del origen de

los vientos totales, seguido por los vientos con origen del oeste suroeste, con un 9,7%.

En la Figura 22 podemos ver la frecuencia de la velocidad de viento para los meses de

primavera. Podemos observar que hay tendencia a modelar vientos entre 2,1-3,6 m/s, los

cuales representan un 36,7% del total de velocidades simuladas.

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 36 de 75

**Figura 22 Frecuencia de la velocidad de los vientos en primavera.**

6.1.2.5 Perfil Diario de las velocidades del viento anuales.

En la siguiente figura se presenta el perfil horario promedio de las velocidades del viento

para cada estación del año, además de su evolución con respecto a las velocidades anuales,

con los datos extraídos del modelo WRF del año 2022.

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 37 de 75

**Figura 23 Perfil diario de velocidad del viento estacional**

Se aprecia de la figura anterior, que el comportamiento de la velocidad de los vientos para

las distintas estaciones del año, en relación con la variación anual, es muy similar. Se aprecia

que la velocidad de los vientos en las distintas estaciones del año sigue la misma tendencia

que las velocidades anuales, salvo los meses de invierno, el cual mantiene velocidades en

torno a los 2,75-3,5 m/s.

Vemos que la velocidad del viento tiende a disminuir constantemente entre las 00:00 a

04:00 horas, luego comienzan a aumentar alcanzando su máximo entre las 12 y 15 UTC,

alcanzando variación mayor a 1,72 m/s. Esta diferencia aumenta a 2,95 m/s en verano y

disminuye a 0,7 m/s en invierno. Estas variaciones se deben a las diferencias en las

temperaturas alcanzadas en dichas estaciones.

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

6.1.3 Caracterización de la Temperatura del Aire

6.1.3.1 Temperatura mensual.

Página 38 de 75

Tal como se ve en la Figura 24, la simulación del modelo meteorológico (WRF) sugiere que

la temperatura promedio mensual disminuye paulatinamente a partir del mes de enero hasta

julio. Desde entonces se observa un aumento sostenido hasta diciembre.

En este sentido la temperatura promedio más alta se simuló para el mes de febrero, donde

alcanzarían los 17,42°C, en tanto que la mínima temperatura promedio mensual se espera

en el mes de Julio donde llegaría a los 9,43°c.

Con respecto a la amplitud térmica se observa que esta es mayor en el mes de diciembre

con un valor de 25,61°C, mientras que la más baja ocurre en el mes de junio, alcanzado los

13,51°C.

**Figura 24 Perfil mensual de temperatura**

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

6.1.3.2 Perfil diario de Temperatura.

Página 39 de 75

La simulación del modelo meteorológico WRF dentro del área de estudio, demuestra que

las temperaturas horarias simuladas tienen una misma tendencia en todas las estaciones

del año. En efecto, tal como se muestra en la Figura 14, la evolución de la temperatura

diaria resulta tener una leve disminución entre las 00:00 y 06:00 horas, a partir de entonces

la temperatura aumenta hasta alcanzar temperaturas máximas entre las 12:00 y 15:00

horas, luego la temperatura disminuye constantemente hasta las 23:00 horas.

**Figura 25 Perfil diario de temperatura**

Además, se hace visible que en los meses de verano la amplitud térmica diaria es mayor

que en las otras estaciones del año, llegando a una diferencia de 7,78°C entre la mínima y

máxima promedio horario. Durante los meses de primavera la amplitud térmica es menor

bordeando los 6,77°C. Durante los meses de otoño la amplitud térmica es menor bordeando

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 40 de 75

los 6,59°C. Por último, en los meses de invierno la amplitud termina es inferior a la alcanzada

en las otras estaciones llegando los 3,63°C.

6.1.4 Caracterización de la Precipitación

A partir de la modelación meteorológica del modelo WRF se obtienen las precipitaciones del

lugar, que es un parámetro importante en cuanto a la potencial deposición húmeda de

algunos contaminantes.

Según los resultados presentados por el modelo WRF, se concluye que, para la zona de

interés, el total de precipitación para el año 2022 es de 1290,37 mm.

**Figura 26 Perfil mensual de la temperatura**

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 41 de 75

En la anterior se muestra la precipitación mensual para el año de estudio, de donde se

concluye que la precipitación se concentra en los meses de julio y junio, en donde precipita

el 53,84% del total anual.

6.1.5 Altura Capa de meza

La altura de la capa de mezcla se define como la capa de la atmósfera (tropósfera) que está

influenciada de manera directa con las condiciones de la superficie del suelo, y es donde se

da lugar la turbulencia mecánica y térmica (transferencia de calor y materia) de los gases y

partículas presentes en ella (contaminantes), proceso característico de la troposfera baja.

En términos generales, la altura de la capa de mezcla varía de unos cuantos kilómetros en

el día a unos cientos de metros en la noche.

El modelo WRF es capaz de simular el comportamiento horario de la altura de capa de

mezcla. De hecho, tal como se observa en la Figura 27, el comportamiento de la capa de

mezcla muestra un aumento de su altura desde el horario de salida del sol (entre 06:00 a

08:00 am) teniendo su mayor valor entre las 12:00 a las 15:00 horas, la cual tiene una

altura máxima cercana a los 700 metros para el verano, otoño y primavera, mientras que

en invierno su altura máxima es de aproximadamente 540 metros. Luego de este periodo

del día, la altura de la capa disminuye debido a la menor influencia de la radiación reflejada

(albedo) de la superficie. Por último, durante la noche y madrugada, la altura de capa de

mezcla alcanza sus menores valores, debido a una menor influencia del albedo. Este

comportamiento es el esperado, resaltando el hecho que, en verano y primavera, las alturas

máximas de la capa sean mayores que en invierno debido a la influencia de la radiación

solar.

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 42 de 75

**Figura 27 Perfil diario de la altura de la capa de mezcla.**

Lo anterior, se explica debido a que la capa de mezcla se hace más estable durante las

noches, debido a la ausencia de aporte energético del sol, influyendo negativamente en el

intercambio vertical, de este modo, la turbulenta térmica es prácticamente nula. Con la

salida del sol, el calentamiento de la superficie terrestre es transmitido a la atmósfera,

produciendo agitación en la capa de mezcla, lo que provoca un incremento en el espesor

del volumen del aire afectado por el suelo, llegando al máximo entre las 12:00 y 15:00 horas

del día, es en este momento del día en donde se propician las condiciones de máxima

inestabilidad atmosférica, favoreciendo la turbulencia térmica y la dispersión de

contaminantes.

Por ende, y a modo de conclusión, se puede mencionar que este parámetro es importante

para la concentración de un contaminante, ya que a medida que disminuye la altura de capa

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 43 de 75

de mezcla, el contaminante tiende a concentrarse, y, por el contrario, a medida que se aleja

de la superficie, el contaminante tiende a dispersarse.

#### 6.2 Concentraciones Modeladas

6.2.1 Dispersión e Isoconcentración Material Particulado Respirable MP10

Para el presente estudio se modelaron 37,81 ton/año, entre fuentes representativas del

tránsito de vehículos, tanto en el interior del proyecto como fuera de él; además de la

calefacción residencial.

Los resultados demuestran que las emisiones del proyecto se dispersan dentro del sitio del

proyecto, influenciados principalmente por las emisiones de calefacción residencia. Si bien,

la mayoría de las emisiones provienen por las rutas externas, al haberlas representado en

toda su longitud la concentración que alcanzan en el aire son de baja magnitud con relación

a aquellas que se generan por la calefacción residencias, las cuales se generan dentro del

mismo proyecto la una muy cerca de la otra, por lo que generan una mayor concentración

en el aire.

Tanto para el MP 10 en su concentración promedio anual como 24 horas, la dispersión de los

contaminantes nace desde la zona del proyecto y se dispersan por la zona circundante, tal

como se puede ver en las Figura 28 y Figura 29. Como era de esperar, los receptores que

se ubican dentro de la pluma de dispersión corresponden en su mayoría a los

representativos del propio proyecto, los que además son fuentes de emisión.

En relación con la pluma de dispersión de MP 10 como promedio anual, se destaca:

 - La pluma de dispersión tiene un área total de 98,8 ha, de las cuales más del 46% se

encuentra dentro del propio proyecto.

 - La pluma de dispersión se desplaza desde el centro del proyecto en 400 m al norte,

405 m al sur, 680 m al este y 638 m al oeste.

 - Las concentraciones varían desde 0,64 μg/m [3] hasta 0,22 μg/m [3] .

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 44 de 75

 - La zona de máxima concentración tiene una superficie de 8,62 ha, alcanzando el

punto de máxima concentración en la coordenada UTM, HUSO 18 S WGS 84:

Este: 678.166 m

Norte: 5.923.394 m

En el Anexo 4.4.3 se presenta la pluma de dispersión y el punto de máximo impacto en

formato kmz.

Con respecto a la pluma de dispersión de MP 10 como promedio 24 horas, se destaca:

 - La pluma de dispersión tiene un área total de 226 ha, en donde se puede observar

que el proyecto se encuentra totalmente inmerso en ella.

 - La pluma de dispersión se desplaza desde el centro del proyecto en 820 m al norte,

682 m al sur, 966 m al este y 834 m al oeste.

 - Las concentraciones varían desde 4,00 μg/m [3] hasta 1,00 μg/m [3] .

 - La zona de máxima concentración tiene una superficie de 1,72 ha, alcanzando el

punto de máxima concentración en la coordenada UTM, HUSO 18 S WGS 84:

Este: 678.324 m

Norte: 5.923.514 m

En el Anexo 4.4.3 se presenta la pluma de dispersión y el punto de máximo impacto en

formato kmz.

**Figura 28 Isoconcentración de MP10 como promedio anual**

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 46 de 75

**Figura 29 Isoconcentración de MP10 como promedio 24 horas**

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 47 de 75

6.2.2 Dispersión e Isoconcentración Material Particulado Fino Respirable MP 2.5

Para el presente estudio se modelaron 15,23 ton/año, entre fuentes representativas del

tránsito de vehículos tanto en el interior del proyecto como fuera de él; además de la

calefacción residencial, siendo esta actividad la que más aporta al inventario del proyecto.

Al igual que en el caso de MP 10, la pluma de dispersión se encuentra principalmente

influenciada por las emisiones de la calefacción residencial, la que no sólo constituye la

mayor fuente de emisión de MP 2,5, sino que también la ubicación espacial de las fuentes.

Tanto para el MP 2,5 en su concentración promedio anual como 24 horas, la dispersión de los

contaminantes nace desde la zona del proyecto y se dispersan por la zona circundante, tal

como se puede ver en las Figura 30 y Figura 31. Como era de esperar, los receptores que

se ubican dentro de la pluma de dispersión corresponden en su mayoría a los

representativos del propio proyecto, los que además son fuentes de emisión.

En relación con la pluma de dispersión de MP 2,5 como promedio anual, se destaca:

 - La pluma de dispersión tiene un área total de 50,03 ha, de las cuales más del 74%

se encuentra dentro del propio proyecto.

 - La pluma de dispersión se desplaza desde el centro del proyecto en 298 m al norte,

340 m al sur, 511 m al este y 469 m al oeste.

 - Las concentraciones varían desde 0,58 μg/m [3] hasta 0,30 μg/m [3] .

 - La zona de máxima concentración tiene una superficie de 0,03 ha, alcanzando el

punto de máxima concentración en la coordenada UTM, HUSO 18 S WGS 84:

Este: 678.063 m

Norte: 5.923.307 m

En el Anexo 4.4.3 se presenta la pluma de dispersión y el punto de máximo impacto en

formato kmz.

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 48 de 75

Con respecto a la pluma de dispersión de MP 2,5 como promedio 24 horas, se destaca:

 - La pluma de dispersión tiene un área total de 89,73 ha, en donde se puede observar

que el proyecto se encuentra totalmente inmerso en ella.

 - La pluma de dispersión se desplaza desde el centro del proyecto en 509 m al norte,

400 m al sur, 640 m al este y 520 m al oeste.

 - Las concentraciones varían desde 3,5 μg/m [3] hasta 2,00 μg/m [3] .

 - La zona de máxima concentración tiene una superficie de 10,9 ha, alcanzando el

punto de máxima concentración en la coordenada UTM, HUSO 18 S WGS 84:

Este: 678.324 m

Norte: 5.923.514 m

En el Anexo 4.4.3 se presenta la pluma de dispersión y el punto de máximo impacto en

formato kmz.

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 49 de 75

**Figura 30 Isoconcentración de MP2,5 como promedio anual**

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 50 de 75

**Figura 31 Isoconcentración de MP2,5 como promedio 24 horas**

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

6.2.3 Modelación discreta de las emisiones contaminantes

Página 51 de 75

Los resultados de la modelación discreta son congruentes con la modelación obtenida en

las plumas de dispersión.

En la Tabla 5 se presenta la concentración modelada para cada receptor ubicado en Valle

Noble y en la Tabla 6 se presentan los resultados para los receptores cercanos al proyecto.

Para todos los casos se puede observar:

1. Se utilizó como concentración basal las registradas en la EMRP Kingston College para

el año 2022 y que fueron presentadas en el apartado 3.2.

2. En la Tabla 5 se presentan las concentraciones modeladas de MP 10 y MP 2,5 en sus

concentraciones anuales y 24 horas.

En el caso de MP 10 en su concentración promedio anual, el aumento frecuentemente

fue del ~1%, llegando a un máximo del 2% en los receptores 11, 12 y 13. Respecto

a la concentración de este contaminante como 24 horas, la variación del aumento

llega a un máximo del 4% en los receptores 1, 9, 12, 17, 18, 21, 24 y 25.

Respecto al MP 2,5 el aumento del promedio anual varió entre el 1% y 3%, siendo

máxima la proyección del aumento en los recetores 11, 12 y 13. Del mismo modo,

la concentración 24 horas para el MP 2,5 varió en el aumento en una relación

porcentual del 1% al 6%, los receptores que experimentaron un mayor aumento fue

el receptor 25.

Más allá del aumento porcentual se observa que las concentraciones se observan

que las concentraciones proyectadas son de baja magnitud respecto de la situación

base, por lo cual, el desarrollo del proyecto no presume un escenario

sustancialmente distinto al actual, sino que los aumentos son mínimos y que no

afectarán la salud de la población ni la calidad de vida de los receptores.

3. En la Tabla 6 se presentan las concentraciones modeladas de MP 10 y MP 2,5 en sus

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

concentraciones anuales y 24 horas.

Página 52 de 75

En el caso de MP 10 en su concentración promedio anual, fue del ~1% en los

receptores 1, 2, 3 y 4, en tanto que en el resto de los receptores el aumento fue

cercano a 0. Por su parte, la concentración promedio 24 h, experimentó un aumento

de entre 0% y 3%, siendo máximo en el receptor 3 y 4.

Respecto al MP 2,5 el aumento del promedio anual varió entre el 0% y 2%, siendo

máxima la proyección del aumento para el receptor 1. Del mismo modo, la

concentración 24 horas para el MP 2,5 varió en el aumento en una relación porcentual

del 0% al 4%, los receptores que experimentaron un mayor aumento fue el recetor

3.

Más allá del aumento porcentual se observa que las concentraciones proyectadas

son de baja magnitud respecto de la situación base, por lo cual, el desarrollo del

proyecto no presume un escenario sustancialmente distinto al actual, sino que los

aumentos son mínimos y que no afectarán la salud de la población ni la calidad de

vida de los receptores.

4. Finalmente, cabe destacar que en el caso de los receptores representativos de

edificios o establecimientos educacionales se modelaron las concentraciones a

distintas alturas, con el fin de identificar distintos potenciales impactos, demostrando

que a distancias medias las concentraciones eran máximas, lo que tiene sentido,

toda vez que las concentraciones se encuentran influenciadas por la calefacción

residencial, cuya liberación ocurre en los tubos de salida a una altura que simula la

salida por un segundo piso.

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 53 de 75

**Tabla 5. Concentraciones Modeladas en Receptores de Valle Noble.**

|Receptor|Descripción|Altura (m)|Concentración MP10 (μg/m3)|Col5|Col6|Col7|Col8|Col9|Concentración MP2,5 (μg/m3)|Col11|Col12|Col13|Col14|Col15|Col16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Altura (m)**|**Modelada**|**Modelada**|**Línea de**<br>**base**|**Línea de**<br>**base**|**Proyectada**|**Proyectada**|**Modelada**|**Modelada**|**Línea de base**|**Línea de base**|**Proyectada**|**Proyectada**|**Proyectada**|
|**Receptor**|**Descripción**|**Altura (m)**|Anual|24 h|Anual|24 h|Anual|24 h|Anual|24 h|Anual|24 h|24 h|Anual|24 h|
|1|Colegio|1,6|0,24|1,33|25,0|52,3|25,24|53,63|0,22|1,22|14,1|37,6|37,6|14,32|38,82|
|1|Colegio|3,6|0,27|1,75|25,0|52,3|25,27|54,05|0,25|1,61|14,1|37,6|37,6|14,35|39,21|
|1|Colegio|5,6|0,29|1,98|25,0|52,3|25,29|54,28|0,26|1,82|14,1|37,6|37,6|14,36|39,42|
|2|Supermercado|1,6|0,26|1,42|25,0|52,3|25,26|53,72|0,24|1,31|14,1|37,6|37,6|14,34|38,91|
|3|Casas|1,6|0,24|1,11|25,0|52,3|25,24|53,41|0,22|1,11|14,1|37,6|37,6|14,32|38,71|
|4|Casas|1,6|0,27|1,29|25,0|52,3|25,27|53,59|0,24|1,18|14,1|37,6|37,6|14,34|38,78|
|5|Casas|1,6|0,21|1,03|25,0|52,3|25,21|53,33|0,19|0,95|14,1|37,6|37,6|14,29|38,55|
|6|Casas|1,6|0,29|1,44|25,0|52,3|25,29|53,74|0,27|1,32|14,1|37,6|37,6|14,37|38,92|
|7|Casas|1,6|0,19|1,11|25,0|52,3|25,19|53,41|0,18|1,02|14,1|37,6|37,6|14,28|38,62|
|8|Casas|1,6|0,24|1,34|25,0|52,3|25,24|53,64|0,22|1,23|14,1|37,6|37,6|14,32|38,83|
|9|Edificio|1,6|0,19|1,2|25,0|52,3|25,19|53,5|0,17|1,11|14,1|37,6|37,6|14,27|38,71|
|9|Edificio|7,6|0,24|1,99|25,0|52,3|25,24|54,29|0,22|1,84|14,1|37,6|37,6|14,32|39,44|
|9|Edificio|13,6|0,12|0,57|25,0|52,3|25,12|52,87|0,11|0,52|14,1|37,6|37,6|14,21|38,12|
|10|Casas|1,6|0,37|1,79|25,0|52,3|25,37|54,09|0,34|1,65|14,1|37,6|37,6|14,44|39,25|
|11|Casas|1,6|0,41|1,7|25,0|52,3|25,41|54|0,38|1,57|14,1|37,6|37,6|14,48|39,17|
|12|Casas|1,6|0,39|2,02|25,0|52,3|25,39|54,32|0,36|1,86|14,1|37,6|37,6|14,46|39,46|
|13|Casas|1,6|0,4|1,67|25,0|52,3|25,4|53,97|0,36|1,54|14,1|37,6|37,6|14,46|39,14|
|14|Casas|1,6|0,3|1,51|25,0|52,3|25,3|53,81|0,27|1,39|14,1|37,6|37,6|14,37|38,99|
|15|Casas|1,6|0,33|1,51|25,0|52,3|25,33|53,81|0,31|1,39|14,1|37,6|37,6|14,41|38,99|
|16|Casas|1,6|0,33|1,8|25,0|52,3|25,33|54,1|0,3|1,67|14,1|37,6|37,6|14,4|39,27|
|17|Casas|1,6|0,35|1,85|25,0|52,3|25,35|54,15|0,31|1,71|14,1|37,6|37,6|14,41|39,31|
|18|Casas|1,6|0,33|1,84|25,0|52,3|25,33|54,14|0,3|1,7|14,1|37,6|37,6|14,4|39,3|

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 54 de 75

|Receptor|Descripción|Altura (m)|Concentración MP10 (μg/m3)|Col5|Col6|Col7|Col8|Col9|Concentración MP2,5 (μg/m3)|Col11|Col12|Col13|Col14|Col15|Col16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Altura (m)**|**Modelada**|**Modelada**|**Línea de**<br>**base**|**Línea de**<br>**base**|**Proyectada**|**Proyectada**|**Modelada**|**Modelada**|**Línea de base**|**Línea de base**|**Proyectada**|**Proyectada**|**Proyectada**|
|**Receptor**|**Descripción**|**Altura (m)**|Anual|24 h|Anual|24 h|Anual|24 h|Anual|24 h|Anual|24 h|24 h|Anual|24 h|
|19|Casas|1,6|0,38|1,72|25,0|52,3|25,38|54,02|0,34|1,59|14,1|37,6|37,6|14,44|39,19|
|20|Casas|1,6|0,31|1,57|25,0|52,3|25,31|53,87|0,29|1,46|14,1|37,6|37,6|14,39|39,06|
|21|Casas|1,6|0,35|1,84|25,0|52,3|25,35|54,14|0,32|1,7|14,1|37,6|37,6|14,42|39,3|
|22|Casas|1,6|0,23|1,15|25,0|52,3|25,23|53,45|0,21|1,06|14,1|37,6|37,6|14,31|38,66|
|23|Casas|1,6|0,23|1,21|25,0|52,3|25,23|53,51|0,22|1,12|14,1|37,6|37,6|14,32|38,72|
|24|Casas|1,6|0,37|1,94|25,0|52,3|25,37|54,24|0,34|1,79|14,1|37,6|37,6|14,44|39,39|
|25|Edificio|1,6|0,19|1,34|25,0|52,3|25,19|53,64|0,18|1,24|14,1|37,6|37,6|14,28|38,84|
|25|Edificio|7,6|0,25|2,31|25,0|52,3|25,25|54,61|0,23|2,14|14,1|37,6|37,6|14,33|39,74|
|25|Edificio|13,6|0,12|0,54|25,0|52,3|25,12|52,84|0,11|0,5|14,1|37,6|37,6|14,21|38,1|
|26|Casas|1,6|0,24|1,21|25,0|52,3|25,24|53,51|0,22|1,12|14,1|37,6|37,6|14,32|38,72|
|27|Casas|1,6|0,3|1,43|25,0|52,3|25,3|53,73|0,28|1,32|14,1|37,6|37,6|14,38|38,92|
|28|Casas|1,6|0,18|1,01|25,0|52,3|25,18|53,31|0,16|0,94|14,1|37,6|37,6|14,26|38,54|
|29|Casas|1,6|0,17|1,06|25,0|52,3|25,17|53,36|0,15|0,98|14,1|37,6|37,6|14,25|38,58|
|30|Casas|1,6|0,2|0,99|25,0|52,3|25,2|53,29|0,18|0,91|14,1|37,6|37,6|14,28|38,51|

**Tabla 6 Concentraciones Modeladas en Receptores de cercanos a Valle Noble**

|Receptor|Descripción|Altura (m)|Concentración MP10 (μg/m3)|Col5|Col6|Col7|Col8|Col9|Concentración MP2,5 (μg/m3)|Col11|Col12|Col13|Col14|Col15|Col16|Col17|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Altura (m)**|**Modelada**|**Modelada**|**Línea de**<br>**base**|**Línea de**<br>**base**|**Proyectada**|**Proyectada**|**Modelada**|**Modelada**|**Línea de base**|**Línea de base**|**Línea de base**|**Proyectada**|**Proyectada**|**Proyectada**|
|**Receptor**|**Descripción**|**Altura (m)**|Anual|24 h|Anual|24 h|Anual|24 h|Anual|24 h|24 h|Anual|24 h|24 h|Anual|24 h|
|31|Casas|1,6|1,6|0,24|1,3|25|52,3|25,24||0,22|0,22|1,19|14,1|14,1|37,6|14,32|
|32|Lugar de Trabajo|1,6|1,6|0,18|1,21|25|52,3|25,18||0,16|0,16|1,12|14,1|14,1|37,6|14,26|
|33|Lugar de Trabajo|1,6|1,6|0,19|1,47|25|52,3|25,19||0,18|0,18|1,36|14,1|14,1|37,6|14,28|

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 55 de 75

|Receptor|Descripción|Altura (m)|Concentración MP10 (μg/m3)|Col5|Col6|Col7|Col8|Col9|Concentración MP2,5 (μg/m3)|Col11|Col12|Col13|Col14|Col15|Col16|Col17|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Altura (m)**|**Modelada**|**Modelada**|**Línea de**<br>**base**|**Línea de**<br>**base**|**Proyectada**|**Proyectada**|**Modelada**|**Modelada**|**Línea de base**|**Línea de base**|**Línea de base**|**Proyectada**|**Proyectada**|**Proyectada**|
|**Receptor**|**Descripción**|**Altura (m)**|Anual|24 h|Anual|24 h|Anual|24 h|Anual|24 h|24 h|Anual|24 h|24 h|Anual|24 h|
|34|Edificio|1,6|1,6|0,19|1,41|25|52,3|25,19||0,18|0,18|1,29|14,1|14,1|37,6|14,28|
|34|Edificio|3,6|3,6|0,15|0,9|25|52,3|25,15||0,13|0,13|0,82|14,1|14,1|37,6|14,23|
|34|Edificio|5,6|5,6|0,11|0,67|25|52,3|25,11||0,1|0,1|0,61|14,1|14,1|37,6|14,2|
|35|Lugar de Trabajo|1,6|1,6|0,09|0,53|25|52,3|25,09||0,08|0,08|0,48|14,1|14,1|37,6|14,18|
|36|Casas|1,6|1,6|0,04|0,24|25|52,3|25,04||0,04|0,04|0,22|14,1|14,1|37,6|14,14|
|37|Casas|1,6|1,6|0,04|0,21|25|52,3|25,04||0,04|0,04|0,19|14,1|14,1|37,6|14,14|
|38|Universidad|1,6|1,6|0,05|0,24|25|52,3|25,05||0,04|0,04|0,22|14,1|14,1|37,6|14,14|
|39|Colegio|1,6|1,6|0,05|0,28|25|52,3|25,05||0,04|0,04|0,25|14,1|14,1|37,6|14,14|
|39|Colegio|3,6|3,6|0,03|0,12|25|52,3|25,03||0,02|0,02|0,1|14,1|14,1|37,6|14,12|
|40|Lugar de Trabajo|1,6|1,6|0,03|0,13|25|52,3|25,03||0,02|0,02|0,11|14,1|14,1|37,6|14,12|
|41|Edificio|1,6|1,6|0,03|0,15|25|52,3|25,03||0,02|0,02|0,12|14,1|14,1|37,6|14,12|

A continuación, se presenta en ciclo diario de la concentración por cada mes del año, de donde se comprueba que efectivamente las

concentraciones se encuentran fuertemente influenciadas por la calefacción residencial, la que fue simulada en los meses de otoñoinvierno, con un uso de 12 horas al día, segregado en mañana y tarde.

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 56 de 75

**Figura 32. Ciclo diario de la concentración por cada mes del año, para los receptores del 1 al 12.**

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 57 de 75

**Figura 33. Ciclo diario de la concentración por cada mes del año, para los receptores del 13 al 24.**

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 58 de 75

**Figura 34. Ciclo diario de la concentración por cada mes del año, para los receptores del 25 al 36.**

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 59 de 75

**Figura 35 Ciclo diario de la concentración por cada mes del año, para los receptores del 37 al 48.**

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 60 de 75

En la Figura 36, Figura 37, Figura 38 y Figura 39 se presentan las serie de tiempo para todos

los receptores en donde se simularon las concentraciones de MP 10, de donde se observa

que no hay picos de concentración que presuman una exposición aguda a altas

concentraciones por el desarrollo del proyecto. Del mismo modo en la Figura 40, Figura 41,

Figura 42 y Figura 43 se presenta para el MP 2,5 donde el comportamiento es similar al del

MP 10 .

**Figura 36. Series de tiempo de las concentraciones de MP10, para los**

**receptores del 1 al 12.**

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 61 de 75

**Figura 37 Series de tiempo de las concentraciones de MP10, para los receptores**

**del 13 al 24.**

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 62 de 75

**Figura 38. Series de tiempo de las concentraciones de MP10, para los**

**receptores del 25 al 36.**

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 63 de 75

**Figura 39 Series de tiempo de las concentraciones de MP10, para los receptores**

**del 37 al 48.**

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 64 de 75

**Figura 40. Series de tiempo de las concentraciones de MP2,5, para los**

**receptores del 1 al 12.**

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 65 de 75

**Figura 41. Series de tiempo de las concentraciones de MP2,5, para los**

**receptores del 13 al 24.**

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 66 de 75

**Figura 42. Series de tiempo de las concentraciones de MP2,5, para los**

**receptores del 25 al 36.**

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 67 de 75

**Figura 43. Series de tiempo de las concentraciones de MP2,5, para los**

**receptores del 37 al 48.**

#### 6.3 Aporte a la estación de Monitorio de Representatividad Poblacional (EMRP)

A continuación, se presentan los resultados de la concentración de MP 2,5 simuladas en la

EMRP Kingston College y la proyección con el año de mayor emisión del proyecto. En la

Tabla 7, se observa el aumento de la concentración basal registrada en la EMRP entre enero

y diciembre de 2022 para MP 10 y MP 2,5 .

Los resultados evidencian un aumento de la condición basal del 0,01% para los

contaminantes en su concentración promedio anual y del 0,03% en la concentración 24

horas, concluyendo que dicho aumento en la EMRP no es sustancial.

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 68 de 75

**Tabla 7. Aumento de la concentración basal en la EMRP Kingston College, año**

**2022**

|Contaminante|Col2|Registro EMRP|Modelado|Proyectado|Porcentaje<br>de aumento|
|---|---|---|---|---|---|
|MP10|Anual|25,0|0,002|25,00|0,01%|
|MP10|24 horas|52,3|0,014|52,31|0,03%|
|MP2,5|Anual|14,1|0,002|14,10|0,01%|
|MP2,5|24 horas|37,6|0,012|37,61|0,03%|

Por lo cual, teniendo en cuenta que esta estación representa zonas urbanas pobladas de la

ciudad y es la estación más próxima al proyecto en evaluación, resulta importante destacar

que se prevé un **aumento no significativo en la condición basal registrada en esta**

**estación y que la puesta en marcha del proyecto, no representa un**

**empeoramiento sustancial de la calidad del aire.**

# 7 Análisis de incertidumbre

La “Guía para el Uso de Modelos de Calidad del Aire en el SEIA” (SEA, 2023) plantea que

los procesos de modelamiento pretenden simular un proceso acercándose a la realidad, con

ciertas licencias, que en definitiva resultan en incertidumbre.

Tal como lo señala la guía, para efectos de este estudio, la incertidumbre será expresada a

través de las diferencias, tanto cualitativas como cuantitativas, entre los datos modelados y

observados en el dominio de modelación. Cabe señalar, que la “Guía para el Uso de Modelos

de Calidad del Aire en el SEIA” (SEA, 2023) señala que no se han de ponderar la

incertidumbre del modelo meteorológico a los valores de concentración obtenidos de la

simulación de las concentraciones.

La selección de la estación para el análisis de incertidumbre se realizó con base a la calidad

de los datos, en concreto, se utilizó la estación meteorológica Carriel Sur para el año 2022.

De acuerdo con los criterios de la guía, la elección meteorológica se encuentra en el nivel

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 69 de 75

3, comunal o regional en donde se observa que esta se encuentra fuera del área de

influencia (AI) aproximadamente a 7 km del proyecto, tal como se observa en la Figura 44.

**Figura 44 Ubicación de la Estación Meteorológica**

#### 7.1 Análisis cualitativo

De acuerdo con el apartado 6.2.1. de la “Guía para el Uso de Modelos de Calidad del Aire

en el SEIA” (SEA, 2023) el análisis debe centrarse en la velocidad y dirección del viento,

temperatura, humedad absoluta o relativa y precipitación. Sin embargo, la humedad no es

una variable que suela medirse en las estaciones meteorológicas.

En relación a la temperatura, en el siguiente gráfico, se observa la frecuencia de

temperaturas simuladas, de donde se observa que son similares en los distintos segmentos

de temperaturas, por lo que se concluye que el modelo es capaz de simular con alto grado

de exactitud las temperaturas en la zona circundante.

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 70 de 75

**Figura 45 Frecuencia de temperaturas comparadas.**

En la Figura 46 se observa la frecuencia para el viento, de donde se puede observar una

mayor variabilidad respecto a la temperatura. Sin embargo, no son sustanciales, a excepción

de los vientos de 5,7 - 8,8 m/s en donde el modelo simula vientos menos frecuentes con

estas magnitudes y, los vientos calmos, en donde los vientos modelados son mayores a los

que se registran en la estación.

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

**Figura 46 Frecuencia de viento comparadas.**

#### 7.2 Análisis cuantitativo

Página 71 de 75

El análisis cuantitativo por realizar se basará en los contenidos solicitados en la “Guía para

el Uso de Modelos de Calidad del Aire en el SEIA” (SEA, 2023) evaluando las métricas

estadísticas del sesgo (BIAS), error absoluto medio (MAE) y la raíz del error cuadrático medio

(RMSE), además del coeficiente de correlación (r); las ecuaciones que basan su cálculo son:

n

BIAS = [1]

n [ ∑(S] [i] [−O] [i] [)]

i=1

n

MAE = [1]

n [ ∑|S] [i] [−O] [i] [|]

i=1

n

RMSE = √ [1]

n

n [ ∑(S] [i] [−O] [i] [)] [2]

i=1

Donde:

i, es la variable meteorológica.

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

n, es la cantidad de datos.

S, son los valores modelados.

O, son los valores observados.

Página 72 de 75

El coeficiente de correlación lineal es una medida de relación de Pearson entre dos variables

y se usa para medir el grado de relación entre ellas. El rango de valores va desde el -1 al 1

y está representado por la siguiente ecuación.

r = [σ] [x][y]
xy

σ x . σ y

Donde,

 - σ xy, es la covarianza entre x e y;

 - σx, es la desviación estándar de x;

 - σy, es la desviación estándar de y;

En la siguiente tabla se presentan los resultados de las medidas estadísticas, prueba del

desempeño del modelo.

**Tabla 8 Métricas estadísticas para el análisis de incertidumbre**

|Estadístico|Velocidad del viento|Temperatura|
|---|---|---|
|BIAS|-0,53|0,30|
|MAE|1,29|2,00|
|RMSE|1,64|2,62|
|Coeficiente de correlación|0,7|0,8|

Se concluye que el modelo tiene un rendimiento aceptable de representación de acuerdo

con la Tabla 2 de la “Guía para el Uso de Modelos de Calidad del Aire en el SEIA” (SEA,

2023) toda vez que los valores de los estadísticos del modelo se encuentran dentro de los

rangos recomendados por la guía.

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 73 de 75

# 8 Conclusión

Se estudió la concentración de las emisiones producto de la construcción y operación del

proyecto en evaluación, proyectadas para el año 23 del **“Proyecto Modificación**

**Proyecto Inmobiliario Valle Noble”** ubicado en la comuna de Concepción, Región del

Biobío. De esta forma, fueron modeladas las emisiones MP 10 y MP 2,5 a fin de determinar las

concentraciones que éstos tendrán en la atmósfera, además de prever posibles efectos a la

salud de las personas.

La concentración en el aire de los contaminantes depende de múltiples factores, entre ellos

la tasa de emisión de las fuentes, además de las características topográficas y

meteorológicas de la zona.

En este sentido, la caracterización de las dos últimas variables es de importancia en la

elección de los modelos de uso meteorológico sobre los cuales se simula la dispersión y

concentración de los contaminantes, las que en este caso se hizo según los lineamientos

establecidos por el servicio de evaluación ambiental “Guía para el uso de Modelos de Calidad

del Aire en el SEIA” (SEA, 2023). Esta guía recomienda utilizar WRF, el cual fue empleado

para la modelación y dispersión de contaminantes; cuya implementación tiene ciertas

limitaciones, más, sin embargo, la representatividad del modelo se ajusta a las

recomendaciones del SEA en la guía para la modelación, según los estadísticos de ajusto

del modelo analizados para la estación Carriel Sur, tal como se presentó en la Tabla 8.

<!-- INICIO TABLA 8 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- En la siguiente tabla se presentan los resultados de las medidas estadísticas, prueba del desempeño del modelo. -->

**Tabla 8: Métricas estadísticas para el análisis de incertidumbre****

| Estadístico | Velocidad del viento | Temperatura |
| --- | --- | --- |
| BIAS | -0,53 | 0,30 |
| MAE | 1,29 | 2,00 |
| RMSE | 1,64 | 2,62 |
| Coeficiente de correlación | 0,7 | 0,8 |

<!-- Estadísticas: 4 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Se concluye que el modelo tiene un rendimiento aceptable de representación de acuerdo con la Tabla 2 de la “Guía para el Uso de Modelos de Calidad del Aire en el SEIA” (SEA, -->
<!-- FIN TABLA 8 -->


Para efectos de este estudio se modelaron todas las emisiones del proyecto para el año 23,

las que correspondían a tres fuentes: calefacción residencial, transporte interno y externo.

Los resultados demuestran que las concentraciones se encuentran fuertemente

influenciadas por las emisiones provenientes de la calefacción.

En general se observa que, si bien las plumas de dispersión abarcan una amplia área, las

concentraciones son de baja concentración y que se emplaza principalmente en la zona del

proyecto, abarcando en algunos casos la totalidad de los receptores que se encuentran en

Valle Noble, las que además son fuentes de emisión.

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 74 de 75

El estudio también incluyó un análisis de los receptores que se encuentran en el proyecto y

cercanos a este, concluyendo bajas concentraciones y reafirmando que estas se encuentran

fuertemente influenciadas por la calefacción residencial, así también se demuestra que en

los receptores no se simula concentraciones altas, tal que se presuma una exposición aguda

crítica.

El análisis de la variación de la concentración demuestra que la ejecución del **proyecto no**

**representa una perturbación respecto a las concentraciones que actualmente se**

**registran en la estación de monitoreo analizada.** De hecho, se prevé un aumento

máximo de la condición basal de 0,01% - 0,03%en comparación a la situación basal medida

en la Kingston College la cual es propiedad del SINCA.

Finalmente, la modelación de las emisiones del proyecto de material particulado (MP10 y

MP2,5) resultaron ser de baja magnitud concluyendo que, el funcionamiento del **proyecto**

**no representa un riesgo significativo a la salud ni calidad de vida de la población,**

**según los criterios establecidos en la legislación ambiental vigente** . Considerando

que en ningún caso la concentración proyectada respecto de la concentración basal presentó

un aumento significativo que generara una posible condición de riesgo para las componentes

evaluadas.

ADENDA
INFORME MODELACIÓN ATMOSFERICA
“Modificación Proyecto Inmobiliario Valle

Noble”

Página 75 de 75

# 9 Bibliografía

CALMET/CALPUFF models simulations around a large power plant stack, p. 51. Recuperado

el 27 de junio de 2016, desde

http://revistas.ucm.es/index.php/FITE/article/view/51192/47527

Hernández-Garces, A., U. Jáuregui-Haga, J. González, J. Caseres-Long, S. Saavedra, F.

Guzmán-Martínez, A. Torres-Valle, 2016. Aplicaciones del modelo lagrangiano de dispersión

atmosférica CALPUFF, Ciencias de la Tierra y el Espacio, enero-junio, Vol. 17, No 1, p. 37.

ISSN 1729-3790. Recuperado el 29 de junio de 2016, desde

http://www.iga.cu/publicaciones/revista/assets/calpuffreview2.pdf.

Servicio de Evaluación Ambiental, 2023, Guía para el Uso de Modelos de Calidad del Aire en

el SEIA.

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1: Valores normados para MP10 y MP2,5 en Chile.****

| Nivel | MP (μg/m3N)<br>10 | MP (μg/m3)<br>2,5 |
| --- | --- | --- |
| **Concentración Anual** | 50 | 20 |
| **Concentración 24 horas** | 130 | 50 |
| **Alerta** | 180-229 | 80-109 |
| **Preemergencia** | 230-329 | 110-169 |
| **Emergencia** | 330 o superior | 170 o superior |

**Tabla 2: Fuentes de Emisión****

| Etapa del<br>proyecto | Actividades | Contami-<br>nantes<br>simulados | Tasa de<br>Emisión | Horas de<br>operación | Meses de<br>Operación | Tipo<br>de<br>Fuente | Características<br>Geométricas |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Operación | Calefacción<br>Residencial | MP10<br>MP2,5<br>SOX <br>NOX <br>NH3 | Ver<br>Anexo<br>4.3 de la<br>Adenda | 12 horas | Marzo<br>- <br>Septiembre | De área | Polígono |
| Operación | Tránsito<br>Interno | Tránsito<br>Interno | Tránsito<br>Interno | 3 <br>min/vehículo | Todos | Móvil | Polígono |
| Operación | Tránsito<br>Externo | Tránsito<br>Externo | Tránsito<br>Externo | 20<br>min/vehículo | Todos | Móvil | Polígono |

**Tabla 3: y espacialmente en la Figura 11.**

| Receptor | Descripción | Coordenada UTM (m) HUSO 18 S | Col4 | Altura (m) |
| --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Este** | **Norte** | **Norte** |
| 1 | Colegio | 677.827 | 5.923.434 | 1,6 |
| 1 | Colegio | 677.827 | 5.923.434 | 3,6 |

**Tabla 4: Receptores cercanos al proyecto****

| Receptor | Descripción | Coordenada UTM (m) HUSO 18 S | Col4 | Altura (m) |
| --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Este** | **Norte** | **Norte** |
| 1 | Casas | 679.321 | 5.923.971 | 1,6 |
| 2 | Lugar de Trabajo | 678.589 | 5.923.062 | 1,6 |
| 3 | Lugar de Trabajo | 677.893 | 5.923.243 | 1,6 |
| 4 | Edificio | 678.002 | 5.922.973 | 1,6 |
| 4 | Edificio | 678.002 | 5.922.973 | 3,6 |
| 4 | Edificio | 678.002 | 5.922.973 | 5,6 |
| 5 | Lugar de Trabajo | 677.590 | 5.923.456 | 1,6 |

**Tabla 5.: Concentraciones Modeladas en Receptores de Valle Noble.****

| Receptor | Descripción | Altura (m) | Concentración MP10 (μg/m3) | Col5 | Col6 | Col7 | Col8 | Col9 | Concentración MP2,5 (μg/m3) | Col11 | Col12 | Col13 | Col14 | Col15 | Col16 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Altura (m)** | **Modelada** | **Modelada** | **Línea de**<br>**base** | **Línea de**<br>**base** | **Proyectada** | **Proyectada** | **Modelada** | **Modelada** | **Línea de base** | **Línea de base** | **Proyectada** | **Proyectada** | **Proyectada** |
| **Receptor** | **Descripción** | **Altura (m)** | Anual | 24 h | Anual | 24 h | Anual | 24 h | Anual | 24 h | Anual | 24 h | 24 h | Anual | 24 h |
| 1 | Colegio | 1,6 | 0,24 | 1,33 | 25,0 | 52,3 | 25,24 | 53,63 | 0,22 | 1,22 | 14,1 | 37,6 | 37,6 | 14,32 | 38,82 |
| 1 | Colegio | 3,6 | 0,27 | 1,75 | 25,0 | 52,3 | 25,27 | 54,05 | 0,25 | 1,61 | 14,1 | 37,6 | 37,6 | 14,35 | 39,21 |
| 1 | Colegio | 5,6 | 0,29 | 1,98 | 25,0 | 52,3 | 25,29 | 54,28 | 0,26 | 1,82 | 14,1 | 37,6 | 37,6 | 14,36 | 39,42 |
| 2 | Supermercado | 1,6 | 0,26 | 1,42 | 25,0 | 52,3 | 25,26 | 53,72 | 0,24 | 1,31 | 14,1 | 37,6 | 37,6 | 14,34 | 38,91 |
| 3 | Casas | 1,6 | 0,24 | 1,11 | 25,0 | 52,3 | 25,24 | 53,41 | 0,22 | 1,11 | 14,1 | 37,6 | 37,6 | 14,32 | 38,71 |
| 4 | Casas | 1,6 | 0,27 | 1,29 | 25,0 | 52,3 | 25,27 | 53,59 | 0,24 | 1,18 | 14,1 | 37,6 | 37,6 | 14,34 | 38,78 |
| 5 | Casas | 1,6 | 0,21 | 1,03 | 25,0 | 52,3 | 25,21 | 53,33 | 0,19 | 0,95 | 14,1 | 37,6 | 37,6 | 14,29 | 38,55 |
| 6 | Casas | 1,6 | 0,29 | 1,44 | 25,0 | 52,3 | 25,29 | 53,74 | 0,27 | 1,32 | 14,1 | 37,6 | 37,6 | 14,37 | 38,92 |
| 7 | Casas | 1,6 | 0,19 | 1,11 | 25,0 | 52,3 | 25,19 | 53,41 | 0,18 | 1,02 | 14,1 | 37,6 | 37,6 | 14,28 | 38,62 |
| 8 | Casas | 1,6 | 0,24 | 1,34 | 25,0 | 52,3 | 25,24 | 53,64 | 0,22 | 1,23 | 14,1 | 37,6 | 37,6 | 14,32 | 38,83 |
| 9 | Edificio | 1,6 | 0,19 | 1,2 | 25,0 | 52,3 | 25,19 | 53,5 | 0,17 | 1,11 | 14,1 | 37,6 | 37,6 | 14,27 | 38,71 |
| 9 | Edificio | 7,6 | 0,24 | 1,99 | 25,0 | 52,3 | 25,24 | 54,29 | 0,22 | 1,84 | 14,1 | 37,6 | 37,6 | 14,32 | 39,44 |
| 9 | Edificio | 13,6 | 0,12 | 0,57 | 25,0 | 52,3 | 25,12 | 52,87 | 0,11 | 0,52 | 14,1 | 37,6 | 37,6 | 14,21 | 38,12 |
| 10 | Casas | 1,6 | 0,37 | 1,79 | 25,0 | 52,3 | 25,37 | 54,09 | 0,34 | 1,65 | 14,1 | 37,6 | 37,6 | 14,44 | 39,25 |
| 11 | Casas | 1,6 | 0,41 | 1,7 | 25,0 | 52,3 | 25,41 | 54 | 0,38 | 1,57 | 14,1 | 37,6 | 37,6 | 14,48 | 39,17 |
| 12 | Casas | 1,6 | 0,39 | 2,02 | 25,0 | 52,3 | 25,39 | 54,32 | 0,36 | 1,86 | 14,1 | 37,6 | 37,6 | 14,46 | 39,46 |
| 13 | Casas | 1,6 | 0,4 | 1,67 | 25,0 | 52,3 | 25,4 | 53,97 | 0,36 | 1,54 | 14,1 | 37,6 | 37,6 | 14,46 | 39,14 |
| 14 | Casas | 1,6 | 0,3 | 1,51 | 25,0 | 52,3 | 25,3 | 53,81 | 0,27 | 1,39 | 14,1 | 37,6 | 37,6 | 14,37 | 38,99 |
| 15 | Casas | 1,6 | 0,33 | 1,51 | 25,0 | 52,3 | 25,33 | 53,81 | 0,31 | 1,39 | 14,1 | 37,6 | 37,6 | 14,41 | 38,99 |
| 16 | Casas | 1,6 | 0,33 | 1,8 | 25,0 | 52,3 | 25,33 | 54,1 | 0,3 | 1,67 | 14,1 | 37,6 | 37,6 | 14,4 | 39,27 |
| 17 | Casas | 1,6 | 0,35 | 1,85 | 25,0 | 52,3 | 25,35 | 54,15 | 0,31 | 1,71 | 14,1 | 37,6 | 37,6 | 14,41 | 39,31 |
| 18 | Casas | 1,6 | 0,33 | 1,84 | 25,0 | 52,3 | 25,33 | 54,14 | 0,3 | 1,7 | 14,1 | 37,6 | 37,6 | 14,4 | 39,3 |

**Tabla 6: Concentraciones Modeladas en Receptores de cercanos a Valle Noble****

| Receptor | Descripción | Altura (m) | Concentración MP10 (μg/m3) | Col5 | Col6 | Col7 | Col8 | Col9 | Concentración MP2,5 (μg/m3) | Col11 | Col12 | Col13 | Col14 | Col15 | Col16 | Col17 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Altura (m)** | **Modelada** | **Modelada** | **Línea de**<br>**base** | **Línea de**<br>**base** | **Proyectada** | **Proyectada** | **Modelada** | **Modelada** | **Línea de base** | **Línea de base** | **Línea de base** | **Proyectada** | **Proyectada** | **Proyectada** |
| **Receptor** | **Descripción** | **Altura (m)** | Anual | 24 h | Anual | 24 h | Anual | 24 h | Anual | 24 h | 24 h | Anual | 24 h | 24 h | Anual | 24 h |
| 31 | Casas | 1,6 | 1,6 | 0,24 | 1,3 | 25 | 52,3 | 25,24 |  | 0,22 | 0,22 | 1,19 | 14,1 | 14,1 | 37,6 | 14,32 |
| 32 | Lugar de Trabajo | 1,6 | 1,6 | 0,18 | 1,21 | 25 | 52,3 | 25,18 |  | 0,16 | 0,16 | 1,12 | 14,1 | 14,1 | 37,6 | 14,26 |
| 33 | Lugar de Trabajo | 1,6 | 1,6 | 0,19 | 1,47 | 25 | 52,3 | 25,19 |  | 0,18 | 0,18 | 1,36 | 14,1 | 14,1 | 37,6 | 14,28 |

**Tabla 7.: Aumento de la concentración basal en la EMRP Kingston College, año****

| Contaminante | Col2 | Registro EMRP | Modelado | Proyectado | Porcentaje<br>de aumento |
| --- | --- | --- | --- | --- | --- |
| MP10 | Anual | 25,0 | 0,002 | 25,00 | 0,01% |
| MP10 | 24 horas | 52,3 | 0,014 | 52,31 | 0,03% |
| MP2,5 | Anual | 14,1 | 0,002 | 14,10 | 0,01% |
| MP2,5 | 24 horas | 37,6 | 0,012 | 37,61 | 0,03% |
