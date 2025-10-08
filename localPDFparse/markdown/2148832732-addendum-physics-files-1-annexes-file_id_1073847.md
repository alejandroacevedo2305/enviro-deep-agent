---
title: Sin título
author: Katherine Núñez
date: D:20210630165634-04'00'
language: es
type: report
pages: 45
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ADENDA N°1 “PROYECTO MODIFICACIÓN BARRIO LOS PINARES” ANEXO 7.2: INFORME DE MODELACIÓN ATMOSFÉRICA
-->

# ADENDA N°1 “PROYECTO MODIFICACIÓN BARRIO LOS PINARES” ANEXO 7.2: INFORME DE MODELACIÓN ATMOSFÉRICA

## Elaborado para:

JUNIO 2021

Adenda N°1

Proyecto Modificación Barrio Los Pinares

Informe de Modelación Atmosférica

**INDICE DE CONTENIDO**

1. INTRODUCCIÓN .................................................................................................... 5

1.1. Objetivos ........................................................................................................... 7

2. ANTECEDENTES ..................................................................................................... 8

2.1. Antecedentes de la Calidad del Aire en la comuna de Rancagua. ......................... 9

2.1.1. Material Particulado Respirable (MP 10 ). ........................................................ 11

2.1.2. Material Particulado Respirable (MP 2,5 ). ....................................................... 13

2.1.3. Dióxido de nitrógeno (NO2). ........................................................................ 15

2.1.4. Monóxido de Carbono (CO). ......................................................................... 17

2.1.5. Dióxido de Azufre (SO 2 ). ............................................................................... 18

2.2. Antecedentes Meteorológicos ......................................................................... 21

2.2.1. Vientos ........................................................................................................ 21

2.2.2. Temperatura y Precipitación ........................................................................ 22

3. JUSTIFICACIÓN DE LOS MODELOS UTILIZADOS EN LA MODELACIÓN ..................... 24

3.1. Uso del Modelo CALPUFF. ................................................................................ 24

3.2. Uso del Modelo Weather Research and Forecasting Model (WRF). ................... 25

4. METODOLOGÍA ................................................................................................... 26

4.1. Dominio Modelación Meteorológica ................................................................ 26

4.2. Dominio de Modelación CALPUFF .................................................................... 28

4.3. Post procesamiento de información ................................................................. 30

4.4. Escenario de modelación ................................................................................. 32

5. RESULTADOS ....................................................................................................... 35

5.1. Caracterización geofísicas ................................................................................ 35

5.1.1. Topografía ................................................................................................... 35

5.2. Concentraciones .............................................................................................. 36

5.2.1. Concentración de compuestos dentro del área de estudio. ........................... 36

5.2.2. Evaluación discreta y dispersión de los niveles de concentración .................. 38

2

Adenda N°1

Proyecto Modificación Barrio Los Pinares

Informe de Modelación Atmosférica

5.3. Área de influencia ............................................................................................ 41

5.4. Consideraciones. ............................................................................................. 43

6. CONCLUSIÓN ...................................................................................................... 44

**INDICE DE TABLAS**

Tabla 1. Normas de Calidad del Aire Consideradas en el Estudio. ...................................... 8

Tabla 2. Información general de la EMRP “Rancagua I”. .................................................. 10

Tabla 3. Concentración Media Anual de MP 10 (μg/m [3] N) .................................................. 12

Tabla 4. Concentraciones 24 horas de MP 10 (μg/m [3] N). .................................................... 13

Tabla 5. Concentración Media Anual de MP 2,5 (μg/m [3] N). ................................................ 14

Tabla 6. Concentraciones 24 horas de MP 2,5 (μg/m [3] N). ................................................... 15

Tabla 7. Concentración Media Anual de NO 2 (μg/m [3] N). .................................................. 16

Tabla 8. Concentraciones Percentil 99 Promedio Horario de NO 2 (μg/m [3] N). .................... 17

Tabla 9. Concentración Percentil 99 Horario de CO (μg/m [3] N). ......................................... 18

Tabla 10. Concentración Percentil 99 Promedio 8 Horas de CO (μg/m [3] N). ....................... 18

Tabla 11. Concentración Media Anual de SO 2 (μg/m [3] N). ................................................. 20

Tabla 12. Concentración Percentil 99 Promedio Diario de SO 2 (μg/m [3] N). ........................ 20

Tabla 13. Concentración Percentil 98,5 1 Hora de SO 2 (μg/m [3] N). .................................... 20

Tabla 14. Precipitación y temperatura normal mensual, comuna de Rancagua. ............... 23

Tabla 15. Coordenadas de vértices y centroide del dominio de Modelación WRF. ........... 27

Tabla 16. Coordenadas de vértices y centroide del dominio de Modelación CALPUFF. ..... 29

Tabla 17. Coordenadas de receptores discretos. ............................................................. 31

Tabla 18. Tasa de emisión. ............................................................................................. 32

Tabla 19. Coordenadas polígono de fuente de área. ....................................................... 34

Tabla 20. Evaluación de niveles de concentración para MP 10 . ......................................... 36

Tabla 21. Evaluación de niveles de concentración para MP 2,5 . ......................................... 36

Tabla 22. Evaluación de niveles de concentración para NO 2 . ........................................... 37

3

Adenda N°1

Proyecto Modificación Barrio Los Pinares

Informe de Modelación Atmosférica

Tabla 23. Evaluación de niveles de concentración para SO 2 . ............................................ 37

Tabla 24. Evaluación de niveles de concentración para CO. ............................................. 37

Tabla 25. Concentración de MP 2,5 en receptores discretos. ............................................. 40

**INDICE DE FIGURAS**

Figura 1. Ubicación de EMRP “Rancagua I”. ...................................................................... 9

Figura 2. Concentración promedio de 24 horas MP 10 . ..................................................... 11

Figura 3. Concentración promedio anual de MP 10 . ......................................................... 12

Figura 4. Concentración promedio de 24 horas MP 2,5 . .................................................... 13

Figura 5. Concentración promedio anual de MP 2,5 . ........................................................ 14

Figura 6. Serie de Tiempo Concentraciones horarias de NO 2. .......................................... 15

Figura 7. Serie de Tiempo Concentraciones anuales de NO 2 ............................................ 16

Figura 8. Serie de Tiempo Concentraciones de CO Estación Rancagua I. .......................... 17

Figura 9. Serie de Tiempo Concentraciones de SO2 Estación Rancagua I.......................... 19

Figura 10. Rosas de dirección de viento por estación del año. ......................................... 22

Figura 11. Precipitación y temperaturas, comuna de Rancagua. ...................................... 23

Figura 12. Dominio modelación WRF.............................................................................. 27

Figura 13. Dominio de la Modelación de CALPUFF. ......................................................... 28

Figura 14. Ubicación receptores. .................................................................................... 31

Figura 15. Fuente de área. ............................................................................................. 33

Figura 16. Elevación de terreno del área de estudio........................................................ 35

Figura 17. Iso-concentración de promedio anual de MP2,5 sobre puntos discretos y área de

estudio. ......................................................................................................................... 39

Figura 18. Área de influencia del proyecto, componente aire (emisiones atmosféricas) ... 42

4

Adenda N°1

Proyecto Modificación Barrio Los Pinares

Informe de Modelación Atmosférica

**1.** **INTRODUCCIÓN**

El Proyecto “Modificación Barrio Los Pinares” corresponde a la modificación de un proyecto

con RCA de tipo inmobiliario, ubicado en el sector noroeste de la ciudad de Rancagua,

Región del Libertador Bernardo O’Higgins.

El proyecto “Barrio Los Pinares”, el cual cuenta con la RCA N°7/2019, constituye una

modificación de proyecto existente, el cual se ejecutó en el lote 3A, de una superficie
69.171,36 m [2] (6,91 ha) y consistió en 264 viviendas de integración social, además de

estacionamientos, áreas verdes y equipamiento. El proyecto “Barrio Los Pinares” consiste

en la ampliación del mencionado proyecto existente con la construcción de 366 viviendas

adicionales que se emplazarán el los Lotes 4-1B, Lote 3B y Lote Sucesión Escobar Espíndola,

en una superficie total de 95.275,94 m1 (9,52 ha).

El presente Proyecto “Modificación Barrio Los Pinares” que se somete a evaluación

ambiental, consiste en la ampliación del referido proyecto inmobiliario mediante la

construcción de 785 viviendas adicionales que se emplazarán en el Lote LT-2, en una
superficie total de 239.887,81 m [2] (23,99 hectáreas), con sus correspondientes

estacionamientos, áreas verdes y equipamiento.

El proyecto se emplaza en una zona declarada saturada por material particulado respirable

MP 10, de acuerdo al D.S. N°7/2009 del MINGEPRES como concentración anual y de 24 horas

el valle central de la VI Región, que incluye totalmente a las siguientes comunas: Graneros,

Rancagua, Doñihue, Olivar, Coltauco, Coínco, Quinta de Tilcoco, San Vicente de Tagua Tagua

y Placilla; e incluye parcialmente a las comunas de Mostazal, Codegua, Machalí, Malloa,

Rengo, Requínoa, San Fernando y Chimbarongo y que actualmente se cuenta con un Plan

de Descontaminación Atmosférica (PDA), por DTO 15/2013 MMA, que establece plan de

descontaminación atmosférica para el Valle Central de la Región del Libertador General

Bernardo O’Higgins. Se considerará dicho PDA como referencia para este estudio de

emisiones.

Para evaluar el impacto sobre la calidad del aire de la comuna de Rancagua, debido a la

emisión de material particulado respirable MP 10 generada por el proyecto y descartar un

riesgo para la salud de las personas, bajo los términos establecidos en el literal a) del artículo

5 del Reglamento del Sistema de Evaluación de Impacto Ambiental (D.S. N°40/2013 del

MMA), se realizó una modelación de dispersión atmosférica a través del modelo de

proyecto. Adicionalmente, para dar cumplimiento a las normas ambientales vigentes, se

evalúan otros compuestos generados por el proyecto como MP 2,5, CO, NO x y SO 2.

5

Adenda N°1

Proyecto Modificación Barrio Los Pinares

Informe de Modelación Atmosférica

Para la modelación, tanto meteorológica como de dispersión atmosférica, se consideró un

dominio de 74x74 km, con 1 km de resolución. La emisión considerada para este análisis

corresponde a la mayor emisión generada por el proyecto, la cual se presenta en la en el

año 7 de construcción del proyecto, ya que a esa altura se encontraran operativas las

viviendas del proyecto existente (ya evaluado ambientalmente) y la finalización de la

construcción de la modificación de Barrio Los Pinares y operación de la misma. Esta emisión

fue estimada a través de la metodología indicada en el Estudio de Emisiones Atmosféricas

presentado en el Anexo X de la Adenda N°1, y considera el peor escenario para la fase de

operación del proyecto, lo que corresponde a un escenario donde la totalidad de las

viviendas poseen calefacción residencial con base a leña, tanto del proyecto existente como

de la modificación que se encuentra actualmente en evaluación.

Adicionalmente, se consideraron 6 receptores específicos, ubicados dentro del área de

influencia del componente medio humano, para la evaluación sobre la salud de las

personas, principalmente poblaciones aledañas al proyecto.

6

Adenda N°1

Proyecto Modificación Barrio Los Pinares

Informe de Modelación Atmosférica

**1.1.** **Objetivos**

**Objetivo General**

Definir concentración de elementos MP 10 y MP 2,5, CO, NO 2 y SO 2, para poder fundamentar

que las medidas a implementar para controlar dichas emisiones son suficientes para

descartar un riesgo para la salud de las personas, bajo los términos establecidos en el literal

a) del artículo 5 del Reglamento del Sistema de Evaluación de Impacto Ambiental (D.S.

N°40/2013 del MMA).

**Objetivos Específicos**

 - Modelar la dispersión atmosférica de la mayor emisión de material particulado

respirable MP 10 y material particulado fino respirable MP 2,5 generado por el proyecto.

 - Modelar la dispersión atmosférica de la mayor emisión de dióxido de azufre (SO 2 ),

dióxido de nitrógeno (NO 2 ) y monóxido de carbono (CO), generado por el proyecto.

 - Determinar zonas de máximo y bajo impacto a través de la evaluación del alcance de la

dispersión del material particulado (MP 10 ) identificando máximas y mínimas

concentraciones.

 - Delimitar, con base a la modelación de la dispersión de las emisiones de MP 10

mencionados, determinando así el área de influencia para el componente aire

relacionado a emisiones atmosféricas.

 - Evaluar la concentración de material particulado (MP 10 y MP 2,5 ), dióxido de azufre (SO 2 ),

dióxido de nitrógeno (NO 2 ) y monóxido de carbono (CO), sobre receptores cercanos al

proyecto (edificaciones con destino habitacional, principalmente).

 - Determinar la magnitud del impacto generado por el aporte de concentración asociado

las emisiones del proyecto evaluando los niveles obtenidos con respecto a la condición

basal de la comuna de Rancagua, y con respecto a la normativa primaria de calidad

ambiental de material particulado respirable (MP 10 ) y material particulado fino

respirable (MP 2,5 ), dióxido de azufre (SO 2 ), dióxido de nitrógeno (NO 2 ) y monóxido de

carbono (CO).

7

Adenda N°1

Proyecto Modificación Barrio Los Pinares

Informe de Modelación Atmosférica

**2.** **ANTECEDENTES**

Actualmente, la presencia de material particulado y gases en el ambiente está regulada por

normas primarias de calidad ambiental definidas para cada clasificación. Estas normas

primarias de calidad ambiental establecen límites de concentración, condiciones de

superación y niveles para determinar situaciones de emergencia ambiental, con el objetivo

de proteger la salud de las personas de los efectos agudos y crónicos del material

particulado y gases, con un nivel de riesgo aceptable.

A continuación en la Tabla 1, se presentan los valores límites de referencia para el análisis

del presente documento.

**Tabla 1. Normas de Calidad del Aire Consideradas en el Estudio.**

|Parámetro|Tipo de<br>Norma|Estadístico|Valor de<br>referencia|Fuente|
|---|---|---|---|---|
|MP10|Primaria|Promedio del<br>periodo|50 μg/m3N|D.S. N°45/02 MINSEGPRES|
|MP10|Primaria|Percentil<br>98<br>Diario|150 μg/m3N|D.S. N°59/98 MINSEGPRES|
|MP2,5|Primaria|Promedio del<br>periodo|20 μg/m3N|D.S. N°12/11 MMA|
|MP2,5|Primaria|Percentil<br>98<br>Diario|50 μg/m3N|D.S. N°12/11 MMA|
|SO2|Primaria|Promedio del<br>periodo|60 μg/m3N|D.S. N°104/18 MMA|
|SO2|Primaria|Percentil<br>99<br>Diario|150 μg/m3N|D.S. N°104/18 MMA|
|SO2|Primaria|Percentil 98,5<br>Horario|350 μg/m3N|D.S. N°104/18 MMA|
|NO2|Primaria|Promedio del<br>periodo|100 μg/m3N|D.S.<br>N°114/02<br>MINSEGPRES|
|NO2|Primaria|Percentil<br>99<br>Horario|400 μg/m3N|D.S.<br>N°114/02<br>MINSEGPRES|
|CO|Primaria|Percentil 99 8<br>horas|1.000 μg/m3N|D.S.<br>N°115/02<br>MINSEGPRES|
|CO|Primaria|Percentil<br>99<br>Horario|3.000 μg/m3N|D.S.<br>N°115/02<br>MINSEGPRES|

_Fuente: Elaboración propia en base a normativa ambiental de calidad de aire._

8

Adenda N°1

Proyecto Modificación Barrio Los Pinares

Informe de Modelación Atmosférica

**2.1.** **Antecedentes de la Calidad del Aire en la comuna de Rancagua.**

El proyecto se emplaza en la comuna de Rancagua, dentro de la zona declarada saturada

por material particulado respirable MP 10, de acuerdo al D.S. N°7/2009 del MINGEPRES como

concentración anual y de 24 horas, debido a la superación de la normativa primaria de

calidad ambiental para dicho compuesto. Para evaluar la calidad de aire en la zona de

ubicación del proyecto se considera la estación más cercana, la cual corresponde a la EMRP

Rancagua I, la cual se encuentra a aproximadamente 1,5 km del proyecto.

A continuación, en la Figura 1 se presenta la ubicación de dicha estación con respecto al

proyecto, mientras que en la Tabla 2, se presentan los antecedentes generales de dicha

estación.

|Figura 1. Ubicación de EMRP “Rancagua I”.|Col2|Col3|Col4|
|---|---|---|---|
|||||
|**Consultor:**|**Carta:**|**Escala:**<br>|**Simbología**|
||UBICACIÓN EMRP<br>COMUNA DE<br>RANCAGUA|1:15.000|<br> <br>Proyecto<br>EMRP|
||UBICACIÓN EMRP<br>COMUNA DE<br>RANCAGUA|**Proyección:**<br>|**Proyección:**<br>|
||UBICACIÓN EMRP<br>COMUNA DE<br>RANCAGUA|WGS 84 UTM H19S|WGS 84 UTM H19S|

_Fuente: Elaboración propia._

9

Adenda N°1

Proyecto Modificación Barrio Los Pinares

Informe de Modelación Atmosférica

**Tabla 2. Información general de la EMRP “Rancagua I”.**

|Estación|Rancagua I|
|---|---|
|Propietario|Ministerio del Medio Ambiente|
|Operador|Asesorías Algoritmos Ltda.|
|Región|del Libertador General Bernardo<br>O'Higgins|
|Provincia|Cachapoal|
|Comuna|Rancagua|
|Coordenadas UTM 19S|342015 E|
|Coordenadas UTM 19S|6218523 N|
|Recepción de datos|En línea|
|Inicio de operación|2004-05-01|
|Estado|Vigente|

_Fuente: https://sinca.mma.gob.cl/_

De acuerdo a la tabla precedente y los registros disponibles en el Sistema de Información

Nacional de Calidad del Aire (SINCA), la estación cuenta con datos desde el año 2004 hasta

la fecha.

En los puntos a continuación, se presentan los antecedentes de la calidad del aire de la

comuna de Rancagua con base en los registros de la estación de monitoreo calificada con

representatividad poblacional “Rancagua I”, los cuales serán utilizados para comparar la

situación basal de la comuna con el aporte adicional de material particulado y gases de

combustión del proyecto.

El periodo contemplado para la caracterización de la calidad de aire de la comuna de

Rancagua correspondió a los datos trianuales de la estación (periodo 2017 - 2019), lo

anterior debido a los datos correspondientes al año 2020 a la fecha no se encuentran

validados. Cabe destacar que para algunos casos, no existen datos para el periodo de

tiempo seleccionado, lo cual se indica en cada uno de los puntos evaluados a continuación.

10

Adenda N°1

Proyecto Modificación Barrio Los Pinares

Informe de Modelación Atmosférica

**2.1.1.** **Material Particulado Respirable (MP** **10** **).**

En la Figura 2, se presentan las series de tiempo correspondientes a las concentraciones

promedio en 24 horas de MP 10 para la estación Rancagua I, se presentan los registros para

los años 2017-2019. Como se puede observar existe una tendencia a un aumento de las

concentraciones de MP 10 en el período mayo a septiembre (temporada más fría).

**Figura 2. Concentración promedio de 24 horas MP** **10** **.**

_[Fuente: Elaboración propia con base en datos obtenidos de https://sinca.mma.gob.cl/](https://sinca.mma.gob.cl/)_

Por otro lado, en la

11

Adenda N°1

Proyecto Modificación Barrio Los Pinares

Informe de Modelación Atmosférica

Figura 3, se presenta la concentración promedio anual de MP 10, donde se puede ver que en

los tres años seleccionados existe superación de la normativa de calidad de aire primaria

establecida para dicho elemento.

12

Adenda N°1

Proyecto Modificación Barrio Los Pinares

Informe de Modelación Atmosférica

**Figura 3. Concentración promedio anual de MP** **10** **.**

_[Fuente: Elaboración propia con base en datos obtenidos de https://sinca.mma.gob.cl/](https://sinca.mma.gob.cl/)_

Por otro lado, en la Tabla 3 y Tabla 4 se presentan la concentración media y el percentil 98

de concentraciones en 24 horas de MP 10 registradas en la estación Rancagua I. De las tablas

se puede concluir que, en la estación, los registros del trienio considerado superan el nivel

de latencia, para la norma anual de MP 10, alcanzando un 120% del valor de la norma.

**Tabla 3. Concentración Media Anual de MP** **10** **(μg/m** **[3]** **N)**

|Estación|Norma Primaria de MP (D.S. No 59/98 MINSEGPRES)<br>10<br>- Media Anual|Col3|Col4|Trianual|Porcentaje de la<br>norma|
|---|---|---|---|---|---|
|**Estación**|**Valor Norma: 50 (μg/m3N)**|**Valor Norma: 50 (μg/m3N)**|**Valor Norma: 50 (μg/m3N)**|**Valor Norma: 50 (μg/m3N)**|**Valor Norma: 50 (μg/m3N)**|
|**Estación**|**Año**|**Año**|**Año**|**Año**|**Año**|
|**Estación**|**2017**|**2018**|**2019**|**2019**|**2019**|
|Rancagua I|64,59|55,46|60,42|60,16|120%|

_Fuente: https://sinca.mma.gob.cl/_

13

Adenda N°1

Proyecto Modificación Barrio Los Pinares

Informe de Modelación Atmosférica

**Tabla 4. Concentraciones 24 horas de MP** **10** **(μg/m** **[3]** **N).**

|Estación|Norma Primaria de MP10 (D.S. No 59/98 MINSEGPRES) - Percentil 98 24 Horas|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**Estación**|**Valor Norma: 150 (μg/m3N)**|**Valor Norma: 150 (μg/m3N)**|**Valor Norma: 150 (μg/m3N)**|**Valor Norma: 150 (μg/m3N)**|**Valor Norma: 150 (μg/m3N)**|**Valor Norma: 150 (μg/m3N)**|
|**Estación**|**Año**|**Año**|**Año**|**Año**|**Año**|**Año**|
|**Estación**|**2017**|**2017**|**2018**|**2018**|**2019**|**2019**|
|**Estación**|**Valor**|**% Norma**|**Valor**|**% Norma**|**Valor**|**% Norma**|
|Rancagua I|132,84|89%|115,76|104%|142,2|95%|

_Fuente: https://sinca.mma.gob.cl/_

**2.1.2.** **Material Particulado Respirable (MP** **2,5** **).**

La Figura 4, muestra la serie de tiempo correspondiente a las concentraciones promedio en

24 horas de MP 2,5 para la Estación Rancagua I. En dicha figura se puede observar la

tendencia a un aumento durante los meses de la época más fría (mayo a septiembre), al

igual que la serie de tiempo de MP 10, presentada anteriormente.

**Figura 4. Concentración promedio de 24 horas MP** **2,5** **.**

_[Fuente: Elaboración propia con base en datos obtenidos de https://sinca.mma.gob.cl/](https://sinca.mma.gob.cl/)_

14

Adenda N°1

Proyecto Modificación Barrio Los Pinares

Informe de Modelación Atmosférica

Por otro lado, en la Figura 5, se presenta la concentración promedio anual de MP 2,5, donde

se puede ver que en los tres años seleccionados no existe superación de la normativa de

calidad de aire primaria establecida para dicho elemento.

**Figura 5. Concentración promedio anual de MP** **2,5** **.**

_[Fuente: Elaboración propia con base en datos obtenidos de https://sinca.mma.gob.cl/](https://sinca.mma.gob.cl/)_

Por otra parte, en la Tabla 5 y Tabla 6 se observa que para el promedio trianual de las

concentraciones en estación Rancagua I, las cuales sobrepasan el nivel de saturación

establecido en el D.S. No 12/11 MMA. Respecto al percentil 98 de las concentraciones en

24 horas, los registros muestran que, en todos los años estudiados en la estación sobrepasa

el límite de saturación establecido.

**Tabla 5. Concentración Media Anual de MP** **2,5** **(μg/m** **[3]** **N).**

|Estación|Norma Primaria de MP (D.S. N° 12/2011 del MMA) -<br>2,5<br>Media Anual|Col3|Col4|Trianual|Porcentaje de la<br>norma|
|---|---|---|---|---|---|
|**Estación**|**Valor Norma: 20 (μg/m3N)**|**Valor Norma: 20 (μg/m3N)**|**Valor Norma: 20 (μg/m3N)**|**Valor Norma: 20 (μg/m3N)**|**Valor Norma: 20 (μg/m3N)**|
|**Estación**|**Año**|**Año**|**Año**|**Año**|**Año**|
|**Estación**|**2017**|**2018**|**2019**|**2019**|**2019**|
|Rancagua I|23,58|21,79|24,81|23,38|117%|

_Fuente: https://sinca.mma.gob.cl/_

15

Adenda N°1

Proyecto Modificación Barrio Los Pinares

Informe de Modelación Atmosférica

**Tabla 6. Concentraciones 24 horas de MP** **2,5** **(μg/m** **[3]** **N).**

|Estación|Norma Primaria de MP (D.S. N° 12/2011 del MMA) - Percentil 98 24 Horas<br>2,5|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**Estación**|**Valor Norma: 50 (μg/m3N)**|**Valor Norma: 50 (μg/m3N)**|**Valor Norma: 50 (μg/m3N)**|**Valor Norma: 50 (μg/m3N)**|**Valor Norma: 50 (μg/m3N)**|**Valor Norma: 50 (μg/m3N)**|
|**Estación**|**Año**|**Año**|**Año**|**Año**|**Año**|**Año**|
|**Estación**|**2017**|**2017**|**2018**|**2018**|**2019**|**2019**|
|**Estación**|**Valor**|**% Norma**|**Valor**|**% Norma**|**Valor**|**% Norma**|
|Rancagua I|73|148%|75,82|152%|82|164%|

_Fuente: https://sinca.mma.gob.cl/_

**2.1.3.** **Dióxido de nitrógeno (NO2).**

En la Figura 6, se presentan las series de tiempo de los registros horarios de NO 2 de la

estación Rancagua I, cabe destacar que se observan registros con categoría de preliminares

(color anaranjado) y no validados (color verde). Además, la estación solamente cuenta con

datos hasta el año 2009, por lo tanto se realiza el análisis con los datos disponibles,

considerando también los últimos tres años con los que se cuenta información.

**Figura 6. Serie de Tiempo Concentraciones horarias de NO** **2.**

_Fuente: Elaboración propia con base en datos obtenidos de https://sinca.mma.gob.cl/_

16

Adenda N°1

Proyecto Modificación Barrio Los Pinares

Informe de Modelación Atmosférica

**Figura 7. Serie de Tiempo Concentraciones anuales de NO** **2**

_Fuente: Elaboración propia con base en datos obtenidos de https://sinca.mma.gob.cl/_

En la Tabla 7 y Tabla 8 se presentan los estadísticos correspondientes al monitoreo de

dióxido de nitrógeno en la estación Rancagua I, Se observa que los límites de saturación y

latencia establecidos por el D.S. No 114/02 MINSEGPRES, tanto para la media anual como

el percentil 99 horario, no son sobrepasados, alcanzando un máximo de 20% respecto de la

norma anual, al igual que para el percentil 99 horario, se presenta un máximo del 16,2%

respecto al valor de la norma.

**Tabla 7. Concentración Media Anual de NO** **2** **(μg/m** **[3]** **N).**

|Estación|Norma Primaria de NO2 (D.S. No 114/02 MINSEGPRES)<br>- Media Anual|Col3|Col4|Trianual|Porcentaje de la<br>norma|
|---|---|---|---|---|---|
|**Estación**|**Valor Norma: 100 (μg/m3N)**|**Valor Norma: 100 (μg/m3N)**|**Valor Norma: 100 (μg/m3N)**|**Valor Norma: 100 (μg/m3N)**|**Valor Norma: 100 (μg/m3N)**|
|**Estación**|**Año**|**Año**|**Año**|**Año**|**Año**|
|**Estación**|**2007**|**2008**|**2009**|**2009**|**2009**|
|Rancagua I|21,86|17,34|21,08|20,09|20%|

_Fuente: https://sinca.mma.gob.cl/_

17

Adenda N°1

Proyecto Modificación Barrio Los Pinares

Informe de Modelación Atmosférica

**Tabla 8. Concentraciones Percentil 99 Promedio Horario de NO** **2** **(μg/m** **[3]** **N).**

|Estación|Norma Primaria de NO2 (D.S. No 114/02 MINSEGPRES)<br>- Percentil 99 1 Hora|Col3|Col4|Trianual|Porcentaje de la<br>norma|
|---|---|---|---|---|---|
|**Estación**|**Valor Norma: 400 (μg/m3N)**|**Valor Norma: 400 (μg/m3N)**|**Valor Norma: 400 (μg/m3N)**|**Valor Norma: 400 (μg/m3N)**|**Valor Norma: 400 (μg/m3N)**|
|**Estación**|**Año**|**Año**|**Año**|**Año**|**Año**|
|**Estación**|**2007**|**2008**|**2009**|**2009**|**2009**|
|Rancagua I|70,68|59,57|63,73|64,66|16,2%|

_Fuente: https://sinca.mma.gob.cl/_

**2.1.4.** **Monóxido de Carbono (CO).**

En la Figura 8 se presentan las series de tiempo de los registros horarios de CO en la estación

Rancagua I. Cabe destacar que en la estación seleccionada se observan registros con

categoría de preliminares (color anaranjado) y no validados (color verde), sin embargo, la

mayoría de los datos de encuentran validados (color azul).

**Figura 8. Serie de Tiempo Concentraciones de CO Estación Rancagua I.**

_Fuente: https://sinca.mma.gob.cl/_

18

Adenda N°1

Proyecto Modificación Barrio Los Pinares

Informe de Modelación Atmosférica

En la Tabla 9 y Tabla 10 se presentan los estadísticos correspondientes al monitoreo de

monóxido de carbono en la estación Rancagua I. Se observa que los valores registrados no

sobrepasan los límites de saturación y latencia establecidos por el D.S. No 115/02

MINSEGPRES para la norma anual, alcanzando un máximo de 7% del valor de la norma en

estación Rancagua I. De la misma manera para la norma de 8 horas en la Estación Rancagua

I se presenta el promedio trianual que alcanza el 26% respecto al valor.

**Tabla 9. Concentración Percentil 99 Horario de CO (μg/m** **[3]** **N).**

|Estación|Norma Primaria de CO (D.S. No 115/02 MINSEGPRES) -<br>Percentil 99 máximos diarios en 1 Hora|Col3|Col4|Trianual|Porcentaje de la<br>norma|
|---|---|---|---|---|---|
|**Estación**|**Valor Norma: 30.000 (μg/m3N)**|**Valor Norma: 30.000 (μg/m3N)**|**Valor Norma: 30.000 (μg/m3N)**|**Valor Norma: 30.000 (μg/m3N)**|**Valor Norma: 30.000 (μg/m3N)**|
|**Estación**|**Año**|**Año**|**Año**|**Año**|**Año**|
|**Estación**|**2017**|**2018**|**2019**|**2019**|**2019**|
|Rancagua I|2713,65|1032,22|2836,39|2194,09|7%|

_Fuente: https://sinca.mma.gob.cl/_

**Tabla 10. Concentración Percentil 99 Promedio 8 Horas de CO (μg/m** **[3]** **N).**

|Estación|Norma Primaria de CO (D.S. No 115/02 MINSEGPRES) -<br>Percentil 99 máximos diarios en 8 Horas|Col3|Col4|Trianual|Porcentaje de la<br>norma|
|---|---|---|---|---|---|
|**Estación**|**Valor Norma: 10.000 (μg/m3N)**|**Valor Norma: 10.000 (μg/m3N)**|**Valor Norma: 10.000 (μg/m3N)**|**Valor Norma: 10.000 (μg/m3N)**|**Valor Norma: 10.000 (μg/m3N)**|
|**Estación**|**Año**|**Año**|**Año**|**Año**|**Año**|
|**Estación**|**2017**|**2018**|**2019**|**2019**|**2019**|
|Rancagua I|3026,69|1038,52|3712,66|2592,62|26%|

_Fuente: https://sinca.mma.gob.cl/_

**2.1.5.** **Dióxido de Azufre (SO** **2** **).**

En la Figura 9 se presentan las series de tiempo de los registros horarios de SO 2 . Cabe

destacar que, en la estación Rancagua I, se tienen registros con categoría de preliminares

(color anaranjado) y no validados (color verde), sin embargo, la mayoría de los datos se

encuentran validados (color azul).

19

Adenda N°1

Proyecto Modificación Barrio Los Pinares

Informe de Modelación Atmosférica

**Figura 9. Serie de Tiempo Concentraciones de SO2 Estación Rancagua I.**

_Fuente: https://sinca.mma.gob.cl/_

En la Tabla 11, Tabla 12 y Tabla 13 se presentan los estadígrafos de la norma primaria de

dióxido de azufre (media anual, percentil 99 de las concentraciones diarias y percentil 98,5

de las concentraciones horarias, respectivamente) registrados en la estación, durante el

trienio analizado (2017-2019). En estas Tablas se observa que para todos los estadígrafos

los registros no sobrepasan los límites de saturación y latencia establecidos por el D.S. No

104/18 del MMA, alcanzando un máximo de 10% de la norma para el promedio anual de

las concentraciones en la estación Rancagua I.

20

Adenda N°1

Proyecto Modificación Barrio Los Pinares

Informe de Modelación Atmosférica

**Tabla 11. Concentración Media Anual de SO** **2** **(μg/m** **[3]** **N).**

|Estación|Norma Primaria de SO2 (D.S. No 104/18 MMA) -<br>Media Anual|Col3|Col4|Trianual|Porcentaje de la<br>norma|
|---|---|---|---|---|---|
|**Estación**|**Valor Norma: 60 (μg/m3N)**|**Valor Norma: 60 (μg/m3N)**|**Valor Norma: 60 (μg/m3N)**|**Valor Norma: 60 (μg/m3N)**|**Valor Norma: 60 (μg/m3N)**|
|**Estación**|**Año**|**Año**|**Año**|**Año**|**Año**|
|**Estación**|**2017**|**2018**|**2019**|**2019**|**2019**|
|Rancagua I|4,23|9,92|4,55|6,23|10%|

_Fuente: https://sinca.mma.gob.cl/_

**Tabla 12. Concentración Percentil 99 Promedio Diario de SO** **2** **(μg/m** **[3]** **N).**

|Estación|Norma Primaria de SO2 (D.S. No 104/18 MMA) -<br>Percentil 99 24 Horas|Col3|Col4|Trianual|Porcentaje de la<br>norma|
|---|---|---|---|---|---|
|**Estación**|**Valor Norma: 150 (μg/m3N)**|**Valor Norma: 150 (μg/m3N)**|**Valor Norma: 150 (μg/m3N)**|**Valor Norma: 150 (μg/m3N)**|**Valor Norma: 150 (μg/m3N)**|
|**Estación**|**Año**|**Año**|**Año**|**Año**|**Año**|
|**Estación**|**2017**|**2018**|**2019**|**2019**|**2019**|
|Rancagua I|10,44|16,00|14,52|13,65|9,10%|

_Fuente: https://sinca.mma.gob.cl/_

**Tabla 13. Concentración Percentil 98,5 1 Hora de SO** **2** **(μg/m** **[3]** **N).**

|Estación|Norma Primaria de SO2 (D.S. No 104/18 MMA) -<br>Percentil 98,5 1 Hora|Col3|Col4|Trianual|Porcentaje de la<br>norma|
|---|---|---|---|---|---|
|**Estación**|**Valor Norma: 350 (μg/m3N)**|**Valor Norma: 350 (μg/m3N)**|**Valor Norma: 350 (μg/m3N)**|**Valor Norma: 350 (μg/m3N)**|**Valor Norma: 350 (μg/m3N)**|
|**Estación**|**Año**|**Año**|**Año**|**Año**|**Año**|
|**Estación**|**2017**|**2018**|**2019**|**2019**|**2019**|
|Rancagua I|9,1|20,4|6,5|12,0|4,46%|

_Fuente: https://sinca.mma.gob.cl/_

21

Adenda N°1

Proyecto Modificación Barrio Los Pinares

Informe de Modelación Atmosférica

**2.2.** **Antecedentes Meteorológicos**

Al momento de analizar la dispersión de contaminantes en la atmósfera, es muy importante

caracterizar la meteorología de la zona de estudio, dado que sus parámetros, tales como

vientos, temperatura y precipitación, entre otros, influyen de muchas maneras sobre la

concentración. A continuación, se presenta la caracterización de los vientos, temperatura y

precipitación de la comuna de Rancagua, cuyos datos se obtienen de la Estación EMRP

“Rancagua I”.

**2.2.1.** **Vientos**

Para la presentación de los vientos, se consideró el mismo periodo de tiempo utilizado para

la caracterización de la calidad del aire de la comuna de Rancagua. Los datos fueron

obtenidos de la estación Rancagua I para el año 2020, ya que la base de datos utilizada para

la modelación corresponde a datos del año 2020 y se representan en la Figura 10.

De acuerdo a lo mostrado en la Figura 10, los vientos predominantes de la comuna de

Rancagua corresponden a vientos provenientes desde el noreste, los cuales se hacen

presente en todas las estaciones del año. En verano y primavera se puede observar que el

porcentaje de vientos que se dirigen hacia el sur son mayor que en las demás estaciones,

además la dirección del viento es más homogéneas que en invierno y otoño.

22

Adenda N°1

Proyecto Modificación Barrio Los Pinares

Informe de Modelación Atmosférica

**Figura 10. Rosas de dirección de viento por estación del año.**

|Verano|Otoño|
|---|---|
|||
|**Invierno**|**Primavera**|
|||

_Fuente: Elaboración propia con base en datos obtenidos de https://sinca.mma.gob.cl/_

**2.2.2.** **Temperatura y Precipitación**

A continuación, en la Figura 11, se presenta un climograma que incluye precipitación y

temperatura mensual normal para la comuna de Rancagua. Tal como se mencionó

anteriormente, dicha información se obtuvo de la Estación Rancagua I y también se realiza

para el año 2017, ya que corresponde al último año que contiene registros completos en la

estación seleccionada.

23

Adenda N°1

Proyecto Modificación Barrio Los Pinares

Informe de Modelación Atmosférica

**Figura 11. Precipitación y temperaturas, comuna de Rancagua.**

_Fuente: Elaboración propia con base en datos obtenidos de https://sinca.mma.gob.cl/_

De acuerdo al gráfico anterior, las precipitaciones se presentan principalmente en invierno,

siendo agosto el mes más lluvioso. Con respecto a las temperaturas, éstas oscilan entre los

7,9 y 21 °C (Tabla 14), presentando los valores más bajos en el periodo otoño - invierno.

**Tabla 14. Precipitación y temperatura normal mensual, comuna de Rancagua.**

|Mes|Precipitación (mm)|Temperatura (°C)|
|---|---|---|
|ENE|0,0|21,0|
|FEB|0,0|20,3|
|MAR|0,0|18,0|
|ABR|5,0|13,8|
|MAY|4,0|10,4|
|JUN|13,0|8,6|
|JUL|5,0|7,9|
|AGO|25,0|9,4|
|SEP|11,0|11,5|
|OCT|4,0|14,3|
|NOV|0,0|17,1|
|DIC|0,0|19,7|

_Fuente: Elaboración propia con base en datos obtenidos de https://sinca.mma.gob.cl/_

24

Adenda N°1

Proyecto Modificación Barrio Los Pinares

Informe de Modelación Atmosférica

**3.** **JUSTIFICACIÓN DE LOS MODELOS UTILIZADOS EN LA MODELACIÓN**

**3.1.** **Uso del Modelo CALPUFF.**

La modelación de dispersión atmosférica de las emisiones de material particulado y gases

de combustión generadas por el proyecto, se realizó a través un modelo tipo “Puff”,

específicamente el modelo CALPUFF.

Tal como lo define la Guía, los modelos tipo “puff” son una combinación entre los modelos

Gaussianos y los modelos Lagrangeanos, en el sentido de que esencialmente calculan la

dispersión de contaminantes provenientes de una emisión instantánea, llamada “puff”, a lo

largo de una trayectoria. Su aproximación matemática consiste en estimar la dispersión en

forma Gaussiana en cada punto de una trayectoria, es decir, los modelos tipo “puff” sólo

requieren una trayectoria por “puff”, lo que hace su cálculo mucho más rápido. En el caso

de emisiones continuas, se simulan las trayectorias y la dispersión Gaussiana de muchos

“puffs”. El modelo tipo “puff” recomendado por la Guía es el modelo CALPUFF.

El CALPUFF, es un modelo completo que incorpora herramientas para procesar datos

meteorológicos y geofísicos, modelos de dispersión y pos procesamiento. Dicho modelo es

recomendado por la Agencia de Protección Ambiental de los Estados Unidos (EPA) para

modelar transporte de contaminantes a larga distancia.

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

25

Adenda N°1

Proyecto Modificación Barrio Los Pinares

Informe de Modelación Atmosférica

2σ
y [2][c2] []]

Q
C=
2πσ x σ y

gexp

~~[~~ [−d] 2σ x [2][a2]

[−d] 2σ x [2][a2] ~~[ ]]~~ [ exp[−d] 2σ y [2][c2]

2
g=

(2π)

1
2 σ z

∞

∑exp

n=−∞

~~[~~ [−][(][H] [e] 2σ [+ 2nh] z [2] [)] [2] ~~]~~

Dónde:

C, es concentración a nivel del suelo (g/m [3] ),

Q, es masa de contaminantes (g) en la nube.

σx, es desviación estándar (m) de la distribución de Gauss en el viento a lo largo de la

dirección.

σy, es desviación estándar (m) de la distribución de Gauss en el viento de costado

σz, es desviación estándar (m) de la distribución de Gauss en la dirección vertical.

da, es distancia (m) del centro de la nube al receptor en la dirección del viento a lo largo.

dc, es distancia (m) del centro de la nube al receptor en la dirección de viento cruzado.

g, es el término vertical (m) de la ecuación Gaussiana.

H, es la altura afectiva (m) desde el nivel del suelo del hojaldre.

h, es la altura de la capa de mezcla.

De acuerdo a las características del terreno, las distintas unidades geomorfológicas del área

de influencia del proyecto y el dominio de la modelación se consideró utilizar el modelo

CALPUFF para simular la dispersión de los contaminantes.

**3.2.** **Uso del Modelo Weather Research and Forecasting Model (WRF).**

El modelo Weather Research and Forecasting (WRF), es un modelo numérico recomendado

para la generación de datos meteorológicos y uno de los modelos de pronóstico

meteorológicos más avanzados.

Debido a la falta de una red robusta de estaciones meteorológicas, la Guía para el Uso de

Modelos de Calidad del Aire en el SEIA recomienda el uso de WRF por sobre el uso del

CALMET. Además, el mismo documento, sugiere el uso del WRF para la modelación de

dispersión de contaminantes con CALPUFF.

26

Adenda N°1

Proyecto Modificación Barrio Los Pinares

Informe de Modelación Atmosférica

**4.** **METODOLOGÍA**

La modelación de la dispersión de contaminantes se realizó de acuerdo a la siguiente

metodología.

**4.1.** **Dominio Modelación Meteorológica**

El modelo WRF es un modelo matemático que simula, a partir de variables influyentes en la

meteorología, las condiciones meteorológicas dentro de un dominio de modelación. Para

el presente caso, se consideró un dominio de 74 x 74 km, con 1 km de resolución, y 10 celdas

de altura desde 0 m hasta los 4.000 m, permitiendo considerar un amplio rango para la

variación diaria de la capa de mezcla.

El dominio de modelación WRF abarca toda el área circundante a la zona de emplazamiento

del proyecto, incluyendo la comuna de Rancagua y comunas aledañas, tal como se muestra

en la Figura 12. Las coordenadas de los vértices y el centroide del dominio de la modelación

WRF, se presentan en la Tabla 15 a continuación:

27

Adenda N°1

Proyecto Modificación Barrio Los Pinares

Informe de Modelación Atmosférica

|Figura 12. Dominio modelación WRF.|Col2|Col3|Col4|
|---|---|---|---|
|||||
|**Consultor:**|**Carta:**|**Escala:**<br>|**Simbología**|
||DOMINIO MODELACIÓN<br>WRF|1:600.000|<br> <br>Proyecto<br>Dominio|
||DOMINIO MODELACIÓN<br>WRF|**Proyección:**|**Proyección:**|
||DOMINIO MODELACIÓN<br>WRF|WGS 84 UTM H19S|WGS 84 UTM H19S|

_Fuente: Elaboración propia._

**Tabla 15. Coordenadas de vértices y centroide del dominio de Modelación WRF.**

|Vértice|Proyección UTM, Huso 19 Sur; Datum WGS-84|Col3|
|---|---|---|
|**Vértice**|**Este (m)**|**Norte (m)**|
|Noroeste|306999,29|6257280,76|
|Noreste|380068,05|6256135,48|
|Suroeste|305624,96|6185586,34|
|Sureste|377777,49|6183753,90|
|Centroide|342554,00|6220358,00|

_Fuente: Elaboración propia._

28

Adenda N°1

Proyecto Modificación Barrio Los Pinares

Informe de Modelación Atmosférica

**4.2.** **Dominio de Modelación CALPUFF**

El dominio de la modelación de CALPUFF se extiende sobre el mismo dominio de la

modelación WRF, correspondiente a un área 74 km x 74 km, tal como se presenta en la

Figura 13. Esto para evaluar la mayor cantidad de territorio posible con las herramientas

disponibles.

|Figura 13. Dominio de la Modelación de CALPUFF.|Col2|Col3|Col4|
|---|---|---|---|
|||||
|**Consultor:**|**Carta:**|**Escala:**<br>|**Simbología**|
||DOMINIO MODELACIÓN<br>CALPUFF|1:600.000|<br> <br>Proyecto<br>Dominio|
||DOMINIO MODELACIÓN<br>CALPUFF|**Proyección:**|**Proyección:**|
||DOMINIO MODELACIÓN<br>CALPUFF|WGS 84 UTM H19S|WGS 84 UTM H19S|

_Fuente: Elaboración propia._

Las coordenadas de los vértices y el centroide del dominio de la modelación CALPUFF, se

presentan en la Tabla 16 a continuación:

29

Adenda N°1

Proyecto Modificación Barrio Los Pinares

Informe de Modelación Atmosférica

**Tabla 16. Coordenadas de vértices y centroide del dominio de Modelación CALPUFF.**

|Vértice|Proyección UTM, Huso 19 Sur; Datum WGS-84|Col3|
|---|---|---|
|**Vértice**|**Este (m)**|**Norte (m)**|
|Noroeste|306999,29|6257280,76|
|Noreste|380068,05|6256135,48|
|Suroeste|305624,96|6185586,34|
|Sureste|377777,49|6183753,90|
|Centroide|342554,00|6220358,00|

_Fuente: Elaboración propia._

30

Adenda N°1

Proyecto Modificación Barrio Los Pinares

Informe de Modelación Atmosférica

**4.3.** **Post procesamiento de información**

Para analizar los resultados de dispersión de material particulado y gases de combustión, la

modelación realizada en el dominio presentado anteriormente, representado a través de

una grilla de resolución 1 km, la que entrega datos de concentración de cada vértice de la

misma. El resultado de la concentración en cada una de las grillas en el área estudiada se

adjunta en el Anexo X del presente documento.

Posteriormente, se define el valor de mayor concentración de material particulado y gases

de combustión en toda el área de estudio, dicho valor se compara con la normativa de cada

elemento y también con la situación base de calidad de aire de la zona de estudio.

Para definir el área aproximada de dispersión de estos elementos se toma como referencia

el que supera en mayor porcentaje la normativa, y se realiza un mapa de iso-concentracion

de dicho elemento. Dicho mapa permite evaluar los niveles de concentración en toda el

área de estudio con respecto a la norma primaria de calidad ambiental.

Dadas las características de la grilla, los mapas son el resultado de la interpolación entre los

datos de modelación en cada vértice. Además, los datos de concentración generados por el

modelo son el resultado de la concentración promedio de la primara capa de modelación,

la que tiene lugar desde 0 m nivel del suelo hasta los 20 m.

De acuerdo a lo anterior, el mapa de dispersión e isoconcentración es considerado como

una representación espacial de la pluma y no como referencia concreta de la concentración,

pues éstas suelen estar sobre dimensionadas.

Por otro lado, la evaluación de la concentración en puntos discretos ofrece un sentido de la

magnitud más libre de distorsiones. Por esta razón y con objeto de analizar el impacto en la

calidad del aire sobre la salud de las personas, se consideró adicionalmente una modelación

discreta en 6 receptores específicos que corresponden principalmente a áreas

habitacionales.

En la Tabla 17, se identifica cada uno de los receptores, se presentan sus coordenadas y la

distancia con respecto al proyecto (en relación a un punto medio). Así mismo, en la Figura

14, se puede observar la ubicación espacial de estos puntos con respecto al proyecto.

31

Adenda N°1

Proyecto Modificación Barrio Los Pinares

Informe de Modelación Atmosférica

**Tabla 17. Coordenadas de receptores discretos.**

|Punto|Coordenadas WGS 84 UTM 19S|Col3|Distancia respecto al<br>proyecto (m)|
|---|---|---|---|
|**Punto**|**Este (m)**|**Norte (m)**|**Norte (m)**|
|R1|342250|6220015|114|
|R2|341879|6220509|508|
|R3|342462|6220705|90|
|R4|343133|6221013|520|
|R5|343581|6220504|709|
|R6|343220|6219780|258|

_Fuente: Elaboración propia._

|Figura 14. Ubicación receptores.|Col2|Col3|Col4|
|---|---|---|---|
|||||
|**Consultor:**|**Carta:**|**Escala:**<br>|**Simbología**|
||UBICACIÓN DE<br>RECEPTORES<br>RESPECTO AL<br>PROYECTO|1:20.000|<br> <br>Modificación Barrio Los Pinares<br>Barrio Los Pinares<br>Receptores|
||UBICACIÓN DE<br>RECEPTORES<br>RESPECTO AL<br>PROYECTO|**Proyección:**|**Proyección:**|
||UBICACIÓN DE<br>RECEPTORES<br>RESPECTO AL<br>PROYECTO|WGS 84 UTM H19S|WGS 84 UTM H19S|

_Fuente: Elaboración propia._

32

Adenda N°1

Proyecto Modificación Barrio Los Pinares

Informe de Modelación Atmosférica

**4.4.** **Escenario de modelación**

De acuerdo a los resultados obtenidos en la estimación de emisiones atmosféricas del

proyecto (Anexo X de la Adenda), las mayores emisiones de material particulado se

presentan en el año 7, por lo que la tasa de emisión utilizada para la modelación de la

dispersión del material particulado y gases de combustión corresponde a la emisión

generada por la fase de operación del proyecto y que contempla la totalidad de las viviendas

materializadas como operativas, tanto del proyecto existente como de la modificación que

se presenta actualmente a evaluación. Cabe destacar que para la fase de operación del

proyecto se consideraron dos actividades emisoras (fuentes): la utilización de vehículos por

parte de los propietarios y la operación de viviendas, siendo esta última la principal

actividad generadora de compuestos debido a la calefacción en base a leña (Tabla 18).

Dado que el proyecto corresponde a uno de tipo inmobiliario, el tipo de fuente considerada
para la modelación corresponde a una fuente de Área. Para esto, se construyó un polígono

que abarcase toda la superficie del proyecto. Es importante mencionar que, a pesar que la

actividad de los vehículos se realiza fuera del área de emplazamiento del loteo (trayecto

proyecto - sector céntrico de Rancagua, de acuerdo a lo considerado en el Estudio de

Emisiones Atmosféricas, Anexo X de la Adenda), sólo se consideró el área del loteo dado

que la emisión de los vehículos es despreciable en comparación a la generada por las

viviendas.

De esta manera, la tasa de emisión está dada por la emisión y el área de dicho polígono

(Tabla 18).

**Tabla 18. Tasa de emisión.**

|Elemento|Tipo de<br>fuente|Superficie<br>polígono (m2)|Emisión<br>(t/año)|Tasa de<br>emisión<br>(t/m2/año)|
|---|---|---|---|---|
|MP10|Área|404335,11|7,34|1,82E-05|
|MP2,5|Área|404335,11|6,46|1,60E-05|
|CO|Área|404335,11|55,84|1,38E-04|
|NO2|Área|404335,11|5,37|1,33E-05|
|SO2|Área|404335,11|3.22.E-04|7,97E-10|

_Fuente: Elaboración propia._

33

Adenda N°1

Proyecto Modificación Barrio Los Pinares

Informe de Modelación Atmosférica

A continuación, en la Figura 15 y la Tabla 19 se muestra el polígono de la fuente y las

coordenadas de sus vértices, respectivamente. Cabe destacar que para efectos de programa

se selecciona un polígono de cuatro vértices, por lo tanto, se considera un área mayor a la

de aplicación sobreestimando dicha emisión.

|Figura 15. Fuente de área.|Col2|Col3|Col4|
|---|---|---|---|
|||||
|**Consultor:**|**Carta:**|**Escala:**<br>|**Simbología**|
||FUENTE DE ÁREA|1:5.000|<br> <br>Modificación Barrio Los Pinares<br>Barrio Los Pinares<br>Área modelación<br>Vertices|
||FUENTE DE ÁREA|**Proyección:**|**Proyección:**|
||FUENTE DE ÁREA|WGS 84 UTM H19S|WGS 84 UTM H19S|

_Fuente: Elaboración propia._

34

Adenda N°1

Proyecto Modificación Barrio Los Pinares

Informe de Modelación Atmosférica

**Tabla 19. Coordenadas polígono de fuente de área.**

|Vértice|Proyección UTM, Huso 19 Sur; Datum WGS-84|Col3|
|---|---|---|
|**Vértice**|**Este (m)**|**Norte (m)**|
|A|342599|6220768|
|B|342247|6220150|
|C|342677|6219535|
|D|343183|6220271|

_Fuente: Elaboración propia._

35

Adenda N°1

Proyecto Modificación Barrio Los Pinares

Informe de Modelación Atmosférica

**5.** **RESULTADOS**

**5.1.** **Caracterización geofísicas**

**5.1.1.** **Topografía**

En la Figura 16, se puede observar la topografía dentro del dominio de modelación

meteorológica. La elevación del terreno varía entre los 201 y 3.526 m.s.n.m. El punto rojo

del centro representa la ubicación del proyecto, el cual se encuentra a una elevación de

502 m.s.n.m.

**Figura 16. Elevación de terreno del área de estudio**

|Col1|Consultor:|
|---|---|
|||
||**Carta:**|
||ELEVACIÓN DEL<br>TERRENO|
||**Escala:**<br>|
||1:390.000|
||**Proyección:**<br>|
||LCC|
||**Simbología**|
|||

_Fuente: Elaboración propia._

36

Adenda N°1

Proyecto Modificación Barrio Los Pinares

Informe de Modelación Atmosférica

**5.2.** **Concentraciones**

Con el fin de evaluar la dispersión de los contaminantes generados por las fuentes, como

material particulado respirable (MP 10 ), material particulado respirable fino (MP 2,5 ), dióxido

de azufre (SO 2 ), óxidos de nitrógeno (NO X ) y monóxido de carbono (CO), para la etapa de

operación del Proyecto se realizó una modelación de dispersión de compuestos.

**5.2.1.** **Concentración de compuestos** **dentro del área de estudio.**

Para evaluar la concentración de material particulado y gases de combustión aportada por

las emisiones generadas por el proyecto en su fase de operación, se elaboró una tabla

comparativa de cada uno de los compuestos generados por el proyecto con la normativa

ambiental vigente y la concentración de cada uno de los compuestos dentro del área de

estudio.

**Tabla 20. Evaluación de niveles de concentración para MP** **10** **.**

|Compuesto|Promedio del periodo<br>(μg/m3)|Promedio del periodo<br>EMRP (μg/m3)|Límite D.S. N°59/1998 del<br>MINSEGPRES (μg/m3)|
|---|---|---|---|
|MP10|2,05|60,16|50|
|**Porcentaje respecto a modelación (%)**|**Porcentaje respecto a modelación (%)**|**3,40**|**4,09**|
|**Compuesto**|**Percentil 98 diario**<br>**modelación (μg/m3) **|**Percentil 98 EMRP**<br>**(μg/m3) **|**Límite D.S. N°59/1998 del**<br>**MINSEGPRES (μg/m3) **|
|MP10|5,01|115,76|150|
|**Porcentaje respecto a modelación (%)**|**Porcentaje respecto a modelación (%)**|**4,33**|**3,34**|

_Fuente: Elaboración propia._

**Tabla 21. Evaluación de niveles de concentración para MP** **2,5** **.**

|Compuesto|Promedio del periodo<br>(μg/m3)|Promedio del periodo<br>EMRP (μg/m3)|D.S. N°12/11 MMA<br>(μg/m3)|
|---|---|---|---|
|MP2,5|1,80|24,81|20|
|**Porcentaje respecto a modelación (%)**|**Porcentaje respecto a modelación (%)**|**7,25**|**8,99**|
|**Compuesto**|**Percentil 98 diario**<br>**modelación (μg/m3) **|**Percentil 98 EMRP**<br>**(μg/m3) **|**D.S. N°12/11 MMA**<br>**(μg/m3)**|
|MP2,5|4,41|75,82|50|
|**Porcentaje respecto a modelación (%)**|**Porcentaje respecto a modelación (%)**|**5,82**|**8,82**|

_Fuente: Elaboración propia._

37

Adenda N°1

Proyecto Modificación Barrio Los Pinares

Informe de Modelación Atmosférica

**Tabla 22. Evaluación de niveles de concentración para NO** **2** **.**

|Compuesto|Promedio del periodo<br>(μg/m3)|Promedio del periodo<br>EMRP (μg/m3)|D.S. N°114/02<br>MINSEGPRES (μg/m3)|
|---|---|---|---|
|NO2|1,39|20,09|100|
|**Porcentaje respecto a modelación (%)**|**Porcentaje respecto a modelación (%)**|**6,91**|**1,39**|
|**Compuesto**|**Percentil 99 horario**<br>**modelación (μg/m3) **|**Percentil 99 horario**<br>**EMRP (μg/m3) **|**D.S. N°114/02**<br>**MINSEGPRES (μg/m3) **|
|NO2|3,38|64,66|400|
|**Porcentaje respecto a modelación (%)**|**Porcentaje respecto a modelación (%)**|**5,23**|**0,85**|

_Fuente: Elaboración propia._

**Tabla 23. Evaluación de niveles de concentración para SO** **2** **.**

|Contaminante|Promedio del periodo<br>(μg/m3)|Promedio del periodo<br>EMRP (μg/m3)|D.S. N°104/18 MMA<br>(μg/m3)|
|---|---|---|---|
|SO2|0,00009|6,23|80|
|**Porcentaje respecto a modelación (%)**|**Porcentaje respecto a modelación (%)**|**0,0014**|**0,0001**|
|**Compuesto**|**Percentil 99 Diario**<br>**(μg/m3) **|**Percentil 99 Diario**<br>**EMRP (μg/m3) **|**D.S. N°104/18 MMA**<br>**(μg/m3) **|
|SO2|0,00021|13,65|250|
|**Porcentaje respecto a modelación (%)**|**Porcentaje respecto a modelación (%)**|**0,002**|**0,0001**|
|**Compuesto**|**Percentil 98,5 Horario**<br>**modelación (μg/m3) **|**Percentil 98,5 Horario**<br>**EMRP (μg/m3) **|**D.S. N°104/18 MMA**<br>**(μg/m3) **|
|SO2|0,0009|12|1000|
|**Porcentaje respecto a modelación (%)**|**Porcentaje respecto a modelación (%)**|**0,01**|**0,0001**|

_Fuente: Elaboración propia._

**Tabla 24. Evaluación de niveles de concentración para CO.**

|Compuesto|Percentil 99 8 horas<br>(μg/m3)|Percentil 99 8 horas<br>EMRP (μg/m3)|D.S. N°115/02<br>MINSEGPRES (μg/m3)|
|---|---|---|---|
|CO|37,09|2592,62|10000|
|**Porcentaje respecto a modelación (%)**|**Porcentaje respecto a modelación (%)**|**1,43**|**0,37**|
|**Compuesto**|**Percentil 99 Horario**<br>**modelación (μg/m3) **|**Percentil 99 Horario**<br>**EMRP (μg/m3) **|**D.S. N°115/02**<br>**MINSEGPRES (μg/m3) **|
|CO|158,32|2194,09|30000|
|**Porcentaje respecto a modelación (%)**|**Porcentaje respecto a modelación (%)**|**7,22%**|**0,53**|

_Fuente: Elaboración propia._

Tal como se puede observar en las tablas precedentes, lo obtenido por la modelación

presenta un máximo de 8,99% de MP 2,5 comparado con la normativa ambiental vigente.

38

Adenda N°1

Proyecto Modificación Barrio Los Pinares

Informe de Modelación Atmosférica

Dado que la concentración obtenida con la modelación de la emisión generada por la

operación del proyecto representa un bajo porcentaje (todos inferior a un 10%), tanto de

la condición basal evaluada y también la comparación con la normativa primaria de calidad

ambiental, se puede concluir que no se generará un impacto significativo sobre la calidad

del aire de las comunas que considera el proyecto.

**5.2.2.** **Evaluación discreta y dispersión de los niveles de concentración**

Tal como se menciona anteriormente, la concentración de MP 2,5 corresponde al mayor

valor emitido por el proyecto comparado con la normativa y con la condición basal de

calidad de aire del proyecto, por lo tanto a continuación se presenta el mapa de dispersión

de dicho compuesto . Con respecto a los resultados obtenidos en los puntos discretos, en la

Tabla 25 se presentan los valores de concentración obtenidos para cada uno de los

compuestos evaluados.

39

Adenda N°1

Proyecto Modificación Barrio Los Pinares

Informe de Modelación Atmosférica

**Figura 17. Iso-concentración de promedio anual de MP** **2,5** **sobre puntos discretos y área**

|de estudio.|Col2|Col3|Col4|
|---|---|---|---|
|||||
|**Consultor:**|**Carta:**|**Escala:**<br>|**Simbología**|
||ISO<br>CONCNETRACIÓN<br>PROMEDIO ANUAL<br>MP2,5|1:20.000|<br> <br>Modificación Barrio Los Pinares<br>Barrio Los Pinares<br>Receptores<br> <br> 1,2 μg/m3 <br> 1,0 μg/m3 <br> 0,8 μg/m3 <br> 0,5 μg/m3 <br> 0,3 μg/m3 <br> 0,1 μg/m3|
||ISO<br>CONCNETRACIÓN<br>PROMEDIO ANUAL<br>MP2,5|**Proyección:**|**Proyección:**|
||ISO<br>CONCNETRACIÓN<br>PROMEDIO ANUAL<br>MP2,5|WGS 84 UTM H19S|WGS 84 UTM H19S|

_Fuente: Elaboración propia._

40

Adenda N°1

Proyecto Modificación Barrio Los Pinares

Informe de Modelación Atmosférica

**Tabla 25. Concentración de MP** **2,5** **en receptores discretos.**

|Punto|Prom<br>anual<br>MP<br>10|P98<br>diario<br>MP<br>10|Prom<br>anual<br>MP<br>2.5|P98<br>diario<br>MP<br>2.5|Prom<br>anual SO<br>2|P99<br>diario SO<br>2|P99,73<br>horario<br>SO<br>2|Prom<br>anual<br>NO<br>2|P99<br>horario<br>NO<br>2|P99 8<br>horas CO|P99<br>horario<br>CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|R1|1.76.E+00|4.49.E+00|1.55.E+00|3.95.E+00|7.55.E-05|1.93.E-04|9.01.E-04|1.20.E+00|3.07.E+00|3.33.E+01|1.58.E+02|
|R2|4.58.E-01|1.32.E+00|4.03.E-01|1.16.E+00|1.95.E-05|5.63.E-05|2.80.E-04|2.94.E-01|8.43.E-01|9.80.E+00|4.89.E+01|
|R3|1.70.E+00|3.13.E+00|1.50.E+00|2.75.E+00|7.30.E-05|1.34.E-04|5.72.E-04|1.17.E+00|2.15.E+00|2.32.E+01|1.00.E+02|
|R4|1.22.E+00|2.29.E+00|1.07.E+00|2.01.E+00|5.18.E-05|9.78.E-05|3.44.E-04|8.27.E-01|1.55.E+00|1.68.E+01|6.07.E+01|
|R5|7.39.E-01|2.36.E+00|6.50.E-01|2.07.E+00|3.15.E-05|9.99.E-05|2.83.E-04|4.89.E-01|1.55.E+00|1.77.E+01|5.01.E+01|
|R6|1.13.E+00|3.46.E+00|9.92.E-01|3.04.E+00|4.81.E-05|1.47.E-04|5.27.E-04|7.57.E-01|2.35.E+00|2.51.E+01|9.08.E+01|

_Fuente: Elaboración propia._

41

Adenda N°1

Proyecto Modificación Barrio Los Pinares

Informe de Modelación Atmosférica

**5.3.** **Área de influencia**

De acuerdo a los resultados obtenidos de la modelación de la dispersión de las emisiones,

se definió el área de influencia del proyecto como el alcance de la concentración anual de

MP 2,5, ya que se considera el compuesto con mayores concentraciones aportadas al área

en evaluación, y además representa el mayor porcentaje de superación de la normativa de

calidad de aire evaluada.

Finalmente, en la figura a continuación se presenta el área de influencia del proyecto para

el componente aire respecto a las emisiones atmosféricas generadas por él.

42

Adenda N°1

Proyecto Modificación Barrio Los Pinares

Informe de Modelación Atmosférica

|Figura 18. Área de influencia del proyecto, componente aire (emisiones atmosféricas)|Col2|Col3|Col4|
|---|---|---|---|
|||||
|**Consultor:**|**Carta:**|**Escala:**|**Simbología**|
||ÁREA DE INFLUENCIA|1:5.000|<br> <br>Modificación Barrio Los Pinares<br>Barrio Los Pinares<br>Receptores<br>Area de influencia|
||ÁREA DE INFLUENCIA|**Proyección**:|**Proyección**:|
||ÁREA DE INFLUENCIA|WGS 84 UTM H19S|WGS 84 UTM H19S|

_Fuente: Elaboración propia._

43

Adenda N°1

Proyecto Modificación Barrio Los Pinares

Informe de Modelación Atmosférica

**5.4.** **Consideraciones.**

La base de datos meteorológica y geográfica fue adquirida a una empresa especializada en

modelación para servicios de evaluación ambiental, la cual fue generada por medio del

software WRF, cumpliendo con las condiciones establecidas por el Servicio de Evaluación

Ambiental.

44

Adenda N°1

Proyecto Modificación Barrio Los Pinares

Informe de Modelación Atmosférica

**6.** **CONCLUSIÓN**

La ejecución del proyecto “Modificación Barrio Los Pinares” genera una cantidad

significativa de material particulado fino respirable, principalmente en su fase de operación

debido a la calefacción residencial de leña, tal como se puede verificar en el estudio de

emisiones atmosféricas adjunto en el Anexo X de la presente Adenda.

Para evaluar el impacto sobre la calidad del aire de la comuna de Rancagua y sobre la salud

de las personas generado por la emisión de material particulado y gases de combustión, se

realizó una modelación de dispersión atmosférica a través del software CALPUFF. La

modelación contempló un dominio de 74x74 km, que incluyó toda la información

meteorológica proporcionada por la base de datos construida a partir de modelación WRF.

La información utilizada para la evaluación del impacto generado por el proyecto

correspondió a los valores de concentraciones en distintos periodos de tiempo de un año

calendario de los compuestos como MP 10, MP 2,5, CO, NO 2 y SO 2 . Esto permitió evaluar los

niveles de concentración en toda el área de estudio con respecto a la norma primaria de

calidad ambiental y con la condición basal de la zona.

A partir de la modelación de dispersión atmosférica del material particulado y gases de

combustión generado por el proyecto se concluye que las concentraciones generadas por

éste son de baja magnitud y de bajo alcance, lo cual se puede verificar en la cartografía de

isolineas que representa la dispersión de MP 2,5 y adicionalmente en los receptores discretos

evaluados en el presente informe.

Adicionalmente se puede ver que en el escenario de operación se puede observar que los

mayores valores de concentración simulados tienden a acumularse hacia el suroeste

condiciéndose con el análisis meteorológico y geográfico de la zona.

Sobre el set de receptores evaluados se puede indicar que estos nos sufren de impactos

significativos ya que no se acercan a la latencia de la norma, ni a la concentración basal

evaluada.

Dado que la concentración obtenida con la modelación de la emisión generada por la

operación del proyecto “Modificación Barrio Los Pinares” representa un bajo porcentaje,

tanto de la condición basal de la comuna como de la normativa primaria de calidad

ambiental, y es de baja magnitud y alcance, se puede concluir que no se generará un

impacto significativo sobre la calidad del aire de Rancagua. Por lo tanto, se descarta un

riesgo para la salud de las personas bajo los términos establecidos en el literal a) del artículo

5 del Reglamento del Sistema de Evaluación de Impacto Ambiental (D.S. N°40/2013 del

MMA).

45

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Normas de Calidad del Aire Consideradas en el Estudio.****

| Parámetro | Tipo de<br>Norma | Estadístico | Valor de<br>referencia | Fuente |
| --- | --- | --- | --- | --- |
| MP10 | Primaria | Promedio del<br>periodo | 50 μg/m3N | D.S. N°45/02 MINSEGPRES |
| MP10 | Primaria | Percentil<br>98<br>Diario | 150 μg/m3N | D.S. N°59/98 MINSEGPRES |
| MP2,5 | Primaria | Promedio del<br>periodo | 20 μg/m3N | D.S. N°12/11 MMA |
| MP2,5 | Primaria | Percentil<br>98<br>Diario | 50 μg/m3N | D.S. N°12/11 MMA |
| SO2 | Primaria | Promedio del<br>periodo | 60 μg/m3N | D.S. N°104/18 MMA |
| SO2 | Primaria | Percentil<br>99<br>Diario | 150 μg/m3N | D.S. N°104/18 MMA |
| SO2 | Primaria | Percentil 98,5<br>Horario | 350 μg/m3N | D.S. N°104/18 MMA |
| NO2 | Primaria | Promedio del<br>periodo | 100 μg/m3N | D.S.<br>N°114/02<br>MINSEGPRES |
| NO2 | Primaria | Percentil<br>99<br>Horario | 400 μg/m3N | D.S.<br>N°114/02<br>MINSEGPRES |
| CO | Primaria | Percentil 99 8<br>horas | 1.000 μg/m3N | D.S.<br>N°115/02<br>MINSEGPRES |
| CO | Primaria | Percentil<br>99<br>Horario | 3.000 μg/m3N | D.S.<br>N°115/02<br>MINSEGPRES |

**Tabla 2.: Información general de la EMRP “Rancagua I”.****

| Estación | Rancagua I |
| --- | --- |
| Propietario | Ministerio del Medio Ambiente |
| Operador | Asesorías Algoritmos Ltda. |
| Región | del Libertador General Bernardo<br>O'Higgins |
| Provincia | Cachapoal |
| Comuna | Rancagua |
| Coordenadas UTM 19S | 342015 E |
| Coordenadas UTM 19S | 6218523 N |
| Recepción de datos | En línea |
| Inicio de operación | 2004-05-01 |
| Estado | Vigente |

**Tabla 3.: Concentración Media Anual de MP** **10** **(μg/m** **[3]** **N)****

| Estación | Norma Primaria de MP (D.S. No 59/98 MINSEGPRES)<br>10<br>- Media Anual | Col3 | Col4 | Trianual | Porcentaje de la<br>norma |
| --- | --- | --- | --- | --- | --- |
| **Estación** | **Valor Norma: 50 (μg/m3N)** | **Valor Norma: 50 (μg/m3N)** | **Valor Norma: 50 (μg/m3N)** | **Valor Norma: 50 (μg/m3N)** | **Valor Norma: 50 (μg/m3N)** |
| **Estación** | **Año** | **Año** | **Año** | **Año** | **Año** |
| **Estación** | **2017** | **2018** | **2019** | **2019** | **2019** |
| Rancagua I | 64,59 | 55,46 | 60,42 | 60,16 | 120% |

**Tabla 4.: Concentraciones 24 horas de MP** **10** **(μg/m** **[3]** **N).****

| Estación | Norma Primaria de MP10 (D.S. No 59/98 MINSEGPRES) - Percentil 98 24 Horas | Col3 | Col4 | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Estación** | **Valor Norma: 150 (μg/m3N)** | **Valor Norma: 150 (μg/m3N)** | **Valor Norma: 150 (μg/m3N)** | **Valor Norma: 150 (μg/m3N)** | **Valor Norma: 150 (μg/m3N)** | **Valor Norma: 150 (μg/m3N)** |
| **Estación** | **Año** | **Año** | **Año** | **Año** | **Año** | **Año** |
| **Estación** | **2017** | **2017** | **2018** | **2018** | **2019** | **2019** |
| **Estación** | **Valor** | **% Norma** | **Valor** | **% Norma** | **Valor** | **% Norma** |
| Rancagua I | 132,84 | 89% | 115,76 | 104% | 142,2 | 95% |

**Tabla 5.: Concentración Media Anual de MP** **2,5** **(μg/m** **[3]** **N).****

| Estación | Norma Primaria de MP (D.S. N° 12/2011 del MMA) -<br>2,5<br>Media Anual | Col3 | Col4 | Trianual | Porcentaje de la<br>norma |
| --- | --- | --- | --- | --- | --- |
| **Estación** | **Valor Norma: 20 (μg/m3N)** | **Valor Norma: 20 (μg/m3N)** | **Valor Norma: 20 (μg/m3N)** | **Valor Norma: 20 (μg/m3N)** | **Valor Norma: 20 (μg/m3N)** |
| **Estación** | **Año** | **Año** | **Año** | **Año** | **Año** |
| **Estación** | **2017** | **2018** | **2019** | **2019** | **2019** |
| Rancagua I | 23,58 | 21,79 | 24,81 | 23,38 | 117% |

**Tabla 6.: Concentraciones 24 horas de MP** **2,5** **(μg/m** **[3]** **N).****

| Estación | Norma Primaria de MP (D.S. N° 12/2011 del MMA) - Percentil 98 24 Horas<br>2,5 | Col3 | Col4 | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Estación** | **Valor Norma: 50 (μg/m3N)** | **Valor Norma: 50 (μg/m3N)** | **Valor Norma: 50 (μg/m3N)** | **Valor Norma: 50 (μg/m3N)** | **Valor Norma: 50 (μg/m3N)** | **Valor Norma: 50 (μg/m3N)** |
| **Estación** | **Año** | **Año** | **Año** | **Año** | **Año** | **Año** |
| **Estación** | **2017** | **2017** | **2018** | **2018** | **2019** | **2019** |
| **Estación** | **Valor** | **% Norma** | **Valor** | **% Norma** | **Valor** | **% Norma** |
| Rancagua I | 73 | 148% | 75,82 | 152% | 82 | 164% |

**Tabla 7.: Concentración Media Anual de NO** **2** **(μg/m** **[3]** **N).****

| Estación | Norma Primaria de NO2 (D.S. No 114/02 MINSEGPRES)<br>- Media Anual | Col3 | Col4 | Trianual | Porcentaje de la<br>norma |
| --- | --- | --- | --- | --- | --- |
| **Estación** | **Valor Norma: 100 (μg/m3N)** | **Valor Norma: 100 (μg/m3N)** | **Valor Norma: 100 (μg/m3N)** | **Valor Norma: 100 (μg/m3N)** | **Valor Norma: 100 (μg/m3N)** |
| **Estación** | **Año** | **Año** | **Año** | **Año** | **Año** |
| **Estación** | **2007** | **2008** | **2009** | **2009** | **2009** |
| Rancagua I | 21,86 | 17,34 | 21,08 | 20,09 | 20% |

**Tabla 8.: Concentraciones Percentil 99 Promedio Horario de NO** **2** **(μg/m** **[3]** **N).****

| Estación | Norma Primaria de NO2 (D.S. No 114/02 MINSEGPRES)<br>- Percentil 99 1 Hora | Col3 | Col4 | Trianual | Porcentaje de la<br>norma |
| --- | --- | --- | --- | --- | --- |
| **Estación** | **Valor Norma: 400 (μg/m3N)** | **Valor Norma: 400 (μg/m3N)** | **Valor Norma: 400 (μg/m3N)** | **Valor Norma: 400 (μg/m3N)** | **Valor Norma: 400 (μg/m3N)** |
| **Estación** | **Año** | **Año** | **Año** | **Año** | **Año** |
| **Estación** | **2007** | **2008** | **2009** | **2009** | **2009** |
| Rancagua I | 70,68 | 59,57 | 63,73 | 64,66 | 16,2% |

**Tabla 9.: Concentración Percentil 99 Horario de CO (μg/m** **[3]** **N).****

| Estación | Norma Primaria de CO (D.S. No 115/02 MINSEGPRES) -<br>Percentil 99 máximos diarios en 1 Hora | Col3 | Col4 | Trianual | Porcentaje de la<br>norma |
| --- | --- | --- | --- | --- | --- |
| **Estación** | **Valor Norma: 30.000 (μg/m3N)** | **Valor Norma: 30.000 (μg/m3N)** | **Valor Norma: 30.000 (μg/m3N)** | **Valor Norma: 30.000 (μg/m3N)** | **Valor Norma: 30.000 (μg/m3N)** |
| **Estación** | **Año** | **Año** | **Año** | **Año** | **Año** |
| **Estación** | **2017** | **2018** | **2019** | **2019** | **2019** |
| Rancagua I | 2713,65 | 1032,22 | 2836,39 | 2194,09 | 7% |

**Tabla 10.: Concentración Percentil 99 Promedio 8 Horas de CO (μg/m** **[3]** **N).****

| Estación | Norma Primaria de CO (D.S. No 115/02 MINSEGPRES) -<br>Percentil 99 máximos diarios en 8 Horas | Col3 | Col4 | Trianual | Porcentaje de la<br>norma |
| --- | --- | --- | --- | --- | --- |
| **Estación** | **Valor Norma: 10.000 (μg/m3N)** | **Valor Norma: 10.000 (μg/m3N)** | **Valor Norma: 10.000 (μg/m3N)** | **Valor Norma: 10.000 (μg/m3N)** | **Valor Norma: 10.000 (μg/m3N)** |
| **Estación** | **Año** | **Año** | **Año** | **Año** | **Año** |
| **Estación** | **2017** | **2018** | **2019** | **2019** | **2019** |
| Rancagua I | 3026,69 | 1038,52 | 3712,66 | 2592,62 | 26% |

**Tabla 11.: Concentración Media Anual de SO** **2** **(μg/m** **[3]** **N).****

| Estación | Norma Primaria de SO2 (D.S. No 104/18 MMA) -<br>Media Anual | Col3 | Col4 | Trianual | Porcentaje de la<br>norma |
| --- | --- | --- | --- | --- | --- |
| **Estación** | **Valor Norma: 60 (μg/m3N)** | **Valor Norma: 60 (μg/m3N)** | **Valor Norma: 60 (μg/m3N)** | **Valor Norma: 60 (μg/m3N)** | **Valor Norma: 60 (μg/m3N)** |
| **Estación** | **Año** | **Año** | **Año** | **Año** | **Año** |
| **Estación** | **2017** | **2018** | **2019** | **2019** | **2019** |
| Rancagua I | 4,23 | 9,92 | 4,55 | 6,23 | 10% |

**Tabla 12.: Concentración Percentil 99 Promedio Diario de SO** **2** **(μg/m** **[3]** **N).****

| Estación | Norma Primaria de SO2 (D.S. No 104/18 MMA) -<br>Percentil 99 24 Horas | Col3 | Col4 | Trianual | Porcentaje de la<br>norma |
| --- | --- | --- | --- | --- | --- |
| **Estación** | **Valor Norma: 150 (μg/m3N)** | **Valor Norma: 150 (μg/m3N)** | **Valor Norma: 150 (μg/m3N)** | **Valor Norma: 150 (μg/m3N)** | **Valor Norma: 150 (μg/m3N)** |
| **Estación** | **Año** | **Año** | **Año** | **Año** | **Año** |
| **Estación** | **2017** | **2018** | **2019** | **2019** | **2019** |
| Rancagua I | 10,44 | 16,00 | 14,52 | 13,65 | 9,10% |

**Tabla 13.: Concentración Percentil 98,5 1 Hora de SO** **2** **(μg/m** **[3]** **N).****

| Estación | Norma Primaria de SO2 (D.S. No 104/18 MMA) -<br>Percentil 98,5 1 Hora | Col3 | Col4 | Trianual | Porcentaje de la<br>norma |
| --- | --- | --- | --- | --- | --- |
| **Estación** | **Valor Norma: 350 (μg/m3N)** | **Valor Norma: 350 (μg/m3N)** | **Valor Norma: 350 (μg/m3N)** | **Valor Norma: 350 (μg/m3N)** | **Valor Norma: 350 (μg/m3N)** |
| **Estación** | **Año** | **Año** | **Año** | **Año** | **Año** |
| **Estación** | **2017** | **2018** | **2019** | **2019** | **2019** |
| Rancagua I | 9,1 | 20,4 | 6,5 | 12,0 | 4,46% |

**Tabla 14.: Precipitación y temperatura normal mensual, comuna de Rancagua.****

| Mes | Precipitación (mm) | Temperatura (°C) |
| --- | --- | --- |
| ENE | 0,0 | 21,0 |
| FEB | 0,0 | 20,3 |
| MAR | 0,0 | 18,0 |
| ABR | 5,0 | 13,8 |
| MAY | 4,0 | 10,4 |
| JUN | 13,0 | 8,6 |
| JUL | 5,0 | 7,9 |
| AGO | 25,0 | 9,4 |
| SEP | 11,0 | 11,5 |
| OCT | 4,0 | 14,3 |
| NOV | 0,0 | 17,1 |
| DIC | 0,0 | 19,7 |

**Tabla 15.: Coordenadas de vértices y centroide del dominio de Modelación WRF.****

| Vértice | Proyección UTM, Huso 19 Sur; Datum WGS-84 | Col3 |
| --- | --- | --- |
| **Vértice** | **Este (m)** | **Norte (m)** |
| Noroeste | 306999,29 | 6257280,76 |
| Noreste | 380068,05 | 6256135,48 |
| Suroeste | 305624,96 | 6185586,34 |
| Sureste | 377777,49 | 6183753,90 |
| Centroide | 342554,00 | 6220358,00 |

**Tabla 16.: Coordenadas de vértices y centroide del dominio de Modelación CALPUFF.****

| Vértice | Proyección UTM, Huso 19 Sur; Datum WGS-84 | Col3 |
| --- | --- | --- |
| **Vértice** | **Este (m)** | **Norte (m)** |
| Noroeste | 306999,29 | 6257280,76 |
| Noreste | 380068,05 | 6256135,48 |
| Suroeste | 305624,96 | 6185586,34 |
| Sureste | 377777,49 | 6183753,90 |
| Centroide | 342554,00 | 6220358,00 |

**Tabla 17.: Coordenadas de receptores discretos.****

| Punto | Coordenadas WGS 84 UTM 19S | Col3 | Distancia respecto al<br>proyecto (m) |
| --- | --- | --- | --- |
| **Punto** | **Este (m)** | **Norte (m)** | **Norte (m)** |
| R1 | 342250 | 6220015 | 114 |
| R2 | 341879 | 6220509 | 508 |
| R3 | 342462 | 6220705 | 90 |
| R4 | 343133 | 6221013 | 520 |
| R5 | 343581 | 6220504 | 709 |
| R6 | 343220 | 6219780 | 258 |

**Tabla 18.: Tasa de emisión.****

| Elemento | Tipo de<br>fuente | Superficie<br>polígono (m2) | Emisión<br>(t/año) | Tasa de<br>emisión<br>(t/m2/año) |
| --- | --- | --- | --- | --- |
| MP10 | Área | 404335,11 | 7,34 | 1,82E-05 |
| MP2,5 | Área | 404335,11 | 6,46 | 1,60E-05 |
| CO | Área | 404335,11 | 55,84 | 1,38E-04 |
| NO2 | Área | 404335,11 | 5,37 | 1,33E-05 |
| SO2 | Área | 404335,11 | 3.22.E-04 | 7,97E-10 |

**Tabla 19.: Coordenadas polígono de fuente de área.****

| Vértice | Proyección UTM, Huso 19 Sur; Datum WGS-84 | Col3 |
| --- | --- | --- |
| **Vértice** | **Este (m)** | **Norte (m)** |
| A | 342599 | 6220768 |
| B | 342247 | 6220150 |
| C | 342677 | 6219535 |
| D | 343183 | 6220271 |

**Tabla 20.: Evaluación de niveles de concentración para MP** **10** **.****

| Compuesto | Promedio del periodo<br>(μg/m3) | Promedio del periodo<br>EMRP (μg/m3) | Límite D.S. N°59/1998 del<br>MINSEGPRES (μg/m3) |
| --- | --- | --- | --- |
| MP10 | 2,05 | 60,16 | 50 |
| **Porcentaje respecto a modelación (%)** | **Porcentaje respecto a modelación (%)** | **3,40** | **4,09** |
| **Compuesto** | **Percentil 98 diario**<br>**modelación (μg/m3) ** | **Percentil 98 EMRP**<br>**(μg/m3) ** | **Límite D.S. N°59/1998 del**<br>**MINSEGPRES (μg/m3) ** |
| MP10 | 5,01 | 115,76 | 150 |
| **Porcentaje respecto a modelación (%)** | **Porcentaje respecto a modelación (%)** | **4,33** | **3,34** |

**Tabla 21.: Evaluación de niveles de concentración para MP** **2,5** **.****

| Compuesto | Promedio del periodo<br>(μg/m3) | Promedio del periodo<br>EMRP (μg/m3) | D.S. N°12/11 MMA<br>(μg/m3) |
| --- | --- | --- | --- |
| MP2,5 | 1,80 | 24,81 | 20 |
| **Porcentaje respecto a modelación (%)** | **Porcentaje respecto a modelación (%)** | **7,25** | **8,99** |
| **Compuesto** | **Percentil 98 diario**<br>**modelación (μg/m3) ** | **Percentil 98 EMRP**<br>**(μg/m3) ** | **D.S. N°12/11 MMA**<br>**(μg/m3)** |
| MP2,5 | 4,41 | 75,82 | 50 |
| **Porcentaje respecto a modelación (%)** | **Porcentaje respecto a modelación (%)** | **5,82** | **8,82** |

**Tabla 22.: Evaluación de niveles de concentración para NO** **2** **.****

| Compuesto | Promedio del periodo<br>(μg/m3) | Promedio del periodo<br>EMRP (μg/m3) | D.S. N°114/02<br>MINSEGPRES (μg/m3) |
| --- | --- | --- | --- |
| NO2 | 1,39 | 20,09 | 100 |
| **Porcentaje respecto a modelación (%)** | **Porcentaje respecto a modelación (%)** | **6,91** | **1,39** |
| **Compuesto** | **Percentil 99 horario**<br>**modelación (μg/m3) ** | **Percentil 99 horario**<br>**EMRP (μg/m3) ** | **D.S. N°114/02**<br>**MINSEGPRES (μg/m3) ** |
| NO2 | 3,38 | 64,66 | 400 |
| **Porcentaje respecto a modelación (%)** | **Porcentaje respecto a modelación (%)** | **5,23** | **0,85** |

**Tabla 23.: Evaluación de niveles de concentración para SO** **2** **.****

| Contaminante | Promedio del periodo<br>(μg/m3) | Promedio del periodo<br>EMRP (μg/m3) | D.S. N°104/18 MMA<br>(μg/m3) |
| --- | --- | --- | --- |
| SO2 | 0,00009 | 6,23 | 80 |
| **Porcentaje respecto a modelación (%)** | **Porcentaje respecto a modelación (%)** | **0,0014** | **0,0001** |
| **Compuesto** | **Percentil 99 Diario**<br>**(μg/m3) ** | **Percentil 99 Diario**<br>**EMRP (μg/m3) ** | **D.S. N°104/18 MMA**<br>**(μg/m3) ** |
| SO2 | 0,00021 | 13,65 | 250 |
| **Porcentaje respecto a modelación (%)** | **Porcentaje respecto a modelación (%)** | **0,002** | **0,0001** |
| **Compuesto** | **Percentil 98,5 Horario**<br>**modelación (μg/m3) ** | **Percentil 98,5 Horario**<br>**EMRP (μg/m3) ** | **D.S. N°104/18 MMA**<br>**(μg/m3) ** |
| SO2 | 0,0009 | 12 | 1000 |
| **Porcentaje respecto a modelación (%)** | **Porcentaje respecto a modelación (%)** | **0,01** | **0,0001** |

**Tabla 24.: Evaluación de niveles de concentración para CO.****

| Compuesto | Percentil 99 8 horas<br>(μg/m3) | Percentil 99 8 horas<br>EMRP (μg/m3) | D.S. N°115/02<br>MINSEGPRES (μg/m3) |
| --- | --- | --- | --- |
| CO | 37,09 | 2592,62 | 10000 |
| **Porcentaje respecto a modelación (%)** | **Porcentaje respecto a modelación (%)** | **1,43** | **0,37** |
| **Compuesto** | **Percentil 99 Horario**<br>**modelación (μg/m3) ** | **Percentil 99 Horario**<br>**EMRP (μg/m3) ** | **D.S. N°115/02**<br>**MINSEGPRES (μg/m3) ** |
| CO | 158,32 | 2194,09 | 30000 |
| **Porcentaje respecto a modelación (%)** | **Porcentaje respecto a modelación (%)** | **7,22%** | **0,53** |

**Tabla 25.: Concentración de MP** **2,5** **en receptores discretos.****

| Punto | Prom<br>anual<br>MP<br>10 | P98<br>diario<br>MP<br>10 | Prom<br>anual<br>MP<br>2.5 | P98<br>diario<br>MP<br>2.5 | Prom<br>anual SO<br>2 | P99<br>diario SO<br>2 | P99,73<br>horario<br>SO<br>2 | Prom<br>anual<br>NO<br>2 | P99<br>horario<br>NO<br>2 | P99 8<br>horas CO | P99<br>horario<br>CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R1 | 1.76.E+00 | 4.49.E+00 | 1.55.E+00 | 3.95.E+00 | 7.55.E-05 | 1.93.E-04 | 9.01.E-04 | 1.20.E+00 | 3.07.E+00 | 3.33.E+01 | 1.58.E+02 |
| R2 | 4.58.E-01 | 1.32.E+00 | 4.03.E-01 | 1.16.E+00 | 1.95.E-05 | 5.63.E-05 | 2.80.E-04 | 2.94.E-01 | 8.43.E-01 | 9.80.E+00 | 4.89.E+01 |
| R3 | 1.70.E+00 | 3.13.E+00 | 1.50.E+00 | 2.75.E+00 | 7.30.E-05 | 1.34.E-04 | 5.72.E-04 | 1.17.E+00 | 2.15.E+00 | 2.32.E+01 | 1.00.E+02 |
| R4 | 1.22.E+00 | 2.29.E+00 | 1.07.E+00 | 2.01.E+00 | 5.18.E-05 | 9.78.E-05 | 3.44.E-04 | 8.27.E-01 | 1.55.E+00 | 1.68.E+01 | 6.07.E+01 |
| R5 | 7.39.E-01 | 2.36.E+00 | 6.50.E-01 | 2.07.E+00 | 3.15.E-05 | 9.99.E-05 | 2.83.E-04 | 4.89.E-01 | 1.55.E+00 | 1.77.E+01 | 5.01.E+01 |
| R6 | 1.13.E+00 | 3.46.E+00 | 9.92.E-01 | 3.04.E+00 | 4.81.E-05 | 1.47.E-04 | 5.27.E-04 | 7.57.E-01 | 2.35.E+00 | 2.51.E+01 | 9.08.E+01 |
