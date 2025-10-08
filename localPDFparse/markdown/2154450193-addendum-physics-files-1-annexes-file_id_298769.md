---
title: Sin título
author: Hugo Toledo A
date: D:20220427175816-04'00'
language: es
type: report
pages: 27
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - PARQUE FOTOVOLTAICO Y ALMACENAMIENTO COPIAPÓ ENERGÍA SOLAR
  - PARQUE FOTOVOLTAICO Y ALMACENAMIENTO COPIAPÓ ENERGÍA SOLAR
  - Control de Cambios
-->

## COPIAPÓ ENERGÍA SOLAR SPA

# PARQUE FOTOVOLTAICO Y ALMACENAMIENTO COPIAPÓ ENERGÍA SOLAR

## INFORME DE MODELACIÓN HIDRÁULICA LÍNEA DE ALTA TENSIÓN

Abril 2022

# PARQUE FOTOVOLTAICO Y ALMACENAMIENTO COPIAPÓ ENERGÍA SOLAR

## INFORME DE MODELACIÓN HIDRÁULICA LÍNEA DE ALTA TENSIÓN

##### COPIAPÓ ENERGÍA SOLAR SPA

VERSIÓN B

CONFIDENCIAL

COES0002-HID-MC-0004

FECHA: ABRIL 2022

WSP

Av. Las Condes 11.700

Vitacura, Santiago

CHILE

TELÉFONO: +56 2 2653 8000

wsp.com

# Control de Cambios

Revisión A Revisión B Revisión C Revisión D

|Elaborado por|Gustavo Vargas|Gustavo Vargas|Col4|Col5|
|---|---|---|---|---|
|Fecha|27.04.2022|27.04.2022|||
|Revisado por|Francisco<br>Berrios|Francisco<br>Berrios|||
|Fecha|27.04.2022|27.04.2022|||
|Aprobado por|Francisco<br>Berrios|Francisco<br>Berrios|||
|Fecha|27.04.2022|27.04.2022|||

**wsp.com**

**Código: COES0002-HID-MC-0004** **Página** 3 **de** 27

**Rev.: B** **Abril 2022**

1. INTRODUCCIÓN .............................................................................. 5

1.1 O BJETIVOS ................................................................................................ 6

2. REFERENCIAS ................................................................................. 6

3. ANTECEDENTES .............................................................................7

3.1 H IDROLOGÍA ............................................................................................ 7

3.2 T OPOGRAFÍA ........................................................................................... 8

3.3 G RANULOMETRÍA ................................................................................ 10

3.4 L ÍNEA A LTA T ENSIÓN (LAT) PROYECTADA ............................... 12

4. METODOLOGÍA ............................................................................. 14

4.1 C ONSIDERACIONES INICIALES ........................................................ 14

4.2 M ETODOLOGÍA DE T RABAJO .......................................................... 14

4.3 E LEMENTOS DE M ODELACIÓN H IDRÁULICA ........................... 15

4.3.1 Caudales de crecida ................................................................. 15

4.3.2 Área de flujo 2D y malla de simulación ..................... 16

4.3.3 Rugosidad del cauce ............................................................... 17

4.3.4 Régimen de escurrimiento y condiciones de

borde .................................................................................................................. 18

5. RESULTADOS ................................................................................. 22

6. COMENTARIOS Y CONCLUSIONES ................................. 26

**wsp.com**

**Código: COES0002-HID-MC-0004** **Página** 4 **de** 27

**Rev.: B** **Abril 2022**

## 1. INTRODUCCIÓN

La empresa Copiapó Energía Solar SpA (en adelante COES) ha solicitado a WSP el

desarrollo de la ingeniería del Parque Fotovoltaico Copiapó Solar, ubicado en la región de

Atacama a unos 80 km al noreste de la ciudad de Copiapó.

En la Figura 1-1 se presenta la ubicación general del Proyecto. El parque fotovoltaico tendrá

aproximadamente 150 MWac de potencia y se conectará a Sistema Eléctrico Nacional

(SEN) en la subestación eléctrica (SE) Carrera Pinto de 220 kV.

Figura 1-1: Ubicación General del Proyecto

**wsp.com**

**Código: COES0002-HID-MC-0004** **Página** 5 **de** 27

**Rev.: B** **Abril 2022**

### 1.1 Objetivos

El presente estudio tiene por objeto determinar las características del escurrimiento en los

cauces existentes que interfieren con el desarrollo de la Línea de Alta Tensión proyectada,

durante la ocurrencia de una crecida de 100 años de periodo de retorno para la condición

sin proyecto y evaluar la posible afectación de las obras proyectadas.

## 2. REFERENCIAS

REF. 1 Proyecto de Levantamiento con Láser Aerotransportado y Cámara Aérea

Digital Copiapó Solar - Informa Final, FRUGO INTERRA, 2014.

REF. 2 Estudio Geotécnico Proyecto Copiapó Solar - Informe Geotécnico, Arcadis,

2015.

REF. 3 Estudio Hidrológico, COES0002-HID-INF-0003, WSP, 2022.

REF. 4 Informe de Modelación Hidráulica, COES0002-HID-MC-0002, WSP, 2022.

REF. 5 Hydraulic Reference Manual, Hydrologic Engineering Center, 2016.

REF. 6 Experimental Study on Debris Flows Over a Non-Erodible Bed. Tamburrino,

Espinoza and Niño. Rivertech 96 Chicago Illinois USA.

**wsp.com**

**Código: COES0002-HID-MC-0004** **Página** 6 **de** 27

**Rev.: B** **Abril 2022**

## 3. ANTECEDENTES

### 3.1 Hidrología

Los hidrogramas de crecida de 10, 20, 25, 50, 100, 150 y 200 años de periodos de retorno

utilizados en el análisis hidráulico de la zona del proyecto corresponden a aquellos

determinados en el documento GA0004-HID-INF-0001 “Estudio Hidrológico”. La Figura 3-1

y Tabla 3-1 a continuación muestran los hidrogramas de crecidas para distintos periodos

de retorno para las cuencas aportantes a la LAT proyectada, mientras que la Tabla 3-1

muestra el caudal peak de estos.

Figura 3-1: Hidrograma de crecidas Cuenca LAT

Fuente: REF. 3

Tabla 3-1: Caudal máximo en Cuenca LAT

<!-- INICIO TABLA 3-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Figura 3-1: Hidrograma de crecidas Cuenca LAT Fuente: REF. 3 -->

**Tabla 3-1: Caudal máximo en Cuenca LAT**

| T (años) | Caudal Máximo (m3/s) |
| --- | --- |
| 10 | 6,5 |
| 20 | 25,5 |
| 25 | 34,3 |
| 50 | 71,9 |
| 100 | 124,2 |
| 150 | 165,3 |
| 200 | 196,8 |

<!-- Estadísticas: 7 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: REF. 3 **wsp.com** -->
<!-- FIN TABLA 3-1 -->


|T (años)|Caudal Máximo (m3/s)|
|---|---|
|10|6,5|
|20|25,5|
|25|34,3|
|50|71,9|
|100|124,2|
|150|165,3|
|200|196,8|

Fuente: REF. 3

**wsp.com**

**Código: COES0002-HID-MC-0004** **Página** 7 **de** 27

**Rev.: B** **Abril 2022**

### 3.2 Topografía

Se desarrolló un levantamiento topográfico con Sistema Laser aerotransportado y cámara

digital, cubriendo un área total de 2.684 hectáreas (REF. 1). Este levantamiento consideró

la realización de trabajos de terreno y la posterior la revisión de calidad de la información

proveniente de la captura de los datos LIDAR, referenciados en el sistema SIRGAS. Junto

con la revisión de los puntos láser, se efectuó la revisión de la captura de imágenes y la

calidad de estas mediante la inspección visual de las imágenes brutas, revisión del

histograma RGB de las imágenes y revisión de la cobertura de las imágenes logradas en

la misión.

Posterior a la verificación y generación de las coberturas obtenidas mediante los métodos

empleados, se procede a calibrar la nube de puntos, generando una cobertura

homogénea no afecta por los errores provenientes de la captura de información. Una vez

realizada la calibración, corrección, etc. Se procede a la clasificación automática de los

puntos, la cual consiste en clasificar los puntos laser como terreno (Ground) y no terreno

(no Ground) mediante un algoritmo que separa los puntos en las dos clases antes

señaladas, adicionalmente se complementa este proceso mediante clasificación manual,

con el objetivo de generan un modelo preciso y que represente la realidad del terreno.

La Figura 3-2 muestra el área considerada para el levantamiento topográfico.

**wsp.com**

**Código: COES0002-HID-MC-0004** **Página** 8 **de** 27

**Rev.: B** **Abril 2022**

Figura 3-2: Área de levantamiento topográfico

Fuente: Elaboración propia

Los resultados obtenidos del levantamiento desarrollado son los siguientes:

 - Ortofotos en sistema SIRGAS, escalas 1:500 y 1:1000.

 - Cartografía en sistema SIRGAS, escalas 1:500 y 1:1000.

 - Curvas de Nivel escala 1:500, Modelo de curvas de nivel principales cada 0,5 m y

curvas índice cada 2,5 m

 - Curvas de Nivel escala 1:1000, Modelo de curvas de nivel principales cada 1,0 m y

curvas índice cada 5,0 m

 - Modelo digital de Terreno.

**wsp.com**

**Código: COES0002-HID-MC-0004** **Página** 9 **de** 27

**Rev.: B** **Abril 2022**

### 3.3 Granulometría

La información granulométrica utilizada para el análisis es obtenida de un estudio

desarrollado por ARCADIS (REF. 2), en la zona de emplazamiento del proyecto fotovoltaico.

El estudio geotécnico mencionado anteriormente, presenta información granulométrica

de una gran cantidad de calicatas, en particular se realizaron 10 sondajes geotécnicos y 32

calicatas de 4 m de profundidad, siendo 9 de estas realizadas en el sector de

emplazamiento del parque fotovoltaico.

Del análisis de las calicatas, se observa que el suelo de fundación es homogéneo hasta las

profundidades prospectadas (80m) y no presenta variación que permitan diferenciar

geotécnicamente las diversas áreas del proyecto. Los materiales clasifican en forma

predominante como arenas gravosas con limos (SW-SM, SP-SM) y arenas gravo-limosas

(SM).

En la Figura 3-3 se muestra la ubicación de las calicatas realizadas en el sector de

emplazamiento del parque siendo estas las que serán utilizadas para el análisis a

desarrollar en este documento.

**wsp.com**

**Código: COES0002-HID-MC-0004** **Página** 10 **de** 27

**Rev.: B** **Abril 2022**

Figura 3-3: Ubicación calicatas consideradas para el análisis

Fuente: Elaboración propia

Adicionalmente, en la Figura 3-4, se muestran las curvas granulométricas de las calicatas

utilizadas en el sector de estudio.

Figura 3-4: Curvas granulométricas consideradas para el sector de estudio

Fuente: REF. 2

**wsp.com**

**Código: COES0002-HID-MC-0004** **Página** 11 **de** 27

**Rev.: B** **Abril 2022**

### 3.4 Línea Alta Tensión (LAT) proyectada

Se proyecta construir una línea eléctrica de circuito simple en 220kV entre la subestación

Elevadora del proyecto y la Subestación Carrera Pinto, propiedad de Transelec, ubicado a

21 km al sur de la localidad de Inca de Oro en la comuna de Copiapó.

La Línea de Alta Tensión (LAT) se proyecta en una configuración de circuito simple en

220kV con una capacidad de 260MW en disposición aérea triangular, de categoría C con

una longitud de 8890 m. Su trazado se inicia en la S/E Elevadora Copiapó Solar ubicada a

un extremo del sitio del proyecto, las coordenadas UTM de la primera estructura son

417545,21mE - 7015855,99mN a 1992 m.s.n.m. y finaliza con la estructura 27 entrando a la

S/E Carrera Pinto con coordenadas UTM: 410536,20mE - 7013205,70mN a 1766 m.s.n.m.

Debido a las condiciones del terreno y obstáculos en el trazado, se han contemplado para

la línea tres tipos de estructuras (torres), una del tipo suspensión y 2 de anclaje. El vano

promedio es de 286m y el vano máximo llega hasta los 435m. El valor de la franja de

seguridad se ha considerado en 40m (20m para cada lado desde el eje del trazado).

En la Figura 3-5 se muestra la LAT junto a sus torres proyectadas.

**wsp.com**

**Código: COES0002-HID-MC-0004** **Página** 12 **de** 27

**Rev.: B** **Abril 2022**

Figura 3-5: Línea de Alta Tensión proyectada

Fuente: Elaboración propia

**wsp.com**

**Código: COES0002-HID-MC-0004** **Página** 13 **de** 27

**Rev.: B** **Abril 2022**

## 4. METODOLOGÍA

### 4.1 Consideraciones iniciales

El estudio hidráulico se evalúa para el evento de crecida asociado a un período de retorno

de 100 años, considerando la situación actual, o sin proyecto, en el sector de estudio,

desarrollado sobre la base de la topografía descrita en el acápite anterior.

El análisis hidráulico se efectúa tomando en consideración los hidrogramas de crecidas

para las cuencas aportantes en el sector de emplazamiento de las obras que componen

el proyecto.

La modelación hidráulica se realiza con el software computacional HEC-RAS, programa

desarrollado por el Cuerpo de Ingenieros de la Armada de Estados Unidos (US Army Corps

of Engineers) el cual permite resolver el cálculo del eje hidráulico en modelos de terreno,

usando un modelo numérico hidrodinámico de flujo bidimensional basado en la

metodología de escurrimiento no estacionario (ecuaciones de Saint Venant) y resolución

de ecuaciones por el algoritmo de Volúmenes Finitos Implícitos, y así determinar las

alturas de agua, velocidades y demás parámetros hidráulicos de interés (REF. 5).

### 4.2 Metodología de Trabajo

El procedimiento para determinar el eje hidráulico y las zonas de inundación asociadas al

período de retorno evaluado considera los siguientes pasos:

i. Elaboración de un modelo de terreno en HEC-RAS basado en la topografía del

terreno. Se desarrolla una malla computacional 2D con una grilla de resolución

adecuada al modelo de terreno. El área de flujo del polígono 2D creado considera

toda el área de estudio (incluyendo las obras de canalización proyectadas).

ii. Se determinan sectores de flujo preferente crea dada por la red hidrográfica

detectada en la zona durante la visita a terreno y por el análisis del modelo de

terreno mediante herramientas GIS.

iii. Se imponen las condiciones de borde que definirán la escorrentía en el área de flujo

2D. Estas condiciones corresponden a un hidrograma de flujo de entrada para el

**wsp.com**

**Código: COES0002-HID-MC-0004** **Página** 14 **de** 27

**Rev.: B** **Abril 2022**

período de retorno a evaluar en el sector de aguas arriba modelado, y condición de

altura normal de salida en el sector de aguas abajo.

iv. Se incorpora la alcantarilla proyectada en una de las canalizaciones consideradas

durante el cruce con un camino interior proyectado, mediante una conexión del

tipo 1D/2D.

v. Finalmente, se ejecuta el modelo 2D de flujo impermanente con el programa HEC

RAS. El modelo se ejecuta resolviendo las ecuaciones de Saint Venant y

considerando un régimen de flujo mixto, para trabajar de manera más adecuada

las transiciones de flujo subcrítico a supercrítico y viceversa.

### 4.3 Elementos de Modelación Hidráulica

La elaboración del modelo hidráulico en el sector de emplazamiento y análisis se realizó

mediante la aplicación del software HEC-RAS, en su versión 5.0.7, el cual resuelve el cálculo

del eje hidráulico usando un modelo numérico hidrodinámico de flujo bidimensional

basado en la metodología de escurrimiento no estacionario.

Los antecedentes para la simulación se detallan en los puntos siguientes.

#### 4.3.1 Caudales de crecida

Dada la magnitud de los caudales de crecida y de las condiciones de los suelo observados

en la zona de emplazamiento de la Línea de Alta Tensión (LAT) proyectada durante la visita

a terreno y de las imágenes satelitales, se ha considerado apropiado asumir que frente a

un evento climático de magnitud importante (evento de 100 años de periodo de retorno)

se desarrollará flujo detrítico, con una concentración de sólidos del 30% de acuerdo a lo

estipulado en REF. 6. Los caudales detríticos utilizados para la modelación hidráulica del

sector en estudio han sido determinados a partir de los hidrogramas de crecida líquida

obtenidos en el estudio hidrológico de la REF. 3 y presentados en la Figura 3-1, a través de

la siguiente expresión:

Q detr = 1 −C [Q] [li][q]

**wsp.com**

**Código: COES0002-HID-MC-0004** **Página** 15 **de** 27

**Rev.: B** **Abril 2022**

Donde:

Q detr : Caudal detrítico, m3/s

Q liq : Caudal líquido, m3/s

C : Concentración en volumen de sólidos

Los hidrogramas de caudal detrítico para un periodo de retorno de 100 años para la cuenca

afluente a la LAT en la zona de interés, se muestra en la figura a continuación.

Figura 4-1: Hidrograma de crecida detrítica asociada a 100 años de periodo de retornoCuenca LAT

Fuente: Elaboración propia

#### 4.3.2 Área de flujo 2D y malla de simulación

Se ha desarrollado una malla no estructurada compuesta por celdas que pueden llegar a

tener hasta 8 caras, en las cuales se irá almacenando información de las propiedades

hidráulicas del terreno, tales como perímetro mojado, radio hidráulico, coeficiente de

rugosidad, volumen, etc. Esta información es utilizada por el modelo para ir resolviendo las

ecuaciones de cantidad de movimiento y continuidad en toda la malla.

La malla de modelación hidráulica elaborada para la zona de estudio está compuesta por

12894 celdas, desarrollada a partir de una grilla base con celdas de 5 x 5 m y refinada

posteriormente en sectores en particulares (p. ej. zonas elevadas, ejes de quebradas, entre

otros.) a través de breaklines y zonas de refinamiento con celdas de dimensiones entre 2,5

m y 1 m. La Figura 4-2 muestra la malla de modelación elaborada para el sector de estudio.

**wsp.com**

**Código: COES0002-HID-MC-0004** **Página** 16 **de** 27

**Rev.: B** **Abril 2022**

Figura 4-2: Malla de modelación hidráulica 2D elaborada

Fuente: Elaboración propia

#### 4.3.3 Rugosidad del cauce

El coeficiente de rugosidad de Manning para flujo liquido adoptado, ha sido aquel

obtenido en el estudio hidráulico de la REF. 4 para el sector del parque fotovoltaico

proyectado, correspondiente a 0,035. Sin embargo como se ha mencionado

anteriormente, para este análisis hidráulico se ha considerado que se desarrollara flujo

detrítico durante el paso de la crecida, por lo cual el valor del coeficiente de rugosidad ha

sido amplificado en 1,75, tomando en consideración desde el punto de vista conservador

que el coeficiente de rugosidad de Manning para flujo detrítico podría ser entre 50 y 75%

mayor al coeficiente para flujo líquido, de acuerdo a lo expuesto en la REF. 6. Finalmente

se adopta un coeficiente de rugosidad de 0,06.

**wsp.com**

**Código: COES0002-HID-MC-0004** **Página** 17 **de** 27

**Rev.: B** **Abril 2022**

#### 4.3.4 Régimen de escurrimiento y condiciones de borde

Para desarrollar una correcta modelación de crecidas del sector en estudio, el software es

capaz de utilizar un régimen de escurrimiento mixto a lo largo de todo el sector de análisis,

con la finalidad de trabajar de manera más adecuada las transiciones de flujo subcrítico a

supercrítico y viceversa.

Para el caso de la condición de borde aguas abajo presentada en la Figura 4-5, se ha

considerado altura normal de escurrimiento con una pendiente de los cauces equivalente

a 0,15% obtenida del Modelo Digital de Terreno (MDT) obtenido a partir del levantamiento

topográfico realizado en el sector de estudio.

Para las condiciones de borde aguas arriba o de entrada se han ingresado hidrogramas de

crecida de 100 años de periodo de retorno. Para una mejor representación del flujo que

ingresa a la malla de modelación se han tomado las siguientes consideraciones.

 - División de la cuenca afluente a la LAT determinada en el estudio hidrológico en

dos subcuencas, la primera denominada Subcuenca N°1 la cual aporta escorrentía

a la quebrada ubicada inmediatamente al oriente de la ruta C-17 y la segunda

denominada Subcuenca N°2 la cual aporta escorrentía al resto de quebradas

ubicadas al oriente de la ruta C-17 que interfieren con la LAT. En la Figura 4-3 se

muestran las subcuencas delimitadas, mientras que en la Tabla 4-1 sus áreas

aportantes respectivas.

**wsp.com**

**Código: COES0002-HID-MC-0004** **Página** 18 **de** 27

**Rev.: B** **Abril 2022**

Figura 4-3: Subcuencas aportantes a Línea de Alta Tensión

Fuente: Elaboración propia

Tabla 4-1: Área aportante subcuencas N°1 y N°2

<!-- INICIO TABLA 4-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Figura 4-3: Subcuencas aportantes a Línea de Alta Tensión Fuente: Elaboración propia -->

**Tabla 4-1: Área aportante subcuencas N°1 y N°2**

| Cuenca | Área (km2) |
| --- | --- |
| Subcuenca N°1 | 37,3 |
| Subcuenca N°2 | 256,7 |

<!-- Estadísticas: 2 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia - Hidrogramas de crecida para las subcuencas N°1 y N°2 (ver Figura 4-4) -->
<!-- FIN TABLA 4-1 -->


|Cuenca|Área (km2)|
|---|---|
|Subcuenca N°1|37,3|
|Subcuenca N°2|256,7|

Fuente: Elaboración propia

 - Hidrogramas de crecida para las subcuencas N°1 y N°2 (ver Figura 4-4)

determinados mediante transposición por área a partir de la cuenca afluente a la

LAT. En la Tabla 4-2 se muestran los caudales máximos determinados para las

subcuencas N°1 y N°2.

**wsp.com**

**Código: COES0002-HID-MC-0004** **Página** 19 **de** 27

**Rev.: B** **Abril 2022**

Tabla 4-2: Caudal Peak de crecida detrítica para 100 años de periodo de retorno, m [3] /s.

<!-- INICIO TABLA 4-2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **Código: COES0002-HID-MC-0004** **Página** 19 **de** 27 **Rev.: B** **Abril 2022** -->

**Tabla 4-2: Caudal Peak de crecida detrítica para 100 años de periodo de retorno, m [3] /s.**

| Subcuenca N°1 | Subcuenca N°2 |
| --- | --- |
| 21,8 | 155,6 |

<!-- Estadísticas: 1 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia Figura 4-4: Hidrograma de crecida detrítica de 100 años de periodo de retorno para -->
<!-- FIN TABLA 4-2 -->


|Subcuenca N°1|Subcuenca N°2|
|---|---|
|21,8|155,6|

Fuente: Elaboración propia

Figura 4-4: Hidrograma de crecida detrítica de 100 años de periodo de retorno para

cuenca LAT y subcuencas

Fuente: Elaboración propia

 - Para una mejor representación de la distribución de la escorrentía por las

quebradas que conforman la Subcuenca N°2, se ha modelado hidráulicamente un

sector aguas arriba de la zona de interés en cuestión, de tal manera de obtener los

hidrogramas de entrada para el modelo en el sector de la LAT a partir de los

resultados obtenidos en la salida del modelo desarrollado aguas arriba. La Figura

4-5 a continuación muestra esquemáticamente el procedimiento recién descrito.

**wsp.com**

**Código: COES0002-HID-MC-0004** **Página** 20 **de** 27

**Rev.: B** **Abril 2022**

Figura 4-5: Esquema de transferencia de hidrogramas de entrada para modelo

hidráulico 2D en sector de estudio

Fuente: Elaboración propia

 - Las condiciones de entrada para el modelo desarrollado en el sector de la LAT

corresponden a aquellas presentadas en la Figura 4-5, utilizando los hidrogramas

obtenidos del modelo desarrollado aguas arriba de la zona de interés, que se

presentan en la figura a continuación.

**wsp.com**

**Código: COES0002-HID-MC-0004** **Página** 21 **de** 27

**Rev.: B** **Abril 2022**

Figura 4-6: Hidrogramas de entrada para modelo hidráulico 2D en sector de estudio

Fuente: Elaboración propia

## 5. RESULTADOS

La Figura 5-1 muestra la extensión de la inundación obtenida por el modelo hidráulico para

una crecida detrítica de 100 años de periodo de retorno en el sector de estudio. Los

resultamos muestran alturas de escurrimiento máximas del orden de 1,4 m y velocidades

máximas cercanas a los 2,5 m/s (ver Figura 5-2), además se tiene en su mayoría

escurrimiento subcrítico (ver Figura 5-3). En relación a la interacción de la escorrentía con

las torres de la LAT, los resultados del modelo muestran que la inundación no logra

alcanzar las torres N°24 y N°25 que se emplazan en el sector modelado, ya que estas se

ubican en sectores elevados y adyacentes a los cauces principales o zonas preferenciales

de escurrimiento, en particular se tiene que la Torre N°24 y Torre N°25 se ubicarían

aproximadamente a 50 cm y 30 cm por sobre el nivel de escurrimiento respectivamente.

En la Figura 5-4 se muestra un perfil transversal al escurrimiento, donde es posible

visualizar que las torres se ubican en sector elevados y que no son afectadas por la crecida

de 100 años de periodo de retorno.

**wsp.com**

**Código: COES0002-HID-MC-0004** **Página** 22 **de** 27

**Rev.: B** **Abril 2022**

Figura 5-1: Área de inundación sector en estudio - T=100 años

Fuente: Elaboración propia

Figura 5-2: Velocidad de escurrimiento sector de estudio - T=100 años

Fuente: Elaboración propia

**wsp.com**

**Código: COES0002-HID-MC-0004** **Página** 23 **de** 27

**Rev.: B** **Abril 2022**

Figura 5-3: N° de Froude sector de estudio - T=100 años

Fuente: Elaboración propia

**wsp.com**

**Código: COES0002-HID-MC-0004** **Página** 24 **de** 27

**Rev.: B** **Abril 2022**

Figura 5-4: Sección transversal al escurrimiento en sector de emplazamiento de Torre

N°24 y N°25

Fuente: Elaboración propia

**wsp.com**

**Código: COES0002-HID-MC-0004** **Página** 25 **de** 27

**Rev.: B** **Abril 2022**

## 6. COMENTARIOS Y CONCLUSIONES

El análisis hidráulico presentado en este Informe hace referencia a las crecida de 100 años

de período de retorno de las quebradas que interfieren con el desarrollo de la Línea de Alta

Tensión (LAT) proyectada.

Se ha desarrollado un modelo hidráulico 2D en el sector de emplazamiento de la LAT

considerando una crecida detrítica de 100 años de periodo de retorno. Los resultados del

modelo, muestra escurrimiento con régimen subcrítico, con alturas y velocidades de

escurrimiento máximas de 1,4 m y 2,5 m/s respectivamente. Por otro lado, los resultados

muestran que las Torres N°24 y 25 no serían afectadas por la crecida, puesto que estas se

ubicarían en sectores elevado del terreno, aproximadamente a 50 cm y 30 cm por sobre el

nivel de escurrimiento respectivamente.

**wsp.com**

**Código: COES0002-HID-MC-0004** **Página** 26 **de** 27

**Rev.: B** **Abril 2022**

Avda. Las Condes 11.700

Edificio San Damián

Vitacura

Santiago, Chile

www.wsp.com

**wsp.com**

**Código: COES0002-HID-MC-0004** **Página** 27 **de** 27

**Rev.: B** **Abril 2022**