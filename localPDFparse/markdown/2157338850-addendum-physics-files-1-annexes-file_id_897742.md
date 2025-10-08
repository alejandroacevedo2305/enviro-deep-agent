---
title: Sin título
author: Katherine Núñez
date: D:20230627170724-04'00'
language: es
type: report
pages: 31
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - INFORME DE MODELACIÓN DE EMISIONES ATMOSFÉRICAS PROYECTO INMOBILIARIO “REGULARIZACIÓN SENDEROS DE LOS ANDES III” ANEXO 7.2: MODELACION ATMOSFERICA
-->

# INFORME DE MODELACIÓN DE EMISIONES ATMOSFÉRICAS PROYECTO INMOBILIARIO “REGULARIZACIÓN SENDEROS DE LOS ANDES III” ANEXO 7.2: MODELACION ATMOSFERICA

## Elaborado para:

**JUNIO 2023**

Declaración de Impacto Ambiental
Proyecto Inmobiliario “Regularización Senderos De Los Andes III”

Informe de Modelación Atmosférica

INDICE DE CONTENIDO

1. INTRODUCCIÓN ........................................................................................................... 5

1.1. Objetivos. ................................................................................................................. 6

2. ANTECEDENTES............................................................................................................ 7

2.1. Antecedentes de la Calidad del Aire en la comuna de Los Andes. .......................... 7

2.2. Antecedentes Meteorológicos................................................................................. 7

2.2.1. Vientos ................................................................................................................. 7

2.2.2. Temperatura y Precipitación ............................................................................... 9

2.3. Antecedentes Generales del Proyecto .................................................................. 10

3. JUSTIFICACIÓN DE LOS MODELOS UTILIZADOS EN LA MODELACIÓN ....................... 12

3.1. Uso del Modelo CALPUFF. ..................................................................................... 12

3.2. Uso del Modelo Weather Research and Forecasting Model (WRF). ..................... 13

4. METODOLOGÍA .......................................................................................................... 14

4.1. Dominio Modelación Meteorológica ..................................................................... 14

4.2. Dominio de Modelación CALPUFF ......................................................................... 16

4.3. Post procesamiento de información ..................................................................... 17

4.4. Escenario de modelación. ...................................................................................... 19

5. RESULTADOS .............................................................................................................. 23

5.1. Caracterización geofísica ....................................................................................... 23

5.1.1. Topografía .......................................................................................................... 23

5.2. Concentraciones .................................................................................................... 24

5.2.1. Dispersión y concentración de compuestos dentro del área de estudio en

relación a normativa primaria de calidad de aire. ............................................................... 24

5.2.2. Evaluación discreta de los niveles de concentración ........................................ 26

5.2.3. Evaluación de los niveles de concentración. ..................................................... 27

5.3. Área de influencia .................................................................................................. 29

5.4. Consideraciones. .................................................................................................... 30

2

Declaración de Impacto Ambiental
Proyecto Inmobiliario “Regularización Senderos De Los Andes III”

Informe de Modelación Atmosférica

6. CONCLUSIÓN ............................................................................................................. 31

**INDICE DE TABLAS**

Tabla 1. Precipitación y temperatura normal mensual, comuna de Los Andes. .................. 10

Tabla 2. Áreas de emisión, fase de operación del proyecto. ............................................... 11

Tabla 3. Coordenadas de vértices y centroide del dominio de Modelación WRF. .............. 15

Tabla 4. Coordenadas de vértices y centroide del dominio de Modelación CALPUFF. ....... 17

Tabla 5. Coordenadas de receptores discretos. ................................................................... 18

Tabla 6. Coordenadas polígono de fuente de área. ............................................................. 21

Tabla 7. Tasa de emisión. ..................................................................................................... 22

Tabla 8. Máxima concentración de dispersión de MPS, comparado con normativa de calidad

de aire secundaria. ............................................................................................................... 26

Tabla 9. Concentración de compuestos en receptores discretos. ....................................... 27

Tabla 10. Evaluación de niveles de concentración para MP 10 . ............................................ 28

3

Declaración de Impacto Ambiental
Proyecto Inmobiliario “Regularización Senderos De Los Andes III”

Informe de Modelación Atmosférica

**INDICE DE FIGURAS**

Figura 1. Rosas de dirección de viento por estación del año. ................................................ 8

Figura 2. Precipitación y temperaturas, comuna de Los Andes. ............................................ 9

Figura 3. Dominio modelación WRF. .................................................................................... 15

Figura 4. Dominio de la Modelación de CALPUFF. ............................................................... 16

Figura 5. Ubicación receptores. ............................................................................................ 19

Figura 6. Fuentes de área ..................................................................................................... 20

Figura 7. Elevación de terreno del área de estudio .............................................................. 23

Figura 8. Iso-concentración del promedio anual de MPS. ................................................... 25

Figura 9. Área de influencia del proyecto, componente aire (emisiones atmosféricas). .... 29

4

Declaración de Impacto Ambiental
Proyecto Inmobiliario “Regularización Senderos De Los Andes III”

Informe de Modelación Atmosférica

**1.** **INTRODUCCIÓN**

El proyecto “Sendero de los Andes III” consiste en la construcción de 322 viviendas, se

realizará en dos fases constructivas, la primera fase con 173 viviendas y la segunda fase

con 149 viviendas. El terreno de emplazamiento del presente Proyecto, corresponde a

una superficie bruta de 7,45 hectáreas, al respecto, según el Plan Regulador de la

comuna de los Andes vigente el proyecto se emplaza dentro de los límites urbanos de

la comuna de los Andes, identificado como zona H-3, lugar donde se permite el uso de
suelo Vivienda, Equipamientos de Salud, Educación, Culto, Cultura, Áreas Verdes, y

Servicios Profesionales en todas sus escalas; Equipamientos Deportivos, Equipamientos

de Seguridad y de Servicios públicos de escalas Comunal y Vecinal.

Para dar respuesta a las concentraciones, altura y distancia de la dispersión del

contaminante MPS se realiza la modelación meteorológica y de dispersión atmosférica,

mediante CALPUFF versión 6.42, donde se consideró un dominio de 74x74 km, con 1 km

de resolución. Las emisiones de material particulado sedimentable consideradas para

este análisis, corresponden a la mayor emisión generada por el proyecto, la cual se

presenta en la fase de operación de éste, cuya duración es indefinida debido a la

tipología del proyecto.

Adicionalmente, para la evaluación afectación de suelo y flora circundante al proyecto,

se considera un total de 25 receptores específicos correspondientes a predios agrícolas

ubicados en las cercanías y de las vías involucradas en el desplazamiento diario de los

vehículos pertenecientes al proyecto en esta etapa, en donde se generará un aumento

de la congestión vehicular, determinando así una mayor concentración del

contaminante a considerar.

5

Declaración de Impacto Ambiental
Proyecto Inmobiliario “Regularización Senderos De Los Andes III”

Informe de Modelación Atmosférica

**1.1.** **Objetivos.**

**Objetivo General**

Definir distancia de dispersión del contaminante MPS, para poder fundamentar que las

medidas a implementar para controlar dichas emisiones son suficientes para descartar

un riesgo en la flora perteneciente a predios agrícolas circundantes al proyecto, bajo

los términos establecidos en el literal c) del artículo 5 del Reglamento del Sistema de

Evaluación de Impacto Ambiental (D.S. N°40/2013 del MMA).

**Objetivos Específicos**

 - Modelar la dispersión atmosférica de la mayor emisión de material particulado

sedimentable MPS generado por el proyecto.

 - Determinar zonas de máximo y bajo impacto a través de la evaluación del alcance

de la dispersión del material particulado sedimentable (MPS) identificando máximas

y mínimas concentraciones.

 - Delimitar, con base a la modelación de la dispersión de las emisiones de los

elementos mencionados, el área de influencia para el componente aire relacionado

a emisiones atmosféricas.

 - Evaluar la concentración de material particulado (MPS), sobre receptores cercanos

al proyecto (predios con destino agrícola, humedal Rio Aconcagua).

 - Determinar la magnitud del impacto generado por el aporte de concentración

asociado las emisiones del proyecto evaluando los niveles obtenidos con respecto a

la normativa secundaria existente de calidad ambiental de material particulado

sedimentable (MPS) que se utiliza como referencia.

6

Declaración de Impacto Ambiental
Proyecto Inmobiliario “Regularización Senderos De Los Andes III”

Informe de Modelación Atmosférica

**2.** **ANTECEDENTES**

Actualmente, la presencia de material particulado sedimentable en el ambiente no se

encuentra regulada como norma primaria de calidad ambiental, sin embargo, a nivel

nacional existe una norma de calidad secundaria establecida para la cuenca del rio

Huasco en la III región. Esta norma secundaria de calidad ambiental establece los límites

de concentración, condiciones de superación y niveles para determinar situaciones de

emergencia ambiental, con el objetivo de proteger los recursos naturales tanto de flora

endémica como plantaciones agrícolas de los efectos agudos y crónicos del material

particulado sedimentable, con un nivel de riesgo aceptable.

**2.1.** **Antecedentes de la Calidad del Aire en la comuna de Los Andes.**

El Proyecto se emplaza en la comuna de Los Andes, en el área urbana de dicha comuna.

Por motivos de no existencia de datos de calidad de aire en relaciona al material

particulado sedimentable (MPS) no es posible realizar una comparación con el estado

base de la comuna y por tanto solo fue posible utilizar la norma de calidad de aire

secundaria disponible en el país a manera de referencia, para así estimar los niveles de

concentración estimados para el proyecto en comparación con esta.

**2.2.** **Antecedentes Meteorológicos**

Al momento de analizar la dispersión de contaminantes en la atmósfera, es muy

importante caracterizar la meteorología de la zona de estudio, dado que sus

parámetros, tales como vientos, temperatura y precipitación, entre otros, influyen de

muchas maneras sobre la concentración. A continuación, se presenta la caracterización

de los vientos, temperatura y precipitación de la comuna de Los Andes, cuyos datos se

obtienen de la Estación Escuela Agrícola San Felipe, la cual es la estación más cercana

que posee esta información disponible.

**2.2.1.** **Vientos**

Para la presentación de los vientos, se consideró el mismo periodo de tiempo utilizado

para la modelación atmosférica del proyecto. Los datos fueron obtenidos de la Estación

Escuela Agrícola San Felipe, la cual es la estación meteorológica más cercana que

presenta datos disponibles en esta materia para el año 2020, ya que la base de datos

utilizada para la modelación corresponde a datos corresponde al mismo año.

7

Declaración de Impacto Ambiental
Proyecto Inmobiliario “Regularización Senderos De Los Andes III”

Informe de Modelación Atmosférica

De acuerdo a lo mostrado en la

Figura **1**, los vientos predominantes de la comuna de Los Andes corresponden a vientos

provenientes desde el noreste, los cuales se hacen presente en todas las estaciones del

año. En otoño e invierno se puede observar que el porcentaje de vientos que se dirigen

hacia el sur son mayor que en las demás estaciones, además la dirección del viento es

más homogénea que en primavera y verano.

**Figura 1. Rosas de dirección de viento por estación del año.**

|Verano|Otoño|
|---|---|
||<br>|
|**Invierno**|**Primavera**|
|||

_Fuente: Elaboración propia con base en datos obtenidos de https://sinca.mma.gob.cl/_

8

Declaración de Impacto Ambiental
Proyecto Inmobiliario “Regularización Senderos De Los Andes III”

Informe de Modelación Atmosférica

**2.2.2.** **Temperatura y Precipitación**

A continuación, en la Figura 2, se presenta un climograma que incluye precipitación y

temperatura mensual normal para la comuna Los Andes. Tal como se mencionó

anteriormente, dicha información se obtuvo de la Estación Escuela Agrícola de San

Felipe, ya que es la estación meteorológica más cercana que cuenta los datos

requeridos, donde para el caso actual solo se encontraron datos de ambas variables

desde el año 2019 debido a la poca disponibilidad de información meteorológica

existente en la zona previo a esa fecha.

**Figura 2. Precipitación y temperaturas, comuna de Los Andes.**

_Fuente: Elaboración propia con base en datos obtenidos de https://sinca.mma.gob.cl/_

De acuerdo al gráfico anterior, las precipitaciones se presentan principalmente en

invierno, siendo junio el mes más lluvioso. Con respecto a las temperaturas promedio,

éstas oscilan entre los 10 y 21 °C (Tabla 1), presentando los valores más bajos en el

periodo de invierno.

9

Declaración de Impacto Ambiental
Proyecto Inmobiliario “Regularización Senderos De Los Andes III”

Informe de Modelación Atmosférica

**Tabla 1. Precipitación y temperatura normal mensual, comuna de Los Andes.**

|Mes|Precipitación (mm)|Temperatura (°C)|
|---|---|---|
|ENE|0,32|22,23|
|FEB|0,00|21,55|
|MAR|0,00|20,30|
|ABR|0,10|17,11|
|MAY|0,25|13,99|
|JUN|1,73|10,01|
|JUL|0,62|10,77|
|AGO|0,16|12,42|
|SEP|0,09|13,95|
|OCT|0,01|16,73|
|NOV|0,00|19,44|
|DIC|0,00|21,22|

_Fuente: Elaboración propia con base en datos obtenidos de https://sinca.mma.gob.cl/_

**2.3.** **Antecedentes Generales del Proyecto**

El proyecto “Sendero de los Andes” consiste en la construcción de 322 viviendas, se

realizará en dos fases constructivas, la primera fase con 173 viviendas y la segunda fase

con 149 viviendas. El terreno de emplazamiento del presente Proyecto, corresponde a

una superficie bruta de 7,45 hectáreas, al respecto, según el Plan Regulador de la

comuna de los Andes vigente el proyecto se emplaza dentro de los límites urbanos de

la comuna de los Andes, identificado como zona H-3, lugar donde se permite el uso de
suelo Vivienda, Equipamientos de Salud, Educación, Culto, Cultura, Áreas Verdes, y

Servicios Profesionales en todas sus escalas; Equipamientos Deportivos, Equipamientos

de Seguridad y de Servicios públicos de escalas Comunal y Vecinal.

Con respecto a las emisiones de material particulado sedimentable que generará el

proyecto de acuerdo a la metodología explicada en el Estudio de Emisiones

Atmosféricas, las mayores emisiones se presentan en la fase de operación del proyecto

y están relacionadas principalmente con el transito interno de vehículos pesados.

Las emisiones directas de material particulado sedimentable (MPS) generadas en cada

área del proyecto se presentan en la tabla a continuación:

10

Declaración de Impacto Ambiental
Proyecto Inmobiliario “Regularización Senderos De Los Andes III”

Informe de Modelación Atmosférica

**Tabla 2. Áreas de emisión, fase de operación del proyecto.**

|Áreas de emisión|Emisión (t/año)|
|---|---|
|**Áreas de emisión**|**MPS**|
|Polígono Proyecto|4.028|
|Tramo 1- camino pavimentado|0.111|
|Tramo 2- camino pavimentado|0.099|
|Tramo 3- camino pavimentado|0.262|
|Tramo 4- camino pavimentado|0.457|
|Tramo 5- camino pavimentado|0.202|
|Tramo 6- camino pavimentado|0.047|

_Fuente: Elaboración propia._

11

Declaración de Impacto Ambiental
Proyecto Inmobiliario “Regularización Senderos De Los Andes III”

Informe de Modelación Atmosférica

**3.** **JUSTIFICACIÓN DE LOS MODELOS UTILIZADOS EN LA MODELACIÓN**

**3.1.** **Uso del Modelo CALPUFF.**

La modelación de dispersión atmosférica de las emisiones de MPS generadas por el

proyecto, se realizó a través un modelo tipo “Puff”, específicamente el modelo

CALPUFF.

Tal como lo define la Guía, los modelos tipo “puff” son una combinación entre los

modelos Gaussianos y los modelos Lagrangeanos, en el sentido de que esencialmente

calculan la dispersión de contaminantes provenientes de una emisión instantánea,

llamada “puff”, a lo largo de una trayectoria. Su aproximación matemática consiste en

estimar la dispersión en forma Gaussiana en cada punto de una trayectoria, es decir,

los modelos tipo “puff” sólo requieren una trayectoria por “puff”, lo que hace su cálculo

mucho más rápido. En el caso de emisiones continuas, se simulan las trayectorias y la

dispersión Gaussiana de muchos “puffs”. El modelo tipo “puff” recomendado por la

Guía es el modelo CALPUFF.

El CALPUFF, es un modelo completo que incorpora herramientas para procesar datos

meteorológicos y geofísicos, modelos de dispersión y pos procesamiento. Dicho

modelo es recomendado por la Agencia de Protección Ambiental de los Estados Unidos

(EPA) para modelar transporte de contaminantes a larga distancia.

CALPUFF se compone de tres módulos:

 - CALMET: Es un modelo meteorológico que desarrolla campos horarios de viento y

temperatura en una grilla de tres dimensiones. También asocia campos en dos

dimensiones de altura y usos de suelo.

Este módulo puede ser reemplazado por el modelo matemático WRF, cuyo uso es

recomendado por la guía citada.

 - CALPUFF: Es un modelo de transporte y dispersión emitido desde fuentes modeladas,

simulando procesos de dispersión y transformación. CALPUFF utiliza los datos

generados por CALMET. Los archivos de salida de CALPUFF contienen las

concentraciones horarias o deposición por hora de flujos evaluados en receptores

seleccionados.

 - CALPOST: Es usado para procesar aquellos archivos generados por CALMET y CALPUFF,

produciendo tabulaciones que resumen los resultados de la simulación.

Ecuación del modelo CALPUFF

La ecuación básica que utiliza el modelo para realizar las modelaciones es la siguiente:

12

Declaración de Impacto Ambiental
Proyecto Inmobiliario “Regularización Senderos De Los Andes III”

Informe de Modelación Atmosférica

2

2σ
y [2][c] ~~[]]~~

2

Q
C=
2πσ x σ y

2

gexp[ [−d] 2σ x [2][a]

2 2

[−d] 2σ x [2][a] ~~[]]~~ [ exp[−d] 2σ y [2][c]

2

2
g=

(2π)

1
2 σ z

∞

∑exp

n=−∞

~~[~~ [−(H] [e] 2σ [+ 2nh)] z [2] [2] ~~]~~

Dónde:

C, es concentración a nivel del suelo (g/m3),

Q, es masa de contaminantes (g) en la nube.

σx, es desviación estándar (m) de la distribución de Gauss en el viento a lo largo de la

dirección.

σy, es desviación estándar (m) de la distribución de Gauss en el viento de costado

σz, es desviación estándar (m) de la distribución de Gauss en la dirección vertical.

da, es distancia (m) del centro de la nube al receptor en la dirección del viento a lo

largo.

dc, es distancia (m) del centro de la nube al receptor en la dirección de viento cruzado.

g, es el término vertical (m) de la ecuación Gaussiana.

H, es la altura afectiva (m) desde el nivel del suelo del hojaldre.

h, es la altura de la capa de mezcla.

De acuerdo a las características del terreno, las distintas unidades geomorfológicas del

área de influencia del proyecto y el dominio de la modelación se consideró utilizar el

modelo CALPUFF para simular la dispersión de los contaminantes.

**3.2.** **Uso del Modelo Weather Research and Forecasting Model (WRF).**

El modelo Weather Research and Forecasting (WRF), es un modelo numérico

recomendado para la generación de datos meteorológicos y uno de los modelos de

pronóstico meteorológicos más avanzados.

Debido a la falta de una red robusta de estaciones meteorológicas, la Guía para el Uso

de Modelos de Calidad del Aire en el SEIA recomienda el uso de WRF por sobre el uso

del CALMET. Además, el mismo documento, sugiere el uso del WRF para la modelación

de dispersión de contaminantes con CALPUFF.

13

Declaración de Impacto Ambiental
Proyecto Inmobiliario “Regularización Senderos De Los Andes III”

Informe de Modelación Atmosférica

**4.** **METODOLOGÍA**

La modelación de la dispersión de contaminantes se realizó de acuerdo a la siguiente

metodología.

**4.1.** **Dominio Modelación Meteorológica**

El modelo WRF es un modelo matemático que simula, a partir de variables influyentes

en la meteorología, las condiciones meteorológicas dentro de un dominio de

modelación. Para el presente caso, se consideró un dominio de 74 x 74 km, con 1 km

de resolución, y 10 celdas de altura desde 0 m hasta los 4.000 m, permitiendo

considerar un amplio rango para la variación diaria de la capa de mezcla.

El dominio de modelación WRF abarca toda el área circundante a la zona de

emplazamiento del proyecto, incluyendo la comuna de Los Andes y comunas aledañas,

tal como se muestra en la Figura 8. Las coordenadas de los vértices y el centroide del

dominio de la modelación WRF, se presentan en la Tabla 3 a continuación:

14

Declaración de Impacto Ambiental
Proyecto Inmobiliario “Regularización Senderos De Los Andes III”

Informe de Modelación Atmosférica

|Figura 3. Dominio modelación WRF.|Col2|Col3|Col4|
|---|---|---|---|
|||||
|**Consultor:**|**Carta:**|**Escala:**<br>|**Simbología**|
||DOMINIO MODELACIÓN<br>WRF|1:500.000|<br> <br>Centroide<br>Dominio|
||DOMINIO MODELACIÓN<br>WRF|**Proyección:**<br>|**Proyección:**<br>|
||DOMINIO MODELACIÓN<br>WRF|WGS 84 UTM H19S|WGS 84 UTM H19S|

**Tabla 3. Coordenadas de vértices y centroide del dominio de Modelación WRF.**

|Vértice|Proyección UTM, Huso 18 Sur; Datum WGS-84|Col3|
|---|---|---|
|**Vértice**|**Este (m)**|**Norte (m)**|
|Noroeste|312520.0|6404319.0|
|Noreste|385577.0|6404302.0|
|Suroeste|312554.0|6331239.0|
|Sureste|386057.0|6330684.0|
|Centroide|349001.7|6367848.1|

_Fuente: Elaboración propia._

15

Declaración de Impacto Ambiental
Proyecto Inmobiliario “Regularización Senderos De Los Andes III”

Informe de Modelación Atmosférica

**4.2.** **Dominio de Modelación CALPUFF**

El dominio de la modelación de CALPUFF se extiende sobre el mismo dominio de la

modelación WRF, correspondiente a un área 74 km x 74 km, tal como se presenta en la

Figura 4.

Esto para evaluar la mayor cantidad de territorio posible con las herramientas

disponibles.

|Figura 4. Dominio de la Modelación de CALPUFF.|Col2|Col3|Col4|
|---|---|---|---|
|||||
|**Consultor:**|**Carta:**|**Escala:**<br>|**Simbología**|
||DOMINIO MODELACIÓN<br>WRF|1:500.000|<br> <br>Centroide<br>Dominio|
||DOMINIO MODELACIÓN<br>WRF|**Proyección:**<br>|**Proyección:**<br>|
||DOMINIO MODELACIÓN<br>WRF|WGS 84 UTM H19S|WGS 84 UTM H19S|

_Fuente: Elaboración propia._

Las coordenadas de los vértices y el centroide del dominio de la modelación CALPUFF,

se presentan en la Tabla 4 a continuación:

16

Declaración de Impacto Ambiental
Proyecto Inmobiliario “Regularización Senderos De Los Andes III”

Informe de Modelación Atmosférica

**Tabla 4. Coordenadas de vértices y centroide del dominio de Modelación CALPUFF.**

|Vértice|Proyección UTM, Huso 198 Sur; Datum WGS-84|Col3|
|---|---|---|
|**Vértice**|**Este (m)**|**Norte (m)**|
|Noroeste|312520.0|6404319.0|
|Noreste|385577.0|6404302.0|
|Suroeste|312554.0|6331239.0|
|Sureste|386057.0|6330684.0|
|Centroide|349001.7|6367848.1|

_Fuente: Elaboración propia._

**4.3.** **Post procesamiento de información**

Para analizar los resultados de la modelación de dispersión de MPS, se realizaron mapas

de iso-concentraciones definidas según la normativa de calidad secundaria evaluada

(Decreto Exento No04/92 del MINAGRI), asociado a las emisiones generadas en la fase

de operación del proyecto. Dicho mapa permite evaluar los niveles de concentración

en toda el área de estudio con respecto a la norma secundaria de calidad ambiental.

Es importante señalar que este mapa nace de la modelación del dominio, representado

a través de una grilla de resolución 1 km, la que entrega datos de concentración de

cada vértice de la misma. Dadas las características de la grilla, los mapas son el

resultado de la interpolación entre los datos de modelación en cada vértice. Además,

los datos de concentración generados por el modelo son el resultado de la

concentración promedio de la primara capa de modelación, la que tiene lugar desde 0

m nivel del suelo hasta los 20 m.

De acuerdo a lo anterior, el mapa de dispersión e isoconcentración es considerado

como una representación espacial de la pluma y no como referencia concreta de la

concentración, pues éstas suelen estar sobre dimensionadas.

Por otro lado, la evaluación de la concentración en puntos discretos ofrece un sentido

de la magnitud más libre de distorsiones. Por esta razón y con objeto de analizar el

impacto en la calidad del aire sobre la salud de las personas, se consideró

adicionalmente una modelación discreta en 25 receptores específicos que

corresponden principalmente a viviendas cercanas al proyecto.

En la Tabla 5, se identifica cada uno de los receptores, se presentan sus coordenadas y

la distancia con respecto al proyecto (punto más cercano ya sea de cuña instalación o

camino). Así mismo, en la Figura 5, se puede observar la ubicación espacial de estos

puntos con respecto al proyecto.

17

Declaración de Impacto Ambiental
Proyecto Inmobiliario “Regularización Senderos De Los Andes III”

Informe de Modelación Atmosférica

**Tabla 5. Coordenadas de receptores discretos.**

|Receptor|Coordenadas WGS 84 UTM 19S|Col3|
|---|---|---|
|**Receptor**|**Este (m)**|**Norte (m)**|
|R1|349378|6367800|
|R2|349509|6367670|
|R3|349600|6367614|
|R4|349393|6367624|
|R5|349399|6367482|
|R6|349452|6367362|
|R7|349544|6367500|
|R8|349261|6367861|
|R9|349270|6367993|
|R10|349094|6368064|
|R11|348927|6368146|
|R12|349167|6368185|
|R13|348850|6368021|
|R14|348751|6367873|
|R15|348579|6368103|
|R16|348611|6368407|
|R17|348424|6367301|
|R18|348577|6367072|
|R19|348811|6366747|
|R20|348045|6367550|
|R21|348090|6367915|
|R22|348204|6368326|
|R23|349324|6368229|
|R24|348954|6368398|
|R25|349706|6368025|

_Fuente: Elaboración propia._

18

Declaración de Impacto Ambiental
Proyecto Inmobiliario “Regularización Senderos De Los Andes III”

Informe de Modelación Atmosférica

|Figura 5. Ubicación receptores.|Col2|Col3|Col4|
|---|---|---|---|
|||||
|**Consultor:**|**Carta:**|**Escala:**|**Simbología**|
||RECEPTORES DISCRETOS|1:15.000|<br>Receptores<br>Proyecto<br>Camino pavimentado|
||RECEPTORES DISCRETOS|**Proyección**:|**Proyección**:|
||RECEPTORES DISCRETOS|WGS 84 UTM H19S|WGS 84 UTM H19S|

_Fuente: Elaboración propia._

**4.4.** **Escenario de modelación.**

La tasa de emisión utilizada para la modelación de la dispersión del material particulado

sedimentable (MPS) corresponde a la emisión directa de material particulado generado

durante la fase de operación. Debido a que las emisiones se generarán en distintas

áreas, principalmente el área total del proyecto y de las vías de tránsito pavimentadas,

19

Declaración de Impacto Ambiental
Proyecto Inmobiliario “Regularización Senderos De Los Andes III”

Informe de Modelación Atmosférica

para la modelación se definieron 25 fuentes de área asociadas a las anteriormente

mencionadas.

Se definió un polígono de 4 vértices para el sector de emisión (cantidad de vértices

requerido por el modelo para fuentes de área).

Finalmente, en la Figura 6 y la Tabla 6 se muestran los polígonos de las fuentes y las

coordenadas de sus vértices, respectivamente.

|Figura 6. Fuentes de área|Col2|Col3|
|---|---|---|
||**Consultor:**|**Consultor:**|
||||
||**Carta:**|**Carta:**|
||FUENTES DE<br>EMISIÖN|FUENTES DE<br>EMISIÖN|
||**Escala:**|**Escala:**|
||1:12.500|1:12.500|
||**Proyección:**|**Proyección:**|
||WGS 84 UTM H19S|WGS 84 UTM H19S|
||**Simbología**|**Simbología**|
|||Área de proyecto<br>Camino<br>Pavimentado<br>Vértices<br>|

_Fuente: Elaboración propia._

20

Declaración de Impacto Ambiental
Proyecto Inmobiliario “Regularización Senderos De Los Andes III”

Informe de Modelación Atmosférica

**Tabla 6. Coordenadas polígono de fuente de área.**

|Área de emisión|Proyección UTM, Huso 19 Sur; Datum WGS-84|Col3|
|---|---|---|
|**Área de emisión**|**Este (m)**|**Norte (m)**|
|Polígono Proyecto|349237.10|6367465.34|
|Polígono Proyecto|348773.50|6367747.75|
|Polígono Proyecto|348935.20|6368034.60|
|Polígono Proyecto|349335.15|6367749.26|
|Tramo 1- camino<br>pavimentado|349321.08|6367616.60|
|Tramo 1- camino<br>pavimentado|349076.35|6367756.01|
|Tramo 1- camino<br>pavimentado|349084.07|6367768.99|
|Tramo 1- camino<br>pavimentado|349328.98|6367629.07|
|Tramo 2- camino<br>pavimentado|349348.88|6367387.61|
|Tramo 2- camino<br>pavimentado|349313.33|6367618.59|
|Tramo 2- camino<br>pavimentado|349327.91|6367618.21|
|Tramo 2- camino<br>pavimentado|349363.43|6367382.53|
|Tramo 3- camino<br>pavimentado|349508.61|6366746.36|
|Tramo 3- camino<br>pavimentado|349350.93|6367380.88|
|Tramo 3- camino<br>pavimentado|349367.82|6367377.27|
|Tramo 3- camino<br>pavimentado|349521.31|6366746.03|
|Tramo 4- camino<br>pavimentado|349509.28|6366744.14|
|Tramo 4- camino<br>pavimentado|350617.95|6366435.32|
|Tramo 4- camino<br>pavimentado|350614.50|6366422.24|
|Tramo 4- camino<br>pavimentado|349512.41|6366731.13|
|Tramo 5- camino<br>pavimentado|350449.76|6365941.07|
|Tramo 5- camino<br>pavimentado|350606.82|6366422.79|
|Tramo 5- camino<br>pavimentado|350619.70|6366416.89|
|Tramo 5- camino<br>pavimentado|350457.75|6365937.01|
|Tramo 6- camino<br>pavimentado|350339.59|6365984.25|
|Tramo 6- camino<br>pavimentado|350450.11|6365947.91|
|Tramo 6- camino<br>pavimentado|350447.51|6365938.64|
|Tramo 6- camino<br>pavimentado|350336.74|6365975.18|

_Fuente: Elaboración propia._

De esta manera, la tasa de emisión de cada área está dada por la emisión y la superficie

del polígono definido (Tabla 7). Cabe destacar que, para definir la tasa emisión de

material particulado sedimentable (MPS) asociada a cada sector, las emisiones directas

generadas por el proyecto se agruparon de acuerdo al área donde se ejecutan (Polígono

de proyecto, Tramos vía pavimentada), cuyo detalle se puede consultar en el estudio

de Emisiones Atmosféricas adjunto.

21

Declaración de Impacto Ambiental
Proyecto Inmobiliario “Regularización Senderos De Los Andes III”

Informe de Modelación Atmosférica

**Tabla 7. Tasa de emisión.**

|Áreas de emisión|Área (m2)|Emisión (t/m2 año)|
|---|---|---|
|**Áreas de emisión**|**Área (m2) **|**MPS**|
|Polígono Proyecto|160.213|2.51E-05|
|Tramo 1- camino pavimentado|4.209|2.65E-05|
|Tramo 2- camino pavimentado|3.303|3.01E-05|
|Tramo 3- camino pavimentado|9.063|2.90E-05|
|Tramo 4- camino pavimentado|14.479|3.16E-05|
|Tramo 5- camino pavimentado|5.814|3.49E-05|
|Tramo 6- camino pavimentado|1.115|4.28E-05|

_Fuente: Elaboración propia._

22

Declaración de Impacto Ambiental
Proyecto Inmobiliario “Regularización Senderos De Los Andes III”

Informe de Modelación Atmosférica

**5.** **RESULTADOS**

**5.1.** **Caracterización geofísica**

**5.1.1.** **Topografía**

En la Figura 7, se puede observar la topografía dentro del dominio de modelación

meteorológica. La elevación del terreno varía entre los 387,1 y 4314,9 m.s.n.m. El

punto rojo del centro representa la ubicación del proyecto, el cual se encuentra a

una elevación de 804,7 m.s.n.m. aproximadamente.

**Figura 7. Elevación de terreno del área de estudio**

|Col1|Consultor:|
|---|---|
|||
||**Carta:**|
||ELEVACIÓN DEL TERRENO|
||**Escala:**|
||1:3.000|
||**Proyección:**|
||LLC - NWS-84|
||**Simbología**|
|||

_Fuente: Elaboración propia._

23

Declaración de Impacto Ambiental
Proyecto Inmobiliario “Regularización Senderos De Los Andes III”

Informe de Modelación Atmosférica

**5.2.** **Concentraciones**

A continuación, se presentan los resultados de la modelación de las emisiones de MPS,

tanto para la dispersión dentro del área de estudio, como para la evaluación de los

puntos discretos cercanos al proyecto.

**5.2.1.Dispersión y concentración de compuestos dentro del área de estudio en relación a**

**normativa primaria de calidad de aire.**

Para evaluar la concentración de los compuestos evaluados, aportada por las

emisiones generadas por el proyecto se elaboró un mapa de iso-concentración de los

límites establecidos en las concentraciones expuestas en la norma de calidad de aire

secundaria utilizada como referencia, dichos mapas de iso-lineas de concentración de

MPS en el entorno del Proyecto se presentan a continuación.

24

Declaración de Impacto Ambiental
Proyecto Inmobiliario “Regularización Senderos De Los Andes III”

Informe de Modelación Atmosférica

|Figura 8. Iso-concentración del promedio anual de MPS.|Col2|Col3|Col4|
|---|---|---|---|
|<br>|<br>|<br>|<br>|
|**Consultor:**|**Carta:**|**Escala:**|**Simbología**|
||ISO-CONCENTRACIÓN DEL<br>PROMEDIO ANUAL DE MPS.|1:15.000|<br> <br> <br> <br>0,005 mg/m2 <br>0,010 mg/m2 <br>0,015 mg/m2 <br>0,020 mg/m2 <br>0,025 mg/m2 <br>Receptores<br>Proyecto<br>Rutas<br>Humedal|
||ISO-CONCENTRACIÓN DEL<br>PROMEDIO ANUAL DE MPS.|**Proyección**:|**Proyección**:|
||ISO-CONCENTRACIÓN DEL<br>PROMEDIO ANUAL DE MPS.|WGS 84 UTM H19S|WGS 84 UTM H19S|

_Fuente: Elaboración propia._

25

Declaración de Impacto Ambiental
Proyecto Inmobiliario “Regularización Senderos De Los Andes III”

Informe de Modelación Atmosférica

De las representaciones de isolineas presentadas anteriormente, se puede concluir

que, las mayores concentraciones se dan hacia el sector norte más próximo al

proyecto, es decir cercano a los receptores R8, R1 y R9, al igual que en lo que se

presenta en la evaluación de la dispersión respecto a las normas de calidad de aire

secundaria. Por otro lado, se puede observar que efectivamente existe un rango de

concentraciones medio, que tiende hacia todo el sur del proyecto, debido

principalmente a los vientos que predominan durante el año. Respecto a lo anterior,

para MPS, se puede ver en dirección al R8, se presenta una concentración máxima
de 0,0308 mg/m [2] día. Sin embargo, para los receptores seleccionados del norte

menos próximo al proyecto, es decir, cercanos o sobre el humedal Río Aconcagua,

presentan valores de concentración inferiores a 0,001 mg/m [2] día.

Finalmente, a continuación, se presenta una tabla de comparación de la máximas

concentración presentada para MPS, el cual se encuentra muy próximo al proyecto

con dirección norte, hacia R8, con la normativa de calidad de aire secundaria

utilizada como comparación.

**Tabla 8. Máxima concentración de dispersión de MPS, comparado con normativa de**

**calidad de aire secundaria.**

|Compuesto|Prom anual MPS<br>0|
|---|---|
|**Máximo (mg/m2dia)**|3,08E-2|
|**Norma (mg/m2dia)**|100|
|**% de la norma**|0.03|

_Fuente: Elaboración propia._

De la Tabla 8, se puede concluir que las concentraciones generadas por el proyecto,

se encuentran muy por debajo de la concentración límite establecida en la

normativa de calidad de aire secundaria como promedio anual, donde al hacer la

comparación con esta, se da cuenta de que el porcentaje de emisión

correspondiente a un 0,03%, lo cual se considera poco significativo.

**5.2.2.** **Evaluación discreta de los niveles de concentración**

Con respecto a los resultados obtenidos en los puntos discretos, a continuación, en

la Tabla 9 se indican los valores de concentración de material particulado

sedimentable (MPS) generados por las fuentes, para la etapa de operación del

Proyecto.

26

Declaración de Impacto Ambiental
Proyecto Inmobiliario “Regularización Senderos De Los Andes III”

Informe de Modelación Atmosférica

**Tabla 9. Concentración de compuestos en receptores discretos.**

|Punto|Coordenadas WGS 84 UTM 19S|Col3|Concentración (mg/m2dia)|
|---|---|---|---|
|**Punto**|**Este (m)**|**Norte (m)**|**Prom anual MPS**|
|R1|349378|6367800|1,51E-02|
|R2|349509|6367670|8,61E-03|
|R3|349600|6367614|7,07E-03|
|R4|349393|6367624|1,09E-02|
|R5|349399|6367482|1,14E-02|
|R6|349452|6367362|7,53E-03|
|R7|349544|6367500|7,49E-03|
|R8|349261|6367861|3,08E-02|
|R9|349270|6367993|1,25E-02|
|R10|349094|6368064|1,32E-02|
|R11|348927|6368146|6,71E-03|
|R12|349167|6368185|5,99E-03|
|R13|348850|6368021|9,14E-03|
|R14|348751|6367873|1,18E-02|
|R15|348579|6368103|5,37E-03|
|R16|348611|6368407|2,29E-03|
|R17|348424|6367301|6,51E-03|
|R18|348577|6367072|5,20E-03|
|R19|348811|6366747|2,09E-03|
|R20|348045|6367550|2,74E-03|
|R21|348090|6367915|2,46E-03|
|R22|348204|6368326|1,38E-03|
|R23|349324|6368229|4,63E-03|
|R24|348954|6368398|3,10E-03|
|R25|349706|6368025|3,80E-03|

_Fuente: Elaboración propia._

De acuerdo a los valores de concentración del compuesto evaluado en cada uno de

los receptores considerados para la evaluación discreta de concentraciones, las

mayores concentraciones se dan en el receptor R8 en concentración promedio

anual.

**5.2.3.** **Evaluación de los niveles de concentración.**

Con el objetivo de evaluar los niveles de concentración de MPS generados por la

operación del proyecto, se comparará la magnitud de este valor con la normativa

secundaria de calidad ambiental existente en el país y utilizada como referencia.

A continuación, se presenta el porcentaje del mayor valor de promedio anual para

MPS en la modelación con respecto a los valores límite anual establecidos por la

norma secundaria de calidad ambiental señalada anteriormente.

27

Declaración de Impacto Ambiental
Proyecto Inmobiliario “Regularización Senderos De Los Andes III”

Informe de Modelación Atmosférica

**Tabla 10. Evaluación de niveles de concentración para MP** **10** **.**

|Compuesto|Promedio del periodo anual<br>(mg/m2 dia)|Límite D. Exento N° 4/1992 del<br>MINAGRI(mg/m2 dia)|
|---|---|---|
|MPS|0,0308|100|
|**Porcentaje respecto a modelación (%)**|**Porcentaje respecto a modelación (%)**|**0,0308**|

_Fuente: Elaboración propia_ 8

De acuerdo a la Tabla 10, respecto de la norma de calidad secundaria comparable al

proyecto, se puede indicar que el punto de máximo impacto corresponde a las áreas

cercanas a R8, no presentando aportes significativos de concentraciones de material

particulado sedimentable generados por el proyecto, en el área de estudio. Lo

anterior debido a que el porcentaje de cumplimiento respecto a la normativa de

calidad de aire secundaria utilizada como referencia no supera el 0,031%.

Dado que la concentración obtenida con la modelación de la emisión generada por

la operación del proyecto representa un bajo porcentaje en comparación con la

normativa secundaria de calidad ambiental, se puede concluir que no se generará

un impacto sobre flora o vegetación agrícola circundante al proyecto.

28

Declaración de Impacto Ambiental
Proyecto Inmobiliario “Regularización Senderos De Los Andes III”

Informe de Modelación Atmosférica

**5.3.** **Área de influencia**

De acuerdo a los resultados obtenidos de la modelación de la dispersión de las

emisiones, se definió el área de influencia del proyecto como el alcance del Promedio

anual de MPS, donde se consideró como límite del área de influencia la isolinea de valor

0,005 mg/m [2] día, el cual representa el 0,005 % de la normativa de calidad de aire

secundaria de MPS .

Finalmente, en la figura a continuación se presenta el área de influencia del proyecto

para el componente aire respecto a las emisiones atmosféricas generadas por él.

**Figura 9. Área de influencia del proyecto, componente aire (emisiones atmosféricas).**

|Col1|Consultor:|Col3|
|---|---|---|
||||
||**Carta:**|**Carta:**|
||AREA DE<br>INFLUENCIA|AREA DE<br>INFLUENCIA|
||**Escala:**|**Escala:**|
||1:15.000|1:15.000|
||**Proyección:**|**Proyección:**|
||WGS 84 UTM H19S|WGS 84 UTM H19S|
||**Simbología**<br>|**Simbología**<br>|
||<br>|Proyecto<br>Camino<br>Pavimentado<br>Área de<br>Influencia<br>Receptores|

_Fuente: Elaboración propia._

29

Declaración de Impacto Ambiental
Proyecto Inmobiliario “Regularización Senderos De Los Andes III”

Informe de Modelación Atmosférica

**5.4.** **Consideraciones.**

La base de datos meteorológica y geográfica fue adquirida a una empresa especializada

en modelación para servicios de evaluación ambiental, la cual fue generada por medio

del software WRF, cumpliendo con las condiciones establecidas por el Servicio de

Evaluación Ambiental.

30

Declaración de Impacto Ambiental
Proyecto Inmobiliario “Regularización Senderos De Los Andes III”

Informe de Modelación Atmosférica

**6.** **CONCLUSIÓN**

La ejecución del proyecto “Sendero de los Andes III” provoca una cantidad poco

significativa de material particulado sedimentable, principalmente debido a las

actividades de tránsito en vías pavimentadas y no pavimentadas en la etapa de

operación de este.

Para evaluar el impacto generado por la emisión de material particulado MPS sobre la

flora y vegetación próxima al proyecto, se realizó una modelación de dispersión

atmosférica a través del software CALPUFF. La modelación contempló un dominio de

74x74 km, que incluyó toda la información meteorológica proporcionada por la base de

datos construida a partir de modelación WRF.

A partir de la modelación de dispersión atmosférica del material particulado

sedimentable MPS generado por la operación del proyecto, se concluye que las

concentraciones generadas por éste son de baja magnitud y de bajo alcance.

El promedio anual para MPS es de baja magnitud y de bajo alcance, con valores de 0,005
mg/m [2] dia hasta un radio de aproximadamente 1 km con respecto al área del proyecto.

Los mayores valores de concentración se presentan en los sectores aledaños a esta área,
alcanzando 0,025 mg/m [2] dia. En el caso de los receptores ubicados sobre el humedal Río
Aconcagua, estos presentan valores menores a los 0,01 mg/m [2] dia, lo que se traduce en

una nula significancia de impacto sobre el mismo.

Adicionalmente, se realizó una evaluación de concentración en 25 puntos discretos, que

corresponden a predios con vegetación, principalmente con destino agrícola o con

carácter de protección ambiental (humedal Río Aconcagua), cercanas al área del

proyecto y las vías no pavimentadas de las cuales se hará uso. De acuerdo a los valores

del promedio anual asociados a cada uno de los receptores considerados para la

evaluación discreta, ninguno presentó valores sobre una unidad para MPS. Para las

concentraciones de MPS, todos los receptores se encuentran bajo los 0,0308 mg/m [2] día,

(mayor valor se presenta en R8).

Dado que los valores sobre los receptores son de baja magnitud, se puede inferir que

las concentraciones de material particulado sedimentable (MPS) no generarán un

impacto negativo sobre los recursos naturales de la comuna de Los Andes, tanto de las

áreas agrícolas circundantes al proyecto como de las áreas de protección como es el

caso del recientemente declarado humedal Río Aconcagua..

31

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Precipitación y temperatura normal mensual, comuna de Los Andes.****

| Mes | Precipitación (mm) | Temperatura (°C) |
| --- | --- | --- |
| ENE | 0,32 | 22,23 |
| FEB | 0,00 | 21,55 |
| MAR | 0,00 | 20,30 |
| ABR | 0,10 | 17,11 |
| MAY | 0,25 | 13,99 |
| JUN | 1,73 | 10,01 |
| JUL | 0,62 | 10,77 |
| AGO | 0,16 | 12,42 |
| SEP | 0,09 | 13,95 |
| OCT | 0,01 | 16,73 |
| NOV | 0,00 | 19,44 |
| DIC | 0,00 | 21,22 |

**Tabla 2.: Áreas de emisión, fase de operación del proyecto.****

| Áreas de emisión | Emisión (t/año) |
| --- | --- |
| **Áreas de emisión** | **MPS** |
| Polígono Proyecto | 4.028 |
| Tramo 1- camino pavimentado | 0.111 |
| Tramo 2- camino pavimentado | 0.099 |
| Tramo 3- camino pavimentado | 0.262 |
| Tramo 4- camino pavimentado | 0.457 |
| Tramo 5- camino pavimentado | 0.202 |
| Tramo 6- camino pavimentado | 0.047 |

**Tabla 3.: Coordenadas de vértices y centroide del dominio de Modelación WRF.****

| Vértice | Proyección UTM, Huso 18 Sur; Datum WGS-84 | Col3 |
| --- | --- | --- |
| **Vértice** | **Este (m)** | **Norte (m)** |
| Noroeste | 312520.0 | 6404319.0 |
| Noreste | 385577.0 | 6404302.0 |
| Suroeste | 312554.0 | 6331239.0 |
| Sureste | 386057.0 | 6330684.0 |
| Centroide | 349001.7 | 6367848.1 |

**Tabla 4.: Coordenadas de vértices y centroide del dominio de Modelación CALPUFF.****

| Vértice | Proyección UTM, Huso 198 Sur; Datum WGS-84 | Col3 |
| --- | --- | --- |
| **Vértice** | **Este (m)** | **Norte (m)** |
| Noroeste | 312520.0 | 6404319.0 |
| Noreste | 385577.0 | 6404302.0 |
| Suroeste | 312554.0 | 6331239.0 |
| Sureste | 386057.0 | 6330684.0 |
| Centroide | 349001.7 | 6367848.1 |

**Tabla 5.: Coordenadas de receptores discretos.****

| Receptor | Coordenadas WGS 84 UTM 19S | Col3 |
| --- | --- | --- |
| **Receptor** | **Este (m)** | **Norte (m)** |
| R1 | 349378 | 6367800 |
| R2 | 349509 | 6367670 |
| R3 | 349600 | 6367614 |
| R4 | 349393 | 6367624 |
| R5 | 349399 | 6367482 |
| R6 | 349452 | 6367362 |
| R7 | 349544 | 6367500 |
| R8 | 349261 | 6367861 |
| R9 | 349270 | 6367993 |
| R10 | 349094 | 6368064 |
| R11 | 348927 | 6368146 |
| R12 | 349167 | 6368185 |
| R13 | 348850 | 6368021 |
| R14 | 348751 | 6367873 |
| R15 | 348579 | 6368103 |
| R16 | 348611 | 6368407 |
| R17 | 348424 | 6367301 |
| R18 | 348577 | 6367072 |
| R19 | 348811 | 6366747 |
| R20 | 348045 | 6367550 |
| R21 | 348090 | 6367915 |
| R22 | 348204 | 6368326 |
| R23 | 349324 | 6368229 |
| R24 | 348954 | 6368398 |
| R25 | 349706 | 6368025 |

**Tabla 6.: Coordenadas polígono de fuente de área.****

| Área de emisión | Proyección UTM, Huso 19 Sur; Datum WGS-84 | Col3 |
| --- | --- | --- |
| **Área de emisión** | **Este (m)** | **Norte (m)** |
| Polígono Proyecto | 349237.10 | 6367465.34 |
| Polígono Proyecto | 348773.50 | 6367747.75 |
| Polígono Proyecto | 348935.20 | 6368034.60 |
| Polígono Proyecto | 349335.15 | 6367749.26 |
| Tramo 1- camino<br>pavimentado | 349321.08 | 6367616.60 |
| Tramo 1- camino<br>pavimentado | 349076.35 | 6367756.01 |
| Tramo 1- camino<br>pavimentado | 349084.07 | 6367768.99 |
| Tramo 1- camino<br>pavimentado | 349328.98 | 6367629.07 |
| Tramo 2- camino<br>pavimentado | 349348.88 | 6367387.61 |
| Tramo 2- camino<br>pavimentado | 349313.33 | 6367618.59 |
| Tramo 2- camino<br>pavimentado | 349327.91 | 6367618.21 |
| Tramo 2- camino<br>pavimentado | 349363.43 | 6367382.53 |
| Tramo 3- camino<br>pavimentado | 349508.61 | 6366746.36 |
| Tramo 3- camino<br>pavimentado | 349350.93 | 6367380.88 |
| Tramo 3- camino<br>pavimentado | 349367.82 | 6367377.27 |
| Tramo 3- camino<br>pavimentado | 349521.31 | 6366746.03 |
| Tramo 4- camino<br>pavimentado | 349509.28 | 6366744.14 |
| Tramo 4- camino<br>pavimentado | 350617.95 | 6366435.32 |
| Tramo 4- camino<br>pavimentado | 350614.50 | 6366422.24 |
| Tramo 4- camino<br>pavimentado | 349512.41 | 6366731.13 |
| Tramo 5- camino<br>pavimentado | 350449.76 | 6365941.07 |
| Tramo 5- camino<br>pavimentado | 350606.82 | 6366422.79 |
| Tramo 5- camino<br>pavimentado | 350619.70 | 6366416.89 |
| Tramo 5- camino<br>pavimentado | 350457.75 | 6365937.01 |
| Tramo 6- camino<br>pavimentado | 350339.59 | 6365984.25 |
| Tramo 6- camino<br>pavimentado | 350450.11 | 6365947.91 |
| Tramo 6- camino<br>pavimentado | 350447.51 | 6365938.64 |
| Tramo 6- camino<br>pavimentado | 350336.74 | 6365975.18 |

**Tabla 7.: Tasa de emisión.****

| Áreas de emisión | Área (m2) | Emisión (t/m2 año) |
| --- | --- | --- |
| **Áreas de emisión** | **Área (m2) ** | **MPS** |
| Polígono Proyecto | 160.213 | 2.51E-05 |
| Tramo 1- camino pavimentado | 4.209 | 2.65E-05 |
| Tramo 2- camino pavimentado | 3.303 | 3.01E-05 |
| Tramo 3- camino pavimentado | 9.063 | 2.90E-05 |
| Tramo 4- camino pavimentado | 14.479 | 3.16E-05 |
| Tramo 5- camino pavimentado | 5.814 | 3.49E-05 |
| Tramo 6- camino pavimentado | 1.115 | 4.28E-05 |

**Tabla 8.: Máxima concentración de dispersión de MPS, comparado con normativa de****

| Compuesto | Prom anual MPS<br>0 |
| --- | --- |
| **Máximo (mg/m2dia)** | 3,08E-2 |
| **Norma (mg/m2dia)** | 100 |
| **% de la norma** | 0.03 |

**Tabla 9.: Concentración de compuestos en receptores discretos.****

| Punto | Coordenadas WGS 84 UTM 19S | Col3 | Concentración (mg/m2dia) |
| --- | --- | --- | --- |
| **Punto** | **Este (m)** | **Norte (m)** | **Prom anual MPS** |
| R1 | 349378 | 6367800 | 1,51E-02 |
| R2 | 349509 | 6367670 | 8,61E-03 |
| R3 | 349600 | 6367614 | 7,07E-03 |
| R4 | 349393 | 6367624 | 1,09E-02 |
| R5 | 349399 | 6367482 | 1,14E-02 |
| R6 | 349452 | 6367362 | 7,53E-03 |
| R7 | 349544 | 6367500 | 7,49E-03 |
| R8 | 349261 | 6367861 | 3,08E-02 |
| R9 | 349270 | 6367993 | 1,25E-02 |
| R10 | 349094 | 6368064 | 1,32E-02 |
| R11 | 348927 | 6368146 | 6,71E-03 |
| R12 | 349167 | 6368185 | 5,99E-03 |
| R13 | 348850 | 6368021 | 9,14E-03 |
| R14 | 348751 | 6367873 | 1,18E-02 |
| R15 | 348579 | 6368103 | 5,37E-03 |
| R16 | 348611 | 6368407 | 2,29E-03 |
| R17 | 348424 | 6367301 | 6,51E-03 |
| R18 | 348577 | 6367072 | 5,20E-03 |
| R19 | 348811 | 6366747 | 2,09E-03 |
| R20 | 348045 | 6367550 | 2,74E-03 |
| R21 | 348090 | 6367915 | 2,46E-03 |
| R22 | 348204 | 6368326 | 1,38E-03 |
| R23 | 349324 | 6368229 | 4,63E-03 |
| R24 | 348954 | 6368398 | 3,10E-03 |
| R25 | 349706 | 6368025 | 3,80E-03 |

**Tabla 10.: Evaluación de niveles de concentración para MP** **10** **.****

| Compuesto | Promedio del periodo anual<br>(mg/m2 dia) | Límite D. Exento N° 4/1992 del<br>MINAGRI(mg/m2 dia) |
| --- | --- | --- |
| MPS | 0,0308 | 100 |
| **Porcentaje respecto a modelación (%)** | **Porcentaje respecto a modelación (%)** | **0,0308** |
