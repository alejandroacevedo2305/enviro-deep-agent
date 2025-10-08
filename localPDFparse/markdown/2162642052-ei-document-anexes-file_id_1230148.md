---
title: Sin título
author: Desconocido
date: Sin fecha
language: es
type: manual
pages: 35
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - APÉNDICE 2 MODELO HIDRÁULICO PAS 156
-->

# APÉNDICE 2 MODELO HIDRÁULICO PAS 156

Baqua Ingeniería

[www.baqua.cl](https://www.baqua.cl/)
[contacto@baqua.cl](mailto:contacto@baqua.cl)

APÉNDICE 2. MODELO HIDRÁULICO

## PERMISO AMBIENTAL SECTORIAL 156 SISTEMA DE ALMACENAMIENTO DE ENERGÍA ALTAIR

para SPHERA ENERGY

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
|0|-|17/07/2024|Ingreso DIA|DPP|BGP|ABL|
|A|-|12/07/2024|Revisión cliente|DPP|BGP|ABL|
|Rev.|Rev. Int.|Fecha|Emitido para|Emitido por|Revisado por|Aprobado por|

|Col1|Comuna de Molina<br>Región del Maule|Col3|
|---|---|---|
||SPH-B24006-PAS156-DOC-02-0|Rev. 0|

APÉNDICE 2. MODELO HIDRÁULICO

PERMISO AMBIENTAL SECTORIAL 156
SISTEMA DE ALMACENAMIENTO DE ENERGÍA

ALTAIR

### Contenidos

1. Introducción ............................................................................................................................................. 4

2. Descripción del modelo.......................................................................................................................... 4

3. Parámetros de entrada ......................................................................................................................... 5

3.1. Obra existente ....................................................................................................................................... 5

3.2. Obras proyectadas ............................................................................................................................... 7

3.2.1. Proyección obra de atravieso OA 01 ................................................................................................... 8

3.2.2. Proyección obra de atravieso OA 02 ................................................................................................. 10

3.3. Coeficiente de rugosidad .................................................................................................................. 13
3.4. Condiciones de borde e iniciales ..................................................................................................... 16

3.5. Otras consideraciones........................................................................................................................ 19

4. Resultados .............................................................................................................................................. 19

4.1. Condición sin proyecto ..................................................................................................................... 20
4.2. Condición con proyecto .....................................................................................................................25

4.3. Resumen de resultados.................................................................................................................... 29

4.3.1. Obra de atravieso OA 01 ...................................................................................................................... 29

4.3.2. Obra de atravieso OA 02 ..................................................................................................................... 30

4.3.3. Camino de acceso AB ............................................................................................................................ 31

5. Referencias ............................................................................................................................................ 33

### Figuras

Figura 3-1. Ubicación de obras existentes y Layout (color gris) ............................................................................... 6

Figura 3-2. Obra existente OE_01 .................................................................................................................................. 7

Figura 3-3. Topografía de la zona de estudio de la obra OA 01, incluyendo una representación del camino

(color gris). Condición sin proyecto ................................................................................................................................ 8

Figura 3-4. Topografía de la zona de estudio de la obra OA 01, incluyendo una representación del camino

(color gris). Condición con proyecto ............................................................................................................................... 9

Figura 3-5. Topografía de la zona de estudio de la obra OA 02, incluyendo una representación del camino y

pandereta (color gris). Condición sin proyecto .......................................................................................................... 10

ii Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 2. MODELO HIDRÁULICO

PERMISO AMBIENTAL SECTORIAL 156
SISTEMA DE ALMACENAMIENTO DE ENERGÍA

ALTAIR

Figura 3-6. Topografía de la zona de estudio de la obra OA 02, incluyendo una representación del camino y

cerco (color gris). Condición con proyecto ....................................................................................................................11

Figura 3-7. Topografía de la zona de estudio del camino de la OA 02 (color gris). Condición sin proyecto ... 12

Figura 3-8. Topografía de la zona de estudio del camino de la OA 02 (color gris). Condición con proyecto . 13

Figura 3-9. Ortofoto de terreno en ubicación de las obras OA 01 y OA 02, incluyendo una representación del

layout (color negro) ........................................................................................................................................................ 14

Figura 3-10. Registro fotográfico visita a terreno en ubicación de la obra OA 01 ............................................... 15

Figura 3-11. Registro fotográfico visita a terreno en ubicación de la obra OA 02 ................................................ 15

Figura 3-12. Ubicación condiciones de borde, layout (negro) y zona de refinamiento (rojo) ............................. 17

Figura 3-13. Hidrogramas de entrada. Crecida de diseño (100 años) .................................................................... 18

Figura 3-14. Hidrogramas de entrada. Crecida de verificación (150 años) ........................................................... 18

Figura 4-1. Profundidad máxima. Crecida de diseño (100 años). Condición sin proyecto ................................. 20

Figura 4-2. Velocidad máxima. Crecida de diseño (100 años). Condición sin proyecto ...................................... 21

Figura 4-3. Profundidad máxima. Crecida de verificación (150 años). Condición sin proyecto ........................ 22

Figura 4-4. Velocidad máxima. Crecida de verificación (150 años). Condición sin proyecto ............................ 23

Figura 4-5. Hidrograma a la salida del modelo. Condición sin proyecto .............................................................. 24

Figura 4-6. Profundidad máxima. Crecida de diseño (100 años). Condición con proyecto ............................... 25

Figura 4-7. Velocidad máxima. Crecida de diseño (100 años). Condición con proyecto .................................... 26

Figura 4-8. Profundidad máxima. Crecida de verificación (150 años). Condición con proyecto ...................... 27

Figura 4-9. Velocidad máxima. Crecida de verificación (150 años). Condición con proyecto ........................... 28

Figura 4-10. Hidrograma a la salida del modelo. Condición con proyecto ........................................................... 29

Figura 4-11. Polígono obra OA 01 (color rojo) para los resultados de profundidad y velocidad ....................... 30

Figura 4-12. Polígono obra OA 02 (color rojo) para los resultados de profundidad y velocidad ....................... 31

Figura 4-13. Tramos referenciales (color rojo) para los resultados de profundidad y velocidad...................... 32

### Tablas

Tabla 2-1. Descripción general de los modelos hidráulicos ........................................................................................ 4

Tabla 3-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan ......................16

Tabla 3-2. Condiciones de borde e iniciales .................................................................................................................16

Tabla 4-1. Resultados de la obra OA 01 ...................................................................................................................... 30

Tabla 4-2. Resultados de la obra OA 02 ...................................................................................................................... 31

Tabla 4-3. Resultados del camino de acceso AB situación Sin Proyecto .............................................................. 32

Tabla 4-4. Resultados del camino de acceso AB situación Con Proyecto ............................................................ 32

iii Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 2. MODELO HIDRÁULICO

PERMISO AMBIENTAL SECTORIAL 156
SISTEMA DE ALMACENAMIENTO DE ENERGÍA

ALTAIR

#### 1. Introducción

Se construyó el modelo hidráulico de las obras de atravieso denominadas OA 01 y OA 02 emplazadas sobre

el cauce natural sin nombre. Para la elaboración del modelo, se utilizó el software HEC-RAS (HEC, 2024). El

objetivo del modelo es representar la condición actual del cauce, sin proyecto, y su condición futura, con

proyecto, para los caudales de diseño y verificación de la obra.

Los resultados entregados por el software permitirán conocer las características del flujo y la superficie

inundada para cada condición. A continuación, se presentan las principales consideraciones para elaborar los

modelos y los resultados más relevantes en cada caso.

#### 2. Descripción del modelo

El modelo se construyó con el software HEC-RAS, utilizando para su cálculo un flujo bidimensional. La

descripción general de cada modelo se representa en la Tabla 2-1.

Tabla 2-1. Descripción general de los modelos hidráulicos

|Condición|Descripción|Objetivo|
|---|---|---|
|Sin Proyecto|Representa la condición actual del cauce, en una extensión total de<br>420 m a lo largo de su eje, centrado en las obras proyectadas y<br>manteniendo más de 120 m hacia aguas arriba y hacia aguas abajo<br>desde el inicio y fin de cada obra proyectada.<br> <br>Este modelo incluye la representación de una obra existente (OE_01),<br>correspondiente a una pandereta compuesta por muros prefabricados<br>de hormigón de 1.8 m de alto, 2 m de largo y 2.5 cm de ancho. En la<br>zona del atravieso de cauce, posee una apertura de 1 m de alto y 2 m<br>de largo, sobre un muro de 0.3 m altura y 2 m de largo desde el fondo<br>del cauce.<br>|Representar<br>la<br>condición<br>actual<br>del<br>cauce|
|Con Proyecto|Representa la condición futura del cauce. Mantiene las características<br>del modelo Sin Proyecto, sin embargo la pandereta existente es<br>remplazada por un cerco perimetral y se incorporan las obras<br>proyectadas: (i) OA 01, correspondiente a un badén de mampostería<br>de piedra de sección compuesta con (a) una sección principal de base<br>15 m, altura variable entre 0.3 y 0.4 m, talud de 10:1 (H:V) y longitud<br>de 6.0 m, y (b) una sección secundaria con base de 2 m, altura variable<br>entre 0.4 y 0.5 m, talud de 10:1 (H:V) y longitud de 6.0 m; y (ii) OA 02,|Representar<br>la<br>condición<br>futura<br>del<br>cauce|

4 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 2. MODELO HIDRÁULICO

PERMISO AMBIENTAL SECTORIAL 156
SISTEMA DE ALMACENAMIENTO DE ENERGÍA

ALTAIR

|Condición|Descripción|Objetivo|
|---|---|---|
||badén de mampostería de piedra de sección compuesta con (a) una<br>sección principal de base 15 m, altura de 0.3 m en la sección del camino<br>y 0.6 m en la sección del cerco, talud de 10:1 (H:V) y longitud de 8 m, y<br>(b) una sección secundaria con base de 2 m, altura de 0.5 m, talud de<br>10:1 (H:V) y longitud de 8 m. Adicionalmente, se incluye la carpeta de<br>rodado del camino de acceso entre dos sectores del Área de Baterías,<br>el cual tiene un ancho basal de 6.0 m y mantiene el nivel del terreno<br>natural.||

Cabe destacar, que el camino de acceso asociado a la OA 02 posee algunos tramos que están cubiertos por

la zona de inundación. Sin embargo, las profundidades y velocidades en estas zonas son muy pequeñas, por

lo tanto, no es necesario incluir una obra hidráulica en esos tramos. En el capítulo 4.3 se presenta un resumen

de los resultados de profundidad y velocidad del camino de acceso.

#### 3. Parámetros de entrada 3.1. Obra existente

Para representar la condición actual del cauce, se incluyó en la situación Sin Proyecto una obra existente que

fue identificada durante la visita a terreno realizada el día 13/05/2023. En la Figura 3-1 se muestra su

ubicación y en la Figura 3-2 una fotografía de la obra existente registrada durante la visita a terreno.

5 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 2. MODELO HIDRÁULICO

PERMISO AMBIENTAL SECTORIAL 156
SISTEMA DE ALMACENAMIENTO DE ENERGÍA

ALTAIR

Figura 3-1. Ubicación de obras existentes y Layout (color gris)

6 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 2. MODELO HIDRÁULICO

PERMISO AMBIENTAL SECTORIAL 156
SISTEMA DE ALMACENAMIENTO DE ENERGÍA

ALTAIR

Figura 3-2. Obra existente OE_01

Esta obra fue incorporada en el modelo de la situación Sin Proyecto mediante el uso de las herramientas de

modificación de terreno de Ras Mapper. Cabe destacar que, por simplificación del modelo, solo se incorporó

el muro de 0.3 m de alto en el lecho del cauce y los muros laterales a este de 1.8 m de alto; además se le dio

un espesor al muro de 0.4 m para que el software pudiera identificar la existencia de la pandereta y evitar

así posibles errores numéricos de modelación.

#### 3.2. Obras proyectadas

La obra de atravieso se proyectó mediante herramientas de geometría de HEC-RAS y las modificaciones de

terreno de RAS Mapper. A continuación, se muestra el terreno sin y con la obra incorporada.

7 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 2. MODELO HIDRÁULICO

PERMISO AMBIENTAL SECTORIAL 156
SISTEMA DE ALMACENAMIENTO DE ENERGÍA

ALTAIR

#### 3.2.1. Proyección obra de atravieso OA 01

Figura 3-3. Topografía de la zona de estudio de la obra OA 01, incluyendo una representación del camino

(color gris). Condición sin proyecto

8 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 2. MODELO HIDRÁULICO

PERMISO AMBIENTAL SECTORIAL 156
SISTEMA DE ALMACENAMIENTO DE ENERGÍA

ALTAIR

Figura 3-4. Topografía de la zona de estudio de la obra OA 01, incluyendo una representación del camino

(color gris). Condición con proyecto

9 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 2. MODELO HIDRÁULICO

PERMISO AMBIENTAL SECTORIAL 156
SISTEMA DE ALMACENAMIENTO DE ENERGÍA

ALTAIR

#### 3.2.2. Proyección obra de atravieso OA 02

Figura 3-5. Topografía de la zona de estudio de la obra OA 02, incluyendo una representación del camino y

pandereta (color gris). Condición sin proyecto

10 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 2. MODELO HIDRÁULICO

PERMISO AMBIENTAL SECTORIAL 156
SISTEMA DE ALMACENAMIENTO DE ENERGÍA

ALTAIR

Figura 3-6. Topografía de la zona de estudio de la obra OA 02, incluyendo una representación del camino y

cerco (color gris). Condición con proyecto

11 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 2. MODELO HIDRÁULICO

PERMISO AMBIENTAL SECTORIAL 156
SISTEMA DE ALMACENAMIENTO DE ENERGÍA

ALTAIR

Figura 3-7. Topografía de la zona de estudio del camino de la OA 02 (color gris). Condición sin proyecto

12 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 2. MODELO HIDRÁULICO

PERMISO AMBIENTAL SECTORIAL 156
SISTEMA DE ALMACENAMIENTO DE ENERGÍA

ALTAIR

Figura 3-8. Topografía de la zona de estudio del camino de la OA 02 (color gris). Condición con proyecto

#### 3.3. Coeficiente de rugosidad

Se estimó el coeficiente de rugosidad del cauce natural a partir del método de Cowan (MOP, 2023):

n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

n : coeficiente de rugosidad de Manning

m : coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : coeficiente asociado al material del lecho

n 1 : coeficiente asociado al grado de irregularidad del perímetro mojado

n 2 : coeficiente asociado a la variación de las secciones transversales

n 3 : coeficiente asociado al efecto relativo de las obstrucciones

n 4 : coeficiente asociado a la densidad de vegetación

13 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 2. MODELO HIDRÁULICO

PERMISO AMBIENTAL SECTORIAL 156
SISTEMA DE ALMACENAMIENTO DE ENERGÍA

ALTAIR

Los valores asociados a cada componente se obtuvieron según lo evidenciado en la ortofoto del proyecto

obtenida de un levantamiento LiDAR, presentada en la Figura 3-9, y las fotografías registradas en las visitas

a terreno, las cuales se muestran en la Figura 3-10 y la Figura 3-11. Finalmente, el cálculo de rugosidad basado

en estas imágenes se presenta en la Tabla 3-1.

Figura 3-9. Ortofoto de terreno en ubicación de las obras OA 01 y OA 02, incluyendo una representación

del layout (color negro)

14 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 2. MODELO HIDRÁULICO

PERMISO AMBIENTAL SECTORIAL 156
SISTEMA DE ALMACENAMIENTO DE ENERGÍA

ALTAIR

Figura 3-10. Registro fotográfico visita a terreno en ubicación de la obra OA 01

Figura 3-11. Registro fotográfico visita a terreno en ubicación de la obra OA 02

15 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 2. MODELO HIDRÁULICO

PERMISO AMBIENTAL SECTORIAL 156
SISTEMA DE ALMACENAMIENTO DE ENERGÍA

ALTAIR

Tabla 3-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.020|
|Grado de irregularidad del perímetro mojado|Leve|n1|0.005|
|Variación de las secciones transversales|Graduales|n2|0.000|
|Efecto relativo de las obstrucciones|Leve|n3|0.010|
|Densidad de vegetación|Baja|n4|0.010|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|Coeficiente de rugosidad|Coeficiente de rugosidad|n|0.045|

Para las obras proyectadas correspondientes a baden se asignó un valor de rugosidad igual a 0.025 basado

en valores tabulados en la literatura (Chow, 1994).

#### 3.4. Condiciones de borde e iniciales

Se definieron tres tipos de condiciones de borde (CB): (i) inicial o aguas arriba, (ii) intermedia y (iii) final o

aguas abajo. La CB de aguas arriba incorpora el caudal de la cuenca desde el inicio del área de interés. Por

otro lado, parte del modelo posee una longitud de cauce significativa y sus caudales pueden variar bastante

entre su inicio y final, ya que el área drenante de su cuenca aumenta a medida que se avanza hacia aguas

abajo. En estos casos se agrega una CB intermedia, cuyo objetivo es añadir un incremento de caudal al

modelo para representar el aumento del caudal a lo largo del cauce. Por último, se incluye la CB aguas abajo

para permitir la salida del flujo.

En resumen, las CB aguas arriba e intermedias incluyen parámetros de caudal en función de su ubicación a

lo largo del cauce. Además, las tres CB incorporan el parámetro de pendiente normal a partir de la topografía

del modelo. Todos los caudales están asociados a los periodos de retorno de diseño y verificación de las

obras, correspondientes a 100 y 150 años, respectivamente. Un resumen de las CB y su ubicación se presenta

en la Tabla 3-2 y en la Figura 3-12:

Tabla 3-2. Condiciones de borde e iniciales

|Nombre CB|CB aguas<br>arriba|CB interm.|CB aguas<br>abajo|Caudal de<br>diseño<br>[m3/s]|Caudal de<br>verificación<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|---|---|
|US_00|✅|||1.56|1.65|0.020|
|US_01||✅||0.25|0.26|0.014|

16 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 2. MODELO HIDRÁULICO

PERMISO AMBIENTAL SECTORIAL 156
SISTEMA DE ALMACENAMIENTO DE ENERGÍA

ALTAIR

|Nombre CB|CB aguas<br>arriba|CB interm.|CB aguas<br>abajo|Caudal de<br>diseño<br>[m3/s]|Caudal de<br>verificación<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|---|---|
|DS|||✅|-|-|0.010|

Figura 3-12. Ubicación condiciones de borde, layout (negro) y zona de refinamiento (rojo)

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 1 hora y

permanecen constantes por, a lo más, un periodo de 2 horas.

17 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 2. MODELO HIDRÁULICO

PERMISO AMBIENTAL SECTORIAL 156
SISTEMA DE ALMACENAMIENTO DE ENERGÍA

ALTAIR

Los hidrogramas de entrada utilizados para el modelo se muestran a continuación:

Figura 3-13. Hidrogramas de entrada. Crecida de diseño (100 años)

Figura 3-14. Hidrogramas de entrada. Crecida de verificación (150 años)

18 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 2. MODELO HIDRÁULICO

PERMISO AMBIENTAL SECTORIAL 156
SISTEMA DE ALMACENAMIENTO DE ENERGÍA

ALTAIR

#### 3.5. Otras consideraciones

En el modelo, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción SWE-ELM

en HEC-RAS 6.5). Además, el área de flujo se discretizó en celdas de 1.0 x 1.0 m. Se utilizó un paso de tiempo

de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15 y un

máximo de 0.40. Se consideró un tiempo de modelo de 3 horas para que el flujo entrara en régimen

permanente, con caudales de entrada iguales a los de salida, maximizando así su superficie inundada.

Adicionalmente, se consideró el refinamiento de la malla de cálculo a celdas de 0.2 x 0.2 m, en las zonas que

se muestran en la Figura 3-12 (con color rojo) para la situación Sin Proyecto. El objetivo de este refinamiento

es representar de mejor forma las características de la obra existente y solucionar algunas inestabilidades

numéricas del modelo.

#### 4. Resultados

A continuación, se presentan los resultados de profundidad y velocidad de inundación del modelo:

19 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 2. MODELO HIDRÁULICO

PERMISO AMBIENTAL SECTORIAL 156
SISTEMA DE ALMACENAMIENTO DE ENERGÍA

ALTAIR

#### 4.1. Condición sin proyecto

Figura 4-1. Profundidad máxima. Crecida de diseño (100 años). Condición sin proyecto

20 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 2. MODELO HIDRÁULICO

PERMISO AMBIENTAL SECTORIAL 156
SISTEMA DE ALMACENAMIENTO DE ENERGÍA

ALTAIR

Figura 4-2. Velocidad máxima. Crecida de diseño (100 años). Condición sin proyecto

21 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 2. MODELO HIDRÁULICO

PERMISO AMBIENTAL SECTORIAL 156
SISTEMA DE ALMACENAMIENTO DE ENERGÍA

ALTAIR

Figura 4-3. Profundidad máxima. Crecida de verificación (150 años). Condición sin proyecto

22 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 2. MODELO HIDRÁULICO

PERMISO AMBIENTAL SECTORIAL 156
SISTEMA DE ALMACENAMIENTO DE ENERGÍA

ALTAIR

Figura 4-4. Velocidad máxima. Crecida de verificación (150 años). Condición sin proyecto

23 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 2. MODELO HIDRÁULICO

PERMISO AMBIENTAL SECTORIAL 156
SISTEMA DE ALMACENAMIENTO DE ENERGÍA

ALTAIR

Figura 4-5. Hidrograma a la salida del modelo. Condición sin proyecto

24 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 2. MODELO HIDRÁULICO

PERMISO AMBIENTAL SECTORIAL 156
SISTEMA DE ALMACENAMIENTO DE ENERGÍA

ALTAIR

#### 4.2. Condición con proyecto

Figura 4-6. Profundidad máxima. Crecida de diseño (100 años). Condición con proyecto

25 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 2. MODELO HIDRÁULICO

PERMISO AMBIENTAL SECTORIAL 156
SISTEMA DE ALMACENAMIENTO DE ENERGÍA

ALTAIR

Figura 4-7. Velocidad máxima. Crecida de diseño (100 años). Condición con proyecto

26 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 2. MODELO HIDRÁULICO

PERMISO AMBIENTAL SECTORIAL 156
SISTEMA DE ALMACENAMIENTO DE ENERGÍA

ALTAIR

Figura 4-8. Profundidad máxima. Crecida de verificación (150 años). Condición con proyecto

27 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 2. MODELO HIDRÁULICO

PERMISO AMBIENTAL SECTORIAL 156
SISTEMA DE ALMACENAMIENTO DE ENERGÍA

ALTAIR

Figura 4-9. Velocidad máxima. Crecida de verificación (150 años). Condición con proyecto

28 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 2. MODELO HIDRÁULICO

PERMISO AMBIENTAL SECTORIAL 156
SISTEMA DE ALMACENAMIENTO DE ENERGÍA

ALTAIR

Figura 4-10. Hidrograma a la salida del modelo. Condición con proyecto

#### 4.3. Resumen de resultados

A continuación, se presenta un resumen de resultados de profundidad y velocidad en cada obra, incluyendo

los valores mínimo, máximo y promedio para la condición de diseño en la situación Sin y Con Proyecto.

#### 4.3.1. Obra de atravieso OA 01

Los resultados de la obra OA 01 fueron extraídos de un polígono de la obra en la zona inundada, como se

muestra en la Figura 4-11. El resumen de resultados de profundidad y velocidad se presenta en la Tabla 4-1

29 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 2. MODELO HIDRÁULICO

PERMISO AMBIENTAL SECTORIAL 156
SISTEMA DE ALMACENAMIENTO DE ENERGÍA

ALTAIR

Figura 4-11. Polígono obra OA 01 (color rojo) para los resultados de profundidad y velocidad

Tabla 4-1. Resultados de la obra OA 01

|Condición|Profundidad<br>[m]|Col3|Col4|Velocidad<br>[m/s]|Col6|Col7|
|---|---|---|---|---|---|---|
|Condición|Máximo|Media|Mínimo|Máximo|Media|Mínimo|
|Sin Proyecto|0.684|0.170|0.002|0.675|0.418|0.133|
|Con Proyecto|0.563|0.284|0.002|0.509|0.250|0.012|

#### 4.3.2. Obra de atravieso OA 02

Los resultados de la obra OA 02 fueron extraídos de un polígono de la obra en la zona inundada, como se

muestra en la Figura 4-12. El resumen de resultados de profundidad y velocidad se presenta en la Tabla 4-2.

30 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 2. MODELO HIDRÁULICO

PERMISO AMBIENTAL SECTORIAL 156
SISTEMA DE ALMACENAMIENTO DE ENERGÍA

ALTAIR

Figura 4-12. Polígono obra OA 02 (color rojo) para los resultados de profundidad y velocidad

Tabla 4-2. Resultados de la obra OA 02

|Condición|Profundidad<br>[m]|Col3|Col4|Velocidad<br>[m/s]|Col6|Col7|
|---|---|---|---|---|---|---|
|Condición|Máximo|Media|Mínimo|Máximo|Media|Mínimo|
|Sin Proyecto|0.864|0.603|0.243|0.323|0.136|0.013|
|Con Proyecto|0.86|0.56|0.01|0.45|0.14|0.01|

#### 4.3.3. Camino de acceso AB

Los resultados del camino de acceso fueron extraídos de un polígono en los tramos que se encuentran

cubiertos por la zona inundada, como se muestra en la siguiente Figura. El resumen de resultados de

profundidad y velocidad se presenta en la Tabla 4-3 y la Tabla 4-4.

31 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 2. MODELO HIDRÁULICO

PERMISO AMBIENTAL SECTORIAL 156
SISTEMA DE ALMACENAMIENTO DE ENERGÍA

ALTAIR

Tramo 2 Tramo 3

Figura 4-13. Tramos referenciales (color rojo) para los resultados de profundidad y velocidad

Tabla 4-3. Resultados del camino de acceso AB situación Sin Proyecto

|Tramos|Profundidad<br>[m]|Col3|Col4|Velocidad<br>[m/s]|Col6|Col7|
|---|---|---|---|---|---|---|
|Tramos|Máx.|Med.|Mín.|Máx.|Med.|Mín.|
|Tramo 1|0.228|0.096|0.001|0.237|0.101|0.002|
|Tramo 2|0.529|0.154|0.001|0.292|0.038|0.001|
|Tramo 3|0.712|0.226|0.001|0.110|0.043|0.002|

Tabla 4-4. Resultados del camino de acceso AB situación Con Proyecto

|Tramos|Profundidad<br>[m]|Col3|Col4|Velocidad<br>[m/s]|Col6|Col7|
|---|---|---|---|---|---|---|
|Tramos|Máx.|Med.|Mín.|Máx.|Med.|Mín.|
|Tramo 1|0.091|0.040|0.001|0.201|0.064|0.004|
|Tramo 2|0.045|0.021|0.001|0.232|0.032|0.002|
|Tramo 3|0.134|0.088|0.001|0.710|0.058|0.003|

32 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 2. MODELO HIDRÁULICO

PERMISO AMBIENTAL SECTORIAL 156
SISTEMA DE ALMACENAMIENTO DE ENERGÍA

ALTAIR

#### 5. Referencias

Chow, V. T. (1994). Hidráulica de canales abiertos. Colombia: McGraw-Hill.

HEC. (2024). HEC-RAS. Versión 6.5. HEC-RAS. Versión 6.5. Hydrologic Engineering Center. Obtenido de

https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2023). Manual de Carreteras. Volumen 3. Instrucciones y criterios de diseño. Ministerio de Obras

Públicas.

33 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

+56 9 5001 9945
[www.baqua.cl](https://www.baqua.cl/)

+56 9 5001 3096

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 2-1.: Descripción general de los modelos hidráulicos**

| Condición | Descripción | Objetivo |
| --- | --- | --- |
| Sin Proyecto | Representa la condición actual del cauce, en una extensión total de<br>420 m a lo largo de su eje, centrado en las obras proyectadas y<br>manteniendo más de 120 m hacia aguas arriba y hacia aguas abajo<br>desde el inicio y fin de cada obra proyectada.<br> <br>Este modelo incluye la representación de una obra existente (OE_01),<br>correspondiente a una pandereta compuesta por muros prefabricados<br>de hormigón de 1.8 m de alto, 2 m de largo y 2.5 cm de ancho. En la<br>zona del atravieso de cauce, posee una apertura de 1 m de alto y 2 m<br>de largo, sobre un muro de 0.3 m altura y 2 m de largo desde el fondo<br>del cauce.<br> | Representar<br>la<br>condición<br>actual<br>del<br>cauce |
| Con Proyecto | Representa la condición futura del cauce. Mantiene las características<br>del modelo Sin Proyecto, sin embargo la pandereta existente es<br>remplazada por un cerco perimetral y se incorporan las obras<br>proyectadas: (i) OA 01, correspondiente a un badén de mampostería<br>de piedra de sección compuesta con (a) una sección principal de base<br>15 m, altura variable entre 0.3 y 0.4 m, talud de 10:1 (H:V) y longitud<br>de 6.0 m, y (b) una sección secundaria con base de 2 m, altura variable<br>entre 0.4 y 0.5 m, talud de 10:1 (H:V) y longitud de 6.0 m; y (ii) OA 02, | Representar<br>la<br>condición<br>futura<br>del<br>cauce |

**Tabla 3-1.: Condición del cauce para el cálculo del coeficiente de Manning con método Cowan**

| Condición del cauce | Col2 | Símbolo | Valor |
| --- | --- | --- | --- |
| Material del lecho | Tierra | n0 | 0.020 |
| Grado de irregularidad del perímetro mojado | Leve | n1 | 0.005 |
| Variación de las secciones transversales | Graduales | n2 | 0.000 |
| Efecto relativo de las obstrucciones | Leve | n3 | 0.010 |
| Densidad de vegetación | Baja | n4 | 0.010 |
| Sinuosidad y frecuencia de meandros | Leve | m | 1.000 |
| Coeficiente de rugosidad | Coeficiente de rugosidad | n | 0.045 |

**Tabla 3-2.: Condiciones de borde e iniciales**

| Nombre CB | CB aguas<br>arriba | CB interm. | CB aguas<br>abajo | Caudal de<br>diseño<br>[m3/s] | Caudal de<br>verificación<br>[m3/s] | Pendiente<br>[m/m] |
| --- | --- | --- | --- | --- | --- | --- |
| US_00 | ✅ |  |  | 1.56 | 1.65 | 0.020 |
| US_01 |  | ✅ |  | 0.25 | 0.26 | 0.014 |

**Tabla 4-1.: Resultados de la obra OA 01**

| Condición | Profundidad<br>[m] | Col3 | Col4 | Velocidad<br>[m/s] | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Condición | Máximo | Media | Mínimo | Máximo | Media | Mínimo |
| Sin Proyecto | 0.684 | 0.170 | 0.002 | 0.675 | 0.418 | 0.133 |
| Con Proyecto | 0.563 | 0.284 | 0.002 | 0.509 | 0.250 | 0.012 |

**Tabla 4-2.: Resultados de la obra OA 02**

| Condición | Profundidad<br>[m] | Col3 | Col4 | Velocidad<br>[m/s] | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Condición | Máximo | Media | Mínimo | Máximo | Media | Mínimo |
| Sin Proyecto | 0.864 | 0.603 | 0.243 | 0.323 | 0.136 | 0.013 |
| Con Proyecto | 0.86 | 0.56 | 0.01 | 0.45 | 0.14 | 0.01 |

**Tabla 4-3.: Resultados del camino de acceso AB situación Sin Proyecto**

| Tramos | Profundidad<br>[m] | Col3 | Col4 | Velocidad<br>[m/s] | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Tramos | Máx. | Med. | Mín. | Máx. | Med. | Mín. |
| Tramo 1 | 0.228 | 0.096 | 0.001 | 0.237 | 0.101 | 0.002 |
| Tramo 2 | 0.529 | 0.154 | 0.001 | 0.292 | 0.038 | 0.001 |
| Tramo 3 | 0.712 | 0.226 | 0.001 | 0.110 | 0.043 | 0.002 |

**Tabla 4-4.: Resultados del camino de acceso AB situación Con Proyecto**

| Tramos | Profundidad<br>[m] | Col3 | Col4 | Velocidad<br>[m/s] | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Tramos | Máx. | Med. | Mín. | Máx. | Med. | Mín. |
| Tramo 1 | 0.091 | 0.040 | 0.001 | 0.201 | 0.064 | 0.004 |
| Tramo 2 | 0.045 | 0.021 | 0.001 | 0.232 | 0.032 | 0.002 |
| Tramo 3 | 0.134 | 0.088 | 0.001 | 0.710 | 0.058 | 0.003 |
