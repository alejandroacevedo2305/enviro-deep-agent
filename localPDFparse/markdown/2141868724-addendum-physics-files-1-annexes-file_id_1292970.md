---
title: 1761-21463-3-01_Estudio de impacto de Olor - RR Wines
author: Roberto Fuenzalida
date: D:20190327152124-03'00'
language: es
type: report
pages: 52
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ESTUDIO DE IMPACTO DE OLOR RR WINES SAGRADA FAMILIA
  - REVISIONES
  - NOTA
  - TABLA DE CONTENIDO
  - LISTA DE TABLAS
  - LISTA DE FIGURAS
  - LISTA DE ANEXOS
  - GLOSARIO, SIGLAS Y UNIDADES
  - 1 CONTEXTO
  - 2 MODELO DE DISPERSIÓN
  ... y 9 secciones más
-->

# ESTUDIO DE IMPACTO DE OLOR RR WINES SAGRADA FAMILIA

**PRESENTADO POR Odotech Chile SpA**
**Una empresa de** _**Envirosuite Ltd**_
**CONTACTO: + 569 75892529.**

**CONFIDENCIAL**

**Estudio de impacto de olor - RR Wines Sagrada Familia**

**Sustenable**

**Reporte No.: 1761-21463-3-01**

**Marzo de 2019**

Preparado por: Fecha : Marzo 2019

Ing. Roberto Fuenzalida
Encargado de Proyectos

# REVISIONES

|Revisión No.|Fecha|Descripción de Modificaciones|
|---|---|---|
|01|27/03/2019|Versión preliminar|
||||
||||
||||

# NOTA

_El siguiente documento es obra de Odotech Ltda. y está protegido por las leyes de_
_propiedad intelectual. La información, análisis y recomendaciones deben ser utilizados_
_exclusivamente para la intención presentada en el informe. Toda adaptación o_
_reproducción (ya sea parcial o completa) está estrictamente prohibida sin previo_
_consentimiento por escrito de Odotech y del cliente. La información, conclusiones,_
_estimaciones, resultados y recomendaciones se basan en: i) la información disponible a_
_la cual se pudo acceder durante la producción del documento, ii) los datos obtenidos de_
_fuentes externas y iii) las condiciones, estimaciones, escenarios e hipótesis que se_
_indican en el informe._

_Odotech Ltda. siempre considera las mejores fuentes externas de información_
_disponibles, ya sean servicios, metodologías o consultores, para el suministro y la_
_preparación de los datos meteorológicos requeridos; sin embargo, Odotech Ltda. no se_
_puede hacer responsable de la exactitud ni la integridad de los datos meteorológicos_
_utilizados en sus estudios de dispersión._

_El uso de datos meteorológicos provenientes del sitio será siempre preferible. Odotech_
_Ltda. puede ayudar al cliente al establecimiento de un sistema de dispersión de olores en_
_tiempo real, que incluye una estación meteorológica. Los impactos modelados y los datos_
_meteorológicos reflejarían realidades micrometeorológicas locales._

_Las conclusiones incluidas en el presente documento están basadas en los objetivos_
_acordados entre el cliente y Odotech Ltda. Podrían existir otros impactos que no están_
_incluidos o discutidos en este estudio como: cambios en las emisiones de otros_
_contaminantes, impacto en los procesos, impacto en los costos, impacto en los_
_requerimientos de recursos humanos, impactos sociales, etc. Es importante también_
_considerar que otras reglas pueden aplicarse como: límites, guías, normas, estándares,_
_obligaciones o acuerdos previos además de los que hace referencia el presente_
_documento, los que pueden alterar significativamente los análisis y conclusiones del_
_presente estudio._

# TABLA DE CONTENIDO

1 Contexto .................................................................................................................... 1

2 Modelo de dispersión ................................................................................................ 1

2.1 Modelo de dispersión atmosférico ..................................................................... 2

2.2 Dominio de modelación y grillas ........................................................................ 2

2.3 Topografía......................................................................................................... 2

2.4 Configuración de la malla de receptor ............................................................... 4

2.5 Receptores discretos ........................................................................................ 4

2.6 Información Meteorológica ................................................................................ 7

2.7 Análisis de incertidumbre ................................................................................ 10

2.7.1 Análisis cualitativo ___________________________________________ 10
2.7.2 Análisis cuantitativo __________________________________________ 11
2.7.3 Comentarios y resultados del análisis de incertidumbre ______________ 13
2.8 Método de evaluación del impacto de olor ...................................................... 14

2.9 Descripción de las fuentes y escenarios de modelación.................................. 15

3 Resultados de la modelación de dispersión atmosférica ......................................... 20

3.1 Resultados Escenario ACTUAL ...................................................................... 20

3.2 Resultados Escenario PROYECTADO ............................................................ 22

4 Conclusion .............................................................................................................. 24

5 Referencias ............................................................................................................. 26

# LISTA DE TABLAS

**Tabla 1: Características de los receptores discretos ................................................. 4**

**Tabla 2: Fuentes información meteorológica .............................................................. 7**

**Tabla 4: Velocidad de Viento Promedio. .................................................................... 10**

**Tabla 5: Sesgo, Error Cuadrático Medio y Coeficiente de Correlación - Información**
**Estación Sagrada Familia vs Información Modelo WRF ............................ 12**

**Tabla 2: Criterios de Calidad de Olor a Nivel Internacional ..................................... 14**

**Tabla 3: Fuentes en la Planta de RILES RR Wines ................................................... 15**

**Tabla 4 : Características de las fuentes a modelar - Fuentes Superficiales ........... 16**

**Tabla 7: Resultados de concentración de olor y frecuencia de exceso en los**
**receptores discretos Escenario Actual ....................................................... 21**

**Tabla 7: Resultados de concentración de olor y frecuencia de exceso en los**
**receptores discretos Escenario Proyectado ............................................... 23**

# LISTA DE FIGURAS

**Figura 1: Dominio de Modelación y Topografía .......................................................... 3**

**Figura 2: Límite de propiedad y receptores discretos ................................................ 6**

**Figura 3: Ubicación de fuentes de información meteorológica. ................................ 9**

**Figura 4: Fuentes - Escenario de Modelación Actual ............................................... 18**

**Figura 5: Fuentes - Escenario de Modelación Proyectada ....................................... 19**

# LISTA DE ANEXOS

**ANEXO A: SERIES DE TIEMPO DE VELOCIDAD Y DIRECCIÓN DEL VIENTO ........ 27**

**ANEXO B: ANÁLISIS DE INCERTIDUMBRE ............................................................... 32**

**ANEXO C: RESULTADOS GRÁFICOS DE MODELACIÓN ......................................... 40**

# GLOSARIO, SIGLAS Y UNIDADES

|Términos|Definiciones|
|---|---|
|Análisis Olfatométrico|Técnica de cuantificación de olor o medida de concentración de olor.|
|Concentración de olor|Número de unidades de olor en 1 m3 de gas, o número de diluciones (con<br>aire) necesarias para obtener por parte del panel de los jurados, la<br>situación en que el 50% de ellos percibe (u.o./m3).|
|CP98|Las concentraciones calculadas en este punto son inferiores al valor<br>determinado por la modelación y 2% de los valores de concentración<br>calculados son superiores (175 horas/ acumuladas en un año).|
|EN|_European Standard_ / Norma Europea.|
|Fuente1 puntual|Fuente estacionaria discreta, de emisión de gases a la atmósfera a través<br>de conductos, de dimensión y caudal de aire definidos. (Por ejemplo:<br>chimeneas, venteos, otros).|
|Fuentes difusas|Fuentes con dimensiones definidas (prioritariamente fuentes superficiales)<br>que no tienen flujo de gas residual definido.|
|Fuentes difusas activas|Fuentes difusas con aireación forzada. (Por ejemplo: biofiltros, piscina de<br>aireación extendida, otros).|
|Fuentes difusas<br>pasivas|Fuentes difusas sin aireación forzada. (Por ejemplo: pilas de lodos,<br>estanques de sedimentación, otros).|
|Fuentes fugitivas|Fuentes esquivas o de difícil identificación que liberan cantidades<br>indefinidas de sustancias olorosas (por ejemplo: fugas de válvulas y<br>juntas, aperturas de ventilación pasiva, otros).|
|Molestia|Efecto acumulativo de episodios de olor, los cuales superan el nivel de<br>tolerancia de las personas expuestas. Son cuatro los elementos que<br>deben ser considerados durante el análisis para determinar la molestia a<br>causa de un olor: concentración de olor, frecuencia, duración y tono<br>hedónico.|
|m.s.n.m|Metros sobre el nivel del mar|
|Nm3|Volumen en un m3 a temperatura y presión normalizada (P=101,3 kPa and<br>T=293K).|
|PTRILES|Planta de Tratamiento de Residuos Líquidos Industriales|
|SEA|Servicio de Evaluación Ambiental|
|SEIA|Sistema de Evaluación Impacto Ambiental|

1 Definiciones de Fuentes puntuales, difusas, difusas activas, difusas pasivas y fuentes fugitivas han sido de
acuerdo a lo descrito en la NCh 3190.Of 2010.

|Términos|Definiciones|
|---|---|
|u.o./m3|Unidades de olor por metro cúbico de aire. Unidad de Medida. 1 u.o./m3 <br>corresponde al nivel en que el 50% de la población es capaz de comenzar<br>a detectar un olor, en un ambiente libre de olor.|
|u.o./m2/s|Unidad de olor por metro cuadrado por tasa de emisión de olor por unidad<br>de superficie (aplica para fuentes superficiales).|
|UTM|Universal Transverse Mercator|

# 1 CONTEXTO

Sustentable mandata Odotech para caracterizar los olores de las fuentes odoríficas de
las Instalaciones Agroindustriales de RR Wines ubicada en la comuna de Sagrada
Familia, Provincia de Curicó, Región del Maule, Chile. Cabe señalar que el estudio esta
enfocado en la operación de la PTRILES, siendo los procesos de esta los generadores
de emisión de olor del Proyecto.

Este informe presenta los parámetros de modelación de la dispersión de los olores de las
Instalaciones Agroindustriales de RR Wines para dos escenarios de modelación En el
escenario actual de operación de la planta se consideran los siguientes componentes o

procesos.

 - Sistema de Conducción

 - Pretratemiento (Estanque de Impulsión, Filtro Rotatorio y Filtro Lamelar)

 - Decantadores Lamelares (2 unidades)

 - Embalse ecualizador (neutralización)

 - Reactores Aeróbicos (30 unidades)

 - Digestor de Lodos

 - Cunas de Secado (4 unidades)

 - Reactores Aeróbicos (2 unidades)

 - Tranque Acumulador de Riles Tratados

Por su parte en el escenario proyectado se considera añadir las siguientes unidades:

 - Filtros Lamerales (2 unidades)

 - Cunas de Secado de Lodos (3 unidades)

 - Tranque de Riego

 - Se profundiza uno de los estanque aeróbicos existentes.

El estudio fue realizado con el modelo CALPUFF y con datos meteorológicos WRF [2] . Este
informe presenta la caracterización de olor de las fuentes consideradas en el Proyecto,
los parámetros de modelación de la dispersión y los resultados de la misma.

# 2 MODELO DE DISPERSIÓN

La dispersión de olores emitidos por la Planta de RILES de RR Wines fue modelada a fin
de evaluar los impactos sobre el área de influencia. Las siguientes subsecciones
describen el modelo de dispersión utilizado, el lugar bajo estudio, la topografía del área,
la configuración de la malla de receptores, así como los receptores discretos a evaluar en
los alrededores de la Planta y el período de la meteorología a utilizar en el modelo de

2 El modelo numérico recomendado para la generación de datos meteorológicos es el _Weather Research_
_Forecasting Model_ (WRF). WRF es uno de los modelos meteorológicos de pronóstico más avanzados y
completos, y mantenido por NCAR/NOAA ( _National Center for Atmospheric Research/National Oceanic and_
_Atmospheric Administration_ ) de Estados Unidos (SEA, 2012). Este modelo de pronóstico numérico es
utilizado a nivel global y se encuentra en continuo desarrollo.

dispersión atmosférico.

## 2.1 Modelo de dispersión atmosférico

Para el presente estudio, la dispersión de olores fue modelada con CALPUFF-View
(versión actualizada de _Lakes Environmental_ 8.5.0 y versión aprobada de la US-EPA
5.8.5). Este software de modelación de dispersión atmosférica, fue desarrollado por la
Agencia Estadounidense de Protección Ambiental (US-EPA) para predecir los impactos
atmosféricos. Adicionalmente, es el modelo recomendado por la Guía para el uso de
modelos de calidad del aire en el SEIA (SEA, 2012).

El Calpuff es un software con una combinación del modelo Gaussiano y el modelo
Lagrangeano, en el sentido de que esencialmente calculan la dispersión de
contaminantes provenientes de una emisión instantánea, llamada “puff”, a lo largo de una
trayectoria.

## 2.2 Dominio de modelación y grillas

El estudio de impacto de los olores se realiza en una grilla meteorológica de 50 km por
50 km (la resolución de la grilla es de 1 km x 1 km). Véase punto rojo en la Figura 1. Las
coordenadas geográficas centrales del área son X 287 715 km, Y 6118 524 km (UTM,
WGS84, Huso 19). La localización de la planta es identificada con un punto rojo en la
Figura 1.

## 2.3 Topografía

Las elevaciones del terreno del área a modelar pueden presentar un alto impacto en la
dispersión de olores, cuando existen desnivelaciones de más de 10 m se estima el terreno
como accidentado y las desnivelaciones serán tomadas en consideración para la
modelación. En el presente estudio, la elevación del terreno varía entre 97 metros y 1 415
metros sobre el nivel del mar, en particular el área en donde se emplaza el Proyecto se
encuentra entre los 200 y 300 metros sobre el nivel del mar (véase Figura 1), en
consecuencia se tuvieron en cuenta las elevaciones del terreno para la modelación.
La información de topografía utilizada, será obtenida a través de la interfaz de _Lakes_
_Environmental_ y se basa en los datos de la misión de topografía _Shuttle Radar_
_Topography Mission_ (SRTM1). Estos datos son utilizados por TERREL para calcular la
altura del terreno de cada una de las fuentes de emisión y de los receptores para su uso
en el modelo.

|Col1|PROYECTO<br>PLANTA RILES RR WINES<br>REGIÓN DEL MAULE|Col3|
|---|---|---|
||**Leyenda**<br>Ubicación del Proyecto|**Leyenda**<br>Ubicación del Proyecto|
||**Situación**<br>**Regional**<br>**Comuna de**<br>**Sagrada**<br>**Familia**<br> <br> <br> <br>|**Situación**<br>**Nacional**<br>|
||**Referencia Geodésica**<br>Proyección: UTM<br>Datum: WGS 84<br>Zona: 19H<br>Coordenadas centrales del<br>proyecto:<br>X 287.715 km<br>Y 6118.524 km|**Referencia Geodésica**<br>Proyección: UTM<br>Datum: WGS 84<br>Zona: 19H<br>Coordenadas centrales del<br>proyecto:<br>X 287.715 km<br>Y 6118.524 km|

_**Figura 1: Dominio de Modelación y Topografía**_

[Reporte no. 1761-21463-3-01 ] **3**
Estudio de impacto de olor - RR Wines Sagrada Familia

## 2.4 Configuración de la malla de receptor

Un receptor es un punto en el cual el modelo calcula las concentraciones de olor. Una
malla de receptores es un grupo de receptores configurados a diferentes distancias de la
fuente de olores. La malla de receptores se ha configurado dentro de un radio de 5 km
alrededor de la Planta, de esta forma es posible abarcar el entorno directo de la misma y
otros sector en la comuna de Sagrada Familia y alrededores, presentando distancias
variables entre cada receptor (cuando su posición es más alejada de la fuente, la distancia
entre receptores aumenta). Para el presente estudio la distancia entre los receptores de
la malla variará entre 20 y 500 m, mientras que la distancia entre los receptores discretos
y la Planta variaran entre 80 y 1 100 m. Todos los receptores se fijaron a una altura de
1,5 m, que corresponde a la altura media de la nariz humana.

## 2.5 Receptores discretos

Para reflejar más eficientemente los posibles impactos provocados por los olores, se
agregaron receptores discretos a la malla de receptores. Estos receptores se encuentran
ubicados en las primeras residencias del sector poblado más próximo al sitio.

Al igual que los receptores de la malla, los receptores discretos se fijaron a una altura de
1,5 m del suelo. En total, veintiún (21) receptores discretos situados entre 80 a 1 100 m
de los límites del terreno del sitio han sido agregados para el presente estudio.

La Tabla 1 presenta los receptores discretos definidos para el actual estudio. En la Figura
2 están representados con una cruz azul.

_**Tabla 1: Características de los receptores discretos**_

|Receptor|Localización<br>UTM<br>WGS84, 18H|Col3|Altura<br>m.s.n.m.|Distancia<br>al límite de la<br>propiedad*|Descripción|
|---|---|---|---|---|---|
|**Receptor**|**X [m]**|**Y [m]**|**H [m]**|**L [m]**|**L [m]**|
|1|287912|6118733|201|480|Primer Vecino Noreste (NE)|
|2|287958|6118555|201|350|Primer Vecino Este (E)|
|3|287804|6118249|213|80|Primer Vecino Sur Interno (S)|
|4|287632|6118017|223|280|Segundo Vecino Sur Interno<br>(SO)|
|5|287365|6119315|197|1100|Primer Vecino Norte (N)|
|6|287640|6118007|218|280|Tercer Vecino Sur Interno (S)|
|7|287828|6118132|216|170|Vecino Este Interno 1 (E)|
|8|287824|6118188|213|130|Vecino Este Interno 2 (E)|

|Receptor|Localización<br>UTM<br>WGS84, 18H|Col3|Altura<br>m.s.n.m.|Distancia<br>al límite de la<br>propiedad*|Descripción|
|---|---|---|---|---|---|
|**Receptor**|**X [m]**|**Y [m]**|**H [m]**|**L [m]**|**L [m]**|
|9|287804|6118251|201|80|Segundo Vecino Sur Interno<br>(S)|
|10|288034|6118546|202|410|Vecino Noreste 1 (NE)|
|11|288053|6118488|204|390|Vecino Noreste 2 (NE)|
|12|288118|6118431|208|420|Vecino Noreste 3 (NE)|
|13|288376|6118304|201|650|Vecino Noreste 4 (NE)|
|14|288096|6118561|200|470|Vecino Noreste 5 (NE)|
|15|287943|6118683|200|460|Vecino Noreste 6 (NE)|
|16|287919|6118716|201|480|Vecino Noreste 7 (NE)|
|17|287904|6118742|200|480|Vecino Noreste 8 (NE)|
|18|288215|6118572|201|580|Vecino Noreste 9 (NE)|
|19|288123|6118657|201|560|Vecino Noreste 10 (NE)|
|20|288206|6188713|200|660|Vecino Noreste 11 (NE)|
|21|288284|6118769|201|750|Vecino Noreste 12 (NE)|

|Col1|PROYECTO<br>PLANTA RILES RR WINES<br>REGIÓN DEL MAULE|Col3|
|---|---|---|
||**Leyenda**<br>Ubicación del Proyecto|**Leyenda**<br>Ubicación del Proyecto|
||**Situación**<br>**Regional**<br>**Comuna de**<br>**Sagrada**<br>**Familia**<br> <br> <br> <br>|**Situación**<br>**Nacional**<br>|
||**Referencia Geodésica**<br>Proyección: UTM<br>Datum: WGS 84<br>Zona: 19H<br>Coordenadas centrales del<br>proyecto:<br>X 287.715 km<br>Y 6118.524 km|**Referencia Geodésica**<br>Proyección: UTM<br>Datum: WGS 84<br>Zona: 19H<br>Coordenadas centrales del<br>proyecto:<br>X 287.715 km<br>Y 6118.524 km|

_**Figura 2: Límite de propiedad y receptores discretos**_

( _zoom in_ del dominio de modelación)

[Reporte no. 1761-21463-3-01 ] **6**
Estudio de impacto de olor - RR Wines Sagrada Familia

## 2.6 Información Meteorológica

El estudio de impacto de olor se realizó en base a un (01) año de data meteorológica
(periodo del 01/01/2016 al 31/12/2016) representativa del área de estudio dentro de una
grilla de modelación de 50 x 50 km. Esta data fue obtenida a partir del modelo de
pronóstico meteorológico WRF [3] . Cabe señalar que la data meteorológica a partir del
modelo de pronóstico WRF fue configurada de acuerdo a requerimiento de la Guía para
el Uso de Modelos de Calidad del Aire en el SEIA (SEA, 2012). Así también, de acuerdo
a lo señalado en SEA (2012), “ _Se reconoce además que existen limitaciones e_
_incertidumbre inherentes a cada tipo de modelo, así como también incertidumbre_
_asociada a los datos utilizados como información de entrada a los modelos_ ”. En particular
se reconoce la incertidumbre generada por el uso de meteorología de pronóstico, la Guía
señala que “ _Considerando que sólo se pueden estimar los errores entre modelación y_
_observaciones en el caso de la meteorología (ni para las emisiones ni para los impactos_
_futuros existen observaciones), el análisis de incertidumbre debe centrarse en el análisis_
_de los errores de la meteorología tanto en superficie como en altura_ ”.

En este caso no se cuenta con información de meteorología en altura, por lo que el
análisis se centrará en una comparación cualitativa y cuantitativa de la información
meteorológica de superficie. Utilizando como información observada la registrada por la
estación Sagrada Familia, cuya información se encuentra disponible para el año 2016 en
la plataforma AGROMET (www.agromet.cl) dependiente del Ministerio de Agricultura.

Para realizar las comparaciones cualitativas y cuantitativas se utilizará información
meteorológica de una estación de superficie y del archivo WRF utilizado en la modelación
de dispersión de olores. El análisis estará principalmente centrado en los campos de
viento, dirección y velocidad, considerando que son las variables que tienen un mayor
efecto sobre la dispersión del olor desde las fuentes consideradas.

En la Tabla 2 se presenta el detalle de las fuentes de información para el Análisis de
Incertidumbre.

_**Tabla 2: Fuentes información meteorológica**_

|Información|Estación|Ubicación<br>UTM WGS 84<br>Huso 19|Periodo|Parámetros|
|---|---|---|---|---|
|Observada|Sagrada<br>Familia|E 283358 m<br>S 6124817 m|01-01-2016 al<br>31-12-2016|Dirección de Viento<br>Velocidad de Viento|
|Modelo Pronostico*|Archivo<br>WRF|E 283017 m<br>S 6124676 m|E 283017 m<br>S 6124676 m|E 283017 m<br>S 6124676 m|

_*Corresponde a la coordenada del punto central de la cuadricula de la grilla meteorológica en la_
_que se encuentra contenida la estación Sagrada Familia._

3 El modelo numérico recomendado para la generación de datos meteorológicos es el _Weather Research_
_Forecasting Model_ (WRF). WRF es uno de los modelos meteorológicos de pronóstico más avanzados y
completos, y mantenido por NCAR/NOAA ( _National Center for Atmospheric Research/National Oceanic and_
_Atmospheric Administration_ ) de Estados Unidos (SEA, 2012). Este modelo de pronóstico numérico es
utilizado a nivel global y se encuentra en continuo desarrollo. Una de las ventajas más significativas se
manifiesta en la parametrización física configurada para el territorio Chileno, que entre otras cosas permite
otorgar una resolución horizontal de la grilla meteorológica de 1km.

En la Figura 3 se presenta la ubicación de la estación considerada y del punto que se
utilizó para obtener la información del archivo WRF, ambos puntos se encuentran a una
distancia de 300 metros entre sí, cabe señalar que ambos puntos se encuentran en un
área industrial.

Ambos puntos se encuentran aproximadamente a menos de 7 kilómetros de la Planta.

En el ANEXO a desde las Figura A-1 a la Figura A-4, las cuales presentan las series de
tiempo para las velocidades y dirección de viento de los datos registrados en la estación
observacional Sagrada Familia y los obtenidos del modelo WRF.

Se aprecia que en el caso de la información obtenida de la estación Sagrada Familia
existe un 94% de información disponible para el año 2016, lo anterior producto de
problemas en los registros, de todas formas se utilizará esta información para realizar los
análisis posteriores.

|Col1|PROYECTO<br>PLANTA RILES RR WINE<br>REGIÓN DEL MAULE|Col3|
|---|---|---|
||**Leyenda**<br>Ubicación del Proyecto|**Leyenda**<br>Ubicación del Proyecto|
||**Situación**<br>**Regional**<br>**Comuna de**<br>**Sagrada**<br>**Familia**<br> <br> <br> <br>|**Situación**<br>**Nacional**<br>|
||**Referencia Geodésica**<br>Proyección: UTM<br>Datum: WGS 84<br>Zona: 19H<br>Coordenadas centrales del<br>proyecto:<br>X 287.715 km<br>Y 6118.524 km|**Referencia Geodésica**<br>Proyección: UTM<br>Datum: WGS 84<br>Zona: 19H<br>Coordenadas centrales del<br>proyecto:<br>X 287.715 km<br>Y 6118.524 km|

_**Figura 3: Ubicación de fuentes de información meteorológica.**_

[Reporte no. 1761-21463-3-01 ] **9**
Estudio de impacto de olor - RR Wines Sagrada Familia

## 2.7 Análisis de incertidumbre

El Análisis de Incertidumbre que se presenta a continuación, considera dos metodologías
de comparación para la información meteorología observada y la generada por el modelo
de pronóstico, a saber:

 - _Análisis Cualitativo_ : se describe el comportamiento de los campos de viento a
partir de, considerando principalmente sus velocidades promedios y sus
direcciones predominantes, de promedios y gráficos asociadas a cada una de las
fuentes de información.

 - _Análisis Cuantitativo_ : considera la evaluación del modelo de pronóstico a partir de
la comparación de estadísticos como el sesgo, el error cuadrático medio y el
coeficiente de relación para determinar la relación entre el modelo de pronóstico
y la información obtenida por la estación de superficie.

Finalmente a partir de ambos análisis descritos anteriormente se determina si es
necesario corregir los resultados del impacto de olor a partir de un factor de corrección a
modo de subsanar la incertidumbre que genera la aplicación del modelo CALPUFF para
la evaluación realizada.

2.7.1 Análisis cualitativo

Considerando la velocidad promedio para ambas fuentes de información, existe una
sobreestimación de la velocidad de viento promedio, considerando que el archivo WRF
presenta una velocidad promedio de 2,43 m/s y la estación Sagrada Familia presenta una
velocidad promedio de1,43 m/s, si bien esto se puede deber a una sobreestimación del
modelo de pronostico también puede ser explicado producto de la diferencia en la
ubicación de ambas fuentes de información (como se aprecia en la Figura 3), además del
hecho de considerar la sensibilidad del anemómetro que se encuentra midiendo en la
estación Sagrada Familia.

_**Tabla 3: Velocidad de Viento Promedio.**_

|Información|Estación|Velocidad de Viento Promedio (m/s)|
|---|---|---|
|Observada|Sagrada Familia|0,7|
|Modelo Pronostico|Archivo WRF|2,3|

Por su parte, en el ANEXO B, Figura B- 1, es posible apreciar la distribución de la
velocidad de viento para ambas fuentes de información, a partir de la cual es posible
determinar que ambas fuentes de información tienen una concentración de intensidades
entre los 0,5 y 2,1 m/s, para Sagrada Familia representan el 95,1 % mientras que para el
modelo WRF representa un 48,1 %. Por su parte, con respecto a los niveles de calma
(esto es decir <0,5 m/s) los niveles de la estación Sagrada Familia alcanza un 0,0%,
mientras que los datos del archivo WRF para el mismo periodo alcanza un 8,2% de
porcentaje de calmas.

Además en el mismo ANEXO B, Figura B- 2, se pueden apreciar las rosas de viento para
el periodo en ambas fuentes de información meteorológica. Se puede apreciar que el
comportamiento de ambas rosas de viento presenta leves diferencias, siendo
principalmente relevante las componentes de viento provenientes desde el cuadrante
entre el Sur y el Oeste paraa el WRF y desde el Norte para el caso de la estación Sagrada

Reporte no. 1761-21463-3-01
**10**
Estudio de impacto de olor - RR Wines Sagrada Familia

Familia. La diferencia que se presenta en este caso está dada por la intensidad de los
vientos, en donde es superior en el caso de los datos obtenidos del archivo WRF.

En el ANEXO B, Figura B- 3, se presenta la frecuencia diaria de la dirección del viento
durante un día promedio, apreciando a partir de ambas imágenes, que existe un
comportamiento diferenciado que se condice con lo presentado en las rosas de viento

En la Figura B- 4, se presentan los ciclos estacionales de velocidad y dirección del viento
para los datos observados en la estación Sagrada Familia y los datos obtenidos del
Modelo WRF, con respecto a la velocidad se aprecia un comportamiento que se diferencia
principalmente en la intensidad de los vientos registrados por ambas fuentes de
información.

En las Figura B-5 y Figura B-6 del ANEXO B, se presentan las rosas de viento por periodo
del día, a partir de dichas figuras es posible señalar que:

 - _Periodo entre 00:00 y 05:00 horas:_ para los datos observados existe una
componente predominantes proveniente desde el Norte (S), similar dirección para
los datos generados por el WRF que corresponde al este (E); en este caso para
ambas fuentes de información la intensidad del viento es similar.

 - _Periodo entre 06:00 y 11:00 horas:_ para los datos observados existe una
componente principal proveniente desde el Norte (N), a su vez para los datos del
archivo WRF existe una componente principal desde el este (E); en este caso para
los datos del modelo WRF es levemente mayor la intensidad en los campos de
viento registrado.

 - _Periodo entre 12:00 y 17:00 horas:_ para los datos observados existe una
componente principal proveniente desde el norte (n), a su vez para los datos del
archivo WRF existe una componente principal desde el oeste-suroeste (OSO); en
este caso para los datos del modelo WRF es levemente mayor la intensidad en
los campos de viento registrado.

 - _Periodo entre 18:00 y 23:00 horas:_ para los datos observados existe una
componente principal proveniente desde el norte (n), a su vez para los datos del
archivo WRF existe una componente principal desde el Suroeste (SO); en este
caso para los datos del modelo WRF es levemente mayor la intensidad en los
campos de viento registrado.

A partir de lo presentado anteriormente es posible señalar que, si bien existe una
sobreestimación en cuanto a la velocidad de viento entre los datos modelados con
respecto a los observados, estos pueden ser explicados a partir del análisis de la
ubicación de ambos puntos considerados para la obtención de la información que se
encuentra siendo comparada. A su vez, se aprecia que las direcciones están
relativamente representadas, presentando diferencias, posiblemente producto de la
diferencia en la ubicación de la estación de monitoreo.

2.7.2 Análisis cuantitativo

Para la realización del análisis cuantitativo se han considerado las siguientes medidas de
error estadístico, a saber:
Sesgo: que representa la tendencia del modelo de pronostico WRF a sobreestimar o
subestimar las condiciones reales. Los resultados a obtener se comparan con respecto a
si son negativos o positivos, en el primer caso se interpreta como que el modelo
subestima el valor de las variables modeladas y viceversa. La fórmula para el cálculo del
sesgo es la siguiente:

Reporte no. 1761-21463-3-01
**11**
Estudio de impacto de olor - RR Wines Sagrada Familia

ே

ܵ݁ݏ݃݋ൌ [1]
ܰ [෍ሺܯ] [௜] [െܱ] [௜] [ሻ]

௜ୀଵ

Donde:

N: Tamaño de la muestra

M: Valor del Modelo de Pronostico
O: Valor Observado en la Estación de Superficie

Error Cuadrático Medio (ECM): este valor entrega la diferencia promedio entre los valores
promedios del modelo de pronostico y observados en la estación superficial. La fórmula
para el cálculo del error cuadrático medio es la siguiente:

ே

ሺܯ ௜ െܱ ௜ ሻ [ଶ]

ܰ

௜ୀଵ

ܧܥܯൌ ඩ෍

ே

ܰ

௜ୀଵ

Donde:

N: Tamaño de la muestra

M: Valor del Modelo de Pronostico
O: Valor Observado en la Estación de Superficie

Coeficiente de Correlación (r): a partir de este coeficiente se mide la relación lineal entre
la variable generada por el modelo de pronóstico y la variable observada en la estación
de superficie. El resultado de este coeficiente se encuentra en el intervalo [-1, 1]. El
resultado ideal es 1, considerando este como la mejor capacidad del modelo para
representar las condiciones generadas. La fórmula para el cálculo del coeficiente de
correlación es la siguiente:

ே

ሺܯ ௜ െܯ [ഥ] ሻሺܱ ௜ െܱ [ത] ሻ
ݎൌ [1] [෍]
ܰ ߪ ெ ߪ ௢

௜ୀଵ

Donde:

N: Tamaño de la muestra

M: Valor del Modelo de Pronostico
O: Valor Observado en la Estación de Superficie
σ: Desviación Estándar

En base a la fórmula para cada estadístico presentado anteriormente, en la siguiente tabla
se presentan los valores obtenidos para la comparación entre los datos del modelo de
pronóstico WRF y los datos observados en la estación Playa Blanca.

_**Tabla 4: Sesgo, Error Cuadrático Medio y Coeficiente de Correlación - Información**_
_**Estación Sagrada Familia vs Información Modelo WRF**_

|Información|Estación|Sesgo|Error Cuadrático<br>Medio|Coeficiente de<br>Correlación|
|---|---|---|---|---|
|Observada|Sagrada<br>Familia|1,40|2,24|0,24|
|Modelo<br>Pronostico|Archivo<br>WRF|Archivo<br>WRF|Archivo<br>WRF|Archivo<br>WRF|

Con respecto al análisis de los estadísticos de error analizados, es posible señalar en
primer lugar, que este complementa la información presentada en la Tabla 3, es decir se
manifiesta una clara sobreestimación del modelo sobre las velocidades de viento en el
área de modelación de acuerdo a los resultados del cálculo del sesgo. Asociado a lo

Reporte no. 1761-21463-3-01
**12**
Estudio de impacto de olor - RR Wines Sagrada Familia

anterior el Error Cuadrático Medio complementa dicha información y de acuerdo a lo que
es posible apreciar del cálculo de velocidad promedio de ambas fuentes de información
es posible señalar que el modelo aumenta en cerca de dos veces las velocidades
promedio de los datos observados.
Por último con respecto al coeficiente de correlación, para este se obtiene un valor de
0,24, valor positivo, por lo tanto las velocidades de viento tienen un comportamiento
similar, a pesar de las diferencias en las velocidades de viento promedio registradas, lo
anterior se puede apreciar en el ANEXO B, Figura B- 7.

2.7.3 Comentarios y resultados del análisis de incertidumbre

De acuerdo a lo presentado a partir del Análisis Cualitativo y Cuantitativo de la información
meteorológica utilizada para la elaboración del Estudio de Impacto de Olor, es posible
señalar:

 - Que el archivo meteorológico de pronostico WRF utilizado para el periodo 2016
considera una sobreestimación de los niveles de velocidad de viento al compararlo
con datos observados en la Estación Sagrada Familia para el periodo 2017.

 - Que el archivo meteorológico de pronóstico WRF aproxima levemente las
direcciones de viento durante el ciclo en el área de modelación al comparar el
periodo 2016 con los datos observados en la estación Sagrada Familia.
A partir de lo anterior, es posible indicar que los resultados del Estudio de Impacto de Olor
elaborado consideran cierta incertidumbre, según se señala en el documento “Guía
Técnica para la Gestión de las Emisiones Odoríferas Generadas por las Explotaciones
Ganaderas Intensivas” (2008), uno de los factores que explica en mayor medida la
variabilidad de la concentración de olor es la distancia a la fuente generadora de olor. Es
así que existe una relación logarítmica entre la concentración de olor y la distancia a la
fuente, de forma que la concentración de olor es elevada en el entorno directo en las
cercanías de la fuente y disminuye logarítmicamente a medida que uno se aleja de la
misma.

Para el caso del Estudio de Impacto de olor, se han determinado 9 receptores discretos,
los cuales se encuentran entre 80 metros y 1100 metros de los límites de la propiedad de
la Planta de RILES RR Wines, por lo tanto y considerando que los receptores más
cercanos serán los principales afectados por las emisiones de olor, es posible concluir
que la evaluación realizada corresponde al peor escenario posible para el Estudio de
Impacto de Olor y por lo mismo no se requiere un factor de corrección para el mismo,
toda vez que el análisis de incertidumbre se ha realizado con información meteorológica
ubicada en el entorno directo de la operación del Proyecto y que esta fue la información
más próxima a las fuentes que fue posible recopilar.

Reporte no. 1761-21463-3-01
**13**
Estudio de impacto de olor - RR Wines Sagrada Familia

## 2.8 Método de evaluación del impacto de olor

Los resultados de la modelación de dispersión de olores permiten cuantificar las molestias
causadas por los olores. La escala de percepción y concentración de olores generalmente
aceptada se resume de la siguiente forma:

1 u.o./m [3] : 50% de la población puede comenzar a percibir un olor

50% de la población puede reconocer o comenzar a
2-3 u.o./m [3 ] :
reconocer un olor

El olor es calificable y puede comenzar a recibirse quejas
5 u.o./m [3 ] :
(puede ser identificado)

10 u.o./m [3] : Los olores son reconocibles y se pueden recibir reclamos.

Es importante matizar el límite que se debe alcanzar para que exista una queja, ya que
éstas dependen también de la intensidad de los olores percibidos, de su agresividad, de
su apreciación y de su frecuencia. En consecuencia, la sensibilidad individual hacia los
olores tiene una influencia importante en la presentación de quejas.
En el marco del presente estudio, la concentración del percentil 98 será utilizado para
evaluar el nivel de olor de las zonas de ocupación humana de los bordes del terreno del
sitio estudio. Por definición, la concentración del percentil 98 en un punto receptor es el
valor de concentración tal que 98% de las concentraciones calculadas en este punto son
inferiores al valor determinado por la modelación y 2% de los valores de concentración
calculados son superiores (175 horas/ acumuladas en un año).

La evaluación con la concentración de percentil 98 es aceptada y aplicada en países que
cuentan con legislación sobre olores. Según el estudio de ECOTEC (2013), las normas
de referencia, para evaluar el impacto de olor generado por Plantas de Tratamiento de
Aguas Servidas, indica criterios de calidad que varían entre 5 y 10 u.o./m [3] . Estos valores
se especifican en la Tabla 5.

_**Tabla 5: Criterios de Calidad de Olor a Nivel Internacional**_

|ESTADO Ó<br>CIUDAD-PAÍS|LÍMITE|TIEMPO|FRECUENCIA<br>%|USO DE<br>SUELO|TIPO DE<br>FUENTE|REFERENCIA|
|---|---|---|---|---|---|---|
|UK|5 OU/m3|-|98%|-|PTAS|Mahin (2001)|
|Gales|5-10<br>OU/m3|-|-|Límite de la<br>propiedad|PTAS|Welsh<br>Assembly<br>(2005)|

Además, de acuerdo a los criterios presentados en el Estudio: Antecedentes para la
Regulación de Olores en Chile (ECOTEC, 2013), se proponen tres (3) niveles de inmisión
modelados en función de cuan ofensivo es el carácter del olor derivado de la actividad, sí
los niveles propuestos son los siguientes:

 - 3 u.o./m [3 ] como percentil 98 de promedios horarios, para olores de carácter más
ofensivo.

 - 5 u.o./m [3 ] como percentil 98 de promedios horarios, para olores de carácter
ofensivo moderado.

 - 7 u.o./m [3 ] como percentil 98 de promedios horarios, para olores de carácter menos
ofensivo.
De acuerdo a la clasificación presentada por ECOTEC (ECOTEC, 2013), en este caso el
Proyecto es clasificada como de carácter ofensivo moderado, por lo que el criterio de

Reporte no. 1761-21463-3-01
**14**
Estudio de impacto de olor - RR Wines Sagrada Familia

evaluación para la modelación que se realizara considerara el límite de 5 u.o./m [3] como
percentil 98 de promedios horarios.

## 2.9 Descripción de las fuentes y escenarios de modelación

Para la modelación de la Planta se considera la modelación del escenario actual. En la
Tabla 6 se especifican las condiciones de funcionamiento de cada fuente en los
escenarios de modelación propuestos, indicando si las mismas son generadora de gases
odoríficos para ser consideradas en la modelación.

_**Tabla 6: Fuentes en la Planta de RILES RR Wines**_

<!-- INICIO TABLA 6 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- percentil 98 de promedios horarios. ## 2.9 Descripción de las fuentes y escenarios de modelación Para la modelación de la Planta se considera la modelación del escenario actual. En la -->

**Tabla 6: se especifican las condiciones de funcionamiento de cada fuente en los**

| Escenario | Col2 | No | Fuente | Descripción | Incluida en la<br>modelación |
| --- | --- | --- | --- | --- | --- |
| Actual | Proyectado | 1 | Tranque de Riego | Unidad Abierta | Si, operación durante los<br>meses de Junio, Julio y<br>Agosto |
| Actual | Proyectado | 2 | Reactor Aeróbico | Unidad Abierta, 2<br>unidades | Si |
| Actual | Proyectado | 3 | Digestor de Lodos | Unidad Abierta | Si |
| Actual | Proyectado | 4 | Ecualizador | Unidad Abierta | Si |
| Actual | Proyectado | 5 | Cuna de Secado | Unidad Abierta, 4<br>unidades | SI |
| Actual | Proyectado | 6 | Filtros Lamerales | Unidad Abierta, 2<br>unidades | Si |
| Actual | Proyectado | 7 | Filtro Rotatorio | Unidad Abierta | Si |
| Actual | Proyectado | 8 | Reactores<br>Anaeróbicos | 30 Unidades<br>Cerradas | No |
|  |  | 9 | Nuevo Filtro<br>Lamerales | Unidad Abierta, 2<br>unidades | Si |
|  |  | 10 | Nuevas Cunas de<br>Secado | Unidad Abierta, 3<br>unidades | Si |
|  |  | 11 | Tranque de Riego | Unidad Abierta | Si |

<!-- Estadísticas: 11 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- De acuerdo a la Para la modelación de la Planta se considera la modelación del escenario actual. En la Tabla 6 se especifican las condiciones de funcionamiento de cada fuente en los escenarios de modelación propuestos, indicando si las mismas son generadora de gases odoríficos para ser consideradas en la modelación. -->
<!-- FIN TABLA 6 -->


|Escenario|Col2|No|Fuente|Descripción|Incluida en la<br>modelación|
|---|---|---|---|---|---|
|Actual|Proyectado|1|Tranque de Riego|Unidad Abierta|Si, operación durante los<br>meses de Junio, Julio y<br>Agosto|
|Actual|Proyectado|2|Reactor Aeróbico|Unidad Abierta, 2<br>unidades|Si|
|Actual|Proyectado|3|Digestor de Lodos|Unidad Abierta|Si|
|Actual|Proyectado|4|Ecualizador|Unidad Abierta|Si|
|Actual|Proyectado|5|Cuna de Secado|Unidad Abierta, 4<br>unidades|SI|
|Actual|Proyectado|6|Filtros Lamerales|Unidad Abierta, 2<br>unidades|Si|
|Actual|Proyectado|7|Filtro Rotatorio|Unidad Abierta|Si|
|Actual|Proyectado|8|Reactores<br>Anaeróbicos|30 Unidades<br>Cerradas|No|
|||9|Nuevo Filtro<br>Lamerales|Unidad Abierta, 2<br>unidades|Si|
|||10|Nuevas Cunas de<br>Secado|Unidad Abierta, 3<br>unidades|Si|
|||11|Tranque de Riego|Unidad Abierta|Si|

De acuerdo a la Para la modelación de la Planta se considera la modelación del escenario
actual. En la Tabla 6 se especifican las condiciones de funcionamiento de cada fuente en
los escenarios de modelación propuestos, indicando si las mismas son generadora de
gases odoríficos para ser consideradas en la modelación.

Tabla 6, para el escenario actual se han identificado ocho (08) fuentes generadoras de
olor.

Se utilizó la tasa de emisión fija para cada fuente en la modelación. Estos datos fueron
obtenidos de la campaña de muestreo en la Planta los días 10 y 11 de Enero de 2019
(Odotech, 2019).

Las fuentes de olor del Escenario 1 están representadas en la Figura 4 y Figura 5 y la
Tablas 7 se describen sus características.

Reporte no. 1761-21463-3-01
**15**
Estudio de impacto de olor - RR Wines Sagrada Familia

_**Tabla 7 : Características de las fuentes a modelar - Fuentes Superficiales**_

|Escenario|Col2|Fuente|ID|Tipo|Altura de<br>emisión<br>desde el<br>suelo|Concentra<br>ción de<br>Olor|Tasa de<br>Emisión<br>(1)|Área|Flujo de Olor|
|---|---|---|---|---|---|---|---|---|---|
|**Escenario**|**Escenario**|**Fuente**|**ID**|**Tipo**|**[m]**|**[u.o./Nm3] **|**[u.o./s/m2] **|**[m2] **|**[u.o./s]**|
|Actual|Proyectado|Tranque de Riego|TDR|Superficial|0|303|2.527|1550|3917|
|Actual|Proyectado|Reactor Aeróbico 1|RA1|Superficial|0|646|5.783|648|3747|
|Actual|Proyectado|Reactor Aeróbico 2|RA2|Superficial|0|646|5.783|640|3701|
|Actual|Proyectado|Digestor de Lodos|DDL|Superficial|2|203|1.691|30|51|
|Actual|Proyectado|Ecualizador|ECU|Superficial|0|454|3.783|368|1392|
|Actual|Proyectado|Cuna de Secado 1|CDS1|Superficial|0|197|1.641|30|49|
|Actual|Proyectado|Cuna de Secado 2|CDS2|Superficial|0|197|1.641|30|49|
|Actual|Proyectado|Cuna de Secado 3|CDS3|Superficial|0|197|1.641|30|49|
|Actual|Proyectado|Cuna de Secado 4|CDS4|Superficial|0|197|1.641|30|49|
|Actual|Proyectado|Filtros Lamerales|FL|Superficial|1,5|350|2.941|75|221|
|Actual|Proyectado|Filtro Rotatorio|FR|Superficial|1,5|343|2.855|9|26|
|||Nuevo Filtro Lameral|NFL|Superficial|1,5|350|2.941|50|147|
|||Nueva Cuna de Secado 1|NCDS1|Superficial|0|197|1.641|35|57|

[Reporte no. 1761-21463-3-01 ] **16**
Estudio de impacto de olor - RR Wines Sagrada Familia

|Escenario|Fuente|ID|Tipo|Altura de<br>emisión<br>desde el<br>suelo|Concentra<br>ción de<br>Olor|Tasa de<br>Emisión<br>(1)|Área|Flujo de Olor|
|---|---|---|---|---|---|---|---|---|
|**Escenario**|**Fuente**|**ID**|**Tipo**|**[m]**|**[u.o./Nm3] **|**[u.o./s/m2] **|**[m2] **|**[u.o./s]**|
|**Escenario**|Nueva Cuna de Secado 3|NCDS2|Superficial|0|197|1.641|35|57|
|**Escenario**|Nueva Cuna de Secado 3|NCDS3|Superficial|0|197|1.641|35|57|
|**Escenario**|Nuevo Tranque|NTR|Superficial|0|-|0.3(2)|8455|2537|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|Flujo Total de Olor<br>Escenario Actual|Flujo Total de Olor<br>Escenario Actual|13251|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|Flujo Total de Olor<br>Escenario Proyectado|Flujo Total de Olor<br>Escenario Proyectado|16106|

(1) La emisión de olores por unidad de área se calcula con concentración de olor (c en u.o/m [3] ), el flujo de muestreo (V = 250 L/min) y el área del túnel de
viento (A= 0,5 m [2] ) =

(2) Factor de Emisiones para tranques con aireación, Tabla 26, B&S Consultores (2015)

[Reporte no. 1761-21463-3-01 ] **17**
Estudio de impacto de olor - RR Wines Sagrada Familia

|Col1|PROYECTO<br>PLANTA RILES RR WINES<br>REGIÓN DEL MAULE|Col3|
|---|---|---|
||**Leyenda**<br>Ubicación del Proyecto|**Leyenda**<br>Ubicación del Proyecto|
||**Situación**<br>**Regional**<br>**Comuna de**<br>**Sagrada**<br>**Familia**<br> <br> <br> <br>|**Situación**<br>**Nacional**<br>|
||**Referencia Geodésica**<br>Proyección: UTM<br>Datum: WGS 84<br>Zona: 19H<br>Coordenadas centrales del<br>proyecto:<br>X 287.715 km<br>Y 6118.524 km|**Referencia Geodésica**<br>Proyección: UTM<br>Datum: WGS 84<br>Zona: 19H<br>Coordenadas centrales del<br>proyecto:<br>X 287.715 km<br>Y 6118.524 km|

**Figura 4: Fuentes - Escenario de Modelación Actual**

[Reporte no. 1761-21463-3-01 ] **18**
Estudio de impacto de olor - RR Wines Sagrada Familia

|Col1|PROYECTO<br>PLANTA RILES RR WINES<br>REGIÓN DEL MAULE|Col3|
|---|---|---|
||**Leyenda**<br>Ubicación del Proyecto|**Leyenda**<br>Ubicación del Proyecto|
||**Situación**<br>**Regional**<br>**Comuna de**<br>**Sagrada**<br>**Familia**<br> <br> <br> <br>|**Situación**<br>**Nacional**<br>|
||**Referencia Geodésica**<br>Proyección: UTM<br>Datum: WGS 84<br>Zona: 19H<br>Coordenadas centrales del<br>proyecto:<br>X 287.715 km<br>Y 6118.524 km|**Referencia Geodésica**<br>Proyección: UTM<br>Datum: WGS 84<br>Zona: 19H<br>Coordenadas centrales del<br>proyecto:<br>X 287.715 km<br>Y 6118.524 km|

**Figura 5: Fuentes - Escenario de Modelación Proyectada**

[Reporte no. 1761-21463-3-01 ] **19**
Estudio de impacto de olor - RR Wines Sagrada Familia

aaa

# 3 RESULTADOS DE LA MODELACIÓN DE DISPERSIÓN ATMOSFÉRICA

El modelo de dispersión atmosférico predice como los olores se van a dispersar en los
alrededores de la Planta de RILES RR Wines, localizada en la comuna de Sagrada
Familia, Región del Maule, Chile.

Para los propósitos de este estudio, se calcularon el percentil 98 (C P98 ) y la frecuencia de
exceso de los límites de 5 u.o./m [3 ] en porcentaje y hora por año.

Los resultados de percentil 98 son el valor de la concentración tal que el 98 % de las
concentraciones calculadas en este punto son inferiores al valor determinado por la
modelación y 2 % de los valores de concentración calculados son superiores (175 horas/
acumuladas en un año).

Las frecuencias de exceso de los límites de 5 u.o./m [3 ] en porcentaje y hora por año [4]
permite saber cuánto tiempo los receptores discretos son expuestos de acuerdo a los
límites propuestos. Los resultados para cada escenario se presentan en forma gráfica en
el ANEXO C.

**3.1 RESULTADOS ESCENARIO ACTUAL**

Para el Escenario actual de modelación, la concentración del percentil 98 más alta
calculada en los receptores discretos es de 4,7 u.o./m [3] . Esta concentración fue calculada
en el receptor vecino Este Interno 2, ubicado a 80 metros de la Planta. En los demás
receptores discretos las concentraciones se encuentran entre 0.0 y 4,4 u.o./m [3] .

El resultado máximo de la frecuencia de exceso del límite de 5 u.o./m [3], que indica el nivel
donde el olor es calificable y puede comenzar a recibirse quejas (puede ser identificado),
alcanza 1,8% ó 166 horas/año para el receptor vecino Este Interno 2, ubicado a 80 metros
de la Planta. En los demás receptores discretos las frecuencias de exceso se encuentran
alrededor del 0,0% a 1,7 o 0 a 153 horas/año

Los resultados en los receptores discretos de la concentración del percentil 98 y las
frecuencias de exceso de los límites de 5 u.o./m [3 ] en porcentaje y horas/año están
resumidos en la Tabla 8. Las isopletas de concentración se muestran en el ANEXO C.

4 De las 8.760 horas/año, de acuerdo a la data meteorológica utilizada para esta modelación.

_**Tabla 8: Resultados de concentración de olor y frecuencia de exceso en los**_
_**receptores discretos Escenario Actual**_

|Receptores Discretos|Percentil 98|Frecuencia de Exceso del Límite de 5 u.o./m3|
|---|---|---|
|**Receptores Discretos**|**[u.o./ m3] **|**% (# horas/año)**|
|Primer Vecino Noreste (NE)|0,8|0,0% (0 h/año)|
|Primer Vecino Este (E)|0,7|0,0% (1 h/año)|
|Primer Vecino Sur Interno (S)|4,4|1,7% (149 h/año)|
|Segundo Vecino Sur Interno (SO)|2,1|0,1% (11 h/año)|
|Primer Vecino Norte (N)|0,1|0,0% (0 h/año)|
|Tercer Vecino Sur Interno (S)|2,1|0,1% (11 h/año)|
|Vecino Este Interno 1 (E)|3,4|1,1% (104 h/año)|
|Vecino Este Interno 2 (E)|4,7|1,8% (166 h/año)|
|Segundo Vecino Sur Interno (S)|4,4|1,7% (153 h/año)|
|Vecino Noreste 1 (NE)|0,4|0,1% (6 h/año)|
|Vecino Noreste 2 (NE)|0,3|0,0% (4 h/año)|
|Vecino Noreste 3 (NE)|0,3|0,0% (4 h/año)|
|Vecino Noreste 4 (NE)|0,3|0,0% (1 h/año)|
|Vecino Noreste 5 (NE)|0,3|0,0% (2 h/año)|
|Vecino Noreste 6 (NE)|0,8|0,0% (0 h/año)|
|Vecino Noreste 7 (NE)|0,8|0,0% (0 h/año)|
|Vecino Noreste 8 (NE)|0,8|0,0% (0 h/año)|
|Vecino Noreste 9 (NE)|0,2|0,0% (3 h/año)|
|Vecino Noreste 10 (NE)|0,3|0,1% (4 h/año)|
|Vecino Noreste 11 (NE)|0,2|0,0% (0 h/año)|
|Vecino Noreste 12 (NE)|0,2|0,0% (0 h/año)|

**3.2 RESULTADOS ESCENARIO PROYECTADO**

Para el Escenario actual de modelación, la concentración del percentil 98 más alta
calculada en los receptores discretos es de 5,3 u.o./m [3] . Esta concentración fue calculada
en el receptor vecino Este Interno 2, ubicado a 80 metros de la Planta. En los demás
receptores discretos las concentraciones se encuentran entre 0.0 y 4,8 u.o./m [3] .

El resultado máximo de la frecuencia de exceso del límite de 5 u.o./m [3], que indica el nivel
donde el olor es calificable y puede comenzar a recibirse quejas (puede ser identificado),
alcanza 2,2% ó 193 horas/año para el receptor vecino Este Interno 2, ubicado a 80 metros
de la Planta. En los demás receptores discretos las frecuencias de exceso se encuentran
alrededor del 0,0% a 1,9 o 0 a 172 horas/año

Cabe señalar que dicho receptor vecino Este Interno 2, ubicado a 80 metros de la Planta,
corresponde a una vivienda que se utiliza temporalmente, al reconocer que el nivel de
superación coincide con el uso del tranque de riego entre los meses de Junio y
Septiembre, se ha considerado para la futura operación del Proyecto la no utilización de
dicha vivienda durante el periodo señalado para evitar que población se encuentre
expuesta a los niveles de concentración de olor obtenidos como resultado de la
modelación.

Los resultados en los receptores discretos de la concentración del percentil 98 y las
frecuencias de exceso de los límites de 5 u.o./m [3 ] en porcentaje y horas/año están
resumidos en la Tabla 9. Las isopletas de concentración se muestran en el ANEXO C.

_**Tabla 9: Resultados de concentración de olor y frecuencia de exceso en los**_
_**receptores discretos Escenario Proyectado**_

|Receptores Discretos|Percentil 98|Frecuencia de Exceso del Límite de 5 u.o./m3|
|---|---|---|
|**Receptores Discretos**|**[u.o./ m3] **|**% (# horas/año)**|
|Primer Vecino Noreste (NE)|0,9|0,0% (0 h/año)|
|Primer Vecino Este (E)|0,9|0,0% (3 h/año)|
|Primer Vecino Sur Interno (S)|4,8|1,9% (168 h/año)|
|Segundo Vecino Sur Interno (SO)|2,8|0,3% (27 h/año)|
|Primer Vecino Norte (N)|0,1|0,0% (0 h/año)|
|Tercer Vecino Sur Interno (S)|2,8|0,3% (25 h/año)|
|Vecino Este Interno 1 (E)|4,2|1,7% (149 h/año)|
|Vecino Este Interno 2 (E)|5,3|2,2% (193 h/año)|
|Segundo Vecino Sur Interno (S)|4,8|1,9% (172 h/año)|
|Vecino Noreste 1 (NE)|0,6|0,1% (7 h/año)|
|Vecino Noreste 2 (NE)|0,5|0,1% (6 h/año)|
|Vecino Noreste 3 (NE)|0,4|0,1% (8 h/año)|
|Vecino Noreste 4 (NE)|0,4|0,0% (3 h/año)|
|Vecino Noreste 5 (NE)|0,4|0,0% (1 h/año)|
|Vecino Noreste 6 (NE)|0,9|0,0% (3 h/año)|
|Vecino Noreste 7 (NE)|0,9|0,0% (0 h/año)|
|Vecino Noreste 8 (NE)|1,0|0,0% (0 h/año)|
|Vecino Noreste 9 (NE)|0,3|0,0% (4 h/año)|
|Vecino Noreste 10 (NE)|0,4|0,1% (7 h/año)|
|Vecino Noreste 11 (NE)|0,3|0,0% (2 h/año)|
|Vecino Noreste 12 (NE) <br>|0,4|0,0% (0 h/año)|

# 4 CONCLUSION

Para la Planta de RILES RR Wines, ubicada en la comuna de Sagrada Familia, en la
Región del Maule, se realizó la modelación de la dispersión atmosférica a través del
modelo Calpuff [5], para evaluar el impacto de olor en su escenario actual de operación,
midiendo este impacto sobre la población aledaña.

Las etapas desarrolladas para la realización del estudio fueron las siguientes:

a. _Entrega de información por parte del cliente_ . En este sentido, la información está
relacionada a la configuración de las fuentes odoríficas proyectadas a causar
impacto por la Planta (por ejemplo, áreas de emisión de las fuentes [en m [2] ], alturas
de emisión desde el suelo, entre otros).
b. _Cálculo de los Flujos de Olor_ . En este sentido se utilizaron las concentraciones de
olor obtenidas a partir de análisis por olfatometría dinámica, a partir de la toma de
muestras de olor en las fuentes identificadas como odoríficas en la Planta,
campaña realizada en Enero de 2019.
c. _Modelación de la dispersión atmosférica a través del modelo Calpuff,_ el cual
realizó una simulación matemática de los procesos físicos y químicos que
determinan el transporte, dispersión y transformación de los contaminantes
atmosféricos, en este caso, el Olor. El modelo estimó las concentraciones en la
inmisión, donde se utilizaron como parámetros de entrada la meteorología del
lugar [6], topografía, emisión, características de las fuentes, y se añadieron veintiún
(21) receptores discretos.
d. _Escenarios de modelación._ Para la Planta de RILES RR Wines, se consideró la
modelación del escenario actual y proyectado en operación.
e. _Estimación del impacto de olor._ La modelación permitió obtener el cálculo de la
concentración del percentil 98, donde las concentraciones calculadas en este
punto son inferiores al valor determinado por la modelación y el 2% de los valores
de concentración calculados son superiores (175 horas/ acumuladas en un año);
y las frecuencias de exceso de los límites de 5 u.o./m [3 ], valores obtenidos en
porcentaje y hora/año. Todos estos resultados se muestran en las Tablas 8 y 9 y
en forma gráfica en el ANEXO C.

De los resultados obtenidos por la modelación, se tienen:

 - De acuerdo a la configuración actual del Proyecto, la concentración del percentil
98 más alta calculada en los receptores discretos es de 4,7 u.o./m [3] ; esta
concentración fue calculada en el receptor vecino Este Interno 2, ubicado a 80
metros de la Planta.

 - El resultado máximo de la frecuencia de exceso del límite de 5 u.o./m [3], que indica
el nivel donde el olor es calificable y puede comenzar a recibirse quejas (puede
ser identificado), alcanza 1,8% ó 166. horas/año para el receptor vecino Este
Interno 2, ubicado a 80 metros de la Planta.

5 Recomendado por la Guía para el uso de modelos de calidad del aire en el SEIA (SEA, 2012).
6 Se utilizó la meteorología de pronóstico WRF, con período de un año.

 - De acuerdo a la configuración proyectada del Proyecto, la concentración del
percentil 98 más alta calculada en los receptores discretos es de 5,3 u.o./m [3] ; esta
concentración fue calculada en el receptor vecino Este Interno 2, ubicado a 80
metros de la Planta.

 - El resultado máximo de la frecuencia de exceso del límite de 5 u.o./m [3], que indica
el nivel donde el olor es calificable y puede comenzar a recibirse quejas (puede
ser identificado), alcanza 2,2% ó 193. horas/año para el receptor vecino Este
Interno 2, ubicado a 80 metros de la Planta

Cabe señalar que se realizó el análisis de incertidumbre de la meteorología de pronostico
WRF utilizada para la modelación, a partir del cual fue posible determinar que la
evaluación de impacto e olor del Proyecto se desarrolló en el peor escenario de dispersión
posible, por lo que no se requieren factores de corrección para los resultados.

A partir de lo anteriormente presentado es posible señalar los aportes en concentración
de olor generados por la operación actual de la Planta de RILES, no se generan efectos
significativos en cuanto el nivel de las concentraciones de olor generadas sobre los
receptores cercanos, ya que los niveles de concentración generados no superan el valor
de 4,7 u.o./m [3] .

Por su parte en el escenario concentrado si se generan efectos sobre el receptor vecino
Este Interno 2, ubicado a 80 metros de la Planta, en donde los niveles de concentración
generados no superan el valor de 5,3 u.o./m [3], superando el límite de 5 u.o./m [3] como
percentil 98 de concentraciones. Sin embargo cabe señalar que dicho receptor
corresponde a una vivienda que se utiliza temporalmente, principalmente durante la
época de vendimia, esto es entre Febrero y Mayo, por lo que al reconocer que el nivel de
superación coincide con el uso del tranque de riego entre los meses de Junio y
Septiembre, se ha considerado para la futura operación del Proyecto la no utilización de
dicha vivienda durante el periodo señalado de mayor impacto, por lo que la población no
se encuentre expuesta a los niveles de concentración de olor obtenidos como resultado
de la modelación para este receptor.

Los resultados en los receptores discretos de la concentración del percentil 98 y las
frecuencias de exceso de los límites de 5 u.o./m [3 ] en porcentaje y horas/año para ambos
escenarios de modelación se encuentran resumidos en la Tabla 7. Las isopletas de
concentración se muestran en el ANEXO C.

_Este estudio presenta una evaluación del impacto de olor en un momento determinado,_
_según el escenario de emisiones configurado, los resultados del muestreo y datos_
_meteorológicos utilizados (WRF periodo del 01/01/2016 al 31/12/2016). Cualquier_
_variación de estas condiciones puede aumentar o disminuir el nivel de los olores que se_
_traduciría en un impacto de olor diferente al que se describe en este informe._

# 5 REFERENCIAS

ECOTEC (2013), Estudio: Antecedentes para la Regulación de Olores en Chile, realizado
para la Subsecretaría del Medio Ambiente, Santiago de Chile, Agosto

NCh 3190 (2010), Calidad del Aire - Determinación de la concentración de olor por
olfatometría dinámica. (INN).

SEA (2012), Guía para el uso de modelos de calidad del aire en el SEIA.

SEA (2017), Guía para la Predicción y Evaluación de Impactos por Olor en el SEIA

Odotech (2019), MEMO de Configuración Planta de RILES RR Wines, N° 1761-2146302-01

B&S Consultores (2015), Informe Final Servicio de Recopilación y Sistematización de
Factores de Emisión al Aire para el SEA

Odotech (2018), Reporte de Muestreo Planta de RILES RR Wines. Reporte N° 176121463 - 01 - 1

# _ANEXO A: SERIES DE TIEMPO DE VELOCIDAD Y DIRECCIÓN DEL_ _VIENTO_

Se presentan las figuras de las series de tiempo de la velocidad y dirección del viento para
la meteorología observacional y de pronóstico WRF, las cuales son explicadas en detalle
en la sección 2.6 Información Meteorológica.

# LISTA DE FIGURAS ANEXO A

**Figura A-1: Serie de tiempo para registros horarios de velocidad del viento - Datos**
**Estación Sagrada Familia ............................................................................ 28**

**Figura A-2: Serie de tiempo para registros horarios de velocidad del viento - Datos**
**WRF. 29**

**Figura A-3: Serie de tiempo para registros horarios de dirección del viento - Datos**
**Estación Sagrada Familia. ........................................................................... 30**

**Figura A-4: Serie de tiempo para registros horarios de dirección del viento - Datos**
**WRF 31**

_**Figura A-1: Serie de tiempo para registros horarios de velocidad del viento - Datos Estación Sagrada Familia**_

[Reporte no. 1761-21463-3-01 ] **28**
Estudio de impacto de olor - RR Wines Sagrada Familia

_**Figura A-2: Serie de tiempo para registros horarios de velocidad del viento - Datos WRF.**_

[Reporte no. 1761-21463-3-01 ] **29**
Estudio de impacto de olor - RR Wines Sagrada Familia

_**Figura A-3: Serie de tiempo para registros horarios de dirección del viento - Datos Estación Sagrada Familia.**_

[Reporte no. 1761-21463-3-01 ] **30**
Estudio de impacto de olor - RR Wines Sagrada Familia

_**Figura A-4: Serie de tiempo para registros horarios de dirección del viento - Datos WRF**_

[Reporte no. 1761-21463-3-01 ] **31**
Estudio de impacto de olor - RR Wines Sagrada Familia

# _ANEXO B: ANÁLISIS DE INCERTIDUMBRE_

Se presentan las figuras de la distribución del viento para el período en estudio, de ambas
meteorologías, observacional y de pronóstico WRF, las cuales son explicadas en detalle
en la sección 2.7 Análisis de incertidumbre.

# LISTA DE FIGURAS ANEXO B

**Figura B- 1: Gráficos de distribución de viento para el período ............................. 33**

**Figura B- 2: Rosas de viento para el período ........................................................... 34**

**Figura B- 3: Frecuencia diaria de dirección de viento ............................................. 35**

**Figura B- 4: Ciclo estacional de campos de viento .................................................. 36**

**Figura B- 5: Rosas de viento por periodo del día (parte 1) ...................................... 38**

**Figura B- 6: Rosas de viento por periodo del día (parte 2) ...................................... 39**

**Figura B- 7: Ciclo diario promedio de velocidad de viento (m/s) ............................ 39**

|Gráfico Distribución Velocidad de Viento<br>Datos Observados<br>Periodo Enero a Diciembre de 2016|Gráfico Distribución Velocidad de Viento<br>Datos Modelo de Pronostico<br>Periodo Enero a Diciembre de 2016|
|---|---|
|<br>|<br>|

_**Figura B- 1: Gráficos de distribución de viento para el período**_

[Reporte no. 1761-21463-3-01 ] **33**
Estudio de impacto de olor - RR Wines Sagrada Familia

|Rosa de Viento<br>Datos Observados<br>Periodo Enero a Diciembre de 2016|Rosa de Viento<br>Datos Modelo de Pronostico<br>Periodo Enero a Diciembre de 2016|
|---|---|
|<br>|<br>|

_**Figura B- 2: Rosas de viento para el período**_

[Reporte no. 1761-21463-3-01 ] **34**
Estudio de impacto de olor - RR Wines Sagrada Familia

_**Figura B- 3: Frecuencia diaria de dirección de viento**_

_**Figura B- 4: Ciclo estacional de campos de viento**_

|Rosa de Viento<br>Datos Observados<br>Periodo Enero a Diciembre de 2016<br>Periodo entre 00:00 y 05:00 horas|Rosa de Viento<br>Datos WRF<br>Periodo Enero a Diciembre de 2016<br>Periodo entre 00:00 y 05:00 horas|
|---|---|
|||
|Rosa de Viento<br>Datos Observados<br>Periodo Enero a Diciembre de 2016<br>Periodo entre 06:00 y 11:00 horas|Rosa de Viento<br>Datos WRF<br>Periodo Enero a Diciembre de 2016<br>Periodo entre 06:00 y 11:00 horas|
|||

|Figura B- 5: Rosas de viento|por periodo del día (parte 1)|
|---|---|
|Rosa de Viento<br>Datos Observados<br>Periodo Enero a Diciembre de 2016<br>Periodo entre 12:00 y 17:00 horas|Rosa de Viento<br>Datos WRF<br>Periodo Enero a Diciembre de 2016<br>Periodo entre 12:00 y 17:00 horas|
|||
|Rosa de Viento<br>Datos Observados<br>Periodo Enero a Diciembre de 2016<br>Periodo entre 18:00 y 23:00 horas|Rosa de Viento<br>Datos WRF<br>Periodo Enero a Diciembre de 2016<br>Periodo entre 18:00 y 23:00 horas|
|||

|Col1|Figura B- 6: Rosas de viento por periodo del día (parte 2)|
|---|---|
|**Datos Observados Estación Sagrada**<br>**Familia**|<br>0.0<br>0.5<br>1.0<br>1.5<br>2.0<br>2.5<br>3.0<br>3.5<br>4.0<br>4.5<br>5.0<br>5.5<br>6.0<br>6.5<br>7.0<br>7.5<br>8.0<br>0<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9 10 11 12 13 14 15 16 17 18 19 20 21 22 23<br>**Velocidad del viento (m/s)**<br>**Hora Local**<br>Percentile 5<br>Percentile 95<br>Promedio|
|**Datos WRF**|<br><br>0.0<br>0.5<br>1.0<br>1.5<br>2.0<br>2.5<br>3.0<br>3.5<br>4.0<br>4.5<br>5.0<br>5.5<br>6.0<br>6.5<br>7.0<br>7.5<br>8.0<br>0<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9 10 11 12 13 14 15 16 17 18 19 20 21 22 23<br>**Velocidad del viento (m/s)**<br>**Hora Local**<br>Percentile 5<br>Percentile 95<br>Promedio|

_**Figura B- 7: Ciclo diario promedio de velocidad de viento (m/s)**_

# _ANEXO C: RESULTADOS GRÁFICOS DE MODELACIÓN_

Los resultados se presentan en forma gráfica ilustran mediante iso-contornos de los valores
de concentración, calculados en percentil 98 y así mismo, de las frecuencias de exceso del
nivel de 5 u.o./m [3], mostrando la siguiente información:

 - Isopleta de concentración de olor o frecuencia de exceso (líneas que unen los
diferentes puntos con similares valores o rangos de valor), las cuales se encuentran
superpuestas en el mapa sobre el área de modelación. Cada color representa un
rango diferente. Una escala UTM se encuentra situada en el lado inferior e izquierdo.

 - Una leyenda en la que se presentan los distintos rangos y colores asociados a las
concentraciones de olor, se expresan en unidades de olor por metros cúbicos
(u.o./m [3] ), para las concentraciones máximas y el percentil.

 - La frecuencia de exceso de un nivel de olor está expresada horas/año.

 - Los receptores discretos están representados con una cruz azul.

# LISTA DE FIGURAS ANEXO C

Figura C - 1: Percentil 98 Escenario Actual **................................................................... 41**

Figura C - 2: Frecuencia de Exceso 5 u.o./m [3] Escenario Actual **................................... 42**

Figura C - 3: Percentil 98 Escenario Proyectado **........................................................... 43**

Figura C - 4: Frecuencia de Exceso 5 u.o./m [3] Escenario Proyectado **........................... 44**

|Col1|Col2|Col3|Col4|PROYECTO<br>PLANTA DE RILES RR WINES<br>REGIÓN DEL MAULE|Col6|
|---|---|---|---|---|---|
|||||**Leyenda**<br>Ubicación del Proyecto|**Leyenda**<br>Ubicación del Proyecto|
|||||**Situación**<br>**Regional**<br> <br>**Comuna de**<br>**Sagrada Familia**<br> <br> <br> <br> <br> <br> <br>|**Situación**<br>**Nacional**<br>|
|||||**Referencia Geodésica**<br>Proyección: UTM<br>Datum: WGS 84<br>Zona: 19H<br>Coordenadas centrales del<br>proyecto:<br>X 287.715 km<br>Y 6118.524 km|**Referencia Geodésica**<br>Proyección: UTM<br>Datum: WGS 84<br>Zona: 19H<br>Coordenadas centrales del<br>proyecto:<br>X 287.715 km<br>Y 6118.524 km|
||_Figura C - 1: Percentil 98 Escenario Actual_|Proyecto: 1761-21463|Modelador: Roberto Fuenzalida|Modelador: Roberto Fuenzalida|Modelador: Roberto Fuenzalida|
||Datos Meteorológicos - Periodo:<br>01/01/2016 al 31/12/2016, 00:00 a 23:00|Página 41|Fecha: Marzo de 2019|Fecha: Marzo de 2019|Fecha: Marzo de 2019|
||Comentario: S/C|Comentario: S/C|Comentario: S/C|Comentario: S/C|Comentario: S/C|

|Col1|Col2|Col3|Col4|PROYECTO<br>PLANTA DE RILES RR WINES<br>REGIÓN DEL MAULE|Col6|
|---|---|---|---|---|---|
|||||**Leyenda**<br>Ubicación del Proyecto|**Leyenda**<br>Ubicación del Proyecto|
|||||**Situación**<br>**Regional**<br> <br>**Comuna de**<br>**Sagrada Familia**<br> <br> <br> <br> <br> <br> <br>|**Situación**<br>**Nacional**<br>|
|||||**Referencia Geodésica**<br>Proyección: UTM<br>Datum: WGS 84<br>Zona: 19H<br>Coordenadas centrales del<br>proyecto:<br>X 287.715 km<br>Y 6118.524 km|**Referencia Geodésica**<br>Proyección: UTM<br>Datum: WGS 84<br>Zona: 19H<br>Coordenadas centrales del<br>proyecto:<br>X 287.715 km<br>Y 6118.524 km|
||_Figura C - 2: Frecuencia de Exceso 5 u.o./m3 Escenario Actual_|Proyecto: 1761-21463|Modelador: Roberto Fuenzalida|Modelador: Roberto Fuenzalida|Modelador: Roberto Fuenzalida|
||Datos Meteorológicos - Periodo:<br>01/01/2016 al 31/12/2016, 00:00 a 23:00|Página 42|Fecha: Marzo de 2019|Fecha: Marzo de 2019|Fecha: Marzo de 2019|
||Comentario: S/C|Comentario: S/C|Comentario: S/C|Comentario: S/C|Comentario: S/C|

|Col1|Col2|Col3|Col4|PROYECTO<br>PLANTA DE RILES RR WINES<br>REGIÓN DEL MAULE|Col6|
|---|---|---|---|---|---|
|||||**Leyenda**<br>Ubicación del Proyecto|**Leyenda**<br>Ubicación del Proyecto|
|||||**Situación**<br>**Regional**<br> <br>**Comuna de**<br>**Sagrada Familia**<br> <br> <br> <br> <br> <br> <br>|**Situación**<br>**Nacional**<br>|
|||||**Referencia Geodésica**<br>Proyección: UTM<br>Datum: WGS 84<br>Zona: 19H<br>Coordenadas centrales del<br>proyecto:<br>X 287.715 km<br>Y 6118.524 km|**Referencia Geodésica**<br>Proyección: UTM<br>Datum: WGS 84<br>Zona: 19H<br>Coordenadas centrales del<br>proyecto:<br>X 287.715 km<br>Y 6118.524 km|
||_Figura C - 3: Percentil 98 Escenario Proyectado_|Proyecto: 1761-21463|Modelador: Roberto Fuenzalida|Modelador: Roberto Fuenzalida|Modelador: Roberto Fuenzalida|
||Datos Meteorológicos - Periodo:<br>01/01/2016 al 31/12/2016, 00:00 a 23:00|Página 43|Fecha: Marzo de 2019|Fecha: Marzo de 2019|Fecha: Marzo de 2019|
||Comentario: S/C|Comentario: S/C|Comentario: S/C|Comentario: S/C|Comentario: S/C|

|Col1|Col2|Col3|Col4|PROYECTO<br>PLANTA DE RILES RR WINES<br>REGIÓN DEL MAULE|Col6|
|---|---|---|---|---|---|
|||||**Leyenda**<br>Ubicación del Proyecto|**Leyenda**<br>Ubicación del Proyecto|
|||||**Situación**<br>**Regional**<br> <br>**Comuna de**<br>**Sagrada Familia**<br> <br> <br> <br> <br> <br> <br>|**Situación**<br>**Nacional**<br>|
|||||**Referencia Geodésica**<br>Proyección: UTM<br>Datum: WGS 84<br>Zona: 19H<br>Coordenadas centrales del<br>proyecto:<br>X 287.715 km<br>Y 6118.524 km|**Referencia Geodésica**<br>Proyección: UTM<br>Datum: WGS 84<br>Zona: 19H<br>Coordenadas centrales del<br>proyecto:<br>X 287.715 km<br>Y 6118.524 km|
||_Figura C - 4: Frecuencia de Exceso 5 u.o./m3 Escenario_<br>_Proyectado_|Proyecto: 1761-21463|Modelador: Roberto Fuenzalida|Modelador: Roberto Fuenzalida|Modelador: Roberto Fuenzalida|
||Datos Meteorológicos - Periodo:<br>01/01/2016 al 31/12/2016, 00:00 a 23:00|Página 44|Fecha: Marzo de 2019|Fecha: Marzo de 2019|Fecha: Marzo de 2019|
||Comentario: S/C|Comentario: S/C|Comentario: S/C|Comentario: S/C|Comentario: S/C|

533 Airport Blvd., Suite 330,
Burlingame, CA., 94010,
United States of America

3333 Queen Mary Rd
Suite 301, Montreal, Quebec,
H3V 1A2, Canada

Calle Henri Dunant 17

28016 Madrid
Spain

Level 19, 240 Queen St,

Brisbane, Qld,
Australia, 4000

Suecia 211
Oficina 1602, Santiago
Chile, 7510153

**www.envirosuite.com info@envirosuite.com**