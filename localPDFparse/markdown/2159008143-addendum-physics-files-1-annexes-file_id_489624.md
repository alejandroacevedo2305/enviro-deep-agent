---
title: Sin título
author: Katherine Núñez
date: D:20230703083835-04'00'
language: es
type: report
pages: 53
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - PROYECTO INMOBILIARIO “SENDEROS DE TENGLO”
-->

## INFORME DE MODELACIÓN DE EMISIONES ATMOSFÉRICAS

# PROYECTO INMOBILIARIO “SENDEROS DE TENGLO”

## Ulmo Consultores S.A

**JUNIO 2023**

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

INDICE DE CONTENIDO

1. INTRODUCCIÓN ............................................................................................................ 7

1.1. Objetivos. ................................................................................................................... 8

2. ANTECEDENTES ........................................................................................................... 9

2.1. Antecedentes de la Calidad del Aire en la comuna de Puerto Montt............................... 10

2.1.1. Calidad del Aire y antecedentes que fundamentan la condición de Zona Saturada por
MP 2,5 . 10

2.1.2. Concentración promedio anual ............................................................................... 11

2.1.3. Concentración promedio mensual MP 2,5 ................................................................. 12

2.1.4. Concentración promedio diaria, percentil 98 y variación horaria de MP 2,5 . .................. 13

2.2. Antecedentes Meteorológicos .................................................................................... 16

2.2.1. Vientos ................................................................................................................ 16

2.2.2. Temperatura y Precipitación .................................................................................. 18

2.3. Antecedentes Generales del Proyecto ........................................................................ 19

3. JUSTIFICACIÓN DE LOS MODELOS UTILIZADOS EN LA MODELACIÓN ....................... 21

3.1. Uso del Modelo CALPUFF. ........................................................................................ 21

3.2. Uso del Modelo Weather Research and Forecasting Model (WRF). ............................... 22

4. METODOLOGÍA ........................................................................................................... 23

4.1. Dominio Modelación Meteorológica ............................................................................ 23

4.2. Dominio de Modelación CALPUFF ............................................................................. 25

4.3. Post procesamiento de información ............................................................................ 26

4.4. Escenario de modelación. .......................................................................................... 28

5. RESULTADOS ............................................................................................................. 32

5.1. Caracterización Geofísica .......................................................................................... 32

5.1.1. Topografía ........................................................................................................... 32

5.2. Concentraciones ....................................................................................................... 33

2

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

5.2.1. Dispersión y concentración de compuestos dentro del área de estudio en relación a
normativa primaria de calidad de aire. ....................................................................................... 33

5.2.2. Evaluación discreta de los niveles de concentración ................................................ 46

5.2.3. Evaluación de los niveles de concentración. ............................................................ 46

5.3. Área de influencia ..................................................................................................... 50

5.4. Consideraciones. ...................................................................................................... 51

6. CONCLUSIÓN ............................................................................................................. 52

3

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

INDICE DE TABLAS

Tabla 1. Normas de Calidad del Aire Consideradas en el Estudio. ................................................. 9

Tabla 2. Información general de la EMRP “Mirasol”. ................................................................... 11

Tabla 3. Precipitación y temperatura normal mensual, Puerto Montt, estación “Puerto Montt- DGA”.

.............................................................................................................................................. 19

Tabla 4. Áreas de emisión, fase de operación del proyecto. ........................................................ 20

Tabla 5. Coordenadas de vértices y centroide del dominio de Modelación WRF. ........................... 23

Tabla 6. Coordenadas de vértices y centroide del dominio de Modelación CALPUFF. ................... 26

Tabla 7. Coordenadas de receptores discretos. .......................................................................... 27

Tabla 8. Coordenadas fuente puntual y polígonos de fuente de área. ........................................... 30

Tabla 9. Tasa de emisión. ........................................................................................................ 31

Tabla 10. Máxima concentración de dispersión de compuestos, comparados con normativa de calidad
de aire primaria. ...................................................................................................................... 45

Tabla 11. Concentración de compuestos en receptores discretos. ............................................... 46

Tabla 12. Evaluación de niveles de concentración para MP 10 . ..................................................... 47

Tabla 13. Evaluación de niveles de concentración para MP 2,5 . ..................................................... 47

Tabla 14. Evaluación de niveles de concentración para NO x . ....................................................... 47

Tabla 15. Evaluación de niveles de concentración para SO 2 . ....................................................... 48

Tabla 16. Evaluación de niveles de concentración para CO. ........................................................ 48

4

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

INDICE DE FIGURAS

Figura 1. Concentración promedio anual de MP 2,5 . ..................................................................... 11

Figura 2. Concentración promedio mensual de MP 2,5 . ................................................................. 12

Figura 3. Concentración promedio diaria de MP 2,5 . ..................................................................... 13

Figura 4. Percentil 98 de promedios diarios de MP 2,5 . ................................................................. 14

Figura 5. Concentración promedio horaria para meses otoño - invierno MP 2,5 . ............................. 15

Figura 6. Rosas de dirección de viento por estación del año. ....................................................... 17

Figura 7. Precipitación y temperaturas, Puerto Montt. ................................................................. 18

Figura 8. Dominio modelación WRF. ......................................................................................... 24

Figura 9. Dominio de la Modelación de CALPUFF. ..................................................................... 25

Figura 10. Ubicación receptores. ............................................................................................... 28

Figura 11. Fuentes de emisión de área. ..................................................................................... 29

Figura 12. Elevación de terreno del área de estudio .................................................................... 32

Figura 13. Iso-concentración del promedio anual de MP 10 . .......................................................... 34

Figura 14. Iso-concentración del percentil 98 de promedios diarios de MP 10 . ................................ 35

Figura 15. Iso-concentración del promedio anual de MP 2,5 . ......................................................... 36

Figura 16. Iso-concentración del percentil 98 de promedios diarios de MP 2,5 . ................................ 37

Figura 17. Iso-concentración del promedio anual de SO 2 . ........................................................... 38

Figura 18. Iso-concentración del percentil 99 de promedios diarios de SO 2 . .................................. 39

Figura 19. Iso-concentración del percentil 99 de promedios horarios de SO 2 ................................. 40

Figura 20. Iso-concentración del promedio anual de NO 2 . ........................................................... 41

Figura 21. Iso-concentración del percentil 99 de promedios horarios de NO 2 . ............................... 42

5

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

Figura 22. Iso-concentración del percentil 99 de promedios 8 horas de CO. ................................. 43

Figura 23. Iso-concentración del percentil 99 de promedios horarios de CO. ................................. 44

Figura 24. Área de influencia del proyecto, componente aire (emisiones atmosféricas). ................. 50

6

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

**1.** **INTRODUCCIÓN**

El Proyecto Senderos de Tenglo consiste la construcción de un conjunto de 462 viviendas. cuya
titularidad es de Ulmo Consultores S.A.,y se encuentra emplazado en Avenida Los Notros con
Avenida Río Taylor, comuna de Puerto Montt.

Para dar respuesta a las concentraciones, altura y distancia de la dispersión de los contaminantes
de MP 10 y MP 2,5, CO, NO 2 y SO 2 se realiza la modelación meteorológica y de dispersión
atmosférica, mediante CALPUFF versión 6.42, donde se consideró un dominio de 74x74 km, con
1 km de resolución. Las emisiones de material particulado y gases de combustión, consideradas
para este análisis, corresponden a la mayor emisión generada por el proyecto, la cual se presenta
en la fase de operación de éste.

Adicionalmente, para la evaluación del riesgo sobre la salud de las personas, se considera un total
de 11 receptores específicos correspondientes a edificaciones y viviendas ubicadas en las
cercanías del área de emplazamiento del proyecto.

7

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

**1.1.** **Objetivos.**

**Objetivo General**

Definir distancia de dispersión de contaminantes MP 10 y MP 2,5, CO, NO 2 y SO 2, para poder
fundamentar que las medidas a implementar para controlar dichas emisiones son suficientes para
descartar un riesgo para la salud de las personas, bajo los términos establecidos en el literal a)
del artículo 5 del Reglamento del Sistema de Evaluación de Impacto Ambiental (D.S. N°40/2013
del MMA).

**Objetivos Específicos**

 - Modelar la dispersión atmosférica de la mayor emisión de material particulado respirable MP 10

y material particulado fino respirable MP 2,5 generado por el proyecto.

 - Modelar la dispersión atmosférica de la mayor emisión de dióxido de azufre (SO 2 ), dióxido de

nitrógeno (NO 2 ) y monóxido de carbono (CO), generado por el proyecto.

 Determinar zonas de máximo y bajo impacto a través de la evaluación del alcance de la

dispersión del material particulado (MP 10 y MP 2,5 ) identificando máximas y mínimas

concentraciones.

 Determinar zonas de máximo y bajo impacto a través de la evaluación del alcance de la

dispersión del dióxido de azufre (SO 2 ), dióxido de nitrógeno (NO 2 ) y monóxido de carbono
(CO) identificando máximas y mínimas concentraciones.

 Delimitar, con base a la modelación de la dispersión de las emisiones de los elementos

mencionados, el área de influencia para el componente aire relacionado a emisiones

atmosféricas.

 - Evaluar la concentración de material particulado (MP 10 y MP 2,5 ), dióxido de azufre (SO 2 ),

dióxido de nitrógeno (NO 2 ) y monóxido de carbono (CO), sobre receptores cercanos al
proyecto (edificaciones con destino habitacional, principalmente).

 Determinar la magnitud del impacto generado por el aporte de concentración asociado las

emisiones del proyecto evaluando los niveles obtenidos con respecto a la normativa primaria
de calidad ambiental de material particulado respirable (MP 10 ) y material particulado fino
respirable (MP 2,5 ), dióxido de azufre (SO 2 ), dióxido de nitrógeno (NO 2 ) y monóxido de carbono
(CO).

8

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

**2.** **ANTECEDENTES**

Actualmente, la presencia de material particulado y gases de combustión, en el ambiente está
regulada por normas primarias de calidad ambiental definidas para cada clasificación. Estas
normas primarias de calidad ambiental establecen límites de concentración, condiciones de
superación y niveles para determinar situaciones de emergencia ambiental, con el objetivo de
proteger la salud de las personas de los efectos agudos y crónicos del material particulado y gases,
con un nivel de riesgo aceptable.

Adicionalmente, se realiza el análisis de la Norma Secundaria de Calidad de Aire para Anhídrido
Sulfuroso Decreto 22/2010, cuyo objetivo es la protección y conservación de los recursos naturales
renovables del ámbito silvoagropecuario y de vida silvestre, de los efectos agudos y crónicos
generados por la exposición a dióxido de azufre en el aire.

A continuación, en la Tabla 1, se presentan los valores límites de referencia para el análisis del
presente documento.

**Tabla 1. Normas de Calidad del Aire Consideradas en el Estudio.**

|Parámetro|Tipo de Norma|Estadístico|Valor de referencia|Fuente|
|---|---|---|---|---|
|MP10|Primaria|Promedio<br>del<br>periodo|50 μg/m3N|D.S. N°12/22 MMA|
|MP10|Primaria|Percentil 98 Diario|130 μg/m3N|D.S. N°12/22 MMA|
|MP2,5|Primaria|Promedio<br>del<br>periodo|20 μg/m3N|D.S. N°12/11 MMA|
|MP2,5|Primaria|Percentil 98 Diario|50 μg/m3N|D.S. N°12/11 MMA|
|SO2|Primaria|Promedio<br>del<br>periodo|60 μg/m3N|D.S. N°104/18 MMA|
|SO2|Primaria|Percentil 99 Diario|150 μg/m3N|D.S. N°104/18 MMA|
|SO2|Primaria|Percentil 99 Horario|350 μg/m3N|D.S. N°104/18 MMA|
|NO2|Primaria|Promedio<br>del<br>periodo|100 μg/m3N|D.S. N°114/02 MINSEGPRES|
|NO2|Primaria|Percentil 99 Horario|400 μg/m3N|D.S. N°114/02 MINSEGPRES|
|CO|Primaria|Percentil 99 8 horas|1.000 μg/m3N|D.S. N°115/02 MINSEGPRES|
|CO|Primaria|Percentil 99 Horario|3.000 μg/m3N|D.S. N°115/02 MINSEGPRES|
|SO2|Secundaria|Promedio<br>del<br>periodo|60 μg/m3N|D.S. N°22/10 MMA|
|SO2|Secundaria|Percentil 99,7 Diario|260 μg/m3N|D.S. N°22/10 MMA|
|SO2|Secundaria|Percentil<br>99,73<br>Horario|700 μg/m3N|D.S. N°22/10 MMA|

_Fuente: Elaboración propia en base a normativa ambiental de calidad de aire._

9

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

**2.1.** **Antecedentes de la Calidad del Aire en la comuna de Puerto Montt.**

Se estima que la potencial área de influencia del proyecto considera la comuna de Puerto Montt
en la Macrozona Centro-Norte de la Región de Los Lagos, específicamente sectores aledaños al
área de emplazamiento de las viviendas.

La Comuna de Puerto Montt es declarada zona saturada por material particulado fino respirable
MP 2,5, como concentración diaria, por el DS. N°24/2021 del Ministerio del Medio Ambiente, de
acuerdo a lo registrado en las estaciones de monitoreo con representatividad poblacional
(EMRP).

Posteriormente, por resolución exenta No 148, de 3 de marzo 2021, del Ministerio del Medio
Ambiente, publicada en el Diario Oficial el 10 de marzo 2021, se dio inicio al proceso de
elaboración del Plan de Descontaminación Atmosférica para la comuna de San Pablo, de la
Región de Los Lagos y para la Macrozona Centro-Norte de la Región de Los Lagos.

Actualmente dicho proceso de elaboración aún se encuentra en desarrollo, y por tanto, no existe
PDA aprobado para la zona de ubicación del proyecto en evaluación.

**2.1.1.** **Calidad del Aire y antecedentes que fundamentan la condición de Zona Saturada por MP** **2,5** **.**

La red de vigilancia de calidad del aire del Ministerio del Medio Ambiente, cuenta con 3 estaciones
de monitoreo pública ubicadas en la Comuna de San Pablo y la Macrozona Centro-Norte de la
Región de Los Lagos, específicamente en las comunas de Puerto Montt y Puerto Varas. La
estación MirasoI, tiene representatividad poblacional (EMRP) para material particulado (MP) y las
estaciones Puerto Montt y Puerto Varas, cuentan con representatividad poblacional para material
particulado respirable fino (MP 2,5 )

En los puntos a continuación, se presentan los antecedentes de calidad del aire de la comuna de
Puerto Montt, perteneciente a la Macrozona Centro-Norte de la Región de Los Lagos, con base
en los registros de la estación de monitoreo calificada con representatividad poblacional “Mirasol”,
los cuales serán utilizados para comparar la situación basal de la comuna con el aporte adicional
de material particulado del proyecto. Adicionalmente, para datos anuales y diarios, se evalúa la
condición de superación de la norma primaria de calidad ambiental, de acuerdo a lo establecido

en el artículo 4° del D.S N°12/2011 del MMA.

10

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

**Tabla 2. Información general de la EMRP “Mirasol”.**

|Estación|Mirasol|
|---|---|
|Propietario|Ministerio del Medio Ambiente|
|Operador|Algoritmos y Mediciones Ambientales SpA|
|Región|del Los Lagos|
|Provincia|Llanquihue|
|Comuna|Puerto Montt|
|Coordenadas UTM 19S|669585 E|
|Coordenadas UTM 19S|5406017 N|
|Recepción de datos|En línea|
|Inicio de operación|06-04-2013|
|Estado|Vigente|

_Fuente: https://sinca.mma.gob.cl/_

El periodo contemplado para la caracterización de la calidad de aire de la comuna de Puerto
Montt, perteneciente a la Macrozona Centro-Norte de la Región de Los Lagos, correspondió a los
últimos 6 años de datos completos de la estación (periodo 2017 - 2022).

**2.1.2.** **Concentración promedio anual**

Las concentraciones promedio anual de material particulado fino respirable (MP 2,5 ) para la
Macrozona Centro-Norte de la Región de Los Lagos, que incluye la Comuna de Puerto Montt, se
presentan en las **¡Error! No se encuentra el origen de la referencia.** a continuación:

**Figura 1. Concentración promedio anual de MP** **2,5** **.**

_Fuente: Elaboración propia con base en datos obtenidos de https://sinca.mma.gob.cl/_

De acuerdo a la figura precedente se puede apreciar que la concentración promedio anual de
MP 2,5 se mantiene entre los 23 y 30 μg/m [3] y no presenta tendencia a través del tiempo. Por otro

11

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

lado, de acuerdo a las condiciones de superación establecidas por la norma de calidad primaria
para material particulado fino respirable (MP 2,5 ), D.S. N°12/2011 del MMA, la comuna se

mantiene en condición de zona saturada.

**2.1.3.** **Concentración promedio mensual MP** **2,5**

Con respecto a la concentración promedio mensual de material particulado fino respirable (MP 2,5 )
para la Macrozona Centro-Norte de la Región de Los Lagos, tal como se puede observar en la
Figura 2 a continuación, ésta tiende al aumento en los meses de otoño - invierno, periodo entre
abril y septiembre, mostrando las mayores concentraciones en los meses de junio y julio. Esto es
consistente con la mayor tasa de emisión proveniente de la combustión residencial de leña, la
cual se lleva a cabo durante el periodo correspondiente a las mayores concentraciones.

**Figura 2. Concentración promedio mensual de MP** **2,5** **.**

_[Fuente: Elaboración propia con base en datos obtenidos de https://sinca.mma.gob.cl/](https://sinca.mma.gob.cl/)_

Finalmente, con respecto a la variación de los promedios mensuales para los diferentes años
considerados para el análisis, no se muestra una tendencia clara a través del tiempo, tal como se
mencionó anteriormente para las concentraciones promedio anuales. Existiendo meses en los
que las concentraciones tienden al aumento y al mismo tiempo, otros demuestran tendencias a
la disminución para el mismo año, lo cual, como se menciona anteriormente, puede estar
relacionado al tipo de fuente emisora presente en las distintas estaciones del año.

12

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

**2.1.4.** **Concentración promedio diaria, percentil 98 y variación horaria de MP** **2,5** **.**

A continuación, se presentan las figuras de concentración promedio diaria de material particulado
fino respirable (MP 2,5 ), su percentil 98 y la variación horaria promedio en los meses otoñoinvierno para el periodo 2017 - 2022 en la Macrozona Centro-Norte de la Región de Los Lagos.

En primer lugar, se presenta la concentración promedio diaria de MP 2,5 entre los años 2017 y
2022 (Figura 3).

**Figura 3. Concentración promedio diaria de MP** **2,5** **.**

_Fuente: Elaboración propia con base en datos obtenidos de https://sinca.mma.gob.cl/_

Los datos muestran una clara tendencia al aumento en los meses otoño - invierno para todo el
periodo considerado. Adicionalmente, desde el año 2019 se presentan peaks elevados en
periodos previos a los meses de invierno, a diferencia de los años precedentes, lo cual se
presume que puede estar relacionado con un aumento en los incendios forestales que han tenido
lincidencia en la zona. Ambos comportamientos también se pueden observar en la Figura 2.
Concentración promedio mensual de MP2,5.

Adicionalmente, para poder realizar un análisis con respecto a la condición de superación
establecida en las normas primarias de calidad ambiental (D.S. N°12/2011 del MMA y D.S.
N°12/2022 del MMA), en la Figura 4 a continuación, se presentan los percentiles 98 de los
promedios diarios de MP 2,5 y el límite establecido por dicha norma.

13

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

**Figura 4. Percentil 98 de promedios diarios de MP** **2,5** **.**

_Fuente: Elaboración propia con base en datos obtenidos de https://sinca.mma.gob.cl/_

De acuerdo a estos gráficos, se puede observar que en todo el periodo considerado (20172022) la norma primaria de calidad ambiental para MP 2,5 se encuentra superada. El resultado de
las mediciones efectuadas en la estación de monitoreo “Mirasol” (considerada para el análisis del
presente informe), en el periodo comprendido entre el 1 de enero de 2017 y el 31 de diciembre
del año 2019, permitió declarar a la Macrozona Centro-Norte de la Región de Los Lagos como
zona saturada por material particulado fino respirable (MP 2,5 ), como concentración diaria, a través

del D.S. N°24/2021 del MMA. Esta condición se ha mantenido a través de los años. No se muestra

ninguna tendencia de disminución o aumento de concentraciones, sin embargo, en el año 2017
es donde se presenta la mayor superación de la norma.

De acuerdo a las condiciones de superación de la norma primaria de calidad ambiental para
MP 2,5, el año 2022 presenta un comportamiento diferente con respecto al resto de los años del
periodo considerado para la caracterización de la calidad del aire de la Macrozona Centro-Norte
de la Región de Los Lagos. De acuerdo a la Figura 3, las concentraciones del año 2021
comprendidas entre el periodo otoño - invierno son relativamente mayores en comparación a los
años precedentes (2020-2021 presentan valores de concentración a la baja), permitiendo inferir
que la calefacción residencial de leña ha ido en aumento a través de los años (principal fuente
emisora). Por otro lado, las concentraciones del año 2022 comprendidas entre el periodo
primavera - verano son menores con respecto a los años precedentes. De acuerdo a esto, el
percentil 98 de los promedios diarios tiende a ser mayor para el año 2022, con respecto al resto
de los años considerados, ya que se presentan concentraciones de mayor magnitud.

14

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

Finalmente, y con el objetivo de caracterizar con mayor detalle el periodo comprendido entre los
meses de abril a septiembre, periodo que corresponde al contemplado para la estimación de
emisiones atmosféricas provenientes de la calefacción domiciliaria en la fase de operación del
proyecto (principal fuente generadora de material particulado), se graficó el promedio horario de
las concentraciones, lo cual se puede observar en la Figura 5

**Figura 5. Concentración promedio horaria para meses otoño - invierno MP** **2,5** **.**

_Fuente: Elaboración propia con base en datos obtenidos de https://sinca.mma.gob.cl/_

De acuerdo a lo observado en el gráfico, la tendencia de las concentraciones horarias es similar
para todos los meses, siendo abril y septiembre los meses que presentan concentraciones de
una menor magnitud con respecto a los demás. La tendencia horaria es clara; se presenta un
aumento de la concentración a partir de las 15 horas, disminuyendo en el transcurso de la
madrugada, para volver a aumentar a partir de las 7 horas. Se infiere que este comportamiento
se debe a la relación de las actividades diarias de las personas y la calefacción residencial de
leña, principal fuente emisora de material particulado fino respirable en la comuna de Puerto
Montt, ya que coincide con los horarios en que las personas se encuentran activas. El peak de
las concentraciones se presenta entre las 20 horas y 23 horas, cuando la mayoría de personas
se encuentran en sus viviendas. Asimismo, el leve aumento de la concentración a las 7 horas,

coincide con el inicio de las actividades diarias.

15

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

**2.2.** **Antecedentes Meteorológicos**

Al momento de analizar la dispersión de contaminantes en la atmósfera, es muy importante
caracterizar la meteorología de la zona de estudio, dado que sus parámetros, tales como vientos,
temperatura y precipitación, entre otros, influyen de muchas maneras sobre la concentración. A
continuación, se presenta la caracterización de los vientos, temperatura y precipitación de la

comuna de Puerto Montt.

Para determinar la línea de base meteorológica del área donde se emplazará el Proyecto, se han
utilizado los datos registrados en la estación Mirasol, ubicada a cerca de 4 km del proyecto, y que
pertenece al Sistema de Información Nacional de Calidad de Aire (SINCA).

Cabe destacar que la estación de monitoreo “Mirasol” no registra valores de precipitación, por lo
que se utilizó la información disponible en la base de datos del Explorador Climático CR2,
estación Puerto Montt DGA, la cual entrega valores normales mensuales considerando un
periodo de 30 años de datos. Para la consistencia en la presentación de la información, se
construyó un climograma con temperaturas obtenidas de esta misma fuente. Por su parte, la
información de los vientos fue extraída del registro de la estación de monitoreo “Mirasol”.

**2.2.1.** **Vientos**

Para la presentación de los vientos, se consideró como periodo de tiempo el año 2022. Los datos
fueron procesados con el software WRPlot, versión 8.0.2, y se construyeron rosas de vientos
estacionales. En la Figura 6 a continuación, se presentan las rosas de dirección de viento para

cada estación del año.

16

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

**Figura 6. Rosas de dirección de viento por estación del año.**

|Verano|Otoño|
|---|---|
|||
|**Invierno**|**Primavera**|
|||

_Fuente: Elaboración propia con base en datos obtenidos de https://sinca.mma.gob.cl/_

De acuerdo a lo mostrado en la Figura 6, los vientos predominantes de la comuna de Puerto
Montt corresponden a vientos variables provenientes desde las distintas direcciones,
principalmente desde el Noroeste en las estaciones de Invierno y Primavera, durante el mes de
Invierno de igual forma se demuestra una alta cantidad de vientos mayores provenientes desde

17

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

el este, durante el otoño se muestra que los vientos son prioritariamente provenientes desde el
Norte y por último en la estación de Verano existe una mayoría de vientos que vienen desde
dirección sur. En cuanto a las mayores velocidades de viento, estas se presentan en verano.

**2.2.2.** **Temperatura y Precipitación**

A continuación, en la Figura 7, se presenta un climograma que incluye precipitación y temperatura
mensual normal para la comuna de Puerto Montt. A diferencia de la información entregada
anteriormente, la cual fue en base a la información obtenida de la estación Mirasol, debido a que
esta no mantiene un registro de datos meteorológicos de larga data, se decidió utilizar los datos
entregados por la estación Puerto Montt de la DGA, la cual presenta información de
precipitaciones desde el año 1976 y se obtuvo desde el Explorador Climático CR2, el que puede
entregar valores históricos de un periodo de 30 años.

**Figura 7. Precipitación y temperaturas, Puerto Montt.**

_Fuente: Dirección Meteorológica de Chile._

De acuerdo al gráfico anterior, las precipitaciones se presentan principalmente en invierno, siendo
junio el mes más lluvioso. Con respecto a las temperaturas, éstas mantienen una tempratura
promedio que oscila entre los 9 y 17 °C (Tabla 3), presentando los valores más bajos en el periodo
otoño - invierno, lo que coincide con los periodos de mayor concentración de material particulado
fino respirable MP 2,5, ya que en dicha época del año surge la necesidad de calefaccionar las
viviendas, lo cual se realiza principalmente a través de la combustión de leña.

18

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

**Tabla 3. Precipitación y temperatura normal mensual, Puerto Montt, estación “Puerto Montt-**

**DGA”.**

|Mes|Precipitación (mm)|Temperatura (°C)|
|---|---|---|
|ENE|2,81|15,59|
|FEB|2,98|16,19|
|MAR|3,63|12,21|
|ABR|5,28|10,22|
|MAY|6,77|11,12|
|JUN|8,86|9,90|
|JUL|7,09|9,57|
|AGO|6,76|10,15|
|SEP|4,24|10,73|
|OCT|4,43|9,85|
|NOV|3,87|13,38|
|DIC|3,34|14,95|

_Fuente: Dirección Meteorológica de Chile._

**2.3.** **Antecedentes Generales del Proyecto**

El Proyecto Senderos de Tenglo consiste la construcción de 462 viviendas y 3 salas multiuso.
Avenida Los Notros con Avenida Río Taylor, comuna de Puerto Montt. Este terreno se ubica en
el sector poniente de la ciudad de Puerto Montt, provincia de Llanquihue, Región de Los Lagos.

Con respecto a las emisiones que generará el proyecto en de acuerdo a la metodología explicada
en el Estudio de Emisiones Atmosféricas adjunto en el Anexo 02, las principales actividades que
generan emisiones se presentan en la fase de operación del proyecto (Calefacción de viviendas
y tránsito de vehículos particulares).

Por lo tanto, la tasa de emisión utilizada para la modelación de la dispersión del material
particulado (MP 10 y MP 2,5 ) y gases de combustión (SO 2, NO 2 y CO) corresponde a la emisión
directa de estos compuestos durante la fase de operación. Debido a que las emisiones se
generarán en distintos sectores del área de emplazamiento del proyecto, área de calefacción y
área de tránsito de vehículos por vías pavimentadas. Las emisiones directas de MP 10 y MP 2,5 y
gases de combustión (SO2, NO2 y CO) generadas en cada área del proyecto se presentan en la

tabla a continuación:

19

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

**Tabla 4. Áreas de emisión, fase de operación del proyecto.**

|Áreas de emisión|Emisión (t/año)|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|**Áreas de emisión**|**MP10**|**MP2,5**|**NOx**|**SO2 **|**CO**|
|Área Operación<br>(calefacción viviendas)|5,7461|5,2864|4,3670|0,2298|206,85|
|Rutas Pavimentadas<br>Operación (vehículos<br>particulares)|0,4828|0,1181|0,0725|0,0024|0,7368|

_Fuente: Elaboración propia._

20

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

**3.** **JUSTIFICACIÓN DE LOS MODELOS UTILIZADOS EN LA MODELACIÓN**

**3.1.** **Uso del Modelo CALPUFF.**

La modelación de dispersión atmosférica de las emisiones de MP 2.5 y MP 10 generadas por el
proyecto, se realizó a través un modelo tipo “Puff”, específicamente el modelo CALPUFF.

Tal como lo define la Guía, los modelos tipo “puff” son una combinación entre los modelos
Gaussianos y los modelos Lagrangeanos, en el sentido de que esencialmente calculan la
dispersión de contaminantes provenientes de una emisión instantánea, llamada “puff”, a lo largo
de una trayectoria. Su aproximación matemática consiste en estimar la dispersión en forma
Gaussiana en cada punto de una trayectoria, es decir, los modelos tipo “puff” sólo requieren una
trayectoria por “puff”, lo que hace su cálculo mucho más rápido. En el caso de emisiones
continuas, se simulan las trayectorias y la dispersión Gaussiana de muchos “puffs”. El modelo
tipo “puff” recomendado por la Guía es el modelo CALPUFF.

El CALPUFF, es un modelo completo que incorpora herramientas para procesar datos
meteorológicos y geofísicos, modelos de dispersión y pos procesamiento. Dicho modelo es
recomendado por la Agencia de Protección Ambiental de los Estados Unidos (EPA) para modelar
transporte de contaminantes a larga distancia.

CALPUFF se compone de tres módulos:

 CALMET: Es un modelo meteorológico que desarrolla campos horarios de viento y temperatura

en una grilla de tres dimensiones. También asocia campos en dos dimensiones de altura y usos

de suelo.

Este módulo puede ser reemplazado por el modelo matemático WRF, cuyo uso es recomendado
por la guía citada.

 CALPUFF: Es un modelo de transporte y dispersión emitido desde fuentes modeladas, simulando

procesos de dispersión y transformación. CALPUFF utiliza los datos generados por CALMET.
Los archivos de salida de CALPUFF contienen las concentraciones horarias o deposición por
hora de flujos evaluados en receptores seleccionados.

 CALPOST: Es usado para procesar aquellos archivos generados por CALMET y CALPUFF,

produciendo tabulaciones que resumen los resultados de la simulación.

Ecuación del modelo CALPUFF

La ecuación básica que utiliza el modelo para realizar las modelaciones es la siguiente:

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

21

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

Dónde:

C, es concentración a nivel del suelo (g/m3),

Q, es masa de contaminantes (g) en la nube.

σx, es desviación estándar (m) de la distribución de Gauss en el viento a lo largo de la dirección.

σy, es desviación estándar (m) de la distribución de Gauss en el viento de costado

σz, es desviación estándar (m) de la distribución de Gauss en la dirección vertical.

da, es distancia (m) del centro de la nube al receptor en la dirección del viento a lo largo.

dc, es distancia (m) del centro de la nube al receptor en la dirección de viento cruzado.

g, es el término vertical (m) de la ecuación Gaussiana.

H, es la altura afectiva (m) desde el nivel del suelo del hojaldre.

h, es la altura de la capa de mezcla.

De acuerdo a las características del terreno, las distintas unidades geomorfológicas del área de
influencia del proyecto y el dominio de la modelación se consideró utilizar el modelo CALPUFF
para simular la dispersión de los contaminantes.

**3.2.** **Uso del Modelo Weather Research and Forecasting Model (WRF).**

El modelo Weather Research and Forecasting (WRF), es un modelo numérico recomendado para
la generación de datos meteorológicos y uno de los modelos de pronóstico meteorológicos más

avanzados.

Debido a la falta de una red robusta de estaciones meteorológicas, la Guía para el Uso de
Modelos de Calidad del Aire en el SEIA recomienda el uso de WRF por sobre el uso del CALMET.
Además, el mismo documento, sugiere el uso del WRF para la modelación de dispersión de

contaminantes con CALPUFF.

22

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

**4.** **METODOLOGÍA**

La modelación de la dispersión de contaminantes se realizó de acuerdo a la siguiente
metodología.

**4.1.** **Dominio Modelación Meteorológica**

El modelo WRF es un modelo matemático que simula, a partir de variables influyentes en la
meteorología, las condiciones meteorológicas dentro de un dominio de modelación. Para el
presente caso, se consideró un dominio de 74 x 74 km, con 1 km de resolución, y 10 celdas de
altura desde 0 m hasta los 4.000 m, permitiendo considerar un amplio rango para la variación
diaria de la capa de mezcla.

El dominio de modelación WRF abarca toda el área circundante a la zona de emplazamiento del
proyecto, incluyendo la comuna de Puerto Montt y comunas aledañas, tal como se muestra en la
Figura 8. Las coordenadas de los vértices y el centroide del dominio de la modelación WRF, se
presentan en la **Tabla 5** a continuación:

**Tabla 5. Coordenadas de vértices y centroide del dominio de Modelación WRF.**

|Vértice|Proyección UTM, Huso 18 Sur; Datum WGS-84|Col3|
|---|---|---|
|**Vértice**|**Este (m)**|**Norte (m)**|
|Noroeste|629821|5440620|
|Noreste|702846|5440753|
|Suroeste|629463|5366934|
|Sureste|702621|5367727|
|Centroide|665773|5404386|
|Proyecto|665732|5404448|

_Fuente: Elaboración propia._

23

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

|Figura 8. Dominio modelación WRF.|Col2|Col3|
|---|---|---|
||||
|**Carta:**|**Escala:**|**Simbología**|
|DOMINIO MODELACIÓN WRF|1:500.000|<br> <br>Proyecto<br>Dominio|
|DOMINIO MODELACIÓN WRF|**Proyección:**<br>|**Proyección:**<br>|
|DOMINIO MODELACIÓN WRF|WGS 84 UTM H18S|WGS 84 UTM H18S|

24

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

**4.2.** **Dominio de Modelación CALPUFF**

El dominio de la modelación de CALPUFF se extiende sobre el mismo dominio de la modelación

WRF, correspondiente a un área 74 km x 74 km, tal como se presenta en la Figura 9. Esto para
evaluar la mayor cantidad de territorio posible con las herramientas disponibles.

|Figura 9. Dominio de la Modelación de CALPUFF.|Col2|Col3|
|---|---|---|
||||
|**Carta:**|**Escala:**|**Simbología**|
|DOMINIO MODELACIÓN WRF|1:500.000|<br> <br>Proyecto<br>Dominio|
|DOMINIO MODELACIÓN WRF|**Proyección:**<br>|**Proyección:**<br>|
|DOMINIO MODELACIÓN WRF|WGS 84 UTM H18S|WGS 84 UTM H18S|

_Fuente: Elaboración propia._

25

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

Las coordenadas de los vértices y el centroide del dominio de la modelación CALPUFF, se
presentan en la Tabla 6 a continuación:

**Tabla 6. Coordenadas de vértices y centroide del dominio de Modelación CALPUFF.**

|Vértice|Proyección UTM, Huso 18 Sur; Datum WGS-84|Col3|
|---|---|---|
|**Vértice**|**Este (m)**|**Norte (m)**|
|Noroeste|629821|5440620|
|Noreste|702846|5440753|
|Suroeste|629463|5366934|
|Sureste|702621|5367727|
|Centroide|665773|5404386|
|Proyecto|665732|5404448|

_Fuente: Elaboración propia._

**4.3.** **Post procesamiento de información**

Para analizar los resultados de la modelación de dispersión de MP 10, MP 2,5, NO 2, CO y SO 2, se
realizaron mapas de iso-concentraciones definidas en cada una de las normativas de calidad
primaria por compuesto evaluado, asociado a las emisiones generadas en la fase de operación
del proyecto. Dicho mapa permite evaluar los niveles de concentración en toda el área de estudio
con respecto a la norma primaria de calidad ambiental.

Es importante señalar que este mapa nace de la modelación del dominio, representado a través
de una grilla de resolución 1 km, la que entrega datos de concentración de cada vértice de la
misma. Dadas las características de la grilla, los mapas son el resultado de la interpolación entre
los datos de modelación en cada vértice. Además, los datos de concentración generados por el
modelo son el resultado de la concentración promedio de la primara capa de modelación, la que
tiene lugar desde 0 m nivel del suelo hasta los 20 m.

De acuerdo a lo anterior, el mapa de dispersión e isoconcentración es considerado como una
representación espacial de la pluma y no como referencia concreta de la concentración, pues

éstas suelen estar sobre dimensionadas.

Por otro lado, la evaluación de la concentración en puntos discretos ofrece un sentido de la
magnitud más libre de distorsiones. Por esta razón y con objeto de analizar el impacto en la
calidad del aire sobre la salud de las personas, se consideró adicionalmente una modelación
discreta en 11 receptores específicos que corresponden principalmente a viviendas o
establecimientos habitables cercanos al proyecto.

En la Tabla 7, se identifica cada uno de los receptores, se presentan sus coordenadas y la
distancia con respecto al proyecto (punto más cercano ya sea del polígono del proyecto o
camino). Así mismo, en la Figura 10, se puede observar la ubicación espacial de estos puntos
con respecto al proyecto.

26

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

**Tabla 7. Coordenadas de receptores discretos.**

|Receptor|Punto|Coordenadas WGS 84 UTM 18S|Col4|Distancia respecto<br>al proyecto (m)|
|---|---|---|---|---|
|**Receptor**|**Punto**|**Este (m)**|**Norte (m)**|**Norte (m)**|
|Conjunto de viviendas|R1|665620|5404347|43,85|
|Conjunto de viviendas|R2|665572|5404289|27,50|
|Conjunto de viviendas|R3|665605|5404459|35,37|
|Conjunto de viviendas|R4|665494|5404392|157,11|
|Conjunto de viviendas|R5|666109|5405023|523,38|
|Conjunto de viviendas|R6|665709|5403921|133,42|
|Conjunto de viviendas|R7|665906|5403830|298,31|
|Establecimiento Privado|R8|665968|5404102|128,57|
|Conjunto de viviendas|R9|665488|5404579|138,08|
|Conjunto de viviendas|R10|665290|5404554|326,39|
|Conjunto de viviendas|R11|665286|5405067|610,81|

_Fuente: Elaboración propia._

27

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

|Figura 10. Ubicación receptores.|Col2|Col3|
|---|---|---|
||||
|**Carta:**|**Escala:**|**Simbología **|
|RECEPTORES DISCRETOS|1:10.000|<br>Receptores<br>Proyecto Construcción<br>Proyecto Operación|
|RECEPTORES DISCRETOS|**Proyección**:|**Proyección**:|
|RECEPTORES DISCRETOS|WGS 84 UTM H18S|WGS 84 UTM H18S|

**4.4.** **Escenario de modelación.**

_Fuente: Elaboración propia._

La tasa de emisión utilizada para la modelación de la dispersión del material particulado (MP 10 y
MP 2,5 ) y gases (CO, NO 2 y SO 2 ) corresponde a la emisión directa de estos compuestos durante
la fase de operación. Debido a que las emisiones se generarán en distintos sectores del área de
emplazamiento del proyecto, área de operación del proyecto y área de tránsito de vehículos y
camiones por vías pavimentadas desde proyecto Senderos de Tenglo hasta sus distintos

28

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

destinos, se definieron dieciséis fuentes de área asociadas a cada uno de los sectores donde se
desarrollan las diferentes actividades emisoras de MP 10 y MP 2,5, CO, NO 2 y SO 2 .

Se definió un polígono de 4 vértices para los sectores de emisión (cantidad de vértices requerido
por el modelo para fuentes de área) para las áreas de caminos no pavimentados y la zona de
construcción y operación del proyecto.

Finalmente, en la Figura 11 y la Tabla 8 se muestran las fuentes de área y las coordenadas de
sus vértices.

**Figura 11. Fuentes de emisión de área.**

|Col1|Carta:|Col3|
|---|---|---|
||FUENTES DE<br>EMISIÓN|FUENTES DE<br>EMISIÓN|
||**Escala:**|**Escala:**|
||1:6.000|1:6.000|
||**Proyección:**|**Proyección:**|
||WGS 84 UTM H18S|WGS 84 UTM H18S|
||**Simbología**|**Simbología**|
|||Calefacción<br>de<br>viviendas<br>Tránsito caminos<br>pavimentados<br>Vértices|

_Fuente: Elaboración propia._

29

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

**Tabla 8. Coordenadas fuente puntual y polígonos de fuente de área.**

|Área de emisión|Vértice|Proyección UTM, Huso 18 Sur; Datum WGS-84|Col4|
|---|---|---|---|
|**Área de emisión**|**Vértice**|**Este (m)**|**Norte (m)**|
|Polígono Operación<br>(Viviendas zona Norte)|1|665809,2|5404414,9|
|Polígono Operación<br>(Viviendas zona Norte)|2|665668,6|5404333,1|
|Polígono Operación<br>(Viviendas zona Norte)|3|665622,0|5404561,2|
|Polígono Operación<br>(Viviendas zona Norte)|4|665799,3|5404601,7|
|Polígono Operación<br>(Viviendas zona Sur)|1|665526,7|5404227,5|
|Polígono Operación<br>(Viviendas zona Sur)|2|665811,5|5404400,9|
|Polígono Operación<br>(Viviendas zona Sur)|3|665854,1|5404151,2|
|Polígono Operación<br>(Viviendas zona Sur)|4|665700,4|5404059,1|
|Ruta Pavimentada 1|1|665668,8|5404329,2|
|Ruta Pavimentada 1|2|665806,7|5404408,9|
|Ruta Pavimentada 1|3|665808,4|5404403,7|
|Ruta Pavimentada 1|4|665672,4|5404324,2|
|Ruta Pavimentada 2|1|665504,6|5404232,1|
|Ruta Pavimentada 2|2|665668,2|5404328,9|
|Ruta Pavimentada 2|3|665670,8|5404323,6|
|Ruta Pavimentada 2|4|665507,9|5404229,1|
|Ruta Pavimentada 3|1|665330,3|5404390,0|
|Ruta Pavimentada 3|2|665507,1|5404229,3|
|Ruta Pavimentada 3|3|665502,4|5404225,0|
|Ruta Pavimentada 3|4|665327,1|5404385,4|
|Ruta Pavimentada 4|1|665330,6|5404390,6|
|Ruta Pavimentada 4|2|665339,2|5404405,9|
|Ruta Pavimentada 4|3|665343,3|5404403,7|
|Ruta Pavimentada 4|4|665334,3|5404387,3|
|Ruta Pavimentada 5|1|665339,6|5404406,6|
|Ruta Pavimentada 5|2|665324,2|5404478,3|
|Ruta Pavimentada 5|3|665329,4|5404478,0|
|Ruta Pavimentada 5|4|665343,2|5404404,4|
|Ruta Pavimentada 6|1|665324,5|5404478,7|
|Ruta Pavimentada 6|2|665347,6|5404506,5|
|Ruta Pavimentada 6|3|665353,2|5404505,3|
|Ruta Pavimentada 6|4|665329,6|5404478,2|
|Ruta Pavimentada 7|1|665347,6|5404507,3|
|Ruta Pavimentada 7|2|665325,3|5404608,1|
|Ruta Pavimentada 7|3|665330,4|5404610,6|
|Ruta Pavimentada 7|4|665352,9|5404506,5|
|Ruta Pavimentada 8|1|665324,8|5404608,5|
|Ruta Pavimentada 8|2|665286,5|5404727,4|
|Ruta Pavimentada 8|3|665290,6|5404730,9|
|Ruta Pavimentada 8|4|665329,4|5404611,4|
|Ruta Pavimentada 9|1|665286,0|5404727,6|
|Ruta Pavimentada 9|2|665004,7|5405088,7|

30

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

|Col1|3|665010,9|5405093,8|
|---|---|---|---|
||4|665290,6|5404731,3|

_Fuente: Elaboración propia._

De esta manera, la tasa de emisión de cada área está dada por la emisión y la superficie del
polígono definido (Tabla 9). Cabe destacar que, para definir la tasa emisión de material
particulado (MP 10 y MP 2,5 ) y gases (CO, NO 2 y SO 2 ) asociada a cada sector, las emisiones
directas generadas por el proyecto se agruparon de acuerdo al área donde se ejecutan
(Operación por calefacción de viviendas y por tránsito de vehículos en caminos pavimentados),
cuyo detalle se puede consultar en el estudio de Emisiones Atmosféricas adjunto.

**Tabla 9. Tasa de emisión.**

|Área de emisión|Tipo de<br>fuente|Superficie<br>polígono<br>(m2)|Tasa de emisión (Ton/año-m2)|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Área de emisión**|**Tipo de**<br>**fuente**|**Superficie**<br>**polígono**<br>**(m2) **|**MP10 **|**MP2,5 **|**NOx**|**SO2 **|**CO**|
|Área Operación<br>(Calefacción<br>viviendas)|Área|94.782|6,06E-05|5,58E-05|4,61E-05|2,42E-06|2,18E-03|
|Área Operación<br>(Tránsito de<br>vehículos)|Área|8.212|5,88E-05|1,44E-05|8,83E-06|2,89E-07|8,97E-05|

_Fuente: Elaboración propia._

31

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

**5.** **RESULTADOS**

**5.1.** **Caracterización Geofísica**

**5.1.1.Topografía**

En la Figura 12, se puede observar la topografía dentro del dominio de modelación meteorológica.
La elevación del terreno varía entre los 0 y 1582,2 m.s.n.m. El punto rojo del centro representa la
ubicación del proyecto, el cual se encuentra a una elevación de 93,62 m.s.n.m. aproximadamente.

**Figura 12. Elevación de terreno del área de estudio**

|Col1|Carta:|
|---|---|
||ELEVACIÓN DEL<br>TERRENO|
||**Escala:**|
||1:400.000|
||**Proyección:**|
||WGS 84 UTM H18S|
||**Simbología**|
|||

_Fuente: Elaboración propia._

32

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

**5.2.** **Concentraciones**

A continuación, se presentan los resultados de la modelación de las emisiones de MP 10, MP 2,5,
NO 2, SO 2 y CO, tanto para la dispersión dentro del área de estudio, como para la evaluación de
los puntos discretos cercanos al proyecto.

**5.2.1.** **Dispersión y concentración de compuestos dentro del área de estudio en relación a**

**normativa primaria de calidad de aire.**

Para evaluar la concentración de los compuestos evaluados, aportada por las emisiones
generadas por el proyecto se elaboró un mapa de iso-concentración de los límites establecidos
en cada una de las concentraciones expuestas en las normas de calidad primaria, dichos mapas
de iso-lineas de concentración de MP 10, MP 2,5, NO 2, CO, SO 2 en el entorno del Proyecto.

33

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

|Figura 13. Iso-concentración del promedio anual de MP10.|Col2|Col3|
|---|---|---|
||||
|**Carta:**|**Escala:**|**Simbología **|
|ISO-CONCENTRACIÓN DEL PROMEDIO<br>ANUAL DE MP10.|1:20.000|<br> <br> <br> <br>0,3 μg/m3 <br>0,6 μg/m3 <br>0,9 μg/m3 <br>1,2 μg/m3 <br>1,5 μg/m3 <br>1,8 μg/m3 <br>Receptores<br>Proyecto (Tránsito de vehiculos)<br>Proyecto (Calefacción viviendas)|
|ISO-CONCENTRACIÓN DEL PROMEDIO<br>ANUAL DE MP10.|**Proyección**:|**Proyección**:|
|ISO-CONCENTRACIÓN DEL PROMEDIO<br>ANUAL DE MP10.|WGS 84 UTM H18S|WGS 84 UTM H18S|

_Fuente: Elaboración propia._

34

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

|Figura 14. Iso-concentración del percentil 98 de promedios diarios de MP10.|Col2|Col3|
|---|---|---|
||||
|**Carta:**|**Escala:**|**Simbología **|
|ISO-CONCENTRACIÓN DEL PERCENTIL 98<br>DE PROMEDIOS DIARIOS DE MP10.|1:24.000|<br> <br>1 μg/m3 <br>2 μg/m3 <br>3 μg/m3 <br>4 μg/m3 <br>5 μg/m3 <br>6 μg/m3 <br>7 μg/m3 <br>Receptores<br>Proyecto (Tránsito de vehiculos)<br>Proyecto (Calefacción viviendas)|
|ISO-CONCENTRACIÓN DEL PERCENTIL 98<br>DE PROMEDIOS DIARIOS DE MP10.|**Proyección**:|**Proyección**:|
|ISO-CONCENTRACIÓN DEL PERCENTIL 98<br>DE PROMEDIOS DIARIOS DE MP10.|WGS 84 UTM H18S|WGS 84 UTM H18S|

_Fuente: Elaboración propia._

35

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

|Figura 15. Iso-concentración del promedio anual de MP2,5.|Col2|Col3|
|---|---|---|
||||
|**Carta:**|**Escala:**|**Simbología **|
|ISO-CONCENTRACIÓN DEL PROMEDIO<br>ANUAL DE MP2,5.|1:20.000|<br> <br> <br> <br>0,2 μg/m3 <br>0,4 μg/m3 <br>0,6 μg/m3 <br>0,8 μg/m3 <br>1,0 μg/m3 <br>1,2 μg/m3 <br>Receptores<br>Proyecto (Tránsito de vehiculos)<br>Proyecto (Calefacción viviendas)|
|ISO-CONCENTRACIÓN DEL PROMEDIO<br>ANUAL DE MP2,5.|**Proyección**:|**Proyección**:|
|ISO-CONCENTRACIÓN DEL PROMEDIO<br>ANUAL DE MP2,5.|WGS 84 UTM H18S|WGS 84 UTM H18S|

_Fuente: Elaboración propia._

36

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

**Figura 16. Iso-concentración del percentil 98 de promedios diarios de MP** **2,5** **.**

|Col1|Col2|Col3|
|---|---|---|
|**Carta:**|**Escala:**|**Simbología**|
|ISO-CONCENTRACIÓN DEL PERCENTIL 98<br>DE PROMEDIOS DIARIOS DE MP2,5.|1:24.000|<br> <br> <br>1 μg/m3 <br>2 μg/m3 <br>3 μg/m3 <br>4 μg/m3 <br>5 μg/m3 <br>6 μg/m3 <br>Receptores<br>Proyecto (Tránsito de vehiculos)<br>Proyecto (Calefacción viviendas)|
|ISO-CONCENTRACIÓN DEL PERCENTIL 98<br>DE PROMEDIOS DIARIOS DE MP2,5.|**Proyección**:|**Proyección**:|
|ISO-CONCENTRACIÓN DEL PERCENTIL 98<br>DE PROMEDIOS DIARIOS DE MP2,5.|WGS 84 UTM H18S|WGS 84 UTM H18S|

_Fuente: Elaboración propia._

37

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

|Figura 17. Iso-concentración del promedio anual de SO2.|Col2|Col3|
|---|---|---|
||||
|**Carta:**|**Escala:**|**Simbología **|
|ISO-CONCENTRACIÓN DEL PROMEDIO<br>ANUAL DE SO2.|1:20.000|<br> <br>0,01 μg/m3 <br>0,02 μg/m3 <br>0,03 μg/m3 <br>0,04 μg/m3 <br>0,05 μg/m3 <br>0,06 μg/m3 <br>0,07 μg/m3 <br>Receptores<br>Proyecto (Tránsito de vehiculos)<br>Proyecto (Calefacción viviendas)|
|ISO-CONCENTRACIÓN DEL PROMEDIO<br>ANUAL DE SO2.|**Proyección**:|**Proyección**:|
|ISO-CONCENTRACIÓN DEL PROMEDIO<br>ANUAL DE SO2.|WGS 84 UTM H18S|WGS 84 UTM H18S|

38

_Fuente: Elaboración propia._

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

|Figura 18. Iso-concentración del percentil 99 de promedios diarios de SO2.|Col2|Col3|
|---|---|---|
||||
|**Carta:**|**Escala:**|**Simbología **|
|ISO-CONCENTRACIÓN DEL PERCENTIL<br>99 DE PROMEDIOS DIARIOS DE SO2.|1:20.000|<br> <br> <br>0,04 μg/m3 <br>0,08 μg/m3 <br>0,12 μg/m3 <br>0,16 μg/m3 <br>0,20 μg/m3 <br>Receptores<br>Proyecto (Tránsito de vehiculos)<br>Proyecto (Calefacción viviendas)|
|ISO-CONCENTRACIÓN DEL PERCENTIL<br>99 DE PROMEDIOS DIARIOS DE SO2.|**Proyección**:|**Proyección**:|
|ISO-CONCENTRACIÓN DEL PERCENTIL<br>99 DE PROMEDIOS DIARIOS DE SO2.|WGS 84 UTM H18S|WGS 84 UTM H18S|

39

_Fuente: Elaboración propia._

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

|Figura 19. Iso-concentración del percentil 99 de promedios horarios de SO2.|Col2|Col3|
|---|---|---|
||||
|**Carta:**|**Escala:**|**Simbología **|
|ISO-CONCENTRACIÓN DEL<br>PERCENTIL 99 DE PROMEDIOS<br>HORARIOS DE SO2.|1:24.000|<br> <br>0,3 μg/m3 <br>0,6 μg/m3 <br>0,9 μg/m3 <br>1,2 μg/m3 <br>1,5 μg/m3 <br>1,8 μg/m3 <br>Receptores<br>Proyecto (Tránsito de vehiculos)<br>Proyecto (Calefacción viviendas)|
|ISO-CONCENTRACIÓN DEL<br>PERCENTIL 99 DE PROMEDIOS<br>HORARIOS DE SO2.|**Proyección**:|**Proyección**:|
|ISO-CONCENTRACIÓN DEL<br>PERCENTIL 99 DE PROMEDIOS<br>HORARIOS DE SO2.|WGS 84 UTM H18S|WGS 84 UTM H18S|

40

_Fuente: Elaboración propia._

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

|Figura 20. Iso-concentración del promedio anual de NO2.|Col2|Col3|
|---|---|---|
||||
|**Carta:**|**Escala:**|**Simbología **|
|ISO-CONCENTRACIÓN DEL PROMEDIO<br>ANUAL DE NO2.|1:20.000|<br> <br> <br>0,1 μg/m3 <br>0,2 μg/m3 <br>0,3 μg/m3 <br>0,4 μg/m3 <br>0,5 μg/m3 <br>0,6 μg/m3 <br>0,7 μg/m3 <br>Receptores<br>Proyecto (Tránsito de vehiculos)<br>Proyecto (Calefacción viviendas)|
|ISO-CONCENTRACIÓN DEL PROMEDIO<br>ANUAL DE NO2.|**Proyección**:|**Proyección**:|
|ISO-CONCENTRACIÓN DEL PROMEDIO<br>ANUAL DE NO2.|WGS 84 UTM H18S|WGS 84 UTM H18S|

41

_Fuente: Elaboración propia._

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

|Figura 21. Iso-concentración del percentil 99 de promedios horarios de NO2.|Col2|Col3|
|---|---|---|
||||
|**Carta:**|**Escala:**|**Simbología **|
|ISO-CONCENTRACIÓN DEL PERCENTIL 99<br>DE PROMEDIOS HORARIOS DE NO2.|1:24.000|<br> <br> <br>5 μg/m3 <br>10 μg/m3 <br>15 μg/m3 <br>20 μg/m3 <br>25 μg/m3 <br>30 μg/m3 <br>Receptores<br>Proyecto (Tránsito de vehiculos)<br>Proyecto (Calefacción viviendas)|
|ISO-CONCENTRACIÓN DEL PERCENTIL 99<br>DE PROMEDIOS HORARIOS DE NO2.|**Proyección**:|**Proyección**:|
|ISO-CONCENTRACIÓN DEL PERCENTIL 99<br>DE PROMEDIOS HORARIOS DE NO2.|WGS 84 UTM H18S|WGS 84 UTM H18S|

42

_Fuente: Elaboración propia._

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

|Figura 22. Iso-concentración del percentil 99 de promedios 8 horas de CO.|Col2|Col3|
|---|---|---|
||||
|**Carta:**|**Escala:**|**Simbología **|
|ISO-CONCENTRACIÓN DEL PERCENTIL 99<br>DE PROMEDIOS 8 HORAS DE CO.|1:20.000|<br> <br> <br>200 μg/m3 <br>400 μg/m3 <br>600 μg/m3 <br>800 μg/m3 <br>1000 μg/m3 <br>Receptores<br>Proyecto (Tránsito de vehiculos)<br>Proyecto (Calefacción viviendas)|
|ISO-CONCENTRACIÓN DEL PERCENTIL 99<br>DE PROMEDIOS 8 HORAS DE CO.|**Proyección**:|**Proyección**:|
|ISO-CONCENTRACIÓN DEL PERCENTIL 99<br>DE PROMEDIOS 8 HORAS DE CO.|WGS 84 UTM H18S|WGS 84 UTM H18S|

43

_Fuente: Elaboración propia._

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

|Figura 23. Iso-concentración del percentil 99 de promedios horarios de CO.|Col2|Col3|
|---|---|---|
||||
|**Carta: **|**Escala:**|**Simbología **|
|ISO-CONCENTRACIÓN DEL PERCENTIL<br>99 DE PROMEDIOS HORARIOS DE CO.|1:20.000|<br> <br>200 μg/m3 <br>400 μg/m3 <br>600 μg/m3 <br>800 μg/m3 <br>1000 μg/m3 <br>Receptores<br>Proyecto (Tránsito de vehiculos)<br>Proyecto (Calefacción viviendas)|
|ISO-CONCENTRACIÓN DEL PERCENTIL<br>99 DE PROMEDIOS HORARIOS DE CO.|**Proyección**:|**Proyección**:|
|ISO-CONCENTRACIÓN DEL PERCENTIL<br>99 DE PROMEDIOS HORARIOS DE CO.|WGS 84 UTM H18S|WGS 84 UTM H18S|

_Fuente: Elaboración propia._

44

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

De las representaciones de isolineas presentadas anteriormente, se puede concluir que, de los
compuestos evaluados, el material particulado MP 10 y MP 2,5, presentan una mayor concentración
en su promedio anual al igual que en sus concentraciones diarias en la zona norte y este proxima
al proyecto, donde se ubican los receptores R5 y R8, lo que es coincidente con lo que se presenta
en la evaluación de la dispersión respecto a las normas de calidad de aire primaria para este
receptor. Por otro lado, se puede observar que efectivamente existe un rango de concentraciones
medio, que tiende hacia las zonas noroeste, lo cual se debe a la influencia de los vientos.
Respecto a lo anterior, para MP 10 y MP 2,5 Anual se puede ver que en dirección a R11 se presentan
concentraciones menores a los 0,3 μg/m [3] y 0,2 μg/m [3 ] respectivamente. Sin embargo, para los
receptores ubicados al oeste como R1 y R2, se presentan valores de concentración inferiores a
0,2 μg/m [3] . En el caso de CO, se puede observar una dispersión de manera homologa al material
particulado en los sectores aledaños al proyecto, de forma que no se demuestran grandes
concentraciones en las zonas cercanas al proyecto, por la ubicación sur, cercano a R6 se
presentan concentraciones horarias inferiores a 400 μg/m [3] . Lo anterior, también ocurre para NO 2
y SO 2, donde el valor de concentración anual en R6 es inferior a 0,1 μg/m [3 ] para NO 2, y en el caso
de SO 2 el valor de concentración anual en R6 es menor a 0,01 μg/m [3], por lo tanto, la dispersión
se mantiene en las cercanías de hasta 1,6 km del proyecto con concentraciones muy por debajo
de las normativas de calidad aplicable respectiva, no interfiriendo en la población próxima al
proyecto.

Finalmente, a continuación, se presenta una tabla de comparación de las máximas
concentraciones presentadas en los receptores seleccionados para cada uno de los compuestos
evaluados en los puntos de máxima concentración, los cuales se encuentran cercanos a la zona
de operación del proyecto Senderos de Tenglo, hacia R7.

**Tabla 10. Máxima concentración de dispersión de compuestos, comparados con normativa de**

**calidad de aire primaria.**

|Compue<br>sto|Prom<br>anual<br>MP<br>10|P98<br>diario<br>MP<br>10|Prom<br>anual<br>MP<br>2.5|p98<br>diario<br>MP<br>2.5|Prom<br>anual<br>SO<br>2|P99<br>diario<br>SO<br>2|P99<br>horario<br>SO<br>2|Prom<br>anual<br>NO<br>2|P99<br>horario<br>NO<br>2|P99 8<br>horas<br>CO|P99<br>horario<br>CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Máximo**<br>**(μg/m3N)**|0,161|0,849|0,136|0,709|0,006|0,029|0,195|0,089|2,924|111,65<br>5|200,34<br>8|
|**Norma**<br>**(μg/m3N)**|50|130|20|50|60|150|350|100|400|10000|30000|
|**% de la**<br>**norma**|0,321|0,653|0,678|1,419|0,010|0,020|0,056|0,089|0,731|1,117|0,668|

_Fuente: Elaboración propia._

De la Tabla 10, se puede concluir que las concentraciones generadas por el proyecto, se
encuentran muy por debajo de las concentraciones límites establecidas en la normativa de calidad
de aire primaria para los compuestos evaluados. Cabe destacar que el MP 2,5 percentil 98
promedio diario presenta el mayor porcentaje de concentración en comparación con la normativa
de calidad de aire primaria, y corresponde a un 1,42%, lo cual se considera no significativo.

45

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

**5.2.2.** **Evaluación discreta de los niveles de concentración**

Con respecto a los resultados obtenidos en los puntos discretos, a continuación, en la Tabla 11
se indican los valores de concentración de compuestos generados por las fuentes, como material
particulado respirable (MP 10 ), material particulado respirable fino (MP 2,5 ), dióxido de azufre (SO 2 ),
óxidos de nitrógeno (NO X ) y monóxido de carbono (CO), para la etapa de operación/construcción
fase 2 del Proyecto.

**Tabla 11. Concentración de compuestos en receptores discretos.**

|Pun<br>to|Coordenadas WGS 84<br>UTM 19S|Col3|Concentración (μg/m3)|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Pun**<br>**to**|**Este (m)**|**Norte (m)**|**Prom**<br>**anualM**<br>**P10 **|**P98**<br>**diario**<br>**MP10 **|**Prom**<br>**anualM**<br>**P2,5 **|**P98**<br>**diario**<br>**M2,5 **|**Prom**<br>**anual**<br>**SO2 **|**P99**<br>**diario**<br>**SO2 **|**P98,5**<br>**hora**<br>**SO2 **|**Prom**<br>**anual**<br>**NO2 **|**P99**<br>**hora**<br>**NO2 **|**P99 8**<br>**horas**<br>**CO**|**P99**<br>**hora**<br>**CO**|
|R1|665620|5404347|0,064|0,476|0,053|0,397|0,002|0,015|0,146|0,032|1,918|63,606|141,21|
|R2|665572|5404289|0,057|0,437|0,046|0,357|0,002|0,014|0,139|0,028|2,002|59,044|142,40|
|R3|665605|5404459|0,130|0,766|0,109|0,644|0,005|0,025|0,166|0,072|2,731|101,36|163,43|
|R4|665494|5404392|0,112|0,723|0,094|0,613|0,004|0,024|0,163|0,061|2,424|90,226|155,99|
|R5|666109|5405023|0,057|0,310|0,047|0,263|0,002|0,010|0,095|0,027|1,354|47,428|93,973|
|R6|665709|5403921|0,121|0,750|0,102|0,645|0,004|0,024|0,157|0,070|2,483|88,837|156,66|
|R7|665906|5403830|0,161|0,849|0,136|0,709|0,006|0,029|0,195|0,089|2,924|109,78|200,34|
|R8|665968|5404102|0,114|0,659|0,095|0,564|0,004|0,022|0,180|0,060|2,805|111,65|174,25|
|R9|665488|5404579|0,139|0,826|0,114|0,668|0,005|0,027|0,167|0,072|2,542|102,08|172,32|
|R10|665290|5404554|0,104|0,637|0,083|0,519|0,003|0,021|0,125|0,049|1,814|81,497|128,75|
|R11|665286|5405067|0,067|0,349|0,054|0,284|0,002|0,011|0,080|0,031|1,340|44,593|76,748|

_Fuente: Elaboración propia._

De acuerdo a los valores de concentración de los compuestos evaluados en cada uno de los
receptores considerados para la evaluación discreta de las concentraciones, las mayores
concentraciones se dan en el receptor R7 para la totalidad de los compuestos modelados, a
excepción de CO concentración Percentil 99 de promedio de 8 horas, donde es superado en R8.

**5.2.3.** **Evaluación de los niveles de concentración.**

Con el objetivo de evaluar los niveles de concentración de MP 10 y MP 2,5 generados por la
ejecución del proyecto, se comparará la magnitud de estos valores con la normativa primaria de
calidad ambiental respectiva.

A continuación, se presenta el porcentaje del mayor valor de percentil 98 obtenido para MP 10 y
MP 2,5 en la modelación con respecto al límite diario establecido por la norma primaria de calidad
ambiental respectiva.

Por otro lado, para los gases de combustión se realiza la comparación con las normativas de
calidad de aire primaria y secundaria en caso que corresponda.

46

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

**Tabla 12. Evaluación de niveles de concentración para MP** **10** **.**

|Compuesto|Promedio del periodo anual<br>(μg/m3)|Límite D.S. N°59/2022 MMA<br>(μg/m3)|
|---|---|---|
|MP10|0,161|50|
|**Porcentaje respecto a modelación (%)**|**Porcentaje respecto a modelación (%)**|**0,321**|
|**Compuesto**|**Percentil 98 diario (μg/m3) **|**Límite D.S. N°12/2022 MMA**<br>**(μg/m3) **|
|MP10|0,849|130|
|**Porcentaje respecto a modelación (%)**|**Porcentaje respecto a modelación (%)**|**0,653**|

_Fuente: Elaboración propia._

**Tabla 13. Evaluación de niveles de concentración para MP** **2,5** **.**

|Compuesto|Promedio del periodo<br>anual (μg/m3)|Promedio del periodo<br>EMRP Mirasol (μg/m3)|D.S. N°12/11 MMA<br>(μg/m3)|
|---|---|---|---|
|MP2,5|0,135|28,81|20|
|**Porcentaje respecto a modelación (%)**|**Porcentaje respecto a modelación (%)**|**0,471**|**0,678**|
|**Compuesto**|**Percentil 98 diario**<br>**(μg/m3) **|**Percentil 98 diario del**<br>**periodo EMRP Mirasol**<br>**(μg/m3) **|**D.S. N°12/11 MMA**<br>**(μg/m3)**|
|MP2,5|0,709|142,52|50|
|**Porcentaje respecto a modelación (%)**|**Porcentaje respecto a modelación (%)**|**0,498**|**1,419**|

_Fuente: Elaboración propia._

**Tabla 14. Evaluación de niveles de concentración para NO** **x** **.**

|Compuesto|Promedio del periodo anual (μg/m3)|D.S. N°114/02 MINSEGPRES (μg/m3)|
|---|---|---|
|NOx|0,089|100|
|**Porcentaje respecto a modelación (%)**|**Porcentaje respecto a modelación (%)**|**0,0089**|
|**Compuesto**|**Percentil 99 horario (μg/m3) **|**D.S. N°114/02 MINSEGPRES (μg/m3) **|
|NOx|2,924|400|
|**Porcentaje respecto a modelación (%)**|**Porcentaje respecto a modelación (%)**|**0,731**|

_Fuente: Elaboración propia._

47

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

**Tabla 15. Evaluación de niveles de concentración para SO** **2** **.**

|Contaminante|Promedio del periodo<br>anual (μg/m3)|D.S. N°104/18 MMA (μg/m3)|D.S. N°22/2010 MMA<br>(μg/m3)|
|---|---|---|---|
|SO2|0,006|60|60|
|**Porcentaje respecto a modelación (%)**|**Porcentaje respecto a modelación (%)**|**0,010**|**0,010**|
|**Compuesto**|**Percentil 99 Diario/ (μg/m3) **|**D.S. N°104/18 MMA (μg/m3) **|**D.S. N°22/2010 MMA**<br>**(μg/m3) **|
|SO2|0,029|150|260|
|**Porcentaje respecto a modelación (%)**|**Porcentaje respecto a modelación (%)**|**0,020**|**0,012**|
|**Compuesto**|**Percentil 99 Horario**<br>**(μg/m3) **|**D.S. N°104/18 MMA (μg/m3) **|**D.S. N°22/2010 MMA**<br>**(μg/m3) **|
|SO2|0,195|350|700|
|**Porcentaje respecto a modelación (%)**|**Porcentaje respecto a modelación (%)**|**0,056**|**0,028**|

_Fuente: Elaboración propia._

**Tabla 16. Evaluación de niveles de concentración para CO.**

|Compuesto|Percentil 99 8 horas (μg/m3)|D.S. N°115/02 MINSEGPRES (μg/m3)|
|---|---|---|
|CO|111,65|10.000|
|**Porcentaje respecto a modelación (%)**|**Porcentaje respecto a modelación (%)**|**1,117**|
|**Compuesto**|**Percentil 99 Horario (μg/m3) **|**D.S. N°115/02 MINSEGPRES (μg/m3) **|
|CO|200,34|30.000|
|**Porcentaje respecto a modelación (%)**|**Porcentaje respecto a modelación (%)**|**0,668**|

_De Fuente: Elaboración propia._

De acuerdo a las tablas anteriores, respecto de las normas de calidad primaria y secundarias
aplicables al proyecto, se puede indicar que el punto de máximo impacto que corresponde a las
áreas cercanas a R7, presentan aportes poco significativos de concentraciones de material
particulado y gases de combustión generados por el proyecto, en el área de estudio. Lo anterior
debido a que en su mayoría los porcentajes de cumplimiento respecto a la normativa o a la
situación de calidad de aire de la zona, no superan el 0,7% en concentraciones anuales. En el
caso de MP 10, se presenta un % de concentración respecto de la normativa de calidad de aire
primaria correspondiente a 0,321% respecto de la concentración promedio anual de MP 10, y del
0,653% respecto de la concentración percentil 99 diario. Por otro lado, para MP 2,5, se presenta un
0,678% de la concentración promedio anual de MP 2,5 respecto de la normativa de calidad de airea
primaria, y un 1,419% de la concentración percentil 99 diario. En el caso de los gases de
combustión, el elemento que presenta mayor % de concentración respecto a la normativa de
calidad de aire primaria corresponde a CO, en su concentración de 8 horas, el cual representa
un 1,117% de lo establecido en la normativa de calidad de aire, por otro lado, para CO y NOx, el

48

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

porcentaje de comparación con la normativa de calidad de aire primaria, representando entre un
0,731% a un 0,0089% de la concentración modelada.

Dado que la concentración obtenida con la modelación de la emisión generada por la fase de
operación del proyecto representa un bajo porcentaje en comparación con la normativa primaria
y secundaria de calidad ambiental, se puede concluir que no se generará un impacto significativo
sobre la calidad del aire de la comuna de Puerto Montt, ubicada en la Provincia de Llanquihue.

49

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

**5.3.** **Área de influencia**

De acuerdo a los resultados obtenidos de la modelación de la dispersión de las emisiones, se
definió el área de influencia del proyecto como el alcance del Percentil 98 diario de MP 2,5, ya que
se considera el compuesto con mayores concentraciones aportadas al área en evaluación
considerando la zona como saturada por este mismo compuesto, se considera como límite del
área de influencia la isolinea de valor 1 μg/m [3], la cual representa el 2 % de la normativa de calidad
de aire primaria de MP 2,5.

Finalmente, en la figura a continuación se presenta el área de influencia del proyecto para el
componente aire respecto a las emisiones atmosféricas generadas por él en su etapa de
operación.

**Figura 24. Área de influencia del proyecto, componente aire (emisiones atmosféricas).**

|Col1|Carta:|Col3|
|---|---|---|
||AREA DE<br>INFLUENCIA|AREA DE<br>INFLUENCIA|
||**Escala:**|**Escala:**|
||1:24.000|1:24.000|
||**Proyección:**|**Proyección:**|
||WGS 84 UTM H18S|WGS 84 UTM H18S|
||**Simbología**|**Simbología**|
||<br>|Proyecto (Calefacción<br>viviendas)<br>Proyecto (Tránsito de<br>vehiculos)<br>Área de Influencia<br>Receptores|

_Fuente: Elaboración propia._

50

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

**5.4.** **Consideraciones.**

La base de datos meteorológica y geográfica fue adquirida a una empresa especializada en
modelación para servicios de evaluación ambiental, la cual fue generada por medio del software
WRF, cumpliendo con las condiciones establecidas por el Servicio de Evaluación Ambiental.

51

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

**6.** **CONCLUSIÓN**

La ejecución del proyecto “Senderos de Tenglo” provoca una cantidad poco significativa de
material particulado fino respirable, principalmente debido a la calefacción domiciliaria de las
viviendas en etapa de operación del proyecto y del tránsito de vehículos en vías pavimentadas.

Para evaluar el impacto generado por la emisión de material particulado (MP 10 y MP 2,5 ) sobre la
calidad del aire de la comuna de Puerto Montt, y por tanto sobre la salud de las personas, se
realizó una modelación de dispersión atmosférica a través del software CALPUFF. La modelación
contempló un dominio de 74x74 km, que incluyó toda la información meteorológica proporcionada
por la base de datos construida a partir de modelación WRF.

A partir de la modelación de dispersión atmosférica del material particulado MP 10 y MP 2,5 y gases
de combustión (SO 2, NO 2 y CO) generado por la operación del proyecto se concluye que las
concentraciones generadas por este son de magnitudes bajo las normativas de calidad primaria
para los distintivos contenientes y de bajo alcance con respecto al área de alcance.

El percentil 98 de los promedios diarios para MP 10 presenta valores de 1,0 μg/m [3] hasta un radio
de aproximadamente 1,9 km con respecto a la zona de operación del proyecto en su zona más
distante y de 0,65 km de las rutas pavimentadas que serán utilizadas durante la misma etapa. Los
mayores valores de concentración se presentan en el sector sur del emplazamiento del proyecto
y este de las rutas pavimentadas, alcanzando sobre los 6,0 μg/m [3] . Por otro lado, de acuerdo a lo
observado en la Figura 16 para MP 2,5, el percentil 98 de los promedios diarios también es de
magnitud menor al límite de la norma de calidad primaria, presentando valores de 1,0 μg/m [3] hasta
un radio de 1,95 km aproximadamente con respecto a la zona de construcción. Los mayores
valores de concentración se presentan al sureste del proyecto, bajo las rutas pavimentadas
afectadas por el tránsito de vehículos durante la etapa de/operación, alcanzando sobre los 5
μg/m [3] .

Adicionalmente, se realizó una evaluación de concentración en 11 receptores discretos, que
corresponden a edificaciones, principalmente con destino residencial, cercanas al área de
emplazamiento del proyecto. De acuerdo a los valores del percentil 98 de MP 10 y MP 2,5 asociados
a cada uno de los receptores considerados para la evaluación discreta de las concentraciones,
ninguno presentó valores sobre una unidad para MP 2,5 . Para las concentraciones de MP 10, todos
los receptores se encuentran bajo los 0,85 μg/m [3], mientras que para las concentraciones de MP 2,5
todos se encuentran bajo los 0,71 μg/m [3] (el mayor valor se presenta en R7 para MP 10 y para
MP 2,5 ). Dado que los valores sobre los receptores son de baja magnitud en relación a la norma de
calidad primaria aplicable según sea el caso, se puede inferir que las concentraciones de material
particulado (MP 10 y MP 2,5 ) no generarán un impacto significativo sobre la salud de las personas ni
sobre los recursos naturales, de la comuna de Puerto Montt o comunas cercanas.

Por otra parte, con respecto a los gases de combustión (SO 2, NO 2 y CO), los primeros presentan
menores concentraciones en relación a las de material particulado al ser comparadas con su

52

Ulmo Consultores S.A.
Proyecto Inmobiliario “Senderos de Tenglo”.

Informe de Modelación Atmosférica

normativa de calidad aplicable, siendo la concentración de CO percentil 99,8 cada 8 horas quien
presenta mayor presencia, llegando a alcanzar una concentración promedio de 8 horas (percentil
99) de 111,65 μg/m [3], lo que significa un valor equivalente al 1,117 % de la normativa aplicable
para este compuesto (D.S N° 115/02 MINSEGPRES).

53

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Normas de Calidad del Aire Consideradas en el Estudio.****

| Parámetro | Tipo de Norma | Estadístico | Valor de referencia | Fuente |
| --- | --- | --- | --- | --- |
| MP10 | Primaria | Promedio<br>del<br>periodo | 50 μg/m3N | D.S. N°12/22 MMA |
| MP10 | Primaria | Percentil 98 Diario | 130 μg/m3N | D.S. N°12/22 MMA |
| MP2,5 | Primaria | Promedio<br>del<br>periodo | 20 μg/m3N | D.S. N°12/11 MMA |
| MP2,5 | Primaria | Percentil 98 Diario | 50 μg/m3N | D.S. N°12/11 MMA |
| SO2 | Primaria | Promedio<br>del<br>periodo | 60 μg/m3N | D.S. N°104/18 MMA |
| SO2 | Primaria | Percentil 99 Diario | 150 μg/m3N | D.S. N°104/18 MMA |
| SO2 | Primaria | Percentil 99 Horario | 350 μg/m3N | D.S. N°104/18 MMA |
| NO2 | Primaria | Promedio<br>del<br>periodo | 100 μg/m3N | D.S. N°114/02 MINSEGPRES |
| NO2 | Primaria | Percentil 99 Horario | 400 μg/m3N | D.S. N°114/02 MINSEGPRES |
| CO | Primaria | Percentil 99 8 horas | 1.000 μg/m3N | D.S. N°115/02 MINSEGPRES |
| CO | Primaria | Percentil 99 Horario | 3.000 μg/m3N | D.S. N°115/02 MINSEGPRES |
| SO2 | Secundaria | Promedio<br>del<br>periodo | 60 μg/m3N | D.S. N°22/10 MMA |
| SO2 | Secundaria | Percentil 99,7 Diario | 260 μg/m3N | D.S. N°22/10 MMA |
| SO2 | Secundaria | Percentil<br>99,73<br>Horario | 700 μg/m3N | D.S. N°22/10 MMA |

**Tabla 2.: Información general de la EMRP “Mirasol”.****

| Estación | Mirasol |
| --- | --- |
| Propietario | Ministerio del Medio Ambiente |
| Operador | Algoritmos y Mediciones Ambientales SpA |
| Región | del Los Lagos |
| Provincia | Llanquihue |
| Comuna | Puerto Montt |
| Coordenadas UTM 19S | 669585 E |
| Coordenadas UTM 19S | 5406017 N |
| Recepción de datos | En línea |
| Inicio de operación | 06-04-2013 |
| Estado | Vigente |

**Tabla 3.: Precipitación y temperatura normal mensual, Puerto Montt, estación “Puerto Montt-****

| Mes | Precipitación (mm) | Temperatura (°C) |
| --- | --- | --- |
| ENE | 2,81 | 15,59 |
| FEB | 2,98 | 16,19 |
| MAR | 3,63 | 12,21 |
| ABR | 5,28 | 10,22 |
| MAY | 6,77 | 11,12 |
| JUN | 8,86 | 9,90 |
| JUL | 7,09 | 9,57 |
| AGO | 6,76 | 10,15 |
| SEP | 4,24 | 10,73 |
| OCT | 4,43 | 9,85 |
| NOV | 3,87 | 13,38 |
| DIC | 3,34 | 14,95 |

**Tabla 4.: Áreas de emisión, fase de operación del proyecto.****

| Áreas de emisión | Emisión (t/año) | Col3 | Col4 | Col5 | Col6 |
| --- | --- | --- | --- | --- | --- |
| **Áreas de emisión** | **MP10** | **MP2,5** | **NOx** | **SO2 ** | **CO** |
| Área Operación<br>(calefacción viviendas) | 5,7461 | 5,2864 | 4,3670 | 0,2298 | 206,85 |
| Rutas Pavimentadas<br>Operación (vehículos<br>particulares) | 0,4828 | 0,1181 | 0,0725 | 0,0024 | 0,7368 |

**Tabla 5.: Coordenadas de vértices y centroide del dominio de Modelación WRF.****

| Vértice | Proyección UTM, Huso 18 Sur; Datum WGS-84 | Col3 |
| --- | --- | --- |
| **Vértice** | **Este (m)** | **Norte (m)** |
| Noroeste | 629821 | 5440620 |
| Noreste | 702846 | 5440753 |
| Suroeste | 629463 | 5366934 |
| Sureste | 702621 | 5367727 |
| Centroide | 665773 | 5404386 |
| Proyecto | 665732 | 5404448 |

**Tabla 6.: Coordenadas de vértices y centroide del dominio de Modelación CALPUFF.****

| Vértice | Proyección UTM, Huso 18 Sur; Datum WGS-84 | Col3 |
| --- | --- | --- |
| **Vértice** | **Este (m)** | **Norte (m)** |
| Noroeste | 629821 | 5440620 |
| Noreste | 702846 | 5440753 |
| Suroeste | 629463 | 5366934 |
| Sureste | 702621 | 5367727 |
| Centroide | 665773 | 5404386 |
| Proyecto | 665732 | 5404448 |

**Tabla 7.: Coordenadas de receptores discretos.****

| Receptor | Punto | Coordenadas WGS 84 UTM 18S | Col4 | Distancia respecto<br>al proyecto (m) |
| --- | --- | --- | --- | --- |
| **Receptor** | **Punto** | **Este (m)** | **Norte (m)** | **Norte (m)** |
| Conjunto de viviendas | R1 | 665620 | 5404347 | 43,85 |
| Conjunto de viviendas | R2 | 665572 | 5404289 | 27,50 |
| Conjunto de viviendas | R3 | 665605 | 5404459 | 35,37 |
| Conjunto de viviendas | R4 | 665494 | 5404392 | 157,11 |
| Conjunto de viviendas | R5 | 666109 | 5405023 | 523,38 |
| Conjunto de viviendas | R6 | 665709 | 5403921 | 133,42 |
| Conjunto de viviendas | R7 | 665906 | 5403830 | 298,31 |
| Establecimiento Privado | R8 | 665968 | 5404102 | 128,57 |
| Conjunto de viviendas | R9 | 665488 | 5404579 | 138,08 |
| Conjunto de viviendas | R10 | 665290 | 5404554 | 326,39 |
| Conjunto de viviendas | R11 | 665286 | 5405067 | 610,81 |

**Tabla 8.: Coordenadas fuente puntual y polígonos de fuente de área.****

| Área de emisión | Vértice | Proyección UTM, Huso 18 Sur; Datum WGS-84 | Col4 |
| --- | --- | --- | --- |
| **Área de emisión** | **Vértice** | **Este (m)** | **Norte (m)** |
| Polígono Operación<br>(Viviendas zona Norte) | 1 | 665809,2 | 5404414,9 |
| Polígono Operación<br>(Viviendas zona Norte) | 2 | 665668,6 | 5404333,1 |
| Polígono Operación<br>(Viviendas zona Norte) | 3 | 665622,0 | 5404561,2 |
| Polígono Operación<br>(Viviendas zona Norte) | 4 | 665799,3 | 5404601,7 |
| Polígono Operación<br>(Viviendas zona Sur) | 1 | 665526,7 | 5404227,5 |
| Polígono Operación<br>(Viviendas zona Sur) | 2 | 665811,5 | 5404400,9 |
| Polígono Operación<br>(Viviendas zona Sur) | 3 | 665854,1 | 5404151,2 |
| Polígono Operación<br>(Viviendas zona Sur) | 4 | 665700,4 | 5404059,1 |
| Ruta Pavimentada 1 | 1 | 665668,8 | 5404329,2 |
| Ruta Pavimentada 1 | 2 | 665806,7 | 5404408,9 |
| Ruta Pavimentada 1 | 3 | 665808,4 | 5404403,7 |
| Ruta Pavimentada 1 | 4 | 665672,4 | 5404324,2 |
| Ruta Pavimentada 2 | 1 | 665504,6 | 5404232,1 |
| Ruta Pavimentada 2 | 2 | 665668,2 | 5404328,9 |
| Ruta Pavimentada 2 | 3 | 665670,8 | 5404323,6 |
| Ruta Pavimentada 2 | 4 | 665507,9 | 5404229,1 |
| Ruta Pavimentada 3 | 1 | 665330,3 | 5404390,0 |
| Ruta Pavimentada 3 | 2 | 665507,1 | 5404229,3 |
| Ruta Pavimentada 3 | 3 | 665502,4 | 5404225,0 |
| Ruta Pavimentada 3 | 4 | 665327,1 | 5404385,4 |
| Ruta Pavimentada 4 | 1 | 665330,6 | 5404390,6 |
| Ruta Pavimentada 4 | 2 | 665339,2 | 5404405,9 |
| Ruta Pavimentada 4 | 3 | 665343,3 | 5404403,7 |
| Ruta Pavimentada 4 | 4 | 665334,3 | 5404387,3 |
| Ruta Pavimentada 5 | 1 | 665339,6 | 5404406,6 |
| Ruta Pavimentada 5 | 2 | 665324,2 | 5404478,3 |
| Ruta Pavimentada 5 | 3 | 665329,4 | 5404478,0 |
| Ruta Pavimentada 5 | 4 | 665343,2 | 5404404,4 |
| Ruta Pavimentada 6 | 1 | 665324,5 | 5404478,7 |
| Ruta Pavimentada 6 | 2 | 665347,6 | 5404506,5 |
| Ruta Pavimentada 6 | 3 | 665353,2 | 5404505,3 |
| Ruta Pavimentada 6 | 4 | 665329,6 | 5404478,2 |
| Ruta Pavimentada 7 | 1 | 665347,6 | 5404507,3 |
| Ruta Pavimentada 7 | 2 | 665325,3 | 5404608,1 |
| Ruta Pavimentada 7 | 3 | 665330,4 | 5404610,6 |
| Ruta Pavimentada 7 | 4 | 665352,9 | 5404506,5 |
| Ruta Pavimentada 8 | 1 | 665324,8 | 5404608,5 |
| Ruta Pavimentada 8 | 2 | 665286,5 | 5404727,4 |
| Ruta Pavimentada 8 | 3 | 665290,6 | 5404730,9 |
| Ruta Pavimentada 8 | 4 | 665329,4 | 5404611,4 |
| Ruta Pavimentada 9 | 1 | 665286,0 | 5404727,6 |
| Ruta Pavimentada 9 | 2 | 665004,7 | 5405088,7 |

**Tabla 9.: Tasa de emisión.****

| Área de emisión | Tipo de<br>fuente | Superficie<br>polígono<br>(m2) | Tasa de emisión (Ton/año-m2) | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Área de emisión** | **Tipo de**<br>**fuente** | **Superficie**<br>**polígono**<br>**(m2) ** | **MP10 ** | **MP2,5 ** | **NOx** | **SO2 ** | **CO** |
| Área Operación<br>(Calefacción<br>viviendas) | Área | 94.782 | 6,06E-05 | 5,58E-05 | 4,61E-05 | 2,42E-06 | 2,18E-03 |
| Área Operación<br>(Tránsito de<br>vehículos) | Área | 8.212 | 5,88E-05 | 1,44E-05 | 8,83E-06 | 2,89E-07 | 8,97E-05 |

**Tabla 10.: Máxima concentración de dispersión de compuestos, comparados con normativa de****

| Compue<br>sto | Prom<br>anual<br>MP<br>10 | P98<br>diario<br>MP<br>10 | Prom<br>anual<br>MP<br>2.5 | p98<br>diario<br>MP<br>2.5 | Prom<br>anual<br>SO<br>2 | P99<br>diario<br>SO<br>2 | P99<br>horario<br>SO<br>2 | Prom<br>anual<br>NO<br>2 | P99<br>horario<br>NO<br>2 | P99 8<br>horas<br>CO | P99<br>horario<br>CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Máximo**<br>**(μg/m3N)** | 0,161 | 0,849 | 0,136 | 0,709 | 0,006 | 0,029 | 0,195 | 0,089 | 2,924 | 111,65<br>5 | 200,34<br>8 |
| **Norma**<br>**(μg/m3N)** | 50 | 130 | 20 | 50 | 60 | 150 | 350 | 100 | 400 | 10000 | 30000 |
| **% de la**<br>**norma** | 0,321 | 0,653 | 0,678 | 1,419 | 0,010 | 0,020 | 0,056 | 0,089 | 0,731 | 1,117 | 0,668 |

**Tabla 11.: Concentración de compuestos en receptores discretos.****

| Pun<br>to | Coordenadas WGS 84<br>UTM 19S | Col3 | Concentración (μg/m3) | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 | Col14 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Pun**<br>**to** | **Este (m)** | **Norte (m)** | **Prom**<br>**anualM**<br>**P10 ** | **P98**<br>**diario**<br>**MP10 ** | **Prom**<br>**anualM**<br>**P2,5 ** | **P98**<br>**diario**<br>**M2,5 ** | **Prom**<br>**anual**<br>**SO2 ** | **P99**<br>**diario**<br>**SO2 ** | **P98,5**<br>**hora**<br>**SO2 ** | **Prom**<br>**anual**<br>**NO2 ** | **P99**<br>**hora**<br>**NO2 ** | **P99 8**<br>**horas**<br>**CO** | **P99**<br>**hora**<br>**CO** |
| R1 | 665620 | 5404347 | 0,064 | 0,476 | 0,053 | 0,397 | 0,002 | 0,015 | 0,146 | 0,032 | 1,918 | 63,606 | 141,21 |
| R2 | 665572 | 5404289 | 0,057 | 0,437 | 0,046 | 0,357 | 0,002 | 0,014 | 0,139 | 0,028 | 2,002 | 59,044 | 142,40 |
| R3 | 665605 | 5404459 | 0,130 | 0,766 | 0,109 | 0,644 | 0,005 | 0,025 | 0,166 | 0,072 | 2,731 | 101,36 | 163,43 |
| R4 | 665494 | 5404392 | 0,112 | 0,723 | 0,094 | 0,613 | 0,004 | 0,024 | 0,163 | 0,061 | 2,424 | 90,226 | 155,99 |
| R5 | 666109 | 5405023 | 0,057 | 0,310 | 0,047 | 0,263 | 0,002 | 0,010 | 0,095 | 0,027 | 1,354 | 47,428 | 93,973 |
| R6 | 665709 | 5403921 | 0,121 | 0,750 | 0,102 | 0,645 | 0,004 | 0,024 | 0,157 | 0,070 | 2,483 | 88,837 | 156,66 |
| R7 | 665906 | 5403830 | 0,161 | 0,849 | 0,136 | 0,709 | 0,006 | 0,029 | 0,195 | 0,089 | 2,924 | 109,78 | 200,34 |
| R8 | 665968 | 5404102 | 0,114 | 0,659 | 0,095 | 0,564 | 0,004 | 0,022 | 0,180 | 0,060 | 2,805 | 111,65 | 174,25 |
| R9 | 665488 | 5404579 | 0,139 | 0,826 | 0,114 | 0,668 | 0,005 | 0,027 | 0,167 | 0,072 | 2,542 | 102,08 | 172,32 |
| R10 | 665290 | 5404554 | 0,104 | 0,637 | 0,083 | 0,519 | 0,003 | 0,021 | 0,125 | 0,049 | 1,814 | 81,497 | 128,75 |
| R11 | 665286 | 5405067 | 0,067 | 0,349 | 0,054 | 0,284 | 0,002 | 0,011 | 0,080 | 0,031 | 1,340 | 44,593 | 76,748 |

**Tabla 12.: Evaluación de niveles de concentración para MP** **10** **.****

| Compuesto | Promedio del periodo anual<br>(μg/m3) | Límite D.S. N°59/2022 MMA<br>(μg/m3) |
| --- | --- | --- |
| MP10 | 0,161 | 50 |
| **Porcentaje respecto a modelación (%)** | **Porcentaje respecto a modelación (%)** | **0,321** |
| **Compuesto** | **Percentil 98 diario (μg/m3) ** | **Límite D.S. N°12/2022 MMA**<br>**(μg/m3) ** |
| MP10 | 0,849 | 130 |
| **Porcentaje respecto a modelación (%)** | **Porcentaje respecto a modelación (%)** | **0,653** |

**Tabla 13.: Evaluación de niveles de concentración para MP** **2,5** **.****

| Compuesto | Promedio del periodo<br>anual (μg/m3) | Promedio del periodo<br>EMRP Mirasol (μg/m3) | D.S. N°12/11 MMA<br>(μg/m3) |
| --- | --- | --- | --- |
| MP2,5 | 0,135 | 28,81 | 20 |
| **Porcentaje respecto a modelación (%)** | **Porcentaje respecto a modelación (%)** | **0,471** | **0,678** |
| **Compuesto** | **Percentil 98 diario**<br>**(μg/m3) ** | **Percentil 98 diario del**<br>**periodo EMRP Mirasol**<br>**(μg/m3) ** | **D.S. N°12/11 MMA**<br>**(μg/m3)** |
| MP2,5 | 0,709 | 142,52 | 50 |
| **Porcentaje respecto a modelación (%)** | **Porcentaje respecto a modelación (%)** | **0,498** | **1,419** |

**Tabla 14.: Evaluación de niveles de concentración para NO** **x** **.****

| Compuesto | Promedio del periodo anual (μg/m3) | D.S. N°114/02 MINSEGPRES (μg/m3) |
| --- | --- | --- |
| NOx | 0,089 | 100 |
| **Porcentaje respecto a modelación (%)** | **Porcentaje respecto a modelación (%)** | **0,0089** |
| **Compuesto** | **Percentil 99 horario (μg/m3) ** | **D.S. N°114/02 MINSEGPRES (μg/m3) ** |
| NOx | 2,924 | 400 |
| **Porcentaje respecto a modelación (%)** | **Porcentaje respecto a modelación (%)** | **0,731** |

**Tabla 15.: Evaluación de niveles de concentración para SO** **2** **.****

| Contaminante | Promedio del periodo<br>anual (μg/m3) | D.S. N°104/18 MMA (μg/m3) | D.S. N°22/2010 MMA<br>(μg/m3) |
| --- | --- | --- | --- |
| SO2 | 0,006 | 60 | 60 |
| **Porcentaje respecto a modelación (%)** | **Porcentaje respecto a modelación (%)** | **0,010** | **0,010** |
| **Compuesto** | **Percentil 99 Diario/ (μg/m3) ** | **D.S. N°104/18 MMA (μg/m3) ** | **D.S. N°22/2010 MMA**<br>**(μg/m3) ** |
| SO2 | 0,029 | 150 | 260 |
| **Porcentaje respecto a modelación (%)** | **Porcentaje respecto a modelación (%)** | **0,020** | **0,012** |
| **Compuesto** | **Percentil 99 Horario**<br>**(μg/m3) ** | **D.S. N°104/18 MMA (μg/m3) ** | **D.S. N°22/2010 MMA**<br>**(μg/m3) ** |
| SO2 | 0,195 | 350 | 700 |
| **Porcentaje respecto a modelación (%)** | **Porcentaje respecto a modelación (%)** | **0,056** | **0,028** |

**Tabla 16.: Evaluación de niveles de concentración para CO.****

| Compuesto | Percentil 99 8 horas (μg/m3) | D.S. N°115/02 MINSEGPRES (μg/m3) |
| --- | --- | --- |
| CO | 111,65 | 10.000 |
| **Porcentaje respecto a modelación (%)** | **Porcentaje respecto a modelación (%)** | **1,117** |
| **Compuesto** | **Percentil 99 Horario (μg/m3) ** | **D.S. N°115/02 MINSEGPRES (μg/m3) ** |
| CO | 200,34 | 30.000 |
| **Porcentaje respecto a modelación (%)** | **Porcentaje respecto a modelación (%)** | **0,668** |
