---
title: Sin título
author: Desconocido
date: D:20230718191018-04'00'
language: es
type: manual
pages: 48
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ANEXO 8.8 ESTUDIO DE AFORO EN CAUCES ARTIFICIALES
-->

# ANEXO 8.8 ESTUDIO DE AFORO EN CAUCES ARTIFICIALES

## DIA PROYECTO SOL DE LEÓN ANEXO 8.8 ESTUDIO DE AFORO EN CAUCES ARTIFICIALES ELABORADO PARA

[www.modeling.cl](http://www.modeling.cl/) [contacto@modeling.cl](mailto:contacto@modeling.cl)

SPHERA ENERGY MODELING

Tabla de Contenido

**1** **INTRODUCCIÓN ............................................................................................................ 5**

1.1 OBJETIVOS............................................................................................................. 6

1.2 ÁREA DE ESTUDIO ................................................................................................... 7

**2** **METODOLOGÍA ............................................................................................................. 8**

2.1 T OPOGRAFÍA ......................................................................................................... 8

2.2 M ÉTODO DE CÁLCULO HEC-RAS ........................................................................... 9

2.3 C OEFICIENTE DE RUGOSIDAD ............................................................................... 11

2.4 D ATOS GEOMÉTRICOS ......................................................................................... 13

2.5 C AUDALES M ODELADOS ...................................................................................... 13

2.6 C ONDICIONES DE B ORDE ..................................................................................... 14

2.7 E JE H IDRÁULICO Q UEBRADA ................................................................................ 14

**3** **RESULTADOS .............................................................................................................. 15**

3.1 HEC-RAS .......................................................................................................... 15

3.1.1 Canal 1 ................................................................................................................. 16
3.1.2 Canal 2 ................................................................................................................. 22
3.1.3 Canal 3 ................................................................................................................. 25
3.1.4 Canal 4 ................................................................................................................. 29
3.1.5 Canal 5 ................................................................................................................. 32
3.1.6 Canal 6 ................................................................................................................. 35
3.1.7 Canal 7 ................................................................................................................. 38
3.1.8 Canal 8 ................................................................................................................. 43

**4** **CONCLUSIONES ........................................................................................................... 46**

**5** **BIBLIOGRAFIA ............................................................................................................. 47**

**6** **APENDICES ................................................................................................................. 47**

2

Estudio de Aforo en Cauces Artificiales

DIA
PROYECTO SOL DE LEÓN

SPHERA ENERGY MODELING

Índice de Figuras

F IGURA 1. C ANALES A I NTERVENIR POR P ROYECTO S OL DE L EÓN ....................................... 6

F IGURA 2. C AUCES ARTIFICIALES A ESTUDIAR P ROYECTO S OL DE L EÓN .............................. 7

F IGURA 3. T OPOGRAFÍA C ANALES P ROYECTO ................................................................... 8

F IGURA 4. O RTOFOTOGRAFÍA C ANAL 1 E INTERACCIÓN CON C ANAL 2 Y 3 .......................... 12

F IGURA 5. I DENTIFICACIÓN DE PERFILES DE MODELACIÓN EN HEC-RAS C ANAL 1 .............. 16

F IGURA 6. I DENTIFICACIÓN FOTOGRÁFICA DE O BRA DE A TRAVIESO EN PERFIL 1219 DE
MODELACIÓN EN HEC-RAS C ANAL ................................................................................. 17

F IGURA 7. I DENTIFICACIÓN DE O BRA DE A TRAVIESO EN PERFIL 1219 DE MODELACIÓN EN HEC
RAS C ANAL 1 ................................................................................................................ 17

F IGURA 8. P ERFIL 115 SENSIBLE A DESBORDE C ANAL 1 ................................................... 18

F IGURA 9. E JE LONGITUDINAL C ANAL 1 ........................................................................... 18

F IGURA 10. I DENTIFICACIÓN DE PERFILES DE MODELACIÓN EN HEC-RAS C ANAL 2 ............ 22

F IGURA 11. P ERFIL 140 SENSIBLE A DESBORDE C ANAL 2 ................................................. 23

F IGURA 12. E JE LONGITUDINAL C ANAL 2.......................................................................... 23

F IGURA 13. I DENTIFICACIÓN DE PERFILES DE MODELACIÓN EN HEC-RAS C ANAL 3 ............ 25

F IGURA 14. P ERFIL 436 SENSIBLE A DESBORDE C ANAL 3 ................................................. 26

F IGURA 15. E JE LONGITUDINAL C ANAL 3.......................................................................... 26

F IGURA 16. I DENTIFICACIÓN DE PERFILES DE MODELACIÓN EN HEC-RAS C ANAL 4 ............ 29

F IGURA 17. P ERFIL 400 SENSIBLE A DESBORDE C ANAL 4 ................................................. 30

F IGURA 18. E JE LONGITUDINAL C ANAL 4.......................................................................... 30

F IGURA 19. I DENTIFICACIÓN DE PERFILES DE MODELACIÓN EN HEC-RAS C ANAL 5 ............ 32

F IGURA 20. P ERFIL 60 SENSIBLE A DESBORDE C ANAL 5 ................................................... 33

F IGURA 21. E JE LONGITUDINAL C ANAL 5.......................................................................... 33

F IGURA 22. I DENTIFICACIÓN DE PERFILES DE MODELACIÓN EN HEC-RAS C ANAL 6 ............ 35

F IGURA 23. P ERFIL 79 SENSIBLE A DESBORDE C ANAL 6 ................................................... 36

F IGURA 24. E JE LONGITUDINAL C ANAL 6.......................................................................... 36

F IGURA 25. I DENTIFICACIÓN DE PERFILES DE MODELACIÓN EN HEC-RAS C ANAL 7 ............ 38

F IGURA 26. P ERFIL 481 SENSIBLE A DESBORDE C ANAL 7 ................................................. 39

F IGURA 27. E JE LONGITUDINAL C ANAL 7.......................................................................... 39

F IGURA 28. I DENTIFICACIÓN DE PERFILES DE MODELACIÓN EN HEC-RAS C ANAL 8 ............ 43

F IGURA 29. P ERFIL 101 SENSIBLE A DESBORDE C ANAL 8 ................................................. 44

F IGURA 30. E JE LONGITUDINAL C ANAL 8.......................................................................... 44

3

Estudio de Aforo en Cauces Artificiales

DIA
PROYECTO SOL DE LEÓN

SPHERA ENERGY MODELING

Índice de Tablas

T ABLA 1. M ÉTODO DE C OWAN C AUCES A RTIFICIALES ...................................................... 12

T ABLA 2. C ONDICIONES DE BORDE EN QUEBRADAS PARA HEC-RAS ................................. 14

T ABLA 3. E JE H IDRÁULICO EN C ANAL 1 PARA UN CAUDAL DE 0,5 M 3/ S ............................... 19

T ABLA 4. E JE H IDRÁULICO EN C ANAL 2 PARA UN CAUDAL DE 0,29 M 3/ S ............................. 24

T ABLA 5. E JE H IDRÁULICO EN C ANAL 3 PARA UN CAUDAL DE 0,13 M 3/ S ............................. 27

T ABLA 6. E JE H IDRÁULICO EN C ANAL 4 PARA UN CAUDAL DE 0,03 M 3/ S .............................. 31

T ABLA 7. E JE H IDRÁULICO EN C ANAL 5 PARA UN CAUDAL DE 0,01 M 3/ S ............................. 34

T ABLA 8. E JE H IDRÁULICO EN C ANAL 6 PARA UN CAUDAL DE 0,1 M 3/ S ................................ 37

T ABLA 9. E JE H IDRÁULICO EN C ANAL 7 PARA UN CAUDAL DE 0,18 M 3/ S ............................. 40

T ABLA 10. E JE H IDRÁULICO EN C ANAL 8 PARA UN CAUDAL DE 0,9 M 3/ S .............................. 45

4

Estudio de Aforo en Cauces Artificiales

DIA
PROYECTO SOL DE LEÓN

SPHERA ENERGY MODELING

**1** **INTRODUCCIÓN**

El Proyecto “Sol de León”, corresponde a un nuevo parque fotovoltaico, ubicándose su área de

generación a aproximadamente 5 kilómetros al norponiente de la ciudad de Linares, Provincia de

Linares, Región del Maule.

El Proyecto generará energía limpia en base a energías renovables no convencionales (ERNC), a

través de la construcción de una al sur central fotovoltaica de 50 MW AC.

El parque fotovoltaico estará constituido por hasta 93.500 paneles aproximadamente, instalados

con tecnología de seguidores de un eje. Considera la construcción de una Línea Eléctrica de

Transmisión (Línea de Evacuación) de alta tensión (66 kV), la que llevará la energía generada hacia

la Subestación Linares, propiedad de CGE Transmisión S.A., donde será inyectada al Sistema

Eléctrico Nacional (SEN).

El acceso al Proyecto se realizará por un camino secundario denominado “Los Leones”, el cual se

conecta con la Ruta 5 al poniente de la ciudad de Linares, por el cual se recorrerán 350 m

aproximadamente hasta el acceso al Proyecto.

El Proyecto tendrá una vida útil de 40 años y se contempla la utilización de una superficie

aproximada de 107,4 hectáreas, considerando el total de las instalaciones y de la línea eléctrica de

4 km.

Conforme al emplazamiento de las partes y obras del Proyecto, se identifica que tanto el área de

generación como los caminos de la línea de transmisión eléctrica (LTE) del Proyecto se proyectan
sobre siete (7) canales de uso agrícolas existentes (cauces artificiales), por lo que en dichos canales

se requiere sustentar técnicamente la capacidad de porteo de tal manera cumplan con las
características físicas para portar un caudal de hasta 0,5 m3/s. Además, se estudia un canal cercano
al área de Proyecto con el fin de conocer su magnitud (Canal 7). Es en esta interrogante donde en

el presente estudio se compromete estimar numéricamente la capacidad de porteo de los canales,

de tal manera, que se justifique técnicamente las características de dichos canales y consigo la
aplicabilidad o no de un permiso ambiental sectorial mixto (PAS) N°156, para la actividad de

modificación de cauces en dichos cauces artificiales.

Para ello, se utiliza una combinación de modelos numéricos y herramientas de análisis hidráulico

para simular el comportamiento del agua en los cauces artificiales y determinar su capacidad de

porteo máximo.

En base a lo anterior, el presente estudio se basa en modelos computacionales del tipo hidráulico

que permiten simular caudales de porteo máximo de los canales agrícolas, mediante el software

HEC-RAS en su versión 6.3 y topografía de detalle, conforme lo establece la Dirección General de
Aguas (DGA) en su Resolución N°135 del 30 de enero del año 2020, guías de Permisos Ambientales

Sectoriales Mixto 156, y Guías Metodológicas para Proyectos de Modificación de Cauces.

El fin del presente documento es justificar como complemento al Anexo 8.7 Estudio de

Caracterización Hidrológica, la capacidad de porteo máxima de cada canal a modo de comprender

la magnitud de cada cauce artificial.

5

Estudio de Aforo en Cauces Artificiales

DIA
PROYECTO SOL DE LEÓN

SPHERA ENERGY MODELING

A modo de contextualizar la ubicación del área de Proyecto, a continuación, se presenta una figura

cartográfica que identifica la ubicación del área del Proyecto y los ocho (8) canales a estudiar los

cuales fueron identificados por cartografía IGM, visita a terreno, bibliografía e insumos topográficos

de tipo LIDAR y Ortofotografía. Es importante mencionar que el Canal 7 no será intervenido, solo se

estudia a modo de conocer su magnitud ya que se encuentra cercano al área de Proyecto y LTE.

**Figura 1. Canales a Intervenir por Proyecto Sol de León**

Fuente: Elaboración Propia, MODELING 2023.

**1.1** **OBJETIVOS**

Determinar la capacidad de porteo máximo de caudal de ocho (8) canales agrícolas identificados
dentro del Área de Influencia Hidrológica del Proyecto, de los cuales se pretenden intervenir solo
siete (7).

6

Estudio de Aforo en Cauces Artificiales

DIA
PROYECTO SOL DE LEÓN

SPHERA ENERGY MODELING

**1.2** **ÁREA DE ESTUDIO**

El Proyecto se emplazará en la Región del Maule, en la Provincia de Linares, Comuna de Linares,
aproximadamente a 5 km al norponiente de la localidad de Linares, su superficie comprenderá
aproximadamente 107,4 ha.

El área de estudio fue determinada y representada según el área del Proyecto, incluyendo área de
generación y área de línea de transmisión eléctrica, basado en la intervención de los siete (7) canales
y un canal extra (Canal 7) el cual se encuentra cercano al área de Proyecto.

A continuación, se presenta una figura donde se puede apreciar el área del Proyecto, la LTE y la
ubicación de los ocho (8) canales agrícolas identificados.

**Figura 2. Cauces artificiales a estudiar Proyecto Sol de León**

Fuente: Elaboración Propia, MODELING 2023.

Cabe destacar, que, solo el Canal 1 está identificado por cartografía IGM, mientras que, los demás
canales, fueron identificados por información topográfica, ortofotografía y por visita a terreno.

7

Estudio de Aforo en Cauces Artificiales

DIA
PROYECTO SOL DE LEÓN

SPHERA ENERGY MODELING

**2** **METODOLOGÍA**

Para el cálculo del comportamiento hidráulico de los canales, se utiliza el Programa Computacional
HEC-RAS 6.3 desarrollado por el Centro de Ingeniería Hidrológica de Texas, Estados Unidos
(Hydrologic Engineering Center, US Army Corps of Engineers), el cual corresponde a una
herramienta computacional versátil y útil para el cálculo de ejes hidráulicos en ríos y canales. Esta
herramienta se nutre con insumos topográficos, caudales en m [3] /s, condiciones de borde y
parámetros de rugosidad estimados según el tipo de cauce, estrato existente y vegetación entre
otros, los cuales se determinan mediante metodología de Cowan.

2.1 Topografía

La topografía por utilizar es la entregada por el titular del Proyecto, la cual presenta levantamiento
topográfico tipo LIDAR tanto en el área de Proyecto como la trayectoria de la Línea de transmisión
eléctrica (LTE), la cual permite demostrar las características del terreno con curvas de nivel cada 0,5
metros tal cual lo especifica DGA en sus documentos normativos, específicamente esta área abarca
la trayectoria de los canales en el punto de interacción con el proyecto, por lo que en ellos considera

una distancia lineal de modelación de 100 metros.

**Figura 3. Topografía Canales Proyecto**

Fuente: Elaboración Propia, MODELING 2023.

8

Estudio de Aforo en Cauces Artificiales

DIA
PROYECTO SOL DE LEÓN

SPHERA ENERGY MODELING

2.2 Método de cálculo HEC-RAS

Este modelo, opera tanto con flujo supercrítico como subcrítico (mixto). El algoritmo numérico se
basa en la solución de la ecuación de energía y momento, en forma unidimensional; con pérdidas
de energía debidas a la fricción, calculadas mediante la ecuación de Manning, y singularidades
originadas por cambios de sección.

Los principios de cálculo utilizados por este programa son los siguientes:

 - Caudales de máximas crecidas

 - Geometría del cauce

 - Pendiente media

 - Secciones transversales

 - Coeficiente de rugosidad de Manning

Aplicando la fórmula de Manning:

Q= [√i]

n [∗Ω∗ R]

2
3 **en** [m [3] /s]

Es decir,

Q∗n

~~√~~ i

2

= Ω∗R 3

Ecuación de balance de energía

El escurrimiento gradualmente variado se evalúa mediante la ecuación de balance de energía, es

decir:

B1 = B2 + PB 1 [m]

Donde:

 - B1 = Nivel de energía en la sección aguas arriba

 - B2 = Nivel de energía en la sección aguas abajo

 - P = Pérdidas de carga friccionales y singulares por cambios de sección

9

Estudio de Aforo en Cauces Artificiales

DIA
PROYECTO SOL DE LEÓN

SPHERA ENERGY MODELING

Pérdidas friccionales

Las pérdidas de carga friccionales corresponden a la siguiente relación:

Ω f = J∗L [m]

Donde:

 - L = Distancia entre las secciones 1 y 2

 - J = Pérdida de carga unitaria obtenida de la expresión de Manning

Pérdidas Singulares

Los cambios de sección generan pérdidas singulares que quedan determinadas por la siguiente

relación:

Ω s
= C∗(

ent2 −V sal2

−V sal

m
19,6 ~~)~~

V ent

2

Donde:

 - Vent = Velocidad en la sección aguas arriba

 - Vsal = Velocidad en la sección aguas abajo.

 - C = Coeficiente. C es igual a 0,1 para contracción y 0,3 para expansión

10

Estudio de Aforo en Cauces Artificiales

DIA
PROYECTO SOL DE LEÓN

SPHERA ENERGY MODELING

2.3 Coeficiente de rugosidad

En vista que el terreno es homogéneo, los valores de rugosidad de Manning para los canales se

determinan mediante el método de Cowan o multiparamétrico para la sección completa, el cual se

explica a continuación.

Valor de Manning en cauce principal método de Cowan

La expresión es la siguiente:

n= (n b + n 1 + n 2 + n 3 + n 4 ) ∗m
Donde:

 - n b = un valor de n para un cauce recto, uniforme y liso en función del material

de fondo.

 - n 1 = factor de corrección para considerar el efecto de las irregularidades

superficiales.

 - n 2 = un valor que añade las variaciones de forma y tamaño de la sección del

cauce.

 - n 3 = un valor que considera el efecto de las obstrucciones, tales como troncos,

tacos, cantos rodados, escombros, pilotes y muelles, perturba el flujo y aumenta la

rugosidad del cauce.

 - n 4 = un valor que incorpora el efecto de la presencia de vegetación y condiciones

del flujo. El efecto de la vegetación n4 depende de la profundidad del flujo y del

perímetro mojado cubierto por vegetación.

 - m = un factor que implementa la sinuosidad del cauce.

A continuación, se añade una Tabla que demuestra la estimación y cálculo del coeficiente de
rugosidad de Manning para los canales en estudio. En consideración con la visita a terreno y la
ortofoto se puede concluir que los canales agrícolas a estudiar presentan distintas características de
rugosidad por variaciones en cantidad de vegetación, uso y mantenimiento, por lo que se asumen
distintos coeficientes de Manning para los ocho (8) cauces modelados en HEC-RAS.

Es importante destacar que se utilizaron los siguientes coeficientes de rugosidad obtenidos

mediante el método de Cowan.

11

Estudio de Aforo en Cauces Artificiales

DIA
PROYECTO SOL DE LEÓN

SPHERA ENERGY MODELING

**Tabla 1. Método de Cowan Cauces Artificiales**

|CANAL|METODO DE COWAN|Col3|Col4|Col5|Col6|Col7|COEFICIENTE DE MANNING|
|---|---|---|---|---|---|---|---|
|**CANAL**|**Nb**|**n1**|**n2**|**n3**|**n4**|**m **|**n **|
|1|0.025|0.011|0.001|0.002|0.025|1|0.064|
|2|0.025|0.01|0.001|0.002|0.01|1|0.048|
|3|0.025|0.01|0.001|0.005|0.01|1|0.051|
|4|0.025|0.01|0.001|0.002|0.005|1|0.043|
|5|0.025|0.01|0.001|0.001|0.003|1|0.04|
|6|0.025|0.01|0.001|0.001|0.003|1|0.04|
|7|0.025|0.01|0.001|0.002|0.01|1|0.048|
|8|0.025|0.01|0.001|0.002|0.005|1|0.043|

Fuente: Elaboración propia en base a Guide for Selecting Manning's Roughness Coefficients for Natural
Channels and Flood Plains, United States Geological Survey Water-Supply Paper 2339, 1989, MODELING

2023.

Las elecciones de los datos representados en la Tabla anterior fueron asignados en función de la
ortofoto y visita a terreno a modo de establecer fehacientemente los coeficientes de rugosidad
empleados en la modelación. Se agrega la figura a continuación de Ortofotografía de Canal 1 en
interacción con el Canal 2 y Canal 3 como ejemplo de rugosidad.

**Figura 4. Ortofotografía Canal 1 e interacción con Canal 2 y 3**

12

Estudio de Aforo en Cauces Artificiales

DIA
PROYECTO SOL DE LEÓN

SPHERA ENERGY MODELING

Fuente: Elaboración propia en base a Ortofotografía, MODELING 2023.

2.4 Datos geométricos

Tomando como base la topografía entregada, se traza un eje central por la mediana del cauce en
análisis, a partir de este eje se confeccionan perfiles de manera transversales en hasta diez (10)
metros al ancho, y distanciados entre sí a una distancia de 20 metros y hasta 40 metros en
situaciones puntuales.

Luego de determinar los perfiles transversales, se registra la distancia entre perfiles, la que consta
de tres componentes:

 - Distancia central

 - Distancia del extremo izquierdo

 - Distancia del extremo derecho

En segundo lugar, se debe registrar el coeficiente de Manning adoptado y, en tercer lugar, se divide
cada sección en tres subsecciones, de acuerdo con los puntos definidos a modo de representar la
sección central del canal y sus riberas. Se adoptaron valores de 0,1 y 0,3 para los coeficientes de
contracción y expansión respectivamente, considerando que las transiciones entre secciones son
graduales.

2.5 Caudales Modelados

A modo de establecer la capacidad máxima de porteo en los canales en estudio, se modelan
distintos caudales iterados desde los 0,01 m [3] /s hasta los 0,5 m [3] /s, en caso de que los canales tengan
mayores capacidades serán considerado caudales mayores hasta encontrar su máxima capacidad.
Estos caudales fueron iterados progresivamente a modo de encontrar la cantidad máxima de porteo
previo al desborde de los canales demostrado por sus respectivos perfiles.

13

Estudio de Aforo en Cauces Artificiales

DIA
PROYECTO SOL DE LEÓN

SPHERA ENERGY MODELING

2.6 Condiciones de Borde

Se ingresó al modelo las condiciones de borde de aguas abajo y aguas arriba del tramo modelado,
considerando régimen normal y/o subcrítico (régimen mixto). Las cuales son condiciones de
pendiente del fondo de los cauces, estas fueron estimadas mediante la topografía entregada vía
modelo digital de terreno (MDT) y se presentan a continuación:

**Tabla 2. Condiciones de borde en quebradas para HEC-RAS**

|QUEBRADA|UPSTREAM (m/m)|DOWNSTREAM(m/m)|
|---|---|---|
|Canal 1|0.003|0.003|
|Canal 2|0.004|0.004|
|Canal 3|0.003|0.003|
|Canal 4|0.001|0.001|
|Canal 5|0.001|0.001|
|Canal 6|0.001|0.001|
|Canal 7|0.002|0.002|
|Canal 8|0.004|0.004|

Fuente: Elaboración propia, MODELING 2023.

2.7 Eje Hidráulico Quebrada

En este punto, se demuestra el resultado de los cálculos hidráulicos modelados que permiten
determinar, en condiciones actuales, el eje hidráulico máximo de los canales. El objetivo del cálculo
del eje hidráulico es, determinar los niveles del comportamiento del flujo para caudales
determinados que varíen hasta los 0,5 m [3] /s o superior, de esta manera determinar el máximo
porteo de caudal de los canales.

14

Estudio de Aforo en Cauces Artificiales

DIA
PROYECTO SOL DE LEÓN

SPHERA ENERGY MODELING

**3** **RESULTADOS**

3.1 HEC-RAS

En los resultados se muestra el caudal que permiten generar un desborde de cada canal luego de
distintas iteraciones entre caudales, a su vez se demuestra el caudal modelado de 0,5 m [3] /s
hipotético a modo de verificar el comportamiento de los perfiles de cada canal en dicho escenario,
los perfiles con resultados para todos los caudales simulados se encuentran adjuntos en el Apéndice
A del presente documento, y detallado para cada canal evaluado.

Para comprender de mejor manera, a continuación, se muestran los resultados de la modelación
hidráulica computacional HEC-RAS para cada canal de forma individual con sus caudales, mostrando
respectivamente:

 - Perfiles de modelación del canal.

 - Perfil sensible a desborde.

 - Perfil longitudinal del canal.

 - Cuadro de resultados hidráulicos del modelo con caudal máximo de cada canal.

Para entender de mejor manera los resultados de parámetros hidráulicos mostrados por cada perfil
modelado de los canales, en la Tabla de resultados hidráulicos del modelo se incluyen las siguientes
etiquetas que identifican lo descrito a continuación:

 - Q TOTAL : Caudal total modelado.

 - Perfil : Perfil en el cual se representan los resultados de parámetros

hidráulicos.

 - MIN CH EL : Cota de elevación mínima del canal en el perfil modelado.

 - W.S. ELEV : Cota de elevación de la superficie del escurrimiento o pelo de agua.

 - E.G. ELEV : Cota de elevación de la energía también conocido como Bernulli.

 - E.G. SLOPE : Pendiente entre el perfil modelado y el perfil siguiente aguas abajo.

 - VEL CHNL : Velocidad del escurrimiento en el perfil modelado.

 - FLOW AREA : Área hidráulica o área en corte del escurrimiento

 - TOP WIDTH : Ancho del escurrimiento

 - FROUDE # Chl : Numero de froude

Es importante destacar que los perfiles de modelos por cada canal están ubicados a una distancia
de 20 a 40 metros entre sí, por lo que su número identificador representa su ubicación respecto a
la distancia linean desde aguas agua abajo hasta aguas arriba, incrementando su valor identificador
respectivamente a la distancia longitudinal de cada canal. Vale decir, el numero identificador de
cada perfil representa la ubicación longitudinal del modelo hidráulico computacional.

15

Estudio de Aforo en Cauces Artificiales

DIA
PROYECTO SOL DE LEÓN

SPHERA ENERGY MODELING

3.1.1 Canal 1

Se detalla a continuación la identificación de los perfiles determinados en la modelación HEC-RAS
para el Canal 1, cada uno de estos perfiles demuestra junto a la Tabla de los resultados de los
parámetros hidráulicos de la modelación para el caudal máximo permitido físicamente.

En las siguientes figuras se demuestran los perfiles modelados en el Programa HEC-RAS con su
identificación respectiva por canal.

**Figura 5. Identificación de perfiles de modelación en HEC-RAS Canal 1**

Fuente: Elaboración propia, MODELING 2023.

Según lo identificado en terreno, se logra apreciar la existencia de una obra de cruce en torno a los
perfiles 1226 y 1200, por lo cual esta obra se agrega al modelo mediante el perfil 1219 y representar
un escenario real del comportamiento hidráulico del canal. A continuación, se aprecian dos figuras,
en la primera imagen ortofotografía y de terreno de la obra y consigo modelo computacional
considerado. Cabe destacar que se considera una obra tipo tubería de 0,33 m de diámetro interno
y materialidad de acero con baja mantención por lo que se considera un Manning en la obra de

0,024.

16

Estudio de Aforo en Cauces Artificiales

DIA
PROYECTO SOL DE LEÓN

SPHERA ENERGY MODELING

**Figura 6. Identificación fotográfica de Obra de Atravieso en perfil 1219 de modelación en HEC-RAS**

**Canal**

Fuente: Elaboración propia en base a HEC-RAS, MODELING 2023.

**Figura 7. Identificación de Obra de Atravieso en perfil 1219 de modelación en HEC-RAS Canal 1**

Fuente: Elaboración propia en base a HEC-RAS, MODELING 2023.

De todos los caudales modelados en el Canal 1, se demuestra que el límite de porteo máximo es
cercano a 0,5 m [3] /s, es por ello por lo que los resultados visuales en los perfiles hidráulicos se
mostraran con ese valor y también considera demostrar el efecto del flujo para un caudal de 0,7
m [3] /s y caudales menores (Apéndice A). A su vez, se comprende que el límite de porteo del Canal 1
se encuentra representado por varios perfiles del modelo, no obstante, en el Perfil identificado
como “115” se muestra una situación de desborde al simular un caudal de 0,7 m [3] /s, a continuación,
se representa dicho perfil.

17

Estudio de Aforo en Cauces Artificiales

DIA
PROYECTO SOL DE LEÓN

SPHERA ENERGY MODELING

**Figura 8. Perfil 115 sensible a desborde Canal 1**

Fuente: Elaboración propia, MODELING 2023.

A continuación, se muestra el perfil longitudinal del canal modelado, al igual que la figura anterior
se aprecia el caudal de porteo máximo y considerando un caudal extremo de 0,5m [3] /s.

**Figura 9. Eje longitudinal Canal 1**

Fuente: Elaboración propia, MODELING 2023.

A continuación, se muestran los resultados de la modelación entregada por el software HEC-RAS en
su versión 6.3. para el Canal 1, con un caudal de 0,5 m [3] /s. Los resultados se muestran en una Tabla

e incluyen resultados de parámetros hidráulicos como velocidad, ancho, calado, cota de fondo, cota

de superficie del agua, número de froude, entre otros.

18

Estudio de Aforo en Cauces Artificiales

DIA
PROYECTO SOL DE LEÓN

SPHERA ENERGY MODELING

**Tabla 3. Eje Hidráulico en Canal 1 para un caudal de 0,5 m3/s**

|River<br>Sta|Q Total|Min Ch<br>El|W.S.<br>Elev|E.G.<br>Elev|E.G.<br>Slope|Vel<br>Chnl|Flow<br>Area|Top<br>Width|Froude #<br>Chl|
|---|---|---|---|---|---|---|---|---|---|
||**(m3/s)**|**(m)**|**(m)**|**(m)**|**(m/m)**|**(m/s)**|**(m2)**|**(m)**||
|1500|0.5|131.14|131.75|131.76|0.006067|0.59|0.85|2.09|0.3|
|1480|0.5|131.09|131.64|131.65|0.005204|0.55|0.91|2.31|0.28|
|1460|0.5|130.96|131.4|131.45|0.027382|0.94|0.53|2.19|0.61|
|1440|0.5|130.54|131.14|131.16|0.008452|0.68|0.73|1.7|0.33|
|1420|0.5|130.29|131.08|131.09|0.001749|0.37|1.34|2.5|0.16|
|1400|0.5|130.36|131.06|131.07|0.00081|0.27|1.89|4.26|0.12|
|1380|0.5|130.33|131.06|131.06|0.000231|0.15|3.62|8.94|0.07|
|1360|0.5|130.18|131.05|131.05|0.000679|0.25|2.03|4.13|0.11|
|1340|0.5|130.19|131.04|131.04|0.00046|0.22|2.41|5.29|0.09|
|1320|0.5|130.21|131.02|131.03|0.000886|0.27|1.87|3.93|0.12|
|1300|0.5|129.99|131.01|131.01|0.000349|0.19|2.66|5.1|0.08|
|1280|0.5|129.93|131.01|131.01|0.000434|0.21|2.42|4.21|0.09|
|1260|0.5|129.9|131|131|0.000342|0.2|2.53|3.74|0.08|
|1240|0.5|129.7|130.99|131|0.000137|0.14|3.66|4.78|0.05|
|1226|0.5|129.72|130.99|130.99|0.000095|0.12|4.25|5.53|0.04|
|1219|Inl<br>Struct|||||||||
|1200|0.5|129.37|130.2|130.21|0.000843|0.28|1.8|3.2|0.12|
|1180|0.5|129.67|130.1|130.15|0.033768|1.03|0.48|2.06|0.68|
|1160|0.5|129.34|130.08|130.09|0.000858|0.27|1.82|3.52|0.12|
|1140|0.5|129.35|130.07|130.07|0.000626|0.25|2.13|4.73|0.11|
|1120|0.5|129.48|130.04|130.05|0.00258|0.4|1.24|3.12|0.2|
|1100|0.5|129.06|130.03|130.03|0.000322|0.19|2.62|4.11|0.08|
|1080|0.5|128.99|130.02|130.03|0.000276|0.19|2.69|3.61|0.07|
|1060|0.5|129.12|130.02|130.02|0.000416|0.21|2.34|3.54|0.08|
|1040|0.5|129.03|130.01|130.01|0.000149|0.15|3.48|5.73|0.05|
|1020|0.5|129.35|130|130.01|0.002571|0.39|1.28|3.36|0.2|
|1000|0.5|129.48|129.94|129.95|0.002912|0.4|1.25|3.61|0.22|
|980|0.5|129.29|129.66|129.77|0.080145|1.51|0.33|1.46|1.01|
|960|0.5|128.81|129.58|129.59|0.000617|0.24|2.11|4.02|0.1|
|940|0.5|128.81|129.57|129.58|0.000501|0.22|2.24|3.84|0.09|
|920|0.5|128.8|129.56|129.57|0.000456|0.22|2.29|3.99|0.09|
|900|0.5|128.79|129.55|129.55|0.00076|0.26|1.91|3.57|0.11|
|880|0.5|128.82|129.54|129.54|0.000765|0.25|1.96|3.97|0.12|
|860|0.5|128.81|129.53|129.53|0.0004|0.2|2.49|4.31|0.08|
|840|0.5|128.93|129.51|129.51|0.001719|0.34|1.47|3.78|0.17|

19

Estudio de Aforo en Cauces Artificiales

DIA
PROYECTO SOL DE LEÓN

SPHERA ENERGY MODELING

|River<br>Sta|Q Total|Min Ch<br>El|W.S.<br>Elev|E.G.<br>Elev|E.G.<br>Slope|Vel<br>Chnl|Flow<br>Area|Top<br>Width|Froude #<br>Chl|
|---|---|---|---|---|---|---|---|---|---|
||**(m3/s)**|**(m)**|**(m)**|**(m)**|**(m/m)**|**(m/s)**|**(m2)**|**(m)**||
|820|0.5|128.87|129.49|129.49|0.000847|0.26|1.91|3.93|0.12|
|800|0.5|128.9|129.47|129.47|0.000952|0.26|1.91|4.53|0.13|
|780|0.5|129.01|129.43|129.44|0.002893|0.37|1.35|4.51|0.22|
|760|0.5|128.87|129.41|129.41|0.000688|0.22|2.23|5.24|0.11|
|740|0.5|128.98|129.38|129.39|0.002428|0.35|1.47|5.04|0.2|
|720|0.5|128.93|129.32|129.33|0.00383|0.4|1.26|4.76|0.24|
|700|0.5|128.74|129.29|129.29|0.000918|0.25|2.03|5.2|0.13|
|680|0.5|128.74|129.27|129.27|0.001086|0.27|1.92|5.67|0.14|
|660|0.5|128.85|129.24|129.25|0.001904|0.31|1.61|5.1|0.18|
|640|0.5|128.74|129.21|129.21|0.001655|0.31|1.62|4.82|0.17|
|620|0.5|128.77|129.15|129.16|0.004421|0.45|1.1|3.63|0.26|
|600|0.5|128.72|128.93|128.97|0.034516|0.82|0.61|4.05|0.67|
|580|0.5|128.33|128.75|128.76|0.004621|0.47|1.05|3.31|0.27|
|560|0.5|128.15|128.69|128.7|0.002016|0.35|1.45|3.87|0.18|
|540|0.5|128.09|128.67|128.67|0.001112|0.29|1.74|4.13|0.14|
|520|0.5|128.04|128.63|128.64|0.001916|0.37|1.38|3.42|0.18|
|500|0.5|127.99|128.61|128.61|0.00096|0.28|1.82|4.13|0.13|
|480|0.5|128.01|128.59|128.59|0.001245|0.3|1.65|3.7|0.14|
|460|0.5|128|128.57|128.57|0.001007|0.28|1.79|4.08|0.13|
|440|0.5|128|128.54|128.55|0.001352|0.29|1.72|4.55|0.15|
|420|0.5|127.93|128.53|128.53|0.000618|0.22|2.26|4.97|0.1|
|400|0.5|128.04|128.51|128.51|0.001291|0.28|1.8|5.15|0.15|
|380|0.5|128.02|128.48|128.48|0.001615|0.31|1.64|4.63|0.16|
|360|0.5|127.86|128.45|128.45|0.001311|0.3|1.69|4.22|0.15|
|340|0.5|127.92|128.43|128.43|0.00105|0.26|1.9|4.78|0.13|
|320|0.5|127.89|128.4|128.4|0.001522|0.32|1.58|3.99|0.16|
|300|0.5|127.71|128.38|128.39|0.000596|0.23|2.2|4.43|0.1|
|280|0.5|127.89|128.35|128.36|0.003756|0.43|1.16|3.65|0.24|
|260|0.5|127.85|128.31|128.31|0.001497|0.29|1.73|5.07|0.16|
|240|0.5|127.68|128.3|128.3|0.000344|0.17|2.9|6.36|0.08|
|220|0.5|127.63|128.29|128.29|0.000574|0.21|2.36|5.53|0.1|
|200|0.5|127.58|128.28|128.28|0.000701|0.23|2.18|5.04|0.11|
|180|0.5|127.59|128.26|128.26|0.000782|0.24|2.05|4.64|0.12|
|160|0.5|127.7|128.24|128.25|0.000896|0.24|2.11|5.72|0.12|
|140|0.5|127.75|128.23|128.23|0.000811|0.21|2.46|8.85|0.12|
|115|0.5|127.61|128.21|128.21|0.000765|0.21|2.34|6.53|0.11|
|101|0.5|127.66|128.19|128.19|0.002118|0.3|1.67|6.07|0.18|
|80|0.5|127.84|128.08|128.1|0.015608|0.56|0.94|7.47|0.47|

20

Estudio de Aforo en Cauces Artificiales

DIA
PROYECTO SOL DE LEÓN

SPHERA ENERGY MODELING

|River<br>Sta|Q Total|Min Ch<br>El|W.S.<br>Elev|E.G.<br>Elev|E.G.<br>Slope|Vel<br>Chnl|Flow<br>Area|Top<br>Width|Froude #<br>Chl|
|---|---|---|---|---|---|---|---|---|---|
||**(m3/s)**|**(m)**|**(m)**|**(m)**|**(m/m)**|**(m/s)**|**(m2)**|**(m)**||
|55|0.5|127.55|128.01|128.02|0.001256|0.26|2.09|7.77|0.15|
|39|0.5|127.6|127.96|127.98|0.006587|0.49|1.02|4.41|0.31|
|21|0.5|127.36|127.89|127.9|0.003002|0.41|1.24|3.87|0.22|

Fuente: Elaboración propia, MODELING 2023.

21

Estudio de Aforo en Cauces Artificiales

DIA
PROYECTO SOL DE LEÓN

SPHERA ENERGY MODELING

3.1.2 Canal 2

Se detalla a continuación la identificación de los perfiles determinados en la modelación HEC-RAS
para el Canal 2, cada uno de estos perfiles se demuestra junto a la Tabla de los resultados de los
parámetros hidráulicos de la modelación para el caudal máximo permitido físicamente. Cabe
destacar, que, según lo identificado en terreno y según Sistema de Información Geográfica el Canal
2 nace desde el Canal 1 en un predio vecino ubicado al este y vierte en el mismo Canal 1 dentro del
área del Proyecto.

En las siguientes figuras se demuestran los perfiles modelados en el Programa HEC-RAS con su
identificación respectiva por canal.

**Figura 10. Identificación de perfiles de modelación en HEC-RAS Canal 2**

Fuente: Elaboración propia, MODELING 2023.

De todos los caudales modelados en el Canal 2, se demuestra que el límite de porteo máximo es
0,29 m [3] /s, es por ello por lo que los resultados visuales en los perfiles hidráulicos se mostraran con
ese valor y también considera demostrar el efecto del flujo para un caudal de 0,5 m [3] /s y caudales
menores (Apéndice A). A su vez, se comprende que el límite de porteo del Canal 2 se encuentra
representado en el Perfil identificado como “140” el cual se muestra a continuación.

22

Estudio de Aforo en Cauces Artificiales

DIA
PROYECTO SOL DE LEÓN

SPHERA ENERGY MODELING

**Figura 11. Perfil 140 sensible a desborde Canal 2**

Fuente: Elaboración propia, MODELING 2023.

A continuación, se muestra el perfil longitudinal del canal modelado, al igual que la figura anterior
se aprecia el caudal de porteo máximo y considerando un caudal extremo de 0,29 m [3] /s.

**Figura 12. Eje longitudinal Canal 2**

Fuente: Elaboración propia, MODELING 2023.

A continuación, se muestran los resultados de la modelación entregada por el software HEC-RAS en
su versión 6.3. para el Canal 2, con un caudal de 0,29 m [3] /s.

23

Estudio de Aforo en Cauces Artificiales

DIA
PROYECTO SOL DE LEÓN

SPHERA ENERGY MODELING

**Tabla 4. Eje Hidráulico en Canal 2 para un caudal de 0,29 m3/s**

|River<br>Sta|Q<br>Total|Min Ch<br>El|W.S.<br>Elev|E.G.<br>Elev|E.G.<br>Slope|Vel<br>Chnl|Flow<br>Area|Top<br>Width|Froude #<br>Chl|
|---|---|---|---|---|---|---|---|---|---|
||**(m3/s)**|**(m)**|**(m)**|**(m)**|**(m/m)**|**(m/s)**|**(m2)**|**(m)**||
|320|0.29|130.85|131.4|131.4|0.000845|0.34|1.13|6.09|0.16|
|300|0.29|130.88|131.34|131.36|0.006021|0.65|0.46|1.76|0.38|
|280|0.29|130.75|131.26|131.27|0.00344|0.53|0.6|2.28|0.3|
|260|0.29|130.69|131.18|131.2|0.004198|0.56|0.53|2.25|0.33|
|240|0.29|130.61|131.02|131.05|0.014112|0.82|0.36|1.77|0.57|
|220|0.29|130.44|130.97|130.97|0.001576|0.41|0.77|2.77|0.21|
|200|0.29|130.44|130.92|130.93|0.003189|0.54|0.61|2.3|0.29|
|180|0.29|130.42|130.83|130.85|0.005752|0.62|0.49|2.52|0.39|
|160|0.29|130.21|130.79|130.8|0.001053|0.37|0.93|3.49|0.18|
|140|0.29|130.45|130.68|130.73|0.03304|1.08|0.29|2.92|0.87|
|120|0.29|130.01|130.52|130.53|0.002461|0.48|0.65|2.13|0.26|
|100|0.29|130.01|130.48|130.49|0.001946|0.44|0.75|2.94|0.24|
|80|0.29|129.87|130.44|130.45|0.001861|0.43|0.71|2.64|0.23|
|60|0.29|129.95|130.37|130.39|0.005589|0.63|0.49|2.41|0.38|
|40|0.29|129.81|130.25|130.27|0.006031|0.67|0.45|1.79|0.39|
|20|0.29|129.71|130.16|130.17|0.004005|0.57|0.55|2.26|0.33|

Fuente: Elaboración propia, MODELING 2023.

24

Estudio de Aforo en Cauces Artificiales

DIA
PROYECTO SOL DE LEÓN

SPHERA ENERGY MODELING

3.1.3 Canal 3

Se detalla a continuación la identificación de los perfiles determinados en la modelación HEC-RAS
para el Canal 3, cada uno de estos perfiles demuestra junto a la Tabla resultados los parámetros
hidráulicos de la modelación para el caudal máximo permitido físicamente.

Es importante destacar que el Canal 3 nace desde el Canal1 y descarga en el mismo Canal 1 por lo
que se fundamenta que la utilización de este solo ocurre en el predio del área del Proyecto, es por
esto por lo que no afecta a terceros su modificación o intervención.

En las siguientes figuras se demuestran los perfiles modelados en el Programa HEC-RAS con su
identificación respectiva por canal.

**Figura 13. Identificación de perfiles de modelación en HEC-RAS Canal 3**

Fuente: Elaboración propia, MODELING 2023.

De todos los caudales modelados en el Canal 3, se demuestra que el caudal de desborde es 0,13
m [3] /s, es por ello por lo que los resultados visuales en los perfiles hidráulicos se mostraran con ese
valor y también considera demostrar el efecto del flujo para un caudal de 0,5 m [3] /s y menores
(Apéndice A). A su vez, se comprende que el límite de porteo del Canal 3 se encuentra representado

en el Perfil identificado como “436” el cual se muestra a continuación.

25

Estudio de Aforo en Cauces Artificiales

DIA
PROYECTO SOL DE LEÓN

SPHERA ENERGY MODELING

**Figura 14. Perfil 436 sensible a desborde Canal 3**

Fuente: Elaboración propia, MODELING 2023.

A continuación, se muestra el perfil longitudinal del canal modelado, al igual que la figura anterior
se aprecia el caudal de desborde y considerando un caudal extremo de 0,13 m [3] /s.

**Figura 15. Eje longitudinal Canal 3**

Fuente: Elaboración propia, MODELING 2022.

A continuación, se muestran los resultados de la modelación entregada por el software HEC-RAS en
su versión 6.3. para el Canal 3, con un caudal de 0,13 m [3] /s.

26

Estudio de Aforo en Cauces Artificiales

DIA
PROYECTO SOL DE LEÓN

SPHERA ENERGY MODELING

**Tabla 5. Eje Hidráulico en Canal 3 para un caudal de 0,13 m3/s**

|River<br>Sta|Q<br>Total|Min Ch<br>El|W.S.<br>Elev|E.G.<br>Elev|E.G.<br>Slope|Vel<br>Chnl|Flow<br>Area|Top<br>Width|Froude #<br>Chl|
|---|---|---|---|---|---|---|---|---|---|
||**(m3/s)**|**(m)**|**(m)**|**(m)**|**(m/m)**|**(m/s)**|**(m2)**|**(m)**||
|860|0.13|129.3|129.68|129.68|0.002462|0.33|0.4|1.92|0.23|
|840|0.13|129.37|129.58|129.6|0.009324|0.5|0.27|2.14|0.43|
|820|0.13|129.19|129.5|129.51|0.002558|0.33|0.39|1.91|0.23|
|803|0.13|129.14|129.32|129.38|0.05994|1.08|0.12|1.05|1.02|
|720|0.13|128.81|129.29|129.29|0.000172|0.12|1.14|4.36|0.07|
|700|0.13|129.03|129.25|129.28|0.021428|0.75|0.17|1.21|0.63|
|680|0.13|128.8|129.22|129.22|0.000928|0.23|0.56|2.33|0.15|
|640|0.13|128.86|129.13|129.14|0.006479|0.47|0.28|1.66|0.36|
|620|0.13|128.7|129.1|129.1|0.000939|0.22|0.59|2.55|0.15|
|600|0.13|128.49|129.09|129.09|0.000173|0.13|1.11|3.59|0.07|
|580|0.13|128.6|129.09|129.09|0.000413|0.18|0.74|2.58|0.1|
|560|0.13|128.75|129.08|129.08|0.000527|0.17|0.79|4.09|0.12|
|540|0.13|128.65|129.06|129.07|0.000664|0.21|0.64|2.66|0.13|
|519|0.13|128.83|129.01|129.03|0.018697|0.61|0.22|2.41|0.59|
|500|0.13|128.29|129.01|129.01|0.000148|0.12|1.12|3.35|0.06|
|480|0.13|128.36|129.01|129.01|0.000183|0.13|1.02|3.06|0.07|
|460|0.13|128.5|129|129|0.000325|0.15|0.87|3.29|0.09|
|436|0.13|128.64|128.99|128.99|0.000421|0.16|0.91|5|0.1|
|420|0.13|128.76|128.91|128.97|0.058667|1.01|0.13|1.25|1.01|
|400|0.13|128.36|128.7|128.71|0.003767|0.39|0.33|1.59|0.28|
|380|0.13|128.22|128.55|128.57|0.015755|0.67|0.19|1.21|0.53|
|360|0.13|128.11|128.46|128.46|0.002491|0.32|0.41|2.03|0.23|
|340|0.13|127.93|128.43|128.43|0.000825|0.22|0.6|2.33|0.14|
|320|0.13|128.01|128.4|128.4|0.003603|0.38|0.34|1.71|0.27|
|300|0.13|128.01|128.35|128.35|0.002018|0.29|0.45|2.46|0.21|
|280|0.13|127.92|128.32|128.33|0.00079|0.2|0.64|2.9|0.13|
|260|0.13|127.97|128.28|128.29|0.00826|0.49|0.26|1.7|0.4|
|240|0.13|127.76|128.22|128.23|0.00144|0.26|0.51|2.31|0.18|
|220|0.13|127.82|128.2|128.21|0.000836|0.24|0.59|2.83|0.14|
|200|0.13|127.78|128.19|128.19|0.000408|0.17|0.8|3.53|0.1|
|186|0.13|127.72|128.19|128.19|0.000407|0.16|0.8|3.16|0.1|
|160|0.13|127.85|128.17|128.17|0.001853|0.27|0.49|2.71|0.2|
|140|0.13|127.75|128.13|128.13|0.002087|0.29|0.45|2.25|0.21|
|120|0.13|127.78|128.1|128.1|0.000853|0.2|0.64|3.19|0.14|
|102|0.13|127.79|128.07|128.08|0.002589|0.3|0.43|2.83|0.24|
|79|0.13|127.78|128.03|128.04|0.001451|0.24|0.55|3.21|0.18|

27

Estudio de Aforo en Cauces Artificiales

DIA
PROYECTO SOL DE LEÓN

SPHERA ENERGY MODELING

|River<br>Sta|Q<br>Total|Min Ch<br>El|W.S.<br>Elev|E.G.<br>Elev|E.G.<br>Slope|Vel<br>Chnl|Flow<br>Area|Top<br>Width|Froude #<br>Chl|
|---|---|---|---|---|---|---|---|---|---|
||**(m3/s)**|**(m)**|**(m)**|**(m)**|**(m/m)**|**(m/s)**|**(m2)**|**(m)**||
|62|0.13|127.8|127.98|127.99|0.006298|0.38|0.34|2.71|0.35|
|40|0.13|127.61|127.93|127.94|0.001209|0.23|0.57|2.88|0.16|
|21|0.13|127.63|127.9|127.9|0.003001|0.33|0.4|2.39|0.25|

Fuente: Elaboración propia, MODELING 2022.

28

Estudio de Aforo en Cauces Artificiales

DIA
PROYECTO SOL DE LEÓN

SPHERA ENERGY MODELING

3.1.4 Canal 4

Se detalla a continuación la identificación de los perfiles determinados en la modelación HEC-RAS
para el Canal 4, cada uno de estos perfiles demuestra junto a la Tabla resultados los parámetros
hidráulicos de la modelación para el caudal máximo permitido físicamente.

El Canal 4 tiene su origen al Oeste en un cauce artificial en el límite del área de generación del
Proyecto, el cual desemboca en el Canal 1, por lo que su intervención o modificación no afectaría a

terceros.

En las siguientes figuras se demuestran los perfiles modelados en el Programa HEC-RAS con su
identificación respectiva por canal.

**Figura 16. Identificación de perfiles de modelación en HEC-RAS Canal 4**

Fuente: Elaboración propia, MODELING 2023.

De todos los caudales modelados en el Canal 4, se demuestra que el límite de porteo máximo es
0,03 m [3] /s, es por ello por lo que los resultados visuales en los perfiles hidráulicos se mostraran con
ese valor y también considera demostrar el efecto del flujo para un caudal de 0,5 m [3] /s (Apéndice
A). A su vez, se comprende que el límite de porteo del Canal 4 se encuentra representado en el Perfil

identificado como “400” el cual se muestra a continuación.

29

Estudio de Aforo en Cauces Artificiales

DIA
PROYECTO SOL DE LEÓN

**Figura 17. Perfil 400 sensible a desborde Canal 4**

Fuente: Elaboración propia, MODELING 2023.

A continuación, se muestra el perfil longitudinal del canal modelado, al igual que la figura anterior
se aprecia el caudal de porteo máximo y considerando un caudal extremo de 0,03m [3] /s.

**Figura 18. Eje longitudinal Canal 4**

Fuente: Elaboración propia, MODELING 2023.

A continuación, se muestran los resultados de la modelación entregada por el software HEC-RAS en
su versión 6.3 para el Canal 4, con un caudal de 0,03 m [3] /s.

30

Estudio de Aforo en Cauces Artificiales

DIA
PROYECTO SOL DE LEÓN

SPHERA ENERGY MODELING

**Tabla 6. Eje Hidráulico en Canal 4 para un caudal de 0,03m3/s**

|River<br>Sta|Q<br>Total|Min Ch<br>El|W.S.<br>Elev|E.G.<br>Elev|E.G.<br>Slope|Vel<br>Chnl|Flow<br>Area|Top<br>Width|Froude #<br>Chl|
|---|---|---|---|---|---|---|---|---|---|
||**(m3/s)**|**(m)**|**(m)**|**(m)**|**(m/m)**|**(m/s)**|**(m2)**|**(m)**||
|420|0.03|129.32|129.89|129.89|0.000006|0.03|1.22|4.78|0.01|
|400|0.03|129.29|129.89|129.89|0.000005|0.03|1.11|3.15|0.01|
|385|0.03|129.35|129.89|129.89|0.000013|0.04|0.78|2.29|0.02|
|368|0.03|129.3|129.89|129.89|0.000007|0.03|1.01|3.07|0.02|
|344|0.03|129.26|129.89|129.89|0.000006|0.03|1.04|2.95|0.02|
|320|0.03|129.36|129.89|129.89|0.000024|0.05|0.64|2.09|0.03|
|300|0.03|129.35|129.89|129.89|0.000019|0.04|0.68|2.08|0.02|
|280|0.03|129.31|129.89|129.89|0.000013|0.04|0.81|2.5|0.02|
|260|0.03|129.43|129.89|129.89|0.000027|0.05|0.61|2.05|0.03|
|240|0.03|129.36|129.89|129.89|0.000031|0.05|0.56|1.72|0.03|
|220|0.03|129.43|129.89|129.89|0.000036|0.06|0.54|1.85|0.03|
|200|0.03|129.38|129.89|129.89|0.00002|0.05|0.67|2.04|0.03|
|180|0.03|129.5|129.89|129.89|0.000131|0.09|0.34|1.51|0.06|
|160|0.03|129.37|129.89|129.89|0.000035|0.06|0.53|1.68|0.03|
|140|0.03|129.42|129.89|129.89|0.000058|0.07|0.44|1.61|0.04|
|120|0.03|129.44|129.89|129.89|0.000035|0.06|0.54|1.83|0.03|
|100|0.03|129.39|129.89|129.89|0.000026|0.05|0.61|1.99|0.03|
|80|0.03|129.49|129.88|129.88|0.000108|0.09|0.35|1.4|0.05|
|60|0.03|129.27|129.88|129.88|0.000001|0.01|2.21|4.51|0.01|
|40|0.03|129.57|129.88|129.88|0.001101|0.2|0.15|0.91|0.16|
|20|0.03|129.61|129.86|129.86|0.001|0.19|0.16|0.99|0.16|

Fuente: Elaboración propia, MODELING 2023.

31

Estudio de Aforo en Cauces Artificiales

DIA
PROYECTO SOL DE LEÓN

SPHERA ENERGY MODELING

3.1.5 Canal 5

Se detalla a continuación la identificación de los perfiles determinados en la modelación HEC-RAS
para el Canal 5, cada uno de estos perfiles demuestra junto a la Tabla resultados los parámetros
hidráulicos de la modelación para el caudal máximo permitido físicamente.

Según lo visto en terreno y por ortofotografía, el Canal 5 nace desde el área de generación y drena
agua de uso agrícola y/o lluvia hasta el Canal 7, no tiene conexión directa con otro cauce artificial o
natural por lo que su cierre no afecta a terceros.

En las siguientes figuras se demuestran los perfiles modelados en el Programa HEC-RAS con su
identificación respectiva por canal.

**Figura 19. Identificación de perfiles de modelación en HEC-RAS Canal 5**

Fuente: Elaboración propia, MODELING 2023.

De todos los caudales modelados en el Canal 5, se demuestra que el límite de porteo máximo es
0,01 m [3] /s, es por ello por lo que los resultados visuales en los perfiles hidráulicos se mostraran con
ese valor y también considera demostrar el efecto del flujo para un caudal de 0,5 m [3] /s y caudales
menores (Apéndice A). A su vez, se comprende que el límite de porteo del Canal 5 se encuentra
representado en el Perfil identificado como “60” el cual se muestra a continuación.

32

Estudio de Aforo en Cauces Artificiales

DIA
PROYECTO SOL DE LEÓN

SPHERA ENERGY MODELING

**Figura 20. Perfil 60 sensible a desborde Canal 5**

Fuente: Elaboración propia, MODELING 2023.

A continuación, se muestra el perfil longitudinal del canal modelado, al igual que la figura anterior
se aprecia el caudal de porteo máximo y considerando un caudal extremo de 0,01 m [3] /s.

**Figura 21. Eje longitudinal Canal 5**

Fuente: Elaboración propia, MODELING 2023.

A continuación, se muestran los resultados de la modelación entregada por el software HEC-RAS en
su versión 6.3 para el Canal 5, con un caudal de 0,01 m [3] /s.

33

Estudio de Aforo en Cauces Artificiales

DIA
PROYECTO SOL DE LEÓN

SPHERA ENERGY MODELING

**Tabla 7. Eje Hidráulico en Canal 5 para un caudal de 0,01 m3/s**

|River<br>Sta|Q<br>Total|Min Ch<br>El|W.S.<br>Elev|E.G.<br>Elev|E.G.<br>Slope|Vel<br>Chnl|Flow<br>Area|Top<br>Width|Froude #<br>Chl|
|---|---|---|---|---|---|---|---|---|---|
||**(m3/s)**|**(m)**|**(m)**|**(m)**|**(m/m)**|**(m/s)**|**(m2)**|**(m)**||
|272|0.01|130.57|131.02|131.02|0.000001|0.01|0.83|3.11|0.01|
|256|0.01|130.75|131.02|131.02|0.000008|0.02|0.5|3.87|0.02|
|240|0.01|130.88|131.02|131.02|0.000092|0.05|0.22|3.39|0.05|
|216|0.01|130.95|131|131.01|0.042456|0.53|0.02|0.84|0.92|
|194|0.01|130.55|130.85|130.85|0.000017|0.03|0.31|1.66|0.02|
|180|0.01|130.57|130.85|130.85|0.000032|0.04|0.25|1.62|0.03|
|160|0.01|130.65|130.85|130.85|0.00005|0.05|0.21|1.52|0.04|
|143|0.01|130.51|130.85|130.85|0.000003|0.02|0.65|3.15|0.01|
|122|0.01|130.57|130.85|130.85|0.000008|0.02|0.43|2.49|0.02|
|107|0.01|130.53|130.85|130.85|0.000008|0.02|0.44|2.46|0.02|
|80|0.01|130.61|130.85|130.85|0.000023|0.03|0.32|3.25|0.03|
|60|0.01|130.72|130.85|130.85|0.00016|0.06|0.18|2.69|0.07|
|40|0.01|130.62|130.85|130.85|0.000107|0.06|0.16|1.29|0.06|
|19|0.01|130.73|130.84|130.84|0.001001|0.14|0.08|1.27|0.16|

Fuente: Elaboración propia, MODELING 2023.

34

Estudio de Aforo en Cauces Artificiales

DIA
PROYECTO SOL DE LEÓN

SPHERA ENERGY MODELING

3.1.6 Canal 6

Se detalla a continuación la identificación de los perfiles determinados en la modelación HEC-RAS
para el Canal 6, cada uno de estos perfiles demuestra junto a la Tabla resultados los parámetros
hidráulicos de la modelación para el caudal máximo permitido físicamente.

El Canal 6 al igual que el Canal 5 según lo visto en terreno y por ortofotografía, nace desde el área
de generación y drena agua de uso agrícola y/o lluvia hasta el Canal 7, no tiene conexión directa con
otro cauce artificial o natural por lo que su intervención no afecta a terceros.

En las siguientes figuras se demuestran los perfiles modelados en el Programa HEC-RAS con su
identificación respectiva por canal.

**Figura 22. Identificación de perfiles de modelación en HEC-RAS Canal 6**

Fuente: Elaboración propia, MODELING 2023.

De todos los caudales modelados en el Canal 6, se demuestra que el límite de porteo máximo es 0,1
m [3] /s, es por ello por lo que los resultados visuales en los perfiles hidráulicos se mostraran con ese
valor y también considera demostrar el efecto del flujo para un caudal de 0,5 m [3] /s (Apéndice A). A
su vez, se comprende que el límite de porteo del Canal 6 se encuentra representado en el Perfil

identificado como “79” el cual se muestra a continuación.

35

Estudio de Aforo en Cauces Artificiales

DIA
PROYECTO SOL DE LEÓN

SPHERA ENERGY MODELING

**Figura 23. Perfil 79 sensible a desborde Canal 6**

Fuente: Elaboración propia, MODELING 2023.

A continuación, se muestra el perfil longitudinal del canal modelado, al igual que la figura anterior
se aprecia el caudal de porteo máximo y considerando un caudal extremo de 0,1m [3] /s.

**Figura 24. Eje longitudinal Canal 6**

Fuente: Elaboración propia, MODELING 2023.

A continuación, se muestran los resultados de la modelación entregada por el software HEC-RAS en
su versión 6.3 para el Canal 6, con un caudal de 0,1 m [3] /s.

36

Estudio de Aforo en Cauces Artificiales

DIA
PROYECTO SOL DE LEÓN

SPHERA ENERGY MODELING

**Tabla 8. Eje Hidráulico en Canal 6 para un caudal de 0,1m3/s**

|River<br>Sta|Q<br>Total|Min Ch<br>El|W.S.<br>Elev|E.G.<br>Elev|E.G.<br>Slope|Vel<br>Chnl|Flow<br>Area|Top<br>Width|Froude #<br>Chl|
|---|---|---|---|---|---|---|---|---|---|
||**(m3/s)**|**(m)**|**(m)**|**(m)**|**(m/m)**|**(m/s)**|**(m2)**|**(m)**||
|360|0.1|130.59|130.85|130.87|0.014819|0.72|0.14|1.08|0.64|
|340|0.1|130.44|130.82|130.82|0.000785|0.24|0.42|1.9|0.16|
|320|0.1|130.55|130.78|130.79|0.004542|0.42|0.24|1.87|0.37|
|300|0.1|130.34|130.72|130.73|0.002427|0.37|0.27|1.48|0.27|
|280|0.1|130.33|130.62|130.64|0.009418|0.64|0.16|0.98|0.51|
|260|0.1|130.15|130.41|130.44|0.011383|0.7|0.14|0.92|0.56|
|240|0.1|129.98|130.33|130.34|0.002592|0.39|0.25|1.3|0.28|
|220|0.1|129.93|130.24|130.26|0.006825|0.57|0.18|1.03|0.44|
|200|0.1|129.8|130.2|130.2|0.001266|0.31|0.32|1.26|0.2|
|180|0.1|129.83|130.14|130.15|0.006242|0.56|0.18|1|0.42|
|160|0.1|129.65|130.12|130.12|0.000663|0.24|0.42|1.58|0.15|
|140|0.1|129.8|130.09|130.1|0.001874|0.34|0.3|1.57|0.25|
|120|0.1|129.69|130.07|130.07|0.001037|0.27|0.37|1.74|0.19|
|100|0.1|129.61|130.06|130.06|0.000274|0.15|0.65|2.69|0.1|
|79|0.1|129.68|130.05|130.05|0.000376|0.16|0.61|3|0.12|
|58|0.1|129.77|130.03|130.04|0.001966|0.31|0.32|2.06|0.25|
|42|0.1|129.82|129.96|129.98|0.010028|0.49|0.2|2.28|0.53|
|22|0.1|129.71|129.92|129.93|0.001001|0.18|0.54|4.72|0.17|

Fuente: Elaboración propia, MODELING 2023.

37

Estudio de Aforo en Cauces Artificiales

DIA
PROYECTO SOL DE LEÓN

SPHERA ENERGY MODELING

3.1.7 Canal 7

Se detalla a continuación la identificación de los perfiles determinados en la modelación HEC-RAS
para el Canal 7, cada uno de estos perfiles demuestra junto a la Tabla resultados los parámetros
hidráulicos de la modelación para el caudal máximo permitido físicamente.

El Canal 7 tiene su trayectoria al sur del área de generación del Proyecto, es un cauce artificial que,
según lo visto en terreno, ortofotografía y manejo de SIG demuestra ser un cauce drenante de
caudales no utilizados por actividad agrícola, esto debido al nulo mantenimiento y presentan
dirección irregular en su trayectoria.

En las siguientes figuras se demuestran los perfiles modelados en el Programa HEC-RAS con su
identificación respectiva por canal.

**Figura 25. Identificación de perfiles de modelación en HEC-RAS Canal 7**

Fuente: Elaboración propia, MODELING 2022.

De todos los caudales modelados en el Canal 7, se demuestra que el límite de porteo máximo es
0,18 m [3] /s, es por ello por lo que los resultados visuales en los perfiles hidráulicos se mostraran con
ese valor y también considera demostrar el efecto del flujo para un caudal de 0,5 m [3] /s (Apéndice

38

Estudio de Aforo en Cauces Artificiales

DIA
PROYECTO SOL DE LEÓN

SPHERA ENERGY MODELING

A). A su vez, se comprende que el límite de porteo del Canal 7 se encuentra representado en el Perfil

identificado como “481” el cual se muestra a continuación.

**Figura 26. Perfil 481 sensible a desborde Canal 7**

Fuente: Elaboración propia, MODELING 2023.

A continuación, se muestra el perfil longitudinal del canal modelado, al igual que la figura anterior
se aprecia el caudal de porteo máximo y considerando un caudal extremo de 0,18 m [3] /s.

**Figura 27. Eje longitudinal Canal 7**

Fuente: Elaboración propia, MODELING 2023.

A continuación, se muestran los resultados de la modelación entregada por el software HEC-RAS en
su versión 6.3 para el Canal 7, con un caudal de 0,18 m [3] /s.

39

Estudio de Aforo en Cauces Artificiales

DIA
PROYECTO SOL DE LEÓN

SPHERA ENERGY MODELING

**Tabla 9. Eje Hidráulico en Canal 7 para un caudal de 0,18 m3/s**

|River<br>Sta|Q<br>Total|Min Ch<br>El|W.S.<br>Elev|E.G.<br>Elev|E.G.<br>Slope|Vel<br>Chnl|Flow<br>Area|Top<br>Width|Froude #<br>Chl|
|---|---|---|---|---|---|---|---|---|---|
||**(m3/s)**|**(m)**|**(m)**|**(m)**|**(m/m)**|**(m/s)**|**(m2)**|**(m)**||
|1560|0.18|132.46|132.71|132.72|0.001171|0.23|0.84|5.25|0.17|
|1540|0.18|132.44|132.68|132.68|0.002173|0.28|0.66|4.66|0.23|
|1520|0.18|132.43|132.57|132.59|0.018423|0.58|0.31|3.34|0.61|
|1500|0.18|132.25|132.54|132.55|0.000629|0.18|1.04|5.73|0.13|
|1480|0.18|132.18|132.53|132.53|0.000732|0.2|0.92|4.42|0.14|
|1460|0.18|132.23|132.52|132.52|0.000607|0.18|1|4.69|0.13|
|1440|0.18|132.24|132.5|132.5|0.000821|0.2|0.94|5.51|0.14|
|1420|0.18|132.25|132.48|132.48|0.002192|0.27|0.68|4.68|0.22|
|1400|0.18|132.2|132.46|132.46|0.000418|0.13|1.41|8.77|0.1|
|1380|0.18|132.25|132.45|132.45|0.001201|0.19|0.96|7.81|0.17|
|1360|0.18|132.24|132.42|132.42|0.001887|0.22|0.85|7.74|0.2|
|1340|0.18|132.2|132.38|132.38|0.001904|0.21|0.9|8.75|0.2|
|1320|0.18|132.15|132.36|132.36|0.00074|0.14|1.28|10.49|0.13|
|1300|0.18|132.11|132.33|132.33|0.00244|0.27|0.67|5|0.23|
|1284|0.18|132.05|132.26|132.27|0.007537|0.45|0.4|3.26|0.4|
|1259|0.18|131.64|132.27|132.27|0.00002|0.05|3.76|10.71|0.03|
|1240|0.18|131.78|132.26|132.26|0.000198|0.12|1.59|7.19|0.07|
|1219|0.18|132.06|132.24|132.25|0.010549|0.44|0.4|4.25|0.46|
|1200|0.18|131.79|132.21|132.22|0.000662|0.17|1.08|6.08|0.13|
|1178|0.18|131.81|132.18|132.19|0.003731|0.43|0.42|1.94|0.3|
|1155|0.18|131.81|131.99|132.02|0.01973|0.72|0.25|1.97|0.65|
|1142|0.18|131.51|132.01|132.01|0.000074|0.08|2.3|7.84|0.05|
|1116|0.18|131.64|132|132|0.000295|0.14|1.28|5.12|0.09|
|1104|0.18|131.6|132|132|0.000288|0.13|1.35|5.72|0.09|
|1081|0.18|131.64|131.98|131.98|0.002432|0.36|0.5|2.31|0.25|
|1060|0.18|131.62|131.81|131.85|0.032537|0.89|0.2|1.7|0.82|
|1043|0.18|130.97|131.11|131.14|0.055807|0.83|0.22|3.1|1|
|1020|0.18|130.66|131.02|131.03|0.001099|0.26|0.7|2.94|0.17|
|1000|0.18|130.72|130.95|130.97|0.013923|0.69|0.26|1.64|0.56|
|982|0.18|130.61|130.8|130.81|0.006|0.41|0.44|3.4|0.36|
|960|0.18|130.47|130.7|130.71|0.003407|0.35|0.52|3.3|0.28|
|940|0.18|130.37|130.62|130.63|0.004026|0.4|0.44|2.53|0.31|
|920|0.18|130.31|130.55|130.56|0.003203|0.37|0.49|2.73|0.28|
|900|0.18|130.19|130.48|130.49|0.004206|0.41|0.44|2.54|0.32|
|880|0.18|130.1|130.4|130.41|0.003384|0.37|0.49|2.79|0.28|

40

Estudio de Aforo en Cauces Artificiales

DIA
PROYECTO SOL DE LEÓN

SPHERA ENERGY MODELING

|River<br>Sta|Q<br>Total|Min Ch<br>El|W.S.<br>Elev|E.G.<br>Elev|E.G.<br>Slope|Vel<br>Chnl|Flow<br>Area|Top<br>Width|Froude #<br>Chl|
|---|---|---|---|---|---|---|---|---|---|
||**(m3/s)**|**(m)**|**(m)**|**(m)**|**(m/m)**|**(m/s)**|**(m2)**|**(m)**||
|860|0.18|130.07|130.37|130.37|0.001123|0.24|0.74|3.5|0.17|
|840|0.18|130.02|130.34|130.34|0.001954|0.3|0.61|3.27|0.22|
|820|0.18|129.99|130.33|130.33|0.000283|0.13|1.46|7.17|0.09|
|800|0.18|129.97|130.32|130.33|0.000311|0.15|1.22|4.64|0.09|
|780|0.18|129.89|130.31|130.32|0.000854|0.24|0.74|2.76|0.15|
|760|0.18|129.89|130.3|130.31|0.000307|0.15|1.17|4.18|0.09|
|740|0.18|129.69|130.3|130.3|0.000025|0.06|3.24|9.3|0.03|
|720|0.18|129.58|130.3|130.3|0.000049|0.08|2.18|4.8|0.04|
|700|0.18|129.73|130.3|130.3|0.000131|0.11|1.6|4.75|0.06|
|680|0.18|130.09|130.24|130.29|0.052217|0.95|0.19|2.09|1.01|
|660|0.18|129.51|130.25|130.25|0.000013|0.05|3.76|7.81|0.02|
|640|0.18|129.54|130.25|130.25|0.000015|0.05|3.73|9.26|0.02|
|620|0.18|129.42|130.25|130.25|0.000036|0.08|2.31|4.28|0.03|
|600|0.18|129.71|130.25|130.25|0.000207|0.13|1.42|5.06|0.08|
|582|0.18|129.72|130.25|130.25|0.000063|0.09|2.1|5.43|0.04|
|560|0.18|129.27|130.25|130.25|0.000023|0.07|2.74|4.43|0.03|
|539|0.18|129.34|130.25|130.25|0.000005|0.03|5.62|11.44|0.01|
|518|0.18|129.22|130.25|130.25|0.000005|0.04|5.18|9.81|0.01|
|498|0.18|129.2|130.25|130.25|0.000004|0.03|5.44|9.3|0.01|
|481|0.18|129.3|130.25|130.25|0.000009|0.04|4.41|9.84|0.02|
|460|0.18|129.5|130.25|130.25|0.000012|0.04|4.12|9.21|0.02|
|441|0.18|129.68|130.25|130.25|0.000191|0.15|1.29|4.21|0.08|
|420|0.18|129.66|130.24|130.24|0.000035|0.07|2.5|5.62|0.03|
|400|0.18|129.7|130.24|130.24|0.000046|0.07|2.53|8.06|0.04|
|380|0.18|129.79|130.24|130.24|0.00036|0.16|1.11|4.13|0.1|
|360|0.18|129.88|130.23|130.23|0.001174|0.24|0.75|3.83|0.17|
|340|0.18|129.81|130.21|130.21|0.000569|0.19|0.96|4.08|0.12|
|320|0.18|129.9|130.2|130.2|0.00086|0.23|0.8|3.4|0.15|
|303|0.18|129.8|130.19|130.19|0.000484|0.17|1.04|4.37|0.11|
|280|0.18|129.78|130.18|130.18|0.000301|0.14|1.28|5.13|0.09|
|257|0.18|129.84|130.17|130.17|0.000759|0.19|0.96|5.04|0.14|
|240|0.18|129.83|130.16|130.16|0.000486|0.15|1.17|5.9|0.11|
|220|0.18|129.87|130.15|130.15|0.000434|0.16|1.14|5.08|0.11|
|200|0.18|129.72|130.14|130.15|0.000146|0.11|1.63|5.69|0.06|
|180|0.18|129.8|130.14|130.14|0.000482|0.18|0.99|3.77|0.11|
|160|0.18|129.8|130.13|130.13|0.000641|0.2|0.91|3.79|0.13|
|140|0.18|129.96|130.06|130.08|0.056896|0.69|0.26|4.98|0.97|

41

Estudio de Aforo en Cauces Artificiales

DIA
PROYECTO SOL DE LEÓN

SPHERA ENERGY MODELING

|River<br>Sta|Q<br>Total|Min Ch<br>El|W.S.<br>Elev|E.G.<br>Elev|E.G.<br>Slope|Vel<br>Chnl|Flow<br>Area|Top<br>Width|Froude #<br>Chl|
|---|---|---|---|---|---|---|---|---|---|
||**(m3/s)**|**(m)**|**(m)**|**(m)**|**(m/m)**|**(m/s)**|**(m2)**|**(m)**||
|120|0.18|129.66|130.03|130.03|0.000297|0.14|1.27|5.06|0.09|
|100|0.18|129.77|130.02|130.02|0.000537|0.15|1.19|7.22|0.12|
|80|0.18|129.74|130.01|130.01|0.000617|0.17|1.04|5.33|0.12|
|60|0.18|129.79|129.98|129.99|0.002702|0.29|0.62|4.34|0.25|
|40|0.18|129.72|129.95|129.95|0.001169|0.21|0.85|5.11|0.17|
|20|0.18|129.7|129.92|129.92|0.002003|0.25|0.71|5.01|0.21|

Fuente: Elaboración propia, MODELING 2023.

42

Estudio de Aforo en Cauces Artificiales

DIA
PROYECTO SOL DE LEÓN

SPHERA ENERGY MODELING

3.1.8 Canal 8

Se detalla a continuación la identificación de los perfiles determinados en la modelación HEC-RAS
para el Canal 8, cada uno de estos perfiles demuestra junto a la Tabla resultados los parámetros
hidráulicos de la modelación para el caudal máximo permitido físicamente.

El Canal 8 nace aparentemente del Canal 7 y se proyecta sobre la trayectoria del camino de acceso
a las estructuras, el Canal 8 presenta nulo mantenimiento y se desconoce su uso. No obstante, se
estudia a modo de comprender su magnitud.

En las siguientes figuras se demuestran los perfiles modelados en el Programa HEC-RAS con su
identificación respectiva por canal.

**Figura 28. Identificación de perfiles de modelación en HEC-RAS Canal 8**

Fuente: Elaboración propia, MODELING 2023.

De todos los caudales modelados en el Canal 8, se demuestra que el límite de porteo máximo es 0,9
m [3] /s, es por ello por lo que los resultados visuales en los perfiles hidráulicos se mostraran con ese
valor y también considera demostrar el efecto del flujo para un caudal de 0,5 m [3] /s (Apéndice A). A
su vez, se comprende que el límite de porteo del Canal 8 se encuentra representado en el Perfil

identificado como “101” el cual se muestra a continuación.

43

Estudio de Aforo en Cauces Artificiales

DIA
PROYECTO SOL DE LEÓN

SPHERA ENERGY MODELING

**Figura 29. Perfil 101 sensible a desborde Canal 8**

Fuente: Elaboración propia, MODELING 2023.

A continuación, se muestra el perfil longitudinal del canal modelado, al igual que la figura anterior
se aprecia el caudal de porteo máximo y considerando un caudal extremo de 0,9m [3] /s.

**Figura 30. Eje longitudinal Canal 8**

Fuente: Elaboración propia, MODELING 2023.

A continuación, se muestran los resultados de la modelación entregada por el software HEC-RAS en
su versión 6.3 para el Canal 8, con un caudal de 0,9 m [3] /s.

44

Estudio de Aforo en Cauces Artificiales

DIA
PROYECTO SOL DE LEÓN

SPHERA ENERGY MODELING

**Tabla 10. Eje Hidráulico en Canal 8 para un caudal de 0,9m3/s**

|River<br>Sta|Q<br>Total|Min Ch<br>El|W.S.<br>Elev|E.G.<br>Elev|E.G.<br>Slope|Vel<br>Chnl|Flow<br>Area|Top<br>Width|Froude #<br>Chl|
|---|---|---|---|---|---|---|---|---|---|
||**(m3/s)**|**(m)**|**(m)**|**(m)**|**(m/m)**|**(m/s)**|**(m2)**|**(m)**||
|121|0.9|133.3|134.28|134.28|0.0003|0.26|3.89|10.03|0.11|
|101|0.9|133.56|134.27|134.28|0.000468|0.3|3.04|7.43|0.14|
|81|0.9|133.64|134.25|134.26|0.001124|0.4|2.32|7.34|0.21|
|61|0.9|133.41|134.24|134.24|0.000731|0.37|2.48|6|0.17|
|37|0.9|133.41|134.23|134.23|0.000359|0.28|3.36|6.82|0.12|
|18|0.9|133.74|134.21|134.22|0.001324|0.4|2.48|9.96|0.22|
|8|0.9|133.87|134.18|134.2|0.004004|0.57|1.69|8.23|0.37|

Fuente: Elaboración propia, MODELING 2023.

45

Estudio de Aforo en Cauces Artificiales

DIA
PROYECTO SOL DE LEÓN

SPHERA ENERGY MODELING

**4** **CONCLUSIONES**

En el presente documento de respaldo técnico se determinaron las capacidades de porteo
hidráulico en los ocho (8) canales existentes en interacción con el Proyecto Sol de León, tanto en el
área de generación como dentro de la trayectoria del camino de acceso a la línea de transmisión
eléctrica considerada para el Proyecto.

Mediante el uso de la herramienta computacional HEC-RAS se realizó una modelación hidráulica
computacional de los canales, basada en información topográfica de detalle con curvas de nivel cada
0,5 metros, visita a terreno a modo de caracterizar un correcto coeficiente de Manning, y la
disposición de caudales iterativos hasta alcanzar el desborde para simular en cada canal. De esta
manera se permite comprobar la capacidad máxima de porteo de caudal en cada canal estudiado.

Las condiciones de borde usadas son las de la pendiente del fondo de cada canal, las cuales fueron
determinadas según topografía en base a su modelo digital de terreno (MDT), estas oscilan entre
pendientes de 0.001 a 0,004 m/m. Y un coeficiente de rugosidad de Manning que varía entre 0,04
hasta 0,064 según la vegetación y tipo de material del lecho de cada cauce.

Los caudales máximos de porteo fueron determinados según las secciones más desfavorables en
cada canal, los valores correspondientes a los caudales máximos de porteo se encuentran en un
rango entre los 0,01 y 0,9 m [3] /s, para el Canal 5 y Canal 8 respectivamente. Vale decir que, al
incrementar el valor en una décima cúbica de caudal en cada canal se provocaría un desborde por
lo que no se permite portar mayor cantidad de la mencionada.

Los canales superiores a 0,5 m [3] /s en capacidad de porteo, son los Canales 1 y Canal 8. Es importante
destacar que, estos canales comprometen ser de consideración importante según lo establece la
normativa ambiental vigente, por lo que su modificación recae en la implementación de un permiso
ambiental sectorial mixto (SEA-DGA) correspondiente al artículo 156 del Reglamento del SEIA. Para
el resto de los canales que no presentan una capacidad de porteo de 0,5 m [3] /s o superior, no se
considera presentar PAS156, pero si se realizaran intervenciones las cuales se especifican en el
documento Caracterización Hidrológica.

En base a los antecedentes presentados se concluye junto a los argumentos técnicos mostrados
que, el Proyecto Sol de León **presentará un Permiso Ambiental Sectorial (PAS) 156 para modificar**
**el cauce y/o implementar una obra de atravieso en los canales 1 y 8**, incorporado en el Anexo 9.5
de la DIA, de acuerdo con lo establecido en la Resolución N°135 de la Dirección General de Aguas
(DGA) del 30 de enero del año 2020.

46

Estudio de Aforo en Cauces Artificiales

DIA
PROYECTO SOL DE LEÓN

SPHERA ENERGY MODELING

**5** **BIBLIOGRAFIA**

 - Manual de Carreteras V3 (2016), MOP Chile.

 - Manual de Carreteras V4 (2021), MOP Chile.

 - Hidráulica Aplicada (2007) Horacio Mery

 - Hidráulica (1999) Francisco Domínguez

 - Guide for Selecting Manning's Roughness Coefficients for Natural Channels and Flood Plains,

United States Geological Survey Water-Supply Paper 2339, 1989

 - Manual Básico de HEC-RAS 3.1.3 y HEC-GeoRAS 3.1.1 (2007), Universidad de Granada

**6** **APENDICES**

 - Apéndice A. Ejes Hidráulicos Canales

47

Estudio de Aforo en Cauces Artificiales

DIA
PROYECTO SOL DE LEÓN

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Método de Cowan Cauces Artificiales****

| CANAL | METODO DE COWAN | Col3 | Col4 | Col5 | Col6 | Col7 | COEFICIENTE DE MANNING |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **CANAL** | **Nb** | **n1** | **n2** | **n3** | **n4** | **m ** | **n ** |
| 1 | 0.025 | 0.011 | 0.001 | 0.002 | 0.025 | 1 | 0.064 |
| 2 | 0.025 | 0.01 | 0.001 | 0.002 | 0.01 | 1 | 0.048 |
| 3 | 0.025 | 0.01 | 0.001 | 0.005 | 0.01 | 1 | 0.051 |
| 4 | 0.025 | 0.01 | 0.001 | 0.002 | 0.005 | 1 | 0.043 |
| 5 | 0.025 | 0.01 | 0.001 | 0.001 | 0.003 | 1 | 0.04 |
| 6 | 0.025 | 0.01 | 0.001 | 0.001 | 0.003 | 1 | 0.04 |
| 7 | 0.025 | 0.01 | 0.001 | 0.002 | 0.01 | 1 | 0.048 |
| 8 | 0.025 | 0.01 | 0.001 | 0.002 | 0.005 | 1 | 0.043 |

**Tabla 2.: Condiciones de borde en quebradas para HEC-RAS****

| QUEBRADA | UPSTREAM (m/m) | DOWNSTREAM(m/m) |
| --- | --- | --- |
| Canal 1 | 0.003 | 0.003 |
| Canal 2 | 0.004 | 0.004 |
| Canal 3 | 0.003 | 0.003 |
| Canal 4 | 0.001 | 0.001 |
| Canal 5 | 0.001 | 0.001 |
| Canal 6 | 0.001 | 0.001 |
| Canal 7 | 0.002 | 0.002 |
| Canal 8 | 0.004 | 0.004 |

**Tabla 3.: Eje Hidráulico en Canal 1 para un caudal de 0,5 m3/s****

| River<br>Sta | Q Total | Min Ch<br>El | W.S.<br>Elev | E.G.<br>Elev | E.G.<br>Slope | Vel<br>Chnl | Flow<br>Area | Top<br>Width | Froude #<br>Chl |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | **(m3/s)** | **(m)** | **(m)** | **(m)** | **(m/m)** | **(m/s)** | **(m2)** | **(m)** |  |
| 1500 | 0.5 | 131.14 | 131.75 | 131.76 | 0.006067 | 0.59 | 0.85 | 2.09 | 0.3 |
| 1480 | 0.5 | 131.09 | 131.64 | 131.65 | 0.005204 | 0.55 | 0.91 | 2.31 | 0.28 |
| 1460 | 0.5 | 130.96 | 131.4 | 131.45 | 0.027382 | 0.94 | 0.53 | 2.19 | 0.61 |
| 1440 | 0.5 | 130.54 | 131.14 | 131.16 | 0.008452 | 0.68 | 0.73 | 1.7 | 0.33 |
| 1420 | 0.5 | 130.29 | 131.08 | 131.09 | 0.001749 | 0.37 | 1.34 | 2.5 | 0.16 |
| 1400 | 0.5 | 130.36 | 131.06 | 131.07 | 0.00081 | 0.27 | 1.89 | 4.26 | 0.12 |
| 1380 | 0.5 | 130.33 | 131.06 | 131.06 | 0.000231 | 0.15 | 3.62 | 8.94 | 0.07 |
| 1360 | 0.5 | 130.18 | 131.05 | 131.05 | 0.000679 | 0.25 | 2.03 | 4.13 | 0.11 |
| 1340 | 0.5 | 130.19 | 131.04 | 131.04 | 0.00046 | 0.22 | 2.41 | 5.29 | 0.09 |
| 1320 | 0.5 | 130.21 | 131.02 | 131.03 | 0.000886 | 0.27 | 1.87 | 3.93 | 0.12 |
| 1300 | 0.5 | 129.99 | 131.01 | 131.01 | 0.000349 | 0.19 | 2.66 | 5.1 | 0.08 |
| 1280 | 0.5 | 129.93 | 131.01 | 131.01 | 0.000434 | 0.21 | 2.42 | 4.21 | 0.09 |
| 1260 | 0.5 | 129.9 | 131 | 131 | 0.000342 | 0.2 | 2.53 | 3.74 | 0.08 |
| 1240 | 0.5 | 129.7 | 130.99 | 131 | 0.000137 | 0.14 | 3.66 | 4.78 | 0.05 |
| 1226 | 0.5 | 129.72 | 130.99 | 130.99 | 0.000095 | 0.12 | 4.25 | 5.53 | 0.04 |
| 1219 | Inl<br>Struct |  |  |  |  |  |  |  |  |
| 1200 | 0.5 | 129.37 | 130.2 | 130.21 | 0.000843 | 0.28 | 1.8 | 3.2 | 0.12 |
| 1180 | 0.5 | 129.67 | 130.1 | 130.15 | 0.033768 | 1.03 | 0.48 | 2.06 | 0.68 |
| 1160 | 0.5 | 129.34 | 130.08 | 130.09 | 0.000858 | 0.27 | 1.82 | 3.52 | 0.12 |
| 1140 | 0.5 | 129.35 | 130.07 | 130.07 | 0.000626 | 0.25 | 2.13 | 4.73 | 0.11 |
| 1120 | 0.5 | 129.48 | 130.04 | 130.05 | 0.00258 | 0.4 | 1.24 | 3.12 | 0.2 |
| 1100 | 0.5 | 129.06 | 130.03 | 130.03 | 0.000322 | 0.19 | 2.62 | 4.11 | 0.08 |
| 1080 | 0.5 | 128.99 | 130.02 | 130.03 | 0.000276 | 0.19 | 2.69 | 3.61 | 0.07 |
| 1060 | 0.5 | 129.12 | 130.02 | 130.02 | 0.000416 | 0.21 | 2.34 | 3.54 | 0.08 |
| 1040 | 0.5 | 129.03 | 130.01 | 130.01 | 0.000149 | 0.15 | 3.48 | 5.73 | 0.05 |
| 1020 | 0.5 | 129.35 | 130 | 130.01 | 0.002571 | 0.39 | 1.28 | 3.36 | 0.2 |
| 1000 | 0.5 | 129.48 | 129.94 | 129.95 | 0.002912 | 0.4 | 1.25 | 3.61 | 0.22 |
| 980 | 0.5 | 129.29 | 129.66 | 129.77 | 0.080145 | 1.51 | 0.33 | 1.46 | 1.01 |
| 960 | 0.5 | 128.81 | 129.58 | 129.59 | 0.000617 | 0.24 | 2.11 | 4.02 | 0.1 |
| 940 | 0.5 | 128.81 | 129.57 | 129.58 | 0.000501 | 0.22 | 2.24 | 3.84 | 0.09 |
| 920 | 0.5 | 128.8 | 129.56 | 129.57 | 0.000456 | 0.22 | 2.29 | 3.99 | 0.09 |
| 900 | 0.5 | 128.79 | 129.55 | 129.55 | 0.00076 | 0.26 | 1.91 | 3.57 | 0.11 |
| 880 | 0.5 | 128.82 | 129.54 | 129.54 | 0.000765 | 0.25 | 1.96 | 3.97 | 0.12 |
| 860 | 0.5 | 128.81 | 129.53 | 129.53 | 0.0004 | 0.2 | 2.49 | 4.31 | 0.08 |
| 840 | 0.5 | 128.93 | 129.51 | 129.51 | 0.001719 | 0.34 | 1.47 | 3.78 | 0.17 |

**Tabla 4.: Eje Hidráulico en Canal 2 para un caudal de 0,29 m3/s****

| River<br>Sta | Q<br>Total | Min Ch<br>El | W.S.<br>Elev | E.G.<br>Elev | E.G.<br>Slope | Vel<br>Chnl | Flow<br>Area | Top<br>Width | Froude #<br>Chl |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | **(m3/s)** | **(m)** | **(m)** | **(m)** | **(m/m)** | **(m/s)** | **(m2)** | **(m)** |  |
| 320 | 0.29 | 130.85 | 131.4 | 131.4 | 0.000845 | 0.34 | 1.13 | 6.09 | 0.16 |
| 300 | 0.29 | 130.88 | 131.34 | 131.36 | 0.006021 | 0.65 | 0.46 | 1.76 | 0.38 |
| 280 | 0.29 | 130.75 | 131.26 | 131.27 | 0.00344 | 0.53 | 0.6 | 2.28 | 0.3 |
| 260 | 0.29 | 130.69 | 131.18 | 131.2 | 0.004198 | 0.56 | 0.53 | 2.25 | 0.33 |
| 240 | 0.29 | 130.61 | 131.02 | 131.05 | 0.014112 | 0.82 | 0.36 | 1.77 | 0.57 |
| 220 | 0.29 | 130.44 | 130.97 | 130.97 | 0.001576 | 0.41 | 0.77 | 2.77 | 0.21 |
| 200 | 0.29 | 130.44 | 130.92 | 130.93 | 0.003189 | 0.54 | 0.61 | 2.3 | 0.29 |
| 180 | 0.29 | 130.42 | 130.83 | 130.85 | 0.005752 | 0.62 | 0.49 | 2.52 | 0.39 |
| 160 | 0.29 | 130.21 | 130.79 | 130.8 | 0.001053 | 0.37 | 0.93 | 3.49 | 0.18 |
| 140 | 0.29 | 130.45 | 130.68 | 130.73 | 0.03304 | 1.08 | 0.29 | 2.92 | 0.87 |
| 120 | 0.29 | 130.01 | 130.52 | 130.53 | 0.002461 | 0.48 | 0.65 | 2.13 | 0.26 |
| 100 | 0.29 | 130.01 | 130.48 | 130.49 | 0.001946 | 0.44 | 0.75 | 2.94 | 0.24 |
| 80 | 0.29 | 129.87 | 130.44 | 130.45 | 0.001861 | 0.43 | 0.71 | 2.64 | 0.23 |
| 60 | 0.29 | 129.95 | 130.37 | 130.39 | 0.005589 | 0.63 | 0.49 | 2.41 | 0.38 |
| 40 | 0.29 | 129.81 | 130.25 | 130.27 | 0.006031 | 0.67 | 0.45 | 1.79 | 0.39 |
| 20 | 0.29 | 129.71 | 130.16 | 130.17 | 0.004005 | 0.57 | 0.55 | 2.26 | 0.33 |

**Tabla 5.: Eje Hidráulico en Canal 3 para un caudal de 0,13 m3/s****

| River<br>Sta | Q<br>Total | Min Ch<br>El | W.S.<br>Elev | E.G.<br>Elev | E.G.<br>Slope | Vel<br>Chnl | Flow<br>Area | Top<br>Width | Froude #<br>Chl |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | **(m3/s)** | **(m)** | **(m)** | **(m)** | **(m/m)** | **(m/s)** | **(m2)** | **(m)** |  |
| 860 | 0.13 | 129.3 | 129.68 | 129.68 | 0.002462 | 0.33 | 0.4 | 1.92 | 0.23 |
| 840 | 0.13 | 129.37 | 129.58 | 129.6 | 0.009324 | 0.5 | 0.27 | 2.14 | 0.43 |
| 820 | 0.13 | 129.19 | 129.5 | 129.51 | 0.002558 | 0.33 | 0.39 | 1.91 | 0.23 |
| 803 | 0.13 | 129.14 | 129.32 | 129.38 | 0.05994 | 1.08 | 0.12 | 1.05 | 1.02 |
| 720 | 0.13 | 128.81 | 129.29 | 129.29 | 0.000172 | 0.12 | 1.14 | 4.36 | 0.07 |
| 700 | 0.13 | 129.03 | 129.25 | 129.28 | 0.021428 | 0.75 | 0.17 | 1.21 | 0.63 |
| 680 | 0.13 | 128.8 | 129.22 | 129.22 | 0.000928 | 0.23 | 0.56 | 2.33 | 0.15 |
| 640 | 0.13 | 128.86 | 129.13 | 129.14 | 0.006479 | 0.47 | 0.28 | 1.66 | 0.36 |
| 620 | 0.13 | 128.7 | 129.1 | 129.1 | 0.000939 | 0.22 | 0.59 | 2.55 | 0.15 |
| 600 | 0.13 | 128.49 | 129.09 | 129.09 | 0.000173 | 0.13 | 1.11 | 3.59 | 0.07 |
| 580 | 0.13 | 128.6 | 129.09 | 129.09 | 0.000413 | 0.18 | 0.74 | 2.58 | 0.1 |
| 560 | 0.13 | 128.75 | 129.08 | 129.08 | 0.000527 | 0.17 | 0.79 | 4.09 | 0.12 |
| 540 | 0.13 | 128.65 | 129.06 | 129.07 | 0.000664 | 0.21 | 0.64 | 2.66 | 0.13 |
| 519 | 0.13 | 128.83 | 129.01 | 129.03 | 0.018697 | 0.61 | 0.22 | 2.41 | 0.59 |
| 500 | 0.13 | 128.29 | 129.01 | 129.01 | 0.000148 | 0.12 | 1.12 | 3.35 | 0.06 |
| 480 | 0.13 | 128.36 | 129.01 | 129.01 | 0.000183 | 0.13 | 1.02 | 3.06 | 0.07 |
| 460 | 0.13 | 128.5 | 129 | 129 | 0.000325 | 0.15 | 0.87 | 3.29 | 0.09 |
| 436 | 0.13 | 128.64 | 128.99 | 128.99 | 0.000421 | 0.16 | 0.91 | 5 | 0.1 |
| 420 | 0.13 | 128.76 | 128.91 | 128.97 | 0.058667 | 1.01 | 0.13 | 1.25 | 1.01 |
| 400 | 0.13 | 128.36 | 128.7 | 128.71 | 0.003767 | 0.39 | 0.33 | 1.59 | 0.28 |
| 380 | 0.13 | 128.22 | 128.55 | 128.57 | 0.015755 | 0.67 | 0.19 | 1.21 | 0.53 |
| 360 | 0.13 | 128.11 | 128.46 | 128.46 | 0.002491 | 0.32 | 0.41 | 2.03 | 0.23 |
| 340 | 0.13 | 127.93 | 128.43 | 128.43 | 0.000825 | 0.22 | 0.6 | 2.33 | 0.14 |
| 320 | 0.13 | 128.01 | 128.4 | 128.4 | 0.003603 | 0.38 | 0.34 | 1.71 | 0.27 |
| 300 | 0.13 | 128.01 | 128.35 | 128.35 | 0.002018 | 0.29 | 0.45 | 2.46 | 0.21 |
| 280 | 0.13 | 127.92 | 128.32 | 128.33 | 0.00079 | 0.2 | 0.64 | 2.9 | 0.13 |
| 260 | 0.13 | 127.97 | 128.28 | 128.29 | 0.00826 | 0.49 | 0.26 | 1.7 | 0.4 |
| 240 | 0.13 | 127.76 | 128.22 | 128.23 | 0.00144 | 0.26 | 0.51 | 2.31 | 0.18 |
| 220 | 0.13 | 127.82 | 128.2 | 128.21 | 0.000836 | 0.24 | 0.59 | 2.83 | 0.14 |
| 200 | 0.13 | 127.78 | 128.19 | 128.19 | 0.000408 | 0.17 | 0.8 | 3.53 | 0.1 |
| 186 | 0.13 | 127.72 | 128.19 | 128.19 | 0.000407 | 0.16 | 0.8 | 3.16 | 0.1 |
| 160 | 0.13 | 127.85 | 128.17 | 128.17 | 0.001853 | 0.27 | 0.49 | 2.71 | 0.2 |
| 140 | 0.13 | 127.75 | 128.13 | 128.13 | 0.002087 | 0.29 | 0.45 | 2.25 | 0.21 |
| 120 | 0.13 | 127.78 | 128.1 | 128.1 | 0.000853 | 0.2 | 0.64 | 3.19 | 0.14 |
| 102 | 0.13 | 127.79 | 128.07 | 128.08 | 0.002589 | 0.3 | 0.43 | 2.83 | 0.24 |
| 79 | 0.13 | 127.78 | 128.03 | 128.04 | 0.001451 | 0.24 | 0.55 | 3.21 | 0.18 |

**Tabla 6.: Eje Hidráulico en Canal 4 para un caudal de 0,03m3/s****

| River<br>Sta | Q<br>Total | Min Ch<br>El | W.S.<br>Elev | E.G.<br>Elev | E.G.<br>Slope | Vel<br>Chnl | Flow<br>Area | Top<br>Width | Froude #<br>Chl |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | **(m3/s)** | **(m)** | **(m)** | **(m)** | **(m/m)** | **(m/s)** | **(m2)** | **(m)** |  |
| 420 | 0.03 | 129.32 | 129.89 | 129.89 | 0.000006 | 0.03 | 1.22 | 4.78 | 0.01 |
| 400 | 0.03 | 129.29 | 129.89 | 129.89 | 0.000005 | 0.03 | 1.11 | 3.15 | 0.01 |
| 385 | 0.03 | 129.35 | 129.89 | 129.89 | 0.000013 | 0.04 | 0.78 | 2.29 | 0.02 |
| 368 | 0.03 | 129.3 | 129.89 | 129.89 | 0.000007 | 0.03 | 1.01 | 3.07 | 0.02 |
| 344 | 0.03 | 129.26 | 129.89 | 129.89 | 0.000006 | 0.03 | 1.04 | 2.95 | 0.02 |
| 320 | 0.03 | 129.36 | 129.89 | 129.89 | 0.000024 | 0.05 | 0.64 | 2.09 | 0.03 |
| 300 | 0.03 | 129.35 | 129.89 | 129.89 | 0.000019 | 0.04 | 0.68 | 2.08 | 0.02 |
| 280 | 0.03 | 129.31 | 129.89 | 129.89 | 0.000013 | 0.04 | 0.81 | 2.5 | 0.02 |
| 260 | 0.03 | 129.43 | 129.89 | 129.89 | 0.000027 | 0.05 | 0.61 | 2.05 | 0.03 |
| 240 | 0.03 | 129.36 | 129.89 | 129.89 | 0.000031 | 0.05 | 0.56 | 1.72 | 0.03 |
| 220 | 0.03 | 129.43 | 129.89 | 129.89 | 0.000036 | 0.06 | 0.54 | 1.85 | 0.03 |
| 200 | 0.03 | 129.38 | 129.89 | 129.89 | 0.00002 | 0.05 | 0.67 | 2.04 | 0.03 |
| 180 | 0.03 | 129.5 | 129.89 | 129.89 | 0.000131 | 0.09 | 0.34 | 1.51 | 0.06 |
| 160 | 0.03 | 129.37 | 129.89 | 129.89 | 0.000035 | 0.06 | 0.53 | 1.68 | 0.03 |
| 140 | 0.03 | 129.42 | 129.89 | 129.89 | 0.000058 | 0.07 | 0.44 | 1.61 | 0.04 |
| 120 | 0.03 | 129.44 | 129.89 | 129.89 | 0.000035 | 0.06 | 0.54 | 1.83 | 0.03 |
| 100 | 0.03 | 129.39 | 129.89 | 129.89 | 0.000026 | 0.05 | 0.61 | 1.99 | 0.03 |
| 80 | 0.03 | 129.49 | 129.88 | 129.88 | 0.000108 | 0.09 | 0.35 | 1.4 | 0.05 |
| 60 | 0.03 | 129.27 | 129.88 | 129.88 | 0.000001 | 0.01 | 2.21 | 4.51 | 0.01 |
| 40 | 0.03 | 129.57 | 129.88 | 129.88 | 0.001101 | 0.2 | 0.15 | 0.91 | 0.16 |
| 20 | 0.03 | 129.61 | 129.86 | 129.86 | 0.001 | 0.19 | 0.16 | 0.99 | 0.16 |

**Tabla 7.: Eje Hidráulico en Canal 5 para un caudal de 0,01 m3/s****

| River<br>Sta | Q<br>Total | Min Ch<br>El | W.S.<br>Elev | E.G.<br>Elev | E.G.<br>Slope | Vel<br>Chnl | Flow<br>Area | Top<br>Width | Froude #<br>Chl |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | **(m3/s)** | **(m)** | **(m)** | **(m)** | **(m/m)** | **(m/s)** | **(m2)** | **(m)** |  |
| 272 | 0.01 | 130.57 | 131.02 | 131.02 | 0.000001 | 0.01 | 0.83 | 3.11 | 0.01 |
| 256 | 0.01 | 130.75 | 131.02 | 131.02 | 0.000008 | 0.02 | 0.5 | 3.87 | 0.02 |
| 240 | 0.01 | 130.88 | 131.02 | 131.02 | 0.000092 | 0.05 | 0.22 | 3.39 | 0.05 |
| 216 | 0.01 | 130.95 | 131 | 131.01 | 0.042456 | 0.53 | 0.02 | 0.84 | 0.92 |
| 194 | 0.01 | 130.55 | 130.85 | 130.85 | 0.000017 | 0.03 | 0.31 | 1.66 | 0.02 |
| 180 | 0.01 | 130.57 | 130.85 | 130.85 | 0.000032 | 0.04 | 0.25 | 1.62 | 0.03 |
| 160 | 0.01 | 130.65 | 130.85 | 130.85 | 0.00005 | 0.05 | 0.21 | 1.52 | 0.04 |
| 143 | 0.01 | 130.51 | 130.85 | 130.85 | 0.000003 | 0.02 | 0.65 | 3.15 | 0.01 |
| 122 | 0.01 | 130.57 | 130.85 | 130.85 | 0.000008 | 0.02 | 0.43 | 2.49 | 0.02 |
| 107 | 0.01 | 130.53 | 130.85 | 130.85 | 0.000008 | 0.02 | 0.44 | 2.46 | 0.02 |
| 80 | 0.01 | 130.61 | 130.85 | 130.85 | 0.000023 | 0.03 | 0.32 | 3.25 | 0.03 |
| 60 | 0.01 | 130.72 | 130.85 | 130.85 | 0.00016 | 0.06 | 0.18 | 2.69 | 0.07 |
| 40 | 0.01 | 130.62 | 130.85 | 130.85 | 0.000107 | 0.06 | 0.16 | 1.29 | 0.06 |
| 19 | 0.01 | 130.73 | 130.84 | 130.84 | 0.001001 | 0.14 | 0.08 | 1.27 | 0.16 |

**Tabla 8.: Eje Hidráulico en Canal 6 para un caudal de 0,1m3/s****

| River<br>Sta | Q<br>Total | Min Ch<br>El | W.S.<br>Elev | E.G.<br>Elev | E.G.<br>Slope | Vel<br>Chnl | Flow<br>Area | Top<br>Width | Froude #<br>Chl |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | **(m3/s)** | **(m)** | **(m)** | **(m)** | **(m/m)** | **(m/s)** | **(m2)** | **(m)** |  |
| 360 | 0.1 | 130.59 | 130.85 | 130.87 | 0.014819 | 0.72 | 0.14 | 1.08 | 0.64 |
| 340 | 0.1 | 130.44 | 130.82 | 130.82 | 0.000785 | 0.24 | 0.42 | 1.9 | 0.16 |
| 320 | 0.1 | 130.55 | 130.78 | 130.79 | 0.004542 | 0.42 | 0.24 | 1.87 | 0.37 |
| 300 | 0.1 | 130.34 | 130.72 | 130.73 | 0.002427 | 0.37 | 0.27 | 1.48 | 0.27 |
| 280 | 0.1 | 130.33 | 130.62 | 130.64 | 0.009418 | 0.64 | 0.16 | 0.98 | 0.51 |
| 260 | 0.1 | 130.15 | 130.41 | 130.44 | 0.011383 | 0.7 | 0.14 | 0.92 | 0.56 |
| 240 | 0.1 | 129.98 | 130.33 | 130.34 | 0.002592 | 0.39 | 0.25 | 1.3 | 0.28 |
| 220 | 0.1 | 129.93 | 130.24 | 130.26 | 0.006825 | 0.57 | 0.18 | 1.03 | 0.44 |
| 200 | 0.1 | 129.8 | 130.2 | 130.2 | 0.001266 | 0.31 | 0.32 | 1.26 | 0.2 |
| 180 | 0.1 | 129.83 | 130.14 | 130.15 | 0.006242 | 0.56 | 0.18 | 1 | 0.42 |
| 160 | 0.1 | 129.65 | 130.12 | 130.12 | 0.000663 | 0.24 | 0.42 | 1.58 | 0.15 |
| 140 | 0.1 | 129.8 | 130.09 | 130.1 | 0.001874 | 0.34 | 0.3 | 1.57 | 0.25 |
| 120 | 0.1 | 129.69 | 130.07 | 130.07 | 0.001037 | 0.27 | 0.37 | 1.74 | 0.19 |
| 100 | 0.1 | 129.61 | 130.06 | 130.06 | 0.000274 | 0.15 | 0.65 | 2.69 | 0.1 |
| 79 | 0.1 | 129.68 | 130.05 | 130.05 | 0.000376 | 0.16 | 0.61 | 3 | 0.12 |
| 58 | 0.1 | 129.77 | 130.03 | 130.04 | 0.001966 | 0.31 | 0.32 | 2.06 | 0.25 |
| 42 | 0.1 | 129.82 | 129.96 | 129.98 | 0.010028 | 0.49 | 0.2 | 2.28 | 0.53 |
| 22 | 0.1 | 129.71 | 129.92 | 129.93 | 0.001001 | 0.18 | 0.54 | 4.72 | 0.17 |

**Tabla 9.: Eje Hidráulico en Canal 7 para un caudal de 0,18 m3/s****

| River<br>Sta | Q<br>Total | Min Ch<br>El | W.S.<br>Elev | E.G.<br>Elev | E.G.<br>Slope | Vel<br>Chnl | Flow<br>Area | Top<br>Width | Froude #<br>Chl |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | **(m3/s)** | **(m)** | **(m)** | **(m)** | **(m/m)** | **(m/s)** | **(m2)** | **(m)** |  |
| 1560 | 0.18 | 132.46 | 132.71 | 132.72 | 0.001171 | 0.23 | 0.84 | 5.25 | 0.17 |
| 1540 | 0.18 | 132.44 | 132.68 | 132.68 | 0.002173 | 0.28 | 0.66 | 4.66 | 0.23 |
| 1520 | 0.18 | 132.43 | 132.57 | 132.59 | 0.018423 | 0.58 | 0.31 | 3.34 | 0.61 |
| 1500 | 0.18 | 132.25 | 132.54 | 132.55 | 0.000629 | 0.18 | 1.04 | 5.73 | 0.13 |
| 1480 | 0.18 | 132.18 | 132.53 | 132.53 | 0.000732 | 0.2 | 0.92 | 4.42 | 0.14 |
| 1460 | 0.18 | 132.23 | 132.52 | 132.52 | 0.000607 | 0.18 | 1 | 4.69 | 0.13 |
| 1440 | 0.18 | 132.24 | 132.5 | 132.5 | 0.000821 | 0.2 | 0.94 | 5.51 | 0.14 |
| 1420 | 0.18 | 132.25 | 132.48 | 132.48 | 0.002192 | 0.27 | 0.68 | 4.68 | 0.22 |
| 1400 | 0.18 | 132.2 | 132.46 | 132.46 | 0.000418 | 0.13 | 1.41 | 8.77 | 0.1 |
| 1380 | 0.18 | 132.25 | 132.45 | 132.45 | 0.001201 | 0.19 | 0.96 | 7.81 | 0.17 |
| 1360 | 0.18 | 132.24 | 132.42 | 132.42 | 0.001887 | 0.22 | 0.85 | 7.74 | 0.2 |
| 1340 | 0.18 | 132.2 | 132.38 | 132.38 | 0.001904 | 0.21 | 0.9 | 8.75 | 0.2 |
| 1320 | 0.18 | 132.15 | 132.36 | 132.36 | 0.00074 | 0.14 | 1.28 | 10.49 | 0.13 |
| 1300 | 0.18 | 132.11 | 132.33 | 132.33 | 0.00244 | 0.27 | 0.67 | 5 | 0.23 |
| 1284 | 0.18 | 132.05 | 132.26 | 132.27 | 0.007537 | 0.45 | 0.4 | 3.26 | 0.4 |
| 1259 | 0.18 | 131.64 | 132.27 | 132.27 | 0.00002 | 0.05 | 3.76 | 10.71 | 0.03 |
| 1240 | 0.18 | 131.78 | 132.26 | 132.26 | 0.000198 | 0.12 | 1.59 | 7.19 | 0.07 |
| 1219 | 0.18 | 132.06 | 132.24 | 132.25 | 0.010549 | 0.44 | 0.4 | 4.25 | 0.46 |
| 1200 | 0.18 | 131.79 | 132.21 | 132.22 | 0.000662 | 0.17 | 1.08 | 6.08 | 0.13 |
| 1178 | 0.18 | 131.81 | 132.18 | 132.19 | 0.003731 | 0.43 | 0.42 | 1.94 | 0.3 |
| 1155 | 0.18 | 131.81 | 131.99 | 132.02 | 0.01973 | 0.72 | 0.25 | 1.97 | 0.65 |
| 1142 | 0.18 | 131.51 | 132.01 | 132.01 | 0.000074 | 0.08 | 2.3 | 7.84 | 0.05 |
| 1116 | 0.18 | 131.64 | 132 | 132 | 0.000295 | 0.14 | 1.28 | 5.12 | 0.09 |
| 1104 | 0.18 | 131.6 | 132 | 132 | 0.000288 | 0.13 | 1.35 | 5.72 | 0.09 |
| 1081 | 0.18 | 131.64 | 131.98 | 131.98 | 0.002432 | 0.36 | 0.5 | 2.31 | 0.25 |
| 1060 | 0.18 | 131.62 | 131.81 | 131.85 | 0.032537 | 0.89 | 0.2 | 1.7 | 0.82 |
| 1043 | 0.18 | 130.97 | 131.11 | 131.14 | 0.055807 | 0.83 | 0.22 | 3.1 | 1 |
| 1020 | 0.18 | 130.66 | 131.02 | 131.03 | 0.001099 | 0.26 | 0.7 | 2.94 | 0.17 |
| 1000 | 0.18 | 130.72 | 130.95 | 130.97 | 0.013923 | 0.69 | 0.26 | 1.64 | 0.56 |
| 982 | 0.18 | 130.61 | 130.8 | 130.81 | 0.006 | 0.41 | 0.44 | 3.4 | 0.36 |
| 960 | 0.18 | 130.47 | 130.7 | 130.71 | 0.003407 | 0.35 | 0.52 | 3.3 | 0.28 |
| 940 | 0.18 | 130.37 | 130.62 | 130.63 | 0.004026 | 0.4 | 0.44 | 2.53 | 0.31 |
| 920 | 0.18 | 130.31 | 130.55 | 130.56 | 0.003203 | 0.37 | 0.49 | 2.73 | 0.28 |
| 900 | 0.18 | 130.19 | 130.48 | 130.49 | 0.004206 | 0.41 | 0.44 | 2.54 | 0.32 |
| 880 | 0.18 | 130.1 | 130.4 | 130.41 | 0.003384 | 0.37 | 0.49 | 2.79 | 0.28 |

**Tabla 10.: Eje Hidráulico en Canal 8 para un caudal de 0,9m3/s****

| River<br>Sta | Q<br>Total | Min Ch<br>El | W.S.<br>Elev | E.G.<br>Elev | E.G.<br>Slope | Vel<br>Chnl | Flow<br>Area | Top<br>Width | Froude #<br>Chl |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | **(m3/s)** | **(m)** | **(m)** | **(m)** | **(m/m)** | **(m/s)** | **(m2)** | **(m)** |  |
| 121 | 0.9 | 133.3 | 134.28 | 134.28 | 0.0003 | 0.26 | 3.89 | 10.03 | 0.11 |
| 101 | 0.9 | 133.56 | 134.27 | 134.28 | 0.000468 | 0.3 | 3.04 | 7.43 | 0.14 |
| 81 | 0.9 | 133.64 | 134.25 | 134.26 | 0.001124 | 0.4 | 2.32 | 7.34 | 0.21 |
| 61 | 0.9 | 133.41 | 134.24 | 134.24 | 0.000731 | 0.37 | 2.48 | 6 | 0.17 |
| 37 | 0.9 | 133.41 | 134.23 | 134.23 | 0.000359 | 0.28 | 3.36 | 6.82 | 0.12 |
| 18 | 0.9 | 133.74 | 134.21 | 134.22 | 0.001324 | 0.4 | 2.48 | 9.96 | 0.22 |
| 8 | 0.9 | 133.87 | 134.18 | 134.2 | 0.004004 | 0.57 | 1.69 | 8.23 | 0.37 |
