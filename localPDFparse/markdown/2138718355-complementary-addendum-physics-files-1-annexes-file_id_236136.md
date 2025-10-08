---
title: Sin título
author: OHRE
date: D:20190531072758-04'00'
language: es
type: report
pages: 43
has_toc: True
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - 1. INTRODUCCIÓN El presente informe da cuenta de los resultados obtenidos de la modelación de dispersión de olores y
  - Tabla 1. Coordenadas representativas del proyecto.
  - 1 Extraído de la DIA original “Regularización bodega de vinos La Tablada”, Servicios y Gestiones Vitivinícolas Ltda., Marzo
  - 2. MODELACIÓN DE VARIABLES METEOROLÓGICAS
  - 2 The Weather Research & Forecasting Model, NCAR/UCAR, https://www.mmm.ucar.edu/weather-research-and
  - 3. EVALUACIÓN DE LA MODELACIÓN DE VARIABLES METEOROLÓGICAS Para someter a evaluación la modelación de variables meteorológicas, se han seleccionado dos
  - Figura 8. Evaluación de la magnitud del viento modelada y observada, se observa una correlación del
  - Respecto a la temperatura, tal como se presenta en la Figura 9, se puede ver una correlación del 90%,
  - Figura 9. Evaluación de la temperatura modelada y observada, se observa una correlación del 90%.
  - 4. MODELACIÓN DE DISPERSIÓN E IMPACTO EN LA CALIDAD DEL AIRE
  ... y 8 secciones más
-->

Modelación de

Dispersión e Impacto

por Olores

Bodega de Vinos La

Tablada

Santiago, Chile

febrero 2019

Revisión mayo 2019

Modelación de Dispersión e Impacto por Olores Bodega de Vinos La Tablada

**CONTENIDO**

1. INTRODUCCIÓN ................................................................................................ 2

2. MODELACIÓN DE VARIABLES METEOROLÓGICAS ................................................... 3

3. EVALUACIÓN DE LA MODELACIÓN DE VARIABLES METEOROLÓGICAS ..................... 11

4. MODELACIÓN DE DISPERSIÓN E IMPACTO EN LA CALIDAD DEL AIRE ....................... 19

5. FUENTES CONSIDERADAS Y RECEPTORES DISCRETOS DEFINIDOS ........................... 20

6. RESULTADOS DE LA DISPERSIÓN E IMPACTO POR OLORES .................................... 26

7. ANÁLISIS DE IMPACTO HORARIO EN RECEPTORES ................................................ 31

8. CONCLUSIONES .............................................................................................. 40

Página **1** de **42**

Modelación de Dispersión e Impacto por Olores Bodega de Vinos La Tablada

# 1. INTRODUCCIÓN El presente informe da cuenta de los resultados obtenidos de la modelación de dispersión de olores y

los impactos asociados al proyecto “Regularización bodega de vinos La Tablada”, en cumplimiento a

lo solicitado por el Servicio de Evaluación Ambiental por medio del Informe Consolidado de Solicitud
de Aclaraciones, Rectificaciones y/o Ampliaciones a la Declaración de Impacto Ambiental (ICSARA)

asociado al proyecto.

Las instalaciones del proyecto se ubican en el predio Reserva Cora N°1 (Proyecto de Parcelación Viena)

en la comuna de Río Claro, Provincia de Talca, VII Región del Maule. Se trata de un sector rural
conocido como Escudo de Chile, con presencia de actividades principalmente agrícolas. [1 ]

# Tabla 1. Coordenadas representativas del proyecto.

|Coordenadas UTM La Bodega|Col2|
|---|---|
|**Punto**|**Coordenadas Datum**<br>**WGS 84**|
|**La Bodega**|6.100.095 m N<br>283.678 m E|

La Bodega de Vinos La Tablada tiene su origen en el año 2009, cuando las primeras cubas de vinos se
construyeron sólo para almacenar caldos de vinos. El primer período de operación de la planta de
proceso vinificación ocurre durante la temporada 2013-14. Desde ese momento comienza el
procesamiento de uva en el mismo lugar, para la producción de vinos. [1 ]

____________________________________________________

# 1 Extraído de la DIA original “Regularización bodega de vinos La Tablada”, Servicios y Gestiones Vitivinícolas Ltda., Marzo

de 2018.

Página **2** de **42**

Modelación de Dispersión e Impacto por Olores Bodega de Vinos La Tablada

# 2. MODELACIÓN DE VARIABLES METEOROLÓGICAS

Para la generación de la base de datos de variables meteorológicas, se utilizó el modelo WRF versión
3.9.1. Éste es un modelo meteorológico de alta resolución, desarrollado para la simulación de variables

meteorológicas, mediante la resolución de las ecuaciones físicas que describen los movimientos de la

atmósfera, utilizando aproximaciones basadas en métodos numéricos. Este modelo se encuentra en

constante desarrollo y mejora por medio de una asociación colaborativa, principalmente entre el

National Center for Atmospheric Research (NCAR, USA), National Oceanic and Atmospheric

Administration (NCEP, USA), Forecast Systems Laboratory (FSL, USA), Air Force Weather Agency

(AFWA, USA), el Naval Research Laboratory, University of Oklahoma, y la Federal Aviation

Administration (FAA, USA). WRF es un Software Libre y comunitario, por lo que su desarrollo y

mejoramiento se realiza en distintos sitios alrededor del mundo por voluntarios que deseen contribuir
al proyecto [2] .

En el presente informe se utilizó la información meteorológica correspondiente al último año

meteorológico (2017). Esta información se obtuvo a partir del CISL Research Data Archive (NCAR, USA),

utilizándose el conjunto de datos de entrada ds083.2. NCAR (National Center for Atmospherical

Reseach) ofrece a los científicos de Estados Unidos y del mundo, una gran cantidad de herramientas,

desde modelos comunitarios hasta aviones de investigación, supercomputadores y talleres. Los

científicos internos de NCAR colaboran con sus colegas en el mundo académico, el gobierno y el sector

privado para construir, refinar y ampliar los recursos de la comunidad de NCAR para que sean lo más
relevantes y útiles posible. [3]

Para el área de influencia, la configuración del modelo WRF, comprendió la parametrización de

variables propias de los fenómenos de micro escala que inciden en la dispersión de los contaminantes,

esto es: parametrizaciones de microfísica de nubes, fenómenos radiativos, altura de la capa de mezcla

y fenómenos turbulentos causados por la orografía. En la Tabla 2 se detallan las configuraciones de

importancia con las cuales se ejecutó la modelación.

____________________________________________________

# 2 The Weather Research & Forecasting Model, NCAR/UCAR, https://www.mmm.ucar.edu/weather-research-and
[forecasting-model](https://www.mmm.ucar.edu/weather-research-and-forecasting-model) (Visitado en Diciembre de 2018).

3 National Center for Atmospheric Research, NCAR/UCAR, [https://ncar.ucar.edu/what-we-offer](https://ncar.ucar.edu/what-we-offer) (Visitado en Diciembre de

2018).

Página **3** de **42**

Modelación de Dispersión e Impacto por Olores Bodega de Vinos La Tablada

**Tabla 2.** Configuración física del modelo WRF 3.9.1, dominio más pequeño.

|Centro Latitud|-35,21888157686793|
|---|---|
|~~Centro Longitud~~<br>|~~-71,37672584819194~~<br>|
|~~Condiciones de entrada~~<br>|~~FNL DS083.2 2017~~<br>|
|~~Proyección cartográfica~~<br>|~~Mercator~~<br>|
|~~Puntos en X~~<br>|~~100~~<br>|
|~~Puntos en Y~~<br>|~~100~~<br>|
|~~Topografía~~<br>|~~SRTM3 (Aproximadamente 100 metros)~~<br>|
|~~Uso de suelo~~<br>|~~USGS (Aproximadamente 1 Kilómetro)~~<br>|
|~~Resolución horizontal (Km)~~<br>|~~0,1~~<br>|
|~~Resolución vertical (niveles)~~|~~27 niveles hasta 10 hPa~~<br>|
|Microfísica|~~“WRF Single-Moment 8-class scheme”.~~<br>Esquema microfísico de 8 clases, que<br>incorpora además de líquidos, hielo y<br>nieve. Parametrización ideal para<br>simulaciones a alta resolución.<br>|
|Radiación (Onda larga y Corta)|~~“RRTMG”. Esquema radiativo simple y~~<br>eficiente, capaz de simular los<br>fenómenos radiativos de onda larga a<br>través del solapamiento de capas<br>nubosas.<br>|
|Modelo de suelo|~~“ETA Similarity”. Esquema fenómenos~~<br>suelo-atmósfera ampliamente utilizado<br>por otros modelos numéricos además de<br>WRF, basado en Monin-Obukhov<br>(esquema requerido por el modelo de<br>dispersión) que incorpora la longitud de<br>rugosidad térmica Zilitinkevich y<br>funciones de similitud estándar desde<br>tablas predefinidas.<br>|
|Interacción suelo atmósfera|~~“Noah Land Surface Model”. Esquema~~<br>utilizado por NCEP/NCAR/AFWA que<br>incorpora temperatura y humedad del<br>suelo en cuatro capas.<br>|
|Capa planetaria|~~“Mellor-Yamada- Janjic”. Ampliamente~~<br>utilizado operacionalmente por otros<br>modelos además de WRF. Basado en un<br>régimen turbulento unidimensional de<br>energía cinética vertical local.|

Página **4** de **42**

Modelación de Dispersión e Impacto por Olores Bodega de Vinos La Tablada

El dominio más pequeño definido, considera una zona de 10x10 kilómetros, con un dominio

superior de 30x30 kilómetros y otro principal de 90x90 kilómetros, los que se consideran lo

suficientemente amplios como para incorporar fenómenos de escala sinóptica, propios de la zona

como los sistemas frontales o la incursión de altas frías migratorias, configurado además a una alta

resolución de 100 metros en su dominio más pequeño, con la capacidad de incorporar fenómenos

de mesoescala como oscilaciones en la capa altura de la mezcla por efecto radiativo o fenómenos

de intercambio turbulento causados por la orografía. En la Figura 1 y Figura 2 se presenta el

dominio considerado en la modelación.

**Figura 1.** Emplazamiento geográfico del dominio considerado para la modelación de variables
meteorológicas y de dispersión.

Página **5** de **42**

Modelación de Dispersión e Impacto por Olores Bodega de Vinos La Tablada

**Figura 2.** Detalle del dominio considerado para la modelación de variables meteorológicas y de
dispersión.

Página **6** de **42**

Modelación de Dispersión e Impacto por Olores Bodega de Vinos La Tablada

De este modo, se logró tener una base de datos de variables meteorológicas para el área de interés,

con resolución horizontal de 100x100 metros, 27 niveles de altitud llegando al tope de la atmósfera y

resolución temporal de una hora para todo 2017, información requerida como base por el modelo de

dispersión.

A continuación, en la Figura 3, Figura 4, Figura 5 y Figura 6 se muestran los campos de vientos

característicos de la zona para las estaciones del año cálidas durante el período diurno y el período

nocturno, como también los campos de vientos característicos de la zona para las estaciones del año

frías durante el período diurno y nocturno.

**Figura 3.** Campos de vientos durante el período diurno en estaciones cálidas. Se puede ver
claramente el efecto brisa valle-montaña. Se puede ver, además, que los vientos alcanzan en
promedio entre 2 a 3 m/s (7 a 11 Km/h).

Página **7** de **42**

Modelación de Dispersión e Impacto por Olores Bodega de Vinos La Tablada

**Figura 4.** Campos de vientos durante el período nocturno en estaciones cálidas. Se puede ver
claramente el sentido contrario del régimen de vientos respecto al día (efecto brisa montaña-valle).
Se puede ver, además, que los vientos alcanzan en promedio entre 1 a 1,5 m/s (3,6 a 5 Km/h).

Página **8** de **42**

Modelación de Dispersión e Impacto por Olores Bodega de Vinos La Tablada

**Figura 5.** Campos de vientos durante el período diurno en estaciones frías. Se puede ver, además,
que los vientos alcanzan en promedio entre 1 a 1,3 m/s (3,6 a 4,7 Km/h).

Página **9** de **42**

Modelación de Dispersión e Impacto por Olores Bodega de Vinos La Tablada

**Figura 6.** Campos de vientos durante el período nocturno en estaciones frías. Se puede ver alcanzan
en promedio entre 1 a 1,3 m/s (3,6 a 4,7 Km/h).

Página **10** de **42**

Modelación de Dispersión e Impacto por Olores Bodega de Vinos La Tablada

# 3. EVALUACIÓN DE LA MODELACIÓN DE VARIABLES METEOROLÓGICAS Para someter a evaluación la modelación de variables meteorológicas, se han seleccionado dos

estaciones próximas al emplazamiento del proyecto. Dichas estaciones corresponden a la Estación
Curicó y a la Estación Universidad de Talca, ambas con información pública en el portal SINCA. La
primera, a aproximadamente 30 kilómetros al Noreste del proyecto, y la segunda a 33 kilómetros al
suroeste aproximadamente, los datos de las estaciones se presentan en la Tabla 3 y Tabla 4.

|Tabla 3. Información d|de la estación Curicó.|
|---|---|
|Estación|Curicó|
|Propietario|Ministerio del Medio Ambiente|
|Operador|Asesorías Algoritmos Ltda.|
|Región|Del Maule|
|Provincia|Curicó|
|Comuna|Curicó|
|Coordenadas UTM|296068 E 6127456 N|
|Recepción de datos|En línea|
|Huso horario|19|
|Inicio de operación reportado|2012-06-22|

**Tabla 4.** Información de la estación Universidad de Talca.

|Estación|Universidad de Talca|
|---|---|
|Propietario|Ministerio del Medio Ambiente|
|Operador|Asesorías Algoritmos Ltda.|
|Región|Del Maule|
|Provincia|Talca|
|Comuna|Talca|
|Coordenadas UTM|260878 E 6078683 N|
|Recepción de datos|En línea|
|Huso horario|19|
|Inicio de operación reportado|2013-01-01|

Página **11** de **42**

Modelación de Dispersión e Impacto por Olores Bodega de Vinos La Tablada

El emplazamiento de las estaciones Curicó y Universidad de Talca respecto al proyecto a evaluar, se

presenta en la Figura 7.

**Figura 7.** Emplazamiento de las estaciones de monitoreo seleccionadas para la evaluación de la
modelación de variables meteorológicas.

En la Figura 8, Figura 9, Figura 10 y Figura 11 se presenta la evaluación para las variables de magnitud

del viento, temperatura, humedad y dirección del viento para la Estación Curicó. Respecto a la

magnitud del viento, se puede ver una correcta descripción del ciclo diario, subestimando ligeramente

en la madrugada y sobreestimando en horas de la tarde. La correlación es del 70%, dejando un 30%

de incertidumbre, la que será aplicada por defecto al resultado del modelo de dispersión, de manera

de representar el escenario más desfavorable de dispersión.

Página **12** de **42**

Modelación de Dispersión e Impacto por Olores Bodega de Vinos La Tablada

# Figura 8. Evaluación de la magnitud del viento modelada y observada, se observa una correlación del

70%.

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
||||||||||
||||||||||
||||||||||
||||||||||

2,4

2,2

2

1,8

1,6

1,4

1,2

1

Correlación, magnitud del viento modelado y observado

Estación SINCA Curicó

y = 0,718x + 0,3569

R2 = 0,7082

1 1,2 1,4 1,6 1,8 2 2,2 2,4 2,6 2,8

**Observado**

# Respecto a la temperatura, tal como se presenta en la Figura 9, se puede ver una correlación del 90%,

representando de manera adecuada el ciclo diario de esta variable.

# Figura 9. Evaluación de la temperatura modelada y observada, se observa una correlación del 90%.

Página **13** de **42**

Modelación de Dispersión e Impacto por Olores Bodega de Vinos La Tablada

Respecto a la humedad, tal como se presenta en la Figura 10, el ciclo diario se presenta de manera

adecuada subestimando ligeramente en horas de la madrugada y mañana, y sobreestimando

ligeramente en hora de la tarde, donde la correlación de los datos llega al 77%.

**Figura 10.** Evaluación de la humedad modelada y observada, se observa una correlación del 77%.

Correlación, humedad modelado y observado

Estación SINCA Curicó

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|||||||||
|||||||||
|||||||||
|||||||||
|||||||||
|||||||||
|||||||||

y = 1,0408x + 0,5119

1 R2 = 0,7714

40 45 50 55 60 65 70 75 80

**Observado**

91

81

71

61

51

41

31

21

11

En la **Figura 11**, se observa la comparación de la dirección del viento modelada y observada, se puede

ver una tendencia de magnificar la componente zonal del viento, causando una ligera rotación hacia

el oeste, cuando debería ser hacia el suroeste.

Página **14** de **42**

Modelación de Dispersión e Impacto por Olores Bodega de Vinos La Tablada

**Figura 11.** Evaluación de la dirección del viento modelada y observada, se puede ver una tendencia
de magnificar la componente zonal del viento, causando una ligera rotación hacia el oeste, cuando

debería ser hacia el suroeste.

En la Figura 12, Figura 13, Figura 14 y Figura 15 se presenta la evaluación para las variables de

magnitud del viento, temperatura, humedad y dirección del viento para la Estación Universidad de

Talca. Respecto a la magnitud del viento, se puede ver una correcta descripción del ciclo diario,

subestimando ligeramente en la madrugada y sobreestimando en horas de la tarde. La correlación es

del 86%, aun así, asumiendo el peor de los casos se asumirá la incertidumbre más alta que corresponde

a la encontrada para la Estación Curicó, que fue del 70%.

Página **15** de **42**

Modelación de Dispersión e Impacto por Olores Bodega de Vinos La Tablada

**Figura 12.** Evaluación de la magnitud del viento modelada y observada, se observa una correlación
superior al 86%.

Correlación, magnitud del viento modelado y observado

Estación SINCA Talca

1,4

1,2

1

2,4

2,2

2

1,8

1,6

y = 0,7943x + 0,2193

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
||||||||||
||||||||||
||||||||||
||||||||||
|||||||y =|0,7943x +|,2193|

R2 = 0,8672

1 1,2 1,4 1,6 1,8 2 2,2 2,4 2,6 2,8

**Observado**

Respecto a la temperatura, tal como se presenta en la Figura 13, se puede ver una correlación superior
al 85%, representando de manera adecuada el ciclo diario de esta variable.

**Figura 13.** Evaluación de la temperatura modelada y observada, se observa una correlación superior

al 85%.

Página **16** de **42**

Modelación de Dispersión e Impacto por Olores Bodega de Vinos La Tablada

Respecto a la humedad, tal como se presenta en la Figura 14, el ciclo diario se presenta de manera
adecuada subestimando ligeramente en horas de la madrugada y mañana, y sobreestimando
ligeramente en hora de la tarde, donde la correlación de los datos supera el 77%.

**Figura 14.** Evaluación de la humedad modelada y observada, se observa una correlación superior al

77%.

101

91

81

71

61

51

41

31

21

11

Correlación, humedad modelado y observado

Estación SINCA Curicó

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|||||||||
|||||||||
|||||||||
|||||||||
|||||||||
|||||||||
|||||||||
||||||y =|1,0111x +|11,559|

R2 = 0,7764
1

40 45 50 55 60 65 70 75 80

**Observado**

En la Figura 15, se observa la comparación de la dirección del viento modelada y observada, se puede

ver una predominancia de la componente sursuroeste tanto en las variables modeladas como en las

variables observadas.

Página **17** de **42**

Modelación de Dispersión e Impacto por Olores Bodega de Vinos La Tablada

**Figura 15.** Evaluación de la dirección del viento modelada y observada, se puede ver una tendencia
de magnificar ligeramente la componente zonal del viento, sin embargo, la componente
predominante se ve claramente del sursuroeste.

De este modo, se ha podido comprobar la efectividad de la modelación de variables meteorológicas y
su incertidumbre asociada que, en el peor de los casos, llega al 30%.

Página **18** de **42**

Modelación de Dispersión e Impacto por Olores Bodega de Vinos La Tablada

# 4. MODELACIÓN DE DISPERSIÓN E IMPACTO EN LA CALIDAD DEL AIRE

Para la presente modelación se han seguido los procedimientos establecidos por la “Guía

metodológica de uso de modelos de dispersión en el SEIA”, la cual recomienda el uso de CALPUFF

como modelo de dispersión de contaminantes. Para propósitos particulares de este estudio, se ha

utilizado la versión 6.4. CALPUFF es un modelo lagrangiano de dispersión de contaminantes basado

en un sistema de “puffs”, los cuales varían en su forma y posición en función del tiempo, del espacio,

la estabilidad atmosférica y los vientos, entre otros parámetros. Es un modelo que soporta múltiples

tipos de fuentes con diferentes tipos de tratamiento para cada una de ellas: Fuentes de área, fuentes
de volumen, fuentes puntuales y fuentes de línea [4] .

|Tabla 5. Configuración del do|ominio del modelo CALPUFF.|
|---|---|
|Centro UTM N (m)|283678|
|Centro UTM E (m)|6100095|
|Resolución espacial (m)|100|
|Puntos en X|100|
|Puntos en Y|100|
|Topografía|SRTM3 (Aproximadamente 100 metros de<br>resolución)|
|Uso de suelo|GLCC (USGS30 aproximadamente a 1 Kilómetro<br>e resolución)|

____________________________________________________

# 4 A User’s Guide for the CALPUFF Dispersion Model (Version 5), Earth Tech Inc., enero de 2000.

Página **19** de **42**

Modelación de Dispersión e Impacto por Olores Bodega de Vinos La Tablada

# 5. FUENTES CONSIDERADAS Y RECEPTORES DISCRETOS DEFINIDOS Para la modelación se consideraron 4 fuentes emisoras, descritas a continuación: Tabla 6 . Fuentes de olor consideradas para la modelación.

|Fuente de Olor|Tipo Fuente|Principales factores operacionales que<br>influyen en la generación de emisión de olor|Régimen<br>de Emisión<br>(horas/día)|
|---|---|---|---|
|Pozo de Riles<br>pequeño.|~~Unidad Abierta,~~<br>Fuente<br>Superficial<br>Pasiva.|~~Ubicado en la fase posterior al pozo de~~<br>recepción, de pequeñas dimensiones 3,1x2,1<br>metros<br>el<br>cual<br>recibe<br>los<br>riles<br>del<br>intercambiador de temperatura.<br>|24|
|Canaletas de<br>recolección de<br>Riles|Unidad Abierta,<br>Fuente<br>Superficial<br>Pasiva.|~~196x0,1 metros total de canaletas dispuestas~~<br>estratégicamente al interior de la zona de<br>procesos, las cuales cumplen la función de<br>recolectar los riles generados durante el<br>proceso de vinificación y las aguas de lavado,<br>las cuales son conducidas hacia la Planta de<br>riles.<br>|10|
|Planta de Riles|Unidad Abierta,<br>Fuente<br>Superficial<br>Pasiva.<br>|~~Ubicada al Oeste de las instalaciones, recibe el~~<br>total de los riles generados por el proceso,<br>como las aguas de lavado. Compuesta por 2<br>pozos con medidas de 3x3x3 metros con un<br>volumen total de 54m3 más un Filtro<br>parabólico. Consta de 3 fases, Pozo de<br>recepción<br>de<br>Riles,<br>Filtro<br>parabólico<br>(separación y remoción de Solidos) y el pozo<br>de<br>Homogenización,<br>al<br>finalizar<br>el<br>tratamiento, el ril es traslado mediante<br>bombeo al tranque con fines de regadío.<br>|<br>24|
|Batea de<br>Recepción de<br>Sólidos|~~Unidad Abierta,~~<br>Fuente<br>Superficial<br>Pasiva.|~~Se ubica justo debajo del filtro de prensa,~~<br>recibe los restos sólidos de la uva posterior al<br>proceso de prensado. Sus dimensiones son de<br>6 x 5 metros.|24|

Página **20** de **42**

Modelación de Dispersión e Impacto por Olores Bodega de Vinos La Tablada

Respecto del tranque de regadío y su actividad asociada (riego de avellanos), no se consideró como

actividad generadora de olores, y, por lo tanto, no se incluyó en la modelación, por las siguientes

razones:

**Tabla 7. Generación de RIL mensual.**

No fueron considerados como fuentes de olor el tranque de riego, ni el riego de avellanos, ya que la
cantidad de agua necesaria para regar el campo de avellanos durante un año es de 246.800 m [3] y
cantidad de Ril generado en un año de funcionamiento del proyecto es de (1154 m [3] ) el que es marginal
versus la cantidad de agua de riego del Canal Maule con el que se mezcla y es necesario para poder
regar el campo de avellanos (40 hectáreas) que es equivalente a (6170 m3 por hectáreas/año).

De lo que anterior se estima que el Ril está diluido 214 veces, por lo que se debería considerar que, en
la práctica, el riego se realiza solo con agua.

Página **21** de **42**

Modelación de Dispersión e Impacto por Olores Bodega de Vinos La Tablada

# Figura 16 . Ubicación de las fuentes de emisión.

Las fuentes fueron seleccionadas mediante una visita a terreno por parte de panelistas expertos en

monitoreo de olores, considerando que se trata de fuentes abiertas al medio ambiente, por lo que
están en constante emisión. Por tratarse de fuentes de emisiones fugitivas y/o difusas, fueron

consideras individualmente como fuentes de área, para fines de la modelación.

Para la presente modelación se utilizaron datos de tasas de emisión existentes para actividades
similares a las del presente proyecto (elaboración de vino). En particular, los datos utilizados
corresponden a dos estudios:

 - Estudio de generación de olores en Viña Concha y Toro - Planta Lontué [6] .
 - Estudio de dispersión de olores en las dependencias de Viña Concha y Toro [7] .

En ambos estudios mencionados anteriormente, se realizaron mediciones de acuerdo a lo indicado en

la Norma Chilena 3190:2010 “Calidad del aire - Determinación de la concentración de olor por

olfatometría dinámica” y Norma Chilena 3386:2015 “Muestreo estático para olfatometría”, que dan

cuenta de la metodología y procedimientos adecuados para la toma de muestra y determinación de

su concentración.

Página **22** de **42**

Modelación de Dispersión e Impacto por Olores Bodega de Vinos La Tablada

Se utilizaron datos ya existentes en consideración a las pequeñas dimensiones del proyecto en

evaluación, que no justificaban económicamente la realización de nuevas mediciones. Por otra parte,

“la evaluación ambiental debe enfocarse en los impactos relevantes de cada proyecto o actividad. En

este sentido, la necesidad de realizar una simulación de la calidad del aire debe responder a la

posibilidad de que el proyecto genere un impacto de relevancia sobre la calidad del aire, la salud de

las personas u otro componente del medio ambiente. Lo anterior debe analizarse caso a caso

considerando, entre otros, la magnitud y duración de las emisiones, especialmente cuando se trata de
actividades temporales y de impacto acotado” [8] . Debido a las pequeñas dimensiones del proyecto y las

características de la actividad desarrollada, marcada por un fuerte componente estacional (asociado

al tiempo de cosecha de la uva o vendimia, habitualmente entre los meses de Febrero y Mayo, lo que

permite inferir que el impacto por potenciales emisiones se concentrará en este periodo y no durante

todo el año), permiten justificar el uso de información existente con anterioridad.

Los valores de emisión utilizados se muestran en la Tabla 8.

<!-- INICIO TABLA 8 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- todo el año), permiten justificar el uso de información existente con anterioridad. Los valores de emisión utilizados se muestran en la Tabla 8. -->

**Tabla 8: ** . Tasas de emisión.**

| Fuente | Área (m2) | Tasa de Emisión<br>(Uo*m2/s) | Tasa de Emisión<br>Total (Uo/s) |
| --- | --- | --- | --- |
| ~~Pozo de Riles pequeño~~<br> | ~~6,5~~<br> | ~~0,66~~<br> | ~~**4,29**~~<br> |
| ~~Canaletas~~<br> | ~~19,6~~<br> | ~~0,66~~<br> | ~~**12,94**~~<br> |
| ~~Planta de Riles~~<br> | ~~18,0~~<br> | ~~0,66~~<br> | ~~**11,88**~~<br> |
| ~~Batea de Recepción de Sólidos~~<br> | ~~30,0~~ | ~~0,004~~ | ~~**0,12**~~ |

<!-- Estadísticas: 4 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- __________________________________________________ 6 El estudio forma parte de la Declaración de Impacto Ambiental “ _Proyecto de Mejoramiento y Ampliación Bodega, Planta_ -->
<!-- FIN TABLA 8 -->


**Tabla 8** . Tasas de emisión.

|Fuente|Área (m2)|Tasa de Emisión<br>(Uo*m2/s)|Tasa de Emisión<br>Total (Uo/s)|
|---|---|---|---|
|~~Pozo de Riles pequeño~~<br>|~~6,5~~<br>|~~0,66~~<br>|~~**4,29**~~<br>|
|~~Canaletas~~<br>|~~19,6~~<br>|~~0,66~~<br>|~~**12,94**~~<br>|
|~~Planta de Riles~~<br>|~~18,0~~<br>|~~0,66~~<br>|~~**11,88**~~<br>|
|~~Batea de Recepción de Sólidos~~<br>|~~30,0~~|~~0,004~~|~~**0,12**~~|

__________________________________________________

6 El estudio forma parte de la Declaración de Impacto Ambiental “ _Proyecto de Mejoramiento y Ampliación Bodega, Planta_

_y Sistema de Tratamiento de RILES”._ Elaborado por ANAM, octubre de 2015.

7 El estudio forma parte de la Declaración de Impacto Ambiental “ _Proyecto Modificación de Sistema de Manejo de RILES y_
_Continuidad Operacional de Bodega de Vinos Chimbarongo”._ Elaborado por ANAM, septiembre de 2016.

8 Guía para el uso de modelos de calidad del aire en el SEIA, Servicio de Evaluación Ambiental, 2012.

Página **23** de **42**

Modelación de Dispersión e Impacto por Olores Bodega de Vinos La Tablada

Respecto a los receptores definidos, se consideraron 8 receptores discretos alrededor del proyecto,

tal como lo muestra la Figura 17.

**Figura 17.** Receptores definidos dentro del dominio de modelación.

Página **24** de **42**

Modelación de Dispersión e Impacto por Olores Bodega de Vinos La Tablada

La ubicación de los receptores definidos, se presenta en la Tabla 9.

<!-- INICIO TABLA 9 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Modelación de Dispersión e Impacto por Olores Bodega de Vinos La Tablada La ubicación de los receptores definidos, se presenta en la Tabla 9. -->

**Tabla 9: ** . Ubicación de los receptores discretos definidos dentro del dominio de la modelación.**

| Punto | Receptor | UTM E<br>(m) | UTM N<br>(m) | Altitud (m) | Altura<br>(m) | Distancia<br>desde la<br>fuente (m) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Propietario del Proyecto | 283637 | 6100218 | 220,99 | 2 | 125 |
| 2 | Vecino 2 al NE del proyecto | 283872 | 6100362 | 223,54 | 2 | 325 |
| 3 | Vecino 3 al E del Proyecto | 284028 | 6100052 | 223,8 | 2 | 350 |
| 4 | Vecino 4 al S del Proyecto | 283693 | 6099905 | 221,62 | 2 | 195 |
| 5 | Vecino 5 al S del Proyecto | 283644 | 6099913 | 221,08 | 2 | 190 |
| 6 | Vecino 6 al SSO del Proyecto | 283616 | 6099969 | 220,93 | 2 | 145 |
| 7 | Vecino 7 al SSO del Proyecto | 283590 | 6099935 | 220,71 | 2 | 185 |
| 8 <br> | Vecino 8 AL SO del Proyecto | 283549 | 6099904 | 220,42 | 2 | 235 |

<!-- Estadísticas: 8 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- Para la determinación de los receptores, se tomó en cuenta la presencia de casas y viviendas cercanas al proyecto, ya que en estas se concentra la población susceptible de ser afectada por potenciales -->
<!-- FIN TABLA 9 -->


**Tabla 9** . Ubicación de los receptores discretos definidos dentro del dominio de la modelación.

|Punto|Receptor|UTM E<br>(m)|UTM N<br>(m)|Altitud (m)|Altura<br>(m)|Distancia<br>desde la<br>fuente (m)|
|---|---|---|---|---|---|---|
|1|Propietario del Proyecto|283637|6100218|220,99|2|125|
|2|Vecino 2 al NE del proyecto|283872|6100362|223,54|2|325|
|3|Vecino 3 al E del Proyecto|284028|6100052|223,8|2|350|
|4|Vecino 4 al S del Proyecto|283693|6099905|221,62|2|195|
|5|Vecino 5 al S del Proyecto|283644|6099913|221,08|2|190|
|6|Vecino 6 al SSO del Proyecto|283616|6099969|220,93|2|145|
|7|Vecino 7 al SSO del Proyecto|283590|6099935|220,71|2|185|
|8 <br>|Vecino 8 AL SO del Proyecto|283549|6099904|220,42|2|235|

Para la determinación de los receptores, se tomó en cuenta la presencia de casas y viviendas cercanas

al proyecto, ya que en estas se concentra la población susceptible de ser afectada por potenciales

emisiones de malos olores. Al tratarse de una zona rural y principalmente de actividades agrícolas, la

densidad poblacional del sector puede considerarse como baja, lo que reduce la cantidad de

potenciales afectados. Para la distancia entre los receptores y la fuente, se consideró la distancia en

línea recta entre el punto central del proyecto y la coordenada del receptor.

Página **25** de **42**

Modelación de Dispersión e Impacto por Olores Bodega de Vinos La Tablada

# 6. RESULTADOS DE LA DISPERSIÓN E IMPACTO POR OLORES

A continuación, se presentan los resultados obtenidos para la modelación de olores correspondiente

al proyecto en evaluación.

La Figura 18 corresponde a una vista general de todo el dominio considerado, se puede apreciar que

el impacto por olores queda confinado dentro de un área muy próxima al emplazamiento del proyecto.

**Figura 18.** Vista general de todo el dominio considerado y el impacto por olores (100% de la
Modelación).

Página **26** de **42**

Modelación de Dispersión e Impacto por Olores Bodega de Vinos La Tablada

En la Figura 19, se presenta una vista en detalle de la zona donde se confina el impacto por olores, se
ha establecido como condición de corte el valor de las 0,05 Uo/m [3], puesto que este valor en la práctica

se considera totalmente imperceptible por el ser humano.

**Figura 19.** Mapa de dispersión de las Unidades de Olor, valor máximo horario del día (100 % de

la modelación).

Página **27** de **42**

Modelación de Dispersión e Impacto por Olores Bodega de Vinos La Tablada

**Figura 20** . Área de Influencia del proyecto con respecto a olores según resultados de la modelación

(Percentil 98 del promedio horario anual)

Página **28** de **42**

Modelación de Dispersión e Impacto por Olores Bodega de Vinos La Tablada

**Figura 21** . Detalle del área de influencia.

Como criterio para determinar el área de influencia se utiliza la isodora de 1 UO E, que corresponde al
umbral de detección del olor compuesto [9] . Sin embargo, considerando el percentil 98 aplicado al

promedio horario para un año de modelación, se puede observar que el máximo valor obtenido
asciende a 0,3 Uo/m [3], y que el área de influencia queda acotada a los límites del proyecto, sin afectar

a ninguno de los receptores discretos definidos para la modelación.

____________________________________________________

9 Guía para la predicción y evaluación de impactos por olor en el SEIA, Servicio de Evaluación Ambiental (SEA),

2017.

Página **29** de **42**

Modelación de Dispersión e Impacto por Olores Bodega de Vinos La Tablada

En la Tabla 10 se presenta un detalle de los máximos valores promedio horarios entregados por la

modelación para cada receptor discreto definido, junto a los valores obtenidos para el Punto de

Máximo Impacto. Estos datos reafirman lo mencionado anteriormente, en el sentido de que la
inmisión en los receptores discretos definidos está muy por debajo del valor 1 Uo/m [3] e incluso del

valor máximo obtenido; se confirma que todos los receptores quedan fuera del área de influencia.

**Tabla 10** . Valores de UO/m [3] para cada uno de los receptores discretos definidos. (P 98-Horario )

|Receptor|Concentración de<br>Olor P -Horario<br>98<br>(Uo/m3)|
|---|---|
|~~Propietario del~~<br>Proyecto<br>|0,07|
|~~Vecino 2 al NE del~~<br>proyecto<br>|0,04|
|~~Vecino 3 al E del~~<br>Proyecto<br>|0,00|
|~~Vecino 4 al S del~~<br>Proyecto<br>|0,04|
|~~Vecino 5 al S del~~<br>Proyecto<br>|0,04|
|~~Vecino 6 al SSO del~~<br>Proyecto<br>|0,06|
|~~Vecino 7 al SSO del~~<br>Proyecto<br>|0,05|
|~~Vecino 8 AL SO del~~<br>Proyecto<br>|0,00|
|~~Punto de Máximo~~<br>Impacto|0,30|

Página **30** de **42**

Modelación de Dispersión e Impacto por Olores Bodega de Vinos La Tablada

# 7. ANÁLISIS DE IMPACTO HORARIO EN RECEPTORES

Al realizar el análisis a nivel horario, considerando el impacto de sustancias odorantes con valor de
1 Uo/m [3], las horas de impacto en cada receptor discreto definido da como resultado cero, puesto que

en todas las horas del año el impacto por sustancias odorantes está por debajo de este umbral. De

este modo, **para poder identificar horas de exposición a sustancias odorantes, se rebajó el umbral a**
**0,5 Uo/m** **[3]**, con lo que se estableció que el receptor más impactado corresponde a “Vecino 4 al S del

Proyecto” con 2 horas al año que superan dicho umbral durante el mes de agosto alrededor de las

4:00 h (AM), secundariamente el receptor denominado “Vecino 5 al S del Proyecto”, presenta un

impacto de olor durante una hora al año alrededor de las 5:00 h (AM) durante el mismo mes. Siendo

estos los únicos receptores discretos que perciben olor de acuerdo a Modelación de Olores.

Es importante destacar que se realiza este análisis con fines ilustrativos, puesto que el valor de 0,5
Uo/m [3] es considerado prácticamente imperceptible.

# A continuación, se presenta de manera gráfica, un análisis de cada uno de los receptores discretos

considerados en la modelación, se presentan las unidades de olor, hora a hora para todo el año 2017,
luego el ciclo diario de manera de identificar las horas de mayor impacto y posteriormente el ciclo
anual para identificar los meses del año de mayor impacto en unidades de olor, en todos los casos, no
se logra llegar al umbral detectable de 1 unidad de olor.

# Según esta información entregada por la modelación, el mayor impacto se produciría en horas de la

madrugada principalmente, como puede apreciarse en el comportamiento diario para cada uno de los
receptores. Respecto del ciclo anual, se observa una mayor heterogeneidad, atribuible a la

estacionalidad.

Página **31** de **42**

Modelación de Dispersión e Impacto por Olores Bodega de Vinos La Tablada

Figuras 22, 23 y 24 . Impacto Horario Anual, Ciclo Diario y Ciclo Anual en Receptor 1, Propietario del

Proyecto.

Página **32** de **42**

Modelación de Dispersión e Impacto por Olores Bodega de Vinos La Tablada

Figuras 25, 26 y 27 . Impacto Horario Anual, Ciclo Diario y Ciclo Anual en Receptor 2, Vecino 2 al NE del

Proyecto.

Página **33** de **42**

Modelación de Dispersión e Impacto por Olores Bodega de Vinos La Tablada

Figuras 28, 29 y 30 . Impacto Horario Anual, Ciclo Diario y Ciclo Anual en Receptor 3, Vecino 3 al E del

Proyecto.

Página **34** de **42**

Modelación de Dispersión e Impacto por Olores Bodega de Vinos La Tablada

Figuras 31, 32 y 33 . Impacto Horario Anual, Ciclo Diario y Ciclo Anual en Receptor 4, Vecino 4 al S del

Proyecto.

Página **35** de **42**

Modelación de Dispersión e Impacto por Olores Bodega de Vinos La Tablada

Figuras 34, 35 y 36 . Impacto Horario Anual, Ciclo Diario y Ciclo Anual en Receptor 5, Vecino 5 al S del

Proyecto.

Página **36** de **42**

Modelación de Dispersión e Impacto por Olores Bodega de Vinos La Tablada

Figuras 37, 38 y 39 . Impacto Horario Anual, Ciclo Diario y Ciclo Anual en Receptor 6, Vecino 6 al SSO del

Proyecto.

Página **37** de **42**

Modelación de Dispersión e Impacto por Olores Bodega de Vinos La Tablada

Figuras 40, 41 y 42 . Impacto Horario Anual, Ciclo Diario y Ciclo Anual en Receptor 7, Vecino 7 al SSO del

Proyecto.

Página **38** de **42**

Modelación de Dispersión e Impacto por Olores Bodega de Vinos La Tablada

Figuras 43, 44 y 45 . Impacto Horario Anual, Ciclo Diario y Ciclo Anual en Receptor 8, Vecino 8 al SO del

Proyecto.

Página **39** de **42**

Modelación de Dispersión e Impacto por Olores Bodega de Vinos La Tablada

# 8. CONCLUSIONES

En conclusión, se puede observar que la dispersión e impacto por olores queda confinada a la zona

circundante muy próxima al emplazamiento del proyecto, prácticamente en los límites del mismo

(considerando el percentil 98 de los promedios horarios anuales), disminuyendo rápidamente su

inmisión conforme aumenta la distancia desde él.

Además, los valores de concentración en cada uno de los receptores sensibles más próximos definidos
se encuentran por debajo del valor 1 Uo/m [3] . A modo de referencia, se cita la Guía Técnica Preliminar
“Horizontal Guidance for Odour Part 1 - Regulation and Permitting” [10] de la Integrated Pollution

Prevention and Control (IPPC), mecanismo regulatorio medioambiental de la Unión Europea, propone

los siguientes criterios de inmisión según el tipo de actividad:

**Tabla 11.** Valores de inmisión según actividad, IPPC.

|Ofensividad<br>Relativa del<br>Olor|Criterio de inmisión<br>asociado (Percentil<br>98 de los promedios<br>horario anuales)|Tipo de Actividad Relacionada|
|---|---|---|
|ALTA|1,5 Uo/m3|Actividades que involucren basura putrescible<br>Procesos que involucren a restos de animales y pescados<br>Cementeras y cerámicas<br>Procesos lácteos<br>Procesamiento de grasas y aceites<br>Tratamiento de aguas residuales<br>Refino de petróleo<br>Producción de comida para animales|
|MEDIA|3 Uo/m3|Procesos de comida para engorde<br>Procesos de la remolacha<br>Ganadería intensiva|
|BAJA|6 Uo/m3|Fabricación de chocolate/cacao.<br>Cervecerías.<br>Confiterías.<br>Producción de aromas y fragancias.<br>Tostado de café.<br>Panaderías<br>|

____________________________________________________
10 Horizontal Guidance for Odour Part 1 - Regulation and Permitting. Scotish Environment Prevention Agency/Environment
and Heritage Service/UK Environmet Agency. 2002. [https://olores.mma.gob.cl/wp-](https://olores.mma.gob.cl/wp-content/uploads/2019/03/Integrated-Pollution-Prevention-and-Control-part1.pdf)
[content/uploads/2019/03/Integrated-Pollution-Prevention-and-Control-part1.pdf](https://olores.mma.gob.cl/wp-content/uploads/2019/03/Integrated-Pollution-Prevention-and-Control-part1.pdf)

Página **40** de **42**

Modelación de Dispersión e Impacto por Olores Bodega de Vinos La Tablada

Para el presente estudio, los valores obtenidos para el Percentil 98 de los promedios horarios en un

año, en los receptores propuestos, se encuentran muy por debajo de los criterios presentados en esta

guía, incluso también para el punto de máximo impacto.

Por último, la localidad poblada más cercana, Camarico, situada a 4 kilómetros al OSO de la bodega,

no se ve afectada en forma alguna por las emisiones del proyecto, según los resultados de la

modelación.

Por todo lo anterior, se concluye que el presente proyecto no genera impactos significativos para el

medio ambiente ni las personas en relación a emisión de olores molestos, ya que sus niveles de

emisión se encuentran por debajo de lo detectable por un panel experto y muy por debajo en

comparación con normativa internacional vigente relacionada.

Página **41** de **42**

Modelación de Dispersión e Impacto por Olores Bodega de Vinos La Tablada

**www.essconsultores.cl**

**La Capitanía 80, Oficina 108, Las Condes**
**Santiago, Chile**

**+562 23034022**

**+569 82234583**

Página **42** de **42**

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 2.: ** Configuración física del modelo WRF 3.9.1, dominio más pequeño.**

| Centro Latitud | -35,21888157686793 |
| --- | --- |
| ~~Centro Longitud~~<br> | ~~-71,37672584819194~~<br> |
| ~~Condiciones de entrada~~<br> | ~~FNL DS083.2 2017~~<br> |
| ~~Proyección cartográfica~~<br> | ~~Mercator~~<br> |
| ~~Puntos en X~~<br> | ~~100~~<br> |
| ~~Puntos en Y~~<br> | ~~100~~<br> |
| ~~Topografía~~<br> | ~~SRTM3 (Aproximadamente 100 metros)~~<br> |
| ~~Uso de suelo~~<br> | ~~USGS (Aproximadamente 1 Kilómetro)~~<br> |
| ~~Resolución horizontal (Km)~~<br> | ~~0,1~~<br> |
| ~~Resolución vertical (niveles)~~ | ~~27 niveles hasta 10 hPa~~<br> |
| Microfísica | ~~“WRF Single-Moment 8-class scheme”.~~<br>Esquema microfísico de 8 clases, que<br>incorpora además de líquidos, hielo y<br>nieve. Parametrización ideal para<br>simulaciones a alta resolución.<br> |
| Radiación (Onda larga y Corta) | ~~“RRTMG”. Esquema radiativo simple y~~<br>eficiente, capaz de simular los<br>fenómenos radiativos de onda larga a<br>través del solapamiento de capas<br>nubosas.<br> |
| Modelo de suelo | ~~“ETA Similarity”. Esquema fenómenos~~<br>suelo-atmósfera ampliamente utilizado<br>por otros modelos numéricos además de<br>WRF, basado en Monin-Obukhov<br>(esquema requerido por el modelo de<br>dispersión) que incorpora la longitud de<br>rugosidad térmica Zilitinkevich y<br>funciones de similitud estándar desde<br>tablas predefinidas.<br> |
| Interacción suelo atmósfera | ~~“Noah Land Surface Model”. Esquema~~<br>utilizado por NCEP/NCAR/AFWA que<br>incorpora temperatura y humedad del<br>suelo en cuatro capas.<br> |
| Capa planetaria | ~~“Mellor-Yamada- Janjic”. Ampliamente~~<br>utilizado operacionalmente por otros<br>modelos además de WRF. Basado en un<br>régimen turbulento unidimensional de<br>energía cinética vertical local. |

**Tabla 4.: ** Información de la estación Universidad de Talca.**

| Estación | Universidad de Talca |
| --- | --- |
| Propietario | Ministerio del Medio Ambiente |
| Operador | Asesorías Algoritmos Ltda. |
| Región | Del Maule |
| Provincia | Talca |
| Comuna | Talca |
| Coordenadas UTM | 260878 E 6078683 N |
| Recepción de datos | En línea |
| Huso horario | 19 |
| Inicio de operación reportado | 2013-01-01 |

**Tabla 10: ** . Valores de UO/m [3] para cada uno de los receptores discretos definidos. (P 98-Horario )**

| Receptor | Concentración de<br>Olor P -Horario<br>98<br>(Uo/m3) |
| --- | --- |
| ~~Propietario del~~<br>Proyecto<br> | 0,07 |
| ~~Vecino 2 al NE del~~<br>proyecto<br> | 0,04 |
| ~~Vecino 3 al E del~~<br>Proyecto<br> | 0,00 |
| ~~Vecino 4 al S del~~<br>Proyecto<br> | 0,04 |
| ~~Vecino 5 al S del~~<br>Proyecto<br> | 0,04 |
| ~~Vecino 6 al SSO del~~<br>Proyecto<br> | 0,06 |
| ~~Vecino 7 al SSO del~~<br>Proyecto<br> | 0,05 |
| ~~Vecino 8 AL SO del~~<br>Proyecto<br> | 0,00 |
| ~~Punto de Máximo~~<br>Impacto | 0,30 |

**Tabla 11.: ** Valores de inmisión según actividad, IPPC.**

| Ofensividad<br>Relativa del<br>Olor | Criterio de inmisión<br>asociado (Percentil<br>98 de los promedios<br>horario anuales) | Tipo de Actividad Relacionada |
| --- | --- | --- |
| ALTA | 1,5 Uo/m3 | Actividades que involucren basura putrescible<br>Procesos que involucren a restos de animales y pescados<br>Cementeras y cerámicas<br>Procesos lácteos<br>Procesamiento de grasas y aceites<br>Tratamiento de aguas residuales<br>Refino de petróleo<br>Producción de comida para animales |
| MEDIA | 3 Uo/m3 | Procesos de comida para engorde<br>Procesos de la remolacha<br>Ganadería intensiva |
| BAJA | 6 Uo/m3 | Fabricación de chocolate/cacao.<br>Cervecerías.<br>Confiterías.<br>Producción de aromas y fragancias.<br>Tostado de café.<br>Panaderías<br> |
