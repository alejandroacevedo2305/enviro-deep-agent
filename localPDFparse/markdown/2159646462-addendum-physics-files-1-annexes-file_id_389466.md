---
title: Sin título
author: Nasrim Butler
date: D:20240429184857-04'00'
language: es
type: general
pages: 35
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ANEXO 13 ACTUALIZACIÓN ESTUDIO DE INUNDACIÓN PROYECTO LA MOCHA SOLAR
-->

# ANEXO 13 ACTUALIZACIÓN ESTUDIO DE INUNDACIÓN PROYECTO LA MOCHA SOLAR

**ANEXO 13 • ACTUALIZACIÓN ESTUDIO DE INUNDACIÓN**

ADENDA - DECLARACIÓN IMPACTO AMBIENTAL

PROYECTO LA MOCHA SOLAR

**ÍNDICE DE CONTENIDOS**

**1.** **INTRODUCCIÓN ........................................................................................................ 1**

**2.** **ESTUDIO HIDRÁULICO ............................................................................................ 4**

2.1. A LCANCE .............................................................................................................. 4

2.2. M ETODOLOGÍA DE LA SIMULACIÓN HIDRÁULICA ........................................................ 5

_2.2.1._ _Modelización bidimensional del flujo de agua ............................................................. 5_

_2.2.2._ _Fundamentos de cálculo del modelo bidimensional Iber ............................................ 6_

_2.2.3._ _Ecuaciones .................................................................................................................. 7_

_2.2.4._ _Esquemas numéricos y malla de cálculo .................................................................... 8_

_2.2.5._ _Condiciones de contorno ............................................................................................. 9_

_2.2.6._ _Parámetros de entrada del modelo bidimensional de flujo ....................................... 10_

2.3. R ESULTADOS DE LOS MODELOS HIDRÁULICOS ....................................................... 19

_2.3.1._ _Río Larqui .................................................................................................................. 19_

_2.3.2._ _Estero Meco .............................................................................................................. 20_

_2.3.3._ _Cauce natural NN ...................................................................................................... 22_

_2.3.5._ _Estero Maule ............................................................................................................. 23_

_2.3.6._ _Estero Colton ............................................................................................................. 24_

_2.3.7._ _Estero Pitipiti .............................................................................................................. 25_

**3.** **CONCLUSIONES ..................................................................................................... 28**

**4.** **BIBLIOGRAFÍA ........................................................................................................ 31**

i

**ANEXO 13 • ACTUALIZACIÓN ESTUDIO DE INUNDACIÓN**

ADENDA - DECLARACIÓN IMPACTO AMBIENTAL

PROYECTO LA MOCHA SOLAR

**ÍNDICE DE FIGURAS**

F IGURA 1. R ELACIÓN ENTRE EL P ROYECTO Y LA RED HÍDRICA DE LOS CAUCES NATURALES ...... 3

F IGURA 2. A LCANCES DE LA MODELACIÓN HIDRÁULICA PARA LOS CAUCES NATURALES DEL

P ROYECTO .......................................................................................................................... 4

F IGURA 3. INTERRELACIÓN ENTRE MÓDULOS DE CÁLCULO DE I BER ......................................... 7

F IGURA 4. E JEMPLO DE EDICIÓN DE NODOS DE UNA MALLA ..................................................... 9

F IGURA 5. M ODELO DE E LEVACIÓN D IGITAL DE DETALLE DEL P ROYECTO .............................. 11

F IGURA 6. M ALLA NO ESTRUCTURADA UTILIZADA PARA EL P ROYECTO ................................... 15

F IGURA 7. C ONDICIONES HIDRODINÁMICAS AGUAS ARRIBA (INLET) Y ABAJO (OUTLET) DE LOS

MODELOS HIDRÁULICOS ..................................................................................................... 17

F IGURA 8. R ESULTADOS DEL MODELO HIDRÁULICO PARA PROFUNDIDAD OBTENIDO EN EL RÍO

L ARQUI ............................................................................................................................. 19

F IGURA 9. R ESULTADOS DEL MODELO HIDRÁULICO PARA PROFUNDIDAD OBTENIDO EN EL ESTERO

M ECO ............................................................................................................................... 20

F IGURA 10. R ESULTADOS DEL MODELO HIDRÁULICO OBTENIDO EN ZONA DE CRUCE PARA EL

ESTERO M ECO .................................................................................................................. 21

F IGURA 11. R ESULTADOS DEL MODELO HIDRÁULICO PARA PROFUNDIDAD OBTENIDO EN EL C AUCE

N ATURAL NN .................................................................................................................... 22

F IGURA 12. R ESULTADOS DEL MODELO HIDRÁULICO PARA PROFUNDIDAD OBTENIDO EN EL

ESTERO M AULE ................................................................................................................. 23

F IGURA 13. R ESULTADOS DEL MODELO HIDRÁULICO PARA PROFUNDIDAD OBTENIDO EN EL

ESTERO C OLTON ............................................................................................................... 24

F IGURA 14. R ESULTADOS DEL MODELO HIDRÁULICO PARA PROFUNDIDAD OBTENIDO EN EL

ESTERO P ITIPITI ................................................................................................................. 26

F IGURA 15. R ESULTADOS DEL MODELO HIDRÁULICO PARA VELOCIDAD DE FLUJO OBTENIDO EN EL

ESTERO P ITIPITI ................................................................................................................. 27

ii

**ANEXO 13 • ACTUALIZACIÓN ESTUDIO DE INUNDACIÓN**

ADENDA - DECLARACIÓN IMPACTO AMBIENTAL

PROYECTO LA MOCHA SOLAR

**ÍNDICE DE TABLAS**

T ABLA 1: V ALORES PARA EL CÁLCULO DE LA RUGOSIDAD MEDIANTE EL MÉTODO DE C OWAN ... 12

T ABLA 2: C OEFICIENTE DE RUGOSIDAD DE M ANNING DE LOS CAUCES NATURALES ESTUDIADOS

........................................................................................................................................ 14

T ABLA 3: C AUCE NATURAL Y CAUDAL DE ENTRADA EN EL MODELO ........................................ 16

iii

**ANEXO 13 • ACTUALIZACIÓN ESTUDIO DE INUNDACIÓN**

ADENDA - DECLARACIÓN IMPACTO AMBIENTAL

PROYECTO LA MOCHA SOLAR

**1.** **INTRODUCCIÓN**

El Proyecto “La Mocha Solar”, corresponde a un nuevo parque fotovoltaico, ubicándose su

área de generación a aproximadamente 15 kilómetros al surponiente de la ciudad de
Chillán. El Proyecto se ubicará entre las Comunas de Bulnes y San Ignacio, Provincia de
Diguillín, Región de Ñuble. Cabe destacar, que, el 98,5% del Proyecto se ubica en la
Comuna de Bulnes, mientras que el 1,5% restante se ubica en la comuna de San Ignacio.

El Proyecto generará energía limpia en base a energías renovables no convencionales
(ERNC), a través de la construcción de una central fotovoltaica de 160 MW AC.

El parque fotovoltaico estará constituido por hasta 274.000 paneles aproximadamente,
instalados con tecnología de seguidores de un eje. Considera la construcción de dos Líneas
Eléctricas de Transmisión (Líneas de Evacuación) de alta tensión (66 kV) de circuito simple.
Desde las Subestaciones Elevadoras, se transmitirán los 160 MW AC generados por el
Proyecto al Sistema Eléctrico Nacional (SEN) hacia la subestación Lucero y la futura
subestación Montenegro, ambas propiedades de Sistema de Transmisión del Sur S.A.

El acceso al Proyecto se realizará por un camino secundario de 1,82 km, el cual se conecta
con la Ruta N-59-Q, que sale por el sur de la ciudad de Chillán, por la cual se recorrerán 15

km aproximadamente hasta el acceso al Proyecto.

El Proyecto tendrá una vida útil de 40 años y se contempla la utilización de una superficie
aproximada de 341,90 hectáreas, considerando el total de las instalaciones y de las dos
líneas eléctricas de 6,51 km (hasta subestación Lucero) y 4,97 km (hasta subestación

Montenegro), respectivamente.

El presente estudio se ha realizado dada la eventual existencia de cauces en que las

crecidas puedan afectar potencialmente el funcionamiento de las instalaciones del Proyecto
Fotovoltaico La Mocha Solar. El objetivo corresponde a la evaluación de las zonas de riesgo

de inundación ante crecidas centenarias (TR 100 años) de los cauces naturales del entorno
del Proyecto, permitiendo determinar las restricciones para la posterior definición del Layout
y el emplazamiento de las estructuras de las líneas de transmisión eléctrica.

El Proyecto La Mocha Solar cuenta con una topografía de detalle por lo que se ha optado
por una modelación bidimensional para el análisis del comportamiento de los flujos de

1

**ANEXO 13 • ACTUALIZACIÓN ESTUDIO DE INUNDACIÓN**

ADENDA - DECLARACIÓN IMPACTO AMBIENTAL

PROYECTO LA MOCHA SOLAR

crecida. Es importante mencionar, que, el área de generación del Proyecto colinda al norte
con el río Larqui y al sur con estero Meco, mientras que en el centro se identificó un cauce

natural sin nombre (NN) que proviene del predio colindante y es aportante a un cauce

artificial (canal de desagüe) estudiado en el Anexo 8.9 de la DIA y actualizado en el Anexo
14 de la Adenda, definido como Canal 1. Además, se ha incorporado dentro del análisis, el

cauce natural que drena desde una laguna ubicada en el entorno del Proyecto hacia el río
Larqui, denominado como Cauce Derivado Laguna.

Por otro lado, la línea de transmisión eléctrica proyectada hacia la subestación Lucero
contempla el atravieso del estero Meco, estero Maule, estero Colton y estero Pitipiti [1],
mientras que, la proyectada hacia la subestación Montenegro no contempla el atravieso de
cauces naturales. De esta manera, el presente análisis bidimensional permitirá determinar
la extensión de la inundabilidad con mayor realismo en comparación a un modelo

unidimensional de los cauces naturales. Los resultados obtenidos han sido considerados

en la definición del área de generación y la ubicación de las estructuras de la línea de
transmisión. En la siguiente Figura se presenta la ubicación del Proyecto con respecto a los
cauces naturales considerados en el presente estudio de inundación.

1 El estero Pitipiti es conocido por la comunidad del entorno como estero Pite

2

**ANEXO 13 • ACTUALIZACIÓN ESTUDIO DE INUNDACIÓN**

ADENDA - DECLARACIÓN IMPACTO AMBIENTAL

PROYECTO LA MOCHA SOLAR

**Figura 1. Relación entre el Proyecto y la red hídrica de los cauces naturales**

3

**ANEXO 13 • ACTUALIZACIÓN ESTUDIO DE INUNDACIÓN**

ADENDA - DECLARACIÓN IMPACTO AMBIENTAL

PROYECTO LA MOCHA SOLAR

**2.** **ESTUDIO HIDRÁULICO**

**2.1. Alcance**

Se dispone de una topografía de detalle en el terreno donde será emplazado el Proyecto
La Mocha Solar. Para el presente estudio de inundabilidad se utilizará un Modelo de
Elevación Digital ( _DEM_, por sus siglas en inglés) de un levantamiento LiDAR realizado para
el Proyecto, tanto en su área de generación como para las líneas de transmisión, con una
resolución de 0,2 m (20 cm). Los límites perimetrales presentados en la siguiente Figura
definen los alcances de la modelación hidráulica para los cauces río Larqui y Cauce
Derivado Laguna, estero Meco, Cauce Natural sin nombre (NN), estero Maule, estero
Colton y estero Pitipiti, respectivamente. Cabe destacar, que, la modelación de detalle del
presente estudio se realiza para la situación topográfica actual del terreno.

**Figura 2. Alcances de la modelación hidráulica para los cauces naturales del Proyecto**

4

**ANEXO 13 • ACTUALIZACIÓN ESTUDIO DE INUNDACIÓN**

ADENDA - DECLARACIÓN IMPACTO AMBIENTAL

PROYECTO LA MOCHA SOLAR

**2.2. Metodología de la simulación hidráulica**

**2.2.1. Modelización bidimensional del flujo de agua**

La modelización matemática bidimensional del flujo de agua consiste en predecir los valores

que toman las variables hidráulicas (velocidad, calado, caudal, etc.) a partir de la resolución
mediante métodos numéricos de ecuaciones considerando una serie de hipótesis.

La observación de que en la realidad se encuentran muchas situaciones donde el flujo

parece ser efectivamente bidimensional (es decir, predominan las dimensiones horizontales
sobre las verticales) o donde el fenómeno es complejo y es difícil definir a priori los cauces
preferentes, para lo cual se han llevado al uso de ecuaciones y esquemas bidimensionales,

aprovechando la creciente capacidad y velocidad de los computadores modernos.

En la actualidad existe una variedad de herramientas que permiten obtener la resolución
del flujo de agua en lámina libre en 2 dimensiones. Algunas de las más consolidadas como
Mike-21, Tublow2D o Sobek utilizan esquemas en diferencias finitas, con las respectivas
limitaciones propias que se asocian a la flexibilidad de la malla y en el cálculo de las

soluciones con discontinuidades. Otros como Telemac2D, SMS o FLO-2D utilizan

elementos finitos que presentan mayor flexibilidad con arreglos de mallas no estructuradas.

La tendencia de los últimos años decanta hacia la metodología de los volúmenes finitos,
aprovechando importantes desarrollos que ha habido en las últimas décadas para las

ecuaciones someras con este tipo de esquemas. Algunas de las herramientas disponibles
y que utilizan volúmenes finitos son Infoworks, Guad2D, OpenFOAM, Iber, y las últimas
versiones de Mike-21 y HEC-RAS 2D (Bladé, _et al.,_ 2014).

El presente estudio contempla la utilización de la versión 3.1 del programa de modelización
hidráulica bidimensional Iber, software con el suficiente respaldo técnico y aceptado por la
Dirección General de Aguas (DGA), tal como lo manifiesta en su Guía Metodológica para
Presentación y Revisión Técnica de Proyectos de Modificación de Cauces Naturales y

Artificiales del 2016.

5

**ANEXO 13 • ACTUALIZACIÓN ESTUDIO DE INUNDACIÓN**

ADENDA - DECLARACIÓN IMPACTO AMBIENTAL

PROYECTO LA MOCHA SOLAR

**2.2.2. Fundamentos de cálculo del modelo bidimensional Iber**

Iber corresponde a un modelo matemático bidimensional, que incluye un módulo
hidrodinámico para la simulación de flujos de ríos, canales y cauces naturales, permitiendo
así el cálculo de avenidas e inundaciones y la delimitación de las zonas inundables. Este
Software fue desarrollado a partir de la colaboración del Grupo de Ingeniería del Agua y del
Medio Ambiente, GEAMA (Universidad da Coruña), Grupo de Ingeniería Matemática
(Universidad Santiago de Compostela), Instituto Flumen (Universitat Politècnica de
Catalunya y Centro Internacional de Métodos Numéricos en Ingeniería CIMNE), promovido
por el Centro de Estudios Hidrográficos del CEDEX y la Dirección General del Agua de

España.

El modelo numérico ha sido desarrollado de manera directa desde la administración pública
española en colaboración con las universidades y centros de investigación mencionados,
diseñado especialmente para resolver las necesidades técnicas específicas en estudios
hidrológicos e hidráulicos. Algunas de las aplicaciones actuales del Iber son:

 - Simulación del flujo en lámina libre en cauces naturales

 - Evaluación de zonas inundables

 - Cálculo hidráulico de canalizaciones

 - Cálculo hidráulico de redes de canales en lámina libre

 - Cálculo de corriente en estuarios

 - Cálculo de modelos turbulentos

 - Procesos de erosión y sedimentación por transporte de material granular

 - Modelización distribuida hidrológica

 - Calidad de las aguas y transporte de contaminantes

 - Eco-hidráulica y modelos de hábitat de peces

El Software Iber fue desarrollado a partir de 2 herramientas de modelación numérica
bidimensional ya existentes: Turbillón y CARPA, ambas con métodos de volúmenes finitos,
que fueron integrados en un único código ampliado con nuevas capacidades. Para resolver
las aplicaciones ya mencionadas, Iber integra distintos módulos de cálculos acoplados entre
sí. En la siguiente Figura se presenta la interrelación entre módulos de cálculo de Iber.

6

**ANEXO 13 • ACTUALIZACIÓN ESTUDIO DE INUNDACIÓN**

ADENDA - DECLARACIÓN IMPACTO AMBIENTAL

PROYECTO LA MOCHA SOLAR

**Figura 3. interrelación entre módulos de cálculo de Iber**

Fuente: https://www.iberaula.es

**2.2.3. Ecuaciones**

Las ecuaciones que resuelve el módulo hidrodinámico de Iber corresponden a las
ecuaciones de St. Venant bidimensionales, incorporando opcionalmente los efectos de la
turbulencia y rozamiento superficial por viento.

∂h

∂h

∂t [+ ∂hU] ∂x [x]

[x] + [∂hU] [y]

∂x

= 0
∂y

[∂]

∂y [(hU] [x] [U] [y] [) = −gh∂Z] ∂x [b]

[b]

∂x [+] [ ] [s,x]

[2] [∂]

2 ~~[)]~~ [ +] ∂y

∂h

∂h [∂]

∂t [(hU] [x] [) +]

[∂]

∂x [(hU] [x]

2 + g [h] [2]

[s,x]

 [−] []  [b,x]

[x] [∂]

∂x [) +]

[∂]

∂y [(v] [t] [h∂U] ∂y [x]

[x]

∂y [)]

[b,x]

[∂]
 [+]

[∂]

∂x [(v] [t] [h∂U] ∂x [x]

[b]

∂y [+] [ ]  [s,][y]

[s,][y]

 [−] []  [b,][y]

[2]

2 ~~[)]~~ [ = −gh∂Z] ∂y [b]

[∂]

∂y [(v] [t] [h∂U] ∂y [y]

[y]

∂y ~~[)]~~

∂ [∂]
∂t [(hU] [y] [) +] ∂x

[∂] [∂]

∂x [(hU] [x] [U] [y] [) +]

2

[∂]

∂y [(hU] [y]

2 + g [h] [2]

[y] [∂]

∂x ~~[)]~~ [ +]

[b,][y]

[∂]
 [+] ∂x

[∂]

∂x [(v] [t] [h∂U] ∂x [y]

En donde h corresponde al calado, U x, U y corresponden a las velocidades horizontales

promediadas en profundidad, g es la aceleración de la gravedad,  es la densidad del agua,

Z b es la cota de fondo,  s es la fricción en la superficie libre debida al rozamiento producido

por el viento,  b es la fricción debida al rozamiento del fondo y v t es la viscosidad turbulenta.

La fricción de fondo se evalúa mediante la fórmula de Manning como:

 b,x =  hg [n] [2] [U] h [4/3][x] [|U|] [2]

7

**ANEXO 13 • ACTUALIZACIÓN ESTUDIO DE INUNDACIÓN**

ADENDA - DECLARACIÓN IMPACTO AMBIENTAL

PROYECTO LA MOCHA SOLAR

 b,y =  hg [n] [2] [U] h [4/3][y] [|U|] [2]

Es importante mencionar, que, todas las funciones y parámetros que aparecen en las
ecuaciones hidrodinámicas bidimensionales (incluyendo coeficiente de Manning y

velocidad del viento) pueden imponerse de forma variable, tanto espacial como
temporalmente (Bladé, _et al.,_ 2006). Para el presente estudio no se ha considerado el efecto

del viento ni de la turbulencia en el flujo de agua.

**2.2.4. Esquemas numéricos y malla de cálculo**

Las ecuaciones de aguas someras se resuelven mediante el método de volúmenes finitos
para mallas bidimensionales no estructuradas. Los esquemas numéricos utilizados en Iber
son especialmente apropiados para la modelización de cambios de régimen y de frentes
seco-mojado (frentes de inundación). Los volúmenes finitos en las mallas no estructuradas
sirven para realizar la discretización del dominio espacial, admitiéndose las mallas mixtas

formadas por elementos triangulares y cuadrangulares. El flujo convectivo se discretiza
mediante esquemas descentrados de tipo Godunov. Cuando se trabaja con terrenos
complejos se discretiza de forma descentrada al término que incluye la pendiente de fondo
con el fin de evitar oscilaciones espurias de la lámina libre. El resto de los términos es
posible discretizarlos con un esquema centrado, incluidos los de la difusión turbulenta

(Bladé _et al.,_ 2014; Toro, 2001).

Dentro de los procesos que requieren mayor tiempo y esfuerzo a la hora de desarrollar un
estudio de simulación numérica del flujo en ríos, corresponde a la generación de la malla
de cálculo. Un río tiene una geometría irregular y la construcción de una malla eficiente no

es evidente. Es deseable que la malla sea irregular con el fin de minimizar el número de
elementos con transiciones suaves. Para ello son muy adecuados los métodos de mallado
basados en el error cordal (máxima distancia entre el terreno original y la malla). Por ello,
Iber incorpora capacidades de mallado como la creación de mallas estructuradas y no
estructuradas, de triángulos y de cuadriláteros, mediante el uso de diversos algoritmos de
mallado. Adicionalmente, se han desarrollado herramientas de creación y edición de mallas
que se adaptan a las necesidades de los estudios de hidráulica fluvial (Cea & Bladé, 2007).

En este sentido, Iber incorpora una herramienta que permita modificar la cota de los nodos
de los elementos de una malla a partir de una modelo digital del terreno ( _DEM_ ) en formato
ASCII (ver siguiente Figura).

8

**ANEXO 13 • ACTUALIZACIÓN ESTUDIO DE INUNDACIÓN**

ADENDA - DECLARACIÓN IMPACTO AMBIENTAL

PROYECTO LA MOCHA SOLAR

**Figura 4. Ejemplo de edición de nodos de una malla**

Fuente: _Bladé et al., (2014)_

**2.2.5. Condiciones de contorno**

El Software Iber distingue entre contornos cerrados, del tipo pared, y contornos abiertos por
los cuales entra y sale el agua del dominio de los cálculos. Según Bladé _et al._ (2014), en
los contornos cerrados se puede imponer o una condición de deslizamiento libre o una
condición de fricción de pared. Con la condición de deslizamiento libre se desprecia el
rozamiento generado por los contornos sobre el fluido. Si se considera relevante el efecto
del rozamiento generado por el contorno se debe utilizar una condición de contorno tipo

fricción. La velocidad tangencial a la pared puede expresarse como una función de la
velocidad de fricción de pared ( u ∗ ) y de la distancia a la pared como:

[u] [∗]

0,4 [Ln(Edu] v [∗]

|U| = [u] [∗]

v ~~[)]~~

Donde d es la distancia en perpendicular a la pared y E es un parámetro cuyo valor

depende de las características del flujo. Para el cálculo de E se consideran condiciones de

flujo turbulento liso, turbulento rugoso y transición entre turbulento liso y rugoso.

9

**ANEXO 13 • ACTUALIZACIÓN ESTUDIO DE INUNDACIÓN**

ADENDA - DECLARACIÓN IMPACTO AMBIENTAL

PROYECTO LA MOCHA SOLAR

Respecto a los contornos abiertos, se consideran diferentes alternativas en función del
régimen hidráulico en el contorno. En los contornos de entrada se fija el caudal de agua y
se asume que la dirección del flujo es perpendicular al contorno. En caso de que el flujo
entre en régimen supercrítico, se impone adicionalmente el calado. La distribución del
caudal unitario a lo largo del contorno se realiza de forma proporcional al calado en cada

punto de este, según la expresión q n = CH [5/3], donde C es una constante que asegura que

la integral del caudal unitario q n a lo largo del contorno considerado es igual al caudal total

de entrada. En los contornos de salida se impone el nivel de la lámina de agua en caso de
que se produzca un régimen subcrítico, mientras que no es necesario imponer ninguna
condición en el caso de que el régimen sea supercrítico. En los contornos de salida se
considera asimismo la posibilidad de introducir una relación de curva de gasto que defina
la relación entre la cota de la lámina de agua y el caudal específico desaguado en cada
punto del contorno (Bladé, _et al.,_ 2014).

**2.2.6. Parámetros de entrada del modelo bidimensional de flujo**

**2.2.6.1. Modelo de elevación digital (DEM)**

Se realizó un levantamiento topográfico de detalle para la zona de estudio del Proyecto con
el que se ha generado un Modelo de Elevación Digital ( _DEM_ ) de la situación topográfica
sobre la cual se trabajó (ver Figura 5). Esta situación comprende al menos 100 metros

aguas arriba y abajo de las intersecciones de los cauces con el Proyecto, permitiendo
generar una correcta modelación hidráulica. Con esto, es posible construir la malla
geométrica de cálculo del modelo hidráulico.

10

**ANEXO 13 • ACTUALIZACIÓN ESTUDIO DE INUNDACIÓN**

ADENDA - DECLARACIÓN IMPACTO AMBIENTAL

PROYECTO LA MOCHA SOLAR

**Figura 5. Modelo de Elevación Digital de detalle del Proyecto**

11

**ANEXO 13 • ACTUALIZACIÓN ESTUDIO DE INUNDACIÓN**

ADENDA - DECLARACIÓN IMPACTO AMBIENTAL

PROYECTO LA MOCHA SOLAR

**2.2.6.2. Rugosidad del terreno**

El coeficiente de rugosidad implementado para este estudio corresponde al utilizado en la

estimación de coeficiente de rugosidad recomendado en el libro “Hidráulica de Canales

Abiertos” de Ven Te Chow, según el método de Cowan. Dado la anterior, se presenta la
siguiente ecuación:

n= m∗(n 0 + n 1 + n 2 + n 3 + n 4 )

Donde:

 - m : Factor de corrección que incorpora el efecto de la sinuosidad del cauce o la

presencia de meandros.

 - n 0 : Rugosidad base asociado al material de lecho

 - n 1 : Rugosidad adicional debida a irregularidades de la superficie del perímetro

mojado a lo largo del tramo en estudio.

 - n 2 : Rugosidad adicional equivalente debida a variaciones de forma y de las

dimensiones de las secciones a lo largo del tramo en estudio.

 - n 3 : Rugosidad adicional equivalente debido a la existencia de obstrucciones en el

cauce.

 - n 4 : Rugosidad adicional equivalente debido a la presencia de vegetación.

El coeficiente de rugosidad deberá calcularse según la rugosidad de base y a lo observado

en terreno considerando los valores que se muestran en la siguiente Tabla.

**Tabla 1: Valores para el cálculo de la rugosidad mediante el método de Cowan**

<!-- INICIO TABLA 1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- El coeficiente de rugosidad deberá calcularse según la rugosidad de base y a lo observado en terreno considerando los valores que se muestran en la siguiente Tabla. -->

**Tabla 1: Valores para el cálculo de la rugosidad mediante el método de Cowan****

| Condiciones del canal | Col2 | Valor | Col4 |
| --- | --- | --- | --- |
| Material involucrado de<br>rugosidad base | Tierra | n0 | 0,020 |
| Material involucrado de<br>rugosidad base | Corte en roca | Corte en roca | 0,025 |
| Material involucrado de<br>rugosidad base | Grava fina | Grava fina | 0,024 |
| Material involucrado de<br>rugosidad base | Grava gruesa | Grava gruesa | 0,028 |
| Grado de irregularidad<br>perímetro mojado | Despreciable | n1 | 0,000 |
| Grado de irregularidad<br>perímetro mojado | Leve | Leve | 0,005 |
| Grado de irregularidad<br>perímetro mojado | Moderado | Moderado | 0,010 |
| Grado de irregularidad<br>perímetro mojado | Alto | Alto | 0,020 |

<!-- Estadísticas: 8 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- 12 **ANEXO 13 • ACTUALIZACIÓN ESTUDIO DE INUNDACIÓN** -->
<!-- FIN TABLA 1 -->


|Condiciones del canal|Col2|Valor|Col4|
|---|---|---|---|
|Material involucrado de<br>rugosidad base|Tierra|n0|0,020|
|Material involucrado de<br>rugosidad base|Corte en roca|Corte en roca|0,025|
|Material involucrado de<br>rugosidad base|Grava fina|Grava fina|0,024|
|Material involucrado de<br>rugosidad base|Grava gruesa|Grava gruesa|0,028|
|Grado de irregularidad<br>perímetro mojado|Despreciable|n1|0,000|
|Grado de irregularidad<br>perímetro mojado|Leve|Leve|0,005|
|Grado de irregularidad<br>perímetro mojado|Moderado|Moderado|0,010|
|Grado de irregularidad<br>perímetro mojado|Alto|Alto|0,020|

12

**ANEXO 13 • ACTUALIZACIÓN ESTUDIO DE INUNDACIÓN**

ADENDA - DECLARACIÓN IMPACTO AMBIENTAL

PROYECTO LA MOCHA SOLAR

|Condiciones del canal|Col2|Valor|Col4|
|---|---|---|---|
|Variaciones de las<br>secciones|Graduales|n2|0,000|
|Variaciones de las<br>secciones|Alternándose<br>ocasionalmente|Alternándose<br>ocasionalmente|0,005|
|Variaciones de las<br>secciones|Alternándose<br>frecuentemente|Alternándose<br>frecuentemente|0,010 - 0,015|
|Efecto relativo de las<br>obstrucciones|Despreciable|n3|0,000|
|Efecto relativo de las<br>obstrucciones|Leve|Leve|0,010 - 0,015|
|Efecto relativo de las<br>obstrucciones|Apreciable|Apreciable|0,020 - 0,030|
|Efecto relativo de las<br>obstrucciones|Alto|Alto|0,040 - 0,060|
|Densidad de vegetación|Baja|n4|0,005 - 0,010|
|Densidad de vegetación|Media|Media|0,010 - 0,025|
|Densidad de vegetación|Alta|Alta|0,025 - 0,050|
|Densidad de vegetación|Muy alta|Muy alta|0,050 - 0,100|
|Sinuosidad y frecuencia<br>de meandros|Leve|m|1,000|
|Sinuosidad y frecuencia<br>de meandros|Apreciable|Apreciable|1,150|
|Sinuosidad y frecuencia<br>de meandros|Alta|Alta|1,300|

En vista y considerando que los cauces en estudio presentan características similares en
sus secciones medias y las áreas de ribera corresponden a un entorno de plantaciones
forestales principalmente, y, además, en un contexto de estratos y vegetación de similares
características, es que los valores de Manning serán considerados de igual forma para ellos.
En la siguiente Tabla se detallan los parámetros que se adoptan a partir del método de
Cowan, estos valores, igualmente han sido comparados y se encuentran acorde a estudios
extraídos cercanos al Proyecto, y que actualmente han sido aprobados o están siendo
evaluados ambientalmente [2] .

2 Se revisaron los antecedentes de los Proyectos “Línea Eléctrica Montenegro-Lucero” y “Proyecto Santa
Graciela Solar”

13

**ANEXO 13 • ACTUALIZACIÓN ESTUDIO DE INUNDACIÓN**

ADENDA - DECLARACIÓN IMPACTO AMBIENTAL

PROYECTO LA MOCHA SOLAR

**Tabla 2: Coeficiente de rugosidad de Manning de los cauces naturales estudiados**

<!-- INICIO TABLA 2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- ADENDA - DECLARACIÓN IMPACTO AMBIENTAL PROYECTO LA MOCHA SOLAR -->

**Tabla 2: Coeficiente de rugosidad de Manning de los cauces naturales estudiados****

| Coeficiente | Río Larqui, Estero Meco, Estero<br>Maule y Cauce NN | Col3 | Col4 | Estero Colton y Estero Pitipiti | Col6 | Col7 | Cauce Derivado Laguna | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Coeficiente** | Cauce<br>Principal | Riberas | Observación | Cauce<br>Principal | Riberas | Observación | Cauce<br>Principal | Riberas | Observación |
| n0 | 0,02 | 0,02 | Tierra<br>uniforme | 0,02 | 0,02 | Tierra<br>uniforme | 0,02 | 0,02 | Tierra<br>uniforme |
| n1 | 0,015 | 0,015 | De moderado<br>a alto tanto en<br>cauce como<br>planicies | 0,00 | 0,000 | Despreciable<br>en cauce y<br>planicies | 0,00 | 0,015 | Despreciable<br>en cauce y<br>moderado en<br>planicies |
| n2 | 0,005 | 0,005 | Gradualmente<br>variable en<br>cauce y<br>planicies | 0,00 | 0,000 | Gradualmente<br>variable en<br>cauce y<br>planicies | 0,004 | 0,005 | Gradualmente<br>variable en<br>cauce y<br>planicies |
| n3 | 0,01 | 0,02 | Leve en<br>cauce y<br>planicies | 0,00 | 0,00 | Despreciable<br>en cauce y<br>planicies | 0,01 | 0,02 | Leve en<br>cauce y<br>planicies |
| n4 | 0,025 | 0,1 | Media en<br>cauce y muy<br>alta en<br>planicies<br>(plantaciones) | 0,015 | 0,02 | Media tanto<br>en cauce<br>como en<br>planicies | 0,01 | 0,1 | Media en<br>cauce y muy<br>alta en<br>planicies<br>(plantaciones) |
| m | 1,00 | 1,00 | Leve en<br>cauce y<br>planicies | 1,00 | 1,00 | Leve en<br>cauce y<br>planicies | 1,00 | 1,00 | Leve en<br>cauce y<br>planicies |
| **Coef.**<br>**Adoptado** | **0,075** | **0,16** | - | **0,035** | **0,040** | - | **0,044** | **0,16** | - |

<!-- Estadísticas: 8 filas, 10 columnas -->
<!-- Contexto posterior: -->
<!-- 14 **ANEXO 13 • ACTUALIZACIÓN ESTUDIO DE INUNDACIÓN** -->
<!-- FIN TABLA 2 -->


|Coeficiente|Río Larqui, Estero Meco, Estero<br>Maule y Cauce NN|Col3|Col4|Estero Colton y Estero Pitipiti|Col6|Col7|Cauce Derivado Laguna|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Coeficiente**|Cauce<br>Principal|Riberas|Observación|Cauce<br>Principal|Riberas|Observación|Cauce<br>Principal|Riberas|Observación|
|n0|0,02|0,02|Tierra<br>uniforme|0,02|0,02|Tierra<br>uniforme|0,02|0,02|Tierra<br>uniforme|
|n1|0,015|0,015|De moderado<br>a alto tanto en<br>cauce como<br>planicies|0,00|0,000|Despreciable<br>en cauce y<br>planicies|0,00|0,015|Despreciable<br>en cauce y<br>moderado en<br>planicies|
|n2|0,005|0,005|Gradualmente<br>variable en<br>cauce y<br>planicies|0,00|0,000|Gradualmente<br>variable en<br>cauce y<br>planicies|0,004|0,005|Gradualmente<br>variable en<br>cauce y<br>planicies|
|n3|0,01|0,02|Leve en<br>cauce y<br>planicies|0,00|0,00|Despreciable<br>en cauce y<br>planicies|0,01|0,02|Leve en<br>cauce y<br>planicies|
|n4|0,025|0,1|Media en<br>cauce y muy<br>alta en<br>planicies<br>(plantaciones)|0,015|0,02|Media tanto<br>en cauce<br>como en<br>planicies|0,01|0,1|Media en<br>cauce y muy<br>alta en<br>planicies<br>(plantaciones)|
|m|1,00|1,00|Leve en<br>cauce y<br>planicies|1,00|1,00|Leve en<br>cauce y<br>planicies|1,00|1,00|Leve en<br>cauce y<br>planicies|
|**Coef.**<br>**Adoptado**|**0,075**|**0,16**|-|**0,035**|**0,040**|-|**0,044**|**0,16**|-|

14

**ANEXO 13 • ACTUALIZACIÓN ESTUDIO DE INUNDACIÓN**

ADENDA - DECLARACIÓN IMPACTO AMBIENTAL

PROYECTO LA MOCHA SOLAR

**2.2.6.3. Malla de cálculo**

Se ha definido un mallado no estructurado de tipo triangular para el cálculo hidráulico
utilizando las herramientas disponibles en el Software Iber 3.1 en conjunto con el _DEM_ con
resolución de 20 cm. Se ha realizado un mallado de 5 metros para las zonas de inundación
y se definió un mallado de 2,5 metros para el eje principal del cauce. El mallado utilizado se

presenta en la siguiente Figura.

**Figura 6. Malla no estructurada utilizada para el Proyecto**

15

**ANEXO 13 • ACTUALIZACIÓN ESTUDIO DE INUNDACIÓN**

ADENDA - DECLARACIÓN IMPACTO AMBIENTAL

PROYECTO LA MOCHA SOLAR

**2.2.6.4. Condiciones hidrodinámicas**

La condición de contorno considerada para las simulaciones de los cauces aguas arriba fue
la del régimen crítico/subcrítico, el cual contempla un hidrograma constante, con caudales
máximos de crecida para T=100 años, obtenidos de acuerdo con lo presentado en el Anexo

8.7 de la DIA y actualizado en el Anexo 12 de la Adenda, referido a la “Caracterización

Hidrológica”. Es importante mencionar, que, de las metodologías utilizadas en la estimación
de caudales, se han considerado los caudales de periodo de retorno de 100 años más
elevados, como situación más desfavorable para el Proyecto. Esta consideración aplicando
un tiempo de simulación suficiente para que el flujo en el modelo se estabilice, es decir, que

el caudal que entra es igual al que sale, de manera que los resultados obtenidos sean
válidos. Las condiciones de contorno aguas arriba, correspondiente a los caudales con

periodo de retorno de 100 años que se ingresan al modelo (INLET) se presentan en la
siguiente Tabla, mientras que la ubicación de las condiciones de contorno de entrada y de

salida se presentan en la siguiente Figura.

**Tabla 3: Cauce natural y caudal de entrada en el modelo**

<!-- INICIO TABLA 3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- periodo de retorno de 100 años que se ingresan al modelo (INLET) se presentan en la siguiente Tabla, mientras que la ubicación de las condiciones de contorno de entrada y de salida se presentan en la siguiente Figura. -->

**Tabla 3: Cauce natural y caudal de entrada en el modelo****

| CAUCES | METODO | OLOGÍAS DGA | A (m3/s) | TRANSPOSICIÓN DE CUENCAS | CAUDAL ADOPTADO |
| --- | --- | --- | --- | --- | --- |
| **ESTUDIADOS** | **DGA-AC** | **Verni y**<br>**King**<br>**Modificado** | **Formula**<br>**racional** | **DE CUENCAS**<br>**(m3/s)** | **ADOPTADO**<br>**(m3/s)** |
| **Río Larqui** | 103,45 | 116,29 | 88,91 | 125,84 | **125,84** |
| **Estero Meco** | 97,50 | 110,22 | 82,80 | 117,02 | **117,02** |
| **Estero Maule** | 39,88 | 49,10 | 43,35 | 46,18 | **49,10** |
| **Estero Colton** | 116,26 | 129,24 | 96,02 | 137,45 | **137,45** |
| **Estero Pitipiti** | No Aplica | No Aplica | 15,94 | 8,72 | **15,94** |
| **Cauce Sin**<br>**Nombre (NN)** | No Aplica | No Aplica | 2,25 | 1,02 | **2,25** |
| **Cauce**<br>**Derivado**<br>**Laguna** | No Aplica | No Aplica | 0,71 | 0,23 | **0,71** |

<!-- Estadísticas: 8 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- 16 **ANEXO 13 • ACTUALIZACIÓN ESTUDIO DE INUNDACIÓN** -->
<!-- FIN TABLA 3 -->


|CAUCES|METODO|OLOGÍAS DGA|A (m3/s)|TRANSPOSICIÓN DE CUENCAS|CAUDAL ADOPTADO|
|---|---|---|---|---|---|
|**ESTUDIADOS**|**DGA-AC**|**Verni y**<br>**King**<br>**Modificado**|**Formula**<br>**racional**|**DE CUENCAS**<br>**(m3/s)**|**ADOPTADO**<br>**(m3/s)**|
|**Río Larqui**|103,45|116,29|88,91|125,84|**125,84**|
|**Estero Meco**|97,50|110,22|82,80|117,02|**117,02**|
|**Estero Maule**|39,88|49,10|43,35|46,18|**49,10**|
|**Estero Colton**|116,26|129,24|96,02|137,45|**137,45**|
|**Estero Pitipiti**|No Aplica|No Aplica|15,94|8,72|**15,94**|
|**Cauce Sin**<br>**Nombre (NN)**|No Aplica|No Aplica|2,25|1,02|**2,25**|
|**Cauce**<br>**Derivado**<br>**Laguna**|No Aplica|No Aplica|0,71|0,23|**0,71**|

16

**ANEXO 13 • ACTUALIZACIÓN ESTUDIO DE INUNDACIÓN**

ADENDA - DECLARACIÓN IMPACTO AMBIENTAL

PROYECTO LA MOCHA SOLAR

**Figura 7. Condiciones hidrodinámicas aguas arriba (INLET) y abajo (OUTLET) de los**

**modelos hidráulicos**

**2.2.6.5. Condiciones iniciales**

Se ha considerado que el flujo transcurre por un terreno inicialmente seco, asignando valor
cero a las condiciones iniciales 2D. Como límite seco-mojado se define el umbral para

considerar transferencia de caudal entre celdas adyacentes en un valor de 0,001 m.

17

**ANEXO 13 • ACTUALIZACIÓN ESTUDIO DE INUNDACIÓN**

ADENDA - DECLARACIÓN IMPACTO AMBIENTAL

PROYECTO LA MOCHA SOLAR

**2.2.6.6. Opciones de cálculo hidráulico**

Las opciones de cálculo establecidas en Iber para la modelación bidimensional han sido:

|Cálculo con<br>esquema<br>numérico|1er orden|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**Condición de**<br>**discretización**<br>**temporal CFL **|0,45|0,45|0,45|0,45|0,45|0,45|
|**Tiempo**<br>**máximo de**<br>**simulación **|7000 s|5000 s|3000 s|2000 s|2000|2000 s|
|**Intervalo de**<br>**resultados **|10 s|10 s|10 s|10 s|10 s|10 s|
|**Incremento de**<br>**tiempo**<br>**máximo **|1 s (por defecto Iber)|1 s (por defecto Iber)|1 s (por defecto Iber)|1 s (por defecto Iber)|1 s (por defecto Iber)|1 s (por defecto Iber)|
|**Método de**<br>**secado **|Por defecto|Por defecto|Por defecto|Por defecto|Por defecto|Por defecto|
|**Resultados a**<br>**obtener **|Calado, velocidad, mapa de máximo de estos, caudal específico,<br>número de Froude|Calado, velocidad, mapa de máximo de estos, caudal específico,<br>número de Froude|Calado, velocidad, mapa de máximo de estos, caudal específico,<br>número de Froude|Calado, velocidad, mapa de máximo de estos, caudal específico,<br>número de Froude|Calado, velocidad, mapa de máximo de estos, caudal específico,<br>número de Froude|Calado, velocidad, mapa de máximo de estos, caudal específico,<br>número de Froude|

18

**ANEXO 13 • ACTUALIZACIÓN ESTUDIO DE INUNDACIÓN**

ADENDA - DECLARACIÓN IMPACTO AMBIENTAL

PROYECTO LA MOCHA SOLAR

**2.3. Resultados de los modelos hidráulicos**

**2.3.1. Río Larqui y Cauce Derivado Laguna**

Los resultados del modelo hidráulico 2D realizado para el río Larqui y el Cauce Derivado de

la Laguna permitió ajustar el área construible, de tal manera, que, posteriormente en la
definición del Layout, no hubiese instalaciones sobre ninguno de estos cauces (ver la
siguiente Figura). En este sentido, según lo observado en terreno y de acuerdo con la
topografía de detalle de la zona con la que se cuenta, es posible observar que el río Larqui
se encuentra en una zona más baja con respecto al entorno, de aproximadamente 7 metros.
Respecto al Cauce Derivado Laguna, es preciso señalar que se ha ajustado el área de

paneles y el cerco perimetral del Proyecto, de modo que ninguna parte u obra se encuentre

dentro de sus llanuras de inundación.

**Figura 8. Resultados del modelo hidráulico para profundidad obtenido en el río Larqui**

19

**ANEXO 13 • ACTUALIZACIÓN ESTUDIO DE INUNDACIÓN**

ADENDA - DECLARACIÓN IMPACTO AMBIENTAL

PROYECTO LA MOCHA SOLAR

**2.3.2. Estero Meco**

Los resultados del modelo hidráulico 2D realizado para el estero Meco permitió ajustar el
área construible, de tal manera, que, posteriormente en la definición del Layout, no hubiese
instalaciones sobre el cauce (ver la siguiente Figura). En este sentido, según lo observado
en terreno y de acuerdo con la topografía de detalle de la zona con la que se cuenta, es
posible observar que el estero Meco se encuentra en una zona más baja con respecto al

entorno, en particular de los paneles fotovoltaicos, de aproximadamente 20 metros.

**Figura 9. Resultados del modelo hidráulico para profundidad obtenido en el estero Meco**

Adicionalmente, a partir de los resultados obtenidos, se definieron las estructuras de la línea
de transmisión que se proyectarán para poder realizar correctamente el cruce al estero

Meco. En este sentido, se proyectan como necesarias las torres reticuladas T1 y T2 de la

línea de transmisión TES-Lucero, de 24 metros de altura, las cuales se ubican a una

distancia de 291,65 metros entre sí, asegurando factible realizar el cruce correctamente. La

20

**ANEXO 13 • ACTUALIZACIÓN ESTUDIO DE INUNDACIÓN**

ADENDA - DECLARACIÓN IMPACTO AMBIENTAL

PROYECTO LA MOCHA SOLAR

topografía de la zona permite justificar la instalación de dichas estructuras, ubicadas en
cotas más elevadas con respecto a la estimación de la lámina de agua, de

aproximadamente 11 metros para la torre T1 y 5 metros para la torre T2, respectivamente.

**Figura 10. Resultados del modelo hidráulico obtenido en zona de cruce para el estero Meco**

21

**ANEXO 13 • ACTUALIZACIÓN ESTUDIO DE INUNDACIÓN**

ADENDA - DECLARACIÓN IMPACTO AMBIENTAL

PROYECTO LA MOCHA SOLAR

**2.3.3. Cauce natural NN**

En la siguiente Figura se presenta el resultado del modelo hidráulico 2D para el cauce

natural NN, donde es posible observar que el cerco perimetral del Proyecto se ha
proyectado respetando la libre circulación de este. Asimismo, es posible observar que un

camino del Proyecto atraviesa este cauce, para lo cual se presentan los antecedentes
necesarios para el otorgamiento del Permiso Ambiental Sectorial Mixto 156 en el Anexo 9.6

de la DIA, actualizado en el Anexo 18 de la Adenda.

**Figura 11. Resultados del modelo hidráulico para profundidad obtenido en el Cauce Natural**

**NN**

22

**ANEXO 13 • ACTUALIZACIÓN ESTUDIO DE INUNDACIÓN**

ADENDA - DECLARACIÓN IMPACTO AMBIENTAL

PROYECTO LA MOCHA SOLAR

**2.3.5. Estero Maule**

En la siguiente Figura se presenta el resultado del modelo hidráulico 2D para el estero
Maule, donde es posible observar que las estructuras de la línea eléctrica TES-Lucero, las
cuales, en esta sección, son del tipo poste de hormigón de 18 metros de altura, se ubican

fuera las zonas inundables obtenidas. En este sentido, es importante mencionar, que, las

estructuras P20, P21, P22 y P23 **no** se encuentran al interior de la zona inundable obtenida

de acuerdo con el resultado del modelo hidráulico.

**Figura 12. Resultados del modelo hidráulico para profundidad obtenido en el estero Maule**

23

**ANEXO 13 • ACTUALIZACIÓN ESTUDIO DE INUNDACIÓN**

ADENDA - DECLARACIÓN IMPACTO AMBIENTAL

PROYECTO LA MOCHA SOLAR

**2.3.6. Estero Colton**

En la siguiente Figura se presenta el resultado del modelo hidráulico 2D para el estero
Colton, donde es posible observar que las estructuras de la línea eléctrica TES-Lucero, las
cuales, en esta sección, son del tipo poste de hormigón de 18 metros de altura, se ubican

fuera las zonas inundables obtenidas. En este sentido, es importante mencionar, que, las

estructuras P34, P35 y P36 se ubican **fuera** de la zona inundable obtenida de acuerdo con

el resultado del modelo hidráulico.

**Figura 13. Resultados del modelo hidráulico para profundidad obtenido en el estero Colton**

24

**ANEXO 13 • ACTUALIZACIÓN ESTUDIO DE INUNDACIÓN**

ADENDA - DECLARACIÓN IMPACTO AMBIENTAL

PROYECTO LA MOCHA SOLAR

**2.3.7. Estero Pitipiti**

En las siguientes Figuras se presenta el resultado del modelo hidráulico 2D para el estero
Pitipiti junto con las estructuras de la línea eléctrica TES-Lucero, las cuales, en esta sección,
son del tipo poste de hormigón de 18 metros de altura. En este sentido, el poste P50 se
ubica en el límite del resultado del modelo hidráulico, donde se obtuvo una profundidad de
la lámina de inundación de 1,8 cm (0,018 m) (ver Figura 14) y una velocidad de flujo de 0,1
m/s (ver Figura 15), lo cual resulta poco significativo dadas las características constructivas
de la obra proyectada, la cual contempla su instalación con una profundidad de 3 metros,
asegurando de esta manera el correcto funcionamiento de la línea de transmisión y del
Proyecto. Por otro lado, el poste P51 se ubica en una zona **fuera** de la lámina de inundación
obtenida según el modelo hidráulico. Finalmente, es importante aclarar, que, el área de
servidumbre de estructura corresponde a un área estimada para la correcta instalación de
la misma, en la cual **no** se contempla la materialización de ninguna obra, y, además, **no** se

proyecta ninguna obra de cruce al estero Pitipiti por caminos de acceso a las estructuras.

25

**ANEXO 13 • ACTUALIZACIÓN ESTUDIO DE INUNDACIÓN**

ADENDA - DECLARACIÓN IMPACTO AMBIENTAL

PROYECTO LA MOCHA SOLAR

**Figura 14. Resultados del modelo hidráulico para profundidad obtenido en el estero Pitipiti**

26

**ANEXO 13 • ACTUALIZACIÓN ESTUDIO DE INUNDACIÓN**

ADENDA - DECLARACIÓN IMPACTO AMBIENTAL

PROYECTO LA MOCHA SOLAR

**Figura 15. Resultados del modelo hidráulico para velocidad de flujo obtenido en el estero**

**Pitipiti**

27

**ANEXO 13 • ACTUALIZACIÓN ESTUDIO DE INUNDACIÓN**

ADENDA - DECLARACIÓN IMPACTO AMBIENTAL

PROYECTO LA MOCHA SOLAR

**3.** **CONCLUSIONES**

El presente estudio de inundabilidad consideró los siete (7) cauces naturales que se
encuentran en el entorno del Proyecto, cuya modelación con un período de retorno de 100
años, permitió diseñar el Layout del área de generación y de las líneas de transmisión de

manera de no afectar el libre escurrimiento ni las zonas de inundación de los cauces. De

esta manera, y en relación con el área de generación, el Proyecto colinda al norte con el río
Larqui y al sur con el estero Meco, mientras que al oriente se identificó un cauce natural sin
nombre (NN), el cual ingresa al área de generación proveniente del predio colindante, y es
aportante a un cauce artificial estudiado en el Anexo 8.9 de la DIA y actualizado en el Anexo
14 de la Adenda, definido como Canal 1. Asimismo, se incluyó un Cauce Natural que deriva
desde una laguna identificada en el entorno del Proyecto, el cual es aportante del río Larqui,

denominado “Cauce Derivado Laguna”. Por otro lado, la línea de transmisión eléctrica (LTE)

propuesta en dirección sur (hacia la subestación Lucero) atraviesa al estero Meco, estero
Maule, estero Colton y estero Pitipiti.

Para la generación de los modelos hidráulicos se consideró un modelo de elevación digital
( _DEM_ ) obtenido a partir de un vuelo LiDAR con una resolución de detalle de 20 cm. Con la
topografía de detalle se generaron modelos hidráulicos 2D en el Software Iber, en su versión
3.1, que permiten simular de manera más precisa las láminas de inundación de los cauces

naturales con su respectivo calado y velocidad.

El tiempo de simulación dependió del cauce estudiado, de manera que el modelo hidráulico

alcanzara una estabilidad, es decir, que el caudal de ingreso fuese el mismo caudal de
salida. De esta manera, los cauces estudiados que abarcaban una mayor superficie, como
el río Larqui y el estero Meco, contemplaron tiempos de simulación mayores con respecto

a los cauces de la línea de transmisión que contemplaban superficies de simulación
menores, como el estero Maule, Colton y Pitipiti. En relación con el coeficiente de rugosidad
de Manning se consideró lo evaluado en terreno, así como lo propuesto en Proyectos
cercanos y que han sido evaluados o se encuentran en evaluación en el SEIA.

Los resultados obtenidos de los modelos hidráulicos para caudales con periodo de retorno
de 100 años en los cauces naturales, correspondientes a las láminas de inundación de
éstos, han sido considerados en todo momento en la definición del Layout del Proyecto, de
manera de poder ajustar el área construible a dichos resultados, y de manera de no
intervenir estos cauces. Asimismo, estos resultados se han considerado en la definición y

28

**ANEXO 13 • ACTUALIZACIÓN ESTUDIO DE INUNDACIÓN**

ADENDA - DECLARACIÓN IMPACTO AMBIENTAL

PROYECTO LA MOCHA SOLAR

disposición de las estructuras de la línea de transmisión, en particular la propuesta en

dirección sur.

En relación con los resultados obtenidos para los cauces naturales del entorno del área de
generación, y de acuerdo con lo observado en terreno, es posible afirmar que los cauces
del río Larqui, estero Meco y Cauce Natural NN se encuentran en zonas topográficamente
más bajas que donde se dispondrán los paneles, justificación de los resultados de las áreas

inundables obtenidas en los modelos. Asimismo, el ajuste realizado en Adenda al diseño
del Proyecto ha sido considerando los resultados obtenidos en el modelo hidráulico del
Cauce Derivado Laguna, teniendo en consideración las respectivas llanuras de inundación.
En este sentido, no se contemplan obras del área de generación, ya sean paneles solares,
centros de transformación o alguna otra sobre los cauces estudiados, salvo el atravieso vial
y eléctrico al oriente, el cual conectará la parte norte del Proyecto con la sur, atravesando
al cauce natural NN, para lo cual se presenta el respectivo PAS 156 en el Anexo 9.6 de la

DIA, actualizado en el Anexo 18 de la Adenda.

En relación con las líneas eléctricas del Proyecto, los cauces naturales estudiados y motivo
del presente documento tienen relación con la línea propuesta hacia la subestación Lucero
(TES-Lucero). En este sentido, las estructuras han sido dispuestas de manera de no
intervenir los cauces naturales y respetando las distancias de acuerdo con lo factible según
ingeniería. De norte a sur, el primer cauce al que se le contempla el atravieso aéreo

corresponde al estero Meco, para el cual se proyectan las estructuras torres T1 y T2, del
tipo reticuladas de 24 metros de altura. La topografía de la zona permite justificar la
instalación de dichas estructuras, ubicadas en cotas más elevadas que donde se identifica
la lámina de agua, considerando una altura 11 metros para la torre T1 y de 5 metros para

la torre T2 por sobre la lámina de agua. El segundo y tercer cauce corresponde al estero
Maule y Colton, respectivamente, para los cuales se proyectan estructuras del tipo poste
de hormigón de 18 metros de altura para el respectivo atravieso aéreo, ubicándose estas
estructuras fuera de las láminas de inundación. Por último, para el atravieso del estero
Pitipiti se proyectan estructuras del tipo poste de hormigón de 18 metros de altura,
ubicándose el poste P50 en el límite del área inundable, donde se estima una profundidad
de 1,8 cm y una velocidad de flujo de 0,1 m/s, no representando un riesgo para la correcta
instalación de ésta, y el correcto funcionamiento del parque.

29

**ANEXO 13 • ACTUALIZACIÓN ESTUDIO DE INUNDACIÓN**

ADENDA - DECLARACIÓN IMPACTO AMBIENTAL

PROYECTO LA MOCHA SOLAR

Finalmente, y en función de los resultados obtenidos y expuestos en el presente documento,
es posible afirmar que para el diseño del Layout del Proyecto La Mocha Solar, se ha

considerado en todo momento la red hídrica del entorno, así como las áreas inundables

para periodos de retorno de 100 años.

30

**ANEXO 13 • ACTUALIZACIÓN ESTUDIO DE INUNDACIÓN**

ADENDA - DECLARACIÓN IMPACTO AMBIENTAL

PROYECTO LA MOCHA SOLAR

**4.** **BIBLIOGRAFÍA**

Bladé, E., Cea, L., Corestein, G., Escolano, E., Puertas, J., Vásquez-Cendón, E., Dolz, J.,
Coll, A. (2014). Iber: Herramienta de simulación numérica del flujo en ríos. Revista
Internacional de Métodos Numéricos para Cálculo y Diseño de Ingeniería. Vol. 30. Núm. 1.
DOI: 10.1016/j.rimni.2012.07.004. [https://www.elsevier.es/pt-revista-revista-internacional-](https://www.elsevier.es/pt-revista-revista-internacional-metodos-numericos-calculo-338-articulo-iber-herramienta-simulacion-numerica-del-S0213131512000454)

[metodos-numericos-calculo-338-articulo-iber-herramienta-simulacion-numerica-del-](https://www.elsevier.es/pt-revista-revista-internacional-metodos-numericos-calculo-338-articulo-iber-herramienta-simulacion-numerica-del-S0213131512000454)

S0213131512000454

Bladé, E., Gómez-Valentín, M. (2006). Modelación del flujo en lámina libre sobre cauces
naturales. Análisis integrado en una y dos dimensiones. Monograph CIMNE No97.

Barcelona, España.

Cea, L. & Bladé, E. (2007). Modelización matemática en lecho fijo del flujo en ríos. Modelos

 1D y 2D en régimen permanente y variable. [en línea] [https://hidrojing.com/wp](https://hidrojing.com/wp-content/uploads/Bibliografia/17_Modelizacion%20matematica%20en%20lecho%20fijo%20de%20flujo%201D%20y%202D.pdf)

[content/uploads/Bibliografia/17_Modelizacion%20matematica%20en%20lecho%20fijo%20](https://hidrojing.com/wp-content/uploads/Bibliografia/17_Modelizacion%20matematica%20en%20lecho%20fijo%20de%20flujo%201D%20y%202D.pdf)

de%20flujo%201D%20y%202D.pdf

DGA (2016). Guía Metodológica para Presentación y Revisión Técnica de Proyectos de
Modificación de Cauces Naturales y Artificiales. [en línea]
[https://dga.mop.gob.cl/orientacionalpublico/guias/Guias%20para%20presentacion%20de](https://dga.mop.gob.cl/orientacionalpublico/guias/Guias%20para%20presentacion%20de%20solicitudes/Guia%20de%20Presentacion%20y%20Aprobacion%20de%20Proyectos%20de%20Modificacion%20de%20Cauces%20DIC%202016.pdf#page37)
[%20solicitudes/Guia%20de%20Presentacion%20y%20Aprobacion%20de%20Proyectos%](https://dga.mop.gob.cl/orientacionalpublico/guias/Guias%20para%20presentacion%20de%20solicitudes/Guia%20de%20Presentacion%20y%20Aprobacion%20de%20Proyectos%20de%20Modificacion%20de%20Cauces%20DIC%202016.pdf#page37)
20de%20Modificacion%20de%20Cauces%20DIC%202016.pdf#

Toro, E.F. (2001) Shock-Capturing Methods for Shallow Flows. John Wiley and Sons.

31