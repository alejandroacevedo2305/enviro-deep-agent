---
title: SOLEK001.INF001.Rev0
author: Ignacio Jaque Vidal
date: D:20240313233332-03'00'
language: es
type: manual
pages: 31
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Proyecto Parque Fotovoltaico Graneros
-->

### Declaración de Impacto Ambiental - Anexo N°
## Estudio de inundación Estero La Cadena

# Proyecto Parque Fotovoltaico Graneros

Preparado para SOLEK Chile
Código de documento: SOLEK001.INF001.Rev0

Marzo, 2024

Proyecto Parque Fotovoltaico Graneros
SOLEK001.INF001.Rev0

Estudio de inundación Estero La Cadena

i

Estudio de inundación Estero La Cadena

ÍNDICE DE CONTENIDO

1 INTRODUCCIÓN.............................................................................................................................. 4

2 ÁREA DE ESTUDIO .......................................................................................................................... 6

3 METODOLOGÍA .............................................................................................................................. 8

3.1 Estudio Hidrológico .......................................................................................................................................... 8

3.1.1 Revisión de antecedentes .................................................................................................................................... 8

3.1.2 Caracterización hidrográfica .............................................................................................................................. 11
3.1.3 Precipitaciones máximas .................................................................................................................................... 11

3.1.4 Escurrimientos máximos .................................................................................................................................... 11

3.2 Estudio Hidráulico .......................................................................................................................................... 12

3.2.1 _Software_ de modelación .................................................................................................................................... 12
3.2.2 Geometría y extensión del cauce....................................................................................................................... 15
3.2.3 Coeficiente de Manning ..................................................................................................................................... 17

3.2.4 Obra de cruce: Puente Ruta Ex 5 Sur ................................................................................................................. 18

3.2.5 Escenarios y condiciones de modelación .......................................................................................................... 19

4 RESULTADOS ................................................................................................................................ 20

4.1.1 Caracterización hidrográfica .............................................................................................................................. 20
4.2 Precipitaciones máximas ................................................................................................................................ 22

4.3 Escorrentía máxima ....................................................................................................................................... 25

4.4 Modelación hidráulica ................................................................................................................................... 27

5 CONCLUSIONES ............................................................................................................................ 30

TABLAS

Tabla 3-1 Listado de estaciones meteorológicas DGA .................................................................................................... 9

Tabla 3-2 Listado de estaciones fluviométricas DGA ...................................................................................................... 9

Tabla 3-3 Estimación del coeficiente de Manning según método de Cowan ............................................................. 17

Tabla 4-1 Características geomorfológicas de las cuencas estudiadas ....................................................................... 20

Tabla 4-2 Principales estadígrafos de precipitaciones máximas anuales en 24 horas ............................................... 22

Tabla 4-3 Resultados Test Chi Cuadrado para bondad de ajuste a series de precipitación según estación
meteorológica ................................................................................................................................................................. 22

Tabla 4-4 Precipitación máxima en 24 hrs según periodo de retorno y estación meteorológica (mm) ................... 23

Tabla 4-5 Principales estadígrafos de series caudales máximos instantáneos anuales según cuenca ...................... 25

Tabla 4-6 Resultados Test Chi Cuadrado para bondad de ajuste a serie de caudales máximos instantáneos ......... 25

Tabla 4-7 Caudales máximos instantáneos según periodo de retorno método Transposición de caudales ............ 26

FIGURAS

Figura 1-1 Ubicación nacional, regional y local del emplazamiento de las obras del Proyecto ................................... 5

Figura 2-1 Área de estudio ............................................................................................................................................... 7

Proyecto Parque Fotovoltaico Graneros
SOLEK001.INF001.Rev0

ii

Estudio de inundación Estero La Cadena

Figura 3-1 Ubicación estaciones meteorológicas y fluviométricas cercanas al área de estudio ............................... 10

Figura 3-2 Representación de los términos de la ecuación de energía en dos secciones .......................................... 12

Figura 3-3 Esquema del método usado por HEC-RAS para calcular las subsecciones ................................................ 14

Figura 3-4 Resumen vista en planta de perfiles transversales generados en HEC-GeoRAS en cauces estudiados .. 16

Figura 3-5 Fotografías Estero La Cadena ....................................................................................................................... 18

Figura 3-6 Fotografías del Puente Ruta Ex 5 Sur y Estero La Cadena (a) y su vista esquemática en Hec-Ras (b) ..... 19

Figura 4-1 Delimitación de cuencas hidrográficas del Estero La Cadena .................................................................... 21

Figura 4-2 Resultados precipitaciones máximas en 24 horas en mapa según estación (T=10 años) ........................ 24

Figura 4-3 Ajuste distribución LogNormal a serie de caudales máximos instantáneos anuales cuenca en estudio. 26

Figura 4-4 Resultados eje hidráulico en distintas secciones transversales del Estero La Cadena ............................. 27

Figura 4-5 Resultados eje hidráulico en perfil longitudinal, Estero La Cadena ........................................................... 28

Figura 4-6 Superficie de inundación Estero La Cadena para crecida (T=100 años) .................................................... 29

APÉNDICES

Apéndice A - Estudio Topográfico

Apéndice B - Series de precipitación máxima en 24 hrs de las estaciones meteorológicas y Serie de caudales

máximos instantáneos anuales de la estación fluviométrica

Apéndice C - Resultados del Test Chi cuadrado y ajuste de probabilidades de las estaciones meteorológicas y

fluviométricas

Apéndice D - Archivos digitales cartográficos y de modelación

Apéndice E - Tablas de resultados numéricos modelación hidráulica

Apéndice F - Estudio de Riesgo Fundado (Emanagement, 2021)

Proyecto Parque Fotovoltaico Graneros
SOLEK001.INF001.Rev0

iii

Estudio de inundación Estero La Cadena

1 INTRODUCCIÓN

En el marco de la presentación de la Declaración de Impacto Ambiental (DIA) del Proyecto “PFV Graneros”, en
adelante el Proyecto, SOLEK Chile solicitó a Petricor Ingeniería un estudio de hidrológico e hidráulico que permita
establecer la superficie de inundación del Estero La Cadena, con el objetivo de esclarecer la superficie de drenaje
del sector de estudio para un evento de crecida y determinar si existe el riesgo de inundación en el sector de
emplazamiento del Proyecto.

El siguiente documento presenta caracterización hidrológica e hidráulica del Estero La Cadena, donde se entregaron
los antecedentes técnicos que permiten estimar las precipitaciones máximas y caudales máximos que se podrían
generar en el área de estudio, con el objetivo de determinar la magnitud de las crecidas para diferentes periodos de
retorno, y en particular el período de retorno de 100 años que define la superficie de los cauces. Luego, se realizó
una simulación hidráulica del comportamiento de estos flujos naturales para determinar las cotas de inundación y
el área de inundación potencial para las crecidas respectivas. Cabe mencionar que, para cumplir con el objetivo de
la evaluación de recursos hídricos, se definieron trabajos de gabinete para procesar la información disponible y
trabajos en terreno que permitieron levantar la información _in situ_ .

El Proyecto en evaluación consiste en la construcción, operación y cierre de una planta de generación de energía
fotovoltaica ubicada en la comuna de Graneros, Provincia del Cachapoal, Región del Libertador Bernardo O’Higgins.
La Figura 1-1 presenta la ubicación nacional, regional y local del emplazamiento de las obras del Proyecto.

Proyecto Parque Fotovoltaico Graneros
SOLEK001.INF001.Rev0

4

Estudio de inundación Estero La Cadena

Figura 1-1 Ubicación nacional, regional y local del emplazamiento de las obras del Proyecto

Fuente: Petricor Ingeniería, 2024.

Proyecto Parque Fotovoltaico Graneros
SOLEK001.INF001.Rev0

5

Estudio de inundación Estero La Cadena

2 ÁREA DE ESTUDIO

El área de estudio corresponde al sector de emplazamiento del Proyecto y sus alrededores, en particular donde se
ubica Estero La Cadena, el cual se encuentra identificado en la red hidrográfica del Instituto Geográfico Militar (IGM)
a escala 1:50.000 ubicado a 400 metros al sur del Proyecto.

Sin perjuicio de lo anterior, para la caracterización de las componentes del recurso hídrico se definió un área de
estudio que permita entender el comportamiento en un contexto local y regional, para lo cual se consideró la cuenca

del Estero La Cadena.

La Figura 2-1 presenta el área de estudio correspondiente a la cuenca del Estero La Cadena, donde además se
identifica el sector del levantamiento topográfico realizado en el Estero La Cadena, el emplazamiento de las obras
del Proyecto y la red hidrográfica IGM a escala 1:50.000.

Cabe mencionar que, de acuerdo con la delimitación oficial de la Dirección General de Aguas (DGA), el área de
estudio se encuentra dentro de la subsubcuenca del “Estero La Cadena”, que a su vez se encuentra inserta en la
subcuenca “Cachapoal Bajo”, que también a su vez se encuentra emplazado dentro de la cuenca del “Río Rapel”.

Proyecto Parque Fotovoltaico Graneros
SOLEK001.INF001.Rev0

6

Figura 2-1 Área de estudio

Fuente: Petricor Ingeniería, 2024.

Estudio de inundación Estero La Cadena

7

Proyecto Parque Fotovoltaico Graneros
SOLEK001.INF001.Rev0

Estudio de inundación Estero La Cadena

3 METODOLOGÍA

A continuación, se presenta la metodología utilizada para el estudio de crecidas consistente en un estudio
hidrológico e hidráulico del área de estudio. El estudio hidrológico tuvo el objetivo de delimitar las cuencas
hidrográficas de los cauces y determinar el caudal de crecida que pasaría según periodo de retorno, y luego, el
estudio hidráulico evaluó el comportamiento y características del flujo en las secciones a partir del levantamiento
topográfico estimando el eje hidráulico resultante para cada caudal, determinando así la superficie de inundación.

3.1 Estudio Hidrológico

El estudio hidrológico comenzó con una revisión de antecedentes de la zona de estudio, se caracterizaron y
delimitaron las cuencas hidrográficas del área de estudio, se entregaron las precipitaciones máximas en 24 hrs para
diferentes periodos de retorno, y se estimaron los caudales máximos de crecidas según periodos de retorno para la
cuenca en estudio del Estero La Cadena utilizando el método de transposición de caudales.

3.1.1 Revisión de antecedentes

Los antecedentes disponibles en la zona de estudio corresponden principalmente a estudios y datos
hidrometeorológicos de la Dirección General de Aguas (DGA) y del Instituto Geográfico Militar (IGM). A continuación,
se presentan los antecedentes recopilados:

 - Registro de series de precipitaciones máximas anuales en 24 horas de las estaciones meteorológicas
pertenecientes Banco de Aguas (BNA) [1] .

 - Registro de series de Altura y Caudal Instantáneo de las estaciones fluviométricas pertenecientes
Banco de Aguas (BNA) [1] .

 - Red de drenaje registrada por el Instituto Geográfico Militar (IGM) a escala 1:50.000.

 - Las subcuencas hidrográficas definidas en el Inventario de Cuencas Hidrográficas de la DGA [2] .

 - “Precipitaciones máximas en 1, 2 y 3 días” publicado en el año 1991 por la DGA [2] .

 - “Manual del cálculo de crecidas y caudales mínimos en cuencas sin información” publicado por la DGA

en el año 1995 [3] .

 - “Manual de Carreteras” Vol. N°2 y Vol. N°3 publicado por el MOP en el año 2023.

 - Varas, 1985. Hietogramas de Tormentas de Diseño, VII Congreso Nacional de Ingeniería Hidráulica,
Sociedad Chilena de Ingeniería Hidráulica, Concepción, Chile.

 - “Guías Metodológicas para presentación y revisión técnica de Proyectos de Modificación de cauces
naturales y artificiales” publicado en el año 2016 por la DGA.

 - “Diagnóstico de calidad de aguas Estero La Cadena, Región del Libertador Bernardo O’Higgins”
publicado por la DGA en el año 2009.

 - Estudio de Riesgo Fundado (Emanagement, 2021). Estudio de inundación del Estero La Cadena
presentado en Anexo 5 Adenda Complementaria Proyecto “Nueva Central Solar Fotovoltaica

Alameda”.

El listado de las estaciones meteorológicas y fluviométricas DGA cercanas al área de estudio se presenta en la Tabla
3-1 y Tabla 3-2, respectivamente, donde además se presenta el código DGA, sus coordenadas norte y este con Datum
WGS84 19H, altitud, cantidad de años con información, inicio y fin del registro. Por su parte, la Figura 3-1 presenta
la ubicación de las estaciones DGA que existen en el área de estudio. Cabe mencionar que, la cantidad de años con

1 [Disponible en https://dga.mop.gob.cl/servicioshidrometeorologicos/Paginas/default.aspx](https://dga.mop.gob.cl/servicioshidrometeorologicos/Paginas/default.aspx)
2 [Disponible en https://dga.mop.gob.cl/estudiospublicaciones/mapoteca/Paginas/Mapoteca](https://dga.mop.gob.cl/estudiospublicaciones/mapoteca/Paginas/Mapoteca-Digital.aspx) Digital.aspx
3 [Disponible en https://snia.mop.gob.cl/repositoriodga/handle/20.500.13000/1819](https://snia.mop.gob.cl/repositoriodga/handle/20.500.13000/1819)

Proyecto Parque Fotovoltaico Graneros
SOLEK001.INF001.Rev0

8

Estudio de inundación Estero La Cadena

información depende de la estación meteorológica, donde se destacan las estaciones Coltauco y Rancagua
(Cachapoal - DCP) que cuentan con 43 años de registro cada una, por lo que se considera información fiable para
proyección estadística.

Tabla 3-1 Listado de estaciones meteorológicas DGA

|I<br>D|Estación|Código DGA|Coordenadas UTM<br>WGS84 Huso 19H|Col5|Altitud<br>(msnm)|Inicio<br>registro|Fin<br>registro|Cantidad de años<br>con información|
|---|---|---|---|---|---|---|---|---|
|I<br>D|Estación|Código DGA|Norte (m)|Este (m)|Este (m)|Este (m)|Este (m)|Este (m)|
|1|Coltauco|06012003-K|6.204.018|308.549|253|oct-78|nov-20|43|
|2|Graneros|06011003-4|6.230.308|342.326|500|ene-79|jun-98|20|
|3|Rancagua|06010014-4|6.217.432|340.748|510|sep-71|ago-78|8|
|4|Rancagua (Cachapoal -<br>DCP)|06010015-2|6.215.289|338.657|515|oct-78|dic-20|43|
|5|Laguna Aculeo|05716005-5|6.248.925|326.369|360|nov-88|sep-21|32|
|6|Canal Sauzal en Puente<br>Termas|06008009-7|6.210.031|356.748|750|ago-05|sep-20|16|
|7|Estero de La Cadena<br>antes junta Río<br>Cachapoal|06011001-8|6.215.554|329.899|440|abr-17|nov-20|4|

Fuente: Petricor Ingeniería, 2024.

Tabla 3-2 Listado de estaciones fluviométricas DGA

|ID|Estación|Código DGA|Coordenadas UTM<br>WGS84 Huso 19H|Col5|Altitud<br>(msnm)|Inicio registro|Fin<br>registro|Cantidad de años<br>con información|
|---|---|---|---|---|---|---|---|---|
|ID|Estación|Código DGA|Norte (m)|Este (m)|Este (m)|Este (m)|Este (m)|Este (m)|
|8|Estero de La Cadena<br>antes junta Río<br>Cachapoal|06011001-8|6.215.554|329.899|598|may-83|nov-22|31|

Fuente: Petricor Ingeniería, 2024.

Proyecto Parque Fotovoltaico Graneros
SOLEK001.INF001.Rev0

9

Estudio de inundación Estero La Cadena

Figura 3-1 Ubicación estaciones meteorológicas y fluviométricas cercanas al área de estudio

Fuente: Petricor Ingeniería, 2024.

Proyecto Parque Fotovoltaico Graneros
SOLEK001.INF001.Rev0

10

Estudio de inundación Estero La Cadena

3.1.2 Caracterización hidrográfica

Para la definición de los límites de las cuencas en estudio se utilizó como base la red de cauces generada con la
cartografía IGM a escala 1:50.000, la utilización del modelo de elevación digital (DEM) Alos Palsar cuyo tamaño de
celda es de 12,5x12,5 metros y fotointerpretación de imágenes satelitales. Además, se estimaron los parámetros
morfológicos de la cuenca (área aportante, longitud del cauce principal, pendiente media del cauce, pendiente
media de la cuenca, elevación mínima, elevación media y elevación máxima) mediante herramientas
computacionales de Sistema de Información Geográfica (SIG).

3.1.3 Precipitaciones máximas

De la recopilación de antecedentes, se analizaron las series de precipitación máxima anual registradas en las
estaciones consideradas representativas de la condición temporal y espacial de la zona de estudio dada su ubicación
y cantidad de información. Se realizaron los cálculos de los estadígrafos principales de estas series (valor mínimo,
valor medio, valor máximo, desviación estándar y coeficiente de variación). Luego, se realizó un análisis de frecuencia
a la serie de precipitaciones máximas en 24 hrs anuales en base a un ajuste de distribución de probabilidad. Además,
a través del test Chi Cuadrado (significancia de 5%) se estudió la bondad del ajuste con 6 o 7 intervalos de las
distribuciones Log Normal, Pearson III, Log Pearson y Gumbel (Valores Extremos tipo I) comúnmente utilizadas en
hidrología para definir la distribución que mejor se ajusta a los registros observados y así definir la precipitación
estimada según el periodo de retorno. Cabe mencionar que, las series de precipitación máxima en 24 hrs de las
estaciones meteorológicas se presentan en el Apéndice B, y los resultados del Test Chi cuadrado y ajuste de
probabilidades de las estaciones meteorológicas se presentan en el Apéndice C.

3.1.4 Escurrimientos máximos

Los escurrimientos máximos corresponden a los escurrimientos esporádicos líquidos que puedan generarse a partir
de eventos extremos de precipitación. Para evaluar la escorrentía máxima del Estero La Cadena se utilizó el método
de transposición de caudales utilizando los datos fluviométricos registrados en estación DGA emplazada en el mismo

Estero La Cadena.

3.1.4.1 Transposición de caudales
El método de transposición de caudales consiste en estimar la escorrentía máxima en el área de estudio a partir de
información caudales medidos en una estación fluviométrica en la misma cuenca o en cuenca vecina homogénea
denominada cuenca índice. La transposición se realiza a partir de la información fluviométrica de la cuenca índice y
con la proporcionalidad del área y precipitación representativa de las cuencas de acuerdo con la siguiente ecuación:

Q 1

PP 1 ∙A 1

Q 2

=
PP 2 ∙A 2

ecuación N°1

donde Qi es el caudal de salida de la cuenca i; PPi la precipitación de 100 años de periodo de retorno, estimada a
partir del análisis de frecuencia de la precipitación máxima diaria para la cuenca i; Ai es el área de la cuenca i. Este
simple método se sustenta en que las cuencas a transponer son cercanas con un comportamiento hidrológico

similar.

La cuenca índice corresponde a la formada por la estación fluviométrica Estero La Cadena antes junta Río Cachapoal,
la cual se encuentra es el mismo Estero en evaluación y contiene a la cuenca del área de estudio. Luego, se
confeccionó la serie de caudal máximo instantáneo anual registrado en la estación fluviométrica, considerando la
totalidad de los datos, es decir, incluyendo los datos que se catalogan como “ _Caudal en Zona Extrapolada de la_
_Curva_ ”. Utilizando el método de transposición de caudales con las áreas y precipitaciones representativas de cada
cuenca, se estimó la serie de caudales máximos anuales de los últimos 31 años (1992 a 2022) para la cuenca del área

Proyecto Parque Fotovoltaico Graneros
SOLEK001.INF001.Rev0

11

Estudio de inundación Estero La Cadena

de estudio. Luego, se realizó un análisis de frecuencia a la serie de caudales máximos instantáneos anuales en base
a un ajuste de distribución de probabilidad. Además, a través del test Chi Cuadrado (significancia de 5%) se estudió
la bondad del ajuste con 7 intervalos de las distribuciones Log Normal, Pearson III, Log Pearson y Gumbel
comúnmente utilizadas en hidrología para definir la distribución que mejor se ajusta a los registros observados y así
definir el caudal estimada según el periodo de retorno. Cabe mencionar que, las series de caudales máximos
instantáneos anuales de la estación fluviométrica (cuenca índice) y los estimados para la cuenca de estudio se
presenta en el Apéndice B, y los resultados del Test Chi cuadrado y ajuste de probabilidades de la estación
fluviométrica se presenta en el Apéndice C.

3.2 Estudio Hidráulico

El estudio hidráulico determina el comportamiento y características del flujo en todas sus secciones a lo largo del
área de estudio. Para ello, se realizó una modelación hidráulica del escurrimiento superficial con el fin de estimar el
eje hidráulico o cota que alcanzaría el caudal de crecida según periodo de retorno del estudio hidrológico
considerando la topografía del Estero La Cadena. Cabe mencionar que, se realizó una visita a terreno el día 5 de
febrero de 2024 para determinar en terreno la condición actual del Estero.

A continuación, se presenta con mayor detalle la metodología aplicada en las modelaciones hidráulicas como el
_software_ de modelación, la geometría y extensión del cauce, los coeficientes de rugosidad de Manning y otras

condiciones de modelación.

3.2.1 _Software_ de modelación

Para la estimación del eje hidráulico y sus características se realizó una simulación hidráulica de los cauces del área
de estudio en el programa HEC-RAS ( _Hydrologic Engineerng Center - River Analisis System_ ) versión 6.4.1,
desarrollado por el _U.S. Army Corps of Engineer_ . Este programa estima los niveles de agua mediante un balance de
energía entre dos secciones transversales contiguas del cauce incorporando las pérdidas de energías friccionales por
medio de una ley de resistencia (Manning). El nivel de energía y los términos que la componen se presentan
esquemáticamente en la Figura 3-2.

Figura 3-2 Representación de los términos de la ecuación de energía en dos secciones

Fuente: Traducido de Manual HEC RAS 6.4.1.

Proyecto Parque Fotovoltaico Graneros
SOLEK001.INF001.Rev0

12

Estudio de inundación Estero La Cadena

De la ecuación N°2 a la ecuación N°5 participan del proceso de cálculo iterativo para estimar los valores de eje

hidráulico.

[̅]

[̅]

2

[̅]

[̅]

Ecuación de energía
2g [2] ecuación N°2

[̅]

[̅]

2

[̅]

[̅]

y 1 + z 1 + α 1 ∙ [V] [1]

[̅]

[̅]

[V] [1]

2g [+ h] [e] [= y] [2] [ + z] [2] [ + α] [2] [ ∙V] 2g [2]

[̅]

[̅]

1 1 1 2g [e] [2] [2] [2] 2g ecuación N°2

Donde:

y 1, y 2 : Profundidad del escurrimiento en las secciones 1 y 2
z 1, z 2 : Cota de fondo en las secciones 1 y 2
V 1, V 2 : Velocidad Media en las secciones 1 y 2
α 1, α 2 : Coeficiente de Coriolis en las secciones 1 y 2
g : Aceleración de gravedad
h e : Pérdidas de energía entre las secciones 1 y 2

[̅]

[̅]

2 2

[2] −α 1 V 1

[̅]

[̅]

h e
= J∙L+ C∙( [α] [2] [V] [2]

[̅]

[̅]

2

−α 1 V 1 Ecuación de pérdida de carga

2g ~~)~~ ecuación N°3

[̅]

[̅]

2

[̅]

[̅]

ecuación N°3

[̅]

[̅]

Donde:

L : Longitud de cada tramo.
J : Pendiente plano de carga.
C : Coeficiente de pérdida por expansión o contracción.

[̅]

[̅]

L= [L] [iz][q] [Q] [iz][q] [+ L] [central] [Q] [central] [+ L] [der] [Q] [der]

[̅]

[̅]

Longitud equivalente

[̅]

[̅]

Q izq + Q central + Q der ecuación N°4

Donde:

L izq −L central −L der : Longitud entre cada sección para la ribera izquierda, cauce principal y ribera derecha.
Q izq −Q central −Q der : Caudal medio aritmético entre los flujos de la ribera izquierda, cauce y ribera derecha.

[̅]

[̅]

Q izq + Q central + Q der

[̅]

[̅]

Q= [√][J]

[̅]

[̅]

Ecuación de Manning

[̅]

[̅]

n [AR]

[̅]

[̅]

2

3

[̅]

[̅]

ecuación N°5

n

Donde:
Q : Capacidad de porteo del cauce (m [3] /s)
n : Coeficiente de Manning, rugosidad del cauce
J : Pérdida de carga
A : Área hidráulica (m [2] )
R : Radio hidráulico (m)

Además, la pérdida de energía entre secciones transversales incluye las pérdidas por fricción y las pérdidas por
contracción o expansión. La altura de pérdida de energía se calcula mediante la ecuación N°6.

[̅]

[̅]

[̅] [ ∙V] [1]

2 ∙g ~~[|]~~

[̅]

Ecuación de Manning

[̅]

ecuación N°6

[̅]

∆H= L ∙S [̅]
f + C | [α] [2] 2 ∙g [ ∙V] [2]

[̅]

2

[̅]

[̅]

[2] [ ∙V] [2]

[̅] − [α] [1] [ ∙V] [1]

2 ∙g 2 ∙g

[̅]

2

[̅]

[̅]

[̅]

Donde:

C: Coeficiente de pérdida por contracción o expansión.
L: Longitud ponderada del tramo en metros.
S f [̅] : Pendiente de fricción representativa para el tramo, en metros por metro.

Proyecto Parque Fotovoltaico Graneros
SOLEK001.INF001.Rev0

[̅]

[̅]

13

Estudio de inundación Estero La Cadena

Los coeficientes de contracción y expansión se utilizan para calcular las pérdidas de energía relacionadas con los
cambios de forma de las secciones transversales en el cauce. La pérdida de energía se calcula multiplicando este
coeficiente por la diferencia absoluta entre las alturas de velocidad entre las secciones transversales.

De manera general, la sección de un cauce natural o artificial se divide en ribera izquierda, cauce principal y ribera
derecha, donde en cada una de estas subsecciones se evalúa la ley de resistencia escogida usando los respectivos
coeficientes de rugosidad de cada sección. La Figura 3-3 presenta un esquema del método usado por HEC RAS para

calcular subsecciones dentro de una sección transversal.

Figura 3-3 Esquema del método usado por HEC-RAS para calcular las subsecciones

Fuente: Manual HEC RAS 6.0.

3.2.1.1 Limitaciones HEC RAS y su corrección
Uno de los supuestos que se encuentra implícito de las expresiones analíticas es que el cauce superficial tiene
pendiente menor a 1:10. Esto se debe a que la carga de presión vertical se considera igual a la profundidad del agua
medida de forma perpendicular a la base del canal, siendo que la derivación verdadera debiera estar multiplicada
por el coseno del ángulo formado con la pendiente. Para cauces con pendientes igual o menor a 1:10, es decir
ángulos iguales o menores a 5,7°, este es un error pequeño para estimar la profundidad del flujo (cos(5,7°)=0,995).

Sobre cauces con pendientes mayores a 1:10 se necesitaría corregir la profundidad del flujo dividiendo por el coseno
del ángulo formado por la pendiente, tal como se presenta en la ecuación N°7.

d ecuación N°7
D=
cos(θ)

Donde,
D: Profundidad vertical corregida
d: Profundidad vertical estimada por HEC RAS
θ: pendiente del cauce modelado expresado en grados (°).

En el caso particular del Proyecto, cabe mencionar que la pendiente del Estero La Cadena en el tramo de estudio es
del orden de 0,2%, que es menor al límite de 10%, por lo que no es necesaria la corrección por alta pendiente.

Proyecto Parque Fotovoltaico Graneros
SOLEK001.INF001.Rev0

14

Estudio de inundación Estero La Cadena

3.2.2 Geometría y extensión del cauce

La geometría de los cauces se generó utilizando el complemento HEC-GeoRAS para ArcGIS con las curvas de nivel
cada 0,2 metros. Las curvas de nivel se obtuvieron a partir del Estudio Topográfico presentado en el Apéndice AEstudio Topográfico. Luego, se generaron los perfiles transversales a lo largo del Estero La Cadena tomando en
consideración los puntos tomados en terreno para una mayor representatividad. Se destaca que, los perfiles
transversales se trazaron cada 20 m aproximadamente.

Por otro lado, la extensión de la modelación abarcó un tramo de 950 m aproximadamente, donde se respeta un
tramo mínimo de 100 m aguas arriba y 100 m aguas abajo respecto a un control hidráulico. Además, cabe mencionar
que se utilizó la función “ _leeves_ ” para definir los bordes de los cauces superficiales y para direccionar el flujo de agua
entre por ciertos sectores dentro del perfil transversal.

La Figura 3-4 presenta un resumen de la vista en planta de la ubicación de los perfiles transversales trazados a lo
largo del Estero La Cadena.

Proyecto Parque Fotovoltaico Graneros
SOLEK001.INF001.Rev0

15

Estudio de inundación Estero La Cadena

Figura 3-4 Resumen vista en planta de perfiles transversales generados en HEC-GeoRAS en cauces estudiados

Fuente: Petricor Ingeniería, 2024.

Proyecto Parque Fotovoltaico Graneros
SOLEK001.INF001.Rev0

16

Estudio de inundación Estero La Cadena

3.2.3 Coeficiente de Manning

El coeficiente de Manning del estero en estudio se estimó utilizando el método de Cowan, recomendado en el
Manual de Carreteras Volumen N°3. La Ecuación N°8 muestra la expresión para determinar el coeficiente de
Manning (n), mientras que la Tabla 3-3 presenta el valor estimativo de cada índice según las características del cauce.

n= m∙(n 0 + n 1 + n 2 + n 3 + n 4 +) Ecuación N°8

Tabla 3-3 Estimación del coeficiente de Manning según método de Cowan

Fuente: Manual de Carreteras Volumen N°3, MOP 2022.

El coeficiente de Manning se estimó en 0,065 (-) para los bordes y 0,035 (-) para el centro del cauce del Estero Las
Cadenas. Este valor fue estimado a partir de los siguientes criterios de selección según el método de Cowan:

 - Lecho: Centro de tierra n0= 0,02 y borde de tierra n0 = 0,02

 - Grado de irregularidad: Centro Leve n1= 0,005 y borde Leve n1 = 0,005

 - Variaciones de la sección: Centro Graduales n2= 0 y borde Graduales n2 = 0

 - En lo relativo de las obstrucciones: Centro Despreciable n3= 0 y borde Leve n3 = 0,012

 - Vegetación: Centro Baja a Media n4= 0,01 y borde Media a Alta n4 = 0,025

 - Grado de meandros; Centro leve m= 1 y borde Leve m = 1

La Figura 3-5 muestra las fotografías del Estero La Cadena a la altura del cruce con la carretera Ex 5 Sur, indicando
además con una flecha blanca el sentido de escurrimiento del flujo. Se destaca que, las fotografías fueron tomadas

en una visita a terreno realizada el día 5 de febrero de 2024.

Proyecto Parque Fotovoltaico Graneros
SOLEK001.INF001.Rev0

17

(a)

Estudio de inundación Estero La Cadena

Figura 3-5 Fotografías Estero La Cadena

(b)

Fuente: Petricor Ingeniería, 2024.

3.2.4 Obra de cruce: Puente Ruta Ex 5 Sur

La modelación hidráulica incluyó la obra de cruce o atravieso correspondiente al puente de la Ex Ruta 5 Sur que
cruza el Estero La Cadena, el cual permite el libre escurrimiento de las aguas y del flujo vehicular.

Se levantó en terreno las dimensiones de las pilas del puente que se encuentran en el lecho del cauce, junto con
levantar la información topográfica referida a las cotas del borde superior e inferior de la viga del puente. Cabe
mencionar que, la obra de cruce se encuentra entre los perfiles transversales PT153 y PT118.

La Figura 3-6 a) presenta una fotografía de las pilas del puente, mientras que la Figura 3-6 b) presenta una vista
esquemática del puente utilizada en Hec-Ras para la modelación hidráulica.

Proyecto Parque Fotovoltaico Graneros
SOLEK001.INF001.Rev0

18

Estudio de inundación Estero La Cadena

Figura 3-6 Fotografías del Puente Ruta Ex 5 Sur y Estero La Cadena (a) y su vista esquemática en Hec-Ras (b)

(b)

(a)

Fuente: Petricor Ingeniería, 2024.

3.2.5 Escenarios y condiciones de modelación

El escenario de modelación corresponde a las situación existente o natural del Estero La Cadena, es decir, se
representa el cauce en su forma original.

La modelación hidráulica se realizó en régimen permanente y en 1 dimensión, para los caudales de crecidas según
los periodos de retorno de 5, 10, 25, 50 y 100 años. Se destaca que, el caudal que define la superficie de cauce es el
caudal con un periodo de retorno de 100 años estimado según Estudio Hidrológico en 72 m [3] /s. El resto de los
caudales de crecidas se presentan en la Tabla 4-7.

<!-- INICIO TABLA 4-7 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- 25 Estudio de inundación Estero La Cadena -->

**Tabla 4-7: Caudales máximos instantáneos según periodo de retorno método Transposición de caudales**

| T<br>(años) | Cuenca en estudio |
| --- | --- |
| T <br>(años) | Dist LogNormal (m3/s) |
| 5 | 22,8 |
| 10 | 31,4 |
| 25 | 45,6 |
| 50 | 58,0 |
| 100 | 72,0 |

<!-- Estadísticas: 6 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Petricor Ingeniería, 2024. La Figura 4-3 presenta el ajuste de la distribución LogNormal a la serie de caudales máximos instantáneos anuales estimada para la cuenca en estudio. -->
<!-- FIN TABLA 4-7 -->


Las condiciones de borde se asumen tanto para aguas arriba como para aguas abajo, una altura de agua normal con
una pendiente igual a la determinada según las primeras o últimas cuatro secciones del cauce, de manera que el
programa simule el flujo en un régimen mixto (subcrítico o supercrítico). La pendiente de altura normal estimada
como condición de borde aguas arriba corresponde a 0,42% y como condición de borde aguas abajo corresponde a
0,53%.

Proyecto Parque Fotovoltaico Graneros
SOLEK001.INF001.Rev0

19

Estudio de inundación Estero La Cadena

4 RESULTADOS

4.1.1 Caracterización hidrográfica

La cuenca hidrográfica del área de estudio corresponde a la cuenca del Estero La Cadena. Esta cuenca abarca desde
el sector geomorfológico precordillera, abarcando el sector de depresión intermedia denominado Cuenca Rancagua,
e incluye también parte de la cordillera de la costa, donde ésta última obliga al cauce a modificar de sentido de oeste
a este del cauce a un sentido de norte a sur hasta confluir sus aguas con el Río Cachapoal. Además, se destaca que
el Estero La Cadena se encuentra identificado en la cartografía del Instituto Geográfico Militar (IGM) a escala

1:50.000 como “Estero”.

En el sector precordillerano de los Andes de la cuenca del Estero La Cadena se originan una serie de quebradas (El
Naranjillo, Macal, del Manzano, Agua del Estero, Mal Potrerillos, entre otras) que confluyen a 2 cauces superficiales.
El primero corresponde al Estero Leonera que recoge las aguas al noreste de la cuenca, y el segundo es el Estero
Machalí que recibe las aguas de las quebradas ubicadas al sureste. Ambos esteros confluyen a la altura de Rancagua
al norte originando lo que es el Estero La Cadena, el que luego de 500 metros hacia aguas abajo se ubica el área de
estudio. El Estero La Cadena recorre aproximadamente 12 km de este a oeste, hasta que se encuentra con la
cordillera de la costa que lo obliga a cambiar de sentido norte a sur, donde recorre 9 km más hasta su confluencia
con el Río Cachapoal.

Respecto a la delimitación oficial de la DGA, el área de estudio se encuentra dentro de la subsubcuenca del Estero
La Cadena, que a su vez se encuentra inserta en la subcuenca Cachapoal Bajo, que también a su vez se encuentra
inserto dentro de la cuenca del Río Rapel. La cuenca del Estero La Cadena delimita al este con la cuenca del Estero
Coya, al norte con la cuenca del Estero Angostura y al sur con la cuenca del Río Cachapoal. De acuerdo con el Estudio
“Diagnóstico de calidad de aguas Estero La Cadena, Región del Libertador Bernardo O’Higgins” publicado por la DGA
en el año 2009, el sistema hídrico presenta descargas de plantas de tratamiento de aguas servidas y aportes difusos
de agroindustrias. Además, el régimen hidrológico del Estero La Cadena presenta un comportamiento nivo-pluvial,
ya que presenta los máximos caudales de escurrimiento en los meses de deshielo (noviembre - febrero), llegando a
un caudal medio cercano a los 17 m [3] /s, y en menor magnitud presenta un máximo de caudales durante el periodo
de lluvias, principalmente en el mes de junio, durante el cual se presenta un caudal medio en torno a los 12 m [3] /s.

La Figura 4-1 muestra la delimitación de la cuenca aportante al área de estudio, donde además se presenta la cuenca
índice correspondiente a la misma cuenca del Estero la Cadena que se origina a partir de la ubicación de la estación
fluviométrica DGA ubicada antes de la desembocadura en el Río Cachapoal y la delimitación oficial de la DGA.
Además, la Tabla 4-1 presenta los parámetros geomorfológicos de las cuencas delimitadas para el estudio. Cabe
mencionar que, a modo de criterio conservador, el área pluvial es considerado igual al área total de la cuenca.

Tabla 4-1 Características geomorfológicas de las cuencas estudiadas

|c|Cauce|Área (km2)|Elevación<br>media<br>(msnm)|Elevación<br>mínima<br>(msnm)|Elevación<br>máxima<br>(msnm)|Largo del<br>cauce<br>(km)|Pendiente<br>media del cauce<br>(%)|
|---|---|---|---|---|---|---|---|
|1|Cuenca área estudio<br>Estero La Cadena<br>a la altura del Proyecto|165,86|827,7|494|1.991|17,6|2,28|
|2|Cuenca índice<br>Estero La Cadena<br>a la altura de la<br>estación fluviométrica|509,06|731,5|466|2.116|37,8|1,19|

Fuente: Petricor Ingeniería, 2024.

Proyecto Parque Fotovoltaico Graneros
SOLEK001.INF001.Rev0

20

Figura 4-1 Delimitación de cuencas hidrográficas del Estero La Cadena

Fuente: Petricor Ingeniería, 2024.

Estudio de inundación Estero La Cadena

21

Proyecto Parque Fotovoltaico Graneros
SOLEK001.INF001.Rev0

Estudio de inundación Estero La Cadena

4.2 Precipitaciones máximas

Las precipitaciones máximas en 24 horas se obtuvieron de las estaciones 1) Coltauco, 2) Graneros, 3) Rancagua, 4)
Rancagua (Cachapoal - DCP), 5) Laguna Aculeo, 6) Canal Sauzal en Puente Termas y 7) Estero de La Cadena antes
junta Río Cachapoal considerando que se ubican en zonas próximas a los cauces en estudio. Los estadígrafos
principales de la serie de precipitación máxima en 24 horas anual (valor mínimo, valor medio, valor máximo,
desviación estándar y coeficiente de variación) se presentan en la Tabla 4-2, donde se destaca que la estación Laguna
Aculeo, Coltauco y Graneros presentan los mayores registros de precipitación máxima en 24 horas con 170 mm, 161
mm y 137,4 mm, respectivamente. Además, la estación Estero de la Cadena antes junta Río Cachapoal la máxima
precipitación que registró en 24 horas fue de sólo 32,2 mm, lo que se debe al escaso registro histórico de sólo 4
años. Las estaciones meteorológicas con mayor registro histórico corresponden a la estación Rancagua (Cachapoal
- DCP) y a la estación Coltauco con 43 años con información cada una, por lo que se consideran representativas de
la condición hidrometeorológica del área de estudio. Las series de precipitación máxima en 24 hrs de las estaciones
meteorológicas se presentan en el Apéndice B.

Tabla 4-2 Principales estadígrafos de precipitaciones máximas anuales en 24 horas

|ID|Estación|Años con<br>información|Mínimo<br>(mm)|Media<br>(mm)|Máximo<br>(mm)|Desv. Estándar<br>(mm)|Coef. Variación<br>(-)|
|---|---|---|---|---|---|---|---|
|1|Coltauco|43|29,7|85,9|161|36,8|0,43|
|2|Graneros|20|25,8|68,3|137,4|27,5|0,40|
|3|Rancagua|8|12|45,0|80|18,7|0,41|
|4|Rancagua (Cachapoal - DCP)|43|16|50,5|100|19,8|0,39|
|5|Laguna Aculeo|32|7,5|69,9|170|38,2|0,55|
|6|Canal Sauzal en Puente Termas|16|17,5|59,1|94,4|22,9|0,39|
|7|Estero de La Cadena antes<br>junta Río Cachapoal|4|18,3|24,4|32,2|6,2|0,26|

Fuente: Petricor Ingeniería, 2024.

Además, se analizó la frecuencia de la serie anual de precipitaciones máximas en 24 hrs registrados en las estaciones
meteorológicas en base a un ajuste de distribución de probabilidad. A través del test Chi Cuadrado (significancia de
5%) se estudió la bondad del ajuste con 6 o 7 intervalos de las distribuciones Log Normal, Pearson III, Log Pearson y
Gumbel (Valores Extremos tipo I). De los resultados obtenidos presentados en la Tabla 4-3, se destacó que todas las
distribuciones fueron aceptadas modificando el número de intervalos.

Tabla 4-3 Resultados Test Chi Cuadrado para bondad de ajuste a series de precipitación según estación

|Col1|meteorológica|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|Distribución|Estaciones DGA|Estaciones DGA|Estaciones DGA|Estaciones DGA|Estaciones DGA|Estaciones DGA|
|Distribución|Coltauco|Graneros|Rancagua|Rancagua<br>(Cachapoal -<br>DCP)|Laguna Aculeo|Canal Sauzal<br>en Puente<br>Termas|
|Log-Normal|Aceptado|Aceptado|Aceptado|Aceptado|Aceptado|Aceptado|
|Pearson III|Aceptado|Aceptado|Aceptado|Aceptado|Aceptado|Aceptado|
|Log Pearson|Aceptado|Aceptado|Aceptado|Aceptado|Aceptado|Aceptado|
|Gumbel|Aceptado|Aceptado|Aceptado|Aceptado|Aceptado|Aceptado|

Fuente: Petricor Ingeniería, 2024.

Proyecto Parque Fotovoltaico Graneros
SOLEK001.INF001.Rev0

22

Estudio de inundación Estero La Cadena

El análisis de frecuencia da como resultado las precipitaciones máximas en 24 hrs para distintos períodos de retorno.
Los resultados indicaron que, en la estación Graneros la distribución Gumbel estimó los valores de precipitación
máxima en 24 horas para un periodo de retorno de 100 años más conservadores (más altos), y en el resto de las
estaciones fue la distribución LogNormal. La Tabla 4-4 presenta los valores de precipitación máxima en 24 horas
según periodo de retorno del ajuste de la distribución de probabilidades utilizando la distribución más conservadora
según el caso de cada estación. Los resultados del Test Chi cuadrado y ajuste de probabilidades de las estaciones
meteorológicas se presentan en el Apéndice C.

Tabla 4-4 Precipitación máxima en 24 hrs según periodo de retorno y estación meteorológica (mm)

|T<br>(años)|Coltauco|Graneros|Rancagua|Rancagua<br>(Cachapoal - DCP)|Laguna Aculeo|Canal Sauzal en<br>Puente Termas|
|---|---|---|---|---|---|---|
|T <br>(años)|Dist LogNormal<br>(mm)|Dist Gumbel<br>(mm)|Dist LogNormal<br>(mm)|Dist LogNormal<br>(mm)|Dist LogNormal<br>(mm)|Dist LogNormal (mm)|
|5|116,7|95,2|65,3|67,6|102,7|82,2|
|10|140,6|113,1|81,3|80,3|132,1|99,8|
|25|174,5|137,7|104,9|98,1|176,9|125,1|
|50|200,6|155,9|123,6|111,6|213,6|144,8|
|100|227,4|174,0|143,3|125,3|253,1|165,1|

Fuente: Petricor Ingeniería, 2024.

De los resultados obtenidos, se observó que el rango de valores para precipitaciones de 100 años en 24 horas es
entre 125 mm y 253 mm, donde los máximos valores corresponden a las estaciones Laguna Aculeo y Coltauco,
debido probablemente a la influencia de la cordillera de la costa. No obstante, en la depresión intermedia y
precordillera los valores para precipitaciones de 100 años se encuentran en torno a los 170 mm en 24 horas. La
Figura 4-2 presenta los resultados de precipitación máxima obtenidos en un mapa junto con las isoyetas de
precipitación máxima diaria (DGA, 1991) comparables con un periodo de retorno de 10 años, de lo cual se observa
que las precipitaciones máximas estimadas en la estación Coltauco y Graneros son valores conservadores para la

zona de estudio.

Se consideró que la precipitación representativa de las cuencas en estudio corresponde a la estimada por la estación
Graneros debido a que es la más cercana al área de estudio, y que, además, muestra resultados conservadores
respecto a las isoyetas de precipitación máxima estimadas en (DGA, 1991). La precipitación de 100 años de periodo
de retorno representativa del área de estudio es 174 mm y la precipitación de 10 años de periodo de retorno es de

113,1 mm.

Proyecto Parque Fotovoltaico Graneros
SOLEK001.INF001.Rev0

23

Estudio de inundación Estero La Cadena

Figura 4-2 Resultados precipitaciones máximas en 24 horas en mapa según estación (T=10 años)

Fuente: Petricor Ingeniería, 2024.

Proyecto Parque Fotovoltaico Graneros
SOLEK001.INF001.Rev0

24

Estudio de inundación Estero La Cadena

4.3 Escorrentía máxima

El método de transposición de caudales fue utilizado para evaluar la escorrentía según periodo de retorno del Estero
La Cadena, para lo cual se consideraron los registros de la estación fluviométrica DGA Estero de La Cadena antes
junta Río Cachapoal que forma la cuenca índice. Con esta información, se generó la serie de caudales máximos
instantáneos para los último 31 años de registro en la estación fluviométrica.

El área de la cuenca índice es 509,1 km [2], mientras que el área de la cuenca en estudio es de 165,86 km [2], con lo cual
es posible efectuar la relación entre áreas. En el caso de la precipitación representativa de las cuencas, se consideró
que para ambas cuencas es la misma, ya que la cuenca índice contiene a la cuenca en estudio.

Con los antecedentes anteriores, se utilizó la fórmula del método de transposición de caudales con lo que se obtuvo
la serie de caudales máximos anuales transpuesto representativo de la cuenca en estudio. La Tabla 4-5 presenta los
estadígrafos principales (valor mínimo, valor medio, valor máximo, desviación estándar y coeficiente de variación)
de la serie de caudales máximas anuales de la cuenca índice formada por la estación fluviométrica DGA y de la serie
de caudales máximos anuales de la cuenca en estudio estimados a partir del método de transposición de caudales.

Tabla 4-5 Principales estadígrafos de series caudales máximos instantáneos anuales según cuenca

|Cuenca|Años con<br>información|Mínimo<br>(m3/s)|Media<br>(m3/s)|Máximo<br>(m3/s)|Desv. Estándar<br>(m3/s)|Coef. Variación<br>(-)|
|---|---|---|---|---|---|---|
|Cuenca índice<br>a la altura estación fluviométrica|31|9,0|47,76|158,67|41,0|0,9|
|Cuenca en estudio*<br>a la altura del Proyecto|31|2,93|15,56|51,7|13,3|0,9|

*: Estos datos fueron estimados a partir de la cuenca índice y transponiendo caudales

Fuente: Petricor Ingeniería, 20247.

Además, se analizó la frecuencia de la serie de caudales máximos anuales de la cuenca en estudio en base a un ajuste
de distribución de probabilidad. A través del test Chi Cuadrado (significancia de 5%) se estudió la bondad del ajuste
con 7 intervalos de las distribuciones Log Normal, Pearson III, Log Pearson y Gumbel (Valores Extremos tipo I). De
los resultados obtenidos presentados en la Tabla 4-6, se destaca que se aprobó el test para todas las distribuciones,
excepto para la distribución Log-Pearson.

Tabla 4-6 Resultados Test Chi Cuadrado para bondad de ajuste a serie de caudales máximos instantáneos

|Distribución|Serie caudales máximos instantáneos Cuenca en estudio|
|---|---|
|Log-Normal|Aceptado|
|Pearson III|Aceptado|
|Log Pearson|Rechazado|
|Gumbel|Aceptado|

Fuente: Petricor Ingeniería, 2024.

El análisis de frecuencia da como resultado los caudales máximos instantáneos para distintos períodos de retorno
de la cuenca de estudio. Los resultados indicaron que, los valores más altos de escurrimientos máximos los entrega
la distribución de probabilidades LogNormal. La Tabla 4-7 presenta los valores de caudal máximo instantáneo según
periodo de retorno utilizando la distribución de probabilidades más conservadora. Los resultados del Test Chi
cuadrado y ajuste de probabilidades de la estación fluviométrica se presentan en el Apéndice C.

Proyecto Parque Fotovoltaico Graneros
SOLEK001.INF001.Rev0

25

Estudio de inundación Estero La Cadena

Tabla 4-7 Caudales máximos instantáneos según periodo de retorno método Transposición de caudales

|T<br>(años)|Cuenca en estudio|
|---|---|
|T <br>(años)|Dist LogNormal (m3/s)|
|5|22,8|
|10|31,4|
|25|45,6|
|50|58,0|
|100|72,0|

Fuente: Petricor Ingeniería, 2024.

La Figura 4-3 presenta el ajuste de la distribución LogNormal a la serie de caudales máximos instantáneos anuales
estimada para la cuenca en estudio.

Figura 4-3 Ajuste distribución LogNormal a serie de caudales máximos instantáneos anuales cuenca en estudio

Fuente: Petricor Ingeniería, 2024.

De los resultados obtenidos, se consideró que el método de Transposición de caudales entrega un caudal de crecida
representativo del área de estudio, por lo que se determinó que el caudal de crecidas para un periodo de retorno
de 100 años corresponde a 72,0 m [3] /s.

Cabe mencionar que, en el estudio Riesgo Fundado (Emanagement, 2021) presentado en el Apéndice F, se realizó
un estudio de inundación en el mismo tramo del Estero La Cadena, para lo cual también se realizó una estimación
de los caudales máximos de crecidas a partir del método de Transposición de Caudales utilizando la información
registrada en la estación fluviométrica DGA Estero de La Cadena antes junta Río Cachapoal. En este estudio del año
2021 se estimó que el caudal de crecida para 100 años de periodo de retorno a la cuenca en estudio corresponde a
56,8 m [3] /s, lo cual es menor al caudal de crecida de 100 años estimado en el presente estudio.

Proyecto Parque Fotovoltaico Graneros
SOLEK001.INF001.Rev0

26

Estudio de inundación Estero La Cadena

4.4 Modelación hidráulica

La modelación hidráulica determinó el comportamiento y características del flujo en todas sus secciones a lo largo
del Estero La Cadena considerando el caudal de crecidas con un periodo de retorno de 5, 10, 25, 50 y 100 años y la
geometría de los cauces obtenida a partir de las curvas de nivel obtenidas del Estudio Topográfico presentado en el
Apéndice A. Se destaca que, los archivos digitales de cartografía y modelación HEC RAS según periodo de retorno se
presentan en el Apéndice D, y los resultados numéricos de la modelación hidráulica según periodo de retorno del
cauce se presentan en el Apéndice E.

La Figura 4-4 presenta los resultados obtenidos de la simulación hidráulica para el caudal de crecidas de 100 años
de periodo de retorno en distintas secciones transversales a lo largo del Estero La Cadena, PT977 (a), PT752 (b),
PT407 (c) y PT118 (d). Además, la Figura 4-5 presenta el perfil longitudinal modelado del tramo del Estero para el

caudal de crecida.

Figura 4-4 Resultados eje hidráulico en distintas secciones transversales del Estero La Cadena

(a) PT977

(b) PT752

(c) PT407 (d) PT118 Aguas abajo obracruce
Fuente: Petricor Ingeniería, 2024.

Proyecto Parque Fotovoltaico Graneros
SOLEK001.INF001.Rev0

27

Estudio de inundación Estero La Cadena

Figura 4-5 Resultados eje hidráulico en perfil longitudinal, Estero La Cadena

Fuente: Petricor Ingeniería, 2024.

Además, se obtuvo la superficie de inundación del Estero La Cadena para los caudales de crecida de 5, 10, 25, 50 y
100 años de periodo de retorno. La Figura 4-6 presenta el área de inundación del Estero La Cadena junto con la
profundidad estimada para la crecida de 100 años de periodo de retorno obtenida para el área de estudio.

De los resultados de la modelación hidráulica, se destacó que el flujo de agua se mantiene mayoritariamente dentro
del encajonamiento de los bordes del Estero, sin afectar la zona de emplazamiento del Proyecto.

Proyecto Parque Fotovoltaico Graneros
SOLEK001.INF001.Rev0

28

Estudio de inundación Estero La Cadena

29

Figura 4-6 Superficie de inundación Estero La Cadena para crecida (T=100 años)

Fuente: Petricor Ingeniería, 2024.

Proyecto Parque Fotovoltaico Graneros
SOLEK001.INF001.Rev0

Estudio de inundación Estero La Cadena

5 CONCLUSIONES

El estudio realizado y presentado en este documento tuvo por objetivo el levantamiento de información, Hidrológica
e Hidráulica necesaria que permita determinar el área de inundación a 100 años de periodo de retorno del Estero
La Cadena ubicado al menos 400 metros al sur de las obras del Proyecto (sector paneles fotovoltaicos), con la
finalidad de esclarecer la superficie de drenaje del sector de estudio para un evento de crecida y su relación con el
emplazamiento del Proyecto.

El caudal de crecida según periodos de retorno para el Estero La Cadena en el tramo de estudio se estimó en base
al método de Transposición de caudales utilizando los datos de la estación fluviométrica DGA Estero Las Cadenas
antes junta Río Cachapoal. Esta estación fluviométrica DGA registra los valores de caudal del mismo Estero Las
Cadenas en estudio, pero se encuentra emplazada aguas abajo del tramo de Estero en estudio. El caudal de crecida
para 100 años de periodo de retorno se estimó en 72 m [3] /s, el cual es mayor al caudal estimado por Emanagement,
2021, de 56,8 m [3] /s, en el mismo tramo del Estero La Cadena.

Por otro lado, los resultados del estudio hidráulico determinaron las características del escurrimiento para cada
sección transversal del flujo mediante simulación hidráulica, estimando así la superficie de inundación del Estero La
Cadena según periodo de retorno. Se destacó que, dentro de la modelación hidráulica se consideró la rugosidad de
Manning en base al método de Cowan, y se incluyó la obra de cruce correspondiente al puente de la ruta Ex 5 Sur
que cruza al estero La Cadena debido al posible control hidráulico que pueda ejercer en el cauce.

Finalmente, se concluyó que superficie de inundación se encuentra limitada o encajonada en la sección del cauce
dentro de los bordes del Estero Las Cadenas, sin afectar la zona de emplazamiento de paneles fotovoltaicos. Se
destacó que, los resultados obtenidos se consideraron representativos del área de estudio debido a que cálculos
fueron elaborados de acuerdo con las recomendaciones presentadas en “Guías Metodológicas para presentación y
revisión técnica de Proyectos de Modificación de cauces naturales y artificiales” (DGA, 2016).

Proyecto Parque Fotovoltaico Graneros
SOLEK001.INF001.Rev0

30

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 3-1: Listado de estaciones meteorológicas DGA**

| I<br>D | Estación | Código DGA | Coordenadas UTM<br>WGS84 Huso 19H | Col5 | Altitud<br>(msnm) | Inicio<br>registro | Fin<br>registro | Cantidad de años<br>con información |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| I<br>D | Estación | Código DGA | Norte (m) | Este (m) | Este (m) | Este (m) | Este (m) | Este (m) |
| 1 | Coltauco | 06012003-K | 6.204.018 | 308.549 | 253 | oct-78 | nov-20 | 43 |
| 2 | Graneros | 06011003-4 | 6.230.308 | 342.326 | 500 | ene-79 | jun-98 | 20 |
| 3 | Rancagua | 06010014-4 | 6.217.432 | 340.748 | 510 | sep-71 | ago-78 | 8 |
| 4 | Rancagua (Cachapoal -<br>DCP) | 06010015-2 | 6.215.289 | 338.657 | 515 | oct-78 | dic-20 | 43 |
| 5 | Laguna Aculeo | 05716005-5 | 6.248.925 | 326.369 | 360 | nov-88 | sep-21 | 32 |
| 6 | Canal Sauzal en Puente<br>Termas | 06008009-7 | 6.210.031 | 356.748 | 750 | ago-05 | sep-20 | 16 |
| 7 | Estero de La Cadena<br>antes junta Río<br>Cachapoal | 06011001-8 | 6.215.554 | 329.899 | 440 | abr-17 | nov-20 | 4 |

**Tabla 3-2: Listado de estaciones fluviométricas DGA**

| ID | Estación | Código DGA | Coordenadas UTM<br>WGS84 Huso 19H | Col5 | Altitud<br>(msnm) | Inicio registro | Fin<br>registro | Cantidad de años<br>con información |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ID | Estación | Código DGA | Norte (m) | Este (m) | Este (m) | Este (m) | Este (m) | Este (m) |
| 8 | Estero de La Cadena<br>antes junta Río<br>Cachapoal | 06011001-8 | 6.215.554 | 329.899 | 598 | may-83 | nov-22 | 31 |

**Tabla 4-1: Características geomorfológicas de las cuencas estudiadas**

| c | Cauce | Área (km2) | Elevación<br>media<br>(msnm) | Elevación<br>mínima<br>(msnm) | Elevación<br>máxima<br>(msnm) | Largo del<br>cauce<br>(km) | Pendiente<br>media del cauce<br>(%) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Cuenca área estudio<br>Estero La Cadena<br>a la altura del Proyecto | 165,86 | 827,7 | 494 | 1.991 | 17,6 | 2,28 |
| 2 | Cuenca índice<br>Estero La Cadena<br>a la altura de la<br>estación fluviométrica | 509,06 | 731,5 | 466 | 2.116 | 37,8 | 1,19 |

**Tabla 4-2: Principales estadígrafos de precipitaciones máximas anuales en 24 horas**

| ID | Estación | Años con<br>información | Mínimo<br>(mm) | Media<br>(mm) | Máximo<br>(mm) | Desv. Estándar<br>(mm) | Coef. Variación<br>(-) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Coltauco | 43 | 29,7 | 85,9 | 161 | 36,8 | 0,43 |
| 2 | Graneros | 20 | 25,8 | 68,3 | 137,4 | 27,5 | 0,40 |
| 3 | Rancagua | 8 | 12 | 45,0 | 80 | 18,7 | 0,41 |
| 4 | Rancagua (Cachapoal - DCP) | 43 | 16 | 50,5 | 100 | 19,8 | 0,39 |
| 5 | Laguna Aculeo | 32 | 7,5 | 69,9 | 170 | 38,2 | 0,55 |
| 6 | Canal Sauzal en Puente Termas | 16 | 17,5 | 59,1 | 94,4 | 22,9 | 0,39 |
| 7 | Estero de La Cadena antes<br>junta Río Cachapoal | 4 | 18,3 | 24,4 | 32,2 | 6,2 | 0,26 |

**Tabla 4-3: Resultados Test Chi Cuadrado para bondad de ajuste a series de precipitación según estación**

| Col1 | meteorológica | Col3 | Col4 | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Distribución | Estaciones DGA | Estaciones DGA | Estaciones DGA | Estaciones DGA | Estaciones DGA | Estaciones DGA |
| Distribución | Coltauco | Graneros | Rancagua | Rancagua<br>(Cachapoal -<br>DCP) | Laguna Aculeo | Canal Sauzal<br>en Puente<br>Termas |
| Log-Normal | Aceptado | Aceptado | Aceptado | Aceptado | Aceptado | Aceptado |
| Pearson III | Aceptado | Aceptado | Aceptado | Aceptado | Aceptado | Aceptado |
| Log Pearson | Aceptado | Aceptado | Aceptado | Aceptado | Aceptado | Aceptado |
| Gumbel | Aceptado | Aceptado | Aceptado | Aceptado | Aceptado | Aceptado |

**Tabla 4-4: Precipitación máxima en 24 hrs según periodo de retorno y estación meteorológica (mm)**

| T<br>(años) | Coltauco | Graneros | Rancagua | Rancagua<br>(Cachapoal - DCP) | Laguna Aculeo | Canal Sauzal en<br>Puente Termas |
| --- | --- | --- | --- | --- | --- | --- |
| T <br>(años) | Dist LogNormal<br>(mm) | Dist Gumbel<br>(mm) | Dist LogNormal<br>(mm) | Dist LogNormal<br>(mm) | Dist LogNormal<br>(mm) | Dist LogNormal (mm) |
| 5 | 116,7 | 95,2 | 65,3 | 67,6 | 102,7 | 82,2 |
| 10 | 140,6 | 113,1 | 81,3 | 80,3 | 132,1 | 99,8 |
| 25 | 174,5 | 137,7 | 104,9 | 98,1 | 176,9 | 125,1 |
| 50 | 200,6 | 155,9 | 123,6 | 111,6 | 213,6 | 144,8 |
| 100 | 227,4 | 174,0 | 143,3 | 125,3 | 253,1 | 165,1 |

**Tabla 4-5: Principales estadígrafos de series caudales máximos instantáneos anuales según cuenca**

| Cuenca | Años con<br>información | Mínimo<br>(m3/s) | Media<br>(m3/s) | Máximo<br>(m3/s) | Desv. Estándar<br>(m3/s) | Coef. Variación<br>(-) |
| --- | --- | --- | --- | --- | --- | --- |
| Cuenca índice<br>a la altura estación fluviométrica | 31 | 9,0 | 47,76 | 158,67 | 41,0 | 0,9 |
| Cuenca en estudio*<br>a la altura del Proyecto | 31 | 2,93 | 15,56 | 51,7 | 13,3 | 0,9 |

**Tabla 4-6: Resultados Test Chi Cuadrado para bondad de ajuste a serie de caudales máximos instantáneos**

| Distribución | Serie caudales máximos instantáneos Cuenca en estudio |
| --- | --- |
| Log-Normal | Aceptado |
| Pearson III | Aceptado |
| Log Pearson | Rechazado |
| Gumbel | Aceptado |
