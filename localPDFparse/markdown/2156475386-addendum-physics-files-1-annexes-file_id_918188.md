---
title: INFORME DE MODELACION DE DISPERSION DE CONTAMINANTES ATMOSFERICOS
author: IGNACIO GOIC
date: D:20221222095843-03'00'
language: es
type: report
pages: 23
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - INFORME DE MODELACION DE DISPERSION DE CONTAMINANTES ATMOSFERICOS
-->

_PROYECTO “CENTRO DE RECEPCIÓN Y DISPOSICIÓN FINAL DE BIOSÓLIDOS”_

# INFORME DE MODELACION DE DISPERSION DE CONTAMINANTES ATMOSFERICOS
## “CENTRO DE RECEPCIÓN Y DISPOSICIÓN FINAL DE BIOSÓLIDOS” PREPARADO POR:

### IGNACIO GOIC 30/11/2022

V4.0

Informe de Calidad del Aire Pág. 1

_PROYECTO “CENTRO DE RECEPCIÓN Y DISPOSICIÓN FINAL DE BIOSÓLIDOS”_

**INDICE GENERAL**

**1** **INTRODUCCION** **3**

**2** **AREA DE INFLUENCIA** **4**

**3** **MODELACIÓN DE CONTAMINANTES** **6**

**3.1** **TEORIA DE LA DISPERSIÓN DE LOS CONTAMINANTES.** **6**

3.1.1 T IPOS DE MODELOS DE DISPERSIÓN 7

3.1.2 M ODELO C ALPUFF 8
**3.2** **METEOROLOGÍA** **8**

**3.3** **ANALISIS DE INCERTIDUMBRE** **10**

**3.4** **TOPOGRAFIA** **11**

**3.5** **RECEPTORES** **12**

**3.6** **EMISIONES** **13**
**3.7** **RESULTADOS DE LA MODELACIÓN** **13**

**4** **CONCLUSIONES** **22**

**5** **REFERENCIAS BIBLIOGRAFICAS** **23**

Informe de Calidad del Aire Pág. 2

_PROYECTO “CENTRO DE RECEPCIÓN Y DISPOSICIÓN FINAL DE BIOSÓLIDOS”_

**1** **INTRODUCCION**

El proyecto en evaluación se ubica en el borde Sur-Oeste de la comuna de Sierra Gorda, Provincia de
Sierra Gorda, Región del Antofagasta, tal como se muestra en la siguiente figura. El proyecto se ubica
prácticamente en el límite con la comuna de Antofagasta, a 20 km al oeste de la localidad de
Baquedano, a 93 km al suroeste de la localidad de Sierra Gorda y a 57 km al este de la ciudad de
Antofagasta.

**Figura 1. Ubicación proyecto.**

Antofagasta

El presente informe corresponde a la modelación de dispersión de material particulado respirable,
debido a las emisiones generadas por el proyecto sometido a evaluación.

La modelación se realizará con el modelo CALPUFF, tal como se menciona en la “Guía para el uso de
modelos de calidad del aire en el SEIA”, publicada por el Servicio de Evaluación Ambiental en 2012,
dado principalmente por la topografía compleja de la zona y la extensión de la zona de influencia del
proyecto.

Informe de Calidad del Aire Pág. 3

_PROYECTO “CENTRO DE RECEPCIÓN Y DISPOSICIÓN FINAL DE BIOSÓLIDOS”_

**2** **AREA DE INFLUENCIA**

De acuerdo con la definición indicada en la letra a), artículo 2, del RSEIA, el área de influencia de un
Proyecto corresponde “al área o espacio geográfico, cuyos atributos, elementos naturales o
socioculturales deben ser considerados con la finalidad de definir si el Proyecto o actividad genera o
presenta alguno de los efectos, características o circunstancias del artículo 11 de la Ley, o bien para
justificar la inexistencia de dichos efectos, características o circunstancias”.

En este marco, el área de influencia de cada componente ambiental ha considerado la superficie donde
se prevea que el Proyecto podría generar eventualmente algún “Efecto Adverso Significativo sobre la
cantidad y calidad de los recursos naturales renovables, incluidos, suelo, agua y aire”. Para definir dicha
área, se ha tenido en consideración lo siguiente:

- Las características del Proyecto;

- El emplazamiento de las partes del Proyecto, obras o acciones;

- Las etapas del Proyecto (construcción y operación);

- Las características del medio en que se emplaza el Proyecto;

- Las emisiones, efluentes o residuos generados por el Proyecto, que pudieran afectar el medio
ambiente.

Por su parte, la letra d) del artículo 18 del RSEIA, señala que el área de influencia debe ser determinada
y justificada para cada elemento afectado del medio ambiente, tomando en consideración los impactos
ambientales potencialmente significativos sobre ellos, así como el espacio geográfico en el cual se
emplazarán las partes, obras y/o acciones del Proyecto.

Particularmente para la componente Calidad del Aire y siguiendo el lineamiento de la “Guía para la
Descripción de la Calidad del Aire en el Área de Influencia de Proyectos que Ingresan al SEIA”, se
determina que, dada la naturaleza de las emisiones del Proyecto (dado principalmente por tránsito de
vehículos), estas son de rápida dispersión y decantamiento, y también por la geografía del área del
Proyecto.

Los principales efectos potenciales de las actividades del Proyecto sobre la calidad del aire son el
deterioro temporal por emisiones de material particulado y gases de combustión, sobre las áreas de
trabajo y efectos sobre las poblaciones cercanas durante la etapa de construcción. Éstas son de
carácter puntual ya que se concentran en la zona del trazado del Proyecto u obras y originarán la
emisión de gases de combustión y material particulado procedente del uso y tránsito de maquinaria,
equipos y camiones.

En el área de influencia del proyecto se encuentra en el sector sur-oeste de la comuna de Sierra Gorda,
siendo la localidad más cercana Baquedano, distante a 20 km y la faena minera Mantos Blancos (8.5
km).

Por todo lo anterior, el área de influencia se determina como un área cuadrada con el proyecto en el
centro y una arista de 25 km, tal como se muestra en la siguiente figura.

Informe de Calidad del Aire Pág. 4

_PROYECTO “CENTRO DE RECEPCIÓN Y DISPOSICIÓN FINAL DE BIOSÓLIDOS”_

**Figura 2. Diagrama de la Zona de Influencia del proyecto.**

Area de Influencia

Minera

Mantos

Balncos

Proyecto

Baquedano

Informe de Calidad del Aire Pág. 5

_PROYECTO “CENTRO DE RECEPCIÓN Y DISPOSICIÓN FINAL DE BIOSÓLIDOS”_

**3** **MODELACIÓN DE CONTAMINANTES**

**3.1** **TEORIA DE LA DISPERSIÓN DE LOS CONTAMINANTES.**

Las emisiones consideradas para la modelación de dispersión corresponden a MP10, debido a que es
el contaminante más crítico para este tipo de proyectos que se genera en varias fuentes adicionales
que tienen que ver más con los movimientos de tierra y no solo con la combustión de fuentes móviles.

La dispersión de contaminantes en la atmósfera se realiza con el modelo computacional CALMET /
CALPUFF, desarrollado y mantenido actualmente por ASG (Atmospheric Studies Group) en la empresa
TRC Environmental Corporation (basada en Estados Unidos). Este modelo es considerado por el
Servicio de Evaluación Ambiental de Chile como modelo predeterminado para operaciones de largo
alcance (sobre 5 km) y para terrenos complejos según se especifica en la “ **Guía para el Uso de**
**Modelos de Calidad del Aire en el SEIA, 2012** ”. Dado que el Proyecto se sitúa en la cuenca del rio
Maipo la cual presenta una geografía compleja, se utilizará este modelo para estimar el impacto de la
dispersión de las emisiones de MP10.

Los datos meteorológicos corresponden al año 2021 y han sido obtenidos a partir del modelo
meteorológico WRF (Weather Research and Forecasting), que genera información para ser utilizada
en el modelo CALMET (Pre-procesador meteorológico del modelo CALPUFF). La modelación
considera fuentes de tipo superficiales para las actividades de movimientos de tierra (Escarpe,
excavaciones y carga / descarga de material en el botadero) y fuentes tipo volumétricas para las fuentes
móviles (combustión y tráfico).

La dispersión ocurre cuando un flujo continuo de contaminantes es liberado a la atmósfera abierta, el
cual inicialmente sube y luego el flujo es torcido, por efecto de un viento que disuelve los contaminantes
y los lleva lejos de la fuente, dispersándolo en dirección horizontal y vertical de una línea de centro
imaginaria.

Un esquema de este flujo doblado se presenta en la Figura N° 3-1, en donde h corresponde a la altura
física de la chimenea, h es la subida del flujo y H la altura efectiva del flujo disperso. Esta dispersión
avanza desde una concentración alta a una concentración baja. Provocada por diferentes factores,
tales como lo relacionado con la difusión molecular de los componentes de los gases.

**Figura N° 3-1: Esquema del efluente.**

Fuente: Noel de Nevers, Air Pollution Control Engineering, 1995.

Informe de Calidad del Aire Pág. 6

_PROYECTO “CENTRO DE RECEPCIÓN Y DISPOSICIÓN FINAL DE BIOSÓLIDOS”_

Para una mejor comprensión, se debe recordar que todo flujo turbulento presenta vórtices o remolinos
en distintas direcciones, laterales y verticales, los cuales son fluctuaciones microscópicas irregulares
que al interceptar parte del flujo transforma la concentración de contaminantes en aire limpio a alguna
distancia lejos de la fuente.

Estos remolinos son debidos a influencias térmicas y mecánicas. La energía térmica está dada por la
energía del sol que es absorbida por el suelo y convertida en calor, la que es transmitida a los niveles
más bajos del aire por conducción y convección, creando así los remolinos térmicos. Los remolinos
mecánicos se deben a las fuerzas de corte producidas cuando el aire sopla a través de una superficie
áspera, como es el caso de las superficies con árboles y edificios.

Para modelar la dispersión de estas emisiones, es necesario utilizar programas computacionales, los
que se diferencian básicamente por los algoritmos utilizados respecto de la química atmosférica de los
contaminantes, la distancia entre la fuente y los receptores, meteorología local versus global, etc.

**3.1.1 Tipos de modelos de dispersión**

Actualmente existen básicamente dos tipos de modelos utilizados para evaluación ambiental, modelos
Gaussianos y del tipo “puff”, que corresponde a una variación de un modelo Lagrangeano. Cabe señalar
que existe también una serie de modelos denominados “screen” que se utilizan con el objeto de
determinar la necesidad de usar un modelo refinado. Este tipo de modelos sólo se utiliza para decidir
si se debe hacer una estimación de impactos a través de modelación.

Los modelos Gaussianos describen la distribución tridimensional de una pluma bajo condiciones
meteorológicas y de emisiones estacionarias. Las concentraciones se estiman en base a una
distribución Gaussiana cuyos parámetros dependen de las condiciones meteorológicas. Aunque
existen modelos Gaussianos que incluyen algún algoritmo para considerar terreno complejo, sus
conceptos matemáticos son fundamentalmente iguales a aquellos modelos que no lo hacen.

**Figura N° 3-2: Diferencia de modelación entre modelos Gausseanos y PUFF.**

Fuente: Lakes Environmental, Puff vs Plume. www.weblakes.com.

Los modelos tipo “puff” son una combinación entre los modelos Gaussianos y los modelos
Lagrangeanos, en el sentido de que esencialmente calculan la dispersión de contaminantes
provenientes de una emisión instantánea, llamada “puff”, a lo largo de una trayectoria. Su aproximación
matemática consiste en estimar la dispersión en forma Gaussiana en cada punto de una trayectoria; es

Informe de Calidad del Aire Pág. 7

_PROYECTO “CENTRO DE RECEPCIÓN Y DISPOSICIÓN FINAL DE BIOSÓLIDOS”_

decir, a diferencia de los modelos Langrangeanos que necesitan el cálculo de un gran número de
trayectorias para una fuente, los modelos tipo “puff” sólo requieren una trayectoria por “puff”, lo que
hace su cálculo mucho más rápido. En el caso de emisiones continuas, se simulan las trayectorias y la
dispersión Gaussiana de muchos “puffs”.

La diferencia entre los modelos Gaussianos y del tipo “puff” se basa en la precisión que pueden tener
a medida que la estimación se aleja de la fuente, en que la meteorología local pierde representatividad,
o se enfrenta a un cambio brusco en las condiciones meteorológicas, tales como una topografía
accidentada, que desvía el campo de vientos.

En el caso de este Proyecto, y siguiendo la “Guía para el uso de modelos de calidad del aire” elaborada
por el Servicio de Evaluación Ambiental, se ha seleccionado el modelo CALPUFF, que corresponde a
una modelación de tipo “puff” para geografías complejas.

**3.1.2 Modelo Calpuff**

El modelo CALPUFF es un programa de modelación que se compone de tres sub-rutinas:

CALMET: Modelo meteorológico que posee un generador de diagnóstico de campos de vientos y que
contiene un análisis objetivo y tratamiento parametrizado de curvas de flujos, efectos cinéticos del
terreno, efectos de bloqueo por la topografía, una rutina de minimización de divergencia y un modelo
de micro-meteorología para capas límites en suelo y agua.

CALPUFF: Programa de modelación Lagrangeano para condiciones no estacionarias que se desarrolla
a partir del campo de vientos elaborado por CALMET. Además, contiene módulos para terrenos
complejos, transporte de contaminantes sobre agua y efectos de interacción con el frente costero,
interferencias con edificios, depositación húmeda y seca y transformación química simple.

CALPOST: Es una rutina de procesamiento posterior con opciones para calcular las concentraciones y
depositaciones en distintos promedios de tiempos y flujos de depositación determinados por CALPUFF.
Este programa calcula el impacto en la visibilidad de acuerdo con las recomendaciones de IWAQM
(Interagency Workgroup on Air Quality Modeling - Grupo de Interagencias para la Modelacion de
Calidad del Aire) y el documento FLAG 2010.

**3.2** **METEOROLOGÍA**

Los datos meteorológicos utilizados para el Proyecto corresponden a estimaciones del modelo
meteorológico WRF, el cual provee información respecto a la meteorología local como meteorología de
altura.

El modelo WRF (Weather Research and Forecasting) es un sistema numérico de última generación
para predicción del clima, diseñado para servir tanto para la investigación atmosférica como las
necesidades de predicción operativa. Cuenta con dos núcleos dinámicos, un sistema de asimilación de
datos y una arquitectura de software que facilita el cálculo en paralelo y la extensibilidad del sistema.
El modelo ofrece una amplia gama de aplicaciones meteorológicas entre las escalas de decenas de
metros a miles de kilómetros.

El esfuerzo para desarrollar WRF comenzó en la última parte de la década de 1990 y era una asociación
de colaboración principalmente entre el Centro Nacional de Investigación Atmosférica (NCAR), la
Administración Nacional Oceánica y Atmosférica (representado inicialmente por los Centros Nacionales

Informe de Calidad del Aire Pág. 8

_PROYECTO “CENTRO DE RECEPCIÓN Y DISPOSICIÓN FINAL DE BIOSÓLIDOS”_

de Predicción Ambiental (NCEP) y luego por el Laboratorio de Pronóstico de Sistemas (FSL)), la
Agencia de Clima de la Fuerza Aérea (AFWA), el Laboratorio de Investigación Naval, la Universidad de
Oklahoma, y la Administración Federal de Aviación (FAA), todos organismos vigentes en Estados
Unidos de Norte América.

El modelo WRF permite a los investigadores la capacidad de producir simulaciones que reflejan datos
reales (observaciones, análisis) o bien condiciones atmosféricas idealizadas.

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||d<br>va|más, ofrece una predicción op<br>nces en la física, métodos numé|rativa de una plataforma flexible<br>icos, y la asimilación de datos ap|y robu<br>rtados|ta,<br>or d|ie<br>esa|tra<br>rrol|q<br>lad|ue<br>re|ue<br>re|ofr<br>s d|ce<br> la|
||||com|unidad de investigación.|||||||||||
||||<br>||||||||||||
||||**Fig**|**ura N° 3-3: Campo de vientos mod**|**elado con WRF.**||||||||||
|||||**N**||||||ers|||||
|||||**N**||||||ers|||||
||||22|||||||met|||||
||||7||||||||||154|1|
||||7||||||||||||
||||20||||||||||||
||||7|||<br>|**Ba**~~**qu**~~**e**|**dano**|||||150|0|
||||7|||<br>|**Ba**~~**qu**~~**e**|**dano**|||||||
||||418||||||||||||
||||||||||||||10|0|
||||16||||||||||||
||||7||||||||||950||
||||7||||||||||||
||||14||||||||||||
||||7||||||||||900||
||||7||||||||||||
||||412<br>km]||||||||||||
||||rth [||||||||||85||
||||10<br>M No||||||||||||
||||7<br>UT|<br>|||||||||80||
||||08|~~**M**~~**I**~~**n**~~**era**<br>**Mantos B**~~**lanc**~~**os**<br>|||||||||||
||||7||||||||||||
||||7406||||||||||75||
||||04||<br>**Pro**~~**ye**~~**ct**~~**o**~~||||||||700||
||||7||||||||||||
||||02||||||||||65||
||||7||||||||||||
||||00||||||||||60||
||||7|||||||ations|||||
||||98|||||||Elev|||550||
||||98|||||||Elev|||||
||||7|||||||errain|||||
||||7||||||||||||
|||||392<br>394<br>396<br>398<br>|00<br>402<br>404<br>406<br>408<br>41<br>UTM East [km]|412|41|||T|||523|<br>|
||||Fue<br>|nte: Elaboración propia.|||||||||||
||||||||||||||||
||||as<br>on|flechas en la figura indican la<br>siderada.|dirección del viento en cada un|de los|se|me|to|d|l|l|g|illa|
||||||||||||||||
||||||||||||||||
|||I|nfo|rme de Calidad del Aire|||||||P|P|ág.|9|
||||||||||||||||
||||||||||||||||

_PROYECTO “CENTRO DE RECEPCIÓN Y DISPOSICIÓN FINAL DE BIOSÓLIDOS”_

**3.3** **ANALISIS DE INCERTIDUMBRE**

Cualquier modelo (meteorológico o de calidad del aire) representa una aproximación a la realidad y, en
consecuencia, sus resultados tienen incertidumbres asociadas. Estas incertidumbres se expresan a
través de las diferencias entre lo estimado y las observaciones (o errores del modelo). Además, cabe
enfatizar que existe una propagación de errores desde la modelación meteorológica y la estimación de
emisiones hasta la calidad del aire, lo que resulta en una mayor incertidumbre en esta última.

Para realizar el análisis de incertidumbre se consideraron las recomendaciones establecidas en la
“Guía para el uso de Modelos de calidad del aire en el SEIA” elaborada por Servicio de Evaluación
Ambiental en 2012, capítulo 7, que menciona que cualquier modelo representa una aproximación a la
realidad y sus resultados tienen incertidumbres asociadas, las cuales se expresan a través de
diferencias entre lo estimado y lo observado.

Sin embargo, en la zona cercana al proyecto (30 km a la redonda) no se encuentra ninguna estación
de monitoreo meteorológico representativo que permita comprobar la certeza de los datos
meteorológicos modelados con WRF.

Informe de Calidad del Aire Pág. 10

_PROYECTO “CENTRO DE RECEPCIÓN Y DISPOSICIÓN FINAL DE BIOSÓLIDOS”_

**3.4** **TOPOGRAFIA**

La información topográfica del área de emplazamiento del Proyecto utilizada en el modelo WRF,
corresponde a proyecciones topográficas digitales de las misiones de los transbordadores espaciales
SRTM1 (Shuttle Radar Topography Mission), con mediciones cada 30 metros.

1541

1500

1000

950

900

850

800

750

700

650

600

550

523

|Col1|a 4: Proyección topográfica de la zona de modelación.|Col3|Col4|
|---|---|---|---|
|||||
||<br> <br> <br>**Pro**~~**ye**~~**ct**~~**o**~~<br>~~**M**~~**I**~~**n**~~**era**<br>**Mantos B**~~**lanc**~~**os**<br>**Ba**~~**qu**~~**edano**<br>**N**|<br> <br> <br>**Pro**~~**ye**~~**ct**~~**o**~~<br>~~**M**~~**I**~~**n**~~**era**<br>**Mantos B**~~**lanc**~~**os**<br>**Ba**~~**qu**~~**edano**<br>**N**|<br> <br> <br>**Pro**~~**ye**~~**ct**~~**o**~~<br>~~**M**~~**I**~~**n**~~**era**<br>**Mantos B**~~**lanc**~~**os**<br>**Ba**~~**qu**~~**edano**<br>**N**|
|||||

392 394 396 398 400 402 404 406 408 410 412 414

UTM East [km]

Fuente: Elaboración propia.

La información relacionada con el uso de suelo de la zona fue obtenida a través de los archivos Global
Land Cover Characterization (GLCC) publicados por el U.S. Geological Survey (USGS) y disponibles
en Internet para utilización abierta en proyectos de variada índole [1] .

El escenario de modelación considera la emisión simultánea de todas las fuentes (de modo de
considerar el peor escenario), a pesar de que en la realidad la emisión proviene por etapas.

1 [http://www.webgis.com/glcc.html)](http://www.webgis.com/glcc.html)

Informe de Calidad del Aire Pág. 11

_PROYECTO “CENTRO DE RECEPCIÓN Y DISPOSICIÓN FINAL DE BIOSÓLIDOS”_

**3.5** **RECEPTORES**

La modelación ha considerado una grilla rectangular de receptores de 26 km (Este-Oeste) por 21 km
(Norte-Sur) que abarca un área total de 546 km [2] .

La grilla considerada, tiene receptores cada 500 metros, de modo de hacer un análisis fino de la calidad
del aire en el área de desarrollo del Proyecto. Cada punto de la figura siguiente corresponde a un
receptor de la grilla, totalizando 1500 receptores en la grilla.

**Figura 5:** **Proyección grilla de receptores.**

1541

1500

1000

950

900

850

800

750

700

650

600

550

523

390 392 394 396 398 400 402 404 406 408 410 412 414

UTM East [km]

Fuente: Elaboración propia.

Informe de Calidad del Aire Pág. 12

_PROYECTO “CENTRO DE RECEPCIÓN Y DISPOSICIÓN FINAL DE BIOSÓLIDOS”_

**3.6** **EMISIONES**

Se presenta a continuación las emisiones del proyecto y de los proyectos adyacentes.

**Tabla 1: Emisiones declaradas del proyecto - año 2074**

<!-- INICIO TABLA 1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **3.6** **EMISIONES** Se presenta a continuación las emisiones del proyecto y de los proyectos adyacentes. -->

**Tabla 1: Emisiones declaradas del proyecto - año 2074****

| Fuente de emisión MP10 MP2.5 CO NOx<br>ton/año ton/año ton/año ton/año | Col2 | Col3 | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| Operación fase 3 PTAS | 2.88 | 0.31 | 0.12 | 0.31 |
| Cierre Fase 3 monorelleno y<br>desmantelamiento | 1.21 | 0.15 | 0.15 | 0.56 |
| **TOTAL** | **4.08** | **0.47** | **0.27** | **0.87** |

<!-- Estadísticas: 3 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- **3.7** **RESULTADOS DE LA MODELACIÓN** La siguiente tabla muestra los resultados obtenidos del modelo para determinar la dispersión de los contaminantes en la localidad de Baquedano. -->
<!-- FIN TABLA 1 -->


|Fuente de emisión MP10 MP2.5 CO NOx<br>ton/año ton/año ton/año ton/año|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|Operación fase 3 PTAS|2.88|0.31|0.12|0.31|
|Cierre Fase 3 monorelleno y<br>desmantelamiento|1.21|0.15|0.15|0.56|
|**TOTAL**|**4.08**|**0.47**|**0.27**|**0.87**|

**3.7** **RESULTADOS DE LA MODELACIÓN**

La siguiente tabla muestra los resultados obtenidos del modelo para determinar la dispersión de los
contaminantes en la localidad de Baquedano.

**-**
**Tabla 2: Resultados de modelación de Dispersión en Baquedano (E: 413,754** **N: 7,419,241)**

<!-- INICIO TABLA 2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- La siguiente tabla muestra los resultados obtenidos del modelo para determinar la dispersión de los contaminantes en la localidad de Baquedano. **-** -->

**Tabla 2: Resultados de modelación de Dispersión en Baquedano (E: 413,754** **N: 7,419,241)****

| Aporte Norma % Respecto a<br>Contaminante Período<br>[[g/m3N] [[g/m3N] norma | Col2 | Col3 | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| MP10 | 24 hr | 0.006 | 130 | 0.0046% |
| MP10 | Anual | 0.0009 | 50 | 0.0018% |
| MP2.5 | 24 hr | 0.0007 | 50 | 0.0014% |
| MP2.5 | Anual | 0.0001 | 20 | 0.0005% |
| **CO** | 1 hr | 0.004 | 30,000 | 0.0000% |
| **CO** | 8 hr | 0.003 | 10,000 | 0.0000% |
| **NO2** | 1 hr | 0.004 | 400 | 0.0010% |
| **NO2** | Anual | 0.00006 | 100 | 0.0001% |

<!-- Estadísticas: 8 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- La siguiente tabla muestra los resultados obtenidos del modelo para determinar la dispersión de material particulado en la zona de máximo impacto como cercana al proyecto. **Tabla 3: Resultados de modelación de Dispersión en punto de máximo impacto (PMI)** -->
<!-- FIN TABLA 2 -->


|Aporte Norma % Respecto a<br>Contaminante Período<br>[[g/m3N] [[g/m3N] norma|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|MP10|24 hr|0.006|130|0.0046%|
|MP10|Anual|0.0009|50|0.0018%|
|MP2.5|24 hr|0.0007|50|0.0014%|
|MP2.5|Anual|0.0001|20|0.0005%|
|**CO**|1 hr|0.004|30,000|0.0000%|
|**CO**|8 hr|0.003|10,000|0.0000%|
|**NO2**|1 hr|0.004|400|0.0010%|
|**NO2**|Anual|0.00006|100|0.0001%|

La siguiente tabla muestra los resultados obtenidos del modelo para determinar la dispersión de
material particulado en la zona de máximo impacto como cercana al proyecto.

**Tabla 3: Resultados de modelación de Dispersión en punto de máximo impacto (PMI)**

<!-- INICIO TABLA 3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |**NO2**|Anual|0.00006|100|0.0001%| La siguiente tabla muestra los resultados obtenidos del modelo para determinar la dispersión de material particulado en la zona de máximo impacto como cercana al proyecto. -->

**Tabla 3: Resultados de modelación de Dispersión en punto de máximo impacto (PMI)****

| Contaminante Período Aporte Norma % Aporte Coord. E Coord. N<br>[[g/m3N] [[g/m3N] respecto a [m] [m]<br>norma | Col2 | Col3 | Col4 | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| MP10 | 24 hr | 0.84 | 130 | 0.65% | 397,900 | 7,404,300 |
| MP10 | Anual | 0.36 | 50 | 0.72% | 394,900 | 7,419,242 |
| MP2.5 | 24 hr | 0.13 | 50 | 0.26% | 399,900 | 7,404,300 |
| MP2.5 | Anual | 0.06 | 20 | 0.30% | 399,900 | 7,404,300 |
| CO | 1 hr | 4.06 | 30,000 | 0.01% | 399,900 | 7,404,300 |
| CO | 8 hr | 1.68 | 10,000 | 0.02% | 399,900 | 7,404,300 |
| NO2 | 1 hr | 3.45 | 400 | 0.86% | 399,900 | 7,404,300 |
| NO2 | Anual | 0.20 | 100 | 0.20% | 399,900 | 7,404,300 |

<!-- Estadísticas: 8 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- Se presentan a continuación los gráficos de iso-concentración. Informe de Calidad del Aire Pág. 13 -->
<!-- FIN TABLA 3 -->


|Contaminante Período Aporte Norma % Aporte Coord. E Coord. N<br>[[g/m3N] [[g/m3N] respecto a [m] [m]<br>norma|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|MP10|24 hr|0.84|130|0.65%|397,900|7,404,300|
|MP10|Anual|0.36|50|0.72%|394,900|7,419,242|
|MP2.5|24 hr|0.13|50|0.26%|399,900|7,404,300|
|MP2.5|Anual|0.06|20|0.30%|399,900|7,404,300|
|CO|1 hr|4.06|30,000|0.01%|399,900|7,404,300|
|CO|8 hr|1.68|10,000|0.02%|399,900|7,404,300|
|NO2|1 hr|3.45|400|0.86%|399,900|7,404,300|
|NO2|Anual|0.20|100|0.20%|399,900|7,404,300|

Se presentan a continuación los gráficos de iso-concentración.

Informe de Calidad del Aire Pág. 13

_PROYECTO “CENTRO DE RECEPCIÓN Y DISPOSICIÓN FINAL DE BIOSÓLIDOS”_

Figura 3. Resultado modelación de dispersión de MP10 (anual)

**N**

Informe de Calidad del Aire Pág. 14

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|Col26|Col27|Col28|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||||||||||||0|0|
|||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||

_PROYECTO “CENTRO DE RECEPCIÓN Y DISPOSICIÓN FINAL DE BIOSÓLIDOS”_

**Figura 4. Resultado modelación de dispersión de MP10 (diario)**

**N**

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|Col26|Col27|Col28|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||||||||||||0<br>|0<br>|
|||||||||||||||||||||||||||||
|||||||||||||||||||||||||||0|0|
|||||||||||||||||||||||||||||
||||||||||||UT|M East [k|m]|||||||||||||||
||||<br> <br>|||||||||||||||||||||||||
|||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||

Informe de Calidad del Aire Pág. 15

_PROYECTO “CENTRO DE RECEPCIÓN Y DISPOSICIÓN FINAL DE BIOSÓLIDOS”_

**Figura 5. Resultado modelación de dispersión de MP2.5 (anual)**

**N**

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|Col26|Col27|Col28|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||||||||||||0<br>|0<br>|
|||||||||||||||||||||||||||||
|||||||||||||||||||||||||||0|0|
|||||||||||||||||||||||||||||
||||<br> <br> <br>|||||||||||||||||||||||||
|||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||

Informe de Calidad del Aire Pág. 16

_PROYECTO “CENTRO DE RECEPCIÓN Y DISPOSICIÓN FINAL DE BIOSÓLIDOS”_

**Figura 6. Resultado modelación de dispersión de MP2.5 (diario)**

**N**

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|Col26|Col27|Col28|Col29|Col30|Col31|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||||||||||||||||||0|0|
|||||||||||||0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|||||
|||||||||||||0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|||||
|||||||||||||||UTM|East [k|m]|||||||||||||||
||||<br>||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||

Informe de Calidad del Aire Pág. 17

_PROYECTO “CENTRO DE RECEPCIÓN Y DISPOSICIÓN FINAL DE BIOSÓLIDOS”_

**Figura 7. Resultado modelación de dispersión de CO (1 h)**

**N**

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|Col26|Col27|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||||||||||||||4|4|
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||
||||||||||||||||||||||||||||

Informe de Calidad del Aire Pág. 18

_PROYECTO “CENTRO DE RECEPCIÓN Y DISPOSICIÓN FINAL DE BIOSÓLIDOS”_

**Figura 8. Resultado modelación de dispersión de CO (8 h)**

**N**

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|Col26|Col27|Col28|Col29|Col30|Col31|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||||||||||||||||||1<br>|1<br>|
||||||||||||||||||||||||||||||||
|||||||||||||0<br>8|0<br>8|0<br>8|0<br>8|0<br>8|0<br>8|0<br>8|0<br>8|0<br>8|0<br>8|0<br>8|0<br>8|0<br>8|0<br>8|0<br>8|0<br>8|0<br>8|0<br>8|0<br>8|
|||||||||||||0<br>8|0<br>8|0<br>8|0<br>8|0<br>8|0<br>8|0<br>8|0<br>8|0<br>8|0<br>8|0<br>8|0<br>8|0<br>8|0<br>8|0<br>8|||0|0|
|||||||||||||0<br>8|0<br>8|0<br>8|0<br>8|0<br>8|0<br>8|0<br>8|0<br>8|0<br>8|0<br>8|0<br>8|0<br>8|0<br>8|0<br>8|0<br>8|||||
||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||

Informe de Calidad del Aire Pág. 19

_PROYECTO “CENTRO DE RECEPCIÓN Y DISPOSICIÓN FINAL DE BIOSÓLIDOS”_

**Figura 9. Resultado modelación de dispersión de NO** **2** **(1 h)**

**N**

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|Col26|Col27|Col28|Col29|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||||||||||||||||3|3|
||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||

Informe de Calidad del Aire Pág. 20

_PROYECTO “CENTRO DE RECEPCIÓN Y DISPOSICIÓN FINAL DE BIOSÓLIDOS”_

**Figura 10. Resultado modelación de dispersión de NO** **2** **(Anual)**

**N**

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|Col26|Col27|Col28|Col29|Col30|Col31|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||||||||||||||||||0|0|
||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||

Informe de Calidad del Aire Pág. 21

_PROYECTO “CENTRO DE RECEPCIÓN Y DISPOSICIÓN FINAL DE BIOSÓLIDOS”_

**4** **CONCLUSIONES**

El proyecto no es intensivo en generación de emisiones atmosféricas, dado el nivel de movimientos de
tierra, las que son de corta duración. Las mayores emisiones se generan en el año 2074, donde ocurren
al mismo tiempo la operación de la fase 3 de la PTAS y el cierre de la etapa 3 del monorrelleno.

Desde el punto de vista de dispersión de contaminantes se aprecia que la emisión se dispersa
rápidamente, debido a la baja energía ascendente del flujo de emisión, típico de las actividades de
movimientos de tierra, que al no tener suficiente momentum se dispersa y decae rápidamente.

En las figuras de iso-concentración se aprecia que la dispersión se focaliza principalmente en el área
del proyecto y el camino de acceso, dispersándose rápidamente debido a la geografía y características
meteorológicas del área.

Con relación al Punto de Máximo Impacto (PMI) este se ubica dentro del área del proyecto. Cabe
señalar que aproximadamente la mitad de las emisiones son por el tránsito de vehículos en caminos
no pavimentados, que se generan tanto en la etapa de construcción como en la operación y cierre. Los
resultados de la modelación de dispersión en este punto de máximo impacto generan un aporte inferior
al 0.1% de la respectiva norma de calidad del aire, en todos los períodos de tiempo.

Con respecto a los resultados de la modelación de dispersión en la localidad de Baquedano, los niveles
de aporte son inferiores al 0.01% de sus respectivas normas de calidad del aire en todos los períodos
de tiempo establecidos.

Los resultados de la modelación de dispersión de emisiones atmosféricas permiten confirmar que el
área de influencia directa del Proyecto como un cuadrado de 25 km de arista con el proyecto en el
centro de este. Esta distancia está dada por la distancia a Baquedano, a pesar de que los resultados
muestran que a 3 km de distancia el aporte del proyecto es prácticamente nulo.

Se entiende que si los niveles de aporte por dispersión de contaminantes del proyecto en el año de
mayor emisión cumplen con la normativa vigente, en los años de menor emisión también se cumplirá
la condición, lo que garantiza la salud de las personas de acuerdo con lo planteado en la “Guía de
evaluación de impacto ambiental riesgo para la salud de la población en el SEIA”, publicada por SEA
en 2012.

Informe de Calidad del Aire Pág. 22

_PROYECTO “CENTRO DE RECEPCIÓN Y DISPOSICIÓN FINAL DE BIOSÓLIDOS”_

**5** **REFERENCIAS BIBLIOGRAFICAS**

1. Air Pollution Control Engineering, N. De Nevers, 1995.
2. Atmospheric dispersion modeling compliance guide, Karl B. Schnelle & Partha R. Dey, 2000.
3. Guía para uso de modelos de calidad del aire en el SEIA. SEA, 2012.
4. Guía de evaluación de impacto ambiental riesgo para la salud de la población en el SEIA. SEA

2012.

5. Guía para la descripción de la calidad del aire en el área de influencia de proyectos que ingresan
al SEIA. SEA, 2015.

6. Guía para la descripción del área de influencia. SEA, 2017
7. DS12/2022 Establece norma de calidad primaria para material particulado respirable MP10,

Ministerio del Medio Ambiente.

8. DS12/2011. Establece norma primaria de calidad ambiental para material particulado fino
respirable MP2.5, Ministerio del Medio Ambiente.
9. DS114/2002. Establece norma primaria de calidad de aire para Dióxido de Nitrógeno (NO 2 ),
Ministerio Secretaria General de la Presidencia de la República.
10. DS115/2002. Establece norma primaria de calidad de aire para Monóxido de Carbono, Ministerio
Secretaria General de la Presidencia de la República.

Informe de Calidad del Aire Pág. 23