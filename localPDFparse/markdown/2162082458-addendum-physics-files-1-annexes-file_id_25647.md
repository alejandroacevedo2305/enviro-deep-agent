---
title: INFORME DE MODELACION DE DISPERSIÓN EMISIONES ATMOSFERICAS
author: IGNACIO GOIC
date: D:20241231101212-03'00'
language: es
type: report
pages: 23
has_toc: False
has_tables: True
extraction_quality: high
---

_Nuevo Nuevo Proyecto Inmobiliario Hacienda Lo Errázuriz_

**INDICE GENERAL**

**1** **INTRODUCCION** **3**

**2** **AREA DE INFLUENCIA** **4**

**3** **RESUMEN DE EMISIONES** **7**

**4** **MODELACIÓN DE CONTAMINANTES** **8**

**4.1** **TEORÍA DE LA DISPERSIÓN DE LOS CONTAMINANTES.** **8**

4.1.1 T IPOS DE MODELOS DE DISPERSIÓN 9

4.1.2 M ODELO C ALPUFF 10
**4.2** **METEOROLOGÍA** **10**

**4.3** **ANALISIS DE INCERTIDUMBRE** **12**
**4.4** **TOPOGRAFÍA** **14**

**4.5** **RECEPTORES** **15**

**4.6** **LINEA BASE CaliDAD DEL AIRE** **16**
**4.7** **RESULTADOS DE LA MODELACIÓN** **16**

**5** **CONCLUSIONES** **22**

**6** **REFERENCIAS BIBLIOGRÁFICAS** **23**

Informe de Calidad del Aire Pág. 2

_Nuevo Nuevo Proyecto Inmobiliario Hacienda Lo Errázuriz_

**1** **INTRODUCCION**

El Nuevo Proyecto Inmobiliario Hacienda Lo Errázuriz, en adelante "el Proyecto", consiste en la
construcción y posterior operación de un conjunto de condominios que contempla 880 departamentos,
equipamiento, comercio y 695 estacionamientos, en una superficie bruta de 89.418,58 m [2], estimándose
su construcción en aproximadamente 28 meses.

El Proyecto se llevará a cabo una zona urbana de la comuna de Cerrillos de la Región Metropolitana
de Santiago, específicamente en Av. Lo Errázuriz a 120 metros aproximadamente de la Autopista
General Velásquez. Según la ordenanza vigente del Plan Regulador Metropolitano de Santiago, en su
Resolución 118 publicado en el Diario Oficial el 11 de noviembre de 2016, la zonificación en la que se
emplaza el Proyecto pertenece a un área de extensión urbana cuyos usos de suelo están definidos
como del tipo “ZMH3 - Zona de Uso Mixto Preferentemente Residencial en Densidad Media”,
permitiendo el uso Residencial, Equipamiento, Área Verde y Espacio Público, por lo que el Proyecto es
compatible con los usos de suelo permitidos..

**Figura 1. Ubicación proyecto.**

_Fuente: Capítulo 1 de la DIA._

El presente informe corresponde a la modelación de dispersión de material particulado respirable,
debido a las emisiones generadas por la operación actual, construcción y operación del proyecto.

La modelación se realizará con el modelo CALPUFF, tal como se menciona en la “Guía para el uso de
modelos de calidad del aire en el SEIA” (en adelante, “Guía para el uso de modelos de calidad del
aire”), publicada por el Servicio de Evaluación Ambiental en 2023, dado principalmente por la
declaración de zona saturada por MP10 y MP2.5.

Informe de Calidad del Aire Pág. 3

_Nuevo Nuevo Proyecto Inmobiliario Hacienda Lo Errázuriz_

**2** **AREA DE INFLUENCIA**

De acuerdo con la definición indicada en el literal a), artículo 2, del RSEIA, el AI de un Proyecto
corresponde “ _al área o espacio geográfico, cuyos atributos, elementos naturales o socioculturales_
_deben ser considerados con la finalidad de definir si el Proyecto o actividad genera o presenta alguno_
_de los efectos, características o circunstancias del artículo 11 de la Ley, o bien para justificar la_
_inexistencia de dichos efectos, características o circunstancias_ ”.

En este marco, el área de influencia de cada componente ambiental ha considerado la superficie donde
se prevea que el Proyecto podría generar eventualmente algún “Efecto Adverso Significativo sobre la
cantidad y calidad de los recursos naturales renovables, incluidos, suelo, agua y aire”. Para definir dicha
área, se ha tenido en consideración lo siguiente:

- Las características del Proyecto;

- El emplazamiento de las partes del Proyecto, obras o acciones.

- Las etapas del Proyecto (construcción y operación);

- Las características del medio en que se emplaza el Proyecto;

- Las emisiones, efluentes o residuos generados por el Proyecto, que pudieran afectar el medio

ambiente.

Por su parte, el literal d) del artículo 18 del RSEIA, señala que el AI debe ser determinada y justificada
para cada elemento afectado del medio ambiente, tomando en consideración los impactos ambientales
potencialmente significativos sobre ellos, así como el espacio geográfico en el cual se emplazarán las
partes, obras y/o acciones del Proyecto.

En el ámbito regional, el Proyecto se emplaza en la Región Metropolitana, la cual ha sido declarada
zona saturada por Material Particulado Respirable (PM10) mediante el Decreto Supremo N°131 de
1996 (en adelante, “DS N°131/1996”). Además, el proyecto se ubica en una zona declarada como
saturada por Material Particulado Fino Respirable (PM2.5) mediante el Decreto Supremo N°67 de 2014
(en adelante, “DS N°67/2014”). Por otra parte, la región cuenta con el Plan de Descontaminación
Atmosférica (en adelante, “PDA”) por PM10 para la Región Metropolitana establecido por el Decreto
Supremo N°31 de 2016 (en adelante, “DS N°31/2016”), tal como se aprecia en la siguiente figura:

Particularmente para la componente Calidad del Aire y siguiendo el lineamiento de la “ _**Guía para la**_
_**Descripción de la Calidad del Aire en el Área de Influencia de Proyectos que Ingresan al SEIA**_ ”,
del año 2015, del SEIA (en adelante, “Guía para la Descripción de la Calidad del Aire”), se determina
que, dada la naturaleza de las emisiones y geografía del área del Proyecto, estas son de rápida
dispersión y decantamiento.

Informe de Calidad del Aire Pág. 4

_Nuevo Nuevo Proyecto Inmobiliario Hacienda Lo Errázuriz_

**Figura 2. Ubicación PDA Región Metropolitana.**

_Fuente: Capítulo 1 de la DIA_

Los principales efectos potenciales de las actividades del Proyecto sobre la calidad del aire son el
deterioro temporal por emisiones de material particulado y gases de combustión, sobre las áreas de
trabajo y efectos sobre la población cercana durante la etapa de construcción. Éstas son de carácter
puntual ya que se concentran en la zona del Proyecto u obras y originarán la emisión de gases de
combustión y material particulado procedente del uso y tránsito de maquinaria, equipos y camiones.

Por todo lo anterior, y utilizando el **método de Juicio Experto**, se determina el AI inicial como un área
circular centrada en el proyecto con un radio de 1 km, tal como se muestra en la siguiente figura, donde
el AI corresponde a la zona celeste.

Informe de Calidad del Aire Pág. 5

_Nuevo Nuevo Proyecto Inmobiliario Hacienda Lo Errázuriz_

**Figura 3. AI inicial del proyecto.**

Esta AI inicial será confirmada posteriormente con la modelación de dispersión de las emisiones críticas
(capítulo 3 de este informe), cuyos máximos aportes deben quedar contenidas en el interior de esta.

Informe de Calidad del Aire Pág. 6

_Nuevo Nuevo Proyecto Inmobiliario Hacienda Lo Errázuriz_

**3** **RESUMEN DE EMISIONES**

En la siguiente tabla se presenta un resumen de las emisiones del Proyecto por los primeros años,
correspondiendo los primeros 2 años y 4 meses a la construcción y a partir del quinto mes del tercer
año se va añadiendo la operación de la etapa construida en el año anterior.

**Tabla 1. Resumen de emisiones de Material Particulado [ton/año]**

|Año|Etapa|MP10|MP2.5|
|---|---|---|---|
|1|Construcción|3.82|1.91|
|2|Construcción|0.92|0.73|
|3|Operación|1.66|0.48|
|4 +|Operación|2.38|0.61|

_Fuente: Estudio de emisiones atmosféricas._

Debido a que las mayores emisiones de MP2.5 y MP10 ocurren en el primer año, estas serán las
emisiones las que se modelarán, de modo que, por criterio de inducción, el cumplimiento luego se
extienda a los años de menor emisión.

**Figura 4. Emisiones MP10 y MP2.5 del proyecto en el tiempo.**

Informe de Calidad del Aire Pág. 7

_Nuevo Nuevo Proyecto Inmobiliario Hacienda Lo Errázuriz_

**4** **MODELACIÓN DE CONTAMINANTES**

**4.1** **TEORÍA DE LA DISPERSIÓN DE LOS CONTAMINANTES.**

Las emisiones consideradas para la modelación de dispersión corresponden a MP10, debido a que es
el contaminante más crítico para este tipo de proyectos que se genera en varias fuentes adicionales
que tienen que ver más con los movimientos de tierra y no solo con la combustión de fuentes móviles.

La dispersión de contaminantes en la atmósfera se realiza con el modelo computacional CALMET /
CALPUFF, desarrollado y mantenido actualmente por ASG (Atmospheric Studies Group) en la empresa
TRC Environmental Corporation (basada en Estados Unidos). Este modelo es considerado por el
Servicio de Evaluación Ambiental de Chile como modelo predeterminado para operaciones de largo
alcance (sobre 5 km) y para terrenos complejos según se especifica en la Guía para el uso de modelos
de calidad del aire. Dado que el Proyecto se sitúa en la cuenca de Santiago la cual presenta una
geografía compleja, se utilizará este modelo para estimar el impacto de la dispersión de las emisiones
de MP10.

Los datos meteorológicos corresponden al año 2022 y han sido obtenidos a partir del modelo
meteorológico WRF (Weather Research and Forecasting), que genera información para ser utilizada
en el modelo CALMET (Pre-procesador meteorológico del modelo CALPUFF). La modelación
considera fuentes de tipo superficiales para las actividades de movimientos de tierra (Escarpe,
excavaciones y carga / descarga de material en el botadero) y fuentes tipo volumétricas para las fuentes
móviles (combustión y tráfico).

La dispersión ocurre cuando un flujo continuo de contaminantes es liberado a la atmósfera abierta, el
cual inicialmente sube y luego el flujo es torcido, por efecto de un viento que disuelve los contaminantes
y los lleva lejos de la fuente, dispersándolo en dirección horizontal y vertical de una línea de centro
imaginaria.

Un esquema de este flujo doblado se presenta en la Figura 4, en donde h corresponde a la altura física
de la chimenea, h es la subida del flujo y H la altura efectiva del flujo disperso. Esta dispersión avanza
desde una concentración alta a una concentración baja, provocada por diferentes factores, tales como
lo relacionado con la difusión molecular de los componentes de los gases.

**Figura 5. Esquema del efluente.**

Fuente: Noel de Nevers, Air Pollution Control Engineering, 1995.

Informe de Calidad del Aire Pág. 8

_Nuevo Nuevo Proyecto Inmobiliario Hacienda Lo Errázuriz_

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

**4.1.1 Tipos de modelos de dispersión**

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

**Figura 6. Diferencia de modelación entre modelos Gausseanos y PUFF.**

Fuente: Lakes Environmental, Puff vs Plume. www.weblakes.com.

Los modelos tipo “puff” son una combinación entre los modelos Gaussianos y los modelos
Lagrangeanos, en el sentido de que esencialmente calculan la dispersión de contaminantes

Informe de Calidad del Aire Pág. 9

_Nuevo Nuevo Proyecto Inmobiliario Hacienda Lo Errázuriz_

provenientes de una emisión instantánea, llamada “puff”, a lo largo de una trayectoria. Su aproximación
matemática consiste en estimar la dispersión en forma Gaussiana en cada punto de una trayectoria; es
decir, a diferencia de los modelos Langrangeanos que necesitan el cálculo de un gran número de
trayectorias para una fuente, los modelos tipo “puff” sólo requieren una trayectoria por “puff”, lo que
hace su cálculo mucho más rápido. En el caso de emisiones continuas, se simulan las trayectorias y la
dispersión Gaussiana de muchos “puffs”.

La diferencia entre los modelos Gaussianos y del tipo “puff” se basa en la precisión que pueden tener
a medida que la estimación se aleja de la fuente, en que la meteorología local pierde representatividad,
o se enfrenta a un cambio brusco en las condiciones meteorológicas, tales como una topografía
accidentada, que desvía el campo de vientos.

En el caso de este Proyecto, y siguiendo la Guía para el uso de modelos de calidad del aire, se ha
seleccionado el modelo CALPUFF, que corresponde a una modelación de tipo “puff” para geografías
complejas.

**4.1.2 Modelo Calpuff**

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

**4.2** **METEOROLOGÍA**

Los datos meteorológicos utilizados para el Proyecto corresponden a estimaciones del modelo
meteorológico WRF, el cual provee información respecto a la meteorología local como meteorología de
altura.

El modelo WRF (Weather Research and Forecasting) es un sistema numérico de última generación
para predicción del clima, diseñado para servir tanto para la investigación atmosférica como las
necesidades de predicción operativa. Cuenta con dos núcleos dinámicos, un sistema de asimilación de
datos y una arquitectura de software que facilita el cálculo en paralelo y la extensibilidad del sistema.
El modelo ofrece una amplia gama de aplicaciones meteorológicas entre las escalas de decenas de
metros a miles de kilómetros.

Informe de Calidad del Aire Pág. 10

_Nuevo Nuevo Proyecto Inmobiliario Hacienda Lo Errázuriz_

El esfuerzo para desarrollar WRF comenzó en la última parte de la década de 1990 y era una asociación
de colaboración principalmente entre el Centro Nacional de Investigación Atmosférica (NCAR), la
Administración Nacional Oceánica y Atmosférica (representado inicialmente por los Centros Nacionales
de Predicción Ambiental (NCEP) y luego por el Laboratorio de Pronóstico de Sistemas (FSL)), la
Agencia de Clima de la Fuerza Aérea (AFWA), el Laboratorio de Investigación Naval, la Universidad de
Oklahoma, y la Administración Federal de Aviación (FAA), todos organismos vigentes en Estados
Unidos de Norte América.

El modelo WRF permite a los investigadores la capacidad de producir simulaciones que reflejan datos
reales (observaciones, análisis) o bien condiciones atmosféricas idealizadas.

Además, ofrece una predicción operativa de una plataforma flexible y robusta, mientras que ofrece
avances en la física, métodos numéricos, y la asimilación de datos aportados por desarrolladores de la
comunidad de investigación.

**Figura 7. Campo de vientos modelado con WRF.**

_Fuente: Elaboración propia._

Las flechas en la figura indican la dirección del viento en cada uno de los segmentos de la grilla
considerada.

Informe de Calidad del Aire Pág. 11

_Nuevo Nuevo Proyecto Inmobiliario Hacienda Lo Errázuriz_

**4.3** **ANALISIS DE INCERTIDUMBRE**

Cualquier modelo (meteorológico o de calidad del aire) representa una aproximación a la realidad y, en
consecuencia, sus resultados tienen incertidumbres asociadas. Estas incertidumbres se expresan a
través de las diferencias entre lo estimado y las observaciones (o errores del modelo). Además, cabe
enfatizar que existe una propagación de errores desde la modelación meteorológica y la estimación de
emisiones hasta la calidad del aire, lo que resulta en una mayor incertidumbre en esta última.

Para realizar el análisis de incertidumbre se consideraron las recomendaciones establecidas en la Guía
para el uso de modelos de calidad del aire, capítulo 7, que menciona que cualquier modelo representa
una aproximación a la realidad y sus resultados tienen incertidumbres asociadas, las cuales se
expresan a través de diferencias entre lo estimado y lo observado.

Un análisis de incertidumbre tiene como objetivo evaluar la capacidad de un modelo de representar
una cierta situación atmosférica. En este sentido, es importante señalar que este análisis no es ningún
juicio sobre la bondad del modelo o su usuario, sino sólo un reconocimiento de que ningún modelo es
capaz de representar la atmósfera en forma exacta y que, además, su desempeño depende de cada
situación particular.

Es por lo anterior, que a continuación se evalúan los ajustes meteorológicos del modelo WRF, para
reproducir las observaciones de terreno, medida por una estación de monitoreo cercana al proyecto,
que en este caso corresponde a la estación de monitoreo El Bosque, dado que la estación Cerrillos II
no cuenta con medición meteorológica.

Para la evaluación del modelo, se han considerado las variables disponibles de velocidad del viento y
dirección del viento. Estas variables son de las más importantes en la caracterización meteorológica de
una zona. Del análisis estadístico, se comprueba un coeficiente de correlación del 87.8% para la
velocidad del viento y de un 47.6% para la dirección del viento, lo que implica que ambas variables
modeladas tienen una tendencia similar a los valores reales, lo que valida la modelación meteorológica
y por extensión a la dispersión de contaminantes.

**Figura 8. Comparación de velocidad del viento modelada contra medida.**

Informe de Calidad del Aire Pág. 12

_Nuevo Nuevo Proyecto Inmobiliario Hacienda Lo Errázuriz_

**Figura 9. Comparación de dirección del viento en verano modelada contra medida.**

**Figura 10. Comparación de dirección del viento en invierno modelada contra medida.**

Informe de Calidad del Aire Pág. 13

_Nuevo Nuevo Proyecto Inmobiliario Hacienda Lo Errázuriz_

**4.4** **TOPOGRAFÍA**

La información topográfica del área de emplazamiento del Proyecto utilizada en el modelo WRF,
corresponde a proyecciones topográficas digitales de las misiones de los transbordadores espaciales
SRTM3 (Shuttle Radar Topography Mission), con mediciones cada 30 metros.

**Figura 4 Proyección topográfica de la zona de modelación.**

_Fuente: Elaboración propia._

La información relacionada con el uso de suelo de la zona fue obtenida a través de los archivos Global
Land Cover Characterization (GLCC) publicados por el U.S. Geological Survey (USGS) y disponibles
en Internet para utilización abierta en proyectos de variada índole.

El escenario de modelación considera la emisión simultánea de todas las fuentes (de modo de
considerar el peor escenario), a pesar de que en la realidad la emisión proviene por etapas.

Informe de Calidad del Aire Pág. 14

_Nuevo Nuevo Proyecto Inmobiliario Hacienda Lo Errázuriz_

**4.5** **RECEPTORES**

La modelación ha considerado una grilla rectangular de receptores de 8 km (Este-Oeste) por 8 km
(Norte-Sur) que abarca un área total de 64 km [2] .

La grilla considerada, tiene receptores cada 250 metros, de modo de hacer un análisis fino de la calidad
del aire en el área de desarrollo del Proyecto. Cada punto de la figura siguiente corresponde a un
receptor de la grilla, totalizando 1024 receptores en la grilla.

**Figura 5.** **Proyección grilla de receptores.**

_Fuente: Elaboración propia._

Informe de Calidad del Aire Pág. 15

_Nuevo Nuevo Proyecto Inmobiliario Hacienda Lo Errázuriz_

**4.6** **LINEA BASE CALIDAD DEL AIRE**

Los niveles basales de calidad del aire se obtienen de la estación de monitoreo con representatividad
poblacional (EMRP) Cerrillos II, la que presenta los siguientes valores para el año 2023.

**Tabla 2: Valores basales de calidad en EM Cerillos II**

<!-- INICIO TABLA 2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **4.6** **LINEA BASE CALIDAD DEL AIRE** Los niveles basales de calidad del aire se obtienen de la estación de monitoreo con representatividad poblacional (EMRP) Cerrillos II, la que presenta los siguientes valores para el año 2023. -->

**Tabla 2: Valores basales de calidad en EM Cerillos II****

| Contaminante | Estación Monitoreo] | Línea Base<br>[g/m3N] | Norma<br>[g/m3N] | Período | Coord. E<br>[m] | Coord. N<br>[m] |
| --- | --- | --- | --- | --- | --- | --- |
| **MP10** | Cerrillos II | 69.03 | 130.0 | Diario | 341,687 | 6,292,449 |
| **MP10** | Cerrillos II | 69.01 | 50.0 | Anual | 341,687 | 6,292,449 |
| **MP2.5** | Cerrillos II | 25.07 | 50.0 | Diario | 341,687 | 6,292,449 |
| **MP2.5** | Cerrillos II | 25.05 | 20.0 | Anual | 341,687 | 6,292,449 |

<!-- Estadísticas: 4 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- _**Fuente**_ _: Servicio Nacional de Calidad del Aire, 2023._ De las mediciones se aprecia que la norma anual para MP10 y MP2.5 sobrepasan la norma primaria de calidad del aire. Mientras que la norma diaria para ambos contaminantes se encuentra cerca del -->
<!-- FIN TABLA 2 -->


|Contaminante|Estación Monitoreo]|Línea Base<br>[g/m3N]|Norma<br>[g/m3N]|Período|Coord. E<br>[m]|Coord. N<br>[m]|
|---|---|---|---|---|---|---|
|**MP10**|Cerrillos II|69.03|130.0|Diario|341,687|6,292,449|
|**MP10**|Cerrillos II|69.01|50.0|Anual|341,687|6,292,449|
|**MP2.5**|Cerrillos II|25.07|50.0|Diario|341,687|6,292,449|
|**MP2.5**|Cerrillos II|25.05|20.0|Anual|341,687|6,292,449|

_**Fuente**_ _: Servicio Nacional de Calidad del Aire, 2023._

De las mediciones se aprecia que la norma anual para MP10 y MP2.5 sobrepasan la norma primaria
de calidad del aire. Mientras que la norma diaria para ambos contaminantes se encuentra cerca del
50% sus respectivos límites.

**4.7** **RESULTADOS DE LA MODELACIÓN**

Dada la naturaleza del proyecto, consistentes principalmente en emisión de material particulado en una
zona saturada por movimientos de tierra, la modelación se realiza para Material Particulado grueso
(MP10) y fino (MP2.5).

La siguiente tabla muestra los resultados obtenidos al hacer correr el modelo para determinar la
dispersión de material particulado en la zona de máximo impacto, como cercana al proyecto.

**Tabla 3: Resultados de modelación en punto de máximo impacto (PMI)**

<!-- INICIO TABLA 3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- (MP10) y fino (MP2.5). La siguiente tabla muestra los resultados obtenidos al hacer correr el modelo para determinar la dispersión de material particulado en la zona de máximo impacto, como cercana al proyecto. -->

**Tabla 3: Resultados de modelación en punto de máximo impacto (PMI)****

| Aporte Norma % c/r a Coord. E Coord. N<br>Contaminante Período<br>[[g/m3N] [[g/m3N] Norma [m] [m] | Col2 | Col3 | Col4 | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| MP10 | 24 hr | 3.86 | 130.00 | 2.97% | 342,396 | 6,291,824 |
| MP10 | Anual | 0.99 | 50.00 | 1.98% | 342,396 | 6,291,824 |
| MP2.5 | 24 hr | 0.77 | 50.00 | 1.54% | 342,396 | 6,291,824 |
| MP2.5 | Anual | 0.20 | 20.00 | 0.81% | 342,396 | 6,291,824 |

<!-- Estadísticas: 4 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- _**Fuente**_ _: Elaboración propia_ A pesar de ser un proyecto intensivo en emisiones en la etapa de construcción, estas se generan en una amplia zona del proyecto, lo que favorece su dispersión y su distribución a lo largo de toda la -->
<!-- FIN TABLA 3 -->


|Aporte Norma % c/r a Coord. E Coord. N<br>Contaminante Período<br>[[g/m3N] [[g/m3N] Norma [m] [m]|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|MP10|24 hr|3.86|130.00|2.97%|342,396|6,291,824|
|MP10|Anual|0.99|50.00|1.98%|342,396|6,291,824|
|MP2.5|24 hr|0.77|50.00|1.54%|342,396|6,291,824|
|MP2.5|Anual|0.20|20.00|0.81%|342,396|6,291,824|

_**Fuente**_ _: Elaboración propia_

A pesar de ser un proyecto intensivo en emisiones en la etapa de construcción, estas se generan en
una amplia zona del proyecto, lo que favorece su dispersión y su distribución a lo largo de toda la
superficie del proyecto.

Los valores representan aproximadamente menos de un 7% de la norma de calidad del aire primaria
para MP 10 y MP2.5, por lo que se entiende que el proyecto no impactaría significativamente el AI del
proyecto.

Sin embargo y dado los criterios de evaluación de SEA, se realizará un análisis específico a los
receptores humanos cercanos al proyecto e identificados en el estudio de ruido de la presente DIA.

Informe de Calidad del Aire Pág. 16

_Nuevo Nuevo Proyecto Inmobiliario Hacienda Lo Errázuriz_

**Tabla 4. Resultados modelación dispersión en receptores discretos.**

|Receptor|Coordenada<br>Este|Coordenada<br>Norte|MP10<br>24 h|MP10<br>Anual|MP2.5<br>24 h|MP2.5<br>Anual|
|---|---|---|---|---|---|---|
||M|m|**[μg/m3N]**|**[μg/m3N]**|**[μg/m3N]**|**[μg/m3N]**|
|R1|342,256|6,291,969|2.58|0.61|0.52|0.12|
|R2|342,396|6,291,823|3.85|0.99|0.77|0.20|
|R3|342,585|6,291,621|1.03|0.20|0.22|0.04|
|R4|342,513|6,291,916|3.14|0.71|0.59|0.14|
|R5|341,835|6,291,424|0.78|0.08|0.16|0.02|
|R6|342,118|6,291,345|0.92|0.10|0.20|0.02|
|R7|342,472|6,291,795|2.36|0.54|0.47|0.11|

_**Fuente**_ _: Elaboración propia_

Según el documento “Criterio de evaluación en el SEIA: impacto de emisiones en zonas saturadas por
material particulado respirable MP10 y material particulado fino respirable MP2,5”, de 2023, del SEIA,
(en adelante, “Criterio de Evaluación Impacto de Emisiones en Zonas Saturadas”) se establecen 2
criterios para evaluar la significancia de las emisiones. En el caso de este proyecto se utiliza el criterio
de un proyecto con impacto de menos de 3 años con una etapa de construcción intensiva en emisiones
que luego decaen en la operación, por lo que se utilizará el criterio de la Tabla 2 del citado criterio, para
el período de construcción de 28 meses.

**Tabla 5. Valores de significancia sobre receptores por menos de 3 años (28 meses de construcción)**

|Contaminante|Periodo|Incremento concentración<br>[ug/m3N]|
|---|---|---|
|MP 10|24 Horas|6.43|
|MP 10|Anual|1.29|
|MP 2.5|24 Horas|2.20|
|MP 2.5|Anual|0.42|

_**Fuente**_ _: Criterio de evaluación en el SEIA: impacto de emisiones en zonas saturadas por material particulado respirable_

_MP10 y material particulado fino respirable MP2,5”. Servicio de Evaluación Ambiental, en Septiembre 2023._

Por lo tanto, se aprecia que para el período diario y anual de MP10 y MP2.5 no existen receptores, en
que las emisiones se declaran como significativas. A continuación, se presentan los gráficos de isoconcentración:

Informe de Calidad del Aire Pág. 17

_Nuevo Nuevo Proyecto Inmobiliario Hacienda Lo Errázuriz_

**Figura 6. Resultado modelación de dispersión de MP10 (anual)**

Informe de Calidad del Aire Pág. 18

_Nuevo Nuevo Proyecto Inmobiliario Hacienda Lo Errázuriz_

**Figura 7. Resultado modelación de dispersión de MP10 (diario)**

Informe de Calidad del Aire Pág. 19

_Nuevo Nuevo Proyecto Inmobiliario Hacienda Lo Errázuriz_

**Figura 8. Resultado modelación de dispersión de MP2.5 (anual)**

Informe de Calidad del Aire Pág. 20

_Nuevo Nuevo Proyecto Inmobiliario Hacienda Lo Errázuriz_

**Figura 9. Resultado modelación de dispersión de MP2.5 (diario)**

Informe de Calidad del Aire Pág. 21

_Nuevo Nuevo Proyecto Inmobiliario Hacienda Lo Errázuriz_

**5** **CONCLUSIONES**

Desde el punto de vista de dispersión de contaminantes se aprecia que la emisión se dispersa
rápidamente, debido a la baja energía ascendente del flujo de emisión, típico de las actividades de
movimientos de tierra y tráfico vehicular, que al no tener suficiente momentum se dispersa y decae
rápidamente.

A nivel meteorológico, se aprecia que los valores del modelo WRF son consistentes con las mediciones
de la estación EL Bosque, lo que permite tener una representación adecuada de la modelación de
dispersión.

Los resultados de la modelación de dispersión de emisiones atmosféricas permiten confirmar el área
de influencia del Proyecto, a una zona circular de 1 km de radio, toda vez que, más allá de 1 km desde
la fuente, el aporte del proyecto cae por debajo del 90% del total del aporte, dejando solo el nivel base.

Debido a la dispersión de los contaminantes principales, el aporte a la calidad del aire es inferior al 3%
de las correspondientes normas de calidad. Sin embargo, al estar en una zona saturada por MP10 y
MP2.5, estas normas (en período anual) están superadas de forma previa a la construcción del
proyecto.

De acuerdo con el Criterio de Evaluación Impacto de Emisiones en Zonas Saturadas, al observar el
impacto en los receptores más cercanos al proyecto, este impacto está por debajo de los umbrales de
la tabla 1 de dichos criterios para los receptores cercanos al proyecto.

Por lo tanto, se puede concluir que, a nivel de calidad del aire, el proyecto no genera un impacto
significativo.

Informe de Calidad del Aire Pág. 22

_Nuevo Nuevo Proyecto Inmobiliario Hacienda Lo Errázuriz_

**6** **REFERENCIAS BIBLIOGRÁFICAS**

1. Noel de Nevers, Air Pollution Control Engineering, 1995
2. Guía para uso de modelos de calidad del aire en el SEIA, Servicio de Evaluación Ambiental,
2023.
3. Guía para la descripción de la calidad del aire en el área de influencia de proyectos que ingresan
al SEIA. Servicio Evaluación Ambiental, 2015.
4. Decreto Supremo N°31, de 2017, que Establece Plan de descontaminación atmosférica para la
Región Metropolitana.
5. Decreto Supremo N°131, de 1996, que declara zona saturada por material particulado respirable
MP10 como concentración anual y 24 horas a la Región Metropolitana.
6. Decreto Supremo N°67, de 2014, que declara zona saturada por material particulado fino
respirable MP2,5, como concentración anual y de 24 horas a la Región Metropolitana.
7. Criterio de evaluación en el SEIA: Impacto de emisiones en zonas saturadas por material
particulado respirable MP10 y material particulado fino respirable MP2,5. Servicio de Evaluación
Ambiental, Septiembre 2023.

Informe de Calidad del Aire Pág. 23

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Resumen de emisiones de Material Particulado [ton/año]****

| Año | Etapa | MP10 | MP2.5 |
| --- | --- | --- | --- |
| 1 | Construcción | 3.82 | 1.91 |
| 2 | Construcción | 0.92 | 0.73 |
| 3 | Operación | 1.66 | 0.48 |
| 4 + | Operación | 2.38 | 0.61 |

**Tabla 4.: Resultados modelación dispersión en receptores discretos.****

| Receptor | Coordenada<br>Este | Coordenada<br>Norte | MP10<br>24 h | MP10<br>Anual | MP2.5<br>24 h | MP2.5<br>Anual |
| --- | --- | --- | --- | --- | --- | --- |
|  | M | m | **[μg/m3N]** | **[μg/m3N]** | **[μg/m3N]** | **[μg/m3N]** |
| R1 | 342,256 | 6,291,969 | 2.58 | 0.61 | 0.52 | 0.12 |
| R2 | 342,396 | 6,291,823 | 3.85 | 0.99 | 0.77 | 0.20 |
| R3 | 342,585 | 6,291,621 | 1.03 | 0.20 | 0.22 | 0.04 |
| R4 | 342,513 | 6,291,916 | 3.14 | 0.71 | 0.59 | 0.14 |
| R5 | 341,835 | 6,291,424 | 0.78 | 0.08 | 0.16 | 0.02 |
| R6 | 342,118 | 6,291,345 | 0.92 | 0.10 | 0.20 | 0.02 |
| R7 | 342,472 | 6,291,795 | 2.36 | 0.54 | 0.47 | 0.11 |

**Tabla 5.: Valores de significancia sobre receptores por menos de 3 años (28 meses de construcción)****

| Contaminante | Periodo | Incremento concentración<br>[ug/m3N] |
| --- | --- | --- |
| MP 10 | 24 Horas | 6.43 |
| MP 10 | Anual | 1.29 |
| MP 2.5 | 24 Horas | 2.20 |
| MP 2.5 | Anual | 0.42 |
