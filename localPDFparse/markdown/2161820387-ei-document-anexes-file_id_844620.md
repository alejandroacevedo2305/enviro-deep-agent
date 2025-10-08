---
title: Título del Documento
author: Ignacio Jaque Vidal
date: D:20240216025129-03'00'
language: es
type: manual
pages: 30
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Proyecto PFV Los Lagos
-->

## Anexo N°2.7.1 Estudio de crecidas Estero Cuni

# Proyecto PFV Los Lagos

Preparado para IM2Solar
Código de documento: IM2SOLAR003.INF003.Rev0

Enero, 2024

Anexo N°2.7.1 Estudio de crecidas Estero Cuni

ÍNDICE DE CONTENIDO

1 INTRODUCCIÓN ..................................................................................................................................3

2 ÁREA DE ESTUDIO ...............................................................................................................................5

3 METODOLOGÍA ...................................................................................................................................7

3.1 Estudio Hidrológico ...................................................................................................................................... 7

3.1.1 Revisión de antecedentes .................................................................................................................................... 7

3.1.2 Caracterización hidrográfica ................................................................................................................................ 8
3.1.3 Precipitaciones máximas ...................................................................................................................................... 8

3.1.4 Escurrimientos máximos .................................................................................................................................... 10

3.2 Estudio Hidráulico ...................................................................................................................................... 13

3.2.1 _Software_ de modelación..................................................................................................................................... 13
3.2.2 Geometría y extensión del cauce....................................................................................................................... 15
3.2.3 Coeficiente de Manning ..................................................................................................................................... 17

3.2.4 Condiciones de la modelación ........................................................................................................................... 18

4 RESULTADOS ....................................................................................................................................19

4.1 Caracterización hidrográfica ....................................................................................................................... 19
4.2 Precipitaciones máximas ............................................................................................................................ 21

4.3 Escorrentía máxima.................................................................................................................................... 24

4.3.1 Método Racional ................................................................................................................................................. 24

4.4 Modelación hidráulica ................................................................................................................................ 26

4.4.1 Superficie de inundación .................................................................................................................................... 26
4.4.2 Estero Cuni ............................................................................................................ ¡Error! Marcador no definido.

5 CONCLUSIONES ................................................................................................................................29

6 REFERENCIAS ....................................................................................................................................29

TABLAS

Tabla 3-1 Listado de estaciones meteorológicas ............................................................................................................ 7

Tabla 3-2 Factores del Coeficiente de escorrentía para periodo de retorno 10 años. ............................................... 11

Tabla 3-3 Intensidad de la lluvia para distintos períodos de retorno. ......................................................................... 12

Tabla 3-4 Estimación del coeficiente de Manning según método de Cowan ............................................................. 17

Tabla 4-1 Características geomorfológicas de la cuenca estudiada ............................................................................ 19

Tabla 4-2 Principales estadígrafos de precipitaciones máximas anuales en 24 horas ............................................... 21

Tabla 4-3 Resultados Test Chi Cuadrado para bondad de ajuste a series de precipitación según estación
meteorológica ................................................................................................................................................................. 21

Tabla 4-4 Precipitación máxima en 24 hrs según periodo de retorno y estación meteorológica (mm). .................. 22

Tabla 4-5 Coeficiente de escorrentía estimados para la cuenca en estudio ............................................................... 24

Tabla 4-5 Tiempo de concentración estimado.............................................................................................................. 24

Tabla 4-6 Tabla 4 6 Intensidades de precipitación estimadas para la cuenca estudiada ........................................... 25

Tabla 4-7 Caudales máximos estimados según cuenca en estudio y periodo de retorno.......................................... 25

Proyecto PFV Lagos i
IM2SOLAR003.INF003.Rev0

Anexo N°2.7.1 Estudio de crecidas Estero Cuni

FIGURAS

Figura 1-1 Ubicación nacional, regional y local del emplazamiento de las obras del Proyecto ................................... 4

Figura 2-1 Área de estudio ............................................................................................................................................... 6

Figura 3-1 Ubicación estaciones meteorológicas cercanas al área de estudio ............................................................. 9

Figura 3-2 Representación de los términos de la ecuación de energía en dos secciones .......................................... 13

Figura 3-3 Esquema del método usado por HEC-RAS para calcular las subsecciones ................................................ 14

Figura 3-4 Vista en planta de perfiles transversales generados en HEC-GeoRAS ....................................................... 16

Figura 3-5 Fotografías Estero Cuni................................................................................................................................. 18

Figura 4-1 Delimitación de cuenca hidrográfica ........................................................................................................... 20

Figura 4-2 Ajuste distribución Gumbel a serie de precipitación máxima en 24 hrs anuales estación Pirihueico en
Pirihueico, periodo 1939 - 2020 .................................................................................................................................... 22

Figura 4-3 Resultados precipitaciones máximas en 24 horas en mapa según estación (T=100 años) ...................... 23

Figura 4-4 Superficie de inundación estero en área de estudio .................................................................................. 27

Figura 4-5 Resultados eje hidráulico en secciones transversales ................................................................................ 28

Figura 4-6 Resultados eje hidráulico en perfil longitudinal .......................................................................................... 28

APÉNDICES

Apéndice A - Estudio Topográfico

Apéndice B - Resultados del Test Chi cuadrado y ajuste de probabilidades de las estaciones meteorológicas

Apéndice C - Archivos digitales cartográficos y de modelación

Apéndice D - Tablas de resultados numéricos modelación hidráulica

Parque fotovoltaico Los Lagos
IM2SOLAR003.INF003.Rev0

ii

Anexo N°2.7.1 Estudio de crecidas Estero Cuni

1 INTRODUCCIÓN

En el marco de la evaluación de prefactibilidad del Proyecto “Parque Fotovoltaico Los Lagos”, en adelante el
Proyecto, Im2Solar solicitó a Hydrus Ambiental un estudio hidrológico e hidráulico que permita establecer la
superficie de inundación del Estero Cuni, con el objetivo de esclarecer la superficie de drenaje del sector de estudio
para un evento de crecida.

El siguiente documento presenta caracterización hidrológica e hidráulica del Estero Cuni que drenan al sector de
obras del Proyecto, donde para cada uno se entregaron los antecedentes técnicos que permiten estimar las
precipitaciones y caudales máximos que se podrían generar en el área de estudio, con el objetivo de determinar la
magnitud de las crecidas y cotas de inundación para un período de retorno de 100 años, lo cual define la superficie
de los cauces. Luego se realizó una simulación hidráulica del comportamiento de este flujo natural, para determinar
el área de inundación potencial para las crecidas respectivas. Cabe mencionar que, para cumplir con el objetivo de
la evaluación de recursos hídricos, se definieron trabajos de gabinete para procesar la información y trabajos en
terreno que permitieron levantar la información in situ.

El Proyecto en evaluación, corresponde a un Proyecto de Pequeños Medios de Generación Distribuida (PMGD) por
medio de Energía Renovable No Convencional (ERNC) que producirá energía limpia a través de la construcción y
operación de una Central Solar Fotovoltaica (PF) de 13,08 MW de potencia nominal o capacidad instalada, la que
será inyectado al Sistema Interconectado Central (SIC), actual Sistema Eléctrico Nacional (SEN), a través de un
alimentador. La Figura 1-1 presenta la ubicación nacional, regional y local del emplazamiento de las obras del

Proyecto.

Parque fotovoltaico Los Lagos
IM2SOLAR003.INF003.Rev0

3

Anexo N°2.7.1 Estudio de crecidas Estero Cuni

Figura 1-1 Ubicación nacional, regional y local del emplazamiento de las obras del Proyecto

Fuente: Hydrus Ambiental, 2024.

Parque fotovoltaico Los Lagos
IM2SOLAR003.INF003.Rev0

4

Anexo N°2.7.1 Estudio de crecidas Estero Cuni

2 ÁREA DE ESTUDIO

El área de estudio corresponde al sector donde se ubica el Estero Cuni hasta el sector de las obras del Proyecto. Se
destaca que el curso de agua se encuentra inserto dentro de la Cuenca cuenca del Río Valdivia, subcuenca Río Calle
Calle, Subsubcuenca Río Calle Calle entre Junta Río San Pedro y Río Quinchilca Bajo Río Cuicuileufú, acorde a la
subdivisión oficial de la Dirección General de Aguas (DGA).

El Estero Cuni nace a al noreste de la ciudad de Los Lagos a los 78 msnm, tiene una extensión de aproximadamente
8 km y vierte sus aguas al Río Calle Calle. Se destaca que este curso de agua está identificado en la cartografía del
Instituto Geográfico Militar (IGM) a escala 1:50.000.

La Figura 2-1 presenta el área de estudio correspondiente a la cuenca del estero a evaluar hasta la altura del trazado
donde se proyectan las obras del Proyecto.

Parque fotovoltaico Los Lagos
IM2SOLAR003.INF003.Rev0

5

Figura 2-1 Área de estudio

Fuente: Hydrus Ambiental, 2024.

Anexo N°2.7.1 Estudio de crecidas Estero Cuni

6

Parque fotovoltaico Los Lagos
IM2SOLAR003.INF003.Rev0

Anexo N°2.7.1 Estudio de crecidas Estero Cuni

3 METODOLOGÍA

A continuación, se presenta la metodología utilizada para el estudio de crecidas consistente en un estudio
hidrológico e hidráulico del área de estudio. El estudio hidrológico tuvo el objetivo de delimitar la cuenca hidrográfica
del estero Cuni y determinar el caudal de crecida que pasaría por el estero según periodo de retorno, y luego, el
estudio hidráulico evaluó el comportamiento y características del flujo en todas sus secciones estimando el eje
hidráulico resultante para cada caudal, determinando así la superficie de inundación.

3.1 Estudio Hidrológico

El estudio hidrológico comenzó con una revisión de antecedentes de la zona de estudio, se caracterizaron y delimito
la cuenca hidrográfica del área de estudio y se entregaron las precipitaciones máximas en 24 hrs para diferentes
periodos de retorno, con lo cual se estimaron los caudales máximos de crecidas según periodos de retorno para la
cuenca formada por el estero en estudio.

3.1.1 Revisión de antecedentes

Los antecedentes disponibles en la zona de estudio corresponden principalmente a estudios y datos
hidrometeorológicos de la Dirección General de Aguas (DGA) y del Instituto Geográfico Militar (IGM). A continuación,
se presentan los antecedentes recopilados:

 - “Precipitaciones máximas en 1, 2 y 3 días” publicado en el año 1991 por la DGA.

 - Registro de series de precipitaciones máximas anuales en 24 horas de las estaciones meteorológicas
pertenecientes al Banco Nacional de Aguas (BNA).

 - Red de drenaje registrada por el Instituto Geográfico Militar (IGM) a escala 1:50.000.

 - Las subcuencas hidrográficas definidas en el Inventario de Cuencas Hidrográficas de la DGA.

 - Manual de Carreteras, Volumen N°3.

El listado de las estaciones meteorológicas cercanas al área de estudio se presenta en la Tabla 3-1, donde además
se presenta el código DGA, sus coordenadas norte y este con Datum WGS84 18H, altitud, cantidad de años con
información, inicio y fin del registro. Por su parte, la Figura 3-1 presenta la ubicación de las estaciones meteorológicas
que existen en el área de estudio junto a las cuencas determinadas por la DGA.

Tabla 3-1 Listado de estaciones meteorológicas

|ID|Estación|Código DGA|Coordenadas UTM<br>WGS84 Huso 19H|Col5|Altitud<br>(msnm)|Inicio<br>registro|Fin<br>registro|Cantidad de<br>años con<br>información|
|---|---|---|---|---|---|---|---|---|
|ID|Estación|Código DGA|Norte (m)|Este (m)|Este (m)|Este (m)|Este (m)|Este (m)|
|1|Lago Riñihue|10111002-8|5.594.216|718.105|120|01/03/1985|---|36|
|2|Huichaco|10137002-K|5.601.340|693.901|95|02/10/1994|---|27|
|3|Río Fui en desagüe Lago<br>Pirihue|10100002-8|5.582.185|252.705|600|01/12/1926|---|18|
|4|Catamutun|10141001-3|5.552.187|655.957|150|01/10/1997|---|25|
|5|Llancahue|10123004-K|5.586.594|655.803|70|01/09/1972|---|48|
|6|Valdivia (UAustral)|10123006-6|5.589.357|650.280|10|01/01/1960|---|19|
|7|Pirihueico en Pirihueico|10100004-4|5.559.328|269.570|600|01/05/1939|---|48|

Fuente: Hydrus Ambiental, 2024.

Parque fotovoltaico Los Lagos
IM2SOLAR003.INF003.Rev0

7

Anexo N°2.7.1 Estudio de crecidas Estero Cuni

3.1.2 Caracterización hidrográfica

Para la definición de los límites de la cuenca del estero en estudio se utilizó como base la red de cauces generada
con la cartografía IGM a escala 1:50.000, la utilización del modelo de elevación digital (DEM) Alos Palsar cuyo tamaño
de celda es de 12,5x12,5 metros, las curvas de nivel generadas a partir de un levantamiento topográfico (presentado
en Apéndice A), y fotointerpretación de imágenes satelitales. Además, se estimaron los parámetros morfológicos de
la cuenca (área aportante, longitud del cauce principal, pendiente media del cauce, pendiente media de la cuenca,
elevación mínima, elevación media y elevación máxima) mediante herramientas computacionales de Sistema de
Información Geográfica (SIG).

3.1.3 Precipitaciones máximas

De la recopilación de antecedentes, se analizaron las series de precipitación máxima anual registradas en las
estaciones consideradas representativas de la condición temporal y espacial de la zona de estudio dada su ubicación
y cantidad de información. Se realizaron los cálculos de los estadígrafos principales de estas series (valor mínimo,
valor medio, valor máximo, desviación estándar y coeficiente de variación). Luego, se realizó un análisis de frecuencia
a la serie de precipitaciones máximas en 24 hrs anuales en base a un ajuste de distribución de probabilidad. Además,
a través del test Chi Cuadrado (significancia de 5%) se estudió la bondad del ajuste con 6 intervalos de las
distribuciones Log Normal, Pearson III, Log Pearson y Gumbel (Valores Extremos tipo I) comúnmente utilizadas en
hidrología para definir la distribución que mejor se ajusta a los registros observados y así definir la precipitación
estimada según el periodo de retorno. Cabe mencionar que, las series de precipitación máxima en 24 hrs de las
estaciones meteorológicas se presentan en el Apéndice B, y los resultados del Test Chi cuadrado y ajuste de
probabilidades de las estaciones meteorológicas se presentan en el Apéndice C.

Parque fotovoltaico Los Lagos
IM2SOLAR003.INF003.Rev0

8

Parque fotovoltaico Los Lagos
IM2SOLAR003.INF003.Rev0

Anexo N°2.7.1 Estudio de crecidas Estero Cuni

Figura 3-1 Ubicación estaciones meteorológicas cercanas al área de estudio

Fuente: Hydrus Ambiental, 2024.

9

Anexo N°2.7.1 Estudio de crecidas Estero Cuni

3.1.4 Escurrimientos máximos

Los escurrimientos máximos corresponden a los escurrimientos esporádicos líquidos que puedan generarse a partir
de eventos extremos de precipitación. Para evaluar la escorrentía máxima del estero en estudio que no poseen
registros de información fluviométrica, se utilizaron los métodos de precipitación escorrentía recomendados en
Manual de Cálculo de Crecidas y Caudales Mínimos en Cuencas sin Control Fluviométrico (DGA, 1995) y en el Manual
de Carreteras Vol. N°3 (MOP, 2022). Estos métodos relacionan la precipitación máxima en 24 horas para un periodo
de retorno de 100 años y el área pluvial de las cuencas.

La metodología propuesta para estimar el caudal máximo instantáneo corresponde al Método Racional del Manual
de Carreteras dado que cumple los supuestos para su aplicación correspondiente a cuencas pequeñas menores que
25 km [2] . Por otro lado, no se evaluaron otros métodos de precipitación-escorrentía como por ejemplo DGA-AC, VerniKing, debido a que no se cumplen los supuestos para su aplicación correspondiente a cuencas entre 20 y 10.000
km [2] .

3.1.4.1 Método Racional

El método racional (MOP, 2022) es utilizable en cuencas pequeñas menores a 25 km [2] y supone que el escurrimiento
máximo proveniente de una tormenta es proporcional a la lluvia caída. Este método calcula el caudal máximo como
una proporción del tamaño de la intensidad de la lluvia de diseño (i, mm/hr), del área de la cuenca aportante (A,
Km [2] ), y un coeficiente de escorrentía (C, sin unidad) según se presenta en la ecuación N°1. Se destaca que la
precipitación considerada corresponde a la precipitación de 24 hrs de periodo de retorno de 100 años.

Ecuación N°1

Q= [C∙i∙A]

3,6

Donde,
Q = Caudal instantáneo máximo asociado al periodo de retorno T años, expresado en m [3] /s.
C = Coeficiente de escorrentía para el periodo T.
i = intensidad de la lluvia de periodo de retorno T y a una duración igual al tiempo de concentración de la
cuenca en mm/h.
A = Área pluvial de la cuenca, expresada en km [2] .

En cuanto al coeficiente de escorrentía se consideran las recomendaciones del Manual de Carreteras Vol. N°3 (MOP,
2022) presentadas en la Tabla 3-2. Para estimar el coeficiente de escorrentía para un periodo de retorno de 100
años, se amplifica el valor de 10 años por un factor igual a 1,25, mientras que para un periodo de retorno de 50 años
se amplifica el valor por un factor igual a 1,2 (MOP, 2022).

Parque fotovoltaico Los Lagos
IM2SOLAR003.INF003.Rev0

10

Anexo N°2.7.1 Estudio de crecidas Estero Cuni

Tabla 3-2 Factores del Coeficiente de escorrentía para periodo de retorno 10 años.

Fuente: Manual de carreteras Volumen N°3 (MOP, 2022).

Por otro lado, cabe mencionar que la intensidad media de la precipitación de diseño depende de la duración de la
tormenta. Se consideró que la duración de la tormenta es igual al tiempo de concentración de la cuenca, de acuerdo
con las recomendaciones del Manual de Carreteras Vol. 3 (MOP, 2022). Para el cálculo del tiempo de concentración
(tc) de una cuenca existen numerosas expresiones determinadas de manera empírica. Para este análisis se utilizó el
promedio de tres expresiones presentadas en el Manual de Carreteras (MOP, 2022), siempre que cumplieran con
sus restricciones de uso. La primera corresponde a la expresión de _California Culverts Practice_ (1942) (ecuación N°2),
la segunda corresponde a la expresión de Témez (1991) o Normas españolas (ecuación N°3), y la tercera corresponde
a la expresión de Giandotti (ecuación N°4). Se destaca que la Guía Metodológica (DGA, 2016) recomienda tiempos

de concentración no menores a 10 minutos.

ecuación N°2

ecuación N°3

Tc= 0,95 ∙( [L] H [3] ~~[)]~~

0,385

Tc= 0,3 ∙ [L] [0,76]

S [0,19]

ecuación N°4

Tc= [4A] [0,5] [ + 1,5L]

0,8Hm [0,5]

Donde,
L = Largo del cauce principal, expresado en km.
H = Desnivel máximo de la cuenca, expresado en m.
Hm = Desnivel entre cota media de la cuenca y la salida en m.
S = Pendiente (m/m).
A = Área de la cuenca en km [2] .

Tc = Tiempo de concentración, expresado en horas.

Parque fotovoltaico Los Lagos
IM2SOLAR003.INF003.Rev0

11

Anexo N°2.7.1 Estudio de crecidas Estero Cuni

Finalmente, para calcular la Intensidad de la lluvia se utilizó la fórmula de Grunsky, la cual considera la intensidad de
la lluvia de periodo de retorno T y a una duración igual al tiempo de concentración de la cuenca en mm/h.

[T]

24 [∗√24] √Tc

I= [P24] [T]

√Tc

ecuación N°5

I=Intensidad de la lluvia de diseño (mm)
P24 [T] =Precipitación en 24 horas para T período de retorno (mm)
T C =Tiempo de concentración (hr)

Se destaca que se compararon los resultados de la Intensidad de la lluvia con los mostrados en las curvas IDF, de
acuerdo con el tiempo de concentración, según el Manual de Carreteras Vol. 3 para las estaciones cercanas al área
de estudio, tal como se muestran en la Tabla 3-3.

Tabla 3-3 Intensidad de la lluvia para distintos períodos de retorno.

Fuente: Manual de carreteras Volumen N°3 (MOP, 2022).

Parque fotovoltaico Los Lagos
IM2SOLAR003.INF003.Rev0

12

Anexo N°2.7.1 Estudio de crecidas Estero Cuni

3.2 Estudio Hidráulico

El estudio hidráulico determina el comportamiento y características del flujo en todas sus secciones a lo largo del
área de estudio. Para ello, se realizó una modelación hidráulica del escurrimiento superficial con el fin de estimar el
eje hidráulico o cota que alcanzaría el caudal de crecida según periodo de retorno del estudio hidrológico
considerando la topografía del estero. Cabe mencionar que, se realizó una visita técnica a terreno el día 25 de julio
de 2024 para determinar en terreno la condición actual del estero Cuni.

A continuación, se presenta con mayor detalle la metodología aplicada en el estudio hidráulico desde el detalle de
la modelación hidráulica como el software de modelación, la geometría y extensión del cauce, hasta el coeficiente
de Manning del estero y las condiciones de modelación.

3.2.1 _Software_ de modelación

Para la estimación del eje hidráulico y sus características se realizó una simulación hidráulica de los cauces del área
de estudio en el programa HEC-RAS ( _Hydrologic Engineerng Center - River Analisis System_ ) versión 6.0, desarrollado
por el _U.S. Army Corps of Engineer_ . Este programa estima los niveles de agua mediante un balance de energía entre
dos secciones transversales contiguas del cauce incorporando las pérdidas de energías friccionales por medio de
una ley de resistencia (Manning). El nivel de energía y los términos que la componen se presentan
esquemáticamente en la Figura 3-2.

Figura 3-2 Representación de los términos de la ecuación de energía en dos secciones

Fuente: Traducido de Manual HEC RAS 6.0.

Las ecuaciones 10 a la 13 participan del proceso de cálculo iterativo para estimar los valores del eje hidráulico.

2

Ecuación de energía
2g [2] ecuación N°6

2

y 1 + z 1 + α 1 ∙ [V] [1]

[V] [1]

2g [+ h] [e] [= y] [2] [ + z] [2] [ + α] [2] [ ∙V] 2g [2]

1 1 1 2g [e] [2] [2] [2] 2g ecuación N°6

Donde:

Parque fotovoltaico Los Lagos
IM2SOLAR003.INF003.Rev0

13

Anexo N°2.7.1 Estudio de crecidas Estero Cuni

y 1, y 2 : Profundidad del escurrimiento en las secciones 1 y 2
z 1, z 2 : Cota de fondo en las secciones 1 y 2
V 1, V 2 : Velocidad Media en las secciones 1 y 2
α 1, α 2 : Coeficiente de Coriolis en las secciones 1 y 2
g : Aceleración de gravedad
h e : Pérdidas de energía entre las secciones 1 y 2

2 2

[2] −α 1 V 1

h e
= J∙L+ C∙( [α] [2] [V] [2]

2

−α 1 V 1 Ecuación de pérdida de carga

2g ~~)~~ ecuación N°7

2

e 2g ecuación N°7

Donde:

L : Longitud de cada tramo.
J : Pendiente plano de carga.
C : Coeficiente de pérdida por expansión o contracción.

L= [L] [iz][q] [Q] [iz][q] [+ L] [central] [Q] [central] [+ L] [der] [Q] [der]

Longitud equivalente

Q izq + Q central + Q der ecuación N°8

Donde:
L izq −L central −L der : Longitud entre cada sección para la ribera izquierda, cauce principal y ribera derecha.
Q izq −Q central −Q der : Caudal medio aritmético entre los flujos de la ribera izquierda, cauce y ribera derecha.

Q izq + Q central + Q der

Q= ~~[√]~~ [J]

Ecuación de Manning

n [AR]

2

3

ecuación N°9

n

Donde:
Q : Capacidad de porteo del cauce (m [3] /s)
n : Coeficiente de Manning, rugosidad del cauce
J : Pérdida de carga
A : Área hidráulica (m [2] )
R : Radio hidráulico (m)

De manera general, la sección de un cauce natural o artificial se divide en ribera izquierda, cauce principal y ribera
derecha, donde en cada una de estas subsecciones se evalúa la ley de resistencia escogida usando los respectivos
coeficientes de rugosidad de cada sección. La Figura 3-3 presenta un esquema del método usado por HEC RAS para

calcular subsecciones dentro de una sección transversal.

Figura 3-3 Esquema del método usado por HEC-RAS para calcular las subsecciones

Fuente: Manual HEC RAS 6.0.

Parque fotovoltaico Los Lagos
IM2SOLAR003.INF003.Rev0

14

Anexo N°2.7.1 Estudio de crecidas Estero Cuni

3.2.1.1 Limitaciones HEC RAS y su corrección

Uno de los supuestos que se encuentra implícito de las expresiones analíticas es que el cauce superficial tiene
pendiente menor a 1:10. Esto se debe a que la carga de presión vertical se considera igual a la profundidad del agua
medida de forma perpendicular a la base del cauce, siendo que la derivación verdadera debiera estar multiplicada
por el coseno del ángulo formado con la pendiente. Para cauces con pendientes igual o menor a 1:10, es decir
ángulos iguales o menores a 5,7°, este es un error pequeño para estimar la profundidad del flujo (cos(5,7°)=0,995).

Sobre cauces con pendientes mayores a 1:10 se necesitaría corregir la profundidad del flujo dividiendo por el coseno
del ángulo formado por la pendiente, tal como se presenta en la ecuación N°14. Se destaca que, los primeros tramos
de las quebradas en estudio presentan pendientes mayores al 10% por lo que se requiere corregir la altura o
profundidad del flujo, mientras que los sectores más aguas abajo presentan pendientes menores a 10% por lo que

no es necesario la corrección de resultados en estos sectores.

d Ecuación N°10
D=
cos(θ)

Donde,
D : Profundidad vertical corregida
d : Profundidad vertical estimada por HEC RAS
θ : pendiente del cauce modelado expresado en grados (°).

3.2.2 Geometría y extensión del cauce

La geometría de los cauces se generó utilizando el complemento HEC-GeoRAS para ArcGIS con las curvas de nivel
cada 0,5 metros [1] . Luego, se generaron los perfiles transversales en el estero. Se destaca que, los perfiles
transversales se trazaron cada 20 m aproximadamente en cada uno de los cauces. Además, la extensión de la
modelación se realizó sobre un tramo mínimo de 100 m aguas arriba y 100 m aguas abajo con el cruce con el trazado
del Proyecto. Además, cabe mencionar que se utilizó la función “ _leeves_ ” para definir los bordes de los cauces
superficiales. La Figura 3-4 presenta la vista en planta de la ubicación de los perfiles transversales trazados a lo largo
de la bajada de agua identificada en el estero en estudio.

.

1 El detalle de las curvas de nivel se presenta en el Apéndice A

Parque fotovoltaico Los Lagos
IM2SOLAR003.INF003.Rev0

15

Parque fotovoltaico Los Lagos
IM2SOLAR003.INF003.Rev0

Anexo N°2.7.1 Estudio de crecidas Estero Cuni

Figura 3-4 Vista en planta de perfiles transversales generados en HEC-GeoRAS

Fuente: Hydrus Ambiental, 2024.

16

Anexo N°2.7.1 Estudio de crecidas Estero Cuni

3.2.3 Coeficiente de Manning

El coeficiente de Manning del estero en estudio se estimó utilizando el método de Cowan, recomendado en el
Manual de Carreteras Volumen N°3. La ecuación N°15 muestra la expresión para determinar el coeficiente de
Manning (n), mientras que la Tabla 3-4 presenta el valor estimativo de cada índice según las características del cauce.

n= m∙(n 0 + n 1 + n 2 + n 3 + n 4 +) Ecuación N°11

Tabla 3-4 Estimación del coeficiente de Manning según método de Cowan

Fuente: Manual de carreteras Volumen N°3, MOP, 2022.

El coeficiente de Manning se estimó en 0,050 (-) para los bordes y 0,100 (-) para el centro del cauce del estero Cuni
Este valor fue estimado a partir de los siguientes criterios de selección según el método de Cowan:

 - Lecho: Centro n0= 0.02 y borde n0 = 0,02

 - Grado de irregularidad: Centro n1= 0,005 y borde n1 = 0,005

 - Variaciones de la sección: Centro n2= 0,005 y borde n2 = 0,005

 - En lo relativo de las obstrucciones: Centro n3= 0,02 y borde n3 = 0,01

 - Vegetación: Centro n4= 0,05 y borde n4 = 0,01

 - Grado de meandros; Centro m= 1 y borde m = 1


La Figura 3-5 muestra las fotografías en distintos sectores de los cauces, indicando además con una flecha azul el
sentido de escurrimiento del flujo. Se destaca que, las fotografías fueron tomadas en una visita a terreno realizada
el día 25 de julio de 2024, y que en la misma imagen se presentan las coordenadas UTM datum WGS84 18S donde
fue tomada la fotografía.

Parque fotovoltaico Los Lagos
IM2SOLAR003.INF003.Rev0

17

(a)

Anexo N°2.7.1 Estudio de crecidas Estero Cuni

Figura 3-5 Fotografías Estero Cuni

(b)
Fuente: Hydrus Ambiental, 2024.

3.2.4 Condiciones de la modelación

La modelación del cauce en estudio determina la superficie de inundación y se compara con la ubicación del
emplazamiento del Proyecto. Además, la modelación determina el comportamiento y características del flujo en
todas sus secciones a lo largo del área de estudio. A continuación, se presenta un listado de los datos de ingreso y/o

condiciones asumidas en la modelación del cauce.

 - La modelación del cauce se realizó en régimen permanente.

 - Como condiciones de borde se asume para aguas arriba una altura de agua crítica de manera que el
programa simule el flujo en un régimen mixto (subcrítico o supercrítico). Aguas abajo se asume altura de
agua normal, con una pendiente igual a la determinada según las últimas tres secciones en el estero.

 - La modelación hidráulica se realizó para los caudales de crecida (T=100 años) presentados en el acápite
3.1.4, considerando que esta crecida define la delimitación del cauce.

Parque fotovoltaico Los Lagos
IM2SOLAR003.INF003.Rev0

18

Anexo N°2.7.1 Estudio de crecidas Estero Cuni

4 RESULTADOS

4.1 Caracterización hidrográfica

El estero Cuni corresponde a un cauce superficial que drena las aguas hacia el sector donde se ubican las obras del
Proyecto. Se destaca que el estero se encuentra insertas dentro de la Cuenca del Río Valdivia, subcuenca Río Calle
Calle, Subsubcuenca Río Calle Calle entre Junta Río San Pedro y Río Quinchilca Bajo Río Cuicuileufú, acorde a la
subdivisión oficial de la Dirección General de Aguas (DGA).

El Estero Cuni nace a al noreste de la ciudad de Los Lagos a los 78 msnm, tiene una extensión de aproximadamente
8 km y vierte sus aguas al Río Calle Calle. Se destaca que este curso de agua está identificado en la cartografía del
Instituto Geográfico Militar (IGM) a escala 1:50.000.

En la Tabla 4-1 se presentan las características geomorfológicas principales de las cuencas en estudio, y en la Figura
4-1 se presentan la cuenca definida para el estero Cuni hasta la altura de las obras del Proyecto.

Tabla 4-1 Características geomorfológicas de la cuenca estudiada

|ID|Cauce|Área (km2)|Elevación<br>media<br>(msnm)|Elevación<br>mínima<br>(msnm)|Elevación<br>máxima<br>(msnm)|Largo del<br>cauce<br>(km)|Pendiente<br>media del<br>cauce (%)|Pendiente<br>media de la<br>cuenca (%)|
|---|---|---|---|---|---|---|---|---|
|1|Estero Cuni|2.3|79|69|92|2|5|4,2|

Fuente: Hydrus Ambiental, 2024.

Parque fotovoltaico Los Lagos
IM2SOLAR003.INF003.Rev0

19

Figura 4-1 Delimitación de cuenca hidrográfica

Fuente: Hydrus Ambiental, 2024.

Anexo N°2.7.1 Estudio de crecidas Estero Cuni

20

Parque fotovoltaico Los Lagos
IM2SOLAR003.INF003.Rev0

Anexo N°2.7.1 Estudio de crecidas Estero Cuni

4.2 Precipitaciones máximas

Las precipitaciones máximas en 24 horas se obtuvieron de las estaciones 1) Lago Riñihue, 2) Huichaco, 3) Río Fui en
desagüe Lago Pirihue, 4) Catamutun, 5) Llancahue, 6) Estación Valdivia y 7) Estación Pirihueico en Pirihueico
considerando que se ubican en la misma cuenca donde se localizan las obras del proyecto. Los estadígrafos
principales de la serie de precipitación máxima en 24 horas anual (valor mínimo, valor medio, valor máximo,
desviación estándar y coeficiente de variación) se presentan en la Tabla 4-2, donde se destaca que la estación

~
Pirihueico en Pirihueico registra las máximas precipitaciones registrada en 24 hrs ( 97 mm). Además, se destaca

~
que la estación Catamutun es la estación más cercana al área de estudio ( 26 km) con 25 años de registro.

Tabla 4-2 Principales estadígrafos de precipitaciones máximas anuales en 24 horas

|ID|Estación|Años con<br>información|Mínimo<br>(mm)|Media<br>(mm)|Máximo<br>(mm)|Desv. Estándar<br>(mm)|Coef. Variación<br>(-)|
|---|---|---|---|---|---|---|---|
|1|Lago Riñihue|36|51|84|126|18,6|0,22|
|2|Huichaco|27|39|61|93|13,2|0,22|
|3|Río Fui en desagüe Lago<br>Pirihue|18|70|118|184|31|0,26|
|4|Catamutun|25|15|89|151|30,7|0,34|
|5|Llancahue|48|49|77|121|18,7|0,24|
|6|Valdivia|19|51|89|155|27,6|0,31|
|7|Pirihueico en Pirihueico|48|38|97|203|30,9|0,32|

Fuente: Hydrus Ambiental, 2024.

Además, se analizó la frecuencia de las estadísticas meteorológicas en base a un ajuste de distribución de
probabilidad a la serie anual de precipitación máxima en 24 hrs registrados en las siete estaciones considerando
todas las estaciones. A través del test Chi Cuadrado (significancia de 5%) se estudió la bondad del ajuste de las
distribuciones Log Normal, Pearson III, Log Pearson y Gumbel (Valores Extremos tipo I). De los resultados obtenidos
presentados en la Tabla 4-3, se destaca que se aprueba el test para la mayoría de los casos.

Tabla 4-3 Resultados Test Chi Cuadrado para bondad de ajuste a series de precipitación según estación

meteorológica

|Distribución\Estación|Lago Riñihue|Huichaco|Río Fui en<br>desagüe<br>Lago Pirihue|Catamutun|Llancahue|Estación<br>Valdivia|Estación<br>Pirihueico en<br>Pirihueico|
|---|---|---|---|---|---|---|---|
|Log-Normal|Aceptado|Aceptado|Aceptado|Rechazado|Aceptado|Aceptado|Aceptado|
|Pearson III|Aceptado|Aceptado|Aceptado|Aceptado|Aceptado|Aceptado|Aceptado|
|Log Pearson|Rechazado|Rechazado|Rechazado|Rechazado|Rechazado|Rechazado|Aceptado|
|Gumbel|Aceptado|Aceptado|Aceptado|Rechazado|Aceptado|Aceptado|Aceptado|

Fuente: Hydrus Ambiental, 2024.

El análisis de frecuencia da como resultado las precipitaciones máximas en 24 hrs para distintos períodos de retorno.
Los resultados indicaron que, la distribución de probabilidades que estimó los valores más conservadores depende
de cada estación, sin embargo, en la mayoría de los casos la Distribución Gumbel entrego los valores más
conservadores. La Tabla 4-4 presenta los valores de precipitación máxima en 24 horas según periodo de retorno del
ajuste de la distribución de probabilidades utilizando la distribución más conservadora según el caso. Los resultados
del Test Chi cuadrado y ajuste de probabilidades de las estaciones meteorológicas se presentan en el Apéndice B.

Parque fotovoltaico Los Lagos
IM2SOLAR003.INF003.Rev0

21

Anexo N°2.7.1 Estudio de crecidas Estero Cuni

Tabla 4-4 Precipitación máxima en 24 hrs según periodo de retorno y estación meteorológica (mm).

|T<br>(años)|Lago Riñihue|Huichaco|Río Fui en<br>desagüe Lago<br>Pirihue|Catamutun|Llancahue|Valdivia|Pirihueico en<br>Pirihueico|
|---|---|---|---|---|---|---|---|
|T <br>(años)|Dist Gumbel<br>(mm)|Dist Gumbel<br>(mm)|Dist Gumbel<br>(mm)|Dist Pearson III<br>(mm)|Dist Gumbel<br>(mm)|Dist Gumbel<br>(mm)|Dist Gumbel<br>(mm)|
|5|99,8|72,6|147,2|115,2|91,8|115,6|123,2|
|10|112,8|81,5|169,3|126,9|104,1|135|142,7|
|25|127,6|92,9|197,6|138,6|119,6|160|168|
|50|139|101,3|218,6|145,9|131,1|178,5|186,9|
|100|150|109,7|239,4|152,1|142,5|196,9|205,6|

Fuente: Hydrus Ambiental, 2024.

De los resultados obtenidos, se observa que el valor máximo estimado para la precipitación de 100 años de periodo
de retorno fue de 239,4 mm en la estación Río Fui en desagüe Lago Pirihue. La Figura 4-2 presenta el ajuste de la
distribución Gumbel a la serie de precipitaciones máximas anuales registrada en la estación Pirihueico en Pirihueico.
Además, la Figura 4-3 presenta los resultados obtenidos en un mapa junto con las isoyetas de precipitación máxima
diaria (DGA, 1991) comparables con un periodo de retorno de 10 años, de lo cual se considera que las precipitaciones
máximas estimadas son valores conservadores para la zona de estudio.

Figura 4-2 Ajuste distribución Gumbel a serie de precipitación máxima en 24 hrs anuales estación Pirihueico en

Pirihueico, periodo 1939 - 2020

Fuente: Hydrus Ambiental, 2024.

Parque fotovoltaico Los Lagos
IM2SOLAR003.INF003.Rev0

22

Parque fotovoltaico Los Lagos
IM2SOLAR003.INF003.Rev0

Anexo N°2.7.1 Estudio de crecidas Estero Cuni

Figura 4-3 Resultados precipitaciones máximas en 24 horas en mapa según estación (T=100 años)

Fuente: Hydrus Ambiental, 2024.

23

Anexo N°2.7.1 Estudio de crecidas Estero Cuni

4.3 Escorrentía máxima

La escorrentía máxima del estero en estudio fue estimada considerando métodos que relacionan la precipitación
máxima con la escorrentía máxima. Cabe recordar que, en la caracterización hidrográfica se estimó que la superficie
de drenaje de la cuenca en estudio no supera los 2,3 km [2], por lo que no cumple con los requisitos de los métodos
DGA-AC y Verni y King modificado, y solamente sería aplicable el Método Racional del Manual de Carreteras Vol N°3.

4.3.1 Método Racional

El método racional supone que el escurrimiento máximo proveniente de una tormenta es proporcional al área de
drenaje, a un coeficiente que depende de las condiciones del terreno, y a la lluvia caída, la cual se estima para una
duración igual al tiempo de concentración de la cuenca y con periodo de retorno de 100 años.

El coeficiente de escorrentía se estimó para un periodo de retorno de 10 años para el cauce donde el valor estimado
es de 0,32(-) considerando las condiciones o factores de relieve, de infiltración, de cobertura vegetal y de
almacenamiento superficial. Para estimar el coeficiente de escorrentía para un periodo de retorno de 100 años, se
amplifica el valor de 10 años por un factor igual a 1,25 (MOP, 2022), respectivamente, resultando un coeficiente de
escorrentía para 100 años igual a 0,4 (-). La Tabla 4-5 presenta los resultados obtenidos.

Tabla 4-5 Coeficiente de escorrentía estimados para la cuenca en estudio

|Condición o Factor|Coeficiente de escorrentía (-)|
|---|---|
|Relieve|0.14|
|Infiltración|0.08|
|Cobertura Vegetal|0.05|
|Almacenamiento<br>Superficial|0.05|
|Coef. Escorrentía|0.32|
|Coef. Escorrentía<br>(100 años)|0.4|

Fuente: Hydrus Ambiental, 2024.

Por otro lado, el tiempo de concentración fue estimado mediante los métodos de _California Culverts Practice._ Témez
o Normas españolas, y Giandotti y los resultados se presentan en la Tabla 4-6..

Tabla 4-6 Tiempo de concentración estimado

|Método|Tiempo de concentración (hr)|
|---|---|
|_California Culverts Practice_|0.8|
|Témez o Normas Españolas|0.5|
|Giandotti|4.1|
|Promedio|1.8|

Fuente: Hydrus Ambiental, 2024.

Considerando que la duración de la tormenta es igual al tiempo de concentración de la cuenca, y que la estimación
se realiza para un periodo de retorno de 100 años, las intensidades de la precipitación estimadas mediante el uso
de los coeficientes de duración según la fórmula de Grunsky se presenta en la Tabla 4-7.

<!-- INICIO TABLA 4-7 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- 24 Anexo N°2.7.1 Estudio de crecidas Estero Cuni -->

**Tabla 4-7: Tabla 4 6 Intensidades de precipitación estimadas para la cuenca estudiada**

| Periodo de retorno | Intensidad de las precipitaciones |
| --- | --- |
| 10 | 12,2 |
| 25 | 13,7 |
| 50 | 14,8 |
| 100 | 15,9 |

<!-- Estadísticas: 4 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Hydrus Ambiental, 2024. Finalmente, el caudal máximo instantáneo estimado en la cuenca de estudio utilizando la fórmula racional según periodo de retorno se presenta en la Tabla 4-8. El caudal de diseño considerado corresponde al de 100 años. -->
<!-- FIN TABLA 4-7 -->


Parque fotovoltaico Los Lagos
IM2SOLAR003.INF003.Rev0

24

Anexo N°2.7.1 Estudio de crecidas Estero Cuni

Tabla 4-7 Tabla 4 6 Intensidades de precipitación estimadas para la cuenca estudiada

|Periodo de retorno|Intensidad de las precipitaciones|
|---|---|
|10|12,2|
|25|13,7|
|50|14,8|
|100|15,9|

Fuente: Hydrus Ambiental, 2024.

Finalmente, el caudal máximo instantáneo estimado en la cuenca de estudio utilizando la fórmula racional según
periodo de retorno se presenta en la Tabla 4-8. El caudal de diseño considerado corresponde al de 100 años.

<!-- INICIO TABLA 4-8 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Fuente: Hydrus Ambiental, 2024. Finalmente, el caudal máximo instantáneo estimado en la cuenca de estudio utilizando la fórmula racional según periodo de retorno se presenta en la Tabla 4-8. El caudal de diseño considerado corresponde al de 100 años. -->

**Tabla 4-8: Caudales máximos estimados según cuenca en estudio y periodo de retorno**

| T (años) | Caudal máximo (m3/s) Método<br>racional |
| --- | --- |
| 10 | 3,9 |
| 25 | 4,9 |
| 50 | 5,9 |
| 100 | 6,6 |

<!-- Estadísticas: 4 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Hydrus Ambiental, 2024. Parque fotovoltaico Los Lagos IM2SOLAR003.INF003.Rev0 -->
<!-- FIN TABLA 4-8 -->


Tabla 4-8 Caudales máximos estimados según cuenca en estudio y periodo de retorno

|T (años)|Caudal máximo (m3/s) Método<br>racional|
|---|---|
|10|3,9|
|25|4,9|
|50|5,9|
|100|6,6|

Fuente: Hydrus Ambiental, 2024.

Parque fotovoltaico Los Lagos
IM2SOLAR003.INF003.Rev0

25

Anexo N°2.7.1 Estudio de crecidas Estero Cuni

4.4 Modelación hidráulica

La modelación hidráulica determina el comportamiento y características del flujo en todas sus secciones a lo largo
del estero en estudio considerando el caudal de diseño correspondiente a un periodo de retorno de 100 años y la
geometría de los cauces obtenida a partir de las curvas de nivel.

A continuación, se presentan los resultados de la simulación hidráulica del estero donde se identifica la superficie
de inundación. Luego, se presenta el detalle de la modelación hidráulica del cauce indicando los perfiles
transversales representativos y perfil longitudinal del flujo. Se destaca que, los archivos digitales de cartografía y
modelación HEC RAS se presentan en el Apéndice C, y los resultados numéricos de la modelación hidráulica de cada
cauce se presentan en el Apéndice D.

4.4.1 Superficie de inundación

La superficie de inundación asociada a la crecida de 100 años de periodo de retorno del Estero Cuni se presenta en
la Figura 4-4. Se observó que la superficie de inundación a 100 años de retorno no llegaría hasta el emplazamiento
de las obras del Proyecto.

Parque fotovoltaico Los Lagos
IM2SOLAR003.INF003.Rev0

26

Figura 4-4 Superficie de inundación estero en área de estudio

Fuente: Hydrus Ambiental, 2024.

Anexo N°2.7.1 Estudio de crecidas Estero Cuni

27

Parque fotovoltaico Los Lagos
IM2SOLAR003.INF003.Rev0

Anexo N°2.7.1 Estudio de crecidas Estero Cuni

4.4.2 Estero Cuni

La Figura 4-5 y Figura 4-6 presentan los resultados obtenidos de la simulación hidráulica en las secciones
transversales cercanas a las obras del Proyecto y perfil longitudinal del cauce para el caudal de diseño (T=100 años).
En el caso Figura 4-5 (a) se presenta el sector aguas arriba de las obras y la Figura 4-5 (b) presenta un sector donde
se ubican las obras del Proyecto.

Por otro lado, la tabla de resultados numéricos de la modelación hidráulica se presenta en el Apéndice D.

Figura 4-5 Resultados eje hidráulico en secciones transversales

(a)

(b)
Fuente: Hydrus Ambiental, 2024.

Figura 4-6 Resultados eje hidráulico en perfil longitudinal

Fuente: Hydrus Ambiental, 2024.

Parque fotovoltaico Los Lagos
IM2SOLAR003.INF003.Rev0

28

Anexo N°2.7.1 Estudio de crecidas Estero Cuni

5 CONCLUSIONES

El estudio realizado y presentado en este documento tuvo por objetivo el levantamiento de información Hidrológica
e Hidráulica necesaria que permita determinar el área de inundación a 100 años de periodo de retorno al estero
Cuni, localizado a 20 m aproximadamente al norte de las obras del Proyecto ubicado en la comuna de Los Lagos,
Región de Los Ríos

Los resultados del estudio hidrológico determinaron que el estero en estudio corresponde un cauce permanente. El
caudal de crecida fue estimado para diferentes periodos de retorno mediante el método de precipitaciónescorrentía denominado Método Racional, al validar los supuestos de uso para cuencas pequeñas. El caudal
estimado para 100 años de periodo de retorno fue de 6,6 m [3] /s. Se destaca que, los resultados obtenidos se
consideraron representativos y conservadores del área de estudio debido a la cantidad de información disponible
en las estaciones meteorológicas estudiadas, y cuyos cálculos fueron elaborados de acuerdo con las
recomendaciones presentadas en “Guías Metodológicas para presentación y revisión técnica de Proyectos de
Modificación de cauces naturales y artificiales” (DGA, 2016).

Los resultados del estudio hidráulico determinaron las condiciones de escurrimiento mediante el cálculo hidráulico

y mediante simulación hidráulica para cada sección del flujo determinando las superficies de inundación del cauce
en estudio. Se concluyó que superficie de inundación a 100 años de retorno no alcanza las obras del Proyecto.

6 REFERENCIAS

Dirección General de Aguas DGA, 2016. Guías Metodológicas para presentación y revisión técnica de Proyectos de
Modificación de cauces naturales y artificiales.

Dirección General de Aguas DGA, 1991. Precipitaciones máximas en 1, 2 y 3 días.

Dirección General de Aguas, DGA 1995. Manual del cálculo de crecidas y caudales mínimos en cuencas sin

información.

Ministerio de Obras Públicas, 2022. Manual de Carreteras Vol N°3.

Parque fotovoltaico Los Lagos
IM2SOLAR003.INF003.Rev0

29

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 3-1: Listado de estaciones meteorológicas**

| ID | Estación | Código DGA | Coordenadas UTM<br>WGS84 Huso 19H | Col5 | Altitud<br>(msnm) | Inicio<br>registro | Fin<br>registro | Cantidad de<br>años con<br>información |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ID | Estación | Código DGA | Norte (m) | Este (m) | Este (m) | Este (m) | Este (m) | Este (m) |
| 1 | Lago Riñihue | 10111002-8 | 5.594.216 | 718.105 | 120 | 01/03/1985 | --- | 36 |
| 2 | Huichaco | 10137002-K | 5.601.340 | 693.901 | 95 | 02/10/1994 | --- | 27 |
| 3 | Río Fui en desagüe Lago<br>Pirihue | 10100002-8 | 5.582.185 | 252.705 | 600 | 01/12/1926 | --- | 18 |
| 4 | Catamutun | 10141001-3 | 5.552.187 | 655.957 | 150 | 01/10/1997 | --- | 25 |
| 5 | Llancahue | 10123004-K | 5.586.594 | 655.803 | 70 | 01/09/1972 | --- | 48 |
| 6 | Valdivia (UAustral) | 10123006-6 | 5.589.357 | 650.280 | 10 | 01/01/1960 | --- | 19 |
| 7 | Pirihueico en Pirihueico | 10100004-4 | 5.559.328 | 269.570 | 600 | 01/05/1939 | --- | 48 |

**Tabla 4-1: Características geomorfológicas de la cuenca estudiada**

| ID | Cauce | Área (km2) | Elevación<br>media<br>(msnm) | Elevación<br>mínima<br>(msnm) | Elevación<br>máxima<br>(msnm) | Largo del<br>cauce<br>(km) | Pendiente<br>media del<br>cauce (%) | Pendiente<br>media de la<br>cuenca (%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Estero Cuni | 2.3 | 79 | 69 | 92 | 2 | 5 | 4,2 |

**Tabla 4-2: Principales estadígrafos de precipitaciones máximas anuales en 24 horas**

| ID | Estación | Años con<br>información | Mínimo<br>(mm) | Media<br>(mm) | Máximo<br>(mm) | Desv. Estándar<br>(mm) | Coef. Variación<br>(-) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Lago Riñihue | 36 | 51 | 84 | 126 | 18,6 | 0,22 |
| 2 | Huichaco | 27 | 39 | 61 | 93 | 13,2 | 0,22 |
| 3 | Río Fui en desagüe Lago<br>Pirihue | 18 | 70 | 118 | 184 | 31 | 0,26 |
| 4 | Catamutun | 25 | 15 | 89 | 151 | 30,7 | 0,34 |
| 5 | Llancahue | 48 | 49 | 77 | 121 | 18,7 | 0,24 |
| 6 | Valdivia | 19 | 51 | 89 | 155 | 27,6 | 0,31 |
| 7 | Pirihueico en Pirihueico | 48 | 38 | 97 | 203 | 30,9 | 0,32 |

**Tabla 4-3: Resultados Test Chi Cuadrado para bondad de ajuste a series de precipitación según estación**

| Distribución\Estación | Lago Riñihue | Huichaco | Río Fui en<br>desagüe<br>Lago Pirihue | Catamutun | Llancahue | Estación<br>Valdivia | Estación<br>Pirihueico en<br>Pirihueico |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Log-Normal | Aceptado | Aceptado | Aceptado | Rechazado | Aceptado | Aceptado | Aceptado |
| Pearson III | Aceptado | Aceptado | Aceptado | Aceptado | Aceptado | Aceptado | Aceptado |
| Log Pearson | Rechazado | Rechazado | Rechazado | Rechazado | Rechazado | Rechazado | Aceptado |
| Gumbel | Aceptado | Aceptado | Aceptado | Rechazado | Aceptado | Aceptado | Aceptado |

**Tabla 4-4: Precipitación máxima en 24 hrs según periodo de retorno y estación meteorológica (mm).**

| T<br>(años) | Lago Riñihue | Huichaco | Río Fui en<br>desagüe Lago<br>Pirihue | Catamutun | Llancahue | Valdivia | Pirihueico en<br>Pirihueico |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T <br>(años) | Dist Gumbel<br>(mm) | Dist Gumbel<br>(mm) | Dist Gumbel<br>(mm) | Dist Pearson III<br>(mm) | Dist Gumbel<br>(mm) | Dist Gumbel<br>(mm) | Dist Gumbel<br>(mm) |
| 5 | 99,8 | 72,6 | 147,2 | 115,2 | 91,8 | 115,6 | 123,2 |
| 10 | 112,8 | 81,5 | 169,3 | 126,9 | 104,1 | 135 | 142,7 |
| 25 | 127,6 | 92,9 | 197,6 | 138,6 | 119,6 | 160 | 168 |
| 50 | 139 | 101,3 | 218,6 | 145,9 | 131,1 | 178,5 | 186,9 |
| 100 | 150 | 109,7 | 239,4 | 152,1 | 142,5 | 196,9 | 205,6 |

**Tabla 4-5: Coeficiente de escorrentía estimados para la cuenca en estudio**

| Condición o Factor | Coeficiente de escorrentía (-) |
| --- | --- |
| Relieve | 0.14 |
| Infiltración | 0.08 |
| Cobertura Vegetal | 0.05 |
| Almacenamiento<br>Superficial | 0.05 |
| Coef. Escorrentía | 0.32 |
| Coef. Escorrentía<br>(100 años) | 0.4 |

**Tabla 4-6: Tiempo de concentración estimado**

| Método | Tiempo de concentración (hr) |
| --- | --- |
| _California Culverts Practice_ | 0.8 |
| Témez o Normas Españolas | 0.5 |
| Giandotti | 4.1 |
| Promedio | 1.8 |
