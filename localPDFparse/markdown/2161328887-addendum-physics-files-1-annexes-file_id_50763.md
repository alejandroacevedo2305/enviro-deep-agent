---
title: Sin título
author: Cristobal Levicoy
date: D:20241014142509-03'00'
language: es
type: report
pages: 38
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - MODELACIÓN DISPERSIÓN DE OLORES
-->

### PLANTA DE PROCESO CALBUCO

GRANJA MARINA TORNAGALEONES S.A.

# MODELACIÓN DISPERSIÓN DE OLORES

ELABORADO POR:

BUIN 367 - PUERTO MONTT

ARMANDO SANHUEZA 348, OF. 103 - PUNTA ARENAS

+56-65-2752179/+56-65-2714278

[htp://www.ecosistema.clt](http://www.ecosistema.cl/) / [info@ecosistema.cl](mailto:info@ecosistema.cl)

Puerto Montt, Septiembre 2024

Sociedad de Servicios Profesionales Ecosistema Limitada
Buin 367 Puerto Montt - Armando Sanhueza 348, Of. 103 Punta Arenas

+56 65-2752179/+56 65-2714278

[info@ecosistema.cl](mailto:info@ecosistema.cl)

[www.ecosistema.cl](http://www.ecosistema.cl/)

## Tabla de contenido

1. INTRODUCCIÓN ............................................................................................................ 5

2. ANTECEDENTES GENERALES ........................................................................................... 5

2.1. Descripción del proyecto ........................................................................................ 5

2.2. Localización del proyecto ....................................................................................... 7

2.3. Cronograma general del proyecto .......................................................................... 10

3. OBJETIVOS ................................................................................................................. 12

3.1. Objetivos específicos ........................................................................................... 12

4. METODOLOGÍA ........................................................................................................... 12

5. DATOS DE ENTRADA .................................................................................................... 13

5.1. Fuentes de emisión ................................................................................................. 13

5.2. Dominio de modelación y datos meteorológicos ......................................................... 16

6. RESULTADOS .............................................................................................................. 18

6.1. Caracterización meteorológica .................................................................................. 18

6.2. Ubicación de los receptores discretos ........................................................................ 22

6.3. Presentación de datos meteorológicos y de calidad del aire observados ......................... 24

6.4. _Modelación Presentación de los resultados de la modelación meteorológica_ ................... 27

6.5. Presentación de los resultados de la modelación de calidad del aire .............................. 29

6.6. Análisis de validez de los datos Evaluación del desempeño del modelo WRF ................... 32

6.6.1. Análisis Cualitativo ............................................................................................... 33

6.6.2. Análisis Cuantitativo ............................................................................................ 34

7. CONCLUSION .............................................................................................................. 37

8. BIBLIOGRAFIA ............................................................................................................. 38

MODELACIÓN DISPERSIÓN DE OLORES

P á g i n a | 2
PLANTA DE PROCESO CALBUCO

Sociedad de Servicios Profesionales Ecosistema Limitada
Buin 367 Puerto Montt - Armando Sanhueza 348, Of. 103 Punta Arenas

+56 65-2752179/+56 65-2714278

[info@ecosistema.cl](mailto:info@ecosistema.cl)

[www.ecosistema.cl](http://www.ecosistema.cl/)

Índice de tablas y figuras
Tabla 1. Detalle de Superficie del proyecto .......................................................................................... 9
Tabla 2. Coordenadas de referencia punto central ubicación proyecto. .............................................. 9
Tabla 3. Características de la fuente de olor: Fuente informe “Estimación de la Generación de Olores
y Medidas para su Gestión”,ECOTEC. ................................................................................................. 15

Tabla 4. Información del dominio. ..................................................................................................... 17

Tabla 5. Configuración parámetros módulo physics WRF. .................................................................. 18
Tabla 6. Coordenadas geográficas de los receptores discretos (Datum WGS 1984, huso 18S). ......... 22
Tabla 7. Intensidad de olor para cada receptor discretos (Datum WGS 1984, huso 18S). ................. 31
Tabla 8. Métricas estadísticas para análisis de incertidumbre. .......................................................... 36

Figura 1. Ubicación del proyecto Planta de Proceso Calbuco. Fuente: Elaboración propia. ................. 8

Figura 2. Cronograma de trabajo “Planta Proceso Calbuco” .............................................................. 11

Figura 3. Distribución espacial de las fuentes de olores .................................................................... 16

Figura 4. Malla Dominio anidado de la modelación " (51x51 km). Celdas de 1 km. .......................... 17

Figura 5. Clima en zona del proyecto. Fuente: Elaboración propia. ................................................... 19

Figura 5. Precipitación y Temperatura Comuna de Calbuco. Fuente: Actualización Plan Regulador

Comuna de Calbuco ........................................................................................................................... 21

Figura 7. Ubicación de los receptores discretos incluidos en el análisis ............................................ 23

Figura 8. Estaciones de monitoreo cercanas al proyecto. .................................................................. 24

Figura 9. Rosa de los vientos Año 2023, Estación Mirasol, datos del La Red de Estaciones

Agrometeorológicas de INIA. Elaboración propia. ............................................................................. 25
Figura 10. Serie de tiempo Año 2023 para Temperatura del aire y velocidad de viento, Estación
Mirasol, datos del La Red de Estaciones Agrometeorológicas de INIA. Elaboración propia. .............. 26

Figura 11. Variabilidad temporal de Temperatura del aire (rojo) y velocidad de viento (azul), Estación

Mirasol, datos del La Red de Estaciones Agrometeorológicas de INIA. Elaboración propia. ........ ¡Error!

Marcador no def i nido.

Figura 12. Rosa de los vientos Año 2023, Modelo WRF. Elaboración propia. .................................... 27
Figura 13. Serie de tiempo Año 2023 para Temperatura del aire y velocidad de viento, Modelo WRF.
Elaboración propia. ............................................................................................................................ 28
Figura 14. Variabilidad temporal de Temperatura del aire (rojo) y velocidad de viento (azul) Año

2023, Modelo WRF. Elaboración propia. ................................................. ¡Error! Marcador no def i nido.

Figura 15. Variación estacional de Temperatura del aire y velocidad de viento año 2023, Modelo

WRF. Elaboración propia. ................................................................................................................... 28
Figura 16. Percentil 98 de los valores horarios de intensidad de olor (OU/m3). ................................ 29
Figura 17. Percentil 99,5 de los valores horarios de intensidad de olor (OU/m3). ............................. 30
Figura 18. Estaciones de monitoreo cercanas al proyecto. ................................................................ 32

MODELACIÓN DISPERSIÓN DE OLORES

P á g i n a | 3
PLANTA DE PROCESO CALBUCO

Sociedad de Servicios Profesionales Ecosistema Limitada
Buin 367 Puerto Montt - Armando Sanhueza 348, Of. 103 Punta Arenas

+56 65-2752179/+56 65-2714278

[info@ecosistema.cl](mailto:info@ecosistema.cl)

[www.ecosistema.cl](http://www.ecosistema.cl/)

Figura 19. Variabilidad temporal temperatura año 2023 valores observado de la estación Mirasol

(rojo) y valores provenientes del modelo WRF. (Azul) Fuente: Elaboración propia ........................... 33

Figura 20. Variabilidad temporal velocidad del viento año 2023 valores observado de la estación

Mirasol (rojo) y valores provenientes del modelo WRF. (Azul) Fuente: Elaboración propia ............... 34

MODELACIÓN DISPERSIÓN DE OLORES

P á g i n a | 4
PLANTA DE PROCESO CALBUCO

Sociedad de Servicios Profesionales Ecosistema Limitada
Buin 367 Puerto Montt - Armando Sanhueza 348, Of. 103 Punta Arenas

+56 65-2752179/+56 65-2714278

[info@ecosistema.cl](mailto:info@ecosistema.cl)

[www.ecosistema.cl](http://www.ecosistema.cl/)

1. INTRODUCCIÓN

El presente informe presenta una evaluación de los potenciales impactos en la calidad del aire por

parte de las fuentes generadores de olor del proyecto “Planta Proceso Calbuco”, comuna de Calbuco

en su etapa de operación, considerando los lineamientos establecidos por el Servicio de Evaluación

de Impacto Ambiental. En específico se busca verificar que el proyecto no genere alguno de los

efectos, características o circunstancias indicadas en el artículo 5 del D.S. N° 40/2012 del MMA, sobre

los receptores sensibles identificados, modelando las isolíneas de concentración que permiten

observar la zona de máximo impacto del proyecto. Con esta finalidad, se utilizará meteorología

determinada por el modelo meteorológico WRF y el modelo de dispersión de contaminantes Calpuff

desarrollado por la Agencia de Protección Ambiental de Estados Unidos (EPA).

2. ANTECEDENTES GENERALES

2.1. Descripción del proyecto

La Planta de Procesos Calbuco (en adelante Proyecto o Planta) se ubica camino al sector de Caicaen,

aproximadamente a 3,6 kilómetros al Suroeste del centro de la cuidad de Calbuco, en la Comuna del

mismo nombre, en la Provincia de Llanquihue, Región de Los Lagos, en actual titularidad de la

empresa Granja Marina Tornagaleones S.A.

La planta se encuentra construida y dado su nivel de proceso mensual no cuenta con una RCA

considerando la tipología de ingreso n6) del RSEIA 40/2013; sin embargo, fue sometida a evaluación

ambiental bajo la tipología o7) por el sistema de tratamiento de RILes y la disposición de estos fuera

de la zona de protección litoral mediante emisario submarino, cumpliendo con los límites máximos

establecidos por la Tabla No 5 del D.S. No 90/2000 (RCA N°463/2007); en dicha evaluación se detalla

dentro de la fase de operación los productos a procesar, correspondiente a una línea de proceso

primaria de diversas especies de peces, principalmente Merluza ( _Merluccius_ spp), Congrio

( _Genypterus_ spp) y Raya ( _Raja_ spp) y de moluscos, fundamentalmente Chorito ( _Mytilus_ _chilensis_ ); el

caudal medio y máximo de RILes a disponer de 46.8 y 112.1 m [3] /día, respectivamente, considerando

una frecuencia de descarga de 6 horas al día.

MODELACIÓN DISPERSIÓN DE OLORES

P á g i n a | 5
PLANTA DE PROCESO CALBUCO

Sociedad de Servicios Profesionales Ecosistema Limitada
Buin 367 Puerto Montt - Armando Sanhueza 348, Of. 103 Punta Arenas

+56 65-2752179/+56 65-2714278

[info@ecosistema.cl](mailto:info@ecosistema.cl)

[www.ecosistema.cl](http://www.ecosistema.cl/)

En el año 2022, se presenta una solicitud de pertinencia donde se modifica tanto los recursos

hidrobiológicos a procesar de pesca blanca y moluscos bivalvos a especies salmonídeas como el

caudal de descarga en términos de volumen y frecuencia, pertinencia que de acuerdo con los

antecedentes presentados se resuelve que el proyecto no está obligado a someterse al SEIA (Res. No

202210101430). Posteriormente, dado algunas mejoras realizadas en la planta y en la vialidad interna

del proyecto, es que, en marzo del presente año, el actual titular del proyecto ingresa una solicitud

de pertinencia donde se propuso desplazar la planta de tratamiento de RILes y mejorar su

funcionamiento incorporando equipos para ello, además de implementar un filtro UV para desinfectar

el RIL antes de su disposición al medio marino (Res. No 202310101195).

Finalmente, el titular del proyecto ha realizado una remodelación y modernización al interior de la

planta, con el objeto de mejorar la línea de proceso incorporando tecnología de punta en sus

procesos, dado lo anterior, es que el proyecto ingresa al sistema de evaluación de impacto ambiental

para que sea evaluado bajo la tipología principal n6) del RSEIA, toda vez que no ha sido sometida a

evaluación ambiental bajo la tipología antes indicada. Desde el punto de vista operacional, la

modernización de la planta de proceso permite un aumento en el nivel de proceso a 2.500 toneladas

de materia prima mensual en dos líneas entero y filete fresco congelado, lo anterior sin aumentar el

uso de agua declarado en pertinencia Res. No 202210101430 de 20,08 m [3] /hr (5,58 L/s) como tampoco

un aumento en el caudal de RILes a tratar, por lo que la planta de tratamiento de RILes y el emisario

evaluado y aprobado por RCA No 463/2007 y pertinencia Res. N°202210101430 no será modificado

por el presente proyecto. 2000 filete y 500 entero

De acuerdo con lo anterior, el proyecto no considera fase de construcción, ya que tal como se indicó

la planta se encuentra construida y solo se realizaron mejoras y modernizando las líneas de proceso,

cambios que fueron realizados para el cambio del recurso hidrobiológico a procesar (Res. No

202210101430).

El presente proyecto se somete al Sistema de Evaluación de Impacto Ambiental (SEIA), según la Ley

No 19.300 sobre Bases Generales del Medio Ambiente y su modificación Ley No 20.417 en el artículo

10, Letra n) “Proyectos de explotación intensiva, cultivo, y plantas procesadoras de recursos

MODELACIÓN DISPERSIÓN DE OLORES

P á g i n a | 6
PLANTA DE PROCESO CALBUCO

Sociedad de Servicios Profesionales Ecosistema Limitada
Buin 367 Puerto Montt - Armando Sanhueza 348, Of. 103 Punta Arenas

+56 65-2752179/+56 65-2714278

[info@ecosistema.cl](mailto:info@ecosistema.cl)

[www.ecosistema.cl](http://www.ecosistema.cl/)

hidrobiológicos” y artículo 3° del D. S. No 40/2012, Letra n.6) “Planta procesadora de recursos

hidrobiológicos”; y en forma de una Declaración de Impacto Ambiental (DIA), y no como un Estudio

de Impacto Ambiental (EIA), ya que como se indica en los distintos puntos que conforman el cuerpo

de la presente Declaración, la cantidad, disposición y manejo de las emisiones y descargas se enmarca

dentro de la legislación vigente aplicable al proyecto, y no se generan efectos adversos significativos

en ninguno de los literales del Artículo 11 de la Ley, como será demostrado en conformidad a lo

señalado en el literal b) del Artículo 19 del D.S. 40/2012 MMA, Reglamento del Sistema de Evaluación

de Impacto Ambiental, por lo cual el presente proyecto no generará riesgos para la salud de la

población, no produce efectos significativos sobre la cantidad y calidad de los recursos naturales

renovables, incluidos el suelo, agua y aire; no generará reasentamiento de comunidades humanas ni

alterará significativamente los sistemas de vida y costumbres de grupos humanos.

2.2. Localización del proyecto

El proyecto se ubica camino al sector de Caicaen, aproximadamente a 3,6 kilómetros al Suroeste del

centro de la cuidad de Calbuco, en la Comuna del mismo nombre, en la Provincia de Llanquihue,

Región de Los Lagos. La Figura 1 muestra la ubicación geográfica de la zona de emplazamiento del

proyecto en la región de Los Lagos y en la comuna de Calbuco.

MODELACIÓN DISPERSIÓN DE OLORES

P á g i n a | 7
PLANTA DE PROCESO CALBUCO

Sociedad de Servicios Profesionales Ecosistema Limitada
Buin 367 Puerto Montt - Armando Sanhueza 348, Of. 103 Punta Arenas

+56 65-2752179/+56 65-2714278

[info@ecosistema.cl](mailto:info@ecosistema.cl)

[www.ecosistema.cl](http://www.ecosistema.cl/)

Figura 1. Ubicación del proyecto Planta de Proceso Calbuco. Fuente: Elaboración propia.

MODELACIÓN DISPERSIÓN DE OLORES

P á g i n a | 8
PLANTA DE PROCESO CALBUCO

Sociedad de Servicios Profesionales Ecosistema Limitada
Buin 367 Puerto Montt - Armando Sanhueza 348, Of. 103 Punta Arenas

+56 65-2752179/+56 65-2714278

[info@ecosistema.cl](mailto:info@ecosistema.cl)

[www.ecosistema.cl](http://www.ecosistema.cl/)

El proyecto cuenta con una superficie predial de 3.58 hás, dentro de la cual se emplaza lo

actualmente construido. La ¡Error! No se encuentra el origen de la referencia. presenta el detalle de

las superficies construidas y Tabla 2 detalla las coordenadas de ubicación geográfica del proyecto

correspondiente al punto medio del emplazamiento.

Tabla 1. Detalle de Superficie del proyecto

|Instalación|Superficie m2|
|---|---|
|Planta administración|556|
|Planta proceso|3.976|
|Portería y pañol|36,2|
|Frigorífco y embarque|605|
|Pasillo|35|
|Bodega de RESPELs|71,6|
|Tolva de eviscerado|53,3|
|Planta tratamiento RILes|166,5|
|Estanque de aguamar|79,6|
|Estanque agua dulce|156|
|Total|5.735,2|

Tabla 2. Coordenadas de referencia punto central ubicación proyecto.

|Punto Referencia|UTM Este|UTM Norte|Latitud (S)|Longitud (W)|
|---|---|---|---|---|
|Punto Medio|653744|5371443|41 47'38,32"|73 08' 58,48"|

MODELACIÓN DISPERSIÓN DE OLORES

P á g i n a | 9
PLANTA DE PROCESO CALBUCO

Sociedad de Servicios Profesionales Ecosistema Limitada
Buin 367 Puerto Montt - Armando Sanhueza 348, Of. 103 Punta Arenas

+56 65-2752179/+56 65-2714278

[info@ecosistema.cl](mailto:info@ecosistema.cl)

[www.ecosistema.cl](http://www.ecosistema.cl/)

2.3. Cronograma general del proyecto

El presente cronograma entrega las fechas tentativas de duración de cada una de las fases del

incluidas en el proyecto DIA “Planta Proceso Calbuco” de la empresa Granja Marina Tornagaleones

S.A.

|Fase de operación|Col2|
|---|---|
|Fecha estmada de<br>inicio|Enero 2025|
|Parte, obra o acción que<br>establece el inicio|Ingreso materia prima de los distntos centros de cultvo del ttular para<br>procesar 2.500 toneladas al mes en las diferentes líneas de proceso que<br>contempla en proyecto.|
|Fecha estmada de<br>término|Se considera que la vida útl indefnida de 25 años renovable.|
|Parte, obra o acción que<br>establece el término|Actvidades de Mantención: se llevarán a cabo trabajos de mantención,<br>mejoras en la infraestructura y remodelación de instalaciones, con el fn<br>de incorporar nuevas tecnologías que permitan una mejora desde el<br>punto de vista ambiental y de producción.|
|Fase de cierre|Fase de cierre|
|Fecha estmada de<br>inicio|Sin fecha determinada|
|Parte, obra o acción que<br>establece el inicio|Actvidades de Mantención: se llevarán a cabo trabajos de mantención,<br>mejoras en la infraestructura y remodelación de instalaciones, con el fn<br>de incorporar nuevas tecnologías que permitan una mejora desde el<br>punto de vista ambiental y de producción.|
|Fecha estmada de<br>término|-|
|Parte, obra o acción que<br>establece el término|En ttular no considera abandono, en caso de poner término, el ttular<br>considera como últma acción la verifcación del estado del entorno, y<br>ante la eventualidad de existr residuos sólidos, se retrarán del lugar y<br>serán dispuestos en vertederos autorizados.|

MODELACIÓN DISPERSIÓN DE OLORES

P á g i n a | 10
PLANTA DE PROCESO CALBUCO

Sociedad de Servicios Profesionales Ecosistema Limitada
Buin 367 Puerto Montt - Armando Sanhueza 348, Of. 103 Punta Arenas

+56 65-2752179/+56 65-2714278

[info@ecosistema.cl](mailto:info@ecosistema.cl)

[www.ecosistema.cl](http://www.ecosistema.cl/)

La Figura 2 presenta el cronograma de trabajo del proyecto “Planta Proceso Calbuco”, identificando

las diferentes etapas de operación y abandono, esta última se señala una fecha tentativa al concluir

los 25 años de operación de la planta, dado que no está en los planes del titular hacer abandono de

la planta, sino más bien renovar su autorización por tiempo indefinido. La fase tentativa de abandono

tendrá una duración de 3 meses la cual corresponde a un desmantelamiento ordenado de la

infraestructura sin dejar residuos de ningún tipo.

Figura 2. Cronograma de trabajo “Planta Proceso Calbuco”

MODELACIÓN DISPERSIÓN DE OLORES

P á g i n a | 11
PLANTA DE PROCESO CALBUCO

Sociedad de Servicios Profesionales Ecosistema Limitada
Buin 367 Puerto Montt - Armando Sanhueza 348, Of. 103 Punta Arenas

+56 65-2752179/+56 65-2714278

[info@ecosistema.cl](mailto:info@ecosistema.cl)

[www.ecosistema.cl](http://www.ecosistema.cl/)

3. OBJETIVOS

El objetivo general del estudio es evaluar los potenciales impactos en la calidad del aire por parte de

las fuentes generadores de olor del proyecto “Planta Proceso Calbuco”.

3.1. Objetivos específicos

Para lograr el objetivo principal del presente informe, se plantean objetivos específicos que apoyan

la evaluación que se realizó. Así los objetivos específicos son:

 - Realizar una caracterización meteorológica del área de estudio en base a las estaciones

meteorológica cercanas al proyecto y de los datos meteorológicos obtenidos a través del

modelo de predicción WRF.

 Modelar la pluma de dispersión de las fuentes de olores identificados para el proyecto, a

través del modelo de dispersión Calpuff.

 Estimar la intensidad odorífica a la que estarían expuestos los receptores sensibles

identificados en el área de influencia del proyecto.

4. METODOLOGÍA

Se ha aplicado la metodología recomendada en la “Guía de Uso de modelos de calidad del aire en el

SEIA” y la “Guía para la predicción y evaluación de impactos por olor en el SEIA”, ambas desarrolladas

por el SEA. Esta metodología implica el desarrollo de las siguientes actividades:

 - Modelación de la meteorología en altura en la zona del Proyecto, usando el modelo numérico

de pronóstico WRF, para el año 2023 completo, con una resolución espacial de 1x1 km y con

una hora de resolución temporal [1] . Generación del archivo de meteorología para el modelo

de dispersión CALPUFF, a partir de los resultados del modelo WRF. Evaluación estadística del

modelo WRF, comparando meteorología modelada con observada.

MODELACIÓN DISPERSIÓN DE OLORES

P á g i n a | 12
PLANTA DE PROCESO CALBUCO

Sociedad de Servicios Profesionales Ecosistema Limitada
Buin 367 Puerto Montt - Armando Sanhueza 348, Of. 103 Punta Arenas

+56 65-2752179/+56 65-2714278

[info@ecosistema.cl](mailto:info@ecosistema.cl)

[www.ecosistema.cl](http://www.ecosistema.cl/)

 Construcción del inventario de emisiones de olores, a partir de información técnica descrita

en el informe de “Estimación de la Generación de Olores y Medidas para su Gestión”,

elaborado por ECOTEC.

 - Modelación de la dispersión de las emisiones de olores en la zona de estudio usando el

modelo CALPUFF, desarrollado por la Agencia de Protección Ambiental de Estados Unidos

(EPA).

 - Los resultados se entregarán de acuerdo con la recomendación de la Guía para la predicción

y evaluación de impactos por olor en el SEIA, en forma de mapas que entreguen isolíneas de

olor (alcance o nivel de exposición), perfiles de percepción en puntos de interés (definidos en

conjunto con el Cliente), y frecuencias de percepción de olor.

5. DATOS DE ENTRADA

5.1. Fuentes de emisión

En este informe se van a considerar las emisiones de olores generadas durante la fase de operación

del proyecto “Planta de Proceso Calbuco”, considerando aquellas fuentes definidas en el informe de

“Estimación de la Generación de Olores y Medidas para su Gestión”, elaborado por ECOTEC, el cual

hace una descripción de las partes y actividades con potencial odorífico, identificando las principales

fuentes de odoríficas y realizado una estimación de la emisión de olor de cada una de las fuentes, las

cuales son;

 - Planta de Tratamiento de RILes (SRC_3, SRC_4, SRC_5 y SRC_6)

 - Sistema de Manejo de Residuos Sólidos (SRC_2)

 - Manejo de aguas servidas (SRC_7)

A continuación se describen actividades del proyecto con potencial de generación de olores. Estas se

circunscriben exclusivamente a la etapa de operación.

Manejo de RILes : Los puntos de generación de olores corresponden a las superficies donde se puede

generar una transferencia de masa (gases), es decir en los equipos separadores (filtros) y la tolva de

MODELACIÓN DISPERSIÓN DE OLORES

P á g i n a | 13
PLANTA DE PROCESO CALBUCO

Sociedad de Servicios Profesionales Ecosistema Limitada
Buin 367 Puerto Montt - Armando Sanhueza 348, Of. 103 Punta Arenas

+56 65-2752179/+56 65-2714278

[info@ecosistema.cl](mailto:info@ecosistema.cl)

[www.ecosistema.cl](http://www.ecosistema.cl/)

acumulación de sólidos separados, el estanque de ecualización. En menor medida también el equipo

desengrasador, por los lodos que se acumulan en su superficie. La desinfección no se considera punto

de generación de olor.

El sistema de tratamiento de lixiviados (RILes) que utilizará será una combinación de tecnologías, tales

como, físico-químico para eliminación de aceite, grasas y sólidos, stripping para arrastre de gases y

nanofiltración con módulos SPM-HP de canal abierto. El tratamiento físico-químico (DAF) y la unidad

de nanofiltración se entregarán instalados en el interior de contenedores marítimos modificados para

tal fin, con aislamiento térmico-acústico y sistema de refrigeración. Por lo tanto, estas dos unidades

no se consideran fuentes de olor. El stripping del amoniaco tampoco se considera fuente de olor y

que se implementará una etapa posterior de lavado ácido (scrubber) que limpiará el gas.

Manejo de RISes orgánico : La planta estará implementada con un sistema de succión de los residuos

orgánicos proveniente de la sala de proceso, que mediante vacío extraen los residuos a una tolva de

1 4m3 ubicada en el exterior de la sala de proceso, desde este punto son cargados los camiones que

trasladarán estos residuos a plantas reductoras o de hidrolizados.

Manejo de aguas servidas : Las aguas servidas son conducidas a dos fosas sépticas y dispuestos

mediante drenes de infiltración. Las fosas en conjunto tienen una capacidad de aproximadamente 33

m3 (23 m3 y 10 m3, respectivamente). La superficie del líquido del cual se pueden desprender olores

comprende no más de 15 m2. Los olores son liberados al medio ambiente mediante tubos de

ventilación.

La siguiente tabla muestra las características de las fuentes emisoras de olor identificadas. Se asume

que todas estas fuentes operan de manera continua todo el año.

MODELACIÓN DISPERSIÓN DE OLORES

P á g i n a | 14
PLANTA DE PROCESO CALBUCO

Sociedad de Servicios Profesionales Ecosistema Limitada
Buin 367 Puerto Montt - Armando Sanhueza 348, Of. 103 Punta Arenas

+56 65-2752179/+56 65-2714278

[info@ecosistema.cl](mailto:info@ecosistema.cl)

[www.ecosistema.cl](http://www.ecosistema.cl/)

Tabla 3. Características de la fuente de olor: Fuente informe “Estimación de la Generación de Olores
y Medidas para su Gestión”,ECOTEC.

Planta de Tratamiento de RILes

Tratamiento
Filtro tamiz

leve

Filtro

rotatorio

desagradable,
RIL fugitiva Continuo 1,5 72,6
RIL leve

desagradable,
RIL fugitiva Continuo 3,5 169,4
RIL leve

leve

Tratamiento

difusa de
RIL
RIL área

difusa de
RIL, lodos
RIL área

leve

Tratamiento
Ecualizador

desagradable,
Continuo 6 40,2
área leve

desagradable,
Continuo 16,5 51,2
área leve

leve

Tratamiento
Desgrasadora

Manejo de Residuos Sólidos

Sector Tolva

descartes

Fosas

sépticas

Manejo

residuos

orgánicos

Manejo

aguas

servidas

Residuos

orgánicos

Aguas

Servidas

difusa

pasiva y/o

fugitiva

difusa

pasiva y/o

fugitiva

desagradable,
Continuo 10 3,5

leve

desagradable,
Continuo 15 59,3

fuerte

Manejo de Aguas Servidas

Pescado,

Moho leve

Pescado,

Moho leve

Pescado,

Moho

Pescado,

Moho

Pescado,

Moho

Aguas

servidas

La siguiente Figura 3 muestra la ubicación de las fuentes generadoras de olor, incluidas en la

modelación del presente informe.

MODELACIÓN DISPERSIÓN DE OLORES

P á g i n a | 15
PLANTA DE PROCESO CALBUCO

Sociedad de Servicios Profesionales Ecosistema Limitada
Buin 367 Puerto Montt - Armando Sanhueza 348, Of. 103 Punta Arenas

+56 65-2752179/+56 65-2714278

[info@ecosistema.cl](mailto:info@ecosistema.cl)

[www.ecosistema.cl](http://www.ecosistema.cl/)

Figura 3. Distribución espacial de las fuentes de olores

5.2. Dominio de modelación y datos meteorológicos

La información meteorológica requerida por el modelo de dispersión CALPUFF fue construida a partir

de una simulación de un año completo (2023), utilizando el modelo numérico de pronostico del

tiempo WRF ( _Weather Research and Forecasting Model_ ). A continuación, se presenta la modelación

meteorológica y su comparación con las estaciones de monitoreo con datos meteorológicos más

cercanas.

El modelo numérico de pronóstico WRF se utilizó para simular la meteorología de la zona del proyecto

para el año 2023. muestra el dominio de la simulación, el cual tiene una extensión de 51 x 51 km [2],

con resolución horizontal de 1x1 km [2] y donde está incluida la zona del proyecto; las coordenadas en

la figura corresponden a coordenadas locales LCC usadas por el modelo WRF. El origen SO del

MODELACIÓN DISPERSIÓN DE OLORES

P á g i n a | 16
PLANTA DE PROCESO CALBUCO

Sociedad de Servicios Profesionales Ecosistema Limitada
Buin 367 Puerto Montt - Armando Sanhueza 348, Of. 103 Punta Arenas

+56 65-2752179/+56 65-2714278

[info@ecosistema.cl](mailto:info@ecosistema.cl)

[www.ecosistema.cl](http://www.ecosistema.cl/)

dominio de modelación corresponde al punto de coordenadas UTM (WGS84, zona 18S): 593.042 m

E, 5.302.941 m S.

Figura 4. Malla Dominio anidado de la modelación " (51x51 km). Celdas de 1 km.

En Tabla 4 la se presentan las coordenadas vértices del dominio de modelación del proyecto.

Tabla 4. Información del dominio.

|Map project|LCC|
|---|---|
|Latitud|-41.794|
|Longitud|-73.149|
|DX[m]|1000|
|DY[m]|1000|

MODELACIÓN DISPERSIÓN DE OLORES

P á g i n a | 17
PLANTA DE PROCESO CALBUCO

Sociedad de Servicios Profesionales Ecosistema Limitada
Buin 367 Puerto Montt - Armando Sanhueza 348, Of. 103 Punta Arenas

+56 65-2752179/+56 65-2714278

[info@ecosistema.cl](mailto:info@ecosistema.cl)

[www.ecosistema.cl](http://www.ecosistema.cl/)

El modelo WRF fue configurado localmente para 3 dominios anidados. Los parámetros de modelación

físicos se detallan en la Tabla 5.

Tabla 5. Configuración parámetros módulo physics WRF.

|Física|Col2|
|---|---|
|Esquema de radiación|Onda corta: Dudhia, Onda larga: RRTM|
|Tratamiento de capa superficial|MYNNSFC|
|Parametrización de la capa límite|MYNN 3rd level TKE scheme|
|Esquema de convección|Grell-Devenyi ensemble scheme|
|Microfísica de nubes y precipitación|WRF Single-Moment (WSM) 3-class simple ice scheme|
|Parametrización de la turbulencia|Noah Land Surface Model, Smagorinsky horizontal de<br>primer orden|

6. RESULTADOS

6.1. Caracterización meteorológica

La comuna de Calbuco, ubicada en la región de Los Lagos, se encuentra bajo el dominio del clima

Templado Oceánico o lluvioso con la con la ausencia de periodo seco (Municipalidad de Calbuco,

2018). En Calbuco se encuentran presentes dos climas de acuerdo con la clasificación de Koeppen,

como muestra Figura 5. Uno es el Clima templado lluvioso e influencia costera Cfb (i) con

temperaturas promedio de 10 °C y 1.800 milímetros de precipitación. El segundo corresponde al

Clima templado lluvioso Cfb, con temperaturas promedio de 9 °C y 2.100 milímetros de precipitación.

Específicamente, el proyecto se emplaza en la zona con clima templado lluvioso e influencia costera

Cfb (i).

MODELACIÓN DISPERSIÓN DE OLORES

P á g i n a | 18
PLANTA DE PROCESO CALBUCO

Sociedad de Servicios Profesionales Ecosistema Limitada
Buin 367 Puerto Montt - Armando Sanhueza 348, Of. 103 Punta Arenas

+56 65-2752179/+56 65-2714278

[info@ecosistema.cl](mailto:info@ecosistema.cl)

[www.ecosistema.cl](http://www.ecosistema.cl/)

Figura 5. Clima en zona del proyecto. Fuente: Elaboración propia.

En cuanto a las temperaturas, los meses más cálidos coinciden con los meses del período estival con

una media de 18,1C° en enero. Durante esta época existe una mayor influencia de vientos del sur. A

continuación, se presentan dos variables que permitirán caracterizar el área de estudio en términos

meteorológicos, las precipitaciones y las temperaturas. Ambas influyen sobre el desarrollo

vegetacional, su fauna y, sobre el paisaje natural y construido.

_Precipitaciones_

El comportamiento de las precipitaciones evidencia un ambiente húmedo con precipitaciones

durante todo el año con mínimos durante los meses estivales sobre los 50 mm, en contraste con las

precipitaciones invernales alcanzando cerca de los 200 mm.

MODELACIÓN DISPERSIÓN DE OLORES

P á g i n a | 19
PLANTA DE PROCESO CALBUCO

Sociedad de Servicios Profesionales Ecosistema Limitada
Buin 367 Puerto Montt - Armando Sanhueza 348, Of. 103 Punta Arenas

+56 65-2752179/+56 65-2714278

[info@ecosistema.cl](mailto:info@ecosistema.cl)

[www.ecosistema.cl](http://www.ecosistema.cl/)

Los datos respecto de lluvias en la comuna de Calbuco, que corresponde al tipo climático señalado,

permiten describir las precipitaciones en los siguientes puntos:

 - Las precipitaciones presentan una tendencia constante durante todo el año.

 - Tienden a tener mayor concentración en el periodo invernal y una disminución de ellas en

época estival.

 - La sumatoria anual de precipitaciones acumuladas posee en promedio sobre los 1800 mm

anuales

 - Las precipitaciones más bajas se registran el mes de enero con 62 mm.

 - Las precipitaciones mayores se registran en invierno, en el mes de junio con 179 mm.

_Temperatura_

De acuerdo con los datos de temperaturas promedio registradas se puede concluir lo siguiente:

 - Las temperaturas promedio presentan una clara disminución en los meses de invierno,

alcanzando hasta los 3,6° C.

 - Las temperaturas promedio máximas alcanzan los 20,2 ° C en el mes de febrero.

De lo anterior se puede corroborar que las variaciones de temperatura no sobrepasan los 8°C, lo cual

se debe al efecto moderador del mar.

MODELACIÓN DISPERSIÓN DE OLORES

P á g i n a | 20
PLANTA DE PROCESO CALBUCO

Sociedad de Servicios Profesionales Ecosistema Limitada
Buin 367 Puerto Montt - Armando Sanhueza 348, Of. 103 Punta Arenas

+56 65-2752179/+56 65-2714278

[info@ecosistema.cl](mailto:info@ecosistema.cl)

[www.ecosistema.cl](http://www.ecosistema.cl/)

Figura 6. Precipitación y Temperatura Comuna de Calbuco. Fuente: Actualización Plan Regulador

Comuna de Calbuco

MODELACIÓN DISPERSIÓN DE OLORES

P á g i n a | 21
PLANTA DE PROCESO CALBUCO

Sociedad de Servicios Profesionales Ecosistema Limitada
Buin 367 Puerto Montt - Armando Sanhueza 348, Of. 103 Punta Arenas

+56 65-2752179/+56 65-2714278

[info@ecosistema.cl](mailto:info@ecosistema.cl)

[www.ecosistema.cl](http://www.ecosistema.cl/)

6.2. Ubicación de los receptores discretos

En este estudio se analizaron 18 receptores discretos, los cuales son principalmente de tipo

Residencial/laborales a excepción del Receptor 6 (IL8), el cual corresponde al cementerio ubicado

frente a la Planta de procesos. La siguiente Tabla 6 indica la ubicación geográfica de los receptores

discretos analizados y la Figura 7 muestran la ubicación cada uno de estos receptores.

Tabla 6. Coordenadas geográficas de los receptores discretos (Datum WGS 1984, huso 18S).

|N°|Identificación|Distancia a la<br>fuente|Descripción|Coordenada UTM|Col6|
|---|---|---|---|---|---|
|N°|Identificación|Distancia a la<br>fuente|Descripción|Este|Norte|
|1|IL 3|150 m|Habitacional / Laboral|653643.63|5371440.51|
|2|IL 4|150 m|Habitacional|653634.74|5371396.19|
|3|IL 5|180 m|Habitacional|653622.92|5371386.36|
|4|IL 6|170 m|Habitacional|653609.24|5371384.01|
|5|IL 7|1050 m|Laboral|653237.47|5370487.89|
|6|IL 8|200 m|Laboral|653629.48|5371509.06|
|7|IL 9|200 m|Habitacional|653652.48|5371257.96|
|8|IL 10|300 m|Habitacional / Laboral|653599.72|5371622.91|
|9|IL 11|200 m|Habitacional (en construcción)|653784.72|5371600.27|
|10|IL 12|> 300 m|Habitacional / Laboral|653794.15|5371815.10|
|11|IL 13|240 m|Habitacional|653760.66|5371642.95|
|12|IL 14|> 300 m|Habitacional|653695.45|5371721.77|
|13|IL 15|240 m|Laboral (sitio en venta)|653563.01|5371333.17|
|14|IL 16|> 300 m|Habitacional|653494.30|5371242.38|
|15|IL 17|> 300 m|Habitacional|653836.54|5371730.30|
|16|IL 18|240 m|Laboral|653798.59|5371630.62|
|17|IL 19|> 300 m|Habitacional|653836.30|5371854.86|
|18|IL 20|> 300 m|Habitacional (casa de veraneo)|653608.16|5371727.05|

MODELACIÓN DISPERSIÓN DE OLORES

P á g i n a | 22
PLANTA DE PROCESO CALBUCO

Sociedad de Servicios Profesionales Ecosistema Limitada
Buin 367 Puerto Montt - Armando Sanhueza 348, Of. 103 Punta Arenas

+56 65-2752179/+56 65-2714278

[info@ecosistema.cl](mailto:info@ecosistema.cl)

[www.ecosistema.cl](http://www.ecosistema.cl/)

Figura 7. Ubicación de los receptores discretos incluidos en el análisis

Junto con los 18 receptores discretos individualizados, se definió una grilla Cartesiana de receptores

con espaciamiento de 1 km para poder representar adecuadamente la distribución espacial de los

posibles impactos en la calidad del aire producidos por la operación del proyecto. La extensión de

esta grilla es de 51 x 51 km.

MODELACIÓN DISPERSIÓN DE OLORES

P á g i n a | 23
PLANTA DE PROCESO CALBUCO

Sociedad de Servicios Profesionales Ecosistema Limitada
Buin 367 Puerto Montt - Armando Sanhueza 348, Of. 103 Punta Arenas

+56 65-2752179/+56 65-2714278

[info@ecosistema.cl](mailto:info@ecosistema.cl)

[www.ecosistema.cl](http://www.ecosistema.cl/)

6.3. Presentación de datos meteorológicos y de calidad del aire observados

Considerando la ubicación del proyecto se identificaron las estaciones meteorológicas más cercanas,

las cuales corresponde a la estación Putenio y Mirasol, según la información disponible en la Red de

Agrometeorología del INIA (https://agrometeorologia.cl/). Al respecto la estación Mirasol se ubica a

38 kilómetros de distancia en línea recta de la Planta de Proceso Calbuco y la estación Putenio se

encuentra a 13 kilómetros de distancia del proyecto. Es importante indicar que, si bien la estación

Putenio es la más cercana al proyecto, es una estación relativamente nueva, y para el año 2023 solo

tiene registros desde el 19 de octubre en adelante, por lo cual se utilizará como referencia la estación

Mirasol, al contar con un registro completo del año 2023. La Figura 8 muestra la ubicación de las

estaciones meteorológicas cercanas al emplazamiento del proyecto, en base a la información

disponible en la Red INIA

Figura 8. Estaciones de monitoreo cercanas al proyecto.

MODELACIÓN DISPERSIÓN DE OLORES

P á g i n a | 24
PLANTA DE PROCESO CALBUCO

Sociedad de Servicios Profesionales Ecosistema Limitada
Buin 367 Puerto Montt - Armando Sanhueza 348, Of. 103 Punta Arenas

+56 65-2752179/+56 65-2714278

[info@ecosistema.cl](mailto:info@ecosistema.cl)

[www.ecosistema.cl](http://www.ecosistema.cl/)

_Estación Mirasol_

En la Figura 9 se presenta el comportamiento anual de los vientos registrados por la Estación Mirasol,

para los meses de enero a diciembre de 2023. De la rosa de los vientos es posible identificar que el

viento predominante sopla desde el Noroeste y Norte.

Figura 9. Rosa de los vientos Año 2023, Estación Mirasol, datos del La Red de Estaciones

Agrometeorológicas de INIA. Elaboración propia.

En las figuras 9 y 10 presentadas a continuación podemos observar que la temperatura promedio

registrada en la estación Mirasol fue de 10,9°C, con una velocidad de viento media de 2,6 m/s, con

las mayores temperaturas registradas en el periodo de verano y con las mayores velocidades

registradas a finales del invierno e inicio de primavera, en horarios cercanos al medio día.

MODELACIÓN DISPERSIÓN DE OLORES

P á g i n a | 25
PLANTA DE PROCESO CALBUCO

Sociedad de Servicios Profesionales Ecosistema Limitada
Buin 367 Puerto Montt - Armando Sanhueza 348, Of. 103 Punta Arenas

+56 65-2752179/+56 65-2714278

[info@ecosistema.cl](mailto:info@ecosistema.cl)

[www.ecosistema.cl](http://www.ecosistema.cl/)

Figura 10. Serie de tiempo Año 2023 para Temperatura del aire y velocidad de viento, Estación

Mirasol, datos del La Red de Estaciones Agrometeorológicas de INIA. Elaboración propia.

Figura 11. Variación estacional de Temperatura del aire y velocidad de viento año 2023, Estación

Mirasol, datos del La Red de Estaciones Agrometeorológicas de INIA. Elaboración propia.

MODELACIÓN DISPERSIÓN DE OLORES

P á g i n a | 26
PLANTA DE PROCESO CALBUCO

Sociedad de Servicios Profesionales Ecosistema Limitada
Buin 367 Puerto Montt - Armando Sanhueza 348, Of. 103 Punta Arenas

+56 65-2752179/+56 65-2714278

[info@ecosistema.cl](mailto:info@ecosistema.cl)

[www.ecosistema.cl](http://www.ecosistema.cl/)

6.4. _Modelación Presentación de los resultados de la modelación meteorológica_

En la Figura 12 se presenta el comportamiento anual de los vientos determinado por el modelo WRF,

para los meses de enero a diciembre de 2023. De la rosa de los vientos es posible identificar que el

viento predominante sopla desde el Noroeste.

Figura 12. Rosa de los vientos Año 2023, Modelo WRF. Elaboración propia.

En las figuras 13 y 14 presentadas a continuación podemos observar que la temperatura promedio

registrada en la estación Mirasol fue de 11,3°C, con una velocidad de viento media de 3,8 m/s, con

las mayores temperaturas registradas en el periodo de verano y con las mayores velocidades

registradas a finales del invierno e inicio de primavera, en horarios cercanos al medio día.

MODELACIÓN DISPERSIÓN DE OLORES

P á g i n a | 27
PLANTA DE PROCESO CALBUCO

Sociedad de Servicios Profesionales Ecosistema Limitada
Buin 367 Puerto Montt - Armando Sanhueza 348, Of. 103 Punta Arenas

+56 65-2752179/+56 65-2714278

[info@ecosistema.cl](mailto:info@ecosistema.cl)

[www.ecosistema.cl](http://www.ecosistema.cl/)

Figura 13. Serie de tiempo Año 2023 para Temperatura del aire y velocidad de viento, Modelo WRF.

Elaboración propia.

Figura 14. Variación estacional de Temperatura del aire y velocidad de viento año 2023, Modelo

WRF. Elaboración propia.

MODELACIÓN DISPERSIÓN DE OLORES

P á g i n a | 28
PLANTA DE PROCESO CALBUCO

Sociedad de Servicios Profesionales Ecosistema Limitada
Buin 367 Puerto Montt - Armando Sanhueza 348, Of. 103 Punta Arenas

+56 65-2752179/+56 65-2714278

[info@ecosistema.cl](mailto:info@ecosistema.cl)

[www.ecosistema.cl](http://www.ecosistema.cl/)

6.5. Presentación de los resultados de la modelación de calidad del aire

A continuación, se presentan los resultados de la modelación, expresados como concentración de

olor (OU/m [3] ). En las siguientes figuras y tablas presentamos los resultados, evaluando los aportes de

las fuentes de olores identificadas en la planta de proceso Calbuco sobre los receptores discretos.

Figura 15. Percentil 98 de los valores horarios de intensidad de olor (OU/m3).

MODELACIÓN DISPERSIÓN DE OLORES

P á g i n a | 29
PLANTA DE PROCESO CALBUCO

Sociedad de Servicios Profesionales Ecosistema Limitada
Buin 367 Puerto Montt - Armando Sanhueza 348, Of. 103 Punta Arenas

+56 65-2752179/+56 65-2714278

[info@ecosistema.cl](mailto:info@ecosistema.cl)

[www.ecosistema.cl](http://www.ecosistema.cl/)

Figura 16. Percentil 99,5 de los valores horarios de intensidad de olor (OU/m3).

Para el proyecto, el Punto de Máximo Impacto (PMI) para el percentil 98 de los valores horarios de

olor está ubicado en el punto de coordenadas UTM (WGS84, zona 18S): 653792.09 m E y 5371441.70

m S, el cual está ubicado en el sector Sureste de las instalaciones de la Planta, al interior del predio

donde se encuentra ubicada la planta de proceso y parte del bosque del predio aledaño, propiedad

del mismo titular. De igual manera se observa el mismo comportamiento de la intensidad de

concentración para los resultados del percentil 99,5.

La siguiente tabla muestra las concentraciones horarias modeladas de olor en los receptores

discretos. El proyecto no va a exponer a los receptores sensibles a concentraciones de olor

significativas, ya que todos los receptores quedan con niveles horarios de olor (percentil 98) menores

a 1 (OU/m [3] ), ver Figura 19. Considerando que las intensidades de olor son bastante bajas, no se

realizaron figuras para visualizar el número de horas de excedencia de la concentración de olor de

referencia. Los perfiles diarios y anuales de intensidad de olor se presentan en el anexo de este

documento.

MODELACIÓN DISPERSIÓN DE OLORES

P á g i n a | 30
PLANTA DE PROCESO CALBUCO

Sociedad de Servicios Profesionales Ecosistema Limitada
Buin 367 Puerto Montt - Armando Sanhueza 348, Of. 103 Punta Arenas

+56 65-2752179/+56 65-2714278

[info@ecosistema.cl](mailto:info@ecosistema.cl)

[www.ecosistema.cl](http://www.ecosistema.cl/)

Tabla 7. Intensidad de olor para cada receptor discretos (Datum WGS 1984, huso 18S).

|Receptor|ID|Conc. Max (OU/m3)|Percentil 98 (OU/m3)|Percentil 99,5 (OU/m3)|
|---|---|---|---|---|
|1|IL3|0,517|0,017|0,272|
|2|IL4|0,531|0,011|0,270|
|3|IL5|0,551|0,009|0,268|
|4|IL6|0,526|0,008|0,262|
|5|IL7|0,140|0,001|0,010|
|6|IL8|0,475|0,020|0,248|
|7|IL9|0,527|0,015|0,259|
|8|IL10|0,491|0,012|0,183|
|9|IL11|0,586|0,099|0,234|
|10|IL12|0,398|0,035|0,110|
|11|IL13|0,437|0,060|0,198|
|12|IL14|0,423|0,018|0,156|
|13|IL15|0,548|0,006|0,247|
|14|IL16|0,525|0,004|0,200|
|15|IL17|0,450|0,053|0,155|
|16|IL18|0,474|0,096|0,228|
|17|IL19|0,320|0,032|0,096|
|18|IL20|0,431|0,009|0,140|

Al considerarse los resultados de la modelación de calidad del aire, se empleó un dominio de 51 x 51

km [2], que incluye todas las zonas pobladas alrededor del proyecto, y que considera 18 receptores

sensibles (viviendas) cercanas al proyecto. Para el caso de olores, el percentil 98 de las

concentraciones horarias modeladas para todo el año 2023 se usó como indicador de impactos en

calidad del aire. El mayor valor de este indicador en las viviendas fue de 0,099 OU/m3,

correspondiente al receptor IL11, vivienda en construcción ubicada en el punto de coordenadas UTM

(datum WGS84, huso 18S): 653784.72 m E y 5371600.27 m S. En todas las demás viviendas, los

aportes del proyecto son menores a ese valor. Por otra parte, el máximo valor del percentil 98 horario

está ubicado dentro del predio del proyecto, en el punto de coordenadas UTM (datum WGS84, huso

18S): 653792.09 m E y 5371441.70 m S.

MODELACIÓN DISPERSIÓN DE OLORES

P á g i n a | 31
PLANTA DE PROCESO CALBUCO

Sociedad de Servicios Profesionales Ecosistema Limitada
Buin 367 Puerto Montt - Armando Sanhueza 348, Of. 103 Punta Arenas

+56 65-2752179/+56 65-2714278

[info@ecosistema.cl](mailto:info@ecosistema.cl)

[www.ecosistema.cl](http://www.ecosistema.cl/)

6.6. Análisis de validez de los datos Evaluación del desempeño del modelo WRF

En la zona modelada, se utilizó la información de la estación meteorológica más cercana al proyecto,

en este caso la estación Mirasol, pertenecientes a la red Agrometeorológica INIA

[(htps://agrometeorologia.cl/)t](https://agrometeorologia.cl/) . La estación Mirasol se ubicada a 38 kilómetros de distancia en línea

recta de la Planta de Proceso Calbuco. Es importante indicar que según fuentes del INIA existe una

estación más cercana, la estación Putenio, ubicada en la comuna de Calbuco a 13 kilómetros de

distancia del proyecto, pero debido a que es una estación relativamente nueva, para el año 2023 solo

tiene registros desde el 19 de octubre en adelante. La Figura 17 muestra la ubicación de las estaciones

meteorológicas cercanas al emplazamiento del proyecto, en base a la información disponible en la

Red INIA.

Figura 17. Estaciones de monitoreo cercanas al proyecto.

MODELACIÓN DISPERSIÓN DE OLORES

P á g i n a | 32
PLANTA DE PROCESO CALBUCO

Sociedad de Servicios Profesionales Ecosistema Limitada
Buin 367 Puerto Montt - Armando Sanhueza 348, Of. 103 Punta Arenas

+56 65-2752179/+56 65-2714278

[info@ecosistema.cl](mailto:info@ecosistema.cl)

[www.ecosistema.cl](http://www.ecosistema.cl/)

6.6.1. Análisis Cualitativo

Con respecto a la correlación entre la temperatura modelada y la observada, las siguientes figuras

muestran que las variables de temperatura y velocidad del aire tienen un comportamiento similar. De

ambas variables, es la temperatura quien visualmente presenta mayor similitud (Figura 18), por otra

parte, la velocidad del viento si bien se presenta una diferencia en la intensidad, la variabilidad horaria,

semanal y mensual tienen un comportamiento similar, como lo presenta la Figura 19.

Figura 18. Variabilidad temporal temperatura año 2023 valores observado de la estación Mirasol (rojo)

y valores provenientes del modelo WRF. (Azul) Fuente: Elaboración propia

MODELACIÓN DISPERSIÓN DE OLORES

P á g i n a | 33
PLANTA DE PROCESO CALBUCO

Sociedad de Servicios Profesionales Ecosistema Limitada
Buin 367 Puerto Montt - Armando Sanhueza 348, Of. 103 Punta Arenas

+56 65-2752179/+56 65-2714278

[info@ecosistema.cl](mailto:info@ecosistema.cl)

[www.ecosistema.cl](http://www.ecosistema.cl/)

Figura 19. Variabilidad temporal velocidad del viento año 2023 valores observado de la estación

Mirasol (rojo) y valores provenientes del modelo WRF. (Azul) Fuente: Elaboración propia

6.6.2.Análisis Cuantitativo

Se realizo un análisis cuantitativo considerando las métricas estadísticas sugeridas en el numeral 6.2.2

de la “Guía para el uso de modelos de calidad del aire en el SEIA” (Servicio de Evaluación Ambiental,

2023), las cuales corresponde a sesgo (error medio o BIAS), error absoluto medio (MAE) y la raíz del

error cuadrático medio (RMSE), cuyas ecuaciones se presentan a continuación.

MODELACIÓN DISPERSIÓN DE OLORES

P á g i n a | 34
PLANTA DE PROCESO CALBUCO

Sociedad de Servicios Profesionales Ecosistema Limitada
Buin 367 Puerto Montt - Armando Sanhueza 348, Of. 103 Punta Arenas

+56 65-2752179/+56 65-2714278

[info@ecosistema.cl](mailto:info@ecosistema.cl)

[www.ecosistema.cl](http://www.ecosistema.cl/)

Donde:

n: Cantidad de datos

S: Valores obtenidos del modelo

0: Valores observados en estaciones meteorológicas

Tanto BIAS como MAE son estimadores de la diferencia entre el valor modelado y observado de un

mismo fenómeno, en este caso meteorológico. De igual forma, RMSE es un estimador de la frecuencia

de las diferencias entre los valores observados y modelados, siendo especialmente sensible a los

valores atípicos, por lo tanto, a mayor diferencia entre estos valores menor será el grado de ajuste de

este estadístico.

A su vez, a las métricas señaladas se incorporar el coeficiente de correlación (r), que corresponde a

una medida de la correlación lineal entre dos conjuntos de variables, siendo para este caso, los valores

modelados y observados. Su fórmula se presenta a continuación

Donde:

Oi: corresponde a las observaciones

Mi corresponde a los valores modelados

I: corresponde a cada uno de los N valores horarios de las variables analizadas para la estación.

Las métricas fueron estimadas para las estaciones mas cercanas al proyecto, en este caso la estación

Mirasol y la estación Putenio, siendo esta ultima la más cercana al proyecto. Para la estación Mirasol

se contrastaron los datos de velocidad y temperatura para todo el año 2023, en el caso de la estación

Putenio de igual manera se contrastaron datos de velocidad y temperatura pero solo desde el 19 de

octubre 2023 al 31 de diciembre 2023 dado que la estación solo tiene registros desde esa fecha en

MODELACIÓN DISPERSIÓN DE OLORES

P á g i n a | 35
PLANTA DE PROCESO CALBUCO

Sociedad de Servicios Profesionales Ecosistema Limitada
Buin 367 Puerto Montt - Armando Sanhueza 348, Of. 103 Punta Arenas

+56 65-2752179/+56 65-2714278

[info@ecosistema.cl](mailto:info@ecosistema.cl)

[www.ecosistema.cl](http://www.ecosistema.cl/)

adelante. Los resultados de la estimación de las métricas indicadas se presentan en la Tabla 8, y como

se puede observar en el contraste con la estación Mirasol todos lo estadísticos se encuentran dentro

de los valores de referencia, sugeridos en la Tabla 2 “Guía para el uso de modelos de calidad del aire

en el SEIA”, en el caso de la estación Putenio se observa que todos los estadísticos cumplen con los

valores de referencia, con la excepción del coeficiente de correlación para Viento, al respecto es

importante indicar que el contraste de la estación Putenio versus los datos del modelo WRF se realizo

sólo para los tres últimos meses del año 2023, debido a la poca disponibilidad de datos por parte de

la estación Putenio.

Tabla 8. Métricas estadísticas para análisis de incertidumbre.

|Metrica|WRF vs Estación Mirasol|Col3|WRF vs Estación Putenio|Col5|Valor referencia (*)|Col7|
|---|---|---|---|---|---|---|
|Metrica|Temperatura|Viento|Temperatura|Viento|Temperatura|Viento|
|BIAS|0,4|1,2|0,7|2,3|[-4;4] (°C)|[-2,5;2,5]<br>(m/s)|
|MAE|1,7|1,5|1,7|2,4|≤4 (°C)|≤3 (m/s)|
|RMSE|2,6|1,9|2,3|2,9|≤ 4,5 (°C)|≤3,5 (m/s)|
|r|0,8|0,6|0,9|0,4|>0,8|>0,6|

(*) Según recomendación en numeral 6.2.2 de la “Guía para el uso de modelos de calidad del aire en

el SEIA”

MODELACIÓN DISPERSIÓN DE OLORES

P á g i n a | 36
PLANTA DE PROCESO CALBUCO

Sociedad de Servicios Profesionales Ecosistema Limitada
Buin 367 Puerto Montt - Armando Sanhueza 348, Of. 103 Punta Arenas

+56 65-2752179/+56 65-2714278

[info@ecosistema.cl](mailto:info@ecosistema.cl)

[www.ecosistema.cl](http://www.ecosistema.cl/)

7. CONCLUSION

Para el proyecto Planta de Proceso Calbuco, ubicado en la comuna de Calbuco, provincia de

Llanquihue, Región de los Lagos, se ha modelado los aportes a la calidad del aire asociados a olores

en la etapa de operación. Para esto se hizo una modelación de la meteorología de la zona alrededor

del proyecto para todo el año 2023, empleando el modelo numérico de pronóstico del tiempo WRF

(Weather Research and Forecasting Model). La evaluación estadística del desempeño del modelo

indica que el modelo tiene tendencia a sobrestimar la velocidad del viento, y a representar muy bien

la temperatura.

Al considerarse los resultados de la modelación de calidad del aire, se empleó un dominio de 51 x 51

km2, que incluye todas las zonas pobladas alrededor del proyecto, y que considera 18 receptores

sensibles (viviendas) cercanas al proyecto.

Para el caso de olores, el percentil 98 de las concentraciones horarias modeladas para todo el año

2023 se usó como indicador de impactos en calidad del aire. El mayor valor de este indicador en las

viviendas fue de 0,098 OU/m3, correspondiente al receptor IL11, vivienda en construcción ubicada

en el punto de coordenadas UTM (datum WGS84, huso 18S): 653784.72 m E y 5371600.27 m S. En

todas las demás viviendas, los aportes del proyecto son menores a ese valor. Por otra parte, el máximo

valor del percentil 98 horario está ubicado dentro del predio del proyecto, en el punto de coordenadas

UTM (datum WGS84, huso 18S): 653792.09 m E y 5371441.70 m S.

Por lo tanto, el proyecto Planta de Proceso Calbuco va a cumplir con la normativa ambiental de calidad

del aire en el componente olor, durante la etapa de operación, que es la que produce mayores

emisiones.

MODELACIÓN DISPERSIÓN DE OLORES

P á g i n a | 37
PLANTA DE PROCESO CALBUCO

Sociedad de Servicios Profesionales Ecosistema Limitada
Buin 367 Puerto Montt - Armando Sanhueza 348, Of. 103 Punta Arenas

+56 65-2752179/+56 65-2714278

[info@ecosistema.cl](mailto:info@ecosistema.cl)

[www.ecosistema.cl](http://www.ecosistema.cl/)

8. BIBLIOGRAFIA

 - Información de meteorología y calidad del aire en la zona del Proyecto: Información obtenida

[de la red Agrometeorológica INIA (htps://agrometeorologia.cl/t](https://agrometeorologia.cl/) ).

 Anexo 12 de Estudios Complementarios carpeta 3.Olores, Informe “Estimación de la

Generación de Olores y Medidas para su Gestión” DIA “Planta de proceso Calbuco“, informe

realizado por ECOTEC Ingeniería SPA.

 Información de dominio público: información del National Center for Atmospheric Research

(NCAR) para realizar la modelación de WRF.

MODELACIÓN DISPERSIÓN DE OLORES

P á g i n a | 38
PLANTA DE PROCESO CALBUCO

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Detalle de Superficie del proyecto**

| Instalación | Superficie m2 |
| --- | --- |
| Planta administración | 556 |
| Planta proceso | 3.976 |
| Portería y pañol | 36,2 |
| Frigorífco y embarque | 605 |
| Pasillo | 35 |
| Bodega de RESPELs | 71,6 |
| Tolva de eviscerado | 53,3 |
| Planta tratamiento RILes | 166,5 |
| Estanque de aguamar | 79,6 |
| Estanque agua dulce | 156 |
| Total | 5.735,2 |

**Tabla 2.: Coordenadas de referencia punto central ubicación proyecto.**

| Punto Referencia | UTM Este | UTM Norte | Latitud (S) | Longitud (W) |
| --- | --- | --- | --- | --- |
| Punto Medio | 653744 | 5371443 | 41 47'38,32" | 73 08' 58,48" |

**Tabla 4.: Información del dominio.**

| Map project | LCC |
| --- | --- |
| Latitud | -41.794 |
| Longitud | -73.149 |
| DX[m] | 1000 |
| DY[m] | 1000 |

**Tabla 5.: Configuración parámetros módulo physics WRF.**

| Física | Col2 |
| --- | --- |
| Esquema de radiación | Onda corta: Dudhia, Onda larga: RRTM |
| Tratamiento de capa superficial | MYNNSFC |
| Parametrización de la capa límite | MYNN 3rd level TKE scheme |
| Esquema de convección | Grell-Devenyi ensemble scheme |
| Microfísica de nubes y precipitación | WRF Single-Moment (WSM) 3-class simple ice scheme |
| Parametrización de la turbulencia | Noah Land Surface Model, Smagorinsky horizontal de<br>primer orden |

**Tabla 6.: Coordenadas geográficas de los receptores discretos (Datum WGS 1984, huso 18S).**

| N° | Identificación | Distancia a la<br>fuente | Descripción | Coordenada UTM | Col6 |
| --- | --- | --- | --- | --- | --- |
| N° | Identificación | Distancia a la<br>fuente | Descripción | Este | Norte |
| 1 | IL 3 | 150 m | Habitacional / Laboral | 653643.63 | 5371440.51 |
| 2 | IL 4 | 150 m | Habitacional | 653634.74 | 5371396.19 |
| 3 | IL 5 | 180 m | Habitacional | 653622.92 | 5371386.36 |
| 4 | IL 6 | 170 m | Habitacional | 653609.24 | 5371384.01 |
| 5 | IL 7 | 1050 m | Laboral | 653237.47 | 5370487.89 |
| 6 | IL 8 | 200 m | Laboral | 653629.48 | 5371509.06 |
| 7 | IL 9 | 200 m | Habitacional | 653652.48 | 5371257.96 |
| 8 | IL 10 | 300 m | Habitacional / Laboral | 653599.72 | 5371622.91 |
| 9 | IL 11 | 200 m | Habitacional (en construcción) | 653784.72 | 5371600.27 |
| 10 | IL 12 | > 300 m | Habitacional / Laboral | 653794.15 | 5371815.10 |
| 11 | IL 13 | 240 m | Habitacional | 653760.66 | 5371642.95 |
| 12 | IL 14 | > 300 m | Habitacional | 653695.45 | 5371721.77 |
| 13 | IL 15 | 240 m | Laboral (sitio en venta) | 653563.01 | 5371333.17 |
| 14 | IL 16 | > 300 m | Habitacional | 653494.30 | 5371242.38 |
| 15 | IL 17 | > 300 m | Habitacional | 653836.54 | 5371730.30 |
| 16 | IL 18 | 240 m | Laboral | 653798.59 | 5371630.62 |
| 17 | IL 19 | > 300 m | Habitacional | 653836.30 | 5371854.86 |
| 18 | IL 20 | > 300 m | Habitacional (casa de veraneo) | 653608.16 | 5371727.05 |

**Tabla 7.: Intensidad de olor para cada receptor discretos (Datum WGS 1984, huso 18S).**

| Receptor | ID | Conc. Max (OU/m3) | Percentil 98 (OU/m3) | Percentil 99,5 (OU/m3) |
| --- | --- | --- | --- | --- |
| 1 | IL3 | 0,517 | 0,017 | 0,272 |
| 2 | IL4 | 0,531 | 0,011 | 0,270 |
| 3 | IL5 | 0,551 | 0,009 | 0,268 |
| 4 | IL6 | 0,526 | 0,008 | 0,262 |
| 5 | IL7 | 0,140 | 0,001 | 0,010 |
| 6 | IL8 | 0,475 | 0,020 | 0,248 |
| 7 | IL9 | 0,527 | 0,015 | 0,259 |
| 8 | IL10 | 0,491 | 0,012 | 0,183 |
| 9 | IL11 | 0,586 | 0,099 | 0,234 |
| 10 | IL12 | 0,398 | 0,035 | 0,110 |
| 11 | IL13 | 0,437 | 0,060 | 0,198 |
| 12 | IL14 | 0,423 | 0,018 | 0,156 |
| 13 | IL15 | 0,548 | 0,006 | 0,247 |
| 14 | IL16 | 0,525 | 0,004 | 0,200 |
| 15 | IL17 | 0,450 | 0,053 | 0,155 |
| 16 | IL18 | 0,474 | 0,096 | 0,228 |
| 17 | IL19 | 0,320 | 0,032 | 0,096 |
| 18 | IL20 | 0,431 | 0,009 | 0,140 |

**Tabla 8.: Métricas estadísticas para análisis de incertidumbre.**

| Metrica | WRF vs Estación Mirasol | Col3 | WRF vs Estación Putenio | Col5 | Valor referencia (*) | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Metrica | Temperatura | Viento | Temperatura | Viento | Temperatura | Viento |
| BIAS | 0,4 | 1,2 | 0,7 | 2,3 | [-4;4] (°C) | [-2,5;2,5]<br>(m/s) |
| MAE | 1,7 | 1,5 | 1,7 | 2,4 | ≤4 (°C) | ≤3 (m/s) |
| RMSE | 2,6 | 1,9 | 2,3 | 2,9 | ≤ 4,5 (°C) | ≤3,5 (m/s) |
| r | 0,8 | 0,6 | 0,9 | 0,4 | >0,8 | >0,6 |
